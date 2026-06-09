# .excalidraw element schema

Read this only to debug `build.py` or extend the layout. The file is JSON:

```json
{
  "type": "excalidraw",
  "version": 2,
  "source": "...",
  "elements": [ ... ],
  "appState": { "viewBackgroundColor": "#ffffff" },
  "files": {}
}
```

Every element shares these fields: `id`, `type`, `x`, `y`, `width`, `height`, `angle`, `strokeColor`, `backgroundColor`, `fillStyle`, `strokeWidth`, `strokeStyle`, `roughness`, `opacity`, `groupIds`, `frameId`, `roundness`, `seed`, `version`, `versionNonce`, `isDeleted`, `boundElements`, `updated`, `link`, `locked`. Coordinates are absolute pixels; `x,y` is the top-left corner.

## Shapes

`rectangle`, `diamond`, `ellipse` use only the shared fields. `roundness: {"type":3}` rounds rectangle corners; `null` keeps them sharp.

## Text

A label is a separate `text` element bound to its shape:
- text has `containerId` = the shape id, plus `fontSize`, `fontFamily` (1 hand-drawn, 2 normal, 3 code), `text`, `originalText`, `textAlign`, `verticalAlign`, `lineHeight`.
- the shape lists the text in `boundElements: [{"type":"text","id":<textId>}]`.

Excalidraw re-centers bound text on load, so approximate `x,y` is fine.

## Arrows

An `arrow` has `points` relative to its own `x,y`, e.g. `[[0,0],[dx,dy]]`, and:
- `startBinding`/`endBinding`: `{"elementId": <shapeId>, "focus": 0, "gap": 4}`.
- `startArrowhead` (usually `null`), `endArrowhead` (`"arrow"`).
- both endpoint shapes must list the arrow in their `boundElements`.

Bindings let excalidraw re-route the arrow when a shape moves. Every id in a binding or `boundElements` must resolve to a real element, or the file is broken.

An edge label is a `text` element with `containerId` set to the arrow id, and the arrow lists it in `boundElements`. Excalidraw renders this as a centered arrow label.

## Images

An `image` element has `fileId`, `status: "saved"`, `scale: [1,1]`, `crop: null`, plus `x,y,width,height`. The picture lives in the top-level `files` map: `files[fileId] = {id, dataURL, mimeType, created, lastRetrieved}`, where `dataURL` is `data:image/svg+xml;base64,...` (or PNG). Image nodes carry no bound text; their caption is a separate free `text` element placed below.

## Layout notes

`build.py` does longest-path layering with barycenter ordering per layer. Known limit: a back-edge between two adjacent layers is drawn straight over the forward edge. Pull it apart in the editor if it matters; the `.excalidraw` is editable.
