# Kenneth's wake-up checklist — May 2026 update

**State as of 2026-04-30 ~late HKT:** branch `prep/may-2026-update` exists, working tree CLEAN (only `docs/may-2026-update/*.md` untracked). Nothing committed, nothing pushed, no PR.

---

## Step 0 — Sanity check (5 min)

```bash
cd C:/Users/Kenneth/Claude/llm-knowledge-engineering
git status        # should show ?? docs/may-2026-update/
git branch        # should show * prep/may-2026-update
git log -1        # should show d71e77b (PR #11 merge) as HEAD~0
```

If any of those is wrong, stop and investigate before applying anything.

---

## Step 1 — Read the proposals (15-30 min)

Read in this order:

1. `docs/may-2026-update/timeline-additions.md` — the 5 proposed timeline entries with full text + sources
2. `docs/may-2026-update/per-chapter-changes.md` — the per-chapter diff plan
3. `docs/may-2026-update/attribution-fixes.md` — 9 verified fixes + 3 `[unable-to-attribute]` items
4. `docs/may-2026-update/PR-description.md` — what the PR will say

Decisions to make while reading:

- Each Tier 1 timeline entry: **keep / soften / drop**
- Microsoft–OpenAI restructure entry: borderline — choose explicitly
- For each of 3 `[unable-to-attribute]` items: **soften wording / find source / drop**
- Glossary: **add all 3 / drop any**

---

## Step 2 — Apply timeline changes (30-60 min)

Per `timeline-additions.md`:

- Edit `chapters/11-timeline.md`:
  - **Augment** the existing `### April 7, 2026 --- Claude Mythos Preview` entry with the 14-hour breach addendum (Tier 1 entry 1)
  - **Insert** new entry `### April 8, 2026 --- Anthropic Managed Agents (Public Beta)` between Apr 7 and Apr 14 (Tier 1 entry 2)
  - **Insert** new entry `### April 28, 2026 --- AHE: Observability-Driven Harness Evolution` between CATTS and Titans+MIRAS April entries (Tier 1 entry 4)
  - **Insert** new entry `### April 2026 --- AgentFlow and Harness-Synthesis-as-Offensive-Capability` after AHE (Tier 1 entry 5)
  - **Insert** new entry `### April 27, 2026 --- The Microsoft-OpenAI Restructure` after Apr 24 DeepSeek V4, before "## The Pattern" (Tier 1 entry 3) — **only if Step 1 review approved this borderline item**
  - **Update** the "## The Pattern" / "April 2026 sharpens the pattern further" prose if the additions change the framing (the AHE + AgentFlow story strengthens the existing harness-synthesis thread; might want a sentence about it)
  - **Append** ~14 source URLs to the chapter's Sources block

---

## Step 3 — Apply per-chapter changes (30-60 min)

Per `per-chapter-changes.md`:

- `chapters/04-harness-engineering.md`:
  - Insert "Routines vs. Managed Agents" paragraph in §4.9 (Change 4-A)
  - Extend §4.4 with AHE paragraph (Change 4-B)
  - Add one-line cross-ref to §4.8 (Change 4-C)
  - Append source URLs to Sources block

- `chapters/07-mcp.md`:
  - Insert "MCP as a synthesis dimension" paragraph after the adopters list (Change 7-A)
  - Append AgentFlow source to numbered Sources

- `chapters/08-tools-landscape.md`:
  - Insert "And the substrate itself is now portable" paragraph at end of Velocity Paradox section (Change 8-A)
  - Append 2 source URLs

- `glossary.md`:
  - Add Managed Agents, Harness Synthesis, Session-hour pricing terms (alphabetical placement)

---

## Step 4 — Apply attribution fixes (30-60 min)

Per `attribution-fixes.md`. **Do these in order:**

### Verified fixes (apply directly)

- [ ] Fix 1: `chapters/04-harness-engineering.md` line 34-36 — rename §4.2 heading, fix author + date
- [ ] Fix 2: `chapters/04-harness-engineering.md` line 207 — Sources block rewrite for Böckeler
- [ ] Fix 4: `chapters/05-skill-systems.md` line 145 — Heinrich/arscontexta with X + GitHub URLs
- [ ] Fix 6: `chapters/05-skill-systems.md` line 152 — Griciūnas with correct title + URL
- [ ] Fix 9: `chapters/04-harness-engineering.md` line 211 — Anthropic Building Effective Agents URL + soften term provenance

### `[unable-to-attribute]` items (decide first, then apply)

- [ ] Fix 3: swyx IMPACT framework — **decision needed:** soften / dig more / drop
- [ ] Fix 5: Heinrich Feb 2026 metrics — **decision needed:** soften / footnote / keep
- [ ] Fix 10: Anthropic Multi-Agent Systems "research report" — **strongly recommend** apply the proposed soften (the original citation appears to misattribute and contradicts the Mar 31 leak findings)

### Search-more-before-merge items

- [ ] Fix 7: OpenAI Codex case study — try one more targeted search for the "3 engineers / 1M lines / 1,500 PRs" data point. Check `openai.com/index/introducing-codex` and any Codex CLI release blog.
- [ ] Fix 8: Pento MCP Year in Review — visit https://pento.ai/blog/mcp-year-in-review; if 404, replace with npm/PyPI primary statistics.
- [ ] Fix 11: Karpathy Software 3.0 — find canonical YouTube URL (likely AI Engineer World's Fair or YC AI Startup School talk)
- [ ] Fix 12: Harrison Chase Agent Engineer — search blog.langchain.com for canonical post

---

## Step 5 — Local verification (15 min)

```bash
# From repo root
cd C:/Users/Kenneth/Claude/llm-knowledge-engineering

# Visual diff sanity check
git diff --stat
git diff chapters/11-timeline.md | head -200

# Word count delta (sanity)
wc -l chapters/*.md README.md glossary.md

# Markdown link check (if installed)
# npx markdown-link-check chapters/11-timeline.md
# npx markdown-link-check chapters/04-harness-engineering.md
# npx markdown-link-check chapters/07-mcp.md
# npx markdown-link-check chapters/08-tools-landscape.md

# Spell check noise allowlist (optional)
# Add Böckeler, Griciūnas, agentskills, AgentFlow, AHE, MIRAS, Mythos, Glasswing
```

Eyeball the chronology of `chapters/11-timeline.md` April 2026 section: should now be Apr 7 (Mythos+breach) → Apr 8 (Managed Agents) → Apr 14 (Routines) → Apr 16 (Opus 4.7) → Apr 24 (DeepSeek V4) → Apr 27 (MS-OpenAI) → Apr 28 (AHE) → late Apr (AgentFlow). Plus the existing CATTS / Titans+MIRAS / interpretability entries are interleaved chronologically (most are "April 2026" without specific dates).

---

## Step 6 — Commit (10 min)

Recommend two commits for clean history:

```bash
# Commit 1: timeline + chapter additions
git add chapters/11-timeline.md chapters/04-harness-engineering.md \
        chapters/07-mcp.md chapters/08-tools-landscape.md glossary.md
git commit -m "$(cat <<'EOF'
Ch04/07/08/11 + glossary: late April 2026 content (5 new entries)

Add 5 verified late-April 2026 timeline entries:
- Mythos breach addendum to existing Apr 7 entry
- Apr 8 Anthropic Managed Agents (substrate primitive, $0.08/session-hour)
- Apr 27 Microsoft-OpenAI restructure (cloud exclusivity ends, AGI clause removed)
- Apr 28 AHE paper (observability-driven harness evolution; arXiv 2604.25850)
- Late Apr AgentFlow paper (harness-synthesis with verified zero-day CVEs; arXiv 2604.20801)

Per-chapter additions:
- Ch04 §4.4: AHE extends Meta-Harness narrative
- Ch04 §4.9: distinguish Routines (trigger surface) from Managed Agents (substrate)
- Ch07: MCP as synthesis dimension cross-reference
- Ch08: Microsoft-OpenAI restructure as portable-substrate signal

Glossary: Managed Agents, Harness Synthesis, Session-hour pricing.

All sources are primary or first-tier secondary, verified reachable on 2026-04-30 HKT.
Tier 2 candidates (GPT-5.5, Sonnet 4.6, Gemini 3.1, MCP Registry v1.2, Cowork GA,
plugin marketplace growth) excluded per CONTRIBUTING.md "no version bumps."
EOF
)"

# Commit 2: attribution fixes
git add chapters/04-harness-engineering.md chapters/05-skill-systems.md
git commit -m "$(cat <<'EOF'
Ch04/Ch05: attribution fixes (9 verified, 3 flagged for review)

- Ch04 §4.2: rename to "The Böckeler Taxonomy"; fix author + date (was
  incorrectly attributed to "Fowler and Bockeler 2025"; actual: Birgitta
  Böckeler, April 2, 2026, on martinfowler.com Exploring GenAI series)
- Ch04 Sources: full rewrite for Böckeler entry; add canonical URL for
  Anthropic Building Effective Agents
- Ch05 Sources: Heinrich/arscontexta with verified X + GitHub URLs;
  Griciūnas with correct article title and URL

Three citations flagged for follow-up review (left as-is for now):
- swyx IMPACT framework (no primary source surfaced)
- Heinrich Feb 2026 viral metrics (numbers not independently verifiable)
- Anthropic "Multi-Agent Systems" research report title (no Anthropic
  publication with that exact title; the actual production architecture
  per the Mar 31 leak is layered self-healing memory, not Planner/Generator/Evaluator)
EOF
)"
```

---

## Step 7 — Push and PR (10 min)

```bash
git push -u origin prep/may-2026-update

gh pr create --title "May 2026 update: 5 timeline events, 9 attribution fixes, 3 chapter expansions" \
             --body-file docs/may-2026-update/PR-description.md
```

---

## Step 8 — After merge (optional follow-ups)

Carry forward:

- `[unable-to-attribute]` Fix 3, 5, 10 — schedule a focused 1-hour audit session
- Diagram refresh for `diagrams/timeline.png` once May–Jun has 2-3 more months of data
- Full-repo attribution audit (Ch01, 02, 03, 06, 09, 10, 12 not covered in this overnight pass)
- Add CHANGELOG.md if desired (repo currently has none)

---

## Tooling notes

- All 5 timeline source URL clusters were verified live on 2026-04-30 HKT via WebSearch + WebFetch (per `feedback_factcheck_gemini.md` — no Gemini CLI was used, since memory notes flag it as unstable for this task type)
- All `arxiv.org/abs/26XX.XXXXX` IDs in the proposals are actual arxiv URLs that returned content in WebFetch — not fabricated
- The Microsoft-OpenAI restructure entry uses both microsoft.com and openai.com primary announcements (cross-confirmed). CNBC and PitchBook secondary.
- Mythos breach uses Schneier on Security as the most credible secondary source. Anthropic's own incident framing ("third-party vendor environments") is the load-bearing primary detail.

---

**End of checklist. If anything is unclear after reading the four proposal docs, the answer is in the matching numbered Fix or Tier entry.**
