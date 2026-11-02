# Claude Code Prompt — Extract a reusable studio engine from Bridge

~~~text
Inspect the real source repo and installed local Remotion project BEFORE modifying files. Create new branch work/engine-extraction and record baseline Bridge render/stills/commit and legal license notices.

Step A: map file imports and dependencies of Bridge.tsx, ink.ts, lensblur.ts, grade.ts, shade.ts, paint.ts, lights.ts, toon.ts, cardshade.ts, cast.ts, world.ts, build.ts and story.ts. Identify bridge-specific constants vs truly generic functions; provide table and risks.

Step B: extract the render/post pipeline as a reusable wrapper WITHOUT changing image output. Make before/after still comparisons. Verify effect order and resolution scaling.

Step C: extract light/material/character utilities behind versioned interfaces; preserve NOINK and cardshade, shadow/contact; visual regression test after each extraction.

Step D: extract WorldHost / scene hooks. Place bridge object builders and timeline under episodes/bridge rather than in core. Retain original working project as baseline.

Step E: implement two independent 4-second pilots, Empty City and Storm Ship, each with new scene TS assets, no reimplementation of core post renderer. Compare visual art direction, not identical colors/sun angles.

For each step: report files changed, typecheck/test commands, still paths, differences and PASS/FAIL. Stop when regression occurs; revert or repair before proceeding. Do not refactor everything in one giant change. Do not modify third-party reference assets.
~~~