import re
import os
from typing import List, Dict, Any, Optional

# Regex to find protected span markers like <!-- BEGIN_PROTECTED:ID --> and <!-- END_PROTECTED:ID -->
# For V1, we assume no nesting and simple ID matching.
PROTECTED_SPAN_START_REGEX = re.compile(r"<!--\s*BEGIN_PROTECTED:([\w-]+)\s*-->")
PROTECTED_SPAN_END_REGEX = re.compile(r"<!--\s*END_PROTECTED:([\w-]+)\s*-->")

class ProtectedSpan:
    def __init__(self, start_marker: str, end_marker: str, span_id: str, content: str, start_line: int, end_line: int):
        self.start_marker = start_marker
        self.end_marker = end_marker
        self.span_id = span_id
        self.content = content
        self.start_line = start_line
        self.end_line = end_line

    def __repr__(self) -> str:
        return f"ProtectedSpan(id='{self.span_id}', lines={self.start_line}-{self.end_line})"

class ProtectedSpanParser:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.protected_spans: List[ProtectedSpan] = []
        self.lines: List[str] = []
        self.current_span_id: Optional[str] = None
        self.current_span_start_line: Optional[int] = None
        self.current_span_content_lines: List[str] = []

    def parse(self) -> List[ProtectedSpan]:
        """
        Parses protected spans from the file.

        Rules:
        - BEGIN/END ID matching.
        - No nesting in V1.
        - Protected span parsed before production markers inside it.
        - Marker-looking syntax inside protected material remains literal.
        - Invalid markup produces SPEC-defined failure.
        """
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"File not found: {self.file_path}")

        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                self.lines = f.readlines()
        except Exception as e:
            raise IOError(f"Error reading file {self.file_path}: {e}")

        self._process_lines()
        return self.protected_spans

    def _process_lines(self):
        for line_num, line in enumerate(self.lines, 1):
            start_match = PROTECTED_SPAN_START_REGEX.search(line)
            end_match = PROTECTED_SPAN_END_REGEX.search(line)

            if start_match and end_match:
                # Handle case where both start and end markers are on the same line
                # Ensure start_match appears before end_match if they are on the same line
                start_pos = start_match.start()
                end_pos = end_match.start()

                if start_pos < end_pos:
                    # START marker before END marker on the same line
                    start_id = start_match.group(1)
                    end_id = end_match.group(1)
                    if start_id == end_id:
                        # This is a complete span on one line.
                        # Add any pending content if we were inside a span.
                        if self.current_span_id is not None:
                            # This indicates nesting or an unbalanced span, which is an error for V1.
                            raise ValueError(f"Nesting detected or unbalanced span at line {line_num}. Expected END for '{self.current_span_id}' but found start/end for '{start_id}'.")
                        
                        span_content = line[start_match.end():end_pos].strip()
                        self.protected_spans.append(ProtectedSpan(
                            start_marker=start_match.group(0),
                            end_marker=end_match.group(0),
                            span_id=start_id,
                            content=span_content,
                            start_line=line_num,
                            end_line=line_num
                        ))
                    else:
                        raise ValueError(f"Mismatched BEGIN/END IDs on line {line_num}. Expected ID '{start_id}' to match '{end_id}'.")
                else:
                    # END marker appears before START marker on the same line, or they are on different lines.
                    # Treat as separate events, potentially indicating an error if we are in a span.
                    pass # Will be handled by the end_match block below if it's indeed an END

            if start_match and (end_match is None or start_match.start() > end_match.start()):
                # Found a START marker, and either no END marker on this line, or END is before START.
                if self.current_span_id is not None:
                    # This indicates nesting or an unbalanced span.
                    raise ValueError(f"Nesting detected or unbalanced span at line {line_num}. Expected END for '{self.current_span_id}' but found START for '{start_match.group(1)}'.")
                
                self.current_span_id = start_match.group(1)
                self.current_span_start_line = line_num
                self.current_span_content_lines = [] # Reset content for new span

            elif end_match and (start_match is None or end_match.start() < start_match.start()):
                # Found an END marker, and either no START marker on this line, or START is before END.
                if self.current_span_id is None:
                    # Found END marker without a corresponding BEGIN marker.
                    raise ValueError(f"Unmatched END_PROTECTED marker found at line {line_num} for ID '{end_match.group(1)}'.")
                
                # Check if the END marker's ID matches the current open span's ID.
                if end_match.group(1) != self.current_span_id:
                    raise ValueError(f"Mismatched BEGIN/END IDs. Expected END for '{self.current_span_id}' but found END for '{end_match.group(1)}' at line {line_num}.")

                # Complete the span
                span_content = "\n".join(self.current_span_content_lines).strip()
                self.protected_spans.append(ProtectedSpan(
                    start_marker=f"<!-- BEGIN_PROTECTED:{self.current_span_id} -->", # Reconstruct for clarity
                    end_marker=end_match.group(0),
                    span_id=self.current_span_id,
                    content=span_content,
                    start_line=self.current_span_start_line,
                    end_line=line_num
                ))
                
                # Reset span state
                self.current_span_id = None
                self.current_span_start_line = None
                self.current_span_content_lines = []

            elif self.current_span_id is not None:
                # If we are inside a protected span and the line does not contain START/END markers,
                # add the line to the content. This handles literal marker-looking syntax.
                self.current_span_content_lines.append(line.rstrip('\n')) # Store line content, preserve indentation but not trailing newline
            # else: the line is outside any span and not a marker, ignore.

        # After processing all lines, check if we are still inside an unclosed span.
        if self.current_span_id is not None:
            raise ValueError(f"Unclosed protected span. Expected END_PROTECTED for '{self.current_span_id}' starting at line {self.current_span_start_line}. File ended prematurely.")


# --- Test Fixtures --- (for demonstration; actual tests should be in a separate test file)

# Example of a valid file with protected spans
VALID_PROTECTED_SPAN_CONTENT = """
This is some regular content before the span.
<!-- BEGIN_PROTECTED:SECRET_INFO -->
This is secret information.
It should be treated literally.
It might contain things that look like <!-- markers -->.
<!-- MP:0001 --> this should not be parsed as a production marker.
<!-- END_PROTECTED:SECRET_INFO -->
This is content after the protected span.

<!-- BEGIN_PROTECTED:ANOTHER_ID -->
Another piece of protected content.
<!-- END_PROTECTED:ANOTHER_ID -->
"""

# Example with nesting (invalid for V1)
NESTED_PROTECTED_SPAN_CONTENT = """
<!-- BEGIN_PROTECTED:OUTER -->
Outer content.
  <!-- BEGIN_PROTECTED:INNER -->
  Inner content.
  <!-- END_PROTECTED:INNER -->
Outer content continued.
<!-- END_PROTECTED:OUTER -->
"""

# Example with mismatched BEGIN/END IDs
Mismatched_ID_PROTECTED_SPAN_CONTENT = """
<!-- BEGIN_PROTECTED:ID1 -->
Content.
<!-- END_PROTECTED:ID2 -->
"""

# Example with unclosed span
UNCLOSED_PROTECTED_SPAN_CONTENT = """
<!-- BEGIN_PROTECTED:OPEN_SPAN -->
This span is never closed.
"""

# Example with unmatched END marker
UNMATCHED_END_PROTECTED_SPAN_CONTENT = """
Some content.
<!-- END_PROTECTED:UNMATCHED -->
"""

# Example with BEGIN/END on the same line, with content in between
SAME_LINE_SPAN_CONTENT = """
Content before.
<!-- BEGIN_PROTECTED:ONELINE -->Span content on the same line.<!-- END_PROTECTED:ONELINE -->
Content after.
"""

# Example with BEGIN/END on the same line, but END before BEGIN
SAME_LINE_MISORDERED_CONTENT = """
Content before.
<!-- END_PROTECTED:MISORDERED --> <!-- BEGIN_PROTECTED:MISORDERED -->
Content after.
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
    TEST_DIR = "test_fixtures/protected_span"
    os.makedirs(TEST_DIR, exist_ok=True)

    print("--- Testing Protected Span Parser ---")

    # Test case 1: Valid spans
    valid_file = os.path.join(TEST_DIR, "valid_protected_spans.md")
    create_test_fixture_file(valid_file, VALID_PROTECTED_SPAN_CONTENT)
    print(f"\nTesting with valid content: {valid_file}")
    try:
        parser = ProtectedSpanParser(valid_file)
        spans = parser.parse()
        print("Parsing PASSED.")
        print(f"Found {len(spans)} spans:")
        for span in spans:
            print(f"- {span}")
            # Basic check: ensure content is not empty if markers exist
            if span.content == "":
                print(f"  WARNING: Span '{span.span_id}' has empty content.")
    except (FileNotFoundError, IOError, ValueError) as e:
        print(f"Parsing FAILED: {e}")
    finally:
        cleanup_test_fixture_file(valid_file)

    # Test case 2: Nested spans (should fail in V1)
    nested_file = os.path.join(TEST_DIR, "nested_protected_spans.md")
    create_test_fixture_file(nested_file, NESTED_PROTECTED_SPAN_CONTENT)
    print(f"\nTesting with nested content (should fail): {nested_file}")
    try:
        parser = ProtectedSpanParser(nested_file)
        parser.parse()
        print("Parsing PASSED (unexpected - nesting should fail).")
    except ValueError as e:
        print(f"Parsing FAILED as expected due to nesting: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        cleanup_test_fixture_file(nested_file)

    # Test case 3: Mismatched IDs
    mismatched_file = os.path.join(TEST_DIR, "mismatched_id_protected_spans.md")
    create_test_fixture_file(mismatched_file, MISMATCHED_ID_PROTECTED_SPAN_CONTENT)
    print(f"\nTesting with mismatched IDs (should fail): {mismatched_file}")
    try:
        parser = ProtectedSpanParser(mismatched_file)
        parser.parse()
        print("Parsing PASSED (unexpected - mismatched IDs should fail).")
    except ValueError as e:
        print(f"Parsing FAILED as expected due to mismatched IDs: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        cleanup_test_fixture_file(mismatched_file)

    # Test case 4: Unclosed span
    unclosed_file = os.path.join(TEST_DIR, "unclosed_protected_spans.md")
    create_test_fixture_file(unclosed_file, UNCLOSED_PROTECTED_SPAN_CONTENT)
    print(f"\nTesting with unclosed span (should fail): {unclosed_file}")
    try:
        parser = ProtectedSpanParser(unclosed_file)
        parser.parse()
        print("Parsing PASSED (unexpected - unclosed span should fail).")
    except ValueError as e:
        print(f"Parsing FAILED as expected due to unclosed span: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        cleanup_test_fixture_file(unclosed_file)

    # Test case 5: Unmatched END marker
    unmatched_end_file = os.path.join(TEST_DIR, "unmatched_end_protected_spans.md")
    create_test_fixture_file(unmatched_end_file, UNMATCHED_END_PROTECTED_SPAN_CONTENT)
    print(f"\nTesting with unmatched END marker (should fail): {unmatched_end_file}")
    try:
        parser = ProtectedSpanParser(unmatched_end_file)
        parser.parse()
        print("Parsing PASSED (unexpected - unmatched END should fail).")
    except ValueError as e:
        print(f"Parsing FAILED as expected due to unmatched END marker: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        cleanup_test_fixture_file(unmatched_end_file)

    # Test case 6: BEGIN/END on the same line with content
    same_line_file = os.path.join(TEST_DIR, "same_line_protected_spans.md")
    create_test_fixture_file(same_line_file, SAME_LINE_SPAN_CONTENT)
    print(f"\nTesting with span on the same line: {same_line_file}")
    try:
        parser = ProtectedSpanParser(same_line_file)
        spans = parser.parse()
        print("Parsing PASSED.")
        print(f"Found {len(spans)} spans:")
        for span in spans:
            print(f"- {span}")
            print(f"  Content: {span.content!r}")
    except (FileNotFoundError, IOError, ValueError) as e:
        print(f"Parsing FAILED: {e}")
    finally:
        cleanup_test_fixture_file(same_file)

    # Test case 7: BEGIN/END on the same line, but misordered
    same_line_misordered_file = os.path.join(TEST_DIR, "same_line_misordered_protected_spans.md")
    create_test_fixture_file(same_line_misordered_file, SAME_LINE_MISORDERED_CONTENT)
    print(f"\nTesting with misordered BEGIN/END on the same line (should fail): {same_line_misordered_file}")
    try:
        parser = ProtectedSpanParser(same_line_misordered_file)
        parser.parse()
        print("Parsing PASSED (unexpected - misordered spans should fail).")
    except ValueError as e:
        print(f"Parsing FAILED as expected due to misordered BEGIN/END: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        cleanup_test_fixture_file(same_line_misordered_file)

    # Test case 8: File not found
    non_existent_file = os.path.join(TEST_DIR, "non_existent_protected_span.md")
    print(f"\nTesting with non-existent file: {non_existent_file}")
    try:
        parser = ProtectedSpanParser(non_existent_file)
        parser.parse()
        print("Parsing PASSED (unexpected).")
    except FileNotFoundError as e:
        print(f"Parsing FAILED as expected: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    print("\n--- Protected Span Parser Testing Complete ---")
