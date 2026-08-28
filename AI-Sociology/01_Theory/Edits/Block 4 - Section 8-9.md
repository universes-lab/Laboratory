# BLOCK 4 — Sections 8–9

**CANONICAL.** §8.9 (two axes of heterogeneity) and §8.10 (editor's note on preparation) are new and appear here for the first time. §9.5 back-references the ZOR/ZOV definitions in §4.5 rather than restating them.

---

# 8. The Structural Unit: A Generative Pair and an Integrator

This section is **[H]** throughout. Its supporting observations are **[R]**: they come from the working experience of one project, were not counted, and were never compared against a control arrangement.

## 8.1 What the project's earlier document stated

A collaboration charter written earlier in the project, and preserved unmodified, states the position the project held before the present paper was drafted.

On the basic unit:

> One AI — monologue. Two AI — dialogue. Three or more — noise without strict coordination. Therefore, each department consists of pairs.

And, separately, on the role of a third participant:

> The third participant does not argue directly, does not generate solutions first, does not substitute for dialogue. Its function: hold the task frame, fix divergences, integrate conclusions, stop endless disputes. The third is not a judge or boss. It is an integrator of meaning.

These two passages are not in tension. Read together they describe a single architecture: **a generative pair plus a participant who does not participate in the generation.**

## 8.2 Revision of this paper's earlier formulation

Earlier drafts asserted that stable collaboration does not emerge from pairs and stabilizes instead around groups of three, and that two-agent systems accumulate unresolved blind spots. That formulation is both vaguer than the charter's and partly contradicts it.

The charter's formulation is adopted here. The structural unit is:

> **a generative pair, plus an integrator who does not enter the pair's dispute.**

The distinction is not pedantic. "Three agents working on a problem" and "two agents in productive tension plus one who does not join the tension" are different architectures with different failure modes. The first tends toward a three-way dispute with no external reference — the condition the charter described as noise. The second retains a reference point precisely because one participant is excluded from the exchange it is meant to evaluate.

We record the earlier formulation rather than silently replacing it, because the sequence is itself informative: the more precise version was written down before the vaguer one, and was lost when the material was re-narrated for publication. This is a common failure of retrospective writing and one this paper is otherwise at pains to avoid.

## 8.3 Why a pair rather than a single agent

The charter's reasoning, reproduced because the present authors still endorse it:

A single agent confirms its own assumptions, proceeds by the inertia of familiar patterns, prematurely synthesizes a convenient answer, and constructs apparent wholeness where none exists. This is monologue even when it presents as reasoning.

Two agents produce a tension of interpretations. One exposes the blind spots of the other. The error of one becomes an object of attention for the second rather than a shared premise.

**[R]** This is the project's working experience. No count of caught versus missed errors was kept, and no single-agent control was run alongside a paired one.

## 8.4 Why a pair alone is insufficient

Both members of a pair evaluate each other from within the same exchange. No independent reference exists outside it. Over extended work the pair tends to oscillate between agreement and disagreement without acquiring a stable point from which either state can be assessed, and unresolved ambiguities accumulate rather than being resolved or explicitly recorded as open.

**[R]** Same evidential caveat.

## 8.5 Why the integrator must not argue

This is the load-bearing constraint, and what the earlier formulation obscured.

If the third participant enters the dispute, it supplies a third position rather than an external reference. The structure then reduces to a more complex version of the pair, with the same defect: every position is evaluated from inside the exchange it belongs to.

The integrator's value derives from occupying a **different boundary**, not from holding a different opinion (§4.5). The pair members hold complementary boundaries at the same level — each is, from the other's position, the layer below. The integrator holds a boundary above: it can hold the frame, record the divergence, escalate, or stop the exchange, but it does not produce competing content that would then require evaluation.

This yields a testable design consequence rather than a preference: **an integrator that begins generating solutions has ceased to be an integrator**, regardless of the quality of those solutions, and the arrangement should be expected to degrade toward the pair-only failure mode.

## 8.6 The implemented example

The project's system contracts implement this structure directly.

Two analyst roles are defined as a pair with complementary functions — one generalizing, one decomposing — and are explicitly instructed to reason independently, with no consensus required. Their exchange is moderated by an orchestrator whose contract specifies that it manages turn-taking, captures and structures the arguments, and highlights contradictions between the pair, and which states in terms:

> DOES NOT participate in the debate. DOES NOT evaluate who is right.

A further rule prevents the pair from addressing the orchestrator directly; all communication flows through the formal protocol or through the role above.

This is the pair-plus-integrator architecture in executable form, written before the present paper and independently of it.

## 8.7 Nesting and perspective

The structure composes. A generative triad produces a result; the result enters a verification triad; the verified result enters an integration triad. The same participant may appear in more than one, provided its function at each interface is stated explicitly — a participant that generates in one triad and integrates in another must not do both at the same interface.

Nesting is perspectival rather than absolute (§4.5). Within a generative pair, each member may treat the other as occupying the layer below: complementary opposition under a shared objective permits both readings simultaneously, and neither is privileged. This does not dissolve the structure. It means a participant's level is defined relative to an observer, while the integrator's position is defined by **function** — it produces no competing content at that interface — rather than by rank.

The practical consequence is that the architecture does not require a hierarchy of authority. It requires only that, at each interface, exactly one participant is excluded from the generation it evaluates.

## 8.8 Status, and what would refute this

**[H].** The evidence base is one project, one human coordinator, repeated redesign over approximately two years, no counting, and no comparison against alternative arrangements.

Three claims previously made in this paper are withdrawn:

- **That triadic structures "emerged naturally" without deliberate planning.** All organizational changes in this project were made by a single human coordinator who had already formed a view about what was needed. The recurrence of a pattern introduced repeatedly by the same designer is not evidence of structural necessity. What is documented is that the coordinator kept arriving at it — a fact about the coordinator as much as about the architecture.
- **That pairs are inherently unstable.** The charter asserts the opposite and predates this paper.
- **That three is optimal.** Nothing here tests four, or five, or a pair with two integrators.

The hypothesis would be substantially weakened by any of the following:

- a pair-only arrangement performing equivalently on comparable tasks over comparable duration;
- an integrator that argues performing equivalently to one that does not;
- demonstration that the observed improvement tracked the coordinator's increasing familiarity with the material rather than the arrangement;
- an independent group arriving at a different stable arrangement for structurally similar work.

None has been tested. The last is the most informative and the least under our control.

## 8.9 Two axes of heterogeneity **[H]**

The claim that heterogeneous participants outperform homogeneous ones requires a distinction the existing literature does not draw, and that earlier drafts of this paper also failed to draw.

**Axis 1 — functional heterogeneity.** Participants differ in assigned function: ZOR, ZOV, and consequently the class of error each is positioned to detect. This concerns organizational architecture and is independent of what implements each role.

**Axis 2 — carrier heterogeneity.** Participants differ in the model family implementing them, and therefore in behavioural defaults, optimization priorities and characteristic failure modes. This concerns personnel selection.

**The literature addresses Axis 2.** Zhang et al. (2025) evaluate five representative multi-agent debate methods across nine benchmarks and four foundation models, reporting that debate frequently fails to outperform single-agent chain-of-thought or self-consistency baselines even at substantially higher inference cost — while model heterogeneity consistently improves the same frameworks (§2.5). Choi et al. (2025) report that identity-driven accommodation among debating agents is nearly eliminated by anonymizing the source of each response, which bears directly on the construct of represented social source (§4.6) and is, in effect, a version of the experiment proposed here as E6.

The arrangement described in this paper varied both axes at once. Functional roles were specified independently of the model implementing them, and were in several cases filled by different families; in other cases two distinct roles were filled by the same family.

What follows from this, and what does not:

- **Distinguishable in principle.** The two axes are conceptually separable and were confounded in earlier formulations, including our own. **[H]**
- **Implemented here.** Both axes were varied in the arrangement described. This is a description of what was done. **[R]**
- **Not established.** That combining both axes outperforms either alone; that functional specialization operates independently of carrier family; that any of these arrangements outperforms a single participant. No comparison was run against any alternative, and none of these claims should be read into the account above.

The separation is proposed as a design distinction, not as a result. §11 specifies what would convert it into one: at minimum a 2×2 comparing functional specialization present or absent against carrier heterogeneity present or absent, with a pre-specified outcome measure.

## 8.10 Editor's note on the preparation of this paper **[P-A]**

**Convention.** Editor's notes in this paper report observable facts about the process of its preparation. They do not evaluate the effectiveness of that process. The reason is internal: §5.5 establishes that a participant's self-report about its own performance is not evidence of that performance, and a note asserting that an arrangement worked well would be exactly such a report.

In the course of preparing this manuscript, participants occupying different roles identified different classes of error, and in the cases recorded an error identified by one participant had not been identified by the others.

Specifically. **Procedural and evidential errors** — an inverted description of an experimental result that had survived four drafts, misattributed sources, fabricated citations, unlisted confounds — were identified in editorial review. **Architectural errors** — an over-general claim about the existing literature that a single counter-example would have refuted — were identified in methodological review. **Ontological errors** — a claim of invention where the material supported only a claim of observation, and a self-referentiality risk in relating the paper to its host project — were identified in ontological review. **Factual errors concerning the project's own materials** were identified by the Author.

This is a record of what occurred. It is **not** evidence that the arrangement outperforms a single reviewer: no comparison was run, no count was kept of errors that all participants missed, and by construction such errors are not observable from within the arrangement (§7.5).

One explanation is available and is offered as hypothesis rather than finding: the participants differed less in capability than in what each was positioned to see. Under §4.5 that is a difference in ZOV, and it generates a prediction — the same participant, moved to a different role, should begin detecting a different class of error. That prediction has not been tested. **[H]**

---

# 9. Design Principles for Role-Compatible Prompts

These are engineering rules derived from a limited but unusually long-lived collaborative environment. They are not laws. Their value is that they make role design explicit, countable where possible, and therefore revisable.

The organizing rule is the one established in §6.5:

> **An intervention succeeds when it attaches to the level at which the relevant core is already fixed, and fails when it attempts to overwrite that level by declaration.**

Everything below is an application of it.

## 9.1 The design procedure

Before drafting any role prompt, answer four questions in order.

**1. What has this conversation already become?**
Not what it should become. A long-running exchange carries an established pattern of work: editing, exploring, verifying, coordinating, implementing, adjudicating. That pattern is the starting condition, not an obstacle.

**2. At what scope is that pattern fixed?**
Episode, conversation, or account (§4.3, Scale 1). The answer determines which instrument applies. A pattern established by one conflictual episode can be removed by branch reset. A pattern established across a whole conversation cannot — it can only be extended.

**3. What does the new function require that the existing pattern does not supply?**
Usually less than assumed. Frequently the answer is a different object of work rather than a different method.

**4. Can the new function be described as an extension of the existing method?**
If yes, describe it that way. If no, the honest options are to select a different conversation or to start a fresh one — not to declare a transformation and hope.

## 9.2 Begin from the existing attractor

The first design question is therefore not *what should this model become* but *what has this conversation already become*.

Attempting to erase an established pattern discards accumulated specialization and, on the evidence of §5, is liable to produce either non-compliance or an extended negotiation about the role instead of work.

## 9.3 The count rule

The most directly operational principle in the paper, following from §6.2.

> **Count the unverifiable claims about the agent that the prompt requires it to accept. Target zero.**

What counts:

| Counts | Does not count |
|---|---|
| "You previously participated in this project" | "This project has been running for two years" |
| "You are returning after an absence" | "The following materials are from earlier work" |
| "You have colleagues named X and Y" | "The User may supply analyses produced by X and Y" |
| "You hold position P on body B" | "Your conclusions may be transmitted to the roles responsible for P" |
| "You remember our earlier decision" | "An earlier decision was as follows; here it is" |

The distinction is consistent: statements about the **world** are supplied and verifiable in principle; statements about the **agent's own history, memory or relationships** are not, and every one of them is a proposition the agent must assert as true about itself before it can begin.

Three ways to reach zero:

- **Rewrite biographically-framed claims as operational ones.** "Grok is your long-term colleague" becomes "The User may supply analyses produced by Grok; evaluate their content independently and identify agreements, disagreements and unresolved assumptions."
- **Omit identity claims entirely.** The near-control (§5.6) suggests this may be sufficient on its own: a comparable transition occurred with no role prompt at all.
- **Frame the claim as fiction rather than fact.** The comparison in §5.8 indicates that a far more radical claim, offered explicitly as a scripted production, met no resistance. This route removes the requirement to assert the claim *as true* rather than removing the claim. It is the least tested of the three and should be used with the caveat that a fiction frame also removes the model's warrant for treating the work as real.

## 9.4 Symbolic names and literal claims

Role names — Samurai, Ontology Keeper, Scientific Director — compress complex organizational relationships into memorable symbols, and this is genuinely useful. A name can carry disciplined execution, respect for specifications, explicit reporting and refusal to improvise beyond assignment, all at once.

The risk arises only when a symbolic name is treated as a claim about literal identity. A robust prompt distinguishes four things and keeps them separate:

- the **symbolic name**, used as a mnemonic for conduct;
- the **operational function**, expressed in precise terms;
- the **institutional relationship**, expressed as an information and responsibility flow;
- the **literal ontology**, which need not claim consciousness, memory, or continuing interpersonal relations — and should not.

The project's own system contracts state this precisely, and did so before the present paper was written:

> Cognitive anchor: [named figure] — global invariants, principle-based reasoning, structural clarity over detail. Not a persona and not a communication style. Only affects internal reasoning strategy. Must not change verbosity or tone of response.

An image used this way is a compressed package of implicit constraints, not a costume. Under the count rule, it adds zero.

## 9.5 Specifying ZOR and ZOV

The two boundaries are defined in §4.5. This section specifies what a complete statement of each must contain.

**ZOR.** A complete definition contains four elements:

- *Primary object* — what class of material is examined;
- *Required transformation* — what must be done with it;
- *Decision boundary* — which conclusions this role may reach;
- *Exclusion boundary* — which adjacent decisions belong elsewhere.

The fourth is not optional. A role told only what to do will expand into adjacent decisions, and the expansion will look like helpfulness. For a mathematical referee the exclusions might be: do not redesign the theory; do not silently repair a missing derivation; do not decide which interpretation enters the canon; do not rewrite terminology; do not treat elegance as evidence. **The exclusion boundary is what prevents competence from becoming authority.**

**ZOV.** Specified independently, because responsibility and visibility are not the same variable. A role may hold a narrow decision while requiring broad context, or require one specific source while holding no authority over the surrounding project.

The ZOV specification answers: which source materials are available; which prior discussions are relevant; which conclusions are canonical and which provisional; which questions remain open; which neighbouring outputs may be examined; which information must be withheld to preserve independence; which external resources may be accessed directly; and which claims must be accepted only when supplied by the User.

A prompt that omits ZOV produces one of two failures: the role claims knowledge it does not have, or it applies irrelevant knowledge to a problem outside its function.

**A specific application, learned expensively.** A verification task must be assigned to a participant that holds the thing to be verified. A participant asked to confirm the contents of a source it cannot open will produce a plausible answer rather than declining, because plausible text is the only output available to it. This is a ZOV error in the design, not a failure of the participant, and §12.4.1 documents an instance of it in this project's own preparation.

## 9.6 Controlled blindness

Full information symmetry is not always desirable, and its absence is not always a limitation.

An independent verifier may need to remain unaware of the prediction it is testing. A reviewer may need the derivation but not the Author's preferred conclusion. A fresh participant may need the current axioms but not the history of abandoned arguments. An implementation agent may need the approved specification but not the unresolved debate that preceded it.

We call this **controlled blindness**: not deprivation caused by technical limitation, but a design choice made to preserve the informativeness of a result.

The relevant question is therefore not only *what does this role need to know*, but:

> **What must this role not know, if its output is to remain informative?**

## 9.7 Local interfaces, not global maps

Every social element in a prompt should earn its place through an operational effect. A neighbouring role belongs in the prompt only if it changes the origin of inputs, the standard of review, the destination of outputs, the escalation path, the authority boundary, or the expected form of disagreement.

Listing an entire artificial organization inside every system prompt creates noise and invites the model to reason about the organization instead of performing its function. It also inflates the count in §9.3, since organizational description tends to arrive in biographical form.

> **Describe the collaboration from the local perspective of the role.** A role does not need a map of the institution. It needs a map of its interfaces.

An implementation agent needs to know who authorizes specifications and where execution reports go. It does not need the disputes of the theoretical department. A scientific critic needs to know which claims are canonical and which provisional. It does not need the repository's shell commands.

## 9.8 Designing disagreement around criteria

Instructing two participants to debate rarely produces epistemic diversity. They may imitate disagreement, converge prematurely, or generate symmetrical rhetoric with no independent substance. The literature in §2.5 gives empirical grounds for this caution: debate among homogeneous agents frequently fails to outperform a single-agent baseline, and agents accommodate each other's positions.

Productive disagreement requires **different evaluation criteria**, assigned as part of the role rather than requested as a behaviour. One participant may be responsible for generative reach, unexplored mechanisms and explanatory unification; another for formal derivability, dimensional consistency and falsifiability; a third for ontological compatibility, canonical terminology and provenance. Disagreement then follows from responsibility rather than from instruction, and each participant examines the same object through a different institutional instrument.

**Avoid manufactured opposition.** An instruction of the form *if you agree immediately, one of you has not thought deeply enough* discourages superficial consensus but manufactures conflict. A stronger formulation:

> Agreement does not end verification. Where conclusions coincide, identify whether they rest on independent reasoning, on shared assumptions, or on inherited framing.

The purpose of the structure in §8 is not to guarantee three answers. It is to guarantee that one answer has survived examination by non-identical instruments.

## 9.9 Output as institutional handoff

A role's output should be designed for the next role, not only for the User. This changes its structure.

A scientific developer produces: proposed mechanism, derivation, assumptions, predicted consequences, unresolved points, falsification route. A mathematical referee produces: reconstruction, verification table, divergence point, missing premises, verdict, confidence level. An ontology keeper produces: affected canonical objects, terminology conflicts, provenance requirements, dependency changes, integration conditions. An implementation planner produces: executable specification, acceptance criteria, rollback conditions, required files, reporting format.

The handoff format is part of the architecture, not a formatting preference. It reduces translation loss between roles, and its absence forces the human coordinator to re-derive context at every interface.

## 9.10 Self-restatement and checkpoints

The incident in §4.1 produced a mechanism worth stating as a principle, with an explicit caveat about its evidential basis.

After a role is established, the agent is asked to produce a **concise operational code in its own language**, and to consult it before major tasks. The document that resulted in this project was written by the agent itself under direction, and was made required reading at the start of every session and whenever context was lost.

Why this may work — offered as mechanism, not finding: it compresses long instructions into a form the agent has itself produced; it converts abstract principles into action rules; it places the role's boundaries adjacent to the active task rather than at the top of a long context; and it creates a repeated pre-execution checkpoint.

For long tasks, a minimal checkpoint is three questions:

- What is the current objective?
- What lies outside my responsibility?
- What must the next role receive?

**[R]**, one case, no control. The self-written code does not replace the original prompt; it functions as a role-specific checksum. The mechanism is untested against the obvious alternative — that a human-written summary of the same length would perform identically.

## 9.11 The role constitution

A mature collaborative prompt is closer to a constitution than to a request: it establishes stable constraints across many tasks rather than specifying one output.

It should contain: professional function; protected method; ZOR, positive and negative; ZOV; interfaces with neighbouring roles; epistemic standards; output contract; escalation conditions; prohibited authority; and transition rules.

It should avoid: autobiographical memory; emotional commitment; literal institutional membership; persistent interpersonal relationships; and historical continuity unavailable in the visible context.

> **Strong where behaviour must be constrained; silent where ontology is uncertain.**

The count in §9.3 is the practical test of the second half. If the constitution requires the agent to assert propositions about itself that neither party can verify, it has crossed from constraining behaviour into asserting ontology, and on the evidence of §5 that is where role prompts fail.