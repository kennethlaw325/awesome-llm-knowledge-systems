# PR — May 2026 update — 5 timeline events, 9 attribution fixes, 3 chapter sections expanded

**Status:** Draft. Branch `prep/may-2026-update`. NOT pushed, NOT opened as PR.
**Generated:** 2026-04-30 HKT.

---

## Title (under 70 chars)

`May 2026 update: 5 timeline events, 9 attribution fixes, 3 chapter expansions`

---

## Summary

- **Timeline:** 5 verified late-April 2026 entries — Mythos breach, Managed Agents (Apr 8), Microsoft–OpenAI restructure (Apr 27), AHE paper (Apr 28), AgentFlow harness-synthesis. All sourced to primary or first-tier secondary URLs. Tier 2 candidates (Sonnet 4.6 / GPT-5.5 / Gemini 3.1, MCP Registry hardening, Cowork GA, plugin-marketplace growth) deliberately excluded per CONTRIBUTING.md "no version bumps."
- **Chapter 04 (Harness Engineering):** 3 changes — distinguish Routines (trigger surface) from Managed Agents (substrate) in §4.9; extend Meta-Harness narrative with AHE in §4.4; one-line cross-reference in §4.8.
- **Chapter 07 (MCP):** 1 paragraph noting MCP-as-synthesis-dimension (AgentFlow framing).
- **Chapter 08 (Tools Landscape):** 1 paragraph on the Microsoft–OpenAI restructure as a substrate-portability change.
- **Glossary:** 3 new terms — Managed Agents, Harness Synthesis, Session-hour pricing.
- **Attribution audit:** 9 verified citation fixes applied (Böckeler 2026 vs. "Fowler-Bockeler 2025"; Heinrich/arscontexta with proper X + GitHub URLs; Griciūnas 2026 with correct article title and URL; Anthropic Building Effective Agents URL; etc.); 3 entries flagged `[unable-to-attribute]` for future review (swyx IMPACT framework, Heinrich Feb 2026 viral metrics, Anthropic "Multi-Agent Systems" research-report title).

## Per-chapter change summary

| Chapter | File | Change |
|---------|------|--------|
| 04 Harness Engineering | `chapters/04-harness-engineering.md` | §4.2 heading rename, §4.4 AHE addition, §4.8 cross-ref, §4.9 Managed Agents distinction, Sources block updates |
| 07 MCP | `chapters/07-mcp.md` | One-paragraph cross-ref to AgentFlow as synthesis dimension; Sources block addition |
| 08 Tools Landscape | `chapters/08-tools-landscape.md` | One-paragraph Microsoft–OpenAI restructure as portable-substrate signal; 2 source URLs added |
| 11 Timeline | `chapters/11-timeline.md` | 4 new entries + 1 augmentation; ~14 new source URLs |
| Glossary | `glossary.md` | 3 new terms added |

**No changes to:** README, Ch01, Ch02, Ch03, Ch05 (Sources block fix only — see attribution-fixes.md), Ch06, Ch09, Ch10, Ch12, diagrams, translations.

## Diff size estimate

- ~+130 lines added across content
- ~21 new source URLs (all primary or first-tier secondary, all verified reachable)
- 9 attribution fixes (corrections, not deletions)

## Test plan

- [ ] Markdown link check on all chapter files (e.g. `markdown-link-check chapters/*.md`)
- [ ] Spell check on changed sections (Böckeler with umlaut, Griciūnas with macron — these will trigger spellcheck noise; allowlist them)
- [ ] Table-of-contents validity in `chapters/11-timeline.md` (new entries must be in chronological order: Apr 7 → Apr 8 → Apr 14 → Apr 16 → Apr 24 → Apr 27 → Apr 28 → late Apr)
- [ ] `## Sources` blocks in Ch04, Ch07, Ch08, Ch11 — each new entry has a primary URL
- [ ] Cross-references work (e.g. Ch04 §4.4 reference to Ch04 §4.8 cross-ref AHE)
- [ ] No broken anchor links to `chapters/05-skill-systems.md` after potential heading rename
- [ ] Visual scan of Tier 2 rejections list to confirm no genuinely structural item was filtered out
- [ ] CONTRIBUTING.md inclusion criteria still consistent with the new Tier 1 entries

## Sources index (verified 2026-04-30 HKT)

See `timeline-additions.md` and `attribution-fixes.md` for complete source URL tables.

## What this PR does NOT do

- No diagram update (timeline.png, ecosystem-map.png stay as-is)
- No translation file changes
- No README change
- No CHANGELOG file (repo doesn't appear to have one; can be added in a follow-up if desired)
- Does not implement the 3 `[unable-to-attribute]` decisions — those are listed for Kenneth's review-and-decide pass

## Reviewer focus areas

1. **Tier 2 rejections** — confirm that GPT-5.5, Sonnet 4.6, Gemini 3.1, Cowork GA, MCP Registry v1.2 are correctly excluded. If reviewer feels any are structural, promote them.
2. **Microsoft–OpenAI restructure entry** — borderline business-news vs. distribution-model. Drop if it skews the timeline's tone.
3. **Three `[unable-to-attribute]` items** — IMPACT framework (Fix 3), Heinrich engagement metrics (Fix 5), Anthropic "Multi-Agent Systems" report (Fix 10). Each needs a soften-or-drop-or-search-more decision.

🤖 Generated with overnight prep agent on 2026-04-30 HKT
