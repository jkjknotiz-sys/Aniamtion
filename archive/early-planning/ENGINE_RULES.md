# Engine Rules: reuse / extend / create

## Key diagnosis
The source repo is a **working Bridge episode** with a sophisticated look, not yet a generic scene engine. Some classes/functions are reusable but other files embed bridge, river, 74 soldiers, timing and town geometry. Port carefully.

## Source-to-target mapping (proposed, not implemented)
| Original | Target module | Strategy |
|---|---|---|
| `Bridge.tsx` | `engine/render/Composer.tsx` | Extract effects + render contract, no bridge data |
| `ink.ts` | `engine/post/InkPass.ts` | Preserve measured edge logic / NOINK layer contract |
| `lensblur.ts`, `grade.ts` | `engine/post/*` | Keep stages + resolution scaling |
| `shade.ts` | `engine/materials/ToonShade.ts` | Extract reusable material functions |
| `paint.ts` | `engine/materials/PaintedTextures.ts` | Move reusable brushes; add episode-specific recipes |
| `lights.ts` | `engine/lighting/Presets.ts` | Parametrize day / golden / storm etc |
| `toon.ts`, `cardshade.ts` | `characters/core/*` | Pen, face system, scene-lit cards |
| `cast.ts` | `characters/runtime/*` | Extract card pools & posing; move soldiers/roles to episode |
| `build.ts` | `world/kit/*` + `episodes/<id>/build.ts` | Keep generic builders; remove Broughton-specific buildings |
| `world.ts` | `world/SceneHost.ts` + episode/world | Sky/fog loops common; river/bridge specific |
| `story.ts` | `episodes/<id>/story.ts` | Camera utility shared, shots always episode data |

## Change policy
- REUSE: stable shaders, grading, billboarding, renderer; bug fixes need regression comparisons.
- EXTEND: light presets, materials, character face/expression methods through documented interfaces.
- CREATE: scene-specific geometry + animation + shots. Example: ship.ts, ocean.ts, storm.ts; city.ts, signage.ts, abandonedCars.ts.
- NEVER rewrite an entire proven module just to change story topic. Avoid silent fallback to crude geometry if assets fail.
- NEVER let two agents edit the same file simultaneously; designate owner and isolated worktree/branch.
- Maintain LICENSE and copyright notices for any MIT source copied.

## Incremental extraction contract
1. Take a reproducible baseline render of existing Bridge sample; save hashes, frames and settings. If baseline cannot run, document blocker; do not pretend equivalent.
2. Extract renderer only; rerender and compare representative frames, ensure no lost effects.
3. Extract lighting/material utils with snapshots; rerender.
4. Extract character runtime; rerender. Test turn/costume features separately.
5. Extract world host; rerender. Separate all Bridge object/timing constants.
6. New Empty City 4-second test. Then Storm Ship 4-second test.
7. Only mark reusable once **two very different scenes** render without changing core shader files.

## Interface sketch — design only, not an existing API
~~~ts
type EpisodeSpec = {
  id: string;
  aspect: [9, 16];
  fps: 30;
  characterIds: string[];
  shots: ShotSpec[];
  lightingPreset: "day" | "golden" | "night" | "storm" | "interior";
  buildScene: (context: SceneContext) => void;
  updateScene: (frame: number, context: SceneContext) => void;
};
~~~
Define/export `ShotSpec` and `SceneContext` during implementation; no production types are provided here.

## Evidence
Before approval, check visual regression, TS typecheck, render smoke test, asset loading, effects order, disk use and audio mapping. No automated score substitutes for human visual acceptance.