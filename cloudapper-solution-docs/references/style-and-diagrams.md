# Style, diagrams and quality check

## Writing style

- Short sentences, plain words, active voice. Tables over paragraphs.
- Bold the UI labels the reader clicks (**Run Calculation**) and status values (**Pending**).
- Use the exact form, workflow and node names from the app so readers can search for them.
- Every gap or risk mentioned in the body points to its finding ID (F-xx) or risk ID (R-xx).
- Counts and other changing values carry the date they were read.
- Verified facts only; mark inferences *(inferred)* and unconfirmed people facts **[confirm]**.
- Open questions inside the document, each with why we ask and what the answer is needed for.
- Write as the named author. No first person, no "as requested", no mention of AI assistants, browser automation, scripts or file paths. Mentions of the product's own AI or automation features are fine.

## Diagrams

- **Mermaid only:** `flowchart`, `stateDiagram-v2`, `sequenceDiagram`, `erDiagram`.
- **Show only the running solution:** business users, the CloudApper app, its workflow service and API, external systems (UKG, SFTP, email). Leave out design-time and production tooling: no engineers, no App Studio, no automation or documentation tools. App Studio may appear in the text and screenshots.
- Label edges with the trigger or call (`User: Submit`, `GET /api/...`, `status = Approved`).
- Prefer `flowchart TB` for component diagrams (wide diagrams become unreadable on A4) and `flowchart LR` for decision trees with many branches. Split a diagram rather than shrink the text.
- Quote labels, or avoid `( ) [ ] { }` inside node text, when Mermaid fails to parse.

## PDF (only on request)

`scripts/md-to-pdf.js` turns the Markdown (with Mermaid and images) into a PDF using Node and Playwright with headless Chromium. Mermaid and the Markdown parser load from a CDN, so it needs internet.

```bash
node <skill folder>/scripts/md-to-pdf.js docs/<App>-Documentation.md docs/<App>-Documentation.pdf
```

- `SHOT_DIR=<folder>` saves each diagram as a PNG at page width for checking; `SKIP_PDF=1` skips the PDF while iterating.
- If `require('playwright')` fails, set `PW_PATH` to an installed playwright package. If a browser build is missing, set `CHROME_EXE` to an installed headless Chrome.
- Expect `0 broken` images, `error: none`, and as many diagrams as Mermaid blocks.

## Quality checklist before delivery

- [ ] Sections 2 and 3 (technical guide) or section 1 (PM guide) make sense on their own.
- [ ] Every screenshot: loaded, 1920 × 1080, personal data blurred.
- [ ] No credentials, tokens, webhook URLs or customer personal data in the text.
- [ ] Every finding has evidence and a date; every body mention links to an F-xx or R-xx.
- [ ] Names match the app exactly.
- [ ] Diagrams render and are readable at page width.
- [ ] Open questions have why / what for.
- [ ] Forbidden-word scan passed: no mention of AI assistants, automation tools, scripts, file paths or first person.
- [ ] Author and date in the header.
