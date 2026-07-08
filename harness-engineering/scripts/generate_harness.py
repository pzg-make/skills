#!/usr/bin/env python3
"""Generate a conservative AI Coding Agent harness for a repository."""

from __future__ import annotations

import argparse
import os
import stat
from pathlib import Path


DOC_TOPICS = {
    "product": "Business goals, user scenarios, scope, acceptance criteria, risks, rollout, and rollback notes.",
    "api": "HTTP, WebSocket, RPC, CLI, SDK, and webhook contracts with request and response examples.",
    "database": "Schemas, migrations, indexes, data fixes, compatibility notes, and rollback SQL.",
    "frontend": "Frontend or client integration notes, UI states, routing, assets, and compatibility.",
    "backend": "Backend module boundaries, services, jobs, events, configuration, and third-party integrations.",
    "testing": "Test strategy, commands, fixtures, regression scenarios, and manual verification checklists.",
    "troubleshooting": "Bug reproduction notes, logs, incident patterns, runbooks, and diagnostic checklists.",
}


def detect_project(root: Path) -> dict:
    files = {p.name for p in root.iterdir() if p.is_file()}
    dirs = {p.name for p in root.iterdir() if p.is_dir()}
    modules = []
    kind = "generic"

    if "pom.xml" in files:
        kind = "java-maven"
        modules = [p.name for p in root.iterdir() if p.is_dir() and (p / "pom.xml").exists()]
    elif "build.gradle" in files or "build.gradle.kts" in files or "settings.gradle" in files or "settings.gradle.kts" in files:
        kind = "java-gradle"
        modules = [p.name for p in root.iterdir() if p.is_dir() and ((p / "build.gradle").exists() or (p / "build.gradle.kts").exists())]
    elif "package.json" in files:
        kind = "node"
    elif "pyproject.toml" in files or "requirements.txt" in files or "setup.py" in files:
        kind = "python"
    elif "go.mod" in files:
        kind = "go"
    elif "Cargo.toml" in files:
        kind = "rust"

    source_dirs = sorted(name for name in dirs if name in {"src", "app", "apps", "packages", "services", "lib", "server", "client", "web", "api"})
    test_dirs = sorted(name for name in dirs if name in {"test", "tests", "__tests__", "spec", "e2e"})

    return {
        "kind": kind,
        "modules": modules,
        "source_dirs": source_dirs,
        "test_dirs": test_dirs,
        "has_frontend": "package.json" in files or any(name in dirs for name in {"web", "client", "frontend", "apps"}),
    }


def write_file(path: Path, content: str, force: bool) -> bool:
    if path.exists() and not force:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")
    return True


def make_executable(path: Path) -> None:
    current = path.stat().st_mode
    path.chmod(current | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)


def module_lines(info: dict) -> str:
    if info["modules"]:
        return "\n".join(f"- `{name}`: TODO: describe this module's responsibility." for name in info["modules"])
    if info["source_dirs"]:
        return "\n".join(f"- `{name}`: TODO: describe this source area." for name in info["source_dirs"])
    return "- TODO: list the important modules, packages, services, apps, or libraries."


def command_block(info: dict) -> str:
    kind = info["kind"]
    if kind == "java-maven":
        return """```bash
./scripts/lint.sh
./scripts/build.sh
./scripts/test.sh
MODULE=module-name TEST=SomeTest ./scripts/test.sh
```"""
    if kind == "java-gradle":
        return """```bash
./scripts/lint.sh
./scripts/build.sh
./scripts/test.sh
TASK=:module:test ./scripts/test.sh
```"""
    if kind == "node":
        return """```bash
./scripts/lint.sh
./scripts/build.sh
./scripts/test.sh
```"""
    if kind == "python":
        return """```bash
./scripts/lint.sh
./scripts/build.sh
./scripts/test.sh
TEST=tests/test_example.py ./scripts/test.sh
```"""
    if kind == "go":
        return """```bash
./scripts/lint.sh
./scripts/build.sh
./scripts/test.sh
```"""
    if kind == "rust":
        return """```bash
./scripts/lint.sh
./scripts/build.sh
./scripts/test.sh
```"""
    return """```bash
./scripts/lint.sh
./scripts/build.sh
./scripts/test.sh
```"""


def ag_text(project_name: str, info: dict) -> str:
    return f"""# AGENTS.md

## Project Goal

`{project_name}` is a `{info["kind"]}` project. TODO: replace this paragraph with the product or technical goal in one or two sentences.

This file is the AI Coding Agent entry point. Keep it concise and link to `docs/` for details.

## Required Rules

1. Read the relevant modules, entry points, and tests before editing.
2. Keep changes scoped to the user's request; do not perform unrelated refactors or formatting.
3. Preserve user changes. Do not delete, revert, or overwrite unrelated dirty work.
4. Prefer existing project patterns, helpers, and dependency choices.
5. Add or update tests for behavior changes and bug fixes when practical.
6. Run the narrowest useful validation before finalizing.
7. Explain what changed, how it was verified, and any remaining risk.

## Project Entry Points

- Architecture: `ARCHITECTURE.md`
- Docs index: `docs/README.md`
- Build manifest: TODO
- Main app or package entry: TODO
- Configuration: TODO
- Tests: TODO

## Module Boundaries

{module_lines(info)}

## Common Commands

{command_block(info)}

## Workflows

### Bug Fix

1. Reproduce or identify the failing path.
2. Locate root cause and affected modules.
3. Make the smallest correct fix.
4. Add or update a regression test when practical.
5. Run focused validation.
6. Report root cause, fix, and residual risk.

### Requirement Development

1. Read the requirement and similar existing implementation.
2. Identify API, data, permissions, cache, async, and client impacts.
3. Implement in small, reviewable steps.
4. Update tests and docs for user-visible behavior.
5. Run focused validation.

### Review

Prioritize behavioral regressions, compatibility, permissions, security, data consistency, missing tests, and over-broad changes.
"""


def architecture_text(project_name: str, info: dict) -> str:
    return f"""# ARCHITECTURE.md

## Overview

`{project_name}` is detected as a `{info["kind"]}` project. TODO: replace this section with the actual runtime, framework, deployment shape, and main user-facing capability.

## System Map

```text
User / Client / External caller
  -> TODO: API, UI, CLI, job, or event entry point
  -> TODO: application or service layer
  -> TODO: persistence, cache, queues, external services
```

## Modules

{module_lines(info)}

## Data And Integration Points

- Data stores: TODO
- External APIs: TODO
- Background jobs or queues: TODO
- Authentication and authorization: TODO
- Observability: TODO

## Deprecated Or Local-Only Areas

List generated artifacts, local experiments, archived modules, and directories that Agents should not use as implementation entry points.

## Validation Strategy

- Lightweight checks: `./scripts/lint.sh`
- Build: `./scripts/build.sh`
- Tests: `./scripts/test.sh`
- Bug reproduction: `./scripts/reproduce-bug.sh`

Update this section when the project gains more precise CI, integration tests, fixtures, or environment-specific validation.
"""


def docs_readme(project_name: str) -> str:
    bullets = "\n".join(f"- `{topic}/`: {description}" for topic, description in DOC_TOPICS.items())
    return f"""# {project_name} Docs

This directory stores project knowledge for engineers and AI Coding Agents.

## Sections

{bullets}

## Writing Rules

1. Prefer focused documents with clear titles.
2. Link related code, API contracts, migrations, tests, and rollout notes.
3. Keep reproduction steps, expected behavior, and validation results with bug documents.
4. Keep historical or exploratory notes separate from active implementation guidance.
"""


def topic_readme(topic: str, description: str) -> str:
    return f"""# {topic.title()}

{description}

## What To Add Here

- Current behavior and active contracts.
- Important entry points and owners.
- Compatibility and migration notes.
- Validation or troubleshooting guidance.

Keep this README as an index. Put detailed documents next to it and link them here.
"""


def shell_script(kind: str, script_name: str) -> str:
    header = """#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"
"""
    if script_name == "lint":
        if kind == "node":
            return header + """
git diff --check
if npm run | grep -q "^  lint"; then
  npm run lint
fi
"""
        if kind == "python":
            return header + """
git diff --check
if command -v ruff >/dev/null 2>&1; then
  ruff check .
fi
"""
        if kind == "go":
            return header + """
git diff --check
gofmt -w=false . >/dev/null
"""
        if kind == "rust":
            return header + """
git diff --check
cargo fmt --check
"""
        return header + "\ngit diff --check\n"

    if script_name == "build":
        if kind == "java-maven":
            return header + """
MAVEN_BIN="${MAVEN_BIN:-mvn}"
MODULE="${MODULE:-}"

if [[ -n "$MODULE" ]]; then
  exec "$MAVEN_BIN" -pl "$MODULE" -am -DskipTests compile "$@"
fi

exec "$MAVEN_BIN" -DskipTests compile "$@"
"""
        if kind == "java-gradle":
            return header + """
GRADLE_BIN="${GRADLE_BIN:-./gradlew}"
if [[ ! -x "$GRADLE_BIN" ]]; then
  GRADLE_BIN="${GRADLE_BIN:-gradle}"
fi
TASK="${TASK:-build}"
exec "$GRADLE_BIN" "$TASK" -x test "$@"
"""
        if kind == "node":
            return header + """
if npm run | grep -q "^  build"; then
  exec npm run build -- "$@"
fi
echo "No npm build script found." >&2
exit 2
"""
        if kind == "python":
            return header + """
if [[ -f pyproject.toml ]]; then
  python3 -m build "$@"
else
  python3 -m compileall . "$@"
fi
"""
        if kind == "go":
            return header + '\nexec go build ./... "$@"\n'
        if kind == "rust":
            return header + '\nexec cargo build "$@"\n'
        return header + '\necho "No build command configured yet." >&2\nexit 2\n'

    if script_name == "test":
        if kind == "java-maven":
            return header + """
MAVEN_BIN="${MAVEN_BIN:-mvn}"
MODULE="${MODULE:-}"
TEST="${TEST:-}"

ARGS=(test)
if [[ -n "$TEST" ]]; then
  ARGS=(-Dtest="$TEST" test)
fi

if [[ -n "$MODULE" ]]; then
  exec "$MAVEN_BIN" -pl "$MODULE" "${ARGS[@]}" "$@"
fi

exec "$MAVEN_BIN" "${ARGS[@]}" "$@"
"""
        if kind == "java-gradle":
            return header + """
GRADLE_BIN="${GRADLE_BIN:-./gradlew}"
if [[ ! -x "$GRADLE_BIN" ]]; then
  GRADLE_BIN="${GRADLE_BIN:-gradle}"
fi
TASK="${TASK:-test}"
exec "$GRADLE_BIN" "$TASK" "$@"
"""
        if kind == "node":
            return header + """
if npm run | grep -q "^  test"; then
  exec npm test -- "$@"
fi
echo "No npm test script found." >&2
exit 2
"""
        if kind == "python":
            return header + """
TEST="${TEST:-}"
if command -v pytest >/dev/null 2>&1; then
  if [[ -n "$TEST" ]]; then
    exec pytest "$TEST" "$@"
  fi
  exec pytest "$@"
fi
python3 -m unittest discover "$@"
"""
        if kind == "go":
            return header + '\nexec go test ./... "$@"\n'
        if kind == "rust":
            return header + '\nexec cargo test "$@"\n'
        return header + '\necho "No test command configured yet." >&2\nexit 2\n'

    return header + """
if [[ "${1:-}" == "--help" || "${1:-}" == "-h" ]]; then
  echo "Usage: TEST=SomeRegressionTest ./scripts/reproduce-bug.sh"
  echo "   or: ./scripts/reproduce-bug.sh ./custom-command arg1 arg2"
  exit 0
fi

if [[ "$#" -gt 0 ]]; then
  exec "$@"
fi

if [[ -n "${TEST:-}" ]]; then
  exec ./scripts/test.sh
fi

echo "No reproduction target provided. Set TEST or pass a command." >&2
exit 2
"""


def generate(root: Path, force: bool, project_name: str) -> list[Path]:
    info = detect_project(root)
    written = []

    targets = {
        root / "AGENTS.md": ag_text(project_name, info),
        root / "ARCHITECTURE.md": architecture_text(project_name, info),
        root / "docs" / "README.md": docs_readme(project_name),
    }
    for topic, description in DOC_TOPICS.items():
        targets[root / "docs" / topic / "README.md"] = topic_readme(topic, description)

    scripts = {
        root / "scripts" / "lint.sh": shell_script(info["kind"], "lint"),
        root / "scripts" / "build.sh": shell_script(info["kind"], "build"),
        root / "scripts" / "test.sh": shell_script(info["kind"], "test"),
        root / "scripts" / "reproduce-bug.sh": shell_script(info["kind"], "reproduce"),
    }

    for path, content in {**targets, **scripts}.items():
        if write_file(path, content, force):
            written.append(path)
            if path.suffix == ".sh":
                make_executable(path)

    return written


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate an Agent-ready project harness.")
    parser.add_argument("repo", nargs="?", default=".", help="Repository root. Defaults to current directory.")
    parser.add_argument("--force", action="store_true", help="Overwrite existing generated files.")
    parser.add_argument("--project-name", help="Project name to use in generated docs.")
    args = parser.parse_args()

    root = Path(args.repo).expanduser().resolve()
    if not root.exists() or not root.is_dir():
        parser.error(f"Repository root does not exist or is not a directory: {root}")

    project_name = args.project_name or root.name
    written = generate(root, args.force, project_name)

    if written:
        print("Generated harness files:")
        for path in written:
            print(f"  {path.relative_to(root)}")
    else:
        print("No files generated. Existing harness files were kept. Use --force to overwrite.")

    print("\nNext steps:")
    print("  1. Review TODOs in AGENTS.md and ARCHITECTURE.md.")
    print("  2. Tighten module boundaries and commands using repository facts.")
    print("  3. Run: git diff --check")
    print("  4. Run: bash -n scripts/*.sh")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
