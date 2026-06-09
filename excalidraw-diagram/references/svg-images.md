# Using SVG images in a diagram

A node with an `image` field is drawn as that picture (SVG or PNG) with its `label` as a caption below. The top-level `images` array places pictures freely at given coordinates. A source is a local path or a URL; both are inlined as data URLs in the file's `files` map, so the `.excalidraw` and the PNG are self-contained.

```json
{
  "nodes": [
    {"id": "db", "label": "Postgres", "image": "https://raw.githubusercontent.com/devicons/devicon/master/icons/postgresql/postgresql-original.svg"},
    {"id": "logo", "label": "Local", "image": "./assets/icon.svg"}
  ],
  "images": [
    {"src": "https://cdn.simpleicons.org/redis", "x": 400, "y": 40, "width": 60}
  ]
}
```

## Where to get SVGs

- Tech and tool logos (colored), Devicon: `https://raw.githubusercontent.com/devicons/devicon/master/icons/<name>/<name>-original.svg`. Examples of `<name>`: `react`, `nodejs`, `python`, `postgresql`, `docker`, `kubernetes`, `redis`, `git`, `aws` (as `amazonwebservices`).
- Brand icons (single color), Simple Icons: `https://cdn.simpleicons.org/<slug>` or with a color `https://cdn.simpleicons.org/<slug>/<hex>`. Browse slugs at https://simpleicons.org.
- Any other raw `.svg` URL, or a local `.svg`/`.png` file path.

Verify a URL returns SVG before using it (some pages return HTML). `build.py` treats a source as SVG when the path ends in `.svg`, the content type is SVG, or the first 4 KB contain `<svg`. A non-image response (e.g. an HTML page) is embedded as-is and will not render.

## Sizing

An image node fits the picture into a `72 px` box, preserving aspect ratio, with the caption below. For a free image, give `width` or `height` and the other is derived from the aspect ratio; omit both for a default width of `120 px`. Aspect ratio is read from the SVG `viewBox` or `width`/`height`.
