# Paragraph Construction and Rhythm

Two micro-skills that show up across every section: how to build a paragraph, and how to vary sentence length.

## TEEL Paragraph Structure

A reliable default for any analytic paragraph (related work, discussion, threats to validity). Not a rigid template — but if a paragraph feels weak, check whether one of the four elements is missing.

- **T**opic sentence — states the paragraph's single claim in one sentence.
- **E**vidence — the data, citation, example, or quoted result that supports the claim.
- **E**xplanation — interprets the evidence, connects it to the claim, addresses why this matters.
- **L**ink — connects to the next paragraph, the section thesis, or the paper's overall argument.

### Example

> **[T]** Spectrum-based fault localization degrades when the test suite is small. **[E]** Pearson et al. (2017) report that Ochiai's mean reciprocal rank drops from 0.42 to 0.18 when the number of failing tests falls below five, across 357 real faults in Defects4J. **[E]** This is because the suspiciousness score relies on contrast between passing and failing executions — with few failing tests, the contrast is dominated by noise. **[L]** The next section introduces a learning-based filter that addresses this regime directly.

### Anti-patterns

- **Missing topic sentence**: paragraph opens with an example or citation and never states the claim. The reader has to reconstruct the point.
- **Missing explanation**: data dump — evidence with no interpretation. The reader has to do the analytic work themselves.
- **Missing link**: paragraphs sit as disconnected blocks. The reader cannot tell why this paragraph follows the previous one.
- **Buried claim**: topic sentence appears at the end of the paragraph. Acceptable rarely (for rhetorical effect), but if every paragraph does this, the section becomes hard to scan.

## Sentence Length Variation (Burstiness)

Good writing has natural variation. Short sentences create impact. Longer sentences develop complex ideas. The alternation creates rhythm.

### Detection rule

If 5+ consecutive sentences all fall within a narrow word-count range (e.g., all between 20 and 25 words), flag for review. The pattern reads as monotonous and is one of the strongest signals of LLM-generated text.

### How to fix

- Insert a short sentence (≤ 10 words) to break a run of long ones.
- Combine two short sentences into one complex one if the pattern is monotonously short.
- Read the paragraph aloud — if it feels metronomic, vary it.

### Variation targets by section

Different sections naturally tolerate different rhythms. Do not force variation where the genre prefers uniformity.

| Section | Variation | Why |
|---------|-----------|-----|
| Abstract | Moderate | Factual, steady pace. Each sentence carries one claim. |
| Introduction | High | Hook with short sentences, build with long ones. |
| Related Work | Moderate | Steady analytical pace, occasional short synthesis sentence. |
| Problem Formulation | Low | Definitional sentences naturally have similar shape. |
| Proposed Solution | Low to moderate | Procedural and algorithmic content tolerates uniformity. |
| Experimental Setup | Low | Procedural sections naturally have uniform length. |
| Results | Moderate | Short for key findings ("Our approach wins on 9 of 12 projects."), longer for detailed explanations. |
| Discussion | Highest | Short for emphasis, long for interpretation, very short for take-aways. |
| Threats to Validity | Moderate | Each threat is a self-contained mini-paragraph. |
| Conclusion | Moderate to high | Short for the punchline, longer for the bridge to future work. |

### Anti-pattern: uniform paragraph length

A related symptom is when every paragraph in a section is approximately the same length (e.g., all between 150 and 200 words). Natural writing varies — a 2-sentence paragraph after a 10-sentence paragraph creates rhythm and emphasizes the short one. If every paragraph in your Discussion section is the same size, the section reads as template-generated.
