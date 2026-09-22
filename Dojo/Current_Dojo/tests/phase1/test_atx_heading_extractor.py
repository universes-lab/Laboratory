import unittest
import re
from typing import List, Optional

from src.parser.atx_heading_extractor import ATXHeadingExtractor, ATXHeading
from src.parser.protected_span_parser import ProtectedSpan, ProtectedSpanParser

class TestATXHeadingExtractor(unittest.TestCase):

    def test_single_pre_marker_heading(self):
        """
        TESTS REQUIRED #1: Single Pre-Marker Heading
        Input: '# Section 1'
        Returns one heading:
        raw_heading == '# Section 1'
        heading_text == 'Section 1'
        level == 1
        marker_id is None
        offset invariant holds exactly.
        """
        content = "# Section 1"
        extractor = ATXHeadingExtractor(content)
        headings = extractor.extract()

        self.assertEqual(len(headings), 1)
        h = headings[0]
        self.assertEqual(h.raw_heading, "# Section 1")
        self.assertEqual(h.heading_text, "Section 1")
        self.assertEqual(h.level, 1)
        self.assertIsNone(h.marker_id)
        
        # Offset invariant
        self.assertEqual(content[h.start_offset:h.end_offset], h.raw_heading)
        self.assertEqual(h.start_offset, 0)
        self.assertEqual(h.end_offset, 11)

    def test_heading_after_production_marker(self):
        """
        TESTS REQUIRED #2: Heading After Production Marker
        Input contains: <!-- MP:0001 -->, on a later line: ## Section 1
        Heading has: level == 2, marker_id == 'MP:0001', exact raw_heading, exact offset invariant.
        """
        content = "<!-- MP:0001 -->\n\n## Section 1"
        extractor = ATXHeadingExtractor(content)
        headings = extractor.extract()

        self.assertEqual(len(headings), 1)
        h = headings[0]
        self.assertEqual(h.level, 2)
        self.assertEqual(h.marker_id, "MP:0001")
        self.assertEqual(h.raw_heading, "## Section 1")
        self.assertEqual(h.heading_text, "Section 1")
        
        # Offset invariant
        self.assertEqual(content[h.start_offset:h.end_offset], h.raw_heading)

    def test_multiple_headings_position_preservation(self):
        """
        TESTS REQUIRED #3: Multiple Headings / Position Preservation
        Multiple headings in one and/or multiple marker regions are returned in SOURCE order.
        For every returned heading: slotted_source[start_offset:end_offset] == raw_heading.
        marker_id changes only when a later production marker becomes current.
        """
        content = (
            "# Top\n"
            "<!-- MP:0001 -->\n"
            "## Section 1\n"
            "### Detail 1.1\n"
            "<!-- MP:0002 -->\n"
            "#### Section 2\n"
        )
        extractor = ATXHeadingExtractor(content)
        headings = extractor.extract()

        self.assertEqual(len(headings), 4)
        
        # 1. # Top
        self.assertEqual(headings[0].raw_heading, "# Top")
        self.assertIsNone(headings[0].marker_id)
        self.assertEqual(content[headings[0].start_offset:headings[0].end_offset], "# Top")
        
        # 2. ## Section 1
        self.assertEqual(headings[1].raw_heading, "## Section 1")
        self.assertEqual(headings[1].marker_id, "MP:0001")
        self.assertEqual(content[headings[1].start_offset:headings[1].end_offset], "## Section 1")
        
        # 3. ### Detail 1.1
        self.assertEqual(headings[2].raw_heading, "### Detail 1.1")
        self.assertEqual(headings[2].marker_id, "MP:0001")
        self.assertEqual(content[headings[2].start_offset:headings[2].end_offset], "### Detail 1.1")
        
        # 4. #### Section 2
        self.assertEqual(headings[3].raw_heading, "#### Section 2")
        self.assertEqual(headings[3].marker_id, "MP:0002")
        self.assertEqual(content[headings[3].start_offset:headings[3].end_offset], "#### Section 2")

    def test_protected_heading_is_not_extracted(self):
        """
        TESTS REQUIRED #4: Protected Heading Is Not Extracted
        - Start with raw SOURCE containing:
          - a protected span whose protected material contains # Hidden Heading;
          - an external production marker;
          - an external ATX heading.
        - Run ProtectedSpanParser first.
        - Run ATXHeadingExtractor on the resulting SLOTTED_SOURCE.
        - Only the external heading is returned.
        """
        raw_source = (
            "<!-- MP:PROTECTED id=\"P1\":BEGIN -->\n"
            "# Hidden Heading\n"
            "<!-- MP:PROTECTED id=\"P1\":END -->\n"
            "<!-- MP:0001 -->\n"
            "# Visible Heading"
        )
        
        # 1. Run ProtectedSpanParser
        parser = ProtectedSpanParser()
        spans, slotted_source = parser.parse(raw_source)
        
        # Verify slotting happened
        self.assertIn("⟦MP_PROTECTED:P1⟧", slotted_source)
        self.assertNotIn("# Hidden Heading", slotted_source)
        
        # 2. Run ATXHeadingExtractor on SLOTTED_SOURCE
        extractor = ATXHeadingExtractor(slotted_source)
        headings = extractor.extract()
        
        # 3. Verify only visible heading is returned
        self.assertEqual(len(headings), 1)
        self.assertEqual(headings[0].raw_heading, "# Visible Heading")
        self.assertEqual(headings[0].marker_id, "MP:0001")
        
        # Verify offset invariant on slotted_source
        self.assertEqual(slotted_source[headings[0].start_offset:headings[0].end_offset], "# Visible Heading")

    def test_atx_level_boundary(self):
        """
        TESTS REQUIRED #5: ATX Level Boundary
        Valid levels 1 through 6 are recognized.
        A line beginning with 7 # characters is not returned as an ATX heading.
        """
        content = (
            "###### Level 6\n"
            "####### Level 7 (Invalid)\n"
            "# Level 1"
        )
        extractor = ATXHeadingExtractor(content)
        headings = extractor.extract()
        
        self.assertEqual(len(headings), 2)
        self.assertEqual(headings[0].level, 6)
        self.assertEqual(headings[0].raw_heading, "###### Level 6")
        self.assertEqual(headings[1].level, 1)
        self.assertEqual(headings[1].raw_heading, "# Level 1")

    def test_crlf_offsets(self):
        """
        Verify CRLF offsets correctly:
        slotted_source[start_offset:end_offset] == raw_heading.
        """
        content = "# Heading 1\r\nText\r\n## Heading 2\r\n"
        extractor = ATXHeadingExtractor(content)
        headings = extractor.extract()
        
        self.assertEqual(len(headings), 2)
        
        h1 = headings[0]
        self.assertEqual(h1.raw_heading, "# Heading 1")
        self.assertEqual(content[h1.start_offset:h1.end_offset], h1.raw_heading)
        
        h2 = headings[1]
        self.assertEqual(h2.raw_heading, "## Heading 2")
        self.assertEqual(content[h2.start_offset:h2.end_offset], h2.raw_heading)

if __name__ == '__main__':
    unittest.main()
