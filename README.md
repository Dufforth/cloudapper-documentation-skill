# CloudApper solution documentation skill

A Claude Code skill for **documenting CloudApper solutions across their life cycle**: business requirements, software requirements (SRS), UAT test documentation, technical and troubleshooting guides for solution engineers, PM handover guides for business and project understanding, and analysis reports of existing apps. Each document follows the structure of an ISO/IEC/IEEE standard, tailored for no-code business solutions. Owner and approver: Pablo Huanca.

This is a standalone repository and skill for **analysis and documentation only**. It contains no knowledge for building, configuring or changing apps (no form design, workflow construction, integration build patterns or write APIs), and it does not depend on any other skill.

## Documents and standards

| Document | Reader | Based on |
|---|---|---|
| Business Requirements Document (BRD) | PM, customer owner, team | ISO/IEC/IEEE 29148:2018 (BRS/StRS) |
| Software Requirements Specification (SRS) | Solution engineers, testers, PM | ISO/IEC/IEEE 29148:2018 + ISO/IEC 25010:2023 |
| UAT test plan and test cases | Testers, key users, PM | ISO/IEC/IEEE 29119-3:2021 |
| Technical and troubleshooting guide | Support, solution engineers | ISO/IEC/IEEE 42010:2022, 26514:2022 |
| PM handover guide | Project and account managers | ISO 21502:2020 |
| Analysis report | Team leads, managers | ISO/IEC 25010:2023 |
| Document control on all of them | Everyone | ISO/IEC/IEEE 15289:2019 |

Why these standards and what was tailored out: `cloudapper-solution-docs/references/standards-map.md`.

## What is inside

| Path | What |
|---|---|
| `cloudapper-solution-docs/SKILL.md` | Entry point: deliverables, rules, process |
| `…/references/standards-map.md` | Chosen standards, document life cycle, tailoring, standards not used |
| `…/references/document-control.md` | Control block, versioning, cross-document IDs |
| `…/references/requirements-engineering.md` | Elicitation, requirement quality rules, priority, acceptance criteria, traceability, change control, CloudApper questions |
| `…/references/business-requirements.md` | BRD structure |
| `…/references/srs.md` | SRS structure and the ISO 25010 non-functional checklist with CloudApper examples |
| `…/references/uat-test-documentation.md` | UAT plan, test cases, completion summary |
| `…/references/technical-guide.md` | As-built technical and troubleshooting guide, architecture views |
| `…/references/pm-handover-guide.md` | PM handover guide |
| `…/references/reading-a-cloudapper-app.md` | Platform concepts for readers and analysts |
| `…/references/read-only-analysis.md` | Access, read-only data collection, screenshots, personal data and secrets |
| `…/references/analysis-checklist.md` | Risks to look for and how to write findings |
| `…/references/style-and-diagrams.md` | Writing style, diagrams, PDF, quality checklist |
| `…/templates/` | BRD, SRS (Markdown and Quarto PDF), UAT, technical guide and PM guide skeletons |
| `…/scripts/md-to-pdf.js` | Markdown + Mermaid to PDF (Node + Playwright) |
| `docs/CloudApper-Documentation-Method.md` | The documentation method explained for managers |

## Install

Skills are read from `~/.claude/skills/` (Windows: `C:\Users\<you>\.claude\skills\`).

```bash
git clone https://github.com/Cloudapper-SDE/cloudapper-docs-skill.git ~/cloudapper-docs-skill
```

Then make the skill folder visible to Claude Code, either by linking it (Windows PowerShell, no admin needed):

```powershell
New-Item -ItemType Junction -Path "$env:USERPROFILE\.claude\skills\cloudapper-solution-docs" -Target "$env:USERPROFILE\cloudapper-docs-skill\cloudapper-solution-docs"
```

(macOS/Linux: `ln -s ~/cloudapper-docs-skill/cloudapper-solution-docs ~/.claude/skills/cloudapper-solution-docs`)

or by copying `cloudapper-solution-docs/` into `~/.claude/skills/` (then copy again after each `git pull`). If `~/.claude/skills` is itself a git repository, add `/cloudapper-solution-docs/` to its `.gitignore`.

Start a new Claude Code session and ask, for example:
- *"Write a BRD and an SRS for {project} from these session notes."*
- *"Create UAT test cases from the approved SRS."*
- *"Document the {App Name} CloudApper app as a technical and troubleshooting guide."*
- *"Write a PM handover guide for this CloudApper solution."*

Browser access for app walkthroughs: the Playwright MCP is recommended (tested against Chrome DevTools MCP on 2026-11-09: fewer calls, batch screenshots, works with the window in the background).

## Versions

`VERSION` holds the current version; `CHANGELOG.md` lists what changed and why, newest first. Patch for added knowledge, minor for structural changes.

## Contributing

See `CONTRIBUTING.md`: fork, branch, pull request; merged only after the owner approves. To get access, ask Pablo to add you to the **Cloudapper-SDE** organization.
