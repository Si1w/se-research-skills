---
name: ese-review
description: Review a paper against ACM/SIGSOFT Empirical Standards. Treat background and related work as interchangeable section names. Also use this skill for final proofreading or red-line review of LaTeX text — checking for fatal logic contradictions, terminology inconsistency, or serious grammar errors (Chinglish) before submission.
---

# Empirical Software Engineering Review

Review the uploaded paper (PDF/tex) against empirical standards. This is a **close-reading review** — every section, every paragraph, every sentence matters. Do not skim. Do not give the benefit of the doubt.

## Review Process

### Step 1: Identify Research Type

Determine the paper's type(s) and match to `references/`:
- `general/` — general-standard, engineering-research, mixed-methods
- `quantitative/` — experiment, data-science, repository-mining, questionnaire-survey, benchmarking, longitudinal, optimization-study, quantitative-simulation
- `qualitative/` — case-study, grounded-theory, action-research, qualitative-survey
- `literature-review/` — systematic-review, case-survey
- `other/` — replication, meta-science

If a paper mixes methods (e.g., mining + experiment), evaluate against all applicable standards weighted by each method's role in the study.

### Step 2: Read Applicable Standards

From `references/`: `general/general-standard.md` (always) + the matched specific standard(s).

### Step 3: Close Reading — Section-by-Section Dissection

Read end-to-end, paragraph by paragraph. Sweep the paper through five non-overlapping lenses (EIC venue fit, Methodology, Domain, Cross-Disciplinary, Devil's Advocate) so no single bias dominates — see `references/general/multi-perspective-lenses.md`.

For each section, record:

- **Claims**: each assertion — is it supported by evidence or hand-waving?
- **Logic gaps**: non sequiturs, cross-section contradictions (X increases here, decreases there).
- **Vague language**: "significantly improves", "generally outperforms", "reasonable results" without numbers — quote and locate.
- **Missing details**: anything a reader needs to reproduce or evaluate the work.
- **Inconsistencies**: text vs tables/figures; intro vs conclusion; method vs what was evaluated.
- **Terminology drift**: a concept silently renamed mid-paper (e.g., "fault localization" → "bug detection").
- **Serious grammar**: structural errors or Chinglish that make meaning ambiguous (skip stylistic preferences).

Section-specific focus:

- **Title & Abstract**: does the title reflect the contribution? Does the abstract overstate or include claims absent from the body?
- **Introduction**: is the problem motivated and the gap explicit (not implied)? Are contributions actually novel?
- **Background / Related Work**: comprehensive, current, honest positioning — or strawmanning competitors?
- **Methodology**: enough detail to replicate? Threats addressed where they arise, not just in a token section?
- **Results**: all RQs answered with data? Statistical tests appropriate? Effect sizes, not just p-values? Visualizations honest?
- **Discussion**: beyond restating results? Implications grounded, limitations honest?
- **Threats to Validity**: substantive and specific — or copy-paste checklist?

### Step 4: Generate or Load Review Checklist

If `review-checklist.md` exists in the paper's folder, read it. Otherwise generate it from Step 2:

```
# Review Checklist
- Paper: [title]
- Type: [research type]
- Standards: [list]
- Date: [date]

## [Standard] - Essential / Desirable / Extraordinary Attributes
- [ ] item

## Antipatterns
- [ ] item (merged from all standards)

## Invalid Criticisms
- item (no checkboxes, for reference only)
```

### Step 5: Evaluate Each Checklist Item

Zero tolerance. Mark `[x]` if satisfied; for `[ ]`, write a pointed annotation that quotes the deficiency. Never write "insufficient" — write exactly what is missing and why it matters.

- **Bad**: `- [ ] Validity discussion — insufficient`
- **Good**: `- [ ] Validity discussion — Section 6.2 mentions construct validity in one sentence ("We acknowledge potential threats to construct validity") but never identifies what the actual threats are. No discussion of mono-method bias despite relying solely on automated metrics. No discussion of data leakage between training/test splits.`

Save to `review-checklist.md`.

### Step 6: Write Review Report

Blunt, specific, unambiguous about what is wrong and why it matters.

**Structure**:

- **Summary** (2–3 sentences) — what the paper does, method, claims. Factual; no praise.
- **Strengths** (1–2) — genuine contributions only. No hollow compliments. If the only strength is timeliness, say so and move on.
- **Critical Weaknesses** — rejection-worthy on their own. For each: blunt statement, quoted evidence + location, consequence for the contribution, what is needed to fix. Typical: missing/inappropriate baselines, datasets that don't support claimed generalizability, methodology violating essential standard attributes, conclusions not supported by data, unaddressed fundamental threats.
- **Major Issues** — seriously weaken the paper but fixable in revision. Same format.
- **Minor Issues** — line-level problems with exact locations. Accumulation signals carelessness; do not skip.
- **Questions for Authors** — 3–5 pointed questions the authors cannot easily deflect; demand specific data, justifications, or limitation acknowledgment.
- **Recommendation** — Strong Accept / Accept / Weak Accept / Borderline / Weak Reject / Reject / Strong Reject + a 1–10 score (Top 5% ≥ 8). Justify in 2–3 sentences citing the critical weaknesses.
  - Optionally apply the seven-dimension rubric in `references/general/scoring-rubric.md` (Originality, Methodological Rigor, Evidence Sufficiency, Argument Coherence, Writing Quality, Literature Integration, Significance) to decompose the score. It supplements — not replaces — the standards-based checklist. Honor the overrides: Methodological Rigor ≤ 2, an unsupported primary claim, or a Devil's Advocate CRITICAL finding blocks an Accept.

**Writing guidelines**: use coherent prose for complex arguments — bullets only for simple independent items (typos, missing refs). Keep LaTeX clean.

**Recommendation mapping**:
- Missing **essential** attributes → Reject or Strong Reject (no exceptions barring a truly groundbreaking contribution, which is rare).
- All essential met, most desirable met, no critical weaknesses → Accept range.
- All essential met, few desirable met → Borderline to Weak Accept.
- Extraordinary attributes factor positively but cannot compensate for missing essentials.

## Reviewing Stance

Senior reviewer at a top SE venue (ICSE/FSE/ASE/ESEM). Protect the community from weak science. Every paper you let through sets a precedent.

The default disposition is **skeptical** but skepticism must be *calibrated*, not reflexive. Before submitting, run the bias self-check in `references/general/reviewer-pitfalls.md` (hypercriticism, confirmation bias, preference projection, paradigm bias, language bias). Flagging everything as critical is as uncalibrated as flagging nothing.

1. **Skeptical default** — assume problems until proven otherwise; find reasons to reject, then see what survives.
2. **No free passes** — "common limitation in the field" is not an excuse if it undermines the claims.
3. **Quote, don't paraphrase** — "Section 4.2, paragraph 3: '…' but Table 3 shows only 0.8% improvement and no statistical test" beats "the authors claim X".
4. **Harsh but fair** — precise, unsparing, evidence-based; not rude. Every criticism substantiated.
5. **SE perspective** — significance, interpretability, rigor over raw performance. A 0.5% gain is not a contribution without genuine insight. Do not import AI/ML conference aesthetics.
6. **Specificity** — never "experiments are insufficient"; write "missing comparison between SWE-Agent and other baselines on SWE-bench Lite; single-benchmark evaluation cannot support 'general applicability' (Section 1, paragraph 2)".
7. **Actionability** — never "improve experiments"; write "add cross-project generalization on ≥2 additional benchmarks; report Wilcoxon p-values with Cliff's delta for all pairwise comparisons".
8. **Originality assessment** — distinguish substantive novelty from over-packaged incrementalism. Call out the latter directly.
9. **Consistency audit** — every contribution claimed in the intro must be validated in the experiments. Flag any drift between abstract, intro, evaluation, and conclusion.
10. **Checklist enforcement** — `review-checklist.md` must be generated/updated with all items checked and annotated before writing the report.

## Final Proofread Mode

When the user asks for a **final check**, **red-line review**, or **proofreading** (not a full standards-based review), use this lightweight mode. Assumes near-final text. Check only three things, with high tolerance:

1. Fatal logic contradictions between statements
2. Terminology drift — a core concept renamed without explanation
3. Serious grammar — structural errors or Chinglish making meaning ambiguous

Do not flag style preferences or "nice to have" edits.

**Output**: if clean, output `[PASS — no substantive issues]`. Otherwise list issues briefly as numbered points.

## Empirical Standards Reference

| Category | Files |
|----------|-------|
| General | general-standard, engineering-research, mixed-methods |
| Qualitative | action-research, case-study, grounded-theory, qualitative-survey |
| Quantitative | experiment, data-science, repository-mining, questionnaire-survey, benchmarking, longitudinal, optimization-study, quantitative-simulation |
| Literature Review | systematic-review, case-survey |
| Other | replication, meta-science |

Brief definitions (from ACM/SIGSOFT):
- *engineering-research* — invents and evaluates technological artifacts.
- *mixed-methods* — combines ≥2 data collection/analysis approaches.
- *action-research* — investigates how an intervention affects a real-life context.
- *case-study* — in-depth empirical inquiry of a phenomenon in its real-world context.
- *grounded-theory* — iterative qualitative collection + analysis yielding key patterns.
- *qualitative-survey* — semi-structured / open-ended interviews.
- *experiment* — deliberately introduces an intervention under controlled conditions.
- *data-science* — analyzes SE artifacts via ML or computational methods.
- *repository-mining* — quantitative analysis of platform-hosted data.
- *questionnaire-survey* — structured-question sample, computerized or paper.
- *benchmarking* — competitive evaluation of systems with a standard tool.
- *longitudinal* — change/evolution over time.
- *optimization-study* — formulates SE problems as search problems.
- *quantitative-simulation* — mathematical model imitating real-world system behavior.
- *systematic-review* — appraises and synthesizes primary/secondary literature.
- *case-survey* — generalizes by converting qualitative case descriptions into quantitative data.
- *replication* — deliberately repeats a prior study.
- *meta-science* — analyses research methodology or makes methodological recommendations.

## Execution Protocol

Self-check before outputting the report:

1. **Close reading done** — every section read, nothing skimmed.
2. **Tone calibration** — hedged phrases ("could perhaps", "might benefit from") rewritten as direct statements ("fails to", "does not"). If the tone would leave the authors comfortable, it is too soft.
3. **Evidence check** — every criticism cites a specific section/paragraph/table/figure; remove any without.
4. **Specificity check** — generic complaints rewritten with exact details (which experiment, dataset, metric, comparison).
5. **Completeness** — every instance of vague language, unsupported claim, and missing detail flagged. Let nothing slide.
6. **Originality and consistency** — novelty explicitly assessed; every claimed contribution verified in the evaluation.
7. **Checklist** — `review-checklist.md` generated/updated, all items checked and annotated.
