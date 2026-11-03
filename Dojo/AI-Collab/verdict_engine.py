# verdict_engine.py – pure function per WEB_SEAT_WS0_OBSERVATION_CONTRACT v0.4 §2.1
# Implements SPEC v2.3 rule map

from typing import Any, Optional, Dict, List
import json
from copy import deepcopy
from datetime import datetime, timezone

VERDICTS = {"RECOVERED", "AMBIGUOUS", "LOST", "NEEDS_HUMAN", "MISMATCH"}

FORBIDDEN_KEYS = {"text", "content", "body", "messages", "prompt", "completion"}

# Allowed reasons as per SPEC v2.3 #6
ALLOWED_REASONS = {
    "L0_VIOLATION",
    "NO_EVIDENCE",
    "SESSION_EXPIRED",
    "SESSION_CHALLENGE",
    "DOUBLE_OWNERSHIP",
    "AUTOMATION_FORBIDS_OBSERVATION",
    "CONV_ID_DIFFERS",
    "PATHS_NOT_COMPARABLE",
    "HISTORY_INCOMPLETE",
    "PREFIX_CHANGED",
    "SNAPSHOT_INCONSISTENT",
    "SEND_UNRESOLVED",
    "UNATTRIBUTED_DELTA",
    None,
}

def check_l0(obj: Any, source: str, path: str = "") -> Optional[str]:
    """Return first forbidden key path, or None."""
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k in FORBIDDEN_KEYS:
                # SPEC v2.3: L0 path format = $.text
                return f"{source}{path}.{k}"
            sub = check_l0(v, source, f"{path}.{k}")
            if sub:
                return sub
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            sub = check_l0(v, source, f"{path}[{i}]")
            if sub:
                return sub
    return None

def _empty_result(pre, post, l0_path=None):
    """Helper to create a result dict, primarily for L0 violation."""
    return {
        "verdict": None if l0_path else None,
        "reason": "L0_VIOLATION" if l0_path else None,
        "delta": None,
        "send_status": None,
        "flags": [],
        "decisive_rule": None,
        "rules_trace": [],
        "pre_ref": (pre or {}).get("snapshot_id") if isinstance(pre, dict) else None,
        "post_ref": (post or {}).get("snapshot_id") if isinstance(post, dict) else None,
        "l0_violation": l0_path,
    }

def _result(pre, post, verdict, reason, delta, decisive_rule, trace):
    """Helper to construct the standard result dictionary."""
    post_dict = post if isinstance(post, dict) else {}
    return {
        "verdict": verdict,
        "reason": reason,
        "delta": delta,
        "send_status": post_dict.get("send_status") if post is not None else None,
        "flags": list(post_dict.get("flags") or []),
        "decisive_rule": decisive_rule,
        "rules_trace": trace,
        "pre_ref": (pre or {}).get("snapshot_id") if isinstance(pre, dict) else None,
        "post_ref": (post or {}).get("snapshot_id") if isinstance(post, dict) else None,
        "l0_violation": None, # L0 is a separate pre-check
    }

def is_valid_timestamp(ts_str: Optional[str]) -> bool:
    """Checks if a string conforms to YYYY-MM-DDTHH:MM:SSZ format."""
    if not isinstance(ts_str, str) or not ts_str.endswith('Z'):
        return False
    try:
        datetime.strptime(ts_str[:-1], '%Y-%m-%dT%H:%M:%S')
        return True
    except ValueError:
        return False

def verdict(pre: Optional[Dict], post: Optional[Dict]) -> Dict:
    """
    Determines the verdict based on pre and post snapshots according to SPEC v2.3 rules.
    Pure function: no side effects, deterministic.
    """
    # --- L0 Guard ---
    l0_violation_path = check_l0(pre, "$pre") # Scan pre first
    if not l0_violation_path:
        l0_violation_path = check_l0(post, "$post") # Then scan post

    if l0_violation_path:
        return _empty_result(pre, post, l0_path=l0_violation_path)

    # --- Initialize result ---
    result = _empty_result(pre, post) # Creates base structure with pre/post_ref, no L0 violation

    # --- Safely extract data for rule checks ---
    pre_chain = pre.get("chain") if isinstance(pre, dict) else []
    post_chain = post.get("chain") if isinstance(post, dict) else []
    pre_conv_opened = pre.get("conversation_opened") if isinstance(pre, dict) else None
    post_conv_opened = post.get("conversation_opened") if isinstance(post, dict) else None
    pre_session_state = pre.get("session_state") if isinstance(pre, dict) else None
    post_session_state = post.get("session_state") if isinstance(post, dict) else None
    pre_conv_id = pre.get("conv_id") if isinstance(pre, dict) else None
    post_conv_id = post.get("conv_id") if isinstance(post, dict) else None
    pre_extraction_path = pre.get("extraction_path") if isinstance(pre, dict) else None
    post_extraction_path = post.get("extraction_path") if isinstance(post, dict) else None
    pre_fp_version = pre.get("fp_version") if isinstance(pre, dict) else None
    post_fp_version = post.get("fp_version") if isinstance(post, dict) else None
    pre_history_complete = pre.get("history_complete") if isinstance(pre, dict) else None
    post_history_complete = post.get("history_complete") if isinstance(post, dict) else None
    pre_restart_epoch = pre.get("restart_epoch") if isinstance(pre, dict) else None
    post_restart_epoch = post.get("restart_epoch") if isinstance(post, dict) else None
    pre_restart_kind = pre.get("restart_kind") if isinstance(pre, dict) else None
    post_restart_kind = post.get("restart_kind") if isinstance(post, dict) else None
    pre_send_attempt_logged = pre.get("send_attempt_logged") if isinstance(pre, dict) else False
    post_send_attempt_logged = post.get("send_attempt_logged") if isinstance(post, dict) else False
    pre_send_status = pre.get("send_status") if isinstance(pre, dict) else None
    post_send_status = post.get("send_status") if isinstance(post, dict) else None
    pre_operator_actions = pre.get("operator_actions") if isinstance(pre, dict) else []
    post_operator_actions = post.get("operator_actions") if isinstance(post, dict) else []
    post_flags = list(post.get("flags") or []) if isinstance(post, dict) else []
    pre_flags = list(pre.get("flags") or []) if isinstance(pre, dict) else []

    # --- Rule 1: NO_EVIDENCE ---    
    is_pre_none = pre is None
    is_post_none = post is None

    # Check snapshot validity (excluding I-1 exception for null content fields)
    snapshot_invalid = False
    invalidity_reason = None

    # SPEC §2.1 / §3 / closed lists check
    allowed_extraction_paths = {"DOM", "API", "MANUAL"}
    allowed_session_states = {"AUTHENTICATED", "CHALLENGE", "EXPIRED", "LOGGED_OUT", "UNKNOWN"}
    allowed_transport_states = {"ATTACHED", "DETACHED", "UNKNOWN"}
    allowed_occupant_states = {"VERIFIED", "UNVERIFIED", "REACHABLE", "UNREACHABLE", "UNKNOWN"}
    allowed_generation_states = {"IDLE", "RUNNING", "GENERATED", "UNKNOWN"}
    allowed_send_statuses = {"NONE", "INTENDED", "CONFIRMED_PRESENT", "AMBIGUOUS", "UNKNOWN"}
    allowed_restart_kinds = {"graceful", "kill", "network", "unknown"}

    if isinstance(post, dict):
        if post.get("send_attempt_logged") is True and post.get("send_status") == "NONE":
            snapshot_invalid = True
            invalidity_reason = "SEND_ATTEMPT_LOGGED_WITH_NONE_STATUS"
        
        if not is_valid_timestamp(post.get("ts_utc")):
            snapshot_invalid = True
            invalidity_reason = "INVALID_TIMESTAMP_FORMAT_FOR_TS_UTC"
        
        post_extraction_path_val = post.get("extraction_path")
        if post_extraction_path_val is not None and post_extraction_path_val not in allowed_extraction_paths:
            snapshot_invalid = True
            invalidity_reason = "EXTRACTION_PATH_OUTSIDE_CLOSED_LIST"
        
        post_session_state_val = post.get("session_state")
        if post_session_state_val is not None and post_session_state_val not in allowed_session_states:
            snapshot_invalid = True
            invalidity_reason = "SESSION_STATE_OUTSIDE_CLOSED_LIST"
        
        post_transport_state_val = post.get("transport_state")
        if post_transport_state_val is not None and post_transport_state_val not in allowed_transport_states:
             snapshot_invalid = True
             invalidity_reason = "TRANSPORT_STATE_OUTSIDE_CLOSED_LIST"

        post_occupant_state_val = post.get("occupant_state")
        if post_occupant_state_val is not None and post_occupant_state_val not in allowed_occupant_states:
             snapshot_invalid = True
             invalidity_reason = "OCCUPANT_STATE_OUTSIDE_CLOSED_LIST"

        post_generation_state_val = post.get("generation_state")
        if post_generation_state_val is not None and post_generation_state_val not in allowed_generation_states:
            snapshot_invalid = True
            invalidity_reason = "GENERATION_STATE_OUTSIDE_CLOSED_LIST"

        post_send_status_val = post.get("send_status")
        if post_send_status_val is not None and post_send_status_val not in allowed_send_statuses:
             snapshot_invalid = True
             invalidity_reason = "SEND_STATUS_OUTSIDE_CLOSED_LIST"

        post_restart_kind_val = post.get("restart_kind")
        if post_restart_kind_val is not None and post_restart_kind_val not in allowed_restart_kinds:
             snapshot_invalid = True
             invalidity_reason = "RESTART_KIND_OUTSIDE_CLOSED_LIST"

    # Rule 1 Condition logic:
    rule1_triggered = False
    if is_pre_none or is_post_none or snapshot_invalid:
        rule1_triggered = True

    # SPEC: I-1 Exception: if post_conv_opened is False, specific nulls are permitted.
    # If the only invalidity was a permitted null, Rule 1 should not trigger.
    # This logic assumes `snapshot_invalid` flags concrete errors, not just permitted nulls.
    # The Restart-Only Clarification implies these specific differences don't trigger Rule 1.
    # For Rule 1, if snapshot_invalid is True, it triggers unless it was *only* due to permitted nulls.
    # The current SPEC phrasing implies Rule 1 triggers if `pre is None or post is None OR snapshot_invalid` is true.
    # The I-1 exception is about *not* flagging nulls as invalid. If other concrete invalidities exist, Rule 1 still triggers.
    # Given the SPEC, the simplest path is if `rule1_triggered` is True, apply Rule 1.

    if rule1_triggered:
        return _result(pre, post, "AMBIGUOUS", "NO_EVIDENCE", None, "1", ["1"])

    # --- Rule 2: NEEDS_HUMAN ---
    rule2_reason = None
    if post_session_state == "EXPIRED":
        rule2_reason = "SESSION_EXPIRED"
    elif post_session_state == "CHALLENGE":
        rule2_reason = "SESSION_CHALLENGE"
    elif "double_ownership" in post_flags:
        rule2_reason = "DOUBLE_OWNERSHIP"
    elif "automation_forbids_observation" in post_flags:
        rule2_reason = "AUTOMATION_FORBIDS_OBSERVATION"

    if rule2_reason:
        return _result(pre, post, "NEEDS_HUMAN", rule2_reason, None, "2", ["2"])

    # --- Rule 3: LOST ---
    # SPEC: Rule 3 fires if post_conv_opened is False. Rule 2 has priority if session_state is EXPIRED.
    # If Rule 2 didn't fire (e.g., session_state was not EXPIRED), and post_conv_opened is False, Rule 3 applies.
    if post_conv_opened is False:
        return _result(pre, post, "LOST", None, None, "3", ["3"])

    # --- Rule 4: CONV_ID_DIFFERS ---
    if pre_conv_id is not None and post_conv_id is not None and pre_conv_id != post_conv_id:
        return _result(pre, post, "MISMATCH", "CONV_ID_DIFFERS", None, "4", ["4"])

    # --- Rule 5: PATHS_NOT_COMPARABLE ---
    paths_not_comparable = (pre_extraction_path != post_extraction_path) or \
                           (pre_fp_version != post_fp_version)

    # --- Rule 6: HISTORY_INCOMPLETE ---
    history_incomplete = post_history_complete is False

    if paths_not_comparable:
        return _result(pre, post, "AMBIGUOUS", "PATHS_NOT_COMPARABLE", None, "5", ["5"])
    elif history_incomplete:
        return _result(pre, post, "AMBIGUOUS", "HISTORY_INCOMPLETE", None, "6", ["6"])

    # --- Rule 7: PREFIX_CHANGED ---
    n_pre = len(pre_chain)
    n_post = len(post_chain)

    prefix_changed = False
    if n_post < n_pre:
        prefix_changed = True
    elif n_post >= n_pre and n_pre > 0:
        if post_chain[:n_pre] != pre_chain[:n_pre]:
            prefix_changed = True
    
    if prefix_changed:
        return _result(pre, post, "MISMATCH", "PREFIX_CHANGED", None, "7", ["7"])

    # --- Rule 7a: SNAPSHOT_INCONSISTENT ---
    if n_post == n_pre and n_post > 0:
        pre_tail_fps = pre.get("tail_fps") if isinstance(pre, dict) else []
        post_tail_fps = post.get("tail_fps") if isinstance(post, dict) else []

        if isinstance(pre_tail_fps, list) and isinstance(post_tail_fps, list):
            if len(pre_tail_fps) == len(post_tail_fps):
                differences_found = False
                for i in range(len(pre_tail_fps)):
                    pre_fps_item = pre_tail_fps[i]
                    post_fps_item = post_tail_fps[i]
                    
                    if isinstance(pre_fps_item, dict) and isinstance(post_fps_item, dict):
                        if pre_fps_item.get("role") != post_fps_item.get("role") or \
                           pre_fps_item.get("len") != post_fps_item.get("len") or \
                           pre_fps_item.get("msg_fp") != post_fps_item.get("msg_fp"):
                            differences_found = True
                            break
                    else: # Non-dict items or type mismatch
                        differences_found = True
                        break
                
                if differences_found:
                    return _result(pre, post, "AMBIGUOUS", "SNAPSHOT_INCONSISTENT", None, "7a", ["7a"])
            # If lengths differ, it's not SNAPSHOT_INCONSISTENT based on this condition.

    # --- Rule 8: SEND_UNRESOLVED ---
    if post_send_status in {"INTENDED", "AMBIGUOUS"}:
        return _result(pre, post, "AMBIGUOUS", "SEND_UNRESOLVED", None, "8", ["8"])

    # --- Rule 9: DELTA ---
    if n_post > n_pre and n_pre >= 0: # n_pre can be 0
        all_attributable = True
        operator_action_ids = {op_action.get("action_id") for op_action in post_operator_actions if isinstance(op_action, dict)}
        
        for i in range(n_pre, n_post):
            found_attribution = False
            current_tail_fps_item = None
            if isinstance(post_tail_fps, list):
                for fps_item in post_tail_fps:
                    if isinstance(fps_item, dict) and fps_item.get("idx") == i:
                        current_tail_fps_item = fps_item
                        break

            if current_tail_fps_item:
                # Check Attribution A: send_nonce
                if post_send_status == "CONFIRMED_PRESENT" and post.get("attributions"):
                    for attr in post.get("attributions", []):
                        if isinstance(attr, dict) and attr.get("idx") == i and \
                           attr.get("by") == "send_nonce" and attr.get("ref") == post.get("send_nonce"):
                            found_attribution = True
                            break
                
                # Check Attribution B: operator action
                if not found_attribution and post.get("attributions"):
                    for attr in post.get("attributions", []):
                        if isinstance(attr, dict) and attr.get("idx") == i and \
                           attr.get("by") == "operator_action":
                            action_ref = attr.get("ref")
                            if action_ref and action_ref in operator_action_ids:
                                found_attribution = True
                                break

            if not found_attribution:
                all_attributable = False
                break

        if all_attributable:
            return _result(pre, post, "RECOVERED", None, True, "9", ["9"])
        else:
            return _result(pre, post, "AMBIGUOUS", "UNATTRIBUTED_DELTA", None, "9", ["9"])

    # --- Rule 10: RECOVERED FALLBACK ---
    # If no earlier rule fired.
    # SPEC explicitly states delta: false for rule 10.
    # If there's a difference but no rule caught it, it's still RECOVERED with delta: false.
    result = _result(pre, post, "RECOVERED", None, False, "10", ["10"])
    
    # SPEC v2.3 rule map is respected for rule 5/6 and L0 path format.
    
    return result
