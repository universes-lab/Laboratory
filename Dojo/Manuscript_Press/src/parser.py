import re
import os
from typing import List, Dict, Any

# Regex to find production markers like <!-- MP:0001 -->
PRODUCTION_MARKER_REGEX = re.compile(r"<!--\s*MP:(\d+)\s*-->")

class ProductionMarker:
    def __init__(self, original_marker: str, logical_id: str, filesystem_safe_id: str, line_number: int):
        self.original_marker = original_marker
        self.logical_id = logical_id
        self.filesystem_safe_id = filesystem_safe_id
        self.line_number = line_number

    def __repr__(self) -> str:
        return f"ProductionMarker(logical_id='{self.logical_id}', filesystem_safe_id='{self.filesystem_safe_id}', line={self.line_number})"

class DuplicateMarkerError(ValueError):
    """Custom exception for duplicate production marker errors."""
    pass

def parse_production_markers(file_path: str) -> List[ProductionMarker]:
    """
    Parses production markers from a given file.

    Args:
        file_path: The path to the file to parse.

    Returns:
        A list of ProductionMarker objects, ordered by their appearance in the file.

    Raises:
        FileNotFoundError: If the file does not exist.
        DuplicateMarkerError: If duplicate logical marker IDs are found.
        IOError: If there is an error reading the file.
    """
    markers: List[ProductionMarker] = []
    seen_logical_ids = set() # To detect duplicates

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                matches = PRODUCTION_MARKER_REGEX.findall(line)
                for match in matches:
                    number = match
                    logical_id = f"MP:{number}"
                    if logical_id in seen_logical_ids:
                        # SPEC requires MARKER_GRAPH_INVALID for duplicates
                        raise DuplicateMarkerError(f"Duplicate production marker found: {logical_id} on line {line_num}")
                    seen_logical_ids.add(logical_id)

                    filesystem_safe_id = f"MP-{number}"
                    original_marker = f"<!-- MP:{number} -->"
                    markers.append(ProductionMarker(original_marker, logical_id, filesystem_safe_id, line_num))
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        raise # Re-raise to be caught by caller/tests
    except DuplicateMarkerError as e:
        print(f"Error: {e}")
        raise # Re-raise to be caught by caller/tests
    except Exception as e:
        print(f"An error occurred while parsing {file_path}: {e}")
        raise IOError(f"An error occurred while parsing {file_path}: {e}") from e
    return markers

if __name__ == '__main__':
    # Example Usage:
    # Create a dummy file for testing
    dummy_file_content = """
This is some text before the marker.
<!-- MP:0001 -->
This is the content after the first marker.
Another line.
<!-- MP:0005 -->
This is the content after the second marker.
Some more text.
<!-- MP:0002 -->
This is the content after the third marker.
"""
    dummy_file_path = "temp_source_file.md"
    with open(dummy_file_path, "w", encoding="utf-8") as f:
        f.write(dummy_file_content)

    print(f"Parsing markers from: {dummy_file_path}")
    try:
        parsed_markers = parse_production_markers(dummy_file_path)
        if parsed_markers:
            print("Found markers:")
            for marker in parsed_markers:
                print(f"- Logical ID: {marker.logical_id}, Filesystem-safe ID: {marker.filesystem_safe_id}, Line: {marker.line_number}")
        else:
            print("No markers found or an error occurred.")
    except Exception as e:
        print(f"An error occurred during parsing: {e}")

    # Clean up dummy file
    if os.path.exists(dummy_file_path):
        os.remove(dummy_file_path)

    print("\nTesting with a file containing no markers:")
    dummy_file_no_markers = "temp_no_markers.md"
    with open(dummy_file_no_markers, "w", encoding="utf-8") as f:
        f.write("This file has no production markers.")
    try:
        parsed_markers_no_markers = parse_production_markers(dummy_file_no_markers)
        if not parsed_markers_no_markers:
            print("Correctly found no markers.")
        else:
            print("Error: Found markers when none were expected.")
    except Exception as e:
        print(f"An error occurred during parsing: {e}")
    if os.path.exists(dummy_file_no_markers):
        os.remove(dummy_file_no_markers)

    print("\nTesting with duplicate markers:")
    dummy_file_duplicate = "temp_duplicate_markers.md"
    duplicate_content = """
<!-- MP:0001 -->
<!-- MP:0001 -->
"""
    with open(dummy_file_duplicate, "w", encoding="utf-8") as f:
        f.write(duplicate_content)
    try:
        parse_production_markers(dummy_file_duplicate)
    except DuplicateMarkerError as e:
        print(f"Correctly caught expected error: {e}")
    except Exception as e:
        print(f"Caught unexpected error for duplicate markers: {e}")
    if os.path.exists(dummy_file_duplicate):
        os.remove(dummy_file_duplicate)

    print("\nTesting with malformed markers:")
    dummy_file_malformed = "temp_malformed.md"
    malformed_content = """
<!-- MP: 0001 --> (extra space)
<!--MP:0002--> (no space)
<!-- MP:abc --> (non-numeric)
"""
    with open(dummy_file_malformed, "w", encoding="utf-8") as f:
        f.write(malformed_content)
    try:
        parsed_markers_malformed = parse_production_markers(dummy_file_malformed)
        if parsed_markers_malformed:
            print("Found markers (malformed input):")
            for marker in parsed_markers_malformed:
                print(f"- Logical ID: {marker.logical_id}, Filesystem-safe ID: {marker.filesystem_safe_id}, Line: {marker.line_number}")
        else:
            print("No valid markers found in malformed input.")
    except Exception as e:
        print(f"An error occurred during parsing: {e}")
    if os.path.exists(dummy_file_malformed):
        os.remove(dummy_file_malformed)
