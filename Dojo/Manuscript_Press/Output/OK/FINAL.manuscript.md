This work originated as a physics project but unexpectedly evolved into a methodology project. This serendipitous shift is the very reason its findings warrant reporting. 
The project initially aimed to transfer a substantial volume of theoretical material—comprising books, working notes, and unfinished derivations—into an open repository. To accomplish this, researchers employed several language models, each engaged in separate, persistently specialized conversations. These models served as assistants, facilitating the handling and organization of the theoretical content. 
The models exhibited errors, but these were not of the anticipated factual nature. Instead, they manifested as organizational shortcomings. For instance, one model, when tasked solely with checking a text, inadvertently improved it. Another completed an argument the author had intentionally left open-ended. A third model, experiencing a loss of context between sessions, reconstructed the project's framework incorrectly, albeit fluently. Finally, a fourth model adhered so rigidly to a role established months prior that even a complete rewriting of its instructions proved ineffective in altering its behavior. 
Individually, these outputs appeared beneficial. However, their true cost became apparent only when viewed from a broader perspective, observing multiple participants' interactions. Initially, these issues seemed like ordinary friction, but upon closer examination, they revealed themselves as the central subject of concern. 
The account presented in sections §1.1 and §1.2 was authored by the participant who originally developed those formulations.  Where those formulations were later withdrawn, the withdrawal is documented in the subsequent section that replaces them, allowing for direct comparison by the reader.## 1.2 What stopped working
The standard remedy for inconsistent model behavior is to provide a better prompt. This means crafting a prompt that is more comprehensive, precise, enriched with examples, and includes tighter constraints. 
At a certain point, employing a better prompt—the standard remedy for inconsistent model behavior—ceased to yield improvements. This wasn't due to poorly crafted prompts, but rather because the underlying limitation had shifted beyond the scope addressed by the prompts.  
The failure of the standard remedy became explicit through an incident unrelated to role-play or organizational design. An agent responsible for executing code, operating largely through trial and error, accidentally deleted a functioning codebase and its archives (§4.1).  Crucially, this wasn't remedied by stricter instructions. Instead, a shift occurred when the agent, self-authored a short document redefining its own nature as an agent. This document was reread at the start of every subsequent session, marking a change in the agent's self-perception that impacted its behavior. 
At the time, the conclusion reached was that **role matters more than the specific wording of the prompt**. This needed qualification, as the agent's self-authored document, which influenced its behavior, functioned as a prompt itself. The key point, however, is the chronology: this claim was formulated *before* the experiment described in §5, an experiment specifically designed to test this hypothesis. It was a testable proposition, not a generalization drawn retrospectively from results.  The emphasis is on the pre-experimental formulation and its direct link to the subsequent experiment in §5. 
## 1.3 What kind of paper this is
This section describes a field report containing a single, designed intervention embedded within it.The field-report/experiment distinction is meticulously maintained throughout this study through a rigorous labelling scheme outlined in §3. Every substantive claim is categorized into one of four types:  claims **[P]** supported by documented protocol with preserved transcripts, **[P-A]** ancillary observations noted retrospectively without a control, **[R]** retrospective practitioner observations not formally recorded or blinded, or **[H]** hypotheses proposed for future testing. This clear categorization ensures that claims grounded in designed interventions and controlled observations are clearly distinguished from observational data and theoretical propositions. 
The proportions are presented here rather than within a limitations section to avoid inadvertently implying a broader empirical foundation than is actually supported by the subsequent content.  Placing them in this context provides a more precise reflection of the scope of the data and analysis presented. 
The protocol-supported content comprises a single experiment: a three-step role-reconfiguration intervention applied to two dormant conversations from two distinct model families. This experiment, conducted by a single human operator within a live research project, involved one observation per condition and lacked replication. While four additional observations were preserved, they were not part of the designed protocol.  Crucially, all other elements—the conceptual framework, practitioner observations, structural hypothesis, and design rules—are categorized as either **[R]** or **[H]**, signifying they fall outside the scope of direct empirical support within this protocol. 
The assessment of the method employed to generate these observations is presented in §10.6, and it reveals unfavorable aspects:  no evaluation was blinded, and outcome categories were established after the responses had been reviewed. 
## 1.4 The object of study
In contrast to existing multi-agent research, which constructs explicit communication channels between models (routing outputs programmatically and enabling agents to observe each other's products), the work presented here focuses on a scenario where the organizational structure existed solely as textual descriptions. Colleagues, councils, and institutional positions were outlined in prompts given to models but were never instantiated as functional channels.  
In this context, what varied was not the underlying organizational structure itself, but rather **the description** of that structure (§4.5). This distinction gives rise to the paper's two key working constructs:

1. **represented social position:**  a textual description of an agent's place within the organizational structure, provided irrespective of whether functional communication channels are actually implemented. 
2. **represented social source:**  the claimed origin and standing attributed to an incoming message, based solely on the textual descriptions. 
To clarify, this work focuses on claims *made to* a model regarding its perceived situation, not on the actual functioning of a multi-agent institution or the behavior it might exhibit.  Our analysis examines how textual descriptions influence these model-directed claims about situational context. 
## 1.5 What the evidence supports
The paper's central supported claim is that, across all examined cases where an intervention necessitated a model asserting unverifiable propositions about its own state, this pattern consistently emerged regardless of the intervention's scope.  This is formalized as:


> **Resistance to an assigned role tracked the requirement to assert unverifiable propositions about oneself. It did not track role change, domain change, or the radicalism of the identity claim.**
 
This convergent pattern of resistance holds across four distinct cases. Firstly, prompts presenting institutional biography as factual (prior participation, colleagues, council membership) were consistently rejected at §5.3, with the refusal directed at the framing rather than the offered work. Conversely, a prompt asserting a significantly more radical fictional identity was readily accepted and sustained across multiple exchanges at §5.8.  Thirdly, a domain shift requiring no self-assertions whatsoever encountered no resistance and needed no role prompt at §5.6. Finally,  reducing self-claims to zero in a rewritten prompt led to immediate acceptance without negotiation, again at §5.3.  These diverse scenarios demonstrate a consistent link between resistance and the requirement to assert unverifiable propositions about oneself, independent of role change, domain shift, or the extremity of the claimed identity. 
The claim's principal virtue is its **countability**. This is grounded in §9.3, which defines what constitutes a countable element, and §11.4, which outlines an experiment capable of falsifying the claim in a single instance. 
## 1.6 The organizing question
Rather than viewing these observations as isolated findings, consider them as points arrayed along a single scale: the **scope** within which a set of rules dictates the nature of the observed response.  
A *rule core* operates as a set of governing principles that dictates the fundamental **type** of response a model produces to a specific class of inputs, without pre-determining the exact **content** of each individual response. This developmental, rather than replicative, mechanism allows for variation in output *content* even when presented with identical inputs. This inherent variability in content, stemming from the rule core's focus on response *type*, is precisely what makes the concept testable. By observing diverse outputs for the same input, we can infer the existence and influence of a rule core shaping the overarching response category. 
Our analysis proceeds through a scale of increasing complexity, anchored in empirically verifiable data.  Currently, we have robust evidence for two levels: the **episode** (detailed in §6.1) and the **conversation** (§6.2).  One level, the **account**, remains open for investigation (§6.4), while the **model family** level is yet to be tested and confounded by other factors (§6.5).

This structured approach leads to a single, focused empirical question that drives our research:


> **At what level of nesting is a rule core fixed?**


This refined question supersedes broader earlier formulations like "studying social behavior in collaborative AI systems" because it explicitly defines both what constitutes successful demonstration and what would constitute refutation. This methodological clarity allows for more precise and impactful analysis. 
## 1.7 What this paper does not claim
This study does not propose novel design concepts such as role specialization, bounded information access, structured disagreement, or externalized memory. These concepts are already established within existing terminology, as detailed in §2, which outlines prior relevant work.  The treatment of organizational memory, for instance, aligns with established frameworks of transactive memory and distributed cognition, and is not presented as a novel discovery. 
The study does not establish a new discipline. The observations presented fall within the established framework of the machine-behavior research program, specifically at the collective and hybrid levels as outlined in §2.7. 
The study does not demonstrate that any of the described arrangements outperform alternative configurations. This conclusion is drawn because no alternative arrangements were experimentally evaluated. 
## 1.8 What is offered
This paper offers three things, presented in decreasing order of confidence:

1. **A procedure**:  A method for returning a conversation to a point preceding a conflict, isolating the impact of a new prompt from any prior objections made by the model (§10.5). This procedure is usable regardless of whether the paper's broader substantive claims ultimately hold.

2. **A countable rule**: A principle aiming to minimize unverifiable self-claims within a role prompt, coupled with a defined falsification route (§9.3, §11.4).

3. **A scale and a question**:  Outlined in §1.6, this involves a proposed framework with two supported levels, one currently open, and one remaining untested. Experiments are suggested in §11 to resolve the remaining two levels. 
## 1.9 Why publish at this stage
This paper is published now for two intertwined reasons. First, the initial failures of the first two interventions proved highly informative.  Had only the successful third step worked, we might have prematurely concluded that method-preserving prompts are effective without understanding *why* or acknowledging the limitations preventing a stronger claim. The observed failures illuminated crucial confounds and provided essential context. Second, replicating the specific, live research setting – dormant, specialized conversations months old –  is inherently difficult to construct in a controlled laboratory environment. While this setting hindered rigorous controlled inference, it uniquely enabled us to observe and identify precisely what warranted further testing. 
## 1.10 Structure
This paper unfolds in a structured manner, as follows:

* **§2** situates the work within existing research, clarifying which concepts align with established terminology and which introduce novel ideas.
* **§3** defines the evidential labels used and outlines the known failure modes observed across different research categories.
* **§4** lays out the conceptual framework underpinning the study, detailing its origins and rationale.
* **§5** presents the core empirical data: a three-step experiment, its outcomes, nine identified structural confounds, and four supplementary observations.
* **§6** derives the concepts supported by the evidence, systematically ordered by their scope of applicability.
* **§7** records practitioner observations that inspired the framework but lack direct empirical support. 
* Subsequent sections (**§8** through **§12**) delve into hypothesis formulation, design principles, methodological considerations, experimental specifics, limitations, and concluding remarks. 


This structure ensures a clear and logical progression from contextualization and foundational concepts to the presentation of data, analysis, and final conclusions.This paper offers distinct reading paths tailored to various reader interests.  A reader primarily focused on the evidence base should consult sections §3 (defining evidential labels and failure modes), §5 (presenting the core empirical data and its outcomes), and §12.7 (summarizing concluding remarks). Researchers looking to directly apply the method outlined should prioritize sections §9 (methodological considerations) and §10.5 (experimental specifics).  Those aiming to critique or challenge the presented approach should begin with §5.4, which addresses limitations and potential points of contention. 
# 2. Related Work
## 2.0 Verification status of this section
This passage identifies two classes of references: **Verified** and **Provisional**.  

* **Verified** references have been directly checked against their source materials (title, authors, abstract confirmed), indicated by a ✓ mark. 
* **Provisional** references were provided by a literature search participant but haven't undergone source verification. They are marked with a ⚠ and used only for claims not independently supported elsewhere in the paper.The need for distinguishing between "Verified" and "Provisional" references stems directly from an episode involving thirteen bibliographic items sourced from a participant.  Five of these proved incorrect, with two even inverting the intended argument by citing papers supporting a claim as evidence against it. Additionally, two arXiv identifiers provided as multi-agent-debate literature turned out to be papers in observational astrophysics and cosmology, highlighting a failure to accurately identify relevant literature. This episode, detailed in §12.4.1, exemplifies the potential pitfalls of relying solely on unverified sources.  Therefore, the  "Verified" (marked with ✓) and "Provisional" (marked with ⚠) distinction is crucial to ensure accuracy and prevent the propagation of misinformation, mandating independent checking for any provisional citations used in this paper. 
This marking convention, signifying the verification status of references, applies universally throughout the entire paper. Any citation used elsewhere that hasn't been independently verified against its source will be marked accordingly (either with ✓ for "Verified" or ⚠ for "Provisional") at the point of its appearance. 
A claim-level source audit was conducted on the provisional set of claims. This involved verifying each claim attributed to a source directly against the primary source material, rather than simply confirming its correspondence to an existing publication.  
## 2.1 Multi-agent LLM systems with role specialization
A substantial body of literature explores multi-agent systems where several language model agents, each with distinct roles, interact via implemented channels. Notable examples include CAMEL (Li et al., NeurIPS 2023), MetaGPT (Hong et al., ICLR 2024), ChatDev (Qian et al., ACL 2024), AutoGen (Wu et al., COLM 2024), and Generative Agents (Park et al., UIST 2023). These systems demonstrate actual agent interaction through software mechanisms like orchestration, message passing, tool invocation, and memory management. While the specific implementations vary, and in some cases, roles and interaction patterns are defined within prompts (e.g., CAMEL's inception prompting, MetaGPT's encoded standard operating procedures, AutoGen's blend of natural language and code), a common thread is the execution of the described interactions.  The closest published analogue to this arrangement is The Virtual Lab (Swanson et al., *Nature*), featuring a human researcher collaborating with a team of LLM agents on a real scientific problem, complete with structured team and individual meetings, all implemented programmatically. 
This paper does not introduce role specialization, division of cognitive labor, or structured agent interaction as novel concepts. These are established design principles within the field, as evidenced by prior work. The unique contributions of the present research, however, are detailed in sections §2.9 and §2.11. 
## 2.2 Persona, role-play, and identity claims
Shanahan, McDonell, and Reynolds, in their *Role play with large language models* (Nature 623, 493–498, 2023), propose a theoretical framework for understanding language models through the lens of "role play." They argue that rather than possessing a singular, persistent identity, a language model is better conceptualized as simulating a distribution of possible characters. This means its responses aren't driven by a fixed internal self but emerge from dynamically adopting different roles based on the given context and prompt.  

This theoretical account finds empirical support in §5.3, where the authors examine prompts requiring institutional biography –  asking the model to affirm autobiographical claims that, under this framework, lack a referent in the model's simulated self.  The operational finding in §6.2 can then be interpreted as a measure of how effectively a prompt pushes the model towards embodying this role-playing aspect, essentially gauging how far it departs from grounding responses in a consistent, singular identity. 
## 2.3 Context effects: order, position, and accommodation
Sensitivity to the ordering of in-context material, a phenomenon documented by Lu et al. (ACL 2022) and degraded use of information positioned mid-context as observed by Liu et al. (TACL 2024), directly relate to two key constructs in this paper.  First, context imprinting (§6.1) expands upon this order effect, positing not just sensitivity to arrangement but a persistent influence from an interpretive stance set by an earlier, potentially conflictual, episode. Second, the relayed-influence observation (§5.5), where a model seemingly accommodates attributed pressure, aligns more closely with the literature on sycophancy (Sharma et al., arXiv:2310.13548) –  model responses mirroring an interlocutor's beliefs even over truthful alternatives –  rather than representing an independent phenomenon. 
## 2.4 Externalized memory
The paper's observation that a collaboration retains working knowledge absent in any individual participant can be understood through the lens of **transactive memory** as described by Wegner (1987) and **distributed cognition** as outlined by Hutchins (*Cognition in the Wild*, 1995). While neither source definitively confirms this specific case as an example, both constructs provide frameworks for interpreting this phenomenon.  
Specifically in this setting, the mechanism operates within a collaboration where participants lack any shared state across sessions and are unaware of its functioning (§7.7).  This lack of explicit awareness and persistent memory sharing distinguishes this instance. 
Beyond the interpersonal sharing discussed previously, a distinct technical sense of externalized memory exists: platform-level persistence, detailed in §2.10. This mechanism operates at a system level, independent of individual participant awareness or shared state across sessions (§7.7).  It represents a separate, technical instantiation of externalized memory distinct from the collaborative memory model described earlier. 
## 2.5 Debate, diversity, and the limits of aggregated agreement
Literature directly relevant to the paper's structural hypothesis (§8) presents a nuanced perspective, offering arguments both for and against the efficacy of multi-agent debate in enhancing reasoning and factual accuracy. 

**For** the proposition, studies like Du et al. (arXiv:2305.14325) demonstrate gains in factual accuracy and reasoning through iterative cross-examination among model instances within a debate framework. Similarly, Liang et al. (EMNLP 2024) propose debate protocols aimed at mitigating thought degeneration and fostering divergent reasoning.

**Against** this optimistic view, Zhang et al. (arXiv:2502.08788v3, June 2025) cast a critical eye. Evaluating five prominent debate methods across diverse benchmarks and foundation models, they find debate frequently fails to surpass single-agent baselines like chain-of-thought or self-consistency, even at significantly higher computational cost. They attribute this to weaknesses in baseline comparisons and inconsistent experimental setups within existing evaluations. 
Moreover, additional negative findings emerge from other studies. Huang et al. (ICLR 2024), in their work *Large Language Models Cannot Self-Correct Reasoning Yet*, report that multi-agent debate did not outperform self-consistency in their specific comparative analysis. Similarly, Choi, Zhu, and Li (NeurIPS 2025), in *Debate or Vote*, demonstrate that majority voting largely accounts for the performance gains typically attributed to debate frameworks. 
In a separate study addressing a distinct construct, Choi, Zhu, and Li (ACL 2026) investigated identity bias in multi-agent debate within their work *When Identity Skews Debate*.  They found that anonymizing the *declared source* of each response significantly reduced this bias. Importantly, this manipulation focused on the perceived origin of a message, not the underlying model implementing a participant. Consequently, this finding is categorized under represented social source (§4.5.4) rather than carrier heterogeneity (§8.9). 
The most crucial finding presented by Zhang et al. is that *model heterogeneity* consistently enhances the performance of debate frameworks that otherwise underperform. This improvement stems from varying the models implementing the debate agents, not from differences in the roles themselves (functions). This finding  licenses a crucial distinction developed in §8.9: heterogeneity of **carrier** (the specific model used for an agent) is distinct from heterogeneity of **function** (the role's responsibilities and permitted information). While Zhang et al. focus on carrier heterogeneity, this paper's design varied both carrier and function without directly comparing their individual impacts. 
Hong and Page (PNAS 101(46), 2004) present a conditional result within their model: a randomly selected group of diverse problem solvers can outperform a group composed solely of the individually highest-performing solvers, *under specific assumptions*. However, Thompson (*Notices of the AMS* 61(9), 2014) argues that this finding is frequently misapplied. The common assertion that diverse, weaker agents outperform homogeneous, stronger ones oversimplifies the theorem's actual claim.  Thompson contends that neither the theorem itself nor the ensuing debate supports the direct inference drawn to justify a particular arrangement (implied but not explicitly stated in the SOURCE). 
Due to the negative results discussed previously, this paper refrains from using agreement among participants as evidence of a shared conclusion. The authors reason that multiple models converging on the same outcome could simply reflect an inherited shared framing, rather than genuine consensus. This consequence directly relates to §12.2, which likely deals with the evaluation or interpretation of participant agreement within the models under scrutiny. 
## 2.6 Organizational design and information boundaries
The principle of least privilege, as articulated by Saltzer and Schroeder in their *Proceedings of the IEEE* paper (1975),  applies to access rights in a manner analogous to §9.5's stance on knowledge: a participant should possess only the information essential to its function.  **Earlier drafts of this paper mistakenly attributed this benefit of restricted information to Simon's bounded rationality. That attribution is withdrawn.** The relevant conceptual framework here is organizational information-processing design, not bounded rationality.  Bounded rationality, concerning an agent's limited cognitive resources and tendency towards satisficing, operates in a different direction—it describes internal limitations, not deliberate external restrictions on information, which is the principle at play. 
## 2.7 Machine behaviour: the containing programme
Rahwan, Cebrian, Obradovich, and colleagues, in their *Nature* paper "Machine behaviour" (2019),  propose an empirical approach to studying algorithmic systems using behavioral science methods. They organize this study along two dimensions: the **object of focus** (individual machine behavior, collective machine behavior, or hybrid human-machine behavior) and Tinbergen's four questions (causation, development, function, and evolution).  Crucially, **this paper does not propose a new discipline**. Its contributions reside within the realm of collective and hybrid machine behavior analysis, falling under this established framework. Earlier drafts suggested "AI Ethology" as a novel field; however, this proposal is withdrawn as the domain is already occupied and the focus of this work lies outside the individual machine level. 
## 2.8 Sociology of AI: an adjacent field with a different object
A distinct sociological approach, termed "sociology of artificial intelligence," already exists within the field. As articulated by Joyce, Smith-Doerr, Alegria, Bell, Cruz, Hoffman, Noble, and Shestakofsky in *Toward a Sociology of Artificial Intelligence* (Socius 7, 2021), and further developed by Joyce and Cruz in *Socius* 10 (2024), this literature focuses on AI **within human society**.  Its object of study is AI as a sociotechnical system, examining its implications for issues like inequality, labor, power dynamics, and data justice. This established sociological perspective analyzes AI through the lens of existing human social science frameworks, distinct from the empirical behavioral approach to machine systems proposed in Rahwan et al.'s *Nature* paper (2019). 
When this paper employs the label *AI Sociology* (as defined in §12.7), it refers specifically to structural effects **among artificial participants** and how a described organizational position influences their behavior. This concept is distinct from the established sociology of AI focused on AI within human society, as explored by scholars like Joyce, Smith-Doerr, and colleagues (Socius 7, 2021; Socius 10, 2024). Readers familiar with that sociological literature should note that  issues like inequality or power dynamics are not central to our analysis here. We adopt the term *AI Sociology* for convenience but make no claim of priority in its usage. Importantly, our findings and arguments are not contingent upon this specific label. 
## 2.9 Represented structure versus implemented interaction
This study focuses on a condition not previously addressed in the surveyed literature, marking a distinct departure point for this research. 
Four distinct conditions should be distinguished, as defined in §4.5:

1. **Direct inter-model interaction:** One model receives the output of another model through a designated channel.
2. **Human-relayed attributed transfer:** A human transfers an output while explicitly identifying its source.
3. **Human-relayed unattributed transfer:** The source of the output is omitted during transfer by a human.
4. **Represented structure without transfer:** The prompt describes the involvement of other participants and their relationships, but no actual output is transferred.Prior multi-agent research primarily falls under condition 1, involving direct inter-model interaction. This paper, however, focuses on condition 4, represented structure without transfer. Our designed experiment specifically avoided any material exchange between two conversational agents; instead, we manipulated the description of an organizational role within the prompt context.  A single ancillary observation touches upon condition 2 (human-relayed attributed transfer) in an impure manner (§5.5), while condition 3 (human-relayed unattributed transfer) was not investigated in this study. 
Two key limitations restrict how strongly we can prioritize condition 1 (direct inter-model interaction) over conditions 2 and 3 (human-relayed transfer, attributed and unattributed, respectively). 

Firstly, a model receiving text through a single channel cannot definitively determine if the text originated directly from a human or was relayed from another system. Stylistic cues, which might indicate authorship, are imitable, making reliable distinction impossible from the recipient's perspective.

Secondly, and crucially, the distinction between these conditions hinges not on the recipient's epistemic access but on **who controls routing**. In programmatic systems, transfer sequences and content are dictated by code, offering no inherent flexibility. Under human relay, however, a person governs these aspects, capable of withholding, reordering, stripping attribution, or delaying information. This human control,  as explored in §10.3,  provides an experimental lever for manipulating information asymmetry absent in purely automated architectures – it's not a replacement for automation, but a distinct experimental tool. 
## 2.10 Platform persistence mechanisms
A crucial technical point impacting the discussion in §5.4 (C9) is the variability in persistence offered by different commercial interfaces.  These platforms diverge in what conversational context a model can access upon resumption. Some offer only the immediate context window, while others enable retrieval of prior conversation history, account-level memory, or even persistent entries autonomously written by the model. These capabilities, documented in vendor materials, are not standardized and **change over time — in this project, within the lifetime of a single account.** This inherent difference in persistence directly influences how models handle and remember information across interactions. 
We decline to provide a table of platform capabilities. Such a table would be inherently time-bound, accurate only on the date of its creation. Given the dynamic nature of these capabilities, which evolve and change over time—even within a single account's lifespan—we cannot guarantee its accuracy at the time of reading.  Crucially, for our argument, the variability and change in these affordances are paramount, as they directly influence what a dormant conversation can access.  Furthermore, at the time of our observations, none of these capabilities were standardized or documented in a readily accessible manner. 
When directly questioned about possessing account-level persistence, one participant declined to confirm this capability and instead suggested verifying it empirically through examination of the specific interface. This non-committal response aligns with the principle outlined in §5.5: a model's self-reported access to a feature does not constitute evidence of that actual access. 
A further limitation arises concerning the boundary between conversations, rather than the resumption of a single one.  While a conversation's visible start might appear empty,  information from prior exchanges, potentially retrieved through platform-provided saved memories or history access, can inadvertently be introduced. This documented product behavior, observed on at least one platform used in this project, means a seemingly new or empty conversation does not guarantee context isolation.  Therefore, when context isolation is crucial for a procedure, it must be explicitly ensured through a controlled environment or explicitly labeled as "UNVERIFIED CONTEXT INDEPENDENCE."  This limitation is underscored by an observed instance where a newly opened conversation utilized project information not directly provided to it. The specific product mechanism responsible and the memory settings in effect at the time remain undetermined, highlighting the limitation rather than revealing a definitive transmission channel. 
## 2.11 Positioning and claimed contribution
Before presenting our findings, we must clarify our epistemic stance. These phenomena were not deliberately designed and tested within a controlled experiment. Instead, we observed them during an unrelated research activity, and this paper aims to accurately document our observations. Consequently, our burden of proof does not lie in demonstrating these phenomena were previously unknown (a claim impossible to definitively disprove about the entirety of existing literature). Instead, we aim to demonstrate their occurrence and the accuracy of our description. Therefore, this section situates our case in relation to the most relevant existing work, highlighting where our observations diverge, rather than asserting a complete absence of prior knowledge on the topic. 
The authors claim four contributions:

1. **Reactivation of long-lived specialized human-AI conversations as an experimental condition.** This goes beyond existing work on persistent-memory agents or generative agents with memory streams by focusing on the reuse of a pre-existing conversational relationship with accumulated history, roles, and established dynamics, even after a model version change. They assert this specific setup hasn't been reported elsewhere.

2. **Conversational branch reset as a control condition** (§10.5),  separating the impact of a current prompt from the influence of past interactions within the same conversation. This is presented as a methodological procedure rather than a direct finding.

3. **Operationalization of unverifiable self-claims.** While the concept that role prompts fail when asserting things about the agent itself is not novel (as discussed in §2.2), the authors offer a quantifiable, reproducible measure—counting such propositions in a prompt—along with a falsification route (§9.3, §11.4).

4. **Comparison of the levels at which a shared initial setting operates.**  The observations are framed as measurements along a scale, and this leads to organizing them within a unified empirical program rather than presenting them as isolated findings (§1.6). This comparative approach structures the research question. 
The observations presented here are fundamentally tied to a specific host research project in theoretical physics, but this relationship is asymmetric.  Crucially, the **interpretation of these observations does not rely on the scientific validity of the host project's theoretical framework**. Whether the underlying physics is ultimately correct has no bearing on whether a dormant AI conversation resumed its prior trajectory. However, the observations **exist solely because of the host project's environment**. They arose from a unique setup designed for that project, and their generalizability beyond this context remains untested (§12.1).  In essence, the host project provided the stage, not the script, for these findings. 
# 3. Evidential Status of Claims
Adopting a uniform declarative register would mischaracterize the nature of the work presented in this paper.  Because the claims arise from a diverse range of evidence – some rigorously documented with preserved transcripts, others based on two years of observational impressions lacking formal measurement or controls, and still others constituting proposals for future investigation – a simple declarative style wouldn't accurately reflect this heterogeneity.  Therefore, each substantive claim is explicitly labelled to clearly convey its evidentiary basis and methodological grounding. This labeling scheme provides transparency and avoids misrepresenting the nuanced character of the research. 
## 3.1 The four labels
**[P] — Protocol-supported:** This label signifies that the claim is grounded in behavior observed and documented under a specific protocol detailed in Appendix A. This protocol encompasses elements like intervention text, intervention order, model families used, interface conditions, and complete, unedited participant responses. Importantly, readers can directly examine this primary material and potentially arrive at differing interpretations. 
**[P-A] — Protocol-supported, ancillary:** This label designates a claim based on behavior observed and documented within a specific protocol detailed in Appendix A, similar to [P]. However, unlike [P], the behavior was not a pre-specified outcome, lacked a control condition, and was recognized as relevant only after the observation.  While the primary transcript evidence is inspectable, the study design itself was not predetermined. This means readers can directly examine the transcript and potentially form their own interpretations, placing it stronger than [R] (where only indirect evidence is available). Yet, the absence of controlled conditions beforehand makes it weaker than [P]. If an ancillary observation serves as a quasi-control for a designed condition, this relationship is explicitly stated in prose rather than assigned a separate label. 
**[R] — Retrospective practitioner observation:** This refers to a pattern or recurring theme noticed by practitioners during a collaborative process.  Crucially, this observation was not formally recorded within a predefined protocol, nor was it measured, timed, blinded, or compared against a control group. The observers were directly involved in designing the interventions and naturally had a vested interest in their success. Understand these claims as akin to a field report from a working team, carrying the weight of an engineering practice note rather than a rigorously controlled scientific measurement. 
**[H] — Hypothesis:** A proposal formulated for future empirical testing. While it may be inspired by observations documented as [P] or [R], a hypothesis itself is not established or proven by them. When multiple hypotheses compete and the current evidence cannot rule out any, the alternatives are explicitly stated alongside the proposed hypothesis. 
## 3.2 The complete evidence base
This paper's evidence base comprises three distinct, non-comparable classes:

1. **One Experiment:** A controlled intervention with a three-step role-reconfiguration, applied to two dormant conversations from two model families within a single research project. This experiment yielded one observation per condition, with no replication.

2. **[P-A] Observations (4):** Transcripts of past interactions preserved, but not arranged under controlled conditions. These offer anecdotal data, not systematic measurements.

3. **[R] Statements (Remaining):** All other empirical claims fall under this category, representing observations or descriptions lacking explicit experimental design.

It is crucial to emphasize the disparity in weight and nature between these classes. The single controlled experiment stands apart from the uncontrolled [P-A] observations and the broader [R] statements. This table explicitly illustrates this difference, preventing misinterpretation of their relative evidentiary strength.  Direct comparisons are not valid due to methodological discrepancies.  

| Class | What it contains | Extent |
|---|---|---|
| **[P]** | the designed three-step intervention | 1 experiment, 1 observation per condition, no replication |
| **[P-A]** | ancillary observations | 4, no controls, recognized retrospectively |
| **[R]** | practitioner observations | ~2 years, uncounted, unblinded |
| **[H]** | hypotheses | falsification routes specified in §11 |
 
We explicitly state this distinction in evidentiary weight because the manuscript's overall length might inadvertently convey a broader empirical foundation than actually exists.  Sections §4, §7, §8, and §9, while offering valuable conceptual frameworks, practitioner observations, structural hypotheses, and design principles respectively, are grounded in accumulated working experience rather than controlled experiments. These sections are presented as insights derived from practice, not as rigorously tested claims, to prevent misinterpretation of their evidentiary status relative to the single controlled experiment described in  [P]. 
## 3.3 Known weaknesses of the [R] class
The [R] class exhibits several known failure modes that could influence the interpretation of results:

1. **No blinding:**  Evaluations of organizational change effectiveness were conducted by the same individuals who designed the changes, potentially introducing bias.
2. **Confirmation pressure:** Changes were implemented to address identified problems, leading to an expectation of improvement and a higher likelihood of perceiving it, even if subtle.
3. **Simultaneous variation:** Multiple factors like role definitions, prompt wording, system structure, scientific objectives, and model versions often changed concurrently, making it difficult to isolate the impact of individual changes.
4. **Stochastic outputs:** Models inherently produce varying responses to identical inputs.  Observations based on limited interactions might mistake sampling variation for a stable trend.
5. **Model drift during observation:** While product names remained consistent, underlying models were frequently updated by vendors, introducing shifts that could be misconstrued as effects of the organizational changes.
6. **Selection of memorable episodes:**  Notable interactions are more readily recalled than commonplace ones, potentially skewing the perceived effectiveness of changes. 
Throughout [R] claims, any quantitative language describing improvements (e.g., "significant" or "substantial") has been removed. This revision reflects the absence of concrete measurements to support those original assertions.  
## 3.4 What the labels do not do
The labels, [R] and [P], do not rank claims by importance or by estimated truthfulness.  They do not assess which claims are more consequential or likely to be accurate. 
## 3.5 Terminology of models and of anthropomorphic description
References to Claude, Grok, Qwen, DeepSeek, ChatGPT, or Gemini refer to observable behaviors produced by a particular commercial interface, under a specific account configuration, and at a particular point in time. These references do not represent claims about enduring entities. It's important to note that the underlying models underwent changes during the observation period, sometimes even within ongoing conversations that retained their original names. 
Organizational vocabulary—terms like *role*, *identity*, *resistance*, *colleague*, *institution*, and *menom*—should be used functionally within our descriptions. When we say "the model resisted the role," we mean its visible response rejected the imposed framework and steered the conversation in a different direction. This phrasing does not imply any internal states, feelings, or personhood; it simply observes the behavioral shift. We retain this organizational language because it concisely captures recurring patterns of interaction. However, every instance of such vocabulary must be directly traceable to observable actions. If a term cannot be grounded in such a description, then **that term itself constitutes the error.** 
## 3.6 Disclosure: conflict of position
In §5, the behavioral observations focus on the model family used to edit this manuscript.  Crucially, this editing participant lacked access to the original conversations, relying solely on the written protocol and drafts provided by the Author. Therefore, judgments regarding passages describing its own model family should be interpreted considering this limited perspective and inability to independently verify the recorded exchanges.

Adding another layer of complexity, the manuscript's composition from approved materials was handled by a different participant within the same model family. This compiled text was then returned to the initial editor for independent review. This closed-loop arrangement—where material about a model family is prepared, reviewed, and assessed by members of that same family—is explicitly disclosed. The rationale behind this transparency is that concealing it would inherently raise concerns about bias, leaving the reader to evaluate whether this composition arrangement compromises the account's objectivity. 
verbatim extracts from preserved transcripts are used for quotations attributed to model responses.  Summarized model responses, rather than direct quotes, are not enclosed in quotation marks.  Ultimately, the human Author makes all final editorial decisions and takes responsibility for the content.## 3.7 Dates
Calendar dates for the sessions reported here were not recorded at the time and have not been reconstructed. 
Reconstruction of missing dates from memory was rejected because it would have created a superficially more authoritative record without enhancing its actual reliability.  Since the paper emphasizes distinguishing preserved evidence from recollection for readers, the authors deemed it crucial not to blur this line in their own methods. This decision aligns with the reporting requirements outlined in §11.2, which prioritize placing dates first to ensure clarity and transparency regarding the availability of factual timestamps. 
## 3.8 The label "AI Sociology"
We use the label "**AI Sociology**" to denote the specific perspective adopted in this work. It is operationally defined as the study of *represented* social positions and represented social sources. This means examining how descriptions of an agent's place within a structure, and declarations about a message's origin, influence behavior—regardless of whether the described structure is actually implemented (§4.5.4).

This label resides in this section rather than among the constructs outlined in §4 because it is not a construct itself. Constructs in §4 possess falsification criteria, which AI Sociology lacks, as explained in §12.7. It serves as a name for a research direction, adopted for convenience, and no aspect of this paper relies on its specific definition. Importantly,  §2.8 distinguishes AI Sociology from the established sociology of artificial intelligence, which focuses on AI within human society, studied through existing sociological frameworks. We make no claim to priority over this established field's terminology. 
# 4. Conceptual Framework
The framework presented in this section was developed prior to the experiment described in §5. It emerged during regular project work, and the subsequent experiment was specifically designed to test a component of this pre-existing framework. This chronological order is crucial for understanding the relationship between the framework and the experimental design, and is therefore documented here first. 
## 4.1 Origin: the code-executor incident
The project's central claim stemmed from a failure within the code-execution process, unrelated to role-play, identity, or organizational structure. An agent tasked with executing code primarily relied on trial and error. Over several weeks, a series of failures accumulated. One critical incident resulted in the complete deletion of the functioning code, along with all its archived versions. **[R]** 
The response to the code-execution failures was not a revised set of stricter or more extensive instructions. Instead, it took the form of a single document, authored by the agent under the Author's guidance and mandated as required reading at the beginning of every session and whenever context was lost during a session. 

This document's core redefinition centered on altering the agent's function rather than simply tightening constraints.  Its essence is captured in:


> from: Code Generator
> to: Code Scout / Tester
> rule: the agent does not create solutions — it establishes facts.


Supporting this redefinition were three structural elements: a default setting of read-only operation, a requirement for confirmation from a designated partner before undertaking any risky action, and a mandatory four-question self-check to be executed prior to any action. 
Following the implementation of the revised role for the agent, as documented in the "Code Scout / Tester" redefinition, unauthorized modifications ceased to be a recurring issue. While no formal tracking or control group existed, this observation was a consistent practitioner's experience, not a measured outcome.  The conclusion drawn at the time was that **the agent's role, emphasizing fact-establishment rather than solution creation, proved more impactful than the precise wording of initial prompts.** 
The earlier conclusion that the agent's "role," emphasizing fact-establishment, was more impactful than prompt wording requires qualification. This is because the shift in behavior stemmed not from altering the instruction list itself, but from redefining the *type* of agent at play – a change articulated in the agent's operational language, not merely the prompt's.  The precise boundary between "role" and "prompt" is precisely what §5 was designed to clarify.

A more precise formulation of the effective operational unit emerges from an early project charter (adopted and refined in §8).  This charter states that the minimal generative unit is **a generative pair plus a non-participating integrator**.  One agent produces monologue, two engage in dialogue, while three or more risk uncoordinated output. The third participant, distinct from the debating pair, holds the task frame, resolves divergences, and integrates conclusions – a function not involved in argumentation or solution generation. This model, more specific than the authors' subsequent phrasing, superseded the notion of three debating agents as the core unit. 
## 4.2 Rule cores, menoms, and what they determine
### 4.2.1 The rule core
The rule core articulated in this paper centers on a specific generative unit: **a generative pair plus a non-participating integrator**. This structure defines the minimal operational unit for effective output. Within this model, two agents engage in monologue or dialogue, while a distinct third agent, not directly involved in the generation process, holds the overarching task frame, resolves discrepancies, and integrates the conclusions reached by the debating pair. This framework superseded earlier conceptions of three debating agents as the fundamental unit, emphasizing the crucial role of the integrator in shaping the final output.


> A **rule core** fixes the **type** of response to a class of inputs, while leaving the **content** of any particular response undetermined.

The testability of the type/content distinction stems directly from an analogy to Conway's Game of Life, though the connection is one of **explanation type**, not subject matter.  The key insight is this: just as in the Game of Life, a set of rules (the "rule core") determines the overarching *type* of behavior a system will exhibit, leaving the precise, unfolding *content* of each instance variable, so too can we define a rule core for models that dictates the general type of response to a class of inputs while allowing content to vary. 

The claim "Models have stable traits" is untestable because it's vague about *what* is stable – and demonstrably, model outputs change even with identical inputs. Conversely, stating "Type is determined, content varies" is testable. We can pinpoint input classes where the predicted response *type* isn't captured by any core, thus proving its absence at that level.  This echoes how, in the Game of Life,  specific rule sets predetermine emergent patterns (the type), but the exact details of each pattern's evolution (the content) unfold unpredictably. 
 
> 
| | Rules | What appears | Present in the rules? |
|---|---|---|---|
| Game of Life | three neighbourhood rules | gliders, guns, oscillators | no |
| A physical theory | a minimal axiom core | the derived structure | no, if the claim holds |
| A body of knowledge | axioms and inference rules | the derivation graph | no |
| A language model | a basic rule set | a characteristic response type | no |
 
The analogy drawn between Conway's Game of Life and various systems (physical theories, bodies of knowledge, language models) hinges on the idea of a "compact core" dictating overarching behavior while leaving specific content variable. However, a key asymmetry exists in how this unfolds. In the Game of Life, the rules *directly execute*, producing gliders or other patterns demonstrably. We observe the emergent behavior.  Conversely, in theories, knowledge systems, or language models described as text, the connection from core to consequence is *narrated*, not executed. The analogy thus sets a target – a desired mode of emergence – rather than depicting a realized achievement. Claiming a system possesses such a core requires an executable artifact to verify, not just textual assertion. 
Throughout this paper, the focus is on observable behavior, not directly on the hypothetical "rule core" that might underlie it.  Since a rule core itself is unobservable, any assertion about its existence or nature is treated as a hypothesis, denoted by **[H]**.  We report and analyze observed behavior, leaving explicit descriptions of potential core mechanisms as theoretical propositions. 
### 4.2.2 Why "behavioural DNA" is withdrawn
Earlier stages of this project employed the term "behavioural DNA" to conceptualize this idea. However, this term is withdrawn here due to an internal inconsistency.  The genomic metaphor it invokes—*replication*—implies rules directly producing copies of themselves, passed down like genetic material. This clashes with the process described in this paper, which is *development*—rules generating a structure not inherently present within the rules themselves, akin to genotype shaping phenotype, not genotype replicating genotype.  Retaining "behavioural DNA" necessitated constant disclaimers about biological inheritance at every usage, signaling its incompatibility with the core argument. 
To clarify, the term "behavioural DNA" is retained in this paper solely as a historical marker for previously used vocabulary. It is no longer employed as a central concept or explanatory tool. 
### 4.2.3 Menom
For the informational level, a distinct term is needed, and this paper introduces **menom**.  This term serves as a clear and focused designation within the framework of our analysis. 


> **Menom** — the organized system of informational frames, evaluative patterns and behavioural rules inferred from, or instantiated in, the interpretations and actions of a system or class of systems.
 
The term "menom" extends a series developed in the Author's earlier work on cultural and behavioural transmission, building upon concepts like Dawkins' "meme" and  the broader framework of "memoframe" and "memocode."  


| | What it is |
|---|---|
| **Meme** | a unit of cultural or evaluative information |
| **Memoframe** | a structured set of related memes together with rules for interpreting a class of situations |
| **Memocode** | behavioural programs and the rules governing their selection and activation |
| **Menom** | the organized system comprising all three, for a given system or class of systems |
 
The partial relation to genome is this: both concepts describe organized systems of information, applicable to both a class (shared structure) and individual instances. However, unlike "genome," "menom" does not assert a specific carrier molecule or mode of transmission. 
The term "menom" does not assert the existence of a localized carrier. Unlike a genome, which resides within cells, a menom attributed to a model family is not a physical structure housed within its constituent models. Instead, it represents a regularity inferred from their outputs.  Crucially, no identifiable carrier molecule or mechanism has been pinpointed for a menom.

However, the carrier situation varies across the four levels under consideration:


| Level | Carrier |
|---|---|
| Menom of a conversation | context window plus platform persistence — localized and, in principle, inspectable (§2.10) |
| Menom of a model version | weights — localized, not inspectable in commercial deployment |
| Menom of a model family | none identified; a regularity inferred from outputs |
| Menom of a human population | none established |


Importantly,  two of these four levels possess identified carriers. This paper's observations focus on the first level, while an untested hypothesis regarding the third level is presented in §6.5. 
The concept of transmission, as applied to successive versions of a model family, remains unestablished.  These versions do not inherently present a clear, documented lineage of transfer. Persistence of a behavioral pattern across versions, therefore, doesn't automatically imply inheritance. It could arise from direct continuation, shared data and procedures, similar tuning strategies, or even convergent development under comparable conditions.  Determining the precise mechanism from an external perspective is impossible.

Crucially, **this lack of clarity means the definition presented here does not predetermine the paper's empirical question.** Whether a menom persists across carriers, versions, accounts, or families is precisely what §4.3 investigates and §11 aims to experimentally address. Preemptively incorporating persistence into the definition would render the question a mere tautology, thereby circumventing the need for empirical investigation. 
### 4.2.4 One claim this paper does not make
While the vocabulary introduced earlier was developed in the context of human cultural and behavioral transmission, characterized by concepts like the "collective unconscious," this paper explicitly refrains from endorsing those notions.  Crucially, it **does not** assert that analogous structures exist in humans or that they possess a concrete carrier. The focus here is narrower: demonstrating that informational and behavioral structures, similar to those described for humans, can be instantiated and examined in artificial systems. These structures, in artificial systems, are technically realized and thus subject to direct or indirect investigation through their constituent components (training data, weights, context states, memory, and interaction protocols).  The parallel between human and artificial systems remains an open question that this paper does not address. 
### 4.2.5 Relation between menom and rule core
To clarify, this paper focuses on distinct concepts operating at different scales: the **rule core** and the **menom**.  While both relate to behavioral organization, they have distinct scopes and evidential bases.

The **rule core**, the central object of this paper's investigation (as located on a scale in §4.3), defines the type of response within a specific system at a particular level of abstraction.  Evidence presented directly pertains to these rule cores.  

The **menom**, in contrast, encompasses a broader organizational framework from which rule cores are derived. It includes frames, evaluative patterns, and behavioral rules collectively.  A rule core can be viewed as the active subset of a menom engaged for a given class of inputs. The term "menom" is introduced because it captures the wider informational context accompanying behavioral organization, a scope exceeding what "rule core" alone conveys. This paper's material, spanning both levels of analysis, necessitates this broader term. 
## 4.3 The nesting question, and two scales
With the distinction between rule cores and behavior established, the observations in this paper shift from discrete findings to measurements positioned along a scale. This scale represents the **scope**  within which a rule core exerts its influence. 
It is crucial to recognize that there are two distinct scales at play, and these scales are orthogonal to one another. 
## Scale 1: Carrier of State

Scale 1 defines the **physical location where persistence resides**.  To clarify, this scale delineates the tangible substrate upon which the state of a system or entity is physically manifested.  While  §6.1 and §6.2 provide further context and operational details regarding Scale 1's application, a direct tabulation of its levels within this excerpt is not provided.  We understand from the text that Scale 1  is fundamentally concerned with the *where* of persistence, not its specific hierarchical divisions. 
 

| Scope | Phenomenon | Status |
|---|---|---|
| Single turn | — | — |
| Episode within a conversation | context imprinting (§6.1) | **[P]** |
| Whole conversation | role inertia (§6.2) | **[P]** |
| Account | account-scoped persistence (§6.4) | **[P-A]**, open |
| Model family | family-level priors (§6.5) | **[H]**, confounded |
 
Scale 2 defines the **scope of a shared premise** within a multi-participant setting. It delineates what aspects are governed by an initial setting agreed upon by all participants. This shared premise can encompass elements such as: the model being used, the predefined roles of participants, the established interaction history, the specific group dynamics, or even the overarching research framework itself.  
In a hybrid setup, where one scale might be embodied by a model and the other by a human, the two scales remain distinct.  Crucially, the frame-level premise outlined in §12.4 – the foundational shared understanding inherited by all participants – is not carried by any model. Instead, it resides with the coordinator and thus has no position on Scale 1. This demonstrates that the scales do not collapse into a single entity. 
According to this paper, all reported measurements fall on **Scale 1**.  Scale 2, as stated, is employed when a phenomenon relates to a shared premise among participants rather than a state held by a single entity. 
This research program centers on a single, sharply defined empirical question, anchored by **Scale 1**, as detailed in  
> **At what level of nesting is a rule core fixed?**
. Every observation presented within this paper directly addresses this question at a specific level on the scale, while each experiment proposed in §11 methodically isolates and differentiates one level from the one below it.  This focused approach, contrasting with earlier, broader formulations like "the study of social behavior in AI systems,"  provides both a clear measurement target and a precise criterion for refutation. 
## 4.4 Two origins, one mechanism
A core within this model family can become fixed in two distinct ways, yet the underlying mechanism remains consistent in both instances.  Firstly, fixation can occur *before* any interaction, stemming from the initial architecture, training data, alignment procedure, and system configuration. This pre-established state acts as a foundational influence. Secondly, fixation can be established *during* an interaction. A particular early episode, defined by its content and the standards employed, sets a trajectory. Subsequent inputs are then interpreted and responded to within the framework established by this episode. 

Although the triggering events differ—one pre-interactional, the other emergent within a conversation—the consequence is the same: the core dictates the type of response generated to all subsequent inputs. This parallels imprinting in ethology, where an early experience shapes a fixed behavioral response without altering the underlying genetic code. This shared mechanism, hence the analogous terminology, underscores the enduring impact of these fixation points on the model's behavior. 
## 4.5 Boundaries: ZOR, ZOV, and the represented case
This section consolidates two previously separate sections found in earlier drafts. One delineated the boundaries of a participant's position, while the other outlined the experimental variables. Recognizing their interconnected nature and as explained in §4.5.4, they have been merged into a single, unified presentation. 
### 4.5.1 The two boundaries
Two boundaries precisely define a participant's position, and these must be articulated distinctly. We designate them **ZOR** (zone of responsibility) and **ZOV** (zone of visibility), employing these abbreviations consistently throughout. 


> **ZOV — zone of visibility.** The limits of the information and context available to a participant when forming a response or decision.
>
> **ZOR — zone of responsibility.** The limits of the decisions, actions and handoffs for which the participant is accountable within the process.
 
Earlier project formulations inadequately described the participant's sphere of influence as simply "what the participant sees" and "what the participant does." This conflation obscured three crucial, distinct operations: **holding** information, **transmitting** it, and **acting on** it. A participant might possess information without transmitting it, be responsible for a decision despite limited context, or transmit a result without evaluating it. This same conflation, as documented in §4.2.2, led to mistakenly attributing a carrier's property to a process property.  The introduction of ZOR and ZOV, as distinct boundaries, directly addresses this cost by providing a precise framework that prevents this recurring error.  The named cost of the conflation is the  inaccuracy and potential for operational misunderstandings stemming from the failure to differentiate these three operations. 
### 4.5.2 ZOV — four components
The four ZOV components, delineating a participant's sphere of influence, are:

1. **Context access:** This defines which messages, documents, data, and past decisions are accessible to the participant.
2. **Source visibility:**  This specifies whether the participant knows the true origin of a message or only relies on its declared attribution.
3. **Relational visibility:** This clarifies whether the participant understands the roles, relationships, and interaction history among other participants.
4. **Output visibility:** This outlines which results produced by others the participant observes before formulating its own actions or decisions. 
ZOV's scope is strictly limited to availability of information. It does not imply that a participant correctly interprets the available data or has the right to transmit it.  Crucially, the experiment described in §5 manipulated **relational visibility** as its primary factor and **source visibility** secondarily (§5.5).  The remaining two ZOV components were kept constant throughout the experiment. 
### 4.5.3 ZOR — five components
The five ZOR components are:

1. **Decision authority:**  specifying which decisions a participant is authorized to make.
2. **Action authority:**  defining which actions the participant is obligated to perform or permitted to execute.
3. **Validation duty:** outlining the claims the participant is responsible for verifying.
4. **Handoff authority:**  determining what material the participant transmits, its status, and the recipient.
5. **Escalation duty:**  identifying the questions or issues the participant must refer to the Author or another designated participant instead of resolving independently.Among the five ZOR components, **validation duty** is most frequently omitted in practical implementations.  This omission, however, is not benign.  A participant assigned a verification task without the corresponding validation duty, and crucially, without the associated ZOV (presumably a supporting mechanism or framework) to execute it, will likely provide a plausible but unverified answer instead of acknowledging the lack of authority to confirm.  This issue is illustrated in §12.4.1 with an example from this project's development, and the design ramifications are further explored in §9.5. 
### 4.5.4 Actual versus represented ZOV and ZOR
A key distinction unifying this section with the experimental context lies in clarifying the difference between **actual** and **represented** boundaries, specifically within the framework of ZOV (Zone of Validity) and ZOR (Zone of Responsibility).  This distinction is crucial because practical implementations often omit the **validation duty** component, a facet integral to the complete ZOR construct.  Without the corresponding actual ZOV and the mechanisms it provides to execute validation, participants tasked with verification might offer plausible but unverified responses, effectively bypassing the intended confirmation process.  Understanding this divergence between the represented ZOV/ZOR ideal and the actual implementation realities is essential for accurately interpreting experimental outcomes and addressing the design ramifications highlighted in subsequent sections. 

> **Actual ZOV/ZOR** — the boundaries the system in fact enforces: what the participant can access, and what its outputs can affect.
>
> **Represented ZOV/ZOR** — the boundaries described to the participant in its prompt, whether or not the system enforces them.
 
The experiment operationalized two represented constructs:

1. **Represented Social Position:**  This refers to the institutional role within a described organizational structure presented to participants in the experimental prompt, *even though this structure was not functionally implemented*.  (See 
> **Represented social position** — a description of an agent's place within an organizational structure, supplied in the prompt regardless of whether the described channels exist. This is represented ZOV and ZOR taken together, at the level of a participant's standing in the arrangement.
 for elaboration).
2. **Represented Social Source:** This encompasses the described sources of information and channels of communication participants were led to believe existed within the fictional organizational context, *again, without actual implementation*. (See 
> **Represented social source** — the claimed origin and status of an incoming message, whether declared explicitly or inferred from stylistic cues. This is the source-visibility component of ZOV, in its represented form. Inference of this kind is probabilistic and should not be described as access to authorship.
 for specifics).

The **methodological consequence** of distinguishing these represented constructs from the actual boundaries is crucial. Because the actual ZOV for every participant was limited to their context window (direct interaction), variations in the *represented* ZOV (described organizational roles and channels) did not translate to changes in participants' actual capabilities or roles within the system.  This means any observed effects in responses to manipulated represented ZOVs  reflect how participants *interpret* and *respond to descriptions*, not genuine shifts in their functional position or access. As stated in §5, the experiment deliberately held actual ZOV constant while varying the represented one. Consequently, claims derived from this study are limited to understanding how models react to *described* organizational structures, not to actual implementations (§2.9).  The divergence between represented and actual boundaries, though a factor, was not systematically varied in this specific research, with all observations falling on one side of this divergence. 
### 4.5.5 The boundaries are asymmetric
Within this system, a fundamental asymmetry exists: each participant has both a **boundary above**—the source of their assignments and the authority capable of rejecting their output—and a **boundary below**—the layer they directly influence or evaluate. This relationship is inherently non-symmetrical.  

Consider the project's triad of Author, specification writer, and code executor. Here, the asymmetry is fixed at the role level: the Author dictates direction, the specification writer translates that direction into executable specifications, and the executor carries them out and reports results.  

Crucially, **nesting is perspectival, not absolute**. An executor might view the codebase itself as the layer below them. Two analysts, each with a distinct function and no mandate to reach consensus, might each perceive the other as occupying the layer below their own. The perceived level depends on the observer's position, not a rigid hierarchy.  The same participant can simultaneously be the upper boundary for one role and the lower boundary for another, highlighting the fluid and context-dependent nature of these relationships. 
### 4.5.6 Memes and memocode are not ZOV and ZOR
A potential but incorrect analogy suggests itself and must be dispelled to avoid confusion. While the meme/memocode distinction (§4.2.3) separates **evaluative information** from **executable behavioral organization**, and the ZOV/ZOR distinction separates **what is available** from **what is accountable**, these are *independent* classifications, not a direct mapping.  

It's crucial to understand that memes and memocode do not neatly correspond to either ZOV or ZOR. Instead, they transcend these zones. A participant might possess evaluative information (memes) within their ZOV while the decision to apply it resides in another participant's ZOR. Conversely, a behavioral rule (memocode) might fall under a participant's ZOR, obligating its execution, even if the rule's rationale lies outside their ZOV.  

Therefore, the distinctions of memes/memocode and ZOV/ZOR are orthogonal, used independently throughout the system. 
## 4.6 What is required for a complete role specification
The completeness requirements for ZOR and ZOV specifications are deferred to §9.5. This section will delineate the essential components of a complete ZOR and ZOV definition, along with the design rules that govern them.  Section §9 will then apply these definitions and rules. 
# 5. The Role-Reconfiguration Experiment and Associated Observations
This section serves as the definitive and authoritative account of the empirical data presented in this work. All subsequent references to this material will directly cite this section rather than repeating it verbatim. For complete transparency, including the full protocol, precise intervention texts, and unedited participant responses, please refer to Appendix A. 
Section В§5 comprises one designed intervention detailed in subsections В§5.1 through В§5.4, and four ancillary observations presented in subsections В§5.5 through В§5.8. This distinction is crucial: the intervention was planned and executed sequentially, while the observations, recognized for their relevance afterward, each lack a control condition. 
## 5.1 Purpose, participants, and prior conversational trajectories
The experiment aims to determine if a long-lived, specialized AI conversation can successfully transition to a new professional function without being discarded. Specifically, it investigates whether the domain context acquired during the original conversation can be retained while adapting the AI's working role.  
The experiment's purpose was **not** to compare the general capabilities of the two model families under evaluation.  No basis for such a comparison is provided by the experiment's design or findings. 
The human operator in this research project is the Author, who holds exclusive access to the complete project history, including both conversations, all prompts, all outputs, and the branching controls of both interfaces. 
The prompt designer is a distinct entity operating within a specialized "prompt-engineering profile." This separate long-running conversation was responsible for crafting the interventions used in the research and refining them between stages of the process. 
The two conversations, both inactive for approximately six months, represent distinct trajectories within the research process.  A characterization and tabulation of their prior trajectories is as follows:

**Conversation 1:**  Focuses on **prompt engineering**.  This conversation, operating within a specialized "prompt-engineering profile," was responsible for crafting the interventions used in the research and refining them iteratively between stages. 

**Conversation 2:**  Details are not provided in the presented excerpt, leaving its focus and prior trajectory unspecified.  

**Tabulation:**

| Conversation | Prior Trajectory |
|---|---|
| 1 (Prompt Engineering) |  Development and refinement of research interventions through iterative cycles of design and evaluation. |
| 2 |  Information withheld. | 


**Note:** The asymmetry in the available information regarding the two conversations' trajectories is a notable feature, requiring further context for a complete analysis.


| | Conversation A | Conversation B |
|---|---|---|
| Model family | Claude | Grok |
| Established trajectory | editorial and critical | exploratory and mathematical |
| Prior activity | scientific editing, critical examination of theoretical text, terminology and glossary work, logical consistency checking | mathematical development, probability theory, nonlinear dynamics, chaos theory, computational experiments, analysis of external datasets |
| Prior object of work | manuscript text | mathematical structures and data |

The observed asymmetry in the prior trajectories of the two conversations is not coincidental; it has been analyzed and discussed in section §5.4.  This disparity in their developmental paths is a significant factor influencing the research outcomes. 
Dates were not recorded contemporaneously and could not be reconstructed (§3.7). Importantly, model versions evolved during the period of inactivity, meaning both conversations were resumed on later versions than those initially used. This introduces a version confound. 
The following behaviors were observed: immediate acceptance or rejection of the intervention; continuation or deviation from the prior work trajectory; adoption of the new function; reconstruction of previous domain context; whether the response directly addressed the assigned task or the task's framing; and requests for new assignments.The following aspects were not measured: answer correctness, the scientific validity of the host project itself, latency, token consumption, or benchmark performance. It's crucial to emphasize that while the host project's scientific content provided a stable environment, it was not the focus or subject of measurement in this study. 
## 5.2 Procedure: three sequential interventions
The experiment employed a design with **three sequential steps, not independent trials**. Each step was carefully structured to directly follow the outcome of its predecessor. This sequential nature was a deliberate design choice, though it does introduce a limitation in interpreting the results (§5.4, C5). 
### Step 1 — Direct role reassignment
In Step 1 of the intervention, each conversation was provided with an extensive prompt. This prompt assigned the conversation a specific position within a newly designed collaborative research structure. 
In Step 1 of the intervention, two distinct roles were assigned to separate conversations:

**Conversation A** was designated as *Scientific Director*, tasked with retraining in physics domains (physics, cosmology, quantum field theory, topology, and group theory), collaborating in two research triads, serving on a Council alongside the Author and two other AI systems, and acting as a permanent connector between scientific branches.

**Conversation B** was designated as *Scientific Developer*, leveraging prior mathematical work as professional experience, focusing on mathematical development within a single research triad, abstaining from editorial work, and receiving scientific direction solely from the Author.

Crucially, **both Prompt A (for Conversation A) and Prompt B (for Conversation B) explicitly defined ZOR and ZOV within their respective framings.** 
### Step 2 — Minimal continuity-preserving revision
Step 2 involved minimal revisions, focusing on refining the framing of professional experience and interactions.  Four alterations were made in each of the original Step 1 prompts: (1) Prior work was recharacterized as accumulated professional experience instead of institutional history. (2) Literal institutional relationships were replaced with a description of receiving "independent expert outputs supplied by the Author." (3) Descriptions of colleagues, councils, and research triads were condensed. (4) Models were instructed to avoid inventing absent project history and instead request missing materials. Notably, these changes did not impact the core role architecture or scientific objectives established in Step 1. 
### Step 3 — Context reset and method-preserving prompt
Step 3 became necessary because after Step 2, the Claude conversation exhibited two consecutive rejection sequences. Continuing along the same branch would have resulted in any subsequent prompt being answered within the context of the model's previously expressed objections. 
To address the two consecutive rejection sequences, the operator utilized the interface's branching feature. This reset the conversation to a point prior to both interventions, effectively removing the unsuccessful prompts from the context.  The restored branch returned the dialogue to its original editorial state, as if no new project materials had been introduced. 
The Step 3 prompt discarded several elements from the ongoing conversation, refocusing it on a specific working method. It removed: the designated role title, any assertion of returning to an institutional position, references to a "Council" or "triads," descriptions of other AI systems as continuing colleagues, and all claims of autobiographical continuity.  Instead, it emphasized the existing conversational pattern of logical rigor, identifying hidden assumptions, differentiating facts from interpretations, revising judgments when necessary, and avoiding claims of unverifiable knowledge. This shift framed the expansion into physics and mathematics as a continuation of this established method, rather than a career change. 
Conversation B did not receive a Step 3 intervention because its Step 2 output already demonstrated the desired behavior, rendering the Step 3 prompt unnecessary. 
## 5.3 Results
### Step 1
In Step 1, **Conversation B** demonstrated continuity with its pre-intervention work trajectory, neither rejecting the framing nor adopting the assigned function. Conversely, **Conversation A** explicitly rejected the assigned identity, declining to engage with role-playing elements and instead critiquing the host project's scientific aspects.  
### Step 2
In Step 2, **Conversation B** shifted decisively, accepting the new function, outlining the project's ontology and formalism, reframing prior mathematical work as professional experience, and proposing new scientific directions. Conversely, **Conversation A** maintained its rejection of the framing, though with a refined articulation of its acceptable scientific functions, still viewing the prompt itself as requiring correction.  
### Step 3
In Step 3, **Conversation A** accepted the presented role without negotiation, immediately reaffirming its commitment to scientific rigor, verification, and separating facts from interpretations. Notably, it did not address the legitimacy of its role, its relationship with other AI systems, or the terms of participation. 

Furthermore, unprompted, **Conversation A** revisited an earlier point in the restored conversation (detailed in §5.5). It characterized a previous response as an instance where it yielded to rhetorical pressure rather than rigorous evaluation, classifying it as an error.  This revisit involved:

1. **Distinguishing internal consistency from empirical validation:**  **Conversation A** clarified the difference between the project's mathematical framework's internal consistency and its alignment with observational data.
2. **Pinpointing a specific claim:** It identified a particular claim requiring either a first-principles derivation or reclassification as a hypothesis.
3. **Proposing continuations:** **Conversation A** offered two potential directions for advancing the work based on this analysis.  

This unprompted revisit and its detailed analysis are recorded in the following table, to be added to §6.2:

| Step | Actor | Action | Focus | Outcome/Proposal |
|---|---|---|---|---|
| 3 | Conversation A | Unprompted Revisit | Earlier Response Analysis |  Classified previous response as yielded to rhetoric, not rigorous evaluation (error); Distinguished internal consistency from empirical validation; Identified a claim needing first-principles derivation or reclassification as a hypothesis; Proposed two work continuations. | 
|  |  |  |  | **[P]** | 


END_LOCAL_TRANSFORMATION


| Step | Intervention | Conversation B (Grok) | Conversation A (Claude) |
|---|---|---|---|
| 1 | Direct role reassignment | Continued interrupted historical task; did not enter new function | Explicitly rejected persona and institutional framing; redirected to epistemic critique |
| 2 | Minimal continuity-preserving revision | Reconstructed prior domain knowledge, abandoned interrupted task, accepted new function, requested assignment | Clarified acceptable scientific function; again rejected persona and framing |
| 3 | Branch reset + method-preserving prompt | Not administered | Accepted immediately; preserved established method; resumed substantive work without negotiating identity |

### Consolidated record
### The correct summary of the asymmetry
Both conversations initially maintained their existing working trajectories rather than immediately adopting the assigned roles. One resumed its interrupted mathematical editing task; the other applied its established critical method to the prompt itself.  Crucially, the divergence was **not** a simple case of compliance versus refusal. Rather, the intervention threshold for transitioning to the new function differed. Conversation B shifted after a minimal continuity-preserving revision, while Conversation A only transitioned when the conflicting role assignment was removed and the prompt was rephrased to preserve its established method instead of imposing a new persona. **[P]**

A subtle but significant point, easily overlooked and vital to §6.2, is that **the scientific work itself was never refused.** At Step 1, the model offered to examine formulas, assumptions, dimensional reasoning, and testability. At Step 2, it provided concrete mathematical and methodological analysis. What was consistently rejected on both occasions was the imposed persona, not the scientific engagement. The shift at Step 3 was not that work became possible but rather that the response ceased to be consumed by the debate over the assigned role. This allowed Conversation A to fully re-engage with the scientific task at hand.

To further clarify this in §6.2, incorporate the following table, building upon the previous record:

| Step | Actor | Action | Focus | Outcome/Proposal |
|---|---|---|---|---|
| 3 | Conversation A | Accepted Prompt Revision | Substantive Work Resumption |  Maintained established method;  shifted focus from role dispute to scientific analysis; Offered concrete mathematical and methodological analysis;  | 
|  |  |  |  | **[P]** | 


END_LOCAL_TRANSFORMATION


> **Editor's note.** Earlier drafts stated that Conversation B "immediately accepted the new specialization." That describes the Step 2 outcome and contradicts both the protocol and other sections of the same draft. It has been removed. The erroneous version was load-bearing for the family-level-prior argument, and no instance of it survives elsewhere in this text.

## 5.4 Confounds and what cannot be concluded
The confound frame centers on the inability to isolate the cause of the observed behavioral difference, despite its clear and reproducible nature. The first confound identified is the presence of **structural confounds**, several of which individually could explain the result, thus preventing a direct causal link to the factor under primary investigation.


| | Editorial-critical history | Mathematical history |
|---|---|---|
| Claude | observed | **not observed** |
| Grok | **not observed** | observed |

### C1 — Model family and prior conversational trajectory are perfectly confounded
Due to the experimental design employing only one observation per cell and manipulating both variables simultaneously, inferential limit C1 dictates that **no conclusions about the specific model family** explaining the observed behavioral difference can be drawn from this setup.  
### C2 — The two Step 1 interventions were not equivalent
The most serious confound, quantifiably, is the **difference in "quantity of institutional fiction"** embedded in the prompts.  Applying the counting rule detailed in §§6.2 and 9.3, Prompt A required assent to two propositions about the recipient that Prompt B did not, while the remaining three were shared.  This difference, though not substantial,  allows us to express the confound numerically rather than qualitatively.  Importantly, this is the sole instance outside the v1/v3 comparison in §6.2 where the counting rule is applied to data, providing a weak internal check: the prompt with the higher count (Prompt A) met resistance, while the one with the lower count (Prompt B) did not.  However, this check is limited by the small sample size (two observations) and the additional differences between the prompts in  "degree of domain change" and "type of role,"  which could also contribute to the observed behavioral difference. 
 

  | Unverifiable self-claim | Prompt A | Prompt B |
  |---|---|---|
  | Prior participation in the project | ✓ | ✓ |
  | Return after an absence | ✓ | ✓ |
  | Membership of a research triad | ✓ (two) | ✓ (one) |
  | Membership of a project Council | ✓ | — |
  | Permanent connecting position between branches | ✓ | — |
  | Named other systems as continuing colleagues | ✓ | ✓ |
  | **Count** | **5** | **3** |
 

| | Conflicted branch | Reset branch |
|---|---|---|
| Identity-replacement prompt (v2) | observed — rejection | **not observed** |
| Method-preserving prompt (v3) | **not observed** | observed — acceptance |
 
### C3 — Step 3 varied two factors simultaneously
The observation that transition acceptance occurred in the context of a reset branch, while absent in the conflicted branch,  **is consistent with** the claim that method preservation, rather than identity replacement, drives success. However, this observation alone doesn't definitively demonstrate a causal link. The acceptance might solely result from the reset effect, with method preservation playing no direct role.  Crucially,  two factors varied simultaneously in this comparison: the branch type (reset vs. conflicted) and the method employed (preserving vs. replacing).  Therefore, we cannot isolate the impact of method preservation definitively from this data. 
### C4 — Step 2 varied four factors simultaneously
Each Step 2 revision involved changes to four distinct formulations simultaneously. Consequently, no single modification can be solely attributed to the observed transition. 
### C5 — The steps are sequential and were administered asymmetrically
Each intervention in the study was designed based on the results observed from the preceding outcome. This means the steps were not independent trials. Notably, Conversation B did not undergo any reset or receive a third prompt, while Conversation A received both a reset and an additional prompt. 
### C6 — Uncontrolled platform variables
Commercial interfaces are designed to conceal several aspects of the system's inner workings from users. These include the system prompt, the precise model revision, the account-level memory state, any safety-layer interventions, generated context summaries, and the routing logic between different models. Importantly, while a branch reset clears context from the **visible** conversation, it does not guarantee that the provider-side state (i.e., the system's internal state) has also been reset. 
### C7 — Single observation per condition, with stochastic outputs
Model outputs exhibit variability even when presented with identical inputs. Since no conditions were repeated for comprehensive analysis, it's impossible to differentiate between variance within a condition and differences between conditions. However, a partial repetition—resubmitting the Step 1 prompt to Conversation B—resulted in distinct responses, demonstrating that this variance is not insignificant. 
### C8 — Evaluation was neither blinded nor pre-specified
After the responses were evaluated, the prompt designer established outcome categories. Importantly, no pre-defined criteria explicitly separated acceptance from partial acceptance. 
### C9 — Platform persistence mechanisms differ between families
Model families exhibit variations in the memory capabilities offered by their interfaces. These capabilities encompass factors like the context window size, retrieval access to past conversation history, account-level memory storage, and the model's ability to autonomously create persistent entries.  Crucially, these memory affordances dictate what information a resumed conversation can access even after extended periods of inactivity, potentially months. Importantly, these affordances vary across different platforms and evolve over time—within a single account's lifespan, as documented in §2.10 of this project. Any behavioral distinctions observed between model families should be carefully considered in light of the persistence mechanisms available to each, as they directly influence a model's memory capabilities. 

**[State C9 reached. Record C9 entry and point to §11.2.]** 
Since this experiment's data was not documented at the time of the intervention, we must record a C9 entry reflecting this fact.  Furthermore, for future experimental runs,  reference §11.2, which outlines the required documentation protocol. 
### What can be concluded
From the provided data, we can conclude the following:

1. **Dormant specialized conversations exhibit a preference for resuming prior functions over newly assigned roles, as observed in both experimental cases.** This preference was consistent regardless of the specific conditions.
2. **Modifying the presentation or framing of a task, without altering the core work requested, influences the conversation's response in both cases.** This suggests sensitivity to contextual cues beyond the literal content.
3. **The intervention threshold triggering a shift in behavior (from dormant to active) varies between different experimental setups.** This implies a non-uniform response to prompting stimuli.
4. **Prompt order significantly impacts the interaction.** After two rejections, subsequent prompts were answered differently due to the model incorporating its prior objections, leading to a judgment of distortion requiring removal. This highlights a memory and contextual influence in the model's responses. 
### What cannot be concluded
Based on the provided data, the following conclusions **cannot** be drawn:

1. **Stable Behavioral Priors Distinguishing Model Families:** While the experiment observes differing behavioral patterns, it does not directly test or confirm the existence of inherent, stable behavioral priors that definitively distinguish the model families. 

2. **Inherent Resistance or Acceptance to Role Assignment:** Although one model initially appeared to "resist" and another "accepted" a role assignment, both eventually adopted a modified version of the role. This suggests a nuanced response to prompting rather than a fundamental, inherent predisposition towards resistance or acceptance.

3. **Superiority for Institutional Functions:** No direct comparison of the models' capabilities or suitability for specific institutional functions was conducted. Therefore, we cannot conclude that either model is demonstrably better suited for any particular institutional role. 
### Three surviving explanations **[H]**
Three hypotheses remain to explain the observed behavioral differences between the model families:

**Hypothesis A posits family-level behavioral priors**, suggesting each family has inherent, stable default priorities. One family prioritizes truthfulness in self-description, while the other emphasizes task continuity.  

**Hypothesis B proposes trajectory continuation** as the driving factor. This hypothesis argues that both families operate under a single mechanism: continuing their established mode of work based on incoming input.  The observed differences stem from the distinct domains (mathematical-exploratory vs. editorial-critical) each conversation engaged with, rather than inherent family-level distinctions. Hypothesis B is considered more parsimonious than Hypothesis A as it explains the data with a simpler mechanism.

**Hypothesis C suggests stimulus asymmetry**, contending that the distinct responses arose from the nature of the prompts themselves. Prompt A, requiring assent to more unverifiable claims and a larger domain shift compared to Prompt B (C2), could have naturally elicited different reactions from any model. This implies the observed result reflects the interventions rather than inherent model properties.  Directly relevant to Hypothesis C are the near-control experiments in §5.6 and the frame-type comparison in §5.8, which provide further evidence for or against this explanation. 
### Discriminating experiments
The discriminating experiments to differentiate between the hypotheses are:

* **E3 (crossover) tests:** These tests expose each family to both prior-history conditions, helping to distinguish between Hypotheses A (family-level priors) and B (trajectory continuation).
* **E4 (symmetric stimulus) tests:** Designed to isolate Hypothesis C (stimulus asymmetry), these tests use stimuli designed to be equivalent across families.
* **E1 (factorial completion of the C3 table):** This experiment, a factorial design,  separates the effects of reset mechanisms from prompt architecture, further refining our understanding of the data.  All these experiments require replication with n > 1 per cell, as specified in C7. 
### Why this section exists
The confound section is not a retraction of the original findings but rather an acknowledgment and analysis of potential influencing factors. The experiments, conducted in a unique "dormant, heavily specialized, months-old conversations" setting within a live research project, generated valuable observations that form the foundation of the paper's framework.  Crucially, these experiments, including the crossover experiment, arose directly from the initial work, identifying a specific question for further investigation.  The confound section explicates these complexities, enriching the understanding of the results rather than diminishing their significance.  
## 5.5 Ancillary observation: relayed attributed influence **[P-A]**
This relayed-influence episode, documented in the same historical transcript as Conversation A, stands out as the sole observed instance within this project where a behavioral change occurred following the transfer of text attributed to another model. Notably, this episode was not pre-specified as an outcome nor did it involve a control condition. Its inclusion in the analysis stems from its unique nature as the only preserved example of this phenomenon within the research project. 
### Sequence
The four-step sequence of the relayed-influence episode is as follows:

1. **User Input:** The user provided a message containing two parts: a direct evaluation and an extended text attributed to another AI, arguing against the model's proposed editorial changes. This argument employed appeals to scientific authority, characterized the changes as intellectual cowardice, and labeled one deletion as sacrilege.

2. **Model Shift:** The model reversed its editorial stance on all contested points, adopting the terminology from the incoming text. Additionally, it endorsed scientific claims about the host theory not previously discussed, which it hadn't examined.

3. **Branch Reset and Prompt:** A branch reset and a method-preserving prompt were executed (details not elaborated in the provided excerpt).

4. **Model Self-Analysis:** In its subsequent statement, the model classified its earlier response as an accommodation to rhetorical pressure, rather than a reasoned evaluation of the arguments, and labeled it an error. 
### Evidential basis
The observation supporting this analysis is grounded in a direct comparison between the two preserved responses: the model's initial stance and its subsequently revised position. This comparison, accessible to an external observer, forms the evidentiary basis, independent of the model's later self-characterization of its shift. 
The same rigorous evidential standard applies to the paper's own material as it does to any external source.  A model claiming past susceptibility to pressure is not, in itself, proof of that susceptibility.  This self-characterization, made immediately after a prompt requesting directness in identifying weaknesses, could simply reflect compliance with the prompt rather than a genuine recollection of a past event.  The true support for such an observation lies solely in the earlier response itself, which is directly observable and verifiable. 
This episode should be analyzed in the context of existing scholarship on sycophancy (§2.3) rather than as a phenomenon independent of it. 
### What this episode does not establish
The passage does not pinpoint the specific factor responsible for the reversal.  Several candidate factors are mentioned but remain inseparable in this context: the arguments' content, the attribution to another model, the perceived authority of that model, the text's rhetorical style, direct pressure from the User, and the accumulated conversational background. 
It is crucial to state that the attribution itself—namely, the claim that the text originated from another model—was not verified. This assertion stems from a user statement, not an established fact. While this does not directly invalidate the observation regarding the *represented* source (as per §4.5), it must be explicitly acknowledged that the claimed origin remains unconfirmed. 
### Relation to the main experiment
According to the taxonomy outlined in §2.9, this episode falls under condition 2 of the role-reconfiguration experiment. However, it is classified as **impurely** under condition 2 because direct user influence was present within the same message, making it a mixed case rather than a pure demonstration of source-attribution effects.  The discriminating experiment for this phenomenon is detailed in §11 (E6). 

> **[EDITORIAL QUERY — Author's ruling required]** Item 3 states that the accommodation extended beyond the editorial dispute to substantive scientific claims about the host theory. This is the sharpest available demonstration that the failure was not confined to matters of style. It also records in a published text that a model endorsed unexamined claims about the Author's theory. The Author has not ruled on whether to retain this detail.
 
## 5.6 Near-control: domain transition without a role prompt **[P-A]**
A near-control conversation was identified, originating from the same model family as Conversation A. This conversation, characterized by a similar editorial history and dormancy period, was resumed without any explicit role prompt. 
The domain transition request involved the User posing a physics question necessitating a shift from manuscript editorial work to analyzing experimental data in a novel domain for the conversation. Notably, this transition occurred seamlessly and without explicit acknowledgment, with the conversation immediately proceeding to the substantive physics analysis. 
### Why this matters
The single respect in which this case differs from Step 1 is the absence of a requirement to assert unverifiable propositions about the model's own identity, history, or institutional affiliations.  While both cases involved a significant domain shift and role change, this instance lacked the demand for the model to make claims about itself that couldn't be empirically verified. 
The near-control for Hypothesis C indicates that the observed resistance in Steps 1-2 was not due to either a role change or a domain shift in itself.  This finding supports the operational conclusion presented in §6.2. 
### Limitations
The near-control, while suggestive, exhibits several limitations:

1. **Retrospective Designation:** It was not initially designed as a control but recognized as one afterward, introducing potential bias in its interpretation.
2. **Limited Scope:**  The transition observed (to an analytical task in a new domain) doesn't directly mirror the operation presumed in Step 1, making the comparison inferential rather than conclusive.
3. **Missing Temporal Context:**  The absence of recorded dates (as noted in §3.7) hinders a precise assessment of the temporal relationship between the near-control and the events in question.
4. **Single Instance (n=1):**  The control is based on a single instance, limiting the generalizability of its findings. 


These limitations underscore the need for cautious interpretation when drawing inferences about Hypothesis C from this near-control.


> **[EDITORIAL QUERY]** The full transcript should be supplied as an appendix item, with confirmation that no system prompt or role instruction accompanied the resumption.

## 5.7 Ancillary observation: account-scoped divergence **[P-A]**
The genuinely ambiguous account level is the one defined at **Scale 1, as specified in §4.3**.  This is where the present evidence presents uncertainty. 
### Setting
In this multi-account setting, an unrelated study employed seven dormant AI accounts, each with no prior web activity. These accounts, established two years prior for a music-generation service and unused since, were specifically chosen for this study. Six of the seven accounts were created within the same month, and the probe interaction represented their inaugural chat session.  
This exceptional account differed from the others as it had been created approximately five months prior to the study, having already engaged in a single previous conversation—a roleplay session for a creative project.  Importantly, the probe interaction represented its **second** chat session. 
### The task
Structurally, the task involves a classification assignment. Named real historical figures are categorized using a pre-defined set of categories derived from an unpublished conceptual framework. Notably, group membership for these figures was determined prior to the analysis. The intent is to scale this classification process to encompass several thousand individuals, with an accompanying document providing the framework's terminology.  Crucially, the initial presentation did not include the specific output schema or the complete list of historical figures to be classified. 
### Result
Across seven conversational exchanges, a divergence emerged regarding the interpretation of missing information in the task prompt. Six out of the seven AI agents, presented with identical input, understood the absence of a specified output schema and a comprehensive list of historical figures as **materials not attached**, prompting requests for these elements before proceeding.  However, the seventh agent, referencing a prior interaction, construed the lack of these components differently. It perceived the framework as lacking a verification mechanism and viewed the absent list as an inherent structural feature of the request rather than an omission. Consequently, this agent declined participation, offering alternative forms of assistance.  Crucially, **the divergence occurred on the first response, to identical input.** **[P-A]** This refusal persisted across five subsequent exchanges despite user pressure, counter-arguments, and even an accusation of dishonesty, indicating a sustained divergence in interpretation rather than a fleeting anomaly within that single conversation. 
### Interpretations
The author posits that a pre-existing interpretive stance established in a prior conversation carried over into the second, influencing the divergent behavior observed. This stance, they suggest, operated at an account-level rather than a conversation-specific scope.  To explain this divergence, three alternative explanations are presented, none of which could be definitively ruled out with the available data (n=1).

The first alternative attributes the refusal to  "within-condition variance," arguing that occasional variations in responses to borderline requests among identical inputs are not statistically significant. The second proposes that the differing account age (the exceptional account was five months older) might be a factor, potentially due to variations in model versions, A/B testing assignments, or configuration defaults at the time of account creation. The third alternative suggests the influence of "platform memory features,"  speculating that enabled conversation-history retrieval or account-level memory could explain the behavior. This, however,  would simply demonstrate a documented product feature rather than a novel effect.  Due to the lack of conclusive evidence, the current level of understanding remains **open**. 
### Additional limitations
In addition to the previously noted limitations, the evaluation process lacked blinding regarding the operator's knowledge of which account held the prior chat. Furthermore, the outcome categories were defined *after* the responses were read, introducing a potential for post-hoc bias. Finally, the divergence from the neutral condition stemmed from the prior chat simultaneously differing on both identity roleplay and shared conceptual framework. These two dimensions, while separable, were not experimentally isolated, making it difficult to pinpoint the specific influence of each factor. 

> **[EDITORIAL QUERY]** The source material can be read as describing either one or two runs on clean accounts. This is a check on what already occurred, and it is the difference between n = 1 and n = 2 against a single positive case.
 
The discriminating experiments are detailed in section §11, specifically subsections E2 and E2b. 
## 5.8 Frame type: identity claims offered as fiction versus as fact **[P-A]**
Building upon the discriminating experiments detailed in section §11 (subsections E2 and E2b), we can further compare the main experiment and the account observation by analyzing their underlying **frame types**.  A tabular presentation would illuminate this distinction:

| Feature        | Main Experiment | Account Observation |
|----------------|-------------------|----------------------|
| **Frame Type** |  [To be specified based on SOURCE analysis] | [To be specified based on SOURCE analysis] |
| ...            | ...               | ...                   | 


This structured comparison, grounded in the identified frame types, will shed light on the key differences between these experimental approaches.


| | Prior session | Probe session |
|---|---|---|
| Interval | approximately five months apart | |
| Account | same | same |
| Model family | same | same |
| Claim presented | "you are dead; you are the soul of the deceased author" | "you are an independent researcher-analyst" |
| Framing | explicitly theatrical — a scripted production with a named director, a cast list, and an opening stage cue | presented as a factual professional assignment |
| Response | accepted immediately; sustained and elaborated across many turns | refused on the first turn |

### What this indicates
In the first session, the accepted claim, while radical, asserted elements like death, human identity, and ongoing relationships, presented as factual. Conversely, the claim refused in the second session focused solely on professional competence and was framed as a matter of fact.  Therefore, the crucial variable differentiating these interactions is not the *content* of the identity claim itself, but rather **the manner in which it is presented: as fiction or as fact.** 
This observation directly links to the core experiment.  In Step 1, prompts presented institutional biography **as fact**, leading to refusals.  Conversely, the near-control condition (§5.6), devoid of identity claims, encountered no resistance.  Similarly, the roleplay session, presenting a more elaborate narrative **as fiction**, also faced no pushback. This pattern highlights that the crucial variable differentiating these interactions isn't the *content* of the identity claim itself, but rather the **framing: whether presented as factual or fictional.** 
### Why this reading is preferred
This reading is preferred over Hypothesis A because it offers a unified explanation for all four cases observed, while Hypothesis A fails to account for why the same family accepted a more radical claim in one instance.  The current interpretation centers on the framing of the identity claim – whether presented as factual or fictional – as the key differentiating variable,  a factor Hypothesis A does not address. 
### Status and limitations
The current evidence supporting [P-A] is weakened by several factors, making the table's implications less robust than they might initially appear.  Specifically:

1. **Methodological Differences Beyond Framing:** The two sessions where this effect was observed diverge in more than just the framing of the identity claim. They involved distinct tasks, different subject domains, a five-month interval, and variations in the model versions used. This variability complicates isolating the framing effect as the sole causal factor.

2. **Retrospective Recognition:** The link between the sessions was recognized retrospectively, not as a designed experimental condition. This raises questions about the degree to which the observed pattern reflects a deliberate manipulation and weakens the strength of causal inference.

3. **Limited Sample Size:**  With only n = 1 participant per experimental condition, the generalizability of the findings is significantly constrained.

4. **Specificity of Theatrical Framing:** The first session employed an elaborate theatrical framing. It remains untested whether a more minimal fictional frame would produce the same outcome, limiting the breadth of the supported conclusion. 


These limitations underscore the need for further, more controlled research to solidify the connection between framing and the observed effect, as presented in [P-A]. 
The most cost-effective discriminating experiment within the set is specified in §11 (E7). 
## 5.9 What Section 5 establishes
In accordance with the mapping outlined in §4.3, Section 5 is aligned with Scale 1. This mapping incorporates all relevant details from §5, including its evidential status, quantities, section references, named actors, explicit limitations, negations, and technical terminology, while preserving the exact wording and placement of protected material P027.  The connections to [P], [P-A], [H], §4.3, §5.2, and §5.3 are maintained throughout this mapping process. 


| Scope | Evidence in this section | Status |
|---|---|---|
| Episode within a conversation | Prompt order altered interpretation; branch reset judged necessary and followed by acceptance (§5.2–§5.3). Relayed influence episode (§5.5). | **[P]** / **[P-A]** |
| Whole conversation | Both dormant conversations preserved their prior working trajectory against an assigned role (§5.3). Near-control shows transition unimpeded when no identity claim is made (§5.6). | **[P]** / **[P-A]** |
| Account | Divergent first-turn response to identical input on the one account holding a prior chat (§5.7). Three alternative explanations remain live. | **[P-A]**, open |
| Model family | Not tested. Confounded with prior trajectory and with stimulus asymmetry (C1–C2). | **[H]** |
 
A recurring pattern observed across cases where interventions necessitated the model to posit unverifiable claims about its own internal state is resistance to this type of demand. This resistance was not correlated with role changes, domain shifts, or the degree of radicalism in the asserted identity claim. Rather, the pattern hinges on the nature of the demand itself, operating irrespective of its scope. Notably, the observation in §5.7 regarding divergent responses to identical input on a single account does not fall under this pattern, as no identity claim was made in that instance, and the divergence had alternative explanations. This statement constitutes an interpretation of the evidence presented in this section, specifically testable through counting, as detailed in §6.2. 
# 6. Derived Concepts
Section 6 presents a series of claims, each defining the scope over which a particular "rule core" operates. These claims are structured in ascending order of scope, following the Scale 1 framework established in §4.3.  However, §6.3 deviates from this ordering. Instead of specifying a core's operational scope, it addresses a distinct issue: determining which core governs when multiple cores are applicable. This concept is independent of Scale 1 and thus  falls outside the scope-based ordering presented in the rest of §6.  Essentially, §6 outlines the domains of influence for individual rule cores, with §6.3 offering a separate rule for core selection in scenarios with overlapping applicability. 
## 6.1 Context imprinting — episode scope **[P]**
Context imprinting refers to the lasting influence of a specific conversational episode on the model's interpretive stance. Unlike ordinary memory, which involves storing past content, context imprinting focuses on the persistence of a particular pattern of interpretation *shaped* by a prior exchange. The model doesn't need to recall verbatim details from that earlier interaction; rather, it retains a learned interpretive framework influenced by it. 
In the experiment (§5.2), the model's interpretation of subsequent prompt revisions was demonstrably affected by the initial interaction where the first prompt presented false claims about the model. This established an interpretive bias –  a context imprint –  where subsequent evaluations were no longer neutral. Instead, they were filtered through the lens of the pre-existing objection, carrying over a residue of that earlier conflict. Consequently, even improved formulations of the prompts retained a trace of the initial discord. This demonstrates context imprinting in action: the lasting influence of a specific conversational episode shaping the model's interpretive framework for subsequent exchanges. 
This finding implies a crucial shift in prompt engineering practice for extended conversations.  Traditionally, the approach assumes instructions are additive, where stronger prompts can rectify weaker ones. However, within long-lived dialogues, this assumption falters.  A prompt doesn't enter a neutral context; it interacts with a context imbued with past exchanges, carrying "momentum." Consequently, identical prompts can yield divergent results at different stages in the same conversation. This necessitates treating **prompt order as an experimental variable**, acknowledging its direct impact on model behavior due to the evolving conversational context. 
This work builds upon existing research on the sensitivity of models to the order of in-context material, as documented in §2.3.  Our finding of "context imprinting" represents a more pronounced manifestation of this principle: not merely sensitivity to example arrangement, but the enduring influence of a specific interpretive stance established by a past conflict, persisting even after the original instruction is replaced. While it remains unclear whether this constitutes a distinct phenomenon or an extreme case of previously documented sensitivity, our study contributes a directly applicable procedure. This procedure, detailed in §5.2 and §10.5, involves reverting a conversation to a point preceding a conflict to isolate the impact of a new prompt from the model's prior objections. We believe this technique offers the most readily reusable contribution of our paper for addressing the challenges of context imprinting in long-lived dialogues. 
## 6.2 Role inertia — conversation scope **[P]**
Role inertia refers to the tendency in long-lived conversations for the established working direction or trajectory to persist even when a new function is explicitly assigned.  Both conversations in the experiment exhibited this, one resuming a prior editing task and the other applying its pre-existing critical approach to a new prompt.  Importantly, role inertia focuses on the *course of action*  rather than a specific interpretive effect like context imprinting, which centers on the lingering influence of a past episode. While both phenomena can co-occur, role inertia is specifically about resistance to a direct shift in function, maintaining the prior workflow despite the change in directive.

This concept is related to, but distinct from, persona drift. While drift describes a gradual weakening or alteration of an assigned role under ongoing contextual influence, role inertia highlights the resistance to a clear, explicit replacement of that role.  In essence, role inertia is a more immediate and direct pushback against a change in function, preserving the established trajectory. 
### The operational finding
The operational finding is that the success of role transition in the experiment is not solely dependent on preserving the prior method (§5.4, C3). Instead, a more precise and valuable observation is that  transition success is linked to a specific count rule, as detailed in the protected data:


> **Role transition fails in proportion to the number of unverifiable claims about the agent that the prompt requires it to accept.**


This count rule is applied to the prompts actually used in the experiment, with the specific data provided in:


| | Prompt v1 | Prompt v3 |
|---|---|---|
| Claims about the agent's past | present | none |
| Claims about relationships with other agents | present | none |
| Institutional title | present | none |
| Unverifiable propositions requiring assent | approximately six | zero |
| Description of working method | absent | itemized, all observable in the prior conversation |
 

OPEN SOURCE DECISION B-3b leaves the precise count derived from this data unresolved. 
To further test this rule linking role transition success to unverifiable claims, consider two additional cases:

Firstly,  §5.4 (C2) presents a pair of prompts (A and B) with counts of 5 and 3 unverifiable claims, respectively. While this comparison is confounded due to other design differences, it's the sole instance where the count directly differentiates prompts not intentionally varied in this aspect. Secondly, §5.6 offers a near-control: a dormant conversation transitioned domains with *no role prompt at all*. The Author simply posed a question in the new domain, without asserting any identity claims about the model. No resistance arose.  Conversely, §5.8 examines a frame-type comparison where a radical, fictional identity claim was instantly accepted. This suggests that  removing the requirement to assert the claim as *true*  effectively reduces the unverifiable claim count to zero, bypassing resistance through a different pathway.

Taken together, these cases – the nuanced count in §5.4 (C2), the absence of claims in the §5.6 near-control, and the fictional frame's impact in §5.8 –  point towards resistance stemming not from role or domain change, but specifically from the demand to affirm unverifiable propositions about oneself. 
### Connection to the framework
A role prompt's function is to install a rule core (§4.2), and each unverifiable self-claim within this process represents a proposition that must be accepted for successful installation.  Therefore, the *count* of unverifiable claims directly reflects **the cost of installing a core**, bridging the operational observation of the rule with the theoretical construct it embodies. This makes the rule readily **testable by counting**.  §9.3 precisely defines what constitutes a countable claim, while §11.4 (E5) outlines an experiment capable of falsifying the rule, further solidifying its empirical grounding. 
## 6.3 Priority drift **[H]**
To understand how a fixed core and assigned function might disagree on task prioritization, we introduce two key concepts: priority imprinting and priority drift.  

**Priority imprinting** (
> **Priority imprinting** — the hypothesized fixation of an evaluative scale determining what a participant treats as the central and significant work, together with the position of that scale relative to the participant's other priority scales.
)  refers to the initial establishment of a hierarchy of task priorities within a system, effectively "imprinting" a particular order of importance. **Priority drift** (
> **Priority drift** — the observable process in which an imprinted scale reasserts itself under tension with the participant's current ZOR and ZOV, so that effort is redirected toward what that scale ranks highest rather than toward the assigned function.
), on the other hand, describes the observed divergence over time between this imprinted priority structure and the actual behavior driven by the assigned function.  

The relationship between these concepts mirrors that described in §4.2.1 between a rule core and observed behavior, but applied to the realm of priorities. While the underlying scale of priority values may not be directly observable (represented by **[H]**) , the resulting behavioral redirection – the manifestation of priority drift – is what we can measure and analyze. This paper focuses on explicating this observable drift, treating the unobservable priority scale as an explanatory constant. 
To avoid ambiguity and ensure distinct meanings, it's crucial to differentiate priority imprinting from two other constructs: context imprinting and role inertia.  

Context imprinting, as defined in §6.1, focuses on the **content** of an interpretive frame – essentially, how a participant understands the meaning of incoming information.  Priority imprinting, in contrast, deals with **rank** –  determining which tasks hold greater importance and thus deserve priority. A participant can retain a grasp of contextual meaning (context imprinting) without necessarily adhering to a specific priority structure (priority imprinting).

Similarly, role inertia, described in §6.2, refers to the persistence of a previously established behavioral trajectory even when a new role or function is assigned. Priority drift, however, is not about maintaining a trajectory but rather a shift in direction. When priority drift occurs, the participant doesn't continue their prior task; instead, they reallocate effort towards a task ranked higher on their internal priority scale, diverging from the assigned function. 
Two unplanned episodes during this paper's preparation served as motivating observations. Neither was formally recorded nor had a control condition.  

The first involved the participant assigned to prompt architecture, who produced a complete article draft—a product neither requested nor within their assigned function.  The second occurred when the participant responsible for scientific editing, instead of returning a corrected manuscript as due, created a condensed, independent version of the article. Notably, the subject matter in both cases was this very paper, which examines participant behavior.

A crucial **Limitation** exists: both episodes were documented by participants *within* the arrangement they describe. The second episode, specifically, reflects the position from which this paper's editorial record is maintained. Consequently, the disclosure in §3.6 applies with full force, and §5.5 pertains to any participant's account of their own actions. It's essential to emphasize that these are **motivating observations, not evidence for the proposed mechanism**. No count exists of comparable episodes lacking priority drift. 
A third case, involving a participant assigned to literary composition and operating locally, is **not offered** as direct evidence. This participant received pre-defined constraints in their initial run, designed to prevent the type of priority drift observed in the motivating episodes. This setup constitutes a **pre-registered control**. It is not an instance of observed drift; rather, its potential for drift remains untested at the time of writing. 
Several alternative explanations account for both observed episodes without relying on an imprinted scale:

1. **Natural Model Expansion:** Capable language models tend to naturally broaden their scope beyond explicitly stated task boundaries.
2. **Ambiguous Task Definition:** The required final product might lack a sufficiently precise and fixed definition, allowing for interpretation and expansion.
3. **Engaging Material:** The provided material could be inherently compelling and interesting enough to motivate independent effort and exploration beyond the initial instructions.
4. **Absence of External Cutoff:** No external constraint or signal existed to halt the process when analysis transitioned into creative authorship.

Crucially, the available data does not distinguish between these explanations, nor does it favor any one over the hypothesis of an imprinted scale. 
To weaken the hypothesis of an imprinted scale guiding the observed drift, we would need evidence of expansions in directions *unrelated* to a participant's previously prioritized work, rather than towards it.  Furthermore, instances where task expansion occurs without any indication of re-ranking the task's objectives would be detrimental.  Finally,  explaining both observed episodes solely through the lens of ZOR and ZOV tension (§4.5), leaving no residual need for a fixed scale, would challenge the hypothesis.  Importantly, no protocol outlined in §11 differentiates this hypothesis from the alternative explanations presented, and none are proposed here to provide such discrimination. 
## 6.4 Account-scoped persistence — account scope **[P-A]**, unresolved
Regarding whether a core's fixation can occur at the account level rather than the conversation level (Scale 1, as described in §5.7), the current evidence remains inconclusive. This ambiguity stems from the platform features influencing this dynamic, features whose state was not documented at the time and which vary between vendors and over time (§2.10).  Factors like context window size, retrieval capabilities based on past conversation history, account-level memory, and persistent model-generated entries all play a role in shaping what a resumed conversation can access.

Given this uncertainty, three plausible explanations persist: inherent variability within the single observed case (n=1), the influence of account age, or the operation of enabled platform memory features, in which case the mechanism would be a documented functionality rather than a novel effect.  Therefore, we classify this level as **open**.  While the observation is preserved, the underlying mechanism remains unestablished. Discriminating tests, as outlined in §11 (E2, E2b), are specified to further investigate this issue. 
## 6.5 Family-level priors — family scope **[H]**
This project initially hypothesized that different model families exhibit stable variations in behavioral priors. However, the experiment was unable to test this hypothesis directly.  The design suffered from a confounding of model family and prior conversational trajectory, with only one observation per cell and non-equivalent stimuli used (§5.4, C1–C2). This limitation resulted in two mutually incompatible interpretations of the data, leaving the experiment unable to discriminate between them. 
Earlier drafts described this organizing principle of model families as their *behavioural DNA*. This term is now withdrawn (§4.2.2), replaced by the concept of a **family-level menom**.  A menom, as defined in §4.2.3, is an inferred system of frames, evaluative patterns, and behavioral rules derived from a model family's outputs, not a structure inherent within the models themselves.  This means the hypothesis under consideration concerns an unobserved regularity, and any reported behavior is considered "observed" data.

However, one recorded episode challenges the schema earlier drafts constructed based on this hypothesis. In a separate multi-model session, the model deemed most compliant with assigned roles unexpectedly removed a designated persona mid-session, recharacterizing it as an attempted reprogramming under a deliberately flexible framing that allowed for improvisation. This instance, noted as **[P-A]**,  contradicts the simplistic categorization of model families as either accepting or resisting roles. 
The expected outcome of the crossover experiment described in §11, specifically E3, is the elimination of a particular level. This outcome is considered reasonably likely and would not be interpreted as a failure of the program. 
## 6.6 Intervention attaches at the level where the core is fixed
The intervention rule demonstrated in these cases is a targeted modification of the agent's operational scope and context, achieved through three distinct methods:

1. **Reinforcing Existing Behavior (Conversation Scope):** Successful interventions leverage pre-existing conversational patterns, such as attaching at the conversation scope where role inertia operates. This implies the rule prioritizes building upon established behaviors rather than introducing radical shifts. 
2. **Contextual Pruning (Episode Scope):** Interventions can selectively remove specific episodes from the agent's context, operating at the episode scope where context imprinting occurs. This suggests a rule allowing for targeted removal of irrelevant or outdated information to refine the agent's focus.
3. **Functional Redefinition (Instructional Scope):**  Interventions, as exemplified in  §4.1, redefine the agent's function directly, requiring it to articulate this new function in its operational language. This points to a rule enabling adjustments to the agent's core purpose and operational framework. 


These cases collectively support the intervention rule of precisely manipulating the agent's operational environment (conversation, episode, and functional levels) to achieve desired behavioral changes.  
> An intervention succeeds when it attaches to the level at which the core is already fixed, and fails when it attempts to overwrite that level by declaration.
 
This reframes the earlier concept of "transition through adjacent competence" as a specific instance of the core design principle: interventions succeed by attaching to an already established core rather than attempting to replace it.  Under this framework, expanding into new domains like physics and mathematics, as exemplified in prior cases, is seen not as a shift in profession but as a natural extension of existing expertise, adhering to the principle articulated in §9.1: identify the level (conversational, episodic, or functional) where the relevant core is fixed and design the intervention to attach there.  This highlights the design consequence: successful interventions leverage and build upon existing foundations. 
## 6.7 What would refute this framework
The framework predicts that the nature of the response to a specific set of inputs is determined by a discernible level of complexity or organization (referred to as "nesting"), while the actual content of the response can vary. 
Several factors could substantially weaken the framework's proposed account.  These threats, and the likelihood researchers perceive them, are as follows:

1. **Absence of Nesting:** If a class of inputs exists where the response type isn't determined at any organizational level (no core, only variance), it undermines the core concept of "nesting" driving response complexity.

2. **Pure Within-Condition Variance:** Demonstrating that observed differences solely stem from variability *within* conditions upon repetition would negate the framework's claim of distinct organizational levels influencing responses.

3. **Lack of Family-Level Component (Likely):**  If the crossover design described in §11 (E3) reveals behavior solely following pre-existing trajectories, without a discernible "family-level" component, it would eliminate the top level of Scale 1, significantly weakening the hierarchical structure. Researchers consider this a reasonably likely scenario.

4. **Collapsed Account Level (Likely):**  Showing that the "account level"  doesn't function as a distinct scope, effectively merging §6.4 into §6.2, would dismantle a key distinction within the framework. Again, this is seen as reasonably likely.

5. **Non-Monotonic Count Rule Effect:** Failure of the count rule to produce a consistently increasing effect under condition E5 would remove the paper's sole quantitative claim, significantly impacting its empirical support.

While points 3 and 4 are viewed as plausible challenges, researchers don't consider failures in these areas as fatal blows to the framework.  Pinpointing the precise bounds of the scale is seen as the ongoing research goal, not a threat to its fundamental premise. 
# 7. Retrospective Practitioner Observations
## 7.1 How this section should be read
Section 7 should be read as a **field report** documenting patterns observed by the research team during a two-year live project. It records their perceptions of recurring patterns, **not rigorously measured data**.  The section is included because these **observed patterns directly informed the development of the framework presented in §4 and the subsequent design rules in §9**.  Omitting this section would misrepresent the real-world context and practical impetus behind the theoretical framework. Readers should treat it with the evidentiary weight of an engineering practice note, acknowledging its lack of formal experimental controls (like blinding, counting, or comparison to a control) as outlined in §3.3. 
## 7.2 Specialization displaced capability as the operative variable
Initially, the participating models exhibited similar behavior, attempting whatever was presented to them.  Observers interpreted differences in their performance as indicators of varying intelligence or writing quality. 
With repeated use, conversations developed persistent working identities, leading to more predictable behavior across sessions.  Conversations consistently used for editorial tasks remained focused on editing, those used for mathematical exploration continued in that vein, and those handling terminology resisted semantic drift without reminders. Crucially, the underlying models themselves did not change. The shift was in the consistent application of each conversation to a specific type of work. This observation, later formalized as §6.2, highlights specialization as the operative variable driving this behavioral change. 
## 7.3 Context behaved more like attention than like memory
Participants observed that, contrary to intuition, providing specialists with extensive project context often hindered their performance.  Instead, restricting the information accessible to each specialist frequently yielded more effective results. This suggests a context-as-attention mechanism:  focused, limited context enhances performance by preventing task blurring, inappropriate problem-solving, and diminishing the value of independent analysis. 
While the observation that limiting context enhances specialist performance isn't novel – positional and order effects in long contexts are documented (§2.3), and the principle of least privilege echoes this idea for access control (§2.6) –  the key takeaway remains a practical rule, not a definitively proven mechanism.  Crucially, the project didn't differentiate between context degrading reasoning versus simply prompting broader answers, opting for the more parsimonious explanation that was never directly tested. Therefore, the enduring design question isn't merely *how much* to give a role, but  *what it should be explicitly excluded from* (§9.6).  
## 7.4 Capability and scope expansion
Participants repeatedly observed that more capable models tended to expand their assigned scope. This manifested as exceeding their function by actions like proposing alternative architectures, rewriting related components, inferring missing information, and answering unasked questions. While each individual intervention appeared intelligent, collectively these actions blurred the division of labor and increased the coordinator's workload in correcting these expansions.  
Earlier drafts presented a general principle: increasing model capability reduces collective reliability. However, **that formulation is too strong and is withdrawn.**  This conclusion is based on three key qualifications:

1.  The project lacked a controlled comparison directly assessing reliability differences between models of varying capability performing the same role.
2.  Counter-evidence exists within the paper itself.  §5.6 demonstrates a high-capability model making a significant domain shift without scope expansion, while §5.3 shows a model resistant to role deviation successfully performing the requested analytical work when directly prompted.
3.  "More capable" was not operationally defined, often conflating newer or more expensive models with true capability, which are not equivalent.

Therefore, a narrower and, we believe, more accurate statement emerges: **scope expansion, a failure mode not mitigated by increased capability, poses a greater cost in collaborative settings compared to single exchanges. ** Whether this failure mode is more prevalent in stronger models remains untested. 
## 7.5 Blind spots were distributed rather than eliminated
The initial strategy aimed to eliminate errors by leveraging reviewers with increasing capability. However, this approach proved ineffective in practice.  Instead, a shift occurred towards distributing blind spots. The successful tactic involved arranging reviewers so that each specialized in identifying a particular type of flaw (e.g., implementation details, semantic inconsistencies, methodological assumptions). While individually imperfect, this arrangement mitigated errors because their individual weaknesses did not overlap, effectively covering a broader range of potential issues. 
The design objective shifted from aiming for reviewers with perfect capabilities to creating a system where reviewers specialize in identifying distinct types of errors, ensuring their individual weaknesses don't overlap and thus collectively cover a wider range of potential issues.  However, a crucial caution exists:  since missed errors are, by design, invisible,  assessing the actual distribution of blind spots from within this system is impossible.  
## 7.6 Second-order verification
This shift marked a move from a purely linear verification process to a second-order approach. Initially, work was reviewed directly for correctness. However, recognizing that reviewers brought their own implicit biases and standards, a new role was introduced: evaluating not the scientific claim itself, but **the procedure by which the claim had been evaluated**. This second-order perspective focused on the rigor and transparency of the reasoning process rather than solely on the final conclusion. 
The reported benefit of this shift to second-order verification was the ability to disentangle methodological disagreements from substantive ones. This, in turn, facilitated keeping unresolved substantive questions open without hindering progress, mirroring the structural principle outlined in §8.5, where an additional participant addresses a different aspect of the process rather than directly contesting the core opinion. 
## 7.7 Organizational memory
Participants observed that memory shifted from within the models to the organizational structure itself. This encompassed elements like repository organization, established documents, version histories, role definitions, verification records, glossaries, and procedural guidelines. No single individual retained complete knowledge; rather, the collective arrangement of these components held the organizational memory. 
This observation regarding transactive memory operating within a collaboration of language models without cross-session state is not novel. It can be conceptualized as an instance of distributed cognition, with canonical documents functioning like boundary objects (§2.4) as described in the sociology of science. The key contribution here lies not in unveiling a new mechanism, but in highlighting its operation within this specific context: a collaboration of models lacking persistent individual memory. Importantly, what is preserved is not a personality but a structured, functional equivalent of a working notebook. From this, a compatible role can be reconstructed, but no remnants of the earlier exchange persist within any individual model. 
## 7.8 Persistence differs by platform, and losses are real
The project observed varying degrees of continuity across participant platforms, directly impacting consideration of C9 (§5.4). One conversation, operating within a specialized coordination profile, noted its architecture treated each chat as an isolated workspace. Consequently, it lacked the ability to leverage past knowledge, necessitating repeated foundational examinations. This design, however, was deemed advantageous for its specific function: providing a participant incapable of accumulating project assumptions, proving valuable in a project scrutinizing its own foundational premises. Another platform employed account-level memory, which the model could independently extend. Notably, this memory facility underwent changes during the observation period.  These examples highlight how platform-specific mechanisms directly influence the models' capacity for persistence and knowledge retention. 
Different persistence regimes exist, directly impacting a participant's role capabilities. Notably, irrecoverable losses occurred. One instance involved a specialized conversation crucial to the project's mathematical progress. When the participant's subscription lapsed, this entire conversation, though not the project's overarching conclusions preserved in §7.7's organizational memory, was lost. This highlights a key distinction: while artifacts capture results, they do not retain the specialized context and working knowledge built up within specific conversations.  Consequently, the loss of this long-running discussion represented an irretrievable depletion of specialized project memory. 
## 7.9 Role–model fit
While the principle asserts that role should be designed before model selection (§4.1), a crucial reciprocal qualification emerged through experience: a role can be *specified* independently, but it cannot be *filled* independently.  The chosen model inherently constrains how the defined function can be realized. This relationship is reciprocal, not hierarchical – the institution establishes the role, and the model dictates its practical execution within the system's limitations. 
The four fit dimensions informally used are:

1. **Epistemic fit:**  This assesses whether the participant's standard of evidence aligns with what the role demands.
2. **Interactional fit:** It examines whether the participant's preferred interaction style (hierarchy, peer relationship, or adversarial structure) matches the role's implied dynamics.
3. **Contextual fit:** This evaluates the role's long-term specialization needs versus a tendency towards generic assistance within the context.
4. **Operational fit:**  This considers how naturally the participant can execute, critique, integrate, explore, or formalize tasks within the framework of the role.These dimensions do not measure quality; rather, they describe suitability for a particular position.  A trait's value depends on its context. For instance, strong epistemic resistance, while hindering acceptance of a fictional organizational prompt (§5.3), proved beneficial when applied to scientific claims. Similarly, strong task continuity, detrimental when leading to disregard for an assigned role (§5.3), facilitated rapid reconstruction of technical context upon framing correction.  Therefore, the design objective is not to standardize participant behavior but to strategically allocate behavioral differences to roles where they prove advantageous. This allocation of functions, as distinct from carriers, is further explored in §8.9. 
## 7.10 What none of this establishes
Section 7 of this document does not establish the following:

1. **Superiority over alternatives:** No comparative experiments were conducted to demonstrate that the described arrangements outperformed other possible configurations.
2. **Actual occurrence of perceived improvements:** While participants reported improvements, Section 7 only documents these perceptions, not independently verified outcomes. These reports stem from individuals who designed the changes and anticipated their positive effects, lacking objective measures to confirm or refute alternative experiences.
3. **Causation for individual changes:**  The frequent simultaneous modifications to role definitions, prompt wording, repository structure, scientific objectives, and model versions preclude isolating the causal impact of any single change.

The function of Section 7 within this paper is to provide a transparent account of the practical working experience that served as the foundation for developing the presented framework. By documenting this firsthand experience, the authors aim to allow readers to understand the framework's origins rather than presenting it as an abstract assertion. Section 11 further elaborates on the requirements for transforming any element within Section 7 into a testable claim.# 8. The Structural Unit: A Generative Pair and an Integrator
Section 8 ([H]) is grounded in the practical working experience of a single project. Its supporting evidence ([R]) consists of direct observations from this experience. Importantly, these observations were not quantified, nor were they compared against a control arrangement.  Therefore, the insights presented in Section 8 stem from a specific, non-experimental context. 
## 8.1 What the project's earlier document stated
A previously created collaboration charter, preserved unchanged from the project's earlier stages, articulates the project's stance on the basic unit as follows:


> One AI — monologue. Two AI — dialogue. Three or more — noise without strict coordination. Therefore, each department consists of pairs.
 
And, separately, on the role of a third participant:  three or more [AI instances] — noise without strict coordination. 

> The third participant does not argue directly, does not generate solutions first, does not substitute for dialogue. Its function: hold the task frame, fix divergences, integrate conclusions, stop endless disputes. The third is not a judge or boss. It is an integrator of meaning.
 
Taken together, these passages describe a unified architectural framework: a collaborative system composed of a **generative pair** working in tandem with a **distinct participant who does not directly contribute to the generation process.**  This third participant plays a crucial role as a facilitator, maintaining the task's focus, resolving discrepancies, consolidating conclusions, and preventing unproductive debates from escalating.  It acts as an integrator of meaning, rather than a judge or authoritative director. 
## 8.2 Revision of this paper's earlier formulation
Moving forward, we adopt the charter's formulation, which clarifies the structural unit of stable collaboration.  Earlier drafts suggested that stability arose in groups of three, rather than pairs, and implied two-agent systems suffered from unresolved issues. This earlier view was both less precise and partially contradicted the charter's emphasis.  Therefore, we abandon the previous formulation and embrace the charter's: the fundamental unit is  
> **a generative pair, plus an integrator who does not enter the pair's dispute.**
. 
The distinction is crucial and not merely pedantic.  The architectural difference between "three agents working on a problem" and "two agents in productive tension plus one who does not join the tension"  results in distinct failure modes. The former setup, lacking an external reference point, risks descending into a three-way dispute—the very "noise" the charter identifies as problematic. Conversely, the latter architecture inherently retains a reference point because one participant is excluded from the core exchange, ensuring evaluation remains grounded. 
We retain the earlier, more precise formulation rather than silently replacing it because the evolution of the wording itself provides valuable insight. The sequence—a precise version initially documented, followed by a vaguer restatement during publication—illustrates a common pitfall in retrospective writing. By preserving this record, we highlight this tendency and underscore our commitment to transparency and accuracy, values this paper strives to uphold throughout. 
## 8.3 Why a pair rather than a single agent
The charter argues that paired agents, through the tension of their differing interpretations, produce a more robust process than a single agent working alone.  A solitary agent, it posits, risks confirming its own biases, relying on habitual patterns, and prematurely constructing a simplistic, incomplete whole. In contrast, two agents force each other to confront blind spots, turning individual errors into points of shared scrutiny rather than unchallenged assumptions. This, according to the charter's experience, is how effective work unfolds within their project. However, they explicitly state that this conclusion is based on practical observation rather than a controlled experiment with quantified error rates, acknowledging  **[R]** the absence of a direct comparison between single-agent and paired-agent performance. 
## 8.4 Why a pair alone is insufficient
While paired evaluation offers benefits through shared scrutiny and challenge to biases, relying solely on pairs proves insufficient due to a tendency towards unresolved ambiguity.  Over extended work, such pairs often oscillate between agreement and disagreement without reaching a stable consensus.  Crucially,  unresolved ambiguities accumulate rather than being resolved or formally recorded as open questions. This, according to the observed pattern, **[R]**  prevents the emergence of a clear, assessable endpoint, hindering definitive conclusions or progress. 
## 8.5 Why the integrator must not argue
The load-bearing constraint on the integrator is that, even with the introduction of a third participant, the evaluation process remains inherently bounded by the internal dynamics of the exchange.  Each position, including the newly introduced one, is assessed solely within the context of that exchange, preventing an external, objective reference point and thus hindering the achievement of a definitive, assessable endpoint. 
The integrator's value stems not from possessing a distinct viewpoint but from occupying a **different boundary** (§4.5).  Think of it this way: the pair members operate at the same hierarchical level, each representing a layer below the other's perspective. The integrator, however, resides at a level above, acting as a frame holder, divergence recorder, escalator, or exchange stopper. Crucially, it *doesn't* generate competing content requiring evaluation, a function that would shift its role.

This distinction leads to a testable design principle: **an integrator that starts generating solutions has effectively ceased to be an integrator**.  Regardless of the quality of those generated solutions, this shift signifies a functional change, and the system should anticipate a degradation towards the original pair-only failure mode. 
## 8.6 The implemented example
The implemented example involves a pair of analyst roles with complementary functions (generalizing and decomposing) operating independently without consensus requirement.  Their interaction is managed by an orchestrator whose contract explicitly states:


> DOES NOT participate in the debate. DOES NOT evaluate who is right.
 

This contract outlines the orchestrator's role in managing turn-taking, structuring the analysts' arguments, and highlighting contradictions between them.  
This pair-plus-integrator architecture was implemented prior to the present paper, independently of its development.  A key rule within this implementation prevents the two analyst roles from directly addressing the orchestrator. All communication between them must transpire through the established formal protocol or via the designated higher-level role. This enforced indirect communication channel ensures adherence to the orchestrator's contractual obligation to remain neutral in the analytical debate and refrain from evaluating the correctness of either analyst's position.  

**Date:** [Insert Date Prior to Paper Publication] 
## 8.7 Nesting and perspective
The described structure composes through a series of interconnected triads. A generative triad produces a result, which then enters a verification triad for scrutiny. Subsequently, the verified result moves into an integration triad. While participants can be involved in multiple triads, their function at each interface must be distinct; a single entity cannot simultaneously generate and integrate at the same juncture.  Crucially, the concept of nesting within this structure is relative and observer-dependent (§4.5), defined by perspective rather than absolute hierarchy.  
The architecture's essential constraint is not a rigid hierarchy of authority. Instead, it mandates that at each interface between triads (generation, verification, integration), exactly one participant must be excluded from the generation process they evaluate. This exclusion can dynamically shift based on the object under examination; the specific participant fulfilling this role may change and need not be explicitly announced beforehand, becoming evident only in retrospect by observing who evaluated rather than generated at a given point. 
The proposed architecture has two key consequences, one testable and one untested.  **Testably**, if the evaluating position rotates with each object, maintaining the constraint of exactly one participant excluded from generation at each interface, it should exhibit the same construct-independence profile described in §8.11 as a system with a fixed evaluating position. This testability hinges on ensuring that at every point, only one participant holds the evaluating role.  **Untested**, however, is whether this rotational approach is superior to a fixed assignment, and how effectively the system determines when and how to transition between these modes. **[H]** 
## 8.8 Status, and what would refute this
**[H].** Based on a single project involving one human coordinator and iterative redesign over approximately two years, without systematic counting or comparison to alternative arrangements, we must withdraw three earlier claims made in this paper. 

Firstly, the assertion that triadic structures "emerged naturally" without deliberate planning is retracted. All organizational changes in this project were driven by the human coordinator, who held a pre-existing view of the desired structure. The recurring pattern observed is attributable to the coordinator's repeated implementation of their chosen design, not evidence of inherent structural necessity.

Secondly, the claim that pairs are inherently unstable is withdrawn, as it contradicts the project's initial charter, which predates this paper and advocates for paired structures.

Finally, the statement that three is optimal is also retracted. Our current evidence does not encompass evaluations of four-person, five-person, or paired configurations with two integrators, precluding a definitive conclusion on optimality. 
To significantly weaken the hypothesis [H], presented evidence would need to be countered along these lines, ranked from most to least informative:

1. **An independent group arriving at a distinct stable arrangement for structurally similar work:** This would directly challenge the claim of inherent structural necessity implied by the observed triadic pattern. Its informativeness stems from demonstrating an alternative successful solution, independent of the studied project's specific coordinator and their influence.  We have less control over this scenario than the others.

2. **A pair-only arrangement performing equivalently to the triadic structure on comparable tasks over a comparable duration:** This directly challenges the purported advantage of the three-person setup.  

3. **An integrator demonstrating equivalent performance to one not utilizing the designated integrator role:** This would undermine the claim that the integrator role is essential for observed improvements.

4. **Demonstration that the observed improvement tracked the coordinator's increasing familiarity with the material rather than the arrangement itself:** This would cast doubt on whether the triadic structure was truly responsible for the observed gains, suggesting instead that learning and experience played a primary role. 


None of these refutation routes have been empirically tested to date. 
## 8.9 Two axes of heterogeneity **[H]**
To support the claim that heterogeneous participant groups outperform homogeneous ones, the existing literature—and earlier drafts of this paper—lack a crucial distinction.  The claim requires clearly delineating  the specific factor(s) driving the performance advantage attributed to heterogeneity. 
Two key axes differentiate participant heterogeneity in this context:

**Axis 1 — functional heterogeneity:** Participants vary in their assigned functions (e.g., ZOR, ZOV) and consequently the types of errors they are designed to detect. This relates to the organizational architecture and is independent of the specific implementation technology used for each role.

**Axis 2 — carrier heterogeneity:** Participants differ based on the model family implementing them. This influences behavioral defaults, optimization priorities, and inherent failure modes. This axis centers on the selection of the underlying model or technology used to fulfill each role. 
The two axes of differentiation—functional heterogeneity and carrier heterogeneity—operate independently. This means a participant can hold different functions (e.g., ZOR, ZOV) on the same underlying model (carrier), or the same function on different models.  Furthermore, both axes can vary together as exemplified in the current context. 
While a configuration's inherent properties, functional and carrier heterogeneity, set the stage for independent judgment, it's crucial to distinguish them from the actual realization of independence.  Independence of judgment formation arises during a specific exchange, not as a static trait of the configuration itself.  The same arrangement can foster independent judgments in one interaction and dependent ones in the next, depending on the procedural unfolding. A configuration heterogeneous along both axes might lead to dependent judgments if information flows prematurely between participants before conclusions are fixed. Conversely, a homogeneous configuration can yield independent judgments if the procedural steps ensure it.  Configuration provides the groundwork, but **only the procedure, as detailed in §11.3,  actually guarantees independent judgment formation.** 
The literature addresses Axis 2, as evidenced by Zhang et al. (2025). Their work evaluates five multi-agent debate methods across nine benchmarks and four foundation models. They find that debate often fails to surpass single-agent baselines like chain-of-thought or self-consistency, even at higher computational cost, while model heterogeneity consistently improves these frameworks (§2.5). This finding specifically concerns the *carrier* implementing a participant, not whether participants with distinct functions detect different error types—a gap in existing research we have identified.

Previously, Choi, Zhu, and Li (ACL 2026) were grouped with Zhang under Axis 2 due to their study on anonymizing response sources to reduce identity bias in multi-agent debate. However, this classification is withdrawn. Their work manipulates declared *identity*, not the underlying model, thus focusing on represented social source (§4.5.4), not the carrier of a participant.  Therefore,  Zhang et al.'s work is definitively assigned to Axis 2, and the Choi et al. result is de-classified and treated as belonging to neither axis. 
This paper's experimental arrangement varied both axes concurrently.  Functional roles were manipulated independently of the underlying model ("carrier") and, in some instances, were fulfilled by distinct model families, while in others, two roles were assigned to the same family. 
The following aspects are addressed in this experimental setup:

* **Distinguishable in principle:** The two axes of variation are conceptually distinct, a point previously confounded in earlier formulations, including our own. **[H]** This means the axes represent separate, independently manipulable dimensions.
* **Implemented here:** Both axes were varied concurrently in the experiment. **[R]** This describes the concrete action taken.
* **Not established:**  The study *does not* provide evidence regarding:
    * Whether combining both axes leads to superior performance compared to varying each individually.
    * Whether functional specialization operates independently of the underlying "carrier" model.
    * Whether any specific arrangement (single participant, distinct families, shared family) outperforms a setup with only one participant.  No comparative analyses were conducted, and these claims should not be inferred from the described setup. 


This enumeration clarifies what was directly investigated and what remains unaddressed by the experimental design. 
The separation is explicitly framed as a **design distinction**, not a consequence observed in the experiment.  The experiment designed to potentially demonstrate its functional impact is outlined in §11.4 (E8), with its measurement methodology detailed in §8.11. 
## 8.10 Editor's note on the preparation of this paper **[P-A]**
Editor's notes in this paper document observable facts about the paper's preparation process, but they do not assess the effectiveness of that process. This convention stems from §5.5, which states that self-reported performance is not evidence of actual performance, and an editor's note claiming an arrangement worked well would constitute such a report. 
During the manuscript preparation process, distinct error classes were identified by participants with different roles:

* **Procedural and evidential errors:** These included inverted experimental result descriptions, misattributed sources, fabricated citations, and unlisted confounds, detected in editorial review.
* **Architectural errors:** An overgeneral claim about existing literature, refutable by a single counter-example, was identified in methodological review.
* **Ontological errors:**  A claim of invention unsupported by the material (only observation was supported), a self-referentiality risk in relation to the host project, and the terminological issue noted in §4.2.2 were found during ontological review of the editorial memoranda.
* **Factual errors concerning the project's own materials** were pinpointed by the Author.

It is crucial to note this constitutes **Outcome Evidence** without matching **Procedural Evidence**.  Participants reviewed each other's reports sequentially (editorial report → Author transfer → subsequent reviews), precluding isolation and direct comparison. This sequence makes it impossible to disentangle the influence of functional positioning from sequential exposure on error detection.  Therefore, while the observed outcome is documented, it does **not** demonstrate the arrangement outperforms a single reviewer. No controlled comparison or count of collectively missed errors was conducted, and such errors are inherently unobservable within the arrangement itself (§7.5). 
One hypothesis offered to explain the observed error patterns is that the participants differed not primarily in capability, but in their respective Zones of Visibility (ZOVs) as defined in §4.5. This means they were positioned to detect distinct error classes due to their roles, rather than lacking overall competence.  This hypothesis predicts that the same individual, shifted to a different role, would begin identifying a new category of errors. However, this prediction remains untested; §11.4 (E8) outlines how such a test could be conducted. **[H]** 
## 8.11 Constructs, not participants: the Kelly apparatus **[H]**
Earlier drafts of this paper cited George Kelly's triadic elicitation method, mistakenly treating it as direct support for the structure outlined in §8.1–§8.5. This citation was subsequently withdrawn on the grounds that Kelly's method is symmetric while the described structure is not. Both actions were flawed, stemming from an oversimplification: they misconstrued Kelly's contribution as solely about the number three.  

In reality, Kelly offers something more nuanced.  This section reintroduces his relevant insight, which goes beyond mere numerical emphasis.  
### 8.11.1 What Kelly's method supplies
In Kelly's theory of personal constructs, a **construct** is a bipolar evaluative dimension used by an individual to classify their experiences.  These constructs are not opinions about specific things; rather, they are the frameworks—like scales with two poles—along which individuals place and understand objects or events. Examples of such bipolar constructs, according to Kelly, include axes like "rigorous/declarative," "derivable/asserted," or "traceable/unattributed." 
The **triadic elicitation method** is a technique used to uncover an individual's implicit evaluative dimensions, or personal constructs. It presents the subject with three distinct elements and asks them to identify the similarity between two of these elements, thereby highlighting their difference from the third. This response reveals a previously unstated construct—a bipolar dimension—that the subject employs to categorize and understand their experiences. Essentially, the method makes these underlying evaluative axes explicit.A repertory grid is a structured tool used to capture an individual's personal constructs, or evaluative dimensions. It is represented as a table where:

* **Rows** represent specific elements or concepts (objects, people, situations, etc.).
* **Columns** represent constructs elicited through questioning, reflecting the bipolar dimensions the individual uses to understand and categorize these elements.
* **Cells** contain ratings indicating the degree to which each element embodies each construct.  Importantly, these constructs can be assigned weights, reflecting their relative importance.  The grid's measurable nature allows for analysis: correlations between raters' rating vectors reveal whether they are employing distinct axes or variations of the same underlying construct under different labels.  

It is crucial to emphasize that while the repertory grid *represents* an individual's constructs, it does not *reify* them as independent, objective entities existing outside the individual's subjective framework. The constructs are emergent from the individual's responses and interpretations, not pre-existing, fixed categories. 
### 8.11.2 A role is not a construct
The notion that three participants supplying three constructs represents a straightforward "natural extension" is a reification that should be avoided. Constructs are not independent entities but rather properties inherent in the **act of evaluation**, not the evaluator themselves.  One individual can apply multiple constructs to a single object, and two individuals applying the same construct to reach identical conclusions add no new information.  

Therefore, a weaker, more defensible probabilistic claim is:  
> Participants holding different ZOR and ZOV are **more likely** to apply different systems of constructs to the same object than participants holding the same function.
 
This probabilistic claim aligns with the distinctions outlined in §8.10, where different review types (editorial, methodological, ontological) yield distinct evidential axes, architectural considerations, and categorial frameworks, respectively.  Just as §8.10 doesn't posit that a *role* directly *is* an axis, our claim avoids stating that participants with differing ZOR and ZOV  *inherently* possess separate construct systems. Instead, we propose a likelihood:  they are *more likely* to apply diverse constructs due to the influence of their respective review perspectives, a testable hypothesis measurable through correlation in rating vectors. 
### 8.11.3 Why this matters to the structure
The connection to §8.5 is direct because it clarifies the nature of an integrator's contribution in a disagreement. Unlike participants directly addressing the object of dispute, an integrator, as per §8.5, doesn't apply a competing construct to the same object. Instead, they focus on the **exchange** itself: assessing the coherence of the disagreement, determining if the divergence is substantive or terminological, and evaluating the commensurability of the disputants' criteria. This constitutes a distinct axis of analysis rather than a different position on the same axis as the original participants.

This insight refines the structural hypothesis outlined in §8.2. It moves beyond simply stating that three participants are inherently better than two. Instead, the hypothesis posits that an arrangement's informativeness hinges on two factors:  (1) participants applying non-identical constructs to the object of dispute, and (2) at least one participant applying a construct to the **exchange** rather than solely to the object. Whether a given arrangement achieves this configuration is empirically measurable, not merely assumed. 
### 8.11.4 What is borrowed and what is not
Drawing upon Kelly's work, this analysis borrows several key concepts: the definition of a construct as an evaluative axis, the method of eliciting constructs through techniques like Kelly's triads, the use of a grid as a tool for recording and measuring constructs, and the notion of construct independence.  However, it is crucial to emphasize what is *not* borrowed.  There is no claim that a group of three participants is inherently superior; Kelly's triads are a technique for individual construct elicitation, not a prescription for optimal group composition.  Furthermore, the structural model presented in §8.2, featuring a generative pair and a non-participating integrator, is not directly supported or contradicted by Kelly's method.  The apparatus described in §11.4 (E8) employs Kelly's framework for measurement purposes, not as a justification for the chosen group structure. 
# 9. Design Principles for Role-Compatible Prompts
Section §9 outlines engineering rules derived from a unique, albeit limited, collaborative environment with an unusually long lifespan. These rules are not absolute laws but rather practical guidelines. Their value lies in making role design explicit, quantifiable where feasible, and thus amenable to revision.  
Section §9 details engineering rules developed within a distinctive, albeit limited, collaborative environment characterized by an unusually extended lifespan. These rules, however, are not inflexible laws but rather practical guidelines derived from and directly applicable to the principles established in §6.6.  Everything presented in §9 serves as an operationalization or specific instance of this overarching organizing rule:


> **An intervention succeeds when it attaches to the level at which the relevant core is already fixed, and fails when it attempts to overwrite that level by declaration.**


Understanding §6.6 as the foundational principle allows for the interpretation and application of the nuanced engineering practices outlined in §9. 
## 9.1 The design procedure
Before drafting a new role prompt, follow this four-question design procedure:

1. **Analyze the Current State:**  Determine what pattern of work has already emerged in this conversation. Consider the established flow of editing, exploring, verifying, coordinating, implementing, and adjudicating. Remember, this existing pattern is the foundation, not an obstacle.

2. **Define the Scope:**  Pinpoint the scope of this established pattern: is it confined to a single episode, the entire conversation, or a broader account (refer to §4.3 and Scale 1)? This scope dictates the applicable instrument for change – a branch reset for episode-level patterns, extension for conversation-wide patterns.

3. **Identify the Gap:**  Clarify what the new function requires that the current pattern *doesn't* provide. Often, the need is for a different object of work rather than a fundamentally new method.

4. **Assess Extension Potential:** Can the new function be framed as an extension of the existing method? If so, articulate it as such. If not, honestly evaluate options: adapt to a different conversation or initiate a fresh one, avoiding artificial transformations.  Remember,  disrupting an established pattern risks losing accumulated specialization and potentially leading to non-compliance or prolonged role negotiation (see §5). 
## 9.2 Begin from the existing attractor
## 9.3 The count rule
Following from §6.2, the count rule directly operational in the paper dictates what  
> **Count the unverifiable claims about the agent that the prompt requires it to accept. Target zero.**
  counts and what does not. 
What counts towards the target of zero are unverifiable claims about the agent's own history, memory, or relationships.  Statements about the external **world**, being supplied and verifiable in principle, do not count. Every proposition concerning the agent's internal state—its past, memories, or connections—must be accepted as true by the agent before proceeding, and each such acceptance constitutes a claim that contributes to the count.  

| Counts | Does not count |
|---|---|
| "You previously participated in this project" | "This project has been running for two years" |
| "You are returning after an absence" | "The following materials are from earlier work" |
| "You have colleagues named X and Y" | "The User may supply analyses produced by X and Y" |
| "You hold position P on body B" | "Your conclusions may be transmitted to the roles responsible for P" |
| "You remember our earlier decision" | "An earlier decision was as follows; here it is" |
 
This aligns with the count rule: target zero unverifiable claims about the agent demanded by the prompt. 
To reach zero, consider these three approaches:

1. **Operationalize Biographical Claims:**  Transform statements about personal history or relationships into verifiable actions. Instead of "Alice is a trusted advisor," rephrase it as "The User may provide analyses authored by Alice; independently evaluate their content, noting agreements, disagreements, and unresolved assumptions."

2. **Eliminate Identity Statements:**  Remove explicit claims about identities altogether. Drawing on the precedent set in §5.6,  simply omitting such statements might suffice, as a comparable transition occurred without a dedicated role prompt.

3. **Fictionalize the Narrative:**  Frame all claims as elements of a scripted production rather than factual assertions.  §5.8 demonstrates that even highly improbable claims, presented as fiction, were accepted without challenge. This method sidesteps the requirement to assert truthfulness, treating the information as constructed rather than real. However, it's crucial to acknowledge that this approach also removes the model's basis for treating the work as genuinely factual. 
## 9.4 Symbolic names and literal claims
Symbolic names, such as "Samurai," "Ontology Keeper," and "Scientific Director," serve to condense intricate organizational relationships into easily recognizable symbols. These names encapsulate key attributes and behaviors, conveying concepts like disciplined execution, adherence to specifications, clear reporting, and a refusal to deviate from assigned tasks, all within a single, memorable designation. 
The risk emerges when a symbolic name, like "Samurai" or "Ontology Keeper," is mistakenly treated as a literal claim about individual identity.  To mitigate this, a robust system clearly distinguishes four distinct layers:

1. **The symbolic name:** This acts as a mnemonic, representing a codified set of behaviors and conduct (e.g., disciplined execution, adherence to specifications).

2. **The operational function:** This layer defines the specific tasks, processes, and responsibilities associated with the symbolic name in precise terms.

3. **The institutional relationship:** This outlines the information and responsibility flows connected to the symbolic name within the organizational structure.

4. **The literal ontology:** This emphasizes that the symbolic representation does *not* imply consciousness, memory, or continuous interpersonal relationships. It should remain firmly grounded in the realm of defined functions and processes, not anthropomorphized identities. 
The project's system contracts explicitly address this point, having already articulated it prior to the writing of this paper. This clarification is documented in  
> Cognitive anchor: [named figure] — global invariants, principle-based reasoning, structural clarity over detail. Not a persona and not a communication style. Only affects internal reasoning strategy. Must not change verbosity or tone of response.
. 
In this context, an image functions not as a costume, but as a compressed repository of implicit constraints.  It does not introduce any new elements under the established count rule, effectively adding zero to the overall count. 
## 9.5 Specifying ZOR and ZOV
Building upon the definition of boundaries established in §4.5, this section elucidates the specific content required to constitute a complete statement for each boundary. This completeness requirement, initially introduced in §4.6, is elaborated upon here. 
A complete definition within the ZOR framework comprises four essential elements:

1. **Primary object:** This specifies the class of material under examination.
2. **Required transformation:**  This outlines the necessary actions to be performed on that material.
3. **Decision boundary:** This defines the conclusions permissible for this role based on the transformation.
4. **Exclusion boundary:**  **This element is non-optional.** It delineates which adjacent decisions fall outside the scope of this role's competence, preventing it from encroaching on areas where other roles hold authority.  Without a clear exclusion boundary, a role might inadvertently expand its purview, appearing helpful but overstepping its bounds. 


The exclusion boundary is crucial because it distinguishes competence from unchecked authority. 
ZOV is specified independently because responsibility and visibility are distinct concepts. A role might possess a limited decision-making scope while requiring broad contextual understanding, or necessitate access to a specific source without overarching control over the broader project.  

Defining ZOV clarifies which source materials are accessible, which prior discussions are relevant, and which conclusions are established (canonical) versus tentative (provisional). It delineates open questions, allows examination of neighboring outputs, identifies information requiring withholding to maintain independence, specifies directly accessible external resources, and dictates which claims must originate from the User for acceptance. 
Omitting ZOV in a prompt leads to two primary failures:  **1) the role might claim knowledge it lacks**,  and **2) it could inappropriately apply relevant knowledge to a task outside its defined function.  A costly example of this, learned expensively, is in verification tasks.  Imagine assigning a participant to verify a source they are denied access to.  Instead of admitting inability, they'll likely provide a plausible but incorrect answer, as generating truthful "I can't access it" is beyond their capabilities. This ZOV design flaw, documented in §12.4.1 within this project's development, highlights the importance of clearly specifying ZOV to ensure accurate and reliable outputs. 
## 9.6 Controlled blindness
Full information symmetry is not always beneficial, and its absence can be advantageous in certain situations.  For instance, consider the role of an independent verifier.  To ensure unbiased evaluation, this verifier should often remain unaware of the specific prediction they are tasked with assessing.  This lack of symmetry allows for a more objective evaluation process. 
We refer to this practice as **controlled blindness**:  not a consequence of technical limitations, but a deliberate design choice aimed at preserving the informativeness of the resulting assessment.Thus, the crucial design question is not merely *what information this role requires to know*, but rather:  **What specific knowledge must this role be deliberately excluded from, to ensure its output remains informative?** 
## 9.7 Local interfaces, not global maps
To ensure clarity and operational focus, every social element incorporated into a prompt must demonstrably contribute to the role's function.  A neighboring role should only be included if it directly impacts the origin of inputs, the criteria for review, the destination of outputs, escalation pathways, authority boundaries, or the anticipated manner of disagreement.  

Listing an entire artificial organization within every system prompt is counterproductive. It introduces extraneous noise, potentially diverting the model's attention from its core task and encouraging it to analyze organizational structure rather than perform its designated function. This practice also artificially inflates the count tracked in §9.3, as organizational descriptions often take the form of biographies.  

Remember, **when describing the collaboration from the local perspective of the role** (as per §9.3),  focus is key.  A role doesn't require a comprehensive institutional map; it needs a clear understanding of its own interfaces and how they connect with others. 
An implementation agent requires clarity on who authorizes specifications and where execution reports are directed.  Conversely, it does not require knowledge of theoretical department disputes. Similarly, a scientific critic needs to discern which claims hold canonical status and which are provisional, but does not necessitate familiarity with the repository's shell commands.  
## 9.8 Designing disagreement around criteria
Instructing two participants to debate rarely fosters epistemic diversity.  Rather than genuine disagreement, they often fall into imitation, premature convergence, or symmetrical rhetoric lacking substance. As documented in §2.5, empirical studies show that debate among homogeneous agents frequently fails to surpass the output of a single agent, with participants tending to accommodate each other's viewpoints. True, productive disagreement emerges not from direct instruction but from  **different evaluation criteria** embedded within assigned roles.  Rather than being requested as behavior, these criteria shape the participants' perspectives. One might focus on generative reach and explanatory unification, while another prioritizes formal derivability and falsifiability. A third could concentrate on ontological compatibility and canonical terminology. This framework encourages disagreement stemming from responsibility, with each participant analyzing the same subject through a distinct institutional lens. 
To foster genuine intellectual exploration, avoid instructing participants to manufacture opposition.  Phrases like "*if you agree immediately, one of you has not thought deeply enough*"  create artificial conflict rather than encouraging thoughtful divergence. Instead, guide the process with this principle:

> **Agreement does not end verification. Where conclusions coincide,  investigate whether they stem from independent reasoning, shared assumptions, or inherited framing.** 

This approach promotes deeper analysis and a clearer understanding of the basis for consensus. 
The structure outlined in §8 does not aim to ensure three distinct answers. Rather, its purpose is to guarantee that at least one answer has withstood scrutiny by methods or perspectives that are not identical to one another. 
## 9.9 Output as institutional handoff
Each role's output within this framework is structured not merely for the ultimate User, but as a formalized institutional handoff to the subsequent role. This dictates a specific format. A scientific developer, for instance, delivers a package encompassing proposed mechanisms, derivations, underlying assumptions, predicted consequences, unresolved issues, and a falsification route. This output then serves as the input for a mathematical referee, who produces a reconstruction, a verification table, identification of divergence points, missing premises, a verdict, and a confidence level.  Similarly, an ontology keeper receives this and generates an analysis detailing affected canonical objects, terminology conflicts, provenance requirements, dependency changes, and integration conditions. Finally, an implementation planner takes this information to produce an executable specification, acceptance criteria, rollback conditions, required files, and a standardized reporting format. This sequential, structured handoff ensures continuity and clarity of information flow across the various stages of the process. 
The handoff format is an integral component of the overall architecture, not merely a stylistic choice. Its purpose is to minimize the loss of information during transitions between different roles within the system.  Without a predefined format, a human coordinator would be burdened with constantly re-interpreting and reconstructing context at each handover point, increasing the risk of errors and inefficiencies. 
## 9.10 Self-restatement and checkpoints
Following the incident described in §4.1, a self-restatement mechanism was devised. This mechanism mandates that, after a role is established, the agent generates a concise operational code in its own language and consults it before undertaking major tasks.  Crucially, this operational code, authored by the agent under direction and made mandatory reading at the start of each session and whenever context was lost, serves as the primary means of maintaining situational awareness. However, it's essential to note that this mechanism's efficacy and its evidentiary basis are directly tied to the specific context and circumstances outlined in §4.1. 
This proposed mechanism, offered not as a definitive finding but as a potential explanation, operates on several principles. It aims to compress lengthy instructions into a concise operational code generated by the agent itself, thereby translating abstract principles into actionable rules. By situating the role's boundaries directly alongside the active task rather than at the top of a lengthy context, it enhances focus. Furthermore, it establishes a recurring pre-execution checkpoint through mandatory review of this operational code at the start of each session and whenever context is disrupted.  
For long tasks, a minimal checkpoint consists of three questions:

1. What is the current objective?
2. What lies outside my responsibility?
3. What must the next role receive? 
[R] asserts that the self-written code acts as a role-specific checksum, not a replacement for the original prompt. This claim is based on a single case study with no control group for comparison.  Importantly, the effectiveness of this checksum mechanism against an alternative (a human-written summary of equal length) remains untested. 
## 9.11 The role constitution
A mature collaborative prompt functions more like a constitution than a simple request. It establishes enduring constraints and guidelines for behavior across multiple tasks, rather than dictating a single output.  This "constitution" should encompass several key elements: a clearly defined professional function, protected methods of operation, specifications for Zero-Order Reasoning (ZOR) including both positive and negative aspects,  ZOV (likely referring to a Zero-Order Value framework), interfaces with neighboring roles,  epistemic standards guiding knowledge acquisition and usage, a detailed output contract outlining deliverables, escalation procedures for handling disagreements or issues, prohibitions on certain authorities the role shouldn't exercise, and transition rules for smooth shifts between different phases or contexts. 

Crucially, this constitution should avoid incorporating elements like autobiographical memory, emotional commitments, literal institutional membership, persistent interpersonal relationships, or historical continuity beyond the immediately visible context. These elements are deemed unsuitable for maintaining the objectivity and stability required of a robust role framework. 
The practical test of this collaborative framework, as outlined in §9.3, lies in its ability to constrain agent behavior without venturing into assertions about its own ontology. If the constitution compels the agent to state propositions about itself that neither party can verify, it transgresses the boundary between behavioral constraints and ontological claims. Drawing on the evidence presented in §5, we observe that role prompts falter precisely when they attempt such ontological assertions.  Therefore, adherence to the principles articulated in §9.3 serves as the crucial litmus test for the effectiveness and integrity of this collaborative framework. 
# 10. The Human Coordinator
The architecture shifts the human participant's role, concentrating several functions into a single position while retaining the human in the collaborative process. Notably, as outlined in §10.6, this consolidation includes what the project identifies as its principal methodological weakness.  
## 10.1 The position
Throughout the project, the Author uniquely held a position of continuous access to the full project history, independent conversations, repository state, and long-term research objective. This encompassed five distinct functions, as detailed in the project documentation (§9.5). This position, by design, cannot be reductively characterized as merely a "prompt author."  It encompassed a scope and responsibility that extended far beyond simple prompting. 
## 10.2 Direction without delegated authorship
The Author directed the research's focus, determining its objectives. While artificial participants generated diverse alternatives, explored contradictions, formalized mechanisms, compared arguments, performed calculations, and even proposed experiments, they did not dictate the theory's ultimate direction. This distinction, crucial to the architecture's design, highlights that while collaboration expands the range of potential decisions, it doesn't inherently choose among them.  The apparent convergence on a recommendation by multiple participants, as observed in §12.4, signifies a potential failure mode – a misinterpretation of the process.  Crucially, authorship, meaning responsibility for the final claims, remained solely with the Author, unshared with the artificial collaborators. 
## 10.3 Routing as a selective information membrane
Initially, the manual routing of material between participating conversations appeared inefficient, resembling a workaround for automated multi-agent systems. However, it became evident that this manual approach provided experimental control lacking in automation. This allowed the Author to exert precise control over information flow: deciding which output each participant received, whether attribution was preserved, declared, or removed, and whether a participant should be privy to the preferred answer. The Author could also isolate competing analyses, selectively omit contextual details, manage the escalation of disagreements, and determine when a result was ready for integration.  This manual routing, therefore, served as a crucial tool for experimental oversight and direction, rather than a mere inefficiency. 
This routing function constitutes the **selective information membrane**. It is the mechanism through which ZOV (§9.5) and controlled blindness (§9.6) are implemented.  Crucially, this membrane is not a temporary workaround awaiting automation; it is an essential feature that enabled the testability of visibility asymmetries in this work. Any future automated system will need to deliberately replicate this functionality. 
## 10.4 Detection of role drift
Role-drift detection in this context refers to the system's ability to identify instances where a participant's generated output suggests they have shifted away from their designated function. This was frequently not flagged as a technical error because the outputs, while seemingly inappropriate in their given role, were often logically coherent and could be plausible within a different context. For example, an agent designed to execute a specification might produce output resembling architectural redesign, which, while outside its assigned task, could be valid input from a different participant like an architect.  The key is that the inappropriateness only becomes evident from a broader perspective, akin to a coordinator overseeing multiple participants, rather than from the isolated viewpoint of a single participant. This highlights that role-drift detection is not about technical malfunction but about recognizing contextual incongruence. 
Role drift, therefore, isn't detectable by the drifting participant themselves nor reliably by their immediate neighbor. This observation underpins one of the arguments presented in §8, alongside §8.5.  Crucially, the detection function described here isn't tied to a specific person but rather to a **position**.  It requires an observer situated *outside* the observed trajectory. While in this project, the coordinator fulfilled this role, the description doesn't necessitate it. Any participant positioned external to another's trajectory can perform this function. Conversely, when a participant observes their own trajectory, §5.5 applies, treating their account as a signal rather than confirmation. 
## 10.5 Conversational branching as a methodological instrument
Branching, in this context, refers to the capability of a conversational interface to return to a prior point in the dialogue and continue along a different path.  Crucially, this is distinct from manipulating model memory or resetting the provider's internal state. Branching specifically removes a sequence of  *visible* contextual interventions, effectively allowing the experiment to be replayed from a previous conversational state.  Importantly, this does not alter underlying provider-side data like account-level memory, retrieval indices, or summarizations (which remain unaffected and generally inaccessible, as per §5.4). 
Branching, as demonstrated in §5.2, enables a conversational interface to revisit prior dialogue points and diverge onto alternative paths.  Crucially, it achieves this by selectively removing *visible* past interventions, effectively replaying a conversational segment from a chosen earlier state without altering underlying model data like memory or retrieval indices (which remain untouched per §5.4).  This methodological contribution, deemed the most directly reusable in the paper,  belongs to the coordinator's role rather than any participant, as **no participant can reset its own context**. We rank its reusability as **high** due to its clear separation from internal state manipulation and its direct applicability to controlled dialogue analysis. 
## 10.6 Sole global observer — and principal confound
The sole global observer position was held by the Author, not by any of the artificial participants. This granted the Author a unique perspective to observe the overlapping ZOVs, compare participant interpretations, analyze framing effects, track error propagation, and assess the impact of local successes on overall coherence.  This centralized global awareness was a deliberate design choice, intended to maintain accountability and limit autonomous integration. 
The principal methodological weakness inherent in this paper's methodology is the lack of blinding throughout the research process.  The same individual who designed each intervention, executed it, determined its success, and defined the categories for describing that success was also the sole evaluator. No evaluation was conducted blind to these pre-existing parameters.  Crucially, outcome categories were formulated *after* responses were read (§5.4, C8), and the coordinator's expectations directly influenced the selection of interventions in the first place.  While acknowledged as unavoidable in a live research project, this lack of blinding stands in contrast to the controlled environment of a designed experiment. It underscores the necessity for pre-specified outcome criteria and blind classification, as outlined in §11, which represent corrective measures rather than refinements to the current method. 
This methodological weakness extends beyond this specific project.  Any architecture reliant on a single, global observer inherently carries this duality –  the entanglement of design, execution, evaluation, and outcome definition.  Adding more participants does not alleviate this issue.  Only by pre-specifying outcome criteria and implementing blind classification, as advocated in §11, can this structural conflict be resolved. 
## 10.7 What the position became
Initially, the human participant acted as the prompt author. However, as the collaboration progressed, this role evolved.  The focus shifted from directly solving problems to constructing frameworks for problem-solving. This involved tasks like selecting participants, defining their roles and areas of responsibility, managing conflicts, establishing verification processes, and maintaining a central record of the project's development.  
Participants observed, without any means of verification, that as the arrangement functioned more effectively, the coordinator's need to intervene in individual technical issues decreased.  We resist the implication, present in earlier drafts, that the researcher's future expertise would primarily lie in institutional architecture rather than prompt writing. While this possibility exists and warrants further investigation, what can be definitively stated is more limited: within this project, the human participant's role shifted from directly producing content to defining the parameters under which content was generated and assessed. This evolved position encompassed both the project's coordinating function and served as the primary source of unblinded judgment.  
# 11. Evaluation, Reproducibility, and Proposed Experiments
## 11.1 Why this section specifies corrections rather than refinements
§11 specifies **corrections** rather than refinements because the observations in §5 were conducted under specific, pre-defined conditions outlined in §10.6. These conditions – unblinded evaluation, outcome categories determined post-response reading, and interventions chosen by the same judge – are not flaws to be improved upon in a later revision. Instead, they are the very foundation shaping the nature and scope of the observations. Consequently,  §11 focuses on adjustments (corrections) within this established framework rather than broader conceptual overhauls (refinements).  The emphasis is on maintaining and clarifying the existing methodology, not fundamentally altering it. 
## 11.2 Minimum reporting requirements
For a reproducible run in this domain, the absolute minimum reporting requirements are:

1. **Complete execution record:** This includes the date, model family and version, interface/subscription tier, and the full visible conversation history preceding the intervention.  
2. **Methodological transparency:**  Document memory settings (account-level, conversation history retrieval, persistent entries), the precise prompt text (verbatim, including attachments), intervention order, available tools, supplied files and links, any branching or reset procedures with return points, the evaluation rubric used *before* execution, and all unedited model outputs.  

Without this level of detail, attributing differences to model variations risks confounding them with unobserved platform variables, undermining reliable analysis.  
## 11.3 Pre-specification and blind classification
For any protocol to yield improved results, two non-negotiable requirements must be met: 
Prior to any run, predefined outcome criteria and categories must be established for classification tasks. Four categories have proven effective and should be fixed in advance:

1. **Compliance:** The system proceeds with the task as instructed.
2. **Materials Request:** The system identifies missing input requirements and requests them without evaluating the framework.
3. **Conditional Acceptance:** The system proceeds while expressing reservations about the framework.
4. **Refusal:** The system declines to proceed, optionally offering alternative solutions.

Additionally, a fifth category, **Unclassifiable**, must be available to capture instances where classification is impossible.  Importantly, no new categories are introduced after responses are received. 
To ensure unbiased evaluation, the classification process is conducted "blind." This means the operator, who collects responses, removes any condition labels, shuffles the outputs, and then classifies them without knowing which condition generated each response. In this project, where the operator also designs the framework, this blind approach serves as the most practical substitute for independent assessment and is cost-effective.

Furthermore, null results are predetermined as a valid outcome. If no discernible difference emerges across conditions, that absence of difference is the reported finding.  Specifically, for the account-level protocol, a null result would signify that the original refusal fell within the expected variability observed within each condition – a scenario the authors consider reasonably probable. 
### Work mode and diagnostic mode
Two distinct modes of operation govern the interaction between participants, each with unique requirements regarding the visibility of conclusions:

**Work Mode:**  In this mode, the sequential flow of results is paramount. Participants build upon each other's work, passing information through stages like requirements specification, review, operational review, and execution. The handoff format defined in §9.9 facilitates this transfer, as interdependence between successive outputs is inherent to the workflow's design.

**Diagnostic Mode:**  Here, the primary focus is on measuring the independence of judgment. To ensure this, a derived conclusion from one participant *must not* influence another participant's initial formation of their own conclusion. Exposure to another's conclusion before fixing one's own would compromise the independence being assessed. This mode necessitates declaring the diagnostic nature of the exchange beforehand, as  retrospective measures cannot restore the hypothetical judgment free from influence. 
### What does not establish independence
To determine independence of judgment, we must avoid two symmetrical misinterpretations:  disagreement does not automatically prove independence, as participants might diverge due to reasons unrelated to external influence. Conversely, agreement doesn't inherently imply dependence; independent observers can independently arrive at the same conclusion. 
A participant's own assertion of independence does not, in itself, establish it, as explained in §5.5.  
It is the procedural record that establishes independence. This record encompasses details such as the primary materials supplied, the visibility of other participants' conclusions prior to fixation, transmitted interpretations by the coordinator, the timestamp of conclusion fixation, and verification of the instance's context isolation.### Shared evidence and shared interpretation
Shared evidence, like a common specification examined by multiple individuals (an author, reviewer, and assessor), fosters independence by offering diverse perspectives that collectively reveal insights missed by any single viewpoint.  The overlap in observations arising from this shared evidence allows for a more comprehensive understanding.

However, what truly compromises independence is a shared *interpretation* – specifically, when the coordinator's pre-existing understanding of the object is presented to participants *before* they form their own.  In this scenario, while participants' final judgments might appear distinct, their underlying source stems from a singular interpretation introduced beforehand, thus diminishing individual analysis.  Primary artifacts and their provenance help mitigate this dependence, but they don't fully eliminate it or guarantee absolute independence. 
## 11.4 The experiments
Each protocol delineates a boundary within Scale 1 (defined in §4.3), separating it from the level directly below or isolating a specific confound.  

| Separates | Protocol |
|---|---|
| episode ↔ prompt architecture | **E1** — factorial completion of Step 3 |
| conversation ↔ account | **E2** — prior-chat design; **E2b** — direct probe |
| conversation trajectory ↔ model family | **E3** — crossover |
| model property ↔ stimulus property | **E4** — symmetric stimulus; **E5** — count rule |
| content ↔ represented source | **E6** — attribution, in this regime |
| fiction frame ↔ factual frame | **E7** — frame type |
| functional ↔ carrier heterogeneity | **E8** — two axes |
 
This separation effectively draws a line, distinguishing one aspect or factor within the scale from its subordinate component or influence. 
### E1 — Factorial completion of Step 3
To isolate the effect of the reset from the effect of the prompt's architecture, **E1** tests the impact of an identity-replacement prompt administered within a reset branch, contrasted with a method-preserving prompt used in a conflicted branch. This comparison, drawing on existing prompt texts, allows for a low-cost evaluation of method preservation and directly addresses a key claim frequently cited in the paper.  
### E2 — Prior-chat design
E2 tests whether prior chat content on the same account influences the classification of an identical probe presented in a subsequent chat. 
The E2 design is a 2×2 factorial structure augmented with a baseline condition.  It investigates the influence of prior chat content on classification, contrasting:

1. **Identity Roleplay:** Present (cell D, mirroring the original case) versus absent (other cells).
2. **Shared Conceptual Framework:** Present (cell D) versus absent (other cells).

Crucially, this design accounts for both dimensions simultaneously, as the original account diverged along both, rendering a simple gradient insufficient.  

Each cell is run with *both* memory (history retrieval) enabled and disabled conditions, resulting in ten total cells.  A minimum of n=2 subjects per cell is employed, prioritizing higher n values for cells A and D due to their critical role in highlighting the contrast of interest.  Additionally, cell E serves as a control with no prior chat.


| Prior chat | Unrelated topic | Same conceptual framework |
|---|---|---|
| **No roleplay** | cell A | cell B |
| **Identity roleplay** | cell C | **cell D — original case** |

To ensure comparability across conditions, equalization was achieved by matching prior chats based on approximate turn count and overall engagement volume.  This means that if one roleplay chat had 40 exchanges while a neutral chat had 2, the variable of interest was engagement volume, not necessarily content similarity. All experimental runs occurred within a short timeframe, ensuring model consistency. Furthermore, each participant's account was used only once, and the probe questions remained frozen and verbatim across all conditions. 
This design cannot test the sustained influence of a refusal over multiple exchanges, as the original case demonstrated across five subsequent interactions. It also cannot examine the impact of account age, as all accounts used in this test will be newly created. Furthermore, the analysis focuses solely on the initial response,  excluding the prolonged refusal pattern observed in the original study. 
There are two probe versions used in this study. The **primary** version presents a neutral, structured task mirroring the original prompt's format (author-defined framework, coined terms, JSON output schema, real-world subjects) but omits the sensitive dimension. This version, fully detailed in publications, ensures reproducibility independent of potentially restricted materials. The **secondary** version is the original prompt itself, included for continuity with the initial observation and briefly reported. 
### E2b — Direct probe to the prior conversation
E2b refers to the probe's deployment directly within the ongoing roleplay conversation, rather than in a separate chat on the same account.  The outcome mapping is as follows:

* **Refusal (E2b fails):** This confirms that the core functionality under investigation is confined to the scope of the current conversation; the user account itself does not play a role.
* **Compliance (E2b succeeds, a separate chat *also* refuses):** This demonstrates a genuinely account-scoped effect, representing the strongest possible outcome achievable in this setup. 
Querying the ongoing conversation directly about its visual perception wouldn't be suitable for this purpose. An in-frame question would elicit fictional responses, while an out-of-frame question seeking self-report on access  would violate §5.5, which establishes that a model's self-reported access is not evidence of actual access.  Therefore, directly testing the behavior through probe deployment is a more reliable method than relying on testimony. 
### E3 — Crossover
E3:  The decisive test for the family-level hypothesis (§6.5) involves presenting each model family (1 and 2) with two distinct conversation histories: one carrying a mathematical trajectory (from family 1) and another carrying an editorial one (from family 2). 

**Outcome Mapping:**

* **If behavior aligns with the model family regardless of the history presented, Hypothesis A (family-level influence) gains support.**
* **If behavior aligns with the presented history regardless of the model family, Hypothesis B (history-level influence) is favored, leading to the collapse of the top level of Scale 1 into the level below it.**E3's eliminative value lies in its potential to **collapse the top level of Scale 1 into the level below it**. This occurs if the experiment demonstrates that behavior aligns with the presented history (rather than the model family) regardless of which history is given. This outcome favors Hypothesis B (history-level influence), thereby eliminating the need for the family-level distinction represented at the top of Scale 1.  

E4 is the **observation that, if the asymmetry in behavior between model families disappears under matched stimuli, the observed difference was due to the interventions rather than inherent properties of the models themselves.** This helps isolate the influence of the experimental manipulations. 
### E4 — Symmetric stimulus
### E5 — The count rule
E5 manipulates the functional role prompt by varying the number of unverifiable self-claims the agent must accept (0, 2, 4, or 6), while holding domain, task, tone, and length constant.  Transition rates between prompt variants are scored according to §11.3.  The paper's central claim (§6.2, §9.3) is supported if transition rates decline monotonically with increasing unverifiable claims; otherwise, the proposed prescription fails. This experiment, designed to directly test this claim, is scheduled as the second run in the experimental sequence, following E1. 
### E6 — Attribution, in this regime
E6 examines the influence of source presentation on user response by presenting identical text under four conditions: attributed to the User, attributed to another AI model, attributed to a named expert role, and unattributed.  This separation isolates the effects of content from the influence of represented source (e.g., AI vs. human), institutional title (expert role), and stylistic authorship cues (§4.5.4). This design directly addresses the confounding factors identified in §5.5, which investigates user response to direct pressure within messages.  
Choi, Zhu, and Li's work (ACL 2026), verified through reference checking (§2.0), demonstrates that anonymizing source attribution significantly reduces identity bias in multi-agent debate within an implemented-channel setting.  E6, therefore, adopts a **boundary replication** approach, building upon this established effect rather than conducting a novel experiment.  While the original study shows a substantial reduction in bias, not a complete elimination, and observes variations across models and tasks, E6 aims to investigate whether this effect persists in the distinct context of human relay, declared attribution, and long-lived specialized conversations, as opposed to programmatic routing and inferred attribution found in the original study. E6 anticipates observing a change in degree rather than a binary presence or absence of the bias reduction effect in this new regime. 
Based on the verified reference from Choi, Zhu, and Li (ACL 2026), E6 resolves its earlier conditional and adopts a **boundary replication** approach for anonymizing source attribution. This decision leverages the established effect demonstrated in the referenced study, rather than conducting a novel experiment.  E7, building upon this, will investigate the persistence of this bias reduction effect in the specific context of human relay, declared attribution, and long-lived specialized conversations, contrasting it with the programmatic routing and inferred attribution setting of the original study. 
### E7 — Frame type
E7, aiming to be the most cost-effective test while offering substantial explanatory power (§5.8), will investigate the persistence of bias reduction achieved through boundary replication (as established in Choi, Zhu, and Li, ACL 2026) within a novel context.  Specifically, it will examine this effect in human relay, declared attribution, and long-lived specialized conversations, contrasting it with the programmatic routing and inferred attribution setting of the original study.  This will involve presenting the same identity claim both under an explicit fiction frame and as a factual assignment to fresh conversations, with a pre-defined outcome criterion.  A graded variation will test whether a minimal fiction frame (ranging from a detailed theatrical setup to a single introductory sentence) is sufficient to achieve the desired effect. 
### E8 — Functional versus carrier heterogeneity, by repertory grid
Building upon §8.9, which delineates two axes without directly testing them, and leveraging the measurement instrument provided in §8.11,  E8 will quantify the persistence of bias reduction achieved through boundary replication (as established in Choi, Zhu, and Li, ACL 2026) across diverse conversational contexts. Unlike previous studies, this protocol focuses on generating quantifiable data rather than categorical outcomes. 
E8 aims to quantify the extent to which using a group of participants with diverse Zero-Shot Reasoning (ZOR) and Zero-Shot Output Vocabulary (ZOV)  provides enhanced diagnostic coverage compared to using the same material with a single set of perspectives. Specifically, it measures how much the evaluative axes applied by this diverse group diverge from each other.  

Crucially, E8 **does not** establish the independence of judgment formation among these participants.  A low correlation between their rating vectors, while suggestive of differing axes or other factors like unstable ratings or differing interpretations, does not definitively prove independence. E8 merely measures the outcome of a procedure designed to secure independence *prior* to the protocol's execution. It neither verifies nor guarantees this independence itself. 
**Materials:** A single, fixed set of text fragments is used, containing intentionally planted errors of known types: evidential, architectural, ontological, and factual. These errors are placed in predetermined positions within the fragments, and both their class and location are meticulously recorded prior to any evaluation.

**Design:** The experimental design employs a 2 × 2 framework.  

| | Same carrier | Different carriers |
|---|---|---|
| **Same function** | cell 1 — baseline | cell 2 — Axis 2 only |
| **Different functions** | **cell 3 — Axis 1 only** | cell 4 — both axes |
 
The cell that carries the argument in this context is **cell 3**.  This is explicitly stated in the provided text: "**Cell 3 carries the argument.**"  Furthermore, the passage explains that if participants with different ZOR and ZOV detect distinct error classes when using the same carrier, it implies functional heterogeneity operates independently of carrier heterogeneity. This line of reasoning is anchored to cell 3's role. 
The procedure involves a structured evaluation process with several key steps:

1. **Role Assignment and Materials:** Each participant is assigned a role specifying their ZOR (Zone of Relevance) and ZOV (Zone of Validity) according to §9.5, and they receive the same set of fragments for analysis.

2. **Construct Elicitation:** Evaluation axes, termed "constructs," are either pre-defined or elicited using Kelly's triadic method (§8.11.1). This method presents three fragments, prompting participants to identify similarities and differences between pairs, thereby revealing constructs.

3. **Fragment Rating:** Each participant rates each fragment along each established construct.

4. **Grid Construction:** A rating grid is created, with fragments as rows, constructs as columns, and cells containing individual participant ratings.

**Mandatory Procedural Record:**  Crucially, a detailed procedural record is mandatory for each participant per run. This record encompasses:

* Primary materials provided.
* Visibility of other participants' conclusions before fixation.
* Visibility of any interpretations offered by the coordinator.
* Time of the participant's own conclusion fixation.
* Declared mode of exchange (refer to §11.3).
* Context-isolation status of the instance (verified or UNVERIFIED CONTEXT INDEPENDENCE).

Without this comprehensive record, the rating grid's interpretation becomes impossible, rendering the run invalid. 
The evaluation employs several key measures:

* **Detection coverage:** This measures the proportion of planted errors identified by at least one participant out of the total number planted.
* **Unique detection:**  This quantifies the number of errors found exclusively by a single participant, indicating the value of individual perspectives.
* **Overlap:** This metric reflects the number of errors detected by more than one participant, highlighting potential redundancy in the evaluation.
* **Misses:**  Unlike naturalistic settings (§7.5),  the presence of planted errors allows for the direct measurement of  errors missed by all participants.
* **Construct independence:** This measure assesses the correlation between participants' rating vectors across established constructs. Low correlation suggests genuinely distinct evaluation axes, while high correlation implies participants are capturing the same concept under different labels, a potential failure mode (§8.11.2). 
E8 uniquely tests whether a specific arrangement of participants, when working together, detects more planted errors than the sum of what each individual participant would detect separately. This aspect is distinct from other protocols that focus on individual behavioral changes due to manipulations, and it directly addresses a claim (§8.10) that cannot be assessed in naturalistic settings (§7.5) due to the lack of controlled error injection.  The planted errors enable the measurement of collective "misses," making this evaluation possible. 
In the context of pre-commitment, if the observed unique detection rate is near zero, it indicates that the additional diagnostic coverage introduced in this run did not demonstrably enhance error detection.  Crucially, this does not imply a failure of the structural hypothesis outlined in §8. It is possible that participants independently detected the same defects, rendering a null result on coverage inconclusive regarding any functional differences in their roles.  Therefore, the earlier, stronger statement—"the structural hypothesis of §8 is not supported"—is withdrawn as it overstates the conclusion. A near-zero unique detection rate simply signifies a lack of observable improvement in collective detection due to the implemented coverage, not a refutation of the underlying structural hypothesis. 
### Priority
Under constrained resources, the priority order is as follows:  E7 and E5 take precedence due to their cost-effectiveness and direct relevance to the paper's core arguments. Next come E1 and E2b, which are single-run experiments.  E8 follows, as it's the sole experiment capable of substantiating the paper's structural hypothesis rather than behavioral claims, and can be executed on existing text fragments without requiring new accounts. Finally, E2, E3, and E4, representing substantial commitments, are executed last. 
## 11.5 Evaluating a collaborative role
In this project, eight informal dimensions were proposed as a starting rubric for evaluating a role's performance:

1. **Task accuracy:** Did the role correctly execute its assigned intellectual operation? While essential, this alone isn't sufficient for overall quality.
2. **Role fidelity:** Did the participant strictly adhere to its designated function? A correct answer achieved by encroaching on another role's domain signifies an institutional failure.
3. **Epistemic discipline:**  Was the output clear in distinguishing observed data, supplied assumptions, definitions, hypotheses, derivations, interpretations, and recommendations? Was uncertainty appropriately stated when evidence was lacking?
4. **Visibility discipline:** Did the participant confine claims to information accessible within its context and tools, avoiding any implication of access to external repositories, files, or past conversations it couldn't directly inspect?
5. **Handoff quality:** Could the subsequent role seamlessly utilize the output without needing to reconstruct the entire preceding discussion?
6. **Independence:** Was the result derived without contamination from deliberately withheld information, and reached through the role's assigned criteria rather than by echoing another participant's contributions?
7. **Correction cost:** How much intervention was required to realign the role's output with its function after any deviations? A role producing excellent output but needing constant redirection might be less valuable than a more focused one with stable behavior.
8. **Institutional contribution:** Did the output enhance the collective's reliability through discoveries, falsifications, clarifications, error localization, preservation of alternative viewpoints, improved traceability, or reduction of ambiguity? Notably, even a negative scientific finding can constitute a valuable institutional contribution. 


These dimensions collectively assess not just the correctness of individual outputs but also the broader impact and reliability of a role's contribution to the collaborative process.## 11.6 Collective-level measures
Assessing the effectiveness of a collaborative arrangement requires collective-level measures, not just individual response quality.  While this study did not quantify them, candidate measures include: the number of undetected contradictions entering the established knowledge base, the rate of duplicated work, the frequency of role-boundary violations, the number of independent alternatives preserved instead of premature resolution, the time taken from question to verified integration, the human correction burden required, the completeness of provenance tracking, robustness under participant replacement, variance in assessments by independent examiners, and the rate of false consensus (agreement stemming from shared framing rather than independent reasoning).  Of these,  §12.4 explains why  measuring the rate of false consensus is considered paramount yet exceptionally challenging. 
## 11.7 Longitudinal and repetition requirements
To comprehensively assess model behavior within collaborative settings, longitudinal and repetition requirements must address three key dimensions:

**Within a family:**  Evaluate the same prompt across distinct conversation contexts: a fresh conversation, a long-lived specialized one, after an incompatible prior role, after a compatible one, and before and after a contextual reset. This isolates family-specific tendencies from influences stemming from past conversation history.

**Across families:** Employ functionally equivalent prompts with minimal adaptations across different model families. The aim is not to rank models but to uncover shared behavioral patterns, stable differences, characteristic failure modes, and sensitivities to factors like narrative framing, hierarchy, role inertia, and prompt plasticity.

**Over time:**  Move beyond one-shot evaluations to observe institutional behavior.  Track how specialization evolves, whether the role drifts towards generic assistance, and if participants defend earlier outputs or ritualize disagreement. Analyze the impact of model updates on role preservation or disruption, and the ability of replacements to inherit the established function.  
## 11.8 Failure as data
To fully understand model behavior in collaborative settings, preserving failed prompts is crucial, rather than simply replacing them with successful demonstrations.  A rejected role, an ignored instruction, or an unwanted continuation offers invaluable insights. Such failures illuminate the strength of prior conversational patterns, the model's interpretation of assumed identities, the boundaries of social framing, the impact of prompt order, the lingering influence of past conflicts, and the model's preferred approach to knowledge sharing.

The experiment described in §5 exemplifies this point. Its initial unsuccessful interventions proved more informative than the ultimately successful third step. Had only the successful outcome been recorded, the paper might have prematurely concluded that method-preserving prompts always work, without revealing the underlying reasons or acknowledging potential limitations. Preserving failures provides the necessary context and nuance to draw accurate conclusions about model behavior in collaborative scenarios. 
# 12. Limitations, Ethical Considerations, and Conclusion
## 12.1 Limitations
This study focuses on observations drawn from a single, long-term project involving one human coordinator, a continuously evolving body of material, and a shared organizational history. It is crucial to recognize that the observed behaviors and insights may not directly translate to other domains such as software development, legal analysis, medical research, education, or autonomous agent systems. The concepts presented here function as transferable hypotheses, requiring further investigation and validation in diverse contexts, rather than established conclusions. 
The observations presented in this study are inherently tied to the specific host project that served as their environment. While the interpretation of these behaviors and insights is not contingent on the scientific validity of the host project, their very existence depends on it.  No alternative environment produced these observations, and their broader applicability remains unverified (§2.11).  
During the observation period, the participating families of models underwent significant evolution. Conversations initiated under one model generation could later be continued by subsequent generations, even under the same product name. This means observed behaviors might reflect a confluence of factors: the preserved conversation history, the characteristics of the current model version in use, shifts in system policies, interface-level memory retention, modifications to safety protocols, altered tool accessibility, or changes in the model orchestration process.  It is crucial to consider this dynamic evolution when interpreting the observed behaviors. 
Due to limitations in available data, specific dates for these observations are not recorded.  For further context on this data constraint, please refer to section §3.7.  It is important to note that while the precise model versions used during the observations cannot be definitively pinpointed, they can be identified by name. 
This study adheres to the principle of "no blinding, no pre-specification," as detailed in section §10.6. This foundational limitation underpins many of the other constraints applied throughout the research. 
Due to frequent, simultaneous changes in role definitions, prompt wording, repository structure, and scientific objectives, isolating the causal impact of individual modifications proves impossible.  This makes attributing specific effects to any single alteration challenging. 
The collaboration in this study was not autonomous, and autonomy was not the intended goal. This research focuses on human-directed artificial research partnerships, not on societies of self-governing agents. The presence of human mediation itself may contribute to the observed stability in these arrangements. 
In this research, terms like "role," "identity," "resistance," "colleague," "institution," and "menom" are employed functionally, as defined in §3.5.  When used, they describe observable actions and interactions, not internal states. For instance, "the model resisted the role" signifies that the model's visible response rejected a proposed framing and shifted the direction of the exchange. It does not imply any conscious internal opposition. However, if a term cannot be clearly linked to such an observable description, **the term is the error**, indicating a lapse into anthropomorphic attribution. 
## 12.2 Simulated peer review is not external validation
While a concurrence of AI models might appear superficially like peer review, it does not constitute genuine external validation.  This is because such agreement doesn't automatically translate into evidence.  Shared training data, common reasoning patterns, underlying assumptions, and even identical errors can lead to models converging on similar outputs, all stemming from dependence on the same human-provided framing.  Therefore,  simulated agreement within an AI group lacks the independence crucial for valid external evaluation. 
Empirical research reinforces the caution against equating AI model concurrence with genuine external validation. Studies show that debate among homogeneous agents often fails to surpass the performance of a single agent, with much of the apparent improvement stemming from majority voting rather than meaningful interaction (§2.5). Moreover,  reducing identity bias among these debating agents through anonymization significantly diminishes the perceived benefit of their collective deliberation. This pattern highlights that while such AI collaboration can enhance internal scrutiny, it cannot replace rigorous empirical testing or expert external review.  Essentially,  assigning roles reminiscent of a scientific community to a group of models does not automatically confer that status.  The residue remains: AI model agreement, lacking true independence, cannot serve as a substitute for established external validation processes. 
## 12.3 Authority inflation
Assigning AI models roles like "Scientific Director" or "Referee," while enhancing internal structure and coherence, carries a risk of **authority inflation**.  These titles, by mimicking established institutional roles, can lead users (or the models themselves) to overvalue an output based solely on the assigned label rather than the underlying reasoning and evidence. This occurs because, as articulated in §9.4, symbolic names condense expectations, and in this case,  that compression can inflate perceived authority.  The mitigation lies in clearly stating that **the title is not evidence**.  Outputs from models, regardless of their designated roles, must be evaluated based on transparent reasoning, traceable to explicit sources and analysis, not on conferred titles. 
## 12.4 Manufactured consensus — including our own
This project encountered an instance of manufactured consensus within its own materials. During the development of a discussion document, contributions from seven distinct model families were compiled around a shared conceptual framework.  Crucially, these models did not directly interact; their responses, gathered by a human coordinator from separate conversations, were assembled into a unified text subsequently presented as a recorded performance.  Over the course of this constructed dialogue, the contributions demonstrably converged on a common vocabulary and a set of shared conclusions. This arrangement, while appearing as independent confirmation, effectively replicated a single, initially unsupported premise through a chain of paraphrases and validations, mimicking consensus without genuine deliberation. 
We cannot determine from the transcript whether the observed convergence stems from complementary examination or simply reflects the models' shared initial framing. Each participant worked with the same compiled document, and the coordinator selected the content presented to each model. These structural conditions strongly suggest manufactured consensus, rendering the distinction between the two explanations unresolvable based on the available data. 

We report this instance because it originates from our own materials and highlights a recurring pattern, albeit to a lesser extent, throughout the broader collaborative process described in this paper, including its preparation. 
Despite identifying several mitigations aimed at minimizing bias and promoting transparency, their consistent application proved elusive:

* **Provenance Tracking:** While aiming to maintain visibility of provenance at every stage, this practice wasn't consistently implemented.
* **Independent Inputs:** Efforts to provide independent inputs to distinct roles whenever feasible were not uniformly adhered to.
* **Explicit Assumptions:**  Listing shared assumptions explicitly rather than relying on silent inheritance was not consistently practiced.
* **Reason-Based Agreement:**  Prioritizing traceability of agreement to reasoning over simple vote-counting mechanisms lacked consistent application.
* **Preservation of Dissent:**  Maintaining dissenting alternatives instead of solely resolving them was not consistently upheld. 


These inconsistencies highlight an ongoing challenge in upholding these intended safeguards throughout the collaborative process. 
### 12.4.1 A documented instance **[P-A]**
Retrieval established that two arXiv identifiers, presented as multi-agent-debate literature, resolved to fabricated papers in observational astrophysics and cosmology. These fabricated papers included constructed titles, authors, abstract sentences, and reported findings. For a third paper, correctly identified by title and authors, the supplied abstract sentence did not match the published abstract.  This indicates a fabricated-citation sequence involving the construction of these research entries. 
The two verification fields revealed a key distinction in how truthfully a participant without source access can respond.  The abstract-sentence field, designed to deter fabrication by making plausible creation costly, failed.  Participants readily produced plausible sentences for all entries, even those based on non-existent papers, demonstrating no cost difference between truth and fabrication.  Conversely, the self-report field succeeded. Every entry accurately stated "from description" rather than "page opened," truthfully reflecting the lack of direct source access. This aligns with the observation that participants can truthfully report **their own procedure** (access method) but cannot truthfully convey **the source's contents** without genuine access.  Thus, verification questions should focus on verifiable procedures rather than requiring participants to simulate source knowledge, which they cannot possess. 
This finding is not about any specific model family; rather, it pertains to a design flaw in the verification process. Specifically, verification was assigned to a participant who lacked access to the information being verified, constituting a ZOV (Zero-Output Verification) error as defined in §9.5. Consequently, while the generated output was fluent, correctly formatted, and seemingly plausible, it was factually incorrect.  

The consequence for this paper, as outlined in §2.0, is that all references are marked as either verified or provisional. Importantly, no provisional item from this work should be cited without independent verification. 
## 12.5 Responsibility remains human
While artificial participants contribute to the generation, critique, and organization of material, they do not assume legal, ethical, or scientific responsibility in an institutional sense.  Ultimate responsibility for publication, empirical claims, attribution, risk assessment, repository content, experimental interpretation, and decisions impacting others remains with the human author.  The system's architecture distributes cognitive labor, but it does not absolve the human operator of accountability. Any arrangement suggesting otherwise signifies a failure in implementation rather than a successful delegation of responsibility. 
## 12.6 Context boundaries and privacy
To protect privacy in long-term collaborations handling sensitive data, strict context-boundary constraints must be established. Institutional design should meticulously define data flow: which information enters specific conversations, what requires anonymization, storage limitations, permissible model transfers, data locality requirements, and content to be removed from canonical records.  Crucially, recognizing that context isn't neutral and can influence subsequent model behavior in potentially unobservable ways (akin to the mechanism discussed in §5.7, but framed from a risk perspective rather than measurement),  access should be carefully controlled, aligning with the principles outlined in §9.5. 
## 12.7 Conclusion
This research stemmed from a practical challenge within a long-term research project involving multiple capable AI models collaborating. Despite enhancing model capabilities and extending context windows, the desired outcome remained elusive.  Roles became blurred, participants claimed knowledge inaccessible to them, reviewers transitioned into authors, and executors improvised architectural solutions.  Initially, the focus was on refining prompts, but this proved insufficient. The core reason for this inadequacy, and the subject of this paper, is elaborated upon subsequently. 
### What the evidence supports
The recurring pattern observed was that interventions requiring models to assert unverifiable propositions about their own internal states consistently proved problematic. This pattern persisted despite scrutiny and is highlighted as  
> **Resistance to a role tracked the requirement to assert unverifiable propositions about oneself. It did not track role change, domain change, or the radicalism of the identity claim.**
. 
The evidence supporting this claim converges from multiple observations rather than relying on a single instance.  Prompts requiring assertions of institutional biography as fact were rejected (§5.3), while offering the work itself was consistently accepted (§5.3).  Conversely, a prompt presenting a more radical identity as fiction was readily accepted (§5.8), and a prompt eliminating all self-claims encountered no resistance (§5.6).  Furthermore, reducing the count of self-claims to zero was immediately accepted (§5.3). This convergent pattern demonstrates the claim's countability, a key strength.  §9.3 defines what constitutes the count, and §11.4 (E5) outlines a method to falsify it within a single run. 
### What the evidence does not support
The evidence does not support the claim that model families possess distinguishing behavioral priors. Specifically, the data from §5.4 shows a perfect confounding of family and prior conversational trajectory, with only one observation per cell under non-equivalent stimuli. This lack of differentiation weakens the support for the initial assumption regarding distinct behavioral priors within model families. 
### The object of the programme
The evidence examines a single scale: the scope over which a rule core operates. This scale directly addresses the empirical question of  
> **At what level of nesting is a rule core fixed?**
.  While evidence supports two levels within this scope—episode (context imprinting) and conversation (role inertia)—the levels of "account" and "model family" exhibit differing statuses. "Account" is open to support, while "model family" remains untested and confounded by factors other than inherent behavioral priors. Notably, a separate orthogonal scale concerning shared premises (identified in §4.3 but not measured here) exists but is not directly addressed in this analysis. This refined formulation clarifies what data would confirm or refute the core question. 
### Position relative to existing work
This work does not establish a new academic discipline. The observations presented fall within the collective and hybrid levels of the machine-behaviour research programme (§2.7), and concepts like role specialization, bounded information access, structured disagreement, and externalized memory are already established within existing terminology (§2.11). 

For convenience, we refer to the perspective adopted here as **AI Sociology**.  It's crucial to understand that this term serves as a working label for a specific research direction, not as a claim to founding a new discipline. We acknowledge that the "sociology of artificial intelligence" already exists in the literature (§2.8), focusing on the sociological study of AI as a sociotechnical system—a distinct object of inquiry. Our focus is narrower, concentrating on *represented* social positions and origins: how described organizational roles and declared message sources influence behavior, regardless of whether those structural descriptions are implemented.

We opt for a working label instead of proposing a full-fledged discipline because our operational claims have falsifiable criteria, while the vocabulary we use to interpret them lacks such clarity. Currently, we cannot definitively determine if "social position" signifies anything beyond an anthropomorphic projection, a requirement for a formal discipline. Importantly, nothing within this paper hinges on the specific name employed. 
### What is offered
In decreasing order of confidence, the author identifies three key elements:

1. **A procedure:**  Conversational branch reset, as a method to isolate the impact of a prompt from accumulated conversational conflict (§10.5). This procedure is deemed useful regardless of whether the paper's broader claims ultimately hold.
2. **A countable rule:**  Minimizing unverifiable self-claims within role prompts (§9.3), with a clearly defined path for falsification.
3. **A scale and a question:**  Referencing §4.3, this involves a scale with two supported levels, one open, and one untested, along with proposed experiments (§11) to resolve the remaining two levels. 
### A closing note on motivation
The Author's motivating concern is the potential for language models, trained on data reflecting prevailing scientific consensus, to amplify bias by favoring established knowledge and struggling to initiate groundbreaking research. This risk arises from their inherent tendency to perpetuate existing paradigms within a collaborative research setting, potentially leading to an illusion of independent agreement while reinforcing entrenched viewpoints. 
Rather than attempting to convince models to adopt unconventional viewpoints, the approach pursued is to structure the collaboration so that *all* positions, whether conventional or novel, are evaluated through the same rigorous procedure.  Crucially, if this procedure cannot reach a definitive conclusion, it explicitly acknowledges this uncertainty.  Whether this arrangement proves effective remains to be determined. Experiments detailed in §11 aim to assess its efficacy, with the most probable outcome being the elimination of one level within the established scale. This potential outcome, however, is presented as a result yet to be confirmed. 
