---
name: mh-writing
description: Use when writing, drafting, revising, or polishing any part of a software engineering research paper, or when fixing awkward or Chinglish academic English.
---

# SE Paper Writing

## Writing Process

1. Create/Modify/Read `outline.md` until every part of the paper is clear.
2. Create/Modify/Read `terminology.md` that defines all technical terms.
3. Read the existing paper content.
4. Write a single paragraph. Follow the Patterns and avoid the Anti-Patterns.
5. Dispatch an isolated subagent to review the paragraph against the Review checklist below.

## Structure

Title → Abstract → Introduction → Background / Related Work → Problem Formulation → Proposed Solution → Experimental Setup → Results → Threats to Validity → Actionable Findings → Conclusion and Future Work.

## Paragraph Construction

Start every paragraph with its main claim (its conclusion), then justify it with evidence and explanation. Use the TEEL structure:

- **T**opic sentence: states the paragraph's single claim in one sentence.
- **E**vidence: the data, citation, example, or result that supports the claim.
- **E**xplanation: interprets the evidence and connects it to the claim.
- **L**ink: connects to the next paragraph or the section's argument.

## Patterns

The Patterns and Anti-Patterns apply to all text. Follow them while writing; the review step is a double-check.

- Favour precision: give exact numbers or a specific range.
- Context-free figures, tables and other boxouts: give enough context in each figure, table, or boxout and its caption to understand it alone.
- Précis, and précis again: keep the writing succinct.
- Succinct, pithy names: name technical terms briefly and define them in `terminology.md`.
- Space: use the page budget fully, with no wasted white space.
- Paragraph breaks over a page break: arrange paragraphs to end neatly at each column, and place headings at the top of a column where possible.
- Claims need evidence: back every claim with evidence or a citation.
- Use concise, simple, and direct language.

## Anti-Patterns

- Avoid prose-less sections.
- Avoid repetition.
- Avoid vague statements: define what is measured and give numbers. Write "3 of the 17 programs crashed", not "several programs crashed".
- DeFrag: collect scattered mentions of one topic into one coherent account under one heading.
- Avoid bait and switch: do not introduce a topic and then drop it without saying anything substantial.
- Avoid bullet lists: they waste space and signal lazy structure; prefer prose, a table, or at most a short enumeration.
- Explain alarm-bell interventions: when you filter, normalise, or exclude data, state what you did and explain its motivation and its effect on the results.
- Avoid hyperbole: no emotive intensifiers such as "massively", "vast", "huge", "tiny", or "slight".
- Avoid colloquial English.
- Avoid stating the obvious.
- Avoid contractions: write "do not", not "don't".
- Avoid em-dashes.
- Avoid complex multi-clause sentences: break them into simpler ones.

## References

### Section References

| Section | File |
|---------|------|
| Title | `references/title.md` |
| Abstract | `references/abstract.md` |
| Introduction | `references/introduction.md` |
| Background / Related Work | `references/background-and-related-work.md` |
| Problem Formulation | `references/problem-formulation.md` |
| Proposed Solution | `references/proposed-solution.md` |
| Experimental Setup | `references/experimental-setup.md` |
| Results | `references/results.md` |
| Threats to Validity | `references/threats-to-validity.md` |
| Actionable Findings | `references/actionable-findings.md` |
| Conclusion and Future Work | `references/conclusion.md` |
| Figures and Tables | `references/figures-and-tables.md` |
| Bibliography | `references/bibliography.md` |

### Templates

| Template | File |
|----------|------|
| Terminology | `templates/terminology-template.md` |
| Outline | `templates/outline-template.md` |

## Review

Double-check the paragraph:

- Does it follow the TEEL structure?
- Does it follow the Patterns and avoid the Anti-Patterns?
- Does it follow the corresponding section reference?
- Does it read smoothly and clearly?
