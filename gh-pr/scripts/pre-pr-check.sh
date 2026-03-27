#!/bin/bash
# Pre-PR hook: block if still on main, warn if README not updated when new files are added

set -euo pipefail

INPUT=$(cat)
COMMAND=$(echo "$INPUT" | jq -r '.tool_input.command // ""')

# Only intercept gh pr create commands
if ! echo "$COMMAND" | grep -qE '^\s*gh\s+pr\s+create'; then
  exit 0
fi

BRANCH=$(git branch --show-current)

# Block creating PR from main
if [ "$BRANCH" = "main" ]; then
  echo "ERROR: Cannot create a PR directly from main. Switch to a feature branch first." >&2
  exit 2
fi

# Warn when new files were added but README was not updated
UPSTREAM="origin/main"
DIFF_STAT=$(git diff --diff-filter=A --name-only "$UPSTREAM"...HEAD 2>/dev/null || \
            git diff --diff-filter=A --name-only HEAD~1 2>/dev/null || echo "")

NEW_FILES=$(echo "$DIFF_STAT" | grep -v '^$' | grep -v '^README\.md$' || true)
README_UPDATED=$(git diff --name-only "$UPSTREAM"...HEAD 2>/dev/null | grep -q '^README\.md$' && echo "yes" || echo "no")

if [ -n "$NEW_FILES" ] && [ "$README_UPDATED" = "no" ]; then
  echo "New files added but README.md was not updated. Please verify if README needs updating:" >&2
  echo "$NEW_FILES" | sed 's/^/  - /' >&2
  exit 1
fi

exit 0
