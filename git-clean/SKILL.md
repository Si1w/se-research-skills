---
name: git-clean
description: Clean up the current feature branch and return to main with latest changes. Use when the user says "clean branch", "delete branch", "cleanup", "back to main", "PR merged", or wants to tidy up after a PR is merged or closed.
---

# Git Branch Cleanup

Clean up the current feature branch, switch back to main, and pull latest.

## Workflow

### 1. Check Current State

- Run `git branch --show-current` to get the current branch.
- If already on `main`, just run `git pull origin main` and stop.

### 2. Check PR Status

- Run `gh pr list --head <current-branch> --state all --json number,state,title` to find the PR associated with this branch.
- If a PR exists and is **merged** or **closed**: proceed with cleanup.
- If a PR exists and is **open**: warn the user that the PR is still open, ask for confirmation before continuing.
- If no PR found: inform the user no PR was found for this branch, ask for confirmation before deleting.

### 3. Switch to Main

- `git checkout main`
- `git pull origin main`

### 4. Delete Local Branch

- `git branch -d <branch-name>`
- If `-d` fails (unmerged changes), inform the user and ask whether to force-delete with `-D`.

### 5. Delete Remote Branch

- `git push origin --delete <branch-name>`
- If the remote branch doesn't exist, skip silently.

## Rules

- Never delete `main`.
- Always check PR status before deleting — avoid deleting branches with open PRs unless the user confirms.
- Use `-d` (safe delete) first, only escalate to `-D` with user approval.

## Anti-patterns

- Do not force-delete without asking the user.
- Do not skip the PR status check.
