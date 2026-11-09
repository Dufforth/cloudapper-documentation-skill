---
name: cloudapper-solution-docs
description: Understand, analyse and document an existing CloudApper solution (an app on web.cloudapper.com, m2sys.cloudapper.com or another tenant) without changing it - read-only walkthrough, reading forms, menus, roles, workflows, connectors and reports, explaining how the solution works, finding risks, and writing a technical and troubleshooting guide, a PM handover guide or an analysis report in Markdown (PDF on request). Use when asked to document, explain, analyse, review, audit, hand over or write a troubleshooting guide for a CloudApper app or solution, or when someone needs to understand what a CloudApper app does. This skill is for understanding and documenting only; it does not cover building or changing apps.
---

# CloudApper solution documentation and analysis

This skill helps a reader **understand an existing CloudApper solution and write it down** so that others can support it, hand it over or decide what to improve. It never changes the app. Building and changing apps is out of scope.

## What you can produce

| Deliverable | Reader | Guide |
|---|---|---|
| **Technical and troubleshooting guide** | Support analysts, solution engineers | `references/technical-guide.md` |
| **PM handover guide** | Project managers, account managers | `references/pm-handover-guide.md` |
| **Analysis report** (findings and recommendations only) | Team leads, managers | `references/analysis-checklist.md` + `references/technical-guide.md` §8 |
| **Solution summary** (one page) | Managers, new team members | `references/technical-guide.md` §1–2 only |

Ready-to-fill skeletons are in `templates/`.

## Read before you start

| Task | Read |
|---|---|
| Understand CloudApper concepts (forms, workflows, triggers, connectors, roles, reports) well enough to explain an app | `references/reading-a-cloudapper-app.md` |
| Get access and collect facts without changing anything (walkthrough, APIs, screenshots, personal data, secrets) | `references/read-only-analysis.md` |
| Write the technical and troubleshooting guide | `references/technical-guide.md` |
| Write the PM handover guide | `references/pm-handover-guide.md` |
| Find risks and write findings (F-01…) | `references/analysis-checklist.md` |
| Diagrams, writing style, quality check before delivery | `references/style-and-diagrams.md` |

## Rules that apply to every task

1. **Read-only, always.** Never create, edit, delete, import, run, activate or deactivate anything: records, workflows, forms, menus, roles, reports. Reading Production is acceptable for documentation when the user agrees; changing it never is. If someone asks for a change, say that this skill only documents and point them to the solution engineering team.
2. **The user signs in.** Never type passwords. Ask the user to sign in, choose the company and open the app, then confirm the app name shown in the header before reading anything. One account can hold several customers' apps.
3. **Secrets.** Workflow connectors can hold credentials. Record only *that* a credential exists and where (as a finding). Never print, save or quote the value. Delete raw dumps that contain secrets once parsed.
4. **Personal data.** Blur names, emails, person IDs and other personal data in every screenshot that is kept or shared.
5. **Facts, not guesses.** State what was verified. Mark anything inferred as *(inferred)*. Counts and other values that change carry the date they were read.
6. **Describe the solution as it is, not as it should be.** An existing app shows what was built, not necessarily the right way to build it. Explain it neutrally; put judgements in the findings section with evidence.
7. **Generic knowledge only in this skill.** Client IDs, app IDs, customer names and project facts go in the project's own notes, never in this skill.

## Output defaults

- **Markdown** by default, one file per deliverable, screenshots in a `screenshots/` folder next to it. **PDF only when asked** (`scripts/md-to-pdf.js`, see `references/style-and-diagrams.md`).
- **Internal audience.** No customer emails. Open questions go inside the document, each with *why we ask* and *what the answer is needed for*.
- **No production notes.** Documents name the author and the date. They never mention how they were produced: no AI assistants, browser automation, scripts, file paths or first person. Before delivering, scan for these words.
- Suggested layout: `<project>/docs/<App-Name>-Documentation.md`, `<App-Name>-PM-Guide.md`, `screenshots/NN-<what>.png`. Never overwrite another app's documents.

## Process in short

1. **Scope:** which app, which environment, which deliverable, who reads it. Look for existing docs or notes on the app first and read them.
2. **Collect:** read-only snapshot (structure, workflows, counts, last runs), then a walkthrough of every menu and one record per main form with screenshots (`references/read-only-analysis.md`).
3. **Understand:** trace the main flow end to end: who starts it, which workflows run, which statuses change, which external systems are called (`references/reading-a-cloudapper-app.md`).
4. **Analyse:** go through `references/analysis-checklist.md` and write findings with evidence.
5. **Write:** follow the structure of the chosen deliverable.
6. **Check:** run the quality checklist in `references/style-and-diagrams.md` before delivering.

## Maintaining this skill

Edit in place. Add, don't remove: extend a section or add a dated note next to an older finding. Keep everything generic. Contributions arrive through pull requests (see the repository's `CONTRIBUTING.md`).
