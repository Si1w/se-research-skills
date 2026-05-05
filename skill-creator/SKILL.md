---
name: skill-creator
description: Create new skills, modify and improve existing skills. Use when users want to create a skill from scratch, turn a conversation into a skill, update or optimize an existing skill, or need guidance on skill structure and writing patterns.
---

# Skill Creator

Treat each skill as a product. Start from the real problem, validate every decision, then build and test.

Determine where the user is and jump in:
- New skill → Phase 1
- "Turn this into a skill" → extract from conversation history, confirm gaps, then Phase 2
- Improving existing skill → read current SKILL.md, identify the gap, revise

---

## Phase 1: Problem Discovery

Understand the problem before writing anything. Have a conversation — don't dump all questions at once.

**The Problem**
- What do you do manually today that this skill should handle?
- Show me an example — a past conversation, a file, a workflow.
- What goes wrong without a skill? What's the failure mode?

**The Interaction**
- What would you say to Claude to invoke this? What trigger phrases?
- What does the ideal output look like? Format, content, destination.
- Are there distinct modes? (e.g., write/trim/expand, review/proofread)

**The Scope**
- What should this skill NOT do?
- What's the minimum version that's already useful?

---

## Phase 2: Design

Plan structure before writing. Present to the user for feedback.

**Content Architecture**
- **SKILL.md** (<500 lines): workflow, rules, constraints, examples
- **references/**: domain knowledge loaded only when relevant
- **assets/**: templates, files used in output
- **scripts/**: deterministic tasks to execute, not reason about

**Key Decisions**
1. **Trigger description** — specific enough to avoid false triggers, broad enough to catch all uses. Agent undertriggers by default, so err toward "pushy".
2. **Anti-patterns** — catalog common mistakes explicitly. Often more useful than positive instructions because they prevent the worst failures.
3. **Output format** — define with a concrete template or example.
4. **Constraints** — few, well-justified hard rules.

### Agent Search Optimization (ASO)

The agent reads the `description` field to decide which skills to load. This is the single most important field for discoverability.

**Description = when to trigger, NOT what the skill does.**

Testing revealed that when a description summarizes the skill's workflow, the agent may follow the description instead of reading the full skill content. A description saying "code review between tasks" caused the agent to do ONE review, even though the skill specified TWO reviews.

```yaml
# BAD: Summarizes workflow — agent takes this as a shortcut
description: Use when executing plans - dispatches subagent per task with code review between tasks

# BAD: Too much process detail
description: Use for TDD - write test first, watch it fail, write minimal code, refactor

# GOOD: Just triggering conditions
description: Use when executing implementation plans with independent tasks in the current session

# GOOD: Triggering conditions only
description: Use when implementing any feature or bugfix, before writing implementation code
```

**Keyword coverage** — use words the agent would search for:
- Error messages, symptoms, synonyms, tool names
- E.g., "flaky", "race condition", "timeout/hang/freeze"

**Token efficiency targets:**
- Frequently-loaded skills: <200 words
- Other skills: <500 words

---

## Phase 3: Build

### Frontmatter

```yaml
---
name: skill-name
description: What + when to trigger. Be specific and slightly pushy about trigger contexts.
---
```

### Structure

A good SKILL.md typically has:
1. One-line purpose
2. Workflow steps (imperative form)
3. Rules — good practices + anti-patterns
4. Output format template
5. Constraints
6. Reference pointers — when to load which file

### Directory

```
skill-name/
├── SKILL.md
├── scripts/      (optional)
├── references/   (optional)
└── assets/       (optional)
```

When a skill covers multiple domains, organize references by variant — the agent loads only the relevant one.

### Writing Principles

**Explain why.** "Use past tense in results — readers expect completed experiments described as finished work" beats "ALWAYS use past tense." The model handles edge cases better when it understands the reasoning.

**Be precise where it matters.** Technical specs (font sizes, file formats, output structure) need exact values. Judgment calls (writing style, emphasis) need principles.

**Anti-patterns earn their weight.** What NOT to do is often more valuable than what to do. Catalog common mistakes with explicit counters.

**Keep SKILL.md lean.** Workflow and rules in SKILL.md. Domain knowledge in references. If approaching 500 lines, add a reference layer with clear pointers.

---

## Phase 4: Test & Validate

**Writing skills IS Test-Driven Development applied to documentation.** If you didn't watch an agent fail without the skill, you don't know if the skill teaches the right thing.

### The Iron Law

```
NO SKILL WITHOUT A FAILING TEST FIRST
```

This applies to NEW skills AND EDITS to existing skills.

### RED-GREEN-REFACTOR for Skills

**RED — Baseline without skill:**
Run pressure scenario with subagent WITHOUT the skill. Document:
- What choices did the agent make?
- What rationalizations did it use (verbatim)?
- Which pressures triggered violations?

**GREEN — Write minimal skill:**
Write skill that addresses those specific rationalizations. Run same scenarios WITH skill. Agent should now comply.

**REFACTOR — Close loopholes:**
Agent found new rationalization? Add explicit counter. Re-test until bulletproof.

### Testing by Skill Type

| Type | Test with | Success criteria |
|------|-----------|-----------------|
| Discipline (rules) | Pressure scenarios: time + sunk cost + exhaustion | Agent follows rule under maximum pressure |
| Technique (how-to) | Application + edge case scenarios | Agent applies technique correctly |
| Pattern (mental model) | Recognition + counter-example scenarios | Agent correctly identifies when to apply |
| Reference (docs/API) | Retrieval + application scenarios | Agent finds and uses info correctly |

### Bulletproofing Against Rationalization

For discipline-enforcing skills, explicitly close every loophole:

```markdown
# BAD: Just the rule
Write code before test? Delete it.

# GOOD: Rule + closed loopholes
Write code before test? Delete it. Start over.

**No exceptions:**
- Don't keep it as "reference"
- Don't "adapt" it while writing tests
- Delete means delete
```

Build a rationalization table from baseline testing — every excuse agents make goes in:

| Excuse | Reality |
|--------|---------|
| "Skill is obviously clear" | Clear to you != clear to other agents. Test it. |
| "Testing is overkill" | Untested skills have issues. Always. |
| "I'll test if problems emerge" | Problems = agents can't use skill. Test BEFORE deploying. |

### Checklist

**RED Phase:**
- [ ] Create pressure scenarios (3+ combined pressures for discipline skills)
- [ ] Run scenarios WITHOUT skill — document baseline behavior verbatim
- [ ] Identify patterns in rationalizations/failures

**GREEN Phase:**
- [ ] Description starts with "Use when..." and includes specific triggers
- [ ] Address specific baseline failures identified in RED
- [ ] Run scenarios WITH skill — verify agents now comply

**REFACTOR Phase:**
- [ ] Identify NEW rationalizations from testing
- [ ] Add explicit counters and red flags list
- [ ] Re-test until bulletproof

**Quality Checks:**
- [ ] No narrative storytelling — reusable techniques only
- [ ] One excellent example beats many mediocre ones
- [ ] Supporting files only for heavy reference or reusable tools

For detailed testing methodology, see `references/testing-skills-with-subagents.md`.
For Anthropic's official skill authoring guidelines, see `references/anthropic-best-practices.md`.
For psychology of skill compliance, see `references/persuasion-principles.md`.
