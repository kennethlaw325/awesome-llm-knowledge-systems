# 第 2 章：RAG、长上下文与知识图谱

> **一句话总结：** 给 AI 取得知识有三种主要方法: 搜数据库（RAG）、喂长文件、或在图里连结事实。
>
> **为什么重要：** 如果你用 AI 处理任何关于自己数据的事情, 这章解释哪种做法最适合你的情境。

**知识检索层——什么有效、什么无效, 为什么答案几乎永远是「混合」。**

---

## RAG 没死

每六个月就有人发表「RAG 死了, 长上下文就够了」。每六个月企业证明他们错了。

**Gartner 2025 Q4 企业调查** 发现, 71% 试着用纯 context-stuffing（把整个文件库喂进大上下文窗口）取代 RAG 管线的组织, 在 12 个月内把 RAG 加回去。理由都一样: 成本、延迟、规模化时的准确度退化、以及无法处理动态或频繁更新的知识库。

RAG 没死, 它在演化。问题从来不是「RAG 还是不 RAG」——而是「哪种 RAG, 配合什么其他东西」。

---

## 成本现实

RAG 的经济论点仍然压倒性。

一个典型 RAG 管线检索 5-20 个相关 chunk（约 2,000-8,000 token）, 把它们喂入模型调用。同样查询的 context-stuffing 做法可能需要加载 500K-1M token 的来源文件。

**每查询成本对比（约略, 2026 年中价格）:**

| 做法 | 输入 token | 约略成本 | 相对成本 |
|------|-----------|---------|---------|
| RAG（针对性检索） | ~5,000 | ~$0.00008 | 1x |
| Context-stuffing（全库） | ~500,000 | ~$0.10 | 1,250x |

这不是四舍五入的误差。在企业规模——每月数百万查询——每月推论成本 $80 与 $100,000 的差异决定项目是否能撑过预算审查。

随模型价格下降, 差距会缩, 但检索永远比把整个知识库硬塞进每次调用便宜。信息论的定律保证: 选择相关信息比处理全部信息便宜。

---

## 长上下文：何时有效, 何时无效

长上下文窗口（128K、200K、1M+ token）对特定用例是真正变革性的:

**长上下文擅长的地方:**
- **静态、有边界的文件分析**: 分析单一合同、codebase 档、研究论文, 整个相关语料能放进窗口
- **交叉参照任务**: 在一组固定、一次加载的文件中找连结
- **总结**: 把大量但有限的输入浓缩成结构化输出

**长上下文崩溃的地方:**

**「迷失在中间」退化。** [Liu et al.（2023）](https://arxiv.org/abs/2307.03172) 的研究显示, LLM 对放在长 context 中间的信息表现, 显著差于放在头或尾的。后续模型改进减少但没消除这个效应。截至 2026 年初, 当相关信息埋在 500K+ token 的 context 中时, 模型仍显示可衡量的准确度退化。

**动态知识库。** 如果你的知识库每小时更新（产品库存、客服工单、新闻流）, 你不能在每次 context window 都重新 embed 整个语料。RAG 的检索步骤天然处理更新——新文件被索引并立即可检索, 不需改 prompt 结构。

**多租户隔离。** 长上下文在权限控制上挣扎。当来自多个用户或权限级别的文件存在同一语料中, RAG 管线能在检索时强制过滤。Context-stuffing 需要小心（且容易出错）的文件分隔。

**规模延迟。** 处理 100 万 token 比处理 5K token 显著慢, 即便是优化后的推论。对面向用户、需要亚秒级回应时间的应用, 针对性检索胜出。

### 2026 更新：Titans + MIRAS 重构长上下文取舍

上面所有限制都假设 Transformer 风格的上下文窗口: 一段被 attention 读取的扁平 token, 每 token 成本不分位置都一样, 同样的「迷失在中间」失效模式。**Titans + MIRAS**, Google Research 2026 年 4 月的架构家族, 打破这个假设。在 Titans 中, 记忆不是 attention 窗口——它是**可训练神经模块**, 在推论期间用梯度下降更新自己的权重, 所以模型字面上把长历史压缩成权重更新, 而非作为 token 向前携带。MIRAS 提供让这种边推论边学过程稳定的训练配方。在参数量相当下, Google 报告 Titans 在长距回忆与多跳推理上优于 Mamba-2、Gated DeltaNet、Transformer++。这并不反驳原本的长上下文限制——那些对 GPT-4 Turbo、Gemini 1.5、Claude 仍在用的 attention 窗口范式仍成立——但它确立**「attention 预算稀缺」框架现在是单一架构家族的属性, 不是普遍约束**。对从业者, 这意味着长上下文取舍不再是单一曲线。现在至少有两条: attention 窗口曲线（迷失在中间和每 token 成本主导）与可训练记忆曲线（成本转向推论时权重更新, 失效模式转向稳定性与遗忘）。RAG 在两者中都仍是强默认, 但 RAG 胜出的*理由*在每个范畴里不同。

---

## GraphRAG：当扁平检索不够

标准 RAG 把文件当独立的 chunk。这对事实查找有效（「退货政策是什么？」）, 但对要求*关系推理*的问题失败（「哪些供应商同时跟我们的延迟出货和质量投诉相连？」）。

[Microsoft GraphRAG](https://github.com/microsoft/graphrag)（2024-2025）引入混合做法: 从来源文件构建知识图, 然后用图遍历配合向量检索回答查询。

### GraphRAG 怎么运作

1. **索引阶段**: 文件被处理以提取实体（人、组织、概念）和它们之间的关系。这些与传统向量 embedding 一起形成图结构。
2. **社群侦测**: 图被分割成密集连接实体的社群。每个社群得到一个总结描述。
3. **查询阶段**: 给定查询, 向量相似度*与*图遍历都被用来检索相关 context。实体关系提供扁平检索错过的多跳推理路径。

### GraphRAG 何时重要

- **多跳查询**: 「2025 年 IPO 公司与被收购公司之间的共同投资人是谁？」——需要遍历关系链
- **以实体为中心的推理**: 关于特定实体与它们对其他实体之连结的问题
- **全局总结**: 「我们所有客户回馈的主题是什么？」——社群总结提供这, 而不需处理每份文件

### GraphRAG 何时过度

- 简单事实查找（标准 RAG 处理得很好）
- 长上下文能容纳一切的小语料
- 实体提取质量低的用例（垃圾进, 垃圾出）

GraphRAG 的索引成本显著高于标准 RAG。只在关系推理是核心需求时建图, 不要作为默认。

### 2026 演化：KG 作为长上下文的语意骨干

整个 2024 与 2025 年大部分时间, GraphRAG 被框为 **RAG 的替代**——一种为有限上下文窗口的模型检索 chunk 的不同方法。到 2026 年, 这个框架转变了。当前沿模型把上下文窗口推到数百万 token 范围（Gemini 1.5 1M、Kimi 超过 200 万中文字、还在扩张）, 问题不再是「我们怎么检索少量相关 chunk」而是「我们怎么导览一个已经够大、能容纳大部分所需的 context」。

在那个世界, 知识图不再是**检索替代品**, 变成 **长上下文的结构化索引层**。图不是用来决定加载哪些 chunk——chunk 已经在窗口里。图是用来给模型一张窗口内容的语意地图: 哪些实体在场、它们如何相关、哪些段落对应哪些主题、矛盾住在哪、哪些多跳路径连结问题与相关证据。GraphRAG 重新浮现为 **语意骨干**, 让 agent 高效走过百万 token 窗口, 而非作为它出生的 8K token 窗口的解决方案。2026 年 4 月可训练记忆模块（Titans + MIRAS）的到来不会取代这个角色——早期证据显示知识图与可训练记忆会**共存且很可能在生产堆叠中组合**, 由图在可训练模块已经压缩进权重的内容上提供类型化、可查询的结构。

---

## 2025-2026 RAG 技术地景

RAG 本身已分支出多个专门做法。关键变体:

### Self-RAG（Asai et al., 2023）

[Self-RAG](https://arxiv.org/abs/2310.11511) 训练模型决定 *何时* 需要检索、*检索什么*、检索内容是否真的相关。不是总是检索, 模型生成特殊的「reflection token」来 gate 检索过程。

**关键好处**: 减少不必要的检索调用, 过滤掉不相关的检索内容, 同时改善效率与准确度。

### Corrective RAG（CRAG）

[Corrective RAG](https://arxiv.org/abs/2401.15884)（Yan et al., 2024）在检索后加一个验证步骤。一个轻量评估器评估检索文件是否与查询相关。如果信心低, 系统触发网页搜寻或替代检索策略作为后备。

**关键好处**: 主要知识库不含答案时优雅退化。

### Adaptive RAG

[Adaptive RAG](https://arxiv.org/abs/2403.14403)（Jeong et al., 2024）用分类器根据复杂度把查询路由到不同检索策略。简单查询直接检索。复杂查询多步检索配思维链推理。模糊查询多次检索 pass 配结果融合。

**关键好处**: 把检索成本与查询复杂度匹配, 而非用一刀切管线。

### Golden-Retriever RAG

Golden-Retriever RAG 聚焦于检索质量, 让 LLM 自己改写查询再检索。模型生成一个「理想文件」描述, 然后用作检索查询而非原始用户输入。

**关键好处**: 桥接用户提问方式与文件写作方式之间的词汇差距。

---

## RAG 作为「Context Engine」

[RAGFlow](https://github.com/infiniflow/ragflow), 开源 RAG 引擎, 2025 年底发表年度回顾, 主张「Retrieval-Augmented Generation」一词不再捕捉现代 RAG 系统在做的事。他们提议的重构: RAG 已从检索技术演化为 **Context Engine**——一个通用系统, 用于把异质来源的相关信息组装到模型 context window。

这个重构与 [第 1 章](01-evolution.md) 描述的 context engineering 演化对齐。RAG 不只是「检索并塞」。一个现代 RAG 系统:

- 分类查询意图与复杂度
- 路由到合适的检索策略（向量、关键字、图、混合）
- 重排与过滤结果
- 压缩检索内容以符合 token 预算
- 用合适结构与 metadata 格式化结果
- 追踪溯源以便引用与验证

这是一个 context 组装管线, 不是检索步骤。RAG 系统*就是* context engine。

---

## 混合架构：收敛

2025-2026 的证据清楚指向混合做法。没有单一技术在所有维度都胜出:

| 维度 | RAG | 长上下文 | 知识图 |
|------|-----|---------|--------|
| 每查询成本 | 低 | 高 | 中 |
| 动态更新 | 强 | 弱 | 中 |
| 关系推理 | 弱 | 弱 | 强 |
| 设置复杂度 | 中 | 低 | 高 |
| 准确度（针对性） | 高 | 中 | 高 |
| 准确度（全局） | 中 | 高 | 高 |

**生产中胜出的 pattern:**

1. **知识图** 处理实体关系与全局理解
2. **RAG** 处理特定查询的动态、针对性检索
3. **长上下文** 处理整份文件重要的有界分析任务
4. **查询路由器** 为每个查询挑对的策略

这不是理论。规模化生产系统（企业搜寻、编程助手、客服 agent）三者并用。工程挑战不是选一个——是建那个为每个查询挑对工具的路由器。

---

## 关键项目与资源

| 项目 | 描述 | 链接 |
|------|------|------|
| Microsoft GraphRAG | 知识图 + RAG 混合 | [github.com/microsoft/graphrag](https://github.com/microsoft/graphrag) |
| RAGFlow | 配深度文件理解的开源 RAG 引擎 | [github.com/infiniflow/ragflow](https://github.com/infiniflow/ragflow) |
| NirDiamant/RAG_Techniques | 综合 RAG 实现集合 | [github.com/NirDiamant/RAG_Techniques](https://github.com/NirDiamant/RAG_Techniques) |
| LangChain | 含广泛 RAG 工具的框架 | [github.com/langchain-ai/langchain](https://github.com/langchain-ai/langchain) |
| LlamaIndex | LLM 应用的数据框架 | [github.com/run-llama/llama_index](https://github.com/run-llama/llama_index) |
| Chroma | 开源 embedding 数据库 | [github.com/chroma-core/chroma](https://github.com/chroma-core/chroma) |

---

## 来源

- Gartner. "Enterprise RAG Adoption" 调查评论, 2025 Q4 ——本章顶引用的 71% 反转数字在多份行业分析中流通; 主要存取需 Gartner 订阅, 所以这个数字在此被作为广为引用的行业数据报告, 而非来自可自由抵达的主要 URL。
- Liu, N. F. 等（2023）. "Lost in the Middle: How Language Models Use Long Contexts." [arXiv:2307.03172](https://arxiv.org/abs/2307.03172)
- Microsoft.（2024）. "GraphRAG: Unlocking LLM discovery on narrative private datasets." [microsoft.com/research](https://www.microsoft.com/en-us/research/blog/graphrag-unlocking-llm-discovery-on-narrative-private-datasets/)
- Asai, A. 等（2023）. "Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection." [arXiv:2310.11511](https://arxiv.org/abs/2310.11511)
- Yan, S. 等（2024）. "Corrective Retrieval Augmented Generation." [arXiv:2401.15884](https://arxiv.org/abs/2401.15884)
- Jeong, S. 等（2024）. "Adaptive-RAG: Learning to Adapt Retrieval-Augmented Large Language Models through Question Complexity." [arXiv:2403.14403](https://arxiv.org/abs/2403.14403)
- RAGFlow.（2025）. "Year-End Review: From RAG to Context Engine." [github.com/infiniflow/ragflow](https://github.com/infiniflow/ragflow)
- NirDiamant.（2025）. "RAG Techniques." [github.com/NirDiamant/RAG_Techniques](https://github.com/NirDiamant/RAG_Techniques)
- Google Research.（2026 年 4 月）. "Titans + MIRAS: Helping AI Have Long-Term Memory." [research.google/blog/titans-miras-helping-ai-have-long-term-memory/](https://research.google/blog/titans-miras-helping-ai-have-long-term-memory/) ——可训练记忆模块在相当尺寸下优于 Mamba-2 / Gated DeltaNet / Transformer++。

---

*上一章: [第 1 章 —— 三个世代](01-evolution.md)*

*下一章: [第 3 章 —— Context Engineering](03-context-engineering.md)*
