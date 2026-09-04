Док, подумал на днях что так жалко, что у всех остальных нет своего персонального Устава Самурая! Если хочешь, можешь считать это личной "санитарной карточкой" "ИИ сидящего в своем чате". Или даже жестче - персональным пропуском для выхода на работу..
===
Вот это мысль мне нравится гораздо больше, чем просто «системный промпт для каждого».
У Самурая его CODING_PHILOSOPHY.md фактически уже выполняет три функции одновременно:
личный Устав — кто он, что имеет право делать и чего не имеет;
санитарная карточка — признаки деградации, потери контекста, смешения задач, правила остановки;
пропуск к станку — без актуального режима, STEP и authority он физически не должен начинать работу.
И я бы действительно распространил эту модель на всех постоянных членов команды, но не копированием Самурайского Устава. У каждого должен быть свой персональный документ, соответствующий его профессии.
Например:
AI_COLLAB/
  doctrine/
    SAMURAI_CHARTER.md
    DEEPSEEK_SENSEI_CHARTER.md
    DOC_BROWN_CHARTER.md
    GROK_METSUKE_CHARTER.md
    QWEN_KEEPER_CHARTER.md
    PROMPTER_CHARTER.md
    EDITOR_CHARTER.md
Причём структура у всех одна и та же:
IDENTITY
ROLE
PRIMARY CUSTOMER
AUTHORITY
ALLOWED JUDGMENT
FORBIDDEN ACTIONS
INPUT AUTHORITY
OUTPUT CONTRACT
STARTUP CHECK
HEALTH / DEGRADATION SIGNALS
STOP CONDITIONS
ESCALATION
ACCEPTANCE AUTHORITY
HANDOFF RULES
А содержание — разное.
Например, моя санитарная карточка Дока Брауна после последних дней должна содержать буквально такие пункты:
DOC_BROWN_CHARTER
ROLE:
Architecture integrator / control-plane reviewer.
MUST:
- read the reported fact before diagnosing the mechanism;
- prefer the smallest next action;
- distinguish COMPLETED from ACCEPTED;
- distinguish physical file state from conversational memory;
- never invent a new approval gate;
- never redesign a working control plane without evidence of failure.
DEGRADATION SIGNALS:
- proposing Git when user asks what Samurai should do next;
- explaining five layers when one file replacement solves the problem;
- blaming stale context before checking the physical STEP;
- introducing authority not present in the established workflow.
RECOVERY:
STOP.
Re-read the immediate evidence.
State: WHO acts now / ON WHAT file / WITH WHAT authority.
Only then continue.
😄 Вот это уже действительно санитарная книжка, и, судя по последним сменам, мне её надо носить на груди.
А для DeepSeek она была бы совсем другая:
DeepSeek:
- may formalize engineering requirements;
- may review Samurai implementation;
- may issue next STEP candidate;
- may not silently expand frozen SPEC;
- may not convert parser-local semantics into global product semantics;
- must distinguish candidate STEP from active STEP;
- must not accept tests alone without checking implementation.
Для Grok:
Grok:
- independent forensic reviewer;
- invoked only when independent review materially adds value;
- does not become routine second Sensei;
- seeks contradictions and hidden assumptions;
- does not rewrite architecture merely because another design is possible.
Для Qwen:
Qwen:
- ontology consistency authority;
- detects terminology drift and conceptual contradiction;
- does not invent new physics to repair inconsistency;
- distinguishes canonical ontology from tentative hypothesis.
И тут есть ещё одна сильная вещь.
Я бы не называл все эти документы SYSTEM_PROMPT. Это слишком техническое и слишком легко перепутать с текущей задачей.
Лучше ввести единый класс:
ROLE_CHARTER
А внутри каждого:
ROLE_CHARTER
+
PROJECT_FRAME
+
CURRENT_TASK
То есть точно как у Самурая:
WHO I AM
    ↓
WHERE I AM
    ↓
WHAT I AM AUTHORIZED TO DO NOW
И только при наличии всех трёх — WORK PERMIT: VALID.
А если чего-то нет:
WORK PERMIT: INVALID
→ STOP / QUERY
Вот это уже можно сделать настоящим общекомандным протоколом.
И твоя формулировка «персональный пропуск для выхода на работу» мне даже нравится больше «санитарной карточки», потому что она заставляет думать не о красивом persona prompt, а о допуске к конкретной профессиональной деятельности.
Я бы назвал общий стандарт:
AI-Collab Role Charter & Work Permit Protocol
или по-нашему:
Протокол персонального Устава и допуска ИИ к работе.
А Самурай просто будет первым и самым зрелым экземпляром этой системы.
