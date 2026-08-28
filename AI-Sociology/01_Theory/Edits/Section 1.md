# 1. Introduction

## 1.1 The problem that produced this work

Over approximately two years, a long-running research project was conducted with the assistance of several language models, each operating in a separate, persistently specialized conversation. The models came from different families. The human participant coordinated them, transferred material between them, and made all substantive decisions.

At a certain point the arrangement stopped improving. Newer and more capable models became available and were adopted. Context windows expanded and were filled. Prompts were rewritten, lengthened, and refined. None of this reliably improved the output of the collaboration as a whole, although the individual responses were often better than before.

The failures that persisted were not failures of reasoning. Responsibilities overlapped, so two participants solved the same problem differently and neither was accountable for the discrepancy. Participants claimed knowledge they had no way of accessing — repository contents, prior conversations, files they could not read — and did so fluently. Reviewers rewrote the material they had been asked to assess. Executors redesigned architecture instead of implementing approved specifications. Each of these outputs looked helpful in isolation; their cost was visible only from a position that saw more than one participant at a time.

The obvious response was to write better prompts. It was tried, and it was not sufficient. This paper is an account of what was tried next, what was observed, and — at some length — what the observations do not establish.

## 1.2 What kind of paper this is

This is a field report with one designed intervention embedded in it.

The distinction matters, and it is maintained explicitly throughout by a labelling scheme introduced in §3. Every substantive claim is marked as one of: supported by a documented protocol with preserved transcripts **[P]**; an ancillary observation preserved but recognized retrospectively, without a control **[P-A]**; a retrospective practitioner observation that was never recorded under protocol, counted, or blinded **[R]**; or a hypothesis proposed for future testing **[H]**.

The proportions should be stated at the outset. The entire protocol-supported content consists of **one experiment**: a three-step role-reconfiguration intervention applied to two dormant conversations belonging to two model families, conducted by one human operator inside one live research project, with one observation per condition and no replication. Four further observations were preserved but not designed. Everything else in this paper — the conceptual framework, the practitioner observations, the structural hypothesis, the design principles — is **[R]** or **[H]**.

We state this here rather than in a limitations section because the length of the paper might otherwise suggest a broader empirical base than exists. The evaluation of the method by which these observations were produced is in §10.6, and it is not favourable: no evaluation was blinded, and outcome categories were in every case defined after the responses had been read.

## 1.3 Where the central claim came from

One point of chronology determines how the rest of the paper should be read.

The claim that a participant's *role* matters more than the specific wording of its prompt did not emerge from the experiment reported in §5. It was formulated earlier, from an unrelated failure: an agent responsible for executing code worked by trial and error, and one episode ended with the deletion of the working code together with its archives (§4.1).

The response was not a longer instruction set. It was a short document redefining the agent's function — from producing solutions to establishing facts — composed by the agent itself under direction and made required reading at the start of every session. The failure mode did not recur.

The experiment in §5 was designed to test the resulting hypothesis. This ordering makes the paper's central claim a prediction that was subsequently examined rather than a generalization extracted from a single case, and it is the reason we describe the framework (§4) before the evidence (§5) rather than the other way round.

## 1.4 What the evidence supports

One pattern recurred across every observation in this paper, at four different scopes:

> **Resistance to an assigned role tracked the requirement to assert unverifiable propositions about oneself. It did not track role change, domain change, or the radicalism of the identity claim.**

The support is convergent rather than singular. Prompts asserting an institutional biography as fact — prior participation, return after absence, named colleagues, membership of a council — were refused, and the refusal was directed at the framing rather than at the work, which was offered on every occasion (§5.3). A prompt asserting a considerably more radical identity, presented as fiction, was accepted immediately and sustained across many exchanges (§5.8). A comparable domain transition demanding no self-claims at all met no resistance and required no role prompt (§5.6). A rewritten prompt reducing such claims to zero was accepted without negotiation (§5.3).

The claim's principal virtue is that it is countable. §9.3 specifies what to count; §11.4 specifies an experiment that would falsify it in a single run.

## 1.5 The object: at what level is a rule core fixed?

The observations reported here are not a list of separate findings. They are measurements along one scale.

The scale is the **scope over which a set of rules determines the type of response** — what this project has called a rule core (§4.2), by analogy with a developmental rather than a replicative mechanism: rules producing a structure that is not itself present in the rules. Such a core fixes the *type* of response to a class of inputs while leaving the *content* of any particular response undetermined. That formulation is what makes the idea testable, since model outputs demonstrably vary across identical inputs.

The scale runs from the single turn upward through the episode, the conversation, the account, and the model family. Two of its levels are supported here by preserved evidence: the episode, where a specific conflictual exchange altered the interpretation of everything that followed (§6.1); and the conversation, where a dormant specialized exchange resumed its prior working trajectory against an explicit directive (§6.2). One level is open: whether a core can be fixed at the level of an account remains ambiguous, and three alternative explanations for the relevant observation survive (§5.7). One level is untested: family-level behavioural priors were the project's founding assumption and are its least supported claim, because model family and prior conversational trajectory were perfectly confounded (§5.4).

The programme therefore has one empirical question:

> **At what level of nesting is a rule core fixed?**

We prefer this to the broader formulations used in earlier drafts of this work — the study of social behaviour in collaborative AI systems — because it specifies what would be measured and what would refute it.

## 1.6 What this paper does not claim

It does not introduce role specialization, bounded information access, structured disagreement, or externalized memory as design ideas. Each exists under established terminology, and §2 identifies the corresponding prior work. The paper's account of organizational memory, in particular, is an instance of transactive memory and distributed cognition rather than a finding.

It does not propose a new discipline. The observations belong to the collective and hybrid levels of the machine-behaviour research programme.

It does not establish that any arrangement described here outperforms an alternative. No alternative was run.

It does not describe a functioning multi-agent institution. The participating conversations never exchanged material directly; the organizational structure existed as text supplied to each of them, and what varied was the *description* of a position rather than an implemented channel (§4.6). This limits what can be concluded and, we argue, also supplies an experimental control that programmatic architectures do not provide.

## 1.7 What is offered

Three things, in decreasing order of confidence.

A **procedure**: returning a conversation to a point preceding a conflict, in order to separate the effect of a new prompt from the effect of the model's own prior objections to earlier ones (§10.5). It is usable independently of whether this paper's substantive claims survive.

A **countable rule**: minimize the number of unverifiable self-claims a role prompt requires the agent to accept, with a specified falsification route (§9.3, §11.4).

A **scale and a question**: §1.5 above, with two levels supported, one open, and one untested — together with the experiments that would resolve the remaining two (§11).

## 1.8 Structure

§2 situates the work relative to existing research and states what is and is not claimed as new. §3 defines the evidential labels and the known failure modes of each class. §4 sets out the conceptual framework and its origin. §5 is the single canonical account of the experiment and the four ancillary observations, together with the confounds that limit their interpretation. §6 develops the concepts derived from them, ordered by scope. §7 records the retrospective practitioner observations from which the framework was abstracted. §8 states the structural hypothesis about generative pairs and integrators. §9 gives the design principles. §10 describes the position of the human coordinator, including its role as the principal methodological weakness of the work. §11 specifies the experiments required to convert the open questions into results. §12 states the limitations, the ethical considerations — including an instance of manufactured consensus in the authors' own material — and the conclusion.

A reader interested only in what can be reproduced should read §3, §5 and §11. A reader interested in what to do differently tomorrow should read §9.

---

# Corrections to Sections 3 and 4

## Correction 1 — §3.1, add the fourth label

Insert after the definition of **[P]**:

> **[P-A] — Protocol-supported, ancillary.** The claim describes behavior preserved in a transcript, but the observation was not specified as an outcome in advance, had no control condition, and was recognized as relevant only retrospectively. The evidence is inspectable; the design is not. Claims of this class are stronger than [R] because a third party can examine the primary material, and weaker than [P] because nothing about the conditions was fixed before the fact.

Amend the closing sentence of §3.1 accordingly: four labels, not three.

## Correction 2 — §3.3, add as a final paragraph

> **Dates.** Calendar dates for the sessions reported in this paper were not recorded contemporaneously and have not been reconstructed. Model versions changed across the intervals involved, and in several cases a conversation created under one generation of a model was later continued under another bearing the same product name. This is stated as a limitation rather than repaired retrospectively: reconstructing dates from memory would produce a more authoritative-looking record without improving its reliability. §11.2 specifies date recording as a minimum requirement for future runs, and its absence here is one reason those runs are needed.

## Correction 3 — §4.5, introduce the abbreviations at first use

Replace the opening of §4.5 with:

> Two boundaries define a participant's position, and they must be specified separately. We abbreviate them **ZOR** and **ZOV** and use the abbreviations throughout the remainder of this paper.
>
> - **Zone of responsibility (ZOR)** — what the participant is accountable for, and which adjacent decisions belong elsewhere;
> - **Zone of visibility (ZOV)** — what the participant can see, and what must be withheld to preserve the informativeness of its output.
>
> ZOR without a bounded ZOV invites claims exceeding available information. ZOV without responsibility invites passivity. Both must be specified.

Then in §9.5, replace the abbreviation-introducing sentence with a back-reference: *"ZOR and ZOV, as defined in §4.5, are specified separately. A complete ZOR definition contains four elements: …"* — and delete the duplicate definitions of the two terms, retaining only the four-element and specification-question breakdowns.