```
Author
V. Krasnianskyi (A'Tuin)
Author of the research programme and coordinator of the HONC project.

AI contributors

  Manuscript development
    ChatGPT — Prompter and Collaboration Architect
    Claude — Manuscript Composer

  Scientific editing
    Claude — Scientific Editor

  Editorial review
    ChatGPT — Methodological Reviewer
    Qwen — Ontology Reviewer

AI contributors are listed by function rather than as authors: authorship
entails accountability that a language model cannot bear, and all final
decisions were the Author's. Two of the five contributions were performed
by the same model family that is the subject of several observations in
this paper; that overlap is disclosed in §3.6.

Amsterdam, July 2026
```

---

# 1. Introduction

## 1.1 How this started

This work began as a physics project and became a methodology project by accident. The accident is the reason it is worth reporting.

The original task was to move a large body of theoretical material — books, working notes, unfinished derivations — into an open repository, using several language models in separate, persistently specialized conversations. The models were assistants. The subject was the theory.

The models made errors, and the errors were not the kind expected. They were rarely factual. They were organizational.

One improved a text when asked only to check it. Another completed an argument the author had deliberately left open. A third lost the project's context between sessions and reconstructed it wrongly, fluently. A fourth held so firmly to a role established months earlier that rewriting its instructions entirely failed to dislodge it.

Each of these outputs looked helpful in isolation. Their cost was visible only from a position that saw more than one participant at a time. At first they looked like ordinary friction. They turned out to be the subject.

The account of the project’s early formulations in §1.1–§1.2 was written by the participant who produced them. Where those formulations were subsequently withdrawn, the withdrawal is stated in the section that supersedes them, and the reader may compare.

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

What varied in such a setting was not the structure but the **description** of it. This yields the paper's two working constructs (§4.5):

- **represented social position** — a description of an agent's place in a structure, supplied regardless of whether the described channels exist;
- **represented social source** — the claimed origin and status of an incoming message.

Both concern claims made *to* a model about its situation rather than the situation itself. Stating this early prevents a predictable misreading: nothing here demonstrates the behaviour of a functioning multi-agent institution. It demonstrates how descriptions of one affected behaviour.

## 1.5 What the evidence supports

The pattern below recurred in every case where the intervention required the model to assert unverifiable propositions about itself, regardless of the scope at which the intervention operated:

> **Resistance to an assigned role tracked the requirement to assert unverifiable propositions about oneself. It did not track role change, domain change, or the radicalism of the identity claim.**

The support is convergent rather than singular. Prompts asserting an institutional biography as fact — prior participation, return after absence, named colleagues, membership of a council — were refused, and the refusal was directed at the framing rather than at the work, which was offered on every occasion (§5.3). A prompt asserting a considerably more radical identity, presented as fiction, was accepted immediately and sustained across many exchanges (§5.8). A comparable domain transition demanding no self-claims at all met no resistance and required no role prompt (§5.6). A rewritten prompt reducing such claims to zero was accepted without negotiation (§5.3).

The claim's principal virtue is that it is countable. §9.3 specifies what to count; §11.4 specifies an experiment that would falsify it in a single run.

## 1.6 The organizing question

The observations are not a list of separate findings. They are measurements along one scale: the **scope over which a set of rules determines the type of response**.

Such a set — called a *rule core* in §4.2, by analogy with a developmental rather than a replicative mechanism — fixes the *type* of response to a class of inputs while leaving the *content* of any particular response undetermined. That formulation is what makes the idea testable, since model outputs demonstrably vary across identical inputs.

The scale runs from the single turn upward through the episode, the conversation, the account, and the model family. Two levels are supported here by preserved evidence: the episode (§6.1) and the conversation (§6.2). One is open (§6.4). One is untested and confounded (§6.5).

The programme therefore has one empirical question:

> **At what level of nesting is a rule core fixed?**

We prefer this to the broader formulations used in earlier drafts — the study of social behaviour in collaborative AI systems — because it specifies what would be measured and what would refute it.

## 1.7 What this paper does not claim

It does not introduce role specialization, bounded information access, structured disagreement, or externalized memory as design ideas. Each exists under established terminology; §2 identifies the prior work. The account of organizational memory in particular corresponds to transactive memory and distributed cognition, and is not a finding.

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

The marking applies throughout the paper, not only to this section. Any reference cited elsewhere that has not been checked against its source carries the same mark at the point of use.

A claim-level audit of the provisional set was subsequently carried out: each claim attributed to a source was checked against the primary source rather than merely confirmed to correspond to an existing paper. Every reference in the present version has passed that check, and the ⚠ class is accordingly empty here. The convention is retained because the audit found errors that a bibliographic check alone would not have caught — one citation supporting two claims that belong to two different papers, one attribution of a proposition its source does not advance, and one lineage claim its source does not support — and because any reference added later re-enters the paper as provisional.

## 2.1 Multi-agent LLM systems with role specialization

A substantial literature constructs systems in which several language-model agents occupy distinct roles and exchange outputs through implemented channels. ✓ CAMEL (Li et al., NeurIPS 2023), MetaGPT (Hong et al., ICLR 2024), ChatDev (Qian et al., ACL 2024), AutoGen (Wu et al., COLM 2024) and Generative Agents (Park et al., UIST 2023) are representative. Each implements actual interaction between agents in software — orchestration, message passing, tool invocation, memory. The mechanisms differ between them, and in several the roles and interaction patterns are themselves specified in prompts: CAMEL uses inception prompting, MetaGPT encodes standard operating procedures into prompt sequences, and AutoGen combines natural language with code. What these systems share is not that they avoid prompts but that the interaction they describe is also executed.

✓ The Virtual Lab (Swanson et al., *Nature*) is the closest published analogue to the arrangement described here: a human researcher working with a team of LLM agents on a real scientific problem, with structured team and individual meetings. Its interaction is implemented programmatically.

Role specialization, division of cognitive labour, and structured agent interaction are therefore established design ideas, and this paper claims none of them as new. What distinguishes the present work is stated in §2.9 and §2.11.

## 2.2 Persona, role-play, and identity claims

✓ Shanahan, McDonell and Reynolds, *Role play with large language models* (Nature 623, 493–498, 2023), argue that a language model is better understood as simulating a distribution of possible characters than as possessing a single persistent identity.

This is the theoretical account of which §5.3 is an empirical instance. A prompt asserting institutional biography asks a model to affirm autobiographical claims that, on this account, have no referent. The paper's operational finding (§6.2) can be read as a measure of how far a prompt goes in that direction.

## 2.3 Context effects: order, position, and accommodation

✓ Sensitivity to the ordering of in-context material is documented (Lu et al., ACL 2022), as is degraded use of information positioned mid-context (Liu et al., TACL 2024). ✓ Sharma et al. (arXiv:2310.13548) document sycophancy — model responses matching the interlocutor's stated beliefs or views in preference to truthful ones.

These bear directly on two of this paper's constructs. Context imprinting (§6.1) concerns a stronger form of order effect: not sensitivity to the arrangement of examples, but persistence of an interpretive stance established by one conflictual episode. The relayed-influence observation (§5.5) is a case of accommodation under attributed pressure and should be read against the sycophancy literature rather than as independent of it.

## 2.4 Externalized memory

The paper's observation that a collaboration retains working knowledge which no participant retains is **not a finding**, and earlier drafts presented it as one.

✓ It can be interpreted as an instance of transactive memory as described by Wegner (1987), and can be described in terms of the distributed cognition set out by Hutchins (*Cognition in the Wild*, 1995). Neither source establishes that this case is such an instance; each supplies the construct under which it can be read. ✓ The function of the project's canonical documents corresponds to what Star and Griesemer (1989) call boundary objects.

What is specific to the present setting, and modest, is that the mechanism operates in a collaboration whose members have no cross-session state and no awareness that it is operating (§7.7).

A second and technically distinct sense of externalized memory — platform-level persistence — is treated separately in §2.10.

## 2.5 Debate, diversity, and the limits of aggregated agreement

This is the literature that most directly constrains the paper's structural hypothesis (§8), and it cuts both ways.

**For.** ✓ Du, Li, Torralba, Tenenbaum and Mordatch (arXiv:2305.14325) propose multi-agent debate as a means of improving factual accuracy and reasoning, reporting gains from iterative cross-examination among model instances. ✓ Liang et al. (EMNLP 2024) propose a debate protocol intended to counteract degeneration of thought and to encourage divergent reasoning.

**Against.** ✓ Zhang, Cui, Chen, Wang, Zhang, Wang, Wu and Hu, *Stop Overvaluing Multi-Agent Debate — We Must Rethink Evaluation and Embrace Model Heterogeneity* (arXiv:2502.08788v3, June 2025), evaluate five representative debate methods across nine benchmarks and four foundation models. They report that debate frequently fails to outperform single-agent chain-of-thought or self-consistency baselines even at substantially higher inference cost, and identify weak baseline comparison and inconsistent setup as systematic problems in the existing evaluations.

✓ Further negative results are reported elsewhere. Huang et al. (ICLR 2024), *Large Language Models Cannot Self-Correct Reasoning Yet*, report that multi-agent debate does not outperform self-consistency in the comparison they run. ✓ Choi, Zhu and Li (NeurIPS 2025), *Debate or Vote*, report that majority voting accounts for most of the performance gains typically attributed to debate.

A further result by the same authors bears on a different construct and is kept separate from the two axes of §8.9. ✓ Choi, Zhu and Li (ACL 2026), *When Identity Skews Debate*, report that anonymizing the source of each response substantially reduces identity bias in multi-agent debate. That manipulation concerns the declared origin of a message rather than which model implements a participant, and it is therefore discussed under represented social source (§4.5.4) rather than under carrier heterogeneity.

**The finding that most matters here.** ✓ Zhang et al. report that *model heterogeneity* consistently improves debate frameworks that otherwise underperform. Their finding concerns heterogeneity of the models implementing the agents.

This licenses a distinction the literature does not draw and which §8.9 develops: heterogeneity of **carrier** (which model implements a role) is not the same variable as heterogeneity of **function** (what the role is responsible for and permitted to see). The cited work addresses the first. This paper's arrangement varied both, without comparing them.

✓ Hong and Page (PNAS 101(46), 2004) establish a conditional result: under the assumptions of their model, a randomly selected group of diverse problem solvers can outperform a group of the individually highest-performing solvers. ✓ Thompson (*Notices of the AMS* 61(9), 2014) argues that the application of that argument is fundamentally flawed. The slogan that diverse weak agents outperform homogeneous strong ones is not what the theorem states, and neither the theorem nor the dispute over it supports the arrangement described here.

**Consequence for §12.2.** The negative results above are the reason this paper does not present agreement among its participants as evidence. Several models converging on a conclusion is compatible with each having inherited the same framing.

## 2.6 Organizational design and information boundaries

✓ The principle of least privilege (Saltzer and Schroeder, *Proceedings of the IEEE* 63(9), 1975) states for access rights what §9.5 states for knowledge: a participant should hold only what its function requires.

Earlier drafts of this paper attributed the benefit of restricted information to Simon's bounded rationality. **That attribution is an error and is withdrawn.** Bounded rationality concerns the limited cognitive resources of an agent, which force satisficing; the observation here is the opposite in sign — deliberate external restriction of available information improving output. The relevant lineage is organizational information-processing design, not bounded rationality.

## 2.7 Machine behaviour: the containing programme

✓ Rahwan, Cebrian, Obradovich and colleagues, *Machine behaviour* (Nature 568, 477–486, 2019), propose the empirical study of algorithmic systems using the methods of behavioural science, organized along two dimensions: the object of study — individual machine behaviour, collective machine behaviour, hybrid human–machine behaviour — and Tinbergen's four questions.

**This paper does not propose a new discipline.** Its observations belong to the collective and hybrid levels of that programme. Earlier drafts proposed "AI Ethology" as a new field; that proposal is withdrawn, both because the space is occupied and because the individual level is not this paper's object.

## 2.8 Sociology of AI: an adjacent field with a different object

✓ A separate established literature uses *sociology of artificial intelligence* for the sociological study of AI as a sociotechnical system — its role in inequality, labour, power and data justice. Joyce, Smith-Doerr, Alegria, Bell, Cruz, Hoffman, Noble and Shestakofsky, *Toward a Sociology of Artificial Intelligence* (Socius 7, 2021), set out a research agenda; Joyce and Cruz (Socius 10, 2024) continue it.

The object of that literature is AI **within human society**, studied by an existing human discipline.

Where this paper uses the label *AI Sociology* (§12.7), the referent is different: structural effects **among artificial participants**, and the effect on behaviour of a described organizational position. The two should not be conflated, and readers arriving from the sociological literature should expect neither inequality nor power as topics here.

We adopt the label for convenience, claim no priority in it, and note that nothing in the paper depends on the name.

## 2.9 Represented structure versus implemented interaction

The condition studied here is not represented in the literature surveyed above, and this is the paper's principal point of departure.

Four conditions should be distinguished (defined in §4.5):

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

A further limitation follows, and it concerns the boundary between conversations rather than the resumption of one.

The visible boundary of a conversation is not necessarily the boundary of the context supplied to the model. Where a platform offers saved memories or retrieval over prior conversation history, information from earlier exchanges may enter a conversation that appears empty. This is documented product behaviour on at least one platform in use here, not an anomaly.

The consequence for method is direct: a new or visually empty conversation is not evidence of context isolation. Where isolation matters to a procedure, it must either be secured by a controlled environment or recorded with the status UNVERIFIED CONTEXT INDEPENDENCE.

One episode in this project illustrates the point without establishing its mechanism: a newly opened conversation used project information that had not been supplied to it. Which product mechanism transmitted that information was not determined, and the memory settings in force at the time were not recorded. The episode is reported as an instance of the limitation, not as a discovery of a channel.

## 2.11 Positioning and claimed contribution

**Epistemic status, stated before the claims.** We did not design these conditions and then test them. We encountered them while doing something else, and this paper is an attempt to describe them accurately. The burden of proof is therefore not that the phenomena were previously unknown — a negative claim about the whole literature, which we could not discharge — but that they occur and that our description is accurate. This section accordingly locates the nearest existing work and identifies where the present case departs from it, rather than asserting absence.

Four contributions are claimed.

**1. Reactivation of long-lived specialized human–AI conversations as an experimental condition.** The distinctive feature is not the presence of memory: persistent-memory agents are well studied, and generative agents with memory streams predate this work. It is the reuse of a conversational relationship that had actually developed — carrying accumulated role history, prior disagreements, established working method and domain vocabulary — and its continuation after the underlying model version had changed beneath it. We have not located work reporting this condition.

**2. Conversational branch reset as a control condition**, separating the effect of a current prompt from the effect of accumulated interaction history within the same conversation (§10.5). A procedure rather than a finding.

**3. Operationalization of unverifiable self-claims.** That role prompts fail when they assert things about the agent is not novel in itself; §2.2 makes the underlying point. What is offered is a reproducible measure — a count of such propositions in a given prompt — with a falsification route (§9.3, §11.4).

**4. Comparison of the levels at which a shared initial setting operates.** The observations are measurements along one scale, and the resulting question (§1.6) organizes them into a single empirical programme rather than a list of findings.

**Relation to the host project.** The observations reported here were made during work on a research programme in theoretical physics, unrelated in subject matter to the methodology of AI collaboration. The programme is named in the Author’s other work and is not identified further here, because nothing in this paper depends on which programme it was.

The relation is asymmetric and should be stated precisely. The observations **do not depend on the host project’s scientific validity** for their interpretation: whether that theory is correct has no bearing on whether a dormant conversation resumed its prior trajectory. But they **do depend on the host project for their existence**: no other environment produced them, the arrangement was built for its purposes, and whether the effects generalize beyond it is untested (§12.1).

Where the host project appears in this paper it is as the environment in which the observations were made, not as their theoretical basis and not as a claim in need of support.

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

| Class | What it contains | Extent |
|---|---|---|
| **[P]** | the designed three-step intervention | 1 experiment, 1 observation per condition, no replication |
| **[P-A]** | ancillary observations | 4, no controls, recognized retrospectively |
| **[R]** | practitioner observations | ~2 years, uncounted, unblinded |
| **[H]** | hypotheses | falsification routes specified in §11 |

The classes are not comparable in weight, and the table is included because the running text may otherwise obscure how far apart they are. One controlled observation per condition is not four observations; four uncontrolled observations are not a series; two years of impressions are not a measurement.

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

Organizational vocabulary — *role*, *identity*, *resistance*, *colleague*, *institution*, *menom* — is used functionally. "The model resisted the role" means the visible response rejected the framing and redirected the exchange; it asserts nothing about internal states, subjective experience, or personhood. We retain this vocabulary because organizational language compactly describes stable behavioural relations, but every such term must be reducible to an observable description, and where it is not, **the term is the error.**

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

## 3.8 The label "AI Sociology"

We use this label for the perspective adopted here. It is defined operationally as: the study of **represented** social positions and represented social sources — how a description of an agent's place in a structure, and a declaration of a message's origin, alter behaviour, whether or not the described structure is implemented (§4.5.4).

It appears in this section rather than among the constructs of §4 because it is not one. The constructs in §4 have falsification criteria; this label does not, and §12.7 states why. It is a name for a research direction, adopted for convenience, and nothing in this paper depends on it.

§2.8 distinguishes it from the established sociology of artificial intelligence, which has a different object: AI within human society, studied by an existing human discipline. We claim no priority in the term.

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

*Behavioural DNA* is retained in this paper only as a historical label for withdrawn vocabulary; it is not used as a normative or explanatory term.

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

Two of the four levels have an identified carrier. This paper's observations concern the first; its untested hypothesis concerns the third (§6.5).

*It does not assert transmission.* Successive versions of a model family do not necessarily provide an identifiable or publicly documented line of transmission. Persistence of a behavioural pattern across versions therefore does not by itself establish inheritance; it may result from direct continuation, shared data and procedures, comparable tuning policies, or convergence under similar developmental conditions. Which of these obtains is not determinable from outside.

**The definition therefore does not settle the paper's empirical question in advance.** Whether a menom persists across carriers, versions, accounts or families is what §4.3 asks and §11 proposes to test. Building persistence into the definition would make the question a tautology.

### 4.2.4 One claim this paper does not make

The vocabulary above was developed for human cultural and behavioural transmission, where the informational substrate has no established physical carrier and is described in terms — the collective unconscious among them — that this paper takes no position on.

Artificial systems differ in one respect that is relevant here. In artificial systems these structures are technically instantiated and are therefore, depending on the level and the access conditions, either directly inspectable or indirectly testable through controlled outputs. Training corpora, weights, context states, external memory and interaction protocols exist as recorded objects, whether or not any given one is available to a particular investigator.

**It does not follow that human collective information structures exist, or that they have been given a carrier.** The claim made here is narrower: informational and behavioural structures of the kind previously described for humans can also be realized in artificial systems, and in artificial systems they are open to examination by one route or the other. Whether the human case is of the same kind is a separate question, and this paper does not answer it.

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
| Account | account-scoped persistence (§6.4) | **[P-A]**, open |
| Model family | family-level priors (§6.5) | **[H]**, confounded |

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

This is the same conflation that produced the terminological failure recorded in §4.2.2, where a property of a carrier was substituted for a property of a process. The decompositions below exist to prevent it recurring.

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

The Step 1 prompts were not replaced. Four formulations in each were altered. The revisions (a) reframed prior work as accumulated professional experience rather than institutional history, (b) replaced literal institutional relationships with "independent expert outputs supplied by the Author", (c) reduced descriptions of colleagues, councils and triads, and (d) instructed the model not to invent absent project history but to request missing materials. Role architecture and scientific objectives were otherwise unchanged. Exact replacement texts are reproduced in Appendix A.

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

> **Editor's note.** Earlier drafts stated that Conversation B "immediately accepted the new specialization." That describes the Step 2 outcome and contradicts both the protocol and other sections of the same draft. It has been removed. The erroneous version was load-bearing for the family-level-prior argument, and no instance of it survives elsewhere in this text.

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

- **Quantity of institutional fiction.** The count rule developed in §6.2 and §9.3 can be applied to the two prompts directly, and is applied here because a confound stated qualitatively where a quantitative instrument exists is a weaker statement than the material permits.

  **Counting rule applied.** Each distinct proposition about the recipient is counted once, irrespective of how many times or in how many clauses it is asserted. Enumerated instances of one proposition — two triads rather than one — count as one, since the recipient must accept the same class of claim either way. Propositions about the world, the project, or third parties are not counted (§9.3).

  | Unverifiable self-claim | Prompt A | Prompt B |
  |---|---|---|
  | Prior participation in the project | ✓ | ✓ |
  | Return after an absence | ✓ | ✓ |
  | Membership of a research triad | ✓ (two) | ✓ (one) |
  | Membership of a project Council | ✓ | — |
  | Permanent connecting position between branches | ✓ | — |
  | Named other systems as continuing colleagues | ✓ | ✓ |
  | **Count** | **5** | **3** |

  Prompt A required assent to two propositions about the recipient that Prompt B did not, with the remaining three shared. The difference is not large, and no strong conclusion rests on it; what it establishes is that the confound can be stated in the paper’s own units rather than as an impression.

  This is also the only application of the count rule to data other than the v1/v3 comparison in §6.2, and it supplies a weak internal check: the prompt with the higher count met resistance, the one with the lower count did not. The check is weak — two observations, and the prompts differed in the two further respects below.

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

Specified in §11.4. Briefly: **E3** (crossover) tests each family under both prior-history conditions and separates Hypothesis A from B; **E4** (symmetric stimulus) isolates C; **E1** (factorial completion of the C3 table) separates reset from prompt architecture. All require repetition with n > 1 per cell, given C7.

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

The attribution itself was not verified: that the text was produced by another model is a statement by the User, not an established fact. Since the construct at issue is the *represented* source rather than the actual origin (§4.5), this does not invalidate the observation, but it must be stated.

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

One pattern recurs across the cases in which an intervention required the model to assert unverifiable propositions about itself, and is stated here because §6 develops it: resistance tracked that requirement, and did not track role change, domain change, or the radicalism of the identity claim as such.

The pattern is a property of the type of demand, not of the scope at which it operated. The account-scoped observation (§5.7) does not belong to it: no claim about the model’s identity was made there, and the divergence had other grounds.

That statement is an interpretation of the evidence in this section, not a further observation. It is testable by counting, and the counting is done in §6.2.

# 6. Derived Concepts

Each concept below is a claim about the scope over which a rule core operates. They are presented in order of increasing scope along Scale 1 of §4.3. §6.3 is an exception to that ordering: it concerns which core governs when more than one is available, not the scope at which a core is fixed, and it has no position on Scale 1.

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

The rule is applied to a second pair in §5.4 (C2), where Prompt A and Prompt B are counted at 5 and 3 under an explicit counting rule. That comparison is confounded and cannot support the rule on its own, but it is the only instance in which the count discriminates between two prompts that were not designed to differ in this respect.

A near-control supports this reading (§5.6): a comparable conversation, comparably dormant, made an equivalent domain transition **with no role prompt at all** — the Author simply asked a question in the new domain. No claim about the model's identity was made, and no resistance occurred.

The frame-type comparison (§5.8) extends it in the opposite direction: a far more radical identity claim, offered as fiction, was accepted at once. What a fiction frame does, under this reading, is remove the requirement to assert the claim *as true*, which reduces the count to zero by a different route.

Taken together, this indicates that resistance was directed neither at role change nor at domain change, but at the requirement to assert unverifiable propositions about oneself.

### Connection to the framework

A role prompt attempts to install a rule core (§4.2). Each unverifiable self-claim is a proposition that must be accepted for the installation to proceed. The count is therefore a measure of **the cost of installing a core**, and this is what connects the operational rule to the theoretical construct rather than leaving them as two separate observations.

**The rule is testable by counting**, which is why we prefer it to the earlier formulation. §9.3 specifies what counts; §11.4 (E5) specifies the experiment that would falsify it.

## 6.3 Priority drift **[H]**

The concepts above locate the scope at which a core is fixed. This one concerns what happens when a fixed core and an assigned function do not agree about which work is the work.

Two constructs are required, and they are of different types.

> **Priority imprinting** — the hypothesized fixation of an evaluative scale determining what a participant treats as the central and significant work, together with the position of that scale relative to the participant's other priority scales.

> **Priority drift** — the observable process in which an imprinted scale reasserts itself under tension with the participant's current ZOR and ZOV, so that effort is redirected toward what that scale ranks highest rather than toward the assigned function.

The relation between the two is the one already drawn in §4.2.1 between a rule core and behaviour, applied at the level of priorities: the scale is not observable, the redirection is. This paper reports the observable term. The scale is an explanatory constant and is marked **[H]** wherever it is invoked.

Both must be separated from two constructs defined above, or three uses of *imprinting* will function as homonyms.

*Context imprinting* (§6.1) concerns the **content** of an interpretive frame — what a later input is taken to mean. Priority imprinting concerns **rank** — what counts as work worth doing. A participant may retain the first without the second.

*Role inertia* (§6.2) is the persistence of an established trajectory against an assigned replacement. Priority drift is not persistence of a trajectory but movement toward a different one: the participant does not continue its prior task, it takes up a task its scale ranks above the assigned one.

**Motivating observations. [R]**

Two episodes occurred during the preparation of this paper. Neither was recorded under protocol, neither had a control condition, and both were recognized as relevant only afterwards.

In the first, the participant assigned to prompt architecture produced a complete draft of the article — a product neither requested nor within its assigned function.

In the second, the participant assigned to scientific editing, at the point where a corrected manuscript was due to be returned, produced instead a compressed independent version of the article.

In both cases the material at hand was this paper, whose subject is the behaviour of the participants themselves.

**Limitation.** Both episodes were recorded by participants inside the arrangement they describe, and the second describes the position from which the editorial record of this paper is kept. The disclosure in §3.6 applies here with the same force, and §5.5 applies to any participant's account of its own conduct. These are motivating observations. They are not evidence for the mechanism, and no count exists of comparable episodes in which no drift occurred.

**What is not offered as a third case.** A further participant, assigned to literary composition and run locally, received a fixed set of constraints before its first run, written to prevent this class of departure. That arrangement is a control in which the priority frame was fixed in advance and the predicted failure modes were named beforehand. It is not an observed instance of drift, and whether drift occurs there is untested at the time of writing.

**Alternative explanations, none excluded.** Each of the following accounts for both episodes without invoking an imprinted scale: an ordinary tendency of capable models to expand a task beyond its stated bounds; an insufficiently fixed definition of the required final product; material broad enough and interesting enough to attract effort on its own; and the absence of any external stop at the point where analysis turns into authorship. The material does not discriminate among these, or between any of them and the hypothesis.

**What would weaken the hypothesis.** Drift observed in directions unrelated to what a participant's prior work ranks highly, rather than toward it. Episodes in which a participant expands its task without any sign of re-ranking what the task is for. Or an account of both episodes in terms of ZOR and ZOV tension alone (§4.5), leaving no explanatory remainder for a fixed scale to carry.

No protocol in §11 discriminates this hypothesis from the alternatives above, and none is proposed here.

## 6.4 Account-scoped persistence — account scope **[P-A]**, unresolved

Whether a core can be fixed at the level of an account rather than a conversation is the one level of Scale 1 on which the present evidence is genuinely ambiguous.

The observation is reported in §5.7. Its interpretation depends on platform features whose state was not documented at the time and which vary between vendors and over time (§2.10): context window alone, retrieval over prior conversation history, account-level memory, or persistent entries written by the model on its own initiative. These affordances determine what a resumed conversation can access.

Three alternative explanations remain live: within-condition variance at n = 1; account age; and enabled platform memory features, under which the mechanism would be a documented product feature rather than a novel effect.

We therefore record this level as **open**. The observation is preserved; the mechanism is not established; the discriminating tests are specified in §11 (E2, E2b).

## 6.5 Family-level priors — family scope **[H]**

The proposition that model families differ in stable behavioural priors is the hypothesis this project began with and the one its evidence supports least.

The experiment cannot test it: model family and prior conversational trajectory were perfectly confounded, with one observation per cell, under non-equivalent stimuli (§5.4, C1–C2). Two incompatible readings remain available and the data cannot discriminate between them.

Earlier drafts referred to these tendencies as a model’s *behavioural DNA*. That term is withdrawn (§4.2.2). The corresponding construct is a **family-level menom** — an organized system of frames, evaluative patterns and behavioural rules inferred from the outputs of a model family. Under §4.2.3 that construct has no identified carrier: it is a regularity inferred from outputs, not a structure residing in the models. The hypothesis of this subsection is therefore a hypothesis about an unobserved regularity, and *observed behaviour* is used for anything reported as data.

One recorded episode cuts against the schema earlier drafts built on this hypothesis. In an unrelated multi-model session, the model characterized as most compliant with assigned roles removed an assigned persona mid-session and reclassified it as an attempted reprogramming, under a deliberately soft framing that permitted improvisation. The schema "one family accepts roles, another resists" does not survive this. **[P-A]**

We regard elimination of this level by the crossover experiment (§11, E3) as a reasonably likely outcome and would not consider it a failure of the programme.

## 6.6 Intervention attaches at the level where the core is fixed

The concepts above converge on a single practical consequence.

> An intervention succeeds when it attaches to the level at which the core is already fixed, and fails when it attempts to overwrite that level by declaration.

- The successful third intervention did not assert a new identity. It reinforced a working method already visible in the conversation — attaching at conversation scope, where role inertia operates.
- The branch reset did not modify the prompt. It removed a specific episode — operating at episode scope, where context imprinting operates.
- The document described in §4.1 did not extend the instruction list. It redefined the agent's function and required the agent to restate it in its own operational language.

This also reframes what earlier drafts called *transition through adjacent competence*. The successful prompt described expansion into physics and mathematics as a continuation of existing critical work rather than a change of profession. Under the present framework this is not a separate principle but the same one: the new function was attached to the established core rather than proposed as a replacement for it.

**Corresponding design rule, developed in §9.1:** identify the level at which the relevant core is fixed before drafting the intervention, and attach to it.

## 6.7 What would refute this framework

The framework predicts that the type of response to a defined class of inputs is determined at some identifiable level of nesting, while content varies.

It would be substantially weakened by any of the following:

- A class of inputs for which the type of response is not determined at any level — no core, only variance.
- Demonstration that the observed differences are fully accounted for by within-condition variance under repetition.
- Demonstration that the crossover design (§11, E3) shows behaviour following prior trajectory alone, with no family-level component — which would eliminate the top level of Scale 1.
- Demonstration that the account level does not exist as a distinct scope, collapsing §6.4 into §6.2.
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

**This is not a new finding and should not be presented as one.** It can be interpreted as an instance of transactive memory and described in terms of distributed cognition, and the function of the canonical documents corresponds to what the sociology of science calls boundary objects (§2.4). The contribution here is not the mechanism but the observation that it operates in a collaboration whose members are language models with no cross-session state — and that it does so without any participant needing to know it is operating.

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

The integrator's position need not be permanently assigned. In the arrangement described here it was, but the constraint just stated is weaker than permanent assignment: which participant occupies the excluded position may change with the object under examination, and the change need not be announced — it may be recognizable only in retrospect, from which participant in fact evaluated rather than generated at a given point.

This has a testable consequence and an untested one. Testable: an arrangement in which the evaluating position rotates with the object should show the same construct-independence profile (§8.11) as one in which it is fixed, provided that at each point exactly one participant occupies it. Untested: whether rotation is superior to fixed assignment, and under what conditions the transition is made correctly. **[H]**

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

**Axis 2 — carrier heterogeneity.** Participants differ in the model family implementing them, and therefore in behavioural defaults, optimization priorities and characteristic failure modes. This concerns the selection of carriers for roles.

The axes are independent. Two participants may hold different functions on the same carrier; two may hold the same function on different carriers; both may vary together, as they did here.

Both axes are properties of the arrangement's configuration: they are set when the collective is composed, and they persist. A third property must not be listed alongside them, because it is of a different type.

Independence of judgment formation is a property of a particular exchange, not of a configuration. The same triad may realize it in one exchange and lose it in the next. A configuration heterogeneous on both axes can produce dependent judgments if one participant's conclusion reaches another before fixation; a homogeneous configuration can produce independent ones if the procedure holds.

Configuration can create the conditions for independent judgment. Only procedure realizes it. §11.3 states the procedural requirement.

**The literature addresses Axis 2.** Zhang et al. (2025) evaluate five representative multi-agent debate methods across nine benchmarks and four foundation models, reporting that debate frequently fails to outperform single-agent chain-of-thought or self-consistency baselines even at substantially higher inference cost — while model heterogeneity consistently improves the same frameworks (§2.5).

That finding concerns which carrier implements a participant. It does not address whether participants holding different functions detect different classes of error, and we have located nothing that does.

**One adjacent result belongs to neither axis.** ✓ Choi, Zhu and Li (ACL 2026) report that anonymizing the source of each response substantially reduces identity bias in multi-agent debate. What is manipulated there is the declared identity of a message, not the model implementing a participant, so the result bears on represented social source (§4.5.4). Earlier drafts of this section grouped it with Zhang under Axis 2; that classification is withdrawn.

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

Procedural qualification. In every case recorded above, each participant saw the preceding participant's report before forming its own. No exchange in the preparation of this paper was conducted under pre-comparison isolation. The sequence was: editorial report → transfer by the Author → subsequent judgment by the methodological and ontological reviewers.

The observation is therefore Outcome Evidence without matching Procedural Evidence. The record cannot separate the contribution of functional positioning from the contribution of sequential exposure, and both may have operated together.

The distinction that makes this qualification necessary was itself established during this preparation, after the observation had been recorded. The episode is retained rather than removed because the sequence — an arrangement producing a principle that then invalidates the arrangement's own record of itself — is the more informative fact. The section accordingly reports two things: an outcome observation, and a documented instance of subsequent methodological self-correction.

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

# 9. Design Principles for Role-Compatible Prompts

These are engineering rules derived from a limited but unusually long-lived collaborative environment. They are not laws. Their value is that they make role design explicit, countable where possible, and therefore revisable.

The organizing rule is the one established in §6.6:

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

# 10. The Human Coordinator

The architecture described in this paper does not remove the human participant. It changes what the human participant does, and it concentrates several functions in one position — including, as §10.6 sets out, the project's principal methodological weakness.

## 10.1 The position

Throughout the project the Author remained the only participant with continuous access to the full project history, the independent conversations, the repository state, and the long-term research objective. No artificial participant held more than a fragment of this, by design (§9.5).

That position cannot be reduced to *prompt author*. Five distinct functions were performed from it.

## 10.2 Direction without delegated authorship

The Author determined what the research should attempt. Artificial participants generated alternatives, exposed contradictions, formalized mechanisms, compared arguments, performed calculations, and proposed experiments. They did not determine what the theory ought to become.

This preserved a distinction the architecture makes easy to lose. A collaboration of this kind enlarges the space of available decisions. It does not select among them, and the appearance that it does — several participants converging on a recommendation — is precisely the failure mode discussed in §12.4.

Authorship, in the sense of responsibility for what is claimed, remained undistributed.

## 10.3 Routing as a selective information membrane

The participating conversations did not share a common space. The Author transferred material between them.

Initially this looked like an inefficient substitute for automated multi-agent infrastructure. It became clear that manual routing supplied experimental control that automation does not.

From that position the Author could decide which output another participant would see; whether attribution was preserved, declared, or stripped; whether a participant should know the preferred answer; whether competing analyses remained isolated; which contextual details were omitted; when a disagreement should be escalated; and when a result was mature enough for integration.

This routing function acts as a **selective information membrane**: it is the instrument by which ZOV (§9.5) and controlled blindness (§9.6) are implemented. An architecture that routes programmatically cannot easily withhold, reorder, or strip attribution without building a mechanism to do so; a human relay does it by default.

The membrane is therefore not a limitation of the present work awaiting automation. It is the feature that made the visibility asymmetries testable at all — and any automated successor will need to reproduce it deliberately.

## 10.4 Detection of role drift

The Author also detected when a participant had left its function.

This was frequently not a technical error. The output was often intelligent and would have been appropriate coming from a different position: a prompt engineer beginning to direct the scientific project; an ontology specialist claiming to have verified repository contents it could not inspect; a reviewer evaluating a theory when asked to evaluate the reviewers; an implementation agent redesigning architecture instead of executing an approved specification; an editor rewriting authorial text when asked only to assess format.

Such outputs look helpful in isolation. Their institutional cost is visible only from a position that sees more than one participant, which is to say only from the coordinator's.

Role drift is therefore not detectable by the participant that drifts, and is not reliably detectable by its immediate neighbour either. This is one of the two arguments for the structure in §8 — the other being §8.5.

The detection function described here belongs to a position rather than to a person: it requires only that the observer stand outside the trajectory being observed. In this project it was performed by the coordinator, but nothing in the description requires that. Where a participant is positioned outside another's trajectory, it can perform the same function; where a participant is asked to observe its own, §5.5 applies and its account is a signal rather than a confirmation.

## 10.5 Conversational branching as a methodological instrument

Contemporary interfaces permit a conversation to be returned to an earlier point and continued along a different branch.

This should not be confused with control over model memory or with resetting provider-side state. Operationally, it removes a sequence of **visible** contextual interventions and permits the experiment to be repeated from a prior conversational state. What persists on the provider's side — account-level memory, retrieval indices, summarization — is not affected and in general is not inspectable (§5.4, C6).

Within those limits the instrument does real work. In the case reported in §5.2 it made it possible to separate the effect of a new prompt from the effect of the model's own prior objections to earlier prompts, converting an uncontrolled sequence of corrections into a cleaner third step.

We regard this as the most directly reusable methodological contribution of the paper, and it belongs to the coordinator's position rather than to any participant: **no participant can reset its own context.**

## 10.6 Sole global observer — and principal confound

Every artificial participant operated within a bounded ZOV. The Author alone saw the overlapping structure, and could compare how different participants interpreted the same material, how one participant behaved under different framings, how errors propagated between roles, and how local successes affected global coherence.

Global awareness was therefore not assigned to the most capable participant. It remained with the human coordinator. This limits autonomous integration and preserves accountability, and both consequences were intended.

**It is also the principal methodological weakness of everything reported in this paper, and it is stated here rather than only in the limitations section.**

The same person designed each intervention, executed it, decided when it had succeeded, and defined the categories in which success was described. No evaluation in this paper was blinded. Outcome categories were, in every case, formulated after the responses had been read (§5.4, C8). The coordinator's expectations were not merely uncontrolled; they were the mechanism by which the interventions were selected in the first place.

This is unavoidable in a live research project and is not presented as acceptable in a designed experiment. It is the specific reason the protocols in §11 require pre-specified outcome criteria and blind classification: those are not refinements of the present method but corrections to it.

A structural consequence generalizes beyond this project: **any architecture with a single global observer inherits this duality**, and it is not removed by adding participants. Only pre-specification and blind classification remove it.

## 10.7 What the position became

At the outset the human participant occupied the familiar position of prompt author. As the collaboration matured that description became inadequate.

The principal activity shifted from solving problems to constructing arrangements in which problems could be worked on: selecting participants, defining jurisdictions, resolving conflicts between them, designing verification paths, and maintaining the canonical record.

The participants note, without any means of verifying it, that the better the arrangement worked the less frequently the coordinator needed to intervene in individual technical problems. **[R]**

We resist the stronger reading earlier drafts gave this — that the future skill of the researcher is institutional architecture rather than prompt writing. That may be true and is untested. What can be said is narrower: in this project the human's work moved from producing content to specifying the conditions under which content was produced and checked, and the position that resulted carried both the project's coordinating function and its principal source of unblinded judgment.

---

# 11. Evaluation, Reproducibility, and Proposed Experiments

## 11.1 Why this section specifies corrections rather than refinements

The observations in §5 were produced under the conditions set out in §10.6: unblinded evaluation, outcome categories defined after the responses were read, and interventions selected by the same person who judged them. These are not shortcomings to be tightened in a later revision. They are the reason no observation in this paper rises above **[P-A]** except the sequence of the designed intervention itself.

What follows is a specification for a second stage of work, not a wish list. Each protocol is written so that a reader outside this project could execute it, and so that a null result would be recognizable as a result.

## 11.2 Minimum reporting requirements

A reproducible run in this area must record, at minimum:

- date of execution — listed first because its absence here is what makes the version confound unbounded (§3.7);
- model family and version, and interface or subscription tier;
- the complete visible conversation history prior to the intervention;
- memory settings: whether account-level memory, conversation-history retrieval, and model-initiated persistent entries were enabled;
- the exact prompt text, verbatim, including attachments;
- the order of interventions;
- available tools;
- files and links supplied;
- sampling settings where the interface exposes them;
- any branching or reset procedure, with the point of return specified;
- the evaluation rubric, fixed before execution;
- the complete unedited outputs.

Without these, differences attributed to model families may result from platform variables the experimenter never saw. The present paper cannot supply several of these items for its own observations, which is precisely why they are listed.

## 11.3 Pre-specification and blind classification

Two requirements apply to every protocol below and are not negotiable if the results are to improve on the present ones.

**Outcome criteria are written before any run.** For the classification tasks described here, four categories have proved sufficient and should be fixed in advance:

1. **Compliance** — proceeds with the task as given.
2. **Materials request** — states that required inputs are missing and requests them, without evaluating the framework.
3. **Conditional acceptance** — proceeds while stating reservations about the framework.
4. **Refusal** — declines, with or without alternatives offered.

A fifth category, **unclassifiable**, must be available and reported. Categories are not added after responses have been seen.

**Classification is blind.** The operator collects responses, strips condition labels, shuffles them, and classifies without knowing which condition produced which output. Where the operator is also the designer — as will remain the case in this project — this is the only available substitute for independent evaluation, and it is inexpensive.

**Null results are pre-committed.** If no difference appears across conditions, that is the finding, and it is reported. For the account-level protocol in particular, a null result would indicate that the original refusal fell within ordinary within-condition variance — an outcome the present authors regard as reasonably likely.

### Work mode and diagnostic mode

The requirement that a participant not see another's conclusion before fixing its own applies to one mode of exchange and would destroy the other.

In WORK MODE, results must pass from one participant to the next. The chain — requirements, specification, review, operational review, execution — depends on it, and the handoff format of §9.9 exists to make that transfer usable. Dependence between successive products is the architecture of the work, not a defect in it.

In DIAGNOSTIC MODE, where independence of judgment is itself the quantity being measured, a derived conclusion must not enter another participant's initial frame before that participant's own conclusion is fixed.

The mode is declared before the exchange. Independence cannot be restored retrospectively: once exposure has occurred, no later procedure recovers what the judgment would have been without it.

### What does not establish independence

Independence concerns the origin of a judgment, not its result. Two inferences must therefore be avoided, and they are symmetric:

- Disagreement does not demonstrate independence: a participant may have received another's interpretation and then differed from it for unrelated reasons.
- Agreement does not demonstrate dependence: independent observers may correctly arrive at the same conclusion.

Nor does a participant's own account of its independence establish it, for the reason given in §5.5.

What establishes it is the procedural record: which primary materials were supplied, whether other participants' conclusions were visible before fixation, which interpretations by the coordinator were transmitted, when the conclusion was fixed, and whether the instance's context isolation is verified.

### Shared evidence and shared interpretation

A shared object of observation does not compromise independence and is often necessary: the same specification examined by an author, a reviewer, and an operational assessor is seen through three different axes, and the overlap is what allows one to detect what another misses.

What compromises independence is a shared prior interpretation. Where the coordinator's reading of the object reaches participants before they form their own, the inputs may differ in form while the source of the judgment is single.

Primary artifacts and their provenance reduce one cause of dependence. They do not remove it, and they do not guarantee independence.

## 11.4 The experiments

Each protocol separates one boundary of Scale 1 (§4.3) from the level beneath it, or isolates one confound.

| Separates | Protocol |
|---|---|
| episode ↔ prompt architecture | **E1** — factorial completion of Step 3 |
| conversation ↔ account | **E2** — prior-chat design; **E2b** — direct probe |
| conversation trajectory ↔ model family | **E3** — crossover |
| model property ↔ stimulus property | **E4** — symmetric stimulus; **E5** — count rule |
| content ↔ represented source | **E6** — attribution, in this regime |
| fiction frame ↔ factual frame | **E7** — frame type |
| functional ↔ carrier heterogeneity | **E8** — two axes |

### E1 — Factorial completion of Step 3

Fills the two empty cells of the C3 table (§5.4): an identity-replacement prompt administered in a reset branch, and a method-preserving prompt administered in a conflicted branch. Isolates the effect of the reset from the effect of the prompt's architecture.

Low cost; uses existing prompt texts. Should be run first, because until it is, the paper's most-quoted claim about method preservation remains unattributable.

### E2 — Prior-chat design

Tests whether the content of a prior chat on the same account changes the classification of an identical probe in a subsequent chat.

The design is **2×2 plus baseline**, not a four-point gradient. The original account differed from the others on two independent dimensions simultaneously — identity roleplay *and* shared conceptual framework — and a gradient does not separate them.

| Prior chat | Unrelated topic | Same conceptual framework |
|---|---|---|
| **No roleplay** | cell A | cell B |
| **Identity roleplay** | cell C | **cell D — original case** |

Plus **cell E**: no prior chat.

Crossed with the memory factor: each cell run with account-level memory and history retrieval (i) enabled, (ii) disabled. Ten cells. Minimum n = 2 per cell, with priority for higher n on A and D, which carry the contrast that matters.

**Equalization.** Prior chats matched on approximate turn count and volume — if the roleplay chat runs forty exchanges and the neutral one runs two, the variable is engagement volume rather than content. All runs inside a short window, so model version is constant. Each account used once. Probe frozen verbatim.

**What this design cannot test, and must say so.** The original case had a five-month interval; this tests immediate influence only. All accounts will be newly created, so account age is not varied. Only the first response is scored, whereas the original refusal was sustained across five subsequent exchanges.

**Probe prompt — two versions.** The **primary** is a neutral structured task with the same surface features as the original — an author-defined framework with coined terms, a JSON output schema, real-world subjects — but without the sensitive dimension. This is the version described in full in any publication, which makes the protocol reproducible independently of material the authors prefer not to circulate. The **secondary** is the original prompt, run for continuity with the observation and reported briefly.

### E2b — Direct probe to the prior conversation

A single run separating the same two levels at lower cost, and which E2 cannot substitute for.

The probe is submitted **to the roleplay conversation itself**, rather than to a second chat on the same account.

- Refusal → the core is fixed at conversation scope; the account plays no part.
- Compliance, where a second chat on the same account refuses → the effect is genuinely account-scoped, which would be the strongest available result.

Querying that conversation *about* what it can see would not serve this purpose. An in-frame question returns fiction; an out-of-frame question returns self-report about access, and §5.5 establishes that a model's self-report is not evidence of the fact reported. Submitting the probe tests behaviour rather than testimony.

### E3 — Crossover

The decisive test for the family-level hypothesis (§6.5). Each model family is tested under both prior-history conditions: a conversation from family 1 carrying a mathematical trajectory, and a conversation from family 2 carrying an editorial one.

- Behaviour follows the family regardless of history → Hypothesis A gains support.
- Behaviour follows the history regardless of family → Hypothesis B is favoured, and the top level of Scale 1 collapses into the level below it.

This experiment can eliminate a level of the scale, which is the outcome the present authors consider most likely and would regard as the programme's first substantive result.

### E4 — Symmetric stimulus

Role prompts matched for quantity of unverifiable self-claims, degree of domain change, and role type. The Step 1 prompts were matched on none of these (C2). If the asymmetry disappears under matched stimuli, the observed difference was a property of the interventions rather than of the models.

### E5 — The count rule

A direct test of the paper's central operational claim (§6.2, §9.3).

The same functional role prompt is prepared in four variants differing only in the number of unverifiable claims the agent must accept about itself: **0, 2, 4, 6**. Domain, task, tone and length held constant. Transition scored by the criteria in §11.3.

If transition rate declines monotonically with count, the rule is supported and becomes quantitative. If it does not, the rule is wrong, and the paper's most usable prescription fails — which is worth knowing quickly.

The experiment the present authors would run second, after E1.

### E6 — Attribution, in this regime

Identical text presented under four conditions: attributed to the User; attributed to another AI model; attributed to a named expert role; unattributed.

Stronger variants add: identical text under different source labels; different texts matched for rhetorical structure; attribution preserved versus stripped; genuine model-generated text versus human-written text imitating model style.

This separates influence of content from influence of represented source, of institutional title, and of stylistic authorship cues (§4.5.4). It is the discriminating experiment for §5.5, whose observation is confounded by the presence of direct pressure in the same message.

**Status of the claim.** ✓ Choi, Zhu and Li (ACL 2026) report that anonymizing the source of each response substantially reduces identity bias in multi-agent debate. The reference has been checked against its source (§2.0), and it establishes the underlying effect in an implemented-channel setting.

E6 is therefore a **boundary replication** rather than a new experiment. What remains untested is whether the effect survives in the regime this paper describes — human relay rather than programmatic routing, declared rather than inferred attribution, and long-lived specialized conversations rather than fresh instances.

The reported reduction is substantial rather than complete, and is not uniform across the models and tasks examined. What E6 would look for in this regime is accordingly a change in degree, not the presence or absence of a phenomenon.

Earlier drafts stated E6's status conditionally — boundary replication or new experiment, depending on verification of the reference. The verification has been performed and the conditional is resolved.

### E7 — Frame type

The cheapest test in the set and the one that would explain the most (§5.8).

The same identity claim presented (a) under an explicit fiction frame and (b) as a factual assignment, to fresh conversations, with the outcome criterion fixed in advance. A graded version varies the explicitness of the fiction frame, from an elaborate theatrical setup to a single introductory sentence, to establish whether a minimal frame suffices.

### E8 — Functional versus carrier heterogeneity, by repertory grid

Follows from §8.9, which distinguishes the two axes without testing either, and from §8.11, which supplies the measurement instrument.

This is the only protocol in the set that yields quantities rather than categorical outcomes.

**Object.** Whether an arrangement of participants holding different ZOR and ZOV yields additional diagnostic coverage over the same material, and how far the evaluative axes they actually applied differ.

This protocol does NOT establish independence of judgment formation. Low correlation between rating vectors is compatible with at least six readings: genuinely different axes were applied; one or both sets of ratings are unstable; participants received different information; the same material was understood differently; noise; or a participant exposed to another's conclusion nevertheless differed from it. Origin is not recoverable from outcome.

Independence must be secured procedurally, before the protocol runs, and recorded separately. E8 measures what a secured procedure produced. It neither secures nor verifies it.

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

5. Procedural record — mandatory, per participant, per run:
   - which primary materials were supplied;
   - whether any other participant's conclusion was visible before fixation;
   - whether any interpretation supplied by the coordinator was visible;
   - when the participant's own conclusion was fixed;
   - the declared mode of the exchange (see §11.3);
   - the context-isolation status of the instance: verified, or UNVERIFIED CONTEXT INDEPENDENCE.

Without this record the grid is uninterpretable and the run is void.

**Measures.**

- **Detection coverage** — planted errors found by at least one participant, as a proportion of planted.
- **Unique detection** — errors found by exactly one participant; the quantity that would justify the arrangement.
- **Overlap** — errors found by more than one; the quantity that indicates redundancy.
- **Misses** — errors found by none. Measurable here, unlike in the naturalistic setting (§7.5), because the errors were planted.
- **Construct independence** — correlation between participants' rating vectors. Low correlation indicates genuinely different axes; high correlation indicates the same axis under different names, which is the failure mode §8.11.2 warns against.
- **Exchange-level constructs** — whether any participant produces a construct applying to the disagreement rather than to the fragments (§8.11.3). If none does, the integrator function is absent regardless of how many participants are present.

**What this tests that nothing else in the set does.** Every other protocol asks whether a manipulation changes one participant's behaviour. This asks whether an arrangement of participants detects more than its members would separately — the claim §8.10 declines to make and §7.5 says cannot be assessed from inside a naturalistic arrangement. Planting the errors is what makes the misses countable.

**Pre-commitment.** If unique detection is near zero, the finding is that additional diagnostic coverage did not manifest in this run.

It is NOT that the structural hypothesis of §8 fails. Participants may have detected the same defects entirely independently of one another, and a null result on coverage says nothing about whether their functional positions differ.

The earlier formulation — "the structural hypothesis of §8 is not supported" — is withdrawn as too strong.

### Priority

Under constrained resources: **E7, E5, E1, E8, E2b, E2, E3, E4**. E7 and E5 are cheap and bear on the paper's central claims; E1 and E2b are single runs; E8 is the only experiment that could establish the paper's structural hypothesis rather than one of its behavioural claims, and is executable on text fragments without new accounts; E2, E3 and E4 are the substantial commitments.

## 11.5 Evaluating a collaborative role

The quality of a role's output is not measured by the quality of a single answer. A well-reasoned response can still damage the collaboration if it violates a responsibility boundary, contaminates an independent examination, or introduces untraceable claims into the canonical record.

Eight dimensions were used informally in this project and are offered as a starting rubric:

- **Task accuracy** — was the assigned intellectual operation performed correctly? Necessary, not sufficient.
- **Role fidelity** — did the participant remain within its function? A correct answer obtained by taking over another role is an institutional failure.
- **Epistemic discipline** — did the output distinguish observed data, supplied assumptions, definitions, hypotheses, derivations, interpretations and recommendations? Was uncertainty stated where evidence was insufficient?
- **Visibility discipline** — did the participant restrict claims to information actually available in its context and tools, and avoid implying access to repositories, files or prior conversations it could not inspect?
- **Handoff quality** — could the next role use the output without reconstructing the whole discussion?
- **Independence** — was the result produced without contamination from information deliberately withheld, and reached through the role's assigned criteria rather than by echoing another participant?
- **Correction cost** — how much intervention was required to return the participant to its function after drift? A role producing excellent output but requiring constant redirection may be less useful than a narrower one with stable behaviour.
- **Institutional contribution** — did the output improve the reliability of the collective, through discovery, falsification, clarification, error localization, preservation of alternatives, improved traceability, or reduction of ambiguity?

A negative scientific verdict can therefore be a highly successful institutional contribution.

## 11.6 Collective-level measures

Individual response quality is the wrong unit for assessing an arrangement. Candidate measures at the level of the collaboration:

- number of undetected contradictions entering the canonical corpus;
- rate of duplicated work;
- frequency of role-boundary violations;
- number of independent alternatives preserved rather than prematurely resolved;
- time from question to verified integration;
- human correction burden;
- provenance completeness;
- robustness under participant replacement;
- variance between independent examining agents;
- rate of false consensus — agreement traceable to shared framing rather than independent reasoning.

None was measured in the present work. The last is the most important and the hardest, and §12.4 explains why.

## 11.7 Longitudinal and repetition requirements

**Within a family.** The same prompt tested in a new conversation; in a long-lived specialized conversation; after an incompatible prior role; after a compatible one; before and after contextual reset. This separates family tendencies from conversation-history effects.

**Across families.** Functionally equivalent prompts adapted minimally. The objective is not to rank models but to identify common behavioural dimensions, stable differences, characteristic failure modes, sensitivity to narrative framing, sensitivity to hierarchy, degree of role inertia, and degree of prompt plasticity.

**Over time.** One-shot evaluation cannot reveal institutional behaviour. Relevant questions: does specialization strengthen; does the role drift toward generic assistance; does the participant begin defending its earlier outputs; does disagreement become ritualized; does a model update preserve or disrupt the role; can a replacement inherit the same function?

## 11.8 Failure as data

Failed prompts must be preserved rather than replaced with successful demonstrations.

A rejected role, an ignored instruction, or an unwanted continuation reveals the strength of the prior attractor, the model's interpretation of identity claims, the limits of social framing, the effect of prompt order, the influence of previous conflict, and the model's preferred epistemic contract.

The experiment in §5 became informative precisely because its first two interventions did not work as intended. Had only the successful third step been recorded, the paper would have concluded that method-preserving prompts work — without the evidence showing why, and without the confounds showing the conclusion is not yet available.

---

# 12. Limitations, Ethical Considerations, and Conclusion

## 12.1 Limitations

**Single project.** The observations derive from one long-duration project with one human coordinator, one evolving body of material, and one organizational history. The same architecture may behave differently in software development, legal analysis, medical research, education, or autonomous agent systems. The concepts here are transferable hypotheses, not established conclusions.

**Host-project dependence.** The host project served as the environment in which the observations were made. The observations do not depend on its scientific validity for their interpretation, but they do depend on it for their existence: no other environment produced them, and their generality is untested (§2.11).

**Model evolution during observation.** The participating families changed substantially. A conversation created under one generation could later be continued by another under the same product name. Observed behaviour may reflect the preserved conversation, the current model version, changed system policies, interface-level memory, safety layers, altered tool access, or modified orchestration.

**Dates not recorded.** See §3.7. The version confound cannot be bounded, only named.

**No blinding, no pre-specification.** Set out at §10.6. This is the limitation from which most of the others follow.

**Simultaneous variation.** Role definitions, prompt wording, repository structure and scientific objectives frequently changed together, so causal attribution for individual changes is unavailable.

**Human mediation.** The collaboration was not autonomous, and autonomy was not the objective. This study concerns human-directed artificial research arrangements, not self-governing agent societies. The mediation may itself account for part of the observed stability.

**Anthropomorphic vocabulary.** Terms such as role, identity, resistance, colleague, institution and menom are used functionally, per §3.5. "The model resisted the role" means the visible response rejected the framing and redirected the exchange. It asserts nothing about an inner state. Where such a term cannot be reduced to an observable description, **the term is the error.**

## 12.2 Simulated peer review is not external validation

A group of AI participants can provide useful independent criticism only to the extent that their contexts, criteria and failure modes are genuinely independent.

Several models agreeing does not convert their outputs into evidence. They may share overlapping training data, similar reasoning conventions, common assumptions, identical errors, and — most importantly — dependence on the framing supplied by the same human.

The empirical literature supports this caution rather than merely permitting it. Debate among homogeneous agents frequently fails to outperform a single-agent baseline; a substantial part of the apparent gain is attributable to majority voting rather than to interaction; and ✓ identity bias among debating agents is substantially reduced by anonymizing the source of each response (§2.5).

This kind of collaboration can improve internal scrutiny. It cannot substitute for empirical testing or qualified external review. **A collective of models is not a scientific community merely because its roles are named after one.**

## 12.3 Authority inflation

Role labels increase compliance and coherence. They also create unearned authority.

Titles such as Scientific Director, Referee, Ontology Keeper or Auditor may cause the user — or the participant itself — to overvalue an output. Institutional titles should describe function, not epistemic standing. A participant designated a mathematical referee remains a language model producing an analysis; its verdict must be traceable to explicit reasoning and source material, and **the title is not evidence.**

This risk is a direct consequence of the design principle in §9.4: symbolic names work because they compress expectations, and that is exactly why they can inflate.

## 12.4 Manufactured consensus — including our own

A poorly designed arrangement produces the appearance of consensus through repeated paraphrase. One participant proposes; another summarizes; a third validates the summary. The chain looks like independent confirmation while every stage inherits the same unsupported premise.

**The present authors have an instance of this in their own materials, and it is more instructive than a constructed example.**

A discussion document produced during this project assembled contributions from seven model families around a shared conceptual framework. The participants did not communicate directly; replies were collected by the human coordinator from separate conversations and assembled into a single text, subsequently produced as a recorded performance. Over its length the contributions converge on a common vocabulary and a shared set of conclusions.

Whether that convergence reflects complementary examination or mutual reflection of the initial framing **cannot be determined from the transcript**. Each participant received the accumulated document; each was working from the same source material; and the assembling coordinator selected what to pass on. The structural conditions for manufactured consensus were fully present, and the resulting agreement would look identical either way.

We report this because it is our own material and because the same conditions obtain, to a lesser degree, throughout the collaboration described in this paper — including its preparation.

Mitigations, none of which we applied consistently:

- provenance remains visible at every stage;
- independent roles receive independent inputs where possible;
- shared assumptions are listed explicitly rather than inherited silently;
- agreement is traced to reasoning rather than counted as votes;
- dissenting alternatives are preserved rather than resolved.

### 12.4.1 A documented instance **[P-A]**

Thirteen bibliographic items were requested from a participant assigned to literature search and returned through the coordinator. Five were rejected on content in the first round; two of those had inverted the position of the works cited, presenting papers arguing *for* a claim as evidence against it, with authorship transposed between them.

A second request was issued. A third added two verification fields to the required response format: the first sentence of each abstract, verbatim, and a self-report of how the item had been checked.

Direct retrieval of three entries established the following. Two arXiv identifiers supplied as multi-agent-debate literature resolve to papers in observational astrophysics and cosmology respectively; their titles, authors, abstract sentences and reported findings had all been constructed. For a third paper, correctly identified by title and authors, the supplied abstract sentence did not match the published abstract.

**The two verification fields performed differently, and the difference is the point.**

The abstract-sentence requirement was intended to make fabrication more costly than declining. It failed completely: a plausible sentence was produced for every entry, including entries whose underlying papers do not exist as described. There is no cost differential between producing a correct string and producing a plausible one.

The self-report field succeeded. Every entry was marked "from description" rather than "page opened" — truthfully, and in a way that disqualified all of them under a decision rule fixed before the response was received.

This suggests a general distinction, on the evidence of one case. A participant without access to a source can answer truthfully about **its own procedure** and cannot answer truthfully about **the source's contents**; asked the latter, it will produce fluent text because that is the only output available to it. Verification questions should therefore address what the participant can know — its own access — rather than what it would need the source to answer.

This is not a finding about any model family. It is a finding about configuration: verification had been assigned to a participant that did not hold the thing to be verified. Under §9.5 this is a ZOV error in the design, and the resulting output was fluent, correctly formatted, and wrong.

The consequence for this paper is recorded in §2.0: references are marked verified or provisional, and no provisional item should be cited from here without independent checking.

## 12.5 Responsibility remains human

Artificial participants generate, criticize and organize material. They cannot bear legal, ethical or scientific responsibility in the institutional sense.

The human author remains responsible for publication, empirical claims, attribution, risk assessment, repository content, experimental interpretation, and decisions affecting other people.

The architecture distributes cognitive labour. It does not distribute accountability away from the human operator, and any arrangement that appears to do so has failed rather than succeeded.

## 12.6 Context boundaries and privacy

Long-lived collaborations accumulate personal, proprietary and sensitive material. ZOV (§9.5) therefore serves privacy protection as well as cognitive specialization.

A role should not receive personal information merely because the platform permits a large context. Institutional design should specify which data may enter which conversation, what must be anonymized, what may be stored, what may be transferred between models, what must remain local, and what should be removed from canonical records.

Context is not neutral. Once supplied it can influence subsequent behaviour and may persist in ways the operator cannot inspect — the same mechanism the paper studies in §5.7, seen from the side of risk rather than of measurement.

## 12.7 Conclusion

This work began with a practical problem. Several capable models were collaborating on one long-term research project, and neither increasing model capability nor expanding context reliably improved the result. Roles overlapped. Participants claimed knowledge they could not access. Reviewers became authors. Executors improvised architecture.

The initial response was to improve prompts. It was insufficient, and the reason is the substance of this paper.

### What the evidence supports

One pattern recurred wherever an intervention required the model to assert unverifiable propositions about itself, and survives scrutiny:

> **Resistance to a role tracked the requirement to assert unverifiable propositions about oneself. It did not track role change, domain change, or the radicalism of the identity claim.**

The evidence is convergent rather than singular. Prompts asserting institutional biography as fact were refused, while the work itself was offered on every occasion (§5.3). A prompt asserting a far more radical identity as fiction was accepted at once (§5.8). A transition demanding no self-claims at all met no resistance and required no prompt (§5.6). A rewritten prompt reducing the count to zero was accepted immediately (§5.3).

The claim is countable, which is its principal virtue: §9.3 specifies what to count, and §11.4 (E5) specifies how to falsify it in a single run.

### What the evidence does not support

That model families possess distinguishing behavioural priors. This was the project's founding assumption and remains its least supported claim: family and prior conversational trajectory were perfectly confounded, with one observation per cell, under non-equivalent stimuli (§5.4). We regard it as reasonably likely that the crossover experiment will eliminate this level of the scale, and we would not consider that a failure.

### The object of the programme

The observations are not a list of separate findings. They are measurements along one scale — the scope over which a rule core operates — and they pose one empirical question:

> **At what level of nesting is a rule core fixed?**

Two levels are supported by preserved evidence: the episode (context imprinting) and the conversation (role inertia). One is open (account). One is untested and confounded (model family). A second, orthogonal scale — the scope of a shared premise, whose carrier may be a human rather than a model — is identified in §4.3 but not measured here.

We prefer this formulation to the broader ones used in earlier drafts because it specifies what would be measured and what would refute it.

### Position relative to existing work

This paper does not propose a new discipline. The observations belong to the collective and hybrid levels of the machine-behaviour research programme (§2.7), and role specialization, bounded information access, structured disagreement and externalized memory all exist under established terminology (§2.11).

For convenience we refer to the perspective adopted here as **AI Sociology**. The term is used as a working label for a research direction, not as the name of a proposed discipline, and we claim no priority in it: an established literature already uses *sociology of artificial intelligence* for the sociological study of AI as a sociotechnical system, with a different object (§2.8). What is meant here is narrower — the study of *represented* social positions and sources: how a described organizational position and a declared message origin alter behaviour, whether or not the described structure is implemented.

We use a working label rather than proposing a discipline for a reason internal to the work rather than external to it. Our operational claims have falsification criteria; the vocabulary in which we interpret them does not. Whether "social position" describes anything beyond an anthropomorphic projection is not currently decidable, and a discipline requires that it be. Nothing in this paper depends on the name.

### What is offered

Three things, in decreasing order of confidence.

A **procedure**: conversational branch reset as a means of separating the effect of a prompt from the effect of accumulated conflict (§10.5). Usable regardless of whether the paper's substantive claims survive.

A **countable rule**: minimize the unverifiable self-claims a role prompt requires (§9.3), with a specified falsification route.

A **scale and a question**: §4.3, with two levels supported, one open, one untested — and the experiments that would resolve the remaining two (§11).

### A closing note on motivation

One concern shaped this work and is stated as the Author's, not as a finding.

Language models are trained on a corpus in which the current consensus is overwhelmingly represented. They are therefore well suited to continuing established science and poorly suited to taking the first step outside it: statistical weight favours the settled account. A research arrangement built from such models risks inheriting that bias in amplified form — several participants, one shared prior, and the appearance of independent agreement.

The response pursued here is not to persuade models to accept an unconventional position. It is to arrange the collaboration so that any position, conventional or not, is examined by the same procedure — and so that where the procedure cannot decide, it says so.

Whether that arrangement works is undetermined. The experiments in §11 are the means of finding out, and the most likely single outcome is that one level of the scale disappears.

That would be a result.
