# Chapter 13 outline — Loop Engineering

Section map for `chapters/13-loop-engineering.md`, with the primary source behind each beat. The chapter's editorial posture is constant: the term was named in June 2026, lives in practitioner discourse, has no academic literature yet, and is tracked as *emerging*, not a settled generation.

---

**Opening.** House template — title with ` -- ` subtitle, one-sentence / why-it-matters blockquote, honesty-first intro (the shortest-lived idea in the guide), "this chapter covers" line, then the sections.

**13.1 The week it got a name (June 2026).**
- Peter Steinberger (@steipete, creator of OpenClaw, now at OpenAI) — June 7 post that catalyzed the idea and named nothing; live impressions cited as a mid-July figure.
- Addy Osmani (Google) — same-day essay that supplied the definition; O'Reilly Radar syndication June 22.
- Boris Cherny (head of Claude Code, Anthropic) — "my job is to write loops," flagged as a spoken quote transcribed inconsistently.
- Honesty paragraph: crystallized in weeks, no peer-reviewed use, reception split (genuine shift vs premature).

**13.2 One floor above the harness.**
- Osmani's "one floor above the harness" relation to Ch04.
- 鱼皮 (liyupi) 層層包含 nesting and the horse/rider metaphor (harness = reins/saddle/fence you steer by hand; loop = set a patrol route, the horse runs it).
- The load-bearing distinction: a loop is a scheduler plus a state-reading, re-deciding agent — not a bare timer. Cross-ref Ch01 Coexistence.

**13.3 What a loop is made of.**
- Osmani's "five pieces, and then notes": automations, worktrees, skills, connectors (MCP), sub-agents, plus external state/memory. Five pieces plus state, not six co-equal blocks.
- His morning-triage worked example, mapped piece by piece.

**13.4 Generator vs evaluator.**
- Rajasekaran, "Harness design for long-running application development" (Anthropic, March 24 2026 — predates the naming week). Agents over-rate their own work; GAN-inspired generator/evaluator split; skeptical standalone evaluator; behavioral (Playwright-MCP) verification.
- Product primitives: `/loop` (interval rerun; v2.1.71; 7-day recurring expiry), `/goal` (run-until-condition, fresh model judges; v2.1.139+; prompt-based Stop hook), Cloud Routines (managed infra, 1-hour minimum, fresh clone), Codex scheduled automations (daily/weekly + RFC 5545 RRULE custom cadence). The `/loop` vs `/goal` split = interval rerun vs condition-judged termination.

**13.5 Production case: Stripe's minions (March 2026).**
- Steve Kaliski on "How I AI" (Claire Vo) + Stripe dev blog (Parts 1 & 2). ~1,300 PRs/week, human-reviewed, no human-written code; Slack emoji/tag trigger; deterministic MCP pre-hydration before the model; Goose fork; devbox = EC2, "cattle not pets" (dev blog, not podcast). Framework beat: reliability from deterministic/probabilistic boundary placement; human moves from writing to reviewing. Month precision only (episode day disputed).

**13.6 Stacking loops.**
- LangChain, "The Art of Loop Engineering" (Sydney Runkle, June 16 2026). Base agent algorithm quote; four rungs with the page's own mixed "Loop 1" / "Level 2/3/4" headings; fourth rung is self-improvement (not harness-rewriting); "loopcraft" attributed to Swyx, not LangChain.

**13.7 The outer loop: what the human keeps.**
- Osmani, "Own the Outer Loop" (announced X July 8 2026; Substack byline July 9). Inner (agent) vs outer (human) loop; three pillars Quality / Verdict / Answerability (his exact singular terms); failure modes cognitive debt / cognitive surrender / orchestration tax; closes on the June 7 "stay the engineer" line and the corrected "exact same loop … completely opposite results."

**13.8 Adoption signal.**
- Vendor: @ClaudeDevs "Getting started with loops" X Article (July 6 2026, ~6.0M impressions / 38K+ bookmarks), teaching "loops"; the "loop engineering" label is the Claude blog mirror's framing.
- China: 鱼皮's June 16 保姆级 guide (title flagged for its "已死" hook that the body walks back); GitHub 23.9k as reach proxy.
- Memory/eval: Snorkel Continual Learning Bench (arXiv 2606.05661) — qualitative Fable-backbone finding only, plus the ~25% best-in-class launch figure with in-context learning leading.
- Closing honesty paragraph.

**Sources.** Every canonical URL used, mirroring the Ch11 Sources style.

**Footer.** `*Previous: [Chapter 12: Local Models for Knowledge Engineering](12-local-models.md)*` — no Next (Ch13 is the last chapter).
