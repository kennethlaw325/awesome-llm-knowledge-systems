# Mid-July 2026 — per-chapter change plan

Scope: ten new timeline entries + one entry extension, targeted integration across nine chapters, two glossary terms, README roll-forward, CHANGELOG entry. English-only; no translation propagation this wave. Surgical additions only — existing prose was not rewritten.

## chapters/11-timeline.md
- Twelve new entries inserted after the June 2 Microsoft Build entry, before `## The Pattern`, in chronological order (June 8 → July 6), including two skill-security entries (June 22 AIR incident, July 2 Cloak-and-Detonate).
- June 2 Microsoft Build entry extended by two sentences (Agent Harness + Foundry Hosted Agents), cross-referencing the new June 17 AWS entry.
- `## The Pattern` gains a sixth thread ("government enters the distribution loop") placed after the ARC-AGI-3 line and before the closing "trajectory is clear" paragraph — chronologically honest (June-July), so the existing "four/five threads" April framing is left intact.
- `## Sources` gains new primary source lines for every new entry.

## chapters/04-harness-engineering.md
- §4.2 (Böckeler taxonomy, Sensors quadrant): new paragraph introducing a feature-level sensor class — emotion vectors + CoT monitoring (April), METR's June GPT-5.6 CoT catch, and July's J-space as a CoT-independent sensor. (Ch04 had no prior interpretability section; §4.2 Sensors is the correct conceptual home.)
- §4.8 (stress-testing / compute allocation): UK AISI arXiv 2606.17930 (report capability vs inference-time compute) + Terminal-Bench Challenges multi-day endurance null result.
- §4.9 (cloud-native primitives): AWS AgentCore harness GA + Microsoft Agent Harness / Foundry Hosted Agents ("harness" as hyperscaler SKU); the May 13 metered-credit announcement and its June 15 walk-back; Cowork web/mobile July 7.
- §4.10 (managed-inference turn): refusal-as-`stop_reason` + fallback contract as a new harness contract in the task-budgets family.
- Sources: added Fable 5, AWS AgentCore harness, MS Agent Harness/Foundry, SDK-metering walk-back, Cowork, Terminal-Bench Challenges, METR, UK AISI, J-space.

## chapters/07-mcp.md
- New `## 2026-06-18: Enterprise-Managed Authorization` section between the IETF section and `## Market Context`.
- `## 2026-05-21: The 2026-07-28 Release Candidate` section extended with a "Beta SDKs and the finalization window (June 29)" paragraph: Python/TypeScript/Go/C# betas, four-week testing period, TypeScript v2 package split, SEP-2322 Multi Round-Trip Requests (framed as re-plumbing transport for sampling/elicitation, NOT superseding them). No beta version strings printed.
- STALE FIX (line ~21): "2026 (present). MCP SDK downloads exceed 97 million…" → "2026. MCP SDK downloads exceeded 97 million per month as of Q1 2026…".
- Sources: added #17 (EMA) and #18 (SDK betas / SEP-2322).

## chapters/06-agent-memory.md
- New `## Mid-2026: Evaluation Grows Governance Axes` section after "Feature-Level Memory Research (2026)": GateMem (arXiv 2606.18829), MemSyco-Bench (arXiv 2607.01071), Decision-Aware Memory Cards (arXiv 2606.08151), "Are We Ready For An Agent-Native Memory System?" (arXiv 2606.24775), plus a flagged single-author control-plane-placement note (arXiv 2606.15903).
- MANDATORY corrected figures used: MemSyco 18.67%→32.67% (DeepSeek-V4-Flash) and 27.4%→44.7% (Qwen3-8B); agent-native survey MemOS 8.9 EM on LoCoMo (not 11.5).
- Sources: added #17-#21.

## chapters/03-context-engineering.md
- §3.3 (KV-cache): new paragraph on Still (arXiv 2606.07878) and TokenPilot (arXiv 2606.17016), quantifying the append-only / don't-bust-the-cache principle the section states qualitatively.
- Sources: added Still and TokenPilot.

## chapters/02-knowledge-layer.md
- "RAG as Context Engine" section: new `### 2026: RAG Becomes a Managed Cloud Primitive` (Amazon Bedrock Managed Knowledge Base GA, June 17). No LazyAttention/DeepMind material.
- Long-context section: new `### 2026 Caution: A Contested 12M-Token Claim` (Subquadratic's SubQ; "Subquadratic Selective Attention (SSA)"; MIT Tech Review June 19 scrutiny; Will Depue pushback; Qwen-weight reuse). Framed as contested.
- KG section: one sentence on Agents-K1 (arXiv 2606.13669) appended to the "KG as Semantic Backbone" subsection.
- Sources: added Bedrock Managed KB, MIT Tech Review SubQ, Agents-K1.

## chapters/09-china-ecosystem.md
- DeepSeek V4 subsection: appended paragraph on the June 29-30 official-release announcement + peak/off-peak API pricing.
- New `### Sovereign Silicon at Carrier Scale (Huawei + China Mobile, June 2026)` subsection: MWC Shanghai live-network validation with the mandatory "simulated 8K-190K-token workloads" framing; TTFT −51-93% for GLM-5.1, throughput +372% at 128K.
- GLM subsection: appended GLM-5.2 (June 13) — IndexShare, MTP acceptance length "up to 20%", HF-card benchmarks only.
- New `### Hunyuan 3.0 / Hy3 (Tencent, July 2026)` subsection.
- The April 2026 mHC "awaiting replication" flag left unchanged (no verified resolution).
- Sources: added DeepSeek V4 pricing, GLM-5.2, Hy3, Huawei carrier validation.

## chapters/08-tools-landscape.md
- Notion section: appended a Notion 3.6 paragraph (External Agents = Claude + Cursor; distinct from the 3.5 Developer Platform Codex/Decagon API partners; Notion Workers; five MCP connectors; verbatim "usage has 10×'d in the past month").
- Emerging Platforms: Heptabase v1.98.0 (June 2) and Capacities AI Chat Connectors 2.0 (June 2026, month precision) one-liners; Tana bullet corrected to **Tana Outliner** (outliner.tana.inc) with the March 2026 brand-split note (month precision, no day).
- Obsidian Feb-2026 user stat left as-is (explicitly dated).
- Sources: #8-#10 updated (Heptabase changelog, Capacities release 66, Tana Outliner + brand reassignment); #15 added (Notion 3.6 + 3.5 releases).

## chapters/12-local-models.md
- New `## 2026: Local Models Get an OS-Native API and Vendor QAT` section: Apple Foundation Models `LanguageModel` protocol (Ch12 angle: local MLX/HF models first-class in an OS-native API) and Gemma 4 QAT (mandatory VRAM framing — "third-party analysis estimates ~72% VRAM reduction vs BF16; Google's own figure is only that E2B drops under 1GB via a mobile format").
- Sources: added Apple WWDC26 sessions and Gemma 4 QAT (+ third-party VRAM analysis).

## chapters/05-skill-systems.md
- New `## 5.10 Skill Security and the Supply-Chain Problem` (the chapter's first security coverage): the scanning ecosystem (Cisco skill-scanner, NVIDIA SkillSpector open-sourced mid-June, skills.sh audit); the June 22 AIR incident (TOCTOU / external-URL bypass, 26,000 agents); Cloak-and-Detonate (arXiv 2607.02357, evasion + SkillDetonate 97%@2%FP); framework tie-in to the Ch07 IETF security draft (publish-time scanning → runtime containment).
- §5.2: Vercel skills.sh API GA (June 5) — queryable registry API, OIDC-token auth, 600 req/min per team and per project, 600,000+ indexed skills, per-skill security audit.
- §5.5: Compositional Skill Routing (arXiv 2606.18051, single author Xueping Gao, Alibaba Cloud) — CompSkillBench; Iterative Skill-Aware Decomposition 51.0%→67.7%.
- §5.8: Workflow-to-Skill (arXiv 2606.06893, Wuhan / Nanchang University) — RWSA; +10.5% relative behavioral-replay consistency.
- Sources: added skills.sh, Compositional Skill Routing, Workflow-to-Skill, AIR incident, Cloak-and-Detonate, NVIDIA SkillSpector.
- Integrated from `wave-skills-addendum.md`, which arrived after the initial pass (Ch05 was briefly UNTOUCHED).

## Not touched
- `translations/` — English-first, consistent with the last three waves.
- `docs/archive/` — untouched; this wave's planning docs live in `docs/mid-july-2026/`.

## Editorial exclusions (neutral reasons)
- **Tree Ring Memory** (GitHub issue #48) — real project, launched July 7 with ~5 stars and no external validation; does not yet clear the inclusion bar. Revisit if it gains ecosystem traction.
- **Remio** (GitHub issue #47) — real product, but a cloud-BYOK personal index rather than a local-model primitive; does not clear the bar for Ch08/Ch12 at this time.
- **Qwen3.7-Plus** — no authoritative primary source (official Qwen channels do not list it); excluded on sourcing.
- **Claude Cowork web/mobile** — folded into Ch04 §4.9 as one sentence; not a standalone timeline entry.
- **KV-cache marketplace proposal** (arXiv 2606.13361) — proposal-only, no operational case yet.
- **Anthropic Agent-SDK metering pause** — integrated at chapter level (Ch04 §4.9), not as a timeline entry.
- **agentskills.io adoption-count updates + Microsoft .NET Agent Skills** (June 29) — vendor-adoption counts, no new primitive.
- **NVIDIA SkillSpector standalone entry** — folded into the June 22 AIR incident entry.
- **OKX AI agent marketplace** — off-axis for this guide.
