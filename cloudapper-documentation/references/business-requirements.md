# Business Requirements Document (BRD)

ISO/IEC/IEEE 29148 business requirements (BRS) and stakeholder requirements (StRS), merged into one document because on a CloudApper project the same people own both. It answers **why** the solution exists and **what the business needs**, in business words, before any design. Readers: PM, customer owner, solution team. Skeleton: `templates/brd-template.md`. Process and writing rules: `requirements-engineering.md`.

## Structure

0. **Document control** (`document-control.md`).
1. **Executive summary:** the problem, the proposed solution in one paragraph, expected benefits, scope in one line.
2. **Business context:** organisation and department, business process concerned, why now (trigger: audit, growth, manual errors, system change).
3. **Business objectives:** BO-n, each measurable (from → to, by when). Example: "**BO-1** Reduce time to prepare tip payroll from 6 h to under 1 h per pay period by Q3."
4. **Stakeholders:** table of stakeholder | role | interest / concern | influence | involvement (approve, consult, inform). Include end users, supervisors, payroll/HR, IT, the integrated system's owner, support.
5. **Current process (as-is):** flowchart and pain points table (pain point | impact | frequency | evidence).
6. **Target process (to-be):** flowchart with the app in it, what changes for each user group, what stays manual.
7. **Business rules:** BR-n table (rule | source | owner | example). Rules are the customer's, written in their words, with a worked example.
8. **Stakeholder requirements:** StR-n table (need | stakeholder | priority | source | confidence). Needs, not features: "Supervisors need to see unapproved timecards before the payroll cut-off."
9. **Scope:** in scope, out of scope (with reason), future phases.
10. **Data and systems:** systems involved, which one is the source of truth for each data item, data volumes, data that must not leave a system.
11. **Constraints, assumptions, dependencies:** CON-n, AS-n, DEP-n (for example: "DEP-1 UKG test tenant available with API access").
12. **Success criteria and benefits:** how BO-n will be measured after go-live, who measures, when.
13. **Risks:** R-n (risk | likelihood | impact | mitigation | owner), shared with the PM guide.
14. **Open issues:** OI-n (question | why it matters / what for | owner | due date).
15. **Glossary.**
16. **Approval.**

## Quality checks

- Every BO is measurable and has at least one StR.
- Every BR has an owner and an example with numbers.
- No platform words (workflow, form, connector) in sections 3–9: business language only.
- Out-of-scope list exists and was confirmed.
- Source of truth stated for every data item that is synced.
