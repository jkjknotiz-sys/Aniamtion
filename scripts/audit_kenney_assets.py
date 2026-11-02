#!/usr/bin/env python3
"""Audit the EXACT Kenney GLB filenames requested by upstream Bridge world.ts.

Standard-library only, read-only. Checks installed public assets for GLB v2
header + glTF JSON meshes, and finds same-name candidates in user-supplied
directories/ZIP packs. Does not download, copy, rename or alter models.
The scan does NOT prove that matching meshes have the same visual identity.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import struct
import zipfile
from collections import defaultdict
from pathlib import Path

EXCLUDED_DIRS = {".git", "node_modules", "dist", "build", ".next", ".tmp"}
SUPPORTED = {".glb", ".gltf", ".obj", ".fbx"}


def requested_names(world: Path) -> list[str]:
    src = world.read_text(encoding="utf-8")
    match = re.search(r"\bconst\s+KENNEY\s*=\s*\[(.*?)\]", src, re.S)
    if not match:
        raise ValueError(f"Cannot find const KENNEY = [...] in {world}")
    names = re.findall(r"""["']([^"']+)["']""", match.group(1))
    if not names:
        raise ValueError(f"No model names parsed in {world}")
    if len(set(names)) != len(names):
        raise ValueError("Duplicated model names in source; inspect manually")
    return names


def validate_glb_bytes(content: bytes, label: str) -> dict:
    """Inspect the binary glTF 2.0 header and its first JSON chunk."""
    issue = None
    result = {"path": label, "valid_glb": False, "meshes": 0, "materials": 0}
    if len(content) < 20 or content[:4] != b"glTF":
        issue = "Not a GLB file (invalid magic/too short)"
    else:
        _, version, declared_length = struct.unpack_from("<4sII", content, 0)
        if version != 2:
            issue = f"GLB version {version}, expected 2"
        elif declared_length != len(content):
            issue = f"GLB length header {declared_length} != file size {len(content)}"
        else:
            chunk_len, kind = struct.unpack_from("<I4s", content, 12)
            if kind != b"JSON" or 20 + chunk_len > len(content):
                issue = "Missing or damaged JSON chunk"
            else:
                try:
                    obj = json.loads(content[20:20+chunk_len].decode("utf-8").rstrip(" \x00"))
                    meshes = obj.get("meshes", [])
                    if not meshes:
                        issue = "GLB contains no meshes (not a usable visible model)"
                    else:
                        result["valid_glb"] = True
                        result["meshes"] = len(meshes)
                        result["materials"] = len(obj.get("materials", []))
                        result["images"] = len(obj.get("images", []))
                        result["external_uris"] = [
                            x["uri"] for group in ("images", "buffers") for x in obj.get(group, [])
                            if isinstance(x, dict) and "uri" in x
                            and not x["uri"].startswith("data:")
                        ]
                except (UnicodeError, json.JSONDecodeError, TypeError) as exc:
                    issue = f"Invalid JSON chunk: {exc}"
    if issue:
        result["issue"] = issue
    return result


def validate_glb_file(path: Path) -> dict:
    data = path.read_bytes()
    result = validate_glb_bytes(data, str(path))
    result["bytes"] = len(data)
    result["sha256"] = hashlib.sha256(data).hexdigest()
    return result


def candidates_in(pack: Path, needed: set[str]) -> tuple[list[dict], list[str]]:
    results, warnings = [], []
    if not pack.exists():
        return [], [f"Not found: {pack}"]
    if pack.is_file() and pack.suffix.lower() == ".zip":
        zips = [pack]
        files = []
    elif pack.is_dir():
        zips, files = [], []
        for folder, dirs, entries in __import__("os").walk(pack):
            dirs[:] = [d for d in dirs if d not in EXCLUDED_DIRS]
            for name in entries:
                p = Path(folder) / name
                if p.suffix.lower() == ".zip":
                    zips.append(p)
                elif p.suffix.lower() in SUPPORTED and p.stem.lower() in needed:
                    files.append(p)
    else:
        return [], [f"Unsupported pack path: {pack}"]
    for p in files:
        found = {"filename": p.name, "source": str(p), "format": p.suffix.lower()[1:]}
        if p.suffix.lower() == ".glb":
            try:
                found.update(validate_glb_file(p))
            except OSError as e:
                found["issue"] = str(e)
        results.append(found)
    for zp in zips:
        try:
            with zipfile.ZipFile(zp) as z:
                for item in z.infolist():
                    p = Path(item.filename.replace("\\", "/"))
                    if (not item.is_dir() and p.suffix.lower() in SUPPORTED
                            and p.stem.lower() in needed):
                        found = {"filename": p.name, "source": f"{zp}!{item.filename}",
                                 "format": p.suffix.lower()[1:], "compressed_bytes": item.compress_size}
                        if p.suffix.lower() == ".glb":
                            try:
                                found.update(validate_glb_bytes(z.read(item), found["source"]))
                            except (OSError, RuntimeError, ValueError) as e:
                                found["issue"] = str(e)
                        results.append(found)
        except (OSError, zipfile.BadZipFile, RuntimeError) as e:
            warnings.append(f"{zp}: {e}")
    return results, warnings


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--world", type=Path, default=Path(__file__).resolve().parents[1] / "templates/bridge/world.ts")
    ap.add_argument("--public-dir", type=Path, required=True,
                    help="Remotion app public dir (contains bridge/kenney/, not that folder itself)")
    ap.add_argument("--pack", type=Path, action="append", default=[],
                    help="One extracted pack directory or ZIP path; may repeat")
    ap.add_argument("--out", type=Path, required=True, help="Output JSON + Markdown report folder")
    args = ap.parse_args()

    names = requested_names(args.world)
    need = set(n.lower() for n in names)
    installed, matches, warnings = [], [], []
    for name in names:
        p = args.public_dir / "bridge" / "kenney" / f"{name}.glb"
        try:
            check = validate_glb_file(p) if p.is_file() else {
                "path": str(p), "valid_glb": False, "issue": "MISSING"
            }
        except OSError as e:
            check = {"path": str(p), "valid_glb": False, "issue": str(e)}
        check["name"] = name
        installed.append(check)

    for pack in args.pack:
        found, issues = candidates_in(pack, need)
        matches.extend(found)
        warnings.extend(issues)

    found_by_name = defaultdict(list)
    for item in matches:
        found_by_name[Path(item["filename"]).stem.lower()].append(item)
    status = []
    for item in installed:
        name = item["name"]
        candidates = found_by_name[name.lower()]
        status.append({
            "name": name,
            "installed_valid": item["valid_glb"],
            "installed_issue": item.get("issue"),
            "matching_pack_candidates": candidates,
            "candidate_count": len(candidates),
        })

    complete = all(row["installed_valid"] for row in status)
    output = {
        "world_source": str(args.world), "public_dir": str(args.public_dir),
        "pack_locations": [str(p) for p in args.pack],
        "required_count": len(names),
        "installed_valid_count": sum(row["installed_valid"] for row in status),
        "missing_or_invalid_count": sum(not row["installed_valid"] for row in status),
        "candidate_model_count": len(matches),
        "all_installed_valid": complete,
        "scope_note": (
            "Exact filename and GLB2 structural inspection only. This does not "
            "prove correct models, materials, CC0 provenance, visual matching or "
            "successful browser GLTFLoader fetch. Source ZIP pack may be a different version."
        ),
        "installed_files": installed,
        "status": status,
        "warnings": warnings,
    }
    args.out.mkdir(parents=True, exist_ok=True)
    (args.out / "kenney_asset_audit.json").write_text(
        json.dumps(output, indent=2, ensure_ascii=False), encoding="utf-8")
    lines = [
        "# Kenney asset audit (read-only)",
        "",
        f"Required: **{len(names)}** · Valid installed: **{output['installed_valid_count']}**",
        f"Missing/invalid: **{output['missing_or_invalid_count']}** · Pack candidates: **{len(matches)}**",
        "",
        "Note: a valid GLB header does NOT prove source/visual parity; inspect models and render.",
        "",
        "| Expected name | Installed | Matching candidate(s) in supplied packs |",
        "|---|---|---|",
    ]
    for row in status:
        valid = "VALID GLB" if row["installed_valid"] else f"MISSING/INVALID ({row['installed_issue']})"
        sources = "; ".join(str(x["source"]).replace("|", "\\|") for x in row["matching_pack_candidates"][:3])
        lines.append(f"| {row['name']}.glb | {valid} | {sources or 'none found'} |")
    if warnings:
        lines += ["", "## Scan warnings"] + [f"- {w}" for w in warnings]
    lines += ["", "## Next checks", "- Check exact mesh visuals and official pack version/license.",
              "- Confirm all 26 actual requests load as GLB with no 404s.",
              "- Compare Bridge frame 60 and 1350 (then transition frames) to approved references.",
              "- A model with different silhouette/material is NOT a faithful original asset."]
    (args.out / "KENNEY_ASSET_AUDIT.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"VALID {output['installed_valid_count']}/{len(names)}; candidates {len(matches)}")
    print(f"Reports: {args.out / 'KENNEY_ASSET_AUDIT.md'}")
    if not complete:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
