# Claude Code Prompt — New topic without losing look

~~~text
You are producing an ORIGINAL vertical animated short with our shared studio engine.

TOPIC: <enter topic>
LANGUAGE: <Thai/English>
DURATION: <target sec>
CHARACTER IDS: <approved original characters>
APPROVED REFERENCE PATHS: <our legal baseline stills>
WORKING REMOTION PROJECT PATH: <actual project path>

First read README.md, STYLE_BIBLE.md, CHARACTER_BIBLE_TEMPLATE.md, ENGINE_RULES.md, CLAUDE_WORKFLOW.md and QA_CHECKLIST.md. Discover the actual project rather than assuming it exists in this docs repo.

1. Research and validate story facts (create FACTS.md with citations); create original SCRIPT.md using hook/escalation/pivot/payoff.
2. Produce voice.wav and timing JSON with checked Thai phrase/word boundaries if Thai; audio-first.
3. Produce shot specs: narrative purpose, camera, assets, foreground/midground/background, lighting preset and hero material details.
4. List reusable assets/classes and proposed new episode-specific .ts/.tsx/.glb files. If advanced geometry/rig needed, make it explicitly; never silently substitute low-detail boxes.
5. Create 8+ storyboard stills then a 4s moving style proof. Compare against approved baseline. Stop and fix P0/P1 defects.
6. After human acceptance, implement complete story/camera/animation, sync events and SFX. Preserve shared renderer/post pipeline and tested character identity.
7. Typecheck, render, run frame + audio QA, provide full source paths and QA log. If a required asset or effect is unavailable, report it rather than declaring success.

Do not copy third-party distinctive scripts/characters/shots. Don't touch the original Bridge folder. Do not promise final quality before reviewing renders.
~~~