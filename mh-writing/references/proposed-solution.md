# Proposed Solution

## Purpose

This section contains the definitive explanation of your novel technical approach. It is where the referee assesses the intellectual contribution of the paper — the ideas, the algorithm, the design. This must be clear, precise, and well-separated from both the problem description and the evaluation.

## Format

- Typically the longest technical section (2–4 pages).
- Use figures (architecture diagrams, algorithm pseudocode, workflow diagrams) to aid understanding.
- Subsections are appropriate for multi-part approaches.
- Algorithm listings should use standard pseudocode conventions, not implementation-specific syntax.

## Required Elements

- **High-level approach**: Start with an overview of the approach before diving into details. The reader should understand the big picture before the mechanics.
- **Technical details**: The algorithm, method, or design in enough detail that an expert could reimplement it.
- **Running example** (when helpful): A concrete example that illustrates the approach on a small input. This is especially valuable for complex algorithms.
- **Design decisions**: Explain key design choices and why alternatives were not chosen (when non-obvious).

## Common Pitfalls

- **Mixed with evaluation**: Do not discuss how you intend to evaluate in this section. "We evaluate on 12 projects..." belongs in the experimental setup, not here.
- **Mixed with problem description**: Do not re-describe the problem. Whether the problem is in the introduction or its own section, do not repeat it here.
- **Algorithm mixed with implementation**: Readers want to understand the ideas, algorithm, and overall approach. Implementation details (language, libraries, hardware) must be kept clearly separate. A paper that mixes implementation details with the high-level approach is hard to read and irritates referees. This is a common failing in early drafts.
- **No overview before details**: Jumping straight into notation and formulas without first explaining what the approach does at a high level. The referee needs a mental model before they can follow the details.

## Checklist

- [ ] High-level overview is given before diving into details
- [ ] Technical approach is described with enough detail for reimplementation
- [ ] No evaluation methodology is discussed in this section
- [ ] Problem is not re-described
- [ ] Algorithm and implementation details are clearly separated
- [ ] Figures or pseudocode are used where they aid understanding
- [ ] Key design decisions are justified
