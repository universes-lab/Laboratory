# AI_COLAB_2_LEGACY_TO_TARGET_RECONCILIATION_DRAFT — часть Developer Claude

STATUS: DRAFT (часть Claude; разделы DeepSeek помечены `[DEEPSEEK]`; общий документ не сведён, разногласий пока не зафиксировано)

Метки происхождения утверждений: **[CODE]** — подтверждено прочитанным кодом (CODE_READ/STATIC_ANALYZED, без запуска); **[DOC]** — положение исторического документа; **[PROPOSAL]** — новое предложение разработчика; **[RECALL]** — память разработчика без паспорта (не свидетельство).

---

## SOURCES_USED

LEGACY_CODE (HF `lhc-lab/AI-Colab`, REVISION UNKNOWN):
- 17 файлов из P0.1 + 6 файлов пакета P0.2-A (паспорта в `CLAUDE_P0_1_LEGACY_CODE_EVIDENCE_REPORT` и `EVIDENCE_PACKAGE_P0_2_A`). Новые находки F-15…F-18 — в записке для DeepSeek.

PROJECT_DISCUSSIONS (фактически прочитано мной, загружено Автором):
- `AI_COLAB_2_PROGRAM_PLAN.md` (+ дополнение «Samurai Repository/File Guide»)
- `Endpoint_Spike.md` v3.1
- `Secretary_search.md`, `Secretary_topic.md`, `Secretary_topic-part3.md` (протоколы дискуссий)
- `control-plane-discovery.md` (моя Discovery-разведка)

KNOWN_LIMITATIONS:
- `HONC_AI-Collaboration_Control_Plane-Roadmap.md` и `Readme.md` из `Plan_AI-Collab` **мне не доступны** (в HF-датасете каталога `Laboratory/` нет; файлы не загружены). Дорожная карта в разделах ниже восстановлена только по пересказам в дискуссиях. Нужен файл от Автора.
- `Old_discussions/Secretary*.md`: прочитаны три загруженных файла; другие, если есть, не читались.
- Секции о реальном поведении (запуск, сеть, стабильность DOM/API) **не имеют рантайм-подтверждения**; Endpoint Spike v3.1 **не исполнялся**.
- Roadmap-утверждения «принято Автором» берутся из Program Plan §12 и сообщений Интегратора; других протоколов решений Автора я не видел.

---

## LEGACY_CAPABILITY_MAP (сторона коммуникации и workspace; полная карта — [DEEPSEEK])

| Возможность | Что показывает код | Уровень |
|---|---|---|
| Web-seat (постоянный авторизованный веб-чат) | **Отсутствует.** Нет playwright/selenium/webview в 20 прочитанных .py [CODE]. UI — собственный Quart + templates/static (static/chat.js не читался) | STATIC |
| Agent-seat (OpenRouter, роли → модели) | `RoleBindingManager`: отделы A–D по 2 роли, sticky-binding md5(role) % pool, последовательный «улучши результат коллеги» [CODE] | STATIC |
| Локальный исполнитель (Samurai) | Gemini CLI: ephemeral `execute()` stdin→JSON; legacy WS-серверы; GCB-очередь с shell [CODE] | STATIC |
| Конверт сообщений FROM/TO/THREAD | **Отсутствует.** Обмен — запрос/ответ HTTP/WS между UI и роль-цепочкой; единственная «структура» — `[TASK]` + JSON [CODE] | STATIC |
| Проверка прав / permit | **Не обнаружена.** gateway — интерпретатор ответа; HIL-логгер не вызывается [CODE] | STATIC |
| Состояние офиса / dynasty | **Нет.** `roles_state.json` хранит связки роль↔модель; понятий office/occupant/dynasty нет [CODE; roles_state читался как путь, не как содержимое] | STATIC |
| Восстановление после сбоя | Лок отдела не снимается (F-3/F-4); ошибки CLI возвращаются как обычный текст (F-17) [CODE] | STATIC |

## REUSE_CANDIDATES / REWORK_OR_REPLACEMENT_CANDIDATES
`[DEEPSEEK]` — основной автор. Моя позиция по сторонам, где я располагаю свидетельствами:
- **Идея** sticky-binding «роль → модель» с явным переключением (`switch_binding(reason)`) соответствует требованию Program Plan «office ≠ model» только на уровне *Agent-seat*. Как код — REWORK (дефекты F-3/F-4). [PROPOSAL, не утверждение пригодности]
- Концепция ephemeral-вызова CLI «одно сообщение — один процесс» — кандидат для Samurai-транспорта *как идея*; без изоляции параметров (F-6) и с утечкой префикса ключа (F-13) — REWORK. [PROPOSAL]
- GCB (shell из очереди) — не кандидат без отдельного решения о безопасности. [CODE+PROPOSAL]
- Для web-seat и конвертов у легаси **нечего переиспользовать** — это NEW. [CODE]

---

## HISTORICAL_ARCHITECTURE_OPTIONS

### ACCEPTED (Program Plan §12; решение Автора/Интегратора) [DOC]
1. AI-Colab 2 — размораживается позже; старая система и живая коллаборация сливаются концептуально.
2. Управляются **офисы (seats)**, а не «взаимозаменяемые модели»; OFFICE ≠ OCCUPANT ≠ DYNASTY ≠ SESSION/WORKSPACE.
3. Persistent web-чаты — первоклассные кандидаты в occupants; браузерный слой исследуется как часть AI-Colab.
4. Secretary/postman переосмыслен как **внутренняя шина маршрутизации**, браузерная доставка — только где необходима.
5. OpenRouter-персонал — отдельный класс (Agent seats); Samurai — локальный исполнитель.
6. Dynastic succession и наследование — архитектурные понятия; финальная власть у Автора; автономная самомодификация конституций не разрешена.
7. Ограничения §14: не делать browser-automation фундаментом; graceful degradation (видимое ручное действие вместо выдуманного успеха); provenance; не смешивать web-память и институциональную память.
8. Samurai Repository/File Guide: детерминированный показ (TREE/FILE/LINES/DIFF/COMMIT) + Gemini-Секретарь (SUMMARY/EXTRACT), provenance-шапка, read-only по умолчанию, белый список корней, исключение секретов (дополнение, принято как расширение плана).
9. Разделение (Discovery-итог Методолога, принято): **Endpoint Adapter** — детерминированный технический доступ без смыслового видения; **Secretary** — семантическое видение метаданных без технического доступа к BODY. «Technical access ≠ semantic visibility» — RETAIN.

### EXPERIMENTALLY_SUPPORTED
**Пусто — по корпусу, который я видел.** Всё, что звучит как «подтверждено», — либо ручная практика коллаборации (персистентные чаты, династии, Автор как курьер), либо чтение документации/кода внешних репозиториев:
- ctxport: мной прочитан код (STATIC_ANALYZED): использует **внутренние API платформ** (same-origin fetch с cookies), а не DOM-парсинг — поправка к более раннему мнению DeepSeek/Методолога («DOM parsers», «ADAPTABLE»). Рантайм не проверялся; Chrome Web Store статус «Coming soon» по README. [DOC+STATIC]
- Endpoint Spike v3.1 (Stage 0 API-check 5/5, Stage 1 N=30 CDP-сценарии, Stage 2 двухнедельный мониторинг) — **SPEC VALID/REUSABLE, не исполнялся.**

### PROPOSED (гипотезы разработчиков; приняты только как кандидаты) [DOC: Secretary_topic]
- **PULL/mailbox внутри, PUSH на границе** (гибрид): адресованные пакеты в `mailboxes/{id}/inbox/{pkg}/`, Courier заканчивает работу атомарной доставкой в ящик; будущий wake: push / polling / manual («проверь почту»).
- Конверт: message_id, parent_id, task_id, from, to, triad, timestamp, status, body_ref, reply_to.
- Прогрессивное раскрытие L0–L3 (каталог сотрудников → метаданные → … → BODY только исполнителю).
- Хранение: SQLite (метаданные/реестр) + файловая система (BODY) — минимальный прототип (Методолог поддержал «не собирать Zero+AutoContext+Redis одновременно»).
- Endpoint: Playwright + CDP-attach как ведущий кандидат; Browser-bridge проекты (ai-browser-bridge и др.) — надстройки над ним.
- Durable-слой: Temporal/Inngest/Restate; политики: OPA; протокол-модель сотрудника: A2A; UI: React Flow; MCP/SLIM — все **гипотезы, понижены Методологом из «решений»**.
- Прототипный каркас FastAPI/SQLAlchemy (Secretary/Courier/Audit) от DeepSeek — иллюстративный скелет, не принят.
- Program Plan §4.3: сравнить Electron/CEF/PySide-QWebEngine/внешний Chromium-профиль как хост для web-seats — **список кандидатов, выбор не сделан**.
- Из Endpoint Spike v3.1: A-API параллельно с A-DOM; self-report per-call через API; ctxport как источник адаптеров (DeepSeek-предложение, см. поправку выше).

### SUPERSEDED / ОТВЕРГНУТО
- «Secretary как человекоподобный почтальон по браузерам — фундамент» — заменено внутренней шиной (Program Plan §7). [DOC]
- «Playwright — единственный путь» (DeepSeek) — снято Методологом как слишком сильное; статус: ведущий кандидат, нуждающийся в проверке. [DOC]
- Тема Claude Desktop как endpoint — закрыта в Secretary_search. [DOC]
- Преждевременный выбор стека (Temporal+Playwright+SQLite+OPA «берём») — возвращён в Mapping. [DOC]
- Secretary как отдельная «постоянно думающая» модель — статус RE-EVALUATE (не отвергнуто окончательно). [DOC]

### OPEN (Program Plan §13 + Discovery)
Хост web-seats (Electron/CEF/Qt/внешний Chromium); можно ли встраивать все провайдеры; безопасное хранение сессий; число профилей; формат конверта/протокол; уровень автоматизации и автоматическая вставка; интерчейндж API↔web-seat; хранение учётных данных; восстановление сессии; локально vs сервер; таксономия ролей; формат dynasty-файла; модель безопасности продакшена; есть ли готовый control room с организационным графом (Discovery: не найден — «не обнаружено», не «не существует»).

---

## LEGACY_TO_TARGET_MAPPING (моя сторона)

| Цель AI-Colab 2 | Факт в легаси | Статус моста |
|---|---|---|
| Organizational roles / model staff | Agent-seats через RoleBindingManager | Частичное покрытие; office/occupant/dynasty — NEW |
| Маршрутизация и коммуникация | Нет конверта; цепочка ролей внутри отдела | NEW (конверт, mailbox) |
| Web-seat/workspace | Нет | NEW; ключевой неопределённый узел (хост, авторизация) |
| Сохранение состояния | `roles_state.json`/`models_config.json` (связки), логи ролей по `ProjectContext` | Ничтожное покрытие institutional memory |
| Контроль разрешений | Не обнаружен (gateway ≠ permit) | NEW |
| Gemini CLI / Samurai | Ephemeral executor + legacy WS + GCB | Транспорт как идея; безопасность — REWORK |
| Файловое обслуживание участников (Repository Guide) | Не обнаружено; ближайший — `validate_path` в `gemini_mcp_server2.py` | NEW |
| Восстановление после отказов | Нет; ошибки скрываются в строках | NEW |

Принцип, который я предлагаю соблюдать при сведении: легаси даёт **Agent-seat + Samurai-транспорт**; остальные пункты мишени — новые, и их опора — дискуссии (Secretary/Spike/Program Plan), а не код.

---

## DESIGN_ALTERNATIVES (communication / web-workspace; без выбора стека) [PROPOSAL]

**Ось 1. Кто хостит web-seat.**
- (a) Внешние профили Chromium + CDP-attach; (b) встроенный shell (Electron/CEF/QtWebEngine); (c) гибрид: seats в профилях, UI AI-Colab — отдельное приложение.
- TRADEOFFS: (a) минимально меняет текущую практику и сохраняет логины, но зависит от внешних процессов и anti-bot; (b) единое окно, но риск отказов провайдеров во встроенных браузерах (Program Plan §4.3); (c) ближе к графу деградации §14.6.
- EVIDENCE_NEEDED: эксперимент «запуск и восстановление N фиксированных авторизованных seats» (Phase 1 плана) — **не выполнялся**.

**Ось 2. Модель доставки.**
- PULL (mailbox, ручное/semi-автоматическое пробуждение), PUSH (вставка в чат), HYBRID (внутри PULL, на границе PUSH).
- TRADEOFFS: PULL отодвигает сложность Courier и даёт видимый fallback; PUSH требует решения задач identity/окончание генерации/дублирование.
- EVIDENCE_NEEDED: Endpoint Spike A/B/B1/C; шаг 0 API-проверки.

**Ось 3. Чтение/запись endpoint.**
- Вариант чтения: внутренние API (по ctxport-образцу) / DOM / ручной экспорт; запись: вставка в DOM / API / ручной Ctrl-V.
- TRADEOFFS: API стабильнее по структуре, но недокументирован и ближе к нарушению условий платформ; DOM хрупок. Выбор остаётся Architecture (Spike §1).
- DEPENDENCIES: юридические/ToS-оценки (в спайк не входят).

**Ось 4. Состояние.** Файловое + SQLite (минимум) vs durable-engine; зависит от того, нужны ли таймеры/реплей на первом этапе. EVIDENCE_NEEDED: требования Автора к audit/replay.

**Ось 5. Repository Guide.** Детерминированный слой — отдельный компонент, независимый от LLM; семантический слой читает только через него; read-only + whitelist. Зависит от решения, какой процесс держит «окно в файлы» (Samurai-исполнитель vs выделенный сервис). EVIDENCE_NEEDED: подтверждение, что Gemini CLI позволяет ограничить корень и режим (в легаси `execute()` этого не делает).

Решаемо по имеющимся свидетельствам (кандидаты на решение триады): (i) принцип «PULL внутри/PUSH на границе» как рабочая гипотеза; (ii) read-only whitelist для Repository Guide; (iii) конверт и институциональное состояние как отдельный слой от transcript. Требует эксперимента: хост web-seats; endpoint чтение/запись; стабильность по платформам.

---

## DEVELOPER_DISAGREEMENTS (текущее)
- ctxport: DeepSeek — «DOM parsers → ADAPTABLE»; Claude — по коду это внутренние API-вызовы, адаптация в headless требует проверки; расхождение в формулировке, не в вердикте «рассмотреть как строительный блок». Требует сверки конкретных файлов ctxport (из чата DeepSeek паспортов нет).
- Живая точка входа: DeepSeek — app2.py «наиболее вероятен»; Claude — F-16 (start_server → app:app, порт 5000) делает вывод невозможным без E:-данных. Фиксируется как OPEN.

## QUESTIONS_FOR_AUTHOR
1. Загрузить `HONC_AI-Collaboration_Control_Plane-Roadmap.md` и `Readme.md` из `Plan_AI-Collab` — без них карта «что уже решено» неполная.
2. Нужны ли сейчас web-seats внутри AI-Colab как *встроенные* или достаточно удобной панели над внешними профилями?
3. Допустим ли для Spike/endpoint путь через внутренние API платформ (ToS-риск) или только DOM/ручной экспорт?
4. Требуется ли на первом этапе replay/таймеры (определяет, нужен ли durable-engine)?
5. `requirements.txt` в HF нечитаем (NUL-байты, вероятно UTF-16): разрешить ли позже получить его содержимое через исполнительную цепочку?

## PROPOSED_NEXT_PHASE
1. DeepSeek заполняет `[DEEPSEEK]` разделы после проверки пакета P0.2-A; разногласия — в таблицу.
2. Я прочитаю по HF файлы P1 (model_management, prompt_registry, shared_state, chat_storage, chief_orchestrator, doctor_engine, templates/static) по порядку, который назовёт DeepSeek.
3. Совместно сводим документ; затем STOP → Chief Integrator.
4. Любые рантайм-проверки и E:-манифест — только после выбора конкретного компонента-кандидата (позиция Интегратора).
