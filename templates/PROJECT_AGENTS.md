# Codex project instructions — Aniamtion Shorts

> **Copy/merge this file as `AGENTS.md` at the ROOT of your actual Remotion project.** It is intentionally stored in the Skill repo as `templates/PROJECT_AGENTS.md` so installing the Skill alone never overwrites an existing project's agent instructions.

When handling storyboards, 3D animation, video rendering or quality fixes **in this project**, use the `aniamtion-shorts` Skill already installed in the user's Codex skills directory.

## Always read before new work

1. `aniamtion-shorts/SKILL.md`
2. `aniamtion-shorts/references/PRODUCTION_QUALITY_STANDARD.md`
3. `aniamtion-shorts/references/FULL_SCENE_AND_CAST_STANDARD.md`
4. `aniamtion-shorts/references/LESSONS_RED_BUTTON_TOWN.md`
5. `aniamtion-shorts/references/OUR_STYLE_BIBLE.md`
6. Actual source/renderer code for this working Remotion project

Locate the installed Skill. If it cannot be found, report the path issue instead of silently inventing its content.

## Core intent

We are **adapting the process and existing source techniques of mromidev/claude-animated-shorts**, not building a new animation framework, not copying the original story/characters, and not writing throwaway prompts instead of code.

## Acceptance rules

- A topic alone is sufficient to PLAN: generate fact-checked original story (if factual), storyboard, original scene-specific geometry, character acting, lighting, camera and action specs.
- Have shot purpose, focal hierarchy, depth, acting, visual variety, material quality and an intentional reveal.
- **Every story-character counts:** parse the script into a cast table, including speaking supporting roles and visual extras. For each named actor, verify original design, rendering module, expression/acting, shot presence, staging, eye-lines and continuity. Do not simply duplicate Natee for everyone; Natee v2/v2-acting is not the entire cast.
- **Whole-scene look pass:** before full render deliver `CAST_BIBLE.md`, `SHOT_VISUAL_PLAN.md`, `SCENE_LOOK_REVIEW.md`; compare representative actual Render frames against matched references for motivated key/fill/rim lighting, color harmony, environment richness, foreground/midground/background, character-to-scene shading, props, composition and shot-to-shot consistency. Flag `CAST_MISSING`/`BLOCKED_VISUAL` for critical errors. Do not rely on a static-looking shot count.
- **Physical interactions are a blocking gate.** For each key press/pickup/door/lever/vehicle impact, prove anticipation → geometric contact → prop actuation → consequence → settle with multiple rendered frames. If billboard actors cannot do it, change the camera or create suitable local 3D parts; do not pretend a floating hand is a press.
- Before full rendering, render storyboard hero frames and a short motion proof of the hardest action. Show and fix the artistic failings. A correct MP4 is not necessarily a good-looking one.
- User-reviewable storyboard is a deliverable when requested. If the user asked to approve it, STOP before final video. Otherwise, proceed only after self-review gates PASS and flag subjective approval as pending.
- Preserve proven Bridge look code/shaders and original source. Make new `.ts/.tsx` for episode-specific worlds, props, camera, actor behavior and action mechanisms.
- Do not spend time reanalyzing previously studied rail/ship references unless a *specific* new evidence gap requires it.
- **Reuse the existing local Asset Library first**: inspect `ASSET_CATALOG.md`, `asset-manifest.json`, `src/asset-library/`, `public/asset-library/` when present. Do not download duplicate GLBs. Read entry license/bounds/style previews/readiness scope. The existing 36 GLBs passed technical *static scenery* tests; they are not automatically hero-closeup/rig/hand-contact-ready. If the shot needs articulated interaction, create and test the proper pivots/geometry/actor contact in scene code.
- For every shot list what catalog items are reused, what must be built, and what is unsuitable (wrong style/detail/rig). Validate in final shot context, not just asset showroom.
- Report artistic quality separately from technical video QA.

## Make improvements persist

On feedback such as "the pressing looks fake" or "the image is not attractive":
1. Find the problematic real code and frames. Do not just write another generic prompt.
2. Record a concrete failure in the episode's `PRODUCTION_REVIEW.md` with frame/time, visual observation, cause or hypothesis, changed code and validation evidence.
3. Fix, rerender matching frames and check the action's physical and cinematic result.
4. Propose an update to the Skill's reusable quality rules or case log where the lesson generalizes. Save approved changes locally and sync to the Git repository through the normal review/commit process.
5. If it is still not good enough, report `BLOCKED_VISUAL` or `BLOCKED_ACTION` instead of `APPROVED`.

**The most important distinction:** numeric frame checks and successful renders are technical evidence; good directing, credible motion and visual appeal require visual proof and user review.
