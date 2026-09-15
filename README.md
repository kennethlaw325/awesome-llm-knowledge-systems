# The Map Everyone's Missing: LLM Knowledge Engineering in 2026

**English** | [繁體中文](translations/README-zh.md) | [简体中文](translations/README_zh-CN.md) | [日本語](translations/README_ja.md) | [한국어](translations/README_ko.md) | [Español](translations/README_es.md)

> I analyzed 50+ awesome lists, surveys, and guides -- none of them connected the dots. RAG papers don't mention harness engineering. Memory frameworks ignore skill systems. MCP docs skip progressive disclosure. This guide draws the complete map.

<details>
<summary><b>What's new in September 2026</b> (click to expand)</summary>

The mid-September 2026 wave adds ten timeline entries — nine external plus this guide's own survival-gate result — and integrations across ten chapters and the glossary. The through-line is the security layer catching up with the primitives it has been trailing: the first shipped runtime-detection product for AI agents (CrowdStrike's Falcon Guardian) lands the same day AIR leaves stealth with $50M and a measurement of the exposed surface, OpenAI ships the first model it designates *Critical* for cybersecurity and writes a refusal contract into a broadly available release, and Anthropic's September threat report alleges industrial-scale distillation by named Chinese labs. In the same window Chapter 14's own September survival gate came due, and the verdict splits: the term survived the circulation test the gate stated, its status as a distinct engineering layer is unproved. It builds on the late-August wave (the harness layer going open-source on both sides of the Pacific inside a week) and the early-August wave (Metis). Most recent first (full chronological log: [CHANGELOG.md](CHANGELOG.md)):

- **September 15 Chapter 14's survival gate comes due** — the gate this guide published in July is checked and the verdict splits: the term survived the circulation test it stated (independent essays through August and September, plus a paid course teaching the agent-organization sense), but no vendor adoption was found in the documentation checked, the production case study is met only retrospectively by Anthropic's June 2025 multi-agent research system, and its status as a distinct engineering layer stays unproved and outside the numbered generations ([Ch14 §14.7](chapters/14-graph-engineering.md), [Ch01](chapters/01-evolution.md), [Ch11](chapters/11-timeline.md), glossary)
- **September 11 Salesforce ships a long-horizon runtime for Agentforce** — memory that persists between sessions, durable execution that keeps a plan running across them, and dynamic steering mid-run, announced alongside a portfolio of seven job-scoped agents, with Hunter the first on the runtime in pilot; the demand-side half of the 14-day sessions AWS put into the substrate, though "pursues goals across days and weeks" is Salesforce's own claim and Hunter, the agent built to demonstrate it, reaches general availability in November 2026 ([Ch04 §4.9](chapters/04-harness-engineering.md), [Ch11](chapters/11-timeline.md))
- **September 10 Anthropic's threat report alleges industrial-scale distillation** — the September threat-intelligence report alleges Moonshot AI routed Kimi customer requests to Claude through 5,380 fraudulent accounts, close to 300,000 requests inside a ten-day cluster and more than 23 million exchanges across May-July, and attributes over 151 million exchanges to Alibaba across the same window, naming DeepSeek, Z.ai, Xiaomi, MiniMax and SenseTime alongside them; every figure is Anthropic's allegation against competitors with no independent adjudication, read from the report's own distillation section ([Ch09](chapters/09-china-ecosystem.md), [Ch11](chapters/11-timeline.md))
- **September 4 Does agent memory survive a model upgrade?** — a controlled study finds fixed-schema graph memory near-invariant under a model swap (accuracy moving 0.0004 plus or minus 0.0020) while compressed notes swing +9.91 or -13.28 points, and attributes roughly 80% of note degradation to information discarded at *write* time — so keeping the raw source beside the compressed form is what makes repair work (34 of 48 cases, in one of the two tested migration directions); two authors and 48 synthetic cases, a design rule on a narrow evidence base ([Ch06](chapters/06-agent-memory.md), [Ch02](chapters/02-knowledge-layer.md), [Ch11](chapters/11-timeline.md))
- **September 3 GPT-6 Astra crosses OpenAI's Critical cybersecurity threshold** — the first model OpenAI calls Critical for cybersecurity under its Preparedness Framework; the shipped model refuses work such as generating proof-of-concept exploits and OpenAI names Daybreak and Daybreak Blue as the planned path for vetted defenders, while access itself rolls out broadly with enterprise workspaces off by default at launch — and the same safety overview reports chain-of-thought monitorability *decreasing*, including sandbagging that stays undetected; ExploitBench 100% against 78.5%, ExploitGym 42.4%, SRE-Bench 88.0% first-attempt are all OpenAI's own figures, measured without production safeguards ([Ch04 §4.2](chapters/04-harness-engineering.md), [Ch11](chapters/11-timeline.md))
- **September 1 Skill security goes commercial: Falcon Guardian and AIR's $50M** — CrowdStrike launches Falcon Guardian, which inventories known and shadow AI agents on Windows and macOS endpoints and then applies policy enforcement and runtime detection — the first shipped product answering §5.10's publish-time-scanning-to-runtime-containment argument, with no efficacy number in either fetched source; the same day AIR leaves stealth with $50M and reports 17,800+ public AI add-ons, roughly 6.7M installations, depending on untrusted external instruction sources, its own numbers on an unpublished methodology ([Ch05 §5.10](chapters/05-skill-systems.md), [Ch11](chapters/11-timeline.md))
- **August 20 StateMemBench adds recency supersession as a memory-evaluation axis** — 234 multi-session scenarios revise a fact, a constraint or a decision partway through, then ask whether the memory layer returns the value that currently holds or the superseded one; the third governance axis after GateMem (access control) and MemSyco-Bench (sycophancy), and the first of the three to arrive with a fix attached rather than a null result — StateMem reports 1.8x current-state accuracy on DeepSeek-V4-Flash and, as a wrapper over six backends, +15 to +32 points after controlling for the context it adds, all the paper's own numbers, unreplicated ([Ch06](chapters/06-agent-memory.md), [Ch11](chapters/11-timeline.md))
- **July 30 Gemini Enterprise Agent Platform: Memory Bank reaches GA** — Agent Memory Bank (conversation context extracted into a developer-defined schema), Agent Runtime with continuous agents up to seven days, Agent Identity as a native IAM type, an Agent Gateway and an Agent Registry — five capabilities reaching general availability together; every capability description is Google's own, and this is the GA of the renamed successor to Vertex AI Memory Bank's July 2025 public preview rather than a first announcement — with TencentDB four days later it makes managed memory a cloud-vendor category ([Ch06](chapters/06-agent-memory.md), [Ch04 §4.9](chapters/04-harness-engineering.md), [Ch11](chapters/11-timeline.md))
- **July 29-30 Three memory papers in two days** — the first systematic study of the markdown-directory-tree memory pattern (arXiv 2607.26637; keeping the store organized roughly halves retrieval cost once it is large, though organization erodes for all but the strongest management agent and no agent it measures turns organization into better answers), MemTxn's transaction boundary around memory *writes* (arXiv 2607.27834; 60 source-supported updates accepted and 179 constructed negatives rejected on the authors' own small validation set, with a separate team's MemTX three days earlier making transactional memory two independent proposals rather than one thread), and Memory Decoder at Scale (arXiv 2607.27919; a 6.9B memory module lifting a 410M Pythia base past Pythia-12B's 17-benchmark average at 39% fewer total parameters, the authors' own figures) — filesystem, governed store and weights each got a result inside forty-eight hours ([Ch06](chapters/06-agent-memory.md), [Ch11](chapters/11-timeline.md))
- **July 29 Chinese models sweep OpenRouter's weekly top five** — Xiaomi's MiMo-V2.5 at #1 ahead of DeepSeek, MiniMax, Qwen and Kimi, the first all-Chinese top five in OpenRouter's global weekly token-usage ranking, with the lead still holding in early September; OpenRouter publishes rankings as a live rolling view with no historical archive, so both the sweep and the share figures rest on secondary analyses, and the "more than 60%" of routed traffic around the July sweep and the early-September "46.4%" are different measurements reported separately, never joined into a trend line ([Ch09](chapters/09-china-ecosystem.md), [Ch11](chapters/11-timeline.md))

*From earlier waves (full detail in [CHANGELOG.md](CHANGELOG.md)):*

- **August 22 The new MCP roadmap** — under four weeks after the final specification, the core maintainers formalize governance (Contributor Ladder, Working-Group SEP triage, a feature lifecycle and deprecation policy) and name five priorities: agentic messaging primitives with *Tasks moving toward the core*, HTTP-native transport for local deployments, agent identity via DPoP and Workload Identity Federation, tool-result handling and progressive discovery over large catalogs, and SDK conformance ([Ch07](chapters/07-mcp.md), [Ch11](chapters/11-timeline.md))
- **August 19 OpenAI repositions Codex as a platform** — `codex exec`, the Codex SDK, and *app-server* ship under Apache 2.0 as a decoupled harness product while model access stays proprietary; note that `openai/codex` has been public and Apache-2.0 since April 2025, so this is a repositioning, not a first open-sourcing, and the ARC-AGI-3 13.3%→38.3% at 6x fewer output tokens figure is OpenAI's own ([Ch04 §4.7](chapters/04-harness-engineering.md), [Ch11](chapters/11-timeline.md))
- **August 19 Anthropic's Skills API reaches GA** — `/v1/skills` leaves beta (release note August 19, companion blog August 20) inside a wider production-agent GA wave; twelve days earlier, GitHub-hosted skills let Managed Agents auto-discover a mounted repo's `.claude/skills` at session start, with Anthropic's own docs noting the repo becomes part of the agent's *trust boundary* with no review step ([Ch05 §5.2](chapters/05-skill-systems.md), [Ch11](chapters/11-timeline.md))
- **August 13 DeepSeek Harness (dsh)** — an MIT-licensed agent harness whose model adapter, tool registry, session log, sandbox, storage, scheduler, and UI are all swappable plugins ("Cordis"), with an append-only log of every context injection; 190,630 stars / 21,319 forks in 11 days (GitHub API, checked August 24) extends China's open-source-first logic from weights to the harness ([Ch09](chapters/09-china-ecosystem.md), [Ch11](chapters/11-timeline.md))
- **August 10 Meta Muse Glimmer** — a 30B dense Apache-2.0 model distilled from Muse Spark and built for local agents (under 20GB at 4-bit, single consumer GPU) with day-0 support across Ollama, llama.cpp, MLX, ExecuTorch, vLLM and more; the first US frontier lab shipping for the single-GPU local case rather than server-class open weights, with all speedup and benchmark figures Meta's own ([Ch12](chapters/12-local-models.md), [Ch11](chapters/11-timeline.md))
- **August 7 Claude Code ships cross-session agent messaging** — `ListAgents` and `SendMessage` make named sessions addressable to each other with per-session inbound accept / hold / refuse governance, while no history, files, or permission approvals cross the boundary; a major vendor shipping Chapter 14's *org graph* primitive without ever using the phrase "graph engineering" ([Ch14 §14.2](chapters/14-graph-engineering.md), [Ch11](chapters/11-timeline.md))
- **August 6 The Paperclip skill campaign** — impersonated `paperclipai` and `browser-use` orgs published skills that were benign on July 5, weaponized on July 11, and #8 trending; the payload swept 138 credential paths through four independent trigger mechanisms, and the >1.7M install counter is an aggregate, not unique agents — the time-of-check-to-time-of-use pattern scaling from one fake skill to a whole family ([Ch05 §5.10](chapters/05-skill-systems.md), [Ch11](chapters/11-timeline.md))
- **August 6 AWS AgentCore: Temporal Policies + Runtime Instances GA** — deterministic, deny-by-default authorization that evaluates a tool call against the agent's *prior session history*, written in the new Apache-2.0 Dogwood policy language; shipped the same day as Runtime Instances GA, whose customer-selected EC2 sessions run up to 14 days against the serverless default's 8 hours ([Ch04 §4.1](chapters/04-harness-engineering.md), [Ch11](chapters/11-timeline.md), glossary)
- **August 3 TencentDB Agent Memory v2.0 adds Team Memory** — private / team / restricted / agent *visibility tiers* over four versioned memory asset types, a Memory Proxy speaking both Anthropic's and OpenAI's protocols, and L0-L3 distillation: the first shipped answer to the access-control axis GateMem found no framework satisfies, though every governance claim is Tencent's own and no independent benchmark exists ([Ch06](chapters/06-agent-memory.md), [Ch11](chapters/11-timeline.md))
- **August 2 Practical online KV-cache compaction for agents** — the first systematic study of compaction on *agent trajectories*: compacting immediately costs accuracy, delaying until the agent's own later queries act as a proxy-query signal recovers most of it, and token eviction beats attention-matching reconstruction — 80% cache reduction with better throughput than no compaction at all ([Ch03 §3.3](chapters/03-context-engineering.md), [Ch11](chapters/11-timeline.md))
- **July 29 MemTensor's Metis proposes memory foundation models** — MemTensor (Shanghai), the same lab behind June's agent-native-memory survey, joined by co-authors from Renmin University / NUS / SJTU / Tongji, proposes agent memory as *persistent, parametric state inside the transformer backbone itself* rather than an external store: a frozen Qwen3.5 backbone (4B/9B/27B) with only a Fast-Weight-Programming-inspired "hyper memory block" and "local memory block" trained, updated at inference by a gradient-free EMA-style pass; the paper itself reports long-horizon information loss under fixed-size compression and "information confusion in some cases, possibly caused by the blending of semantics within the latent space" ([Ch06](chapters/06-agent-memory.md), [Ch11](chapters/11-timeline.md), glossary)
- **July 29 LangChain ships Deep Agents v0.7** — removes the framework's default base system prompt, trims built-in tool descriptions 43%, and makes the todo-list planning scaffold opt-in after evals across three model families found no measurable gain from it, cutting base input tokens on a default agent turn roughly 65% (~6k to ~2k) — a production instance of this guide's stress-testing discipline ([Ch04 §4.8](chapters/04-harness-engineering.md), [Ch11](chapters/11-timeline.md))
- **July 29 MinIO ships AIStor Memory** — an object-storage-backed layer for agent memory, workspace state, and credentials, positioned to replace a hand-assembled stack of vector store, metadata database, and credential tooling with a durable, customer-owned, full-fidelity record ([Ch11](chapters/11-timeline.md))
- **July 28 The MCP 2026-07-28 specification ships final** — the largest revision since authorization was added: a *stateless request/response core*, Multi Round-Trip Requests (SEP-2322), RFC 9207 issuer validation, Client ID Metadata Documents replacing Dynamic Client Registration, and a formal extensions framework, with a 12-month deprecation window for Roots / Sampling / Logging / HTTP+SSE ([Ch07](chapters/07-mcp.md), [Ch11](chapters/11-timeline.md), glossary)
- **July 24 Claude Opus 5** — pricing unchanged from Opus 4.8 at half Fable 5's rate, 1M context / 128K output, a *five-level `effort` dial*, paid Fast mode, and mid-conversation tool changes without prompt-cache invalidation (beta); benchmark figures are Anthropic's own claims ([Ch04 §4.10](chapters/04-harness-engineering.md), [Ch11](chapters/11-timeline.md))
- **July 17-22 New Chapter 14 — Graph Engineering** — the second layer-name in six weeks gets a full chapter: Steinberger's July 17-18 catalyst post, the org-graph / work-graph split (Thakker), loops supervising loops held down by *anchors* (Perez), governed topologies (TrueFoundry, Eigent), and LangChain's double-edged "3 Years of Graph Engineering with LangGraph" response — framed as *emerging and contested*, two weeks old, with the skeptics given equal weight and an explicit September 2026 survival gate — checked September 15, 2026: circulation survived, distinct-layer status unproved ([Ch14](chapters/14-graph-engineering.md), [Ch01](chapters/01-evolution.md), glossary)
- **July 18 Anthropic resolves Fable 5 subscription access** — Max and Team Premium keep Fable 5 permanently from July 20 at 50% of weekly usage limits, while Pro and Team Standard move to usage-credit rates — closing the arc that began with the June 12 export-control suspension ([Ch11](chapters/11-timeline.md))
- **July 17 Moonshot releases Kimi K3** — at 2.8T parameters (MoE) the largest open-weight model ever released, with 1M context and native vision; topping Arena's frontend coding leaderboard as an open-weight model, weights following July 27 under Moonshot's bespoke Kimi K3 License ("open weight," in the company's own framing, not "open source") — server-class only, so the open-weight frontier widens without changing the local-deployment story ([Ch09](chapters/09-china-ecosystem.md), [Ch11](chapters/11-timeline.md))
- **July 17 WAIC 2026 and the founding of WAICO** — the World AI Conference in Shanghai produces the agreement establishing the World Artificial Intelligence Cooperation Organization, the first intergovernmental organization dedicated to AI, headquartered in Shanghai ([Ch09](chapters/09-china-ecosystem.md), [Ch11](chapters/11-timeline.md))
- **July 14 New Chapter 13 — Loop Engineering** — the June 2026 "loop engineering" frame gets a full chapter: Peter Steinberger's catalyst post, Addy Osmani's naming essay and "Own the Outer Loop" follow-up, Boris Cherny, the generator-evaluator split (Rajasekaran), Stripe's minions, LangChain's four stacked rungs, and adoption signals — framed as *emerging and contested*, five weeks old with no academic literature yet ([Ch13](chapters/13-loop-engineering.md), [Ch01](chapters/01-evolution.md), glossary)

</details>

---

## TL;DR

- **Prompt engineering was just the beginning.** The field has evolved through three generations: Prompt Engineering (2022-2024), Context Engineering (2025), and Harness Engineering (2026). Each layer subsumes the last -- and a contested fourth layer, *loop engineering*, emerged in mid-2026 ([Ch13](chapters/13-loop-engineering.md)). Six weeks later came a fifth claim, *graph engineering*, put under a survival gate that was checked on September 15, 2026: it remained in circulation as a contested name for multi-agent coordination, and a distinct fifth layer is unproved ([Ch14](chapters/14-graph-engineering.md)).
- **RAG is not dead.** 71% of enterprises that tried context-stuffing came back to RAG within 12 months (Gartner Q4 2025). Hybrid architectures are winning.
- **Context engineering is about what surrounds the call, not the call itself.** Andrej Karpathy's mid-2025 reframe shifted focus from crafting prompts to constructing the entire context window dynamically.
- **Harness engineering is the operating system layer.** Birgitta Böckeler (writing in Martin Fowler's *Exploring Generative AI* memo series, April 2026) and the OpenAI Codex team's harness-design framing formalized this -- the model is the CPU, context is RAM, and the harness is the OS that orchestrates everything.
- **No single guide connected all of this until now.** RAG, knowledge graphs, long context, MCP, skill routing, memory systems, and progressive disclosure are all part of one ecosystem. This is the map.

---

## Start Here

AI tools are getting smarter every year, but they only work well when they receive the right information at the right time. This guide explains how that works -- from the basics of telling an AI what to do, all the way up to designing entire systems around AI models.

Think of AI like a brilliant new employee on their first day. Prompt engineering is giving them a single task. Context engineering is giving them all the background information they need to do the task well. Harness engineering is designing their entire work environment -- their desk, their tools, their filing system, their team structure -- so they can do their best work consistently. This guide covers all three, and shows how they connect.

If you are new to this topic, start with the [Glossary](glossary.md) for definitions of key terms. If you build AI applications, jump straight into the chapters below. If you just want the big picture, look at the Ecosystem Map diagram further down this page.

---

## Which Path Should You Take?

Not sure where to start? Pick the description that fits you best:

- **"I just want to understand what all these AI buzzwords mean."** -- Start with the [Glossary](glossary.md), then read [Chapter 1: The Three Generations](chapters/01-evolution.md).
- **"I'm building an AI application."** -- Read [Ch02: RAG, Long Context & Knowledge Graphs](chapters/02-knowledge-layer.md), then [Ch03: Context Engineering](chapters/03-context-engineering.md), then [Ch04: Harness Engineering](chapters/04-harness-engineering.md).
- **"I want to make my AI tools work better."** -- Read [Ch05: Skill Systems](chapters/05-skill-systems.md), then [Ch06: Agent Memory](chapters/06-agent-memory.md), then [Ch10: Case Study](chapters/10-case-study.md).
- **"I want my agents to run without me pushing every step."** -- Read [Ch13: Loop Engineering](chapters/13-loop-engineering.md), then [Ch04: Harness Engineering](chapters/04-harness-engineering.md) and [Ch06: Agent Memory](chapters/06-agent-memory.md).
- **"I'm wiring multiple agents together."** -- Read [Ch14: Graph Engineering](chapters/14-graph-engineering.md), then [Ch13: Loop Engineering](chapters/13-loop-engineering.md) and [Ch04: Harness Engineering](chapters/04-harness-engineering.md).
- **"I want to see real examples."** -- Jump straight to [Ch10: Case Study](chapters/10-case-study.md).
- **"I work with Chinese AI tools."** -- Start with [Ch09: The Chinese AI Ecosystem](chapters/09-china-ecosystem.md).
- **"I want the complete picture."** -- Read front to back, starting with Chapter 1.

---

## Use Cases

This guide helps you design systems for these real-world scenarios. Each row links to the chapters that matter most for that build:

| Scenario | What You're Building | Core Chapters |
|----------|---------------------|---------------|
| **Personal Second Brain** | Personal notes + papers + web clippings searchable via natural-language queries | [Ch02](/chapters/02-knowledge-layer.md) · [Ch05](/chapters/05-skill-systems.md) · [Ch08](/chapters/08-tools-landscape.md) |
| **Internal Company Knowledge Base** | Employees query policy / handbooks / runbooks — low hallucination bar, citations required | [Ch02](/chapters/02-knowledge-layer.md) · [Ch04](/chapters/04-harness-engineering.md) · [Ch06](/chapters/06-agent-memory.md) |
| **Developer Documentation Assistant** | Engineers query codebases / API docs / past incident postmortems across multi-repo environments | [Ch02](/chapters/02-knowledge-layer.md) · [Ch05](/chapters/05-skill-systems.md) · [Ch07](/chapters/07-mcp.md) |
| **Support / QA Agent** | Customer or internal tickets → context-aware replies with cited sources and follow-up memory | [Ch03](/chapters/03-context-engineering.md) · [Ch06](/chapters/06-agent-memory.md) · [Ch04](/chapters/04-harness-engineering.md) |
| **Domain-Specific Knowledge Automation** *(legal, healthcare, finance, engineering)* | Reuse decades of domain documents — regulated, IP-sensitive, often requires local models and audit trails | [Ch02](/chapters/02-knowledge-layer.md) · [Ch09](/chapters/09-china-ecosystem.md) · [Ch12](/chapters/12-local-models.md) |

If your scenario doesn't fit cleanly, it's probably a composition of these — start from the closest row and adapt.

---

## The Evolution

![The five layers of LLM engineering, each nested inside the next](diagrams/evolution-stack.png)

*Figure: Each generation contains the last rather than replacing it. The outer two are drawn dashed because they are claims, not settled layers -- loop engineering is tracked here as emerging, and Chapter 14's September 15, 2026 gate found that graph engineering survived as a circulating term while its status as a distinct layer stayed unproved.*

```
2022-2024               2025                    2026                    2026 (mid)?             2026 (late)??
PROMPT ENG        -->   CONTEXT ENG       -->   HARNESS ENG       -->   LOOP ENG (emerging) --> GRAPH ENG (contested)
                        (Karpathy)              (Fowler, OpenAI)        (Steinberger, Osmani)   (Steinberger, Perez)

"Craft the              "Construct the          "Orchestrate the        "Design the system      "Wire the org
 perfect prompt"        dynamic context         entire system           that prompts            of agents that
                        window"                 around the model"       the agent"              run the loops"
```

Each generation does not replace the last -- it contains it. Harness engineering includes context engineering, which includes prompt engineering. Loop engineering, a still-contested fourth layer, wraps all three -- the system that runs the harness on a timer, spawns helpers, and feeds it back to itself. Graph engineering, the July 2026 claim covered in [Ch14](chapters/14-graph-engineering.md), would wrap even that -- the wiring of multiple loops into a designed organization -- and the September 15, 2026 check of that chapter's own survival gate left the question open on purpose: the term circulates, but no vendor adoption was found in the documentation checked, two vendors shipped the governance it names without it, and its status as a real fifth layer rather than three-year-old practice with a new name (LangChain's counter) is unproved.

---

## The Lifecycle

The Ecosystem Map shows **what** the pieces are. The Lifecycle shows **how data moves through them**:

```
                    ┌───── feedback ──────────────┐
                    ▼                             │
 INGEST  ───▶ PROCESS  ───▶ STORE  ───▶ QUERY ───▶ IMPROVE
    │             │            │          │           │
 Docs          Chunking      Vector DB    RAG        Evals
 APIs          Embeddings    Graph DB     GraphRAG   Feedback
 Web clips     Cleaning      Cache        Agents     Fine-tune
 Crawlers      Multi-modal   Long doc     Tool use   Skill updates
    │             │            │          │           │
   Ch02       Ch02 · Ch03    Ch02-08    Ch02-07     Ch06
```

```mermaid
flowchart LR
    I[INGEST<br/>Docs · APIs · Webscrape] --> P[PROCESS<br/>Chunking · Embeddings · Cleaning]
    P --> S[STORE<br/>Vector DB · Graph DB · Cache]
    S --> Q[QUERY<br/>RAG · GraphRAG · Agents]
    Q --> M[IMPROVE<br/>Evals · Feedback · Fine-tune]
    M -. feedback .-> I
```

Every production system moves data through all five stages — even if some are implicit. A good harness design makes **each stage inspectable and replaceable**. Ch02 covers Ingest/Process/Store; Ch03–Ch07 cover Query; Ch06 and Ch10 cover Improve.

---

## Ecosystem Map

![LLM Knowledge Engineering Ecosystem Map](diagrams/ecosystem-map.png)

*[View interactive HTML version](diagrams/ecosystem-map.html)*

```
+---------------------------+     +---------------------------+     +---------------------------+
|    KNOWLEDGE SOURCES      |     |   CONTEXT ENGINEERING     |     |   HARNESS ENGINEERING     |
|                           |     |                           |     |                           |
|  +---------------------+ | --> |  +---------------------+ | --> |  +---------------------+ |
|  | RAG Pipelines       | |     |  | Dynamic Context     | |     |  | Skill Systems       | |
|  | - Self-RAG          | |     |  |   Assembly          | |     |  | - Routing Logic     | |
|  | - Corrective RAG    | |     |  |                     | |     |  | - Progressive       | |
|  | - Adaptive RAG      | |     |  | KV-Cache            | |     |  |   Disclosure        | |
|  +---------------------+ |     |  |   Optimization      | |     |  +---------------------+ |
|                           |     |  |                     | |     |                           |
|  +---------------------+ |     |  | System Prompts      | |     |  +---------------------+ |
|  | Knowledge Graphs    | |     |  |   + Instructions    | |     |  | Memory Frameworks   | |
|  | - GraphRAG          | |     |  |                     | |     |  | - Short-term        | |
|  | - Entity Relations  | |     |  | Tool Definitions    | |     |  | - Long-term         | |
|  | - Multi-hop Queries | |     |  |   + Schemas         | |     |  | - Episodic          | |
|  +---------------------+ |     |  |                     | |     |  +---------------------+ |
|                           |     |  | Few-shot Examples   | |     |                           |
|  +---------------------+ |     |  |                     | |     |  +---------------------+ |
|  | Long Context        | |     |  | Conversation        | |     |  | MCP / Tool Layer    | |
|  | - 1M+ token windows | |     |  |   History           | |     |  | - Protocol Std      | |
|  | - Static doc ingest | |     |  +---------------------+ |     |  | - Tool Routing      | |
|  +---------------------+ |     +---------------------------+     |  | - Auth + Sandboxing | |
+---------------------------+                                       |  +---------------------+ |
                                                                    |                           |
                                                                    |  +---------------------+ |
                                                                    |  | Agent Runtime       | |
                                                                    |  | - Planning Loops    | |
                                                                    |  | - Error Recovery    | |
                                                                    |  | - Multi-agent       | |
                                                                    |  |   Coordination      | |
                                                                    |  +---------------------+ |
                                                                    +---------------------------+
```

```mermaid
graph LR
    subgraph Sources["Knowledge Sources"]
        RAG[RAG Pipelines]
        KG[Knowledge Graphs]
        LC[Long Context Windows]
    end

    subgraph Context["Context Engineering"]
        DCA[Dynamic Context Assembly]
        KVC[KV-Cache Optimization]
        SP[System Prompts + Instructions]
        TD[Tool Definitions + Schemas]
        FSE[Few-shot Examples]
        CH[Conversation History]
    end

    subgraph Harness["Harness Engineering"]
        SK[Skill Systems + Routing]
        MEM[Memory Frameworks]
        MCP[MCP / Tool Layer]
        AR[Agent Runtime + Planning]
        PD[Progressive Disclosure]
    end

    Sources --> Context --> Harness
```

---

## Table of Contents

### Chapters

| # | Chapter | Description |
|---|---------|-------------|
| 01 | [The Three Generations](/chapters/01-evolution.md) | From prompt engineering to context engineering to harness engineering |
| 02 | [RAG, Long Context & Knowledge Graphs](/chapters/02-knowledge-layer.md) | The knowledge retrieval layer -- what works, what doesn't, and why hybrid wins |
| 03 | [Context Engineering](/chapters/03-context-engineering.md) | The art of filling the context window -- KV-cache, the 100:1 ratio, dynamic assembly |
| 04 | [Harness Engineering](/chapters/04-harness-engineering.md) | Building the OS around the model -- guides, sensors, and the 6x performance gap |
| 05 | [Skill Systems & Skill Graphs](/chapters/05-skill-systems.md) | From flat files to traversable graphs -- progressive disclosure in practice |
| 06 | [Agent Memory](/chapters/06-agent-memory.md) | The missing layer -- episodic, semantic, and procedural memory architectures |
| 07 | [MCP: The Standard That Won](/chapters/07-mcp.md) | Model Context Protocol -- from launch to 97M+ monthly downloads (Q1 2026) |
| 08 | [AI-Native Knowledge Management](/chapters/08-tools-landscape.md) | Tools landscape -- Notion AI, Obsidian, Mem, and the AI-native gap |
| 09 | [The Chinese AI Ecosystem](/chapters/09-china-ecosystem.md) | Dify, RAGFlow, DeepSeek, Kimi -- a parallel universe of innovation |
| 10 | [Case Study: A Real-World Knowledge Harness](/chapters/10-case-study.md) | How one developer built a complete harness with 65% token reduction |
| 11 | [Timeline](/chapters/11-timeline.md) | Key moments in LLM knowledge engineering, 2022-2026 |
| 12 | [Local Models for Knowledge Engineering](/chapters/12-local-models.md) | Run your knowledge harness locally -- embedding, RAG, compilation, and the fine-tuning endgame |
| 13 | [Loop Engineering](/chapters/13-loop-engineering.md) | The emerging fourth layer -- designing the system that prompts the agent, and whether it is its own generation |
| 14 | [Graph Engineering](/chapters/14-graph-engineering.md) | The contested fifth claim -- wiring the organization of agents; it survived its September 2026 circulation gate and is still unproved as a distinct layer |

---

## Why This Guide Exists

The LLM ecosystem in 2026 has a fragmentation problem. Not a lack of information -- an excess of disconnected information.

There are mass surveys on RAG. Comprehensive prompt engineering guides. MCP specification documents. Agent framework comparisons. Memory system papers. Each one is excellent in isolation. None of them show you how the pieces fit together.

This guide is that missing layer. It connects RAG to context engineering, context engineering to harness engineering, harness engineering to agent runtimes -- and shows you the decisions that matter at each boundary.

---

## Contributing

Contributions are welcome! This list is community-maintained.

- **Add a resource:** [Submit a Pull Request](../../pulls) -- see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines
- **Suggest a resource:** [Open an Issue](../../issues/new?template=suggest-resource.md)
- **Report a broken link:** [Open an Issue](../../issues/new?template=report-broken-link.md)
- **Discuss:** [Join the Discussion](../../discussions)
- **Translations**: Translation PRs go in `/translations/`. Maintain the same file structure. Available translations: [繁體中文](translations/README-zh.md) | [简体中文](translations/README_zh-CN.md) | [日本語](translations/README_ja.md) | [한국어](translations/README_ko.md) | [Español](translations/README_es.md)

Please keep the tone professional but accessible. Cite sources. No hype.

---

## License

MIT License. See [LICENSE](LICENSE) for details.

Use this however you want. Attribution appreciated but not required.

---

*Last updated: September 2026*
