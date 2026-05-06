# Changelog

All notable changes to this guide are documented here. Dates are in HKT.

The guide is a living document — chapter and timeline updates ship continuously. This file gives returning readers a chronological view of what has shifted since their last visit, organized by month.

---

## May 2026

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
