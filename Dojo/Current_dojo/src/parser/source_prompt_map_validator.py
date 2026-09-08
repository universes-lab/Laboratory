"""
Module for validating the correspondence between SOURCE production markers and PROMPT_MAP entries.
"""

from src.parser.source_parser import Marker

class SourcePromptMapValidator:
    def __init__(self):
        pass

    def validate(self, marker_graph: list[Marker], prompt_map: dict) -> bool:
        """
        Validates the exact correspondence between SOURCE markers and PROMPT_MAP entries.

        Args:
            marker_graph: An ordered list of Marker objects from SOURCE.
            prompt_map: A dictionary keyed by marker IDs from PROMPT_MAP.

        Returns:
            True if exact correspondence exists.

        Raises:
            ValueError: If SOURCE_PROMPT_MAP_MISMATCH is detected.
        """
        source_marker_ids = {m.marker_id for m in marker_graph}
        prompt_map_keys = set(prompt_map.keys())

        if source_marker_ids != prompt_map_keys:
            missing_in_prompt_map = source_marker_ids - prompt_map_keys
            extra_in_prompt_map = prompt_map_keys - source_marker_ids
            
            error_msg = "SOURCE_PROMPT_MAP_MISMATCH"
            details = []
            if missing_in_prompt_map:
                details.append(f"Missing in PROMPT_MAP: {sorted(list(missing_in_prompt_map))}")
            if extra_in_prompt_map:
                details.append(f"Extra in PROMPT_MAP: {sorted(list(extra_in_prompt_map))}")
            
            raise ValueError(f"{error_msg}: {'; '.join(details)}")

        return True
