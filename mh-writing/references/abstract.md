# Abstract

## Purpose

The abstract is the paper's elevator pitch. Most readers, and many referees, decide whether to read further based on the abstract alone. It must convey the core contribution and its evidence in minimal space, and get to the point quickly. Study abstracts from top SE venues (ICSE, FSE, ASE, ISSTA, RE, TSE, TOSEM) to get a sense of the expected format.

## Format

- Single paragraph. No line breaks, no subsections.
- No references or citations.
- No forward references to sections, figures, or tables.
- Typically 150 to 250 words (check venue guidelines).

## The Four Questions

A strong abstract answers four questions, in this order:

1. **What is the problem?**
2. **Why does it matter?**
3. **What is your solution?**
4. **What evidence do you offer?**

## Exemplars

**Vision / roadmap (no numbers, pure high-level synthesis):**

> Large Language Models (LLMs) are increasingly integrated into software applications, giving rise to a broad class of prompt-enabled systems, in which prompts serve as the primary ‘programming’ interface for guiding system behavior. Building on this trend, a new software paradigm, promptware, has emerged, which treats natural language prompts as first-class software artifacts for interacting with LLMs. Unlike traditional software, which relies on formal programming languages and deterministic runtime environments, promptware is based on ambiguous, unstructured, and context-dependent natural language and operates on LLMs as runtime environments, which are probabilistic and non-deterministic. These fundamental differences introduce unique challenges in prompt development. In practice, prompt development remains largely ad hoc and relies heavily on time-consuming trial-and-error, a challenge we term the promptware crisis. To address this, we propose promptware engineering, a new methodology that adapts established Software Engineering (SE) principles to prompt development. Drawing on decades of success in traditional SE, we envision a systematic framework encompassing prompt requirements engineering, design, implementation, testing, debugging, evolution, deployment, and monitoring. Our framework re-contextualizes emerging prompt-related challenges within the SE lifecycle, providing principled guidance beyond ad-hoc practices. Without the SE discipline, prompt development is likely to remain mired in trial-and-error. This paper outlines a comprehensive roadmap for promptware engineering, identifying key research directions and offering actionable insights to advance the development of prompt-enabled systems.

Note: every sentence is a generalisable claim (the paradigm, the contrast, the named crisis, the proposed methodology). It would be just as strong with no dataset behind it, because the contribution *is* the framing.

**Empirical study (numbers present, but subordinated to claims):**

> Build systems are essential for modern software maintenance and development, while build failures occur frequently across software systems, inducing non-negligible costs in development activities. Build failure resolution is a challenging problem and multiple studies have demonstrated that developers spend non-trivial time in resolving encountered build failures; to relieve manual efforts, automated resolution techniques are emerging recently, which are promising but still limitedly effective. Understanding how build failures are resolved in practice can provide guidelines for both developers and researchers on build issue resolution. Therefore, this work presents a comprehensive study of fix patterns in practical build failures. Specifically, we study 1,080 build issues of three popular build systems Maven, Ant, and Gradle from Stack Overflow, construct a fine-granularity taxonomy of 50 categories regarding to the failure symptoms, and summarize the fix patterns for different failure types. Our key findings reveal that build issues stretch over a wide spectrum of symptoms; 67.96% of the build issues are fixed by modifying the build script code related to plugins and dependencies; and there are 20 symptom categories, more than half of whose build issues can be fixed by specific patterns. Furthermore, we also address the challenges in applying non-intuitive or simplistic fix patterns for developers.

Note: the numbers (1,080 issues, 50 categories, 67.96%) appear, but each is attached to a high-level finding. The claim leads; the number supports.

**Technique / approach paper (the four questions answered in order, well Zellerised):**

> Machine Learning (ML) software can lead to unfair and unethical decisions, making software fairness bugs an increasingly significant concern for software engineers. However, addressing fairness bugs often comes at the cost of introducing more ML performance (e.g., accuracy) bugs. In this paper, we propose MAAT, a novel ensemble approach to improving fairness-performance trade-off for ML software. Conventional ensemble methods combine different models with identical learning objectives. MAAT, instead, combines models optimized for different objectives: fairness and ML performance. We conduct an extensive evaluation of MAAT with 5 state-of-the-art methods, 9 software decision tasks, and 15 fairness-performance measurements. The results show that MAAT significantly outperforms the state-of-the-art. In particular, MAAT beats the trade-off baseline constructed by a recent benchmarking tool in 92.2% of the overall cases evaluated, 12.2 percentage points more than the best technique currently available. Moreover, the superiority of MAAT over the state-of-the-art holds on all the tasks and measurements that we study. We have made publicly available the code and data of this work to allow for future replication and extension.

Note: this walks the four questions in order: problem (fairness bugs), why it matters (they trade off against ML performance), solution (MAAT, whose conceptual move is stated by contrast: "Conventional ensemble methods combine... identical objectives. MAAT, instead, combines models optimized for different objectives"), and evidence. The headline numbers (92.2% of cases, 12.2 percentage points more) are each subordinated to the claim "significantly outperforms the state-of-the-art" rather than reported as bare measurements.