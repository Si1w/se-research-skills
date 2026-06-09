// Render a .excalidraw file to PNG.
// build.py already placed every element with absolute coordinates, so we draw
// a clean SVG from those coordinates and screenshot it with headless Chromium.
// Faithful to excalidraw at roughness 0 (the formal default); sketch wobble at
// roughness>0 is not reproduced. The .excalidraw source keeps the full look.
import { readFileSync } from "node:fs";
import { createRequire } from "node:module";
import { execSync } from "node:child_process";

// puppeteer is a global install (npm install -g puppeteer), not vendored in the
// skill. Resolve it from the global modules dir instead of a local node_modules.
let puppeteer;
try {
  const gRequire = createRequire(execSync("npm root -g").toString().trim() + "/");
  puppeteer = gRequire("puppeteer");
} catch {
  console.error("puppeteer not found. Install it once: npm install -g puppeteer");
  process.exit(1);
}

const [, , inPath, outPath, scaleArg] = process.argv;
if (!inPath || !outPath) {
  console.error("usage: node export_png.mjs <in.excalidraw> <out.png> [scale=2]");
  process.exit(1);
}
const scale = Number(scaleArg) || 2;
const doc = JSON.parse(readFileSync(inPath, "utf8"));
const els = doc.elements.filter((e) => !e.isDeleted);
const files = doc.files || {};
const bg = doc.appState?.viewBackgroundColor || "#ffffff";

const esc = (s) =>
  String(s).replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));

// bounding box
const PAD = 24;
let minX = Infinity, minY = Infinity, maxX = -Infinity, maxY = -Infinity;
for (const e of els) {
  minX = Math.min(minX, e.x);
  minY = Math.min(minY, e.y);
  maxX = Math.max(maxX, e.x + (e.width || 0));
  maxY = Math.max(maxY, e.y + (e.height || 0));
  if (e.type === "arrow") for (const [px, py] of e.points || []) {
    minX = Math.min(minX, e.x + px); minY = Math.min(minY, e.y + py);
    maxX = Math.max(maxX, e.x + px); maxY = Math.max(maxY, e.y + py);
  }
}
minX -= PAD; minY -= PAD; maxX += PAD; maxY += PAD;
const W = maxX - minX, H = maxY - minY;

const FONT = "Helvetica, Arial, sans-serif";
const parts = [];
for (const e of els) {
  const sc = e.strokeColor || "#1e1e1e";
  const fill = e.backgroundColor && e.backgroundColor !== "transparent" ? e.backgroundColor : "none";
  const sw = e.strokeWidth || 2;
  if (e.type === "rectangle") {
    const r = e.roundness ? 12 : 0;
    parts.push(`<rect x="${e.x}" y="${e.y}" width="${e.width}" height="${e.height}" rx="${r}" fill="${fill}" stroke="${sc}" stroke-width="${sw}"/>`);
  } else if (e.type === "ellipse") {
    parts.push(`<ellipse cx="${e.x + e.width / 2}" cy="${e.y + e.height / 2}" rx="${e.width / 2}" ry="${e.height / 2}" fill="${fill}" stroke="${sc}" stroke-width="${sw}"/>`);
  } else if (e.type === "diamond") {
    const cx = e.x + e.width / 2, cy = e.y + e.height / 2;
    const pts = `${cx},${e.y} ${e.x + e.width},${cy} ${cx},${e.y + e.height} ${e.x},${cy}`;
    parts.push(`<polygon points="${pts}" fill="${fill}" stroke="${sc}" stroke-width="${sw}"/>`);
  } else if (e.type === "arrow") {
    const pts = (e.points || []).map(([px, py]) => `${e.x + px},${e.y + py}`).join(" ");
    parts.push(`<polyline points="${pts}" fill="none" stroke="${sc}" stroke-width="${sw}" marker-end="url(#ah)"/>`);
  } else if (e.type === "image") {
    const url = files[e.fileId]?.dataURL;
    if (url) parts.push(`<image x="${e.x}" y="${e.y}" width="${e.width}" height="${e.height}" href="${url}" preserveAspectRatio="xMidYMid meet"/>`);
  } else if (e.type === "text") {
    const cx = e.x + e.width / 2, cy = e.y + e.height / 2;
    const onArrow = typeof e.containerId === "string" && e.containerId.startsWith("a_");
    if (onArrow) {
      parts.push(`<rect x="${e.x - 2}" y="${e.y - 1}" width="${e.width + 4}" height="${e.height + 2}" fill="${bg}"/>`);
    }
    parts.push(`<text x="${cx}" y="${cy}" font-family="${FONT}" font-size="${e.fontSize || 20}" fill="${sc}" text-anchor="middle" dominant-baseline="central">${esc(e.text)}</text>`);
  }
}

const svg = `<svg xmlns="http://www.w3.org/2000/svg" width="${W}" height="${H}" viewBox="${minX} ${minY} ${W} ${H}">
<defs><marker id="ah" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto" markerUnits="strokeWidth">
<path d="M0,0 L8,3 L0,6 Z" fill="#1e1e1e"/></marker></defs>
<rect x="${minX}" y="${minY}" width="${W}" height="${H}" fill="${bg}"/>
${parts.join("\n")}
</svg>`;

const browser = await puppeteer.launch({ headless: true, args: ["--no-sandbox"] });
try {
  const page = await browser.newPage();
  await page.setViewport({ width: Math.ceil(W), height: Math.ceil(H), deviceScaleFactor: scale });
  await page.setContent(`<!doctype html><html><body style="margin:0">${svg}</body></html>`, { waitUntil: "networkidle0" });
  await page.screenshot({ path: outPath, omitBackground: false });
  console.log(outPath);
} finally {
  await browser.close();
}
