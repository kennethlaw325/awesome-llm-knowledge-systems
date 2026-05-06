# 第 4 章：Harness Engineering —— 围绕模型构建操作系统

> **一句话总结：** Harness 是 AI 模型周围的一切——让它真正可用的规则、工具、安全检查、工作流程。
>
> **为什么重要：** AI 模型像一具强大引擎。没有底盘、方向盘、煞车, 它就没用。Harness 是把原始 AI 变成产品的东西。

> 「Harness 中每一个组件都编码了一个关于模型自己做不到什么的假设, 而这些假设值得做压力测试。」
> —— Anthropic, "Building Effective Agents", 2025

> 「模型從來都沒有長手。」
> —— Cab, 论为什么工具使用是 harness 问题而非模型问题

Agent 不是模型。Agent 是 **模型加 harness**——围绕的 prompt、工具、记忆、控制流、评估逻辑、编排代码系统, 把原始推论变成可靠行为。模型是引擎; harness 是车辆。本章检视从业者如何设计、评估、演化那辆车。

**关于直觉的注记。** 把这件事变具体的隐喻, 对许多初学者来说是 Cab 的观察:「模型从来没有真的长出手。」当一个编程 agent 编辑文件, 编辑文件的不是模型——是 harness, 由模型作为文字返回的工具调用所触发。我们归给「AI」的每个能力, 实际上是围绕模型的 harness 的能力。把 harness 拿走, 你得到一个只能产文字的模型。把模型拿走, 你得到一个没有东西可路由的 harness。Harness engineering 是决定那条线在哪、两半如何合作的学科。

---

## 4.1 定义 Harness

Harness 是除模型权重以外的一切。它包括:

- 系统 prompt 与指令模板
- 工具定义与执行沙盒
- 记忆系统（短期、长期、情节）
- 规划与分解逻辑
- 控制流（循环、条件、重试政策）
- 评估与自我修正机制
- 安全护栏与输出验证
- Context 组装管线（第 3 章）

一个赤裸的模型 API 调用配用户讯息是个琐碎 harness。一个有规划、多步工具使用、自我评估、持续记忆的生产 agent 是复杂的。Harness engineering 的学科是在这个光谱上做有原则的决策。

## 4.2 Böckeler 分类

Birgitta Böckeler（ThoughtWorks, 2026 年 4 月）在 Martin Fowler 的 *Exploring Generative AI* 系列中, 提出了一个二轴 harness 组件分类, 已成为标准参考:

**轴 1：方向**
- **Guides（前馈）：** 在模型行动*之前*塑造行为的组件。系统 prompt、few-shot 例子、工具 schema、规划模板。它们设定轨道。
- **Sensors（回馈）：** 在模型行动*之后*评估行为并把结果回馈的组件。输出验证器、测试执行器、人工审查、自我评估 prompt。它们修正路线。

**轴 2：机制**
- **计算控制：** 确定性代码——regex 验证器、类型检查器、schema 强制、权限检查。这些是从不幻觉的硬约束。
- **推论控制：** 用来评判、路由、精炼的另一次 LLM 调用。评估模型、分类器、总结器。这些是软约束, 用精度换取灵活性。

这个分类揭示一个设计空间。大多数生产 harness 都用四个象限:

|  | 前馈（Guides） | 回馈（Sensors） |
|--|---------------|----------------|
| **计算** | 工具输入的 schema 验证、权限白名单 | 输出格式检查、测试套件执行 |
| **推论** | 规划 prompt、few-shot 路由 | 自我评估、LLM-as-judge、批评链 |

洞察是: 计算控制更便宜、更可靠但较不灵活, 而推论控制处理模糊但引入自己的失效模式。好的 harness 设计尽可能用计算控制, 把推论控制保留给真正模糊的决策。

## 4.3 OpenAI Codex：透过 Harness 规模化

社群广为引用的一个数据点描述 OpenAI 内部使用 Codex 的情况: **三位工程师加上 Codex agent 系统产出约 100 万行代码、约 1,500 个 PR**。生产力倍数主要不是关于模型质量——是关于 harness 设计。（具体数字在 2025-2026 年 OpenAI 演讲与文章中流传; 关于 Codex harness 的公开材料, 见 [openai.com/index/introducing-codex](https://openai.com/index/introducing-codex)。）

Codex harness 包括:
- 自动化 PR 分解（把大任务拆成可审查单元）
- 每个任务的沙盒执行环境
- 自动化测试生成与验证
- PR 边界的人工审查整合
- 关于 repo 结构与惯例的持续 context

教训: 在足够的 harness 成熟度下, 模型变成更大生产系统中的一个组件, 而非独立工具。Harness 处理编排、质量控制、整合——这些是 prompt engineering 怎么调都解决不了的关切。

## 4.4 IMPACT 框架

在 2020 年代中期从业者讨论中, **IMPACT 助记词**——Intent、Memory、Planning、Authority、Control flow、Tools——浮现为系统化思考 harness 设计维度的方式:

- **Intent（意图）：** 系统如何理解用户实际想要什么？包括意图分类、澄清对话、目标分解。
- **Memory（记忆）：** 系统跨回合与 session 记得什么？包括对话缓冲、向量库、结构化知识库、用户偏好系统。
- **Planning（规划）：** 系统如何把复杂任务分解成步骤？包括思维链 prompting、明确计画生成、动作空间的树搜寻。
- **Authority（权限）：** 系统被允许做什么？包括权限系统、人在回路 gate、能力边界。
- **Control Flow（控制流）：** 执行如何进行？包括顺序链、并行扇出、条件分支、含退出条件的循环、重试政策。
- **Tools（工具）：** 系统能存取什么外部能力？包括函数定义、API 整合、代码执行环境、浏览器存取。

IMPACT 作为设计清单有用。建构或审查 harness 时, 走过每个维度能浮现差距。一个工具强但权限弱的系统有安全问题。一个规划强但无记忆的系统不能从错误学习。这个框架让这些不平衡可见。

## 4.5 Meta-Harness 论文：自动化 harness 设计

Stanford、MIT、KRAFTON 联合论文（2026 年 3 月）引入 **meta-harness** 概念——一个自动优化 harness 配置的系统。

他们的关键发现: 在同一基准、同一基础模型上, 不同 harness 配置产出 **6 倍效能差距**。给定任务的最佳 harness 配置很少明显, 常常违反直觉。手动 harness 调整正在桌上留下大量效能。

Meta-harness 做法把 harness 参数（重试次数、规划深度、工具选择策略、记忆窗口大小、评估严格度）视为搜寻空间, 用自动优化找出高效能配置。系统能把 harness 适配到不同任务类型、不同模型、不同成本约束。

这个结果有深刻含义: **harness engineering 不是已知最佳实务的已解决设计问题——它是有大且不太理解搜寻空间的优化问题**。把 harness 设计视为一次性架构决策的团队, 很可能在远低于前沿的状态运行。

Meta-Harness 论文现在是快速移动一线上的一个数据点。2026 年 4 月, **AHE 论文**（「Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses」, arXiv 2604.25850, 复旦/北大/上海齐迹智锋）把这个问题从搜寻重构为*可观测性*: 不是把 harness 配置当搜寻空间然后跑优化器, AHE 装备三个可观测性支柱——组件（明确、可还原的动作空间）、经验（浓缩的轨迹证据）、决策（执行前做的可证伪编辑预测）——让 harness 透过读自己的 runtime 信号自我演化。经过 10 次 AHE 迭代, Codex-CLI 风格的基线在 Terminal-Bench 2 上 69.7% pass@1 达到 77.0%, 超越人类设计基线（71.9%）, 在转移到没被优化过的模型家族时显示 **+5.1 到 +10.1 个百分点的跨家族增益**。跨家族转移是结构性新闻: 演化的 harness 不只是过拟合到一个模型的怪癖, 它在底下基底换代时仍能延续。Meta-Harness 发现（「harness engineering 是有大搜寻空间的优化问题」）与 AHE 发现（「……而搜寻能跑成连续可观测性回路, 不是单次优化」）一起描述一个快速远离手动调整的工程实务。

### 从研究到生产：Advisor Tool（2026 年 4 月）

Meta-harness 发现是研究结果。一个月后, Anthropic 出货首个产品化的 meta-harness pattern: **Advisor Tool**（beta, `advisor-tool-2026-03-01`）。该 pattern 把更快的 executor 模型与更有能力的 advisor 模型配对。Executor 处理大部分工作; 当它撞到决策点, 它调用 `advisor()` 并收到一个策略计画或路线修正（典型 400-700 文字 token, 含思考 1,400-1,800）, 而不离开当前 API 请求。

Anthropic 推荐的默认配置很说明:

| Executor | Advisor | 目标用途 |
|----------|---------|----------|
| Haiku 4.5 | Opus 4.6 | 从只用 Haiku 提升智能 |
| Sonnet 4.6 | Opus 4.6 | 用 Sonnet 成本达到 Opus 单独的质量 |
| Opus 4.6 | Opus 4.6 | 最难任务的质量精炼 |

这是 6 倍 meta-harness 差距被翻译成定价策略。不是为每个 token 付 Opus 价格, 你为执行付 Sonnet 价格、为真正塑造输出的 1-2 次 advisor 调用付 Opus 价格。Anthropic 建议的 prompting pattern 值得引用, 因为它把 harness 时机编纂成规则:

> 「在实质工作*之前*调用 advisor——在写之前、在承诺解读之前、在基于假设建构之前。[...] 在长于几步的任务上, 至少在承诺做法之前调用一次 advisor, 并在宣告完成之前调用一次。」

文档中几个细节对从业者重要:

- **服务端子推论。** Advisor 在同一个 `/v1/messages` 请求内运行。Executor 发出 `server_tool_use` 块, Anthropic 用完整 transcript 跑独立推论 pass, 结果作为 `advisor_tool_result` 回来。你的代码不需额外 round trip。
- **快取约 3 次调用打平。** 在 advisor 工具上启用 `caching` 把 advisor 的 transcript 写入 5 分钟或 1 小时快取。第一次调用花费额外; 收益从约第三次调用开始。短任务应关 caching。
- **简洁 prompt 减少输出 35-45%。** 单一指令——「Advisor 应在 100 字内回应, 用列举步骤而非解释」——可衡量地减少 advisor 的最大成本驱动, 而不改变调用频率。
- **明确协调协议。** 当 advisor 建议与 executor 已经收集的实证证据冲突, Anthropic 的系统 prompt 告诉 executor 再做一次 advisor 调用, 框为「我发现 X, 你建议 Y, 哪个约束破解平局？」, 而非沉默切换。这是对「该信任规划者还是数据」问题的生产级答覆——这个问题在多个角色不同意时都会出现。

Advisor Tool 在直接效用之外重要。它是 meta-harness 思维已从研究好奇心移到商业 primitive 的信号。「同模型、不同 harness、6 倍差距」发现不再需要研究团队来利用——Anthropic 把它暴露为工具调用。预期其他实验室跟进推出他们自己的 advisor/executor 配对, 预期 harness engineering 职位描述开始把多模型协调列为核心技能。

## 4.6 Anthropic 的三 Agent 架构

一个反复出现的三角色 pattern, 常被从业者社群总结为 **Planner / Generator / Evaluator**, 整个 2025 年成为多 agent harness 的常见框架。这个框架最好读为对 Anthropic 的 [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents) 中描述的 pattern（orchestrator-worker、evaluator-optimizer）的教学综合, 而非 Anthropic 自己在主要写作中采用的标签。2026 年 3 月 31 日 Claude Code 原始码外泄（本节稍后涵盖）确认了这个区别: 在生产中, Anthropic 实际 harness 是围绕分层自愈记忆组织, 而非字面的三角色分解。这些角色仍描述一个有用分类, 所以本节用它们讨论关切分离:

- **Planner：** 把任务分解成子任务, 维持整体计画, 决定何时修订。
- **Generator：** 执行个别子任务——写代码、起草文字、调用工具。
- **Evaluator：** 对照任务要求评估 Generator 输出, 提供结构化回馈。

这种关切分离被广泛用于处理本章标记为 **context anxiety** 与 **self-evaluation bias** 的两个失效模式（这些标签是本指南用的框架; 底层观察出现在受 Anthropic 已发表 agent 研究启发的 pattern 中）:

**Context Anxiety（上下文焦虑）。** 当单一 agent 处理规划、执行、评估, 它倾向规避。它给输出加资格、加不必要的注意事项、把 token 花在元评论而非任务执行上。分离角色让每个 agent 专注, 不必扛其他角色的认知负载。

**Self-Evaluation Bias（自我评估偏差）。** 模型系统性地不擅长评估自己的输出。它们表现出有据可查的宽容偏差——给自己的工作打的分比独立评判者会打的高。三 agent 架构透过用独立的评估器（可能是不同模型或不同 prompt 的实例）来缓解, 评估器对生成输出没有投资。

从业者社群强调的一个微妙之处, 与 Anthropic 的 evaluator-optimizer 指引中观察到的 pattern 一致: **评估器校准本身是个 harness engineering 问题**。过严的评估器导致无限修订循环。过宽的让低质量工作通过。评估器的阈值与标准需要和 generator 的指令一样仔细调整。

### Claude Code 外泄：实证观察（2026 年 3 月 31 日）

整个 2025 年大部分时间, 三 agent 架构是透过 Anthropic 已发表研究知道的、从行为推论的。2026 年 **3 月 31 日**, 这变了。Anthropic 不慎在 npm 包 **`@anthropic-ai/claude-code` v2.1.88** 内发布一份 59.8MB source map, 暴露约 **513,000 行未混淆 TypeScript 跨 1,906 档**。Anthropic 把事件描述为「人为打包错误, 不是安全外泄」, 但从业者首次能直接读到一个前沿实验室的生产 harness。

外泄中重塑社群对架构描述的几个发现:

- **它字面上不是「Planner / Generator / Evaluator」。** 早期社群文章把 Claude Code 映射到 4.6 三角色框架, 结果是对研究的误读。实际架构组织为**三层「自愈记忆」**系统。这些层对应到 scratchpad / 工作状态、压缩中期状态、持久项目记忆——层之间有明确的修复与协调逻辑。
- **`MEMORY.md` 是索引, 不是仓库。** 不是单一记忆档, `MEMORY.md` 担任**轻量级指针索引**, 指向更详细笔记。这更接近文件系统目录而非 transcript, 这是让记忆层在不膨胀 context 下扩展的原因。
- **`KAIROS` 是自主 daemon 模式。** 名为 `KAIROS` 的 feature flag 在原始码中被引用 **超过 150 次**。它把守一个自主 daemon 模式——一个无人看管、长时间执行的循环, 远超大多数用户知道的互动 REPL。
- **44 个隐藏 feature flag。** 除了 `KAIROS`, 原始码含 44 个未发布功能的 feature flag, 显示公开发布的是 harness 内部支援的保守子集。

实务结论: Planner / Generator / Evaluator 拆分仍是有用的概念分类（Anthropic 研究论文仍以这些术语描述系统）, 但生产中架构是围绕**记忆与修复**分层, 而非仅围绕角色分解。2026 年的 harness engineering 越来越意味着设计记忆层与层之间的转换。

外泄两周后, 同一架构再走一步——这次向外, 离开用户机器。透过 **Claude Code Routines**（2026 年 4 月 14 日）, Anthropic 把编排器席位本身从笔电移到自己的云端, 把排程、API、GitHub 事件触发器暴露为一等 harness primitive。读在外泄旁边, 这是一个清楚的架构修辞: 编排器不再被建模为用户照顾的 REPL, 而是住在 Anthropic 基底上的 daemon。三层自愈记忆跨触发器持续; harness 不再需要用户的程序活着才能让循环进展。无论你采纳 Routines 与否, 这个框架现在在空气里: 编排器席位是产品表面, 「循环在哪运行」是设计决策而非默认。

## 4.7 Harness 即护城河

2026 年初, Meta 以约 20 亿美元收购 Manus。Manus 没有专有模型。它的全部价值在 harness——把商品级模型 API 变成可靠 agent 产品的编排逻辑、context engineering 管线、工具整合层、运营基础设施。

这场收购把行业一直在发现的事结晶化: **harness 是护城河**。模型越来越商品化。差异化在于你怎么包它——你提供什么工具、你怎么管 context、你怎么处理失败、你怎么编排多步工作流、你怎么评估质量。

对从业者的含义是: harness engineering 不是通往模型开发「真正工作」途中要应付的管线工事。对大多数生产 AI 团队它*就是*真正工作。到 2026 年 4 月,「harness engineering」作为正式学科已进入行业词汇, Claude Code 外泄提供了对生产 harness 实际包含什么的首次实证观察。

## 4.8 Harness 维护：压力测试的命令

Anthropic 最可行动的洞察可能是最简单的: 每个 harness 组件编码一个关于模型局限的假设, 而**这些假设会过期**。

当一个 harness 围绕 GPT-4 级能力建构, 它可能包括:
- 明确思维链 prompting（因为模型需要它）
- 激进的输出解析（因为模型在格式上不一致）
- 多步验证（因为单 pass 准确度不足）
- 详细 few-shot 例子（因为零样本表现差）

随着新模型带来改善的推理、指令遵循、输出一致性, 这些组件变成**可能不再需要承重的承重墙**。它们加 latency、成本、复杂度而不贡献质量。

学科是周期性压力测试: 系统性地停用 harness 组件, 决定哪些仍必要。如果移除规划步骤不退化效能, 移除它。如果模型现在不需 few-shot 例子也能可靠遵循格式, 丢掉它们。如果自我评估加成本但不加质量, 消除它。

这违反直觉。工程师天然加安全机制并抗拒移除它们。但在 harness engineering, 不必要组件不是免费的——它们消耗 context window 空间、加 latency、增加成本、创造维护负担。一个匹配当前模型能力的精简 harness, 跑赢一个为更弱模型过度工程的。

实务建议: 当上线新模型, 先跑你现有的 harness, 然后系统性剥离组件同时衡量任务效能。剩下的就是你真正的 harness。你移除的是先前能力时代的技术债。

成熟 harness 最终把压力测试问题反转: 不是问「我能移除哪些组件」, 而是「我应该在哪些组件上多花运算, 何时多花」。2026 年 4 月 **CATTS** 预印本（Consensus-Aware Test-Time Scaling, arXiv 2602.12276）给那个问题一个可用答案。CATTS 每个 agent 步骤采样小型 rollout 委员会, 用它们之间的分歧作为每步不确定性分数; 该分数被用来不均匀分配测试时运算——委员会分歧时更多 rollout, 收敛时更少。在 WebArena-Lite 与 GoBrowse 上, 该技术报告在 **2.3 倍少 token** 下 **+9.1%** 任务准确度。对成熟 harness, CATTS 与 Advisor Tool 并排: advisor pattern 决定*想什么*, CATTS 决定*想多深*。两者都用 runtime 计算的衡量不确定性讯号, 取代假设（「永远重试三次」、「永远在难问题上用 Opus」）。

2026 年 4 月 AHE 结果（第 4.5 节）在结构上做出同样论点: 压力测试不是一次性审查活动, 而是连续可观测性回路。手动压力测试作为从业者今天能跑的学科仍有价值; AHE 显示它也是可自动化的。

## 4.9 云原生 Harness Primitive

整个 2025 与 2026 年第一季, harness 几乎都是你自己建、自己跑的东西。即使最复杂的 pattern——三 agent 架构、Advisor Tool、KAIROS 风格自主循环——也都假设你的代码握有编排器席位。你写 cron 工作、跑 daemon、保持笔电唤醒、拥有失效模式。基底是通用运算（Mac mini、VPS、Kubernetes pod）, harness 层从程序监督员往上是你的责任。

**2026 年 4 月 14 日**, Anthropic 的 **Claude Code Routines** 研究 preview 朝改变这件事跨出第一具体步。一个 Routine 是在 Anthropic 云端而非用户机器上运行的 Claude Code 工作流, 由三种触发器之一触发: **排程**（cron 等价）、**API 调用**（来自其他服务的程式化呼叫）、**GitHub 事件**（push、PR、issue、comment）。这些触发器是 harness 工程师过去 18 个月写的档案式排程 pattern 的刻意泛化: 一样的「每周日 09:00 HKT 跑」语意, 但被表达为托管 primitive 而非 `cron + tmux + claude` shell 咒语。配额与底层 Claude Code 订阅分层——**Pro 5/天、Max 15/天、Team/Enterprise 25/天**——把基底定价为「每席每天少数有意义的循环」, 而非「按小时的原始运算」。

云端执行细节比听起来重要。自架档案式排程器把编排器席位握在用户拥有的硬件上; 如果 Mac 关、睡、没电, 循环不跑。Routine 不论用户机器状态都完成。这溶解了一整类失效模式（笔电盖、网络掉、OS 更新、意外重启）和对应一类补偿机制（wake-on-LAN 把戏、Mac Mini「永远开」服务器、冗余执行器）。对真正事件驱动的工作流——「PR 开时, 做 X」——托管 primitive 直截了当比自架轮询器更适合。

取舍是新的天花板。托管 primitive 按触发器与配额定价, 不按工作负载的物理。它假设你的循环符合排程 / API / GitHub 事件形状、每天配额够、Anthropic 基底是你代码与数据该住的地方。对相当数量的 harness 工作负载, 那些假设都不干净成立。**浏览器自动化** 已认证 session 仍受益于运行在已经有用户 cookie、profile、信任状态的机器上。**高频编排**——亚分钟轮询、即时市场或感测器数据、每天 25 次调用是侮辱的任何东西——需要按秒计费的 runtime, 不是按触发器。**非 GitHub 事件来源**（Discord 讯息、内部 webhook、客制 MCP 服务器、设备上文件系统事件）在 Routines 中没有一等触发器; 暴露它们需要自己写 bridge, 这把你放回自架机器跑 bridge。任何依赖本机文件、本机模型推论、本机网络存取的, 在结构上都仍在云外。

对 2026 年 harness 工程师的诚实框架: 像 Routines 这样的云原生 primitive 是 harness 工作负载里 **GitHub 事件触发、排程、API 调用** 那一象限的对答, 它们很可能在接下来 12 个月戏剧性压缩那个象限的运营成本。自架 harness 不会消失——它正被收窄到它实际付清自己的地方。要发展的学科是本章一直在建构的同一学科: 知道每个组件编码什么假设, 注意到下面基底何时改变。

**Routines 与 Managed Agents。** 值得精确说明 Anthropic 在 2026 年 4 月实际出货什么, 因为这两块有时被混淆。**Claude Managed Agents**（公测, 2026 年 4 月 8 日）是*基底*: 一个把 session（一切发生过事情的 append-only 事件 log）、harness（调用 Claude 与路由工具调用的循环）、sandbox（Claude 可执行代码的环境）暴露为三个虚拟化组件的托管 runtime, 配 tracing 与 Agent / Environment / Session / Events API 表面叠加在上。SiliconANGLE 的发布报道指出基底定价是标准 token 费率加上**每 agent runtime 小时 8 美分**; 该数字来自次级科技媒体, 不是 Anthropic 主要文档。即便在次级引用 bar, 定价结构重要: 这是首个把编排器席位本身与推论分开计费的前沿供应商 primitive。**Claude Code Routines**（研究 preview, 2026 年 4 月 14 日）是*触发表面*, 跑在该基底（或相容替代）之上: 排程、API 调用、GitHub 事件, 配 Pro / Max / Team-Enterprise 层级每天 5 / 15 / 25 次调用配额。两者回答不同问题。Managed Agents 答「agent 循环物理上在哪运行, 它的状态如何在回合之间持久维持？」Routines 答「什么让循环开始？」一个采纳 Routines 但不采纳 Managed Agents 的自架 harness, 仍拥有它的状态与执行环境; 一个采纳 Managed Agents 但建自己触发层的, 仍拥有工作何时开始。实务上, 2026 年中大多数云原生 harness 设计都会两者都采——但解绑是架构重点。Anthropic 不再把「harness」当一件事卖; 它在卖它的组成 primitive。

解绑在 2026 年 4 月底两个结构性重要的动作中继续。第一, **4 月 23 日**, Anthropic 把 **Memory for Managed Agents** 加到公测: 一个文件系统挂载、稽核日志的存储, 给 agent 耐久跨 session 状态, 配并发存取语意、范围企业权限、Claude Console 的 rollback / redaction 表面。基底现在出货第三个 primitive——*耐久记忆*——与 sessions 和 sandboxes 并列; 3 月 31 日 Claude Code 原始码外泄揭示的生产架构（三层自愈记忆）现在是其他团队能租用的供应商管理 primitive。第二, **4 月 28 日**, AWS 与 OpenAI 出货 **Amazon Bedrock Managed Agents powered by OpenAI** 在 limited preview, 首次命名并贩售「OpenAI agent harness」作为独立产品表面。读在一起, 这两件事把 Managed Agents pattern 从「Anthropic 4 月 8 日的赌注」转移到 **跨供应商基底形状**——三个前沿供应商中两个现在把编排器席位作为托管 primitive 出货, 配每 agent 身分、动作日志、内建耐久状态。对 2026 年中在编排器席位上比较 build vs. buy 的 harness 工程师, 选项集不再单一供应商, 基底不再是薄 runtime: 它含记忆。

## 4.10 托管推论转变（2026 年 4 月）

整个 2025 年, 呼叫者与模型之间的 harness 合约大致是个旋钮面板: `temperature`、`top_p`、`top_k`、`max_tokens`、`budget_tokens`、系统 prompt。从业者按案转旋钮, 有时在同一 agentic 循环内每步都转。2026 年 4 月 16 日 **Claude Opus 4.7** 的发布打破那个 pattern。在单一发布中, 三项变更朝同一方向拉:

1. **`temperature`、`top_p`、`top_k` 被弃用。** 任何非默认值返回 400 错误。采样级控制不再在呼叫者手上。
2. **自适应思考是唯一的思考开模式。** 手动 `budget_tokens`（extended thinking）被移除; `effort`（`low`、`high`、`xhigh`、`max`）取代它。
3. **Task budgets 变成一等 primitive。** 一个新 beta 标头（`anthropic-beta: task-budgets-2026-03-13`）让呼叫者为*整个 agentic 循环*——思考、工具调用、工具结果、最终输出——声明建议性 token 预算。模型在工作时看到倒数。

前两项变更是减法: 旋钮被移除。第三项是加法: 一个先前在任何前沿 API 都不存在的 primitive。一起它们描述合约变更。不是「你调采样器, 模型产生回应」, 合约现在是「你声明运算预算, 模型对它自我分配, 一步一步决定任务还值多少搜寻、推理、综合」。Harness 变成预算对话而非参数面板。

「建议而非强制」细节重要。Task budgets 不是硬上限（`max_tokens` 仍担任那个角色, 仍只面向呼叫者）。相反, 模型被告知它的预算并用它来排序优先。实务上, 设太紧的预算产生拒答式输出而非退化的——模型偏好拒绝而非出货它判定为资金不足的结果。最低 20K token 被强制, 正是为防止重大任务的那个失效模式。

对 harness 设计者, 含义具体: 任何在 Opus 4.6 跑的 harness 需要为 4.7 重新基线, 不只在 prompt 层级, 也在 timeout、retry、压缩、工具调用预算层级。Anthropic 自家迁移文档直接说: *重新基线 harness, 不只是 prompt*。Advisor Tool（第 4.5 节）与 task budgets（本节）描述任何长时间 harness 的新两轴优化: Advisor 决定*想什么*; task budgets 决定*每一步想多深*。两者都用 runtime 计算的衡量讯号取代旋钮调整。

这是更广 pattern: **托管推论转变**。前沿供应商越来越把推论本身视为产品表面而非参数表面。Harness 层正从「你配置推论调用」移到「你描述工作, 推论层适配」。其他实验室是否跟随 Anthropic 的具体决策（采样旋钮弃用、建议性预算）还是只跟方向, 是开放问题。方向本身看起来已成定局。

---

## 来源

- **Böckeler, Birgitta.** "Harness engineering for coding agent users." martinfowler.com（Exploring Generative AI 系列）, 2026 年 4 月 2 日。[https://martinfowler.com/articles/harness-engineering.html](https://martinfowler.com/articles/harness-engineering.html) ——Guides vs. Sensors、Computational vs. Inferential 分类。
- **OpenAI.** Codex 公开材料: [https://openai.com/index/introducing-codex](https://openai.com/index/introducing-codex)。OpenAI Codex 的 harness 设计框架锚点; 广为引用的「三位工程师 / 约 100 万行 / 约 1,500 个 PR」数字在 2025-2026 年 OpenAI 演讲与文章中流传, 在此引用为社群引用而非来自单一标准帖。
- **IMPACT 助记词。** Intent / Memory / Planning / Authority / Control flow / Tools——一个六维 harness 设计清单, 在 2020 年代中期从业者讨论中浮现。在本章作为教学框架使用; 不归属任何特定原始来源。
- **Stanford / MIT / KRAFTON.** "Meta-Harness: Automated Optimization of LLM Agent Harnesses." arXiv 预印本, 2026 年 3 月。6 倍效能差距发现, 自动化 harness 调整。
- **Lin et al.** "Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses." arXiv 2604.25850, 2026 年 4 月 28 日。[https://arxiv.org/abs/2604.25850](https://arxiv.org/abs/2604.25850) ——复旦/北大/上海齐迹智锋。Meta-harness 搜寻问题的可观测性支柱重构; 在 Terminal-Bench 2 上 69.7% → 77.0%, 配跨家族转移。
- **Anthropic.** "Claude Managed Agents overview." API 文档, 2026 年 4 月 8 日。[https://platform.claude.com/docs/en/managed-agents/overview](https://platform.claude.com/docs/en/managed-agents/overview)
- **Anthropic Engineering.** "Scaling Managed Agents: Decoupling the brain from the body." 2026 年 4 月 8 日。[https://www.anthropic.com/engineering/managed-agents](https://www.anthropic.com/engineering/managed-agents) ——三个虚拟化组件（session、harness、sandbox）; 定价细节（标准 token 费率加上每 agent runtime 小时 8 美分, 按 SiliconANGLE 发布报道）不在 Anthropic 主要文档中, 由次级科技媒体引用。
- **Anthropic.** "Memory for Claude Managed Agents"（2026 年 4 月 23 日）。[https://claude.com/blog/claude-managed-agents-memory](https://claude.com/blog/claude-managed-agents-memory) ——文件系统挂载记忆、跨 session 学习、稽核日志、范围企业权限; 与 3 月 31 日 Claude Code 原始码外泄关于三层自愈记忆的发现关闭回路。
- **AWS 与 OpenAI.** "Bedrock Managed Agents powered by OpenAI"（2026 年 4 月 28 日, limited preview）。AWS 公告: [https://aws.amazon.com/about-aws/whats-new/2026/04/bedrock-openai-models-codex-managed-agents/](https://aws.amazon.com/about-aws/whats-new/2026/04/bedrock-openai-models-codex-managed-agents/)。About Amazon: [https://www.aboutamazon.com/news/aws/bedrock-openai-models](https://www.aboutamazon.com/news/aws/bedrock-openai-models)。OpenAI 公告: [https://openai.com/index/openai-on-aws/](https://openai.com/index/openai-on-aws/) ——首次「OpenAI agent harness」被命名并作为独立产品表面贩售; Managed Agents pattern 上的跨供应商收敛。
- **Anthropic.** "Building Effective Agents." Anthropic 工程博客, 2024 年 12 月 19 日。[https://www.anthropic.com/engineering/building-effective-agents](https://www.anthropic.com/engineering/building-effective-agents) ——描述 orchestrator-worker pattern 与 evaluator-optimizer workflow; 本指南把相关失效模式标为「context anxiety」与「self-evaluation bias」作教学使用。从业者社群把它总结为 Planner / Generator / Evaluator triple 的框架, 是建立在这些 pattern 上; Anthropic 自己在主要写作中没用那个明确 triple。实际 Claude Code 架构, 由 2026 年 3 月 31 日原始码外泄揭示（第 4.6 节）, 是围绕分层自愈记忆组织而非角色分解。
- **Meta / Manus 收购。** 多份报道, 2026 年初。约 20 亿美元收购验证 harness 即护城河论点。
- **Karpathy, Andrej.** "From Vibe Coding to Agentic Engineering" —— Sequoia AI Ascent 2026 fireside chat（约 2026 年 4 月底录制, 主要 YouTube 视频 [https://www.youtube.com/watch?v=96jN2OCOfLs](https://www.youtube.com/watch?v=96jN2OCOfLs); 作者总结在 [https://karpathy.bearblog.dev/sequoia-ascent-2026/](https://karpathy.bearblog.dev/sequoia-ascent-2026/)）。把 vibe coding 框为*提升地板*模式（人人能建）, agentic engineering 为*抬升天花板*学科（规格、计画督导、diff 检查、eval 回路、权限范围、worktree 隔离）。锚定 2025 年 12 月一个拐点, Karpathy 在那时把自己的编程比例从约 80% 手写翻转到约 80% 委派。早期 2025「Software 3.0」/「Software Is Changing (Again)」演讲在 AI Engineer World's Fair 与 YC AI Startup School, 建立模型作为新一类可程式化组件的更广框架。
- **LangChain.** "Agent Architecture Patterns." LangChain 文档, 2025。控制流与工具编排的实务 pattern。
- **Harrison Chase.** "Agent Engineer" 框架, 2025——LangChain 博客与 X 贴。这个词以 harness 为中心工程的角色定义框架进入从业者词汇; 在此作为 2025 年代讨论中的 pattern 引用, 而非单一标准帖。
- **"CATTS: Consensus-Aware Test-Time Scaling for Agents."** arXiv 2602.12276（2026 年 4 月发布周期）。投票推导不确定性作为测试时运算分配器; 在 WebArena-Lite 与 GoBrowse 上 +9.1% / 比均匀扩展少 2.3 倍 token。[https://arxiv.org/abs/2602.12276](https://arxiv.org/abs/2602.12276)
- **Anthropic.** "Introducing Routines in Claude Code." Anthropic 博客, 2026 年 4 月 14 日。[https://claude.com/blog/introducing-routines-in-claude-code](https://claude.com/blog/introducing-routines-in-claude-code)
- **Anthropic.** "Claude Code Routines documentation." [https://code.claude.com/docs/en/routines](https://code.claude.com/docs/en/routines) ——触发器（排程 / API / GitHub 事件）、配额（Pro 5/天、Max 15/天、Team/Enterprise 25/天）、云端执行语意。
- **Anthropic.** "Introducing Claude Opus 4.7"（2026 年 4 月 16 日）。[https://www.anthropic.com/news/claude-opus-4-7](https://www.anthropic.com/news/claude-opus-4-7)
- **Anthropic.** "What's new in Claude Opus 4.7"（API 文档）。[https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-7](https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-7) ——task budgets（`anthropic-beta: task-budgets-2026-03-13`, 建议性, 最低 20K）、自适应专用思考、移除 `temperature` / `top_p` / `top_k`。
- **Caylent.** "Claude Opus 4.7 Deep Dive: Capabilities, Migration, and the New Economics of Long-Running Agents"（2026 年 4 月）。[https://caylent.com/blog/claude-opus-4-7-deep-dive-capabilities-migration-and-the-new-economics-of-long-running-agents](https://caylent.com/blog/claude-opus-4-7-deep-dive-capabilities-migration-and-the-new-economics-of-long-running-agents) ——「重新基线 harness, 不只是 prompt」。
- **Archon GitHub Repository.** [https://github.com/coleam00/Archon](https://github.com/coleam00/Archon) ——TypeScript / Bun harness 构建器, YAML DAG 工作流包 Claude Code 与 OpenAI Codex CLI; v2.1 在 2026 年 4 月发布。
- **OpenHarness GitHub Repository.** [https://github.com/HKUDS/OpenHarness](https://github.com/HKUDS/OpenHarness) ——香港科技大学数据实验室的 Python 参考实现; 首次 commit 2026 年 4 月 1 日。

### 给入门者的延伸阅读

- **Cab.** 「A Layer-by-Layer Walk Through Harness Engineering.」繁体中文文章, 2026。从单一 `POST /v1/messages` 调用一路建到 prompt engineering、function calling、agent loop, 最后到完整 harness 复杂度。值得注意的是「模型從來都沒有長手」的隐喻, 把工具使用重构为 harness 问题而非模型能力, 还有它对 Claude Code 的 harness 实际在背后做什么的明确走读。推荐作为读本章理论优先框架（Böckeler 分类、IMPACT、Meta-Harness）之前的温和入门。
- **Anthropic.** ["Building Effective Agents"](https://www.anthropic.com/research/building-effective-agents) ——给来自非研究背景读者的标准短篇介绍。与上面的 Cab 文章配对得好: Cab 给建构, Anthropic 给具体 pattern。

---

*上一章: [第 3 章 —— Context Engineering](03-context-engineering.md)*

*下一章: [第 5 章 —— Skill Systems 与 Skill Graphs](05-skill-systems.md)*
