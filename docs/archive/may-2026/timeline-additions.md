# May 2026 Update — Proposed Timeline Additions

**Status:** Draft proposals only. Not committed. Branch: `prep/may-2026-update`.
**Generated:** 2026-04-30 (HKT) by overnight prep agent
**Repo:** kennethlaw325/awesome-llm-knowledge-systems · target file: `chapters/11-timeline.md`

---

## Inclusion-criteria filter applied

Per `CONTRIBUTING.md`:

> **In:** First-of-a-kind capability, new economic point, new context-window class, new distribution model, new modality-fusion architecture.
> **Out:** Version bumps. The repo does not include Claude 3.5 / 3.7 / 4 / 4.5 / 4.6, GPT-5.x base, Gemini 2.x, the Llama series, etc.

The agent filtered ~10 candidate stories down to **5 proposed entries** (Tier 1) and **0 borderline (Tier 2)** that we recommend skipping.

Quality > quantity. If review wants to drop any of the 5, drop them — none are load-bearing for the existing narrative.

---

## TIER 1 — Recommended additions (5 entries)

### Proposed entry 1: April 7, 2026 — Mythos / Glasswing breach (~14 hours)

**Insertion point:** Augment the existing `### April 7, 2026 — Claude Mythos Preview` entry rather than create a new one. The current entry only describes the launch; it needs a 2-3 sentence addendum about the unauthorized-access incident.

**Why include:** Inclusion criteria explicitly cite "new distribution model (Mythos's Glasswing coalition)" — which means the operational reality of that distribution model (it was breached on day one) is part of the same story arc. This is a harness-as-security-perimeter case study, not a model release.

**Proposed addition (append to existing entry):**

> Within approximately 14 hours of the Glasswing program being publicly announced, Anthropic disclosed unauthorized access to Claude Mythos Preview "through one of our third-party vendor environments." The breach is significant for the harness narrative for two reasons. First, it makes concrete what "harness as security perimeter" means in practice: the model itself was not compromised, but the *distribution harness* — the third-party vendor stack used to gate Glasswing access — was. Second, it foreshadows the inversion of the cyber-defense thesis behind Mythos: a model whose stated job is to find vulnerabilities for defenders was itself reachable through the supply chain that fronted it.

**Sources:**
- Resultsense, "Anthropic probes unauthorised access to Claude Mythos" (2026-04-23): https://www.resultsense.com/news/2026-04-23-anthropic-mythos-unauthorised-access-probe
- Schneier on Security, "On Anthropic's Mythos Preview and Project Glasswing" (April 2026): https://www.schneier.com/blog/archives/2026/04/on-anthropics-mythos-preview-and-project-glasswing.html
- Arnav.au, "Anthropic Mythos AI Breach 2026" (2026-04-29): https://arnav.au/2026/04/29/anthropic-mythos-ai-breach-2026/

**Confidence:** High. Multiple independent sources, including a Bruce Schneier post. Anthropic's own incident framing ("third-party vendor environments") is the operative phrasing.

---

### Proposed entry 2: April 8, 2026 — Anthropic Managed Agents (Public Beta)

**Insertion point:** New entry, between `### April 7, 2026 --- Claude Mythos Preview` and the existing April 14 Routines entry. Chronologically correct.

**Why include:** This is the productized harness — strictly stronger than the existing "Routines" entry as a structural moment, because Routines is a triggering surface (schedules / API / GitHub events) while Managed Agents is the underlying *substrate* (sandboxed sessions, durable state, scoped permissions, tool execution, $0.08/session-hour pricing). Inclusion criteria: **new economic point** (per-session-hour pricing for hosted agent runtime is novel) + **new distribution model** (Anthropic now sells the orchestrator seat, not just inference).

**Proposed entry text:**

> ### April 8, 2026 — Anthropic Managed Agents (Public Beta)
>
> Anthropic ships **Claude Managed Agents** as a public-beta hosted runtime for long-horizon agent work. Where the Advisor Tool (April 2026) productized *what to think about* and Claude Opus 4.7's task budgets (April 16) productized *how hard to think*, Managed Agents productizes *where the loop runs*. The service exposes four primitives — **sessions** (durable context state outside the model's context window, with durable session logs), **harnesses** (Anthropic-managed orchestration with scoped permissions), **sandboxes** (Anthropic-operated execution environments for tool calls), and **tracing** — and prices the substrate at **standard API token rates plus $0.08 per session-hour**. The pricing detail matters: it is the first frontier-vendor primitive that bills the *orchestrator seat* itself, separate from inference. Read alongside the Manus acquisition (early 2026) and Routines (April 14), the trajectory is clear: the harness layer that 2025 framed as "the moat" is in 2026 being unbundled into vendor-sold primitives. The self-hosted harness is not gone, but its scope has narrowed to the workloads — local execution, sub-minute cadence, non-GitHub triggers, on-device data — that the managed primitives don't yet cover.

**Sources:**
- Anthropic API Docs, "Claude Managed Agents overview": https://platform.claude.com/docs/en/managed-agents/overview
- Anthropic Engineering, "Scaling Managed Agents: Decoupling the brain from the body": https://www.anthropic.com/engineering/managed-agents
- SiliconANGLE, "Anthropic launches Claude Managed Agents to speed up AI agent development" (2026-04-08): https://siliconangle.com/2026/04/08/anthropic-launches-claude-managed-agents-speed-ai-agent-development/
- InfoWorld, "Anthropic rolls out Claude Managed Agents": https://www.infoworld.com/article/4156852/anthropic-rolls-out-claude-managed-agents.html

**Confidence:** High. Primary Anthropic docs + multiple independent tech-press confirmations. Pricing of $0.08/session-hour confirmed via SiliconANGLE.

**Cross-chapter implication:** Ch04 (Harness Engineering) — Section 4.9 "Cloud-Native Harness Primitives" should add a paragraph distinguishing **Routines** (trigger surface) from **Managed Agents** (substrate). See `per-chapter-changes.md`.

---

### Proposed entry 3: April 27, 2026 — Microsoft–OpenAI Partnership Restructure

**Insertion point:** New entry, after the existing April 24 DeepSeek V4 entry, before "## The Pattern" section.

**Why include:** Inclusion criteria explicitly admit "new distribution model" as a qualifier. Removing OpenAI's cloud-exclusivity to Azure (it can now serve via AWS, GCP) and removing the **AGI clause** from the partnership agreement is a structural shift in how frontier AI gets distributed — and the AGI-clause removal in particular is a *narrative* moment for the field (the legal definition of AGI no longer load-bears commercial agreements between the two largest AI players). For a knowledge-systems guide, the relevant reframing is that "the model layer" is no longer plausibly going to be locked behind a single cloud — which has implications for the harness portability discussion.

**Proposed entry text:**

> ### April 27, 2026 — The Microsoft–OpenAI Restructure
>
> Microsoft and OpenAI announce an amended partnership agreement that materially loosens the relationship that has defined frontier model distribution since 2019. Three changes matter for the field, in declining order of long-term consequence:
>
> 1. **OpenAI's cloud exclusivity ends.** OpenAI can now serve API access to its models through any cloud provider, including AWS and Google Cloud. Microsoft remains primary cloud partner with first-product-ship rights on Azure, but the lockstep of "OpenAI = Azure" is gone.
> 2. **The AGI clause is removed.** The provision that would have let OpenAI exit financial obligations on a unilateral declaration that AGI had been achieved no longer exists. Investor valuations no longer hinge on a definition of AGI that no two parties agreed on.
> 3. **Revenue share is asymmetrically capped.** Microsoft no longer pays revenue share to OpenAI; OpenAI's payments to Microsoft continue through 2030 but under a total cap, not the open-ended structure that previously existed.
>
> The framing is widely reported as IPO preparation — OpenAI is targeting a Q4 2026 IPO at a possible ~$1T valuation, and removing the AGI commercial trigger and the cloud monogamy is what an IPO-ready cap table looks like. For knowledge engineers, the practical consequence is that the largest closed-weight frontier model will now be available under the same multi-cloud distribution shape that DeepSeek and the open-weight ecosystem already enjoy. "Pick your cloud" stops being a choice that constrains "pick your model" — at least for the GPT family.

**Sources:**
- Microsoft Official Blog, "The next phase of the Microsoft-OpenAI partnership" (2026-04-27): https://blogs.microsoft.com/blog/2026/04/27/the-next-phase-of-the-microsoft-openai-partnership/
- OpenAI, "The next phase of the Microsoft partnership": https://openai.com/index/next-phase-of-microsoft-partnership/
- CNBC, "OpenAI shakes up partnership with Microsoft, capping revenue share payments" (2026-04-27): https://www.cnbc.com/2026/04/27/openai-microsoft-partnership-revenue-cap.html
- PitchBook, "OpenAI loosens Microsoft's grip ahead of IPO push": https://pitchbook.com/news/articles/openai-loosens-microsofts-grip-ahead-of-ipo-push

**Confidence:** Very high. Both companies issued first-party announcements. CNBC and PitchBook independently confirmed financial details.

**Note:** This is borderline — it's an industry-structure event more than a knowledge-engineering primitive. If reviewer feels it skews too "business news," drop it. Primary justification is the inclusion-criteria phrase "new distribution model."

---

### Proposed entry 4: April 28, 2026 — Agentic Harness Engineering (AHE) paper

**Insertion point:** New entry, between the existing CATTS and Titans+MIRAS April entries (chronological grouping with the other April research papers).

**Why include:** This is a direct continuation of the **Meta-Harness** entry the repo already has under "March 2026 — The Research Papers." AHE is from a different group (Fudan / Peking / Shanghai Qiji Zhifeng) and reaches a stronger result by treating harness optimization as an *observability* problem rather than a search problem. The Meta-Harness story without AHE looks frozen in March; with AHE it shows the field is iterating in public.

**Proposed entry text:**

> ### April 28, 2026 — AHE: Observability-Driven Harness Evolution
>
> A team from Fudan University, Peking University, and Shanghai Qiji Zhifeng publishes **"Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses"** (arXiv 2604.25850). AHE reframes the harness-optimization problem the March 2026 Meta-Harness paper opened: instead of treating harness configurations as a search space and running an optimizer over it, AHE instruments three observability pillars — **component observability** (an explicit, revertible action space over harness components), **experience observability** (condensed trajectory evidence from prior runs), and **decision observability** (falsifiable edit predictions that the system commits to before executing them) — and lets the harness evolve itself by reading its own runtime signals.
>
> The benchmark numbers update the Meta-Harness story: starting from a Codex-CLI-style baseline at 69.7% pass@1 on Terminal-Bench 2, after 10 AHE iterations the harness reaches **77.0%**, surpassing the human-designed Codex-CLI baseline (71.9%) and showing **+5.1 to +10.1 pp cross-family gains** when transferred to model families the harness was not optimized on. The cross-family transfer detail is the structural news: an evolved harness is not just over-fit to one model's quirks, it carries forward as the substrate underneath turns over. For practitioners, AHE makes the discipline that Section 4.8 of this guide called "stress-testing" automatable — not as a single-shot search but as a continuous observability loop the harness runs against itself.

**Sources:**
- arXiv 2604.25850 (April 28, 2026): https://arxiv.org/abs/2604.25850 / HTML: https://arxiv.org/html/2604.25850
- GitHub repo: https://github.com/china-qijizhifeng/agentic-harness-engineering

**Confidence:** Very high. arXiv paper is primary source; abstract, results, and GitHub are all directly verifiable.

**Cross-chapter implication:** Ch04 Section 4.8 "Harness Maintenance: The Stress-Testing Imperative" should reference AHE as the automated counterpart to manual stress-testing.

---

### Proposed entry 5: Late April 2026 — AgentFlow & the harness-as-vulnerability-surface

**Insertion point:** New entry, after the AHE entry above. Chronologically grouped (both are April research-paper releases) and thematically tied (both are harness-synthesis papers).

**Why include:** AgentFlow demonstrates that automated harness synthesis is no longer a paper trick — the *same synthesis loop*, re-run on Chrome with Kimi K2.5, produced ten previously unknown zero-day vulnerabilities including two Critical sandbox-escape CVEs (CVE-2026-5280, CVE-2026-6297). This is the first published case of an automatically-synthesized agent harness producing externally-validated security findings. It belongs in the timeline because it closes the loop with the Mythos / Glasswing arc: the offensive side of the cyber thesis is no longer gated to one frontier vendor's preview tier — open-source synthesis can produce the same class of finding.

**Proposed entry text:**

> ### April 2026 — AgentFlow and Harness-Synthesis-as-Offensive-Capability
>
> "Synthesizing Multi-Agent Harnesses for Vulnerability Discovery" (arXiv 2604.20801) introduces **AgentFlow**, a typed-graph DSL over five harness dimensions (agent roles, prompts, tools, communication topology, coordination protocol) with a feedback-driven outer loop and structural validation for candidate edits. On **TerminalBench-2**, AgentFlow's synthesized harness reaches **84.3% with Claude Opus 4.6** — the highest score on the public Opus 4.6 leaderboard, and a step beyond AHE's 77.0% (on a different baseline model).
>
> The benchmark is not the news. The news is that the same synthesis loop, re-run on Chrome with Kimi K2.5 as the model, produced **ten previously unknown zero-day vulnerabilities, including two Critical sandbox-escape CVEs (CVE-2026-5280 and CVE-2026-6297)**. This is the first published instance of an automatically-synthesized agent harness producing externally-validated security findings. Read alongside Anthropic's Mythos coalition (April 7), AgentFlow shows that the offensive side of the cybersecurity thesis is no longer gated to one frontier vendor's preview tier — an open synthesis loop, an open model, and a target program are sufficient. The "harness as moat" framing of 2025 acquires a counterpart in 2026: **the harness as offensive capability**, with all the dual-use discomfort that implies.
>
> For knowledge engineers, AgentFlow + AHE together establish that harness synthesis is now a viable engineering surface. Practitioners building production harnesses in mid-2026 should expect the Manual / Meta-Harness / AHE / AgentFlow trajectory to compress: the design choices a senior harness engineer makes by hand today are the design choices a synthesis loop will make automatically tomorrow.

**Sources:**
- arXiv 2604.20801: https://arxiv.org/abs/2604.20801 / HTML: https://arxiv.org/html/2604.20801

**Confidence:** High. arXiv primary source. CVE numbers are claimed in the paper's own abstract — they should be independently spot-checked against NVD or MITRE before merging (see CHECKLIST).

**Cross-chapter implication:** Ch04 — extends the Meta-Harness / AHE arc. Possibly worth a one-line mention in Ch07 (MCP) given that AgentFlow's synthesis includes "tools" as one of the five dimensions.

---

## TIER 2 — Considered and rejected

These passed initial WebSearch but fail inclusion criteria. Listed for transparency:

| Candidate | Reason rejected |
|-----------|-----------------|
| **Claude Sonnet 4.6** (Feb 17, 2026) — 79.6% SWE-bench, 1M context | Version bump. CONTRIBUTING.md explicit out: "Claude 3.5 / 3.7 / 4 / 4.5 / 4.6". |
| **GPT-5.5** (April 23-24, 2026) — 82.7% Terminal-Bench 2.0 | Version bump. CONTRIBUTING.md out: "GPT-5.x base". |
| **Gemini 3.1 Pro** (April 2026 global rollout) — 77.1% ARC-AGI-2, 94.3% GPQA Diamond | Version bump on a 3.x line that itself launched November 2025. ARC-AGI-2 lift is real but doesn't redefine. |
| **MCP Registry v1.2.0** (April 20, 2026) — Redis-backed session routing, vMCP horizontal scaling | Registry hardening is operational, not narrative-defining. The April 2026 SEP-1686 Tasks entry already covers the MCP-as-orchestration-layer story. |
| **Claude Cowork GA** (April 9, 2026) — macOS/Windows GA with OpenTelemetry, RBAC | Product packaging of existing pieces. Doesn't open a new surface. |
| **plugin marketplace expansion** (Feb 2026 launch + April growth) — 423 plugins, 2,849 skills, 177 agents | Quantitative growth on the skill-system narrative. Already covered structurally by the December 2025 agentskills.io entry and the April 2026 Google Agent Skills Spec entry. |
| **Memoria / Supermemory / Memento LongMemEval results** (April 2026) | These are individual benchmark entries on an existing benchmark. The April 2026 MemPalace entry already covers the memory-architecture-race framing. |

---

## Sources index (for review)

All Tier 1 source URLs are real and HTTP-reachable as of 2026-04-30 HKT. None are paywalled. None are speculative.

| # | URL | Type | Notes |
|---|-----|------|-------|
| 1 | https://www.resultsense.com/news/2026-04-23-anthropic-mythos-unauthorised-access-probe | News | Mythos breach disclosure |
| 2 | https://www.schneier.com/blog/archives/2026/04/on-anthropics-mythos-preview-and-project-glasswing.html | Analysis | Schneier secondary commentary |
| 3 | https://arnav.au/2026/04/29/anthropic-mythos-ai-breach-2026/ | Blog | Independent timeline reconstruction |
| 4 | https://platform.claude.com/docs/en/managed-agents/overview | Anthropic primary | Managed Agents docs |
| 5 | https://www.anthropic.com/engineering/managed-agents | Anthropic primary | "Decoupling the brain from the body" engineering post |
| 6 | https://siliconangle.com/2026/04/08/anthropic-launches-claude-managed-agents-speed-ai-agent-development/ | Tech press | Launch-date confirmation, pricing |
| 7 | https://www.infoworld.com/article/4156852/anthropic-rolls-out-claude-managed-agents.html | Tech press | Independent confirmation |
| 8 | https://blogs.microsoft.com/blog/2026/04/27/the-next-phase-of-the-microsoft-openai-partnership/ | Microsoft primary | Restructure announcement |
| 9 | https://openai.com/index/next-phase-of-microsoft-partnership/ | OpenAI primary | Counterpart announcement |
| 10 | https://www.cnbc.com/2026/04/27/openai-microsoft-partnership-revenue-cap.html | News | Independent financial detail |
| 11 | https://pitchbook.com/news/articles/openai-loosens-microsofts-grip-ahead-of-ipo-push | Industry analysis | IPO framing |
| 12 | https://arxiv.org/abs/2604.25850 | arXiv primary | AHE paper |
| 13 | https://github.com/china-qijizhifeng/agentic-harness-engineering | Code repo | AHE companion code |
| 14 | https://arxiv.org/abs/2604.20801 | arXiv primary | AgentFlow paper |
