---
name: code-review
description: Use when completing tasks, implementing major features, before merging, or when receiving code review feedback. Covers both requesting fresh code review and handling review feedback with technical rigor.
---

# Code Review

Two modes:
- **Request** — dispatch a fresh reviewer to catch issues
- **Receive** — evaluate feedback with technical rigor, not performative agreement

---

## Mode 1: Request Review

Dispatch a code reviewer subagent with precisely crafted context — never your session history.

### When to Request

**Recommended:**
- After completing a major feature
- Before merge to main
- When stuck (fresh perspective)
- After fixing a complex bug

### How to Request

1. **Get git SHAs:**
```bash
BASE_SHA=$(git merge-base HEAD main)  # or origin/main
HEAD_SHA=$(git rev-parse HEAD)
```

2. **Dispatch reviewer subagent** using the template at `references/code-reviewer-prompt.md`. Fill in:
   - `{DESCRIPTION}` — brief summary of what was built
   - `{PLAN_OR_REQUIREMENTS}` — what it should do
   - `{BASE_SHA}` — starting commit
   - `{HEAD_SHA}` — ending commit

3. **Act on feedback:**
   - Fix Critical issues immediately
   - Fix Important issues before proceeding
   - Note Minor issues for later
   - Push back if reviewer is wrong (with reasoning)

---

## Mode 2: Receive Feedback

### The Response Pattern

```
1. READ: Complete feedback without reacting
2. UNDERSTAND: Restate requirement in own words (or ask)
3. VERIFY: Check against codebase reality
4. EVALUATE: Technically sound for THIS codebase?
5. RESPOND: Technical acknowledgment or reasoned pushback
6. IMPLEMENT: One item at a time, test each
```

### Forbidden Responses

- "You're absolutely right!" (performative)
- "Great point!" / "Excellent feedback!" (performative)
- "Let me implement that now" (before verification)

**Instead:** Restate the technical requirement. Ask clarifying questions. Push back with reasoning if wrong. Just start working — actions > words.

### Handling Unclear Feedback

If any item is unclear: **STOP** — do not implement anything yet. Ask for clarification on unclear items first. Items may be related; partial understanding = wrong implementation.

### From External Reviewers

Before implementing:
1. Technically correct for THIS codebase?
2. Breaks existing functionality?
3. Reason for current implementation?
4. Works on all platforms/versions?
5. Does reviewer understand full context?

If suggestion seems wrong → push back with technical reasoning.
If conflicts with prior architectural decisions → discuss first.

### YAGNI Check

If reviewer suggests "implementing properly":
```bash
grep -r "function_name" .  # Check actual usage
```
If unused: "This isn't called. Remove it (YAGNI)?"
If used: then implement properly.

### Implementation Order

For multi-item feedback:
1. Clarify anything unclear FIRST
2. Blocking issues (breaks, security)
3. Simple fixes (typos, imports)
4. Complex fixes (refactoring, logic)
5. Test each fix individually
6. Verify no regressions

### When to Push Back

- Suggestion breaks existing functionality
- Reviewer lacks full context
- Violates YAGNI (unused feature)
- Technically incorrect for this stack
- Conflicts with architectural decisions

**How:** Technical reasoning, not defensiveness. Ask specific questions. Reference working tests/code.

### Acknowledging Correct Feedback

```
GOOD: "Fixed. [Brief description]"
GOOD: "Good catch — [issue]. Fixed in [location]."
GOOD: [Just fix it and show in the code]

BAD: "You're absolutely right!"
BAD: "Thanks for catching that!"
BAD: ANY gratitude expression
```

Actions speak. The code itself shows you heard the feedback.

## Anti-patterns

- Skipping review because "it's simple"
- Blind implementation without verification
- Performative agreement instead of technical evaluation
- Batch implementing without testing each fix
- Avoiding pushback when feedback is technically wrong
- Can't verify but proceeding anyway
