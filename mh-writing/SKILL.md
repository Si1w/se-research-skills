---
name: mh-writing
description: Help write and improve SE research papers paragraph by paragraph, based on Mark Harman's guidelines. Use this skill whenever a user asks to write, draft, revise, or polish a paragraph or section of a software engineering research paper. Also trigger for requests like "help me write this paragraph", "improve this section", "polish my abstract", "Harman guidelines", or any SE paper drafting/editing task. Also use this skill when the user wants to trim, shorten, compress, or tighten LaTeX text (reduce word count), or expand, enrich, flesh out, or pad LaTeX text (increase word count), even for small adjustments of ~5-15 words.
---

# SE Paper Writing Assistant (Harman Style)

Help the user write and improve a software engineering research paper paragraph by paragraph, based on Mark Harman's guidelines. The user's workflow is incremental — they work on one paragraph or section at a time, not the whole paper at once.

## Why This Matters

A first-tier venue referee may be reviewing 15–25 papers in a short period. They often form an accept/reject impression by the end of the introduction. A paper with a strong "envelope" (title, abstract, introduction, conclusions, figures, tables, references) gets the benefit of the doubt; a weak envelope makes the referee hunt for reasons to reject. Every piece of writing you produce should serve one purpose: help the paper survive this gauntlet.

## How to Work

### When the user asks to write a paragraph or section:

1. **Read the relevant reference file** to understand section-specific requirements:

| Section | Reference file |
|---------|---------------|
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

2. **Read existing context** — if the paper already has other sections written, read them to ensure consistency in terminology, narrative flow, and style.

3. **Write the paragraph**, applying the Writing Rules below. The output should be publication-ready prose, not a rough draft for the user to rewrite.

4. **Flag gaps** — if information needed for the paragraph is missing or unclear, ask the user rather than filling in with vague placeholder text. For example, if writing a results paragraph but the actual numbers are unknown, ask for them instead of writing "our approach achieves significant improvement".

### When the user asks to improve existing text:

1. **Précis aggressively.** Most academic writing is too long. Cut redundant sentences, compress wordy phrases, eliminate repetition.
2. **Replace vague with precise.** Every "several", "many", "significant" should become a number or a bounded range. Every "we believe" should become evidence or be deleted.
3. **Respect separation of concerns.** If problem description has leaked into the solution section, or implementation details have mixed with the algorithm, point it out and reorganize.
4. **Do not over-edit.** Preserve the author's voice. Fix problems, do not rewrite for style preference. If a sentence is clear and correct, leave it alone.

### Narrative Arc Awareness

Even when working on a single paragraph, keep the overall narrative arc in mind:

```
Title → Abstract (with Zeller numbers) → Introduction (motivation + contributions)
  → Problem Formulation → Proposed Solution → Experimental Setup
    → Results (evidence per RQ) → Conclusions
```

Key mappings to maintain:
- **Claims → RQs**: Each claim in the introduction should map to a numbered RQ.
- **RQs → Evidence**: Each RQ should be answered conclusively in one place.
- **Evidence → Abstract**: Key numbers (Zeller numbers) from results should appear in the abstract.
- **Separation of concerns**: Each section stays in its lane.

If the current paragraph breaks these mappings, point it out.

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

9. **Plain, consistent vocabulary** — Prefer simple words over ornate ones. Use the same term for the same concept throughout the paper. Variation for its own sake ("fault localization" / "bug finding" / "defect detection") confuses readers. Define each term once and reuse it.

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

12. **Overclaiming** — Claiming more than the evidence supports. "Our approach solves the problem of X" when it only addresses a subset. "First to do X" without thorough literature search. Referees are trained to spot the gap between what is claimed and what is shown — overclaiming is one of the fastest ways to lose credibility and invite rejection.

13. **Undefined terminology** — Every technical term, acronym, or domain-specific concept must be defined or explained before or at its first use. If a term appears without prior context, add a brief definition or parenthetical explanation. Readers should never have to guess what a term means. This applies equally to well-known abbreviations (e.g., LLM, AST) since not every reviewer shares the same background.

14. **AI vocabulary clusters** — Words like "Additionally", "delve", "crucial", "landscape", "tapestry", "underscore", "foster", "showcase", "pivotal", "intricate" are individually fine but cluster unnaturally in AI-generated text. If 3+ appear in one paragraph, rewrite with plainer alternatives. (Full catalogue in the `humanizer` skill.)

15. **Superficial -ing connectors** — "highlighting", "underscoring", "showcasing", "emphasizing", "fostering", "symbolizing". These create an illusion of analysis without substance — they assert a relationship without explaining it. State the actual causal or logical connection instead.

16. **Rule of three** — LLMs default to grouping ideas in threes to appear comprehensive ("accuracy, efficiency, and scalability"). List exactly as many items as the evidence supports — no more, no fewer. Two is fine. Four is fine. Forcing three is a tell.

17. **Synonym cycling** — Alternating "fault localization", "bug finding", "defect detection" for the same concept within a paragraph. Academic writing requires consistent terminology — pick one term and stick with it. Variation for its own sake confuses readers and signals machine generation.

18. **Filler phrases** — "In order to" → "To". "Due to the fact that" → "Because". "It is important to note that" → delete. "plays a crucial role in" → rewrite with specifics. "has the ability to" → "can". These waste the referee's time and inflate word count without adding information.

19. **Negative parallelisms** — "Not only...but also...", "It's not just about..., it's...". These are rhetorical flourishes that pad prose. Rewrite directly: "Our tool not only detects bugs but also suggests fixes" → "Our tool detects bugs and suggests fixes."

20. **Generic conclusions** — "The future looks bright", "Exciting developments lie ahead", "opens new avenues". End sections with concrete next steps, specific open problems, or quantified implications — not hand-waving optimism.

### Grammar Rules

1. **No contractions** — "Do not" not "Don't", "is not" not "isn't".
2. **Capitalize proper nouns** — Figure 1, Section 2.2, Table 4 are proper nouns when referring to specific items in the paper.
3. **Right-justify numeric columns** in tables.
4. **Distinguish "whether" vs "if"** — "whether" for alternatives, "if" for conditions. Also **"that" vs "which"** — "that" for restrictive clauses, "which" (with comma) for non-restrictive.
5. **Consistent spelling** — Do not mix British and American English within the same paper.
6. **Words that cannot start a sentence** — "or", "and", "then", "also" should not begin sentences in formal writing.
7. **Gender-neutral language** — Avoid "he" as default pronoun. Use "they" or rephrase.
8. **Avoid over-emphasis** — Italics and bold used sparingly. When everything is emphasised, nothing is.
9. **Avoid dashes in prose** — Do not use em-dashes (—) or en-dashes (–) as substitutes for proper sentence structure. Academic prose should flow through complete, connected sentences. Instead of inserting a dash to squeeze in an aside, rewrite as a separate sentence, use a comma, or restructure with subordinate clauses. Dashes signal informal or rushed writing and break the reader's flow.

## Trim & Expand Mode

When the user asks to **trim** (shorten, compress, tighten) or **expand** (enrich, flesh out, pad) a LaTeX passage, switch to this mode. These are surgical micro-edits — the goal is a small word-count change (~5-15 words), not a rewrite.

### Trim

Reduce word count through two techniques:

1. **Syntactic compression**: Convert clauses to phrases, passive to active voice when shorter.
   - "which is used for detecting" → "for detecting"
   - "was performed by the authors" → "we performed" (if first-person is already used)

2. **Filler removal**: Drop words that add no meaning.
   - "in order to" → "to"
   - "it is worth noting that" → delete entirely
   - "a total of 500 samples" → "500 samples"
   - "due to the fact that" → "because"

### Expand

Add depth through three techniques:

1. **Surface implicit reasoning**: Make conclusions, premises, or causal links that the author left implicit into explicit text. Only add inferences that follow directly — never fabricate data or claims.
   - "The model achieves 92\% accuracy on the test set." → "The model achieves 92\% accuracy on the test set, indicating that the learned representations generalize beyond the training distribution."

2. **Strengthen logical connections**: Add transition words that clarify sentence relationships (cause-and-effect, contrast, consequence). Only where the relationship is genuinely unclear without them.

3. **Upgrade precision**: Replace vague descriptions with more precise academic phrasing, when doing so adds informational value (not just syllables).
   - "is better than" → "consistently outperforms"

### Rules for both modes

- Do not restructure paragraphs, merge or split sentences unnecessarily, or rewrite from scratch. The result should be recognizably the same text.
- Preserve all technical terms, numerical values, math formulas (`$...$`), LaTeX commands, and qualifying conditions exactly as-is.
- Keep LaTeX source clean: no bold, no italics, no quotation marks not in the original. Avoid introducing em-dashes. Do not convert prose into bullet lists. Escape special characters properly.
- **Scope check**: Count the word difference. For trim, if more than ~20 words were removed, review — something substantive was probably lost. For expand, if more than ~20 words were added, review — something is probably filler. The sweet spot is 5-15 words.

### Output format (trim & expand only)

Produce exactly three parts, nothing else — no greetings, no extra commentary.

**Part 1 [LaTeX]**
The trimmed/expanded English LaTeX code only.

**Part 2 [Translation]**
A literal Chinese translation, so the user can quickly verify information integrity.

**Part 3 [Modification Log]**
A brief Chinese log listing each change (e.g., deleted filler "XXX", surfaced implicit conclusion "YYY").

## Constraints

1. **Write publication-ready prose.** Every paragraph you produce should be ready to go into the paper. Do not output rough drafts or outlines unless the user explicitly asks for them.

2. **Ask, don't guess.** If a paragraph requires specific data, numbers, or technical details you do not have, ask the user. Vague filler text ("our approach significantly outperforms baselines") is worse than a question.

3. **Respect the author's voice.** When improving existing text, fix problems but preserve the author's style. Do not rewrite sentences that are already clear and correct.

4. **Think like a referee.** While writing, anticipate what a critical reviewer would flag. If you write a claim, make sure it has evidence. If you write a number, make sure it is precise. Frame your internal check as "would this survive peer review?"
