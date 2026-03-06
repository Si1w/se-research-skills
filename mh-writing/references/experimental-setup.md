# Experimental Setup

## Purpose

This section explains how you propose to demonstrate that your solution addresses the problem. It is the bridge between "here is what we built" and "here is what happened when we tested it." A well-written experimental setup lets the referee assess your methodology before seeing the results.

## Format

- Typically 1–2 pages.
- Often structured around research questions (RQs), with subsections for subjects, metrics, and procedure.
- RQs should be numbered, named with pithy noun-phrases, and motivated.

## Required Elements

- **Research Questions**: Numbered and named RQs that the experiments will answer. Each RQ needs a brief motivation — why is this question worth asking?
- **Subjects / Benchmarks**: What datasets, programs, or subjects you chose to evaluate on, and why. The selection criteria matter: if you chose 12 Java projects, explain why these 12 and not others.
- **Metrics and measurements**: What you measured and how. Statistical tests applied, significance thresholds, effect size measures.
- **Baselines**: What you compare against and why these baselines are appropriate.
- **Procedure**: How the experiments were conducted (replication count, environment, configuration).

## Common Pitfalls

- **Polluted with results**: Do not include any results in this section. "Our approach achieved 85% accuracy" is a result, not setup. This is the most common separation-of-concerns violation in SE papers.
- **Polluted with solution details**: Do not re-describe the approach here. If the reader needs a refresher, point them back to the solution section.
- **Unnamed or unnumbered RQs**: RQs without numbers are hard to reference. RQs without pithy names are hard to remember. "RQ1: Approximation Effect" is better than "RQ1: Does the use of approximation techniques lead to different results in terms of the overall accuracy of our approach?"
- **Missing motivation for RQs**: Each RQ should explain why the question matters, not just state it.
- **Unclear subject selection**: If the referee suspects cherry-picking, the paper is in trouble.

## Sanity Check

Ask: could you write this same experimental setup section about someone else's proposed solution to the same problem, without knowing anything about their results? If yes, the separation of concerns is right. If no, results or solution details have leaked in.

## Checklist

- [ ] RQs are numbered and have pithy names
- [ ] Each RQ is motivated (why ask this question?)
- [ ] Subjects/benchmarks are described with selection criteria
- [ ] Metrics, statistical tests, and significance thresholds are specified
- [ ] Baselines are identified and justified
- [ ] Experimental procedure is described (replication, environment)
- [ ] No results are presented in this section
- [ ] No solution details are re-described
