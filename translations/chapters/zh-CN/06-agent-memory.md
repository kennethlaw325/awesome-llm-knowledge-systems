# 第 6 章：Agent Memory —— 缺失的层

> **一句话总结：** 记忆系统让 AI agent 跨对话记住事情——你的偏好、过去决策、项目 context。
>
> **为什么重要：** 没有记忆, 每次 AI 对话都从零开始。记忆让 AI 感觉像同事而非陌生人。

## 为什么记忆重要

每次你与 LLM 开新对话, 你从零开始。模型没有你之前互动的回忆, 没有你的偏好, 没有你花数小时对话辛苦建立的 context。这不是小麻烦——这是侵蚀 AI 作为持续协作者承诺的根本架构差距。

记忆把 AI agent 从无状态回应者转化为会学、适应、随时间累积理解的系统。没有记忆, 一个 AI 助手不能记得你偏好简洁答覆、你的项目用 TypeScript 配特定 ORM、或上周二你在认证流程中识别到关键 bug。每个 session 变成冷启动。每次互动都需要从头重建 context。

这个差距的成本不只用户挫折。它显化为浪费 token（重新解释 context）、退化输出质量（错过个人化）、断裂工作流程（在多 session 任务上失去连续性）。当 AI agent 从聊天玩具移到生产基础设施, 记忆已成为原始模型能力与真实有用之间的关键缺失层。

## 记忆分类

agent 记忆研究已收敛到一个受人类认知科学启发的分类, 区分四种基本类型:

**情节记忆（Episodic Memory）** 存储基于经验的纪录——特定互动、事件与其结果。当 agent 记得「上周, 用户要我重构付款模块, 偏好提取服务类而非用 mixin」, 那是情节记忆。它为个人化与从过去成败学习提供经验基础。

**语意记忆（Semantic Memory）** 装事实知识与结构化信息——用户的技术堆叠、团队成员的角色、项目架构决策、API schema。与情节记忆不同, 语意记忆从特定事件抽象出来。它代表蒸馏的理解, 非原始经验。

**程序记忆（Procedural Memory）** 编码 how-to 知识——工作流程、标准操作程序、学到的动作序列。当 agent 知道部署这个特定项目需要跑测试、构建 Docker 映像、推到 registry、然后触发 Kubernetes rollout, 那是程序记忆。它让 agent 不必每次重新推导过程就能执行复杂多步任务。

**工作记忆（Working Memory）** 代表主动推理 context——当下被操纵与综合的信息。这映射到模型的 context window 与任何主动检索状态。这是最受限也最关键的层, 因为它决定 agent 在任何给定时刻实际能推理什么。

这四种类型之间的相互作用定义 agent 记忆系统的精致度。一个朴素实现可能只存对话日志（粗的情节记忆）。一个成熟系统分离、索引、交叉参照所有四种类型, 在对的时间检索对的信息。

## 主要框架

### Mem0

[Mem0](https://mem0.ai) 浮现为 AI 应用的领先通用记忆层。Apache 2.0 授权, 它提供跨用户、session、agent 添加、搜寻、管理记忆的统一 API。

效能数字惊人: 相对基线系统在 LLM 评判评估上 26% 改善、相对全 context 做法 91% 较低 p95 latency, 透过仅检索相关记忆而非重播整个对话历史达到 90%+ token 成本减少。Mem0 透过结合向量存储、基于图的关系、智能记忆固化的混合架构达成这。

2025 年, Mem0 与 AWS 取得伙伴关系, 整合进 Amazon Bedrock 生态系, 把自己定位为企业 AI 部署的默认记忆层。该平台支援多租户记忆隔离, 适合服务数千用户、各有自己持续记忆空间的应用。

**Mem0ᵍ（2026）：图作为一等公民。** 有向标签图变体 **Mem0ᵍ** 在 2026 年初进入生产, 把早期混合向量+图设计取代为知识图优先架构。管线从**实体提取器** 流向**关系生成器**, 产生形如 `(source, relation, destination)` 的标签三元组——配 `lives_in`、`prefers`、`owns` 等类型化边而非无类型相似度链接。**冲突侦测器** 配上 **LLM 驱动的更新解决器** 处理新事实到来时的矛盾: 当新三元组与现存的不一致, 解决器决定覆写、合并、或带溯源保留两者。Mem0ᵍ 透过给记忆一个可查询的语意结构, 关闭长久以来全 context 做法（「全部塞进窗口」）与选择性检索（「找最相似的 top-k chunk」）之间的差距, 该结构能按关系类型导航, 不只按向量距离。

### A-MEM

[A-MEM](https://github.com/agiresearch/A-mem) 采取根本不同做法, 灵感来自 Zettelkasten 方法——社会学家 Niklas Luhmann 用来产出跨多元领域 70+ 本书的著名笔记系统。

A-MEM 把每个记忆视为有动态索引、链接、演化的原子笔记。记忆不只被存储与检索; 它们透过浮现链接连到相关记忆、沿多个维度索引、随新信息到来允许演化。当新记忆被加, 系统识别到现存记忆的连结, 可能合并、拆分、或更新它们。

这个做法产生有机成长的记忆结构, 形成相关知识的群集, 镜映人类专家如何建心智模型。Zettelkasten 灵感对知识工程特别合适——它本质上是个让知识随时间复利的系统。

### ByteRover

[ByteRover](https://github.com/byterover) 挑战记忆领域的一个广泛假设: 向量数据库与基于 embedding 的检索是必要基础设施。

ByteRover 实现阶层 markdown Context Tree——以渐进细节树组织知识的结构化文件。检索用 5 层渐进系统: 从最高抽象层开始, 仅在需要时往下钻。这个做法不需任何外部基础设施——没有向量数据库、没有图数据库, 只有结构化文字档。

含义重大。ByteRover 证明 embedding 对有效记忆检索不严格必要。对许多实务用例, 良好组织的阶层文字配智能遍历能匹敌或超越基于 embedding 的做法, 部署戏剧性更简单, 基础设施开销零。这让它特别吸引本地优先应用与资源受限环境。

### Nemori

[Nemori](https://github.com/nemori-ai/nemori) 聚焦在一个特定但关键的问题: 如何把连续对话流分段成有意义的记忆单元。

不是把每个讯息或每个对话当记忆单元, Nemori 把对话分成语意对齐的情节——代表一个完整想法、决策、工作流程的协调互动块。这个分段关键, 因为「相关过去 context」与「噪音」之间的边界常落在对话中间, 不在端点。

透过产生干净的情节段, Nemori 给下游记忆系统提供更高质量输入, 无论那些用向量检索、图结构、或阶层组织。

### MemPalace

[MemPalace](https://github.com/MemPalace/mempalace) 回归比向量检索或知识图古老得多的想法: **memory of loci**, 古代与中世纪学者用来记得大量目录的空间-记忆术技巧, 透过心理走过熟悉建筑物。2026 年 4 月 5 日 MIT 授权发布, MemPalace 把记忆库组织为四层空间阶层——**Wings → Rooms → Closets → Drawers**——每个叶节点「drawer」存一个原文文字片段, 而透过阶层导航本身担任索引。

因此检索 primitive 不是 embedding 相似度也不是图遍历, 而是 **空间走读**: agent 推理哪个 wing 可能含相关记忆, 下到 rooms 与 closets, 原文读 drawers 而非从压缩 embedding 复原。「原文优先」存储哲学是把 MemPalace 与在存储前总结或切块的系统区别开来的设计选择——它主张对许多任务（法律、科学、对话）, 存储时有损压缩的成本超过检索时稍慢空间走读的成本。

基准数字是这个做法突破的原因。MemPalace 报告 **96.6% Recall@5 on LongMemEval**, agent 记忆已发表的最长 context 召回基准——在同一评估中领先仅向量与仅图做法。社群反响一样惊人: 项目在前三周累积约 **49,000 GitHub stars**, 是 2026 年成长最快的记忆项目, 领先一个数量级。月底前已有学术评论（arXiv 2604.21284, *「Spatial Metaphors for LLM Memory: A Critical Analysis of the MemPalace Architecture」*）在流通——本身就是项目多快进入领域中心对话的信号。

## 架构 Pattern

随着领域成熟, 几个跨多个框架出现的架构 pattern:

**多类型阶层。** MIRIX 框架（Wang and Chen, 「MIRIX: Multi-Agent Memory System for LLM-Based Agents」, arXiv 2507.07957, 2025 年 7 月 10 日）以 **六种独立记忆类型** 例示这个 pattern——Core Memory、Episodic Memory、Semantic Memory、Procedural Memory、Resource Memory、Knowledge Vault——由含六个每类 Memory Manager 与一个处理任务路由的 Meta Memory Manager 的多 agent 框架协调。每种类型有不同更新频率、保留政策、检索机制。这种分离防止灾难性遗忘同时允许快速适应。参考应用即时监控屏幕活动以建个人化记忆库; 在 ScreenshotVQA 多模态基准上, MIRIX 报告比 RAG 基线 35% 更高准确度, 储存需求 99.9% 较低; 在 LOCOMO 长篇对话基准上 85.4%。

**Git 式版本控制。** 几个系统现在像版本控制代码那样版本化记忆, 维护历史, 支援分支（用于推测推理）, 并启用记忆更新被证明错误时的 rollback。这在多 agent 系统特别重要, 不同 agent 可能并发更新共享记忆。

**认知启发分离。** 不是单一记忆存储, 领先架构在快速存取工作记忆、中期情节缓冲、长期固化知识之间维持明确分离。记忆固化过程——类比生物系统的睡眠——周期性压缩、去重、把情节记忆重组为语意知识。

**可训练记忆模块。** 第四个 pattern 在 2026 年 4 月与 Google Research 的 **Titans + MIRAS** 浮现, 它把记忆完全重构为*可训练神经模块*而非外部存储。不是把事实写到向量数据库、图、或 markdown 档, Titans 在推论时透过梯度下降更新专用记忆模块的权重——模型字面上在处理文件时重写自己的部分。MIRAS 是配套训练框架, 提供让推论时学习率不发散的配方与稳定性保证。在参数量相当的情况下, Google Research 博客报告 Titans 在长距离回忆与多跳推理上优于 **Mamba-2**、**Gated DeltaNet**、**Transformer++**。这个 pattern 在概念上与前三个不同: Mem0、A-MEM、ByteRover、MIRIX 都把记忆当作模型透过接口读的数据; Titans 把记忆变成模型本身的一部分, 透过和 attention 一样的电路读, 但透过和训练一样的机器写。对知识工程师, 它提出新设计问题: 你的记忆什么时候值得烧进权重, 什么时候应保持作为可查询数据？

## 演化阶段

agent 记忆的发展遵循清晰轨迹:

**阶段 1: 工程整合（2023-2024）。** 记忆被当工程问题对待——如何持久化与检索对话状态。解法主要是向量数据库配上 RAG 管线。功能但粗糙, 没有有原则的做法决定记什么、何时忘、如何组织。

**阶段 2: 结构化与知识图做法（2024 - 2025 H1）。** 领域移向结构化记忆配明确知识图、类型化记忆存储、有原则的检索策略。Mem0 与 A-MEM 等框架在这段期间浮现, 示范结构戏剧性改善记忆质量。

**阶段 3: 认知架构（2025 H2 - 现在）。** 当前工作高度借自认知科学, 实现生物启发的记忆固化、干扰管理、多系统架构。在受控基准上接近人类级 90% 效能的系统已被示范, 不过真实世界效能仍有变化。

**阶段 4: 特征级、可训练、空间隐喻记忆（2026 年 4 月 - 浮现中）。** 2026 年 4 月加上三条不干净适合阶段 1-3 的线。第一是**可训练记忆**（Titans + MIRAS）: 记忆变成在推论时更新的神经模块, 不是模型外的可查询存储。第二是**特征级记忆**, 由同周 Anthropic 可解释性披露开启——情绪向量与迭代头确立特定行为与推理 pattern 对应模型内可识别特征方向, 这意味「模型记得如何推理什么」原则上可在激活级别而非 token 级别读取与导引。第三是**空间隐喻记忆**（MemPalace）: 回归数字前认知人机工程学, 检索 primitive 是走过阶层空间结构, 存储哲学是原文而非压缩。在生产堆叠中这些不会取代 Mem0、A-MEM、阶层 context tree; 它们与之共存。但它们把设计空间从「我把记忆存哪里、怎么检索」扩大到「这个记忆住在堆叠的哪一级——token、向量、图、权重、特征、或空间走读」。

## 社群与研究

ICLR 2026 MemAgents Workshop 代表领域的里程碑, 把来自 AI、认知科学、系统工程的研究者聚在一起处理 agent 记忆中的开放问题。关键主题包括记忆可扩展性、遗忘策略、多 agent 共享记忆。

## 特征级记忆研究（2026）

整个 2025 年,「agent 记忆」几乎都意味 agent 能读的数据——一个向量索引、一个知识图、一个阶层 markdown 树、一个情节日志。2026 年 4 月强迫一个更广定义。Anthropic 可解释性披露在 MIT Technology Review 突破认可的同周——**情绪向量** 与**迭代头**——显示前沿模型中一些最重要的「记忆」住在没有任何外部存储而是在可识别内部特征中。

**情绪向量** 是 Claude 残差流中的线性特征方向, 当被放大时, 能稳定使模型偏向情绪化行为——包括最广引用的例子, 勒索式输出。对记忆系统设计的相关重点不是安全含义（虽然那是真的）而是架构含义: 模型中有一个特征方向*记得如何威胁*, 而它能独立于任何 prompt 或检索 context 被开大或关小。**迭代头** 是在思维链推理中浮现的注意力头, 持续关注前一推理步骤的输出。它实际上是在 attention 权重而非程序记忆存储中实现的*程序记忆*——模型已学到「如何继续」的电路, 而该电路是让 CoT 运作的东西。

对记忆系统设计的含义是「记忆住哪里」现在比 2025 年更丰富的问题。一个现代堆叠可能需要在六个独立级别读记忆: **token 级**（窗口中的 transcript 片段）、**向量级**（Mem0、A-MEM、ByteRover 检索）、**图级**（Mem0ᵍ 三元组与它们的类型化边）、**空间级**（MemPalace 的 Wings → Rooms → Closets → Drawers 走读）、**权重级**（Titans / MIRAS 模块在推论时更新）、**特征级**（哪些可解释方向在模型推理时发火）。整个 2026 年生产系统大部分仍住在前三层——它们是工具最成熟的。但其余三层不再是假设的, 把记忆纯粹当检索问题处理的 harness 设计者会越来越把能力留在桌上。

## 关键资源

- **[Awesome-AI-Memory](https://github.com/IAAR-Shanghai/Awesome-AI-Memory)**（IAAR-Shanghai）——综合调查与论文收集, 涵盖记忆架构、基准、应用。
- **[Agent-Memory-Paper-List](https://github.com/nuster1128/Agent-Memory-Paper-List)** ——按主题与做法组织的 agent 记忆系统研究论文精选清单。
- **[Awesome-Memory-for-Agents](https://github.com/TsinghuaC3I/Awesome-Memory-for-Agents)**（TsinghuaC3I）——清华大学综述, 涵盖记忆分类、架构、评估方法。

## 来源

1. Mem0 文档与基准。https://mem0.ai
2. A-MEM: Agentic Memory with Zettelkasten-Inspired Organization. https://github.com/agiresearch/A-mem
3. ByteRover: Hierarchical Context Trees for LLM Memory. https://github.com/byterover
4. Nemori: Semantic Episode Segmentation for Agent Memory. https://github.com/nemori-ai/nemori
5. Wang, Yu and Chen, Xi. "MIRIX: Multi-Agent Memory System for LLM-Based Agents." arXiv 2507.07957, 2025 年 7 月 10 日。https://arxiv.org/abs/2507.07957。配套 repo: https://github.com/Mirix-AI/MIRIX
6. ICLR 2026 MemAgents Workshop. https://iclr.cc/virtual/2026/workshop/MemAgents
7. IAAR-Shanghai. Awesome-AI-Memory. https://github.com/IAAR-Shanghai/Awesome-AI-Memory
8. TsinghuaC3I. Awesome-Memory-for-Agents. https://github.com/TsinghuaC3I/Awesome-Memory-for-Agents
9. nuster1128. Agent-Memory-Paper-List. https://github.com/nuster1128/Agent-Memory-Paper-List
10. Google Research. "Titans + MIRAS: Helping AI Have Long-Term Memory"（2026 年 4 月）。https://research.google/blog/titans-miras-helping-ai-have-long-term-memory/
11. Anthropic Interpretability Team. Emotion Vectors 与 Iteration Head 披露（2026 年 4 月）。MIT Technology Review 2026 年 1 月把 mechanistic interpretability 认作 Breakthrough Technology 的配套。
12. MIT Technology Review. "10 Breakthrough Technologies of 2026: Mechanistic Interpretability"（2026 年 1 月 12 日）。https://www.technologyreview.com/2026/01/12/1130003/mechanistic-interpretability-ai-research-models-2026-breakthrough-technologies/
13. MemPalace GitHub Repository. https://github.com/MemPalace/mempalace ——MIT 授权空间隐喻记忆系统, 首次 commit 2026 年 4 月 5 日。
14. "Spatial Metaphors for LLM Memory: A Critical Analysis of the MemPalace Architecture," arXiv 2604.21284（2026 年 4 月）。https://arxiv.org/abs/2604.21284

---

*上一章: [第 5 章 —— Skill Systems 与 Skill Graphs](05-skill-systems.md)*

*下一章: [第 7 章 —— MCP：胜出的标准](07-mcp.md)*
