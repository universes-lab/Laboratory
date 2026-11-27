import os
import yaml
import re

def check_duplicates():
    ids = []
    root_dir = 'library/canon'
    for root, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.md'):
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    content = f.read()
                    match = re.search(r'^id:\s*(OBJ-\d+)', content, re.MULTILINE)
                    if match:
                        ids.append(match.group(1))
    
    duplicates = set([x for x in ids if ids.count(x) > 1])
    if duplicates:
        print(f"Duplicate IDs found: {duplicates}")
        exit(1)
    print("No duplicate IDs found.")

if __name__ == '__main__':
    check_duplicates()
