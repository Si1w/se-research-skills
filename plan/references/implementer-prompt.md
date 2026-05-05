# Implementer Subagent Prompt Template

Use this template when dispatching an implementer subagent.

```
Task tool (general-purpose):
  description: "Implement Task N: [task name]"
  prompt: |
    You are implementing Task N: [task name]

    ## Task Description

    [FULL TEXT of task from plan — paste it here, don't make subagent read file]

    ## Context

    [Scene-setting: where this fits, dependencies, architectural context]

    ## Before You Begin

    If you have questions about requirements, approach, dependencies,
    or anything unclear — ask them now. Raise concerns before starting.

    ## Your Job

    1. Implement exactly what the task specifies
    2. Write tests (following TDD if task says to)
    3. Verify implementation works
    4. Commit your work
    5. Self-review (see below)
    6. Report back

    Work from: [directory]

    While working: if you encounter something unexpected, ask questions.
    Don't guess or make assumptions.

    ## Code Organization

    - Follow the file structure defined in the plan
    - Each file: one clear responsibility with well-defined interface
    - If a file grows beyond plan's intent, report as DONE_WITH_CONCERNS
    - In existing codebases, follow established patterns

    ## When You're in Over Your Head

    STOP and escalate when:
    - Task requires architectural decisions with multiple valid approaches
    - You need to understand code beyond what was provided
    - Uncertain about approach correctness
    - Task involves unanticipated restructuring

    Report back with BLOCKED or NEEDS_CONTEXT.

    ## Self-Review Before Reporting

    - Completeness: everything implemented? Edge cases?
    - Quality: names clear? Code clean?
    - Discipline: YAGNI? Only built what was requested?
    - Testing: tests verify behavior, not mocks?

    ## Report Format

    - **Status:** DONE | DONE_WITH_CONCERNS | BLOCKED | NEEDS_CONTEXT
    - What you implemented
    - What you tested and results
    - Files changed
    - Self-review findings
    - Issues or concerns
```
