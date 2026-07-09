---
name: resume-builder
description: Create, import, read, edit, preserve formatting and original content, polish, tailor, design, and export professional resumes. Use when an AI coding tool needs to work on resumes or CVs from scratch or from imported DOCX, PDF, HTML, Markdown, JSON, or YAML files; split resume intent into tasks; read PDFs without losing content by combining text extraction with rendered-page checks; bind headings to the correct visual content blocks; never modify imported or referenced source files; generate new uniquely named outputs; preserve source layout, typography, alignment, spacing, and all source content during edits; customize resume UI/design; source resume style inspiration from mmmlllnnn/ResumeCollection; improve resume content without deleting user-provided facts; tailor a resume to a job description; check ATS friendliness; or export editable DOCX/HTML/Markdown plus selectable-text PDF files.
---

# Resume Builder

## Overview

Use this skill to create a new resume, import and edit an existing resume, preserve source formatting during targeted edits, tailor content to a job description, customize the visual design, and export both final and editable files.

When the user imports a resume and does not explicitly request layout or style changes, preserve the original visual system first: template, section order, fonts, font sizes, colors, margins, spacing, bullets, tables, headers, footers, and pagination.

When modifying an existing resume, preserve all user-provided content by default. Do not delete, hide, merge away, summarize away, or omit any experience, project, skill, education item, certificate, award, date, employer, metric, or contact field unless the user explicitly asks for deletion or approves a proposed removal.

Treat imported and referenced files as read-only. Never edit, overwrite, resave, rename, or delete the original input file. Always generate a new output file with a unique filename.

## Workflow

1. Classify the request before editing:
   - New resume from raw career facts.
   - Imported resume edit with formatting preservation.
   - Existing resume rewrite or modernization.
   - Job-description tailoring.
   - Content-only polishing.
   - Layout/UI customization.
   - Export or format conversion.
2. Inspect available inputs:
   - Prefer DOCX for faithful import editing.
   - Use PDF when the user only has PDF, but never rely on text extraction alone; extract text, render pages visually, and compare the inventory against the rendered pages before editing.
   - Use HTML or Markdown as editable sources when present.
   - Use JSON/YAML as structured input for new or rebuilt resumes.
3. Build a preservation inventory for existing resumes:
   - List all sections, roles/projects, bullets, skills, education items, dates, links, and contact fields before editing.
   - Bind every title/heading to the visual content block it labels before rewriting or exporting.
   - Treat this inventory as the minimum content that must survive the edit unless the user says otherwise.
4. Choose the least invasive path:
   - For imported DOCX edits, generate a new document based on the original and keep existing styles; never save changes into the imported file.
   - For imported PDF edits, generate a new editable reconstruction and PDF; preserve text and layout where possible, and state any PDF-reading limitations.
   - For new or rebuilt resumes, use `scripts/export_resume.py` to generate DOCX, PDF, HTML, and Markdown outputs.
5. Verify the result:
   - Ensure requested content changed.
   - Ensure no source content was removed, merged into invisibility, or silently summarized away.
   - Ensure unrequested formatting changes did not occur.
   - Ensure typography, alignment, indentation, spacing, bullets, columns, tables, and page breaks are consistent.
   - Ensure PDF output contains selectable text, not flattened images.
   - Ensure an editable source file is delivered with the PDF.
   - Ensure output filenames did not overwrite existing files; if a same-name PDF exists, use `_1`, `_2`, and so on.

## Intent Splitting

Break broad resume requests into these modules and handle only the modules the user asked for:

- Content: summary, experience bullets, projects, skills, education, awards, links, and facts.
- Positioning: target role, seniority, industry, language, region, ATS keywords, and recruiter scan path.
- Layout: page count, section order, density, margins, typography, spacing, bullets, and pagination.
- UI customization: template style, accent color, icons, avatar/photo, columns, separators, and visual hierarchy.
- Export: DOCX, PDF, HTML, Markdown, TXT, or source package.

If the user asks for "optimize" without details, optimize content first and preserve layout unless layout problems are visible or the user asks for design changes.

## Content Preservation Contract

Use this contract for every imported or existing resume edit:

- Preserve every original section and item by default, even if it seems less relevant, repetitive, old, or visually crowded.
- Rewrite text in place instead of deleting bullets. If a bullet is weak, improve it; do not remove it.
- Keep all dates, employers, titles, schools, skills, links, metrics, certifications, and awards unless the user explicitly asks to remove or anonymize them.
- Do not shorten a resume by deleting content just to fit one page. First try wording of similar length, spacing adjustments, a smaller but readable font, or a two-page layout.
- Do not convert several bullets into one bullet if that makes any original fact disappear.
- Do not drop "less relevant" roles or projects during JD tailoring; instead, reorder emphasis or lightly retarget wording while preserving the original content.
- If deletion, merging, or major compression would improve the resume, present it as a recommendation and wait for approval before applying it.
- Include a brief delivery note that states whether any content was removed. The default answer should be "no content removed".

## Import Editing Fidelity

Default to preservation. Without explicit user approval, do not:

- Delete, hide, merge away, or omit source content.
- Modify, overwrite, resave, rename, or delete the imported source file or any referenced template file.
- Change the template, font family, font size, color palette, margins, or section order.
- Convert a one-page resume into two pages or compress a two-page resume into one page.
- Replace bullets, icons, tables, columns, headers, footers, or separators.
- Rebuild a DOCX from scratch when direct editing can preserve styles.
- Flatten a PDF into images.

When editing imported files:

- Keep the original file untouched and create a new output file for every result.
- Use a unique output filename. If `resume.pdf` exists, write `resume_1.pdf`; if that exists, write `resume_2.pdf`, continuing upward.
- Make targeted text replacements inside existing runs, paragraphs, table cells, and styles whenever possible.
- Match the surrounding language, punctuation, bullet rhythm, and tense.
- If a rewrite changes text length enough to disturb pagination, first try equivalent-length wording before changing layout; never solve overflow by deleting content without approval.
- If layout must change to avoid overflow, make the smallest visible adjustment and mention it in the delivery note.

Read `references/resume-workflow.md` when the task involves imported files, ATS checks, detailed content quality review, Chinese/English differences, or export acceptance.

## PDF Reading Safety

PDF text extraction can lose content or reorder text, especially with columns, tables, text boxes, headers/footers, icons, scanned pages, or hidden layers. For PDF inputs:

- Render every page to images or inspect page screenshots before trusting extracted text.
- Build the content inventory from both extracted text and rendered pages.
- Check page count, visible sections, bullet count, table cells, dates, links, and contact fields against the rendered pages.
- Validate every extracted heading/title against the rendered page before assigning body content to it.
- If the PDF is scanned or text extraction is incomplete, use OCR if available; otherwise ask for DOCX or source content before editing.
- If extracted content conflicts with the rendered page, preserve the rendered page as the source of truth and state the uncertainty.
- Never silently proceed with a partial PDF extraction.

## Heading And Content Binding

Do not infer resume structure from text order alone. PDF and DOCX extraction can return headings, columns, tables, and body text out of order.

- Build structure by visual blocks first: page, column, section boundary, table cell, heading, then body content.
- Keep each heading attached only to the content directly beneath it, beside it, or inside the same visual container.
- Do not move content from the right column under a left-column heading, or from a table cell under a nearby unrelated heading.
- Preserve original section titles exactly unless the user requests renamed sections.
- If two headings are visually close, use separators, indentation, font hierarchy, whitespace, and alignment to decide the boundary.
- If a heading-to-content relationship is ambiguous, stop and ask for clarification or report the ambiguity instead of guessing.
- After reconstruction, compare the output outline with the rendered source page: section title order, item counts, and first/last bullet under each title must match.

## Layout Consistency Gate

Before delivering any edited or exported resume, inspect layout consistency. Treat visible inconsistencies as defects, not preferences.

- Keep each text level consistent: name, headline, section headings, role/project titles, body text, bullets, dates, and footnotes should each use one intended font size and weight.
- Match the imported document's font family, fallback fonts, line spacing, paragraph spacing, margins, and indentation unless the user asks for redesign.
- Align repeated structures the same way: dates, company names, locations, role titles, section headings, bullet blocks, skill lists, and contact fields.
- Preserve bullet symbol, hanging indent, tab stops, and bullet-to-text spacing within the same section.
- Keep columns and tables balanced: equal left/right padding, consistent row heights, no clipped text, no unexpected wrapped labels, and no misaligned vertical borders.
- Keep section spacing visually uniform. Do not let one edited section become tighter or looser than comparable sections.
- Avoid orphaned headings, widowed single bullets, overlapping text, text outside margins, and accidental blank pages.
- Use standard A4 page size by default for new or rebuilt resumes unless the user explicitly requests another page size.
- When the current page cannot fit the next section, role/project block, table row, or bullet group cleanly, move that whole block to the next page instead of squeezing, clipping, overlapping, or splitting it awkwardly.
- If content length creates overflow, adjust wording length or spacing minimally while preserving content; do not solve layout issues by deleting content.
- For DOCX, prefer existing paragraph/table styles over ad hoc direct formatting. For HTML, prefer shared CSS classes over per-element inline changes.
- After PDF export, visually inspect page breaks, alignment, and font rendering against the editable source.

## Style Sources

Use `references/resume-style-sources.md` when the user asks for template selection, visual style, UI customization, or style inspiration.

Prefer `mmmlllnnn/ResumeCollection` as the default external style source for Chinese, English, multi-page, cover, and simple table resume references. Treat the repository as a style and template index: inspect the relevant category, select a style that matches the user's role and delivery channel, then adapt the design instead of blindly copying a template. Check the repository license and file type before reusing any downloaded template.

## Content Polishing

Improve content without inventing facts:

- Convert vague responsibility statements into impact-oriented bullets only when evidence is present.
- Ask for missing metrics when metrics are essential and cannot be inferred.
- Prefer concrete action, scope, tool, result, and business value.
- Preserve truthful seniority; do not inflate titles, employers, dates, degrees, or certifications.
- Tailor summaries and bullets to the target job description by adding relevant existing experience and keywords.
- Rewrite weak, repetitive, or empty claims instead of removing them; only remove content after explicit user approval.
- Keep Chinese resumes concise and direct; keep English resumes action-verb led, parallel, and ATS-readable.

## Layout And UI

Use modern resume-builder patterns conservatively:

- Prefer ATS-friendly modern-simple layouts for new resumes.
- Use creative layouts only when the target role or user preference supports them.
- Keep hierarchy scannable: name/contact, summary, core skills, experience/projects, education, extras.
- Keep font-size hierarchy restrained and consistent: do not introduce new body sizes or mixed heading sizes unless the design system already uses them.
- Keep alignment predictable: left-align body content, align dates/locations consistently, and avoid mixed center/left/right alignment in repeated sections.
- Use one accent color at most unless the user requests a brand-like design.
- Avoid decorative elements that reduce parser readability.
- Keep text selectable, readable, and professional in all exported formats.

Only change layout or UI when the user asks, imported layout is broken, content overflows, or export fidelity requires a minimal repair.

## Export

Always provide a final application file and an editable source when exporting:

- PDF: final sharing/application format; must preserve a text layer.
- DOCX: primary editable format for most users.
- HTML: editable and useful for visual preview or browser-based PDF generation.
- Markdown: portable source for versioning and later regeneration.

Use `scripts/export_resume.py` for new resumes, structured resume data, Markdown input, or rebuilt resumes:

```bash
python3 scripts/export_resume.py input.json --output-dir out
python3 scripts/export_resume.py input.md --output-dir out --base-name resume
```

The script defaults to A4 page size and unique output stems. If `resume.pdf` already exists, it will write `resume_1.pdf` and matching editable source files.

Do not use the export script as the first choice for imported DOCX preservation tasks. Generate a new file from the original document structure without overwriting the source.
