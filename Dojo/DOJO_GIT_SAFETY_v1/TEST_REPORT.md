# DOJO GIT SAFETY v1 — Implementation Test Report

## Scope

Implementation was created **outside the live Dojo**. No operation touched `D:\Gemini\dojo`, `GEMINI.md`, `Current_Prompt.md`, `SPEC.md`, or the Coding Samurai.

The supplied contract defines the mechanism as a local recovery system with no remote and with externally authorized destructive recovery. This implementation follows that scope.

## Created implementation files

- `.gitignore`
- `dojo_git.bat`
- `git_tools/rollback_authorized.bat`
- `git_tools/DOJO_GIT_POLICY.md`

A temporary sandbox tree was also created under `sandbox/dojo/`.

## Functional test results

- PASS — **1 CREATE BASELINE**: commit=9aae99cb, staged_files=10, clean=True
- PASS — **2 CREATE WIP**: commit=e99631da
- PASS — **3 ACCEPTED STEP**: missing-token gate present; accepted commit=7b9a8bb5
- PASS — **4 STATUS / HISTORY**: HEAD unchanged
- PASS — **5 PREPARE ROLLBACK REPORT**: clean=True, checkpoints=3, rollback_performed=NO
- PASS — **6 FINAL RELEASE**: commit=03852c07, bundle_verified=True
- PASS — **0 EXIT**: no Git state change


## Safety-gate tests

- PASS — **STEP missing token**
- PASS — **FINAL missing token**
- PASS — **Forbidden staged file hard block**
- PASS — **Unexpected untracked fail-closed**
- PASS — **Remote configured block**
- PASS — **Baseline existing .git block**
- PASS — **Ordinary menu has no rollback execution**
- PASS — **Rollback missing hash block**
- PASS — **Rollback missing authorization block**
- PASS — **Rollback invalid hash verification**
- PASS — **Dirty rollback block**
- PASS — **Authorization token not committed**
- PASS — **Rollback tree equals target**
- PASS — **Rollback preserves later history**


## rollback_authorized.bat behavior

Implemented recovery is **history-preserving**:

1. Validates target commit.
2. Requires an external authorization token.
3. Blocks if the worktree/index is dirty and instructs creation of a forensic WIP first.
4. Restores the target tree with `git restore --source=<hash> --staged --worktree -- .`.
5. Creates a new `RECOVERY - restore state <hash>` commit.
6. Verifies the resulting tree matches the requested target.
7. Does **not** record the authorization token in Git history.

This is intentionally safer than `git reset --hard`: the bad/intermediate commits remain in history for forensics.

## Technical issues / deviations requiring review

1. **Native BAT execution was not possible in this runtime.** The available execution environment is Linux and has no `cmd.exe`, PowerShell, or Wine. Therefore:
   - Git behavior was functionally exercised in a disposable sandbox using the same underlying Git operations.
   - BAT control-flow and gates were statically validated.
   - A final native Windows sandbox run is still required before live-Dojo deployment.

2. **BASELINE pre-init `git status --short` is impossible before `git init`.** The script explicitly prints `[repository not initialized yet]`, then initializes Git and performs the real status/staging review. If any post-init safety gate fails, the newly created `.git` is removed so the sandbox returns to the pre-BASELINE state.

3. **“Explicit preparation state” for an already existing `.git` is undefined in the contract.** v1 therefore fails closed: BASELINE is allowed only when `.git` is absent.

4. **Sandbox test override added:** production ROOT remains hard-fixed to `D:\Gemini\dojo`. An alternate root is accepted only when both `DOJO_GIT_TEST_MODE=1` and `DOJO_GIT_TEST_ROOT` are explicitly supplied. This exists solely so the exact scripts can be tested outside the live Dojo.

5. **Unexpected-file policy:** already tracked files are treated as expected. New untracked files are accepted by default only for the contract’s stated normal areas (`Input/`, `src/`, `config/`, `Evidence/`, `git_tools/`, root Markdown files, `.gitignore`, `dojo_git.bat`). Other new paths fail closed with `[REVIEW REQUIRED]`.

6. **Remote gate:** checkpoint and rollback operations block if any Git remote is configured. This mechanically enforces the contract’s “local recovery / no remote” requirement.

7. **FINAL bundle path:** bundles are created outside the repository in the sibling directory `..\dojo_bundles`, preventing release bundles from becoming checkpoint candidates.

## Native Windows test still required before PASS

Run only in a temporary Windows sandbox, for example:

```bat
set DOJO_GIT_TEST_MODE=1
set DOJO_GIT_TEST_ROOT=D:\Gemini\dojo_git_test
dojo_git.bat
```

Exercise menu items 0–6 and then test:

```bat
git_tools\rollback_authorized.bat <known-good-hash> <external-auth-token>
```

Do **not** install into the live `D:\Gemini\dojo` until DeepSeek technical review and Doctor rollback/destructive safety review both PASS.

## STOP

Implementation complete. No live-Dojo deployment performed.
