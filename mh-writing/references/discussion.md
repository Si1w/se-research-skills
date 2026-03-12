# Discussion

## Purpose

Discussion is the bridge between "what we found" and "what it means." Unlike Results (which objectively presents data) and Threats to Validity (which questions whether the data is trustworthy), Discussion interprets the findings, explains why they matter, and connects them to the broader research landscape. This is where the author earns the right to speculate, using phrases like "we conjecture" or "this seems to be due to," provided each speculation is clearly distinguished from evidence.

## Format

- Typically 1–2 pages.
- Each subsection should have a **bold title** that signals its topic. This helps referees quickly locate specific discussion points and gives the section visual structure. A wall of undifferentiated prose is hard to navigate.
- Organise by theme or by RQ, depending on which produces a more coherent narrative.

## Required Elements

- **Interpretation of results**: For each key finding, explain *why* the result looks the way it does. Do not repeat the numbers from Results. Instead, offer mechanistic explanations, connect to theory, or highlight surprising patterns.
- **Comparison with prior work**: Position your findings relative to existing literature. Where do they agree, contradict, or extend previous results? This demonstrates awareness of the field and helps the referee assess novelty.
- **Implications for researchers**: What new research directions does this work open? What should the community investigate next?
- **Implications for practitioners**: How can practitioners use these findings? Be specific and grounded in the evidence.
- **Cross-RQ synthesis** (when applicable): If the paper has multiple RQs, discuss how the findings across RQs relate to each other. Patterns that emerge only when combining RQs are often the most interesting insights.

## Subsection Formatting

Give each discussion point a short descriptive title using `\paragraph{}` or `\textbf{}`. Both are common at SE venues; `\paragraph{}` is preferred as it is a semantic heading command. This makes the section scannable so referees can quickly locate specific points.

**Example structure:**

```
\paragraph{LLM-based agents outperform rule-based baselines on complex tasks.}
Our results show that... This aligns with findings by Smith et al. [12], who...
However, unlike their work, we observe that...

\paragraph{Context window size is the dominant bottleneck.}
Across all configurations, we find that... This suggests practitioners should...

\paragraph{Implications for tool builders.}
Based on our findings, we recommend...
```

## Key References

The following classic SE methodology papers inform how Discussion sections should be written:

- **Ralph et al., ACM SIGSOFT Empirical Standards (2021)** — Essential: "discusses implications of the results." Desirable: "provides plausibly useful interpretations or recommendations for practice, education or research."
- **Shaw, "Writing Good SE Research Papers" (ICSE 2003)** — Discussion should show how the work responds to the "big question" posed in the Introduction. Distinguish observable evidence from author inference.
- **Wohlin et al., "Experimentation in Software Engineering" (2012)** — Result interpretation should tie back to experimental design and validity concerns.
- **Runeson & Höst, "Guidelines for Case Study Research in SE" (2009)** — Case studies need deeper contextual discussion; explain applicability within the studied context.
- **Stol & Fitzgerald, "Guidelines for Conducting SE Research"** — Explicitly separate Results (objective) from Discussion (subjective interpretation). Discussion may report interesting observations not directly tied to RQs.

## Common Pitfalls

- **Repeating Results**: Discussion should not restate findings. "As shown in Table 3, our approach achieves 85% accuracy" belongs in Results. Discussion explains *why* 85% and *what it means*.
- **All future work, no current implications**: Discussion should prioritise "what this means now" over "what we plan to do next." Future work belongs in Conclusion or a separate subsection.
- **Overclaiming**: Stating causal relationships when the study only shows correlation. "LLM agents cause fewer bugs" requires a controlled experiment; "LLM agents are associated with fewer bugs in our study" is honest.
- **Ignoring contradictory evidence**: If some results do not support the hypothesis, discuss them honestly. Referees notice when inconvenient findings are quietly omitted.
- **Speculation without labels**: Every conjecture should be explicitly marked as such. Unmarked speculation reads as an unsupported claim.
- **Disconnection from literature**: Discussing results in isolation without referencing related work. The referee wants to see how your findings fit into the existing body of knowledge.
- **Acknowledging limitations then ignoring them**: Ralph et al. flag this as a common anti-pattern: stating a limitation in Threats to Validity but then writing implications as though the limitation does not exist.

## Checklist

- [ ] Each key finding is interpreted (not just restated)
- [ ] Each subsection has a bold descriptive title
- [ ] Findings are compared with prior work (agreement, contradiction, extension)
- [ ] Implications for researchers are discussed
- [ ] Implications for practitioners are discussed
- [ ] Speculation is clearly distinguished from evidence
- [ ] Cross-RQ patterns are discussed (if multiple RQs)
- [ ] No overclaiming beyond what the evidence supports
- [ ] Limitations acknowledged in Threats to Validity are respected in the discussion