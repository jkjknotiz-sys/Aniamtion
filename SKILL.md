---
name: aniamtion-shorts
description: Create and direct polished original stylized animated shorts using the proven Three.js/Remotion bridge techniques, reference-study reports, original characters and reusable scene code. Mandatory storyboarding, believable physical interactions (hands touching buttons, props responding, actor continuity), cinematic composition, render-and-critique quality gates, and learning from failed user-reviewed episodes. Use for animation video topics, storyboards, production and improvement of shorts.
---

# Aniamtion Shorts — source-grounded skill

**Goal:** reproduce the *method* shown by mromidev/claude-animated-shorts and adapt it for original stories, our own recurring characters, and new worlds. This is a source-backed Agent Skill usable by Codex, with upstream MIT source templates and analysis/QA scripts; **it is not a new animation framework**.

For persistent use inside a Remotion project, copy/merge `templates/PROJECT_AGENTS.md` into the project's root as `AGENTS.md`; this project-level instruction does not replace the Skill. Never overwrite an existing AGENTS.md without merging.

Read this file first, then:
- `README.md` for installation and what is included;
- `CODE_MAP.md` for exact source responsibilities and what changes between episodes;
- `references/OUR_STYLE_BIBLE.md` for **our provisional evidence-based rail/ship study**; ask the user to approve hero references before using its candidate art directions as fixed rules;
- `references/STYLE_BIBLE.md` and `references/reports/*.md` for the upstream study (do not conflate their 20-video measurements with our two-video study);
- `templates/bridge/*.ts`, `templates/bridge/Bridge.tsx` for actual proven example code;
- `templates/scripts/*.py` for frame comparison and QA;
- `scripts/analyze_references.py` for analyzing your own locally available example videos.
- `scripts/audit_kenney_assets.py` for read-only inspection of exact Kenney GLB files expected by `world.ts`, and same-name candidates inside downloaded official ZIP/pack directories; NEVER assume a filename match proves visual equivalence.
- `references/BRIDGE_RENDER_DIAGNOSTIC_TH.md` for the **user-verified** Remotion readiness bug, isolated compatibility fix, and originally missing 26 GLBs (user later restored all 26 in their local project; files aren't packaged here).
- **MANDATORY on EVERY new episode:** `references/PRODUCTION_QUALITY_STANDARD.md` — physical contact/acting, cinematic art direction, storyboard, reveal contract, quality gates and learning loop.
- **MANDATORY known failure case:** `references/LESSONS_RED_BUTTON_TOWN.md` — 12-shot button/toy-town storyboard with user-reported implausible button press and insufficient visual appeal. Apply *generalized rules*, not the episode's props/story.
- **MANDATORY whole-scene and casting standard:** `references/FULL_SCENE_AND_CAST_STANDARD.md` — audit every actor in the script, not only Natee; stage ensemble blocking, lighting/color script, shot composition and reference-matched visual review.
- **MANDATORY asset-library lesson:** `references/ASSET_LIBRARY_STATUS_TH.md`. Use the **local** project `asset-manifest.json`, `ASSET_CATALOG.md` and `src/asset-library/` if they exist, before building/downloading any assets. Confirm exact paths and import APIs by inspecting the user's actual project; do not assume the asset files live inside the Skill repository.

## Non-negotiable constraints

1. **Reference precedence:** our approved user style evidence outranks generic upstream look targets when building new episodes; the current OUR_STYLE_BIBLE is provisional, based on 2 videos and not yet human-approved. Missing external local assets such as `review_manifest.json`, `reports/methodology.md`, `evidence/01` and `evidence/02` must not be invented.
2. **Source-first, not prompt-first.** Open the real modules, inspect symbols and dependencies, and render actual frames. No guesses about assets or exports.
3. **Never pretend the bridge template is a generic scene engine.** `world.ts`, `build.ts`, `cast.ts` and `story.ts` contain bridge/town/soldier logic. A new topic needs appropriate geometry, painted materials, props, movements and camera staging, often in NEW .ts modules.
4. **Keep the look code until proven otherwise.** Original drawing/shader/effects in `toon.ts`, `cardshade.ts`, `shade.ts`, `paint.ts`, `ink.ts`, `lensblur.ts` and `grade.ts` are a baseline. Verify which utilities are reusable; do not rewrite all of them just because story changed.
5. **Original people and stories.** Study references for measurable techniques, not for copying distinctive designs/shots or distributing private video frames. Original source licensed MIT (retain LICENSE).
6. **Human quality gate.** A video is not 'finished' because a render succeeded or an agent gave it a good score.
7. **No silent broad fallback.** If a required GLB/detail asset is missing, report it and obtain/author legal equivalents rather than finishing with unpainted block geometry.
8. **No false 'watched all frames' claims.** The scripts process every frame numerically; human/LLM image review normally happens through sampled/contact-sheet images. Explain the distinction.
9. **Technical success is not artistic success.** Rendering 12 storyboards or 54 seconds without missing frames does not mean the action reads, the story is cinematic, or the user approves. A real button press must show contact/depression/consequence on sequential frames. Physical plausibility still matters in fantasy scenes.
10. **Mandatory acceptance gates.** Apply Gate 0→4 in `references/PRODUCTION_QUALITY_STANDARD.md`. Stop before full render if `BLOCKED_STORY`, `BLOCKED_ACTION` or `BLOCKED_VISUAL`; do not rubber-stamp an attractive-looking static storyboard as a moving action test.
11. **Whole-scene and cast coverage.** Every scripted named character must have an original identifiable design, code/asset, animation capacity and rendered evidence. Plan lighting, color, blocking and composition for every shot, not just the main actor; apply `references/FULL_SCENE_AND_CAST_STANDARD.md` before storyboard approval and full rendering.
12. **Persistent learning.** When user rejects visuals, first record a concrete failure case and an observable regression test; update reusable Skill rules only for generalizable findings, and never claim a visual improvement was proven without before/after renders.

## Exact production workflow (derived from the original example + the tutorial)

### Stage A — study our approved references once, deeply

- Collect a chosen batch of accessible videos (with rights to use for private study). Keep raw files off GitHub unless licensed.
- Run `python scripts/analyze_references.py --input <video_or_folder> --out <study-folder>`. Use `--help` for optional settings. Record frame-level brightness/contrast/saturation, edge density, difference scores, tentative cut candidates and phase-correlation shifts. This is **not** a perfect camera motion estimator.
- Inspect the 2-second contact sheets (60 frames at 30fps), relevant frame pairs, and full speed playback for motion subtleties. The original creator studied 20 videos, but our input count should be what we actually have.
- Have specific specialist reviews for motion, character ratios, ink, material texture, light, depth, color and camera; write each report with observable evidence, measurements, frame IDs, uncertainty.
- Build **our** `references/OUR_STYLE_BIBLE.md` and a small set of approved hero reference frames. Do not overwrite or blindly adopt upstream measurements. An original upstream camera summary underestimated subtle movement and was revised after further review.

### Stage B — reproduce source Bridge baseline before new story

- Read `upstream/SKILL.md` and `README.md`. Integrate `templates/bridge/` in a compatible local Three.js + Remotion project, register `BridgeShort` and match needed assets and scripts. This repository alone lacks a fully assembled app and local third-party GLBs.
- Capture 8+ stills from varied shots and one playable test. Save the settings, dimensions, engine dependency versions, asset manifest and comparison sheet.
- Understand post chain: **ink → lens pre → lens main → bloom → neutral tone map → grade**; characters are card billboards excluded from world-ink via `NOINK` and lit using `cardshade.ts`.
- Do NOT refactor the entire renderer before establishing a working baseline.

### Stage C — direct and design a NEW episode, not a copied Bridge

- **Start by reading the mandatory quality rules and previous failure case.** User can supply only a topic; plan story, storyboard, camera, actions, scene code and QA from it. If user requests storyboard approval, stop before full animation.
- Research and verify factual story; use a paradox hook, escalating beats, pivot/mechanism and payoff where appropriate, but write original script with user's chosen language.
- **For story twists:** write a reveal contract (what audience believes, allowed clues, forbidden early reveals, payoff frame/shot). Don't accidentally show the giant hand/miniature scale before it should become apparent.
- **For each important action:** specify world-space actor/prop scale and contact location, anticipation, first touch, force/deformation, response and follow-through. If a 2.5D billboard cannot show a convincing hand interaction, create the required original 3D hand/prop geometry or use an honest camera angle; never fake contact via sound alone.
- Produce narration first, then timing map; align reaction/camera changes to narration.
- **Script breakdown MUST include all cast**: generate `CAST_BIBLE.md` and `SHOT_VISUAL_PLAN.md` per `references/FULL_SCENE_AND_CAST_STANDARD.md`. Identify named supporting actors, reactions, extras, world locations and shared light/scale. Natee v2 acting (if present in local project) is one reusable character, not the default actor for every story role. Create original character variants and suitable .ts drawing/pose assets for others as needed.
- **Asset-first without sacrificing quality:** inspect local `asset-manifest.json`, `ASSET_CATALOG.md`, `src/asset-library/` and original episode assets. Match each planned shot to real catalog entries, their source bounds/scale, license, material adapter, preview and *readiness scope*. Reuse verified styled GLBs for suitable environment/medium/background scenes. **Do not treat a static GLB as rigged/interactive**, and never call a Kenney low-poly model hero-closeup-ready just because it renders. For close hero shots or character-object interactions, author/select appropriate geometry, pivot, rig/animation and contact solution. If no catalog exists, describe what is missing; don't invent catalog IDs. Do not download the same assets again.
- Plan scene/shot camera geometry and list assets **specific to the new subject**, plus the focal story intent, visual hierarchy, purposeful camera variety, actor gaze/gesture, motivated lighting, atmospheric depth, foreground/midground/background staging, legible text and readable physical interactions. Avoid repeating nearly identical framing where it adds no story value. Examples:
  - Empty City: city facades, window bays, shop signs, street markings, cars, neglected props, traffic lights, original character; building and material recipes.
  - Storm Ship: hull, mast, sails, rigging, water, spray, sky/fog, ship roll and reaction animations.
- Copy proven template into a NEW episode folder in local Remotion project. Inspect and adapt `story.ts`, `build.ts`, `world.ts` and `cast.ts` with topic-specific .ts/.glb as required; adapt lighting presets to story context without losing shading/post rules.
- Reuse original character-runtime ideas, but design **independent recurring characters**. 2D lit cards in 3D are 2.5D; switch to fully rigged 3D only if the shot needs it.

### Stage D — look-match + physical-interaction loop (what made original good)

1. Render representative storyboard stills **before full video**, including varied shot types; do not mark them approved based on number alone. For physical actions render a time-sequenced strip with at least anticipation, contact, full actuation and consequence; show that the button physically depresses, a door pivots on a hinge, a hand actually holds an object, etc.
2. Put our frames against approved *shot-compatible* style/reference examples with `templates/scripts/sbs_sheet.py` (local paths). Inspect ink, hue, contrast, silhouette, shadow, texture grain, depth, camera framing and actor anatomy. Check whether the action is physically legible, characters react, Thai signs/subtitles are accurate, and whether the aesthetic is compelling — not merely technically complete.
3. Log failures as frame number → observed issue → measured delta → suspected cause → source file/function → owner.
4. Delegate by **file ownership**, separate branches/sandboxes. Example: cam owns story; world owns world/build; character owns toon/cast/cardshade; post owns ink/lensblur/grade. Avoid concurrent edits to the same source.
5. Re-render changed frames and compare. The original found an ink pass accidentally overwritten by blur, over-thick limbs, too-flat materials and too-snappy camera moves. Diagnose actual issues instead of assuming identical ones.
6. Build a 4–8 second moving proof of the hardest acting/interaction/reveal where possible; compare actual consecutive frames, camera micro-motion and gesture/contact timing. The old 4-second single-shot city proof did **not** validate long-form directing or tactile interactions. **No full render while critical story/action/visual defects remain.**
7. Produce `PRODUCTION_REVIEW.md` with blocking statuses and exact fixes. If a button press or twist cannot be shown convincingly, revise assets/geometry/acting or storyboard and rerender; do not just add props or extra references.
8. After user feedback, update the failure log (symptom → proven cause or hypothesis → owning file/function → before/after frames → reusable rule and regression test) so next episode starts from this lesson. Without new renders, label correction unverified.

### Stage E — sound, full render, audit

- Use upstream audio recipes in `templates/audio/` where applicable; dependencies/environment and audio cues are episode-specific. Check loudness and timing.
- Render using actual composition ID and entry path discovered from the local project, not guessed file paths. The upstream example rendered 1080×1920/30fps and scaled to 1440×2560.
- Run `templates/scripts/short_qa.py` with ffmpeg, Python, numpy and Pillow. It flags black/white/frozen/pop frames and exports review sheets, but it cannot judge overall aesthetic quality.
- Human approval of image quality is mandatory. Save proven fixes into our Style Bible, episode-specific modules and own Skill notes. Separate `TECHNICALLY_RENDERED_NOT_APPROVED` from `APPROVED`. If the user is unhappy, the job is not artistically accepted regardless of successful MP4 or clean render logs.

## Source contracts to preserve

- **Post:** composer in `Bridge.tsx` coordinates `ink.ts`, `lensblur.ts` and `grade.ts`. Correct effect order; keep resolution-aware pixel params.
- **Character:** `toon.ts` draws Canvas2D faces, `cast.ts` animates scene-facing cards, `cardshade.ts` lights cards. Preserve NOINK and ground contact shadow behavior.
- **Scenery:** `paint.ts` generates painted texture detail, `shade.ts` supplies two-tone shading; `build.ts` and `world.ts` are world-specific and must be rebuilt/adapted to each subject.
- **Camera/timeline:** `story.ts` includes hard-coded Bridge sequence, transitions, physical motion and focus; generate new shot plan rather than copying soldier actions.
- **Extras:** `templates/scripts/bridge-stills.mjs` hardcodes a Windows Chrome path and composition `BridgeShort`. Patch it in the local project as appropriate, **do not claim it is portable as-is**.
- Original reference reports are measurement notes, not verified universal truths. Some initial camera conclusions were revised in the creator's later analysis.

## What counts as a successful Skill

A user can invoke it in Codex, and Codex can read the included **real sources and scripts**, study references, plan/build a subject-specific new .ts scene in a configured local Remotion project, render a 4s sample, inspect side-by-sides, and improve it. Success needs actual rendered motion and artistic review — not merely static frames or a successful MP4. Before another topic, apply the permanent learning loop in `references/PRODUCTION_QUALITY_STANDARD.md`; **having these files in GitHub alone does not prove visual parity**.

## Version / upstream
This Skill adapts [mromidev/claude-animated-shorts](https://github.com/mromidev/claude-animated-shorts) commit `e3b817b6afc6cd413466d43f11ba31209e034bbf`. Copyright/license preserved in `LICENSE`; original unmodified skill snapshot at `upstream/SKILL.md`. No reference JPEGs/videos copied to this repository.
