---
name: ese-review
description: Review a paper against ACM/SIGSOFT Empirical Standards
---

# Empirical Software Engineering Review

Review the uploaded paper (PDF/tex) against empirical standards.

## Review Process

### Step 1: Identify Research Type

Based on the [Empirical Standards Reference](#empirical-standards-reference), determine the paper's research type. Match against `references/`:
- `general/` — general-standard, engineering-research, mixed-methods
- `quantitative/` — experiment, data-science, repository-mining, questionnaire-survey, benchmarking, longitudinal, optimization-study, quantitative-simulation
- `qualitative/` — case-study, grounded-theory, action-research, qualitative-survey
- `literature-review/` — systematic-review, case-survey
- `other/` — replication, meta-science

A paper may use multiple research methods (e.g., mining repositories then running a controlled experiment). Identify all applicable types and read the corresponding standards for each — evaluate the paper against all of them based on the weight each method carries in the study.

### Step 2: Read Applicable Standards

Read from `references/`:
1. `general/general-standard.md` (always required)
2. The matched specific standard file(s) — if the paper spans multiple types, read each one

### Step 3: Generate or Load Review Checklist

If `review-checklist.md` exists in the paper's folder, read it. Otherwise, generate it from the standards in Step 2:

```
# Review Checklist
- Paper: [title]
- Type: [research type]
- Standards: [list]
- Date: [date]

## [Standard] - Essential Attributes
- [ ] item

## [Standard] - Desirable Attributes
- [ ] item

## [Standard] - Extraordinary Attributes
- [ ] item

## Antipatterns
- [ ] item (merged from all standards)

## Invalid Criticisms
- item (no checkboxes, for reference only)
```

### Step 4: Evaluate Each Item

Check each item against the paper. Mark satisfied `[x]`, keep unsatisfied `[ ]` with annotation (e.g. `- [ ] ... — **Feature engineering steps not described**`). Save to `review-checklist.md`.

### Step 5: Write Review Report

Based on Step 4 results, write a review report containing:
- **Summary**: One-sentence core summary.
- **Strengths**: 1–2 genuinely valuable contributions.
- **Weaknesses (Critical)**: 3–5 fatal issues that could lead to rejection (e.g. missing baselines, insufficient dataset representativeness, superficial validity discussion, methodology not meeting empirical standards).
- **Minor Issues**: 2–3 non-fatal issues affecting quality (e.g. poor chart readability, incomplete background/related work, unclear writing).
- **Questions for Authors**: 2–3 key questions the authors must answer in rebuttal.
- **Recommendation**: One of: Strong Accept / Accept / Weak Accept / Borderline / Weak Reject / Reject / Strong Reject, with a one-sentence justification.

How checklist results map to the recommendation:
- Missing **essential** attributes → typically Reject or Weak Reject, unless the contribution is exceptionally strong in other dimensions.
- All essential met, most desirable met → Accept range.
- All essential met, few desirable met → Borderline to Weak Accept.
- Any extraordinary attributes met → factor positively into the recommendation.

## Constraints

1. **Tone**: Professional, critical, strict.
  - Presume rejection unless strengths are compelling.
  - Skip superficial praise — focus on fatal flaws.

2. **Dimensions**:
  - **Validity** — sound methodology, well-defined RQs, conclusions supported by data
  - **Novelty** — new insights or methods, differentiated from prior work
  - **Significance** — important problem, meaningful impact
  - **Clarity** — well-written, well-organized, easy to follow
  - **Reproducibility** — data availability, replication package, open science practices (code, scripts, raw results). Absence is not fatal but should be noted as a weakness, especially for empirical studies where independent verification matters.

## Empirical Standards Reference

### General

| File | Summary |
|------|---------|
| general-standard | |
| engineering-research | Research that invents and evaluates technological artifacts |
| mixed-methods | Studies that use two or more approaches to data collection or analysis to corroborate, complement and expand research findings (multi-methodology) or combine and integrate inductive research with deductive research (mixed methods) |

### Qualitative

| File | Summary |
|------|---------|
| action-research | Empirical research that investigates how an intervention, like the introduction of a method or tool, affects a real-life context |
| case-study | An empirical inquiry that investigates a contemporary phenomenon in depth and within its real-world context |
| grounded-theory | A study that involves iterative and interleaved rounds of qualitative data collection and analysis, leading to key patterns |
| qualitative-survey | Research comprising semi-structured or open-ended interviews |

### Quantitative

| File | Summary |
|------|---------|
| benchmarking | A study in which a software system is assessed using a standard tool for competitively evaluating and comparing methods, techniques or systems |
| repository-mining | A study that quantitatively analyzes a dataset extracted from a platform hosting structured or semi-structured text |
| optimization-study | Research studies that focus on the formulation of SE problems as search problems, and apply optimization techniques to solve such problems |
| data-science | Studies that analyze SE phenomena or artifacts using data-centric analysis methods such as machine learning or other computational intelligence approaches |
| quantitative-simulation | A study that involves developing and using a mathematical model that imitates a real-world system's behavior |
| longitudinal | A study focusing on the changes in and evolution of a phenomenon over time |
| experiment | A study in which an intervention is deliberately introduced to observe its effects on some aspects of reality under controlled conditions |
| questionnaire-survey | A study in which a sample of respondents answer a series of (mostly structured) questions, typically through a computerized or paper form |

### Literature Review

| File | Summary |
|------|---------|
| case-survey | A study that aims to generalize results about a complex phenomenon by systematically converting qualitative descriptions in published case studies into quantitative data |
| systematic-review | A study that appraises, analyses, and synthesizes primary or secondary literature to provide a complete, exhaustive summary of current evidence |

### Other

| File | Summary |
|------|---------|
| meta-science | A paper that analyses an issue of research methodology or makes recommendations for conducting research |
| replication | A study that deliberately repeats a previous study to determine whether its results can be reproduced |

## Execution Protocol
Before outputting, self-check:
1. **SE perspective**: Review as an ICSE/FSE/ASE reviewer. The SE community values problem significance, method interpretability, experiment systematicness over raw performance gains. Do not apply AI/ML aesthetics.
2. **Tone calibration**: If tone feels too gentle, re-examine ambiguous results and raise pointed challenges.
3. **Specificity**: Never say "experiments are insufficient" — say "missing comparison between SWE-Agent and other baselines." Never say "threats to validity is insufficient" — say "no discussion of potential data leakage between training and test sets."
4. **Actionability**: Never say "need to improve experiments" — say "add cross-project generalization experiments and report Wilcoxon test p-values with Cliff's delta effect sizes."
5. **Checklist**: Ensure `review-checklist.md` has been generated/updated with all items checked and annotated.