# 第 13 章：Loop Engineering —— 设计提示 Agent 的系统

> **一句话总结：** Loop engineering 是建构那套替你提示 agent 的系统的实践——让你不再每一回合都亲手驾驶, 而是开始设计一个会自己运行、自我检查、自我喂养的 loop。
>
> **为什么重要：** 这是本指南演进故事里最新、也最未定型的一层, 也最可能在接下来一年里, 形塑自主 agent 工作实际上要怎么被排程、验证、审查。

这是本指南目前寿命最短的一个概念。（它保住这个头衔只有六周：2026 年 7 月下旬, 同一套剧本又产出了一个「loop 之上还有更高一层」的主张, 也就是 graph engineering, 详见[第 14 章](14-graph-engineering.md)。）「loop engineering」这个词在写作当下大约只有五周历史：它在 2026 年 6 月初被命名, 几天内就透过从业者部落格、播客、X 传开, 目前背后还没有任何学术文献。以下内容刻意保持保留的态度。如果某个论述只靠一句被三种不同方式转录的播客口述引言撑住, 或者只靠一篇什么都没命名的病毒式贴文撑住, 本章会明写出来。目标是准确描述一个正在浮现的框架, 而不是把它认证成一个已经定型的世代。

这个框架值得描述, 因为它在从业者论述里确实起着作用：它替一个转变命了名——这个转变是 harness engineering（第 4 章）暗示过、但没有单独挑出来讲的——从*提示一个 agent*, 转移到*设计那个替你提示 agent 的系统*。这到底该不该算独立一层, 还是不过是「harness engineering 加一个排程器」, 正是本章刻意留白的开放问题。

本章涵盖这个词从哪里来、支持者怎么把它和 harness 连起来、一个 loop 由什么组成、让 loop 保持诚实的 generator-evaluator split、一个大型生产案例、堆叠 loop 的框架、人类被交代要保留的判断力, 以及早期的采用信号——争议的部分会全程标出。

---

## 13.1 得名的那一周（2026 年 6 月）

催化剂是一篇贴文。2026 年 6 月 7 日, **Peter Steinberger**（@steipete）——**OpenClaw** 的创造者, Y Combinator 形容它「在不到 5 个月内, 从一个周末项目变成 GitHub 上星数最多的软件仓库, 拿下 346k+ 星」, 超越 React, 他现在人在 OpenAI——写道：

> 这是你每个月的例行提醒：你不该再手动提示编程 agent 了。
>
> 你该做的是设计出会提示你的 agent 的 loop。

截至 2026 年 7 月中, 这篇贴文已获得 **8.4M+ 曝光次数**。它什么都没命名：Steinberger 没有用「loop engineering」这个说法, 这几个字在他的原文里完全没出现。命名是其他人在回应他所催化的想法时给出的。

同一天, **Addy Osmani**（Google）发表了那篇替这个实践命名的文章（《Loop Engineering》, addyosmani.com/blog/loop-engineering/, 6 月 7 日; 6 月 22 日在 O'Reilly Radar 转载）。他的定义, 就是后续论述里被反复引用的那个版本：

> Loop engineering, 就是把你自己从「提示 agent 的那个人」这个角色里换掉。你转而去设计一个替你做这件事的系统。

同一个转变, 也从一间前沿实验室内部冒出来。**Boris Cherny**, Claude Code 的创造者兼 Anthropic 的 Claude Code 负责人, 在 2026 年中的一次播客里, 用同样的说法框定了自己的工作流。根据 Lenny's Podcast 那场访谈被引用最多的转录版本：

> 我现在已经不再提示 Claude 了。我有一堆 loop 在跑, 是它们在提示 Claude、决定该做什么。我的工作是写 loop。

这句引言需要一个但书, 而这正是本章存在的意义所在。这是一句*口述*的话, 不同媒体的转录版本并不一致（有些引用的是 Acquired 播客, 而不是 Lenny's）, 也没有权威的逐字文本或完整转录稿可查。但其*实质内容*——Cherny 不再亲手提示, 而是写会提示 Claude、决定下一步动作的 loop——在多个二手来源里都得到印证; 只是确切措辞没有定案。

合起来看, 6 月 7 日那一周产出了一个催化剂（Steinberger）、一个名字和定义（Osmani）, 以及一个来自内部人士的回声（Cherny）。它没有产出的, 是共识。这个词在几周内就在从业者论述中结晶化, 但接受度是分裂的：一部分读者称它是真正的转变, 另一部分读者称它为时过早——不过是排程的改名, 或者「配了 cron 工作的 harness」。目前没有任何同行评审的著作使用这个词。本指南把 loop engineering 当作一个正在浮现、有争议的框架来处理（见第 1 章的第四代那一节）, 这也是为什么以下每一个有分量的论述都绑着一手来源, 而空白之处会被明写出来, 而不是被填满。

---

## 13.2 比 Harness 高一层楼

支持者做出的最干净的定义动作, 就是把 loop 直接放在第 4 章的 harness 正上方。Osmani 直接讲明了这层关系：

> Loop engineering 就坐落在 harness 上面那一层楼。

他对 loop *是什么*的心智模型, 仍然把 harness 当作构件：loop 是那个「按计时器运行、会生出小帮手、会自己喂自己」的 harness。他明确表示这是延伸先前的工作, 而不是取代它——他「之前写过这件事的表亲, agent harness engineering, 也就是打造单一个 agent 运行所在的那个环境」。

中国开发者 **程序员鱼皮**（liyupi）给出了这层关系里结构性最强的版本。在他 6 月 16 日的教程（codefather.cn）里, 他把提示词技巧、上下文管理、harness 搭建, 和 loop 排成 **層層包含**——一层套一层：

> 这四者是层层包含的关系。提示词技巧、上下文管理、Harness 搭建，这些能力在 Loop 里面全都要用上。

这和第 1 章套在 prompt → context → harness 上的嵌套层逻辑是一样的, 只是往外多加了一个框。归属这件事值得讲精确一点：鱼皮是在替中国开发者受众重新包装、整理既有的术语, 而不是在造词——「harness engineering」和「loop engineering」这两个词, 源头要追溯到 Claude Code 与 Cherny 的论述。

他的马匹比喻, 把 harness 和 loop 之间的界线画得比任何人都清楚：

> 如果把 AI 比作一匹马，Harness 就是你给马装上的缰绳、马鞍和围栏，然后你骑在马上手动驾驭它。

> 而 Loop 呢，是你设定好一条巡逻路线后，不用上马，让马自己按路线一圈一圈地跑。

这个比喻编码了让 loop engineering 不至于沦为「给 agent 用的 cron」的那个唯一分野：**loop 不是排程器。** 排程器按时触发。loop 按时触发, *然后再读取当下状态, 决定这一轮该做什么。* 这个运行时的决策者——检查 CI 状态、开着的 issue、或上一次运行留下的残局, 再挑选动作的那个部分——正是一条 cron 条目所没有的东西。loop 是排程器加上一个每一轮都重新读状态、重新决策的 agent。（交叉参照：第 1 章「核心洞见：共存, 而非取代」。）

---

## 13.3 一个 Loop 由什么组成

Osmani 的文章给出了最具体的清单。他那一节的标题是 **「五个组件, 外加一些补充」（"The five pieces, and then notes"）**——数量很重要, 因为很容易被灌水。实际上是*五个组件加外部状态*, 而不是六个平起平坐的构件：

- **Automations（自动化触发）** —— 让 loop 启动的触发器（排程、事件）。
- **Worktrees（工作树）** —— 隔离的工作副本, 让并行的 agent 不会互相碰撞。
- **Skills（技能）** —— 第 5 章里那些可重用的能力包。
- **Connectors（MCP, 连接器）** —— 第 7 章讲的工具与数据触及范围。
- **Sub-agents（子 agent）** —— 一次运行会生出的那些小帮手。

「外加的补充」指的是**外部状态／记忆**——一份 markdown 档案, 或一块 Linear 看板, 在各次运行之间把进度持久保存下来。它不是第六个平起平坐的构件; 它是那五个组件读写所在的底层基质。

他给出的实作范例是一个晨间分诊 loop, 它之所以有用, 正是因为每个环节都能对应回那五个组件里的一个。一个 **automation** 每天早上触发。一个分诊 **skill** 读取 CI 失败记录、开着的 issue、最近的 commit。隔离的 **worktrees** 各自容纳一个起草修复的 **sub-agent**, 和另一个审查它的 sub-agent。**Connectors** 负责开 PR、更新工单。没处理完的项目会浮现在分诊收件匣里, 而一份 **状态档** 会把进度持久保存下来, 让隔天早上的运行是接续而非重来。状态档是承重的那部分：没有它, loop 就不记得昨天发生过什么, 每一次运行都从零开始。

---

## 13.4 Generator 对 Evaluator

一个会自己提示自己的 loop, 天生就继承了一个难题：*谁来检查这份工作？* 如果产出变更的 agent 同时也是打分的那个, loop 就会朝着自我恭维的方向优化。被引用最多的一手论述, 其实早于命名的那一周就存在了, 这本身就很说明问题——实践跑在标签前面。**Prithvi Rajasekaran** 的《Harness design for long-running application development》（anthropic.com/engineering/harness-design-long-running-apps, 2026 年 3 月 24 日）直接记录了这个失效模式：被要求评估自己的产出时, agent「往往会以自信地称赞这份工作来回应」, 而且「在给自己的工作打分时, 稳定地偏向正面」。

他的解法, 借用了对抗式训练的结构：

> 受生成对抗网络（GAN）启发, 我设计了一个含 generator 与 evaluator agent 的多 agent 结构。

这个不对称性就是全部的洞见所在, 也是为什么值得多养一个 agent 去做这个拆分：

> 结果发现, 调教一个独立的 evaluator 让它保持怀疑, 远比让一个 generator 学会批判自己的作品要容易处理得多。

关键在于, evaluator 验证的是*行为*, 而不是 diff。在 Rajasekaran 的设计里, 它「用 Playwright MCP, 像用户一样点击浏览正在运行的应用, 测试 UI 功能、API 端点、数据库状态」, 而且它会「自己在页面上导航, 截图、仔细研究实作, 才对每一项标准打分, 写出详细的评语」。读代码不算验证; 真正把它跑起来才算。

这个 generator-evaluator 的拆分, 现在已经能在出货的 loop 控制原语里看到, 而它们之间重要的区别在于：*一个 loop 怎么知道该在什么时候停下来*：

- **`/loop`**（Claude Code v2.1.71）以固定间隔重跑一个 prompt 或斜线命令——changelog 上的说明是「新增 `/loop` 命令, 以固定间隔重跑一个 prompt 或斜线命令（例如 `/loop 5m check the deploy`）」。重复性任务在建立后七天到期; 任务最后再触发一次, 然后自我删除。
- **`/goal`**（Claude Code v2.1.139+）会一直运行*直到某个条件成立*：「一个小型快速模型会检查条件是否成立」（默认用 Haiku）, 这个独立的 evaluator 会「在每一回合之后」检查条件, 「所以是否完成, 是由一个全新的模型来决定, 而不是那个在做事的模型」。在底层, `/goal` 是「一层包在 session 范围、基于 prompt 的 Stop hook 外面的包装」。
- **Cloud Routines** 运行「在 Anthropic 托管的云端基础设施上, 所以就算你的笔电盖上了, 它们还是会继续运作」; 最短间隔是一小时, 每次运行都从一个全新的 clone 开始。
- **Codex 排程自动化** 支持每日和每周排程, 或者透过 RFC 5545 重复规则（RRULE）设定客制化的节奏。

`/loop` 和 `/goal` 之间的对比, 就是 generator-evaluator 拆分浮现成产品设计的样子。`/loop` 是*按间隔重跑*——按时钟再次触发, 不管状态如何。`/goal` 是*由条件判断终止*——由第二个独立的模型来决定工作是否已经完成。一个负责重复; 另一个负责裁决。一个正经的 loop 通常两者都需要：一个用来触发运行的触发器, 和一个知道何时该停下来的 evaluator。

---

## 13.5 生产案例：Stripe 的「Minions」（2026 年 3 月）

目前公开披露、规模最大的生产环境 loop, 是 Stripe 的 **「minions」**。Stripe 工程师 **Steve Kaliski**, 在 2026 年 3 月的 *「How I AI」* 播客（由 Claire Vo 主持）上描述了这套系统; Stripe 自己的开发者部落格用两篇 *Minions* 文章记录了内部细节。（这一集的确切播出日期在各二手来源之间有出入, 所以这里只写出月份。）

最引人注目的数字, 是无人看管产出的量。Kaliski 说 Stripe 「每周落地大约 1,300 个 PR, 除了审查以外没有任何人工协助」。Stripe 的部落格用比较保守的说法给出同一个数字：「Stripe 每周合并的 pull request 里, 超过一千个是完全由 minion 产出的」, 尽管它们「经过人工审查」, 但「不含任何人工写的代码」。

一个 minion 是从 Slack 触发的——方法是加上一个特定的表情符号反应, 或者 tag 那个 Slack app。用 Stripe 自己的话说, 「透过 tag 我们的 Slack app, 工程师可以直接从讨论某个变更的那条串里, 启动一个 minion」。

对本指南来说, 这里承重的细节是 *Stripe 把确定性与概率性的边界划在哪里。* Context 组装发生在模型运行**之前**, 而且是确定性的：「在一个 minion 运行真正开始之前, 我们会确定性地对看起来相关的链接跑相关的 MCP 工具, 好把 context 补得更饱满。」只有到了这一步之后, 概率性的部分才开始。核心 agent loop 是 Block 开源的 **Goose** 的一个 fork——「核心 agent loop 跑在 Block 的编程 agent goose 的一个 fork 上……我们很早就 fork 了它」。执行是在 Stripe 的 **devbox** 里沙盒化的; 根据 Stripe 的开发者部落格（不是播客里说的）, 「一个 Stripe devbox 就是一台 AWS EC2 实例」, 被当成「牲口, 而不是宠物」来对待——标准化、可丢弃, 而不是量身订做、长期存活。

这个框架的重点是：可靠性不是来自更聪明的模型。它来自*边界的摆放位置*——在概率性生成之前先做确定性的 context 补给——也来自人类从写代码的路径, 挪到了审查的路径上。每一个 minion PR 仍然由工程师审查。loop 把写代码这件事规模化了; 它没有移除人类, 只是把人类挪了位置。

---

## 13.6 堆叠 Loop

**LangChain** 的 *「The Art of Loop Engineering」*（Sydney Runkle, 2026 年 6 月 16 日）, 是替这一层赋予内部结构最清楚的一次尝试。它从最基本的情况讲起：

> 核心 agent 算法很简单：给 LLM context, 让它在一个 loop 里调用工具, 直到完成为止。

从这里开始, 它往上堆叠了四级阶梯。原文的标题本身就混用了「Loop」和「Level」两种标法, 这里照原文重现——**「Loop 1: The Agent」「Level 2: Verification loop」「Level 3: Event driven loop」「Level 4: Hill climbing loop」**。这个递进过程是：

1. **Loop 1: The Agent** —— 最基本的工具调用 loop, context 输进去, 调用工具直到完成。
2. **Level 2: Verification loop** —— 对 agent 产出的独立检查, 是 §13.4 的 generator-evaluator split 被套用成的一级阶梯。
3. **Level 3: Event driven loop** —— loop 由真实世界的事件触发, 而不只是靠间隔或人类的推动。
4. **Level 4: Hill climbing loop** —— 一个自我改进的 loop, 系统会随着连续运行而变得更好。

有一点需要讲精确, 因为二手报道把它讲得过头了：原文把第四级阶梯框定为*连续运行间的自我改进*, 而不是一个会改写自己 harness 的系统。这个更强的说法并不在原始来源里。Runkle 也借用了 **「loopcraft」** 这个词——但把它归功于 Swyx, 引用的是他那篇讲「loopcraft：堆叠 loop 的艺术」的文章。这个造词是 Swyx 的, 被 LangChain 引用, 而不是 LangChain 自己造的。

---

## 13.7 Outer Loop：人类保留的东西

如果说 §13.1 到 §13.6 描述的是 agent 运行的那个 loop, Osmani 的后续文章描述的, 就是人类被交代要保留的那个 loop。*《Own the Outer Loop》*（addyo.substack.com/p/own-the-outer-loop）在 2026 年 7 月 8 日于 X 上公布（Substack 版本的落款日期是 7 月 9 日）。它的拆分是：agent 现在负责运行**内层执行 loop**——调查、实作、测试／验证、报告——而工程师握着 **outer loop**。他的核心论点讲得很直白：

> 工程师拥有 outer loop。

outer loop 就是那个没有被委派出去的判断力, 用他的原话架构成三根支柱——**Quality**、**Verdict**、**Answerability**。Quality 是在 agent 行动之前运行的那些检查所形成的反压力。**Verdict** 是「工作进入我们依赖的系统之前, 我们做出的最终决定」。**Answerability** 是「如果有人问起, 我保证能解释为什么」的那个保证。（他用的词是单数的 *Verdict*, 「quality bar」不是他的原话——那根支柱就单纯叫 *Quality*。）把这些留给人类的理由是：

> Agent 可以把它写出来。但在它触及用户之前, 得有人能解释它为什么该存在、为什么安全到可以成为生产环境的一部分, 以及当它出错时该怎么办。

他点名了过度委派 outer loop 的三种失效模式：**cognitive debt（认知负债）**（「你对怎么解决问题的理解与记忆逐渐被侵蚀」）、**cognitive surrender（认知投降）**（「不假思索地接受 AI 给你的东西」）, 以及 **orchestration tax（编排税）**（生出比你的判断力实际能覆盖还多的 agent, 所拖累的成本）。这些都是按下「go」、却没有继续当那个工程师所要付出的代价。

回扣到 6 月 7 日那篇文章的这条主线, 体现在它结尾的指示里, 读起来正是在警告这件事：

> 把 loop 建出来。但要用一个打算继续当工程师的人的方式去建它, 而不是只当那个按下 go 的人。

还有这一句, 打掉了「loop 自己就能证明自己合理」的任何假设：

> 两个人可以建出一模一样的 loop, 却得到完全相反的结果。

loop 的好坏, 取决于围着它的那个 outer loop 有多好。这就是整个框架里最诚实的核心。

---

## 13.8 采用信号

三个标记显示这个框架正在扩散到最初提出者之外。每一个都只讲能核实的部分, 和它们一起流传的夸大说法都被排除在外。

**厂商。** Anthropic 的官方开发者账号 **@ClaudeDevs** 在 2026 年 7 月 6 日发布了 X Article《Getting started with loops》（截至 7 月中大约 **6.0M 曝光次数、38K+ 收藏**）。这篇材料直接教授 agentic loop 本身——「你送出的每一个 prompt, 都启动了一个由你亲自指挥每一回合的手动 loop。Claude 收集 context、采取行动、检查自己的工作、需要时重复, 然后回应」——并且走过了按回合、按目标（`/goal`）、按时间（`/loop`、`/schedule`）这三种 loop。有一个编辑上的细微差别值得保留：X article 自己的标题讲的是 *「loops」*, 而不是 *「loop engineering」*。「loop engineering」这个标签, 只出现在权威的 Claude 部落格镜像版本的框定文字里（claude.com/blog/getting-started-with-loops）, 而不在产品词汇本身。厂商教 loop 是个比厂商采用这个词更弱的信号——而目前得到核实的, 只有这个较弱的信号。

**中国。** 鱼皮 6 月 16 日那篇保姆级教程, 是通往中文开发者论述的入口。它的标题——「提示词工程已死，Loop Engineering 称王！保姆级教程 + 项目实战」——以「已死」开头, 而这个噱头, 被内文自己打了回去：这份教程自己的 層層包含 论述（§13.2）讲的是提示词技巧*被用在* loop 里面, 而不是被它杀死。作为一个粗略的触及率代理指标, 他的 GitHub 账号显示 **23.9k 关注者**。（外界流传更大的总关注数字, 但没能对照到一手来源核实, 所以在此省略。）

**记忆与评测。** loop 最依赖的那个子问题——能在各次运行之间存活的跨 session 状态——现在有了独立的基准测试。Snorkel 的 **Continual Learning Bench**（arXiv 2606.05661; Snorkel AI / UC Berkeley SkyRL / UW-Madison）把结果按 agent、记忆系统、任务这三个维度拆解。在这个基准上, 使用 **Fable 作记忆骨干的 agent 系统, 表现优于建在 Opus 或 Sonnet 上的系统**（出自 Snorkel 的 Benchtalks 访谈, 是一个定性发现——arXiv 论文里的模型名单是 Opus 4.7 / Sonnet 4.6 / Gemini 3.1 Pro / Gemini 3 Flash / GPT-5.4, 并没有给 Fable 附上具体数值分数）。发布当时, 最佳系统大约达到 **25% 的标准化增益**, in-context learning 排在排行榜首位。这里的信号不是那个数字; 而是*哪个记忆撑着这个 loop*, 现在成了一个被测量的维度。

得名五周之后, loop engineering 有了一个定义、一段和 harness 的关系陈述、一个大型生产案例、一个框架厂商的课程、一份中文主流教程, 以及一份厂商自己的 loops 材料。它没有的, 是学术文献、定型的接受度, 或者「它是真正的第四代, 而不只是配了排程器和状态档的 harness engineering」这件事上的共识。本指南把它当作正在浮现、尚未定型的东西来追踪——而 Osmani 自己的那句提醒, 两个人可以建出一样的 loop 却得到相反的结果, 是对原因最公道的总结。

---

## 来源

- **Steinberger, Peter（@steipete）。** 催化「loops, 而非 prompts」这个框定的贴文（2026 年 6 月 7 日）：[https://x.com/steipete/status/2063697162748260627](https://x.com/steipete/status/2063697162748260627) ——截至 2026 年 7 月中已有 8.4M+ 曝光次数; 贴文本身并没有用「loop engineering」这个说法。
- **Osmani, Addy.**《Loop Engineering》（2026 年 6 月 7 日）：[https://addyosmani.com/blog/loop-engineering/](https://addyosmani.com/blog/loop-engineering/); 6 月 22 日在 O'Reilly Radar 转载：[https://www.oreilly.com/radar/loop-engineering/](https://www.oreilly.com/radar/loop-engineering/) ——命名这个实践的文章; 定义、「比 harness 高一层楼」、五个组件、晨间分诊实作范例。
- **Osmani, Addy.**《Own the Outer Loop》（2026 年 7 月 8 日于 X 公布; Substack 落款日期 2026 年 7 月 9 日）：[https://addyo.substack.com/p/own-the-outer-loop](https://addyo.substack.com/p/own-the-outer-loop) ——内层 loop 与 outer loop 之分; Quality / Verdict / Answerability; cognitive debt、cognitive surrender、orchestration tax。
- **Cherny, Boris.**「Head of Claude Code: what happens next」访谈, Lenny's Podcast / Lenny's Newsletter（2026 年中）：[https://www.lennysnewsletter.com/p/head-of-claude-code-what-happens](https://www.lennysnewsletter.com/p/head-of-claude-code-what-happens) ——「我不再提示 Claude 了……我的工作是写 loop」这句话; 一句在各媒体转录不一致的口述引言, 在此附上这个但书引用。
- **Rajasekaran, Prithvi.**《Harness design for long-running application development》, Anthropic Engineering（2026 年 3 月 24 日）：[https://www.anthropic.com/engineering/harness-design-long-running-apps](https://www.anthropic.com/engineering/harness-design-long-running-apps) ——generator/evaluator（受 GAN 启发）的拆分; 保持怀疑的独立 evaluator; Playwright-MCP 行为验证。
- **Runkle, Sydney.**《The Art of Loop Engineering》, LangChain 博客（2026 年 6 月 16 日）：[https://www.langchain.com/blog/the-art-of-loop-engineering](https://www.langchain.com/blog/the-art-of-loop-engineering) ——四级堆叠阶梯（「Loop 1: The Agent」/「Level 2/3/4」）;「loopcraft」归功于 Swyx。
- **Kaliski, Steve.** Stripe「minions」, 出自 *How I AI* 与 Claire Vo 的对谈（2026 年 3 月）; Stripe 开发者部落格,《Minions》（第一、二部分）：[https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents](https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents) ——每周约 1,300 个 minion PR（人工审查、无人工写的代码）; 确定性 MCP 预先补给; Goose fork; devbox = EC2,「牲口, 不是宠物」（开发者部落格）。
- **程序员鱼皮（liyupi）。**「提示词工程已死，Loop Engineering 称王！保姆级教程 + 项目实战」, codefather.cn（2026 年 6 月 16 日）：[https://www.codefather.cn/post/2066793761979092994](https://www.codefather.cn/post/2066793761979092994) —— 層層包含 嵌套; 马匹与骑手的比喻; GitHub @liyupi 23.9k 关注者。
- **Anthropic（@ClaudeDevs）。** X Article《Getting started with loops》（2026 年 7 月 6 日）：[https://x.com/ClaudeDevs/status/2074208949205881033](https://x.com/ClaudeDevs/status/2074208949205881033); 权威镜像：[https://claude.com/blog/getting-started-with-loops](https://claude.com/blog/getting-started-with-loops) ——约 6.0M 曝光次数／38K+ 收藏（7 月中）; 教的是「loops」, 「loop engineering」这个标签是部落格镜像自己的框定说法。
- **Claude Code 产品文档：**`/loop` 与排程任务 [https://code.claude.com/docs/en/scheduled-tasks](https://code.claude.com/docs/en/scheduled-tasks)（v2.1.71; 7 天重复任务到期）;`/goal` [https://code.claude.com/docs/en/goal](https://code.claude.com/docs/en/goal)（v2.1.139+; 全新模型的条件检查; 基于 prompt 的 Stop hook 包装）; Cloud Routines [https://code.claude.com/docs/en/routines](https://code.claude.com/docs/en/routines)（Anthropic 托管基础设施; 最短一小时; 每次运行从全新 clone 开始）。
- **Codex 排程自动化**（ChatGPT/Codex 文档）：[https://learn.chatgpt.com/docs/automations](https://learn.chatgpt.com/docs/automations) ——每日／每周排程, 外加透过 RFC 5545 RRULE 设定的客制化节奏。
- **Snorkel AI / UC Berkeley SkyRL / UW-Madison。**「Continual Learning Bench」, arXiv 2606.05661（2026 年 6 月）：[https://arxiv.org/abs/2606.05661](https://arxiv.org/abs/2606.05661) ——拆解 agent／记忆系统／任务; 出自 Snorkel Benchtalks 访谈的定性 Fable-骨干发现; 发布时最佳系统标准化增益约 25%, in-context learning 领先。

---

*上一章: [第 12 章 —— 本地模型与知识工程](12-local-models.md)*

*下一章: [第 14 章 —— Graph Engineering](14-graph-engineering.md)*
