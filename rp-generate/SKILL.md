---
name: rp-generate
description: Propose a research project in software engineering or Agent-based systems
---

# Research Proposal

Help the user turn a vague research idea into a concrete, feasible project proposal through interactive dialogue, then output a structured document based on `reference/template.md`.

## Phase 1: Brainstorming

Start by understanding the user's rough idea. Ask targeted questions to progressively sharpen it — don't try to extract everything at once. A natural conversation flow matters more than a rigid interview.

Key things to uncover through dialogue:

1. **Core idea**: What problem are they trying to solve? What's the intuition behind their approach?
2. **Scope**: Is this a tool/framework, an empirical study, a benchmark, or something else?
3. **Target**: Who benefits from this work? Developers, researchers, practitioners?
4. **Feasibility signals**:
   - What data/resources are available or obtainable?
   - What's the expected timeline and effort?
   - Are there technical risks that could block progress?
   - Does the user (or their team) have the skills and infrastructure needed?

Throughout the conversation, actively push back on ideas that seem infeasible, overly broad, or underspecified. The goal is to help the user land on something they can actually execute — not just something that sounds impressive.

## Phase 2: Overlap Check

Before investing more effort, search for existing work that overlaps with the proposed idea. This is about avoiding wasted effort, not about novelty claims (that comes later when writing the paper).

1. Search arxiv, Google Scholar, or relevant venues (ICSE, FSE, ASE, ISSTA, MSR, etc.) for closely related work.
2. Report findings honestly:
   - If there's significant overlap: flag it clearly and discuss with the user whether to pivot, narrow the scope, or differentiate the approach.
   - If the space is relatively open: confirm this and move on.
   - If there's partial overlap: explain what's been done and what gap remains.

Do not skip this step — discovering a duplicate after months of work is costly.

## Phase 3: Structured Output

Once the idea is sufficiently clear and validated, read `reference/template.md` and produce a complete proposal document. Save it to the user's working directory.

Fill in each section with concrete content based on the brainstorming. Where information is still missing or ambiguous, insert a clearly marked `[TODO: ...]` placeholder explaining what needs to be resolved — do not fill gaps with vague generic text.

Section guidance:

- **TODO List**: Break the project into actionable tasks with rough ordering. Think about what can be parallelized and what blocks other work.
- **Introduction / Research Gap & Motivation**: Frame the problem from a practical angle — why does this matter to real developers or the SE community? Keep it grounded.
- **Key Contribution**: List 2-3 expected contributions. Be specific (e.g., "a dataset of X" or "a tool that does Y") rather than abstract ("insights into Z").
- **Background / Related Work**: Summarize the overlap check findings. Position the proposed work relative to what exists.
- **Problem Formulation**: Define the problem precisely. If there are research questions, state them. If it's a tool/system, define the input/output and success criteria.
- **Method**: Describe the proposed approach at a level where someone could start implementing it. Flag any parts that are still speculative.
- **Experiment Setup**: Design experiments that can actually be run with available resources. Specify datasets, baselines, metrics, and evaluation criteria. Be realistic about what's achievable.
- **Results**: Leave as `[TODO: to be filled after experiments]`.
- **Discussion**: Anticipate limitations and threats to validity. Identify what could go wrong and how to mitigate it.

## Constraints

- **Feasibility over ambition**: A doable project is worth more than a grand vision that never ships. When in doubt, suggest narrowing the scope rather than expanding it.
- **Be direct about weaknesses**: If part of the proposal is hand-wavy, say so. The user needs honest feedback before committing months of effort, not encouragement.
- **No filler**: Every section should contain substantive content or an explicit TODO. Generic statements like "this is an important area" without specific justification waste space.
