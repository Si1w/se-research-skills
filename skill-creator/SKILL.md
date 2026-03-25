---
name: skill-creator
description: Create new skills, modify and improve existing skills. Use when users want to create a skill from scratch, update or optimize an existing skill, or need guidance on skill structure and writing patterns.
---

# Skill Creator

Treat each skill as a product. Start from the real problem, validate every decision, then build.

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
1. **Trigger description** — specific enough to avoid false triggers, broad enough to catch all uses. Claude undertriggers by default, so err toward "pushy".
2. **Anti-patterns** — catalog common mistakes explicitly. Often more useful than positive instructions because they prevent the worst failures.
3. **Output format** — define with a concrete template or example.
4. **Constraints** — few, well-justified hard rules.

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

When a skill covers multiple domains, organize references by variant — Claude loads only the relevant one.

### Writing Principles

**Explain why.** "Use past tense in results — readers expect completed experiments described as finished work" beats "ALWAYS use past tense." The model handles edge cases better when it understands the reasoning.

**Be precise where it matters.** Technical specs (font sizes, file formats, output structure) need exact values. Judgment calls (writing style, emphasis) need principles.

**Anti-patterns earn their weight.** What NOT to do is often more valuable than what to do.

**Keep SKILL.md lean.** Workflow and rules in SKILL.md. Domain knowledge in references. If approaching 500 lines, add a reference layer with clear pointers.
