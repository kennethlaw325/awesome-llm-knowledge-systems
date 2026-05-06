# Chapter 3: Context Engineering -- The Art of Filling the Window

> **In one sentence:** Context engineering is the art of giving AI exactly the right information at the right time -- not too much, not too little.
>
> **Why it matters:** Better context means better AI answers. This is why some people get amazing results from AI while others get generic responses.

> "Context engineering is the delicate art and science of filling the context window with just the right information for the next step."
> -- Andrej Karpathy, June 2025

If prompt engineering is writing a good question, context engineering is building the entire briefing packet that surrounds it. The shift from one to the other marks a fundamental change in how practitioners think about LLM systems: the unit of design is no longer a single instruction but an *information environment*.

This chapter maps the landscape -- from theoretical frameworks to production-tested patterns -- and points you to the primary sources that define the discipline.

---

## 3.1 From Prompts to Contexts

The term "context engineering" entered mainstream usage in mid-2025 when Karpathy drew a sharp line between it and prompt engineering. A prompt is a static string. A context is a dynamically assembled package of everything the model needs -- instructions, memory, retrieved documents, tool definitions, conversation history, and the immediate task -- composed programmatically and updated at every turn.

The distinction matters because modern agents rarely send the same context twice. Each inference call is the product of routing logic, retrieval pipelines, compression heuristics, and tool availability checks that together determine what fills the window and what gets left out.

## 3.2 A Six-Layer Context Model

Drawing on patterns described in Anthropic's [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents) and adjacent practitioner writing, the context window can usefully be decomposed into six conceptual layers, ordered from most persistent to most ephemeral. The labels here are this guide's pedagogical synthesis, not a taxonomy Anthropic itself publishes:

| Layer | Contents | Typical Persistence |
|-------|----------|-------------------|
| **System Rules** | Safety constraints, persona definitions, behavioral guardrails | Static per deployment |
| **Memory** | User preferences, prior session summaries, learned facts | Cross-session |
| **Retrieved Documents** | RAG results, search snippets, file contents | Per-turn |
| **Tool Schemas** | Function definitions, API specs, capability declarations | Per-session or masked per-turn |
| **Conversation History** | Prior messages, assistant responses, tool call results | Sliding window |
| **Current Task** | The immediate user request plus any task-specific injections | Per-turn |

The key insight is that each layer has different update frequencies, different compression strategies, and different failure modes. Over-stuffing the Retrieved Documents layer drowns the Current Task signal. Under-populating Memory forces the model to re-derive context it should already have. Good context engineering is about balance across all six layers simultaneously.

## 3.3 Lessons from Manus: KV-Cache as the North Star

In July 2025, Yichao "Peak" Ji (CTO of Manus) published a set of production lessons that reframed context engineering around a single operational metric: **KV-cache hit rate**.

Manus observed a consistent 100:1 ratio between input and output tokens in their agent system. At that ratio, input cost dominates everything. KV-cache hits -- where previously computed key-value pairs are reused rather than recomputed -- become the primary lever for both latency and cost.

Three techniques emerged from this insight:

1. **Append-only context structure.** Never rewrite earlier portions of the context. Insertions or edits in the middle invalidate cached prefixes, forcing full recomputation. Design your context as a log, not a document.

2. **Tool masking via logit bias, not schema removal.** When a tool is temporarily unavailable, Manus suppressed its selection through logit-level masking rather than removing the tool definition from the context. Removing definitions changes the token sequence, busting the cache. Masking preserves the prefix while preventing selection.

3. **Rolling todo-list rewrites.** Rather than relying on the model to recall objectives from early in a long conversation, Manus periodically appended a rewritten todo list near the end of the context. This exploits recency bias in attention -- objectives in the most recent tokens receive stronger attention weight than identical objectives buried thousands of tokens earlier.

These are infrastructure-level decisions, not prompt-level ones. They illustrate why "context engineering" requires systems thinking.

## 3.4 Five Dominant Patterns

Aurimas Griciūnas synthesized the emerging practice into five recurring patterns observed across production systems (canonical write-up: "State of Context Engineering in 2026," SwirlAI Newsletter, March 22, 2026, [https://www.newsletter.swirlai.com/p/state-of-context-engineering-in-2026](https://www.newsletter.swirlai.com/p/state-of-context-engineering-in-2026); see also "Breaking Down Context Engineering"):

**Progressive Disclosure.** Do not load everything upfront. Present a lightweight index first; expand sections only when the model (or routing logic) determines they are relevant. This is the context-window equivalent of lazy loading. Anthropic's own agent skills system uses this pattern -- 17 skills consume roughly 1,700 tokens at rest, expanding only on invocation.

**Context Compression.** Summarize, truncate, or distill information before injection. Conversation history beyond a sliding window gets compressed into summaries. Retrieved documents get excerpted to relevant passages. The goal is to preserve semantic density while reducing token count.

**Context Routing.** Not all queries need the same context. A routing layer examines the incoming request and selects which memory banks, tool sets, and document collections to include. This is the context-window analog of a database query planner.

**Retrieval Evolution.** Static RAG (retrieve once, inject, generate) gives way to iterative retrieval where the model can request additional information mid-generation. The context is not assembled once but evolves through the generation process.

**Tool and Capability Management.** As tool libraries grow, loading all schemas becomes prohibitive. Systems use meta-tool patterns (a discovery tool that returns relevant tool schemas on demand) or skill-graph architectures to keep the tool layer lean.

## 3.5 The Academic Landscape

Mid-2025 brought the first comprehensive academic survey of context engineering as a formal research area: **"A Survey of Context Engineering for Large Language Models"** (Mei et al., arXiv 2507.13334, July 17-21, 2025), which through systematic analysis of over 1,400 research papers established a technical roadmap for the field. The survey organizes the design space along two axes: **foundational components** (context retrieval and generation, context processing, context management) and **system implementations** (RAG, memory systems, tool-integrated reasoning, multi-agent systems). Its load-bearing finding is a fundamental capability asymmetry: current models are remarkably proficient at understanding complex contexts but exhibit pronounced limitations in generating equally sophisticated long-form outputs. For practitioners, the survey is the closest thing the field has to a textbook --- it formalized what had been discovered empirically that context engineering is not a single technique but a design space with multiple independent dimensions.

## 3.6 Agentic Context Engineering (ACE)

The ACE paper, **"Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models"** (Zhang et al., arXiv 2510.04618, October 6, 2025; companion repo at [github.com/ace-agent/ace](https://github.com/ace-agent/ace)), introduced a conceptual shift: treating contexts not as static assemblies but as **evolving playbooks**. In an ACE system, the context is a living document that the agent itself maintains --- adding observations, updating plans, pruning irrelevant history, and restructuring its own instructions based on task progress. Reported headline gains: +10.6% on agent benchmarks and +8.6% on finance tasks, with reductions in adaptation latency and rollout cost; on the AppWorld leaderboard, ACE matches the top-ranked production-level agent on the overall average and surpasses it on the harder test-challenge split despite using a smaller open-source model. ACE also names the failure modes it is engineered against: **brevity bias** (drops domain insights for concise summaries) and **context collapse** (iterative rewriting erodes details over time).

This moves context engineering from a purely infrastructure concern (what the harness assembles before each call) into a collaborative one (what the harness prepares *and* what the model actively reshapes). The boundary between "context the system provides" and "context the model creates" becomes fluid.

ACE systems typically maintain a structured scratchpad within the context -- a designated region where the model writes working notes, intermediate results, and revised plans. The harness preserves this region across turns while managing the surrounding layers according to its own policies.

## 3.7 Practical Implications

Several principles emerge from this landscape:

- **Measure input tokens, not just output.** At production scale, the 100:1 input/output ratio means context assembly cost dominates. Optimize for cache hits and minimal redundancy.
- **Design contexts as layered systems.** Each layer has its own update policy, compression strategy, and failure mode. Treat them independently.
- **Use progressive disclosure by default.** Start lean. Expand on demand. The cost of including irrelevant information is not just tokens -- it is degraded attention and increased hallucination risk.
- **Test context composition, not just prompts.** The same prompt in different contexts produces different results. Your test suite should vary the context, not just the final instruction.
- **Anticipate model improvements.** As models get better at long-context reasoning, some compression and routing strategies become unnecessary overhead. Build with clear abstraction boundaries so layers can be simplified or removed.

---

## Sources

- **Karpathy, Andrej.** Public remarks on "context engineering" (mid-2025). Widely-shared framing across X and the AI engineering community that coined the working definition adopted across the field.
- **Anthropic.** "Building Effective Agents." Anthropic engineering blog, December 19, 2024. [https://www.anthropic.com/engineering/building-effective-agents](https://www.anthropic.com/engineering/building-effective-agents) --- describes orchestrator-worker patterns and evaluator-optimizer workflows; this guide labels the six conceptual layers in §3.2 pedagogically.
- **Ji, Yichao "Peak"** (Manus). "Context Engineering Lessons from Building Manus." Blog post, July 2025. [manus.im/blog](https://manus.im/blog) --- KV-cache hit rate as the operational metric, append-only context structure, tool masking via logit bias, rolling todo-list rewrites.
- **Griciūnas, Aurimas.** "State of Context Engineering in 2026." SwirlAI Newsletter, March 22, 2026. [https://www.newsletter.swirlai.com/p/state-of-context-engineering-in-2026](https://www.newsletter.swirlai.com/p/state-of-context-engineering-in-2026). See also "Breaking Down Context Engineering": [https://www.newsletter.swirlai.com/p/breaking-down-context-engineering](https://www.newsletter.swirlai.com/p/breaking-down-context-engineering)
- **Mei, Lingrui et al.** "A Survey of Context Engineering for Large Language Models." arXiv 2507.13334, July 17-21, 2025. [https://arxiv.org/abs/2507.13334](https://arxiv.org/abs/2507.13334) --- 1,400+ paper review establishing context engineering as a formal research area.
- **Zhang, Qizheng et al.** "Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models." arXiv 2510.04618, October 6, 2025. [https://arxiv.org/abs/2510.04618](https://arxiv.org/abs/2510.04618). Companion repo: [github.com/ace-agent/ace](https://github.com/ace-agent/ace). Frames contexts as evolving playbooks; names brevity bias and context collapse.
- **Schmid, Philipp.** "The New Skill in AI is Not Prompting, It's Context Engineering" and follow-up. [https://www.philschmid.de/context-engineering](https://www.philschmid.de/context-engineering); [https://www.philschmid.de/context-engineering-part-2](https://www.philschmid.de/context-engineering-part-2)
- **LangChain blog.** Context-engineering coverage at [blog.langchain.com](https://blog.langchain.com) --- the Agent Engineer framing as a practitioner pattern (no single canonical post; cited as discourse anchor).
- **Willison, Simon.** Ongoing AI engineering coverage at [simonwillison.net](https://simonwillison.net) --- accessible practitioner introductions that connect the ecosystem.
