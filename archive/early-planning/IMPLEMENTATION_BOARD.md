# IMPLEMENTATION BOARD — งานที่ต้องทำและวิธีตรวจรับ

> ไม่ใช่ Prompt; ใช้เป็น task/acceptance board สำหรับงานพัฒนาจริง สถานะเริ่มต้นยังไม่ได้ implement

## Milestone 0 — Baseline
- [ ] Clone/inspect `mromidev/claude-animated-shorts` และ dependencies
- [ ] Set up separate working Remotion project (Node/Python/ffmpeg/asset paths)
- [ ] Render Bridge original golden frames + record parameters
- [ ] Diagnose Empty City import/effect pipeline from actual source (if provided)
**Evidence:** screenshot contacts, dependency manifest, baseline render QA

## Milestone 1 — Reusable Core
- [ ] Extract bridge post composer without changing appearance
- [ ] Verify Ink/DOF/Bloom/grade order + scaling
- [ ] Extract shared light/material/painted texture utilities with presets
- [ ] Extract WorldHost/Camera without Bridge hardcoding
- [ ] Run Bridge visual regression after every extraction
**Evidence:** build/typecheck; side-by-side baseline sample; visible matched outlines and subject shadows

## Milestone 2 — Original Character
- [ ] Approve original design, silhouettes, expressions and costumes
- [ ] Implement scene-lit character card runtime and consistent contact shadow
- [ ] Test character in daylight + storm + close/wide + multiple costumes
- [ ] Add 3D rig support only if needed for continuous full-turn movement
**Evidence:** identity sheet, test frames from two lighting settings

## Milestone 3 — Cross-Topic Scenes
- [ ] Empty City scene-specific modules and assets
- [ ] Storm Ship scene-specific modules and assets
- [ ] 120-frame animated proof and 8+ keyframes each
- [ ] Verify both reuse same renderer, post and character systems
- [ ] Owner signs off visual consistency vs approved baselines
**Evidence:** pilot MP4s and QA reports; no fallback low-detail boxes in final hero views

## Milestone 4 — Full Short
- [ ] Original fact-checked script
- [ ] Voice WAV and hand-checked Thai or English timings
- [ ] Storyboard and production shots
- [ ] Render complete 9:16 MP4 at 30fps with proper SFX/music
- [ ] Technical QA plus human approval
- [ ] Capture reusability: assets, source modules, instructions and rights
**Evidence:** final MP4, Git commit, build scripts, updated episode files, QA report

## Current truth
These checkboxes are unchecked because this repository presently holds planning documents, not the production implementation. Do not report progress that cannot be demonstrated by committed code and rendered video.
