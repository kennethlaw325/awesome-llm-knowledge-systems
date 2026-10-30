# 第 12 章：本地模型与知识工程

> 部分事实更正已于 2026-10-31 核对；其余沿用较早英文版本。最新英文版：[English](../../../chapters/12-local-models.md)。

> **一句话总结：** 本地模型把推理移到自有硬件，减少供应商数据暴露与逐 token API 费用，但仍有运营成本。
>
> **为什么重要：** 敏感知识与个人微调让推理边界成为架构选择；工具、日志与同步仍须各自设限。

前几章描述的知识工程堆叠基本假设云端 API 存取——把你的 context window 送给 Anthropic、OpenAI 或 Google, 拿回回应。这对大多数用户运作良好。但有越来越多的从业者, 云端推论对他们要么不切实际, 要么不可取: 处理敏感企业数据的、所在司法管辖区有严格数据驻地要求的、以及想透过在自己编纂知识上微调模型来完全闭环的。

本章涵盖本地模型与知识工程的交集。它不涵盖 GPU 采购指南、基准比较、或量化技术——那些主题有其他资源专门处理。相反, 它聚焦于把模型带进你自己基础设施时真正重要的架构决策。

---

## 为什么本地对知识工程重要

三股力量推动本地模型在知识系统中的采用:

**以架构控制隐私。** 云端 RAG 可能把文档片段发送给供应商。完整路径留在本地时，本地推理可移除这项传输；工具调用、遥测、日志与同步仍须审查。具体要求取决于部署场景。

**规模化成本。** vault 检查、笔记编纂与重新索引可产生大量 API 调用。本地执行减少逐 token 账单，但电力、硬件容量与维护仍有成本，应与 API 用量比较。

**微调终局。** 这或许是最有说服力的理由。一旦你的知识库达到足够质量——透过数月 Ingest 操作累积数百份结构良好、互相链接的笔记——它变成原始合成数据集。你能在这个数据集上微调一个小本地模型, 产出一个内在「知道」你领域的模型, 不需在 runtime 检索。知识在权重里, 不在 context window。

---

## 架构：本地模型适合哪里

不是知识 harness 的每个组件都同等受益于本地推论。这里是本地模型提供最大价值的地方:

### Embedding 模型（高价值）

Embedding 是任何 RAG 管线的基础。每次你加笔记到 vault, 它需要被转成向量做相似度搜寻。这是高量、低复杂度的操作——本地推论的完美对象。

热门选择:
- **nomic-embed-text**（137M 参数）: 强健的通用 embedding, 在 CPU 上跑
- **mxbai-embed-large**（335M）: 更高质量, 在普通硬件上仍可管理
- **bge-m3**（568M）: 多语言, 对混合语言内容的 vault 极佳

这些模型够小, 能在任何现代笔电跑而不需 GPU。本地与云端 embedding（OpenAI 的 text-embedding-3、Cohere 的 embed）之间的质量差距已显著缩窄——对大多数知识管理用例, 本地 embedding 够用。

透过 Ollama 在本地跑:
```
ollama pull nomic-embed-text
```

### 查询与推理（中等价值）

用本地模型回答关于你 vault 的问题——Query 操作——是取舍变得更微妙的地方。云端模型（Claude Opus、GPT-4o）在复杂推理、多步综合、微妙指令遵循上仍有意义地更好。但对直接的检索式 Q&A（「我上个月写过关于 X 的什么？」）, 7-14B 参数范围的本地模型表现良好。

实务选项:
- **Qwen3-14B**: 强健多语言效能, Apache 2.0 授权
- **Llama 3.1-8B-Instruct**: 快速推论, 擅长遵循结构化指令
- **DeepSeek-R1-Distill-Qwen-7B**: 从完整 R1 蒸馏的推理能力, MIT 授权
- **Gemma 3-12B**: Google 的高效架构, 擅长结构化输出

最有效的 pattern 是 **分层做法**: 用本地模型处理日常查询与 vault 维护, 升级到云端 API 处理复杂综合与创意任务。这呼应渐进式揭露的 harness engineering 原则如何应用到模型选择——为每个任务用最低能干模型。

### 知识编纂（高价值）

Ingest 操作——读原始来源并把它们编纂成结构化 wiki 页面——出乎意料地适合本地模型。这个任务定义良好: 读文章、提取关键点、生成含 wikilink 的结构化笔记。一个 14B 模型配良好指令遵循能可靠处理这个, 特别在系统 prompt 精确指定输出格式时。

文章可在本地编纂，让知识库持续增长而不产生逐 token API 账单；可用计算容量与运营成本仍是限制。

### Vault 维护（高价值）

Lint 扫描矛盾、陈旧与孤立笔记，可按本地计算预算定期执行。要让整个报告流程保持私密，也需要本地工具与存储。

---

## 微调终局

Andrej Karpathy 概述了一个许多从业者现在在追求的愿景: 一旦你的 LLM 维护 wiki 达到足够质量, 用它微调一个个人小型语言模型（SLM）。

工作流程:

1. **编纂** 你的知识库, 透过数月 Ingest 操作。Wiki 成长到数百份结构良好、互相链接的笔记。
2. **提取** wiki 的训练对: 每份笔记变成一个（问题, 答覆）对, 或一个（context, 续写）对。
3. **微调** 一个小模型（1-3B 参数）在这个数据集上, 用 LoRA 或 QLoRA。
4. **部署** 微调后的模型在本地。它现在从权重回答关于你领域的问题, 不需检索。

这不会完全取代 RAG——微调后的模型对最近信息与具体细节仍受益于检索。但它戏剧性减少检索负担。模型「知道」你领域的基础概念、关系、pattern。RAG 只需补充新或高度特定的信息。

这个管线的工具已成熟:
- **Unsloth** 用于高效微调（快 2 倍, 记忆少 60%）
- **Axolotl** 用于托管训练配置
- **MLX**（Apple Silicon）或 **llama.cpp** 用于微调后模型的本地推论

---

## 整合 Pattern

### Pattern 1: Ollama 作为通用后端

Ollama 提供一个用兼容 OpenAI API 跑本地模型的统一接口。这意味着任何与 OpenAI API 一起运作的工具能透过改 base URL 指向本地模型:

```
base_url: http://localhost:11434/v1
model: qwen3:14b
```

这与 LangChain、LlamaIndex、Dify、大多数 RAG 框架一起运作。对 Obsidian 用户, Smart Connections 等插件能配置成用本地 Ollama 模型而非云端 API。

### Pattern 2: 混合云端-本地

对大多数用户最实用的架构:
- **本地**: Embedding、vault 维护、日常查询、知识编纂
- **云端**: 复杂推理、创意综合、多步 agent 工作流

这给你高量操作的隐私与成本优势, 同时保留对真正需要的任务存取前沿模型能力。

### Pattern 3: MCP 配本地模型

此集成需要 **MCP host/client**：它发现服务器工具，把工具定义与结果交给模型 API，执行获授权的调用及权限检查。Ollama 提供推理，兼容 OpenAI 的端点本身不是 MCP host。只有 host、服务器、模型与存储全在本地，整套 harness 才能留在本地。

---

## 本章不涵盖什么

本章刻意省略:
- **硬件建议**: GPU 选择、VRAM 要求、云端 GPU 租赁在 r/LocalLLaMA 的 wiki 与 Ollama 文档等资源中广泛涵盖。
- **模型基准**: 排名每月变。最新排名见 [Open LLM Leaderboard](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard)。
- **量化细节**: GGUF 格式、INT4 vs INT8、质量/速度取舍在 llama.cpp 与 Ollama 社群中有良好文档。
- **训练基础设施**: 多 GPU 设置、分布式训练、云端训练平台都在知识工程范围之外。

这里的焦点是架构问题: 本地模型在你的知识 harness 中适合哪里, 它们如何改变什么是可能的？

---

## 关键要点

1. **本地 embedding 值得优先评估。** 它减少供应商数据暴露与逐 token 账单，但仍须预算硬件及运营成本。

2. **分层推论是务实选择。** 本地处理日常操作, 云端处理复杂推理。不要强迫 7B 模型做前沿模型做得更好的事。

3. **编纂用例被低估。** 本地 Ingest 把持续工作从供应商账单移到自有计算预算。

4. **微调是终局, 不是起点。** 先建 wiki。编纂数百份质量笔记。然后微调。训练数据的质量——你的 wiki——决定结果模型的质量。

5. **隐私是架构决策。** 敏感知识需要推理、工具、存储与同步边界；本地推理只控制其中一部分。

---

## 来源

- Ollama FAQ: [https://docs.ollama.com/faq](https://docs.ollama.com/faq)
- Meta Llama 3.1-8B-Instruct: [https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct)
- DeepSeek-R1 distilled models: [https://github.com/deepseek-ai/DeepSeek-R1](https://github.com/deepseek-ai/DeepSeek-R1)

- Ollama: [https://ollama.ai](https://ollama.ai)
- llama.cpp: [https://github.com/ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)
- Unsloth: [https://github.com/unslothai/unsloth](https://github.com/unslothai/unsloth)
- Karpathy, Andrej. "LLM Wiki" pattern——本章引用的 raw → wiki → schema 分层架构与 Ingest / Compile / Lint / Query 操作所定义的 Gist。[https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
- Open LLM Leaderboard: [https://huggingface.co/spaces/open-llm-leaderboard](https://huggingface.co/spaces/open-llm-leaderboard)
- Nomic Embed: [https://huggingface.co/nomic-ai/nomic-embed-text-v1.5](https://huggingface.co/nomic-ai/nomic-embed-text-v1.5)
- r/LocalLLaMA: [https://reddit.com/r/LocalLLaMA](https://reddit.com/r/LocalLLaMA)

---

*上一章: [第 11 章 —— LLM 知识工程的关键时刻](11-timeline.md)*

*下一章: [第 13 章 —— Loop Engineering](13-loop-engineering.md)*
