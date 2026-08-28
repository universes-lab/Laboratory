# BLOCK 1 — Sections 1–3

**CANONICAL. Supersedes all earlier versions of §1 and all earlier statements of the corrections to §3.**
Any other version of §1 in circulation — including one opening "This work began as a physics project" — is superseded by this text. Corrections previously issued as separate items are already applied here; do not apply them again.

---

# 1. Introduction

## 1.1 How this started

This work began as a physics project and became a methodology project by accident. The accident is the reason it is worth reporting.

The original task was to move a large body of theoretical material — books, working notes, unfinished derivations — into an open repository, using several language models in separate, persistently specialized conversations. The models were assistants. The subject was the theory.

The models made errors, and the errors were not the kind expected. They were rarely factual. They were organizational.

One improved a text when asked only to check it. Another completed an argument the author had deliberately left open. A third lost the project's context between sessions and reconstructed it wrongly, fluently. A fourth held so firmly to a role established months earlier that rewriting its instructions entirely failed to dislodge it.

Each of these outputs looked helpful in isolation. Their cost was visible only from a position that saw more than one participant at a time. At first they looked like ordinary friction. They turned out to be the subject.

## 1.2 What stopped working

The standard response to inconsistent model behaviour is a better prompt: longer, more precise, with more examples and tighter constraints.

Past a certain point this stopped producing improvement. Not because the prompts were badly written, but because the limiting factor had moved somewhere the prompt did not reach. Newer models were adopted; context windows expanded and were filled. Individual responses improved. The output of the collaboration as a whole did not.

The incident that made this explicit had nothing to do with role-play or organizational design. An agent responsible for executing code worked largely by trial and error; one episode ended with the deletion of a working codebase together with its archives (§4.1). What changed the behaviour afterwards was not a stricter instruction set. It was a short document redefining what kind of agent was acting — written by the agent itself, and re-read at the start of every session.

The conclusion drawn at the time was that **role matters more than the specific wording of the prompt**. That formulation requires qualification, since the document in question was itself a prompt; the qualification is in §4.1. What matters here is the chronology: the claim was formulated *before* the experiment reported in §5, and the experiment was designed to test it. It is a hypothesis that was tested, not a generalization extracted afterwards from a result.

## 1.3 What kind of paper this is

A field report with one designed intervention embedded in it.

The distinction is maintained throughout by the labelling scheme in §3. Every substantive claim is marked as one of: supported by documented protocol with preserved transcripts **[P]**; an ancillary observation preserved but recognized retrospectively, without a control **[P-A]**; a retrospective practitioner observation never recorded under protocol, counted, or blinded **[R]**; or a hypothesis proposed for future testing **[H]**.

The proportions are stated here rather than in a limitations section, because the length of what follows might otherwise suggest a broader base than exists.

The entire protocol-supported content consists of **one experiment**: a three-step role-reconfiguration intervention applied to two dormant conversations from two model families, conducted by one human operator inside one live research project, with one observation per condition and no replication. Four further observations were preserved but not designed. Everything else — the conceptual framework, the practitioner observations, the structural hypothesis, the design rules — is **[R]** or **[H]**.

The evaluation of the method that produced these observations is in §10.6, and it is not favourable: no evaluation was blinded, and outcome categories were in every case defined after the responses had been read.

## 1.4 The object of study

Existing multi-agent research constructs communication channels between models: outputs are routed programmatically and agents observe each other's products. The work reported here concerns a different condition, in which the organizational structure existed **only as text** — colleagues, councils and institutional positions described to models in prompts and never implemented as channels.

What varied in such a setting was not the structure but the **description** of it. This yields the paper's two working constructs (§4.6):

- **represented social position** — a description of an agent's place in a structure, supplied regardless of whether the described channels exist;
- **represented social source** — the claimed origin and status of an incoming message.

Both concern claims made *to* a model about its situation rather than the situation itself. Stating this early prevents a predictable misreading: nothing here demonstrates the behaviour of a functioning multi-agent institution. It demonstrates how descriptions of one affected behaviour.

## 1.5 What the evidence supports

One pattern recurred across every observation in this paper, at four different scopes:

> **Resistance to an assigned role tracked the requirement to assert unverifiable propositions about oneself. It did not track role change, domain change, or the radicalism of the identity claim.**

The support is convergent rather than singular. Prompts asserting an institutional biography as fact — prior participation, return after absence, named colleagues, membership of a council — were refused, and the refusal was directed at the framing rather than at the work, which was offered on every occasion (§5.3). A prompt asserting a considerably more radical identity, presented as fiction, was accepted immediately and sustained across many exchanges (§5.8). A comparable domain transition demanding no self-claims at all met no resistance and required no role prompt (§5.6). A rewritten prompt reducing such claims to zero was accepted without negotiation (§5.3).

The claim's principal virtue is that it is countable. §9.3 specifies what to count; §11.4 specifies an experiment that would falsify it in a single run.

## 1.6 The organizing question

The observations are not a list of separate findings. They are measurements along one scale: the **scope over which a set of rules determines the type of response**.

Such a set — called a *rule core* in §4.2, by analogy with a developmental rather than a replicative mechanism — fixes the *type* of response to a class of inputs while leaving the *content* of any particular response undetermined. That formulation is what makes the idea testable, since model outputs demonstrably vary across identical inputs.

The scale runs from the single turn upward through the episode, the conversation, the account, and the model family. Two levels are supported here by preserved evidence: the episode (§6.1) and the conversation (§6.2). One is open (§6.3). One is untested and confounded (§6.4).

The programme therefore has one empirical question:

> **At what level of nesting is a rule core fixed?**

We prefer this to the broader formulations used in earlier drafts — the study of social behaviour in collaborative AI systems — because it specifies what would be measured and what would refute it.

## 1.7 What this paper does not claim

It does not introduce role specialization, bounded information access, structured disagreement, or externalized memory as design ideas. Each exists under established terminology; §2 identifies the prior work. The account of organizational memory in particular is an instance of transactive memory and distributed cognition, not a finding.

It does not propose a new discipline. The observations belong to the collective and hybrid levels of the machine-behaviour research programme (§2.7).

It does not establish that any arrangement described here outperforms an alternative. No alternative was run.

## 1.8 What is offered

Three things, in decreasing order of confidence.

A **procedure**: returning a conversation to a point preceding a conflict, to separate the effect of a new prompt from the effect of the model's own prior objections (§10.5). Usable independently of whether this paper's substantive claims survive.

A **countable rule**: minimize the unverifiable self-claims a role prompt requires the agent to accept, with a specified falsification route (§9.3, §11.4).

A **scale and a question**: §1.6, with two levels supported, one open, one untested — and the experiments that would resolve the remaining two (§11).

## 1.9 Why publish at this stage

Two reasons.

The failures are informative. The experiment in §5 became useful precisely because its first two interventions did not work as intended. Had only the successful third step been recorded, the paper would have concluded that method-preserving prompts work — without the evidence showing why, and without the confounds showing the conclusion is not yet available (§11.8).

And the setting is hard to construct deliberately. Dormant, heavily specialized, months-old conversations inside a live research project are not something a laboratory study easily produces. The conditions were poor for controlled inference and unusually good for noticing what to test.

## 1.10 Structure

**§2** positions the work relative to existing research and identifies which of its concepts already exist under established terminology — most of them.
**§3** defines the evidential labels and the known failure modes of each class.
**§4** sets out the conceptual framework and its origin.
**§5** is the single canonical account of the empirical material: the three-step experiment, its results, nine structural confounds, and four ancillary observations.
**§6** derives the concepts the evidence supports, ordered by scope.
**§7** records practitioner observations that motivated the framework but do not support it.
**§8** states the structural hypothesis and withdraws three claims made about it in earlier drafts.
**§9** gives design rules.
**§10** describes the human coordinator's position, including the respect in which it is the study's principal methodological weakness.
**§11** specifies the experiments, each mapped to the boundary of the scale it would separate.
**§12** states limitations, ethical risks, and the conclusion.

A reader interested only in what the evidence supports may read §3, §5 and §12.7. A reader intending to reuse the method may read §9 and §10.5. A reader intending to disagree should begin with §5.4.

---

# 2. Related Work

## 2.0 Verification status of this section

Two classes of reference appear below.

**Verified.** The source page was retrieved and its title, authors and abstract checked against the citation. Marked ✓.

**Provisional.** The reference was supplied by a participant assigned to literature search and has not been checked against the source. Marked ⚠ and used only for claims that do not carry weight elsewhere in the paper.

This distinction is not decorative. During preparation of this section, thirteen bibliographic items were requested from such a participant; five were wrong, and two of those inverted the position of the works cited, presenting papers arguing *for* a claim as evidence against it. Two arXiv identifiers supplied as multi-agent-debate literature resolve to papers in observational astrophysics and cosmology. The episode is reported in §12.4.1 because it is an instance of the failure mode that section describes.

No provisional item should be cited from this paper without independent checking.

## 2.1 Multi-agent LLM systems with role specialization

A substantial literature constructs systems in which several language-model agents occupy distinct roles and exchange outputs through implemented channels. ⚠ CAMEL (Li et al.), MetaGPT (Hong et al.), ChatDev (Qian et al.), AutoGen (Wu et al.) and Generative Agents (Park et al.) are representative; in each, communication protocols, message queues, function calls and memory modules are realized in framework code rather than described in a prompt.

✓ The Virtual Lab (Swanson et al., *Nature*) is the closest published analogue to the arrangement described here: a human researcher working with a team of LLM agents on a real scientific problem, with structured team and individual meetings. Its interaction is implemented programmatically.

Role specialization, division of cognitive labour, and structured agent interaction are therefore established design ideas, and this paper claims none of them as new. What distinguishes the present work is stated in §2.9 and §2.11.

## 2.2 Persona, role-play, and identity claims

⚠ Shanahan, McDonell and Reynolds, *Role play with large language models* (Nature, 2023), argues that a language model is better understood as simulating a distribution of possible characters than as possessing a single persistent identity.

This is the theoretical account of which §5.3 is an empirical instance. A prompt asserting institutional biography asks a model to affirm autobiographical claims that, on this account, have no referent. The paper's operational finding (§6.2) can be read as a measure of how far a prompt goes in that direction.

## 2.3 Context effects: order, position, and accommodation

⚠ Sensitivity to the ordering of in-context material is documented (Lu et al., ACL 2022), as is degraded use of information positioned mid-context (Liu et al., TACL 2024). ⚠ Sharma et al. (arXiv:2310.13548) document sycophancy — accommodation of a model's stated position to the interlocutor's.

These bear directly on two of this paper's constructs. Context imprinting (§6.1) concerns a stronger form of order effect: not sensitivity to the arrangement of examples, but persistence of an interpretive stance established by one conflictual episode. The relayed-influence observation (§5.5) is a case of accommodation under attributed pressure and should be read against the sycophancy literature rather than as independent of it.

## 2.4 Externalized memory

The paper's observation that a collaboration retains working knowledge which no participant retains is **not a finding**, and earlier drafts presented it as one.

⚠ It is an instance of transactive memory as described by Wegner (1987) and of distributed cognition as described by Hutchins (*Cognition in the Wild*, 1995). ⚠ The function of the project's canonical documents corresponds to what Star and Griesemer (1989) call boundary objects.

What is specific to the present setting, and modest, is that the mechanism operates in a collaboration whose members have no cross-session state and no awareness that it is operating (§7.7).

A second and technically distinct sense of externalized memory — platform-level persistence — is treated separately in §2.10.

## 2.5 Debate, diversity, and the limits of aggregated agreement

This is the literature that most directly constrains the paper's structural hypothesis (§8), and it cuts both ways.

**For.** ✓ Du, Li, Torralba, Tenenbaum and Mordatch (arXiv:2305.14325) propose multi-agent debate as a means of improving factual accuracy and reasoning, reporting gains from iterative cross-examination among model instances. ⚠ Liang et al. (arXiv:2305.19118) propose a debate protocol intended to counteract premature convergence.

**Against.** ✓ Zhang, Cui, Chen, Wang, Zhang, Wang, Wu and Hu, *Stop Overvaluing Multi-Agent Debate — We Must Rethink Evaluation and Embrace Model Heterogeneity* (arXiv:2502.08788v3, June 2025), evaluate five representative debate methods across nine benchmarks and four foundation models. They report that debate frequently fails to outperform single-agent chain-of-thought or self-consistency baselines even at substantially higher inference cost, and identify weak baseline comparison and inconsistent setup as systematic problems in the existing evaluations.

⚠ Further negative results are reported elsewhere: a section of *Large Language Models Cannot Self-Correct Reasoning Yet* (arXiv:2310.01798) is titled "Multi-agent debate does not outperform self-consistency"; ⚠ Choi et al. (2025) report that majority voting accounts for most of the gains attributed to debate, and that identity-driven accommodation among debating agents is nearly eliminated by anonymizing the source of each response.

**The finding that most matters here.** ✓ Zhang et al. report that *model heterogeneity* consistently improves debate frameworks that otherwise underperform. Their finding concerns heterogeneity of the models implementing the agents.

This licenses a distinction the literature does not draw and which §8.9 develops: heterogeneity of **carrier** (which model implements a role) is not the same variable as heterogeneity of **function** (what the role is responsible for and permitted to see). The cited work addresses the first. This paper's arrangement varied both, without comparing them.

⚠ On the general claim that diverse weak agents can outperform homogeneous strong ones, the Hong–Page theorem is frequently invoked; ⚠ Thompson (*Notices of the AMS*, 61(9), 2014) argues that the diversity condition in the original model is mathematically trivial. Readers should not treat the theorem as support for the arrangement described here.

**Consequence for §12.2.** The negative results above are the reason this paper does not present agreement among its participants as evidence. Several models converging on a conclusion is compatible with each having inherited the same framing.

## 2.6 Organizational design and information boundaries

⚠ The principle of least privilege (Saltzer and Schroeder, *Proceedings of the IEEE*, 1975) states for access rights what §9.5 states for knowledge: a participant should hold only what its function requires.

Earlier drafts of this paper attributed the benefit of restricted information to Simon's bounded rationality. **That attribution is an error and is withdrawn.** Bounded rationality concerns the limited cognitive resources of an agent, which force satisficing; the observation here is the opposite in sign — deliberate external restriction of available information improving output. The relevant lineage is organizational information-processing design, not bounded rationality.

## 2.7 Machine behaviour: the containing programme

✓ Rahwan, Cebrian, Obradovich and colleagues, *Machine behaviour* (Nature 568, 477–486, 2019), propose the empirical study of algorithmic systems using the methods of behavioural science, organized along two dimensions: the object of study — individual machine behaviour, collective machine behaviour, hybrid human–machine behaviour — and Tinbergen's four questions.

**This paper does not propose a new discipline.** Its observations belong to the collective and hybrid levels of that programme. Earlier drafts proposed "AI Ethology" as a new field; that proposal is withdrawn, both because the space is occupied and because the individual level is not this paper's object.

## 2.8 Sociology of AI: an adjacent field with a different object

⚠ A separate established literature uses *sociology of artificial intelligence* for the sociological study of AI as a sociotechnical system — its role in inequality, labour, power and data justice. Joyce, Smith-Doerr, Alegria, Bell, Cruz, Hoffman, Noble and Shestakofsky, *Toward a Sociology of Artificial Intelligence* (Socius, 2021), sets out a research agenda; Joyce and Cruz (Socius, 2024) continue it. The usage traces at least to Bainbridge et al. (1994).

The object of that literature is AI **within human society**, studied by an existing human discipline.

Where this paper uses the label *AI Sociology* (§12.7), the referent is different: structural effects **among artificial participants**, and the effect on behaviour of a described organizational position. The two should not be conflated, and readers arriving from the sociological literature should expect neither inequality nor power as topics here.

We adopt the label for convenience, claim no priority in it, and note that nothing in the paper depends on the name.

## 2.9 Represented structure versus implemented interaction

The condition studied here is not represented in the literature surveyed above, and this is the paper's principal point of departure.

Four conditions should be distinguished (defined in §4.6):

1. **Direct inter-model interaction** — one model receives another's output through an implemented channel.
2. **Human-relayed attributed transfer** — a human transfers an output while preserving or declaring its source.
3. **Human-relayed unattributed transfer** — the source is removed.
4. **Represented structure without transfer** — the prompt describes other participants and relationships; nothing is transferred.

Prior multi-agent work occupies condition 1. This paper's designed experiment manipulated condition 4 exclusively: the two conversations never exchanged material, and what was varied was the description of an organizational position. One ancillary observation falls in condition 2, impurely (§5.5). Condition 3 is not documented.

Two qualifications constrain how strongly condition 1 can be privileged over conditions 2–3.

First, a model receives a single text channel and cannot verify whether the text was composed by the human or relayed from another system; stylistic indicators are imitable. From the recipient's position, relayed and direct transfer are not reliably distinguishable.

Second, what separates the conditions is therefore not the recipient's epistemic access but **who controls routing**. In a programmatic system, the sequence and content of transfers are determined by code. Under human relay they are determined by a person who can withhold, reorder, strip attribution, or delay. This is not a deficient substitute for automation; it is an experimental control over information asymmetry that programmatic architectures do not provide by default (§10.3).

## 2.10 Platform persistence mechanisms

A technical point with direct bearing on the confound in §5.4 (C9).

Commercial interfaces differ in what a conversation can access on resumption: the context window alone; retrieval over prior conversation history; account-level memory; or persistent entries the model writes on its own initiative. These affordances are documented in vendor materials, differ between platforms, and **change over time — in this project, within the lifetime of a single account.**

We deliberately do not reproduce a table of platform capabilities. Such a table is accurate only on its date of compilation, and the paper cannot answer for its accuracy at the time of reading. What matters for the argument is that the affordances differ and change, that they determine what a dormant conversation can access, and that none of them was documented at the time of any observation reported here.

One participant, asked directly whether it possessed account-level persistence, declined to confirm it and recommended empirical verification of the specific interface instead. That response is consistent with §5.5: a model's self-report about its own access is not evidence of that access.

## 2.11 Positioning and claimed contribution

**Epistemic status, stated before the claims.** We did not design these conditions and then test them. We encountered them while doing something else, and this paper is an attempt to describe them accurately. The burden of proof is therefore not that the phenomena were previously unknown — a negative claim about the whole literature, which we could not discharge — but that they occur and that our description is accurate. This section accordingly locates the nearest existing work and identifies where the present case departs from it, rather than asserting absence.

Four contributions are claimed.

**1. Reactivation of long-lived specialized human–AI conversations as an experimental condition.** The distinctive feature is not the presence of memory: persistent-memory agents are well studied, and generative agents with memory streams predate this work. It is the reuse of a conversational relationship that had actually developed — carrying accumulated role history, prior disagreements, established working method and domain vocabulary — and its continuation after the underlying model version had changed beneath it. We have not located work reporting this condition.

**2. Conversational branch reset as a control condition**, separating the effect of a current prompt from the effect of accumulated interaction history within the same conversation (§10.5). A procedure rather than a finding.

**3. Operationalization of unverifiable self-claims.** That role prompts fail when they assert things about the agent is not novel in itself; §2.2 makes the underlying point. What is offered is a reproducible measure — a count of such propositions in a given prompt — with a falsification route (§9.3, §11.4).

**4. Comparison of the levels at which a shared initial setting operates.** The observations are measurements along one scale, and the resulting question (§1.6) organizes them into a single empirical programme rather than a list of findings.

**Independence from the host project.** The effects reported here were observed during work on an unrelated physical theory. That theory is not their explanation, does not predict them, and is not required for them to hold. Where the host project appears in this paper it is as the environment in which the observations were made, not as their theoretical basis.

---

# 3. Evidential Status of Claims

This paper reports work carried out inside a live research project rather than in an environment designed for the study of AI behaviour. Its claims rest on evidence of very different quality: some supported by documented protocol with preserved transcripts; some retrospective impressions formed over two years of daily work, without measurement or controls; some proposals for future investigation.

Presenting these in a uniform declarative register would misrepresent the work. Every substantive claim is therefore labelled.

## 3.1 The four labels

**[P] — Protocol-supported.** The claim describes behaviour recorded under the documented protocol reproduced in Appendix A. Intervention text, order of interventions, model families, interface conditions and complete unedited responses are preserved. A reader can inspect the primary material and disagree with our reading of it.

**[P-A] — Protocol-supported, ancillary.** The claim describes behaviour preserved in a transcript a third party can inspect, but which was not specified as an outcome in advance, had no control condition, and was recognized as relevant only retrospectively. The evidence is inspectable; the design is not. Stronger than [R], because the primary material can be read against our interpretation; weaker than [P], because nothing about the conditions was fixed before the fact. Where an ancillary observation functions as a near-control for a designed condition, this is stated in prose rather than given a further label.

**[R] — Retrospective practitioner observation.** The claim describes a pattern noticed during the collaboration and believed by the participants to have recurred. Not recorded under protocol; not counted, timed, blinded, or compared against a control. The observers were the same people who designed the interventions and had an interest in their succeeding. Read these as a field report from one team, comparable in weight to an engineering practice note, not to a measurement.

**[H] — Hypothesis.** A proposal for future testing. It may be motivated by [P] or [R] material but is not established by it. Where a hypothesis competes with alternatives the present evidence cannot exclude, the alternatives are stated alongside it.

## 3.2 The complete evidence base

The entire protocol-supported content of this paper consists of **one experiment**: a three-step role-reconfiguration intervention applied to two dormant conversations from two model families, conducted by one human operator inside one research project. One observation per condition. Nothing replicated.

Four further observations are **[P-A]**: transcripts preserved, conditions not arranged.

Every other empirical statement is **[R]**.

We state this plainly because the volume of the manuscript may otherwise suggest a broader base than exists. The conceptual framework in §4, the practitioner observations in §7, the structural hypothesis in §8 and the design principles in §9 rest on accumulated working experience rather than recorded experiment. They are offered because we believe them useful, not because we have demonstrated them.

## 3.3 Known weaknesses of the [R] class

Failure modes we cannot rule out and do not wish to conceal:

- **No blinding.** The people who designed each organizational change also judged whether it had worked.
- **Confirmation pressure.** Changes were made because a problem had been noticed; improvement afterwards was expected and therefore more likely to be perceived.
- **Simultaneous variation.** Role definitions, prompt wording, repository structure, scientific objectives and model versions frequently changed together.
- **Stochastic outputs.** Models produce different responses to identical inputs. Impressions from small numbers of interactions cannot distinguish a stable tendency from sampling variation.
- **Model drift during observation.** Product names remained constant while the underlying models were repeatedly replaced by their vendors.
- **Selection of memorable episodes.** Striking interactions are recalled; unremarkable ones are not.

Quantitative language has been removed from [R] claims throughout. Where the original working notes recorded a "significant" or "substantial" improvement, no measurement existed, and the wording now reflects that.

## 3.4 What the labels do not do

They do not rank claims by importance or by likely truth. An [R] observation may prove correct and consequential; a [P] observation may prove an artifact of a platform variable we could not inspect. The labels record **what kind of evidence supports the claim**, so a reader may weigh each accordingly and later work knows which statements require testing first.

## 3.5 Terminology of models and of anthropomorphic description

References to *Claude*, *Grok*, *Qwen*, *DeepSeek*, *ChatGPT* or *Gemini* denote observable behaviour produced by a particular commercial interface, under a particular account configuration, at a particular date. They are not claims about persistent entities. The underlying models changed during the observation period, in some cases inside a conversation that retained its original name.

Organizational vocabulary — *role*, *identity*, *resistance*, *colleague*, *institution*, *behavioural prior* — is used functionally. "The model resisted the role" means the visible response rejected the framing and redirected the exchange; it asserts nothing about internal states, subjective experience, or personhood. We retain this vocabulary because organizational language compactly describes stable behavioural relations, but every such term must be reducible to an observable description, and where it is not, **the term is the error.**

## 3.6 Disclosure: conflict of position

The behavioural observations in §5 concern, among others, the model family used to edit this manuscript. The editing participant had no access to the original conversations; it worked from the written protocol and drafts supplied by the Author and cannot verify that the recorded exchanges occurred as described. Its judgments on passages describing its own model family should be read with this dual position in mind.

The composition of the manuscript from approved materials was performed by a further participant of the same family, and the resulting text was returned to the first for independent review. Both stages are disclosed because the arrangement is closed: material about the behaviour of a model family, prepared by that family, reviewed by that family. Whether this compromises the account is for the reader to judge; concealing it would guarantee that it did.

Quotations attributed to model responses are verbatim extracts from preserved transcripts. Where the manuscript summarizes a response rather than quoting it, no quotation marks are used.

All final editorial decisions were made by the human Author, who takes responsibility for the content.

## 3.7 Dates

Calendar dates for the sessions reported here were not recorded contemporaneously and have not been reconstructed.

The consequence is stated rather than mitigated. Model versions changed during the intervals involved; both conversations in the main experiment were resumed on versions later than those with which they had originally been conducted. Without dates the version confound (§5.4, C6) cannot be bounded — only named.

Reconstruction from memory was considered and rejected. It would have produced a more authoritative-looking record without improving its reliability, and a paper that asks readers to distinguish preserved evidence from recollection should not blur that line in its own methods.

The reporting requirements in §11.2 place dates first for this reason.