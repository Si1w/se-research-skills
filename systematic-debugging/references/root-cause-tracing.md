# Root Cause Tracing

Bugs often manifest deep in the call stack. Your instinct is to fix where the error appears, but that's treating a symptom.

**Core principle:** Trace backward through the call chain until you find the original trigger, then fix at the source.

## When to Use

- Error happens deep in execution (not at entry point)
- Stack trace shows long call chain
- Unclear where invalid data originated

## The Tracing Process

### 1. Observe the Symptom
```
Error: git init failed in ~/project/packages/core
```

### 2. Find Immediate Cause
```typescript
await execFileAsync('git', ['init'], { cwd: projectDir });
```

### 3. Ask: What Called This?
```typescript
WorktreeManager.createSessionWorktree(projectDir, sessionId)
  → called by Session.initializeWorkspace()
  → called by Session.create()
  → called by test at Project.create()
```

### 4. Keep Tracing Up
- `projectDir = ''` (empty string!)
- Empty string as `cwd` resolves to `process.cwd()`

### 5. Find Original Trigger
```typescript
const context = setupCoreTest(); // Returns { tempDir: '' }
Project.create('name', context.tempDir); // Accessed before beforeEach!
```

## Adding Stack Traces

When you can't trace manually:

```typescript
async function gitInit(directory: string) {
  const stack = new Error().stack;
  console.error('DEBUG git init:', {
    directory,
    cwd: process.cwd(),
    stack,
  });
  await execFileAsync('git', ['init'], { cwd: directory });
}
```

- Use `console.error()` in tests (not logger — may not show)
- Log BEFORE the dangerous operation, not after it fails
- Include context: directory, cwd, environment variables

## Finding Which Test Causes Pollution

If something appears during tests but you don't know which test, use bisection: run tests one-by-one, stop at first polluter.

```bash
# Run each test file individually, check for side effects after each
for f in $(find . -name '*.test.ts'); do
  npx jest "$f" --forceExit 2>/dev/null
  if [ -d ".git/unexpected" ]; then
    echo "POLLUTER: $f"
    break
  fi
done
```

## Key Principle

**NEVER fix just where the error appears.** Trace back to find the original trigger. Then add defense-in-depth validation at each layer (see `defense-in-depth.md`).
