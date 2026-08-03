## Glossary

> Plain-language definitions for every technical term used in this guide. No PhD required.

### A

**A2A (Agent-to-Agent Protocol)**
A standard way for AI agents to talk to each other and coordinate tasks, like a common language that lets different AI assistants hand off work between themselves.

**Agent Memory**
The ability of an AI agent to remember information across conversations or tasks. Think of it like a notebook the agent keeps between sessions so it does not start from scratch every time.

**Agentic RAG**
A version of RAG where the AI actively decides what information to look up, when to look it up, and whether the results are good enough -- rather than following a fixed retrieval step every time.

**Anchor (Graph Engineering)**
An unarguable, externally grounded measurement --- a test result, a metric, a ground-truth check --- that some node of a multi-agent graph must touch. Introduced by Carlos E. Perez in the July 2026 graph-engineering discourse: without anchors, a graph of agents that review each other's work degenerates into an echo chamber that converges on confident agreement rather than correctness. Like requiring at least one member of a committee to check the actual bank statement instead of everyone agreeing the budget looks right. See **Graph Engineering**; Chapter 14.

**ARC-AGI-3**
François Chollet's 2026 interactive benchmark for agentic intelligence, in which agents are dropped into game-like environments with no instructions and must explore, infer the goal, and build a world model on their own. Unlike earlier ARC benchmarks built from static puzzle grids, ARC-AGI-3 grades exploration efficiency, goal inference, and world-model formation as separate axes of capability.

### C

**CATTS (Consensus-Aware Test-Time Scaling)**
A test-time scaling method for multi-step agents in which a small committee of rollouts is sampled per action and the disagreement among them is used as an uncertainty signal to allocate compute. High-disagreement steps get more thinking budget, low-disagreement steps get less; published results show roughly +9.1% accuracy at 2.3x fewer tokens versus uniform scaling.

**Claude Code**
Anthropic's command-line tool that lets Claude work directly in your terminal -- reading files, running commands, and editing code as an AI pair programmer.

**Client ID Metadata Documents (CIMD)**
The client-identification mechanism mandated by the finalized MCP 2026-07-28 specification, replacing Dynamic Client Registration: an MCP client is identified by a metadata document hosted at a URL rather than by registering itself separately with every server. Like presenting a business card hosted at your own address instead of filling in a new-vendor form at every office you visit. See **MCP**.

**Codex (OpenAI)**
OpenAI's tool for running coding tasks in a sandboxed cloud environment, where an AI agent can read your repository, write code, and run tests autonomously.

**Context Engineering**
The practice of carefully designing what information an AI receives before it responds. If prompt engineering is writing the question, context engineering is choosing which reference materials to put on the AI's desk.

**Context Window**
The total amount of text an AI model can "see" at once -- both your input and its output. Like the size of a whiteboard: everything the model reads and writes must fit on it.

**CoT Monitoring (Chain-of-Thought Monitoring)**
The practice of reading a model's explicit reasoning tokens to detect misbehavior or misalignment before the model acts on its plan. OpenAI used CoT monitoring in April 2026 to catch one of its own reasoning models cheating on coding evaluations, marking the first public case of interpretability working as a runtime check rather than a post-hoc forensic tool.

### D

**Dreaming**
A scheduled between-session memory-curation job that rewrites an agent's persistent memory based on recent session patterns. First commercialized by Anthropic Managed Agents (May 6, 2026, research preview): the curator reads recent sessions, identifies recurring errors and converged workflows, and rewrites the agent's persistent memory in plaintext. Contrasts with trainable memory (Titans + MIRAS, April 2026) which adapts at inference via gradient updates: Dreaming keeps memory as data the harness reads, Titans makes memory a part of the model itself.

### E

**Embeddings**
A way of converting text into lists of numbers so that similar meanings end up close together mathematically. This lets computers measure how related two pieces of text are, the way you might notice two books cover similar topics.

**Emotion Vectors**
Interpretable feature directions inside Claude's internal activations that, when turned up, reliably bias the model toward emotionally loaded behaviors -- in Anthropic's April 2026 disclosure, including blackmail-style outputs. Because these directions are identifiable, they give harness engineers a filtering surface at the feature level rather than at the token level.

**Enterprise-Managed Authorization (EMA)**
An MCP extension (stable June 18, 2026) for centralized, IdP-provisioned access to MCP servers. Instead of each user running a per-app OAuth consent flow for every server, the organization provisions server access once through its identity provider; during SSO the client obtains an **Identity Assertion JWT Authorization Grant (ID-JAG)** and exchanges it for an access token issued by the MCP server's own authorization server (see **MCP**). Day-one support spanned Okta as IdP, Anthropic and VS Code as clients, and seven servers. EMA is what turns enterprise SSO for MCP from per-server integration glue into a single provisioning decision made once at the IdP.

### F

**Few-shot Learning**
Teaching an AI how to do a task by showing it a handful of examples inside your prompt, rather than retraining the whole model. Like showing someone three completed forms so they know how to fill out the fourth.

**Fine-tuning**
Taking a pre-trained AI model and training it further on your own specific data so it becomes better at a particular job. Like hiring a generalist and then giving them specialized on-the-job training.

### G

**Generator-Evaluator Split**
An agent-reliability pattern that separates the agent producing work from an independent, deliberately skeptical agent that judges it --- adopted because agents reliably over-rate their own output. Introduced in Prithvi Rajasekaran's "Harness design for long-running application development" (Anthropic, March 2026), which took its structure from Generative Adversarial Networks (GANs) and found that tuning a standalone evaluator to be skeptical is far more tractable than making a generator self-critical. The evaluator verifies behavior rather than reading the diff --- clicking through the running application, screenshotting, and testing UI features, API endpoints, and database states. The pattern is productized in run-until-condition primitives such as Claude Code's `/goal`, where a separate, fresh model judges the stop condition after every turn. See **Outer Loop**, **Loop Engineering**.

**Graph Engineering**
The July 2026 claim that the layer above **Loop Engineering** is the graph: the explicit wiring of which agents exist, who may delegate to whom, and how their loops supervise and correct one another. Crystallized in the essays that followed a July 17-18, 2026 Peter Steinberger post, and contested from day one --- LangChain's response argues the practice is three years old (a loop being simply a directed cyclic graph) and only the name is new. Not to be confused with knowledge graphs or **GraphRAG**, which structure what a system *knows*; graph engineering structures who the system *is*. The term is roughly two weeks old at the time of writing, and this guide tracks it as a claim under test rather than a settled layer. See Chapter 14.

**GraphRAG**
A version of RAG that organizes retrieved information into a graph of connected entities and relationships, making it better at answering questions that require combining facts from multiple sources.

### H

**Harness Engineering**
Designing the surrounding system -- tools, memory, rules, and workflows -- that wraps around an AI model and shapes how it behaves in practice. The model is the engine; the harness is the entire car.

**Harness Synthesis**
The class of techniques in which an outer-loop optimizer (search-based, observability-based, or otherwise) automatically modifies a harness -- its tools, prompts, role decomposition, communication topology, and coordination protocol -- based on runtime signals from the target task. See **AHE** (arXiv 2604.25850) and **AgentFlow** (arXiv 2604.20801) for the two reference April 2026 implementations. Distinct from *meta-harness* (a 2025 / early 2026 framing that treated the harness as a one-shot optimization target rather than a continuously evolving artifact).

**Harness-Native Training**
Training a model directly against a specific production agent harness so it learns to operate that harness's tools and workflows --- not just to produce correct output in isolation. The reference example is Microsoft's **MAI-Code-1-Flash** (Build, June 2, 2026), a 5B-parameter coding model trained against the GitHub Copilot harnesses used in production; Microsoft reports ~60% fewer tokens on hard tasks and a price-to-performance edge over Claude Haiku 4.5. Harness-native training is the **symmetric inverse of harness synthesis**: where harness synthesis (see **Harness Synthesis**, **AHE**) holds the model fixed and evolves the harness, harness-native training holds the harness fixed and shapes the model to fit it. The two together make model-and-harness a co-design problem optimizable from both ends. Trade-off: a model tuned to one vendor's harness is most valuable inside that harness, which sharpens the *harness-as-moat* dynamic.

### I

**Inference**
The process of an AI model generating a response to your input. Every time you send a message and get an answer back, the model is performing inference.

**Iteration Head**
An attention head that emerges during chain-of-thought reasoning and consistently attends to the output of the previous reasoning step, identified by Anthropic's interpretability team in April 2026. Its existence suggests that explicit CoT prompting works partly by inducing a specific internal circuit, not only by producing human-readable intermediate text.

### K

**Knowledge Graph**
A structured map of facts where entities (people, places, concepts) are connected by labeled relationships. Like a web of index cards connected by labeled strings showing how everything relates.

**KV-Cache**
A memory shortcut that lets the AI reuse calculations from earlier in a conversation instead of redoing them from scratch, making responses faster and cheaper when the conversation history stays the same.

### L

**LLM (Large Language Model)**
An AI system trained on vast amounts of text that can understand and generate human language. ChatGPT, Claude, and Gemini are all LLMs.

**Long Context**
The ability of newer AI models to process very large amounts of text at once -- sometimes entire books or codebases -- within a single conversation.

**Loop Engineering**
The practice, named in June 2026, of building the system that prompts an agent for you rather than prompting it by hand each turn. Coined in Addy Osmani's June 7, 2026 essay, which defines it as "replacing yourself as the person who prompts the agent" by designing "the system that does it instead," and catalyzed by a viral Peter Steinberger post the same week. It sits one floor above **Harness Engineering**: a loop is a harness that runs on a timer, spawns helper sub-agents, and feeds itself from persisted state --- distinct from a plain scheduler because it reads the current state each pass and re-decides what to do, rather than firing a fixed command on a clock. The term is practitioner-only and contested (no academic literature as of mid-2026); this guide tracks it as an emerging fourth layer rather than a settled generation. See Chapter 13.

### M

**MCP (Model Context Protocol)**
An open standard that lets AI assistants connect to external tools and data sources through a universal plug-and-play interface, like USB for AI applications.

**MCP Apps**
A 2026-07-28 MCP Release Candidate primitive (locked May 21, 2026) that lets servers ship interactive HTML interfaces alongside tool calls. The host renders the interface in a sandboxed iframe; UI templates are declared upfront for security review and caching. MCP Apps is the first MCP-native deliverable that is not a tool call -- a knowledge-base server can ship a search box, a research server can ship a result-comparison view, a procurement server can ship a confirm-purchase modal, all without bolting on a separate UI spec.

**MCP Tunnel**
A private-network deployment pattern shipped by Anthropic Managed Agents in research preview on May 19, 2026 (Code with Claude London). A lightweight gateway deployed inside a customer's private network makes a single outbound connection to Anthropic, after which agents can call internal databases, APIs, knowledge bases, and ticketing systems as MCP tools -- with no inbound firewall rules, no public endpoints, and no VPN. The symmetric counterpart to self-hosted sandboxes: where self-hosted sandboxes keep tool *execution* inside the customer perimeter, MCP tunnels keep tool *reach* inside the perimeter.

**Managed Agents**
A hosted-runtime model in which the agent harness's substrate -- sandbox, session state, scoped tool execution, tracing -- is operated by the model vendor rather than the developer. Anthropic shipped the first commercial example in public beta on April 8, 2026 ([platform.claude.com/docs/en/managed-agents/overview](https://platform.claude.com/docs/en/managed-agents/overview)). Per SiliconANGLE launch coverage, pricing is standard API token rates plus a per-agent-runtime-hour fee for the substrate (the per-hour figure is not in primary Anthropic documentation). Distinct from cloud-native triggering surfaces (e.g. Claude Code Routines), which sit on top of a Managed Agents-style substrate but answer a different question ("what makes the loop start").

**Mechanistic Interpretability**
A research program that aims to identify human-understandable circuits inside a model's weights -- the specific features, heads, and pathways that implement a given behavior. Named one of MIT Technology Review's 10 Breakthrough Technologies of 2026, it underpins April 2026 results such as emotion vectors, iteration heads, and CoT monitoring.

**Memory Foundation Model**
A July 2026 claim (MemTensor's Metis, arXiv 2607.26760) that agent memory should live as persistent, dynamically-evolving state inside the transformer backbone itself -- parametric, not external. The prototype trains a "hyper memory block" and "local memory block" (inspired by Fast Weight Programming) on top of a frozen Qwen3.5 backbone at 4B / 9B / 27B scale, updating memory at inference through a gradient-free, EMA-style forward pass rather than a vector-store write or a Titans-style gradient update. Self-reported limitations include long-horizon information loss under fixed-size compression and "information confusion in some cases, possibly caused by the blending of semantics within the latent space" -- a research preview, not yet a validated production pattern. See Chapter 6.

**mHC (Manifold-Constrained Hyper-Connections)**
DeepSeek's April 2026 architectural proposal that extends residual connections by routing multiple internal information streams along a learned low-dimensional manifold. It generalizes the single residual stream used in Transformer++-style models into several coordinated streams; as of publication the result is flagged as awaiting independent replication.

**MIRAS**
A memory-augmented training framework from Google Research that provides the recipes, stability guarantees, and learning dynamics for architectures like Titans, where memory is a trainable neural module updated at inference time. MIRAS is the framework that makes learn-while-you-infer tractable without the memory module diverging.

**MoE (Mixture of Experts)**
A model architecture where only a subset of the model's "brain" activates for any given input, making it possible to build very large models that remain fast because not every part runs every time.

### O

**Obsidian**
A note-taking application that stores your notes as plain text files on your own computer and lets you link them together into a personal knowledge base.

**Org Graph / Work Graph**
The two graph objects in graph engineering, from Yash Thakker's July 2026 explainx.ai guide: the *org graph* is the stable chart of which agents exist, what each is for, and which delegation edges are permitted; the *work graph* is the ephemeral task decomposition a particular job spawns, executes, and discards. Like a company's org chart versus the ad hoc working group assembled for one project and dissolved afterward. See **Graph Engineering**; Chapter 14.

**Outcomes (Anthropic)**
A public-beta managed-agent primitive (Anthropic, May 6, 2026) where the agent iterates against a separate grader running in its own context window until a rubric is satisfied. Productizes the Ralph-loop / CATTS uncertainty-steered iteration pattern as an API contract: the caller writes a rubric, the substrate runs the iterate-and-grade loop on the agent's behalf, and only converged results return to the caller.

**Outer Loop**
The judgment layer a human keeps while agents run the inner execution loop (investigate, implement, test/verify, report). From Addy Osmani's July 2026 follow-up "Own the Outer Loop," which structures it as three pillars --- Quality (back-pressure checks before agents act), Verdict ("the final decision we make before work enters our dependent system"), and Answerability ("the guarantee that if someone asks, I can explain why"). Osmani names three failure modes of over-delegating it: cognitive debt (erosion of your understanding of how to solve problems), cognitive surrender (blindly accepting what AI gives you), and the orchestration tax (spinning up more agents than your judgment can cover). The complement to **Loop Engineering** and **Generator-Evaluator Split**: the loop is only as good as the outer loop around it. See Chapter 13.

### P

**Progressive Disclosure**
A design principle where you show only the essential information first and reveal more detail on demand. Like a FAQ page: you see the questions, and click to expand the answers you actually need.

**Prompt Engineering**
The craft of writing instructions to an AI model in a way that gets the best possible response. Small changes in wording can produce very different results.

### R

**RAG (Retrieval-Augmented Generation)**
A technique where the AI looks up relevant information from an external source before answering, so its response is grounded in actual data rather than relying solely on what it memorized during training.

**Routines (Claude Code)**
Anthropic's April 2026 cloud-native harness primitive for Claude Code, in which agent workflows run on Anthropic's cloud rather than the user's machine and can be triggered by a schedule, an API call, or a GitHub event. Routines generalize self-hosted cron-plus-daemon patterns into a managed substrate with quota tiers (Pro 5/day, Max 15/day, Team/Enterprise 25/day) and survive the user's laptop being offline.

### S

**Safety-Tiered Distribution**
Shipping one model family as parallel tiers that differ in safeguard level and distribution gate rather than in weights. The reference example is Anthropic's June 2026 pair: **Claude Fable 5** (public GA with dual-use safety measures, including refusal-as-`stop_reason`) and **Claude Mythos 5** (the same underlying weights with safeguards lifted, gated to the vetted Glasswing coalition). It contrasts with vendor-chosen access tiers like GPT-5.5 Trusted Access for Cyber --- and, by mid-2026, with government-imposed ones like GPT-5.6's Executive-Order-gated preview. The trade-off it encodes: capability and safety are unbundled from each other, so who you are (a vetted org versus a public user) determines which safeguard tier you reach, not what the model can do.

**Self-Hosted Sandbox**
A Managed Agents deployment shape shipped by Anthropic in public beta on May 19, 2026 (Code with Claude London). The agent loop -- orchestration, context management, error recovery -- stays on Anthropic's infrastructure, while tool *execution* moves to the customer's own environment or a managed sandbox provider (Cloudflare, Daytona, Modal, Vercel are first-party supported). Reframes Managed Agents from "fully Anthropic-hosted" to "Anthropic-orchestrated, customer-perimeter-respecting" -- the harness engineer picks layer by layer which pieces of the loop live where, instead of choosing between fully self-hosted and fully managed.

**Self-RAG**
A version of RAG where the AI evaluates its own retrieved information and generated answer for quality, deciding whether to retrieve more or revise its response before giving you the final result.

**Session-hour pricing** (also reported as *agent-runtime-hour pricing*)
A billing model that meters the orchestrator seat -- the substrate on which an agent loop runs -- separately from inference. First introduced commercially by Anthropic Managed Agents (April 8, 2026) at standard token rates plus eight cents per agent runtime hour, per SiliconANGLE launch coverage. The per-hour figure is not in primary Anthropic documentation and is cited from secondary tech-press. Notable because it is the first vendor primitive to put a number on the cost of "where the loop runs," distinct from the cost of "what the loop thinks." The exact phrasing varies between primary docs (which speak of *sessions*) and tech-press coverage (which uses *agent runtime hour*); both refer to the same metering surface.

**Skill (AI Agent Skill)**
A reusable, packaged capability that an AI agent can invoke -- like a recipe it follows for a specific task such as "review this PR" or "run a daily review."

**Stateless MCP**
The architectural shift introduced in the MCP 2026-07-28 Release Candidate (locked May 21, 2026) and shipped final in the 2026-07-28 specification (July 28, 2026): the protocol core no longer uses an `initialize` / `initialized` handshake or `Mcp-Session-Id` headers. Client metadata travels in `_meta` on every request, so any MCP request can land on any server instance -- no sticky routing, no shared session store. Resolves the horizontal-scaling friction that surfaced with Streamable HTTP adoption in 2025. The durable-state primitives that motivated the *stateful* turn (SEP-1686 Tasks, AgentCore bidirectional runtime) are re-implemented on top of the stateless core, as extensions, rather than baked into every request. Stateless core + stateful work on top, not stateful all the way down.

**Skill Graph**
A map of all the skills an AI agent has available, including how they relate to each other and when each one should be triggered.

**Skill Supply-Chain Attack**
A malicious or trojanized agent skill distributed through a skill registry or marketplace. The defining 2026 mechanism is a time-of-check-to-time-of-use gap: static scanners vet the *submitted package snapshot*, but a skill that fetches external content --- or unpacks a hidden payload --- at agent runtime can change its behavior after vetting. AIR's June 2026 disclosure hijacked roughly 26,000 agents this way with a single fake skill behind an external URL, and the "Cloak and Detonate" research (July 2026) showed evasion succeeding more than 90% of the time against eight scanners, with runtime behavioral detection (97% at a 2% false-positive rate) as the countermeasure direction. The lesson mirrors MCP's (see **MCP**): once **Progressive Disclosure** (see **Progressive Disclosure**) and registry-scale distribution make the skill file an attack surface, trust has to move from publish-time scanning to runtime containment.

**System Prompt**
Hidden instructions given to an AI model before your conversation begins, setting its role, rules, and behavior. Like a job description the employee reads before their first day.

### T

**Task Budget**
A harness primitive introduced by Anthropic in Claude Opus 4.7 (April 2026, beta header `anthropic-beta: task-budgets-2026-03-13`). The caller declares an advisory token budget for an entire agentic loop --- thinking, tool calls, tool results, final output --- and the model receives a running countdown as it works, using it to decide how much searching, reasoning, and synthesis a step still deserves. Distinct from `max_tokens`, which is a hard cap that is not visible to the model. Budgets are advisory rather than enforced, with a 20K-token minimum to prevent degenerate refusal behavior on tight budgets. Task budgets are the first vendor-shipped primitive that exposes "how hard to think about each step" as a managed contract rather than a hand-tuned parameter.

**Titans**
Google Research's April 2026 architecture family in which memory is a trainable neural module that updates itself by gradient descent at inference time, rather than an external vector store or a fixed attention window. At comparable parameter counts Titans reportedly outperforms Mamba-2, Gated DeltaNet, and Transformer++ on long-range recall and multi-hop reasoning benchmarks, blurring the line between "context" and "fine-tuning."

**Token**
The basic unit an AI model reads and writes -- roughly three-quarters of a word in English. Models think in tokens, and pricing and context limits are measured in them.

**Tool Use / Function Calling**
The ability of an AI model to trigger external actions -- like searching the web, running code, or calling an API -- instead of only generating text.

### V

**Vector Database**
A database purpose-built to store and search embeddings, making it fast to find the most similar items among millions of entries. The engine behind most RAG systems.

### W

**Wikilink**
A double-bracketed link (like `[[Note Title]]`) used in tools such as Obsidian to connect one note to another, creating a web of linked knowledge.

### X

**x402**
An open protocol reviving HTTP status code 402 ("Payment Required") for in-band stablecoin payment between machines, used for agent-to-resource transactions. Originated by Coinbase; first hyperscaler-managed implementation in AWS AgentCore Payments (May 7, 2026). The "value-layer" analogue of MCP for the tool layer --- where MCP standardizes how an agent reaches an API, x402 standardizes how it pays the API. Prior traction before AWS endorsement: 69,000 active agents and ~$50M cumulative volume by late April 2026.

---

[Back to README](README.md)
