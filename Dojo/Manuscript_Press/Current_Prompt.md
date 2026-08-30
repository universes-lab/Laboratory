# MANUSCRIPT_PRESS — CURRENT_PROMPT

## PHASE 1: CORE PARSERS + REVISION FREEZE

Before any action read, in this order:

1. `CODING_PHILOSOPHY.md`
2. `SPEC.md`
3. `IMPLEMENTATION_PLAN.md`
4. `IMPLEMENTATION_MAP_APPROVED.yaml`

These documents have distinct authority:

* `SPEC.md` — WHAT the system must be.
* `IMPLEMENTATION_PLAN.md` — approved build sequence.
* `IMPLEMENTATION_MAP_APPROVED.yaml` — approved forensic assessment of the old repository.
* `Current_Prompt.md` — your CURRENT operational scope.

Do NOT repeat Phase 0.

Do NOT reclassify the repository.

If the actual repository materially contradicts `IMPLEMENTATION_MAP_APPROVED.yaml`, STOP and report:

`REPOSITORY_DRIFT`

with the exact discrepancy.

## Gemma.md

`Gemma.md` is the SYSTEM CONTRACT for the local Gemma-The-Writer model.

It is NOT your own system prompt and not an instruction addressed to Coding Samurai.

---

# CURRENT TASK

Execute **PHASE 1 only** from `IMPLEMENTATION_PLAN.md`:

## CORE PARSERS + REVISION FREEZE

Implement and test:

1. SOURCE production-marker parsing:

   * `<!-- MP:0001 -->`
   * logical ID `MP:0001`
   * filesystem-safe `MP-0001`
   * SOURCE order is execution order
   * numeric adjacency is not required

2. PROMPT_MAP YAML parsing:

   * keyed by logical marker ID
   * exactly one entry per SOURCE marker
   * mandatory non-empty `LONG_RANGE_FRAME`
   * mandatory non-empty `LOCAL_TRANSFORMATION`
   * reject missing or extra entries

3. PROTECTED span parsing:

   * BEGIN/END ID matching
   * no nesting in V1
   * protected span parsed before production markers inside it
   * marker-looking syntax inside protected material remains literal
   * invalid markup produces the SPEC-defined failure

4. Markdown ATX structural passthrough extraction:

   * headings only
   * outside protected spans
   * retain deterministic position for later assembly

5. Deterministic authority freeze:

   * frozen copies under `work/revisions/<revision_id>/frozen/`
   * deterministic authority hashes
   * canonical revision payload
   * deterministic `revision_id`
   * `PRODUCTION_REVISION.manifest`

6. Revision validation:

   * START/RESUME-capable validation primitive
   * pre-GENERATE validation primitive
   * pre-COMMIT validation primitive
   * active frozen-authority mutation must be detectable as specified

## Implementation boundaries

Phase 1 MUST NOT implement:

* Gemma inference
* typed inference context assembly
* CACHE_BEFORE
* candidate generation
* human acceptance
* COMMIT_RECORD
* resume/recovery progress logic
* final manuscript assembly

Those belong to later phases.

Do NOT resurrect or invoke:

* `src/builder.py`
* CONCEPT_PACKAGE input paths
* paired generation
* PART_HANDOFF
* CHAPTER_CONTEXT
* `paired_runner`
* old logs/Output as runtime state

`src/loader.py` is approved for later reuse but is not the focus of Phase 1.

Do not delete legacy files during this phase unless explicitly instructed.

## Tests

Write focused Phase-1 tests for the behavior implemented now.

At minimum cover the applicable frozen acceptance cases:

* duplicate SOURCE marker
* missing PROMPT_MAP entry
* extra PROMPT_MAP entry
* PROMPT_MAP physical order different from SOURCE
* inline protected span
* multiline protected span
* protected material containing quotes/Markdown/code
* marker-looking syntax inside protected material
* malformed protected markup
* structural ATX heading passthrough
* deterministic revision ID
* editable preparation source changing after freeze does not alter frozen revision
* frozen active authority mutation is detected

Do not implement fake stubs merely to claim later-phase tests pass.

## STOP / BLOCKER RULE

If a necessary Phase-1 decision is genuinely unresolved by `SPEC.md` and this Current_Prompt:

STOP and report:

`IMPLEMENTATION OPEN POINT`

Do not invent architecture.

## REQUIRED PHASE REPORT

After Phase 1 implementation and tests, report only:

```yaml
Phase: 1
Status: COMPLETED | BLOCKED
Files_Changed: [...]
Implemented: [...]
Tests_Run: [...]
Test_Results: [...]
Limitations: [...]
SPEC_Sections_Satisfied: [...]
Next: WAIT_FOR_APPROVAL | BLOCKED
```

Then STOP.

Do not begin Phase 2 without explicit human approval.
