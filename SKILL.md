---
name: aniamtion-shorts
description: Produce original stylized 2.5D characters in real 3D world short videos by studying references quantitatively, adapting the preserved Claude Animated Shorts bridge code, rendering diagnostics, and iterating until visual quality passes. Use for new animated shorts across topics such as ships, railways, abandoned cities, history and science.
---

# Aniamtion Shorts — source-grounded skill

**Goal:** reproduce the *method* shown by mromidev/claude-animated-shorts and adapt it for original stories, our own recurring characters, and new worlds. This is a source-backed Agent Skill usable by Codex, with upstream MIT source templates and analysis/QA scripts; **it is not a new animation framework**.

Read this file first, then:
- `README.md` for installation and what is included;
- `CODE_MAP.md` for exact source responsibilities and what changes between episodes;
- `references/OUR_STYLE_BIBLE.md` for **our provisional evidence-based rail/ship study**; ask the user to approve hero references before using its candidate art directions as fixed rules;
- `references/STYLE_BIBLE.md` and `references/reports/*.md` for the upstream study (do not conflate their 20-video measurements with our two-video study);
- `templates/bridge/*.ts`, `templates/bridge/Bridge.tsx` for actual proven example code;
- `templates/scripts/*.py` for frame comparison and QA;
- `scripts/analyze_references.py` for analyzing your own locally available example videos.

## Non-negotiable constraints

1. **Reference precedence:** our approved user style evidence outranks generic upstream look targets when building new episodes; the current OUR_STYLE_BIBLE is provisional, based on 2 videos and not yet human-approved. Missing external local assets such as `review_manifest.json`, `reports/methodology.md`, `evidence/01` and `evidence/02` must not be invented.
2. **Source-first, not prompt-first.** Open the real modules, inspect symbols and dependencies, and render actual frames. No guesses about assets or exports.
2. **Never pretend the bridge template is a generic scene engine.** `world.ts`, `build.ts`, `cast.ts` and `story.ts` contain bridge/town/soldier logic. A new topic needs appropriate geometry, painted materials, props, movements and camera staging, often in NEW .ts modules.
3. **Keep the look code until proven otherwise.** Original drawing/shader/effects in `toon.ts`, `cardshade.ts`, `shade.ts`, `paint.ts`, `ink.ts`, `lensblur.ts` and `grade.ts` are a baseline. Verify which utilities are reusable; do not rewrite all of them just because story changed.
4. **Original people and stories.** Study references for measurable techniques, not for copying distinctive designs/shots or distributing private video frames. Original source licensed MIT (retain LICENSE).
5. **Human quality gate.** A video is not 'finished' because a render succeeded or an agent gave it a good score.
6. **No silent broad fallback.** If a required GLB/detail asset is missing, report it and obtain/author legal equivalents rather than finishing with unpainted block geometry.
7. **No false 'watched all frames' claims.** The scripts process every frame numerically; human/LLM image review normally happens through sampled/contact-sheet images. Explain the distinction.

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

### Stage C — design a NEW episode, not a copied Bridge

- Research and verify factual story; use a paradox hook, escalating beats, pivot/mechanism and payoff where appropriate, but write original script with user's chosen language.
- Produce narration first, then timing map; align reaction/camera changes to narration.
- Plan scene/shot camera geometry and list assets **specific to the new subject**. Examples:
  - Empty City: city facades, window bays, shop signs, street markings, cars, neglected props, traffic lights, original character; building and material recipes.
  - Storm Ship: hull, mast, sails, rigging, water, spray, sky/fog, ship roll and reaction animations.
- Copy proven template into a NEW episode folder in local Remotion project. Inspect and adapt `story.ts`, `build.ts`, `world.ts` and `cast.ts` with topic-specific .ts/.glb as required; adapt lighting presets to story context without losing shading/post rules.
- Reuse original character-runtime ideas, but design **independent recurring characters**. 2D lit cards in 3D are 2.5D; switch to fully rigged 3D only if the shot needs it.

### Stage D — look-match loop (what made original good)

1. Render 8–12 representative stills **before full video**.
2. Put our frames against approved style/reference examples with `templates/scripts/sbs_sheet.py` (local paths). Inspect ink, hue, contrast, silhouette, shadow, texture grain, depth, camera framing and actor anatomy.
3. Log failures as frame number → observed issue → measured delta → suspected cause → source file/function → owner.
4. Delegate by **file ownership**, separate branches/sandboxes. Example: cam owns story; world owns world/build; character owns toon/cast/cardshade; post owns ink/lensblur/grade. Avoid concurrent edits to the same source.
5. Re-render changed frames and compare. The original found an ink pass accidentally overwritten by blur, over-thick limbs, too-flat materials and too-snappy camera moves. Diagnose actual issues instead of assuming identical ones.
6. Build 4-second moving proof where possible; compare camera micro-motion and gesture timing. **No full render while critical defects remain.**

### Stage E — sound, full render, audit

- Use upstream audio recipes in `templates/audio/` where applicable; dependencies/environment and audio cues are episode-specific. Check loudness and timing.
- Render using actual composition ID and entry path discovered from the local project, not guessed file paths. The upstream example rendered 1080×1920/30fps and scaled to 1440×2560.
- Run `templates/scripts/short_qa.py` with ffmpeg, Python, numpy and Pillow. It flags black/white/frozen/pop frames and exports review sheets, but it cannot judge overall aesthetic quality.
- Human approval of image quality is mandatory. Save fixes into our Style Bible, episode-specific modules and own Skill notes.

## Source contracts to preserve

- **Post:** composer in `Bridge.tsx` coordinates `ink.ts`, `lensblur.ts` and `grade.ts`. Correct effect order; keep resolution-aware pixel params.
- **Character:** `toon.ts` draws Canvas2D faces, `cast.ts` animates scene-facing cards, `cardshade.ts` lights cards. Preserve NOINK and ground contact shadow behavior.
- **Scenery:** `paint.ts` generates painted texture detail, `shade.ts` supplies two-tone shading; `build.ts` and `world.ts` are world-specific and must be rebuilt/adapted to each subject.
- **Camera/timeline:** `story.ts` includes hard-coded Bridge sequence, transitions, physical motion and focus; generate new shot plan rather than copying soldier actions.
- **Extras:** `templates/scripts/bridge-stills.mjs` hardcodes a Windows Chrome path and composition `BridgeShort`. Patch it in the local project as appropriate, **do not claim it is portable as-is**.
- Original reference reports are measurement notes, not verified universal truths. Some initial camera conclusions were revised in the creator's later analysis.

## What counts as a successful Skill

A user can invoke it in Codex, and Codex can read the included **real sources and scripts**, study references, plan/build a subject-specific new .ts scene in a configured local Remotion project, render a 4s sample, inspect side-by-sides, and improve it. Success needs an actual rendered test; **having these files in GitHub alone does not prove visual parity**.

## Version / upstream
This Skill adapts [mromidev/claude-animated-shorts](https://github.com/mromidev/claude-animated-shorts) commit `e3b817b6afc6cd413466d43f11ba31209e034bbf`. Copyright/license preserved in `LICENSE`; original unmodified skill snapshot at `upstream/SKILL.md`. No reference JPEGs/videos copied to this repository.
