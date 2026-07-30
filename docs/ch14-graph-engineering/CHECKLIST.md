# Review checklist — Graph Engineering wave (Chapter 14 + late-July refresh)

**State as of 2026-07-30 HKT:** branch `ch14-graph-engineering` (created from master HEAD). Files edited only; no commits yet (orchestrator commits after review and handles push/PR). Planning docs live in `docs/ch14-graph-engineering/`.

This wave adds one new chapter, a late-July refresh across five existing chapters, and the connective tissue (README / glossary / CHANGELOG / CITATION / Ch01 / Ch13). The term "graph engineering" is roughly two weeks old (crystallized after July 17-18, 2026) and is framed throughout as *emerging and contested* — a claim under test with an explicit September 2026 survival gate, not a settled fifth generation.

---

## Step 1 — Read the proposals

1. `chapter-outline.md` — the section map of Chapter 14 (14.1–14.7 + Sources), with the primary source behind each beat
2. `exclusions.md` — the four excluded claims (see `exclusions.md`) plus author drops and corrections, with one-line reasons
3. `PR-description.md` — the draft PR body

---

## Step 2 — Review the changes

```bash
cd C:/Users/Kenneth/Claude/awesome-llm-knowledge-systems
git status
git diff --stat
```

Expected file groups (three agents, disjoint ownership):
1. CHAPTER: `chapters/14-graph-engineering.md` + `docs/ch14-graph-engineering/`
2. REFRESH: `chapters/02-knowledge-layer.md`, `04-harness-engineering.md`, `07-mcp.md`, `09-china-ecosystem.md`, `11-timeline.md`
3. CONNECT: `README.md`, `glossary.md`, `CHANGELOG.md`, `CITATION.cff`, `chapters/01-evolution.md`, `chapters/13-loop-engineering.md`

`translations/`, `diagrams/`, `CONTRIBUTING.md`, `LICENSE`, `docs/archive/`, `docs/mid-july-2026/`, and `docs/ch13-loop-engineering/` must be untouched.

---

## Step 3 — New chapter (Ch14), sections checked off as drafted

- [x] 14.1 The tweet that started it (July 17-18, 2026) — Steinberger via secondary sources; dated essay-wave list; view-count conflict reported as conflict
- [x] 14.2 What graph engineering claims to be — org/work graph (explainx), loops-supervising-loops + anchors (Perez), governed topologies (TrueFoundry/Eigent)
- [x] 14.3 The pushback — LangChain "3 years" counter carried as adoption signal AND skeptical source; Tony Bai buzzword warning; absence-of-evidence paragraph
- [x] 14.4 Not knowledge graphs — TrueFoundry disambiguation quote + side-by-side table; Ch02 cross-ref
- [x] 14.5 Where it sits — MarkTechPost stacked-layers reading vs the deflationary refactor-of-the-fourth reading; explicitly unresolved
- [x] 14.6 The Chinese-ecosystem echo — 图工程; Tony Bai + 36kr verified; CSDN/alphalab flagged titles-only
- [x] 14.7 Should you care yet? — label/problems split + September 2026 survival gate with concrete watch list
- [x] Sources section (9 bullets; Steinberger with no URL, cited via secondaries only)
- [x] Footer: Previous → Ch13 (no Next)

## Step 4 — Integrations (owned by REFRESH / CONNECT agents; verify before merge)

- [ ] Ch11 — six timeline entries in chronological slots (graph-engineering naming week; Opus 5 July 24; MCP spec July 28; Kimi K3 July 17; WAIC/WAICO July 17; Fable 5 resolution July 18) + Sources appended (REFRESH)
- [ ] Ch07 — dated subsection on the 2026-07-28 finalized MCP spec (REFRESH)
- [ ] Ch04 — minimal dated Opus 5 note (REFRESH)
- [ ] Ch09 — Kimi K3 + WAIC/WAICO additions (REFRESH)
- [ ] Ch02 — GraphRAG-vs-graph-engineering disambiguation line + 2026 graph-tooling-consolidation sub-section (REFRESH)
- [ ] Ch01 — emerging-generation section extended with the hedged July graph claim + sources (CONNECT)
- [ ] Ch13 — footer Next link to Ch14 + one editorial pointer sentence (CONNECT)
- [ ] glossary.md — Graph Engineering, Org Graph / Work Graph, Anchor (Perez sense) in alpha slots (CONNECT)
- [ ] README — What's-new bullets, TL;DR clause, Which-Path row, Evolution ASCII fifth column (contested), ToC row 14 (CONNECT)
- [ ] CHANGELOG — 2026-07-30 entry with explicit Caveats clause (CONNECT)
- [ ] CITATION.cff — chapter count → fourteen (CONNECT)

## Step 5 — Style + verification gates

- [x] Ch14 body uses ASCII ` --- ` / ` -- ` only; zero Unicode em/en dashes (verified by script: em-dash 0, en-dash 0)
- [x] None of the four excluded claims (see `exclusions.md`) appears in Ch14 or its docs outside `exclusions.md`
- [x] Every URL in Ch14 comes from the verified research record; the unverified X link is not used
- [x] View counts and the tweet date follow the numeric-claim discipline ("reported at 2.6M by 36kr"; "July 17-18")
- [x] Ch14 length inside the 160–210 target
- [x] Ch14 relative footer link resolves (`13-loop-engineering.md` exists)
- [ ] Post-integration: grep the full diff for em-dashes in chapters/glossary and for excluded terms (run after REFRESH + CONNECT land)
