import yaml
from llama_cpp import Llama
import time
import os

def load_model(config_path: str) -> Llama:
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)

    model_path = config['model']['path']
    # Default parameters if not specified in config
    n_ctx = config.get('model', {}).get('n_ctx', 2048)
    
    print(f"Loading model from: {model_path}")
    start_time = time.time()
    
    # Initialize Llama model
    # Note: Using essential parameters as per requirements
    llm = Llama(
        model_path=model_path,
        n_ctx=n_ctx,
        n_gpu_layers=-1, # As suggested by common usage for local inference
        verbose=True,
        chat_format="gemma"  # <-- ADD THIS LINE
    )
    # Hypothesis 1: Add debug print for llm.n_ctx
    print(f"DEBUG: llm.n_ctx = {llm.n_ctx}")

    end_time = time.time()
    load_time = end_time - start_time
    print(f"Model loaded successfully in {load_time:.2f} seconds.")
    
    # Log the load time
    log_dir = "logs/runs" # As defined in SPEC
    os.makedirs(log_dir, exist_ok=True)
    with open(os.path.join(log_dir, "runtime.log"), "a") as log_file:
        log_file.write(f"Model loaded in {load_time:.2f} seconds\n")
        
    return llm

if __name__ == "__main__":
    # Test loading
    config_file = "config/writer_config.yaml"
    model = load_model(config_file)
    if model:
        print("Model check: PASSED")
