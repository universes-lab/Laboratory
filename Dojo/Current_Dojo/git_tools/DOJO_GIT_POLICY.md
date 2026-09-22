# DOJO GIT POLICY

Git in D:\Gemini\dojo is a local recovery mechanism.

It is not the Git repository of the permanent project and has no remote by default.

## CHECKPOINT TYPES

BASELINE  
Externally confirmed initial state of the current Dojo project.

WIP  
Recoverable but NOT accepted working state.

STEP  
Externally accepted completed STEP.

FINAL  
Externally accepted release state.

Checkpoint does not imply acceptance.

## BEFORE ANY CHECKPOINT

1. Confirm ROOT = `D:\Gemini\dojo`.
2. Run `git status --short`.
3. Review all changed and untracked files.
4. Refuse forbidden or suspicious files.
5. Stage candidates.
6. Show `git diff --cached --name-status`.
7. Commit only after this staged-set review succeeds.

## ACCEPTANCE

WIP may be created when authorized by workflow.

STEP and FINAL require an externally supplied acceptance token.  
Coding Samurai cannot generate or approve this token for itself.

## ROLLBACK

Rollback is destructive.

Coding Samurai may inspect status, diff and history and propose a recovery commit.

Actual rollback requires:
- external authorization;
- externally supplied commit hash;
- preservation of forensic Evidence before rollback.

No rollback command is available in the ordinary `dojo_git.bat` menu.

## RELEASE

FINAL  
→ verify repository state  
→ transfer project  
→ verify destination  
→ create and verify git bundle  
→ only then authorize Dojo cleanup.
