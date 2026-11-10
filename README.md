# CloudApper Documentation Skill

A Claude Code skill for **analysing and documenting CloudApper solutions**: business requirements, software requirements (SRS), UAT test documentation, technical and troubleshooting guides for solution engineers, PM handover guides for business and project understanding, and analysis reports. Each document follows the structure of an ISO/IEC/IEEE standard, tailored for no-code business solutions. Owner and approver: Pablo Huanca.

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

Why these standards and how they are tailored: `cloudapper-documentation/references/standards-map.md`.

## What is inside

| Path | What |
|---|---|
| `cloudapper-documentation/SKILL.md` | Entry point: deliverables, rules, process |
| `…/references/standards-map.md` | Chosen standards, document life cycle, tailoring |
| `…/references/document-control.md` | Control block, versioning, cross-document IDs |
| `…/references/requirements-engineering.md` | Elicitation, requirement quality rules, priority, acceptance criteria, traceability, change control |
| `…/references/business-requirements.md` | BRD structure |
| `…/references/srs.md` | SRS structure and the ISO 25010 quality checklist |
| `…/references/uat-test-documentation.md` | UAT plan, test cases, completion summary |
| `…/references/technical-guide.md` | Technical and troubleshooting guide, architecture views |
| `…/references/pm-handover-guide.md` | PM handover guide |
| `…/references/reading-a-cloudapper-app.md` | Concepts needed to read and explain an app |
| `…/references/read-only-analysis.md` | Access, read-only data collection, screenshots, personal data and secrets |
| `…/references/analysis-checklist.md` | Risks to look for and how to write findings |
| `…/references/style-and-diagrams.md` | Writing style, diagrams, PDF, quality checklist |
| `…/templates/` | BRD, SRS (Markdown and PDF layout), UAT, technical guide and PM guide skeletons |
| `…/scripts/md-to-pdf.js` | Markdown + Mermaid to PDF |
| `docs/CloudApper-Documentation-Method.md` | The documentation method explained for managers |

## Install

Skills are read from `~/.claude/skills/` (Windows: `C:\Users\<you>\.claude\skills\`).

```bash
git clone https://github.com/Dufforth/cloudapper-documentation-skill.git ~/cloudapper-documentation-skill
```

Then make the skill folder visible to Claude Code, either by linking it (Windows PowerShell, no admin needed):

```powershell
New-Item -ItemType Junction -Path "$env:USERPROFILE\.claude\skills\cloudapper-documentation" -Target "$env:USERPROFILE\cloudapper-documentation-skill\cloudapper-documentation"
```

(macOS/Linux: `ln -s ~/cloudapper-documentation-skill/cloudapper-documentation ~/.claude/skills/cloudapper-documentation`)

or by copying `cloudapper-documentation/` into `~/.claude/skills/` (then copy again after each `git pull`). If `~/.claude/skills` is itself a git repository, add `/cloudapper-documentation/` to its `.gitignore`.

Start a new Claude Code session and ask, for example:
- *"Write a BRD and an SRS for {project} from these session notes."*
- *"Create UAT test cases from the approved SRS."*
- *"Document the {App Name} CloudApper app as a technical and troubleshooting guide."*
- *"Write a PM handover guide for this CloudApper solution."*

## Versions

`VERSION` holds the current version; `CHANGELOG.md` lists what changed and why, newest first. Patch for added content, minor for structural changes.

## Contributing

See `CONTRIBUTING.md`: fork, branch, pull request; merged only after the owner approves. To get access, ask Pablo to add you as a collaborator (read access) on `Dufforth/cloudapper-documentation-skill`.
