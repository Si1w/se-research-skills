# Hedging Strength and Tense Usage

A small reference for two recurring micro-decisions: how strongly to phrase a claim, and what tense to use in each section. Both are common defects in SE paper drafts.

## Hedging Strength

Match the verb to the evidence. Overhedging signals lack of confidence; underhedging invites the referee to challenge you.

| Strength | Devices | When to use | Example |
|----------|---------|-------------|---------|
| Weak | may, might, could, possibly, it is possible that | Causal claims from correlational data; generalizations beyond the sample; alternative explanations exist | "This may suggest a correlation between code complexity and defect density." |
| Moderate | suggests, indicates, appears, points to | Findings supported by data but needing replication; effects observed in one setting | "The data suggest that LLM-based fault localization outperforms spectrum-based methods on Java projects." |
| Strong | demonstrates, establishes, confirms, shows | Findings strongly supported by multiple lines of evidence; replicated results; controlled experiments | "The benchmark results demonstrate a 23% reduction in false positives under the proposed filter." |

### When NOT to hedge

- Reporting factual data: "The response rate was 78%." (not "appeared to be 78%")
- Describing methodology: "We used Wilcoxon signed-rank tests." (not "we attempted to use")
- Well-established prior work: "Spectrum-based fault localization computes suspiciousness scores from coverage." (no hedging needed)

### Anti-pattern: defensive hedging

Stacking hedges to avoid commitment ("may possibly suggest", "could potentially indicate") signals you do not know what your data shows. Pick one device or commit to the claim.

## Tense Usage by Section

A clean tense pattern reduces cognitive load for the referee. The convention in SE papers:

| Section | Tense | Example |
|---------|-------|---------|
| Abstract (findings) | Past or present perfect | "We evaluated X on 12 projects." / "We have shown that..." |
| Introduction (contributions) | Present | "This paper presents a new approach for..." |
| Related Work (reporting prior findings) | Past | "Zhang et al. (2023) found that..." |
| Related Work (ongoing state of art) | Present | "Spectrum-based methods rely on coverage data." |
| Problem Formulation | Present | "The task is to identify..." |
| Proposed Solution (algorithm description) | Present | "The algorithm computes a suspiciousness score for each statement." |
| Experimental Setup | Past | "Data were collected from 50 open-source projects." |
| Results (reporting) | Past | "Our approach achieved a Top-1 accuracy of 67%." |
| Results (what figures/tables show) | Present | "Figure 3 shows the distribution of suspiciousness scores." |
| Discussion (interpreting findings) | Present | "These results suggest that..." |
| Threats to Validity | Present | "A threat to external validity is..." |
| Conclusion (summary) | Present or past | "We have presented..." / "This paper presents..." |
| Conclusion (future work) | Future or present | "Future work will explore..." / "We plan to investigate..." |

### Common errors

- Mixing past and present within a single Results paragraph: "We found X. Our method achieves Y." → pick one register and stay there for the paragraph.
- Using present tense for one-time experimental procedures: "We use 12 projects" → "We used 12 projects" (the action is complete; reserve present for the algorithm or theory itself).
- Using past tense for what a figure shows: "Figure 3 showed..." → "Figure 3 shows..." (the figure is in front of the reader now).
