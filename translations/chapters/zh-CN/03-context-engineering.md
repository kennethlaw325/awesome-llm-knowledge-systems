# 第 3 章：Context Engineering —— 填充窗口的艺术

> **一句话总结：** Context engineering 是给 AI 在对的时间正好对的信息的艺术——不多不少。
>
> **为什么重要：** 更好的 context 意味着更好的 AI 答覆。这就是为什么有些人从 AI 取得惊艳结果, 而其他人只得到普通回应。

> 「Context engineering 是用下一步正好需要的信息填满 context window 的微妙艺术与科学。」
> —— Andrej Karpathy, 2025 年 6 月

如果 prompt engineering 是写好一个问题, context engineering 就是建构围绕它的整套简报包。从一者到另一者的转变, 标志着从业者思考 LLM 系统方式的根本变化: 设计单元不再是单一指令, 而是*信息环境*。

本章绘制这个地景——从理论框架到生产验证的 pattern——并指向定义这个学科的主要来源。

---

## 3.1 从 Prompt 到 Context

「Context engineering」一词在 2025 年中进入主流, 当 Karpathy 在它与 prompt engineering 之间画下清楚分界。Prompt 是静态字符串。Context 是模型所需一切的动态组装包——指令、记忆、检索文件、工具定义、对话历史、当下任务——以程式化方式组成, 每一回合都更新。

这个区分重要, 因为现代 agent 极少送两次相同 context。每次推论调用都是路由逻辑、检索管线、压缩启发法、工具可用性检查的产物——这些一起决定窗口装什么、什么被排除。

## 3.2 一个六层 Context 模型

参考 Anthropic 的 [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents) 与相邻从业者写作中的 pattern, context window 可以有用地被分解为六个概念层, 由最持久到最短暂排序。这里的标签是本指南的教学综合, 不是 Anthropic 自己发表的分类:

| 层 | 内容 | 典型持续 |
|----|------|---------|
| **System Rules（系统规则）** | 安全限制、角色定义、行为护栏 | 每部署静态 |
| **Memory（记忆）** | 用户偏好、先前 session 总结、学到的事实 | 跨 session |
| **Retrieved Documents（检索文件）** | RAG 结果、搜寻片段、档案内容 | 每回合 |
| **Tool Schemas（工具 schema）** | 函数定义、API 规格、能力声明 | 每 session 或每回合 mask |
| **Conversation History（对话历史）** | 先前讯息、助手回应、工具调用结果 | 滑动窗口 |
| **Current Task（当下任务）** | 当下的用户请求, 加上任何任务专属注入 | 每回合 |

关键洞察是: 每一层有不同的更新频率、不同的压缩策略、不同的失效模式。把检索文件层塞太满会淹没当下任务讯号。记忆层填得不够会迫使模型重新推导它本应已经有的 context。好的 context engineering 是六个层同时的平衡。

## 3.3 来自 Manus 的教训：KV-Cache 是北极星

2025 年 7 月, Yichao「Peak」Ji（Manus CTO）发布一组生产教训, 把 context engineering 围绕单一运营指标重构: **KV-cache 命中率**。

Manus 在他们 agent 系统中观察到稳定的 100:1 输入对输出 token 比。在那个比例下, 输入成本主导一切。KV-cache 命中——之前算过的 key-value 对被重用而非重算——成为 latency 与成本的主要杠杆。

三个技术从这个洞察浮现:

1. **Append-only context 结构。** 永不重写 context 的早期部分。中间的插入或编辑会让快取的前缀失效, 强制完全重算。把你的 context 设计为一份 log, 不是文档。

2. **用 logit bias 作工具 mask, 不要移除 schema。** 当一个工具暂时不可用, Manus 在 logit 层级压制它的选择, 而非把工具定义从 context 移除。移除定义改变 token 序列, 破坏快取。Mask 保留前缀同时阻止选择。

3. **滚动 todo-list 重写。** 不是依赖模型从长对话早期回想目标, Manus 周期性在 context 末尾附上重写过的 todo list。这利用 attention 中的近因偏差——最近 token 中的目标得到比埋在数千 token 之前同样目标更强的 attention 权重。

这些是基础设施级决策, 不是 prompt 级。它们说明为什么「context engineering」需要系统思维。

## 3.4 五种主导 Pattern

Aurimas Griciūnas 把浮现实务综合为在生产系统中观察到的五个反复 pattern（标准写作: 「State of Context Engineering in 2026」, SwirlAI Newsletter, 2026 年 3 月 22 日, [https://www.newsletter.swirlai.com/p/state-of-context-engineering-in-2026](https://www.newsletter.swirlai.com/p/state-of-context-engineering-in-2026); 也见「Breaking Down Context Engineering」）:

**渐进式揭露。** 不要前置加载一切。先呈现一个轻量索引; 只在模型（或路由逻辑）判定相关时展开段落。这是 context window 的 lazy loading 等价物。Anthropic 自家 agent skills 系统用这个 pattern——17 个技能在静态时消耗约 1,700 token, 仅在调用时展开。

**Context 压缩。** 在注入前总结、截断、或蒸馏信息。滑动窗口之外的对话历史被压成总结。检索文件被节录成相关段落。目标是保留语意密度同时减少 token 数。

**Context 路由。** 不是所有查询都需要相同 context。路由层检视进来的请求, 选择要包含哪些记忆库、工具集、文件集合。这是数据库查询规划器的 context window 类比。

**检索演化。** 静态 RAG（检索一次、注入、产生）让位给迭代检索, 模型可以在生成中途请求额外信息。Context 不是一次组装, 而是在生成过程中演化。

**工具与能力管理。** 当工具库变大, 加载所有 schema 变得不可行。系统用 meta-tool pattern（按需返回相关工具 schema 的发现工具）或技能图架构来保持工具层精简。

## 3.5 学术地景

2025 年中带来了 context engineering 作为正式研究领域的第一份综合学术综述: **「A Survey of Context Engineering for Large Language Models」**（Mei et al., arXiv 2507.13334, 2025 年 7 月 17-21 日）, 它透过对 1,400+ 篇研究论文的系统分析, 为这个领域建立技术 roadmap。该综述把设计空间沿两个轴组织: **基础组件**（context 检索与生成、context 处理、context 管理）与**系统实现**（RAG、记忆系统、工具整合推理、多 agent 系统）。它的承重发现是基本能力不对称: 当前模型在理解复杂 context 上极擅长, 但在产生同样精致的长篇输出上有显著局限。对从业者, 这份综述是这个领域最接近教科书的东西——它把一直在经验上发现的事正式化: context engineering 不是单一技术而是有多个独立维度的设计空间。

## 3.6 Agentic Context Engineering（ACE）

ACE 论文 **「Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models」**（Zhang et al., arXiv 2510.04618, 2025 年 10 月 6 日; 配套 repo 在 [github.com/ace-agent/ace](https://github.com/ace-agent/ace)）引入概念转变: 把 context 视为不是静态组装而是**演化的 playbook**。在 ACE 系统中, context 是一份 agent 自己维护的活文件——加观察、更新计画、修剪不相关历史、根据任务进展重组自己的指令。报告中头条收益: 在 agent 基准上 +10.6%, 在金融任务上 +8.6%, 配 adaptation latency 与 rollout 成本的减少; 在 AppWorld 排行榜上, ACE 在整体平均上和顶尖生产级 agent 持平, 在更难的 test-challenge split 上超越它, 即使用较小的开源模型。ACE 也命名它要工程对抗的失效模式: **简洁偏差**（为简洁总结丢掉领域洞察）与 **context 崩塌**（迭代重写久了侵蚀细节）。

这把 context engineering 从纯基础设施关切（harness 在每次调用前组装什么）移到协作的（harness 准备的*以及*模型主动重塑的）。「系统提供的 context」与「模型创造的 context」之间的边界变得流动。

ACE 系统典型在 context 内维持一个结构化 scratchpad——一个指定区域, 模型在那里写工作笔记、中间结果、修订的计画。Harness 跨回合保留这个区域, 同时按它自己的政策管理周围的层。

## 3.7 实务含义

几个原则从这个地景浮现:

- **衡量输入 token, 不只输出。** 在生产规模, 100:1 输入/输出比意味着 context 组装成本主导。为快取命中与最少冗余优化。
- **把 context 设计为分层系统。** 每一层有自己的更新政策、压缩策略、失效模式。独立处理它们。
- **默认用渐进式揭露。** 起步精简。按需展开。包含不相关信息的成本不只是 token——是退化的 attention 与增加的幻觉风险。
- **测试 context 组成, 不只 prompt。** 同样 prompt 在不同 context 中产生不同结果。你的测试套件应该变化 context, 不只最终指令。
- **预期模型改进。** 当模型在长 context 推理上变好, 一些压缩与路由策略变成不必要的开销。用清楚的抽象边界建构, 让层可以被简化或移除。

---

## 来源

- **Karpathy, Andrej.** 关于「context engineering」的公开发言（2025 年中）。在 X 与 AI engineering 社群广为流传的框架, 奠定这个领域采用的工作定义。
- **Anthropic.** "Building Effective Agents." Anthropic 工程博客, 2024 年 12 月 19 日。[https://www.anthropic.com/engineering/building-effective-agents](https://www.anthropic.com/engineering/building-effective-agents) ——描述 orchestrator-worker pattern 与 evaluator-optimizer workflow; 本指南把第 3.2 节的六层概念框架作教学使用。
- **Ji, Yichao "Peak"**（Manus）. "Context Engineering Lessons from Building Manus." 博文, 2025 年 7 月。[manus.im/blog](https://manus.im/blog) ——KV-cache 命中率作为运营指标、append-only context 结构、用 logit bias 作工具 mask、滚动 todo-list 重写。
- **Griciūnas, Aurimas.** "State of Context Engineering in 2026." SwirlAI Newsletter, 2026 年 3 月 22 日。[https://www.newsletter.swirlai.com/p/state-of-context-engineering-in-2026](https://www.newsletter.swirlai.com/p/state-of-context-engineering-in-2026)。也见 "Breaking Down Context Engineering": [https://www.newsletter.swirlai.com/p/breaking-down-context-engineering](https://www.newsletter.swirlai.com/p/breaking-down-context-engineering)
- **Mei, Lingrui et al.** "A Survey of Context Engineering for Large Language Models." arXiv 2507.13334, 2025 年 7 月 17-21 日。[https://arxiv.org/abs/2507.13334](https://arxiv.org/abs/2507.13334) ——1,400+ 论文综述, 把 context engineering 确立为正式研究领域。
- **Zhang, Qizheng et al.** "Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models." arXiv 2510.04618, 2025 年 10 月 6 日。[https://arxiv.org/abs/2510.04618](https://arxiv.org/abs/2510.04618)。配套 repo: [github.com/ace-agent/ace](https://github.com/ace-agent/ace)。把 context 框为演化的 playbook; 命名简洁偏差与 context 崩塌。
- **Schmid, Philipp.** "The New Skill in AI is Not Prompting, It's Context Engineering" 与续篇。[https://www.philschmid.de/context-engineering](https://www.philschmid.de/context-engineering); [https://www.philschmid.de/context-engineering-part-2](https://www.philschmid.de/context-engineering-part-2)
- **LangChain 博客.** Context engineering 报道在 [blog.langchain.com](https://blog.langchain.com) ——「Agent Engineer」作为从业者 pattern 的框架（无单一标准帖; 在此作为讨论锚点引用）。
- **Willison, Simon.** [simonwillison.net](https://simonwillison.net) 上持续的 AI engineering 报道——把生态系串连的可亲实务介绍。

---

*上一章: [第 2 章 —— RAG、长上下文与知识图谱](02-knowledge-layer.md)*

*下一章: [第 4 章 —— Harness Engineering](04-harness-engineering.md)*
