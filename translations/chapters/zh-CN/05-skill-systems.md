# 第 5 章：Skill Systems —— 技能、技能图与渐进式揭露

> **一句话总结：** Skill 是可重用的指令集, 告诉 AI 如何做特定任务; skill graph 把它们连成可导航的知识网络。
>
> **为什么重要：** 不用每次都跟 AI 解释同一件事, skill 让你教一次就永远复用那份知识。

Skill 是预先打包的指令集——内含 prompt、工具配置、行为规则的自足束——在需要某种特定能力时被注入 agent 的 context window。它们是 agent 系统从少数内建行为扩展到数百上千专门能力, 同时不让模型淹没在不相关指令中的机制。

本章涵盖技能系统的架构、它们造成的组合问题, 以及解决它的渐进式揭露 pattern。

---

## 5.1 技能概念

最简单的技能是含特定任务指令的 markdown 档（或结构化文字块）。当用户请求匹配技能的触发条件, 技能内容被加载到 context window。无匹配时, 该技能贡献零 token。

这与一个想涵盖每种能力的整体系统 prompt 根本不同。一个描述 90 个工具与 50 种行为模式的系统 prompt 在用户开始打字之前就可能消耗 50,000 token 以上。基于技能的系统只加载相关的, 让基线 context 精简, 把窗口容量保留给实际任务。

设计 pattern 借自软件工程: skill 之于 agent 就像 plugin 之于应用。它们提供可扩展性而不臃肿。

## 5.2 Anthropic 技能生态系

Anthropic 在 2025 年 10 月为 Claude Code 推出技能, 最初是个项目专用功能——`.claude/` 目录下的 markdown 档, Claude 在相关时能调用。格式刻意简单: 一个含描述、触发条件、指令的 markdown 档。

到 2025 年 12 月, Anthropic 透过 agentskills.io 把技能作为开放标准发布, 定义任何 agent 系统都能采纳的可移植格式。规格涵盖:

- 技能元数据（名称、描述、版本、作者）
- 触发定义（关键字匹配、意图分类器、regex pattern）
- 内容结构（指令、例子、工具配置）
- 依赖声明（这个技能建立在其他哪些技能之上）

生态系反应迅速。到 2026 年初, 官方仓库累积超过 87,000 GitHub stars, 社群贡献的技能超过 700,000。awesome-llm-skills、awesome-agent-skills（含来自官方平台团队的 1,000+ 技能）、awesome-claude-code 等收集成为主要发现频道。

这种成长创造了技能本来要解决的问题: 太多能力争抢有限 context 空间。

## 5.3 扩展问题

OpenAI 的 agent 文档含一个实务指引: **保持 agent 在 20 个工具以下, 预期超过 10 个会准确度退化**。跨多个模型家族的实证测试确认这个阈值。每个额外工具定义都加 token 到 context, 加决策分支到模型选择空间。在 90 个工具时, schema 开销本身就可能超过 50,000 token——在任何对话、记忆、检索文件进入窗口之前。

退化不只是 token 数。是关于决策复杂度。当模型必须在 90 个工具间选, 概率质量分薄。模型把更多推理容量花在工具选择上, 较少在任务执行上。工具参数构造的错误率上升。模型开始更频繁选「合理但错」的工具。

技能面对同样的扩展压力。一个有 500 个可用技能的系统不能把全部 500 个描述都加载到 context。即使只加载 500 个技能的触发描述, 也可能消耗数千 token, 退化模型处理实际请求的能力。

解法是渐进式揭露。

## 5.4 渐进式揭露架构

渐进式揭露是个多层信息架构, 每一层为下一个路由决策提供刚好够的细节:

**第 0 层: 路由索引。** 一个把类别映射到技能群组的精简表。整个技能库可能总共消耗 200-500 token。这是静态时坐在系统 prompt 里的东西。

**第 1 层: 类别描述。** 当路由索引识别相关类别, 加载该类别中技能的一段描述。每个描述为扫读优化——足以判断相关性, 不足以执行。

**第 2 层: 技能链接与依赖。** 对选中的技能, 加载它的依赖图——它需要哪些其他技能或工具、它预期什么 context。

**第 3 层: 段落与摘要。** 加载技能的结构大纲——段落标题、关键决策点、参数清单——不含完整指令内容。

**第 4 层: 完整内容。** 把完整技能指令加载到 context window。这只对实际被调用的一两个技能发生。

由 Heinrich 与 arscontexta 团队正式化的关键洞察是: **大多数决策在读到任一完整文件之前就发生**。路由索引消除 95% 技能。类别描述消除大多数剩余。完整内容加载是例外, 不是规则。

跨生产系统衡量, 渐进式揭露相对于前置加载所有技能定义, 把 token 开销减少 **85-95%**。Anthropic 自家 agent skills 实现示范这一点: 17 个生产技能在静态时消耗约 1,700 token（第 0 层 + 第 1 层）, 仅在调用时展开到完整内容。

## 5.5 技能图

Heinrich 的 Skill Graph 架构（arscontexta, 2025-2026）把渐进式揭露延伸到网络结构。不是按类别组织的扁平技能清单, 技能图是 **由 wikilink 连结的互联 markdown 档网络**, 每个节点带:

- 含简洁描述的 YAML frontmatter 区块（用于第 1 层扫读）
- 指向相关技能、前置技能、子技能的 wikilink
- 能独立加载的结构化段落

图结构启用扁平技能清单不能支援的几个能力:

**情境式导航。** 当一个技能被调用, 它链接的技能成为共载候选。一个「deploy」技能链接到「test」、「rollback」、「monitor」技能——不是因为它们在同一类别, 而是因为它们在运营上相邻。

**依赖解析。** 技能能声明前置条件。调用复杂技能自动拉入它依赖的基础技能, 类似套件依赖解析。

**部分加载。** 因为技能用清晰段落结构化, 系统能加载特定段落（例如部署技能的「错误处理」段落）而不加载完整文件。

图拓扑本身变成一种知识表示。密集连接的技能群指出有高内部一致性的能力领域。孤立技能可能指出系统涵盖的差距或整合机会。

## 5.6 SkillReducer 论文

2026 年 3 月发表的研究检视跨多个 agent 平台的 55,315 个技能, 产生挑战对技能质量天真假设的发现:

- **26.4% 技能完全缺路由描述**。它们有完整指令内容但无元数据帮路由系统识别何时调用。这些技能只能透过精确名字触发——对任何智能路由层都不可见。

- **超过 60% 技能 body 内容是非可行动的**。它包含背景 context、动机、注意事项、解释性文字, 而非模型能执行的具体指令。这些内容消耗 token 而不贡献任务效能。

- **压缩过的技能比原版改善输出质量 2.8%**。当研究者剥离非可行动内容并紧缩指令语言, 模型效能实际改善。少即是多——context 中减少的噪音让模型聚焦于可行动指令。

技能撰写的含义直接:

1. **每个技能都需要路由描述**。没有它, 技能对渐进式揭露系统等于不可见。
2. **指令内容应密集且可行动**。背景 context 属于文档, 不是被注入 context window 的技能 body。
3. **技能质量衡量应包含 token 效率**——不只「它有效吗」而是「每消耗 token 它有效吗」。

## 5.7 MCP 的 Meta-Tool Pattern

Model Context Protocol（MCP）引入跨供应商 agent 发现并调用工具的标准方式。但 MCP 原本设计在连线时加载所有可用工具 schema, 创造与技能面对的同样扩展问题。

Meta-tool pattern 用两个组件解决:

- **发现工具:** 一个接受自然语言描述、从完整注册表返回相关工具 schema 的单一工具。这是基线时唯一加载的工具。
- **执行工具:** 一个通用工具调用包装器, 一旦工具的 schema 透过发现取得, 就能按名调用任何工具。

系统加载两个工具 schema 而非数百。当模型判定需要某能力, 它调用发现工具, 收到相关 schema, 然后调用具体工具。该 pattern 用一次额外推论 round-trip 换取大量 context 节省。

这是渐进式揭露应用到工具管理: 模型拿到电话簿, 不是每个联络人档案的内容。

## 5.8 撰写指引

从 SkillReducer 发现与生产经验, 一组技能撰写最佳实务浮现:

- **以路由描述领头。** YAML frontmatter 描述是档案中最重要一行。它决定技能是否会被调用。为分类器写, 不是为人类读者写。
- **前置可行动指令。** 技能 body 头 200 token 应含核心行为指令。背景与 context 在后。
- **用结构化段落。** 标题、清单、清楚分隔启用部分加载与段落级检索。
- **明确声明依赖。** 如果技能假设另一技能或工具可用, 在元数据中陈述。
- **包含触发例子。** 提供 3-5 个该激活技能的用户讯息例子。这些既是文档也是路由层的测试案例。
- **衡量 token 成本。** 追踪每个技能的 token 数并设预算。如果技能超过 2,000 token, 考虑它能否被拆或压缩。

## 5.9 行业收敛：Google Agent Skills 规格（2026 年 4 月）

整个 2025 年大部分时间, 渐进式揭露主要是 Anthropic 惯例——透过 2025 年 10 月 Claude Code 技能与 12 月 agentskills.io 开放标准正式化。在 **2026 年 4 月**, Google Developers Blog 把它自己的 **Agent Skills 规格** 正式化, 采纳并延伸同一架构。规格描述渐进式揭露的三个明确层级:

- **第 1 层 —— 元数据（每技能约 100 token）。** 含技能名称、单行描述、触发提示、版本的精简描述符。每个可用技能的第 1 层元数据坐在 agent 的基线 context 中。加载 10 个技能, 这是约 1,000 token 的恒定开销。
- **第 2 层 —— 指令（< 5K token）。** 一个技能的完整行为指令, 在第 1 层匹配识别该技能为相关时按需加载。第 2 层内容在技能实际被选中前永不进入 context。
- **第 3 层 —— 外部资源。** 完全住在 context window 外的资产——参考文件、数据集、工具 schema、代码范例——只在技能在执行时明确需要才取。

头条效率主张: 对一个有 10 个技能的 agent, 基线 context 用量从约 **10K token**（前置加载完整技能内容）降到约 **1K token**（仅第 1 层元数据）, **90% 减少**。第 2 层内容一次加载一个技能, 第 3 层资源只在执行中需要时加载。

两个细节让 Google 规格在数字之外显著:

1. **它用通用的 `agentskills.io` 规格**。不是分叉, Google 把它的格式与 Anthropic 在 2025 年 12 月发布的开放标准对齐。对一个规格写的技能, 能由另一个平台的 agent 以最少调整消费。
2. **它把渐进式揭露从惯例提升到正式系统设计 pattern**。约一年时间, 渐进式揭露被描述为「Anthropic 跟技能做的事」。随 Google 的采纳与正式化, 它变成有命名架构与可衡量目标的跨供应商行业 pattern——可比作「MVC」或「REST」如何从特定实现演化为通用 pattern。

实务效果是技能库正变得跨供应商可移植, 「你的基线 agent context 消耗多少 token」已变成供应商竞争的一等指标。

---

## 来源

- **Anthropic.** "Claude Code Skills." 文档与开放标准规格, 2025 年 10 月（推出）, 2025 年 12 月（透过 agentskills.io 的开放标准）。2026 年初 87K+ GitHub stars。
- **OpenAI.** "Agent Design Best Practices." OpenAI 文档, 2025。建议每 agent 少于 20 个工具, 超过 10 个会准确度退化。
- **Heinrich (@arscontexta).** Skill Graphs 概念与实现。X 贴（2026）: [https://x.com/arscontexta/status/2023957499183829467](https://x.com/arscontexta/status/2023957499183829467)（Skill Graphs > SKILL.md）。GitHub: [https://github.com/agenticnotetaking/arscontexta](https://github.com/agenticnotetaking/arscontexta) ——Claude Code 插件, 生成含 wikilink 与 YAML frontmatter 扫描的个人化 markdown-graph 知识系统。次级分析: Linas Substack, "Skill Graphs: The Architecture That Solves the AI Agent Context Window Problem." [https://linas.substack.com/p/skill-graphs](https://linas.substack.com/p/skill-graphs)
- **SkillReducer Paper.** "Less Is More: Compressing Agent Skills for Improved Performance." 2026 年 3 月。分析 55,315 个技能, 26.4% 缺路由描述, 60%+ 非可行动内容, 压缩后 2.8% 质量改善。
- **Model Context Protocol（MCP）.** Anthropic 规格, 2024-2025。标准化工具发现与调用协议。
- **awesome-llm-skills.** GitHub 上的社群收集。跨平台编纂的技能库。
- **awesome-agent-skills.** GitHub 收集, 来自官方平台团队的 1,000+ 技能。
- **awesome-claude-code.** GitHub 收集。Claude Code 专属技能与配置。
- **OpenAI.** "Function Calling Best Practices." 2025。工具数量与准确度取舍的实证数据。
- **Griciūnas, Aurimas.** "State of Context Engineering in 2026." SwirlAI Newsletter, 2026 年 3 月。[https://www.newsletter.swirlai.com/p/state-of-context-engineering-in-2026](https://www.newsletter.swirlai.com/p/state-of-context-engineering-in-2026) ——渐进式揭露 / 压缩 / 滑动窗口 pattern; meta-tool pattern。也见 "Breaking Down Context Engineering": [https://www.newsletter.swirlai.com/p/breaking-down-context-engineering](https://www.newsletter.swirlai.com/p/breaking-down-context-engineering)

---

*上一章: [第 4 章 —— Harness Engineering](04-harness-engineering.md)*

*下一章: [第 6 章 —— Agent Memory](06-agent-memory.md)*
