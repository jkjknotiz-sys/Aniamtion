# Next Episode: production workflow that transfers lessons to a NEW topic

**Scope:** For a topic supplied by the user, apply the successful source-backed Three.js/Remotion method to produce the NEXT original animated short. This is a reusable Codex workflow, **not a new animation engine, not a new red-button episode, and not an automatic quality guarantee**.

## Entry condition

- Ask for **only the next topic** if the user has not provided one. Do not substitute an example episode as if the user chose it.
- A user-provided script, preferred style, language, duration or references take precedence. If no script was supplied, research factual claims and draft an original script. For invented stories label fiction clearly.
- Read the actual current Remotion project, root `AGENTS.md`, installed `SKILL.md`, `references/PRODUCTION_QUALITY_STANDARD.md`, `references/FULL_SCENE_AND_CAST_STANDARD.md`, `references/ASSET_LIBRARY_STATUS_TH.md`, and **local** `CHARACTER_LIBRARY.md`, `CHARACTER_STYLE_BIBLE.md`, `asset-manifest.json` where present. Do not invent these paths or their exports.
- Reuse prior reference studies and source code; consult selected original reference frames again when they improve a specific new shot. Do **not** rescan every reference for every new topic.

## Deliverables in a single episode-specific folder

### 1. Story-first design
- `EPISODE_BRIEF.md`: exact topic, audience, promise/hook, narration, runtime, factual evidence/uncertainty, emotional arc, twist contract if any.
- `CAST_BIBLE.md`: **every scripted speaking and reacting character**, plus purposeful background cast, with distinct identity, silhouette, age/size, clothes, palette, expressions, actor module, tested movement limits, appearance-by-shot and continuity. Natee is not default for every role. Do not recolor Natee to fabricate new named characters.
- `SHOT_VISUAL_PLAN.md`: shot ID, timing and narration phrase, narrative beat, all cast/blocking/eye-lines, hero object, foreground/midground/background, camera/lens/motion, lighting direction, color hierarchy, materials/scene detail, asset catalog IDs, interactions and exact rendered check frames.
- `LIGHTING_AND_COLOR_SCRIPT.md`: consistent **story-phase** look (e.g. daylight, conflict, mystery, resolution); meaningful key/shadow/bounce/rim vocabulary adapted to original Bridge shade/cardshade behavior. Adding arbitrary Three.js lights alone is NOT a verified diffuse-relighting solution.
- `ASSET_USAGE.md`: existing local models/characters/recipes reused vs missing; license/provenance and close-up suitability. A GLB that loads is not automatically rigged, interactive or hero-ready.

### 2. Rendered visual design (not only prose)
- Generate **4–6 representative stills** at episode target size from the **actual project renderer**, covering story opening, scene environment, multiple actors, one hero prop/close view, any demanding lighting/reveal/action and finale where relevant.
- Produce `LOOK_COMPARISON.jpg` or HTML side-by-side with **shot-compatible** reference frames (private local only); explain what specifically matches and what fails regarding: focal hierarchy, silhouette, composition, color/contrast, shadow structure, world/actor integration, texture and material detail, acting/cast.
- At least one 2+ actor shot must show **clear actor-to-actor eyelines/reaction**. Supporting cast are NOT faceless recolors. Render on-phone-size review.
- For any important interaction, make a 4–8 second temporal proof with before/contact/deformation/consequence; do not rely on a single pose screenshot or SFX.
- **No regression** on existing shader/order, baseline Bridge, asset library originals or previously approved scripts. New episode-specific `.ts/.tsx` are normal, not a new engine.
- Record `SCENE_LOOK_REVIEW.md` and `PRODUCTION_REVIEW.md` with visually grounded observations, actual frame IDs, critical fixes, untested constraints and separate technical vs artistic statuses.

### 3. Practical release path
- Default when user requests a **storyboard**: deliver draft, playable visual preview and contact sheets; pause for review before rendering full.
- Default when user explicitly says **publish-first**, needs a video for the channel, or authorizes full production: spend a bounded short look-and-action pass, fix major blockers (story incomprehensible, floating contact, missing actors, unreadable text, blank/frozen frames), then render the actual full original episode, audio and Thai subtitles. Report unresolved aesthetic flaws without endless polishing.
- If user has not chosen between storyboard review or final delivery, infer from their latest instruction, not from previous example tasks. Do not ask repetitive preference questions.
- Final technical QA: playable vertical MP4, actual FPS/duration, missing assets, frozen/blank frames, voice/SFX/sync, subtitle readability and scene transitions. Human artistic approval remains separate from a technically complete MP4.

## Story-specific production rule

The 12-shot Red Button Town is a **learning case**, not the next default topic. Never create more red button scenes or a Natee-only demo instead of the user-selected next story. Retain transferable lessons: believable physical touch, intentional camera angles, vibrant-but-controlled color, useful background details, emotionally specific secondary cast, accurate scale and meaningful reveals.

## Report succinctly

Return paths to actual files (not invented), a preview sheet and optional video, a one-paragraph summary of what improved vs previous episode, and only remaining important limitations. Keep user focused on making episodes, not endlessly accumulating reference reports.
