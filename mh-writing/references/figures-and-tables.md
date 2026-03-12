# Figures and Tables

## Purpose

Figures and tables are "boxouts" — elements that stand out when a referee flicks through the paper. Together with the envelope (title, abstract, introduction, conclusions), they form the referee's first impression. A referee who sees clear, informative figures will approach the text more favourably.

## Format

### Figures
- Must be readable when reduced to fit the column/page width. Increase point size of labels (axis labels, legends) relative to figure size.
- All text within figures (axis labels, tick marks, legend entries, annotations) must be clearly legible when printed on A4 paper at the final layout size. If any text requires squinting or zooming, the font size is too small. As a rule of thumb, no text in a figure should be smaller than the caption font size.
- Use vector formats (PDF, SVG) over raster formats (PNG, JPG) whenever possible.
- Captions go below the figure.

### Tables
- Numeric columns: always right-justified.
- Name columns (e.g., program names): left-justified.
- Centre justification: rarely appropriate — only when data does not require left or right alignment.
- Units go in column headings, not repeated in each row.
- Captions go above the table.

## Required Elements

- **Self-contained captions**: Every figure and table must be understandable from its caption alone. A referee flicking through the paper should be able to understand what each figure shows without reading the surrounding text.
- **Referenced in text**: Every figure and table must be referenced and discussed in the body text. An unreferenced figure is a wasted figure.
- **Every element explained**: Every axis, column, row label, legend entry, symbol, abbreviation, and data series in a figure or table must be explicitly explained, either in the caption or in the surrounding text. If a table has a column called "Δ" or "Config.", the reader should never have to guess what it means. Unexplained elements signal carelessness and invite referee skepticism.
- **Connected to RQs**: Each figure/table in the results section should clearly map to a research question.

## Common Pitfalls

- **Not self-contained**: Caption says "Results of our experiment" — this is useless. Caption should say "Fault detection rates (%) of our approach vs. three baselines across 12 Java projects. Higher is better. Bold indicates statistical significance at p < 0.05."
- **Unreadable when printed**: Tiny labels, thin lines, low contrast. Referees often review on printouts or small screens.
- **Colour-only encoding**: Using colour as the only way to distinguish data series. The paper must be perfectly understandable when printed in black and white — referees usually see things in B&W. Use patterns, markers, or line styles in addition to colour.
- **Superficial visual features (SIP violation)**: The Semantic Information Principle says every discernible visual difference should convey meaning. If two boxes have different shapes, that difference must mean something. Avoid decorative shading, 3D effects, background colours on plots, or other visual noise that does not encode data.
- **Repeated information**: If you see the same word repeated in every row of a table, it belongs in the heading. Like programming: repeated code means you need a loop.
- **Too many figures/tables**: If figures and tables consume more than 40% of the paper, the text-to-visual ratio is off. Each visual should earn its space.
- **Poor page layout**: As a last step, arrange paragraphs to complete neatly at column ends, and place headings at the top of columns where possible. Avoid orphaned figure/table captions separated from their content.

## Checklist

- [ ] Every figure/table has a self-contained caption
- [ ] Every figure/table is referenced in the body text
- [ ] Figures are readable when reduced to column width
- [ ] Numeric table columns are right-justified
- [ ] Units are in column headings, not in rows
- [ ] Paper is understandable in black and white
- [ ] No decorative visual elements that do not encode data (SIP)
- [ ] Every axis, column, legend entry, and symbol is explained in caption or text
- [ ] Results figures/tables map to research questions
- [ ] No unnecessary repetition in table rows
