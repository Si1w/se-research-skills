---
name: brainstorming
description: Brainstorm, validate, and structure a research proposal in software engineering or Agent-based systems. Use whenever the user wants to develop a research idea, research direction, or research question — including vague hunches — or wants to check whether a planned study's design is rigorous and complete. Not for engineering project/feature planning (use project-draft for that).
---

# Research Proposal Brainstorming

Help the user develop a research idea into a well-reasoned proposal through rigorous, adversarial dialogue. The goal is not to find a publishable gap — it's to force deep thinking about whether a research direction is genuinely valuable, how to execute it well, and whether the planned study will hold up to the same empirical standards a reviewer will later apply.

## External Tools

### Python environment

Scripts in this skill use the shared Python environment at `~/.claude/skills/.venv/`, managed by `uv` with `~/.claude/skills/pyproject.toml`. Run scripts with:
```bash
uv run --project ~/.claude/skills python ~/.claude/skills/brainstorming/scripts/<script>.py
```

### Zotero

Search the user's paper library via `scripts/zotero.py`. Requires Zotero running with Better-BibTeX plugin.

```bash
uv run --project ~/.claude/skills python ~/.claude/skills/brainstorming/scripts/zotero.py search "<keywords>"
uv run --project ~/.claude/skills python ~/.claude/skills/brainstorming/scripts/zotero.py search "<keywords>" -c <collection>
uv run --project ~/.claude/skills python ~/.claude/skills/brainstorming/scripts/zotero.py get <citation-key>
uv run --project ~/.claude/skills python ~/.claude/skills/brainstorming/scripts/zotero.py collections
```

---

## Phase 1: Deep Problem Understanding

Don't rush it. One question at a time, follow the thread, challenge every vague claim.

**Must think through:**

1. **The problem, precisely.** Not "LLM-based code generation has limitations" — what specific limitation, in what context, causing what consequence? Push until the user can state the problem in one concrete sentence.

2. **Who is affected and how severely?** A problem that bothers everyone mildly is less compelling than one that blocks a specific group critically. Demand specifics — what kind of developers, in what scenario, how often, what's the cost?

3. **What exists today and why is it insufficient?** This isn't a literature gap — it's understanding why smart people haven't solved this yet. Maybe they tried and failed (why?). Maybe the problem wasn't visible until recently (what changed?). Maybe existing solutions work 80% of the time (is the remaining 20% worth a research effort?).

4. **Why is this the right time?** New data sources, new capabilities (LLMs, new tools), new scale of the problem, recent paradigm shifts. Research without timing is either too early (can't validate) or too late (already solved).

5. **What would a solution change?** Concrete before/after. If the research succeeds perfectly, what can people do that they couldn't before? If the answer is marginal, the research might not be worth the effort.

**How to push back:**

Don't be polite about weak thinking. The user wants to be challenged before they invest months, not after.

- When the problem is vague: "You're describing a general area, not a problem. What specifically breaks? Give me a concrete scenario."
- When the motivation is weak: "Suppose you solve this perfectly. What changes? If the answer is 'slightly better accuracy on a benchmark', is that worth 6 months?"
- When it's solution-first: "You're telling me what you want to build, not why it needs to exist. What happens if no one builds it?"
- When the scope is too broad: "This is three projects. Which one would you do if you could only pick one?"
- When novelty is confused with value: "No one has applied X to Y — but should they? What evidence suggests this combination would work?"

Do not proceed until the user can clearly answer: what is the problem, why does it matter, and why is now the right time.

---

## Phase 2: Validation

Before committing to execution, verify the idea holds up.

### Existing Work Analysis

The question is not "has this been done" but **"why hasn't this been solved satisfactorily?"**

Search in order:
1. **Zotero** — papers the user already collected are high-signal. Check notes for prior thinking.
2. **Local notes** — grep/search the user's existing markdown notes and past proposals for related thinking.
3. **External** — arxiv, Google Scholar, SE venues (ICSE, FSE, ASE, ISSTA, MSR).

Synthesize:
- Direct overlap → flag it, discuss differentiation or pivot
- Partial overlap → what remains unsolved, and is that remainder substantial?
- Open space → is it open because no one cares, because it's too hard, or because something recently changed?

### Feasibility Check

- Data: what's needed, what's available, what's the gap?
- Skills & infrastructure: does the user/team have what's needed?
- Timeline: realistic estimate, including unknowns
- Technical risks: what could fundamentally block this?

### Minimum Viable Experiment

The smallest test that validates the core assumption. Not the full evaluation — the one experiment that, if it fails, means the entire direction is wrong.

Push the user to define:
- What data, what metric, what threshold constitutes success
- What result would make them stop

### Research Design Completeness Check

Once the study shape is clear, pre-mortem it against the **same empirical standards a reviewer will later apply**. Catching a missing baseline or an unsupported generalizability claim now is cheap; catching it in review is a rejection.

1. **Classify the planned study type(s)** using the same taxonomy as the review standards (e.g., engineering-research, experiment, benchmarking, repository-mining, data-science, optimization-study, case-study, questionnaire-survey, systematic-review). A study often spans several — classify all that apply.

2. **Load the matching standard(s)** from the shared reference set at `~/.claude/skills/ese-review/references/`:
   - `general/general-standard.md` — always
   - `general/engineering-research.md` — for any study that builds and evaluates an artifact (most SE/Agent tool papers)
   - the specific standard(s) for the planned method (see the table below)

3. **Walk the essential attributes as design requirements, not a grading rubric.** For each essential attribute the standard demands, ask: *will the study as currently planned be able to satisfy it?* Surface the gaps now:
   - Baselines the design must include to support its claims
   - Datasets/benchmarks needed for the breadth the claims will assert (single-benchmark designs cannot back "general applicability")
   - Statistical plan — effect sizes and tests, not just p-values, planned before data collection
   - Threats to validity that must be designed against, not bolted on later
   - Reproducibility artifacts (data, code, prompts, seeds) the design should commit to producing

4. **Turn each gap into a proposal decision or an explicit TODO.** Either adjust the design to close the gap, or scope the claim down to what the design can actually support. Record the gap and the resolution in the proposal — don't let it stay implicit.

Be blunt: if the planned design cannot satisfy an essential attribute of its own method type, the claims must shrink or the design must change before writing a line of the proposal.

---

## Phase 3: Structured Output

Read `assets/template.md` for the template. Write the proposal as a single markdown file with the Write/Edit tools. Ask the user for the destination path; default to `<Project-Name>.md` in the current working directory. Maintain that one file as the thinking evolves.

**Writing rules:**
- Write for yourself. Be blunt, skip hedging, capture the reasoning process.
- Every sentence must carry information. No "X is an important area" without saying why.
- Missing information → `[TODO: specific question to resolve]`, not vague filler.
- Record why you chose this approach over alternatives. Future-you needs the reasoning, not just the decision.

---

## Anti-patterns

- **Gap-filling research**: "No one has done X" is not a motivation. The question is whether X is worth doing.
- **Solution-first thinking**: Describing a tool before articulating why it needs to exist.
- **Vague impact**: "Help developers" — which developers, doing what, how much better?
- **Scope creep**: "And we could also..." — is that core to the value, or distraction?
- **Feasibility blindness**: Grand vision without a realistic execution path.
- **Benchmark chasing**: Optimizing numbers on a leaderboard without asking if the benchmark measures something meaningful.
- **Claim/design mismatch**: Promising broad conclusions a design that's too narrow can't support. Run the Research Design Completeness Check and either widen the design or narrow the claim.
- **Deferring rigor**: "We'll add baselines/stats/threats later." If an essential attribute of the method isn't in the design now, the proposal is building on sand.

## Constraints

- **Depth over breadth.** Force the user to think deeply about one well-scoped problem rather than skim across a broad area.
- **Be brutally honest.** If the idea is weak, say so. Hard truths before committing months.
- **No filler.** Every section: substantive content or explicit TODO.

## Empirical Standards Reference

Shared with `ese-review` — read on demand from `~/.claude/skills/ese-review/references/`.

| Category | Files (under `references/`) |
|----------|------------------------------|
| General | `general/general-standard`, `general/engineering-research`, `general/mixed-methods` |
| Quantitative | `quantitative/experiment`, `data-science`, `repository-mining`, `questionnaire-survey`, `benchmarking`, `longitudinal`, `optimization-study`, `quantitative-simulation` |
| Qualitative | `qualitative/case-study`, `grounded-theory`, `action-research`, `qualitative-survey` |
| Literature Review | `literature-review/systematic-review`, `case-survey` |
| Other | `other/replication`, `meta-science` |
