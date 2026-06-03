# Early-June 2026 — per-chapter change plan

Scope kept deliberately tight (mirrors the late-May wave: 2 timeline entries + targeted chapter integration + 1 glossary term). English-only; no translation propagation this wave.

## chapters/11-timeline.md
- Two new entries inserted after the May 21 MCP RC entry, before `## The Pattern`:
  - `### June 1, 2026 --- IETF Internet-Draft: Security Considerations for MCP Implementations`
  - `### June 2, 2026 --- Microsoft Build: MAI-Thinking-1 and MAI-Code-1-Flash (Harness-Native Training)`
- Six source lines appended to `## Sources` (IETF I-D, DEV.to, Microsoft AI, GitHub Changelog, TechTimes).

## chapters/07-mcp.md
- New section `## 2026-06-01: Security Considerations Move to the IETF` inserted after the `## 2026-05-21: The 2026-07-28 Release Candidate` section, before `## Market Context`.
- Frames the I-D as filling the operational-security gap the RC's authorization hardening left open; enumerates the six vulnerability classes with mitigations; positions independent standards-track scrutiny as a maturity marker.
- Source #16 added to the numbered Sources list.

## chapters/04-harness-engineering.md
- §4.5 extended with a bolded paragraph **"The symmetric move: training the model for the harness"** — MAI-Code-1-Flash as the inverse of harness synthesis (model shaped to a fixed harness vs. harness evolved for a fixed model). Cross-references §4.7 (harness-as-moat) for the lock-in trade-off and points to the new glossary term.
- One source line appended to `## Sources` (Microsoft AI + GitHub Changelog + TechTimes, bundled).

## glossary.md
- New **H**-section term **Harness-Native Training**, placed after **Harness Synthesis**. Defines it as the symmetric inverse of harness synthesis with the MAI-Code-1-Flash reference and the harness-as-moat trade-off.

## README.md
- "What's new" callout rolled forward from **May 2026** to **June 2026**: two new June bullets (most-recent-first), existing May bullets retained under a *"From the late-May wave"* divider pointing to CHANGELOG.

## CHANGELOG.md
- New `## June 2026` → `### 2026-06-03 — Early-June 2026 update` section at the top, with full caveat list.

## Not touched
- Ch08 (the vendor-decoupling angle is already carried by the existing April 27 entry + the new Ch11 entry; adding more would be redundant).
- Translations (English-first, consistent with the late-May wave).
