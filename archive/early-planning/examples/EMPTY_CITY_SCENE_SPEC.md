# Example Pilot — Empty City opening shot (invented, not extracted from video)

- Episode ID: empty-city-v2
- Shot: EC01; frames 0–119 (4s @30fps)
- Narrative: A city is eerily empty; evidence of life just stopped.
- Location: modern commercial street, late afternoon, overcast warm side-light.
- Focal subject: our approved character at the crosswalk, looking at an abandoned rolling bicycle.
- Camera: slow low-angle push-in with smoothstep; start behind foreground shop awning, focus on character at ~8m.
- Foreground: cropped recognizable parking meter and hanging shop sign framing subject; must not block face.
- Midground: crosswalk cracks, storefront steps, bike with spinning front wheel, litter reacting to wind.
- Background: receding building facades (different heights, inset windows, signs and trim), traffic light, hazy intersection; no humans.
- Textures: road asphalt with painted markings and chips; windows with variations; readable painted siding; careful UV/material variation.
- Lighting: day preset with warm key and cool sky fill; cast character shadow and contact on road; do not force golden preset.
- Ink: world outlines for architectural depth and bike geometry; card with own face/linework; keep NOINK separation.
- Depth: use DOF only if focal plane remains readable; signage may blur.
- Animation: dangling sign small sway, bike wheel deceleration, one paper flutter, character blink and hesitant step.
- Potential new modules: episodes/empty-city/buildCity.ts, props/Bicycle.ts, actions/LookAround.ts; visual renderer reused.
- QA: silhouette clear by 1st second; no featureless blocks in hero zone; street feels designed but not over-cluttered; all assets loaded.
- Gate: 8 stills + 4s test, visually compare against own Bridge-quality baseline.
- **This is a shot specification, not rendering code.**