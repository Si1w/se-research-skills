# Excalidraw JSON Schema Reference

Verified against obsidian-excalidraw-plugin source and @excalidraw/excalidraw v0.18.0.

## File Format (.excalidraw.md)

The Obsidian Excalidraw plugin stores drawings as markdown files with embedded JSON.

### Exact structure:

```markdown
---
excalidraw-plugin: parsed
tags: [excalidraw]
excalidraw-autoexport: svg
excalidraw-export-transparent: true
excalidraw-export-dark: false
excalidraw-export-padding: 20
---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠== You can decompress Drawing data with the command palette: 'Decompress current Excalidraw file'. For more info check in plugin settings under 'Saving'

# Excalidraw Data

## Text Elements

## Element Links

## Embedded Files

## Drawing
```json
{JSON data}
```
%%
```

### Frontmatter keys for export

| Key | Type | Values |
|-----|------|--------|
| `excalidraw-plugin` | text | `"parsed"` (required) |
| `excalidraw-autoexport` | text | `"none"`, `"both"`, `"png"`, `"svg"` |
| `excalidraw-export-transparent` | boolean | transparent background |
| `excalidraw-export-dark` | boolean | dark mode export |
| `excalidraw-export-padding` | number | padding in px |
| `excalidraw-export-pngscale` | number | PNG scale (0.5-5) |

## Top-level JSON Structure

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

## Base Element Fields

Every element (rectangle, text, arrow, etc.) requires all of these fields:

```json
{
  "id": "abcd1234",
  "type": "rectangle",
  "x": 100,
  "y": 100,
  "width": 200,
  "height": 80,
  "angle": 0,
  "strokeColor": "#1e1e1e",
  "backgroundColor": "transparent",
  "fillStyle": "solid",
  "strokeWidth": 2,
  "strokeStyle": "solid",
  "roughness": 0,
  "opacity": 100,
  "groupIds": [],
  "roundness": { "type": 3 },
  "seed": 12345,
  "version": 1,
  "versionNonce": 987654321,
  "index": null,
  "isDeleted": false,
  "frameId": null,
  "boundElements": [],
  "updated": 1710000000000,
  "link": null,
  "locked": false
}
```

Field notes:
- `id`: 8-character nanoid (alphanumeric)
- `seed`: `Math.floor(Math.random() * 100000)` — used by roughjs for consistent rendering
- `versionNonce`: `Math.floor(Math.random() * 1000000000)`
- `updated`: `Date.now()` epoch milliseconds
- `index`: fractional index for ordering, use `null`
- `frameId`: parent frame id, use `null` for standalone elements
- `boundElements`: array of `{ id, type }` for bound text/arrows, or `[]` if none
- `angle`: rotation in radians

## Element Types

### Rectangle
Uses base fields. `roundness: { "type": 3 }` for rounded corners, `null` for sharp.

### Ellipse
Uses base fields. `roundness: { "type": 2 }`.

### Diamond
Uses base fields. `roundness: { "type": 2 }`.

### Text

Base fields plus:
```json
{
  "text": "Display Text",
  "fontSize": 24,
  "fontFamily": 5,
  "textAlign": "center",
  "verticalAlign": "middle",
  "containerId": null,
  "originalText": "Display Text",
  "autoResize": true,
  "lineHeight": 1.25
}
```

- `fontFamily`: 1=Virgil, 2=Helvetica, 3=Cascadia, 4=LocalFont(Obsidian), 5=Excalifont, 6=Nunito, 7=Lilita One, 8=Comic Shanns, 9=Liberation Sans
- `containerId`: set to the parent shape's `id` when text is bound inside a container; `null` for standalone text
- `originalText`: should match `text`

### Arrow

Base fields plus:
```json
{
  "points": [[0, 0], [200, 0]],
  "lastCommittedPoint": null,
  "startBinding": null,
  "endBinding": null,
  "startArrowhead": null,
  "endArrowhead": "arrow",
  "elbowed": false
}
```

- `points`: array of [x, y] relative to the element's x, y position. First point is always [0, 0].
- `startBinding` / `endBinding`: `{ "elementId": "target-id", "focus": 0, "gap": 5 }` or `null`
- `elbowed`: `true` for right-angle connector arrows

### Line

Same as Arrow but without arrowheads. Use `type: "line"`.

## Text Binding to Containers

To place text inside a shape, both sides must reference each other:

**Container** declares its bound text:
```json
{
  "type": "rectangle",
  "id": "box-1",
  "boundElements": [{ "id": "text-1", "type": "text" }]
}
```

**Text** declares its container:
```json
{
  "type": "text",
  "id": "text-1",
  "containerId": "box-1",
  "textAlign": "center",
  "verticalAlign": "middle"
}
```

When text is bound, its position is auto-calculated by the plugin. Set x/y to the container's x/y as a default.

## Arrow Binding to Shapes

To connect an arrow to shapes, both sides must reference each other:

**Arrow** declares its bindings:
```json
{
  "type": "arrow",
  "id": "arrow-1",
  "startBinding": { "elementId": "box-1", "focus": 0, "gap": 5 },
  "endBinding": { "elementId": "box-2", "focus": 0, "gap": 5 }
}
```

**Shapes** list the arrow in their boundElements:
```json
{ "id": "box-1", "boundElements": [{ "id": "arrow-1", "type": "arrow" }, { "id": "text-1", "type": "text" }] }
{ "id": "box-2", "boundElements": [{ "id": "arrow-1", "type": "arrow" }, { "id": "text-2", "type": "text" }] }
```

## Enum Values

### fillStyle
`"solid"` | `"hachure"` | `"cross-hatch"` | `"zigzag"`

### strokeStyle
`"solid"` | `"dashed"` | `"dotted"`

### roughness
| Value | Name | Visual |
|-------|------|--------|
| 0 | architect | Clean, precise lines |
| 1 | artist | Slightly hand-drawn (default) |
| 2 | cartoonist | Very sketchy |

### roundness
| Type | Usage |
|------|-------|
| `{ "type": 1 }` | Legacy rounding |
| `{ "type": 2 }` | Proportional radius (ellipse, diamond, linear elements) |
| `{ "type": 3 }` | Adaptive radius (rectangles, recommended) |
| `null` | Sharp corners |

### arrowhead
`"arrow"` | `"bar"` | `"dot"` | `"circle"` | `"circle_outline"` | `"triangle"` | `"triangle_outline"` | `"diamond"` | `"diamond_outline"` | `"crowfoot_one"` | `"crowfoot_many"` | `"crowfoot_one_or_many"`

## Text Centering (standalone text only)

Standalone text elements (containerId: null) need manual x-coordinate calculation:
- English: `estimatedWidth = text.length * fontSize * 0.5`
- CJK: `estimatedWidth = text.length * fontSize * 1.0`
- Center formula: `x = containerCenterX - estimatedWidth / 2`

Bound text (containerId set) is auto-centered by the plugin.

## Grouping

Set the same group ID in `groupIds` for all elements that should be grouped:
```json
{ "id": "box-1", "groupIds": ["group-phase1"] }
{ "id": "text-1", "groupIds": ["group-phase1"] }
```
