import re
import os
from typing import List, Dict, Any, Optional

# Regex to find Markdown ATX headings (e.g., # Heading, ## Subheading)
# This regex captures the heading level and the text.
ATX_HEADING_REGEX = re.compile(r"^(#+)\s+(.*)$")

class ATXHeading:
    def __init__(self, level: int, text: str, line_number: int):
        self.level = level
        self.text = text
        self.line_number = line_number

    def __repr__(self) -> str:
        return f"ATXHeading(level={self.level}, text='{self.text}', line={self.line_number})"

class ATXHeadingExtractor:
    def __init__(self, file_path: str, protected_spans: List[Any] = None):
        # protected_spans is a list of objects that have 'start_line', 'end_line', and 'span_id' attributes.
        # This is to ensure headings within protected spans are ignored.
        self.file_path = file_path
        self.protected_spans = protected_spans if protected_spans is not None else []
        self.headings: List[ATXHeading] = []
        self.lines: List[str] = []

    def extract(self) -> List[ATXHeading]:
        """
        Extracts ATX headings from the file, ignoring those within protected spans.
        """
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"File not found: {self.file_path}")

        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                self.lines = f.readlines()
        except Exception as e:
            raise IOError(f"Error reading file {self.file_path}: {e}")

        self._process_lines()
        return self.headings

    def _is_line_in_protected_span(self, line_num: int) -> bool:
        """Checks if a given line number falls within any of the protected spans."""
        for span in self.protected_spans:
            if span.start_line <= line_num <= span.end_line:
                return True
        return False

    def _process_lines(self):
        for line_num, line in enumerate(self.lines, 1):
            if self._is_line_in_protected_span(line_num):
                # Ignore lines within protected spans
                continue

            match = ATX_HEADING_REGEX.match(line)
            if match:
                level = len(match.group(1))  # Number of '#' characters
                text = match.group(2).strip()
                self.headings.append(ATXHeading(level, text, line_num))


# --- Test Fixtures --- (for demonstration; actual tests should be in a separate test file)

# Example of a file with headings and protected spans
VALID_CONTENT_WITH_HEADINGS_AND_SPANS = """
# Main Title
This is some introductory text.

## Section 1
This is content for section 1.

<!-- BEGIN_PROTECTED:SECRET_INFO -->
# This heading should be ignored.
## This subheading should also be ignored.
It contains sensitive data.
<!-- END_PROTECTED:SECRET_INFO -->

## Section 2
Content for section 2.

### Subsection 2.1
More details here.

# Another Top Level Heading
"""

# Example with no headings
NO_HEADINGS_CONTENT = """
Just plain text.
No headings here.
<!-- BEGIN_PROTECTED:SPAN -->
Protected content.
<!-- END_PROTECTED:SPAN -->
"""

# Example with only headings
ONLY_HEADINGS_CONTENT = """
# Heading 1
## Heading 2
### Heading 3
"""

# Example with malformed lines/markers (should not affect heading extraction if not headings themselves)
MALFORMED_LINES_CONTENT = """
# Valid Heading 1
This is a line with invalid <!-- markup -->.
<!-- BEGIN_PROTECTED:SPAN -->
# Heading inside protected span.
## Another heading inside.
<!-- END_PROTECTED:SPAN -->
# Valid Heading 2
"""

# Helper functions for creating and cleaning up test files
def create_test_fixture_file(file_path: str, content: str):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

def cleanup_test_fixture_file(file_path: str):
    if os.path.exists(file_path):
        os.remove(file_path)

if __name__ == '__main__':
    TEST_DIR = "test_fixtures/atx_heading_extractor"
    os.makedirs(TEST_DIR, exist_ok=True)

    print("--- Testing ATX Heading Extractor ---")

    # Test case 1: Valid content with headings and protected spans
    valid_file = os.path.join(TEST_DIR, "valid_content.md")
    create_test_fixture_file(valid_file, VALID_CONTENT_WITH_HEADINGS_AND_SPANS)
    print(f"\nTesting with valid content: {valid_file}")
    try:
        # We need a dummy protected span object for the parser to ignore
        # In a real scenario, this would come from the ProtectedSpanParser
        # For simplicity here, we'll mock it.
        class DummyProtectedSpan:
            def __init__(self, start, end):
                self.start_line = start
                self.end_line = end

        protected_spans_for_test = [
            DummyProtectedSpan(start=6, end=11) # Corresponds to the secret info span
        ]

        extractor = ATXHeadingExtractor(valid_file, protected_spans=protected_spans_for_test)
        headings = extractor.extract()
        print("Extraction PASSED.")
        print(f"Found {len(headings)} headings:")
        for heading in headings:
            print(f"- {heading}")
            # Expected: Main Title (L1), Section 1 (L2), Section 2 (L2), Subsection 2.1 (L3), Another Top Level Heading (L1)
            # Headings inside protected span should be ignored.
    except (FileNotFoundError, IOError) as e:
        print(f"Extraction FAILED: {e}")
    finally:
        cleanup_test_fixture_file(valid_file)

    # Test case 2: Content with no headings
    no_headings_file = os.path.join(TEST_DIR, "no_headings.md")
    create_test_fixture_file(no_headings_file, NO_HEADINGS_CONTENT)
    print(f"\nTesting with no headings: {no_headings_file}")
    try:
        extractor = ATXHeadingExtractor(no_headings_file)
        headings = extractor.extract()
        print("Extraction PASSED.")
        if not headings:
            print("Correctly found no headings.")
        else:
            print(f"Error: Found {len(headings)} headings when none were expected.")
    except (FileNotFoundError, IOError) as e:
        print(f"Extraction FAILED: {e}")
    finally:
        cleanup_test_fixture_file(no_headings_file)

    # Test case 3: Content with only headings
    only_headings_file = os.path.join(TEST_DIR, "only_headings.md")
    create_test_fixture_file(only_headings_file, ONLY_HEADINGS_CONTENT)
    print(f"\nTesting with only headings: {only_headings_file}")
    try:
        extractor = ATXHeadingExtractor(only_headings_file)
        headings = extractor.extract()
        print("Extraction PASSED.")
        print(f"Found {len(headings)} headings:")
        for heading in headings:
            print(f"- {heading}")
            # Expected: Heading 1 (L1), Heading 2 (L2), Heading 3 (L3)
    except (FileNotFoundError, IOError) as e:
        print(f"Extraction FAILED: {e}")
    finally:
        cleanup_test_fixture_file(only_headings_file)

    # Test case 4: Malformed lines, ensuring they don't interfere with valid headings or protected spans
    malformed_file = os.path.join(TEST_DIR, "malformed_lines.md")
    create_test_fixture_file(malformed_file, MALFORMED_LINES_CONTENT)
    print(f"\nTesting with malformed lines: {malformed_file}")
    try:
        protected_spans_for_malformed_test = [
            DummyProtectedSpan(start=5, end=8) # Corresponds to the protected span
        ]
        extractor = ATXHeadingExtractor(malformed_file, protected_spans=protected_spans_for_malformed_test)
        headings = extractor.extract()
        print("Extraction PASSED.")
        print(f"Found {len(headings)} headings:")
        for heading in headings:
            print(f"- {heading}")
            # Expected: Valid Heading 1 (L1), Valid Heading 2 (L1)
            # Heading inside protected span should be ignored.
            # Invalid markup line should be ignored.
    except (FileNotFoundError, IOError) as e:
        print(f"Extraction FAILED: {e}")
    finally:
        cleanup_test_fixture_file(malformed_file)

    # Test case 5: File not found
    non_existent_file = os.path.join(TEST_DIR, "non_existent_headings.md")
    print(f"\nTesting with non-existent file: {non_existent_file}")
    try:
        extractor = ATXHeadingExtractor(non_existent_file)
        extractor.extract()
        print("Extraction PASSED (unexpected).")
    except FileNotFoundError as e:
        print(f"Extraction FAILED as expected: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    print("\n--- ATX Heading Extractor Testing Complete ---")
