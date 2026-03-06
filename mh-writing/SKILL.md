---
name: mh-writing
description: Review SE paper writing quality based on Mark Harman's guidelines. Use this skill whenever a user asks to review, check, critique, or improve the writing of a software engineering research paper, an academic paper draft, or a conference/journal submission. Also trigger when the user mentions "writing review", "paper feedback", "Harman guidelines", "SE paper quality", or wants to polish a paper before submission. Even partial requests like "check my abstract" or "is my introduction good" should use this skill.
---

# SE Paper Writing Review (Harman Style)

Review a software engineering research paper for writing quality, structure, and presentation based on Mark Harman's guidelines. The goal is not just to find surface issues — it is to help the author tell a clear, compelling scientific story that a busy referee will want to accept.

## Why This Matters

A first-tier venue referee may be reviewing 15–25 papers in a short period. They often form an accept/reject impression by the end of the introduction. A paper with a strong "envelope" (title, abstract, introduction, conclusions, figures, tables, references) gets the benefit of the doubt; a weak envelope makes the referee hunt for reasons to reject. Every suggestion you make should serve one purpose: help the paper survive this gauntlet.

## Review Process

### Step 1: Read the Paper

Read the full paper. While reading, note:
- The overall narrative arc: what is the problem, why does it matter, what is the solution, what is the evidence?
- Whether the paper tells a coherent story from start to finish
- First impressions of prose quality, structure, and presentation

### Step 2: Check the Narrative Arc

This is the most important check. A well-written SE paper has a traceable thread:

```
Title → Abstract (with Zeller numbers) → Introduction (motivation + contributions)
  → Problem Formulation → Proposed Solution → Experimental Setup
    → Results (evidence per RQ) → Conclusions
```

Verify these mappings:
1. **Claims → RQs**: Each claim in the introduction should map to a numbered RQ.
2. **RQs → Evidence**: Each RQ should be answered conclusively in one place, supported by a specific table or figure.
3. **Evidence → Abstract**: The key numbers (Zeller numbers) from the results should appear in the abstract.
4. **Separation of concerns**: Problem formulation, proposed solution, experimental setup, and results should each stay in their lane. A paper that mixes "what we did" with "how we evaluated" with "what we found" confuses the referee.

If the narrative arc is broken — claims without matching RQs, RQs answered in multiple scattered places, results missing from the abstract — flag this as a critical issue. Everything else is secondary.

### Step 3: Read Applicable Section References

Based on which sections the paper contains, read the corresponding reference files for section-specific criteria. Each reference file follows a consistent structure: Purpose, Format, Required Elements, Common Pitfalls, and Checklist.

| Section | Reference file |
|---------|---------------|
| Abstract | `references/abstract.md` |
| Introduction | `references/introduction.md` |
| Background / Related Work | `references/background-and-related-work.md` |
| Problem Formulation | `references/problem-formulation.md` |
| Proposed Solution | `references/proposed-solution.md` |
| Experimental Setup | `references/experimental-setup.md` |
| Results | `references/results.md` |
| Threats to Validity | `references/threats-to-validity.md` |
| Conclusion | `references/conclusion.md` |
| Figures and Tables | `references/figures-and-tables.md` |

### Step 4: Check Against Writing Rules

Evaluate the paper against the Patterns, Anti-Patterns, and Grammar Rules below, plus the section-specific criteria from the reference files. For each violation, note the specific location (section, paragraph, or sentence) and why it matters.

Focus your attention proportionally: a broken narrative arc or missing evidence for claims matters far more than a minor grammar issue. Do not bury critical structural problems under a long list of nitpicks.

### Step 5: Write the Review Report

Structure the report as follows:

**1. Overall Assessment** (2-3 sentences)
State the paper's overall writing quality and the single most important thing the author should fix. Be direct.

**2. Narrative Arc Check**
- Is the story coherent from title to conclusion?
- Do claims map to RQs? Do RQs map to evidence?
- Are Zeller numbers in the abstract?
- Rate: Strong / Adequate / Broken

**3. Section-by-Section Findings**
For each section of the paper, list issues found. For each issue:
- **What**: Which rule is violated (reference by name, e.g., "Hyperbole", "Prose-less section")
- **Where**: Specific location (e.g., "Section 3.2, paragraph 2", or quote the problematic text)
- **Why it matters**: Why this hurts the paper (connects to referee psychology)
- **Suggested fix**: A concrete, actionable suggestion

Group issues by severity within each section:
- **Critical**: Would cause a referee to lower their score (broken narrative, unsupported claims, missing evidence, severe separation-of-concerns violations)
- **Minor**: Worth fixing but unlikely to cause rejection alone (grammar, formatting, mild hyperbole)

**4. Strengths**
Highlight what the paper does well. Positive feedback helps the author know what to preserve during revision.

**5. Priority Checklist**
A compact table summarizing all rules checked:

| Rule | Status | Location |
|------|--------|----------|
| Narrative arc coherent | Pass/Fail | — |
| Abstract has Zeller numbers | Pass/Fail | Abstract |
| ... | ... | ... |

### Step 6: Improve the Paper (Optional)

If the user asks for revisions (or if the review reveals issues that benefit from concrete rewrites), apply edits guided by these principles:

1. **Fix critical issues first.** Start with narrative arc problems — if claims do not map to RQs, or RQs are not answered, restructuring is needed before prose polish.

2. **Précis aggressively.** Most academic writing is too long. Cut redundant sentences, compress wordy phrases, and eliminate repetition across sections. When two sections say the same thing, keep the better version and delete the other.

3. **Replace vague with precise.** Every "several", "many", "significant" should become a number or a bounded range. Every "we believe" should become evidence or be deleted.

4. **Respect separation of concerns.** If problem description has leaked into the solution section, or implementation details have mixed with the algorithm, reorganize. Use the DeFrag principle: collect scattered information about one topic into one place.

5. **Strengthen the envelope.** The title, abstract, introduction, and conclusions are what the referee sees first and remembers last. Invest disproportionate effort here. Make the contribution statement tight and compelling. Ensure the abstract answers the four questions (problem, importance, solution, evidence).

6. **Do not over-edit.** Preserve the author's voice. Fix problems, do not rewrite for style preference. If a sentence is clear and correct, leave it alone.

## Writing Rules

### Patterns (Good Practices)

1. **Favour precision** — Replace vague statements with numbers. "Several programs crashed" → "3 of 17 programs crashed". If uncertain, bound with a range instead of using "roughly". Precision signals scientific rigour to the referee.

2. **Context-free figures/tables** — Every figure, table, and boxout must be understandable from its caption alone. Referees often flick through figures before reading the paper — this is their first impression of your results.

3. **Zellerise the abstract** — The abstract should contain key numbers that quantify the primary findings. These numbers are what the referee (and later, readers scanning proceedings) use to judge whether the results are meaningful.

4. **Précis repeatedly** — Good writing is succinct. Cut relentlessly, especially in the abstract. Like programming: get it right first, then optimise to make it tight and fast.

5. **Titles matter** — The title should be memorable and informative. Do not sacrifice clarity for cleverness. The title is the first thing anyone reads and often the only thing — it must work on its own.

6. **Numbered and named RQs** — RQs should be numbered, clearly answered in one place, and given pithy noun-phrase names (e.g., "Approximation Effect" not "Assessing the effect of approximation on our results"). This helps referees navigate the paper and verify that each question is actually answered.

7. **Pithy names** — Give concise, evocative names to technical concepts. Avoid cumbersome clauses. Drop prepositions where possible. Good names make the paper easier to discuss and remember.

8. **Use space wisely** — The paper should look like it was a struggle to fit everything in (but not cramped). No wasted white space. A paper with generous whitespace signals that the authors did not have enough to say.

### Anti-Patterns (Things to Avoid)

1. **Prose-less sections** — Sections that jump straight to a subsection with no introductory prose. This is jarring and signals that the author has not thought about the narrative flow between sections.

2. **Repetition** — Same point made in multiple places. Pick the best version, delete the rest. Good writing involves more deleting than inserting. Repetition wastes the referee's limited reading time.

3. **Fragmented content (DeFrag)** — Technical information about one topic scattered across multiple sections. Collect into one coherent account. A referee should not have to flip between sections to understand one concept.

4. **Hyperbole** — Words like "massively", "vast", "enormous", "huge", "tiny". These are inherently unscientific. They signal that the author does not have precise data, or worse, is trying to inflate weak results.

5. **Alarm bell ringers** — Statements about filtering data, ignoring results, or normalizing without explaining the motivation and effect. These make referees suspicious that the methodology is unsound.

6. **Claims without evidence** — Every claim needs evidence or a citation. Remove unsupported claims. An unsupported claim is worse than no claim — it suggests the author does not understand the burden of proof.

7. **Sloppy references** — Missing key papers, inconsistent formatting. Referees check references early — it is a quick way to assess whether the authors know their field.

8. **Colloquial English** — Informal language looks bad in scientific writing. "A bunch of", "pretty good", "kind of" have no place in a research paper.

9. **Stating the obvious** — Signals low technical understanding to the referee. If something is obvious to the target audience, do not state it.

10. **Excessive bullets** — Bullet points eat space and break flow. Use at most 1–2 lists, prefer enumeration, and consider tables/figures for longer lists. A paper that reads like a slide deck will not impress.

11. **Bait and switch** — Introducing a topic then moving to something else without substance. A sign of rushed writing that irritates referees.

### Grammar Rules

1. **No contractions** — "Do not" not "Don't", "is not" not "isn't".
2. **Capitalize proper nouns** — Figure 1, Section 2.2, Table 4 are proper nouns when referring to specific items in the paper.
3. **Right-justify numeric columns** in tables.
4. **Distinguish "whether" vs "if"** — "whether" for alternatives, "if" for conditions. Also **"that" vs "which"** — "that" for restrictive clauses, "which" (with comma) for non-restrictive.
5. **Consistent spelling** — Do not mix British and American English within the same paper.
6. **Words that cannot start a sentence** — "or", "and", "then", "also" should not begin sentences in formal writing.
7. **Gender-neutral language** — Avoid "he" as default pronoun. Use "they" or rephrase.
8. **Avoid over-emphasis** — Italics and bold used sparingly. When everything is emphasised, nothing is.

## Constraints

1. **Be a story editor, not just a copy editor.** The most valuable feedback is about the paper's narrative coherence — whether the story flows logically from problem to solution to evidence. Surface-level grammar fixes are easy; structural guidance is what the author actually needs.

2. **Be specific, always.** Never say "writing needs improvement" — say "Section 3.2, paragraph 2 uses 'enormous' and 'massive' (hyperbole anti-pattern); replace with the measured quantities from Table 3." Every issue needs a location and a fix.

3. **Be constructive but direct.** Do not soften critical feedback to the point of vagueness. The author needs to know what will get their paper rejected. Frame feedback as "here is what the referee will think" to motivate action.

4. **Prioritise ruthlessly.** A review that lists 50 issues with equal weight is not useful. Lead with the 3-5 things that matter most for acceptance. A referee who sees a broken narrative arc will not care about comma placement.

5. **Respect the author's intent.** The goal is to help the paper succeed, not to rewrite it in your preferred style. Fix problems, suggest improvements, but preserve the author's voice and research contribution.
