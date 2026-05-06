# Chapter 02: RAG, Long Context & Knowledge Graphs

> **In one sentence:** There are three main ways to give AI access to knowledge: searching a database (RAG), feeding it long documents, or connecting facts in a graph.
>
> **Why it matters:** If you use AI for anything involving your own data, this chapter explains which approach works best for your situation.

**The knowledge retrieval layer -- what works, what doesn't, and why the answer is almost always "hybrid."**

---

## RAG Is Not Dead

Every six months, someone publishes "RAG Is Dead, Long Context Is All You Need." Every six months, enterprises prove them wrong.

**Gartner's Q4 2025 enterprise survey** found that 71% of organizations that attempted to replace RAG pipelines with pure context-stuffing (feeding entire document corpora into large context windows) added RAG back within 12 months. The reasons were consistent: cost, latency, accuracy degradation at scale, and the inability to handle dynamic or frequently updated knowledge bases.

RAG is not dead. It is evolving. The question was never "RAG or not RAG" -- it was "what kind of RAG, combined with what else."

---

## The Cost Reality

The economic argument for RAG remains overwhelming.

A typical RAG pipeline retrieves 5-20 relevant chunks (roughly 2,000-8,000 tokens) and feeds them into a model call. A context-stuffing approach for the same query might require loading 500K-1M tokens of source documents.

**Per-query cost comparison (approximate, mid-2026 pricing):**

| Approach | Input Tokens | Approximate Cost | Relative Cost |
|----------|-------------|-----------------|---------------|
| RAG (targeted retrieval) | ~5,000 | ~$0.00008 | 1x |
| Context-stuffing (full corpus) | ~500,000 | ~$0.10 | 1,250x |

This is not a rounding error. At enterprise scale -- millions of queries per month -- the difference between $80 and $100,000 in monthly inference costs determines whether a project survives budget review.

The cost gap narrows as model pricing drops, but retrieval will always be cheaper than brute-forcing the entire knowledge base into every call. The laws of information theory guarantee this: selecting relevant information is cheaper than processing all information.

---

## Long Context: When It Works, When It Doesn't

Long context windows (128K, 200K, 1M+ tokens) are genuinely transformative for specific use cases:

**Where long context excels:**
- **Static, bounded document analysis**: Analyzing a single contract, codebase file, or research paper where the entire relevant corpus fits in the window
- **Cross-reference tasks**: Finding connections across a fixed set of documents loaded once
- **Summarization**: Condensing large but finite inputs into structured outputs

**Where long context breaks down:**

**"Lost in the middle" degradation.** Research from [Liu et al. (2023)](https://arxiv.org/abs/2307.03172) demonstrated that LLMs perform significantly worse on information placed in the middle of long contexts compared to information at the beginning or end. Subsequent model improvements have reduced but not eliminated this effect. As of early 2026, models still show measurable accuracy degradation when relevant information is buried among 500K+ tokens of context.

**Dynamic knowledge bases.** If your knowledge base updates hourly (product inventory, support tickets, news feeds), you cannot re-embed the entire corpus into every context window. RAG's retrieval step naturally handles updates -- new documents are indexed and immediately retrievable without changing the prompt structure.

**Multi-tenant isolation.** Long context approaches struggle with access control. When documents from multiple users or permission levels exist in the same corpus, RAG pipelines can enforce retrieval-time filtering. Context-stuffing requires careful (and error-prone) document segregation.

**Latency at scale.** Processing 1M tokens takes meaningfully longer than processing 5K tokens, even with optimized inference. For user-facing applications where sub-second response times matter, targeted retrieval wins.

### 2026 Update: Titans + MIRAS Reframes the Long-Context Tradeoff

Every limitation above assumes a Transformer-style context window: a flat span of tokens read by attention, with the same per-token cost regardless of position, and the same "lost in the middle" failure modes. **Titans + MIRAS**, the April 2026 architecture family from Google Research, breaks that assumption. In Titans, memory is not the attention window --- it is a **trainable neural module** that updates its own weights by gradient descent during inference, so the model literally compresses long history into weight updates rather than carrying it forward as tokens. MIRAS provides the training recipes that keep this learn-while-you-infer process stable. At comparable parameter counts, Google reports Titans outperforming Mamba-2, Gated DeltaNet, and Transformer++ on long-range recall and multi-hop reasoning. None of this refutes the original long-context limitations --- those still hold for the attention-window paradigm that GPT-4 Turbo, Gemini 1.5, and Claude continue to use --- but it does establish that **the "attention budget is scarce" framing is now a property of one architecture family, not a universal constraint.** For practitioners, this means the long-context tradeoff is no longer a single curve. There are now at least two: the attention-window curve (where lost-in-the-middle and per-token cost dominate) and the trainable-memory curve (where the cost shifts toward inference-time weight updates and the failure modes shift toward stability and forgetting). RAG remains a strong default for both, but the *reasons* RAG wins are different in each regime.

---

## GraphRAG: When Flat Retrieval Is Not Enough

Standard RAG treats documents as independent chunks. This works for factual lookup ("What is the return policy?") but fails for questions requiring *relationship reasoning* ("Which suppliers are connected to both our delayed shipments and our quality complaints?").

[Microsoft's GraphRAG](https://github.com/microsoft/graphrag) (2024-2025) introduced a hybrid approach: build a knowledge graph from source documents, then use graph traversal alongside vector retrieval to answer queries.

### How GraphRAG Works

1. **Indexing phase**: Documents are processed to extract entities (people, organizations, concepts) and relationships between them. These form a graph structure alongside traditional vector embeddings.
2. **Community detection**: The graph is partitioned into communities of densely connected entities. Each community gets a summary description.
3. **Query phase**: For a given query, both vector similarity *and* graph traversal are used to retrieve relevant context. Entity relationships provide multi-hop reasoning paths that flat retrieval misses.

### When GraphRAG matters

- **Multi-hop queries**: "Who are the common investors between companies that went public in 2025 and companies that were acquired?" -- requires traversing relationship chains
- **Entity-centric reasoning**: Questions about specific entities and their connections to other entities
- **Global summarization**: "What are the main themes across all our customer feedback?" -- community summaries provide this without processing every document

### When GraphRAG is overkill

- Simple factual lookup (standard RAG handles this fine)
- Small corpora where long context can hold everything
- Use cases where entity extraction quality is low (garbage in, garbage out)

The indexing cost of GraphRAG is significantly higher than standard RAG. Build the graph only when relationship reasoning is a core requirement, not as a default.

### 2026 Evolution: KG as Semantic Backbone for Long Context

Through 2024 and most of 2025, GraphRAG was framed as an **alternative to RAG** --- a different way to retrieve chunks for a model with a limited context window. By 2026, that framing has shifted. As frontier models push context windows into the multi-million-token range (Gemini 1.5 at 1M, Kimi past 2M Chinese characters, with further expansion underway), the question is no longer "how do we retrieve a small number of relevant chunks" but "how do we navigate a context that is already large enough to hold most of what we need."

In that world, the knowledge graph stops being a **retrieval substitute** and becomes a **structured index layer for long context**. The graph is not there to decide which chunks to load --- the chunks are already in the window. The graph is there to give the model a semantic map of what is in the window: which entities are present, how they are related, which sections correspond to which topics, where contradictions live, and which multi-hop paths connect the question to the relevant evidence. GraphRAG re-emerges as a **semantic backbone** that lets an agent walk a million-token window efficiently, rather than as a workaround for the 8K-token windows it was born in. The April 2026 arrival of trainable memory modules (Titans + MIRAS) does not displace this role --- the early evidence is that knowledge graphs and trainable memory will **coexist and likely compose** in production stacks, with the graph providing typed, queryable structure over what the trainable module has already compressed into weights.

---

## The 2025-2026 RAG Technique Landscape

RAG itself has branched into multiple specialized approaches. The key variants:

### Self-RAG (Asai et al., 2023)

[Self-RAG](https://arxiv.org/abs/2310.11511) trains the model to decide *when* retrieval is needed, *what* to retrieve, and *whether* the retrieved content is actually relevant. Instead of always retrieving, the model generates special "reflection tokens" that gate the retrieval process.

**Key benefit**: Reduces unnecessary retrieval calls and filters out irrelevant retrieved content, improving both efficiency and accuracy.

### Corrective RAG (CRAG)

[Corrective RAG](https://arxiv.org/abs/2401.15884) (Yan et al., 2024) adds a verification step after retrieval. A lightweight evaluator assesses whether retrieved documents are relevant to the query. If confidence is low, the system triggers a web search or alternative retrieval strategy as a fallback.

**Key benefit**: Graceful degradation when the primary knowledge base does not contain the answer.

### Adaptive RAG

[Adaptive RAG](https://arxiv.org/abs/2403.14403) (Jeong et al., 2024) uses a classifier to route queries to different retrieval strategies based on complexity. Simple queries get direct retrieval. Complex queries get multi-step retrieval with chain-of-thought reasoning. Ambiguous queries get multiple retrieval passes with result fusion.

**Key benefit**: Matches retrieval cost to query complexity instead of using a one-size-fits-all pipeline.

### Golden-Retriever RAG

Golden-Retriever RAG focuses on retrieval quality by using the LLM itself to rewrite queries before retrieval. The model generates an "ideal document" description, which is then used as the retrieval query instead of the raw user input.

**Key benefit**: Bridges the vocabulary gap between how users ask questions and how documents are written.

---

## RAG as "Context Engine"

[RAGFlow](https://github.com/infiniflow/ragflow), the open-source RAG engine, published a year-end review in late 2025 arguing that the term "Retrieval-Augmented Generation" no longer captures what modern RAG systems do. Their proposed reframe: RAG has evolved from a retrieval technique into a **Context Engine** -- a general-purpose system for assembling relevant information from heterogeneous sources into a model's context window.

This reframe aligns with the context engineering evolution described in [Chapter 01](/chapters/01-evolution.md). RAG is not just "retrieve and stuff." A modern RAG system:

- Classifies query intent and complexity
- Routes to appropriate retrieval strategies (vector, keyword, graph, hybrid)
- Reranks and filters results
- Compresses retrieved content to fit token budgets
- Formats results with appropriate structure and metadata
- Tracks provenance for citation and verification

This is a context assembly pipeline, not a retrieval step. The RAG system *is* the context engine.

---

## Hybrid Architectures: The Convergence

The evidence from 2025-2026 points clearly toward hybrid approaches. No single technique wins across all dimensions:

| Dimension | RAG | Long Context | Knowledge Graph |
|-----------|-----|-------------|----------------|
| Cost per query | Low | High | Medium |
| Dynamic updates | Strong | Weak | Medium |
| Relationship reasoning | Weak | Weak | Strong |
| Setup complexity | Medium | Low | High |
| Accuracy (targeted) | High | Medium | High |
| Accuracy (global) | Medium | High | High |

**The winning pattern in production:**

1. **Knowledge graph** for entity relationships and global understanding
2. **RAG** for dynamic, targeted retrieval on specific queries
3. **Long context** for bounded analysis tasks where the full document matters
4. **Query router** that selects the right strategy per query

This is not theoretical. Production systems at scale (enterprise search, coding assistants, customer support agents) use all three in combination. The engineering challenge is not choosing one -- it is building the router that picks the right tool for each query.

---

## Key Projects and Resources

| Project | Description | Link |
|---------|-------------|------|
| Microsoft GraphRAG | Knowledge graph + RAG hybrid | [github.com/microsoft/graphrag](https://github.com/microsoft/graphrag) |
| RAGFlow | Open-source RAG engine with deep document understanding | [github.com/infiniflow/ragflow](https://github.com/infiniflow/ragflow) |
| NirDiamant/RAG_Techniques | Comprehensive collection of RAG implementations | [github.com/NirDiamant/RAG_Techniques](https://github.com/NirDiamant/RAG_Techniques) |
| LangChain | Framework with extensive RAG tooling | [github.com/langchain-ai/langchain](https://github.com/langchain-ai/langchain) |
| LlamaIndex | Data framework for LLM applications | [github.com/run-llama/llama_index](https://github.com/run-llama/llama_index) |
| Chroma | Open-source embedding database | [github.com/chroma-core/chroma](https://github.com/chroma-core/chroma) |

---

## Sources

- Gartner. "Enterprise RAG Adoption" survey commentary, Q4 2025 --- the 71%-revert figure cited at the top of this chapter circulates across multiple industry analyses; primary access requires a Gartner subscription, so the figure is reported here as widely-cited industry stat rather than from a freely-reachable primary URL.
- Liu, N. F. et al. (2023). "Lost in the Middle: How Language Models Use Long Contexts." [arXiv:2307.03172](https://arxiv.org/abs/2307.03172)
- Microsoft. (2024). "GraphRAG: Unlocking LLM discovery on narrative private datasets." [microsoft.com/research](https://www.microsoft.com/en-us/research/blog/graphrag-unlocking-llm-discovery-on-narrative-private-datasets/)
- Asai, A. et al. (2023). "Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection." [arXiv:2310.11511](https://arxiv.org/abs/2310.11511)
- Yan, S. et al. (2024). "Corrective Retrieval Augmented Generation." [arXiv:2401.15884](https://arxiv.org/abs/2401.15884)
- Jeong, S. et al. (2024). "Adaptive-RAG: Learning to Adapt Retrieval-Augmented Large Language Models through Question Complexity." [arXiv:2403.14403](https://arxiv.org/abs/2403.14403)
- RAGFlow. (2025). "Year-End Review: From RAG to Context Engine." [github.com/infiniflow/ragflow](https://github.com/infiniflow/ragflow)
- NirDiamant. (2025). "RAG Techniques." [github.com/NirDiamant/RAG_Techniques](https://github.com/NirDiamant/RAG_Techniques)
- Google Research. (April 2026). "Titans + MIRAS: Helping AI Have Long-Term Memory." [research.google/blog/titans-miras-helping-ai-have-long-term-memory/](https://research.google/blog/titans-miras-helping-ai-have-long-term-memory/) --- trainable memory modules outperforming Mamba-2 / Gated DeltaNet / Transformer++ at comparable sizes.

---

*Previous: [Chapter 01 -- The Three Generations](/chapters/01-evolution.md)*

*Next: Chapter 03 -- Context Engineering Deep Dive (coming soon)*
