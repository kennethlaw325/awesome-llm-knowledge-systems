# PR: Chapter 13 — Loop Engineering (emerging fourth generation)

## Summary

Adds **Chapter 13: Loop Engineering** and threads it through the guide. "Loop engineering" is the June 2026 practitioner frame for *designing the system that prompts the agent* rather than prompting it by hand. The term is roughly five weeks old, has no academic literature behind it, and its status as a genuine fourth generation is contested — so the chapter and every integration are framed as **emerging**, not settled, with each load-bearing claim tied to a primary source and the gaps named in-text.

## What's in the chapter

- **13.1** the naming week (Steinberger's catalyst post, Osmani's naming essay, Cherny)
- **13.2** loop as "one floor above the harness" (Osmani; 鱼皮's nesting + horse metaphor); loop ≠ a bare scheduler
- **13.3** what a loop is made of (Osmani's five pieces plus external state; morning-triage example)
- **13.4** generator vs evaluator (Rajasekaran, GAN-inspired); `/loop` vs `/goal` and the other loop-control primitives
- **13.5** production case: Stripe's minions (March 2026), ~1,300 PRs/week
- **13.6** stacking loops (LangChain's four rungs; Swyx's "loopcraft")
- **13.7** the outer loop the human keeps (Osmani's Quality / Verdict / Answerability)
- **13.8** adoption signals (@ClaudeDevs, 鱼皮, Snorkel's Continual Learning Bench)

## Files changed

- `chapters/13-loop-engineering.md` — new chapter (13.1–13.8 + Sources)
- `chapters/12-local-models.md` — footer gains a Next link to Ch13
- `chapters/01-evolution.md` — "An Emerging Fourth Generation? Loop Engineering" section + 3 primary sources
- `chapters/11-timeline.md` — June 7 and June 16, 2026 entries in chronological slots + Sources appended
- `glossary.md` — Loop Engineering, Generator-Evaluator Split, Outer Loop
- `README.md` — Evolution ASCII 4th column (emerging), nested-boxes note, TL;DR clause, ToC row 13, a Which-Path persona line, What's-new bullets
- `CHANGELOG.md` — 2026-07-14 Loop Engineering entry with caveats
- `CITATION.cff` — "three generations (and an emerging fourth)"; chapter count → thirteen
- `docs/ch13-loop-engineering/` — planning docs (this folder)

## Not touched

`translations/` (12-count banners and 12-row ToCs there go stale — follow-up in the next translation wave), `docs/archive/`, `docs/mid-july-2026/`, and the historical `CHANGELOG.md` "twelve chapters" entry.

## Verification

- Every quote checked verbatim against the verified-sources record; contested/spoken quotes (Cherny) and disputed dates (Stripe episode day) flagged in-text.
- Chapter / timeline / glossary body uses ASCII ` --- `, never em-dash (grep-verified).
- No excluded/unverified claim appears in the diff (grep-verified); see `exclusions.md` for the dropped/corrected list and reasons.
- Four commits on `ch13-loop-engineering`; no push, no PR (orchestrator handles that).
