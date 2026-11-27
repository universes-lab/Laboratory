import os
import yaml

def validate_manifest(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        if not content.startswith('---'):
            return False, "Missing YAML frontmatter"
        try:
            # Extract YAML part
            parts = content.split('---')
            if len(parts) < 3:
                return False, "Invalid YAML structure"
            data = yaml.safe_load(parts[1])
            
            required_fields = ['id', 'type', 'provenance_type', 'provenance_source']
            for field in required_fields:
                if field not in data:
                    return False, f"Missing required field: {field}"
            return True, "OK"
        except Exception as e:
            return False, f"YAML error: {e}"

def main():
    root_dir = 'library/canon'
    errors = []
    for root, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.md'):
                path = os.path.join(root, file)
                ok, msg = validate_manifest(path)
                if not ok:
                    errors.append(f"{path}: {msg}")
    
    if errors:
        print("\n".join(errors))
        exit(1)
    print("All manifests are valid.")

if __name__ == '__main__':
    main()
