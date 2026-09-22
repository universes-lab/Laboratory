import os
import argparse

def build_prompt(package_id: str, run_id: str) -> tuple[str, str]:
    # Precondition file paths
    syst_prompt_path = "Gemma.md"
    concept_package_path = f"Input/{package_id}.CONCEPT_PACKAGE.md"
    package_prompt_path = f"Input/{package_id}.CONCEPT_PACKAGE_Prompt.md"
    
    files = [syst_prompt_path, concept_package_path, package_prompt_path]
    
    # Precondition check
    for file in files:
        if not os.path.exists(file):
            raise FileNotFoundError(f"File not found: {file}")
        if os.path.getsize(file) == 0:
            raise ValueError(f"File is empty: {file}")
            
    # Reading contents
    with open(syst_prompt_path, 'r', encoding='utf-8') as f:
        syst_prompt = f.read()
    with open(concept_package_path, 'r', encoding='utf-8') as f:
        concept_package = f.read()
    with open(package_prompt_path, 'r', encoding='utf-8') as f:
        package_prompt = f.read()
        
    # Assembly
    assembled_prompt = "\n\n---\n\n".join([syst_prompt, concept_package, package_prompt])
    user_prompt = "\n\n---\n\n".join([concept_package, package_prompt]) # User prompt excludes system prompt
    
    # Save output
    run_log_dir = f"logs/runs/{run_id}"
    os.makedirs(run_log_dir, exist_ok=True)
    compiled_input_path = os.path.join(run_log_dir, "compiled_input.txt")
    
    with open(compiled_input_path, 'w', encoding='utf-8') as f:
        f.write(assembled_prompt)
        
    print(f"Prompt assembled and saved to {compiled_input_path}")
    return syst_prompt, user_prompt

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Builder script for Manuscript Writer.")
    parser.add_argument("--run_id", type=str, default="01_T00", help="The unique identifier for this run.")
    parser.add_argument("--package_id", type=str, required=True, help="The package identifier.")
    args = parser.parse_args()

    package_id = args.package_id
    run_id = args.run_id
    
    try:
        system_prompt, user_prompt = build_prompt(package_id, run_id)
        print("Prompt builder check: PASSED")
        print(f"System prompt length: {len(system_prompt)} chars")
        print(f"User prompt length: {len(user_prompt)} chars")
    except Exception as e:
        print(f"Prompt builder check: FAILED - {e}")
