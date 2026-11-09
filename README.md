# CloudApper solution documentation skill

A Claude Code skill for **understanding, analysing and documenting existing CloudApper solutions**. It is meant for anyone who needs to explain, hand over, support or review a CloudApper app: solution engineers, support analysts, project and account managers. Owner and approver: Pablo Huanca.

This repository deliberately contains **no app-building knowledge** (designing forms, writing workflows, integration patterns, API writes). It only covers what is needed to read an app safely and write about it. App building lives in the separate `cloudapper-skills` repository.

## What is inside

| Path | What |
|---|---|
| `cloudapper-solution-docs/SKILL.md` | Entry point: deliverables, rules, process |
| `cloudapper-solution-docs/references/reading-a-cloudapper-app.md` | Platform concepts for readers: forms, workflows, triggers, nodes, connectors, roles, behaviours that explain "strange" results, glossary |
| `cloudapper-solution-docs/references/read-only-analysis.md` | Access, read-only API snapshot, walkthrough, screenshots, personal data and secrets |
| `cloudapper-solution-docs/references/technical-guide.md` | Structure of the technical and troubleshooting guide, and of a findings-only analysis report |
| `cloudapper-solution-docs/references/pm-handover-guide.md` | Structure of the PM handover guide |
| `cloudapper-solution-docs/references/analysis-checklist.md` | What to look for when writing findings, with severities |
| `cloudapper-solution-docs/references/style-and-diagrams.md` | Writing style, diagram rules, PDF, quality checklist |
| `cloudapper-solution-docs/templates/` | Fill-in skeletons for both guides |
| `cloudapper-solution-docs/scripts/md-to-pdf.js` | Markdown + Mermaid to PDF (Node + Playwright) |
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

or by copying `cloudapper-solution-docs/` into `~/.claude/skills/` (then update by copying again after `git pull`). If `~/.claude/skills` is itself a git repository, add `/cloudapper-solution-docs/` to its `.gitignore`.

Start a new Claude Code session and ask, for example: *"Document the {App Name} CloudApper app as a technical and troubleshooting guide"* or *"Write a PM handover guide for this CloudApper solution"*.

## Versions

`VERSION` holds the current version; `CHANGELOG.md` lists what changed and why, newest first. Patch for added knowledge, minor for structural changes.

## Contributing

See `CONTRIBUTING.md`: fork, branch, pull request; merged only after the owner approves. To get access, ask Pablo to add you to the **Cloudapper-SDE** organization.
