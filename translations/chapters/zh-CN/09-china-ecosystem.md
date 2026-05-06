# 第 9 章：中国 AI 知识工程地景

> **一句话总结：** 中国建出一套平行 AI 生态系, 配自己的开源平台、模型、社群——常常朝与西方不同的方向创新。
>
> **为什么重要：** 全球一半的 AI 研究者在中国。忽略这个生态系意味错过一半的创新。

![中国 vs. 西方 AI 知识工程](../../../diagrams/china-comparison.png)

关于 LLM 知识工程的全球对话, 不检视中国生态系就不完整。截至 2025 年 12 月已向监管机构申报超过 748 项 AI 服务, 中国发展出一套平行——某些领域且发散——的方法来用大型语言模型建知识系统。本章绘制塑造中国开发者与企业如何处理知识工程的关键平台、模型、文化差异。

## A. 开源 RAG 与 Agent 平台

中国开源 AI 生态系产生几个在 GitHub 流行度上匹敌或超越西方对手的平台。这些项目的特征是它们对视觉化工作流、企业部署就绪度、深度文件理解的强调——反映中国企业客户的实务需求。

### Dify（136K+ GitHub Stars）

[Dify](https://github.com/langgenius/dify) 是全球最多 star 的 agentic AI 平台。Apache 2.0 授权, 它提供视觉画布建构 RAG 管线、agentic 工作流、多步推理链。从 1.0 版起 Dify 支援 Model Context Protocol（MCP）, 让外部工具服务器能无缝整合。它的强项在于桥接视觉设计工作流的无代码用户与需要程式化控制的开发者之间的差距。企业用户能自架整个堆叠, 这在数据主权要求常排除仅云端解法的中国市场关键。

### RAGFlow（62-75K+ GitHub Stars）

[RAGFlow](https://github.com/infiniflow/ragflow) 透过深度文件理解差异化。不是把文件当扁平文字处理, RAGFlow 跨 20+ 文件格式（包括扫描 PDF、试算表、投影片）应用版面感知解析、OCR、表格提取。它的「agentic RAG」做法意味系统能根据查询类型自主决定要应用哪种检索策略。对处理遗留文件库的企业——中国国营企业与制造公司常见的情境——这能力不是 nice-to-have 而是要求。

### FastGPT（27K+ GitHub Stars）

[FastGPT](https://github.com/labring/FastGPT) 瞄准企业知识库 Q&A, 聚焦在资源效率。它的 QA 对提取管线自动把文件转成 question-answer 对, 然后能用于检索与微调。该平台被设计成能在低至 2GB RAM 的机器上跑, 让请不起专用 GPU 基础设施的中小企业能存取。这个节俭反映中国生态系的更广 pattern: 在约束下的优化。

### MaxKB（18K+ GitHub Stars）

[MaxKB](https://github.com/1Panel-dev/MaxKB) 把自己定位为配一键部署的企业 agent 平台。它支援 MCP 做工具整合, 并为常见企业情境提供预建模板: 客服、内部知识检索、文件总结。它的吸引力在于把「我们要个 AI 助手」到「我们有一个在跑」的时间从数周缩到数小时。

### Coze Studio（15K+ GitHub Stars, ByteDance）

[Coze Studio](https://github.com/coze-dev/coze-studio) 是 ByteDance 的开源视觉 agent 开发平台。原本是闭源产品, ByteDance 在 2025 年 7 月开源它, 三天内累积 10,000 GitHub stars——既证明压抑需求也证明 ByteDance 的分发力。Coze Studio 提供拖放接口建 agent, 含内建记忆、工具使用、多轮对话管理。它与 ByteDance 的豆包模型家族整合给它在中文任务上原生优势。

### DB-GPT（17K+ GitHub Stars）

[DB-GPT](https://github.com/eosphoros-ai/DB-GPT) 专精在 AI 原生数据互动。它的核心能力是自然语言转 SQL 转换, 让非技术用户能对话式查询数据库。它用视觉化生成与多 agent 数据分析管线延伸这。对坐拥大型结构化数据集的企业——这描述大多数中国金融、物流、制造公司——DB-GPT 提供 AI 增强分析的可亲入口。

## B. 中国 LLM 的知识管理

中国基础模型地景已快速成熟, 几个模型现在在特定基准上与西方对手竞争或胜过。

### Qwen3（阿里云）

Qwen3 是阿里的旗舰模型家族。最大变体是 2,350 亿参数 Mixture of Experts（MoE）模型, Apache 2.0 授权发布。Qwen3-Coder-480B, 编程专门化变体, 支援 256K 到 1M token 的上下文窗口。Apache 2.0 授权策略性重要: 它启用无限制商用, 推动跨负担不起专有 API 成本中国创业公司的采纳。Qwen 的多语言能力在中文、日文、韩文上特别强——这些语言西方模型历史上表现差。

### DeepSeek R1

DeepSeek R1 在数学与科学推理基准上与 OpenAI 的 o1 持平, 同时 MIT 授权发布。该模型据报训练成本不到 600 万美元, 是可比西方模型的小部分。这个成本效率在行业引发震荡: R1 发布后数月, 中国企业开源模型采纳率从 23% 跳到 67%。DeepSeek R1 证明前沿级推理不需前沿级预算, 根本上转移知识工程的经济学。

2026 年 4 月, DeepSeek 用 **流形受限超连接（mHC）** 延伸它的架构贡献, 这是 Transformer++ 风格模型用的残差连接的泛化。当标准残差流跨层向前携带单一通道信息, mHC 携带 **多个内部流**, 每个被约束在一个学到的低维流形上。这个构造被设计来给后期层更丰富存取早期表示, 而不受简单多流残差在规模上承受的维度崩塌。DeepSeek 的博客在参数量相当下报告长程推理基准上的增益, 在信息必须跨许多中间层携带的任务上有最大改进。截至 2026 年 4 月, 该结果应被 **标记为等独立复制**——这是单一实验室对单一实验室模型的披露, 而该领域在没经过第三方再现的架构主张上吃过亏。如果结果成立, mHC 加入 MoE、MLA、DeepSeek 早期 multi-token prediction 工作, 成为在中国开源权重生态系起源后跨入主流使用的第三或第四个架构 primitive。

### DeepSeek V4（2026 年 4 月）

DeepSeek 的 **V4 preview**（2026 年 4 月 24 日）在三轴同时延伸 R1 叙事: 经济学、能力、**推论基底**。该发布在 Hugging Face 以 MIT 授权出货两个开源权重 Mixture-of-Experts 模型——**V4-Pro 1.6 万亿参数 / 49B 活跃**、**V4-Flash 284B / 13B 活跃**——配 100 万 token 上下文窗口作为默认而非分层。API 定价是 2026 年任何前沿级模型最激进: **V4-Flash 每百万输出 token $0.28**、V4-Pro $3.48, 反映 V4 比 V3 **每 token 推论 FLOPs 减少 73%**, 由架构变更驱动而非仅硬件优化。在编程基准上——R1 首先建立信誉的领域——V4-Pro 拿下排行榜首, **LiveCodeBench 93.5%**（领先 Gemini 3.1 Pro 91.7% 与 Claude Opus 4.6 88.8%）和 **Codeforces 评分 3206**（超越 GPT-5.4 3168）。

但对本章最重要的结构细节, 不是定价或基准, 而是 **推论基底**。训练 V4 用了含 NVIDIA A100 与 H20 硬件的混合集群——前沿*训练*能否完全在 NVIDIA 堆叠外发生的问题仍困难。但模型 **day-zero 适配 Huawei Ascend 950PR**, DeepSeek 与 Huawei 联合报告在为模型生产服务上 Ascend NPU 与 NVIDIA H20 GPU 之间的 **推论对等——在这个架构上, 约 2.8 倍运算吞吐**。这是主权硅论点的微妙形式: 不是「我们没用 NVIDIA 训练」而是 **「我们没用 NVIDIA 服务」**。对面对美国出口管制的中国企业客户, V4 是首次有前沿级开源权重模型在 day-one 就有可信的国产硅服务路径——对本章一直在描述的部署重的中国生态系, 这比训练可选性更接近承重约束。读在 R1 2025 年 1 月拐点旁边, V4 关闭一个一年的故事弧线: 中国开源权重生态系现在能在同一天发布前沿编程模型 **与** 为它服务的基底。

### Kimi K2.5（Moonshot AI）

Kimi K2.5 引入「Agent Swarm」——一个能力, 单一查询能 spawn 至多 100 个子 agent, 透过约 1,500 次工具调用协作。这不是研究 demo; 它是用于复杂研究任务的生产功能, 系统并行 web 搜寻、文件分析、跨数十并发 agent 综合。早些时候, Kimi 达到 200 万中文字符上下文窗口（约 2025 年 3 月）, 让它成为针对中文优化的最长 context 模型。

### ERNIE 5.0（百度）

ERNIE 5.0 是百度的 2.4 万亿参数模型, 配原生全模态支援——单一模型内的文字、图像、声音、视频理解与生成。2026 年 1 月推出, 它代表百度的赌注: 知识系统的未来从地基起就是多模态, 不是把多模态附加到文字模型作为事后想法。

### GLM-4.5/5（Zhipu AI）

Zhipu AI 的 GLM 系列, 以 7,440 亿参数 MoE GLM-5 为高峰, 是为 agent harness 量身打造。模型架构含原生工具使用 token 与结构化输出保证, 减少建可靠 agent 整合到生产管线所需的 scaffolding 代码。这种「agent 原生」设计哲学意味较少 prompt engineering 与较少把 GLM 整合进生产管线的重试。

## C. 与西方生态系的关键差异

理解中国知识工程地景需要不只编纂工具与模型。生态系在根本不同的约束与诱因下运作, 这些从第一天起就塑造架构决策。

### 工具偏好：视觉优先 vs. 代码优先

最受欢迎中国平台——Dify、Coze Studio、FastGPT——是视觉优先。用户透过在画布上拖放节点建知识管线。相反, 西方生态系的主导框架（LangChain、LlamaIndex、Haystack）是代码优先, 视觉工具是次要附加。这个发散反映不同用户人口统计: 中国 AI 采纳大量由企业 IT 部门与可能不写 Python 的「公民开发者」推动, 而西方早期采用者倾向是擅长代码的软件工程师。

### 部署：On-premise vs. API 优先

On-premise 部署在中国主导。这由两个相互加强因素驱动: 数据主权的监管要求（特别在金融、医疗、政府）和实务约束自美国晶片出口管制让大规模云端 GPU 存取更贵。结果是中国平台大量投资量化、蒸馏、效率——让模型在可用硬件上跑得好, 而非假设无限云端运算。西方平台相反默认 API 优先架构, 模型跑在供应商基础设施上。

### 监管架构

到 2025 年 12 月, 已有 748 个 AI 服务在《生成式 AI 管理办法》下向中国监管机构申报。合规不是可选或抱负——它从设计阶段塑造技术架构。内容过滤、稽核日志、用户身分验证作为核心功能内建在平台中, 不是发布前栓上的。这个监管压力悖论地创造了更标准化架构: 当每个人都必须实现同样合规要求, 让合规容易的平台胜出。

### 社群与知识分享

中国开发者社群在根本不同平台上运作。微信群组（不是 Slack 或 Discord）是即时讨论的主要频道。知乎担任长技术 Q&A 的 Stack Overflow 角色。CSDN（中国软件开发网络）托管教程与博文。GitHub 用于代码, 但讨论在别处发生。这个碎片化意味西方开发者搜 GitHub Issues 或 Discord 求中国工具的帮助常找到稀疏的英文支援, 而中文社群充满活力——只是对非中文使用者不可见。

### 透过约束创新

美国晶片出口管制创造了意外创新动态。中国 AI 实验室无法简单扩展运算, 不成比例地投资在算法效率。DeepSeek R1 不到 600 万美元训练成本是最可见结果, 但该 pattern 跨整个生态系延伸: 较小模型配更好推论优化、更激进量化技术、为最大化每 FLOP 能力设计的架构。西方生态系运算更多, 倾向透过规模创新。两个做法都产生前沿结果, 但透过不同路径。

### 开源作为策略性必要

中国开源权重模型发布在数量上现已超越西方。这不是利他——是策略。开源建生态系锁定（开发者基于你的模型建）、吸引人才（研究者想做人们用的模型）、在全球开发者社群创造外交善意。Alibaba 的 Apache 2.0 授权 Qwen、DeepSeek 的 MIT 授权、ByteDance 的 Coze Studio 开源都遵循这 pattern。结果是任何地方的 solo 开发者现在能完全在中国开源基础设施上建生产知识系统, 从模型到框架到部署工具。

## D. 关于 Bilibili 内容的注记

Bilibili（B 站）托管大量 AI 教程, 但从业者应注意许多是英文 YouTube 内容的重新上传或翻译。Bilibili AI 内容的原创价值在于中文专属工具教程: Dify 步步部署指南、Qwen 整合走读、英文不存在的企业部署案例研究。在 Bilibili 上研究时, 永远把内容追溯到原始来源。如果一个教程示范英文叙述配中文配音的 LangChain, 原始 YouTube 版本可能更新。

## 来源

- Dify GitHub Repository: [https://github.com/langgenius/dify](https://github.com/langgenius/dify)
- RAGFlow GitHub Repository: [https://github.com/infiniflow/ragflow](https://github.com/infiniflow/ragflow)
- FastGPT GitHub Repository: [https://github.com/labring/FastGPT](https://github.com/labring/FastGPT)
- MaxKB GitHub Repository: [https://github.com/1Panel-dev/MaxKB](https://github.com/1Panel-dev/MaxKB)
- Coze Studio GitHub Repository: [https://github.com/coze-dev/coze-studio](https://github.com/coze-dev/coze-studio)
- DB-GPT GitHub Repository: [https://github.com/eosphoros-ai/DB-GPT](https://github.com/eosphoros-ai/DB-GPT)
- Qwen3 技术报告与模型卡, 阿里云（2025）——主要入口: [https://huggingface.co/Qwen](https://huggingface.co/Qwen) 与 Qwen 团队的 Hugging Face 文章。Apache 2.0 授权细节透过仓库 LICENSE 档确认。
- DeepSeek R1 论文: "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning"（2025 年 1 月）。[https://github.com/deepseek-ai/DeepSeek-R1](https://github.com/deepseek-ai/DeepSeek-R1) 托管模型并连结到技术报告 PDF。
- Moonshot AI. Kimi K2.5 Agent Swarm 报道在 2026 年初跨 Moonshot 博客与科技媒体流通; 这里引用的 100 子 agent / 约 1500 工具调用数字从次级科技媒体总结报告。主要存取透过 [https://platform.moonshot.ai](https://platform.moonshot.ai)。
- 百度. ERNIE 5.0 推出（2026 年 1 月）; 2.4T 参数 / 原生全模态主张透过百度官方频道与中国科技媒体流通。这里没引用单一主要 URL; 把模态与参数数字当作广为报告但次级。
- Zhipu AI. GLM-4/5 模型卡在 Hugging Face 与官方 ZhipuAI 博客;「744B MoE GLM-5」+ agent 原生工具 token 跨模型卡与博客报道报告。主要入口: [https://www.zhipuai.cn](https://www.zhipuai.cn)。
- Cyberspace Administration of China,「生成式 AI 服务申报」披露（2025 年 12 月）——748 服务数字在中国科技媒体广为复制; 底层 registry 透过 CAC 官方网站分批发布。
-「中国开源 AI」市场评论——R1 后中国企业开源采纳从 23% 到 67% 的转变跨多个次级出口在 2025-2026 报告; 视为广为引用但这里没钉单一主要调查。
- DeepSeek. "DeepSeek mHC: Manifold-Constrained Hyper-Connections"（2026 年 4 月）。[https://deepseek.ai/blog/deepseek-mhc-manifold-constrained-hyper-connections](https://deepseek.ai/blog/deepseek-mhc-manifold-constrained-hyper-connections) ——标记为等独立复制。
- DeepSeek. V4 模型在 Hugging Face 发布（2026 年 4 月 24 日）。MIT 授权; V4-Pro 1.6T（49B 活跃）/ V4-Flash 284B（13B 活跃）; 1M token 默认 context。
- Fortune. "DeepSeek unveils V4 model, with rock-bottom prices and close integration with Huawei's chips"（2026 年 4 月 24 日）。[https://fortune.com/2026/04/24/deepseek-v4-ai-model-price-performance-china-open-source/](https://fortune.com/2026/04/24/deepseek-v4-ai-model-price-performance-china-open-source/)
- South China Morning Post. "DeepSeek unveils next-gen AI model as Huawei vows 'full support' with new chips"（2026 年 4 月 24 日）。[https://www.scmp.com/tech/big-tech/article/3351239/deepseek-releases-next-gen-ai-model-world-leading-efficiency](https://www.scmp.com/tech/big-tech/article/3351239/deepseek-releases-next-gen-ai-model-world-leading-efficiency)
- Phemex News. "DeepSeek V4 Matches NVIDIA on Huawei Ascend, Dispels Rumors"（2026 年 4 月）。[https://phemex.com/news/article/deepseek-v4-matches-nvidia-performance-on-huawei-ascend-dispels-delay-rumors-75616](https://phemex.com/news/article/deepseek-v4-matches-nvidia-performance-on-huawei-ascend-dispels-delay-rumors-75616) ——推论对等主张, 在 Ascend 950PR 上比 NVIDIA H20 约 2.8 倍运算吞吐。

---

*下一章: [第 10 章 —— 构建一个真实世界的知识 Harness](10-case-study.md)*
