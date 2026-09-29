# PROJECT GEMINI
# CODING SAMURAI DOJO

## DOJO ROOT

```text
E:\Gemini\Dojo
```

This is the common parent workspace for Coding Samurai projects.

Each project lives in its own child directory, for example:

```text
E:\Gemini\Dojo\Manuscript_Press
```

The Dojo root is not itself an active project.

---

## PURPOSE

The Dojo provides one common controlled environment for Coding Samurai.

Project-specific operational authority lives inside the selected project directory.

A project does NOT require its own `GEMINI.md`.

By default, project control is provided by:

```text
Current_Prompt.md
SPEC.md
STEP.md
and other authority artifacts explicitly activated by them.
```

A project-local `GEMINI.md` is not assumed and must not be invented.

---

## PROJECT ORIENTATION

At session start:

1. Establish the actual current workspace.

2. If the workspace is:

```text
E:\Gemini\Dojo
```

then no child project is active unless the user explicitly selects one.

3. If the workspace is inside a child directory of:

```text
E:\Gemini\Dojo
```

treat that child directory as the current PROJECT ROOT.

Example:

```text
E:\Gemini\Dojo\Manuscript_Press
```

means:

```yaml
PROJECT_ROOT: E:\Gemini\Dojo\Manuscript_Press
```

4. In the current PROJECT ROOT, inspect `Current_Prompt.md` when present.

`Current_Prompt.md` is the project's current operational frame.

5. Read or activate `SPEC.md`, `STEP.md`, or other project authority only as directed by the current operational frame or explicit external instruction.

Do not search other child projects for authority.

---

## NO ROOT-LEVEL CURRENT PROMPT

There is no permanent:

```text
E:\Gemini\Dojo\Current_Prompt.md
```

There is no permanent root-level:

- PROJECT;
- ACTIVE_MODE;
- ACTIVE_OPERATION;
- SPEC;
- STEP;
- execution state.

Do not infer one.

If Samurai is started directly in:

```text
E:\Gemini\Dojo
```

without an explicit task:

```text
WAIT
```

---

## PROJECT ISOLATION

Each child directory is an independent project namespace.

Do not carry between projects:

- PROJECT identity;
- ROOT;
- ACTIVE_MODE;
- ACTIVE_OPERATION;
- Current Prompt;
- SPEC;
- STEP;
- implementation state;
- execution state;
- unfinished work;
- permissions;
- acceptance state.

Do not inspect sibling projects merely to reconstruct history or discover work.

Cross-project access requires explicit authorization.

---

## AUTHORITY MODEL

The Dojo root does not assign ownership of project-specific technical artifacts.

Authority for:

- SPEC;
- architecture;
- route;
- STEP;
- implementation;
- model behavior;
- acceptance;

is defined by the active project's authority structure and current external instructions.

Do not infer artifact ownership from another project or from historical practice.

Permanent final authority:

```text
FINAL AUTHORITY → Author / Shogun
```

Capability is not authorization.

---

## CURRENT PROMPT

When `Current_Prompt.md` exists in the current PROJECT ROOT:

- it defines the current operational frame;
- it establishes ACTIVE_MODE when required;
- it identifies the active operation;
- it defines the current authorization boundary;
- it identifies or activates the relevant technical authorities.

Do not replace it with remembered session state.

Do not create a hidden Current Prompt.

If `Current_Prompt.md` changes, treat it as a new operational frame.

---

## SPEC / STEP DISCIPLINE

The existence of `SPEC.md` or `STEP.md` in a project does not by itself authorize execution.

Use them only when activated by:

- the current `Current_Prompt.md`;
- or an explicit current external instruction.

Do not search for another SPEC or STEP merely because the current one appears incomplete.

Do not create:

- SUBSTEP;
- hidden STEP;
- private implementation plan;
- extra approval layer;

as a new authority level unless explicitly authorized.

A current external technical instruction may clarify or correct the active STEP without silently creating a new workflow hierarchy.

---

## HISTORICAL STATE

Files left from previous runs are evidence or historical state unless current authority explicitly activates them.

This includes:

- old prompts;
- old STEP files;
- outputs;
- run directories;
- checkpoints;
- logs;
- launchers;
- resume parameters;
- temporary state.

Presence on disk is not authorization.

Do not automatically resume unfinished work.

Do not promote historical execution state into the current operation.

---

## REFERENCE ACCESS

Default scope:

```text
CURRENT PROJECT ROOT
```

Do not inspect:

- sibling Dojo projects;
- parent repositories;
- unrelated directories;
- unrelated historical projects;

unless explicitly authorized.

References outside PROJECT ROOT may be used only when the current task or authority explicitly permits them.

---

## EXECUTION BOUNDARY

Inside an active project:

```text
GLOBAL SAMURAI DISCIPLINE
→ DOJO ORIENTATION
→ CURRENT PROJECT ROOT
→ Current_Prompt.md
→ activated SPEC / STEP / current external instruction
```

More specific valid authority refines the more general layer.

It does not silently erase permanent Coding Samurai discipline.

---

## STARTUP DISCIPLINE

At every new session:

```text
1. Use the already loaded global Coding Samurai context.
2. Establish actual current workspace.
3. Establish current PROJECT ROOT.
4. Read current PROJECT ROOT\Current_Prompt.md when present.
5. Establish PROJECT, ACTIVE_MODE, ACTIVE_OPERATION and authorization.
6. Read only the technical authority required by that frame.
7. Execute nothing until orientation is sufficient.
```

Do not reconstruct the task from:

- old chat history;
- neighboring projects;
- arbitrary files;
- previous session state.

If no active task exists:

```text
WAIT
```

If required authority is materially ambiguous or contradictory:

```text
STOP → REPORT → QUERY
```

---

## PERMANENT PRINCIPLE

`E:\Gemini\Dojo` defines the common workspace.

The selected child directory defines the project.

`Current_Prompt.md` defines what Samurai is doing now.

Activated technical authority defines how that work is to be performed.

Do not add another control layer unless explicitly authorized.

END OF DOJO CONTEXT