# STEP.md — MANUSCRIPT_PRESS

## IDENTITY

**Project:** MANUSCRIPT_PRESS
**Phase:** 1
**Step:** 6
**Status:** ACTIVE
**Version:** 1.3
**Date:** 2026-09-05
**Technical Authority:** SPEC v3.2.2 §5 (PRODUCTION_REVISION)
**Approval:** DOC APPROVED — 2026-09-05

---

## OBJECTIVE

Implement the authority-freeze mechanism:

* capture the four authority inputs as one immutable byte snapshot;
* derive the deterministic `revision_id`;
* create the revision-namespaced `frozen/` directory;
* persist byte-for-byte identical frozen authority files;
* create `PRODUCTION_REVISION.manifest`.

---

## PREREQUISITES

Accepted Phase-1 components are available:

* SOURCE marker parser — Step 2;
* PROMPT_MAP parser — Step 3;
* Source ↔ Prompt Map validator — Step 4;
* ATX heading extractor — Step 5.

---

## ALLOWED WORKING FILES

* `src/core/authority_freeze.py` — create new.
* `tests/phase1/test_authority_freeze.py` — create new.

No other production files may be modified by this STEP.

---

## FROZEN SPEC BEHAVIOR — AUTHORITATIVE

SPEC v3.2.2 §5 defines `PRODUCTION_REVISION` as a frozen snapshot of four authority inputs:

1. `SOURCE_MANUSCRIPT.md`
2. `PROMPT_MAP.yaml`
3. `Gemma.md`
4. `STABLE_CONFIG.yaml`

Frozen authorities are stored under:

```text
work/revisions/<revision_id>/frozen/
```

The revision identity is:

```text
revision_id = SHA256(canonical_payload)
```

---

## CANONICAL PAYLOAD

The canonical payload is strictly:

```json
{
  "source_sha256": "...",
  "prompt_map_sha256": "...",
  "stable_config_sha256": "...",
  "gemma_sha256": "...",
  "ordered_marker_graph": ["MP:0001", "MP:0005"]
}
```

Canonicalization requirements:

* fixed key names;
* fixed key order exactly as shown above;
* deterministic JSON serialization;
* UTF-8 encoding;
* no insignificant whitespace.

`revision_id` is **not** part of the canonical payload.

The SHA256 digest is calculated over the UTF-8 encoded canonical payload bytes.

---

## AUTHORITY SNAPSHOT RULE

The four authority files MUST be read exactly once at the beginning of one freeze operation and retained as immutable byte snapshots.

These captured byte snapshots are the sole authority material for the remainder of that freeze operation.

All subsequent:

* SHA256 hashing;
* SOURCE parsing;
* ordered marker graph derivation;
* validation required by the accepted Phase-1 components;
* frozen-copy writing;

MUST operate from these captured snapshots.

The authority source files MUST NOT be re-read during the same freeze operation.

This prevents a source authority from changing between hash calculation and frozen-copy creation.

---

## FREEZE SEQUENCE — DETERMINISTIC

### 1. Capture Authorities

Read exactly once, as raw bytes:

* `SOURCE_MANUSCRIPT.md`
* `PROMPT_MAP.yaml`
* `Gemma.md`
* `STABLE_CONFIG.yaml`

If any required authority file does not exist:

```text
FileNotFoundError
```

This is a pre-condition failure and does not introduce a new MANUSCRIPT_PRESS failure-taxonomy code.

No target revision directory may be created yet.

---

### 2. Compute Authority Hashes

Calculate SHA256 directly from the captured byte snapshots:

* `source_sha256`
* `prompt_map_sha256`
* `stable_config_sha256`
* `gemma_sha256`

No normalization is permitted.

This includes no:

* newline conversion;
* text reserialization;
* Unicode normalization;
* BOM removal or insertion;
* encoding conversion.

Bytes present in the authority snapshot, including any BOM or original line endings, are authoritative.

---

### 3. Build Ordered Marker Graph

Derive `ordered_marker_graph` from the captured `SOURCE_MANUSCRIPT.md` snapshot using the accepted Step-2 SOURCE marker parser behavior.

Do not re-read `SOURCE_MANUSCRIPT.md` from disk.

Marker order comes only from SOURCE order.

Do not invent new marker validation semantics in this STEP.

---

### 4. Build Canonical Payload

Construct the canonical payload using:

* `source_sha256`
* `prompt_map_sha256`
* `stable_config_sha256`
* `gemma_sha256`
* `ordered_marker_graph`

Serialize it deterministically according to the canonicalization rules above.

---

### 5. Compute Revision ID

Calculate:

```text
revision_id = SHA256(canonical_payload_bytes)
```

The `revision_id` MUST be fully determined before any revision directory is created.

The result MUST NOT depend on:

* target directory existence;
* target path;
* timestamps;
* filesystem metadata;
* execution order outside the defined canonical payload;
* previous freeze attempts.

---

### 6. Create Frozen Directory

Only after `revision_id` has been computed, create:

```text
work/revisions/<revision_id>/frozen/
```

Directory creation MUST NOT influence revision identity.

---

### 7. Write Frozen Authorities

Write the captured byte snapshots into:

```text
work/revisions/<revision_id>/frozen/SOURCE_MANUSCRIPT.md
work/revisions/<revision_id>/frozen/PROMPT_MAP.yaml
work/revisions/<revision_id>/frozen/Gemma.md
work/revisions/<revision_id>/frozen/STABLE_CONFIG.yaml
```

Each frozen file MUST be byte-for-byte identical to the captured source snapshot used to calculate its hash.

Do not re-read the original authority files while writing frozen copies.

---

### 8. Write PRODUCTION_REVISION.manifest

Create:

```text
work/revisions/<revision_id>/frozen/PRODUCTION_REVISION.manifest
```

The persisted manifest contains:

* `revision_id`
* `source_sha256`
* `prompt_map_sha256`
* `stable_config_sha256`
* `gemma_sha256`
* `ordered_marker_graph`

The manifest is not itself the canonical payload because it additionally contains `revision_id`.

The manifest MUST nevertheless deterministically represent the frozen revision metadata.

---

## INVARIANTS

### Revision Identity

Identical:

* four authority byte snapshots;
* ordered marker graph;

MUST produce the same `revision_id`.

---

### Authority Sensitivity

Changing any one of:

* SOURCE bytes;
* PROMPT_MAP bytes;
* STABLE_CONFIG bytes;
* Gemma.md bytes;
* ordered marker graph;

MUST change `revision_id`.

---

### Byte Identity

For every frozen authority:

```text
frozen_bytes == captured_source_snapshot_bytes
```

and:

```text
SHA256(frozen_bytes) == corresponding_manifest_sha256
```

---

### Canonical Payload Binding

Reconstructing the canonical payload from manifest authority hashes and `ordered_marker_graph` MUST satisfy:

```text
SHA256(canonical_payload_bytes) == manifest.revision_id
```

---

### No TOCTOU Authority Drift

Changes made to an original authority source file after its byte snapshot was captured MUST NOT alter the current freeze operation.

The current freeze is bound exclusively to the captured snapshots.

A later freeze may capture the changed authority and therefore produce a different revision.

---

## TESTS REQUIRED

### 1. Basic Freeze

Given four valid authorities:

* revision directory is created;
* `frozen/` exists;
* all four authority files exist;
* `PRODUCTION_REVISION.manifest` exists;
* hashes are correct.

---

### 2. Deterministic Revision ID

Same four authority byte snapshots + same ordered marker graph:

```text
same revision_id
```

across independent freeze executions.

---

### 3. Different SOURCE

Changing `SOURCE_MANUSCRIPT.md` bytes:

```text
different revision_id
```

---

### 4. Different PROMPT_MAP

Changing `PROMPT_MAP.yaml` bytes:

```text
different revision_id
```

---

### 5. Different STABLE_CONFIG

Changing `STABLE_CONFIG.yaml` bytes:

```text
different revision_id
```

---

### 6. Different Gemma.md

Changing `Gemma.md` bytes:

```text
different revision_id
```

---

### 7. Different Marker Graph

Same four authority bytes but different `ordered_marker_graph`:

```text
different revision_id
```

---

### 8. Manifest / Frozen Consistency

Verify:

* manifest authority hashes equal hashes calculated from frozen files;
* manifest `ordered_marker_graph` equals the graph used for canonical payload construction;
* reconstructed canonical payload produces the manifest `revision_id`;
* every frozen authority is byte-for-byte identical to the captured authority snapshot.

The test MUST include explicit byte comparison, not only decoded text comparison.

---

### 9. Missing Authority

If any required authority file is missing:

```text
FileNotFoundError
```

No new MANUSCRIPT_PRESS error-taxonomy code is introduced.

The freeze MUST NOT create a valid revision artifact from incomplete authority inputs.

---

### 10. Snapshot Stability / TOCTOU Protection

Verify that the freeze operation uses one captured authority snapshot.

Test behavior:

1. capture authority bytes;
2. alter the original source file after capture;
3. continue the freeze operation;
4. verify that:

   * hashes correspond to the captured bytes;
   * frozen copy corresponds to the captured bytes;
   * `revision_id` corresponds to the captured bytes;
   * the later disk mutation does not contaminate the active freeze.

---

## NON-GOALS

* ❌ Editing SOURCE.
* ❌ Editing PROMPT_MAP.
* ❌ Reimplementing SOURCE marker parsing.
* ❌ Reimplementing PROMPT_MAP parsing.
* ❌ ATX heading extraction.
* ❌ Inference.
* ❌ Gemma execution.
* ❌ Candidate pipeline.
* ❌ Acceptance processing.
* ❌ Commit protocol.
* ❌ Resume / recovery.
* ❌ Final assembly.
* ❌ Revision migration.
* ❌ Archiving old revisions.
* ❌ Git operations.
* ❌ New failure-taxonomy codes.

---

## EVIDENCE REQUIRED FOR COMPLETION

* [ ] `python -m py_compile src/core/authority_freeze.py` → PASS.
* [ ] STEP-6 test suite → PASS.
* [ ] Deterministic `revision_id` test → PASS.
* [ ] Frozen byte-identity verification → PASS.
* [ ] Manifest / canonical-payload consistency → PASS.
* [ ] Snapshot-stability / TOCTOU test → PASS.

---

## REPORT FORMAT

```yaml
Phase: 1
Step: 6
Status: COMPLETED / BLOCKED / FAILED

Files_Changed:
  - src/core/authority_freeze.py
  - tests/phase1/test_authority_freeze.py

Implemented:
  - immutable authority byte snapshots
  - deterministic authority hashing
  - ordered marker graph binding
  - canonical payload generation
  - deterministic revision_id generation
  - frozen authority creation
  - PRODUCTION_REVISION.manifest creation
  - TOCTOU-safe freeze behavior

Tests_Run:
  - STEP-6 test suite

Test_Results:
  - all passed / list of failures

Evidence:
  - py_compile: PASS / FAIL
  - tests: PASS / FAIL
  - deterministic_revision_id: PASS / FAIL
  - frozen_byte_identity: PASS / FAIL
  - manifest_consistency: PASS / FAIL
  - snapshot_stability: PASS / FAIL

Limitations:
  - none within scope / factual limitation

Next: WAIT_FOR_DEEPSEEK
```

---

After successful VERIFY and REPORT, Samurai may update the current `STEP.md` status to:

```text
COMPLETED
```

Then:

```text
STOP → WAIT_FOR_DEEPSEEK
```

Do not execute any subsequent STEP without a new active operational instruction.

---

END OF ACTIVE STEP
