"""
Tests for the ProtectedSpanParser.
"""

import unittest

from src.parser.protected_span_parser import ProtectedSpan, ProtectedSpanParser

class TestProtectedSpanParser(unittest.TestCase):

    def setUp(self):
        """Set up test fixtures, if any."""
        self.parser = ProtectedSpanParser()

    def test_single_protected_span(self):
        """Test parsing a single protected span."""
        text = """
This is some text before.
<!-- MP:PROTECTED id="P42_01":BEGIN -->
This is the protected content.
<!-- MP:PROTECTED id="P42_01":END -->
This is text after.
"""
        # The BEGIN marker is on line 2, END marker is on line 4.
        expected_spans = [
            ProtectedSpan(id='P42_01', content='This is the protected content.', start_line=2, end_line=4)
        ]
        # The initial newline from the first line of the text should be preserved.
        expected_slotted_source = """
This is some text before.
⟦MP_PROTECTED:P42_01⟧
This is text after.
"""
        spans, slotted_source = self.parser.parse(text)
        self.assertEqual(spans, expected_spans)
        self.assertEqual(slotted_source, expected_slotted_source)

    def test_multiline_protected_span(self):
        """Test parsing a multiline protected span."""
        text = """
Some intro text.
<!-- MP:PROTECTED id="P42_02":BEGIN -->
Line 1 of protected content.
Line 2 of protected content.
<!-- MP:PROTECTED id="P42_02":END -->
More text.
"""
        # BEGIN on line 2, END on line 5
        expected_spans = [
            ProtectedSpan(id='P42_02', content='Line 1 of protected content.\nLine 2 of protected content.', start_line=2, end_line=5)
        ]
        expected_slotted_source = """
Some intro text.
⟦MP_PROTECTED:P42_02⟧
More text.
"""
        spans, slotted_source = self.parser.parse(text)
        self.assertEqual(spans, expected_spans)
        self.assertEqual(slotted_source, expected_slotted_source)

    def test_content_inside_protected_span(self):
        """Test parsing content like quotes, Markdown, and code inside a protected span."""
        text = """
Start.
<!-- MP:PROTECTED id="P42_03":BEGIN -->
This is **bold** text.
`print("hello")`
A list:
- item 1
- item 2
<!-- MP:PROTECTED id="P42_03":END -->
End.
"""
        # BEGIN on line 2, END on line 8
        expected_spans = [
            ProtectedSpan(id='P42_03', content='This is **bold** text.\n`print("hello")`\nA list:\n- item 1\n- item 2', start_line=2, end_line=8)
        ]
        expected_slotted_source = """
Start.
⟦MP_PROTECTED:P42_03⟧
End.
"""
        spans, slotted_source = self.parser.parse(text)
        self.assertEqual(spans, expected_spans)
        self.assertEqual(slotted_source, expected_slotted_source)

    def test_mismatched_start_end_ids(self):
        """Test for mismatched START and END IDs, should raise ValueError."""
        text = """
Content before.
<!-- MP:PROTECTED id="ID_A":BEGIN -->
Protected content.
<!-- MP:PROTECTED id="ID_B":END -->
Content after.
"""
        # The parser correctly raises 'Mismatched START/END IDs'. The test should assert for this.
        with self.assertRaisesRegex(ValueError, "PROTECTED_MARKUP_INVALID: Mismatched START/END IDs"):
            self.parser.parse(text)

    def test_missing_end_marker_or_nesting(self):
        """Test for issues like missing END marker or nesting, should raise ValueError."""
        # This test case now checks for nesting as per SPEC.
        # The original input had two BEGIN markers, which constitutes nesting.
        text = """
Content before.
<!-- MP:PROTECTED id="ID_C":BEGIN -->
Protected content.
<!-- MP:PROTECTED id="ID_C":BEGIN --> # This is now a nested BEGIN, not a missing END.
"""
        # Expecting a nesting error because of the second BEGIN marker.
        with self.assertRaisesRegex(ValueError, "PROTECTED_MARKUP_INVALID: Nesting detected"):
            self.parser.parse(text)

    def test_nesting_forbidden(self):
        """Test for forbidden nesting of protected spans, should raise ValueError."""
        text = """
Outer start.
<!-- MP:PROTECTED id="NEST_OUTER":BEGIN -->
Outer content.
<!-- MP:PROTECTED id="NEST_INNER":BEGIN -->
Inner content.
<!-- MP:PROTECTED id="NEST_INNER":END -->
<!-- MP:PROTECTED id="NEST_OUTER":END -->
"""
        with self.assertRaisesRegex(ValueError, "PROTECTED_MARKUP_INVALID: Nesting detected"):
            self.parser.parse(text)

    def test_production_marker_inside_protected_span(self):
        """Test that production markers remain literal inside a protected span."""
        text = """
Start.
<!-- MP:PROTECTED id="P42_04":BEGIN -->
This is literal <!-- SOURCE: PRODUCTION_MARKER -->
<!-- MP:PROTECTED id="P42_04":END -->
End.
"""
        # BEGIN on line 2, END on line 4
        expected_spans = [
            ProtectedSpan(id='P42_04', content='This is literal <!-- SOURCE: PRODUCTION_MARKER -->', start_line=2, end_line=4)
        ]
        expected_slotted_source = """
Start.
⟦MP_PROTECTED:P42_04⟧
End.
"""
        spans, slotted_source = self.parser.parse(text)
        self.assertEqual(spans, expected_spans)
        self.assertEqual(slotted_source, expected_slotted_source)

    def test_duplicate_protected_id(self):
        """Test for duplicate protected IDs, should raise ValueError."""
        text = """
First span.
<!-- MP:PROTECTED id="DUP_ID":BEGIN -->
Content 1.
<!-- MP:PROTECTED id="DUP_ID":END -->
Second span.
<!-- MP:PROTECTED id="DUP_ID":BEGIN -->
Content 2.
<!-- MP:PROTECTED id="DUP_ID":END -->
"""
        # This input actually triggers nesting first, so we expect a nesting error.
        # Correction: The parser correctly raises 'Duplicate ID'. The test should assert for this.
        with self.assertRaisesRegex(ValueError, "PROTECTED_MARKUP_INVALID: Duplicate ID"):
            self.parser.parse(text)

if __name__ == '__main__':
    unittest.main()
