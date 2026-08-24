# 第 14 章：Graph Engineering —— 串連 Agent 組織架構

> **一句話總結：** Graph engineering 是 2026 年 7 月出現的說法, 主張 loop engineering 之上的下一層是圖——明確串連哪些 agent 存在、誰可以委派給誰, 以及它們的迴圈如何互相監督、互相糾正。
>
> **為什麼重要：** 如果這個說法站得住腳, 它就為多 agent 系統從迴圈的臨時集合變成設計出來的組織的那一層命名；如果站不住腳, 它就是這些世代標籤如何被造出來——又被拆掉——最清楚的一次現場案例研究。

這現在是本指南中壽命最短的概念, 從第 13 章手上接過這個頭銜。「graph engineering」這個詞在寫作當下大約兩週大：它在 2026 年 7 月 17–18 日之後幾天內結晶, 完全活在從業者部落格與廠商文章裡, 背後沒有任何學術文獻。它也是本指南涵蓋過爭議最大的詞。對它最大聲的單一回應——來自 LangChain, 一家框架字面上就是以圖命名的廠商——是這個實踐已經三年了, 新的只有標籤。

以下內容刻意帶著保留。懷疑者拿到跟支持者一樣多的篇幅, 各來源互相衝突的瀏覽數會被如實報告為衝突, 本章結尾用一個明確的存活關卡收尾, 而不是一個判決。

本章涵蓋催化貼文與它觸發的文章浪潮、這個新框架實際主張了什麼、對它的反擊、這個名字讓人必須做的「與知識圖譜的區分」、如果它真的是一層, 它會坐落在哪裡、中國生態系的迴響, 以及從業者現在該不該在乎。

---

## 14.1 引爆一切的那則推文（2026 年 7 月 17–18 日）

這套劇本很眼熟, 因為本指南才剛看它跑過一次。在他 6 月 7 日那則催化了 loop engineering 的貼文（第 13.1 節）六週之後, **Peter Steinberger**——OpenClaw 的創建者, 現在在 OpenAI——又發文了。根據 [Carlos E. Perez](https://medium.com/intuitionmachine/from-loop-engineering-to-graph-engineering-d3ebeb08511c) 與 [Yash Thakker](https://explainx.ai/blog/graph-engineering-ai-agents-multi-agent-organizations-2026) 逐字引用, 這則貼文寫道：

> 我們還在談迴圈, 還是已經換到圖了？

在講任何東西之前先講兩個來源上的但書, 因為這正是本章存在的目的。第一, 這則貼文本身沒有為本指南直接抓取, 而各自獨立抓取的二手來源對它的呈現也不完全一致。只有 Perez 和 Thakker 逐字引用了這個確切的英文用字。[LangChain](https://www.langchain.com/blog/3-years-of-graph-engineering-with-langgraph) 和 Perez 連結了這則貼文但沒有引用其文字；[36kr](https://eu.36kr.com/en/p/3904771418867330) 和 Tony Bai 用中文翻譯來呈現它, 36kr 的英文版又把它回譯成「Are we still talking about loops, or have we moved on to graphs?」；而 [Eigent](https://www.eigent.ai/blog/graph-engineering-ai-agents) 則是用改述的方式。這兩份逐字引用, 是上面之所以能印出那句話的唯一依據。

第二, 它周圍的數字對不上。每一個為這則貼文標日期的來源都標的是 7 月 18 日；本章標題所用範圍中 7 月 17 日那一端, 是一種美國時區的可能性, 不是來源之間有記載的分歧。瀏覽數確實互相衝突, 不過它們是在不同時刻拍下的快照, 而不是對同一個時間點的競爭測量：Thakker 回報數小時內 575K 次瀏覽, 36kr 是兩天內 2.6M（同一篇文章對照六週前那則 8.4M 瀏覽的 loop 世代貼文）, Tony Bai 則是兩天內大約 800K。這裡不把任何單一數字當成事實陳述。

跟 6 月那則貼文一樣, Steinberger 什麼都沒命名。「graph engineering」這個詞組在他的文字裡完全沒出現。這個複合詞是在幾天內於回應文章中結晶的, 有意識地仿照 prompt、context、harness、loop engineering 的模式——而且這波浪潮很快：

- **7 月 18 日**——[Yash Thakker 的 explainx.ai 教程](https://explainx.ai/blog/graph-engineering-ai-agents-multi-agent-organizations-2026)（更新到 7 月 26 日）把這則推文點名為催化劑, 並提供了 org-graph／work-graph 的拆分。
- **7 月 19 日**——**Carlos E. Perez**（Intuition Machine）發表第一篇有實質分量的理論擴充。
- **7 月 20 日**——企業廠商 **TrueFoundry** 出貨一份[面向生產的教程](https://www.truefoundry.com/blog/graph-engineering-enterprise-guide), 附治理檢查清單。
- **7 月 21 日**——**eigent.ai** 發表它的廠商文章；中國的 **Tony Bai** 與 **36kr** 同一天都報導了這場論述（14.6）。
- **7 月 22 日**——**LangChain** 由 Sydney Runkle 與 Harrison Chase 執筆的官方回應, 在催化劑之後第四天落地（14.3）。

一個催化劑、一波文章浪潮、一個廠商反框架、一次中國生態系的迴響, 全部發生在一週之內：loop-engineering 的命名序列, 用更快的速度重播了一遍。

---

## 14.2 Graph Engineering 聲稱自己是什麼

把這些文章剝到最精簡, 有三個說法反覆出現。

**Agent 組織, 不是 agent 行為。** Thakker 的框定是這個演進裡最好引用的版本：

> 迴圈讓 agent 行為變得可程式化。圖讓 agent 組織變得可程式化。

他的教程把圖拆成兩個不同的物件：

- **org graph（組織圖）**——哪些 agent 存在、每個是幹嘛用的、哪些委派邊被允許, 這張穩定的圖表；
- **work graph（工作圖）**——某個特定工作所生出、執行、丟棄的短暫任務分解。

這個主張是：兩者現在都是要被設計、版本化、審查的工程產物, 就像第 4 章對待 harness、第 13 章對待迴圈那樣。

**迴圈監督迴圈, 被 anchor 摁住。** [Perez 的文章](https://medium.com/intuitionmachine/from-loop-engineering-to-graph-engineering-d3ebeb08511c)——第一篇理論擴充, 7 月 19 日——把圖描述成一個由互相監督、互相約束的迴圈組成的網路。他獨到的補充是 **anchor（錨點）**：一個無可爭辯、對外扎根的測量（一個測試結果、一個指標、一次事實查核）, 圖中某個節點必須碰到它。他主張, 沒有 anchor, 一個由互相審查的 agent 組成的圖會退化成一個回聲室, 收斂到有信心的一致同意, 而不是收斂到正確——這是第 13.4 節為單一迴圈記錄過的自我評分失效模式的多 agent 版本。

**受治理的拓撲。** 廠商文章——[TrueFoundry](https://www.truefoundry.com/blog/graph-engineering-enterprise-guide)（7 月 20 日）與 [Eigent](https://www.eigent.ai/blog/graph-engineering-ai-agents)（7 月 21 日, 同時歸功於 Steinberger 的貼文與 Perez 的迴圈網路擴充）——收斂到同一種運營上的解讀：graph engineering 是 agent 拓撲的治理與可觀測性。照這個解讀, 它所擁有的問題是：

- agent 之間哪些轉移被允許, 哪些在結構上根本不可能；
- 一個失敗在級聯擴散到整個組織之前, 在哪裡被隔離；
- work graph 裡一個失控的分支要怎麼被偵測並切斷；
- 對一個 agent 組織的稽核到底長什麼樣子。

TrueFoundry 為這些問題出貨了一份企業檢查清單；這份清單是否需要一個新的學科名稱才能存在, 正是下一節要處理的問題。

**廠商出貨的是結構, 不是名字。** 2026 年 8 月 7 日（Claude Code v2.1.224, 到 8 月 23 日迭代至 v2.1.241）, Anthropic 出貨了跨 session 的 agent 訊息傳遞：`ListAgents` 能發現具名的 session——子 agent、agent-team 隊友、其他本機 session、雲端 session, 以及其他機器上的 Remote Control session——`SendMessage` 則按名字在它們之間傳遞純文字, 由每個 session 各自的入站治理（接受／保留／拒絕）、一個基於許可模式的預設值, 以及大小／突發／迴圈節流來把關。範圍被刻意收窄：對話歷史或檔案不跨 session、沒有跨 session 的許可核准, 而且這個功能在 Bedrock、AWS 上的 Claude Platform、Google Cloud Agent Platform、Microsoft Foundry 上都不可用。對照上面剛定義的 org graph——一份具名 agent 的穩定名冊加上被允許的委派邊——這看起來就是它的一個出貨實例：具名、可定址的 session, 加上它們之間受治理的訊息邊。它不是的東西, 是詞彙上的採用：Anthropic 自己的文件與 changelog 從頭到尾沒有用「graph engineering」這個詞組來描述這個功能。這個落差——一個主要 harness 廠商把本章追蹤的模式產品化, 卻對為它造出來的標籤保持沉默——是原語的證據, 不是這個詞的證據, 兩者不是同一個主張。

---

## 14.3 反擊

懷疑者在這裡該得到同等的份量, 而不是一段禮貌性的段落, 因為在四天之內, 這場論述就從最有資格提出反駁的那一方, 產出了它自己最有力的反論。

**LangChain：這已經三年了。**《[3 Years of Graph Engineering with LangGraph](https://www.langchain.com/blog/3-years-of-graph-engineering-with-langgraph)》（Sydney Runkle 與 Harrison Chase, 2026 年 7 月 22 日）同時做了兩件事。它讓這個詞取得正當性——這篇文章明確把 graph engineering 排在「prompt engineering、context engineering、harness engineering、loop engineering」之後, 這正是本指南追蹤的那條世代脊椎, 多加了一個階梯。而它又在同一口氣裡把這個詞洩了氣：

> 把 agentic 系統表示成圖並不新, 我們已經這樣做三年了。

他們的化約很乾淨：**迴圈就只是一個有向、有環的圖。** LangGraph 從 2023 年起就把 agent 建模成圖拓撲——節點、邊、條件轉移、環。照這個解讀, 2026 年 7 月除了詞彙以外什麼都沒變：這個實踐比這個標籤早了三年, 而標籤加上的是一個名字, 不是一種能力。

注意這對證據基礎做了什麼。graph engineering 目前最強的採用訊號——一個主要框架廠商在四天內做出回應——同時也是它最強的懷疑來源。同一份文件兩者皆是, 任何誠實的說明都必須把它同時當成這兩者來承載。

**Tony Bai：今天的框架, 明天的棄置堆。** 這位中國開發者基礎設施作家的 [7 月 21 日貼文](https://tonybai.com/2026/07/21/from-loop-engineering-to-graph-engineering/), 用同情的角度解釋了迴圈監督迴圈與 anchor 的框定, 然後話鋒一轉：loop engineering 才紅不到兩個月, 矽谷就已經產出下一個詞, 而「graph」本身也可能是明天被丟棄的流行語。這句警告出自一個早期就仔細講解過迴圈框架的人——他的懷疑不是反射性的反炒作——反而讓這個警告落地得更重。

**證據缺席說明了什麼。** 進行到第二週, 沒有任何研討會演講、沒有課程、也沒有職缺公告使用這個詞；為本指南做的搜尋一個都沒找到。這既符合一個未滿兩週的詞的樣子, 也同樣符合一個不會持久的詞的樣子。誠實的說法是：證據目前還無法區分這兩者。

---

## 14.4 不是知識圖譜

這個名字帶著一個本指南在結構上有義務要拆除的碰撞, 因為第 2 章從本指南一開始就已經在講圖了。「知識圖譜工程」是一門確立已久、超過十年歷史的學科——語意網、本體、三元組資料庫——而 GraphRAG（第 2 章）建構實體與關係的圖, 讓系統能對它所知道的東西做檢索與推理。2026 年 7 月意義上的 graph engineering, 除了這個詞以外, 跟這個沒有任何共同之處。TrueFoundry 的區分是目前最清楚的一個版本, 值得引用來當作這條界線：

> 知識圖譜結構化一個系統*知道什麼*；2026 年意義上的 graph engineering, 結構化一個系統*是誰*——它的成員、授權、訊息路徑。

並排放在一起看, 這兩種圖除了資料結構以外沒有任何共同點：

| | 知識圖譜／GraphRAG（第 2 章） | Graph Engineering（本章） |
|---|---|---|
| 節點 | 實體 | Agent |
| 邊 | 標記的關係 | 被允許的委派 |
| 建構時機 | 索引時 | 架構設計時 |
| 使用時機 | 檢索時 | 執行時（被走訪, 也被變異） |
| 回答的問題 | 系統知道什麼？ | 系統是誰？ |

從第 2 章的 GraphRAG 小節看到這一章的讀者, 應該把這個共用的詞當成詞彙上的巧合, 而不是血緣上的共享。（第 2 章帶著反向的指標。）

---

## 14.5 它坐落在哪裡——第五世代, 還是第四代的重構？

如果這個框架存活下來, 它在本指南的演進故事裡要放在哪裡？本指南的脊椎是從 prompt（第 1 章）到 context（第 1–3 章）到 harness（第 4 章）到迴圈（第 13 章）。支持者的答案是：再多一層樓。LangChain 自己的排列——把 graph engineering 排在 prompt、context、harness、迴圈之後——把它放成第五個階梯, 即便同時在質疑它的新穎性。

這個時間窗內最有用的結構性處理, 也是最新的一篇。[MarkTechPost 7 月 29 日的文章](https://www.marktechpost.com/2026/07/29/prompt-engineering-vs-loop-engineering-vs-graph-engineering-what-changes-at-each-layer/)主張這些層不是接續關係, 而是堆疊起來的控制單元：

- **harness**（第 4 章）是圍繞單一 agent 的環境；
- **迴圈**（第 13 章）是單一 agent 的行為週期；
- **圖**協調多個 agent, 透過一張穩定的組織圖加上一張短暫的工作圖。

它的貫穿線——「圖是由迴圈建成的, 迴圈是由 prompt 建成的」——是第 1 章共存論點多加了一個框的延伸, 也是與本指南對待更早層次的方式最相容的一種解讀。

但那個洩氣式的解讀也符合同一組事實。如果迴圈就只是一個有向環圖（LangChain 的說法）, 那麼一個由迴圈組成的圖就是一個更大的迴圈系統, 而「graph engineering」就是把 harness 加迴圈工程套用到 N 個 agent 而不是 1 個——是第四層的重構, 不是第五層。第 13 章留下了 loop engineering 究竟是不是真正的一層, 還是「配了排程器的 harness engineering」這個開放問題；graph engineering 繼承了這個開放問題, 又加上了它自己的一個。本指南不打算解決它。這個框架才兩週大；解決它會變成認證, 而不是描述。

---

## 14.6 中國生態系的迴響

一個框架已經逃出它的原生泡泡的較強訊號之一, 是中國開發者生態系接手它的速度有多快, 而這次的迴響在三天內就出現了, 而且已經帶著一個定型的翻譯：**圖工程**。

已驗證的錨點有兩個。[Tony Bai 7 月 21 日的貼文](https://tonybai.com/2026/07/21/from-loop-engineering-to-graph-engineering/)——標題：「Loop Engineering才火兩個月，矽谷已經捲出"Graph Engineering"了」——是一篇實質的解說, 為中國基礎設施受眾涵蓋了 Perez 的迴圈監督迴圈與 anchor, 並附上 14.3 節的流行語警告。而 [36kr 英文版的報導](https://eu.36kr.com/en/p/3904771418867330)（同樣是 7 月 21 日）把這場論述當新聞處理：它報導了 14.1 節的瀏覽數比較, 並點名 Geoffrey Huntley、Boris Cherny、Addy Osmani、Luis Catacora 是這場論述的參與者。（這些歸屬僅依據 36kr 單一來源, 在此也只作為這樣的引用。）

超出這兩個之外, 迴響就薄成只剩標題。中文搜尋浮現出兩篇 CSDN 智能體開發者社區的文章——一篇標題冷靜, 叫「從Loop Engineering到Graph Engineering」, 一篇跑滿整套炒作模板, 叫「Loop工程已死，Graph工程永生」（「loop engineering 已死, graph engineering 永生」——跟第 13.8 節記錄過的 loop 那波浪潮同一個「已死」噱頭）——還有一篇繁體中文解說。這三篇都沒有為本指南獨立抓取；它們是以搜尋結果標題的身分被引用, 是 CN 內容管線已經接手這個詞的證據, 僅此而已。

這個模式從第 13 章看來很眼熟：把 loop-engineering 解說文章工業化的那條管線, 現在正在處理圖工程, 從催化劑到催化劑大約有六週的延遲, 但從催化劑到迴響只有幾天。

---

## 14.7 你現在該在乎嗎？

在 2026 年 7 月下旬讀到這裡的從業者, 需要兩個分開的答案, 因為標籤跟問題是可以拆開的。

**不管標籤是什麼, 這些問題都是真的。** 如果你在一個 harness 裡跑一個 agent、一個迴圈, 本章裡的東西都不會改變你的工作；第 4 章跟第 13 章依然是在起作用的層。如果你已經在把多個 agent 串在一起, 這些文章點名的關切——哪些委派邊被允許、一個失敗在級聯之前在哪裡被隔離、什麼會被觀測與稽核、哪個節點碰到 anchor 讓系統不會漂移進自我一致——不管「graph engineering」有沒有作為它們的名字存活下來, 都是你本來就有的工程問題。TrueFoundry 的檢查清單與 Perez 的 anchor, 現在不管用哪套詞彙都能用。LangChain 的反駁, 在這一點上其實是同意：他們已經在做這些圖的工程三年了, 這代表這些問題至少已經三年了。

**這個標籤是一個你不必下的賭注。** 本指南在 loop engineering 五週大的時候幫它開了第 13 章；graph engineering 在兩週大的時候就拿到一章, 早期證據嚴格來說更強（更快的文章浪潮、同一週的框架廠商回應、更快的中國迴響）, 而成熟度嚴格來說更弱（沒有可跟 Stripe 的 minions 相比的生產案例研究、沒有廠商教材、沒有基準測試）。所以本章用一個關卡而不是一個判決收尾。**存活測試是：這個詞到 2026 年 9 月是否還在流通。** 具體來說, 要留意：

- 框架或廠商文件在產品詞彙裡採用這個詞, 而不只是部落格框定；
- 用它的研討會演講、課程、或職缺公告（寫作當下：一個都沒找到）；
- 一個份量跟 Stripe 的 minions 給 loop engineering 的份量相當的具名生產案例研究；
- 一波不是為了回應某一則貼文而寫的第二次文章浪潮。

如果這些出現, 本章會像第 13 章那樣長大。如果沒有, 本章就會作為一次為期兩週的命名事件的紀錄留在這裡, 而洩氣式的解讀就贏了。

本指南把 graph engineering 當作一個正在被檢驗的主張來追蹤, 而不是一個已經定型的層——而 Tony Bai 的警告, 今天的框架可能是明天被丟棄的流行語, 是對這個賭注最公道的一句總結。

---

## 來源

- Steinberger, Peter. X 貼文,「Are we still talking loops or did we shift to graphs yet?」（2026 年 7 月 18 日, 依下方每個標了日期的來源）——沒有為本指南直接抓取, 僅透過這些來源引用：被 Perez 與 Thakker（explainx）逐字引用, 被 LangChain 與 Perez 連結但未引文, 被 36kr 與 Tony Bai 譯成中文, 被 Eigent 改述。各家回報的瀏覽數彼此衝突。
- Runkle, Sydney 與 Harrison Chase（LangChain）。「3 Years of Graph Engineering with LangGraph」（2026 年 7 月 22 日）：[https://www.langchain.com/blog/3-years-of-graph-engineering-with-langgraph](https://www.langchain.com/blog/3-years-of-graph-engineering-with-langgraph)——把 graph engineering 排在 prompt/context/harness/loop 之後；「一個迴圈就只是一個有向環圖」；「這個實踐已經三年了」的反擊。
- Perez, Carlos E.（Intuition Machine）。「From Loop Engineering to Graph Engineering?」（2026 年 7 月 19 日）：[https://medium.com/intuitionmachine/from-loop-engineering-to-graph-engineering-d3ebeb08511c](https://medium.com/intuitionmachine/from-loop-engineering-to-graph-engineering-d3ebeb08511c)——第一篇理論擴充；迴圈監督迴圈；anchor 作為對抗回聲室的無可爭辯測量。
- Thakker, Yash（explainx.ai）。「Graph Engineering: After Loops, This Is How You Wire Multi-Agent Orgs (2026)」（2026 年 7 月 18 日, 更新至 7 月 26 日）：[https://explainx.ai/blog/graph-engineering-ai-agents-multi-agent-organizations-2026](https://explainx.ai/blog/graph-engineering-ai-agents-multi-agent-organizations-2026)——org graph 對 work graph；「迴圈讓 agent 行為變得可程式化。圖讓 agent 組織變得可程式化。」
- TrueFoundry。「Graph Engineering for Multi-Agent Systems: Architecture, Governance, and Observability」（2026 年 7 月 20 日）：[https://www.truefoundry.com/blog/graph-engineering-enterprise-guide](https://www.truefoundry.com/blog/graph-engineering-enterprise-guide)——企業檢查清單；與知識圖譜區分的引言（「系統知道什麼」對「系統是誰」）。
- Eigent。「Graph Engineering for AI Agents」（2026 年 7 月 21 日）：[https://www.eigent.ai/blog/graph-engineering-ai-agents](https://www.eigent.ai/blog/graph-engineering-ai-agents)——歸功於 Steinberger 的貼文與 Perez 的擴充；互相糾正的迴圈組成的受治理拓撲。
- 36kr（英文版）。「Father of Lobster's One Tweet: Is the Loop Era Over?」（2026 年 7 月 21 日）：[https://eu.36kr.com/en/p/3904771418867330](https://eu.36kr.com/en/p/3904771418867330)——報導這則推文有 2.6M 次瀏覽, 對比 8.4M 次瀏覽的 loop 世代貼文；點名額外的論述參與者；把這個詞當作正在浮現來處理。
- Bai, Tony.「Loop Engineering才火兩個月，矽谷已經捲出"Graph Engineering"了」（2026 年 7 月 21 日）：[https://tonybai.com/2026/07/21/from-loop-engineering-to-graph-engineering/](https://tonybai.com/2026/07/21/from-loop-engineering-to-graph-engineering/)——為中國生態系寫的圖工程解說；警告「graph」本身可能變成被丟棄的流行語。
- MarkTechPost。「Prompt Engineering vs Loop Engineering vs Graph Engineering: What Changes at Each Layer」（2026 年 7 月 29 日）：[https://www.marktechpost.com/2026/07/29/prompt-engineering-vs-loop-engineering-vs-graph-engineering-what-changes-at-each-layer/](https://www.marktechpost.com/2026/07/29/prompt-engineering-vs-loop-engineering-vs-graph-engineering-what-changes-at-each-layer/)——堆疊控制單元的解讀；org graph + work graph；「圖是由迴圈建成的, 迴圈是由 prompt 建成的」。
- Claude Code（Anthropic）。跨 session 訊息傳遞文件與 changelog（2026 年 8 月 7 日, v2.1.224；到 8 月 23 日迭代至 v2.1.241）：[https://code.claude.com/docs/en/cross-session-messaging](https://code.claude.com/docs/en/cross-session-messaging)；[https://code.claude.com/docs/en/changelog](https://code.claude.com/docs/en/changelog)——ListAgents/SendMessage 出貨了具名 agent 發現與跨 session 受治理的訊息邊；「graph engineering」這個詞組在兩個頁面裡都完全沒出現。

---

*上一章: [第 13 章 —— Loop Engineering](13-loop-engineering.md)*
