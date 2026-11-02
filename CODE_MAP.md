# CODE MAP — what the upstream files actually do

Source pinned to [mromidev/claude-animated-shorts](https://github.com/mromidev/claude-animated-shorts/tree/e3b817b6afc6cd413466d43f11ba31209e034bbf). Files in `templates/bridge/` are copied intact. Descriptions from source code inspection and upstream Skill, not a render verification.

| Source | Verified role | What to do on new topic |
|---|---|---|
| `Bridge.tsx` | Remotion composition, ThreeCanvas, world integration and post chain | Preserve and adapt per-episode composition without replacing effects |
| `ink.ts` | Custom edge-ink pass, world NOINK layer convention | Keep; regression-test edge visibility and order |
| `lensblur.ts` | Lens/DOF and film-grain implementation | Keep depth features, tune focus per shot |
| `grade.ts` | Color grade and shot presets | Tune palette, keep grade and exposure control |
| `lights.ts` | Day/golden light constants and atmospheric look | Adapt for nighttime/ships etc; don't freeze Bridge-only sun |
| `shade.ts` | Two-tone material shading / color helpers | Reuse unless model differs materially |
| `paint.ts` | Code-painted high-res textures with seams/material recipes | Reuse texture pattern technique; add new world materials |
| `toon.ts` | Canvas2D drawing and face expressions | Build our own original character designs using technique |
| `cardshade.ts` | Scene-light response for billboards | Preserve lit cards rather than emissive stickers |
| `cast.ts` | Soldier/town cast movement, card pools, expressions | Reuse technical methods, replace soldier choreography & roles |
| `build.ts` | Geometry primitives, batches, houses, kit props | Reuse generic geometry helpers, create detailed specific structures |
| `world.ts` | Bridge river/town scene, sky/fog, GLB loading, motion | Author new city/ship/train scene; keep shared principles |
| `story.ts` | Bridge-only frames, 15 shots, camera, impacts and DOF | Author NEW story timeline and camera movements |

## QA / analysis modules
- `templates/scripts/bridge-stills.mjs`: renders specified still frames. Has Windows Chrome path and BridgeShort ID hardcoded.
- `templates/scripts/bridge_shots.py`: parse **Bridge-specific** timeline source using regex; unsuitable for arbitrary new episodes without adapting.
- `templates/scripts/bridge_merge.py`: merge files from fixed agent-owned Bridge copies; adapt paths before use.
- `templates/scripts/sbs_sheet.py`: compare our images and approved references.
- `templates/scripts/short_qa.py`: analyze rendered video's technical defects and contact sheets.
- `scripts/analyze_references.py`: **new tool in our Skill** for numeric per-frame stats on local videos.
- `templates/audio/*.py`: original synthesis, mix and cues tools; original Bridge narration/events are not generic.

## What is missing for one-click rendering
Source repository is a **skill bundle, not a complete npm Remotion application**. This copy, too, lacks a runnable app scaffold, verified packages, and external GLB files expected at `public/bridge/kenney/*.glb`. These must be supplied/configured in local Remotion project. Avoid asserting that a Git clone by itself exports an MP4.

## Critical lesson from tutorial
Earlier notes guessed the camera hardly moved. The author's later frame-level correction found slow push-ins in more frames. Study methods must measure AND inspect. Never overstate motion estimates derived from phase correlation alone.
