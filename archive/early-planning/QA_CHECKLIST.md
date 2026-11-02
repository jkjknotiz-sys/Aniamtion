# Visual Quality Gates — human + measurable checks

## Required artifacts
- [ ] At least 3–5 legally usable style references or our own approved baseline
- [ ] 4s test MP4; 8 representative PNG stills across video
- [ ] Side-by-side sheet & numbered notes
- [ ] TS/type/build and asset load checks
- [ ] Written PASS/FAIL; reviewer names/date and next action

| Dimension | PASS test | Typical defect → owner |
|---|---|---|
| Character identity | Face silhouette and landmark consistency across costumes/shots | redrawn face → character |
| Geometry & environment | Correct recognisable structure at camera distance | generic boxes, lost railings → world |
| Texture | Grain/seams/edges visible where close enough | flat unpainted surfaces → material |
| Ink | Scene edges/creases present, no double outlines | effect erased by blur → post |
| Lighting | Key/fill directions and subject readability intentional | flattened ambient / crushed faces → lighting |
| Color | Saturation & shadow hue coherent with story/time | unmotivated color shift → grade |
| Depth | Correct DOF focus, atmosphere and foreground readability | character sticker/no shadow → post/character |
| Composition | Story action clear at thumbnail, no occluding props | empty or cluttered focal point → camera/world |
| Motion | Feet contact, reaction timing, no jerks/freezes | static card, abrupt push → camera/character |
| Audio | Speech clear, voice aligned, event SFX matched | bad timeline → audio |
| Rights | Own characters/story/audio; asset licenses recorded | unclear reuse → producer |

## Severity
- **P0 stop**: lost effect pass, broken assets, blackout, unlicensed copy, unreadable hero.
- **P1 rework before full render**: repetitive blank scenes, wrong character design, pop motion, wrong focal plane.
- **P2 improve**: optional extra prop, minor material variation.
- 1–10 scores are optional notes, not objective proof. **Approval requires screenshots and reviewer signoff.**

## QA log template
~~~md
# QA REPORT
Episode / Commit / Render config / Reviewer / Date:
Frames audited:
Reference version:
| Time/frame | Severity | Observation | Likely cause | File owner | Fix | Retest frame | Status |
|---|---|---|---|---|---|---|---|
Decision: PASS / FAIL
Evidence paths:
~~~

## Before final
- [ ] No unauthorized changes to shared renderer
- [ ] Stills from first / middle / last scenes pass
- [ ] 4s moving test passes
- [ ] Full video checks: resolution/FPS/black/white/frozen/pop frames/audio/subtitle safe area
- [ ] Disk/temp checked; original assets and attribution retained
- [ ] Final render visually approved by a person