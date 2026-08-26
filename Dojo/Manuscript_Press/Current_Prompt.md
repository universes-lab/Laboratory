# CURRENT OPERATIONAL FRAME

ACTIVE_OPERATION:
MANUSCRIPT WRITER — FINALIZE 01_T00_VERIFY

ACTIVE_MODE:
IMPLEMENTER

ACTIVE SPEC:
D:\Gemini\dojo\SPEC.md

ACTIVE STEP:
FINALIZE 01_T00_VERIFY

Execute only the ACTIVE STEP defined by the current SPEC.

Before acting, confirm that:
ACTIVE_MODE == REQUIRED_MODE.

AUTHORIZED NOW:
- inspect only the artifacts belonging to run_id 01_T00_VERIFY;
- inspect logs/runs/01_T00_VERIFY/raw_output.md;
- inspect logs/runs/01_T00_VERIFY/metadata.yaml;
- inspect logs/runs/01_T00_VERIFY/constants_check.yaml if present;
- inspect Output/01_T00_VERIFY.manuscript.md;
- if constants_check.yaml is absent or zero-length, create it solely
  from 01_T00_VERIFY/raw_output.md using the existing
  parse_constants_check() result;
- replace a zero-length constants_check.yaml only for this purpose;
- calculate the actual SHA-256 of the 01_T00_VERIFY manuscript;
- compare it with metadata.yaml;
- physically verify all Evidence required by the ACTIVE SPEC;
- produce the factual report required by the ACTIVE SPEC.

NOT AUTHORIZED:
- use Evidence from any other run_id;
- read constants data from 01_T00 or another run as substitute Evidence;
- modify metadata.yaml to make it agree with expected results;
- modify raw_output.md;
- modify manuscript.md;
- modify generator.py or other production code;
- execute model inference;
- start another production or verification run;
- modify Syst_Prompt.md or Input/;
- perform unrelated cleanup, refactoring, migration, Git work, or repair;
- continue to another STEP;
- modify the SPEC or Current Prompt.

If constants_check.yaml is already non-empty but contradicts
01_T00_VERIFY/raw_output.md:

STOP → REPORT → QUERY SENSEI.

If metadata, manuscript SHA-256, Constants Check, or other required
Evidence contradict each other:

STOP → REPORT.

Do not repair factual contradictions by rewriting Evidence.

If all required Evidence is mutually consistent:
REPORT → STOP → WAIT FOR EXTERNAL REVIEW.

At closure, perform the Execution Health check defined by
CODING_PHILOSOPHY.md.

STOP.
WAIT FOR EXTERNAL REVIEW.