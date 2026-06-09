"""Build a .excalidraw file from a node+edge graph.

Runs under the repo's uv project (root pyproject.toml); uses only the standard
library, so no extra dependency is needed.

Input (stdin or file): JSON
  {
    "direction": "TB" | "LR",      # default TB (top-bottom)
    "roughness": 0 | 1 | 2,         # 0 sharp/formal, 1 default, 2 sketchy
    "font": 1 | 2 | 3,              # 1 hand-drawn(default), 2 normal, 3 code
    "nodes": [{"id","label"?,"shape"?,"image"?}],  # image: .svg/.png path or URL
    "edges": [{"from","to","label"?}],
    "images": [{"src","x","y","width"?,"height"?}]  # free-placed images
  }
Output: .excalidraw JSON to stdout (or -o file).

A node with "image" is drawn as that picture (SVG/PNG) with the label as a
caption below it. Images are embedded as data URLs in the file's `files` map, so
the .excalidraw and PNG are self-contained.

Layout is deterministic: longest-path layering + barycenter ordering.
Claude never computes coordinates; it only describes the graph.
"""
import sys, json, random, argparse, base64, hashlib, re, mimetypes, urllib.request
from graphlib import TopologicalSorter

# --- tunables ---
FONT_SIZE = 20
LINE_H = 1.25
GAP_WITHIN = 60      # space between siblings in a layer
GAP_BETWEEN = 110    # space between layers
PAD_X = 48           # label horizontal padding inside a node
ICON = 72            # max dimension of an image node's picture
LABEL_GAP = 8        # gap between an image and its caption
SIZE = {             # min (w, h) per shape
    "rectangle": (160, 64),
    "diamond":   (180, 90),
    "ellipse":   (150, 70),
}
PALETTE = {          # subtle fills keep it readable, not loud
    "rectangle": "#e7f5ff",
    "diamond":   "#fff9db",
    "ellipse":   "#ebfbee",
}


def node_size(label, shape):
    w_min, h_min = SIZE.get(shape, SIZE["rectangle"])
    w = max(w_min, int(len(label) * FONT_SIZE * 0.6) + PAD_X)
    return w, h_min


_IMG_CACHE = {}  # src -> (fileId, dataURL, mime, aspect)


def svg_aspect(data):
    """Width/height ratio of an SVG, from viewBox or width/height attrs."""
    txt = data[:2000].decode("utf-8", "ignore")
    m = re.search(r'viewBox\s*=\s*["\']\s*[-\d.]+\s+[-\d.]+\s+([-\d.]+)\s+([-\d.]+)', txt)
    if m and float(m.group(1)) > 0 and float(m.group(2)) > 0:
        return float(m.group(1)) / float(m.group(2))
    mw = re.search(r'\bwidth\s*=\s*["\']([\d.]+)', txt)
    mh = re.search(r'\bheight\s*=\s*["\']([\d.]+)', txt)
    if mw and mh and float(mw.group(1)) > 0 and float(mh.group(1)) > 0:
        return float(mw.group(1)) / float(mh.group(1))
    return 1.0


def load_image(src):
    """Fetch a local path or URL, return (fileId, dataURL, mime, aspect)."""
    if src in _IMG_CACHE:
        return _IMG_CACHE[src]
    if src.startswith(("http://", "https://")):
        req = urllib.request.Request(src, headers={"User-Agent": "excalidraw-diagram"})
        with urllib.request.urlopen(req, timeout=20) as r:
            data = r.read()
            mime = r.headers.get_content_type()
    else:
        data = open(src, "rb").read()
        mime = mimetypes.guess_type(src)[0] or ""
    if src.lower().endswith(".svg") or "svg" in (mime or ""):
        mime = "image/svg+xml"
    elif mime in ("", "text/plain", "application/octet-stream") and b"<svg" in data[:4096]:
        mime = "image/svg+xml"
    elif not mime:
        mime = "application/octet-stream"
    aspect = svg_aspect(data) if mime == "image/svg+xml" else 1.0
    url = f"data:{mime};base64," + base64.b64encode(data).decode()
    fid = hashlib.sha1(src.encode()).hexdigest()[:16]
    out = (fid, url, mime, aspect)
    _IMG_CACHE[src] = out
    return out


def fit(aspect, box):
    """Fit a box-sized picture preserving aspect ratio."""
    return (box, box / aspect) if aspect >= 1 else (box * aspect, box)


def layer_nodes(ids, edges):
    """Longest-path layering. Tolerates cycles by dropping back edges."""
    succ = {i: [] for i in ids}
    pred = {i: set() for i in ids}
    # DFS to drop back edges -> guaranteed DAG
    color = {i: 0 for i in ids}      # 0 white 1 gray 2 black
    order = []
    adj = {i: [] for i in ids}
    for e in edges:
        if e["from"] in adj and e["to"] in adj:
            adj[e["from"]].append(e["to"])

    def dfs(u):
        color[u] = 1
        for v in adj[u]:
            if color[v] == 1:
                continue  # back edge -> skip, breaks the cycle
            if (u, v) not in dropped:
                kept.add((u, v))
            if color[v] == 0:
                dfs(v)
        color[u] = 2
        order.append(u)

    dropped, kept = set(), set()
    for i in ids:
        if color[i] == 0:
            dfs(i)
    for u, v in kept:
        succ[u].append(v)
        pred[v].add(u)

    ts = TopologicalSorter({i: pred[i] for i in ids})
    layer = {}
    for n in ts.static_order():
        layer[n] = max((layer[p] + 1 for p in pred[n]), default=0)
    return layer, pred


def build(graph):
    direction = graph.get("direction", "TB").upper()
    roughness = int(graph.get("roughness", 1))
    font = int(graph.get("font", 1))
    nodes = graph.get("nodes") or []
    edges = graph.get("edges", [])
    if not nodes:
        raise SystemExit("graph has no nodes")
    ids = [n["id"] for n in nodes]
    dup = {i for i in ids if ids.count(i) > 1}
    if dup:
        raise SystemExit(f"duplicate node ids: {sorted(dup)}")
    meta = {n["id"]: n for n in nodes}

    # load images: node pictures and free-placed pictures share one files map
    files = {}
    imgplan = {}  # nid -> {fileId, iw, ih}

    def add_file(src):
        fid, url, mime, aspect = load_image(src)
        files[fid] = {"id": fid, "dataURL": url, "mimeType": mime,
                      "created": 1, "lastRetrieved": 1}
        return fid, aspect

    for n in nodes:
        if n.get("image"):
            fid, aspect = add_file(n["image"])
            iw, ih = fit(aspect, ICON)
            imgplan[n["id"]] = {"fileId": fid, "iw": int(iw), "ih": int(ih)}

    free_imgs = []
    for im in graph.get("images", []):
        fid, aspect = add_file(im["src"])
        w, h = im.get("width"), im.get("height")
        if w and not h:
            h = w / aspect
        elif h and not w:
            w = h * aspect
        elif not w and not h:
            w, h = 120, 120 / aspect
        free_imgs.append({"fileId": fid, "x": im["x"], "y": im["y"], "w": int(w), "h": int(h)})

    layer, pred = layer_nodes(ids, edges)
    # group by layer, order by barycenter of parents
    layers = {}
    for i in ids:
        layers.setdefault(layer[i], []).append(i)
    maxL = max(layers) if layers else 0
    pos = {}  # id -> index within its layer
    for L in range(maxL + 1):
        row = layers.get(L, [])
        if L == 0:
            row.sort(key=lambda i: ids.index(i))
        else:
            row.sort(key=lambda i: (sum(pos.get(p, 0) for p in pred[i]) / len(pred[i]))
                     if pred[i] else ids.index(i))
        for idx, i in enumerate(row):
            pos[i] = idx
        layers[L] = row

    def size_of(n):
        if n["id"] in imgplan:
            p = imgplan[n["id"]]
            iw, ih = p["iw"], p["ih"]
            if n.get("label"):
                lw = int(len(n["label"]) * FONT_SIZE * 0.6)
                return max(iw, lw), ih + LABEL_GAP + int(FONT_SIZE * LINE_H)
            return iw, ih
        return node_size(n.get("label", ""), n.get("shape", "rectangle"))

    sizes = {n["id"]: size_of(n) for n in nodes}

    # assign coordinates. cross = within-layer axis, depth = layer axis
    coord = {}
    cross_cursor = {}
    # compute each layer's total cross extent to center it
    layer_extent = {}
    for L, row in layers.items():
        layer_extent[L] = sum(sizes[i][0 if direction == "TB" else 1] for i in row) + GAP_WITHIN * max(0, len(row) - 1)
    max_extent = max(layer_extent.values()) if layer_extent else 0
    depth_cursor = 0
    for L in range(maxL + 1):
        row = layers.get(L, [])
        layer_depth = max((sizes[i][1 if direction == "TB" else 0] for i in row), default=0)
        cross = (max_extent - layer_extent.get(L, 0)) / 2
        for i in row:
            w, h = sizes[i]
            if direction == "TB":
                coord[i] = (cross, depth_cursor, w, h)
                cross += w + GAP_WITHIN
            else:
                coord[i] = (depth_cursor, cross, w, h)
                cross += h + GAP_WITHIN
        depth_cursor += layer_depth + GAP_BETWEEN

    return emit(meta, coord, edges, direction, roughness, font, imgplan, free_imgs, files)


def emit(meta, coord, edges, direction, roughness, font, imgplan, free_imgs, files):
    rnd = random.Random(7)
    def seed(): return rnd.randint(1, 2**31)
    els = []

    def base(t, x, y, w, h):
        return {
            "id": None, "type": t, "x": x, "y": y, "width": w, "height": h,
            "angle": 0, "strokeColor": "#1e1e1e", "backgroundColor": "transparent",
            "fillStyle": "solid", "strokeWidth": 2, "strokeStyle": "solid",
            "roughness": roughness, "opacity": 100, "groupIds": [], "frameId": None,
            "roundness": None, "seed": seed(), "version": 1, "versionNonce": seed(),
            "isDeleted": False, "boundElements": [], "updated": 1, "link": None, "locked": False,
        }

    th = int(FONT_SIZE * LINE_H)
    idmap = {}
    for nid, (x, y, w, h) in coord.items():
        n = meta[nid]
        eid = f"n_{nid}"
        idmap[nid] = eid
        label = n.get("label", "")

        if nid in imgplan:  # image node: picture on top, caption below
            p = imgplan[nid]
            iw, ih = p["iw"], p["ih"]
            el = base("image", x + (w - iw) / 2, y, iw, ih)
            el["id"] = eid
            el["fileId"] = p["fileId"]
            el["status"] = "saved"
            el["scale"] = [1, 1]
            el["crop"] = None
            els.append(el)
            if label:
                tw = int(len(label) * FONT_SIZE * 0.6) or FONT_SIZE
                t = base("text", x + (w - tw) / 2, y + ih + LABEL_GAP, tw, th)
                t.update({
                    "id": f"t_{nid}", "fontSize": FONT_SIZE, "fontFamily": font,
                    "text": label, "textAlign": "center", "verticalAlign": "top",
                    "originalText": label, "lineHeight": LINE_H, "autoResize": True,
                })
                els.append(t)
            continue

        shape = n.get("shape", "rectangle")
        el = base(shape if shape in SIZE else "rectangle", x, y, w, h)
        el["id"] = eid
        el["backgroundColor"] = PALETTE.get(shape, "#ffffff")
        el["roundness"] = {"type": 3} if shape == "rectangle" else None
        tid = f"t_{nid}"
        el["boundElements"] = [{"type": "text", "id": tid}]
        els.append(el)
        # bound label
        tw = int(len(label) * FONT_SIZE * 0.6) or FONT_SIZE
        t = base("text", x + (w - tw) / 2, y + (h - th) / 2, tw, th)
        t.update({
            "id": tid, "fontSize": FONT_SIZE, "fontFamily": font, "text": label,
            "textAlign": "center", "verticalAlign": "middle", "containerId": eid,
            "originalText": label, "lineHeight": LINE_H, "autoResize": True,
        })
        els.append(t)

    def abox(nid):  # box arrows attach to: the icon itself for image nodes
        x, y, w, h = coord[nid]
        if nid in imgplan:
            p = imgplan[nid]
            return x + (w - p["iw"]) / 2, y, p["iw"], p["ih"]
        return x, y, w, h

    for k, e in enumerate(edges):
        if e["from"] not in coord or e["to"] not in coord:
            continue
        if direction == "TB":  # full box: exit below caption, enter at icon top
            sx, sy, sw, sh = coord[e["from"]]
            ex, ey, ew, eh = coord[e["to"]]
            p0 = (sx + sw / 2, sy + sh)
            p1 = (ex + ew / 2, ey)
        else:  # attach to icon edges so arrows touch the picture
            sx, sy, sw, sh = abox(e["from"])
            ex, ey, ew, eh = abox(e["to"])
            p0 = (sx + sw, sy + sh / 2)
            p1 = (ex, ey + eh / 2)
        aid = f"a_{k}"
        a = base("arrow", p0[0], p0[1], abs(p1[0] - p0[0]), abs(p1[1] - p0[1]))
        a["id"] = aid
        a["points"] = [[0, 0], [p1[0] - p0[0], p1[1] - p0[1]]]
        a["startBinding"] = {"elementId": idmap[e["from"]], "focus": 0, "gap": 4}
        a["endBinding"] = {"elementId": idmap[e["to"]], "focus": 0, "gap": 4}
        a["startArrowhead"] = None
        a["endArrowhead"] = "arrow"
        a["lastCommittedPoint"] = None
        a["elbowed"] = False
        # register on nodes so excalidraw re-routes on edit
        for el in els:
            if el["id"] == idmap[e["from"]] or el["id"] == idmap[e["to"]]:
                el["boundElements"].append({"type": "arrow", "id": aid})
        lbl = e.get("label")
        if lbl:
            ltid = f"al_{k}"
            tw = int(len(lbl) * FONT_SIZE * 0.6) or FONT_SIZE
            t = base("text", (p0[0] + p1[0]) / 2, (p0[1] + p1[1]) / 2, tw, int(FONT_SIZE * LINE_H))
            t.update({
                "id": ltid, "fontSize": FONT_SIZE, "fontFamily": font, "text": lbl,
                "textAlign": "center", "verticalAlign": "middle", "containerId": aid,
                "originalText": lbl, "lineHeight": LINE_H, "autoResize": True,
            })
            a["boundElements"].append({"type": "text", "id": ltid})
            els.append(a)
            els.append(t)
        else:
            els.append(a)

    for k, fi in enumerate(free_imgs):
        el = base("image", fi["x"], fi["y"], fi["w"], fi["h"])
        el["id"] = f"img_{k}"
        el["fileId"] = fi["fileId"]
        el["status"] = "saved"
        el["scale"] = [1, 1]
        el["crop"] = None
        els.append(el)

    return {
        "type": "excalidraw", "version": 2, "source": "skill:excalidraw-diagram",
        "elements": els, "appState": {"gridSize": None, "viewBackgroundColor": "#ffffff"},
        "files": files,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input", nargs="?", help="graph JSON file; omit to read stdin")
    ap.add_argument("-o", "--out", help="output .excalidraw path; omit for stdout")
    a = ap.parse_args()
    raw = open(a.input).read() if a.input else sys.stdin.read()
    doc = build(json.loads(raw))
    out = json.dumps(doc, indent=2)
    if a.out:
        open(a.out, "w").write(out)
        print(a.out)
    else:
        sys.stdout.write(out)


if __name__ == "__main__":
    main()
