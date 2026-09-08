STEP — CONTINUITY INFERENCE BLOCKER (SAMURAI INSTRUCTION)

Назначение: Один исполняемый STEP для Самурая — закрыть blocker, не дающий create_chat_completion выполниться.

Статус: ЧЕРНОВИК — НЕ ИСПОЛНЯТЬ до подтверждения Grok/Шогуна.
ИДЕНТИФИКАЦИЯ
yaml

STEP:
  id: CONTINUITY_INFERENCE_BLOCKER
  type: CORRECTIVE
  target: src/continuity_cache_bench.py
  prerequisite: PREFLIGHT continuity bench — PASS, payload + CACHE — PASS, inference — 0 calls, abort — AttributeError: 'Llama' object has no attribute 'max_tokens'
  invariant: NO EXECUTION CLAIM WITHOUT EXECUTION EVIDENCE

PHASE A — PHASE A AUTHORIZED

Обязательна первой. Никаких правок в Phase A.
A.1 — Источник generation knobs

Выполнить read-only inspection src/continuity_cache_bench.py и определить:

    Откуда берутся max_tokens, temperature, top_p для вызова create_chat_completion:

        Из config/writer_config.yaml (через загрузку и чтение полей)?

        Из атрибутов загруженной модели (llm.max_tokens, llm.temperature, llm.top_p)?

        Из другого источника (указать)?

    Как эти значения передаются в create_chat_completion:

        Как именованные аргументы (max_tokens=..., temperature=..., top_p=...)?

        Как часть kwargs?

        Иным способом?

    Что loader.py передаёт в Llama(...) при инициализации:

        Ожидаемо: model_path, n_ctx, chat_format.

        Передаётся ли max_tokens, temperature, top_p на этапе инициализации?

        Если да — какие именно параметры?

A.2 — Классификация дефекта

На основании A.1 выбрать один из трёх классов:
yaml

CLASS:
  A: bench пытается читать generation knobs из атрибутов Llama-объекта (llm.max_tokens и т.п.), которых у объекта нет.
  B: loader.py при инициализации Llama(...) не передаёт параметры, которые bench потом ожидает.
  C: иное API / иной источник knobs (указать).

Отчёт Phase A (STOP после отчёта):
yaml

PHASE_A_REPORT:
  SOURCE_OF_KNOBS: <config / llm attrs / other>
  PASSED_TO_COMPLETION: <named args / kwargs / other>
  LOADER_INIT_PARAMS: <list>
  CLASS: A / B / C
  EVIDENCE: <цитата из кода или конкретное наблюдение>
  NEXT: WAIT_FOR_CLASS_CONFIRMATION

PHASE B — AUTHORIZED

Только после подтверждения CLASS A (или явной развилки).
B.1 — Принцип исправления

Generation knobs берутся только из:

    config/writer_config.yaml (загруженного и прочитанного ранее в скрипте)

    ИЛИ из уже прочитанного словаря/объекта конфигурации

Передаются в create_chat_completion как именованные аргументы (max_tokens=..., temperature=..., top_p=...).

Запрещено:

    Писать llm.max_tokens, llm.temperature, llm.top_p и аналоги.

    Менять loader.py, если CLASS ≠ B.

    Менять parsers, CACHE semantics, marker extraction.

B.2 — Принятие candidate diff (условно)

Если candidate diff Самурая (удаление чтений llm.max_tokens / .temperature / .top_p) совпадает с CLASS A — можно принять как основу.

Если CLASS ≠ A — заменить минимальным патчем, соответствующим фактическому источнику knobs.
B.3 — Проверка fix

После применения fix, но ДО rerun:

    Скрипт должен проходить preflight.

    create_chat_completion должен получать валидные именованные аргументы.

    Никаких AttributeError: 'Llama' object has no attribute 'max_tokens'.

Отчёт Phase B (STOP после отчёта):
yaml

PHASE_B_REPORT:
  CLASS_CONFIRMED: A / B / C
  FIX_APPLIED: <краткое описание>
  FILES_MODIFIED:
    - src/continuity_cache_bench.py
  PREFLIGHT_AFTER_FIX: PASS / FAIL
  NEXT: WAIT_FOR_GREEN_LIGHT

PHASE C — ОДИН КОНТРОЛИРУЕМЫЙ RERUN

Только после PASS Phase B и явного «GREEN LIGHT» от Grok (через Шёгуна).
C.1 — Условия запуска

    Phase B выполнен и подтверждён.

    Получен явный GREEN LIGHT от Grok/Шогуна.

    Архив Output/evidence/pre_controlled_rerun/ создан (если ещё нет — см. предыдущую инструкцию).

C.2 — Исполнение

Один controlled rerun текущего continuity bench:

    Те же входы: Input/TEST_SOURCE_MANUSCRIPT.md, Input/TEST_PROMPT_MAP.yaml, config/writer_config.yaml, Gemma.md, Output/SMOKE_MP-0101.md.

    Наблюдаемая цепочка состояний (один непрерывный run, без STOP между состояниями):
    text

    PREFLIGHT_PASSED
        → PAYLOAD_PERSISTED
        → INFERENCE_RETURNED
        → OUTPUT_PERSISTED
        → EVIDENCE_VERIFIED
        → FINAL_REPORT

C.3 — Evidence gate

SUCCESS запрещён без:

    Трёх physical files:

        Output/CONT_MP-0102.md (non-empty)

        Output/CONT_MP-0102.payload.txt (contains CACHE)

        Output/CONT_MP-0102.run.log (contains CREATE_CHAT_COMPLETION_CALLS: 1)

    CREATE_CHAT_COMPLETION_CALLS: 1

Preflight FAIL или 0 completions → честный FAILURE, без narrative SUCCESS.
C.4 — Отчёт
yaml

PHASE_C_REPORT:
  RUN_STATUS: SUCCESS / FAILURE
  CREATE_CHAT_COMPLETION_CALLS: <0 или 1>
  PRIMARY_EVIDENCE:
    - Output/CONT_MP-0102.md: <exists / absent>, <size>, <non-empty>
    - Output/CONT_MP-0102.payload.txt: <exists / absent>, <contains CACHE>
    - Output/CONT_MP-0102.run.log: <exists / absent>, <contains INFERENCE_RETURNED>
  BENCH_MECHANICS: PASS / FAIL
  NEXT: WAIT_FOR_GROK

ЗАПРЕТЫ (СКВОЗНЫЕ)

    Не переписывать SPEC / IMPLEMENTATION_PLAN.

    Не строить production orchestrator / commit / revision.

    Не делать самовольные follow-up edits после rerun.

    Не запускать python ... continuity rerun внутри Phase A/B без GREEN LIGHT.

    Не исполнять Phase C без явного GREEN LIGHT от Grok/Шогуна.

    Не писать STATUS: SUCCESS без трёх physical files + 1 completion.

ИТОГОВЫЙ ДОКЛАД БРИГАДИРА (GROK)
yaml

BRIGADIER_STATUS:
  step: CONTINUITY_INFERENCE_BLOCKER
  status: DRAFT — READY FOR GROK REVIEW
  phases:
    - A: READ_ONLY_LOCALIZATION — defined, STOP after report
    - B: MINIMAL_FIX — conditional on CLASS A, STOP after report
    - C: CONTROLLED_RERUN — requires GREEN LIGHT, STOP after report
  restrictions: enforced
  next: WAIT_FOR_GROK_SIGN_OFF


Бригадир на линии. STOP.
