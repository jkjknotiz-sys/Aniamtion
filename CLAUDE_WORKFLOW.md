# Claude Code workflow — from brief to MP4

## Gate 0: inventory & safety
Read current project tree / package scripts / Remotion compositions and LICENSE. Confirm local paths; do not assume repo kit contains runtime. Work on new branch/episode folder. Record baseline render settings and asset provenance.

## Gate 1: research / narrative
Create `episode/FACTS.md` with each factual claim and source, `SCRIPT.md` with hook → setting → escalation → pivot → payoff. Verify data before scripting. For Thai: avoid enforcing English word/second target.

## Gate 2: approved character & environment
Load CHARACTER_BIBLE and approved palette, make SCENE_SPEC per shot: focal point, background, geometry, textures, motion, weather, foreground. Identify asset reuse vs missing assets; define file ownership for new .ts modules.

## Gate 3: voice-first
Generate/record `voice.wav`, transcript and word/phrase timing (Thai needs tested segmentation, manually corrected). Lock timeline after signoff. Use event table for sound; avoid timing mismatch in render.

## Gate 4: storyboard stills
Create 8–12 keyframes across hooks, peaks and twist; include far/wide, medium, close/insert. Review colors, outlines, composition and props before committing to full animation.

## Gate 5: 4-second style test
Make 120 frames at 30fps in a new composition (or 3–5s if timing demands); render sample and stills. Ask reviewer for specific defects with frame numbers. Iterate after each targeted fix, without modifying unrelated modules. No full render before pass.

## Gate 6: implementation
Generate scene/episode-specific .ts for required environments, actor logic, shot paths; reuse engine. Typecheck. Verify textures and asset paths, depth buffers, NOINK, post order, movement with frame-level review. Lock picture timing before final audio mix.

## Gate 7: QA and delivery
Use QA_CHECKLIST.md. Run technical checks (duration, fps, dimensions, silent/black/white/frozen frames, clipping, subtitles, audio loudness) and human review of hero frames. Render final 9:16 MP4 via actual configured composition and settings; version project and log issues in `QA_REPORT.md`.

## Optional parallel agent plan
- research owns FACTS/SCRIPT; character owns character files; world owns scene-specific build/material recipes; camera owns timeline; post owns core effect fixes **only with documented approval**; QA read-only.
- Each agent works in its own copy/branch; merge validated changes sequentially.

## Stop conditions
Missing source rights; broken asset paths; unapproved character design; post effects missing; plain boxes used as final environment; major frame glitches; voice timing inconsistent; 4s test fails. Report the blocker and fix before further rendering.

## Example final commands (adapt to real project)
~~~bash
npx tsc --noEmit
npx remotion compositions src/index.ts
npx remotion render src/index.ts <EXISTING_COMPOSITION_ID> out/episode.mp4 --codec h264 --crf 16
ffprobe -v error -show_entries format=duration -of json out/episode.mp4
~~~
Do not run example commands without checking actual entry point, composition and package dependencies.