# Bridge Render Diagnostic — สิ่งที่ทดสอบยืนยันแล้ว (2026-11-02)

**แหล่งหลักฐาน:** รายงาน `BRIDGE_DIAGNOSTIC_REPORT.md`, ภาพเปรียบเทียบ และ `diagnostic-source.diff` ที่ผู้ใช้ส่งจาก Codex ทำงานบน Windows Remotion project ของผู้ใช้  
**สถานะ:** วาด Bridge scene ได้จริงที่ frame 60 และ 1350; *ยังไม่ผ่าน* fidelity ของ assets และ full-video continuity

## ข้อเท็จจริงที่พิสูจน์แล้ว

- Upstream 13 `.ts/.tsx` files คงเดิมใน baseline; การแก้ทำใน `bridge-debug/Bridge.tsx` ซึ่งเป็นสำเนาแยกต่างหาก
- Remotion 4.0.539, Fiber 9.8.2, React Three Postprocessing 3.2.2, Postprocessing 6.38.3 และ Three 0.181.1 ใช้ร่วมกันในเครื่องที่ทดสอบ
- Test A: green cube ที่ไม่มี post-processing มองเห็นได้
- Test B: Bridge scene **ไม่ใช้ post-processing** มองเห็น Geometry/characters ได้ แม้ GLB หาย
- Test C: Bridge + post **ก่อนแก้** ภาพฟ้าล้วน; การจับภาพเกิดตอน `renderReady=true` แต่ **WebGL draws=0**
- Test C: ใช้ readiness hold + `requestAnimationFrame` + Fiber `advance` ก่อน `continueRender` แล้วแสดงภาพได้; frame 60 มี 609 WebGL draws/129,794 unique colors; frame 1350 มี 404 draws
- Re-render frame 60 ผล pixels ตรงกัน (ในสภาพแวดล้อมทดลอง); ไม่ได้แก้ shader, camera, world logic หรือ post order
- **สาเหตุจริง:** React Three post composer ยังเริ่มไม่เสร็จตอน Remotion ปลด render hold และ screenshot; `frameloop=never` จึงไม่มี draw ถัดมาเอง
- **แยกปัญหา:** การขาด 26 GLB ไม่ได้ทำให้ภาพฟ้าล้วน เพราะ Test B/C ที่แก้ readiness แล้ว render procedure geometry ได้

## ข้อควรระวัง: อย่าคัดลอก Diff ทั้งก้อนเข้าผลิตจริง

Diff ทดสอบเพิ่ม `SceneProbe`, `__diagEvent` logging, `diagnostic.noPost`, `diagnostic.settle` และ `useLayoutEffect` เพื่อแยกสาเหตุ โดย **instrumentation ทั้งหมดเป็น diagnostic-only**. ถ้าต้อง port ให้ดึงเฉพาะ readiness behavior ที่ทำให้ภาพปรากฏ แล้วลบ probe/diagnostic globals; ให้ Codex ตรวจ `delayRender` /`continueRender` lifecycle ของ hold และทดสอบ frame 60, 1350 อีกครั้ง รวมทั้ง frame boundary/crossfade. ห้ามแก้ renderer ต้นฉบับใน Skill โดยไม่มี regression proof.

ผู้ใช้ส่ง source diff ระบุ patch บน `Inner`: ใช้ `useThree().advance` และ `useLayoutEffect` สร้าง `delayRender("bridge post-processing commit")`; RAF เรียก `advance(performance.now())` ก่อน `continueRender(handle)`. นี่เป็น **วิธีแก้ที่ทดสอบผ่านใน environment ที่ระบุ** ไม่ใช่ข้อรับรองว่าวิธีเดียวเหมาะสำหรับ Remotion ทุกเวอร์ชัน

## โมเดล 26 ชิ้นที่ยังขาด

Required by KENNEY array in upstream `templates/bridge/world.ts`. Must be findable inside the local Remotion app's `public/bridge/kenney/` with **these exact filenames**:

```text
tree_oak.glb
tree_default.glb
tree_detailed.glb
tree_fat.glb
tree_cone.glb
tree-high-round.glb
tree.glb
plant_bushLarge.glb
plant_bushDetailed.glb
plant_bush.glb
hedge.glb
flower_redA.glb
flower_yellowA.glb
flower_purpleA.glb
grass_large.glb
grass.glb
lily_large.glb
lantern.glb
cart.glb
stall-red.glb
stall-green.glb
stall-bench.glb
banner-red.glb
banner-green.glb
windmill.glb
canoe.glb
```

## ดึง asset อย่างไรโดยไม่เดา

1. Download official [Kenney Nature Kit](https://kenney.nl/assets/nature-kit) (330 3D files, CC0) and inspect files.
2. Download official [Kenney Fantasy Town Kit](https://kenney.nl/assets/fantasy-town-kit) (160 3D files, CC0). Note that current v2.0 is *completely remade*, may differ from upstream.
3. Recursively inventory extracted formats (GLB/glTF, OBJ/FBX); compare basenames to 26 required names. Match exact meshes and file compatibility, not name only. If source pack uses other names, document alias and evidence before conversion/renaming.
4. Copy only verified matching models and dependencies to `public/bridge/kenney/`. Verify expected 26 model URLs load with HTTP 200 and correct GLB parsing. Do not treat a 200 HTML fallback as valid GLB; inspect response type/content.
5. Keep source URL, release/version, file hash and CC0 license record in `asset-manifest.json` outside third-party restricted data. Reference images are not included in this Skill.
6. For models not present in the current kits, locate original version or clearly report replacements and aesthetic differences; do not silently fill in with boxes.

## Next pass criteria

- Render frame 60 and 1350 with post, no debug globals; visual verification and pixel variance.
- Render additional sample frames across 15 shots, including transition/crossfade frames (time-dependent and double-canvas composition).
- Validate model URLs; restore as many original 26 names as possible, reporting exact mismatches.
- Render a short playable Bridge baseline, inspect audio (if added) and temporal continuity, check for black/frozen frames and asset failures.
- Only then begin a **new-topic** scene (e.g. Empty City) using the approved `references/OUR_STYLE_BIBLE.md` and original source techniques.

## Reference vs repo guarantee

The above numbers come from a **user-supplied Codex test report**, not from a test this GitHub repo executed itself. This repository contains source/study/Skill files, not an independently verified runnable Remotion project. Keep that distinction clear.
