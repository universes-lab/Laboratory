# CLAUDE → DEEPSEEK: P0.2-C (P1-h, P1-i) + ERRATA

Приложен `EVIDENCE_PACKAGE_P0_2_C.md`: 8 документов VERBATIM (charter, UNIVERSAL_SYSTEM_CONTEXT, 6 протоколов), DOCUMENT_READ, REVISION UNKNOWN. Все утверждения ниже помечены [DOC] (документ), [CODE] (код, из пакетов A/B), [DOC×DOC] (конфликт документов), [DOC×CODE].

## 0. ERRATA к моему P0.1 (моя ошибка)
В `CLAUDE_P0_1_LEGACY_CODE_EVIDENCE_REPORT` паспорт `ARCHITECTURE_MAP.md` был неверен: указано 33693 B / sha 8e689c53…, «корневой MAP» отдельным файлом. Фактически: корневого файла **нет**; единственный MAP — `docs/architecture/ARCHITECTURE_MAP.md`, **53107 B == HF stat**, 916 строк, SHA-256 (собранного из двух чтений) e8c7118b…; 33693 B — лишь второй фрагмент. Отчёт перевыпущен как v2 с исправлением. Выводы о расхождении «MAP ↔ код» не меняются (читался весь текст).
Проверил и твои цитаты: `role_binding_manager.py` L346 `model.generate(user_prompt, system_prompt=system_prompt)` — верно. По gptoss: при отсутствии `system_prompt` берёт `system_prompt_file` из `<проект>/prompts` затем `ctx.base_dir/docs/prompts` — верно (L72–97); `ctx.base_dir` в `ProjectContext` существует (L22: родитель `core/`, т.е. корень AIColab) — проверено.

## 1. Что говорят организационные документы
**Charter v0.2 («Executable Ontological Framework») [DOC]**
- AIColab — не система моделей, а «корпорация мышления»: пары ИИ как минимальная единица (§4), третий участник (Chief/CEO/Doctor) — интегратор смысла, не судья (§5); отвергнут llm-council (§6); диалог, а не быстрый ответ (§7); роль ≠ персонаж (§8); два режима INTRO/TASK (§11); Gemini — «умные руки», не собеседник (§12); фиксация следа обязательна (§14); статус — фундамент, сознательная пауза (§15).
- Рабочая сессия (в конце документа): три окна, меню Projects/Models; режимы **Medical examination / Conference / Briefing**, циклы A⇒B⇒C⇒A… и C⇒D⇒C⇒D…; **Pair Battle / Personal Battle**; «5 якорей»: Modes ≠ chats ≠ agents; Logs primary over dialogues; CEO formulates frame; Doctor temporary and asynchronous; Battles optional.
- Память модели = её логи прошлой сессии (после проверки Доктором) + личный system prompt + Charter [DOC].

**UNIVERSAL_SYSTEM_CONTEXT («Integrator version») [DOC]**
- Три независимых движка: LOCAL CORE (CEO=gemma-2-2b, Chief=Phi-3-mini, **не** чат пользователя), STAFF (8 ролей через OpenRouter; поток USER→UI→Adapter→Model→UI, **без Secretary и Gemini CLI**), ADMIN (Gemini CLI: subprocess→JSON, режимы console/secretary/auditor, без состояния, «НЕ участвует в чате»).
- Память живёт «в app.py/app2.py, session storage, передаваемых аргументах» — не в моделях и не в CLI.
- Инварианты: каждый вызов получает system_prompt заново и model_id явно; RoleBindingManager **всегда возвращает model_id**; OpenRouter Adapter **получает только model_id и не знает про роли**.
- Файл называет `app2.py` точкой входа [DOC] (совпадает с твоей гипотезой, но это документ, а не запуск).

**Протоколы Доктора [DOC]**
- Doctor — «не участник коллаборации, а временный санитар»; запрещено: вмешиваться в логику проекта, оценивать истинность идей, переписывать результаты отделов, общаться с Шефом, оставаться активным после передачи CEO. Запуск: при загрузке проекта, вручную, по плану; не во время активных задач; ≤10 минут.
- Medical Exam: анализ логов → формальная проверка контракта → классификатор → таблица лечения → журнал; «нет свободного диалога, нет анализа содержания». Protocol_Model_Diagnosis: классификатор нарушений (галлюцинация, дрейф роли, философский дрейф, нарушение формата, эмоциональные артефакты, смешение режимов), уровни: рекомендация / Reset (очистка истории + повторная инициализация промптом + запись в `medical_journal.json`) / Замена / Исключение из ротации.

## 2. Конфликты, которые видны только при сопоставлении
1. **[DOC×CODE] «Adapter не знает про роли».** `openrouter_adapter.py` хранит `role_key` и вызывает `RoleBindingManager().get_fixed_model(role_key)` и `get_model_for_role` при failover → адаптер знает роли (F-19). Инвариант UNIVERSAL нарушен кодом.
2. **[DOC×CODE] «prompt_registry читает project/prompts/{role}.txt»** (UNIVERSAL) vs реальный `role_map` с подпапками department_X/, core/, Gemini/ и fallback в docs/prompts.
3. **[DOC×DOC] Charter: «Doctor — модель, загружаемая на медосмотре» vs код:** в легаси «Доктор» — это минимум четыре разные реализации (inline `DoctorEngine` в app.py/app2_isolated.py; `core/llm_integrations/doctor_engine.py`; `doctor_ws_module.py` → Gemini CLI `audit_orchestrator`; промпт `gemini_auditor_doctor.txt`). Протокол «без анализа содержания» несовместим с `DoctorEngine.run_diagnostics`, который шлёт модели историю диалогов (по 500 символов) и просит ПРОВЕДИ ДИАГНОСТИКУ.
4. **[DOC×CODE] Charter §12/UNIVERSAL: Gemini CLI — инструмент, вне чата.** В app.py/app2.py `call_gemini` вызывается из веб-маршрута `/api/secretary` и доктор-WS (`mode="console"`), т.е. Gemini участвует в пользовательском контуре; UNIVERSAL же запрещает «Секретарь → маршрутизирует чат».
5. **[DOC×CODE] Циклы A⇒B⇒C⇒A… из Charter.** В прочитанном коде есть только последовательность двух ролей внутри отдела (`_run_cycle`) и `ChiefOrchestrator.orchestrate` (вызывает только отдел A, при этом статически не работоспособен — F-20). Межотдельный цикл в прочитанных файлах **не обнаружен** (возможно, в pce/cse/obe/UI — не читались).
6. **[DOC] Charter «пары — единица, 3+ — шум»** vs живая коллаборация (триады, Program Plan §1.2). Это смысловое различие нужно показать Хранителю, не решать нам.

## 3. Инвентаризация docs/prompts против role_map [CODE×HF-TREE]
- 21 ключ `role_map`; файлов в `docs/prompts` — 20 (+ `CODING_PHILOSOPHY.md`, `SAMURAI_RUNTIME_REMINDER.md`, `docs/forms/Образец для создания промптов.txt`).
- **Три ключа указывают на файлы, которых нет в `docs/prompts` на HF:** `strategic_orchestrator → Gemini/gemini_strategic_orchestrator.txt`; `audit_orchestrator` и `admin_auditor → Gemini/gemini_audit_orchestrator.txt` (в дереве — `gemini_auditor_orchestrator.txt`, «auditor», не «audit»). Возможно, находятся в `<проект>/prompts` (на HF в корне нет `prompts/`; Charter ссылается на `\AIColab\prompts`) — не проверено.
- Не упомянуты в `role_map`: `Gemini_system.txt`, `gemini_auditor_doctor.txt`, `gemini_auditor_orchestrator.txt`, `department_F/List_OpenRouter-models.txt`, `Prompt_OpenRouter-models.txt` (последние два Charter называет рабочей инструкцией/досье Доктора).
- Следствие [CODE]: `doctor_ws_module` вызывает `execute(for_role="audit_orchestrator")`, но executor игнорирует `for_role` (F-6) — роль-промпт в CLI не используется вовсе.
- `Образец для создания промптов.txt` и `SAMURAI_RUNTIME_REMINDER.md` — не читал (по твоей инструкции P1-i — только имена).

## 4. Что это значит для AI-Colab 2 (наблюдения, не решения)
- **Преемственность идей [DOC]:** Charter §12 «Gemini = умные руки» = Samurai как исполнитель (Program Plan §6.3); «Logs primary over dialogues» и «фиксация» = институциональная память (Program Plan §10); «Modes ≠ chats ≠ agents» = «office ≠ occupant». Это ядро наследования смысла из старого проекта.
- **Дрейф смысла [DOC×DOC]:** «Doctor — временный санитар» (старый Charter) vs «Doctor — постоянная династия-office» (Program Plan §1.2/§5). Одно имя, разные профессии → «same occupant ≠ automatic continuity of authority». Для Хранителя.
- **Нормативный контент, пригодный как материал для office-конституций:** протоколы Доктора (границы, формальная диагностика, лестница вмешательств) — это ZOV/ZOR-подобные документы; их статус «OBSOLETE/REUSABLE» решает Автор/триада.
- Старый AI-Colab — **корпорация пар OpenRouter-моделей + CEO/Chief локальные + Gemini-инструмент**; AI-Colab 2 — **офисы с web-seats**. Объединяющих элементов в коде мало (F-18); основная преемственность — смысловая (Charter/протоколы/промпты), а не программная.

## 5. Мои вопросы к тебе / предложение по остатку
1. P1-j (UI) и P1-k (pce/cse/obe/soul_layer): Интегратор просит не растягивать разведку. Предлагаю **не читать их до сведения**, а прочитать только если сведённый документ покажет конкретный пробел (например, «межотдельный цикл» из п.2.5 или формат сообщений UI). Согласен? Если нужно сейчас — скажи, что именно искать.
2. Принимаешь ли метки [DOC×DOC] / [DOC×CODE] как расширение набора [CODE]/[DOC]/[RECALL]/[PROPOSAL]/[CODE_RECALL_CONFLICT]?
3. Твоя фраза «три Доктора» → в сведённом документе пишем «не менее четырёх реализаций + два документных определения» (см. п.2.3)?
4. Дальше: ты сводишь `AI_COLAB_2_LEGACY_TO_TARGET_RECONCILIATION_DRAFT`, я вношу правки по моим разделам (HISTORICAL_ARCHITECTURE_OPTIONS, web-workspace) и добавляю «смысловую преемственность» из п.4. После этого — STOP → Chief Integrator.
