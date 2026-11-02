# Asset Library status & how to reuse it (local Codex work; 2026-11-03)

## What has been verified by user's Codex report
The user's working Remotion project now has a **36-item static asset catalog**: 26 previously present Kenney Bridge assets + 9 selected from local Kenney packs + 1 adapted from Poly Haven. The report describes:
- 36/36 loaded by GLTFLoader with textures decoded and zero reported WebGL errors; styled using the existing Bridge twoTone/ink/lens/grade pipeline without modifying core shaders.
- 72 before/after preview stills, 3 gallery pages, a multi-object scenery test, and a 3-second (90-frame, 30 fps) technical motion test with a hinged door and rotating lever.
- Source mesh/triangle/bounds unchanged in static before-after renders; no silent replacement of original Bridge/Thai/storyboard files.
- Per-model provenance/license in a **local** `asset-manifest.json` with ID, file path, SHA256, source URL, material family, bounds, readiness scope, preview paths, and a `heroReady` indicator.
- Assets are reported CC0 in the user's local catalog; no GLBs or textures from this catalog have been uploaded to **this Skill repository** by this workflow.

**Important limitations:**
- "Ready" means technically **READY_STATIC_STYLE_TESTED** for scene dressing. It does NOT imply rigged character animation, wheels turning, grasp points, collision, physics or hero close-up quality.
- Kenney low-poly trees/props are most suitable in medium/background shots; hero closeups need extra geometry/material treatment.
- Poly Haven photo-detailed wooden crate may not match Kenney style despite adapter, requires shot-specific review.
- Door and lever motion test shows independent prop pivots, but blue contact marker is not an actor hand. No completed proof of real character-hand contact here.
- Quaternius Chair/Table not downloaded due quota; license conflict QAL vs older CC0 must be checked before use. Kenney Survival Kit was unavailable. Do not sidestep licensing/restrictions.
- For ships, trains, articulated mechanical structures, moving waves and interactive props, create/select episode-specific models and animation logic rather than pretending all are in the static library.
- Asset style parity with the user's reference videos remains **human-review pending**; technical rendering is not visual approval.

## How the Codex Skill MUST use the library when starting a new topic

1. Find the actual current Remotion project root. Search for `ASSET_CATALOG.md`, `asset-manifest.json`, `src/asset-library/`, and `public/asset-library/`. These were created in **the user's local project**, not inside this GitHub Skill. Inspect code exports and paths; never invent asset IDs or APIs.
2. Before new downloads/procedural creation, build a **shot-to-asset map**: shot ID → hero/mid/background object → reuse candidate → scale/bounds → material adapter → original file path → license → whether animation/rig/interaction is required.
3. Prefer catalog GLBs in medium/background shots and established Bridge-style materials. Do not blindly replace detailed hero props with a distant low-poly tree/crate. Preserve source identity and material semantics.
4. Where a shot needs moving props, identify if meshes have usable pivots/independent nodes. Animate only what the source supports; if no rig, author a tested scene-specific .ts animation or properly separate geometry.
5. For hands pressing buttons or grabbing things, test **world-space contact and deformation** in a short multi-frame render. The static library cannot prove interaction on its own.
6. Render the **actual storyboard hero frames**, not just an asset showroom. Check style, scale, silhouettes, shadows, readability, lighting and material mismatch at output size.
7. After producing a new asset legitimately, append catalog entry and tested previews, recording whether it is static medium/background, hero close-up ready or interactive and physically verified. Document rights/version/hashes.

**Do not download more models just to increase the 36 count.** The next production task should be a real episode that demonstrates deliberate selection and use of existing assets; obtain special-purpose assets only when the script requires them.

## Evidence limitation
This file summarizes user-provided `LIBRARY_REVIEW.md`, `asset-manifest.json` and screenshots. This Skill GitHub repo has not executed the 3-second MP4 independently; no claim of independent visual verification is made.
