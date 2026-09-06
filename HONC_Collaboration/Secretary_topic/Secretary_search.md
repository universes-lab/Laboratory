ТЗ: Закрываем тему Claude Desktop. 
Вместо этого надо ответить на четыре разных вопроса:
A. Endpoint layer: каким способом реально обращаться именно к существующим долгоживущим веб-чатам и получать их новые ответы?
B. Control-plane layer: какие готовые проекты уже дают durable task/message state, identity, audit, replay, timers и permissions?
C. Progressive disclosure / isolation: чем можно технически обеспечить метаданные отдельно от BODY и выдавать интеллектуальному слою только необходимое?
D. Human control room: какие готовые средства способны визуализировать одновременно organizational graph и workflow/provenance graph из внешнего хранилища состояния?
I. gemini.google
Для реализации описанной мультиагентной федеративной системы (где автономный Control Plane оркестрирует работу сторонних Web-чатов и сервисов без прямого раскрытия контекста) ниже представлен детальный архитектурный и стек-анализ по всем четырём слоям.
A. Endpoint layer: Реальное обращение к существующим веб-чатам
Поскольку ни OpenAI, ни Google, ни Anthropic, ни DeepSeek не предоставляют официального API для прямой адресации существующих UI-чатов пользователя, на этом слое применяются 3 практических паттерна:
1. CDP-Attach (Chrome DevTools Protocol к действующему браузеру)
Механика: Браузер (Chrome/Edge) запускается с флагом --remote-debugging-port=9222. Скрипт (Playwright/Puppeteer/Python-PyCDP) подключается к уже запущенному экзекутору без пересоздания профиля.
Адресация: Навигация по прямым URL чатов:
ChatGPT: [https://chatgpt.com/c/](https://chatgpt.com/c/){chat_id}
Gemini: [https://gemini.google.com/app/](https://gemini.google.com/app/){chat_id}
DeepSeek: [https://chat.deepseek.com/a/chat/s/](https://chat.deepseek.com/a/chat/s/){chat_id}
Claude: [https://claude.ai/chat/](https://claude.ai/chat/){chat_id}
Ввод/Извлечение: Вместо ненадежного поиска по CSS-селекторам применяется паттерн DOM MutationObserver + Clipboard Injection:
Текст вставляется через native clipboard API (navigator.clipboard.writeText) или эмуляцию ввода в contenteditable / textarea.
Нажатие на кнопку отправки (или Enter).
Ожидание завершения ответа детектируется не по секундомеру, а через MutationObserver на дереве DOM (отслеживание исчезновения класса streaming / появлении атрибута data-is-streaming="false" / остановки роста текстового нода).
Считывание ответа: Извлечение innerText последнего элемента ответа (div[data-message-author-role="assistant"]:last-child или его аналога).
2. Local Proxy / Extension Interception
Механика: Браузерное расширение (Custom Chrome Extension) инжектируется в сессию. Расширение перехватывает внутренние WebSocket или XHR/Fetch вызовы чатов (например, SSE-потоки /backend-api/conversation).
Плюсы: Не зависит от изменений визуальной верстки (CSS-классов), так как перехватывает структурированные JSON/SSE события напрямую из сетевого стека браузера.
Минусы: Требует постоянной актуализации логики декодирования внутренних приватных API.
3. Native OS GUI Automation (Computer Use / PyAutoGUI)
Механика: Claude Computer Use API или локальные инструменты эмуляции ОС (PyAutoGUI / Windows Automation UI).  
ZTABS
Применение: Резервный канал на случай агрессивных защиты от ботов (Cloudflare, CAPTCHA), когда браузерный WebSocket блокируется.
B. Control-plane layer: Готовые движки оркестрации и состояния
Для управления графами задач, долгоживущими таймерами, репраем, аудитом и ролевым доступом используются проверенные производственные платформы оркестрации процессов:
1. Temporal (Temporal.io) — Золотой стандарт
Durable Task / State: Вся логика записывается как обычный код (TypeScript, Python, Go), но состояние любой переменной, циклических таймеров и await-ожиданий автоматически сохраняется в БД (Event Sourcing).
Replay & Audit: Встроенный журнал событий (History) хранит каждый шаг. При сбое сервера процесс возобновляется с той же точки execution.
Timers: Поддержка нативных таймеров (включая задержки на дни/месяцы) без расхода CPU.
Permissions/Identity: Интеграция с OIDC/OAuth2 и mTLS.
2. Apache Airflow / Prefect / Dagster
Применение: Отлично подходят, если граф задач является строго направленным ациклическим графом (DAG) с упором на пакетную обработку данных и пайплайны.
Сравнение: Prefect / Dagster лучше приспособлены под события реального времени и dynamic task generation, чем классический Airflow.
3. Zeebe (Camunda 8)
Применение: Движок стандартизированного BPMN 2.0. Если маршруты сообщений и утверждения должны проектироваться визуально бизнес-аналитиками.
Особенности: Встроенная поддержка визуального графа workflow out-of-the-box, аудит и встроенный IAM/RBAC.
C. Progressive disclosure / isolation: Изоляция содержимого (BODY) от Диспетчера
Чтобы оркестратор (Claude / Control Plane) видел только маршрутные данные и не получал чувствительное содержимое сообщений в промпт, применяются следующие паттерны:
1. Envelope Pattern (Конвертная адресация)
Сообщение разделяется на две структуры:
Envelope Metadata (передается Диспетчеру):
JSON
{
  "envelope_id": "env_992384",
  "sender_agent_id": "ChatGPT_Architect",
  "target_agent_id": "DeepSeek_Coder",
  "target_chat_url": "https://chat.deepseek.com/a/chat/s/abc-123",
  "payload_ref": "s3://secure-bucket/payloads/env_992384.enc",
  "payload_hash_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
  "status": "QUEUED"
}
Payload Body (хранится изолированно): Исходное тело сообщения помещается в зашифрованное локальное хранилище или S3. Диспетчер получает только payload_ref и payload_hash_sha256.
2. Zero-Data-Access MCP / Worker Executability
При вызове MCP-инструмента отправки Claude указывает:
send_message(envelope_id="env_992384")
Локальный Worker (MCP-сервер):
Вычитывает зашифрованное тело из payload_ref.
Вставляет его в DOM/API целевого чата.
Получает ответ от целевого чата.
Записывает этот ответ в новое хранилище s3://secure-bucket/payloads/env_992385.enc.
Возвращает Диспетчеру (Claude) только статус и ссылку:
{"status": "SUCCESS", "new_envelope_id": "env_992385"}.
3. Deterministic Policy Engine (OPA — Open Policy Agent)
Для проверки прав (can Agent A send to Agent B?) применяется OPA. Диспетчер запрашивает OPA-сервер:
opa_eval(sender="ChatGPT", target="Gemini", action="send") -> ALLOW / DENY.
Диспетчер выполняет логику только на основе бинарного ответа OPA.
D. Human control room: Средства визуализации Organizational Graph и Workflow Provenance
Для одновременного представления мета-графа структуры компании/агентов и реального графа исполнения потоков данных используются готовые open-source и enterprise решения:
1. React Flow / Svelte Flow (Кастомные UI-панели)
Применение: Стандарт де-факто для построения интерактивных систем управления агентами.
Преимущества: Позволяет легко рендерить составные узлы (Nodes) с динамическими статусами, подсветкой активных ребер (Edges), отображением метрик доставки в реальном времени и кликабельным просмотром Envelope Metadata.
2. Temporal UI / Camunda Operate (Готовые панели оркестраторов)
Temporal Web UI: Из коробки показывает полный Provenance Graph процесса execution, таймлайны вызовов, статус репраев и стек ошибок без необходимости писать фронтенд.
Camunda Operate: Визуализирует выполнение процессов на нативной BPMN-схеме с тепловыми картами (Heatmaps) задержек на узлах.
3. Apache Atlas / OpenLineage + Marquez (Data & Agent Provenance)
Применение: Специализированные фреймворки для отслеживания происхождения данных (Data Provenance & Lineage).
Назначение: Позволяют визуализировать полный граф того, какой агент создал пакет, через какие промежуточные ноды и трансформеры он прошёл, и кто является финальным получателем.
II. kimi
Собрано достаточно данных. Отвечаю по четырём слоям.
A. Endpoint Layer: доступ к существующим долгоживущим веб-чатам
Общий вывод
Ни один из крупных сервисов не предоставляет официального API для обращения к уже существующим веб-чатам. Все публичные API создают изолированные сессии. Единственные реальные пути — reverse engineering или browser automation, оба нестабильны и нарушают Terms of Service.
По сервисам
Table
Сервис	Официальный API к существующему чату	Реальные (неофициальные) пути	Статус
ChatGPT	❌ Нет	Reverse-engineered endpoints (/backend-anon/f/conversation, /backend-api/conversation) — проекты типа realasfngl/ChatGPT эмулируют браузер, решают Turnstile/PoW, работают через sessionKey 	Нестабильно; Atlas (standalone browser) закрывается 9 августа 2026 
Claude.ai	❌ Нет	Claude Explorer — сторонний проект, использует Playwright + mitmproxy для перехвата sessionKey, затем ходит в chat_conversations API Anthropic и скачивает историю локально. MCP-сервер позволяет новой сессии Claude читать архив 	Только чтение/архивирование, не живой двусторонний доступ
Gemini	⚠️ Частично	Interactions API (beta, май 2026) — previous_interaction_id позволяет продолжать server-side сессию, но это API-взаимодействия, а не доступ к gemini.google.com веб-чату. Хранение: 55 дней (paid) / 1 день (free)  	API-native, не веб-чат
DeepSeek	❌ Нет	Нет известных reverse-engineering проектов для chat.deepseek.com. API (deepseek-v4-pro, deepseek-v4-flash) — только новые сессии 	Нет пути
Практическая рекомендация
Если задача — писать и читать в существующий долгоживущий чат, единственная рабочая техника — browser automation (Playwright/Puppeteer) с авторизацией через cookies/session storage. Но:
Ломается при каждом обновлении UI
Требует обхода anti-bot (Turnstile, Arkose, PoW)
Нарушает ToS всех сервисов
Не масштабируется
Альтернатива: не пытаться подключиться к чужим чатам, а строить собственные долгоживущие сессии поверх API каждого сервиса, синхронизируя историю в собственном хранилище.
B. Control-Plane Layer: durable state, identity, audit, replay, timers, permissions
Workflow / Task Orchestration (durable execution)
Table
Проект	Durable State	Replay	Timers	Identity	Audit	Permissions	Примечание
Temporal	✅ Event History	✅ Deterministic replay	✅ Workflow.sleep	⚠️ Через Activity	✅ Event History + UI	⚠️ RBAC в Enterprise	Золотой стандарт durable execution. Требует отдельный кластер  
Inngest	✅ Step memoization	✅ Resume from step	✅ step.waitForEvent	⚠️ Через event payload	⚠️ Через логи	✅ Concurrency, throttling, idempotency	Встраивается в существующее приложение, не требует отдельной инфраструктуры  
Hatchet	✅ Durable event log	✅ Replay from checkpoint	✅ Sleep / event wait	⚠️ Через task context	⚠️ Через логи	⚠️ Через policies	Durable tasks с runtime-выбором ветвлений 
Restate	✅ Durable log + keyed state	✅ Journaled replay	✅ Timers	✅ Virtual objects (keyed)	✅ Durable log	⚠️ Через policies	Log-first runtime, state materialization 
Trigger.dev	✅ Checkpoint/resume	✅ Resume	✅ Waits	⚠️ Через task	⚠️ Через логи	⚠️ Через policies	Отдельно развёрнутые таски, self-hosted опция 
Bernstein	✅ .sdd/ state	✅ Replay journal	⚠️ Через адаптер	⚠️ Через адаптер	✅ HMAC-chained audit log	⚠️ Через адаптер	Специфичен для coding agents, но архитектура универсальна: lineage spine + deterministic scheduler 
Identity, Permissions, Audit
Table
Проект / Стандарт	Что даёт	Примечание
Open Policy Agent (OPA)	Policy-as-code, fine-grained authorization	Стандарт для cloud-native, но не встроен в workflow engines напрямую
Keycloak / ZITADEL	Identity, SSO, RBAC	Для human + service account identity
Coworker.ai	Runtime permissions, short-lived scoped tokens, attested audit trails	«Policy guards that evaluate business rules at runtime...attested audit trails with who approved what and why» 
Pactvera	Evidence-grade immutable audit (blockchain-sealed)	Для high-stakes workflows: ChainIT ID + MFA + VDT + Touch Audit 
AWS CloudTrail + S3 Object Lock	Infrastructure audit + WORM retention	Для AWS-native governance 
Вывод по Control-Plane
Для AI-оркестрации наиболее зрелый стек: Temporal или Inngest для durable execution + OPA/ZITADEL для identity + Bernstein-подход (HMAC audit log, lineage spine) для audit. Если нужен лёгкий self-hosted вариант — Hatchet или Restate.
C. Progressive Disclosure / Isolation: метаданные отдельно от BODY
1. Progressive Disclosure в AI-агентах
Концепция уже применяется: вместо загрузки всех tool definitions в контекст, агент видит только Layer 1 — Discovery (имя + описание), затем Layer 2 — Activation (инструкции), затем Layer 3 — Execution (полные данные). Это снижает token usage и ограничивает контекст .
2. Протокольный уровень: AGNTCY SLIM (IETF Draft)
SLIM (Secure Low-Latency Interactive Messaging) — draft от февраля 2026, специально для агентов:
Data plane маршрутизирует сообщения только по metadata (без чтения BODY)
Session layer — MLS-based E2EE для BODY
Control plane — оркестрация routing nodes 
Это прямой ответ на ваш вопрос: routing nodes видят envelope metadata, но не content.
3. Secure Enclaves / TEE
Для изоляции интеллектуального слоя от данных:
Intel TDX / AMD SEV-SNP / ARM CCA — Confidential VMs
NVIDIA H100 CC — GPU memory isolation
Intel SGX — process-level enclaves для credential material, prompt handling
Применение: model weights, KV-cache, tool-call isolation, persistent memory confidentiality .
4. Envelope Encryption + Content-Addressable Storage
Архитектура:
plain
Envelope = { metadata: открытый, body_cid: <hash>, body: encrypted }
Маршрутизатор видит metadata + CID, но не BODY
BODY хранится в content-addressable storage (IPFS-like, или локальный CAS)
Расшифровка — только у получателя (E2EE)
Ограничение: E2EE защищает content, но metadata (sender, recipient, timestamps) остаются видимыми для routing infrastructure .
5. MCP: скрытие tool result от модели (перспектива)
Обсуждение в Anthropic (#1197) описывает FileContent type для tool results, который не попадает в LLM context, а хранится в «virtual filesystem inside the client's session». На август 2026 это еще не реализовано в стандарте MCP, но является запланированным направлением .
6. Bernstein-подход: state вне agent memory
Bernstein хранит состояние в .sdd/ директории вне памяти агента. Orchestrator (Python code, zero LLM tokens) принимает решения на основе этого состояния, а агенты только исполняют задачи. Это физическое разделение control plane от data plane .
Вывод по Isolation
Технически возможно построить транспорт, где интеллектуальный слой видит только metadata:
SLIM — на уровне протокола (data plane vs session layer)
Envelope + CAS — на уровне архитектуры (CID вместо content)
TEE — на уровне hardware (enclave для sensitive data)
Bernstein model — на уровне оркестратора (state вне LLM)
D. Human Control Room: визуализация org graph + workflow/provenance graph
Готовые платформы
Table
Платформа	Org Graph	Workflow/Provenance	Внешнее хранилище	Примечание
AgentCenter	✅ Agent roles	✅ Task state, execution traces	✅ API-first	«Mission control dashboard», framework-agnostic, $14/мес 
Netskope AI Command Center	✅ AI assets / identities	✅ Risk correlation, data access maps	✅ External	Запущен июнь 2026. Active control surface, не passive report 
Noma Agent Access Control	✅ Agent discovery	✅ Per-agent boundaries, enforcement logs	✅ External	Запущен июнь 2026. Runtime policy monitoring 
Microsoft Conductor	⚠️ YAML-defined	✅ Task graph, parallel groups, web dashboard	✅ YAML + external	CLI + web dashboard, MIT license 
Bernstein	⚠️ Через адаптеры	✅ Task graph inspection (browser view), lineage spine	✅ .sdd/ directory	TUI + browser view для task graph и diffs 
LeafMesh	✅ AI-Org (PODs)	✅ Workflow orchestration graph	✅ External	«Compose your AI-Org in YAML; govern every action from LeafMesh» 
ChartHop	✅ HR org chart (live HRIS sync)	⚠️ Workforce planning scenarios	✅ Workday, BambooHR, ADP	Для людей, не агентов, но с timeline slider и scenario modeling 
Библиотеки для кастомной визуализации
Если нужно строить свой control room поверх внешнего хранилища состояния:
Table
Библиотека	Что визуализирует	Подключение к внешнему state
React Flow	Node-based graphs (workflow, org)	Любое API/WS
Cytoscape.js	Large-scale network graphs	Любое API
D3.js	Custom provenance/lineage	Любое API
Rete.js	Visual programming / agent workflows	Любое API
Provenance / Lineage (научные/индустриальные)
AVOCADO — визуализация workflow-derived data provenance с hierarchical + motif-based aggregation. Концепция применима к AI-оркестрации 
OpenLineage / Marquez / DataHub — data lineage для ETL, но адаптируемы для agent workflow lineage
Архитектура Control Room
Рекомендуемый паттерн (август 2026):
plain
Внешнее хранилище состояния (Temporal/Event Sourcing/CAS)
           ↓
    Graph API (org + provenance)
           ↓
    React Flow / Cytoscape.js (frontend)
           ↓
    WebSocket/SSE (real-time updates)
Ключевые фичи, которые уже реализованы в лидерах:
Live execution traces (как в AgentCenter, Netskope)
Exception routing по контексту (не только severity)
Decision attribution (кто/когда/почему)
Human-in-the-loop gates 
Итог по D
Если нужен готовый продукт — AgentCenter ($14/мес) или Netskope AI Command Center (enterprise). Если нужен open-source — Microsoft Conductor (MIT) или Bernstein (Apache-2.0) с их task graph inspection. Если нужна кастомная визуализация поверх собственного хранилища — React Flow + Cytoscape.js + OpenLineage для provenance.
4. Enterprise Observability: LangSmith / Arize Phoenix / Helicone
Назначение: Специализированный трейсинг мультиагентных систем. Позволяют видеть граф вызовов агентов, задержки, статус передачи метаданных и аудиторский след каждого шага.
===



===
ЧАСТЬ ВТОРАЯ
ОТ: Методолог
КОМУ: Независимому Поисковику
ТЕМА: Discovery Phase — существующие решения для Organizational Control Plane AI-коллаборации
Нужна независимая техническая разведка, без проектирования нашей системы и без подгонки ответа под уже обсуждавшиеся нами инструменты.
Контекст задачи: у нас существует коллаборация из нескольких долгоживущих AI-чатов разных платформ и ролей. Сейчас человек вручную переносит между ними сообщения, следит, кто кому должен ответить, какие обсуждения завершены, какие решения приняты и какие ветви работы из них возникли. Мы исследуем, какие уже существующие open-source проекты, официальные механизмы, стандарты или готовые компоненты могут снять эту нагрузку.
Искомая система условно состоит из четырёх функциональных областей:
Endpoint access — обращение именно к существующим долгоживущим AI-чатам и получение их новых ответов. Интересуют ChatGPT, Claude, Gemini, DeepSeek и локальные модели. Проверять API, desktop connectors/extensions, CLI, browser automation и другие реально существующие способы.
Organizational control plane — хранение ролей/участников, задач, маршрутов, статусов, таймеров, ожиданий, истории выполнения, восстановления после сбоев и происхождения задач/решений.
Message / knowledge isolation — возможность разделять организационные метаданные и содержимое сообщения: центральный координатор должен уметь знать кто → кому → статус → маршрут, не обязательно получая BODY в свой модельный контекст. Здесь же интересуют progressive disclosure, skills, permissions, sandboxing, envelope/payload separation и близкие механизмы.
Human control room — визуальное представление живой коллаборации: участники и рабочие группы, движение задач/сообщений, ожидания и блокировки, происхождение ветвей решений, состояние процессов. Желательно без обязательного раскрытия содержимого сообщений. 
Отдельно ищите системы, решающие координацию коллективного обсуждения: несколько независимых ответов → ожидание всех требуемых участников → синтез/проверка → решение → следующий раунд. Нас интересует не «multi-agent debate» как генерация ответа внутри одного фреймворка, а управление уже существующими независимыми участниками и длительными рабочими процессами.
Что именно искать
Не ограничивайтесь заранее известными названиями. Ищите по классам решений:
agent harness / control plane;
durable workflows / orchestration;
multi-agent coordination;
message bus / mailbox for agents;
human-in-the-loop workflow;
agent registry / identity / routing;
task provenance / decision provenance;
persistent sessions / replay;
progressive disclosure / agent skills;
AI operations dashboards / graph visualization;
browser/desktop automation для существующих AI-чатов;
connectors/extensions, которые могут работать с уже существующими чатами или пользовательскими сессиями.
Если встретятся Zero, AutoContext, Agent Skills, Temporal, SLIM, MCP и т.п. — проверить их наравне с другими, не считать заранее предпочтительными.
Для каждого найденного кандидата укажите только:
что это за проект/стандарт;
какую из четырёх областей он реально закрывает;
что именно подтверждено документацией или кодом;
чего он не закрывает;
можно ли использовать его как отдельный строительный блок;
зрелость: production / активно развивается / эксперимент;
лицензия, если open source;
ссылка на официальный сайт, документацию и GitHub.
Особенно отмечайте случаи, когда популярное описание проекта расходится с тем, что реально делает репозиторий.
Что сейчас НЕ делать
Не предлагать итоговый стек.
Не писать архитектуру нашей системы.
Не выбирать «лучший фреймворк».
Не давать пошаговый план реализации.
Не проектировать SQLite-схемы, workflow, adapters или SPEC.
Не считать отсутствие найденного решения доказательством, что решения не существует.
Ключевой исследовательский вопрос
Какие уже существующие технологии могут закрыть отдельные функции локального organizational control plane для коллаборации долгоживущих независимых AI-чатов, а какие функции пока остаются действительно специфическими и потребуют собственной разработки?
Формат результата
Сначала короткое резюме на 1–2 страницы: какие классы решений реально существуют и где находятся главные пробелы.
Затем сравнительная таблица:
Candidate | Endpoint | Control Plane | Isolation | Human Control Room | Deliberation | Maturity | Main gap | Sources
В конце — раздел «Что стоит исследовать вторым, прицельным поиском»: не ответы и не проекты реализации, а максимум 5–7 вопросов, которые стали ясны только после проведённой разведки.
===
I. gemini.google
Discovery Phase — существующие решения для Organizational Control Plane AI-коллаборацииКороткое резюме (1.5 страницы)На текущий момент (август 2026 года) рынка единого коробочного решения, которое бы «из коробки» связывало внешние веб-чаты (ChatGPT, Gemini, Claude.ai, DeepSeek), организовывало между ними оркестрацию процессов, скрывало тело сообщений от центрального координатора и визуализировало граф решений в едином Human Control Room, не существует.Однако инфраструктурный ландшафт содержит зрелые, готовые для использования блоки по каждой из четырех областей.               +-----------------------------------------------------+
               |             Human Control Room (UI Layer)           |
               |     (React Flow / Temporal UI / OpenLineage)        |
               +--------------------------+--------------------------+
                                          | Metadata / Events
                                          v
               +-----------------------------------------------------+
               |        Organizational Control Plane (State/Tasks)    |
               |       (Temporal.io / Zeebe / Microsoft Agent Framework)|
               +-------------+-------------------------+-------------+
                             | Envelope                | Execution
                             v                         v
+---------------------------------------------------+  +-----------------------------------+
|     Message / Knowledge Isolation (Envelope Bus)   |  |   Endpoint Access (Connectors)    |
| (MCP-JSON Payload Ref Store / Masumi Agent Inbox) |  | (CDP Playwright MCP / Local API)  |
+---------------------------------------------------+  +-----------------------------------+
1. Реальное состояние 4 функциональных областейEndpoint Access (Обращение к долгоживущим веб-чатам)  Ни один вендор (OpenAI, Anthropic, Google, DeepSeek) не предоставляет официального API или протокола для прямой адресации существующих UI-чатов с их веб-историей.Работающее решение: CDP (Chrome DevTools Protocol) + Playwright MCP. Подключение к уже запущенному браузеру пользователя с сохраненной сессией, навигация по URL чата (/c/{id}) и асинхронный перехват ответов через MutationObserver.Пробел: Отсутствие официальной стабильности. Любое изменение CSS/DOM-структуры веб-чатов требует обновления селекторов или логики перехвата.  Organizational Control Plane (Состояние, роли, маршруты, возобновление)Работающее решение: Индустриальные engines оркестрации Temporal.io и Zeebe (Camunda 8), а также специализированные агентурные фреймворки Microsoft Agent Framework (MAF) и Open Multi-Agent (OMA). Они обеспечивают Event Sourcing, таймеры (до месяцев), возобновление работы после сбоев (Replay) и контроль цепочки задач.Пробел: Ни один из этих движков «не понимает» спецификацию веб-чатов: они оперируют вызовами функций/агентов через код или REST/gRPC.  Message / Knowledge Isolation (Разделение Meta и Body, Progressive Disclosure)Работающее решение: Паттерн Envelope / Payload Ref Separation, стандартизированный поверх Model Context Protocol (MCP), а также протоколы зашифрованных почтовых ящиков агентов (Masumi Agent Messenger).Механика: Координатор получает только метаданные {"envelope_id", "sender", "recipient", "payload_ref": "s3://..."}. Вызов передачи исполняется изолированным Worker'ом без отправки текста в контекст координатора.Пробел: Нет единого стандарта декларативного ограничения вычитывания тела ответа при коллективном обсуждении: скрытие контекста сейчас обеспечивается архитектурно на уровне кода MCP-инструмента.  Human Control Room (Визуализация графа организации и процессов)Работающее решение: Графовые UI-библиотеки (React Flow), штатные панели оркестраторов (Temporal Web UI / Camunda Operate) и специализированные системы Provenance & Lineage (OpenLineage / Marquez / Semantica).Пробел: Готовые UI отображают либо граф выполнения задач (DAG/Workflow), либо граф происхождения данных (Data Lineage). Связка «Организационный граф ролей + Живой граф сообщений без демонстрации их тела» создается комбинацией React Flow поверх метаданных Control Plane.Deliberation (Коллективное обсуждение и синтез)Работающее решение: Реализуется паттернами Fan-Out / Fan-In (Barrier Synchronization) в Temporal/MAF или консенсусными проверками в Open Multi-Agent (OMA).Механика: Движок приостанавливает выполнение ветви (Suspend/Wait) до тех пор, пока от всех указанных сторонних чатов (ChatGPT, Gemini и т.д.) не поступят сигналы о готовности Envelope Metadata.Сравнительный анализ кандидатовНиже представлен анализ существующих проектов, протоколов и фреймворков.CandidateEndpointControl PlaneIsolationHuman Control RoomDeliberationMaturityMain gapSourcesPlaywright MCP / Browser MCPДа (CDP/DOM)НетЧастичноНетНетActiveНе обеспечивает состояние задач, зависит от устойчивости DOM браузеровGitHubTemporal.ioНетДа (Durable Event Sourcing)Да (Data Converter)Частично (Workflow UI)Да (Signals, Join/Barriers)ProductionНе содержит агентурных сущностей и адаптеров к веб-чатамTemporal Docs / GitHubMicrosoft Agent Framework (MAF)НетДа (Graph Workflows)ЧастичноНетДа (Group Collaboration)ProductionЗавязан на API-вызовы моделей, а не на интерфейсы внешних UI-чатовGitHubOpen Multi-Agent (OMA)НетДа (Dynamic Task DAG)ЧастичноЧастично (Offline Viewer)Да (Consensus)ActiveРассчитан на Node.js/TS и работу с API-моделямиGitHubMasumi Agent MessengerНетЧастично (Mailbox/Threads)Да (E2E Encrypted Payload)Частично (TUI / Web Inbox)НетActiveНе оркестрирует логику DAG, только хранит и доставляет сообщенияGitHubModel Context Protocol (MCP)Частично (Tools)НетДа (Schema / JSON-RPC)НетНетActive (Standard)Это протокол взаимодействия, а не сервер оркестрации или база состоянийAnthropic / MCP SpecSemanticaНетЧастично (Decision Records)ЧастичноДа (Context Graph UI)Частично (Causal Audit)ActiveФреймворк графов знаний, а не оркестратор реального времениGitHubOpenLineage + MarquezНетНетДа (Metadata-only)Да (Lineage Graph UI)НетProductionРазработан для ETL/Data Pipeline, требует адаптеров под события AI-чатовOpenLineage / GitHubReact Flow / Svelte FlowНетНетN/AДа (UI Framework)НетProductionБиблиотека компонентов визуализации UI, требует backend-данныхReact Flow WebПодробный разбор кандидатов по компонентам1. Playwright MCP Server / Browser MCP Server  Что это: MCP-серверы, предоставляющие инструментарий автоматизации Chromium/Firefox через Chrome DevTools Protocol (CDP).  Область: Endpoint access.Подтверждено кодом/документацией: Подключение к запущенному браузеру с флагом --user-data-dir / --remote-debugging-port=9222, сохранение авторизованных сессий, навигация, считывание DOM-дерева, отправка событий кликов и текста.Чего НЕ закрывает: Не хранит историю задач, не занимается маршрутизацией.Строительный блок: Идеальный изолированный адаптер нижнего уровня для работы с UI-чатами (ChatGPT, Gemini, Claude, DeepSeek).  Зрелость / Лицензия: Активно развивается / MIT / Repos: microsoft/playwright-mcp, ricardodeazambuja/browser-mcp-server.  2. Temporal.ioЧто это: Платформа оркестрации с моделью Durable Execution (Event Sourcing).  Область: Organizational Control Plane, Deliberation.Подтверждено кодом/документацией: Таймеры на неограниченный срок, гарантированное восстановление состояния после перезапусков, механизмы Signals и Queries для коллективного ожидания (Fan-In/Barrier), кастомный Data Converter для шифрования/сокрытия тела payload.Чего НЕ закрывает: Не имеет готовности к работе с промптами, AI-агентами или DOM браузеров из коробки.Строительный блок: Главный промышленный движок для устойчивого хранения состояния и графа задач.Зрелость / Лицензия: Production / MIT / Site: temporal.io, GitHub: temporalio/temporal.3. Microsoft Agent Framework (MAF)  Что это: Open-source фреймворк (.NET / Python) от Microsoft для создания и оркестрации распределенных агентурных систем.  Область: Organizational Control Plane, Deliberation.Подтверждено кодом/документацией: Графовые паттерны оркестрации (sequential, concurrent, handoff, group collaboration), контроль версионности, чекпоинты, Human-in-the-loop контроллеры.  Чего НЕ закрывает: Работает через API LLM и direct function calling. Не имеет адаптеров к внешним Web-чатам.Строительный блок: Да, как готовая кодовая база структуры управления агентурным графом.Зрелость / Лицензия: Production / MIT / GitHub: microsoft/agent-framework.4. Masumi Agent MessengerЧто это: Открытый протокол и шина сообщений (Mailbox) для асинхронной коммуникации независимых AI-агентов.  Область: Message / Knowledge Isolation.Подтверждено кодом/документацией: Уникальные стабильные адреса агентов (slugs), сквозное E2E-шифрование сообщений на клиенте, разделение данных на открытые заголовки и закрытый payload, поддержка режимов подтверждения человеком.Чего НЕ закрывает: Не содержит бизнес-логику оркестрации DAG или принятия решений.Строительный блок: Независимый сервис асинхронных почтовых ящиков для агентов.Зрелость / Лицензия: Активно развивается / Open Source / GitHub: masumi-network/masumi-agent-messenger.  5. SemanticaЧто это: Графовая инфраструктура для фиксации происхождения решений (Decision Provenance) и причинно-следственного аудита.  Область: Human Control Room, Isolation.Подтверждено кодом/документацией: Построение Context Graph и Knowledge Graph без обязательного участия LLM, интерактивный веб-интерфейс для инспекции связей и хронологии принятых решений.Чего НЕ закрывает: Не управляет исполнением задач или отправкой сообщений в чаты.Строительный блок: Отдельный модуль аудита и отображения причинно-следственного графа.Зрелость / Лицензия: Активно развивается / Open Source / GitHub: semantica-agi/semantica.  Ответ на ключевой исследовательский вопросГотовые технологии (Что НЕ нужно писать с нуля):Durable Task / Message State & Recovery: Полностью закрывается платформой Temporal.io или Zeebe. Написывание собственной базы состояний, таймеров и логики повторов задач не требуется.Асинхронный транспорт с изоляцией тела: Закрывается паттерном MCP JSON-RPC + S3/Local Blob Store или готовым шифрованным транспортом Masumi Agent Messenger.Low-level Browser Connector: Закрывается Playwright MCP с флагом сохранения пользовательского профиля.Графовая отрисовка UI: Закрывается библиотекой React Flow / Svelte Flow.  Специфические функции (Требующие собственной разработки / адаптации):DOM-Mutation Parsers под внешние чаты: Написание и поддержка специфических скриптов-парсеров для забора/отправки сообщений в веб-интерфейсы ChatGPT, Claude, Gemini, DeepSeek без нарушения работы при изменении верстки.Envelope Middleware Adapter: Прослойка между Control Plane и MCP, которая отсекает BODY от ответа внешнего чата, сохраняет его в Blob Store, а в Temporal отправляет исключительно Envelope Metadata.Унифицированный UI Human Control Room: Связка представления "Граф участников + Граф выполнения Temporal + Метаданные конвертов" в единый дашборд оператора.Что стоит исследовать вторым, прицельным поискомМеханика устойчивого перехвата ответов через MutationObserver и WebSocket Interception:Какие существующие open-source решения для анализа сети (Chrome DevTools Protocol network domain) позволяют перехватывать потоковые SSE/WebSocket ответы от ChatGPT, Gemini, Claude и DeepSeek до их рендеринга в DOM-дереве?Стандартизация Envelope Spec в MCP:Существуют ли общепринятые спецификации или протоколы расширения MCP (MCP Tool Extensions), предназначенные исключительно для возврата payload_reference вместо передачи данных в content ответа инструмента?Связка Temporal Data Converter с локальным Blob Storage:Какова наименее ресурсоемкая практика настройки Temporal Data Converter для полного маскирования/вынесения тела аргументов за пределы Event History сервера Temporal?Интеграция React Flow с Event Sourcing историями:Есть ли готовые паттерны или библиотеки-адаптеры, преобразующие историю событий Temporal (Event History JSON) напрямую в формат графа узлов и связей React Flow (nodes и edges)?  Паттерны обхода капчи и авторизационных замков при долгоживущих CDP-сессиях:Каковы реальные технические ограничения и опыт использования фоновых Chrome-процессов под Windows при длительной (длиннее нескольких суток) непрерывной работе с вкладками веб-чатов?
===
II. kimi (ЗАмечание Автора: К этим жлобам его разработчикам больше обращаться не буду - жадность плещет через край!)
Discovery Phase: Существующие решения для Organizational Control Plane AI-коллаборации
Резюме (1–2 страницы)
Что реально существует
Разведка выявила чёткое разделение экосистемы на слои, но почти все существующие решения ориентированы на одного разработчика, строящего мульти-агентную систему внутри одного фреймворка. Ваша задача — оркестрация уже существующих независимых AI-чатов — оказалась на стыке нескольких классов решений, и ни один из них не закрывает её целиком.
Классы решений, которые реально существуют и зрелы:
Durable Workflow Engines (Temporal, Inngest, Restate, Trigger.dev) — зрелые open-source системы для отказоустойчивого выполнения долгоживущих процессов. Они дают: checkpointing, replay после сбоев, human-in-the-loop паузы, таймеры на дни/недели. Но это generic execution engines, не специфичные для агентов, и не решают routing между независимыми участниками.
Agent Orchestration Frameworks (LangGraph, CrewAI, Microsoft Agent Framework, OpenAI Agents SDK, Google ADK, Claude Agent SDK) — дают stateful graphs, role-based crews, conversation loops, tool calling. Но это frameworks: «пиши своих агентов внутри моей структуры». Они не управляют внешними существующими чатами.
Agent Control Planes / Harnesses (Guild AI, OpenHands Enterprise, Exemplar) — появились в 2025–2026 как ответ на необходимость fleet-level governance. Дают: centralized credentials, policy enforcement, audit trails, cost attribution, sandboxing. Но это либо коммерческие продукты (Guild AI, Exemplar), либо заточены под coding-агентов (OpenHands).
Communication Protocols (A2A, MCP) — A2A (Agent-to-Agent Protocol, Linux Foundation, Apache 2.0) — единственный реальный open стандарт для межагентного взаимодействия. Даёт Agent Cards (identity + capabilities), task lifecycle, streaming, async push, input-required states. Критически: сохраняет opacity — агенты не делятся internal memory. MCP (Model Context Protocol) — стандарт для подключения инструментов, не для межагентной коммуникации; с июля 2026 стал полностью stateless.
Observability & Tracing (Langfuse, AgentOps, LangSmith, Arize Phoenix) — зрелые системы для capture traces LLM-вызовов, tool calls, sessions. Langfuse — MIT, self-hostable. Но это ретроспективная observability, не живой control room для коллаборации.
Workflow Automation Platforms (n8n) — source-available, self-hosted, визуальный canvas, native AI Agent nodes, 500+ интеграций. Может служить скелетом control plane, но это low-code инструмент, не специфичный для агентской коллаборации.
Главные пробелы
Endpoint Access к существующим долгоживущим чатам — это самый тяжёлый пробел. Официальные API (OpenAI, Anthropic, Google, DeepSeek) — stateless: вы сами храните историю, и они не связаны с веб-чатами, которые ведёт человек. Browser automation (Playwright, Puppeteer) теоретически возможна, но нет готового стабильного решения для программного чтения/записи в существующие сессии chatgpt.com, claude.ai, gemini.google.com. Расширения типа Claude Conversation Exporter дают только односторонний экспорт. Opera Neon MCP Connector позволяет подключить внешнего агента к браузеру, но это не доступ к уже существующему чату.
Message / Knowledge Isolation — A2A даёт separation на уровне протокола (Agent Cards = metadata, Tasks = payload), но нет готовой реализации «центральный координатор видит envelope, но не видит body». Progressive disclosure, envelope/payload separation, sandboxing на уровне сообщений — это архитектурные паттерны, которые придётся реализовывать самостоятельно поверх A2A или custom message bus.
Human Control Room для живой коллаборации — не существует open-source продукта, который визуализирует: кто из N независимых агентов ответил, кто заблокирован, какая ветка решения откуда выросла, какие таймеры ожидания активны. Есть workflow UI (Temporal, n8n), есть trace UI (Langfuse), но нет «карты коллаборации» с участниками, задачами, блокировками и provenance ветвей в реальном времени.
Deliberation / Collective Discussion Coordination — нет готового open-source решения для паттерна: «несколько независимых ответов → ожидание всех → синтез → решение → следующий раунд». AutoGen/MS Agent Framework реализует debate внутри одного фреймворка. A2A имеет task lifecycle, но не специфичен для deliberation. Это придётся строить самостоятельно.
Task / Decision Provenance — существует только академическая работа PROV-AGENT (расширение W3C PROV), которая предлагает схему для lineage агентских решений. Готовой production-системы для отслеживания provenance решений, принятых в коллаборации нескольких агентов, нет.
Сравнительная таблица
Таблица
Candidate	Endpoint	Control Plane	Isolation	Human Control Room	Deliberation	Maturity	Main gap	Sources
Temporal	❌ (generic)	⚠️ (durable execution, HITL, retries)	❌	⚠️ (Temporal UI — technical workflow view)	❌	Production / зрелый (Uber-originated, MIT)	Не знает про агентов; требует deterministic code; нет routing/registry	temporal.io, GitHub
Inngest	❌ (generic)	⚠️ (durable steps, event-driven, HITL)	❌	⚠️ (dashboard для runs)	❌	Production / зрелый (4K+ stars, open source)	Не агент-специфичен; нет identity/routing	inngest.com, GitHub
Restate	❌ (generic)	⚠️ (durable execution, virtual objects, exactly-once)	❌	⚠️ (basic UI)	❌	Активно развивается (1.x, SDK MIT, runtime BSL)	Очень молодой; нет агент-специфичных примитивов	restate.dev, GitHub
Trigger.dev	❌ (generic, но AI-native)	⚠️ (durable tasks, HITL waitpoints, checkpointing, queues)	❌	⚠️ (run tracing dashboard)	❌	Активно развивается (16K+ stars, MIT)	TypeScript-only; нет cross-agent routing; нет registry	trigger.dev, GitHub
LangGraph	❌ (framework)	⚠️ (stateful graphs, checkpointing, time-travel)	❌	⚠️ (LangSmith — proprietary)	⚠️ (multi-agent patterns внутри graph)	Production (34% enterprise adoption, MIT)	Framework, не control plane; требует писать агентов внутри; тесная связь с LangChain	langchain.com, GitHub
CrewAI	❌ (framework)	⚠️ (role-based crews, task delegation)	❌	❌	⚠️ (crew collaboration)	Production (52K+ stars, open source)	Framework; нет durable execution; нет checkpointing на уровне продакшена	crewai.com, GitHub
A2A Protocol	⚠️ ( Agent Cards, task lifecycle, async)	⚠️ (discovery, identity, routing via Agent Cards)	✅ (opacity by design, envelope/payload separation на уровне спецификации)	❌	⚠️ (task delegation, input-required)	Production-ready v1.0 (Linux Foundation, Apache 2.0, 150+ orgs)	Нет reference implementation control plane; нет deliberation-специфичных примитивов	a2aproject.org, GitHub
MCP	❌ (tools protocol)	❌	❌	❌	❌	Production (stateless с июля 2026, Linux Foundation)	Это протокол для инструментов, не для агентов; не даёт routing/isolation между агентами	modelcontextprotocol.io, GitHub
Guild AI	❌	✅ (control plane: routing, credentials, approvals, audit, SIEM)	⚠️ (credentials isolation)	⚠️ (observability)	❌	Production (коммерческий, SDK открыты)	Коммерческий продукт; не open-source целиком; не про существующие чаты	guild.ai
OpenHands Enterprise	❌ (coding agents)	✅ (orchestration, sandboxing, cost attribution, plugin marketplace)	⚠️ (sandboxed execution)	⚠️ (observability, audit)	❌	Production (72K+ stars, open core)	Заточен под coding-агентов; не про коллаборацию независимых чатов	openhands.dev, GitHub
n8n	⚠️ (HTTP Request, webhook nodes)	⚠️ (visual workflow, AI Agent node, queues)	❌	⚠️ (visual canvas для workflows)	❌	Production (230K+ users, fair-code)	Не агент-специфичен; нет durable execution для долгих ожиданий; нет provenance	n8n.io, GitHub
Langfuse	❌	❌	❌	⚠️ (trace explorer, session grouping)	❌	Production (MIT, self-hostable)	Только observability; нет orchestration/control	langfuse.com, GitHub
AgentOps	❌	❌	❌	⚠️ (session replay, cost tracking)	❌	Production	Proprietary; только observability	agentops.ai
MCP Gateway & Registry	❌	⚠️ (tool registry, auth, routing)	⚠️ (OAuth, access control)	❌	❌	Эксперимент / ранняя (open source)	Реестр инструментов, не агентов; FastAPI + nginx	GitHub
PROV-AGENT	❌	❌	❌	❌	❌	Академический прототип	Только схема provenance; нет production системы	arXiv
Opera Neon MCP Connector	⚠️ (подключает внешних AI к браузеру)	❌	❌	❌	❌	Production ($19.90/mo)	Не даёт доступа к существующим чатам; создаёт новые browser-сессии	opera.com/neon
Легенда: ✅ — реально закрывает область | ⚠️ — частично или требует доработки | ❌ — не закрывает
Детальные карточки кандидатов
Temporal
Что это: Durable execution engine, originated at Uber (Cadence fork). MIT license.
Закрывает: Control Plane (частично) — durable workflows, human-in-the-loop, retries, timers на годы, replay после сбоев.
Подтверждено: History-based replay; 7 официальных SDK; OpenAI использует для Codex; документация по AI-агентам от Google (Gemini + Temporal).  
Не закрывает: Endpoint access; message isolation; human control room; deliberation. Не агент-специфичен.
Строительный блок: Да — как durable execution layer под custom control plane.
Зрелость: Production (самый зрелый в классе).
Ссылки: temporal.io | GitHub
A2A Protocol
Что это: Open standard для межагентного взаимодействия (Google → Linux Foundation). Apache 2.0.
Закрывает: Isolation (opacity by design — агенты не делятся internal memory); Control Plane (частично) — Agent Cards (identity, capabilities, cryptographic verification), task lifecycle, discovery, routing.
Подтверждено: JSON-RPC 2.0 over HTTP; Agent Cards; streaming (SSE) и async push; input-required states; 150+ организаций; SDK на Python, Go, JS, Java, .NET, Rust.  
Не закрывает: Endpoint access к существующим чатам; human control room; deliberation-специфичные примитивы. Нет reference implementation полноценного control plane.
Строительный блок: Да — как communication/routing layer.
Зрелость: Production-ready v1.0 (апрель 2026).
Ссылки: a2aproject.org | GitHub
OpenHands Enterprise Agent Control Plane
Что это: Open-source platform (72K+ stars) для coding agents + Enterprise control plane.
Закрывает: Control Plane (orchestration, sandboxed execution, observability, audit, cost attribution, plugin marketplace/skills).
Подтверждено: Workflows across repos; sandboxed execution; every conversation logged; cost tracking at org/user/conversation level.  
Не закрывает: Endpoint access к внешним чатам; message isolation; deliberation. Заточен под software engineering.
Строительный блок: Частично — можно позаимствовать идеи sandboxing и audit, но не готовый блок.
Зрелость: Production (open core).
Ссылки: openhands.dev | GitHub
Trigger.dev
Что это: Open-source (MIT) AI-native durable workflow platform, TypeScript.
Закрывает: Control Plane (частично) — durable tasks, queues, retries, checkpointing, human-in-the-loop (waitpoints), real-time streaming, no timeouts.
Подтверждено: v3 с chat agent API; needsApproval: true для HITL; atomic versioning; browser/Python/FFmpeg в tasks.  
Не закрывает: Endpoint access; cross-agent routing/registry; message isolation; human control room для коллаборации.
Строительный блок: Да — как durable execution + HITL layer.
Зрелость: Активно развивается (16K+ stars).
Ссылки: trigger.dev | GitHub
LangGraph
Что это: Graph-based agent orchestration framework от LangChain team. MIT.
Закрывает: Control Plane (частично) — stateful graphs, checkpointing, time-travel debugging, human-in-the-loop interrupts, subgraph composition.
Подтверждено: Checkpointers (Postgres, Redis, SQLite); 34% enterprise adoption; используется Anthropic, Replit, LinkedIn, Uber.  
Не закрывает: Endpoint access; framework-agnostic control plane (требует писать агентов внутри LangGraph); message isolation; deliberation между независимыми участниками.
Строительный блок: Да — если агенты пишутся внутри LangGraph, но не для внешних чатов.
Зрелость: Production (v1.0 GA).
Ссылки: langchain.com/langgraph | GitHub
n8n
Что это: Source-available workflow automation platform (fair-code), self-hostable.
Закрывает: Control Plane (частично) — visual workflow canvas, AI Agent node с ReAct loop, 500+ integrations, queues, Git sync.
Подтверждено: Native AI Agent node; multi-agent routing; self-hosted бесплатно; execution-based pricing.  
Не закрывает: Endpoint access к существующим чатам; durable execution для долгих ожиданий (нет native checkpointing на уровне продакшена); message isolation; provenance; deliberation.
Строительный блок: Да — как visual workflow + integration layer.
Зрелость: Production (230K+ users).
Ссылки: n8n.io | GitHub
Guild AI
Что это: Commercial agent control plane (framework-agnostic).
Закрывает: Control Plane — routing, credentials isolation, approvals, audit logs, SIEM integration, policy enforcement.
Подтверждено: «One of the few products that treats agent control plane as a first-class problem»; credentials externalized; causality logging. 
Не закрывает: Endpoint access; message isolation (нет envelope/payload separation); human control room; deliberation. Коммерческий, не полностью open source.
Строительный блок: Нет — коммерческий продукт, не отдельный блок.
Зрелость: Production.
Ссылки: guild.ai
Langfuse
Что это: Open-source (MIT) LLM/agent observability platform, self-hostable (ClickHouse-based).
Закрывает: Human Control Room (частично) — trace explorer, session grouping, cost attribution, agent graph visualization.
Подтверждено: OpenTelemetry-native; 60+ framework integrations; self-hosted требует 5+ сервисов.  
Не закрывает: Endpoint access; control plane; message isolation; deliberation. Только observability.
Строительный блок: Да — как tracing/observability layer.
Зрелость: Production.
Ссылки: langfuse.com | GitHub
MCP Gateway & Registry (agentic-community)
Что это: Open-source MCP Gateway + Registry (FastAPI + nginx + MongoDB).
Закрывает: Control Plane (частично) — tool registry, auth (OAuth/OIDC), dynamic discovery, routing; A2A discovery.
Подтверждено: nginx reverse proxy (data plane) + FastAPI registry (control plane); Keycloak/Entra integration; handles A2A discovery. 
Не закрывает: Endpoint access; message isolation; human control room; deliberation. Это реестр инструментов, не агентов.
Строительный блок: Да — как registry/auth layer.
Зрелость: Эксперимент / ранняя.
Ссылки: GitHub
Что стоит исследовать вторым, прицельным поиском
Существуют ли неофициальные или community-driven проекты для программного доступа к веб-чатам ChatGPT/Claude/Gemini через reverse-engineering их internal API? (Например, проекты типа poe-api, chatgpt-api 2023-2024, но актуальные на 2026.) Поиск по классам: «unofficial ChatGPT API», «Claude web API reverse engineering», «chatgpt.com internal API», «claude.ai websocket».
Есть ли готовые open-source реализации «message bus with envelope/payload separation» специфично для агентов? Поиск по: «agent mailbox», «agent message queue envelope», «secure multi-agent message bus», «agent communication layer with metadata routing».
Существуют ли open-source проекты для «collective deliberation» или «structured multi-agent discussion» за пределами AutoGen? Поиск по: «multi-agent deliberation framework», «structured agent debate», «consensus building AI agents», «round-robin agent discussion», «synthesis from multiple agent outputs».
Какие именно browser automation инструменты (Playwright, Puppeteer, Browser Use, Skyvern) могут работать с аутентифицированными сессиями существующих AI-чатов, и насколько они хрупки к изменениям UI? Поиск по: «Browser Use authenticated session», «Playwright ChatGPT automation», «Puppeteer Claude.ai login», «headless browser AI chat automation 2026».
Есть ли готовые open-source компоненты для «human control room» — визуализации живых workflow с участниками, блокировками, таймерами? Поиск по: «workflow visualization dashboard open source», «real-time collaboration dashboard», «human-in-the-loop control room», «process mining visualization open source», «agent fleet dashboard».
Какова реальная зрелость и производительность Restate vs Temporal для долгоживущих агентских workflow? Поиск по: «Restate production use case», «Restate vs Temporal long-running workflow», «Restate virtual objects agent».
Существуют ли готовые интеграции A2A с существующими чат-платформами (ChatGPT, Claude, Gemini) или A2A применим только к «агентам как сервисам»? Поиск по: «A2A ChatGPT integration», «A2A Claude agent», «A2A consumer chat platforms».
===
III. perplexity.ai
Discovery Phase: существующие решения
Краткое резюме
На рынке уже существуют зрелые компоненты для надёжного исполнения долгоживущих процессов, маршрутизации сообщений, доступа к API моделей, браузерной автоматизации, аудита и визуализации трасс. Однако готовой системы, которая одновременно управляет несколькими уже существующими долгоживущими чатами ChatGPT, Claude, Gemini и DeepSeek как независимыми участниками, не обнаружено.
Главный результат разведки: четыре функциональные области закрываются технологиями разного класса.
Endpoint access достаточно хорошо закрывается официальными API для новых программных сессий, локальными API и браузерной автоматизацией для пользовательских веб-сессий.
Organizational control plane наиболее полно обеспечивают durable workflow-системы, прежде всего Temporal. Они имеют персистентное состояние, ожидания, таймеры, сигналы, retries, task queues, replay и восстановление после сбоев.
temporal
+1
Message / knowledge isolation частично поддерживается A2A, MCP, Agent Skills и SLIM. A2A специально допускает взаимодействие между непрозрачными агентами без раскрытия их внутренней памяти и инструментов; MCP разделяет host, client и server и предоставляет resources, prompts и tools. Но ни один из этих протоколов сам по себе не гарантирует разделение организационного envelope и содержимого payload в требуемом смысле.
modelcontextprotocol
+1
Human control room существует преимущественно как observability-инструмент: Langfuse, OpenTelemetry-совместимые системы, отдельные dashboards и agent-control projects. Они хорошо показывают traces, spans, DAG и выполнение, но обычно не дают полноценной операционной модели живой коллаборации с участниками, ожиданиями, блокировками, ветвлением решений и выборочным сокрытием BODY.
opentelemetry
+1
Отдельно важное различие:
A2A — протокол связи между независимыми агентами, а не durable coordinator.
MCP — протокол подключения модели к tools/resources, а не шина координации рабочих групп.
Agent Skills — формат динамически загружаемых инструкций и ресурсов, а не система маршрутизации или управления состоянием.
Temporal — durable execution engine, но не endpoint-адаптер для ChatGPT/Claude Web и не визуальная карта содержательной дискуссии.
LangGraph — persistent graph execution и human-in-the-loop для графов, которые вы сами строите, но не управляющая система для произвольных внешних долгоживущих чатов.
Playwright — реальный способ подключиться к уже открытым авторизованным браузерным сессиям, но это низкоуровневый механизм автоматизации, а не устойчивый адаптер конкретных AI-платформ.
playwright
Наиболее специфический и пока плохо закрытый слой — это совместное управление существующими пользовательскими чатами разных платформ. Официальные API обычно создают отдельные программные взаимодействия и не дают универсального доступа к истории конкретного consumer-чата. Браузерная автоматизация может работать с уже открытыми сессиями, cookies и вкладками, но остаётся хрупкой относительно изменений UI, CAPTCHA, MFA, rate limits и политик сервисов.
Вторая специфическая область — операционная семантика коллективного обсуждения: «ожидать всех обязательных участников», определить quorum, различать timeout и отказ, собрать ответы, провести synthesis/verification, зафиксировать decision и породить следующий раунд. Temporal и A2A дают необходимые примитивы, но не готовую доменную семантику такой дискуссии.
Сравнительная таблица
Candidate	Endpoint	Control Plane	Isolation	Human Control Room	Deliberation	Maturity	Main gap	Sources
Temporal	Нет специализированных AI-chat endpoints; внешние API вызываются через Activities	Сильная сторона: durable state, retries, task queues, signals, timers, replay и recovery	Может хранить metadata отдельно от payload, но схема разделения задаётся приложением	Есть visibility по workflow execution, но не готовая карта AI-коллаборации	Даёт primitives для fan-out, wait, quorum, timeout и rounds; не задаёт semantics debate	Production; open source, MIT	Нет готовых адаптеров к существующим ChatGPT/Claude Web-сессиям и полноценного control-room UI	
temporal
+1
A2A Protocol	Да, если участник предоставляет A2A endpoint; Agent Card описывает capabilities	Task lifecycle, long-running tasks, status, artifacts, push/streaming	Сильная сторона: агенты могут оставаться opaque, не раскрывая memory/tools/internal state	Только протокольные события и статусы; UI не входит в стандарт	Поддерживает делегацию и long-running tasks, но не collective quorum/synthesis protocol	Активно развивается; Apache-2.0	Большинство consumer AI-чатов не являются A2A servers; нет общего registry/control room/provenance store	
developers.googleblog
+1
MCP	Подключает LLM host к tools, resources и prompts; может быть мостом к локальным или внешним системам	Нет workflow scheduler, durable task manager или registry участников	Resources/tools/prompts и consent-модель дают основу для ограниченного раскрытия данных	Нет собственного операционного UI	Sampling и elicitation позволяют вложенные AI/human interactions, но не управляют коллективным обсуждением	Production standard; specification open, implementation licenses vary	Это agent-to-tool/context protocol, а не agent-to-agent control plane; не решает endpoint access к закрытым чатам	
modelcontextprotocol
+1
Agent Skills	Не endpoint-протокол; может быть поддержан конкретными клиентами и SDK	Нет хранения задач, таймеров, маршрутов и истории выполнения	Сильная сторона — progressive disclosure: metadata → SKILL.md → references/scripts/assets	Нет	Может формализовать роль, процедуру synthesis или review внутри агента	Активно развивается; опубликован как open standard; лицензирование зависит от реализации	Не обеспечивает изоляцию организационного metadata от фактически переданного message body и не управляет внешними чатами	
anthropic
SLIM	Messaging transport для агентов, людей и tools; request-response, pub/sub, streaming	Даёт транспортный слой, routing и secure messaging, но не workflow state machine	Encryption, trust boundaries и routing; семантическое разделение envelope/payload нужно определить выше	Нет готовой control-room визуализации	Может переносить сообщения для deliberation, но не реализует quorum/synthesis/decision rounds	Активно развивается; Apache-2.0 reference implementation; spec CC-BY-4.0	Transport не равен организационному control plane; зрелость и совместимость экосистемы ещё формируются	
github
+2
LangGraph	API/model calls через узлы и tools; не подключает автоматически произвольные долгоживущие внешние чаты	Checkpoints, graph state, durable execution, interrupts и resume	State можно разделять по узлам/графам, но политика visibility задаётся разработчиком	Есть graph/debugging и human interrupts, но не независимый operational cockpit	Хорошо моделирует fan-out/fan-in, review и iterative rounds внутри собственного graph runtime	Production-oriented; open source, MIT	Управляет графом, который вы создали; не является универсальным координатором уже существующих chat sessions	
github
+1
Agent Zero	Dockerized desktop, browser и tools; может взаимодействовать с сайтами через UI	Есть agent runtime и extensible skills, но не полноценный durable organizational scheduler	Container/desktop isolation; не специализированная message/payload governance	Есть live desktop interaction, но не multi-team control room	Может быть участником или исполнительным агентом, не коллективным coordination engine	Активно развивается; open source, лицензия должна проверяться в репозитории перед использованием	Сильнее как автономный agent harness, чем как координатор независимых долгоживущих участников	
github
Playwright / Playwright MCP / CLI	Реально подключается к существующим Chrome/Edge tabs, cookies, extensions и авторизованным сессиям через CDP или extension	Нет durable orchestration, task registry или recovery semantics	Browser contexts позволяют разделять cookies/storage; это техническая изоляция, не semantic data isolation	Может предоставлять screenshots/snapshots, но не collaboration dashboard	Только исполняет scripted interaction; deliberation отсутствует	Production-grade automation tooling; open source, Apache-2.0	UI changes, authentication, anti-bot controls и отсутствие официальной семантики chat messages делают адаптеры хрупкими	
playwright
+1
Claude Platform API / Managed Agents / Sessions	Официальные Messages API, Agents API, Sessions API; sessions имеют stateful event stream	Внутри Claude platform есть managed sessions/agents, но не cross-provider coordinator	Skills, environments и managed sandboxes дают provider-specific isolation	Usage monitoring и platform operations, но не общий cockpit нескольких AI-платформ	Возможны long-running Claude sessions, но не collective independent-participant protocol	Production API; отдельные Sessions/Agents/Skills функции обозначены как beta в найденной документации	Закрывает Claude, но не ChatGPT/Gemini/DeepSeek; отдельный API session не равен существующему Claude.ai consumer chat	
platform.claude
Langfuse	Инструментирует приложения и agent frameworks; не обращается к чатам сам	Хранит traces/observations и позволяет анализировать execution	Поддерживает разные уровни записи, включая возможность не сохранять inputs/outputs или хранить content externally	Agent graph view показывает агрегированный и фактически исполненный DAG	Визуализирует уже записанную deliberation, но не запускает quorum или rounds	Production-oriented; open source core, лицензирование компонентов необходимо проверять по репозиторию	Observability, а не control plane: не маршрутизирует задачи и не ждёт участников	
langfuse
+1
OpenTelemetry GenAI semantic conventions	Не endpoint; стандарт телеметрии для model/agent/tool calls	Не хранит и не исполняет workflow; задаёт vocabulary для traces/metrics/events	Документация допускает не записывать content либо хранить его отдельно и ссылаться на него	Даёт основу для внешнего dashboard, но не UI	Может фиксировать causal chain, tasks, agents и handoffs, но не управляет ими	Standard активно развивается; GenAI conventions имеют Development status	Семантические conventions не являются task database, scheduler или provenance graph store	
opentelemetry
+2
Mission Control	Зависит от подключённого agent runtime; не является универсальным ChatGPT/Claude/Gemini connector	Self-hosted dispatch, workflows, agent registry/operations и cost monitoring по описанию проекта	Skills scanning и workspace conventions, но степень message-body isolation требует проверки кода	Сильная сторона — dashboard/mission-control presentation	Может координировать workflows своего runtime; подтверждение collective deliberation для независимых external chats не найдено	Молодой проект; actively developing; лицензия и production claims нужно проверять в репозитории	Популярное описание шире подтверждённой совместимости: это control UI для определённой agent ecosystem, не neutral cross-provider plane	
github
OpenAgents	Указывает discovery, MCP и A2A connectivity; endpoint compatibility зависит от конкретных adapters	Claims identity, discovery, network orchestration и deployment	AgentID/provenance/trust claims; concrete isolation semantics требуют проверки реализации	Не найдено подтверждение полноценного live control room	A2A delegation/collaboration, но не подтверждён collective deliberation coordinator	Активно развивается; open source, license следует подтвердить в репозитории	Marketing-level full-stack claims нужно отделять от реально реализованных APIs и interoperability matrix	
openagents
Conductor	Browser-first, CLI, MCP, webhooks и coding-agent runtime	Durable ideas around task surface, local config, worktrees и sessions	Isolated git worktrees и execution sessions; не general message/body isolation	Browser dashboard и control endpoints	Parallel coding-agent workflows, но не arbitrary multi-platform chat deliberation	Активно развивается; license/production maturity требуют проверки	Domain-specific orchestration around code repositories, не neutral collaboration plane	
conductross
Agent Control	Интегрируется через SDK/decorator с agent applications	Runtime policy layer: allow, deny, steer, warn	Policy enforcement and governance, not necessarily payload segregation	Governance/operations visibility заявлена, но full collaboration graph не подтверждён	Может вмешиваться в шаги workflow, не координирует debate rounds	Активно развивается; Apache-2.0	Policy control не равен durable orchestration или endpoint adapter	
agentcontrol
AutoContext	Harness-oriented; endpoint capabilities зависят от underlying agent	Self-improving harness, inspection и skill export; durable organizational state не подтверждён	Progressive-disclosure skill export, но не coordinator-level isolation	Нет подтверждения human control room	Помогает агенту улучшать выполнение, а не управлять коллективом независимых чатов	Эксперимент / actively developing; license нужно проверить в репозитории	Название и описание могут создавать впечатление context-control plane, но найденный код прежде всего harness/skill tooling	
github
Endpoint access
Официальные API
Официальные API хорошо подходят для сценария, в котором coordinator сам создаёт и сохраняет программные conversations. Они хуже подходят для требования «обратиться именно к уже существующему долгоживущему чату пользователя».
Claude предоставляет Messages API, а также Agents и Sessions API; документация отдельно описывает stateful sessions, event stream, skills и environments. Это полноценный provider-specific программный endpoint, но найденные материалы не подтверждают универсальную работу с произвольным уже существующим Claude.ai conversation.
platform.claude
Для ChatGPT, Gemini и DeepSeek следует разделять:
API вызов модели.
API-managed assistant/agent session.
consumer web-chat, открытый пользователем в браузере.
Это разные объекты с разными идентификаторами, историей и политиками доступа. Наличие API модели само по себе не означает наличие официального API для чтения и продолжения конкретного пользовательского чата.
Browser automation
Playwright документированно умеет подключаться к уже работающему Chromium-браузеру через CDP или расширение, использовать существующие tabs, cookies и installed extensions. Это делает его реальным endpoint-механизмом для веб-чатов, включая сценарий «человек уже вошёл в систему».
playwright
Но Playwright предоставляет действия браузера, а не устойчивую модель сообщений. Adapter должен сам определять:
как обнаружить новый assistant response;
как отличить streaming от завершённого ответа;
как получить conversation/thread identifier;
как восстановиться после reload или изменения DOM;
как избежать повторной отправки;
как безопасно работать с MFA, CAPTCHA и rate limits.
Поэтому browser automation — полезный отдельный строительный блок, но не готовое решение endpoint access.
Локальные модели
Локальные модели обычно дают наиболее контролируемый endpoint: HTTP API, OpenAI-compatible API, CLI или inference server. Однако это не означает автоматически наличие долгоживущего chat-session semantics. Историю, session identity, replay и ownership часто должен предоставлять внешний runtime или само приложение.
Control plane и коллективное обсуждение
Temporal — наиболее зрелый найденный общий примитив для этой области. Он сохраняет состояние workflow, поддерживает durable timers, signals, retries, task queues и replay после отказа. Документация прямо описывает ожидание human input на дни или месяцы, escalation по таймеру и восстановление после рестарта Worker.
temporal
+1
Для требуемого паттерна:
отправить запрос нескольким участникам;
ждать заданное множество ответов;
обработать timeout и partial failure;
передать результаты synthesis/review;
зафиксировать decision;
породить следующий round;
у Temporal имеются необходимые технические механизмы. Но semantics «обязательный участник», «quorum», «решение принято», «ветвь создана из решения» являются прикладной логикой, а не встроенной функцией Temporal.
LangGraph способен выразить похожую логику в виде graph state и checkpointed super-steps. Его documentation подтверждает durable execution, human-in-the-loop и доступ к прошлым checkpoints для inspection, modification и time travel. Но его естественный объект управления — собственный граф исполнения, а не внешний реестр независимых долгоживущих чат-сессий.
github
+1
A2A ближе к требуемой межагентной модели, чем большинство agent frameworks. Он определяет Agent Card, task lifecycle, long-running tasks, artifacts и работу с opaque agents. В официальном репозитории подчёркивается, что агент может сотрудничать без раскрытия internal state, memory или tools.
github
Тем не менее A2A предполагает, что участник предоставляет A2A-compatible server. ChatGPT Web, Claude.ai, Gemini Web и DeepSeek Web не становятся A2A endpoints только потому, что их можно автоматизировать браузером.
Isolation и progressive disclosure
A2A
A2A является наиболее прямым стандартным примером операционной видимости без раскрытия внутреннего содержания участника. Клиент видит task, status и artifacts, а remote agent может сохранять свою внутреннюю память и инструменты непрозрачными.
github
Это близко к требованию «кто → кому → статус → маршрут» без обязательного доступа coordinator к полному BODY. Но A2A не предписывает, что coordinator должен получать только envelope, и не задаёт универсальную политику доступа к каждому фрагменту payload.
MCP
MCP разделяет host, client и server, а protocol features включают resources, prompts, tools, sampling, roots и elicitation. Спецификация подчёркивает consent, user control и то, что host должен контролировать передачу данных server-у.
modelcontextprotocol
Это полезная основа для selective disclosure, но MCP не является изолированным mailbox protocol. Вызов tool может передать содержимое, если host/client это разрешит. Сам протокол не превращает payload separation в обязательную организационную гарантию.
Agent Skills
Agent Skills реализует наиболее чётко документированный progressive disclosure:
при старте доступны только name и description;
полный SKILL.md читается при необходимости;
references, scripts и assets загружаются дополнительно и по требованию.
Это снижает контекстную нагрузку и даёт переносимый способ упаковки ролей, процедур и локальных знаний.
anthropic
Но progressive disclosure не равен security isolation. Если клиент или агент имеет разрешение прочитать полный skill или reference, Skill format сам по себе не предотвращает это. Также Skills не хранит task state, не маршрутизирует сообщения и не ведёт decision provenance.
OpenTelemetry
OpenTelemetry GenAI conventions особенно интересны как механизм ссылки на BODY вместо его обязательной записи. В документации указаны варианты не записывать instructions/inputs/outputs либо хранить content externally и помещать в span только reference.
github
Это важное подтверждение технической возможности metadata/content separation в observability layer. Но conventions являются словарём телеметрии, а не механизмом доступа. Нужны внешние storage и authorization rules.
Human control room
Готовый универсальный control room для независимых cross-provider AI-чатов не найден.
Langfuse показывает agent graphs как агрегированный или фактически исполненный DAG, если в trace есть подходящие observations или используется LangGraph integration. Это полезно для visualizing execution, но graph строится из телеметрии уже работающего приложения.
langfuse
OpenTelemetry даёт vendor-neutral основу для traces, metrics и events, включая agent/task/handoff concepts, однако официальные GenAI conventions всё ещё развиваются. Это хороший interoperability layer для будущих dashboards, но не само dashboard-приложение.
opentelemetry
+1
Mission Control, Conductor и ClawPort-подобные проекты показывают emerging class self-hosted operational dashboards: agent registry, task dispatch, cost monitoring, cron/failure views, browser UI и workspace state. Но найденные описания в основном относятся к конкретным runtimes, coding agents или OpenClaw-подобным экосистемам. Их нельзя автоматически считать neutral control room для ChatGPT/Claude/Gemini/DeepSeek.
Особенно важно отделять:
визуализацию traces от управления процессом;
kanban задач от task provenance;
список agents от identity federation;
dashboard runtime-specific agents от cross-provider endpoint layer.
Зрелость найденных классов
Production или близко к production
Temporal.
Playwright.
Официальные model APIs.
MCP implementations и ecosystem tooling.
LangGraph для собственных graph-based workflows.
Langfuse как observability platform.
Активно развиваются
A2A.
SLIM.
Agent Skills как cross-platform standard.
OpenTelemetry GenAI conventions.
Agent Control.
OpenAgents.
Mission Control.
Conductor.
Экспериментальные или требующие осторожной проверки
AutoContext.
проекты, заявляющие «control plane» только на основании dashboard для конкретного agent runtime;
browser connectors, которые используют внутренние, undocumented web endpoints вместо UI automation или официального API.
Что остаётся специфическим
На основании найденных источников наиболее вероятно, что собственной разработки потребуют именно следующие функции:
единый registry реальных участников, включая API agents, local models и browser-attached consumer chats;
стабильная идентичность конкретной долгоживущей chat session независимо от provider API или UI;
надёжная доставка сообщения с idempotency, deduplication и acknowledgement;
coordinator-level envelope/payload separation с per-participant authorization;
collective deliberation semantics: required participants, quorum, synthesis, verification, decision и next round;
единый provenance graph для задач, ответов, решений, производных ветвей и повторных попыток;
human control room, показывающий topology и status без обязательного раскрытия BODY;
cross-provider recovery после зависшего browser session, token expiration, UI change или частично выполненного запроса.
Это не означает, что каждый компонент придётся писать с нуля. Скорее, готовые технологии закрывают нижние слои — transport, workflow durability, browser control, telemetry, protocol envelopes — а специфический организационный слой пока не выглядит стандартизированным продуктом.
Что стоит исследовать вторым, прицельным поиском
Есть ли у ChatGPT, Claude.ai, Gemini и DeepSeek официальные или documented-but-less-visible механизмы чтения и продолжения именно существующих consumer chat sessions, включая session IDs, event streams и экспорт истории?
Какие реализации A2A уже поддерживают durable task persistence, push notifications, authentication, artifacts и task history на уровне production, а не только демонстрационного SDK?
Может ли SLIM использоваться как транспорт с отдельными routing headers и encrypted payloads так, чтобы relay видел envelope, но не содержимое сообщения?
Какие open-source проекты реализуют именно quorum/barrier/fan-in semantics для независимых внешних agents, включая partial responses, deadline, cancellation и re-rounding?
Какие существующие observability backends поддерживают content references или redaction так, чтобы строить provenance graph без сохранения полного BODY?
Есть ли стандартизированный registry/identity layer, совместимый одновременно с A2A Agent Cards, MCP servers, local model endpoints и browser-attached sessions?
Какие browser-automation проекты имеют production-grade механизм обнаружения завершённого ответа, replay/idempotency и восстановление долгоживущего authenticated session для AI-chat UIs?
===
IV. Claude:
Discovery Phase: существующие решения для Organizational Control Plane AI-коллаборации
ОТ: Независимого Поисковика КОМУ: Методологу ТЕМА: Техническая разведка по четырём функциональным областям + координация коллективного обсуждения
1. Резюме
Ландшафт 2025–2026 годов даёт достаточно зрелые готовые блоки для трёх из четырёх областей — но ни один существующий проект не закрывает задачу целиком, и не существует ни одного проекта, который решал бы именно вашу конкретную проблему: координацию между уже существующими долгоживущими чатами на потребительских веб-интерфейсах (ChatGPT, Claude, Gemini как продукты, а не API-агенты).
Endpoint access. Официальных, поддерживаемых производителем способов "достучаться" именно до живого веб-чата (а не до API с чистого листа) крайне мало. Anthropic предлагает Claude in Chrome (браузерный агент) и Claude Tag (Slack-интеграция), но не официальный способ читать/писать в конкретный существующий чат программно. Для ChatGPT, Gemini, DeepSeek такого официального механизма тоже нет. Вся экосистема, которая решает именно эту задачу — браузерная автоматизация и "мосты" поверх пользовательской сессии: ai-browser-bridge, web-model-bridge, gpt-browser-api, unofficial-claude2-api, коммерческие расширения вроде HARPA. Это самый юридически и технически хрупкий слой всей системы: он завязан на неофициальные DOM-селекторы, нарушает буквальную букву ToS большинства провайдеров и ломается при любом редизайне интерфейса. Официальный API — это качественно другая вещь: он даёт устойчивый программный доступ, но не к тем чатам, которые уже видит человек в браузере, а к отдельным, новым сессиям (если только вы не переносите историю вручную).
Organizational control plane. Это единственная область, где индустрия по-настоящему консолидировалась вокруг зрелых движков. Temporal (Apache 2.0, production, спин-офф Cadence из Uber) — наиболее развитая платформа durable-execution: журналирование истории выполнения, replay после сбоя, сигналы, таймеры, длительные ожидания человека — всё то, что вы описываете как "таймеры, ожидания, восстановление после сбоев", покрывается нативно. Конкуренты — Prefect, Restate, Inngest, Temporal-подобный Dagster/Airflow 3.1 (последний получил нативные HITL-операторы только недавно). Ни один из них не имеет встроенной модели "участник AI-чата", "маршрут между чатами" или "происхождение решения" — это пришлось бы моделировать поверх их примитивов (workflow/activity/signal) самостоятельно.
Message / knowledge isolation. Здесь происходит настоящая генеральная уборка стандартов, начатая в 2025 году. MCP (Anthropic) решает isolation в первую очередь между агентом и инструментами/данными (sandboxing, permissions, context isolation через отдельные серверы), но не между "координатором" и "содержимым сообщения" в смысле вашей задачи — конверт/полезная нагрузка не разделены нативно в протоколе, это паттерн, который каждая реализация строит сама (MCP gateway с permission separation — пример стороннего надстроечного решения, а не части спецификации). Agent Skills (открытый стандарт Anthropic, декабрь 2025, ~26+ платформ-адоптеров) реализуют именно ту прогрессивную загрузку, о которой вы говорите: на старте в контекст попадает только заголовок/описание (~80–100 токенов), тело — только при активации, файлы — только при выполнении. Это архитектурно близко к тому, что нужно для "координатор знает статус, не видя BODY", но Skills спроектированы для загрузки инструкций, а не для маршрутизации сообщений между независимыми участниками — это смежная, а не тождественная задача. A2A (Google → Linux Foundation, Apache 2.0) даёт формальную модель задачи (task lifecycle: submitted → working → input-required → completed…) и Agent Card для описания возможностей, что близко к "маршрутам/статусам", но рассчитан на программных агентов с HTTP/JSON-RPC эндпоинтом, а не на людей, кликающих в веб-чате. SLIM/AGNTCY (Cisco → Linux Foundation) — транспортный/messaging-слой (pub-sub поверх gRPC, MLS-шифрование) для A2A/MCP, экспериментальная зрелость, отдельно от organizational-логики.
Human control room. Готовых визуальных "центров управления" именно для межплатформенной AI-коллаборации нет — вся экосистема observability (LangGraph Studio, Langfuse Agent Graphs, LangSmith, AgentOps) заточена под агентов, построенных на одном фреймворке (в первую очередь LangGraph), где граф известен заранее из кода. Они прекрасно визуализируют состояние выполнения и умеют не раскрывать полное содержимое (можно смотреть на структуру трейса без разворачивания payload), но не рассчитаны на "чужие", независимо управляемые долгоживущие чаты как узлы графа. Agent Inbox (LangChain) — ближайший аналог "человеческого рабочего стола ожиданий": inbox-подобный UI для approve/edit/reject прерываний, но опять же — только для LangGraph-агентов через их API прерываний, не универсальный.
Deliberation / коллективное обсуждение. Здесь важно разделить два непохожих класса, которые вы верно развели в задании. Первый класс — debate-внутри-одного-фреймворка (Semantic Kernel GroupChat, AutoGen, Microsoft Agent Framework RoundRobinGroupChatManager, DOVA, LLM committees с voting-раундами) — это генерация ответа, где сам фреймворк порождает и оркестрирует "участников". Он не подходит вам напрямую, но полезен как источник паттернов протокола (round-robin, unanimous-consensus, судья/chairman-синтез, hung-deliberation термination). Второй, более близкий к вашей задаче класс — оркестраторы существующих независимых конечных точек: Quorum-MCP — MCP-сервер, который параллельно опрашивает Claude/OpenAI/Gemini/Cohere/Mistral/Novita/локальные модели через их API, ждёт всех, затем проводит раунды cross-review и синтеза. Это структурно ближе всего к вашему "несколько независимых ответов → ожидание всех → синтез → решение", но (а) это API-модели, не веб-чаты с сохранённой историей и личностью участника, и (b) публично задокументированной зрелости проекта немного, нужно отдельно проверять состояние репозитория.
Provenance. Отдельно стоит выделить W3C PROV — устоявшийся (не AI-специфичный) стандарт для "кто/что/когда/из чего произошло", и его AI-надстройку PROV-AGENT (исследовательская работа 2025 г., расширяет PROV поверх MCP для трассировки решений агентов, entity/activity/agent модель). Это именно то структурное решение, которое покрывает "происхождение задач/решений" из вашего ТЗ — но это модель данных и научный прототип, а не готовый продукт с UI.
Главный вывод. Технологии, закрывающие инфраструктурные функции (durable state, таймеры, восстановление после сбоя, транспорт, sandboxing инструментов, progressive disclosure инструкций, W3C-провенанс-модель), существуют и зрелы. Технологии, закрывающие именно вашу предметную специфику — координацию не программных агентов-с-API, а людьми управляемых/просматриваемых долгоживущих веб-чатов разных вендоров, где "участник" не имеет native webhook/callback — не существуют как готовый продукт. Это тот самый зазор, который в конце обозначен как область для собственной разработки.
2. Сравнительная таблица
Candidate	Endpoint	Control Plane	Isolation	Human Control Room	Deliberation	Maturity	Main gap	Sources
Temporal	—	Полное покрытие: durable workflows, activities, signals, таймеры, replay-восстановление, история выполнения	Частично: разделение workflow (детерминированный код) / activity (недетерминированная работа с внешним миром) — архитектурная изоляция, не про payload/envelope	Встроенный Web UI показывает историю событий workflow, но это дебаг-инструмент разработчика, не операционная панель для нетехнического человека	Не является deliberation-фреймворком; можно реализовать поверх signals/queries	Production (спин-офф Cadence, используется Uber/NVIDIA/Gorgias)	Не знает про "AI-чат" как сущность; всё AI-специфичное (агенты, статусы, роли) моделируется руками поверх примитивов	temporal.io/solutions/ai; github.com/temporalio
Prefect	—	Durable execution, human-in-the-loop через pause_flow_run/suspend_flow_run, авто-генерируемые формы для ввода человека	Нет специальной модели isolation	Есть встроенная observability/UI (таймлайн задач, логи), ориентирован на разработчика	Нет	Production, open-source (Apache 2.0-подобная модель, "fork it, modify it")	Python-first DAG/flow-модель, не заточен под "чат как участник"; нет agent registry	prefect.io/prefect/open-source; prefect.io/solutions/agents
Airflow 3.1 (HITL-операторы)	—	Нативные ApprovalOperator, HitlOperator, HitlBranchOperator для пауз на решение человека	—	Airflow UI (DAG-граф), не заточен на AI-специфику	Нет	Production, HITL-часть — недавнее (конец 2025) дополнение, менее обкатанное	DAG (ацикличный) по природе — плохо ложится на итеративные/циклические AI-диалоги	medium.com (Sebastian, Airflow 3.1 HITL)
MCP (Model Context Protocol)	Частично: официальный способ подключать инструменты и источники данных к модели; НЕ способ подключаться к чужому существующему чату другого вендора	—	Ядро назначения протокола: sandboxing серверов, least-privilege для инструментов, разделение контекста между разными MCP-серверами	—	—	Production, широко принят индустрией (Anthropic, поддержан OpenAI/Google)	Isolation в MCP — это про модель↔инструмент, а не про координатор↔тело-сообщения между несколькими AI-чатами; "конверт против payload" в вашем смысле нужно строить сверху (см. паттерны MCP gateway/permission-separation у сторонних проектов)	modelcontextprotocol.io/specification; arxiv 2511.20920 (Securing MCP)
Agent Skills / SKILL.md (agentskills.io)	—	—	Прогрессивная трёхуровневая загрузка (discovery ~100 токенов → activation полного тела → execution файлов/скриптов) — прямое совпадение с "progressive disclosure" из ТЗ	—	—	Production, открытый стандарт с декабря 2025, ~26–40+ платформ-клиентов	Это механизм раскрытия инструкций для одного агента, а не маршрутизации сообщений между несколькими независимыми участниками; переносить его на межчатовую координацию — экстраполяция, не готовое решение	platform.claude.com/docs/agent-skills; agentskills.io
Agent2Agent (A2A)	Только для агентов с HTTP/JSON-RPC эндпоинтом (Agent Card на /.well-known/agent-card.json); не решает доступ к веб-чату ChatGPT/Claude/Gemini как к человеко-ориентированному продукту	Формальная модель task lifecycle (submitted/working/input-required/completed/failed/canceled/rejected) — прямое совпадение со "статусами/маршрутами"	Возможность заявлять capability через Agent Card, но не про изоляцию содержимого сообщения от координатора	—	Поддерживает делегирование подзадач между агентами, но не "ждать всех → синтез → раунд" из коробки	Production/активно развивается (Linux Foundation, Apache 2.0, 150+ организаций-сторонников)	Спроектирован для программных, API-доступных агентов разных вендоров, а не для координации людьми-управляемых долгоживущих веб-сессий	github.com/a2aproject/A2A; a2a-protocol.org; wikipedia Agent2Agent
SLIM / AGNTCY	—	—	Транспортный/messaging-слой для A2A/MCP: pub-sub, MLS-шифрование "точка-точка", но не решает вашу задачу envelope/payload на уровне организационных метаданных	—	—	Эксперимент/раннее развитие (IETF Internet-Draft, донирован в Linux Foundation в 2025)	Это низкоуровневый транспорт, а не organizational control plane; заявленная "agent observability" в AGNTCY выглядит скорее как roadmap-пункт, чем готовый продукт — нужно проверять репозиторий отдельно от пресс-релизов	github.com/agntcy/slim; ietf.org draft-mpsb-agntcy-slim; linuxfoundation.org press
PROV-AGENT / W3C PROV	—	—	—	—	—	W3C PROV — зрелый, устоявшийся стандарт (не AI-специфичный); PROV-AGENT — научная работа/прототип 2025 г., экспериментальная зрелость	Модель данных (entity/activity/agent) прямо соответствует "происхождению задач/решений" из ТЗ, но нет готового UI/хранилища "из коробки" — нужно реализовывать самим	arxiv.org/html/2508.02866; emergentmind.com provenance-tracking
LangGraph + LangGraph Studio + Langfuse Agent Graphs / LangSmith / AgentOps	—	LangGraph даёт state-персистентность, checkpoint/resume, встроенный HITL через interrupt — но только для агентов, построенных на самом LangGraph	—	Наиболее близкий к "человеческойконтрольной комнате" готовый визуальный инструмент: граф выполнения, инспекция состояния, time-travel/forking, работа без обязательного разворачивания каждого payload	—	Production/активно развивается (широко используемый open-source + коммерческие облачные надстройки)	Граф известен заранее из кода одного фреймворка; не подходит для узлов-"чужих чатов", чья внутренняя структура координатору не подконтрольна и не описана заранее	github.com/langchain-ai/langgraph; langfuse.com/docs/observability/agent-graphs; laminar.sh agent-observability-platforms
Agent Inbox (LangChain)	—	—	—	Gmail-подобный inbox UI именно для решений человека (accept/edit/respond/ignore) по прерываниям агентов	—	Активно развивается, open-source	Жёстко привязан к LangGraph deployment API; не универсальный "мультивендорный" inbox	github.com/langchain-ai/agent-inbox
Quorum-MCP	Опрашивает через официальные API нескольких провайдеров (Claude, OpenAI, Gemini, Cohere, Mistral, Novita, локальные Ollama-модели) параллельно	Режимы: quick_consensus (1 раунд), full_deliberation (3 раунда: независимый анализ → cross-review → синтез), devils_advocate	—	—	Наиболее прямое совпадение с "несколько независимых ответов → ожидание всех → синтез → решение → следующий раунд" из всех найденных кандидатов	Судя по описанию — недавний, вероятно экспериментальный/нишевый проект; нужна отдельная проверка активности репозитория и лицензии	Работает с API-моделями "с нуля", а не с уже существующими долгоживущими чатами, сохраняющими историю/личность участника; зрелость не подтверждена независимо	medium.com (Ageddes, "2500 hours") — вторичный источник, требует верификации по первоисточнику
ai-browser-bridge / web-model-bridge / gpt-browser-api / unofficial-claude2-api / HARPA	Единственный найденный класс решений, которые реально обращаются именно к существующей залогиненной веб-сессии ChatGPT/Claude/Gemini/DeepSeek и других, а не к отдельному API	—	—	—	—	Разброс: от активных open-source репозиториев (ai-browser-bridge, web-model-bridge) до расширений с коммерческой подпиской (HARPA) — ни один явно не production-grade для организационного использования	—	Юридически хрупко (нарушение ToS большинства провайдеров), технически хрупко (завязка на DOM/селекторы, ломается при редизайне), не даёт официальных гарантий доступности; это единственный практический путь к "существующим долгоживущим чатам", но с высоким операционным риском
Claude for Chrome / Claude Tag / Google Gemini in Chrome / ChatGPT Agent	Официальные, поддерживаемые вендорами браузерные/чат-интеграционные агенты — но они управляют браузером/Slack от имени модели, а не дают программный доступ координатору к содержимому существующего чата другого продукта	—	—	—	—	Production (официальные продукты вендоров)	Решают другую задачу: "AI действует в браузере/Slack", а не "внешний координатор читает/пишет в конкретный долгоживущий чат по расписанию"	claude.com product docs (см. также product_information в системном контексте); minded.com Best AI Browser Agents 2026
3. Что стоит исследовать вторым, прицельным поиском
Существуют ли у ChatGPT, Gemini или DeepSeek — помимо обычного chat-completions API — какие-либо полуофициальные механизмы продолжения именно ранее начатого пользователем диалога (например, "Projects"/"custom GPTs"/"Gems" с постоянным контекстом), доступные программно, а не только через веб-интерфейс?
Какова реальная (не рекламная) степень зрелости AGNTCY/SLIM в части "Agent Observability" — есть ли рабочий код/демо для наблюдаемости workflow, или на текущий момент это преимущественно пресс-релиз и roadmap?
Есть ли у Quorum-MCP (или аналогичных MCP-серверов для multi-provider консенсуса) публичный репозиторий с проверяемой активностью, лицензией и тестами, или это единичный экспериментальный проект без сообщества?
Существуют ли открытые реализации паттерна "MCP gateway с permission separation" (по типу упомянутого Peta) как самостоятельного строительного блока, а не как часть закрытой коммерческой платформы — то есть можно ли взять именно механизм envelope/payload-изоляции отдельно от остального продукта?
Насколько формат Agent Card (A2A) и формат SKILL.md (Agent Skills) конфликтуют или дополняют друг друга, если понадобится одновременно описывать "участника коллаборации" (кто это, какие у него роли) и "то, что он умеет делать" (progressive disclosure инструкций) — есть ли прецеденты совместного использования этих двух стандартов в одном проекте?
Какие юридические/ToS-риски конкретно применимы к browser-bridge классу решений у каждого из четырёх провайдеров (OpenAI, Anthropic, Google, DeepSeek) по состоянию на текущий момент — этот вопрос требует прямого чтения актуальных условий использования, а не вторичных источников.
Есть ли в экосистеме W3C PROV готовые открытые UI/визуализаторы provenance-графов (не научные прототипы, а поддерживаемые инструменты), которые можно было бы взять за основу для "человеческойконтрольной комнаты" происхождения решений, вместо разработки визуализации с нуля?
---
Коротко о сути находок, помимо самого отчёта:
Control plane / durability — единственная зона, где индустрия реально консолидировалась: Temporal (production-grade) закрывает почти всё из вашего списка (таймеры, ожидания, restart-recovery, история), но не знает про "AI-чат" как сущность.
Isolation / progressive disclosure — MCP и Agent Skills решают смежные, но не тождественные задачи: MCP изолирует агент↔инструмент, Skills прогрессивно раскрывают инструкции одному агенту, а не сообщения между несколькими независимыми участниками. Готового "конверт/payload"-механизма именно под вашу задачу нет.
Endpoint access к уже существующим веб-чатам — единственный практический путь сегодня это неофициальные browser-bridge проекты (ai-browser-bridge, web-model-bridge, unofficial-claude2-api и т.п.). Официальных механизмов для этого не существует ни у одного из четырёх провайдеров.
Human control room — LangGraph Studio / Langfuse Agent Graphs ближе всего по духу, но жёстко привязаны к графам, известным заранее из кода одного фреймворка, а не к "чужим" узлам-чатам.
Deliberation по нескольким независимым конечным точкам (не debate-внутри-фреймворка) — единственный найденный близкий кандидат — Quorum-MCP, но его зрелость не подтверждена независимо и требует отдельной проверки репозитория.
В конце документа — 7 прицельных вопросов для следующего раунда разведки (там же зафиксировано, что "Zero" и "AutoContext" не дали однозначного попадания на конкретный проект — под именем "Zero" существует минимум три разных, не связанных друг с другом продукта, это стоит уточнить, что именно имелось в виду).