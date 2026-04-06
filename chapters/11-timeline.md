# Chapter 11: Key Moments in LLM Knowledge Engineering

> **In one sentence:** A chronological record of the key moments that shaped LLM knowledge engineering from 2022 to 2026.
>
> **Why it matters:** Context for everything in this guide -- when it happened, who did it, and what changed.

![LLM Knowledge Engineering Timeline 2022-2026](../diagrams/timeline.png)

A chronological map of the events, releases, and ideas that shaped how we build knowledge systems with large language models. Where precise dates are known, they are included. Where only a quarter or month is confirmed, that granularity is used.

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

### November --- Anthropic Releases the Model Context Protocol (MCP)

Anthropic publishes MCP as an open specification for connecting LLMs to external tools and data sources. MCP standardizes how models discover, authenticate with, and invoke tools --- replacing the fragmented landscape of custom function-calling implementations. It is designed as a protocol, not a product: any model provider or tool developer can implement it. The analogy to USB or HTTP is deliberate. This moment marks the beginning of interoperable knowledge infrastructure.

---

## 2025

### January --- DeepSeek R1 and the Open-Source Inflection

DeepSeek releases R1, an open-weight reasoning model that matches OpenAI's o1 on key benchmarks. Trained for under $6 million and released under the MIT license, it demonstrates that frontier reasoning capabilities are no longer exclusive to well-funded labs. Enterprise open-source model adoption in China surges from 23% to 67%. The knowledge engineering implication: the foundation model is no longer the bottleneck or the moat.

### March --- Kimi Achieves 2M Chinese Character Context

Moonshot AI's Kimi reaches a 2-million Chinese character context window, the longest for any model optimized for Chinese text. This enables full-document processing for Chinese enterprise use cases --- legal contracts, regulatory filings, technical manuals --- that were previously impractical.

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

### April --- This Guide Published

This research report is published, attempting to synthesize the preceding four years of rapid development into a coherent framework for practitioners. The field continues to evolve faster than any single document can capture.

---

## The Pattern

Reading this timeline vertically, a pattern emerges:

**2022-2023**: The model is the product. Prompt engineering is the skill. RAG is the architecture.

**2024**: Context windows expand. Protocols standardize. The conversation shifts from "what can the model do" to "what can we build around the model."

**2025**: Context engineering replaces prompt engineering. Skills, agents, and harnesses become the primary engineering surface. Open-source models commoditize the foundation layer. MCP becomes infrastructure.

**2026**: The harness is the product. Skill management at scale is the new challenge. The 6x performance gap between naive and engineered harnesses makes the case: how you orchestrate the model matters more than which model you choose.

The trajectory is clear. The next chapter of this story will not be about larger models. It will be about better systems.

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
- Moonshot AI, Kimi Long-Context Technical Blog (March 2025)
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

---

*Previous: [Chapter 10 - Building a Real-World Knowledge Harness](10-case-study.md)*
