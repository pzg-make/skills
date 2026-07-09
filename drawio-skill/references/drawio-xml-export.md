# Draw.io XML And Export Reference

Use this reference when `SKILL.md` points here for XML structure, export commands, fallback behavior, self-check rules, or platform-specific draw.io details.

## Prerequisites

The draw.io desktop app must be installed and the CLI accessible for local export. In sandboxed macOS environments, even `drawio --version` can crash or produce no output. Treat that as a sandbox limitation and use browser fallback or XML-only output instead of repeatedly retrying.

Install options:

```bash
# macOS
brew install --cask drawio
drawio --version

# macOS app path
/Applications/draw.io.app/Contents/MacOS/draw.io --version

# Windows
"C:\Program Files\draw.io\draw.io.exe" --version

# Linux
drawio --version
```

Avoid Linux snap installs on servers; AppArmor sandboxing often breaks draw.io desktop export.

## XML Skeleton

```xml
<?xml version="1.0" encoding="UTF-8"?>
<mxfile host="drawio" version="26.0.0">
  <diagram name="Page-1">
    <mxGraphModel>
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

Rules:

- `id="0"` and `id="1"` are required root cells.
- User shapes normally start at `id="2"` and increment sequentially.
- Shapes use `parent="1"` unless they are inside a container.
- Text labels should use `html=1` in style.
- Never use `--` inside XML comments.
- Escape XML attribute values: `&amp;`, `&lt;`, `&gt;`, `&quot;`.
- Use `&#xa;` for line breaks inside labels.

## Shapes

Common vertex styles:

| Style keyword | Use for |
|---|---|
| `rounded=0` | Plain rectangle |
| `rounded=1` | Services, modules, common boxes |
| `ellipse;` | Start/end, circles, ovals |
| `rhombus;` | Decisions |
| `shape=cylinder3;` | Databases |
| `swimlane;` | Titled groups or containers |

For vendor/branded icons and uncommon shapes, run:

```bash
python3 <this-skill-dir>/scripts/shapesearch.py "<keywords>"
```

For AI/LLM brand logos, run:

```bash
python3 <this-skill-dir>/scripts/aiicons.py "<brand>"
```

Examples:

```xml
<mxCell id="2" value="API" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="160" height="60" as="geometry" />
</mxCell>

<mxCell id="3" value="DB" style="shape=cylinder3;whiteSpace=wrap;html=1;fillColor=#f5f5f5;strokeColor=#666666;" vertex="1" parent="1">
  <mxGeometry x="350" y="100" width="120" height="80" as="geometry" />
</mxCell>
```

## Containers

For nested architecture diagrams, use draw.io containment instead of placing shapes visually on top of larger boxes.

| Type | Style | When to use |
|---|---|---|
| Group | `group;pointerEvents=0;` | Invisible grouping, no direct connections |
| Swimlane | `swimlane;startSize=30;` | Visible title bar or connectable container |
| Custom container | `container=1;pointerEvents=0;` | Any shape acting as a container |

Children set `parent="containerId"` and use coordinates relative to the container.

## Connectors

Every edge must contain a `<mxGeometry relative="1" as="geometry" />` child. Self-closing edge cells do not render reliably.

```xml
<mxCell id="10" value="HTTP" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;" edge="1" parent="1" source="2" target="3">
  <mxGeometry relative="1" as="geometry" />
</mxCell>
```

Edge rules:

- Include `rounded=1;orthogonalLoop=1;jettySize=auto`.
- Pin `exitX/exitY/entryX/entryY` when nodes have multiple connections.
- Add waypoints when an edge must route around unrelated shapes.
- Keep at least 20px for the final segment into an arrowhead.
- Use `labelBackgroundColor=#ffffff;fontSize=11` and geometry offsets for crowded edge labels.
- Add `flowAnimation=1;` for animated connectors when useful in SVG/draw.io desktop.

Connection points:

| Position | exitX/entryX | exitY/entryY |
|---|---:|---:|
| Top center | 0.5 | 0 |
| Top-left | 0.25 | 0 |
| Top-right | 0.75 | 0 |
| Right center | 1 | 0.5 |
| Bottom center | 0.5 | 1 |
| Left center | 0 | 0.5 |

## Palette And Layout

Built-in palette when no preset is active:

| Color | fillColor | strokeColor | Use for |
|---|---|---|---|
| Blue | `#dae8fc` | `#6c8ebf` | Services, clients |
| Green | `#d5e8d4` | `#82b366` | Success, databases |
| Yellow | `#fff2cc` | `#d6b656` | Queues, decisions |
| Orange | `#ffe6cc` | `#d79b00` | Gateways, APIs |
| Red/Pink | `#f8cecc` | `#b85450` | Errors, alerts |
| Grey | `#f5f5f5` | `#666666` | External or neutral |
| Purple | `#e1d5e7` | `#9673a6` | Security, auth |

Spacing guide:

| Complexity | Nodes | Horizontal gap | Vertical gap |
|---|---:|---:|---:|
| Simple | 5 or fewer | 200px | 150px |
| Medium | 6-10 | 280px | 200px |
| Complex | More than 10 | 350px | 250px |

Layout rules:

- Snap coordinates and sizes to multiples of 10.
- Leave about 80px routing corridors between rows or columns.
- Place highly connected hubs centrally.
- Use swimlanes for visible logical grouping.
- For event bus patterns, place the bus in the center of the service row to reduce crossings.
- For large or graph-like diagrams, use autolayout instead of hand placement.

## Preview And Final Export

There are two export modes:

- Preview/self-check: no `-e`; output `diagram.png`; cap width around 2000px.
- Final/deliverable: pass `-e`; output `diagram.drawio.png`; repair embedded PNG afterward.

Commands use `drawio` as a placeholder for the resolved binary name.

```bash
# Preview PNG
drawio -x -f png --width 2000 -o diagram.png input.drawio

# Final embedded PNG
drawio -x -f png -e -s 2 -o diagram.drawio.png input.drawio
python3 <this-skill-dir>/scripts/repair_png.py diagram.drawio.png

# SVG and PDF final exports
drawio -x -f svg -e -o diagram.svg input.drawio
drawio -x -f pdf -e -o diagram.pdf input.drawio
```

Important flags:

- `-x`: export mode.
- `-f`: output format: `png`, `svg`, `pdf`, or `jpg`.
- `-e`: embed diagram XML; use only for final PNG/SVG/PDF exports.
- `-s`: scale; use for final PNG, not preview width-capped PNG.
- `--width <px>`: preview sizing; do not combine with `-s`.
- `-o`: output path; create target directories first.
- `--page-index 0`: export a specific page.

For final embedded PNGs, draw.io may truncate the IEND chunk. Always run `scripts/repair_png.py`; it is safe even after upstream fixes.

## Self-Check

After preview export, use vision if available. The preview PNG must not use `-e`.

Check:

- Overlapping shapes.
- Clipped labels.
- Missing or disconnected arrows.
- Off-canvas shapes.
- Edge-shape overlap.
- Stacked edges.
- Edge-label overlap.

Auto-fix with minimal XML edits and re-export. Stop after two self-check rounds if issues remain and show the user.

## Review Loop

Apply targeted XML edits for user feedback:

| Request | XML action |
|---|---|
| Change color | Update `fillColor` or `strokeColor` on the matching `mxCell`. |
| Add node | Append a new vertex with next available id near related nodes. |
| Remove node | Delete the vertex and edges using it as source or target. |
| Move/resize shape | Update `mxGeometry` x/y/width/height. |
| Add arrow | Append a new edge with matching `source` and `target`. |
| Change label | Update the matching `value` attribute. |
| Change layout direction | Regenerate the diagram. |

Overwrite the same preview PNG each iteration. Reserve embedded export for final output.

## Browser Fallback

When the CLI is unavailable:

```bash
python3 <this-skill-dir>/scripts/encode_drawio_url.py input.drawio
python3 <this-skill-dir>/scripts/encode_drawio_url.py --edit input.drawio
```

The script produces diagrams.net URLs with the XML encoded in the URL fragment. The fragment is not sent to the server. On WSL2/Windows, use the `.url` workaround described in `references/troubleshooting.md` because `cmd.exe` can drop `#fragment`s.

## Fallback Chain

| Scenario | Behavior |
|---|---|
| CLI missing, Python available | Use browser fallback. |
| CLI missing, Python missing | Generate `.drawio` XML only and explain manual export. |
| CLI crashes or prints nothing in macOS sandbox | Treat CLI as unavailable in-sandbox; use fallback or ask for host export. |
| Vision unavailable | Skip self-check and show preview PNG. |
| Linux export fails | Try `xvfb-run -a`, then `--no-sandbox` at the end if root, `--disable-gpu`, `HOME=/tmp`, required apt libs, or renderer Docker. |

## CLI Detection

```bash
if command -v drawio >/dev/null 2>&1; then
  DRAWIO="drawio"
elif command -v draw.io >/dev/null 2>&1; then
  DRAWIO="draw.io"
elif [ -f "/Applications/draw.io.app/Contents/MacOS/draw.io" ]; then
  DRAWIO="/Applications/draw.io.app/Contents/MacOS/draw.io"
elif grep -qi microsoft /proc/version 2>/dev/null && [ -f "/mnt/c/Program Files/draw.io/draw.io.exe" ]; then
  DRAWIO="/mnt/c/Program Files/draw.io/draw.io.exe"
else
  echo "drawio not found"
fi
```

Use the resolved binary exactly in later commands.
