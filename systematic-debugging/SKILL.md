---
name: systematic-debugging
description: Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes. Also use when under time pressure, when "just one quick fix" seems obvious, or when previous fixes haven't worked.
---

# Systematic Debugging

Random fixes waste time and create new bugs. Quick patches mask underlying issues.

**Core principle:** ALWAYS find root cause before attempting fixes. Symptom fixes are failure.

## The Iron Law

```
NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST
```

If you haven't completed Phase 1, you cannot propose fixes.

## The Four Phases

You MUST complete each phase before proceeding to the next.

### Phase 1: Root Cause Investigation

**BEFORE attempting ANY fix:**

1. **Read Error Messages Carefully**
   - Don't skip past errors or warnings
   - Read stack traces completely
   - Note line numbers, file paths, error codes

2. **Reproduce Consistently**
   - Can you trigger it reliably? What are the exact steps?
   - If not reproducible → gather more data, don't guess

3. **Check Recent Changes**
   - What changed? Git diff, recent commits
   - New dependencies, config changes, environmental differences

4. **Gather Evidence in Multi-Component Systems**

   For EACH component boundary:
   - Log what data enters and exits the component
   - Verify environment/config propagation
   - Run once to gather evidence showing WHERE it breaks
   - THEN investigate the specific failing component

5. **Trace Data Flow**

   When the error is deep in the call stack, trace backward:
   - Where does the bad value originate?
   - What called this with the bad value?
   - Keep tracing up until you find the source
   - Fix at source, not at symptom

   See `references/root-cause-tracing.md` for the complete backward tracing technique.

### Phase 2: Pattern Analysis

1. **Find Working Examples** — locate similar working code in the same codebase
2. **Compare Against References** — read reference implementations COMPLETELY, don't skim
3. **Identify Differences** — list every difference, however small
4. **Understand Dependencies** — what components, settings, config, assumptions?

### Phase 3: Hypothesis and Testing

1. **Form Single Hypothesis** — "I think X is the root cause because Y"
2. **Test Minimally** — smallest possible change, one variable at a time
3. **Verify Before Continuing** — worked → Phase 4. Didn't work → new hypothesis, don't pile on more fixes.
4. **When You Don't Know** — say so. Ask for help. Research more.

### Phase 4: Implementation

1. **Create Failing Test Case** — simplest reproduction, automated if possible. MUST have before fixing. Use `/tdd` for proper test writing.
2. **Implement Single Fix** — address the root cause. ONE change at a time. No "while I'm here" improvements.
3. **Verify Fix** — test passes? No other tests broken? Issue resolved?
4. **If Fix Doesn't Work:**
   - If < 3 attempts: return to Phase 1, re-analyze
   - **If >= 3 attempts: STOP. Question the architecture.** 3+ failed fixes = architectural problem, not a bug. Discuss before attempting more fixes.

## Red Flags — STOP and Follow Process

- "Quick fix for now, investigate later"
- "Just try changing X and see if it works"
- "Skip the test, I'll manually verify"
- "It's probably X, let me fix that"
- "I don't fully understand but this might work"
- Proposing solutions before tracing data flow
- "One more fix attempt" (when already tried 2+)
- Each fix reveals new problem in different place

**ALL of these mean: STOP. Return to Phase 1.**

## Common Rationalizations

| Excuse | Reality |
|--------|---------|
| "Issue is simple, don't need process" | Simple issues have root causes too. Process is fast for simple bugs. |
| "Emergency, no time for process" | Systematic debugging is FASTER than guess-and-check thrashing. |
| "Just try this first, then investigate" | First fix sets the pattern. Do it right from the start. |
| "Multiple fixes at once saves time" | Can't isolate what worked. Causes new bugs. |
| "I see the problem, let me fix it" | Seeing symptoms != understanding root cause. |
| "One more fix attempt" (after 2+ failures) | 3+ failures = architectural problem. Question the pattern. |

## Supporting Techniques

Available in `references/`:

- **`root-cause-tracing.md`** — Trace bugs backward through call stack to find original trigger
- **`defense-in-depth.md`** — Add validation at multiple layers to make bugs structurally impossible
- **`condition-based-waiting.md`** — Replace arbitrary timeouts with condition polling to eliminate flaky tests
