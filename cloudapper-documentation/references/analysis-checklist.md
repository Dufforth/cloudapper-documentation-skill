# Analysis checklist (findings)

Recommendations state the outcome needed and who should act ("credentials moved to the credentials store and rotated; owner: solution team"), never how to build it.

Use this to write the findings section (F-01…, severity, evidence, recommendation). Each item has come up in real production apps. Review read-only: describe the risk and the direction of the fix; the fix itself is for the solution engineering team.

Severity: 🔴 **high**: security exposure, data loss or wrong results reaching users or payroll. 🟠 **medium**: failures that need manual work, performance, environment mix-ups. 🟡 **low**: housekeeping, naming, documentation gaps.

Each finding needs **evidence**: the workflow and step, form and field, a count, a run log line or a screenshot, with the date read.

## Security and secrets
- Credentials typed into connector steps (including inactive and test copies) → move to the credentials store, rotate.
- Credentials kept as plain fields in a setup form that users can read → restrict, move to the credentials store, rotate.
- Incoming webhook workflows: no sign-in, the identifier is the only secret → check the workflow validates a shared secret; switch off unused ones; keep URLs out of documents.
- Public links protected only by a GUID (approval pages) → accept the risk explicitly or add expiry.
- Visible sequential IDs used as PINs.
- Restricted users on the default Standard User role, which can have full rights on new forms → a dedicated role.

## Environments
- UAT calling Production external tenants, or the reverse; base URLs typed into many steps.
- Workflow order, on/off state or setup records differ between UAT and Production.
- Hard-coded email recipients or "Prod" names in UAT.

## Workflow logic
- Logic Path branches assumed exclusive (every true path runs); conditions that are always true (`!= A OR != B`); dead branches (`1 = 0`); Debug Log steps left in.
- A workflow that should trigger another sits after it in the list, so the chain never fires.
- A workflow writes the status that triggers itself, or a rerun cannot restart a stuck status.
- The same list, threshold or date copied into several workflows, and the copies disagree.
- Business rules keyed on a person's name.
- Pairing records by "newest by create date"; durations cut by whole-hour differences.
- Business dates from `UtcNow()` without converting to the customer's time zone.
- Before workflows with side effects on other records.
- Test or one-off workflows left active (especially recurring or "delete all").

## Integrations and syncs
- Syncs that only create (duplicates) instead of create-or-update on an external ID; check record counts against the source.
- No handling for timeouts or empty answers; no retry; no log of failed payloads.
- Connector failures that do not stop the run, or REST steps that log success on an error answer.
- One external call per employee where a bulk or report endpoint exists; full pulls where incremental would do. State calls per run and run time.
- A connector built for a different product than the one called (for example the wrong UKG product).
- No sync log (one record per run with counts and errors).
- Change detection that depends on someone remembering to run an on-demand sync.
- Changes in the source (corrections, deletions) never reflected after the first import.

## Data and screens
- Validation only in UI workflows or Mandatory fields (skipped by API, imports and workflows).
- Formula or lookup-display fields used in reports or rules (empty for records written by workflows).
- Matching or reporting on reference display text instead of the record link.
- Child records holding history that disappears when the parent is deleted.
- Status fields users can edit by hand; status values no workflow ever sets.
- Choice fields written with labels where keys are stored (missing from boards and rules).
- Setup forms no workflow reads.
- "Today" dashboard widgets without a date filter.
- Typos, the same label meaning different things on different forms, menus opening the wrong form.

## Performance and operations
- Long After workflows that make every save wait.
- Loops that start many triggered runs and finish before them; overlapping batches.
- Execution logs showing long runs, frequent failures or runs stuck at "running".

## Housekeeping
- Workflows without descriptions; many near-identical workflows.
- No inactive backup copy kept before core workflow changes.
- Credential or configuration pages in wikis.

## Writing a finding

| # | Severity | Finding | Evidence | Recommendation |
|---|---|---|---|---|
| F-01 | 🔴 | A sync workflow holds a typed-in API password | Workflow *Employee Sync*, step *Get Token*, read 2026-01-15 | Move to the credentials store and rotate |

Then list the priorities: **now** (🔴), **next** (🟠 that cause manual work), **later**.
