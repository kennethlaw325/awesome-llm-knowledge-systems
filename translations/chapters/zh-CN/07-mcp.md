# 第 7 章：MCP —— 胜出的标准

> **一句话总结：** MCP 是一个通用标准, 让 AI 透过单一协议连接到任何外部工具或数据源。
>
> **为什么重要：** 把 MCP 想成 AI 的 USB——之前每个工具都需要自己的客制连接。现在有一个插头到处通用。

## 什么是 MCP？

Model Context Protocol（MCP）是 Anthropic 创造的开放协议, 标准化 AI 模型如何连接到外部工具、数据源、服务。MCP 之前, 每个 AI 整合都是客制——客制函数定义、专有工具格式、手写认证、脆弱粘合代码。MCP 用通用接口取代这碎片: 任何模型都能用单一协议发现、认证、调用任何工具。

把 MCP 想成 AI 的 USB。USB 之前, 每个外设需要自己的连接器、驱动、协议。USB 没让外设更强大——它让它们可互操作。MCP 对 AI 工具生态系做同样的事。一个 MCP 服务器实现能服务 Claude、GPT、Gemini, 或任何讲该协议的模型。一个 MCP 客户端能连到数千服务器而不需客制整合代码。

## 时间线：从推出到 Linux Foundation

**2024 年 11 月。** Anthropic 把 MCP 作为开源规格发布, 配 Python 与 TypeScript 的参考实现。初次发布含一些参考服务器（filesystem、GitHub、Slack）与建客制服务器的 SDK 支援。反响审慎乐观——AI 社群之前看过被提议的可互操作性标准。

**2025 年 4 月。** 推出后六个月, MCP 跨过累积 800 万 SDK 下载, 社群已建超过 5,800 个服务器。生态系成长比任何人预期都快。关键的是, 竞争 AI 实验室开始采纳该协议, 而非创造替代。

**2025 年底。** MCP 被捐给 Agentic AI Foundation, Linux Foundation 旗下的新实体, 由 Anthropic、Block、OpenAI 联合治理。这个动作中和「Anthropic 控制标准」的关切, 把 MCP 确立为真正行业标准而非供应商专属协议。

**2026（现在）。** MCP SDK 跨所有套件 registry 下载每月超过 9,700 万。生态系含 75+ 个由 foundation 维护的官方连接器, 加上数千个社群建的服务器。该协议已成为 AI 应用的默认整合层, 像 REST 之于 web API。

## 为什么它胜出

几个因素解释 MCP 的快速主导:

**第一天就开放标准。** MCP 在宽松授权下发布, 含完整规格而非只 SDK。这意味竞争者能实现它而不依赖 Anthropic 的代码或善意。

**简单架构。** 协议有三个核心概念: 客户端（AI 模型一侧）、服务器（工具/数据一侧）、传输层（它们如何沟通）。服务器用 JSON Schema 描述暴露工具。客户端发现并调用。传输层处理沟通层（stdio、HTTP+SSE、WebSocket）。这个简单让采纳琐碎——一位胜任开发者能在一小时内建好 MCP 服务器。

**供应商中立治理。** 捐给 Linux Foundation, 配 OpenAI 作为联合治理成员, 消除了最后可信反对。当你的主要竞争者联合治理标准, 标准是真正中立的。

**网络效应。** 每个新 MCP 服务器让协议对每个客户端更有价值, 反之亦然。一旦生态系跨过有用服务器的临界质量, 不支援 MCP 的成本变得高于采纳它的成本。

## 关键采用者

MCP 采纳的广度说明它的主导:

- **OpenAI** 把 MCP 支援整合进 ChatGPT 平台与 Agents SDK, 让 GPT 模型能用任何 MCP 服务器。
- **Google DeepMind** 给 Gemini 加了 MCP 客户端支援, 引用生态系兼容性为主要动机。
- **Microsoft** 走最远, 在 Windows 的 OS 层级建 MCP 支援, 跨 Azure AI 服务、Copilot、GitHub Copilot 整合。
- **Amazon / AWS** 在 2026 年 4 月出货 **Bedrock AgentCore Runtime**, 第一个生产级双向 MCP runtime, 在标准协议上加 elicitation 与 sampling（见下方「有状态 MCP 转变」）。
- **GitHub** 把 Copilot extensions 系统重建在 MCP 上, 取代它们的专有工具格式。
- **Figma、Slack、Block、Notion** 全部出货官方 MCP 服务器, 让它们的平台成为任何 AI 工作流中的一等公民。
- **Hugging Face** 在它的模型 hub 旁边托管社群 MCP 服务器的 registry。
- **LangChain** 与其他编排框架提供原生 MCP 客户端支援, 让它成为默认工具整合方法。

**MCP 作为合成维度。** 一个微妙的 2026 年发展: MCP 工具选择开始作为自动 harness 合成系统中的*变量*之一出现, 而非固定基底。AgentFlow 论文（arXiv 2604.20801, 2026 年 4 月）把 agent 角色、prompt、*工具*、通讯拓扑、协调协议视为它合成回路搜寻的类型化图 DSL 的五个维度。对 MCP 觉知的 harness 设计者这是双面刃。MCP 的标准化让工具维度真正可搜寻——合成回路能用一个 MCP 服务器换另一个而不重写整合层。但同样的标准化让 MCP 服务器本身变成选择候选: 问题不再是「我装哪些服务器」而是「在可观测性压力下我的 harness *演化成用* 哪些服务器」。

## 与知识工程的连结

MCP 本身不是知识工程技术——它是让知识工程可扩展的基础设施层。本报告讨论的每个做法——RAG 管线、知识图、记忆系统、context engineering pattern——都需要把外部知识喂给模型。MCP 标准化这个喂法。

考虑一个实务例子: 一个增强了知识的 AI agent 需要存取公司 wiki、查询数据库、搜寻向量存储、读文件系统。没有 MCP, 每个整合都需要客制代码、客制认证、客制错误处理。有 MCP, 每个都是一个 MCP 服务器, agent 透过统一接口连到它们全部。

这是 MCP 对知识工程生态系核心的原因。它不取代 RAG 或记忆——它提供让它们跨模型与平台可组合、可移植、可互操作的管线工事。

## Meta-Tool Pattern

MCP 采纳浮现的最重要架构 pattern 之一是 Meta-Tool Pattern, 也叫工具的渐进式揭露。

问题: 当 MCP 生态系成长, 一个 agent 可能有数十或数百工具的存取权。把它们的 schema 全加载到 context window 是浪费的——大多数工具对任何给定任务无关。加载 29 个工具 schema, 你在模型永不会用的工具描述上烧数千 token, 你增加模型选错工具的机会。

解法: 不是前置加载所有工具 schema, 加载两个 meta-tool: **发现工具**让 agent 按描述搜寻相关工具, **执行工具**透过参照调用已发现工具。Agent 先发现当下任务有什么工具可用, 然后只加载它需要的 schema。

该 pattern 在工具密集环境减少 context window 消耗 80-90%, 透过减少决策空间改善工具选择准确度。它已成为任何含 10-15 个以上可用工具部署的最佳实务。

## 2026 挑战

尽管成功, MCP 面对显著的开放挑战:

**稽核轨迹。** 在企业环境, 每次工具调用需要日志、归属、合规追踪。当前 MCP 规格不规定稽核轨迹格式, 导致不一致实现。

**SSO 整合认证。** MCP 的认证故事自推出以来显著改善, 但跨完整客户端-服务器-传输链整合企业 SSO 系统（SAML、OIDC）仍摩擦重。最近批准的 MCP OAuth 2.1 流程处理这一些, 但采纳还在 rollout。

**Gateway 行为。** 当组织规模化部署 MCP, 它们需要 gateway 层做 rate limiting、存取控制、请求路由、监控。生态系缺少标准 MCP gateway 规格, 导致专有解法。

**配置可移植性。** MCP 服务器配置（连哪些服务器、用什么凭证、按什么顺序）没有标准化。在机器、团队、组织间移动 MCP 设置需要手动重新配置。

**工具描述质量。** MCP 的有效性完全依赖工具描述质量。描述差的工具导致错误调用。没有工具描述质量的标准、没有 linting、没有认证。

**Schema 版本控制。** 当 MCP 服务器更新它的工具 schema, 现存客户端可能坏。该协议缺内建版本控制与兼容性协商机制。

**工具重叠。** 数千社群服务器中, 多个服务器常提供重叠功能。该协议没去重或偏好表达机制。

## 2026：有状态 MCP 转变

整个头 18 个月, MCP 根本上是个 **无状态 RPC 协议**: 客户端调用服务器, 服务器返回结果, 对话继续。这模型对简单工具调用（读文件、查询 API、贴讯息）运作良好, 但对任何长期或互动东西挣扎。2026 年 4 月, 两个发展开始把 MCP 推向真正编排层。

**SEP-1686：Tasks Primitive。** 在 2026 年 4 月 MCP Dev Summit 引入, **SEP-1686** 给协议加了一个耐久任务状态机。每个长期工具调用变成一个有持续 ID 的 **task**, 状态有五种: `working`、`input_required`、`completed`、`failed`、`cancelled`。客户端能开始任务、断线、之后重连查状态或取结果——一个 **call-now / fetch-later** pattern。Task ID 与服务器送出的通知关联, 客户端能订阅进度事件而不必维持开放连线。该 primitive 直接瞄准 MCP 之前强迫客制 workaround 的工作流:

- 花数分钟到数小时完成的**数据管线**
- 跨大 repo 的**代码迁移**
- 完整 CI 套件的**测试执行**
- 衍生子 agent 与等外部 API 的**深度研究**
- 一个 agent 异步把工作交给另一个的**多 agent 系统**

SEP-1686 在 2026 年 4 月 MCP 规格中作为实验性出货。它是从无状态 RPC 迈向耐久、可恢复编排的第一个认真步骤。

**Amazon Bedrock AgentCore：第一个双向 runtime。** 也在 2026 年 4 月, AWS 出货 **Bedrock AgentCore Runtime**, 第一个实现 **双向** 沟通的生产 MCP runtime。标准 MCP 是客户端发起: 客户端调用工具, 服务器回应。AgentCore 加上两个服务器发起的能力:

- **Elicitation。** 执行中, 服务器能暂停并按 JSON schema 向用户请求结构化输入。这把先前需要客制 UI 层的多步工作流变成协议级互动。一个迁移工具能停下来问「我应该针对哪个分支？」配类型化回应。
- **Sampling。** 服务器能从客户端请求 LLM 生成完成, 而不必持有自己的模型凭证。服务器提供 prompt 与采样参数; 客户端跑自己的模型并返回完成。这让工具服务器做 LLM 驱动的工作（总结、分类、提取）, 同时用户的模型、配额、计费留在客户端。

一起, elicitation 与 sampling 完成 MCP 的双向协议表面。服务器现在能 **驱动** 部分对话, 不只对调用回应。

**含义。** 2025 年 MCP 的框架是「无状态工具的统一插头」。2026 年框架更广: MCP 正变成 **有状态、互动、双向 agent 编排** 的协议层。工具服务器不再被动——它们能持有耐久状态、暂停等用户输入、向客户端请求 LLM 工作。对知识工程, 这意味长期检索管线、分阶段数据丰富、人在回路工作流终于有原生协议跑在上面。

## 市场情境

行业分析师把 2025 年 AI 工具整合市场（MCP 是其中主导协议）预测在 18 亿美元, 当企业采纳加速时预期显著成长。这个数字包含 MCP 基础设施、服务器开发、gateway 服务、相关工具。

## 关键资源

- **[modelcontextprotocol.io](https://modelcontextprotocol.io)** ——官方规格、SDK、文档。
- **Anthropic MCP 课程** ——可在 [Skilljar](https://anthropic.skilljar.com) 与 [DeepLearning.AI](https://www.deeplearning.ai/short-courses/) 取得, 涵盖协议基础与服务器开发。
- **The New Stack** ——MCP 架构、采纳、挑战的持续技术报道。关于 meta-tool pattern 与企业部署 pattern 的著名文章。
- **MCP SDK 下载统计** ——npm（`@modelcontextprotocol/sdk`, [https://www.npmjs.com/package/@modelcontextprotocol/sdk](https://www.npmjs.com/package/@modelcontextprotocol/sdk)）与 PyPI（`mcp`, [https://pypi.org/project/mcp/](https://pypi.org/project/mcp/)）作为第一方采纳指标。

## 来源

1. Anthropic. "Introducing the Model Context Protocol."（2024 年 11 月）。https://www.anthropic.com/news/model-context-protocol
2. Model Context Protocol Specification. https://modelcontextprotocol.io
3. Linux Foundation. "Agentic AI Foundation Established."（2025）。https://www.linuxfoundation.org/press/agentic-ai-foundation
4. MCP SDK 下载统计, npm: [https://www.npmjs.com/package/@modelcontextprotocol/sdk](https://www.npmjs.com/package/@modelcontextprotocol/sdk) 与 PyPI: [https://pypi.org/project/mcp/](https://pypi.org/project/mcp/)（2026 Q1 累积约 9,700 万下载, 在次级报道中广为引用）。
5. The New Stack. "The Meta-Tool Pattern: Progressive Disclosure for AI Tools."（2025）。
6. Anthropic. MCP Course. Skilljar. https://anthropic.skilljar.com
7. DeepLearning.AI. "Building MCP Servers." https://www.deeplearning.ai/short-courses/
8. Microsoft. "MCP Support in Windows and Azure."（2025）。https://devblogs.microsoft.com
9. OpenAI. "Agents SDK: MCP Integration."（2025）。https://openai.com/index/new-tools-for-building-agents
10. AgentFlow / "Synthesizing Multi-Agent Harnesses for Vulnerability Discovery." arXiv 2604.20801（2026 年 4 月）。[https://arxiv.org/abs/2604.20801](https://arxiv.org/abs/2604.20801)

---

*上一章: [第 6 章 —— Agent Memory：缺失的层](06-agent-memory.md) | 下一章: [第 8 章 —— 工具地景：AI 原生知识管理](08-tools-landscape.md)*
