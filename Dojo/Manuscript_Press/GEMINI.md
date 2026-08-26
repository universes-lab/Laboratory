# PROJECT GEMINI

## PROJECT ID

PROJECT: Coding Samurai Dojo
ROOT: D:\Gemini\dojo

## PURPOSE

Controlled workspace for Coding Samurai tasks, project restarts,
implementation tests, and validation before accepted work is moved
to its permanent project location.

## PROJECT MAP

- Current_Prompt.md — current operational frame for Coding Samurai
- SPEC.md — active task specification when explicitly activated
- state/ — mechanical execution state
- logs/ — task-local execution records

Additional files and directories may be introduced by the active task.
Their presence does not make them permanent Dojo structure.

## CONTROL

CURRENT PROMPT: D:\Gemini\dojo\Current_Prompt.md
STATE: D:\Gemini\dojo\state\current_state.yaml

ACTIVE SPEC: referenced by Current Prompt.
Do not search for or infer an Active SPEC.

Current Prompt is the active operational frame for Coding Samurai.
STATE records execution state only.

A project-specific prompt used by software being developed is NOT
Coding Samurai's Current Prompt.

## AUTHORITY

CODE / SPEC → Coding Sensei DeepSeek
PROMPT / MODEL BEHAVIOR → Grok
CLI / SESSION / QUOTA / EXECUTION HEALTH → Samurai Doctor ChatGPT
FINAL AUTHORITY → Shogun

## PERMANENT BOUNDARIES

- D:\Gemini\dojo is the active Dojo root.
- Do not infer a task from files present in the Dojo.
- Do not execute an empty or inactive SPEC.
- Do not create, modify, or reinterpret prompt content unless the active
  task explicitly authorizes that operation.
- Project-specific model prompts and Coding Samurai control prompts are
  separate namespaces.
- Work outside the active Current Prompt requires STOP → QUERY.

If a required action conflicts with a permanent boundary:
STOP → QUERY.

## REFERENCE ACCESS

DEFAULT: DENY

Do not inspect files, directories, repositories, or projects outside ROOT
unless they are explicitly authorized by the active Current Prompt or SPEC.

Permanent exceptions:
- NONE