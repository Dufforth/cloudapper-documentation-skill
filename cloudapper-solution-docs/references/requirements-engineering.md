# Requirements engineering for CloudApper solutions (ISO/IEC/IEEE 29148, tailored)

How requirements are gathered, written, checked, traced and changed. Document structures: `business-requirements.md` (BRD) and `srs.md` (SRS).

## Contents
1. Process
2. Sources and elicitation
3. Writing a good requirement
4. Priority and source confidence
5. Acceptance criteria
6. Traceability
7. Review and approval
8. Change control
9. CloudApper-specific questions to ask

## 1. Process

| Step | What happens | Output |
|---|---|---|
| 1. Frame | Business problem, sponsor, users, systems involved, deadline | BRD sections 1–3 draft |
| 2. Elicit | Sessions, existing spreadsheets and forms, tickets, current app (read-only), system of record (e.g. UKG) | Notes with dates (sources R1, R2…) |
| 3. Analyse | As-is and to-be process, business rules, data, volumes, conflicts, gaps | BRD complete, open issues |
| 4. Specify | Functional, quality, interface and data requirements with acceptance criteria | SRS draft |
| 5. Validate | Walk the customer and the team through the BRD and SRS; check each requirement against §3 | Review comments, version 0.9 |
| 6. Approve | Customer owner and PM sign off | Version 1.0 baseline |
| 7. Manage | Change requests, traceability kept current, UAT cases derived | New versions, UAT plan |

## 2. Sources and elicitation

- Record every source as a reference row (R1: "Requirements session, 2026-03-04, customer HR and payroll"). Each requirement cites its source.
- Prefer concrete artefacts over opinions: the spreadsheet used today, a pay-code list, a sample file, a screenshot of the current process, an API response.
- Ask for **examples with numbers**: "show three employees and what their result should be". Examples become acceptance criteria and UAT data.
- Separate **what** (need, rule, outcome) from **how** (screens, workflows). Requirements state what; the design decides how.
- When a meeting transcript is the source, quote the decision, not the discussion, and note who decided.

## 3. Writing a good requirement

Form: **"The system shall <do something observable> [when / for <condition>] [within <limit>]."** Business rules: "**BR-3** An employee with more than 40 hours in a week receives overtime at 1.5 × the base rate."

Each requirement must be (29148 characteristics):

| Characteristic | Test it with | Bad → good |
|---|---|---|
| Necessary | Would anyone miss it? Linked to a BO or StR? | — |
| Appropriate | Right level: what, not how | "Add a workflow that loops employees" → "The system shall calculate the weekly total for every active employee" |
| Unambiguous | One reading only; no "fast", "user-friendly", "etc." | "Sync quickly" → "Changes made in UKG appear within 30 minutes" |
| Complete | Condition, actor, result, limits stated | "Send a notification" → "…email the supervisor when a request is submitted" |
| Singular | One requirement, no "and/or" chains | Split into two IDs |
| Feasible | Possible on the platform and the integrated system, within budget | Check with a solution engineer |
| Verifiable | A test can pass or fail it | Has acceptance criteria |
| Correct | Confirmed by the source owner | Source confidence *Stated* |
| Conforming | Follows this template and the glossary terms | — |

As a set, requirements must also be **complete** (every BO covered), **consistent** (no conflicts), **bounded** (out-of-scope list) and **affordable**.

Words to avoid: *should* (use *shall*, priority carries importance), *all/always/never* without a scope, *as appropriate*, *support*, *handle*, *user-friendly*, *flexible*, *real time* without a number.

## 4. Priority and source confidence

- **MoSCoW:** **M** must (release fails without it), **S** should (important, workaround exists), **C** could, **W** won't this release (keep it listed).
- **Source confidence:** *Stated* (customer said it, with source), *Proposed* (team proposed, customer did not reject), *Inferred* (derived; needs confirmation, becomes an open issue).

## 5. Acceptance criteria

- Observable and testable: Given / When / Then, or a table of inputs and expected outputs.
- Use real-looking examples with numbers and edge cases (zero, boundary, missing data, late changes, terminated employee, time zone edge).
- Each criterion becomes at least one UAT test case (`uat-test-documentation.md`).

Example:

| ID | Requirement | Acceptance criteria |
|---|---|---|
| FR-07 | The system shall flag a timecard with more than 12 hours in one day for supervisor review. | Given a shift of 12 h 01 min, when the daily check runs, then the timecard shows status **Review** and the supervisor receives one email. A shift of exactly 12 h 00 min is not flagged. |

## 6. Traceability

Keep one matrix, updated with every version:

| BO / StR | BR | FR / NFR | IF / DR | TC | Delivered by (as built) |
|---|---|---|---|---|---|
| BO-1 | BR-3 | FR-07, NFR-02 | IF-01 | TC-07, TC-08 | Workflow *Daily Hours Check* |

Rules: every FR traces back to a BO or StR (no orphan features) and forward to at least one TC (nothing untested). The last column is filled after the build from the as-built technical guide.

## 7. Review and approval

- Review with the customer owner (business correctness), a solution engineer (feasibility on the platform and the integrated system) and a tester (verifiability).
- Record decisions in the approval table; open questions stay as OI-n with owner and date.
- Version 1.0 is the baseline for the build and for UAT.

## 8. Change control

1. Change request logged (ticket) with reason and requester.
2. Impact: which requirements, interfaces, test cases and existing workflows change; effort.
3. Decision by the customer owner and PM.
4. New document version; changed rows marked *(changed in vX.Y)*; withdrawn rows kept with status **Withdrawn**; traceability and UAT cases updated.

## 9. CloudApper-specific questions to ask

| Topic | Ask |
|---|---|
| Users and roles | Who creates, approves, views? On web, tablet, kiosk? Shared devices with PIN? |
| System of record | Which system owns each data item (for example UKG Pro WFM owns timecards)? What may the app change there? |
| Volumes | Employees, records per day, peak times, history to keep |
| Timing | How fresh must synced data be? Which time zones? When do schedules run (platform schedules are in UTC)? |
| Environments | UAT and Production accounts; test tenant of the external system; who tests |
| Rules | Where business rules and lists live today; who maintains them after go-live |
| Notifications | Who is told what, how (email, SMS, Teams/Slack), how often |
| Reports and exports | Layout, filters, file format, who receives them |
| Errors | What happens when the external system is down or data is missing; who fixes it |
| Security and privacy | Personal data, retention, who may see what, audit needs |
| Migration | Existing data to load; from where; one-off or recurring |
| Support | Who supports the app after go-live; what they need documented |
