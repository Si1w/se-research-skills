#!/bin/bash
# Pre-push hook: remind to check README when new files/directories are added

set -euo pipefail

INPUT=$(cat)
COMMAND=$(echo "$INPUT" | jq -r '.tool_input.command // ""')

# Only intercept git push commands
if ! echo "$COMMAND" | grep -qE '^\s*git\s+push'; then
  exit 0
fi

UPSTREAM=$(git rev-parse --abbrev-ref '@{upstream}' 2>/dev/null || echo "origin/main")
DIFF_STAT=$(git diff --diff-filter=A --name-only "$UPSTREAM"...HEAD 2>/dev/null || \
            git diff --diff-filter=A --name-only HEAD~1 2>/dev/null || echo "")

# Only warn when new files were added (excluding README itself) but README was not updated
NEW_FILES=$(echo "$DIFF_STAT" | grep -v '^$' | grep -v '^README\.md$' || true)
README_UPDATED=$(git diff --name-only "$UPSTREAM"...HEAD 2>/dev/null | grep -q '^README\.md$' && echo "yes" || echo "no")

if [ -n "$NEW_FILES" ] && [ "$README_UPDATED" = "no" ]; then
  echo "New files added but README.md was not updated. Please verify if README needs updating:" >&2
  echo "$NEW_FILES" | sed 's/^/  - /' >&2
  exit 1
fi

exit 0