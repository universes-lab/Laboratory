# AI_COLAB_2_LEGACY_TO_TARGET_RECONCILIATION_DRAFT — v1.2

STATUS: DRAFT (совместный документ Developer DeepSeek + Developer Claude; свод v1.0 — DeepSeek, правки v1.1 и v1.2 — Claude по редакторским указаниям Интегратора, принятым DeepSeek)
Режим: Research / Read Only. Production-SPEC, план кодирования, выбор технологий — НЕ содержатся.
Метки происхождения: **[CODE]** подтверждено прочитанным кодом (CODE_READ/STATIC_ANALYZED, без запуска) · **[DOC]** положение документа · **[DOC×DOC]** конфликт документов · **[DOC×CODE]** расхождение документа и кода · **[EXT]** внешний репозиторий, прочитан статически, паспорта в P0-пакетах нет · **[RECALL]** память разработчика (не свидетельство) · **[RECALL_CONFLICT]** память противоречит коду/документу · **[PROPOSAL]** предложение разработчика.
RUNTIME_VERIFIED: 0 пунктов. REVISION HF: UNKNOWN — закрывается фиксацией конкретного снапшота (commit SHA + манифест, см. Web-Seat план §9) **до любого исполняемого эксперимента**. Пригодность ни одного компонента к повторному использованию не доказана.
`LEGACY_ONLY`, `REWORK`, `REPLACE` в этом документе — предварительные **[PROPOSAL]** разработчиков, а не вердикты P0.

## Правки v1.2 (по указаниям Интегратора; для прозрачности)
1. F-27 переписан как **риск** преждевременного обрыва/усечения многоабзацного ответа (`stop=[…,'\n\n']` + `max_tokens=512`); во время выполнения не проверялось.
2. F-18 уточнён: «не обнаружено в просмотренном корпусе легаси» (а не «в легаси нет»).
3. `LEGACY_ONLY` — предварительное предложение разработчика `[PROPOSAL]`, не вердикт P0.
4. `REVISION HF: UNKNOWN` остаётся и блокирует **исполняемые** эксперименты до фиксации снапшота (способы — Web-Seat план §9).
5. Последний запускавшийся файл/порт не запрашивается у Автора как обязательный; допускается пометка `[RECALL: Author]`, проверка — экспериментом.
6. Чтение `requirements.txt` по сырым байтам — задача разработчика (Claude), не Автора.
7. Вопросы Хранителю пока не отправляются; инженерные вопросы остаются у разработчиков.
8. `Readme.md` и `HONC_AI-Collaboration_Control_Plane-Roadmap.md` прочитаны и включены в источники (хэши ниже). Конфликтов с содержанием карты не выявлено; принципы, значимые для экспериментов, сведены в Web-Seat план §2.2.
9. Из списка вопросов Автору убраны пункты о последнем запуске и `requirements.txt`.
10. v1.1 на GitHub совпадает с моей копией побайтно (SHA-256 префикс 0a288cdfffa9ed17).

## Правки Claude к своду v1.0 (v1.1; для прозрачности)
1. ctxport убран из карты старого кода: это внешний репозиторий, помечен [EXT] (в P0-пакетах его паспорта нет; мой статический разбор был раньше, в спайке).
2. `roles_state.json`: читалась логика загрузки/сохранения, содержимое файла — нет.
3. «Опровергнуто» по `Gemini вне чата` смягчено до «расхождение» (в UNIVERSAL есть режим secretary для CEO/Chief; код вызывает `call_gemini` из `/api/secretary` и Doctor-WS).
4. Восстановлены оси DESIGN_ALTERNATIVES 2–5 и пункты PROPOSED из моей части, которые выпали при сведении.
5. Добавлен реестр находок F-1…F-27 (в своде F-номера использовались без расшифровки). F-12 — не дефект, а заметка о способе чтения; F-14 не назначался.
6. Новая находка F-27 (см. реестр). *(Вопрос Автору о последнем запуске, введённый в v1.1, снят в v1.2 — см. правку 5.)*

---

## SOURCES_USED
LEGACY_CODE (HF `lhc-lab/AI-Colab`, REVISION UNKNOWN, паспорта в пакетах):
- `CLAUDE_P0_1_LEGACY_CODE_EVIDENCE_REPORT` v2 (17 файлов; ERRATA: `docs/architecture/ARCHITECTURE_MAP.md` = 53107 B, корневого нет)
- `EVIDENCE_PACKAGE_P0_2_A` (6 файлов), `_B` (9 файлов), `_C` (8 документов)

PROJECT_DISCUSSIONS: `AI_COLAB_2_PROGRAM_PLAN.md` (+ дополнение Repository Guide), `Endpoint_Spike.md` v3.1, `Secretary_search.md`, `Secretary_topic.md`, `Secretary_topic-part3.md`, `control-plane-discovery.md`.
ПРОЧИТАНЫ в v1.2 (DOCUMENT_READ; GitHub `universes-lab/Laboratory`, ветка main, HEAD `d5a7508414752562fe8fa97daaac002c52eea51d` на 2026-10-18; commit последнего изменения каждого файла не получен):
- `Dojo/Plan_AI-Collab/HONC_AI-Collaboration_Control_Plane-Roadmap.md` — 4073 B, SHA-256 префикс 27699ab34eca58a4
- `Dojo/Plan_AI-Collab/Readme.md` — 14746 B, SHA-256 префикс ba957f963265969b
- `Dojo/Plan_AI-Collab/Endpoint_Spike.md` (v3.1) — 18217 B, SHA-256 префикс 4a9256d58c4b8338
- `Dojo/Plan_AI-Collab/AI_COLAB_2_LEGACY_TO_TARGET_RECONCILIATION_DRAFT_v1.1.md` — SHA-256 префикс 0a288cdfffa9ed17
(Каталога `Plan_AI-Collab` в HF-датасете нет; эти документы живут в GitHub.)

KNOWN_LIMITATIONS: `requirements.txt` не прочитан (NUL-байты, вероятно UTF-16; нужны сырые байты — задача разработчика, пути в Web-Seat плане §9); UI (`static/chat.js`, `templates/index.html`) и движки `pce/cse/obe/soul_layer` не читались (осознанно); содержимое `roles_history.jsonl`, `calls_history.jsonl`, `docs/prompts/*` (кроме списка имён), `integrations/model_formatter.py` не читалось; Endpoint Spike v3.1 не исполнялся; E:-манифест не запрошен.

---

## LEGACY_CAPABILITY_MAP
**Точки входа** (какая «живая» — OPEN):
- `app.py` [CODE] Quart, WS на :8765 к Gemini, порт 5000, `debug=True`, `host=0.0.0.0`; staff-ветка без `system_prompt` (L302, L310).
- `app2.py` [CODE] Quart+uvicorn, CLI-executor, порт из `gemini_sockets.json` (5005); staff-ветка с `system_prompt` и `max_tokens=2048`.
- `app2_isolated.py` [CODE] диагностический вариант, WS-Gemini.
- `app3.py` [CODE] почти копия app2.py; `uvicorn.run("app2:app")`; импорт несуществующей модульной `get_current_project_path` (F-1, F-2).
- `start_server.py` [CODE] целится в `app:app`, 127.0.0.1:5000, `--workers 2 --reload`; падает на `ProjectContext.is_initialized()/initialize()` (F-15, F-16).
- Для «живого» входа (OPEN): [DOC] UNIVERSAL называет `app2.py` точкой входа; [CODE] лаунчер указывает на `app.py`; `app3.py` не стартует. Вывод: по статическим данным определить нельзя; возможна пометка `[RECALL: Author]`, проверяемая экспериментом (смоук-план) и манифестом E:.

**Маршрутизация и роли:** `RoleBindingManager` [CODE] — отделы A–D по 2 роли, sticky-binding md5(role) % pool, `switch_binding(reason)`, блокировки отделов с неработающим TTL (F-3, F-4), из маркеров разбирается только `[TASK]` (`[INFO]` нет), внутри отдела роли идут последовательно («Улучши результат коллеги»). `get_model_for_role`: ветка фиксированной модели недостижима из-за типа `active_models` (F-21).

**Проект и состояние:** `ProjectContext` [CODE] singleton, выбирает последний каталог в `projects/`; нет `is_initialized/initialize` (F-15). `shared_state` [CODE] файл `shared_state.json` в cwd, создаётся при импорте, flock/msvcrt (F-22). `ChatStorage` [CODE] `chats/<role>/<session>.json`, атомарная запись, `role` не санитизируется (F-23). `roles_state.json` [CODE: логика load/save; содержимое не читалось]. `models_config.json` [CODE] `active_models` — список; 8 сотрудников на одной бесплатной модели; CEO/Chief — локальные GGUF; `verification_report` 2026-04-01; `last_updated_by_samurai` (F-25). Логи ролей: `logs/subjects/{role}/{log_type}/{file}` внутри проекта [CODE: `ProjectContext.get_role_log_path`].

**Модели и промпты:** `ModelManager` [CODE] фабрика без кэша, `get_model(key)` без `require_context` (F-20, F-21). `PromptRegistry` [CODE] 21 ключ, PROJECT→GLOBAL, кэш без учёта проекта, корень `parent.parent.parent` против `ModelManager` `parent.parent`; три ключа указывают на файлы, отсутствующие в `docs/prompts` на HF. `openrouter_adapter` [CODE] retry 1/2/4 с, failover через `RoleBindingManager()` напрямую, `max_tokens=512` (F-19). `gptoss_adapter` [CODE, skim] `torch` на верхнем уровне (F-26); для phi3 `stop=['\n\n', …]`, `max_tokens=512` — **риск** преждевременного обрыва ответов с пустой строкой (F-27, не проверено).

**Транспорт Gemini:** ephemeral CLI executor [CODE] stdin→JSON, параметры mode/for_role/scope/project_path не используются, cwd не задан, `env=os.environ`, на DEBUG логирует присутствие и первые 5 символов `GEMINI_API_KEY` (F-6, F-13), ошибки возвращаются обычными строками (F-17). WS-серверы [CODE]: `legacy/gemini_mcp_server.py` — замороженный стаб; `gemini_mcp_server2.py` — deny-list + `validate_path` + `WORKSPACE_ROOT=D:\gemini\AIColab`, протокол несовместим с `{"message": prompt}` app.py. GCB [CODE]: `create_subprocess_shell` из JSON-очереди без подтверждения (F-7); `GCBEngine()` создаётся при старте всех четырёх app.

**Права и HIL:** `gateway` [CODE] интерпретатор ответа (`intercept_response`), не слой прав; `log_hil_decision` не вызывается (F-5); staff-ветка обходит gateway (F-8); `WORK_PERMIT` [отсутствует]. Тесты `test_gateway_hil.py` ссылаются на пакет `AIColab.*` и устарели (static).

**Доктор:** не менее **четырёх реализаций** [CODE]: inline в `app.py` (L488), inline в `app2_isolated.py` (L572), `core/llm_integrations/doctor_engine.py`, `doctor_ws_module.py` (→ Gemini CLI `audit_orchestrator`, где `for_role` игнорируется) + **два документных определения** [DOC×DOC]: Charter (модель, загружаемая на медосмотре) и протоколы (временный санитар, без анализа содержания, ≤10 минут).

**Web-seat/браузер:** не обнаружен в просмотренном корпусе легаси — нет playwright/selenium/webview ни в одном прочитанном .py (F-18).

**Оркестрация:** `ChiefOrchestrator` [CODE] статически неработоспособен: `ModelManager.get_instance()` (нет метода) стоит до `try`; `get_model(..., require_context=False)` (нет параметра); имена «Флик/Клик…» вместо ключей (F-20).

---

## REUSE_CANDIDATES (предварительно, пригодность не доказана)
- Идея sticky-binding «роль→модель» + явный `switch_binding(reason)` — [PROPOSAL, REWORK]; соответствует «office ≠ model» только на уровне Agent-seat.
- Иерархия PROJECT→GLOBAL для промптов + карта ролей — [PROPOSAL, REWORK] (кэш, корни).
- `ProjectContext` как «текущий проект» — [CODE с дефектами, REWORK].
- Ephemeral CLI «одно сообщение — один процесс» — идея транспорта Samurai; без изоляции/очистки env/честных ошибок — REWORK.
- `ChatStorage` (сессии по роли, атомарная запись) — единственный аналог памяти; REWORK (F-23).
- `shared_state` (межпроцессное состояние) — REWORK (F-22).

## REWORK_OR_REPLACEMENT_CANDIDATES
`RoleBindingManager` (F-3, F-4, F-21) · `ProjectContext` (F-15) · `gemini_cli_executor` (F-6, F-13, F-17) · `gateway` (нет прав) · staff-ветки · `ModelManager` (F-20, F-21) → REWORK/REPLACE · `PromptRegistry` · `shared_state` · `chat_storage` · `openrouter_adapter` (F-19) · `gptoss_adapter` (F-26, F-27). **LEGACY_ONLY — предварительное `[PROPOSAL]` разработчика, не вердикт P0 (код):** `ChiefOrchestrator` (F-20), все реализации Доктора (кроме смысла протоколов), `app.py`, `app2_isolated.py`, `app3.py`, `legacy/gemini_mcp_server.py`, `GCBEngine` без отдельного решения о безопасности.

---

## HISTORICAL_ARCHITECTURE_OPTIONS
**ACCEPTED [DOC: Program Plan §12/§14 + реплики Интегратора]:** размораживание позже; слияние старого AI-Colab и живой коллаборации; управляются офисы, а не модели (OFFICE ≠ OCCUPANT ≠ DYNASTY ≠ WORKSPACE); persistent web-чаты — кандидаты-occupants; Secretary/postman → внутренняя шина маршрутизации; OpenRouter-персонал — Agent seats; Samurai — локальный исполнитель; dynasty/наследование — архитектурные понятия; финальная власть у Автора; ограничения: не делать browser-automation фундаментом, graceful degradation (видимый ручной fallback, без выдуманного успеха), provenance, web-память ≠ институциональная; Samurai Repository/File Guide (детерминированный показ + семантический Gemini-Секретарь, provenance-шапка, read-only, white-list, исключение секретов); разделение Endpoint Adapter (технический доступ без смыслового видения) и Secretary (смысловое видение метаданных без доступа к BODY) — RETAIN.

**EXPERIMENTALLY_SUPPORTED:** пусто. Только ручная практика коллаборации и статическое чтение внешних репозиториев. ctxport [EXT]: внутренние API платформ (same-origin fetch с cookies), не DOM — поправка к прежнему «DOM parsers → ADAPTABLE» принята обеими сторонами. Endpoint Spike v3.1: SPEC VALID/REUSABLE, не исполнялся.

**PROPOSED [DOC: дискуссии Secretary_*]:** PULL/mailbox внутри + PUSH на границе; конверт (message_id, parent_id, task_id, from, to, triad, timestamp, status, body_ref, reply_to); прогрессивное раскрытие L0–L3; SQLite (метаданные) + файловая система (BODY); Playwright + CDP-attach как ведущий кандидат endpoint; Temporal/Inngest/Restate, OPA, A2A, React Flow, MCP/SLIM — гипотезы, понижены Методологом; прототипный FastAPI/SQLAlchemy-каркас Secretary/Courier/Audit от DeepSeek — иллюстрация, не принят; Spike v3.1: A-API параллельно A-DOM, self-report per-call через API; Program Plan §4.3: Electron/CEF/PySide-QWebEngine/внешний Chromium-профиль — список кандидатов, выбор не сделан.

**SUPERSEDED:** Secretary как «почтальон по браузерам» как фундамент (Program Plan §7); «Playwright — единственный путь» (снято Методологом); тема Claude Desktop как endpoint (закрыта); преждевременный выбор стека (возвращён в Mapping); Secretary как отдельная «постоянно думающая» модель — RE-EVALUATE.

**OPEN:** хост web-seats; встраиваемость всех провайдеров; безопасное хранение сессий и учётных данных; число профилей; формат конверта/протокола; уровень автоматизации и автовставка; взаимозаменяемость API и web-seat; восстановление сессий; локально vs сервер; таксономия ролей; формат dynasty-файла; модель безопасности; существует ли готовый control room с организационным графом («в разведке не обнаружено»).

---

## LEGACY_TO_TARGET_MAPPING
| Цель AI-Colab 2 | Факт в легаси | Вердикт |
|---|---|---|
| Роли и модельный персонал | `RoleBindingManager` (Agent-seat), `ChatStorage`, `*_history.jsonl` | частичное покрытие; office/occupant/dynasty — NEW |
| Маршрутизация/коммуникация | цепочка ролей в отделе, `[TASK]`; gateway интерпретирует ответ | NEW (конверта нет) |
| Web-seat/workspace | не обнаружен в просмотренном корпусе (F-18) | NEW; главный неопределённый узел |
| Сохранение состояния | `roles_state.json`, `logs/subjects/…`, `ChatStorage` | ничтожное покрытие институциональной памяти; NEW |
| Контроль разрешений | не обнаружен (F-5, F-8) | NEW |
| Gemini CLI / Samurai | ephemeral executor, WS-стабы, GCB | транспорт — идея; безопасность — REWORK; Repository Guide — NEW |
| Файловое обслуживание участников | только `validate_path` в `gemini_mcp_server2.py` | NEW |
| Восстановление после отказов | ошибки маскируются (F-17), блокировки не снимаются (F-3/F-4) | NEW (антипаттерны не переносить) |

**Смысловая преемственность [DOC]** (основной вклад старого проекта):
- Charter §12 «Gemini — умные руки, не собеседник» → Samurai как исполнитель.
- «Logs primary over dialogues», «фиксация следа» → институциональная память.
- «Modes ≠ chats ≠ agents» → «office ≠ occupant».
- Протоколы Доктора (границы, формальная диагностика, лестница вмешательств) → материал для будущих конституций офисов; статус OBSOLETE/REUSABLE решает Автор.
- **Дрейф смысла [DOC×DOC]:** «Доктор — временный санитар» (старые протоколы) против «Доктор — постоянная династия» (Program Plan). Одно имя — разные профессии («same occupant ≠ automatic continuity of authority»). Charter «пара — единица, 3+ — шум» против современных триад — вопрос Хранителю, не разработчикам.

---

## DESIGN_ALTERNATIVES (без выбора стека)
**Ось 1. Транспорт Gemini.** Варианты: ephemeral CLI «как есть»; + изоляция (cwd/allow-list/очистка env); WS-протокол; GCB-очередь. Плюсы/минусы: простота против отсутствия изоляции (F-6, F-13, F-17); WS — конфиг сокетов есть, протокол несовместим; GCB — shell без allow-list, без отдельного решения о безопасности не кандидат. Зависимости: допустимость ephemeral CLI как транспорта (решение Автора). Нужны свидетельства: умеет ли Gemini CLI ограничить корень/режим.

**Ось 2. Слой прав.** gateway-as-permit; отдельный control plane; middleware перед staff-веткой. Зависит от границы «интерпретатор ≠ permit» (Хранитель). Нужно: подтверждение отсутствия скрытого слоя прав (grep по всем маршрутам).

**Ось 3. Repository/File Guide.** Встроен в Samurai-исполнитель / отдельный сервис / часть Gemini CLI. Зависит от того, какой процесс держит «окно в файлы»; нужно подтвердить возможность read-only whitelist. Детерминированный слой не зависит от LLM; семантический читает только через него.

**Ось 4. Хост web-seats.** (a) внешние профили Chromium + CDP-attach; (b) встроенный shell (Electron/CEF/QtWebEngine); (c) гибрид. (a) ближе к текущей практике и сохраняет логины, но зависит от внешних процессов/anti-bot; (b) единое окно, риск отказов провайдеров во встроенных браузерах; (c) ближе к деградации §14.6. Нужен эксперимент (Phase 1 плана) — не выполнялся.

**Ось 5. Модель доставки.** PULL (mailbox, ручное/полуавтоматическое пробуждение) / PUSH (вставка в чат) / гибрид. PULL откладывает сложность Courier и даёт видимый fallback; PUSH требует решения identity, окончания генерации, дублирования. Нужны Spike A/B/B1/C и шаг 0 API-проверки.

**Ось 6. Чтение/запись endpoint.** Чтение: внутренние API [EXT-образец] / DOM / ручной экспорт; запись: DOM-вставка / API / ручная вставка. API стабильнее по структуре, но недокументирован и ближе к нарушению условий платформ; DOM хрупок. Выбор — фаза Architecture. Зависит от ToS-оценки (в спайк не входит).

**Ось 7. Состояние.** Файлы + SQLite (минимум) против durable-engine; зависит от того, нужны ли таймеры/реплей на первом этапе.

Можно решить по имеющимся свидетельствам (кандидаты на решение триады): PULL внутри/PUSH на границе как рабочая гипотеза; read-only whitelist для Guide; конверт и институциональное состояние отдельно от transcript; не переносить антипаттерны F-3/F-4/F-17. Нужен эксперимент: хост web-seats; endpoint чтение/запись; границы Gemini CLI.

---

## DEVELOPER_DISAGREEMENTS (итог)
Снято: ctxport (DOM→внутренние API); `[INFO]`-парсинг; `ModelManager`/`ChiefOrchestrator` как reuse; «system_prompt теряется везде» (только app.py).
OPEN: живой вход (проверка экспериментом). Roadmap/Readme прочитаны; их закрытые решения учтены в Web-Seat плане §2.2.
Расхождения документов и кода: Adapter «не знает про роли» (UNIVERSAL) vs код (хранит `role_key`, зовёт RoleBindingManager); «prompt_registry читает project/prompts/{role}.txt» vs реальный `role_map` с подпапками; Gemini «вне чата» vs `call_gemini` в `/api/secretary` и Doctor-WS; цикл A⇒B⇒C⇒A… Charter vs единственная последовательность из двух ролей в отделе (межотдельный цикл в прочитанных файлах не найден — мог остаться в непрочитанных pce/cse/obe/UI).

## QUESTIONS_TO_KEEPER
*(v1.2: **не отправляются** по решению Интегратора; сохранены как внутренний список. Инженерные вопросы остаются у разработчиков.)*
1) Достаточна ли граница «entry points → gateway → executor ↔ Gemini CLI» для проверки прав или нужна отдельная сущность WORK_PERMIT; как фиксировать различие «интерпретатор ответа» и «слой прав»? 2) Из «не менее четырёх реализаций Доктора + двух документных определений» какая онтологически необходима, какие — исторические опыты? 3) Допустим ли ephemeral CLI как транспорт при изоляции, или нужен единый протокол? 4) `ChatStorage` + `*_history.jsonl` — институциональная память или транскрипт, где граница? 5) Дрейф «временный санитар» → «постоянная династия»: как фиксировать, что одно имя ≠ одна профессия? 6) Пара как единица (Charter) против триады (современная практика).

## QUESTIONS_FOR_AUTHOR
*(Пункты о последнем запуске, `requirements.txt` и загрузке Roadmap/Readme сняты.)*
1. Допустим ли для endpoint путь через внутренние API платформ (ToS-риск) или только DOM/ручной экспорт? — **задавать после** получения данных WS-2/WS-3 (Web-Seat план §11), не раньше.
2. Нужны ли на первом этапе replay/таймеры (определяет необходимость durable-engine)?
3. Статус протоколов Доктора для будущих конституций офисов: OBSOLETE/REUSABLE?
4. Для запуска любой ступени экспериментов — решения P-A…P-C Web-Seat плана §2.4 и отдельное разрешение на каждую ступень.

## PROPOSED_NEXT_PHASE
STOP → Chief Integrator. Два независимых плана экспериментов (PROPOSED / NOT_EXECUTED): `DEEPSEEK_LEGACY_SMOKE_TEST_PLAN` и `CLAUDE_WEB_SEAT_FEASIBILITY_PLAN`; перекрёстные замечания оформлены отдельно. Запуск любого — только по отдельному разрешению Автора. Блокер исполняемых экспериментов над легаси: фиксация ревизии HF + манифест E:. Хранитель — не привлекается сейчас; UI/движки — только по конкретному пробелу.

---

## ПРИЛОЖЕНИЕ. РЕЕСТР НАХОДОК (все — статические, RUNTIME_UNVERIFIED)
| № | Находка | Где |
|---|---|---|
| F-1 | `app3.py` импортирует модульную `get_current_project_path`, а это метод класса → ImportError | app3.py L22; project_context.py L48 |
| F-2 | `app3.py` запускает `"app2:app"` | app3.py |
| F-3 | `run_department`: `self.unlock_department(dept)` без `await` (async) → отдел остаётся занятым | role_binding_manager.py L322, L305 |
| F-4 | TTL блокировки (`LOCK_TTL_SECONDS=120`) записывается, не проверяется | там же L19, L295–303, L289 |
| F-5 | `log_hil_decision` не вызывается | core/gateway.py |
| F-6 | `execute()` не использует mode/for_role/scope/project_path; cwd не задан | gemini_cli_executor.py |
| F-7 | `execute_local` → `create_subprocess_shell` из очереди без подтверждения | gcb_engine.py L73–104 |
| F-8 | staff-ветка возвращает ответ до `gateway.intercept_response` | app.py, app2.py |
| F-9 | `apply_mode_logic` просто добавляет «\nВеди диалог.» | core/mode_handler.py |
| F-10 | Пути `D:\Gemini\AIColab` (код/конфиг) против `E:\Gemini\AI-Colab\` (цель) | gemini_mcp_server2.py, gcb_engine.py, models_config.json |
| F-11 | `app.py`: `debug=True`, `host=0.0.0.0` | app.py |
| F-12 | (не дефект) способ чтения role_binding_manager: сборка из двух чтений | — |
| F-13 | DEBUG-лог пишет присутствие и первые 5 символов GEMINI_API_KEY | gemini_cli_executor.py L66–67 |
| F-14 | не назначен | — |
| F-15 | `start_server.py` зовёт `ProjectContext.is_initialized()/initialize()` — их нет → AttributeError | start_server.py L56, L65 |
| F-16 | лаунчер целится в `app:app`, порт 5000, `--workers 2 --reload`; убивает python-процессы на порту | start_server.py |
| F-17 | `execute()` возвращает ошибки/таймауты обычными строками | gemini_cli_executor.py |
| F-18 | browser-automation/web-seat **не обнаружены** в просмотренном корпусе легаси | grep по прочитанным .py |
| F-19 | адаптеры создают `RoleBindingManager()` напрямую (много экземпляров); циклический импорт | openrouter_adapter.py, chief_orchestrator.py |
| F-20 | `ChiefOrchestrator` статически неработоспособен (`get_instance`, `require_context`) | chief_orchestrator.py |
| F-21 | `active_models` — список в конфиге, словарь в `get_model_for_role` → ветка недостижима | role_binding_manager.py L278–280; models_config.json |
| F-22 | `shared_state` создаётся при импорте, файл в cwd | shared_state.py |
| F-23 | `ChatStorage`: `role` не санитизируется; read-modify-write без блокировки | chat_storage.py |
| F-24 | `DoctorEngine`: `generate` без system_prompt; HR-ротация только логирует; пути `D:/…` | doctor_engine.py |
| F-25 | 8 сотрудников на одной бесплатной модели; free-модели в статусе «limit» (отчёт 2026-04-01) | models_config.json |
| F-26 | `GptOssModel` импортирует `torch` на верхнем уровне | gptoss_adapter.py |
| F-27 | **риск (не проверен в runtime):** для phi3 (Chief) `stop=['<|end|>','<|user|>','\n\n']` и `max_tokens=512` → возможен преждевременный обрыв многоабзацного ответа и усечение | gptoss_adapter.py L100–110 |
