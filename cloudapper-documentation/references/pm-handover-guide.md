# PM handover guide

Written for the project or account manager taking over a customer solution: non-technical, plain words. It sits next to the technical guide and links to it.

Skeleton: `templates/pm-guide-template.md`.

Standard line: "Structure based on ISO 21502:2020 project management guidance, tailored for CloudApper solutions." The 21502 subjects map to the sections: business case and benefits (§1, §3), stakeholders (§9), scope (§5), risks and issues (§10), communication (§11), handover (§12).

## Header

The document control block (`document-control.md`, type PMG), then audience, solution and tenant, as-of date, sources (ticket system read-only, the app, public information), link to the technical guide, and the **[confirm]** marker for anything not verified.

## Structure

1. **At a glance:** one-sentence summary; table of customer, systems, platform, users, environments, scope, start date, phase, open tickets, volumes, health (green / amber / red).
2. **The customer:** public facts with sources and why they matter **[confirm]**.
3. **Problem and value:** the manual process vs what the app does (table), value messages, what the app does NOT do.
4. **How it works in plain words:** big-picture flowchart, the life of one record with statuses in plain words, record types, a worked example.
5. **Features and components:** features with status (working / off / no effect), components in plain words, menus per audience, environments.
6. **Domain basics** (for example UKG, payroll, scheduling, HR): concept | meaning | why it matters.
7. **CloudApper basics:** tenant, app, form, workflow, connector, audit log, App Studio (use the glossary in `reading-a-cloudapper-app.md` §13).
8. **Glossary** of customer and solution terms.
9. **People and roles:** role | side | responsibilities | name **[confirm]**; "who to go to for what".
10. **Current state, risks, open items:** ticket buckets and themes, risk register R-xx (impact | severity | action | link to technical finding F-xx), suggested order (now / next / then).
11. **Customer communication:** key messages, what not to share (credentials, internal findings wording, other customers), issue-handling flowchart, what to ask for every time, message templates (acknowledge, data-caused issue, rule rejection, close approved items, weekly status), meeting cadence.
12. **Questions for the first weeks:** with our team, with the customer.
13. **Sources.**

Templates in section 11 are for the PM to adapt. The guide itself is internal and is not sent to the customer.
