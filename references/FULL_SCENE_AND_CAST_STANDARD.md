# Full-scene visual direction & ensemble cast (mandatory for every episode)

**Why this exists:** Improving the one recurring character, Natee, does not fix the appearance of the entire finished short. A polished shot needs intentional **lighting, palette, scene composition, materials, camera and ALL characters required by the script**, including secondary cast and extras. The original Bridge methods are the source baseline; do not build a new renderer.

## 1. Read the SCRIPT as a production casting/visual document

Before finalizing a storyboard, extract an **episode cast inventory** and a **scene inventory**. No character or event required by the narration may disappear merely because no asset is currently available.

| Required per character | Meaning |
|---|---|
| id / story role / first-last shot | Identify Natee, antagonist, supporting character, background extras and their narrative function |
| dialogue/reaction cue and emotion | Include non-speaking reactions and interaction partners |
| on-screen appearances | Exact shot IDs, shot sizes, entry/exit and continuity across cuts |
| design identity | Distinct readable silhouette, height/shape proportions, clothing, palette, hat/hair and unique expression set; original designs, not copied from references |
| animation capability | Which gestures/turns/walk/contacts are already tested vs need new pose or geometry |
| drawing/geometry asset path | Inspect actual `.ts` drawing modules, billboards, local GLBs and licenses; **no invented cast asset IDs** |
| light/occlusion/grounding | Character must share scene key/fill/shadow world rules; correct depth overlap/contact shadows |
| readiness | `READY`, `NEEDS_VARIANT`, `NEEDS_ACTING`, `NEEDS_CONTACT_PROOF`, `MISSING` |

Natee v2/v2-acting is a *single recurring hero*, not a replacement for every character. Build other script-defined characters from reusable Canvas2D drawing conventions and shared shading/ink rules with their OWN heads/shape language/identities, expressions and poses; do not recolor/resize Natee and call it a new cast unless the script specifically depicts an identical group. Background extras may use simple cards if not starring in interactions. Named supporting characters need medium/close readability and acting. Different people must not all look emotionally identical.

**Every scripted character must be traceable:** Script line → shot ID → actor ID → actual reusable module/object → rendered frame evidence. If not, flag CAST_MISSING / BLOCKED_VISUAL rather than filling an empty shot with Natee.

## 2. Shot art direction must exist BEFORE coding

For each shot author a `SHOT_VISUAL_PLAN` row with:

- Story beat and emotional goal: what viewer learns now; what NOT to reveal yet.
- Cast/Blocking: actor positions in **world space**, facing/eye-lines, role priority, entry/exit, depth overlaps, action/react, prop interactions; include background extras if required.
- Composition: portrait 9:16 safe areas, shot scale (EWS/WS/MS/CU/ECU), focal subject, thirds/leading lines/negative space, silhouette contrast, foreground/midground/background and intentional perspective. Don't force identical eye-level centered shots.
- Camera: focal length/FOV, position, target, motion path, easing, DOF focal distance & emotional purpose; no camera teleport, clipping or flat billboard profile exposure.
- Lighting: time of day, **motivated key/fill/rim** (color, intensity, direction), shadow softness/contact, local/practical lights, volumetric/fog depth, reflected color; ensure ALL actors are lit consistently with props/world.
- Color script: intended warm/cool relationships, local material palettes, subject-to-background separation, saturation/contrast/exposure and shot continuity. Day/night/indoors/storm must differ without becoming a completely different channel style.
- World/props: visual hierarchy and narrative-specific details (rooflines, doors, wires, seams, dents, weathering, reflected highlights). Avoid repeating cloned facade patterns, but also avoid arbitrary prop spam.
- Assets: cataloged model IDs and suitability (background/medium/hero/interactive), scene-specific `.ts` modules needed, asset license.
- Technical proof: requested still-frame IDs and **moving** check IDs, script/shot/character coverage status, known limitations.

A composition is **not successful** just because it contains all props. Phone-screen glance test: viewer must identify the narrative focal subject within ~1 second without reading a caption, and foreground/actor must not merge with background silhouettes.

## 3. Lighting & palette review: specific, not generic "make it cinematic"

For each representative keyframe actually render:
1. **Silhouette/grayscale pass** (or luminance-only preview): subject/body/hand/prop distinct in value; don't flatten all faces into one brightness.
2. **Albedo/material pass or ungraded frame** where practical: check unintentional material hue shifts, wrong metalness, oversaturated colors, pale faces pasted into dark worlds, broken textures/UVs.
3. **Lit/graded final** with original Bridge post chain: inspect world-to-billboard illumination, ink legibility, contact shadows and bloom/DOF not wiping detail.
4. **Reference side-by-side:** choose corresponding **type of shot and lighting condition**, not random image from another setting; visually compare (a) color temperature relationships, (b) contrast/value structure, (c) texture/object density, (d) shadow grounding, (e) depth layering and (f) visual focal hierarchy.
5. **Shot transition/continuity check:** no sudden unmotivated white balance/exposure flips, position jumps, costume changes or vanishing background extras.

Numbers like luminance and saturation are diagnostic, not universal targets; don't force a night ship scene to match a sunny train station's absolute saturation.

## 4. Ensemble animation and scene integration

- Secondary cast must have at least one authored **role-specific behavior**: eyes/gesture/pose/gait/reaction. Avoid copy-paste mirrored Natee idle loops for crowd scenes.
- Establish **eye-line** and relative scale: if one person speaks, someone reacts with a delayed head/eye shift. If a character acts, both the character and surroundings/other cast show causally meaningful response.
- Integrate actors with **shared ground plane, world units, shadows, occlusion and lighting**. Flat cards should not float, cut across props or expose impossible side/back geometry. Adapt camera or add pose-specific drawing or local 3D geometry.
- In scenes with 2+ actors, render at least one frame where **both** are clearly staged and an animated exchange/reaction proof across several frames. Verify characters do not overlap awkwardly and speaking/acting focus is clear.
- Maintain continuity: actors' clothing, hats, proportions, object ownership, positions, handedness, gaze and emotion before/after camera cuts.
- Natee v2-acting recipes (from user's **local** `CHARACTER_LIBRARY.md`) may be applied only within their documented tested ranges. Inspect current local code before reuse. Do not treat them as a general rig for all NPCs.

## 5. Episode-level required deliverables / acceptance checks

Create these inside the actual episode folder:
- `CAST_BIBLE.md`: every scripted character, original appearance, palette, silhouette, height, expression/pose, interaction readiness and code paths.
- `SHOT_VISUAL_PLAN.md`: all shots with the exact visual plan fields above; include all cast and lighting.
- `SCENE_LOOK_REVIEW.md`: before/after or side-by-side reference sheets, 6+ representative stills when runtime allows (cover intro, multi-character scene, environment, hero prop, special lighting, finale), and a short temporal strip at reactions/interactions.
- `PRODUCTION_REVIEW.md`: mark actual `CAST_MISSING`, `BLOCKED_VISUAL`, `BLOCKED_ACTION` or `TECHNICALLY_RENDERED_NOT_APPROVED` until evidence supports acceptance. These are production review states, not synthetic numerical artistry ratings.

**Fail conditions:** any scripted named cast omitted; generic identical crowd used as named supporting cast; main action/reaction absent; character visibly unlit or floating relative to set; severe incoherent palette/exposure; repetitive camera compositions that add no information; incorrect facial silhouette/ink/occlusion; hero prop too low-detail for distance; no rendered evidence.

**Stop condition:** don't call a storyboard or episode artistically approved because a valid 1080×1920 MP4 exists. Conversely, if the user explicitly requests publish-first, fix critical clarity failures, deliver with documented limitations instead of an endless polish loop.

## 6. Update the library, not just a single shot

When a supporting character design or color/lighting configuration passes human review, save an independent reusable character variant / expression and lighting preset **in the local project**, with test images. Record its exact exports and tested camera range. Do not invent modules or claim upgrades were merged into the current production without verifying the imports.

Reference-derived designs should be **original**, not traceovers or near-copies of recognizable media characters. Reference frames remain local/private.
