---
name: md2gdoc
description: Use when the user wants to sync a local Markdown file with Google Docs: push a .md up to a Google Doc, or pull a Google Doc back into Markdown for local editing. Keywords google doc, gdoc, google docs, push, pull, md2gdoc.
---

# md2gdoc

Sync one Markdown file with one Google Doc, both directions, via the native Drive API Markdown conversion. The Doc id lives in the file's frontmatter, so the same file always maps to the same Doc.

## Setup (once)

Needs a Google Cloud project and OAuth credentials. Walk the user through `references/gcp-setup.md`, then put the downloaded `credentials.json` at `~/.config/md2gdoc/credentials.json` (override the directory with `MD2GDOC_HOME`). Skip this if `credentials.json` already exists.

## Workflow

Run from the repo root so `uv` picks up `pyproject.toml`. First run opens a browser for one-time consent.

- Push (create on first run, update the same Doc after): `uv run python md2gdoc/scripts/md2gdoc.py push <file.md>`
- Pull (export the Doc back, frontmatter kept): `uv run python md2gdoc/scripts/md2gdoc.py pull <file.md>`

## Frontmatter

The script reads and writes YAML frontmatter:

- `gdoc_id`: written automatically on the first push; identifies which Doc to update and pull. To adopt an existing Doc, paste its id here by hand before pushing.
- `title`: optional; the Doc name on creation (defaults to the filename).

Frontmatter is local metadata: it is stripped before upload and never appears in the Doc.

## Rules

- Push replaces the whole Doc; pull overwrites the local body. No merge, last write wins, so push or pull deliberately.
- Tables: standard pipe tables convert both ways, but only structure survives. Cell colors, merged cells, and alignment are lost.
- Images: inline images export as broken base64. Use external links `![](https://...)` so they survive both directions.

## Constraints

- One file maps to one Doc. No directory or batch sync.
- Uses the wide `drive` scope; `token.json` is created and refreshed automatically next to `credentials.json`.
