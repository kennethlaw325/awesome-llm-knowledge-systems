# Review checklist — Loop Engineering wave (Chapter 13)

**State as of 2026-07-14 HKT:** branch `ch13-loop-engineering` (created from master HEAD). Changes committed in four logical chunks; PR not yet opened (orchestrator handles push/PR). Planning docs live in `docs/ch13-loop-engineering/`.

This wave adds one new chapter and integrates it across the guide. Every quote and number was checked verbatim against the verified-sources record used at drafting time; the term is roughly five weeks old (named June 2026) and is framed throughout as *emerging and contested*, not a settled fourth generation.

---

## Step 1 — Read the proposals

1. `chapter-outline.md` — the section map of Chapter 13 (13.1–13.8 + Sources), with the primary source behind each beat
2. `exclusions.md` — claims that circulated with the term but were dropped or corrected after primary-source checking, with one-line reasons
3. `PR-description.md` — the PR body

---

## Step 2 — Review the commits (4 chunks)

```bash
cd C:/Users/Kenneth/Claude/awesome-llm-knowledge-systems
git log --oneline master..ch13-loop-engineering
git diff --stat master..ch13-loop-engineering
```

Expected commits (oldest first):
1. Ch13 (new chapter) + Ch12 footer Next link
2. Ch01 fourth-generation section + Ch11 two timeline entries + glossary three terms
3. README + CHANGELOG + CITATION.cff
4. Planning docs (`docs/ch13-loop-engineering/`)

`translations/`, `docs/archive/`, and `docs/mid-july-2026/` must be untouched.

---

## Step 3 — New chapter (Ch13), sections checked off as drafted

- [x] 13.1 The week it got a name (June 2026) — Steinberger, Osmani, Cherny
- [x] 13.2 One floor above the harness — Osmani relation + 鱼皮 nesting/horse metaphor
- [x] 13.3 What a loop is made of — Osmani's five pieces + external state
- [x] 13.4 Generator vs evaluator — Rajasekaran + `/loop` / `/goal` / Routines / Codex primitives
- [x] 13.5 Production case: Stripe's minions (March 2026)
- [x] 13.6 Stacking loops — LangChain four rungs + Swyx's "loopcraft"
- [x] 13.7 The outer loop: what the human keeps — Osmani "Own the Outer Loop"
- [x] 13.8 Adoption signal — @ClaudeDevs, 鱼皮, Snorkel Continual Learning Bench
- [x] Sources section (every canonical URL used)
- [x] Footer: Previous → Ch12 (no Next)

## Step 4 — Integrations checked off as done

- [x] Ch01 — "An Emerging Fourth Generation? Loop Engineering" section (after Coexistence, before Sources) + 3 sources
- [x] Ch11 — June 7 entry (after June 2, before June 8); June 16 entry (after June 12, before June 17); Sources appended
- [x] glossary.md — Loop Engineering (L), Generator-Evaluator Split (G), Outer Loop (O), each in correct alpha slot
- [x] README — Evolution ASCII 4th column (emerging); nested-boxes note; TL;DR clause; ToC row 13; Which-Path persona line; What's-new 3 bullets on top; footer left at "July 2026"
- [x] Ch12 — footer Next link to Ch13
- [x] CHANGELOG — 2026-07-14 Loop Engineering entry (above the mid-July wave entry) with caveats
- [x] CITATION.cff — "three generations (and an emerging fourth)"; chapter count → thirteen

## Step 5 — Style + verification gates

- [x] Chapter/timeline/glossary body uses ASCII ` --- `, never em-dash (verified by grep)
- [x] No excluded/banned claim appears in the diff (verified by grep — see `exclusions.md`)
- [x] Every quote verbatim per the verified-sources record; contested/spoken quotes flagged in-text
- [x] All new relative links resolve against the file tree
