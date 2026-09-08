📋 MANUSCRIPT_PRESS — IMPLEMENTATION_PLAN.md
МИССИЯ

Реализовать систему Manuscript Press строго по замёрзшей ENGINEERING SPEC v3.2.2. Не добавлять архитектуру, не упрощать модель, не решать дизайнерские вопросы. Если SPEC неоднозначна — STOP → IMPLEMENTATION BLOCKER.
ЗАМОРОЖЕННЫЙ АВТОРИТЕТ

Единственный нормативный документ:
MANUSCRIPT_PRESS ENGINEERING SPEC v3.2.2

Самурай НЕ должен:

    искать решения в старых черновиках;

    опираться на обсуждения в чате;

    использовать предыдущие архитектуры как образец.

Если реализация расходится со SPEC — это блокер, а не повод для правки SPEC.
ЗАПРЕЩЕНО (НАРУШЕНИЕ = БЛОКЕР)

    ❌ Изменять архитектуру (marker grammar, protected-span semantics, commit/recovery semantics, typed authority domains).

    ❌ Добавлять autonomous literary logic, agents, summaries, handoffs, resident literary memory.

    ❌ Оптимизировать deterministic шаги.

    ❌ Использовать старую пакетную архитектуру как образец.

    ❌ Переопределять значения из SPEC под «удобство реализации».

ШАГ 0: АУДИТ РЕПОЗИТОРИЯ (ПЕРЕД КОДИНГОМ)

Самурай должен прочитать:

    CODING_PHILOSOPHY.md (или локальный инженерный устав, если есть);

    текущую структуру проекта;

    Gemma.md;

    существующие файлы генератора/рантайма;

    существующие конфиги и тесты;

    замёрзшую SPEC v3.2.2.

Идентифицировать для каждого существующего компонента:

    KEEP — совместим с SPEC, оставить.

    REPLACE — несовместим, переписать.

    DEPRECATE — устарел, исключить.

    NEW — отсутствует в коде, создать.

Никаких изменений на этом этапе. Только карта состояния.

DELIVERABLE: отчёт IMPLEMENTATION_MAP.yaml с четырьмя категориями.
ФАЗЫ РЕАЛИЗАЦИИ (ПОСЛЕДОВАТЕЛЬНО)

Каждая фаза завершается отчётом:

    FILES CHANGED

    WHAT WAS IMPLEMENTED

    TESTS RUN + RESULTS

    KNOWN LIMITATIONS

    SPEC SECTIONS SATISFIED

Переход к следующей фазе — только после человеческого подтверждения.
ФАЗА 1: CORE PARSERS + REVISION FREEZE

Реализовать и протестировать:

    парсер SOURCE markers (<!-- MP:XXXX -->);

    парсер PROMPT_MAP (YAML, ключи MP:XXXX);

    парсер PROTECTED spans (BEGIN/END, ID matching);

    structural passthrough extraction (ATX-заголовки);

    преобразование логического ID → filesystem-safe имя;

    валидацию: каждый SOURCE marker → ровно одна PROMPT_MAP запись, и наоборот;

    заморозку авторитетов (копия в work/revisions/<rev_id>/frozen/);

    детерминированный PRODUCTION_REVISION.manifest + revision_id (SHA256 канонического JSON);

    валидацию revision (при старте, перед GENERATE, перед COMMIT).

ФАЗА 2: BLOCK EXTRACTION + CONTEXT ASSEMBLY

Реализовать и протестировать:

    выбор одного блока по маркеру (один MP → одна транзакция);

    построение SLOTTED_SOURCE (замена protected span на ⟦MP_PROTECTED:ID⟧);

    сборку PROTECTED_CONTEXT (ID → exact protected material);

    сборку STRUCTURAL_CONTEXT (заголовки);

    восстановление CACHE_BEFORE из последнего canonical output;

    загрузку LONG_RANGE_FRAME и LOCAL_TRANSFORMATION из PROMPT_MAP;

    сборку SYSTEM (Gemma.md + STABLE_CONFIG);

    сборку USER (все 6 блоков по порядку, cache опционален);

    загрузку WRITER_CONFIG одним снимком;

    валидацию контекстного окна (против n_ctx).

БЕЗ COMMIT ЛОГИКИ.
ФАЗА 3: GENERATION + CANDIDATE PIPELINE

Реализовать и протестировать:

    cold/stateless вызов Gemma (один блок, один inference);

    привязку кандидата к revision_id и marker_id;

    сохранение raw.md, slotted.md, restored.md;

    детектирование CONTROL_RESPONSE (<<QUERY: ...>>);

    валидацию protected slots (все expected ровно один раз, без дубликатов/неизвестных/нарушения порядка);

    механическое восстановление protected material (замена ID на exact frozen текст);

    проверку eligibility кандидата (все gates).

Генератор НЕ коммитит и не двигает прогресс.
ФАЗА 4: HUMAN ACCEPTANCE + COMMIT

Реализовать и протестировать:

    REJECT — no commit; no cursor advance; CACHE_BEFORE remains unchanged;

    ACCEPT_AS_IS (canonical = restored);

    ACCEPT_PATCHED:
    Human edits SLOTTED_CANDIDATE.
    Protected slots remain locked / immutable.
    After edit → revalidate slots → mechanical restore →
    human declares PATCH_SCOPE = NON_SUBSTANTIVE.
    Runtime does not classify whether the patch is substantive.

    создание canonical output;

    создание COMMIT_RECORD (schema из SPEC);

    атомарный протокол (output → record → state);

    orphan semantics (output без record — не commit);

    идемпотентный ACCEPT (повтор того же → ALREADY_COMMITTED; другой candidate → COMMIT_CONFLICT);

    защита protected материала от патча.

ФАЗА 5: RESUME / RECOVERY

Реализовать и протестировать:

    проверку активной revision при старте;

    сканирование commit-книги (только активная revision);

    валидацию непрерывного префикса;

    валидацию цепочки (previous_accepted_marker + previous_canonical_hash);

    восстановление LAST_ACCEPTED и CURRENT;

    восстановление CACHE_BEFORE из canonical output;

    перестройку state.yaml (если расходится с commits);

    устойчивость к сбоям: output без commit, commit без state, битый state при валидных commits;

    кросс-ревизионную изоляцию (артефакты старой revision не влияют на новую).

ФАЗА 6: ASSEMBLY

Реализовать и протестировать:

    финальную сборку только после полного commit-графа;

    восстановление structural passthrough (заголовки) из frozen SOURCE;

    без повторного восстановления protected material (оно уже в canonical output);

    preview/partial assembly (для отладки);

    детерминированную воспроизводимость после перезапуска.

ФАЗА 7: ПОЛНЫЙ НАБОР ПРИЁМОЧНЫХ ТЕСТОВ

Реализовать все 33 нормативных теста из SPEC v3.2.2.

Ни один тест не может быть пропущен, ослаблен или интерпретирован иначе.

Тесты должны проверять:

    дубликаты/пропуски маркеров;

    несоответствия SOURCE ↔ PROMPT_MAP;

    protected spans (inline, multiline, специальные символы);

    маркер-подобный синтаксис внутри protected material;

    control response mixed with prose;

    изменение редактируемого SOURCE после freeze;

    мутацию замороженного SOURCE;

    разные PATCHED-выходы из одного raw кандидата;

    crash между output и commit;

    crash между commit и state;

    битую цепочку commit;

    кросс-ревизионную изоляцию;

    переполнение контекста из-за CACHE;

    детерминированную финальную сборку после рестарта.

ОПРЕДЕЛЕНИЕ ГОТОВНОСТИ (DONE)

Проект считается завершённым ТОЛЬКО когда:

    все компоненты SPEC v3.2.2 реализованы;

    все 33 acceptance-теста проходят;

    нет легаси-путей, обходящих revision/commit семантику;

    cold/stateless работа чиста;

    resume и финальная сборка детерминированы;

    protected material доказано неизменяемо (тестами).

ПРОТОКОЛ БЛОКИРОВКИ

Если при реализации SPEC оказывается неоднозначной или противоречивой:

    IMPLEMENTATION BLOCKER

        точная секция SPEC

        точная причина (чего не хватает или что противоречит)

Самурай НЕ чинит SPEC, НЕ принимает архитектурных решений, НЕ продолжает с «наиболее вероятной» интерпретацией.

Он останавливается, возвращает блокер и ждёт ответа.
ФОРМАТ ФИНАЛЬНОГО ОТЧЁТА
yaml

Phase: <номер фазы>
Status: COMPLETED / BLOCKED
Files_Changed: [...]
Implemented: [...]
Tests_Run: [...]
Test_Results: [...]
Limitations: [...]
SPEC_Sections_Satisfied: [...]
Next: WAIT_FOR_APPROVAL / BLOCKED

Самурай, приступай к ШАГУ 0: АУДИТ РЕПОЗИТОРИЯ. Прочитай CODING_PHILOSOPHY.md (или локальный устав) перед любыми действиями.

🎌 Никакого кода до аудита. Только карта состояния.
