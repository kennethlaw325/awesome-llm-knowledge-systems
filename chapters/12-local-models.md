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

## 2026: Local Models Get an OS-Native API and Vendor QAT

Three 2026 releases changed the local-inference picture this chapter describes.

**Apple opens Foundation Models to any provider (WWDC26, June 8).** Apple's Foundation Models framework --- the same Swift API that powers Apple Intelligence, with streaming, tool calling, and `@Generable` structured output --- shipped a public **`LanguageModel` / `LanguageModelExecutor` protocol**, and Apple ships a reference **`MLXLanguageModel`** backend that loads any mlx-community model from Hugging Face at runtime and caches it on disk. For local knowledge engineering this matters: local open-source models become a *first-class, OS-native backend* rather than a third-party integration. A macOS or iOS knowledge app can now target one Swift API and swap between Apple's on-device model and a downloaded open-weight model without rewriting its inference layer (Anthropic and Google are shipping conforming Swift packages). The Ollama-as-universal-backend pattern above gains an Apple-native sibling.

**Gemma 4 QAT (June 5).** Google published **quantization-aware training checkpoints** for all five Gemma 4 sizes (E2B, E4B, 12B, 26B-A4B, and 31B), simulating 4-bit precision *during* training so the quantized weights recover most of the BF16 quality rather than losing it at post-hoc compression. The release shipped **day-one artifacts across llama.cpp (GGUF), Ollama, LM Studio, and MLX**, with vLLM support day-one for E2B, E4B, 12B, and 31B --- the 26B-A4B MoE was excluded from the vLLM w4a16-ct QAT format because its 704-wide expert dimension loses too much quality at 4-bit. On memory: Google's own blog publishes no percentage figure; a third-party analysis estimates roughly **72% VRAM reduction versus BF16**, while Google's own stated figure is only that E2B drops under 1GB via a mobile format. The beat worth noting is the *release pattern itself*: vendor-native QAT plus simultaneous multi-runtime day-one distribution is becoming the default shape of a serious open-weight launch, which lowers the friction of the "run it locally" decision this chapter argues for.

**Meta ships an open-weight model built for local agents (Muse Glimmer, August 10).** Meta Superintelligence Labs released **Muse Glimmer**, a 30B dense model distilled from the closed Muse Spark, under Apache 2.0 --- positioned explicitly as an open agentic model for on-device use rather than a scaled-down research artifact. At 4-bit quantization it comes in under 20GB, sized deliberately for the 24-32GB memory budget of a single consumer GPU, Mac or PC. Meta's own benchmarks report **DFlash** speculative-decoding speedups of **3.1x on an RTX 5090**, **1.8x on M5-Max**, and **1.5x on M4-Max**, plus benchmark superiority over Gemma4-31B and Qwen3.6-27B --- these are Meta's own figures, not independently reproduced. What distinguishes the release from a typical weights drop is distribution: near-day-zero runtime support across Hugging Face, Ollama, llama.cpp, MLX, ExecuTorch, LM Studio, Unsloth, vLLM, SGLang, Together AI, Fireworks AI, and OpenRouter. Every open-weight model this book has covered so far in the local-deployment context has been server-class only (Chapter 9's Kimi K3, explicitly excluded from the local story at 2.8T parameters); Muse Glimmer is the first US-frontier-lab model designed and benchmarked, from the outset, for single-consumer-GPU local agent use, shipped with the same vendor-native-QAT-plus-multi-runtime-day-one pattern the Gemma 4 QAT release modeled above. The pattern this chapter flagged as Google's is no longer Google-specific. (Meta separately said a later release of Muse Spark 1.2 weights is coming; that is a distinct, undated event and is not covered here.)

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
- Apple. "Bring an LLM provider to the Foundation Models framework," WWDC26 Session 339 (June 8, 2026). [https://developer.apple.com/videos/play/wwdc2026/339/](https://developer.apple.com/videos/play/wwdc2026/339/) and Session 241 [https://developer.apple.com/videos/play/wwdc2026/241/](https://developer.apple.com/videos/play/wwdc2026/241/) --- public `LanguageModel` / `LanguageModelExecutor` Swift protocol; reference `MLXLanguageModel` backend for Hugging Face mlx-community models.
- Google. "Quantization-Aware Training for Gemma 4" (June 5, 2026). [https://blog.google/innovation-and-ai/technology/developers-tools/quantization-aware-training-gemma-4/](https://blog.google/innovation-and-ai/technology/developers-tools/quantization-aware-training-gemma-4/) --- QAT checkpoints for all five sizes; day-one llama.cpp / Ollama / LM Studio / MLX; vLLM day-one except the 26B-A4B MoE. Third-party VRAM analysis (~72% vs BF16; Google's own figure only that E2B drops under 1GB via a mobile format): [https://runaihome.com/blog/gemma-4-qat-local-ai-hardware-update-2026/](https://runaihome.com/blog/gemma-4-qat-local-ai-hardware-update-2026/).
- Meta Superintelligence Labs. "Introducing Muse Glimmer: an open agentic model" (August 10, 2026). [https://research.meta.ai/blog/introducing-muse-glimmer-open-agentic-model](https://research.meta.ai/blog/introducing-muse-glimmer-open-agentic-model) --- 30B dense, Apache 2.0, distilled from Muse Spark; DFlash speedup and benchmark figures are Meta's own. Secondary: Phoronix [https://phoronix.com/news/Meta-Muse-Glimmer](https://phoronix.com/news/Meta-Muse-Glimmer) ; CNBC [https://www.cnbc.com/2026/08/10/meta-muse-glimmer-open-weight-ai.html](https://www.cnbc.com/2026/08/10/meta-muse-glimmer-open-weight-ai.html) ; Ghacks (August 11, 2026) [https://www.ghacks.net/2026/08/11/meta-releases-muse-glimmer-a-30-billion-parameter-open-weight-ai-model-that-runs-on-a-single-consumer-gpu/](https://www.ghacks.net/2026/08/11/meta-releases-muse-glimmer-a-30-billion-parameter-open-weight-ai-model-that-runs-on-a-single-consumer-gpu/).

---

*Previous: [Chapter 11 - Key Moments in LLM Knowledge Engineering](11-timeline.md)*

*Next: [Chapter 13 - Loop Engineering](13-loop-engineering.md)*
