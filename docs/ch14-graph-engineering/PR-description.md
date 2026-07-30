# PR: Chapter 14 — Graph Engineering (contested fifth layer) + late-July 2026 wave

## Summary

Adds **Chapter 14: Graph Engineering** and a late-July refresh across the guide. "Graph engineering" is the July 2026 practitioner claim that the layer above loop engineering is the *graph* — the explicit wiring of which agents exist, who may delegate to whom, and how their loops supervise one another. The term is roughly **two weeks old**, has no academic literature, and is contested by the vendor best positioned to champion it (LangChain: three-year-old practice, new name) — so the chapter and every integration are framed as **a claim under test**, with an explicit September 2026 survival gate, each load-bearing claim tied to a primary source, and the gaps named in-text. The repo's generational spine becomes prompt -> context -> harness -> loop -> graph(?).

## What's in the chapter

- **14.1** the catalyst (Steinberger's July 17-18 post, cited only via fetched secondary sources; view-count conflict reported as a conflict) and the one-week essay wave
- **14.2** what the frame claims: org graph vs work graph (explainx), loops-supervising-loops + anchors (Perez), governed topologies (TrueFoundry, Eigent)
- **14.3** the pushback at full weight: LangChain's "3 Years of Graph Engineering with LangGraph" (a loop is just a directed, cyclic graph) and Tony Bai's buzzword warning
- **14.4** not knowledge graphs: the disambiguation from Ch02's GraphRAG ("what a system knows" vs "who the system is"), with a side-by-side table
- **14.5** fifth generation or refactor of the fourth — MarkTechPost's stacked-layers reading held open against the deflationary one; unresolved by design
- **14.6** the Chinese-ecosystem echo (图工程): Tony Bai and 36kr verified; CSDN pieces flagged as titles-only
- **14.7** practitioner guidance + the survival gate (does the term still circulate by September 2026?)

## Also in this wave (late-July refresh)

- **Ch11 timeline** — graph-engineering naming week (July 17-22); Claude Opus 5 (July 24); MCP 2026-07-28 spec finalized; Kimi K3 (July 17); WAIC 2026 / WAICO founding (July 17); Fable 5 subscription resolution (July 18)
- **Ch07** — dated subsection on the finalized MCP spec (stateless core, auth hardening, extensions framework)
- **Ch04** — dated Opus 5 note (effort levels, cache-safe tool swapping)
- **Ch09** — Kimi K3 + WAIC/WAICO
- **Ch02** — graph-engineering disambiguation cross-ref + 2026 graph-tooling consolidation (graphrag v3.x, LightRAG, graphiti/cognee agent-memory category, GraphRAG-Bench at ICLR 2026, KAG dormancy)

## Files changed

- `chapters/14-graph-engineering.md` — new chapter (14.1–14.7 + Sources)
- `chapters/02-knowledge-layer.md`, `04-harness-engineering.md`, `07-mcp.md`, `09-china-ecosystem.md`, `11-timeline.md` — refresh wave
- `chapters/01-evolution.md` — emerging-generation section extended (hedged) + sources
- `chapters/13-loop-engineering.md` — footer Next link + one editorial pointer to Ch14
- `glossary.md` — Graph Engineering, Org Graph / Work Graph, Anchor (Graph Engineering), Client ID Metadata Documents (CIMD; defined by Ch07's new spec section), plus a one-line fix to the existing MCP entry reflecting spec finalization
- `README.md` — What's-new bullets, TL;DR clause, Which-Path row, Evolution ASCII fifth column (contested), ToC row 14
- `CHANGELOG.md` — 2026-07-30 entry with caveats
- `CITATION.cff` — chapter count → fourteen
- `docs/ch14-graph-engineering/` — planning docs (this folder)

## Not touched

`translations/` (stale by policy — English leads, sync waves follow), `diagrams/` (ecosystem-map + timeline flagged "pending refresh" per existing convention), `CONTRIBUTING.md`, `LICENSE`, `docs/archive/`, `docs/mid-july-2026/`, `docs/ch13-loop-engineering/`.

## Verification

- Every date, number, name, and quote in Ch14 traceable to a verified source in the research record; the catalyst post is cited only through independently fetched secondary sources (the X link itself was unverified), and the chapter states how each of them carries it: verbatim (Perez, Thakker), linked only (LangChain, Perez), in Chinese translation (36kr, Tony Bai), paraphrased (Eigent).
- Numeric-claim discipline applied: tweet date written "July 17-18", with the range flagged in-text as a US-time hedge rather than a source split (every source that dates the post dates it July 18); view counts attributed to each source and described as snapshots at different times, never a bare number.
- The four excluded claims (see `exclusions.md`) are excluded everywhere except that file; see it for the full dropped/corrected list.
- Chapter body uses ASCII ` --- ` / ` -- ` only — zero Unicode em/en dashes (script-verified).
- Independently fact-checked and style-checked: an adversarial pass re-fetched every load-bearing URL and traced every quantifier to a source (9 findings fixed, incl. corrected source attributions for the catalyst post, the Kimi K3 leaderboard claim, and the Fable 5 resolution sourcing); a separate acceptance pass re-verified all fixes, 132 relative links, and the dash/exclusion greps.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
