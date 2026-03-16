#!/bin/bash
# Pre-push hook: block push if SKILL.md changed but README.md did not

set -euo pipefail

INPUT=$(cat)
COMMAND=$(echo "$INPUT" | jq -r '.tool_input.command // ""')

# Only intercept git push commands
if ! echo "$COMMAND" | grep -qE '^\s*git\s+push'; then
  exit 0
fi

UPSTREAM=$(git rev-parse --abbrev-ref '@{upstream}' 2>/dev/null || echo "origin/main")
CHANGED_FILES=$(git diff --name-only "$UPSTREAM"...HEAD 2>/dev/null || git diff --name-only HEAD~1 2>/dev/null || echo "")

if echo "$CHANGED_FILES" | grep -qE 'SKILL\.md' && \
   ! echo "$CHANGED_FILES" | grep -q '^README\.md$'; then
  echo "SKILL.md changed but README.md was not updated. Please verify if README needs updating." >&2
  exit 2
fi

exit 0