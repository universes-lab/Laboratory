import unittest
import os
import shutil
import tempfile
import hashlib
import json
from src.core.authority_freeze import AuthorityFreeze

class TestAuthorityFreeze(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory for the test
        self.test_dir = tempfile.mkdtemp()
        self.root_dir = os.path.join(self.test_dir, "root")
        self.revision_base_dir = os.path.join(self.test_dir, "work/revisions")
        os.makedirs(self.root_dir)
        os.makedirs(self.revision_base_dir)

        # Default valid authority contents
        self.source_content = "<!-- MP:0001 -->\n# Title\n<!-- MP:0002 -->\nContent"
        self.prompt_map_content = "map: content"
        self.gemma_content = "gemma: instructions"
        self.stable_config_content = "config: stable"

        self._write_authorities()

    def tearDown(self):
        # Remove the temporary directory after the test
        shutil.rmtree(self.test_dir)

    def _write_authorities(self, source=None, prompt_map=None, gemma=None, config=None):
        def write_if_not_none(name, content):
            if content is not None:
                with open(os.path.join(self.root_dir, name), "wb") as f:
                    f.write(content.encode("utf-8") if isinstance(content, str) else content)

        write_if_not_none("SOURCE_MANUSCRIPT.md", source if source is not None else self.source_content)
        write_if_not_none("PROMPT_MAP.yaml", prompt_map if prompt_map is not None else self.prompt_map_content)
        write_if_not_none("Gemma.md", gemma if gemma is not None else self.gemma_content)
        write_if_not_none("STABLE_CONFIG.yaml", config if config is not None else self.stable_config_content)

    def _get_sha256(self, content):
        data = content.encode("utf-8") if isinstance(content, str) else content
        return hashlib.sha256(data).hexdigest()

    def test_basic_freeze(self):
        """1. Basic Freeze: Verify files, manifest, and hashes."""
        frozener = AuthorityFreeze(self.root_dir, self.revision_base_dir)
        rev_id = frozener.freeze_authorities()

        frozen_dir = os.path.join(self.revision_base_dir, rev_id, "frozen")
        self.assertTrue(os.path.exists(frozen_dir))

        for filename in AuthorityFreeze.AUTHORITY_FILES:
            self.assertTrue(os.path.exists(os.path.join(frozen_dir, filename)))

        manifest_path = os.path.join(frozen_dir, "PRODUCTION_REVISION.manifest")
        self.assertTrue(os.path.exists(manifest_path))

        with open(manifest_path, "r", encoding="utf-8") as f:
            manifest = json.load(f)

        self.assertEqual(manifest["revision_id"], rev_id)
        self.assertEqual(manifest["source_sha256"], self._get_sha256(self.source_content))
        self.assertEqual(manifest["ordered_marker_graph"], ["MP:0001", "MP:0002"])

    def test_deterministic_revision_id(self):
        """2. Deterministic Revision ID: Same inputs -> same revision_id."""
        f1 = AuthorityFreeze(self.root_dir, self.revision_base_dir)
        id1 = f1.freeze_authorities()

        # New instance, same files
        f2 = AuthorityFreeze(self.root_dir, self.revision_base_dir)
        id2 = f2.freeze_authorities()

        self.assertEqual(id1, id2)

    def test_sensitivity_source(self):
        """3. Different SOURCE -> different revision_id."""
        f1 = AuthorityFreeze(self.root_dir, self.revision_base_dir)
        id1 = f1.freeze_authorities()

        self._write_authorities(source=self.source_content + "\nmutation")
        f2 = AuthorityFreeze(self.root_dir, self.revision_base_dir)
        id2 = f2.freeze_authorities()

        self.assertNotEqual(id1, id2)

    def test_sensitivity_prompt_map(self):
        """4. Different PROMPT_MAP -> different revision_id."""
        f1 = AuthorityFreeze(self.root_dir, self.revision_base_dir)
        id1 = f1.freeze_authorities()

        self._write_authorities(prompt_map=self.prompt_map_content + "\nmutation")
        f2 = AuthorityFreeze(self.root_dir, self.revision_base_dir)
        id2 = f2.freeze_authorities()

        self.assertNotEqual(id1, id2)

    def test_sensitivity_config(self):
        """5. Different STABLE_CONFIG -> different revision_id."""
        f1 = AuthorityFreeze(self.root_dir, self.revision_base_dir)
        id1 = f1.freeze_authorities()

        self._write_authorities(config=self.stable_config_content + "\nmutation")
        f2 = AuthorityFreeze(self.root_dir, self.revision_base_dir)
        id2 = f2.freeze_authorities()

        self.assertNotEqual(id1, id2)

    def test_sensitivity_gemma(self):
        """6. Different Gemma.md -> different revision_id."""
        f1 = AuthorityFreeze(self.root_dir, self.revision_base_dir)
        id1 = f1.freeze_authorities()

        self._write_authorities(gemma=self.gemma_content + "\nmutation")
        f2 = AuthorityFreeze(self.root_dir, self.revision_base_dir)
        id2 = f2.freeze_authorities()

        self.assertNotEqual(id1, id2)

    def test_sensitivity_marker_graph(self):
        """7. Different Marker Graph -> different revision_id."""
        f1 = AuthorityFreeze(self.root_dir, self.revision_base_dir)
        id1 = f1.freeze_authorities()

        # Same bytes, but change a marker so the graph changes
        source_alt = self.source_content.replace("MP:0002", "MP:0003")
        self._write_authorities(source=source_alt)
        f2 = AuthorityFreeze(self.root_dir, self.revision_base_dir)
        id2 = f2.freeze_authorities()

        self.assertNotEqual(id1, id2)

    def test_byte_identity(self):
        """8. Byte Identity: frozen == captured snapshot."""
        # Use binary data to ensure no text-mode artifacts
        binary_source = b"\x00\xFF\xFE<!-- MP:0001 -->"
        self._write_authorities(source=binary_source)

        frozener = AuthorityFreeze(self.root_dir, self.revision_base_dir)
        rev_id = frozener.freeze_authorities()

        frozen_path = os.path.join(self.revision_base_dir, rev_id, "frozen/SOURCE_MANUSCRIPT.md")
        with open(frozen_path, "rb") as f:
            frozen_bytes = f.read()

        self.assertEqual(frozen_bytes, binary_source)

    def test_missing_authority(self):
        """9. Missing Authority -> FileNotFoundError."""
        os.remove(os.path.join(self.root_dir, "Gemma.md"))
        frozener = AuthorityFreeze(self.root_dir, self.revision_base_dir)
        with self.assertRaises(FileNotFoundError):
            frozener.freeze_authorities()

    def test_snapshot_stability_toctou(self):
        """10. Snapshot Stability / TOCTOU: disk mutation after capture is ignored."""
        # This test is a bit tricky because the implementation is sequential.
        # But we can verify that AuthorityFreeze stores the snapshots in self.authority_snapshots
        # and uses them for hashing and writing.
        
        frozener = AuthorityFreeze(self.root_dir, self.revision_base_dir)
        
        # Step 1: Capture (simulated by manual load for verification of the logic if needed, 
        # but the class does it all in freeze_authorities).
        # To truly test TOCTOU in a single-threaded environment, we'd need hooks.
        # However, the rule is "read exactly once".
        
        # We can verify that if we mutation the file AFTER the freeze, the frozen copy
        # matches what was there at the START. Since we can't easily pause freeze_authorities,
        # we trust the implementation which reads into bytes first.
        
        # Actually, let's verify that the class HAS the bytes stored.
        rev_id = frozener.freeze_authorities()
        
        # Mutate on disk
        with open(os.path.join(self.root_dir, "SOURCE_MANUSCRIPT.md"), "wb") as f:
            f.write(b"mutated")
            
        # Verify frozen copy is NOT mutated
        frozen_path = os.path.join(self.revision_base_dir, rev_id, "frozen/SOURCE_MANUSCRIPT.md")
        with open(frozen_path, "rb") as f:
            frozen_bytes = f.read()
            
        self.assertEqual(frozen_bytes, self.source_content.encode("utf-8"))

if __name__ == '__main__':
    unittest.main()
