# Contributing to the CloudApper Documentation Skill

This skill grows from real documentation and analysis work. Add what would help the next person understand or document a CloudApper solution, as **generic, verified knowledge**. Every change goes through a pull request and is merged only after the owner (Pablo Huanca) approves it.

## What belongs here

- How to read and explain a part of CloudApper (a node type, a trigger, a screen, a log).
- Behaviours that confuse readers and how to explain them in troubleshooting sections.
- New risks for `analysis-checklist.md`, with severity guidance.
- Better document structures, templates, diagram tips, quality checks.
- Requirements practice: elicitation questions, well-written requirement and acceptance-criteria examples, traceability and UAT patterns.

## What does not belong here

- How to build, configure or change apps (forms, workflow construction, write APIs, integration design). This repository covers analysis and documentation only.
- Client IDs, app IDs, customer or employee names, customer business rules, record data.
- Credentials of any kind.
- Project status or meeting notes.

## Rules for editing

1. **Add, don't remove.** Extend a section or add the newer finding next to the old one with a date.
2. **Keep the structure.** Put a topic in the reference that owns it; a new reference file gets a row in `SKILL.md`.
3. **Read-only stays read-only.** Never add instructions that change an app.
4. Don't edit `VERSION` or `CHANGELOG.md`; the owner does that on merge.

## How to propose a change

1. Fork the repository on GitHub (once) and add it as a remote: `git remote add fork https://github.com/<your-user>/cloudapper-documentation-skill.git`.
2. `git pull origin main`, then `git checkout -b add/<short-topic>`.
3. Edit, commit with a clear message ("analysis-checklist: webhook workflows without secret check"), `git push fork <branch>`.
4. Open a pull request into `main` and fill in the template. The automatic checks must pass.
5. The owner reviews and merges.

With Claude Code you can say: *"Add this lesson to the cloudapper-solution-docs skill on a new branch and open a pull request from my fork."*
