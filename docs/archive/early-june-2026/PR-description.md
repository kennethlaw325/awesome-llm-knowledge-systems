## Early-June 2026 update: 2 timeline entries + Ch07/Ch04 expansion + glossary

Adds the first two June 2026 timeline entries on top of the late-May wave, with targeted chapter integration. Scope kept tight and on-thesis; English-only (no translation propagation this wave).

### Timeline entries (Ch11)

- **June 1, 2026 — IETF Internet-Draft: Security Considerations for MCP Implementations** (`draft-mohiuddin-mcp-security-considerations-00`). The first standards-track document scoped to MCP security, opening on *"The MCP specification does not define normative security requirements."* Catalogs six vulnerability classes (SSRF, excessive tool permissions, prompt-injection surface, lifecycle bypass, information leakage, auth-enforcement gaps) with concrete mitigations and the open-source `mcp-safeguard` CI scanner. Continues the post-RC MCP arc: the May 21 RC hardened *authorization*; this addresses the *operational* surface the spec leaves to implementers.
- **June 2, 2026 — Microsoft Build: MAI-Thinking-1 + MAI-Code-1-Flash (harness-native training).** Microsoft ships its first in-house reasoning model (reported trained without OpenAI data) plus a 5B coding model **trained directly against the production GitHub Copilot harnesses**. Carries the April 27 Microsoft–OpenAI restructure from contract to capability, and introduces *harness-native training* as the symmetric inverse of harness synthesis.

### Per-chapter integration

- **Ch07** — new section *"2026-06-01: Security Considerations Move to the IETF"* after the RC section; six vulnerability classes + mitigations; independent standards-track scrutiny as a maturity marker.
- **Ch04 §4.5** — *"The symmetric move: training the model for the harness"*: harness synthesis (AHE/AgentFlow) evolves the harness for a fixed model; MAI-Code inverts it, shaping the model to a fixed harness. Flags the harness-as-moat lock-in (§4.7).
- **Glossary** — adds **Harness-Native Training**.
- **README** — "What's new" callout rolled forward to June 2026.

### Sourcing & caveats

All sources are primary or first-tier secondary.

- IETF I-D month is firm (June 2026; expires Dec 3 2026); **day (June 1)** is derived from the 185-day expiry convention — soften to "June 2026" if preferred.
- The `mcp-safeguard` **GitHub repo** named in secondary coverage returned **404** via the GitHub API at draft time; we cite only the IETF I-D (which names the tool) + the author's DEV.to post and flag the repo as unresolved. No GitHub URL asserted for it.
- Microsoft `microsoft.ai` / CNBC URLs may **403 to crawlers** (documented repo pattern); **GitHub Changelog (2026-06-02)** is the load-bearing dated primary for MAI-Code-1-Flash. Benchmark/efficiency figures are Microsoft-reported and framed as such.

### Dropped from scope

Google Cloud Next 2026 (dated April 22 — out of window); Anthropic IPO filing (finance beat, low knowledge-systems signal); the March agent-memory survey (out of window).

Full review checklist and change plan in `docs/early-june-2026-update/`.
