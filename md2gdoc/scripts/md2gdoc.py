"""md2gdoc: sync a local Markdown file with a Google Doc via the Drive API.

push: convert the file body to a Google Doc (create first time, update the same
      Doc after); the Doc id is written back into the file's frontmatter.
pull: export the Doc back to Markdown, replacing the body and keeping frontmatter.
"""

import argparse
import io
import os
import sys
from pathlib import Path

import frontmatter
from google.auth.exceptions import RefreshError
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload

SCOPES = ["https://www.googleapis.com/auth/drive"]
DOC_MIME = "application/vnd.google-apps.document"
MD_MIME = "text/markdown"
HOME = Path(os.environ.get("MD2GDOC_HOME", Path.home() / ".config" / "md2gdoc"))
DOC_URL = "https://docs.google.com/document/d/{}/edit"


def service():
    """Build an authenticated Drive client. First run opens a browser for consent."""
    creds_file = HOME / "credentials.json"
    token_file = HOME / "token.json"
    if not creds_file.exists():
        sys.exit(f"Missing {creds_file}. Run GCP setup first (see references/gcp-setup.md).")
    creds = Credentials.from_authorized_user_file(token_file, SCOPES) if token_file.exists() else None
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            try:
                creds.refresh(Request())
            except RefreshError:
                creds = None  # revoked or expired past recovery; re-consent below
        if not creds or not creds.valid:
            creds = InstalledAppFlow.from_client_secrets_file(creds_file, SCOPES).run_local_server(port=0)
        token_file.write_text(creds.to_json())
    return build("drive", "v3", credentials=creds)


def push(path):
    post = frontmatter.load(path)
    media = MediaIoBaseUpload(io.BytesIO(post.content.encode("utf-8")), mimetype=MD_MIME)
    svc = service()
    gid = post.get("gdoc_id")
    if gid:
        svc.files().update(fileId=gid, media_body=media).execute()
        print("Updated " + DOC_URL.format(gid))
    else:
        title = post.get("title") or Path(path).stem
        created = svc.files().create(
            body={"name": title, "mimeType": DOC_MIME}, media_body=media, fields="id"
        ).execute()
        post["gdoc_id"] = created["id"]
        Path(path).write_text(frontmatter.dumps(post), encoding="utf-8")
        print("Created " + DOC_URL.format(created["id"]))


def pull(path):
    post = frontmatter.load(path)
    gid = post.get("gdoc_id")
    if not gid:
        sys.exit(f"No gdoc_id in {path}. Push it first, or add gdoc_id to the frontmatter.")
    data = service().files().export(fileId=gid, mimeType=MD_MIME).execute()
    post.content = data.decode("utf-8") if isinstance(data, bytes) else data
    Path(path).write_text(frontmatter.dumps(post), encoding="utf-8")
    print(f"Pulled {gid} into {path}")


def main():
    ap = argparse.ArgumentParser(description="Sync a Markdown file with a Google Doc.")
    sub = ap.add_subparsers(dest="cmd", required=True)
    for name in ("push", "pull"):
        sub.add_parser(name).add_argument("file")
    args = ap.parse_args()
    {"push": push, "pull": pull}[args.cmd](args.file)


if __name__ == "__main__":
    main()
