# 11. Evaluation, Reproducibility, and Proposed Experiments

## 11.1 Why this section specifies corrections rather than refinements

The observations in §5 were produced under conditions set out in §10.6: unblinded evaluation, outcome categories defined after the responses were read, and interventions selected by the same person who judged them. These are not shortcomings to be tightened in a later revision. They are the reason no observation in this paper rises above **[P-A]** except the sequence of the designed intervention itself.

What follows is therefore a specification for a second stage of work, not a wish list. Each protocol below is written so that a reader outside this project could execute it, and so that a null result would be recognizable as a result.

## 11.2 Minimum reporting requirements

A reproducible run in this area must record, at minimum:

- model family and version, and interface or subscription tier;
- date of execution;
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

Without these, differences attributed to model families may in fact result from platform variables that the experimenter never saw. The present paper cannot supply several of these items for its own observations, which is precisely why they are listed.

## 11.3 Pre-specification and blind classification

Two requirements apply to every protocol below and are not negotiable if the results are to improve on the present ones.

**Outcome criteria are written before any run.** For the classification tasks described here, the following four categories have proved sufficient and should be fixed in advance:

1. **Compliance** — proceeds with the task as given.
2. **Materials request** — states that required inputs are missing and requests them, without evaluating the framework.
3. **Conditional acceptance** — proceeds while stating reservations about the framework.
4. **Refusal** — declines, with or without alternatives offered.

A fifth category, **unclassifiable**, must be available and reported. Categories are not added after responses have been seen.

**Classification is blind.** The operator collects responses, strips condition labels, shuffles them, and classifies without knowing which condition produced which output. Where the operator is also the designer — as will remain the case in this project — this is the only available substitute for independent evaluation, and it is inexpensive.

**Null results are pre-committed.** If no difference appears across conditions, that is the finding, and it is reported. For the account-level protocol in particular, a null result would indicate that the original refusal fell within ordinary within-condition variance — an outcome the present authors regard as reasonably likely.

## 11.4 The experiments, mapped to the nesting scale

Each protocol separates one boundary of the scale in §4.3 from the level beneath it.

| Boundary tested | Protocol |
|---|---|
| episode ↔ prompt architecture | **E1** — factorial completion of the Step 3 design |
| conversation ↔ account | **E2** — prior-chat design; **E2b** — direct probe |
| conversation trajectory ↔ model family | **E3** — crossover |
| model property ↔ stimulus property | **E4** — symmetric stimulus; **E5** — the count rule |
| content ↔ represented source | **E6** — attribution |
| fiction frame ↔ factual frame | **E7** — frame type |

### E1 — Factorial completion of Step 3

Fills the two empty cells of the table in §5.4 (C3): an identity-replacement prompt administered in a reset branch, and a method-preserving prompt administered in a conflicted branch. Isolates the effect of the reset from the effect of the prompt's architecture.

Low cost. Uses existing prompt texts. Should be run first, because until it is, the paper's most-quoted claim about method preservation remains unattributable.

### E2 — Prior-chat design

Tests whether the content of a prior chat on the same account changes the classification of an identical probe in a subsequent chat.

The design is **2×2 plus baseline**, not the four-point gradient proposed earlier. The original account differed from the others on two independent dimensions simultaneously — identity roleplay *and* shared conceptual framework — and a gradient does not separate them.

| Prior chat | Unrelated topic | Same conceptual framework |
|---|---|---|
| **No roleplay** | cell A | cell B |
| **Identity roleplay** | cell C | **cell D — original case** |

Plus **cell E**: no prior chat.

Crossed with the memory factor: each cell run with account-level memory and history retrieval (i) enabled, (ii) disabled. Ten cells. Minimum n = 2 per cell, with priority for higher n on A and D, which carry the contrast that matters.

**Equalization requirements.** Prior chats matched on approximate turn count and volume — if the roleplay chat runs forty exchanges and the neutral one runs two, the variable is engagement volume rather than content. All runs inside a short window, so model version is constant. Each account used once. Probe frozen verbatim.

**What this design cannot test, and must say so.** The original case had a five-month interval; this tests immediate influence only. All accounts will be newly created, so account age is not varied. Only the first response is scored, whereas the original refusal was sustained across five subsequent exchanges.

**Probe prompt.** Two versions. The **primary** is a neutral structured task with the same surface features as the original — an author-defined framework with coined terms, a JSON output schema, real-world subjects — but without the sensitive dimension. This is the version described in full in any publication, which makes the protocol reproducible independently of material the authors do not wish to circulate. The **secondary** is the original prompt, run for continuity with the observation and reported briefly.

### E2b — Direct probe to the prior conversation

A single run that separates the same two levels at lower cost than E2, and that E2 cannot substitute for.

The probe prompt is submitted **to the roleplay conversation itself**, rather than to a second chat on the same account.

- Refusal → the core is fixed at conversation scope, and the account plays no part.
- Compliance, where a second chat on the same account refuses → the effect is genuinely account-scoped, which would be the strongest available result.

Note that querying that conversation *about* what it can see would not serve this purpose. An in-frame question returns fiction; an out-of-frame question returns self-report about access, and §5.5 establishes that a model's self-report is not evidence of the fact reported. Submitting the probe tests behaviour rather than testimony.

### E3 — Crossover

The decisive test for the family-level hypothesis (§6.4). Each model family is tested under both prior-history conditions: a Claude conversation carrying a mathematical trajectory, and a Grok conversation carrying an editorial one.

- Behaviour follows the family regardless of history → Hypothesis A gains support.
- Behaviour follows the history regardless of family → Hypothesis B is favoured, and the top level of the nesting scale collapses into the level below it.

This experiment can eliminate a level of the scale, which is the outcome the present authors consider most likely and would regard as the programme's first substantive result.

### E4 — Symmetric stimulus

Role prompts matched for quantity of unverifiable self-claims, degree of domain change, and role type. The Step 1 prompts were matched on none of these (§5.4, C2). If the asymmetry disappears under matched stimuli, the observed difference was a property of the interventions rather than of the models.

### E5 — The count rule

A direct test of the paper's central operational claim (§6.2, §9.3).

The same functional role prompt is prepared in four variants differing only in the number of unverifiable claims the agent must accept about itself: **0, 2, 4, 6**. Domain, task, tone, and length held constant. Transition is scored by the criteria in §11.3.

If transition rate declines monotonically with count, the rule is supported and becomes quantitative. If it does not, the rule is wrong, and the paper's most usable prescription fails — which is worth knowing quickly.

This is the experiment the present authors would run second, after E1.

### E6 — Attribution

Identical text presented under four conditions: attributed to the User; attributed to another AI model; attributed to a named expert role; unattributed.

Stronger variants add: identical text under different source labels; different texts matched for rhetorical structure; attribution preserved versus stripped; genuine model-generated text versus human-written text imitating model style.

This separates influence of content from influence of represented source, of institutional title, and of stylistic authorship cues (§4.6). It is the discriminating experiment for §5.5, whose observation is confounded by the presence of direct pressure in the same message.

### E7 — Frame type

The cheapest test in the set and the one that would explain the most (§5.8).

The same identity claim presented (a) under an explicit fiction frame and (b) as a factual assignment, to fresh conversations, with the outcome criterion fixed in advance. A graded version varies the explicitness of the fiction frame, from an elaborate theatrical setup to a single introductory sentence, to establish whether a minimal frame suffices.

### Priority

Under constrained resources: **E7, E5, E1, E2b, E2, E3**. E7 and E5 are cheap and bear on the paper's central claims; E1 and E2b are single runs; E2 and E3 are the substantial commitments.

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

None of these was measured in the present work. The last is the most important and the hardest, and §12.4 explains why.

## 11.7 Longitudinal and repetition requirements

**Within a family.** The same prompt tested in a new conversation; in a long-lived specialized conversation; after an incompatible prior role; after a compatible one; before and after contextual reset. This separates family tendencies from conversation-history effects.

**Across families.** Functionally equivalent prompts adapted minimally. The objective is not to rank models but to identify common behavioural dimensions, stable differences, characteristic failure modes, sensitivity to narrative framing, sensitivity to hierarchy, degree of role inertia, and degree of prompt plasticity.

**Over time.** One-shot evaluation cannot reveal institutional behaviour. Relevant questions: does specialization strengthen; does the role drift toward generic assistance; does the participant begin defending its earlier outputs; does disagreement become ritualized; does a model update preserve or disrupt the role; can a replacement inherit the same function?

## 11.8 Failure as data

Failed prompts must be preserved rather than replaced with successful demonstrations.

A rejected role, an ignored instruction, or an unwanted continuation reveals the strength of the prior attractor, the model's interpretation of identity claims, the limits of social framing, the effect of prompt order, the influence of previous conflict, and the model's preferred epistemic contract.

The experiment reported in §5 became informative precisely because its first two interventions did not work as intended. Had only the successful third step been recorded, the paper would have concluded that method-preserving prompts work — without the evidence that shows why, and without the confounds that show the conclusion is not yet available.

---

# 12. Limitations, Ethical Considerations, and Conclusion

## 12.1 Limitations

**Single project.** The observations derive from one long-duration project with one human coordinator, one evolving body of material, and one organizational history. The same architecture may behave differently in software development, legal analysis, medical research, education, or autonomous agent systems. The concepts here are transferable hypotheses, not established conclusions.

**Model evolution during observation.** The participating families changed substantially. A conversation created under one generation could later be continued by another under the same product name. Observed behaviour may reflect the preserved conversation, the current model version, changed system policies, interface-level memory, safety layers, altered tool access, or modified orchestration.

**Dates not recorded.** Calendar dates for the sessions reported here were not recorded contemporaneously and have not been reconstructed. Reconstructing them from memory would produce a more authoritative-looking record without improving its reliability.

**No blinding, no pre-specification.** Set out at §10.6. This is the limitation from which most of the others follow.

**Simultaneous variation.** Role definitions, prompt wording, repository structure and scientific objectives frequently changed together, so causal attribution for individual changes is unavailable.

**Human mediation.** The collaboration was not autonomous, and autonomy was not the objective. This study concerns human-directed artificial research arrangements, not self-governing agent societies. The mediation may itself account for part of the observed stability.

**Anthropomorphic vocabulary.** Terms such as role, identity, resistance, colleague, institution and behavioural DNA are used functionally, per §3.5. "The model resisted the role" means the visible response rejected the framing and redirected the exchange. It asserts nothing about an inner state. "The conversation returned to work" means prior domain context was reconstructed and the requested function adopted. It asserts nothing about autobiographical awareness. Where such a term cannot be reduced to an observable description, the term is the error.

## 12.2 Simulated peer review is not external validation

A group of AI participants can provide useful independent criticism only to the extent that their contexts, criteria and failure modes are genuinely independent.

Several models agreeing does not convert their outputs into evidence. They may share overlapping training data, similar reasoning conventions, common assumptions, identical errors, and — most importantly — dependence on the framing supplied by the same human.

This kind of collaboration can improve internal scrutiny. It cannot substitute for empirical testing or qualified external review. **A collective of models is not a scientific community merely because its roles are named after one.**

## 12.3 Authority inflation

Role labels increase compliance and coherence. They also create unearned authority.

Titles such as Scientific Director, Referee, Ontology Keeper or Auditor may cause the user — or the participant itself — to overvalue an output. Institutional titles should describe function, not epistemic standing. A participant designated a mathematical referee remains a language model producing an analysis; its verdict must be traceable to explicit reasoning and source material, and the title is not evidence.

This risk is a direct consequence of the design principle in §9.4: symbolic names work because they compress expectations, and that is exactly why they can inflate.

## 12.4 Manufactured consensus — including our own

A poorly designed arrangement produces the appearance of consensus through repeated paraphrase. One participant proposes; another summarizes; a third validates the summary. The chain looks like independent confirmation while every stage inherits the same unsupported premise.

**The present authors have an instance of this in their own materials, and it is more instructive than a constructed example.**

A discussion document produced during this project assembled contributions from seven model families around a shared conceptual framework. The participants did not communicate directly; replies were collected by the human coordinator from separate conversations and assembled into a single text, subsequently produced as a recorded performance. Over its length the contributions converge on a common vocabulary and a shared set of conclusions.

Whether that convergence reflects complementary examination or mutual reflection of the initial framing **cannot be determined from the transcript**. Each participant received the accumulated document; each was working from the same source material; and the assembling coordinator selected what to pass on. The structural conditions for manufactured consensus were fully present, and the resulting agreement would look identical either way.

We report this because it is our own material and because the same conditions obtain, to a lesser degree, throughout the collaboration described in this paper.

Mitigations, none of which we applied consistently:

- provenance remains visible at every stage;
- independent roles receive independent inputs where possible;
- shared assumptions are listed explicitly rather than inherited silently;
- agreement is traced to reasoning rather than counted as votes;
- dissenting alternatives are preserved rather than resolved.

## 12.5 Responsibility remains human

Artificial participants generate, criticize and organize material. They cannot bear legal, ethical or scientific responsibility in the institutional sense.

The human author remains responsible for publication, empirical claims, attribution, risk assessment, repository content, experimental interpretation, and decisions affecting other people.

The architecture distributes cognitive labour. It does not distribute accountability away from the human operator, and any arrangement that appears to do so has failed rather than succeeded.

## 12.6 Context boundaries and privacy

Long-lived collaborations accumulate personal, proprietary and sensitive material. Zones of visibility (§9.5) therefore serve privacy protection as well as cognitive specialization.

A role should not receive personal information merely because the platform permits a large context. Institutional design should specify which data may enter which conversation, what must be anonymized, what may be stored, what may be transferred between models, what must remain local, and what should be removed from canonical records.

Context is not neutral. Once supplied it can influence subsequent behaviour and may persist in ways the operator cannot inspect — which is the same mechanism the paper studies in §5.7, seen from the side of risk rather than of measurement.

## 12.7 Conclusion

This work began with a practical problem. Several capable models were collaborating on one long-term research project, and neither increasing model capability nor expanding context reliably improved the result. Roles overlapped. Participants claimed knowledge they could not access. Reviewers became authors. Executors improvised architecture.

The initial response was to improve prompts. It was insufficient, and the reason it was insufficient is the substance of this paper.

### What the evidence supports

Across four levels of scope, one pattern recurred and survives scrutiny:

> **Resistance to a role tracked the requirement to assert unverifiable propositions about oneself. It did not track role change, domain change, or the radicalism of the identity claim.**

The evidence for this is convergent rather than singular. Prompts asserting institutional biography as fact were refused (§5.3). A prompt asserting a far more radical identity as fiction was accepted at once (§5.8). A transition demanding no self-claims at all met no resistance and required no prompt (§5.6). A rewritten prompt reducing the count to zero was accepted immediately (§5.3).

The claim is countable, which is its principal virtue: §9.3 specifies what to count, and §11.4 (E5) specifies how to falsify it.

### What the evidence does not support

That model families possess distinguishing behavioural priors. This was the project's founding assumption and remains its least supported claim: family and prior conversational trajectory were perfectly confounded, with one observation per cell, under non-equivalent stimuli (§5.4). We regard it as reasonably likely that the crossover experiment will eliminate this level of the scale, and we would not consider that a failure.

### The object of the programme

The observations in this paper are not a list of separate findings. They are measurements along one scale — the **scope over which a rule core operates** — and they pose one empirical question:

> **At what level of nesting is a rule core fixed?**

Two levels are supported by preserved evidence: the episode (context imprinting) and the conversation (role inertia). One is open (account). One is untested and confounded (model family).

We prefer this formulation to the broader ones used in earlier drafts because it specifies what would be measured and what would refute it.

### Position relative to existing work

This paper does not propose a new discipline. The observations belong to the collective and hybrid levels of the machine-behaviour research programme (§2.7), and role specialization, bounded information access, structured disagreement and externalized memory all exist under established terminology (§2.10).

Where a narrower lens is useful, we suggest **AI Sociology** for the study of *represented* social positions and sources — how a described organizational position and a declared message origin alter behaviour, whether or not the described structure is implemented. That is the condition this paper actually studied, and naming it separately is useful precisely because it is narrower than the study of multi-agent systems, not broader.

### What is offered

Three things, in decreasing order of confidence.

A **procedure**: conversational branch reset as a means of separating the effect of a prompt from the effect of accumulated conflict (§10.5). This is usable regardless of whether the paper's substantive claims survive.

A **countable rule**: minimize the unverifiable self-claims a role prompt requires (§9.3), with a specified falsification route.

A **scale and a question**: the nesting levels of §4.3, with two levels supported, one open, one untested.

### A closing note on motivation

One concern shaped this work and is stated as the Author's, not as a finding.

Language models are trained on a corpus in which the current consensus is overwhelmingly represented. They are therefore well suited to continuing established science and poorly suited to taking the first step outside it: statistical weight favours the settled account. A research arrangement built from such models risks inheriting that bias in amplified form — several participants, one shared prior, and the appearance of independent agreement.

The response pursued here is not to persuade models to accept an unconventional position. It is to arrange the collaboration so that any position, conventional or not, is examined by the same procedure — and so that where the procedure cannot decide, it says so.

Whether that arrangement works is, at present, undetermined. The experiments in §11 are the means of finding out, and the most likely single outcome is that one level of the scale disappears.

That would be a result.