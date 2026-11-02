# Aniamtion — เราจะสร้าง Animation Studio ของเราเอง

**เอกสารหลัก:** [FINAL_DECISION.md](FINAL_DECISION.md) — **นี่คือข้อสรุปสุดท้ายที่ตกลงกันว่าจะสร้างอะไร** ไม่ใช่ชุด Prompt

**รายการลงมือจริง:** [IMPLEMENTATION_BOARD.md](IMPLEMENTATION_BOARD.md)

## เป้าหมาย

นำองค์ความรู้ทางเทคนิคจาก [mromidev/claude-animated-shorts](https://github.com/mromidev/claude-animated-shorts) มาสกัดเป็น shared visual engine สำหรับผลิต Shorts ที่ใช้ **ตัวละครต้นฉบับของช่องในโลก 3D** และเปลี่ยนหัวข้อได้โดยคุณภาพงานภาพไม่ตก

- **Reuse**: render/post, ink outlines, lighting model, painted textures, depth/camera language
- **Build**: character library, reusable world builders, assets/GLB recipes, animation & episode runtime
- **New per topic**: `.ts` สร้างฉากและเหตุการณ์ เช่น `city.ts`, `ship.ts`, `ocean.ts`, `train.ts`
- **Prove**: Bridge regression → original character → Empty City pilot → Storm Ship pilot → full short

**ไม่ใช่สิ่งที่เราจะทำ:** ล็อกไฟล์ TypeScript ทั้งก้อน, คัดลอกสะพานแล้วเปลี่ยนชื่อ, ใช้แค่ Prompt หรือสั่ง AI ทำคลิปเต็มโดยไม่มีภาพทดสอบ

## เริ่มจากไหน

อ่าน [FINAL_DECISION.md](FINAL_DECISION.md) ทั้งฉบับ แล้วทำ Milestone 0 ใน [IMPLEMENTATION_BOARD.md](IMPLEMENTATION_BOARD.md) ก่อน มันบอกสิ่งที่ต้องเขียน สิ่งที่ต้อง reuse หลักฐานการทดสอบ และเกณฑ์ยอมรับ

## เอกสารประกอบเชิงเทคนิค

- [ENGINE_RULES.md](ENGINE_RULES.md): mapping ไฟล์ Bridge ไปสู่โมดูลใหม่
- [STYLE_BIBLE.md](STYLE_BIBLE.md): กฎภาพที่เราจะคุม
- [CHARACTER_BIBLE_TEMPLATE.md](CHARACTER_BIBLE_TEMPLATE.md): สเปกตัวละครประจำช่อง
- [SCENE_SPEC_TEMPLATE.md](SCENE_SPEC_TEMPLATE.md): สเปกช็อต
- [QA_CHECKLIST.md](QA_CHECKLIST.md): ตรวจคุณภาพ
- [examples/EMPTY_CITY_SCENE_SPEC.md](examples/EMPTY_CITY_SCENE_SPEC.md): ตัวอย่างฉากเมืองร้าง
- [SOURCES_AND_LIMITS.md](SOURCES_AND_LIMITS.md): แหล่งข้อมูล / ข้อจำกัด

## สถานะจริงตอนนี้

เอกสารและข้อสรุปได้ลง GitHub แล้ว **ยังไม่ได้สร้างหรือทดสอบ runtime animation engine** และยังไม่มีภาพ render จาก engine ใหม่ Repo นี้ไม่ได้รวม code ของผู้พัฒนาต้นฉบับหรือ third-party reference frames

เมื่อเริ่ม implementation ค่อยเพิ่มซอร์สพร้อม license notice ที่เกี่ยวข้อง ผล render และ QA evidence ตาม Milestones
