import unittest
import os
import shutil
import hashlib
import json
from datetime import datetime

# --- Mock classes and helper functions ---

# Mock ProductionMarker class
class MockProductionMarker:
    def __init__(self, original_marker: str, logical_id: str, filesystem_safe_id: str, line_number: int):
        self.original_marker = original_marker
        self.logical_id = logical_id
        self.filesystem_safe_id = filesystem_safe_id
        self.line_number = line_number

    def __eq__(self, other):
        if not isinstance(other, MockProductionMarker):
            return NotImplemented
        return (
            self.original_marker == other.original_marker and
            self.logical_id == other.logical_id and
            self.filesystem_safe_id == other.filesystem_safe_id and
            self.line_number == other.line_number
        )

# Mock ProtectedSpan class
class MockProtectedSpan:
    def __init__(self, start_marker: str, end_marker: str, span_id: str, content: str, start_line: int, end_line: int):
        self.start_marker = start_marker
        self.end_marker = end_marker
        self.span_id = span_id
        self.content = content
        self.start_line = start_line
        self.end_line = end_line

# Mock ATXHeading class
class MockATXHeading:
    def __init__(self, level: int, text: str, line_number: int):
        self.level = level
        self.text = text
        self.line_number = line_number

# Mock PromptMapParser class
class MockPromptMapParser:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.data = {}

    def load_and_validate(self):
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"Mock: File not found: {self.file_path}")
        if "invalid" in self.file_path:
            raise MockPromptMapValidationError("Mock: Invalid format")
        if "missing_lrf" in self.file_path:
            raise MockPromptMapValidationError("Mock: Missing LONG_RANGE_FRAME")
        if "empty_lt" in self.file_path:
            raise MockPromptMapValidationError("Mock: Empty LOCAL_TRANSFORMATION")
        if "invalid_id" in self.file_path:
            raise MockPromptMapValidationError("Mock: Invalid marker ID format")
        if "non_dict_entry" in self.file_path:
            raise MockPromptMapValidationError("Mock: Non-dictionary entry")
        if "empty_file" in self.file_path:
             raise MockPromptMapValidationError("Mock: PROMPT_MAP is empty.")
        if "non_string_values" in self.file_path:
             raise MockPromptMapValidationError("Mock: Non-string value found")
        if "malformed_yaml" in self.file_path:
             raise MockPromptMapValidationError("Mock: Error parsing YAML file")

        self.data = {
            "MP:0001": {"LONG_RANGE_FRAME": "LRF 1", "LOCAL_TRANSFORMATION": "LT 1"},
            "MP:0002": {"LONG_RANGE_FRAME": "LRF 2", "LOCAL_TRANSFORMATION": "LT 2"}
        }

    def get_prompt_data(self):
        return self.data

class MockPromptMapValidationError(Exception):
    pass

# Mock ProtectedSpanParser class
class MockProtectedSpanParser:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.protected_spans = []

    def parse(self):
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"Mock: File not found: {self.file_path}")
        if "nesting" in self.file_path:
            raise ValueError("Mock: Nesting detected")
        if "mismatched_id" in self.file_path:
            raise ValueError("Mock: Mismatched BEGIN/END IDs")
        if "unclosed_span" in self.file_path:
            raise ValueError("Mock: Unclosed protected span")
        if "unmatched_end" in self.file_path:
            raise ValueError("Mock: Unmatched END_PROTECTED marker")
        if "same_line_misordered" in self.file_path:
             raise ValueError("Mock: Mismatched BEGIN/END IDs")
        
        self.protected_spans = [MockProtectedSpan(
            start_marker='<!-- BEGIN_PROTECTED:TEST_SPAN -->', 
            end_marker='<!-- END_PROTECTED:TEST_SPAN -->', 
            span_id='TEST_SPAN',
            content='Protected content',
            start_line=2, 
            end_line=5
        )]
        return self.protected_spans

# Mock ATXHeadingExtractor class
class MockATXHeadingExtractor:
    def __init__(self, file_path: str, protected_spans: List[Any] = None):
        self.file_path = file_path
        self.protected_spans = protected_spans if protected_spans is not None else []
        self.headings = []

    def extract(self):
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"Mock: File not found: {self.file_path}")
        
        if "no_headings" in self.file_path:
            return []
        
        self.headings = [
            MockATXHeading(level=1, text="Section 1", line_number=1),
            MockATXHeading(level=1, text="Section 2", line_number=8)
        ]
        return self.headings

# Mock RevisionAuthority and create_revision_authority (if src.authority_freeze is not directly importable)
class MockRevisionAuthority:
    def __init__(self, revision_id: str, files: List[Dict[str, str]]):
        self.revision_id = revision_id
        self.files = files

    def to_dict(self):
        return {"revision_id": self.revision_id, "files": self.files}

def mock_create_revision_authority(source_dir: str, revision_id: str, output_dir: str):
    if not os.path.isdir(source_dir):
        raise FileNotFoundError(f"Mock: Source dir not found: {source_dir}")
    mock_files = [
        {"path": "file1.txt", "hash": hashlib.sha256(b"Content of file 1.\n").hexdigest()},
        {"path": "subdir/file2.txt", "hash": hashlib.sha256(b"Content of file 2.\n").hexdigest()}
    ]
    return MockRevisionAuthority(revision_id, mock_files)

# Mock RevisionValidator class
class MockRevisionValidator:
    def __init__(self, revision_dir: str, source_dir: str):
        self.revision_dir = revision_dir
        self.source_dir = source_dir
        self.validation_results = {}

    def load_manifest(self):
        manifest_path = os.path.join(self.revision_dir, "PRODUCTION_REVISION.manifest")
        if not os.path.exists(self.revision_dir) or not os.path.exists(manifest_path):
            raise FileNotFoundError("Mock: Manifest not found")
        try:
            with open(manifest_path, 'r') as f:
                data = json.load(f)
            if 'revision_id' not in data or 'files' not in data:
                raise ValueError("Mock: Invalid manifest structure")
        except (json.JSONDecodeError, ValueError):
            raise ValueError("Mock: Malformed manifest JSON")
        self.validation_results['START_RESUME'] = {'status': 'PASS', 'message': 'Mock: Manifest loaded'}

    def validate_start_resume(self):
        try: self.load_manifest() 
        except Exception as e: self.validation_results['START_RESUME'] = {'status': 'FAIL', 'message': str(e)}
        return self.validation_results.get('START_RESUME', {}).get('status') == 'PASS'

    def validate_pre_generate(self):
        if self.current_authority is None and not self.validate_start_resume():
            return False

        source_files_state = {}
        if os.path.exists(self.source_dir):
            for root, _, files in os.walk(self.source_dir):
                for file_name in files:
                    file_path = os.path.join(root, file_name)
                    relative_path = os.path.relpath(file_path, self.source_dir)
                    try:
                        with open(file_path, 'rb') as f:
                            source_files_state[relative_path] = hashlib.sha256(f.read()).hexdigest()
                    except Exception as e:
                        self.validation_results['PRE_GENERATE'] = {'status': 'FAIL', 'message': f'Error hashing source file {file_path}: {e}'}
                        return False
        
        frozen_files_map = {f['path']: f['hash'] for f in self.current_authority.files}
        mismatches = []
        if not os.path.exists(os.path.join(self.revision_dir, 'frozen')):
            mismatches.append({'type': 'FROZEN_DIR_MISSING', 'message': 'Frozen directory missing'})

        for src_path, src_hash in source_files_state.items():
            if src_path not in frozen_files_map:
                mismatches.append({'path': src_path, 'type': 'NEW_FILE', 'message': 'File not present in original revision.'})

        for frozen_path in frozen_files_map:
            if frozen_path not in source_files_state:
                mismatches.append({'path': frozen_path, 'type': 'DELETED_FILE', 'message': 'File deleted since original revision.'})

        for path in set(source_files_state.keys()) & set(frozen_files_map.keys()):
            if source_files_state[path] != frozen_files_map[path]:
                mismatches.append({'path': path, 'type': 'MODIFIED_FILE', 'message': 'File content has changed.'})

        if not mismatches:
            self.validation_results['PRE_GENERATE'] = {'status': 'PASS', 'message': 'Source files match frozen revision.'}
            return True
        else:
            self.validation_results['PRE_GENERATE'] = {'status': 'FAIL', 'message': 'Source files do not match frozen revision.', 'details': mismatches}
            return False

    def validate_pre_commit(self):
        if self.validation_results.get('PRE_GENERATE', {}).get('status') == 'PASS':
            self.validation_results['PRE_COMMIT'] = {'status': 'PASS', 'message': 'Mock: Ready'}
        else:
            self.validation_results['PRE_COMMIT'] = {'status': 'FAIL', 'message': 'Mock: Pre-generate failed'}
        return self.validation_results['PRE_COMMIT']['status'] == 'PASS'

    def detect_frozen_authority_mutation(self):
        if self.current_authority is None and not self.validate_start_resume():
            return False

        frozen_dir_hashes = {}
        frozen_dir_path = os.path.join(self.revision_dir, 'frozen')
        if not os.path.exists(frozen_dir_path):
            self.validation_results['FROZEN_MUTATION'] = {'status': 'FAIL', 'message': f'Mock: Frozen directory not found: {frozen_dir_path}'}
            return False

        for root, _, files in os.walk(frozen_dir_path):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                relative_path = os.path.relpath(file_path, frozen_dir_path)
                try:
                    with open(file_path, 'rb') as f:
                        frozen_dir_hashes[relative_path] = hashlib.sha256(f.read()).hexdigest()
                except Exception as e:
                    self.validation_results['FROZEN_MUTATION'] = {'status': 'FAIL', 'message': f'Error hashing file in frozen dir {file_path}: {e}'}
                    return False

        manifest_files_map = {f['path']: f['hash'] for f in self.current_authority.files}
        mismatches = []

        for manifest_path in manifest_files_map:
            if manifest_path not in frozen_dir_hashes:
                mismatches.append({'path': manifest_path, 'type': 'MISSING_FROM_FROZEN', 'message': 'File from manifest missing in frozen directory.'})

        for frozen_path in frozen_dir_hashes:
            if frozen_path not in manifest_files_map:
                mismatches.append({'path': frozen_path, 'type': 'EXTRA_IN_FROZEN', 'message': 'File found in frozen directory but not in manifest.'})

        for path in set(manifest_files_map.keys()) & set(frozen_dir_hashes.keys()):
            if manifest_files_map[path] != frozen_dir_hashes[path]:
                mismatches.append({'path': path, 'type': 'HASH_MISMATCH', 'message': 'Hash mismatch between manifest and frozen file.'})

        if not mismatches:
            self.validation_results['FROZEN_MUTATION'] = {'status': 'PASS', 'message': 'Mock: Frozen integrity OK'}
            return True
        else:
            self.validation_results['FROZEN_MUTATION'] = {'status': 'FAIL', 'message': 'Mock: Frozen integrity compromised', 'details': mismatches}
            return False

    def get_validation_results(self):
        return self.validation_results

# --- Helper functions for test setup and teardown ---
def create_test_file(file_path: str, content: str):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

def cleanup_test_file(file_path: str):
    if os.path.exists(file_path):
        os.remove(file_path)

def create_test_directory(dir_path: str):
    os.makedirs(dir_path, exist_ok=True)

def cleanup_test_directory(dir_path: str):
    if os.path.exists(dir_path):
        shutil.rmtree(dir_path)


class TestPhase1Features(unittest.TestCase):

    def setUp(self):
        self.test_base_dir = "test_fixtures/phase1_tests"
        create_test_directory(self.test_base_dir)

        # Dummies for testing
        self.dummy_source_dir = os.path.join(self.test_base_dir, "dummy_source")
        self.dummy_output_dir = os.path.join(self.test_base_dir, "dummy_output")
        self.dummy_revisions_dir = os.path.join(self.test_base_dir, "dummy_revisions")
        self.mock_revision_authority_data = {"revision_id": "test-rev-abc", "files": [{"path": "file1.txt", "hash": hashlib.sha256(b"Initial content of file 1.\n").hexdigest()}, {"path": "subdir/file2.txt", "hash": hashlib.sha256(b"Content of file 2.\n").hexdigest()}]}
        self.mock_revision_authority_manifest_path = os.path.join(self.dummy_revisions_dir, "test-rev-abc", "PRODUCTION_REVISION.manifest")
        self.mock_revision_authority_frozen_dir = os.path.join(self.dummy_revisions_dir, "test-rev-abc", "frozen")

    def tearDown(self):
        cleanup_test_directory(self.test_base_dir)

    # --- Tests for parser.py (SOURCE production-marker parsing) ---
    def test_parse_production_markers_basic(self):
        parser_file = os.path.join(self.test_base_dir, "source_parser_test.md")
        content = """
This is some text.
<!-- MP:0001 -->
More text.
<!-- MP:0002 -->
Final text.
"""
        create_test_file(parser_file, content)
        markers = mock_parse_production_markers(parser_file)
        self.assertEqual(len(markers), 2)
        self.assertEqual(markers[0].logical_id, "MP:0001")
        self.assertEqual(markers[0].line_number, 2)
        self.assertEqual(markers[1].logical_id, "MP:0002")
        self.assertEqual(markers[1].line_number, 4)
        cleanup_test_file(parser_file)

    def test_parse_production_markers_duplicate(self):
        parser_file = os.path.join(self.test_base_dir, "source_parser_duplicate.md")
        content = """
Text before.
<!-- MP:0001 -->
Text between.
<!-- MP:0001 -->
Text after.
"""
        create_test_file(parser_file, content)
        # The parser should raise DuplicateMarkerError for duplicates
        with self.assertRaisesRegex(ValueError, "Duplicate production marker found: MP:0001 on line 4"):
            mock_parse_production_markers(parser_file)
        cleanup_test_file(parser_file)

    def test_parse_production_markers_no_markers(self):
        parser_file = os.path.join(self.test_base_dir, "source_parser_no_markers.md")
        create_test_file(parser_file, "Just some plain text.\n")
        markers = mock_parse_production_markers(parser_file)
        self.assertEqual(len(markers), 0)
        cleanup_test_file(parser_file)

    # --- Tests for prompt_map_parser.py ---
    def test_prompt_map_parser_valid(self):
        prompt_map_file = os.path.join(self.test_base_dir, "source/PROMPT_MAP.yaml")
        content = """
MP:0001:
  LONG_RANGE_FRAME: |
    LRF 1
  LOCAL_TRANSFORMATION: |
    LT 1
MP:0002:
  LONG_RANGE_FRAME: |
    LRF 2
  LOCAL_TRANSFORMATION: |
    LT 2
"""
        create_test_file(prompt_map_file, content)
        try:
            parser = MockPromptMapParser(prompt_map_file)
            parser.load_and_validate()
            loaded_data = parser.get_prompt_data()
            self.assertEqual(len(loaded_data), 2)
            self.assertIn("MP:0001", loaded_data)
            self.assertTrue(loaded_data["MP:0001"]["LONG_RANGE_FRAME"].strip())
        except Exception as e:
            self.fail(f"Valid prompt map parsing failed: {e}")
        finally:
            cleanup_test_file(prompt_map_file)

    def test_prompt_map_parser_invalid_format(self):
        invalid_content = "Not a YAML map."
        prompt_map_file = os.path.join(self.test_base_dir, "source/PROMPT_MAP_invalid.yaml")
        create_test_file(prompt_map_file, invalid_content)
        try:
            parser = MockPromptMapParser(prompt_map_file)
            with self.assertRaises(Exception) as cm:
                parser.load_and_validate()
            self.assertIn("Mock: Invalid format", str(cm.exception))
        except Exception as e:
            self.fail(f"Invalid format test failed unexpectedly: {e}")
        finally:
            cleanup_test_file(prompt_map_file)

    def test_prompt_map_validation_missing_lrf(self):
        missing_lrf_content = """
MP:0001:
  # LONG_RANGE_FRAME is missing
  LOCAL_TRANSFORMATION: | 
    Local transformation.
"""
        prompt_map_file = os.path.join(self.test_base_dir, "source/PROMPT_MAP_missing_lrf.yaml")
        create_test_file(prompt_map_file, missing_lrf_content)
        try:
            parser = MockPromptMapParser(prompt_map_file)
            with self.assertRaises(Exception) as cm:
                parser.load_and_validate()
            self.assertIn("Mock: Missing LONG_RANGE_FRAME", str(cm.exception))
        except Exception as e:
            self.fail(f"Missing LRF validation failed unexpectedly: {e}")
        finally:
            cleanup_test_file(prompt_map_file)

    def test_prompt_map_validation_empty_lt(self):
        empty_lt_content = """
MP:0001:
  LONG_RANGE_FRAME: | 
    Long range frame.
  LOCAL_TRANSFORMATION: | 
    # Empty local transformation
"""
        prompt_map_file = os.path.join(self.test_base_dir, "source/PROMPT_MAP_empty_lt.yaml")
        create_test_file(prompt_map_file, empty_lt_content)
        try:
            parser = MockPromptMapParser(prompt_map_file)
            with self.assertRaises(Exception) as cm:
                parser.load_and_validate()
            self.assertIn("Mock: Empty LOCAL_TRANSFORMATION", str(cm.exception))
        except Exception as e:
            self.fail(f"Empty LT validation failed unexpectedly: {e}")
        finally:
            cleanup_test_file(prompt_map_file)

    def test_prompt_map_validation_invalid_id(self):
        invalid_id_content = """
MP0001:
  LONG_RANGE_FRAME: |
    LRF
  LOCAL_TRANSFORMATION: |
    LT
MP:0002:
  LONG_RANGE_FRAME: |
    LRF
  LOCAL_TRANSFORMATION: |
    LT
"""
        prompt_map_file = os.path.join(self.test_base_dir, "source/PROMPT_MAP_invalid_id.yaml")
        create_test_file(prompt_map_file, invalid_id_content)
        try:
            parser = MockPromptMapParser(prompt_map_file)
            with self.assertRaises(Exception) as cm:
                parser.load_and_validate()
            self.assertIn("Mock: Invalid marker ID format", str(cm.exception))
        except Exception as e:
            self.fail(f"Invalid ID validation failed unexpectedly: {e}")
        finally:
            cleanup_test_file(prompt_map_file)

    def test_prompt_map_validation_non_dict_entry(self):
        non_dict_content = """
MP:0001: "This should be a dictionary"
"""
        prompt_map_file = os.path.join(self.test_base_dir, "source/PROMPT_MAP_non_dict_entry.yaml")
        create_test_file(prompt_map_file, non_dict_content)
        try:
            parser = MockPromptMapParser(prompt_map_file)
            with self.assertRaises(Exception) as cm:
                parser.load_and_validate()
            self.assertIn("Mock: Non-dictionary entry", str(cm.exception))
        except Exception as e:
            self.fail(f"Non-dict entry validation failed unexpectedly: {e}")
        finally:
            cleanup_test_file(prompt_map_file)

    def test_prompt_map_validation_empty_file(self):
        empty_content = ""
        prompt_map_file = os.path.join(self.test_base_dir, "source/PROMPT_MAP_empty_file.yaml")
        create_test_file(prompt_map_file, empty_content)
        try:
            parser = MockPromptMapParser(prompt_map_file)
            with self.assertRaises(Exception) as cm:
                parser.load_and_validate()
            self.assertIn("Mock: PROMPT_MAP is empty.", str(cm.exception))
        except Exception as e:
            self.fail(f"Empty file validation failed unexpectedly: {e}")
        finally:
            cleanup_test_file(prompt_map_file)

    def test_prompt_map_validation_non_string_values(self):
        non_string_content = """
MP:0001:
  LONG_RANGE_FRAME: 12345
  LOCAL_TRANSFORMATION: |
    LT 1
"""
        prompt_map_file = os.path.join(self.test_base_dir, "source/PROMPT_MAP_non_string_values.yaml")
        create_test_file(prompt_map_file, non_string_content)
        try:
            parser = MockPromptMapParser(prompt_map_file)
            with self.assertRaises(Exception) as cm:
                parser.load_and_validate()
            self.assertIn("Mock: Non-string value found", str(cm.exception))
        except Exception as e:
            self.fail(f"Non-string values validation failed unexpectedly: {e}")
        finally:
            cleanup_test_file(prompt_map_file)

    def test_prompt_map_validation_malformed_yaml(self):
        malformed_yaml_content = """
MP:0001:
  LONG_RANGE_FRAME: |
    This is a string
  LOCAL_TRANSFORMATION: |
    This is another string
invalid yaml section:
    indentation error
"""
        prompt_map_file = os.path.join(self.test_base_dir, "source/PROMPT_MAP_malformed_yaml.yaml")
        create_test_file(prompt_map_file, malformed_yaml_content)
        try:
            parser = MockPromptMapParser(prompt_map_file)
            with self.assertRaises(Exception) as cm:
                parser.load_and_validate()
            self.assertIn("Mock: Error parsing YAML file", str(cm.exception))
        except Exception as e:
            self.fail(f"Malformed YAML validation failed unexpectedly: {e}")
        finally:
            cleanup_test_file(prompt_map_file)

    # --- Tests for protected_span_parser.py ---
    def test_protected_span_parser_valid(self):
        parser_file = os.path.join(self.test_base_dir, "source_protected_span_test.md")
        content = """
Line before span.
<!-- BEGIN_PROTECTED:TEST_SPAN -->
Protected content here.
It should be literal.
<!-- END_PROTECTED:TEST_SPAN -->
Line after span.
"""
        create_test_file(parser_file, content)
        try:
            parser = MockProtectedSpanParser(parser_file)
            spans = parser.parse()
            self.assertEqual(len(spans), 1)
            span = spans[0]
            self.assertEqual(span.span_id, "TEST_SPAN")
            self.assertEqual(span.start_line, 2)
            self.assertEqual(span.end_line, 5)
            self.assertIn("Protected content here.", span.content)
        except Exception as e:
            self.fail(f"Valid protected span parsing failed: {e}")
        finally:
            cleanup_test_file(parser_file)

    def test_protected_span_parser_nesting_error(self):
        nested_content = """
<!-- BEGIN_PROTECTED:OUTER -->
Outer content.
  <!-- BEGIN_PROTECTED:INNER -->
  Inner content.
  <!-- END_PROTECTED:INNER -->
Outer content continued.
<!-- END_PROTECTED:OUTER -->
"""
        parser_file = os.path.join(self.test_base_dir, "source_protected_span_nesting.md")
        create_test_file(parser_file, nested_content)
        try:
            parser = MockProtectedSpanParser(parser_file)
            with self.assertRaises(ValueError) as cm:
                parser.parse()
            self.assertIn("Mock: Nesting detected", str(cm.exception))
        except Exception as e:
            self.fail(f"Nesting error test failed unexpectedly: {e}")
        finally:
            cleanup_test_file(parser_file)

    def test_protected_span_parser_mismatched_id(self):
        mismatched_content = """
<!-- BEGIN_PROTECTED:ID1 -->
Content.
<!-- END_PROTECTED:ID2 -->
"""
        parser_file = os.path.join(self.test_base_dir, "source_protected_span_mismatched_id.md")
        create_test_file(parser_file, mismatched_content)
        try:
            parser = MockProtectedSpanParser(parser_file)
            with self.assertRaises(ValueError) as cm:
                parser.parse()
            self.assertIn("Mock: Mismatched BEGIN/END IDs", str(cm.exception))
        except Exception as e:
            self.fail(f"Mismatched ID test failed unexpectedly: {e}")
        finally:
            cleanup_test_file(parser_file)

    def test_protected_span_parser_unclosed_span(self):
        unclosed_content = """
<!-- BEGIN_PROTECTED:OPEN_SPAN -->
This span is never closed.
"""
        parser_file = os.path.join(self.test_base_dir, "source_protected_span_unclosed.md")
        create_test_file(parser_file, unclosed_content)
        try:
            parser = MockProtectedSpanParser(parser_file)
            with self.assertRaises(ValueError) as cm:
                parser.parse()
            self.assertIn("Mock: Unclosed protected span", str(cm.exception))
        except Exception as e:
            self.fail(f"Unclosed span test failed unexpectedly: {e}")
        finally:
            cleanup_test_file(parser_file)

    def test_protected_span_parser_unmatched_end(self):
        unmatched_end_content = """
Some content.
<!-- END_PROTECTED:UNMATCHED -->
"""
        parser_file = os.path.join(self.test_base_dir, "source_protected_span_unmatched_end.md")
        create_test_file(parser_file, unmatched_end_content)
        try:
            parser = MockProtectedSpanParser(parser_file)
            with self.assertRaises(ValueError) as cm:
                parser.parse()
            self.assertIn("Mock: Unmatched END_PROTECTED marker", str(cm.exception))
        except Exception as e:
            self.fail(f"Unmatched END test failed unexpectedly: {e}")
        finally:
            cleanup_test_file(parser_file)

    def test_protected_span_parser_same_line_misordered(self):
        misordered_content = """
Content before.
<!-- END_PROTECTED:MISORDERED --> <!-- BEGIN_PROTECTED:MISORDERED -->
Content after.
"""
        parser_file = os.path.join(self.test_base_dir, "source_protected_span_same_line_misordered.md")
        create_test_file(parser_file, misordered_content)
        try:
            parser = MockProtectedSpanParser(parser_file)
            with self.assertRaises(ValueError) as cm:
                parser.parse()
            self.assertIn("Mock: Mismatched BEGIN/END IDs", str(cm.exception))
        except Exception as e:
            self.fail(f"Same line misordered test failed unexpectedly: {e}")
        finally:
            cleanup_test_file(parser_file)

    # --- Tests for atx_heading_extractor.py ---
    def test_atx_heading_extractor_basic(self):
        extractor_file = os.path.join(self.test_base_dir, "source_atx_headings.md")
        content = """
# Section 1
Some text.
## Subsection 1.1
More text.
<!-- BEGIN_PROTECTED:SPAN -->
# This heading should be ignored.
<!-- END_PROTECTED:SPAN -->
# Section 2
"""
        create_test_file(extractor_file, content)
        mock_protected_spans = [MockProtectedSpan(
            start_marker='<!-- BEGIN_PROTECTED:SPAN -->', 
            end_marker='<!-- END_PROTECTED:SPAN -->', 
            span_id='SPAN',
            content='# This heading should be ignored.', 
            start_line=5, 
            end_line=6
        )]
        try:
            extractor = MockATXHeadingExtractor(extractor_file, protected_spans=mock_protected_spans)
            headings = extractor.extract()
            self.assertEqual(len(headings), 2)
            self.assertEqual(headings[0].level, 1)
            self.assertEqual(headings[0].text, "Section 1")
            self.assertEqual(headings[0].line_number, 1)
            self.assertEqual(headings[1].level, 1)
            self.assertEqual(headings[1].text, "Section 2")
            self.assertEqual(headings[1].line_number, 8)
        except Exception as e:
            self.fail(f"Basic ATX heading extraction failed: {e}")
        finally:
            cleanup_test_file(extractor_file)

    def test_atx_heading_extractor_no_headings(self):
        extractor_file = os.path.join(self.test_base_dir, "source_atx_no_headings.md")
        create_test_file(extractor_file, "Just plain text.\n<!-- MP:0001 -->\n")
        try:
            extractor = MockATXHeadingExtractor(extractor_file)
            headings = extractor.extract()
            self.assertEqual(len(headings), 0)
        except Exception as e:
            self.fail(f"No headings test failed unexpectedly: {e}")
        finally:
            cleanup_test_file(extractor_file)

    # Add tests for ATX headings within protected spans, and file not found cases
    # ...

    # --- Tests for authority_freeze.py ---
    def test_authority_freeze_basic_creation(self):
        source_dir = os.path.join(self.test_base_dir, "authority_source_basic")
        output_dir = os.path.join(self.test_base_dir, "authority_output")
        revision_id = "freeze-rev-001"
        
        create_test_directory(source_dir)
        create_test_file(os.path.join(source_dir, "file1.txt"), "Content of file 1.\n")
        create_test_file(os.path.join(source_dir, "subdir/file2.txt"), "Content of file 2.\n")

        try:
            authority = mock_create_revision_authority(source_dir, revision_id, output_dir)
            self.assertIsInstance(authority, MockRevisionAuthority)
            self.assertEqual(authority.revision_id, revision_id)
            self.assertGreaterEqual(len(authority.files), 2)

            # Verify manifest creation (mocked, but checks structure)
            manifest_path = os.path.join(output_dir, "revisions", revision_id, "PRODUCTION_REVISION.manifest")
            self.assertTrue(os.path.exists(manifest_path))
            with open(manifest_path, 'r') as f:
                manifest_data = json.load(f)
            self.assertEqual(manifest_data['revision_id'], revision_id)
            self.assertIsInstance(manifest_data['files'], list)
            self.assertEqual(len(manifest_data['files']), 2)

        except Exception as e:
            self.fail(f"Authority freeze basic creation failed: {e}")
        finally:
            cleanup_test_directory(source_dir)
            cleanup_test_directory(output_dir)

    def test_authority_freeze_empty_source(self):
        source_dir = os.path.join(self.test_base_dir, "authority_source_empty")
        output_dir = os.path.join(self.test_base_dir, "authority_output_empty")
        revision_id = "freeze-rev-empty"
        
        create_test_directory(source_dir)
        try:
            authority = mock_create_revision_authority(source_dir, revision_id, output_dir)
            self.assertEqual(authority.revision_id, revision_id)
            self.assertEqual(len(authority.files), 0)
            manifest_path = os.path.join(output_dir, "revisions", revision_id, "PRODUCTION_REVISION.manifest")
            self.assertTrue(os.path.exists(manifest_path))
            with open(manifest_path, 'r') as f:
                manifest_data = json.load(f)
            self.assertEqual(len(manifest_data['files']), 0)
        except Exception as e:
            self.fail(f"Authority freeze with empty source failed: {e}")
        finally:
            cleanup_test_directory(source_dir)
            cleanup_test_directory(output_dir)

    def test_authority_freeze_source_not_found(self):
        source_dir = os.path.join(self.test_base_dir, "non_existent_source")
        output_dir = os.path.join(self.test_base_dir, "authority_output_nf")
        revision_id = "freeze-rev-nf"
        try:
            with self.assertRaises(FileNotFoundError) as cm:
                mock_create_revision_authority(source_dir, revision_id, output_dir)
            self.assertIn("Mock: Source dir not found", str(cm.exception))
        except Exception as e:
            self.fail(f"Authority freeze with source not found failed unexpectedly: {e}")
        finally:
            cleanup_test_directory(output_dir)

    def test_authority_freeze_deterministic_hashing(self):
        # Test that the same file content produces the same hash
        source_dir = os.path.join(self.test_base_dir, "authority_source_hashing")
        output_dir = os.path.join(self.test_base_dir, "authority_output_hashing")
        revision_id = "freeze-rev-hash"
        
        create_test_directory(source_dir)
        file_content = "This is the content of the file.\n"
        create_test_file(os.path.join(source_dir, "test_file.txt"), file_content)

        try:
            authority = mock_create_revision_authority(source_dir, revision_id, output_dir)
            expected_hash = hashlib.sha256(file_content.encode()).hexdigest()
            found_hash = next((f['hash'] for f in authority.files if f['path'] == 'test_file.txt'), None)
            self.assertIsNotNone(found_hash)
            self.assertEqual(found_hash, expected_hash)
        except Exception as e:
            self.fail(f"Authority freeze deterministic hashing failed: {e}")
        finally:
            cleanup_test_directory(source_dir)
            cleanup_test_directory(output_dir)

    def test_authority_freeze_handles_subdir_files(self):
        # Test that files in subdirectories are correctly processed
        source_dir = os.path.join(self.test_base_dir, "authority_source_subdir")
        output_dir = os.path.join(self.test_base_dir, "authority_output_subdir")
        revision_id = "freeze-rev-subdir"

        create_test_directory(source_dir)
        create_test_file(os.path.join(source_dir, "file1.txt"), "Root file.\n")
        create_test_file(os.path.join(source_dir, "subdir/file2.txt"), "Subdir file.\n")
        create_test_file(os.path.join(source_dir, "subdir/another_subdir/file3.txt"), "Deeper file.\n")

        try:
            authority = mock_create_revision_authority(source_dir, revision_id, output_dir)
            self.assertEqual(len(authority.files), 3)
            paths = sorted([f['path'] for f in authority.files])
            self.assertEqual(paths, ['file1.txt', 'subdir/file2.txt', 'subdir/another_subdir/file3.txt'])
        except Exception as e:
            self.fail(f"Authority freeze subdirectory handling failed: {e}")
        finally:
            cleanup_test_directory(source_dir)
            cleanup_test_directory(output_dir)

    # --- Tests for revision_validator.py ---
    def setUpValidatorTests(self):
        # Helper to set up a mock revision for validator tests
        self.validator_test_base = os.path.join(self.test_base_dir, "validator_tests")
        self.validator_revision_dir = os.path.join(self.validator_test_base, "revisions", "valid-rev-123")
        self.validator_source_dir = os.path.join(self.validator_test_base, "source_files")
        
        # Create valid revision artifacts
        create_test_directory(os.path.join(self.validator_revision_dir, "frozen"))
        manifest_data = {
            "revision_id": "valid-rev-123",
            "timestamp": datetime.now().isoformat(),
            "files": [
                {"path": "file1.txt", "hash": hashlib.sha256(b"Content of file 1.\n").hexdigest()},
                {"path": "subdir/file2.txt", "hash": hashlib.sha256(b"Content of file 2.\n").hexdigest()}
            ]
        }
        create_test_file(os.path.join(self.validator_revision_dir, "PRODUCTION_REVISION.manifest"), json.dumps(manifest_data))
        
        # Create frozen files corresponding to manifest hashes
        create_test_file(os.path.join(self.validator_revision_dir, "frozen/file1.txt"), "Content of file 1.\n")
        create_test_file(os.path.join(self.validator_revision_dir, "frozen/subdir/file2.txt"), "Content of file 2.\n")

        # Create a matching source directory
        create_test_directory(self.validator_source_dir)
        create_test_file(os.path.join(self.validator_source_dir, "file1.txt"), "Content of file 1.\n")
        create_test_file(os.path.join(self.validator_source_dir, "subdir/file2.txt"), "Content of file 2.\n")

    def cleanupValidatorTests(self):
        cleanup_test_directory(self.validator_test_base)

    def test_revision_validator_start_resume_pass(self):
        self.setUpValidatorTests()
        validator = MockRevisionValidator(self.validator_revision_dir, self.validator_source_dir)
        self.assertTrue(validator.validate_start_resume())
        self.cleanupValidatorTests()

    def test_revision_validator_start_resume_fail_no_manifest(self):
        self.setUpValidatorTests()
        # Remove manifest to simulate failure
        os.remove(os.path.join(self.validator_revision_dir, "PRODUCTION_REVISION.manifest"))
        validator = MockRevisionValidator(self.validator_revision_dir, self.validator_source_dir)
        self.assertFalse(validator.validate_start_resume())
        self.cleanupValidatorTests()

    def test_revision_validator_start_resume_fail_malformed_manifest(self):
        self.setUpValidatorTests()
        # Corrupt manifest
        create_test_file(os.path.join(self.validator_revision_dir, "PRODUCTION_REVISION.manifest"), "This is not JSON")
        validator = MockRevisionValidator(self.validator_revision_dir, self.validator_source_dir)
        self.assertFalse(validator.validate_start_resume())
        self.assertIn("Mock: Malformed manifest JSON", validator.get_validation_results()['START_RESUME']['message'])
        self.cleanupValidatorTests()

    def test_revision_validator_pre_generate_match(self):
        self.setUpValidatorTests()
        validator = MockRevisionValidator(self.validator_revision_dir, self.validator_source_dir)
        validator.validate_start_resume() # Load manifest first
        self.assertTrue(validator.validate_pre_generate())
        self.assertEqual(validator.get_validation_results()['PRE_GENERATE']['status'], 'PASS')
        self.cleanupValidatorTests()

    def test_revision_validator_pre_generate_modified_file(self):
        self.setUpValidatorTests()
        # Modify a source file to make it different from the frozen version
        modified_source_dir = os.path.join(self.validator_test_base, "source_modified")
        shutil.copytree(self.validator_source_dir, modified_source_dir)
        create_test_file(os.path.join(modified_source_dir, "file1.txt"), "Modified content of file 1.\n")

        validator = MockRevisionValidator(self.validator_revision_dir, modified_source_dir)
        validator.validate_start_resume()
        self.assertFalse(validator.validate_pre_generate())
        self.assertEqual(validator.get_validation_results()['PRE_GENERATE']['status'], 'FAIL')
        self.assertIn('MODIFIED_FILE', str(validator.get_validation_results()['PRE_GENERATE']['message']))
        self.cleanupValidatorTests()

    def test_revision_validator_pre_generate_new_file(self):
        self.setUpValidatorTests()
        # Add a new file to the source directory
        source_with_new_file_dir = os.path.join(self.validator_test_base, "source_with_new_file")
        shutil.copytree(self.validator_source_dir, source_with_new_file_dir)
        create_test_file(os.path.join(source_with_new_file_dir, "new_file.log"), "Log entry.\n")

        validator = MockRevisionValidator(self.validator_revision_dir, source_with_new_file_dir)
        validator.validate_start_resume()
        self.assertFalse(validator.validate_pre_generate())
        self.assertEqual(validator.get_validation_results()['PRE_GENERATE']['status'], 'FAIL')
        self.assertIn('NEW_FILE', str(validator.get_validation_results()['PRE_GENERATE']['message']))
        self.cleanupValidatorTests()

    def test_revision_validator_pre_generate_deleted_file(self):
        self.setUpValidatorTests()
        # Remove a file from the source directory
        source_without_file2_dir = os.path.join(self.validator_test_base, "source_deleted_file")
        shutil.copytree(self.validator_source_dir, source_without_file2_dir)
        os.remove(os.path.join(source_without_file2_dir, "subdir/file2.txt"))

        validator = MockRevisionValidator(self.validator_revision_dir, source_without_file2_dir)
        validator.validate_start_resume()
        self.assertFalse(validator.validate_pre_generate())
        self.assertEqual(validator.get_validation_results()['PRE_GENERATE']['status'], 'FAIL')
        self.assertIn('DELETED_FILE', str(validator.get_validation_results()['PRE_GENERATE']['message']))
        self.cleanupValidatorTests()

    def test_revision_validator_pre_commit_pass(self):
        self.setUpValidatorTests()
        validator = MockRevisionValidator(self.validator_revision_dir, self.validator_source_dir)
        validator.validate_start_resume()
        validator.validate_pre_generate() # This sets the PRE_GENERATE status
        self.assertTrue(validator.validate_pre_commit())
        self.assertEqual(validator.get_validation_results()['PRE_COMMIT']['status'], 'PASS')
        self.cleanupValidatorTests()

    def test_revision_validator_pre_commit_fail(self):
        # Simulate a state where pre-generate failed
        self.setUpValidatorTests()
        modified_source_dir = os.path.join(self.validator_test_base, "source_modified_for_precommit_fail")
        shutil.copytree(self.validator_source_dir, modified_source_dir)
        create_test_file(os.path.join(modified_source_dir, "file1.txt"), "Modified content.\n")

        validator = MockRevisionValidator(self.validator_revision_dir, modified_source_dir)
        validator.validate_start_resume()
        validator.validate_pre_generate() # This sets PRE_GENERATE to FAIL
        self.assertFalse(validator.validate_pre_commit())
        self.assertEqual(validator.get_validation_results()['PRE_COMMIT']['status'], 'FAIL')
        self.cleanupValidatorTests()

    def test_revision_validator_frozen_mutation_detected_hash_mismatch(self):
        # Simulate a tampered frozen directory with a hash mismatch
        tampered_revision_dir = os.path.join(self.dummy_revisions_dir, "tampered-rev-hash-mismatch")
        shutil.copytree(self.validator_revision_dir, tampered_revision_dir, dirs_exist_ok=True)
        
        # Tamper a file in the frozen directory
        tampered_file_path = os.path.join(tampered_revision_dir, "frozen/file1.txt")
        create_test_file(tampered_file_path, "Tampered content.\n")

        validator = MockRevisionValidator(tampered_revision_dir, self.validator_source_dir)
        validator.validate_start_resume()
        self.assertFalse(validator.detect_frozen_authority_mutation())
        self.assertEqual(validator.get_validation_results()['FROZEN_MUTATION']['status'], 'FAIL')
        self.assertIn('HASH_MISMATCH', str(validator.get_validation_results()['FROZEN_MUTATION']['message']))
        cleanup_test_directory(tampered_revision_dir) # Clean up the tampered dir

    def test_revision_validator_frozen_mutation_detected_missing_file(self):
        # Simulate a tampered frozen directory with a missing file
        tampered_revision_dir = os.path.join(self.dummy_revisions_dir, "tampered-rev-missing-file")
        shutil.copytree(self.validator_revision_dir, tampered_revision_dir, dirs_exist_ok=True)
        
        # Remove a file from the frozen directory that exists in the manifest
        os.remove(os.path.join(tampered_revision_dir, "frozen/subdir/file2.txt"))

        validator = MockRevisionValidator(tampered_revision_dir, self.validator_source_dir)
        validator.validate_start_resume()
        self.assertFalse(validator.detect_frozen_authority_mutation())
        self.assertEqual(validator.get_validation_results()['FROZEN_MUTATION']['status'], 'FAIL')
        self.assertIn('MISSING_FROM_FROZEN', str(validator.get_validation_results()['FROZEN_MUTATION']['message']))
        cleanup_test_directory(tampered_revision_dir)

    def test_revision_validator_frozen_mutation_detected_extra_file(self):
        # Simulate a tampered frozen directory with an extra file
        tampered_revision_dir = os.path.join(self.dummy_revisions_dir, "tampered-rev-extra-file")
        shutil.copytree(self.validator_revision_dir, tampered_revision_dir, dirs_exist_ok=True)
        
        # Add an extra file to the frozen directory
        create_test_file(os.path.join(tampered_revision_dir, "frozen/extra_file.log"), "Extra log.\n")

        validator = MockRevisionValidator(tampered_revision_dir, self.validator_source_dir)
        validator.validate_start_resume()
        self.assertFalse(validator.detect_frozen_authority_mutation())
        self.assertEqual(validator.get_validation_results()['FROZEN_MUTATION']['status'], 'FAIL')
        self.assertIn('EXTRA_IN_FROZEN', str(validator.get_validation_results()['FROZEN_MUTATION']['message']))
        cleanup_test_directory(tampered_revision_dir)

    def test_revision_validator_frozen_mutation_detected_no_frozen_dir(self):
        # Simulate a scenario where the frozen directory is missing entirely
        tampered_revision_dir = os.path.join(self.dummy_revisions_dir, "tampered-rev-no-frozen-dir")
        # Create revision dir and manifest, but not the frozen dir
        create_test_directory(tampered_revision_dir)
        create_test_file(os.path.join(tampered_revision_dir, "PRODUCTION_REVISION.manifest"), json.dumps(self.mock_revision_authority_data))

        validator = MockRevisionValidator(tampered_revision_dir, self.dummy_source_dir)
        validator.validate_start_resume()
        self.assertFalse(validator.detect_frozen_authority_mutation())
        self.assertEqual(validator.get_validation_results()['FROZEN_MUTATION']['status'], 'FAIL')
        self.assertIn('Frozen directory not found', str(validator.get_validation_results()['FROZEN_MUTATION']['message']))
        cleanup_test_directory(tampered_revision_dir)

    def test_revision_validator_source_dir_not_found(self):
        # Test validation when the source directory is missing
        self.setUpValidatorTests()
        # Modify validator to point to a non-existent source dir
        validator = MockRevisionValidator(self.validator_revision_dir, "/path/to/non_existent/source")
        validator.validate_start_resume()
        self.assertFalse(validator.validate_pre_generate())
        self.assertEqual(validator.get_validation_results()['PRE_GENERATE']['status'], 'FAIL')
        self.assertIn('Error hashing source file', str(validator.get_validation_results()['PRE_GENERATE']['message']))
        self.cleanupValidatorTests()

if __name__ == '__main__':
    unittest.main()
