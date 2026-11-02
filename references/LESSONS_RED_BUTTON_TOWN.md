# Learning Case: “Red Button Town” 12-shot storyboard — 2026-11-02

**Source:** user-provided screenshots of Codex's 12-shot storyboard (approximately 54 seconds), with a red button at a city square and a toy-city twist. User reports dissatisfaction with the physical believability of button pressing and overall visual attractiveness. No complete final animation was supplied for this case; screenshots show rendered storyboard stills, not frame-by-frame proof of contact or a completed full video.

**Status:** quality problems observed/reported, **not** a validated corrected episode.

## What works and is worth preserving

- 12 rendered 3D storyboard stills appear to use original flat ink-outlined characters and detailed, colored town geometry
- The town has a coherent visual identity across several shots and multiple lighting conditions
- A clear narrative concept exists: an apparently real town with a forbidden red button and a reveal that it is a toy-like miniature
- Bridge source techniques have been proven applicable to non-Bridge locations in earlier Empty City proof; no evidence that shaders must be rewritten

## Specific shortcomings seen in these stills / user feedback

1. **Physical action looks unconvincing:** a large finger/hand over the button does not by itself show the audience that a press happens. Several stills show approach/hover/in-frame hand. Need a physically contiguous action: fingertip approach → aligned contact → cap depresses → reaction. Verify through *consecutive frames*, not one attractive still.
2. **Reveal timing risks spoiling the twist:** hand/finger from above is already conspicuous in opening/early shots, while the story's toy-city reveal occurs in shots 9–12. This is a storytelling issue to test, not an absolute ban on hints.
3. **Repeated staging:** town square/button/sign and two characters appear in several shots. Repetition can establish stakes, but variations must convey fresh information or emotional states. Need meaningful inserts/reactions/POV/compositional changes.
4. **Main character acting is underspecified:** repeated front-facing idle pose in storyboards makes events less persuasive. Need gesture, head/eye shift, anticipation, reaction and world/contact continuity when animated. Still frames alone do not prove motion is missing; they do expose that planned acting isn't visually communicated.
5. **Visual hierarchy/atmosphere:** colored town geometry and hard sunlight alone do not ensure a dramatic story frame. Some storyboard shots feel like direct documentation of assets, rather than intentional cinematic lighting, foreground layering, depth/contrast hierarchy and lens selection.
6. **Toy-world physical logic:** giant child, miniature city and giant hand must obey one consistent world-space scale, perspective and spatial continuity across reveal. The contrast can be surreal, but interactions must still align/affect props coherently.
7. **Text legibility:** verify Thai warning-sign copy in actual output at phone size. Do not declare text accurate based solely on a zoomed-out storyboard image.

These are observations and user feedback, **not** claims about the unseen animation or exact root cause in unpublished project code.

## Convert feedback into GENERAL rules for every future episode

| Failure symptom | Persistent rule | Evidence required next time |
|---|---|---|
| Hand looks as if it floats over button | Every hero physical interaction has 5–6 named states and world-space contact aligned with target mesh | 4+ stills at anticipation, touch, compressed/actuated, consequence; short motion test |
| Giant hand appears before toy twist | Every twist has a reveal contract: allowed clues vs forbidden early reveals | storyboard shot-by-shot reveal audit |
| Repeated button/town compositions | Every shot must add new story information/emotion; vary framing with purpose | shot purpose table and review sheet |
| Characters seem passive | Role-dependent gesture, gaze, pose, reaction and contact shadow | keyed pose/acting thumbnails for hero shots |
| Town looks built but not cinematic | Per-shot art direction: hero silhouette, meaningful prop layers, atmosphere, material detail, controlled light | side-by-side matched shot-category references |
| No proof that quality is production-ready | Separate technical QA from artistic approval | QA report with `TECHNICALLY_RENDERED_NOT_APPROVED` when appropriate |

## What Codex should change next time

Before writing full episode TS:
- review prior case studies, especially **physical action** and **shot logic**
- define `scene storyboard spec` for prop mechanisms, interaction actor, camera, reveal and critical states
- make a *single* hero-action test (e.g. button press) with meaningful tactile contact and continuity
- render look-test frames and compare with approved references
- only after passing direct-review gates build the rest of the storyboard/full short
- any limitation from billboard character articulation must be handled with a suitable camera or additional original 3D hand geometry. Never fake believable hand contact by merely adjusting audio

**How to update this document:** add before/after links, exact file/function and rendered evidence when an actual corrected implementation is available; then mark the specific rule verified. Do not assert it is fixed before re-rendering.