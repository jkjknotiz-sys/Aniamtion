# Aniamtion — our Codex Animated Shorts Skill

**นี่คือการแกะวิธีทำจาก [claude-animated-shorts](https://github.com/mromidev/claude-animated-shorts) เพื่อสร้างคลิปหลายหัวข้อด้วย Codex** — ไม่ใช่โปรแกรม Animation Engine ใหม่

## ตอนนี้มีอะไรแล้ว?

- **[SKILL.md](SKILL.md)**: Agent Skill ที่ Codex อ่านเพื่อทำงานตาม Workflow ของผู้สร้าง
- **[CODE_MAP.md](CODE_MAP.md)**: แกะบทบาทไฟล์ source ทุกตัวจากคลิป Bridge
- **[references/OUR_STYLE_BIBLE.md](references/OUR_STYLE_BIBLE.md)**: ผลวิเคราะห์สองคลิปของเรา 3,892 เฟรม / 66 Contact Sheets (ยังรอทบทวน Hero Frames)
- **[references/BRIDGE_RENDER_DIAGNOSTIC_TH.md](references/BRIDGE_RENDER_DIAGNOSTIC_TH.md)**: ประวัติการแก้ภาพฟ้าล้วนและ GLB (ล่าสุดผู้ใช้เติม GLB 26/26 ในโปรเจกต์ท้องถิ่นแล้ว)
- **[references/PRODUCTION_QUALITY_STANDARD.md](references/PRODUCTION_QUALITY_STANDARD.md)**: กฎบังคับ Storyboard, Physical Acting, Cinematic Composition, Quality Gates และวิธีเก็บบทเรียนข้ามตอน
- **[references/LESSONS_RED_BUTTON_TOWN.md](references/LESSONS_RED_BUTTON_TOWN.md)**: บทเรียนจาก Storyboard 12 ช็อตเรื่องปุ่มแดงที่ผู้ใช้ไม่พอใจ
- **[references/TUTORIAL_TECHNIQUES_TH.md](references/TUTORIAL_TECHNIQUES_TH.md)**: แกะ Workflow ผู้สอนจากคำบรรยายพร้อมเวลา
- **[templates/bridge/](templates/bridge/)**: โค้ด Three.js/Remotion ต้นฉบับทั้ง 13 ไฟล์ (.ts/.tsx)
- **[templates/scripts/](templates/scripts/)**: สคริปต์ render ภาพนิ่ง, side-by-side comparison, QA และ merge งาน agent
- **[templates/audio/](templates/audio/)**: โค้ดเสียง/ดนตรี/SFX จากต้นฉบับ
- **[references/](references/)**: Style Bible และรายงานวิเคราะห์จากต้นฉบับเป็นข้อความ ไม่มีภาพอ้างอิงที่เป็นของบุคคลอื่น
- **[scripts/analyze_references.py](scripts/analyze_references.py)**: ตัววิเคราะห์คลิปวิดีโอบนเครื่องเองทีละเฟรม สร้าง 2s contact sheets และค่าสถิติ
- **[upstream/SKILL.md](upstream/SKILL.md)**: เก็บ Skill ต้นฉบับไว้เทียบ
- **[LICENSE](LICENSE)**: MIT/copyright ตามต้นฉบับ

## วิธีเอาไปใช้

### 1. ติดตั้ง Agent Skill ใน Codex
สำหรับ Codex ให้ใช้ตำแหน่ง repo-local `.agents/skills/aniamtion-shorts/` หรือ Skill directory ที่ Codex ตั้งค่าไว้ โดยโฟลเดอร์ Skill ต้องมี `SKILL.md` อยู่ที่ระดับบนสุด (Repo นี้เป็น Private จึงต้องล็อกอิน GitHub ที่มีสิทธิ์):

~~~bash
git clone https://github.com/jkjknotiz-sys/Aniamtion.git .agents/skills/aniamtion-shorts
~~~

หากติดตั้ง Skill อยู่แล้วไม่ต้องติดตั้งซ้ำ ให้ `git pull` ที่โฟลเดอร์เดิม การที่ Codex วิเคราะห์ 2 คลิปได้สำเร็จแปลว่า workflow วิเคราะห์เริ่มทำงานแล้ว แต่ยังไม่ใช่หลักฐานว่า Render ผ่าน

### 2. เตรียม Project Render (สำคัญ)
ใช้ Remotion project ที่มี Three.js และ dependencies อย่าง `remotion`, `@remotion/three`, `three`, `@react-three/fiber`, `@react-three/postprocessing` และ `postprocessing` หรือโปรเจกต์ที่คุณมีอยู่แล้ว

**Repo นี้ไม่ใช่ Remotion app สำเร็จรูป:** ไม่มี `package.json`, `src/index.ts`, registration/Root และ GLB assets ที่ใช้ใน Bridge เช่น `public/bridge/kenney/*.glb`. Codex ต้องตรวจแล้วเตรียมก่อน Render; สคริปต์ต้นฉบับบางตัว hardcode Windows Chrome path

ตัวอย่าง bridge source จะอยู่ใน Skill; เมื่อจะใช้งานต้อง copy/integrate ไปใน Remotion project ที่คุณต้องการ Render หลีกเลี่ยงแก้ source เริ่มต้นโดยตรง


### ตรวจ Kenney GLB 26 ชิ้นด้วย Codex (อ่านอย่างเดียว)
ก่อนสร้างคลิปใหม่ ให้ใช้ `scripts/audit_kenney_assets.py` ตรวจชื่อไฟล์จาก `templates/bridge/world.ts`, โครงสร้าง GLB จริง และค้นหา candidate ใน pack ที่ดาวน์โหลดจากเว็บไซต์ทางการ:

~~~powershell
$skill = "$HOME\.codex\skills\aniamtion-shorts"
git -C $skill pull --ff-only
py "$skill\scripts\audit_kenney_assets.py" --public-dir "D:\Facebook Reel\bridge-march-thai\public" --out "D:\Facebook Reel\bridge-march-thai\out\bridge-debug\asset-audit"
# ถ้าดาวน์โหลด ZIP/แตก pack แล้ว ให้เพิ่ม --pack "D:\PATH\TO\kenney-pack.zip" ได้ซ้ำหลายครั้ง
~~~

ผลลัพธ์: `KENNEY_ASSET_AUDIT.md`, `kenney_asset_audit.json`. Exit code 2 หมายถึงไฟล์ยังไม่ครบ/ไม่ถูกต้อง (ไม่ใช่สคริปต์เสีย); ไม่มีการคัดลอกหรือเปลี่ยนไฟล์ใด ๆ เอง การ match ชื่อและตรวจ GLB header ไม่รับรองว่าโมเดลหน้าตาเหมือนต้นฉบับ ต้องตรวจด้วยภาพและ Render อีกครั้ง

### 3. ส่งวิดีโออ้างอิงให้ Codex **ครั้งแรก**
เก็บวิดีโออ้างอิงบนเครื่อง เช่น `~/reference-videos/` ไม่ต้อง push ไฟล์ลิขสิทธิ์ขึ้น GitHub

วิเคราะห์ทีละเฟรม (30 fps เป็นเป้าหมาย ถ้าคลิปต้นทางไม่ใช่ 30fps ให้รายงาน fps จริง):
~~~bash
python -m pip install numpy Pillow opencv-python-headless
python ~/.codex/skills/aniamtion-shorts/scripts/analyze_references.py --input ~/reference-videos --out ~/animation-study
~~~

Codex อ่าน contact sheets และรายงาน → ถอด style ของเรา → บันทึกไว้ในไฟล์ส่วนตัวของโปรเจกต์ (อย่าเขียนทับ upstream reports)

### 4. สร้างคลิปโดยใช้บทเรียนจากงานเก่า
ก่อนทำทุกตอน Codex ต้องอ่าน `references/PRODUCTION_QUALITY_STANDARD.md` และ `references/LESSONS_RED_BUTTON_TOWN.md` ผ่าน `SKILL.md` เสมอ. ตรวจ Storyboard ไม่ใช่แค่จำนวนภาพ แต่รวม acting/prop contact, twist reveal, composition และคุณภาพจริงจากการ Render ด้วย. หากเห็นปัญหา ให้ตั้งสถานะ BLOCKED_ACTION หรือ BLOCKED_VISUAL แล้วแก้/ตรวจซ้ำก่อน full render.

เปิด Codex ใน Remotion project ที่เตรียมไว้ แล้วบอก:
"ใช้ Skill aniamtion-shorts อ่าน references/OUR_STYLE_BIBLE.md ที่วิเคราะห์ไว้แล้วก่อน ไม่ต้องวิเคราะห์คลิปรถไฟ/เรือซ้ำ ตรวจ dependencies และ GLB ของ Bridge ทำให้ Render stills ต้นฉบับได้ก่อน แล้วค่อยสร้างตอนใหม่ผ่านโค้ด .ts เฉพาะเรื่อง"

นี่เป็นคำสั่งเรียกใช้งานสั้น ๆ เท่านั้น **หัวใจจริงอยู่ที่ source, measurements, renderer และการแก้ภาพ**

## หมายเหตุสถานะ

- ✅ Skill instructions, upstream source snapshot, original QA scripts/reports are in GitHub.
- ✅ ผู้ใช้ทดสอบ Render Bridge 90 เฟรมและ Empty City 120 เฟรมผ่านในโปรเจกต์ Remotion ท้องถิ่น รวมถึงคืนโมเดล GLB 26/26 แล้ว (ไม่ได้อัปโหลดโมเดลหรือ runtime ทั้งชุดไว้ใน Skill repo)
- ✅ Codex ได้วิเคราะห์คลิปอ้างอิง 2 คลิป 3,892 เฟรมแล้ว; [OUR_STYLE_BIBLE.md](references/OUR_STYLE_BIBLE.md) ถูกเก็บไว้แล้วและยังรอผู้ใช้ยืนยัน hero frames
- ✅ มี Storyboard เมืองปุ่มแดง 12 ช็อต ความยาวประมาณ 54 วินาทีจาก Codex แต่ผู้ใช้ **ยังไม่พอใจคุณภาพ** และไม่มีหลักฐานว่า Full Video ผ่านการอนุมัติ
- ⏳ ตัวละครต้นฉบับของช่องและความสม่ำเสมอเชิงศิลป์ของหลายตอนยังไม่ผ่าน human approval
- ✅ เก็บ source MIT พร้อม LICENSE; ไม่คัดลอก original reference photos/videos

**แผนเก่าที่ไม่ตรงโจทย์** ถูกเก็บไว้ที่ [archive/early-planning/](archive/early-planning/) เพื่อไม่ให้ปะปนกับ Skill จริง; ให้ยึด [SKILL.md](SKILL.md) และ [CODE_MAP.md](CODE_MAP.md) เป็นหลัก

### Upstream provenance
From `mromidev/claude-animated-shorts` commit `e3b817b6afc6cd413466d43f11ba31209e034bbf`. Copied code/docs remain under upstream MIT terms. Reference images/sheets intentionally excluded.
