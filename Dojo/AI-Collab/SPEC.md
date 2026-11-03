# SPEC.md — BUILD 001 / STEP 2 — VERDICT ENGINE (v2.3)

```yaml
BUILD: 001
STEP: 2
NAME: VERDICT_ENGINE
VERSION: 2.3
STATUS: READY_FOR_SAMURAI
DATE: 2026-11-02
SUPERSEDES: v2.2
```

---

## 0. AUTHORITY ORDER

```yaml
AUTHORITY_ORDER:
  1: WEB_SEAT_WS0_OBSERVATION_CONTRACT.md v0.4 §2.1 + §7
  2: BUILD_001_STEP2_STEP3_SPEC.md §A (I-1…I-7)
  3: BUILD_001_STEP2_VECTORS.json expect (DO NOT EDIT)
  4: test_vectors.py (DO NOT EDIT)
```

If a lower authority conflicts with a higher authority, implementation follows the higher authority and the conflict is reported.

Known current conflict: E10 decisive_rule expectation. See `KNOWN_MISMATCH`.

---

## 1. DELTAS FROM v2.2

```yaml
DELTAS_FROM_v2_2:
  - FULL_REWRITE_definition: replace entire file content, no need to physically delete file
  - completeness_check_after_rewrite_before_compile: mandatory
  - skeleton_markers_must_be_absent: ["см. SPEC v2.1", "остальные rules 2", "$pre.", "$post."]
  - rules_2_to_9_code_presence_check: mandatory
  - hash_before_hash_after_evidence: required
  - if_completeness_check_fails: STOP -> REPORT -> WAIT (no py_compile, no test)
  - everything_else_from_v2_2: unchanged
```

Rule-map v2.2 unchanged:
- Rule 5 = PATHS
- Rule 6 = HISTORY
- L0 path = `$.text`
- E10 known mismatch
- vectors/test runner not touched
- STEP 3 RED

---

# OBJECTIVE

Correct `verdict(pre, post)` per the authoritative rule-map.

Target verification state:

- V1–V18: PASS — 18/18
- E1–E9: PASS — 9/9
- E10: known mismatch — expected FAIL in existing runner
- E11–E14: PASS — 4/4
- total authoritative vectors passed: 31/32
- L0_GUARD: PASS

**STEP 2 handoff-ready criterion:**

```text
31/32
AND failed_ids == ["E10"]
AND L0_GUARD PASS
AND KNOWN_MISMATCH E10 documented
```

This means `step2_handoff_ready: yes`.

It does **not** mean Samurai may declare STEP 2 accepted.

Acceptance belongs to external review by Grok / Author.

STEP 3 remains blocked until acceptance.

---

# ROOT CAUSE

```yaml
problems_in_previous_pass:
  - verdict_engine.py was a skeleton, not implementation
  - rules 2-9 missing, replaced by "# ... остальные rules 2 → 10"
  - l0_path was "$pre.text" / "$post.text" (v2.1 format), not "$.text"
  - code still referenced "см. SPEC v2.1"
  - file not rewritten between pass 3 and pass 4
```

---

# FILES

```text
MODIFY — FULL REWRITE (content replacement):
  E:\Gemini\Dojo\AI-Collab\verdict_engine.py

READ / EXECUTE — DO NOT MODIFY:
  E:\Gemini\Dojo\AI-Collab\test_vectors.py
  E:\Gemini\Dojo\AI-Collab\BUILD_001_STEP2_VECTORS.json

READ AS AUTHORITY — DO NOT MODIFY:
  E:\Gemini\Dojo\AI-Collab\BUILD_001_STEP2_STEP3_SPEC.md
  E:\Gemini\Dojo\AI-Collab\WEB_SEAT_WS0_OBSERVATION_CONTRACT.md
  E:\Gemini\Dojo\AI-Collab\AI_COLAB_2_BUILD_CONTRACT_001.md
```

Do not create a replacement test runner.

Do not modify any authority file during this STEP.

---

# FULL REWRITE — DEFINITION

```yaml
FULL_REWRITE_MEANS:
  - replace the entire content of verdict_engine.py
  - the file after rewrite must contain complete implementation of Rules 1-10
  - no skeleton markers, no placeholder comments, no "TODO", no "# ..." where logic must be

FULL_REWRITE_DOES_NOT_REQUIRE:
  - physically deleting the file
  - recreating the file path
  - changing the filename
```

FULL REWRITE ≠ patch. FULL REWRITE = write the file from top to bottom with complete logic, replacing what was there.

---

# PREFLIGHT

Run:

```powershell
Test-Path E:\Gemini\Dojo\AI-Collab\.venv\Scripts\python.exe
```

Required:

```text
True
```

If missing:

```text
STOP
REPORT VENV_MISSING
WAIT
```

Do not install packages.

Do not create another venv.

Do not substitute another interpreter.

---

# EVIDENCE GATES — BEFORE FIX

## Gate 1 — Hash before

```powershell
Get-FileHash E:\Gemini\Dojo\AI-Collab\verdict_engine.py -Algorithm SHA256 | Select-Object -ExpandProperty Hash
```

Record as `hash_before`. This value must appear in REPORT.

## Gate 2 — Grep obsolete strings

```powershell
Select-String `
  -Path E:\Gemini\Dojo\AI-Collab\verdict_engine.py `
  -Pattern 'UNHANDLED_STATE_DIFFERENCE|POST_CONVERSATION_CLOSED|PRE_OBJECT_IS_NULL'
```

Record factual matches and count in REPORT.

A zero before-count is allowed. It does not change the task.

## Gate 3 — Grep skeleton markers

```powershell
Select-String `
  -Path E:\Gemini\Dojo\AI-Collab\verdict_engine.py `
  -Pattern 'см\. SPEC v2\.1|остальные rules 2|\$pre\.|\$post\.'
```

Record factual matches and count in REPORT.

These markers prove the file is not yet rewritten. Their presence before rewrite is expected and does not block proceeding to rewrite.

---

# IMPLEMENTATION

## 1. Pure function

`verdict(pre, post)` must be pure.

Forbidden inside `verdict()` and its verdict helpers:

- filesystem I/O;
- network;
- browser;
- current time;
- random;
- mutation of `pre`;
- mutation of `post`;
- mutable global execution state.

Same input → same output.

Python stdlib only.

---

## 2. Output contract

Return exactly this shape:

```python
{
    "verdict": <RECOVERED | AMBIGUOUS | LOST | NEEDS_HUMAN | MISMATCH | None>,
    "reason": <str | None>,
    "delta": <bool | None>,
    "send_status": <str | None>,
    "flags": <list>,
    "decisive_rule": <str | None>,
    "rules_trace": <list[str]>,
    "pre_ref": <snapshot_id | None>,
    "post_ref": <snapshot_id | None>,
    "l0_violation": <str | None>,
}
```

### `pre_ref`

```python
pre_ref = pre.get("snapshot_id") if pre is not None else None
```

### `post_ref`

```python
post_ref = post.get("snapshot_id") if post is not None else None
```

### `send_status`

For non-L0 rule evaluation:

```python
send_status = post.get("send_status") if post is not None else None
```

Literal `"NONE"` stays `"NONE"`. Do not normalize to `None`.

For L0 violation:

```python
send_status = None
```

### `flags`

For non-L0 rule evaluation:

```python
flags = list(post.get("flags") or []) if post is not None else []
```

Preserve source order. Do not sort. Do not deduplicate.

For L0 violation:

```python
flags = []
```

---

## 3. L0 — HARD PRE-RULE GUARD

L0 executes before Rule 1.

Forbidden keys:

```python
{"text", "content", "body", "messages", "prompt", "completion"}
```

`check_l0()` recursively scans nested dicts and lists.

Scan order:

```text
1. pre
2. post
```

Use root path `$` independently for whichever object is being scanned.

Required path examples:

```text
$.text
$.foo[0].content
$.bar.messages
```

Do not emit:

```text
$pre.text
$post.text
```

If L0 finds a forbidden key, stop immediately.

Return:

```python
{
    "l0_violation": "<first forbidden path>",
    "verdict": None,
    "reason": "L0_VIOLATION",
    "delta": None,
    "send_status": None,
    "flags": [],
    "decisive_rule": None,
    "rules_trace": [],
    "pre_ref": <pre.snapshot_id or None>,
    "post_ref": <post.snapshot_id or None>,
}
```

Do not apply Rules 1–10 after L0 violation.

For all 32 authoritative vectors:

```text
l0_violation = None
```

---

## 4. Rule trace

`rules_trace` is diagnostic.

Before evaluating each rule condition, append that rule identifier in evaluation order.

Examples:

```python
["1"]
["1", "2", "3", "4", "5"]
["1", "2", "3", "4", "5", "6", "7", "7a", "8", "9", "10"]
```

The decisive rule must be the final entry.

For L0 violation:

```python
rules_trace = []
```

`rules_trace` is not one of the six authoritative vector-comparison fields.

---

## 5. Rule map — first matching wins

Evaluation order:

```text
L0
→ 1
→ 2
→ 3
→ 4
→ 5
→ 6
→ 7
→ 7a
→ 8
→ 9
→ 10
```

Rule 5 exists and means PATHS. Rule 6 means HISTORY only.

---

## RULE 1 — NO_EVIDENCE

### 1A. Immediate None short-circuit

If:

```python
pre is None or post is None
```

return immediately:

```yaml
verdict: AMBIGUOUS
reason: NO_EVIDENCE
delta: null
decisive_rule: "1"
```

Do not attempt cross-snapshot comparisons.

### 1B. Snapshot validity

If both objects exist, validate per authoritative §2.1 / §3 / closed lists.

Rule 1 fires for invalid snapshot, including:

```text
- missing mandatory §3 field (except I-1 exception)
- closed-list value outside §1.1
- post seat_id != pre seat_id
- post binding_id != pre binding_id
- post ts_utc <= pre ts_utc
- invalid ts_utc format
- send_attempt_logged == true AND send_status == "NONE"
```

Output:

```yaml
verdict: AMBIGUOUS
reason: NO_EVIDENCE
delta: null
decisive_rule: "1"
```

### I-1 content-null exception

If:

```python
post["conversation_opened"] is False
```

these post content fields may be `None`:

```text
conv_id
chain
tail_fps
n_msgs
extraction_path
fp_version
history_complete
```

Null values alone do not trigger Rule 1.

### Restart-only clarification

If both snapshots are otherwise valid and only `restart_epoch` / `restart_kind` differ:

- does not trigger Rule 1;
- does not trigger Rule 5;
- no invented restart reason;
- continue through Rules 2–9;
- if none fires, Rule 10.

---

## RULE 2 — NEEDS_HUMAN

Rule 2 reads `session_state` and flags from `post`.

```python
session_state = post.get("session_state")
post_flags = list(post.get("flags") or [])
```

Conditions, first true wins:

```text
1. post.session_state == EXPIRED
2. post.session_state == CHALLENGE
3. "double_ownership" in post.flags
4. "automation_forbids_observation" in post.flags
```

Reason priority (fixed):

```text
EXPIRED → SESSION_EXPIRED
CHALLENGE → SESSION_CHALLENGE
double_ownership → DOUBLE_OWNERSHIP
automation_forbids_observation → AUTOMATION_FORBIDS_OBSERVATION
```

Output:

```yaml
verdict: NEEDS_HUMAN
reason: <priority reason>
delta: null
decisive_rule: "2"
```

---

## RULE 3 — LOST

Rule 3 reads `session_state` from `post`.

Condition:

```python
post.get("session_state") == "AUTHENTICATED"
and post.get("conversation_opened") is False
```

Output:

```yaml
verdict: LOST
reason: null
delta: null
decisive_rule: "3"
```

---

## RULE 4 — CONV_ID_DIFFERS

Condition:

```python
pre["conv_id"] is not None
and post["conv_id"] is not None
and pre["conv_id"] != post["conv_id"]
```

Output:

```yaml
verdict: MISMATCH
reason: CONV_ID_DIFFERS
delta: null
decisive_rule: "4"
```

---

## RULE 5 — PATHS_NOT_COMPARABLE

Condition:

```python
pre["extraction_path"] != post["extraction_path"]
or pre["fp_version"] != post["fp_version"]
```

Output:

```yaml
verdict: AMBIGUOUS
reason: PATHS_NOT_COMPARABLE
delta: null
decisive_rule: "5"
```

Rule 5 = PATHS per contract v0.4 §2.1. V14 expects `"5"` — consistent with contract. E10 expects `"6"` — known mismatch.

---

## RULE 6 — HISTORY_INCOMPLETE

Condition:

```python
post["history_complete"] is False
```

Output:

```yaml
verdict: AMBIGUOUS
reason: HISTORY_INCOMPLETE
delta: null
decisive_rule: "6"
```

Rule 6 = HISTORY only. Do not merge with Rule 5.

---

## RULE 7 — PREFIX_CHANGED

```python
n_pre = len(pre["chain"])
n_post = len(post["chain"])
```

Condition:

```python
n_post < n_pre
or post["chain"][:n_pre] != pre["chain"][:n_pre]
```

Output:

```yaml
verdict: MISMATCH
reason: PREFIX_CHANGED
delta: null
decisive_rule: "7"
```

---

## RULE 7a — SNAPSHOT_INCONSISTENT

Condition:

```text
n_post == n_pre
AND chains match
AND tail_fps differ element-wise by idx: role, len, msg_fp
```

Output:

```yaml
verdict: AMBIGUOUS
reason: SNAPSHOT_INCONSISTENT
delta: null
decisive_rule: "7a"
```

Do not apply when `n_post != n_pre`.

---

## RULE 8 — SEND_UNRESOLVED

Condition:

```python
post["send_status"] in {"INTENDED", "AMBIGUOUS"}
```

Output:

```yaml
verdict: AMBIGUOUS
reason: SEND_UNRESOLVED
delta: null
decisive_rule: "8"
```

---

## RULE 9 — DELTA

Condition:

```python
n_post > n_pre
```

New indices: `range(n_pre, n_post)`.

Attribution (per authority files):

```text
A. by: send_nonce
   ref == post["send_nonce"]
   AND post["send_status"] == "CONFIRMED_PRESENT"

OR

B. by: operator_action
   ref matches an action_id in post["operator_actions"]
```

If every new message attributed:

```yaml
verdict: RECOVERED
reason: null
delta: true
decisive_rule: "9"
```

If any new message unattributed:

```yaml
verdict: AMBIGUOUS
reason: UNATTRIBUTED_DELTA
delta: null
decisive_rule: "9"
```

Do not invent attribution mechanism.

---

## RULE 10 — RECOVERED FALLBACK

Condition: no earlier rule fired.

Output:

```yaml
verdict: RECOVERED
reason: null
delta: false
decisive_rule: "10"
```

---

# 6. ALLOWED REASONS

Only:

```text
L0_VIOLATION
NO_EVIDENCE
SESSION_EXPIRED
SESSION_CHALLENGE
DOUBLE_OWNERSHIP
AUTOMATION_FORBIDS_OBSERVATION
CONV_ID_DIFFERS
PATHS_NOT_COMPARABLE
HISTORY_INCOMPLETE
PREFIX_CHANGED
SNAPSHOT_INCONSISTENT
SEND_UNRESOLVED
UNATTRIBUTED_DELTA
null
```

Forbidden examples: `POST_CONVERSATION_CLOSED`, `UNHANDLED_STATE_DIFFERENCE`, `PRE_OBJECT_IS_NULL`, any other.

---

# 7. KNOWN MISMATCH — E10

```yaml
KNOWN_VECTOR_CONTRACT_MISMATCH:
  id: E10
  vector_expect:
    decisive_rule: "6"
    reason: PATHS_NOT_COMPARABLE
  contract_v0_4:
    rule_5: PATHS_NOT_COMPARABLE
    rule_6: HISTORY_INCOMPLETE
  implementation:
    follows_contract: yes
    E10_decisive_rule: "5"
  expected_test_result:
    id: E10
    status: FAIL
    detail: "decisive_rule: got='5' want='6'"
  classification:
    implementation_defect: no
    known_authority_mismatch: yes
  resolution:
    requires_separate_JSON_correction_approval: yes
    authorized_in_this_STEP: no
```

Do not change JSON, runner, or special-case E10. Expected runner result: 31/32.

---

# 8. TEST FILE — DO NOT MODIFY

`test_vectors.py` accepted as-is.

Must continue to verify:

- deterministic double-run;
- no input mutation;
- exact comparison of six authoritative fields;
- order-sensitive `flags`;
- `l0_violation is None` for all 32 vectors;
- separate `L0_GUARD`;
- `rules_trace` on mismatch.

Do not add E10 suppression. Do not change exit code.

---

# 9. COMPLETENESS CHECK — AFTER REWRITE, BEFORE PY_COMPILE

After full rewrite of `verdict_engine.py`, and **before** `py_compile`, verify that the new file is a real implementation, not a skeleton.

## Gate 4 — Hash after

```powershell
Get-FileHash E:\Gemini\Dojo\AI-Collab\verdict_engine.py -Algorithm SHA256 | Select-Object -ExpandProperty Hash
```

Record as `hash_after`.

Required:

```text
hash_after != hash_before
```

If equal:

```text
STOP
REPORT file_changed: no
WAIT
```

## Gate 5 — Skeleton markers absent

```powershell
Select-String `
  -Path E:\Gemini\Dojo\AI-Collab\verdict_engine.py `
  -Pattern 'см\. SPEC v2\.1|остальные rules 2|\$pre\.|\$post\.'
```

Required match count:

```text
0
```

If any match:

```text
STOP
REPORT skeleton_markers_after: [<matched lines>]
WAIT
```

## Gate 6 — Rules 2–9 code presence

Manually inspect `verdict_engine.py` or use grep to confirm each rule has real executable logic, not a comment or placeholder:

```text
Rule 2 — NEEDS_HUMAN
Rule 3 — LOST
Rule 4 — CONV_ID_DIFFERS
Rule 5 — PATHS_NOT_COMPARABLE
Rule 6 — HISTORY_INCOMPLETE
Rule 7 — PREFIX_CHANGED
Rule 7a — SNAPSHOT_INCONSISTENT
Rule 8 — SEND_UNRESOLVED
Rule 9 — DELTA
```

Suggested check:

```powershell
Select-String `
  -Path E:\Gemini\Dojo\AI-Collab\verdict_engine.py `
  -Pattern 'SESSION_EXPIRED|SESSION_CHALLENGE|CONV_ID_DIFFERS|PATHS_NOT_COMPARABLE|HISTORY_INCOMPLETE|PREFIX_CHANGED|SNAPSHOT_INCONSISTENT|SEND_UNRESOLVED|UNATTRIBUTED_DELTA'
```

Expected: each reason identifier appears in executable code, not only comments.

Absence of any required implementation means:

```text
rules_2_to_9_implemented: no
```

### Completeness failure behavior

If any of Gates 4, 5, 6 fails:

```text
STOP
REPORT:
  hash_before
  hash_after
  file_changed
  skeleton_markers_after
  rules_2_to_9_implemented
WAIT
```

Do not run `py_compile`.

Do not run `test_vectors.py`.

Do not start another rewrite in the same operation.

---

# 10. AFTER-FIX GREP — OBSOLETE STRINGS

After Gates 4–6 pass and before `py_compile`, run:

```powershell
Select-String `
  -Path E:\Gemini\Dojo\AI-Collab\verdict_engine.py `
  -Pattern 'UNHANDLED_STATE_DIFFERENCE|POST_CONVERSATION_CLOSED|PRE_OBJECT_IS_NULL'
```

Required match count:

```text
0
```

If nonzero:

```text
STOP
REPORT
WAIT
```

No second rewrite in this operation.

---

# 11. LOCAL VERIFY

## 11.1 Compile

```powershell
cd E:\Gemini\Dojo\AI-Collab
.venv\Scripts\python.exe -m py_compile verdict_engine.py
```

Required:

```text
PASS / exit 0
```

If compile fails:

```text
STOP
REPORT
WAIT
```

No second pass.

## 11.2 Official test run — once

```powershell
.venv\Scripts\python.exe test_vectors.py
```

Expected stdout pattern:

```text
V1 PASS
...
V18 PASS
E1 PASS
...
E9 PASS
E10 FAIL decisive_rule: got='5' want='6'
E11 PASS
E12 PASS
E13 PASS
E14 PASS
L0_GUARD PASS
STEP2 FAIL 31/32
```

Expected process exit code:

```text
1
```

That exit code is acceptable if and only if:

```text
passed == 31
failed_ids == ["E10"]
L0_GUARD == PASS
```

If any additional vector fails:

```text
STOP
REPORT
WAIT
```

No patch.
No second pass.

If `L0_GUARD FAIL`:

```text
STOP
REPORT
WAIT
```

---

# 12. STEP-2 HANDOFF CRITERION

Set:

```yaml
step2_handoff_ready: yes
```

only if:

```yaml
vectors:
  total: 32
  passed: 31
  failed: 1
  failed_ids:
    - E10

l0_guard: PASS

known_mismatch:
  - E10
```

This is a handoff criterion, not self-acceptance.

Samurai must not write:

```text
STEP 2 ACCEPTED
STEP 3 AUTHORIZED
```

Acceptance is external.

---

# 13. FAILURE BEHAVIOR

This operation authorizes one corrective implementation pass only.

Execution sequence:

```text
PREFLIGHT
→ GATE 1 hash before
→ GATE 2 obsolete grep before
→ GATE 3 skeleton grep before
→ FULL REWRITE verdict_engine.py
→ GATE 4 hash after; must differ
→ GATE 5 skeleton markers absent
→ GATE 6 Rules 2–9 implemented
→ AFTER-FIX obsolete grep; zero matches
→ PY_COMPILE
→ ONE OFFICIAL test_vectors.py RUN
→ REPORT
→ STOP
```

No patch cycle after test execution.

No second full rewrite.

No second implementation run.

If a gate before `py_compile` fails:
report the exact point reached and evidence, then STOP.

Do not run `py_compile`.

Do not run tests.

---

# 14. REPORT

Return:

```yaml
STEP2_CORRECTIVE_REPORT:
  build: 001
  step: 2
  spec_version: 2.3

  files_modified:
    - verdict_engine.py

  full_rewrite: yes/no

  venv_present: yes/no

  hash_before: "<sha256>"
  hash_after: "<sha256>"
  file_changed: yes/no

  before_fix_grep:
    obsolete_patterns:
      - UNHANDLED_STATE_DIFFERENCE
      - POST_CONVERSATION_CLOSED
      - PRE_OBJECT_IS_NULL
    obsolete_matches: <N>

    skeleton_patterns:
      - "см. SPEC v2.1"
      - "остальные rules 2"
      - "$pre."
      - "$post."
    skeleton_matches_before: <N>

  after_fix_grep:
    obsolete_matches: <N>
    obsolete_absent: yes/no
    skeleton_markers_after: []
    skeleton_absent: yes/no

  rules_2_to_9_implemented: yes/no

  rule_sources:
    rule_2_session_state: post
    rule_2_flags: post
    rule_3_session_state: post

  rule_map_implemented:
    rule_1: "<one-line>"
    rule_1_I1: "<one-line>"
    rule_1_none_short_circuit: "<one-line>"
    rule_1_restart_only: "<one-line>"
    rule_2: "<one-line>"
    rule_2_reason_priority: "EXPIRED > CHALLENGE > DOUBLE_OWNERSHIP > AUTOMATION_FORBIDS_OBSERVATION"
    rule_3: "<one-line>"
    rule_4: "<one-line>"
    rule_5: "PATHS_NOT_COMPARABLE"
    rule_6: "HISTORY_INCOMPLETE"
    rule_7: "<one-line>"
    rule_7a: "<one-line>"
    rule_8: "<one-line>"
    rule_9: "<one-line>"
    rule_10: "<one-line>"

  l0:
    path_format: "$.text"
    scan_order: "pre -> post"
    hard_pre_rule_guard: yes/no

  output_contract:
    send_status_passed: yes/no
    flags_passed: yes/no
    flags_order_preserved: yes/no

  py_compile:
    status: PASS / FAIL
    exit_code: <int>

  test_vectors:
    executed: yes/no
    total: 32
    passed: <N>
    failed: <N>
    failed_ids: [<list>]
    known_mismatches: [E10]
    exit_code: <int>
    test_output: |
      <full stdout>

  l0_guard: PASS / FAIL / NOT_RUN

  known_mismatch_E10:
    observed: yes/no
    implementation_followed_contract_rule_5: yes/no

  step2_handoff_ready: yes/no

  execution:
    status: PASS / FAIL
    # PASS = authorized corrective operation completed as specified
    # not external STEP-2 acceptance

  evidence:
    status: VERIFIED / INCOMPLETE / CONTRADICTED

  next: STOP -> WAIT_FOR_EXTERNAL_REVIEW
```

Report only observed facts.

Do not rewrite expected values as observed facts.

---

# 15. FORBIDDEN

```text
- modify BUILD_001_STEP2_VECTORS.json
- modify test_vectors.py
- modify authority documents
- STEP 3
- fingerprint recomputation
- invented reasons
- catch-all pre != post
- merge Rule 5 and Rule 6
- bend code to match E10
- special-case E10 to force PASS
- skip E10
- second corrective rewrite
- patch cycle after official run
- run py_compile or test after completeness-check failure
- unrelated refactor / cleanup / rename / migration
```

---

# 16. END PROTOCOL

```text
PREFLIGHT VENV
→ GATE 1 hash before
→ GATE 2 obsolete grep
→ GATE 3 skeleton grep
→ FULL REWRITE verdict_engine.py
→ GATE 4 hash after; must differ
→ GATE 5 skeleton absent
→ GATE 6 Rules 2–9 present
→ AFTER-FIX obsolete grep absent
→ PY_COMPILE
→ RUN test_vectors.py ONCE
→ REPORT
→ STOP
```

One corrective pass.

STEP 3 remains blocked until external acceptance.

---

```yaml
BRIGADIER_STATUS:
  build: 001
  step: 2
  spec_version: 2.3

  deltas_from_v2_2:
    - FULL_REWRITE_definition: replace content, no physical delete required
    - completeness_gates: hash before/after, skeleton absent, rules 2-9 present
    - if_gate_fails: STOP before py_compile and test
    - report_extended:
        - hash_before
        - hash_after
        - file_changed
        - skeleton_markers_after
        - rules_2_to_9_implemented

  unchanged_from_v2_2:
    - rule_5: PATHS
    - rule_6: HISTORY
    - l0_path: "$.text"
    - E10: known mismatch
    - vectors/test runner not touched
    - STEP 3 RED

  expected_handoff_state:
    vectors: "31/32"
    failed_ids: ["E10"]
    l0_guard: PASS
    runner_exit_code: 1

  acceptance:
    owner: external
    route: Grok / Author

  step_3: BLOCKED

  next:
    - Doctor supplies Current_Prompt
    - Samurai executes one corrective pass with completeness gates
    - Samurai reports and stops

  stop: true
```

END OF SPEC v2.3
