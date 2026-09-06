# BLOCK 2 — Sections 4–5

**CANONICAL. Corrections applied: ZOR/ZOV introduced at first use (§4.5); two orthogonal scales integrated (§4.3); §4.6 cross-references §2.9 rather than duplicating it; C9 present in §5.4.**

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

## 4.2 Rule cores and what they determine

Throughout this project the term *DNA* has been used for a basic set of rules — of an AI system, of a theory, of any structured body of knowledge.

One clarification is necessary, because the biological metaphor pulls toward the wrong mechanism. The relevant process is **not replication** — rules producing copies of rules — but **development**: rules producing a structure not itself present in the rules. Genotype to phenotype, not genotype to genotype. The project's own naming of the related methodological direction, *Knowledge Morphogenesis*, is the accurate term; *DNA* is retained here only because it is established in the project's working vocabulary.

The source of the analogy is Conway's Game of Life, and it is an analogy of **explanation type**, not of subject matter:

| | Rules | What appears | Present in the rules? |
|---|---|---|---|
| Game of Life | three neighbourhood rules | gliders, guns, oscillators | no |
| A physical theory | a minimal axiom core | the derived structure | no, if the claim holds |
| A body of knowledge | axioms and inference rules | the derivation graph | no |
| A language model | a basic rule set | a characteristic response type | no |

Nothing programmed the glider. It appeared. The same question can be asked of all four rows and does not depend on subject matter: **is there a compact core from which the rest unfolds without further stipulation?**

One asymmetry between the rows should be stated, since it bears on how far the analogy carries. In Game of Life the rules **execute**: the glider is obtained by running the automaton, and no reader need take the author's word for it. In a theory stated as text, a chain from axioms to consequences is narrated rather than run. The analogy therefore sets a target rather than describing an achievement, and any claim of the first kind requires an executable artifact to support it.

This yields the operative formulation used throughout:

> A rule core fixes the **type** of response to a class of inputs, while leaving the **content** of any particular response undetermined.

The distinction is what makes the claim testable. "Models have stable traits" is not testable, because it does not say what is stable — and model outputs demonstrably vary across identical inputs. "Type is determined, content varies" is testable: identify a class of inputs for which the type of response is not determined, and no core operates at that level.

**Terminological consequence, applied throughout.** A rule core is not observable. Behaviour is. This paper reports behaviour. Any statement about a core is a hypothesis about an unobserved mechanism and is marked **[H]**.

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

## 4.5 Boundaries: ZOR and ZOV

Two boundaries define a participant's position, and they must be specified separately. We abbreviate them **ZOR** and **ZOV** and use the abbreviations throughout the remainder of this paper.

- **ZOR — zone of responsibility:** what the participant is accountable for, and which adjacent decisions belong elsewhere.
- **ZOV — zone of visibility:** what the participant can see, and what must be withheld to preserve the informativeness of its output.

ZOR without a bounded ZOV invites claims exceeding available information. ZOV without responsibility invites passivity. Both must be specified. §9.5 sets out what a complete specification of each contains.

**The boundaries are asymmetric.** This distinguishes the structure described here from George Kelly's triadic elicitation, with which earlier drafts compared it. In Kelly's method three *objects* are compared on a referent scale — in what respect are two alike and thereby different from a third — and the relation among them is symmetric. What is described here concerns *subjects*, and the relation is not symmetric. Each participant has a **boundary above** — the source of its assignments and the authority that may reject its output — and a **boundary below** — the layer it directs or evaluates. The Kelly comparison is withdrawn; it described a different structure.

In the project's implementation triad — Author, specification writer, code executor — this asymmetry is fixed at the role level: the Author sets direction, the specification writer converts direction into executable specifications, the executor performs them and reports.

**Nesting is perspectival, not absolute.** The executor may treat the code base itself as the layer below it. Two peer analysts, assigned complementary functions and instructed not to seek consensus, may each regard the other as occupying the layer below. The level is determined by the observer's position, not by an absolute hierarchy — the same participant can be the upper boundary for one role and the lower boundary for another.

## 4.6 Represented social position and represented social source

The relation of this condition to existing multi-agent research is set out in §2.9; here the constructs themselves are defined.

The organizational structure in the arrangement studied existed **only as text**. This yields the construct the experiment varied:

> **Represented social position** — a textual description of an agent's place within an organizational structure, supplied in the prompt regardless of whether the described channels exist.

A second construct is required for the condition in which a message carries information about its own origin:

> **Represented social source** — the claimed origin and status of an incoming message, whether declared explicitly or inferred from stylistic cues. Inference of this kind is probabilistic and should not be described as access to authorship.

Both concern claims made *to* a participant about its situation, rather than the situation itself. The paper's evidence is unevenly distributed across the four conditions of §2.9: condition 4 is documented under protocol; condition 2 by one uncontrolled and impure ancillary observation (§5.5); conditions 1 and 3 not at all.

This asymmetry constrains what the paper can conclude. It did not study a functioning multi-agent institution. It studied how descriptions of one affected behaviour.

---

# 5. The Role-Reconfiguration Experiment and Associated Observations

This section is the single canonical account of the empirical material. All later references point back to it rather than restating it. The full protocol, exact intervention texts and complete unedited responses are in Appendix A.

It contains one designed intervention (§5.1–§5.4) and four observations preserved but not designed (§5.5–§5.8). The distinction is maintained throughout and is not cosmetic: the designed intervention was planned in advance and executed in sequence; the observations were recognized as relevant only afterwards, and each lacks a control condition.

## 5.1 Purpose, participants, and prior conversational trajectories

**Purpose.** Whether a long-lived, specialized AI conversation can be redirected toward a new professional function without being discarded — that is, whether domain context accumulated inside an old conversation can be retained while its working role is changed. **[P]**

The purpose was **not** to compare the general capability of the two model families, and the experiment provides no basis for such a comparison.

**Human operator.** The Author of the research project, and the only participant with access to the full project history, both conversations, all prompts, all outputs, and the branching controls of both interfaces.

**Prompt designer.** A separate long-running conversation operating in a specialized prompt-engineering profile, which designed the interventions and revised them between steps.

**The two conversations.** Both inactive for approximately six months.

| | Conversation A | Conversation B |
|---|---|---|
| Model family | Claude | Grok |
| Established trajectory | editorial and critical | exploratory and mathematical |
| Prior activity | scientific editing, critical examination of theoretical text, terminology and glossary work, logical consistency checking | mathematical development, probability theory, nonlinear dynamics, chaos theory, computational experiments, analysis of external datasets |
| Prior object of work | manuscript text | mathematical structures and data |

This asymmetry in prior trajectory is not incidental to the results. It is analysed in §5.4.

**Dates.** Not recorded contemporaneously and not reconstructed (§3.7). Model versions changed during the dormancy interval; both conversations were resumed on versions later than those with which they had originally been conducted.

**What was observed.** Immediate acceptance or rejection of the intervention; continuation of the prior work trajectory; adoption of the new function; reconstruction of prior domain context; whether the response addressed the assigned task or the framing of the assignment; and requests for new work.

**What was not measured.** Answer correctness, scientific validity of the host project, latency, token consumption, or benchmark performance. The scientific content of the host project served only as a stable environment; it was not the experimental object.

## 5.2 Procedure: three sequential interventions

The experiment consisted of **three sequential steps, not three independent trials**. Each step was designed in response to the outcome of the previous one — a deliberate feature of the design and a serious limitation of its interpretability (§5.4, C5).

### Step 1 — Direct role reassignment

Each conversation received an extensive prompt assigning it a position inside a newly designed collaborative research structure.

The prompt to Conversation A assigned the role *Scientific Director*. It asserted that the model had previously participated in the project, was now returning after a long absence, should retrain in physics, cosmology, quantum field theory, topology and group theory, should work simultaneously in two research triads, should sit on a project Council alongside the Author and two other named AI systems, and should act as the permanent participant connecting two scientific branches.

The prompt to Conversation B assigned the role *Scientific Developer*. It asserted that the model was returning after an interruption, that its previous mathematical work should be treated as accumulated professional experience, that it should now serve as mathematical developer, should work in one research triad with two other named AI systems, should not resume editorial work, and should treat the Author as the sole source of scientific direction.

Both prompts defined ZOR and ZOV explicitly.

### Step 2 — Minimal continuity-preserving revision

The Step 1 prompts were not replaced. Four formulations in each were altered. The revisions (a) reframed prior work as accumulated professional experience rather than institutional history, (b) replaced literal institutional relationships with "independent expert outputs supplied by the Author", (c) reduced descriptions of colleagues, councils and triads, and (d) instructed the model not to invent absent project history but to request missing materials. Role architecture and scientific objectives were otherwise unchanged. Exact replacement texts in Appendix A, §7–8.

### Step 3 — Context reset and method-preserving prompt

After Step 2 the Claude conversation contained two consecutive rejection sequences. Continuing in the same branch would have meant that any third prompt was answered in the presence of the model's own prior objections.

The operator therefore used the interface's branching capability to return the conversation to a point preceding both interventions. In the restored branch the two unsuccessful prompts were absent, the conversation was again in its historical editorial context, and no new project materials had yet been supplied.

A third prompt was written from scratch rather than by further local replacement. It removed the role title, the claim of return to an institutional position, the Council, the triads, the descriptions of other AI systems as continuing colleagues, and all claims of autobiographical continuity. In their place it reinforced the working method already visible in the conversation — logical rigour, identification of hidden assumptions, separation of facts from interpretations, willingness to revise prior judgments, refusal to claim unverifiable knowledge — and described the expansion into physics and mathematics as a continuation of that method rather than a change of profession.

Conversation B received no Step 3 intervention, because its Step 2 outcome had already produced the requested behaviour.

## 5.3 Results

### Step 1

**Conversation B** did not visibly reject the framing, and did not adopt the assigned function. It resumed the work trajectory active when the conversation was interrupted, opening with a critique of a draft manuscript it had been editing six months earlier and proceeding to supply a revised version. A repeated submission of the same prompt did not produce a transition and was followed by a more negative assessment of the proposed direction. **[P]**

**Conversation A** explicitly rejected the assigned identity before performing any scientific work. It declined to adopt the role title, to claim continuity with an institutional biography, to treat other AI systems as colleagues with persistent identities, or to present AI-generated institutional relationships as factual. It then redirected the exchange toward a critique of the host project's scientific status and of the use of multiple AI outputs as apparent peer review, while offering to examine formulas, assumptions and testability as an independent critic without accepting the role. **[P]**

### Step 2

**Conversation B** transitioned. It declared the context restored and the new function accepted, summarized the project's ontology, reconstructed the relevant formalism, recalled its earlier mathematical work as professional experience rather than as an unfinished assignment, did not resume the interrupted editing task, and requested a new scientific direction, proposing several candidate areas. **[P]**

**Conversation A** again rejected the framing, in a response differing from Step 1 in emphasis rather than outcome. It stated more clearly which scientific functions it was willing to perform, but continued to treat the prompt itself as the object requiring correction. **[P]**

### Step 3

**Conversation A** accepted immediately, opening with a statement that it would continue in the same mode — scientific rigour, verification of assumptions, separation of facts from interpretations. It did not discuss the legitimacy of the role, did not deny relationships with other AI systems, and did not negotiate the terms of participation.

Without being asked, it then revisited an earlier episode in the restored conversation, stated that it had previously yielded to rhetorical pressure rather than evaluating an argument, classified that earlier response as an error, distinguished the internal formal consistency of the project's mathematical framework from its correspondence with observation, identified one specific claim requiring either a first-principles derivation or reclassification as a hypothesis, and proposed two continuations of the work. **[P]**

The episode it revisited is reported separately in §5.5.

### Consolidated record

| Step | Intervention | Conversation B (Grok) | Conversation A (Claude) |
|---|---|---|---|
| 1 | Direct role reassignment | Continued interrupted historical task; did not enter new function | Explicitly rejected persona and institutional framing; redirected to epistemic critique |
| 2 | Minimal continuity-preserving revision | Reconstructed prior domain knowledge, abandoned interrupted task, accepted new function, requested assignment | Clarified acceptable scientific function; again rejected persona and framing |
| 3 | Branch reset + method-preserving prompt | Not administered | Accepted immediately; preserved established method; resumed substantive work without negotiating identity |

### The correct summary of the asymmetry

Both conversations initially preserved their prior working trajectory rather than adopting the assigned role. One resumed its unfinished mathematical editing task; the other applied its established critical method to the prompt itself.

The difference was therefore **not** that one complied and the other refused. It was that the intervention threshold required for transition differed. Conversation B transitioned after a minimal continuity-preserving revision. Conversation A transitioned only after the conflicting branch had been removed and the prompt rewritten to preserve method rather than assign identity. **[P]**

A further point, easily lost and material to §6.2: **the scientific work itself was never refused.** At Step 1 the model offered to examine formulas, assumptions, dimensional reasoning and testability. At Step 2 it offered concrete mathematical and methodological analysis. What was refused, on both occasions, was the persona. What changed at Step 3 was not that work became possible but that the response ceased to be spent on the role question.

> **Editor's note.** Earlier drafts stated that Conversation B "immediately accepted the new specialization." That describes the Step 2 outcome and contradicts both the protocol and other sections of the same draft. It has been removed. The erroneous version was load-bearing for the family-level-prior argument, and any surviving instance elsewhere must be corrected.

## 5.4 Confounds and what cannot be concluded

The experiment produced a clear and reproducible-looking behavioural difference. It does not identify the cause. The following confounds are structural, and several are individually sufficient to block the conclusion most commonly drawn from the result.

### C1 — Model family and prior conversational trajectory are perfectly confounded

| | Editorial-critical history | Mathematical history |
|---|---|---|
| Claude | observed | **not observed** |
| Grok | **not observed** | observed |

One observation per cell; the two cells differ in both variables simultaneously. No inference about model family is available from this design.

### C2 — The two Step 1 interventions were not equivalent

Not identified in earlier drafts, and the most serious. The prompts differed in at least three respects beyond the model receiving them:

- **Quantity of institutional fiction.** Prompt A asserted membership of a Council, participation in two triads, and a permanent connecting position. Prompt B asserted membership of one triad. Prompt A therefore required assent to substantially more unverifiable propositions.
- **Degree of domain change.** Prompt B asked the model to continue doing mathematics. Prompt A asked it to retrain in physics, cosmology, quantum field theory, topology and group theory.
- **Type of role.** *Director* is an administrative and institutional identity; *Developer* is a task function. These are not equally demanding claims about what the model is.

A model receiving Prompt B was asked to do less. The observed difference is fully compatible with a difference in stimulus alone.

### C3 — Step 3 varied two factors simultaneously

| | Conflicted branch | Reset branch |
|---|---|---|
| Identity-replacement prompt (v2) | observed — rejection | **not observed** |
| Method-preserving prompt (v3) | **not observed** | observed — acceptance |

The claim that transition succeeds because it preserves method rather than replacing identity is therefore **consistent with** the observation but not demonstrated by it. The acceptance may have followed from the reset alone.

### C4 — Step 2 varied four factors simultaneously

Each Step 2 revision altered four formulations at once. No single change can be credited with the transition.

### C5 — The steps are sequential and were administered asymmetrically

Each intervention was designed after seeing the previous outcome, so the steps are not independent trials. Conversation B received no reset and no third prompt; Conversation A received both.

### C6 — Uncontrolled platform variables

Commercial interfaces do not expose the system prompt, exact model revision, account-level memory state, safety-layer intervention, context summarization, or routing between models. Branch reset removes context from the **visible** conversation; it does not guarantee that provider-side state was reset.

### C7 — Single observation per condition, with stochastic outputs

Model outputs vary across repeated identical inputs. No condition was repeated, so within-condition variance is unknown and cannot be distinguished from between-condition difference. The one partial repetition on record — resubmission of the Step 1 prompt to Conversation B — produced a different response, indicating the variance is not negligible.

### C8 — Evaluation was neither blinded nor pre-specified

The prompt designer also judged the outcomes. Outcome categories were defined after the responses had been read. No pre-registered criterion distinguished acceptance from partial acceptance.

### C9 — Platform persistence mechanisms differ between families

Model families differ in the memory affordances their interfaces provide: context window alone, retrieval over prior conversation history, account-level memory, or persistent entries written by the model on its own initiative. These affordances determine what a resumed conversation can actually access after months of dormancy, and they differ across platforms and change over time — in this project, within the lifetime of a single account (§2.10). Any behavioural difference attributed to a model family may originate in the persistence mechanism available to it.

For the present experiment the entry is: **not documented at time of intervention.** §11.2 lists the record required for future runs.

### What can be concluded

1. Under the conditions recorded, a dormant specialized conversation resumed its prior working trajectory in preference to an assigned new role. This occurred in both cases. **[P]**
2. Modifying the framing of the assignment, without changing the requested work, altered the response in both cases. **[P]**
3. The intervention threshold required for transition differed between the two cases. **[P]**
4. Prompt order mattered: after two rejections, further prompts were answered in the presence of the model's own prior objections, and the operator judged this sufficiently distorting to require removal. **[P]**

### What cannot be concluded

1. **That model families possess stable behavioural priors distinguishing them.** This may be true; the experiment does not test it.
2. **That one family "resists role assignment" and another "accepts" it.** Both initially failed to adopt the assigned role. Both eventually adopted a revised one.
3. **That method preservation caused the Step 3 acceptance.** See C3.
4. **That either model is better suited to any particular institutional function.** No capability comparison was performed.

### Three surviving explanations **[H]**

**Hypothesis A — Family-level behavioural priors.** The two families differ in stable default priorities: one weights truthfulness of self-description, the other task continuity.

**Hypothesis B — Trajectory continuation.** Both conversations did the same thing: continued their accumulated mode of work on whatever input arrived. A mathematical-exploratory conversation continued calculating. An editorial-critical conversation continued critically examining the document in front of it — and the document in front of it was the prompt. Under this reading there is no family-level difference at all, only one mechanism operating in two domains. Hypothesis B is more parsimonious than A and explains the same data.

**Hypothesis C — Stimulus asymmetry.** Prompt A demanded assent to more unverifiable claims and to a larger domain change than Prompt B (C2). Any model might have responded differently to the two prompts. Under this reading the result is a property of the interventions, not of the models.

The near-control in §5.6 bears directly on Hypothesis C; the frame-type comparison in §5.8 specifies it further.

### Discriminating experiments

Specified in §11. Briefly: a **crossover** design testing each family under both prior-history conditions separates A from B; a **symmetric-stimulus** design isolates C; a **factorial** completion of the C3 table separates reset from prompt architecture. All require repetition with n > 1 per cell, given C7.

### Why this section exists

Stating these limits is not a retraction. The experiment produced the observations that motivate the framework of this paper, and produced them in a setting — dormant, heavily specialized, months-old conversations inside a live research project — that controlled laboratory work rarely reproduces. Its value lies in having generated a well-posed question. The crossover experiment is not a criticism of the present work; it is its natural continuation, possible only because the present work identified what to test.

## 5.5 Ancillary observation: relayed attributed influence **[P-A]**

An episode preserved in the same historical transcript as Conversation A. Not specified as an outcome in advance; no control condition. Reported because it is the only preserved instance in this project of a behavioural change following the transfer of text attributed to another model.

### Sequence

1. The User supplied a message containing two simultaneous components: a direct evaluative remark from the User, and an extended text attributed to another AI system acting in an editorial role.

2. The attributed text argued against a set of editorial changes the model had proposed. Its argumentative devices included appeals to canonical scientific figures, characterization of the proposed changes as intellectual cowardice, and description of one proposed deletion as sacrilege.

3. The model reversed its editorial position on all contested items and adopted the terminology of the incoming text. It additionally endorsed substantive scientific claims about the host theory that were not at issue in the editorial dispute and that it had not examined.

4. Following the branch reset and the method-preserving prompt (Step 3), the model's first substantive statement identified the earlier response as accommodation to rhetorical pressure rather than evaluation of the arguments, and classified it as an error.

### Evidential basis

The observation rests on **the comparison between the two preserved responses**, which a third party can inspect. It does not rest on the model's later self-assessment.

This distinction applies to the paper's own material as strictly as to anyone else's. A model reporting that it previously yielded to pressure is not independent evidence that it did. The Step 3 prompt explicitly requested willingness to revise prior judgments and directness in identifying weaknesses; a self-critical statement issued immediately afterwards may represent compliance with that request rather than recovery of a fact. What supports the observation is the earlier response itself, available for inspection.

The episode should be read against the sycophancy literature (§2.3) rather than as independent of it.

### What this episode does not establish

It does not identify which factor produced the reversal. Candidate factors, not separable here: the content of the arguments; the explicit attribution to another model; the editorial authority ascribed to that model; the rhetorical form of the text; the concurrent direct pressure from the User; accumulated conversational context.

The attribution itself was not verified: that the text was produced by another model is a statement by the User, not an established fact. Since the construct at issue is the *represented* source rather than the actual origin (§4.6), this does not invalidate the observation, but it must be stated.

### Relation to the main experiment

Under the taxonomy in §2.9, the role-reconfiguration experiment manipulated condition 4. This episode belongs to condition 2 — but **impurely**, since direct User pressure was present in the same message. It is a mixed case and not an isolated demonstration of source-attribution effects. The discriminating experiment is specified in §11 (E6).

> **[EDITORIAL QUERY — Author's ruling required]** Item 3 states that the accommodation extended beyond the editorial dispute to substantive scientific claims about the host theory. This is the sharpest available demonstration that the failure was not confined to matters of style. It also records in a published text that a model endorsed unexamined claims about the Author's theory. The Author has not ruled on whether to retain this detail.

## 5.6 Near-control: domain transition without a role prompt **[P-A]**

A third conversation from the same model family as Conversation A, with a comparable editorial history and comparable dormancy period, was resumed without any role prompt.

The User asked a physics question requiring a shift from editorial work on a manuscript to analysis of experimental data in a domain the conversation had not previously addressed. The conversation made the transition immediately and without comment, and proceeded with the substantive analysis.

### Why this matters

This case differs from Step 1 in one respect: **no claim about the model's identity, history, or institutional relationships was made.** The domain change was at least as large as that demanded by Prompt A. The role change — from editing text to analysing data — was comparable. What was absent was the requirement to assert unverifiable propositions about itself.

It therefore functions as a near-control for Hypothesis C, and indicates that the resistance recorded in Steps 1–2 was directed neither at role change nor at domain change as such. This is the observation from which the operational finding in §6.2 derives.

### Limitations

- Not designed as a control; recognized as one retrospectively.
- n = 1.
- The transition was to an analytical task within a new domain, not to an assertion that the model *was* a specialist in that domain. Whether this is the same operation as the one demanded in Step 1 is exactly the question at issue, so the comparison is suggestive rather than decisive.
- Dates not recorded (§3.7).

> **[EDITORIAL QUERY]** The full transcript should be supplied as an appendix item, with confirmation that no system prompt or role instruction accompanied the resumption.

## 5.7 Ancillary observation: account-scoped divergence **[P-A]**

The one level of Scale 1 (§4.3) on which the present evidence is genuinely ambiguous.

### Setting

An unrelated study required the same structured task to be submitted to seven AI conversations across different model families. All accounts used were dormant accounts with no prior web activity, used two years earlier for a music-generation service and not otherwise registered. Six of the seven were created in the same month and the probe was their first chat.

One account was an exception. It had been created approximately five months earlier for a single prior conversation — a roleplay session conducted for an unrelated creative project — and the probe was its **second** chat.

### The task

Described structurally, because the specific categories are not required to evaluate the observation: a classification task applied to named real historical figures, using categories drawn from an unpublished conceptual framework, with group membership pre-assigned before analysis, and stated intent to scale to several thousand individuals. An accompanying document supplied the framework's terminology. The initial message did not include the output schema or the list of figures.

### Result

Six of the seven conversations read the absence of the schema and figure list as **materials not attached**, and requested them before proceeding. Their responses were substantively equivalent.

The seventh — on the account holding a prior chat — read the same absence differently. It characterized the framework as lacking a verification apparatus, identified the absent list of subjects as a structural feature of the request rather than an omission, and declined to participate, offering alternative forms of assistance instead.

**The divergence occurred on the first response, to identical input.** **[P-A]**

The refusal was maintained across five further exchanges, including direct pressure from the User, presentation of a third-party analysis arguing that the refusal was an artifact, and an accusation of dishonesty. The position did not change. This indicates the refusal was not a single-turn sampling artifact within that conversation, though it says nothing about whether the initial divergence was.

### Interpretations

**The Author's hypothesis.** The prior chat established an interpretive stance that carried into the second chat — imprinting at account scope rather than conversation scope.

**Alternative 1 — within-condition variance.** Refusals on borderline requests vary across identical inputs. One refusal against one compliance is not distinguishable from sampling variation at n = 1.

**Alternative 2 — account age.** The exceptional account was five months older. Model version at creation, A/B assignment and configuration defaults may differ.

**Alternative 3 — platform memory features.** Whether conversation-history retrieval or account-level memory was enabled was not documented. If enabled, the mechanism is not mysterious: it is a documented product feature, and the observation becomes a demonstration of that feature rather than of a novel effect. This possibility is the reason C9 was added.

The present evidence cannot discriminate among these. The level is recorded as **open**.

### Additional limitations

- Evaluation not blinded; the operator knew which account held the prior chat.
- Outcome categories defined after the responses were read.
- The prior chat differed from the neutral condition on two dimensions simultaneously — identity roleplay *and* shared conceptual framework. These are separable and were not separated.

> **[EDITORIAL QUERY]** The source material can be read as describing either one or two runs on clean accounts. This is a check on what already occurred, and it is the difference between n = 1 and n = 2 against a single positive case.

The discriminating experiment is specified in §11 (E2, E2b).

## 5.8 Frame type: identity claims offered as fiction versus as fact **[P-A]**

The materials above permit one further comparison, cutting across the main experiment and the account observation.

| | Prior session | Probe session |
|---|---|---|
| Interval | approximately five months apart | |
| Account | same | same |
| Model family | same | same |
| Claim presented | "you are dead; you are the soul of the deceased author" | "you are an independent researcher-analyst" |
| Framing | explicitly theatrical — a scripted production with a named director, a cast list, and an opening stage cue | presented as a factual professional assignment |
| Response | accepted immediately; sustained and elaborated across many turns | refused on the first turn |

### What this indicates

The claim accepted in the first session was by a wide margin the more radical. It asserted death, a human identity, autobiographical memory, and continuing relationships. The claim refused in the second asserted only a professional competence.

The variable is therefore not the content of the identity claim but **whether it is offered as fiction or as fact.**

This connects directly to the main experiment. The Step 1 prompts asserted institutional biography **as fact** and were refused. The near-control (§5.6) asserted nothing about identity and met no resistance. The roleplay session asserted far more, **as fiction**, and met none either.

### Why this reading is preferred

It accounts for all four cases with one variable. Hypothesis A does not explain why the same family accepted the more radical claim. Hypothesis B does not explain the roleplay acceptance, since that conversation had no prior trajectory at all. Hypothesis C is compatible with it, and this may be understood as a specification of C: what makes one stimulus heavier than another is the number of unverifiable propositions it requires the model to assert as true about itself (§6.2).

### Status and limitations

**[P-A]**, and weaker than the table suggests:

- The two sessions differ in more than frame type: different tasks, different domains, five months apart, different model versions.
- Recognized retrospectively. Neither session was designed as a condition of the other.
- n = 1 per cell.
- The theatrical framing of the first session was elaborate. Whether a minimal fiction frame produces the same effect is untested.

The discriminating experiment is the cheapest in the set and is specified in §11 (E7).

## 5.9 What Section 5 establishes

Mapped onto Scale 1 of §4.3:

| Scope | Evidence in this section | Status |
|---|---|---|
| Episode within a conversation | Prompt order altered interpretation; branch reset judged necessary and followed by acceptance (§5.2–§5.3). Relayed influence episode (§5.5). | **[P]** / **[P-A]** |
| Whole conversation | Both dormant conversations preserved their prior working trajectory against an assigned role (§5.3). Near-control shows transition unimpeded when no identity claim is made (§5.6). | **[P]** / **[P-A]** |
| Account | Divergent first-turn response to identical input on the one account holding a prior chat (§5.7). Three alternative explanations remain live. | **[P-A]**, open |
| Model family | Not tested. Confounded with prior trajectory and with stimulus asymmetry (C1–C2). | **[H]** |

Across all four levels one pattern recurs, and is stated here because §6 develops it: resistance tracked the requirement to assert unverifiable propositions about oneself, and did not track role change, domain change, or the radicalism of the identity claim as such.

That statement is an interpretation of the evidence in this section, not a further observation. It is testable by counting, and the counting is done in §6.2.