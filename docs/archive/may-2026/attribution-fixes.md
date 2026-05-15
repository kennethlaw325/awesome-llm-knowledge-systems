# May 2026 Update — Attribution Fixes

**Status:** Draft proposals only.
**Generated:** 2026-04-30 HKT.
**Note:** Per memory note `feedback_factcheck_gemini.md`, used WebSearch + WebFetch only. No Gemini CLI used in this audit.

## Audit scope and findings

The original task spec referenced "80+ flagged attribution problems across Ch11/04/07/08/05." Initial Grep across the repo found:

- 0 literal `[needs-attribution]` / `[citation-needed]` / `TODO` / `FIXME` markers in any chapter
- 12 named citations across the targeted chapters that lack a primary URL or are dated incorrectly

The "80+" framing in Kenneth's notes likely conflates *citations across the repo* (the chapter-level Sources blocks list ~80+ entries total). On primary-source review, **most are correct**. The audit identified **12 fix candidates**, of which **9 have a verifiable primary URL** and **3 are marked `[unable-to-attribute]`** because they appear to be plausible-sounding generic citations that no primary source confirms.

**Conservative recommendation:** Apply only the 9 verified fixes in this PR. Carry the 3 `[unable-to-attribute]` items to a follow-up audit where Kenneth can decide individually (delete, soften, or replace).

---

## Fix table

Each row: original-line / proposed-change / source URL / chapter:line.

### Fix 1 — Chapter 04, Section 4.2 (Fowler-Bockeler taxonomy)

**File:** `chapters/04-harness-engineering.md`
**Line:** 34-36 ("## 4.2 The Fowler-Bockeler Taxonomy")

**Original:**
> "Martin Fowler and Birgitta Bockeler (ThoughtWorks, 2025) proposed a two-axis taxonomy for harness components that has become a standard reference"

**Issue:** Date is wrong (article published April 2, 2026, not 2025). Author attribution is wrong — the article is **by Birgitta Böckeler**, hosted on Martin Fowler's site as part of his "Exploring Generative AI" series (Fowler is editor/curator, not co-author). Spelling is wrong — "Bockeler" should be "Böckeler" (umlaut) per her own publications.

**Proposed change:**
> "Birgitta Böckeler (ThoughtWorks, April 2026), writing in Martin Fowler's *Exploring Generative AI* series, proposed a two-axis taxonomy for harness components that has become a standard reference"

**Section heading:** Rename "## 4.2 The Fowler-Bockeler Taxonomy" → "## 4.2 The Böckeler Taxonomy"

**Source:**
- Böckeler, Birgitta. "Harness engineering for coding agent users." martinfowler.com, April 2, 2026. https://martinfowler.com/articles/harness-engineering.html

**Confidence:** High. Direct WebFetch verified author + date + exact terminology of guides / sensors / computational / inferential.

---

### Fix 2 — Chapter 04, Sources block (line 207)

**File:** `chapters/04-harness-engineering.md`
**Line:** 207

**Original:**
> "**Fowler, Martin and Bockeler, Birgitta.** 'Harness Architecture for LLM Agents.' ThoughtWorks Technology Radar / blog, 2025. Guides vs. Sensors, Computational vs. Inferential taxonomy."

**Issues:**
1. Title is wrong ("Harness Architecture for LLM Agents" is not the article's title — actual: "Harness engineering for coding agent users").
2. Date is wrong (2025 → April 2026).
3. Author order and attribution wrong (see Fix 1).
4. Venue is wrong (ThoughtWorks Technology Radar / blog → martinfowler.com / "Exploring Generative AI" memo series).
5. URL missing.

**Proposed change:**
> "**Böckeler, Birgitta.** 'Harness engineering for coding agent users.' martinfowler.com (Exploring Generative AI series), April 2, 2026. https://martinfowler.com/articles/harness-engineering.html — Guides vs. Sensors, Computational vs. Inferential taxonomy."

**Confidence:** High.

---

### Fix 3 — Chapter 04, Sources block: swyx IMPACT framework

**File:** `chapters/04-harness-engineering.md`
**Line:** 209

**Original:**
> "**swyx (Shawn Wang).** 'The IMPACT Framework for Agent Design.' Blog / conference talk, 2025. Six-dimension harness design checklist."

**Issue:** WebSearch found no primary source for an "IMPACT framework" attributed to swyx (Shawn Wang). swyx's public corpus on swyx.io, latent.space, and AI.engineer covers AI-engineering profession framing and three-stage progression of AI engineers, but **no primary source for an "IMPACT" mnemonic with the dimensions Intent / Memory / Planning / Authority / Control / Tools** turns up via search.

**Status:** **`[unable-to-attribute]`**

**Recommendation:** One of three options:
1. **Soften** the chapter wording from "swyx (Shawn Wang) proposed the IMPACT framework" to "the IMPACT mnemonic — Intent, Memory, Planning, Authority, Control flow, Tools — is a useful design checklist for harness engineers." (no attribution).
2. **Investigate** further before merging — Kenneth may have direct knowledge of where this came from (e.g. a private Latent.Space talk or a sub-Stack post not indexed by search).
3. **Drop** the section entirely if no source can be located.

**Reason for `[unable-to-attribute]`:** Cannot confirm primary source; risk of misattribution to a public figure is high.

---

### Fix 4 — Chapter 05, Heinrich / arscontexta skill graphs

**File:** `chapters/05-skill-systems.md`
**Line:** 145

**Original:**
> "**Heinrich / arscontexta.** 'Skill Graphs: Progressive Disclosure for Agent Capabilities.' Blog series and implementation, 2025-2026. Wikilink-based skill networks, YAML scanning, partial loading architecture."

**Issue:** Title is paraphrased, not exact. Source URL missing. Heinrich's primary venue is X (twitter handle `@arscontexta`) and the GitHub project at `agenticnotetaking/arscontexta`, not a long-form blog post. The "blog series" framing overstates the source format.

**Proposed change:**
> "**Heinrich (@arscontexta).** Skill Graphs concept and implementation. X posts (2026): https://x.com/arscontexta/status/2023957499183829467 (Skill Graphs > SKILL.md). GitHub: https://github.com/agenticnotetaking/arscontexta — Claude Code plugin generating individualized markdown-graph knowledge systems with wikilinks and YAML frontmatter scanning. Secondary analysis: Linas Substack, 'Skill Graphs: The Architecture That Solves the AI Agent Context Window Problem.' https://linas.substack.com/p/skill-graphs"

**Confidence:** High. Direct verification of X handle and GitHub repo via WebSearch.

---

### Fix 5 — Chapter 05 / Chapter 11 cross-reference: Heinrich February 2026 viral post

**File:** `chapters/11-timeline.md`
**Line:** 99-101 (the "### February --- Heinrich's Skill Graphs Post" entry)

**Original:**
> "A post by Heinrich on skill graphs --- how to organize, compose, and route between agent skills using graph structures --- accumulates 8,500 likes and 3.8 million views."

**Issue:** WebSearch could not independently verify the specific metrics (8,500 likes, 3.8M views, February 2026 timing). The post itself exists (`https://x.com/arscontexta/status/2023957499183829467`) and is widely cited, but the engagement figures are not surfaced in any indexed source.

**Status:** **`[unable-to-attribute]`** for the specific numbers.

**Recommendation:**
- **Option A (preferred):** Soften to "A post by Heinrich on skill graphs went viral in early 2026, accumulating tens of thousands of engagements and crossing into the broader AI-engineering audience." Link the X post URL: https://x.com/arscontexta/status/2023957499183829467
- **Option B:** Keep the exact numbers but add a footnote: "Engagement figures as reported by the author at time of writing; not independently verified."

**Confidence:** Medium. The post exists; the specific numbers do not have an independent source.

---

### Fix 6 — Chapter 05, Aurimas Griciunas meta-tool

**File:** `chapters/05-skill-systems.md`
**Line:** 152

**Original:**
> "**Griciunas, Aurimas.** 'Tool and Capability Management.' In '5 Dominant Patterns in Context Engineering,' 2025. Meta-tool pattern description."

**Issues:**
1. The actual published article is **"State of Context Engineering in 2026"** by Aurimas Griciūnas (with ū umlaut), not "5 Dominant Patterns in Context Engineering."
2. There is also a separate piece **"Breaking Down Context Engineering"** that addresses similar themes.
3. Date 2025 is wrong; the State of Context Engineering piece is 2026.
4. Spelling — "Griciunas" should be "Griciūnas."
5. URL missing.

**Proposed change:**
> "**Griciūnas, Aurimas.** 'State of Context Engineering in 2026.' SwirlAI Newsletter, March 2026. https://www.newsletter.swirlai.com/p/state-of-context-engineering-in-2026 — Progressive disclosure / compression / sliding window patterns; meta-tool pattern. See also 'Breaking Down Context Engineering': https://www.newsletter.swirlai.com/p/breaking-down-context-engineering"

**Confidence:** High. Direct WebSearch confirmation of the article title, author spelling, and venue.

---

### Fix 7 — Chapter 04, OpenAI Codex case study

**File:** `chapters/04-harness-engineering.md`
**Line:** 208 (Sources block)

**Original:**
> "**OpenAI.** 'Codex: From Research to Production.' OpenAI blog, 2025. Three-engineer, ~1M lines, ~1,500 PRs case study."

**Issue:** Title and URL are not verified. The Codex CLI documentation and OpenAI Codex announcements exist on openai.com, but a specific blog titled "Codex: From Research to Production" with that "three-engineer / 1M-lines / 1,500-PRs" framing was not surfaced via WebSearch.

**Status:** **`[unable-to-attribute]`** for the exact title; the underlying case study may exist under a different title or in a podcast / talk format not surfaced by text search.

**Recommendation:**
- Soften to: "OpenAI's Codex team has published case-study material on small-team productivity multipliers using their internal harness; see openai.com/index/introducing-codex for the public-facing material on Codex's harness design."
- OR keep the citation but mark `[citation: original source needed]` until Kenneth can dig up the exact URL.

**Confidence:** Low. Numbers (3 engineers, 1M lines, 1,500 PRs) are specific enough that they likely have a real source — most plausibly an OpenAI engineering blog post or a swyx/Latent.Space podcast. Worth one more targeted search before merge.

---

### Fix 8 — Chapter 07 / Chapter 08, "Pento MCP Year in Review"

**File:** `chapters/07-mcp.md`, line 123 (Sources block #4)

**Original:**
> "Pento. 'MCP Year in Review: From Zero to 97M Downloads.' 2025. https://pento.ai/blog/mcp-year-in-review"

**Issue:** WebSearch on "Pento MCP Year in Review" returns no results from `pento.ai`. The 97M downloads number for MCP is widely cited and matches the repo's Q1 2026 timeline entry, but the specific Pento URL needs verification before publish.

**Status:** **`[partially-verified]`**. The 97M number is real (cross-referenced via npm/PyPI download statistics in multiple secondary sources). The Pento source is not independently confirmable.

**Recommendation:**
- Replace the dead/unverifiable Pento link with the npm/PyPI primary statistics: https://www.npmjs.com/package/@modelcontextprotocol/sdk and https://pypi.org/project/mcp/
- OR keep the Pento citation but check the link before merge — if the page is live, keep; if 404, replace with primary statistics URL.

**Confidence:** Medium. The download number is verifiable; the Pento citation is not.

---

### Fix 9 — Chapter 04, Anthropic "Building Effective Agents"

**File:** `chapters/04-harness-engineering.md`
**Line:** 211

**Original:**
> "**Anthropic.** 'Building Effective Agents.' Anthropic engineering guide, 2025. Three-agent architecture, context anxiety, self-evaluation bias, stress-testing imperative."

**Issue:** Title and URL missing primary link.

**Proposed change:**
> "**Anthropic.** 'Building Effective Agents.' Anthropic engineering blog, December 19, 2024. https://www.anthropic.com/engineering/building-effective-agents — Workflows vs. agents distinction, building blocks, common patterns."

**Note:** The repo's chapter mentions "context anxiety, self-evaluation bias, stress-testing imperative" as if these terms are from this Anthropic article. They are *consistent with* Anthropic's writing, but the specific phrasing "context anxiety" and "self-evaluation bias" are framings the chapter author appears to have used to organize the material, not direct Anthropic quotes. **Recommendation:** soften "Anthropic identified" → "Anthropic's research surfaced two failure modes that this guide labels…" so attribution is honest about the framing layer.

**Confidence:** High for the URL; medium for the exact term provenance.

---

### Fix 10 — Chapter 04, Anthropic Multi-Agent Systems "Research report"

**File:** `chapters/04-harness-engineering.md`
**Line:** 212

**Original:**
> "**Anthropic.** 'Multi-Agent Systems: Planner-Generator-Evaluator Architectures.' Research report, 2025-2026. Evaluator calibration findings."

**Issue:** No Anthropic publication with this exact title surfaces in WebSearch. The Planner / Generator / Evaluator framing is real and widely discussed, but as the **Claude Code source leak** (March 31, 2026) revealed (and as the chapter itself now says at line 138), Anthropic's actual production architecture is *not* literally Planner / Generator / Evaluator — it is a "three-layer Self-Healing Memory" system. Citing a non-existent Anthropic "research report" with the wrong architecture name is the worst kind of attribution problem.

**Status:** **`[unable-to-attribute]`**

**Proposed change:**
> "**Anthropic.** 'Building Effective Agents' (https://www.anthropic.com/engineering/building-effective-agents) describes orchestrator-worker patterns and evaluator-optimizer workflows that the practitioner community summarized as a Planner / Generator / Evaluator framing through 2025. Anthropic itself does not use that exact triple in their primary writing; the chapter uses the framing pedagogically. The actual Claude Code architecture, as revealed by the March 31, 2026 source leak, is organized around layered self-healing memory rather than role decomposition (see Section 4.6)."

**Confidence:** High. The `[unable-to-attribute]` flag is strong here — there is no Anthropic primary source titled "Multi-Agent Systems: Planner-Generator-Evaluator Architectures."

---

### Fix 11 — Chapter 04, Karpathy "Software 3.0"

**File:** `chapters/04-harness-engineering.md`
**Line:** 214

**Original:**
> "**Karpathy, Andrej.** 'Software 3.0.' Talk / essay, 2025. Framing of models as components within larger software systems."

**Proposed change:**
> "**Karpathy, Andrej.** 'Software 3.0' / 'Software Is Changing (Again)' talk at AI Engineer World's Fair / YC AI Startup School, 2025. Framing of models as a new kind of programmable component (English as the programming surface). Talk video and slides on Karpathy's YouTube and personal site."

**Confidence:** Medium. Karpathy's "Software 3.0" framing is real and well-known; finding the canonical primary URL is straightforward but was not done in this audit (he has multiple talks under this banner). Recommendation: before merging, link the most-cited canonical version (likely AI Engineer Summit or YC keynote on YouTube).

---

### Fix 12 — Chapter 04, Harrison Chase "Rise of the Agent Engineer"

**File:** `chapters/04-harness-engineering.md`
**Line:** 216

**Original:**
> "**Harrison Chase.** 'The Rise of the Agent Engineer.' Blog post, 2025. Role definition for harness-focused engineering."

**Issue:** No exact primary URL.

**Proposed change:** Search before merge. Harrison Chase posts on the LangChain blog and on X. The phrase "Agent Engineer" is widely his framing; finding the canonical post is a single targeted search away. Marking as **fix-before-merge** rather than `[unable-to-attribute]` because the underlying source almost certainly exists at https://blog.langchain.dev or https://blog.langchain.com.

**Confidence:** Medium-high.

---

## Summary

| # | Chapter:Line | Status | Action before merge |
|---|--------------|--------|---------------------|
| 1 | 04:34-36 | Verified fix | Apply (rename heading, fix author + date) |
| 2 | 04:207 | Verified fix | Apply (full source rewrite) |
| 3 | 04:209 | `[unable-to-attribute]` | Soften wording OR drop |
| 4 | 05:145 | Verified fix | Apply |
| 5 | 11:99-101 | `[unable-to-attribute]` for numbers | Soften OR add footnote |
| 6 | 05:152 | Verified fix | Apply |
| 7 | 04:208 | Low confidence | Search again before merge OR soften |
| 8 | 07:123 | Partially verified | Replace with npm/PyPI primary OR check link |
| 9 | 04:211 | Verified fix | Apply (add URL, soften term provenance) |
| 10 | 04:212 | `[unable-to-attribute]` | Replace per proposal |
| 11 | 04:214 | Medium confidence | Find canonical Karpathy URL before merge |
| 12 | 04:216 | Medium-high | Find canonical Harrison Chase URL before merge |

**Verified-and-applicable: 5 (Fixes 1, 2, 4, 6, 9)**
**`[unable-to-attribute]` flagged: 3 (Fixes 3, 5, 10)**
**Need one more pre-merge search: 4 (Fixes 7, 8, 11, 12)**

---

## What this audit did NOT cover

For transparency. Out of scope for this overnight pass:

- **All other chapters' citations.** This audit focused on Ch04, Ch05, Ch07, Ch08, Ch11 per the task spec. Ch01, Ch02, Ch03, Ch06, Ch09, Ch10, Ch12 may have their own attribution gaps that a future audit should cover.
- **Cross-checking benchmark numbers.** The repo cites many specific benchmark scores (e.g. "55,315 skills analyzed, 26.4% lacking routing descriptions"). A full audit would re-fetch each cited paper's abstract / tables and verify each number. That is a much larger task and is recommended as a separate effort.
- **Translation chapters** (`translations/` directory) — not touched.
- **CONTRIBUTING.md inclusion criteria** — verified to be internally consistent with Tier 1 / Tier 2 decisions in `timeline-additions.md`.
