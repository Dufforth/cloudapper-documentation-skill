# UAT test documentation (ISO/IEC/IEEE 29119-3, tailored)

User acceptance testing proves that the solution meets the approved SRS. Three items: a **test plan**, **test cases** derived from acceptance criteria, and a **test completion summary**. Defects are tracked in the ticket system, not in these documents. Skeleton: `templates/uat-test-cases-template.md`.

## Test plan

0. Document control (link to the SRS version under test).
1. **Scope:** features and requirement IDs in scope; out of scope.
2. **Approach:** who tests (customer key users, PM, solution team), test types (functional, integration with the external test tenant, roles, reports, negative cases, volume where an NFR asks for it).
3. **Environment:** the UAT app, the external system's test tenant, test users per role, devices. Production is never used for testing.
4. **Test data:** where it comes from (synced from the test tenant, prepared records), anonymised; the worked examples from the BRD/SRS.
5. **Entry criteria:** build complete in UAT, configuration loaded, test users ready, integrations reachable.
6. **Exit criteria:** all Must test cases passed; no open critical or high defects; Should failures accepted in writing.
7. **Schedule and responsibilities.**
8. **Risks** to testing (test tenant data, availability of testers).

## Test cases

| TC | Requirement | Title | Preconditions | Steps | Expected result | Actual | Pass/Fail | Tester / date |
|---|---|---|---|---|---|---|---|---|

Rules:
- At least one test case per acceptance criterion; Must requirements get positive and negative cases.
- Steps use the exact screen, button and status names.
- Expected results are observable (status value, amount, email received, record in the external system).
- Include role tests (a user who must not see or do something) and integration tests (data reaches or arrives from the external system).
- Include time-based cases: schedules, cut-offs, time zone edges, rerun of the same period.

## Test completion summary

| Item | Content |
|---|---|
| Executed / passed / failed / blocked | Counts per priority |
| Open defects | Ticket links with severity |
| Accepted deviations | What, why, who accepted |
| Recommendation | Go / go with conditions / no go |
| Sign-off | Customer owner, PM, date |

Update the SRS traceability matrix with the TC results.
