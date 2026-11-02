# Claude Code Prompt — Inspect why a new episode looks worse

~~~text
ROLE: visual regression auditor. Be evidence-driven.

Compare the approved best-quality Bridge/railway/sailor reference (legal use only) with the NEW episode, using source files and representative stills. Inspect actual import chains and shader pipeline; do not infer file changes from appearance alone.

1) Confirm which files implement ink, lens blur, grading, tone mapping, world geometry, painted textures, lighting, cardshade, NOINK, camera and contacts in BOTH projects. Report missing/bypassed code paths.
2) Render matching shot categories (wide, medium, close) and annotate 8+ pairs with frames/times.
3) Explain deficits in geometry detail, materials, silhouette, depth layers, lighting direction, contrast, outlines, focal plane, motion and framing.
4) For every deficit, give proof, suspected root cause (distinguish confirmed vs hypothesis), exact file/function, minimal fix, regression risk and test frame.
5) NEVER say 'looks cheap' without describing observable differences.
6) Delegate by file ownership (world, materials, characters, camera, post). No concurrent edits to same file.
7) Produce QA_REPORT.md and prioritize P0/P1/P2. Request human approval at style gate.

Do not rewrite the bridge visual pipeline or fabricate measurements. If source isn't available, state what cannot be confirmed.
~~~