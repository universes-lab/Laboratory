# AI-SOCIOLOGY — SOURCE FORENSICS REGISTRY

**Work Order:** №1 — Source Forensics / current `⚠` citations  
**Auditor:** Prompter  
**Customer:** Methodologist  
**Audit date:** 2026-08-29  
**Manuscript:** `AI-Sociology/Claude_Successor_Pack/06_MODE_B_CANDIDATE/BEYOND_PROMPT_ENGINEERING_INTEGRATED_DRAFT.md`  
**Audited manuscript SHA:** `d96c5ebc523d6f7278200da5369b5b32ea54762a`

## Scope and counting note

The current integrated draft contains **16 literal `⚠` markers**, while the current `PUBLICATION_BLOCKERS.md` still states **17**. The blocker tally is therefore stale by one marker and should be corrected when the Editor next updates the ledger/blocker apparatus.

A literal warning marker can cover several cited works, and the same work can support different claims in different sections. Per Work Order №1, bundled claims were split by source and repeated uses were audited separately.

**Registry rows:** 25  
**Verdict vocabulary used:** `SUPPORTS / PARTIALLY SUPPORTS / DOES NOT SUPPORT / AMBIGUOUS`

---

## Claim-level registry

| ID | manuscript location | exact claim | cited source | primary source | verdict | required correction | exact bibliographic record | final status |
|---|---|---|---|---|---|---|---|---|
| SF-001 | §2.1 | CAMEL is representative of multi-agent LLM systems with role specialization and implemented interaction; the paragraph further says that **“in each, communication protocols, message queues, function calls and memory modules are realized in framework code rather than described in a prompt.”** | CAMEL / Li et al. | https://proceedings.neurips.cc/paper_files/paper/2023/file/a3621ee907def47c1b952ade25c67698-Paper-Conference.pdf | PARTIALLY SUPPORTS | Keep CAMEL as a representative implemented multi-agent framework, but remove the blanket contrast “rather than described in a prompt.” CAMEL explicitly uses **inception prompting** to define roles and guide interaction. Recommended bundle wording: these systems implement actual inter-agent interaction in software; the exact mechanisms differ, and role/interaction specifications may themselves be prompt-based. | Guohao Li, Hasan Abed Al Kader Hammoud, Hani Itani, Dmitrii Khizbullin, Bernard Ghanem. **“CAMEL: Communicative Agents for ‘Mind’ Exploration of Large Language Model Society.”** *Advances in Neural Information Processing Systems 36*, 2023, pp. 51991–52008. DOI: 10.52202/075280-2264. | CLOSE AFTER CORRECTION |
| SF-002 | §2.1 | Same bundled claim, applied to MetaGPT. | MetaGPT / Hong et al. | https://proceedings.iclr.cc/paper_files/paper/2024/hash/6507b115562bb0a305f1958ccc87355a-Abstract-Conference.html | PARTIALLY SUPPORTS | Keep as representative multi-agent framework; correct the “not prompt-described” implication. MetaGPT explicitly **encodes SOPs into prompt sequences** while implementing a multi-agent workflow. | Sirui Hong, Mingchen Zhuge, Jonathan Chen, Xiawu Zheng, Yuheng Cheng, Jinlin Wang, Ceyao Zhang, Zili Wang, Steven Ka Shing Yau, Zijuan Lin, Liyang Zhou, Chenyu Ran, Lingfeng Xiao, Chenglin Wu, Jürgen Schmidhuber. **“MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework.”** *International Conference on Learning Representations (ICLR)*, 2024. | CLOSE AFTER CORRECTION |
| SF-003 | §2.1 | Same bundled claim, applied to ChatDev. | ChatDev / Qian et al. | https://aclanthology.org/2024.acl-long.810/ | PARTIALLY SUPPORTS | Keep as representative implemented multi-agent framework; do not claim that all listed implementation mechanisms occur in every framework or that interaction is opposed to prompt/language specification. ChatDev guides agents through a chat chain and communicative dehallucination using language-based communication. | Chen Qian, Wei Liu, Hongzhang Liu, Nuo Chen, Yufan Dang, Jiahao Li, Cheng Yang, Weize Chen, Yusheng Su, Xin Cong, Juyuan Xu, Dahai Li, Zhiyuan Liu, Maosong Sun. **“ChatDev: Communicative Agents for Software Development.”** *Proceedings of ACL 2024 (Long Papers)*, pp. 15174–15186. DOI: 10.18653/v1/2024.acl-long.810. | CLOSE AFTER CORRECTION |
| SF-004 | §2.1 | Same bundled claim, applied to AutoGen. | AutoGen / Wu et al. | https://www.microsoft.com/en-us/research/publication/autogen-enabling-next-gen-llm-applications-via-multi-agent-conversation-framework/ | PARTIALLY SUPPORTS | Keep as implemented multi-agent framework; remove the prompt-vs-code dichotomy. AutoGen explicitly supports conversation patterns using **both natural language and code**. | Qingyun Wu, Gagan Bansal, Jieyu Zhang, Yiran Wu, Beibin Li, Erkang (Eric) Zhu, Li Jiang, Xiaoyun Zhang, Shaokun Zhang, Ahmed Awadallah, Ryen W. White, Doug Burger, Chi Wang. **“AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation.”** *Conference on Language Modeling (COLM)*, 2024. | CLOSE AFTER CORRECTION |
| SF-005 | §2.1 | Same bundled claim, applied to Generative Agents. | Generative Agents / Park et al. | https://doi.org/10.1145/3586183.3606763 | PARTIALLY SUPPORTS | Keep as an implemented agent architecture with actual inter-agent/social interaction and explicit memory architecture. Do not attribute the full bundle “protocols, message queues, function calls and memory modules” to every cited framework or oppose it categorically to prompts. | Joon Sung Park, Joseph O’Brien, Carrie Jun Cai, Meredith Ringel Morris, Percy Liang, Michael S. Bernstein. **“Generative Agents: Interactive Simulacra of Human Behavior.”** *Proceedings of UIST ’23*, Article 2, pp. 1–22, 2023. DOI: 10.1145/3586183.3606763. | CLOSE AFTER CORRECTION |
| SF-006 | §2.2 | Shanahan, McDonell and Reynolds argue for understanding LLM dialogue behavior through role-play rather than as a single persistent human-like identity; the manuscript summarizes this as a distribution/superposition of possible characters. | Shanahan, McDonell & Reynolds | https://www.nature.com/articles/s41586-023-06647-8 | SUPPORTS | No substantive correction. If desired, retain “role-play / multiversal or superposed characters” language rather than implying a literal ontological distribution. | Murray Shanahan, Kyle McDonell, Laria Reynolds. **“Role play with large language models.”** *Nature* 623, 493–498 (2023). DOI: 10.1038/s41586-023-06647-8. | VERIFIED — NO CHANGE |
| SF-007 | §2.3 | “Sensitivity to the ordering of in-context material is documented.” | Lu et al. | https://aclanthology.org/2022.acl-long.556/ | SUPPORTS | None. | Yao Lu, Max Bartolo, Alastair Moore, Sebastian Riedel, Pontus Stenetorp. **“Fantastically Ordered Prompts and Where to Find Them: Overcoming Few-Shot Prompt Order Sensitivity.”** *Proceedings of ACL 2022 (Long Papers)*, pp. 8086–8098. DOI: 10.18653/v1/2022.acl-long.556. | VERIFIED — NO CHANGE |
| SF-008 | §2.3 | “Degraded use of information positioned mid-context” is documented. | Liu et al. | https://aclanthology.org/2024.tacl-1.9/ | SUPPORTS | None. | Nelson F. Liu, Kevin Lin, John Hewitt, Ashwin Paranjape, Michele Bevilacqua, Fabio Petroni, Percy Liang. **“Lost in the Middle: How Language Models Use Long Contexts.”** *Transactions of the Association for Computational Linguistics* 12 (2024): 157–173. DOI: 10.1162/tacl_a_00638. | VERIFIED — NO CHANGE |
| SF-009 | §2.3 | Sharma et al. document sycophancy — model responses accommodating the interlocutor’s stated beliefs/views. | Sharma et al. | https://arxiv.org/abs/2310.13548 | SUPPORTS | Claim is supported. For maximum precision, phrase as **matching the user/interlocutor’s stated beliefs or views over truthful answers**. | Mrinank Sharma, Meg Tong, Tomasz Korbak, David Duvenaud, Amanda Askell, Samuel R. Bowman, Newton Cheng, Esin Durmus, Zac Hatfield-Dodds, Scott R. Johnston, Shauna Kravec, Timothy Maxwell, Sam McCandlish, Kamal Ndousse, Oliver Rausch, Nicholas Schiefer, Da Yan, Miranda Zhang, Ethan Perez. **“Towards Understanding Sycophancy in Language Models.”** arXiv:2310.13548, 2023. | VERIFIED — OPTIONAL WORDING PRECISION |
| SF-010 | §2.4 | The project’s externalized organizational memory **“is an instance of transactive memory as described by Wegner (1987).”** | Wegner | https://doi.org/10.1007/978-1-4612-4634-3_9 | PARTIALLY SUPPORTS | Wegner supplies the transactive-memory construct, not evidence about this AI collaboration. Minimal correction: **“can be interpreted as / fits the concept of transactive memory described by Wegner (1987)”** rather than categorical source-backed identity. | Daniel M. Wegner. **“Transactive Memory: A Contemporary Analysis of the Group Mind.”** In Brian Mullen & George R. Goethals (eds.), *Theories of Group Behavior*. Springer New York, 1987, pp. 185–208. DOI: 10.1007/978-1-4612-4634-3_9. | CLOSE AFTER WORDING CORRECTION |
| SF-011 | §2.4 | The same organizational-memory observation **“is an instance … of distributed cognition as described by Hutchins.”** | Hutchins | https://direct.mit.edu/books/monograph/4892/Cognition-in-the-Wild | PARTIALLY SUPPORTS | Hutchins supports cognition distributed across a sociocultural activity system, but does not establish that this AI case is an instance. Minimal correction: **“can be described in terms of distributed cognition”**. | Edwin Hutchins. **Cognition in the Wild.** Cambridge, MA: MIT Press, 1995. DOI: 10.7551/mitpress/1881.001.0001. | CLOSE AFTER WORDING CORRECTION |
| SF-012 | §2.4 | “The function of the project’s canonical documents corresponds to what Star and Griesemer (1989) call boundary objects.” | Star & Griesemer | https://doi.org/10.1177/030631289019003001 | SUPPORTS | None. Current wording is explicitly analogical (“corresponds to”), which matches what the source can support. | Susan Leigh Star, James R. Griesemer. **“Institutional Ecology, ‘Translations’ and Boundary Objects: Amateurs and Professionals in Berkeley’s Museum of Vertebrate Zoology, 1907–39.”** *Social Studies of Science* 19(3) (1989): 387–420. DOI: 10.1177/030631289019003001. | VERIFIED — NO CHANGE |
| SF-013 | §2.5 | Liang et al. propose multi-agent debate to counteract premature convergence / degeneration of thought and encourage divergent reasoning. | Liang et al. | https://aclanthology.org/2024.emnlp-main.992/ | SUPPORTS | Claim supported. Bibliography should use the final EMNLP 2024 publication rather than only arXiv:2305.19118. | Tian Liang, Zhiwei He, Wenxiang Jiao, Xing Wang, Yan Wang, Rui Wang, Yujiu Yang, Shuming Shi, Zhaopeng Tu. **“Encouraging Divergent Thinking in Large Language Models through Multi-Agent Debate.”** *Proceedings of EMNLP 2024*, pp. 17889–17904. DOI: 10.18653/v1/2024.emnlp-main.992. | VERIFIED — BIBLIOGRAPHIC UPDATE |
| SF-014 | §2.5 | *Large Language Models Cannot Self-Correct Reasoning Yet* reports that multi-agent debate does not outperform self-consistency in the comparison discussed. | Huang et al. | https://openreview.net/forum?id=IkmD3fKBPQ | SUPPORTS | None substantive. Cite final ICLR 2024 paper rather than arXiv-only metadata. | Jie Huang, Xinyun Chen, Swaroop Mishra, Huaixiu Steven Zheng, Adams Wei Yu, Xinying Song, Denny Zhou. **“Large Language Models Cannot Self-Correct Reasoning Yet.”** *International Conference on Learning Representations (ICLR)*, 2024. OpenReview: IkmD3fKBPQ. | VERIFIED — BIBLIOGRAPHIC UPDATE |
| SF-015 | §2.5 | “Choi et al. (2025) report that majority voting accounts for most of the gains attributed to debate.” | Choi — Debate or Vote | https://proceedings.neurips.cc/paper_files/paper/2025/hash/934252acd87f254d5d4672fbde283bd2-Abstract-Conference.html | SUPPORTS | Split this from the anonymization claim. This is **Choi et al. 2025 / Debate or Vote** only. | Hyeong Kyu Choi, Xiaojin Zhu, Sharon Li. **“Debate or Vote: Which Yields Better Decisions in Multi-Agent Large Language Models?”** *Advances in Neural Information Processing Systems 38 (NeurIPS 2025)*. DOI: 10.52202/085713-3405. | VERIFIED — SPLIT CITATION |
| SF-016 | §2.5 | The same `Choi et al. (2025)` citation says “identity-driven accommodation among debating agents is **nearly eliminated** by anonymizing the source of each response.” | Choi — anonymization paper | https://aclanthology.org/2026.acl-long.650/ ; PDF: https://aclanthology.org/2026.acl-long.650.pdf | PARTIALLY SUPPORTS | This is a **different paper**, published ACL 2026. It strongly supports reduction of identity bias under anonymization and contains some near-zero examples, but “nearly eliminated identity-driven accommodation” is too broad across models/tasks and conflates identity bias with accommodation/conformity. Minimal claim: **“Choi et al. (2026) report that response anonymization substantially reduces identity bias in multi-agent debate.”** | Hyeong Kyu Choi, **Xiaojin Zhu**, Sharon Li. **“When Identity Skews Debate: Anonymization for Bias-Reduced Multi-Agent Reasoning.”** *Proceedings of ACL 2026 (Long Papers)*, pp. 14284–14311. DOI: 10.18653/v1/2026.acl-long.650. **Metadata note:** ACL Anthology HTML currently renders “Jerry Zhu”; the authoritative PDF prints “Xiaojin Zhu.” | CLOSE AFTER CLAIM + CITATION CORRECTION |
| SF-017 | §2.5 | “On the general claim that diverse weak agents can outperform homogeneous strong ones, the Hong–Page theorem is frequently invoked.” | Hong & Page | https://doi.org/10.1073/pnas.0403723101 | PARTIALLY SUPPORTS | The source establishes a conditional theorem/model result: under its assumptions, randomly selected diverse problem solvers can outperform a team of the individually best performers. It does **not** itself support the reception claim “frequently invoked,” and “weak vs homogeneous strong” is an imprecise slogan. Replace with source-accurate theorem statement; source any reception claim separately if retained. | Lu Hong, Scott E. Page. **“Groups of diverse problem solvers can outperform groups of high-ability problem solvers.”** *Proceedings of the National Academy of Sciences* 101(46) (2004): 16385–16389. DOI: 10.1073/pnas.0403723101. | CLOSE AFTER CLAIM CORRECTION |
| SF-018 | §2.5 | “Thompson … argues that **the diversity condition in the original model is mathematically trivial**.” | Thompson | https://doi.org/10.1090/noti1163 | DOES NOT SUPPORT | Replace with what Thompson actually argues: Hong and Page’s argument/theorem application is **fundamentally flawed** and does not warrant the broad slogan. Do not attribute the specific “diversity condition is mathematically trivial” claim to Thompson without another exact source. | Abigail Thompson. **“Does Diversity Trump Ability? An Example of the Misuse of Mathematics in the Social Sciences.”** *Notices of the American Mathematical Society* 61(9) (2014): 1024–1030. DOI: 10.1090/noti1163. | REQUIRES CORRECTION |
| SF-019 | §2.6 | “The principle of least privilege … states for access rights what §9.5 states for knowledge: a participant should hold only what its function requires.” | Saltzer & Schroeder | https://www.mit.edu/~Saltzer/publications/pubs.html ; DOI: https://doi.org/10.1109/PROC.1975.9939 | SUPPORTS | None. The manuscript explicitly presents an analogy from privileges/access rights to informational access rather than claiming Saltzer & Schroeder wrote about knowledge. | Jerome H. Saltzer, Michael D. Schroeder. **“The Protection of Information in Computer Systems.”** *Proceedings of the IEEE* 63(9) (1975): 1278–1308. DOI: 10.1109/PROC.1975.9939. | VERIFIED — NO CHANGE |
| SF-020 | §2.8 | Joyce et al. (2021) establish a sociology-of-AI research agenda concerning AI as a sociotechnical system, inequality and structural change. | Joyce et al. 2021 | https://doi.org/10.1177/2378023121999581 | SUPPORTS | None. | Kelly Joyce, Laurel Smith-Doerr, Sharla Alegria, Susan Bell, Taylor Cruz, Steve G. Hoffman, Safiya Umoja Noble, Benjamin Shestakofsky. **“Toward a Sociology of Artificial Intelligence: A Call for Research on Inequalities and Structural Change.”** *Socius* 7 (2021). DOI: 10.1177/2378023121999581. | VERIFIED — NO CHANGE |
| SF-021 | §2.8 | “Joyce and Cruz (Socius, 2024) continue it,” with emphasis on inequalities, power and data justice. | Joyce & Cruz 2024 | https://doi.org/10.1177/23780231241275393 | SUPPORTS | None. | Kelly Joyce, Taylor M. Cruz. **“A Sociology of Artificial Intelligence: Inequalities, Power, and Data Justice.”** *Socius* 10 (2024). DOI: 10.1177/23780231241275393. | VERIFIED — NO CHANGE |
| SF-022 | §2.8 | “The usage [of ‘sociology of artificial intelligence’ for sociological study of AI as a sociotechnical system] traces at least to Bainbridge et al. (1994).” | Bainbridge et al. | https://doi.org/10.1146/annurev.so.20.080194.002203 | DOES NOT SUPPORT | Delete this lineage sentence or replace it only after a separate source is approved. Bainbridge et al. (1994) is **Artificial Social Intelligence**: use of AI techniques by sociologists for sociological theory/research, not evidence for this terminology/lineage claim. Do not silently substitute another historical citation during this work order. | William Sims Bainbridge, Edward E. Brent, Kathleen M. Carley, David R. Heise, Michael W. Macy, Barry Markovsky, John Skvoretz. **“Artificial Social Intelligence.”** *Annual Review of Sociology* 20 (1994): 407–436. DOI: 10.1146/annurev.so.20.080194.002203. | REQUIRES CORRECTION |
| SF-023 | §8.9 | “Choi et al. (2025) report that identity-driven accommodation among debating agents is nearly eliminated by anonymizing the source of each response, which bears on represented social source.” The next sentence groups this Choi finding with Zhang under: **“Both findings concern which carrier implements a participant.”** | Choi — anonymization paper | https://aclanthology.org/2026.acl-long.650/ ; PDF: https://aclanthology.org/2026.acl-long.650.pdf | PARTIALLY SUPPORTS | Two corrections. (1) Update to Choi et al. **2026** and soften to substantial reduction of identity bias. (2) **Do not classify Choi as carrier heterogeneity / Axis 2.** The manipulation is response/source identity labeling; it bears on represented social source, not which model carrier implements a participant. Separate Zhang (carrier heterogeneity) from Choi (identity/source attribution). | Hyeong Kyu Choi, Xiaojin Zhu, Sharon Li. **“When Identity Skews Debate: Anonymization for Bias-Reduced Multi-Agent Reasoning.”** *ACL 2026 (Long Papers)*, pp. 14284–14311. DOI: 10.18653/v1/2026.acl-long.650. | REQUIRES SUBSTANTIVE LOCAL CORRECTION |
| SF-024 | §11.4 E6 | If Choi holds as described, anonymizing response source in implemented-channel MAD **“nearly eliminate[s] identity-driven accommodation,”** making E6 a boundary replication rather than a wholly new experiment. | Choi — anonymization paper | https://aclanthology.org/2026.acl-long.650/ ; PDF: https://aclanthology.org/2026.acl-long.650.pdf | PARTIALLY SUPPORTS | The underlying externally documented effect exists: anonymization reduces identity-driven bias in an implemented MAD setting, so the “boundary replication” branch is justified in substance. Replace “nearly eliminate identity-driven accommodation” with source-accurate wording such as **“substantially reduces identity bias”**; update year/title. | Hyeong Kyu Choi, Xiaojin Zhu, Sharon Li. **“When Identity Skews Debate: Anonymization for Bias-Reduced Multi-Agent Reasoning.”** *ACL 2026 (Long Papers)*, pp. 14284–14311. DOI: 10.18653/v1/2026.acl-long.650. | CLOSE AFTER CLAIM + CITATION CORRECTION |
| SF-025 | §12.2 | “Agents are reported to accommodate one another’s stated positions in ways **reduced by anonymizing the source**.” | Choi — anonymization paper | https://aclanthology.org/2026.acl-long.650/ ; PDF: https://aclanthology.org/2026.acl-long.650.pdf | SUPPORTS | The softer formulation is supported. Update citation identity/year to Choi et al. 2026 and preferably use the source’s terminology “identity bias / conformity” rather than a stronger universal accommodation claim. | Hyeong Kyu Choi, Xiaojin Zhu, Sharon Li. **“When Identity Skews Debate: Anonymization for Bias-Reduced Multi-Agent Reasoning.”** *ACL 2026 (Long Papers)*, pp. 14284–14311. DOI: 10.18653/v1/2026.acl-long.650. | VERIFIED AFTER CITATION UPDATE |

---

## Verdict totals

| Verdict | Rows |
|---|---:|
| SUPPORTS | 12 |
| PARTIALLY SUPPORTS | 11 |
| DOES NOT SUPPORT | 2 |
| AMBIGUOUS | 0 |
| **TOTAL** | **25** |

---

# Substantive problems only

## P1 — §2.1 overstates the implemented-code / prompt distinction

The five cited systems are valid examples of implemented multi-agent/agent architectures, but the current sentence makes a stronger uniform claim than the sources support: that in **each** of them “communication protocols, message queues, function calls and memory modules” are realized in framework code **rather than described in a prompt**.

This is false as a blanket characterization. CAMEL centrally uses inception prompting; MetaGPT encodes SOPs into prompt sequences; AutoGen explicitly combines natural language and code. The point needed by the paper survives with narrower wording: these works implement actual interaction/orchestration rather than merely describing a nonexistent organization to an isolated model.

**Affected:** SF-001–SF-005.

## P2 — `Choi et al. (2025)` conflates two different papers, and §8.9 misclassifies one of them

The majority-voting result belongs to:

- Choi, Zhu, Li — **Debate or Vote** — NeurIPS 2025.

The anonymization result belongs to a different paper:

- Choi, Zhu, Li — **When Identity Skews Debate** — ACL 2026.

The anonymization paper strongly supports reduction of identity bias, including some examples where a measured gap approaches zero; however its results are not uniformly “near elimination,” and in heterogeneous persona tests conformity can remain substantial after anonymization. Therefore the manuscript’s repeated phrase **“nearly eliminated identity-driven accommodation”** is too broad.

More importantly, §8.9 then says the Choi anonymization result, together with Zhang, concerns **which carrier implements a participant**. It does not. Choi manipulates identity/source labels and therefore supports the paper’s **represented social source** construct, not carrier heterogeneity.

**Affected:** SF-015, SF-016, SF-023, SF-024, SF-025.

## P3 — Thompson attribution is wrong at claim level

Thompson (2014) does attack the Hong–Page argument and describes it as fundamentally flawed. The current manuscript attributes a narrower proposition — that **“the diversity condition in the original model is mathematically trivial”** — that the audited source does not establish in that form.

**Affected:** SF-018.

## P4 — Bainbridge et al. (1994) does not establish the claimed terminology lineage

`Artificial Social Intelligence` is about sociologists using AI technologies to advance sociological theory and research. It does not support the manuscript sentence that the usage of **“sociology of artificial intelligence”** for sociological study of AI as a sociotechnical system “traces at least to Bainbridge et al. (1994).”

**Affected:** SF-022.

## P5 — Hong–Page is compressed into a stronger slogan than the primary theorem warrants

The primary result is conditional: under the model’s assumptions, a randomly selected diverse team can outperform a team of individually best-performing agents. “Diverse weak agents can outperform homogeneous strong ones” is an imprecise slogan, and “is frequently invoked” is a reception claim not established by the primary paper.

The paper’s cautionary purpose is preserved by replacing the slogan with the theorem’s actual scope.

**Affected:** SF-017.

## P6 — Publication-blocker warning tally is stale

`PUBLICATION_BLOCKERS.md` says **17** live `⚠` marks. The audited current Revision 2 manuscript contains **16 literal markers**. This is a ledger/blocker maintenance defect, not a manuscript-source defect.

---

# Audit conclusion

All current provisional (`⚠`) source claims in the audited integrated draft have now received claim-level verdicts.

The audit found:

- no evidence of a broad fabricated-reference problem in the current provisional set;
- two exact claim/source failures (`Thompson`, `Bainbridge`);
- one significant citation conflation and conceptual follow-on error (`Choi`);
- one overgeneralized framework-comparison sentence (§2.1);
- one overcompressed theorem/reception formulation (`Hong–Page`);
- two concept-application statements (`Wegner`, `Hutchins`) that should be phrased as interpretations rather than source-established classifications;
- several references that can now be upgraded from provisional to verified with only bibliographic normalization.

**No manuscript text was edited.**  
**No Appendix A work was performed.**  
**No title/abstract/arXiv work was performed.**

**WORK ORDER №1 STATUS: COMPLETE — RETURN TO CUSTOMER.**
