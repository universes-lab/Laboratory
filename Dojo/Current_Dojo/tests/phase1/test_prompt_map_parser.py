"""
Tests for the PromptMapParser.
"""

import unittest
import re
import yaml

from src.parser.prompt_map_parser import PromptMapParser

class TestPromptMapParser(unittest.TestCase):

    def setUp(self):
        """Set up test fixtures, if any."""
        self.parser = PromptMapParser()
        # Use a consistent temporary directory path for creating test files
        self.temp_dir = "D:/Gemini/.gemini/tmp/dojo/"
        # Ensure the temporary directory exists, create it if it doesn't
        import os
        os.makedirs(self.temp_dir, exist_ok=True)

    def tearDown(self):
        """Clean up test fixtures, if any."""
        import os
        # Clean up temporary files created by tests
        for file_name in os.listdir(self.temp_dir):
            if file_name.endswith(('.yaml', '.yml')):
                file_path = os.path.join(self.temp_dir, file_name)
                try:
                    os.remove(file_path)
                except OSError as e:
                    print(f"Error removing temporary file {file_path}: {e}")

    def test_valid_prompt_map(self):
        """Test parsing a valid PROMPT_MAP.yaml file."""
        valid_yaml_content = """
MP:0001:
  LONG_RANGE_FRAME: |-
    This is a long range frame.
  LOCAL_TRANSFORMATION: |-
    This is a local transformation.
MP:0005:
  LONG_RANGE_FRAME: |-
    Another long range frame.
  LOCAL_TRANSFORMATION: |-
    Another local transformation.
"""
        file_path = self.temp_dir + "valid_prompt_map.yaml"
        with open(file_path, 'w') as f:
            f.write(valid_yaml_content)

        expected_map = {
            'MP:0001': {
                'long_range_frame': 'This is a long range frame.',
                'local_transformation': 'This is a local transformation.'
            },
            'MP:0005': {
                'long_range_frame': 'Another long range frame.',
                'local_transformation': 'Another local transformation.'
            }
        }
        parsed_map = self.parser.parse(file_path)
        self.assertEqual(parsed_map, expected_map)

    def test_missing_required_field(self):
        """Test for missing required fields, should raise ValueError."""
        invalid_yaml_content = """
MP:0001:
  LONG_RANGE_FRAME: |-
    This is a long range frame.
MP:0002:
  LOCAL_TRANSFORMATION: |-
    This is a local transformation.
"""
        file_path = self.temp_dir + "invalid_prompt_map_missing_field.yaml"
        with open(file_path, 'w') as f:
            f.write(invalid_yaml_content)

        with self.assertRaisesRegex(ValueError, "PROMPT_ENTRY_INVALID: Missing or invalid 'LOCAL_TRANSFORMATION' for marker 'MP:0001'."):
            self.parser.parse(file_path)

    def test_empty_required_field(self):
        """Test for empty or whitespace-only required fields, should raise ValueError."""
        invalid_yaml_content = """
MP:0001:
  LONG_RANGE_FRAME: |-
    
  LOCAL_TRANSFORMATION: |-
    This is a local transformation.
"""
        file_path = self.temp_dir + "empty_field_prompt_map.yaml"
        with open(file_path, 'w') as f:
            f.write(invalid_yaml_content)

        with self.assertRaisesRegex(ValueError, "PROMPT_ENTRY_INVALID: Missing or invalid 'LONG_RANGE_FRAME' for marker 'MP:0001'."):
            self.parser.parse(file_path)

    def test_invalid_marker_key(self):
        """Test for invalid marker key format, should raise ValueError."""
        invalid_yaml_content = """
MP0001:
  LONG_RANGE_FRAME: |-
    This is a long range frame.
  LOCAL_TRANSFORMATION: |-
    This is a local transformation.
"""
        file_path = self.temp_dir + "invalid_key_prompt_map.yaml"
        with open(file_path, 'w') as f:
            f.write(invalid_yaml_content)

        with self.assertRaisesRegex(ValueError, "PROMPT_ENTRY_INVALID: Invalid marker key format: MP0001"):
            self.parser.parse(file_path)

    def test_malformed_invalid_structure(self):
        """Test for malformed YAML and invalid structure, should raise ValueError."""
        # Malformed YAML (missing colon for MP:0002 entry)
        invalid_yaml_content = """
MP:0001:
  LONG_RANGE_FRAME: |-
    This is a long range frame.
  LOCAL_TRANSFORMATION: |-
    This is a local transformation.
MP:0002 invalid_entry
"""
        file_path = self.temp_dir + "malformed_prompt_map.yaml"
        with open(file_path, 'w') as f:
            f.write(invalid_yaml_content)

        # The error should be 'Malformed YAML' due to the syntax error.
        with self.assertRaisesRegex(ValueError, "PROMPT_ENTRY_INVALID: Malformed YAML"):
            self.parser.parse(file_path)

    def test_empty_prompt_map(self):
        """Test with an empty PROMPT_MAP, should return an empty dictionary."""
        empty_yaml_content = ""
        file_path = self.temp_dir + "empty_prompt_map.yaml"
        with open(file_path, 'w') as f:
            f.write(empty_yaml_content)

        expected_map = {}
        marker_graph = self.parser.parse(file_path)
        self.assertEqual(marker_graph, expected_map)

if __name__ == '__main__':
    unittest.main()
