# test_vectors.py
import json
import sys
import os
from copy import deepcopy
from datetime import datetime, timezone

# Ensure verdict_engine is importable
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from verdict_engine import verdict, VERDICTS, FORBIDDEN_KEYS

VECTORS_PATH = "BUILD_001_STEP2_VECTORS.json"

def load_vectors():
    if not os.path.exists(VECTORS_PATH):
        print(f"Error: Vectors file not found at {VECTORS_PATH}", file=sys.stderr)
        sys.exit(1)
    with open(VECTORS_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data.get("vectors", [])

def deep_freeze(obj):
    # Creates a deep copy that is JSON serializable and ensures no mutable objects are passed
    # This is crucial for verifying that inputs are not mutated.
    try:
        return json.loads(json.dumps(obj))
    except TypeError as e:
        print(f"Error during deep freeze (input might contain non-serializable types): {e}", file=sys.stderr)
        # Fallback for non-serializable types if needed, though SPEC implies JSON-like structures.
        # For this task, assume standard JSON-serializable types.
        return obj # Might not be truly frozen, but better than crashing.

def check_vector(v):
    pre_orig = v.get("pre")
    post_orig = v.get("post")
    exp = v.get("expect")

    if pre_orig is None and post_orig is None:
        return False, f"Vector {v.get('id', 'N/A')}: Both pre and post are None. Cannot test."
    if exp is None:
        return False, f"Vector {v.get('id', 'N/A')}: Missing 'expect' field."

    # Deep freeze inputs to ensure they are not mutated by the verdict function
    pre_frozen = deep_freeze(pre_orig)
    post_frozen = deep_freeze(post_orig)
    pre_copy_for_mutation_check = deep_freeze(pre_orig)
    post_copy_for_mutation_check = deep_freeze(post_orig)

    try:
        # Run verdict function twice for determinism check
        r1 = verdict(pre_frozen, post_frozen)
        r2 = verdict(pre_frozen, post_frozen)
    except Exception as e:
        return False, f"Error during verdict execution: {e}"

    # 1. Check for non-determinism
    if r1 != r2:
        return False, f"non-deterministic: got={r1!r}, expected_2={r2!r}"

    # 2. Check for input mutation
    # Compare frozen copies with original frozen copies after verdict call
    if pre_frozen != pre_copy_for_mutation_check:
        return False, "input pre mutated"
    if post_frozen != post_copy_for_mutation_check:
        return False, "input post mutated"

    # Compare result with expected output
    mismatches = []
    fields_to_compare = ["verdict", "reason", "delta", "decisive_rule", "send_status", "flags"]
    
    for f in fields_to_compare:
        got = r1.get(f)
        want = exp.get(f)
        if got != want:
            mismatches.append(f"{f}: got={got!r} want={want!r}")
            
    # Check l0_violation specifically
    got_l0 = r1.get("l0_violation")
    want_l0 = exp.get("l0_violation")
    if got_l0 != want_l0:
        mismatches.append(f"l0_violation: got={got_l0!r} want={want_l0!r}")

    # If there are mismatches, format the output with rules_trace
    if mismatches:
        rules_trace = r1.get('rules_trace', [])
        return False, "; ".join(mismatches) + f"; rules_trace={rules_trace!r}"

    return True, ""

def test_l0_guard():
    # Synthetic object with forbidden key "text".
    # Pre-condition: L0 is checked BEFORE Rule 1.
    bad_pre = {"snapshot_id": "pre_l0_test", "kind": "pre", "text": "forbidden content", "conversation_opened": True}
    bad_post = {"snapshot_id": "post_l0_test", "kind": "post", "conversation_opened": False}

    r = verdict(bad_pre, bad_post)

    # Expected L0 violation structure
    expected_l0_violation_path = "$.text"
    expected_verdict = None
    expected_reason = "L0_VIOLATION"
    expected_decisive_rule = None
    expected_rules_trace = []

    if r.get("l0_violation") != expected_l0_violation_path:
        return False, f"l0_violation expected '{expected_l0_violation_path}' but got '{r.get('l0_violation')!r}'"
    if r.get("verdict") != expected_verdict:
        return False, f"verdict should be {expected_verdict!r} on L0 violation, got {r.get('verdict')!r}"
    if r.get("reason") != expected_reason:
        return False, f"reason should be '{expected_reason}', got '{r.get('reason')!r}'"
    if r.get("decisive_rule") != expected_decisive_rule:
        return False, f"decisive_rule should be {expected_decisive_rule!r}, got {r.get('decisive_rule')!r}"
    if r.get("rules_trace") != expected_rules_trace:
        return False, f"rules_trace should be {expected_rules_trace!r}, got {r.get('rules_trace')!r}"
    if r.get("pre_ref") != bad_pre.get("snapshot_id"):
        return False, f"pre_ref mismatch"
    if r.get("post_ref") != bad_post.get("snapshot_id"):
        return False, f"post_ref mismatch"

    return True, ""

def main():
    vectors = load_vectors()
    total_vectors = len(vectors)
    passed_vectors = 0
    failed_vectors_details = []

    for v in vectors:
        vector_id = v.get('id', 'N/A')
        ok, msg = check_vector(v)
        if ok:
            passed_vectors += 1
            print(f"{vector_id} PASS")
        else:
            failed_vectors_details.append(f"{vector_id} FAIL {msg}")
            print(f"{vector_id} FAIL {msg}")

    # Run L0 Guard test separately
    l0_ok, l0_msg = test_l0_guard()
    l0_guard_passed = l0_ok
    if l0_ok:
        print("L0_GUARD PASS")
    else:
        print(f"L0_GUARD FAIL {l0_msg}")

    # Overall status determination
    overall_ok = (passed_vectors == total_vectors) and l0_guard_passed

    # Final output line
    final_status = "PASS" if overall_ok else "FAIL"
    vector_summary = f"{passed_vectors}/{total_vectors}"
    print(f"STEP2 {final_status} {vector_summary}")

    # Exit with code 0 for success, 1 for failure
    sys.exit(0 if overall_ok else 1)

if __name__ == "__main__":
    main()
