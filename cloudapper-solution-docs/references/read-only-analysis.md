# Read-only analysis: access, data collection, screenshots

How to collect everything a document needs without changing anything in the app.

## Contents
1. Access and confirming the app
2. What to collect
3. Read-only snapshot through the APIs
4. Walkthrough and screenshots
5. Personal data and secrets
6. Allowed and forbidden actions

## 1. Access and confirming the app

1. Ask which app, which environment (Production or UAT) and which deliverable.
2. The user signs in, picks the company and opens the app. Never type passwords and never click through companies or apps to find it: an account can hold other customers' apps.
3. Read the app name in the page header and the client and app IDs in the URL. Say which app you are on before reading anything. Stop if it does not match.
4. If the app already has documentation or project notes, read them first and only fill the gaps.

## 2. What to collect

| Area | Facts to collect |
|---|---|
| Data model | Forms, child forms, key fields, references, record count per form (with date) |
| Navigation | Visible menus and what each opens |
| Roles | Roles, what each can do per form, who uses them |
| Screens | Main list and detail screens, buttons per status |
| Backend workflows | Name, active/inactive, trigger (form, event, rule, schedule), position in the list, steps, records written, status changes, connector calls (method + URL), hard-coded values |
| UI workflows | Name, trigger, what it opens or fills |
| Integrations | External systems, operations, how credentials are stored (not the values) |
| Live behaviour | Last runs per workflow (status, duration), errors in the last weeks |
| Reports | Report names, forms they read, where users open them |

## 3. Read-only snapshot through the APIs

Reading through the app's own APIs is faster and more exact than clicking. Use only read calls, from inside the signed-in browser page so the session token is at hand. API hosts depend on the cluster; find them in the browser's network tab.

| Purpose | Call (read only) |
|---|---|
| App structure: forms, fields, child relations, menus, roles, UI workflows | `GET <api>/v3/Apps/{appId}/details` |
| Backend workflows with full definitions | `GET <api>/v3/Workflows` (large: save to a file, return summaries) |
| One workflow | `GET <api>/v3/Workflows/{AutomationId}` |
| Record count of a form | `POST <api>/v3/Records/fetch` with `TotalRows: 1` → read `Count` |
| Recent runs of a workflow | `POST <api>/v3/auditlogs/workflows/fetch-execution-log` `{AutomationId, StartRow: 0, TotalRows: 20}` → status 1 ok, 2 failed, 3 running |
| Who changed a record | `POST <api>/v3/auditlogs/fetch` filtered on `EntityId` = record id |

Never call create, update, delete, run, sequence or save endpoints.

Working method:
1. Save the app details and workflow JSON to the project folder, after masking every key that matches `password|secret|apikey|token|clientid|authorization` and any `Bearer …` text. Mask in the browser before the data leaves it.
2. Return only counts to the conversation, then read the saved files with small local scripts: inventory of forms and fields, workflow step trees (`AutomationConfiguration.root`, children run in order), form usage (forms no workflow touches), connector calls.
3. Expression placeholders (`__argNNN__`) are numbered globally. Replace each with the entry in `Arguments` whose `Name` equals it, never by list position.
4. Run a leak check on the saved files: no secret-like key may still hold a value.
5. Collect live signals as numbers only: counts per form, last run status and duration per workflow.

Workflow fields worth knowing: `Status` 1 = active, 2 = inactive; `TriggerType` 1 Before, 2 After, 8 After Async, 3 schedule (`ScheduleExpression`, Quartz cron in UTC), 4 on demand, 6 webhook; `TriggeredOn` 1 create, 2 update, 4 create or update; `TypeId` = the form; `Sequence` = position in the list.

## 4. Walkthrough and screenshots

1. Open every menu and list screen, one record of each main form (Details, child tables, **Audit Log** tab) and the buttons per status.
2. Screenshots at **1920 × 1080**. Never capture a loading state: wait until the list shows `record(s)` and no overlay is visible ("Loading...", "preparing your app environment", spinners, the cloud watermark, grey skeleton boxes, charts still loading). The app keeps a hidden loading element in the page after loading, so test only *visible* elements. Then pause about 1.5 s.
3. Blur personal data **after** the wait (late-loaded rows would stay readable otherwise). Blur every column that holds people's names, not only the obvious ones. Leave the `record(s)` footer readable.
4. Look at every saved screenshot. Retake it if any overlay, spinner, blank grid, wrong size or unblurred personal data shows.
5. Name files `NN-<what>.png` in reading order.

Useful App Studio screenshots for the appendix: the workflow list (order and on/off state) and the designer view of the most complex workflow.

## 5. Personal data and secrets

- Blur names, emails, person IDs, phone numbers and IPs in screenshots. Do not copy record data into documents beyond counts and anonymised examples.
- Credentials found in workflow steps or setup records are a **finding**: write *where* (workflow and step, or form and field) and *what kind*, never the value.
- Delete raw dumps with secrets once parsed and say which folders still hold snapshots.
- Snapshots hold structure, not records, but keep them inside the project folder and out of shared repositories.

## 6. Allowed and forbidden actions

| Allowed | Forbidden |
|---|---|
| Open menus, lists, records, tabs | Create, edit, delete, import or export-then-reimport records |
| Read the designer, workflow list, execution logs | Save anything in the designer, even unchanged |
| Read API calls listed in §3 | Run, activate, deactivate or reorder workflows |
| Open reports in the viewer | Click action buttons that change status or start workflows |
| Screenshots | Change roles, users, menus or settings |

If a fact can only be confirmed by running something, write it as an open question in the document (why it matters, what the answer is needed for) instead of running it.
