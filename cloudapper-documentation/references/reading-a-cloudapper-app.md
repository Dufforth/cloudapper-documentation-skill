# Reading a CloudApper app

What a reader needs to know about the platform to understand and explain an existing solution. Building details are left out on purpose.

## Contents
1. The building blocks
2. Where to find each piece
3. Forms, fields and child forms
4. Menus, roles and users
5. UI workflows vs backend workflows
6. Backend workflow triggers
7. Workflow steps (nodes) and what they mean
8. Connectors and external systems
9. Reports and dashboards
10. Environments
11. Platform behaviours that explain "strange" results
12. Tracing a flow end to end
13. Glossary

## 1. The building blocks

| Block | What it is | Explain it as |
|---|---|---|
| **Account / tenant** | The customer's CloudApper space; one account can hold several apps | "The company space" |
| **App** | One solution inside an account | "The application" |
| **Form** | A record type with fields (the data model) | "A table / a kind of record" |
| **Child form** | Records that live under a parent record (e.g. lines under an order) | "Detail lines" |
| **Menu** | Navigation entries in the runtime app | "Where users click" |
| **Role** | Which forms a user can create, edit, delete or view | "Permissions" |
| **UI workflow** | Logic that runs in the user's browser (open a form, prefill, look up by PIN) | "Screen behaviour" |
| **Backend workflow** | Logic that runs on the server (automation, integrations, calculations) | "Automation" |
| **Connector** | A workflow step that talks to an external system (UKG, REST API, SFTP, email) | "Integration call" |
| **Report** | A DevExpress report or dashboard over form data | "Printable / exported view" |

## 2. Where to find each piece

| Piece | Runtime (what users see) | App Studio (design) |
|---|---|---|
| Records | Menu → list → record details (with **Audit Log** tab) | — |
| Forms and fields | Record screens | **Solution Builder** (form tree) |
| Menus | Left navigation | **User Experience** |
| Backend workflows | Buttons that start them | **AI Agents & Automation** (list in run order, designer per workflow, execution log) |
| UI workflows | Buttons and screen behaviour | **Settings → UI Workflow Configuration** |
| Roles and users | — | Account home → **Manage User** (Users / Roles tabs) |
| Reports | **Report** menu, report buttons on forms | Report designer |

Runtime URLs look like `/<clientId>/app/<appId>/list/<formId>/<menuId>` (list) and `/details/<formId>/<recordId>` (record). App Studio uses `/design/...` for forms and menus and `/studio/...` for workflows. The client ID is a 16-digit number, the app ID a GUID. Keep both out of shared documents unless the document is about that specific app and the audience is internal.

## 3. Forms, fields and child forms

- Top-level forms are often called **entity types**, child forms **event types**. The API calls both "Schemas".
- Every record has system fields: `id`, `DisplayName` (the title), `CreateDate`, `LastModifyDate`, `CreatedBy`, `Status`, and for child records `ParentId`.
- Field internal names follow the type (`stringField3`, `dateField1`, `numericField2`). The same internal name repeats in every form, so always resolve a label by **form + field name**.
- Common field kinds: text, number, date, date-time, choice (dropdown), Yes/No, reference (a link to a record of another form; it stores display text plus the target's ID), lookup-display (a copy of a value from the referenced record), subform (a grid of child records), file.
- **Buttons** on a form can set a field value, open a report, or start a UI or backend workflow. Buttons can be shown only for certain statuses or values.
- Deleting a parent record deletes its child records.

## 4. Menus, roles and users

- Menus can be visible or hidden. A menu for a form the user's role cannot access is hidden automatically.
- Users and roles live at account level. Every app has an **Administrator** role (can design) and a **Standard User** role. Each role has **Create / Edit / Delete / View** per form. Note in the documentation which roles exist and what each one can do.
- The runtime caches the app in the browser. After design changes, users must click the refresh icon next to the app name or sign in again. "I don't see the new menu" is usually this.

## 5. UI workflows vs backend workflows

| | UI workflow | Backend workflow |
|---|---|---|
| Runs | In the user's browser | On the server |
| Typical use | Open a form for a child record, prefill fields, look up by PIN or scan, show records | Status changes, calculations, syncs, integrations, emails |
| Started by | A button, screen event | Record events, schedules, buttons, webhooks |
| Applies to API and imports? | **No** | Yes |

Validation that exists only in a UI workflow is skipped by imports, the API and backend workflows. That is a common finding.

## 6. Backend workflow triggers

| Trigger | When it runs | Note for readers |
|---|---|---|
| **Before** (create / update / delete) | Before the record is saved; can stop the save (Halt) | Used for validation |
| **After** | After the save; the user's screen waits until it ends | Long After workflows make saves feel slow |
| **After Async** | After the save, in parallel; the screen does not wait | Runs can overlap |
| **Every Time Interval** (schedule) | Hourly, daily, weekly or a cron expression, **in UTC** | Convert to the customer's time zone when documenting |
| **On Demand** | Started by a button or the ▶ Run Now in the list | "Manual run" |
| **On Demand (Data-Driven)** | Started on a chosen record | |
| **Incoming Webhook** | An external system calls the workflow's URL | The URL has no sign-in: the identifier is the only secret |

A trigger can have a **rule** (for example: only when **Status** changed and is now **Approved**). `_IsUpdated` means "this field changed in this save".

Workflow status: **Active** (on) or **Inactive** (off). A workflow saved from the designer is active at once, so test or half-built workflows are sometimes left on.

## 7. Workflow steps (nodes) and what they mean

| Designer name | Internal type | What it does |
|---|---|---|
| Trigger | TRIGGER | The start: event, schedule, button or webhook |
| Update Variable | ASSIGN_VARIABLES | Sets working values (dates, flags, lists) |
| Fetch Records (single / multiple) | LOOKUP_RECORD / LOOKUP_RECORDS | Reads records with a filter |
| Filter & Sort | FILTER_AND_SORT | Filters an earlier result in memory |
| Logic Path | ROUTER + ROUTE | Branches; **every path whose condition is true runs**, not just the first |
| Iterator | FOREACH | Loops over records, or while a condition holds |
| Create / Update / Delete Records | CREATE_RECORD / UPDATE_RECORD / DELETE_RECORDS | Writes records |
| Save Records | SAVE_RECORDS | Bulk create-or-update (upsert) on a key |
| Transform | TRANSFORM_RECORDS | Maps one data shape to another |
| Extract | EXTRACT | Parses JSON or XML text into fields |
| Connector | CONNECTOR | Calls an external system (see §8) |
| Debug Log | DEBUG_LOG | Writes text to the execution log |
| Return & Exit / Return & Continue | RETURN_JSON / RETURN_STRING_AND_CONTINUE | Answers a webhook or on-demand call |
| Show Message / Data Input / Show Records | UI_* | Talks to the user who started the workflow |

Expressions are C#-like (`UtcNow()`, `AddDays(d, n)`, `IsNull(x) ? a : b`, `ConvertFromUTCDateTime(d, tz)`). When documenting a calculation, quote the expression and explain it in plain words.

The three agent kinds in **AI Agents & Automation** (Autonomous Agent, Agent Task, Chat Agent) use the same step palette as a workflow; only the start differs. Document them like workflows and note which AI connector they call.

## 8. Connectors and external systems

- A connector step names the system and the operation. For REST connectors, record the **method and URL** (without credentials or tokens) and which variable is sent as the body. Workflows often build several payloads and send only one: read which one the connector actually sends.
- Credentials are either typed into the step (**Direct Credentials**, a finding) or kept in the credentials store (**Credential Reference**).
- Most CloudApper solutions read from or write to **UKG** (Pro HCM, Pro WFM, Ready). Name the UKG product each connector calls; they are different products with different APIs.
- A failed connector call does not always fail the run. Some REST connectors report success in the log even when the external system answered with an error. When documenting troubleshooting, tell the reader to check the external system's answer, not only the run status.
- Other common connectors: SFTP, CSV/Excel/JSON/XML file parsers, email/SMS/Slack, AI/LLM, vendor packages (Workday, ADP, Dayforce, Salesforce and others).

## 9. Reports and dashboards

- Reports are DevExpress reports over one or more forms. They open from the **Report** menu or from a button on a form.
- Dashboards live in **User Experience**. A "today" widget without a date filter shows all-time totals (finding).
- Formula and lookup-display fields are calculated on screen only: records written by workflows, imports or the API can have them empty, which makes report totals look wrong.

## 10. Environments

Most customers have a **Production** app and a **UAT** (test) app, often in different accounts. Note in the document which environment was read and the date. Differences between environments (workflow order, active/inactive workflows, setup records, external URLs) are a common source of "works in UAT, not in Production".

## 11. Platform behaviours that explain "strange" results

Use these when writing troubleshooting sections and "known behaviours that look like bugs".

| Behaviour | What the reader sees |
|---|---|
| **Workflow order matters.** A record changed by a workflow only starts workflows that sit **later** in the workflow list. | "The next step never ran" although everything is active |
| **A status trigger needs a real change.** Setting the same value again starts nothing. | A record stuck at **Running** cannot be rerun by setting **Running** again |
| **Runs triggered from one workflow go one at a time,** and a loop does not always wait for them. | A batch "finished" in seconds while its records keep changing for an hour |
| **Logic Path runs every true path.** | Two outcomes for one record (two emails, two records) |
| **After workflows hold the screen.** | Save spins for a long time |
| **After Async runs overlap and nothing is locked.** | Duplicate records with the same key |
| **Schedules are in UTC; "today" from `UtcNow()` is UTC.** | Evening runs in US time zones use tomorrow's date |
| **Synced data is restored by the next sync.** | A manual fix "comes back" |
| **Setup records must exist.** | A copied app or new environment produces no results |
| **Mandatory fields are checked on screen only.** | Records from integrations with empty "required" fields |
| **Runtime cache.** | New menus or fields not visible until refresh |
| **Names can mislead.** | A node called "DO NOT USE" may still be essential: check what reads its output |

## 12. Tracing a flow end to end

1. Start from the user's action or the schedule: which button, form or time?
2. Find the workflow it starts (button configuration, trigger form and event, schedule).
3. Read the workflow's steps in order: what it reads, decides, writes, calls.
4. For every record it writes, check which workflows trigger on that form and event, and whether they sit later in the list.
5. Follow the **Status** field: list every value, which workflow or button sets it, and what should happen next.
6. Confirm with live evidence: a real record's **Audit Log** (workflow changes show `WorkflowService`, user edits show `Web`) and the workflow execution logs around that time.

The result is the "flow in N steps" table and the status lifecycle diagram in the technical guide.

## 13. Glossary

| Term | Meaning |
|---|---|
| App Studio | The design area of CloudApper |
| Solution Builder | The form tree (data model) in App Studio |
| User Experience | Menus, dashboards and themes |
| AI Agents & Automation | Backend workflows and agents |
| Execution log | Run history of a workflow: start, end, status, per-step messages |
| Audit Log | Per-record history of field changes and who made them |
| Upsert | Create the record if it does not exist, otherwise update it |
| Sync | A scheduled or on-demand workflow that copies data from an external system |
| Halt | A Before workflow step that rejects a save with a message |
| Webhook | A URL an external system calls to start a workflow |
