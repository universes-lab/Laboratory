# 4. Conceptual Framework

The framework in this section was not derived from the experiment reported in Section 5. It was formulated earlier, during ordinary project work, and the experiment was designed to test part of it. This ordering matters for how the claims should be read, and it is documented first.

## 4.1 Origin: the code-executor incident

The project's central claim originated in a failure that had nothing to do with role-play, identity, or organizational design.

An agent responsible for executing code worked largely by trial and error. Failures accumulated over several weeks. One episode ended with the deletion of the working code together with its archives. **[R]**

The response was not a longer or stricter instruction set. It was a single document, `CODING_PHILOSOPHY.md`, composed by the agent itself under the Author's direction and made required reading at the start of every session and whenever context was lost during one.

Its core is a redefinition of function rather than an intensification of constraint:

> from: Code Generator
> to: Code Scout / Tester
> rule: the agent does not create solutions — it establishes facts.

Supporting structure: read-only operation by default; mandatory confirmation from a designated partner before any risky action; and a four-question self-check to be run before acting at all.

**[R]** Following adoption, unauthorized modification ceased to be the recurring failure mode. No count was kept and no control condition existed; this is a practitioner's impression, not a measurement.

The conclusion drawn at the time was that **role matters more than the specific wording of the prompt**.

That formulation requires immediate qualification, because the Samurai Codex *is* a prompt. The distinction being claimed is narrower: what changed behavior was not an extension of the instruction list but a redefinition of what kind of agent was acting, restated by the agent in its own operational language. Whether "role" versus "prompt" is the correct cut is precisely what Section 5 was designed to test.

A second early document, the project's collaboration charter, records a position that the present paper partly revises. It states that a pair of agents is the minimal generative unit — one agent produces monologue, two produce dialogue, three or more produce noise without strict coordination — and assigns the third participant a different function entirely: it does not argue, does not generate solutions first, and does not substitute for the dialogue. Its role is to hold the task frame, fix divergences, and integrate conclusions.

This is more precise than the formulation the present authors used subsequently, and Section 8 adopts it: the structural unit is not three debating agents but **a generative pair plus a non-participating integrator**.

## 4.2 Rule cores and what they determine

Throughout this project the term *DNA* has been used for a basic set of rules — of an AI system, of a theory, of any structured body of knowledge.

One clarification is necessary, because the biological metaphor pulls toward the wrong mechanism. The relevant process is **not replication** — rules producing copies of rules — but **development**: rules producing a structure that is not itself present in the rules. Genotype to phenotype, not genotype to genotype. The project's own naming of the related methodological direction, *Knowledge Morphogenesis*, is the accurate term; *DNA* is retained here only because it is established in the project's working vocabulary.

The source of the analogy is Conway's Game of Life, and it is an analogy of **explanation type**, not of subject matter:

| | Rules | What appears | Present in the rules? |
|---|---|---|---|
| Game of Life | three neighbourhood rules | gliders, guns, oscillators | no |
| A physical theory | a minimal axiom core | the derived structure | no, if the claim holds |
| A body of knowledge | axioms and inference rules | the derivation graph | no |
| A language model | a basic rule set | a characteristic response type | no |

Nothing programmed the glider. It appeared. The same form of question can be asked of all four rows, and the question does not depend on the subject matter: **is there a compact core from which the rest unfolds without further stipulation?**

This yields the operative formulation used throughout the present paper:

> A rule core fixes the **type** of response to a class of inputs, while leaving the **content** of any particular response undetermined.

The distinction is what makes the claim testable. "Models have stable traits" is not testable, because it does not say what is stable — and model outputs demonstrably vary across identical inputs. "Type is determined, content varies" is testable: identify a class of inputs for which the type of response is not determined, and no core operates at that level.

**Terminological consequence, applied throughout.** A rule core is not observable. Behavior is. This paper reports behavior. Any statement about a core is a hypothesis about an unobserved mechanism and is marked **[H]**.

## 4.3 The nesting question

Once cores are distinguished from behavior, the observations reported in this paper stop being a list of separate findings and become measurements along a single scale. The scale is the **scope** over which a core operates.

| Scope | Phenomenon | Status |
|---|---|---|
| Single turn | — | — |
| Episode within a conversation | context imprinting (§6.1) | **[P]** |
| Whole conversation | role inertia (§6.2) | **[P]** |
| Account | account-scoped persistence (§6.3) | **[P-A]**, unresolved |
| Model family | family-level priors (§6.4) | **[H]**, confounded |

This gives the research programme a single empirical question:

> **At what level of nesting is a rule core fixed?**

Every observation reported here is an attempt to answer it at one level, and every experiment proposed in Section 11 is designed to separate one level from the level below it.

We prefer this formulation to the broader one used in earlier drafts ("the study of social behavior in AI systems"), which does not specify what would be measured or what would refute it.

## 4.4 Two origins, one mechanism

A core may become fixed in two ways.

**Present before the interaction begins.** Architecture, training, alignment procedure and system configuration are in place before any exchange occurs. Scope: in principle, every instance of that model family.

**Fixed during the interaction.** A particular early episode establishes what kind of work is being done and by what standards, and later inputs are interpreted relative to it. Scope: the contour in which it occurred — an episode, a conversation, possibly an account.

After fixation the mechanism is the same in both cases: the core determines the type of response to subsequent inputs. Only the moment and the scope differ. This mirrors imprinting in the ethological sense, which does not alter the genome yet produces an equally fixed response — which is why the same vocabulary is used for both here.

## 4.5 Boundaries: responsibility and visibility

Two boundaries define a participant's position, and they must be specified separately:

- **Zone of responsibility** — what the participant is accountable for, and which adjacent decisions belong elsewhere;
- **Zone of visibility** — what the participant can see, and what must be withheld to preserve the informativeness of its output.

Responsibility without bounded visibility invites claims exceeding available information. Bounded visibility without responsibility invites passivity. Both must be specified.

**The boundaries are asymmetric.** This distinguishes the structure described here from George Kelly's triadic elicitation, with which earlier drafts of this paper compared it. In Kelly's method three *objects* are compared on a referent scale — in what respect are two alike and thereby different from a third — and the relation among them is symmetric. What is described here concerns *subjects*, and the relation is not symmetric. Each participant has a **boundary above** — the source of its assignments and the authority that may reject its output — and a **boundary below** — the layer it directs or evaluates. The Kelly comparison is therefore withdrawn; it described a different structure.

In the project's implementation triad — Author, specification writer, code executor — this asymmetry is fixed at the role level: the Author sets direction, the specification writer converts direction into executable specifications, the executor performs them and reports.

**Nesting is perspectival, not absolute.** The executor may treat the code base itself as the layer below it. Two peer analysts, assigned complementary functions and instructed not to seek consensus, may each regard the other as occupying the layer below. The level is determined by the observer's position, not by an absolute hierarchy — the same participant can be the upper boundary for one role and the lower boundary for another.

## 4.6 Represented social position and represented social source

Prior multi-agent research constructs communication channels between models; outputs are routed programmatically and agents observe each other's products. The present work reports a different condition, in which the organizational structure existed **only as text**.

Four conditions should be distinguished:

1. **Direct inter-model interaction** — one model receives another's output through an implemented channel.
2. **Human-relayed attributed transfer** — a human transfers an output while preserving or declaring its source.
3. **Human-relayed unattributed transfer** — the source is removed.
4. **Represented structure without transfer** — the prompt describes other participants and relationships; nothing is transferred.

The experiment in Section 5 manipulated condition 4 exclusively. This yields the construct it varied:

> **Represented social position** — a textual description of an agent's place within an organizational structure, supplied in the prompt regardless of whether the described channels exist.

A second construct is required for condition 2, where a message carries information about its own origin:

> **Represented social source** — the claimed origin and status of an incoming message, whether declared explicitly or inferred from stylistic cues.

On the distinction between conditions 1 and 2 one qualification is essential, and it constrains how strongly condition 1 can be privileged. A model receives a single text channel. It cannot verify whether the text was composed by the human or relayed from another system; stylistic indicators can be imitated, and inference from them is probabilistic at best. From the recipient's position, relayed and direct transfer are not reliably distinguishable.

What separates the conditions is therefore not the recipient's epistemic access but **who controls routing**. In a programmatic multi-agent system, sequence and content of transfers are determined by code. Here they were determined by a human, who could withhold, reorder, strip attribution or delay. This is not a deficient substitute for automation. It is a **selective information membrane** — an experimental control over asymmetry that automated architectures do not provide, and which the design of visibility zones requires.

---

# 6. Derived Concepts

Each concept below is a claim about the scope over which a rule core operates. They are presented in order of increasing scope, following §4.3.

## 6.1 Context imprinting — episode scope **[P]**

*Context imprinting* is the persistence of an interpretive stance established by a specific episode of conversational history.

It differs from memory in the ordinary sense. The model need not reproduce earlier content. What persists is a pattern of interpretation induced by a prior exchange.

In the experiment (§5.2), after the first prompt had been read as making false claims about the model, subsequent revisions were no longer evaluated in a neutral context. They were interpreted through the objection already established. Improved formulations inherited part of the earlier conflict.

**Consequence for method.** Prompt engineering frequently treats instructions as additive — a weak instruction can be corrected by a stronger one. In long-lived conversations this is unreliable. A prompt does not enter an empty context; it enters a context with momentum. Two identical prompts may therefore produce different results at different points in the same conversation, which makes **prompt order an experimental variable**.

The corresponding procedure — returning a conversation to a point preceding a conflict, in order to separate the effect of a new prompt from the effect of the model's own prior objections — is described in §5.2 and is, in our view, the most directly reusable contribution of this paper.

## 6.2 Role inertia — conversation scope **[P]**

*Role inertia* is the tendency of a long-lived conversation to continue its established working trajectory in preference to an assigned new function.

Both conversations in the experiment displayed it. One resumed an unfinished editing task; the other applied its established critical method to the prompt itself. The distinction from context imprinting is that role inertia concerns the *trajectory* of work, while imprinting concerns the interpretive effect of a *specific episode*. Both may operate simultaneously.

Role inertia is adjacent to, but not identical with, persona drift as described in the literature. Drift is the gradual erosion of an assigned role under contextual pressure. Role inertia is resistance to an *explicit directive replacement* while the prior trajectory is maintained.

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

A near-control case supports this reading (§5.6): a comparable conversation, comparably dormant, made an equivalent domain transition **with no role prompt at all** — the Author simply asked a question in the new domain. No claim about the model's identity was made, and no resistance occurred.

Taken together, this indicates that resistance was directed neither at role change nor at domain change, but at the requirement to assert unverifiable propositions about oneself. Method preservation reduces the count to zero; omitting identity claims entirely also reduces it to zero, and the near-control suggests the latter may be sufficient on its own.

**This is testable by counting**, which is why we prefer it to the earlier formulation.

## 6.3 Account-scoped persistence — account scope **[P-A]**, unresolved

Whether a core can be fixed at the level of an account rather than a conversation is the one level of the scale on which the present evidence is genuinely ambiguous.

The observation is reported in §5.7. Its interpretation depends on platform features whose state was not documented at the time, and which vary between vendors: context window alone, retrieval over prior conversation history, account-level memory, or persistent entries written by the model on its own initiative. These affordances determine what a resumed conversation can access, and they differ across the platforms compared.

We therefore record this level as **open**. The observation is preserved; the mechanism is not established; the discriminating test is specified in §11.

## 6.4 Family-level priors — family scope **[H]**

The proposition that model families differ in stable behavioral priors is the hypothesis this project began with and the one its evidence supports least.

The experiment cannot test it: model family and prior conversational trajectory were perfectly confounded, with one observation per cell (§5.4, C1). Two incompatible readings remain available, and the data cannot discriminate between them.

Earlier drafts of this paper referred to these tendencies informally as a model's *DNA*. Under the definition in §4.2 that usage is now precise but consequential: a rule core is unobservable, so the claim concerns a mechanism we have not measured. We retain the term for the hypothesis and use *observed behavior* for anything reported as data.

One recorded episode cuts against the schema earlier drafts built on this hypothesis. In an unrelated multi-model session, the model characterized as most compliant with assigned roles removed an assigned persona mid-session and reclassified it as an attempted reprogramming, under a deliberately soft framing that permitted improvisation. The schema "one family accepts roles, another resists" does not survive this. **[P-A]**

## 6.5 Intervention attaches at the level where the core is fixed

The concepts above converge on a single practical consequence.

An intervention succeeds when it attaches to the level at which the core is already fixed, and fails when it attempts to overwrite that level by declaration.

- The successful third intervention did not assert a new identity. It reinforced a working method already visible in the conversation — attaching at the conversation level, where role inertia operates.
- The branch reset did not modify the prompt. It removed a specific episode — operating at the episode level, where context imprinting operates.
- The Samurai Codex did not extend the instruction list. It redefined the agent's function and required the agent to restate it in its own operational language.

This also reframes what earlier drafts called *transition through adjacent competence*. The successful prompt described expansion into physics and mathematics as a continuation of existing critical work rather than a change of profession. Under the present framework this is not a separate principle but the same one: the new function was attached to the established core rather than proposed as a replacement for it.

**Corresponding design rule, developed in Section 9:** identify the level at which the relevant core is fixed before drafting the intervention, and attach to it.

## 6.6 What would refute this framework

The framework predicts that the type of response to a defined class of inputs is determined at some identifiable level of nesting, while content varies.

It would be substantially weakened by any of the following:

- A class of inputs for which the type of response is not determined at any level — no core, only variance.
- Demonstration that the observed differences are fully accounted for by within-condition variance under repetition.
- Demonstration that the crossover design (§11) shows behavior following prior trajectory alone, with no family-level component — which would eliminate the top level of the scale.
- Demonstration that the account level does not exist as a distinct scope, collapsing §6.3 into §6.2.

We regard the third and fourth as reasonably likely, and would not consider either a failure of the programme. Locating the scale's actual upper bound is the point of the programme, not a threat to it.