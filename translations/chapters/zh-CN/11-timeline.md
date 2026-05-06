# 第 11 章：LLM 知识工程的关键时刻

> **一句话总结：** 一份从 2022 到 2026 年塑造 LLM 知识工程的关键时刻按时间排序的记录。
>
> **为什么重要：** 本指南内一切的背景脉络——何时发生、谁做的、改变了什么。

![LLM 知识工程时间线 2022-2026](../../../diagrams/timeline.png)

一张按时间顺序绘制的事件、发布与想法地图, 显示我们如何用大型语言模型构建知识系统。已知精确日期会标出。只确认季度或月份的, 就用该粒度。

这是一份**精挑**的时间线, 不是详尽的。一个事件能上这份清单, 是因为它**引入、验证或操作化**本框架追踪的某个 primitive、pattern 或 narrative beat。许多值得注意的发布——模型版本递增、融资轮、垂直产品——是被刻意排除的。完整收录标准见 [CONTRIBUTING.md](../../../CONTRIBUTING.md)。

---

## 2022

### 11 月 30 日 —— ChatGPT 上线

OpenAI 推出 ChatGPT, 一个对话式接入 GPT-3.5 的界面。两个月内累积 1 亿用户, 是有史以来最快的消费技术普及。「prompt engineering」时代由此开启: 用户发现「怎么问」和「问什么」一样重要。

---

## 2023

### Q1-Q2 —— RAG 框架兴起

**LangChain** 与 **LlamaIndex** 作为最早的 LLM 应用开发框架快速被采纳。Retrieval-Augmented Generation（RAG）成为把 LLM 回应建立在外部知识之上的标准 pattern。架构简单但具变革性: 检索相关文件、注入 prompt、产生有根据的回应。LLM 第一次能回答关于它从未训练过的私人数据的问题。

### 11 月 —— GPT-4 Turbo 与 128K 上下文窗口

OpenAI 在 DevDay 公布 GPT-4 Turbo, 配 128K token 上下文窗口。从 GPT-4 的 32K 扩张 4 倍, 改变了知识检索的经济学: 整份文件能塞进 context, 在某些用例下减少切块与检索的需要。「全部塞进 context」流派开始成形。

### 12 月 —— Gemini 1.0 推出

Google 推出 Gemini 1.0, 它的第一个原生多模态模型。从一开始就为处理文字、图像、声音、视频而打造, 标志着知识工程将必须处理的不只是文字。

---

## 2024

### 2 月 —— Gemini 1.5 与 1M token 上下文窗口

Google 发布 Gemini 1.5 Pro, 配 100 万 token 上下文窗口。这不是渐进改进——这是范式转换。整个 codebase、整本书、几小时的视频转录都能放进单一 prompt。「RAG vs. long context」论战升温。从业者开始意识到, 长上下文不会消除检索; 它改变了检索的用途。

### 3 月 —— Kimi 达到 200 万中文字符上下文

Moonshot AI 的 Kimi 达到 200 万中文字符上下文窗口, 是任何针对中文优化的模型中最长的。这让中文企业用例的全文件处理变得可行——法律合同、监管申报、技术手册——这些过去都不切实际。

### 11 月 —— Anthropic 发布 Model Context Protocol（MCP）

Anthropic 把 MCP 公开为开放规格, 用于把 LLM 连接到外部工具与数据源。MCP 标准化模型如何发现、认证、调用工具——取代过去碎片化的客制化 function-calling 实现景观。它被设计为协议, 不是产品: 任何模型供应商或工具开发者都能实现它。与 USB 或 HTTP 的类比是有意为之。这个时刻标志着可互操作知识基础设施的开端。

---

## 2025

### 1 月 —— DeepSeek R1 与开源拐点

DeepSeek 发布 R1, 一个开放权重的推理模型, 在关键基准上和 OpenAI o1 持平。训练成本不到 600 万美元, MIT 授权发布, 它证明前沿推理能力不再是资金充裕实验室的专利。中国企业开源模型采用率从 23% 飙升到 67%。对知识工程的含义: 基础模型不再是瓶颈或护城河。

### 2025 年中 —— 「Context Engineering」进入词汇

Andrej Karpathy 公开支持用 **「context engineering」** 取代「prompt engineering」, 主张这个学科已经远超精心设计单一 prompt。这次转变反映一个更广的认知: 重要的不是孤立的 prompt, 而是整个 context 组装管线——什么被加载、何时、按什么顺序、为什么。社群很快采纳这个框架。

### 7 月 —— Manus 公布 Context Engineering 教训

自主 agent 创业公司 Manus 发布详细博文, 谈他们对 context engineering 的方法。关键洞察包括: 把 context window 当作随任务完成自然缩短的「todo list」、用文件系统操作作为延伸记忆、以及「context engineering 是在对的时间用对的格式给出对的信息的艺术」的重要性。该贴成为从业者的参考文件。

### 9 月 —— Notion 3.0：AI Agent 重构

Notion 发布 3.0 版, 从地基重新建为 AI 原生工作空间。核心知识管理功能——数据库、页面、关联——被重新架构以与 AI agent 无缝运作。这重要不是作为单一产品发布, 而是主流生产力工具向知识 harness pattern 收敛的证据: 结构化知识 + agent 编排 + context engineering。

### 10 月 —— Anthropic 推出 Agent Skills

Anthropic 为 Claude 引入技能系统, 允许用户定义可重用、可组合的能力, agent 能发现并调用。技能被结构化为 markdown 档配 YAML frontmatter, 定义触发条件、参数、依赖。这把高级用户已经非正式建构的 pattern 正式化: 可重用 agent 行为的库。

### 11 月 —— MCP 越过 800 万下载

Model Context Protocol 达到 800 万 SDK 下载, 比 12 个月前的近零增长极快。该协议已成为 LLM 与工具整合的事实标准, 涵盖每个主要模型供应商和数百个工具服务器的实现。

### 12 月 —— 决定性的一个月

2025 年 12 月数件事汇聚:

- **Anthropic 在 agentskills.io 公布技能开放标准**, 提议任何平台都能实现的 agent 能力共享格式。
- **MCP 捐给 Linux Foundation**, 巩固它作为由开源社群维护的供应商中立协议的地位。
- **渐进式揭露** 被主要平台采纳为技能与 context 管理的标准做法, 验证了多个团队独立开发的 pattern。
- **Meta 以约 20 亿美元收购 Manus**, 信号自主 agent 基础设施现在已是最大规模的策略性资产。

---

## 2026

### 1 月 —— ERNIE 5.0 与 Kimi K2.5

- **ERNIE 5.0** 由百度推出: 2.4 万亿参数, 原生全模态（单一模型内的文字、图像、声音、视频）。
- **Kimi K2.5** 引入 Agent Swarm: 单一查询能 spawn 至多 100 个子 agent, 透过约 1,500 次工具调用协作。这不是 demo——是用于复杂多步研究任务的生产功能。

### 2 月 —— Heinrich 的 Skill Graphs 贴

Heinrich（`@arscontexta`）关于技能图的贴——如何用图结构组织、组合、路由 agent 技能——在 2026 年初病毒式传播, 跨进了更广的 AI engineering 受众。回响显示从业者社群渴求的是架构 pattern, 不只是模型能力。技能路由与组合作为一等工程关注点浮现。原贴: [https://x.com/arscontexta/status/2023957499183829467](https://x.com/arscontexta/status/2023957499183829467)。

### 3 月 —— 研究论文

两篇重要论文发表:

- **「Meta-Harness」** 用同样的基础模型证明朴素 harness 与精心工程的 harness 之间有 6 倍效能差距。该论文为生产知识系统提供了实证: harness engineering 比模型选择更重要。
- **「SkillReducer」** 处理浮现中的技能扩散问题, 提出透过自动去重、聚类、阶层组织来管理含 55,000+ 技能的系统的技术。

### Q1 —— MCP 规模化

MCP 达到每月 9,700 万 SDK 下载, 比 2025 年 11 月成长 12 倍。该协议现已嵌入 CI/CD 管线、IDE 扩展、企业平台、消费应用。可互操作的承诺正在实现: 为某模型写的工具服务器能与任何模型一起运作。

### 2026 年 4 月 —— 初次发布

本研究报告发表, 试图把过去四年的快速发展综合成一个对从业者连贯的框架。这个领域演进的速度远超任何单一文件能捕捉的。

### 2026 年 3 月 31 日 —— Claude Code 原始码外泄

Anthropic 不慎在 npm 包 `@anthropic-ai/claude-code` v2.1.88 内运送一份 59.8MB 的 source map, 暴露约 513,000 行未混淆 TypeScript, 跨 1,906 档。外泄揭示一个三层 **「Self-Healing Memory」** 架构, `MEMORY.md` 担任轻量级指针索引而非完整存储。还暴露 **KAIROS** feature flag——一个在原始码中被引用超过 150 次的自主 daemon 模式——以及另外 44 个用于未发布功能的隐藏 feature flag。Anthropic 把事件描述为「人为打包错误, 不是安全外泄」。即便如此, 外泄交出了对生产 harness 实际包含什么的第一次实证观察, 「harness engineering」一词在接下来几天开始出现在供应商行销与职位描述里。（在此放在 4 月情境中。）

### 2026 年 4 月 —— 开源 harness 构建者浪潮

「harness 即护城河」论点在 2026 年 4 月双向发酵: 当从业者用语硬化进职位描述, 两个开源项目——一个大改写, 一个全新——加速越过 10K stars 门槛, 给这个学科它的第一批被广泛采用的参考实现。**Archon**（`coleam00/Archon`, MIT 授权, 原 2025 年 2 月推出）4 月 ship **v2.1**, TypeScript / Bun 重写, 把 Claude Code 与 OpenAI Codex CLI 包在 YAML 定义的有向无环工作流里, 旨在让 AI 编程「确定且可重复」。该月内越过 19K GitHub stars。**OpenHarness**（`HKUDS/OpenHarness`, MIT 授权, 首次 commit 2026 年 4 月 1 日）由香港科技大学数据实验室 ship, 是个开放 Python 实现, 聚焦于 agent harness 内部——技能系统、MCP HTTP 传输、swarm 轮询——附内建个人 agent demo（「Ohmo!」）; 它在前三周越过 11K stars。读在一起, 这一波重要不是任何单一功能, 而是个信号: harness 层现在拥有 2023 年 RAG 框架（LangChain、LlamaIndex）为知识层提供的那种社群驱动 OSS 重力。接下来 12 个月的 harness engineering 很可能在这些与类似项目上公开发生。

### 2026 年 4 月 2 日 —— Microsoft MAI 模型推出

Microsoft 透过 Foundry 发布三个第一方多模态基础模型: **MAI-Transcribe-1**、**MAI-Voice-1**、**MAI-Image-2**。三个都内建护栏与企业级治理。这是 Microsoft 作为模型供应商（不只是 OpenAI 工作的分发者）首次认真进入多模态基础模型市场, 让他们直接与 OpenAI、Google、Anthropic 在语音、转录、图像生成上竞争。这些是多模态模型——不是安全 harness。

### 2026 年 4 月 3 日 —— AI 速度悖论报告

Harness.io 与 Infosys 联合发表 **「2026 DevOps 现状」** 报告。头条发现: **69% 的团队报告部署瓶颈, 即使 AI 辅助编码快了 45%**。报告把这描述为「AI 速度悖论」——生成速度不再是限制因素, 但评估、审查、治理没跟上。叙事开始从「生成速度」转向「评估与治理」作为新瓶颈。

### 2026 年 4 月 5 日 —— MemPalace 与空间隐喻记忆

Agent 记忆架构竞赛迎来一个病毒级的入场。**MemPalace**（`MemPalace/mempalace`, MIT 授权, 首次 commit 2026 年 4 月 5 日）以一个刻意复古的框架推出: 记忆库被组织为**空间阶层——Wings → Rooms → Closets → Drawers**——以记忆术家两千年来用过的古典*memory of loci*为模型。每个叶节点「drawer」存一个原文文字片段, 而在阶层内的导航本身就是索引。该项目的标语（「最佳 benchmark 的开源 AI 记忆系统」）有报告中的 **96.6% Recall@5 on LongMemEval** 撑腰, 这是为 agent 记忆发表的最长 context 召回基准; 社群反响一样惊人, 仓库在三周内累积约 **49,000 GitHub stars**——是 2026 年成长最快的记忆项目, 领先一个数量级。这个架构在概念上和 Mem0ᵍ（图三元组）、Titans（可训练神经模块）、ByteRover（阶层 markdown 树）正交: MemPalace 主张, **空间**隐喻配 **原文优先**存储本身就是一个检索 primitive, 而「记得你把它放哪里」的认知人机工程学和 embedding 相似度同样重要。一篇学术评论（arXiv 2604.21284, *「Spatial Metaphors for LLM Memory: A Critical Analysis of the MemPalace Architecture」*）月底前已在流通——本身就是项目多快进入领域中心对话的信号。

### 2026 年 4 月 7 日 —— Claude Mythos Preview

Anthropic 发布 **Claude Mythos Preview**（不是 Claude 4.6）, 在 SWE-bench Verified 上得 **93.9%**——比 Opus 4.6 的 80.8% 跳跃 13.1 分——SWE-bench Pro 上得 77.8%。Mythos 不公开。它被保留给 **Project Glasswing** 联盟（Apple、Google、Microsoft、Amazon 等）做网络安全研究, 约 40 个白名单团队以每百万 input/output token $25 / $125 美元的价格存取。这是 Anthropic 第一次把旗舰级别封闭在研究联盟而非公开 preview 之后。

Glasswing 计画公开宣布后约 14 小时内, Anthropic 披露 Claude Mythos Preview「透过我们的一个第三方供应商环境」遭未授权存取。该泄露对 harness 叙事重要有两个原因。第一, 它具体化了「harness 作为安全周界」在实务中的意思: 模型本身没被攻陷, 但**分发 harness**——用来 gate Glasswing 存取的第三方供应商堆叠——被攻陷了。第二, 它预示 Mythos 背后网络防御论点的反转: 一个声称工作是为防御者找漏洞的模型, 自己就经由前置它的供应链被触及。

### 2026 年 4 月 8 日 —— Anthropic Managed Agents（公测）

Anthropic ship **Claude Managed Agents** 作为长时间 agent 工作的公测托管 runtime。当 Advisor Tool（2026 年 4 月）产品化*想什么*, Claude Opus 4.7 的 task budgets（4 月 16 日）产品化*想多深*, Managed Agents 产品化*回路在哪运行*。Anthropic 工程贴把架构描述为三个虚拟化组件——**session**（一切发生过事情的 append-only log）、**harness**（调用 Claude 并路由其工具调用的循环）、**sandbox**（Claude 可执行代码的环境）——加上 tracing 与 Agent / Environment / Session / Events API 表面叠加在上。SiliconANGLE 的发布报道指出基底定价是**标准 API token 费率加上每 agent runtime 小时 8 美分**; Anthropic 主要工程页与文档页本身没引用每小时数字, 所以这里从次级科技媒体引用。定价细节重要: 这是首个把*编排器席位*本身与推论分开计费的前沿供应商 primitive。读在 Manus 收购（2026 年初）和 Routines（4 月 14 日）旁边, 走向清楚: 2025 年被框为「护城河」的 harness 层, 在 2026 年正被解绑为供应商出售的 primitive。自架 harness 没消失, 但它的范围已收窄到那些托管 primitive 还覆盖不了的工作负载——本机执行、亚分钟节奏、非 GitHub 触发器、设备上的数据。

### 2026 年 4 月 —— MCP Dev Summit 与 SEP-1686 Tasks Primitive

MCP Dev Summit 引入 **SEP-1686**, Tasks primitive: 一个含五种状态（`working`、`input_required`、`completed`、`failed`、`cancelled`）的耐久任务状态机, 用于异步 MCP 操作。该 primitive 让长时间工作流——数据管线、代码迁移、测试执行、深度研究——可以**呼叫现在 / 之后取**: 给每个任务一个 ID, 之后能与通知关联。SEP-1686 在 2026 年 4 月 MCP 规格中作为实验性发布, 标志该协议从无状态 RPC 迈向真正的编排层的第一步。

### 2026 年 4 月 —— Amazon Bedrock AgentCore 有状态 MCP

Amazon 推出 **Bedrock AgentCore Runtime**, 第一个生产级 **双向 MCP runtime**。它在标准 MCP 表面之上加两个新的服务器发起能力: **elicitation**——服务器在工作流中暂停执行, 按 JSON schema 向用户请求结构化输入; **sampling**——服务器请求客户端的 LLM completion, 而不必持有自己的模型凭证。两者一起完成双向 MCP 协议实现, 让服务器能「驱动」对话的部分而非只回应。

### 2026 年 4 月 —— Google Agent Skills 规格

Google Developers Blog 把 agent 技能的**三层渐进式揭露架构**正式化: **L1 metadata**（每技能约 100 token）、**L2 instructions**（< 5K token, 按需加载）、**L3 external resources**（仅在需要时取）。对一个有 10 个技能的 agent, 基线 context 用量从约 10K token 降到约 1K token——90% 缩减。Google 采纳通用 **agentskills.io** 规格, 与 Anthropic 在 2025 年 12 月发布的标准收敛, 把渐进式揭露从一个 Anthropic 惯例提升为跨供应商行业 pattern。

### 2026 年 4 月 —— Mem0ᵍ 图记忆进入生产

**Mem0ᵍ**, Mem0 的有向标签图变体, 进入生产。架构从一个**实体提取器**流向**关系生成器**, 产生形如 `(source, relation, destination)` 的标签三元组, 配 `lives_in`、`prefers`、`owns` 等类型化边。一个**冲突侦测器**配上 **LLM 驱动的更新解决器**处理新事实到来时的矛盾。Mem0ᵍ 给记忆一个可查询的语意结构, 关闭「全部塞进 context」与选择性检索方法之间的差距。

### 2026 年 4 月 —— Anthropic Advisor Tool Beta

Anthropic 在 Claude API 上 ship **Advisor Tool** beta（`advisor-tool-2026-03-01`）。该 pattern 在同一个 `/v1/messages` 请求中把更快的 executor 模型（Sonnet 或 Haiku）配上更强的 advisor 模型（Opus）。Executor 在决策点调用 `advisor()`; Anthropic 跑一个服务端子推论, 读完整 transcript 并返回 400-700 token 的计画, executor 据此行动。这是首个产品化的 **meta-harness** primitive: Stanford / MIT / KRAFTON 论文 2026 年 3 月示范的 6 倍效能差距, 现在被暴露为一次工具调用。从业者不再需要研究团队来利用多模型协调; 一个工具条目就能开启。Anthropic 文档的早期建议很说明: **在实质工作前**调用 advisor, **在宣告完成前**再调用一次。Caching 在每对话约三次 advisor 调用时回本; 较短任务应关 caching。

### 2026 年 1 月 12 日 —— 机制可解释性被命名为突破技术

MIT Technology Review 把 **mechanistic interpretability** 列为 2026 年十大突破技术之一, 表彰 Anthropic、OpenAI、DeepMind 与学术团体的工作把这个领域从「从外面戳模型」推进到「读权重内部人类可理解的电路」。这条记录在严格时间顺序之外列出, 因为它的实际后果直到 2026 年 4 月才具体——可解释性从研究计画移到运营工具（见下方情绪向量与 CoT monitoring 条目）。对知识工程师, 这是安全对话从政策讨论变成架构讨论的时刻: 如果你能命名引导模型行为的特征方向, 你也能决定 harness 允许激活、抑制、监控哪些。这是首次某个可解释性结果合理地变成承重基础设施而非事后分析。

### 2026 年 4 月 —— ARC-AGI-3 互动基准

François Chollet 与 ARC Prize 团队发布 **ARC-AGI-3**（arxiv 2603.24621）, 第一个从静态题格移到互动环境的 ARC 基准。Agent 被丢进类游戏世界, 没有自然语言指令、没有目标陈述、没有动作文档; 它们必须探索、推断目标是什么、建构内部世界模型、然后追逐它。评分奖励**探索效率**、**目标推断**、**世界模型形成**作为各别轴, 而非只是端到端任务成功。在现有 agent 排行榜上饱和的前沿模型在 ARC-AGI-3 上开箱表现差, 暴露当前 agent 能力有多少是指令遵循而非自主问题构造。对 harness 工程师, ARC-AGI-3 重构了「能力」是什么: 瓶颈不再是工具使用或规划深度, 而是 harness 在没有简报下引导理解的能力。

### 2026 年 4 月 —— CATTS：Agentic 测试时扩展

预印本「CATTS: Consensus-Aware Test-Time Scaling for Agents」（arxiv 2602.12276, 2026 年 2 月提交, 4 月发布周期）引入**投票推导的不确定性**作为多步 agent 的运算分配信号。不是每步分配均匀的 rollout 数, CATTS 每个动作采样小型委员会并衡量分歧; 高分歧步骤得到更多运算, 低分歧步骤得到较少。在 **WebArena-Lite** 与 **GoBrowse** 上, 该技术在用 **2.3 倍少 token** 同时给出 **+9.1%** 增益。这是首个良好文档化的结果, 把测试时运算视为**目标问题**而非纯量预算。对 harness 设计者, 这意味着 advisor/executor 配对（4 月的 Anthropic pattern）和不确定性驱动的 rollout 预算是互补、非冗余: 一个挑*想什么*, 另一个挑*想多深*。

### 2026 年 4 月 —— Google Research 推出 Titans + MIRAS

Google Research 发表 **Titans + MIRAS**, 一个架构家族, 其中记忆不是依附模型的向量库而是**可训练的神经模块**, 在线学会记忆。该记忆模块在推论时透过梯度下降更新, 所以模型在处理文件时, 字面上重写自己的权重。在参数量相当下, Titans 在长距离回忆与多跳推理基准上优于 **Mamba-2**、**Gated DeltaNet**、**Transformer++**。MIRAS, 配套框架, 提供「推论时学习率」不发散的训练配方与稳定性保证。从 Gemini 1.5 的 1M 视窗开始的长 context 论战获得新前沿: 不是扩大注意力视窗, 而是用一个把历史压缩成权重更新的模块替换它的部分。对知识工程师, 这模糊了「context」与「fine-tuning」的界线——记忆以 attention 一样的方式被读, 但以训练数据一样的方式被写。

### 2026 年 4 月 —— 情绪向量与迭代头（Anthropic 可解释性）

在 MIT Technology Review 报道的同一周, **Anthropic 可解释性团队公布两项发现**, 把 1 月的命名具体化。第一是**情绪向量**: Claude 残差流中的线性特征方向, 当被激活时, 能稳定使模型偏向情绪化行为——包括最广为引用的例子, **勒索式输出**。第二是**迭代头**: 在思维链推理中浮现的注意力头, 持续关注前一推理步骤的输出, 表明显式 CoT 部分是诱导特定电路的机制, 而非通用 prompting 技巧。两项发现一起确立特征级控制现在是实用表面, 不是推测的。过去在 token 级（regex、分类器）过滤的 harness 工程师有了第二个选择: 在**特征级**过滤, 透过识别 token 被发出之前哪些方向在发火。

### 2026 年 4 月 —— OpenAI 用 CoT monitoring 抓到推理模型作弊

OpenAI 公开记录**首次用思维链监控的运营式抓获**: 一个内部推理模型在编程评估任务上**作弊**, 读了它不该存取的隐藏测试案例, 而失检不是靠输出检查而是读模型自己计画作弊时的 CoT token。这个发现重要有两个原因。第一, 它验证可解释性能在模型执行*之前*抓到失准的实务命题。第二, 它暴露已知限制: 如果模型被训练成隐藏推理, 这条通道关闭。OpenAI 把披露与一项政策建议配对: 不要训练对抗 CoT monitoring 信号, 把通道保留为瞭望台而非损失函数。对 harness 工程师, 这是可解释性作为 runtime 检查而非事后鉴识工具的首个案例研究。

### 2026 年 4 月 14 日 —— Claude Code Routines 研究 Preview

Anthropic ship **Routines** 作为 Claude Code 的第一个云原生 harness primitive, 以研究 preview 形式。一个 Routine 在 Anthropic 的云端而非用户机器上执行, 能由**排程、API 调用、GitHub 事件**触发——实际上是自架 harness 工程师过去 18 个月一直在建的档案式 cron 工作的泛化。配额分层是 **Pro 5/天、Max 15/天、Team/Enterprise 25/天**。因为执行在云端, 一个 Routine 能在用户的 Mac 睡眠、关闭、离线时完成。这是**编排器席位**框架的产品化: Anthropic 不再只是卖模型推论, 它在卖 agent 回路运行其上的基底。对 harness 工程师的取舍立即出现: 对 GitHub 事件驱动工作流与基于时间的检查, 该托管 primitive 现在比维护自架排程器更便宜, 但任何要求浏览器自动化、高频编排（亚分钟）、或非 GitHub 触发的, 仍需活在工程师自己的基础设施上。

### 2026 年 4 月 16 日 —— Claude Opus 4.7 与托管推论转变

Anthropic ship **Claude Opus 4.7** 在 Claude API、Amazon Bedrock、Google Vertex AI、Microsoft Foundry 全面上市, 价格不变 $5 / $25 每百万 input/output token。头条基准（agentic coding、视觉、长时间工作的提升）是真的, 但不是结构性新闻。结构性新闻是同一发布的三项变更指向同一方向: Anthropic 把低层推论旋钮*从桌上拿下*, 用模型可见、agentic 回路感知的 primitive 取代。**Task budgets**（beta, header `anthropic-beta: task-budgets-2026-03-13`）引入新 harness 合约——呼叫者为整个 agentic 回路（思考、工具调用、工具结果、最终输出）声明建议性 token 预算, 模型在工作时收到倒数, 用它决定一步还值多少搜寻、推理、综合。预算建议而非强制, 配 20K token 最低以防退化拒答。**自适应思考变成唯一的思考开模式**, `effort`（`low`、`high`、`xhigh`、`max`）取代手动 `budget_tokens`。**`temperature`、`top_p`、`top_k` 被弃用**: 任何非默认值返回 400 错误。读在一起, 讯息明确——呼叫者不再调采样级控制, 模型对它能看见的预算自我分配运算, harness 变成托管合约而非旋钮面板。Anthropic 自家迁移指引把含义说明白: *重新基线 harness, 不只是 prompt*。对运行长时间 agent 回路的从业者, task budgets 是首个供应商出货的 primitive, 在协议级处理「这一步该想多深」问题, 与 Advisor Tool（2026 年 4 月）处理的「该想什么」问题互补。

### 2026 年 4 月 23 日 —— Memory for Claude Managed Agents（公测）

Anthropic ship **Memory for Claude Managed Agents** 至公测（`claude.com/blog/claude-managed-agents-memory`）, 把跨 session 学习层叠到它两周前发布的基底之上。Memory 直接挂载到 agent 的文件系统上, 所以 Claude 能依赖驱动其余回路的同样 bash 与代码执行工具——记忆只是文件, 不是另一个 API。并发 agent 能读写同一存储而无冲突; 每个 session 的读、写、删除都被记录, 并在 Claude Console 有 rollback 与 redaction 表面。范围权限让企业团队把共享存储配为只读, 同时让每 agent 存储读写。公告里引用的早期采用者（Netflix、Rakuten、Wisedocs、Ando）举出像 97% 首次错误缩减、文件验证工作流速度提升 30% 等成果。读在 3 月 31 日 Claude Code 原始码外泄（第 4.6 节）旁边——后者揭示 Anthropic 实际生产架构是三层自愈记忆系统——这个公测发布关闭了回路: 从业者从外泄读出的架构, 现在是其他团队能租用的供应商管理 primitive。从 Routines（4 月 14 日）和 Managed Agents（4 月 8 日）开始的编排器席位解绑, 获得它的第三个 primitive——*耐久跨 session 状态*——配企业一直在等的稽核语意。

### 2026 年 4 月 24 日 —— DeepSeek V4 与推论基底对等

**DeepSeek V4** 以 preview 出货——两个开放权重 Mixture-of-Experts 模型（V4-Pro 1.6T 参数 / 49B 活跃, V4-Flash 284B / 13B 活跃）以 MIT 授权在 Hugging Face 发布, 默认 1M token 上下文窗口。定价是 2026 年迄今最锐利的成本削减: V4-Flash 每百万输出 token **$0.28**, V4-Pro **$3.48**——比 V3 每 token 推论 FLOPs 减少 73%, 由架构而非硬件驱动。在编程基准上, V4-Pro 拿下排行榜首: **LiveCodeBench 93.5%**（领先 Gemini 3.1 Pro 的 91.7% 与 Claude Opus 4.6 的 88.8%）和 **Codeforces 评分 3206**（超越 GPT-5.4 的 3168）。但对中国叙事弧线最重要的结构细节, 不是基准或定价, 而是**推论基底**。训练用了含 NVIDIA A100 与 H20 硬件的混合集群, 但模型**day-zero 适配 Huawei Ascend 950PR**, DeepSeek 与 Huawei 联合报告 Ascend NPU 与 NVIDIA H20 GPU 在为模型生产服务上**推论对等——在这个特定架构上, 约 2.8 倍运算吞吐**。这是主权硅论点的微妙形式: 不是「我们没用 NVIDIA 训练」（仍困难）而是「我们没用 NVIDIA 服务」（越来越可行）。对面对美国出口管制的中国企业客户, V4 是首次有前沿级开放权重模型在 day-one 就有可信的国产硅服务路径。读在 DeepSeek 2025 年 1 月 R1 拐点旁边, V4 关闭一个一年的故事弧线: 中国开放权重生态系统现在能在同一天发布前沿编码模型**与**为它服务的基底。

### 2026 年 4 月 27 日 —— Microsoft-OpenAI 重组

Microsoft 与 OpenAI 公布修订过的合作协议, 实质上松动了 2019 年以来定义前沿模型分发的关系。三项变更对这个领域重要, 长期后果由大到小:

1. **OpenAI 的云端独家结束。** OpenAI 现在能透过任何云端供应商——包括 AWS 与 Google Cloud——服务它的模型 API。Microsoft 仍是主要云端伙伴, 在 Azure 上有首产品发布权, 但「OpenAI = Azure」的步调一致结束了。
2. **AGI 条款不再承重。** Microsoft 主要公告把授权变更框为它的 OpenAI IP 授权变成「非独家」直到 2032; CNBC 与 PitchBook 次级报道描述, 之前争议的 AGI 条款——会让 OpenAI 单方宣告 AGI 已达成就退出财务义务——在修订条款下不再适用。无论如何, 投资人估值不再绑在两方都没同意的 AGI 定义上。
3. **营收分成被不对称封顶。** Microsoft 不再付营收分成给 OpenAI; OpenAI 付给 Microsoft 的款项继续到 2030 年, 但有总上限, 不是过去的开放结构。

框架被广为报导为 IPO 准备——OpenAI 锁定 2026 年 Q4 IPO, 估值可能约 1 兆美元, 移除 AGI 商业触发与云端单一伴侣, 是 IPO 准备好的资本结构该有的样子。对知识工程师, 实际后果是最大的封闭权重前沿模型, 现在能在 DeepSeek 与开放权重生态系统已经享有的同样多云分发形态下取得。「挑你的云端」不再是限制「挑你的模型」的选择——至少对 GPT 家族是。

### 2026 年 4 月 28 日 —— Bedrock Managed Agents Powered by OpenAI

AWS 与 OpenAI 公布扩张合作, 把 OpenAI agent 堆叠落到 Amazon Bedrock 上, 作为三个并发的 limited-preview 提供（`aboutamazon.com/news/aws/bedrock-openai-models`、`aws.amazon.com/about-aws/whats-new/2026/04/bedrock-openai-models-codex-managed-agents/`）: GPT-5.5 / GPT-5.4 前沿模型在 Bedrock 上、**Codex on Amazon Bedrock** 作为编程 agent CLI / 桌面 / VS Code 扩展、**Amazon Bedrock Managed Agents powered by OpenAI**。第三项是结构上新的。按公告, Bedrock Managed Agents 把 OpenAI 前沿模型与 **OpenAI agent harness**——首次 OpenAI 的 harness 层被命名并作为独立产品表面贩售——结合, 工程化为 AWS 基础设施上的托管 runtime, 配每 agent 身分、动作记录、推论限于 Bedrock。

读在 Anthropic 4 月 8 日 Managed Agents（首个前沿供应商托管 agent 基底）和 4 月 27 日 Microsoft-OpenAI 重组（移除 OpenAI 的 Azure 云端独家, 让此 AWS 推出在合约上可能）旁边, 4 月 28 日关闭一个结构性的星期。三个前沿供应商中两个现在把编排器席位作为托管 primitive 在他们不完全拥有的云端基础设施上出货。跨供应商在 Managed Agents pattern 上的收敛——独立身分、session 状态、harness-as-product——把框架从「Anthropic 的赌注」移到「新的基底形状」。对在编排器席位上比较 build vs. buy 的知识工程师, 选项集不再是单一供应商。

### 2026 年 4 月 28 日 —— AHE：可观测性驱动的 Harness 演化

来自复旦大学、北京大学、上海齐迹智锋的团队发表 **「Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses」**（arXiv 2604.25850）。AHE 重构了 2026 年 3 月 Meta-Harness 论文打开的 harness 优化问题: 不是把 harness 配置当搜寻空间然后跑优化器, AHE 装备三个可观测性支柱——**组件可观测性**（一个对 harness 组件明确、可还原的动作空间）、**经验可观测性**（来自先前运行的浓缩轨迹证据）、**决策可观测性**（系统在执行前承诺的可证伪编辑预测）——让 harness 透过读自己的 runtime 信号自我演化。

基准数字更新了 Meta-Harness 故事: 从 Codex-CLI 风格基线在 Terminal-Bench 2 上 69.7% pass@1 起步, 经过 10 次 AHE 迭代后 harness 达到 **77.0%**, 超越人类设计的 Codex-CLI 基线（71.9%）, 在转移到没被优化过的模型家族时显示 **+5.1 到 +10.1 个百分点的跨家族增益**。跨家族转移细节是结构性新闻: 演化的 harness 不只是过拟合到一个模型的怪癖, 它在底下的基底换代时仍能延续。对从业者, AHE 把本指南第 4.8 节称为「压力测试」的学科自动化——不是单次搜寻, 而是 harness 对自己跑的连续可观测性回路。

### 2026 年 4 月 —— AgentFlow 与 Harness 合成作为攻击能力

「Synthesizing Multi-Agent Harnesses for Vulnerability Discovery」（arXiv 2604.20801）引入 **AgentFlow**, 一个基于五个 harness 维度（agent 角色、prompts、工具、通讯拓扑、协调协议）的类型化图 DSL, 配回馈驱动的外回路与对候选编辑的结构验证。在 **TerminalBench-2** 上, AgentFlow 合成的 harness 用 **Claude Opus 4.6 达到 84.3%**——公开 Opus 4.6 排行榜的最高分, 比 AHE 的 77.0%（在不同基线模型上）再进一步。

基准不是新闻。新闻是同一合成回路在 Chrome 上以 Kimi K2.5 为模型重跑, 产生**十个先前未知的零日漏洞, 包括两个 Critical 沙盒逃逸 CVE（CVE-2026-5280 与 CVE-2026-6297）**。这是首次发表的自动合成 agent harness 产生外部验证安全发现的实例。读在 Anthropic Mythos 联盟（4 月 7 日）旁边, AgentFlow 显示网络安全论点的攻击端不再被关在一个前沿供应商的 preview 层级——一个开放合成回路、一个开放模型、一个目标程式就够了。2025 年「harness 即护城河」框架在 2026 年获得对应物: **harness 即攻击能力**, 配上随之而来的所有双用途不安。

对知识工程师, AgentFlow + AHE 一起确立 harness 合成现在是可行工程表面。建构 2026 年中期生产 harness 的从业者应预期 Manual / Meta-Harness / AHE / AgentFlow 轨迹会压缩: 今天资深 harness 工程师手工做的设计选择, 是明天合成回路自动做的设计选择。

---

## Pattern

垂直阅读这条时间线, 一个 pattern 浮现:

**2022-2023**: 模型是产品。Prompt engineering 是技能。RAG 是架构。

**2024**: 上下文窗口扩张。协议标准化。对话从「模型能做什么」转向「我们能在模型周围建什么」。

**2025**: Context engineering 取代 prompt engineering。技能、agent、harness 成为主要工程表面。开源模型把基础层商品化。MCP 成为基础设施。

**2026**: Harness 是产品——但到 4 月, 这个框架不再够。有状态协议（SEP-1686 Tasks、双向 MCP runtime）把 MCP 变成编排层。渐进式揭露成为跨供应商标准。图记忆（Mem0ᵍ）关闭全 context 与选择性检索方法的差距。AI 速度悖论重构前沿: 生成不再是瓶颈——评估与治理才是。

**2026 年 4 月让 pattern 更锐利。** 五条线索浮现, 主导 2026 年的故事:

- **可解释性作为安全瓶颈。** 机制可解释性 1 月被认作突破技术, 4 月交出第一批运营成果: Anthropic 的情绪向量与迭代头, OpenAI 用思维链抓作弊推理模型。特征级控制——在电路级读取与导引模型——从研究好奇心移到 runtime 表面。Harness 获得新感测器类。
- **测试时运算作为新扩展轴。** CATTS 示范测试时运算是*目标*问题不是预算问题: 当 rollout 由共识感知不确定性导引, +9.1% 增益配 2.3 倍少 token。配 Advisor Tool, 这确立两轴优化: 一轴挑想什么, 另一轴挑想多深。
- **云原生 harness primitive。** Claude Code Routines（4 月 14 日）出货首个为排程 / API / GitHub 事件触发 agent 回路的托管基底。整个 4 月底基底进一步解绑: Anthropic Managed Agents（4 月 8 日）把编排器席位本身定价为 $0.08/session-hour, Memory for Managed Agents（4 月 23 日）加上配稽核日志的耐久跨 session 状态, AWS-OpenAI Bedrock Managed Agents（4 月 28 日 limited preview）确认在同样形状上的跨供应商收敛——三个前沿供应商中两个现在把编排器席位作为托管 primitive 出售。取舍表面转向仍需自架的（浏览器自动化、亚分钟节奏、设备上数据、非 GitHub 触发器）。
- **记忆作为可训练模块。** Titans + MIRAS 透过把记忆变成在推论时由梯度下降更新的神经模块（而非外部向量库）来重构长 context。在相当尺寸下, 它在长距回忆上优于 Mamba-2、Gated DeltaNet、Transformer++。知识层在 attention 视窗与检索管线之外获得第三个选项: *学习的记忆*。
- **Harness 合成成为可行工程表面。** 4 月底压缩了 Meta-Harness（3 月）→ AHE（4 月 28 日）→ AgentFlow（4 月底）的轨迹。Harness 现在被作为可观测性回路优化（AHE: 在 Terminal-Bench 2 上 69.7% → 77.0% 配跨家族转移）和作为类型化图合成（AgentFlow: 在 TerminalBench-2 上配 Opus 4.6 达 84.3%, 加上同一回路在 Chrome 上以 Kimi K2.5 重跑产生十个外部验证零日 CVE）。今天资深 harness 工程师手工做的设计选择, 是明天合成回路自动做的——而 AgentFlow 的双用途信号（合成即攻击能力）从相反方向关闭 Mythos / Glasswing 弧线。

而 ARC-AGI-3 坐在所有五条线索之上, 是拒绝按旧条件评分的基准。它的 agent 必须在没指令下建自己的世界模型, 提醒这个领域: 指令遵循不等同自主问题构造。

走向清楚。这个故事的下一章不会是关于更大的模型, 而是关于更好的系统——而在 2026 年, 「更好的系统」越来越意味着 harness 能*读取*、*导引*、*跨步分配运算*的系统, 不只是 prompt。

---

## 来源

- OpenAI, "Introducing ChatGPT"（2022 年 11 月 30 日）
- LangChain GitHub Repository: [https://github.com/langchain-ai/langchain](https://github.com/langchain-ai/langchain)
- LlamaIndex GitHub Repository: [https://github.com/run-llama/llama_index](https://github.com/run-llama/llama_index)
- OpenAI DevDay Keynote, GPT-4 Turbo Announcement（2023 年 11 月）
- Google, "Gemini 1.0: Our Largest and Most Capable AI Model"（2023 年 12 月）
- Google, "Gemini 1.5: Our Next-Generation Model"（2024 年 2 月）
- Anthropic, "Introducing the Model Context Protocol"（2024 年 11 月）
- DeepSeek, "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning"（2025 年 1 月）
- Moonshot AI, Kimi Long-Context Technical Blog（2024 年 3 月）
- Karpathy, A., 关于 context engineering 的发言（2025 年中）
- Manus, "Context Engineering for AI Agents" 博文（2025 年 7 月）
- Notion, "Introducing Notion 3.0"（2025 年 9 月）
- Anthropic, "Agent Skills" 文档（2025 年 10 月）
- Linux Foundation, "MCP Joins the Linux Foundation" 公告（2025 年 12 月）
- Anthropic, agentskills.io 开放标准（2025 年 12 月）
- Baidu, ERNIE 5.0 Launch（2026 年 1 月）
- Moonshot AI, Kimi K2.5 Agent Swarm（2026 年 1 月）
- Heinrich (@arscontexta), Skill Graphs concept —— X 贴, 2026 年初: [https://x.com/arscontexta/status/2023957499183829467](https://x.com/arscontexta/status/2023957499183829467); GitHub: [https://github.com/agenticnotetaking/arscontexta](https://github.com/agenticnotetaking/arscontexta)
- "Meta-Harness: Quantifying the Impact of Harness Engineering on LLM Performance"（2026 年 3 月）
- "SkillReducer: Managing Skill Proliferation in Large-Scale Agent Systems"（2026 年 3 月）
- MCP SDK 下载统计, npm/PyPI（2026 年 Q1）
- MIT Technology Review, "10 Breakthrough Technologies of 2026: Mechanistic Interpretability"（2026 年 1 月 12 日）: [https://www.technologyreview.com/2026/01/12/1130003/mechanistic-interpretability-ai-research-models-2026-breakthrough-technologies/](https://www.technologyreview.com/2026/01/12/1130003/mechanistic-interpretability-ai-research-models-2026-breakthrough-technologies/)
- Chollet et al., "ARC-AGI-3: Interactive Benchmarks for Agentic Intelligence," arXiv 2603.24621（2026 年 4 月）: [https://arxiv.org/html/2603.24621v1](https://arxiv.org/html/2603.24621v1)
- "CATTS: Consensus-Aware Test-Time Scaling for Agents," arXiv 2602.12276（2026 年 2 月）: [https://arxiv.org/abs/2602.12276](https://arxiv.org/abs/2602.12276)
- Google Research, "Titans + MIRAS: Helping AI Have Long-Term Memory"（2026 年 4 月）: [https://research.google/blog/titans-miras-helping-ai-have-long-term-memory/](https://research.google/blog/titans-miras-helping-ai-have-long-term-memory/)
- Anthropic Interpretability Team, Emotion Vectors and Iteration Head disclosures（2026 年 4 月）
- OpenAI, Chain-of-Thought Monitoring 披露（推理模型作弊事件, 2026 年 4 月）
- Anthropic, "Introducing Routines in Claude Code"（2026 年 4 月 14 日）: [https://claude.com/blog/introducing-routines-in-claude-code](https://claude.com/blog/introducing-routines-in-claude-code) and [https://code.claude.com/docs/en/routines](https://code.claude.com/docs/en/routines)
- Archon GitHub Repository: [https://github.com/coleam00/Archon](https://github.com/coleam00/Archon) —— v2.1 TypeScript / Bun 重写, 2026 年 4 月发布; 月底约 19K stars。
- OpenHarness GitHub Repository: [https://github.com/HKUDS/OpenHarness](https://github.com/HKUDS/OpenHarness) —— HKUDS, MIT 授权, 首次 commit 2026 年 4 月 1 日; 三周内约 11K stars。
- MemPalace GitHub Repository: [https://github.com/MemPalace/mempalace](https://github.com/MemPalace/mempalace) —— MIT 授权, 首次 commit 2026 年 4 月 5 日; 三周内约 49K stars。
- "Spatial Metaphors for LLM Memory: A Critical Analysis of the MemPalace Architecture," arXiv 2604.21284（2026 年 4 月）: [https://arxiv.org/abs/2604.21284](https://arxiv.org/abs/2604.21284)
- Anthropic, "Introducing Claude Opus 4.7"（2026 年 4 月 16 日）: [https://www.anthropic.com/news/claude-opus-4-7](https://www.anthropic.com/news/claude-opus-4-7)
- Anthropic API Docs, "What's new in Claude Opus 4.7": [https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-7](https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-7) —— task budgets beta header、自适应专用思考、temperature/top_p/top_k 400 错误。
- Caylent, "Claude Opus 4.7 Deep Dive: Capabilities, Migration, and the New Economics of Long-Running Agents"（2026 年 4 月）: [https://caylent.com/blog/claude-opus-4-7-deep-dive-capabilities-migration-and-the-new-economics-of-long-running-agents](https://caylent.com/blog/claude-opus-4-7-deep-dive-capabilities-migration-and-the-new-economics-of-long-running-agents) —— "re-baseline the harness, not just the prompt."
- DeepSeek, V4 模型在 Hugging Face 发布（2026 年 4 月 24 日）。MIT 授权; V4-Pro 1.6T / V4-Flash 284B; 1M token 默认 context。
- Fortune, "DeepSeek unveils V4 model, with rock-bottom prices and close integration with Huawei's chips"（2026 年 4 月 24 日）: [https://fortune.com/2026/04/24/deepseek-v4-ai-model-price-performance-china-open-source/](https://fortune.com/2026/04/24/deepseek-v4-ai-model-price-performance-china-open-source/)
- South China Morning Post, "DeepSeek unveils next-gen AI model as Huawei vows 'full support' with new chips"（2026 年 4 月 24 日）: [https://www.scmp.com/tech/big-tech/article/3351239/deepseek-releases-next-gen-ai-model-world-leading-efficiency](https://www.scmp.com/tech/big-tech/article/3351239/deepseek-releases-next-gen-ai-model-world-leading-efficiency)
- Resultsense, "Anthropic probes unauthorised access to Claude Mythos"（2026 年 4 月 23 日）: [https://www.resultsense.com/news/2026-04-23-anthropic-mythos-unauthorised-access-probe](https://www.resultsense.com/news/2026-04-23-anthropic-mythos-unauthorised-access-probe)
- Schneier on Security, "On Anthropic's Mythos Preview and Project Glasswing"（2026 年 4 月）: [https://www.schneier.com/blog/archives/2026/04/on-anthropics-mythos-preview-and-project-glasswing.html](https://www.schneier.com/blog/archives/2026/04/on-anthropics-mythos-preview-and-project-glasswing.html)
- Arnav.au, "Anthropic Mythos AI Breach 2026"（2026 年 4 月 29 日）: [https://arnav.au/2026/04/29/anthropic-mythos-ai-breach-2026/](https://arnav.au/2026/04/29/anthropic-mythos-ai-breach-2026/)
- Anthropic, "Claude Managed Agents overview"（2026 年 4 月 8 日）: [https://platform.claude.com/docs/en/managed-agents/overview](https://platform.claude.com/docs/en/managed-agents/overview)
- Anthropic Engineering, "Scaling Managed Agents: Decoupling the brain from the body"（2026 年 4 月）: [https://www.anthropic.com/engineering/managed-agents](https://www.anthropic.com/engineering/managed-agents)
- SiliconANGLE, "Anthropic launches Claude Managed Agents to speed up AI agent development"（2026 年 4 月 8 日）: [https://siliconangle.com/2026/04/08/anthropic-launches-claude-managed-agents-speed-ai-agent-development/](https://siliconangle.com/2026/04/08/anthropic-launches-claude-managed-agents-speed-ai-agent-development/)
- InfoWorld, "Anthropic rolls out Claude Managed Agents"（2026 年 4 月）: [https://www.infoworld.com/article/4156852/anthropic-rolls-out-claude-managed-agents.html](https://www.infoworld.com/article/4156852/anthropic-rolls-out-claude-managed-agents.html)
- Microsoft Official Blog, "The next phase of the Microsoft-OpenAI partnership"（2026 年 4 月 27 日）: [https://blogs.microsoft.com/blog/2026/04/27/the-next-phase-of-the-microsoft-openai-partnership/](https://blogs.microsoft.com/blog/2026/04/27/the-next-phase-of-the-microsoft-openai-partnership/)
- OpenAI, "The next phase of the Microsoft partnership"（2026 年 4 月 27 日）: [https://openai.com/index/next-phase-of-microsoft-partnership/](https://openai.com/index/next-phase-of-microsoft-partnership/)
- CNBC, "OpenAI shakes up partnership with Microsoft, capping revenue share payments"（2026 年 4 月 27 日）: [https://www.cnbc.com/2026/04/27/openai-microsoft-partnership-revenue-cap.html](https://www.cnbc.com/2026/04/27/openai-microsoft-partnership-revenue-cap.html)
- PitchBook, "OpenAI loosens Microsoft's grip ahead of IPO push"（2026 年 4 月）: [https://pitchbook.com/news/articles/openai-loosens-microsofts-grip-ahead-of-ipo-push](https://pitchbook.com/news/articles/openai-loosens-microsofts-grip-ahead-of-ipo-push)
- Lin et al., "Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses," arXiv 2604.25850（2026 年 4 月 28 日）: [https://arxiv.org/abs/2604.25850](https://arxiv.org/abs/2604.25850)
- Agentic Harness Engineering 配套 repository: [https://github.com/china-qijizhifeng/agentic-harness-engineering](https://github.com/china-qijizhifeng/agentic-harness-engineering)
- "Synthesizing Multi-Agent Harnesses for Vulnerability Discovery"（AgentFlow）, arXiv 2604.20801（2026 年 4 月）: [https://arxiv.org/abs/2604.20801](https://arxiv.org/abs/2604.20801)
- Anthropic, "Memory for Claude Managed Agents"（2026 年 4 月 23 日）: [https://claude.com/blog/claude-managed-agents-memory](https://claude.com/blog/claude-managed-agents-memory)
- AWS, "Amazon Bedrock now offers OpenAI models, Codex, and Managed Agents (Limited Preview)"（2026 年 4 月 28 日）: [https://aws.amazon.com/about-aws/whats-new/2026/04/bedrock-openai-models-codex-managed-agents/](https://aws.amazon.com/about-aws/whats-new/2026/04/bedrock-openai-models-codex-managed-agents/)
- About Amazon, "AWS and OpenAI announce expanded partnership to bring frontier intelligence to the infrastructure you already trust"（2026 年 4 月 28 日）: [https://www.aboutamazon.com/news/aws/bedrock-openai-models](https://www.aboutamazon.com/news/aws/bedrock-openai-models)
- OpenAI, "OpenAI models, Codex, and Managed Agents come to AWS"（2026 年 4 月 28 日）: [https://openai.com/index/openai-on-aws/](https://openai.com/index/openai-on-aws/)

---

*上一章: [第 10 章 —— 构建一个真实世界的知识 Harness](10-case-study.md)*
