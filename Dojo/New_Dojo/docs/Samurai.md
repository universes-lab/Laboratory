В CODING_PHILOSOPHY уже сказано:

CURRENT PROMPT = текущая operational frame;
SPEC / ТЗ = план операции, который может содержать будущие шаги, но их наличие не разрешает выполнение;
CURRENT SENSEI INSTRUCTION = текущая инструкция Сенсея, которая уточняет/исправляет/сужает именно текущий шаг.

То есть STEP.md — не новая бюрократия. Это просто физический файл для уже предусмотренного Уставом CURRENT SENSEI INSTRUCTION.

Три рабочих документа
Документ	Автор	Назначение	Срок жизни
Current_Prompt.md	Док; при необходимости Промптер по behavioral части	Какую операцию сейчас выполняет Самурай, в каком MODE, где ROOT, какой SPEC и какой STEP активны	Несколько STEP; меняется при смене операции / MODE / проекта
SPEC.md	DeepSeek формализует архитектуру Дока; Grok review; Автор freeze	Полный технический закон системы + список работ/фаз + acceptance requirements	Вся версия SPEC v3.2.2; frozen
STEP.md	DeepSeek; утверждает Док; в особо важных случаях Grok review/sign-off	Единственное текущее техническое задание Самураю	Один STEP или одна correction; затем заменяется целиком

Это и есть правильная ZOV/ZOR.

1. Current_Prompt.md — мой

Ты был прав.

Он не должен содержать сам STEP. Нынешний файл в New_Dojo именно этим и испорчен: там уже сидит весь PHASE 1 — STEP 1, плюс ссылки на IMPLEMENTATION_PLAN и MAP.

Его задача гораздо меньше:

PROJECT: Manuscript_Press
ROOT: D:\Gemini\dojo
ACTIVE_MODE: IMPLEMENTER
ACTIVE_OPERATION: Phase 1 implementation

ACTIVE SPEC:
@D:\Gemini\dojo\SPEC.md

CURRENT SENSEI INSTRUCTION:
@D:\Gemini\dojo\STEP.md

Execute only the current STEP.
STEP completion does not authorize NEXT.
REPORT → STOP → WAIT.

Всё.

Он может жить весь Phase 1, пока не изменился MODE или сама operational frame.

2. SPEC.md — закон Дипсика

Нынешний SPEC.md по содержанию именно такой: filesystem, markers, protected grammar, revision semantics, commit, acceptance tests и т. д.

Его не надо переписывать при каждом STEP.

И он может содержать весь будущий фронт работ. Устав прямо разрешает SPEC иметь множество planned steps, отдельно оговаривая, что это не authorization.

Только позже поправим его шапку с:

GROK REVIEW CANDIDATE

на фактический:

FROZEN

Без изменения содержательной части.

3. STEP.md — переменный приказ Сенсея

Вот сюда теперь помещается целиком последнее исправленное ТЗ DeepSeek.

Не в Current_Prompt.

Каждая correction означает:

старый STEP.md
      ↓ replace whole file
новый STEP.md

Не дописываем снизу историю исправлений.

Каждый STEP.md самодостаточен:

STEP ID
OBJECTIVE

ALLOWED FILES

EXACT REQUIREMENTS

TESTS / ACCEPTANCE

NON-GOALS

REPORT FORMAT

STOP

DeepSeek составляет техническое содержание. Я проверяю его на полноту и противоречия и ставлю GO. Для рискованного места можем сначала дать Grok.

После завершения Самураем:

Samurai report
    ↓
DeepSeek verification
    ↓
Doc arbitration if needed
    ↓
STEP accepted
    ↓
new STEP.md
А IMPLEMENTATION_PLAN и IMPLEMENTATION_MAP?

Из управляющего контекста Самурая убрать. Не уничтожать.

IMPLEMENTATION_PLAN.md фактически уже дублирует фазовую часть SPEC и даже содержит старую команду Самураю снова начинать с Phase 0. Именно такие документы и создают лазейки.

IMPLEMENTATION_MAP_APPROVED.yaml полезен Доку / Grok / DeepSeek как forensic reference, но Самураю постоянно читать его незачем.

Итого рабочий control plane:

D:\Gemini\GEMINI.md
    ├─ @D:\Gemini\System_Prompt.md
    ├─ @D:\Gemini\dojo\Current_Prompt.md
    └─ @D:\Gemini\SAMURAI\doctrine\CODING_PHILOSOPHY.md

Current_Prompt.md
    ├─ operation + MODE + ZOR
    ├─ @SPEC.md
    └─ @STEP.md

SPEC.md
    └─ frozen technical law

STEP.md
    └─ one current Sensei instruction

Причём Устав уже требует при смене Current Prompt заново установить operation, MODE, active SPEC и authorization и запрещает переносить разрешение из старой истории.

И -r

Вот здесь схема особенно удачная. Gemini CLI официально поддерживает @file imports внутри context-файлов и позволяет принудительно перечитать их через /memory refresh.

Поэтому при сохранении одной сессии:

DeepSeek выдал новый STEP
        ↓
заменили STEP.md
        ↓
/memory refresh
        ↓
продолжаем через -r

А старый STEP, оставшийся в conversation history, по собственному Уставу Самурая не является текущей авторизацией: там прямо записано «Never treat an old instruction as current merely because it remains in context».

Вот теперь конструкция совпала с тем, для чего Самурай первоначально проектировался: постоянный характер → текущая рамка → закон → один приказ Сенсея.