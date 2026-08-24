# 第 14 章：Graph Engineering —— 为 Agent 组织布线

> **一句话总结：** Graph engineering 是 2026 年 7 月出现的一个主张：loop engineering 之上还有一层, 就是 graph——明确接好哪些 agent 存在、谁可以把工作委派给谁, 以及它们的 loop 之间如何互相监督、互相纠正。
>
> **为什么重要：** 如果这个主张站得住脚, 它就替那一层命了名——在那一层, 多 agent 系统不再是一堆临时凑起来的 loop, 而是被设计出来的组织; 如果站不住脚, 它就是最清楚的一个活案例, 让我们看到这些世代标签是怎么被造出来、又怎么被拆掉的。

这现在是本指南寿命最短的概念, 从第 13 章手上接过这个头衔。「graph engineering」这个词在写作当下大约只有两周历史：它在 2026 年 7 月 17-18 日之后的几天内结晶化, 完全活在从业者部落格与厂商文章里, 背后没有任何学术文献。它也是本指南涵盖的争议最大的一个词。对它最响亮的一个反驳——来自 LangChain, 一家框架名字本身就叫做「图」的厂商——是说这个实践已经有三年历史, 新的只是这个标签。

以下内容刻意保持保留的态度。怀疑者得到和支持者一样多的篇幅, 各来源之间互相冲突的观看次数会照实报告为冲突, 本章结尾用一道明确的存活关卡收尾, 而不是给出定论。

本章涵盖那篇催化剂贴文与它触发的文章浪潮、这个新框架实际主张什么、对它的反驳、这个名字所必须做的与知识图谱的区分、如果它真是独立一层的话会坐落在哪里、中文生态圈的回声, 以及从业者现在该不该在乎。

---

## 14.1 引发一切的那条推文（2026 年 7 月 17-18 日）

这套剧本很眼熟, 因为本指南才刚看着它跑过一遍。在他 6 月 7 日那篇催化了 loop engineering 的贴文（第 13.1 节）之后六周, **Peter Steinberger**——OpenClaw 的创造者, 现在人在 OpenAI——又发了一次贴文。根据 [Carlos E. Perez](https://medium.com/intuitionmachine/from-loop-engineering-to-graph-engineering-d3ebeb08511c) 与 [Yash Thakker](https://explainx.ai/blog/graph-engineering-ai-agents-multi-agent-organizations-2026) 的逐字引用, 这篇贴文写道：

> 我们现在还在讲 loop, 还是已经转去讲 graph 了？

在讲别的之前, 先讲两个来源上的但书, 因为本章存在的意义正是要讲这些。第一, 这篇贴文本身没有被本指南直接抓取过, 各自独立抓取的二手来源之间的转述也不完全一致。只有 Perez 和 Thakker 逐字引用了这句确切的英文措辞。[LangChain](https://www.langchain.com/blog/3-years-of-graph-engineering-with-langgraph) 和 Perez 只链接了这篇贴文, 没有引用它的文字; [36kr](https://eu.36kr.com/en/p/3904771418867330) 和 Tony Bai 把它译成了中文, 36kr 的英文版又把中译回译成「我们还在讲 loop 吗, 还是已经转移到 graph 了？」; [Eigent](https://www.eigent.ai/blog/graph-engineering-ai-agents) 则是转述。上面之所以能印出这句措辞, 依据的就是这两处逐字引用。

第二, 围绕它的数字彼此不一致。每一个给这篇贴文标注日期的来源, 标的都是 7 月 18 日; 本章标题里用到的 7 月 17 日这个区间下限, 是一个美国时区的可能性, 而不是来源之间有记载的分歧。观看次数确实互相冲突, 不过这些是不同时刻拍下的快照, 而不是对同一时点的竞争性测量：Thakker 报的是几小时内 575K 次观看, 36kr 报的是两天内 2.6M 次（同一篇文章里, 对照六周前那篇 loop 时代贴文的 8.4M 次观看）, Tony Bai 报的是两天内大约 800K 次。这里没有把任何单一数字当作事实来陈述。

和 6 月那篇一样, Steinberger 什么都没命名。「graph engineering」这个复合词, 在他的原文里完全没出现。这个复合词是在几天内的回应文章里结晶化的, 有意识地仿照了 prompt、context、harness、loop engineering 这条脉络——而且这波浪潮来得很快：

- **7 月 18 日** —— [Yash Thakker 的 explainx.ai 指南](https://explainx.ai/blog/graph-engineering-ai-agents-multi-agent-organizations-2026)（持续更新到 7 月 26 日）, 点名这条推文是催化剂, 提出了 org graph／work graph 的拆分。
- **7 月 19 日** —— **Carlos E. Perez**（Intuition Machine）发表第一篇有分量的理论扩展。
- **7 月 20 日** —— 企业厂商 **TrueFoundry** 出货一份[面向生产的指南](https://www.truefoundry.com/blog/graph-engineering-enterprise-guide), 附治理检查清单。
- **7 月 21 日** —— **eigent.ai** 发表自己的厂商文章; 中国的 **Tony Bai** 与 **36kr** 同一天都报道了这场论述（14.6）。
- **7 月 22 日** —— **LangChain** 由 Sydney Runkle 与 Harrison Chase 联名发表的官方回应, 在催化剂出现四天后落地（14.3）。

一个催化剂、一波文章浪潮、一个厂商的反框架, 加上一个中文生态圈的回声, 全都发生在一周之内：loop-engineering 的命名顺序, 用更快的速度重播了一遍。

---

## 14.2 Graph Engineering 声称是什么

把这些文章拆到最简, 会看到三个反复出现的主张。

**Agent 组织, 而非 Agent 行为。** Thakker 的框定, 是这个递进关系里最好引用的版本：

> Loop 让 agent 的行为变得可编程。Graph 让 agent 的组织变得可编程。

他的指南把 graph 拆成两个不同的对象：

- **org graph（组织图）**——一张稳定的图表, 记录哪些 agent 存在、每个 agent 是干嘛的, 以及哪些委派边是被允许的;
- **work graph（工作图）**——某个特定工作生出、执行、再丢弃的那个短命任务分解。

这里的主张是：两者现在都是需要被设计、版本化、审查的工程产物, 就像第 4 章对待 harness、第 13 章对待 loop 那样。

**Loop 监督 Loop, 被 Anchor 摁住。** [Perez 的文章](https://medium.com/intuitionmachine/from-loop-engineering-to-graph-engineering-d3ebeb08511c)——7 月 19 日发表的第一篇理论扩展——把 graph 描述成一个由 loop 组成的网络, 彼此监督、彼此约束。他特有的补充是 **anchor**：一个无可争辩、扎根于外部现实的测量（一个测试结果、一个指标、一次对照真实情况的检查）, graph 里的某个节点必须触碰到它。他主张, 没有 anchor 的话, 一张互相审阅的 agent 组成的 graph, 会退化成一个回声室, 收敛到自信的一致意见, 而不是正确性——这是第 13.4 节记录过的单一 loop 自我打分失效模式的多 agent 版本。

**受治理的拓扑。** 各厂商的文章——[TrueFoundry](https://www.truefoundry.com/blog/graph-engineering-enterprise-guide)（7 月 20 日）与 [Eigent](https://www.eigent.ai/blog/graph-engineering-ai-agents)（7 月 21 日, 同时把功劳归给 Steinberger 的那句提示和 Perez 的「loop 网络」扩展）——都收敛到同一个操作层面的理解：graph engineering 就是对 agent 拓扑的治理与可观测性。按这个理解, 它拥有的问题是：

- agent 之间哪些转移是被允许的, 哪些在结构上根本不可能;
- 一次失败在蔓延到整个组织之前, 会在哪里被隔离;
- work graph 里失控的分支, 要怎么被侦测、被切断;
- 对一个 agent 组织做稽核, 到底该长什么样。

TrueFoundry 为这些问题出货了一份企业检查清单; 这份清单是否需要一个新的学科名字才能存在, 正是下一节要处理的问题。

**厂商出货了结构, 却没出货这个名字。** 2026 年 8 月 7 日（Claude Code v2.1.224, 到 8 月 23 日迭代到 v2.1.241）, Anthropic 出货了跨 session 的 agent 讯息传递：`ListAgents` 会发现具名的 session——子 agent、agent-team 队友、其他本地 session、云端 session, 以及其他机器上的 Remote Control session——而 `SendMessage` 按名字在它们之间传递纯文字, 由每个 session 各自的入站治理（接受／保留／拒绝）、一个基于权限模式的默认值, 以及大小／突发／loop 节流来把关。范围刻意收得很窄：对话历史和档案不会跨 session、没有跨 session 的权限批准, 而且这个功能在 Bedrock、AWS 上的 Claude Platform、Google Cloud Agent Platform, 或 Microsoft Foundry 上都用不了。拿它对照上面刚定义的 org graph——一份稳定的具名 agent 名单, 加上被允许的委派边——这看起来就是它的一个出货实例：具名、可寻址的 session, 加上受治理的讯息边连在它们之间。它不是的, 是词汇上的采用：Anthropic 自己的文档和更新日志, 没有任何一处用「graph engineering」这个说法来描述这个功能。这个落差——一家主要的 harness 厂商, 把本章追踪的这个模式实作出来了, 却对替它造的这个标签保持沉默——是这个原语存在的证据, 不是这个词存在的证据, 而这两者不是同一个主张。

---

## 14.3 反驳声音

怀疑者在这里该得到同等的份量, 而不只是一段礼貌性的段落, 因为在四天之内, 这场论述自己就产出了最有力的反驳——而且是来自最有资格提出它的那一方。

**LangChain：这事已经有三年了。** [《3 Years of Graph Engineering with LangGraph》](https://www.langchain.com/blog/3-years-of-graph-engineering-with-langgraph)（Sydney Runkle 与 Harrison Chase, 2026 年 7 月 22 日）同时做了两件事。它替这个词赋予了合法性——这篇文章明确把 graph engineering 排在「prompt engineering、context engineering、harness engineering、loop engineering」之后, 这正是本指南追踪的那条世代主线, 只是多加了一级阶梯。但它同一口气里, 也把这个词的气给放掉了：

> 把 agentic 系统表示成 graph 并不新鲜, 我们已经这么做三年了。

他们的化简很干净：**一个 loop 不过就是一个有向的、有环的 graph。** LangGraph 从 2023 年起就把 agent 建模成 graph 拓扑——节点、边、条件转移、环。照这个读法, 2026 年 7 月除了词汇之外什么都没变：这个实践比这个标签早了三年, 而标签只是加了一个名字, 而不是加了一个能力。

注意这对证据基础做了什么。graph engineering 目前拥有的最强的采用信号——一家主要框架厂商在四天内做出回应——同时也是它最强的怀疑来源。同一份文件两者都是, 任何诚实的说法都得把它同时当成这两者来看待。

**Tony Bai：今天的框架, 明天的废弃堆。** 这位中国开发者基础设施领域的写作者在 [7 月 21 日的贴文](https://tonybai.com/2026/07/21/from-loop-engineering-to-graph-engineering/) 里, 先是同情地解释了 loop 互相监督加上 anchor 这个框架, 然后话锋一转：loop engineering 才火了不到两个月, 硅谷就又产出了下一个词, 而「graph」自己也可能是明天被丢弃的流行语。这个警告来自一位早期就认真讲解过 loop 框架的人——他的怀疑不是反射性的反炒作——所以这句话落地得更重。

**证据的缺席说明了什么。** 两周过去了, 目前没有任何会议演讲、课程, 或者职位招聘用到这个词; 本指南为此做过搜寻, 一个都没找到。这既符合「这个词还不到两周」的情况, 也同样符合「这个词撑不下去」的情况。诚实的说法是：目前的证据还分辨不出这两者。

---

## 14.4 不是知识图谱

这个名字带来了一场碰撞, 本指南在结构上有义务把它解开, 因为第 2 章从本指南一开始就在讲 graph。「知识图谱工程」是一个已经确立、超过十年历史的学科——语义网、本体、三元组存储——GraphRAG（第 2 章）建的是实体与关系构成的图, 好让系统能检索、推理它所知道的东西。2026 年 7 月意义上的 graph engineering, 除了这个字之外, 和它没有任何共通之处。TrueFoundry 的区分是目前最干脆的一个版本, 值得当作分界线引用出来：

> 知识图谱结构化的是系统*知道什么*; 2026 年意义上的 graph engineering, 结构化的是系统*是谁*——它的成员、职责, 和讯息路径。

把两者摆在一起看, 这两种 graph 除了数据结构之外, 什么共同点都没有：

| | 知识图谱／GraphRAG（第 2 章） | Graph engineering（本章） |
|---|---|---|
| 节点 | 实体 | Agent |
| 边 | 有标签的关系 | 被允许的委派 |
| 建立时机 | 索引阶段 | 架构阶段 |
| 使用时机 | 检索阶段 | 运行时（被遍历、也被改动） |
| 回答的问题 | 系统知道什么？ | 系统是谁？ |

从第 2 章 GraphRAG 那一节走到本章的读者, 应该把这个共用的字当成词汇上的巧合, 而不是共同的血缘。（第 2 章里有一个反向指回来的指标。）

---

## 14.5 它坐落在哪里——第五代, 还是第四代的重构？

如果这个框架真的站得住脚, 它在本指南的演进故事里该放在哪里？本指南的主线是从 prompt（第 1 章）到 context（第 1-3 章）到 harness（第 4 章）再到 loop（第 13 章）。支持者的答案是：再往上一层楼。LangChain 自己的排列——把 graph engineering 排在 prompt、context、harness、loop 之后——即使一边质疑它的新颖性, 一边还是把它放成了第五级阶梯。

这段时间里最有用的结构性处理, 也是最新的一篇。[MarkTechPost 7 月 29 日的文章](https://www.marktechpost.com/2026/07/29/prompt-engineering-vs-loop-engineering-vs-graph-engineering-what-changes-at-each-layer/) 主张这些层不是彼此的继任者, 而是层层堆叠的控制单元：

- **harness**（第 4 章）是单一个 agent 周围的环境;
- **loop**（第 13 章）是单一个 agent 的行为循环;
- **graph** 协调多个 agent, 靠的是一张稳定的组织图, 加上一张短命的工作图。

它的主线——「graph 是由 loop 建成的, loop 是由 prompt 建成的」——是第 1 章的共存论点往外多加了一个框, 也是和本指南对待前面几层的方式最相容的读法。

但泄气版的读法, 一样能吻合同一批事实。如果一个 loop 不过就是一个有向环状 graph（LangChain 的说法）, 那么一张由 loop 组成的 graph, 不过是一个更大的 loop 系统, 而「graph engineering」就是把 harness-加-loop 的那套 engineering, 套用到 N 个 agent 而不是一个 agent 身上而已——是第四层的重构, 而不是第五层。第 13 章留下的开放问题是 loop engineering 到底是不是真的独立一层, 还是「配了排程器的 harness engineering」; graph engineering 继承了那个开放问题, 又加上了自己的一个。本指南不打算解决这个问题。这个框架才两周历史; 解决它等于认证它, 而不是描述它。

---

## 14.6 中文生态圈的回声

一个框架是否已经逃出它诞生的那个泡泡, 比较强的信号之一, 就是中文开发者生态圈接住它的速度有多快——而这一次, 回声在三天之内就出现了, 而且已经带着一个定型的译名：**图工程**。

得到核实的锚点有两个。[Tony Bai 7 月 21 日的贴文](https://tonybai.com/2026/07/21/from-loop-engineering-to-graph-engineering/)——标题：「Loop Engineering才火两个月，硅谷已经卷出"Graph Engineering"了」——是实质内容的解说文, 替中文基础设施受众讲解了 Perez 的 loop 互相监督加 anchor 这套说法, 并附上了 14.3 那个流行语警告。而 [36kr 的英文版报道](https://eu.36kr.com/en/p/3904771418867330)（同样是 7 月 21 日）把这场论述当新闻处理：它报告了 14.1 里的观看次数比较, 并点名 Geoffrey Huntley、Boris Cherny、Addy Osmani、Luis Catacora 是这场论述的参与者。（这些归属只依据 36kr 一家, 在此也只以此为依据引用。）

除了这两个之外, 回声就只剩下标题了。中文搜寻找到两篇 CSDN 智能体开发者社区的文章——一篇标题比较克制, 叫「从Loop Engineering到Graph Engineering」, 一篇把整套炒作模板用满, 叫「Loop工程已死，Graph工程永生」（和第 13.8 节记录过的、loop 那波浪潮里同一个「已死」噱头）——还有一篇繁体中文的解说文。这三篇都没有被本指南独立抓取过; 它们只是以「搜寻结果里的标题」这个身份被引用, 用来证明中文内容管线已经在处理这个词, 仅此而已。

这个模式在第 13 章就见过：那条把 loop-engineering 解说文产业化的管线, 现在正在处理 图工程, 从催化剂到催化剂大约隔了六周, 但从催化剂到回声只隔了几天。

---

## 14.7 你现在该在乎吗？

一个在 2026 年 7 月下旬读到这里的从业者, 需要两个分开的答案, 因为标签和问题本身是可以分开的。

**不管标签怎样, 问题都是真的。** 如果你在一个 harness 里用一个 loop 跑一个 agent, 本章的内容不会改变你的工作; 第 4 章和第 13 章仍然是在起作用的那两层。如果你已经在把多个 agent 接在一起, 这些文章点名的那些担忧——哪些委派边是被允许的、一次失败在蔓延之前会在哪里被隔离、什么东西会被观测与稽核、哪个节点触碰了 anchor 好让系统不会漂移到自说自话——不管「graph engineering」这个名字能不能撑下去, 都是你本来就有的工程问题。TrueFoundry 的检查清单和 Perez 的 anchor, 不管用哪套词汇, 现在都能用。LangChain 的反驳, 在这一点上其实是同意的：他们已经工程这些 graph 三年了, 这意味着这些问题至少已经存在了三年。

**这个标签, 是一场你不必下注的赌局。** 本指南在 loop engineering 才五周大的时候加入了第 13 章; graph engineering 在才两周大的时候就拿到了一章, 靠的是严格来说更强的早期证据（更快的文章浪潮、同一周内框架厂商的回应、更快的中文回声）, 和严格来说更弱的成熟度（没有能和 Stripe 的 minions 相提并论的生产案例研究、没有厂商课程、没有基准测试）。所以本章用一道关卡收尾, 而不是一个定论。**存活测试是：这个词到 2026 年 9 月还会不会继续流通。** 具体来说, 要留意：

- 框架或厂商文档把这个词采纳进产品词汇, 而不只是部落格里的框定说法;
- 会议演讲、课程, 或职位招聘用到它（截至写作时：一个都没找到）;
- 一个具名的生产案例研究, 分量能比得上 Stripe 的 minions 给 loop engineering 带来的那种分量;
- 第二波文章浪潮, 而且不是为了回应某一篇贴文而写的。

如果这些都出现了, 本章会像第 13 章那样继续长大。如果没有出现, 本章就会作为一场为期两周的命名事件的记录留在那里, 而泄气版的读法就赢了。

本指南把 graph engineering 当作一个还在接受检验的主张来追踪, 而不是一层已经定型的东西——而 Tony Bai 的那句警告, 今天的框架可能是明天被丢弃的流行语, 是对这盘赌注最公道的一句话总结。

---

## 来源

- **Steinberger, Peter.** X 贴文, 「Are we still talking loops or did we shift to graphs yet?」（2026 年 7 月 18 日, 依下方每一个标注了日期的来源为准）——没有被本指南直接抓取, 只透过下方这些来源引用：Perez 与 Thakker（explainx）逐字引用; LangChain 与 Perez 只链接、没有引用文字; 36kr 与 Tony Bai 译成中文; Eigent 转述。各来源报告的观看次数互相冲突。
- **Runkle, Sydney 与 Harrison Chase（LangChain）。**「3 Years of Graph Engineering with LangGraph」（2026 年 7 月 22 日）：[https://www.langchain.com/blog/3-years-of-graph-engineering-with-langgraph](https://www.langchain.com/blog/3-years-of-graph-engineering-with-langgraph) ——把 graph engineering 排在 prompt／context／harness／loop 之后; 「一个 loop 不过就是一个有向的、有环的 graph」; 「这事已经三年」的反驳。
- **Perez, Carlos E.（Intuition Machine）。**「From Loop Engineering to Graph Engineering?」（2026 年 7 月 19 日）：[https://medium.com/intuitionmachine/from-loop-engineering-to-graph-engineering-d3ebeb08511c](https://medium.com/intuitionmachine/from-loop-engineering-to-graph-engineering-d3ebeb08511c) ——第一篇理论扩展; loop 监督 loop; anchor 作为对抗回声室的无可争辩测量。
- **Thakker, Yash（explainx.ai）。**「Graph Engineering: After Loops, This Is How You Wire Multi-Agent Orgs (2026)」（2026 年 7 月 18 日, 更新至 7 月 26 日）：[https://explainx.ai/blog/graph-engineering-ai-agents-multi-agent-organizations-2026](https://explainx.ai/blog/graph-engineering-ai-agents-multi-agent-organizations-2026) —— org graph 与 work graph 之分; 「Loop 让 agent 行为可编程。Graph 让 agent 组织可编程。」
- **TrueFoundry.**「Graph Engineering for Multi-Agent Systems: Architecture, Governance, and Observability」（2026 年 7 月 20 日）：[https://www.truefoundry.com/blog/graph-engineering-enterprise-guide](https://www.truefoundry.com/blog/graph-engineering-enterprise-guide) ——企业检查清单; 知识图谱区分引言（「系统知道什么」对「系统是谁」）。
- **Eigent.**「Graph Engineering for AI Agents」（2026 年 7 月 21 日）：[https://www.eigent.ai/blog/graph-engineering-ai-agents](https://www.eigent.ai/blog/graph-engineering-ai-agents) ——把功劳归给 Steinberger 那句提示和 Perez 的扩展; 受治理、互相纠正的 loop 拓扑。
- **36kr（英文版）。**「Father of Lobster's One Tweet: Is the Loop Era Over?」（2026 年 7 月 21 日）：[https://eu.36kr.com/en/p/3904771418867330](https://eu.36kr.com/en/p/3904771418867330) ——报告这条推文 2.6M 次观看, 对照 8.4M 次观看的 loop 时代贴文; 点名其他论述参与者; 把这个词当作正在浮现的东西处理。
- **Bai, Tony.**「Loop Engineering才火两个月，硅谷已经卷出"Graph Engineering"了」（2026 年 7 月 21 日）：[https://tonybai.com/2026/07/21/from-loop-engineering-to-graph-engineering/](https://tonybai.com/2026/07/21/from-loop-engineering-to-graph-engineering/) —— 图工程 解说文, 面向中文生态圈; 警告「graph」自己也可能变成被丢弃的流行语。
- **MarkTechPost.**「Prompt Engineering vs Loop Engineering vs Graph Engineering: What Changes at Each Layer」（2026 年 7 月 29 日）：[https://www.marktechpost.com/2026/07/29/prompt-engineering-vs-loop-engineering-vs-graph-engineering-what-changes-at-each-layer/](https://www.marktechpost.com/2026/07/29/prompt-engineering-vs-loop-engineering-vs-graph-engineering-what-changes-at-each-layer/) ——层层堆叠的控制单元读法; org graph 加 work graph; 「graph 是由 loop 建成的, loop 是由 prompt 建成的」。
- **Claude Code（Anthropic）。** 跨 session 讯息传递文档与更新日志（2026 年 8 月 7 日, v2.1.224; 到 2026 年 8 月 23 日迭代至 v2.1.241）：[https://code.claude.com/docs/en/cross-session-messaging](https://code.claude.com/docs/en/cross-session-messaging) ; [https://code.claude.com/docs/en/changelog](https://code.claude.com/docs/en/changelog) —— ListAgents／SendMessage 出货具名 agent 发现与受治理的跨 session 讯息边; 「graph engineering」这个说法在两份文档里都完全没出现。

---

*上一章: [第 13 章 —— Loop Engineering](13-loop-engineering.md)*
