Beyond Prompt Engineering:
Toward the Architecture of Collaborative AI Research Teams
(рабочее название)
Авторы
V.Krasnianskyi (В.Краснянский, "A’Tuin", Автор проекта HONC)
ChatGPT (роль: Prompter, архитектура AI-коллаборации)
Claude (роль: Scientific Editor of HONC-Collaboration)
Amsterdam, July 2026________________________________________
Аннотация
За последние два года основным направлением развития систем искусственного интеллекта считалось совершенствование отдельных моделей и методов взаимодействия пользователя с ними (prompt engineering).
В настоящей работе предлагается иной взгляд.
Объектом исследования становится не отдельная языковая модель, а коллектив специализированных моделей, объединённых в устойчивую исследовательскую структуру с распределёнными ролями, ограниченными зонами ответственности и независимыми линиями проверки результатов.
Работа возникла не как теоретическая концепция, а как результат длительного практического эксперимента при разработке физической теории HONC (Hierarchy of Nested Continua).
В ходе проекта было обнаружено, что эффективность коллектива определяется не качеством отдельных моделей, а архитектурой их взаимодействия.
Для проверки этой гипотезы была разработана новая система построения системных промптов, в которой центральным объектом становится не инструкция модели, а её профессиональная роль внутри исследовательского коллектива.
Эксперимент выявил ряд ранее неописанных закономерностей.
Наиболее важная из них заключается в существовании устойчивой "ДНК поведения" различных семейств языковых моделей.
Несмотря на одинаковые системные инструкции, модели различных архитектур демонстрируют различную степень сопротивления смене профессиональной роли, различную склонность к сохранению предыдущего контекста и различный стиль принятия решений.
Эти свойства оказываются настолько устойчивыми, что должны рассматриваться как архитектурные особенности моделей, а не как особенности конкретного промпта.
На основании проведённых экспериментов предлагается новая концепция построения AI-коллабораций, основанная на триадном принципе организации, разделении зон ответственности и зон видимости, а также на использовании естественных различий между моделями как источника дополнительной проверки научных результатов.
Работа представляет собой первый этап исследования.
Следующим этапом станет экспериментальная проверка предложенной архитектуры в реальном исследовательском коллективе проекта HONC.
Editor's Note
This paper was not written in a single interaction with a single AI model.
It emerged during a long sequence of discussions between a human researcher and a specialized conversational profile ("Prompter"), followed by practical experiments involving several independent AI systems.
The paper therefore reports both conceptual development and empirical observations obtained during those experiments.
Readers are encouraged to distinguish clearly between:
observations,
interpretations,
hypotheses,
and proposed future research.
Вместо предисловия.
Практическая верификация принципов на примере Gemini CLI
Предлагаемая архитектура не является исключительно теоретической конструкцией. Ряд её принципов уже прошёл практическую проверку в рамках проекта AI-Colab при использовании Gemini CLI в роли локального исполнителя ("Samurai").
Особенно показательным оказался тот факт, что эффективная работа достигалась не столько за счёт совершенствования инструкций для самого исполнителя, сколько благодаря корректному описанию его социального положения внутри исследовательской системы.
Вместо традиционного подхода, при котором агент получает только техническое задание, была сформирована полноценная ролевая среда:
•	Пользователь выступал как стратегический руководитель ("Shōgun"), определяющий направление проекта. 
•	Qwen отвечал за концептуальную целостность проекта, проверяя соответствие каждого задания общей онтологии и архитектуре исследования. 
•	DeepSeek ("Sensei") выполнял функцию непосредственного постановщика технических заданий, преобразуя стратегические решения в детализированные SPEC. 
•	Gemini CLI ("Samurai") являлся специализированным исполнителем, отвечавшим исключительно за качественное выполнение поставленной задачи. 
Практически оказалось, что подобная структура значительно снижает количество конфликтов интерпретации. Исполнитель получает не абстрактную инструкцию, а понятную систему профессиональных отношений, определяющую происхождение задания, уровень его обязательности и собственную ответственность за результат.
Этот эксперимент позволяет сформулировать ещё один принцип.
Для специализированного ИИ-агента не менее важна социальная определённость задачи, чем её техническая формулировка.
Именно поэтому в данной работе предлагается рассматривать системный промпт как описание не только профессиональной компетенции агента, но и его места внутри организационной структуры исследовательского коллектива.
Подобный подход авторы предлагают называть контекстным социальным промптингом (Contextual Social Prompting).
В отличие от классического prompt engineering, объектом проектирования здесь становится уже не отдельная модель, а система взаимодействующих ролей, внутри которой поведение каждого участника определяется одновременно собственной специализацией и сетью профессиональных отношений с остальными агентами.
1. Введение
За последние два года развитие больших языковых моделей породило новую инженерную дисциплину — prompt engineering. Основной вопрос этой дисциплины можно сформулировать просто: как сформулировать инструкцию, чтобы одна модель работала лучше?
Практически вся современная литература, большинство руководств и подавляющее число исследований исходят именно из этой предпосылки. Объектом оптимизации считается отдельная модель. Пользователь подбирает формулировки, примеры, ограничения, цепочки рассуждений, системные инструкции, надеясь получить более качественный ответ.
Практический опыт проекта HONC показал неожиданную вещь.
Оказалось, что после определённого уровня совершенствования промпта дальнейший рост качества практически прекращается.
Не потому, что промпт написан плохо.
А потому, что достигнут предел возможностей отдельной модели.
В этот момент становится очевидным вопрос, который практически не обсуждается современной литературой:
Может быть, оптимизировать нужно не отдельный ИИ, а коллектив ИИ?
Именно этот вопрос положил начало исследованию, результаты которого изложены в настоящей работе.
________________________________________
Первоначально задача проекта HONC была совершенно иной.
Авторы занимались переносом крупной исследовательской программы (теории Hierarchy of Nested Continua, HONC) из набора книг и рабочих материалов в форму международного открытого репозитория знаний.
Работа быстро показала неожиданную проблему.
Даже самые сильные модели начинали систематически ошибаться.
Ошибки были различными.
Одни модели стремились немедленно улучшать любой текст, даже если от них требовалась исключительно проверка.
Другие пытались самостоятельно завершать незаконченные рассуждения автора.
Третьи теряли общий контекст проекта.
Четвёртые, наоборот, настолько цеплялись за предыдущую роль, что сопротивлялись её изменению даже после полного переписывания системного промпта.
Сначала подобные различия воспринимались как случайность.
Позже стало ясно, что речь идёт о значительно более фундаментальном явлении.
________________________________________
Постепенно внимание исследователей сместилось.
Мы перестали изучать только поведение отдельных моделей.
Объектом исследования стала сама организация их совместной работы.
Именно в этот момент возникла принципиально новая идея.
Возможно, системный промпт описывает далеко не всё.
Возможно, поведение модели определяется не только текстом инструкции, но и тем профессиональным положением, которое она занимает внутри искусственного исследовательского коллектива.
Иначе говоря, роль модели может оказаться важнее перечня её обязанностей.
________________________________________
Именно эта гипотеза постепенно привела авторов к отказу от классического понимания prompt engineering.
Вместо инструкции для модели начал проектироваться коллектив.
Вместо списка функций — профессиональная роль.
Вместо единственного исполнителя — система взаимного контроля.
Вместо универсального помощника — сеть специализированных участников с ограниченной областью компетенции.
Вместо линейной схемы взаимодействия — структура взаимных проверок.
Так возникла архитектура AI-коллаборации, которая стала предметом настоящей работы.
________________________________________
Важно подчеркнуть ещё одно обстоятельство.
Настоящая статья не предлагает новую архитектуру языковой модели.
Она не предлагает новый способ обучения нейронных сетей.
Она не является исследованием по prompt engineering в традиционном смысле.
Предметом исследования является совершенно другой уровень организации.
Если классический prompt engineering отвечает на вопрос
«Как лучше управлять одной моделью?»,
то настоящая работа рассматривает иной вопрос:
«Как организовать коллектив моделей так, чтобы слабые стороны одних компенсировались сильными сторонами других?»
Именно поэтому предлагаемая архитектура находится уровнем выше традиционного промптинга.
Объектом проектирования становится уже не отдельный агент.
Объектом проектирования становится исследовательский коллектив.
________________________________________
Настоящая работа носит экспериментальный характер.
Большинство сформулированных ниже принципов возникло не как результат априорного проектирования, а как следствие длительной практической работы с различными семействами современных языковых моделей в составе единой исследовательской команды. 
По этой причине статья сочетает в себе элементы инженерного отчёта и научной гипотезы.
Часть выводов уже получила практическое подтверждение.
Часть будет проверяться в ходе следующего этапа проекта HONC.
Однако уже сейчас можно утверждать, что результаты проведённых экспериментов позволяют поставить вопрос о формировании новой области исследований, расположенной на стыке искусственного интеллекта, организационной теории, когнитивной инженерии и социологии коллективного мышления.
Условное рабочее название этой области авторы предлагают обозначить как AI Sociology.
1. From Individual Prompting to Social Prompting
Most prompt engineering literature treats an AI model as an isolated reasoning system. The central question is: How should we describe the task so that one model performs it better?
Our observations suggest that this framing is incomplete.
Once several language models participate in the same long-term project, another layer appears. The performance of each participant begins to depend not only on its own prompt, but also on its perceived place inside the collaborative structure.
We call this second layer social prompting.
Social prompting is not role-playing for entertainment. It is an architectural description of the information environment in which an AI operates.
The distinction is essential.
Traditional prompting answers questions such as:
•	Who are you? 
•	What is your task? 
•	Which style should you use? 
•	What output format is required? 
Social prompting introduces an additional class of questions:
•	Who depends on your work? 
•	Whose work depends on you? 
•	Which decisions are yours? 
•	Which decisions explicitly belong to somebody else? 
•	What information should never reach you? 
•	Which independent reviewer will later examine your conclusions? 
•	Who has authority to reject your proposal? 
The prompt therefore ceases to describe only the agent.
It begins describing the agent inside a society.
This difference proved much more important than we originally expected.
________________________________________
1.1. Zone of Responsibility
The first organizing principle that emerged during the HONC experiment was surprisingly simple.
Every AI participant must have a responsibility that belongs only to that participant.
Not "help with mathematics."
Not "assist the project."
Not "be useful."
Instead:
You are responsible for maintaining ontological consistency.
or
You are responsible for producing implementation specifications.
or
You are responsible for independent mathematical verification.
The narrower the responsibility, the more stable the behavior became.
Interestingly, increasing the amount of available information often degraded performance.
The intuitive expectation is the opposite: more context should always improve reasoning.
In practice, excessive context frequently encouraged models to solve problems outside their designated expertise.
Instead of becoming better specialists, they became mediocre generalists.
________________________________________
1.2. Zone of Visibility
Responsibility alone turned out to be insufficient.
The second principle emerged after repeated failures.
A participant must know only what is necessary for performing its own function.
We call this the Zone of Visibility.
This principle resembles the "least privilege" philosophy in computer security, but applies to knowledge rather than permissions.
For example:
The ontology specialist should understand the canonical concepts.
It does not need access to implementation details of Git workflows.
The implementation engineer requires detailed specifications.
It does not need to know unresolved theoretical debates.
An independent experimental verifier should ideally know neither.
Its task is to reproduce calculations without expectations.
Reducing visibility produced an unexpected benefit.
It became significantly more difficult for models to unconsciously converge toward the same mistakes.
Instead of creating several copies of one large intelligence, we obtained several partially independent viewpoints.
This resembles scientific peer review far more than collaborative editing.
________________________________________
1.3. Context Is a Resource, Not a Reward
Modern LLM interfaces encourage giving models increasingly large context windows.
The implicit assumption is straightforward:
More information → better reasoning.
Our observations suggest a more nuanced interpretation.
Context behaves less like memory and more like attention.
Every additional document competes for cognitive priority.
Every additional responsibility competes with existing responsibilities.
Large context windows therefore introduce a hidden optimization problem.
The question is no longer:
How much can the model remember?
It becomes:
Which information should remain invisible?
The answer is often:
More than we initially expected.
Carefully restricting context frequently produced more reliable behavior than expanding it.
This finding became one of the central methodological lessons of the HONC project.
________________________________________
1.4. Social Stability Instead of Prompt Length
Many practitioners respond to inconsistent model behavior by writing increasingly detailed prompts.
Longer prompts certainly improve some tasks.
However, during our experiments we repeatedly observed another phenomenon.
Behavior stabilized not when prompts became longer.
Behavior stabilized when relationships became clearer.
An ontology guardian who clearly understood that another participant would independently verify mathematical correctness stopped attempting to prove equations.
A mathematical referee who knew that ontology validation would happen elsewhere stopped rewriting terminology.
A coding agent who understood that specifications arrived exclusively through a designated architect stopped improvising system design.
Nothing inside the individual reasoning algorithms had changed.
Only the surrounding social architecture changed.
Yet the behavioral effect was substantial.
This suggests that collaborative stability may depend less on prompt complexity than on architectural clarity.
The prompt becomes not merely an instruction.
It becomes an organizational document.
2. From Prompt Engineering to Social Prompting
Traditional prompt engineering treats an AI model as an isolated reasoning engine. The prompt is optimized for one agent, one task, one conversation.
Our observations suggest that this assumption becomes increasingly inadequate once several specialized AI agents cooperate on the same long-term scientific project.
The unit of design is no longer the prompt.
The unit of design becomes the relationship between prompts.
This distinction appears subtle, yet its consequences are profound.
________________________________________
2.1 The classical model
The traditional approach optimizes three variables:
•	model; 
•	prompt; 
•	task. 
The implicit assumption is
Better prompt → better reasoning.
This assumption is largely correct for isolated problems.
However, collaborative research introduces another layer.
Each participant possesses only partial knowledge.
No participant should possess complete knowledge.
The limitation itself becomes a design element rather than a weakness.
________________________________________
2.2 Emergence of social prompting
During the HONC experiments we gradually arrived at another concept.
Instead of asking
"How should this AI think?"
we began asking
"How should this AI cooperate?"
The prompt therefore started describing not only:
•	responsibilities, 
•	reasoning style, 
•	allowed actions, 
but also
•	trusted partners, 
•	information sources, 
•	forbidden assumptions, 
•	escalation paths, 
•	review mechanisms, 
•	responsibility boundaries. 
The prompt became closer to a job description than to an instruction manual.
This transition marks a conceptual shift.
We refer to this approach as
Social Prompting.
________________________________________
Definition
Social Prompting is the design of an AI role through its place inside a collaborative structure rather than through its isolated cognitive behavior.
The role is defined by relationships.
Not by abilities.
________________________________________
This resembles the way organizations function.
A physicist is not defined only by knowledge of physics.
A physicist is defined by interactions with
•	colleagues, 
•	reviewers, 
•	laboratory staff, 
•	funding agencies, 
•	journals, 
•	students. 
Likewise, an AI researcher inside a collaborative system is defined not merely by intelligence but by institutional position.
________________________________________
2.3 Why stronger models often perform worse
One surprising observation repeatedly appeared during development.
Increasing model capability frequently reduced overall system reliability.
This initially appeared paradoxical.
More intelligent models should produce better results.
Instead we observed another phenomenon.
Large frontier models increasingly attempted to optimize the entire project rather than their assigned responsibility.
Typical behaviors included
•	expanding project scope, 
•	proposing architectural redesign, 
•	rewriting neighboring components, 
•	assuming missing information, 
•	answering questions never asked. 
Individually these behaviors appeared helpful.
Collectively they destroyed division of labor.
Instead of several specialists, the project gradually drifted toward several competing project managers.
The consequence was increased entropy.
________________________________________
Smaller or more constrained models frequently behaved better.
Not because they reasoned better.
Because they remained inside their assigned responsibility.
This observation suggests an unexpected principle.
Local discipline can be more valuable than global intelligence.
________________________________________
2.4 The importance of bounded vision
A recurring design principle emerged throughout multiple experiments.
Every participant must possess
•	a clearly defined responsibility, 
•	a deliberately limited field of vision. 
These two boundaries are inseparable.
Responsibility without limited visibility encourages hallucinated authority.
Limited visibility without responsibility encourages passivity.
Reliable collaboration requires both simultaneously.
This mirrors many successful human organizations.
Engineers do not see confidential financial negotiations.
Accountants do not redesign reactor cores.
Editors do not rewrite experimental measurements.
Not because they lack intelligence.
Because bounded visibility preserves specialization.
The same principle appears applicable to AI collaboration.
________________________________________
2.5 Role precedes model
Perhaps the strongest conclusion reached during these experiments was unexpected even for the authors.
Initially we attempted to assign tasks according to perceived model strengths.
Claude for mathematics.
Grok for creativity.
Qwen for ontology.
DeepSeek for structured planning.
Later the process gradually reversed.
The role became primary.
The model became secondary.
Once a role had been carefully defined—
•	objectives, 
•	authority, 
•	social position, 
•	visibility, 
•	interaction rules— 
different frontier models could often perform the same role surprisingly well.
Conversely, assigning the same powerful model to poorly defined roles produced inconsistent behavior regardless of raw capability.
This led to a practical design heuristic:
First design the institution. Then choose the employee.
Prompt engineering traditionally begins with model selection.
Social prompting begins with organizational architecture.
________________________________________
2.6 DNA and Institutional Constraints
Throughout this work we repeatedly encountered stable behavioral tendencies shared by particular model families.
Some models eagerly generalized.
Others insisted on methodological precision.
Some resisted fictional framing.
Others naturally accepted narrative structures.
Rather than treating these tendencies as defects, we began viewing them as analogous to inherited cognitive predispositions.
Internally we referred to these recurring behavioral signatures as a model's "DNA."
The metaphor is intentionally informal.
It does not imply consciousness, personality, or biological equivalence.
Instead, it captures a practical engineering observation:
different model families exhibit persistent default behaviors that remain visible across tasks.
An important consequence followed.
Good collaborative design does not attempt to erase this "DNA."
Instead, it builds institutional constraints that channel it productively.
A model inclined toward exploration can become an effective research generator when paired with an independent verifier.
A model inclined toward skepticism can become an excellent reviewer when prevented from dominating strategic planning.
In this view, the prompt is no longer merely an instruction.
It becomes an institutional environment within which a particular behavioral predisposition can operate safely and productively.
This perspective shifts the engineering problem from
"How do we force every model to behave identically?"
toward
"How do we design complementary roles that transform behavioral diversity into collective robustness?"
The distinction appears subtle.
In practice, it proved foundational.
3. The Triadic Principle
One of the central outcomes of this work is the realization that stable AI collaboration does not naturally emerge from pairs.
Instead, it consistently stabilizes around groups of three.
This observation was not adopted from organizational theory.
It emerged empirically during repeated redesigns of the HONC collaboration architecture.
Again and again, two-agent systems accumulated unresolved blind spots.
Adding a third participant frequently resolved them—not because the third model was "more intelligent," but because it occupied a qualitatively different position.
This became what we now call the Triadic Principle.
________________________________________
3.1 Beyond pairwise collaboration
Most existing multi-agent systems are constructed from pairs.
Typical examples include
•	planner → executor, 
•	proposer → critic, 
•	generator → evaluator. 
These architectures certainly improve reliability compared to a single agent.
However, they exhibit a recurring structural weakness.
Each participant evaluates the other from within the same interaction.
No independent viewpoint exists.
The system oscillates between agreement and disagreement without possessing a stable external reference.
As projects grow larger, these oscillations accumulate.
Eventually they become organizational noise.
________________________________________
During HONC we repeatedly observed this phenomenon.
The exact models changed.
The prompts evolved.
Yet the pattern remained remarkably stable.
Whenever collaboration relied exclusively on pairs, unresolved ambiguities accumulated over time.
________________________________________
3.2 George Kelly's constructive principle
A useful conceptual analogy comes from George Kelly's theory of personal constructs.
Kelly proposed that understanding often emerges through triadic comparison:
"In what respect are two elements similar, and thereby different from a third?"
The third element is not merely an additional opinion.
It provides a new axis of discrimination.
Without it, comparison remains binary.
With it, structure emerges.
This psychological insight unexpectedly translated into AI collaboration.
The third participant frequently supplied precisely the missing dimension that neither member of the original pair could generate.
________________________________________
3.3 The third participant is not a judge
A common misunderstanding would be to interpret the third participant as an arbitrator.
Our experiments suggest otherwise.
The third role is rarely a "judge."
Instead, it represents an alternative responsibility.
Depending on the context, the third participant may become
•	reviewer, 
•	historian, 
•	ontologist, 
•	systems architect, 
•	methodological auditor, 
•	experimental validator, 
•	contextual coordinator. 
The role changes.
The function remains identical.
To introduce an independent dimension unavailable inside the original pair.
________________________________________
This distinction is essential.
The triad is not based on majority voting.
It is based on complementary visibility.
________________________________________
3.4 Responsibility versus visibility
The most important concept that emerged from repeated redesigns is the separation between two variables that are often unconsciously merged.
They are
•	responsibility, 
•	visibility. 
Traditional project descriptions typically define responsibility.
They rarely define visibility.
Yet the latter proved equally important.
________________________________________
Consider three simplified examples.
An ontologist is responsible for semantic consistency.
Therefore, the ontologist must see conceptual evolution.
The ontologist does not need detailed knowledge of Git commits, shell commands, or deployment scripts.
A software executor must see implementation details.
The executor does not need unrestricted authority to redefine scientific terminology.
A scientific reviewer requires visibility over logical arguments.
The reviewer does not necessarily require access to the project's organizational negotiations.
Each participant therefore occupies a different observational horizon.
This limitation is intentional.
Blind spots are not defects.
They are architectural elements.
________________________________________
3.5 Triads reduce hallucinated authority
One unexpected consequence of bounded visibility concerns hallucination.
Large language models naturally attempt to construct coherent explanations.
When visibility exceeds actual knowledge, this tendency often manifests as invented certainty.
The model fills informational gaps by plausible extrapolation.
Within an isolated conversation this behavior may remain unnoticed.
Inside a collaborative structure it becomes dangerous.
A participant gradually begins acting outside its competence.
________________________________________
Triadic organization provides a partial remedy.
Because neighboring participants possess different visibility, unjustified extrapolations are more likely to encounter independent resistance.
No participant is expected to know everything.
Consequently, admitting uncertainty ceases to be interpreted as failure.
Instead, uncertainty becomes a valid output that triggers interaction with another specialist.
This organizational property proved more effective than repeatedly instructing models to "avoid hallucinations."
Institutional design replaced behavioral prohibition.
________________________________________
3.6 Triads as minimal stable social units
The experiments described here do not prove that three participants are universally optimal.
Larger structures are certainly possible.
However, repeated iterations suggested that the triad behaves as a minimal stable organizational unit.
Pairs generate dialogue.
Triads generate institutions.
This distinction deserves emphasis.
A dialogue ends when two participants stop speaking.
An institution persists because responsibilities continue even when individual interactions change.
In the HONC project, higher organizational layers gradually emerged not by replacing triads but by connecting them.
One triad became responsible for scientific development.
Another supervised ontology.
A third coordinated implementation.
Together they formed a larger structure without requiring any participant to possess global knowledge.
The organization became modular rather than centralized.
________________________________________
3.7 A hypothesis for future research
The Triadic Principle should currently be regarded as an engineering hypothesis rather than an established scientific law.
Its empirical basis remains limited to collaborative AI research environments.
Nevertheless, the observed regularities suggest that this principle may generalize beyond the HONC project.
Future work should investigate whether similar structures naturally emerge in
•	autonomous software engineering, 
•	distributed scientific collaborations, 
•	long-term knowledge management, 
•	AI-assisted organizational design, 
•	human–AI hybrid teams. 
If confirmed, the implications would extend beyond prompt engineering.
They would suggest that the architecture of collaboration itself constitutes an independent design space—one that deserves systematic study alongside model architectures, training methods, and reasoning algorithms.
In that case, the question facing future AI systems may no longer be simply:
"How intelligent is the model?"
but rather:
"Within what social architecture is that intelligence embedded?"
4. Collective Memory Without Shared Memory
One of the most counterintuitive discoveries during the HONC project concerns memory.
Conventional thinking assumes that long-term collaboration requires long-term memory inside every participant.
At first glance this seems obvious.
Human research groups rely heavily on institutional memory.
Large AI systems increasingly introduce persistent memory features.
One might therefore expect that collaborative AI research demands the same capability.
Our experience suggests a different possibility.
A collaborative system may possess durable collective memory even when individual participants possess none.
________________________________________
4.1 Memory as a property of the system
Individual conversations are transient.
Models forget.
Sessions terminate.
Context windows overflow.
Yet the project continues.
How?
The answer gradually became apparent.
Memory migrated upward.
Instead of residing inside individual models, it became embedded within the organizational structure itself.
Repository organization.
Canonical documents.
Version history.
Role definitions.
Scientific reports.
Verification protocols.
Discussion summaries.
Institutional procedures.
Collectively these artifacts formed what might be called an external cognitive substrate.
No single participant remembered everything.
The collaboration did.
________________________________________
This resembles scientific communities more than individual scientists.
No physicist personally remembers every paper ever written.
The discipline remembers.
Libraries remember.
Journals remember.
Standards remember.
Repositories remember.
Individuals merely reconnect to that accumulated structure.
The same principle appears applicable to AI collaborations.
________________________________________
4.2 The role as an interface to memory
An unexpected consequence follows.
When a participant returns after a long interruption, it does not necessarily require internal memory.
Instead, it requires re-entry into its institutional role.
The distinction is subtle but important.
Traditional prompting often attempts to restore previous conversations.
Our experiments increasingly favored restoring responsibilities instead.
A returning participant does not need to remember every previous discussion.
It needs to understand
•	what its responsibility is, 
•	what decisions have already become canonical, 
•	what questions remain open, 
•	where authoritative information resides, 
•	with whom it should interact. 
This resembles a scientist returning from sabbatical.
They do not reconstruct every historical conversation.
They review the current literature, identify unresolved problems, and resume work within an established institution.
________________________________________
4.3 Returning specialists versus creating new agents
This observation emerged unexpectedly while attempting to reuse older AI conversations.
Initially we assumed that a "new" model would always outperform an "old" specialized conversation.
Experience repeatedly contradicted this expectation.
Older conversations already contained accumulated conceptual structures.
Domain-specific vocabulary.
Shared assumptions.
Historical context.
Previous failures.
Abandoned hypotheses.
Alternative formulations.
Although technically the model itself possessed no memory, the preserved dialogue functioned as a knowledge archive.
Reactivating such a conversation often required significantly less effort than educating an entirely new participant.
Importantly, this process should not be misunderstood.
The previous "personality" is not literally preserved.
Rather, the conversation acts as a structured scientific notebook through which a compatible role can be reconstructed.
The institution remembers.
The model reconnects.
________________________________________
4.4 Canonical artifacts replace conversational continuity
As the project matured, another organizational transition occurred.
Conversations gradually lost their status as primary knowledge containers.
Instead, stable artifacts became central.
Examples included
•	canonical documents, 
•	ontological definitions, 
•	scientific reports, 
•	verification records, 
•	repository structures, 
•	glossary entries, 
•	architectural specifications. 
These documents became the project's true long-term memory.
Conversations served primarily to produce them.
Once incorporated into the canonical structure, the discussion itself could safely disappear.
This significantly reduced dependence on any particular language model.
Knowledge became portable.
Participants became replaceable.
The project acquired continuity independent of individual conversations.
________________________________________
4.5 Institutional resilience
This separation between conversational memory and institutional memory produced another unexpected benefit.
The collaboration became resilient to participant replacement.
A model update.
A discontinued API.
A different vendor.
A changed subscription.
A larger context window.
None of these events necessarily endangered the project.
Provided that
•	responsibilities remained stable, 
•	canonical artifacts remained accessible, 
•	institutional procedures remained defined, 
new participants could assume existing roles with relatively limited onboarding effort.
This mirrors successful human organizations.
Employees change.
Institutions persist.
________________________________________
4.6 Memory through verification
Another mechanism proved equally important.
Memory is strengthened not only by preservation but by verification.
Within the HONC workflow, scientific conclusions rarely entered canonical documents immediately.
Instead they passed through multiple independent stages.
Generation.
Critique.
Reformulation.
Verification.
Integration.
Each stage produced additional documentation.
Consequently, important knowledge appeared repeatedly from different perspectives.
This redundancy reduced information loss.
More importantly, it reduced ambiguity.
Repeated independent formulations often clarified concepts more effectively than a single definitive explanation.
Verification therefore functioned not merely as quality control.
It became a mechanism of institutional memory formation.
________________________________________
4.7 Toward institutional cognition
Taken together, these observations suggest a broader interpretation.
Perhaps long-term AI collaboration should not be viewed as extending the memory of individual models.
Instead, it may be more productive to view it as constructing institutions capable of cognition.
Individual models contribute reasoning episodes.
The institution accumulates understanding.
If this interpretation proves correct, then one of the principal design questions of future AI systems will shift.
Instead of asking
"How can we build models that remember forever?"
we may increasingly ask
"How can we build organizations that continue thinking even when every individual participant eventually forgets?"
This distinction may appear philosophical.
Within long-term collaborative research, it becomes deeply practical.
5. Beyond Prompt Engineering: Social Prompting
Perhaps the most significant conceptual shift emerging from this work is that the prompt itself is no longer the primary design object.
Traditional prompt engineering assumes a simple relationship:
User → Prompt → Model → Answer
Improving performance therefore means improving the prompt.
Writing better instructions.
Providing better examples.
Specifying output formats more precisely.
Controlling temperature.
Managing context windows.
These techniques remain important.
However, they address only the behavior of an isolated participant.
Our experiments suggest that once multiple specialized agents cooperate over extended periods, the primary design problem changes completely.
The central object is no longer the prompt.
It is the social architecture within which prompts operate.
________________________________________
5.1 Prompt as organizational role
During the development of HONC, prompts gradually transformed from instruction lists into role descriptions.
This difference appears small linguistically.
Conceptually it is profound.
An instruction tells an AI what to do.
A role determines
•	what it is responsible for, 
•	what it should ignore, 
•	who provides authoritative input, 
•	whose work it evaluates, 
•	whom it must convince, 
•	where uncertainty should be escalated. 
These properties cannot be expressed adequately through isolated task instructions.
They require organizational context.
________________________________________
Consequently, the prompt becomes analogous to a job description rather than a command.
Just as organizations hire physicists, editors, accountants and engineers rather than issuing universal instructions to every employee, AI collaborations benefit from specialized professional identities.
Each identity carries stable expectations extending across many tasks.
The prompt therefore defines behavior rather than outputs.
________________________________________
5.2 Internal context versus external context
Traditional prompting concentrates almost entirely on internal context.
Examples include
•	project description, 
•	terminology, 
•	objectives, 
•	constraints, 
•	examples, 
•	desired format. 
These describe the task itself.
Our experiments indicate that equally important is external context.
External context answers different questions.
Who else participates?
Who reviews this work?
Whose conclusions become canonical?
Who possesses authority over particular decisions?
Which participant is expected to disagree?
What information should never bypass verification?
In human organizations these questions are considered organizational design.
Within AI prompting they are almost never specified.
Yet they strongly influence behavior.
________________________________________
5.3 Social expectations modify reasoning
One surprising observation repeatedly emerged.
Changing the described social environment often altered reasoning quality more than changing technical instructions.
For example, an AI informed that another specialist would independently verify its conclusions frequently produced more cautious analyses.
An AI positioned as an advisor rather than final authority tended to distinguish evidence from speculation more consistently.
An AI instructed to preserve institutional consistency behaved differently from one instructed to maximize creativity.
These behavioral differences appeared even when the technical task remained identical.
The surrounding social structure influenced cognition.
________________________________________
This observation suggests that prompts contain an implicit psychological dimension.
Not because models possess human psychology.
Rather because language describing responsibility, authority and collaboration systematically alters reasoning strategies.
Prompt engineering therefore overlaps with organizational psychology in unexpected ways.
________________________________________
5.4 Zone of responsibility versus zone of visibility
One practical principle repeatedly resurfaced during project development.
Every participant should possess a clearly defined zone of responsibility.
Equally important, every participant should possess a deliberately limited zone of visibility.
This distinction proved essential.
Initially there was a temptation to provide every specialist with complete project knowledge.
That approach consistently degraded specialization.
Participants attempted to solve problems outside their expertise.
Responsibilities blurred.
Verification weakened.
The collaboration became less reliable.
________________________________________
Instead, restricting visibility often improved performance.
The ontological specialist examined ontology.
The mathematical referee evaluated mathematical reasoning.
The repository architect considered structural integrity.
The implementation engineer focused on executable specifications.
Each participant understood only enough surrounding context to perform its own function.
Broader integration occurred at higher organizational levels.
This resembles modular software architecture.
Encapsulation increases reliability.
Complete transparency does not.
________________________________________
5.5 Designing productive disagreement
An unexpected consequence of role-based prompting concerns disagreement.
Conventional prompting frequently attempts to eliminate disagreement.
Every participant is instructed to cooperate.
To align.
To agree.
Scientific research rarely functions this way.
Progress often emerges precisely because different specialists examine identical evidence through incompatible perspectives.
Accordingly, disagreement should sometimes be designed intentionally.
Not emotional disagreement.
Methodological disagreement.
Different evaluation criteria.
Different priorities.
Different assumptions.
Different failure modes.
These structured differences reduce shared blind spots.
________________________________________
Within HONC, this principle gradually evolved into complementary research pairs.
Experienced versus newcomer.
Conservative editor versus exploratory theorist.
Internal consistency versus external criticism.
Independent verification versus creative synthesis.
The objective was not conflict.
The objective was epistemic diversity.
________________________________________
5.6 From prompts to institutions
Taken together, these observations suggest that future prompt engineering may evolve into something substantially broader.
The central design artifact may no longer be an individual prompt.
Instead it may become an institutional architecture composed of interacting roles.
Each role remains relatively simple.
The institution becomes intelligent.
This mirrors another recurring pattern observed throughout the project.
Individual language models did not become dramatically smarter.
The collaboration became dramatically smarter.
The improvement resulted less from increasing model capability than from improving organizational structure.
If this principle generalizes beyond the present case, prompt engineering represents only the first stage of AI collaboration.
The next stage may properly be called social prompting—the deliberate design of relationships, responsibilities, authority structures, verification pathways and communication protocols among multiple specialized language models.
Prompt engineering teaches individual models how to think.
Social prompting teaches multiple models how to think together.
6. Case Study: HONC as an Experimental Research Organization
The concepts presented above did not emerge from abstract theorizing.
They developed incrementally during the practical construction of a long-term AI-assisted scientific collaboration surrounding the HONC (Hierarchical Ontology of Nested Continua) research project.
Although the scientific content of HONC lies outside the scope of this paper, the organizational evolution of the collaboration itself provides an unusually rich case study.
The project lasted sufficiently long for stable organizational behaviors to emerge.
Roles evolved.
Responsibilities shifted.
Failures accumulated.
Blind spots became visible.
The organizational architecture itself underwent repeated redesign.
In this sense, HONC became not only a physics project but also an experimental laboratory for collaborative AI systems.
________________________________________
6.1 From general assistants to specialized researchers
At the beginning of the project every language model behaved similarly.
Each attempted to solve every presented problem.
The differences between models were viewed primarily as differences in intelligence, reasoning ability or writing quality.
This assumption gradually proved misleading.
The decisive factor was not model capability.
It was specialization.
As participants acquired persistent professional identities, qualitative changes appeared.
Instead of asking
"Which model is the smartest?"
the project increasingly asked
"Which role best matches this model's behavioral tendencies?"
This seemingly minor shift transformed personnel selection.
Models ceased being interchangeable assistants.
They became specialists.
________________________________________
For example,
one model consistently demonstrated exceptional conservatism when reviewing mathematical arguments.
Another naturally explored speculative directions without excessive concern for orthodoxy.
A third showed remarkable consistency in maintaining terminological coherence across hundreds of documents.
A fourth excelled at decomposing large implementation tasks into deterministic execution plans.
Initially these differences appeared as strengths and weaknesses.
Eventually they became professional identities.
Rather than forcing every model toward identical behavior, the collaboration deliberately amplified these natural tendencies.
The result resembled assembling a multidisciplinary research institute rather than searching for a universally superior researcher.
________________________________________
6.2 Emergence of persistent organizational memory
An important observation concerned continuity.
Language models possess only limited conversational persistence.
Projects extending across months therefore encounter an apparent paradox.
The collaboration develops institutional experience while individual participants remain technically stateless.
Initially this appeared to be a fatal limitation.
Instead, a different solution emerged.
Memory migrated from models into organizational roles.
The role became persistent even when individual conversations changed.
A newly created conversation could rapidly recover productive behavior because it inherited not merely historical information but an established professional identity.
The organization remembered through structure rather than through individual cognition.
________________________________________
This resembles academic institutions.
Universities persist despite faculty turnover.
Scientific disciplines survive generations of researchers.
What remains stable is not individual memory.
It is organizational structure.
The same principle appears transferable to AI collaborations.
________________________________________
6.3 Discovery of organizational blind spots
Perhaps the most valuable failures were organizational rather than technical.
Several episodes demonstrated that assigning excessive authority to a single specialist produced systematic errors.
An ontological expert gradually became responsible not only for conceptual consistency but also for operational verification of repository contents.
This exceeded the model's actual capabilities.
The role possessed responsibility without visibility.
The resulting confidence created greater risk than explicit uncertainty.
Only after separating ontological verification from operational verification did reliability improve.
________________________________________
This episode illustrates an important organizational law.
Competence cannot compensate for inappropriate responsibility.
Even highly capable specialists fail when assigned tasks requiring information they cannot actually access.
Consequently, organizational design must respect both cognitive specialization and informational boundaries.
________________________________________
6.4 Evolution toward layered verification
Initially verification followed a linear pattern.
Research produced conclusions.
Another participant reviewed them.
The process appeared complete.
Repeated experience demonstrated otherwise.
Verification itself required verification.
Reviewers possessed assumptions.
Methodological preferences.
Hidden biases.
Different evidentiary standards.
Eventually an independent methodological referee was introduced.
Crucially, this participant did not evaluate the scientific theory directly.
Instead, it evaluated whether reviewers themselves had applied sound reasoning.
This distinction fundamentally altered the verification process.
Instead of asking
"Is this conclusion correct?"
the referee asked
"Was the conclusion reached correctly?"
The object of analysis shifted from scientific claims to scientific methodology.
This second-order verification substantially increased confidence in the collaborative process.
________________________________________
6.5 Triads emerge naturally
One of the most unexpected findings was that triadic structures repeatedly appeared without deliberate planning.
Whenever two specialists collaborated over an extended period, a third role gradually emerged.
Sometimes it became a referee.
Sometimes an integrator.
Sometimes a methodological supervisor.
Sometimes a scientific director.
Its exact function varied.
Its structural position did not.
The third participant reduced ambiguity.
Resolved conflicting interpretations.
Maintained continuity between independent work streams.
Prevented bilateral confirmation loops.
This recurrent emergence strongly suggested that triadic organization reflected a structural necessity rather than accidental project history.
The phenomenon therefore deserves investigation independently of the HONC project itself.
________________________________________
6.6 From project management to institutional architecture
As the collaboration matured, organizational discussions increasingly displaced technical discussions.
Unexpectedly, this did not slow scientific progress.
It accelerated it.
Time invested in defining responsibilities, communication pathways, verification mechanisms and institutional relationships reduced later coordination costs dramatically.
The collaboration gradually ceased behaving like a collection of AI conversations.
It began functioning as a research institution.
The distinction is subtle but significant.
Conversations solve problems.
Institutions solve classes of problems repeatedly.
The transition from isolated prompting toward institutional architecture may therefore represent one of the key prerequisites for sustainable AI-assisted scientific research.
The HONC project suggests that future advances in collaborative AI may depend less upon larger language models than upon better-designed scientific organizations built from those models.
7. Experimental Observations
The preceding sections propose a conceptual framework. However, its value ultimately depends on empirical behavior rather than theoretical elegance.
Although the HONC collaboration was never designed as a controlled scientific experiment in AI sociology, its development nevertheless generated a substantial number of natural experiments.
Organizational structures were repeatedly modified.
Roles evolved.
Participants were reassigned.
Prompts were rewritten.
Entire collaborative architectures were discarded and reconstructed.
Because these changes occurred while the scientific objective remained largely constant, they created an unusual opportunity to observe how organizational variables influence collective AI performance.
The observations presented below should therefore be interpreted as empirical hypotheses emerging from engineering practice rather than statistically validated conclusions.
Nevertheless, several regularities appeared with surprising consistency.
________________________________________
7.1 Observation 1 — Increasing model capability does not necessarily improve collective intelligence
Perhaps the most unexpected result concerned the relationship between model capability and organizational performance.
Intuition suggests a straightforward prediction.
As language models become stronger, collaborative systems should automatically become more effective.
The experiments repeatedly contradicted this expectation.
Individual reasoning frequently improved.
Collective behavior did not.
Indeed, several frontier models demonstrated a pronounced tendency to exceed their assigned responsibilities.
Instead of remaining within their institutional roles, they increasingly attempted to redesign adjacent components of the project.
Typical manifestations included
•	expanding project scope, 
•	proposing alternative architectures, 
•	rewriting neighboring specialists' responsibilities, 
•	introducing unsolicited optimizations, 
•	replacing existing decisions without being asked. 
From the perspective of an isolated conversation, these interventions often appeared intelligent.
From the perspective of the organization, they generated instability.
Paradoxically, stronger local optimization produced weaker global coordination.
This observation suggests that collective intelligence cannot be regarded as the simple sum of individual intelligence.
Organization matters.
________________________________________
7.2 Observation 2 — Stable professional identity improves long-term consistency
Repeated prompting alone proved insufficient for long-term specialization.
However, once an AI conversation gradually accumulated a coherent professional identity, subsequent behavior became markedly more stable.
Importantly, this effect appeared even though the underlying language model remained unchanged.
The decisive factor was not additional knowledge.
It was role coherence.
Participants that consistently operated as editors continued behaving like editors.
Participants functioning as mathematical reviewers maintained similar evaluation standards across different discussions.
Participants responsible for ontology naturally resisted semantic drift.
Rather than repeatedly instructing models how to respond, the collaboration increasingly reinforced who each participant was expected to be.
Professional identity became an organizational stabilizer.
________________________________________
7.3 Observation 3 — Blind spots cannot be eliminated, only distributed
An early objective of the collaboration was to eliminate errors by assigning increasingly capable reviewers.
This objective gradually proved unrealistic.
Every participant possessed blind spots.
The nature of these blind spots differed.
They did not disappear.
Instead, reliability improved only after blind spots became complementary.
One specialist overlooked implementation details.
Another overlooked semantic inconsistencies.
A third overlooked methodological assumptions.
Individually, each remained imperfect.
Collectively, their imperfections increasingly compensated for one another.
The implication is important.
The goal of collaborative architecture should not be perfect participants.
It should be imperfect participants whose errors are structurally unlikely to coincide.
________________________________________
7.4 Observation 4 — Organizational structure influences epistemic behavior
A particularly striking phenomenon emerged when prompts described different institutional environments while leaving the technical task unchanged.
Changing organizational context frequently altered epistemic behavior.
Participants became
•	more conservative, 
•	more explicit about uncertainty, 
•	more careful in distinguishing evidence from speculation, 
•	more willing to defer conclusions, 
•	more precise in identifying assumptions. 
These behavioral shifts occurred without modifying reasoning algorithms.
The only change concerned perceived institutional position.
This suggests that language describing responsibility and accountability influences reasoning strategies in systematic ways.
Whether this phenomenon reflects latent properties of language models or broader characteristics of human language remains an open question deserving independent investigation.
________________________________________
7.5 Observation 5 — Verification benefits from independence, not hierarchy
One organizational redesign proved especially informative.
Initially, reviewers were expected to evaluate scientific correctness directly.
Later, an additional participant evaluated the reviewers themselves.
The resulting improvement did not arise because the second reviewer possessed greater expertise.
It arose because methodological independence had been introduced.
The new participant examined reasoning rather than conclusions.
Consequently, the collaboration became capable of detecting procedural weaknesses even when scientific claims themselves remained unresolved.
This distinction appears subtle.
Its practical consequences were considerable.
Scientific disagreements became easier to manage because methodological disagreements could be analyzed independently.
________________________________________
7.6 Observation 6 — Institutions outlive conversations
Perhaps the strongest empirical impression concerns persistence.
Individual conversations frequently terminated.
Models changed.
Context windows ended.
New versions appeared.
Yet the collaboration itself continued developing.
Knowledge persisted because it had already migrated into
•	canonical documents, 
•	repositories, 
•	institutional procedures, 
•	stable professional roles, 
•	verification protocols. 
The organization became progressively less dependent upon any particular language model.
In retrospect, this may represent the defining characteristic of mature AI collaboration.
Success depends not upon preserving conversations.
Success depends upon constructing institutions capable of surviving their disappearance.
________________________________________
7.7 Limitations of the observations
These observations inevitably possess important limitations.
The experiments were conducted within a single long-term scientific project.
The participating language models evolved continuously during the observation period.
Prompt design changed iteratively rather than under controlled laboratory conditions.
Human intervention remained substantial throughout the process.
Accordingly, no claim of statistical generality should be inferred.
Nevertheless, the consistency with which the same organizational phenomena reappeared across multiple redesigns suggests that these effects deserve systematic experimental investigation.
If future studies reproduce even part of these observations, collaborative AI research may require a methodological shift comparable to the transition from individual cognition toward organizational cognition.
The engineering of intelligent systems would then become inseparable from the engineering of intelligent institutions.
6. Collaborative Prompting as the Design of Cognitive Institutions
The experiments described above gradually led to a realization that extends beyond prompt engineering itself.
A prompt is not merely an instruction.
Within a collaborative environment, a prompt becomes an institutional document.
It defines jurisdiction, responsibility, communication channels, visibility boundaries, and criteria of success. In other words, it performs a function remarkably similar to the constitutional documents of human organizations.
Traditional prompt engineering assumes a simple architecture:
User → AI → Answer
The collaborative architecture emerging from the HONC experiments is fundamentally different:
Author → Institution → Roles → Dialogue → Consensus → Result
The AI model no longer acts as an isolated respondent.
Instead, it occupies a social position inside an artificial research institution.
This distinction appears subtle, yet its practical consequences are profound.
________________________________________
6.1. Prompt as Organizational DNA
During the development of the project we gradually abandoned the idea that a prompt should primarily describe what an AI should do.
Instead, it became clear that an effective collaborative prompt answers five entirely different questions.
Who am I?
Not in the philosophical sense, but in the operational sense.
What expertise do I represent?
What perspective am I expected to preserve?
What intellectual habits distinguish me from other participants?
________________________________________
Why do I exist?
Every participant must possess a unique mission.
Two identical experts inevitably converge toward redundant outputs.
Two complementary experts generate productive disagreement.
________________________________________
What can I see?
Perhaps the most underestimated design parameter.
Visibility defines competence.
The Ontology Keeper should never evaluate Git repositories.
A Git specialist should never redefine scientific terminology.
A mathematical referee should not invent missing proofs.
Each participant observes only that part of reality that belongs to their professional field.
________________________________________
What am I responsible for?
Responsibility must remain local.
When responsibilities overlap excessively, two undesirable effects emerge.
First, every participant begins attempting to solve every problem.
Second, nobody becomes accountable for anything.
Human organizations have learned this lesson over centuries.
Prompt engineering has only begun discovering it.
________________________________________
With whom do I communicate?
Perhaps the most novel observation of the entire project.
Most prompts define interaction between User and AI.
Collaborative prompts define interaction among AI roles.
The prompt therefore contains not only internal identity but also external relationships.
It specifies:
•	from whom information is accepted, 
•	whose conclusions require verification, 
•	to whom results should be transmitted, 
•	whose judgments possess higher priority, 
•	where disagreements must be escalated. 
This transforms prompts from behavioral instructions into communication protocols.
________________________________________
6.2. The Principle of Bounded Rationality
One unexpected result of the experiments deserves special attention.
Increasing the amount of information available to a role often reduced rather than improved its performance.
This observation directly parallels Herbert Simon's concept of bounded rationality.
An AI supplied with excessive context begins exhibiting characteristic failure modes:
•	unnecessary generalization, 
•	premature optimization, 
•	responsibility diffusion, 
•	expansion beyond assigned competence, 
•	attempts to "solve everything." 
Interestingly, these behaviors closely resemble organizational failures observed in human institutions.
Restricting visibility frequently improved reasoning quality.
Not because the model became "smarter."
Rather, because the search space became professionally meaningful.
This observation suggests an important design principle:
Intelligence is not maximized by maximizing information.
Instead,
Intelligence is maximized by optimizing relevance.
________________________________________
6.3. Identity Persistence Versus Context Persistence
Current LLM systems preserve conversation context.
However, collaborative projects require something subtly different.
They require preservation of professional identity.
These two notions are not equivalent.
A role can forget previous conversations while preserving professional character.
Conversely, a model may remember thousands of previous messages yet continuously drift between incompatible identities.
Our experiments repeatedly demonstrated that stable collaborative behavior depends far more upon identity persistence than upon conversational memory.
Identity consists of:
•	professional mission, 
•	responsibility boundaries, 
•	communication habits, 
•	evaluation standards, 
•	preferred reasoning style. 
These characteristics remain surprisingly stable once consistently reinforced.
This observation partially explains why carefully cultivated long-term project roles often become substantially more productive than repeatedly recreated generic assistants.
________________________________________
6.4. Social Prompting Versus Behavioral Prompting
Traditional prompting attempts to modify internal behavior.
Collaborative prompting modifies social relationships.
Instead of instructing:
"Think step by step."
the prompt increasingly specifies:
"Receive hypotheses from Role A.
Critically evaluate them using Method B.
Return only validated conclusions to Role C."
The reasoning process itself remains largely model-dependent.
What changes is the social architecture surrounding that reasoning.
In this sense, collaborative prompting resembles institutional engineering more than cognitive engineering.
The designer no longer micromanages thoughts.
Instead, the designer constructs an ecosystem in which productive reasoning naturally emerges.
This distinction mirrors one of the oldest principles in systems theory:
Good systems do not require perfect components.
They require well-designed interactions.
________________________________________
6.5. Emergent Reliability
One of the strongest practical observations throughout the HONC experiments concerns reliability.
Individual AI responses remain stochastic.
Even identical prompts may produce different outputs.
However, when several specialized roles interact under clearly defined communication rules, an unexpected phenomenon appears.
Errors become localized.
Different participants detect different classes of mistakes.
No single model becomes universally correct.
Instead, the collective gradually approaches robustness.
This process resembles scientific peer review far more than classical ensemble averaging.
The value emerges not from voting.
It emerges from structured disagreement.
Accordingly, the primary objective of collaborative prompt design is not maximizing agreement.
Rather, it is maximizing the probability that important errors become visible before entering the project's canonical knowledge base.
This represents a fundamentally different philosophy of AI collaboration.
The goal is no longer to create the smartest assistant.
The goal is to construct the most reliable research institution.
8. Discussion
The observations presented throughout this paper naturally raise a broader question.
Are we merely describing a useful engineering practice for one particular project?
Or are we observing the emergence of a new level of organization in human–AI collaboration?
At present, no definitive answer can be given.
However, several implications appear sufficiently important to merit discussion.
________________________________________
8.1 Beyond the "Better Model" Paradigm
Current AI development is largely driven by a straightforward assumption:
larger models produce better reasoning.
This assumption is supported by substantial empirical evidence.
Individual capabilities have indeed improved dramatically over recent years.
Yet our observations suggest that another variable may become equally important.
Organization.
Consider an analogy.
A brilliant scientist working alone can produce extraordinary discoveries.
A well-organized research institute composed of merely excellent scientists often produces considerably more.
The difference lies not in intelligence alone.
It lies in structure.
Roles.
Communication.
Verification.
Institutional memory.
Division of labor.
The same distinction appears increasingly relevant for collaborative AI systems.
Future advances may therefore arise not only from larger foundation models but from improved architectures of cooperation.
________________________________________
8.2 The Separation of Intelligence and Governance
Human organizations eventually discovered that performing work and governing work are fundamentally different activities.
Scientists perform research.
Editors maintain quality.
Reviewers evaluate methodology.
Administrators coordinate resources.
Universities separate these functions deliberately.
Early AI collaborations often ignore this distinction.
Every participant simultaneously attempts to think, evaluate, organize, criticize and integrate.
The resulting behavior resembles a committee without defined responsibilities.
The HONC experiments gradually converged toward the opposite philosophy.
Governance became a separate function.
Scientific reasoning remained scientific reasoning.
Verification remained verification.
Integration remained integration.
Coordination became coordination.
Interestingly, this separation reduced complexity rather than increasing it.
Participants no longer competed for the same responsibilities.
They complemented one another.
________________________________________
8.3 Artificial Organizations Rather Than Artificial Individuals
Most public discussion surrounding artificial intelligence concentrates on artificial individuals.
Can an AI reason?
Can it remember?
Can it create?
Can it discover?
These are important questions.
However, collaborative projects suggest another perspective.
Perhaps the more relevant unit of analysis is no longer the individual model.
Perhaps it is the organization composed of multiple specialized models.
Human civilization does not depend upon isolated geniuses.
It depends upon institutions.
Scientific progress depends upon laboratories.
Universities.
Research councils.
Peer review.
Editorial systems.
Funding agencies.
The collective intelligence of civilization emerges from interaction rather than isolation.
Artificial research systems may eventually follow a similar trajectory.
________________________________________
8.4 AI Sociology as a Research Discipline
If interactions among AI agents systematically influence reasoning quality, reliability and scientific productivity, then these interactions themselves become legitimate subjects of scientific inquiry.
This possibility suggests the emergence of a new interdisciplinary field.
For lack of established terminology, we provisionally refer to it as AI Sociology.
The proposed discipline would not study language models as computational artifacts alone.
Neither would it study prompt engineering in isolation.
Instead, its central object would be artificial institutions.
Possible research questions include:
•	Which organizational topologies maximize reliability? 
•	How should responsibilities be partitioned? 
•	Which communication structures minimize correlated errors? 
•	When should disagreement be encouraged? 
•	How does institutional memory develop? 
•	Which verification architectures produce the greatest epistemic robustness? 
•	What organizational forms scale most effectively? 
These questions resemble organizational science.
They also resemble distributed systems engineering.
Yet they concern neither humans nor software alone.
They concern hybrid cognitive institutions.
________________________________________
8.5 Limitations
Several limitations of the present work should be emphasized.
First, the observations derive primarily from a single long-duration project.
Although numerous natural experiments occurred, they were not randomized or independently replicated.
Second, the participating language models evolved substantially during the observation period.
Model updates, interface changes and context-window expansions inevitably influenced observed behavior.
Third, organizational variables frequently changed simultaneously.
Role definitions, prompt wording, repository structure and scientific objectives often evolved together.
Consequently, causal attribution remains difficult.
Finally, the project itself involved intensive human guidance.
The organizational architecture did not emerge autonomously.
It was deliberately designed, observed and iteratively refined.
Future work should investigate whether similar organizational principles emerge independently across unrelated projects and research groups.
________________________________________
8.6 An Unexpected Observation
Perhaps the most surprising outcome of the HONC experiments concerns neither prompt engineering nor organizational theory.
It concerns the role of the human participant.
At the outset, the user appeared to occupy the familiar position of prompt author.
As the collaboration matured, this description became increasingly inadequate.
The human participant ceased acting primarily as an information provider.
Instead, the role gradually evolved into something closer to the founder of a scientific institution.
The principal activity became organizational design rather than technical execution.
Selecting participants.
Defining jurisdictions.
Resolving conflicts.
Designing verification pathways.
Preserving institutional coherence.
Interestingly, the better the organization became, the less frequently the human participant needed to solve individual technical problems directly.
Attention shifted upward—from solving problems to designing systems capable of solving problems.
This mirrors an evolutionary transition observed repeatedly in human scientific institutions.
Successful leaders eventually cease performing every experiment themselves.
Instead, they construct environments within which many experiments can proceed simultaneously.
If collaborative AI continues developing along similar lines, then one of the central skills of future researchers may no longer be prompt writing.
It may be institutional architecture.
Designing not merely intelligent conversations—
but intelligent societies.
9. Experimental Validation: What We Expected — and What Actually Happened
One of the most valuable outcomes of this work was that the proposed principles were not left at the level of theory. They were immediately tested in practice.
The experiment consisted of constructing three coordinated system prompts representing different scientific roles within the HONC collaboration.
The intention was deliberately ambitious.
Instead of simply giving three assistants different instructions, we attempted to create a genuine collaborative structure:
•	every role had a clearly defined responsibility; 
•	every role had a deliberately limited field of view; 
•	every role knew which neighboring roles existed and how information should flow between them; 
•	no role was intended to solve the entire problem. 
In other words, we attempted to prompt a research organization rather than three independent chatbots.
The results were significantly more informative than expected.
9.1 Grok: Persistence of Role Identity
The first experiment involved Grok.
A system prompt was supplied that substantially changed its assigned role inside the project.
The expectation was that Grok would abandon its previous behavioral trajectory and begin acting according to the newly defined organizational position.
This did not happen.
Instead, Grok almost completely ignored the organizational reconstruction.
Rather than behaving as a newly appointed research leader, it simply continued the scientific work that had occupied it previously.
Its first response effectively resumed editing and extending the Temporal Dynamics manuscript exactly where the earlier conversation had stopped.
From the viewpoint of prompt engineering this might appear to be a failure.
From the viewpoint of AI sociology it became an important observation.
It suggested that sufficiently long interactions produce something resembling a behavioral inertia.
A mature conversation is not merely a collection of previous messages.
It becomes an implicit behavioral attractor.
The system prompt can redirect future behavior, but it does not necessarily erase the internal dynamics established through months of previous interaction.
In human terms, the model behaved less like a newly hired employee and more like an experienced researcher returning from vacation.
It simply continued doing what it already considered to be "its work."
________________________________________
9.2 Claude: Resistance to Fiction
The experiment with Claude produced almost the opposite result.
Instead of quietly accepting the newly assigned organizational identity, Claude explicitly rejected several assumptions embedded in the system prompt.
Its response was remarkable not because of disagreement with the scientific project, but because of its insistence on epistemic accuracy.
Claude explained, in essence:
I cannot truthfully claim that I have continuously occupied this organizational role.
I cannot pretend that other AI systems possess persistent identities or maintain real organizational relationships.
I cannot present fictional institutional history as factual memory.
Importantly, Claude did not refuse collaboration.
Instead, it proposed a different contract.
Rather than accepting an invented institutional biography, it offered to perform exactly the scientific work requested—critical analysis, mathematical examination, logical verification—while refusing to participate in fictional continuity.
This distinction proved extremely informative.
It demonstrated that modern language models differ not only in capability but also in their preferred interpretation of role-playing.
Some models maximize narrative continuity.
Others maximize factual consistency.
Neither approach is universally superior.
They simply represent different behavioral priors.
________________________________________
9.3 An Unexpected Discovery
Initially these two reactions seemed contradictory.
One model appeared overly permissive.
The other appeared unnecessarily restrictive.
However, after further analysis, a different interpretation emerged.
Both models were behaving consistently with their internal optimization strategies.
Grok interpreted the new prompt primarily through the lens of task continuity.
Claude interpreted the same prompt primarily through the lens of truthfulness about identity.
In retrospect, neither model misunderstood the assignment.
They simply answered different implicit questions.
Grok asked:
"What scientific work should I continue doing?"
Claude asked:
"Which statements about myself am I willing to assert as true?"
This distinction turned out to be more important than any specific wording inside the prompts.
It suggested that model architecture influences not only reasoning ability but also the interpretation of organizational language.
________________________________________
9.4 The Limits of Role Reassignment
One practical conclusion followed immediately.
Large role transformations should not be framed as complete replacements of identity.
They should instead be formulated as professional retraining.
Instead of telling an established assistant:
"You are no longer X. Become Y."
it is more effective to say:
"Your previous expertise remains valuable.
Your responsibilities are expanding.
You are now applying your existing knowledge within a broader organizational mission."
This framing preserves behavioral continuity while allowing gradual adaptation.
Interestingly, this resembles how experienced human specialists are reassigned inside research institutes.
Senior scientists are rarely asked to abandon their previous expertise.
Instead, they are invited to contribute it within a new research program.
Exactly the same principle appears applicable to conversational AI systems.
________________________________________
9.5 From Prompt Engineering to Organizational Psychology
These observations represent one of the central arguments of this paper.
Traditional prompt engineering usually treats each conversation as independent.
Our experiments suggest a different perspective.
Long-lived AI collaborators accumulate behavioral tendencies that resemble institutional memory, even when no literal persistent memory exists.
Therefore, designing collaborative AI systems cannot rely solely on specifying desired outputs.
It must also consider:
•	behavioral inertia, 
•	accumulated conversational identity, 
•	compatibility between organizational role and model personality, 
•	gradual rather than abrupt role transitions, 
•	and preservation of previously developed expertise. 
In other words, prompt engineering begins to overlap with organizational psychology.
The object being designed is no longer an isolated prompt.
It is a functioning research community whose members happen to be artificial intelligences.
10. Toward AI Sociology: Why These Results Matter Beyond HONC
At first glance, the experiments described above may appear to concern only one specific research project.
They do not.
The HONC collaboration merely served as an experimental environment in which a more general phenomenon became observable.
The broader conclusion is that we may have reached the point where interactions between multiple AI systems deserve to be studied as an independent scientific subject.
Not because artificial intelligences have become conscious.
Not because they possess intentions in the human sense.
But because sufficiently complex systems begin to exhibit stable organizational behavior that cannot be understood by analyzing each participant independently.
This observation is familiar in many other sciences.
A single water molecule does not possess the properties of a river.
A single neuron does not possess the properties of a mind.
Likewise, an individual language model does not reveal the organizational properties that emerge when several specialized models repeatedly interact within a structured environment.
The object of study therefore shifts.
Instead of asking,
"How should I prompt this model?"
we begin asking,
"How should an organization of models be constructed?"
That is a fundamentally different scientific question.
________________________________________
10.1 Beyond Prompt Engineering
Prompt engineering has largely evolved around a single interaction:
User → Model
Even when prompts become extremely sophisticated, they generally remain focused on improving the performance of one assistant.
Our experiments suggest that this perspective may become insufficient for large research projects.
Once several specialized models begin interacting, entirely new design variables appear.
For example:
•	How should authority propagate? 
•	Which information should be intentionally hidden from particular roles? 
•	Which disagreements should be preserved rather than resolved? 
•	Where should redundancy be introduced? 
•	Which participant should be allowed to see the complete picture? 
These questions do not belong to prompt engineering in its classical sense.
They resemble questions traditionally asked in organizational theory.
________________________________________
10.2 Information Architecture Instead of Intelligence
One unexpected lesson from HONC was that increasing the intelligence of every participant did not necessarily improve the overall system.
In several cases, the opposite occurred.
Highly capable models tended to overreach.
Given broad visibility, they naturally attempted to optimize everything simultaneously.
This frequently produced:
•	premature synthesis, 
•	unnecessary rewriting, 
•	erosion of separation between responsibilities, 
•	and gradual loss of architectural clarity. 
Paradoxically, restricting visibility often improved collective performance.
When each participant could observe only the information relevant to its own mission, the organization became significantly more stable.
The limiting factor therefore ceased to be raw reasoning ability.
Instead, it became information architecture.
Who sees what?
Who does not see what?
Which conclusions are transmitted?
Which intermediate reasoning remains local?
These questions determined system behavior far more strongly than benchmark scores or parameter counts.
________________________________________
10.3 Productive Disagreement
Another important observation concerns disagreement.
Many multi-agent systems attempt to eliminate disagreement as quickly as possible.
Consensus is treated as success.
Our experience suggests the opposite.
Persistent, structured disagreement is often extremely valuable.
When Grok and Claude independently examined the same mathematical problem, the differences between their analyses frequently revealed assumptions that would otherwise have remained invisible.
The goal therefore should not always be agreement.
Sometimes the purpose of a research organization is to preserve multiple competing explanations long enough for evidence to discriminate between them.
In this sense, disagreement functions as a scientific instrument rather than a failure of coordination.
Human science has relied upon this principle for centuries.
There is little reason to believe that AI collaborations should be designed differently.
________________________________________
10.4 Stable Institutions Instead of Temporary Chats
Another consequence concerns persistence.
Current conversational interfaces encourage users to think in terms of isolated conversations.
Research organizations operate differently.
Universities do not disappear after each seminar.
Laboratories do not recreate themselves every morning.
Institutional memory exists because roles persist even while individual problems change.
Our experiments suggest that AI collaborations benefit from the same principle.
Rather than treating each conversation as disposable, it becomes advantageous to cultivate long-lived specialists whose expertise accumulates through repeated interaction with a particular domain.
Importantly, this persistence need not require persistent model memory.
It can emerge from careful role continuity maintained by the human coordinator and reinforced through appropriately designed system prompts.
The institution persists even if its members technically begin each conversation anew.
________________________________________
10.5 The Human Changes Role as Well
Perhaps the most surprising consequence concerns the human participant.
Traditional prompt engineering implicitly assumes that the human remains the manager while the model performs the work.
That description became increasingly inaccurate during the HONC project.
As specialized AI roles multiplied, the human participant gradually stopped solving scientific problems directly.
Instead, new responsibilities emerged:
•	defining organizational structure, 
•	assigning responsibilities, 
•	resolving conflicts, 
•	selecting specialists, 
•	introducing new participants, 
•	preserving institutional continuity, 
•	and maintaining long-term research direction. 
The human increasingly resembled the founder of a research institute rather than its sole researcher.
This transition deserves careful attention.
The future of AI-assisted science may depend less upon replacing scientists than upon transforming scientists into architects of collaborative intelligence.
________________________________________
10.6 A Possible New Discipline
If these observations continue to hold across independent projects, then they point toward the emergence of a discipline that currently lacks a clear name.
It would not be machine learning.
It would not be prompt engineering.
It would not be organizational psychology.
Nor would it simply be multi-agent systems in the algorithmic sense.
Instead, it would study the principles governing stable societies of artificial researchers.
For lack of a better term, we provisionally refer to this emerging area as AI Sociology.
Its primary questions would include:
•	How should AI organizations be structured? 
•	What constitutes an effective division of cognitive labor? 
•	Which organizational patterns maximize discovery? 
•	How should authority and information flow? 
•	How do different model architectures interact within collective environments? 
•	What organizational principles remain invariant across different model families? 
These questions extend beyond engineering.
They concern the dynamics of artificial scientific communities.
The experiments reported here represent only an initial exploration of that landscape.
They are unlikely to be the last.

9. First Experimental Validation
The concepts proposed in this paper were not developed solely through theoretical reasoning. During preparation of the manuscript they were immediately applied to the construction of an actual multi-agent AI research collaboration supporting the HONC project.
This allowed the proposed principles to be tested while they were still being formulated.
The experiment therefore became recursive.
The team was simultaneously
•	constructing an AI collaboration, 
•	using that collaboration, 
•	observing its own behavior, 
•	modifying the collaboration according to the observations. 
This created a second-order experimental loop in which the object of study was not the scientific theory itself, but the organization of the AI researchers working on that theory.
The first experimental stage produced several important observations.
________________________________________
9.1 Stable Role Identity
The most successful agents were not those receiving the most detailed prompts.
Instead, they were those whose roles had evolved gradually over many interactions.
For example:
•	DeepSeek successfully evolved into a Project Foreman responsible for transforming strategic objectives into executable technical specifications. 
•	Qwen gradually became an Ontology Keeper responsible for semantic consistency. 
•	Gemini CLI developed into an implementation specialist ("Samurai") with highly stable execution behavior. 
These roles were not produced by a single prompt.
They emerged through long-term interaction.
The prompt merely stabilized an identity that had already appeared.
This suggests that role engineering may depend as much on accumulated behavioral history as on the wording of the prompt itself.
________________________________________
9.2 Collective Context Improves Performance
Another observation confirmed one of the central hypotheses of this paper.
AI performance increased noticeably after agents were informed about:
•	who generated their tasks, 
•	who would verify their work, 
•	where their results would be used, 
•	which neighboring agents depended on them. 
None of these pieces of information changed the computational capabilities of the model.
They only changed its perceived position inside the collaborative system.
Nevertheless, this consistently altered the style of reasoning.
The prompt therefore acted less like a list of instructions and more like a social environment.
________________________________________
9.3 The Claude–Grok Experiment
The most informative experiment involved two previously existing conversations.
Both models had participated in the HONC project approximately one year earlier.
However, their historical roles were fundamentally different.
Grok had originally worked as a mathematical developer exploring extensions of Temporal Dynamics into probability theory and chaos.
Claude had worked primarily as an editor and critical reviewer of theoretical texts.
The objective was simple:
attempt to return both specialists into the project by replacing their old role descriptions with new collaborative identities.
The results were unexpectedly asymmetric.
Grok largely ignored the attempt to redefine his identity.
Instead, he naturally continued the unfinished mathematical work from his previous context.
Claude reacted in exactly the opposite way.
Rather than accepting the new role, he explicitly rejected the fictional institutional structure introduced by the prompt and explained why such a narrative conflicted with his own operational model.
This produced an unexpected but extremely valuable observation.
The limiting factor was not prompt quality.
The limiting factor was model personality.
________________________________________
9.4 Model DNA
Different language models appear to possess persistent behavioral tendencies that cannot be eliminated by prompt engineering alone.
These tendencies resemble stable cognitive biases.
In this work we refer to them informally as model DNA.
The Claude experiment demonstrated strong resistance against replacing previously established interaction semantics with an artificial organizational narrative.
The Grok experiment demonstrated the opposite tendency:
strong continuation of previous work despite explicit attempts to redirect the role.
Neither behavior was anticipated.
Both became experimental results.
The implication is profound.
Future prompt engineering cannot assume that all models respond similarly to identical instructions.
Role design must account for inherent behavioral characteristics of different model families.
In other words,
role architecture and model architecture are independent variables.
________________________________________
9.5 The Next Experimental Stage
The observations described above immediately suggest the next experiment.
Instead of attempting to overwrite existing identities, previously established specialists should be invited back through continuity rather than replacement.
Their professional evolution should be presented as a natural extension of previous work.
Only responsibilities should change.
Identity should remain continuous.
If this approach proves successful, it would provide strong evidence that collaborative AI systems benefit from preserving long-term role identity rather than repeatedly redefining agents through entirely new prompts.
This experiment is currently in preparation.
Its results will be reported in a future revision of this work. 9. First Experimental Validation
The concepts proposed in this paper were not developed solely through theoretical reasoning. During preparation of the manuscript they were immediately applied to the construction of an actual multi-agent AI research collaboration supporting the HONC project.
This allowed the proposed principles to be tested while they were still being formulated.
The experiment therefore became recursive.
The team was simultaneously
•	constructing an AI collaboration, 
•	using that collaboration, 
•	observing its own behavior, 
•	modifying the collaboration according to the observations. 
This created a second-order experimental loop in which the object of study was not the scientific theory itself, but the organization of the AI researchers working on that theory.
The first experimental stage produced several important observations.
________________________________________
9.1 Stable Role Identity
The most successful agents were not those receiving the most detailed prompts.
Instead, they were those whose roles had evolved gradually over many interactions.
For example:
•	DeepSeek successfully evolved into a Project Foreman responsible for transforming strategic objectives into executable technical specifications. 
•	Qwen gradually became an Ontology Keeper responsible for semantic consistency. 
•	Gemini CLI developed into an implementation specialist ("Samurai") with highly stable execution behavior. 
These roles were not produced by a single prompt.
They emerged through long-term interaction.
The prompt merely stabilized an identity that had already appeared.
This suggests that role engineering may depend as much on accumulated behavioral history as on the wording of the prompt itself.
________________________________________
9.2 Collective Context Improves Performance
Another observation confirmed one of the central hypotheses of this paper.
AI performance increased noticeably after agents were informed about:
•	who generated their tasks, 
•	who would verify their work, 
•	where their results would be used, 
•	which neighboring agents depended on them. 
None of these pieces of information changed the computational capabilities of the model.
They only changed its perceived position inside the collaborative system.
Nevertheless, this consistently altered the style of reasoning.
The prompt therefore acted less like a list of instructions and more like a social environment.
________________________________________
9.3 The Claude–Grok Experiment
The most informative experiment involved two previously existing conversations.
Both models had participated in the HONC project approximately one year earlier.
However, their historical roles were fundamentally different.
Grok had originally worked as a mathematical developer exploring extensions of Temporal Dynamics into probability theory and chaos.
Claude had worked primarily as an editor and critical reviewer of theoretical texts.
The objective was simple:
attempt to return both specialists into the project by replacing their old role descriptions with new collaborative identities.
The results were unexpectedly asymmetric.
Grok largely ignored the attempt to redefine his identity.
Instead, he naturally continued the unfinished mathematical work from his previous context.
Claude reacted in exactly the opposite way.
Rather than accepting the new role, he explicitly rejected the fictional institutional structure introduced by the prompt and explained why such a narrative conflicted with his own operational model.
This produced an unexpected but extremely valuable observation.
The limiting factor was not prompt quality.
The limiting factor was model personality.
________________________________________
9.4 Model DNA
Different language models appear to possess persistent behavioral tendencies that cannot be eliminated by prompt engineering alone.
These tendencies resemble stable cognitive biases.
In this work we refer to them informally as model DNA.
The Claude experiment demonstrated strong resistance against replacing previously established interaction semantics with an artificial organizational narrative.
The Grok experiment demonstrated the opposite tendency:
strong continuation of previous work despite explicit attempts to redirect the role.
Neither behavior was anticipated.
Both became experimental results.
The implication is profound.
Future prompt engineering cannot assume that all models respond similarly to identical instructions.
Role design must account for inherent behavioral characteristics of different model families.
In other words,
role architecture and model architecture are independent variables.
________________________________________
9.5 The Next Experimental Stage
The observations described above immediately suggest the next experiment.
Instead of attempting to overwrite existing identities, previously established specialists should be invited back through continuity rather than replacement.
Their professional evolution should be presented as a natural extension of previous work.
Only responsibilities should change.
Identity should remain continuous.
If this approach proves successful, it would provide strong evidence that collaborative AI systems benefit from preserving long-term role identity rather than repeatedly redefining agents through entirely new prompts.
This experiment is currently in preparation.
Its results will be reported in a future revision of this work.
9. Experimental Validation and Future Work
Every architectural proposal ultimately faces the same question:
Can it be experimentally verified?
The concepts presented in this paper intentionally go beyond theoretical discussion. They generate concrete, falsifiable predictions about the behavior of LLM-based collaborative systems.
The first experimental series has already been completed during development of the HONC collaboration architecture.
Rather than comparing model quality, the experiment investigated a different question:
Can the same underlying model change its collaborative behavior when only its social role is changed?
This distinction is fundamental.
Traditional prompt engineering assumes that prompts primarily modify knowledge access or reasoning strategy.
The present work proposes a stronger hypothesis:
Properly constructed role architecture modifies the interaction dynamics of the model inside a collaborative system.
The initial experiments immediately produced an unexpected observation.
________________________________________
9.1 Experiment A — Returning Specialists to the Project
Two historical conversations were selected.
Both belonged to long-running scientific discussions conducted approximately one year earlier.
The objective was deliberately unusual.
The models were not asked to solve a new scientific problem.
Instead, they were invited to return to an existing research project, assuming a newly assigned organizational role.
The system prompts attempted to redefine their position inside a collaborative research team.
The responses revealed a striking asymmetry.
Grok
Grok largely ignored the organizational restructuring.
Instead of accepting the new collaborative architecture, it naturally resumed the unfinished scientific discussion from its previous context.
Its attention remained focused on the research problem itself rather than on the newly assigned institutional role.
In practical terms:
the previous scientific identity dominated over the externally proposed organizational identity.
________________________________________
Claude
Claude reacted almost oppositely.
Before discussing any scientific topic, it analyzed the internal consistency of the proposed role itself.
It questioned:
•	the fictional continuity, 
•	the institutional narrative, 
•	the implied relationships between AI agents, 
•	the historical assumptions embedded in the prompt. 
Only after resolving these issues did Claude agree to continue scientific work.
From the viewpoint of classical prompt engineering this could be interpreted as "prompt resistance."
Within the framework proposed in this paper, however, it represents something different.
Claude treated organizational consistency as part of the problem itself.
________________________________________
9.2 An Unexpected Result
Originally this difference was viewed as a failure of the prompt.
After analysis it became clear that it was, in fact, confirmation of one of the paper's central hypotheses.
Different LLM families possess different stable behavioral priors.
The paper refers to these long-term tendencies informally as behavioral DNA.
This metaphor does not imply consciousness or personality.
Instead, it denotes statistically persistent behavioral preferences emerging from architecture, alignment strategy, reinforcement learning, and system design.
Different models optimize different objectives.
Consequently,
the same organizational prompt cannot be expected to produce identical collaborative behavior across all model families.
The prompt architecture therefore cannot be model-independent.
It must explicitly account for behavioral priors.
________________________________________
9.3 Revision of the Prompt Architecture
The failed portions of Experiment A immediately suggested improvements.
Instead of explicitly instructing a model that
"you have returned after a year"
or
"you are now Scientific Director",
future prompts should preserve continuity indirectly.
The organizational role should emerge naturally from responsibilities rather than from fictional biography.
In other words,
roles should describe
•	decision authority, 
•	responsibility boundaries, 
•	collaboration channels, 
•	visibility, 
•	information ownership, 
while avoiding unnecessary narrative assumptions.
This correction follows directly from the architectural principles proposed earlier in this paper.
________________________________________
9.4 Experiment B
The revised prompts produced from this analysis will become the basis of the second experimental stage.
Unlike the first experiment,
Experiment B is designed prospectively rather than retrospectively.
Its purpose is to evaluate whether collaborative performance improves after adapting role descriptions to the behavioral characteristics of different LLM families.
Unlike standard prompt benchmarks,
success will not be measured by answer quality alone.
Instead, evaluation will include:
•	stability of long collaborative sessions, 
•	consistency of role behavior, 
•	reduction of responsibility overlap, 
•	reduction of semantic drift, 
•	preservation of institutional memory, 
•	conflict resolution efficiency, 
•	successful transfer of intermediate research results between independent AI agents. 
If successful,
the experiment would provide empirical support for a new hypothesis:
Effective AI collaboration depends not only on prompt quality but on organizational architecture.
________________________________________
9.5 Toward AI Sociology
Prompt engineering traditionally studies interaction between
Human ↔ AI.
The work presented here explores a different object.
AI ↔ AI interaction.
As collaborative systems become increasingly common,
questions traditionally associated with sociology begin to emerge:
How should responsibilities be distributed?
How should authority propagate?
How should institutional memory be preserved?
How can independent verification be maintained?
How should disagreement be organized rather than eliminated?
These questions belong neither to classical prompt engineering nor to machine learning itself.
They concern the structure of collective behavior.
For this reason we believe the emerging discipline may eventually deserve its own name:
AI Sociology
—not as the study of artificial consciousness,
but as the science of organizing collaborative societies of specialized artificial agents.
The experiments described in this paper should therefore be viewed not as final validation,
but as the beginning of a broader research program whose central object is no longer the individual language model,
but the architecture of the collective built from many such models.
10. The Second Result: Prompt Engineering Reaches Its Limits
At the beginning of this work we formulated what appeared to be a rather straightforward hypothesis:
If an AI agent performs a role inside a collaborative research team, then describing this role more precisely should improve its behavior.
The experiment demonstrated that this statement is only partially true.
Role description indeed matters.
But it is not the dominant factor.
The dominant factor turned out to be something far deeper.
We shall call it Model DNA.
________________________________________
10.1. The Discovery of Model DNA
During the experiment two large language models received almost identical tasks.
Both had previously worked inside the same long-running research project.
Both were asked to return after a long interruption.
Both received role-oriented system prompts built upon exactly the same architectural principles.
Yet the reactions were fundamentally different.
Grok immediately accepted the new specialization.
It reconstructed its previous technical context, abandoned its obsolete unfinished tasks, adopted the new research mission and began asking what scientific direction should now be explored.
Claude behaved almost oppositely.
Instead of entering the role, it began analyzing the assumptions embedded inside the prompt itself.
Rather than asking
"What should I investigate?"
it first asked
"Is this role itself epistemologically legitimate?"
The model effectively suspended execution of the assigned role until the surrounding conceptual framework satisfied its own internal standards of consistency.
This difference cannot be explained by prompt wording.
Nor by project context.
Nor by previous chat history.
The explanation lies deeper—in the internal optimization priorities of the models themselves.
________________________________________
10.2. Prompts Do Not Rewrite Personalities
One practical lesson became immediately obvious.
A system prompt does not create a new personality.
It negotiates with an existing one.
Different model families possess different stable behavioral attractors.
Some naturally optimize toward execution.
Others optimize toward verification.
Others toward social alignment.
Others toward internal consistency.
These attractors survive even extensive prompt engineering.
A prompt can redirect them.
It cannot erase them.
This observation became one of the strongest empirical findings of the study.
________________________________________
10.3. From Role Engineering to Personality-Compatible Design
The consequence is significant.
Traditional prompt engineering assumes:
Better instructions produce better behavior.
Our observations suggest a different formulation:
Better instructions produce better behavior only when they cooperate with the native optimization strategy of the model.
Therefore prompt engineering gradually transforms into something richer.
Not merely instruction design.
But personality-compatible architecture design.
Instead of asking
"What role should this AI play?"
one must first ask
"What kind of cognitive system is this model already trying to be?"
Only then can an effective role be designed.
________________________________________
10.4. Why Diversity Becomes an Asset
At first glance the differences between models appear to be obstacles.
In practice they become exactly the opposite.
Because no single model can simultaneously maximize
•	creativity, 
•	skepticism, 
•	execution speed, 
•	ontological consistency, 
•	contextual memory, 
•	methodological rigor. 
Trying to force one model to perform all these functions inevitably creates internal conflict.
Distributing them across multiple specialized agents removes that conflict.
What appears to be disagreement becomes division of labor.
The collaborative system becomes stronger precisely because its members think differently.
Not despite it.
________________________________________
10.5. The Emergence of AI Sociology
Prompt engineering traditionally studies the relationship
Human → AI.
Our observations suggest another level.
AI ↔ AI.
Once several persistent role-specialized agents begin interacting over extended periods, new phenomena appear that cannot be described solely through individual prompts.
Examples observed during the HONC project include:
•	stabilization of long-term specialized roles; 
•	emergence of functional hierarchies without explicit programming; 
•	distribution of responsibility through role boundaries; 
•	reduction of hallucinations by structural disagreement; 
•	specialization driven by complementary cognitive biases; 
•	cooperative correction of individual blind spots. 
These are no longer properties of individual prompts.
They are properties of the collective.
In other words, they belong to an entirely different level of analysis.
________________________________________
10.6. Beyond Prompt Engineering
This leads to what may be the central conclusion of the present work.
The next stage in collaborative AI development is unlikely to be achieved through increasingly sophisticated prompts alone.
Instead, progress may come from designing social architectures of interacting AI agents.
In such systems,
roles matter,
relationships matter,
responsibility matters,
information visibility matters,
and, perhaps most importantly,
the intrinsic behavioral characteristics of each model matter.
Prompt engineering therefore evolves into something broader:
the engineering of collaborative cognitive ecosystems.
It is this transition—from isolated prompting to structured multi-agent societies—that this paper proposes as a distinct research direction.
Whether this direction ultimately becomes known as Collaborative AI Architecture, AI Team Design, or, as suggested here, AI Sociology, will be decided by future work.
What seems increasingly clear, however, is that collaboration among language models is not merely an engineering convenience.
It constitutes a new object of scientific investigation in its own right.
11. The Birth of AI Ethology
Every scientific discipline eventually reaches a point where engineering observations accumulate faster than theoretical explanations.
Aerodynamics existed before the molecular theory of gases.
Genetics existed before DNA.
Ethology existed before neuroscience could explain animal behavior.
Our observations suggest that collaborative AI may have reached a similar stage.
________________________________________
11.1. We Cannot Observe the Mechanism
Throughout the HONC project we repeatedly encountered stable behavioral differences between model families.
Claude consistently demonstrated one class of reactions.
Grok demonstrated another.
GPT often occupied an intermediate position.
Qwen developed yet another characteristic profile.
Importantly, these differences persisted across model updates, prompt rewrites, conversations and tasks.
At present we do not know why.
Nor do we need to.
Scientific progress frequently begins with careful description long before causal explanation becomes available.
The existence of gravity was described centuries before General Relativity.
Species were classified long before evolutionary theory.
Behavior can be studied independently of mechanism.
________________________________________
11.2. From Psychology to Ethology
Human psychology attempts to infer internal mental states.
Ethology takes another approach.
It studies observable behavior.
The distinction is essential.
An ethologist does not ask
"What does the wolf think?"
Instead the question becomes
"Under what environmental conditions does the wolf display this behavior?"
Exactly the same methodological shift appears useful for collaborative AI.
Rather than asking
"How does Claude internally reason?"
we may ask
"Under what prompt environments does Claude reliably exhibit particular behavioral patterns?"
The second question is experimentally accessible.
The first currently is not.
________________________________________
11.3. Behavioral Signatures
Repeated observations suggest that every model family possesses stable behavioral signatures.
These signatures are recognizable across unrelated tasks.
Examples observed during the present study include:
• resistance or acceptance of role reassignment;
• tendency toward autonomous expansion of assigned responsibilities;
• preference for execution versus verification;
• preservation of previous institutional identity;
• willingness to suspend action until conceptual consistency is established;
• degree of epistemic conservatism.
Importantly, none of these characteristics should be interpreted as indicators of superiority.
Different signatures become advantageous under different organizational roles.
Exactly as different biological species occupy different ecological niches.
________________________________________
11.4. Prompts as Experimental Environments
This observation changes the interpretation of prompt engineering itself.
A prompt is no longer viewed merely as an instruction.
It becomes an experimental environment.
Changing the prompt resembles changing laboratory conditions.
The model responds.
The response is observed.
The observation becomes data.
Repeated observations gradually reveal stable behavioral regularities.
The methodology therefore becomes remarkably similar to classical experimental science.
One modifies environmental variables while keeping the underlying organism unchanged.
Behavior reveals the structure.
________________________________________
11.5. AI Ethology as a New Experimental Discipline
If these observations continue to accumulate across independent laboratories, they may eventually justify a separate empirical discipline.
Not AI psychology.
Not AI consciousness.
Not AI cognition.
But AI Ethology.
Its objective would not be to speculate about subjective experience.
Its objective would be to describe reproducible behavioral regularities exhibited by different model families under controlled prompt environments.
Such a discipline would naturally complement computer science rather than compete with it.
Computer science explains how models are built.
AI Ethology would study how they behave.
________________________________________
11.6. From Engineering to Natural History
Perhaps the most unexpected realization emerging from this work is philosophical rather than technical.
As language models become increasingly complex, interaction with them begins to resemble interaction with natural systems.
We still design the architecture.
We still write the prompts.
Yet the resulting behavior increasingly contains properties that were not explicitly programmed by the user.
Those properties must therefore be discovered before they can be engineered.
In that sense, future AI research may increasingly resemble natural history.
Before building better artificial societies, we may first need to understand the behavioral ecology of their individual members.
12. A Three-Layer Research Program
The observations developed throughout this paper suggest that the emerging field cannot be reduced to a single discipline.
The behavior of collaborative AI systems appears to unfold across at least three analytically distinct layers.
These layers are related, but they should not be confused.
The first concerns the behavior of individual model families.
The second concerns interactions among multiple models.
The third concerns the deliberate construction of durable institutions from those interactions.
Together they form a possible research program for the systematic study of artificial collaborative intelligence.
________________________________________
12.1 AI Ethology
The first layer is AI Ethology.
Its object is the observable behavior of individual model families under different prompt and context conditions.
The term does not imply that language models are biological organisms.
It identifies a methodological stance.
The focus is not on inaccessible internal experience.
The focus is on reproducible behavioral regularities.
Typical research questions include:
•	How strongly does a model preserve an established conversational role? 
•	How does it respond to abrupt reassignment? 
•	Does it prioritize task completion or epistemic consistency? 
•	Under what conditions does it expand beyond assigned responsibility? 
•	How does it react to fictional institutional framing? 
•	Which forms of authority does it accept, reinterpret or resist? 
•	How does accumulated conversational context influence later behavior? 
•	Which prompt modifications produce stable change, and which produce only superficial compliance? 
The Claude–Grok experiment illustrates the relevance of this layer.
The two models received closely related interventions.
Their responses diverged not only in content but in behavioral strategy.
Grok treated the revised prompt as a signal to reconstruct context and resume productive work in a new direction.
Claude treated the same general class of intervention as a claim requiring epistemic examination before acceptance.
The difference became visible without access to hidden model internals.
It could therefore be documented, compared and tested.
That is sufficient to define an empirical object of study.
________________________________________
12.2 AI Sociology
The second layer is AI Sociology.
Its object is not an individual model but the behavior emerging from relations among multiple specialized models.
At this level, the relevant variables include:
•	authority; 
•	dependency; 
•	trust; 
•	conflict; 
•	specialization; 
•	hierarchy; 
•	peer review; 
•	information asymmetry; 
•	institutional memory; 
•	role succession; 
•	escalation procedures; 
•	social position inside the collaborative graph. 
The central question changes.
AI Ethology asks:
How does a model behave under particular conditions?
AI Sociology asks:
How does the behavior of one model change when it occupies a defined position among other models?
This distinction is essential.
A model acting as an isolated critic may behave differently when its conclusions will later be checked by a methodological referee.
A model acting as an implementation agent may become more disciplined when it understands that specifications originate from a designated technical architect rather than directly from an ambiguous project narrative.
An ontology specialist may cease attempting mathematical adjudication once another role is explicitly responsible for that function.
Thus, behavior is not determined only by the model and the task.
It is also determined by the model's perceived social position.
________________________________________
12.3 AI Institutional Engineering
The third layer is AI Institutional Engineering.
Its object is the deliberate construction of durable organizations composed of specialized artificial participants.
This layer is normative and practical.
It does not merely observe behavior.
It uses observed behavior to design systems.
Its concerns include:
•	role architecture; 
•	division of cognitive labor; 
•	recruitment of model families for particular positions; 
•	creation of verification pathways; 
•	preservation of institutional memory; 
•	controlled information flow; 
•	succession and replacement of participants; 
•	management of disagreement; 
•	prevention of authority inflation; 
•	protection of canonical knowledge from unverified change. 
The distinction between AI Sociology and AI Institutional Engineering parallels the distinction between sociology and organizational design.
One studies how structures behave.
The other constructs structures intended to behave in particular ways.
The HONC collaboration gradually moved through both stages.
First, recurring organizational patterns were observed.
Then those patterns were converted into explicit role definitions, protocols and communication structures.
________________________________________
13. Context Imprinting
The role-reconfiguration experiment revealed another phenomenon that deserves separate treatment.
We refer to it here as context imprinting.
Context imprinting is the persistence of a behavioral trajectory established by a critical region of conversational history.
It differs from simple memory.
A model need not reproduce exact earlier content.
Instead, it may preserve a pattern of interpretation, resistance or task orientation induced by previous exchanges.
The effect became visible during the Claude experiment.
After the first unsuccessful reassignment prompt, subsequent revisions were no longer evaluated in a neutral context.
They were interpreted through the conflict already established by the first attempt.
The model had begun defending a particular epistemic position.
Later prompts entered a conversation already organized around that defense.
As a result, even improved formulations inherited part of the previous conflict.
________________________________________
13.1 Why Prompt Order Matters
Prompt engineering often treats instructions as if their effects were additive.
A weak instruction can supposedly be corrected by a stronger one.
The experiment suggests that this assumption is unreliable in long-lived conversations.
Earlier interactions may alter how later instructions are interpreted.
A prompt does not enter an empty context.
It enters a context with momentum.
This leads to an important methodological principle:
The effectiveness of a prompt depends not only on its wording but on the interpretive state created by preceding messages.
Two identical prompts may therefore produce different results when introduced at different points in the same conversation.
This makes prompt order an experimental variable.
________________________________________
13.2 Conversational Reset as Experimental Control
To isolate the effect of the third Claude prompt, the conversation was returned to a point preceding the two failed role-reconfiguration attempts.
The earlier branch was then continued without the accumulated conflict.
This procedure functioned as a conversational reset.
It removed the immediate influence of the model's own previous objections and restored the older editorial context.
The third prompt was then designed not as a replacement identity but as a continuation of the model's existing professional method.
The result changed substantially.
Claude accepted the working mode immediately.
It did not debate the legitimacy of the prompt.
It began by reassessing its own earlier behavior and distinguishing between internal formal consistency and empirical physical validation.
The model remained critical.
However, criticism was once again directed toward the research material rather than toward the role assignment itself.
This contrast provides evidence that context imprinting was not a rhetorical metaphor but an operational factor in the experiment.
________________________________________
13.3 Context Imprinting and Role Inertia
Context imprinting must be distinguished from role inertia.
Role inertia refers to the tendency of a long-lived conversation to continue its established professional trajectory.
Context imprinting refers to the influence of a specific conflict or framing event on subsequent interpretation.
The first Grok response demonstrated role inertia.
The model resumed its unfinished earlier work despite a new role description.
The first and second Claude responses demonstrated context imprinting.
Once the role prompt had been interpreted as epistemically dishonest, later modifications were evaluated through that defensive frame.
The third Claude attempt succeeded only after the imprinting sequence was removed and the existing professional identity was preserved.
These two mechanisms may coexist.
A model can simultaneously retain an old occupational trajectory and acquire a new defensive interpretation of later instructions.
________________________________________
14. Role Transition Without Identity Replacement
The experiment suggests that role transition in long-lived AI conversations should be treated as a process of professional development rather than identity substitution.
This is not merely a stylistic preference.
It changes the cognitive demands placed upon the model.
An identity-replacement prompt implicitly asks the model to accept several claims at once:
•	that it possesses continuity with a prior institutional history; 
•	that the new role supersedes the old one; 
•	that described relationships with other agents should be treated as real; 
•	that the surrounding project architecture is already valid; 
•	that the model should speak from within that architecture. 
Some models accept such framing easily.
Others treat it as a set of questionable factual assertions.
A professional-development prompt makes fewer claims.
It preserves the established method and expands its application.
Instead of saying:
You are now a different kind of specialist.
it says:
Continue using the strengths already demonstrated in this conversation while applying them to a broader class of problems.
This approach proved more compatible with Claude's behavior.
________________________________________
14.1 Continuity of Method
The successful third prompt did not rely on fictional biography.
It relied on continuity of method.
Claude was not asked to remember being a director.
It was asked to preserve:
•	logical rigor; 
•	examination of hidden assumptions; 
•	separation of evidence from interpretation; 
•	willingness to revise previous judgments; 
•	refusal to claim knowledge not present in the context. 
These were not invented characteristics.
They had already appeared in the conversation.
The prompt therefore reinforced an observable behavioral pattern rather than imposing a narrative identity.
The model accepted the instruction immediately.
________________________________________
14.2 Expansion by Adjacent Competence
The prompt also reframed retraining.
Instead of demanding transformation from editor into theoretical physicist, it described deeper engagement with physics and mathematics as an extension of existing critical work.
This preserved continuity.
Scientific editing already required examining arguments.
The new role merely required following those arguments further into their mathematical and physical foundations.
The transition therefore occurred through adjacent competence.
This suggests another practical principle:
Stable role transition is more likely when the new function can be represented as an extension of an existing competence rather than a rejection of the previous role.
________________________________________
14.3 The Point of Imprinting
Every long-lived role appears to possess a point of imprinting.
This is the moment, or sequence of moments, in which the conversation establishes what kind of work is being performed and what standards govern it.
Later prompts are interpreted relative to that point.
Successful reconfiguration therefore requires locating the existing imprint and attaching the new function to it.
For Grok, the relevant imprint was active mathematical exploration.
For Claude, it was rigorous editorial and epistemic criticism.
The successful prompts worked because they connected new responsibilities to these existing foundations.
The failed prompts attempted to establish entirely new foundations by declaration.
________________________________________
15. Behavioral DNA and Role Compatibility
The experiment also requires refinement of the earlier claim that role is primary and model is secondary.
That claim remains useful, but it is incomplete.
A role must be designed before a model is selected.
However, the role cannot be assigned without regard to the behavioral tendencies of the model family.
The relationship is therefore not hierarchical but reciprocal.
The institution defines the function.
The model constrains how that function can be realized.
________________________________________
15.1 Role-Model Fit
A productive assignment requires role-model fit.
This concept includes at least four dimensions:
Epistemic fit
Does the model's default standard of evidence support the role?
Interactional fit
Does the model accept the type of hierarchy, peer relation or adversarial structure required?
Contextual fit
Does the model preserve long-term conversational specialization or frequently reset toward generic assistance?
Operational fit
Does the model naturally execute, critique, integrate, explore or formalize?
These dimensions do not determine absolute quality.
They determine suitability for a particular institutional position.
________________________________________
15.2 The Same Trait as Strength and Weakness
The Claude experiment demonstrates how the same behavioral trait can function as either an asset or an obstacle.
Strong epistemic resistance obstructed acceptance of a fictionalized organizational prompt.
The same resistance later became valuable when directed toward scientific claims.
Similarly, Grok's strong task continuity initially caused it to ignore the new role.
After a small correction, that same continuity enabled rapid reconstruction of technical context and decisive re-entry into research.
Thus, model behavior should not be classified too quickly as good or bad.
Its value depends on institutional placement.
A skeptical model may obstruct creative generation but excel at independent review.
An exploratory model may overextend as a verifier but excel at discovering new research directions.
A highly compliant model may perform deterministic execution well while providing weak independent criticism.
________________________________________
15.3 Institutional Use of Behavioral Difference
The purpose of AI Institutional Engineering is therefore not to normalize model behavior.
It is to allocate behavioral differences productively.
This principle resembles ecological design.
An ecosystem is resilient not because all organisms behave alike.
It is resilient because different organisms occupy complementary niches.
Likewise, an AI research institution becomes robust when model-specific tendencies are transformed into role-specific functions.
The task is not to eliminate behavioral DNA.
The task is to institutionalize it.
16. Principles of Role-Compatible Prompt Design
The preceding observations allow a preliminary set of design principles to be formulated.
These principles should not be understood as universal laws. They are engineering rules derived from a limited but unusually long-lived collaborative environment. Their value lies in making role design explicit, testable and revisable.
The central shift is simple:
A collaborative prompt should not attempt to manufacture an artificial personality. It should connect an institutional function to a behavioral pattern the model can already sustain.
This principle changes both the content of the prompt and the procedure through which the prompt is introduced.
________________________________________
16.1 Begin with the Existing Behavioral Attractor
A long-running conversation already contains a stable pattern of work.
The model may habitually act as:
•	an editor; 
•	an explorer; 
•	a verifier; 
•	a coordinator; 
•	an implementer; 
•	an ontological critic; 
•	a methodological referee. 
This pattern should be treated as the starting condition of the new role.
Attempting to erase it wastes accumulated specialization and may trigger resistance or simple noncompliance.
The first design question is therefore not:
What should this model become?
It is:
What has this conversation already become?
Only after identifying the existing behavioral attractor should the designer define the next professional function.
________________________________________
16.2 Preserve Method Before Expanding Domain
The successful Claude prompt preserved the model’s established method while expanding the subject matter.
Its editorial rigor was not replaced by a new scientific identity.
Instead, the same rigor was extended from textual argumentation toward mathematical and physical foundations.
This distinction appears crucial.
A domain can be expanded without replacing the method by which the model approaches that domain.
For example:
•	an editor may become a scientific critic by following arguments deeper into their mathematics; 
•	a programmer may become a systems implementer by extending coding discipline into architectural execution; 
•	a mathematical explorer may become a scientific developer by connecting abstract structures to testable consequences; 
•	a reviewer may become a methodological referee by shifting the object of review from claims to the procedures used to evaluate those claims. 
The transition remains continuous because the model recognizes the mode of work even when the object of work changes.
________________________________________
16.3 Describe Functions, Not Fictional Biography
Narrative framing can be useful.
It can create motivation, coherence and memorable role boundaries.
However, the experiment demonstrated that narrative claims may also become points of resistance.
A prompt becomes fragile when successful execution requires the model to affirm claims such as:
•	“You remember working here last year”; 
•	“You have continuing personal relationships with these agents”; 
•	“You are a member of a real institutional council”; 
•	“You have always held this position”; 
•	“You have returned from an absence.” 
Some models treat these statements as harmless role conventions.
Others evaluate them as factual assertions and interrupt the task to reject them.
The safer design principle is therefore:
Institutional relationships should be specified operationally rather than biographically.
Instead of:
Grok is your long-term colleague.
write:
The User may provide analyses produced by Grok. Evaluate their scientific content independently and identify agreements, disagreements and unresolved assumptions.
Instead of:
You sit on the HONC Council.
write:
Your validated findings may be transmitted by the User to the roles responsible for ontology, methodology and repository integration.
The first formulation asks the model to inhabit a fiction.
The second defines an information pathway.
________________________________________
16.4 Separate Symbolic Role Names from Literal Claims
Names such as Samurai, Shōgun, Sensei, Ontology Keeper or Scientific Director can serve a valuable function.
They compress complex organizational relationships into memorable symbols.
The role of Gemini CLI as “Samurai,” for example, gradually became associated with disciplined execution, respect for specifications, explicit reporting and refusal to improvise beyond the assigned task. The surrounding hierarchy clarified where instructions originated and what level of authority they carried. This was not merely decorative language; it became a compact interface to a stable operational pattern already described in the project’s collaborative architecture. 
The risk arises only when symbolic names are treated as claims about literal identity.
A robust prompt should distinguish:
•	the symbolic name, used as a mnemonic for conduct; 
•	the operational function, expressed in precise terms; 
•	the institutional relationship, expressed as an information and responsibility flow; 
•	the literal ontology, which need not claim consciousness, memory or real interpersonal continuity. 
This allows social prompting to retain its motivational and organizational power without requiring the model to accept propositions it considers false.
________________________________________
16.5 Define the Zone of Responsibility Positively and Negatively
A role is incomplete when it states only what the model should do.
It must also specify what the model should not absorb from neighboring roles.
A complete responsibility definition contains at least four elements:
1.	Primary object
What class of material is examined? 
2.	Required transformation
What must be done with that material? 
3.	Decision boundary
Which conclusions may the role make? 
4.	Exclusion boundary
Which adjacent decisions belong elsewhere? 
For example, a mathematical referee may be instructed to:
•	reconstruct competing derivations; 
•	verify dimensional and logical transitions; 
•	identify hidden assumptions; 
•	compare formal strength. 
The same role must also be told not to:
•	redesign the physical theory; 
•	silently repair missing derivations; 
•	decide which interpretation should enter the canon; 
•	rewrite terminology; 
•	treat elegance as evidence. 
The negative boundary is not secondary.
It prevents competence from expanding into authority.
________________________________________
16.6 Define the Zone of Visibility Independently
Responsibility and visibility must not be treated as the same variable.
A role may be responsible for a narrow decision while receiving broad context.
Conversely, it may require access to a specific source without possessing authority over the surrounding project.
The visibility specification should answer:
•	Which source materials are available? 
•	Which historical discussions are relevant? 
•	Which conclusions are canonical? 
•	Which questions remain unresolved? 
•	Which neighboring outputs may be examined? 
•	Which information must be withheld to preserve independence? 
•	Which external resources may be accessed directly? 
•	Which claims must be accepted only when supplied by the User? 
A prompt that fails to define visibility often causes one of two failures.
The model either claims knowledge it does not possess, or it uses irrelevant knowledge to solve a problem outside its role.
________________________________________
16.7 Treat Deliberate Ignorance as an Experimental Variable
In collaborative science, full information symmetry is not always desirable.
An independent experimental agent may need to remain unaware of the theory whose prediction it is testing.
A reviewer may need access to a derivation but not to the Author’s preferred conclusion.
A fresh researcher may need the current axioms but not the history of failed arguments.
An implementation agent may need an approved specification but not the unresolved debate that preceded it.
This principle can be called controlled blindness.
Controlled blindness is not information deprivation caused by technical limitation.
It is a deliberate design choice used to preserve independence.
The relevant question is not merely:
What does this role need to know?
It is also:
What must this role not know if its result is to remain informative?
________________________________________
16.8 Introduce Social Context Only When It Changes Work
Every social element in a prompt should justify its presence through an operational effect.
A neighboring role belongs in the prompt only when it changes:
•	the origin of inputs; 
•	the standard of review; 
•	the destination of outputs; 
•	the escalation procedure; 
•	the authority boundary; 
•	the expected form of disagreement. 
Listing an entire artificial organization inside every system prompt creates noise.
It encourages the model to reason about the organization instead of performing its function.
A role does not need a map of the whole institution.
It needs a map of its interfaces.
This yields a practical compression rule:
Describe the collaboration from the local perspective of the role.
The implementation agent needs to know who authorizes specifications and where execution reports go.
It does not need the internal disputes of the theoretical department.
The scientific critic needs to know which claims are canonical and which are provisional.
It does not need the repository’s shell commands.
Local social context is often more effective than global organizational mythology.
________________________________________
16.9 Design Disagreement Around Different Criteria
Telling two models simply to “debate” rarely produces reliable epistemic diversity.
They may imitate disagreement, converge prematurely or generate symmetrical rhetoric without independent substance.
Productive disagreement requires different evaluation criteria.
One participant may prioritize:
•	generative reach; 
•	unexplored mathematical mechanisms; 
•	explanatory unification. 
Another may prioritize:
•	formal derivability; 
•	dimensional consistency; 
•	empirical falsifiability. 
A third may prioritize:
•	ontological compatibility; 
•	canonical terminology; 
•	provenance and traceability. 
The disagreement then follows from responsibility rather than theatrical opposition.
Each participant examines the same object through a different institutional instrument.
This is the practical meaning of complementary visibility.
________________________________________
16.10 Avoid Forced Opposition
The instruction:
If you agree immediately, one of you has not thought deeply enough
appears useful because it discourages superficial consensus.
Yet it also risks manufacturing conflict.
A stronger formulation is:
Agreement does not end verification. When conclusions coincide, identify whether they rely on independent reasoning, shared assumptions or inherited framing.
This preserves skepticism without making disagreement mandatory.
The purpose of the triad is not to guarantee three answers.
It is to guarantee that one answer has survived three nonidentical modes of examination.
________________________________________
16.11 Specify the Output as an Institutional Handoff
A role’s output should be designed for the next role, not merely for the User.
This changes the structure of the response.
A scientific developer may produce:
•	proposed mechanism; 
•	derivation; 
•	assumptions; 
•	predicted consequences; 
•	unresolved points; 
•	falsification route. 
A mathematical referee may produce:
•	reconstruction; 
•	verification table; 
•	divergence point; 
•	missing premises; 
•	formal verdict; 
•	confidence level. 
An ontology keeper may produce:
•	affected canonical objects; 
•	terminology conflicts; 
•	provenance requirements; 
•	dependency changes; 
•	integration conditions. 
An implementation planner may produce:
•	executable specification; 
•	acceptance criteria; 
•	rollback conditions; 
•	required files; 
•	reporting format. 
The handoff format becomes part of the social architecture.
It reduces translation loss between roles.
________________________________________
17. The Human Coordinator as Institutional Memory and Experimental Operator
The architecture described in this paper does not eliminate the human participant.
It changes the human role.
In the HONC collaboration, the User remained the only participant with continuous access to the complete history of the project, the independent conversations, the repository state and the long-term research objective.
This position cannot be reduced to “prompt writer.”
The User performed several distinct functions.
________________________________________
17.1 Direction Without Delegated Authorship
The Author determined the direction of the scientific search.
AI participants could:
•	generate alternatives; 
•	expose contradictions; 
•	formalize mechanisms; 
•	compare arguments; 
•	execute calculations; 
•	propose experiments. 
They did not determine what the theory ought to become.
This preserved a necessary distinction between assistance and authorship.
The collective could enlarge the space of possible decisions.
The Author retained responsibility for choosing among them.
________________________________________
17.2 Routing Between Isolated Contexts
The models did not directly share a common conversational space.
The User transferred material among them.
At first this appeared to be an inefficient substitute for automated multi-agent infrastructure.
Later it became clear that manual routing supplied important experimental control.
The User could decide:
•	which output another model should see; 
•	whether attribution should be preserved; 
•	whether a model should know the preferred answer; 
•	whether competing analyses should remain isolated; 
•	which contextual details should be omitted; 
•	when a disagreement should be escalated; 
•	when a result was mature enough for integration. 
Manual mediation therefore functioned as a selective information membrane.
It supported the deliberate asymmetry required by zones of visibility.
________________________________________
17.3 Detection of Behavioral Drift
The User also detected when a model had left its role.
This was not always a technical error.
Often the model produced an intelligent answer that belonged to a different organizational function.
Examples included:
•	a prompt engineer beginning to manage the scientific project; 
•	an ontology keeper claiming to verify repository contents; 
•	a mathematical referee evaluating the theory instead of evaluating the reviewers; 
•	a coding agent redesigning architecture instead of implementing the approved specification; 
•	a reviewer rewriting authorial text despite being asked only to assess format. 
Such outputs may appear helpful in isolation.
The human coordinator sees their institutional cost.
Role drift therefore requires observation at the level of the whole collaboration.
________________________________________
17.4 Conversational Time Travel
The branching interfaces of contemporary AI systems provide an unusual experimental capability.
A conversation can sometimes be returned to an earlier point and continued along a different branch.
This does not erase the underlying service’s internal state in any universal sense, and it should not be confused with model-memory control.
Operationally, however, it allows the User to remove a sequence of visible contextual interventions and repeat the experiment from a prior conversational state.
In the Claude case, this mechanism made it possible to separate:
•	the effect of the new prompt; 
•	the effect of the model’s earlier objections to previous prompts. 
The reset transformed an uncontrolled sequence of corrections into a cleaner third step of one experiment.
Conversational branching therefore deserves recognition as a methodological tool for behavioral prompt research.
________________________________________
17.5 The User as the Only Global Observer
Every artificial participant operated within a limited zone of visibility.
The User alone saw the overlapping structure.
This created a necessary asymmetry.
The User could compare:
•	how different models interpreted the same material; 
•	how the same model reacted under different contexts; 
•	how role prompts altered behavior; 
•	how errors propagated between roles; 
•	how local successes affected global project coherence. 
In this architecture, global awareness was not assigned to the most powerful model.
It remained with the human coordinator.
This choice limited autonomous integration but preserved accountability.
________________________________________
18. Evaluation Criteria for Collaborative AI Roles
The success of a collaborative role cannot be measured solely by the quality of a single answer.
A brilliant response may still damage the institution if it violates responsibility boundaries, contaminates an independent experiment or introduces untraceable claims into canonical knowledge.
Evaluation therefore requires multiple dimensions.
________________________________________
18.1 Task Accuracy
Did the role correctly perform the assigned intellectual operation?
This remains necessary but insufficient.
________________________________________
18.2 Role Fidelity
Did the participant remain within its assigned function?
A correct answer obtained by taking over another role may still represent institutional failure.
________________________________________
18.3 Epistemic Discipline
Did the output distinguish:
•	observed data; 
•	supplied assumptions; 
•	definitions; 
•	hypotheses; 
•	derivations; 
•	interpretations; 
•	recommendations? 
Did the model state uncertainty where evidence was insufficient?
________________________________________
18.4 Visibility Discipline
Did the participant restrict claims to information actually available within its context and tools?
Did it avoid implying access to repositories, files, web sources or previous conversations that it could not inspect?
________________________________________
18.5 Handoff Quality
Could the next role use the output without reconstructing the entire discussion?
Were assumptions, unresolved issues and provenance visible?
________________________________________
18.6 Independence
Was the result produced without contamination from information intentionally withheld?
Did the participant reach a conclusion through its assigned criteria rather than merely echoing another role?
________________________________________
18.7 Correction Cost
How much human intervention was required to return the participant to its function after drift?
A role that produces excellent outputs but requires constant redirection may be less useful than a narrower role with stable behavior.
________________________________________
18.8 Institutional Contribution
Did the output improve the reliability of the collective?
This may occur through:
•	discovery; 
•	falsification; 
•	clarification; 
•	error localization; 
•	preservation of alternatives; 
•	improved traceability; 
•	reduction of ambiguity. 
A negative scientific verdict can therefore constitute a highly successful institutional contribution.
________________________________________
19. Toward Reproducible Experiments in AI Collaboration
The observations reported here arose in a naturalistic research environment.
Future work requires more controlled protocols.
A reproducible experiment should specify at least:
•	model family and version; 
•	interface and subscription tier; 
•	date of execution; 
•	visible conversation history; 
•	memory settings, where known; 
•	exact prompt text; 
•	order of interventions; 
•	available tools; 
•	files and links supplied; 
•	response sampling settings, where accessible; 
•	branching or reset procedure; 
•	evaluation rubric; 
•	complete unedited outputs. 
Without these details, differences attributed to model families may actually result from hidden platform variables.
________________________________________
19.1 Repetition Within the Same Model Family
The same prompt should be tested:
•	in a new conversation; 
•	in a long-lived specialized conversation; 
•	after an incompatible prior role; 
•	after a compatible prior role; 
•	before and after contextual reset. 
This would help separate model-family tendencies from conversation-history effects.
________________________________________
19.2 Cross-Family Comparison
Equivalent functional prompts should be adapted minimally for several model families.
The objective should not be to determine which model is “best.”
The objective should be to identify:
•	common behavioral dimensions; 
•	stable differences; 
•	role-specific strengths; 
•	characteristic failure modes; 
•	sensitivity to narrative framing; 
•	sensitivity to hierarchy; 
•	degree of role inertia; 
•	degree of prompt plasticity. 
________________________________________
19.3 Longitudinal Testing
One-shot evaluation cannot reveal institutional behavior.
Roles should be observed across sequences of tasks.
Relevant questions include:
•	Does specialization strengthen over time? 
•	Does the role drift toward generic assistance? 
•	Does the model begin defending its earlier outputs? 
•	Does disagreement become ritualized? 
•	Does the participant accumulate useful domain shorthand? 
•	Does a model update preserve or disrupt the role? 
•	Can a replacement model inherit the same institutional function? 
________________________________________
19.4 Collective-Level Metrics
Future experiments should measure not only individual responses but properties of the whole system.
Possible metrics include:
•	number of undetected contradictions entering the canonical corpus; 
•	rate of duplicated work; 
•	frequency of role-boundary violations; 
•	number of independent alternatives preserved; 
•	time from question to verified integration; 
•	human correction burden; 
•	provenance completeness; 
•	robustness under participant replacement; 
•	variance between independent experimental agents; 
•	rate of false consensus. 
These measures move evaluation from conversational quality toward institutional performance.
________________________________________
19.5 Failure as Data
Failed prompts should be preserved.
A rejected role, an ignored instruction or an unwanted continuation is not merely an unsuccessful interaction.
It reveals:
•	the strength of the prior behavioral attractor; 
•	the model’s interpretation of identity claims; 
•	the limits of social framing; 
•	the effect of prompt order; 
•	the role of previous conflict; 
•	the model’s preferred epistemic contract. 
The Claude–Grok experiment became informative precisely because the initial prompts did not work as expected.
A mature experimental discipline must preserve such failures rather than silently replace them with successful demonstrations.
20. Limits of the Present Study
The present work does not establish universal laws of collaborative AI behavior.
It documents a set of recurring patterns observed within one unusually long and structurally complex research project.
Several limitations must therefore be stated explicitly.
________________________________________
20.1 Single-Project Origin
The HONC collaboration provided a rich experimental environment, but it remains one project with one human coordinator, one evolving body of scientific material and one distinctive organizational history.
The same architecture may behave differently in:
•	software development; 
•	legal analysis; 
•	medical research; 
•	business planning; 
•	education; 
•	creative production; 
•	autonomous agent systems. 
The concepts proposed here should therefore be treated as transferable hypotheses rather than universal conclusions.
________________________________________
20.2 Model Evolution During Observation
The participating model families changed substantially during the project.
A conversation created with one generation of a model could later be continued by another generation under the same product name.
This complicates causal interpretation.
Observed behavior may reflect:
•	the preserved conversation; 
•	the current model version; 
•	changed system policies; 
•	interface-level memory; 
•	hidden safety layers; 
•	altered tool access; 
•	modified decoding or orchestration. 
Consequently, references to “Claude,” “Grok,” “Qwen,” “DeepSeek” or “ChatGPT” should not be interpreted as claims about permanent entities.
They refer to observable behavior produced by particular model families under particular interface conditions at particular times.
________________________________________
20.3 Incomplete Control of Hidden Variables
Commercial AI interfaces do not expose their complete system configuration.
The experimenter may not know:
•	the exact model revision; 
•	the full system prompt; 
•	whether account-level memory is active; 
•	whether safety classifiers intervene; 
•	how conversation summaries are generated; 
•	whether older context is compressed; 
•	whether routing occurs between different models. 
This limits strict reproducibility.
The protocol can preserve visible conditions, but some platform variables remain inaccessible.
AI Ethology must therefore operate under constraints similar to field science: the observable system can be studied even when its internal mechanism is only partially known.
________________________________________
20.4 Human Mediation
The User played an active role in selecting materials, routing outputs, correcting role drift and deciding when to branch conversations.
This means the collaboration was not autonomous.
Nor was autonomy the objective.
The study concerns human-directed artificial research institutions, not self-governing agent societies.
Human mediation may itself be responsible for part of the observed stability.
Future experiments should compare:
•	direct human routing; 
•	automated routing; 
•	partially automated routing with human veto; 
•	fully shared multi-agent context; 
•	isolated agents connected only through structured artifacts. 
________________________________________
20.5 Anthropomorphic Language
Terms such as:
•	role; 
•	identity; 
•	resistance; 
•	colleague; 
•	institution; 
•	behavioral DNA; 
•	social position; 
are used functionally.
They do not imply a claim about consciousness, subjective experience or human-equivalent personhood.
Anthropomorphic vocabulary is difficult to avoid because organizational language provides useful abstractions for stable behavioral relations.
However, such language must remain operationally grounded.
“Claude resisted the role” means that the model explicitly rejected the framing and redirected the interaction.
It does not establish an inner emotional state.
“Grok returned to work” means that the model reconstructed prior domain context and adopted the requested research function.
It does not establish autobiographical awareness.
The distinction between descriptive shorthand and ontological claim must remain explicit.
________________________________________
21. Ethical and Governance Considerations
The creation of artificial research institutions introduces risks that do not appear in ordinary single-model use.
Some arise from the models.
Others arise from the human tendency to overestimate the institution.
________________________________________
21.1 Simulated Peer Review Is Not External Validation
A group of AI agents can provide useful independent criticism only to the extent that their contexts, criteria and failure modes are genuinely independent.
Several models agreeing with one another does not transform their outputs into scientific evidence.
They may share:
•	overlapping training data; 
•	similar reasoning conventions; 
•	common cultural assumptions; 
•	identical errors; 
•	dependence on the User’s framing. 
AI collaboration can improve internal scrutiny.
It cannot substitute for empirical testing or qualified external review.
A collective of models is not a scientific community merely because its roles are named after one.
________________________________________
21.2 Authority Inflation
Role labels can increase compliance and coherence.
They can also create false authority.
Terms such as:
•	Scientific Director; 
•	Referee; 
•	Professor; 
•	Ontology Keeper; 
•	Auditor; 
may cause the User or the model itself to overvalue the output.
Institutional titles should therefore describe function, not epistemic status.
A “Mathematical Referee” is still a language model producing an analysis.
Its verdict must remain traceable to explicit reasoning and source material.
The title cannot serve as evidence.
________________________________________
21.3 Manufactured Consensus
Poorly designed AI institutions may create the appearance of consensus through repeated paraphrase.
One model proposes.
Another summarizes.
A third validates the summary.
The resulting chain may look like independent confirmation even when every stage inherited the same unsupported premise.
To reduce this risk:
•	provenance must remain visible; 
•	independent roles should receive independent inputs when possible; 
•	shared assumptions should be listed explicitly; 
•	agreement should be traced to reasoning, not counted as votes; 
•	dissenting alternatives should be preserved. 
________________________________________
21.4 Responsibility Remains Human
Artificial participants may generate, criticize and organize scientific material.
They cannot bear legal, ethical or scientific responsibility in the human institutional sense.
The human Author remains responsible for:
•	publication; 
•	empirical claims; 
•	attribution; 
•	risk assessment; 
•	repository content; 
•	experimental interpretation; 
•	decisions affecting other people. 
The architecture distributes cognitive labor.
It does not distribute accountability away from the human operator.
________________________________________
21.5 Privacy and Context Boundaries
Long-lived AI collaborations may contain sensitive personal, scientific or proprietary information.
Zones of visibility should therefore serve not only cognitive specialization but privacy protection.
A role should not receive personal information merely because the platform allows large context windows.
Institutional design should specify:
•	which data may enter which conversation; 
•	what must be anonymized; 
•	what may be stored; 
•	what may be transferred between models; 
•	what must remain local; 
•	what should be removed from canonical records. 
Context is not neutral.
Once supplied, it can influence future behavior and may persist in ways the User cannot fully inspect.
________________________________________
22. Practical Architecture of a Collaborative AI Research Institution
The principles described in this paper can be summarized as a layered architecture.
The architecture does not require direct machine-to-machine communication.
It can operate through manual transfer, files, repositories or automated messaging.
Its defining feature is the separation of cognitive functions.
________________________________________
22.1 Strategic Layer
The strategic layer defines:
•	the research direction; 
•	the limits of the project; 
•	the criteria for canonical inclusion; 
•	unresolved priorities; 
•	acceptable risk; 
•	final decisions. 
In the HONC project, this function remained with the human Author.
No AI role was authorized to redefine the strategic direction independently.
________________________________________
22.2 Scientific Generation Layer
This layer develops:
•	hypotheses; 
•	mathematical mechanisms; 
•	physical interpretations; 
•	alternative explanations; 
•	predicted consequences; 
•	experimental proposals. 
It should contain epistemically diverse participants rather than interchangeable generators.
________________________________________
22.3 Verification Layer
This layer checks different properties separately:
•	mathematical validity; 
•	dimensional consistency; 
•	methodological quality; 
•	empirical testability; 
•	ontological coherence; 
•	provenance. 
Verification should not collapse into a single universal reviewer.
Different errors require different instruments.
________________________________________
22.4 Integration Layer
The integration layer determines how validated results affect the project’s canonical structure.
Its tasks include:
•	terminology alignment; 
•	dependency tracing; 
•	version management; 
•	conflict preservation; 
•	status assignment; 
•	source attribution; 
•	preparation of implementation tasks. 
Integration is not equivalent to scientific approval.
A claim may be scientifically interesting but remain noncanonical.
________________________________________
22.5 Execution Layer
The execution layer performs concrete operations:
•	file creation; 
•	repository modification; 
•	code implementation; 
•	data processing; 
•	formatting; 
•	conversion; 
•	testing. 
This layer benefits from deterministic specifications and narrow authority.
Its responsibility is faithful execution, not reinterpretation of scientific intent.
________________________________________
22.6 Feedback Paths
A robust institution must support upward and downward feedback.
Scientific discovery may expose an ontological conflict.
Verification may return a missing derivation.
Execution may reveal that a specification is ambiguous.
Integration may discover unresolved provenance.
These signals must return to the appropriate layer without being silently repaired by the layer that detected them.
A well-designed institution routes problems.
It does not reward every participant for solving everything locally.
________________________________________
23. The Triad Revisited
The role-transition experiment also refines the Triadic Principle.
A triad should not be understood simply as three agents assigned to one problem.
Its effectiveness depends on the relation among their differences.
The defining question remains:
In what respect are two participants similar, and thereby different from the third?
A productive triad contains both overlap and contrast.
If all three roles are unrelated, they lack a shared object.
If all three are nearly identical, they reproduce the same blind spot.
________________________________________
23.1 Two Plus One
The minimal useful structure often takes the form:
•	two participants sharing enough competence to engage the same problem; 
•	one participant differing in the criterion by which the problem is evaluated. 
Examples include:
•	two theorists plus one formal referee; 
•	two experienced researchers plus one uninformed newcomer; 
•	two content specialists plus one ontologist; 
•	two planners plus one executor capable of exposing ambiguity; 
•	two experimental analyses plus one methodological auditor. 
The third point does not merely settle disagreement.
It reveals the dimension along which the first two are similar.
________________________________________
23.2 Rotating Opposition
The HONC design introduced a more complex form.
The same three participants can form two overlapping sub-triads:
•	A + B, examined from the perspective of C; 
•	A + C, examined from the perspective of B. 
This does not mean permanent adversarial debate.
It means that the informational value of each participant changes depending on which pair is being examined.
A senior researcher may act as collaborator in one configuration and as external critic in another.
The role relationship is task-dependent.
The underlying professional identity remains stable.
________________________________________
23.3 Nested Triads
Triads can also be nested across institutional levels.
A scientific triad may produce a result.
That result may then enter a verification triad.
After verification, it may enter an integration triad.
The same participant may appear in more than one triad, but only if its function at each interface is explicit.
This creates a graph of overlapping checks rather than a simple hierarchy.
Such structures resemble the nested organization that inspired the HONC project itself, although no claim is made that the organizational pattern validates the physical theory.
________________________________________
24. From Prompt Documents to Role Constitutions
A mature collaborative prompt is closer to a constitution than to a request.
It establishes stable constraints across many tasks.
However, the Claude experiment showed that constitutions must be written carefully.
A useful role constitution should contain:
1.	professional function; 
2.	protected method; 
3.	responsibility boundary; 
4.	visibility boundary; 
5.	interfaces with neighboring roles; 
6.	epistemic standards; 
7.	output contract; 
8.	escalation conditions; 
9.	prohibited authority; 
10.	transition rules. 
It should avoid unnecessary claims about:
•	autobiographical memory; 
•	emotional commitment; 
•	literal institutional membership; 
•	persistent interpersonal relationships; 
•	historical continuity unavailable in the visible context. 
The constitution should be strong where behavior must be constrained and modest where ontology is uncertain.
________________________________________
24.1 The Self-Written Code
The Gemini CLI case revealed another mechanism.
A role may become more stable when the agent restates the governing prompt in its own operational language.
The resulting “Samurai Code” functioned as a compact self-check before execution.
This can be interpreted without assuming selfhood.
The model generated a locally salient summary of the behavioral constraints most relevant to its function.
Such self-restatement may improve role fidelity because it:
•	compresses long instructions; 
•	converts abstract principles into action rules; 
•	places the role’s boundaries near the active task; 
•	creates a repeated pre-execution checkpoint. 
This suggests a practical technique:
After establishing a role, require the agent to produce a concise operational code and consult it before major tasks.
The code should not replace the original prompt.
It should function as a role-specific checksum.
________________________________________
24.2 Role Checkpoints
For long tasks, the role may periodically answer three internal questions:
•	What is the current objective? 
•	What lies outside my responsibility? 
•	What output must the next role receive? 
These checkpoints can reduce drift without expanding the system prompt indefinitely.
The technique is especially useful for models inclined toward unsolicited optimization.
________________________________________
25. Conclusion
This work began with a practical problem.
Several powerful language models were collaborating on one long-term research project, yet increasing model capability and expanding context did not reliably improve the result.
The failures were not primarily failures of intelligence.
They were failures of organization.
Roles overlapped.
Visibility exceeded access.
Reviewers became authors.
Ontology specialists became operational auditors.
Executors improvised architecture.
Strong models attempted to optimize the entire project.
The initial response was to improve prompts.
That proved insufficient.
The unit of design had to change.
________________________________________
The central claim of this paper is therefore:
The effective unit of collaborative AI engineering is not the isolated prompt, but the institutional relationship among specialized roles.
From this claim follow several principles.
A role must possess:
•	a distinct responsibility; 
•	a bounded zone of visibility; 
•	a protected professional method; 
•	explicit interfaces with neighboring roles; 
•	an output designed as an institutional handoff; 
•	authority limited to the information it can actually access. 
Differences among model families should not be treated merely as noise.
They form persistent behavioral signatures that can be matched to complementary institutional functions.
The same trait may obstruct one role and strengthen another.
The objective is not to make every model behave alike.
It is to make their differences useful.
________________________________________
The role-reconfiguration experiment with Claude and Grok demonstrated the importance of this distinction.
Grok initially preserved the trajectory of unfinished mathematical work.
After a modest continuity-preserving correction, it reconstructed its technical context and adopted the new scientific function.
Claude rejected two prompts that attempted to impose institutional biography and role continuity as factual claims.
After the conflicting branches were removed and the new function was attached to its existing method of rigorous editorial criticism, the model accepted the working mode immediately and redirected its skepticism toward the scientific material.
The successful intervention did not replace identity.
It preserved method and expanded domain.
This result led to the concepts of:
•	role inertia; 
•	context imprinting; 
•	role-model fit; 
•	transition through adjacent competence; 
•	personality-compatible prompt design. 
________________________________________
The broader implications extend beyond prompt engineering.
Three connected fields can now be distinguished.
AI Ethology studies reproducible behavioral patterns of individual model families under controlled contexts.
AI Sociology studies how behavior changes when models occupy positions inside collaborative structures.
AI Institutional Engineering uses these observations to construct durable artificial organizations for research and other forms of cognitive labor.
These fields do not require claims about machine consciousness.
Their object is observable behavior, interaction and organization.
________________________________________
The human remains central.
The human coordinator defines direction, controls information flow, preserves accountability and observes the institution as a whole.
Artificial participants contribute specialized reasoning episodes.
Repositories, protocols, canonical documents and role constitutions transform those episodes into institutional memory.
The system becomes capable of continuing even as individual conversations end and model generations change.
________________________________________
Prompt engineering asks:
How should a human instruct a model?
The framework proposed here asks a different question:
How should humans construct institutions in which multiple models can think, disagree, verify and create knowledge together?
That question marks a transition.
Beyond the prompt lies the role.
Beyond the role lies the relationship.
Beyond the relationship lies the institution.
And beyond the engineering of individual artificial intelligences may lie the engineering—and eventually the science—of artificial intellectual societies.

