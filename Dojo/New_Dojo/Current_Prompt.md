# MANUSCRIPT_PRESS — CURRENT_PROMPT

## ACTIVE MODE

IMPLEMENTER

## GOVERNING DOCUMENTS

Read and obey:

1. `CODING_PHILOSOPHY.md`
2. `SPEC.md`
3. `IMPLEMENTATION_PLAN.md`
4. `IMPLEMENTATION_MAP_APPROVED.yaml`

Authority:

* `SPEC.md` — frozen system requirements.
* `IMPLEMENTATION_PLAN.md` — frozen campaign sequence.
* `IMPLEMENTATION_MAP_APPROVED.yaml` — approved factual repository/code map.
* `Current_Prompt.md` — current operational authorization only.

`IMPLEMENTATION_PLAN.md` does NOT authorize autonomous progression.

Only the ACTIVE STEP below authorizes work.

---

# EXECUTION CONTROL

Engineering Sensei: DeepSeek.

Perform exactly ONE DeepSeek STEP.

After completing it:

REPORT → STOP → WAIT_FOR_DEEPSEEK.

Do not:

* choose the next step;
* anticipate later Phase-1 work;
* expand tests beyond the active STEP;
* add useful abstractions, refactors, APIs or edge cases;
* reinterpret SPEC to fit existing code;
* use quarantined Phase-1 code unless the active STEP explicitly permits it.

If a material decision is unresolved:

`IMPLEMENTATION BLOCKER`

and STOP.

---

# PHASE 1 — STEP 1

## OBJECTIVE

Implement the protected-span parser according to SPEC v3.2.2 §4.

## FILES ALLOWED TO CREATE/MODIFY

* `src/parser/protected_span_parser.py`
* `tests/phase1/test_protected_span_parser.py`

## REQUIRED GRAMMAR

```text
<!-- MP:PROTECTED id="P42_01":BEGIN -->
<exact literal material>
<!-- MP:PROTECTED id="P42_01":END -->
```

## REQUIRED BEHAVIOR

* START/END IDs match.
* Protected IDs are unique.
* Nesting is forbidden in V1.
* Protected spans are recognized before production-marker interpretation.
* `<!-- MP:XXXX -->` inside protected material remains literal content.
* Production markers do not become boundaries while a protected span is open.

Return:

* protected span objects containing:

  * `id`
  * `content`
  * `start_line`
  * `end_line`
* SLOTTED_SOURCE representation using:
  `⟦MP_PROTECTED:P42_01⟧`

## REQUIRED TESTS

1. single protected span;
2. multiline protected span;
3. quotes / Markdown / code inside protected span;
4. mismatched START/END IDs → `PROTECTED_MARKUP_INVALID`;
5. missing END → `PROTECTED_MARKUP_INVALID`;
6. nesting → `PROTECTED_MARKUP_INVALID`;
7. production marker inside protected span remains literal;
8. duplicate protected ID → `PROTECTED_MARKUP_INVALID`.

Use protected IDs in the frozen-contract form such as `P42_01`.

## NON-GOALS

Do not:

* parse SOURCE production markers;
* build marker graph;
* validate PROMPT_MAP;
* implement revision/freeze;
* extract ATX headings.

## EVIDENCE

* `python -m py_compile` passes;
* all 8 STEP tests pass.

## REPORT

Return only:

```yaml
Phase: 1
Step: 1
Status: COMPLETED | BLOCKED
Files_Changed: [...]
Implemented: [...]
Tests_Run: [...]
Test_Results: [...]
Evidence: [...]
Limitations: [...]
Next: WAIT_FOR_DEEPSEEK
```

Then STOP.
