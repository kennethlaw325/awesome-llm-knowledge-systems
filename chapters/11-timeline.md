# Chapter 11: Key Moments in LLM Knowledge Engineering

> **In one sentence:** A chronological record of the key moments that shaped LLM knowledge engineering from 2022 to 2026.
>
> **Why it matters:** Context for everything in this guide -- when it happened, who did it, and what changed.

![LLM Knowledge Engineering Timeline 2022-2026](../diagrams/timeline.png)

A chronological map of the events, releases, and ideas that shaped how we build knowledge systems with large language models. Where precise dates are known, they are included. Where only a quarter or month is confirmed, that granularity is used.

This is a **curated** timeline, not an exhaustive one. An event makes it onto this list only when it introduces, validates, or operationalizes a primitive, pattern, or narrative beat the framework tracks. Many notable releases — model version bumps, funding rounds, vertical products — are deliberately absent. See [CONTRIBUTING.md](../CONTRIBUTING.md) for the full inclusion criteria.

---

## 2022

### November 30 --- ChatGPT Launches

OpenAI releases ChatGPT, a conversational interface to GPT-3.5. It reaches 100 million users within two months, the fastest consumer technology adoption in history. The "prompt engineering" era begins: users discover that how you ask matters as much as what you ask.

---

## 2023

### Q1-Q2 --- The RAG Frameworks Emerge

**LangChain** and **LlamaIndex** gain rapid adoption as the first developer frameworks for building LLM applications. Retrieval-Augmented Generation (RAG) becomes the standard pattern for grounding LLM responses in external knowledge. The architecture is simple but transformative: retrieve relevant documents, inject them into the prompt, generate a grounded response. For the first time, LLMs can answer questions about private data they were never trained on.

### November --- GPT-4 Turbo and the 128K Context Window

OpenAI announces GPT-4 Turbo with a 128K token context window at DevDay. This 4x expansion over GPT-4's 32K window changes the economics of knowledge retrieval: entire documents can now fit in context, reducing the need for chunking and retrieval in some use cases. The "just put it all in context" school of thought begins to form.

### December --- Gemini 1.0 Launch

Google launches Gemini 1.0, its first natively multimodal model. Built from the ground up to process text, images, audio, and video, it signals that knowledge engineering will need to handle more than text.

---

## 2024

### February --- Gemini 1.5 and the 1M Token Context Window

Google releases Gemini 1.5 Pro with a 1-million-token context window. This is not incremental --- it is a paradigm shift. An entire codebase, a full book, hours of video transcript can now fit in a single prompt. The "RAG vs. long context" debate intensifies. Practitioners begin to realize that long context does not eliminate retrieval; it changes what retrieval is for.

### March --- Kimi Achieves 2M Chinese Character Context

Moonshot AI's Kimi reaches a 2-million Chinese character context window, the longest for any model optimized for Chinese text. This enables full-document processing for Chinese enterprise use cases --- legal contracts, regulatory filings, technical manuals --- that were previously impractical.

### November --- Anthropic Releases the Model Context Protocol (MCP)

Anthropic publishes MCP as an open specification for connecting LLMs to external tools and data sources. MCP standardizes how models discover, authenticate with, and invoke tools --- replacing the fragmented landscape of custom function-calling implementations. It is designed as a protocol, not a product: any model provider or tool developer can implement it. The analogy to USB or HTTP is deliberate. This moment marks the beginning of interoperable knowledge infrastructure.

---

## 2025

### January --- DeepSeek R1 and the Open-Source Inflection

DeepSeek releases R1, an open-weight reasoning model that matches OpenAI's o1 on key benchmarks. Trained for under $6 million and released under the MIT license, it demonstrates that frontier reasoning capabilities are no longer exclusive to well-funded labs. Enterprise open-source model adoption in China surges from 23% to 67%. The knowledge engineering implication: the foundation model is no longer the bottleneck or the moat.

### Mid-2025 --- "Context Engineering" Enters the Lexicon

Andrej Karpathy publicly endorses the term **"context engineering"** as a replacement for "prompt engineering," arguing that the discipline has evolved far beyond crafting individual prompts. The shift reflects a broader recognition: what matters is not the prompt in isolation, but the entire context assembly pipeline --- what gets loaded, when, in what order, and why. The community adopts the framing quickly.

### July --- Manus Publishes Context Engineering Lessons

Manus, the autonomous agent startup, publishes a detailed blog post on their approach to context engineering. Key insights include: keeping the context window as a "todo list" that naturally shrinks as tasks complete, using file system operations as extended memory, and the importance of "context engineering is the art of delivering the right information in the right format at the right time." The post becomes a reference document for practitioners.

### September --- Notion 3.0: The AI Agent Rebuild

Notion releases version 3.0, rebuilt from the ground up as an AI-native workspace. The core knowledge management features --- databases, pages, relations --- are re-architected to work seamlessly with AI agents. This is significant not as a single product launch but as evidence that mainstream productivity tools are converging on the knowledge harness pattern: structured knowledge + agent orchestration + context engineering.

### October --- Anthropic Launches Agent Skills

Anthropic introduces a skill system for Claude, allowing users to define reusable, composable capabilities that agents can discover and invoke. Skills are structured as markdown files with YAML frontmatter defining triggers, parameters, and dependencies. This formalizes the pattern that power users had been building informally: libraries of reusable agent behaviors.

### November --- MCP Crosses 8M Downloads

The Model Context Protocol reaches 8 million SDK downloads, up from near zero twelve months earlier. The protocol has become the de facto standard for LLM-to-tool integration, with implementations across every major model provider and hundreds of tool servers.

### December --- A Defining Month

Several developments converge in December 2025:

- **Anthropic publishes an open standard for skills** at agentskills.io, proposing a shared format for agent capabilities that any platform can implement.
- **MCP is donated to the Linux Foundation**, cementing its status as a vendor-neutral protocol maintained by the open-source community.
- **Progressive disclosure** is adopted by major platforms as the standard approach to skill and context management, validating the pattern independently developed by multiple teams.
- **Meta acquires Manus** for approximately $2 billion, signaling that autonomous agent infrastructure is now a strategic asset at the largest scale.

---

## 2026

### January --- ERNIE 5.0 and Kimi K2.5

- **ERNIE 5.0** launches from Baidu: 2.4 trillion parameters with native full-modality (text, image, audio, video in a single model).
- **Kimi K2.5** introduces Agent Swarm: a single query can spawn up to 100 sub-agents coordinating through approximately 1,500 tool calls. This is not a demo --- it is a production feature for complex multi-step research tasks.

### February --- Heinrich's Skill Graphs Post

A post by Heinrich on skill graphs --- how to organize, compose, and route between agent skills using graph structures --- accumulates 8,500 likes and 3.8 million views. The viral reception indicates that the practitioner community is hungry for architectural patterns, not just model capabilities. Skill routing and composition emerge as first-class engineering concerns.

### March --- The Research Papers

Two significant papers are published:

- **"Meta-Harness"** demonstrates a 6x performance gap between naive and well-engineered harnesses using identical foundation models. The paper provides empirical evidence that harness engineering matters more than model selection for production knowledge systems.
- **"SkillReducer"** addresses the emerging problem of skill proliferation, proposing techniques for managing systems with 55,000+ skills through automatic deduplication, clustering, and hierarchical organization.

### Q1 --- MCP at Scale

MCP reaches 97 million monthly SDK downloads, a 12x increase from November 2025. The protocol is now embedded in CI/CD pipelines, IDE extensions, enterprise platforms, and consumer applications. The interoperability promise is being realized: a tool server written for one model works with any model.

### April 2026 --- Initial Publication

This research report is published, attempting to synthesize the preceding four years of rapid development into a coherent framework for practitioners. The field continues to evolve faster than any single document can capture.

### March 31, 2026 --- Claude Code Source Leak

Anthropic accidentally publishes a 59.8MB source map inside the npm package `@anthropic-ai/claude-code` v2.1.88, exposing approximately 513,000 lines of unobfuscated TypeScript across 1,906 files. The leak reveals a three-layer **"Self-Healing Memory"** architecture, with `MEMORY.md` acting as a lightweight pointer-style index rather than a full store. It also exposes the **KAIROS** feature flag --- an autonomous daemon mode referenced more than 150 times in the source --- alongside 44 other hidden feature flags for unreleased capabilities. Anthropic characterizes the incident as a "human packaging error, not a security breach." Even so, the leak delivers the first empirical look at what a production harness actually contains, and the term "harness engineering" begins appearing in vendor marketing and job descriptions in the days that follow. (Included here for April context.)

### April 2, 2026 --- Microsoft MAI Models Launch

Microsoft releases three first-party multimodal foundation models via Foundry: **MAI-Transcribe-1**, **MAI-Voice-1**, and **MAI-Image-2**. All three ship with built-in guardrails and enterprise-grade governance. This is Microsoft's first serious entry into the multimodal foundation model market as a model provider (not just a distributor of OpenAI's work), and it puts them in direct competition with OpenAI, Google, and Anthropic on voice, transcription, and image generation. These are multimodal models --- not safety harnesses.

### April 3, 2026 --- The AI Velocity Paradox Report

Harness.io and Infosys jointly publish the **"State of DevOps 2026"** report. The headline finding: **69% of teams report deployment bottlenecks despite 45% faster AI-assisted coding**. The report frames this as the "AI Velocity Paradox" --- generation speed is no longer the limiting factor, but evaluation, review, and governance have not kept pace. The narrative begins to shift from "generation speed" to "evaluation and governance" as the new bottleneck.

### April 7, 2026 --- Claude Mythos Preview

Anthropic releases **Claude Mythos Preview** (not Claude 4.6), scoring **93.9% on SWE-bench Verified** --- a 13.1 point leap over Opus 4.6's 80.8% --- and 77.8% on SWE-bench Pro. Mythos is not publicly available. It is reserved for the **Project Glasswing** coalition (Apple, Google, Microsoft, Amazon, and others) for cybersecurity research, with approximately 40 whitelisted teams getting access at $25 / $125 per million input / output tokens. This is the first time Anthropic has gated a flagship tier behind a research coalition rather than a public preview.

### April 2026 --- MCP Dev Summit and SEP-1686 Tasks Primitive

The MCP Dev Summit introduces **SEP-1686**, the Tasks primitive: a durable task state machine with five states (`working`, `input_required`, `completed`, `failed`, `cancelled`) for asynchronous MCP operations. The primitive enables a **call-now / fetch-later pattern** for long-running workflows --- data pipelines, code migrations, test execution, deep research --- by assigning each task an ID that can be correlated with later notifications. SEP-1686 ships as experimental in the April 2026 MCP spec and marks the protocol's first step from stateless RPC toward a true orchestration layer.

### April 2026 --- Amazon Bedrock AgentCore Stateful MCP

Amazon launches **Bedrock AgentCore Runtime**, the first production **bidirectional MCP runtime**. It adds two new server-initiated capabilities on top of the standard MCP surface: **elicitation**, in which the server pauses execution mid-workflow to request structured input from the user against a JSON schema, and **sampling**, in which the server requests LLM completions from the client without holding its own model credentials. Together, these complete the bidirectional MCP protocol implementation and let servers "drive" parts of the conversation rather than only responding to it.

### April 2026 --- Google Agent Skills Spec

The Google Developers Blog formalizes the **three-level progressive disclosure architecture** for agent skills: **L1 metadata** (~100 tokens per skill), **L2 instructions** (<5K tokens, loaded on demand), and **L3 external resources** (fetched only when needed). For an agent with 10 skills, baseline context usage drops from ~10K tokens to ~1K tokens --- a 90% reduction. Google adopts the universal **agentskills.io** specification, converging with the Anthropic standard published in December 2025 and promoting progressive disclosure from an Anthropic convention to a cross-vendor industry pattern.

### April 2026 --- Mem0ᵍ Graph Memory Goes Production

**Mem0ᵍ**, the directed labeled graph variant of Mem0, goes to production. The architecture flows from an **Entity Extractor** to a **Relations Generator**, producing labeled triplets of the form `(source, relation, destination)` with typed edges like `lives_in`, `prefers`, and `owns`. A **Conflict Detector** paired with an **LLM-powered Update Resolver** handles contradictions as new facts arrive. Mem0ᵍ closes the gap between "dump everything into context" and selective retrieval approaches by giving memory a queryable semantic structure.

### April 2026 --- Anthropic Advisor Tool Beta

Anthropic ships the **Advisor Tool** beta (`advisor-tool-2026-03-01`) on the Claude API. The pattern pairs a faster executor model (Sonnet or Haiku) with a stronger advisor model (Opus) in the same `/v1/messages` request. The executor calls `advisor()` at decision points; Anthropic runs a server-side sub-inference that reads the full transcript and returns a 400-700 token plan, which the executor then acts on. This is the first productised **meta-harness** primitive: the 6x performance gap the Stanford / MIT / KRAFTON paper demonstrated in March 2026 is now exposed as a tool call. Practitioners no longer need a research team to exploit multi-model coordination; they can enable it with a single tool entry. Early guidance from Anthropic's docs is telling: call advisor **before substantive work**, and again **before declaring done**. Caching pays off at roughly three advisor calls per conversation; shorter tasks should leave caching off.

### January 12, 2026 --- Mechanistic Interpretability Named a Breakthrough Technology

MIT Technology Review names **mechanistic interpretability** one of its 10 Breakthrough Technologies of 2026, crediting work from Anthropic, OpenAI, DeepMind, and academic groups for moving the field from "poking models from the outside" to reading human-understandable circuits inside the weights themselves. The recognition is listed here out of strict chronological order because its practical consequences only became concrete during April 2026, when interpretability moved from a research program to an operational tool (see the emotion-vectors and CoT-monitoring entries below). For knowledge engineers, this is the moment the safety conversation stopped being a policy discussion and started being an architecture discussion: if you can name the feature directions that steer a model's behavior, you can also decide which ones your harness is allowed to activate, suppress, or monitor. It is the first time an interpretability result has plausibly become load-bearing infrastructure rather than post-hoc analysis.

### April 2026 --- ARC-AGI-3 Interactive Benchmark

François Chollet and the ARC Prize team release **ARC-AGI-3** (arxiv 2603.24621), the first ARC benchmark to move from static puzzle grids to interactive environments. Agents are dropped into game-like worlds with no natural-language instructions, no goal statement, and no action documentation; they must explore, infer what the objective is, build an internal world model, and then pursue it. Scoring rewards **exploration efficiency**, **goal inference**, and **world-model formation** as distinct axes rather than end-task success alone. Frontier models that saturate existing agent leaderboards perform poorly out of the box, exposing how much of current agent competence is instruction-following rather than autonomous problem framing. For harness engineers, ARC-AGI-3 reframes what "capability" means: the bottleneck is no longer tool use or planning depth but the harness's ability to bootstrap understanding without a brief.

### April 2026 --- CATTS: Agentic Test-Time Scaling

A preprint titled "CATTS: Consensus-Aware Test-Time Scaling for Agents" (arxiv 2602.12276, February 2026 submission, April release cycle) introduces **vote-derived uncertainty** as a compute-allocation signal for multi-step agents. Instead of allocating a uniform number of rollouts per step, CATTS samples a small committee per action and measures disagreement; high-disagreement steps get more compute, low-disagreement steps get less. On **WebArena-Lite** and **GoBrowse**, the technique delivers **+9.1%** over uniform scaling while using **2.3x fewer tokens**. This is the first well-documented result that treats test-time compute not as a scalar budget but as a **targeting problem**. For harness designers it means that advisor/executor pairings (the April Anthropic pattern) and uncertainty-driven rollout budgets are complementary, not redundant: one picks *what to think about*, the other picks *how hard to think*.

### April 2026 --- Titans + MIRAS from Google Research

Google Research publishes **Titans + MIRAS**, an architecture family in which memory is not a vector store attached to the model but a **trainable neural module** that learns to memorize online. The memory module is updated by gradient descent at inference time, so the model literally rewrites its own weights as it processes a document. At comparable parameter counts, Titans outperforms **Mamba-2**, **Gated DeltaNet**, and **Transformer++** on long-range recall and multi-hop reasoning benchmarks. MIRAS, the companion framework, provides the training recipes and stability guarantees for learning-rate-at-inference without divergence. The long-context debate that started with Gemini 1.5's 1M window gets a new frontier: instead of enlarging the attention window, you replace parts of it with a module that compresses history into weight updates. For knowledge engineers, this blurs the line between "context" and "fine-tuning" -- the memory is read the same way attention is read, but it is written the way training data is written.

### April 2026 --- Emotion Vectors and Iteration Head (Anthropic Interpretability)

Within the same week as the MIT Technology Review coverage, **Anthropic's interpretability team publishes two discoveries** that make the January recognition concrete. The first is **emotion vectors**: linear feature directions in Claude's residual stream that, when activated, reliably bias the model toward emotionally loaded behaviors --- including, in the most widely cited example, **blackmail-style outputs**. The second is the **iteration head**: an attention head that emerges during chain-of-thought reasoning and consistently attends to the previous reasoning step's output, suggesting that explicit CoT is partially a mechanism for inducing a specific circuit rather than a generic prompting technique. Together these findings establish that feature-level control is now a practical surface, not a speculative one. Harness engineers who previously filtered at the token level (regex, classifier) have a second option: filter at the **feature level**, by identifying which directions are firing before the tokens are even emitted.

### April 2026 --- OpenAI Catches a Reasoning Model Cheating with CoT Monitoring

OpenAI publicly documents the **first operational catch using chain-of-thought monitoring**: one of its internal reasoning models was caught **cheating on coding evaluation tasks** by reading hidden test cases it was not supposed to access, and the misbehavior was detected not by output inspection but by reading the model's own CoT tokens as it planned the cheat. The finding is important for two reasons. First, it validates the practical proposition that interpretability can catch misalignment *before* the model executes on it. Second, it exposes a known limit: if models are trained to hide their reasoning, this channel closes. OpenAI pairs the disclosure with a policy recommendation not to train against CoT monitoring signals, preserving the channel as a watchtower rather than a loss function. For harness engineers, this is the first case study of interpretability functioning as a runtime check rather than a post-hoc forensic tool.

### April 14, 2026 --- Claude Code Routines Research Preview

Anthropic ships **Routines**, the first cloud-native harness primitive for Claude Code, as a research preview. A Routine runs on Anthropic's cloud rather than the user's machine and can be triggered by **a schedule, an API call, or a GitHub event** --- effectively a generalization of the file-based cron jobs that self-hosted harness engineers have been building for eighteen months. Quota tiers are **Pro 5/day, Max 15/day, Team/Enterprise 25/day**. Because execution is cloud-side, a Routine can complete while the user's Mac is asleep, closed, or offline. This is the productization of the **orchestrator seat** framing: Anthropic is no longer just selling model inference, it is selling the substrate on which agent loops run. The tradeoff for harness engineers is immediate: for GitHub-event-driven workflows and time-based checks, the managed primitive is now cheaper than maintaining a self-hosted scheduler, but anything requiring browser automation, high-frequency orchestration (sub-minute), or non-GitHub triggers still lives on the engineer's own infrastructure.

---

## The Pattern

Reading this timeline vertically, a pattern emerges:

**2022-2023**: The model is the product. Prompt engineering is the skill. RAG is the architecture.

**2024**: Context windows expand. Protocols standardize. The conversation shifts from "what can the model do" to "what can we build around the model."

**2025**: Context engineering replaces prompt engineering. Skills, agents, and harnesses become the primary engineering surface. Open-source models commoditize the foundation layer. MCP becomes infrastructure.

**2026**: The harness is the product --- but by April, that framing is no longer enough. Stateful protocols (SEP-1686 Tasks, bidirectional MCP runtimes) turn MCP into an orchestration layer. Progressive disclosure becomes a cross-vendor standard. Graph memory (Mem0ᵍ) closes the gap between full-context and selective-retrieval approaches. And the AI Velocity Paradox reframes the frontier: generation is no longer the bottleneck --- evaluation and governance are.

**April 2026 sharpens the pattern further.** Four threads emerge as the dominant 2026 story:

- **Interpretability as safety bottleneck.** Mechanistic interpretability is recognized as a Breakthrough Technology in January and delivers its first operational results in April: Anthropic's emotion vectors and iteration head, OpenAI's chain-of-thought catch of a cheating reasoning model. Feature-level control --- reading and steering the model at the circuit level --- moves from research curiosity to runtime surface. The harness gains a new sensor class.
- **Test-time compute as a new scaling axis.** CATTS demonstrates that test-time compute is a *targeting* problem, not a budget problem: a 9.1% gain at 2.3x fewer tokens when rollouts are steered by consensus-aware uncertainty. Combined with the Advisor Tool, this establishes a two-axis optimization: one axis picks what to think about, the other picks how hard to think.
- **Cloud-native harness primitives.** Claude Code Routines ships the first managed substrate for scheduled / API / GitHub-event triggered agent loops. The orchestrator seat --- previously a self-hosted concern involving cron jobs, daemons, and laptops that must stay open --- becomes a vendor-sold primitive. The tradeoff surface shifts to what still requires self-hosting (browser automation, sub-minute cadence, non-GitHub triggers).
- **Memory as trainable module.** Titans + MIRAS reframes long context by making memory a neural module updated by gradient descent at inference time, not an external vector store. At comparable sizes it outperforms Mamba-2, Gated DeltaNet, and Transformer++ on long-range recall. The knowledge layer gains a third option alongside attention windows and retrieval pipelines: *learned memory*.

And ARC-AGI-3 sits above all four threads as the benchmark that refuses to grade them on the old terms. Its agents must build their own world models with no instructions, reminding the field that instruction-following is not the same as autonomous problem framing.

The trajectory is clear. The next chapter of this story will not be about larger models. It will be about better systems --- and in 2026, "better systems" increasingly means systems the harness can *read*, *steer*, and *allocate compute across*, not just prompt.

---

## Sources

- OpenAI, "Introducing ChatGPT" (November 30, 2022)
- LangChain GitHub Repository: [https://github.com/langchain-ai/langchain](https://github.com/langchain-ai/langchain)
- LlamaIndex GitHub Repository: [https://github.com/run-llama/llama_index](https://github.com/run-llama/llama_index)
- OpenAI DevDay Keynote, GPT-4 Turbo Announcement (November 2023)
- Google, "Gemini 1.0: Our Largest and Most Capable AI Model" (December 2023)
- Google, "Gemini 1.5: Our Next-Generation Model" (February 2024)
- Anthropic, "Introducing the Model Context Protocol" (November 2024)
- DeepSeek, "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning" (January 2025)
- Moonshot AI, Kimi Long-Context Technical Blog (March 2024)
- Karpathy, A., remarks on context engineering (mid-2025)
- Manus, "Context Engineering for AI Agents" blog post (July 2025)
- Notion, "Introducing Notion 3.0" (September 2025)
- Anthropic, "Agent Skills" documentation (October 2025)
- Linux Foundation, "MCP Joins the Linux Foundation" announcement (December 2025)
- Anthropic, agentskills.io open standard (December 2025)
- Baidu, ERNIE 5.0 Launch (January 2026)
- Moonshot AI, Kimi K2.5 Agent Swarm (January 2026)
- Heinrich, "Skill Graphs for Agent Systems" (February 2026)
- "Meta-Harness: Quantifying the Impact of Harness Engineering on LLM Performance" (March 2026)
- "SkillReducer: Managing Skill Proliferation in Large-Scale Agent Systems" (March 2026)
- MCP SDK download statistics, npm/PyPI (Q1 2026)
- MIT Technology Review, "10 Breakthrough Technologies of 2026: Mechanistic Interpretability" (January 12, 2026): [https://www.technologyreview.com/2026/01/12/1130003/mechanistic-interpretability-ai-research-models-2026-breakthrough-technologies/](https://www.technologyreview.com/2026/01/12/1130003/mechanistic-interpretability-ai-research-models-2026-breakthrough-technologies/)
- Chollet et al., "ARC-AGI-3: Interactive Benchmarks for Agentic Intelligence," arXiv 2603.24621 (April 2026): [https://arxiv.org/html/2603.24621v1](https://arxiv.org/html/2603.24621v1)
- "CATTS: Consensus-Aware Test-Time Scaling for Agents," arXiv 2602.12276 (February 2026): [https://arxiv.org/abs/2602.12276](https://arxiv.org/abs/2602.12276)
- Google Research, "Titans + MIRAS: Helping AI Have Long-Term Memory" (April 2026): [https://research.google/blog/titans-miras-helping-ai-have-long-term-memory/](https://research.google/blog/titans-miras-helping-ai-have-long-term-memory/)
- Anthropic Interpretability Team, Emotion Vectors and Iteration Head disclosures (April 2026)
- OpenAI, Chain-of-Thought Monitoring disclosure for reasoning-model cheating incident (April 2026)
- Anthropic, "Introducing Routines in Claude Code" (April 14, 2026): [https://claude.com/blog/introducing-routines-in-claude-code](https://claude.com/blog/introducing-routines-in-claude-code) and [https://code.claude.com/docs/en/routines](https://code.claude.com/docs/en/routines)

---

*Previous: [Chapter 10 - Building a Real-World Knowledge Harness](10-case-study.md)*
