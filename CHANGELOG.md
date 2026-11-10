# Change log

Newest first. Patch for added knowledge, minor for structural changes.

## v1.1.0 (2026-11-09)

**Why:** Extend the skill from as-built documentation to the full document set of a CloudApper solution, each following a tailored ISO/IEC/IEEE standard: requirements for the team, test documents to accept the solution, and guides for SEs and PMs. Adds lessons from a Playwright vs Chrome DevTools MCP comparison on a test app.

**Added:**
- `references/standards-map.md`: chosen standards (29148, 25010, 42010, 26514, 29119-3, 15289, 21502, 12207), document life cycle, tailoring decisions, standards not used.
- `references/document-control.md`: control block, versioning, IDs shared across documents.
- `references/requirements-engineering.md`, `business-requirements.md`, `srs.md`, `uat-test-documentation.md`: process, requirement quality rules, MoSCoW and source confidence, acceptance criteria, traceability, change control, CloudApper questions, ISO 25010 checklist with CloudApper examples.
- Templates: BRD, SRS (Markdown and Quarto PDF with non-functional and data sections), UAT plan and test cases.
- Technical guide: 42010 architecture views; PM guide: 21502 mapping; read-only analysis: browser tool lessons.
- Manager guide 1.1: full document set, standards table, requirements process.

**Files:** SKILL.md (rewritten for the wider scope), README.md, docs/CloudApper-Documentation-Method.md, 6 new references, 4 new templates.

## v1.0.0 (2026-11-09)

**Why:** A separate skill for understanding, analysing and documenting CloudApper solutions, shareable with managers and analysts without the app-building knowledge.

**Added:** `cloudapper-solution-docs` skill (rules, process, deliverables), references for reading an app, read-only analysis, technical guide, PM handover guide, analysis checklist, style and diagrams; templates for both guides; Markdown-to-PDF script; documentation method for managers in `docs/`.
