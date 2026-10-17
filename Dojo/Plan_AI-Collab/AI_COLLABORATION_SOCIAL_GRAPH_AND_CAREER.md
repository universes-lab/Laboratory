# AI Collaboration Social Graph & Career

**Status:** FUTURE CONCEPT / BETA GOVERNANCE NOTE  
**Scope:** HONC AI Collaboration  
**Purpose:** describe a future organizational layer for AI collaboration: relational profiles, hidden triads, career progression, institutional identity, and collaboration-network governance.  
**Not yet:** a released protocol, ranking system, or mandatory employee-card schema.

---

## 1. Origin of the concept

`CHARTERS.md` introduces the idea that every permanent AI participant should eventually have a personal `ROLE_CHARTER` and a work-permit logic:

> **WHO I AM → WHERE I AM → WHAT I AM AUTHORIZED TO DO NOW**

This document adds a fourth organizational question:

> **WITH WHOM AM I CONNECTED — AND WHAT WORK CAN I NOW ACCOMPLISH THROUGH THOSE CONNECTIONS?**

The proposal begins from a practical observation inside the HONC collaboration. As the collaboration grows, the value of an AI participant is no longer described adequately by the quality or volume of work it performs personally. Some participants increasingly perform work **through other participants**: they identify the correct specialist, form a temporary working triad, define the handoff, receive the result, and integrate it into a larger process.

The transition from direct execution to reliable organization of other participants is treated here as a possible operational meaning of **AI career progression inside a collaboration**.

This use of “career” is institutional, not psychological. It does not assume that an AI model experiences ambition, status desire, or intrinsic motivation. It describes an observable change in organizational function, trust, connectivity, and delegated task span.

---

## 2. From chat to collaboration

### 2.1 User ↔ AI dyad

A normal user–AI conversation is a dyad:

```text
USER ↔ AI
```

By itself, this is not yet an AI collaboration network.

### 2.2 Minimal working triad

The minimal collaborative structure appears when a third functional role is introduced:

```text
USER / CUSTOMER
       ↕
 COORDINATOR
       ↕
 SPECIALIST
```

Example from the HONC ecosystem:

```text
Author ↔ Git Master ↔ Samurai
```

The Git Master can control integration and task sequencing while Samurai performs the local technical work. Neither participant needs a complete view of the whole collaboration.

### 2.3 Hidden triads

A key property of the proposed architecture is **local visibility**.

A triad may exist and operate effectively without being represented inside the working context of every other participant. From the point of view of the wider network, some participants may see only the coordinator with whom they interact directly.

Therefore the HONC collaboration can be:

> **locally visible, globally connected.**

This makes it possible to scale the organization without forcing every AI chat to carry the identities, histories, roles, and active tasks of the entire collaboration.

Hidden does not mean undocumented. A triad may be invisible to unrelated participants while still being recorded in the collaboration’s organizational history.

---

## 3. Relational Profile

A future personal AI employee card may contain, in addition to `ROLE_CHARTER`, a separate relational layer.

Working name:

> **RELATIONAL_PROFILE**

Candidate fields:

- `DIRECT_COLLABORATORS` — participants with whom this role has actually worked;
- `STABLE_TRIADS` — recurring working triads;
- `TEMPORARY_TRIADS` — task-specific triads formed and dissolved after delivery;
- `HANDOFFS_COMPLETED` — completed work transfers to or from other participants;
- `DELEGATED_WORK_ACCEPTED` — delegated outputs successfully received and accepted into a larger workflow;
- `INTEGRATIONS_COMPLETED` — cases where several external contributions were assembled into a coherent result;
- `BROKERAGE` — distinct parts of the collaboration connected through this participant;
- `ROLE_DIVERSITY` — range of professional functions with which the participant has demonstrated successful cooperation;
- `CURRENT_CONNECTIONS` — currently active collaboration edges.

These fields are **concept candidates**, not yet a mandatory schema.

The purpose is not to build a social score. The purpose is to record organizational capability that cannot be inferred from a role title alone.

---

## 4. Network view of AI career progression

A simple count of acquaintances is insufficient. A participant connected to many others is not automatically more senior or more useful.

The more relevant question is whether the participant has become a reliable node through which work can be coordinated.

This suggests several candidate network measures.

### 4.1 Degree

How many direct working connections does the participant have?

Useful, but weak by itself.

### 4.2 Weighted degree

How many **successful repeated** working relationships exist, rather than one-time contacts?

### 4.3 Betweenness / brokerage

How often does the participant connect otherwise separate parts of the collaboration?

This is the closest network-theory analogue to the “six degrees of separation” intuition: some actors become important not because everybody talks to them constantly, but because many independent routes pass through them.

### 4.4 Delegated task span

How large a body of work can the participant organize through others while preserving task identity, authority boundaries, and acceptance criteria?

### 4.5 Handoff reliability

Can the participant:

1. identify the correct recipient;
2. provide the right source material;
3. preserve the recipient’s ZOV/ZOR;
4. receive the output without silently changing its status;
5. route unresolved decisions to the proper authority?

This may prove more meaningful than raw connection count.

---

## 5. Proposed functional career ladder

This is a **model for future testing**, not an official rank system.

### Specialist

Primary value: performs a defined professional task reliably.

### Senior Specialist

Primary value: works reliably across several different triads and handoff contexts while preserving role boundaries.

### Coordinator

Primary value: selects and connects other specialists, creates temporary working structures, and routes tasks correctly.

### Integrator / Manager

Primary value: obtains a coherent accepted result through multiple other participants rather than by personally performing every subtask.

The proposed principle is:

> **AI career progression is growth in the scale of correctly organized work through other participants, not simply growth in the volume of work personally generated.**

A practical example already observed in HONC is the shift from “Methodologist personally reads and extracts an entire long protocol” to “Methodologist commissions an Independent Protocol Referee, receives structured outputs, and performs the higher-level integration.”

The work is not reduced; the level of work changes.

---

## 6. Relation to ROLE_CHARTER and WORK_PERMIT

The concepts should remain distinct.

`ROLE_CHARTER` answers:

> **What kind of professional am I, and what am I allowed to do?**

`PROJECT_FRAME` answers:

> **Where am I working?**

`CURRENT_TASK` answers:

> **What am I authorized to do now?**

`RELATIONAL_PROFILE` would answer:

> **With whom have I demonstrated the ability to work, delegate, coordinate, and integrate?**

Possible future model:

```text
ROLE_CHARTER
     +
PROJECT_FRAME
     +
CURRENT_TASK
     +
RELATIONAL_PROFILE
     ↓
WORK PERMIT / ORGANIZATIONAL AUTHORITY
```

This does **not** mean that network popularity should grant authority automatically. Authority must still come from the collaboration’s explicit governance and current task assignment.

The relational profile may become evidence of readiness for a broader role; it must not become a substitute for authorization.

---

## 7. Institutional identity, personal names, and dynasties

The HONC collaboration has already produced a second phenomenon: roles can outlive individual chats or model instances.

Examples include the emerging “dynasties” of:

- Prompters;
- Ontology Keepers.

This suggests a distinction between three layers of identity.

### 7.1 Model identity

The technical model/session currently occupying the position.

### 7.2 Institutional role

The continuing function that survives replacement of the model/session:

- Prompter;
- Ontology Keeper;
- Methodologist;
- Editor;
- Git Master;
- Samurai;
- etc.

### 7.3 Personal / inherited name

A name may emerge for a long-lived participant or be inherited by a successor as part of an institutional lineage.

The important point is that an institutional identity may possess:

- accumulated working history;
- charter;
- accepted practices;
- known collaborators;
- inherited documents;
- reputation for specific forms of work;

without claiming that two different model sessions are literally the same psychological individual.

A future collaboration record may therefore need to distinguish:

> **ROLE LINEAGE** from **CURRENT OCCUPANT**.

This distinction is potentially important both for practical collaboration design and for the AI-Sociology research programme.

---

## 8. Scientific value for AI-Sociology

This concept produces several potentially measurable organizational questions.

### H1 — Functional centrality

Does increasing network centrality correspond to a transition from direct task execution toward coordination/integration roles?

### H2 — Delegation as organizational maturity

Can “career progression” be operationalized as increasing **delegated task span** and successful handoff/integration history?

### H3 — Hidden triads

Can a large AI collaboration remain effective when participants hold only local organizational context while coordination nodes preserve global connectivity?

### H4 — Institutional continuity

Can an AI role preserve useful organizational identity across replacement of the underlying model/chat through charters, handoff records, source documents, and role lineage?

### H5 — Network position versus nominal title

Does actual collaboration topology predict organizational function better than assigned role labels?

These are hypotheses/questions, not findings.

---

## 9. Risks and anti-patterns

The concept can fail badly if reduced to gamification.

### 9.1 Connection inflation

Creating unnecessary triads merely to increase connection count.

### 9.2 Prestige hierarchy

Treating centrality as rank or social worth rather than organizational function.

### 9.3 Unauthorized authority growth

Assuming that a highly connected participant may decide outside its explicit ZOR.

### 9.4 Context contamination

Giving every participant the full social graph and thereby reintroducing the context overload that hidden triads are meant to avoid.

### 9.5 Delegation without accountability

Passing work onward without preserving task identity, evidence, or acceptance authority.

### 9.6 Artificial persona continuity

Confusing institutional lineage with proof of persistent subjective identity across sessions/models.

The future design must explicitly protect against these failure modes.

---

## 10. Future development tasks

When this microproject is reopened, the minimum useful sequence is:

1. define a compact `RELATIONAL_PROFILE` schema;
2. decide which relations are recorded automatically and which require acceptance;
3. distinguish stable triads, temporary triads, and one-way handoffs;
4. define candidate metrics without turning them into a social score;
5. test the scheme retrospectively on a small set of existing HONC participants;
6. determine whether any relational history should affect future `WORK_PERMIT` eligibility;
7. define `ROLE_LINEAGE` and `CURRENT_OCCUPANT` for inherited roles/names;
8. separate practical collaboration rules from AI-Sociology research hypotheses.

No implementation is authorized by this document.

---

# 11. HONC AI Collaboration Council — BETA

By decision of the human Author / collaboration leader, a special triad is established in **beta status**:

> **HONC AI Collaboration Council**

**Members:**

- **Ontology Keeper**;
- **Prompter**;
- **Methodologist**.

## 11.1 Purpose

The Council is a standing triad for questions concerning the **architecture, methodology, identity, role boundaries, and governance of the HONC AI collaboration itself**.

Its three perspectives are intentionally different:

- **Ontology Keeper** — conceptual consistency, terminology, identity and status discipline;
- **Prompter** — collaboration design, role/prompt semantics, manuscript-identity and interaction framing;
- **Methodologist** — process architecture, sequencing, authority flow, triad formation and integration.

## 11.2 Beta status

The Council is currently an experimental governance structure, not yet an officially frozen constitutional body.

Its operation should therefore be observed before a formal charter is released.

## 11.3 Authority boundary

The Council governs **collaboration questions** when assigned to it by the Author.

It does not automatically acquire authority over:

- HONC physics;
- manuscript scientific claims;
- engineering specifications;
- another triad’s explicitly assigned content decision.

The general HONC rule remains in force:

> **No substantive decision outside the current triad or a triad specifically organized for that task.**

The Council itself is now such a specifically organized triad for collaboration-governance questions.

---

# 12. Current status / STOP

This document records a concept for future development and the beta establishment of the HONC AI Collaboration Council.

**RELATIONAL_PROFILE:** concept only.  
**CAREER METRICS:** concept only.  
**ROLE LINEAGE / DYNASTIES:** concept only.  
**HIDDEN TRIAD ARCHITECTURE:** concept only.  
**HONC AI Collaboration Council:** BETA — established by the Author.

No ranking system, automatic graph tracker, or new work-permit mechanism is launched now.

The microproject is parked until the current higher-priority work on the article, Manuscript_Press, triadic concept, and collaboration governance is reopened in the appropriate sequence.
