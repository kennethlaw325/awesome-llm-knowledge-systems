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

In late 2025, two influential pieces formalized the next evolution:

**Martin Fowler** published an analysis arguing that the most impactful engineering work in LLM applications was happening not in model training or prompt crafting, but in *the harness* -- the surrounding system of tools, routing, memory, planning, and error recovery that orchestrates model calls into reliable workflows.

**OpenAI's Codex team** published a blog post describing their architecture for agentic coding. The key insight: Codex's quality was primarily determined not by the model but by the harness -- the system that decided *when* to call the model, *what context* to provide, *which tools* to make available, and *how* to validate and recover from errors.

### The Phil Schmid Analogy

[Phil Schmid](https://www.philschmid.de/) (Hugging Face) offered the analogy that crystallized the concept:

- **The model is the CPU** -- raw compute capability
- **The context window is RAM** -- the working memory for the current operation
- **The harness is the operating system** -- scheduling, resource management, I/O, error handling, and the user interface

This analogy clarifies why harness engineering matters: nobody ships a CPU without an OS. The model is necessary but not sufficient. The harness determines what the model can actually accomplish.

### The Meta-Harness Paper and the 6x Gap

Research published in early 2026 quantified what practitioners already suspected: the gap between a bare model and a well-harnessed model was approximately **6x on complex tasks**. The same model, with the same weights, with the same training data, produced results that varied by a factor of six depending on the quality of its harness.

This meant that harness engineering offered more leverage than model improvement for most practical applications. A better harness on a good model outperformed a great model with a mediocre harness.

### swyx's IMPACT Framework

[swyx](https://www.swyx.io/) (Shawn Wang) proposed the IMPACT framework for evaluating harness quality:

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

---

## Sources

- Brown, T. et al. (2020). "Language Models are Few-Shot Learners." [arXiv:2005.14165](https://arxiv.org/abs/2005.14165)
- Wei, J. et al. (2022). "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models." [arXiv:2201.11903](https://arxiv.org/abs/2201.11903)
- Yao, S. et al. (2022). "ReAct: Synergizing Reasoning and Acting in Language Models." [arXiv:2210.03629](https://arxiv.org/abs/2210.03629)
- Yao, S. et al. (2023). "Tree of Thoughts: Deliberate Problem Solving with Large Language Models." [arXiv:2305.10601](https://arxiv.org/abs/2305.10601)
- Wang, X. et al. (2022). "Self-Consistency Improves Chain of Thought Reasoning in Language Models." [arXiv:2203.11171](https://arxiv.org/abs/2203.11171)
- Karpathy, A. (2025). Post on context engineering. [X/Twitter](https://x.com/karpathy)
- Manus. (2025). "Context Engineering Lessons from Building Manus." [manus.im/blog](https://manus.im/blog)
- Fowler, M. (2025). "Harness Engineering for LLM Applications." [martinfowler.com](https://martinfowler.com/)
- OpenAI. (2025). "How Codex Works: An Architecture for Agentic Coding." [openai.com/blog](https://openai.com/blog)
- Schmid, P. (2025). "The Model-Context-Harness Analogy." [philschmid.de](https://www.philschmid.de/)
- swyx. (2025). "The IMPACT Framework for LLM Harness Engineering." [swyx.io](https://www.swyx.io/)
- Meta/Manus acquisition reporting. (2026). Various sources.

---

*Next: [Chapter 02 -- RAG, Long Context & Knowledge Graphs](/chapters/02-knowledge-layer.md)*
