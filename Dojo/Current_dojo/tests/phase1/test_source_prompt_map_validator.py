import unittest
from src.parser.source_prompt_map_validator import SourcePromptMapValidator
from src.parser.source_parser import Marker

class TestSourcePromptMapValidator(unittest.TestCase):
    def setUp(self):
        self.validator = SourcePromptMapValidator()

    def test_perfect_correspondence(self):
        """Test 1 — Perfect Correspondence"""
        source_graph = [
            Marker(marker_id="MP:0001", filesystem_id="MP-0001"),
            Marker(marker_id="MP:0005", filesystem_id="MP-0005")
        ]
        prompt_map = {
            "MP:0001": {"LONG_RANGE_FRAME": "...", "LOCAL_TRANSFORMATION": "..."},
            "MP:0005": {"LONG_RANGE_FRAME": "...", "LOCAL_TRANSFORMATION": "..."}
        }
        self.assertTrue(self.validator.validate(source_graph, prompt_map))

    def test_missing_prompt_map_entry(self):
        """Test 2 — Missing PROMPT_MAP Entry"""
        source_graph = [
            Marker(marker_id="MP:0001", filesystem_id="MP-0001"),
            Marker(marker_id="MP:0005", filesystem_id="MP-0005")
        ]
        prompt_map = {
            "MP:0001": {"LONG_RANGE_FRAME": "...", "LOCAL_TRANSFORMATION": "..."}
        }
        with self.assertRaisesRegex(ValueError, "SOURCE_PROMPT_MAP_MISMATCH"):
            self.validator.validate(source_graph, prompt_map)

    def test_extra_prompt_map_entry(self):
        """Test 3 — Extra PROMPT_MAP Entry"""
        source_graph = [
            Marker(marker_id="MP:0001", filesystem_id="MP-0001")
        ]
        prompt_map = {
            "MP:0001": {"LONG_RANGE_FRAME": "...", "LOCAL_TRANSFORMATION": "..."},
            "MP:0005": {"LONG_RANGE_FRAME": "...", "LOCAL_TRANSFORMATION": "..."}
        }
        with self.assertRaisesRegex(ValueError, "SOURCE_PROMPT_MAP_MISMATCH"):
            self.validator.validate(source_graph, prompt_map)

    def test_both_inputs_empty(self):
        """Test 4 — Both Inputs Empty"""
        source_graph = []
        prompt_map = {}
        self.assertTrue(self.validator.validate(source_graph, prompt_map))

    def test_prompt_map_order_independence(self):
        """Test 5 — PROMPT_MAP Order Independence"""
        source_graph = [
            Marker(marker_id="MP:0001", filesystem_id="MP-0001"),
            Marker(marker_id="MP:0005", filesystem_id="MP-0005")
        ]
        # Dictionaries in Python 3.7+ maintain insertion order, but we want to show it doesn't matter.
        prompt_map = {
            "MP:0005": {"LONG_RANGE_FRAME": "...", "LOCAL_TRANSFORMATION": "..."},
            "MP:0001": {"LONG_RANGE_FRAME": "...", "LOCAL_TRANSFORMATION": "..."}
        }
        self.assertTrue(self.validator.validate(source_graph, prompt_map))

if __name__ == "__main__":
    unittest.main()
