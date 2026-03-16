---
name: ob-excalidraw
description: Generate research diagrams for SE papers using Excalidraw in Obsidian — including pipeline overviews, method illustration figures, and architecture diagrams. Outputs .excalidraw.md with auto-export SVG to the user's PhD vault. Use this skill whenever the user wants to create any kind of figure or diagram from a paper (PDF/tex) or codebase, whether it's a high-level system overview or a worked-example figure that illustrates how a method or algorithm operates step by step.
---

# Excalidraw Research Diagram Generator

Generate publication-quality research diagrams from papers or code, output as Excalidraw files in Obsidian with auto-exported SVG.

This skill supports two broad categories of figures:

- **Pipeline/architecture diagrams** — high-level overviews showing system components and data flow between them
- **Method illustration figures** — worked-example diagrams that show *how* a method operates, walking the reader through a concrete example with intermediate states, transformations, and results. These often use sub-figure panels, side-by-side comparisons, nested containers, or tree/graph structures to make the method tangible.

## Workflow

1. **Read the source material** — the user provides a PDF, tex file, or verbal description. Identify what needs to be illustrated.

2. **Determine the diagram type and extract key elements:**
   - For pipeline/architecture: identify 3-7 major components, their inputs/outputs, relationships, and any grouping/layering.
   - For method illustrations: identify the key steps or sub-processes, what concrete example to walk through, what intermediate states to show, and how the sub-figures relate to each other.

3. **Choose a layout** — pick the layout that best represents the content:
   - **Left-to-right flow**: for sequential pipelines (most common for method overviews)
   - **Top-to-bottom hierarchy**: for systems with clear layers or tree structures
   - **Grouped flow**: for pipelines with parallel branches that merge
   - **Multi-panel**: for method illustrations that show several steps or compare alternative approaches — use large grouped regions with sub-figure labels (e.g., circled A, B, or numbered steps)

4. **Generate the Excalidraw JSON** following the design rules below.

5. **Save files and embed** — save the `.excalidraw.md` to the project folder and embed it in the proposal document.

## Output Destination

When generating a diagram:
1. Save the `.excalidraw.md` file to the project folder: `<project>/<name>.excalidraw.md`
2. The Excalidraw plugin auto-exports SVG to the same folder (configured via frontmatter)
3. Append an embed link to the project's main proposal document (e.g., `<project>.md`):
   ```
   ![[<name>.svg]]
   ```

If you're unsure which project folder to use, ask the user.

## Excalidraw File Format

Read the template at `assets/template.excalidraw.md` and use it as the base for every generated file. Replace `{complete Excalidraw JSON here}` with the actual Excalidraw JSON data. Do not modify the frontmatter or section headers — the Obsidian Excalidraw plugin requires this exact structure to parse the file correctly.

The `excalidraw-autoexport: svg` frontmatter tells the plugin to automatically generate and keep in sync an SVG file alongside the drawing.

## Design Rules for Academic Figures

These rules ensure figures are readable when printed on A4 paper and meet academic publication standards. Read `references/figures-and-tables.md` from the `mh-writing` skill for the full rationale — the key points are below.

### Readability First

The most important rule: every piece of text must be legible when the figure is reduced to fit a single-column or double-column layout on A4 paper. This means:

| Element | Font Size |
|---------|-----------|
| Titles | 28-32px |
| Labels | 20-24px |
| Minimum (any text) | 20px |

- **High contrast**: dark text on light backgrounds. No light gray text on white.
- **Keep it simple**: 3-7 major boxes. If you need more detail, consider splitting into multiple figures.

### Black-and-White Friendly

Referees often print in B&W. Color can enhance understanding but must not be the only way to distinguish elements:

- Use distinct shapes (rectangle, rounded-rect, diamond) and line styles (solid, dashed) to differentiate element types
- Use fill patterns or shading levels that remain distinguishable in grayscale
- Read `references/academic-palettes.md` for the recommended color palette — it's designed to degrade gracefully to B&W

### Layout Principles

- **Canvas size**:

  | Layout Type | Canvas Size (px) |
  |-------------|-----------------|
  | Landscape pipeline | ~1400 x 600 |
  | Portrait hierarchy | ~800 x 1000 |
  | Multi-panel method illustration | ~1800 x 1200 (scale up as needed) |
- **Generous spacing**: minimum 40px between elements. Cramped diagrams are unreadable when scaled down.
- **Alignment**: keep elements on a grid. Misaligned boxes look sloppy.
- **Flow direction**: make data flow obvious with arrows. Left-to-right or top-to-bottom, pick one and be consistent.
- **Group labels**: if the diagram has layers/phases, use large semi-transparent background rectangles with a label, to visually group related components.
- **Sub-figure labels**: for multi-panel method illustrations, use circled letters or numbers (e.g., a filled circle with white text "A", "B", "1", "2") to label each panel. Place them at the top-left of the panel they describe.
- **Canvas padding**: leave 60-80px margin on all sides.

### Semantic Information Principle (SIP)

Every visual difference should encode meaning. Do not add decorative gradients, shadows, 3D effects, or random color variations. If two boxes look different, that difference should mean something (e.g., different component types, different execution phases).

### Method Illustration Figures

Method illustration figures differ from pipeline diagrams: instead of abstracting components into labeled boxes, they walk the reader through a concrete example showing how the method works. The goal is to make the method tangible and intuitive — the reader should be able to follow the worked example and understand the approach without reading the full paper text.

Key principles:

- **Show, don't just label.** Use concrete examples (actual data samples, code snippets, intermediate outputs) rather than abstract box names. Let the reader see the transformation happening.
- **Use nesting to show structure.** Large rounded-rect containers group related content into panels. Within each panel, smaller boxes show individual elements. Use stroke and fill color consistently across panels so the reader can trace elements through transformations.
- **Connect panels with arrows.** Show how one step leads to the next with curved or angled arrows between panels.
- **Consistent color coding across panels.** If a color represents a semantic category in one panel, maintain that mapping in all other panels so elements are visually traceable.
- **Use monospace text** (`fontFamily: 3`, Cascadia) for code snippets and technical content within worked examples. Use the default font (`fontFamily: 5`, Excalifont) for panel titles and labels.

### No Emoji

Do not use emoji in diagram text. Use shapes and colors for visual markers instead.

## Color Palette

Read `references/academic-palettes.md` for all color definitions (text, fills, strokes, contrast pairings). Default palette is Blue-Green Academic.

## JSON Structure

See `references/excalidraw-schema.md` for the complete element type reference. Key points:

```json
{
  "type": "excalidraw",
  "version": 2,
  "source": "https://github.com/zsviczian/obsidian-excalidraw-plugin",
  "elements": [],
  "appState": {
    "gridSize": null,
    "viewBackgroundColor": "#ffffff"
  },
  "files": {}
}
```

See `references/excalidraw-schema.md` for all element fields and binding syntax. Key guidelines:

- Use `roughness: 0` for clean academic style (not hand-drawn)
- Use `fontFamily: 5` (Excalifont) for labels and headings; use `fontFamily: 3` (Cascadia) for code snippets in method illustrations
- Each element needs a unique `id` (8-char alphanumeric) and unique `seed`
- Include all required fields: `versionNonce`, `frameId: null`, `index: null`, `updated` (use `Date.now()`)
- Bind text to containers: set `containerId` on text and `boundElements` on the shape — bound text is auto-centered
- Bind arrows to shapes: set `startBinding`/`endBinding` on arrow and list the arrow in each shape's `boundElements`

## After Generation

Report to the user:
1. What the diagram shows and the design rationale
2. File save location
3. Remind them to open in Obsidian → switch to Excalidraw view
4. The SVG will auto-export to the same folder
5. Ask if any adjustments are needed (layout, grouping, labels, colors)
