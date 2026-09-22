"""
Module for parsing source manuscripts, identifying production markers, and building a marker graph.
"""

import re

class Marker:
    def __init__(self, marker_id: str, filesystem_id: str):
        self.marker_id = marker_id
        self.filesystem_id = filesystem_id

    def __repr__(self):
        return f"Marker(marker_id='{self.marker_id}', filesystem_id='{self.filesystem_id}')"

    def __eq__(self, other):
        if not isinstance(other, Marker):
            return NotImplemented
        return (self.marker_id == other.marker_id and
                self.filesystem_id == other.filesystem_id)

class SourceParser:
    # Regex to find production markers like <!-- MP:XXXX -->
    PRODUCTION_MARKER_RE = re.compile(r"<!-- MP:(\d{4}) -->")

    def __init__(self):
        self.marker_graph = []
        self.used_marker_ids = set()

    def parse(self, slotted_source: str) -> list[Marker]:
        """
        Parses the SLOTTED_SOURCE to extract production markers and build an ordered graph.

        Args:
            slotted_source: The input string with protected spans replaced by slot tokens.

        Returns:
            A list of Marker objects in order of appearance.

        Raises:
            ValueError: If duplicate marker IDs are found.
        """
        # print(f"--- Parsing Text ---")
        lines = slotted_source.splitlines()
        
        for i, line in enumerate(lines):
            current_line_num = i + 1
            # print(f"Processing line {current_line_num}: '{line}'")
            
            # Use findall to get all marker matches on a line.
            matches = self.PRODUCTION_MARKER_RE.findall(line)
            
            for match_group in matches:
                marker_id = f"MP:{match_group}"
                filesystem_id = f"MP-{match_group}"
                
                if marker_id in self.used_marker_ids:
                    # print(f"  RAISING Duplicate ID Error for ID: {marker_id}")
                    raise ValueError(f"MARKER_GRAPH_INVALID: Duplicate marker ID found: {marker_id}")
                
                self.used_marker_ids.add(marker_id)
                self.marker_graph.append(Marker(marker_id=marker_id, filesystem_id=filesystem_id))
                # print(f"  Processed marker. Marker graph size: {len(self.marker_graph)}")

        # print(f"--- Parsing Complete ---")
        # print(f"Final marker_graph: {self.marker_graph}")
        return self.marker_graph
