# Changelog

All notable changes to this guide are documented here. Dates are in HKT.

The guide is a living document — chapter and timeline updates ship continuously. This file gives returning readers a chronological view of what has shifted since their last visit, organized by month.

---

## August 2026

### 2026-08-03 — Memory foundation models (Metis) + timeline entries

- **PR (early-August wave)** — A memory foundation model claim gets its first coverage: MemTensor's **Metis** ("Metis: Training Large Language Models as Memory Foundation Models," arXiv 2607.26760, submitted July 29, 2026), from the same MemTensor lab (with Renmin University / NUS / SJTU / Tongji co-authors) behind the mid-July agent-native-memory survey (arXiv 2606.24775) already covered in **Ch06**. New Ch06 section "Late-July 2026: A Parametric Native-Memory Claim" (three paragraphs) presents memory foundation models as a research-preview direction — persistent, dynamically-evolving memory living as parametric state inside a frozen transformer backbone (Metis prototypes at 4B/9B/27B on Qwen3.5, training only a Fast-Weight-Programming-inspired hyper memory block and local memory block, updated at inference through a gradient-free EMA-style pass) — explicitly carrying the paper's self-reported limitations (long-horizon information loss under fixed-size compression; "information confusion... from the blending of semantics within the latent space") and framed against the chapter's existing governance benchmarks as a fourth candidate entering an already-contested field, not a resolution to it. New **Ch11** timeline entry (July 29) plus appended source. One glossary addition: **Memory Foundation Model**.
- Two further July 29, 2026 timeline entries, both fact-checked against their primary sources: **LangChain Deep Agents v0.7** (default base system prompt removed, built-in tool descriptions trimmed 43%, `TodoListMiddleware` / `write_todos` made opt-in after evals across three model families found no measurable gain from the default planning scaffold; ~6K → ~2K, 65%, base input tokens on a default agent turn) integrated into **Ch04 §4.8** as a production instance of the chapter's stress-testing discipline, plus a Ch11 entry and source; and **MinIO AIStor Memory** (object-storage-backed layer for agent memory, workspace state, and credentials, positioned to replace a hand-assembled vector-store / metadata-DB / credential-tooling stack with a durable, customer-owned, full-fidelity record), Ch11 entry only, corroborated by 8+ independent outlets dated July 29-30, 2026.
- README What's-new block rolled forward to August 2026 (three new-wave bullets; the late-July wave's full bullet list demoted to the trailing "from the late-July wave" section; the early-June trailing bullets dropped) and the *Last updated* footer corrected to August 2026. **Caveats:** Metis is a single-version arXiv preprint (no third-party replication or peer review yet) and is framed throughout as emerging/contested, consistent with the paper's own reported failure modes; the MinIO claim that AIStor Memory replaces a "secrets manager" is a paraphrase of its Vault/MinKMS credentials component, not a literal quote from MinIO, and is written as "credential tooling" rather than attributed to MinIO's own wording; no HN/X/social pickup is claimed for Metis. No new diagrams-worthy primitive shipped this wave, so `diagrams/` pending-refresh status is unchanged.

---

## July 2026

### 2026-07-30 — Graph Engineering chapter + late-July wave

- **PR (graph-engineering wave)** — New **Chapter 14: Graph Engineering**, covering the July 2026 frame: the Steinberger catalyst post (July 17-18, 2026; cited only via secondary sources, with conflicting view counts reported as conflicting), the essay wave (Thakker's org-graph / work-graph split, Perez's loops-supervising-loops and anchors, TrueFoundry and Eigent's governed topologies), the pushback given structural weight (LangChain's "3 Years of Graph Engineering with LangGraph" carried as simultaneously the strongest adoption signal and the strongest skeptical source; Tony Bai's buzzword warning), a knowledge-graph disambiguation table cross-referenced with Ch02, the fifth-generation-vs-refactor question left explicitly unresolved, the Chinese-ecosystem echo (图工程), and a concrete September 2026 survival gate. Six new **Ch11** timeline entries (**July 17** Kimi K3, the 2.8T-parameter open-weight flagship; **July 17** WAIC 2026 and the founding of WAICO; **July 17-18** the week "graph engineering" got its name; **July 18** Fable 5 subscription-access resolution; **July 24** Claude Opus 5; **July 28** the MCP 2026-07-28 specification ships final) with appended Sources. Per-chapter integrations: **Ch07** (new "2026-07-28: The Specification Ships Final" section: stateless core, Multi Round-Trip Requests, RFC 9207 issuer validation, Client ID Metadata Documents replacing Dynamic Client Registration, formal extensions framework, 12-month deprecation window), **Ch04** (minimal Opus 5 note in §4.10: pricing, five-level effort, Fast mode, cache-safe mid-conversation tool changes; benchmark figures marked as vendor claims), **Ch09** (Kimi K3 subsection; WAIC/WAICO under the regulatory section), **Ch02** (a one-line knows-vs-wired disambiguation pointer to Ch14 at the GraphRAG section head, plus a "2026 Update: Graph Tooling Consolidates" sub-section: LightRAG overtakes microsoft/graphrag as most-starred at ~38k stars, graph-based agent memory splits off as a category, GraphRAG-Bench at ICLR 2026, OpenSPG/KAG dormant since January 2026, GitHub figures API-verified; LightRAG added to the Key Projects table), and **Ch01** (a graph-engineering sub-part in the emerging-generation section plus two primary sources). Four glossary additions (**Graph Engineering**, **Org Graph / Work Graph**, **Anchor (Graph Engineering)**, **Client ID Metadata Documents (CIMD)**) and a one-line finalization update to **Stateless MCP**. README updates (What's-new rolled forward with six late-July bullets, TL;DR graph-engineering clause, a Which-Path row for multi-agent wiring, Evolution ASCII fifth column, ToC row 14); a Next link plus a one-sentence Ch14 pointer in **Ch13**; **CITATION.cff** chapter count to fourteen. **Caveats:** the term is roughly two weeks old and contested from day one — the chapter is framed as *emerging*, with the skeptics given equal weight and no verdict rendered; the catalyst post was not directly fetched and is cited only through secondary sources, which do not carry it identically (two quote the English wording verbatim, two link it without quoting, two render it in Chinese translation, one paraphrases); every source that dates it dates it July 18, so the "July 17-18" range is a US-time hedge rather than a source disagreement, and its view counts conflict as snapshots taken at different moments (575K within hours per explainx, 2.6M within two days per 36kr); two CSDN pieces and one Traditional-Chinese explainer are cited as titles-in-search-results only, not fetched; several circulated claims were excluded as unverified and are recorded in `docs/ch14-graph-engineering/exclusions.md`; diagrams are pending refresh; translations remain stale by policy.

### 2026-07-14 — Loop Engineering chapter

- **PR (loop-engineering wave)** — New **Chapter 13: Loop Engineering**, covering the June 2026 frame: Peter Steinberger's catalyst post (June 7), Addy Osmani's naming essay and "Own the Outer Loop" follow-up, Boris Cherny's "my job is to write loops," the Rajasekaran generator/evaluator split (Anthropic, March 2026), Stripe's minions (~1,300 PRs/week), LangChain's four stacked rungs, the Claude Code `/loop` vs `/goal` primitives, and adoption signals (@ClaudeDevs, 鱼皮, Snorkel's Continual Learning Bench). Plus: a new **"An Emerging Fourth Generation? Loop Engineering"** section in **Ch01** with three primary sources; two new **Ch11** timeline entries (**June 7** the naming week; **June 16** loop stacking goes institutional and bilingual) with appended Sources; three glossary terms (**Loop Engineering**, **Generator-Evaluator Split**, **Outer Loop**); README updates (Evolution ASCII fourth column, TL;DR bullet, ToC row 13, a Which-Path persona line, and What's-new bullets); a Next link in the **Ch12** footer; and a minimal **CITATION.cff** edit noting the emerging fourth generation. **Caveats:** the term is roughly five weeks old and contested — the chapter is framed as *emerging*, not a settled fourth generation. Several widely-circulated claims were excluded after primary-source verification: a viral "prompt engineering to loop engineering" post falsely attributed to a prominent AI researcher (the cited post does not exist), an unsourced reception-split statistic, unverifiable productivity figures and a fabricated graduated-autonomy scale attributed to Boris Cherny, an unfounded vendor "loop engineering course" claim, and fabricated per-model benchmark numbers on Snorkel's Continual Learning Bench (only the qualitative Fable-backbone finding is kept). Stripe's minions are dated March 2026 (the podcast episode day is disputed across sources, so month precision only); Steinberger's post metrics are quoted as live mid-July impressions (8.4M+); the Cherny "write loops" line is a spoken quote transcribed inconsistently across outlets.

### 2026-07-14 — Mid-July 2026 update

- **PR (mid-July wave)** — Twelve new June-July 2026 timeline entries (**June 8** Apple opens Foundation Models to any LLM provider; **June 9** Claude Fable 5 + Mythos 5, the first public GA of a Mythos-class model; **June 12** export-control suspension + staged restoration + jailbreak-severity framework; **June 17** AWS AgentCore harness GA; **June 18** MCP Enterprise-Managed Authorization; **June 18** Terminal-Bench Challenges; **June 22** AIR skill-supply-chain hijack (26,000 agents); **June 26** OpenAI GPT-5.6 Sol/Terra/Luna; **June 29** DeepSeek V4 peak/off-peak pricing; **July 2** Cloak-and-Detonate (HKUST scanner-evasion + runtime detection); **July 6** Tencent Hy3; **July 6** Anthropic J-space), plus a two-sentence extension of the June 2 Microsoft Build entry (Agent Harness + Foundry Hosted Agents). Ch11 also gains a sixth *"government enters the distribution loop"* thread in `## The Pattern` and new primary sources. Per-chapter integrations: **Ch04** (AWS / Microsoft harness-as-product + metered-credit walk-back + Cowork web/mobile; refusal-as-`stop_reason` primitive; Terminal-Bench Challenges + UK AISI inference-compute reporting; J-space and METR CoT as a feature-level sensor class), **Ch05** (new "Skill Security and the Supply-Chain Problem" section — AIR incident + Cloak-and-Detonate; skills.sh API GA; Compositional Skill Routing; Workflow-to-Skill), **Ch07** (new Enterprise-Managed Authorization section; June 29 SDK betas + SEP-2322 Multi Round-Trip Requests; 97M-download stat date-qualified to Q1 2026), **Ch06** (new "Evaluation Grows Governance Axes" section: GateMem, MemSyco-Bench, Decision-Aware Memory Cards, "Are We Ready For An Agent-Native Memory System?"), **Ch03** (Still + TokenPilot KV-cache compaction), **Ch02** (Amazon Bedrock Managed Knowledge Base GA; contested Subquadratic SubQ 12M-token claim; Agents-K1), **Ch09** (DeepSeek V4 peak pricing; Huawei + China Mobile carrier-scale inference validation; GLM-5.2; Hy3 open-sourcing), **Ch08** (Notion 3.6 External Agents; Tana → Tana Outliner brand-split correction; Heptabase v1.98.0 + Capacities AI Chat Connectors 2.0), **Ch12** (Apple `LanguageModel` protocol; Gemma 4 QAT). Three glossary additions: **Safety-Tiered Distribution**, **Enterprise-Managed Authorization (EMA)**, and **Skill Supply-Chain Attack**. README "What's new" rolled forward to July 2026 (early-June entries demoted, late-May list dropped) and the stale *Last updated* footer corrected to July 2026; Ch07 ToC row date-qualified. **Caveats:** the Tana brand split is dated to month precision (March 2026; the source gives no day); Capacities AI Chat Connectors 2.0 is dated to month precision (June 2026; no day published); the Hy3 post-preview hallucination figure (5.4%) is per Tencent's Hugging Face model card; the DeepSeek V4 official-release / peak-pricing announcement is dated June 29-30 (TechNode dates it June 30); the AWS AgentCore harness GA whats-new post is dated June 17 with the AWS New York Summit showcase June 18; the AIR incident is dated to AIR's June 22 disclosure (The Hacker News coverage June 23); Cloak-and-Detonate is dated to its arXiv submission July 2 (The Hacker News coverage July 6); SkillSpector naming follows NVIDIA's own repo (the incident reports don't name it), open-sourced mid-June 2026.

---

## June 2026

### 2026-06-03 — Early-June 2026 update

- **PR (early-June wave)** — Two new June 2026 timeline entries: **June 1 IETF MCP security Internet-Draft** (`draft-mohiuddin-mcp-security-considerations-00` by Anas Mohiuddin Syed — first standards-track document scoped to MCP security; six vulnerability classes with mitigations plus the open-source `mcp-safeguard` scanner) and **June 2 Microsoft Build: MAI-Thinking-1 + MAI-Code-1-Flash** (first in-house Microsoft reasoning model trained without OpenAI data; 5B coding model trained directly against production GitHub Copilot harnesses). Per-chapter integrations: Ch07 (new "2026-06-01: Security Considerations Move to the IETF" section closing the post-RC authorization-vs-operational-security gap), Ch04 §4.5 ("the symmetric move: training the model for the harness" — harness-native training as the inverse of harness synthesis). Glossary addition: **Harness-Native Training**. README "What's new" callout rolled forward to June 2026. **Caveats:** the IETF draft is firmly dated to month (June 2026; I-D expires December 3, 2026) — the day (June 1) is derived from the 185-day I-D expiry rule; the `mcp-safeguard` GitHub repository named in secondary coverage was not resolvable via the GitHub API at draft time (the IETF I-D itself, which names the tool, is the primary source); Microsoft's `microsoft.ai` and CNBC URLs may 403 to automated crawlers, so GitHub Changelog (June 2, 2026) is the load-bearing dated primary for MAI-Code-1-Flash.

---

## May 2026

### 2026-05-24 — Late-May 2026 update

- **PR #42** — Two new May 2026 timeline entries: **May 19 Code with Claude London** (self-hosted sandboxes public beta + MCP tunnels research preview, splitting the Managed Agents substrate along the perimeter line) and **May 21 MCP 2026-07-28 Release Candidate locked** (stateless protocol core, MCP Apps as first non-tool-call MCP deliverable, Tasks moved to extension status, plus Extensions framework / OAuth 2.0 hardening / formal deprecation policy). Per-chapter integrations: Ch04 §4.9 (perimeter-split substrate as the next move after the cloud-native triangle), Ch07 (new "The 2026-07-28 Release Candidate" section closing the stateless-core / stateful-extensions arc). Glossary additions: MCP Apps, MCP Tunnel, Self-Hosted Sandbox, Stateless MCP. **Editorial note:** Entry 2 (May 21 MCP RC) softened from a 5-primitive enumeration in the timeline body to a 3-headline framing (stateless core / MCP Apps / Tasks-as-extension), with the remaining structural changes folded into a single closing list-form sentence; per-primitive depth lives in the Ch07 expansion instead.

### 2026-05-06 — Translation sync + 2026 attribution audit

- **PR #16** — Sync 5 translation READMEs (繁體中文 / 简体中文 / 日本語 / 한국어 / Español) to current English content. Adds Use Cases section, The Lifecycle section, and Chapter 12 row to each translation's Table of Contents. English README's TL;DR Harness Engineering bullet aligned with the verified Böckeler / OpenAI Codex attribution.
- **PR #15** — Full attribution audit pass on Ch01 / Ch02 / Ch03 / Ch06 / Ch09 / Ch12 (the chapters not covered by the May 2026 audit). Two factual corrections: Ch03 §3.5 cited two academic surveys that conflate or fabricate (real survey is Mei et al. arXiv 2507.13334); Ch06 MIRIX claim was "four-layer architecture" with the wrong title (actual paper has six memory types and is titled "Multi-Agent Memory System"). Plus URL specificity hardening across Karpathy's LLM Wiki Gist, ACE paper attribution (arXiv 2510.04618), and the same Fowler/swyx/Codex pattern fixes that landed in Ch04/05.

### 2026-05-06 — Late-April follow-up + fact-check pass

- **PR #14** — Two timeline entries the overnight prep agent missed: **April 23 Memory for Claude Managed Agents** (filesystem-mounted memory, audit logs, public beta) and **April 28 AWS Bedrock Managed Agents powered by OpenAI** (limited preview; first time the OpenAI agent harness is named and sold as a product surface). Plus synthesis-lane references: Karpathy's Sequoia Ascent 2026 talk (vibe coding floor / agentic engineering ceiling) and the Externalization in LLM Agents survey (arXiv 2604.08224, 19-author Weights → Context → Harness convergence with this guide's framing). Updates `## The Pattern` cloud-native-primitives bullet to reflect the substrate / triggering / memory unbundling.
- **Fact-check pass** (in PR #14) — WebFetch verification of all critical URLs surfaced three claims to soften: $0.08 pricing measure word ("session-hour" → "agent runtime hour" with explicit SiliconANGLE secondary attribution), Anthropic Managed Agents primitive count ("four primitives" → "three virtualized components" matching the engineering blog), and the Microsoft-OpenAI restructure AGI clause framing (primary Microsoft blog uses "non-exclusive licensing"; the explicit "AGI clause removed" framing comes from CNBC and PitchBook secondary).

### 2026-05-06 — May 2026 update

- **PR #13** — Five new timeline entries (April 7 Mythos breach addendum, April 8 Anthropic Managed Agents, April 27 Microsoft–OpenAI restructure, April 28 AHE paper [arXiv 2604.25850], late-April AgentFlow [arXiv 2604.20801]). Per-chapter integrations across Ch04 §4.5 / §4.8 / §4.9, Ch07 (MCP as synthesis dimension), Ch08 (portable substrate), and three new glossary terms (Managed Agents, Harness Synthesis, Session-hour pricing). Adds a fifth thread to `## The Pattern` ("harness synthesis as a viable engineering surface"). Plus 9 attribution fixes per `CONTRIBUTING.md` inclusion-criteria audit, including renamed §4.2 "The Böckeler Taxonomy" (was misattributed as "Fowler-Bockeler 2025"; actual is Birgitta Böckeler, April 2 2026, on martinfowler.com), softened OpenAI Codex case-study citation, dropped swyx IMPACT person attribution, verified Heinrich/arscontexta and Griciūnas URLs in Ch05, and replaced unverifiable Pento MCP citation with npm/PyPI primary statistics in Ch07.

---

## April 2026

### 2026-04-30 — Anthropic P/G/E attribution soften

- **PR #12** — Ch04 §4.6 rewrite. The earlier "Anthropic three-agent architecture" framing cited a fabricated "Multi-Agent Systems: Planner-Generator-Evaluator Architectures" research report. Replaced with Anthropic's verified [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents) URL plus an explicit note that the practitioner-community P/G/E summary is a pedagogical synthesis built on Anthropic's orchestrator-worker and evaluator-optimizer patterns. Cross-references the March 31 Claude Code source-leak finding that the actual production architecture is layered self-healing memory.

### 2026-04-25 — Late-April content + inclusion criteria

- **PR #11** — Four new April 2026 timeline entries plus integrations across Ch04, Ch06, Ch09, Ch11, and the glossary.
- **PR #10** — `CONTRIBUTING.md` formalizes the **inclusion test**: "Does this event introduce, validate, or operationalize a primitive, pattern, or narrative beat that the framework tracks?" Establishes the per-event-type bar (model release, protocols, primary research, surveys, products, market events) and the academic-policy two-lane rule. Backfilled across Ch11 timeline. This is the editorial spine the May 2026 update used to filter Tier 1 vs Tier 2 candidates.

### 2026-04-23 — README expansion

- **PR #9** — README adds **Use Cases** table (5 real-world build scenarios mapped to core chapters) and **The Lifecycle** section (INGEST → PROCESS → STORE → QUERY → IMPROVE flow), plus dedupe of the Ecosystem Map ASCII / mermaid pair.

### 2026-04-16 — April mid-month research wave

- **PR #8** — Integrates April mid-2026 research into Ch02 / Ch04 / Ch06 / Ch09 plus glossary updates (Meta-Harness, mHC, ARC-AGI-3 entries gain chapter-body context).
- **PR #7** — Seven April mid-2026 timeline entries (CATTS, Titans+MIRAS, ARC-AGI-3, ERNIE 5.0 follow-up, mechanistic interpretability operationalization, plus the OpenAI CoT-monitoring catch and Anthropic emotion vectors / iteration head disclosures).

### 2026-04-10 — Cab essay + Advisor Tool + ecosystem batch

- **PR #6** — Ch04 integrates Cab's *Layer-by-Layer Walk Through Harness Engineering* essay as the gentle on-ramp for the chapter's theory-first framings.
- **PR #5** — Adds the Advisor Tool section to Ch04 §4.5 plus a Ch11 timeline entry. Documents the first productized meta-harness primitive (Anthropic's `advisor_tool_2026-03-01` beta exposing the Stanford / MIT / KRAFTON 6x harness gap as a single tool call).
- **PR #4** — Eight April 2026 ecosystem events added to Ch11 timeline (MCP Dev Summit + SEP-1686 Tasks primitive, Bedrock AgentCore stateful MCP, Google Agent Skills Spec, Mem0ᵍ graph memory production release, Claude Mythos Preview, AI Velocity Paradox report, MemPalace, Open-Source Harness Builder Wave).

### 2026-04-08 — Community infrastructure

- **PR #3** — Adds CONTRIBUTING.md (initial version), issue / PR templates, code of conduct entry points.

### 2026-04-07 — i18n initial release

- **PR #2** — Ships translation infrastructure with five language READMEs: 繁體中文, 简体中文, 日本語, 한국어, Español. Each translation banners "chapter content remains in English." Translations mirror the English README only; chapter translations are out of scope at this stage.

### 2026-04-06 — Initial fact-check pass

- **PR #1** — Gemini-CLI-assisted fact-check pass on the initial release. Corrects citation drift introduced during the original assembly.

---

## Pre-April 2026

The initial release shipped before this changelog was kept. See `git log` for granular history before April 2026.

- **Initial release** — twelve chapters (Ch01–Ch12), Ch11 curated timeline, glossary, ecosystem-map and timeline diagrams, and the framing thesis: prompt → context → harness as three nested generations.
- **Diagrams** — `diagrams/ecosystem-map.png` and `diagrams/timeline.png` shipped alongside the initial release; pending refresh as of mid-2026 to capture Managed Agents / Routines / Memory primitives and the AHE / AgentFlow harness-synthesis arc.

---

## Conventions

- **Each entry is one PR.** PR number links to the merge commit; commit hashes are stable references for archival linking.
- **Dates are HKT.** When secondary sources differ on a date for an event the timeline cites, the entry uses the most credible primary source's date and notes the divergence.
- **Hedged citations.** The May 2026 audits softened wording on three persistent `[unable-to-attribute]` items: swyx's IMPACT framework (no primary source), Heinrich's specific February 2026 viral metrics (numbers not independently verifiable), and the Anthropic "Multi-Agent Systems" research-report title (no Anthropic publication with that exact title surfaces). These are noted in the relevant chapters and Sources blocks rather than cited as load-bearing facts.
- **Translations follow the English version.** Per `CONTRIBUTING.md`, translation PRs sync forward to match the English README; the English version leads.
