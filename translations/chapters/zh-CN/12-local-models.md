# 第 12 章：本地模型与知识工程

> **一句话总结：** 本地模型让你在自己的硬件上跑整套知识 harness——私密、免费, 而且越来越能与云端 API 竞争。
>
> **为什么重要：** 如果你的知识库含敏感数据, 或你想在自己的笔记上微调模型, 本地推论是唯一让一切留在你掌握下的路径。

前几章描述的知识工程堆叠基本假设云端 API 存取——把你的 context window 送给 Anthropic、OpenAI 或 Google, 拿回回应。这对大多数用户运作良好。但有越来越多的从业者, 云端推论对他们要么不切实际, 要么不可取: 处理敏感企业数据的、所在司法管辖区有严格数据驻地要求的、以及想透过在自己编纂知识上微调模型来完全闭环的。

本章涵盖本地模型与知识工程的交集。它不涵盖 GPU 采购指南、基准比较、或量化技术——那些主题有其他资源专门处理。相反, 它聚焦于把模型带进你自己基础设施时真正重要的架构决策。

---

## 为什么本地对知识工程重要

三股力量推动本地模型在知识系统中的采用:

**隐私作为架构, 不只政策。** 当你对内部公司文件跑 RAG, 每次查询都送文件 chunk 给云端供应商。数据处理协议有帮助, 但不消除攻击面。本地推论下, 数据从不离开机器。对法律事务所、医疗组织、政府机构, 这不是偏好——是要求。

**规模化成本。** 一个跑持续背景程序——vault 检查、自动笔记编纂、定期重新索引——的知识系统每天产生数千次 API 调用。在云端定价下, 这快速累积。一个跑在消费级硬件的本地模型, 在初始设置后, 每查询零边际成本。对永远开着的知识维护（来自 Karpathy 架构的 Lint 操作）, 本地推论彻底改变经济学。

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
- **Llama 3.3-8B**: 快速推论, 擅长遵循结构化指令
- **DeepSeek-R1-Distill-7B**: 从完整 R1 蒸馏的推理能力, MIT 授权
- **Gemma 3-12B**: Google 的高效架构, 擅长结构化输出

最有效的 pattern 是 **分层做法**: 用本地模型处理日常查询与 vault 维护, 升级到云端 API 处理复杂综合与创意任务。这呼应渐进式揭露的 harness engineering 原则如何应用到模型选择——为每个任务用最低能干模型。

### 知识编纂（高价值）

Ingest 操作——读原始来源并把它们编纂成结构化 wiki 页面——出乎意料地适合本地模型。这个任务定义良好: 读文章、提取关键点、生成含 wikilink 的结构化笔记。一个 14B 模型配良好指令遵循能可靠处理这个, 特别在系统 prompt 精确指定输出格式时。

这是经济论点最强的地方。如果你的 Web Clipper 每天捕捉 5-10 篇文章, 每次编纂花 2-3 分钟推论, 在本地跑这件事意味着你的知识库以零边际成本持续成长。

### Vault 维护（高价值）

Lint 操作——扫描矛盾、陈旧、孤立笔记——是个批次过程, 极受益于本地推论。你能每小时、每天、或在背景持续跑它而不用担心 API 成本。一个本地模型扫描你的 vault, 标记问题, 产出健康报告——全部不需任何数据离开你的机器。

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

Model Context Protocol 透过 Ollama 的兼容 OpenAI 端点与本地模型一起运作。这意味着你能建 MCP 服务器, 连到本地知识来源——你的 vault、你的数据库、你的文件系统——并把它们服务给本地跑的模型。整套知识 harness 跑在你的机器上。

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

1. **本地 embedding 是不用想的选择。** 质量差距已关闭, 成本是零, 隐私好处是绝对的。如果你跑 RAG, 在本地跑 embedding。

2. **分层推论是务实选择。** 本地处理日常操作, 云端处理复杂推理。不要强迫 7B 模型做前沿模型做得更好的事。

3. **编纂用例被低估。** 在本地跑 Ingest 意味着你的知识库能以零成本持续成长。这改变知识维护的经济学。

4. **微调是终局, 不是起点。** 先建 wiki。编纂数百份质量笔记。然后微调。训练数据的质量——你的 wiki——决定结果模型的质量。

5. **隐私是架构决策。** 如果你的知识含敏感信息, 本地推论不是可选的。从一开始就为它设计。

---

## 来源

- Ollama: [https://ollama.ai](https://ollama.ai)
- llama.cpp: [https://github.com/ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)
- Unsloth: [https://github.com/unslothai/unsloth](https://github.com/unslothai/unsloth)
- Karpathy, Andrej. "LLM Wiki" pattern——本章引用的 raw → wiki → schema 分层架构与 Ingest / Compile / Lint / Query 操作所定义的 Gist。[https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
- Open LLM Leaderboard: [https://huggingface.co/spaces/open-llm-leaderboard](https://huggingface.co/spaces/open-llm-leaderboard)
- Nomic Embed: [https://huggingface.co/nomic-ai/nomic-embed-text-v1.5](https://huggingface.co/nomic-ai/nomic-embed-text-v1.5)
- r/LocalLLaMA: [https://reddit.com/r/LocalLLaMA](https://reddit.com/r/LocalLLaMA)

---

*上一章: [第 11 章 —— LLM 知识工程的关键时刻](11-timeline.md)*
