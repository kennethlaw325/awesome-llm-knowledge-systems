# Early-June 2026 — proposed timeline additions

Two Tier 1 timeline entries, both genuinely post-May-21 (the prior wave's last entry). Both pass the `CONTRIBUTING.md` inclusion test ("introduces, validates, or operationalizes a primitive, pattern, or narrative beat the framework tracks").

---

## Entry 1 — June 1, 2026: IETF Internet-Draft, Security Considerations for MCP Implementations

**Why it's Tier 1:** continues the MCP standardization/security arc directly off the May 21 RC. The RC hardened *authorization*; this is the first standards-track document to address the *operational* attack surface the spec leaves undefined. Independent (non-vendor) scrutiny is itself the maturity signal.

**Inclusion test:** operationalizes a pattern (MCP security) the framework tracks (Ch07).

**Core facts (verified):**
- `draft-mohiuddin-mcp-security-considerations-00`, author **Anas Mohiuddin Syed** (Chicago, IL).
- Abstract: *"The MCP specification does not define normative security requirements."*
- Six vulnerability classes: SSRF, excessive tool permissions, prompt-injection surface exposure, MCP lifecycle bypass, information leakage, authentication-enforcement gaps.
- Mitigations: validate resolved IPs at connection time (block RFC 1918 / loopback / link-local), OS-level egress restrictions, disable HTTP redirects by default, minimal filesystem scoping, complete handshake before tool calls, structured logging of tool invocations.
- Names open-source tool **mcp-safeguard** (CI scanner, `scan --target ./my-mcp-server/`).

**Source:** [IETF datatracker](https://datatracker.ietf.org/doc/draft-mohiuddin-mcp-security-considerations/) (primary, WebFetch-verified). Companion: author's [DEV.to write-up](https://dev.to/syedanas01/i-built-the-first-security-scanner-for-mcp-servers-heres-what-i-found-2np2).

**Caveats:**
- Month is firm (June 2026; I-D expires December 3, 2026). The **day (June 1)** is derived from the 185-day I-D expiry convention, not stated explicitly — soften to "June 2026" if you prefer.
- The `mcp-safeguard` **GitHub repo** referenced in secondary coverage (`SyedAnas01/mcp-safeguard`) returned **404** via the GitHub API at draft time. We cite only the IETF I-D (which names the tool) + the DEV.to post, and flag the repo as unresolved. **No GitHub URL was asserted.**

---

## Entry 2 — June 2, 2026: Microsoft Build — MAI-Thinking-1 + MAI-Code-1-Flash (Harness-Native Training)

**Why it's Tier 1:** two beats in one. (1) Carries the April 27 Microsoft–OpenAI restructure from *contract* to *capability* — Microsoft now ships in-house frontier-adjacent models. (2) MAI-Code-1-Flash was **trained directly against production GitHub Copilot harnesses** — a new primitive (harness-native training) that is the symmetric inverse of harness synthesis (AHE/AgentFlow). On-thesis for the harness-engineering spine.

**Inclusion test:** introduces a primitive (harness-native training) the framework tracks (Ch04); validates a narrative beat (vendor decoupling) already in Ch11.

**Core facts (verified, multi-source):**
- **MAI-Thinking-1** — Microsoft's first in-house reasoning model, reported trained without OpenAI data.
- **MAI-Code-1-Flash** — 5B-parameter coding model; trained directly with the GitHub Copilot harnesses used in production; ~60% fewer tokens than comparable models on hard tasks; beats Claude Haiku 4.5 on price-to-performance; shipped same-day into Copilot model picker across all plans.
- Event: Microsoft Build, San Francisco, June 2, 2026.

**Sources:** [Microsoft AI — Introducing MAI-Code-1-Flash](https://microsoft.ai/news/introducingmai-code-1-flash/) (primary); [GitHub Changelog, 2026-06-02](https://github.blog/changelog/2026-06-02-mai-code-1-flash-is-now-available-for-github-copilot/) (primary, dated); [TechTimes](https://www.techtimes.com/articles/317631/20260602/microsoft-build-2026-mai-thinking-1-first-house-reasoning-model-trained-without-openai-data.htm) (secondary, MAI-Thinking-1 + decoupling).

**Caveats:**
- `microsoft.ai` and the CNBC coverage **403 to automated crawlers** (same pattern the repo already documents for OpenAI URLs). The **GitHub Changelog** is the load-bearing dated primary.
- Benchmark/efficiency figures (5B, ~60% fewer tokens, Haiku-4.5 comparison) are **Microsoft-reported** — framed as such in the prose.

---

## Considered and dropped

- **Google Cloud Next 2026** (Vertex AI → Gemini Enterprise Agent Platform, A2A v1.2) — dated **April 22, 2026**, out of window for an early-June wave. Not new.
- **Anthropic confidential IPO filing (June 1, 2026)** — business/finance beat; carries less knowledge-systems signal than the two selected. Skipped to keep the wave tight.
- **"Memory for Autonomous LLM Agents" survey (arXiv 2603.07670)** — March 2026, out of window; candidate for a future Ch06 reference enrichment, not a June timeline entry.
