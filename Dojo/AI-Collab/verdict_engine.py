# verdict_engine.py
# Pure function. No I/O, no time, no network, no global state.

from typing import Any, Optional, Dict, List
import json
from copy import deepcopy

VERDICTS = {"RECOVERED", "AMBIGUOUS", "LOST", "NEEDS_HUMAN", "MISMATCH"}

FORBIDDEN_KEYS = {"text", "content", "body", "messages", "prompt", "completion"}


def check_l0(obj: Any, path: str = "$") -> List[str]:
    """
    Recursively scan obj for forbidden keys.
    Returns list of paths where forbidden key found, or empty list.
    """
    if obj is None:
        return []

    if isinstance(obj, dict):
        paths = []
        for key, value in obj.items():
            if key in FORBIDDEN_KEYS:
                paths.append(f"{path}.{key}")
            paths.extend(check_l0(value, f"{path}.{key}"))
        return paths
    elif isinstance(obj, list):
        paths = []
        for i, item in enumerate(obj):
            paths.extend(check_l0(item, f"{path}[{i}]"))
        return paths
    else:
        return []


def verdict(pre: Optional[Dict], post: Optional[Dict]) -> Dict:
    """
    Returns:
      {
        "verdict": <one of VERDICTS or None on L0 violation>,
        "reason": <str or None>,
        "delta": <bool or None>,
        "send_status": <str or None>,
        "flags": <list>,
        "decisive_rule": <str or None>,
        "rules_trace": <list of str>,
        "pre_ref": <snapshot_id or None>,
        "post_ref": <snapshot_id or None>,
        "l0_violation": <str or None>   # path if L0 key found
      }

    Pure: no mutation of pre/post; same input -> same output.
    """
    # --- L0 Guard ---
    l0_violations_pre = check_l0(pre)
    l0_violations_post = check_l0(post)
    l0_violations = l0_violations_pre + l0_violations_post

    if l0_violations:
        # Per SPEC, use first violation path, verdict null, reason "L0_VIOLATION"
        violation_path = l0_violations[0]
        return {
            "verdict": None,
            "reason": "L0_VIOLATION",
            "delta": None,
            "send_status": None,
            "flags": [],
            "decisive_rule": None,
            "rules_trace": [],
            "pre_ref": pre.get("snapshot_id") if isinstance(pre, dict) else None,
            "post_ref": post.get("snapshot_id") if isinstance(post, dict) else None,
            "l0_violation": violation_path
        }

    # --- Initializing result structure ---
    result = {
        "verdict": None,
        "reason": None,
        "delta": None,
        "send_status": None,
        "flags": [],
        "decisive_rule": None,
        "rules_trace": [],
        "pre_ref": pre.get("snapshot_id") if isinstance(pre, dict) else None,
        "post_ref": post.get("snapshot_id") if isinstance(post, dict) else None,
        "l0_violation": None # L0 already checked
    }

    # --- Rule Interpretations from §A of BUILD_001_STEP2_STEP3_SPEC.md ---
    # I-1: post["conversation_opened"] == False -> content fields can be None, rule 1 doesn't fail on their absence.
    # I-2: chain prefix check. len(post["chain"]) < n_pre -> rule 7 (PREFIX_CHANGED).
    # I-3: rule 7a applies only if n_post == n_pre.
    # I-4: fingerprints not recomputed.
    # I-5: delta attribution via attributions (by=send_nonce / by=operator_action).
    # I-6: flags double_ownership, automation_forbids_observation, model_label_changed, ui_variant_changed pass through.
    # I-7: invalidity by §2.1 item 1 + closed lists §1.1 + send_attempt_logged=true with send_status=NONE + ts format YYYY-MM-DDTHH:MM:SSZ.

    # --- Rules 1-10 (apply in order, first match wins) ---
    # Rule 1: Conversation state changes
    pre_conv_opened = pre.get("conversation_opened") if isinstance(pre, dict) else None
    post_conv_opened = post.get("conversation_opened") if isinstance(post, dict) else None
    
    if post_conv_opened is False and pre_conv_opened is not False: # Rule 1 condition
        result["verdict"] = "RECOVERED"
        result["reason"] = "POST_CONVERSATION_CLOSED"
        result["decisive_rule"] = "1"
        result["rules_trace"].append("1: POST_CONVERSATION_CLOSED")
        return result

    # Rule 2: State is LOST
    if post is None and pre is not None:
        result["verdict"] = "LOST"
        result["reason"] = "POST_OBJECT_IS_NULL"
        result["decisive_rule"] = "2"
        result["rules_trace"].append("2: POST_OBJECT_IS_NULL")
        return result

    # Rule 3: State is AMBIGUOUS
    if post is not None and pre is None: # This implies initial state is ambiguous (e.g., post exists but pre doesn't)
        result["verdict"] = "AMBIGUOUS"
        result["reason"] = "PRE_OBJECT_IS_NULL"
        result["decisive_rule"] = "3"
        result["rules_trace"].append("3: PRE_OBJECT_IS_NULL")
        return result

    # Rule 4: State is MISMATCH (general structural difference, not covered by specific rules)
    # This rule implies a significant structural difference that doesn't fall into other categories.
    # For now, we'll use it as a catch-all if post differs from pre and no other rule applies.
    # This might need refinement based on SPEC §2.1 for actual structural comparison.
    # A simple check for deep equality will be used as a proxy.
    if pre != post:
        # Placeholder for structural mismatch analysis. For now, assume if not caught by other rules, it's MISMATCH.
        # This might be too broad. Refinement needed if SPEC details structural diffs.
        pass # Deferring specific structural comparison logic.

    # Rule 5: State is NEEDS_HUMAN
    # This rule typically involves conditions that require manual intervention or more complex logic not automatable by the function.
    # Examples could be specific error codes, or states indicating an unrecoverable automated process.
    # For now, we'll use a placeholder logic if no other rule matches and there's a difference.
    if pre != post and not result["verdict"]: # If different and no verdict yet
        result["verdict"] = "NEEDS_HUMAN"
        result["reason"] = "UNHANDLED_STATE_DIFFERENCE"
        result["decisive_rule"] = "5"
        result["rules_trace"].append("5: UNHANDLED_STATE_DIFFERENCE")
        return result

    # Rule 6: Delta calculation and attributions (I-5)
    # This rule focuses on whether a change (delta) occurred and how it was attributed.
    # Delta is true if pre != post.
    # Attribution logic is complex and might need more SPEC details.
    # For now, just setting delta based on object inequality.
    is_delta = (pre != post)
    result["delta"] = is_delta

    # Rule 7: Chain prefix check (I-2)
    pre_chain = pre.get("chain") if isinstance(pre, dict) else []
    post_chain = post.get("chain") if isinstance(post, dict) else []
    n_pre = len(pre_chain)
    n_post = len(post_chain)

    if n_post < n_pre:
        result["verdict"] = "MISMATCH"
        result["reason"] = "PREFIX_CHANGED"
        result["decisive_rule"] = "7"
        result["rules_trace"].append("7: PREFIX_CHANGED")
        return result

    # Rule 7a: Applies only if n_post == n_pre (I-3)
    if n_post == n_pre and n_post > 0:
        # Check if post_chain[:n_pre] == pre_chain[:n_pre]
        if post_chain[:n_pre] != pre_chain[:n_pre]:
            result["verdict"] = "MISMATCH"
            result["reason"] = "CHAIN_PREFIX_MISMATCH_POST_EQ_PRE_LEN"
            result["decisive_rule"] = "7a"
            result["rules_trace"].append("7a: CHAIN_PREFIX_MISMATCH_POST_EQ_PRE_LEN")
            return result
    
    # Rule 8: send_attempt_logged=true with send_status=NONE (I-7)
    pre_send_attempt_logged = pre.get("send_attempt_logged") if isinstance(pre, dict) else False
    pre_send_status = pre.get("send_status") if isinstance(pre, dict) else None
    post_send_attempt_logged = post.get("send_attempt_logged") if isinstance(post, dict) else False
    post_send_status = post.get("send_status") if isinstance(post, dict) else None

    if pre_send_attempt_logged is True and pre_send_status == "NONE" and \
       post_send_attempt_logged is True and post_send_status == "NONE":
        result["verdict"] = "MISMATCH"
        result["reason"] = "SEND_ATTEMPT_LOGGED_WITH_NONE_STATUS_PERSISTS"
        result["decisive_rule"] = "8"
        result["rules_trace"].append("8: SEND_ATTEMPT_LOGGED_WITH_NONE_STATUS_PERSISTS")
        return result

    # Rule 9: Validity of timestamp format YYYY-MM-DDTHH:MM:SSZ (I-7)
    def is_valid_timestamp(ts_str: Optional[str]) -> bool:
        if not isinstance(ts_str, str):
            return False
        if not ts_str.endswith('Z'):
            return False
        try:
            datetime.strptime(ts_str[:-1], '%Y-%m-%dT%H:%M:%S') # Check format excluding 'Z'
            return True
        except ValueError:
            return False

    # Applying to relevant fields like 'timestamp', 'event_ts', 'created_at', etc.
    # Need to identify all fields that should conform to this TS format from the contract.
    # For now, assuming 'timestamp' and 'event_ts' if they exist in either pre or post.
    timestamp_fields = ["timestamp", "event_ts", "created_at", "updated_at"]
    
    all_obj_keys = set()
    if isinstance(pre, dict): all_obj_keys.update(pre.keys())
    if isinstance(post, dict): all_obj_keys.update(post.keys())

    for field in timestamp_fields:
        if field in all_obj_keys:
            ts_pre = pre.get(field) if isinstance(pre, dict) else None
            ts_post = post.get(field) if isinstance(post, dict) else None
            
            if not is_valid_timestamp(ts_pre) and not is_valid_timestamp(ts_post):
                # If neither pre nor post has a valid timestamp for this field, no violation.
                pass
            elif not is_valid_timestamp(ts_post):
                # If post has an invalid timestamp, it's a violation.
                result["verdict"] = "MISMATCH"
                result["reason"] = f"INVALID_TIMESTAMP_FORMAT_FOR_{field.upper()}"
                result["decisive_rule"] = "9"
                result["rules_trace"].append(f"9: INVALID_TIMESTAMP_FORMAT_FOR_{field.upper()}")
                return result

    # Rule 10: Handling of closed lists (I-7)
    # This rule implies checking against predefined closed lists.
    # Example: SPEC mentions "closed lists §1.1". This would require knowing those lists.
    # Without explicit lists, this rule is hard to implement. Assuming standard checks for now.
    # If a field is expected to be in a closed list and isn't, it's a MISMATCH.

    # --- Flags handling (I-6) ---
    # Pass through specific flags if they exist and match conditions.
    # These are not verdict-determining rules but part of the output.
    
    # Flag: double_ownership
    if isinstance(post, dict) and post.get("double_ownership") is True:
        result["flags"].append("double_ownership")

    # Flag: automation_forbids_observation
    if isinstance(post, dict) and post.get("automation_forbids_observation") is True:
        result["flags"].append("automation_forbids_observation")
        
    # Flag: model_label_changed
    pre_model_label = pre.get("model_label") if isinstance(pre, dict) else None
    post_model_label = post.get("model_label") if isinstance(post, dict) else None
    if pre_model_label != post_model_label and post_model_label is not None:
        result["flags"].append("model_label_changed")

    # Flag: ui_variant_changed
    pre_ui_variant = pre.get("ui_variant") if isinstance(pre, dict) else None
    post_ui_variant = post.get("ui_variant") if isinstance(post, dict) else None
    if pre_ui_variant != post_ui_variant and post_ui_variant is not None:
        result["flags"].append("ui_variant_changed")

    # --- Delta attribution (I-5) ---
    # Logic for attributing delta via 'attributions' field.
    # This requires parsing 'attributions' which is likely a list of dicts.
    # For now, assume delta is set if pre != post. Attribution details would go into rules_trace or specific fields if SPEC detailed them.

    # --- Final verdict if no rule matched ---
    if result["verdict"] is None: # No specific rule triggered a verdict
        if pre == post: # If objects are identical and no rule triggered, consider it RECOVERED with no delta.
            result["verdict"] = "RECOVERED"
            result["delta"] = False
            result["reason"] = "STATE_UNCHANGED"
            result["decisive_rule"] = "DEFAULT_UNCHANGED"
            result["rules_trace"].append("DEFAULT_UNCHANGED: STATE_UNCHANGED")
        else: # If objects differ but no rule applied, it falls to NEEDS_HUMAN or MISMATCH as per Rule 5 or a more detailed structural analysis.
            # Given the SPEC's "first match wins" and the rules provided,
            # if we reach here and objects differ, it implies an unhandled difference.
            # Rule 5: NEEDS_HUMAN for unhandled differences.
            result["verdict"] = "NEEDS_HUMAN"
            result["reason"] = "UNHANDLED_DIFFERENCE_AFTER_ALL_RULES"
            result["decisive_rule"] = "DEFAULT_UNHANDLED"
            result["rules_trace"].append("DEFAULT_UNHANDLED: UNHANDLED_DIFFERENCE_AFTER_ALL_RULES")
            result["delta"] = True # A difference implies delta occurred.
    
    # Ensure 'send_status' is set if it's part of the output, even if not determining verdict.
    # Example: if post has send_status, include it.
    if isinstance(post, dict) and "send_status" in post:
        result["send_status"] = post["send_status"]
    elif isinstance(pre, dict) and "send_status" in pre: # Carry over if it exists in pre and not post
        result["send_status"] = pre["send_status"]
        
    # Ensure 'pre_ref' and 'post_ref' are populated if available
    if isinstance(pre, dict) and "snapshot_id" in pre:
        result["pre_ref"] = pre["snapshot_id"]
    if isinstance(post, dict) and "snapshot_id" in post:
        result["post_ref"] = post["snapshot_id"]

    return result
