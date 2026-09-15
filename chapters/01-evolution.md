# Chapter 01: The Three Generations

> **In one sentence:** AI engineering has evolved from writing good prompts to designing entire operating systems around AI models.
>
> **Why it matters:** Understanding where the field is heading helps you pick the right tools and avoid outdated approaches.

**From prompt engineering to context engineering to harness engineering -- and why the boundaries between them matter less than you think.**

---

## Generation 1: Prompt Engineering (2022-2024)

When ChatGPT launched in November 2022, the entire interface between humans and large language models was a text box. The discipline that emerged was prompt engineering: the art and science of crafting input text to get better output.

The core techniques developed rapidly:

**Few-shot prompting** (Brown et al., 2020) demonstrated that including examples in the prompt could dramatically improve task performance without any fine-tuning. Instead of training a model to classify sentiment, you showed it three examples and asked it to classify the fourth.

**Chain-of-thought (CoT) prompting** (Wei et al., 2022) showed that adding "Let's think step by step" or including reasoning traces in examples could unlock multi-step reasoning capabilities that appeared absent in standard prompting. This was arguably the first hint that *how you structured context* mattered as much as *what you asked*.

**Prompt templates** became the standard abstraction. LangChain, LlamaIndex, and dozens of frameworks offered templating systems where variables could be injected into carefully crafted prompt structures. The mental model was clear: the prompt is the program, the model is the runtime.

Other techniques from this era include:

- **ReAct** (Yao et al., 2022): Interleaving reasoning and action steps, letting models plan and execute tool calls within a single prompt structure.
- **Tree of Thought** (Yao et al., 2023): Exploring multiple reasoning paths and selecting the best one.
- **Self-consistency** (Wang et al., 2022): Sampling multiple reasoning chains and taking a majority vote.

The limitation of this era was its assumption: that the quality of an LLM interaction was primarily determined by the quality of the prompt. This was true when context windows were 4K-8K tokens and the only input was user text. It stopped being true once models could ingest 100K+ tokens and call external tools.

### What this era got right

Prompt engineering established that *structure matters*. The difference between a good and bad prompt is not vibes -- it is information architecture. That insight carried forward into everything that came next.

### What this era missed

It treated the context window as a static artifact. You crafted a prompt, submitted it, and got a response. The idea that the context window itself could be *dynamically constructed* from multiple sources at runtime -- that was the next generation's insight.

---

## Generation 2: Context Engineering (2025)

In mid-2025, Andrej Karpathy posted what became one of the most reshared observations in the AI engineering community:

> "I've been thinking about this and I think the right term for what most people actually need to get good at is not 'prompt engineering' but 'context engineering.' The art and science of filling the context window with just the right information for the next step."

This reframe was significant because it shifted attention from the *instruction* (prompt) to the *entire information package* (context window). A modern LLM call's context window contains far more than a user prompt:

- System instructions defining behavior and constraints
- Retrieved documents from RAG pipelines
- Tool definitions and schemas
- Conversation history (selectively compressed)
- Few-shot examples chosen dynamically
- Structured metadata about the current task

The prompt is one component. Context engineering is about orchestrating all of them.

### The Six Techniques

[Towards AI's analysis](https://towardsai.net/) of context engineering identified six core techniques that define the discipline:

1. **Retrieval-Augmented Generation (RAG)**: Pulling relevant documents at query time
2. **Tool and API integration**: Giving models access to external capabilities with structured schemas
3. **Memory management**: Maintaining relevant information across conversation turns and sessions
4. **Dynamic prompt construction**: Assembling prompts from templates, retrieved content, and runtime state
5. **Context window optimization**: Managing what goes in and what stays out of limited token budgets
6. **Instruction hierarchy**: Layering system, developer, and user instructions with clear precedence

### Lessons from Manus

[Manus](https://manus.im/), the AI agent platform that became one of the most talked-about products of 2025, shared critical lessons about context engineering at scale:

**The KV-cache insight**: Manus engineered their context window to maintain high KV-cache hit rates -- ensuring that previously computed key-value pairs from the attention mechanism could be reused across turns. This reduced latency and cost dramatically. The principle: structure your context so that the *prefix stays stable* while only the *suffix changes* between calls.

**The 100:1 ratio**: Manus reported that for every 1 token of model output, approximately 100 tokens of context were consumed. This inverted the common assumption that output tokens were the primary cost driver. The real engineering challenge was not generating text -- it was *selecting which context to feed*.

**Context as product**: Manus treated context window construction as a core product feature, not an implementation detail. The quality of their agent was directly proportional to the quality of their context assembly pipeline.

### The taxonomy shift

Context engineering reframed LLM application development from "write good prompts" to "build good information pipelines." The model became a reasoning engine that operated on whatever context it received. The engineering challenge moved upstream -- to retrieval, filtering, ranking, compression, and assembly.

But even this framing had a ceiling. It described *what goes into the model* but not *how the system around the model operates*. That required another shift.

---

## Generation 3: Harness Engineering (2026)

From late 2025 through early 2026, two influential pieces formalized the next evolution:

**Birgitta Böckeler** (ThoughtWorks), writing in Martin Fowler's *Exploring Generative AI* memo series in April 2026, published an analysis arguing that the most impactful engineering work in LLM applications was happening not in model training or prompt crafting, but in *the harness* -- the surrounding system of tools, routing, memory, planning, and error recovery that orchestrates model calls into reliable workflows.

**OpenAI's Codex team** has published case-study material on the harness side of agentic coding (see openai.com/index/introducing-codex for the public-facing material). The widely-cited "three engineers / ~1M lines / ~1,500 PRs" figure circulated in 2025-2026 OpenAI talks and posts; the underlying observation is that Codex's quality was primarily determined not by the model but by the harness -- the system that decided *when* to call the model, *what context* to provide, *which tools* to make available, and *how* to validate and recover from errors.

### The Phil Schmid Analogy

[Phil Schmid](https://www.philschmid.de/) (Hugging Face) offered the analogy that crystallized the concept:

- **The model is the CPU** -- raw compute capability
- **The context window is RAM** -- the working memory for the current operation
- **The harness is the operating system** -- scheduling, resource management, I/O, error handling, and the user interface

This analogy clarifies why harness engineering matters: nobody ships a CPU without an OS. The model is necessary but not sufficient. The harness determines what the model can actually accomplish.

### The Meta-Harness Paper and the 6x Gap

Research published in early 2026 quantified what practitioners already suspected: the gap between a bare model and a well-harnessed model was approximately **6x on complex tasks**. The same model, with the same weights, with the same training data, produced results that varied by a factor of six depending on the quality of its harness.

This meant that harness engineering offered more leverage than model improvement for most practical applications. A better harness on a good model outperformed a great model with a mediocre harness.

### The IMPACT Framework

In mid-2020s practitioner discourse, the IMPACT mnemonic emerged as a checklist for evaluating harness quality:

- **I**nstructions -- clarity and completeness of system instructions
- **M**emory -- persistence and retrieval across sessions
- **P**lanning -- task decomposition and sequencing
- **A**ctions -- tool availability and reliability
- **C**ontext -- dynamic assembly of relevant information
- **T**esting -- evaluation and quality assurance loops

IMPACT positions context engineering as one component (the "C") within the broader harness engineering discipline. This nesting is the key structural insight: context engineering is *within* harness engineering, not replaced by it.

### Meta Acquires Manus (~$2B)

In early 2026, Meta acquired Manus for approximately $2 billion. The acquisition was widely interpreted as Meta buying *the harness, not the model*. Meta already had Llama. What it did not have was a production-proven system for context assembly, tool orchestration, and agent runtime management.

The acquisition validated the thesis: the most valuable engineering in the LLM ecosystem was increasingly in the orchestration layer, not the model layer.

---

## The Key Insight: Coexistence, Not Replacement

These three generations are not clean historical periods where one replaces the next. They are *nested layers* that coexist in every production system:

```
+--------------------------------------------------+
|              HARNESS ENGINEERING                  |
|  +--------------------------------------------+  |
|  |          CONTEXT ENGINEERING                |  |
|  |  +--------------------------------------+  |  |
|  |  |       PROMPT ENGINEERING             |  |  |
|  |  |                                      |  |  |
|  |  |  System prompts, CoT, few-shot,      |  |  |
|  |  |  instruction formatting              |  |  |
|  |  +--------------------------------------+  |  |
|  |                                            |  |
|  |  RAG pipelines, memory, tool schemas,      |  |
|  |  context window optimization               |  |
|  +--------------------------------------------+  |
|                                                  |
|  Skill routing, planning loops, error recovery,  |
|  progressive disclosure, multi-agent coord       |
+--------------------------------------------------+
```

A harness engineer still writes prompts. They still do context engineering. But they also build the *system* that decides which prompts to use when, which context to assemble for each situation, and how to recover when things go wrong.

The evolution is not about abandoning earlier techniques. It is about recognizing that they are necessary but insufficient -- and building the layers above them that turn raw LLM capability into reliable, production-grade applications.

A 19-author survey from Shanghai Jiao Tong and collaborators, **"Externalization in LLM Agents: A Unified Review of Memory, Skills, Protocols and Harness Engineering"** (arXiv 2604.08224, April 9, 2026), independently arrives at the same three-layer organization this chapter uses: the field's progression, in their framing, runs from *weights* to *context* to *harness*, and they treat memory, skills, protocols, and harness engineering as four externalized components unified by harness as the integration layer. The convergence is worth flagging for readers coming from the academic literature: this is not a practitioner-only framing and it is not unique to this guide --- it is the organizing axis that the academic survey of late April 2026 also chose.

---

## An Emerging Fourth Generation? Loop Engineering (mid-2026)

This chapter's title deliberately stays *The Three Generations*. But in June 2026 a fourth candidate layer crystallized fast enough to note here, even though it is too new to promote into the numbered sequence. Within a single week --- Peter Steinberger's viral June 7 post that you "shouldn’t be prompting coding agents anymore ... You should be designing loops that prompt your agents," Addy Osmani's same-day essay that named **loop engineering**, and Boris Cherny (Claude Code) framing his own job as "writing loops" --- practitioners began describing a layer *above* the harness: the system that prompts the agent for you on a schedule, spawns helpers, and feeds itself.

Its proponents define the relation to Generation 3 precisely. Osmani places loop engineering "one floor above the harness": a loop, in his framing, is the harness "but it runs on a timer, it spawns little helpers, and it feeds itself." That is the same nested logic this chapter already uses --- the loop is simply the outermost box, wrapping harness, context, and prompt, so a loop engineer still writes prompts, still does context engineering, and still builds a harness. What separates a loop from a plain scheduler is that it reads the current state each pass and re-decides, rather than firing a fixed command on a clock.

Two honesty caveats keep this out of the numbered generations for now. The term is roughly five weeks old at the time of writing, lives entirely in practitioner discourse --- blogs, podcasts, X --- with no academic literature behind it, and its reception is split between readers who call it a genuine shift and readers who call it a premature rebranding of scheduling. This guide therefore tracks loop engineering as *emerging* rather than settled, the same posture it takes toward any claim that has not yet cleared primary-source and time-tested scrutiny. [Chapter 13](13-loop-engineering.md) covers the frame in full, with each load-bearing claim tied to a source and the gaps named rather than filled.

The naming machine has since run again. In mid-July 2026, six weeks after the loop week, a second candidate crystallized on the same playbook: **graph engineering**, the claim that above the loop sits the graph --- the explicit wiring of which agents exist, who may delegate to whom, and how their loops supervise and correct one another. Another Steinberger post (dated July 18, 2026 by the sources that date it; July 17 US time is possible) was the catalyst, an essay wave followed within days, and the pushback arrived just as fast: LangChain's official response lists graph engineering after prompt, context, harness, and loop engineering --- and in the same breath argues that representing agentic systems as graphs is three-year-old practice, a loop being simply a directed cyclic graph, so only the name is new. Chapter 14 set an explicit survival gate on the term and ran it on September 15, 2026. The finding was split: graph engineering stayed in circulation --- three months of essays that are not replies to the catalyst, a paid course teaching the agent-organization sense, a September tutorial --- while no vendor adoption of the term was found in the documentation checked, and two vendors shipped the governance the term names without ever using it, one of them starting a month before the term existed. The verdict recorded there is that the term survived as a contested name for multi-agent coordination and that its status as a distinct layer is unproved, so it stays outside the numbered generations. This chapter's own placement of multi-agent coordination inside the harness box remains the live alternative reading rather than a placeholder. [Chapter 14](14-graph-engineering.md) carries the dated scorecard, with the skeptics given equal weight.

---

## Sources

- Brown, T. et al. (2020). "Language Models are Few-Shot Learners." [arXiv:2005.14165](https://arxiv.org/abs/2005.14165)
- Wei, J. et al. (2022). "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models." [arXiv:2201.11903](https://arxiv.org/abs/2201.11903)
- Yao, S. et al. (2022). "ReAct: Synergizing Reasoning and Acting in Language Models." [arXiv:2210.03629](https://arxiv.org/abs/2210.03629)
- Yao, S. et al. (2023). "Tree of Thoughts: Deliberate Problem Solving with Large Language Models." [arXiv:2305.10601](https://arxiv.org/abs/2305.10601)
- Wang, X. et al. (2022). "Self-Consistency Improves Chain of Thought Reasoning in Language Models." [arXiv:2203.11171](https://arxiv.org/abs/2203.11171)
- Karpathy, A. (mid-2025). Public remarks coining "context engineering" as the right term for the discipline; widely-shared framing across X and the AI engineering community.
- Manus. (2025). "Context Engineering Lessons from Building Manus." [manus.im/blog](https://manus.im/blog) --- KV-cache hit rate as the operational metric, append-only context, tool masking via logit bias, rolling todo-list rewrites.
- Böckeler, Birgitta. (April 2, 2026). "Harness engineering for coding agent users." martinfowler.com (*Exploring Generative AI* series). [https://martinfowler.com/articles/harness-engineering.html](https://martinfowler.com/articles/harness-engineering.html) --- Guides vs. Sensors, Computational vs. Inferential taxonomy.
- OpenAI. Codex public-facing material: [https://openai.com/index/introducing-codex](https://openai.com/index/introducing-codex). Anchor for the harness-design framing of Codex; the widely-cited "three engineers / ~1M lines / ~1,500 PRs" figures circulated in 2025-2026 OpenAI talks and posts and are reported here as community-cited rather than from a single canonical post.
- Schmid, Philipp. "The New Skill in AI is Not Prompting, It's Context Engineering" and follow-up. [https://www.philschmid.de/context-engineering](https://www.philschmid.de/context-engineering); [https://www.philschmid.de/context-engineering-part-2](https://www.philschmid.de/context-engineering-part-2) --- Model = CPU, Context = RAM, Harness = OS analogy.
- IMPACT mnemonic. Intent / Memory / Planning / Authority / Control flow / Tools --- a six-dimension harness design checklist that emerged in mid-2020s practitioner discourse. Used in this chapter as a pedagogical framing; not attributed to a specific primary source.
- Meta/Manus acquisition reporting. (2026). Various sources.
- Zhou, C. et al. (April 2026). "Externalization in LLM Agents: A Unified Review of Memory, Skills, Protocols and Harness Engineering." [arXiv:2604.08224](https://arxiv.org/abs/2604.08224) --- 19-author survey from Shanghai Jiao Tong and collaborators that independently uses the Weights → Context → Harness three-layer historical framing. Cited in this chapter's "Coexistence, Not Replacement" section as evidence the practitioner thesis converged with academic literature.
- Steinberger, Peter (@steipete). Post catalyzing the "design loops that prompt your agents" framing (June 7, 2026). [https://x.com/steipete/status/2063697162748260627](https://x.com/steipete/status/2063697162748260627) --- cited in the "Emerging Fourth Generation" section; the post itself does not use the phrase "loop engineering."
- Osmani, Addy. "Loop Engineering" (June 7, 2026). [https://addyosmani.com/blog/loop-engineering/](https://addyosmani.com/blog/loop-engineering/) --- the essay that named the practice; source of the "one floor above the harness" relation used in this chapter's fourth-generation section.
- Cherny, Boris. Lenny's Podcast / Lenny's Newsletter interview (mid-2026). [https://www.lennysnewsletter.com/p/head-of-claude-code-what-happens](https://www.lennysnewsletter.com/p/head-of-claude-code-what-happens) --- the "my job is to write loops" framing; a spoken quote, transcribed inconsistently across outlets.
- Runkle, Sydney and Chase, Harrison (LangChain). "3 Years of Graph Engineering with LangGraph" (July 22, 2026). [https://www.langchain.com/blog/3-years-of-graph-engineering-with-langgraph](https://www.langchain.com/blog/3-years-of-graph-engineering-with-langgraph) --- lists graph engineering after prompt, context, harness, and loop engineering while arguing the practice is three years old; source of the directed-cyclic-graph reduction used in this chapter's emerging-generation section.
- Perez, Carlos E. "From Loop Engineering to Graph Engineering?" Intuition Machine (July 19, 2026). [https://medium.com/intuitionmachine/from-loop-engineering-to-graph-engineering-d3ebeb08511c](https://medium.com/intuitionmachine/from-loop-engineering-to-graph-engineering-d3ebeb08511c) --- the first theoretical expansion of the July 2026 graph-engineering frame; cited for the loops-supervising-loops reading.

---

*Next: [Chapter 02 -- RAG, Long Context & Knowledge Graphs](/chapters/02-knowledge-layer.md)*
