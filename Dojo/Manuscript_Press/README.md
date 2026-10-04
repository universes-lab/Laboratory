cd E:\Gemini\Dojo\Manuscript_Press
.venv\Scripts\python.exe -m src.production_runner --start-marker MP:0199 --prior-run-dir Output\runs\<новый_каталог>

# Manuscript Press

Local pilot engine that sends a marked-up SOURCE manuscript through Gemma-The-Writer one production block at a time and assembles `Output/FINAL.manuscript.md`.

It does not invent research conclusions as a design goal. First live article run proved the pipeline works and also showed assembly/control-leak defects. Those are tracked as hardening, not as a new product.

Current engine: Gemma-The-Writer-9B via `llama-cpp-python`.
Current execution authority: SPEC v3.3 PILOT_EXECUTION_PROFILE.
Target architecture (not implemented): SPEC v3.2.2 freeze/commit machine.

## ROOT

```text
E:\Gemini\Dojo\Manuscript_Press
```

## What you run

```bat
cd /d E:\Gemini\Dojo\Manuscript_Press
set PYTHONPATH=%CD%
python -m src.production_runner --preflight-only
python -m src.production_runner
```

Or `run_manuscript_press.bat` after it is rewritten for this ROOT.

Do not use `manuscript_press.bat` from the GitHub snapshot. That file is a historical resume of run `20260923T144611Z`.

## Inputs

| File | Role |
|------|------|
| `Input/SOURCE_MANUSCRIPT.md` | Whole manuscript + `<!-- MP:XXXX -->` + protected spans |
| `Input/PROMPT_MAP.yaml` | Per-marker LONG_RANGE_FRAME + LOCAL_TRANSFORMATION |
| `Gemma.md` | System kernel for Gemma |
| `config/writer_config.yaml` | Model path, n_ctx, max_tokens, temperature, top_p |

## Outputs

| File | Role |
|------|------|
| `Output/FINAL.manuscript.md` | Pilot assembled manuscript |
| `Output/runs/<id>/` | Per-marker payload / raw / restored / rebuilt |

## What this project is not

- Not the old CONCEPT_PACKAGE / `generator.py` writer
- Not paired half-chapter resident sessions
- Not a full SPEC v3.2.2 commit ledger
- Not publication-ready by default
- Not Samurai’s Current_Prompt (Gemma.md ≠ Current_Prompt.md)

## Book-architecture notes

Editorial ideas about nested multigenre / trilingual books live in `templates/` and older README drafts. They are product intent for later books. They are not the runtime contract of `production_runner.py`.
