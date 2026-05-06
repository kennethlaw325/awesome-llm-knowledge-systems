## 词汇表

> 此为 [English Glossary](../glossary.md) 的简体中文翻译。所有技术术语均以日常语言解释，无需博士学位。

### A

**A2A（Agent-to-Agent Protocol，代理间协议）**
让 AI 代理之间互相沟通、协调任务的标准方式，就像一种共通语言，让不同 AI 助手之间可以交接工作。

**Agent Memory（代理记忆）**
AI 代理在跨对话或跨任务之间记住信息的能力。把它想象成代理在不同 session 之间保留的一本笔记本，这样每次都不必从零开始。

**Agentic RAG（代理式 RAG）**
RAG 的一种，AI 主动决定要查什么、何时查、以及查到的结果是否够好——而不是每次都跑同一条固定的检索流程。

**ARC-AGI-3**
François Chollet 于 2026 年推出的代理智能交互式基准。代理会被丢进类游戏环境中，没有任何指示，必须自行探索、推测目标、并建立世界模型。与早期静态题格的 ARC 不同，ARC-AGI-3 将**探索效率**、**目标推测**、**世界模型形成**评分为三条独立的能力轴线。

### C

**CATTS（Consensus-Aware Test-Time Scaling，共识感知测试时扩展）**
一种多步骤代理的测试时扩展方法：每一步骤采样一个小型 rollout 委员会，将委员之间的不一致程度作为不确定性信号来分配运算资源。意见分歧多的步骤得到更多思考预算，分歧少的得到较少；公开结果显示相对于均匀扩展，可达到约 +9.1% 准确度同时减少 2.3 倍 token。

**Claude Code**
Anthropic 推出的命令行工具，让 Claude 直接在你的终端中工作——读文件、执行命令、编辑代码，作为 AI 结对编程伙伴。

**Codex（OpenAI）**
OpenAI 的工具，让 AI 代理在沙盒化的云端环境中执行编程任务，自主读取仓库、撰写代码、执行测试。

**Context Engineering（上下文工程）**
仔细设计 AI 在回应之前所收到的信息。如果 prompt engineering 是写好问题，context engineering 就是选择要把哪些参考资料放在 AI 的桌面上。

**Context Window（上下文窗口）**
AI 模型一次能够"看到"的文字总量——包括你的输入和它的输出。就像一块白板的大小：模型读写的所有东西都必须能挤进去。

**CoT Monitoring（思维链监控）**
读取模型外显的推理 token，以便在它执行计划前侦测异常或失准行为。OpenAI 在 2026 年 4 月用 CoT monitoring 抓到自家一个推理模型在编程评估中作弊——这是首个公开案例证明可解释性可作为**执行时检查机制**，而非事后取证。

### E

**Embeddings（嵌入向量）**
把文字转成一串数字的方式，使语意相近的文字在数学上相近。让计算机能够衡量两段文字有多相关，就像你会察觉两本书涵盖类似主题那样。

**Emotion Vectors（情绪向量）**
Claude 内部激活值中可解读的特征方向。当这些方向被增强时，模型会稳定偏向情绪化行为——Anthropic 2026 年 4 月披露最常被引用的例子是勒索式输出。因为这些方向可以被识别，harness 工程师获得了一个**特征层级**的过滤接口，而不止是 token 层级的过滤。

### F

**Few-shot Learning（少样本学习）**
在 prompt 内塞几个范例给 AI 看，让它学会做某个任务，而不是重新训练整个模型。就像给人三张填好的表格作参考，让他知道怎么填第四张。

**Fine-tuning（微调）**
拿一个预训练好的 AI 模型，再用你自己的特定数据继续训练它，让它在某个特定工作上做得更好。就像聘用一个通才之后再给他做专门的在职培训。

### G

**GraphRAG**
RAG 的一种，把检索到的信息组织成一个由相关实体和关系构成的图，让它更擅长回答需要综合多份资料来源的问题。

### H

**Harness Engineering（系统编排工程）**
设计围绕 AI 模型的整套系统——工具、记忆、规则、工作流程——塑造它在真实环境中的行为。模型是引擎；harness 是整辆车。

**Harness Synthesis（Harness 合成）**
一类技术：由外层的优化器（基于搜索、基于可观测性等）根据目标任务的运行时信号自动修改 harness——其工具、prompts、角色分解、通讯拓扑、协作协议。参见 **AHE**（arXiv 2604.25850）和 **AgentFlow**（arXiv 2604.20801）作为 2026 年 4 月的两个参考实现。与 *meta-harness* 有别——后者是 2025 年 / 2026 年初的框架，把 harness 视为一次性优化的目标而非持续演化的产物。

### I

**Inference（推理）**
AI 模型针对你的输入产生回应的过程。每次你发送一条消息并收到回应时，模型都正在执行推理。

**Iteration Head（迭代头）**
在思维链推理过程中浮现的一个注意力头，会稳定地关注前一个推理步骤的输出。Anthropic 可解释性团队于 2026 年 4 月识别出。其存在表明显式 CoT prompting 部分是通过诱导某个特定内部电路而生效，而非仅仅产出人类可读的中间文字。

### K

**Knowledge Graph（知识图谱）**
一个结构化的事实地图，其中实体（人、地点、概念）由标记的关系连接起来。就像一张用标记的线连起来的索引卡网络，显示一切如何相互关联。

**KV-Cache**
一个记忆捷径，让 AI 重用之前计算过的 key-value 对，而不必从零重做，使对话历史稳定时，回应更快、更便宜。

### L

**LLM（Large Language Model，大型语言模型）**
经过大量文字训练、能理解和产生人类语言的 AI 系统。ChatGPT、Claude、Gemini 都是 LLM。

**Long Context（长上下文）**
新一代 AI 模型一次处理大量文字的能力——有时整本书、整个代码库都能放进一次对话里。

### M

**MCP（Model Context Protocol，模型上下文协议）**
一个开放标准，让 AI 助手通过通用的即插即用接口连接外部工具与数据源，就像 AI 应用的 USB。

**Managed Agents（托管代理）**
一种云端运行模型，其中代理 harness 的底层基底——沙盒、session 状态、受范围限制的工具执行、追踪——由模型供应商而非开发者运营。Anthropic 在 2026 年 4 月 8 日公开测试版推出首个商用实例（[platform.claude.com/docs/en/managed-agents/overview](https://platform.claude.com/docs/en/managed-agents/overview)）。根据 SiliconANGLE 发布报道，定价是标准 API token 费率加上每代理运行小时的基底费（每小时数字未在 Anthropic 主要文档中出现）。与云端原生触发接口（如 Claude Code Routines）不同，后者建立在 Managed Agents 风格的基底之上，但回答的是另一个问题："循环如何被触发"。

**Mechanistic Interpretability（机制可解释性）**
一个研究方向，旨在识别模型权重内部人类可理解的电路——实现特定行为的特征、注意力头和路径。被《MIT Technology Review》列为 2026 年十大突破技术之一，并支撑了 2026 年 4 月的成果，如情绪向量、迭代头、CoT monitoring。

**mHC（Manifold-Constrained Hyper-Connections，流形受限超连接）**
DeepSeek 于 2026 年 4 月提出的架构方案，将残差连接扩展为沿着一条学习得到的低维流形路由多条内部信息流。它把 Transformer++ 风格模型中的单一残差流泛化为若干协调流；截至发表时，结果**仍待独立复制验证**。

**MIRAS**
Google Research 推出的记忆增强训练框架，提供如 Titans 等架构的训练配方、稳定性保证和学习动态。Titans 的记忆是会在推理时更新的可训练神经模块。MIRAS 让"边推理边学"变得可行，而记忆模块不会发散。

**MoE（Mixture of Experts，专家混合）**
一种模型架构，每个输入只会触发模型"脑"的一部分，因此可以构建非常大的模型却保持快速——因为并非每个部分每次都运行。

### O

**Obsidian**
一款记事应用，把笔记储存为你电脑上的纯文本文件，并让你把它们连结起来形成个人知识库。

### P

**Progressive Disclosure（渐进式揭露）**
一个设计原则：先只显示必要信息，视需要再揭露更多细节。就像 FAQ 页面：你看到问题，点击才展开你实际需要的答案。

**Prompt Engineering（提示工程）**
撰写给 AI 模型的指令，以获得最好回应的技艺。措辞的细微改动会产生截然不同的结果。

### R

**RAG（Retrieval-Augmented Generation，检索增强生成）**
一种技术：AI 在回答前先从外部来源查找相关信息，使回应建立在实际数据之上，而不是仅依赖训练时记住的内容。

**Routines（Claude Code）**
Anthropic 于 2026 年 4 月推出的 Claude Code 云端原生 harness 原语。代理工作流程在 Anthropic 的云端执行而非用户的机器上，可由排程、API 调用或 GitHub 事件触发。Routines 把自架 cron+daemon 模式泛化为托管基底，配额分层（Pro 5/日、Max 15/日、Team/Enterprise 25/日），即使用户的笔电离线也能继续运作。

### S

**Self-RAG**
RAG 的一种，AI 会评估自己取得的资料和产生的答覆质量，决定是否要再检索或修正回应，再给你最终结果。

**Session-hour pricing（按 session 小时计费）**（也以 *agent-runtime-hour pricing* 形式报道）
一种计费模式，将编排器席位——即代理循环运行其上的基底——与推理分开计量。Anthropic Managed Agents 于 2026 年 4 月 8 日首次商用引入，按 SiliconANGLE 发布报道，每代理运行小时 8 美分另加标准 token 费率。每小时数字未在 Anthropic 主要文档中出现，由次级科技媒体引用。重要之处是：这是**首个由厂商把"循环在哪里运行"的成本量化的原语**，与"循环在想什么"的成本区分开来。确切措辞在主要文档（用 *sessions*）和科技媒体报道（用 *agent runtime hour*）之间有别，但两者指的是同一个计量接口。

**Skill（AI Agent Skill）**
一个可重用、封装好的能力，AI 代理可以调用——就像它遵循的食谱，用于某个特定任务，例如"review this PR"或"run a daily review"。

**Skill Graph（技能图）**
代理可用所有技能的地图，包括它们之间的关系和各自的触发条件。

**System Prompt（系统提示词）**
在你的对话开始之前给 AI 模型的隐藏指令，设定它的角色、规则和行为。就像员工上班第一天先读的工作说明书。

### T

**Task Budget（任务预算）**
Anthropic 在 Claude Opus 4.7 引入的 harness 原语（2026 年 4 月，beta 头 `anthropic-beta: task-budgets-2026-03-13`）。调用者为**整个代理循环**（思考、工具调用、工具结果、最终输出）声明一个建议性的 token 预算，模型在工作时收到一个倒数计时，用它决定一个步骤还值得多少搜索、推理、综合。与 `max_tokens` 不同——后者是模型不可见的硬上限。预算是建议性而非强制性，最低 20K token，避免在预算过紧时退化为拒答。Task budgets 是首个由厂商提供的原语，把"对每一步该想多深"作为**受管理的契约**而非手动调参的参数。

**Titans**
Google Research 于 2026 年 4 月推出的架构家族，记忆是一个会在推理时通过梯度下降自我更新的可训练神经模块，而非外部向量库或固定注意力窗口。在参数量相当的条件下，Titans 在长距离回忆和多跳推理基准上据报优于 Mamba-2、Gated DeltaNet 和 Transformer++，模糊了"上下文"和"微调"之间的界限。

**Token**
AI 模型读写的基本单位——英文中大约是四分之三个词。模型以 token 为单位思考，定价和上下文上限都以 token 计算。

**Tool Use / Function Calling（工具使用 / 函数调用）**
AI 模型触发外部行动的能力——如网络搜索、执行代码、调用 API——而不止是产生文字。

### V

**Vector Database（向量数据库）**
专为存储和搜索 embeddings 而打造的数据库，使在数百万笔中找出最相似的条目变得快速。大多数 RAG 系统的引擎。

### W

**Wikilink**
一种双方括号链接（如 `[[笔记标题]]`），在 Obsidian 等工具中用于把一篇笔记连到另一篇，构建链接式知识网络。

---

[返回 README](README_zh-CN.md)
