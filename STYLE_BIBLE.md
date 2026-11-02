# STYLE BIBLE v0.1 — กฎศิลป์ประจำช่อง

> Working draft; calibration targets, not a claim that visual equivalence has been achieved. ต้องแทนค่าด้วยภาพต้นแบบที่ได้รับอนุญาตและ render จริง

## 1. Visual identity
- Cartoon ink-edged painted 3D worlds + expressive **2.5D flat character cards** with physical scene lighting. Characters must not appear like unlit stickers pasted onto backgrounds.
- Reference hierarchy: (1) approved frames from our best work (2) our character sheets (3) other legal stylistic references used only for study.
- Original identity required: do not duplicate distinctive characters, scripts, camera sequences or copyrighted footage.

## 2. Ink / post-processing
- World ink detects silhouette/depth/normal creases. Avoid unmotivated lines on floor/wall seams and horizon.
- Character ink drawn separately; exclude character billboards from world ink pass (original uses NOINK).
- Inspect pass order **ink → lens pre → lens main → bloom → neutral tone map → grade** (Bridge baseline); do not blindly reorder.
- Pixel-sized effects must be scaled to output resolution. Check 50% preview and final independently.
- Baseline original: dark ink near #030303, roughly 5.1 px near → 3.3 px far at 1080×1920. Calibrate for our look, never hardcode as universally optimal.

## 3. Lighting / palette
- Lock *lighting model*, not one sun angle. Presets: day / golden / night / storm / interior. Each has key, fill, rim, shadow hue, atmosphere and exposure.
- Warm highlights/cool shadows can be starting art direction, but a night storm must still look like night; no forced amber sunlight.
- No crushed black detail unless intentionally motivated. Key subjects need readable value separation from background.
- Keep sun continuity inside a shot; show sky/fog consistency. Painted material palette should survive changes of light.

## 4. Materials / geometry
- Every medium/close hero object needs readable construction: joints, trims, thickness, wear patterns appropriate to scale.
- Use painted textures or licensed detailed assets. Plain BoxGeometry is allowed as blockout, **not automatically acceptable as final buildings**.
- Evaluate textures at actual camera distance, not just inspect mesh counts. Avoid random clutter.
- Create a reusable asset catalog; procedural .ts builders are for geometry and behaviour, not replacements for art direction.

## 5. 3-layer staging
- Each story beat should have an intentional focal subject, designed silhouette, negative space and foreground/midground/background separation as needed.
- Do **not** enforce an arbitrary minimum number of props: a deliberate empty city can be empty of people but rich in believable evidence (broken signs, abandoned cars, shopfronts).
- Examine scene silhouettes at thumbnail size. Foreground props must remain recognizable and not obscure faces.

## 6. Characters
- Default baseline: Canvas2D card in 3D (2.5D). Shared identity: face landmarks, head/body ratio, line weight, gestures, accent colors.
- Bridge source baseline (not compulsory for our original): adults ~3.5 head heights, bean heads, small limbs, expressive face library.
- Character identity survives costume, era and lighting. Make turnaround sheets and 8–14 useful expressions.
- When continuous 360° turning or physical depth is required: consider multi-view sprites or GLB rig. 3D model is a separate technical track; don't claim billboards are true 3D.

## 7. Camera & motion
- Intentional gliding camera; smootherstep transitions where suitable; cuts for large discontinuities.
- Bridge analysis reports 18–40 frame glides and subtle push-ins, but pick motion based on narrative need.
- Establish / medium / close / insert, varied with purpose; focal plane on character eyes for CU/MS, keep establishing shots readable.
- Feet contact, body bob and secondary motion must read correctly. Verify actual frame-to-frame animation.

## 8. Shot-level style acceptance
For each pilot: at least 8 representative stills + 4-second moving test. Compare to our approved baseline:
1. Character continuity
2. World construction & readable props
3. Ink quality
4. Materials/texture
5. Lighting/shadow continuity
6. Depth/atmosphere
7. Composition/visual storytelling
8. Motion/camera and audio sync (video test)
Set PASS/FAIL with concrete frame numbers; optional 1–10 scores are subjective reviewer notes, **not ground truth**.

## 9. Scope
This document defines taste and quality gates, **not** ready-to-execute render code. Changes must be approved by showing difference frames and recording before/after findings.