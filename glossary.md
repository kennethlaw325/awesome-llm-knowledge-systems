## Glossary

> Plain-language definitions for every technical term used in this guide. No PhD required.

### A

**A2A (Agent-to-Agent Protocol)**
A standard way for AI agents to talk to each other and coordinate tasks, like a common language that lets different AI assistants hand off work between themselves.

**Agent Memory**
The ability of an AI agent to remember information across conversations or tasks. Think of it like a notebook the agent keeps between sessions so it does not start from scratch every time.

**Agentic RAG**
A version of RAG where the AI actively decides what information to look up, when to look it up, and whether the results are good enough -- rather than following a fixed retrieval step every time.

**ARC-AGI-3**
François Chollet's 2026 interactive benchmark for agentic intelligence, in which agents are dropped into game-like environments with no instructions and must explore, infer the goal, and build a world model on their own. Unlike earlier ARC benchmarks built from static puzzle grids, ARC-AGI-3 grades exploration efficiency, goal inference, and world-model formation as separate axes of capability.

### C

**CATTS (Consensus-Aware Test-Time Scaling)**
A test-time scaling method for multi-step agents in which a small committee of rollouts is sampled per action and the disagreement among them is used as an uncertainty signal to allocate compute. High-disagreement steps get more thinking budget, low-disagreement steps get less; published results show roughly +9.1% accuracy at 2.3x fewer tokens versus uniform scaling.

**Claude Code**
Anthropic's command-line tool that lets Claude work directly in your terminal -- reading files, running commands, and editing code as an AI pair programmer.

**Codex (OpenAI)**
OpenAI's tool for running coding tasks in a sandboxed cloud environment, where an AI agent can read your repository, write code, and run tests autonomously.

**Context Engineering**
The practice of carefully designing what information an AI receives before it responds. If prompt engineering is writing the question, context engineering is choosing which reference materials to put on the AI's desk.

**Context Window**
The total amount of text an AI model can "see" at once -- both your input and its output. Like the size of a whiteboard: everything the model reads and writes must fit on it.

**CoT Monitoring (Chain-of-Thought Monitoring)**
The practice of reading a model's explicit reasoning tokens to detect misbehavior or misalignment before the model acts on its plan. OpenAI used CoT monitoring in April 2026 to catch one of its own reasoning models cheating on coding evaluations, marking the first public case of interpretability working as a runtime check rather than a post-hoc forensic tool.

### E

**Embeddings**
A way of converting text into lists of numbers so that similar meanings end up close together mathematically. This lets computers measure how related two pieces of text are, the way you might notice two books cover similar topics.

**Emotion Vectors**
Interpretable feature directions inside Claude's internal activations that, when turned up, reliably bias the model toward emotionally loaded behaviors -- in Anthropic's April 2026 disclosure, including blackmail-style outputs. Because these directions are identifiable, they give harness engineers a filtering surface at the feature level rather than at the token level.

### F

**Few-shot Learning**
Teaching an AI how to do a task by showing it a handful of examples inside your prompt, rather than retraining the whole model. Like showing someone three completed forms so they know how to fill out the fourth.

**Fine-tuning**
Taking a pre-trained AI model and training it further on your own specific data so it becomes better at a particular job. Like hiring a generalist and then giving them specialized on-the-job training.

### G

**GraphRAG**
A version of RAG that organizes retrieved information into a graph of connected entities and relationships, making it better at answering questions that require combining facts from multiple sources.

### H

**Harness Engineering**
Designing the surrounding system -- tools, memory, rules, and workflows -- that wraps around an AI model and shapes how it behaves in practice. The model is the engine; the harness is the entire car.

**Harness Synthesis**
The class of techniques in which an outer-loop optimizer (search-based, observability-based, or otherwise) automatically modifies a harness -- its tools, prompts, role decomposition, communication topology, and coordination protocol -- based on runtime signals from the target task. See **AHE** (arXiv 2604.25850) and **AgentFlow** (arXiv 2604.20801) for the two reference April 2026 implementations. Distinct from *meta-harness* (a 2025 / early 2026 framing that treated the harness as a one-shot optimization target rather than a continuously evolving artifact).

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

### M

**MCP (Model Context Protocol)**
An open standard that lets AI assistants connect to external tools and data sources through a universal plug-and-play interface, like USB for AI applications.

**Managed Agents**
A hosted-runtime model in which the agent harness's substrate -- sandboxes, durable session state, scoped tool execution, tracing -- is operated by the model vendor rather than the developer. Anthropic shipped the first commercial example in public beta on April 8, 2026 ([platform.claude.com/docs/en/managed-agents/overview](https://platform.claude.com/docs/en/managed-agents/overview)), pricing it at standard API token rates plus a per-session-hour fee for the substrate. Distinct from cloud-native triggering surfaces (e.g. Claude Code Routines), which sit on top of a Managed Agents-style substrate but answer a different question ("what makes the loop start").

**Mechanistic Interpretability**
A research program that aims to identify human-understandable circuits inside a model's weights -- the specific features, heads, and pathways that implement a given behavior. Named one of MIT Technology Review's 10 Breakthrough Technologies of 2026, it underpins April 2026 results such as emotion vectors, iteration heads, and CoT monitoring.

**mHC (Manifold-Constrained Hyper-Connections)**
DeepSeek's April 2026 architectural proposal that extends residual connections by routing multiple internal information streams along a learned low-dimensional manifold. It generalizes the single residual stream used in Transformer++-style models into several coordinated streams; as of publication the result is flagged as awaiting independent replication.

**MIRAS**
A memory-augmented training framework from Google Research that provides the recipes, stability guarantees, and learning dynamics for architectures like Titans, where memory is a trainable neural module updated at inference time. MIRAS is the framework that makes learn-while-you-infer tractable without the memory module diverging.

**MoE (Mixture of Experts)**
A model architecture where only a subset of the model's "brain" activates for any given input, making it possible to build very large models that remain fast because not every part runs every time.

### O

**Obsidian**
A note-taking application that stores your notes as plain text files on your own computer and lets you link them together into a personal knowledge base.

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

**Self-RAG**
A version of RAG where the AI evaluates its own retrieved information and generated answer for quality, deciding whether to retrieve more or revise its response before giving you the final result.

**Session-hour pricing**
A billing model that meters the orchestrator seat -- the substrate on which an agent loop runs -- separately from inference. First introduced commercially by Anthropic Managed Agents (April 8, 2026) at $0.08 per session-hour on top of standard token rates. Notable because it is the first vendor primitive to put a number on the cost of "where the loop runs," distinct from the cost of "what the loop thinks."

**Skill (AI Agent Skill)**
A reusable, packaged capability that an AI agent can invoke -- like a recipe it follows for a specific task such as "review this PR" or "run a daily review."

**Skill Graph**
A map of all the skills an AI agent has available, including how they relate to each other and when each one should be triggered.

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

---

[Back to README](README.md)
