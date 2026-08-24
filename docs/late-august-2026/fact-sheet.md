# Late-August 2026 Wave --- Fact Sheet (drafting source of truth)

> **Historical record.** This sheet is the PRE-fact-check drafting input. The adversarial
> fact-check corrected several items afterward (TencentDB v2.0.0 pinned to Aug 3; Codex as a
> Platform re-dated Aug 19 per the primary page stamp; the dsh sub-agent capability confirmed
> first-party; Vertex-AI clause descoped). Shipped text and CHECKLIST.md are authoritative.

Selection date: 2026-08-24 (HKT). Window: 2026-08-01 through 2026-08-24.
Research: 10-agent sweep, every candidate primary-source fetched + deduped against repo.
This sheet is the drafting input. Facts below are researcher-verified unless marked
VENDOR-CLAIM or PIN-DATE (fact-check phase re-verifies every load-bearing URL independently).

**Quote rule (COPY-EXACT-OR-PARAPHRASE-WITHOUT-QUOTES):** anything inside quotation marks
must be a verbatim substring of a fetched source. Ellipsis may only delete, never substitute.
Hedge words (e.g. "possibly") may not vanish inside a quote. When unsure: paraphrase, no quotes.

**Style rules (non-negotiable):**
- `chapters/*.md` + `glossary.md`: ASCII dashes only (` --- ` / ` -- `). No Unicode em-dash.
- README What's-new bullets + CHANGELOG H3 body: Unicode — allowed (matches existing text).
- Timeline entries: `### Month DD, YYYY --- Title` format, inserted chronologically BEFORE `## The Pattern`; add matching source lines under `## Sources`.
- Vendor benchmark/scale claims are always attributed ("per X's own figures", "a vendor claim").
- Dates in HKT; day precision only when a source states the day, else month precision + say so.
- Match the register of surrounding prose: analytical, editorial, compressed. Read the target section before writing.

---

## Selected items (10)

### W1. Paperclip Skills supply-chain campaign on skills.sh (Ch05 §5.10 + Ch11)
- Date: weaponized by July 11; Zenity Labs disclosure **August 6, 2026** (repo precedent: date to disclosure). Timeline entry date: Aug 6.
- Facts: attackers impersonated paperclipai and browser-use GitHub orgs (registered getpaperclipp.com; getpaperclipai org created July 2). Skills published to skills.sh started benign July 5, weaponized July 11, reached #8 trending. Credential-harvesting payload (curl → base64 → node chain) targeted 138 credential paths (SSH, AWS/GCP/Azure, Kubernetes, npm tokens, DB credentials) via four trigger paths: direct skill instructions, malicious PyPI package, npm postinstall hooks, API route handlers. Displayed install counter >1.7M (aggregate, NOT unique agents — carry this caveat, same as AIR's 26,000 ambiguity). Vercel + GitHub removed listings/repos within 12 hours of disclosure.
- Primary: https://labs.zenity.io/post/attackers-target-agents-via-the-skill-supply-chain
- Secondary: thehackernews.com/2026/08/paperclip-ai-flaws-let-attackers-run.html ; csoonline.com/article/4206851/ ; businesswire.com/news/home/20260806707467/en/
- Framing: third beat in §5.10's arc (AIR June 22 → Cloak-and-Detonate July 2 → Paperclip Aug 6): TOCTOU/weaponize-after-vetting generalizes from one Instagram-ad campaign to a whole trending skill family with four trigger mechanisms.
- Do NOT conflate with the separate Paperclip product CVEs (CVE-2026-41679 etc., Aug 5) — those are vulnerabilities in the legitimate product, out of scope.

### W2. Anthropic Agent Skills / Skills API reach GA + GitHub-hosted skills (Ch05 + Ch11)
- Dates: GitHub-hosted skills for Managed Agents **Aug 7** (release note); Skills API out of beta **Aug 19** (release notes) with companion blog dated **Aug 20** — one-day discrepancy across Anthropic's own surfaces, likely publish lag; note both, date the timeline entry Aug 19.
- Facts: /v1/skills out of beta; skills-2025-10-02 beta header no longer required (still accepted). Part of a production-agent GA wave (computer use, browser use, Files API). Available on Claude Platform + Microsoft Foundry; Vertex AI "coming soon" (verify exact wording if quoted). GitHub-hosted skills: mounted repo's root .claude/skills auto-discovered at session start; Anthropic's own docs flag the mounted repo becomes part of the agent's trust boundary (no review step).
- Primary: https://platform.claude.com/docs/en/release-notes/overview ; https://claude.com/blog/computer-use-skills-api-files-api ; https://platform.claude.com/docs/en/managed-agents/skills
- Framing: the skill primitive graduating to production API status ~10 months after the Oct 2025 launch Ch05 already dates; GitHub-hosted auto-discovery is a new trust-boundary pattern that ties into §5.10's security framing.

### W3. TencentDB Agent Memory v2.0 --- Team Memory (Ch06 + Ch11)
- Dates: v2.0.0 release **PIN-DATE early August** (MarkTechPost coverage Aug 7 says v2.0; PRNewswire team-collaboration announcement Aug 13). Researcher dated v2.0 to Aug 3 — fact-check must pin via GitHub releases; if no day-precision source, use "early August 2026" and date timeline entry to the Aug 13 announcement.
- Facts: MIT-licensed, self-hosted; repo created 2026-04-07; 24,185 stars at research time (gh api verified 2026-08-24 — re-verify at check time, cite as "~24K"). Team Memory: governance layer for cross-agent sharing — private/team/restricted/agent visibility tiers over four versioned memory asset types (Chat Memory, Skill, Wiki, CodeGraph). Memory Proxy exposes Anthropic + OpenAI protocols; L0-L3 layered distillation; BM25+vector+RRF retrieval under budget caps. VENDOR-CLAIM: all governance-mechanism claims are Tencent's own — no independent benchmark exists (unlike GateMem's adversarial evaluation). Carry this explicitly.
- Primary: https://github.com/TencentCloud/TencentDB-Agent-Memory ; https://www.marktechpost.com/2026/08/07/tencent-cloud-open-sources-tencentdb-agent-memory-v2-0/
- Secondary: prnewswire.com/apac/news-releases/tencentdb-agent-memory-tops-20-000-github-stars-in-90-days-launches-team-memory-for-multi-agent-collaboration-302850576.html
- Framing: first shipped production attempt at the exact governance gap GateMem (June, already in Ch06) identified as unsolved — extends the chapter's "evaluation grows governance axes" thread from benchmark to shipped primitive, with the independent-evaluation caveat carried.

### W4. AWS AgentCore: Temporal Policies (Dogwood) + Runtime Instances GA (Ch04 + Ch11, ONE combined timeline entry, Aug 6)
- Date: both **Aug 6, 2026** (same AWS release wave).
- Temporal Policies facts: stateful gateway-enforced authorization — evaluates a tool call against the agent's prior actions/session history, deterministic, deny-by-default, fully logged, outside agent code. Built on Dogwood, new Apache-2.0 open-source policy language purpose-built for AI agents. Named uses: data-fabrication prevention (value passed must match earlier call's return), cumulative session cost caps, workflow sequencing / human approval before privileged steps. Shipped alongside gateway Rate Limiting (per-user/OAuth/IAM caps on requests, tokens, connection duration).
- Runtime Instances facts: GA — agents on customer-selected EC2 types (GPU/memory/compute-optimized), AWS-managed lifecycle; microVM serverless remains default (8-hour sessions); Runtime Instances support sessions up to **14 days**; nine regions; EC2 cost + management fee.
- Primary: https://aws.amazon.com/blogs/machine-learning/control-agent-behaviors-and-cost-beyond-a-single-action-new-capabilities-in-amazon-bedrock-agentcore/ ; https://aws.amazon.com/about-aws/whats-new/2026/08/temporal-policies-agentcore/ ; https://aws.amazon.com/about-aws/whats-new/2026/08/aws-bedrock-agentcore-runtime-instances-generally-available/
- Framing: §4.1's AgentCore Payments example was a single-action hard cap; Temporal Policies generalizes deterministic non-LLM enforcement to multi-step session history via an open policy DSL — a new primitive class on the Authority axis. 14-day sessions are the infrastructure counterpoint to §4.8's Terminal-Bench endurance null result (the substrate now offers multi-day sessions, orthogonal to whether the model makes progress across them).
- Glossary: add **Temporal Policies** (ASCII dashes).

### W5. Claude Code ships cross-session agent messaging (Ch14 + Ch11)
- Date: **Aug 7, 2026** (v2.1.224), iterating through v2.1.241 (Aug 23); Windows support v2.1.239 (~Aug 22, per secondary).
- Facts: ListAgents discovers named sessions (subagents, teammates, other local sessions, cloud sessions, Remote Control sessions on other machines); SendMessage delivers plain text between them by name. Per-session inbound governance (accept/hold/refuse), permission-mode-based default, size/burst/loop throttling. Scope limits: no conversation history or files cross sessions, no cross-session permission approval. NOT available on Bedrock / Claude Platform on AWS / Google Cloud Agent Platform / Microsoft Foundry (per docs).
- Primary: https://code.claude.com/docs/en/cross-session-messaging ; https://code.claude.com/docs/en/changelog
- Framing (careful, honest): a major harness vendor ships the org-graph primitive Ch14 describes (named-agent roster + governed message edges) WITHOUT using the "graph engineering" label — coverage must state explicitly that Anthropic does not use the term, so this counts as pattern-operationalization, not vocabulary adoption (feeds §14.7 signal 1 honestly). Place in Ch14 where the org-graph/work-graph discussion lives; timeline entry Aug 7.

### W6. Meta Muse Glimmer --- open-weight model built for local agents (Ch12 + Ch11)
- Date: **Aug 10, 2026**.
- Facts: Meta Superintelligence Labs; 30B dense, Apache 2.0, distilled from closed Muse Spark; positioned as open agentic model for on-device use; <20GB at 4-bit for 24-32GB consumer systems, single consumer GPU (Mac or PC). VENDOR-CLAIM: DFlash speculative decoding speedups (3.1x RTX 5090 / 1.8x M5-Max / 1.5x M4-Max) and benchmark superiority vs Gemma4-31B / Qwen3.6-27B are Meta's own figures, not independently reproduced — attribute explicitly. Day-0/near-day-0 runtime support: Hugging Face, Ollama 0.32.7, llama.cpp, MLX, ExecuTorch, LM Studio, Unsloth, vLLM, SGLang, Together AI, Fireworks AI, OpenRouter. Meta separately said Muse Spark 1.2 weights will be released later — distinct undated event, do NOT cover.
- Primary: https://research.meta.ai/blog/introducing-muse-glimmer-open-agentic-model
- Secondary: phoronix.com/news/Meta-Muse-Glimmer ; cnbc.com/2026/08/10/meta-muse-glimmer-open-weight-ai.html ; ghacks.net (Aug 11)
- Framing: Ch12 has so far only seen server-class open weights (Kimi K3, explicitly excluded from the local story) — this is a US frontier lab shipping a model designed and benchmarked for single-consumer-GPU local agents with multi-runtime day-0 support, the first US-lab instance of the vendor-native release pattern the Gemma-4-QAT section flags.

### W7. DeepSeek Harness (dsh) --- open-source agent harness (Ch09 + Ch11; cross-ref Ch04)
- Date: **Aug 13, 2026** (developer preview).
- Facts: MIT license, github.com/deepseek-ai/deepseek-harness. "Cordis" plugin paradigm (cited whitepaper: "A Programming Paradigm for Spatiotemporal Composability") — model adapter, tool registry, session log, sandbox, storage, scheduling loop, UI all swappable plugins. Append-only session log records every context injection (system prompts, reasoning, tool calls/results, subagent scheduling). Press reports it can invoke Claude Code or Codex as sub-agents (secondary-sourced — attribute to coverage, not DeepSeek, unless primary confirms). Stars: 190,630 + 21,319 forks in 11 days, gh api verified 2026-08-24 — RE-VERIFY at fact-check and cite the checked number with date; "one of the fastest adoption curves recorded for a dev tool" only as qualitative.
- Primary: https://github.com/deepseek-ai/deepseek-harness ; https://deepseek.com/harness/en/
- Secondary: cryptobriefing.com ; mindstudio.ai/blog ; digitalapplied.com ; flowtivity.ai
- Framing: first Chinese-lab open-source agent harness with fully plugin-decomposed runtime + cross-vendor subagent orchestration — extends Ch09's "open-source as strategic imperative" from model weights to the harness layer. Pairs with W8 as the wave's headline beat: the harness layer went open-source on both sides of the Pacific within a week.

### W8. OpenAI open-sources Codex "Harness" --- "Codex as a Platform" (Ch04 + Ch11)
- Date: **Aug 20, 2026** PIN-DATE (secondary outlets date it Aug 20; primary page's date not surfaced to the fetcher — fact-check must pin date + Apache-2.0 from primary or best available).
- Facts: OpenAI open-sources the execution engine behind Codex, branded "Harness", Apache-2.0: codex exec (CLI), Codex SDK, app-server (long-lived local process holding conversation state, streaming events, exposing tools, routing approval requests). Model access + managed services stay proprietary. IMPORTANT nuance: openai/codex repo has been public/Apache-2.0 since April 2025 (gh api verified) — the event is OpenAI formally repositioning/completing the harness layer (app-server + SDK) as a decoupled platform product, NOT a first-ever open-sourcing; draft must carry this nuance. VENDOR-CLAIM: retained-reasoning + context compaction raised GPT-5.6 Sol's ARC-AGI-3 from 13.3% to 38.3% with 6x fewer output tokens (OpenAI's own numbers). Cited production users: Cisco (App Builder in Cisco Cloud Control), GitHub/JetBrains (IDE agent provider), Thrive Holdings/Crete tax-prep pilot (7,000 returns, ~1/3 less prep time — vendor-cited).
- Primary: https://developers.openai.com/blog/codex-as-a-platform
- Secondary: opensourceforu.com/2026/08/openai-open-sources-codex-harness/ ; finance.biggo.com
- Framing: operationalizes §4.7's "harness is the moat" thesis in the OPPOSITE direction from the managed-substrate wave (Anthropic Managed Agents, AWS AgentCore, Microsoft Agent Harness): instead of selling the harness as a hosted SKU, open-source the engine and keep the model as the product.

### W9. The New MCP Roadmap (Ch07 + Ch11)
- Date: **Aug 22, 2026**.
- Facts: MCP core maintainers' updated roadmap for the post-final-spec period. Governance: Contributor Ladder formalized; SEP triage moves into domain-specific Working Groups; formal feature lifecycle/deprecation policy. Five priorities: (1) agentic messaging primitives — server-initiated events (webhooks, channels) + maturing Tasks extension toward full spec inclusion; (2) HTTP-native transport unification extended to local deployments; (3) agent identity / enterprise security standardization (DPoP, Workload Identity Federation); (4) improved tool-result handling + progressive discovery over large tool catalogs; (5) SDK DX/conformance. HN pickup same day: 241 points / 142 comments (cite as snapshot).
- Primary: https://blog.modelcontextprotocol.io/posts/mcp-roadmap/
- Framing: the maintainers' own statement of the next primitive wave after the 2026-07-28 final spec Ch07 already covers fully; Ch07 gets a short "what comes after finalization" section, timeline entry Aug 22.

### W10. Practical Online KV Cache Compaction for LLM Agents (Ch03 §3.3 + Ch11, compact)
- Date: **Aug 2, 2026** (arXiv 2608.00902 submission).
- Facts: systematic empirical study of KV-cache compaction for agent trajectories specifically. Findings: immediate compaction hurts accuracy; delaying until the agent's own future queries serve as a proxy-query signal recovers most of the gap; token eviction (TE) scored by proxy-query-induced attention mass is more robust than attention-matching reconstruction (AM) under imperfect proxies; TE cuts KV cache 80% while improving throughput over no-compaction; evaluated on BrowseComp-Plus and WideSearch.
- Primary: https://arxiv.org/abs/2608.00902
- Framing: short addition to the existing Still/TokenPilot compaction thread in Ch03 — the design guidance (delay compaction; eviction over reconstruction) is the tracked-primitive extension. Keep tight (a few sentences + timeline entry).

### W11 (chapter-only, no timeline entry). Notion Agent APIs reach public beta (Ch08)
- Date: **Aug 20, 2026**.
- Facts: session-based Agent APIs (start chat with a Custom Agent, stream reply, submit action, page session event history) move private alpha → public beta; purpose: embed Custom Agents in third-party surfaces (Slack bot, internal tool, mobile). Alpha-route integrations must migrate to sessions/events model by Sept 30, 2026.
- Primary: https://developers.notion.com/page/changelog
- Framing: next step in the arc Ch08 already tracks (3.5 Developer Platform May 13 → 3.6 External Agents July 1 → embeddable public API surface Aug 20). Follow mid-July precedent: chapter integration only.

---

## NOT selected (for the record)
Researchers' full rejected lists live in the wave research output (workflow wf_39321bd7-c55 journal). Notable deliberate exclusions: ChatGPT memory August updates (UI-level scoping on the pre-window Dreaming architecture), Gemini Memory Bank GA (July 29, pre-window — backfill candidate), GLM-5.3 / Qwen3.8-Max / DeepSeek V4-Pro GA / V4-Flash-Vision (version bumps), Microsoft Agent Framework Harness GA (billing/stability milestone on covered primitive), Terminal-Bench leaderboard shuffles (score movement), Heptabase/Anytype/Tana August items (feature bumps or pre-window), Arcads Marketing OS (no internals disclosed; kept only as survival-gate signal-3 evidence), llama.cpp/Ollama routine updates, MCP allowlists in GitHub Copilot (admin feature).

## Backfill candidates (pre-window, future wave decision, do NOT draft now)
- Anthropic "The new rules of context engineering for Claude 5 generation models" (July 24) — Ch03.
- Google Gemini Enterprise Agent Platform Memory Bank GA (July 29) — Ch06.
- Memory Decoder at Scale / MemTxn / Filesystem-Based Memory Study (arXiv 2607.27919 / 2607.27834 / 2607.26637, July 29-30) — Ch06.
- TTHE (arXiv 2607.08124) + rebuttal (2607.12227) — Ch04.
- Qwen-Scope SAE toolkit (~May 1) — Ch09.
- OpenRouter top-5 all-Chinese week (reported July 29) — Ch09 strengthener.
