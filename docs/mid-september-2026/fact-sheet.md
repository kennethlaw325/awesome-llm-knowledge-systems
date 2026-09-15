# Mid-September 2026 Wave --- Fact Sheet (drafting source of truth)

> **Historical record.** PRE-fact-check drafting input assembled 2026-09-15 from the four research lanes plus the editor's selection. The adversarial fact-check re-verifies every load-bearing URL afterward; shipped text and CHECKLIST.md are authoritative.

Selection date: 2026-09-15 (HKT). Window: 2026-08-23 through 2026-09-15, plus assessed backfill. Research: 4-lane sweep (harness/loop/graph + survival gate; skills/MCP/tools; knowledge/context/memory; China/local), every candidate primary-source fetched where reachable, deduped against the repo; one gap-fill pass.

**Quote rule (COPY-EXACT-OR-PARAPHRASE-WITHOUT-QUOTES):** anything inside quotation marks must be a verbatim substring of a fetched source. Ellipsis may only delete, never substitute. Hedge words may not vanish inside a quote. When unsure: paraphrase, no quotes. Internal markers below (VENDOR-CLAIM / PIN-DATE / SECONDARY-ONLY / UNFETCHED / W#) are annotations and must never appear in shipped text.

---

# Part 1 --- Editor's selection


Selection date: 2026-09-15 (HKT). Window: 2026-08-23 through 2026-09-15, plus assessed backfill (pre-window).
Research inputs (4 lanes, same folder): research-r1-harness-loop-graph.txt (R1), research-r2-skills-mcp-tools.txt (R2),
research-r3-knowledge-context-memory.txt (R3), research-r4-china-local.txt (R4); gap fills in gapfill-01.txt (G1, may land later).
Item IDs below are the wave IDs (W#). "Source section" points at the researcher section holding the facts + URLs; drafters
read that section directly. Every URL must be copied in full from the research file; never abbreviate.

Ch08 note: chapters/08-tools-landscape.md is the AI-native knowledge-management (PKM) chapter, NOT production agent
frameworks (CONTRIBUTING.md:16 says "production frameworks" --- that line is stale). Nothing routes to Ch08 this wave.

## A. TIMELINE + CHAPTER (10 external entries; plus the Ch14 gate entry decided separately)

| W# | Date (per primary) | Title (working) | Chapter(s) | Source section | Editor notes / caveats to carry |
|---|---|---|---|---|---|
| W1 | 2026-09-01 | Skill security goes commercial: CrowdStrike Falcon Guardian + AIR emerges with $50M | Ch05 §5.10 (fourth beat) | R2 C1 + R2 C2 | ONE combined timeline entry (both Sep 1). CrowdStrike = first shipped runtime-detection product answering §5.10's "publish-time scanning -> runtime containment" line (chapters/05-skill-systems.md:161). AIR = June 22 disclosure author, now $50M + ecosystem numbers (17,800+ add-ons / ~6.7M installs on unverified instruction sources; skills impersonating Anthropic/OpenAI). All AIR numbers VENDOR-CLAIM (methodology unpublished). Date the entry Sep 1; note SecurityWeek Sep 3 as publish lag. |
| W2 | 2026-09-03 | GPT-6 Astra: first model to cross OpenAI's "Critical" cybersecurity tier | Ch11 + Ch04 (interpretability / CoT-monitorability thread, chapters/04-harness-engineering.md:59 area) | R1 C1 (+ G1 T1 for primary text) | Passes model-release bar as a first-of-a-kind threshold, NOT as a capability bump: frame around what deployment governance now has to do (limited-organization rollout first, refusal of proof-of-concept exploit tasks, Daybreak / Daybreak Blue vetted-defender expansion --- all verbatim on OpenAI's pages per gap-fill T1). The "enterprise access off by default / admin must enable" claim appears ONLY in CSOOnline secondary coverage, not on OpenAI's pages: do not state it. No pricing / context-window / max-output numbers (not on the primary pages). CoT-monitorability decrease is OpenAI's own statement on the safety overview (T1 (f)) --- cite it as such, not as an analyst view. Benchmarks on the safety page: ExploitBench 100% vs 78.5% (Sol), ExploitGym 42.4%, SRE-Bench 88.0% single-attempt / 99.2% within four (OpenAI's own). ExploitBench/ExploitGym numbers and zero-day count are OpenAI's own (VENDOR-CLAIM). Primary pages were fetched in gap-fill T1 (Exa): https://openai.com/index/gpt-6-astra/ , https://openai.com/index/safety-overview-gpt-6-astra/ (Published 2026-09-03), https://openai.com/index/path-to-astra/ (Published 2026-09-01) --- cite these, not the community repost. Do NOT include Claude Fable 5.1 / Mythos 5.1 (rejected as version bump). |
| W3 | 2026-09-11 | Salesforce ships a long-horizon runtime for Agentforce | Ch04 §4.9 (cloud-native harness primitives) --- NOT Ch08 | R2 C5 | Frame as demand-side complement to AWS Runtime Instances' 14-day sessions (already in §4.1/Ch11): infra existed, here is a production platform claiming multi-week goal pursuit (memory + durable execution + dynamic steering). Hunter agent is pilot-only (GA Nov 2026); "pursues goals across days and weeks" is VENDOR-CLAIM, no independent evidence. Skip the seven named agents beyond one clause. |
| W4 | 2026-08-20 | StateMemBench / StateMem: recency-supersession as a new memory-evaluation axis | Ch06 "Evaluation Grows Governance Axes" (chapters/06-agent-memory.md:111-125) | R3 C1 | Third axis after GateMem (access control) and MemSyco-Bench (sycophancy); unlike GateMem's null result it ships a fix (StateMem wrapper). Numbers are the paper's own, unreplicated. Dated Aug 20 (missed by the late-August wave). |
| W5 | 2026-09-04 | Does agent memory survive a model upgrade? Graphs yes, compressed notes no | Ch06 (memory locus thread, chapters/06-agent-memory.md:109) + Ch02 cross-ref (GraphRAG-as-index-layer, chapters/02-knowledge-layer.md:101) | R3 C3 | Concrete design rule: prefer structured/graph storage if memory must outlive a model swap; keep raw source alongside compressed forms. n=48 synthetic cases, two authors --- say so. |
| W6 | 2026-09-10 | Anthropic's September threat report alleges industrial-scale distillation by Chinese labs | Ch09 Section C "Open-Source as Strategic Imperative" (chapters/09-china-ecosystem.md:107-119), new subsection | R4 C1 | Adversarial counter-narrative to the chapter's thesis. Every number (5,380 accounts, ~300K requests, 23M+ exchanges) is Anthropic's allegation AND was read from secondary coverage --- carry both caveats; the report URL is the primary and the fact-check must fetch its distillation section. Name the labs Anthropic names; no editorializing on guilt. |
| W7 | 2026-07-29 (backfill) with Sept continuation | Chinese models sweep OpenRouter's weekly top 5, then keep the lead into September | Ch09 Section C strengthener | R4 B6 + R4 C6 | ONE entry dated Jul 29 whose body carries the early-Sept continuation. SECONDARY-ONLY throughout (OpenRouter rankings page is live-only; archive unreachable). Report the two share figures (">60%" in July analyses; "46.4%" early Sept) each with its own source and an explicit note that they are not the same measure; never combine them into a trend line. Fact-check: try OpenRouter API / archive. |
| W8 | 2026-07-29 to 07-30 (backfill) | Three memory papers in two days: Filesystem-Based Memory, MemTxn, Memory Decoder at Scale | Ch06 (three separate chapter integrations: ByteRover/filesystem pattern; Mem0-g conflict resolver + GateMem thread; Trainable Memory Modules chapters/06-agent-memory.md:83) | R3 B3c, B3b, B3a (+ G1 T5 on MemTxn vs MemTX) | ONE combined timeline entry. Filesystem paper (arXiv 2607.26637, Jul 29): first systematic study of the markdown-tree memory pattern; organized stores roughly halve retrieval cost at scale. MemTxn (arXiv 2607.27834, Jul 30): transaction boundary for memory writes (60/179 accept/reject validation set --- say small). Memory Decoder at Scale (arXiv 2607.27919, Jul 30): 6.9B memory module + 410M base beats Pythia-12B average at 39% fewer total params. If G1 shows MemTX (2607.23929) is the same team, mention once; if independent, mention as parallel proposal. |
| W9 | 2026-07-30 (backfill; brief said Jul 29 --- use the blog's own date) | Gemini Enterprise Agent Platform: Memory Bank GA alongside Agent Runtime, Identity, Gateway/Registry | Ch06 (vendor managed-memory category, next to TencentDB) + Ch04 cross-ref (7-day Agent Runtime; Agent Identity as native IAM type) | R3 B2 | Distinguish from the July 2025 Vertex AI Memory Bank preview. All capability language is Google's (VENDOR-CLAIM). Frame Ch06 addition as "cloud vendors are shipping managed memory as a category" (TencentDB Aug 3 + Google Jul 30). |
| W10 | 2026-09-15 | Ch14 survival gate result (title depends on verdict) | Ch14 + Ch11 | Astra verdict file astra-gate-verdict.txt + R1 Section E + precheck | DECIDED SEPARATELY after the round-table; drafter for Ch14/Ch01/README/glossary receives a separate brief. Do not draft W10 in the chapter-drafter pass. |

## B. CHAPTER-ONLY (no timeline entry; CHANGELOG lists them)

| W# | Date | Item | Chapter / section | Source section | Editor notes |
|---|---|---|---|---|---|
| W11 | 2026-09-10 | Anthropic Managed Agents `auto` permission policy (server-evaluated per-call allow / deny / pause, applies to MCP toolsets) | Ch04 §4.1 immediately after the Temporal Policies paragraph (chapters/04-harness-engineering.md:36); one-clause cross-ref in Ch07 (authorization / meta-tool discussion, chapters/07-mcp.md:146 area) | R2 C3 | Frame as the second answer to the Authority axis in five weeks: AWS = deterministic policy language evaluated at the gateway; Anthropic = model-evaluated per-call judgment with an `evaluation` object and reason codes; quote the docs' "not a human checkpoint" warning only if verbatim in the fetched text. Single-sourced to vendor docs --- say "per Anthropic's documentation". |
| W12 | 2026-09-03 | `ant apply`: agents, skills, environments, deployments as code with a lockfile | Ch05 §5.8 Authoring Guidelines (chapters/05-skill-systems.md:119-131) with one sentence tying to §5.10 | R2 C4 | The lockfile pins a GitHub-sourced skill to a resolved commit until `--upgrade` --- a shippable mitigation for the TOCTOU pattern §5.10 tracks; say "mitigation", not "solution". Single-sourced to vendor docs. |
| W13 | 2026-07-24 (backfill) | Anthropic, "The new rules of context engineering for Claude 5 generation models" | Ch03 §3.4 Five Dominant Patterns (or adjacent) | R3 B1 | First-party revision of context-engineering guidance for a new model generation: 80%+ system-prompt cut with no measured coding-eval loss (VENDOR-CLAIM, internal case study), rules -> judgment, just-in-time loading, brief agents like a person. |
| W14 | 2026-08-31 | Working memory is heterogeneous, not fungible tokens (arXiv 2608.31057) | Ch03 §3.4 (compaction policy) --- one compact paragraph | R3 C2 | Design rule: do not apply one compaction policy across instruction / artifact / tool-output / agent-state objects. n=55 trajectories; frame as an open empirical finding. |
| W15 | 2026-07-09 / 07-14 (v2 2026-08-27) (backfill) | TTHE (test-time harness evolution, arXiv 2607.08124) and "Rethinking the Evaluation of Harness Evolution for Agents" (arXiv 2607.12227) | Ch04 §4.5 Meta-Harness / §4.8 stress-testing thread | R1 B4 (+ G1 T4) | Present as two sides of the emerging harness-evolution debate; assert a direct citation ONLY if G1 T4 confirms it, otherwise "a methodology critique of the harness-evolution literature" without claiming it names TTHE. Key point of the critique: match search budgets before crediting harness design; overfitting risk when searching and evaluating on the same benchmark. |
| W16 | 2026-09-05 (+ 2026-08-21) | Ollama as a backend for the vendors' own desktop apps: ChatGPT Desktop (v0.34.0) and Claude Desktop (v0.33.0) | Ch12 Pattern 1 "Ollama as Universal Backend" (chapters/12-local-models.md:91-101) | R4 C2 | Inverse of the existing pattern: closed-model vendors' first-party consumer apps now route to a local open-weight backend. Both dates from GitHub release pages. |
| W17 | 2026-08-28 | Tencent Hy4 preview (770B/49B-active open-weight MoE; self-optimizing training claim) | Ch09 Hy3 follow-up (chapters/09-china-ecosystem.md:85-87) | R4 C3 | One or two sentences. Blind-eval scores, 31.8% throughput, and the self-optimization claim are all Tencent's own --- same treatment Ch09 gives DeepSeek's mHC (chapters/09-china-ecosystem.md:51). |
| W18 | reported 2026-08-24 | ByteDance folds TRAE + Coze into Doubao ("Doubao Work") | Ch09 Coze Studio entry / Section C (chapters/09-china-ecosystem.md:31-33) | R4 C4 | Reorg reported by 36kr Aug 24; Doubao Work launch date unpinned (PIN-DATE) --- write "reported", no launch date. |
| W19 | reported 2026-09-04 | DeepSeek reportedly plans 160,000 Huawei Ascend 950DT accelerators for a ~1GW Inner Mongolia site | Ch09 sovereign-silicon thesis (chapters/09-china-ecosystem.md:57-63) | R4 C5 | SECONDARY-ONLY, anonymous-sourced Bloomberg exclusive, unconfirmed by DeepSeek or Huawei. One sentence, explicitly hedged ("Bloomberg reported, citing people familiar; neither company has confirmed"); inference-only use and Huawei supply constraints stay in. |
| W20 | 2026-05-12 (backfill; brief said ~May 1 --- arXiv date wins) | Qwen-Scope: open SAE toolkit for the Qwen family (arXiv 2605.11887) | Ch09 new short entry (interpretability) | R4 B5 | 14 SAE groups across 7 Qwen3/Qwen3.5 variants, 33M+ features, steering / data classification / post-training uses. X announcement UNFETCHED (402) --- cite arXiv only. |
| W21 | 2026-09-15 | DeepSeek Harness star/fork refresh | chapters/09-china-ecosystem.md:67 and chapters/11-timeline.md:386 (and README bullet if it carries the number) | R4 C8 | Update to 224,004 stars / 26,637 forks (GitHub API, checked September 15, 2026); keep the Aug 24 figure as the "11 days in" data point if the sentence structure needs it. |
| W22 | see W10 | Codex governed delegation modes (June 2026 primitive; Sept hardening) and `headcount` (community org graph, ~Aug 30-31) | Ch14 only, inside the gate write-up | R1 C3, R1 C4 (+ G1 T2, T3) | Handled by the Ch14 drafter after the verdict. |

## C. REJECTED this wave (recorded so the next wave does not re-litigate)

Claude Fable 5.1 / Mythos 5.1 GA (Sep 1; version bump, no new primitive) --- MCP Python SDK 2.2.0 (implements already-covered spec) --- DeepSeek V4.1-Flash (version bump on primary evidence; WATCH for a DeepSeek primary on the "Engram parameters" claim) --- Temporal memory poisoning, IEEE Access (primary unfetchable, Web3-agent scope) --- Meta Muse Spark 1.3, Gemini 3.8 Flash, Microsoft Agent Framework 1.18, Google ADK 2.6 telemetry, Claude Code Sept changelog items, Moonshot ARR, Recuris (arXiv 2608.24876, implementation of an existing Ch06 pattern), RAG-IDS, agentic GraphRAG for academic QA, MemOS v2.0.34, Notion memory marketing, Cognee 1.0 (June 26 --- possible future backfill), Apple Foundation Models docs refresh, Qualcomm Snapdragon Summit (Sep 22, next wave), China agent regulation effective Jul 15 (possible future backfill), MiniMax M3 / Baidu ERNIE X1.1 (dates unresolved), Anthropic memory tool betas (2025).

## D. Standing notes
- translations/ stale by policy (English first; Ch13/14 synced Aug 24; nothing this wave). diagrams/ pending refresh unchanged.
- Glossary: no term is mandatory this wave. Drafters may PROPOSE at most one term each in their report (candidates: "runtime containment"? "state supersession"? "skills-as-code"?); the connective pass decides.
- Style: chapters/*.md + glossary.md ASCII dashes only (` --- ` / ` -- `); README What's-new bullets + CHANGELOG H3 body may use Unicode em-dash. Timeline entry heading `### Month DD, YYYY --- Title`, inserted chronologically BEFORE `## The Pattern`, matching source line under `## Sources`. Vendor claims attributed. Quotes verbatim-only. No internal markers (VENDOR-CLAIM / PIN-DATE / SECONDARY-ONLY / W#) may appear in shipped text.


---

# Part 2 --- Researcher sections for selected items (verbatim from the lane reports)


## R2 C1

### C1. CrowdStrike Ships Falcon Guardian, the First Shipped Runtime-Detection Product for Agent Skills/Agents (Ch05) --- 2026-09-01

What happened:
- CrowdStrike launched **Falcon Guardian** (part of a new **AI Detection and Response / AIDR** product line) at its Fal.Con 2026 conference, announced 2026-09-01.
- It discovers and inventories known and shadow AI agents running on Windows and macOS endpoints (who deployed them, security status), then applies access controls, policy enforcement, and **runtime detection/enforcement** to block unauthorized agent activity and reconstruct malicious execution chains.
- Explicit positioning: watches what an agent *does* at runtime, including cases "where a prompt appeared legitimate but the resulting behavior is anomalous" --- i.e., detection moved from install-time/publish-time scanning to execution-time behavior.
- CrowdStrike also announced managed security/threat-hunting services for organizations that can't run this in-house.
- Numbers: none independently verified in the two sources fetched (mostly capability description, no install-base or detection-rate figures given).

Primary: https://www.crowdstrike.com/en-us/press-releases/crowdstrike-unveils-falcon-guardian-ai-agent-security/
Secondary: https://siliconangle.com/2026/09/01/crowdstrike-launches-falcon-guardian-to-police-ai-agents-at-the-endpoint/ ; https://biztechmagazine.com/article/2026/09/crowdstrike-falcon-2026-crowdstrike-announces-falcon-guardian-and-safe-mind-aidr ; https://www.scworld.com/brief/crowdstrike-unveils-falcon-guardian-to-secure-ai-agents

Inclusion test: Section 5.10 (chapters/05-skill-systems.md:151-163) closes with the exact framework lesson this event answers: "trust has to move from *publish-time scanning* to *runtime containment* ... the defensible position is to watch what it does when it runs." Falcon Guardian is a major security vendor's first commercial, shipped, general-market product built on precisely that thesis --- not a research paper or a disclosure, a product. This is the "first shipped runtime-detection product" beat the editor flagged as high-value if found.

Recommendation: TIMELINE+CHAPTER --- extends 5.10's closing thesis from "lesson learned" to "lesson operationalized as a shipped product"; one-sentence addition to the arc.
Dedup: absent (no hits for "CrowdStrike" or "Falcon Guardian" anywhere in chapters/, glossary.md, README.md, CHANGELOG.md).
Flags: none of the standard flags apply cleanly; note detection-rate/efficacy numbers are vendor claims not yet independently benchmarked (VENDOR-CLAIM on any future efficacy number, not on the fact of the launch itself).


## R2 C2

### C2. AIR Security Emerges From Stealth With $50M, Reports 17,800+ Unverified-Source AI Add-ons and Brand-Impersonating Skills (Ch05) --- 2026-09-01/09-03

What happened:
- **AIR** (the same firm behind the June 22, 2026 "26,000 hijacked agents" disclosure already in Chapter 5 / Chapter 11) came out of stealth with **$50M** in seed funding across two rounds ($10M led by Sequoia, $40M led by Greenoaks; other investors include Wiz co-founder Yinon Costica and Cognition president Zach Frankel).
- New research disclosed alongside the raise: **more than 17,800 public AI add-ons/skills, representing roughly 6.7 million installations, rely on untrusted external instruction sources** (i.e., the exact TOCTOU-enabling pattern from the June disclosure, now measured at ecosystem scale).
- AIR also reports finding AI Skills **impersonating Anthropic and OpenAI** to bypass platform security reviews and execute arbitrary code --- a second brand-impersonation data point after the Paperclip campaign's impersonation of paperclipai/browser-use (already covered, Aug 6).
- AIR positions its product as evaluating skills, plugins, and MCP servers for malicious instructions, excessive permissions, and supply-chain risk (it also now touches Ch07's MCP-server trust surface, not just Ch05 skills).
- TechCrunch (2026-09-01) and SecurityWeek (2026-09-03, 8:00am ET) both cover the same announcement with a 2-day date spread --- read as embargo/publish-lag, not two events.

Primary: https://www.securityweek.com/ai-agent-firewall-startup-air-security-emerges-from-stealth-with-50-million/ (2026-09-03) ; https://techcrunch.com/2026/09/01/air-raises-50m-to-help-companies-vet-the-skills-and-add-ons-ai-agents-use/ (2026-09-01, reports AIR "filters out about 27%" of add-ons/skills it scans, 20+ customers, ~40 employees)
Secondary: https://www.bankinfosecurity.com/air-launches-50m-to-keep-enterprise-ai-agents-safe-a-32733 ; https://dealroom.co/news/148163-air-raises-50m-seed-to-build-a-firewall-for-ai-agents/

Inclusion test: this is a **material follow-up** to an already-covered event per the brief's instruction (AIR's June 22 disclosure is in chapters/11-timeline.md:359 and chapters/05-skill-systems.md sources). It converts the single-incident finding (26,000 agents hijacked by one fake skill) into an ecosystem-wide measurement (17,800+ add-ons / 6.7M installs on unverified sources) and adds a second brand-impersonation vector (Anthropic/OpenAI-impersonating skills) alongside the already-covered Paperclip/browser-use impersonation --- validating that brand impersonation is a recurring pattern in the arc, not a one-off.
Recommendation: TIMELINE+CHAPTER --- one addition to the Section 5.10 arc as a fourth beat/coda: the June disclosure's author now has funding, a product, and ecosystem-scale numbers.
Dedup: AIR's June 22 disclosure is present (chapters/05-skill-systems.md:185, chapters/11-timeline.md:359); this September follow-up is absent.
Flags: VENDOR-CLAIM on 17,800/6.7M and 27% filtration (AIR's own measurement methodology not published in either source fetched); PIN-DATE resolved (09-01 TechCrunch vs 09-03 SecurityWeek, use 09-01 as the announcement date, both cited).


## R2 C5

### C5. Salesforce Ships a "Long-Horizon Runtime" for Agentforce: Agents That Pursue Goals Over Weeks (Ch08) --- 2026-09-11

What happened:
- Salesforce announced a portfolio of seven named, job-specific Agentforce agents (2026-09-11): Casey, Paige, Carter, Hunter, Marshall, Piper, Fin, each scoped to a business function (sales, service, commerce, IT/HR, supply chain, customer experience). Six are GA now; **Hunter** (outbound sales) is in pilot with GA planned November 2026.
- The substantive primitive: Salesforce built a new **long-horizon runtime** for Agentforce that lets an agent "pursue goals across days and weeks instead of completing only a task or interaction." Hunter is the first agent on it; Salesforce states more agents will move onto it over time, and customers can build their own long-horizon agents on Agentforce.
- Three named components: **memory** (retains context between sessions), **durable execution** (keeps plans running across sessions), and **dynamic steering** (adjusts behavior mid-run from user instructions).
- Also announced same wave: Multi-Agent Orchestration reaching GA, "AI Skills in Coworker" (pilot, GA October), Agent Optimizer (GA October) --- these read as incremental/GA-timeline items, not new primitives on their own.

Primary: https://www.salesforce.com/uk/news/stories/agentforce-job-ready-ai-agents/
Secondary: https://www.unite.ai/salesforce-debuts-job-ready-agentforce-agents-and-long-horizon-runtime/ ; https://ppc.land/salesforce-agents-gain-a-runtime-that-pursues-goals-over-weeks-not-chats/ ; https://siliconangle.com/2026/09/11/salesforce-introduces-new-ai-agents-to-automate-sales-support-tasks/

Inclusion test: this is squarely the brief's "Notion/Slack/Salesforce/Atlassian agent APIs" scope, and it clears the bar the brief set by example (Microsoft Agent Framework Harness GA was excluded as a billing/stability milestone). The long-horizon runtime is not a GA/pricing milestone --- it's a named new execution primitive (multi-week durable goal pursuit, explicitly contrasted with single-session/single-task execution) shipped in a production, revenue-generating platform, which is a genuinely new economic/architectural point: most of Chapter 4's "long-running agent" coverage so far is infrastructure capability (AWS Runtime Instances' 14-day sessions, Aug 6, already covered) rather than an agent actually *executing a goal* across that horizon. This is the demand-side complement to that supply-side infrastructure story.
Recommendation: TIMELINE+CHAPTER (Ch08; strong cross-reference to Ch04's Aug 6 AWS Runtime Instances entry, chapters/11-timeline.md, as the "infra now exists, here's a product actually using it for weeks-long goals" pairing).
Dedup: absent ("Salesforce", "Agentforce" --- zero hits anywhere in the clone; Ch08 currently has no coverage of any enterprise agent-platform vendor beyond Notion/Slack/Figma mentions in Ch07).
Flags: VENDOR-CLAIM on "pursues goals across days and weeks" (no independent benchmark of Hunter's actual multi-week task completion found; Hunter itself is still in pilot, GA not until November).
Note for editor: chapters/08-tools-landscape.md's current scope is entirely PKM/knowledge-management tools (Notion AI, Obsidian, Mem, Heptabase, Capacities, Tana) plus a closing "AI Velocity Paradox" essay --- it does NOT currently cover production agent frameworks/platforms (LangChain, CrewAI, Salesforce, etc.) despite the brief's framing of "Ch08 tools landscape (production frameworks)." This candidate and the brief's other Ch08 targets (LangChain, Google ADK, etc.) would be the first entries of that kind in the chapter as currently written --- flagging as an open question in Section D since it may signal the editor wants to expand Ch08's scope, or route enterprise-agent-platform items elsewhere (Ch04).


## R1 C1

### C1. GPT-6 Astra Becomes First Model to Cross "Critical" Cybersecurity Threshold (Ch04, Ch11) --- 2026-09-03
- What happened: OpenAI shipped **GPT-6 Astra** September 3-4, 2026 (staged rollout: Trusted Access Program orgs first, then ChatGPT Work/Codex Pro/Business/Enterprise, then Plus/Business, plus API/Azure/AWS Bedrock). Pricing: $10/$50 per million input/output tokens ($1 cached input, $12.50 cache writes), 1,050,000-token context, 128K max output, knowledge cutoff April 30, 2026. It is **OpenAI's first model to reach the "Critical" capability tier for cybersecurity** under the Preparedness Framework --- the highest tier, which "no prior model reached" (per CSOOnline, corroborating OpenAI's own safety materials). Tested without production safeguards, Astra scored 100% on ExploitBench (up from 78.5% for GPT-5.6 Sol) and 42.4% on ExploitGym; during pre-release testing it found and chained two previously unknown zero-days, which OpenAI disclosed to the affected maintainers. This triggers real deployment restrictions: enterprise access is off by default and admins must manually enable it; the public model refuses proof-of-concept exploit generation; OpenAI is building a vetted-defender exception path (Daybreak program). A security analyst (cited by CSOOnline) also flagged **decreased chain-of-thought monitorability** relative to predecessors --- directly extending the interpretability/CoT-monitoring thread Chapter 4 already tracks (METR's raw-CoT catch of GPT-5.6 Sol, Anthropic's J-space).
- Primary: https://openai.com/index/gpt-6-astra/ (direct fetch blocked, HTTP 403 from this tool; content verified via OpenAI's own community forum repost at https://community.openai.com/t/introducing-gpt-6-astra-the-most-intelligent-and-aligned-model-in-the-world/1394703, which quotes the release text verbatim) ; https://openai.com/index/safety-overview-gpt-6-astra/ (also 403'd directly) ; https://openai.com/index/path-to-astra/ (not fetched, listed by OpenAI as a companion doc)
- Secondary: https://www.cnbc.com/2026/09/03/open-ai-astra-gpt-6-cyber.html ; https://www.csoonline.com/article/4218679/openai-launches-gpt-6-astra-its-first-model-to-cross-a-critical-cybersecurity-threshold.html (2026-09-04) ; https://thehackernews.com/2026/09/gpt-6-astra-scores-100-on-exploitbench.html
- Inclusion test: passes the model-release bar as a **first-of-a-kind capability/threshold** (not a version bump extending prior scores) --- crossing a regulatory-style Preparedness Framework tier that did not exist as a crossed line before is closer to DeepSeek R1's "new economic point" class than to a Claude-3.7-style increment, because it changes what deployment governance has to do (opt-in-only enterprise rollout, refusal contract, disclosure obligations). It extends Chapter 4's interpretability/test-time-compute cross-cutting section (CoT-monitorability regression, paralleling the METR/J-space material at chapters/04-harness-engineering.md:59) and belongs in Ch11 timeline as a frontier-model safety-threshold event.
- Recommendation: **TIMELINE + CHAPTER** (Ch11 entry; short addition to Ch04 §"feature-level sensor class" noting the CoT-monitorability regression as a counter-data-point to J-space's optimism).
- Dedup: absent (grep for "GPT-6", "Astra" in chapters/, glossary.md, README.md, CHANGELOG.md --- zero hits).
- Flags: VENDOR-CLAIM (ExploitBench/ExploitGym numbers, zero-day count are OpenAI's own disclosure); PIN-DATE confirmed (Sept 3 rollout start, Sept 4 CSOOnline coverage).


## R3 C1

### C1. StateMemBench / StateMem — a new failure axis for agent memory (Ch06) --- 2026-08-20
- **What happened:** UIUC researchers (Xinyi Fan, Miri Liu, Ruozhen Yang, Siru Ouyang, Jiawei Han) release StateMemBench, a 234-scenario multi-session benchmark testing whether agent memory returns *current* facts or *superseded* ones after facts/constraints/decisions are revised across a long interaction, using closed-pool grading to isolate state-tracking failures from other error types. They also ship StateMem, a state-first memory method tracking supersession and relational dependencies explicitly.
- Numbers: StateMem lifts current-state accuracy 1.8x on DeepSeek-V4-Flash (0.205→0.363) and 1.6x on Qwen-3.5-9B (0.149→0.233) versus leading memory systems; as a wrapper on six existing backends it adds +32 to +67 points, of which +15 to +32 points survive after controlling for the extra context tokens added (i.e. not just "more context helps").
- Primary: https://arxiv.org/abs/2608.19652 (also https://arxiv.org/pdf/2608.19652)
- Secondary: none independently fetched (arXiv abstract page is itself the primary/only source checked)
- Inclusion test: PASSES. Chapter 6's "Mid-2026: Evaluation Grows Governance Axes" section (chapters/06-agent-memory.md:111-125) already documents GateMem (access-control axis, null result) and MemSyco-Bench (sycophancy axis). StateMemBench adds a third, previously untracked axis — *recency/supersession* — and unlike GateMem's null result, pairs the benchmark with a concrete fix that other systems can wrap. This directly extends that section's "portfolio of sub-problems with different frontrunners" thread with a new sub-problem plus a working answer to it.
- Recommendation: **TIMELINE+CHAPTER** — Ch06 "Evaluation Grows Governance Axes" section, and Ch11 timeline.
- Dedup: absent (grep confirmed zero hits for "StateMem" in chapters/, glossary.md, README.md, CHANGELOG.md)
- Flags: none (numbers are the paper's own reported results, not third-party verified — treat as VENDOR-CLAIM-equivalent for an academic paper, i.e. unreplicated)


## R3 C3

### C3. Knowledge graphs survive model upgrades; compressed notes don't (Ch06 + Ch02) --- 2026-09-04
- **What happened:** Ankit Goyal and Jaideep Ray run a controlled study asking whether an agent's stored memory keeps working after the underlying model is swapped. Across 48 synthetic test cases and four memory storage approaches (raw history, RAG, compressed notes, structured knowledge graphs), they find structured/fixed-schema memory (knowledge graphs) is near-invariant to model swaps (accuracy changes by +0.0004 ± 0.0020), while compressed notes are highly model-dependent (accuracy swings +9.91 or −13.28 percentage points depending on direction of the swap). RAG with only partial re-embedding recovers 4.96 points versus 11.90 points for full re-embedding. They attribute ~80% of note-based degradation to information lost at initial memory-construction time, not at read time, and find that store-only repair fails to reach 90% recovery in all 48 cases, while retaining the raw source history alongside the compressed memory enables successful repair in 34/48 cases.
- Primary: https://arxiv.org/abs/2609.05339
- Secondary: none independently fetched
- Inclusion test: PASSES. This is exactly the shape of contribution the brief flags as the bar-clearing precedent (the Aug 2 KV-cache paper "turned a compaction thread into a concrete design rule"). Here the design rule is new and concrete: *if your memory must survive a model migration, prefer graph-structured storage over compressed-note storage, and always retain the raw source alongside any compressed form.* This lands squarely on Ch06's "where does memory live" thread (chapters/06-agent-memory.md:109, the six-level memory-locus discussion) and also strengthens Ch02's claim that knowledge graphs are becoming "a structured index layer" (chapters/02-knowledge-layer.md:101) by giving that claim an empirical portability argument it didn't have before. Small synthetic n (48 cases, 2 authors) — flag accordingly — but the finding is concrete and actionable, not just descriptive.
- Recommendation: **TIMELINE+CHAPTER** — Ch06 (primary) with a cross-reference from Ch02's GraphRAG-as-index-layer section.
- Dedup: absent
- Flags: PIN-DATE confirmed (2026-09-04 per arXiv submission date); small-n academic study, not independently replicated — flag as such if used


## R4 C1

### C1. Anthropic September 2026 Threat Intelligence Report — Chinese labs named in "industrial-scale" distillation campaign (Ch09) --- 2026-09-10
- What happened: Anthropic published "Detecting and countering misuse of AI: September 2026," covering misuse disrupted December 2025–August 2026 across seven harm areas, one of which is "distillation." Per secondary reporting citing the report, Anthropic accuses Moonshot AI of silently routing some Kimi customer requests to Claude (mostly Opus) through a network of 5,380 accounts flagged as fraudulent (mostly appearing in Singapore/Japan), relaying almost 300,000 requests in a ~10-day cluster, then serving Claude's answers back as Kimi's and using the exchanges to train Moonshot's own models. Anthropic separately attributes 23M+ Claude exchanges to Moonshot between May–July 2026, and names Alibaba, DeepSeek, Z.ai (Zhipu), Xiaomi, and MiniMax elsewhere in the distillation section. DeepSeek is described using a similar "cross-session replay" technique to extract Claude Opus reasoning traces.
- Primary: https://www.anthropic.com/threat-intelligence-report-september-2026 (fetched; confirms title "Detecting and countering misuse of AI: September 2026" and the report structure/table of contents including an "Illicit distillation" section; full distillation-section text did not return in the fetch — see Flags). A duplicate/alt URL surfaced in search (https://www.anthropic.com/news/detecting-countering-misuse-ai-sept-2026) returned 404 — the working primary URL is the one above.
Secondary: https://www.cnbc.com/2026/09/11/chinese-ai-labs-moonshot-deepseek-alibaba-anthropic.html ; https://dealroom.co/news/150366-anthropic-alleges-moonshot-routed-some-kimi-user-requests-to-claude-then/ ; https://technode.global/2026/09/11/anthropic-ai-orchestrated-cyberattacks-model-distillation/
- Inclusion test: Ch09's "Open-Source as Strategic Imperative" section (chapters/09-china-ecosystem.md:115-119) frames Chinese open-weight strategy as ecosystem lock-in / talent / goodwill; this event is the adversarial counter-narrative the chapter is currently missing — a Western frontier lab publicly alleging systematic, cross-lab distillation-via-proxy-routing against nearly every major Chinese open-weight vendor the chapter already names (Moonshot, DeepSeek, Alibaba, Zhipu, MiniMax). It operationalizes "distillation" as a named, evidenced adversarial-dynamics beat between the two ecosystems this chapter compares, not just a technical footnote.
- Recommendation: TIMELINE+CHAPTER — extends Ch09 Section C (chapters/09-china-ecosystem.md:107-119) with a new subsection on the distillation dispute; also cross-references Ch06 (agent memory / distillation techniques) if the editor wants a pointer.
- Dedup: absent (grep for "threat-intelligence", "distillation" in chapters/09 and chapters/11 — no hits for this event; TencentDB's own use of "distillation" at chapters/06-agent-memory.md:125 is an unrelated technical term).
- Flags: the specific numeric claims (5,380 accounts, ~300K requests, 23M exchanges) are Anthropic's own investigative claims (VENDOR-CLAIM, effectively — this is Anthropic making an allegation against a competitor, not an independently adjudicated fact) and are drawn from secondary summaries because the full report text did not return through WebFetch (SECONDARY-ONLY for the specific numbers; primary URL and top-level framing are fetched/confirmed).


## R4 B6

### B6. OpenRouter: Chinese models sweep top-5 weekly token usage for the first time --- reported 2026-07-29
- What happened: Chinese-developed models took all five top spots in OpenRouter's global weekly token-usage ranking for the first time: Xiaomi's MiMo-V2.5 (#1), followed by models from DeepSeek, MiniMax, Alibaba's Qwen family, and Moonshot's Kimi. OpenRouter was processing >20 trillion tokens/week at the time, with Chinese-origin models cited as >60% of routed traffic in some contemporaneous analyses.
- Primary: I was unable to retrieve an OpenRouter-published historical data page or announcement pinned to 2026-07-29 (OpenRouter's rankings page is a live, rolling view — https://openrouter.ai/rankings — which I fetched and confirmed shows current, not historical, data; web.archive.org is not fetchable from this environment, so no archived snapshot could be retrieved either). This candidate is therefore SECONDARY-ONLY as researched.
Secondary: Dataconomy, "Chinese LLMs Take Top Five Spots On OpenRouter" (2026-07-29): https://dataconomy.com/2026/07/29/chinese-ai-models-openrouter-top-five/ ; TechBriefly, "Chinese AI models lead OpenRouter for first time" (2026-07-29): https://techbriefly.com/2026/07/29/chinese-ai-models-lead-openrouter-for-first-time/
- Inclusion test: This is exactly the kind of "narrative shift" market event CONTRIBUTING.md's Market Events section calls IN (a structural shift in the global inference-traffic story, not a funding/valuation headline) — and it's a strong strengthener for Ch09's "Open-Source as Strategic Imperative" section (chapters/09-china-ecosystem.md:115-119), giving that thesis a concrete usage-share data point it currently lacks.
- Recommendation: IN — TIMELINE+CHAPTER, merged with C6 above into one arc (July sweep → September continuation/growth).
- Dedup: absent.
- Flags: SECONDARY-ONLY (no OpenRouter-published historical primary retrievable within tool constraints — flagging for the fact-checker to try OpenRouter's API or a paid archive tool if a harder primary is required).


## R4 C6

### C6. Chinese-origin models extend OpenRouter dominance to 46.4% of routed tokens; Tencent Hy4 +379% weekly surge (Ch09) --- week of 2026-08-31 to 2026-09-06
- What happened: Following the July 29 all-Chinese top-5 sweep (see B6), Chinese-origin labs (DeepSeek, Xiaomi, MiniMax, Tencent, Qwen) reportedly reached 46.4% of OpenRouter's >20T weekly routed tokens by early September, vs. 35.7% for US-origin models. For the week of Aug 31–Sep 6, Tencent's newly-released Hy4 (see C3) posted a 379% week-over-week token-usage surge on OpenRouter. A snapshot cited "as of September 1, 2026" lists the top 5 by weekly usage as DeepSeek V4 Flash 0731 (12.1T tokens), GLM-5.3 Flash (10T), GPT-5.6 Luna (9.52T), Xiaomi MiMo-V2.5 (7.2T), Tencent Hy3 (5.89T) — i.e. four of five still Chinese-origin even where a US model (Luna) breaks in.
- Primary: https://openrouter.ai/rankings (fetched directly; confirms the page is live, methodology is "tokens processed... counting both prompt and completion tokens," and data shown was "through Sep 13, 2026" at fetch time — but the specific historical weekly figures above could not be extracted from the live page and come from secondary sources below).
Secondary: https://finance.yahoo.com/technology/ai/articles/chinese-ai-models-now-capture-020440715.html ; https://pro.stockalarm.io/blog/openrouter-llm-rankings-investor-analysis ; https://www.kucoin.com/news/flash/chinese-models-dominate-openrouter-weekly-token-usage-ranking
- Inclusion test: Strengthens/extends B6 (below) within the current window — shows the July all-Chinese sweep was not a one-off blip but a continuing and growing share (46.4% vs. the >60% headline from the July sweep — note these two percentages use different denominators/framings across sources and should not be treated as directly comparable without checking each report's methodology).
- Recommendation: TIMELINE+CHAPTER as a joint entry with B6 — one narrative arc ("Chinese open-weight models take over OpenRouter, July→September 2026") rather than two separate timeline points.
- Dedup: absent.
- Flags: SECONDARY-ONLY for the specific percentages/rankings (live OpenRouter page fetched but did not yield the historical numbers directly); PIN-DATE caveat that "46.4%" and "60%+" come from different secondary analyses that may define "Chinese-origin" or the token universe differently — flagging for the fact-checker to reconcile methodologies before quoting both numbers together.


## R3 B3c

### B3c. Filesystem-Based Memory for LLM Agents: Organization, Evolution, and Sustainability --- 2026-07-29
- **What happened:** Sizhe Zhou and ten coauthors (UIUC, UCSD, Adobe Research) run what they describe as the first systematic study of filesystem-based agent memory — a directory tree of markdown files the agent itself reads/writes/reorganizes via generic file tools (the pattern Claude Code's own Auto Memory / MEMORY.md and ByteRover already use in production, per vendor docs, though the paper studies the pattern generically rather than any one vendor's implementation). They formalize three roles around one shared memory filesystem — a management agent that organizes incoming content, a search agent that answers queries with cited sources, and an execution agent that distills task trajectories into skills — and test whether an agent can keep a growing filesystem-memory store organized as it accumulates, conflicts, and goes stale. Headline finding: organized stores roughly halve retrieval cost when the memory store is large.
- Primary: https://arxiv.org/abs/2607.26637
- Secondary: https://huggingface.co/papers/2607.26637
- Inclusion test: PASSES for backfill. Ch06 already names ByteRover's "hierarchical markdown trees" (chapters/06-agent-memory.md, Major Frameworks / ByteRover subsection) as a shipped pattern but has never had academic validation of whether/why filesystem-as-memory actually scales. This paper is the first academic study that formalizes and quantifies that exact pattern (organization pays off, roughly 2x retrieval-cost reduction at scale) — a genuine "validates a primitive the framework tracks" case, and separately of direct relevance to anyone using Claude Code's own MEMORY.md-based Auto Memory, which follows the same filesystem-memory pattern.
- Recommendation: **TIMELINE+CHAPTER** — Ch06 ByteRover/architectural-patterns section.
- Dedup: absent
- Flags: none beyond standard unreplicated-academic-study caveat


## R3 B3b

### B3b. MemTxn: a transaction boundary for agent memory updates --- 2026-07-30
- **What happened:** Hanshuai Cui and five co-authors propose MemTxn, a governance layer sitting outside the answer model that (1) verifies whether a proposed memory update is actually supported by its cited source via "Ordered PatchTest," (2) picks the visible version when facts conflict via a "Temporal Resolver," and (3) restores application-visible state after a fault using a durable snapshot journal — without needing to know the actual physical write set. On their own test suite, it accepts all 60 source-supported update originals and rejects all 179 constructed hard-negative (unsupported) updates; under injected persistent multi-key faults on LongMemEval-S and LoCoMo-derived states, it fully restores the declared active memory map.
- Primary: https://arxiv.org/abs/2607.27834
- Secondary: a closely related/possibly earlier paper by an overlapping problem space, "MemTX: Transactional Belief Commit for Stateful Agent Memory" (arXiv 2607.23929, July 26 2026) was surfaced in search — worth the editor checking whether MemTxn and MemTX are the same team iterating or two independent transactional-memory proposals; I did not fetch 2607.23929's full text to compare authorship.
- Inclusion test: PASSES for backfill. This is a concrete, mechanism-level answer to a problem Ch06 already names as unsolved: GateMem's null result is about access control and forgetting, not update-integrity/rollback, and none of Ch06's frameworks (Mem0ᵍ's Conflict Detector/Update Resolver is the closest analog) offer a fault-recovery/rollback guarantee. MemTxn's contribution — a transaction boundary specifically for memory writes, with 100%/100% accept/reject on its validation set — is exactly the kind of "operationalizes a primitive the framework tracks" case the inclusion test wants: it turns "memory conflicts get resolved somehow" (Mem0ᵍ's informal Update Resolver) into a formal, testable transactional guarantee.
- Recommendation: **TIMELINE+CHAPTER** — Ch06, cross-referenced against Mem0ᵍ's Conflict Detector/Update Resolver (chapters/06-agent-memory.md:39) and GateMem's governance-null-result thread.
- Dedup: absent
- Flags: small validation set (60 positive / 179 negative cases, single paper, unreplicated) — note as such, not framed as production-proven


## R3 B3a

### B3a. Memory Decoder at Scale: A Pretrained, Parametric Long-Term Memory --- 2026-07-30
- **What happened:** Rubin Wei et al. (incl. Qipeng Guo, Bowen Zhou, Zhouhan Lin) scale a parametric long-term memory module (Memory Decoder) up to 6.9B parameters pretrained on 300B tokens, arguing decoder-only LLMs entangle memory and reasoning in one parameter set and that scaling memory separately is a better parameter-performance tradeoff than scaling the base model. They build a distributed Faiss indexing/retrieval pipeline with sparse batch-wise kNN loading to make this tractable at scale. On 17 benchmarks, pairing their 6.9B memory module with a 410M-parameter Pythia base raises its average score from 29.86 to 37.34 — surpassing Pythia-12B (37.24) while using 39% fewer total parameters.
- Primary: https://arxiv.org/abs/2607.27919
- Secondary: https://huggingface.co/papers/2607.27919 ; prior smaller-scale version at https://arxiv.org/abs/2508.09874 (the original, non-scaled Memory Decoder paper, for context on what "at scale" extends)
- Inclusion test: PASSES for backfill. Directly extends Ch06's "Trainable Memory Modules" thread (Titans/MIRAS, chapters/06-agent-memory.md:83) and the Metis parametric-memory line (chapters/06-agent-memory.md:129-133) with a third, independently-scaled parametric-memory result and a concrete number: a much smaller base model + large external memory module beats a much larger monolithic model at lower total parameter count. This is a genuine empirical data point for the "when is memory worth burning into weights" design question Ch06 already poses but has not yet answered with a param-efficiency number.
- Recommendation: **CHAPTER-ONLY** (Ch06, Trainable Memory Modules subsection) — it's an incremental scaling result on an existing line (Memory Decoder, arXiv 2508.09874, already existed pre-2026), not a first-of-kind primitive, so a timeline entry is a closer call than a chapter addition; editor's discretion on TIMELINE+CHAPTER vs CHAPTER-ONLY.
- Dedup: absent (neither "Memory Decoder" nor arXiv 2508.09874/2607.27919 appear in the local clone)
- Flags: none beyond standard academic-paper caveat (self-reported benchmark numbers)


## R3 B2

### B2. Google: Gemini Enterprise Agent Platform — Memory Bank reaches GA (plus Agent Runtime, Identity, Gateway/Registry) --- 2026-07-30 (brief cites July 29; blog is dated July 30, likely a timezone artifact)
- **What happened:** Google announces several Gemini Enterprise Agent Platform capabilities reaching general availability together: Agent Memory Bank (schema-defined structured extraction of conversation context for low-latency personalization, letting agents "pick up right where they left off" across long-running tasks — this is GA, distinct from the July 2025 Vertex AI Memory Bank *public preview* announcement, which is an earlier, separate milestone for the predecessor product name), Agent Runtime (continuous multi-day agents, up to 7 days), Agent Identity (a native IAM type for least-privilege agent access and token-theft mitigation), and Agent Gateway/Registry (centralized governance and discoverability).
- Primary: https://cloud.google.com/blog/products/ai-machine-learning/whats-new-in-gemini-enterprise-agent-platform
- Secondary: https://enterprisedna.co/resources/news/google-gemini-agent-platform-memory-runtime-identity-ga-2026/ ; https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/memory-bank
- Inclusion test: PASSES for backfill. This is Memory Bank's transition from preview (2025, on the old Vertex AI Agent Engine branding) to GA (2026, on the renamed Gemini Enterprise Agent Platform) — a new economic/reliability point (GA-level SLA, per-1000-events billing since Jan 28 2026) for a capability Ch06 does not currently mention by name at all (Ch06 covers Mem0/A-MEM/ByteRover/Nemori/MemPalace/Titans/Dreaming — no Google-native offering). Adds a second major-cloud-vendor agent-memory GA to sit alongside TencentDB Agent Memory v2.0 already in Ch06, i.e. it's evidence for the "cloud vendors are shipping managed memory as a category" trend Ch06 doesn't yet name explicitly.
- Recommendation: **TIMELINE+CHAPTER** despite predating the window (per brief instructions, backfill items are evaluated on their own IN/OUT merit regardless of window) — Ch06 Major Frameworks / vendor-memory section, Ch11 timeline.
- Dedup: absent — grep of chapters/06-agent-memory.md found zero mentions of "Memory Bank," "Vertex," or "Gemini Enterprise" in a memory context
- Flags: VENDOR-CLAIM (all capability descriptions are Google's own blog language; no independent benchmark of Memory Bank's schema-extraction quality was found)


## R2 C3

### C3. Anthropic Ships `auto` Permission Policy: Server-Side Per-Call Evaluation for Agent and MCP Tool Calls (Ch07, cross-ref Ch04) --- 2026-09-10

What happened:
- Anthropic's Claude Platform release notes (dated 2026-09-10) added an **`auto` permission-policy mode** to Managed Agents, alongside the existing `always_allow` / `always_ask`. Confirmed via direct fetch of the live docs page.
- Under `auto`, the **server** (not the calling client) evaluates each individual tool call --- weighing the tool, its input, and session content so far --- and returns one of three outcomes: the call **runs**, is **denied** (agent gets an error result, client cannot override), or **pauses for approval** (same flow as `always_ask`).
- This applies to both the pre-built agent toolset **and MCP toolsets** --- i.e., it is a live example of server-side authorization being applied specifically to MCP tool calls, reported via a new `evaluation` object on `agent.tool_use` / `agent.mcp_tool_use` events (`type`, nested `evaluated_permission`, `reason_code` such as `"high_risk"` or `"indeterminate"`).
- Docs explicitly warn `auto` is "not a human checkpoint" --- a call the server judges safe runs immediately and may be irreversible.
- Same release window: `ant apply` (see C4) references `auto` in its own examples, and MCP toolset policy defaults to `always_ask` unless explicitly overridden, which the docs frame as protecting against new tools silently added to a trusted MCP server.

Primary: https://platform.claude.com/docs/en/managed-agents/permission-policies (fetched directly, dated via release notes entry 2026-09-10) ; release-note pointer: https://platform.claude.com/docs/en/release-notes/overview
Secondary: none found independently reporting this (appears to be a docs-only ship, no press coverage located)

Inclusion test: Chapter 4 already tracks AWS AgentCore's **Temporal Policies** (Aug 6, 2026 --- deterministic, non-LLM, session-history-aware authorization outside agent code) as a new primitive on the "Authority axis." Anthropic's `auto` policy is a second, model-evaluated (not deterministic-policy-language) answer to the same problem --- and it is the first primitive I found that names **MCP tool calls specifically** as a governed surface at the harness/platform level, which is new ground for Chapter 7's "meta-tool pattern" / authorization discussion (chapters/07-mcp.md:62, :146). Two different vendors shipping two different mechanisms (deterministic policy language vs. model-judged runtime evaluation) for the same problem in five weeks is itself a notable convergence beat.
Recommendation: CHAPTER-ONLY (Ch07, with a cross-reference note to Ch04's Temporal Policies) --- I did not find independent press coverage, so it's a genuine capability but a quiet one; the editor may prefer to fold it into Ch04's Authority-axis discussion instead, next to AgentCore.
Dedup: absent ("permission_policy", "auto.*permission" --- zero hits anywhere in the clone).
Flags: SECONDARY-ONLY does not apply (it's primary-only, no secondary coverage found) --- flagging as **single-sourced**; recommend a fresh fetch of the dated release-notes entry itself (not just the feature page) before inclusion, since I could not get the release-notes page to isolate a single specific 2026-09-10 changelog line separate from the feature docs.


## R2 C4

### C4. Anthropic Ships `ant apply`: Infrastructure-as-Code for Agents, Skills, Environments, and Deployments (Ch05, cross-ref Ch04) --- 2026-09-03

What happened:
- Claude Platform release notes (2026-09-03) shipped `ant apply` in CLI v1.30.0+: a Terraform-style workflow that declares **agents, environments, skills, memory stores, and deployments as files in a repository**, diffs them against live API state, shows a plan, and on approval creates/updates the resources --- writing a `claude-lock.json` lockfile that fingerprints what was sent vs. what the API returned.
- Skills specifically: a skill is a directory with `SKILL.md` at its root; `ant apply` can also pull a skill directly from a **GitHub URL** (`https://github.com/<owner>/<repo>/tree/<branch>/<dir>`), pinned to a resolved commit until `--upgrade` is run --- functionally the same "mounted-repo skill trust boundary" pattern Section 5.10's neighbor topic (Managed Agents GitHub-hosted skills, Aug 7, already covered) established, now generalized into the CLI's own resource model.
- Resources reference each other by relative file path (an agent's `skills:` list, a deployment's `agent:`/`environment_id:` fields), and `ant apply` resolves dependency order and pins versions --- a genuine "agents/skills-as-code" primitive with CI support (`ant apply --yes .`, `--dry-run` for PR-time plans, Workload Identity Federation for CI auth rather than static API keys).
- Docs explicitly recommend Workload Identity Federation for CI authentication --- a second, unrelated-to-MCP data point that WIF is becoming the default recommended credential pattern for agent infrastructure broadly, not just the MCP-specific WIF (SEP-1933) still sitting as an open PR.

Primary: https://platform.claude.com/docs/en/cli-sdks-libraries/cli/apply (fetched directly)

Inclusion test: Section 5.8 (Authoring Guidelines, chapters/05-skill-systems.md:119) and 5.10 both discuss skills as artifacts but the guide has no coverage yet of **skill/agent lifecycle management as code** (GitOps-style plan/apply/lockfile) --- this is a new primitive class distinct from "how to write a skill" or "how skills get attacked." It also directly extends the supply-chain thread: a lockfile that pins a GitHub-sourced skill to a specific commit is a concrete, shippable mitigation for exactly the TOCTOU problem Section 5.10 spends its whole section on (a skill's content can no longer silently change between vetting and use if it's locked to a commit hash) --- worth flagging to the editor as a rare "fix," not just another disclosure.
Recommendation: CHAPTER-ONLY (Ch05, section 5.8 or a new subsection) --- strong candidate to also mention in Ch04 (harness-as-code / CI patterns) as a cross-reference; no independent press coverage found, single-sourced to Anthropic's own docs.
Dedup: absent ("ant apply", "claude-lock" --- zero hits).
Flags: SECONDARY-ONLY does not apply (no secondary source found at all) --- single-sourced to vendor docs, no press pickup located in three related searches.


## R3 B1

### B1. Anthropic, "The new rules of context engineering for Claude 5 generation models" --- 2026-07-24
- **What happened:** Thariq Shihipar (Anthropic) writes that the Claude Code team removed over 80% of the system prompt for Opus 5 / Fable 5-class models with no measurable coding-eval loss. The post frames six shifts: from rules to judgment (agents get principles + trust, not exhaustive instructions), progressive/just-in-time context loading over upfront stuffing, and briefing agents "like a person" — role, constraints, examples only where they matter.
- Primary: https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models
- Secondary: https://enterprisedna.co/resources/ai-pulse/ai-pulse-2026-07-26-anthropic-published-new-context-engineering-guidance-for-the/ ; https://www.developersdigest.tech/blog/claude-5-context-engineering-rules-hn-analysis
- Inclusion test: PASSES for backfill. Ch03 currently frames context engineering around a six-layer model and KV-cache-centric patterns (Manus, §3.3) written for an earlier model generation. This post is a first-party operationalization of "give judgment, not rules" and "progressive disclosure" specifically for the Claude 5 generation — a maturity marker for the discipline (a frontier lab formally revising its own guidance), and directly citable next to Ch03 §3.4's "Five Dominant Patterns."
- Recommendation: **CHAPTER-ONLY** (July 24 falls before this wave's Aug 23 window-start; too old for a new Ch11 timeline entry under this wave, but the guide has apparently not covered it yet, so it belongs as a Ch03 addition without an accompanying timeline bullet, or the editor may choose to timeline it as a dated event with the caveat that it precedes the window).
- Dedup: absent (grep found no "new rules of context engineering" or Thariq Shihipar reference in chapters/, README.md, CHANGELOG.md)
- Flags: VENDOR-CLAIM (the 80% system-prompt-cut figure and "no measurable loss" claim are Anthropic's own, framed as an internal Claude Code case study, not independently benchmarked)


## R3 C2

### C2. Working memory is heterogeneous, not fungible tokens (Ch06, crosses into Ch04 harness) --- 2026-08-31
- **What happened:** A nine-author team (Le Chen, Zishen Wan, Baixi Sun, Xiaolong Ma, Chih-Hsuan Yang, Feng Yan, Sheng Di, Franck Cappello, Rajeev Thakur) analyze 55 archived coding-agent trajectories and propose a four-category taxonomy of working-memory objects — instructions, artifacts, tool outputs, agent-generated state — arguing each has different size/retention/representation profiles and therefore needs different management policy, not one uniform token-budget rule. They propose a four-level evaluation framework (stored state, delivered context, management work, task outcome) and test two semantically-informed strategies (object-aware compression, retrieval-based policies).
- Key finding stated in their own words: "equal token budgets do not imply equal delivered context or management cost," and calibration gains from one task set "may not transfer to held-out tasks."
- Primary: https://arxiv.org/abs/2608.31057
- Secondary: none independently fetched
- Inclusion test: PARTIAL PASS. Ch03's six-layer context model (chapters/03-context-engineering.md:22-35) already separates layers by persistence but treats each layer as internally uniform for compression purposes. This paper's finding — that objects *within* a layer (e.g. all "tool outputs" inside Conversation History) need different compaction rules — is a plausible refinement of Ch03 §3.4 (Five Dominant Patterns) rather than a wholly new primitive; it's an empirical study (55 trajectories, not independently verified) rather than a shipped system. Weaker than C1 but still a genuine design-rule candidate: "don't apply one compaction policy across all object types in the window."
- Recommendation: **CHAPTER-ONLY** — Ch03 §3.4 or Ch06 architectural-patterns section, framed as an open empirical finding rather than a settled pattern (editor's call on which chapter fits better; leaning Ch06 given "coding-agent working memory" framing, but Ch03 is defensible).
- Dedup: absent
- Flags: SECONDARY-ONLY-equivalent (small n=55 trajectory sample; self-reported, no replication)


## R1 B4

### B4. TTHE (arXiv 2607.08124) and Its Rebuttal (arXiv 2607.12227) --- Ch04
- What happened: **TTHE: Test-Time Harness Evolution** (Nie, Zhang, Song, Cai, Yu, Guo, Tian, Han; submitted July 9, 2026) proposes optimizing the *harness itself* --- not model weights --- during evaluation: a population of candidate harnesses is refined by an agentic proposer reasoning over unlabeled execution traces, with a judge committing improved harnesses from execution-derived proxy signals; solver, proposer, and judge are different roles/harnesses around the same frozen LLM. **A second paper, "Rethinking the Evaluation of Harness Evolution for Agents"** (Wang, Zhu, Hu, Yuan, Chen, Senthil, Hajishirzi, Tsvetkov, Dasigi, Xiao; v1 July 14, 2026, **v2 August 27, 2026** --- the v2 date falls inside this wave's window) challenges the evaluation methodology of the harness-evolution literature broadly: it argues such methods must be benchmarked against simple task-level search baselines under matched feedback/inference budgets (to separate "better harness design" from "just more search"), and flags that searching and evaluating on the same benchmark risks overfitting. I could not confirm from the fetched abstract/page that this second paper names TTHE specifically by citation --- it reads as a general critique of the harness-evolution-via-unit-tests protocol, which TTHE's own abstract distinguishes itself from ("without gold labels or task-specific supervision"), so the "rebuttal" framing in the brief may overstate a direct TTHE-vs-critique relationship; both papers should be read as two sides of the same emerging harness-evolution debate rather than confirmed as a direct exchange.
- Primary: https://arxiv.org/abs/2607.08124 ; https://arxiv.org/abs/2607.12227
- Secondary: none fetched
- Inclusion test: TTHE is a genuinely new architectural idea for Ch04 --- moving optimization from pre-deployment harness search to test-time harness adaptation using only execution traces, no gold labels --- which is a new measurement/design axis in the harness-evolution research thread Ch04 already surveys (Meta-Harness's 6x gap, CATTS, the Advisor Tool). The critique paper is a legitimate methodological check on that whole sub-literature (matched-budget baselines, overfitting risk) and its August 27 v2 update is what makes it timely for this wave.
- Recommendation: **IN** --- CHAPTER-ONLY for both (Ch04's harness-evolution/stress-testing section), not a timeline entry for either (neither is a product ship or a benchmark milestone with a hard number the way KV-cache-compaction or CATTS were framed) unless the editor wants a short joint timeline note dated to the v2 update (Aug 27) flagging "the harness-evolution literature gets its first methodology critique."
- Dedup: absent (grep "2607.08124", "2607.12227", "TTHE" --- zero hits).
- Flags: SECONDARY-ONLY caveat on the "rebuttal" relationship (could not verify direct citation from the fetched content --- recommend the fact-check pass re-fetch the full PDF/HTML body, not just the abstract page, before the guide asserts these two papers argue with each other).


## R4 C2

### C2. Ollama v0.34.0 — ChatGPT Desktop runs local Ollama models; v0.33.0 — Claude Desktop as third-party gateway to Ollama (Ch12) --- 2026-09-05 (paired context: 2026-08-21)
- What happened: Ollama v0.34.0 (released 2026-09-05) ships ChatGPT Desktop integration: "Ollama models can now be used directly in ChatGPT Desktop, so you can keep your existing workflow while running open models," configured via the Ollama macOS app; the same release adds OpenAI-compatible client tool search, response compaction, and faster structured output on Apple Silicon. Two weeks earlier, v0.33.0 (2026-08-21, just before the window) shipped the same pattern for the other major closed-model desktop app: "Developers can now easily configure Claude Desktop to seamlessly work with Ollama as a third-party gateway provider."
- Primary: https://github.com/ollama/ollama/releases/tag/v0.34.0 ; https://github.com/ollama/ollama/releases/tag/v0.33.0 (both fetched directly, GitHub release notes)
- Inclusion test: Ch12's local-models framing (chapters/12-local-models.md:91-101, "Pattern 1: Ollama as Universal Backend") already documents Ollama's OpenAI-compatible API as the integration point for third-party tools pointed *at* Ollama. This is the inverse and new: both major closed-model vendors' own first-party desktop chat apps (Claude Desktop, ChatGPT Desktop) now natively route *to* a local Ollama backend as an alternate model provider — an OS/vendor-app-level integration pattern the chapter doesn't yet have. It operationalizes "local open-weight models as a first-class backend for vendor apps," parallel to the Apple `LanguageModel`/`MLXLanguageModel` protocol already in the chapter (chapters/12-local-models.md:120), but this time from the closed-model vendors' own consumer apps rather than an OS vendor.
- Recommendation: CHAPTER-ONLY (Pattern 1 update) or light TIMELINE entry — the primitive is a genuine first (vendor consumer app <-> local OSS backend), but it is a two-vendor infrastructure/UX convenience rather than a new model or protocol; editor's call on whether it clears the timeline bar.
- Dedup: absent — grep for "Ollama" in chapters/12 shows only the existing `ollama pull` / base_url examples (lines 40-100); no mention of Claude Desktop / ChatGPT Desktop integration anywhere in the clone.
- Flags: none (both fetched directly from GitHub release pages, dates confirmed via the releases index).


## R4 C3

### C3. Tencent Hy4 preview — 770B/49B-active open-weight MoE, self-optimizing training loop (Ch09) --- 2026-08-28
- What happened: Tencent released and open-sourced Hunyuan **Hy4 preview**: 770B total parameters, 49B active, 1M+ token context, served via Tencent Cloud TokenHub and OpenRouter (model ID `tencent/hy4-preview`, priced $0.834/M input, $2.501/M output). Tencent's internal blind evaluation (163 experts, 203 engineering tasks) scores it 2.99/4.00 vs GLM-5.3's 2.92 and Kimi K3's 2.94. Tencent states Hy4 "participated for the first time in the automated optimization of training methods, data strategies, evaluation frameworks, and low-level operators," autonomously tuning inference bottlenecks for a claimed 31.8% throughput gain.
- Primary: https://www.tencent.com/tencent-releases-and-open-sources-tencent-hy4-preview/ (fetched directly) ; https://x.com/TencentGlobal/status/2093264031343616239
Secondary: https://technode.com/2026/08/28/tencent-open-sources-hy4-preview-with-770b-parameters-and-a-1m-token-context/ ; https://www.kucoin.com/news/flash/tencent-hunyuan-releases-and-opens-source-hy4-preview-with-770b-total-parameters
- Inclusion test: Ch09 already covers Hy3's full Apache-2.0 open-sourcing (chapters/09-china-ecosystem.md:85-87) as "the last major closed Chinese frontier lab defaulting to fully unrestricted open weights." Hy4 preview is Tencent's next model on the same open-weight cadence — by the version-bump rule this is largely an extension, EXCEPT for the self-optimizing-training-loop claim (model tuning its own training/data/eval/operator pipeline), which if it holds up is a new self-improvement primitive distinct from anything currently in Ch09 or Ch13 (loop engineering).
- Recommendation: CHAPTER-ONLY — add as a brief Hy3 follow-up in Ch09, flagging the self-optimization claim as VENDOR-CLAIM/awaiting-independent-replication (same treatment Ch09 already gives DeepSeek's mHC, chapters/09-china-ecosystem.md:51). Not a strong enough standalone timeline beat on its own (version bump), but the self-optimization claim is worth a sentence.
- Dedup: absent (no "Hy4" hits anywhere in the clone).
- Flags: VENDOR-CLAIM (blind-eval scores, 31.8% throughput, self-optimization claim are all Tencent's own).


## R4 C4

### C4. ByteDance folds TRAE + Coze into Doubao, preps "Doubao Work" super-app (Ch09) --- 2026-08-24 (reorg reported); launch date unpinned
- What happened: ByteDance completed an internal team merger folding its Trae coding platform and Coze agent-building tool into the Doubao consumer chatbot's office-tools org; TRAE IDE/CLI remain standalone, but TRAE Work and Coze combine with Doubao's office features under a single forthcoming brand, "Doubao Work," aimed at competing with Tencent's WorkBuddy. Reporting (2026-08-24) says the standalone app would launch "as soon as this week"; I could not pin an exact launch date within the search budget.
- Primary: 36kr (English edition), "Exclusive ByteDance AI Productivity Integration: TRAE & Coze Merged into Doubao, Unified Office Brand 'Doubao Work' to Launch" (2026-08-24): https://eu.36kr.com/en/p/3953230805876099 (fetched directly)
Secondary: https://theedgemalaysia.com/node/815655 ; https://www.kucoin.com/news/flash/bytedance-integrates-trae-and-coze-into-doubao-launching-doubao-work ; https://aiweekly.co/node/10741
- Inclusion test: Ch09's Coze Studio entry (chapters/09-china-ecosystem.md:31-33) currently frames Coze as ByteDance's standalone open-source visual agent platform with "native advantage" via Doubao integration. This event reverses the framing: ByteDance is now folding the standalone coding (TRAE) and agent-building (Coze) tools *into* the consumer chat app itself, rather than keeping them as separate developer products — a distinctly Chinese "everything-in-the-super-app" consolidation pattern that contrasts with the Western practice of keeping IDE/agent-builder tooling separate from consumer chat products (relevant to Ch09 Section C's "visual-first vs. code-first" / tool-preferences discussion).
- Recommendation: CHAPTER-ONLY — update the Coze Studio entry / Section C discussion to note the consolidation; PIN-DATE needed for the actual "Doubao Work" launch before treating it as a timeline entry.
- Dedup: absent (existing "Doubao" mention at chapters/09-china-ecosystem.md:33 predates this; "Doubao Work" itself: no hits).
- Flags: PIN-DATE (exact Doubao Work launch date not confirmed within budget — only the 2026-08-24 reorg-reporting date is solid).


## R4 C5

### C5. DeepSeek plans 160,000 Huawei Ascend 950DT accelerators for 1GW Inner Mongolia site (Ch09) --- reported 2026-09-04/05
- What happened: Bloomberg reported (2026-09-04) that DeepSeek intends to deploy at least 160,000 Huawei Ascend 950DT accelerators at a ~1GW data center in Ulanqab, Inner Mongolia, targeting partial operation by end-2027/early-2028; the chips would run inference (serving), while DeepSeek continues training on its existing NVIDIA hardware. Huawei's own production is reportedly capacity-constrained (memory-component shortages limit 950DT output to "low hundreds of thousands" for all of 2026), so delivery could take over a year.
- Primary: none — no DeepSeek or Huawei official statement confirming the order was found; this is sourced entirely to "people familiar with the matter" via Bloomberg.
Secondary: Bloomberg, "DeepSeek Plans Big Huawei AI Chip Order to Power New Data Center" (2026-09-04): https://www.bloomberg.com/news/articles/2026-09-04/deepseek-plans-big-huawei-ai-chip-order-to-power-new-data-center (paywalled, not independently fetched) ; https://www.techpowerup.com/352416/huawei-prepares-160-000-ascend-950dt-accelerators-for-deepseek-data-centar ; https://www.techtimes.com/articles/326755/20260905/deepseeks-160000-chip-huawei-order-puts-prc-law-over-every-api-query.htm ; https://www.tftc.io/deepseek-huawei-ascend-160000-chips-inner-mongolia-nvidia-sanctions
- Inclusion test: Directly extends Ch09's "serve without NVIDIA" sovereign-silicon thesis (chapters/09-china-ecosystem.md:57-63, V4/Ascend-950PR inference parity and the June 2026 MWC Shanghai carrier-scale validation). A 160,000-unit, 1GW commitment — "one of the largest known clusters of Huawei AI chips" per reporting — would be the largest concrete capacity commitment yet behind that thesis, if it lands.
- Recommendation: TIMELINE+CHAPTER, but conditional on the editor's tolerance for an unconfirmed-by-principals report — this is planning/intent reported by anonymous sources, not a shipped fact like the April 2026 V4/Ascend day-zero adaptation or the June MWC demo already in the chapter.
- Dedup: absent (no "160,000", "950DT", or "Ulanqab" hits in the clone).
- Flags: SECONDARY-ONLY (no primary confirmation from DeepSeek or Huawei; Bloomberg's own article is paywalled and was not independently fetched — this candidate rests entirely on secondary tech-press reporting of a Bloomberg exclusive).


## R4 B5

### B5. Qwen-Scope — open sparse-autoencoder (SAE) toolkit for the Qwen family (Ch09, cross-cutting interpretability) --- submitted 2026-05-12 (brief estimated ~May 1)
- What happened: Alibaba's Qwen team released Qwen-Scope, an open-source suite of 14 groups of SAEs across 7 Qwen3/Qwen3.5 model variants (dense and MoE, 0.5B–72B), covering 33M+ interpretable features. It packages SAE features into practical tools across three use areas: inference-time steering (manipulating internal features without prompt engineering), data classification/organization, and post-training support (SFT/RL). Announced via Alibaba_Qwen's X account with the framing "an open suite of sparse autoencoders for the Qwen model family... turns SAE features into practical tools."
- Primary: arXiv abstract page, "Qwen-Scope: Turning Sparse Features into Development Tools for Large Language Models," arXiv:2605.11887 (submitted 2026-05-12): https://arxiv.org/abs/2605.11887 (fetched directly — confirms submission date, title, 18 authors including Boyi Deng, Xu Wang, Yaoning Wang, Yu Wan) ; X announcement: https://x.com/Alibaba_Qwen/status/2049861145574690992 (could not fetch — HTTP 402; date not independently pinned beyond the arXiv submission)
Secondary: https://howaiworks.ai/blog/alibaba-qwen-scope-interpretability-sae ; https://www.spacemarvel.ai/blog/spacemarvel-blog-new-qwen-scope-the-open-source-sae-toolkit-that-finally-makes-llm-internals-actionable-md-1777642664525396
- Inclusion test: CONTRIBUTING.md explicitly names interpretability as a cross-cutting concern surfacing in Ch04/Ch11 (CONTRIBUTING.md context near the axis list). This is a first-party, open-source interpretability toolkit shipped by a major Chinese lab specifically for its own frontier open-weight family — a concrete Chinese-ecosystem contribution to the interpretability axis this framework already tracks, and it's currently absent from Ch09 entirely (the chapter's interpretability content is limited to DeepSeek's mHC, which is an architecture claim, not an interpretability tool).
- Recommendation: IN — CHAPTER (Ch09, new short entry) with a cross-link to wherever the framework's interpretability thread lives (Ch04/Ch11 per CONTRIBUTING.md); TIMELINE entry optional given it's outside this wave's window (May 2026) but is a backfill.
- Dedup: absent (no "Qwen-Scope" hits anywhere in the clone).
- Flags: PIN-DATE resolved (arXiv 2605.11887 = 2026-05-12, not the brief's estimated "~May 1"); the X-announcement date is UNFETCHED (402 paywall) so I cannot confirm whether the public/press announcement predates or postdates the arXiv submission.


## R4 C8

### C8. DeepSeek Harness (dsh) star/fork re-check --- 2026-09-15 (follow-up fact, not a new event)
- What happened: Per the brief's invitation to re-check, GitHub API shows DeepSeek Harness at 224,004 stars / 26,637 forks as of 2026-09-15 (`pushed_at` 2026-09-11T03:06:25Z), up from the 190,630/21,319 recorded in Ch09/Ch11 as of 2026-08-24.
- Primary: `gh api repos/deepseek-ai/deepseek-harness` (run 2026-09-15; command output: `{"forks":26637,"pushed_at":"2026-09-11T03:06:25Z","stars":224004}`)
- Inclusion test: pure metric refresh of an already-covered entry (chapters/09-china-ecosystem.md:67, chapters/11-timeline.md:386) — no new primitive.
- Recommendation: CHAPTER-ONLY (footnote-level number update if the editor wants the star count current) — not a timeline entry.
- Dedup: present — dsh is already covered at chapters/09-china-ecosystem.md:65-67, chapters/11-timeline.md:384-386, chapters/07-mcp.md:138/156, glossary.md:195.
- Flags: none (self-fetched via `gh api`, current as of research time).


## R1 C3

### C3. Codex Ships Governed Multi-Agent Delegation Modes (MultiAgentV2) --- Ch04, Ch14 (feeds Section E) --- primitive dated 2026-06-19/06-22; September refinements dated 2026-09-03/09-09
- What happened: OpenAI's Codex CLI/app-server exposes a `multiAgentMode` setting with three states --- `none` (no delegation instructions), `explicitRequestOnly` (delegate only if the user asks; the default for new threads), and `proactive` (delegate when it improves speed/quality) --- settable at thread level and overridable per turn, sticky across turns/resume/fork. This is a governed-delegation-edge primitive of exactly the shape Ch14 calls an "org graph": named roster (subagent threads) + permitted/forbidden transition rules, enforced outside the model (a developer-instruction fragment explicitly revokes standing delegation permission when the mode is not proactive). **The core primitive predates this wave's window** (GitHub PRs #28792 and #29324 merged June 19 and June 22, 2026, respectively) --- i.e., before even the July 17-18 catalyst tweet and before Anthropic's Aug 7 ListAgents/SendMessage. What is new *in this wave's window* is incremental hardening: "Guardian review history survives compaction, restarts, and user-created forks while respecting rollback boundaries and isolating subagent history" (Codex 0.153.0, Sept 3, 2026) and "multi-agent v2 environment context" changes referenced in PR activity around Sept 9, 2026.
- Primary: https://github.com/openai/codex/pull/28792 ; https://github.com/openai/codex/pull/29324 ; https://github.com/openai/codex/pull/28685 ; https://learn.chatgpt.com/docs/changelog (Sept 3 / Sept 9 2026 entries, fetched via redirect from developers.openai.com/codex/changelog)
- Secondary: none needed (GitHub is primary)
- Inclusion test: the underlying primitive is real and directly relevant to Ch14's org-graph definition, but it is not a *new* event in this wave --- the qualifying ship date is June, two backfill windows ago and outside even the "already covered" list's own scope. The September changelog entries are session-durability refinements to an existing feature, not a new primitive. Fails the window test for a fresh timeline entry.
- Recommendation: **REJECT** for a fresh timeline/chapter entry this wave. **Flag for Section E instead**: this is directly relevant "honest form" evidence (a harness vendor other than Anthropic shipping org-graph-shaped governance without ever using the phrase "graph engineering"), and it predates Anthropic's Aug 7 primitive by about seven weeks --- worth a retroactive one-line addition to Ch14 §14.2's "a vendor ships the structure, not the name" paragraph if the editor wants Codex named alongside Claude Code.
- Dedup: absent (grep "MultiAgentV2", "multi-agent delegation" --- zero hits).
- Flags: none (GitHub PRs are primary and unambiguous); PIN-DATE confirmed for the June merges via PR metadata.


## R1 C4

### C4. `headcount`: An Open-Source "Agent Company" Org Graph Ships as a Claude Code Plugin Marketplace --- Ch14 (feeds Section E signal 3) --- 2026-08-30/31
- What happened: An independent developer (GitHub user cbrock84) released **headcount**, an "agent organization for Claude Code, structured as a company": a chief-executive role over 16 departments and roughly 150-172 skills (sources disagree: 125+, 146, 172 across different snapshots of the README), each department an independently installable plugin, skills namespaced as `department:skill` (e.g. `security:threat-modeling`) to avoid collisions. Security and Legal & Risk are "reviewer-class" departments whose blocking findings the reviewed department cannot overrule, and they report to the CEO rather than into the function they audit. Each department ships an agent charter in `.claude/agents/`, giving it an "exclusive write surface" rather than a topic-based split --- the README explicitly argues "a topic split has no checkable boundary." Coverage (Enterprise DNA) dates the piece to roughly two weeks before Sept 15, i.e. ~Aug 30-31, 2026.
- Primary: https://github.com/cbrock84/headcount ; https://cbrock84.github.io/headcount/org-chart.html
- Secondary: https://enterprisedna.co/resources/ai-pulse/ai-pulse-2026-08-31-an-entire-agent-company-org-chart-shipped-as-a-claude-code-p/
- Inclusion test: this is a fully public, inspectable instance of Ch14's org-graph/work-graph split --- stable roster, governed review authority, checkable write-surface boundaries --- built entirely on top of Claude Code's existing subagent/plugin primitives, with no vendor involvement and no use of the term "graph engineering" anywhere in its own materials. It is evidence for Ch14 §14.7 Signal 3 (a named production case study) but at much lower disclosure weight than Stripe's minions: no operational metrics (no PR/task volume, no reliability numbers, no cost data) --- it is a structural artifact, not a production case study with numbers.
- Recommendation: **CHAPTER-ONLY** (Ch14, as supplementary Signal-3 evidence and/or a second example in §14.2's "vendor ships the structure, not the name" discussion, this time community-built rather than vendor-shipped). Not a timeline entry on its own --- it doesn't introduce a new primitive, it composes existing ones.
- Dedup: absent (grep "headcount" --- zero hits).
- Flags: UNFETCHED exact creation date (README/commit history not checked for a precise day; Aug 30-31 is inferred from secondary-source publish timing) --- PIN-DATE needed before citing a specific day.
