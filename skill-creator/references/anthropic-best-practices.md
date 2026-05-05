# Anthropic Skill Authoring Best Practices

Summary of official guidance for writing Claude Code skills.

## Core Principles

1. **Concise** — skills load into every conversation where triggered. Every token counts.
2. **Appropriate degrees of freedom** — be prescriptive for mechanical tasks, flexible for judgment calls.
3. **Test with all models** — skills should work across Opus, Sonnet, and Haiku.

## Skill Structure

### Naming
- Use letters, numbers, and hyphens only
- Active voice, verb-first: `creating-skills` not `skill-creation`
- Name by action or core insight

### Description (Critical)
- Max 1024 characters total for frontmatter
- Start with "Use when..." — triggering conditions ONLY
- Never summarize the skill's workflow in the description
- Write in third person
- Include symptoms, situations, and contexts

### Progressive Disclosure
- Overview first (scannable in seconds)
- Details on demand (reference files loaded when needed)
- Keep SKILL.md under 500 lines

## Content Guidelines

- **Imperative form** for instructions ("Run tests" not "You should run tests")
- **Tables** for quick-reference lookups
- **Anti-patterns** section — often more valuable than positive instructions
- **One excellent example** beats many mediocre ones
- **No narrative storytelling** — reusable techniques only

## Common Patterns

### Template Pattern
Provide exact output format with placeholders.

### Conditional Workflow
Different paths based on context — use decision tables or flowcharts for non-obvious decisions.

### Reference Pattern
Heavy domain knowledge in `references/` — SKILL.md points to the right file.

## Anti-Patterns to Avoid

- Multi-language examples (one good example suffices)
- Verbose descriptions that summarize workflow
- Force-loading references with `@` syntax (burns context)
- Narrative examples ("In session X, we found...")
- Generic labels (step1, helper2)

## Evaluation

Test skills by:
1. Running real scenarios without the skill (baseline)
2. Running same scenarios with the skill
3. Comparing behavior — skill should measurably improve outcomes
4. Pressure testing under adversarial conditions
