# Mid-July 2026 update: 10 timeline entries + June 2 extension + nine-chapter integration

Adds the mid-July 2026 wave (window 2026-06-03 → 2026-07-14) on top of the early-June wave. Ten new timeline entries, one entry extension, targeted integration across nine chapters, two glossary terms, README roll-forward, and a CHANGELOG entry. Scope kept surgical and on-thesis; English-only (no translation propagation this wave).

## Timeline entries (Ch11)

Ten new entries (chronological): **June 8** Apple opens Foundation Models to any LLM provider · **June 9** Claude Fable 5 + Mythos 5 (first public GA of a Mythos-class model) · **June 12** export-control suspension + staged restoration + jailbreak-severity framework · **June 17** AWS AgentCore harness GA · **June 18** MCP Enterprise-Managed Authorization · **June 18** Terminal-Bench Challenges · **June 26** OpenAI GPT-5.6 Sol/Terra/Luna · **June 29** DeepSeek V4 peak/off-peak pricing · **July 6** Tencent Hy3 · **July 6** Anthropic J-space. The June 2 Microsoft Build entry is extended with Agent Harness + Foundry Hosted Agents. `## The Pattern` gains a sixth thread — **government enters the distribution loop** — and `## Sources` gains the new primaries.

## Per-chapter integration

- **Ch04** — harness-as-hyperscaler-product (AWS AgentCore harness + Microsoft Agent Harness); the May 13 metered-credit announcement and its June 15 walk-back; Cowork web/mobile; refusal-as-`stop_reason` as a new harness contract; Terminal-Bench Challenges + UK AISI inference-compute reporting; J-space + METR CoT as a feature-level sensor class.
- **Ch07** — new Enterprise-Managed Authorization section; June 29 SDK betas + SEP-2322 Multi Round-Trip Requests; 97M-download stat date-qualified to Q1 2026.
- **Ch06** — new "Evaluation Grows Governance Axes" section (GateMem, MemSyco-Bench, Decision-Aware Memory Cards, "Are We Ready For An Agent-Native Memory System?", plus a flagged control-plane-placement note).
- **Ch03** — Still + TokenPilot KV-cache compaction.
- **Ch02** — Amazon Bedrock Managed Knowledge Base GA; contested Subquadratic SubQ 12M-token claim; Agents-K1.
- **Ch09** — DeepSeek V4 peak pricing; Huawei + China Mobile carrier-scale inference validation; GLM-5.2; Hy3.
- **Ch08** — Notion 3.6 External Agents; Tana → Tana Outliner brand-split correction; Heptabase v1.98.0 + Capacities AI Chat Connectors 2.0.
- **Ch12** — Apple `LanguageModel` protocol; Gemma 4 QAT.
- **Ch05** — untouched (no skills-axis addendum this wave).
- **Glossary** — **Safety-Tiered Distribution**, **Enterprise-Managed Authorization (EMA)**.
- **README** — "What's new" rolled forward to July 2026 (early-June demoted, late-May dropped); Ch07 ToC row date-qualified; stale *Last updated* footer corrected to July 2026.

## Sourcing & caveats

All sources are primary or first-tier secondary. Two figures were re-fetched at implementation time: Hy3's post-preview hallucination rate (**12.5% → 5.4%**, HF model card) and MemSyco-Bench's Qwen3-8B sycophancy pair (**27.4% → 44.7%**, arXiv HTML) — both confirmed, so the exact figures are printed rather than a qualitative fallback.

Caveats carried into the CHANGELOG: the Tana brand split is dated to month precision (March 2026; no day in source); Capacities AI Chat Connectors 2.0 is month precision (June 2026); the Hy3 hallucination figure is per Tencent's HF card; the DeepSeek V4 announcement is dated June 29-30 (TechNode: June 30); the AWS AgentCore harness GA whats-new post is June 17 with the New York Summit showcase June 18. The June 12 entry carries no time-of-day precision; the jailbreak-severity framework is Anthropic-authored (a consensus draft with Glasswing partners, not a published joint standard); the GPT-5.6 review is METR + Apollo only.

## Excluded from scope (neutral reasons)

Tree Ring Memory (issue #48 — launched July 7, ~5 stars, no external validation; does not yet clear the bar); Remio (issue #47 — cloud-BYOK personal index, not a local-model primitive); Qwen3.7-Plus (no authoritative primary source); Claude Cowork web/mobile (folded into Ch04 as one sentence); KV-cache marketplace proposal arXiv 2606.13361 (proposal-only, no operational case); Anthropic Agent-SDK metering pause (chapter-level, not timeline).

## Not touched

`translations/` (English-first, consistent with the last three waves) and `docs/archive/`. Full review checklist and change plan in `docs/mid-july-2026/`.
