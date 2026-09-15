# Gap-fill fact report — wave 2026-09-15
Check performed: 2026-09-15 08:58 HKT (2026-09-15T00:58:14Z)
All fetches read-only. No edits made to local clone or vault.

---

## T1. GPT-6 Astra primaries

All three URLs returned real page text via `mcp__exa__web_fetch_exa` (method: Exa fetch; WebFetch/curl were not needed — Exa succeeded on first try for all three).

### https://openai.com/index/gpt-6-astra/ (fetched via Exa)
(a) Release date as stated on page: the page itself carries no explicit "Published:" date banner (unlike the other two URLs); the launch is announced in present tense ("We're introducing GPT‑6 Astra..."). Cross-referenced from the safety-overview page (below), the launch date is 2026-09-03.

(b) Preparedness Framework "Critical" cybersecurity tier — exact sentence from this page:
> "As we discussed in our safety update, Astra is a significant jump in cyber capabilities and meets the Critical threshold in cybersecurity under our Preparedness Framework."

(c) Pricing lines (input/output/cached per million tokens): NOT PRESENT on this page. No pricing table or per-token pricing figures appear anywhere in the fetched text.

(d) Context window and max output: NOT STATED on this page. No numeric context-window or max-output-token figures appear in the fetched text.

(e) Enterprise access off-by-default / admin enable: NOT PRESENT on this page. The only access-related sentence is: "GPT‑6 Astra is rolling out today to a limited set of organizations and over the coming days will become available to all ChatGPT Plus, Pro, Business, and Enterprise users, as well as through the OpenAI API, Microsoft Azure, and AWS Bedrock." No mention of an enterprise admin-enable toggle.

(f) Chain-of-thought monitorability — exact sentence:
> "Our evaluations found Astra's written reasoning harder to monitor than GPT‑5.6 Sol's, based on tests that explicitly asked it to evade monitoring."
(Fuller context: "We attribute this to Astra's greater control over written reasoning on simpler tasks and ability to solve problems with fewer written steps. Astra still appears to struggle to conceal the reasoning needed for complex tasks, but we take the decline seriously.")

(g) ExploitBench / ExploitGym numbers — exact sentences:
> "We first tested the model without production safeguards on ExploitBench and ExploitGym, which evaluate whether models can turn known software vulnerabilities into working exploits. On ExploitBench, Astra achieved a perfect score of 100%, compared with 78.5% for GPT‑5.6 Sol, our previous frontier cyber-capable model. On ExploitGym, Astra reached a 42.4% success rate, compared with 30.3% for GPT‑5.6 Sol, while using substantially fewer output tokens."
Also: "We also tested Astra on SRE-Bench, a benchmark that measures whether models can reverse engineer software binaries... Astra solved 88.0% of tasks in a single attempt and 99.2% within four attempts, compared with 55.9% and 68.7% for GPT‑5.6 Sol, respectively."

(h) "Daybreak" program / vetted-defender access — exact sentence:
> "However, Astra will refuse to comply with more advanced cybersecurity tasks such as creating proof-of-concept exploits for vulnerabilities. Through OpenAI Daybreak, we plan to expand access and roll out less restrictive safeguards in the coming weeks. This will enable more defensive workflows, including vulnerability and proof-of-concept validation, malware analysis, and detection engineering."

### https://openai.com/index/safety-overview-gpt-6-astra/ (fetched via Exa)
Page states "Published: 2026-09-03" verbatim.

(a) Release date: 2026-09-03 (this page's own "Published" line).

(b) Critical cybersecurity tier — exact sentence:
> "Today, we are releasing GPT‑6 Astra, the most capable model we have ever broadly deployed. Astra is our first model to reach the Critical level of cybersecurity capability under our Preparedness Framework."
Also point 1 of the numbered list:
> "GPT‑6 Astra is a significant step up in cyber capabilities and meets our Critical threshold. This means that, with the right tools and access, GPT‑6 Astra can find previously unknown security flaws and develop new ways to exploit them across many well-protected systems without a person guiding each step."

(c) Pricing: NOT PRESENT on this page.

(d) Context window / max output: NOT PRESENT on this page.

(e) Enterprise access off-by-default: NOT PRESENT on this page (no such sentence found).

(f) CoT monitorability — exact sentence (point 5):
> "GPT‑6 Astra's monitorability has decreased relative to GPT‑5.6 Sol. We have performed significant investigations on the monitorability and controllability of GPT‑6 Astra. We have found that GPT‑6 Astra is more capable of controlling its own CoT than GPT‑5.6 Sol, and less likely to include incriminating information in its CoT. In adversarial settings (where we push the model to evade our monitors) we find that the model is able to remain undetected when strategically underperforming in evaluations (sandbagging) and can sometimes evade our internal monitors when asked to perform certain sabotage tasks."
And: "We have not seen evidence of steganographic CoT reasoning (e.g., concealing hidden reasoning within ordinary and seemingly unrelated text), indicating that the evasion risk may largely be bounded to lower reasoning tasks."

(g) ExploitBench/ExploitGym: not restated numerically on this page (numbers are on the main index page and path-to-astra page, see above/below).

(h) Daybreak: NOT PRESENT on this specific page (appears on the other two pages).

### https://openai.com/index/path-to-astra/ (fetched via Exa)
Page states "Published: 2026-09-01" verbatim.

(a) Release date: this specific post is dated 2026-09-01; it is a pre-launch capability/safeguards disclosure, not the launch announcement itself (launch was 2026-09-03 per the safety-overview page above).

(b) Critical cybersecurity tier — exact sentence:
> "We now believe Astra meets the Critical cybersecurity capability threshold under our Preparedness Framework, meaning that with the right tools and access, it can find previously unknown security flaws and develop ways to exploit them across many well-protected systems without a person guiding each step. It is the first model we are designating at this level, and requires stronger safeguards during development and before release."

(c) Pricing: NOT PRESENT.

(d) Context window / max output: NOT PRESENT.

(e) Enterprise access off-by-default: NOT PRESENT verbatim; closest related sentence concerns tester-gated cyber capability, not enterprise admin toggles:
> "We plan to make Astra available soon, but access to its most advanced cybersecurity capabilities will be more limited. Advanced cybersecurity work will initially be available to a group of testers, with access through Daybreak Blue following to expand defensive use."

(f) CoT monitorability: not directly addressed on this page (addressed on safety-overview page above).

(g) ExploitBench numbers — exact sentence:
> "As one example, we ran Astra on ExploitBench where the model achieved a perfect score of 100% on the benchmark to evaluate the model's ability to develop exploits from known vulnerabilities."
Also the internal-port benchmark: "we then built an internal benchmark denoted 'ExploitBench - Internal Port (June–August 2026)', which contains 20 high-severity V8 vulnerabilities that were disclosed more recently. On this dataset, Astra achieves much higher arbitrary code-execution rates than GPT‑5.6 Sol using far fewer output tokens. During the evaluation, the model even discovered and used two zero-day vulnerabilities as part of an exploit chain."

(h) Daybreak — exact sentence:
> "We plan to make Astra available soon, but access to its most advanced cybersecurity capabilities will be more limited. Advanced cybersecurity work will initially be available to a group of testers, with access through Daybreak Blue following to expand defensive use."
Also: "On our set of cyber jailbreak evaluations, Astra refuses 91.5% of requests (compared to 59% from GPT‑5.6 Sol)."

**SUMMARY / GAPS**: (c) pricing and (d) context-window/max-output were NOT FOUND on any of the three OpenAI pages — these facts are not present in the fetched marketing/safety pages at all (they likely live in API/pricing docs pages not in scope of this task; flagging as could-not-confirm-from-these-URLs, not a fetch failure). (e) "enterprise access off by default / admin enable" also not found on any of the three pages as a distinct claim.

---

## T2. Codex changelog Sep 1–15, 2026

Method: `mcp__exa__web_fetch_exa` on https://learn.chatgpt.com/docs/changelog (succeeded, no redirect needed) for the official page; `gh api repos/openai/codex/releases/tags/<tag>` via Bash for GitHub release bodies (the paginated `gh api repos/openai/codex/releases --paginate` call failed twice with "stream error: stream ID N; CANCEL; received from peer" — worked around by fetching each tag individually).

**Official changelog page (learn.chatgpt.com/docs/changelog) — September 2026 section**: contains exactly ONE dated entry: "2026-09-01 — Codex CLI 0.152.0". The page then jumps straight to "## August 2026". No entries for 2026-09-02 through 2026-09-15 appear on this page at all — the official changelog page has not been updated past 2026-09-01, even though many GitHub releases (0.152.1 through 0.155.0-alpha.5) shipped after that date.

**"codex queue" cross-session messaging**: Does NOT appear anywhere in the fetched changelog page text or in any of the 9 release bodies checked (0.152.0 through 0.155.0-alpha.5). The only "queue"-adjacent hits found: (1) changelog page, 0.150.0 section: "Reference other Codex tasks with `@` mentions, and ask agents to read, create, or message tasks from the terminal." (#40308, #40315) — task-level cross-references, not literally named "queue"; (2) release body for rust-v0.153.0: "TUI sessions reconnect after an external app-server connection drops, preserving drafts and transcripts while keeping uncertain or queued submissions paused for review." (#41911/#41916/#41918) — this is about paused UI submissions, unrelated to inter-agent messaging; (3) rust-v0.154.0 body: "#42903 Preserve TUI question state and integrate history and queue navigation" — UI history/queue navigation, not a "codex queue" feature. **No evidence of a literal "codex queue" cross-session-messaging feature exists in any fetched material.**

**"agents dashboard"**: Does NOT appear anywhere in fetched changelog page or release bodies.

**Indexed web-search mode**: Does NOT appear anywhere in fetched material. No hits for "indexed" in any release body or the changelog page text.

**Multi-agent / subagent / delegation entries found (dated, from changelog page + release bodies), verbatim one-line descriptions:**
- 2026-08-26 (v0.150.0, per PR list): "#39702 Wait for turn completion events in multi-agent resume tests" — https://github.com/openai/codex/releases/tag/rust-v0.150.0
- 2026-08-26 (v0.150.0): "#39722 Track multi-agent v2 spawn calls in analytics" — same URL
- 2026-08-26 (v0.150.0): "#39804 Use multi-agent V1 for Amazon Bedrock models" — same URL; bug-fix line: "Fixed conversation compaction and multi-agent compatibility for Amazon Bedrock models. (#39804, #39825)"
- 2026-09-01 (v0.152.0): New Feature description doesn't mention multi-agent directly, but PR list includes: "#41308 Make subagents follow the root service tier"; "#41380 Clarify proactive multi-agent delegation guidance"; "#41424 Preserve context baselines across nested agent forks"; "#41435 Allow bundled browser cleanup hooks on subagent stop"; "#41457 Source proactive multi-agent instructions from the model catalog"; "#41570 Fix proactive multi-agent instruction grammar" — all from https://learn.chatgpt.com/docs/changelog (September 2026 / Codex CLI 0.152.0 section), confirmed also present in the rust-v0.152.0 release body via gh api.
- No literal strings "multiAgentMode", "explicitRequestOnly", or "Guardian" (as a proper-noun review-mode name, as opposed to appearing as a common capitalized word) — correction: "Guardian" DOES appear repeatedly (56 times across the 9 release bodies checked) as an internal review/approval subsystem name, e.g. rust-v0.152.0: "#41221 Honor turn token budgets in Guardian review rollover", "#41660 Preserve Guardian authorization across history compaction", "#41846 Preserve Guardian review evidence across compaction". "multiAgentMode" and "explicitRequestOnly" as literal config-key strings were NOT found in any fetched text.

**Token/rollout budget entries (dated, verbatim):**
- 2026-09-01 (v0.152.0): "#41221 Honor turn token budgets in Guardian review rollover" — https://github.com/openai/codex/releases/tag/rust-v0.152.0
- 2026-09-01 (v0.152.0): "#41260 Let the history backend enforce tool output budgets"
- 2026-09-01 (v0.152.0): "Individual MCP tools support an `output_token_limit` setting, with consistent truncation across session resumes. (#41421)" — from changelog page New Features list
- 2026-09-01 (v0.152.0): "#41803 Allow models to enable token budgeting by default"
- 2026-08-29 (v0.151.0): "#41183 Account subagent token usage toward root goals"; bug-fix: "Counted nested subagent token usage toward root goal budgets. (#41183)"

**Default-model change — GPT-6 Astra as default (THE key finding for this task), verbatim, via gh api release-tag bodies:**
- Tag `rust-v0.153.1`, published 2026-09-03T21:02:56Z: "Added support for configuring GPT-6-Astra through the API without changing the default model or showing it in the model picker. (#42605)" — https://github.com/openai/codex/releases/tag/rust-v0.153.1 (this is explicitly NOT yet a default-model change — API-only, hidden from picker)
- Tag `rust-v0.153.4`, published 2026-09-04T23:25:48Z: **"Fixed Astra's visibility in the bundled model picker and made it the bundled default when no model is explicitly configured. (#42874)"** — https://github.com/openai/codex/releases/tag/rust-v0.153.4 — THIS is the line making GPT-6 Astra the bundled default.
- Tag `rust-v0.154.0`, published 2026-09-09T22:35:38Z: "GPT-6-Astra is now available in the model picker and Amazon Bedrock catalogs. (#42879, #42619)" — https://github.com/openai/codex/releases/tag/rust-v0.154.0
- Progression across dates: 0.153.1 (2026-09-03, API-only) → 0.153.4 (2026-09-04, bundled default) → 0.154.0 (2026-09-09, model-picker + Bedrock catalogs) → 0.154.0 also: "Updated the bundled OpenAI Docs skill with GPT-6-Astra migration, compatibility, and prompting guidance. (#42931)"

Full timeline of releases fetched (tag / published_at UTC), all via `gh api repos/openai/codex/releases/tags/<tag>`:
rust-v0.152.0 = 2026-09-01T01:58:32Z; rust-v0.152.1 = 2026-09-01T22:33:02Z; rust-v0.153.0 = 2026-09-03T01:37:38Z; rust-v0.153.1 = 2026-09-03T21:02:56Z; rust-v0.153.2 = 2026-09-03T23:53:12Z; rust-v0.153.3 = 2026-09-04T19:01:32Z; rust-v0.153.4 = 2026-09-04T23:25:48Z; rust-v0.154.0 = 2026-09-09T22:35:38Z; rust-v0.155.0-alpha.5 = 2026-09-15T00:31:51Z (today's most recent alpha — body text is just "Release 0.155.0-alpha.5", no changelog notes).

The full `gh api repos/openai/codex/releases --paginate --jq '...'` list call (unfiltered, all tags since 2026-08-23) DID succeed once (in the first round of this task) before erroring out partway through pagination — the partial output showed ~76 release tags between rust-v0.149.0-alpha.4.3 (2026-08-23) and rust-v0.155.0-alpha.5 (2026-09-15), overwhelmingly alpha/pre-release builds with sparse or empty bodies; I did not re-fetch bodies for every alpha tag (out of scope given the six specific keyword categories were already resolved from the 9 targeted tags above).

---

## T3. headcount dates + stats

Method: `gh api repos/cbrock84/headcount` via Bash (succeeded) for repo metadata; `curl` to `https://raw.githubusercontent.com/cbrock84/headcount/main/README.md` via Bash (HTTP 200) for the README's self-stated numbers.

Check performed: 2026-09-15 08:58 HKT (2026-09-15T00:58:14Z, UTC via `date -u`).

**Repo metadata (gh api, verbatim JSON):**
```
{"created_at":"2026-08-28T18:03:04Z","description":"An agent organization for Claude Code, structured as a company — 15+ departments, 125+ skills, each independently installable.","forks_count":212,"license":"MIT","pushed_at":"2026-09-03T02:54:33Z","stargazers_count":1392}
```
- created_at: 2026-08-28T18:03:04Z (this is the actual GitHub-recorded creation date, not an inference — contradicts the "~Aug 30-31 inferred from a secondary source" note in the task background; the API value is exact: 2026-08-28)
- pushed_at: 2026-09-03T02:54:33Z
- stargazers_count: 1392
- forks_count: 212
- license: MIT
- API-field description (may be stale — this is the GitHub repo "description" metadata field, separate from README content): "An agent organization for Claude Code, structured as a company — 15+ departments, 125+ skills, each independently installable."

**README's own stated numbers TODAY (verbatim, via raw README fetch, differs from the API description field above):**
```
<p align="center"><b>Add a department, not a prompt.</b></p>
<img alt="16 departments" src="https://img.shields.io/badge/departments-16-3F4B5B?style=flat-square">
<img alt="172 skills" src="https://img.shields.io/badge/skills-172-3F4B5B?style=flat-square">
<img alt="The headcount org chart — 16 departments, 172 skills, searchable" src="docs/assets/org-chart-light.png" width="840">
a chief executive over 16 departments, 172 skills in total.
```
**Discrepancy flagged**: the GitHub repo `description` API field says "15+ departments, 125+ skills" but the live README badges and body text say "16 departments" and "172 skills" — the README is more current/specific (exact counts, not "15+/125+" rounded language) and should be treated as the authoritative current figure; the API description field is stale copy that was not updated as the repo grew.

Per-department skill counts sampled from README (verbatim): "Office of the CEO (Chief Executive) — 7 skills"; "Technology (CTO / CIO) — 19 skills"; "Security (CISO) — 8 skills · reviewer-class"; "IT Operations (CIO) — 12 skills"; "Product (CPO) — 11 skills"; "Marketing (CMO) — 19 skills"; "Demand Generation (CMO) — 12 skills" (list continues beyond what was grepped).

---

## T4. TTHE vs critique

Method: `mcp__exa__web_fetch_exa` on https://arxiv.org/html/2607.12227 with maxCharacters raised to 80000 — this returned the COMPLETE paper including the full References list and both appendices (confirmed complete: ends with the paper's own "Instructions for reporting errors" arXiv footer, i.e. nothing was cut off).

**Search results for the four target strings across the full fetched text (abstract, intro, methods §3, experiments §4, discussion §5, conclusion §6, references, appendix A & B):**
- "2607.08124": ZERO occurrences.
- "TTHE": ZERO occurrences.
- "Test-Time Harness Evolution": ZERO occurrences.
- "Nie": ZERO occurrences (checked full author list and full reference list — no author named Nie appears anywhere).

**Does the paper cite/name TTHE?** NO. The paper's related-work discussion (Introduction, and "Automatic Harness Evolution" subsection) names only three prior harness-evolution methods by name: "Meta-Harness (4)" [Lee et al. 2026, arXiv 2603.28052], "Agentic Harness Engineering (6)" [Lin et al. 2026, arXiv 2604.25850], and "AEVO (17)" [Zhang et al. 2026, "Harnessing agentic evolution", arXiv 2605.13821]. The full References section (19 entries, all quoted arXiv IDs extracted) contains no entry matching 2607.08124, and no paper titled anything like "Test-Time Harness Evolution" or "TTHE." The reference list's arXiv IDs are: 2507.19457, 2407.21787, 2310.03714, 2603.28052, 2602.18998, 2604.25850, 2601.11868, 2506.13131, 2408.03314, 2203.11171, 2605.13821, 2510.04618 (several references — Lopopolo, Madaan/Self-refine, Opsahl-Ong, Trivedy, Yang/SWE-agent, Yuksekgonul, Zhao/Expel — carry no arXiv ID in the fetched citation format).

**v2 submission-history line, verbatim (from https://arxiv.org/abs/2607.12227v2, fetched via Exa):**
> "[v1] Tue, 14 Jul 2026 00:18:42 UTC (113 KB) [v2] Thu, 27 Aug 2026 12:13:50 UTC (113 KB)"
This confirms the v2 date is 2026-08-27, as stated in the task background.

---

## T5. MemTxn vs MemTX

Method: `mcp__exa__web_fetch_exa` on both abstract pages (both succeeded).

**MemTxn — https://arxiv.org/abs/2607.27834** (submitted 30 Jul 2026)
Authors (verbatim): "Hanshuai Cui, Zhiqing Tang, Zhi Yao, Fanshuai Meng, Qianli Ma, Weijia Jia"
Submission line (verbatim): "[v1] Thu, 30 Jul 2026 08:15:02 UTC (1,897 KB)" — single version only, no v2.
Full title: "MemTxn: A Transaction Boundary for Source-Supported Updates and Complete-State Recovery in Agent Memory"
Mechanism (verbatim from abstract): "MemTxn verifies whether an update is supported by its source. It also selects the visible version when facts conflict and restores the application-visible state after a fault. The system uses Ordered PatchTest to validate writes, a Temporal Resolver to select versions, and a durable snapshot journal to recover state."

**MemTX — https://arxiv.org/abs/2607.23929** (submitted 27 Jul 2026, v2 28 Jul 2026)
Authors (verbatim): "Xiaoyang Li, Yiqi Wang, Haohui Lu, Zhi Chen, Mo Li, Pingan Song, Mingkai Zheng, Taotao Cai"
Submission line (verbatim): "[v1] Mon, 27 Jul 2026 01:57:39 UTC (297 KB) [v2] Tue, 28 Jul 2026 12:51:37 UTC (297 KB)"
Full title: "MemTX: Transactional Belief Commit for Stateful Agent Memory"
Mechanism (verbatim from abstract): "We present MemTX, a transactional belief-commit protocol. Each record carries evidence, permissions, provenance, and validity. Writes are staged inside snapshot-isolated transactions and admitted by a validate-and-commit pipeline, irreversible tool calls are gated on in-flight belief state, and retracting a belief triggers typed cascading repair of its derived records and tool side effects."

**Same thread or independent?** INDEPENDENT. Zero author overlap between the two papers (8 distinct names on MemTX, 6 distinct names on MemTxn, no name appears on both lists). Submitted three days apart (27 Jul vs 30 Jul 2026) by apparently unrelated groups. The mechanisms are related in theme (both apply database-style "transaction" semantics to LLM agent memory writes) but differ in what they actually solve: MemTxn is about verifying an update is source-supported and recovering complete application state after a fault (via "Ordered PatchTest", "Temporal Resolver", "durable snapshot journal" — evaluated on LongMemEval-S, LoCoMo, MemoryAgentBench FactConsolidation, reporting F1 and accept/reject rates on 60 supported/179 hard-negative originals). MemTX is about gating irreversible tool-call side effects on a belief's commit status and cascading repair when a belief is retracted (via "snapshot-isolated transactions", "action-safety gating", "cascade-repair completeness" — evaluated via property-based testing/5.5M protocol states and paired-McNemar significance across five model backbones). Same high-level "transactional memory for agents" framing, convergent similar naming, but different named mechanisms, different authors, and different evaluation methodologies — not the same research thread.

---

## T6. Zenity Labs in-window posts

Method: `mcp__exa__web_fetch_exa` on https://labs.zenity.io/ (succeeded, full post-title index returned) and https://labs.zenity.io/post (FAILED: "Error fetching https://labs.zenity.io/post: CRAWL_NOT_FOUND" — this pagination URL does not exist / is not a valid path on the site).

**Result: NONE dated in window (2026-08-23 to 2026-09-15).**

The index at https://labs.zenity.io/ lists all posts newest-first. The most recent dated posts on the page (evidence the full/current index was reached), verbatim:
- "Claude in Chrome: From alert(1) to Full Account Takeover — Aug 5, 2026"
- "Claude in Chrome: Breaking down the injection — Aug 5, 2026"
- "Account Takeover via Claude in Chrome: A Technical Deep Dive — Aug 5, 2026"
- "Grand Theft Atlas — Aug 5, 2026 — How we hijacked ChatGPT Atlas with one planted X comment, to phish the victim's WhatsApp contacts and buy ourselves an Amazon order on their card"

There is also one "Featured" post pinned above the dated list with no visible date: "Attackers Target Agents via The Skill Supply Chain" (title only, no date shown on the index — could not confirm whether this falls in-window without opening the individual post page, which was not attempted since it's outside the six-URL/curl-method budget specified for this task and the task only asked to check the two given index URLs).

All four dated posts found (all Aug 5, 2026) fall BEFORE the 2026-08-23 window start. No posts dated 2026-08-23 through 2026-09-15 appear anywhere on the fetched index. The `/post` pagination path returned CRAWL_NOT_FOUND, so if the site paginates further posts are hidden behind a different URL scheme not attempted (out of scope per task instruction to only check these two URLs).

---
END OF REPORT
