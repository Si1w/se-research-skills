# Multi-Perspective Review Lenses

A close reading should sweep the paper from several non-overlapping angles before consolidating findings. Each lens asks different questions and surfaces different defects. The goal is not to write five separate reports — it is to make sure no single bias (your own methodological preference, your own domain background) dominates the review.

Use these lenses as a checklist during Step 3 (close reading). For each lens, note 1–3 specific findings with location and quoted evidence.

## Lens 1: Editor-in-Chief (Venue Fit)

What an EIC asks before reading the technical content:

- Does the paper fit this venue's scope? Is the contribution of interest to its readership?
- Is the topic timely, or has the field moved past it?
- Is the contribution incremental or substantive? Would acceptance set a useful precedent?
- Is the writing at a publishable standard, or would it need a major language pass?

This lens does NOT go deep into methodology — that is the next lens's job. It produces a one-paragraph editorial assessment.

## Lens 2: Methodology Reviewer

The most rigorous lens. What it asks:

- Is the research design appropriate for the question? (e.g., a controlled experiment for a causal claim, a case study for an exploratory question.)
- Is the sampling strategy justified? Are sample sizes adequate?
- Are statistical tests appropriate to the data? Are effect sizes reported, not just p-values?
- Are confounding variables identified and controlled or measured?
- Is the methodology reproducible from the description?
- Are construct, internal, external, and conclusion validity all addressed?

Output: a list of methodological defects, each with section reference and the exact gap.

## Lens 3: Domain Reviewer

What a specialist in the paper's subfield asks:

- Is the literature coverage complete? Are the most relevant baselines and prior work cited?
- Is the positioning against prior work honest, or does it strawman competitors?
- Are the technical claims correct on their merits? (e.g., is the algorithm actually novel given prior X?)
- Does the contribution advance the subfield, or repackage known techniques?

Output: missing references, mis-stated prior work, and an originality judgment grounded in the literature.

## Lens 4: Cross-Disciplinary / Perspective Reviewer

What a reader from an adjacent field asks:

- Does the work import ideas or methods from related fields where they would help?
- Are there practical or policy implications the authors missed?
- Are there assumptions taken for granted in this subfield that would not survive scrutiny from outside?
- Is the "so what" framing strong enough for a reader who is not already invested in this subfield?

Output: blind spots, opportunities, and a sharper framing of significance.

## Lens 5: Devil's Advocate

The most adversarial lens. The job is to find the strongest argument AGAINST the paper. What it asks:

- **Core claim challenge**: What is the single strongest counter-argument to the paper's main claim?
- **Cherry-picking**: Are the benchmarks, datasets, or examples selected to favour the proposed method? What was excluded and why?
- **Confirmation bias**: Did the authors look for evidence that would have refuted their claim, or only evidence that confirms it?
- **Logic chain validation**: Is each step from premise to conclusion sound? Where is the weakest link?
- **Overgeneralization**: Do the conclusions extend beyond what the evaluation supports?
- **Alternative paths**: Could a simpler baseline, a different metric, or a different framing reach the same or better result?
- **Stakeholder blind spots**: Whose perspective is missing from the analysis?
- **The "So what?" test**: If a busy senior researcher read the abstract and asked "So what?", does the paper answer that with anything more than "we built it and measured it"?

Output: 2–4 sharply-stated counter-arguments. Each must be substantive enough that the authors cannot easily deflect.

## How to combine the lenses

After the five sweeps, look for:

- **Consensus**: defects flagged by more than one lens are almost always critical weaknesses.
- **Disagreement**: e.g., the methodology lens says the design is sound but the devil's advocate says the benchmark is cherry-picked — note both and reason about which view dominates.
- **Critical issues**: any CRITICAL finding from the devil's advocate lens (e.g., a fatal logic error or unaddressable cherry-picking) blocks an Accept recommendation, even if the other lenses are positive.

The combined output feeds Step 5 (checklist evaluation) and Step 6 (report writing). Cite which lens surfaced each issue in your internal notes — it helps the user understand the angle of attack.
