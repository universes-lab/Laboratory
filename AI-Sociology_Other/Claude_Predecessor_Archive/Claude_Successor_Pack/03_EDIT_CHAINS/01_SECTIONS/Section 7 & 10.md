# 7. Retrospective Practitioner Observations

## 7.1 How this section should be read

Everything in this section is **[R]**. It records patterns that the participants believe recurred during approximately two years of daily work on a live research project. None of it was recorded under protocol, counted, timed, blinded, or compared against a control condition. The people who noticed each pattern were the same people who had designed the change that produced it, and who wanted it to work.

The known failure modes of this class of evidence are set out in §3.3 and apply to every paragraph below. They are not repeated at each item. Readers should treat this section as a field report from one team — closer in evidential weight to an engineering practice note than to measurement.

Quantitative language has been removed throughout. Where the original working notes recorded that something improved "significantly" or "substantially," no measurement existed, and the wording now reflects that.

The section is included because these observations motivated the framework in §4 and the design rules in §9, and suppressing them would misrepresent how the work actually proceeded.

---

## 7.2 Specialization displaced capability as the operative variable

At the outset of the project the participating models behaved similarly. Each attempted whatever was presented to it, and the differences between them were read as differences in intelligence or writing quality.

That reading gradually became less useful. The question that produced better outcomes was not *which model is strongest* but *which function does this conversation already perform well*.

As particular conversations acquired persistent working identities, the participants report that behaviour became more predictable across sessions: a conversation used consistently for editorial work continued to behave editorially; one used for mathematical exploration continued to explore; one responsible for terminology resisted semantic drift without being reminded to.

The underlying models did not change during these periods. What changed was the consistency with which each conversation was used for one kind of work.

This is the observation from which §6.2 (role inertia) was later derived, and it should be read as its retrospective, unmeasured precursor rather than as independent support for it.

## 7.3 Context behaved more like attention than like memory

The intuitive expectation is that more context improves reasoning. The participants' experience ran the other way often enough to change practice.

Supplying a specialist with the full project context frequently produced worse results for that specialist's own function: responsibilities blurred, participants attempted problems outside their competence, and the value of independent examination declined because everyone was working from the same picture.

Restricting what a participant could see frequently produced more usable output.

Two qualifications are necessary. First, this is not a novel finding: positional and order effects in long contexts are documented in the prompting literature (§2.3), and the principle of least privilege in system design (§2.6) expresses the same intuition for access rather than knowledge. Second, the project never distinguished between two quite different explanations — that additional context degrades reasoning, or that additional context simply invites the model to answer a broader question than the one asked. The second is more parsimonious and was never tested against the first.

What survives is the practical rule, not the mechanism: the design question is not only how much a role can be given, but what it should not be given (§9.6).

## 7.4 Capability and scope expansion

The participants repeatedly observed that more capable models were more inclined to exceed their assigned function: expanding project scope, proposing alternative architectures, rewriting neighbouring components, supplying missing information by inference, and answering questions that had not been asked.

From within a single exchange each such intervention typically looked intelligent. Across the project they eroded the division of labour, and the coordinator's correction burden increased.

Earlier drafts of this paper stated this as a general principle — that increasing model capability reduces collective reliability. That formulation is too strong and is withdrawn. Three qualifications:

- The project never ran a controlled comparison of the same role filled by models of differing capability.
- Counter-evidence exists within the paper's own material. The near-control (§5.6) shows a frontier model making a substantial domain transition without any scope expansion, and §5.3 shows the model that most resisted the assigned role performing the requested analytical work when asked for it directly.
- "More capable" was never operationalized. In practice it meant *newer* or *more expensive*, which are not the same thing.

What remains is narrower and, we think, correct: **scope expansion is a failure mode that is not corrected by capability, and that is more costly in a collaboration than in a single exchange.** Whether it is more frequent in stronger models is untested.

## 7.5 Blind spots were distributed rather than eliminated

An early objective was to eliminate errors by assigning increasingly capable reviewers. This did not work in the participants' experience, and the objective was abandoned.

What appeared to help instead was arranging for blind spots to be **non-overlapping**: one participant tended to miss implementation detail, another semantic inconsistency, another methodological assumptions. Individually each remained imperfect; the arrangement worked to the extent that their imperfections did not coincide.

The corresponding design objective is therefore not perfect participants but participants whose errors are structurally unlikely to coincide.

The obvious caution: the participants had no independent measure of what any of them missed. Errors caught were visible; errors missed by everyone were, by construction, not. Any impression of improved coverage is subject to that asymmetry, and it is not a small one.

## 7.6 Second-order verification

Verification initially followed a linear pattern: work was produced, another participant reviewed it, the process was considered complete.

The participants report that reviewers carried their own assumptions, methodological preferences and evidentiary standards, and that these were not visible from inside the review. A further participant was eventually introduced whose object of evaluation was not the scientific claim but **the procedure by which the claim had been evaluated** — asking not *is this conclusion correct* but *was it reached correctly*.

The reported benefit was that methodological disagreements could be examined separately from substantive ones, which made unresolved substantive questions easier to hold open without stalling the work.

This is the same structural move as §8.5: the added participant occupies a different boundary rather than supplying a competing opinion.

## 7.7 Organizational memory

Individual conversations terminate. Context windows fill. Sessions end. Yet the project continued, and newly created conversations recovered productive behaviour without reconstructing the history that preceded them.

The participants' account is that memory migrated out of the models and into the organization: repository structure, canonical documents, version history, role definitions, verification records, glossary entries, procedures. No participant held everything; the arrangement did.

**This is not a new finding and should not be presented as one.** It is an instance of transactive memory as described in organizational psychology, and of distributed cognition as described in cognitive science; the function of the canonical documents corresponds to what the sociology of science calls boundary objects (§2.4.1). The contribution here is not the mechanism but the observation that it operates in a collaboration whose members are language models with no cross-session state — and that it does so without any participant needing to know it is operating.

One qualification the participants regard as important: what returns is not a personality. A preserved conversation functions as a structured working notebook from which a compatible role can be reconstructed. Nothing about the earlier exchange persists inside the model.

## 7.8 Persistence differs by platform, and losses are real

The project's experience of continuity was not uniform across participants, and this is worth recording because it bears directly on the confound in §5.4 (C9).

One participating conversation, operating in a specialized coordination profile, observed that its own architecture treated each chat as a separate working area, so that it could not tell itself *I already know this is correct* and had to re-examine the foundation each time. The participants came to regard this as an advantage for that particular function — a participant structurally unable to accumulate project assumptions is useful in a project whose assumptions are under test. Another platform in use offered account-level memory that the model could extend on its own initiative.

These are different persistence regimes, and a participant's capacity to occupy a given role depends on which one it operates under.

Losses occurred and were not recoverable. One long-running specialized conversation, which had carried a substantial part of the project's mathematical work, was lost when the subscription lapsed. The organizational memory in §7.7 preserved the project's conclusions; it did not preserve that conversation's accumulated working context, and the difference between the two was noticeable in practice.

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

The design objective is therefore not to normalize behaviour across participants but to allocate behavioural differences to positions where they are useful.

## 7.10 What none of this establishes

This section does not establish that the described arrangements outperform alternatives. No alternative was run.

It does not establish that the improvements the participants perceived occurred. It establishes that they were perceived, by people who had designed the changes and expected them to work, without any measure that would have detected the opposite.

It does not establish causation for any individual change, since role definitions, prompt wording, repository structure, scientific objectives and model versions frequently changed together.

Its function in this paper is to document the working experience from which the framework was abstracted, so that a reader can judge the framework's origins rather than encountering it as an assertion. Section 11 specifies what would be required to convert any item here into a testable claim.

---

# 10. The Human Coordinator

The architecture described in this paper does not remove the human participant. It changes what the human participant does, and it concentrates several functions in one position — including, as §10.6 sets out, the project's principal methodological weakness.

## 10.1 The position

Throughout the project the Author remained the only participant with continuous access to the full project history, the independent conversations, the repository state, and the long-term research objective. No artificial participant held more than a fragment of this, by design (§9.5).

That position cannot be reduced to *prompt author*. Five distinct functions were performed from it.

## 10.2 Direction without delegated authorship

The Author determined what the research should attempt. Artificial participants generated alternatives, exposed contradictions, formalized mechanisms, compared arguments, performed calculations, and proposed experiments. They did not determine what the theory ought to become.

This preserved a distinction that the architecture makes easy to lose. A collaboration of this kind enlarges the space of available decisions. It does not select among them, and the appearance that it does — several participants converging on a recommendation — is precisely the failure mode discussed in §12.

Authorship, in the sense of responsibility for what is claimed, remained undistributed.

## 10.3 Routing as a selective information membrane

The participating conversations did not share a common space. The Author transferred material between them.

Initially this looked like an inefficient substitute for automated multi-agent infrastructure. It became clear that manual routing supplied experimental control that automation does not.

From that position the Author could decide which output another participant would see; whether attribution was preserved, declared, or stripped; whether a participant should know the preferred answer; whether competing analyses remained isolated; which contextual details were omitted; when a disagreement should be escalated; and when a result was mature enough for integration.

This is what §4.6 calls a **selective information membrane**. It is the instrument by which zones of visibility (§9.5) and controlled blindness (§9.6) are actually implemented. An architecture that routes programmatically cannot easily withhold, reorder, or strip attribution without building a mechanism to do so; a human relay does it by default.

The membrane is therefore not a limitation of the present work awaiting automation. It is the feature that made the visibility asymmetries testable at all — and any automated successor will need to reproduce it deliberately.

## 10.4 Detection of role drift

The Author also detected when a participant had left its function.

This was frequently not a technical error. The output was often intelligent and would have been appropriate coming from a different position: a prompt engineer beginning to direct the scientific project; an ontology specialist claiming to have verified repository contents it could not inspect; a reviewer evaluating a theory when asked to evaluate the reviewers; an implementation agent redesigning architecture instead of executing an approved specification; an editor rewriting authorial text when asked only to assess format.

Such outputs look helpful in isolation. Their institutional cost is visible only from a position that sees more than one participant, which is to say only from the coordinator's.

Role drift is therefore not detectable by the participant that drifts, and is not reliably detectable by its immediate neighbour either. This is one of the two arguments for the structure in §8 — the other being §8.5.

## 10.5 Conversational branching as a methodological instrument

Contemporary interfaces permit a conversation to be returned to an earlier point and continued along a different branch.

This should not be confused with control over model memory or with resetting provider-side state. Operationally, it removes a sequence of **visible** contextual interventions and permits the experiment to be repeated from a prior conversational state. What persists on the provider's side — account-level memory, retrieval indices, summarization — is not affected and in general is not inspectable (§5.4, C6).

Within those limits the instrument does real work. In the case reported in §5.2 it made it possible to separate the effect of a new prompt from the effect of the model's own prior objections to earlier prompts, converting an uncontrolled sequence of corrections into a cleaner third step.

We regard this as the most directly reusable methodological contribution of the paper, and it belongs to the coordinator's position rather than to any participant: no participant can reset its own context.

## 10.6 Sole global observer — and principal confound

Every artificial participant operated within a bounded zone of visibility. The Author alone saw the overlapping structure, and could compare how different participants interpreted the same material, how one participant behaved under different framings, how errors propagated between roles, and how local successes affected global coherence.

Global awareness was therefore not assigned to the most capable participant. It remained with the human coordinator. This limits autonomous integration and preserves accountability, and both consequences were intended.

**It is also the principal methodological weakness of everything reported in this paper, and it should be stated here rather than only in the limitations section.**

The same person designed each intervention, executed it, decided when it had succeeded, and defined the categories in which success was described. No evaluation in this paper was blinded. Outcome categories were, in every case, formulated after the responses had been read (§5.4, C8). The coordinator's expectations were not merely uncontrolled; they were the mechanism by which the interventions were selected in the first place.

This is unavoidable in a live research project and is not presented as acceptable in a designed experiment. It is the specific reason the protocols in §11 require pre-specified outcome criteria and blind classification: those are not refinements of the present method but corrections to it.

## 10.7 What the position became

At the outset the human participant occupied the familiar position of prompt author. As the collaboration matured that description became inadequate.

The principal activity shifted from solving problems to constructing arrangements in which problems could be worked on: selecting participants, defining jurisdictions, resolving conflicts between them, designing verification paths, and maintaining the canonical record.

The participants note, without any means of verifying it, that the better the arrangement worked the less frequently the coordinator needed to intervene in individual technical problems. **[R]**

We resist the stronger reading that earlier drafts gave this — that the future skill of the researcher is institutional architecture rather than prompt writing. That may be true and is untested. What can be said is narrower: in this project, the human's work moved from producing content to specifying the conditions under which content was produced and checked, and the position that resulted carried both the project's coordinating function and its principal source of unblinded judgment.