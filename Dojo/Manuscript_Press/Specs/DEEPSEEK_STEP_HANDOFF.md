# DEEPSEEK_STEP_HANDOFF
# Reconstruct clean MANUSCRIPT_PRESS on E:\Gemini\Dojo\Manuscript_Press

From: Grok (Technical Lead)
To: DeepSeek (Coding Sensei)
Then: Sensei writes STEP.md for Samurai
Do not write Current_Prompt.md here.

## Objective
Materialize a clean project tree at E:\Gemini\Dojo\Manuscript_Press from the GitHub snapshot, with correct paths and launchers, verified by --preflight-only only.

## Approved route
SPEC v3.3 PILOT. Do not implement v3.2.2 freeze/commit. Do not run Gemma. Do not resume MP:0170.

## Files

CREATE/INSTALL from audit package:
- SPEC.md (v3.3)
- SPEC_v3.2.2.md ← rename current repo SPEC.md
- IMPLEMENTATION_MAP_APPROVED.yaml
- IMPLEMENTATION_PLAN.md
- README.md (replacement)

CHANGE:
- config/writer_config.yaml → model.path = real gguf on new disk (Shogun supplies path)
- run_manuscript_press.bat → cd to script dir, PYTHONPATH=%CD%, `python -m src.production_runner %*`
  No pause. No start-marker. No D:\ paths.

REMOVE FROM DEFAULT USE (archive):
- manuscript_press.bat
- Output/Old/

DO NOT IMPORT / DO NOT ACTIVATE:
- src/builder.py, src/generator.py, benches, root parser duplicates
- STEP.md / Current_Prompt.md / GEMINI.md as live Samurai frame (Doctor later)

KEEP AS ENGINE:
- src/production_runner.py
- src/loader.py
- src/parser/*
- Input/SOURCE_MANUSCRIPT.md
- Input/PROMPT_MAP.yaml
- Gemma.md

## Required verification
1. Files exist at E:\Gemini\Dojo\Manuscript_Press as mapped.
2. grep launchers: no D:\Gemini\dojo, no paired_runner, no MP:0170 default.
3. `python -m py_compile src/production_runner.py`
4. `python -m src.production_runner --preflight-only`
   Expect validator PASS, marker_count matches SOURCE (was 375 on last known inputs), no load_model.
5. Report physical paths + preflight excerpt.

## Forbidden
- create_chat_completion / load_model except as imported unused during preflight
- full production run
- editing SOURCE or PROMPT_MAP content
- editing Gemma.md literary text
- implementing hardening (prefix/glue/strip) in this STEP
- rewriting Samurai Current_Prompt / philosophy

## Acceptance
```yaml
ROOT: E:\Gemini\Dojo\Manuscript_Press
writer_config.model.path: exists on this machine
launcher: clean
preflight_only: PASS
inference: 0
historical_resume_bat: not default
```

## STOP
After preflight report. WAIT_FOR_GROK / SHOGUN.
Hardening STEP is next and separate.
Full run only on later Shogun GREEN.
