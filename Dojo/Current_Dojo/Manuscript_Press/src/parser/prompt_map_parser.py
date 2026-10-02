"""
Module for parsing PROMPT_MAP.yaml, validating its structure and content.
"""

import re
import yaml

class PromptMapParser:
    def __init__(self):
        pass

    def parse(self, file_path: str) -> dict:
        """
        Parses the PROMPT_MAP.yaml file.

        Args:
            file_path: The path to the PROMPT_MAP.yaml file.

        Returns:
            A dictionary representing the parsed PROMPT_MAP.

        Raises:
            ValueError: If the YAML is malformed or violates SPEC requirements.
        """
        try:
            with open(file_path, 'r') as f:
                prompt_map_data = yaml.safe_load(f)
        except yaml.YAMLError as e:
            raise ValueError(f"PROMPT_ENTRY_INVALID: Malformed YAML: {e}")

        if not prompt_map_data:
            return {}

        # Validate top-level shape: must be a mapping.
        if not isinstance(prompt_map_data, dict):
            raise ValueError("PROMPT_ENTRY_INVALID: Top-level content must be a mapping.")

        parsed_map = {}
        for marker_key, entry_data in prompt_map_data.items():
            # Validate marker key format: MP:XXXX
            if not re.fullmatch(r'MP:\d{4}', marker_key):
                raise ValueError(f"PROMPT_ENTRY_INVALID: Invalid marker key format: {marker_key}")

            # Validate entry shape: must be a mapping.
            if not isinstance(entry_data, dict):
                raise ValueError(f"PROMPT_ENTRY_INVALID: Entry for marker '{marker_key}' must be a mapping.")

            # Validate required fields: LONG_RANGE_FRAME and LOCAL_TRANSFORMATION
            long_range_frame = entry_data.get('LONG_RANGE_FRAME')
            local_transformation = entry_data.get('LOCAL_TRANSFORMATION')

            if not long_range_frame or not isinstance(long_range_frame, str) or not long_range_frame.strip():
                raise ValueError(f"PROMPT_ENTRY_INVALID: Missing or invalid 'LONG_RANGE_FRAME' for marker '{marker_key}'.")
            if not local_transformation or not isinstance(local_transformation, str) or not local_transformation.strip():
                raise ValueError(f"PROMPT_ENTRY_INVALID: Missing or invalid 'LOCAL_TRANSFORMATION' for marker '{marker_key}'.")

            parsed_map[marker_key] = {
                'long_range_frame': long_range_frame,
                'local_transformation': local_transformation
            }

        return parsed_map
