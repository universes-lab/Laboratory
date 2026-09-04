# STEP.md — MANUSCRIPT_PRESS

## IDENTITY
**Project:** MANUSCRIPT_PRESS  
**Phase:** 1  
**Step:** 3  
**Status:** ACTIVE  
**Version:** 1.1  
**Date:** 2026-09-02  
**Technical Authority:** SPEC v3.2.2 (FROZEN)  
**Approval:** DOC APPROVED — 2026-09-02

---

## OBJECTIVE

Implement a parser for `PROMPT_MAP.yaml` that loads the YAML mapping, validates marker keys and the two required per-marker authority fields, and returns a deterministic marker-keyed representation.

## PREREQUISITE

PHASE 1 — STEP 2 is ACCEPTED.

Acceptance record:  
`Evidence/acceptance/PHASE1_STEP2_ACCEPTANCE.md`

## ALLOWED WORKING FILES

- `src/parser/prompt_map_parser.py` — create new.
- `tests/phase1/test_prompt_map_parser.py` — create new.

## FROZEN SPEC BEHAVIOR (AUTHORITATIVE)

- `PROMPT_MAP` is YAML.
- Top-level keys are logical production marker IDs in the exact form `MP:XXXX`, where `XXXX` is four decimal digits.
- Each marker entry must contain:
  - `LONG_RANGE_FRAME`
  - `LOCAL_TRANSFORMATION`
- Both required values must be strings and substantively non-empty.
- Physical YAML order does not define execution order.
- SOURCE ↔ PROMPT_MAP correspondence is NOT validated in this STEP.

## PARSER REQUIREMENTS

1. **Safe YAML Loading**
   - Parse YAML without executing arbitrary YAML constructors.
   - Malformed YAML → `PROMPT_ENTRY_INVALID`.

2. **Top-Level Shape**
   - A non-empty PROMPT_MAP must be a mapping keyed by marker ID.
   - Empty YAML / empty mapping may return an empty parser result.
   - This parser-local result does NOT declare a markerless production revision valid.
   - Non-mapping top-level content → `PROMPT_ENTRY_INVALID`.

3. **Marker Key Validation**
   - Every key must be a string matching exactly `MP:[0-9]{4}`.
   - Invalid key → `PROMPT_ENTRY_INVALID`.

4. **Entry Shape**
   - Each marker value must be a mapping.
   - Non-mapping entry → `PROMPT_ENTRY_INVALID`.

5. **Required Fields**
   - `LONG_RANGE_FRAME` must exist and be a string.
   - `LOCAL_TRANSFORMATION` must exist and be a string.
   - Missing required field → `PROMPT_ENTRY_INVALID`.
   - Empty or whitespace-only required field → `PROMPT_ENTRY_INVALID`.
   - Validation may use stripped content to determine emptiness, but returned field text must preserve the original loaded string value.

6. **Output**
   - Return a dictionary keyed by canonical marker ID.
   - Each value must expose:
     - `long_range_frame`
     - `local_transformation`
   - This mapping does not establish execution order.
   - This STEP validates only the two required authority fields; it does not assign semantics to additional YAML fields.

## TESTS REQUIRED

1. **Valid PROMPT_MAP**
   - Two valid entries load successfully.
   - Returned marker keys and both required field values are correct.

2. **Missing Required Field**
   - Missing `LOCAL_TRANSFORMATION` → `PROMPT_ENTRY_INVALID`.

3. **Empty Required Field**
   - Empty or whitespace-only `LONG_RANGE_FRAME` → `PROMPT_ENTRY_INVALID`.

4. **Invalid Marker Key**
   - A key outside exact `MP:XXXX` form → `PROMPT_ENTRY_INVALID`.

5. **Malformed / Invalid Structure**
   - Malformed YAML, non-mapping top level, or non-mapping marker entry → `PROMPT_ENTRY_INVALID`.
   - These may be parameterized within one normative test.

6. **Empty PROMPT_MAP**
   - Empty YAML or `{}` → empty parser result.
   - Do not infer global revision validity from this parser-local result.

## NON-GOALS

- ❌ Validating SOURCE ↔ PROMPT_MAP correspondence.
- ❌ Using PROMPT_MAP physical order as execution order.
- ❌ ATX heading extraction.
- ❌ Revision freezing.
- ❌ Marker block extraction.
- ❌ Any inference, candidate pipeline, commit, resume, or assembly logic.
- ❌ Interpreting or rewriting the substantive content of `LONG_RANGE_FRAME` or `LOCAL_TRANSFORMATION`.
- ❌ Defining semantics for additional YAML fields.

## EVIDENCE REQUIRED FOR COMPLETION

- [ ] `python -m py_compile src/parser/prompt_map_parser.py` passes.
- [ ] All STEP-3 tests pass.

## REPORT FORMAT

```yaml
Phase: 1
Step: 3
Status: COMPLETED / BLOCKED / FAILED
Files_Changed:
  - src/parser/prompt_map_parser.py
  - tests/phase1/test_prompt_map_parser.py
Implemented:
  - PROMPT_MAP YAML parsing
  - marker-key validation
  - required-field validation
Tests_Run:
  - STEP-3 test suite
Test_Results:
  - all passed / list of failures
Evidence:
  - py_compile: PASS
  - tests: PASS
Limitations:
  - none within scope
Next: WAIT_FOR_DEEPSEEK
```

END OF ACTIVE STEP
