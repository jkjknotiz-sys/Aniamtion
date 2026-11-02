# Production Quality Standard — กฎที่ Codex ต้องใช้กับทุกตอน

**เป้าหมาย:** ให้ผลลัพธ์ดีขึ้นโดยเรียนรู้จากการ Render และคำวิจารณ์ของผู้ใช้ ไม่ใช่ทำคลิปแต่ละตอนจากศูนย์หรือแค่เพิ่มจำนวน reference. เอกสารนี้เป็นข้อกำหนดกระบวนการ/การกำกับ ไม่ใช่รหัสโปรแกรม Animation Engine ใหม่

**ลำดับความสำคัญ:** ความเข้าใจเรื่องและการกระทำที่เชื่อได้ → ช็อตที่เล่าเรื่อง → คุณภาพแสง/วัสดุ/องค์ประกอบ → ความลื่นไหล → technical QA. การที่ Remotion ส่ง MP4 ได้/ไม่มีเฟรมดำเป็นเพียงเงื่อนไขทางเทคนิค ไม่ใช่การอนุมัติคุณภาพ

## 1. ก่อนเขียนโค้ด: Story-first + physical-event plan

สำหรับทุกฉากและทุกช็อตให้ระบุข้อมูลต่อไปนี้ **ก่อน** เริ่ม implementation:
- **Narrative point:** ผู้ชมควรเข้าใจ/รู้สึกอะไรภายใน 1–3 วินาทีนี้
- **Action:** ใครทำอะไรกับวัตถุใด ที่ตำแหน่งโลกและสเกลใด
- **Cause → effect:** การกระทำนั้นก่อผลที่อ่านออกบนภาพอย่างไร และมี reaction ของคน/สิ่งแวดล้อมอย่างไร
- **Camera:** ภาพกว้าง/กลาง/ใกล้เพื่ออะไร และโฟกัสอะไร ไม่ใช่เพียงสุ่ม lens/move
- **Layout/lighting:** subject separation, silhouettes, depth planes, value contrast, surface detail ที่มีประโยชน์ต่อช็อต
- **Asset + code requirement:** อะไร reuse, อะไรต้องทำเพิ่มเป็น scene-specific .ts/.glb; ถ้าตัวละคร 2.5D card หมุนไม่ได้จริงให้เลือกมุมอย่างซื่อสัตย์
- **Reveals:** ถ้ามีจุดหักมุม ให้ระบุข้อมูลที่ผู้ชมยัง *ไม่ควรเห็น* ก่อนถึงช็อตเฉลย

**ห้าม** ตีความว่า "ต้องมี 12 ช็อต/54 วินาที" เป็นมาตรฐานตายตัว จำนวนช็อตขึ้นกับบท. แต่ทุกช็อตต้องพาเรื่องไปข้างหน้า ช็อตที่ไม่มีความหมายต้องรวม ปรับ หรือตัด

## 2. กฎความน่าเชื่อถือทางกายภาพ (physical credibility) — รวมถึงเรื่องแฟนตาซี/ของเล่น

การกระทำสำคัญ (กดปุ่ม, หยิบของ, เปิดประตู, ขึ้นเรือ, พื้นยุบ, รถชน, คนสะดุด) ต้องมี **ลำดับที่มองเห็นได้**:
1. Setup — เห็นตำแหน่ง actor, prop, ระยะ, สเกล และจุดที่จะสัมผัส
2. Anticipation — ส่วนร่างกาย/วัตถุเข้าใกล้ เปลี่ยนท่าหรือจังหวะก่อนออกแรง
3. Contact — นิ้ว/เท้า/มือสัมผัส **surface ของ 3D geometry จริง** ไม่ลอย ไม่ทะลุ ไม่สลับความลึก
4. Force / deformation — วัตถุมีปฏิกิริยาตามชนิดวัสดุ/กลไก; ปุ่มต้องยุบ, คันโยกต้องหมุน, ประตูต้องเคลื่อนไปบนบานพับ
5. Consequence — ภาพ เสียง สีหน้า/องค์ประกอบฉากตอบสนอง **หลัง** การสัมผัส โดย timing ถูกต้อง
6. Settle / follow-through — ลดแรง คืนสภาพหรือค้างในสถานะใหม่ตามเนื้อเรื่อง; continuity ข้ามช็อตไม่เปลี่ยนสถานะมั่ว

ตัวอย่างปุ่ม:
- นิยาม `capRestY`, `pressDepth`, `pressProgress` และตำแหน่ง `contactPointWorld`; อย่าย้ายมือด้วย screen-space อย่างเดียวโดยไม่ตรวจ world-space alignment
- แยก cap เป็น mesh/transform group ที่เลื่อนได้จริง (หรือ animation equivalent), สร้างสปริง/จังหวะหยุด/เสียงกดและการเปลี่ยนแสง **ตาม** frame contact
- Motion path ของมือ/นิ้วและปุ่มต้องใช้ฐาน coordinate เดียวกัน; ถ้ามีตัวละครแบบ Canvas2D card มืออาจต้องมีแขน/มือเป็น separate 3D proxy สำหรับช็อต close-contact หรือออกแบบมุมที่ไม่โชว์ความผิดของ card
- ถ้า "มือยักษ์" เป็นส่วนหนึ่งของ twist เรื่องโลกของเล่น ให้สเกลและแรงมีเจตนาและ **คุมเวลา reveal**; ปรากฏก่อนเฉลยโดยไม่มี hint/perspective ที่พอดีทำให้เรื่องเฉลยเร็วเกินไป
- ต้องตรวจทั้ง before contact, first touch, full press, release/consequence **เป็นภาพจริงจาก Renderer**; storyboard ภาพเดียวพิสูจน์การกดจริงไม่ได้

**Gate B (blocker):** ถ้ากระทำสำคัญไม่มีหลักฐาน contact/deformation/timing หรือเกิด clipping/teleport ให้แก้ shot code/animation ก่อน render full video

## 3. Art direction — ไม่ใช่เพิ่มกล่อง/props แบบสุ่ม

ต้องกำกับแต่ละช็อตเหมือนภาพยนตร์การ์ตูนสั้น:
- **Focal hierarchy:** มี hero subject เด่นทันที, contrast/scale/eye-line พาสายตา; foreground/midground/background ใช้ตามความหมาย ไม่ฝืนทุกช็อต
- **Variation:** อาคารไม่ใช่ก้อน/หน้าต่างซ้ำแพตเทิร์น; silhouette, dimensions, awnings, roofline, doors, trims, weathering, signs และ narrative props มีความหลากหลายที่สอดคล้องโลก
- **Character acting:** ความรู้สึกผ่าน head tilt, eyes, eyebrows, body shift, hands, secondary motion และ reaction to events; เปลี่ยน pose ทุกช็อตด้วยเหตุผล ไม่ใช่แค่วางคนหน้าตรง
- **Lighting:** ใช้ preset ที่เหมาะโลก ไม่ล็อกให้เป็นฟ้าสีเดียวกันทุกเรื่อง. มิติ = directional key/fill/rim, contact shadows, motivated practical lights, atmospheric depth และการแยก value
- **Material readability:** painted texture, wear, seams, relief และ silhouette detail เห็นเมื่ออยู่ระยะกล้องที่ใช้งานจริง; เบลอ DOF ต้องช่วยเล่าเรื่อง ไม่ใช่ซ่อนขาดรายละเอียด
- **Color/story:** สีของ environment เล่าบรรยากาศได้ ขณะที่ character identity/ink vocabulary ยังคงสม่ำเสมอ; เปรียบเทียบ reference ที่ชนิด shot และสภาพแสงใกล้กัน
- **Typography:** ถ้ามีข้อความภาษาไทยบนป้าย/ฉาก/ซับ ต้องอ่านจริงด้วยฟอนต์รองรับภาษาไทย, ไม่ถูกบิดเมื่อเล็ก/เอียง และตรวจด้วยสายตา. อย่าใช้ข้อความประหลาดที่อ่านไม่ได้เป็นเพียง decorative label
- **Shot diversity:** อย่างน้อยต้องพิสูจน์เหตุผลที่เปลี่ยนจาก wide → medium → close → insert → reaction → reveal; ไม่เปลี่ยนกล้องเพื่อความแปลกใหม่เฉย ๆ ไม่ซ้ำ 4 shot ที่ไม่มีข้อมูลใหม่

**Gate A (blocker):** ภาพเบลอ/แบน/โล่งโดยไม่มีเหตุทางเรื่อง, focal point อ่านไม่ออก, มุมภาพผิด anatomy, repetitive scene ภายใต้ช็อตสำคัญ หรือ twist ถูกเปิดเผยเร็วกว่าที่ตั้งใจ → recompose/reshoot ไม่ใช่ปล่อยผ่านเพราะ Technical QA ผ่าน

## 4. Twist/reveal staging

ถ้าเป็นเรื่องหักมุมให้เขียน **reveal contract**:
- What viewer believes at the beginning
- What clues are allowed before pivot
- What is forbidden to show before pivot
- The exact visual evidence that changes the viewer's understanding
- The emotional/visual reaction after pivot

ตัวอย่าง "เมืองเป็นของเล่น": ช่วงต้นให้สร้างภาพเมืองและคนอย่างมี scale consistency. ถ้าจะแสดงนิ้วมหึมาแต่ต้น ต้องตั้งใจให้เป็น hint ที่ผู้ชมยังไม่เข้าใจ ไม่ใช่โชว์ลักษณะโลกของเล่นชัดเจนทันที; หรือเลื่อน shot มือไปตอนท้ายเมื่อ payoff ถึงเวลา. ไม่ใช้คำบรรยายมาแทน visual proof

## 5. Quality Gates ตามลำดับ (ต้องมี evidence)

**Gate 0 — Episode brief & evidence**
- หัวข้อ, target audience, tone, runtime; fact checks ถ้าเป็นสารคดี
- Approved user reference set, source modules, local asset rights, character visual identity
- ถ้า Reference ไม่พอสำหรับฉากเฉพาะเรื่อง ให้เลือก reference ใหม่อย่างมีเป้าหมาย ไม่สุ่มยัดเพิ่ม
- Outcome: one-page visual/story intent + list of production risks

**Gate 1 — Story/Storyboard signoff**
- Storyboard แต่ละ shot แสดงเรื่อง/จุดหักมุม/มุมกล้อง/แสง/ตัวละคร/วัตถุ/interaction
- Rendered storyboard frames จาก Three.js (ถ้ามี project พร้อม) และ review sheet เทียบ approved shot-compatible references
- **Screen images alone are insufficient for physical actions**: ต้องมี action keyframes สี่สถานะขึ้นไปในช็อต interaction
- Codex ต้อง *วิจารณ์ภาพตัวเองเชิงรูปธรรม* และติดป้าย REWORK เมื่อยังไม่สวย/ไม่สมจริง; ไม่เขียน "PASS" แค่ไฟล์ครบ
- ถ้าผู้ใช้ต้องการดู/อนุมัติ storyboard ให้หยุดก่อน full render

**Gate 2 — Hero-shot look & action tests**
- สำหรับช็อตสำคัญอย่างน้อย 1 ภาพ wide, 1 character, 1 environmental detail, 1 physical interaction, 1 reveal (เฉพาะประเภทที่เรื่องมี)
- Render 4–8 วินาทีของ action ที่ยาก + before/contact/after frame sequence
- เปรียบเทียบ side-by-side, ตรวจ silhouette, depth, expression, gestures, contact, shadows, moving camera, texture detail, foreground scale, palette
- ปัญหา blocker ทุกข้อบันทึก frame/time + symptom + source file/function + proposed technical fix + retest result

**Gate 3 — Full production**
- ทำได้หลัง Gate 1–2 ผ่าน; แต่ละ shot ใช้ logic tested เดียวกัน ไม่แค่ยืด static stills
- Voice → phrase timings → shots/animations → sound effects ที่ตรง visual impact
- No undefined dependencies, silent asset substitution, rewrite of proven shaders, or non-Thai-safe subtitles

**Gate 4 — Final evidence**
- MP4, full-res stills, QA report, reference comparison, source files, documented limitations
- Technical checks: fps, black/frozen/pop, missing assets, warnings, audio sync and subtitle safe area
- Artistic checks: purpose of scenes, variety, acting, physical plausibility, readability, twist clarity
- Human visual approval is final. If not approved, record *why* and route to a specific fix; do not call it production-ready

## 6. Mandatory reusable learning loop — ทุกครั้งที่ผู้ใช้ติ

1. Capture feedback *verbatim enough to preserve the issue* + episode + screenshot/frame if available.
2. Categorize root cause: story / cinematography / acting / physics-contact / environment / lighting / material / post / audio / typography / technical.
3. Link symptom to actual offending scene-specific source `.ts/.tsx` **after reading it**, and to shared source code *only if proven*.
4. Apply smallest fix and render comparable before–after evidence, including interaction frames if applicable.
5. Convert a **generalizable** lesson into Skill rule or reusable scene recipe; keep episode-specific details in a case log. Avoid hardcoding one story's props into every future topic.
6. Add a regression example: what screenshot or action sequence next episode must show to prove this bug was avoided.
7. If untested, label "proposed" not "verified"; do not claim automatic model training or improvement without repeat tests.

**Important:** Codex is not retrained by more references. It improves *conditional performance* by accessing approved visual evidence, code patterns, lessons, tested examples and rigorous review. The user must still judge the artwork.

## 7. Required report structure

Each episode must leave `episode/PRODUCTION_REVIEW.md` with:
- Story intent + what reference/style source was used
- Table: shot | visual intent | camera | actions/physical states | required assets/geometry | review status
- Critical action evidence: `time/frame → anticipation → contact → consequence → settle`
- Top five artistic defects with frame/path/code owner
- Before–after stills and motion-proof paths; objective technical results separately from subjective approval
- Status: `BLOCKED_STORY` / `BLOCKED_ACTION` / `BLOCKED_VISUAL` / `TECHNICALLY_RENDERED_NOT_APPROVED` / `APPROVED`
- Reusable rules learned and proposed Skill updates

**Never emit a blanket "looks professional" judgment without images and evidence.**