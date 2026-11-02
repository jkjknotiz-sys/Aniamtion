# FINAL DECISION — สรุปสิ่งที่เราจะสร้างจริง

**สถานะ:** ตกลงทิศทางระบบ / ยังไม่ได้เขียนและทดสอบ Animation Engine  
**เอกสารนี้เป็นข้อสรุปหลัก** เมื่อเอกสารเก่าขัดแย้งกัน ให้ยึดเอกสารนี้จนกว่าจะมีการตัดสินใจใหม่พร้อมเหตุผลและผลทดสอบ

## 1. ปัญหาที่เราต้องแก้

วิดีโอ Bridge จาก `mromidev/claude-animated-shorts` มีงานภาพดี แต่การเปลี่ยนไปเป็นเรื่องใหม่ (Empty City) ทำให้งานภาพ แสง วัสดุ มิติ รายละเอียดวัตถุ และการกำกับกล้องด้อยลงอย่างเห็นได้ชัด

**ต้นเหตุที่ยืนยันได้จากโครงสร้าง:** โปรเจกต์ต้นฉบับผูกฉาก สะพาน เมือง แม่น้ำ ทหาร และ timeline เข้ากับไฟล์ TypeScript ของตอนแรก หลายส่วนไม่ใช่ generic scene generator  
**สิ่งที่ยังไม่ยืนยัน:** สาเหตุระดับฟังก์ชันในโปรเจกต์ Empty City เพราะยังไม่ได้ตรวจซอร์สเต็มของโปรเจกต์ใหม่อย่างสำเร็จ ห้ามฟันธงว่า `ink.ts` หรือ `lights.ts` ถูกลบจนกว่าจะมีหลักฐาน

## 2. ภาพปลายทาง

เราจะสร้าง **Animation Studio / Stylized 2.5D + 3D Shorts Engine** ของเราเอง

- **โลกและฉากเป็น 3D จริง:** เรขาคณิต, แสง/เงา, painted materials, ระยะลึก, การเคลื่อนกล้อง ผ่าน Three.js
- **ตัวละครประจำช่องเป็นดีไซน์ของเรา:** รุ่นแรกใช้ 2.5D Canvas2D character cards ที่รับแสงและสร้างเงาในโลก 3D แบบหลักการใน Bridge; ไม่ลอกหน้าตาหรือเครื่องแต่งกายต้นฉบับ
- รองรับเสื้อผ้า อารมณ์ สีหน้า ท่าทาง และหลายมุมมอง โดยไม่เปลี่ยนหน้าใหม่ทุกตอน
- **เรื่องเปลี่ยนได้:** เรือ รถไฟ เมืองร้าง วิทยาศาสตร์ ประวัติศาสตร์ ฯลฯ ใช้เอนจินกลางเหมือนกัน แต่สร้าง scene-specific geometry, models และ animations ต่างกัน
- เน้นคุณภาพการกำกับภาพระดับคลิปตัวอย่างที่ผู้ใช้ส่ง ไม่ใช่การก๊อปปี้ shot-by-shot
- **เสียงบรรยายมาก่อน timeline** โดยเฉพาะภาษาไทยที่ต้องตรวจ timing เอง
- ออก MP4 แนวตั้ง 9:16, 30 FPS ผ่าน Remotion; full render หลัง QA ผ่าน

> ไม่ใช่การล็อก `.ts` ทุกไฟล์ให้เหมือนเดิม ไม่ใช่สร้างจาก prompt เดียว และไม่ใช่การส่งชุด prompt เป็นผลิตภัณฑ์สุดท้าย

## 3. หลักการแยก 'ระบบกลาง' กับ 'ไฟล์เฉพาะเรื่อง'

**ล็อกสัญญาของระบบ (interfaces, pipeline, regression expectations)** ไม่ล็อกตัวเลขแสงให้เหมือนกันทุกฉาก

| ส่วน | สิ่งที่ทำจริง | นโยบาย |
|---|---|---|
| Renderer / post | Ink outlines, lens blur, bloom, tone map, grade, resolution scaling | รีแฟกเตอร์จาก Bridge โดยรักษาลำดับ/ผลภาพ |
| Lighting | ระบบแสง, sky/fog & day/golden/night/storm presets | ใช้ shared code แต่ปรับค่าตามฉาก |
| Material + texture | Two-tone shading, painted textures, roughness and seams | แยก utility ใช้ซ้ำ; recipe ใหม่ตามวัตถุ |
| Characters | Original character design, card shading, expressions, pose/costumes, contact shadow | Character library ประจำช่อง |
| World builder | Scene host, placement, asset loading, procedural props, occlusion checks | สร้างฉากใหม่ด้วย reusable primitives + GLB |
| Timeline + camera | ช็อต กล้อง transitions, shots/actor actions, audio sync | ใช้ utilities กลางแต่ data ของตอนใหม่ต่างกัน |
| Episode-specific modules | `city.ts`, `train.ts`, `ship.ts`, `ocean.ts` และอื่น ๆ | **สร้าง `.ts` เพิ่มตามหัวข้อ** ห้ามแทนฉากสุดท้ายด้วยกล่องโล่งเพราะง่ายกว่า |

**แนวใช้ Geometry/Assets:** procedural Three.js .ts เหมาะกับสิ่งที่ทำเป็นกฎและใช้ซ้ำ; โมเดล `.glb` เหมาะกับเรือ รถไฟ อุปกรณ์ซับซ้อน โดยต้องมีใบอนุญาตและผ่านการปรับ material ให้เข้ากับสไตล์เดียวกัน

## 4. สิ่งที่แกะจาก Repository ต้นฉบับ

ข้อเท็จจริงจาก [SKILL.md](https://github.com/mromidev/claude-animated-shorts/blob/main/SKILL.md):

| ไฟล์เดิม | แนวทางใหม่ |
|---|---|
| `Bridge.tsx` | Extract composition/render orchestration ไม่เอา Bridge data ลง core |
| `ink.ts`, `lensblur.ts`, `grade.ts` | Extract shared effects; ยืนยันลำดับ `ink → lens pre → lens main → bloom → neutral tone map → grade` |
| `shade.ts`, `paint.ts` | Reusable material/texture generators |
| `lights.ts` | Lighting model และค่าตั้งต้นที่ configurable; เพิ่ม preset สำหรับเรื่องใหม่ |
| `toon.ts`, `cardshade.ts` | Drawing & shading utilities สำหรับตัวละครต้นฉบับของเรา |
| `cast.ts` | แยก reusable actor runtime จากทหาร/ฝูงชน/บทบาทใน Bridge |
| `world.ts`, `build.ts` | แยก world host / generic builders ออกจาก river / town / bridge |
| `story.ts` | ย้าย timeline เดิมไว้ `episodes/bridge/`; สร้าง timeline ใหม่ทุกตอน |

การรีแฟกเตอร์ไม่ใช่การคัดลอกไฟล์ไปเปลี่ยนชื่อ ต้องตรวจ import/dependency ก่อน และเทียบ render ก่อน–หลังทุกช่วง  
ต้นฉบับเป็น MIT สำหรับ code/docs ตาม README; ถ้านำ code มาดัดแปลงจริงต้องเก็บ LICENSE/copyright notice

## 5. รูปแบบโฟลเดอร์ที่ตั้งใจให้ได้เมื่อมีโค้ดจริง

~~~text
Aniamtion/
  studio/
    engine/
      render/           # compositing/post processing
      lighting/         # shared lighting models + presets
      materials/        # painted textures, shader utilities
      camera/           # camera moves, focus, transitions
      world/            # scene host, loaders, object registry
    characters/
      core/             # 2.5D character runtime, shading, animation
      originals/        # character ID / drawings / expressions / costumes
    assets/
      catalog/          # licensed GLB and reusable authored objects
      recipes/          # reusable procedural .ts builders
    episodes/
      bridge/           # original baseline kept intact
      empty-city/       # new episode-specific world/timeline
      storm-ship/       # new episode-specific world/timeline
    audio/
    qa/
  docs/
~~~

> โครงสร้างด้านบนคือ **เป้าหมายการพัฒนา ไม่ใช่โฟลเดอร์ที่สร้างครบแล้ว** ณ วันที่จัดทำเอกสารนี้

**Data / code contract แนวคิด:** Episode บอก shot plan, actors, world builder, per-frame update, lighting preset และ audio timeline; Renderer เป็น shared composition ที่นำแต่ละตอนมาประกอบ ถ้าต้องปรับ shared contract ต้องมี regression test

## 6. ลำดับลงมือ — ห้ามข้าม

### Phase 0 — Baseline + forensic
- นำ code Bridge เข้า local Remotion project แบบไม่ทำลายต้นฉบับ
- ระบุ dependency, assets, licenses, resolution, scene imports
- เก็บ stills อย่างน้อย 8 เฟรม + moving sample + render settings จาก Bridge เป็น GOLDEN MASTER
- ตรวจ Empty City source ที่ใช้งานจริงหากมี เพื่อเทียบว่าระบบใดขาด/ถูก bypass (แยก evidence / hypothesis)

**ถือว่าผ่าน:** clone รัน Bridge baseline ได้ (หรือมี blocker log ที่ซื่อสัตย์); มี golden stills เทียบได้

### Phase 1 — แยกเอนจินอย่างระมัดระวัง
1. ดึง Renderer/Post และทดสอบภาพไม่ถอย
2. ดึง Lighting/Materials พร้อมภาพ before-after
3. ดึง Character runtime โดยยัง render Bridge ได้
4. ดึง WorldHost/Camera utilities; ย้ายเนื้อเรื่องสะพานไป `episodes/bridge/`

**ถือว่าผ่าน:** ภาพ Bridge หลัง refactor ยังคงคุณภาพเดิม ไม่หาย ink/DOF/lighting โดยตรวจตามภาพจริง + typecheck + render smoke test

### Phase 2 — ตัวละครของเรา
- ตกลง Character Bible 1 ตัว: หน้า รูปร่าง เส้นขอบ สีหน้า ท่าทาง ชุด 2–3 แบบ
- สร้าง 2.5D runtime พร้อม lighting/contact shadow ที่เข้าฉาก; เทสต์ front/3-4 view
- ถ้าโจทย์ต้องหมุนตัว 360° จริง ให้เปิด workstream 3D rig แยก ไม่แอบแทนด้วย flat sprite

**ถือว่าผ่าน:** คนดูระบุว่าเป็นตัวละครเดิมเมื่อเปลี่ยนเสื้อผ้าและแสง; เทสต์ day/storm ผ่าน

### Phase 3 — สร้างฉาก 'ที่ไม่ใช่สะพาน' สองแบบ
- **Pilot A: Empty City 4 วินาที (120 frames)** — อาคารมีสัดส่วน/ขอบ/ผิว, ถนนมีรายละเอียด, props สื่อว่าเมืองไร้คน, กล้องและ depth ช่วยเล่าเรื่อง; ไม่ใช้ลังกระดาษแทนตึก
- **Pilot B: Storm Ship 4 วินาที** — เรือ/ทะเล/เสา/เชือก/คลื่น/ฝนกับสภาพแสงพายุ, มี hero character จาก Library เดียวกัน
- ทั้งสองใช้ **renderer/post/character engine ชุดเดียวกัน** และสร้างเฉพาะ `.ts`/GLB ของฉาก

**ถือว่าผ่าน:** สองสภาพแวดล้อมต่างกันมากแต่ character style, ink, shading, cinematic quality ยังคงเป็นช่องเดียวกันโดยผู้ใช้ตรวจภาพยอมรับ

### Phase 4 — ผลิตคลิปเต็มจริงหนึ่งตอน
- ทำ script → verified facts → voice → time-coded script → storyboard → detailed scene builds → 4s proof → full animation → mix → render
- QA ด้านภาพ/เสียง/ซับไตเติลภาษาไทยตามความต้องการ
- เก็บ asset recipes ใหม่เพื่อนำกลับมาใช้ในตอนถัดไป

**ถือว่าผ่าน:** ได้ไฟล์ MP4 9:16 30fps ที่มีต้นฉบับโค้ด, QA report, editable episode และสร้างใหม่ได้โดยไม่แตะ core renderer

## 7. Visual QA ที่จะบังคับใช้

ทุกหัวข้อใหม่ต้องมี:
1. อ้างอิง Hero frames จากผลงานของเราเอง 3–5 ภาพ (หรือ reference ที่มีสิทธิ์ใช้)
2. Keyframe stills อย่างน้อย 8 จุด กระจายต้น–กลาง–ท้าย
3. Moving style test 4 วินาที **ก่อน render ตอนเต็ม**
4. Side-by-side audit ตรวจ **ตัวละคร / รูปทรงฉาก / painted texture / ink / lighting / color / depth / composition / motion**
5. ระบุปัญหาเป็น time/frame + สิ่งที่เห็น + root cause ที่ยืนยัน/สมมติ + ไฟล์ที่ต้องแก้
6. Technical gate: ไม่มี missing asset, คอนทราสต์เสีย, lost ink pass, camera clipping, black/white/pop/frozen frames และเสียงไม่ตรง
7. **Human approval gate**: ถึง AI จะให้คะแนนสูงก็ห้ามถือว่าผ่านหากเจ้าของช่องยังเห็นว่างานภาพไม่ใช่

QA เน้นความสวยและการสื่อความ ไม่บังคับว่าทุกฉากต้องมี props จำนวนเท่ากัน—เมืองร้างควรไร้คน แต่ยังต้องมีเรื่องราวอยู่ในสภาพแวดล้อม

## 8. ข้อห้ามที่ทำให้ Empty City ซ้ำรอย

- ห้ามสั่ง Claude เขียน renderer, post, lighting ใหม่ทั้งชุดเพียงเพราะหัวข้อเปลี่ยน
- ห้ามคิดว่า `build.ts` เดิมของ Bridge ใช้สร้างเรือหรือเมืองได้เองโดยไม่เพิ่ม geometry/asset
- ห้ามลดฉากเหลือ primitive boxes เพื่อส่งงานให้จบ
- ห้ามล็อกค่าแสงเดียวสำหรับทุกสถานการณ์; ล็อกคุณภาพและ API แทน
- ห้ามแก้ shared engine หลาย agent พร้อมกันบนไฟล์เดียว
- ห้าม render 60–70 วินาทีเมื่อ 4 วินาทียังหลุดสไตล์
- ห้ามอ้างว่าตัวละคร billboard เป็น full 3D rig
- ห้ามประกาศว่า engine เสร็จหรือภาพตรง benchmark หากไม่มี render evidence

## 9. สิ่งที่จะส่งมอบ ไม่ใช่ Prompt

**ชิ้นงานที่ต้องมีเมื่อพัฒนาสำเร็จ:**
- โปรเจกต์ Three.js + Remotion ที่เปิดและ render ได้จริง
- Shared Engine ที่ทดสอบด้วย baseline Bridge
- Original reusable Character Library
- World/Asset/Animation modules ที่เพิ่มหัวข้อใหม่ได้ด้วย episode-specific TypeScript
- ตัวอย่างวิดีโอ Empty City และ Storm Ship ที่ผ่านการตรวจ
- Episode template ที่เป็น *working code* ไม่ใช่ prompt
- เครื่องมือตรวจ QA, screenshot comparison และบันทึกวิธีแก้

**สิ่งที่เรามีอยู่ตอนนี้:** เอกสารวิเคราะห์, สเปก, ไฟล์จาก repo ต้นฉบับให้ศึกษาภายนอก  
**สิ่งที่ยังไม่มี:** โค้ด engine ที่ refactor แล้ว, character ที่ออกแบบเสร็จ, GLB library, pilot renders, proof of visual quality

## 10. ตัดสินใจที่ยึดไว้

1. เลือก **original 2.5D lit character inside real 3D** เป็นรุ่นแรก ตามลักษณะคลิปเรือ/รถไฟ; full 3D rig เป็น option ถัดไป
2. เปลี่ยนหัวข้อด้วย scene-specific `.ts` + 3D asset ไม่ใช่ rewrite engine
3. Baseline Bridge ต้องไม่เสียคุณภาพหลัง extraction
4. Empty City และ Storm Ship คือสอง pilot ที่พิสูจน์ว่า engine ใช้ข้ามหัวข้อได้
5. ตัดสินจากภาพจริงก่อน scale production

---

### ที่มา
[Original repo](https://github.com/mromidev/claude-animated-shorts) · [Original SKILL](https://github.com/mromidev/claude-animated-shorts/blob/main/SKILL.md) · ตัวอย่างคลิปและบทความจากภาพที่ผู้ใช้ส่งในการสนทนา

*นี่คือข้อสรุปและสเปกงานสำหรับลงมือสร้าง ไม่ใช่คำกล่าวว่าได้ implement แล้ว*
