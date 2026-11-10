# Technical and troubleshooting guide

Goal: a reader who has never seen the app can (1) understand how it works and (2) start troubleshooting **as soon as possible**. Solution engineers can also find what each core workflow does. Sections 2 and 3 must work on their own for someone who reads nothing else.

Skeleton: `templates/technical-guide-template.md`.

## Header block (under the title)

The document control block (`document-control.md`, type TG) plus: platform and tenant, environment read, integration targets, "read-only walkthrough", and a note that personal data in screenshots is blurred. Standard line: "Architecture views based on ISO/IEC/IEEE 42010:2022, user information on ISO/IEC/IEEE 26514:2022, tailored for CloudApper solutions."

## Architecture views (ISO/IEC/IEEE 42010, tailored)

Section 4 opens with a stakeholders and concerns table (stakeholder | concern | answered in), then five views. Each view answers the concerns of named readers.

| View | Answers | Shown as |
|---|---|---|
| Context | Who uses the app, which systems it talks to | Context flowchart (users, app, external systems) |
| Data | Which record types exist, how they relate, which system owns each | ER diagram, forms table with source of truth |
| Process | How a record moves through statuses and which workflow moves it | Flow-in-N-steps table, `stateDiagram-v2`, sequence diagram |
| Integration | What is exchanged with each external system, when, how it fails | Endpoints table, schedules, error behaviour |
| Environment | UAT and Production apps, external tenants, differences between them | Environment table |

If the solution has an SRS, link each core workflow to the requirement IDs it delivers (traceability column "Delivered by").

## Structure

### 1. What the application is for
The business problem, what the app automates (numbered list), who uses it, and one line: "Read section 2 to understand the app, section 3 if something is broken now."

### 2. How the application works (one-page view)
- **Flow in N steps** table: step | what happens | started by (user button / schedule / event / on demand / webhook) | workflow | status after.
- **End-to-end flowchart:** users, forms, workflows, external system calls.
- **Status lifecycle** (`stateDiagram-v2`) with the workflow or button that moves each transition. Say what a record "stuck" in each intermediate status means.

### 3. Troubleshooting quick start
- **3.1 First five minutes:** numbered checklist: find the record → read status and error field → Audit Log → related tabs → compare with the external system → decide data issue vs app issue.
- **3.2 Triage diagram:** decision flowchart from "problem reported" to an action, branching on whether the record exists, then on status, then on error text.
- **3.3 Symptoms and fixes:** Symptom | Likely cause | What to do (who to contact, what to check).
- **3.4 Known behaviours that look like bugs:** design gaps and platform behaviours (see `reading-a-cloudapper-app.md` §11), each linked to a finding ID, so nobody escalates them as incidents.
- **3.5 What to send when escalating:** record IDs, status, error text, Audit Log screenshot, external-system state, time of the problem with time zone.

### 4. Architecture
Components diagram, layer table, external endpoints table (purpose | method | endpoint without credentials | used by), ER diagram, forms table (form | menu location | record count with date | purpose).

### 5. User guide
Sign-in and navigation, menus table, the main screen, the step-by-step work procedure (step | status before | button | what happens), then each other screen with its screenshot.

### 6. Internal processing in detail
One subsection per workflow stage: trigger, numbered steps, hard-coded values, external calls, status writes. A sequence diagram for the most complex stage. Scheduled syncs as a table: workflow | schedule (cron, UTC and local time) | what it pulls | volume.

### 7. Core workflow reference
Only the workflows that carry the business logic (no generic syncs, tests or inactive ones).
- Index table: workflow | role | trigger | position in the list.
- **7.1 Before anyone changes anything:** where workflows live, node types table, the platform behaviours that make changes risky (order in the list, status triggers, Before vs After, test in UAT first, copy the workflow before editing, lists duplicated across workflows).
- One subsection per core workflow: purpose, trigger, variables and hard-coded lists in full, node-by-node table (order | designer node name | type | what it does), routing conditions table, fields written, things to know (failure behaviour, dead branches such as `1 = 0`, re-run effects, edge cases). Add a diagram where the execution order is not obvious.
- Common adjustments: change request → workflow › node → what would need to change (description only; the change itself is for the solution engineering team).
- Use exact designer node names. Mark anything inferred. Values cut off in the export get "…" and a pointer to the node.

### 8. Findings and recommendations
Table: # (F-01…) | severity (🔴 high, 🟠 medium, 🟡 low) | finding | evidence | recommendation. Then a suggested priority list (now / next / later). Use `analysis-checklist.md`.

### 9. Appendix: workflow inventory
Active workflows (name | trigger | role, ⚠ for test or one-off ones) and inactive ones as a list. Screenshots of the workflow list and designer. Open questions with why we ask and what the answer is needed for.

## Analysis report (findings only)

For managers who need the state of a solution rather than a manual: title block, one-paragraph summary ("In one sentence"), the at-a-glance table from the PM guide, then sections 2 (one-page view), 8 (findings and priorities) and the open questions.
