# Git and GitHub Working Guide

## Purpose

This guide records the small set of Git and GitHub commands I currently use.
It is an operating checklist for reviewing, preserving, and publishing project
work safely. Commands outside this workflow can be learned when a real need
appears.

## The Basic Mental Model

Git manages project history locally on Serval. GitHub stores a published remote
copy of that history.

```text
Working files
    │ git add
    ▼
Staging area
    │ git commit
    ▼
Local Git repository
    │ git push
    ▼
GitHub remote repository
```

Each step has a separate job:

- Editing changes working files.
- `git add` selects an exact snapshot for the next commit.
- `git commit` preserves the staged snapshot in local history.
- `git push` publishes local commits to GitHub.

## Daily Workflow

Use this order for normal project work:

1. Confirm the project directory, Python environment, and Git state.
2. Edit one bounded change.
3. Compile and test the code.
4. Inspect the changed files.
5. Stage exact intended files.
6. Verify the staged snapshot.
7. Commit with a short outcome-based message.
8. Push the commit to GitHub.
9. Confirm that local and remote branches are synchronized.

## Inspect Changes

Check the detailed repository state:

```bash
git status
```

Check the compact branch and synchronization state:

```bash
git status -sb
```

Show tracked changes that have not been staged:

```bash
git --no-pager diff
```

Check tracked unstaged changes for whitespace errors:

```bash
git diff --check
```

Show the latest commit:

```bash
git --no-pager log -1 --oneline
```

A clean synchronized result usually looks like:

```text
## main...origin/main
```

## Stage and Verify

Stage only the intended files:

```bash
git add path/to/file
```

Example:

```bash
git add README.md tests/test_health_report.py
```

Show the exact staged content intended for the next commit:

```bash
git --no-pager diff --cached
```

Check the staged snapshot for whitespace errors:

```bash
git diff --cached --check
```

Show a compact staged-change summary:

```bash
git --no-pager diff --cached --stat
```

Confirm which files are staged:

```bash
git status
```

The staging area contains a snapshot. If a staged file is edited again, run
`git add` on that file again to update the staged snapshot.

## Commit and Publish

Create a local commit with an outcome-based message:

```bash
git commit -m "Add controlled uptime test"
```

Publish local commits to the configured GitHub remote:

```bash
git push
```

A commit preserves work locally. A push publishes commits remotely. Committing
does not automatically update GitHub.

## Confirm the Final State

Verify branch synchronization:

```bash
git status -sb
```

Verify the latest commit:

```bash
git --no-pager log -1 --oneline
```

Common compact states:

```text
## main...origin/main
```

Local and remote branches are synchronized.

```text
## main...origin/main [ahead 1]
```

One local commit has not yet been pushed.

```text
## main...origin/main [behind 1]
```

GitHub contains a commit that is not yet local. Stop and inspect before
combining histories.

## Untracked Files

An untracked file exists in the working directory but is not yet part of Git
history.

`git status` displays untracked filenames, but ordinary `git diff` does not
display their contents.

To inspect an untracked file before staging, use normal file-display tools:

```bash
nl -ba path/to/file
```

To include it in the next commit:

```bash
git add path/to/file
git --no-pager diff --cached
git diff --cached --check
```

Git does not track empty directories. A directory becomes visible to Git when
it contains a tracked file.

## Safe Corrections

Remove a file from staging without deleting its working changes:

```bash
git restore --staged path/to/file
```

After editing a staged file, update the staged snapshot:

```bash
git add path/to/file
```

Cancel a running command or development server:

```text
Ctrl+C
```

Repeating completed operations is normally harmless:

```text
git commit → nothing to commit, working tree clean
git push   → Everything up-to-date
```

A mistyped command such as `got status` normally fails without changing files.
Read the error and correct the command; do not install a suggested package
merely because a familiar command was misspelled.

## Commands to Avoid for Now

Do not casually run:

```bash
git add .
git commit -am "message"
git restore path/to/file
git reset --hard
git clean -fd
git push --force
```

Reasons:

- `git add .` can stage unrelated files.
- `git commit -am` skips untracked files and can hide the staging lesson.
- `git restore path/to/file` can discard uncommitted edits.
- `git reset --hard` can discard work across multiple files.
- `git clean -fd` can permanently delete untracked files and directories.
- `git push --force` can rewrite published history.

Use exact filenames and inspect before changing repository history or deleting
work.

## One-Time Repository Commands

Initialize Git inside a new project:

```bash
git init
```

Rename the current branch to `main`:

```bash
git branch -m main
```

Connect a local repository to an empty GitHub repository:

```bash
git remote add origin https://github.com/USERNAME/REPOSITORY.git
```

Verify the configured remote:

```bash
git remote -v
```

Publish `main` for the first time and establish tracking:

```bash
git push -u origin main
```

Copy an existing GitHub repository to a machine:

```bash
git clone https://github.com/USERNAME/REPOSITORY.git
```

These are setup operations, not commands to repeat during every daily workflow.

## Core Commands to Memorize

Focus first on these six commands:

```bash
git status
git diff
git add path/to/file
git commit -m "Describe the completed change"
git push
git log --oneline
```

Working meaning:

- `status` — What state is the repository in?
- `diff` — What changed?
- `add` — What exact files belong in the next snapshot?
- `commit` — Preserve the staged snapshot locally.
- `push` — Publish local commits to GitHub.
- `log` — What history has been preserved?

Everything else can be read from this guide until repetition makes it familiar.