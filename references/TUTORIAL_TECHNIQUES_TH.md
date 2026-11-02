# แกะ Workflow จากคลิป “How to Make Viral Animated Shorts Using Claude (Full Workflow)”

**ที่มา:** คำบรรยายพร้อมเวลาของวิดีโอที่ผู้ใช้ส่งในแชต และ Source Code ที่ผู้สร้างเผยแพร่ใน GitHub; **ยังไม่ได้ตรวจวิดีโอ MP4 ทั้งหมดแบบภาพต่อภาพในสภาพแวดล้อมนี้**  
**ใช้เอกสารนี้เพื่อให้ Claude Code เข้าใจวิธีของผู้สร้าง ไม่ใช่ทำสำเนาวิดีโอที่ศึกษา**

## ไทม์ไลน์การทำจริง

| เวลาในคลิป (ประมาณ) | สิ่งที่ผู้สร้างทำ | ความหมายต่อ Skill เรา |
|---|---|---|
| 0:37 | อธิบายภาพแบบ 2D characters ใน 3D world | อย่าเรียกตัวละคร flat card ว่า fully rigged 3D |
| 0:46–1:35 | ให้ Claude ศึกษา 20 Shorts รวมกว่า 32,000 frames ที่ 30 FPS | วัดทุก frame ด้วยโค้ดและทำชุดภาพสำหรับตรวจ ไม่ใช่ถาม AI ว่า "สไตล์อะไร" |
| 1:38–2:32 | วิเคราะห์ script formula: paradox hook → escalation → pivot → payoff | เก็บสูตรการเล่าเรื่อง แต่เขียนบทใหม่และตรวจข้อเท็จจริง |
| 2:32–3:10 | 2D characters รับแสง/สร้างเงาใน 3D; painted world, ink lines, warm-cool lighting, camera movements | ตรวจทั้ง shading ของตัวละครและ world geometry ไม่ใช่ดูแค่พาเลตสี |
| 3:10–3:42 | สร้างเครื่องมือวัด: contact sheet ทุก 2 วินาที / 60 เฟรม, phase correlation, cut detection, brightness/contrast/saturation | เหตุผลที่มี scripts/analyze_references.py และ upstream reports |
| 4:13–4:54 | เลือกเรื่อง Broughton Bridge ปี 1831, ตรวจปี/จำนวนทหาร/ความลึกน้ำก่อนเขียนบท | ห้ามสร้างมุก factual โดยเดา |
| 4:54–5:43 | ทดลอง Blender ก่อน แล้วเปลี่ยนเป็น Three.js + Remotion | ต้นฉบับใช้โค้ดสร้างภาพจริง ไม่ได้พึ่ง AI video generation |
| 5:43–6:16 | ใช้โมเดล 3D ฟรี 37 ชิ้น, วาด texture ด้วยโค้ด, หน้า 14 expression, ฉากสะพานและการเดินของทหาร | โมเดล + detailed texture + actor state สำคัญพอ ๆ กับ Renderer |
| 6:16–6:26 | เขียน custom 3D world ink effect | ดู templates/bridge/ink.ts + compositing ใน Bridge.tsx |
| 6:26–7:35 | Render stills พบกล้องทะลุตึก, วัสดุต้นไม้ผิดสี, โซ่บังหน้า; compare side-by-side แล้วเห็นว่างานยังจืด | ห้ามรับงานว่าเสร็จแค่เพราะทุก shot รันได้ |
| 7:37–8:26 | ใช้ 12 agents: 7 วิเคราะห์ช่องว่างงานภาพ, 1 เสียง, 4 agent แก้ภาพ แยก file ownership/sandboxes | สร้าง reports ที่อิง frame IDs และห้าม agent แก้ไฟล์เดียวกัน |
| 8:37–9:39 | แก้ปัญหาจากการวัด: ink ถูก blur pass ทับ, camera snap, shadows ผิดสี, proportions ผิด | ต้องระบุ cause ที่ตรวจจาก source จริง ไม่ใช่สั่ง "เพิ่มคุณภาพ" |
| 9:14–9:39 | ผลวิเคราะห์เดิมบางเรื่องผิด: ลักษณะหัว และกล้องดูนิ่งเพราะ tracker จับ micro-motion ไม่ได้; พบ slow pushes มากกว่าเดิม | อย่าตั้งค่ารูปทรงและกล้องจากรายงานเก่าเพียงอย่างเดียว |
| 9:39–10:22 | รวบรวม source/rules/fixes เป็น Claude Skill บน GitHub | นี่คือผลลัพธ์ที่เราจะทำ: Skill ที่มี template code + reports + tools ไม่ใช่เขียน Framework ใหม่ |

## สิ่งที่ถอดเป็นบทเรียนทางเทคนิค

### A. อย่าย้ายแต่ไฟล์ .ts — ต้องย้ายวิธีตรวจงานด้วย
ผู้สร้างแก้งานให้ดีขึ้นด้วยการระบุสาเหตุเฉพาะ: post-effect order, detail gaps ใน texture, character shape, camera easing, depth-of-field และ scene lighting.

### B. 3D world ไม่ใช่แค่ BoxGeometry
เขามี source mesh builders, 37 โมเดล 3D ฟรี และ code-painted textures. ถ้าทำ Empty City ต้องออกแบบอาคารจริงและวัตถุที่เล่าเรื่อง ไม่ใช่แค่เปลี่ยนวัสดุของกล่องสี่เหลี่ยม

### C. แกะ workflow ไม่ใช่ copy character/style แบบลอกช็อต
วิเคราะห์ measurable patterns แล้วสร้างเรื่องและตัวละครใหม่ของเราเอง; original reference frames ที่ไม่ใช่ของเราใช้ศึกษาในเครื่องเท่านั้น

### D. Source integration matters
Original README เป็น bundle ของ Skill; ไม่มี Remotion project สำเร็จรูปทั้งหมดไว้ใน Repository ต้องใช้ project รันในเครื่องพร้อม dependencies, asset kit และ renderer.

## ขั้นตรวจรับงานจริง
1. Claude Code อ่าน SKILL.md และ source ต้นฉบับได้จาก path ที่ถูกต้อง
2. วิเคราะห์คลิปอ้างอิงที่อยู่บนเครื่องได้ พร้อม metrics CSV + 2s contact sheets
3. Render Bridge baseline ใน Remotion project ที่ตั้งค่าแล้วได้
4. สร้างฉากใหม่ที่ไม่ใช่สะพานด้วย scene-specific .ts + models/textures
5. Render stills แล้วเทียบภาพ / แก้ defects จนผ่าน และจึง Render full

อย่าสับสน **มี Skill ใน GitHub** กับ **ผ่านการทดสอบผลิตวิดีโอจริง** เพราะต้องมี environment และเรนเดอร์หลักฐานก่อน
