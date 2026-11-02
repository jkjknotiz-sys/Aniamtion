# Aniamtion — our Claude Animated Shorts Skill

**นี่คือการแกะวิธีทำจาก [claude-animated-shorts](https://github.com/mromidev/claude-animated-shorts) เพื่อสร้างคลิปหลายหัวข้อด้วย Claude Code** — ไม่ใช่โปรแกรม Animation Engine ใหม่

## ตอนนี้มีอะไรแล้ว?

- **[SKILL.md](SKILL.md)**: Skill ที่ Claude Code อ่านเพื่อทำงานตาม Workflow ของผู้สร้าง
- **[CODE_MAP.md](CODE_MAP.md)**: แกะบทบาทไฟล์ source ทุกตัวจากคลิป Bridge
- **[templates/bridge/](templates/bridge/)**: โค้ด Three.js/Remotion ต้นฉบับทั้ง 13 ไฟล์ (.ts/.tsx)
- **[templates/scripts/](templates/scripts/)**: สคริปต์ render ภาพนิ่ง, side-by-side comparison, QA และ merge งาน agent
- **[templates/audio/](templates/audio/)**: โค้ดเสียง/ดนตรี/SFX จากต้นฉบับ
- **[references/](references/)**: Style Bible และรายงานวิเคราะห์จากต้นฉบับเป็นข้อความ ไม่มีภาพอ้างอิงที่เป็นของบุคคลอื่น
- **[scripts/analyze_references.py](scripts/analyze_references.py)**: ตัววิเคราะห์คลิปวิดีโอบนเครื่องเองทีละเฟรม สร้าง 2s contact sheets และค่าสถิติ
- **[upstream/SKILL.md](upstream/SKILL.md)**: เก็บ Skill ต้นฉบับไว้เทียบ
- **[LICENSE](LICENSE)**: MIT/copyright ตามต้นฉบับ

## วิธีเอาไปใช้

### 1. ติดตั้ง Claude Skill
Clone Repo **Private** นี้ลงในที่เก็บ Claude Skills ของคุณ (ต้องล็อกอิน GitHub ที่มีสิทธิ์):

~~~bash
git clone https://github.com/jkjknotiz-sys/Aniamtion.git ~/.claude/skills/aniamtion-shorts
~~~

หากมีพื้นที่/สิทธิ์ไม่พอ ให้ใช้ GitHub Desktop Clone Repo แล้วคัดลอกโฟลเดอร์ไปยังตำแหน่ง Claude skills ในเครื่องของคุณ

### 2. เตรียม Project Render (สำคัญ)
ใช้ Remotion project ที่มี Three.js และ dependencies อย่าง `remotion`, `@remotion/three`, `three`, `@react-three/fiber`, `@react-three/postprocessing` และ `postprocessing` หรือโปรเจกต์ที่คุณมีอยู่แล้ว

**Repo นี้ไม่ใช่ Remotion app สำเร็จรูป:** ไม่มี `package.json`, `src/index.ts`, registration/Root และ GLB assets ที่ใช้ใน Bridge เช่น `public/bridge/kenney/*.glb`. Claude ต้องตรวจแล้วเตรียมก่อน Render; สคริปต์ต้นฉบับบางตัว hardcode Windows Chrome path

ตัวอย่าง bridge source จะอยู่ใน Skill; เมื่อจะใช้งานต้อง copy/integrate ไปใน Remotion project ที่คุณต้องการ Render หลีกเลี่ยงแก้ source เริ่มต้นโดยตรง

### 3. ส่งวิดีโออ้างอิงให้ Claude Code **ครั้งแรก**
เก็บวิดีโออ้างอิงบนเครื่อง เช่น `~/reference-videos/` ไม่ต้อง push ไฟล์ลิขสิทธิ์ขึ้น GitHub

วิเคราะห์ทีละเฟรม (30 fps เป็นเป้าหมาย ถ้าคลิปต้นทางไม่ใช่ 30fps ให้รายงาน fps จริง):
~~~bash
python -m pip install numpy Pillow opencv-python-headless
python ~/.claude/skills/aniamtion-shorts/scripts/analyze_references.py --input ~/reference-videos --out ~/animation-study
~~~

Claude อ่าน contact sheets และรายงาน → ถอด style ของเรา → บันทึกไว้ในไฟล์ส่วนตัวของโปรเจกต์ (อย่าเขียนทับ upstream reports)

### 4. สร้างคลิป
เปิด Claude Code ภายใน Remotion project ที่เตรียมไว้ แล้วบอก:
"ใช้ Skill aniamtion-shorts ศึกษาคลิปอ้างอิงและ Source Code ของ Bridge จากนั้นสร้างคลิปเรื่อง [หัวข้อ] ด้วยฉากและ .ts ที่เหมาะกับเรื่องใหม่ ต้อง Render stills เทียบ reference และแก้ภาพจนผ่านก่อน Render final"

นี่เป็นคำสั่งเรียกใช้งานสั้น ๆ เท่านั้น **หัวใจจริงอยู่ที่ source, measurements, renderer และการแก้ภาพ**

## หมายเหตุสถานะ

- ✅ Skill instructions, upstream source snapshot, original QA scripts/reports are in GitHub.
- ⏳ ยังไม่ได้ run/render ในเครื่องนี้เพื่อยืนยันว่า dependencies / 3D assets / script compatibility ใช้งานได้จริง
- ⏳ ยังไม่ได้สร้าง original character และ episode ใหม่จากคลิปที่ผู้ใช้ส่ง
- ✅ เก็บ source MIT พร้อม LICENSE; ไม่คัดลอก original reference photos/videos

**เอกสารที่เหลือจากการคุยเดิม** เช่น FINAL_DECISION.md, IMPLEMENTATION_BOARD.md, prompts/ ไม่ใช่แหล่งหลักของ Skill และไม่ใช่งานที่เราจะพัฒนาต่อเป็น Animation Engine; ยึด [SKILL.md](SKILL.md) และ [CODE_MAP.md](CODE_MAP.md) แทน

### Upstream provenance
From `mromidev/claude-animated-shorts` commit `e3b817b6afc6cd413466d43f11ba31209e034bbf`. Copied code/docs remain under upstream MIT terms. Reference images/sheets intentionally excluded.
