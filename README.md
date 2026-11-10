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
| `…/templates/` | BRD, SRS, UAT, technical guide and PM guide skeletons (Markdown) |
| `…/templates/srs-quarto/` | SRS layout for a polished PDF (Quarto + Typst) |
| `…/templates/report-quarto/` | Report layout for analysis and test reports: PDF and interactive HTML, charts, annotated screenshots |
| `…/scripts/md-to-pdf.js` | Markdown + Mermaid diagrams to PDF (Node + Playwright) |
| `…/scripts/md2pdf.py` | Plain Markdown to PDF (Python + Chrome) |
| `docs/CloudApper-Documentation-Method.md` | The documentation method explained for managers |

## Installation guide

### 1. What you need

| Tool | Needed for | Required? | Check it works |
|---|---|---|---|
| [Git](https://git-scm.com/downloads) | Getting and updating the skill | Yes | `git --version` |
| [Claude Code](https://docs.claude.com/en/docs/claude-code) | Running the skill | Yes | `claude --version` |
| [Node.js](https://nodejs.org/) 18 or newer | `md-to-pdf.js`, browser walkthroughs | Yes | `node --version` |
| Playwright + Chromium | `md-to-pdf.js` (renders Mermaid and prints the PDF) | For PDFs | `npx playwright --version` |
| Playwright MCP | Read-only walkthroughs and screenshots of an app | For app analysis | `claude mcp list` |
| [Quarto](https://quarto.org/docs/get-started/) 1.5 or newer (includes Typst) | SRS and report PDFs | For polished PDFs | `quarto --version` |
| [Python](https://www.python.org/downloads/) 3.10 or newer | Report charts, screenshot annotation, `md2pdf.py` | For reports | `python --version` |
| Poppler (`pdftotext`, `pdfinfo`) | Checking finished PDFs | Optional | `pdftotext -v` |
| Google Chrome | `md2pdf.py` | Optional | — |

Tested on Windows 11 with Node 26, Quarto 1.10, Python 3.15 and Chromium from Playwright.

Mermaid and the Markdown parser used by `md-to-pdf.js` load from a CDN, so PDF generation needs internet access.

### 2. Install the skill

Claude Code reads skills from `~/.claude/skills/` (Windows: `C:\Users\<you>\.claude\skills\`).

```bash
git clone https://github.com/Dufforth/cloudapper-documentation-skill.git ~/cloudapper-documentation-skill
```

Link the skill folder into Claude Code's skills folder.

Windows (PowerShell, no admin rights needed):

```powershell
New-Item -ItemType Junction -Path "$env:USERPROFILE\.claude\skills\cloudapper-documentation" -Target "$env:USERPROFILE\cloudapper-documentation-skill\cloudapper-documentation"
```

macOS / Linux:

```bash
ln -s ~/cloudapper-documentation-skill/cloudapper-documentation ~/.claude/skills/cloudapper-documentation
```

Instead of linking, you can copy `cloudapper-documentation/` into `~/.claude/skills/`; copy it again after each update. If `~/.claude/skills` is itself a git repository, add `/cloudapper-documentation/` to its `.gitignore`.

### 3. Install the PDF tools

**Playwright and Chromium** (for `md-to-pdf.js`):

```bash
npm install -g playwright
```

```bash
npx playwright install chromium
```

Troubleshooting:
- `Cannot find module 'playwright'`: point the script at the installed package, for example in PowerShell `$env:PW_PATH = "$(npm root -g)\playwright"`.
- `browserType.launch: Executable doesn't exist at …chrome-headless-shell…`: the Playwright package is newer than the downloaded browser. Run `npx playwright install chromium` again, or set `CHROME_EXE` to an existing browser, for example `$env:CHROME_EXE = "$env:LOCALAPPDATA\ms-playwright\chromium_headless_shell-<build>\chrome-headless-shell-win64\chrome-headless-shell.exe"`.
- A successful run prints `images: … 0 broken` and `diagrams rendered: N error: none`.

**Quarto** (for the SRS and report templates): install from <https://quarto.org/docs/get-started/>. Typst comes with it; Mermaid diagrams render without extra installs.

```bash
quarto check
```

The templates use the *Segoe UI* font (standard on Windows). On macOS or Linux, change `mainfont` in the template's `_quarto.yml` to an installed font.

**Python packages** (for the report template and `md2pdf.py`):

```bash
pip install jupyter pandas matplotlib itables tabulate pillow markdown
```

**Poppler** (optional, to check PDFs): Windows via MSYS2 (`pacman -S mingw-w64-ucrt-x86_64-poppler`) or the Poppler for Windows binaries; macOS `brew install poppler`; Linux `sudo apt install poppler-utils`.

### 4. Browser access for app walkthroughs

Analysing an existing app needs a browser that Claude Code can drive. The Playwright MCP is recommended: it can capture batches of screenshots straight to disk and works with the window in the background.

```bash
claude mcp add playwright --scope user -- npx @playwright/mcp@latest
```

You sign in to CloudApper yourself in the browser window it opens; the skill never types passwords and only reads.

### 5. Check the installation

1. Start a new Claude Code session and ask: *"Which skills do you have for CloudApper documentation?"* It should name `cloudapper-documentation`.
2. Test the PDF script on the manager guide:

   ```bash
   node ~/cloudapper-documentation-skill/cloudapper-documentation/scripts/md-to-pdf.js ~/cloudapper-documentation-skill/docs/CloudApper-Documentation-Method.md ~/method-test.pdf
   ```

   Expect `0 broken`, `error: none`, and the PDF at `~/method-test.pdf`.
3. Test Quarto: copy `templates/srs-quarto/` to a scratch folder and run `quarto render` there; expect `SRS.pdf`.

### 6. Update

```bash
git -C ~/cloudapper-documentation-skill pull
```

A linked install picks up the changes in the next session.

## Using the skill

Start a new Claude Code session and ask, for example:
- *"Write a BRD and an SRS for {project} from these session notes."*
- *"Create UAT test cases from the approved SRS."*
- *"Document the {App Name} CloudApper app as a technical and troubleshooting guide."*
- *"Write a PM handover guide for this CloudApper solution."*

## Versions

`VERSION` holds the current version; `CHANGELOG.md` lists what changed and why, newest first. Patch for added content, minor for structural changes.

## Contributing

The repository is public: anyone can clone and use it. To propose a change, see `CONTRIBUTING.md`: fork, branch, pull request; merged only after the owner approves.
