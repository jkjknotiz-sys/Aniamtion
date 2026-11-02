#!/usr/bin/env python3
"""Inspect every video frame numerically and make two-second contact sheets.

This is an ORIGINAL, standalone reference-study helper for Aniamtion Shorts,
not an upstream script and not a complete AI vision/camera-tracking solution.

Install: python -m pip install opencv-python-headless numpy Pillow
Usage:
    python scripts/analyze_references.py --input /path/to/videos --out /path/to/study
    python scripts/analyze_references.py --input short.mp4 --out study --max-videos 1

Outputs:
    <out>/<NN_name>/frame_metrics.csv, summary.json, sheets/*.jpg
    <out>/collection_summary.json
Each source frame is read and analyzed; contact sheets organize ~2 seconds of
source footage per image (60 frames when the source is 30fps).
"""
from __future__ import annotations

import argparse
import csv
import json
import math
import re
import statistics
from pathlib import Path

import cv2
import numpy as np
from PIL import Image, ImageDraw

VIDEO_EXTS = {".mp4", ".mov", ".mkv", ".webm", ".avi", ".m4v"}
CSV_FIELDS = (
    "frame", "time_seconds", "luma_mean", "luma_std", "saturation_mean",
    "edge_fraction", "frame_diff", "histogram_distance",
    "image_shift_x_px", "image_shift_y_px", "shift_response",
    "candidate_cut",
)


def find_videos(source: Path) -> list[Path]:
    if source.is_file() and source.suffix.lower() in VIDEO_EXTS:
        return [source]
    if source.is_dir():
        return sorted(p for p in source.rglob("*") if p.is_file() and p.suffix.lower() in VIDEO_EXTS)
    raise ValueError(f"Not a supported video or directory: {source}")


def safe_name(name: str) -> str:
    clean = re.sub(r"[^a-zA-Z0-9._-]+", "_", name).strip("._")
    return clean[:70] or "video"


def make_sheet(items: list[tuple[int, Image.Image]], dest: Path, fps: float) -> None:
    if not items:
        return
    cols = 6
    thumb_w, thumb_h, label_h, pad = 116, 206, 24, 7
    rows = math.ceil(len(items) / cols)
    sheet = Image.new("RGB", (cols * (thumb_w + pad) + pad, rows * (thumb_h + label_h + pad) + pad), "#e8e8e8")
    draw = ImageDraw.Draw(sheet)
    for index, (frame_id, raw) in enumerate(items):
        x = pad + (index % cols) * (thumb_w + pad)
        y = pad + (index // cols) * (thumb_h + label_h + pad)
        img = raw.copy()
        img.thumbnail((thumb_w, thumb_h), Image.Resampling.LANCZOS)
        sheet.paste(img, (x + (thumb_w - img.width) // 2, y + (thumb_h - img.height) // 2))
        draw.text((x + 2, y + thumb_h + 3), f"f{frame_id}  {frame_id/fps:.2f}s", fill="#202020")
    dest.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(dest, quality=86, optimize=True)


def avg(rows: list[dict], key: str) -> float:
    return round(float(statistics.mean(r[key] for r in rows)), 6) if rows else 0.0


def analyze_one(video: Path, directory: Path) -> dict:
    cap = cv2.VideoCapture(str(video))
    if not cap.isOpened():
        raise RuntimeError(f"OpenCV could not read video: {video}")
    fps = float(cap.get(cv2.CAP_PROP_FPS))
    fps_reported = fps > 0 and math.isfinite(fps)
    if not fps_reported:
        fps = 30.0  # only a fallback for timestamps/sheet grouping, reported below
    reported_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frames_per_sheet = max(1, round(2 * fps))

    directory.mkdir(parents=True, exist_ok=True)
    sheets_dir = directory / "sheets"
    csv_path = directory / "frame_metrics.csv"

    rows: list[dict] = []
    sheet_items: list[tuple[int, Image.Image]] = []
    prev_gray = None
    prev_hist = None
    hann = None
    frame_idx = 0
    candidates = []
    sample_width = 180

    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=CSV_FIELDS)
        writer.writeheader()
        while True:
            ok, frame = cap.read()
            if not ok:
                break
            h, w = frame.shape[:2]
            scaled_h = max(16, round(h * sample_width / max(w, 1)))
            small = cv2.resize(frame, (sample_width, scaled_h), interpolation=cv2.INTER_AREA)
            gray_uint8 = cv2.cvtColor(small, cv2.COLOR_BGR2GRAY)
            gray = np.asarray(gray_uint8, dtype=np.float32)
            hsv = cv2.cvtColor(small, cv2.COLOR_BGR2HSV)
            sat = float(hsv[:, :, 1].mean() / 255.0)
            luma = float(gray.mean() / 255.0)
            contrast = float(gray.std() / 255.0)
            edge = float(np.mean(cv2.Canny(gray_uint8, 80, 160) > 0))
            hist = cv2.calcHist([gray_uint8], [0], None, [32], [0, 256])
            cv2.normalize(hist, hist, 1.0, 0.0, cv2.NORM_L1)

            diff, dist, dx, dy, response = 0.0, 0.0, 0.0, 0.0, 0.0
            if prev_gray is not None:
                diff = float(np.mean(np.abs(gray - prev_gray)) / 255.0)
                dist = float(cv2.compareHist(prev_hist, hist, cv2.HISTCMP_BHATTACHARYYA))
                if hann is None:
                    hann = cv2.createHanningWindow((gray.shape[1], gray.shape[0]), cv2.CV_32F)
                try:
                    (dx, dy), response = cv2.phaseCorrelate(prev_gray, gray, hann)
                    if not all(math.isfinite(v) for v in (dx, dy, response)):
                        dx, dy, response = 0.0, 0.0, 0.0
                except cv2.error:
                    dx, dy, response = 0.0, 0.0, 0.0
            # Conservative candidate, NOT proof of a hard cut. Flashes and large motion may trigger.
            is_cut = int(frame_idx > 0 and ((diff > 0.23 and dist > 0.28) or diff > 0.42))
            if is_cut:
                candidates.append(frame_idx)
            row = {
                "frame": frame_idx,
                "time_seconds": round(frame_idx / fps, 5),
                "luma_mean": round(luma, 6),
                "luma_std": round(contrast, 6),
                "saturation_mean": round(sat, 6),
                "edge_fraction": round(edge, 6),
                "frame_diff": round(diff, 6),
                "histogram_distance": round(dist, 6),
                "image_shift_x_px": round(float(dx), 4),
                "image_shift_y_px": round(float(dy), 4),
                "shift_response": round(float(response), 5),
                "candidate_cut": is_cut,
            }
            writer.writerow(row)
            rows.append(row)
            prev_gray = gray
            prev_hist = hist

            # Contact sheet review works on ALL source frames, not one frame every few seconds.
            # Thumbnail storage is bounded to one sheet at a time.
            sheet_items.append((frame_idx, Image.fromarray(cv2.cvtColor(small, cv2.COLOR_BGR2RGB))))
            if len(sheet_items) >= frames_per_sheet:
                make_sheet(sheet_items, sheets_dir / f"sheet_{frame_idx // frames_per_sheet:05d}.jpg", fps)
                sheet_items.clear()
            frame_idx += 1

    cap.release()
    if sheet_items:
        make_sheet(sheet_items, sheets_dir / f"sheet_{(frame_idx - 1) // frames_per_sheet:05d}.jpg", fps)
    if frame_idx == 0:
        raise RuntimeError(f"No decoded frames in {video}")
    summary = {
        "source": str(video),
        "fps": fps,
        "fps_read_from_metadata": fps_reported,
        "frames_decoded": frame_idx,
        "frames_reported_by_container": reported_count,
        "seconds_estimate": round(frame_idx / fps, 3),
        "contact_sheet_count": math.ceil(frame_idx / frames_per_sheet),
        "frames_per_sheet": frames_per_sheet,
        "mean_luma": avg(rows, "luma_mean"),
        "mean_contrast": avg(rows, "luma_std"),
        "mean_saturation": avg(rows, "saturation_mean"),
        "mean_edge_fraction": avg(rows, "edge_fraction"),
        "mean_frame_difference": avg(rows, "frame_diff"),
        "candidate_cut_frames": candidates,
        "motion_note": (
            "Phase-correlation shifts are estimates of WHOLE-IMAGE translation "
            f"in a {sample_width}px-wide thumbnail. Character motion, parallax, blur, "
            "lighting and cuts make them unreliable as camera-motion ground truth. "
            "Inspect consecutive frames and source footage manually."
        ),
        "cut_note": "Candidate cuts are a visual-review queue; not confirmed hard cuts.",
        "review_note": "Numbers cover decoded source frames. Contact sheets are for vision/human inspection, not automatic video understanding.",
    }
    (directory / "summary.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description="Numerically analyze every frame and export ~2-second contact sheets.")
    parser.add_argument("--input", required=True, type=Path, help="A video file or folder containing videos")
    parser.add_argument("--out", required=True, type=Path, help="Output folder (do not commit third-party frames)")
    parser.add_argument("--max-videos", type=int, default=0, help="0=all; positive value limits batch size")
    args = parser.parse_args()

    videos = find_videos(args.input)
    if args.max_videos > 0:
        videos = videos[:args.max_videos]
    if not videos:
        parser.error(f"No supported videos found inside {args.input}")
    args.out.mkdir(parents=True, exist_ok=True)
    combined = []
    failures = []
    for index, video in enumerate(videos, 1):
        out = args.out / f"{index:02d}_{safe_name(video.stem)}"
        print(f"[{index}/{len(videos)}] {video}", flush=True)
        try:
            result = analyze_one(video, out)
            combined.append(result)
            print(f"  analyzed {result['frames_decoded']} frames -> {out}", flush=True)
        except (RuntimeError, OSError, ValueError, cv2.error) as exc:
            failures.append({"source": str(video), "error": str(exc)})
            print(f"  FAILED: {exc}", flush=True)
    (args.out / "collection_summary.json").write_text(
        json.dumps({"videos": combined, "failures": failures}, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    if failures:
        raise SystemExit(f"Finished with {len(failures)} failure(s). See collection_summary.json")


if __name__ == "__main__":
    main()
