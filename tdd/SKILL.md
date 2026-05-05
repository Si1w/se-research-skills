---
name: tdd
description: Use when implementing any feature or bugfix, before writing implementation code. Also use when about to claim work is complete, fixed, or passing — requires evidence before assertions.
---

# Test-Driven Development & Verification

Write the test first. Watch it fail. Write minimal code to pass. Verify before claiming done.

**Core principles:**
- If you didn't watch the test fail, you don't know if it tests the right thing.
- If you haven't run verification, you cannot claim it passes.

## The Iron Laws

```
NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST
NO COMPLETION CLAIMS WITHOUT FRESH VERIFICATION EVIDENCE
```

Write code before the test? Delete it. Start over.
Claim "tests pass" without running them? That's dishonesty, not efficiency.

**No exceptions:**
- Don't keep pre-test code as "reference"
- Don't "adapt" it while writing tests
- Delete means delete

## Naming Conventions

Before writing any code, check if `.claude/rules/naming.md` exists in the project. This file is the single source of truth for naming conventions — variable names, function names, class names, constants, file names, etc.

- **Before naming anything**, check `naming.md` for existing conventions. Follow them exactly.
- **When introducing a new name** that establishes a pattern not yet in `naming.md`, add it:
  ```markdown
  ## Session Management
  - **Canonical term:** `session` (not `sess`, `ctx`, `context`)
  - **Functions:** `createSession`, `destroySession` (verb + noun)
  - **Files:** `session-manager.ts` (kebab-case)
  ```
- **When the user renames or corrects a term**, update `naming.md` accordingly.
- If `naming.md` does not exist yet, create it when the first naming decision is made and ask the user to confirm.

This prevents inconsistency across files (e.g., `getUser` in one file, `fetchUser` in another, `retrieveUser` in a third).

## Red-Green-Refactor

### RED — Write Failing Test

Write one minimal test showing what should happen.

**Requirements:** One behavior. Clear name. Real code (no mocks unless unavoidable).

```typescript
test('rejects empty email', async () => {
  const result = await submitForm({ email: '' });
  expect(result.error).toBe('Email required');
});
```

### Verify RED — Watch It Fail

**MANDATORY. Never skip.**

```bash
npm test path/to/test.test.ts
```

Confirm: test fails (not errors), failure message is expected, fails because feature is missing (not typos).

- Test passes immediately? You're testing existing behavior. Fix the test.
- Test errors? Fix the error, re-run until it fails correctly.

### GREEN — Minimal Code

Write the simplest code to pass the test. Don't add features, refactor other code, or "improve" beyond the test.

```typescript
function submitForm(data: FormData) {
  if (!data.email?.trim()) {
    return { error: 'Email required' };
  }
  // ...
}
```

### Verify GREEN — Watch It Pass

**MANDATORY.**

Confirm: test passes, other tests still pass, output pristine (no errors, warnings).

- Test fails? Fix code, not test.
- Other tests fail? Fix now.

### REFACTOR — Clean Up

After green only: remove duplication, improve names, extract helpers. Keep tests green. Don't add behavior.

### Repeat

Next failing test for next feature.

## Verification Gate

Before claiming ANY status or expressing satisfaction:

1. **IDENTIFY:** What command proves this claim?
2. **RUN:** Execute the FULL command (fresh, complete)
3. **READ:** Full output, check exit code, count failures
4. **VERIFY:** Does output confirm the claim?
5. **ONLY THEN:** Make the claim

| Claim | Requires | Not Sufficient |
|-------|----------|----------------|
| Tests pass | Test output: 0 failures | Previous run, "should pass" |
| Build succeeds | Build command: exit 0 | Linter passing |
| Bug fixed | Test original symptom: passes | Code changed, assumed fixed |
| Requirements met | Line-by-line checklist | Tests passing |

**Red flags:** Using "should", "probably", "seems to". Expressing satisfaction before verification. About to commit without verification.

| Excuse | Reality |
|--------|---------|
| "Should work now" | RUN the verification |
| "I'm confident" | Confidence != evidence |
| "Just this once" | No exceptions |
| "Agent said success" | Verify independently |

## Good Tests

| Quality | Good | Bad |
|---------|------|-----|
| **Minimal** | One thing. "and" in name? Split it. | `test('validates email and domain and whitespace')` |
| **Clear** | Name describes behavior | `test('test1')` |
| **Shows intent** | Demonstrates desired API | Obscures what code should do |

## Why Order Matters

**"I'll write tests after"** — Tests written after pass immediately. Passing immediately proves nothing: might test wrong thing, miss edge cases, test implementation not behavior.

**"Already manually tested"** — Manual testing is ad-hoc. No record, can't re-run, easy to forget cases under pressure.

**"Deleting X hours of work is wasteful"** — Sunk cost fallacy. The "waste" is keeping code you can't trust.

## Common Rationalizations

| Excuse | Reality |
|--------|---------|
| "Too simple to test" | Simple code breaks. Test takes 30 seconds. |
| "I'll test after" | Tests passing immediately prove nothing. |
| "Tests after achieve same goals" | Tests-after = "what does this do?" Tests-first = "what should this do?" |
| "Keep as reference, write tests first" | You'll adapt it. That's testing after. Delete means delete. |
| "TDD will slow me down" | TDD faster than debugging. |

## Red Flags — STOP and Start Over

- Code before test
- Test passes immediately
- Can't explain why test failed
- Rationalizing "just this once"
- "It's about spirit not ritual"
- "This is different because..."
- ANY wording implying success without having run verification

**All of these mean: Delete code. Start over with TDD.**

## Verification Checklist

Before marking work complete:

- [ ] Every new function/method has a test
- [ ] Watched each test fail before implementing
- [ ] Each test failed for expected reason
- [ ] Wrote minimal code to pass each test
- [ ] All tests pass (fresh run, not cached)
- [ ] Output pristine (no errors, warnings)
- [ ] Tests use real code (mocks only if unavoidable)
- [ ] Edge cases and errors covered

Can't check all boxes? You skipped TDD. Start over.

## Testing Anti-Patterns

When adding mocks or test utilities, see `references/testing-anti-patterns.md` to avoid:
- Testing mock behavior instead of real behavior
- Adding test-only methods to production classes
- Mocking without understanding dependencies
- Incomplete mocks that hide structural assumptions
