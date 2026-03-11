---
name: git-push
description: Pushes the current branch to the remote repository.
---

# Git Push Procedure

1. Run `git diff` and `git status` to review changes.
2. Update documentation (e.g., `README.md`) if the changes affect usage, setup, or public-facing behavior.
3. Stage changes with `git add` — prefer adding specific files by name rather than `git add .`, to avoid accidentally staging sensitive files (`.env`, credentials, large binaries). Use `git add .` only when you are confident no sensitive files are present.
4. Write a commit message with bullet points summarizing the changes. Do not include "Co-Authored-By" lines.
5. Push to remote:
   - If the current branch has a remote tracking branch: `git push`
   - If it does not (new branch): `git push -u origin <branch-name>`