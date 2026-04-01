---
name: gh-pr
description: Create a new branch, commit changes, push to remote, and open a GitHub PR targeting main. Use when the user wants to create a pull request, submit work for review, or says "PR", "pull request", "open a PR", "submit PR".
hooks:
  PreToolUse:
    - matcher: Bash
      hooks:
        - type: command
          command: $HOME/.claude/skills/gh-pr/scripts/pre-pr-check.sh
---

# GitHub Pull Request Workflow

## Workflow

### 1. Review Changes

- Run `git status` and `git diff` to understand what changed.
- If there are no changes (clean working tree, nothing staged), abort and inform the user.

### 2. Branch Setup

Check the current branch with `git branch --show-current`:

**If on `main`:**
1. Create and switch to a new branch: `git checkout -b feat/<scope>-<description>`

**If NOT on `main`:**
1. Stash uncommitted changes: `git stash`
2. Remember the current branch name for cleanup later.
3. Switch to main and pull latest: `git checkout main && git pull origin main`
4. Create and switch to a new branch from main: `git checkout -b feat/<scope>-<description>`
5. Restore changes: `git stash pop`

### 3. Update Documentation

- If changes affect usage, setup, or public-facing behavior, update `README.md`.

### 4. Stage and Commit

- Stage changes with `git add` — prefer adding specific files by name over `git add .`, to avoid staging sensitive files (.env, credentials, large binaries).
- Commit message uses conventional commit format: `feat(<scope>): <description>` with bullet points summarizing the changes in the body.
- Do not include "Co-Authored-By" lines.

### 5. Push

- Push the new branch to remote: `git push -u origin <branch-name>`

### 6. Create PR

- Use `gh pr create` targeting `main`.
- PR title: short, under 70 characters, matching the commit message subject.
- PR body format:

```
## Summary
- <bullet points describing changes>

## Tests
- [ ] <checklist item>
- [ ] ...
```

- The Tests section MUST use `- [ ]` checkbox format so reviewers can tick them off.
- If a test item has already been verified during the PR workflow (e.g., you ran a command and confirmed it works), mark it as checked: `- [x]`.
- Before running `gh pr create`, print the draft PR body and ask the user to confirm or revise it. Do not create the PR without explicit user approval.
- Add additional sections only when genuinely needed (e.g., Breaking Changes, Migration).
- After `gh pr create` completes, print the PR URL to the user so they can open it directly in the browser.

## Branch Naming

- Format: `feat/<scope>-<short-description>`, all lowercase, hyphens for spaces.
- `<scope>` is a short module or area name (e.g., `auth`, `api`, `ui`).
- Examples: `feat/auth-add-oauth`, `feat/api-pagination`, `feat/ui-dark-mode`

## Rules

- Always review the diff before committing — no blind commits.
- Never force push.
- Never push directly to main — always go through a PR.
- Keep PR scope focused — one logical change per PR.

## Anti-patterns

- Do not use `git add .` or `git add -A` without checking for sensitive files first.
- Do not create a PR with an empty or generic body like "update" or "fix stuff".
- Do not skip the diff review step.
