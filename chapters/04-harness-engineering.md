# Chapter 4: Harness Engineering -- Building the OS Around the Model

> **In one sentence:** A harness is everything around the AI model -- the rules, tools, safety checks, and workflows that make it actually useful.
>
> **Why it matters:** The AI model is like a powerful engine. Without a chassis, steering wheel, and brakes, it's useless. The harness is what turns raw AI into a product.

> "Every component in a harness encodes an assumption about what the model can't do on its own, and those assumptions are worth stress testing."
> -- Anthropic, "Building Effective Agents," 2025

> "模型從來都沒有長手。"
> -- Cab, on why tool use is a harness problem, not a model problem

An agent is not a model. An agent is a **model plus a harness** -- the surrounding system of prompts, tools, memory, control flow, evaluation logic, and orchestration code that turns raw inference into reliable behavior. The model is the engine; the harness is the vehicle. This chapter examines how practitioners design, evaluate, and evolve that vehicle.

**A note on intuition.** The metaphor that makes this concrete for many beginners is Cab's observation that "the model never literally grew hands." When a coding agent edits a file, it is not the model that edited the file -- it is the harness, triggered by a tool-call the model returned as text. Every capability we attribute to "the AI" is actually a capability of the harness surrounding the model. Strip the harness away and you get a model that can only produce text. Strip the model away and you get a harness that has nothing to route. Harness engineering is the discipline of deciding where that line sits and how the two halves cooperate.

---

## 4.1 Defining the Harness

The harness is everything that is not the model weights. It includes:

- System prompts and instruction templates
- Tool definitions and execution sandboxes
- Memory systems (short-term, long-term, episodic)
- Planning and decomposition logic
- Control flow (loops, conditionals, retry policies)
- Evaluation and self-correction mechanisms
- Safety guardrails and output validation
- Context assembly pipelines (Chapter 3)

A bare model API call with a user message is a trivial harness. A production agent with planning, multi-step tool use, self-evaluation, and persistent memory is a complex one. The discipline of harness engineering is about making principled decisions across this spectrum.

## 4.2 The Fowler-Bockeler Taxonomy

Martin Fowler and Birgitta Bockeler (ThoughtWorks, 2025) proposed a two-axis taxonomy for harness components that has become a standard reference:

**Axis 1: Direction**
- **Guides (Feedforward):** Components that shape behavior *before* the model acts. System prompts, few-shot examples, tool schemas, planning templates. These set the rails.
- **Sensors (Feedback):** Components that evaluate behavior *after* the model acts and feed results back. Output validators, test runners, human review, self-evaluation prompts. These correct the course.

**Axis 2: Mechanism**
- **Computational Controls:** Deterministic code -- regex validators, type checkers, schema enforcement, permission checks. These are hard constraints that never hallucinate.
- **Inferential Controls:** Another LLM call used to judge, route, or refine. Evaluator models, classifiers, summarizers. These are soft constraints that trade precision for flexibility.

The taxonomy reveals a design space. Most production harnesses use all four quadrants:

|  | Feedforward (Guides) | Feedback (Sensors) |
|--|---------------------|--------------------|
| **Computational** | Schema validation on tool inputs, permission allow-lists | Output format checks, test suite execution |
| **Inferential** | Planning prompts, few-shot routing | Self-evaluation, LLM-as-judge, critique chains |

The insight is that computational controls are cheaper and more reliable but less flexible, while inferential controls handle ambiguity but introduce their own failure modes. Good harness design uses computational controls wherever possible and reserves inferential controls for genuinely ambiguous decisions.

## 4.3 OpenAI Codex: Scale Through Harness

The OpenAI Codex blog post (2025) offered a striking data point: **three engineers plus the Codex agent system produced approximately one million lines of code across roughly 1,500 pull requests.** The productivity multiplier was not primarily about model quality -- it was about harness design.

The Codex harness included:
- Automated PR decomposition (breaking large tasks into reviewable units)
- Sandboxed execution environments for each task
- Automated test generation and validation
- Human review integration at PR boundaries
- Persistent context about repository structure and conventions

The lesson: at sufficient harness maturity, the model becomes a component in a larger production system rather than a standalone tool. The harness handles orchestration, quality control, and integration -- concerns that no amount of prompt engineering can address.

## 4.4 The IMPACT Framework

swyx (Shawn Wang) proposed the IMPACT framework as a systematic way to think about harness design dimensions:

- **Intent:** How does the system understand what the user actually wants? Includes intent classification, clarification dialogues, and goal decomposition.
- **Memory:** What does the system remember across turns and sessions? Includes conversation buffers, vector stores, structured knowledge bases, and user preference systems.
- **Planning:** How does the system break complex tasks into steps? Includes chain-of-thought prompting, explicit plan generation, and tree-search over action spaces.
- **Authority:** What is the system allowed to do? Includes permission systems, human-in-the-loop gates, and capability boundaries.
- **Control Flow:** How does execution proceed? Includes sequential chains, parallel fan-out, conditional branching, loops with exit conditions, and retry policies.
- **Tools:** What external capabilities does the system have access to? Includes function definitions, API integrations, code execution environments, and browser access.

IMPACT is useful as a design checklist. When building or reviewing a harness, walking through each dimension surfaces gaps. A system with strong Tools but weak Authority has a security problem. A system with strong Planning but no Memory cannot learn from its mistakes. The framework makes these imbalances visible.

## 4.5 The Meta-Harness Paper: Automating Harness Design

A joint paper from Stanford, MIT, and KRAFTON (March 2026) introduced the concept of the **meta-harness** -- a system that automatically optimizes harness configurations.

Their key finding: on the same benchmark, with the same base model, different harness configurations produced a **6x performance gap**. The best harness configuration for a given task was rarely obvious and often counterintuitive. Manual harness tuning was leaving enormous performance on the table.

The meta-harness approach treated harness parameters (number of retries, planning depth, tool selection strategy, memory window size, evaluation stringency) as a search space and used automated optimization to find high-performing configurations. The system could adapt the harness to different task types, different models, and different cost constraints.

This result has a profound implication: **harness engineering is not a solved design problem with known best practices -- it is an optimization problem with a large and poorly understood search space.** Teams that treat harness design as a one-time architecture decision are likely operating far below the frontier.

### From Research to Production: The Advisor Tool (April 2026)

The meta-harness finding was a research result. A month later, Anthropic shipped the first productised meta-harness pattern: the **Advisor Tool** (beta, `advisor-tool-2026-03-01`). The pattern pairs a faster executor model with a more capable advisor model. The executor handles the bulk of the work; when it hits a decision point, it calls `advisor()` and receives a strategic plan or course correction (typically 400-700 text tokens, 1,400-1,800 including thinking) without leaving the current API request.

The default configurations recommended by Anthropic are telling:

| Executor | Advisor | Intended use |
|----------|---------|--------------|
| Haiku 4.5 | Opus 4.6 | Step up in intelligence from Haiku-only |
| Sonnet 4.6 | Opus 4.6 | Match Opus-solo quality at Sonnet cost |
| Opus 4.6 | Opus 4.6 | Quality refinement on hardest tasks |

This is the 6x meta-harness gap translated into a pricing strategy. Instead of paying Opus rates for every token, you pay Sonnet rates for execution and Opus rates for the 1-2 advisor calls that actually shape the output. Anthropic's suggested prompting pattern is worth quoting because it codifies harness timing into a rule:

> "Call advisor BEFORE substantive work -- before writing, before committing to an interpretation, before building on an assumption. [...] On tasks longer than a few steps, call advisor at least once before committing to an approach and once before declaring done."

Several details from the documentation matter for practitioners:

- **Server-side sub-inference.** The advisor runs inside the same `/v1/messages` request. The executor emits a `server_tool_use` block, Anthropic runs a separate inference pass with the full transcript, and the result comes back as an `advisor_tool_result`. No extra round trips from your code.
- **Cache break-even at ~3 calls.** Enabling `caching` on the advisor tool writes the advisor's transcript to a 5-minute or 1-hour cache. The first call costs extra; payoff begins around the third call. Short tasks should leave caching off.
- **Conciseness prompt cuts output 35-45%.** A single instruction -- "The advisor should respond in under 100 words and use enumerated steps, not explanations" -- measurably reduces the advisor's largest cost driver without changing call frequency.
- **Explicit reconcile protocol.** When advisor advice conflicts with empirical evidence the executor has already gathered, Anthropic's system prompt tells the executor to make one more advisor call framed as "I found X, you suggest Y, which constraint breaks the tie?" rather than silently switching. This is a production-grade answer to the "should I trust the planner or the data" question that shows up whenever multiple roles disagree.

The Advisor Tool is important beyond its immediate utility. It is a signal that meta-harness thinking has moved from research curiosity to commercial primitive. The "same model, different harness, 6x gap" finding is no longer something you need a research team to exploit -- Anthropic exposes it as a tool call. Expect other labs to follow with their own advisor/executor pairings, and expect harness engineering job descriptions to start listing multi-model coordination as a core skill.

## 4.6 Anthropic's Three-Agent Architecture

Anthropic's research on multi-agent systems (2025-2026) converged on a recurring three-role architecture:

- **Planner:** Decomposes the task into subtasks, maintains the overall plan, and decides when to revise.
- **Generator:** Executes individual subtasks -- writing code, drafting text, calling tools.
- **Evaluator:** Assesses Generator output against task requirements and provides structured feedback.

This separation of concerns directly addresses two failure modes Anthropic identified:

**Context Anxiety.** When a single agent handles planning, execution, and evaluation, it tends to hedge. It qualifies its outputs, adds unnecessary caveats, and spends tokens on meta-commentary rather than task execution. Separating the roles lets each agent focus without carrying the cognitive load of the others.

**Self-Evaluation Bias.** Models are systematically poor at evaluating their own output. They exhibit a well-documented leniency bias -- rating their own work higher than an independent judge would. The three-agent architecture mitigates this by using a separate evaluator (potentially a different model or a differently prompted instance) that has no investment in the generated output.

A subtlety Anthropic emphasized: **evaluator calibration is itself a harness engineering problem.** An overly strict evaluator causes infinite revision loops. An overly lenient one passes low-quality work. The evaluator's threshold and criteria need tuning as carefully as the generator's instructions.

### The Claude Code Leak: An Empirical Look (March 31, 2026)

For most of 2025 the three-agent architecture was known through Anthropic's published research and inferred from behavior. On **March 31, 2026**, that changed. Anthropic accidentally published a 59.8MB source map inside the npm package **`@anthropic-ai/claude-code` v2.1.88**, exposing approximately **513,000 lines of unobfuscated TypeScript across 1,906 files**. Anthropic characterized the incident as a "human packaging error, not a security breach," but for the first time practitioners could read a production harness from a frontier lab directly.

A few findings from the leak that reshape how the community describes the architecture:

- **It is not literally "Planner / Generator / Evaluator."** Earlier community write-ups that mapped Claude Code onto the 4.6 three-role framing turned out to be a misreading of the research. The actual architecture is organized as a **three-layer "Self-Healing Memory"** system. The layers correspond to scratchpad / working state, compacted medium-term state, and durable project memory --- with explicit repair and reconciliation logic between layers.
- **`MEMORY.md` is an index, not a store.** Rather than a monolithic memory file, `MEMORY.md` acts as a **lightweight index of pointers** into more detailed notes. This is closer to a filesystem directory than a transcript, and it is what allows the memory layer to scale without ballooning context.
- **`KAIROS` is an autonomous daemon mode.** A feature flag called `KAIROS` is referenced **more than 150 times** across the source. It gates an autonomous daemon mode --- an unattended, long-running execution loop that goes well beyond the interactive REPL most users know.
- **44 hidden feature flags.** Beyond `KAIROS`, the source contains 44 feature flags for unreleased capabilities, suggesting that what ships publicly is a conservative subset of what the harness actually supports internally.

The practical upshot: the Planner / Generator / Evaluator split remains a useful conceptual taxonomy (and Anthropic's research papers still describe systems in those terms), but in production the architecture is layered around **memory and repair**, not around role decomposition alone. Harness engineering in 2026 increasingly means designing the memory layers and the transitions between them.

Two weeks after the leak, the same architecture took another step --- this time outward, away from the user's machine. With **Claude Code Routines** (April 14, 2026), Anthropic moved the orchestrator seat itself off the laptop and onto its own cloud, exposing scheduled, API, and GitHub-event triggers as first-class harness primitives. Read alongside the leak, this is a clear architectural rhetoric: the orchestrator is no longer modeled as a REPL the user babysits, but as a daemon that lives on Anthropic's substrate. The three-layer self-healing memory persists across triggers; the harness no longer needs the user's process to be alive for a loop to make progress. Whether you adopt Routines or not, the framing is now in the air: the orchestrator seat is a product surface, and "where the loop runs" is a design decision rather than a default.

## 4.7 The Harness as Moat

In early 2026, Meta acquired Manus for approximately $2 billion. Manus had no proprietary model. Its entire value was in the harness -- the orchestration logic, context engineering pipeline, tool integration layer, and operational infrastructure that turned commodity model APIs into a reliable agent product.

This acquisition crystallized what the industry had been discovering: **the harness is the moat.** Models are increasingly commoditized. The differentiator is how you wrap them -- what tools you provide, how you manage context, how you handle failure, how you orchestrate multi-step workflows, and how you evaluate quality.

The implication for practitioners is that harness engineering is not plumbing to get through on the way to the "real work" of model development. It *is* the real work for most production AI teams. By April 2026, "harness engineering" has entered the industry lexicon as a formal discipline, and the Claude Code leak provided the first empirical look at what a production harness actually contains.

## 4.8 Harness Maintenance: The Stress-Testing Imperative

Anthropic's most actionable insight may be the simplest: every harness component encodes an assumption about model limitations, and **those assumptions expire.**

When a harness was built around GPT-4-level capabilities, it might include:
- Explicit chain-of-thought prompting (because the model needed it)
- Aggressive output parsing (because the model was inconsistent with formats)
- Multi-step verification (because single-pass accuracy was insufficient)
- Detailed few-shot examples (because zero-shot performance was poor)

As newer models arrive with improved reasoning, instruction following, and output consistency, these components become **load-bearing walls that may no longer need to bear load.** They add latency, cost, and complexity without contributing to quality.

The discipline is periodic stress-testing: systematically disabling harness components to determine which ones are still necessary. If removing a planning step does not degrade performance, remove it. If the model now follows a format reliably without few-shot examples, drop them. If self-evaluation adds cost but not quality, eliminate it.

This is counterintuitive. Engineers naturally add safety mechanisms and resist removing them. But in harness engineering, unnecessary components are not free -- they consume context window space, add latency, increase cost, and create maintenance burden. A lean harness that matches the current model's capabilities outperforms an over-engineered one built for a weaker model.

The practical recommendation: when onboarding a new model, start by running your existing harness, then methodically strip components while measuring task performance. What remains is your true harness. What you removed was technical debt from a previous capability era.

A mature harness eventually inverts the stress-testing question: instead of asking "which components can I remove," it asks "which components should I spend more compute on, and when." The April 2026 **CATTS** preprint (Consensus-Aware Test-Time Scaling, arXiv 2602.12276) gives that question a usable answer. CATTS samples a small committee of rollouts per agent step and uses the disagreement among them as a per-step uncertainty score; that score is then used to allocate test-time compute non-uniformly --- more rollouts where the committee disagrees, fewer where it converges. On WebArena-Lite and GoBrowse, the technique reports **+9.1%** task accuracy at **2.3x fewer tokens** than uniform scaling. For a mature harness, CATTS slots in next to the Advisor Tool: the advisor pattern decides *what* to think about, while CATTS decides *how hard* to think about each step. Both replace assumptions ("always retry three times," "always use Opus on hard problems") with measured uncertainty signals computed at runtime.

## 4.9 Cloud-Native Harness Primitives

Through 2025 and the first quarter of 2026, the harness was overwhelmingly something you built and ran yourself. Even the most sophisticated patterns --- the three-agent architecture, the Advisor Tool, KAIROS-style autonomous loops --- still assumed your code held the orchestrator seat. You wrote the cron job, you ran the daemon, you kept the laptop awake, you owned the failure modes. The substrate was generic compute (a Mac mini, a VPS, a Kubernetes pod), and the harness layer was your responsibility from process supervisor up.

On **April 14, 2026**, Anthropic's **Claude Code Routines** research preview took the first concrete step toward changing that. A Routine is a Claude Code workflow that runs on Anthropic's cloud rather than the user's machine, fired by one of three triggers: **a schedule** (cron-equivalent), **an API call** (programmatic invocation from another service), or **a GitHub event** (push, PR, issue, comment). The triggers are a deliberate generalization of the file-based scheduling patterns harness engineers have been writing for the last eighteen months: the same `runs every weekday at 09:00 HKT` semantics, but expressed as a managed primitive rather than a `cron + tmux + claude` shell incantation. Quotas are tiered with the underlying Claude Code subscription --- **Pro 5/day, Max 15/day, Team/Enterprise 25/day** --- which prices the substrate at "a handful of meaningful loops per day per seat" rather than at "raw compute by the hour."

The cloud-side execution detail matters more than it sounds. A self-hosted file-based scheduler holds the orchestrator seat on hardware the user owns; if the Mac is closed, asleep, or out of battery, the loop does not run. A Routine completes regardless of the user's machine state. This dissolves an entire class of failure modes (laptop lid, network drop, OS update, accidental power-cycle) and a corresponding class of compensating mechanisms (wake-on-LAN tricks, Mac Mini "always on" servers, redundant runners). For workflows that are genuinely event-driven --- "when a PR opens, do X" --- the managed primitive is straightforwardly a better fit than a self-hosted poller.

The tradeoff is a new ceiling. A managed primitive prices itself by trigger and quota, not by the physics of the workload. It assumes your loop fits the schedule / API / GitHub-event shape, that the per-day quota is enough, and that Anthropic's substrate is the right place for your code and data to live. For a non-trivial set of harness workloads, none of those assumptions hold cleanly. **Browser automation** of authenticated sessions still benefits from running on a machine that already has the user's cookies, profile, and trust state. **High-frequency orchestration** --- sub-minute polling, real-time market or sensor data, anything where 25 invocations per day is insulting --- needs a runtime billed by the second, not by the trigger. **Non-GitHub event sources** (Discord messages, internal webhooks, custom MCP servers, on-device file system events) have no first-class trigger in Routines yet; surfacing them requires writing the bridge yourself, which puts you back on a self-hosted machine to run the bridge anyway. And anything that depends on local files, local model inference, or local network access remains structurally off-cloud.

The honest framing for harness engineers in 2026: cloud-native primitives like Routines are the right answer for the **GitHub-event-triggered, scheduled, API-called** quadrant of the harness workload, and they are likely to compress that quadrant's operational cost dramatically over the next twelve months. The self-hosted harness is not going away --- it is being narrowed to where it actually pays for itself. The discipline to develop is the same discipline this chapter has been building toward: knowing which assumption each component encodes, and noticing when the substrate underneath it changes.

---

## Sources

- **Fowler, Martin and Bockeler, Birgitta.** "Harness Architecture for LLM Agents." ThoughtWorks Technology Radar / blog, 2025. Guides vs. Sensors, Computational vs. Inferential taxonomy.
- **OpenAI.** "Codex: From Research to Production." OpenAI blog, 2025. Three-engineer, ~1M lines, ~1,500 PRs case study.
- **swyx (Shawn Wang).** "The IMPACT Framework for Agent Design." Blog / conference talk, 2025. Six-dimension harness design checklist.
- **Stanford / MIT / KRAFTON.** "Meta-Harness: Automated Optimization of LLM Agent Harnesses." arXiv preprint, March 2026. 6x performance gap finding, automated harness tuning.
- **Anthropic.** "Building Effective Agents." Anthropic engineering guide, 2025. Three-agent architecture, context anxiety, self-evaluation bias, stress-testing imperative.
- **Anthropic.** "Multi-Agent Systems: Planner-Generator-Evaluator Architectures." Research report, 2025-2026. Evaluator calibration findings.
- **Meta / Manus Acquisition.** Various reporting, early 2026. ~$2B acquisition validating harness-as-moat thesis.
- **Karpathy, Andrej.** "Software 3.0." Talk / essay, 2025. Framing of models as components within larger software systems.
- **LangChain.** "Agent Architecture Patterns." LangChain documentation, 2025. Practical patterns for control flow and tool orchestration.
- **Harrison Chase.** "The Rise of the Agent Engineer." Blog post, 2025. Role definition for harness-focused engineering.
- **"CATTS: Consensus-Aware Test-Time Scaling for Agents."** arXiv 2602.12276 (April 2026 release cycle). Vote-derived uncertainty as a test-time compute allocator; +9.1% / 2.3x fewer tokens vs. uniform scaling on WebArena-Lite and GoBrowse. [https://arxiv.org/abs/2602.12276](https://arxiv.org/abs/2602.12276)
- **Anthropic.** "Introducing Routines in Claude Code." Anthropic blog, April 14, 2026. [https://claude.com/blog/introducing-routines-in-claude-code](https://claude.com/blog/introducing-routines-in-claude-code)
- **Anthropic.** "Claude Code Routines documentation." [https://code.claude.com/docs/en/routines](https://code.claude.com/docs/en/routines) --- triggers (schedule / API / GitHub event), quotas (Pro 5/day, Max 15/day, Team/Enterprise 25/day), cloud-side execution semantics.

### Further reading for beginners

- **Cab.** "A Layer-by-Layer Walk Through Harness Engineering." Traditional Chinese essay, 2026. Builds up from a single `POST /v1/messages` call through prompt engineering, function calling, agent loops, and finally full harness complexity. Notable for the "模型從來都沒有長手" metaphor, which reframes tool use as a harness problem rather than a model capability, and for its explicit walk through what Claude Code's harness is actually doing behind the scenes. Recommended as a gentle on-ramp before reading this chapter's theory-first framings (Fowler-Bockeler, IMPACT, Meta-Harness).
- **Anthropic.** ["Building Effective Agents"](https://www.anthropic.com/research/building-effective-agents) --- the canonical short-form introduction for readers coming from a non-research background. Pairs well with the Cab essay above: Cab gives the build-up, Anthropic gives the concrete patterns.
