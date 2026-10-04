# STEP.md — MANUSCRIPT_PRESS / MAX_TOKENS DOWNSHIFT + REPETITION GUARD

```yaml
IDENTITY:
  Project: MANUSCRIPT_PRESS
  Phase: POST_RECONSTRUCT
  Step: REPETITION_GUARD_AND_MAX_TOKENS
  Version: 1.0
  Status: READY_FOR_SAMURAI
  Date: 2026-10-03
  Step Type: EDIT

  Technical Authority:
    - SPEC v3.3 (current execution contract)
    - Shogun route decision 2026-10-03

  Scope: writer_config max_tokens downshift + repetition guard in runner.
  Not production run.
```

---

## OBJECTIVE

1. В `config/writer_config.yaml` изменить только `generation.max_tokens: 2048` → `768`.
2. В `src/production_runner.py` добавить проверку повторов: если одна и та же последовательность из 8+ символов занимает больше половины текста — не писать PASS.
3. При срабатывании проверки — один повтор того же маркера с `max_tokens=384`. Если повтор снова даёт такой же результат — STOP, cache не обновлять, FINAL не писать.

---

## ALLOWED WORKING FILES

**Изменить:**

```
E:\Gemini\dojo\Manuscript_Press\config\writer_config.yaml
E:\Gemini\dojo\Manuscript_Press\src\production_runner.py
```

**Не трогать:**

```
config\writer_config_9b.yaml
config\writer_restless_quill.yaml
SPEC.md
SPEC_v3.2.2.md
Input\SOURCE_MANUSCRIPT.md
Input\PROMPT_MAP.yaml
Gemma.md
src\loader.py
src\parser\*
manuscript_press.bat
resume_manuscript_press.bat
Output\runs\20261003T144957Z\   (не удалять, не менять)
```

---

## DO_NOT

- Не менять `model.path`, `model.n_ctx`, `generation.temperature`, `generation.top_p` в `writer_config.yaml`.
- Не менять `writer_config_9b.yaml` и `writer_restless_quill.yaml`.
- Не подменять файлы в `Output\runs\20261003T144957Z\`.
- Не удалять `Output\runs\20261003T144957Z\`.
- Не менять SOURCE, PROMPT_MAP, Gemma.md, loader.py, парсеры.
- Не запускать модель.

---

## EDIT 1 — `config/writer_config.yaml`

Изменить только:

```yaml
generation:
  max_tokens: 768
```

`path`, `n_ctx`, `temperature`, `top_p` — не менять.

---

## EDIT 2 — `src/production_runner.py` — repetition guard

### a) Добавить функцию детекции повторов (рядом с другими helper-функциями):

```python
def detect_dominant_repetition(text: str, min_seq_len: int = 8, threshold: float = 0.5) -> Optional[str]:
    """
    Return the repeated substring if a single sequence of length >= min_seq_len
    occupies more than `threshold` of the whole text. Otherwise return None.
    """
    if not text:
        return None
    n = len(text)
    if n < min_seq_len * 2:
        return None
    # Try every start position and length >= min_seq_len, find maximal repeated runs.
    # We keep it cheap: check the most common substring via simple suffix windowing.
    best_seq: Optional[str] = None
    best_cover = 0
    # Candidate seeds: every position of the first half
    for i in range(0, n - min_seq_len, min_seq_len):
        seq = text[i:i + min_seq_len]
        # skip obviously weak seeds
        if len(seq) < min_seq_len:
            continue
        # count occurrences
        count = text.count(seq)
        cover = count * len(seq)
        if cover > best_cover:
            best_cover = cover
            best_seq = seq
    if best_seq is None:
        return None
    if best_cover / n > threshold:
        return best_seq
    return None
```

**Примечание для Самурая:** функция выше — минимальный рабочий вариант. Если во время реализации обнаружен более точный/быстрый эквивалент, допускается замена, но контракт остаётся: «одна последовательность ≥ 8 символов, занимающая > 50% текста».

### b) В маркер-цикле, в месте, где уже есть `generated` и **до** записи PASS-артефактов и `cache_before = restored`, вставить проверку:

```python
rep_seq = detect_dominant_repetition(generated)
if rep_seq is not None:
    log(f"{marker.marker_id}: REPETITION_DETECTED seq_len={len(rep_seq)}")
    # Retry once with max_tokens=384
    response_retry = llm.create_chat_completion(
        messages=[
            {"role": "system", "content": system_payload},
            {"role": "user", "content": user_payload},
        ],
        max_tokens=384,
        temperature=writer["temperature"],
        top_p=writer["top_p"],
    )
    completion_calls += 1
    generated_retry = response_retry["choices"][0]["message"]["content"] if response_retry.get("choices") else None
    if generated_retry is None:
        raise ValueError(f"GENERATION_FAILED on retry: {marker.marker_id}")
    generated_retry = str(generated_retry)
    rep_seq_retry = detect_dominant_repetition(generated_retry)
    if rep_seq_retry is not None:
        raise ValueError(
            f"REPETITION_UNRECOVERABLE: {marker.marker_id} "
            f"initial_seq_len={len(rep_seq)} retry_seq_len={len(rep_seq_retry)}"
        )
    generated = generated_retry
```

**Инвариант:**

- Если повтор при первом inference не обнаружен — поведение не меняется.
- Если обнаружен — один повтор с `max_tokens=384`.
- Если повтор снова обнаружен — STOP (`ValueError`), cache не обновляется (до `cache_before = restored` дело не доходит), FINAL не пишется, `run.log` и `summary.json` фиксируют STOP.
- `raw_output.md` и последующие артефакты пишутся после успешного retry только для финального `generated`.

### c) Что не менять

- `normalize_slots`, `restore_protected`, `rebuild_interval`, `enforce_output_sanitation`, `enforce_no_new_tables` — не трогать.
- `cache_before = restored` — оставить на прежнем месте (после PASS).
- Логику FINAL assembly — не трогать.

---

## MANDATORY_PHYSICAL_READBACK

После edit — перечитать с диска и привести в отчёте фактические строки (номер + текст) для:

```powershell
Get-Content E:\Gemini\dojo\Manuscript_Press\config\writer_config.yaml
Get-Content E:\Gemini\dojo\Manuscript_Press\src\production_runner.py | Select-String -Pattern "max_tokens|detect_dominant_repetition|REPETITION_DETECTED|REPETITION_UNRECOVERABLE" -Context 2,2
```

Подтвердить:

- в `writer_config.yaml` присутствует строка `max_tokens: 768`.
- в `writer_config.yaml` `path`, `n_ctx`, `temperature`, `top_p` — без изменений.
- в `production_runner.py` присутствует определение `def detect_dominant_repetition`.
- в `production_runner.py` присутствует вызов `detect_dominant_repetition(generated)`.
- в `production_runner.py` присутствует `REPETITION_DETECTED` в логе.
- в `production_runner.py` присутствует `REPETITION_UNRECOVERABLE`.
- в блоке retry указан `max_tokens=384`.

---

## LOCAL_VERIFY

### 1. py_compile

```powershell
E:\Gemini\dojo\Manuscript_Press\.venv\Scripts\python.exe -m py_compile src\production_runner.py
```

Ожидаемо: exit 0, без вывода.

### 2. Preflight-only

```powershell
E:\Gemini\dojo\Manuscript_Press\.venv\Scripts\python.exe -m src.production_runner --preflight-only
```

Ожидаемо:

- exit 0
- `ProtectedSpanParser: PASS`
- `SourceParser: PASS marker_count=375`
- `PromptMapParser: PASS`
- `SourcePromptMapValidator: PASS`
- `PREFLIGHT_ONLY: complete, no inference`
- `load_model` не вызывался
- `create_chat_completion` не вызывался

Модель не запускать.

---

## EVIDENCE

В отчёт включить:

- `config/writer_config.yaml` — фактическое содержимое (или как минимум блок `model` и `generation`)
- `config/writer_config_9b.yaml` — mtime/содержимое без изменений (подтверждение)
- `config/writer_restless_quill.yaml` — mtime/содержимое без изменений (подтверждение)
- фактические строки из readback (EDIT 2)
- вывод `py_compile`
- вывод `--preflight-only`: exit code, `marker_count`, отсутствие `load_model` / `create_chat_completion`

---

## REPORT

```yaml
STEP_REPETITION_GUARD_AND_MAX_TOKENS_REPORT:
  files_modified:
    - config/writer_config.yaml
    - src/production_runner.py

  writer_config_content: |
    <полное содержимое writer_config.yaml>

  writer_config_9b_unchanged: yes / no
  writer_restless_quill_unchanged: yes / no

  physical_lines:
    writer_config_max_tokens: "<num>: <text>"
    detect_dominant_repetition_def: "<num>: <text>"
    detect_call_in_loop: "<num>: <text>"
    repetition_detected_log: "<num>: <text>"
    retry_max_tokens_384: "<num>: <text>"
    repetition_unrecoverable: "<num>: <text>"

  py_compile: PASS / FAIL

  preflight_only:
    executed: yes/no
    exit_code: <int>
    marker_count: <N>
    load_model_called: false
    completion_called: false

  output_runs_20261003T144957Z_untouched: yes / no
  inference_executed: false
  second_run: none
  next: STOP → WAIT_FOR_SENSEI
```

**Только фактически подтверждённое. Без «assumed», «likely», «presumably».**

---

## NON-GOALS

- запуск модели
- full article run
- resume / hybrid
- подмена файлов в `Output\runs\20261003T144957Z\`
- удаление `Output\runs\20261003T144957Z\`
- правки `writer_config_9b.yaml`, `writer_restless_quill.yaml`
- правки SOURCE, PROMPT_MAP, Gemma.md, loader.py, парсеров
- правки `manuscript_press.bat`, `resume_manuscript_press.bat`
- правки `SPEC.md`, `SPEC_v3.2.2.md`
- второй прогон при ошибке

---

## END PROTOCOL

```text
EDIT → PY_COMPILE → PREFLIGHT-ONLY → REPORT → STOP → WAIT_FOR_SENSEI
```

Модель не запускать.

---

```yaml
BRIGADIER_STATUS:
  step: REPETITION_GUARD_AND_MAX_TOKENS
  version: 1.0
  status: READY_FOR_SAMURAI
  scope: writer_config max_tokens=768 + repetition guard + retry max_tokens=384
  inference: NOT_AUTHORIZED
  full_run: RED
  stop: true
```

STOP.