# IMPLEMENTATION_PLAN.md
# Reconstruct clean MANUSCRIPT_PRESS on E:\Gemini\Dojo\Manuscript_Press

Authority: SPEC v3.3 (execution) + SPEC v3.2.2 (target, not built now)
No production inference in this plan.

## Goal

Create a clean live ROOT that can later run:

```text
python -m src.production_runner --preflight-only
python -m src.production_runner
```

from E:\ without D: paths, without historical resume, without activating old Samurai STEP.

## Sequence

### Phase 0 — Shogun physical facts
1. Confirm E:\Gemini\Dojo\Manuscript_Press is empty/new.
2. Confirm actual path of `Gemma-The-Writer-9B-*.gguf` on the new disk.
3. If a copy of `Output/runs/20260923T144611Z` or `FINAL.manuscript.md` exists off-repo, park it under `Archive/` — do not make it default.

### Phase 1 — Clone snapshot, then reshape
1. Copy GitHub `Dojo/Manuscript_Press` → `E:\Gemini\Dojo\Manuscript_Press`.
2. Do not run any bat yet.

### Phase 2 — Path and launcher hygiene
1. Edit `config/writer_config.yaml` `model.path` to the real gguf path.
2. Replace `run_manuscript_press.bat`:

```bat
@echo off
cd /d "%~dp0"
set PYTHONPATH=%CD%
python -m src.production_runner %*
```

3. Move `manuscript_press.bat` to `Archive/historical_launchers/` or delete.
4. Do not leave `PYTHONPATH=D:\Gemini\dojo` anywhere.

### Phase 3 — Document set
1. Keep repo `SPEC.md` renamed to `SPEC_v3.2.2.md` (target).
2. Install new `SPEC.md` = v3.3 from this audit package.
3. Install `IMPLEMENTATION_MAP_APPROVED.yaml`.
4. Replace `README.md`.
5. Leave `STEP.md` / `Current_Prompt.md` / `GEMINI.md` in place but **inactive** until Doctor/Sensei rewrite. Do not execute them.

### Phase 4 — Tree classification
1. Keep `src/production_runner.py`, `src/loader.py`, `src/parser/`.
2. Move to `Archive/legacy_src/` (or leave unused, do not import):
   builder, generator, smoke_bridge, continuity_cache_bench, test_inference,
   root parser duplicates, authority_freeze, revision_validator.
3. Move `Output/Old/` → `Archive/Output_Old/`.
4. Ensure `Output/runs/` exists and is empty (or only new runs).

### Phase 5 — Hardening (separate STEP, after reconstruct verify)
Only after preflight PASS on E:\:
- prefix preservation
- heading newline
- delimiter guard
Not in Phase 1–4.

### Phase 6 — Verify reconstruct (no Gemma)
```text
python -m src.production_runner --preflight-only
```
Expect: 375 markers, validator PASS, 0 load_model.
STOP.

### Phase 7 — Full run
Only Shogun GREEN. Not part of reconstruct.

## Blockers
- Unknown new model path
- Missing first-run FINAL in GitHub (editorial copy is offline)
- Old Samurai docs still pointing at D:\

## Done when
- ROOT exists on E:\
- writer_config path is valid
- clean bat works
- preflight-only PASS
- historical resume bat is not default
- no inference has been run as part of restore
