import os
import hashlib
import json
from datetime import datetime

class RevisionAuthority:
    def __init__(self, revision_id: str, files: List[Dict[str, str]]):
        self.revision_id = revision_id
        self.files = files  # List of {'path': str, 'hash': str}
        self.timestamp = datetime.now().isoformat()

    def to_dict(self) -> Dict[str, Any]:
        return {
            "revision_id": self.revision_id,
            "timestamp": self.timestamp,
            "files": self.files
        }

def create_revision_authority(source_dir: str, revision_id: str, output_dir: str) -> RevisionAuthority:
    """
    Creates a deterministic authority freeze for files in a source directory.

    Args:
        source_dir: The directory containing the files to freeze.
        revision_id: A unique identifier for this revision.
        output_dir: The base directory where the revision artifacts will be stored.

    Returns:
        A RevisionAuthority object representing the frozen state.

    Raises:
        FileNotFoundError: If source_dir does not exist.
        IOError: If there are issues reading files or creating directories.
    """
    if not os.path.isdir(source_dir):
        raise FileNotFoundError(f"Source directory not found: {source_dir}")

    revision_dir = os.path.join(output_dir, "revisions", revision_id)
    frozen_dir = os.path.join(revision_dir, "frozen")
    os.makedirs(frozen_dir, exist_ok=True)

    file_hashes: List[Dict[str, str]] = []
    
    # Walk through the source directory to hash files
    for root, _, files in os.walk(source_dir):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            relative_path = os.path.relpath(file_path, source_dir)
            
            try:
                with open(file_path, 'rb') as f:
                    file_hash = hashlib.sha256(f.read()).hexdigest()
                
                file_hashes.append({"path": relative_path, "hash": file_hash})
                
                # Optionally, copy the file to the frozen directory to preserve it
                # For simplicity in this implementation, we'll just record the hash.
                # If a full copy is needed, uncomment the following lines:
                # dest_file_path = os.path.join(frozen_dir, relative_path)
                # os.makedirs(os.path.dirname(dest_file_path), exist_ok=True)
                # with open(dest_file_path, 'wb') as dest_f:
                #     dest_f.write(f.read()) # Note: f is already at the end, need to reopen or seek(0)
                # Reopening for copy:
                with open(file_path, 'rb') as src_f, open(os.path.join(frozen_dir, relative_path), 'wb') as dest_f:
                    dest_f.write(src_f.read())

            except Exception as e:
                raise IOError(f"Error processing file {file_path}: {e}")

    # Sort file_hashes by path to ensure deterministic order
    file_hashes.sort(key=lambda x: x["path"])

    authority = RevisionAuthority(revision_id, file_hashes)
    
    # Create PRODUCTION_REVISION.manifest
    manifest_path = os.path.join(revision_dir, "PRODUCTION_REVISION.manifest")
    try:
        with open(manifest_path, 'w', encoding='utf-8') as f:
            json.dump(authority.to_dict(), f, indent=4)
    except Exception as e:
        raise IOError(f"Error writing manifest file {manifest_path}: {e}")

    return authority

# --- Test Fixtures --- (for demonstration; actual tests should be in a separate test file)

# Example of a simple directory structure to test with

TEST_SOURCE_DIR_CONTENT = {
    "file1.txt": "Content of file 1.\n",
    "subdir/file2.txt": "Content of file 2 in subdir.\n",
    "subdir/another_file.py": "print('hello')\n",
}

def create_test_directory_structure(base_dir: str, content_dict: Dict[str, str]):
    """Helper to create a directory structure with files."""
    os.makedirs(base_dir, exist_ok=True)
    for path, content in content_dict.items():
        full_path = os.path.join(base_dir, path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(content)

def cleanup_test_directory(base_dir: str):
    """Helper to remove a directory and its contents."""
    import shutil
    if os.path.exists(base_dir):
        shutil.rmtree(base_dir)

if __name__ == '__main__':
    TEST_BASE_DIR = "test_fixtures/authority_freeze"
    SOURCE_DIR_NAME = "source_files_to_freeze"
    OUTPUT_ROOT_NAME = "revisions_output"
    
    source_dir_path = os.path.join(TEST_BASE_DIR, SOURCE_DIR_NAME)
    output_root_path = os.path.join(TEST_BASE_DIR, OUTPUT_ROOT_NAME)

    REVISION_ID_1 = "rev-001"
    REVISION_ID_2 = "rev-002"

    print("--- Testing Deterministic Authority Freeze ---")

    # Test case 1: Basic freeze with a few files
    create_test_directory_structure(source_dir_path, TEST_SOURCE_DIR_CONTENT)
    print(f"\nCreated test source directory: {source_dir_path}")

    print(f"\nTesting freeze for revision: {REVISION_ID_1}")
    try:
        authority1 = create_revision_authority(source_dir_path, REVISION_ID_1, output_root_path)
        print("Freeze operation PASSED.")
        print(f"Revision ID: {authority1.revision_id}")
        print(f"Timestamp: {authority1.timestamp}")
        print(f"Number of files frozen: {len(authority1.files)}")
        # Check if manifest was created
        manifest_path1 = os.path.join(output_root_path, "revisions", REVISION_ID_1, "PRODUCTION_REVISION.manifest")
        if os.path.exists(manifest_path1):
            print(f"Manifest file created: {manifest_path1}")
            with open(manifest_path1, 'r') as f:
                manifest_data = json.load(f)
            print(f"Manifest content: {json.dumps(manifest_data, indent=2)}")
        else:
            print("Error: Manifest file not created.")

    except (FileNotFoundError, IOError) as e:
        print(f"Freeze operation FAILED: {e}")
    finally:
        cleanup_test_directory(source_dir_path)
        # Keep output for inspection for now, clean up later if needed

    # Test case 2: Second freeze with slightly different content or new files
    # Simulate content change by modifying a file
    modified_source_dir_path = os.path.join(TEST_BASE_DIR, SOURCE_DIR_NAME + "_modified")
    create_test_directory_structure(modified_source_dir_path, TEST_SOURCE_DIR_CONTENT)
    # Modify one file
    modified_file_path = os.path.join(modified_source_dir_path, "file1.txt")
    with open(modified_file_path, "a", encoding="utf-8") as f:
        f.write("\nAppended line.\n")
    # Add a new file
    new_file_path = os.path.join(modified_source_dir_path, "new_file.log")
    with open(new_file_path, "w", encoding="utf-8") as f:
        f.write("Log entry.\n")

    print(f"\nTesting freeze for revision: {REVISION_ID_2} with modified content")
    try:
        authority2 = create_revision_authority(modified_source_dir_path, REVISION_ID_2, output_root_path)
        print("Freeze operation PASSED.")
        print(f"Revision ID: {authority2.revision_id}")
        print(f"Number of files frozen: {len(authority2.files)}")
        # Check if file hashes are different
        file1_hash_old = next((f['hash'] for f in authority1.files if f['path'] == 'file1.txt'), None)
        file1_hash_new = next((f['hash'] for f in authority2.files if f['path'] == 'file1.txt'), None)
        if file1_hash_old and file1_hash_new and file1_hash_old != file1_hash_new:
            print("Successfully detected hash change for file1.txt.")
        else:
            print("Warning: Hash change for file1.txt not detected or file not found.")

        if any(f['path'] == 'new_file.log' for f in authority2.files):
            print("Successfully detected addition of new_file.log.")
        else:
            print("Warning: new_file.log not found in authority2 files.")

    except (FileNotFoundError, IOError) as e:
        print(f"Freeze operation FAILED: {e}")
    finally:
        cleanup_test_directory(modified_source_dir_path)

    # Test case 3: Empty source directory
    empty_source_dir_path = os.path.join(TEST_BASE_DIR, SOURCE_DIR_NAME + "_empty")
    create_test_directory_structure(empty_source_dir_path, {})
    print(f"\nTesting freeze with empty source directory: {empty_source_dir_path}")
    try:
        authority3 = create_revision_authority(empty_source_dir_path, "rev-empty", output_root_path)
        print("Freeze operation PASSED.")
        print(f"Number of files frozen: {len(authority3.files)}")
        if len(authority3.files) == 0:
            print("Correctly found 0 files in empty directory.")
        else:
            print(f"Error: Found {len(authority3.files)} files in empty directory.")
    except (FileNotFoundError, IOError) as e:
        print(f"Freeze operation FAILED: {e}")
    finally:
        cleanup_test_directory(empty_source_dir_path)

    # Test case 4: Source directory not found
    non_existent_source_dir = os.path.join(TEST_BASE_DIR, "non_existent_source")
    print(f"\nTesting freeze with non-existent source directory: {non_existent_source_dir}")
    try:
        create_revision_authority(non_existent_source_dir, "rev-nonexistent", output_root_path)
        print("Freeze operation PASSED (unexpected).")
    except FileNotFoundError as e:
        print(f"Freeze operation FAILED as expected: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    print("\n--- Deterministic Authority Freeze Testing Complete ---")

    # Final cleanup of test directories
    # cleanup_test_directory(os.path.join(TEST_BASE_DIR, SOURCE_DIR_NAME))
    # cleanup_test_directory(os.path.join(TEST_BASE_DIR, SOURCE_DIR_NAME + "_modified"))
    # cleanup_test_directory(os.path.join(TEST_BASE_DIR, SOURCE_DIR_NAME + "_empty"))
    # print(f"Cleaned up test directories under {TEST_BASE_DIR}")
