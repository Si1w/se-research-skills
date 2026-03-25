"""Access Zotero library for research idea validation.

Uses Better-BibTeX JSON-RPC for search and metadata,
SQLite (via temp copy) for notes and annotations.

Usage:
    uv run python rp-generate/scripts/zotero.py search "LLM code generation"
    uv run python rp-generate/scripts/zotero.py search "agent" --collection Interest
    uv run python rp-generate/scripts/zotero.py collections
    uv run python rp-generate/scripts/zotero.py get <citation-key>
"""

import argparse
import json
import os
import re
import shutil
import sqlite3
import sys
import tempfile
from html.parser import HTMLParser
from pathlib import Path

import requests

BIBTEX_RPC = "http://localhost:23119/better-bibtex/json-rpc"
ZOTERO_DB = Path.home() / "Zotero" / "zotero.sqlite"


class HTMLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []

    def handle_data(self, data):
        self.parts.append(data)

    def get_text(self):
        return "".join(self.parts).strip()


def strip_html(html: str) -> str:
    s = HTMLStripper()
    s.feed(html)
    return s.get_text()


def rpc_call(method: str, params: list) -> dict:
    resp = requests.post(
        BIBTEX_RPC,
        json={"jsonrpc": "2.0", "method": method, "params": params, "id": 1},
        timeout=10,
    )
    resp.raise_for_status()
    data = resp.json()
    if "error" in data:
        print(f"RPC error: {data['error']}", file=sys.stderr)
        sys.exit(1)
    return data["result"]


class ZoteroDB:
    """Copy Zotero SQLite to temp file (avoids lock). Use as context manager."""

    def __init__(self):
        self.tmp = tempfile.mktemp(suffix=".sqlite")
        shutil.copy2(ZOTERO_DB, self.tmp)
        self.conn = sqlite3.connect(self.tmp)
        self.conn.row_factory = sqlite3.Row

    def __enter__(self):
        return self.conn

    def __exit__(self, *args):
        self.conn.close()
        os.unlink(self.tmp)


def get_notes(conn: sqlite3.Connection, item_keys: list[str]) -> dict[str, list[str]]:
    """Get notes for items by their Zotero keys."""
    if not item_keys:
        return {}
    conn2 = conn
    cursor = conn2.cursor()
    notes_by_key = {}
    for key in item_keys:
        cursor.execute(
            """
            SELECT n.note FROM itemNotes n
            JOIN items parent ON n.parentItemID = parent.itemID
            WHERE parent.key = ?
            """,
            (key,),
        )
        rows = cursor.fetchall()
        if rows:
            notes_by_key[key] = [strip_html(r["note"]) for r in rows if r["note"]]
    return notes_by_key


def get_collections_map(conn: sqlite3.Connection) -> dict[int, str]:
    """Map collectionID -> collectionName."""
    cursor = conn.cursor()
    cursor.execute("SELECT collectionID, collectionName FROM collections")
    return {r["collectionID"]: r["collectionName"] for r in cursor.fetchall()}


def get_item_collections(
    conn: sqlite3.Connection, item_keys: list[str]
) -> dict[str, list[str]]:
    """Get collection names for items."""
    if not item_keys:
        return {}
    coll_map = get_collections_map(conn)
    cursor = conn.cursor()
    result = {}
    for key in item_keys:
        cursor.execute(
            """
            SELECT ci.collectionID FROM collectionItems ci
            JOIN items i ON ci.itemID = i.itemID
            WHERE i.key = ?
            """,
            (key,),
        )
        cols = [coll_map[r["collectionID"]] for r in cursor.fetchall() if r["collectionID"] in coll_map]
        if cols:
            result[key] = cols
    return result


def extract_key(item: dict) -> str:
    """Extract Zotero key from item ID URL."""
    item_id = item.get("id", "")
    return item_id.rsplit("/", 1)[-1] if "/" in item_id else item_id


def format_item(item: dict, notes: list[str] | None = None, collections: list[str] | None = None) -> dict:
    """Format a BibTeX item for output."""
    authors = item.get("author", [])
    author_str = "; ".join(
        f"{a.get('family', '')}, {a.get('given', '')}" for a in authors
    )
    issued = item.get("issued", {})
    year = ""
    if "date-parts" in issued and issued["date-parts"]:
        year = str(issued["date-parts"][0][0]) if issued["date-parts"][0] else ""

    result = {
        "citation_key": item.get("citation-key", ""),
        "title": item.get("title", ""),
        "authors": author_str,
        "year": year,
        "type": item.get("type", ""),
    }
    if item.get("abstract"):
        result["abstract"] = item["abstract"]
    if item.get("DOI"):
        result["doi"] = item["DOI"]
    if item.get("URL"):
        result["url"] = item["URL"]
    if collections:
        result["collections"] = collections
    if notes:
        result["notes"] = notes
    return result


def cmd_search(args):
    items = rpc_call("item.search", [args.query])
    if not items:
        print("[]")
        return

    with ZoteroDB() as conn:
        keys = [extract_key(it) for it in items]
        cols_map = get_item_collections(conn, keys)

        if args.collection:
            col_lower = args.collection.lower()
            items = [
                it for it in items
                if extract_key(it) in cols_map
                and any(c.lower() == col_lower for c in cols_map[extract_key(it)])
            ]
            keys = [extract_key(it) for it in items]

        notes_map = get_notes(conn, keys)

    results = [
        format_item(it, notes_map.get(extract_key(it)), cols_map.get(extract_key(it)))
        for it in items
    ]
    print(json.dumps(results, indent=2, ensure_ascii=False))


def cmd_get(args):
    items = rpc_call("item.search", [args.citation_key])
    match = next((it for it in items if it.get("citation-key") == args.citation_key), None)
    if not match:
        print(f"Not found: {args.citation_key}", file=sys.stderr)
        sys.exit(1)

    key = extract_key(match)
    with ZoteroDB() as conn:
        notes_map = get_notes(conn, [key])
        cols_map = get_item_collections(conn, [key])

    result = format_item(match, notes_map.get(key), cols_map.get(key))
    print(json.dumps(result, indent=2, ensure_ascii=False))


def cmd_collections(args):
    with ZoteroDB() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT c.collectionName, COUNT(ci.itemID) as count
            FROM collections c
            LEFT JOIN collectionItems ci ON c.collectionID = ci.collectionID
            GROUP BY c.collectionID
            ORDER BY c.collectionName
            """
        )
        for row in cursor.fetchall():
            print(f"  {row['collectionName']} ({row['count']} items)")


def main():
    parser = argparse.ArgumentParser(description="Access Zotero library")
    sub = parser.add_subparsers(dest="command", required=True)

    p_search = sub.add_parser("search", help="Search papers by keyword")
    p_search.add_argument("query", help="Search query")
    p_search.add_argument("--collection", "-c", help="Filter by collection name")
    p_search.set_defaults(func=cmd_search)

    p_get = sub.add_parser("get", help="Get paper by citation key")
    p_get.add_argument("citation_key", help="Citation key (e.g., sunDAREAligningLLM2026)")
    p_get.set_defaults(func=cmd_get)

    p_cols = sub.add_parser("collections", help="List collections")
    p_cols.set_defaults(func=cmd_collections)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
