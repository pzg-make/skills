---
name: drawio-skill
description: Use when the user requests diagrams, flowcharts, architecture diagrams, ER diagrams, UML / sequence / class diagrams, network topology, ML/DL model figures (Transformer/CNN/LSTM), mind maps, or visual explanations with 3+ components, complex data flows, or relationships. Best suited for polished draw.io diagrams with custom styling, swimlanes, rich shapes, and exportable PNG/SVG/PDF/JPG outputs.
license: MIT
metadata: {"openclaw":{"requires":{"anyBins":["draw.io","drawio"]},"emoji":"📐","os":["darwin","linux","win32"],"install":[{"id":"brew-drawio","kind":"brew","formula":"drawio","bins":["drawio"],"label":"Install draw.io via Homebrew","os":["darwin"]},{"id":"brew-graphviz","kind":"brew","formula":"graphviz","bins":["dot"],"label":"Install Graphviz for optional autolayout.py","os":["darwin"],"optional":true}]},"hermes":{"tags":["drawio","diagram","flowchart","architecture","visualization","uml"],"category":"design","requires_tools":["drawio","draw.io"],"related_skills":["mermaid","excalidraw","plantuml"]},"author":"Agents365-ai","version":"1.14.0","homepage":"https://github.com/Agents365-ai/drawio-skill","platforms":["macos","linux","windows"],"compatibility":"Requires draw.io desktop CLI for local export; optional autolayout uses Graphviz."}
---

# Draw.io Diagrams

## Overview

Generate `.drawio` XML and, when the local draw.io CLI is available, export PNG/SVG/PDF/JPG deliverables. Prefer this skill for precise editable diagrams with solid fills, stock or branded shapes, swimlanes, strict UML/ERD/network structure, or polished exports.

Use a different tool when the user wants:

- Casual hand-drawn whiteboard sketches: Excalidraw or tldraw.
- Diagrams-as-code embedded in Markdown: Mermaid or PlantUML.
- Freehand infinite-canvas drawing: tldraw.

Version and compatibility notes live in `metadata`. The skill preserves the original draw.io capabilities: XML generation, local export, embedded editable exports, shape search, AI brand icons, style presets, autolayout, validation, and browser fallback.

## Bundled Resources

Read these only when the current request needs them.

| File or script | Read or run it when |
|---|---|
| `references/drawio-xml-export.md` | You need XML structure rules, export commands, self-check details, browser fallback, or CLI troubleshooting. |
| `references/diagram-types.md` | The user names a specific diagram type: ERD, UML class, sequence, architecture, ML/DL, or flowchart. |
| `references/shapes.md` + `scripts/shapesearch.py` | The diagram needs vendor, cloud, Kubernetes, Cisco, UML/BPMN/ER, electrical, P&ID, or any non-trivial draw.io shape. |
| `scripts/aiicons.py` | The diagram involves an AI/LLM brand such as OpenAI, Claude, Gemini, Mistral, Llama, HuggingFace, Ollama, or LangChain. |
| `references/style-presets.md` | The user asks to learn, save, list, set default, delete, or apply a named style preset. |
| `references/style-extraction.md` | You are inside the Learn flow from `style-presets.md`. |
| `references/troubleshooting.md` | Export fails, a PNG is rejected by vision, CLI behavior differs by OS, or rendering looks wrong. |
| `references/autolayout.md` | The diagram is large, graph-like, code-structure-oriented, or has more than about 15 nodes. |
| `scripts/pyimports.py`, `jsimports.py`, `goimports.py`, `rustimports.py` | The user wants to visualize Python, JS/TS, Go, or Rust import graphs. |
| `scripts/pyclasses.py` | The user wants a Python class hierarchy or class diagram. |
| `scripts/validate.py` | You generated a `.drawio` file and need structural linting before export or review. |
| `scripts/repair_png.py` | After every final `-e` PNG export, repair draw.io's truncated IEND chunk. |
| `scripts/encode_drawio_url.py` | The CLI is unavailable and you need a diagrams.net viewer or editor URL. |

## Workflow

Before generating, ask only for missing details that materially affect the result: diagram type, output format, output location, or scope/fidelity. Skip questions for simple or already specific requests.

1. Resolve style preset:
   - Treat phrases such as "use my `<name>` style", "with my `<name>` style", "in `<name>` mode", or "in the style of `<name>`" as preset names.
   - Do not treat a bare "with `<name>`" as a preset; it may be a component.
   - Load `~/.drawio-skill/styles/<name>.json`, then `<this-skill-dir>/styles/built-in/<name>.json`.
   - If the named preset does not exist, list available presets and stop.
   - For preset application rules, read `references/style-presets.md`.
2. Resolve dependencies:
   - Try `drawio --version`, then `draw.io --version`, then known platform-specific paths.
   - Use the first working binary name verbatim in subsequent commands.
   - If the CLI is missing, use install guidance or browser fallback. If a known binary fails because of sandbox/display/Electron issues, try one escalated retry before falling back.
3. Plan the diagram:
   - Identify diagram type, components, relationships, layout direction, groups, and output path.
   - Use `references/diagram-types.md` for type-specific structure.
   - For large graphs or code structure diagrams, use the autolayout/import scripts instead of hand-placing nodes.
4. Generate `.drawio`:
   - Follow XML rules in `references/drawio-xml-export.md`.
   - Use `scripts/shapesearch.py` or `scripts/aiicons.py` instead of guessing uncommon shape styles.
   - Validate generated XML with `scripts/validate.py` for large or complex diagrams.
5. Export preview:
   - Export preview PNG without `-e`, width-capped around 2000px, for vision review.
   - If CLI export is unavailable, produce XML plus a browser fallback URL or explain manual export.
6. Self-check and review:
   - Use vision when available to catch overlaps, clipped labels, missing connections, off-canvas shapes, misrouted edges, and label collisions.
   - Apply targeted XML edits for small feedback; regenerate only for layout-wide changes.
   - Keep preview iterations on the same filename; reserve `-e` for final exports.
7. Final export:
   - Export requested final formats, defaulting to PNG.
   - Use `-e` for PNG/SVG/PDF final outputs so they remain editable in draw.io.
   - Run `scripts/repair_png.py` after every final embedded PNG export.
   - Report the `.drawio` source and exported file paths.

## XML And Export Details

Read `references/drawio-xml-export.md` when you need:

- Required draw.io XML skeleton, root cells, shape styles, containers, connectors, waypoints, connection distribution, palette, or layout spacing.
- Preview vs final export commands and flags.
- PNG repair details after `-e` export.
- Browser fallback URL generation.
- CLI detection and platform-specific fallback behavior.
- Common export and rendering mistakes.

Keep SKILL.md lean; do not inline long XML examples or OS-specific command matrices here.

## Diagram Type Presets

When the user requests a specific diagram type, read `references/diagram-types.md` and use the matching section:

| User says | Section |
|---|---|
| "ER diagram", "schema diagram", "data model" | ERD |
| "UML class diagram", "class diagram" | UML Class |
| "sequence diagram", "interaction diagram", "lifeline" | Sequence |
| "architecture", "system diagram", "service diagram" | Architecture |
| "neural network", "model architecture", "ML diagram", "deep learning" | ML / Deep Learning Model |
| "flowchart", "decision tree", "process flow" | Flowchart |

If a user style preset is also active, keep the diagram-type structural keywords and layer color/font/edge/extras from the preset. Read `references/style-presets.md` for merge rules.

## Common Mistakes

For export failures, vision rejection, layout breakage, blank shapes, edge routing problems, WSL2 URL handling, or Linux headless issues, read `references/troubleshooting.md` first, then `references/drawio-xml-export.md` for the exact command or XML rule.
