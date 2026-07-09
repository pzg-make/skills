---
name: harness-engineering
description: General-purpose Harness engineering workflow for making repositories AI Coding Agent ready. Use when an AI coding tool is asked to add, improve, standardize, or generate project harnesses such as AGENTS.md, ARCHITECTURE.md, structured docs, build/test/lint scripts, bug reproduction scripts, validation rules, agent workflows, CI-ready command entry points, or onboarding rules for a new or poorly documented project.
---

# Harness Engineering

## Goal

Turn a repository into an Agent-ready project: clear entry points, scoped rules, structured docs, reproducible commands, validation paths, safety boundaries, and reviewable workflows.

Harness work is not feature development. It creates the operating environment that lets future AI Coding Agents understand the project, make small changes, verify them, and explain them without relying on hidden knowledge.

## Default Workflow

1. Inspect the repository before writing files:
   - root files: README, build manifests, package managers, CI configs, Docker files, existing AGENTS or architecture docs.
   - source modules and entry points.
   - test directories and commands.
   - docs and scripts already present.
   - git status, because unrelated user changes must not be touched.
2. Infer the project type and module boundaries from actual files, not from guesses.
3. Add or update the smallest useful Harness layer:
   - `AGENTS.md` as the Agent entry point and rule index.
   - `ARCHITECTURE.md` as a concise module and data-flow map.
   - `docs/` topic indexes when docs are missing or scattered.
   - `scripts/` command wrappers for lint, build, test, and reproduce-bug.
4. Preserve existing docs and scripts. Prefer indexes and links over mass-moving files.
5. Run lightweight validation after changes. At minimum run whitespace/diff checks and script syntax checks when scripts are added.
6. Explain what was generated, how to use it, what was verified, and what remains project-specific.

## File Set

Create these files only when they are missing or clearly incomplete. Update existing files in place when they already serve the same purpose.

```text
AGENTS.md
ARCHITECTURE.md
docs/
  README.md
  product/README.md
  api/README.md
  database/README.md
  frontend/README.md
  backend/README.md
  testing/README.md
  troubleshooting/README.md
scripts/
  lint.sh
  build.sh
  test.sh
  reproduce-bug.sh
```

Adapt the exact docs categories to the project. For example, omit `frontend/` for backend-only libraries, or add `ops/` for infrastructure-heavy repos.

## AGENTS.md Requirements

Keep `AGENTS.md` short. Treat it as a table of contents and operating contract, not an encyclopedia.

Include:

- project goal in one paragraph.
- non-negotiable rules: read first, keep changes scoped, protect user changes, validate, avoid unrelated rewrites.
- project entry points: app entry files, build manifests, config, schema, API docs, architecture doc.
- module boundaries and ownership.
- common commands.
- task workflows for bug fixes, requirements, tests, reviews, and docs.
- project-specific safety notes such as production data, billing, auth, migrations, or third-party services.

Do not include large API docs, schema dumps, long histories, or copied README content. Link to `docs/` instead.

## ARCHITECTURE.md Requirements

Write a concise map of the current system:

- runtime and framework.
- module list and responsibilities.
- request, job, event, or data flow.
- important external services and storage.
- deprecated modules or ignored directories.
- validation strategy.

Mark uncertain inferences explicitly. If a directory looks deprecated, do not call it active unless confirmed by manifests, imports, CI, or user instruction.

## Script Requirements

Prefer simple shell wrappers that make commands discoverable and overrideable:

- `scripts/lint.sh`: formatting, static checks, or at least `git diff --check`.
- `scripts/build.sh`: compile/package the default app or selected module.
- `scripts/test.sh`: run all tests or a selected test.
- `scripts/reproduce-bug.sh`: stable entry point for a focused bug reproduction.

Use environment variables for common variation:

```bash
MODULE=server TEST=SomeRegressionTest ./scripts/test.sh
PACKAGE=web ./scripts/build.sh
```

Do not invent dependencies. Use the package manager, build tool, and test runner already present in the repo.

## Automation Script

This skill includes `scripts/generate_harness.py`.

Use it when a project has little or no Harness structure and the user wants automatic generation. Run from any repository root:

```bash
python3 <skills-dir>/harness-engineering/scripts/generate_harness.py /path/to/repo
```

Options:

```bash
python3 <skills-dir>/harness-engineering/scripts/generate_harness.py /path/to/repo --force
python3 <skills-dir>/harness-engineering/scripts/generate_harness.py /path/to/repo --project-name "My Project"
```

Behavior:

- creates missing files and directories only.
- skips existing files unless `--force` is passed.
- detects common Java/Maven, Gradle, Node, Python, Go, Rust, and generic projects.
- writes conservative command wrappers based on detected manifests.

After running the script, read the generated files and tighten project-specific sections with facts from the repository.

## Git And Ignore Policy

Before generating files, decide with the user whether Harness files should be committed or kept local. If the user does not specify, assume they are intended to be committed because Harness value usually comes from versioning.

If the user says they should be local-only:

- do not delete generated files.
- add precise ignore rules for the generated entry points.
- avoid broad ignore rules that hide real source files.

## Validation

Run checks proportional to the generated content:

```bash
git diff --check
bash -n scripts/*.sh
```

For project-specific wrappers, run the lightest command that proves the wrapper is wired correctly. Avoid full builds when Harness-only changes do not need them, unless the user asks.

## Final Response

Report:

- files created or updated.
- whether files are committed-intended or local-only.
- validation performed.
- remaining assumptions that should be filled in from product, API, database, deployment, or team knowledge.
