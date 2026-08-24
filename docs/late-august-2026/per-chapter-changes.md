# Late-August 2026 Wave --- Per-Chapter Changes

Built from the six chapter drafters' reports, verified against the files on disk (2026-08-24).
Item IDs refer to `fact-sheet.md`.

## chapters/03-context-engineering.md --- W10

- **Section 3.3 (Lessons from Manus: KV-Cache as the North Star)** --- one compact paragraph after the existing Still / TokenPilot discussion, presenting arXiv 2608.00902 (August 2, 2026) as a narrowed design rule for agent-trajectory compaction: delay compaction until a proxy-query signal is available, and prefer token eviction over attention-matching reconstruction under imperfect proxies. Carries the 80% cache reduction with improved throughput on BrowseComp-Plus and WideSearch.
- **Sources** --- one matching bullet.

## chapters/04-harness-engineering.md --- W4, W8

- **§4.1** --- new paragraph after the AgentCore Payments discussion: Temporal Policies (Dogwood, Apache-2.0) as the session-history-aware generalization of the single-action hard cap, plus same-day Runtime Instances GA (14-day sessions vs the 8-hour serverless default). Cross-references §4.8's Terminal-Bench Challenges 12-hour result as counterpoint (longer sessions are not sustained progress) and the Authority axis in §4.4.
- **§4.7** --- new closing paragraph, "the countermove: open-source the moat": OpenAI's August 19 "Codex as a Platform" repositioning (app-server, Codex SDK, `codex exec` under Apache 2.0), carrying the nuance that `openai/codex` has been public and Apache-2.0 since April 2025. All vendor figures attributed to OpenAI. One-line cross-reference to DeepSeek Harness (Ch09) as the same-week pairing.
- **Sources** --- two matching entries (AWS; OpenAI).

## chapters/05-skill-systems.md --- W1, W2

- **§5.2 (The Anthropic Skills Ecosystem)** --- two paragraphs after the skills.sh registry paragraph: Skills API GA (release note August 19, companion blog August 20, discrepancy noted; `/v1/skills` stable, beta header no longer required; available through the Claude Platform and Microsoft Foundry), and GitHub-hosted skills for Managed Agents (August 7) with the auto-discovery / no-review trust-boundary point tied forward to §5.10.
- **§5.10 (Skill Security and the Supply-Chain Problem)** --- the Paperclip beat added as the third arc entry after Cloak-and-Detonate: org impersonation, the weaponize-after-trending timeline, 138 credential paths via four trigger mechanisms, the 1.7M aggregate-not-unique caveat carried parallel to AIR's 26,000 ambiguity, the 12-hour takedown, and an explicit non-conflation note against the separate Paperclip product CVEs. Closes with a sentence tying all three disclosures into one generalizing TOCTOU failure mode.
- **Sources** --- three bullets (Zenity Labs plus secondaries; Anthropic release notes / blog / Managed Agents docs).

## chapters/06-agent-memory.md --- W3

- **Mid-2026: Evaluation Grows Governance Axes** --- new closing paragraph on TencentDB Agent Memory v2.0's Team Memory as the first shipped production attempt at the access-control axis GateMem's null result identified as unsolved: visibility tiers over four versioned memory asset types, Memory Proxy speaking Anthropic and OpenAI protocols, L0-L3 distillation, BM25+vector+RRF retrieval. Every governance-mechanism claim flagged as Tencent's own, with the absence of any independent benchmark stated explicitly against GateMem's adversarial third-party evaluation.
- **Sources** --- one numbered entry (23) carrying the same vendor-claim caveat.

## chapters/07-mcp.md --- W9

- **New dated section "2026-08-22: What Comes After Finalization,"** inserted between "2026-07-28: The Specification Ships Final" and "Market Context": governance formalization (Contributor Ladder, Working-Group SEP triage, feature lifecycle and deprecation policy) and the five stated priorities, plus the same-day HN pickup flagged as a snapshot. Priority (1) tied back to the chapter's Tasks / extensions thread; priority (4) to its Meta-Tool Pattern section.
- **Sources** --- new entry 23.

## chapters/08-tools-landscape.md --- W11 (chapter-only, no timeline entry)

- **Notion AI section** --- new paragraph following the existing 3.6 External Agents paragraph: session-based Agent APIs move from private alpha to public beta (August 20, 2026) --- start / stream / submit-action / page-event-history against a Custom Agent, for third-party embedding, with the September 30, 2026 migration deadline. Framed as the third step after 3.5 (May 13) and 3.6 (July 1).
- **Sources** --- new entry 16.

## chapters/09-china-ecosystem.md --- W7

- **New subsection "DeepSeek Harness (dsh)"** under B (Chinese LLMs for Knowledge Management): MIT license, the Cordis plugin paradigm, the append-only session log, the Claude-Code / Codex sub-agent capability shipped first-party (`@deepseek-ai/dsh-subagent-claude-code` / `-codex` packages), and 190,630 stars / 21,319 forks with the GitHub-API verification date.
- **C. Open-Source as Strategic Imperative** --- new paragraph tying dsh to the same open-first logic moving from weights to the harness layer, cross-referencing OpenAI's concurrent Codex repositioning (Ch04) as the other side of the same-week beat.
- **Sources** --- primary (GitHub + deepseek.com) plus secondaries for the sub-agent claim and adoption framing.

## chapters/12-local-models.md --- W6

- **2026: Local Models Get an OS-Native API and Vendor QAT** --- section intro count updated from "Two" to "Three" releases; new paragraph on Meta Muse Glimmer (August 10, 2026): 30B dense, Apache 2.0, distilled from Muse Spark, under 20GB at 4-bit for single-consumer-GPU use. All DFlash speedups and the Gemma4-31B / Qwen3.6-27B comparisons marked as Meta's own figures. Framed as the first US-frontier-lab instance of the vendor-native multi-runtime day-0 pattern the Gemma-4-QAT paragraph flags, contrasted against Ch09's server-class-only Kimi K3. The separate undated Muse Spark 1.2 weights announcement is deliberately excluded.
- **Sources** --- primary (research.meta.ai) plus three secondaries.

## chapters/14-graph-engineering.md --- W5

- **§14.2 (What Graph Engineering Claims to Be)** --- new closing paragraph on Claude Code's August 7, 2026 cross-session agent messaging (`ListAgents` / `SendMessage`, v2.1.224 through v2.1.241), described against the org-graph definition already given in that section, with scope limits and platform exclusions carried. States explicitly that Anthropic's docs and changelog never use the phrase "graph engineering" --- evidence for the primitive, not the vocabulary. §14.7's survival-gate verdict is untouched.
- **Sources** --- one matching bullet (cross-session-messaging docs, changelog).

## Files owned by the connective-tissue pass

- `chapters/11-timeline.md` --- ten entries plus ten Sources entries (see `timeline-additions.md`).
- `glossary.md` --- one addition: **Temporal Policies**, in alphabetical position between Task Budget and Titans.
- `README.md` --- What's-new block rolled forward: intro rewritten to lead with the late-August wave, ten new bullets at the top, the early-August wave's three bullets demoted into the trailing list, the ten oldest trailing bullets dropped to hold the block at its previous length. *Last updated* footer verified at August 2026.
- `CHANGELOG.md` --- new H3 `### 2026-08-24 — Late-August 2026 wave: ...` at the top of the August 2026 section, with a Caveats passage carrying every PIN-DATE, VENDOR-CLAIM, and precision caveat that survives into the shipped text.

## Additional file produced by the Ch14 drafter

- `docs/late-august-2026/survival-gate-precheck.md` --- internal planning doc giving a per-signal verdict on the four September survival-gate signals named in Ch14 §14.7 (NOT-MET / NOT-MET / PARTIAL / MET). Report-only; explicitly not to be copied into chapter prose.
