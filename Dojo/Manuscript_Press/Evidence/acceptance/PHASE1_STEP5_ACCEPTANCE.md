# STEP.md — MANUSCRIPT_PRESS

## IDENTITY
**Project:** MANUSCRIPT_PRESS  
**Phase:** 1  
**Step:** 5  
**Status:** CANDIDATE FOR DOC APPROVAL  
**Version:** 1.0  
**Date:** 2026-09-04  
**Technical Authority:** SPEC v3.2.2 (FROZEN)  

---

## OBJECTIVE
Implement extraction of ATX headings (`#` ... `######`) as structural passthrough material, preserving their exact position relative to production blocks.

## PREREQUISITE
This step operates on the `SLOTTED_SOURCE` output from Step 1, after protected spans have been processed.

## ALLOWED WORKING FILES
- `src/parser/atx_heading_extractor.py` — create new.
- `tests/phase1/test_atx_heading_extractor.py` — create new.

## FROZEN SPEC BEHAVIOR (AUTHORITATIVE)
- SPEC §10: ATX headings (`#` ... `######`) are automatic structural passthrough.
- They are extracted BEFORE they reach the Gemma context.
- They are recognized ONLY outside protected spans (guaranteed by operating on `SLOTTED_SOURCE`).
- Their exact position relative to production blocks must be preserved for final assembly.

### Extractor Requirements
1.  **ATX Heading Detection:** Identify lines that start with `#` through `######` followed by a space.
2.  **Position Preservation:** For each heading, record:
    *   `heading_text` (the content after the `#` prefix)
    *   `level` (1-6)
    *   `marker_id` (the nearest preceding production marker, or `None` if before the first marker)
3.  **Output:** Return a list of heading objects with the above fields.
4.  **Edge Cases:** Handle headings without a preceding marker (they belong to the "pre-marker" space, which is not a production block). For these, `marker_id` should be `None`.

## TESTS REQUIRED
1.  **Single Heading:** `# Section 1` → heading with text "Section 1", level 1, marker_id `None`.
2.  **Heading After a Marker:** `<!-- MP:0001 --> # Section 1` → heading with marker_id `MP:0001`.
3.  **Multiple Headings:** Extract all headings correctly.
4.  **Protected Span Ignored:** A protected span containing `# Heading` must NOT be extracted as a structural heading. This is guaranteed by operating on `SLOTTED_SOURCE`.

## NON-GOALS
- ❌ Modifying the source text.
- ❌ Revision freezing.
- ❌ Any inference, candidate pipeline, commit, resume, or assembly logic.
- ❌ Validating heading structure beyond ATX syntax.

## EVIDENCE REQUIRED FOR COMPLETION
- [ ] `python -m py_compile src/parser/atx_heading_extractor.py` passes.
- [ ] All tests pass.

## REPORT FORMAT
```yaml
Phase: 1
Step: 5
Status: COMPLETED / BLOCKED / FAILED
Files_Changed:
  - src/parser/atx_heading_extractor.py
  - tests/phase1/test_atx_heading_extractor.py
Implemented:
  - ATX heading extraction with position preservation
Tests_Run:
  - 4 tests
Test_Results:
  - all passed / list of failures
Evidence:
  - py_compile: PASS
  - tests: PASS
Limitations:
  - none within scope
Next: WAIT_FOR_DEEPSEEK