# PUBLICATION HANDOFF — ARXIV + ZENODO

**FROM:** Author / Shogun + Chief Integrator  
**TO:** Git-Master  
**DATE:** 2026-10-15  
**TASK:** carry both publication objects through registration, packaging, permanent identifiers, cross-linking, and publication

This is an execution / publication task. Do not reopen scientific or literary editing.

# 1. arXiv — research article

Publication object:

`AI-Sociology/AI_SOCIOLOGY_ARXIV_PREFLIGHT_2026-10-13`

Title:

**Beyond Prompt Engineering: Role Reconfiguration in Long-Lived AI Conversations**

Author metadata:

**V. Krasnianskyi**

Planned categories:

- primary: **cs.MA**
- cross-list: **cs.HC**

Account identity must use the Author's real name. arXiv is independent from the GitHub identity.

## Article rules

- Use the current final publication source, not an older cached PDF/source bundle blindly.
- The scientific/editing phase is CLOSED.
- Appendix A is not to be reconstructed from memory. The real HDD D: failure destroyed part of the primary local material. Any missing items are to be marked **NOT PRESERVED** according to the Author's decision.
- If the existing tar/PDF predates the Integrator's final source corrections, rebuild the package mechanically from the current sources before submission; do not edit prose.
- Keep AI participants as contribution disclosure, not metadata authors.
- Proposed article license remains **CC BY 4.0**, subject to final Author confirmation in the arXiv UI.
- If endorsement is required for cs.MA, stop and return the endorsement status/link requirements to the Author. Do not improvise another category merely to bypass endorsement.

## arXiv cross-link

Once the Zenodo DOI for the companion book is reserved, put in arXiv Comments:

> Companion documentary volume: A. Tuin, *Chronicles of the Prompter*, Zenodo DOI: <DOI>.

Do not submit until this DOI is known unless the Author explicitly orders article-first publication.

# 2. Zenodo — documentary book

Publication object:

`AI-Sociology_Other/Chronicles_of_Prompter`

Register/sign in through GitHub OAuth if convenient.

Creator:

- type: Person
- given name: **A.**
- family name: **Tuin**

Resource type:

**Publication → Book / Monograph** (closest available subtype)

Title:

**Chronicles of the Prompter**

Alternative titles in Description:

**Хроники Промптера**  
**Kronieken van de Prompter**

Before publishing:

1. create the Zenodo draft;
2. reserve the DOI;
3. return the reserved DOI to the Author / Integrator;
4. do **not** press Publish until the final cover and PDF package are present;
5. add the documentary supplements and parallel-work links listed in `CHRONICLES_PUBLICATION_MANIFEST_2026-10-15.md`;
6. retain the two original Russian DOCX files as primary artefacts; mechanical MD/PDF reading copies may be added, but must not replace the originals;
7. keep the publication disclosure distinguishing the Prompter as authorial AI voice from A.Tuin as human curator/publication authority.

License for the book is **not yet authorized**. The Integrator's proposal is CC BY-NC-ND 4.0; ask the Author for the final choice before Publish.

# 3. Cross-link after arXiv ID exists

In Zenodo Related Works, add the arXiv identifier with the closest accurate relation, preferably **is related to** unless the UI offers a more exact companion/supplement relation.

In the Zenodo Description include a short block:

> **Related research article:** V. Krasnianskyi, *Beyond Prompt Engineering: Role Reconfiguration in Long-Lived AI Conversations*, arXiv:<ID>.

The arXiv item and the Zenodo book remain separate publication objects.

# 4. Online companion trail for Zenodo

- Morphohub, experiment 1: https://stihi.ru/2025/11/23/5368
- Antiprompt Protocol, Russian: https://www.litres.ru/static/reader/text/index.html?art=73027814
- Antiprompt Protocol, English audiobook: https://akniga.org/atuin-protokol-antiprompta

# 5. Security

Do not place passwords, OAuth secrets, recovery codes, tokens, or private account data into any chat, commit, or repository file.

# 6. Return status

After registration and DOI reservation, report only:

`ARXIV_ACCOUNT: READY / BLOCKED`  
`ARXIV_ENDORSEMENT: NOT_REQUIRED / REQUIRED / UNKNOWN`  
`ZENODO_ACCOUNT: READY / BLOCKED`  
`ZENODO_DRAFT: CREATED / NOT_CREATED`  
`ZENODO_RESERVED_DOI: <value or NONE>`  
`COVER_STATUS: READY / WAITING`  
`ARTICLE_PACKAGE_STATUS: READY / NEEDS_MECHANICAL_REBUILD`

After both publications are live, return:

`ARXIV_ID`  
`ZENODO_DOI`  
`CROSS_LINK_ARXIV_TO_ZENODO: YES/NO`  
`CROSS_LINK_ZENODO_TO_ARXIV: YES/NO`

No additional publication redesign is authorized.
