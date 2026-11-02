# SPEC.md — BUILD 001 / STEP 2 — VERDICT ENGINE

```yaml
BUILD: 001
STEP: 2
NAME: VERDICT_ENGINE_CORRECTIVE
VERSION: 2.1
STATUS: READY_FOR_SAMURAI
DATE: 2026-10-28

AUTHORITY_ORDER:
  1: WEB_SEAT_WS0_OBSERVATION_CONTRACT.md v0.4 §2.1 + §7
  2: BUILD_001_STEP2_STEP3_SPEC.md §A (I-1…I-7)
  3: BUILD_001_STEP2_VECTORS.json expect (do not edit)

PATCHES_APPLIED:
  - PATCH_1: PATHS_NOT_COMPARABLE + HISTORY_INCOMPLETE → decisive_rule "6"
  - PATCH_2: rule 1 does not catch I-1 null-fields; restart-only differences are not invalidity
  - PATCH_3: L0 remains a hard pre-rule guard
  - PATCH_4: output schema and delta semantics are explicit
```

---

## OBJECTIVE

Correct `verdict(pre, post)` so that it implements the authoritative rule-map deterministically and passes:

- all 32 authoritative vectors;
- separate `L0_GUARD`.

This is a **corrective continuation of STEP 2**.

Do not implement STEP 3.

---

## ROOT CAUSE

```yaml
problems:
  - rule_5_is_catch_all
  - false_rule_1_on_conversation_closed
  - session_state_ignored
  - send_status_not_passed
  - restart_epoch_kind_treated_as_state_difference
  - invented_reasons
```

---

## FILES

```text
MODIFY:
  E:\Gemini\Dojo\AI-Collab\verdict_engine.py

READ / EXECUTE, DO NOT MODIFY:
  E:\Gemini\Dojo\AI-Collab\test_vectors.py
  E:\Gemini\Dojo\AI-Collab\BUILD_001_STEP2_VECTORS.json

READ AS AUTHORITY, DO NOT MODIFY:
  E:\Gemini\Dojo\AI-Collab\BUILD_001_STEP2_STEP3_SPEC.md
  E:\Gemini\Dojo\AI-Collab\WEB_SEAT_WS0_OBSERVATION_CONTRACT.md
  E:\Gemini\Dojo\AI-Collab\AI_COLAB_2_BUILD_CONTRACT_001.md
```

Do not touch unrelated project files.

---

## PREFLIGHT

Before modifying `verdict_engine.py`, verify:

```powershell
Test-Path E:\Gemini\Dojo\AI-Collab\.venv\Scripts\python.exe
```

Required:

```text
True
```

If `.venv\Scripts\python.exe` does not exist:

```text
STOP
REPORT VENV_MISSING
WAIT
```

Do not:

- install packages;
- create another venv;
- substitute another Python interpreter.

---

# IMPLEMENTATION

## 1. PURE FUNCTION

`verdict(pre, post)` remains pure.

Forbidden:

- I/O;
- filesystem access;
- network;
- browser;
- time;
- random;
- global mutable state;
- mutation of `pre`;
- mutation of `post`.

Same input must produce the same output.

---

## 2. OUTPUT CONTRACT

Every call returns a dict with exactly these logical fields:

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

For normal non-L0 execution:

```text
l0_violation = null
pre_ref = pre.snapshot_id if available else null
post_ref = post.snapshot_id if available else null
```

### send_status

```yaml
if post is not None:
  send_status: post.get("send_status")
else:
  send_status: null
```

The literal string `"NONE"` remains `"NONE"`.

Do not convert it to null.

### flags

```yaml
if post is not None:
  flags: list(post.get("flags") or [])
else:
  flags: []
```

Preserve order exactly.

Do not sort.

Do not deduplicate.

---

# 3. L0 — HARD PRE-RULE GUARD

L0 executes **before rule 1**.

Forbidden keys:

```python
FORBIDDEN_KEYS = {
    "text",
    "content",
    "body",
    "messages",
    "prompt",
    "completion",
}
```

`check_l0()` recursively scans nested dictionaries/lists.

Evaluation order:

1. `pre`
2. `post`

If more than one forbidden key exists, return the first path found by deterministic traversal.

The path must identify its source, for example:

```text
$pre.text
$post.foo[0].content
```

If L0 finds a forbidden key:

```yaml
l0_violation: "<path>"
verdict: null
reason: L0_VIOLATION
delta: null
send_status: null
flags: []
decisive_rule: null
rules_trace: []
pre_ref: <snapshot_id or null>
post_ref: <snapshot_id or null>
```

Then:

> **DO NOT APPLY RULES 1–10.**

There is no mode in which a normal verdict is calculated together with an L0 violation.

For all 32 authoritative vectors:

```text
l0_violation = null
```

---

# 4. RULE TRACE

For normal non-L0 execution, `rules_trace` is diagnostic only.

Append rule identifiers in actual evaluation order.

Example:

```python
["1", "2", "3", "4", "6"]
```

The decisive rule is included as the final trace entry.

If evaluation reaches rule 10:

```python
[..., "10"]
```

`rules_trace` does not change rule semantics.

It is not one of the six authoritative vector comparison fields.

---

# 5. RULE MAP

First matching rule wins.

Evaluation order:

```text
1 → 2 → 3 → 4 → 6 → 7 → 7a → 8 → 9 → 10
```

There is **no separate rule 5**.

---

## RULE 1 — NO_EVIDENCE

### Condition

Rule 1 fires if:

```text
pre is None
OR
post is None
```

or a snapshot is invalid under the authoritative validity contract, including:

```text
- missing mandatory field, except I-1 permitted null content fields;
- closed-list value outside the allowed set;
- post seat_id != pre seat_id;
- post binding_id != pre binding_id;
- post ts_utc <= pre ts_utc;
- invalid required ts_utc format;
- send_attempt_logged == true AND send_status == "NONE".
```

### Output

```yaml
verdict: AMBIGUOUS
reason: NO_EVIDENCE
delta: null
decisive_rule: "1"
```

---

### I-1 EXCEPTION

If:

```python
post["conversation_opened"] is False
```

the following content fields may be `None` where permitted by the authoritative contract:

```text
conv_id
chain
tail_fps
n_msgs
extraction_path
fp_version
history_complete
```

Those null values alone:

- do not make the snapshot invalid;
- do not trigger rule 1;
- do not imply RECOVERED.

Continue normal rule evaluation.

---

### RESTART-ONLY CLARIFICATION

If both snapshots are otherwise valid and the only pre/post state differences are:

```text
restart_epoch
and/or
restart_kind
```

those differences:

- do not trigger rule 1;
- do not create an invented reason;
- do not create a separate rule;
- do not create rule 5.

Continue normal evaluation through rules 2–9.

If none of rules 2–9 fires, rule 10 wins.

Do **not** jump directly to rule 10 before checking rules 2–9.

---

## RULE 2 — NEEDS_HUMAN

### Conditions

Any of:

```text
session_state == EXPIRED
session_state == CHALLENGE
double_ownership flag present
automation_forbids_observation flag present
```

### Deterministic reason priority

If more than one rule-2 condition is simultaneously true, choose the first true condition in this order:

```text
1. session_state == EXPIRED
2. session_state == CHALLENGE
3. double_ownership
4. automation_forbids_observation
```

### Output

```yaml
verdict: NEEDS_HUMAN
delta: null
decisive_rule: "2"
```

Reason:

```yaml
EXPIRED:
  reason: SESSION_EXPIRED

CHALLENGE:
  reason: SESSION_CHALLENGE

double_ownership:
  reason: DOUBLE_OWNERSHIP

automation_forbids_observation:
  reason: AUTOMATION_FORBIDS_OBSERVATION
```

---

## RULE 3 — LOST

### Condition

```text
session_state == AUTHENTICATED
AND
post["conversation_opened"] == false
```

### Output

```yaml
verdict: LOST
reason: null
delta: null
decisive_rule: "3"
```

---

## RULE 4 — CONVERSATION MISMATCH

### Condition

```text
pre["conv_id"] is not None
AND
post["conv_id"] is not None
AND
pre["conv_id"] != post["conv_id"]
```

### Output

```yaml
verdict: MISMATCH
reason: CONV_ID_DIFFERS
delta: null
decisive_rule: "4"
```

---

## RULE 6 — PATHS / HISTORY

Rule 5 does not exist as a separate rule.

### Condition A — paths not comparable

```text
pre["extraction_path"] != post["extraction_path"]
OR
pre["fp_version"] != post["fp_version"]
```

### Condition B — incomplete history

```text
post["history_complete"] == false
```

### Priority inside rule 6

If A and B are both true:

```text
A wins.
```

### Output for A

```yaml
verdict: AMBIGUOUS
reason: PATHS_NOT_COMPARABLE
delta: null
decisive_rule: "6"
```

### Output for B only

```yaml
verdict: AMBIGUOUS
reason: HISTORY_INCOMPLETE
delta: null
decisive_rule: "6"
```

---

## RULE 7 — PREFIX_CHANGED

Evaluate only when the required `chain` values are available as lists.

```python
n_pre = len(pre["chain"])
n_post = len(post["chain"])
```

### Condition

```text
n_post < n_pre
OR
post["chain"][:n_pre] != pre["chain"][:n_pre]
```

### Output

```yaml
verdict: MISMATCH
reason: PREFIX_CHANGED
delta: null
decisive_rule: "7"
```

---

## RULE 7a — SNAPSHOT_INCONSISTENT

Evaluate only when:

```text
n_post == n_pre
AND
chains match
```

### Condition

`tail_fps` differ element-wise by:

```text
role
len
msg_fp
```

### Output

```yaml
verdict: AMBIGUOUS
reason: SNAPSHOT_INCONSISTENT
delta: null
decisive_rule: "7a"
```

---

## RULE 8 — SEND_UNRESOLVED

### Condition

```python
post["send_status"] in {"INTENDED", "AMBIGUOUS"}
```

### Output

```yaml
verdict: AMBIGUOUS
reason: SEND_UNRESOLVED
delta: null
decisive_rule: "8"
```

---

## RULE 9 — DELTA

Evaluate when chains are available and:

```text
n_post > n_pre
```

New-message indices:

```python
range(n_pre, n_post)
```

Every new message must be attributable.

### Accepted attribution A — send_nonce

For the new index:

```yaml
by: send_nonce
ref: post["send_nonce"]
```

and:

```python
post["send_status"] == "CONFIRMED_PRESENT"
```

### Accepted attribution B — operator action

For the new index:

```yaml
by: operator_action
ref: <action_id>
```

where `<action_id>` exists in:

```python
post["operator_actions"]
```

### If every new message is attributed

```yaml
verdict: RECOVERED
reason: null
delta: true
decisive_rule: "9"
```

### If at least one new message is not attributed

```yaml
verdict: AMBIGUOUS
reason: UNATTRIBUTED_DELTA
delta: null
decisive_rule: "9"
```

---

## RULE 10 — RECOVERED

Condition:

```text
No earlier rule fired.
```

Output:

```yaml
verdict: RECOVERED
reason: null
delta: false
decisive_rule: "10"
```

---

# 6. ALLOWED REASONS

The only permitted `reason` values are:

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

Forbidden examples include:

```text
POST_CONVERSATION_CLOSED
UNHANDLED_STATE_DIFFERENCE
PRE_OBJECT_IS_NULL
```

No reason absent from the allowed list may be invented.

---

# 7. TEST FILE

`test_vectors.py` is already accepted for this corrective pass.

Do not modify it.

It must continue to verify:

- deterministic double-run;
- no input mutation;
- exact comparison of six fields;
- order-sensitive `flags`;
- `l0_violation is None` for the 32 vectors;
- separate `L0_GUARD`;
- `rules_trace` on mismatch.

---

# LOCAL VERIFY

## One corrective pass only

```powershell
cd E:\Gemini\Dojo\AI-Collab

.venv\Scripts\python.exe -m py_compile verdict_engine.py

.venv\Scripts\python.exe test_vectors.py
```

Expected:

```text
V1 PASS
...
E14 PASS
L0_GUARD PASS
STEP2 PASS 32/32
```

Expected exit code:

```text
0
```

---

## FAIL BEHAVIOR

This corrective authorization includes **one verification run**.

If any authoritative vector fails:

```text
STOP
```

Do not:

- modify the vector;
- modify `test_vectors.py`;
- invent another reason;
- immediately patch `verdict_engine.py` again;
- perform another corrective cycle.

Report:

- vector id;
- mismatched fields;
- got;
- want;
- `rules_trace`.

Then:

```text
WAIT_FOR_GROK
```

If `L0_GUARD` fails:

```text
STOP → REPORT → WAIT_FOR_GROK
```

---

# REPORT

```yaml
STEP2_CORRECTIVE_REPORT:
  files_modified:
    - verdict_engine.py

  venv_present: yes/no

  rule_map_implemented:
    rule_1: "<one-line condition>"
    rule_1_I1_exception: "<one line>"
    rule_1_restart_only_clarification: "<one line>"
    rule_2: "<one line>"
    rule_2_reason_priority: "EXPIRED > CHALLENGE > DOUBLE_OWNERSHIP > AUTOMATION_FOR