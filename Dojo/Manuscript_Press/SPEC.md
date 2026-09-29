# STEP.md — MANUSCRIPT_PRESS / RECONSTRUCT CLEAN ROOT

```yaml
IDENTITY:
  Project: MANUSCRIPT_PRESS
  Phase: RECONSTRUCT_AFTER_DISK_LOSS
  Step: MATERIALIZE_CLEAN_ROOT
  Version: 1.0
  Status: READY_FOR_SAMURAI
  Date: 2026-09-29
  Step Type: RECONSTRUCTION

  Technical Authority:
    - SPEC v3.3 PILOT_EXECUTION_PROFILE — current execution authority
    - SPEC v3.2.2 — target architecture (NOT implemented; archived)
    - IMPLEMENTATION_MAP_APPROVED.yaml — component classification
    - IMPLEMENTATION_PLAN.md — sequence
    - DEEPSEEK_STEP_HANDOFF.md — Grok route
    - TECHNICAL_AUDIT.md — READ-ONLY audit facts

  Scope Claim: RECONSTRUCT ONLY — not production inference, not hardening, not v3.2.2 freeze/commit.
```

---

## OBJECTIVE

Материализовать чистый рабочий ROOT на `E:\Gemini\Dojo\Manuscript_Press` из GitHub snapshot:

- канонический pilot engine (`src/production_runner.py`, `src/loader.py`, `src/parser/*`)
- production inputs (`Input/SOURCE_MANUSCRIPT.md`, `Input/PROMPT_MAP.yaml`, `Gemma.md`)
- корректный `config/writer_config.yaml` с реальным путём к `.gguf` на новом диске
- чистый `run_manuscript_press.bat` без D:-путей, без `paired_runner`, без start-marker default
- `SPEC.md` = v3.3, `SPEC_v3.2.2.md` = архив target
- legacy/bench/control-файлы — архивированы, не активны

**Verification — только `--preflight-only`.** Inference запрещён.

---

## CANONICAL INPUTS

```yaml
inputs:
  source: Input/SOURCE_MANUSCRIPT.md
  prompt_map: Input/PROMPT_MAP.yaml
  gemma_kernel: Gemma.md
  writer_config: config/writer_config.yaml
```

---

## PHASE 0 — SHOGUN FACTS (CLOSED)

```yaml
phase_0_shogun_facts:
  status: CLOSED_BY_SHOGUN
  target_root: E:\Gemini\Dojo\Manuscript_Press
  real_gguf_path: E:\Gemini\models\Gemma-The-Writer-9B-D_AU-q5_k_m.gguf   # DEFAULT
  alternative_gguf: E:\Gemini\Dojo\Manuscript_Press\Gemma-The-Writer-N-Restless-Quill-V2-10B-D_AU-q5_k_m.gguf   # NOT USED in this STEP
  historical_output:
    note: Output/runs/20260923T144611Z и первый FINAL — вне GitHub snapshot
    action: if a copy exists off-repo → Archive/, NOT default
```

Блокер «нет пути .gguf» — снят.

---

## ALLOWED WORKING FILES

### Создать / установить

```yaml
- E:\Gemini\Dojo\Manuscript_Press\                    # ROOT
- SPEC.md                                             # v3.3
- SPEC_v3.2.2.md                                      # переименованная копия текущего SPEC.md
- IMPLEMENTATION_MAP_APPROVED.yaml
- IMPLEMENTATION_PLAN.md
- README.md                                           # replacement из пакета
- Archive\                                            # для архивных файлов
```

### Изменить

```yaml
config/writer_config.yaml:
  model.path: E:\Gemini\models\Gemma-The-Writer-9B-D_AU-q5_k_m.gguf

run_manuscript_press.bat:
  content: |
    @echo off
    cd /d "%~dp0"
    set PYTHONPATH=%CD%
    python -m src.production_runner %*
```

### Архивировать (переместить в `Archive/`, не удалять)

```yaml
- manuscript_press.bat                 → Archive/historical_launchers/
- Output/Old/                          → Archive/Output_Old/
- src/builder.py                       → Archive/legacy_src/
- src/generator.py                     → Archive/legacy_src/
- src/smoke_bridge.py                  → Archive/benches/
- src/continuity_cache_bench.py        → Archive/benches/
- src/test_inference.py                → Archive/benches/
- src/parser.py                        → Archive/legacy_src/   # root duplicate
- src/prompt_map_parser.py             → Archive/legacy_src/   # root duplicate
- src/protected_span_parser.py         → Archive/legacy_src/   # root duplicate
- src/atx_heading_extractor.py         → Archive/legacy_src/   # root duplicate
- src/authority_freeze.py              → Archive/target_unused/
- src/core/authority_freeze.py         → Archive/target_unused/
- src/revision_validator.py            → Archive/target_unused/
```

### Оставить inactive (не запускать, не изменять)

```yaml
- STEP.md            # старый Samurai STEP — replacement отдельно
- Current_Prompt.md  # старый Samurai frame
- GEMINI.md          # старый D:\Dojo frame
```

### DO NOT TOUCH

```yaml
- src/production_runner.py
- src/loader.py                # уже грузит Llama с n_gpu_layers=-1, chat_format="gemma"
- src/parser/__init__.py
- src/parser/protected_span_parser.py
- src/parser/source_parser.py
- src/parser/prompt_map_parser.py
- src/parser/source_prompt_map_validator.py
- Input/SOURCE_MANUSCRIPT.md
- Input/PROMPT_MAP.yaml
- Gemma.md                     # литературный текст
- templates/                   # non-runtime

- AI-Colab gguf loader         # https://huggingface.co/datasets/lhc-lab/AI-Colab — OUT OF SCOPE
- app.py из AI-Colab           # не искать, не портировать, не сравнивать
- GPU-тюнинг (n_gpu_layers, VRAM, CUDA)   # после GREEN на preflight, отдельным решением
```

---

## EXECUTION SEQUENCE

### Phase 1 — Clone snapshot, no bat run

1. Скопировать GitHub `Dojo/Manuscript_Press` → `E:\Gemini\Dojo\Manuscript_Press`.
2. **Не запускать bat.**

### Phase 2 — Path + launcher hygiene

1. `config/writer_config.yaml`: `model.path = E:\Gemini\models\Gemma-The-Writer-9B-D_AU-q5_k_m.gguf`.
2. `run_manuscript_press.bat` — заменить на clean launcher (см. ALLOWED WORKING FILES).
3. `manuscript_press.bat` → `Archive/historical_launchers/`.
4. Grep-check: ноль `D:\Gemini\dojo`, ноль `paired_runner`, ноль `--start-marker MP:0170` в default invocation.

### Phase 3 — Document set

1. Текущий repo `SPEC.md` → переименовать в `SPEC_v3.2.2.md`.
2. Установить `SPEC.md` = v3.3.
3. Установить `IMPLEMENTATION_MAP_APPROVED.yaml`.
4. Установить `IMPLEMENTATION_PLAN.md`.
5. Заменить `README.md` на новый.
6. `STEP.md` / `Current_Prompt.md` / `GEMINI.md` — оставить физически, не активировать.

### Phase 4 — Tree classification

1. Canonical engine — остаётся на месте.
2. Legacy/bench/target_unused — переместить в `Archive/`.
3. `Output/Old/` → `Archive/Output_Old/`.
4. Создать `Output/runs/` (пусто).

### Phase 5 — Reconstruct verify (NO Gemma)

```text
python -m py_compile src/production_runner.py
python -m src.production_runner --preflight-only
```

**Ожидаемо:**
- `py_compile`: exit 0
- preflight: `validator PASS`, `marker_count = 375`, **0** `load_model`, **0** `create_chat_completion`

### Phase 6 — Report

```yaml
RECONSTRUCT_REPORT:
  ROOT: E:\Gemini\Dojo\Manuscript_Press
  files_installed: [<list>]
  files_archived: [<list>]
  writer_config_model_path: E:\Gemini\models\Gemma-The-Writer-9B-D_AU-q5_k_m.gguf
  alternative_gguf_present_not_activated: yes
  src_loader_py_unchanged: yes
  ai_colab_loader: not ported
  launcher_clean: yes/no
  grep_D_paths: empty / <list>
  grep_paired_runner: empty / <list>
  grep_start_marker_default: empty / <list>
  py_compile: PASS / FAIL
  preflight_only:
    executed: yes/no
    exit_code: <int>
    validator: PASS / FAIL
    marker_count: <N>
    load_model_called: false
    completion_called: false
  inference_executed: false
  next: WAIT_FOR_GROK_OR_SHOGUN
```

---

## STOP CONDITIONS

```yaml
STOP_CONDITIONS:
  before_phase_1:
    - целевой ROOT пуст ИЛИ Shogun явно разрешил overwrite
  after_phase_1:
    - ROOT обязан содержать snapshot — это НЕ blocker
  hard_stops:
    - любой preflight FAIL
    - любой случайный inference / load_model
    - попытка использовать alternative_gguf
    - попытка портировать AI-Colab loader / app.py
    - попытка изменить src/loader.py
  action_on_stop: honest report, no partial ROOT, WAIT_FOR_SENSEI
```

---

## NON-GOALS

```yaml
non_goals:
  - ❌ production inference
  - ❌ full run (`python -m src.production_runner` без `--preflight-only`)
  - ❌ hardening (prefix, heading newline, delimiter strip) — separate STEP
  - ❌ v3.2.2 freeze/commit implementation
  - ❌ resume MP:0170 as default
  - ❌ rewrite Samurai Current_Prompt.md / GEMINI.md / philosophy
  - ❌ edit Input/SOURCE_MANUSCRIPT.md, Input/PROMPT_MAP.yaml, Gemma.md content
  - ❌ Git operations beyond snapshot copy
  - ❌ не переносить alternative_gguf в writer_config.model.path
  - ❌ не делать alternative_gguf частью GitHub snapshot
  - ❌ не запускать alternative_gguf в reconstruct
  - ❌ не искать / не портировать / не сравнивать AI-Colab loader или app.py
  - ❌ не менять src/loader.py
  - ❌ не выполнять GPU-тюнинг в этом STEP
```

---

## ACCEPTANCE

```yaml
acceptance:
  ROOT: E:\Gemini\Dojo\Manuscript_Press exists
  writer_config.model.path: E:\Gemini\models\Gemma-The-Writer-9B-D_AU-q5_k_m.gguf exists on this machine
  alternative_gguf: present, NOT activated
  src/loader.py: unchanged
  AI-Colab loader: not ported
  launcher: clean (no D:, no paired_runner, no --start-marker default)
  preflight_only: PASS, marker_count=375, validator PASS
  inference: 0
  historical_resume_bat: archived, not default
  SPEC.md: v3.3 present
  SPEC_v3.2.2.md: archived target present
```

---

## END PROTOCOL

```text
MATERIALIZE → PY_COMPILE → PREFLIGHT → REPORT → STOP → WAIT_FOR_GROK_OR_SHOGUN
```

**Hardening STEP — отдельный и последующий. Full run — только после separate Shogun GREEN.**

---

```yaml
BRIGADIER_STATUS:
  step: MATERIALIZE_CLEAN_ROOT
  status: READY_FOR_SAMURAI
  inserts_applied: 1–4 (all Grok binding inserts integrated)
  default_model: E:\Gemini\models\Gemma-The-Writer-9B-D_AU-q5_k_m.gguf
  alternative_model: recorded, NOT activated
  ai_colab_loader: OUT_OF_SCOPE
  src_loader_py: DO_NOT_TOUCH
  inference: FORBIDDEN
  full_run: RED
  next: SHOGUN_DELIVERS_TO_SAMURAI
  stop: true
```
STOP.