# Software Requirements Specification (SRS)

ISO/IEC/IEEE 29148 SRS, with non-functional requirements organised by the ISO/IEC 25010:2023 quality model. It states **what the CloudApper solution shall do and how well**, precisely enough to build, test and accept it. Readers: solution engineers, testers, PM, customer owner. Process and writing rules: `requirements-engineering.md`.

Skeletons: `templates/srs-template.md` (Markdown, default) and `templates/srs-quarto/` (polished PDF, on request).

## Structure

0. **Document control** (`document-control.md`), with the link to the approved BRD version.
1. **Introduction:** purpose, scope (solution name, what it does, what it does not), definitions and acronyms, MoSCoW and source-confidence legend, references (R-n).
2. **Overall description:**
   - Product perspective: context diagram (users, the CloudApper app, external systems only).
   - Business context: link to BO-n and the to-be process in the BRD.
   - User classes: user class | tasks | frequency | device (web, tablet, kiosk, mobile) | role.
   - Operating environment: CloudApper tenant, UAT and Production apps, external systems and their test tenants, browsers and devices, time zones.
   - Constraints (CON-n), assumptions (AS-n), dependencies (DEP-n).
3. **Functional requirements:** grouped by feature area (for example: data synchronisation, request submission, approval, calculation, notifications, reports). Each group starts with one sentence of purpose, then the table:

   | ID | Requirement | Pri | Source | Acceptance criteria |
   |---|---|---|---|---|

   Business rules are referenced (BR-n), not rewritten. Include status lifecycles as `stateDiagram-v2` where records move through statuses.
4. **Non-functional requirements (ISO/IEC 25010:2023):** only the characteristics that matter, each with a measurable target (checklist below).

   | ID | Characteristic | Requirement | Target / measure | Pri |
   |---|---|---|---|---|

5. **Interface requirements:** IF-n per external system: direction, data, trigger and frequency, volume, format, authentication method (never the credential), error handling, owner of the other side.
6. **Data requirements:** DR-n: record types and key attributes in business terms, unique keys, source of truth, retention, personal data, migration/initial load.
7. **Reports and outputs:** report | audience | content | filters | format | schedule.
8. **Verification approach:** how requirements are verified (UAT test cases, inspection of a report, measurement of run time), entry/exit criteria summary; detail in the UAT plan.
9. **Out of scope.**
10. **Open issues:** OI-n with why it matters / what for, owner, due date.
11. **Traceability matrix:** BO/StR → BR → FR/NFR → IF/DR → TC.
12. **Approval.**

## Non-functional checklist (ISO/IEC 25010:2023, CloudApper examples)

Go through each characteristic; write a requirement only where it matters, always with a number.

| Characteristic | Ask | Example requirement |
|---|---|---|
| **Functional suitability** (completeness, correctness, appropriateness) | Are calculations exact? Rounding? | "Tip shares shall be rounded to 2 decimals; the sum of shares equals the pool within 0.01." |
| **Performance efficiency** (time, resources, capacity) | Volumes, peak load, run time | "The nightly sync of up to 30,000 employees shall finish within 45 minutes." "Saving a request shall return to the user within 3 seconds." |
| **Compatibility** (co-existence, interoperability) | Which systems, versions, formats | "Exports shall use the payroll import CSV layout version 3." |
| **Interaction capability** (usability, accessibility, user error protection) | Devices, languages, training | "A first-time employee shall submit a request on a tablet without training in under 2 minutes." "Mandatory fields shall be validated before save." |
| **Reliability** (availability, fault tolerance, recoverability) | What if the external system is down? | "If UKG does not answer, the sync shall retry 3 times and log the failure with the record count." |
| **Security** (confidentiality, integrity, accountability, authenticity) | Who sees what; credentials; audit | "Only the Payroll Admin role shall view pay amounts." "All integration credentials shall be stored in the platform credentials store." "Every status change shall be recorded with user and time." |
| **Maintainability** (modularity, analysability, modifiability, testability) | Who changes rules after go-live | "Overtime thresholds shall be maintained by an admin in a setup screen, without design changes." "Every run shall write a log record with counts and errors." |
| **Flexibility** (adaptability, scalability, installability) | Growth, new sites, environment copies | "Adding a new location shall require only setup records." "The solution shall be deployable to Production from UAT with documented configuration." |
| **Safety** (operational constraint, risk identification, fail safe) | Can a failure harm people or pay? | "If the calculation fails, no payroll export shall be produced for that period." |

## CloudApper points every SRS should settle

- **Source of truth** per synced data item, and what the app may write back.
- **Time zone** of every date rule and schedule (platform schedules run in UTC).
- **Environments:** UAT and Production apps and the matching external test and production tenants; no cross-environment calls.
- **Validation location:** rules that must also apply to imports, integrations and the API (not only on screen).
- **Idempotency:** what happens when a sync or calculation runs twice for the same period.
- **Run logging:** what each scheduled or batch process records (start, end, counts, errors).
- **Roles:** a role per user class with the minimum rights.
- **Configuration owned by the customer:** which lists, thresholds and mappings the customer maintains.

## Quality checks

- Every FR has acceptance criteria and a source; every NFR has a number.
- Every FR traces to a BO/StR and to at least one TC.
- No design instructions ("use a FOREACH node"): requirements state behaviour; the design decides the building blocks.
- Interfaces name the system owner and the authentication method, never credentials.
- Open issues have owners and dates; Inferred requirements appear as open issues too.
