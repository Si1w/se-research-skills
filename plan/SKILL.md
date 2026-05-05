---
name: plan
description: Use when you have a spec or requirements for a multi-step task. Covers both writing implementation plans and executing them. Use before touching code for complex features, or when you have a written plan ready to execute.
---

# Implementation Plans

Write comprehensive implementation plans, then execute them task by task.

Two modes:
- **Write** — create a plan from spec/requirements
- **Execute** — implement a plan task by task

---

## Mode 1: Write Plan

### Scope Check

If the spec covers multiple independent subsystems, suggest breaking into separate plans — one per subsystem. Each plan should produce working, testable software on its own.

### File Structure

Before defining tasks, map out which files will be created or modified:

- Design units with clear boundaries and well-defined interfaces. Each file: one clear responsibility.
- Prefer smaller, focused files over large ones that do too much.
- Files that change together should live together. Split by responsibility, not by technical layer.
- In existing codebases, follow established patterns.

### Bite-Sized Task Granularity

Each step is one action (2-5 minutes):
- "Write the failing test" — step
- "Run it to make sure it fails" — step
- "Implement the minimal code to make the test pass" — step
- "Run the tests" — step
- "Commit" — step

### Plan Document Structure

````markdown
# [Feature Name] Implementation Plan

**Goal:** [One sentence]
**Architecture:** [2-3 sentences about approach]
**Tech Stack:** [Key technologies/libraries]

---

### Task N: [Component Name]

**Files:**
- Create: `exact/path/to/file.py`
- Modify: `exact/path/to/existing.py:123-145`
- Test: `tests/exact/path/to/test.py`

- [ ] **Step 1: Write the failing test**

```python
def test_specific_behavior():
    result = function(input)
    assert result == expected
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/path/test.py::test_name -v`
Expected: FAIL with "function not defined"

- [ ] **Step 3: Write minimal implementation**

```python
def function(input):
    return expected
```

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest tests/path/test.py::test_name -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add tests/path/test.py src/path/file.py
git commit -m "feat: add specific feature"
```
````

### No Placeholders

Every step must contain actual content. These are **plan failures**:
- "TBD", "TODO", "implement later"
- "Add appropriate error handling" / "add validation"
- "Write tests for the above" (without actual test code)
- "Similar to Task N" (repeat the code)
- Steps without code blocks for code steps

### Self-Review

After writing the complete plan:

1. **Spec coverage:** Can you point to a task for each requirement?
2. **Placeholder scan:** Any red flags from the No Placeholders section?
3. **Type consistency:** Do types, method signatures, and names match across tasks?

Fix issues inline.

### Execution Handoff

After saving the plan, offer execution:

> "Plan saved to `{path}`. Ready to execute?"

---

## Mode 2: Execute Plan

### Step 1: Load and Review

1. Read plan file
2. Review critically — identify questions or concerns
3. If concerns: raise them before starting
4. If clear: proceed

### Step 2: Execute Tasks

**With subagent support (recommended):**

For each task, dispatch a fresh subagent:

1. **Implementer subagent** — provide full task text + context (don't make subagent read the plan file). Handle responses:
   - DONE → proceed to review
   - DONE_WITH_CONCERNS → assess concerns, then review
   - NEEDS_CONTEXT → provide info, re-dispatch
   - BLOCKED → resolve or escalate

2. **Spec reviewer subagent** — verify implementation matches spec (nothing more, nothing less). Use template at `references/spec-reviewer-prompt.md`.

3. **Code quality reviewer subagent** — verify clean, tested, maintainable code. Only after spec review passes. Use template at `references/code-reviewer-prompt.md`.

4. If reviewers find issues → implementer fixes → re-review until approved.

5. Mark task complete, proceed to next.

**Without subagent support:**

For each task:
1. Follow each step exactly
2. Run verifications as specified
3. Mark complete

### Step 3: Complete

After all tasks complete:
- Run full test suite
- Verify all requirements met
- Use `/gh-pr` to create PR, or inform user work is ready

### When to Stop and Ask

- Hit a blocker (missing dependency, test fails, instruction unclear)
- Plan has critical gaps
- Verification fails repeatedly
- Don't force through blockers — stop and ask

## Prompt Templates

Available in `references/`:

- **`implementer-prompt.md`** — dispatch implementer subagent
- **`spec-reviewer-prompt.md`** — dispatch spec compliance reviewer
- **`code-reviewer-prompt.md`** — dispatch code quality reviewer (shared with code-review skill)

## Red Flags

- Starting implementation on main/master without explicit consent
- Skipping reviews (spec compliance OR code quality)
- Dispatching multiple implementation subagents in parallel (conflicts)
- Starting code quality review before spec compliance passes
- Moving to next task with open review issues
- Accepting "close enough" on spec compliance
