---
name: weekly-report
description: Generate a Quarto revealjs slide deck for the user's weekly supervisor meeting by extracting work from git commits and markdown updates across user-supplied repos/notes over a confirmable time window, then filling a fixed template into a post file inside the current Quarto project. Use this skill whenever the user wants to prepare a supervisor meeting, make a weekly report, summarize this week's work, or says phrases like "weekly report", "meeting prep", "prepare for meeting".
---

# Weekly Meeting Report Generator

Generate one slide post summarizing the user's work over a confirmable window, for supervisor meetings.

The Quarto website is already scaffolded in the current workspace. This skill only adds one new post per run: a single `posts/YYYY-MM-DD.qmd` file (date = that week's Wednesday). Do not modify the project scaffolding.

## Design Principles

Slides are for **discussion, not status updates**. The meeting is a conversation about results — build the deck around **concrete artifacts** (figures, tables, analysis outputs) that the audience can react to, not a list of what you did.

### Artifact-first hierarchy

1. **Figures & tables** — copy output artifacts (PNGs, CSVs) from the scanned repos into the post directory; each artifact gets its own slide with a 1–2 sentence caption explaining what it shows and what to discuss
2. **Mermaid diagrams** — for workflows, timelines, dependencies, progress pipelines (only when no pre-rendered figure exists)
3. **Key metrics / callouts** — bold numbers, short labels (e.g., "30% AI-authored commits")
4. **Minimal bullets** — fragments, not sentences; max 4 items per slide; use only for Recap, Blockers, Plan, or brief process updates that lack a visual
5. **No prose paragraphs** — if it reads like an email, it belongs in notes not slides

### Language density rules

| Element | Max length | Style |
|---------|-----------|-------|
| Bullet | 8 words | Fragment, no period |
| Slide title | 5 words | Noun phrase or verb phrase |
| Diagram node | 3 words | Label only |
| Callout stat | 1 number + 4-word label | e.g., "3 PRs merged" |

### One idea per slide

If a slide has more than one takeaway, split it. The audience retains nothing from a dense slide.

## Workflow

### 1. Compute and confirm the time window

Default window: **from the most recent past Wednesday 16:00 local time to now.** If today is Wednesday and it is already past 16:00, the window starts today at 16:00.

Run the helper script to get the default:

```bash
python3 <skill_dir>/scripts/compute_window.py
```

Show the computed `since -> now` to the user and ask them to confirm or override. Always confirm — the window drives everything downstream.

### 2. Ask the user for data sources

Prompt the user to list:

- **Repos / directories** to scan (absolute paths).
- **Optional: last meeting notes file** to summarize for the Recap section.

Do NOT guess paths or scan the home directory broadly.

### 3. Extract evidence from sources

For each directory:

- **Commits in window:**

  ```bash
  git -C <path> log --since "<SINCE>" --pretty=format:"%h %ad %s" --date=short
  ```

- **Markdown files modified in window:**

  ```bash
  find <path> -name "*.md" -newermt "<SINCE>" \
    -not -path "*/node_modules/*" -not -path "*/.git/*" -not -path "*/_site/*"
  ```

- Read the top of any new/changed md file to extract headings and salient new content. Do not read huge files in full — a `Read` with `limit: 80` is usually enough.

- **TODO / FIXME added this week** (signal for blockers):

  ```bash
  git -C <path> log --since "<SINCE>" -p -S "TODO" -- "*.md" "*.py" "*.ts" | head -100
  ```

Aggregate commits into 3–5 thematic groups. Do not dump raw `git log` into the slide.

### 3b. Scan for output artifacts

For each directory, find new figures and tables produced during the window:

```bash
find <path>/eval/tables-and-figures -newermt "<SINCE>" -type f 2>/dev/null | sort
```

Also check common output directories (`eval/`, `results/`, `output/`, `figures/`). For each artifact found:

- **PNGs/PDFs**: read the image to understand what it shows.
- **CSVs**: read the file to understand the data; consider rendering as a table slide.

These artifacts are the **primary slide content**. Each interesting artifact becomes its own slide with a brief caption. Copy the relevant files into the post directory.

### 4. Gather qualitative content from the user

Ask the user (one round, batched question) for:

- **Recap**: last meeting's key decisions (2–3 bullets max)
- **Blockers & Questions**: what is stuck. Surface any TODO/FIXME found in step 3 for triage.
- **Plan**: next week's top 3 goals
- **Categories**: propose tags from extracted content (choose from `paper`, `experiment`, `coding`, `reading`, `writing`, `meeting`, `reviewing`)
- **Description**: one-line summary for the listing page

### 5. Generate diagrams

Based on extracted evidence, generate **Mermaid diagrams** to replace text where possible:

**Progress pipeline** — show workflow state:
```markdown
```{mermaid}
flowchart LR
  A[Data collection] --> B[Preprocessing]
  B --> C[Experiment run]
  C --> D[Analysis]
  style C fill:#4CAF50,color:#fff
```
```

Highlight the current stage with color. Use `fill:#4CAF50` for completed, `fill:#FFC107` for in-progress, default for pending.

**Plan timeline** — show next week's goals as a sequence:
```markdown
```{mermaid}
gantt
  dateFormat  YYYY-MM-DD
  section Paper
    Draft RQ section :a1, 2025-04-09, 3d
  section Experiment
    Run ablation      :a2, 2025-04-10, 2d
```
```

Choose the diagram type that best fits the content:
- `flowchart LR` — for pipelines, processes, dependencies
- `gantt` — for time-based plans
- `graph TD` — for hierarchies or architectures
- `sequenceDiagram` — for interactions between components

If the week's work doesn't map naturally to a diagram, skip the diagram slide rather than forcing it.

### 6. Fill the template and save the post

- Read the template at `<skill_dir>/assets/post-template.qmd`.
- Replace every placeholder; remove unused diagram slides entirely (delete the `## Workflow` or `## Next Week` slide if no diagram was generated).
- Write to `posts/YYYY-MM-DD.qmd` where `YYYY-MM-DD` is the ISO date of the window start (the Wednesday). If the file already exists, ask the user whether to overwrite or pick a different date.

### 7. Report back and offer preview

Tell the user:

- The relative path of the new post.
- How to preview: `quarto preview`
- How to render only this post: `quarto render posts/YYYY-MM-DD.qmd`

Do not automatically run `quarto render` unless the user asks.

## Placeholders

| Placeholder | Replacement |
|-------------|-------------|
| `{{WEEK_LABEL}}` | e.g., `"Apr 8 – 14"` (short, no "Week of") |
| `{{DATE}}` | ISO date `YYYY-MM-DD` (the Wednesday) |
| `{{CATEGORIES}}` | Comma-separated tags |
| `{{DESCRIPTION}}` | One-line summary |
| `{{RECAP}}` | 2–3 bullet fragments of last meeting's decisions |
| `{{PROGRESS}}` | 3–5 bullet fragments grouped by theme |
| `{{WORKFLOW_DIAGRAM}}` | Mermaid diagram showing progress pipeline (or remove slide) |
| `{{BLOCKERS}}` | 2–3 bullet fragments |
| `{{PLAN}}` | Top 3 goals as bullet fragments |
| `{{PLAN_DIAGRAM}}` | Mermaid gantt or flowchart for next week (or remove slide) |

## Content rules

- **Fragments, not sentences.** "Drafted RQ section" not "I drafted the RQ section this week."
- **Past participle** for Progress ("Drafted...", "Merged...", "Fixed..."). **Imperative** for Plan ("Finish X", "Run Y").
- **Max 4 bullets per slide.** If Progress has more, split into themed slides (`## Progress — Paper`, `## Progress — Code`).
- **Ground in evidence** — every Progress bullet must trace to a commit, changed file, or user input. Never fabricate.
- **Prefer diagrams over bullets** when showing process, timeline, or dependencies.

## Anti-patterns

- Do **not** write full sentences on slides — fragments only.
- Do **not** exceed 4 bullets per slide.
- Do **not** create text-only slides when a diagram would communicate better.
- Do **not** auto-generate figures or charts beyond Mermaid — the user manages other visuals manually.
- Do **not** re-scaffold the Quarto project. If `_quarto.yml` is missing, stop and tell the user.
- Do **not** dump raw `git log` output — always summarize into fragments.
- Do **not** overwrite an existing post without explicit confirmation.
- Do **not** skip the "confirm window" step.
- Do **not** scan paths the user did not explicitly list.
- Do **not** summarize activity ("worked on X, built Y") without showing a concrete artifact — if there's no figure or table to anchor the slide, condense it into a bullet on a process-update slide instead.
- Do **not** use vague verbs ("worked on", "continued", "progressed") — use concrete verbs ("drafted", "merged", "ran", "fixed").

## If the Quarto project is missing

If `_quarto.yml` does not exist in the current workspace, stop and tell the user they may be in the wrong directory. Do not silently recreate the scaffold.
