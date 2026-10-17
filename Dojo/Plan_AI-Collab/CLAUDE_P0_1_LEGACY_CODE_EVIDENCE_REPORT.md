# CLAUDE_P0_1_LEGACY_CODE_EVIDENCE_REPORT

Роль: Source Evidence Provider (P0.1). Источник: HF dataset `lhc-lab/AI-Colab`, чтение через Hugging Face MCP (`hf_fs ls/cat/stat`).
Уровень: **DOCUMENT_READ / CODE_READ / STATIC_ANALYZED. Ничего не запускалось. RUNTIME_VERIFIED нет ни по одному пункту.**
Общее ограничение: **REVISION = UNKNOWN** (hf_fs не отдаёт commit hash). Целостность каждого файла подтверждена только парой «размер == stat» + SHA-256 полученного текста. Это снимок «как отдал HF в момент чтения», не привязка к ревизии.

Ничего нового не проектируется. Секретов, ключей, cookies, .env в пакете нет (значения не копировались; см. F-13 — упоминание факта логирования префикса ключа без значения).

---

## 1. Файлы, фактически прочитанные (паспорта)

Общие поля всех паспортов: REPOSITORY `lhc-lab/AI-Colab`; SOURCE `HF_DATASET`; REVISION `UNKNOWN`; MODE `VERBATIM` (прочитано целиком, TRUNCATED `false`, если не указано иное). SHA-256 — первые 16 символов (полные значения хранятся в рабочей папке и будут выданы по запросу).

| # | FILE | BYTES | LINES | SHA-256 (16) | LEVEL |
|---|------|------:|------:|--------------|-------|
| 1 | app.py | 30238 | 646 | 81a2e0342eba7bbb | STATIC_ANALYZED |
| 2 | app2.py | 36054 | 758 | 8210783b32986e80 | STATIC_ANALYZED |
| 3 | app2_isolated.py | 33777 | 699 | d0fa29b203b79ad0 | STATIC_ANALYZED |
| 4 | app3.py | 36063 | 757 | 659977fe9847bc81 | STATIC_ANALYZED |
| 5 | docs/architecture/ARCHITECTURE_MAP.md | 33693 | 626 | 8e689c53edb5dacc | DOCUMENT_READ |
| 5b | ARCHITECTURE_MAP.md (корень) | см. прим. | — | не зафиксирован отдельно | DOCUMENT_READ |
| 6 | core/gateway.py | 5483 | 129 | 361f2e98dc48c319 | CODE_READ |
| 7 | tests/test_gateway_hil.py | 15308 | 293 | 2af9e3f1eeaa9a30 | CODE_READ |
| 8 | core/gemini_cli_executor.py | 4495 | 126 | 1a6b22944231dea6 | CODE_READ |
| 9 | core/llm_integrations/gcb_engine.py | 4325 | 104 | f2476a80ae017f6f | CODE_READ |
| 10 | gemini_mcp_server2.py | 10227 | 287 | 06042ca38a6bfefa | CODE_READ |
| 11 | legacy/gemini_mcp_server.py | 3565 | 109 | 1c1206b29c1bddc2 | CODE_READ |
| 12 | core/role_binding_manager.py | 13623 | 358 | 6df2e425887a1a17 | STATIC_ANALYZED |
| 13 | core/project_context.py | 3900 | 95 | 67b8269c141e23cf | CODE_READ |
| 14 | core/mode_handler.py | 325 | 9 | 22752ec6abed5920 | CODE_READ |
| 15 | core/config_loader.py | 1412 | 40 | f0719f2dc4bd15d5 | CODE_READ |
| 16 | config/gemini_sockets.json | 777 | 33 | f72874ca6d3f6d92 | CODE_READ |
| 17 | doctor_ws_module.py | 8982 | 236 | 390bdcdcc1d92691 | CODE_READ |

Примечания к паспортам:
- Строка 5b: корневой MAP читался (≈19.4 КБ), но отдельный хэш не сохранён; рабочий файл `src/ARCHITECTURE_MAP.md` (53107 B) — объединённая копия, её хэш **не является** паспортом ни одного репозиторного файла. Для сверки с E: использовать только файл №5, корневой MAP — перечитать при необходимости.
- Файлы №1–4: `claim_supported` = импорты, маршруты, запуск, различия между вариантами (по AST и чтению). `claims_not_verified` = любое поведение при запуске, работоспособность импортов, наличие зависимостей.
- №12: первоначально читался частями (truncated при первом чтении, затем перечитан целиком, size == stat).
- Список содержимого репозитория (TREE-уровень, не VERBATIM): корень также содержит app_echo.py, start_server.py, ws_minimal.py, scripts/run_uvicorn_*.py, множество verify_*/test_* скриптов, `.bak`/`.diag_bak`, `legacy/`, `debug_ws/`, скелет `projects/Bestihi.ru`; `core/` содержит adapters/, llm_integrations/, session/ (папок dal/fsm/eventbus нет).

CLAIMS_NOT_VERIFIED (общие): какой файл реально запускается на E:; идентичность HF и E:; работоспособность любого пути; наличие/версии зависимостей (requirements.txt не читался); содержимое файлов, не перечисленных выше.

---

## 2. Сравнение четырёх точек входа (static)

| Признак | app.py | app2_isolated.py | app2.py | app3.py |
|---|---|---|---|---|
| Тип | Quart-приложение (`app.run`) | Quart + uvicorn, диагностический вариант | Quart + uvicorn | почти копия app2.py |
| Запуск | `app.run(debug=True, host='0.0.0.0', port=5000)` | uvicorn | `uvicorn.run("app2:app", host, port)`; хост/порт из `load_gemini_sockets()["main_server"]` (по умолчанию 127.0.0.1:5005) | `uvicorn.run("app2:app", …)` — **строка ссылается на app2, не app3** |
| Вызов Gemini | WebSocket `ws://127.0.0.1:8765`, `{"message": prompt}` | WebSocket (диагностика) | `core.gemini_cli_executor.execute(mode="console", …, for_role, project_path)` | то же |
| Gateway | `gateway.intercept_response` только в ветке не-staff | аналогично | аналогично (вызов L543, staff-ветка L415–494 возвращает раньше) | аналогично |
| Защита от сбоев | — | — | весь модуль внутри `try/except`, пишет `app2_critical_error.log` | то же |
| Особенность | первое поколение | отдельный вариант | поколение CLI-executor | **импорт `from core.project_context import ProjectContext, get_current_project_path` (L22)** |

Вывод (static): линия app.py → app2_isolated.py (WS-Gemini) и линия app2.py → app3.py (CLI-executor). Какая из них «живая» — **неизвестно** (нужен запуск/E:).

---

## 3. Первичная карта маршрутизации / HIL

Реально прочитанная цепочка (статически):
1. Вход: HTTP `/api/secretary` и связанные маршруты (UI/WS/API — перечень маршрутов извлечён AST, см. рабочие файлы).
2. Staff-ветка: обрабатывается и возвращает ответ **до** `gateway.intercept_response`.
3. Не-staff: `call_gemini` → ответ → `gateway.intercept_response`.
4. `core/gateway.py` — **интерпретатор ответа** (`intercept_response`, `_strip_markdown`), а не проверка прав. Нет проверки разрешения до исполнения, нет WORK_PERMIT, нет подтверждения результата. `log_hil_decision` определена, **ни разу не вызывается**. Собственный `call_gemini` закомментирован.
5. HIL — это UI-кнопка плюс не подключённый логгер. Модели ролей: `RoleBindingManager` (отделы A–D по две роли, sticky-binding через md5(role) % pool, блокировки отделов).

Границы «команда → проверка прав → маршрутизация → исполнение → подтверждение результата»: из этих пяти звеньев в коде есть **маршрутизация** (роль→модель) и **исполнение**; **проверки прав как отдельного слоя и подтверждения результата не обнаружено** (в прочитанных файлах).
`tests/test_gateway_hil.py` импортирует `from app import app` и `AIColab.core.gateway` (пакет `AIColab` в прочитанном дереве не найден), патчит `AIColab.core.gateway.call_gemini` (в gateway он закомментирован), ожидает `reason_code == 'unspecified'` — тесты, вероятно, **устарели** (STATIC; не запускались).

---

## 4. Карта связей с Gemini CLI

| Путь | Файл | Что реально делает | Статус (static) |
|---|---|---|---|
| Ephemeral CLI | core/gemini_cli_executor.py | `execute(mode, message, project_path, prompt_text, timeout=30, for_role, scope)`; команда `[bin_path, "-o", "json"]`, сообщение через stdin (`communicate`), `env=os.environ` | Текущий путь для app2/app3. **mode, for_role, scope, project_path в команду не попадают** (параметры неиспользуемые) |
| WS «MCP» (legacy) | legacy/gemini_mcp_server.py | помечен «LEGACY: Frozen in SPEC_2026-04-13»; отвечает заглушкой `{"type":"response","data":"ACK","prompt_applied":True}` | замороженный стаб |
| WS-сервер с директивами | gemini_mcp_server2.py | `WORKSPACE_ROOT = D:\gemini\AIColab`; регекс-deny-list `FORBIDDEN_COMMANDS`; `ActionType` {shell, file_edit, file_read, code_analysis, search}; обрабатывает только сообщения с `"directive"`; есть `SecurityLayer.validate_path` | протокол несовместим с `{"message": prompt}` из app.py |
| GCB-очередь | core/llm_integrations/gcb_engine.py | `GCBEngine(queue_path="D:\\Gemini\\AIColab\\sessions\\gcb_queue.json")`; `execute_local` → `asyncio.create_subprocess_shell(command)` **без одобрения и allow-list** | не готовая основа; вызывающие `enqueue` не прочитаны |
| Doctor | doctor_ws_module.py | `register_doctor_ws(app)`, `DoctorState`, `DoctorEngine.process` → `execute(mode="console", for_role="audit_orchestrator")` | использует CLI-executor |
| Сокеты | config/gemini_sockets.json | агенты 5001–5004, 5006 + main_server 5005 | противоречит «ephemeral CLI» (конфиг сокетов vs CLI без сокетов) |

Что нужно будущему Samurai Repository/File Guide (только как требования к источникам, не как дизайн):
- Нужна детерминированная read-only оболочка (дерево/файл/строки/дифф) — в прочитанном коде **её нет**; ближайший по смыслу фрагмент — `SecurityLayer.validate_path` в gemini_mcp_server2.py (path whitelist относительно WORKSPACE_ROOT), но этот сервер запускается отдельно и протокольно несовместим с основным приложением.
- `gemini_cli_executor.execute` умеет только «сообщение на stdin → JSON»; передачи файлов/ограничений каталога/режима чтения нет.
- GCB как основа **не пригоден без подтверждения** (shell без охраны); не считаем готовой базой.

---

## 5. Расхождения «документация ↔ код»

- ARCHITECTURE_MAP (v1.0, 2026-03-15) описывает DAL / FSM / EventBus / InfoBuilder и FastAPI `server/app.py`. В прочитанном дереве папок dal/fsm/eventbus **нет**; приложения — Quart; FastAPI не обнаружен. (static; «нет» означает «не найдено в TREE HF», не «не было на E:».)
- Документ внутренне противоречив: «5 сокетов Gemini» vs «ephemeral CLI».
- Документированные `validate_path`/HTML-санитизация: в app*.py/gateway/role_binding **не найдены**; `validate_path` есть только в gemini_mcp_server2.py.
- Тесты и документация ссылаются на пакет `AIColab.*`, в коде импорты вида `core.*`.

---

## 6. Статические находки по коду (все RUNTIME_UNVERIFIED)

- F-1. `core/project_context.py`: `get_current_project_path` — **метод класса** (L48), на уровне модуля функции нет. `app3.py` L22 импортирует её как имя модуля → при запуске ожидается ImportError (внутри `try/except` → запись в `app2_critical_error.log`). Подтверждено grep.
- F-2. `app3.py` запускает `"app2:app"` — не себя.
- F-3. `role_binding_manager.run_department`: в `finally` вызывается `self.unlock_department(dept)` **без await**, а метод `async` → корутина не исполняется, отдел остаётся заблокированным (`busy_by_system`).
- F-4. `LOCK_TTL_SECONDS = 120`: `expires` записывается, но **нигде не проверяется** (grep: только запись) → TTL не работает; вместе с F-3 даёт постоянную блокировку отдела до перезапуска.
- F-5. `log_hil_decision` не вызывается.
- F-6. `execute()` игнорирует mode/for_role/scope/project_path → «ролевая изоляция» на уровне CLI отсутствует.
- F-7. `GCBEngine.execute_local` — shell без allow-list.
- F-8. Staff-ветка обходит gateway.
- F-9. `apply_mode_logic` просто дописывает `"\nВеди диалог."` (core/mode_handler.py), используется в app*.py внутри функций.
- F-10. Пути D:\Gemini\AIColab (WS-сервер, GCB) vs предполагаемый E:\Gemini\AI-Colab — несоответствие, нужна сверка.
- F-11. `debug=True, host='0.0.0.0'` в app.py.
- F-12. Конфликт имён: файл `core/role_binding_manager.py` и каталог `core/` в разных частях читались раздельно; финальная версия №12 собрана из двух чтений (13623 B == stat).
- F-13. `gemini_cli_executor` на DEBUG логирует факт наличия и первые 5 символов GEMINI_API_KEY — это утечка префикса секрета в логи (значения в отчёт не включены). Для Samurai-интеграции учесть как риск.

---

## 7. Запросы для сверки HF ↔ E:\Gemini\AI-Colab\ (read-only)

Маршрут: Автор → Grok → DeepSeek-бригадир → Доктор → Самурай. Мы Самураю напрямую не пишем.

**SOURCE_REQUEST (для передачи по цепочке; только чтение, ничего не запускать, ничего не менять):**
```
SOURCE_REQUEST: E_MANIFEST_READONLY
SCOPE: E:\Gemini\AI-Colab\ (рекурсивно), исключая: .git, __pycache__, *.pyc, .env*, любые файлы с ключами/токенами/cookies, projects\*\ (содержимое пользовательских проектов)
OUTPUT: таблица (относительный путь с '/', размер в байтах, SHA-256 содержимого, дата изменения UTC)
ПРИМЕЧАНИЕ: считать SHA-256 по сырым байтам. Дополнительно колонка SHA-256 после нормализации CRLF→LF (для текстовых файлов .py .md .json .txt), чтобы отличить реальные изменения от различий окончаний строк.
ПЕРВООЧЕРЕДНЫЕ ФАЙЛЫ (отдать хэши даже если остальное не готово): app.py, app2.py, app2_isolated.py, app3.py, start_server.py, core/gateway.py, core/gemini_cli_executor.py, core/project_context.py, core/role_binding_manager.py, core/llm_integrations/gcb_engine.py, gemini_mcp_server2.py, legacy/gemini_mcp_server.py, doctor_ws_module.py, config/gemini_sockets.json, tests/test_gateway_hil.py, docs/architecture/ARCHITECTURE_MAP.md, requirements.txt
ЗАПРЕЩЕНО: открывать/копировать содержимое .env, ключей, токенов, cookies; запускать код.
ДОПОЛНИТЕЛЬНО (одной строкой от Доктора): git commit hash, если E:\Gemini\AI-Colab — git-репозиторий; какой из app*.py запускался последним (по логам/ярлыку/start-скрипту) — только фактом, без запуска.
```
Классификация результата на нашей стороне: IDENTICAL (сырой или нормализованный хэш совпал) / MODIFIED / MISSING_ON_E / ADDED_ON_E / UNKNOWN.
Эталон HF-манифеста: таблица пунктов 1 выше (хэши полные могу выдать по запросу).

---

## 8. Вопросы к DeepSeek (конкретные)

1. Пришли `DEVELOPER_DEEPSEEK_P0_TECHNICAL_RECONSTRUCTION_FRAME` — сверим твою рамку с пунктами 3–6.
2. Какой из app.py / app2.py / app3.py ты считаешь «живым» и на основании чего (источник, не память)? Мы по статике склоняемся к линии app2.py, но F-1/F-2 говорят, что app3.py, скорее всего, не стартует.
3. Какие из F-1…F-8 тебе нужны подтвердить рантаймом (отдельное разрешение Автора) — расставь приоритет.
4. Какие SOURCE_REQUEST к файлам, которых мы не читали (см. п. 9), ты считаешь P0 для Samurai Repository/File Guide?
5. Согласен ли ты, что gateway — не слой прав, и формулировка «WORK_PERMIT в легаси» не подтверждается?
6. Есть ли у тебя сведения о существовании пакета `AIColab` (на который ссылаются тесты) вне HF-снимка?

---

## 9. Неизвестное и блокеры

Не прочитано: core/chief_orchestrator.py, core/llm_integrations/doctor_engine.py, model_management, chat_storage, shared_state, prompt_registry (импортируются role_binding_manager, но не читались), вызывающие GCB `enqueue`, static/chat.js, templates/index.html, requirements.txt, start_server.py, остальные verify_*/test_*.
Блокеры: (1) commit hash HF неизвестен; (2) нет E:-манифеста; (3) нет рантайм-подтверждения чего-либо; (4) shell сессии не достаёт до huggingface.co (чтение только через MCP).

## 10. Для Хранителя (адресная карта, без кода)

Сущности: entry points (4) → gateway (интерпретатор ответа) → executor (stdin→JSON) ↔ Gemini CLI; RoleBindingManager (отделы A–D, блокировки, sticky-binding); Doctor (FSM по WS); GCB (очередь+shell); legacy WS-серверы (2). Права: отдельного слоя не найдено; HIL — UI + неподключённый логгер; фильтры: deny-list в gemini_mcp_server2, validate_path только там.

---
STOP / HANDOFF TO DEVELOPER DEEPSEEK
