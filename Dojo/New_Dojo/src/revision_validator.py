import os
import hashlib
import json
from datetime import datetime
from typing import List, Dict, Any, Optional

# Placeholder for RevisionAuthority class, assuming it's defined in authority_freeze.py
# In a real scenario, this would be imported or redefined if needed for validation context.
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

class RevisionValidator:
    def __init__(self, revision_dir: str, source_dir: str):
        self.revision_dir = revision_dir  # Path to the directory containing frozen/ and PRODUCTION_REVISION.manifest
        self.source_dir = source_dir      # Path to the current working source files
        self.manifest_path = os.path.join(revision_dir, "PRODUCTION_REVISION.manifest")
        self.frozen_dir = os.path.join(revision_dir, "frozen")
        self.current_authority: Optional[RevisionAuthority] = None
        self.validation_results: Dict[str, Any] = {}

    def load_manifest(self) -> RevisionAuthority:
        """Loads the PRODUCTION_REVISION.manifest file."""
        if not os.path.exists(self.manifest_path):
            raise FileNotFoundError(f"Manifest file not found: {self.manifest_path}")
        
        try:
            with open(self.manifest_path, 'r', encoding='utf-8') as f:
                manifest_data = json.load(f)
            
            # Basic validation of manifest structure
            if not isinstance(manifest_data, dict) or 'revision_id' not in manifest_data or 'files' not in manifest_data:
                raise ValueError("Invalid manifest structure: missing required keys.")
            
            # Reconstruct RevisionAuthority object (or just use the dict)
            self.current_authority = RevisionAuthority(
                revision_id=manifest_data['revision_id'],
                files=manifest_data['files']
            )
            return self.current_authority
        except (json.JSONDecodeError, ValueError, IOError) as e:
            raise ValueError(f"Error loading or validating manifest {self.manifest_path}: {e}")

    def validate_start_resume(self) -> bool:
        """
        Validation primitive for START/RESUME. Checks if a revision is valid to start processing.
        For Phase 1, this might involve checking if the manifest exists and is loadable.
        """
        try:
            self.load_manifest()
            self.validation_results['START_RESUME'] = {'status': 'PASS', 'message': 'Manifest loaded successfully.'}
            return True
        except Exception as e:
            self.validation_results['START_RESUME'] = {'status': 'FAIL', 'message': str(e)}
            return False

    def validate_pre_generate(self) -> bool:
        """
        Validation primitive for pre-GENERATE. Checks if the current source state matches the frozen authority.
        This detects if the source files have been modified since the last freeze.
        """
        if self.current_authority is None:
            if not self.validate_start_resume(): # Ensure manifest is loaded first
                return False

        source_files_state: Dict[str, str] = {}
        # Traverse the current source directory to calculate hashes
        for root, _, files in os.walk(self.source_dir):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                relative_path = os.path.relpath(file_path, self.source_dir)
                try:
                    with open(file_path, 'rb') as f:
                        file_hash = hashlib.sha256(f.read()).hexdigest()
                    source_files_state[relative_path] = file_hash
                except Exception as e:
                    self.validation_results['PRE_GENERATE'] = {'status': 'FAIL', 'message': f'Error hashing source file {file_path}: {e}'}
                    return False

        # Compare with frozen state
        frozen_files_map = {f['path']: f['hash'] for f in self.current_authority.files}
        
        mismatches = []
        # Check for files in source that are not in manifest (new files)
        for src_path, src_hash in source_files_state.items():
            if src_path not in frozen_files_map:
                mismatches.append({'path': src_path, 'type': 'NEW_FILE', 'message': 'File not present in original revision.'})

        # Check for files in manifest that are not in source (deleted files)
        for frozen_path in frozen_files_map:
            if frozen_path not in source_files_state:
                mismatches.append({'path': frozen_path, 'type': 'DELETED_FILE', 'message': 'File deleted since original revision.'})

        # Check for files present in both but with different hashes
        for path in set(source_files_state.keys()) & set(frozen_files_map.keys()):
            if source_files_state[path] != frozen_files_map[path]:
                mismatches.append({'path': path, 'type': 'MODIFIED_FILE', 'message': 'File content has changed.'})

        if not mismatches:
            self.validation_results['PRE_GENERATE'] = {'status': 'PASS', 'message': 'Source files match frozen revision.'}
            return True
        else:
            self.validation_results['PRE_GENERATE'] = {'status': 'FAIL', 'message': 'Source files do not match frozen revision.', 'details': mismatches}
            return False

    def validate_pre_commit(self) -> bool:
        """
        Validation primitive for pre-COMMIT. For Phase 1, this might be similar to pre-GENERATE 
        or could involve checking if the generated output adheres to certain rules.
        Since generation is not part of Phase 1, we can defer detailed checks or make it 
        a placeholder that passes if pre-GENERATE passed.
        """
        # For Phase 1, pre-commit validation might simply confirm that the state is ready for commit
        # if previous steps (like pre-generate) passed.
        # More complex checks would involve comparing generated output against the authority.
        
        pre_gen_result = self.validation_results.get('PRE_GENERATE', {}).get('status')
        if pre_gen_result == 'PASS':
            self.validation_results['PRE_COMMIT'] = {'status': 'PASS', 'message': 'Ready for commit; source matches revision.'}
            return True
        else:
            self.validation_results['PRE_COMMIT'] = {'status': 'FAIL', 'message': 'Cannot commit: PRE_GENERATE validation failed.'}
            return False

    def detect_frozen_authority_mutation(self) -> bool:
        """
        Checks if the frozen authority (manifest and files in frozen_dir) has been altered.
        This is a critical check to ensure the integrity of the revision history.
        """
        if self.current_authority is None:
            if not self.validate_start_resume():
                return False # Cannot check mutation if manifest isn't even loadable

        # 1. Re-hash the files in the frozen directory and compare with the manifest hashes.
        frozen_dir_hashes: Dict[str, str] = {}
        if not os.path.exists(self.frozen_dir):
            self.validation_results['FROZEN_MUTATION'] = {'status': 'FAIL', 'message': f'Frozen directory not found: {self.frozen_dir}'}
            return False

        for root, _, files in os.walk(self.frozen_dir):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                relative_path = os.path.relpath(file_path, self.frozen_dir)
                try:
                    with open(file_path, 'rb') as f:
                        file_hash = hashlib.sha256(f.read()).hexdigest()
                    frozen_dir_hashes[relative_path] = file_hash
                except Exception as e:
                    self.validation_results['FROZEN_MUTATION'] = {'status': 'FAIL', 'message': f'Error hashing file in frozen directory {file_path}: {e}'}
                    return False

        manifest_files_map = {f['path']: f['hash'] for f in self.current_authority.files}

        # Check for mismatches between manifest and actual frozen directory hashes
        mismatches = []
        # Files in manifest but not in frozen_dir
        for manifest_path in manifest_files_map:
            if manifest_path not in frozen_dir_hashes:
                mismatches.append({'path': manifest_path, 'type': 'MISSING_FROM_FROZEN', 'message': 'File from manifest missing in frozen directory.'})

        # Files in frozen_dir but not in manifest
        for frozen_path in frozen_dir_hashes:
            if frozen_path not in manifest_files_map:
                mismatches.append({'path': frozen_path, 'type': 'EXTRA_IN_FROZEN', 'message': 'File found in frozen directory but not in manifest.'})

        # Files present in both but with different hashes
        for path in set(manifest_files_map.keys()) & set(frozen_files_map.keys()):
            if manifest_files_map[path] != frozen_files_map[path]:
                mismatches.append({'path': path, 'type': 'HASH_MISMATCH', 'message': 'Hash mismatch between manifest and frozen directory file.'})

        if not mismatches:
            self.validation_results['FROZEN_MUTATION'] = {'status': 'PASS', 'message': 'Frozen authority integrity verified.'}
            return True
        else:
            self.validation_results['FROZEN_MUTATION'] = {'status': 'FAIL', 'message': 'Frozen authority integrity compromised.', 'details': mismatches}
            return False

    def get_validation_results(self) -> Dict[str, Any]:
        return self.validation_results


# --- Test Fixtures --- (for demonstration; actual tests should be in a separate test file)

# Helper functions for creating and cleaning up test files/directories
def create_test_fixture_file(file_path: str, content: str):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

def cleanup_test_fixture_file(file_path: str):
    if os.path.exists(file_path):
        os.remove(file_path)

def create_test_directory_structure(base_dir: str, content_dict: Dict[str, str]):
    os.makedirs(base_dir, exist_ok=True)
    for path, content in content_dict.items():
        full_path = os.path.join(base_dir, path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(content)

def cleanup_test_directory(base_dir: str):
    import shutil
    if os.path.exists(base_dir):
        shutil.rmtree(base_dir)

if __name__ == '__main__':
    TEST_BASE_DIR = "test_fixtures/revision_validator"
    SOURCE_DIR_NAME = "source_files"
    REVISIONS_DIR_NAME = "revisions"
    
    TEST_SOURCE_DIR_CONTENT = {
        "file1.txt": "Initial content of file 1.\n",
        "subdir/file2.txt": "Content of file 2 in subdir.\n",
        "subdir/another_file.py": "print(\'hello\')\n",
    }

    # Mock data for Authority object, as create_revision_authority is not called directly here
    # In real tests, we would create a revision first, then validate it.
    
    print("--- Testing Revision Validator ---")

    # --- Setup: Create a valid revision first ---
    REVISION_ID_VALID = "valid-rev-123"
    initial_source_dir = os.path.join(TEST_BASE_DIR, SOURCE_DIR_NAME)
    output_revisions_base = os.path.join(TEST_BASE_DIR, REVISIONS_DIR_NAME)
    valid_revision_dir = os.path.join(output_revisions_base, REVISION_ID_VALID)
    valid_frozen_dir = os.path.join(valid_revision_dir, "frozen")
    valid_manifest_path = os.path.join(valid_revision_dir, "PRODUCTION_REVISION.manifest")

    create_test_directory_structure(initial_source_dir, TEST_SOURCE_DIR_CONTENT)
    
    # Manually create a mock manifest and frozen files for validation tests
    # This simulates the output of create_revision_authority
    mock_authority = {
        "revision_id": REVISION_ID_VALID,
        "timestamp": datetime.now().isoformat(),
        "files": [
            {"path": "file1.txt", "hash": hashlib.sha256(b"Initial content of file 1.\n").hexdigest()},
            {"path": "subdir/another_file.py", "hash": hashlib.sha256(b"print(\'hello\')\n").hexdigest()},
            {"path": "subdir/file2.txt", "hash": hashlib.sha256(b"Content of file 2 in subdir.\n").hexdigest()}
        ]
    }
    
    # Create the frozen directory and files based on mock authority
    os.makedirs(valid_frozen_dir, exist_ok=True)
    for f_info in mock_authority['files']:
        frozen_file_path = os.path.join(valid_frozen_dir, f_info['path'])
        os.makedirs(os.path.dirname(frozen_file_path), exist_ok=True)
        with open(frozen_file_path, 'wb') as f:
            # Re-calculate hash to write correct content
            content_hash = f_info['hash']
            # This is a simplification: in reality, we'd need the actual content.
            # For testing, we assume the hash implies the content.
            # If we were testing the whole flow, we would hash the content from initial_source_dir.
            # Let's use the content from initial_source_dir to be more accurate.
            original_content_path = os.path.join(initial_source_dir, f_info['path'])
            with open(original_content_path, 'rb') as src_f:
                f.write(src_f.read())

    # Create the manifest file
    with open(valid_manifest_path, 'w', encoding='utf-8') as f:
        json.dump(mock_authority, f, indent=4)

    print(f"\nCreated mock revision artifacts for: {REVISION_ID_VALID}")

    # --- Test Case 1: VALIDATE_START_RESUME (successful load) ---
    print("\nTesting VALIDATE_START_RESUME...")
    validator_sr = RevisionValidator(valid_revision_dir, initial_source_dir)
    sr_pass = validator_sr.validate_start_resume()
    print(f"START_RESUME validation: {'PASS' if sr_pass else 'FAIL'}\nResults: {validator_sr.get_validation_results()['START_RESUME']}")

    # --- Test Case 2: VALIDATE_PRE_GENERATE (match) ---
    print("\nTesting VALIDATE_PRE_GENERATE (matching source)...")
    validator_pg = RevisionValidator(valid_revision_dir, initial_source_dir)
    pg_pass = validator_pg.validate_pre_generate()
    print(f"PRE_GENERATE validation: {'PASS' if pg_pass else 'FAIL'}\nResults: {validator_pg.get_validation_results()['PRE_GENERATE']}")

    # --- Test Case 3: VALIDATE_PRE_GENERATE (modified source) ---
    print("\nTesting VALIDATE_PRE_GENERATE (modified source)...")
    modified_source_dir = os.path.join(TEST_BASE_DIR, SOURCE_DIR_NAME + "_modified")
    create_test_directory_structure(modified_source_dir, TEST_SOURCE_DIR_CONTENT)
    # Modify file1.txt
    modified_file_path = os.path.join(modified_source_dir, "file1.txt")
    with open(modified_file_path, "a", encoding="utf-8") as f:
        f.write("\nAppended line for modification.\n")
    
    validator_pg_mod = RevisionValidator(valid_revision_dir, modified_source_dir)
    pg_mod_pass = validator_pg_mod.validate_pre_generate()
    print(f"PRE_GENERATE validation: {'PASS' if pg_mod_pass else 'FAIL'}\nResults: {validator_pg_mod.get_validation_results()['PRE_GENERATE']}")
    cleanup_test_directory(modified_source_dir)

    # --- Test Case 4: VALIDATE_PRE_GENERATE (new file in source) ---
    print("\nTesting VALIDATE_PRE_GENERATE (new file in source)...")
    source_with_new_file_dir = os.path.join(TEST_BASE_DIR, SOURCE_DIR_NAME + "_with_new")
    create_test_directory_structure(source_with_new_file_dir, TEST_SOURCE_DIR_CONTENT)
    # Add a new file
    new_file_path = os.path.join(source_with_new_file_dir, "new_file.log")
    with open(new_file_path, "w", encoding="utf-8") as f:
        f.write("Log entry.\n")

    validator_pg_new = RevisionValidator(valid_revision_dir, source_with_new_file_dir)
    pg_new_pass = validator_pg_new.validate_pre_generate()
    print(f"PRE_GENERATE validation: {'PASS' if pg_new_pass else 'FAIL'}\nResults: {validator_pg_new.get_validation_results()['PRE_GENERATE']}")
    cleanup_test_directory(source_with_new_file_dir)

    # --- Test Case 5: VALIDATE_PRE_GENERATE (deleted file from source) ---
    print("\nTesting VALIDATE_PRE_GENERATE (deleted file from source)...")
    # Use the initial source dir, but delete a file conceptually
    # For simplicity, we use the initial source dir but pretend file2.txt was deleted
    # A better test would be to copy and delete.
    # For this test, we'll simulate it by manually creating a source dir without file2.txt
    source_without_file2_dir = os.path.join(TEST_BASE_DIR, SOURCE_DIR_NAME + "_deleted")
    temp_content = TEST_SOURCE_DIR_CONTENT.copy()
    del temp_content["subdir/file2.txt"]
    create_test_directory_structure(source_without_file2_dir, temp_content)
    
    validator_pg_del = RevisionValidator(valid_revision_dir, source_without_file2_dir)
    pg_del_pass = validator_pg_del.validate_pre_generate()
    print(f"PRE_GENERATE validation: {'PASS' if pg_del_pass else 'FAIL'}\nResults: {validator_pg_del.get_validation_results()['PRE_GENERATE']}")
    cleanup_test_directory(source_without_file2_dir)

    # --- Test Case 6: VALIDATE_PRE_COMMIT (passes if pre-generate passed) ---
    print("\nTesting VALIDATE_PRE_COMMIT...")
    validator_pc = RevisionValidator(valid_revision_dir, initial_source_dir) # Use matching source
    validator_pc.validate_pre_generate() # Ensure pre_generate state is set
    pc_pass = validator_pc.validate_pre_commit()
    print(f"PRE_COMMIT validation: {'PASS' if pc_pass else 'FAIL'}\nResults: {validator_pc.get_validation_results()['PRE_COMMIT']}")

    # --- Test Case 7: DETECT_FROZEN_AUTHORITY_MUTATION (integrity check) ---
    print("\nTesting DETECT_FROZEN_AUTHORITY_MUTATION...")
    # Test with valid revision first
    validator_fm_valid = RevisionValidator(valid_revision_dir, initial_source_dir)
    fm_valid_pass = validator_fm_valid.detect_frozen_authority_mutation()
    print(f"FROZEN_MUTATION validation (valid): {'PASS' if fm_valid_pass else 'FAIL'}\nResults: {validator_fm_valid.get_validation_results().get('FROZEN_MUTATION', 'N/A')}")

    # Test by tampering with frozen_dir
    tampered_frozen_dir = os.path.join(valid_revision_dir, "frozen_tampered")
    os.makedirs(tampered_frozen_dir, exist_ok=True)
    # Copy original frozen content, but modify one file
    import shutil
    shutil.copytree(valid_frozen_dir, tampered_frozen_dir, dirs_exist_ok=True)
    tampered_file_path = os.path.join(tampered_frozen_dir, "file1.txt")
    with open(tampered_file_path, "a", encoding="utf-8") as f:
        f.write("\nTampered line.\n")

    # Update the manifest to point to the tampered frozen dir (this is a tricky part for testing)
    # For simplicity, we'll create a new validator that *points* to the tampered frozen dir,
    # but the validator will still load the original manifest. The check is between the original manifest
    # and the *actual* state of the frozen dir (which is now tampered).
    # This is a bit of a hack, as the validator expects frozen_dir to be relative to revision_dir.
    # Let's simulate by making the validator point to the original revision_dir but expect the frozen dir to be tampered.
    # This is imperfect, as the validator's internal logic might get confused. 
    # A better approach: create a new revision dir that IS tampered.
    
    REVISION_ID_TAMPERED = "tampered-rev-456"
    tampered_revision_dir = os.path.join(output_revisions_base, REVISION_ID_TAMPERED)
    shutil.copytree(valid_revision_dir, tampered_revision_dir, dirs_exist_ok=True)
    
    # Now, tamper the frozen content within the tampered revision dir
    tampered_frozen_content_path = os.path.join(tampered_revision_dir, "frozen", "file1.txt")
    with open(tampered_frozen_content_path, "a", encoding="utf-8") as f:
        f.write("\nTampered line in tampered revision.\n")

    print(f"\nTesting DETECT_FROZEN_AUTHORITY_MUTATION (tampered frozen dir)...")
    validator_fm_tampered = RevisionValidator(tampered_revision_dir, initial_source_dir)
    fm_tampered_pass = validator_fm_tampered.detect_frozen_authority_mutation()
    print(f"FROZEN_MUTATION validation (tampered): {'PASS' if fm_tampered_pass else 'FAIL'}\nResults: {validator_fm_tampered.get_validation_results().get('FROZEN_MUTATION', 'N/A')}")
    
    # --- Test Case 8: Manifest not found ---
    print("\nTesting validator with non-existent manifest...")
    non_existent_revision_dir = os.path.join(output_revisions_base, "non-existent-rev")
    validator_no_manifest = RevisionValidator(non_existent_revision_dir, initial_source_dir)
    try:
        validator_no_manifest.validate_start_resume()
        print("START_RESUME validation: PASS (unexpected - manifest should not be found)")
    except FileNotFoundError as e:
        print(f"START_RESUME validation: FAIL as expected: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    # --- Cleanup ---
    print("\nCleaning up test directories...")
    cleanup_test_directory(initial_source_dir)
    cleanup_test_directory(os.path.join(output_revisions_base, REVISION_ID_VALID))
    cleanup_test_directory(os.path.join(output_revisions_base, REVISION_ID_TAMPERED))
    # Note: Keeping TEST_BASE_DIR for manual inspection if needed.
    print(f"Test artifacts created under: {TEST_BASE_DIR}")

    print("\n--- Revision Validator Testing Complete ---")
