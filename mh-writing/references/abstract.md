# Abstract

## Purpose

The abstract is the paper's elevator pitch. Most readers (and many referees) decide whether to read further based on the abstract alone. It must convey the core contribution and evidence in minimal space.

## Format

- Single paragraph. No line breaks, no subsections.
- No references or citations.
- No forward references to sections, figures, or tables.
- Typically 150 to 250 words (check venue guidelines).

## Altitude: write at a high level of abstraction

The abstract is the most abstract part of the paper. Every sentence should be a high-level synthesis that an informed reader could not have written without having done the work, not a transcription of what the experiment logged. Aim for claims, not data dumps.

- **Synthesise, do not report**: state what the numbers *mean*, then attach the number as support. Write "most build issues are resolved by editing plugin and dependency declarations (67.96%)", not "we counted 67.96% of issues in the plugin-and-dependency category".
- **Lead with the conceptual move**: name the problem, the reframing, and the contribution before any measurement. A reader should grasp the idea even if every number were deleted.
- **One claim per sentence, each generalisable**: prefer sentences that survive outside this paper's exact dataset ("build failures span a wide spectrum of symptoms") over sentences that only describe this run's bookkeeping.
- **Numbers are evidence, not the story**: include the few numbers that quantify the *primary* findings (Zellerise), but the narrative is carried by the high-level claims those numbers support, not by an enumeration of counts.

## When an abstract has no numbers

Not every strong abstract reports quantitative results. Vision, roadmap, manifesto, and methodology papers legitimately contain no measurements; their contribution is a new framing, an argument, or a research agenda. For these, the "evidence" is the coherence and novelty of the conceptual structure, and the abstraction level must be even higher. Do not force artificial numbers into such an abstract. For empirical and systems papers, however, a missing Zeller number is a real flaw.

To decide which case applies: empirical and systems papers are measurement-driven (new algorithms, tools, systems, bug or code studies, user studies), and their primary findings are quantitative, so the abstract must carry those numbers. Vision and roadmap papers propose a conceptual structure or agenda without measurement. If a paper has both a novel framing and some measurements, treat it as empirical and Zellerise. If in doubt, apply the empirical standard.

## Required Elements

The abstract must answer four questions, in this order:

1. **What is the problem?** State the problem concisely.
2. **Why does it matter?** Motivate why anyone should care (practical impact, scale of the issue, gap in knowledge).
3. **What is your solution?** Describe your approach in one or two sentences, at the level of the idea, not the implementation.
4. **What evidence do you offer?** For empirical and systems work, Zellerise: weave the few key numbers that quantify the primary findings into the high-level claims. For vision and roadmap work, state the agenda and why the framing is the right one.

## Exemplars

These two top-venue abstracts show the two registers. Study how each sentence operates at the level of a claim, not a data report.

**Vision / roadmap (no numbers, pure high-level synthesis):**

> Large Language Models (LLMs) are increasingly integrated into software applications, giving rise to a broad class of prompt-enabled systems, in which prompts serve as the primary 'programming' interface for guiding system behavior. Building on this trend, a new software paradigm, promptware, has emerged, which treats natural language prompts as first-class software artifacts for interacting with LLMs. Unlike traditional software, which relies on formal programming languages and deterministic runtime environments, promptware is based on ambiguous, unstructured, and context-dependent natural language and operates on LLMs as runtime environments, which are probabilistic and non-deterministic. These fundamental differences introduce unique challenges in prompt development. In practice, prompt development remains largely ad hoc and relies heavily on time-consuming trial-and-error, a challenge we term the promptware crisis. To address this, we propose promptware engineering, a new methodology that adapts established Software Engineering (SE) principles to prompt development. [...] This paper outlines a comprehensive roadmap for promptware engineering, identifying key research directions and offering actionable insights to advance the development of prompt-enabled systems.

Note: every sentence is a generalisable claim (the paradigm, the contrast, the named crisis, the proposed methodology). It would be just as strong with no dataset behind it, because the contribution *is* the framing.

**Empirical study (numbers present, but subordinated to claims):**

> Build systems are essential for modern software maintenance and development, while build failures occur frequently across software systems, inducing non-negligible costs in development activities. [...] Understanding how build failures are resolved in practice can provide guidelines for both developers and researchers on build issue resolution. Therefore, this work presents a comprehensive study of fix patterns in practical build failures. Specifically, we study 1,080 build issues of three popular build systems Maven, Ant, and Gradle from Stack Overflow, construct a fine-granularity taxonomy of 50 categories regarding the failure symptoms, and summarize the fix patterns for different failure types. Our key findings reveal that build issues stretch over a wide spectrum of symptoms; 67.96% of the build issues are fixed by modifying the build script code related to plugins and dependencies; and there are 20 symptom categories, more than half of whose build issues can be fixed by specific patterns.

Note: the numbers (1,080 issues, 50 categories, 67.96%) appear, but each is attached to a high-level finding ("build issues stretch over a wide spectrum of symptoms", "fixed by modifying the build script code related to plugins and dependencies"). The claim leads; the number supports.

## Common Pitfalls

- **Data-dump abstract (low altitude)**: reciting counts, percentages, and dataset sizes without synthesising what they mean. The most common altitude failure; reads as a results table in prose. Each number must be subordinated to a claim.
- **Missing Zeller numbers (empirical/systems papers)**: for measurement-based work, an abstract with no quantitative results reads as vague and unfinished. (Does not apply to vision/roadmap papers.)
- **Too much background**: spending half the abstract on context that the title already conveys. Get to the contribution quickly.
- **Listing contributions instead of telling a story**: "We make three contributions: (1)... (2)... (3)..." is a contribution list, not an abstract. The abstract should flow as a narrative of claims.
- **Overselling**: words like "novel", "unprecedented", "groundbreaking" without evidence. Let the claims and numbers speak.
- **Too long**: if the abstract exceeds the word limit, it has not been précised enough. Every word must earn its place.

## Writing Process

1. Start with each of the four questions as a separate paragraph.
2. Focus on making each answer compelling and precise.
3. Raise the altitude: convert every "we measured X" into "X means Y (value)". Delete sentences that only describe bookkeeping.
4. Once compelling, précis repeatedly until the whole abstract is one paragraph that retains all the semantics.
5. Like programming: get it right first, then optimise to make it tight and fast.
6. Study abstracts from top SE venues (ICSE, FSE, ASE, ISSTA, TSE, TOSEM) for format reference.

## Checklist

- [ ] Single paragraph, no references
- [ ] States the problem clearly
- [ ] Explains why the problem matters
- [ ] Describes the solution approach at the level of the idea
- [ ] Every sentence is a high-level claim, not a raw data report
- [ ] Key numbers (if any) are subordinated to the findings they support
- [ ] Contains Zeller numbers for empirical/systems work; conceptual framing for vision/roadmap work
- [ ] Within word limit
- [ ] No vague claims without support
- [ ] No unnecessary background or preamble
