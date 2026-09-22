import yaml
import os
from typing import Dict, Any, List, Tuple

class PromptMapValidationError(Exception):
    """Custom exception for PromptMap validation errors."""
    pass

class PromptMapParser:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.data: Dict[str, Dict[str, str]] = {}
        # In a more complete implementation, this would be populated by parsing SOURCE markers.
        # For now, we focus on validating the PROMPT_MAP structure itself.
        self.source_marker_ids: List[str] = []

    def load_and_validate(self):
        """Loads the YAML file and validates its structure according to SPEC rules."""
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"PROMPT_MAP file not found: {self.file_path}")

        with open(self.file_path, 'r', encoding='utf-8') as f:
            try:
                loaded_data = yaml.safe_load(f)
                if not isinstance(loaded_data, dict):
                    raise PromptMapValidationError("PROMPT_MAP must be a dictionary.")
                self.data = loaded_data
            except yaml.YAMLError as e:
                raise PromptMapValidationError(f"Error parsing YAML file: {e}")

        self._validate_structure()

    def _validate_structure(self):
        """Validates the structure of the loaded PROMPT_MAP data based on SPEC rules."""
        if not self.data:
            raise PromptMapValidationError("PROMPT_MAP is empty.")

        # Placeholder for matching PROMPT_MAP keys with SOURCE markers. 
        # This check is deferred to a higher-level orchestrator that has access to both.
        # For this parser, we focus on internal PROMPT_MAP structure and key formats.
        
        for marker_id, content in self.data.items():
            # Rule: keys are logical marker IDs (MP:XXXX)
            if not isinstance(marker_id, str) or not marker_id.startswith("MP:") or not marker_id[3:].isdigit():
                raise PromptMapValidationError(f"Invalid marker ID format: '{marker_id}'. Expected format like 'MP:XXXX' where XXXX is a number.")

            if not isinstance(content, dict):
                raise PromptMapValidationError(f"Entry for '{marker_id}' must be a dictionary.")

            # Rule: mandatory non-empty LONG_RANGE_FRAME and LOCAL_TRANSFORMATION
            long_range_frame = content.get("LONG_RANGE_FRAME")
            local_transformation = content.get("LOCAL_TRANSFORMATION")

            if long_range_frame is None:
                raise PromptMapValidationError(f"Missing 'LONG_RANGE_FRAME' for marker '{marker_id}'.")
            if not isinstance(long_range_frame, str) or not long_range_frame.strip():
                raise PromptMapValidationError(f"'LONG_RANGE_FRAME' for marker '{marker_id}' cannot be empty.")

            if local_transformation is None:
                raise PromptMapValidationError(f"Missing 'LOCAL_TRANSFORMATION' for marker '{marker_id}'.")
            if not isinstance(local_transformation, str) or not local_transformation.strip():
                raise PromptMapValidationError(f"'LOCAL_TRANSFORMATION' for marker '{marker_id}' cannot be empty.")

    def get_prompt_data(self) -> Dict[str, Dict[str, str]]:
        """Returns the parsed and validated PROMPT_MAP data."""
        return self.data

    def get_logical_marker_ids(self) -> List[str]:
        """Returns a list of logical marker IDs found in the PROMPT_MAP."""
        return list(self.data.keys())

# --- Test Fixtures --- (for demonstration; actual tests should be in a separate test file)

# Example of a valid PROMPT_MAP content
VALID_PROMPT_MAP_CONTENT = """
MP:0001:
  LONG_RANGE_FRAME: |
    This is the long-range frame for marker 0001.
    It provides context that spans a large section of the document.
  LOCAL_TRANSFORMATION: |
    This is the local transformation for marker 0001.
    It details specific instructions for this section.

MP:0005:
  LONG_RANGE_FRAME: |
    Another long-range frame for marker 0005.
  LOCAL_TRANSFORMATION: |
    Local transformation details for marker 0005.
"""

# Example of PROMPT_MAP with missing LONG_RANGE_FRAME
MISSING_LRF_PROMPT_MAP_CONTENT = """
MP:0001:
  # LONG_RANGE_FRAME is missing
  LOCAL_TRANSFORMATION: |
    Local transformation for marker 0001.
"""

# Example of PROMPT_MAP with empty LOCAL_TRANSFORMATION
EMPTY_LT_PROMPT_MAP_CONTENT = """
MP:0001:
  LONG_RANGE_FRAME: |
    Long range frame for marker 0001.
  LOCAL_TRANSFORMATION: |
    # Empty local transformation
"""

# Example of PROMPT_MAP with invalid marker ID (no colon, non-numeric)
INVALID_ID_PROMPT_MAP_CONTENT = """
MP0001:
  LONG_RANGE_FRAME: |
    Long range frame.
  LOCAL_TRANSFORMATION: |
    Local transformation.

MP:abc:
  LONG_RANGE_FRAME: |
    Another frame.
  LOCAL_TRANSFORMATION: |
    Another transformation.
"""

# Example of PROMPT_MAP with non-dictionary entry for a marker
NON_DICT_ENTRY_PROMPT_MAP_CONTENT = """
MP:0001: "This should be a dictionary"
"""

# Example of PROMPT_MAP with empty content
EMPTY_PROMPT_MAP_CONTENT = ""

# Example of PROMPT_MAP with non-string values
NON_STRING_VALUES_CONTENT = """
MP:0001:
  LONG_RANGE_FRAME: 12345
  LOCAL_TRANSFORMATION: "This is a string"
"""

# Example of PROMPT_MAP with malformed YAML
MALFORMED_YAML_CONTENT = """
MP:0001:
  LONG_RANGE_FRAME: |
    This is a string
  LOCAL_TRANSFORMATION: |
    This is another string
invalid yaml section:
    indentation error
"""

def create_test_fixture_file(file_path: str, content: str):
    """Helper to create a temporary file for testing."""
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

def cleanup_test_fixture_file(file_path: str):
    """Helper to remove a temporary file."""
    if os.path.exists(file_path):
        os.remove(file_path)

if __name__ == '__main__':
    TEST_DIR = "test_fixtures/prompt_map"
    os.makedirs(TEST_DIR, exist_ok=True)

    print("--- Testing PROMPT_MAP Parser ---")

    # Test case 1: Valid PROMPT_MAP
    valid_file = os.path.join(TEST_DIR, "valid_prompt_map.yaml")
    create_test_fixture_file(valid_file, VALID_PROMPT_MAP_CONTENT)
    print(f"\nTesting with valid file: {valid_file}")
    try:
        parser = PromptMapParser(valid_file)
        parser.load_and_validate()
        print("Validation PASSED.")
        print(f"Loaded data keys: {parser.get_logical_marker_ids()}")
    except (FileNotFoundError, PromptMapValidationError, yaml.YAMLError) as e:
        print(f"Validation FAILED: {e}")
    finally:
        cleanup_test_fixture_file(valid_file)

    # Test case 2: Missing LONG_RANGE_FRAME
    missing_lrf_file = os.path.join(TEST_DIR, "missing_lrf_prompt_map.yaml")
    create_test_fixture_file(missing_lrf_file, MISSING_LRF_PROMPT_MAP_CONTENT)
    print(f"\nTesting with missing LONG_RANGE_FRAME: {missing_lrf_file}")
    try:
        parser = PromptMapParser(missing_lrf_file)
        parser.load_and_validate()
        print("Validation PASSED (unexpected).")
    except PromptMapValidationError as e:
        print(f"Validation FAILED as expected: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        cleanup_test_fixture_file(missing_lrf_file)

    # Test case 3: Empty LOCAL_TRANSFORMATION
    empty_lt_file = os.path.join(TEST_DIR, "empty_lt_prompt_map.yaml")
    create_test_fixture_file(empty_lt_file, EMPTY_LT_PROMPT_MAP_CONTENT)
    print(f"\nTesting with empty LOCAL_TRANSFORMATION: {empty_lt_file}")
    try:
        parser = PromptMapParser(empty_lt_file)
        parser.load_and_validate()
        print("Validation PASSED (unexpected).")
    except PromptMapValidationError as e:
        print(f"Validation FAILED as expected: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        cleanup_test_fixture_file(empty_lt_file)

    # Test case 4: Invalid marker ID
    invalid_id_file = os.path.join(TEST_DIR, "invalid_id_prompt_map.yaml")
    create_test_fixture_file(invalid_id_file, INVALID_ID_PROMPT_MAP_CONTENT)
    print(f"\nTesting with invalid marker ID: {invalid_id_file}")
    try:
        parser = PromptMapParser(invalid_id_file)
        parser.load_and_validate()
        print("Validation PASSED (unexpected).")
    except PromptMapValidationError as e:
        print(f"Validation FAILED as expected: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        cleanup_test_fixture_file(invalid_id_file)

    # Test case 5: Non-dictionary entry
    non_dict_entry_file = os.path.join(TEST_DIR, "non_dict_entry_prompt_map.yaml")
    create_test_fixture_file(non_dict_entry_file, NON_DICT_ENTRY_PROMPT_MAP_CONTENT)
    print(f"\nTesting with non-dictionary entry: {non_dict_entry_file}")
    try:
        parser = PromptMapParser(non_dict_entry_file)
        parser.load_and_validate()
        print("Validation PASSED (unexpected).")
    except PromptMapValidationError as e:
        print(f"Validation FAILED as expected: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        cleanup_test_fixture_file(non_dict_entry_file)

    # Test case 6: Empty PROMPT_MAP file
    empty_file = os.path.join(TEST_DIR, "empty_prompt_map.yaml")
    create_test_fixture_file(empty_file, EMPTY_PROMPT_MAP_CONTENT)
    print(f"\nTesting with empty file: {empty_file}")
    try:
        parser = PromptMapParser(empty_file)
        parser.load_and_validate()
        print("Validation PASSED (unexpected).")
    except PromptMapValidationError as e:
        print(f"Validation FAILED as expected: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        cleanup_test_fixture_file(empty_file)

    # Test case 7: Non-string values
    non_string_values_file = os.path.join(TEST_DIR, "non_string_values_prompt_map.yaml")
    create_test_fixture_file(non_string_values_file, NON_STRING_VALUES_CONTENT)
    print(f"\nTesting with non-string values: {non_string_values_file}")
    try:
        parser = PromptMapParser(non_string_values_file)
        parser.load_and_validate()
        print("Validation PASSED (unexpected).")
    except PromptMapValidationError as e:
        print(f"Validation FAILED as expected: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        cleanup_test_fixture_file(non_string_values_file)

    # Test case 8: Malformed YAML
    malformed_yaml_file = os.path.join(TEST_DIR, "malformed_yaml_prompt_map.yaml")
    create_test_fixture_file(malformed_yaml_file, MALFORMED_YAML_CONTENT)
    print(f"\nTesting with malformed YAML: {malformed_yaml_file}")
    try:
        parser = PromptMapParser(malformed_yaml_file)
        parser.load_and_validate()
        print("Validation PASSED (unexpected).")
    except PromptMapValidationError as e:
        print(f"Validation FAILED (expected YAML parsing error): {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        cleanup_test_fixture_file(malformed_yaml_file)

    # Test case 9: File not found
    non_existent_file = os.path.join(TEST_DIR, "non_existent_prompt_map.yaml")
    print(f"\nTesting with non-existent file: {non_existent_file}")
    try:
        parser = PromptMapParser(non_existent_file)
        parser.load_and_validate()
        print("Validation PASSED (unexpected).")
    except FileNotFoundError as e:
        print(f"Validation FAILED as expected: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    print("\n--- PROMPT_MAP Parser Testing Complete ---")
