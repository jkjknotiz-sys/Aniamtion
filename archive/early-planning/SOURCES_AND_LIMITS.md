# Sources, attribution and limitations

## Sources
- Original public project: https://github.com/mromidev/claude-animated-shorts
- Original README: https://github.com/mromidev/claude-animated-shorts/blob/main/README.md
- Original SKILL: https://github.com/mromidev/claude-animated-shorts/blob/main/SKILL.md
- User-provided screenshots of X article from AI_DVD6 (6 steps: install, 4-second style proof, targeted fixes, script, voice-first, storyboard/full render): used as process inspiration, **not copied as full article**.
- User examples: Bridge, Empty City, railway, sailors videos discussed; current kit does not include/reproduce their media.

## Facts from original SKILL.md
- Bridge example uses Three.js + Remotion; flat character Canvas2D cards inside 3D scene.
- Character cards are on NOINK layer and use card shading.
- Frame effects: ink → lens pre → lens main → bloom → neutral tone map → grade.
- Source code organized around bridge-specific `story.ts`, `build.ts`, `cast.ts`, `world.ts`, plus common appearance modules.
- Original author uses comparative look checks, sandbox ownership, and frame QA.
- Original output goal 1440×2560; scripts mention 1080×1920 composition at 30 FPS and final scaling.
- Original reference frames supplied for **style study**, not redistribution.

## Recommendations invented for our future implementation (not part of original code)
- Proposed `engine/`, `characters/`, `world/`, `episodes/` folder architecture.
- New Character Bible and QA gates; Empty City pilot; reuse policy and hypothetical EpisodeSpec.
- New lighting presets and procedural asset libraries as future work.
- 4-second style test from the article, adapted to our repo.
- Numeric score thresholds intentionally not hard-coded; images and human review govern decisions.

## Current implementation status
- This repo contains **documentation/prompts/examples only**.
- No Three.js renderer, Remotion composition, new 3D character implementation, built video or tested integration is included.
- Before claiming performance or fidelity, copy code legally with notices, set up runtime, render Bridge regression, then two distinct new scenes.

## Licensing and safety
Original repository states code and docs MIT; verify LICENSE when copying code. Keep attribution and license notice. Do not redistribute original reference frames without separate permission. Use independently designed characters and scripts. Respect 3D asset licenses.