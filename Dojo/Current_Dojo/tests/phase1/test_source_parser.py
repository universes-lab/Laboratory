"""
Tests for the SourceParser.
"""

import unittest
import re

from src.parser.source_parser import Marker, SourceParser

class TestSourceParser(unittest.TestCase):

    def setUp(self):
        """Set up test fixtures, if any."""
        self.parser = SourceParser()

    def test_no_markers(self):
        """Test with input containing no production markers."""
        slotted_source = """
This is some text without any markers.
This is another line.
"""
        expected_graph = []
        marker_graph = self.parser.parse(slotted_source)
        self.assertEqual(marker_graph, expected_graph)

    def test_single_marker(self):
        """Test parsing a single production marker."""
        slotted_source = """
Text before <!-- MP:0001 --> block content.
"""
        expected_graph = [
            Marker(marker_id='MP:0001', filesystem_id='MP-0001')
        ]
        marker_graph = self.parser.parse(slotted_source)
        self.assertEqual(marker_graph, expected_graph)

    def test_multiple_markers(self):
        """Test parsing multiple production markers in order."""
        slotted_source = """
<!-- MP:0001 --> first <!-- MP:0005 --> second <!-- MP:0130 --> third
"""
        expected_graph = [
            Marker(marker_id='MP:0001', filesystem_id='MP-0001'),
            Marker(marker_id='MP:0005', filesystem_id='MP-0005'),
            Marker(marker_id='MP:0130', filesystem_id='MP-0130')
        ]
        marker_graph = self.parser.parse(slotted_source)
        self.assertEqual(marker_graph, expected_graph)

    def test_non_contiguous_ids(self):
        """Test parsing non-contiguous marker IDs."""
        slotted_source = """
<!-- MP:0001 --> first <!-- MP:0130 --> second
"""
        expected_graph = [
            Marker(marker_id='MP:0001', filesystem_id='MP-0001'),
            Marker(marker_id='MP:0130', filesystem_id='MP-0130')
        ]
        marker_graph = self.parser.parse(slotted_source)
        self.assertEqual(marker_graph, expected_graph)

    def test_duplicate_marker_id(self):
        """Test for duplicate marker IDs, should raise ValueError."""
        slotted_source = """
First span.
<!-- MP:0001 -->
Content 1.
<!-- MP:0001 -->
"""
        with self.assertRaisesRegex(ValueError, "MARKER_GRAPH_INVALID: Duplicate marker ID found: MP:0001"):
            self.parser.parse(slotted_source)

    def test_slotted_source_integration(self):
        """Test integration with SLOTTED_SOURCE, ensuring protected content is ignored."""
        # This requires a ProtectedSpanParser, but we simulate its output here.
        # SLOTTED_SOURCE from Step 1 would have replaced protected spans like 'P42_01' with '⟦MP_PROTECTED:P42_01⟧'.
        slotted_source_with_protected = """
Text before protected span.
⟦MP_PROTECTED:P42_01⟧
Text after protected span.

<!-- MP:0005 -->
"""
        expected_graph = [
            Marker(marker_id='MP:0005', filesystem_id='MP-0005')
        ]
        marker_graph = self.parser.parse(slotted_source_with_protected)
        self.assertEqual(marker_graph, expected_graph)

if __name__ == '__main__':
    unittest.main()
