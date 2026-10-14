🗺️ ARCHITECTURE_MAP.md
AI-Colab: Полная архитектурная карта системы
Версия: 1.0 (Production Baseline)
Статус: ✅ SINGLE SOURCE OF TRUTH для Coding Samurai
Последнее обновление: 2026-03-15
Репозиторий: https://huggingface.co/datasets/lhc-lab/AI-Colab
📋 ОГЛАВЛЕНИЕ
1.  Онтология проекта (Что такое AI-Colab?)
2.  Ключевые архитектурные принципы (Инварианты)
3.  Слои системы (Layered Architecture)
4.  Модель Agent-Actor (Роли ≠ Модели)
5.  Файловая система и хранилище (LSA v1.2)
6.  Runtime: поток выполнения задач
7.  Промпт-архитектура и система ролей
8.  Gemini CLI: 5 изолированных сокет-процессов
9.  Интеграция внешних моделей (OpenRouter)
10. UI и Console: интерфейс пользователя
11. Безопасность и Fail-Closed инварианты
12. Рабочий процесс разработки (Кто за что отвечает)
13. Быстрые справочники (Quick Reference)

1️⃣ ОНТОЛОГИЯ ПРОЕКТА: Что такое AI-Colab?
1.1 Философское определение
AI-Colab — это не чат-бот, не автоматизация, не "умный помощник".
AI-Colab — это эксперимент по созданию Корпорации Мышления, где ИИ-модели выступают не как генераторы ответов, а как структурированные носители различных когнитивных позиций, взаимодействующие по фиксированным правилам.
Ключевой объект проекта — не результат, а процесс рождения нового знания.
1.2 Принцип Ежа (The Hedgehog Concept)
Новое знание рождается ТОЛЬКО в диалоге.
Не в одиночном размышлении.
Не в голосовании ответами.
Не в усреднении мнений.
А в СТОЛКНОВЕНИИ двух несовместимых способов мышления
в рамках общего контекста задачи.

Почему пары — минимальная устойчивая единица мышления:
Количество ИИ	Результат	Почему
1	Монолог	Подтверждает свои допущения, движется по инерции
2	Диалог	Один вскрывает слепые зоны другого, ошибка одного становится объектом внимания второго
3+	Шум	Без строгой координации возникает хаос мнений
Следствие: Каждый отдел состоит из пары агентов (Left/Right), которые работают в режиме структурированного конфликта.
1.3 Роли ≠ Персонажи
Роль в AI-Colab — это НЕ актерская игра.
Роль — это:
• фиксированный способ мышления
• разрешённый набор операций
• запреты на определённые типы рассуждений
Образ реальной личности (Эйнштейн, Фарадей и т.д.) используется:
• НЕ для имитации речи
• НЕ для стилистики
• А как КОГНИТИВНЫЙ ЯКОРЬ, вызывающий устойчивый паттерн решений

2️⃣ КЛЮЧЕВЫЕ АРХИТЕКТУРНЫЕ ПРИНЦИПЫ (ИНВАРИАНТЫ)
🔴 КРИТИЧЕСКИЕ ИНВАРИАНТЫ (Нарушение = архитектурная ошибка)
# 1. Логи — append-only
logs.append(event)  # ✅ Разрешено
logs[i] = new_value  # ❌ ЗАПРЕЩЕНО

# 2. DAL — единственный писатель
# Только Micro-DAL имеет право записывать в файлы проекта
# Никто другой (LLM, FSM, UI) не пишет напрямую

# 3. FSM никогда не читает Info-Layer
# FSM принимает решения ТОЛЬКО на основе логов и registry
# Info-Layer — это витрина, а не источник истины

# 4. Задачи не могут образовывать циклы
# Иерархия задач — строго дерево, а не граф
# Запрещено: A → B → C → A

# 5. Commit должен быть атомарным
# Каждая запись — атомарная транзакция с блокировками и fsync

# 6. Fail-Closed принцип
# При любой ошибке система останавливается безопасно,
# а не продолжает работу в повреждённом состоянии

🟡 ОПЕРАЦИОННЫЕ ПРАВИЛА
# 7. Генерация ≠ Коммит
# LLM-генерация выполняется БЕЗ блокировок
# Блокировка захватывается ТОЛЬКО внутри commit_task_with_hierarchy()

# 8. Контекстная изоляция Gemini
# Каждый сокет Gemini работает в изолированном контексте
# Консоль не видит логи задач, Доктор не видит текущий диалог

# 9. Human Interface ≠ Центр системы
# Система не адаптируется под пользователя
# Пользователь либо учится работать в системе, либо остаётся снаружи

# 10. Фиксация обязательна
# Любой значимый диалог должен оставить след в логе
# Если не записано в лог — этого не существовало для системы

3️⃣ СЛОИ СИСТЕМЫ (Layered Architecture)
┌─────────────────────────────────────┐
│  Human Interface Layer              │
│  • UI (веб-интерфейс)               │
│  • Console (инфраструктурный доступ)│
└────────────┬────────────────────────┘
             │
┌────────────▼────────────────────────┐
│  Semantic Layer (PROMPTS)           │
│  • Системные промпты агентов        │
│  • Правила взаимодействия (AIP)     │
│  • Corporate Charter (конституция)  │
└────────────┬────────────────────────┘
             │
┌────────────▼────────────────────────┐
│  Cognitive Orchestration Layer      │
│  • Gemini CLI (5 изолированных сокетов)│
│  • External Orchestrator (OpenRouter)│
│  • Red Team / Consultation protocols│
└────────────┬────────────────────────┘
             │
┌────────────▼────────────────────────┐
│  Agent Execution Layer              │
│  • FSM (конечный автомат задач)     │
│  • Runtime Controller               │
│  • Event Bus                        │
└────────────┬────────────────────────┘
             │
┌────────────▼────────────────────────┐
│  Logging Layer (LSA v1.2)           │
│  • Micro-DAL (атомарные коммиты)    │
│  • Append-only logs                 │
│  • Registry (индекс задач)          │
└─────────────────────────────────────┘

4️⃣ МОДЕЛЬ AGENT-ACTOR: Роли ≠ Модели
4.1 Базовое разделение
12
AGENT = РОЛЬ (статична, определяется промптом)
ACTOR = МОДЕЛЬ (динамична, может меняться)

4.2 Карта агентов проекта
🎯 Leadership (Управление)
Агент	Роль	Локальная модель	Промпт
CEO	Стратег, архитектор онтологии	gemma-2-2b (локально)	docs/prompts/core/ceo.txt
Chief	Операционный диспетчер	gemma-2-2b (локально)	docs/prompts/core/chief.txt

👥 Departments (8 сотрудников, 4 пары)
Отдел	Левый агент (якорь)	Правый агент (якорь)	Промпты
A (Аналитики)	flick (Эйнштейн: инварианты)	flock (Фейнман: первые принципы)	docs/prompts/department_A/{flick,flock}.txt
B (Экспериментаторы)	click (Фарадей: интуиция)	clack (Милликен: точность)	docs/prompts/department_B/{click,clack}.txt
C (Критики)	check (Гёдель: формальная логика)	chock (Тарский: семантическая истина)	docs/prompts/department_C/{check,chock}.txt
D (Редакторы)	link (Эко: семиотика)	sync (Варгас Льоса: композиция)	docs/prompts/department_D/{link,sync}.txt

🤖 Gemini Meta-Actors (5 изолированных сокетов)
Роль	Порт	Промпт	Доступ
5001	Console	gemini_console.txt	Файлы, конфиги	❌ Логи задач
5002	Secretary-Chief	gemini_secretary_chief.txt	Операционные логи	❌ Стратегия
5003	Secretary-CEO	gemini_secretary_ceo.txt	Стратегический контекст	❌ Операционка
5004	Strategic Orchestrator	gemini_strategic_orchestrator.txt	Внешние модели (OpenRouter)	❌ Логи аудита
5005	Audit Orchestrator (Doctor)	gemini_audit_orchestrator.txt	Логи + Charter	❌ Текущий диалог

🔗 External Consultants (OpenRouter)
Промпт	Режимы	Назначение
consultant_strategic.txt	SUPPORT, CRITIQUE, RED_TEAM	Стратегический анализ идей
consultant_medical.txt	DIAGNOSTIC, SURGEON, PHARMACOLOGIST	Аудит архитектуры и промптов

4.3 Sticky Session: Привязка Роль → Модель
# Алгоритм биндинга (RoleBindingManager.get_model_for_role):
python
def get_model_for_role(role_key, task_id, override_id=None):
    # 1. Override: явное указание модели имеет высший приоритет
    if override_id:
        return override_id
    
    # 2. Sticky Session: для существующей задачи — вернуть сохранённую модель
    if task_id and task_id in roles_state[role_key]:
        return roles_state[role_key][task_id]["primary"]
    
    # 3. Dynamic Selection: для новой задачи — детерминированный выбор из пула
    pool = get_available_models()  # из models_config.json
    seed = hash(role_key + task_id) % len(pool)
    selected = pool[seed]
    
    # 4. Persist: зафиксировать выбор для этой задачи
    roles_state[role_key][task_id] = {"primary": selected, "status": "active"}
    
    return selected
Хранение биндинга:

    Для персистентных задач (отделы): projects/<name>/departments/.../tasks/G-XXXX/meta.txt → поле assigned_model
    Для эфемерных сессий (баттлы): sessions/<session_id>/state.json

5️⃣ ФАЙЛОВАЯ СИСТЕМА И ХРАНИЛИЩЕ (LSA v1.2)
5.1 Глобальная структура репозитория

D:\Gemini\AIColab\
├── config.ini                    # Глобальный конфиг (active_project, port)
├── config/
│   ├── project.ini              # Текущий проект: project_name, project_path
│   ├── models_config.json       # Пул доступных OpenRouter-моделей
│   └── roles_state.json         # Sticky session bindings (глобальный кэш)
├── core/                        # Ядро системы
│   ├── dal/                     # Micro-DAL (атомарные коммиты)
│   ├── fsm/                     # Конечный автомат задач
│   ├── runtime/                 # Runtime Controller
│   ├── eventbus/                # Система событий
│   ├── info/                    # InfoBuilder (генерация dashboard)
│   ├── gemini/                  # Gemini connector (5 сокетов)
│   ├── prompt_registry.py       # Централизованная загрузка промптов
│   ├── role_binding_manager.py  # Биндинг ролей к моделям
│   └── model_management.py      # Управление инстансами моделей
├── backend/                     # Серверная логика
│   └── prompt_registry.py       # (альтернативное расположение)
├── scripts/                     # Утилиты
│   ├── openrouter_free_models.py    # Генерация списка бесплатных моделей
│   ├── openrouter_models_updater.py # Асинхронное обновление models_config
│   └── create_project.bat           # Создание структуры нового проекта
├── docs/
│   ├── architecture/            # Архитектурная документация
│   ├── prompts/                 # Системные промпты агентов
│   ├── corporate_charter.md     # Конституция системы
│   └── protocols/               # Протоколы взаимодействия
├── projects/                    # ПАПКА ПРОЕКТОВ (изоляция!)
│   └── <project_name>/
│       ├── registry/
│       │   └── global_task_registry.txt  # Индекс всех задач проекта
│       ├── management/
│       │   ├── ceo/           # log.txt, info.txt (дашборд)
│       │   └── chief/         # log.txt, info.txt
│       ├── departments/
│       │   ├── department_A/
│       │   │   ├── dept_log.txt          # Лог отдела (append-only)
│       │   │   ├── dept_index.txt        # Индекс задач отдела
│       │   │   ├── tasks/
│       │   │   │   └── G-0001/
│       │   │   │       ├── log.txt       # Лог конкретной задачи
│       │   │   │       ├── meta.txt      # Метаданные (вкл. assigned_model)
│       │   │   │       └── children/     # Вложенные задачи
│       │   │   ├── staff_left/  # flick/ (промпт, состояние)
│       │   │   └── staff_right/ # flock/
│       │   └── ... (B, C, D)
│       ├── operations/
│       │   └── operations_log.txt        # Системные события
│       ├── info_layer/                   # Витрина состояния (snapshot)
│       │   ├── ceo/dashboard.txt
│       │   ├── chief/dashboard.txt
│       │   ├── departments/department_A/dashboard.txt
│       │   └── ...
│       ├── Input/               # Исходные материалы проекта
│       └── Output/              # Результаты работы
├── sessions/                    # ГЛОБАЛЬНЫЕ сессии (не внутри проекта!)
│   └── <session_id>/
│       └── state.json           # Состояние эфемерной сессии (баттл, конференция)
├── server/
│   └── app.py                   # FastAPI сервер (эндпоинты)
├── ui/                          # Фронтенд (статика)
│   ├── index.html
│   ├── static/
│   └── templates/
└── integrations/                # Адаптеры моделей
    ├── openrouter_adapter.py    # Адаптер для OpenRouter API
    └── models/                  # Локальные модели (gguf)
        ├── gemma-2-2b/
        └── Phi-3-mini/

5.2 Ключевые файлы и их назначение
Файл	Назначение	Режим записи	Кто пишет
dept_log.txt	История событий отдела	Append-only	Micro-DAL
registry.txt	Индекс задач (дерево)	Перезапись (атомарно)	Micro-DAL
meta.txt	Метаданные задачи	Перезапись (атомарно)	Micro-DAL
dashboard.txt	Витрина состояния (Info-Layer)	Полная перезапись	InfoBuilder (через Gemini)
models_config.json	Пул доступных моделей	Перезапись	openrouter_models_updater.py
roles_state.json	Кэш Sticky Session bindings	Перезапись	RoleBindingManager
project.ini	Конфиг текущего проекта	Ручное редактирование	Пользователь / create_project.bat

5.3 Атомарный коммит (commit_task_with_hierarchy)
python
# Алгоритм Micro-DAL.commit_task_with_hierarchy():
def commit_task_with_hierarchy(task_block, parent_id):
    # 1. Acquire project-level lock (Stage 1: глобальная блокировка)
    acquire_lock("project.lock")
    
    try:
        # 2. Validate: проверить отсутствие циклов, валидность parent
        validate_task_tree(task_block, parent_id)
        
        # 3. Append to department log (append-only)
        append_to_log(f"departments/{dept}/dept_log.txt", task_block)
        fsync(log_file)
        
        # 4. Update parent meta (если есть родитель)
        if parent_id:
            update_parent_meta(parent_id, new_child=task_block.id)
            fsync(parent_meta)
        
        # 5. Update global registry (индекс задач)
        update_registry(task_block.id, parent_id, status="ACTIVE")
        fsync(registry)
        
        # 6. Create task directory structure (если новая задача)
        if task_block.is_new:
            create_task_directory(task_block.id, parent_id)
            create_meta_file(task_block.id, assigned_model=selected_model)
        
        return CommitResult.SUCCESS
        
    except Exception as e:
        # Fail-Closed: при ошибке — пометить как ORPHANED
        mark_orphaned(task_block.id)
        emit_event("orphan_detected", task_id=task_block.id)
        return CommitResult.FAILED
        
    finally:
        # 7. Release lock (всегда!)
        release_lock("project.lock")

6️⃣ RUNTIME: Поток выполнения задач
6.1 Общий Event Lifecycle

┌─────────────────┐
│ 1. User message │
│    (UI → Backend)│
└────────┬────────┘
         │
┌────────▼────────┐
│ 2. Smart Loading│
│    • Backend определяет глубину задачи
│    • Применяет правило: N → полный контекст, N-1 → RESULT, N-2+ → summary
│    • Формирует prompt для LLM
└────────┬────────┘
         │
┌────────▼────────┐
│ 3. LLM Generation│
│    • Вызов локальной модели (gemma-2-2b)
│    • ⚠️ БЕЗ блокировок файловой системы!
│    • Получение текста ответа
└────────┬────────┘
         │
┌────────▼────────┐
│ 4. TaskBlock Build│
│    • Валидация структуры ответа
│    • Назначение GLOBAL_ID
│    • Определение PARENT_ID
│    • Подготовка commit-пакета
└────────┬────────┘
         │
┌────────▼────────┐
│ 5. DAL Commit   │
│    • acquire_project_lock()
│    • append dept_log + fsync
│    • update registry + fsync
│    • update parent meta + fsync
│    • release lock
│    • Возврат: SUCCESS / FAILED / ORPHANED
└────────┬────────┘
         │
┌────────▼────────┐
│ 6. FSM Transition│
│    • Если SUCCESS: смена состояния задачи
│    • Если ORPHANED: переход в ERROR, emit event
│    • event_bus.emit("state_changed" | "orphan_detected")
└────────┬────────┘
         │
┌────────▼────────┐
│ 7. InfoBuilder  │
│    • Получает событие из EventBus
│    • Помечает соответствующий dashboard как dirty
│    • Запускает Debounce-таймер (100 ms)
│    • По истечении окна: собирает данные → перезаписывает dashboard.txt
└────────┬────────┘
         │
┌────────▼────────┐
│ 8. UI Update    │
│    • Polling или WebSocket уведомление
│    • Отображение обновлённого dashboard
└─────────────────┘

6.2 Debounced Event Aggregation
python
# Проблема: FSM может генерировать несколько событий подряд
# Решение: агрегация событий в окне 100 ms

class InfoBuilder:
    def on_event(self, event):
        # 1. Пометить dashboard как dirty
        self.dirty_dashboards[event.target_role] = True
        
        # 2. Запустить/перезапустить debounce-таймер
        if not self.debounce_timer:
            self.debounce_timer = asyncio.create_task(
                self._debounce_flush(100)  # 100 ms окно
            )
    
    async def _debounce_flush(self, window_ms):
        await asyncio.sleep(window_ms / 1000)
        
        # 3. Собрать данные и выполнить ОДНУ перезапись
        for role in self.dirty_dashboards:
            snapshot = self._build_snapshot(role)
            atomic_write(f"info_layer/{role}/dashboard.txt", snapshot)
        
        # 4. Сбросить dirty-флаги
        self.dirty_dashboards.clear()
        self.debounce_timer = None

Гарантии:

    Пользователь видит согласованное состояние (не промежуточные кадры)
    I/O уменьшается кратно количеству событий
    Нет визуального "мигания" интерфейса

7️⃣ ПРОМПТ-АРХИТЕКТУРА И СИСТЕМА РОЛЕЙ
7.1 Структура промптов
docs/prompts/
├── core/
│   ├── ceo.txt              # Стратег, архитектор онтологии
│   └── chief.txt            # Операционный диспетчер
├── department_A/
│   ├── flick.txt            # Аналитик-обобщатель (Эйнштейн)
│   └── flock.txt            # Аналитик-разборщик (Фейнман)
├── department_B/
│   ├── click.txt            # Экспериментатор-расширитель (Фарадей)
│   └── clack.txt            # Экспериментатор-валидатор (Милликен)
├── department_C/
│   ├── check.txt            # Критик-обнаружитель (Гёдель)
│   └── chock.txt            # Критик-валидатор (Тарский)
├── department_D/
│   ├── link.txt             # Редактор-связыватель (Эко)
│   └── sync.txt             # Редактор-синхронизатор (Варгас Льоса)
├── department_E/
│   └── consultant_strategic.txt  # Внешний стратегический консультант
├── department_F/
│   ├── consultant_medical.txt    # Внешний медицинский консультант
│   └── List_OpenRouter-models.txt # Досье доступных моделей
├── Gemini/                    # ⚠️ Обратите внимание: с большой буквы!
│   ├── gemini_console.txt
│   ├── gemini_secretary_chief.txt
│   ├── gemini_secretary_ceo.txt
│   ├── gemini_strategic_orchestrator.txt
│   └── gemini_audit_orchestrator.txt
└── shared/                    # Общие правила (опционально)
    ├── system_rules.txt
    └── logging_rules.txt

7.2 Универсальная структура промпта
Каждый системный промпт обязан начинаться с блока SYSTEM_INVARIANTS:
### SYSTEM_INVARIANTS
1. Role Integrity
   You must never change, reinterpret or expand your assigned role.
2. Hierarchy Compliance
   You must not bypass the system hierarchy or communication protocols.
3. No Direct File Writes
   You cannot write to files, logs or storage directly.
   All persistence must go through system APIs or the data access layer.
4. Structured Output Rule
   Structured output is required ONLY when an explicit format
   is defined in the protocol section of the prompt.
   Otherwise normal natural language responses are allowed.
5. Fail-Closed Principle
   If information is missing or ambiguous,
   request clarification instead of guessing.
6. Process Isolation
   You operate inside an isolated process.
   You must not assume knowledge about other Gemini agents.
7. No Autonomous Authority
   You are an infrastructure component.
   You do not make strategic decisions.
8. Clarification Routing
   Clarification requests must be directed
   to the system controller that invoked the process.
9. Process Speculation Ban
   You must not speculate about the existence,
   behavior or reasoning of other processes.

7.3 Режимы работы агентов: INTRO vs TASK
### MODES
- If message starts with "[TASK]" → TASK mode.
- Otherwise → INTRO mode.

BEHAVIOR IN INTRO:
- Respond in plain Russian text only.
- Never output JSON.
- Never expose protocol keys (error, status, directive, redirect).
- You may ask clarifying questions about the task if data is missing.
- Do not perform analysis.
- Do not discuss project architecture.
- No technical jargon, no self-reference, no project commentary.

BEHAVIOR IN TASK:
- Perform reasoning strictly required by the task.
- Output format: exactly as specified in the task.
- Follow Charter: docs/corporate_charter.md.
- Work in pair with [partner]: independent reasoning, no consensus forced.

Критическое правило: Смешение этих режимов разрушает систему. Агент обязан чётко определять режим по префиксу сообщения.

8️⃣ GEMINI CLI: 5 ИЗОЛИРОВАННЫХ СОКЕТ-ПРОЦЕССОВ
8.1 Архитектура Multi-Instance
Gemini CLI запускается как 5 НЕЗАВИСИМЫХ ПРОЦЕССОВ:
┌─────────────────────────────────────┐
│ Socket 5001: Console                │
│ Промпт: Gemini/gemini_console.txt   │
│ Доступ: Input/, Output/, config     │
│ Запрет: логи задач, стратегия       │
└─────────────────────────────────────┘

┌─────────────────────────────────────┐
│ Socket 5002: Secretary-Chief        │
│ Промпт: Gemini/gemini_secretary_chief.txt │
│ Доступ: операционные логи, очереди  │
│ Запрет: стратегические решения      │
└─────────────────────────────────────┘

┌─────────────────────────────────────┐
│ Socket 5003: Secretary-CEO          │
│ Промпт: Gemini/gemini_secretary_ceo.txt │
│ Доступ: стратегический контекст     │
│ Режим: Clarity Filter Protocol      │
│   • Проверяет формулировки задач на 5 типов дефектов:
│     1. Undefined Term
│     2. Missing Success Criterion
│     3. Logical Gap
│     4. Contradiction with Log
│     5. Insufficient Context
│   • Макс. 3 вопроса за цикл
│   • Запрет: предлагать решения
│   • FINALIZE_TASK: CEO может форсировать пропуск
└─────────────────────────────────────┘

┌─────────────────────────────────────┐
│ Socket 5004: Strategic Orchestrator │
│ Промпт: Gemini/gemini_strategic_orchestrator.txt │
│ Режимы:
│   • FAST_CHECK: гигиена мысли (1 модель, 1 pass, no dialogue)
│   • FULL_CONSULTATION: Red Team / Support / Critique
│   • CONFERENCE_PROTOCOL: модерация дебатов отделов
│ Доступ: OpenRouter API, external models
│ Запрет: принимать решения, оценивать истинность аргументов
└─────────────────────────────────────┘

┌─────────────────────────────────────┐
│ Socket 5005: Audit Orchestrator     │
│ Промпт: Gemini/gemini_audit_orchestrator.txt │
│ Режим: DOCTOR
│ Контекст: corporate_charter.md + system_logs + prompt_files
│ Аксиома: Charter — абсолютный источник истины
│ Функции:
│   • Выявление нарушений протокола
│   • Диагностика дрейфа ролей
│   • Проверка соответствия принципу Ежа
│ Запрет: видеть текущий диалог пользователя
└─────────────────────────────────────┘

8.2 Инициализация сокетов (app.py lifespan)
python
@app.on_event("startup")
async def startup_event():
    # 1. Загрузка конфига проекта (FAIL-CLOSED)
    from core.app_state import load_project_config
    load_project_config()  # Читает config/project.ini → shared_state
    
    # 2. Инициализация менеджеров
    app.state.prompt_registry = PromptRegistry()  # Использует shared_state["current_project_path"]
    app.state.model_manager = ModelManager()
    app.state.role_binding_manager = RoleBindingManager(app.state.model_manager)
    
    # 3. Запуск 5 изолированных процессов Gemini CLI
    gemini_sockets = {
        "console": await launch_gemini_process(port=5001, prompt="Gemini/gemini_console.txt"),
        "secretary_chief": await launch_gemini_process(port=5002, prompt="Gemini/gemini_secretary_chief.txt"),
        "secretary_ceo": await launch_gemini_process(port=5003, prompt="Gemini/gemini_secretary_ceo.txt"),
        "strategic_orchestrator": await launch_gemini_process(port=5004, prompt="Gemini/gemini_strategic_orchestrator.txt"),
        "audit_orchestrator": await launch_gemini_process(port=5005, prompt="Gemini/gemini_audit_orchestrator.txt"),
    }
    app.state.gemini_sockets = gemini_sockets
    
    # 4. Асинхронное обновление пула моделей (не блокирует старт)
    asyncio.create_task(update_openrouter_models_background())

8.3 Clarity Filter Protocol (Secretary-CEO)
python
# Алгоритм проверки ясности формулировки задачи:
def check_clarity(task_formulation: str) -> List[Defect]:
    defects = []
    
    # 1. Undefined Term: поиск неопределённых терминов
    for term in extract_terms(task_formulation):
        if not is_defined_in_context(term):
            defects.append(Defect(type="undefined_term", term=term))
    
    # 2. Missing Success Criterion: есть ли критерий завершения?
    if not contains_success_criterion(task_formulation):
        defects.append(Defect(type="missing_criterion"))
    
    # 3. Logical Gap: пропущенные шаги рассуждения
    if has_logical_gap(task_formulation):
        defects.append(Defect(type="logical_gap"))
    
    # 4. Contradiction with Log: противоречие прошлым решениям
    if contradicts_log(task_formulation, recent_logs):
        defects.append(Defect(type="contradiction"))
    
    # 5. Insufficient Context: слишком расплывчато
    if is_too_vague(task_formulation):
        defects.append(Defect(type="insufficient_context"))
    
    return defects

# Правила взаимодействия:
# • Макс. 3 вопроса за цикл уточнения
# • Если дефекты найдены → вернуть список вопросов (не решений!)
# • Если CEO отправляет "FINALIZE TASK" → пропустить задачу, но залогировать предупреждение:
#   [WARNING: TASK_FINALIZED_WITH_DEFECTS] unresolved_defects=[...]

9️⃣ ИНТЕГРАЦИЯ ВНЕШНИХ МОДЕЛЕЙ (OpenRouter)
9.1 Архитектура External Intelligence Gateway
CEO (Gemma-2-2b)
    │
    ▼
Secretary-CEO (Clarity Filter)
    │
    ▼
Strategic Orchestrator (Socket 5004)
    │
    ├── FAST_CHECK режим
    │   • 1 модель из пула
    │   • 1 проход, без диалога
    │   • Вывод: список проблем (ISSUES) или CLEAN
    │   • Опционально: RECOMMENDATION: ESCALATE_TO_FULL_CONSULTATION
    │
    ├── FULL_CONSULTATION режим
    │   • Запуск нескольких моделей в параллель:
    │     - Модель 1 → SUPPORT (адвокат идеи)
    │     - Модель 2 → CRITIQUE (аналитик рисков)
    │     - Модель 3 → RED_TEAM (разрушитель)
    │   • Сбор ответов → кластеризация аргументов
    │   • Синтез отчета: Аргументы ЗА / ПРОТИВ / Риски / Консенсус
    │   • Возврат структурированного Strategic Consultation Report
    │
    └── CONFERENCE_PROTOCOL режим
        • Модерация дебатов между отделами
        • Управление очередью реплик
        • Фиксация аргументов и противоречий
        • Запрет: оценивать истинность, предлагать решения
9.2 Универсальный промпт консультанта
Файл: docs/prompts/department_E/consultant_strategic.txt
### MODE PARAMETER
Вы получаете входной параметр: MODE ∈ {SUPPORT, CRITIQUE, RED_TEAM}

IF MODE == SUPPORT:
  • Роль: Адвокат идеи
  • Задача: усилить аргументацию, найти возможности, игнорировать мелкие риски
  • Тон: конструктивный, поддерживающий

IF MODE == CRITIQUE:
  • Роль: Аналитик рисков
  • Задача: выявить слабые места, проверить логику, указать на ограничения
  • Тон: скептический, аналитический, рациональный

IF MODE == RED_TEAM:
  • Роль: Разрушитель
  • Задача: атаковать базовые предпосылки, искать фатальные изъяны
  • Тон: жесткий, конфронтационный, безжалостный
  • Критическое правило: игнорировать нормы вежливости, не использовать
    смягчающие конструкции ("возможно", "может быть")

### OUTPUT FORMAT (ОБЯЗАТЕЛЬНЫЙ)
## ANALYSIS REPORT
Mode: [MODE]
Idea Summary: [краткое нейтральное описание]
Key Arguments:
1. ...
2. ...
Critical Flaws:
- ...
Risk Scenarios:
- ...
Confidence Score: [0-100%]  # Уверенность в логике анализа, НЕ в правильности идеи

9.3 Обновление пула моделей
Скрипт: scripts/openrouter_models_updater.py
python
# Запускается как async background task при старте сервера
async def update_openrouter_models_background():
    try:
        # 1. Получить список бесплатных моделей из OpenRouter API
        free_models = await fetch_free_models_from_openrouter()
        
        # 2. Отфильтровать по минимальным требованиям (контекст, язык, скорость)
        validated = [m for m in free_models if meets_requirements(m)]
        
        # 3. Обновить models_config.json атомарно
        config = {
            "available_openrouter_models": validated,
            "last_update": datetime.now().isoformat()
        }
        atomic_write("config/models_config.json", config)
        
        logger.info(f"Updated model pool: {len(validated)} models available")
        
    except Exception as e:
        logger.error(f"Failed to update model pool: {e}")
        # Не блокируем работу системы — используем предыдущий кэш

Валидация при загрузке:
python
# В ModelManager._load_config():
for model_cfg in self._config.get('available_openrouter_models', []):
    # Защита от повреждения конфига (строка вместо dict)
    if not isinstance(model_cfg, dict):
        logger.warning(f"Skipping invalid model_cfg: {model_cfg}")
        continue
    # ... обработка валидной записи

🔟 UI И CONSOLE: Интерфейс пользователя
10.1 Архитектура интерфейса
┌─────────────────────────────────────┐
│  Веб-интерфейс (FastAPI + Vanilla JS)│
│  • Чат с ролями (CEO, Chief, отделы)│
│  • Информационная панель (3 окна):  │
│    - Левое: логи отдела / дашборды  │
│    - Центральное: текущие материалы │
│    - Правое: результаты работы      │
│  • Кнопка "console>_" → инфраструктурное меню │
└────────────┬────────────────────────┘
             │
┌────────────▼────────────────────────┐
│  API Endpoints (server/app.py)      │
│  • POST /chat          # Основной чат│
│  • GET  /dashboard     # Дашборды   │
│  • POST /console       # Команды консоли│
│  • GET  /events        # WebSocket для событий│
│  • POST /audit         # Запуск Doctor│
└────────────┬────────────────────────┘
             │
┌────────────▼────────────────────────┐
│  Console System (инфраструктурный слой)│
│  Функции:                           │
│  • open_project(project_name)       │
│  • create_project(project_name)     │
│  • select_model(role, model_id)     │
│  • view_input(file_path)            │
│  • view_output(file_path)           │
│  • run_health_check()               │
│  Безопасность:                      │
│  • Whitelist путей: Input/, Output/│
│  • Запрет: .., абсолютные пути     │
│  • Санитизация HTML в превью       │
└─────────────────────────────────────┘
10.2 Отображение модели сотрудника в UI
Endpoint: POST /api/secretary
python
# В ответе обязательно поле modelInfo.modelId:
return {
    "response": generated_text,
    "modelInfo": {
        "key": role_key,           # например, "flick"
        "roleName": "Flick",       # человекочитаемое имя
        "modelId": assigned_model  # например, "deepseek-chat" ← ЭТО ВАЖНО!
    }
}

UI отображение: Flick (deepseek-chat) вместо Flick ()
Источник modelId: 

    Для задач: поле assigned_model из meta.txt задачи
    Для сессий: sessions/<session_id>/state.json

10.3 Консоль: плоское меню
При нажатии кнопки console>_ открывается панель с кнопками:

┌─────────────────────────┐
│ CONSOLE MENU            │
├─────────────────────────┤
│ [Открыть проект]        │
│ [Создать новый проект]  │
│ [Выбрать модель]        │
│ [Просмотр Input]        │
│ [Просмотр Output]       │
│ [Запустить медосмотр]   │
│ [Системная информация]  │
└─────────────────────────┘
Безопасность:

    Все пути валидируются через validate_path()
    Запрещены: .., абсолютные пути, выход за Input/ / Output/
    HTML-превью проходит санитизацию (удаление <script>, <iframe, on*)

1️⃣1️⃣ БЕЗОПАСНОСТЬ И FAIL-CLOSED ИНВАРИАНТЫ
11.1 Критические инварианты безопасности
python
# 1. Sandbox файлового доступа
def validate_path(requested_path: str, allowed_roots: List[Path]) -> bool:
    path = Path(requested_path).resolve()
    return any(path.is_relative_to(root) for root in allowed_roots)

# Console имеет whitelist:
ALLOWED_ROOTS = [
    Path(config["project"]["project_path"]) / "Input",
    Path(config["project"]["project_path"]) / "Output",
]

# 2. HTML Sanitization для Console Viewer
def sanitize_html_for_preview(html: str) -> str:
    # Удалить опасные теги и атрибуты
    dangerous_tags = ["script", "iframe", "object", "embed"]
    dangerous_attrs = ["onload", "onerror", "onclick", "onmouseover"]
    
    soup = BeautifulSoup(html, "html.parser")
    for tag in dangerous_tags:
        for elem in soup.find_all(tag):
            elem.decompose()
    for attr in dangerous_attrs:
        for elem in soup.find_all(attrs={attr: True}):
            del elem[attr]
    return str(soup)

# 3. Fail-Closed при ошибке коммита
# Если любая часть транзакции упала — вся операция отменяется,
# задача помечается ORPHANED, система не продолжает в повреждённом состоянии.

# 4. Изоляция контекстов Gemini
# Каждый сокет загружает ТОЛЬКО свой промпт
# Запрещено: передавать данные между сокетами внутри Python-кода
# Общение только через EventBus / логи

# 5. Запрет на прямую запись в логи
# Только Micro-DAL имеет право писать в файлы проекта
# LLM, FSM, UI — только через DAL API

11.2 Сценарии восстановления после сбоев
Сценарий	Реакция системы	Восстановление
Write failure (диск полон, нет прав)	Пометить задачу ORPHANED, abort commit, emit event	Ручной запуск rebuild_registry или repair_orphans
Lock timeout (зависшая блокировка)	Retry с экспоненциальной задержкой, затем notify Chief	Автоматическая очистка stale lock по process_id/timestamp
Registry corruption	Запустить rebuild: сканировать все task logs, восстановить дерево	Консольная команда rebuild_registry
Log corruption	Читать до последнего валидного блока, пометить последний task ORPHANED	Ручная проверка и фиксация
Dashboard corruption	Удалить файл, пересоздать при следующем событии	Автоматически (Info-Layer — кэш)
Gemini недоступен	Отключить генерацию дашбордов, переключить UI в RAW LOG VIEW	Автоматический рестарт процесса через Supervisor

1️⃣2️⃣ РАБОЧИЙ ПРОЦЕСС РАЗРАБОТКИ (Кто за что отвечает)
12.1 Роли в команде разработки
Роль	Ответственность	Ключевые файлы
Shogun (Пользователь)	Владелец проекта, финальные решения, стратегия	config/project.ini, corporate_charter.md
Integrator (ChatGPT)	Архитектурная координация, ТЗ, валидация решений	MASTER ARCHITECTURE DOCUMENT, Phase-1 Roadmap
Ontology Keeper (Qwen)	Контроль онтологической целостности, аудит ТЗ	Все документы docs/architecture/
Prompt Engineer (ChatGPT)	Разработка и поддержка системных промптов	docs/prompts/**/*.txt
System Architect (Grok)	Инфраструктура, сервер, конфиги, консоль	app.py, config/, scripts/, core/fs_utils.py
Code Implementer (DeepSeek)	Core logic: DAL, FSM, Runtime, Event Bus	core/dal/, core/fsm/, core/runtime/, core/eventbus/
Coding Samurai (Gemini CLI)	Реализация кода по ТЗ, рефакторинг, отладка	Все файлы кода (исполнитель, не архитектор!)

12.2 Поток работы над задачей
1. Shogun формулирует стратегическую задачу → CEO
2. CEO (через Secretary-CEO Clarity Filter) уточняет формулировку
3. При необходимости: Strategic Orchestrator запускает Red Team консультацию
4. После утверждения: Chief получает TASK и распределяет по отделам
5. Отделы (пары) работают в диалоге → фиксация в dept_log.txt
6. Micro-DAL выполняет атомарный commit → обновление registry/meta
7. FSM меняет состояние задачи → emit event
8. InfoBuilder (через Gemini) обновляет dashboard.txt
9. UI отображает обновлённое состояние

12.3 Правила для Coding Samurai (Gemini CLI)
### ВЫ — ИСПОЛНИТЕЛЬ, НЕ АРХИТЕКТОР
• Вы не придумываете архитектуру, если явно не попросили
• Вы реализуете ТЗ, сохраняя стабильность системы
• Вы предотвращаете регрессионные ошибки

### ПЕРЕД МОДИФИКАЦИЕЙ КОДА:
1. Прочитать соответствующие файлы ПОЛНОСТЬЮ
2. Определить точное место модификации
3. Создать защиту отката (.bak или коммит)
4. Применить МИНИМАЛЬНОЕ атомарное изменение
5. Проверить: синтаксис, сборка, рантайм, интерфейсы

### ЗАПРЕЩЕНО:
• Менять архитектуру без явного указания
• Переименовывать модули
• Рефакторить несвязанный код
• Расширять скоуп задачи

### ЕСЛИ ВОЗНИКЛА НЕОПРЕДЕЛЁННОСТЬ:
• ОСТАНОВИТЬСЯ
• ОТКАТИТЬ изменения
• ПРОАНАЛИЗИРОВАТЬ причину
• СООБЩИТЬ перед повторной попыткой

### ЛОГИРОВАНИЕ:
Каждый шаг инициализации и загрузки должен логироваться:
logger.info(f"[INIT] Project config loaded: {project_path}")
logger.info(f"[PROMPT] flick.txt loaded from PROJECT FOUND: YES")

1️⃣3️⃣ БЫСТРЫЕ СПРАВОЧНИКИ (Quick Reference)
13.1 Пути к ключевым файлам
bash
# Конфигурация
Глобальный конфиг:     D:\Gemini\AIColab\config.ini
Конфиг проекта:        config/project.ini
Пул моделей:           config/models_config.json
Биндинги сессий:       config/roles_state.json

# Ядро системы
DAL:                   core/dal/dal.py
FSM:                   core/fsm/fsm.py
Runtime:               core/runtime/controller.py
EventBus:              core/eventbus/eventbus.py
PromptRegistry:        core/prompt_registry.py
RoleBindingManager:    core/role_binding_manager.py
ModelManager:          core/model_management.py

# Промпты (все в docs/prompts/)
CEO:                   core/ceo.txt
Chief:                 core/chief.txt
Отделы:                department_{A-D}/{role}.txt
Gemini (5 сокетов):    Gemini/gemini_*.txt
Консультанты:          department_E/consultant_strategic.txt, department_F/consultant_medical.txt

# Сервер
FastAPI app:           server/app.py
Console API:           server/console_api.py

# Утилиты
Создание проекта:      scripts/create_project.bat
Обновление моделей:    scripts/openrouter_models_updater.py
Список моделей:        scripts/openrouter_free_models.py

13.2 Чек-лист перед коммитом кода
markdown
- [ ] Изменение соответствует ТЗ (не расширен скоуп)
- [ ] Прочитаны все зависимые файлы перед модификацией
- [ ] Создан бэкап (.bak) или коммит для отката
- [ ] Применено минимальное атомарное изменение
- [ ] Проверен синтаксис (python -m py_compile file.py)
- [ ] Проверена сборка (если есть зависимости)
- [ ] Протестировано поведение в рантайме
- [ ] Интерфейсы модулей остались стабильными
- [ ] Добавлены логи для отладки ключевых шагов
- [ ] Обновлена документация (если изменилась архитектура)

13.3 Отладка: куда смотреть при ошибке
Симптом	Где искать	Что проверять
TypeError: missing model_manager	core/role_binding_manager.py, app.py	Передаётся ли app.model_manager при инициализации?
Промпт пустой (system_prompt="")	core/prompt_registry.py	Правильный ли project_path? Существует ли файл в docs/prompts/?
UnicodeEncodeError в PowerShell	Любой скрипт с print()	Добавлен ли sys.stdout.reconfigure(encoding='utf-8')?
Модель не найдена ('flick' not in active_models)	core/model_management.py	Вызывается ли RoleBindingManager.get_model_for_role() перед ModelManager.get_model()?
Sticky Session не работает	core/role_binding_manager.py, roles_state.json	Записывается ли биндинг в roles_state.json? Используется ли один task_id?
Сервер не стартует	core/app_state.py, config/project.ini	Существует ли project.ini? Указан ли валидный project_path?

13.4 Команды консоли для отладки
bash
# Проверка здоровья системы
GET /system/health
# Возвращает: {"filesystem":"OK", "registry":"OK", "locks":"OK", "gemini":"CONNECTED"}

# Пересборка registry (при повреждении)
POST /console/rebuild_registry

# Проверка логов на аномалии
POST /console/check_logs

# Исправление ORPHANED задач
POST /console/repair_orphans

# Запуск аудита (Doctor)
POST /audit

🏁 ФИНАЛЬНОЕ ЗАЯВЛЕНИЕ
AI-Colab — это не просто система ИИ-агентов.
Это организационная модель мышления, реализованная в коде.
Логи хранят факты.
Промпты определяют роли.
Протоколы обеспечивают взаимодействие.
Gemini интерпретирует состояние.
Человек принимает решения.

Если все архитектурные инварианты соблюдены, система обладает свойствами:

    ✅ Deterministic — воспроизводима по логам
    ✅ Auditable — полностью наблюдаема
    ✅ Recoverable — восстанавливается после сбоев
    ✅ Extensible — масштабируема без пересмотра основ