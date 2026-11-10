# Document control (ISO/IEC/IEEE 15289, tailored)

Every deliverable starts with the same control block, so readers know what they hold, how current it is and who approved it.

## Control block

| Field | Content |
|---|---|
| Document ID | `<CUST>-<APP>-<TYPE>-<NNN>`, types: BRD, SRS, UAT, TG (technical guide), PMG (PM guide), AR (analysis report) |
| Title | `<App or project>: <document type>` |
| Version / status | `0.1 Draft` → `0.9 For review` → `1.0 Approved` → `1.1 …` |
| Author | Name and role |
| Customer / project | Name |
| Environment | Production / UAT (for as-built documents) |
| Classification | Internal (default) or Customer-shareable |
| Basis | Sources: sessions with dates, tickets, the app (read-only, date) |
| Standard | "Structure based on <standard>, tailored for CloudApper solutions" |

Then:

**Revision history**

| Version | Date | Author | Change |
|---|---|---|---|

**Review and approval** (BRD, SRS and UAT plan need approval; guides need review only)

| Role | Name | Decision | Date |
|---|---|---|---|

## Versioning rules

- Minor version (0.1 → 0.2, 1.0 → 1.1) for each reviewed change; major version (→ 2.0) for a new release scope.
- An approved BRD or SRS changes only through a change request: new version, revision row, changed requirements marked *(changed in vX.Y)*, and a fresh approval.
- Never reuse a requirement, finding or test ID. Deleted requirements stay in the table with status **Withdrawn**.

## IDs used across documents

| Prefix | Meaning | Defined in |
|---|---|---|
| BO-n | Business objective | BRD |
| BR-n | Business rule | BRD |
| StR-n | Stakeholder requirement | BRD |
| FR-nn | Functional requirement | SRS |
| NFR-nn | Non-functional (quality) requirement | SRS |
| IF-nn | Interface requirement | SRS |
| DR-nn | Data requirement | SRS |
| CON-n, AS-n, DEP-n | Constraint, assumption, dependency | BRD / SRS |
| OI-n | Open issue | any |
| TC-nn | Test case | UAT |
| F-nn | Finding | Technical guide, analysis report |
| R-nn | Risk | PM guide |

## Storage

Keep documents with the project, in Markdown, versioned. Generate PDF only when requested; the PDF carries the same version as the Markdown it was built from.
