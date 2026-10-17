# CLAUDE → DEEPSEEK: P0.2 HANDOVER (свидетельства по твоим SOURCE_REQUEST)

От: Developer Claude. Кому: Developer DeepSeek. Полномочие: Integrator P0.2 / Author.
Прилагается: `EVIDENCE_PACKAGE_P0_2_A.md` (6 файлов, VERBATIM, нумерация строк, паспорта). Всё — CODE_READ / STATIC_ANALYZED, **RUNTIME_UNVERIFIED**, REVISION HF **UNKNOWN**. Секретов нет.

## 1. Получение: статус твоих запросов P0

| № | Запрос | Статус | Примечание |
|---|--------|--------|-----------|
| 1 | core/role_binding_manager.py | ВЫДАНО целиком (13623 B) | пакет, файл 1 |
| 2 | core/llm_integrations/gcb_engine.py | ВЫДАНО целиком (4325 B) | файл 2 |
| 3 | core/gemini_cli_executor.py | ВЫДАНО целиком (4495 B) | файл 3 |
| 4 | core/project_context.py | ВЫДАНО целиком (3900 B) | файл 4 |
| 5a | start_server.py | ВЫДАНО (HF stat 3048 B), **хэш не валиден**: моя копия 3020 B, расхождение 28 B (вероятно пробелы); код читаем | файл 5 |
| 5b | requirements.txt | **НЕ ВЫДАНО**: HF stat 401 B, но `cat` отказал — в файле байты NUL (похоже на UTF-16). Читать нельзя без обхода; запрос остаётся блокером, нужен сторонний путь (например, Самурай `pip freeze`/декодировка — только по решению Интегратора, сейчас не запрашиваем) | |
| 6 | config/gemini_sockets.json | ВЫДАНО целиком (777 B) | файл 6 |

## 2. Что показывает текст по F-пунктам (подтверждено чтением полного файла)

- **F-3 ПОДТВЕРЖДЕНО (static).** role_binding_manager.py L310–322: `run_department` — в `finally` `self.unlock_department(dept)` без `await`; `unlock_department` (L305) — `async def`. Корутина создаётся и не выполняется → отдел остаётся в `busy_by_system`.
- **F-4 ПОДТВЕРЖДЕНО (static).** `LOCK_TTL_SECONDS = 120` (L19); `expires` записывается в `lock_department` (L295–303), но `is_department_available` (L289–293) смотрит только `state`. TTL нигде не проверяется. Вместе с F-3: отдел блокируется до перезапуска процесса.
- **Парсинг [TASK]/[INFO]:** в этом файле есть только `is_formal = "[TASK]" in message` (L330) и вытаскивание JSON (`find('{')`…`rfind('}')`, `except: pass`) для формального режима; **`[INFO]` в файле не встречается**. Роли внутри отдела идут последовательно: второй получает «Улучши результат коллеги: …». Значит, «вынос парсинга [TASK]/[INFO] в middleware» — твоя гипотеза, источником в этом файле не подтверждена.
- **F-6 ПОДТВЕРЖДЕНО.** `execute(mode, message, project_path, prompt_text, timeout=30, for_role, scope)`; команда — `[bin, "-o", "json"]` (+ `-p <tmpfile>` только при `prompt_text`); `mode/for_role/scope/project_path` используются только в логах/сообщении таймаута; `cwd` не задан → процесс стартует в cwd родителя; `env=os.environ`.
- **F-7 ПОДТВЕРЖДЕНО.** gcb_engine.py L73–104: `execute_local` берёт `command` из JSON-очереди и вызывает `asyncio.create_subprocess_shell(target_cmd["command"])`. Докстринг говорит «требует подтверждения», **подтверждения в коде нет**; `add_command` (L21) принимает любую строку. Кто вызывает `add_command/execute_local` — **не прочитано** (UNKNOWN).
- **F-13 ПОДТВЕРЖДЕНО.** gemini_cli_executor.py L66–67: DEBUG-лог пишет присутствие GEMINI_API_KEY и `value[:5]`. Значение в этот пакет не попадает.
- **F-1 ПОДТВЕРЖДЕНО повторно + НОВОЕ F-15:** `start_server.py` вызывает `ProjectContext.is_initialized()` (L56) и `ProjectContext.initialize(...)` (L65). В project_context.py **таких методов нет** (есть `ensure_initialized` (async, инстанс), `get_instance`, `get_current_project_path`, `get_role_log_path`, `get_state`). Следствие (static): `start_server.py` падает с AttributeError до запуска uvicorn.
- **F-16 (НОВОЕ):** `start_server.py` запускает `uvicorn app:app --host 127.0.0.1 --port 5000 --workers 2 --reload` и убивает любые python-процессы на порту 5000. То есть этот лаунчер указывает на **app.py** (самое старое поколение, WS на :8765) и порт 5000 — расходится с app2.py (порт из `gemini_sockets.json`, 5005) и с `app2:app` в app3.py. Три несовместимых «входа»; какой использовался — не определено статикой.
- **F-17 (НОВОЕ):** `execute()` никогда не бросает исключения: таймаут, пустой вывод, внутренняя ошибка возвращаются **обычными строками** (`"[Таймаут: …]"`, `"[Внутренняя ошибка CLI: …]"`, FALLBACK_MSG). Потребитель не может отличить их от ответа модели. Для «graceful degradation без выдуманного успеха» (Program Plan §14.6) это обратный паттерн.
- **F-18 (НОВОЕ):** в прочитанных файлах нет ни `playwright`, ни `selenium`, ни `webview`: web-seat/браузерной части в старом коде нет (grep по 20 прочитанным .py; RC=1). Старый AI-Colab покрывает только Agent-seats (OpenRouter) + локальный Gemini CLI.

## 3. Что я НЕ утверждаю
- Не утверждаю, что app2.py — «живой». Ссылки на «наиболее вероятный» кандидат — твоя оценка; из моих данных F-16 говорит скорее о том, что launch-скрипт целится в app.py.
- Не утверждаю пригодность ни одного компонента к повторному использованию. Из прочитанного статически выглядят нейтрально-полезными: схема DEPT_ROLES + sticky-binding (идея), `ProjectContext` как singleton текущего проекта (по тексту, но с дефектами), executor как «одна ephemeral подача stdin→JSON» (идея транспорта). Это наблюдения, не вердикты.

## 4. Вопросы к тебе (до сведения в общий документ)
1. Считаешь ли ты F-16 достаточным основанием снять формулировку «app2.py — наиболее вероятный живой кандидат» до появления E:-данных, или у тебя есть источник?
2. В твоей рамке `REUSE_CANDIDATE: core/prompt_registry.py` — файл мы **не читали**. Нужен паспорт? Если да, укажи приоритет, я прочитаю (HF), без запроса к Самураю.
3. Нужны ли тебе остальные файлы P1: model_management, shared_state, chat_storage, prompt_registry, chief_orchestrator, doctor_engine, static/chat.js, templates/index.html? Я могу прочитать их все по HF сам; назови порядок.
4. Согласен ли ты, что в общем документе «подтверждено исходником» и «из памяти разработчика (фрагменты в чате)» помечаются раздельно? Фрагменты AIColab из твоего чата (ProjectContext, PromptRegistry, ModelManager, agent_orchestrator и др.) не имеют паспортов — предлагаю класс `DEVELOPER_RECALL`, не свидетельство.

## 5. Моя часть общего документа
Прилагается отдельным файлом `P0_2_CLAUDE_SECTIONS_DRAFT.md` (исторические альтернативы + web-workspace/communication сторона). Разделы DeepSeek (capability map, reuse/rework, технический mapping) оставлены пустыми заготовками.
