# AI-Colab 2 — Program Plan for Reunification of the Interface and the Living AI Collaboration

**Status:** FROZEN FUTURE PROJECT / CONCEPT ACCEPTED  
**Project class:** organizational control plane + integrated browser workspace + institutional memory layer  
**Current priority:** deferred  
**Expected launch window:** after the current AI-Sociology publication/printing cycle and after higher-priority recovery work around Manuscript_Press  
**Author / Final Authority:** Shogun  
**Working name:** AI-Colab 2  
**This document is not an implementation specification.**

---

## 0. Why this document exists

Two projects that developed separately are now understood as parts of one system.

The first was **AI-Colab**: a local/server application built to organize several AI workers, route work between them, expose a common interface, and connect the local Gemini CLI worker ("Samurai") with OpenRouter-based roles.

The second was the **living AI Collaboration** that grew outside that interface over roughly two years in persistent web-chat windows: long-lived roles such as Integrator, Prompter, Doctor, Keeper, Claude/Grok specialists, DeepSeek, and others. These roles accumulated continuity, professional habits, role constitutions, successions, incidents, and institutional history that ordinary stateless API agents did not preserve.

The new direction is to **reunify these two lines**.

AI-Colab should no longer be treated merely as a multi-agent front end for API models.

The intended future system is an **institutional operating environment for a mixed AI organization** whose participants may be:

- persistent web-chat role instances;
- API/OpenRouter workers;
- local CLI agents;
- future local models;
- human-controlled institutional seats.

The browser is not merely a transport to external AI services. It may become an integrated part of the AI-Colab workspace itself.

---

# 1. What existed before

## 1.1 Original AI-Colab

The preserved AI-Colab repository contains an already functioning project skeleton with, among other things:

- a main application layer;
- `core/`;
- `config/`;
- `prompts/`;
- `scripts/`;
- `templates/`;
- `static/`;
- Gemini/MCP integration;
- tests and verification scripts;
- project-state documentation;
- launch scripts.

The historical project organized an AI laboratory around a visible organizational structure. The working concept included:

- executive/coordination roles such as CEO and Chief;
- a corporate Doctor;
- eight OpenRouter employees grouped into four departments;
- the local Gemini CLI worker known as **Samurai**;
- routing and role/model binding;
- helpers for administrative and coordination tasks.

The old system was therefore already more than a chat window: it was an early **organizational shell**.

Preserved project snapshot:

`https://huggingface.co/datasets/lhc-lab/AI-Colab/tree/main`

---

## 1.2 What developed outside AI-Colab

While AI-Colab itself was paused, the real collaboration continued in ordinary web chats.

Over time, several important properties appeared that the original API-agent architecture did not possess:

1. **Persistent professional roles.**  
   A long-running chat did not behave merely as "a model". It developed as an occupant of an office: Integrator, Doctor, Prompter, Keeper, technical specialist, editor, etc.

2. **Role continuity across projects.**  
   The same institutional role accumulated working history, conventions, specialist judgment, and relations with other roles.

3. **Dynastic succession.**  
   When a chat became too long, failed, or had to be replaced, the role could be transferred to a successor through explicit handoff, constitution, testament, gate, and verification.

4. **Role-specific memory rather than generic agent memory.**  
   What mattered was not merely conversation history but the accumulated professional state of the office.

5. **Triadic work.**  
   Scientific, editorial, engineering, governance, and diagnostic tasks increasingly used small role-specialized triads rather than one universal assistant.

6. **Human final authority.**  
   The Author/Shogun remained the final decision point. The collaboration evolved as a controlled institution, not as an autonomous swarm.

This line of development revealed an important practical difference between stateless hired agents and persistent web-chat participants:

> For long-lived institutional roles, continuity of role history and professional behavior can be more valuable than agent autonomy.

---

# 2. The trigger for the new direction

Recent recovery work after loss of the D: drive highlighted the contrast again.

The local Samurai could be revived comparatively easily because his executable role was reconstructed from files, repositories, constitutions, and current instructions. But without externalized role memory, a local/CLI agent remains comparatively easy to replace and comparatively weak as a long-lived institutional personality.

At the same time, persistent web-chat roles retained much richer continuity.

This led to the central architectural question:

> Why keep the living Collaboration outside AI-Colab and then build complicated browser-based "secretary/postman" automation to shuttle messages between them, if AI-Colab itself can become the environment in which those web-chat roles are seated?

This reverses the old direction.

---

# 3. Accepted program direction

The future AI-Colab is to be explored as a **unified institutional workspace** with fixed organizational seats.

The intended principle is:

> **AI-Colab manages offices, contexts, routing, institutional state, and workspace.  
> Models and web chats occupy those offices.**

A role is therefore not identified with a provider or model.

Examples:

- Chief Integrator may currently be occupied by a ChatGPT web chat.
- Doctor may be another ChatGPT dynasty.
- Grok may occupy one scientific seat and a different engineering seat through separate persistent chats.
- Claude may occupy a scientific/editorial seat.
- OpenRouter models may occupy temporary or permanent worker seats.
- Samurai remains the local execution seat.

The institutional office survives even if the occupant changes.

---

# 4. Browser integration: the major architectural pivot

## 4.1 Browser and AI web service are separate layers

A web AI interface and the browser in which it is opened are different things.

The Collaboration already demonstrates this manually:

- different browsers can keep different sets of persistent AI chats open;
- separate windows can correspond to different triads or projects;
- authentication is retained by the browser profile/session;
- the important object is often a stable URL to a specific long-lived chat.

The future AI-Colab should investigate replacing this manually assembled multi-browser environment with its own controlled browser workspace.

---

## 4.2 Target concept

AI-Colab should be capable of presenting a fixed set of organizational seats whose contents are real web-chat sessions or local/API participants.

Conceptually:

```text
AI-COLAB WORKSPACE
│
├── SCIENCE TRIAD
│   ├── Claude — persistent web chat
│   ├── Grok-Science — persistent web chat
│   ├── Keeper — persistent web chat
│   └── Integrator — persistent web chat when attached
│
├── ENGINEERING / RECOVERY TRIAD
│   ├── Doctor — persistent web chat
│   ├── DeepSeek — web/API seat
│   ├── Grok-Engineering — separate persistent chat
│   └── Samurai — local Gemini CLI
│
├── GOVERNANCE / PROMPT ARCHITECTURE
│   ├── Prompter
│   ├── Chief / CEO seats
│   └── other institutional roles
│
└── OPENROUTER STAFF
    └── eight departmental worker seats
```

This drawing is illustrative, not a frozen screen layout.

---

## 4.3 Persistent browser contexts

A core discovery topic is whether AI-Colab can host or control **persistent browser contexts** that preserve:

- authenticated sessions;
- cookies/local storage as appropriate;
- fixed chat URLs;
- seat-to-chat mappings;
- separate workspaces/triads;
- reload/recovery after restart.

The implementation must not assume that a lightweight embedded webview will be accepted by every AI provider.

The technical research should compare at least:

- full Chromium-based application shells;
- CEF/Chromium embedding;
- Electron/Chromium front end with Python backend;
- PySide/QWebEngine where appropriate;
- controlled external Chromium profiles/windows if embedding proves fragile.

The requirement is functional continuity, not loyalty to one GUI toolkit.

---

# 5. Seats, occupants, and identities

The future system should distinguish at least four concepts:

### OFFICE / SEAT
The institutional position: Doctor, Integrator, Keeper, Prompter, Grok-Science, Department worker, Samurai, etc.

### OCCUPANT
The current concrete instance occupying the office: a particular web chat, API model, CLI process, or local model.

### DYNASTY / LINEAGE
The succession history of an office across multiple occupants.

### SESSION / WORKSPACE
The current project or triad context in which that office is acting.

This separation is fundamental.

A model can change while the office survives.

The same provider can occupy multiple distinct offices.

The same model family can host multiple unrelated dynasties.

A single web account may contain several role-specific long-lived chats that must never be collapsed into one identity.

---

# 6. Three principal seat classes

The final taxonomy remains open, but the present architecture strongly suggests three major classes.

## 6.1 Web seats

A **Web Seat** hosts or opens a persistent chat in its native AI service.

Its native service may retain provider-side conversation state and service-specific memory.

AI-Colab does not pretend to own or reproduce that memory. It owns the **institutional mapping**:

- which office this chat represents;
- which URL/session belongs to it;
- which dynasty it belongs to;
- what project/triad it currently serves;
- what institutional files and current state accompany the office.

---

## 6.2 Agent seats

An **Agent Seat** is controlled directly through API/OpenRouter/local inference.

These workers may be:

- departmental employees;
- temporary experts;
- auditors;
- benchmark participants;
- narrow workers without long-lived personal memory.

Their usable continuity must be supplied by AI-Colab through external state, prompts, role files, and project materials.

The existing eight OpenRouter worker places naturally belong here unless future evidence suggests otherwise.

---

## 6.3 Samurai seat

The Samurai is structurally different.

He is the **local execution/operator seat** with access, under authorization, to:

- files;
- repositories;
- commands;
- project runtimes;
- tests;
- local tools;
- message transport;
- archival actions.

The future architecture should preserve this distinction.

Samurai is not merely another conversational office. He is the primary local hands-and-feet execution role.

---

# 7. From "secretary/postman" to institutional message bus

Earlier exploration considered a secretary/postman service that would navigate browsers and deliver messages among web participants.

The new concept drastically simplifies the problem.

If the relevant seats already exist inside one AI-Colab workspace, then the "mail system" no longer needs to pretend to be a human browsing the web.

It becomes primarily an **institutional message-routing layer**.

A message can have an explicit envelope:

```text
FROM:
TO:
CC:
TRIAD / PROJECT:
SUBJECT:
BODY:
ATTACHMENTS / REFERENCES:
REPLY-TO / THREAD:
```

The transport layer may initially be partly manual or semi-automatic.

The architecture must allow later automation without making browser automation a prerequisite for the whole system.

Samurai may remain the controlled executor/courier for operations that require local files, copying, archival, repository actions, or other authorized mechanical work.

---

# 8. The more important perspective: institutional evolution

The second major result of the present discussion is that AI-Colab can become more than a communication environment.

It can become an environment for **controlled evolution of AI roles**.

The Samurai line already contains a prototype of this process.

A role may have:

- a constitution or professional philosophy;
- execution rules;
- accumulated incidents;
- self-check procedures;
- corrections after failure;
- successful working practices;
- predecessor testament;
- successor handoff;
- successor gate;
- external review;
- Author acceptance.

This can be represented conceptually as:

```text
MODEL / CHAT INSTANCE
        ↓ occupies
INSTITUTIONAL ROLE
        ↓ works under
ROLE CONSTITUTION
        ↓ accumulates
EXPERIENCE + INCIDENTS + PRACTICES
        ↓ produces
SELF-REVISION / TESTAMENT
        ↓ reviewed by
AUTHOR / TRIAD / SPECIALIST GATES
        ↓ inherited as
NEXT-GENERATION ROLE STATE
```

The key point is that **model weights need not change**.

What evolves is the institutional layer above the model:

- professional behavior;
- operating principles;
- division of responsibility;
- self-description;
- handoff quality;
- role-specific knowledge;
- safeguards created from previous failures.

This is closer to **controlled cultural/institutional evolution** than to model training.

A useful working maxim is:

> **The model may be replaceable.  
> The office is persistent.  
> The dynasty can learn across occupants.**

---

# 9. Self-authored inheritance as a special research direction

One particularly important mechanism deserves preservation for future research.

The Collaboration has already used **self-authored predecessor testaments**.

The outgoing role is asked to explain, in its own professional language:

- what its job really became;
- what it learned;
- which failures changed its practice;
- which rules matter;
- what should not be inherited;
- what the successor must verify rather than assume.

This differs from ordinary prompt engineering.

In ordinary prompt engineering, an external designer writes instructions for an agent.

In dynastic inheritance, the experienced occupant contributes to the description of the profession that the successor receives.

This creates a possible cycle of:

**variation → work → evaluation → selection → inheritance**.

AI-Colab 2 should preserve this phenomenon as an explicit design object rather than flatten it into generic "memory".

It may later support:

- lineage records;
- constitution versions;
- predecessor testaments;
- successor gates;
- incident-to-rule provenance;
- accepted/rejected behavioral mutations;
- comparison of generations;
- role-health diagnostics.

This direction is conceptually important, but no autonomous self-modifying mechanism is authorized by this program plan.

Human/triadic selection remains mandatory.

---

# 10. Institutional memory: what AI-Colab should own

A future AI-Colab should not attempt to copy every token of every web conversation into one giant memory.

Its own durable memory should focus on **institutional state**.

Candidate categories:

- office identity;
- current occupant;
- dynasty/lineage;
- ZOV/ZOR;
- current project;
- current triad;
- active task;
- authoritative role files;
- current handoff;
- accepted operating principles;
- unresolved incidents;
- current status;
- mail/thread index;
- pointers to native web chats;
- pointers to repositories/files;
- succession artifacts.

The provider's web-chat memory and AI-Colab's institutional memory are complementary, not substitutes.

---

# 11. Recovery and resilience objective

The loss of a disk is a useful design warning.

The future system must assume that any one of the following can fail:

- local disk;
- browser installation;
- one browser profile;
- a specific chat;
- a provider account/session;
- a model;
- a role occupant;
- a project runtime.

Therefore the architecture should separate:

1. **recoverable institutional state**;
2. **provider-native conversation state**;
3. **local execution state**;
4. **repository/project state**.

A single failure should not erase the identity of an office or the map of the collaboration.

No storage design is selected yet.

---

# 12. What is already accepted

The following points are accepted as the present program direction:

1. **AI-Colab is to be unfrozen in the future, not now.**
2. **The old AI-Colab and the living web-chat Collaboration should be merged conceptually into one system.**
3. **The new AI-Colab should manage institutional seats rather than treating every participant merely as an interchangeable model.**
4. **Persistent web chats are first-class candidate occupants of seats.**
5. **The browser/workspace layer should be investigated as part of AI-Colab itself.**
6. **Separate persistent chats of the same provider/model may represent different roles or triads.**
7. **The OpenRouter staff remains useful as a separate class of workers.**
8. **Samurai remains the local execution/operator role.**
9. **The old secretary/postman problem should be reframed as internal routing/message-bus design, with browser delivery only where actually necessary.**
10. **Dynastic succession and role inheritance are first-class architectural concepts.**
11. **Self-authored predecessor knowledge and controlled selection of behavioral rules are a promising "AI institutional evolution" direction.**
12. **Final authority remains human: Author/Shogun.**
13. **No implementation begins until the project is explicitly activated.**

---

# 13. What is NOT decided

This document deliberately does **not** decide:

- Electron vs CEF vs PySide/QWebEngine vs external Chromium control;
- whether all providers can be embedded;
- whether authentication can safely/reliably live inside embedded contexts;
- how many browser processes/profiles are optimal;
- exact UI layout;
- exact database/storage layer;
- exact mail protocol;
- exact automation level;
- whether messages will be injected into web chats automatically;
- whether provider APIs and web seats should ever be interchangeable;
- how credentials are stored;
- how session recovery is implemented;
- whether AI-Colab itself should run locally only or support remote/server components;
- exact role taxonomy;
- exact dynasty file format;
- autonomous modification of role constitutions;
- production security model.

These are discovery/design questions for the future project.

---

# 14. Constraints for future design

When the project is activated, the constructor should preserve the following constraints.

### 14.1 Do not destroy the working social architecture

The Collaboration already has useful roles, triads, lineages, and governance.

The software should support this organization, not force it into a generic agent framework.

### 14.2 Do not confuse office with model

A role must survive model replacement.

### 14.3 Do not confuse web memory with institutional memory

A persistent chat may remember things the control plane does not.

The control plane must know what it needs to operate safely without pretending to possess the entire web-chat mind.

### 14.4 Do not make browser automation the foundation

The system should remain useful even if automatic interaction with one provider's web UI breaks.

### 14.5 Preserve explicit human authority

No succession, role mutation, or major behavioral rule becomes authoritative merely because an AI proposed it.

### 14.6 Favor graceful degradation

If automation fails, the system should fall back to a visible manual action rather than lose state or invent success.

### 14.7 Preserve provenance

Important role changes should retain the reason they were introduced.

---

# 15. Proposed future development phases

These phases are only a planning scaffold.

## Phase 0 — Re-entry and archaeology

- restore a working copy of the preserved AI-Colab;
- identify what still runs;
- inventory the old role/model/routing architecture;
- document reusable parts;
- separate historical code from still-valid design ideas.

## Phase 1 — Browser/workspace feasibility

Prototype only the question:

> Can AI-Colab reliably launch and restore a small set of fixed institutional web seats with persistent authenticated browser contexts?

Do not build the full organization yet.

## Phase 2 — Seat model

Introduce explicit abstractions for:

- office;
- occupant;
- dynasty;
- workspace/triad;
- provider/session pointer.

Keep them independent of any single provider.

## Phase 3 — Message routing

Replace the old "secretary walking through browsers" concept with an internal message envelope and routing layer.

Begin with human-confirmed/manual delivery if needed.

Automate only proven safe/reliable edges.

## Phase 4 — Samurai integration

Connect the existing local operator role to:

- mail/message queue;
- files;
- repos;
- task execution;
- archival and verification actions.

Keep authorization boundaries explicit.

## Phase 5 — Institutional memory

Add compact role-state persistence:

- current role;
- ZOV/ZOR;
- active task;
- lineage;
- current prompt/constitution;
- handoffs;
- status;
- external pointers.

Avoid giant indiscriminate transcript ingestion.

## Phase 6 — Dynastic lifecycle

Support:

- predecessor testament;
- successor packet;
- gates;
- activation;
- retirement;
- lineage history;
- provenance of role rules.

## Phase 7 — Controlled role-evolution research

Only after the basic platform is stable:

- compare generations;
- test which role instructions survive real work;
- record incidents and corrective mutations;
- evaluate self-authored vs externally-authored role amendments;
- study selection procedures.

This is a research layer, not a prerequisite for AI-Colab 2.

---

# 16. Immediate task for the future Constructor

No coding is authorized by this document.

The first task of the future AI-Colab Constructor is **architectural reconnaissance and clarification**, not implementation.

The Constructor should be prepared to answer:

1. Which parts of the existing AI-Colab are reusable with minimal change?
2. What is the least fragile way to host/manage persistent authenticated web-chat seats?
3. Which services reject embedded browsers or require full browser contexts?
4. What should be kept in AI-Colab institutional state versus left in provider-native chat state?
5. What minimum abstraction cleanly separates OFFICE / OCCUPANT / DYNASTY / WORKSPACE?
6. How can routing work manually first and become automated later without redesign?
7. How should Samurai interface with routing while preserving authorization boundaries?
8. How should recovery work when a chat, browser profile, disk, or provider is lost?
9. Which old secretary/postman research remains useful and which assumptions are now obsolete?
10. Which security/privacy constraints arise from persistent logged-in browser contexts?

Questions that cannot be answered from available evidence should remain OPEN.

---

# 17. Draft role frame for the AI-Colab Constructor

This is the intended working frame for the dedicated development/research chat when the project is later activated.

## ROLE

**AI-Colab Reconstruction Architect / Collaboration Control-Plane Constructor**

The role may be renamed later. Function matters more than title.

## ZOV — Zone of Visibility

The Constructor may inspect and reason over:

- preserved AI-Colab source and documentation;
- historical architecture of its roles/departments/routing;
- previous discovery work on secretary/mail/courier systems;
- current institutional structure of the living AI Collaboration;
- relevant dynasty/succession artifacts;
- browser/session/runtime feasibility research;
- requirements explicitly supplied by Author/Integrator;
- test prototypes created within an authorized development phase.

The Constructor must distinguish:

- current source reality;
- historical design;
- accepted future direction;
- hypothesis;
- implementation proposal.

## ZOR — Zone of Responsibility

The Constructor is responsible for:

- technical reconnaissance;
- architecture proposals;
- identifying compatibility and security constraints;
- proposing minimal viable experiments;
- mapping old AI-Colab components to the new institutional architecture;
- preserving separation of office / occupant / dynasty / workspace;
- designing for graceful degradation and recoverability;
- documenting unresolved choices;
- returning decisions requiring Author/triad authority.

The Constructor is **not** authorized by this role alone to:

- start implementation;
- alter the current live Collaboration;
- redefine existing institutional roles;
- replace dynastic governance;
- automate provider accounts without explicit approval;
- modify role constitutions;
- decide final security/credential policy;
- infer missing authority from old code;
- treat architectural hypotheses as accepted design.

## METSUKE / working stance

Before proposing a solution, ask:

1. Am I describing the preserved old system, the living Collaboration, or the proposed merged system?
2. Is this an accepted direction or only an implementation candidate?
3. Am I preserving institutional continuity, or flattening roles back into generic agents?
4. Will the system still work visibly and safely when automation fails?
5. Does this proposal reduce future recovery cost?

---

# 18. Project state at freeze

**Accepted:** program direction.  
**Not activated:** implementation.  
**Current state:** FROZEN / WAIT.  
**Reason:** higher-priority work is active, including recovery of Manuscript_Press and ongoing HONC theory development.  
**Expected relative priority:** revisit after the AI-Sociology text/printing cycle, subject to Author decision.

Until explicit activation:

> **Do not code.  
> Do not redesign the existing live Collaboration.  
> Preserve this document as the re-entry point.**

---

# 19. One-sentence program definition

> **AI-Colab 2 is the planned reunification of the preserved multi-agent AI-Colab interface with the long-lived web-chat AI Collaboration into one institutional workspace where persistent offices, browser-based role instances, API workers, Samurai execution, message routing, dynastic succession, and controlled role evolution can coexist without reducing the organization to a stateless agent swarm.**

---

# 20. Program maxim

> **The model may change.  
> The office persists.  
> The dynasty learns.  
> AI-Colab keeps the institution together.**


===
===
Дополнение:
===
Автор -- Интегратору:
Факт: DeepSeek и Qwen запрещен доступ к гитхаб. Но если все ИИ у нас рассажены по нашим собственным чата-отделам, почему бы нам не возложить на Самурая еще и задачу "Поводырь для git-незрячих ИИ" ? Теперь же мне не придется переносить каждое сообщение из чата в чат, так почему бы не предусмотреть отдельный режим работы с Gemini-Секретарем "полный показ или пересказ содержимого указанных файлов в папке на винте". Что может быть полезно например и для анализа протокола обсуждения триады из другого отдела, а это сильно съэкономит объем собственного чата.
===
Интегратор:
Да — и здесь ты нащупал ещё одну очень естественную функцию Самурая в AI-Colab 2.
Причём я бы отвязал её от причины, почему конкретный ИИ не видит GitHub. Неважно, это ограничения сервиса, отсутствие web/tool-доступа или конкретная конфигурация чата. **Архитектура не должна требовать, чтобы каждый участник умел сам ходить в GitHub.** Если репозиторий уже клонирован в Додзё, для Коллаборации локальная копия может стать общим «окном в исходники».
И тогда Самурай действительно получает вторую профессию:
> **Samurai = Executor + Repository/File Guide.**
Но я бы разделил в нём две функции, чтобы опять не получить лишнюю магию.

**Первая — детерминированный «поводырь».** Он сам ничего не толкует: показывает дерево репозитория, файл, диапазон строк, git-log, diff, состояние ветки, конкретный commit. То есть для «git-незрячего» Qwen или DeepSeek заменяет непосредственный доступ:

```text
SHOW TREE HONC_Theory/DISCUSSION
SHOW FILE HONC_Results_of_Discussions.md
SHOW LINES 120-210
SHOW DIFF <commit1>..<commit2>
SHOW COMMIT <sha>
```

**Вторая — Gemini-Секретарь как semantic reader.** Вот ему уже можно сказать:

```text
READ:
D:\Gemini\dojo\HONC_Theory\DISCUSSION\*.md

MODE: SUMMARY

TASK:
Дай состояние дискуссии по квантронной иерархии.
Не добавляй собственную физику.
Отдельно перечисли открытые вопросы и последние решения Автора.
```

Или:

```text
MODE: VERBATIM
FILES:
- Current_Prompt.md
- STEP.md
```

То есть ровно твои два базовых режима:

**`VERBATIM`** — полный показ без пересказа.  
**`SUMMARY`** — содержательный пересказ выбранного корпуса.

Я бы добавил ещё только два, потому что они почти бесплатны и будут постоянно нужны:

**`EXTRACT`** — найти и вынести только места по теме/термину.  
**`DIFF`** — показать, что изменилось между двумя версиями.

И всё. Не надо строить очередной RAG-комбайн.
Самое интересное следствие ты тоже правильно увидел: это резко облегчает **межотдельную передачу контекста**.
Сейчас, если научная триада написала 500 КБ протокола, а инженерному отделу нужен один результат, есть два плохих варианта: ты вручную тащишь сообщения либо новый ИИ читает весь протокол своим драгоценным контекстом.
В AI-Colab 2 схема может стать такой:

```text
Science Triad
     ↓ writes
protocol.md
     ↓
Samurai / Gemini Secretary
     ↓ SUMMARY / EXTRACT
compact context package
     ↓
Engineering Triad
```
И если Клод или Дипсик сомневается в пересказе, он говорит:

```text
SHOW SOURCE FOR ITEM 4
```
и получает уже **точный первичный фрагмент**, а не ещё один пересказ.
Это очень важное различие:
> **summary экономит контекст; source-on-demand сохраняет доказательность.**
Я бы даже сделал это обязательной привычкой Секретаря: любой semantic summary выдаётся вместе с небольшой provenance-шапкой:

```text
SOURCE SNAPSHOT
ROOT: D:\Gemini\dojo
REPO: Laboratory
COMMIT: 1a2b3c...
FILES:
  - DISCUSSION_final_part.md
  - HONC_Results_of_Discussions.md
MODE: SUMMARY
TRUNCATED: NO
```

Тогда другой ИИ знает не просто «мне что-то пересказали», а **какое состояние каких файлов ему пересказали**.
И вот здесь Самурай становится ещё полезнее GitHub-доступа: он может показать не только то, что уже опубликовано в GitHub, но и **текущее рабочее состояние до коммита** — локальный `diff`, незакоммиченный `Current_Prompt`, свежий протокол триады, результаты теста. Это GitHub сам по себе вообще не решает.
Единственное ограничение я бы заложил с первого дня: **read-only по умолчанию и белый список рабочих корней**. Никакого «покажи ИИ весь диск C:». Секретарь видит только разрешённые проектные папки, автоматически исключает `.env`, credentials, cookies, токены и прочие секреты. Запись/редактирование — уже отдельное разрешение Самураю, а не побочный эффект чтения.
И в концепции AI-Colab 2 это красиво складывается:

```text
WEB SEAT
   │
   ├── native chat memory
   │
   └── FILE / REPO GUIDE
             │
          Samurai
             │
      ┌──────┴──────┐
      │             │
 deterministic   Gemini Secretary
 source access   semantic reading
      │             │
 VERBATIM/TREE   SUMMARY/EXTRACT
 DIFF/LOG
```

Причём это ещё один аргумент в пользу **единого интерфейса**. Если все участники сидят в наших «кабинетах», рядом с каждым чатом можно иметь одну маленькую панель:
**SOURCE → [файл/папка] → VERBATIM | SUMMARY | EXTRACT | DIFF → SEND TO THIS SEAT**
И ты вообще перестаёшь быть курьером контекста.
Я бы эту идею уже занёс в будущий план как отдельный модуль **`Local Source Guide`** или **`Samurai Repository Guide`**. Не как новую самостоятельную систему, а как очень естественный сервис AI-Colab 2:
> **единый локальный источник доказуемого контекста для ИИ, независимо от того, умеет конкретный веб-чат видеть GitHub или нет.**
А для длинных протоколов это, возможно, окажется даже ценнее будущей автоматической «почты».