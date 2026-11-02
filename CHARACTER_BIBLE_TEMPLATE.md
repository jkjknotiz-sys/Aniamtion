# CHARACTER BIBLE — กรอกก่อนสร้างตัวละครถาวร

## Identity
- Character ID / version: `hero-01/v001`
- Original name / role:
- Silhouette in thumbnail:
- Head shape (describe front/side/3/4):
- Body proportions (head-heights):
- Eye spacing / brow / mouth / chin:
- Line color / thickness behaviour:
- Palette HEX (skin, coat, accent):
- Distinct visual feature:
- Forbidden changes: face landmarks, head-body proportions, key accent (without approved redesign)

## Sheets
| Sheet | Required |
|---|---|
| Front neutral | yes |
| 3/4 neutral | yes |
| Profile | yes |
| Rear | if view requires |
| Expressions | neutral, happy, curious, angry, shocked, worried, talking, blink |
| Poses | stand, walk, run, point, react |
| Costumes | original / worker / sailor / scientist, with clear mapping |

## Runtime approach
- [ ] 2.5D Canvas2D character card (scene-lit billboard; shadow contact)
- [ ] 2.5D directional sprite set (side/rear)
- [ ] Full 3D .glb with armature (custom rig, animations)
- Primary source files:
- Face API / expression names:
- Lighting / cardshade:
- World ink exclusion:
- Contact shadow scale:
- Costume data schema:

## Acceptance
Render front + 3/4 + back where supported, daylight + storm, wide/close. Same person? Eyes/skin/outline unchanged? Feet planted? No floating / clipping? Pass only with comparison images.

**Rule**: Do not allow an agent to redesign the base face just because the scene changes. Version deliberate redesigns separately.