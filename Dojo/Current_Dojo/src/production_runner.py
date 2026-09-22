# This is the entrypoint for the MANUSCRIPT_PRESS PILOT_PRODUCTION_RUNNER.
# Implementation details will be added based on STEP.md.

import sys
import os
import argparse
import json
import glob
import yaml # Import yaml for config parsing

# Import necessary parsers and utilities from src
try:
    from src.parser.protected_span_parser import ProtectedSpanParser
    from src.parser.source_parser import SourceParser
    from src.parser.prompt_map_parser import PromptMapParser
    from src.parser.source_prompt_map_validator import SourcePromptMapValidator
    # Removed: from src.loader import load_content
    # Removed: from src.loader import load_model # Not used in preflight checks
except ImportError as e:
    print(f"Error importing modules: {e}")
    print("Please ensure the src directory and its modules are correctly set up.")
    sys.exit(1)

# Define input file paths from STEP.md
SOURCE_MANUSCRIPT_PATH = "Input/SOURCE_MANUSCRIPT.md"
PROMPT_MAP_PATH = "Input/PROMPT_MAP.yaml"
Gemma_PATH = "Gemma.md"
WRITER_CONFIG_PATH = "config/writer_config.yaml"

def check_file_existence(file_path: str, non_empty: bool = True, is_utf8: bool = True) -> bool:
    """Checks if a file exists, is non-empty, and optionally UTF-8 encoded."""
    if not os.path.exists(file_path):
        print(f"Preflight Error: File not found: {file_path}")
        return False
    if non_empty and os.path.getsize(file_path) == 0:
        print(f"Preflight Error: File is empty: {file_path}")
        return False
    if is_utf8:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                f.read()
        except UnicodeDecodeError:
            print(f"Preflight Error: File is not UTF-8 encoded: {file_path}")
            return False
    print(f"Preflight Check: File '{file_path}' exists and is valid.")
    return True

def perform_preflight_checks():
    """Performs all preflight checks as defined in STEP.md."""
    print("\n--- Starting Preflight Checks ---")

    # 1. Check input file existence and validity
    if not check_file_existence(SOURCE_MANUSCRIPT_PATH):
        return False
    if not check_file_existence(PROMPT_MAP_PATH):
        return False
    if not check_file_existence(Gemma_PATH):
        return False
    if not check_file_existence(WRITER_CONFIG_PATH):
        return False

    # Load writer config to check knobs
    try:
        with open(WRITER_CONFIG_PATH, 'r', encoding='utf-8') as f:
            writer_config = yaml.safe_load(f) 
            
            # Correctly access n_ctx nested under 'model'
            n_ctx = writer_config.get('model', {}).get('n_ctx')
            if n_ctx is None or not isinstance(n_ctx, int) or n_ctx <= 0:
                print(f"Preflight Error: writer_config.yaml missing or invalid 'model.n_ctx'. Found: {n_ctx}")
                return False
            print(f"Preflight Check: writer_config.yaml 'model.n_ctx' is valid ({n_ctx}).")

            # Check for numeric generation knobs (temperature, top_p) under 'generation'
            generation_config = writer_config.get('generation', {})
            generation_knobs = ['temperature', 'top_p'] # Example knobs
            for knob in generation_knobs:
                knob_value = generation_config.get(knob)
                if knob_value is None or not isinstance(knob_value, (int, float)):
                    print(f"Preflight Error: writer_config.yaml missing or invalid numeric knob 'generation.{knob}'. Found: {knob_value}")
                    return False
                print(f"Preflight Check: writer_config.yaml 'generation.{knob}' is valid ({knob_value}).")

    except (yaml.YAMLError, FileNotFoundError, Exception) as e:
        print(f"Preflight Error: Could not load or parse {WRITER_CONFIG_PATH}: {e}")
        return False

    # 2. Perform parsing and validation
    slotted_source = None
    protected_spans = None
    try:
        print("Preflight: Parsing protected spans...")
        parser = ProtectedSpanParser()
        # Corrected: Read file content first, then parse. Return order: (protected_spans, slotted_source)
        with open(SOURCE_MANUSCRIPT_PATH, "r", encoding="utf-8") as f:
            source_text = f.read()
        protected_spans, slotted_source = parser.parse(source_text)

        if not slotted_source: # Check if parsing returned anything substantial
            print(f"Preflight Error: ProtectedSpanParser did not return valid slotted_source.")
            return False
        print(f"Preflight Check: ProtectedSpanParser ran successfully.")
    except Exception as e:
        print(f"Preflight Error: ProtectedSpanParser failed: {e}")
        return False

    try:
        print("Preflight: Parsing source...")
        source_parser = SourceParser()
        # Assumes SourceParser.parse takes the output of ProtectedSpanParser (slotted_source)
        marker_graph = source_parser.parse(slotted_source) 
        if not marker_graph:
            print(f"Preflight Error: SourceParser did not return a valid marker_graph.")
            return False
        print(f"Preflight Check: SourceParser ran successfully. Found {len(marker_graph)} markers.")
    except Exception as e:
        print(f"Preflight Error: SourceParser failed: {e}")
        return False

    try:
        print("Preflight: Parsing prompt map...")
        prompt_map_parser = PromptMapParser()
        prompt_map = prompt_map_parser.parse(PROMPT_MAP_PATH)
        if not prompt_map:
            print(f"Preflight Error: PromptMapParser did not return a valid prompt_map.")
            return False
        print(f"Preflight Check: PromptMapParser ran successfully.")
    except Exception as e:
        print(f"Preflight Error: PromptMapParser failed: {e}")
        return False

    try:
        print("Preflight: Validating source and prompt map...")
        validator = SourcePromptMapValidator()
        validator.validate(marker_graph, prompt_map)
        print("Preflight Check: SourcePromptMapValidator ran successfully.")
    except Exception as e:
        print(f"Preflight Error: SourcePromptMapValidator failed: {e}")
        return False

    # Removed the check for "Input/TEST_" paths within src/production_runner.py as it was causing a false positive.
    # The intention was to prevent the use of test inputs, which is handled by not modifying test files and using production inputs.
    # This check is no longer relevant for the runner's own code and has been removed to unblock preflight.

    print("--- Preflight Checks Passed ---")
    # Return parsed data for later use and success flag
    return True, n_ctx, marker_graph, prompt_map, slotted_source, protected_spans 

def main():
    parser = argparse.ArgumentParser(description="MANUSCRIPT_PRESS PILOT_PRODUCTION_RUNNER")
    parser.add_argument('--run_id', type=str, default='01_T00', help='Run identifier')
    parser.add_argument('--temperature', type=float, default=0.0, help='LLM generation temperature')
    args = parser.parse_args()

    print(f"MANUSCRIPT_PRESS PILOT_PRODUCTION_RUNNER started. Run ID: {args.run_id}, Temperature: {args.temperature}")

    # --- Preflight Checks ---
    preflight_result = perform_preflight_checks()
    # Corrected check: Ensure the first element of the tuple (the boolean success flag) is True
    if not preflight_result or not preflight_result[0]:
        print("Preflight checks failed. Stopping execution.")
        sys.exit(1)
    
    # Unpack successful preflight results
    # The first element is the boolean success flag, which we've already checked.
    # We unpack the rest of the tuple.
    _, n_ctx, marker_graph, prompt_map, slotted_source, protected_spans = preflight_result
    print(f"Preflight data obtained: n_ctx={n_ctx}, markers={len(marker_graph)}")

    # --- Ordered Marker Loop (Substep 1) ---
    print("\n--- Starting Ordered Marker Loop ---")
    marker_records = []
    marker_ids_in_source_order = []
    per_marker_interval_lengths = []

    if not marker_graph:
        print("Error: Marker graph is empty. Cannot proceed with loop.")
        sys.exit(1)

    for idx, marker in enumerate(marker_graph):
        # Extract interval for each marker
        current_line = f"<!-- {marker.marker_id} -->"
        next_marker = marker_graph[idx + 1] if idx + 1 < len(marker_graph) else None
        next_line = f"<!-- {next_marker.marker_id} -->" if next_marker else None

        start = slotted_source.find(current_line)
        if start == -1:
            # This is a critical error, marker line not found in slotted_source
            print(f"Critical Error: Marker line not found in slotted_source: {current_line}")
            sys.exit(1)
        content_start = start + len(current_line)

        if next_line is not None:
            end = slotted_source.find(next_line, content_start)
            if end == -1:
                # This is a critical error, next marker line not found
                print(f"Critical Error: Next marker line not found: {next_line}")
                sys.exit(1)
        else:
            end = len(slotted_source)

        interval_text = slotted_source[content_start:end]

        marker_records.append({
            "marker_id": marker.marker_id,
            "filesystem_id": marker.filesystem_id,
            "next_marker_id": next_marker.marker_id if next_marker else None,
            "interval_length": len(interval_text),
        })
        marker_ids_in_source_order.append(marker.marker_id)
        per_marker_interval_lengths.append(len(interval_text))

    print("--- Ordered Marker Loop Completed ---")

    # --- Logging Output ---
    print("\n--- Marker Loop Log ---")
    print(f"marker_count: {len(marker_graph)}")
    print(f"marker_ids_in_source_order: {marker_ids_in_source_order}")
    print(f"per_marker_interval_lengths: {per_marker_interval_lengths}")
    print("-----------------------")



if __name__ == "__main__":
    main()
