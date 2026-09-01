import os
import yaml
import time
import json
import hashlib
from datetime import datetime
from src.loader import load_model
from llama_cpp import Llama
import argparse # Added import

EXPECTED_CHECKLIST = [
    "epistemic status marker on every mandatory claim",
    "canon boundaries, all three lists",
    "withdrawn claims list",
    "required material, complete and quotable",
    "authorial voice samples",
    "output specification: language, length, sections"
]

def parse_constants_check(raw_output: str) -> tuple[str, dict]:
    """
    Returns (status, details)
    status: "ALL_YES" | "HAS_NO" | "NOT_FOUND"
    details: dictionary {label: "YES"/"NO"/"NOT_FOUND"}
    """
    if "CONSTANTS CHECK" not in raw_output:
        return "NOT_FOUND", {}

    lines = raw_output.splitlines()
    in_check = False
    check_lines = []
    
    for line in lines:
        if "CONSTANTS CHECK" in line:
            in_check = True
            continue
        if in_check:
            if line.strip() == "":
                continue
            if "YES" in line or "NO" in line:
                check_lines.append(line.strip())
            elif line.strip() and not line.strip().startswith("---"):
                break

    if not check_lines:
        return "NOT_FOUND", {}

    result = {}
    for label in EXPECTED_CHECKLIST:
        found = False
        for line in check_lines:
            if label.lower() in line.lower():
                if "yes" in line.lower():
                    result[label] = "YES"
                elif "no" in line.lower():
                    result[label] = "NO"
                else:
                    result[label] = "MALFORMED"
                found = True
                break
        if not found:
            result[label] = "NOT_FOUND"

    if all(v == "YES" for v in result.values()):
        return "ALL_YES", result
    elif any(v == "NO" for v in result.values()):
        return "HAS_NO", result
    elif any(v == "NOT_FOUND" for v in result.values()):
        return "NOT_FOUND", result
    else:
        return "MALFORMED", result

def generate(run_id: str, system_prompt: str, user_prompt: str, temperature: float):
    run_log_dir = f"logs/runs/{run_id}"
    os.makedirs(run_log_dir, exist_ok=True)
    
    metadata = {
        "run_id": run_id,
        "timestamp": datetime.now().isoformat(),
        "generation": {"temperature": temperature}
    }
    
    constants_check_status = "NOT_FOUND" # Initialize to default
    constants_check_details = {}
    raw_output = "" # Initialize raw_output

    try:
        # Load config
        with open("config/writer_config.yaml", 'r') as f:
            config = yaml.safe_load(f)
            
        # Load model
        llm = load_model("config/writer_config.yaml")
        
        # Inference
        start_time = time.time()
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        if user_prompt:
            messages.append({"role": "user", "content": user_prompt})

        output = llm.create_chat_completion(
            messages=messages,
            max_tokens=config['generation']['max_tokens'],
            temperature=temperature,
            top_p=config['generation']['top_p']
        )
        duration = time.time() - start_time
        
        # Extract raw output
        if not output or "choices" not in output or not output["choices"]:
            raise ValueError("Model returned empty response")
        raw_output = output['choices'][0]['message']['content']

        # 1. Save raw_output immediately
        raw_output_path = os.path.join(run_log_dir, "raw_output.md")
        with open(raw_output_path, 'w', encoding='utf-8') as f:
            f.write(raw_output)

        # 2. Parse constants check from raw_output
        constants_check_status, constants_check_details = parse_constants_check(raw_output)

        # 3. Save constants_check.yaml
        constants_check_path = os.path.join(run_log_dir, "constants_check.yaml")
        with open(constants_check_path, 'w', encoding='utf-8') as f:
            yaml.dump({
                "status": constants_check_status,
                "items": constants_check_details
            }, f, allow_unicode=True, sort_keys=False)

        query_count = raw_output.count("<<QUERY:")
        
        status = "SUCCESS"
        if constants_check_status == "HAS_NO":
            status = "INPUT_CONTRACT_FAILURE"
        elif query_count > 0:
            status = "SUCCESS_WITH_QUERIES"
            
        # Update metadata with generation results
        metadata.update({
            "result": {
                "status": status,
                "duration_seconds": duration,
                "constants_check": constants_check_status,
                "query_count": query_count
            }
        })
        
    except Exception as e:
        status = "FAILED"
        metadata.update({
            "result": {
                "status": status,
                "failure_reason": str(e)
            }
        })
    finally:
        # Write metadata.yaml in the finally block to ensure it's always written
        metadata_path = os.path.join(run_log_dir, "metadata.yaml")
        with open(metadata_path, 'w') as f:
            yaml.dump(metadata, f)
            
    return metadata, status

if __name__ == "__main__":
    # --- MODIFIED BLOCK ---
    parser = argparse.ArgumentParser(description="Generator script for Manuscript Writer.")
    parser.add_argument("--run_id", type=str, required=True, help="The unique identifier for this run.")
    parser.add_argument("--temperature", type=float, default=0.0, help="The generation temperature.")
    args = parser.parse_args()

    # Use parsed arguments
    run_id = args.run_id
    temperature = args.temperature
    print(f"DEBUG: run_id = {run_id}") # Added debug print for run_id

    # Read system prompt
    try:
        with open("Gemma.md", 'r', encoding='utf-8') as f:
            system_prompt = f.read()
    except FileNotFoundError:
        print("Error: Gemma.md not found.")
        exit(1)

    # Read user prompt from compiled_input.txt using the parsed run_id
    compiled_input_path = os.path.join("logs", "runs", run_id, "compiled_input.txt")
    print(f"Attempting to read compiled input from: {compiled_input_path}") # Added print statement for debugging
    try:
        with open(compiled_input_path, 'r', encoding='utf-8') as f:
            user_prompt = f.read()
    except FileNotFoundError:
        print(f"Error: Compiled input file not found at {compiled_input_path}. Please ensure STEP 1A was completed successfully.")
        exit(1)

    # Execute the generation process
    metadata_from_generate, generation_status = generate(run_id, system_prompt, user_prompt, temperature)

    # Process artifacts *after* generation is complete, only if generation was successful
    if generation_status != "FAILED":
        try:
            # Read raw_output.md using the parsed run_id
            raw_output_path = os.path.join("logs", "runs", run_id, "raw_output.md")
            with open(raw_output_path, 'r', encoding='utf-8') as f:
                raw_output = f.read()

            constants_check_status, constants_check_details = parse_constants_check(raw_output)

            # Check if all constants are YES and create manuscript
            if constants_check_status == "ALL_YES":
                # Extract manuscript text, removing CONSTANTS CHECK block
                manuscript_lines = []
                in_check_block = False
                for line in raw_output.splitlines():
                    if "CONSTANTS CHECK" in line:
                        in_check_block = True
                        continue
                    if in_check_block:
                        if line.strip() == "" or line.strip().startswith("---"):
                            in_check_block = False
                            continue
                    if not in_check_block:
                        manuscript_lines.append(line)

                manuscript = "\n".join(manuscript_lines)

                # Save manuscript using the parsed run_id
                manuscript_path = os.path.join("Output", f"{run_id}.manuscript.md")
                os.makedirs(os.path.dirname(manuscript_path), exist_ok=True) # Ensure output directory exists
                with open(manuscript_path, 'w', encoding='utf-8') as f:
                    f.write(manuscript)
                print(f"Manuscript created at: {manuscript_path}")

            # Update metadata object that was returned from generate()
            # Ensure the 'result' key exists
            if 'result' not in metadata_from_generate:
                metadata_from_generate['result'] = {}

            metadata_from_generate['result']['constants_check'] = constants_check_status
            metadata_from_generate['result']['manuscript_created'] = (constants_check_status == "ALL_YES")

            # Calculate SHA-256 for manuscript if created
            if metadata_from_generate['result'].get('manuscript_created'):
                with open(manuscript_path, 'rb') as f:
                    manuscript_hash = hashlib.sha256(f.read()).hexdigest()
                metadata_from_generate['result']['manuscript_sha256'] = manuscript_hash

            # Write the complete metadata object ONCE
            metadata_path = os.path.join("logs", "runs", run_id, "metadata.yaml")
            with open(metadata_path, 'w') as f:
                yaml.dump(metadata_from_generate, f)

            print(f"Metadata updated with Constants Check status: {constants_check_status}")

        except FileNotFoundError as e:
            print(f"Error processing artifacts after generation: {e}")
        except ValueError as e:
            print(f"Error processing artifacts after generation: {e}")
        except Exception as e:
            print(f"An unexpected error occurred during artifact processing: {e}")
    else:
        print(f"Generation failed with status: {generation_status}. Skipping artifact processing.")
