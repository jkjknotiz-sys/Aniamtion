# Aniamtion — Visual-Consistent Animated Shorts Studio

> ชุดเอกสารออกแบบการผลิต Shorts: ตัวละครเอกลักษณ์ของช่อง + โลก 3D ที่เปลี่ยนเรื่องได้ + QA ก่อนเรนเดอร์  
> **สถานะ: planning / prompt kit — ยังไม่ใช่เอนจินแอนิเมชันที่รันได้หรือทดสอบผ่านแล้ว**

## เป้าหมาย

แก้ปัญหา **Bridge ดูดี แต่ Empty City คุณภาพตกเมื่อเปลี่ยนหัวข้อ** โดยสกัดส่วนที่ใช้ซ้ำได้จาก [mromidev/claude-animated-shorts](https://github.com/mromidev/claude-animated-shorts) มาเป็น shared visual pipeline แทนการคัดลอกเรื่องสะพานแล้วให้ AI เขียนใหม่ทั้งระบบ

**สิ่งที่ต้องคงอยู่:** เอกลักษณ์ตัวละคร, แนวการลงแสง/เงา, ink outlines, painted textures, color grading, depth cues, cinematic camera language และการตรวจเฟรม  
**สิ่งที่ต้องเปลี่ยนได้:** บท, โลเคชัน, โมเดล, props, ชุดตัวละคร, การจัดแสงเฉพาะเหตุการณ์, animation และกล้องแต่ละช็อต

## เริ่มใช้อย่างไร

1. อ่าน **STYLE_BIBLE.md** แล้วเลือก reference ภาพที่คุณมีสิทธิ์ใช้ 3–5 ภาพ; ใส่ภาพต้นแบบงานของตัวเองไว้ในโปรเจกต์ท้องถิ่น (ไม่ต้องอัปโหลดภาพของผู้อื่น)
2. อ่าน **ENGINE_RULES.md** ก่อนแตะโค้ดเดิม แยกให้ชัดว่าเป็น reusable visual engine หรือ episode-specific code
3. ใช้ **CHARACTER_BIBLE_TEMPLATE.md** ออกแบบตัวละครประจำช่องและทำ turnarounds/expressions
4. ทำ spec รายช็อตด้วย **SCENE_SPEC_TEMPLATE.md**; ดูตัวอย่าง **examples/EMPTY_CITY_SCENE_SPEC.md**
5. ใช้ **prompts/4_SECOND_STYLE_TEST.md** สั่ง Claude Code สร้างเทสต์ 4 วินาที *ก่อนคลิปเต็ม*
6. ตรวจภาพกับ **QA_CHECKLIST.md**; ถ้าไม่ผ่านให้ใช้ **prompts/VISUAL_AUDIT.md** แก้เป็นข้อ ๆ
7. เมื่อเทสต์ผ่าน ใช้ **prompts/NEW_EPISODE.md** และ **CLAUDE_WORKFLOW.md** ดำเนินการจนได้คลิปเต็ม
8. ถ้าจะดึงโค้ดออกมาเป็นเอนจินกลาง ให้ใช้ **prompts/ENGINE_REFACTOR.md** ทีละขั้น อย่าทุบทั้งโปรเจกต์

## เอกสารใน repo

| ไฟล์ | ใช้เมื่อ |
|---|---|
| [STYLE_BIBLE.md](STYLE_BIBLE.md) | ตั้งกฎภาพและเกณฑ์วัด |
| [CHARACTER_BIBLE_TEMPLATE.md](CHARACTER_BIBLE_TEMPLATE.md) | ออกแบบตัวละครและการแต่งตัวซ้ำข้ามตอน |
| [ENGINE_RULES.md](ENGINE_RULES.md) | แยกไฟล์ TypeScript ที่ควร reuse/extend/create |
| [CLAUDE_WORKFLOW.md](CLAUDE_WORKFLOW.md) | ขั้นตอนผลิตงานจาก brief ถึง final |
| [SCENE_SPEC_TEMPLATE.md](SCENE_SPEC_TEMPLATE.md) | spec ฉากเพื่อไม่ให้ AI สร้างเมืองโล่ง |
| [QA_CHECKLIST.md](QA_CHECKLIST.md) | pass/fail + บันทึก defects |
| [prompts/4_SECOND_STYLE_TEST.md](prompts/4_SECOND_STYLE_TEST.md) | prompt สร้างตัวอย่าง 4 วินาที |
| [prompts/VISUAL_AUDIT.md](prompts/VISUAL_AUDIT.md) | prompt ตรวจเฟรมและจับ root cause |
| [prompts/NEW_EPISODE.md](prompts/NEW_EPISODE.md) | prompt สร้างเรื่องใหม่ |
| [prompts/ENGINE_REFACTOR.md](prompts/ENGINE_REFACTOR.md) | prompt แยก Bridge-specific code |
| [examples/EMPTY_CITY_SCENE_SPEC.md](examples/EMPTY_CITY_SCENE_SPEC.md) | ตัวอย่างฉากใหม่แบบมีรายละเอียด |
| [SOURCES_AND_LIMITS.md](SOURCES_AND_LIMITS.md) | ที่มาและสิ่งที่ยังไม่ได้พิสูจน์ |

## หลักการทำงาน

**First make it match, then make it scale.** ต้องทดสอบความสม่ำเสมอของภาพจาก *อย่างน้อยสอง environment ที่ต่างกันจริง* เช่น เมืองร้างกลางวันและดาดฟ้าเรือกลางพายุ ก่อนประกาศว่า engine ใช้ซ้ำได้

- มาตรฐาน output เริ่มต้น: แนวตั้ง 9:16, 30 FPS; ทดสอบที่ขนาดต่ำก่อนออก final
- แยก **visual engine** ออกจาก **content/world per episode**
- อนุญาตให้แก้ presets ตามบริบท เช่น พายุ/พระอาทิตย์ตก แต่รักษากฎทางศิลป์และ composition
- ห้ามใช้คะแนน AI เป็นหลักฐานแทนการดูของคน ต้องมี human approval สำหรับ hero frames
- ห้ามให้ agent แก้ไฟล์ส่วนกลางพร้อมกัน ให้แยก owner, branch หรือ sandbox
- อย่า render full 60s จนกว่า 4s test และ storyboard stills ผ่าน

## การใช้กับ Claude Code

เปิดโปรเจกต์ของคุณที่ติดตั้ง Three.js/Remotion แล้วส่ง prompt ที่อยู่ในโฟลเดอร์ prompts/ ให้ Claude Code โดย **อ่านไฟล์จริงและกำหนด working paths ก่อนรัน** เอกสารชุดนี้ไม่มี package.json จึงยังรัน Remotion โดยตัวเองไม่ได้

ตัวอย่าง:
~~~text
Read README.md, ENGINE_RULES.md, STYLE_BIBLE.md and prompts/4_SECOND_STYLE_TEST.md.
Inspect my actual Remotion project. Do not assume paths exist.
Create a 4-second visual baseline test using my approved references.
Do not edit the original bridge project; work in a new directory/branch.
Return still frames and an explicit PASS/FAIL report before full rendering.
~~~

## ขอบเขตและเครดิต

- เอกสารชุดนี้เป็นคำแนะนำใหม่ ไม่ใช่ fork ที่มี code ของผู้สร้างต้นฉบับ
- อ้างอิงเชิงเทคนิคจาก [README](https://github.com/mromidev/claude-animated-shorts/blob/main/README.md) และ [SKILL.md](https://github.com/mromidev/claude-animated-shorts/blob/main/SKILL.md) ของต้นฉบับ ดูรายละเอียดใน SOURCES_AND_LIMITS.md
- หากคัดลอกโค้ด MIT เข้ามาภายหลัง ต้องเก็บ LICENSE และ copyright notice ที่เกี่ยวข้อง; รูป reference ของบุคคลอื่นไม่ใช่ assets สำหรับเผยแพร่ซ้ำ
