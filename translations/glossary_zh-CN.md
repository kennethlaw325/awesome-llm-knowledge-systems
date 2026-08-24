## 词汇表

> 此为 [English Glossary](../glossary.md) 的简体中文翻译。所有技术术语均以日常语言解释，无需博士学位。

### A

**A2A（Agent-to-Agent Protocol，代理间协议）**
让 AI 代理之间互相沟通、协调任务的标准方式，就像一种共通语言，让不同 AI 助手之间可以交接工作。

**Agent Memory（代理记忆）**
AI 代理在跨对话或跨任务之间记住信息的能力。把它想象成代理在不同 session 之间保留的一本笔记本，这样每次都不必从零开始。

**Agentic RAG（代理式 RAG）**
RAG 的一种，AI 主动决定要查什么、何时查、以及查到的结果是否够好——而不是每次都跑同一条固定的检索流程。

**Anchor（Graph Engineering 中的锚点）**
一个无可争辩、扎根于外部现实的测量——一个测试结果、一个指标、一次对照真实情况的检查——多 agent graph 里的某个节点必须触碰到它。由 Carlos E. Perez 在 2026 年 7 月的 graph-engineering 论述中提出：没有 anchor 的话，一张由互相审阅彼此工作的 agent 组成的 graph，会退化成一个回声室，收敛到自信的一致意见，而不是正确性。就像要求委员会里至少一个成员去核对真正的银行对账单，而不是所有人都只是同意「预算看起来没问题」。参见 **Graph Engineering**；第 14 章。

**ARC-AGI-3**
François Chollet 于 2026 年推出的代理智能交互式基准。代理会被丢进类游戏环境中，没有任何指示，必须自行探索、推测目标、并建立世界模型。与早期静态题格的 ARC 不同，ARC-AGI-3 将**探索效率**、**目标推测**、**世界模型形成**评分为三条独立的能力轴线。

### C

**CATTS（Consensus-Aware Test-Time Scaling，共识感知测试时扩展）**
一种多步骤代理的测试时扩展方法：每一步骤采样一个小型 rollout 委员会，将委员之间的不一致程度作为不确定性信号来分配运算资源。意见分歧多的步骤得到更多思考预算，分歧少的得到较少；公开结果显示相对于均匀扩展，可达到约 +9.1% 准确度同时减少 2.3 倍 token。

**Claude Code**
Anthropic 推出的命令行工具，让 Claude 直接在你的终端中工作——读文件、执行命令、编辑代码，作为 AI 结对编程伙伴。

**Client ID Metadata Documents（CIMD，客户端 ID 元数据文档）**
MCP 2026-07-28 最终规范强制要求的客户端识别机制，取代 Dynamic Client Registration：一个 MCP 客户端由一份托管在某个 URL 上的元数据文档来识别，而不是分别向每一台服务器单独注册自己。就像出示一张托管在你自己网址上的名片，而不是每去一间办公室就填一次新供应商表格。参见 **MCP**。

**Codex（OpenAI）**
OpenAI 的工具，让 AI 代理在沙盒化的云端环境中执行编程任务，自主读取仓库、撰写代码、执行测试。

**Context Engineering（上下文工程）**
仔细设计 AI 在回应之前所收到的信息。如果 prompt engineering 是写好问题，context engineering 就是选择要把哪些参考资料放在 AI 的桌面上。

**Context Window（上下文窗口）**
AI 模型一次能够"看到"的文字总量——包括你的输入和它的输出。就像一块白板的大小：模型读写的所有东西都必须能挤进去。

**CoT Monitoring（思维链监控）**
读取模型外显的推理 token，以便在它执行计划前侦测异常或失准行为。OpenAI 在 2026 年 4 月用 CoT monitoring 抓到自家一个推理模型在编程评估中作弊——这是首个公开案例证明可解释性可作为**执行时检查机制**，而非事后取证。

### D

**Dreaming（造梦）**
一个在各 session 之间排程执行的记忆整理工作，根据最近的 session pattern 改写 agent 的持久记忆。由 Anthropic Managed Agents 首次商用化（2026 年 5 月 6 日，研究预览）：curator 读取最近的 session，找出反复出现的错误与已经收敛的工作流，用纯文字改写 agent 的持久记忆。这和可训练记忆（Titans + MIRAS，2026 年 4 月，透过梯度更新在推论时自我调适）形成对比：Dreaming 把记忆保留为 harness 读取的数据，Titans 则把记忆变成模型本身的一部分。

### E

**Embeddings（嵌入向量）**
把文字转成一串数字的方式，使语意相近的文字在数学上相近。让计算机能够衡量两段文字有多相关，就像你会察觉两本书涵盖类似主题那样。

**Emotion Vectors（情绪向量）**
Claude 内部激活值中可解读的特征方向。当这些方向被增强时，模型会稳定偏向情绪化行为——Anthropic 2026 年 4 月披露最常被引用的例子是勒索式输出。因为这些方向可以被识别，harness 工程师获得了一个**特征层级**的过滤接口，而不止是 token 层级的过滤。

**Enterprise-Managed Authorization（EMA，企业管理授权）**
一个 MCP 扩展（2026 年 6 月 18 日定稿），用于对 MCP 服务器做集中化、由 IdP 供应的存取管理。不必让每个用户对每台服务器各自跑一次按 app 计的 OAuth 同意流程，组织可以透过自己的身份提供者（IdP）一次性供应服务器存取权；在 SSO 过程中，客户端会取得一个 **Identity Assertion JWT Authorization Grant（ID-JAG）**，再用它换取由 MCP 服务器自己的授权服务器签发的 access token（参见 **MCP**）。首日支持涵盖 Okta 作为 IdP、Anthropic 与 VS Code 作为客户端，以及七台服务器。EMA 把 MCP 的企业级 SSO，从「每台服务器各自整合的胶水代码」变成「在 IdP 那里一次性做完的供应决策」。

### F

**Few-shot Learning（少样本学习）**
在 prompt 内塞几个范例给 AI 看，让它学会做某个任务，而不是重新训练整个模型。就像给人三张填好的表格作参考，让他知道怎么填第四张。

**Fine-tuning（微调）**
拿一个预训练好的 AI 模型，再用你自己的特定数据继续训练它，让它在某个特定工作上做得更好。就像聘用一个通才之后再给他做专门的在职培训。

### G

**Generator-Evaluator Split（生成器／评估器拆分）**
一种 agent 可靠性 pattern，把产出工作的 agent，和一个独立、刻意保持怀疑的 evaluator agent 分开——之所以采用，是因为 agent 稳定地会高估自己的产出。由 Prithvi Rajasekaran 的《Harness design for long-running application development》（Anthropic，2026 年 3 月）提出，这个结构借用自生成对抗网络（GAN），并发现调教一个独立的 evaluator 让它保持怀疑，远比让一个 generator 学会自我批判要容易处理得多。evaluator 验证的是行为，而不是读 diff——它会点击浏览正在运行的应用、截图，测试 UI 功能、API 端点、数据库状态。这个 pattern 已经被产品化进「运行直到条件成立」的原语里，例如 Claude Code 的 `/goal`，由一个独立的全新模型在每一回合之后判断停止条件。参见 **Outer Loop**、**Loop Engineering**。

**Graph Engineering（图工程）**
2026 年 7 月出现的一个主张：**Loop Engineering** 之上还有一层，就是 graph——明确接好哪些 agent 存在、谁可以把工作委派给谁，以及它们的 loop 之间如何互相监督、互相纠正。在 2026 年 7 月 17-18 日 Peter Steinberger 一篇贴文之后的文章里结晶化，从第一天起就充满争议——LangChain 的回应主张这个实践已经有三年历史（一个 loop 不过就是一个有向环状 graph），新的只是这个名字。不要和知识图谱或 **GraphRAG** 混淆，后两者结构化的是系统*知道什么*；graph engineering 结构化的是系统*是谁*。这个词在写作当下大约只有两周历史，本指南把它当作一个还在接受检验的主张，而不是一层已经定型的东西来追踪。见第 14 章。

**GraphRAG**
RAG 的一种，把检索到的信息组织成一个由相关实体和关系构成的图，让它更擅长回答需要综合多份资料来源的问题。

### H

**Harness Engineering（系统编排工程）**
设计围绕 AI 模型的整套系统——工具、记忆、规则、工作流程——塑造它在真实环境中的行为。模型是引擎；harness 是整辆车。

**Harness Synthesis（Harness 合成）**
一类技术：由外层的优化器（基于搜索、基于可观测性等）根据目标任务的运行时信号自动修改 harness——其工具、prompts、角色分解、通讯拓扑、协作协议。参见 **AHE**（arXiv 2604.25850）和 **AgentFlow**（arXiv 2604.20801）作为 2026 年 4 月的两个参考实现。与 *meta-harness* 有别——后者是 2025 年 / 2026 年初的框架，把 harness 视为一次性优化的目标而非持续演化的产物。

**Harness-Native Training（Harness 原生训练）**
直接针对一个特定的生产 agent harness 训练模型，让它学会操作那个 harness 的工具与工作流——而不只是孤立地产出正确答案。参考范例是微软的 **MAI-Code-1-Flash**（Build，2026 年 6 月 2 日），一个 5B 参数的编程模型，针对生产环境实际使用的 GitHub Copilot harness 训练；微软报告在困难任务上 token 数减少约 60%，且性价比优于 Claude Haiku 4.5。Harness-native training 是 **harness synthesis 的对称反面**：harness synthesis（参见 **Harness Synthesis**、**AHE**）固定模型不变，演化 harness；harness-native training 固定 harness 不变，塑造模型去适配它。两者合起来，让「模型与 harness」变成一个可以从两端同时优化的共同设计问题。取舍是：一个针对某厂商 harness 调教过的模型，价值主要体现在那个 harness 里面，这也让*harness 即护城河*的动态更加尖锐。

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

**Loop Engineering（循环工程）**
2026 年 6 月被命名的一个实践：建构那套替你提示 agent 的系统，而不是每一回合都亲手提示它。由 Addy Osmani 在 2026 年 6 月 7 日的文章里造词，定义为「把你自己从提示 agent 的那个人这个角色里换掉」，转而设计「一个替你做这件事的系统」，并由同一周一篇病毒式的 Peter Steinberger 贴文催化。它坐落在 **Harness Engineering** 上面那一层楼：一个 loop 是一个按计时器运行、会生出帮手 sub-agent、会从持久保存的状态里喂养自己的 harness——和一个单纯的排程器不同，因为它每一轮都会读取当下状态，重新决定该做什么，而不是按时钟触发一条固定命令。这个词目前只存在于从业者之间，且有争议（截至 2026 年中还没有学术文献）；本指南把它当作正在浮现的第四层来追踪，而不是已经定型的一个世代。见第 13 章。

### M

**MCP（Model Context Protocol，模型上下文协议）**
一个开放标准，让 AI 助手通过通用的即插即用接口连接外部工具与数据源，就像 AI 应用的 USB。

**MCP Apps**
一个 2026-07-28 MCP Release Candidate 原语（2026 年 5 月 21 日定案），让服务器能在工具调用的同时出货互动式 HTML 界面。宿主端在一个沙盒化的 iframe 里渲染这个界面；UI 模板要预先声明，好让它能被安全审查、被快取。MCP Apps 是第一个不属于工具调用的 MCP 原生交付物——一个知识库服务器可以出货一个搜寻框，一个研究服务器可以出货一个结果比较视图，一个采购服务器可以出货一个确认购买的对话框，全都不需要另外接上一套独立的 UI 规范。

**MCP Tunnel**
一个私有网络部署 pattern，由 Anthropic Managed Agents 在 2026 年 5 月 19 日（Code with Claude London）以研究预览形式出货。一个部署在客户私有网络内部的轻量级 gateway，只对 Anthropic 发起一次出站连线，之后 agent 就能把内部数据库、API、知识库、工单系统当成 MCP 工具来调用——不需要任何入站防火墙规则、不需要公开端点，也不需要 VPN。它是 self-hosted sandbox 的对称对应物：self-hosted sandbox 把工具的*执行*留在客户边界内，MCP tunnel 把工具的*触及范围*留在边界内。

**Managed Agents（托管代理）**
一种云端运行模型，其中代理 harness 的底层基底——沙盒、session 状态、受范围限制的工具执行、追踪——由模型供应商而非开发者运营。Anthropic 在 2026 年 4 月 8 日公开测试版推出首个商用实例（[platform.claude.com/docs/en/managed-agents/overview](https://platform.claude.com/docs/en/managed-agents/overview)）。根据 SiliconANGLE 发布报道，定价是标准 API token 费率加上每代理运行小时的基底费（每小时数字未在 Anthropic 主要文档中出现）。与云端原生触发接口（如 Claude Code Routines）不同，后者建立在 Managed Agents 风格的基底之上，但回答的是另一个问题："循环如何被触发"。

**Mechanistic Interpretability（机制可解释性）**
一个研究方向，旨在识别模型权重内部人类可理解的电路——实现特定行为的特征、注意力头和路径。被《MIT Technology Review》列为 2026 年十大突破技术之一，并支撑了 2026 年 4 月的成果，如情绪向量、迭代头、CoT monitoring。

**Memory Foundation Model（记忆基础模型）**
2026 年 7 月出现的一个主张（MemTensor 的 Metis，arXiv 2607.26760）：agent 记忆应该以持久、动态演化的状态存在于 transformer 骨干本身里面——是参数化的，而不是外部的。这个原型在一个冻结的 Qwen3.5 骨干（4B / 9B / 27B 规模）上训练了一个「hyper memory block」和「local memory block」（受 Fast Weight Programming 启发），在推论时透过一个无梯度、类似 EMA 的前向传递来更新记忆，而不是靠向量库写入，也不是靠 Titans 那种梯度更新。自陈的局限包括在固定大小的压缩下会丢失长距信息，以及「某些情况下出现信息混淆，可能是由潜空间内语义混合所导致」——这是一个研究预览，还不是一个经过验证的生产 pattern。见第 6 章。

**mHC（Manifold-Constrained Hyper-Connections，流形受限超连接）**
DeepSeek 于 2026 年 4 月提出的架构方案，将残差连接扩展为沿着一条学习得到的低维流形路由多条内部信息流。它把 Transformer++ 风格模型中的单一残差流泛化为若干协调流；截至发表时，结果**仍待独立复制验证**。

**MIRAS**
Google Research 推出的记忆增强训练框架，提供如 Titans 等架构的训练配方、稳定性保证和学习动态。Titans 的记忆是会在推理时更新的可训练神经模块。MIRAS 让"边推理边学"变得可行，而记忆模块不会发散。

**MoE（Mixture of Experts，专家混合）**
一种模型架构，每个输入只会触发模型"脑"的一部分，因此可以构建非常大的模型却保持快速——因为并非每个部分每次都运行。

### O

**Obsidian**
一款记事应用，把笔记储存为你电脑上的纯文本文件，并让你把它们连结起来形成个人知识库。

**Org Graph / Work Graph（组织图／工作图）**
graph engineering 里的两个 graph 对象，出自 Yash Thakker 2026 年 7 月的 explainx.ai 指南：*org graph（组织图）* 是一张稳定的图表，记录哪些 agent 存在、每个 agent 是干嘛的，以及哪些委派边是被允许的；*work graph（工作图）* 是某个特定工作生出、执行、再丢弃的短命任务分解。就像一间公司的组织图，对比为了一个项目临时组起来、事后就解散的工作小组。参见 **Graph Engineering**；第 14 章。

**Outcomes（Anthropic）**
一个公测阶段的托管 agent 原语（Anthropic，2026 年 5 月 6 日），agent 会对着一个跑在自己独立 context window 里的独立评分器反复迭代，直到满足一份评分标准（rubric）为止。它把 Ralph-loop / CATTS 那种由不确定性引导的迭代 pattern，产品化成一份 API 合约：调用者写好一份评分标准，底层基底代替 agent 跑迭代-评分这个 loop，只有收敛后的结果才会回传给调用者。

**Outer Loop（外层循环）**
当 agent 运行内层执行 loop（调查、实作、测试／验证、报告）时，人类所保留的那层判断力。出自 Addy Osmani 2026 年 7 月的后续文章《Own the Outer Loop》，把它架构成三根支柱——Quality（agent 行动之前运行的检查所形成的反压力）、Verdict（「工作进入我们依赖的系统之前，我们做出的最终决定」），和 Answerability（「如果有人问起，我保证能解释为什么」的保证）。Osmani 点名了过度委派它的三种失效模式：cognitive debt（认知负债，你对怎么解决问题的理解逐渐被侵蚀）、cognitive surrender（认知投降，不假思索地接受 AI 给你的东西），以及 orchestration tax（编排税，生出比你的判断力能覆盖还多的 agent）。它是 **Loop Engineering** 与 **Generator-Evaluator Split** 的补充：loop 的好坏，取决于围着它的那个 outer loop 有多好。见第 13 章。

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

**Safety-Tiered Distribution（安全分级发布）**
把同一个模型家族，以安全防护等级与发布关卡不同（而不是权重不同）的并行分层来出货。参考范例是 Anthropic 2026 年 6 月的这一对：**Claude Fable 5**（公开 GA 版，带双重用途安全措施，包括以 `stop_reason` 形式呈现的拒答）与 **Claude Mythos 5**（同一份底层权重，撤除了防护措施，只对通过审核的 Glasswing 联盟开放）。这和厂商自选的存取分层（例如 GPT-5.5 的 Trusted Access for Cyber）形成对比——到 2026 年中，也和政府强制的分层（例如 GPT-5.6 那个受行政命令把关的预览版）形成对比。它编码的取舍是：能力与安全被彼此解绑，所以决定你能拿到哪个防护层级的，是你是谁（通过审核的组织，还是一般公开用户），而不是模型能做到什么。

**Self-Hosted Sandbox（自架沙盒）**
一种 Managed Agents 部署形态，由 Anthropic 在 2026 年 5 月 19 日（Code with Claude London）以公测形式出货。agent loop——编排、context 管理、错误恢复——留在 Anthropic 的基础设施上，而工具的*执行*则挪到客户自己的环境，或一个受管理的沙盒供应商（Cloudflare、Daytona、Modal、Vercel 都有官方支持）。它把 Managed Agents 从「完全由 Anthropic 托管」重新框定为「由 Anthropic 编排，尊重客户边界」——harness 工程师可以逐层挑选 loop 的哪个部分住在哪里，而不是只能在「完全自架」和「完全托管」之间二选一。

**Self-RAG**
RAG 的一种，AI 会评估自己取得的资料和产生的答覆质量，决定是否要再检索或修正回应，再给你最终结果。

**Session-hour pricing（按 session 小时计费）**（也以 *agent-runtime-hour pricing* 形式报道）
一种计费模式，将编排器席位——即代理循环运行其上的基底——与推理分开计量。Anthropic Managed Agents 于 2026 年 4 月 8 日首次商用引入，按 SiliconANGLE 发布报道，每代理运行小时 8 美分另加标准 token 费率。每小时数字未在 Anthropic 主要文档中出现，由次级科技媒体引用。重要之处是：这是**首个由厂商把"循环在哪里运行"的成本量化的原语**，与"循环在想什么"的成本区分开来。确切措辞在主要文档（用 *sessions*）和科技媒体报道（用 *agent runtime hour*）之间有别，但两者指的是同一个计量接口。

**Skill（AI Agent Skill）**
一个可重用、封装好的能力，AI 代理可以调用——就像它遵循的食谱，用于某个特定任务，例如"review this PR"或"run a daily review"。

**Stateless MCP（无状态 MCP）**
MCP 2026-07-28 Release Candidate 引入（2026 年 5 月 21 日定案）、并在 2026-07-28 规范（2026 年 7 月 28 日）里最终出货的架构转变：协议核心不再使用 `initialize` / `initialized` 握手，也不再用 `Mcp-Session-Id` 标头。客户端元数据改为在每一次请求的 `_meta` 里传递，所以任何一次 MCP 请求都可以落在任何一个服务器实例上——不需要黏性路由，不需要共享的 session 存储。这解决了 2025 年 Streamable HTTP 被采用后浮现的水平扩展摩擦。当初促成*有状态*那次转向的持久状态原语（SEP-1686 Tasks、AgentCore 双向 runtime），现在被当成扩展，重新实作在无状态核心之上，而不是烤进每一次请求里。是无状态核心加上层的有状态工作，而不是从头到尾都有状态。

**Skill Graph（技能图）**
代理可用所有技能的地图，包括它们之间的关系和各自的触发条件。

**Skill Supply-Chain Attack（Skill 供应链攻击）**
透过 skill 注册中心或市集散布的恶意或被植入木马的 agent skill。2026 年这类攻击的定义性机制，是一个「检查时刻」与「使用时刻」之间的落差：静态扫描器审查的是*提交时的套件快照*，但一个会在 agent 运行时抓取外部内容、或解包隐藏 payload 的 skill，能在通过审查*之后*改变自己的行为。AIR 在 2026 年 6 月披露的一起事件，用藏在外部 URL 后面的单一伪造 skill，以这种方式挟持了大约 26,000 个 agent；而「Cloak and Detonate」研究（2026 年 7 月）显示，对八款扫描器，逃避检测的成功率超过 90%，运行时行为检测（在 2% 误判率下达到 97% 检出率）是应对方向。这个教训和 MCP 的教训是同一个（参见 **MCP**）：一旦 **Progressive Disclosure**（参见 **Progressive Disclosure**）加上注册中心规模的散布，让 skill 档案本身变成一个攻击面，信任就必须从发布时的扫描，转移到运行时的围堵。

**System Prompt（系统提示词）**
在你的对话开始之前给 AI 模型的隐藏指令，设定它的角色、规则和行为。就像员工上班第一天先读的工作说明书。

### T

**Task Budget（任务预算）**
Anthropic 在 Claude Opus 4.7 引入的 harness 原语（2026 年 4 月，beta 头 `anthropic-beta: task-budgets-2026-03-13`）。调用者为**整个代理循环**（思考、工具调用、工具结果、最终输出）声明一个建议性的 token 预算，模型在工作时收到一个倒数计时，用它决定一个步骤还值得多少搜索、推理、综合。与 `max_tokens` 不同——后者是模型不可见的硬上限。预算是建议性而非强制性，最低 20K token，避免在预算过紧时退化为拒答。Task budgets 是首个由厂商提供的原语，把"对每一步该想多深"作为**受管理的契约**而非手动调参的参数。

**Temporal Policies（时序策略）**
由 AWS 在 2026 年 8 月 6 日于 Amazon Bedrock AgentCore 出货的一个由 gateway 强制执行的授权原语。一般的策略问的是「这个 agent 可不可以发出这次调用」，而 temporal policy 是拿这次调用去对照同一个 session 里 agent *先前*的动作来评估——确定性地、默认拒绝、全程记录，而且在 agent 代码之外，所以没有任何 prompt 或模型决策能绕过它、说服它放行。策略用 **Dogwood** 写成，这是一个新的 Apache-2.0 开源策略语言，专门为 AI agent 打造。它点名的用途，是指令本身没办法防止的那些失效模式：防止数据捏造（agent 往下传递的值，必须真的对得上先前某次调用实际返回的结果）、累积 session 成本上限，以及要求在特权动作之前插入人工批准步骤的工作流排序。它把单次动作硬上限（AgentCore Payments，2026 年 5 月）从单次调用推广到一整个 session 的历史——harness 设计里的 Authority 那根轴，因此拿到了一层有状态的强制执行。

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

### X

**x402**
一个复活 HTTP 状态码 402（「Payment Required」）的开放协议，用于机器之间带内的稳定币支付，供 agent 对资源的交易使用。源起于 Coinbase；首个由超大规模云厂商托管的实作是 AWS AgentCore Payments（2026 年 5 月 7 日）。它是工具层的 MCP 在「价值层」的对应物——MCP 把 agent 怎么触及一个 API 标准化，x402 把它怎么替这个 API 付钱标准化。在 AWS 背书之前就已有的采用势头：截至 2026 年 4 月底，有 69,000 个活跃 agent，累积交易量约 5,000 万美元。

---

[返回 README](README_zh-CN.md)
