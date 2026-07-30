# Chapter 13: Loop Engineering -- Designing the System That Prompts the Agent

> **In one sentence:** Loop engineering is the practice of building the system that prompts the agent for you --- so you stop hand-driving each turn and start designing the loop that runs, checks, and feeds itself.
>
> **Why it matters:** It is the newest and least-settled layer in this guide's evolution story, and the one most likely to shape how autonomous agent work actually gets scheduled, verified, and reviewed over the next year.

This is the shortest-lived idea in this guide. (It held that title for six weeks: in late July 2026 the same playbook produced a claim of a next layer above the loop, graph engineering, covered in [Chapter 14](14-graph-engineering.md).) The term "loop engineering" is roughly five weeks old at the time of writing: it was named in early June 2026, spread through practitioner blogs, podcasts, and X within days, and has no academic literature behind it yet. What follows is deliberately hedged. Where a claim rests on a spoken podcast quote transcribed three different ways, or on a viral post that named nothing, this chapter says so. The goal is to describe an emerging frame accurately, not to certify it as a settled generation.

The frame is worth describing because it is doing real work in practitioner discourse: it gives a name to a shift that harness engineering (Chapter 4) implied but did not isolate --- the move from *prompting an agent* to *designing the system that prompts the agent*. Whether that deserves its own layer or is simply harness engineering with a scheduler attached is exactly the open question this chapter leaves open.

This chapter covers where the term came from, how its proponents relate it to the harness, what a loop is made of, the generator-evaluator split that keeps loops honest, one large production case, the stacked-loop framing, the judgment the human is told to keep, and the early signals of adoption --- with the contested parts flagged throughout.

---

## 13.1 The Week It Got a Name (June 2026)

The catalyst was a single post. On June 7, 2026, **Peter Steinberger** (@steipete) --- creator of **OpenClaw**, which Y Combinator described as having gone "from a weekend project to the most-starred software repo on GitHub in under 5 months, with 346k+ stars," overtaking React, and who is now at OpenAI --- wrote:

> Here’s your monthly reminder that you shouldn’t be prompting coding agents anymore.
>
> You should be designing loops that prompt your agents.

The post has drawn **8.4M+ impressions as of mid-July 2026**. It named nothing: Steinberger did not use the phrase "loop engineering," and the words appear nowhere in his text. The naming came from others responding to the idea he had catalyzed.

The same day, **Addy Osmani** (Google) published the essay that gave the practice its name (*Loop Engineering*, addyosmani.com/blog/loop-engineering/, June 7; syndicated on O'Reilly Radar June 22). His definition is the one the rest of the discourse quotes:

> Loop engineering is replacing yourself as the person who prompts the agent. You design the system that does it instead.

The same shift shows up from inside a frontier lab. **Boris Cherny**, creator and head of Claude Code at Anthropic, framed his own workflow the same way on a mid-2026 podcast. Per the most-cited transcription of the Lenny's Podcast interview:

> I don't prompt Claude anymore. I have loops running that prompt Claude and figuring out what to do. My job is to write loops.

That quote needs a caveat, and it is the kind of caveat this chapter exists to make. It is a *spoken* line, transcribed inconsistently across outlets (some cite the Acquired podcast rather than Lenny's), and no canonical verbatim text or full transcript is available. The substance --- Cherny no longer hand-prompts, but writes loops that prompt Claude and decide the next action --- is corroborated across multiple secondary sources; the exact words are not fixed.

Put together, the week of June 7 produced a catalyst (Steinberger), a name and definition (Osmani), and an insider echo (Cherny). What it did not produce is consensus. The term crystallized in practitioner discourse within weeks, but reception is split between readers who call it a genuine shift and readers who call it premature --- a rebranding of scheduling, or "the harness with a cron job." No peer-reviewed work uses the term. This guide treats loop engineering as an emerging, contested frame (see Chapter 1's fourth-generation section), which is why every load-bearing claim below is tied to a primary source and the gaps are named rather than filled.

---

## 13.2 One Floor Above the Harness

The cleanest definitional move its proponents make is to place the loop directly above the harness of Chapter 4. Osmani states the relation outright:

> Loop engineering sits one floor above the harness.

His mental model of what a loop *is* keeps the harness as the building block: the loop is the harness that "runs on a timer, it spawns little helpers, and it feeds itself." He is explicit that this extends earlier work, not replaces it --- he "wrote before about the cousin of this, agent harness engineering, which is making the environment one single agent runs inside."

The Chinese developer **程序员鱼皮** (liyupi) gives the most structural version of the relationship. In his June 16 guide (codefather.cn), he arranges prompt technique, context management, harness building, and the loop as **層層包含** --- layer-by-layer nested:

> 这四者是层层包含的关系。提示词技巧、上下文管理、Harness 搭建，这些能力在 Loop 里面全都要用上。

(The four are nested; prompt technique, context management, and harness building are all used *inside* the loop.) This is the same nested-layers logic Chapter 1 applies to prompt → context → harness, extended by one outer box. It is worth being precise about attribution: 鱼皮 is repackaging and structuring existing terms for a Chinese-dev audience, not coining them --- "harness engineering" and "loop engineering" trace to Claude Code and Cherny discourse.

His horse metaphor draws the harness/loop line as sharply as anyone has:

> 如果把 AI 比作一匹马，Harness 就是你给马装上的缰绳、马鞍和围栏，然后你骑在马上手动驾驭它。

(If AI is a horse, the harness is the reins, saddle, and fence you put on it --- then you ride and steer it by hand.)

> 而 Loop 呢，是你设定好一条巡逻路线后，不用上马，让马自己按路线一圈一圈地跑。

(The loop is when you set a patrol route, then *don't mount* --- the horse runs the route itself, lap after lap.)

That metaphor encodes the single distinction that keeps loop engineering from collapsing into "cron for agents": **a loop is not a scheduler.** A scheduler fires on time. A loop fires on time *and then reads the current state to decide what to do this round.* The runtime decision-maker --- the part that inspects CI status, open issues, or the last run's leftovers before choosing an action --- is exactly what a cron entry does not have. A loop is a scheduler plus a state-reading agent that re-decides each pass. (Cross-reference: Chapter 1, "The Key Insight: Coexistence, Not Replacement.")

---

## 13.3 What a Loop Is Made Of

Osmani's essay supplies the most concrete inventory. His section is headed **"The five pieces, and then notes"** --- and the count matters, because it is easy to inflate. There are *five pieces plus external state*, not six co-equal building blocks:

- **Automations** --- the trigger that fires the loop (a schedule, an event).
- **Worktrees** --- isolated working copies so parallel agents do not collide.
- **Skills** --- the reusable capability bundles of Chapter 5.
- **Connectors (MCP)** --- the tool and data reach of Chapter 7.
- **Sub-agents** --- the little helpers a run spawns.

The "then notes" is **external state / memory** --- a markdown file or a Linear board that persists progress between runs. It is not a sixth co-equal block; it is the substrate the five pieces write to and read from.

His worked example is a morning triage loop, and it is useful precisely because every piece maps to one of the five. An **automation** fires every morning. A triage **skill** reads CI failures, open issues, and recent commits. Isolated **worktrees** host one **sub-agent** that drafts a fix and a second sub-agent that reviews it. **Connectors** open the PRs and update the tickets. Unresolved items surface in a triage inbox, and a **state file** persists progress so the next morning's run continues rather than restarts. The state file is the load-bearing part: without it, the loop has no memory of yesterday and every run starts cold.

---

## 13.4 Generator vs Evaluator

A loop that prompts itself inherits a hard problem: *who checks the work?* If the agent that produces the change also grades it, the loop optimizes toward self-congratulation. The most-cited primary treatment predates the naming week, which is itself telling --- the practice ran ahead of the label. **Prithvi Rajasekaran**'s *"Harness design for long-running application development"* (anthropic.com/engineering/harness-design-long-running-apps, March 24, 2026) documents the failure mode directly: asked to evaluate their own output, agents "tend to respond by confidently praising the work" and "reliably skew positive when grading their own work."

His fix borrows a structure from adversarial training:

> Taking inspiration from Generative Adversarial Networks (GANs), I designed a multi-agent structure with a generator and evaluator agent.

The asymmetry is the whole insight, and it is why the split is worth the extra agent:

> Tuning a standalone evaluator to be skeptical turns out to be far more tractable than making a generator critical of its own work.

Crucially, the evaluator verifies *behavior*, not the diff. In Rajasekaran's design it "used the Playwright MCP to click through the running application the way a user would, testing UI features, API endpoints, and database states," and it "would navigate the page on its own, screenshotting and carefully studying the implementation before scoring each criterion and writing a detailed critique." Reading the code is not verification; running it is.

This generator-evaluator split is now visible in the shipping loop-control primitives, and the important distinction among them is *how a loop knows when to stop*:

- **`/loop`** (Claude Code v2.1.71) reruns a prompt or slash command on a recurring interval --- the changelog line is "Added `/loop` command to run a prompt or slash command on a recurring interval (e.g. `/loop 5m check the deploy`)." Recurring tasks expire seven days after creation; the task fires one final time, then deletes itself.
- **`/goal`** (Claude Code v2.1.139+) runs *until a condition holds*: "a small fast model checks whether the condition holds" (defaulting to Haiku), a separate evaluator that checks the condition "after every turn, so completion is decided by a fresh model rather than the one doing the work." Underneath, `/goal` is "a wrapper around a session-scoped prompt-based Stop hook."
- **Cloud Routines** run "on Anthropic-managed cloud infrastructure, so they keep working when your laptop is closed"; the minimum interval is one hour, and each run starts from a fresh clone.
- **Codex scheduled automations** support daily and weekly schedules, or a custom cadence set through an RFC 5545 recurrence rule (RRULE).

The `/loop`-versus-`/goal` contrast is the generator-evaluator split surfaced as product design. `/loop` is *interval rerun* --- fire again on the clock, regardless of state. `/goal` is *condition-judged termination* --- a second, independent model decides when the work is done. One repeats; the other adjudicates. A serious loop usually needs both: a trigger to run and an evaluator to know when to stop.

---

## 13.5 Production Case: Stripe's Minions (March 2026)

The largest disclosed loop running in production is Stripe's **"minions."** **Steve Kaliski**, a Stripe engineer, described the system on the *"How I AI"* podcast (hosted by Claire Vo) in March 2026; Stripe's own developer blog documents the internals in a two-part *Minions* write-up. (The episode day is disputed across secondary sources, so only the month is stated here.)

The headline number is the volume of unattended output. Kaliski says Stripe is "landing about 1,300 PRs that have no human assistance besides review per week." Stripe's blog states the same figure conservatively: "over a thousand pull requests merged each week at Stripe are completely minion-produced," and while they are "human-reviewed," they "contain no human-written code."

A minion is triggered from Slack --- either by adding a specific emoji reaction or by tagging the Slack app. In Stripe's words, "by tagging our Slack app, engineers can kick off a minion directly from the thread discussing a change."

For this guide, the load-bearing detail is *where Stripe draws the deterministic/probabilistic boundary.* Context assembly happens **before** the model runs, and it is deterministic: "We deterministically run relevant MCP tools over likely-looking links before a minion run even starts, to better hydrate the context." Only then does the probabilistic part begin. The core agent loop is a fork of Block's open-source **Goose** --- "the core agent loop runs on a fork of Block's coding agent goose ... which we forked early on." Execution is sandboxed in Stripe **devboxes**; per Stripe's dev blog (not the podcast), "a Stripe devbox is an AWS EC2 instance," treated as "cattle, not pets" --- standardized and disposable rather than bespoke and long-lived.

The framework beat: the reliability does not come from a smarter model. It comes from *boundary placement* --- deterministic context hydration before probabilistic generation --- and from the human moving out of the write path and into the review path. Every minion PR is still reviewed by an engineer. The loop scaled the writing; it did not remove the human, it relocated them.

---

## 13.6 Stacking Loops

**LangChain**'s *"The Art of Loop Engineering"* (Sydney Runkle, June 16, 2026) is the clearest attempt to give the layer an internal structure. It starts from the base case:

> The core agent algorithm is simple: give the LLM context and let it call tools in a loop until it's done.

From there it stacks four rungs. The page's own headings mix "Loop" and "Level" labeling, and are reproduced here as written --- **"Loop 1: The Agent," "Level 2: Verification loop," "Level 3: Event driven loop," "Level 4: Hill climbing loop."** The progression:

1. **Loop 1: The Agent** --- the base tool-calling loop, context in, tool calls until done.
2. **Level 2: Verification loop** --- an independent check on the agent's output, the generator-evaluator split of §13.4 applied as a rung.
3. **Level 3: Event driven loop** --- the loop fires on real-world events, not only on an interval or a human's push.
4. **Level 4: Hill climbing loop** --- a self-improvement loop, where the system gets better over successive runs.

One precision note, because secondary coverage overstates it: the page frames the fourth rung as *self-improvement over runs*, not as a system that rewrites its own harness. The stronger claim is not in the source. Runkle also borrows the term **"loopcraft"** --- but attributes it to Swyx, citing his piece on "loopcraft: the art of stacking loops." The coinage is Swyx's, quoted by LangChain, not LangChain's own.

---

## 13.7 The Outer Loop: What the Human Keeps

If §13.1--13.6 describe the loop the agent runs, Osmani's follow-up describes the loop the human is told to keep. *"Own the Outer Loop"* (addyo.substack.com/p/own-the-outer-loop) was announced on X on July 8, 2026 (the Substack copy carries a July 9 byline). Its split: agents now run the **inner execution loop** --- investigate, implement, test/verify, report --- while the engineer holds the **outer loop**. His thesis line is blunt:

> Engineers own the outer loop.

The outer loop is the judgment that is not delegated, structured as three pillars in his exact terms --- **Quality**, **Verdict**, and **Answerability**. Quality is the back-pressure of checks that run before agents act. **Verdict** is "the final decision we make before work enters our dependent system." **Answerability** is "the guarantee that if someone asks, I can explain why." (His term is the singular *Verdict*, and "quality bar" is not his phrase --- the pillar is simply *Quality*.) The reasoning behind keeping these human:

> An agent can write it. But before it reaches users, someone must explain why it should exist, why it's safe enough to be part of production, and what they will do when it is wrong.

He names three failure modes of over-delegating the outer loop: **cognitive debt** (the "erosion of your understanding and memory of how to solve problems"), **cognitive surrender** ("blindly accepting what AI gives you"), and the **orchestration tax** (the drag of spinning up more agents than your judgment can actually cover). These are the costs of pressing "go" without staying the engineer.

The through-line back to the June 7 essay is its closing instruction, which reads as a warning against exactly that:

> Build the loop. But build it like someone who intends to stay the engineer, not just the person who presses go.

And the line that undercuts any assumption a loop is self-justifying:

> Two people can build the exact same loop and get completely opposite results.

The loop is only as good as the outer loop around it. That is the honest center of the whole frame.

---

## 13.8 Adoption Signal

Three markers show the frame spreading past its originators. Each is held to what is verifiable, and the overclaims that circulated alongside them are left out.

**Vendor.** Anthropic's official developer account **@ClaudeDevs** published the X Article *"Getting started with loops"* on July 6, 2026 (roughly **6.0M impressions and 38K+ bookmarks** as of mid-July). The material teaches the agentic loop directly --- "Every prompt you send starts a manual loop with you directing each turn. Claude gathers context, takes action, checks its work, repeats if needed, and responds" --- and walks through turn-based, goal-based (`/goal`), and time-based (`/loop`, `/schedule`) loops. The editorial nuance is worth keeping: the X article's own title says *"loops,"* not *"loop engineering."* The "loop engineering" label appears in the canonical Claude blog mirror's framing (claude.com/blog/getting-started-with-loops), not in the product vocabulary itself. A vendor teaching loops is a weaker signal than a vendor adopting the term --- and only the weaker one is verified.

**China.** 鱼皮's June 16 保姆级 ("nanny-level") guide is the entry point into Chinese-dev discourse. Its title --- 「提示词工程已死，Loop Engineering 称王！保姆级教程 + 项目实战」 ("Prompt engineering is dead, Loop Engineering reigns! Nanny-level tutorial + project practice") --- leads with 已死 ("is dead"), and that hook is hype the body itself walks back: the guide's own 層層包含 argument (§13.2) is that prompt technique is *used inside* the loop, not killed by it. As a rough reach proxy, his GitHub account shows **23.9k followers**. (Larger total-following figures circulate but were not verifiable against a primary source, so they are omitted.)

**Memory and eval.** The sub-problem loops depend on most --- cross-session state that survives between runs --- is now separately benchmarked. Snorkel's **Continual Learning Bench** (arXiv 2606.05661; Snorkel AI / UC Berkeley SkyRL / UW-Madison) factors results into agent, memory system, and task. On it, agent systems using **Fable as the memory backbone outperformed those built on Opus or Sonnet** (Snorkel's Benchtalks interview; a qualitative finding --- the arXiv paper's model roster is Opus 4.7 / Sonnet 4.6 / Gemini 3.1 Pro / Gemini 3 Flash / GPT-5.4, and no numeric score is attached to Fable). At launch, best-in-class systems reached about **25% normalized gain**, with in-context learning leading the leaderboard. The signal is not the number; it is that *which memory backs the loop* is now a measured axis.

Five weeks after it got a name, loop engineering has a definition, a stated relation to the harness, a large production case, a framework vendor's curriculum, a Chinese-mainstream guide, and a vendor's own loops material. It does not have academic literature, settled reception, or agreement that it is a genuine fourth generation rather than harness engineering with a scheduler and a state file. This guide tracks it as emerging, not settled --- and Osmani's own caution, that two people can build the same loop and get opposite results, is the fairest summary of why.

---

## Sources

- Steinberger, Peter (@steipete). Post catalyzing the "loops, not prompts" framing (June 7, 2026): [https://x.com/steipete/status/2063697162748260627](https://x.com/steipete/status/2063697162748260627) --- 8.4M+ impressions as of mid-July 2026; the post itself does not use the phrase "loop engineering."
- Osmani, Addy. "Loop Engineering" (June 7, 2026): [https://addyosmani.com/blog/loop-engineering/](https://addyosmani.com/blog/loop-engineering/); syndicated on O'Reilly Radar (June 22, 2026): [https://www.oreilly.com/radar/loop-engineering/](https://www.oreilly.com/radar/loop-engineering/) --- the naming essay; definition, "one floor above the harness," the five pieces, morning-triage worked example.
- Osmani, Addy. "Own the Outer Loop" (announced on X July 8, 2026; Substack byline July 9, 2026): [https://addyo.substack.com/p/own-the-outer-loop](https://addyo.substack.com/p/own-the-outer-loop) --- inner vs outer loop; Quality / Verdict / Answerability; cognitive debt, cognitive surrender, orchestration tax.
- Cherny, Boris. "Head of Claude Code: what happens next" interview, Lenny's Podcast / Lenny's Newsletter (mid-2026): [https://www.lennysnewsletter.com/p/head-of-claude-code-what-happens](https://www.lennysnewsletter.com/p/head-of-claude-code-what-happens) --- the "I don't prompt Claude anymore ... my job is to write loops" line; a spoken quote transcribed inconsistently across outlets, cited here with that caveat.
- Rajasekaran, Prithvi. "Harness design for long-running application development," Anthropic Engineering (March 24, 2026): [https://www.anthropic.com/engineering/harness-design-long-running-apps](https://www.anthropic.com/engineering/harness-design-long-running-apps) --- generator/evaluator (GAN-inspired) split; skeptical standalone evaluator; Playwright-MCP behavioral verification.
- Runkle, Sydney. "The Art of Loop Engineering," LangChain blog (June 16, 2026): [https://www.langchain.com/blog/the-art-of-loop-engineering](https://www.langchain.com/blog/the-art-of-loop-engineering) --- four stacked rungs ("Loop 1: The Agent" / "Level 2/3/4"); "loopcraft" attributed to Swyx.
- Kaliski, Steve. Stripe "minions," on *How I AI* with Claire Vo (March 2026); Stripe developer blog, *Minions* (Parts 1 & 2): [https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents](https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents) --- ~1,300 minion PRs/week (human-reviewed, no human-written code); deterministic MCP pre-hydration; Goose fork; devbox = EC2, "cattle, not pets" (dev blog).
- 程序员鱼皮 (liyupi). 「提示词工程已死，Loop Engineering 称王！保姆级教程 + 项目实战」, codefather.cn (June 16, 2026): [https://www.codefather.cn/post/2066793761979092994](https://www.codefather.cn/post/2066793761979092994) --- 層層包含 nesting; horse/rider metaphor; GitHub @liyupi 23.9k followers.
- Anthropic (@ClaudeDevs). X Article "Getting started with loops" (July 6, 2026): [https://x.com/ClaudeDevs/status/2074208949205881033](https://x.com/ClaudeDevs/status/2074208949205881033); canonical mirror: [https://claude.com/blog/getting-started-with-loops](https://claude.com/blog/getting-started-with-loops) --- ~6.0M impressions / 38K+ bookmarks (mid-July); teaches "loops," the "loop engineering" label is the blog mirror's framing.
- Claude Code product docs: `/loop` and scheduled tasks [https://code.claude.com/docs/en/scheduled-tasks](https://code.claude.com/docs/en/scheduled-tasks) (v2.1.71; 7-day recurring-task expiry); `/goal` [https://code.claude.com/docs/en/goal](https://code.claude.com/docs/en/goal) (v2.1.139+; fresh-model condition check; prompt-based Stop hook wrapper); Cloud Routines [https://code.claude.com/docs/en/routines](https://code.claude.com/docs/en/routines) (Anthropic-managed infra; 1-hour minimum; fresh clone per run).
- Codex scheduled automations (ChatGPT/Codex docs): [https://learn.chatgpt.com/docs/automations](https://learn.chatgpt.com/docs/automations) --- daily/weekly schedules plus custom RFC 5545 RRULE cadence.
- Snorkel AI / UC Berkeley SkyRL / UW-Madison. "Continual Learning Bench," arXiv 2606.05661 (June 2026): [https://arxiv.org/abs/2606.05661](https://arxiv.org/abs/2606.05661) --- factors agent / memory system / task; qualitative Fable-backbone finding from Snorkel's Benchtalks interview; ~25% best-in-class normalized gain at launch, in-context learning leading.

---

*Previous: [Chapter 12: Local Models for Knowledge Engineering](12-local-models.md)*

*Next: [Chapter 14: Graph Engineering](14-graph-engineering.md)*
