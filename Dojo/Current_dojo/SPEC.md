📋 MANUSCRIPT_PRESS ENGINEERING SPEC v3.2.2 — GROK REVIEW CANDIDATE
1. TERMINOLOGY & INVARIANTS
yaml

PRODUCTION_REVISION:          frozen snapshot of all authority inputs.
SOURCE_MANUSCRIPT:            единый целостный текст с production markers.
PROMPT_MAP:                   per-marker instructions (LONG_RANGE + LOCAL).
STABLE_CONFIG:                глобальный литературный контракт.
WRITER_CONFIG:                generation knobs + context capacity (из config/WRITER_CONFIG.yaml).
Gemma.md:                     system kernel.
MARKER:                       <!-- MP:XXXX --> — начало элементарного блока.
PROTECTED_SPAN:               <!-- MP:PROTECTED id="PXX_YY":BEGIN --> ... <!-- MP:PROTECTED id="PXX_YY":END -->
SLOTTED_SOURCE:               SOURCE с маркерами вместо защищённого текста.
SLOTTED_CANDIDATE:            вывод Gemma с маркерами вместо защищённого текста.
RESTORED_CANDIDATE:           SLOTTED_CANDIDATE с восстановленными PROTECTED_SPAN.
COMMIT_RECORD:                доказательство фиксации блока.
CACHE_BEFORE:                 verbatim prose предыдущего блока (если есть).
LONG_RANGE_FRAME:             per-marker контекст (позиция, reader state, scope).
LOCAL_TRANSFORMATION:         per-marker инструкция для текущего блока.

ONE TRANSACTION = ONE PRODUCTION MARKER BLOCK.
Один вызов Gemma обрабатывает ровно один MP блок.
2. FILESYSTEM LAYOUT
text

config/
  WRITER_CONFIG.yaml

source/                          # ПОДГОТОВИТЕЛЬНЫЕ / РЕДАКТИРУЕМЫЕ ВХОДЫ
  SOURCE_MANUSCRIPT.md
  PROMPT_MAP.yaml
  Gemma.md
  STABLE_CONFIG.yaml

work/
  revisions/
    <revision_id>/
      frozen/                    # ЗАМОРОЖЕННЫЕ АВТОРИТЕТЫ (активная revision)
        SOURCE_MANUSCRIPT.md
        PROMPT_MAP.yaml
        Gemma.md
        STABLE_CONFIG.yaml
        PRODUCTION_REVISION.manifest
      markers/
        MP-XXXX/
          candidate/
            raw.md
            slotted.md
            restored.md
            patched_slotted.md
            patched_restored.md
          output/
            canonical.md
          commit.yaml
      state.yaml

assembly/
  final_manuscript.md

Два физически разных слоя:

    A. Подготовительные входы (source/) — могут редактироваться для будущих revision.

    B. Активные замороженные авторитеты (work/revisions/<revision_id>/frozen/) — используются GENERATE, ACCEPT, RESUME, FINAL ASSEMBLY.

Изменение/несоответствие хеша активных замороженных авторитетов → REVISION_CHANGED → RUN_INVALIDATED.
3. SOURCE_MANUSCRIPT & PROMPT_MAP

SOURCE_MANUSCRIPT:

    SOURCE syntax: <!-- MP:0001 -->

    LOGICAL marker_id: MP:0001

    PROMPT_MAP key: MP:0001

    FILESYSTEM-safe directory: MP-0001

    Блок — от маркера до следующего маркера или EOF.

    Маркеры не обязаны быть численно смежными.

    Уникальность и порядок в SOURCE обязательны.

    Execution order — только из SOURCE order.

PROMPT_MAP (YAML):
yaml

MP:0001:
  LONG_RANGE_FRAME: |
    ...
  LOCAL_TRANSFORMATION: |
    ...

Валидация:

    Для каждого маркера в SOURCE есть ровно одна запись в PROMPT_MAP.

    Каждая запись имеет non-empty LONG_RANGE_FRAME и LOCAL_TRANSFORMATION.

    Обратное тоже верно.

    Порядок в PROMPT_MAP не влияет на выполнение.

4. PROTECTED SPAN GRAMMAR

В SOURCE:
text

<!-- MP:PROTECTED id="P42_01":BEGIN -->
The exact immutable text, which may span multiple lines,
contain "quotes", Markdown, `code`, and arbitrary syntax.
<!-- MP:PROTECTED id="P42_01":END -->

Правила парсинга:

    Protected spans распознаются ДО интерпретации производственных маркеров.

    <!-- MP:XXXX --> внутри валидного protected span — буквальный защищённый контент, НЕ производственная граница.

    Актуальный производственный маркер НЕ МОЖЕТ начинаться внутри открытого protected span.

    Автоматические Markdown-заголовки распознаются ТОЛЬКО вне protected span.

    Точный совпадающий END-разделитель внутри protected контента → PROTECTED_MARKUP_INVALID (V1, без escaping).

Преобразование:

    SOURCE → SLOTTED_SOURCE: ⟦MP_PROTECTED:P42_01⟧

    Gemma output → SLOTTED_CANDIDATE: ⟦MP_PROTECTED:P42_01⟧

    RESTORED_CANDIDATE: механическое восстановление exact frozen protected material.

Инварианты:

    START/END ID совпадают.

    ID уникальны внутри revision.

    Вложенность запрещена (V1).

    Несовпадающий START/END → PROTECTED_MARKUP_INVALID.

Protected Context (для Gemma):
text

BEGIN_PROTECTED_CONTEXT
P42_01: <exact protected material>
P42_02: <exact protected material>
END_PROTECTED_CONTEXT

5. PRODUCTION_REVISION MANIFEST

revision_id = SHA256(канонического payload).

Канонический payload:
json

{
  "source_sha256": "...",
  "prompt_map_sha256": "...",
  "stable_config_sha256": "...",
  "gemma_sha256": "...",
  "ordered_marker_graph": ["MP:0001", "MP:0005", "MP:0130"]
}

    Fixed key names, deterministic order, UTF-8, no insignificant whitespace.

    Идентичные frozen authority → идентичный revision_id.

6. WRITER_CONFIG (ИСТОЧНИК И ОПРЕДЕЛЕНИЕ)

Источник: config/WRITER_CONFIG.yaml
yaml

temperature: 0.0
top_p: 0.9
max_tokens: 3500
n_ctx: 8192
model_identifier: "Gemma-The-Writer-9B"

Свойства:

    НЕ часть PRODUCTION_REVISION.

    Может меняться между поколениями.

    GENERATE читает один снимок WRITER_CONFIG для каждого вызова.

    Контекстная валидация и генерация используют ОДИН загруженный конфиг для вызова.

    Фактические значения записываются в candidate metadata (SHOULD).

7. STABLE_CONFIG

STABLE_CONFIG: литературный контракт, включающий:

    authorial voice

    stable terminology

    epistemic discipline

    canon boundaries

    prohibition on invented substantive material

    cache semantics

    protected-material behaviour

    heading behaviour

    output cleanliness

Изменение STABLE_CONFIG → новая PRODUCTION_REVISION.
8. CONTEXT ASSEMBLY (GEMMA INPUT)

SYSTEM:
text

BEGIN_GEMMA_KERNEL
<Gemma.md>
END_GEMMA_KERNEL

BEGIN_STABLE_CONFIG
<STABLE_CONFIG>
END_STABLE_CONFIG

USER:
text

BEGIN_LONG_RANGE_FRAME
<per-marker LONG_RANGE_FRAME>
END_LONG_RANGE_FRAME

BEGIN_CONTINUITY_CACHE
<CACHE_BEFORE (если есть)>
END_CONTINUITY_CACHE

BEGIN_STRUCTURAL_CONTEXT
<structural passthrough material>
END_STRUCTURAL_CONTEXT

BEGIN_PROTECTED_CONTEXT
<P42_01: exact material>
<P42_02: exact material>
END_PROTECTED_CONTEXT

BEGIN_CURRENT_SOURCE
<SLOTTED_SOURCE текущего блока>
END_CURRENT_SOURCE

BEGIN_LOCAL_TRANSFORMATION
<per-marker LOCAL_TRANSFORMATION>
END_LOCAL_TRANSFORMATION

CACHE_ALWAYS_YIELDS — cache подчиняется всем hard constraints: SYSTEM/STABLE, SOURCE, LONG_RANGE, LOCAL.

Конфликт hard authorities:

    Совместимые → выполняются вместе.

    Несовместимые → CONTEXT_CONFLICT → STOP/QUERY.

    Gemma не выбирает победителя статистически.

9. PROTECTED MATERIAL PIPELINE
text

SOURCE
  ↓
SLOTTED_SOURCE (извлечение protected span IDs)
  ↓
Gemma (cold, stateless)
  ↓
SLOTTED_CANDIDATE
  ↓
Проверка: все expected slots ровно один раз, no duplicates, no unknown, ID не мутированы, порядок сохранён
  ↓
Механическое restoration
  ↓
RESTORED_CANDIDATE
  ↓
Human: REJECT / ACCEPT_AS_IS / ACCEPT_PATCHED
  ↓
CANONICAL_OUTPUT

10. ACCEPTANCE MODES

REJECT:

    Нет commit, advance, cache.

ACCEPT_AS_IS:

    Canonical output = RESTORED_CANDIDATE.

ACCEPT_PATCHED:

    Human редактирует SLOTTED_CANDIDATE (protected slots immutable).

    После патча:

        Revalidate protected slots.

        Механически восстановить protected material.

        Human подтверждает PATCH_SCOPE = NON_SUBSTANTIVE.

        Commit с acceptance_mode: PATCHED.

    Runtime не классифицирует патч.

11. STRUCTURAL PASSTHROUGH

Автоматический structural passthrough: Markdown ATX-заголовки (# ... ######) вне protected span.

Остальное immutable: явный MP:PROTECTED.

SOURCE парсинг сохраняет structural passthrough вместе с их точной позицией относительно текущего блока.

Финальная сборка: заголовки восстанавливаются из frozen SOURCE. Защищённые таблицы/формулы уже в canonical output и не дублируются.
12. CANDIDATE BINDING & ELIGIBILITY
yaml

revision_id: <active>
marker_id: MP:XXXX
generated_at: <timestamp>
candidate_hash: <sha256>

Eligibility (до commit):

    Active revision валидна.

    Candidate revision binding валиден.

    Candidate marker binding валиден.

    Candidate non-empty.

    Protected-slot integrity валидна.

    NO CONTROL_RESPONSE_PRESENT.

    NO CONTEXT_CONFLICT.

    Requested acceptance mode валиден.

    PATCHED declaration присутствует при необходимости.

13. CONTROL_RESPONSE

Любой <<QUERY: ...>> → CONTROL_RESPONSE_PRESENT → invalid.
Raw сохраняется для диагностики (SHOULD).
14. COMMIT_RECORD SCHEMA
yaml

commit_id: <deterministic: revision_id + marker_id + canonical_hash>
revision_id: <active>
marker_id: MP:XXXX
committed_at: <timestamp>
acceptance_mode: AS_IS / PATCHED
patch_scope: NON_SUBSTANTIVE   # только для PATCHED
candidate_hash: <sha256>
canonical_hash: <sha256>
previous_accepted_marker: MP:YYYY / null
previous_canonical_hash: <sha256> / null

15. COMMIT PROTOCOL (ATOMIC)

    Проверить revision.

    Проверить candidate binding + eligibility.

    Создать canonical output во временный файл.

    Атомарно publish canonical output.

    Создать COMMIT_RECORD во временный файл.

    Атомарно publish COMMIT_RECORD.

    Только после — атомарно обновить state.yaml.

Orphan: output есть, COMMIT_RECORD нет → никогда не считается закоммиченным.
16. IDEMPOTENT ACCEPT

Для AS_IS:

    Тот же marker + тот же candidate_hash + тот же canonical_hash → ALREADY_COMMITTED.

Для PATCHED:

    Тот же candidate_hash + тот же canonical_hash + тот же acceptance_mode → ALREADY_COMMITTED.

В любом другом случае: COMMIT_CONFLICT → STOP.
17. RESUME / RECOVERY

    Проверить PRODUCTION_REVISION (из frozen/).

    Загрузить ordered marker graph.

    Просканировать COMMIT_RECORD для активной revision.

    Проверить непрерывность префикса и цепочку.

    LAST_ACCEPTED = последний commit в префиксе.

    CURRENT = первый uncommitted marker.

    CACHE_BEFORE = verbatim output из LAST_ACCEPTED.

    Перестроить state.yaml (если расходится).

Если префикс не непрерывен → STATE_INTEGRITY_FAILURE.

Кросс-ревизионная изоляция: артефакты/коммиты/кандидаты из revision A с идентичными marker ID НЕ участвуют в resume, cache, прогрессе или сборке revision B. Сканируются ТОЛЬКО артефакты активной revision.
18. CONTEXT-WINDOW VALIDATION

Перед GENERATE рассчитать фактический контекст и проверить против n_ctx из WRITER_CONFIG.

Failure: SEGMENTATION_TOO_LARGE_FOR_CURRENT_WRITER_CONFIGURATION.
Правила: нет truncation, нет auto-split, нет drop CACHE/config.
19. FINAL ASSEMBLY

    Доступна только когда весь граф маркеров закоммичен.

    Собрать canonical outputs в порядке SOURCE.

    Восстановить structural passthrough (заголовки) из frozen SOURCE.

    Защищённые таблицы/формулы уже в canonical output и не дублируются.

20. FAILURE TAXONOMY
yaml

REVISION_CHANGED (активный замороженный authority изменён)
RUN_INVALIDATED
MARKER_GRAPH_INVALID
SOURCE_PROMPT_MAP_MISMATCH
PROMPT_ENTRY_INVALID
PROTECTED_MARKUP_INVALID
PROTECTED_MATERIAL_VIOLATION
CONTROL_RESPONSE_PRESENT
CONTEXT_CONFLICT
STATE_INTEGRITY_FAILURE
CACHE_INTEGRITY_FAILURE
SEGMENTATION_TOO_LARGE_FOR_CURRENT_WRITER_CONFIGURATION
GENERATION_FAILED
CANDIDATE_INVALID
COMMIT_CONFLICT

21. IMPLEMENTATION ACCEPTANCE TESTS

    duplicate SOURCE marker → MARKER_GRAPH_INVALID

    missing PROMPT_MAP entry → SOURCE_PROMPT_MAP_MISMATCH

    extra PROMPT_MAP entry → SOURCE_PROMPT_MAP_MISMATCH

    PROMPT_MAP order differs from SOURCE → нормально

    first block no cache → CACHE_BEFORE отсутствует

    cold/stateless second block uses exact previous prose → cache корректен

    missing previous canonical output → CACHE_INTEGRITY_FAILURE

    inline protected span → restored валиден

    multiline protected span → restored валиден

    protected material with quotes/Markdown/code → restored валиден

    missing protected slot → PROTECTED_MATERIAL_VIOLATION

    duplicated protected slot → PROTECTED_MATERIAL_VIOLATION

    unknown protected slot → PROTECTED_MATERIAL_VIOLATION

    changed slot order → PROTECTED_MATERIAL_VIOLATION

    control response alone → CONTROL_RESPONSE_PRESENT

    control response mixed with prose → CONTROL_RESPONSE_PRESENT

    editable preparation SOURCE changes after freeze → активная revision остаётся валидной

    frozen active-revision SOURCE changes → REVISION_CHANGED / RUN_INVALIDATED

    same ACCEPT repeated → ALREADY_COMMITTED

    same candidate, different PATCHED patch → COMMIT_CONFLICT

    different candidate after commit → COMMIT_CONFLICT

    crash after output before commit → orphan

    crash after commit before STATE update → commit восстанавливается

    corrupted STATE with intact commits → STATE перестраивается

    non-contiguous commit prefix → STATE_INTEGRITY_FAILURE

    wrong previous_canonical_hash chain → STATE_INTEGRITY_FAILURE

    ACCEPT_PATCHED + resume → патч сохраняется

    attempted protected-material patch → rejected

    final marker → EOF → валидный блок

    context overflow by CACHE → SEGMENTATION_TOO_LARGE...

    structural heading passthrough → заголовки восстанавливаются

    deterministic final assembly after restart → воспроизводимо

    artifacts from previous revision with identical marker IDs are ignored → кросс-ревизионная изоляция

22. NON-GOALS
text

❌ Нет SOURCE editing.
❌ Нет PROMPT_MAP editing.
❌ Нет marker placement.
❌ Нет BAD CUT decision.
❌ Нет automatic segmentation.
❌ Нет automatic oversized split.
❌ Нет semantic PATCH validation.
❌ Нет global manuscript review.
❌ Нет inferred missing instructions.
❌ Нет resident literary memory.
❌ Нет generated summary/handoff.
❌ Нет revision migration V1.
❌ Нет autonomous rewrite of protected material.
❌ Runtime никогда не решает ACCEPT vs REJECT.
🎌