# src/smoke_bridge.py

import os
import re
import yaml
from datetime import datetime

# Import real, canonical implementations as required by STEP.md
from src.parser.protected_span_parser import ProtectedSpanParser
from src.parser.source_parser import SourceParser
from src.parser.prompt_map_parser import PromptMapParser
from src.parser.source_prompt_map_validator import SourcePromptMapValidator
from src.loader import load_model

# --- Configuration ---
SOURCE_MANUSCRIPT_PATH = "Input/TEST_SOURCE_MANUSCRIPT.md"
PROMPT_MAP_PATH = "Input/TEST_PROMPT_MAP.yaml"
GEMMA_KERNEL_PATH = "Gemma.md"
WRITER_CONFIG_PATH = "config/writer_config.yaml"

OUTPUT_PAYLOAD_PATH = "Output/SMOKE_MP-0101.payload.txt"
OUTPUT_GENERATED_PATH = "Output/SMOKE_MP-0101.md"
OUTPUT_RUN_LOG_PATH = "Output/SMOKE_MP-0101.run.log"

SELECTED_MARKER = "MP:0101"
FOLLOWING_MARKER = "MP:0102"
P01_01_PROTECTED_SPAN_ID = "P01_01"

# --- Helper Functions ---
def log_message(message: str, log_file_path: str):
    """Appends a message to the run log file."""
    try:
        with open(log_file_path, "a", encoding="utf-8") as f:
            f.write(message + "\n")
    except Exception as e:
        print(f"Error writing to log file {log_file_path}: {e}")

def read_file_content(file_path: str) -> str:
    """Reads file content, handling potential encoding issues."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Required input file not found: {file_path}")
    except Exception as e:
        raise IOError(f"Error reading file {file_path}: {e}")

def save_file_content(file_path: str, content: str):
    """Saves content to a file."""
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

# --- Main Execution Logic ---
def run_smoke_bridge():
    run_type = "NON_PRODUCTION_SMOKE"
    operation_id = "PHASE1_SMOKE_BRIDGE_V1_1"
    selected_marker = SELECTED_MARKER
    following_marker = FOLLOWING_MARKER
    protected_span_id = P01_01_PROTECTED_SPAN_ID

    # Ensure output directory exists
    os.makedirs(os.path.dirname(OUTPUT_PAYLOAD_PATH), exist_ok=True)
    os.makedirs(os.path.dirname(OUTPUT_GENERATED_PATH), exist_ok=True)
    os.makedirs(os.path.dirname(OUTPUT_RUN_LOG_PATH), exist_ok=True)

    # Initialize log file
    log_file = OUTPUT_RUN_LOG_PATH
    with open(log_file, "w", encoding="utf-8") as f:
        f.write(f"RUN_TYPE={run_type}\n")
        f.write(f"Operation_ID={operation_id}\n")
        f.write(f"SELECTED_MARKER={selected_marker}\n")
        f.write(f"Date: {datetime.now().isoformat()}\n")
        f.write("--- Execution Start ---\n")

    preflight_results = {
        "ProtectedSpanParser": "FAIL",
        "SourceParser": "FAIL",
        "PromptMapParser": "FAIL",
        "SourcePromptMapValidator": "FAIL",
        "BlockBoundary": "FAIL",
        "PayloadStructure": "FAIL",
    }
    payload_emissions = {
        "CACHE_EMITTED": False,
        "PROTECTED_CONTEXT_EMITTED": False,
        "STRUCTURAL_CONTEXT_EMITTED": False,
        "RUNTIME_CONTRACT_OVERRIDE": False,
    }
    generation_params = {
        "MODEL": "N/A",
        "N_CTX": "N/A",
        "MAX_TOKENS": "N/A",
        "TEMPERATURE": "N/A",
        "TOP_P": "N/A",
        "CREATE_CHAT_COMPLETION_CALLS": 0,
        "OUTPUT_LENGTH": "N/A",
        "OUTPUT_NON_EMPTY": False,
    }
    generation_status = "FAILURE"
    smoke_status = "FAILURE"

    try:
        # 1. Load Complete SOURCE
        log_message("STEP 1: Loading complete SOURCE manuscript.", log_file)
        source_manuscript_content = read_file_content(SOURCE_MANUSCRIPT_PATH)

        # 2. Protected-First Parse
        log_message("STEP 2: Performing Protected-First Parse.", log_file)
        protected_parser = ProtectedSpanParser()
        protected_spans, slotted_source = protected_parser.parse(source_manuscript_content)

        # Preflight check 1: ProtectedSpanParser success
        detected_p01_01 = any(span.id == protected_span_id for span in protected_spans)
        
        # Verify raw body is absent from slotted_source
        p01_01_span = next((span for span in protected_spans if span.id == protected_span_id), None)
        raw_protected_body_absent = (p01_01_span.content not in slotted_source) if p01_01_span else False
        
        # Verify slot representation is present in slotted_source
        slot_representation_present = f"⟦MP_PROTECTED:{protected_span_id}⟧" in slotted_source

        if detected_p01_01 and raw_protected_body_absent and slot_representation_present:
            preflight_results["ProtectedSpanParser"] = "PASS"
            log_message("ProtectedSpanParser: PASS", log_file)
        else:
            log_message(f"ProtectedSpanParser: FAIL. Got: Detected P01_01: {detected_p01_01}, Raw body absent: {raw_protected_body_absent}, Slot present: {slot_representation_present}", log_file)
            raise ValueError("ProtectedSpanParser preflight failed.")

        # 3. Build SOURCE Marker Graph
        log_message("STEP 3: Building SOURCE Marker Graph.", log_file)
        source_parser = SourceParser()
        marker_graph = source_parser.parse(slotted_source)

        # Preflight check 2: SourceParser output
        expected_markers = [selected_marker, following_marker, "MP:0103"]
        marker_graph_ids = [m.marker_id for m in marker_graph]
        
        if len(marker_graph_ids) >= len(expected_markers) and marker_graph_ids[:len(expected_markers)] == expected_markers:
            preflight_results["SourceParser"] = "PASS"
            log_message(f"SourceParser: PASS. Found markers: {marker_graph_ids[:len(expected_markers)]}", log_file)
        else:
            log_message(f"SourceParser: FAIL. Expected markers (prefix): {expected_markers}, Got: {marker_graph_ids}", log_file)
            raise ValueError("SourceParser marker graph preflight failed.")

        # 4. Parse PROMPT_MAP
        log_message("STEP 4: Parsing PROMPT_MAP.", log_file)
        prompt_map_data = PromptMapParser().parse(PROMPT_MAP_PATH)

        # Preflight check 4: PromptMapParser for MP:0101
        mp0101_prompt_data = prompt_map_data.get(selected_marker)
        long_range_frame = mp0101_prompt_data.get("long_range_frame") if mp0101_prompt_data else None
        local_transformation = mp0101_prompt_data.get("local_transformation") if mp0101_prompt_data else None

        if mp0101_prompt_data and long_range_frame and local_transformation:
            preflight_results["PromptMapParser"] = "PASS"
            log_message("PromptMapParser: PASS", log_file)
        else:
            log_message(f"PromptMapParser: FAIL. MP:{selected_marker} prompt data missing or incomplete.", log_file)
            raise ValueError(f"PromptMapParser preflight failed for {selected_marker}.")

        # 5. Validate SOURCE ↔ PROMPT_MAP
        log_message("STEP 5: Validating SOURCE ↔ PROMPT_MAP.", log_file)
        validator = SourcePromptMapValidator()
        validation_result = validator.validate(marker_graph, prompt_map_data)

        if validation_result:
            preflight_results["SourcePromptMapValidator"] = "PASS"
            log_message("SourcePromptMapValidator: PASS", log_file)
        else:
            log_message("SourcePromptMapValidator: FAIL.", log_file)
            raise ValueError("SourcePromptMapValidator preflight failed.")

        # 6. Derive MP:0101 Body & 7. Block-Boundary Preflight
        log_message(f"STEP 6 & 7: Deriving MP:{selected_marker} body and performing block boundary preflight checks.", log_file)
        current_source_content = ""
        
        selected_marker_line = f"<!-- {selected_marker} -->"
        following_marker_line = f"<!-- {following_marker} -->"

        selected_marker_start_pos = slotted_source.find(selected_marker_line)
        if selected_marker_start_pos == -1:
            raise ValueError(f"Selected marker '{selected_marker_line}' not found in slotted_source.")
        
        content_start_pos = selected_marker_start_pos + len(selected_marker_line)
        next_marker_pos = slotted_source.find(following_marker_line, content_start_pos)
        
        if next_marker_pos != -1:
            current_source_content = slotted_source[content_start_pos:next_marker_pos]
        else:
            raise ValueError(f"Following marker '{following_marker_line}' not found in slotted_source.")

        # Preflight check 3: CURRENT_SOURCE content and boundaries
        if selected_marker_line in current_source_content:
             raise ValueError(f"Marker '{selected_marker_line}' found within extracted CURRENT_SOURCE.")
        if following_marker_line in current_source_content:
             raise ValueError(f"Marker '{following_marker_line}' found within extracted CURRENT_SOURCE.")
        
        preflight_results["BlockBoundary"] = "PASS"
        log_message("BlockBoundary: PASS", log_file)

        # 8. Construct USER Payload
        log_message("STEP 8: Constructing USER payload.", log_file)
        user_payload_parts = []

        # LONG_RANGE_FRAME
        user_payload_parts.append(f"BEGIN_LONG_RANGE_FRAME\n{long_range_frame.strip()}\nEND_LONG_RANGE_FRAME")

        # CURRENT_SOURCE
        user_payload_parts.append(f"BEGIN_CURRENT_SOURCE\n{current_source_content.strip()}\nEND_CURRENT_SOURCE")

        # LOCAL_TRANSFORMATION
        user_payload_parts.append(f"BEGIN_LOCAL_TRANSFORMATION\n{local_transformation.strip()}\nEND_LOCAL_TRANSFORMATION")

        user_payload_str = "\n\n".join(user_payload_parts)
        save_file_content(OUTPUT_PAYLOAD_PATH, user_payload_str)
        log_message(f"USER payload saved to {OUTPUT_PAYLOAD_PATH}. Length: {len(user_payload_str)}", log_file)

        # Check for excluded sections
        if "BEGIN_CONTINUITY_CACHE" in user_payload_str:
            raise ValueError("USER payload must not contain BEGIN_CONTINUITY_CACHE.")
        if "BEGIN_PROTECTED_CONTEXT" in user_payload_str:
            raise ValueError("USER payload must not contain BEGIN_PROTECTED_CONTEXT.")
        if "BEGIN_STRUCTURAL_CONTEXT" in user_payload_str:
            raise ValueError("USER payload must not contain BEGIN_STRUCTURAL_CONTEXT.")

        # Preflight check 6: Payload Structure PASS
        preflight_results["PayloadStructure"] = "PASS"
        log_message("PayloadStructure: PASS", log_file)

        # 9. Assemble SYSTEM Payload
        log_message("STEP 9: Assembling SYSTEM payload.", log_file)
        gemma_kernel_content = read_file_content(GEMMA_KERNEL_PATH)
        gemma_kernel_wrapped = f"BEGIN_GEMMA_KERNEL\n{gemma_kernel_content}\nEND_GEMMA_KERNEL"

        runtime_override_content = """BEGIN_RUNTIME_CONTRACT_OVERRIDE
For this diagnostic run, treat the legacy Concept Package / Package Prompt
wording in the Gemma kernel as superseded by the structured USER message.

The authorities for this inference are only the USER sections actually present:
LONG_RANGE_FRAME,
CURRENT_SOURCE,
LOCAL_TRANSFORMATION,
and any STRUCTURAL_CONTEXT, PROTECTED_CONTEXT, or CONTINUITY_CACHE section
when such a section is present.

Do not invent substantive material beyond those supplied authorities.
Do not require a legacy Concept Package or Package Prompt.
END_RUNTIME_CONTRACT_OVERRIDE"""
        payload_emissions["RUNTIME_CONTRACT_OVERRIDE"] = True
        log_message("RUNTIME_CONTRACT_OVERRIDE: PRESENT", log_file)

        system_payload = f"{gemma_kernel_wrapped}\n\n{runtime_override_content}"
        log_message(f"SYSTEM payload assembled. Length: {len(system_payload)}", log_file)

        # 10. Load Model and Run Inference
        log_message("STEP 10 & 11: Loading model and preparing for inference.", log_file)
        
        # Read generation parameters from writer_config.yaml
        with open(WRITER_CONFIG_PATH, 'r', encoding='utf-8') as f:
            writer_config_data = yaml.safe_load(f)
            
        model_config = writer_config_data.get('model', {})
        model_path_from_config = model_config.get('path')
        if not model_path_from_config:
            raise ValueError("Model path not found in writer_config.yaml (expected model.path).")

        gen_config = writer_config_data.get('generation', {})
        generation_params["MODEL"] = model_path_from_config
        generation_params["N_CTX"] = model_config.get("n_ctx", 8192)
        generation_params["MAX_TOKENS"] = gen_config.get("max_tokens", 2048)
        generation_params["TEMPERATURE"] = gen_config.get("temperature", 0.0)
        generation_params["TOP_P"] = gen_config.get("top_p", 0.9)

        # Load real model using canonical loader.py
        llm = load_model(WRITER_CONFIG_PATH)

        messages = [
            {"role": "system", "content": system_payload},
            {"role": "user", "content": user_payload_str},
        ]

        log_message(f"Calling create_chat_completion with model: {generation_params['MODEL']}", log_file)
        generation_params["CREATE_CHAT_COMPLETION_CALLS"] = 1

        # Real create_chat_completion call - NO FALLBACKS
        response = llm.create_chat_completion(
            messages=messages,
            max_tokens=generation_params["MAX_TOKENS"],
            temperature=generation_params["TEMPERATURE"],
            top_p=generation_params["TOP_P"],
        )

        log_message("Extracting generated content from model response.", log_file)
        generated_content = response["choices"][0]["message"]["content"]
        
        generation_params["OUTPUT_LENGTH"] = len(generated_content)
        if generated_content and generated_content.strip():
            generation_params["OUTPUT_NON_EMPTY"] = True
            save_file_content(OUTPUT_GENERATED_PATH, generated_content)
            log_message(f"Generated content saved to {OUTPUT_GENERATED_PATH}", log_file)
            generation_status = "SUCCESS"
        else:
            raise ValueError("GENERATION_FAILED: Model returned empty content.")

    except Exception as e:
        log_message(f"ERROR: {type(e).__name__}: {e}", log_file)
        generation_status = "GENERATION_FAILED"
        # If the file exists from a previous run, delete it to ensure no stale/fake content remains
        if os.path.exists(OUTPUT_GENERATED_PATH):
            os.remove(OUTPUT_GENERATED_PATH)
        raise e
    finally:
        log_message("--- Execution End ---", log_file)
        
        # Determine status
        if generation_status == "SUCCESS" and all(v == "PASS" for v in preflight_results.values()):
            smoke_status = "SUCCESS"
        else:
            smoke_status = "FAILURE"

        log_message(f"Final Smoke Status: {smoke_status}", log_file)
        
        report_dict = {
            "SMOKE_BRIDGE_REPORT": {
                "STATUS": smoke_status,
                "RUN_TYPE": run_type,
                "FILES_CREATED": [
                    "src/smoke_bridge.py",
                    OUTPUT_GENERATED_PATH,
                    OUTPUT_PAYLOAD_PATH,
                    OUTPUT_RUN_LOG_PATH,
                ],
                "SOURCE": {
                    "FILE": SOURCE_MANUSCRIPT_PATH,
                    "SELECTED_MARKER": selected_marker,
                },
                "PROMPT_MAP": {
                    "FILE": PROMPT_MAP_PATH,
                },
                "PREFLIGHT": preflight_results,
                "PAYLOAD": {
                    "CACHE_EMITTED": payload_emissions["CACHE_EMITTED"],
                    "PROTECTED_CONTEXT_EMITTED": payload_emissions["PROTECTED_CONTEXT_EMITTED"],
                    "STRUCTURAL_CONTEXT_EMITTED": payload_emissions["STRUCTURAL_CONTEXT_EMITTED"],
                    "RUNTIME_CONTRACT_OVERRIDE": payload_emissions["RUNTIME_CONTRACT_OVERRIDE"],
                    "SYSTEM_LENGTH": len(system_payload) if 'system_payload' in locals() else 'N/A',
                    "USER_LENGTH": len(user_payload_str) if 'user_payload_str' in locals() else 'N/A',
                },
                "GENERATION": generation_params,
                "PRIMARY_EVIDENCE": {
                    "OUTPUT": OUTPUT_GENERATED_PATH if smoke_status == "SUCCESS" else "N/A",
                    "USER_PAYLOAD": OUTPUT_PAYLOAD_PATH,
                    "RUN_LOG": OUTPUT_RUN_LOG_PATH,
                },
                "LIMITATIONS": [
                    "NON_PRODUCTION_SMOKE",
                    "STABLE_CONFIG not exercised",
                    "continuity/cache not exercised",
                    "no literary acceptance",
                ],
                "NEXT": "WAIT_FOR_DEEPSEEK"
            }
        }
        
        report_yaml = yaml.dump(report_dict, indent=2)
        log_message("\n--- FINAL REPORT ---", log_file)
        log_message(report_yaml, log_file)
        print(report_yaml)

if __name__ == "__main__":
    run_smoke_bridge()
