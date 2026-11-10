---
name: cloudapper-solution-docs
description: Documentation and analysis for CloudApper solutions (apps on web.cloudapper.com, m2sys.cloudapper.com or another tenant), following ISO-based engineering documentation practice - Business Requirements Documents (ISO/IEC/IEEE 29148), Software Requirements Specifications with functional, non-functional (ISO/IEC 25010), interface and data requirements, UAT test plans and test cases (ISO/IEC/IEEE 29119-3), technical and troubleshooting guides for solution engineers (ISO/IEC/IEEE 42010 views), PM handover guides for business and project understanding (ISO 21502), and analysis reports with findings from a read-only review of an existing app. Use when asked to write requirements, an SRS, functional requirements, a BRD, UAT test cases, or to document, explain, analyse, review, audit or hand over a CloudApper app or solution. Markdown by default, PDF on request. It does not cover building or changing apps.
---

# CloudApper solution documentation and analysis

This skill produces the documents a CloudApper solution needs across its life: **requirements before the build, test documents to accept it, and as-built guides to support and hand it over**, plus analysis of existing apps. Each document follows the structure and quality rules of an ISO/IEC/IEEE standard, tailored for no-code business solutions (`references/standards-map.md`). Building and changing apps is out of scope.

## Deliverables

| Deliverable | Reader | Standard | Guide | Template |
|---|---|---|---|---|
| **Business Requirements Document (BRD)**: why and what the business needs | PM, customer owner, team | ISO/IEC/IEEE 29148 (BRS/StRS) | `references/business-requirements.md` | `templates/brd-template.md` |
| **Software Requirements Specification (SRS)**: functional, quality, interface, data requirements | Solution engineers, testers, PM | 29148 SRS + ISO/IEC 25010 | `references/srs.md` | `templates/srs-template.md`, `templates/srs-quarto/` (PDF) |
| **UAT test plan and test cases** | Testers, key users, PM | ISO/IEC/IEEE 29119-3 | `references/uat-test-documentation.md` | `templates/uat-test-cases-template.md` |
| **Technical and troubleshooting guide** (as built) | Support analysts, solution engineers | ISO/IEC/IEEE 42010 views, 26514 user information | `references/technical-guide.md` | `templates/technical-guide-template.md` |
| **PM handover guide**: business and project understanding | Project and account managers | ISO 21502 | `references/pm-handover-guide.md` | `templates/pm-guide-template.md` |
| **Analysis report**: findings and priorities | Team leads, managers | ISO/IEC 25010 quality characteristics | `references/analysis-checklist.md` | `technical-guide.md` §8 |

## Read before you start

| Task | Read |
|---|---|
| Choose the right document and standard; tailoring decisions | `references/standards-map.md` |
| Document control block, versions, IDs used across documents | `references/document-control.md` |
| Gather, write, check, trace and change requirements | `references/requirements-engineering.md` |
| Understand CloudApper concepts well enough to explain or specify a solution | `references/reading-a-cloudapper-app.md` |
| Collect facts from an existing app without changing it | `references/read-only-analysis.md` |
| Find risks and write findings | `references/analysis-checklist.md` |
| Diagrams, writing style, PDF, quality check before delivery | `references/style-and-diagrams.md` |

## Rules that apply to every task

1. **Read-only, always.** When an existing app is involved, never create, edit, delete, import, run, activate or deactivate anything. Reading Production is acceptable for documentation when the user agrees; changing it never is. Requests to change an app go to the solution engineering team.
2. **The user signs in.** Never type passwords. Ask the user to sign in, choose the company and open the app, then confirm the app name in the header before reading. One account can hold several customers' apps.
3. **Secrets.** Record only *that* a credential exists and where (as a finding). Never print, save or quote the value. Interface requirements name the authentication method, never the credential.
4. **Personal data.** Blur names, emails, person IDs and other personal data in every screenshot kept or shared; requirement examples use invented or anonymised people.
5. **Facts, not guesses.** State what was verified or stated, with the source. Mark inferred content *(inferred)* and turn it into an open issue. Values that change carry the date they were read.
6. **What, not how, in requirements.** BRD and SRS describe needs and behaviour in business terms; they do not prescribe forms, workflows or nodes.
7. **Describe existing solutions as they are.** Judgements go in the findings with evidence.
8. **Generic knowledge only in this skill.** Client IDs, app IDs, customer names and project facts go in the project's own notes.

## Output defaults

- **Markdown** by default, one file per deliverable, screenshots in `screenshots/`. **PDF only when asked** (`scripts/md-to-pdf.js`, or Quarto for the SRS; see `references/style-and-diagrams.md`).
- Every document starts with the **document control block** and cites its standard as "structure based on …, tailored for CloudApper solutions". Never claim conformance or certification.
- **Internal audience** unless the user says a document is customer-shareable. Open questions go inside the document with *why we ask* and *what the answer is needed for*.
- Documents name the author and the date and never mention how they were produced: no AI assistants, browser automation, scripts, file paths or first person. Scan before delivering.
- Suggested layout: `<project>/docs/<App-or-Project>-<TYPE>.md` (BRD, SRS, UAT, Technical-Guide, PM-Guide, Analysis), `screenshots/NN-<what>.png`. Never overwrite another project's documents.

## Process in short

**New solution (requirements):** frame → elicit (sources R-n) → BRD → SRS with acceptance criteria → review and approve (v1.0 baseline) → UAT plan and cases → after the build, as-built technical guide and PM guide → keep traceability current through change requests. Details: `references/requirements-engineering.md`.

**Existing solution (documentation or analysis):** scope → read-only snapshot and walkthrough → trace the main flow → findings → write → quality check. Details: `references/read-only-analysis.md`. Where an existing app has no requirements, an *as-built SRS* can be reverse-engineered (source confidence *Inferred*, confirmed with the customer).

## Maintaining this skill

Edit in place. Add, don't remove: extend a section or add a dated note next to an older finding. Keep everything generic. Contributions arrive through pull requests (see the repository's `CONTRIBUTING.md`).
