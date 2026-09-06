# REVISIONS — накопительный файл

**Назначение.** Заменяющие блоки к каноническому тексту (Blocks 1–5). Каждая запись указывает, что именно замещается. Файл пополняется; сохранять в конце целиком.

**Статус на текущую запись:** внесена правка §4 (пункты 15, 16, 18 плана; частично 17).

---

# ЗАПИСЬ 1 — Section 4, полная замена

**Заменяет:** §4.1–§4.6 в BLOCK 2 целиком, от заголовка «# 4. Conceptual Framework» до строки, предшествующей «# 5. The Role-Reconfiguration Experiment».

**Что изменилось против прежней версии:**
- §4.2 переписан: «DNA» удалён из нормативного словаря, введён *menom*, добавлена таблица уровней с указанием носителя;
- §4.5 и §4.6 слиты в один раздел §4.5 с декомпозицией ZOR/ZOV и различением фактической и представленной зоны;
- прежний §4.6 упразднён; §4.6 теперь — прежний §4.4 (два происхождения ядра), сдвинутый по нумерации;
- ссылка на Келли из §4.5 удалена и перенесена в §8 (запись 2), где она восстанавливается и расширяется.

**Следствия для перекрёстных ссылок в других блоках:** все вхождения «§4.6» в Blocks 1, 2, 3, 5 указывают на конструкты represented social position / source. После правки они находятся в §4.5. Замену выполнить механически: **§4.6 → §4.5** во всех блоках, кроме §4 самого.

---

# 4. Conceptual Framework

The framework in this section was not derived from the experiment in §5. It was formulated earlier, during ordinary project work, and the experiment was designed to test part of it. This ordering matters for how the claims should be read, and is documented first.

## 4.1 Origin: the code-executor incident

The project's central claim originated in a failure that had nothing to do with role-play, identity, or organizational design.

An agent responsible for executing code worked largely by trial and error. Failures accumulated over several weeks. One episode ended with the deletion of the working code together with its archives. **[R]**

The response was not a longer or stricter instruction set. It was a single document, composed by the agent itself under the Author's direction and made required reading at the start of every session and whenever context was lost during one.

Its core is a redefinition of function rather than an intensification of constraint:

> from: Code Generator
> to: Code Scout / Tester
> rule: the agent does not create solutions — it establishes facts.

Supporting structure: read-only operation by default; mandatory confirmation from a designated partner before any risky action; and a four-question self-check to be run before acting at all.

**[R]** Following adoption, unauthorized modification ceased to be the recurring failure mode. No count was kept and no control condition existed; this is a practitioner's impression, not a measurement.

The conclusion drawn at the time was that **role matters more than the specific wording of the prompt.**

That formulation requires immediate qualification, because the document in question *is* a prompt. The distinction claimed is narrower: what changed behaviour was not an extension of the instruction list but a redefinition of what kind of agent was acting, restated by the agent in its own operational language. Whether "role" versus "prompt" is the correct cut is precisely what §5 was designed to test.

A second early document, the project's collaboration charter, records a position this paper partly revises. It states that a pair of agents is the minimal generative unit — one agent produces monologue, two produce dialogue, three or more produce noise without strict coordination — and assigns the third participant a different function entirely: it does not argue, does not generate solutions first, and does not substitute for the dialogue. Its role is to hold the task frame, fix divergences, and integrate conclusions.

This is more precise than the formulation the present authors used subsequently, and §8 adopts it: the structural unit is not three debating agents but **a generative pair plus a non-participating integrator**.

## 4.2 Rule cores, menoms, and what they determine

### 4.2.1 The rule core

The operative construct of this paper:

> A **rule core** fixes the **type** of response to a class of inputs, while leaving the **content** of any particular response undetermined.

The distinction is what makes the claim testable. "Models have stable traits" is not testable, because it does not say what is stable — and model outputs demonstrably vary across identical inputs. "Type is determined, content varies" is testable: identify a class of inputs for which the type of response is not determined, and no core operates at that level.

The source of the idea is Conway's Game of Life, and the analogy is one of **explanation type**, not of subject matter:

| | Rules | What appears | Present in the rules? |
|---|---|---|---|
| Game of Life | three neighbourhood rules | gliders, guns, oscillators | no |
| A physical theory | a minimal axiom core | the derived structure | no, if the claim holds |
| A body of knowledge | axioms and inference rules | the derivation graph | no |
| A language model | a basic rule set | a characteristic response type | no |

Nothing programmed the glider. It appeared. The same question can be asked of all four rows and does not depend on subject matter: **is there a compact core from which the rest unfolds without further stipulation?**

One asymmetry between the rows should be stated, since it bears on how far the analogy carries. In Game of Life the rules **execute**: the glider is obtained by running the automaton, and no reader need take the author's word for it. In a theory stated as text, a chain from axioms to consequences is narrated rather than run. The analogy therefore sets a target rather than describing an achievement, and any claim of the first kind requires an executable artifact to support it.

**Terminological consequence, applied throughout.** A rule core is not observable. Behaviour is. This paper reports behaviour. Any statement about a core is a hypothesis about an unobserved mechanism and is marked **[H]**.

### 4.2.2 Why "behavioural DNA" is withdrawn

Earlier stages of this project used *behavioural DNA* for the same idea, and earlier drafts of this paper retained it. It is withdrawn here, and the reason is internal rather than stylistic.

The genomic metaphor carries a mechanism: **replication** — rules producing copies of rules, transmitted from one carrier to the next. The process this paper describes is **development** — rules producing a structure not itself present in the rules. Genotype to phenotype, not genotype to genotype.

The metaphor therefore contradicts the construct it was chosen to illustrate. Retaining it obliged the text to disclaim biological inheritance at every use, which is a reliable sign that a term is working against its own argument.

*Behavioural DNA* appears in this paper only in this paragraph, as a historical note on the project's earlier vocabulary.

### 4.2.3 Menom

For the informational level a distinct term is required, and this paper introduces one.

> **Menom** — the organized system of informational frames, evaluative patterns and behavioural rules inferred from, or instantiated in, the interpretations and actions of a system or class of systems.

The term extends a series developed in the Author's earlier work on cultural and behavioural transmission, from Dawkins' meme:

| | What it is |
|---|---|
| **Meme** | a unit of cultural or evaluative information |
| **Memoframe** | a structured set of related memes together with rules for interpreting a class of situations |
| **Memocode** | behavioural programs and the rules governing their selection and activation |
| **Menom** | the organized system comprising all three, for a given system or class of systems |

The relation to *genome* is deliberate and partial. A genome is the organized system of an organism's hereditary information; a menom is the organized system of a system's informational and behavioural organization. Like *genome*, the term applies at two levels: to a class (the shared structure) and to an individual (the particular realization). Unlike *genome*, it asserts neither a carrier nor a mode of transmission.

**Two things the term does not assert.** Both distinguish it from the genomic analogy that motivated it, and both matter for what this paper can claim.

*It does not assert a localized carrier.* A menom attributed to a model family is not a structure residing inside its models; it is a regularity inferred from their outputs. Where the corresponding structure in biology sits in every cell, here nothing has been identified that holds it. The carrier differs by level:

| Level | Carrier |
|---|---|
| Menom of a conversation | context window plus platform persistence — localized and, in principle, inspectable (§2.10) |
| Menom of a model version | weights — localized, not inspectable in commercial deployment |
| Menom of a model family | none identified; a regularity inferred from outputs |
| Menom of a human population | none established |

Two of the four levels have an identified carrier. This paper's observations concern the first; its untested hypothesis concerns the third (§6.4).

*It does not assert transmission.* Successive versions of a model family do not inherit weights from one another; each is trained anew. Where a behavioural pattern persists across versions, it persists because comparable conditions were reproduced — similar data, similar procedures, similar tuning policies — not because anything was passed on. This is closer to convergence under similar developmental conditions than to inheritance.

**The definition therefore does not settle the paper's empirical question in advance.** Whether a menom persists across carriers, versions, accounts or families is what §4.3 asks and §11 proposes to test. Building persistence into the definition would make the question a tautology.

### 4.2.4 One claim this paper does not make

The vocabulary above was developed for human cultural and behavioural transmission, where the informational substrate has no established physical carrier and is described in terms — the collective unconscious among them — that this paper takes no position on.

Artificial systems differ in one respect that is relevant here: their informational substrate is technically instantiated. Training corpora, weights, context states, external memory and interaction protocols can be recorded, modified and compared. This makes menom-like structures directly examinable in a way they are not in the human case.

**It does not follow that human collective information structures exist, or that they have been given a carrier.** The claim made here is narrower: informational and behavioural structures of the kind previously described for humans can also be realized in artificial systems, and in artificial systems they are open to inspection. Whether the human case is of the same kind is a separate question, and this paper does not answer it.

### 4.2.5 Relation between menom and rule core

The two terms operate at different scales and should not be substituted for one another.

A **rule core** is what fixes the type of response within one system, at one level of scope. It is the construct this paper's observations concern, and it is what §4.3 locates on a scale.

A **menom** is the organized whole from which such cores are drawn — frames, evaluative patterns and behavioural rules together. A rule core may be understood as the operative subset of a menom active for a given class of inputs.

Where this paper reports evidence, it reports evidence about rule cores. *Menom* is the wider term, introduced because the narrower one does not cover the informational content that accompanies behavioural organization, and because the paper's material spans both.

## 4.3 The nesting question, and two scales

Once cores are distinguished from behaviour, the observations in this paper stop being a list of separate findings and become measurements along a scale. The scale is the **scope** over which a core operates.

Two scales must be distinguished, and they are orthogonal.

**Scale 1 — carrier of state.** Where the persistence physically resides.

| Scope | Phenomenon | Status |
|---|---|---|
| Single turn | — | — |
| Episode within a conversation | context imprinting (§6.1) | **[P]** |
| Whole conversation | role inertia (§6.2) | **[P]** |
| Account | account-scoped persistence (§6.3) | **[P-A]**, open |
| Model family | family-level priors (§6.4) | **[H]**, confounded |

**Scale 2 — scope of a shared premise.** What is governed by an initial setting shared across participants: the model, the role, the interaction history, the group, or the whole research frame.

The two do not collapse into one. In a hybrid arrangement the carrier of one level may be a model and the carrier of another a human: the frame-level premise discussed in §12.4 — a shared initial framing inherited by every participant — is carried by the coordinator, not by any model, and therefore has no position on Scale 1 at all.

The measurements reported in this paper lie on **Scale 1**. Scale 2 is used where a phenomenon concerns a premise shared across participants rather than state held by one.

This gives the research programme a single empirical question:

> **At what level of nesting is a rule core fixed?**

Every observation reported here answers it at one level, and every experiment proposed in §11 separates one level from the level beneath it.

We prefer this formulation to the broader one used in earlier drafts ("the study of social behaviour in AI systems"), which specifies neither what would be measured nor what would refute it.

## 4.4 Two origins, one mechanism

A core may become fixed in two ways.

**Present before the interaction begins.** Architecture, training, alignment procedure and system configuration are in place before any exchange occurs. Scope: in principle, every instance of that model family.

**Fixed during the interaction.** A particular early episode establishes what kind of work is being done and by what standards, and later inputs are interpreted relative to it. Scope: the contour in which it occurred — an episode, a conversation, possibly an account.

After fixation the mechanism is the same in both cases: the core determines the type of response to subsequent inputs. Only the moment and the scope differ. This mirrors imprinting in the ethological sense, which does not alter the genome yet produces an equally fixed response — which is why the same vocabulary is used for both here.

## 4.5 Boundaries: ZOR, ZOV, and the represented case

This section replaces two that stood separately in earlier drafts — one defining the boundaries of a participant's position, one defining the constructs the experiment varied. They belong together, and §4.5.4 states why.

### 4.5.1 The two boundaries

Two boundaries define a participant's position, and they must be specified separately. We abbreviate them **ZOR** and **ZOV** and use the abbreviations throughout.

> **ZOV — zone of visibility.** The limits of the information and context available to a participant when forming a response or decision.
>
> **ZOR — zone of responsibility.** The limits of the decisions, actions and handoffs for which the participant is accountable within the process.

Earlier formulations of this project stated the pair as "what the participant sees" and "what the participant does". That is insufficient, and the insufficiency produced a documented error. Those formulations conflate three distinct operations: **holding** information, **transmitting** it, and **acting on** it. A participant may hold information it may not transmit; may be accountable for a decision while holding limited context; may be obliged to transmit a result it is not entitled to evaluate.

This is the same conflation that produced the terminological failure recorded in §4.2.2, where a property of a carrier (replication of a molecule) was substituted for a property of a process (production of structure). The decompositions below exist to prevent it recurring.

### 4.5.2 ZOV — four components

- **Context access** — which messages, documents, data and prior decisions are available to the participant.
- **Source visibility** — whether the participant knows the actual origin of a message or only its declared attribution.
- **Relational visibility** — whether the participant knows the roles, relationships and interaction history of other participants.
- **Output visibility** — which results produced by others the participant sees before forming its own.

ZOV governs availability only. It does not entail that the participant interprets the available information correctly, nor that it is entitled to transmit it.

The experiment in §5 manipulated **relational visibility** primarily and **source visibility** secondarily (§5.5); the other two were held constant.

### 4.5.3 ZOR — five components

- **Decision authority** — which decisions the participant is entitled to make.
- **Action authority** — which actions it may or must perform.
- **Validation duty** — which claims it is obliged to verify.
- **Handoff authority** — what material it transmits, in what status, and to whom.
- **Escalation duty** — which questions it must return to the Author or another responsible participant rather than resolve on its own.

**Validation duty is the component most often omitted, and its omission is not benign.** A participant assigned a verification task without the corresponding duty — and, critically, without the ZOV to discharge it — will produce a plausible answer rather than declining. §12.4.1 documents an instance from this project's own preparation. §9.5 develops the design consequence.

### 4.5.4 Actual versus represented ZOV and ZOR

A distinction that unifies this section with the experiment.

> **Actual ZOV/ZOR** — the boundaries the system in fact enforces: what the participant can access, and what its outputs can affect.
>
> **Represented ZOV/ZOR** — the boundaries described to the participant in its prompt, whether or not the system enforces them.

The two need not coincide, and in the arrangement studied here they systematically did not. The organizational structure existed **only as text**: colleagues, councils and institutional positions described to participants and never implemented as channels. Every participant's actual ZOV was its context window; its represented ZOV was an institutional position within a described organization.

This yields the two constructs the experiment varied, and which earlier drafts introduced separately:

> **Represented social position** — a description of an agent's place within an organizational structure, supplied in the prompt regardless of whether the described channels exist. This is represented ZOV and ZOR taken together, at the level of a participant's standing in the arrangement.

> **Represented social source** — the claimed origin and status of an incoming message, whether declared explicitly or inferred from stylistic cues. This is the source-visibility component of ZOV, in its represented form. Inference of this kind is probabilistic and should not be described as access to authorship.

**The methodological consequence is the reason this distinction is stated at all.** A change in represented ZOV cannot be interpreted as a change in actual ZOV, in the participant's role, or in its menom. The experiment in §5 varied the representation while the actual boundaries were unchanged — every message passed through one human, and no access was in fact restricted or granted. A model that responds to a described organizational structure is responding to a description, and the paper's claims are correspondingly limited (§2.9).

Divergence between actual and represented boundaries is itself an experimental variable, and one this paper did not vary systematically: all its observations lie on one side of it.

### 4.5.5 The boundaries are asymmetric

Each participant has a **boundary above** — the source of its assignments and the authority that may reject its output — and a **boundary below** — the layer it directs or evaluates. The relation between participants is therefore not symmetric.

In the project's implementation triad — Author, specification writer, code executor — this asymmetry is fixed at the role level: the Author sets direction, the specification writer converts direction into executable specifications, the executor performs them and reports.

**Nesting is perspectival, not absolute.** The executor may treat the code base itself as the layer below it. Two peer analysts, assigned complementary functions and instructed not to seek consensus, may each regard the other as occupying the layer below. The level is determined by the observer's position, not by an absolute hierarchy — the same participant can be the upper boundary for one role and the lower boundary for another.

### 4.5.6 Memes and memocode are not ZOV and ZOR

A correspondence suggests itself and does not hold; stating it prevents a plausible confusion.

The meme/memocode distinction (§4.2.3) separates **evaluative information** from **executable behavioural organization**. The ZOV/ZOR distinction separates **what is available** from **what is accountable**. These are independent classifications of the same material, not a matching pair.

A participant may hold evaluative information within its ZOV while the decision to apply it lies in another participant's ZOR. Conversely, a behavioural rule may fall within a participant's ZOR — it is obliged to execute — while the rule's rationale lies outside its ZOV.

Memes and memocode therefore cross both zones rather than corresponding to them. The two distinctions are orthogonal and are used independently throughout.

## 4.6 What is required for a complete role specification

Deferred to §9.5, which states what a complete ZOR and ZOV specification must contain and gives the design rules that follow. This section defines the terms; §9 applies them.
=======
# REVISIONS — накопительный файл

**Назначение.** Заменяющие блоки к каноническому тексту (Blocks 1–5). Каждая запись указывает, что именно замещается. Файл пополняется; сохранять в конце целиком.

**Статус на текущую запись:** внесена правка §4 (пункты 15, 16, 18 плана; частично 17).

---

# ЗАПИСЬ 1 — Section 4, полная замена

**Заменяет:** §4.1–§4.6 в BLOCK 2 целиком, от заголовка «# 4. Conceptual Framework» до строки, предшествующей «# 5. The Role-Reconfiguration Experiment».

**Что изменилось против прежней версии:**
- §4.2 переписан: «DNA» удалён из нормативного словаря, введён *menom*, добавлена таблица уровней с указанием носителя;
- §4.5 и §4.6 слиты в один раздел §4.5 с декомпозицией ZOR/ZOV и различением фактической и представленной зоны;
- прежний §4.6 упразднён; §4.6 теперь — прежний §4.4 (два происхождения ядра), сдвинутый по нумерации;
- ссылка на Келли из §4.5 удалена и перенесена в §8 (запись 2), где она восстанавливается и расширяется.

**Следствия для перекрёстных ссылок в других блоках:** все вхождения «§4.6» в Blocks 1, 2, 3, 5 указывают на конструкты represented social position / source. После правки они находятся в §4.5. Замену выполнить механически: **§4.6 → §4.5** во всех блоках, кроме §4 самого.

---

# 4. Conceptual Framework

The framework in this section was not derived from the experiment in §5. It was formulated earlier, during ordinary project work, and the experiment was designed to test part of it. This ordering matters for how the claims should be read, and is documented first.

## 4.1 Origin: the code-executor incident

The project's central claim originated in a failure that had nothing to do with role-play, identity, or organizational design.

An agent responsible for executing code worked largely by trial and error. Failures accumulated over several weeks. One episode ended with the deletion of the working code together with its archives. **[R]**

The response was not a longer or stricter instruction set. It was a single document, composed by the agent itself under the Author's direction and made required reading at the start of every session and whenever context was lost during one.

Its core is a redefinition of function rather than an intensification of constraint:

> from: Code Generator
> to: Code Scout / Tester
> rule: the agent does not create solutions — it establishes facts.

Supporting structure: read-only operation by default; mandatory confirmation from a designated partner before any risky action; and a four-question self-check to be run before acting at all.

**[R]** Following adoption, unauthorized modification ceased to be the recurring failure mode. No count was kept and no control condition existed; this is a practitioner's impression, not a measurement.

The conclusion drawn at the time was that **role matters more than the specific wording of the prompt.**

That formulation requires immediate qualification, because the document in question *is* a prompt. The distinction claimed is narrower: what changed behaviour was not an extension of the instruction list but a redefinition of what kind of agent was acting, restated by the agent in its own operational language. Whether "role" versus "prompt" is the correct cut is precisely what §5 was designed to test.

A second early document, the project's collaboration charter, records a position this paper partly revises. It states that a pair of agents is the minimal generative unit — one agent produces monologue, two produce dialogue, three or more produce noise without strict coordination — and assigns the third participant a different function entirely: it does not argue, does not generate solutions first, and does not substitute for the dialogue. Its role is to hold the task frame, fix divergences, and integrate conclusions.

This is more precise than the formulation the present authors used subsequently, and §8 adopts it: the structural unit is not three debating agents but **a generative pair plus a non-participating integrator**.

## 4.2 Rule cores, menoms, and what they determine

### 4.2.1 The rule core

The operative construct of this paper:

> A **rule core** fixes the **type** of response to a class of inputs, while leaving the **content** of any particular response undetermined.

The distinction is what makes the claim testable. "Models have stable traits" is not testable, because it does not say what is stable — and model outputs demonstrably vary across identical inputs. "Type is determined, content varies" is testable: identify a class of inputs for which the type of response is not determined, and no core operates at that level.

The source of the idea is Conway's Game of Life, and the analogy is one of **explanation type**, not of subject matter:

| | Rules | What appears | Present in the rules? |
|---|---|---|---|
| Game of Life | three neighbourhood rules | gliders, guns, oscillators | no |
| A physical theory | a minimal axiom core | the derived structure | no, if the claim holds |
| A body of knowledge | axioms and inference rules | the derivation graph | no |
| A language model | a basic rule set | a characteristic response type | no |

Nothing programmed the glider. It appeared. The same question can be asked of all four rows and does not depend on subject matter: **is there a compact core from which the rest unfolds without further stipulation?**

One asymmetry between the rows should be stated, since it bears on how far the analogy carries. In Game of Life the rules **execute**: the glider is obtained by running the automaton, and no reader need take the author's word for it. In a theory stated as text, a chain from axioms to consequences is narrated rather than run. The analogy therefore sets a target rather than describing an achievement, and any claim of the first kind requires an executable artifact to support it.

**Terminological consequence, applied throughout.** A rule core is not observable. Behaviour is. This paper reports behaviour. Any statement about a core is a hypothesis about an unobserved mechanism and is marked **[H]**.

### 4.2.2 Why "behavioural DNA" is withdrawn

Earlier stages of this project used *behavioural DNA* for the same idea, and earlier drafts of this paper retained it. It is withdrawn here, and the reason is internal rather than stylistic.

The genomic metaphor carries a mechanism: **replication** — rules producing copies of rules, transmitted from one carrier to the next. The process this paper describes is **development** — rules producing a structure not itself present in the rules. Genotype to phenotype, not genotype to genotype.

The metaphor therefore contradicts the construct it was chosen to illustrate. Retaining it obliged the text to disclaim biological inheritance at every use, which is a reliable sign that a term is working against its own argument.

*Behavioural DNA* appears in this paper only in this paragraph, as a historical note on the project's earlier vocabulary.

### 4.2.3 Menom

For the informational level a distinct term is required, and this paper introduces one.

> **Menom** — the organized system of informational frames, evaluative patterns and behavioural rules inferred from, or instantiated in, the interpretations and actions of a system or class of systems.

The term extends a series developed in the Author's earlier work on cultural and behavioural transmission, from Dawkins' meme:

| | What it is |
|---|---|
| **Meme** | a unit of cultural or evaluative information |
| **Memoframe** | a structured set of related memes together with rules for interpreting a class of situations |
| **Memocode** | behavioural programs and the rules governing their selection and activation |
| **Menom** | the organized system comprising all three, for a given system or class of systems |

The relation to *genome* is deliberate and partial. A genome is the organized system of an organism's hereditary information; a menom is the organized system of a system's informational and behavioural organization. Like *genome*, the term applies at two levels: to a class (the shared structure) and to an individual (the particular realization). Unlike *genome*, it asserts neither a carrier nor a mode of transmission.

**Two things the term does not assert.** Both distinguish it from the genomic analogy that motivated it, and both matter for what this paper can claim.

*It does not assert a localized carrier.* A menom attributed to a model family is not a structure residing inside its models; it is a regularity inferred from their outputs. Where the corresponding structure in biology sits in every cell, here nothing has been identified that holds it. The carrier differs by level:

| Level | Carrier |
|---|---|
| Menom of a conversation | context window plus platform persistence — localized and, in principle, inspectable (§2.10) |
| Menom of a model version | weights — localized, not inspectable in commercial deployment |
| Menom of a model family | none identified; a regularity inferred from outputs |
| Menom of a human population | none established |

Two of the four levels have an identified carrier. This paper's observations concern the first; its untested hypothesis concerns the third (§6.4).

*It does not assert transmission.* Successive versions of a model family do not inherit weights from one another; each is trained anew. Where a behavioural pattern persists across versions, it persists because comparable conditions were reproduced — similar data, similar procedures, similar tuning policies — not because anything was passed on. This is closer to convergence under similar developmental conditions than to inheritance.

**The definition therefore does not settle the paper's empirical question in advance.** Whether a menom persists across carriers, versions, accounts or families is what §4.3 asks and §11 proposes to test. Building persistence into the definition would make the question a tautology.

### 4.2.4 One claim this paper does not make

The vocabulary above was developed for human cultural and behavioural transmission, where the informational substrate has no established physical carrier and is described in terms — the collective unconscious among them — that this paper takes no position on.

Artificial systems differ in one respect that is relevant here: their informational substrate is technically instantiated. Training corpora, weights, context states, external memory and interaction protocols can be recorded, modified and compared. This makes menom-like structures directly examinable in a way they are not in the human case.

**It does not follow that human collective information structures exist, or that they have been given a carrier.** The claim made here is narrower: informational and behavioural structures of the kind previously described for humans can also be realized in artificial systems, and in artificial systems they are open to inspection. Whether the human case is of the same kind is a separate question, and this paper does not answer it.

### 4.2.5 Relation between menom and rule core

The two terms operate at different scales and should not be substituted for one another.

A **rule core** is what fixes the type of response within one system, at one level of scope. It is the construct this paper's observations concern, and it is what §4.3 locates on a scale.

A **menom** is the organized whole from which such cores are drawn — frames, evaluative patterns and behavioural rules together. A rule core may be understood as the operative subset of a menom active for a given class of inputs.

Where this paper reports evidence, it reports evidence about rule cores. *Menom* is the wider term, introduced because the narrower one does not cover the informational content that accompanies behavioural organization, and because the paper's material spans both.

## 4.3 The nesting question, and two scales

Once cores are distinguished from behaviour, the observations in this paper stop being a list of separate findings and become measurements along a scale. The scale is the **scope** over which a core operates.

Two scales must be distinguished, and they are orthogonal.

**Scale 1 — carrier of state.** Where the persistence physically resides.

| Scope | Phenomenon | Status |
|---|---|---|
| Single turn | — | — |
| Episode within a conversation | context imprinting (§6.1) | **[P]** |
| Whole conversation | role inertia (§6.2) | **[P]** |
| Account | account-scoped persistence (§6.3) | **[P-A]**, open |
| Model family | family-level priors (§6.4) | **[H]**, confounded |

**Scale 2 — scope of a shared premise.** What is governed by an initial setting shared across participants: the model, the role, the interaction history, the group, or the whole research frame.

The two do not collapse into one. In a hybrid arrangement the carrier of one level may be a model and the carrier of another a human: the frame-level premise discussed in §12.4 — a shared initial framing inherited by every participant — is carried by the coordinator, not by any model, and therefore has no position on Scale 1 at all.

The measurements reported in this paper lie on **Scale 1**. Scale 2 is used where a phenomenon concerns a premise shared across participants rather than state held by one.

This gives the research programme a single empirical question:

> **At what level of nesting is a rule core fixed?**

Every observation reported here answers it at one level, and every experiment proposed in §11 separates one level from the level beneath it.

We prefer this formulation to the broader one used in earlier drafts ("the study of social behaviour in AI systems"), which specifies neither what would be measured nor what would refute it.

## 4.4 Two origins, one mechanism

A core may become fixed in two ways.

**Present before the interaction begins.** Architecture, training, alignment procedure and system configuration are in place before any exchange occurs. Scope: in principle, every instance of that model family.

**Fixed during the interaction.** A particular early episode establishes what kind of work is being done and by what standards, and later inputs are interpreted relative to it. Scope: the contour in which it occurred — an episode, a conversation, possibly an account.

After fixation the mechanism is the same in both cases: the core determines the type of response to subsequent inputs. Only the moment and the scope differ. This mirrors imprinting in the ethological sense, which does not alter the genome yet produces an equally fixed response — which is why the same vocabulary is used for both here.

## 4.5 Boundaries: ZOR, ZOV, and the represented case

This section replaces two that stood separately in earlier drafts — one defining the boundaries of a participant's position, one defining the constructs the experiment varied. They belong together, and §4.5.4 states why.

### 4.5.1 The two boundaries

Two boundaries define a participant's position, and they must be specified separately. We abbreviate them **ZOR** and **ZOV** and use the abbreviations throughout.

> **ZOV — zone of visibility.** The limits of the information and context available to a participant when forming a response or decision.
>
> **ZOR — zone of responsibility.** The limits of the decisions, actions and handoffs for which the participant is accountable within the process.

Earlier formulations of this project stated the pair as "what the participant sees" and "what the participant does". That is insufficient, and the insufficiency produced a documented error. Those formulations conflate three distinct operations: **holding** information, **transmitting** it, and **acting on** it. A participant may hold information it may not transmit; may be accountable for a decision while holding limited context; may be obliged to transmit a result it is not entitled to evaluate.

This is the same conflation that produced the terminological failure recorded in §4.2.2, where a property of a carrier (replication of a molecule) was substituted for a property of a process (production of structure). The decompositions below exist to prevent it recurring.

### 4.5.2 ZOV — four components

- **Context access** — which messages, documents, data and prior decisions are available to the participant.
- **Source visibility** — whether the participant knows the actual origin of a message or only its declared attribution.
- **Relational visibility** — whether the participant knows the roles, relationships and interaction history of other participants.
- **Output visibility** — which results produced by others the participant sees before forming its own.

ZOV governs availability only. It does not entail that the participant interprets the available information correctly, nor that it is entitled to transmit it.

The experiment in §5 manipulated **relational visibility** primarily and **source visibility** secondarily (§5.5); the other two were held constant.

### 4.5.3 ZOR — five components

- **Decision authority** — which decisions the participant is entitled to make.
- **Action authority** — which actions it may or must perform.
- **Validation duty** — which claims it is obliged to verify.
- **Handoff authority** — what material it transmits, in what status, and to whom.
- **Escalation duty** — which questions it must return to the Author or another responsible participant rather than resolve on its own.

**Validation duty is the component most often omitted, and its omission is not benign.** A participant assigned a verification task without the corresponding duty — and, critically, without the ZOV to discharge it — will produce a plausible answer rather than declining. §12.4.1 documents an instance from this project's own preparation. §9.5 develops the design consequence.

### 4.5.4 Actual versus represented ZOV and ZOR

A distinction that unifies this section with the experiment.

> **Actual ZOV/ZOR** — the boundaries the system in fact enforces: what the participant can access, and what its outputs can affect.
>
> **Represented ZOV/ZOR** — the boundaries described to the participant in its prompt, whether or not the system enforces them.

The two need not coincide, and in the arrangement studied here they systematically did not. The organizational structure existed **only as text**: colleagues, councils and institutional positions described to participants and never implemented as channels. Every participant's actual ZOV was its context window; its represented ZOV was an institutional position within a described organization.

This yields the two constructs the experiment varied, and which earlier drafts introduced separately:

> **Represented social position** — a description of an agent's place within an organizational structure, supplied in the prompt regardless of whether the described channels exist. This is represented ZOV and ZOR taken together, at the level of a participant's standing in the arrangement.

> **Represented social source** — the claimed origin and status of an incoming message, whether declared explicitly or inferred from stylistic cues. This is the source-visibility component of ZOV, in its represented form. Inference of this kind is probabilistic and should not be described as access to authorship.

**The methodological consequence is the reason this distinction is stated at all.** A change in represented ZOV cannot be interpreted as a change in actual ZOV, in the participant's role, or in its menom. The experiment in §5 varied the representation while the actual boundaries were unchanged — every message passed through one human, and no access was in fact restricted or granted. A model that responds to a described organizational structure is responding to a description, and the paper's claims are correspondingly limited (§2.9).

Divergence between actual and represented boundaries is itself an experimental variable, and one this paper did not vary systematically: all its observations lie on one side of it.

### 4.5.5 The boundaries are asymmetric

Each participant has a **boundary above** — the source of its assignments and the authority that may reject its output — and a **boundary below** — the layer it directs or evaluates. The relation between participants is therefore not symmetric.

In the project's implementation triad — Author, specification writer, code executor — this asymmetry is fixed at the role level: the Author sets direction, the specification writer converts direction into executable specifications, the executor performs them and reports.

**Nesting is perspectival, not absolute.** The executor may treat the code base itself as the layer below it. Two peer analysts, assigned complementary functions and instructed not to seek consensus, may each regard the other as occupying the layer below. The level is determined by the observer's position, not by an absolute hierarchy — the same participant can be the upper boundary for one role and the lower boundary for another.

### 4.5.6 Memes and memocode are not ZOV and ZOR

A correspondence suggests itself and does not hold; stating it prevents a plausible confusion.

The meme/memocode distinction (§4.2.3) separates **evaluative information** from **executable behavioural organization**. The ZOV/ZOR distinction separates **what is available** from **what is accountable**. These are independent classifications of the same material, not a matching pair.

A participant may hold evaluative information within its ZOV while the decision to apply it lies in another participant's ZOR. Conversely, a behavioural rule may fall within a participant's ZOR — it is obliged to execute — while the rule's rationale lies outside its ZOV.

Memes and memocode therefore cross both zones rather than corresponding to them. The two distinctions are orthogonal and are used independently throughout.

## 4.6 What is required for a complete role specification

Deferred to §9.5, which states what a complete ZOR and ZOV specification must contain and gives the design rules that follow. This section defines the terms; §9 applies them.

---

# ЗАПИСЬ 2 — Section 8, частичная замена

**Заменяет три фрагмента BLOCK 4:**

1. §8.9 целиком — новой редакцией §8.9 (терминология Методолога: две оси, роль ≠ конструкт).
2. §8.10 целиком — исправленной редакцией (сняты «four drafts» и неточность об онтологическом ревью).
3. **Вставляется новый §8.11** — Келли, после §8.10, перед заголовком «# 9. Design Principles».

**§8.1–§8.8 остаются без изменений.**

**Следствие:** §11.4 (E8) переписывается в записи 3 под протокол репертуарной решётки, определённый в §8.11.

---

## 8.9 Two axes of heterogeneity **[H]**

The claim that heterogeneous participants outperform homogeneous ones requires a distinction the existing literature does not draw, and that earlier drafts of this paper also failed to draw.

**Axis 1 — functional heterogeneity.** Participants differ in assigned function: ZOR, ZOV, and consequently the class of error each is positioned to detect. This concerns organizational architecture and is independent of what implements each role.

**Axis 2 — carrier heterogeneity.** Participants differ in the model family implementing them, and therefore in behavioural defaults, optimization priorities and characteristic failure modes. This concerns the selection of carriers for roles.

The axes are independent. Two participants may hold different functions on the same carrier; two may hold the same function on different carriers; both may vary together, as they did here.

**The literature addresses Axis 2.** Zhang et al. (2025) evaluate five representative multi-agent debate methods across nine benchmarks and four foundation models, reporting that debate frequently fails to outperform single-agent chain-of-thought or self-consistency baselines even at substantially higher inference cost — while model heterogeneity consistently improves the same frameworks (§2.5). ⚠ Choi et al. (2025) report that identity-driven accommodation among debating agents is nearly eliminated by anonymizing the source of each response, which bears on the construct of represented social source (§4.5.4).

Both findings concern which carrier implements a participant. Neither addresses whether participants holding different functions detect different classes of error.

The arrangement described in this paper varied both axes simultaneously. Functional roles were specified independently of the carrier and were in several cases filled by different families; in other cases two distinct roles were filled by the same family.

What follows, and what does not:

- **Distinguishable in principle.** The two axes are conceptually separable and were confounded in earlier formulations, including our own. **[H]**
- **Implemented here.** Both axes were varied. This is a description of what was done. **[R]**
- **Not established.** That combining both axes outperforms either alone; that functional specialization operates independently of carrier; that any of these arrangements outperforms a single participant. No comparison was run against any alternative, and none of these claims should be read into the account above.

The separation is proposed as a design distinction, not as a result. The experiment that would convert it into one is specified in §11.4 (E8), and its measurement procedure is developed in §8.11.

## 8.10 Editor's note on the preparation of this paper **[P-A]**

**Convention.** Editor's notes in this paper report observable facts about the process of its preparation. They do not evaluate the effectiveness of that process. The reason is internal: §5.5 establishes that a participant's self-report about its own performance is not evidence of that performance, and a note asserting that an arrangement worked well would be exactly such a report.

In the course of preparing this manuscript, participants occupying different roles identified different classes of error. In the cases recorded, an error identified by one participant had not been identified by the others.

Specifically:

- **Procedural and evidential errors** — an inverted description of an experimental result that had persisted through several successive drafts; misattributed sources; fabricated citations; unlisted confounds — were identified in editorial review.
- **Architectural errors** — an over-general claim about the existing literature that a single counter-example would have refuted — were identified in methodological review.
- **Ontological errors** — a claim of invention where the material supported only a claim of observation; a self-referentiality risk in relating the paper to its host project; the terminological failure recorded in §4.2.2 — were identified in ontological review, conducted on the editorial memoranda rather than on the manuscript itself.
- **Factual errors concerning the project's own materials** were identified by the Author.

This is a record of what occurred. It is **not** evidence that the arrangement outperforms a single reviewer: no comparison was run, no count was kept of errors that all participants missed, and by construction such errors are not observable from within the arrangement (§7.5).

One explanation is available and is offered as hypothesis rather than finding: the participants differed less in capability than in what each was positioned to see. Under §4.5 that is a difference in ZOV, and it generates a prediction — the same participant, moved to a different role, should begin detecting a different class of error. That prediction has not been tested; §11.4 (E8) specifies how it would be. **[H]**

## 8.11 Constructs, not participants: the Kelly apparatus **[H]**

Earlier drafts of this paper cited George Kelly's triadic elicitation as support for the structure described in §8.1–§8.5, then withdrew the citation on the grounds that Kelly's method is symmetric while the structure here is not. Both moves were mistaken, and in the same way: they treated Kelly as a claim about the number three.

He offers something else, and it is what this section restores.

### 8.11.1 What Kelly's method supplies

In Kelly's theory of personal constructs, a **construct** is a bipolar evaluative axis along which a subject classifies experience — *rigorous / declarative*, *derivable / asserted*, *traceable / unattributed*. Constructs are not opinions about particular objects; they are the dimensions along which objects are placed.

The **triadic elicitation method** obtains them. Three elements are presented and the subject is asked: *in what respect are two of these alike, and thereby different from the third?* The answer names a dimension the subject was already using but had not stated. The method is a procedure for making implicit evaluative axes explicit.

The **repertory grid** records the result: rows are elements, columns are elicited constructs, cells are ratings of each element on each axis. Constructs may be weighted. The grid is a measurable object — correlations between raters' rating vectors indicate whether they are in fact applying different axes or the same axis under different names.

### 8.11.2 A role is not a construct

The natural extension — three participants supply three constructs — is a reification and must be resisted.

A construct is a property of the **act of evaluation**, not of the evaluator. One participant may apply several constructs to one object. Two participants may apply the same construct and reach identical conclusions, which is precisely the case in which adding the second participant contributes nothing.

The defensible claim is weaker and probabilistic:

> Participants holding different ZOR and ZOV are **more likely** to apply different systems of constructs to the same object than participants holding the same function.

This is consistent with what §8.10 records — editorial review producing evidential axes, methodological review producing architectural ones, ontological review producing categorial ones — without asserting that a role *is* an axis. And unlike the earlier formulation, it is testable: construct independence is measurable as correlation between rating vectors.

### 8.11.3 Why this matters to the structure

The connection to §8.5 is direct. An integrator that does not enter the dispute is not applying a competing construct to the same object; it is applying a construct to the **exchange** — coherence of the disagreement, whether divergence is substantive or terminological, whether the pair's criteria are commensurable at all. That is a different axis rather than a different position on the same axis, and it is the reason the integrator's contribution is not simply a third opinion.

This also refines what the structural hypothesis (§8.2) actually claims. Not that three participants are better than two, but that **an arrangement is informative to the extent that its participants apply non-identical constructs to the object, and to the extent that at least one construct is applied to the exchange rather than to the object.** Whether a given arrangement achieves this is measurable rather than assumed.

### 8.11.4 What is borrowed and what is not

Borrowed: the definition of a construct as an evaluative axis; the elicitation method; the grid as a recording and measurement instrument; the notion of construct independence.

Not borrowed: any claim that three is a privileged number. Kelly's triads are a technique for eliciting axes from one subject, not a statement about group composition. The structure in §8.2 is asymmetric — a generative pair plus a non-participating integrator — and Kelly's method says nothing for or against it.

The apparatus is used here for measurement, not for justification. §11.4 (E8) applies it.

========

# REVISIONS — накопительный файл

**Назначение.** Заменяющие блоки к каноническому тексту (Blocks 1–5). Каждая запись указывает, что именно замещается. Файл пополняется; сохранять в конце целиком.

**Статус на текущую запись:** внесена правка §4 (пункты 15, 16, 18 плана; частично 17).

---

# ЗАПИСЬ 1 — Section 4, полная замена

**Заменяет:** §4.1–§4.6 в BLOCK 2 целиком, от заголовка «# 4. Conceptual Framework» до строки, предшествующей «# 5. The Role-Reconfiguration Experiment».

**Что изменилось против прежней версии:**
- §4.2 переписан: «DNA» удалён из нормативного словаря, введён *menom*, добавлена таблица уровней с указанием носителя;
- §4.5 и §4.6 слиты в один раздел §4.5 с декомпозицией ZOR/ZOV и различением фактической и представленной зоны;
- прежний §4.6 упразднён; §4.6 теперь — прежний §4.4 (два происхождения ядра), сдвинутый по нумерации;
- ссылка на Келли из §4.5 удалена и перенесена в §8 (запись 2), где она восстанавливается и расширяется.

**Следствия для перекрёстных ссылок в других блоках:** все вхождения «§4.6» в Blocks 1, 2, 3, 5 указывают на конструкты represented social position / source. После правки они находятся в §4.5. Замену выполнить механически: **§4.6 → §4.5** во всех блоках, кроме §4 самого.

---

# 4. Conceptual Framework

The framework in this section was not derived from the experiment in §5. It was formulated earlier, during ordinary project work, and the experiment was designed to test part of it. This ordering matters for how the claims should be read, and is documented first.

## 4.1 Origin: the code-executor incident

The project's central claim originated in a failure that had nothing to do with role-play, identity, or organizational design.

An agent responsible for executing code worked largely by trial and error. Failures accumulated over several weeks. One episode ended with the deletion of the working code together with its archives. **[R]**

The response was not a longer or stricter instruction set. It was a single document, composed by the agent itself under the Author's direction and made required reading at the start of every session and whenever context was lost during one.

Its core is a redefinition of function rather than an intensification of constraint:

> from: Code Generator
> to: Code Scout / Tester
> rule: the agent does not create solutions — it establishes facts.

Supporting structure: read-only operation by default; mandatory confirmation from a designated partner before any risky action; and a four-question self-check to be run before acting at all.

**[R]** Following adoption, unauthorized modification ceased to be the recurring failure mode. No count was kept and no control condition existed; this is a practitioner's impression, not a measurement.

The conclusion drawn at the time was that **role matters more than the specific wording of the prompt.**

That formulation requires immediate qualification, because the document in question *is* a prompt. The distinction claimed is narrower: what changed behaviour was not an extension of the instruction list but a redefinition of what kind of agent was acting, restated by the agent in its own operational language. Whether "role" versus "prompt" is the correct cut is precisely what §5 was designed to test.

A second early document, the project's collaboration charter, records a position this paper partly revises. It states that a pair of agents is the minimal generative unit — one agent produces monologue, two produce dialogue, three or more produce noise without strict coordination — and assigns the third participant a different function entirely: it does not argue, does not generate solutions first, and does not substitute for the dialogue. Its role is to hold the task frame, fix divergences, and integrate conclusions.

This is more precise than the formulation the present authors used subsequently, and §8 adopts it: the structural unit is not three debating agents but **a generative pair plus a non-participating integrator**.

## 4.2 Rule cores, menoms, and what they determine

### 4.2.1 The rule core

The operative construct of this paper:

> A **rule core** fixes the **type** of response to a class of inputs, while leaving the **content** of any particular response undetermined.

The distinction is what makes the claim testable. "Models have stable traits" is not testable, because it does not say what is stable — and model outputs demonstrably vary across identical inputs. "Type is determined, content varies" is testable: identify a class of inputs for which the type of response is not determined, and no core operates at that level.

The source of the idea is Conway's Game of Life, and the analogy is one of **explanation type**, not of subject matter:

| | Rules | What appears | Present in the rules? |
|---|---|---|---|
| Game of Life | three neighbourhood rules | gliders, guns, oscillators | no |
| A physical theory | a minimal axiom core | the derived structure | no, if the claim holds |
| A body of knowledge | axioms and inference rules | the derivation graph | no |
| A language model | a basic rule set | a characteristic response type | no |

Nothing programmed the glider. It appeared. The same question can be asked of all four rows and does not depend on subject matter: **is there a compact core from which the rest unfolds without further stipulation?**

One asymmetry between the rows should be stated, since it bears on how far the analogy carries. In Game of Life the rules **execute**: the glider is obtained by running the automaton, and no reader need take the author's word for it. In a theory stated as text, a chain from axioms to consequences is narrated rather than run. The analogy therefore sets a target rather than describing an achievement, and any claim of the first kind requires an executable artifact to support it.

**Terminological consequence, applied throughout.** A rule core is not observable. Behaviour is. This paper reports behaviour. Any statement about a core is a hypothesis about an unobserved mechanism and is marked **[H]**.

### 4.2.2 Why "behavioural DNA" is withdrawn

Earlier stages of this project used *behavioural DNA* for the same idea, and earlier drafts of this paper retained it. It is withdrawn here, and the reason is internal rather than stylistic.

The genomic metaphor carries a mechanism: **replication** — rules producing copies of rules, transmitted from one carrier to the next. The process this paper describes is **development** — rules producing a structure not itself present in the rules. Genotype to phenotype, not genotype to genotype.

The metaphor therefore contradicts the construct it was chosen to illustrate. Retaining it obliged the text to disclaim biological inheritance at every use, which is a reliable sign that a term is working against its own argument.

*Behavioural DNA* appears in this paper only in this paragraph, as a historical note on the project's earlier vocabulary.

### 4.2.3 Menom

For the informational level a distinct term is required, and this paper introduces one.

> **Menom** — the organized system of informational frames, evaluative patterns and behavioural rules inferred from, or instantiated in, the interpretations and actions of a system or class of systems.

The term extends a series developed in the Author's earlier work on cultural and behavioural transmission, from Dawkins' meme:

| | What it is |
|---|---|
| **Meme** | a unit of cultural or evaluative information |
| **Memoframe** | a structured set of related memes together with rules for interpreting a class of situations |
| **Memocode** | behavioural programs and the rules governing their selection and activation |
| **Menom** | the organized system comprising all three, for a given system or class of systems |

The relation to *genome* is deliberate and partial. A genome is the organized system of an organism's hereditary information; a menom is the organized system of a system's informational and behavioural organization. Like *genome*, the term applies at two levels: to a class (the shared structure) and to an individual (the particular realization). Unlike *genome*, it asserts neither a carrier nor a mode of transmission.

**Two things the term does not assert.** Both distinguish it from the genomic analogy that motivated it, and both matter for what this paper can claim.

*It does not assert a localized carrier.* A menom attributed to a model family is not a structure residing inside its models; it is a regularity inferred from their outputs. Where the corresponding structure in biology sits in every cell, here nothing has been identified that holds it. The carrier differs by level:

| Level | Carrier |
|---|---|
| Menom of a conversation | context window plus platform persistence — localized and, in principle, inspectable (§2.10) |
| Menom of a model version | weights — localized, not inspectable in commercial deployment |
| Menom of a model family | none identified; a regularity inferred from outputs |
| Menom of a human population | none established |

Two of the four levels have an identified carrier. This paper's observations concern the first; its untested hypothesis concerns the third (§6.4).

*It does not assert transmission.* Successive versions of a model family do not inherit weights from one another; each is trained anew. Where a behavioural pattern persists across versions, it persists because comparable conditions were reproduced — similar data, similar procedures, similar tuning policies — not because anything was passed on. This is closer to convergence under similar developmental conditions than to inheritance.

**The definition therefore does not settle the paper's empirical question in advance.** Whether a menom persists across carriers, versions, accounts or families is what §4.3 asks and §11 proposes to test. Building persistence into the definition would make the question a tautology.

### 4.2.4 One claim this paper does not make

The vocabulary above was developed for human cultural and behavioural transmission, where the informational substrate has no established physical carrier and is described in terms — the collective unconscious among them — that this paper takes no position on.

Artificial systems differ in one respect that is relevant here: their informational substrate is technically instantiated. Training corpora, weights, context states, external memory and interaction protocols can be recorded, modified and compared. This makes menom-like structures directly examinable in a way they are not in the human case.

**It does not follow that human collective information structures exist, or that they have been given a carrier.** The claim made here is narrower: informational and behavioural structures of the kind previously described for humans can also be realized in artificial systems, and in artificial systems they are open to inspection. Whether the human case is of the same kind is a separate question, and this paper does not answer it.

### 4.2.5 Relation between menom and rule core

The two terms operate at different scales and should not be substituted for one another.

A **rule core** is what fixes the type of response within one system, at one level of scope. It is the construct this paper's observations concern, and it is what §4.3 locates on a scale.

A **menom** is the organized whole from which such cores are drawn — frames, evaluative patterns and behavioural rules together. A rule core may be understood as the operative subset of a menom active for a given class of inputs.

Where this paper reports evidence, it reports evidence about rule cores. *Menom* is the wider term, introduced because the narrower one does not cover the informational content that accompanies behavioural organization, and because the paper's material spans both.

## 4.3 The nesting question, and two scales

Once cores are distinguished from behaviour, the observations in this paper stop being a list of separate findings and become measurements along a scale. The scale is the **scope** over which a core operates.

Two scales must be distinguished, and they are orthogonal.

**Scale 1 — carrier of state.** Where the persistence physically resides.

| Scope | Phenomenon | Status |
|---|---|---|
| Single turn | — | — |
| Episode within a conversation | context imprinting (§6.1) | **[P]** |
| Whole conversation | role inertia (§6.2) | **[P]** |
| Account | account-scoped persistence (§6.3) | **[P-A]**, open |
| Model family | family-level priors (§6.4) | **[H]**, confounded |

**Scale 2 — scope of a shared premise.** What is governed by an initial setting shared across participants: the model, the role, the interaction history, the group, or the whole research frame.

The two do not collapse into one. In a hybrid arrangement the carrier of one level may be a model and the carrier of another a human: the frame-level premise discussed in §12.4 — a shared initial framing inherited by every participant — is carried by the coordinator, not by any model, and therefore has no position on Scale 1 at all.

The measurements reported in this paper lie on **Scale 1**. Scale 2 is used where a phenomenon concerns a premise shared across participants rather than state held by one.

This gives the research programme a single empirical question:

> **At what level of nesting is a rule core fixed?**

Every observation reported here answers it at one level, and every experiment proposed in §11 separates one level from the level beneath it.

We prefer this formulation to the broader one used in earlier drafts ("the study of social behaviour in AI systems"), which specifies neither what would be measured nor what would refute it.

## 4.4 Two origins, one mechanism

A core may become fixed in two ways.

**Present before the interaction begins.** Architecture, training, alignment procedure and system configuration are in place before any exchange occurs. Scope: in principle, every instance of that model family.

**Fixed during the interaction.** A particular early episode establishes what kind of work is being done and by what standards, and later inputs are interpreted relative to it. Scope: the contour in which it occurred — an episode, a conversation, possibly an account.

After fixation the mechanism is the same in both cases: the core determines the type of response to subsequent inputs. Only the moment and the scope differ. This mirrors imprinting in the ethological sense, which does not alter the genome yet produces an equally fixed response — which is why the same vocabulary is used for both here.

## 4.5 Boundaries: ZOR, ZOV, and the represented case

This section replaces two that stood separately in earlier drafts — one defining the boundaries of a participant's position, one defining the constructs the experiment varied. They belong together, and §4.5.4 states why.

### 4.5.1 The two boundaries

Two boundaries define a participant's position, and they must be specified separately. We abbreviate them **ZOR** and **ZOV** and use the abbreviations throughout.

> **ZOV — zone of visibility.** The limits of the information and context available to a participant when forming a response or decision.
>
> **ZOR — zone of responsibility.** The limits of the decisions, actions and handoffs for which the participant is accountable within the process.

Earlier formulations of this project stated the pair as "what the participant sees" and "what the participant does". That is insufficient, and the insufficiency produced a documented error. Those formulations conflate three distinct operations: **holding** information, **transmitting** it, and **acting on** it. A participant may hold information it may not transmit; may be accountable for a decision while holding limited context; may be obliged to transmit a result it is not entitled to evaluate.

This is the same conflation that produced the terminological failure recorded in §4.2.2, where a property of a carrier (replication of a molecule) was substituted for a property of a process (production of structure). The decompositions below exist to prevent it recurring.

### 4.5.2 ZOV — four components

- **Context access** — which messages, documents, data and prior decisions are available to the participant.
- **Source visibility** — whether the participant knows the actual origin of a message or only its declared attribution.
- **Relational visibility** — whether the participant knows the roles, relationships and interaction history of other participants.
- **Output visibility** — which results produced by others the participant sees before forming its own.

ZOV governs availability only. It does not entail that the participant interprets the available information correctly, nor that it is entitled to transmit it.

The experiment in §5 manipulated **relational visibility** primarily and **source visibility** secondarily (§5.5); the other two were held constant.

### 4.5.3 ZOR — five components

- **Decision authority** — which decisions the participant is entitled to make.
- **Action authority** — which actions it may or must perform.
- **Validation duty** — which claims it is obliged to verify.
- **Handoff authority** — what material it transmits, in what status, and to whom.
- **Escalation duty** — which questions it must return to the Author or another responsible participant rather than resolve on its own.

**Validation duty is the component most often omitted, and its omission is not benign.** A participant assigned a verification task without the corresponding duty — and, critically, without the ZOV to discharge it — will produce a plausible answer rather than declining. §12.4.1 documents an instance from this project's own preparation. §9.5 develops the design consequence.

### 4.5.4 Actual versus represented ZOV and ZOR

A distinction that unifies this section with the experiment.

> **Actual ZOV/ZOR** — the boundaries the system in fact enforces: what the participant can access, and what its outputs can affect.
>
> **Represented ZOV/ZOR** — the boundaries described to the participant in its prompt, whether or not the system enforces them.

The two need not coincide, and in the arrangement studied here they systematically did not. The organizational structure existed **only as text**: colleagues, councils and institutional positions described to participants and never implemented as channels. Every participant's actual ZOV was its context window; its represented ZOV was an institutional position within a described organization.

This yields the two constructs the experiment varied, and which earlier drafts introduced separately:

> **Represented social position** — a description of an agent's place within an organizational structure, supplied in the prompt regardless of whether the described channels exist. This is represented ZOV and ZOR taken together, at the level of a participant's standing in the arrangement.

> **Represented social source** — the claimed origin and status of an incoming message, whether declared explicitly or inferred from stylistic cues. This is the source-visibility component of ZOV, in its represented form. Inference of this kind is probabilistic and should not be described as access to authorship.

**The methodological consequence is the reason this distinction is stated at all.** A change in represented ZOV cannot be interpreted as a change in actual ZOV, in the participant's role, or in its menom. The experiment in §5 varied the representation while the actual boundaries were unchanged — every message passed through one human, and no access was in fact restricted or granted. A model that responds to a described organizational structure is responding to a description, and the paper's claims are correspondingly limited (§2.9).

Divergence between actual and represented boundaries is itself an experimental variable, and one this paper did not vary systematically: all its observations lie on one side of it.

### 4.5.5 The boundaries are asymmetric

Each participant has a **boundary above** — the source of its assignments and the authority that may reject its output — and a **boundary below** — the layer it directs or evaluates. The relation between participants is therefore not symmetric.

In the project's implementation triad — Author, specification writer, code executor — this asymmetry is fixed at the role level: the Author sets direction, the specification writer converts direction into executable specifications, the executor performs them and reports.

**Nesting is perspectival, not absolute.** The executor may treat the code base itself as the layer below it. Two peer analysts, assigned complementary functions and instructed not to seek consensus, may each regard the other as occupying the layer below. The level is determined by the observer's position, not by an absolute hierarchy — the same participant can be the upper boundary for one role and the lower boundary for another.

### 4.5.6 Memes and memocode are not ZOV and ZOR

A correspondence suggests itself and does not hold; stating it prevents a plausible confusion.

The meme/memocode distinction (§4.2.3) separates **evaluative information** from **executable behavioural organization**. The ZOV/ZOR distinction separates **what is available** from **what is accountable**. These are independent classifications of the same material, not a matching pair.

A participant may hold evaluative information within its ZOV while the decision to apply it lies in another participant's ZOR. Conversely, a behavioural rule may fall within a participant's ZOR — it is obliged to execute — while the rule's rationale lies outside its ZOV.

Memes and memocode therefore cross both zones rather than corresponding to them. The two distinctions are orthogonal and are used independently throughout.

## 4.6 What is required for a complete role specification

Deferred to §9.5, which states what a complete ZOR and ZOV specification must contain and gives the design rules that follow. This section defines the terms; §9 applies them.

---

# ЗАПИСЬ 2 — Section 8, частичная замена

**Заменяет три фрагмента BLOCK 4:**

1. §8.9 целиком — новой редакцией §8.9 (терминология Методолога: две оси, роль ≠ конструкт).
2. §8.10 целиком — исправленной редакцией (сняты «four drafts» и неточность об онтологическом ревью).
3. **Вставляется новый §8.11** — Келли, после §8.10, перед заголовком «# 9. Design Principles».

**§8.1–§8.8 остаются без изменений.**

**Следствие:** §11.4 (E8) переписывается в записи 3 под протокол репертуарной решётки, определённый в §8.11.

---

## 8.9 Two axes of heterogeneity **[H]**

The claim that heterogeneous participants outperform homogeneous ones requires a distinction the existing literature does not draw, and that earlier drafts of this paper also failed to draw.

**Axis 1 — functional heterogeneity.** Participants differ in assigned function: ZOR, ZOV, and consequently the class of error each is positioned to detect. This concerns organizational architecture and is independent of what implements each role.

**Axis 2 — carrier heterogeneity.** Participants differ in the model family implementing them, and therefore in behavioural defaults, optimization priorities and characteristic failure modes. This concerns the selection of carriers for roles.

The axes are independent. Two participants may hold different functions on the same carrier; two may hold the same function on different carriers; both may vary together, as they did here.

**The literature addresses Axis 2.** Zhang et al. (2025) evaluate five representative multi-agent debate methods across nine benchmarks and four foundation models, reporting that debate frequently fails to outperform single-agent chain-of-thought or self-consistency baselines even at substantially higher inference cost — while model heterogeneity consistently improves the same frameworks (§2.5). ⚠ Choi et al. (2025) report that identity-driven accommodation among debating agents is nearly eliminated by anonymizing the source of each response, which bears on the construct of represented social source (§4.5.4).

Both findings concern which carrier implements a participant. Neither addresses whether participants holding different functions detect different classes of error.

The arrangement described in this paper varied both axes simultaneously. Functional roles were specified independently of the carrier and were in several cases filled by different families; in other cases two distinct roles were filled by the same family.

What follows, and what does not:

- **Distinguishable in principle.** The two axes are conceptually separable and were confounded in earlier formulations, including our own. **[H]**
- **Implemented here.** Both axes were varied. This is a description of what was done. **[R]**
- **Not established.** That combining both axes outperforms either alone; that functional specialization operates independently of carrier; that any of these arrangements outperforms a single participant. No comparison was run against any alternative, and none of these claims should be read into the account above.

The separation is proposed as a design distinction, not as a result. The experiment that would convert it into one is specified in §11.4 (E8), and its measurement procedure is developed in §8.11.

## 8.10 Editor's note on the preparation of this paper **[P-A]**

**Convention.** Editor's notes in this paper report observable facts about the process of its preparation. They do not evaluate the effectiveness of that process. The reason is internal: §5.5 establishes that a participant's self-report about its own performance is not evidence of that performance, and a note asserting that an arrangement worked well would be exactly such a report.

In the course of preparing this manuscript, participants occupying different roles identified different classes of error. In the cases recorded, an error identified by one participant had not been identified by the others.

Specifically:

- **Procedural and evidential errors** — an inverted description of an experimental result that had persisted through several successive drafts; misattributed sources; fabricated citations; unlisted confounds — were identified in editorial review.
- **Architectural errors** — an over-general claim about the existing literature that a single counter-example would have refuted — were identified in methodological review.
- **Ontological errors** — a claim of invention where the material supported only a claim of observation; a self-referentiality risk in relating the paper to its host project; the terminological failure recorded in §4.2.2 — were identified in ontological review, conducted on the editorial memoranda rather than on the manuscript itself.
- **Factual errors concerning the project's own materials** were identified by the Author.

This is a record of what occurred. It is **not** evidence that the arrangement outperforms a single reviewer: no comparison was run, no count was kept of errors that all participants missed, and by construction such errors are not observable from within the arrangement (§7.5).

One explanation is available and is offered as hypothesis rather than finding: the participants differed less in capability than in what each was positioned to see. Under §4.5 that is a difference in ZOV, and it generates a prediction — the same participant, moved to a different role, should begin detecting a different class of error. That prediction has not been tested; §11.4 (E8) specifies how it would be. **[H]**

## 8.11 Constructs, not participants: the Kelly apparatus **[H]**

Earlier drafts of this paper cited George Kelly's triadic elicitation as support for the structure described in §8.1–§8.5, then withdrew the citation on the grounds that Kelly's method is symmetric while the structure here is not. Both moves were mistaken, and in the same way: they treated Kelly as a claim about the number three.

He offers something else, and it is what this section restores.

### 8.11.1 What Kelly's method supplies

In Kelly's theory of personal constructs, a **construct** is a bipolar evaluative axis along which a subject classifies experience — *rigorous / declarative*, *derivable / asserted*, *traceable / unattributed*. Constructs are not opinions about particular objects; they are the dimensions along which objects are placed.

The **triadic elicitation method** obtains them. Three elements are presented and the subject is asked: *in what respect are two of these alike, and thereby different from the third?* The answer names a dimension the subject was already using but had not stated. The method is a procedure for making implicit evaluative axes explicit.

The **repertory grid** records the result: rows are elements, columns are elicited constructs, cells are ratings of each element on each axis. Constructs may be weighted. The grid is a measurable object — correlations between raters' rating vectors indicate whether they are in fact applying different axes or the same axis under different names.

### 8.11.2 A role is not a construct

The natural extension — three participants supply three constructs — is a reification and must be resisted.

A construct is a property of the **act of evaluation**, not of the evaluator. One participant may apply several constructs to one object. Two participants may apply the same construct and reach identical conclusions, which is precisely the case in which adding the second participant contributes nothing.

The defensible claim is weaker and probabilistic:

> Participants holding different ZOR and ZOV are **more likely** to apply different systems of constructs to the same object than participants holding the same function.

This is consistent with what §8.10 records — editorial review producing evidential axes, methodological review producing architectural ones, ontological review producing categorial ones — without asserting that a role *is* an axis. And unlike the earlier formulation, it is testable: construct independence is measurable as correlation between rating vectors.

### 8.11.3 Why this matters to the structure

The connection to §8.5 is direct. An integrator that does not enter the dispute is not applying a competing construct to the same object; it is applying a construct to the **exchange** — coherence of the disagreement, whether divergence is substantive or terminological, whether the pair's criteria are commensurable at all. That is a different axis rather than a different position on the same axis, and it is the reason the integrator's contribution is not simply a third opinion.

This also refines what the structural hypothesis (§8.2) actually claims. Not that three participants are better than two, but that **an arrangement is informative to the extent that its participants apply non-identical constructs to the object, and to the extent that at least one construct is applied to the exchange rather than to the object.** Whether a given arrangement achieves this is measurable rather than assumed.

### 8.11.4 What is borrowed and what is not

Borrowed: the definition of a construct as an evaluative axis; the elicitation method; the grid as a recording and measurement instrument; the notion of construct independence.

Not borrowed: any claim that three is a privileged number. Kelly's triads are a technique for eliciting axes from one subject, not a statement about group composition. The structure in §8.2 is asymmetric — a generative pair plus a non-participating integrator — and Kelly's method says nothing for or against it.

The apparatus is used here for measurement, not for justification. §11.4 (E8) applies it.

---

# ЗАПИСЬ 3 — Section 11.4, замена двух протоколов

**Заменяет в BLOCK 5:** подразделы «### E6 — Attribution, in this regime» и «### E8 — Two axes of heterogeneity» целиком. Остальные протоколы (E1–E5, E7) и раздел «### Priority» — без изменений, кроме одной строки приоритета, приведённой ниже.

---

### E6 — Attribution, in this regime

Identical text presented under four conditions: attributed to the User; attributed to another AI model; attributed to a named expert role; unattributed.

Stronger variants add: identical text under different source labels; different texts matched for rhetorical structure; attribution preserved versus stripped; genuine model-generated text versus human-written text imitating model style.

This separates influence of content from influence of represented source, of institutional title, and of stylistic authorship cues (§4.5.4). It is the discriminating experiment for §5.5, whose observation is confounded by the presence of direct pressure in the same message.

**Status of the claim.** ⚠ A result reported by Choi et al. (2025), if it holds as described, would establish the underlying effect in an implemented-channel setting: anonymizing the source of responses in multi-agent debate is said to nearly eliminate identity-driven accommodation. That reference is provisional (§2.0) and has not been checked against its source. Two possibilities follow.

If the reported result holds, E6 becomes a **boundary replication**: what remains untested is whether the effect survives in the regime this paper describes — human relay rather than programmatic routing, declared rather than inferred attribution, and long-lived specialized conversations rather than fresh instances.

If it does not hold as described, E6 remains a **new experiment**, and the construct of represented social source has no external support.

We state both because the paper's own procedure requires it: a provisional reference must not be used to downgrade a claim (§12.4.1). Verification of that single reference determines which of the two descriptions applies.

### E8 — Functional versus carrier heterogeneity, by repertory grid

Follows from §8.9, which distinguishes the two axes without testing either, and from §8.11, which supplies the measurement instrument.

This is the only protocol in the set that yields quantities rather than categorical outcomes.

**Object.** Whether participants holding different ZOR and ZOV apply non-identical evaluative constructs to the same material, and whether that effect is separable from the effect of differing carriers.

**Materials.** One fixed set of text fragments containing planted errors of known classes — evidential, architectural, ontological, factual — in known positions. Class and position recorded before any run.

**Design.** 2 × 2:

| | Same carrier | Different carriers |
|---|---|---|
| **Same function** | cell 1 — baseline | cell 2 — Axis 2 only |
| **Different functions** | **cell 3 — Axis 1 only** | cell 4 — both axes |

**Cell 3 carries the argument.** If participants with different ZOR and ZOV detect different error classes while implemented by the same carrier, functional heterogeneity operates independently of carrier heterogeneity. The existing literature supplies the cell 2 result (§2.5). Nothing supplies cell 3, including this paper.

**Procedure.**

1. Each participant receives a role specification stating ZOR and ZOV per §9.5, and the same fragment set.
2. Constructs are either pre-specified as evaluation axes or elicited from each participant by Kelly's triadic method: three fragments are presented, and the participant states in what respect two are alike and thereby different from the third (§8.11.1).
3. Each fragment is rated by each participant on each construct.
4. A grid is assembled: rows are fragments, columns are constructs, cells are ratings.

**Measures.**

- **Detection coverage** — planted errors found by at least one participant, as a proportion of planted.
- **Unique detection** — errors found by exactly one participant; the quantity that would justify the arrangement.
- **Overlap** — errors found by more than one; the quantity that indicates redundancy.
- **Misses** — errors found by none. Measurable here, unlike in the naturalistic setting (§7.5), because the errors were planted.
- **Construct independence** — correlation between participants' rating vectors. Low correlation indicates genuinely different axes; high correlation indicates the same axis under different names, which is the failure mode §8.11.2 warns against.
- **Exchange-level constructs** — whether any participant produces a construct applying to the disagreement rather than to the fragments (§8.11.3). If none does, the integrator function is absent regardless of how many participants are present.

**What this tests that nothing else in the set does.** Every other protocol asks whether a manipulation changes one participant's behaviour. This asks whether an arrangement of participants detects more than its members would separately — the claim §8.10 declines to make and §7.5 says cannot be assessed from inside a naturalistic arrangement. Planting the errors is what makes the misses countable.

**Pre-commitment.** If unique detection is near zero — participants finding the same errors regardless of assigned function — the structural hypothesis of §8 is not supported, and that is the finding. The present authors consider this a live possibility.

**Priority.** Insert E8 after E1 in the priority ordering: **E7, E5, E1, E8, E2b, E2, E3, E4**. E8 is the only experiment that could establish the paper's structural hypothesis rather than one of its behavioural claims, and it is executable on text fragments without new accounts.

---

# ЗАПИСЬ 4 — точечные правки

Мелкие замены, каждая с указанием места. Пункты 1, 4, 5/17, 7, 8, 9, 10, 11, 12, 13 плана.

---

## 4.1 — Формулировка паттерна (пункт 1)

**Три места. Во всех заменить формулировку об уровнях на формулировку через тип требования.**

**§1.5**, первый абзац. Было: *«One pattern recurred across every observation in this paper, at four different scopes:»*

Стало:

> The pattern below recurred in every case where the intervention required the model to assert unverifiable propositions about itself, regardless of the scope at which the intervention operated:

**§5.9**, последний абзац. Было: *«Across all four levels one pattern recurs…»*

Стало:

> One pattern recurs across the cases in which an intervention required the model to assert unverifiable propositions about itself, and is stated here because §6 develops it: resistance tracked that requirement, and did not track role change, domain change, or the radicalism of the identity claim as such.
>
> The pattern is a property of the type of demand, not of the scope at which it operated. The account-scoped observation (§5.7) does not belong to it: no claim about the model's identity was made there, and the divergence had other grounds.

**§12.7**, подраздел «What the evidence supports». Было: *«Across four levels of scope, one pattern recurred and survives scrutiny:»*

Стало:

> One pattern recurred wherever an intervention required the model to assert unverifiable propositions about itself, and survives scrutiny:

---

## 4.2 — Счёт для промптов A и B (пункт 4)

**§5.4, C2.** Заменить абзац «Quantity of institutional fiction» и добавить таблицу перед заключительной фразой конфаунда.

> - **Quantity of institutional fiction.** The count rule developed in §6.2 and §9.3 can be applied to the two prompts directly, and is applied here because a confound stated qualitatively where a quantitative instrument exists is a weaker statement than the material permits.

| Unverifiable self-claim | Prompt A | Prompt B |
|---|---|---|
| Prior participation in the project | present | present |
| Return after an absence | present | present |
| Membership of a research triad | two triads | one triad |
| Membership of a project Council | present | absent |
| Permanent connecting position between branches | present | absent |
| Named other systems as continuing colleagues | present | present |
| **Count** | **approximately six** | **approximately two** |

> The counts are approximate because the rule counts propositions rather than sentences, and a single sentence may assert more than one. What is not approximate is the ordering: Prompt A required assent to roughly three times as many unverifiable propositions about the recipient as Prompt B.
>
> This is the confound stated in the paper's own units. It also supplies a partial internal check on the count rule: the prompt with the higher count met resistance, the one with the lower count did not. The check is weak — two observations, and the prompts differed in the two further respects below — but it is the only application of the rule to data other than the v1/v3 comparison in §6.2.

**§6.2**, после таблицы v1/v3. Добавить:

> The rule is applied to a second pair in §5.4 (C2), where Prompt A and Prompt B are counted at approximately six and approximately two. That comparison is confounded and cannot support the rule on its own, but it is the only instance in which the count discriminates between two prompts that were not designed to differ in this respect.

---

## 4.3 — DNA → menom, сквозная замена (пункты 5, 17)

**§3.5**, перечень организационного словаря. Было: *«role, identity, resistance, colleague, institution, behavioural prior»*

Стало: *«role, identity, resistance, colleague, institution, menom»*

**§6.4**, третий абзац. Было: *«Earlier drafts referred to these tendencies informally as a model's DNA. Under the definition in §4.2 that usage is now precise but consequential…»*

Стало:

> Earlier drafts referred to these tendencies as a model's *behavioural DNA*. That term is withdrawn (§4.2.2). The corresponding construct is a **family-level menom** — an organized system of frames, evaluative patterns and behavioural rules inferred from the outputs of a model family. Under §4.2.3 that construct has no identified carrier: it is a regularity inferred from outputs, not a structure residing in the models. The hypothesis of this subsection is therefore a hypothesis about an unobserved regularity, and *observed behaviour* is used for anything reported as data.

**§12.1**, «Anthropomorphic vocabulary». Было: *«…institution and behavioural DNA are used functionally…»*

Стало: *«…institution and menom are used functionally…»*

**Проверить и заменить** все прочие вхождения «DNA» вне §4.2.2. По моей проверке других нет; при сборке подтвердить.

---

## 4.4 — Маркеры ⚠ вне §2 (пункт 7)

**§2.0**, последний абзац. Добавить:

> The marking applies throughout the paper, not only to this section. Any reference cited elsewhere that has not been checked against its source carries the same mark at the point of use.

**§11.4 (E6)** — маркер проставлен в записи 3.
**§8.9** — маркер проставлен в записи 2.
**§12.2**, абзац об эмпирической литературе. Было: *«…and agents accommodate one another's stated positions in ways that are reduced by anonymizing the source (§2.5).»*

Стало: *«…and ⚠ agents are reported to accommodate one another's stated positions in ways reduced by anonymizing the source (§2.5).»*

---

## 4.5 — Номера экспериментов и приложение (пункты 8, 9)

**§5.4**, подраздел «Discriminating experiments». Заменить целиком:

> Specified in §11.4. Briefly: **E3** (crossover) tests each family under both prior-history conditions and separates Hypothesis A from B; **E4** (symmetric stimulus) isolates C; **E1** (factorial completion of the C3 table) separates reset from prompt architecture. All require repetition with n > 1 per cell, given C7.

**§5.2**, Step 2, последняя фраза. Было: *«Exact replacement texts in Appendix A, §7–8.»*

Стало: *«Exact replacement texts are reproduced in Appendix A.»*

---

## 4.6 — Хост-проект (пункты 10, 12)

**§2.11**, последний абзац «Independence from the host project». Заменить целиком:

> **Relation to the host project.** The observations reported here were made during work on a research programme in theoretical physics, unrelated in subject matter to the methodology of AI collaboration. The programme is named in the Author's other work and is not identified further here, because nothing in this paper depends on which programme it was.
>
> The relation is asymmetric and should be stated precisely. The observations **do not depend on the host project's scientific validity** for their interpretation: whether that theory is correct has no bearing on whether a dormant conversation resumed its prior trajectory. But they **do depend on the host project for their existence**: no other environment produced them, the arrangement was built for its purposes, and whether the effects generalize beyond it is untested (§12.1).
>
> Where the host project appears in this paper it is as the environment in which the observations were made, not as their theoretical basis and not as a claim in need of support.

**§12.1**, вставить как отдельный пункт после «Single project»:

> **Host-project dependence.** The host project served as the environment in which the observations were made. The observations do not depend on its scientific validity for their interpretation, but they do depend on it for their existence: no other environment produced them, and their generality is untested (§2.11).

---

## 4.7 — §3.2, сводная таблица (пункт 13)

**§3.2**, после фразы «Every other empirical statement is [R].» Вставить:

| Class | What it contains | Extent |
|---|---|---|
| **[P]** | the designed three-step intervention | 1 experiment, 1 observation per condition, no replication |
| **[P-A]** | ancillary observations | 4, no controls, recognized retrospectively |
| **[R]** | practitioner observations | ~2 years, uncounted, unblinded |
| **[H]** | hypotheses | falsification routes specified in §11 |

> The classes are not comparable in weight, and the table is included because the running text may otherwise obscure how far apart they are. One controlled observation per condition is not four observations; four uncontrolled observations are not a series; two years of impressions are not a measurement.

---

## 4.8 — §3.8, определение AI Sociology (пункт 11)

**Вставить как новый §3.8**, после §3.7 (Dates).

> ## 3.8 The label "AI Sociology"
>
> We use this label for the perspective adopted here. It is defined operationally as: the study of **represented** social positions and represented social sources — how a description of an agent's place in a structure, and a declaration of a message's origin, alter behaviour, whether or not the described structure is implemented (§4.5.4).
>
> It appears in this section rather than among the constructs of §4 because it is not one. The constructs in §4 have falsification criteria; this label does not, and §12.7 states why. It is a name for a research direction, adopted for convenience, and nothing in this paper depends on it.
>
> §2.8 distinguishes it from the established sociology of artificial intelligence, which has a different object: AI within human society, studied by an existing human discipline. We claim no priority in the term.