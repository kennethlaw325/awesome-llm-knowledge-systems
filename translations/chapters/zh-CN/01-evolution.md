# 第一章：三个世代

> **一句话总结：** AI 工程已经从写好 prompt 演进到围绕 AI 模型设计整个操作系统。
>
> **为什么重要：** 理解这个领域的走向, 帮助你挑选合适的工具, 避免过时的方法。

**从 prompt engineering 到 context engineering 再到 harness engineering——以及为什么这些边界其实没有你想的那么重要。**

---

## 世代 1：Prompt Engineering（2022-2024）

2022 年 11 月 ChatGPT 上线时, 人和大型语言模型之间唯一的接口就是一个文字框。由此诞生的学科叫做 prompt engineering：精心设计输入文字以获得更好输出的艺术与科学。

核心技术快速演进:

**Few-shot prompting**（Brown 等, 2020）证明在 prompt 内放入几个例子就能显著提升任务表现, 而完全不需要 fine-tuning。要让模型分类情感, 你不再训练模型, 而是给它三个例子, 然后问它第四个该怎么分。

**Chain-of-thought（CoT）prompting**（Wei 等, 2022）显示, 加一句「Let's think step by step」或在例子里加上推理过程, 能解锁标准 prompting 看不到的多步推理能力。这可以说是首个迹象——**结构怎么写**和**问什么内容**一样重要。

**Prompt 模板** 成为标准抽象。LangChain、LlamaIndex 以及十几个框架都提供了模板系统, 把变量注入精心设计的 prompt 结构。当时的心智模型很清楚：prompt 是程序, 模型是 runtime。

这个时代的其他技术包括:

- **ReAct**（Yao 等, 2022）: 在单一 prompt 结构内交错推理与行动, 让模型在一个 prompt 里规划并执行工具调用。
- **Tree of Thought**（Yao 等, 2023）: 探索多条推理路径, 选择最佳的一条。
- **Self-consistency**（Wang 等, 2022）: 采样多条推理链, 取多数票决。

这个时代的局限在于它的预设：LLM 互动的质量主要由 prompt 质量决定。当上下文窗口只有 4K-8K token、唯一输入只有用户文字时, 这是对的; 当模型可以吃下 100K+ token 并调用外部工具之后, 这就不再成立。

### 这个时代做对了什么

Prompt engineering 确立了一件事: **结构很重要**。好 prompt 和坏 prompt 的差别不是 vibes, 而是信息架构。这个洞察延续到了之后的一切。

### 这个时代漏掉了什么

它把 context window 当成静态产物。你写好一个 prompt, 提交, 拿到回应。Context window 本身可以**在 runtime 由多个来源动态构建**——这是下一代的洞察。

---

## 世代 2：Context Engineering（2025）

2025 年中, Andrej Karpathy 发了一段后来被疯狂转传的话:

> 「我一直在想这件事, 大多数人真正需要做好的不是『prompt engineering』, 而是『context engineering』——在 context window 里塞入下一步所需正好资讯的艺术与科学。」

这次重构很重要, 因为它把焦点从**指令**（prompt）转移到**整个信息包**（context window）。一次现代 LLM 调用的 context window 远不止用户 prompt:

- 定义行为与限制的系统指令
- RAG 流程检索到的文件
- 工具定义和 schema
- 对话历史（选择性压缩过）
- 动态选择的 few-shot 例子
- 关于当前任务的结构化元数据

Prompt 只是其中一块组件。Context engineering 是把这些全部协同安排。

### 六大技术

[Towards AI 的分析](https://towardsai.net/) 指出 context engineering 的六大核心技术:

1. **Retrieval-Augmented Generation（RAG）**: 在查询时拉取相关文件
2. **工具与 API 整合**: 用结构化 schema 给模型外部能力
3. **记忆管理**: 在对话回合与 session 间维持相关信息
4. **动态 prompt 构建**: 由模板、检索内容和 runtime 状态组装 prompt
5. **Context window 优化**: 管理在有限 token 预算内放什么、不放什么
6. **指令层级**: 系统、开发者、用户指令之间的优先序

### 来自 Manus 的教训

[Manus](https://manus.im/) 是 2025 年话题度最高的 AI agent 平台之一, 分享了大规模 context engineering 的关键教训:

**KV-cache 洞察**: Manus 把 context window 工程化, 维持高 KV-cache 命中率——确保之前 attention 计算出来的 key-value 对可以跨回合重用。这大幅降低 latency 和成本。原则是: 安排 context 让**前缀稳定**, 仅**后缀**在调用之间变。

**100:1 比率**: Manus 报告每 1 个输出 token 大约消耗 100 个 context token。这翻转了输出 token 主导成本的常见假设。真正的工程挑战不是产生文字, 而是**选择什么 context 给模型**。

**Context 是产品**: Manus 把 context window 构建当作核心产品功能, 不是实现细节。他们 agent 的质量直接对应 context 组装管线的质量。

### 分类的转变

Context engineering 把 LLM 应用开发从「写好 prompt」重构为「构建好的信息管线」。模型变成对收到的任何 context 进行推理的引擎。工程挑战往上游移动——到检索、过滤、排序、压缩与组装。

但即使这个框架也有上限。它说明了**进入模型的是什么**, 但没说明**模型周围的系统如何运作**。这需要再一次转变。

---

## 世代 3：Harness Engineering（2026）

2025 年末到 2026 年初, 两份有影响力的内容把下一次演进正式化:

**Birgitta Böckeler**（ThoughtWorks）于 2026 年 4 月在 Martin Fowler 的 *Exploring Generative AI* 备忘录系列中发表分析, 主张 LLM 应用最有影响力的工程工作不是模型训练或 prompt 设计, 而是**harness**——围绕模型的工具、路由、记忆、规划、错误恢复系统, 把模型调用编排成可靠的工作流程。

**OpenAI 的 Codex 团队** 已经发布过关于 agentic coding 的 harness 设计案例资料（公开材料见 openai.com/index/introducing-codex）。在 2025-2026 年 OpenAI 的演讲与文章中流传的「三位工程师 / 约 100 万行 / 约 1,500 个 PR」数字是社区广为引用的, 但底层观察是: Codex 的质量主要不是由模型决定, 而是 harness——决定**何时**调用模型、**提供什么 context**、**让哪些工具可用**、**如何**验证与从错误恢复的系统。

### Phil Schmid 的类比

[Phil Schmid](https://www.philschmid.de/context-engineering) 提出了让这个概念结晶化的类比:

- **模型是 CPU**——原始计算能力
- **Context window 是 RAM**——当前操作的工作内存
- **Harness 是操作系统**——调度、资源管理、I/O、错误处理、用户界面

这个类比说明了为什么 harness engineering 重要: 没人会出货一个没有 OS 的 CPU。模型必要但不充分。Harness 决定模型实际能完成什么。

### Meta-Harness 论文与 6 倍差距

2026 年初的研究论文量化了从业者已经怀疑的事: 一个裸模型与一个有良好 harness 的模型之间的差距, 在复杂任务上大约是**6 倍**。同样权重、同样训练数据的同一个模型, 因为 harness 质量不同, 结果可以差到六倍。

这意味着对大多数实际应用来说, harness engineering 比模型改进有更大杠杆。一个好 harness 配上好模型, 跑赢一个一般 harness 配顶尖模型。

### IMPACT 框架

2020 年代中期的从业者讨论中, **IMPACT 助记词** 浮现为评估 harness 质量的清单:

- **I**nstructions——系统指令的清晰度与完整度
- **M**emory——跨 session 的持续与检索
- **P**lanning——任务分解与排序
- **A**ctions——工具可用性与可靠性
- **C**ontext——相关信息的动态组装
- **T**esting——评估与质量保证回路

IMPACT 把 context engineering 定位为更广 harness engineering 学科里的**一个组件**（「C」）。这种嵌套是关键的结构洞察: context engineering 在 harness engineering **之内**, 不是被它取代。

### Meta 收购 Manus（约 20 亿美元）

2026 年初, Meta 以约 20 亿美元收购 Manus。这场收购被广泛解读为 Meta **买的是 harness, 不是模型**。Meta 已经有 Llama, 它没有的是**生产级、可在 context 组装、工具编排、agent runtime 管理上验证的系统**。

收购验证了那个论点: LLM 生态系统里最有价值的工程, 越来越多在编排层, 而非模型层。

---

## 关键洞察：共存而非取代

这三个世代不是清晰的历史阶段, 不是后一个取代前一个。它们是**嵌套层**, 在每个生产系统内共存:

```
+--------------------------------------------------+
|              HARNESS ENGINEERING                  |
|  +--------------------------------------------+  |
|  |          CONTEXT ENGINEERING                |  |
|  |  +--------------------------------------+  |  |
|  |  |       PROMPT ENGINEERING             |  |  |
|  |  |                                      |  |  |
|  |  |  系统 prompt、CoT、few-shot、         |  |  |
|  |  |  指令格式化                          |  |  |
|  |  +--------------------------------------+  |  |
|  |                                            |  |
|  |  RAG 管线、记忆、工具 schema、              |  |
|  |  context window 优化                       |  |
|  +--------------------------------------------+  |
|                                                  |
|  技能路由、规划回路、错误恢复、                    |
|  渐进式揭露、多 agent 协调                        |
+--------------------------------------------------+
```

一个 harness 工程师仍然写 prompt, 仍然做 context engineering。但他还要建构**系统**——决定何时用哪个 prompt、为每种情境组装哪些 context、出错时如何恢复。

演进不是抛弃早期技术, 而是认识到它们必要但不充分——并在它们之上建构那些把原始 LLM 能力转化为可靠、生产级应用程序的层。

一篇来自上海交通大学等机构的 19 作者综述 **「Externalization in LLM Agents: A Unified Review of Memory, Skills, Protocols and Harness Engineering」**（arXiv 2604.08224, 2026 年 4 月 9 日）独立到达本章使用的相同三层组织: 在他们的框架中, 这个领域的演进从 *weights* 到 *context* 到 *harness*, 而他们把记忆、技能、协议、harness engineering 视为四个由 harness 作为整合层统合的外部化组件。这个收敛对从学术文献来的读者值得标注: 这不是只有从业者用的框架, 也不是这本指南独有——它是 2026 年 4 月底学术综述也独立选择的组织轴心。

---

## 来源

- Brown, T. 等（2020）. "Language Models are Few-Shot Learners." [arXiv:2005.14165](https://arxiv.org/abs/2005.14165)
- Wei, J. 等（2022）. "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models." [arXiv:2201.11903](https://arxiv.org/abs/2201.11903)
- Yao, S. 等（2022）. "ReAct: Synergizing Reasoning and Acting in Language Models." [arXiv:2210.03629](https://arxiv.org/abs/2210.03629)
- Yao, S. 等（2023）. "Tree of Thoughts: Deliberate Problem Solving with Large Language Models." [arXiv:2305.10601](https://arxiv.org/abs/2305.10601)
- Wang, X. 等（2022）. "Self-Consistency Improves Chain of Thought Reasoning in Language Models." [arXiv:2203.11171](https://arxiv.org/abs/2203.11171)
- Karpathy, A.（2025 年中）. 关于 context engineering 的公开发言; 在 X 与 AI engineering 社群广为流传, 奠定了这个领域采用的工作定义。
- Manus.（2025）. "Context Engineering Lessons from Building Manus." [manus.im/blog](https://manus.im/blog) ——KV-cache 命中率作为运营指标、append-only context、工具 logit-bias masking、滚动 todo-list 重写。
- Böckeler, Birgitta.（2026 年 4 月 2 日）. "Harness engineering for coding agent users." martinfowler.com（*Exploring Generative AI* 系列）。[https://martinfowler.com/articles/harness-engineering.html](https://martinfowler.com/articles/harness-engineering.html) ——Guides vs. Sensors、Computational vs. Inferential 分类。
- OpenAI. Codex 公开材料: [https://openai.com/index/introducing-codex](https://openai.com/index/introducing-codex)。Codex 的 harness 设计框架锚点; 广为引用的「三位工程师 / 约 100 万行 / 约 1,500 个 PR」数字在 2025-2026 年 OpenAI 演讲与文章中流传, 在此引用为社群引用而非来自单一 canonical 帖。
- Schmid, Philipp. "The New Skill in AI is Not Prompting, It's Context Engineering" 与续篇。[https://www.philschmid.de/context-engineering](https://www.philschmid.de/context-engineering); [https://www.philschmid.de/context-engineering-part-2](https://www.philschmid.de/context-engineering-part-2) ——模型 = CPU、Context = RAM、Harness = OS 类比。
- IMPACT 助记词。Intent / Memory / Planning / Authority / Control flow / Tools——一个六维 harness 设计清单, 在 2020 年代中期从业者讨论中浮现。在本章作为教学框架使用; 不归属任何特定原始来源。
- Meta/Manus 收购报道.（2026）. 多个来源。
- Zhou, C. 等（2026 年 4 月）. "Externalization in LLM Agents: A Unified Review of Memory, Skills, Protocols and Harness Engineering." [arXiv:2604.08224](https://arxiv.org/abs/2604.08224) ——上海交通大学等机构 19 作者综述, 独立使用 Weights → Context → Harness 三层历史框架。在本章「共存而非取代」一节作为从业者论点与学术文献收敛的证据被引用。

---

*下一章: [第 2 章 —— RAG、长上下文与知识图谱](../../../chapters/02-knowledge-layer.md)（英文）*
