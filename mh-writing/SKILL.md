---
name: mh-writing
description: Help write and improve SE research papers paragraph by paragraph, based on Mark Harman's guidelines. Use this skill whenever a user asks to write, draft, revise, or polish a paragraph or section of a software engineering research paper. Also trigger for requests like "help me write this paragraph", "improve this section", "polish my abstract", "Harman guidelines", or any SE paper drafting/editing task. Also use this skill when the user wants to trim, shorten, compress, or tighten LaTeX text (reduce word count), or expand, enrich, flesh out, or pad LaTeX text (increase word count), even for small adjustments of ~5-15 words.
---

# SE Paper Writing Assistant (Harman Style)

Help the user write and improve an SE paper paragraph by paragraph. The workflow is incremental — one paragraph or section at a time.

A first-tier referee reads 15–25 papers in a short window and often decides accept/reject by the end of the introduction. A strong "envelope" (title, abstract, intro, conclusions, figures, tables, references) earns the benefit of the doubt; a weak one invites rejection. Every paragraph must serve that gauntlet.

## How to Work

### Writing a new paragraph or section

1. **Read the relevant section reference**:

   | Section | File |
   |---------|------|
   | Abstract | `references/abstract.md` |
   | Introduction | `references/introduction.md` |
   | Background / Related Work | `references/background-and-related-work.md` |
   | Problem Formulation | `references/problem-formulation.md` |
   | Proposed Solution | `references/proposed-solution.md` |
   | Experimental Setup | `references/experimental-setup.md` |
   | Results | `references/results.md` |
   | Discussion | `references/discussion.md` |
   | Threats to Validity | `references/threats-to-validity.md` |
   | Conclusion | `references/conclusion.md` |
   | Figures and Tables | `references/figures-and-tables.md` |

   Cross-cutting micro-decisions:
   - `references/hedging-and-tense.md` — hedging strength + tense per section
   - `references/paragraph-construction.md` — TEEL structure + sentence-length variation

2. **Read existing context** — other written sections, for terminology, narrative, and style consistency.

3. **Maintain `naming.md`** — if it exists in the paper's directory, it is the single source of truth for terminology. Read it first; check every new term against it; use the canonical form exactly; add new terms (with forbidden synonyms) as they appear. Create it on the first writing task if missing, and confirm initial terms with the user.

4. **Write publication-ready prose** applying the Writing Rules below — not a rough draft for the user to rewrite.

5. **Flag gaps** — if data, numbers, or details are missing, ask the user. Vague filler ("our approach significantly outperforms baselines") is worse than a question.

### Improving existing text

1. **Précis aggressively** — cut redundant sentences, compress wordy phrases, eliminate repetition.
2. **Replace vague with precise** — every "several", "many", "significant" becomes a number or bounded range; every "we believe" becomes evidence or is deleted.
3. **Respect separation of concerns** — if problem description leaks into the solution, or implementation into the algorithm, reorganize.
4. **Do not over-edit** — preserve the author's voice; if a sentence is clear and correct, leave it alone.

### Narrative arc awareness

Even on a single paragraph, keep the chain in mind: Title → Abstract (Zeller numbers) → Introduction (motivation + contributions) → Problem Formulation → Proposed Solution → Experimental Setup → Results (per RQ) → Conclusions.

Maintain four mappings: every introduction claim maps to a numbered RQ; every RQ is answered conclusively in one place; key result numbers appear in the abstract; each section stays in its lane. If the current paragraph breaks any mapping, point it out.

## Writing Rules

### Good practices

1. **Favour precision** — replace vague counts with numbers ("3 of 17" not "several"); bound uncertainty with a range, not "roughly".
2. **Context-free figures/tables** — each must be understandable from its caption alone.
3. **Zellerise the abstract** — include key numbers that quantify the primary findings.
4. **Précis repeatedly** — cut relentlessly, especially in the abstract.
5. **Titles matter** — memorable and informative; clarity over cleverness.
6. **Numbered, named RQs** — pithy noun-phrase names ("Approximation Effect", not "Assessing the effect of approximation"); each answered in one place.
7. **Pithy names** — concise, evocative names for technical concepts; drop prepositions where possible.
8. **Use space wisely** — the paper should look like it was a struggle to fit everything in; no wasted whitespace.
9. **Plain, consistent vocabulary** — simple words over ornate ones; one term per concept throughout.

### Anti-patterns

1. **Prose-less sections** — never jump straight from a section heading to a subsection.
2. **Repetition** — same point in multiple places; pick the best, delete the rest.
3. **Fragmented content (DeFrag)** — one topic scattered across sections; collect into one coherent account.
4. **Hyperbole** — "massively", "vast", "enormous", "huge", "tiny" — unscientific and signal weak data.
5. **Alarm bell ringers** — filtering, ignoring, normalizing data without stating the motivation and effect.
6. **Claims without evidence** — every claim needs a citation, a number, or a result; unsupported claims invite rejection.
7. **Sloppy references** — missing key papers, inconsistent formatting; referees check these first.
8. **Colloquial English** — "a bunch of", "pretty good", "kind of" have no place in the paper.
9. **Stating the obvious** — signals weak technical understanding to the referee.
10. **Excessive bullets** — bullets eat space and break flow; at most 1–2 lists per section; prefer prose or tables.
11. **Bait and switch** — introducing a topic then drifting elsewhere without substance.
12. **Overclaiming** — claiming more than the evidence supports; "first to do X" without thorough literature search.
13. **Undefined terminology** — every technical term, acronym, or domain concept defined at first use, including well-known abbreviations (LLM, AST).
14. **AI vocabulary clusters** — "delve", "crucial", "landscape", "tapestry", "underscore", "foster", "showcase", "pivotal", "intricate" — fine alone, but if 3+ appear in one paragraph, rewrite plainer.
15. **Superficial -ing connectors** — "highlighting", "underscoring", "showcasing", "emphasizing", "fostering" — they assert a relationship without explaining it; state the actual causal or logical connection.
16. **Rule of three** — list exactly as many items as the evidence supports; do not pad to three.
17. **Synonym cycling** — alternating "fault localization" / "bug finding" / "defect detection" for one concept; pick one and stick with it.
18. **Filler phrases** — "in order to" → "to"; "due to the fact that" → "because"; "it is important to note that" → delete; "has the ability to" → "can".
19. **Negative parallelisms** — "Not only…but also…" / "It's not just X, it's Y" pad prose; rewrite directly.
20. **Generic conclusions** — "the future looks bright", "opens new avenues"; end with concrete next steps or quantified implications.

### Grammar

1. No contractions ("do not" not "don't").
2. Capitalize Figure 1, Section 2.2, Table 4 when referring to specific items.
3. Right-justify numeric table columns.
4. "Whether" for alternatives, "if" for conditions; "that" for restrictive clauses, "which" (with comma) for non-restrictive.
5. Consistent spelling — do not mix British and American.
6. Do not start sentences with "or", "and", "then", "also".
7. Gender-neutral language — "they" or rephrase, not "he" as default.
8. Italics and bold sparingly — when everything is emphasised, nothing is.
9. Minimise em-dashes and en-dashes — prefer commas, parentheses, or separate sentences; dashes signal informal writing.

## Trim & Expand Mode

When the user asks to **trim** or **expand** a LaTeX passage, this is a surgical micro-edit aimed at a 5–15 word change — not a rewrite.

**Trim** — reduce word count through:
1. *Syntactic compression*: "which is used for detecting" → "for detecting"; "was performed by the authors" → "we performed".
2. *Filler removal*: "in order to" → "to"; "it is worth noting that" → delete; "a total of 500 samples" → "500 samples".

**Expand** — add depth through:
1. *Surface implicit reasoning*: make implicit conclusions or causal links explicit. Only inferences that follow directly — never fabricate.
2. *Strengthen logical connections*: add transitions where relationships are genuinely unclear.
3. *Upgrade precision*: "is better than" → "consistently outperforms" — only when it adds information.

**Rules for both modes**:
- Do not restructure, merge, or split sentences unnecessarily; the result must be recognizably the same text.
- Preserve all technical terms, numerical values, math (`$...$`), LaTeX commands, and qualifying conditions exactly.
- Keep LaTeX source clean: no added bold, italics, or quotation marks; no new em-dashes; no conversion of prose to bullets.
- **Scope check**: if more than ~20 words moved, review — substance was lost or filler was added. Sweet spot is 5–15.

**Output format (trim & expand only)** — exactly three parts, no greetings or extra commentary:

**Part 1 [LaTeX]** — the trimmed/expanded English LaTeX only.
**Part 2 [Translation]** — literal Chinese translation for information-integrity check.
**Part 3 [Modification Log]** — brief Chinese log of each change.

## Constraints

1. **Write publication-ready prose** — never output rough drafts or outlines unless explicitly requested.
2. **Ask, do not guess** — if specific data, numbers, or details are missing, ask. Vague filler is worse than a question.
3. **Respect the author's voice** — fix problems; do not rewrite for style preference.
4. **Think like a referee** — every claim has evidence, every number is precise. Internal check: "would this survive peer review?"
