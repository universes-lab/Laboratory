# Implement the authority-freeze mechanism.

import hashlib
import json
import os
import re

from typing import List, Dict, Any, Optional

# Assuming ProtectedSpan and Marker classes are available from previous steps.
# For type hinting purposes:

try:
    from src.parser.protected_span_parser import ProtectedSpan
except ImportError:
    # Fallback if ProtectedSpan is not yet available
    class ProtectedSpan: 
        def __init__(self, id: str, content: str, start_line: int, end_line: int):
            self.id = id
            self.content = content
            self.start_line = start_line
            self.end_line = end_line

try:
    from src.parser.source_parser import Marker
except ImportError:
    # Fallback if Marker is not yet available
    class Marker:
        def __init__(self, marker_id: str, filesystem_id: str):
            self.marker_id = marker_id
            self.filesystem_id = filesystem_id


class AuthorityFreeze:
    """
    Implements the authority-freeze mechanism for creating immutable, reproducible revisions.
    """
    # Authority files required for freezing.
    AUTHORITY_FILES = [
        "SOURCE_MANUSCRIPT.md",
        "PROMPT_MAP.yaml",
        "Gemma.md",
        "STABLE_CONFIG.yaml",
    ]

    # Regex for ATX headings (used for ordered_marker_graph derivation).
    # This should align with the ATXHeadingExtractor used in previous steps.
    ATX_HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)")
    # Regex for Production Markers (used to build ordered_marker_graph).
    # This should align with the SourceParser used in previous steps.
    PRODUCTION_MARKER_RE = re.compile(r"<!-- MP:(\d{4}) -->")

    def __init__(self, root_dir: str, revision_base_dir: str):
        """
        Initialize the AuthorityFreeze mechanism.
        
        Args:
            root_dir: The root directory of the project.
            revision_base_dir: The base directory for storing revisions (e.g., 'work/revisions/').
        """
        self.root_dir = root_dir
        self.revision_base_dir = revision_base_dir
        self.authority_snapshots = {}
        self.canonical_payload = {}
        self.revision_id = None

    def _read_authority_file(self, file_path: str) -> bytes:
        """
        Reads an authority file as raw bytes.
        Raises FileNotFoundError if the file does not exist.
        """
        full_path = os.path.join(self.root_dir, file_path)
        if not os.path.exists(full_path):
            raise FileNotFoundError(f"Authority file not found: {file_path}")
        with open(full_path, 'rb') as f:
            return f.read()

    def _calculate_sha256(self, data: bytes) -> str:
        """
        Calculates the SHA256 hash of the given data.
        """
        return hashlib.sha256(data).hexdigest()

    def _build_ordered_marker_graph(self, source_bytes: bytes) -> List[str]:
        """
        Derives the ordered marker graph from the SOURCE_MANUSCRIPT bytes.
        This should use the logic from the SourceParser.
        """
        source_text = source_bytes.decode('utf-8', errors='replace')
        marker_graph = []
        for line in source_text.splitlines():
            matches = self.PRODUCTION_MARKER_RE.findall(line)
            for match_group in matches:
                marker_id = f"MP:{match_group}"
                marker_graph.append(marker_id)
        return marker_graph

    def _build_canonical_payload(self) -> Dict[str, Any]:
        """
        Constructs the canonical payload dictionary.
        """
        return {
            "source_sha256": self.authority_snapshots.get("SOURCE_MANUSCRIPT.md", {"hash": None})["hash"],
            "prompt_map_sha256": self.authority_snapshots.get("PROMPT_MAP.yaml", {"hash": None})["hash"],
            "stable_config_sha256": self.authority_snapshots.get("STABLE_CONFIG.yaml", {"hash": None})["hash"],
            "gemma_sha256": self.authority_snapshots.get("Gemma.md", {"hash": None})["hash"],
            "ordered_marker_graph": self.canonical_payload.get("ordered_marker_graph"),
        }

    def freeze_authorities(self):
        """
        Executes the authority freezing process:
        1. Capture authorities as byte snapshots.
        2. Compute SHA256 hashes for each snapshot.
        3. Build the ordered marker graph from SOURCE.
        4. Construct the canonical payload.
        5. Compute the revision_id.
        6. Create the revision directory and 'frozen/' subdirectory.
        7. Write frozen authority files.
        8. Write the PRODUCTION_REVISION.manifest.
        """
        # 1. Capture Authorities & 2. Compute Hashes
        for filename in self.AUTHORITY_FILES:
            try:
                file_bytes = self._read_authority_file(filename)
                file_hash = self._calculate_sha256(file_bytes)
                self.authority_snapshots[filename] = {"bytes": file_bytes, "hash": file_hash}
            except FileNotFoundError as e:
                # Raise as per STEP requirement - pre-condition failure.
                raise e

        # 3. Build Ordered Marker Graph
        source_bytes = self.authority_snapshots.get("SOURCE_MANUSCRIPT.md", {}).get("bytes")
        if source_bytes is None:
            # This should not happen if FileNotFoundError was raised earlier, but as a safeguard.
            raise ValueError("SOURCE_MANUSCRIPT.md bytes not captured.")
        self.canonical_payload["ordered_marker_graph"] = self._build_ordered_marker_graph(source_bytes)

        # 4. Build Canonical Payload
        self.canonical_payload.update(self._build_canonical_payload())

        # 5. Compute Revision ID
        # The canonical payload needs to be serialized deterministically for hashing.
        # Use json.dumps with sort_keys=True and separators for consistency.
        canonical_payload_bytes = json.dumps(
            self.canonical_payload,
            sort_keys=True,
            separators=(',', ':'),
            ensure_ascii=False  # Ensure correct handling of non-ASCII chars if any
        ).encode('utf-8')
        self.revision_id = self._calculate_sha256(canonical_payload_bytes)

        # 6. Create Revision and Frozen Directories
        revision_dir = os.path.join(self.revision_base_dir, self.revision_id)
        frozen_dir = os.path.join(revision_dir, "frozen")
        os.makedirs(frozen_dir, exist_ok=True)

        # 7. Write Frozen Authorities
        for filename in self.AUTHORITY_FILES:
            snapshot_info = self.authority_snapshots.get(filename)
            if snapshot_info and snapshot_info["bytes"] is not None:
                frozen_file_path = os.path.join(frozen_dir, filename)
                with open(frozen_file_path, 'wb') as f:
                    f.write(snapshot_info["bytes"])
            else:
                # This indicates an internal logic error if not caught by FileNotFoundError.
                raise RuntimeError(f"Missing byte snapshot for authority file: {filename}")

        # 8. Write PRODUCTION_REVISION.manifest
        manifest_data = {
            "revision_id": self.revision_id,
            "source_sha256": self.authority_snapshots.get("SOURCE_MANUSCRIPT.md", {}).get("hash"),
            "prompt_map_sha256": self.authority_snapshots.get("PROMPT_MAP.yaml", {}).get("hash"),
            "stable_config_sha256": self.authority_snapshots.get("STABLE_CONFIG.yaml", {}).get("hash"),
            "gemma_sha256": self.authority_snapshots.get("Gemma.md", {}).get("hash"),
            "ordered_marker_graph": self.canonical_payload.get("ordered_marker_graph"),
        }

        manifest_path = os.path.join(frozen_dir, "PRODUCTION_REVISION.manifest")
        with open(manifest_path, 'w', encoding='utf-8') as f:
            # Use deterministic serialization for the manifest as well.
            json.dump(
                manifest_data,
                f,
                sort_keys=True,
                indent=2,  # Use indent for readability of the manifest file
                ensure_ascii=False
            )

        return self.revision_id

# Example of how this class would be used (for testing purposes or in a script):
# if __name__ == '__main__':
#     # Assuming these files exist in the project root for testing.
#     # You would typically pass the actual paths or relative paths.
#     ROOT_DIR = os.getcwd() # Or a specific project root path
#     REVISION_BASE_DIR = os.path.join(ROOT_DIR, "work/revisions")
# 
#     # Create dummy authority files if they don't exist for a basic run
#     for fname in AuthorityFreeze.AUTHORITY_FILES:
#         fpath = os.path.join(ROOT_DIR, fname)
#         if not os.path.exists(fpath):
#             with open(fpath, 'w') as f: f.write(f"Dummy content for {fname}\n")
# 
#     # Ensure the work/revisions directory exists for the test
#     os.makedirs(REVISION_BASE_DIR, exist_ok=True)
# 
#     try:
#         frozener = AuthorityFreeze(root_dir=ROOT_DIR, revision_base_dir=REVISION_BASE_DIR)
#         rev_id = frozener.freeze_authorities()
#         print(f"Successfully created revision with ID: {rev_id}")
#         print(f"Frozen files are in: {os.path.join(REVISION_BASE_DIR, rev_id, 'frozen/')}")
#     except FileNotFoundError as e:
#         print(f"Error: {e}")
#     except ValueError as e:
#         print(f"Error: {e}")
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")
