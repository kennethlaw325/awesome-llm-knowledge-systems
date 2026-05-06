# Chapter 12: Local Models for Knowledge Engineering

> **In one sentence:** Local models let you run your entire knowledge harness on your own hardware -- private, free, and increasingly competitive with cloud APIs.
>
> **Why it matters:** If your knowledge base contains sensitive data, or if you want to fine-tune a model on your own notes, local inference is the only path that keeps everything under your control.

The previous chapters describe a knowledge engineering stack that largely assumes cloud API access -- sending your context window to Anthropic, OpenAI, or Google and getting a response back. This works well for most users. But there is a growing segment of practitioners for whom cloud inference is either impractical or undesirable: those working with sensitive corporate data, those in jurisdictions with strict data residency requirements, and those who want to close the loop entirely by fine-tuning models on their own compiled knowledge.

This chapter covers the intersection of local models and knowledge engineering. It does not cover GPU purchasing guides, benchmark comparisons, or quantization techniques -- those topics are well-served by other resources. Instead, it focuses on the architectural decisions that matter when you bring the model inside your own infrastructure.

---

## Why Local Matters for Knowledge Engineering

Three forces are driving the adoption of local models in knowledge systems:

**Privacy as architecture, not policy.** When you run RAG over internal company documents, every query sends document chunks to a cloud provider. Data processing agreements help, but they do not eliminate the surface area. With local inference, the data never leaves the machine. For legal firms, healthcare organizations, and government agencies, this is not a preference -- it is a requirement.

**Cost at scale.** A knowledge system that runs continuous background processes -- vault linting, automatic note compilation, periodic re-indexing -- generates thousands of API calls per day. At cloud pricing, this adds up quickly. A local model running on consumer hardware has zero marginal cost per query after the initial setup. For always-on knowledge maintenance (the Lint operation from Karpathy's architecture), local inference changes the economics entirely.

**The fine-tuning endgame.** This is perhaps the most compelling reason. Once your knowledge base reaches sufficient quality -- hundreds of well-structured, cross-linked notes compiled through the Ingest operation -- it becomes a pristine synthetic dataset. You can fine-tune a small local model on this dataset, producing a model that inherently "knows" your domain without needing retrieval at runtime. The knowledge is in the weights, not the context window.

---

## Architecture: Where Local Models Fit

Not every component of a knowledge harness benefits equally from local inference. Here is where local models provide the most value:

### Embedding Models (High Value)

Embedding is the foundation of any RAG pipeline. Every time you add a note to your vault, it needs to be converted to a vector for similarity search. This is a high-volume, low-complexity operation -- perfect for local inference.

Popular choices:
- **nomic-embed-text** (137M parameters): Strong general-purpose embeddings, runs on CPU
- **mxbai-embed-large** (335M): Higher quality, still manageable on modest hardware
- **bge-m3** (568M): Multilingual, excellent for vaults with mixed-language content

These models are small enough to run on any modern laptop without a GPU. The quality difference between local and cloud embeddings (OpenAI's text-embedding-3, Cohere's embed) has narrowed significantly -- for most knowledge management use cases, local embeddings are sufficient.

Running locally via Ollama:
```
ollama pull nomic-embed-text
```

### Query and Reasoning (Medium Value)

Using a local model to answer questions about your vault -- the Query operation -- is where the trade-offs become more nuanced. Cloud models (Claude Opus, GPT-4o) are still meaningfully better at complex reasoning, multi-step synthesis, and nuanced instruction-following. But for straightforward retrieval-based Q&A ("what did I write about X last month?"), local models in the 7-14B parameter range perform well.

Practical options:
- **Qwen3-14B**: Strong multilingual performance, Apache 2.0 license
- **Llama 3.3-8B**: Fast inference, good at following structured instructions
- **DeepSeek-R1-Distill-7B**: Reasoning capabilities distilled from the full R1, MIT license
- **Gemma 3-12B**: Google's efficient architecture, good at structured output

The pattern that works best is a **tiered approach**: use a local model for routine queries and vault maintenance, escalate to a cloud API for complex synthesis and creative tasks. This mirrors how the harness engineering principle of progressive disclosure applies to model selection -- use the minimum capable model for each task.

### Knowledge Compilation (High Value)

The Ingest operation -- reading raw sources and compiling them into structured wiki pages -- is surprisingly well-suited to local models. The task is well-defined: read an article, extract key points, generate a structured note with wikilinks. A 14B model with good instruction-following can handle this reliably, especially when the output format is specified precisely in the system prompt.

This is where the economics argument is strongest. If your Web Clipper captures 5-10 articles per day, and each compilation takes 2-3 minutes of inference, running this locally means your knowledge base grows continuously at zero marginal cost.

### Vault Maintenance (High Value)

The Lint operation -- scanning for contradictions, staleness, and orphaned notes -- is a batch process that benefits enormously from local inference. You can run it hourly, daily, or continuously in the background without worrying about API costs. A local model scans your vault, flags issues, and generates a health report -- all without any data leaving your machine.

---

## The Fine-Tuning Endgame

Andrej Karpathy outlined a vision that many practitioners are now pursuing: once your LLM-maintained wiki reaches sufficient quality, use it to fine-tune a personal Small Language Model (SLM).

The workflow:

1. **Compile** your knowledge base through months of Ingest operations. The wiki grows to hundreds of well-structured, interlinked notes.
2. **Extract** training pairs from the wiki: each note becomes a (question, answer) pair, or a (context, completion) pair.
3. **Fine-tune** a small model (1-3B parameters) on this dataset using LoRA or QLoRA.
4. **Deploy** the fine-tuned model locally. It now answers questions about your domain from its weights, without needing retrieval.

This does not replace RAG entirely -- the fine-tuned model still benefits from retrieval for recent information and specific details. But it dramatically reduces the retrieval burden. The model "knows" the foundational concepts, relationships, and patterns in your domain. RAG only needs to supplement with new or highly specific information.

The tools for this pipeline are mature:
- **Unsloth** for efficient fine-tuning (2x faster, 60% less memory)
- **Axolotl** for managed training configurations
- **MLX** (Apple Silicon) or **llama.cpp** for local inference of the fine-tuned model

---

## Integration Patterns

### Pattern 1: Ollama as Universal Backend

Ollama provides a unified interface for running local models with an OpenAI-compatible API. This means any tool that works with the OpenAI API can be pointed at a local model by changing the base URL:

```
base_url: http://localhost:11434/v1
model: qwen3:14b
```

This works with LangChain, LlamaIndex, Dify, and most RAG frameworks. For Obsidian users, plugins like Smart Connections can be configured to use a local Ollama model instead of cloud APIs.

### Pattern 2: Hybrid Cloud-Local

The most practical architecture for most users:
- **Local**: Embeddings, vault maintenance, routine queries, knowledge compilation
- **Cloud**: Complex reasoning, creative synthesis, multi-step agent workflows

This gives you the privacy and cost benefits of local inference for high-volume operations, while retaining access to frontier model capabilities for tasks that genuinely require them.

### Pattern 3: MCP with Local Models

The Model Context Protocol works with local models through Ollama's OpenAI-compatible endpoint. This means you can build MCP servers that connect to local knowledge sources -- your vault, your databases, your file system -- and serve them to a locally-running model. The entire knowledge harness runs on your machine.

---

## What This Chapter Does Not Cover

This chapter intentionally omits:
- **Hardware recommendations**: GPU selection, VRAM requirements, and cloud GPU rental are covered extensively in resources like r/LocalLLaMA's wiki and the Ollama documentation.
- **Model benchmarks**: Rankings change monthly. Check the [Open LLM Leaderboard](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard) for current standings.
- **Quantization details**: GGUF formats, INT4 vs INT8, and quality/speed trade-offs are well-documented in the llama.cpp and Ollama communities.
- **Training infrastructure**: Multi-GPU setups, distributed training, and cloud training platforms are outside the scope of knowledge engineering.

The focus here is on the architectural question: where do local models fit in your knowledge harness, and how do they change what is possible?

---

## Key Takeaways

1. **Local embedding is a no-brainer.** The quality gap has closed, the cost is zero, and the privacy benefit is absolute. If you run RAG, run your embeddings locally.

2. **Tiered inference is the pragmatic choice.** Local for routine operations, cloud for complex reasoning. Do not force a 7B model to do what a frontier model does better.

3. **The compilation use case is underappreciated.** Running Ingest locally means your knowledge base can grow continuously at zero cost. This changes the economics of knowledge maintenance.

4. **Fine-tuning is the endgame, not the starting point.** Build the wiki first. Compile hundreds of quality notes. Then fine-tune. The quality of the training data -- your wiki -- determines the quality of the resulting model.

5. **Privacy is an architecture decision.** If your knowledge contains sensitive information, local inference is not optional. Design for it from the start.

---

## Sources

- Ollama: [https://ollama.ai](https://ollama.ai)
- llama.cpp: [https://github.com/ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)
- Unsloth: [https://github.com/unslothai/unsloth](https://github.com/unslothai/unsloth)
- Karpathy, Andrej. "LLM Wiki" pattern --- Gist defining the raw → wiki → schema layered architecture and the Ingest / Compile / Lint / Query operations referenced throughout this chapter. [https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
- Open LLM Leaderboard: [https://huggingface.co/spaces/open-llm-leaderboard](https://huggingface.co/spaces/open-llm-leaderboard)
- Nomic Embed: [https://huggingface.co/nomic-ai/nomic-embed-text-v1.5](https://huggingface.co/nomic-ai/nomic-embed-text-v1.5)
- r/LocalLLaMA: [https://reddit.com/r/LocalLLaMA](https://reddit.com/r/LocalLLaMA)

---

*Previous: [Chapter 11 - Key Moments in LLM Knowledge Engineering](11-timeline.md)*
