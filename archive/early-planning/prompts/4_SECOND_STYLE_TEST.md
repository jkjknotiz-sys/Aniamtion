# Claude Code Prompt — 4-Second Style Lock

Paste the following into Claude Code after adding approved reference stills and locating the actual Remotion project.

~~~text
ROLE: senior technical art director + Three.js/Remotion engineer.

GOAL: make a 4-second, 9:16, 30fps moving style proof for a NEW topic, maintaining the APPROVED LOOK (not cloning the reference story).

Read STYLE_BIBLE.md, ENGINE_RULES.md, CHARACTER_BIBLE_TEMPLATE.md, QA_CHECKLIST.md, and actual project package scripts and components. Locate the Bridge baseline and user-approved reference images (3–5). Verify paths; never invent assets. Make a fresh episode directory/branch. Preserve the original Bridge implementation and record its render settings.

Inspect real code; make a table of reused post-processing/character/material modules vs new scene-specific TS files. DO NOT implement a fresh renderer or replace shaders with simple alternatives for convenience. If an API is incompatible, stop and propose minimal adaptations with before/after comparison.

Implement one visually rich, narrative-relevant shot with approved original character design. World must be detailed at camera distance: distinct facades, painted material variation, visible edges, intentional foreground/midground/background, believable light/shadow, readable silhouette. Avoid generic final BoxGeometry facades. Test character shading, NOINK and contact shadow.

Render at least 8 diagnostic stills and exactly 120 frames (4 seconds at 30fps) if configuration supports it. Build a contact sheet and side-by-side comparisons with our approved stills. Record failures with frame numbers and proposed file-owner changes. Revise only the relevant module, and retest. Do not render a 60-second episode yet.

Deliver: test.mp4, stills, comparison sheet, QA_REPORT.md (PASS/FAIL with evidence), changed-files summary, warnings, reproduction commands. Do not claim equivalence without human acceptance.
~~~