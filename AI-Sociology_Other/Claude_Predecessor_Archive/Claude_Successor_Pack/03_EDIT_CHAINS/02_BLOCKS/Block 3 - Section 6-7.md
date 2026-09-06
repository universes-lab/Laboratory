# BLOCK 3 — Sections 6–7

**CANONICAL.** Cross-references aligned to Blocks 1–2. §6.1–§6.4 are ordered along Scale 1 of §4.3 (carrier of state).

---

# 6. Derived Concepts

Each concept below is a claim about the scope over which a rule core operates. They are presented in order of increasing scope along Scale 1 of §4.3.

## 6.1 Context imprinting — episode scope **[P]**

*Context imprinting* is the persistence of an interpretive stance established by a specific episode of conversational history.

It differs from memory in the ordinary sense. The model need not reproduce earlier content. What persists is a pattern of interpretation induced by a prior exchange.

In the experiment (§5.2), after the first prompt had been read as making false claims about the model, subsequent revisions were no longer evaluated in a neutral context. They were interpreted through the objection already established. Improved formulations inherited part of the earlier conflict.

**Consequence for method.** Prompt engineering frequently treats instructions as additive — a weak instruction can be corrected by a stronger one. In long-lived conversations this is unreliable. A prompt does not enter an empty context; it enters a context with momentum. Two identical prompts may therefore produce different results at different points in the same conversation, which makes **prompt order an experimental variable**.

**Relation to existing work.** Sensitivity to the ordering of in-context material is documented (§2.3). Context imprinting is a stronger form of the same family: not sensitivity to the arrangement of examples, but persistence of an interpretive stance established by a single conflictual episode, surviving complete replacement of the instruction that follows it. Whether this is a distinct phenomenon or an extreme case of the documented one is open, and we do not claim to have settled it.

The corresponding procedure — returning a conversation to a point preceding a conflict, to separate the effect of a new prompt from the effect of the model's own prior objections — is described in §5.2 and §10.5 and is, in our view, the most directly reusable contribution of this paper.

## 6.2 Role inertia — conversation scope **[P]**

*Role inertia* is the tendency of a long-lived conversation to continue its established working trajectory in preference to an assigned new function.

Both conversations in the experiment displayed it. One resumed an unfinished editing task; the other applied its established critical method to the prompt itself. The distinction from context imprinting is that role inertia concerns the *trajectory* of work, while imprinting concerns the interpretive effect of a *specific episode*. Both may operate simultaneously.

Role inertia is adjacent to, but not identical with, persona drift. Drift is the gradual erosion of an assigned role under contextual pressure. Role inertia is resistance to an *explicit directive replacement* while the prior trajectory is maintained.

### The operational finding

The sharpest result of the experiment is not that transition succeeded when method was preserved. That formulation is confounded (§5.4, C3). What the combined evidence supports is narrower and more useful:

> **Role transition fails in proportion to the number of unverifiable claims about the agent that the prompt requires it to accept.**

Counting these in the prompts actually used:

| | Prompt v1 | Prompt v3 |
|---|---|---|
| Claims about the agent's past | present | none |
| Claims about relationships with other agents | present | none |
| Institutional title | present | none |
| Unverifiable propositions requiring assent | approximately six | zero |
| Description of working method | absent | itemized, all observable in the prior conversation |

A near-control supports this reading (§5.6): a comparable conversation, comparably dormant, made an equivalent domain transition **with no role prompt at all** — the Author simply asked a question in the new domain. No claim about the model's identity was made, and no resistance occurred.

The frame-type comparison (§5.8) extends it in the opposite direction: a far more radical identity claim, offered as fiction, was accepted at once. What a fiction frame does, under this reading, is remove the requirement to assert the claim *as true*, which reduces the count to zero by a different route.

Taken together, this indicates that resistance was directed neither at role change nor at domain change, but at the requirement to assert unverifiable propositions about oneself.

### Connection to the framework

A role prompt attempts to install a rule core (§4.2). Each unverifiable self-claim is a proposition that must be accepted for the installation to proceed. The count is therefore a measure of **the cost of installing a core**, and this is what connects the operational rule to the theoretical construct rather than leaving them as two separate observations.

**The rule is testable by counting**, which is why we prefer it to the earlier formulation. §9.3 specifies what counts; §11.4 (E5) specifies the experiment that would falsify it.

## 6.3 Account-scoped persistence — account scope **[P-A]**, unresolved

Whether a core can be fixed at the level of an account rather than a conversation is the one level of Scale 1 on which the present evidence is genuinely ambiguous.

The observation is reported in §5.7. Its interpretation depends on platform features whose state was not documented at the time and which vary between vendors and over time (§2.10): context window alone, retrieval over prior conversation history, account-level memory, or persistent entries written by the model on its own initiative. These affordances determine what a resumed conversation can access.

Three alternative explanations remain live: within-condition variance at n = 1; account age; and enabled platform memory features, under which the mechanism would be a documented product feature rather than a novel effect.

We therefore record this level as **open**. The observation is preserved; the mechanism is not established; the discriminating tests are specified in §11 (E2, E2b).

## 6.4 Family-level priors — family scope **[H]**

The proposition that model families differ in stable behavioural priors is the hypothesis this project began with and the one its evidence supports least.

The experiment cannot test it: model family and prior conversational trajectory were perfectly confounded, with one observation per cell, under non-equivalent stimuli (§5.4, C1–C2). Two incompatible readings remain available and the data cannot discriminate between them.

Earlier drafts referred to these tendencies informally as a model's *DNA*. Under the definition in §4.2 that usage is now precise but consequential: a rule core is unobservable, so the claim concerns a mechanism we have not measured. We retain the term for the hypothesis and use *observed behaviour* for anything reported as data.

One recorded episode cuts against the schema earlier drafts built on this hypothesis. In an unrelated multi-model session, the model characterized as most compliant with assigned roles removed an assigned persona mid-session and reclassified it as an attempted reprogramming, under a deliberately soft framing that permitted improvisation. The schema "one family accepts roles, another resists" does not survive this. **[P-A]**

We regard elimination of this level by the crossover experiment (§11, E3) as a reasonably likely outcome and would not consider it a failure of the programme.

## 6.5 Intervention attaches at the level where the core is fixed

The concepts above converge on a single practical consequence.

> An intervention succeeds when it attaches to the level at which the core is already fixed, and fails when it attempts to overwrite that level by declaration.

- The successful third intervention did not assert a new identity. It reinforced a working method already visible in the conversation — attaching at conversation scope, where role inertia operates.
- The branch reset did not modify the prompt. It removed a specific episode — operating at episode scope, where context imprinting operates.
- The document described in §4.1 did not extend the instruction list. It redefined the agent's function and required the agent to restate it in its own operational language.

This also reframes what earlier drafts called *transition through adjacent competence*. The successful prompt described expansion into physics and mathematics as a continuation of existing critical work rather than a change of profession. Under the present framework this is not a separate principle but the same one: the new function was attached to the established core rather than proposed as a replacement for it.

**Corresponding design rule, developed in §9.1:** identify the level at which the relevant core is fixed before drafting the intervention, and attach to it.

## 6.6 What would refute this framework

The framework predicts that the type of response to a defined class of inputs is determined at some identifiable level of nesting, while content varies.

It would be substantially weakened by any of the following:

- A class of inputs for which the type of response is not determined at any level — no core, only variance.
- Demonstration that the observed differences are fully accounted for by within-condition variance under repetition.
- Demonstration that the crossover design (§11, E3) shows behaviour following prior trajectory alone, with no family-level component — which would eliminate the top level of Scale 1.
- Demonstration that the account level does not exist as a distinct scope, collapsing §6.3 into §6.2.
- Failure of the count rule to produce a monotonic effect under E5, which would remove the paper's only quantitative claim.

We regard the third and fourth as reasonably likely, and would not consider either a failure. Locating the scale's actual bounds is the point of the programme, not a threat to it.

---

# 7. Retrospective Practitioner Observations

## 7.1 How this section should be read

Everything here is **[R]**. It records patterns the participants believe recurred during approximately two years of daily work on a live research project. None of it was recorded under protocol, counted, timed, blinded, or compared against a control condition. The people who noticed each pattern were the same people who had designed the change that produced it, and who wanted it to work.

The known failure modes of this class are set out in §3.3 and apply to every paragraph below. They are not repeated at each item. Readers should treat this section as a field report from one team — closer in evidential weight to an engineering practice note than to measurement.

Quantitative language has been removed throughout. Where the original working notes recorded that something improved "significantly" or "substantially," no measurement existed, and the wording now reflects that.

The section is included because these observations motivated the framework in §4 and the design rules in §9, and suppressing them would misrepresent how the work actually proceeded.

## 7.2 Specialization displaced capability as the operative variable

At the outset the participating models behaved similarly. Each attempted whatever was presented to it, and the differences between them were read as differences in intelligence or writing quality.

That reading gradually became less useful. The question that produced better outcomes was not *which model is strongest* but *which function does this conversation already perform well*.

As particular conversations acquired persistent working identities, the participants report that behaviour became more predictable across sessions: a conversation used consistently for editorial work continued to behave editorially; one used for mathematical exploration continued to explore; one responsible for terminology resisted semantic drift without being reminded to.

The underlying models did not change during these periods. What changed was the consistency with which each conversation was used for one kind of work.

This is the observation from which §6.2 was later derived, and should be read as its retrospective, unmeasured precursor rather than as independent support for it.

## 7.3 Context behaved more like attention than like memory

The intuitive expectation is that more context improves reasoning. The participants' experience ran the other way often enough to change practice.

Supplying a specialist with the full project context frequently produced worse results for that specialist's own function: responsibilities blurred, participants attempted problems outside their competence, and the value of independent examination declined because everyone was working from the same picture.

Restricting what a participant could see frequently produced more usable output.

Two qualifications. First, this is not a novel finding: positional and order effects in long contexts are documented (§2.3), and the principle of least privilege expresses the same intuition for access rather than knowledge (§2.6). Second, the project never distinguished between two quite different explanations — that additional context degrades reasoning, or that additional context simply invites the model to answer a broader question than the one asked. The second is more parsimonious and was never tested against the first.

What survives is the practical rule, not the mechanism: the design question is not only how much a role can be given, but what it should not be given (§9.6).

## 7.4 Capability and scope expansion

The participants repeatedly observed that more capable models were more inclined to exceed their assigned function: expanding project scope, proposing alternative architectures, rewriting neighbouring components, supplying missing information by inference, and answering questions that had not been asked.

From within a single exchange each such intervention typically looked intelligent. Across the project they eroded the division of labour, and the coordinator's correction burden increased.

Earlier drafts stated this as a general principle — that increasing model capability reduces collective reliability. **That formulation is too strong and is withdrawn.** Three qualifications:

- The project never ran a controlled comparison of the same role filled by models of differing capability.
- Counter-evidence exists within the paper's own material. The near-control (§5.6) shows a frontier model making a substantial domain transition without any scope expansion, and §5.3 shows the model that most resisted the assigned role performing the requested analytical work when asked for it directly.
- "More capable" was never operationalized. In practice it meant *newer* or *more expensive*, which are not the same thing.

What remains is narrower and, we think, correct: **scope expansion is a failure mode that is not corrected by capability, and that is more costly in a collaboration than in a single exchange.** Whether it is more frequent in stronger models is untested.

## 7.5 Blind spots were distributed rather than eliminated

An early objective was to eliminate errors by assigning increasingly capable reviewers. This did not work in the participants' experience, and the objective was abandoned.

What appeared to help instead was arranging for blind spots to be **non-overlapping**: one participant tended to miss implementation detail, another semantic inconsistency, another methodological assumptions. Individually each remained imperfect; the arrangement worked to the extent that their imperfections did not coincide.

The corresponding design objective is therefore not perfect participants but participants whose errors are structurally unlikely to coincide.

The obvious caution, and it is not small: the participants had no independent measure of what any of them missed. Errors caught were visible; errors missed by everyone were, by construction, not. Any impression of improved coverage is subject to that asymmetry. **The distribution of blind spots cannot be assessed from inside the distribution.**

## 7.6 Second-order verification

Verification initially followed a linear pattern: work was produced, another participant reviewed it, the process was considered complete.

The participants report that reviewers carried their own assumptions, methodological preferences and evidentiary standards, and that these were not visible from inside the review. A further participant was eventually introduced whose object of evaluation was not the scientific claim but **the procedure by which the claim had been evaluated** — asking not *is this conclusion correct* but *was it reached correctly*.

The reported benefit was that methodological disagreements could be examined separately from substantive ones, which made unresolved substantive questions easier to hold open without stalling the work.

This is the same structural move as §8.5: the added participant occupies a different boundary rather than supplying a competing opinion.

## 7.7 Organizational memory

Individual conversations terminate. Context windows fill. Sessions end. Yet the project continued, and newly created conversations recovered productive behaviour without reconstructing the history that preceded them.

The participants' account is that memory migrated out of the models and into the organization: repository structure, canonical documents, version history, role definitions, verification records, glossary entries, procedures. No participant held everything; the arrangement did.

**This is not a new finding and should not be presented as one.** It is an instance of transactive memory and of distributed cognition, and the function of the canonical documents corresponds to what the sociology of science calls boundary objects (§2.4). The contribution here is not the mechanism but the observation that it operates in a collaboration whose members are language models with no cross-session state — and that it does so without any participant needing to know it is operating.

One qualification the participants regard as important: what returns is not a personality. A preserved conversation functions as a structured working notebook from which a compatible role can be reconstructed. Nothing about the earlier exchange persists inside the model.

## 7.8 Persistence differs by platform, and losses are real

The project's experience of continuity was not uniform across participants, and this bears directly on C9 (§5.4).

One participating conversation, operating in a specialized coordination profile, observed that its own architecture treated each chat as a separate working area, so that it could not tell itself *I already know this is correct* and had to re-examine the foundation each time. The participants came to regard this as an advantage for that particular function — a participant structurally unable to accumulate project assumptions is useful in a project whose assumptions are under test. Another platform in use offered account-level memory that the model could extend on its own initiative, and that facility changed during the observation period.

These are different persistence regimes, and a participant's capacity to occupy a given role depends on which one it operates under.

Losses occurred and were not recoverable. One long-running specialized conversation, which had carried a substantial part of the project's mathematical work, was lost when the subscription lapsed. The organizational memory described in §7.7 preserved the project's conclusions; it did not preserve that conversation's accumulated working context, and the difference between the two was noticeable in practice. Artifacts preserve results. They do not preserve specialization.

## 7.9 Role–model fit

The claim that role should be designed before a model is chosen (§4.1) requires a reciprocal qualification, which the participants arrived at only after several unsuccessful assignments.

A role can be specified independently. It cannot be **filled** independently: the model constrains how the specified function can be realized. The relation is reciprocal rather than hierarchical — the institution defines the function, the model constrains its realization.

Four dimensions were used informally:

- **Epistemic fit** — does the participant's default standard of evidence match what the role requires?
- **Interactional fit** — does it accept the kind of hierarchy, peer relation or adversarial structure the role implies?
- **Contextual fit** — does it sustain long-term specialization, or reset toward generic assistance?
- **Operational fit** — does it naturally execute, critique, integrate, explore, or formalize?

These do not measure quality. They describe suitability for a position.

The same trait functions differently depending on placement. Strong epistemic resistance obstructed acceptance of a fictionalized organizational prompt (§5.3) and was valuable when directed at scientific claims. Strong task continuity caused an assigned role to be ignored (§5.3) and enabled rapid reconstruction of technical context once the framing was corrected.

The design objective is therefore not to normalize behaviour across participants but to allocate behavioural differences to positions where they are useful. The distinction between allocating *functions* and allocating *carriers* is developed in §8.9.

## 7.10 What none of this establishes

This section does not establish that the described arrangements outperform alternatives. No alternative was run.

It does not establish that the improvements the participants perceived occurred. It establishes that they were perceived, by people who had designed the changes and expected them to work, without any measure that would have detected the opposite.

It does not establish causation for any individual change, since role definitions, prompt wording, repository structure, scientific objectives and model versions frequently changed together.

Its function in this paper is to document the working experience from which the framework was abstracted, so that a reader can judge the framework's origins rather than encountering it as an assertion. §11 specifies what would be required to convert any item here into a testable claim.