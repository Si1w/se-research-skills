# Results

## Purpose

This section presents the evidence gathered from the experiments and uses it to answer the research questions. It is where the paper delivers on the promises made in the introduction and abstract.

## Format

- Organise by research question: one subsection per RQ (or group of related RQs).
- Within each subsection, present evidence first, then interpretation.
- Typically 2 to 4 pages depending on the number of RQs.

## Required Elements

1. **Evidence presentation**: Tables, figures, and statistical results for each RQ. Present the data without judgement first; let the reader see the numbers.
2. **RQ answers**: After presenting the evidence, state clearly how it answers each RQ. This involves the authors' interpretation and judgement. Separate evidence from interpretation so the referee can form their own view before reading yours.
3. **Figure/Table to RQ mapping**: Aim for a 1:1 correspondence between figures/tables and the research questions they address. If one figure serves multiple RQs, or one RQ requires many figures, consider refactoring. Subsidiary questions may help (RQ1.1, RQ1.2, etc.).
4. **Zeller numbers**: The key quantitative findings that should also appear in the abstract. Identify these numbers explicitly.

## The RQ answer box: write at high altitude

Many papers close each RQ subsection with a highlighted box ("Answer to RQ1: ..."). This box is a synthesis, not a recap. It must read like the abstract's claim about that RQ, not like a second copy of the results table.

- **One or two sentences, a single takeaway**: state the general finding the reader should remember. If it needs three sentences and two clauses of caveats, it is not yet abstracted.
- **Lead with the claim, not the count**: write "Plugin and dependency declarations are where most build failures are actually fixed (67.96%)", not "We observed 67.96% in category A, 12% in category B, and 8% in category C". The box carries the conclusion; the surrounding prose and tables carry the breakdown.
- **At most one or two numbers**: include only the figure that anchors the takeaway. A box full of percentages is a data dump, not an answer.
- **Generalisable wording**: phrase the answer so it states what the study *found to be true*, not what this particular run logged. The reader should be able to quote the box as the paper's position on that question.
- **No new evidence in the box**: every number in the box must already appear in the preceding evidence; the box only interprets.

## Common Pitfalls

- **Evidence and interpretation mixed**: Presenting a number and immediately saying "this shows our approach is better" in the same sentence. Present data first, interpret second.
- **RQs answered in multiple scattered places**: Each RQ should be conclusively answered in one place. If the answer to RQ2 is partly in Section 5.1 and partly in Section 5.3, the referee has to hunt for it.
- **Missing statistical significance**: Reporting differences without statistical tests. "Our approach is 5% better" means nothing without knowing whether the difference is statistically significant.
- **Cherry-picked results**: Reporting only favourable outcomes without discussing cases where the approach does not work well. Referees are suspicious of uniformly positive results.
- **No connection back to claims**: The results should directly support (or refute) the claims made in the introduction. If a claim is not supported by the results, either remove the claim or add more experiments.
- **Data-dump answer box**: An "Answer to RQ" box that lists every percentage and category instead of stating the single high-level takeaway. The box is for the conclusion; the breakdown belongs in the surrounding prose and tables.

## Ideal Structure

```
Claims in introduction
  → map to top-level RQs
    → each answered conclusively in one place
      → with reference to a specific table/figure
        → Zeller numbers selected for the abstract
```

Aim for this ideal, then justify any deviations. Do not follow it slavishly if it harms clarity.

## Checklist

- [ ] Results are organised by RQ
- [ ] Evidence is presented before interpretation
- [ ] Each RQ is answered conclusively in one place
- [ ] RQ answer box is a one-to-two-sentence high-level claim, not a data dump
- [ ] Tables/figures have approximate 1:1 mapping with RQs
- [ ] Statistical significance is reported
- [ ] Negative or mixed results are discussed honestly
- [ ] Key Zeller numbers are identifiable
- [ ] Results connect back to claims in the introduction
