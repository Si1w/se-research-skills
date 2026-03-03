---
name: mh-writing
description: Review SE paper writing quality based on Mark Harman's guidelines
---

# SE Paper Writing Review (Harman Style)

Review the uploaded paper (PDF/tex) for writing quality based on Mark Harman's guidelines for SE research papers.

## Review Process

### Step 1: Read the Paper

Read the full paper and take note of its structure, prose style, and presentation.

### Step 2: Read Applicable Section References

Based on which sections the paper contains, read the corresponding files from `references/`:
- `references/abstract.md`
- `references/introduction.md`
- `references/background-and-related-work.md`
- `references/problem-formulation.md`
- `references/proposed-solution.md`
- `references/experimental-setup.md`
- `references/results.md`
- `references/threats-to-validity.md`
- `references/conclusion.md`
- `references/figures-and-tables.md`

### Step 3: Check Against Writing Rules

Evaluate the paper against the Patterns, Anti-Patterns, and Grammar Rules below, plus section-specific criteria from the references. For each item, note whether it is satisfied or violated with specific examples.

### Step 4: Write the Review Report

Write a writing review report containing:
- **Summary**: One-sentence assessment of overall writing quality.
- **Strengths**: Well-executed aspects of the writing.
- **Issues Found**: Categorized by severity (critical / minor), each with specific location and suggested fix.
- **Checklist Summary**: A pass/fail table of all rules checked.

### Step 5: Improve the Paper (Optional)

Base on the review report, make specific edits to the paper to improve its writing quality.

## Writing Rules

### Patterns (Good Practices)

1. **Favour precision** — Replace vague statements with numbers. "Several programs crashed" → "3 of 17 programs crashed". If uncertain, bound with a range instead of using "roughly".
2. **Context-free figures/tables** — Every figure, table, and boxout must be understandable from its caption alone, without reading surrounding text.
3. **Zellerise the abstract** — The abstract should contain key numbers that quantify the primary findings.
4. **Précis repeatedly** — Good writing is succinct. Cut relentlessly, especially in the abstract.
5. **Titles matter** — The title should be memorable and informative. Do not sacrifice clarity for cleverness.
6. **Numbered and named RQs** — RQs should be numbered, clearly answered in one place, and given pithy noun-phrase names (e.g. "Approximation Effect" not "Assessing the effect of approximation on our results").
7. **Pithy names** — Give concise, evocative names to technical concepts. Avoid cumbersome clauses. Drop prepositions where possible.
8. **Use space wisely** — The paper should look like it was a struggle to fit everything in (but not too much). No wasted white space.

### Anti-Patterns (Things to Avoid)

1. **Prose-less sections** — Sections that jump straight to a subsection with no introductory prose.
2. **Repetition** — Same point made in multiple places. Pick the best version, delete the rest. Good writing involves more deleting than inserting.
3. **Fragmented content (DeFrag)** — Technical information about one topic scattered across multiple sections. Collect into one coherent account.
4. **Hyperbole** — Words like "massively", "vast", "enormous", "huge", "tiny". These are inherently unscientific.
5. **Alarm bell ringers** — Statements about filtering data, ignoring results, or normalizing without explaining the motivation and effect.
6. **Claims without evidence** — Every claim needs evidence or a citation. Remove unsupported claims.
7. **Sloppy references** — Missing key papers, inconsistent formatting. Referees check references early.
8. **Colloquial English** — Informal language looks bad in scientific writing.
9. **Stating the obvious** — Signals low technical understanding to the referee.
10. **Excessive bullets** — Bullet points eat space and break flow. Use at most 1–2 lists, prefer enumeration, and consider tables/figures for longer lists.
11. **Bait and switch** — Introducing a topic then moving to something else without substance. A sign of rushed writing.

### Grammar Rules

1. **No contractions** — "Do not" not "Don't", "is not" not "isn't".
2. **Capitalize proper nouns** — Figure 1, Section 2.2, Table 4 are proper nouns.
3. **Right-justify numeric columns** in tables.
4. **Distinguish "whether" vs "if"** and **"that" vs "which"**.
5. **Consistent spelling** — Do not mix British and American English.
6. **Words that cannot start a sentence** — e.g. "or", "and", "then".
7. **Gender-neutral language** — Avoid "he" as default pronoun.
8. **Avoid over-emphasis** — Italics and bold used sparingly.

## Constraints

1. **Tone**: Constructive but direct. Point out specific violations with page/section references.
2. **Specificity**: Never say "writing needs improvement" — say "Section 3.2 uses 'enormous' and 'massive' (hyperbole), replace with measured quantities."
3. **Actionability**: Every issue should include a concrete suggestion for how to fix it.
