# Resume Workflow Reference

Use this reference for resume import editing, ATS checks, content quality, Chinese/English differences, and export acceptance.

## Import Fidelity Priority

Preserve in this order unless the user explicitly asks for redesign:

1. All original content: sections, roles, projects, bullets, skills, schools, certificates, awards, dates, links, contact fields, and metrics.
2. File editability and source document safety.
3. Existing text hierarchy and section order.
4. Font family, size, weight, color, and paragraph styles.
5. Margins, spacing, bullets, columns, tables, headers, footers, and separators.
6. Page count and pagination.
7. Visual polish for unavoidable overflow or broken layout.

## Source File Safety

Imported and referenced files are read-only:

- Never modify, overwrite, resave, rename, or delete the user's imported resume, source PDF/DOCX/HTML/Markdown, or referenced template.
- Always generate a new output file.
- Use clear output names based on the requested resume name or source stem.
- Never overwrite an existing output. If `name.pdf` already exists, use `name_1.pdf`, then `name_2.pdf`, and continue upward.
- Keep matching editable outputs on the same stem, for example `name_1.pdf`, `name_1.docx`, `name_1.html`, and `name_1.md`.

## No-Deletion Editing Rule

For existing resume edits, assume the user wants content preserved unless they explicitly ask to delete, shorten, cut, condense, merge, remove, or reduce.

Required behavior:

- Create a quick content inventory before editing.
- Preserve every original item in the output.
- Improve weak bullets in place instead of removing them.
- Keep less-relevant roles or projects; retarget wording and emphasis instead of dropping them.
- Do not remove older experience, skills, education, awards, or certificates because they seem redundant.
- Do not solve page overflow by deleting content. Adjust wording length, spacing, typography, or page count first.
- If removal would genuinely help, list the proposed removals separately and ask for approval before applying them.
- In the delivery note, state whether any content was removed. If none was removed, say so explicitly.

Preferred input handling:

- DOCX: read the source and generate a new DOCX output; preserve styles, runs, tables, section settings, headers, and footers without resaving the source file.
- PDF with selectable text: extract text and inspect rendered pages; rebuild only when direct PDF editing is unsuitable. Do not trust extraction alone.
- PDF without selectable text: treat as image-based; explain that exact editable preservation is not reliable, then OCR/rebuild if requested.
- HTML: preserve CSS and DOM structure where possible.
- Markdown: preserve heading structure and regenerate styled outputs.
- JSON/YAML: treat as structured content for new or rebuilt resumes.

## PDF Reading Safety

PDF parsing can drop or reorder content before editing begins. Common failure points include multi-column layouts, tables, text boxes, scanned pages, icons used as labels, headers, footers, hidden layers, clipped text, and unusual encodings.

Required checks for every PDF import:

- Render each page and inspect the visual page, not only extracted text.
- Compare extracted text with the rendered page by page.
- Count visible sections, roles/projects, bullets, table rows/cells, skills, education entries, dates, links, and contact fields.
- Map every heading/title to the visual block it labels before assigning body content.
- Treat the rendered page as the source of truth when text extraction is incomplete or out of order.
- If content cannot be confidently read, stop and ask for DOCX/source text or permission to OCR/reconstruct.
- Mention any PDF-reading uncertainty in the delivery note.

## Heading-Content Binding Checklist

Run this check for every imported PDF, complex DOCX, table resume, and multi-column resume:

- Identify visual containers first: pages, columns, tables, cards, text boxes, sidebars, and main content areas.
- Assign headings only to content in the same visual container unless the source clearly spans containers.
- Preserve original section title text and order unless the user asks for renamed or reordered sections.
- For each heading, verify the first and last item under it against the rendered source.
- Verify item counts under each heading: roles, projects, bullets, skills, education entries, certificates, and awards.
- Treat repeated labels such as date, company, role, project, and skill as fields within the current block, not new section headings.
- Do not let page headers, footers, watermark text, sidebar labels, or template captions become resume section headings.
- Do not attach right-column content to a left-column heading, or table-cell content to a nearby heading outside the table.
- If heading boundaries are unclear, preserve the visual grouping in the output and mention the ambiguity instead of guessing.

## Layout Consistency Checklist

Run this check after every edit, template adaptation, or export:

- Page size: default to standard A4 for new or rebuilt resumes unless the user requests another size.
- Font family: each text level uses the intended font family; no accidental fallback font appears in edited text.
- Font size: body text, bullets, headings, dates, and captions are internally consistent; edited content does not introduce one-off sizes.
- Font weight and style: bold, italic, underline, and color are used consistently for the same semantic level.
- Alignment: repeated dates, locations, company names, role titles, section headings, skill lists, and contact fields align to the same visual grid.
- Indentation: bullets use consistent hanging indents; nested bullets, if present, are aligned and not mistaken for top-level bullets.
- Paragraph spacing: comparable sections have matching before/after spacing and line height.
- Columns and tables: column widths, row heights, cell padding, borders, and vertical alignment remain consistent.
- Page breaks: no orphaned section headings, single stranded bullets, accidental blank pages, or clipped final lines. If a section, role/project block, table row, or bullet group does not fit the current page, move the whole block to the next page.
- Text bounds: no overlapping text, text outside page margins, hidden text, cropped content, or icons covering words.
- Export parity: PDF page layout matches the editable DOCX/HTML source as closely as possible.

If the source resume has inconsistent formatting already, preserve it for targeted edits unless the user asks for cleanup. If cleanup is requested, normalize the inconsistency systematically across the whole document, not only in the edited paragraph.

## ATS Checklist

Check for:

- Standard section names for the target market.
- Real text instead of images.
- Clear contact information with email, phone, location, LinkedIn/GitHub/portfolio when relevant.
- Reverse-chronological experience unless the user has a strong reason for another format.
- Job-title, skill, tool, domain, and certification keywords from the target JD.
- Consistent date format.
- No critical information hidden only in icons, graphics, headers, or footers.
- No excessive tables, text boxes, or multi-column complexity for strict ATS submissions.
- PDF with selectable text and DOCX fallback when the application system asks for Word.

## Content Quality Checklist

For each summary, role, or project:

- Lead with fit for the target role.
- Use action verbs and concrete nouns.
- Include scope: product, user base, data scale, budget, team size, market, or technical environment when known.
- Include result: revenue, conversion, retention, latency, reliability, quality, cost, speed, adoption, ranking, or customer impact when true.
- Rewrite empty claims such as "responsible for", "participated in", "hard-working", and unsupported "excellent" into more concrete wording when possible; do not delete the bullet unless the user approves deletion.
- Keep bullets parallel in tense and structure.
- Avoid inventing employers, dates, degrees, titles, metrics, tools, or certifications.

## Chinese And English Differences

Chinese resumes:

- Keep wording compact and information-dense.
- Use clear project/role labels and concrete business outcomes.
- Put education early for students or new graduates; put experience first for experienced candidates.
- Avoid over-designed decorative layouts unless the user targets creative roles.

English resumes:

- Use action-verb bullets and parallel grammar.
- Prefer one to two pages depending on seniority and market.
- Avoid first-person pronouns.
- Localize terminology for the target country, for example "resume" for the US and "CV" for some other markets.
- Ensure dates, phone format, and location format match the target market.

## Export Acceptance

Before delivery:

- Confirm PDF text is selectable or generated from text, not a page screenshot.
- Confirm DOCX opens as an editable file.
- Confirm HTML and Markdown can regenerate the same content.
- Confirm filenames are clear, for example `resume.pdf`, `resume.docx`, `resume.html`, `resume.md`.
- Confirm no source/import/reference file was modified.
- Confirm output naming did not overwrite an existing file and uses `_1`, `_2`, etc. when needed.
- For PDF imports, confirm rendered pages were checked against extracted content.
- Confirm headings/titles are bound to the correct body content and no section has absorbed unrelated content.
- For imported edits, confirm every original section and item is still present unless the user approved removal.
- For imported edits, compare against the original visually and confirm unrequested style changes are absent.
- For all edits, confirm font sizes, alignment, indentation, bullets, spacing, tables/columns, and page breaks are consistent.
- For redesigned resumes, confirm page count, typography, color, and section order match the chosen design direction.
