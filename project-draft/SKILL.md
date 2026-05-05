---
name: project-draft
description: Brainstorm and design a project or feature before implementation. Use when the user says "I have an idea", "brainstorm", "project draft", "help me think through this", "is this worth building", "let's design this", or describes a new project/feature idea before any code is written.
---

# Brainstorming & Design

Develop an idea into a concrete design before implementation. Start from a toy project mindset — build something small and working first, then evaluate whether it can grow.

Output is a design doc (markdown file), not code.

<HARD-GATE>
Do NOT write any code, scaffold any project, or take any implementation action until you have presented a design and the user has approved it. This applies to EVERY project regardless of perceived simplicity.
</HARD-GATE>

**"This is too simple to need a design"** — Every project goes through this process. "Simple" projects are where unexamined assumptions cause the most wasted work. The design can be short, but you MUST present it and get approval.

## Workflow

### 1. Understand the Idea

- Read `CLAUDE.md` if it exists for project context.
- Check current project state (files, recent commits) if in a repo.
- Before asking detailed questions, assess scope: if the request describes multiple independent subsystems, flag this immediately. Help decompose into sub-projects first — each gets its own design → plan → implementation cycle.
- Ask: **"What do you want to build? Tell me the simplest version."**

### 2. Sharpen the Idea

Ask one at a time, skip any already answered:

| # | Question | Push until you hear |
|---|----------|---------------------|
| 1 | **What's the toy version?** Smallest thing you can build in a weekend that does one useful thing — not a demo, something you'd actually use. | A concrete, self-contained deliverable. |
| 2 | **Who else would use this?** A specific person in a specific situation. If just you, that's fine. | A name, a role, a scenario — or honest "just me." |
| 3 | **What exists today?** Closest thing out there, why it's not enough. If nothing, why not. | Specific tools/workarounds and their shortcomings. |
| 4 | **What makes this interesting?** The non-obvious angle — "huh, that's cool." | One sentence that reframes the idea. |
| 5 | **What's the growth path?** Toy → v1 → v2. Where does this top out? | Concrete milestones with triggers for each step. |

If the user says "just do it" or provides a formed plan, skip remaining questions but still run step 3 and 4.

### 3. Premise Challenge

Challenge assumptions before proposing solutions:

- **Is this the right problem?** Could a different framing yield something simpler?
- **What happens if you do nothing?** Real pain or hypothetical?
- **What already partially solves this?** Existing tools, libraries, code.
- **Is the toy useful on its own?** Toys that only matter as stepping stones rarely grow.

Present as:

```
PREMISES:
1. [statement] — agree/disagree?
2. [statement] — agree/disagree?
3. [statement] — agree/disagree?
```

If the user disagrees, revise and loop back.

### 4. Approaches

Produce 2-3 distinct approaches with trade-offs. At least one **smallest viable toy**, one **most ambitious version**. Lead with your recommended option and explain why.

```
APPROACH A: [Name]
  Summary:     [1-2 sentences]
  Effort:      [weekend / 1-2 weeks / month+]
  Risk:        [Low / Med / High]
  Toy version: [what the weekend prototype looks like]
  Growth path: [how it scales if the toy works]
  Pros:        [2-3 bullets]
  Cons:        [2-3 bullets]
```

End with: **RECOMMENDATION:** Choose [X] because [one-line reason].

Wait for user approval before proceeding.

### 5. Design

Present the design section by section, scaled to complexity. Ask after each section whether it looks right so far. Cover: architecture, components, data flow, error handling, testing.

**Design for isolation and clarity:**
- Break the system into smaller units that each have one clear purpose, communicate through well-defined interfaces, and can be understood and tested independently.
- For each unit: what does it do, how do you use it, what does it depend on?
- Can someone understand what a unit does without reading its internals? Can you change internals without breaking consumers? If not, the boundaries need work.

**Working in existing codebases:**
- Explore current structure before proposing changes. Follow existing patterns.
- Where existing code has problems affecting the work, include targeted improvements — don't propose unrelated refactoring.

### 6. Design Doc

```bash
mkdir -p design-docs
```

Write to `design-docs/{title}-{datetime}.md` using this template:

```markdown
# Project: {title}

Date: {date}
Status: DRAFT

## Problem
{What problem, for whom, why now}

## Toy Version
{Weekend prototype — what it does, what it skips, why it's useful alone}

## Growth Path
{Toy → v1 → v2. Milestones and what triggers each step.}

## Existing Landscape
{What's out there, how this differs}

## Premises
{From step 3}

## Approaches Considered
### A: {name}
### B: {name}

## Chosen Approach
{Which and why}

## Architecture
{Components, data flow, interfaces. Design for isolation.}

## Tech Stack
{Languages, frameworks, key decisions. Short — it's a toy.}

## Open Questions
{Risks, unknowns, things to validate}

## Next Steps
{3-5 actions. First one doable today.}
```

### 7. Spec Self-Review

After writing the doc, review with fresh eyes:

1. **Placeholder scan:** Any "TBD", "TODO", incomplete sections? Fix them.
2. **Internal consistency:** Do sections contradict each other? Does architecture match features?
3. **Scope check:** Focused enough for a single implementation plan, or needs decomposition?
4. **Ambiguity check:** Could any requirement be interpreted two different ways? Pick one, make it explicit.

Fix issues inline.

### 8. User Review Gate

> "Design doc written to `{path}`. Please review and let me know if you want changes before we proceed."

Wait for user approval. If changes requested, revise and re-review.

### 9. Closing

- Summarize: "Draft at `{path}`. Toy version: {one sentence}."
- First action: "Start by: {specific task}."
- If the project has research potential: "This could feed into a research direction — run `/rp-generate` when ready to formalize."
- If ready for implementation: "Run `/plan` to create the implementation plan."

## Rules

- **No code.** Design docs only.
- **Questions one at a time.** Never batch.
- **Every project needs a toy version.** No exceptions.
- **Be direct.** Weak idea or useless toy — say so.
- **YAGNI ruthlessly.** Remove unnecessary features from all designs.
- **Design approved before implementation.** Hard gate — no exceptions.

## Anti-patterns

- **Skipping the toy** — jumping to the full vision without a working small version.
- **Toy needs the full version** — if it's not useful alone, rethink it.
- **Vague growth path** — "then we add more features" without specifying which or why.
- **Solution-first** — describing architecture before articulating the problem.
- **Over-engineering the toy** — the point is small. Ship, learn, iterate.
- **Skipping design for "simple" projects** — simple is where assumptions cause the most waste.

## Pushback patterns

| Signal | Response |
|--------|----------|
| Vague problem | "You're describing a category, not a project. What would you build this weekend?" |
| Solution-first | "You're telling me what to build, not why. What problem does this solve?" |
| Too big | "That's a 6-month project. What's the one-week version that still has value?" |
| No users | "If only you use it, is that enough? Sometimes yes — be honest about it." |
