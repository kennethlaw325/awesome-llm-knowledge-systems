# 第 13 章：Loop Engineering —— 設計提示 Agent 的系統

> **一句話總結：** Loop engineering 是建構那套幫你提示 agent 的系統的實踐——讓你不再每個回合親自出手, 而是開始設計會自己運行、檢查、餵養自己的迴圈。
>
> **為什麼重要：** 它是本指南演進故事裡最新、最未定型的一層, 也最可能在未來一年決定自主 agent 工作實際上怎麼被排程、驗證、審查。

這是本指南中壽命最短的概念。（它保持這個頭銜六週：2026 年 7 月下旬, 同一套劇本又產出一個聲稱在迴圈之上還有一層的說法, graph engineering, 見[第 14 章](14-graph-engineering.md)。）「loop engineering」這個詞在寫作當下大約五週大：它在 2026 年 6 月初被命名, 幾天內就散播到從業者部落格、podcast、X 上, 而且至今背後沒有任何學術文獻。以下內容刻意帶著保留。當某個說法建立在一句被轉錄成三種不同版本的 podcast 口述引言上, 或建立在一則什麼都沒命名的爆紅貼文上, 本章會明講這一點。目標是準確描述一個正在浮現的框架, 而不是把它認證成一個已定型的世代。

這個框架值得描述, 因為它在從業者論述中確實在起作用：它為一個轉變命名, 這個轉變是第 4 章的 harness engineering 暗示過但沒有單獨拆出來的——從*提示 agent* 移到*設計提示 agent 的系統*。這是否值得擁有自己的一層, 還是只是加了個排程器的 harness engineering, 正是本章留待開放的問題。

本章涵蓋這個詞從哪裡來、支持者如何把它跟 harness 連上關係、迴圈由什麼構成、讓迴圈誠實的 generator-evaluator split、一個大型生產案例、堆疊迴圈的框架、人被告知要保留的判斷, 以及採用的早期訊號——有爭議的部分會全程標明。

---

## 13.1 它得名的那一週（2026 年 6 月）

催化劑是單單一則貼文。2026 年 6 月 7 日, **Peter Steinberger**（@steipete）——**OpenClaw** 的創建者, Y Combinator 形容它「從一個週末專案, 在不到 5 個月內變成 GitHub 上星數最多的軟體 repo, 拿下 346k+ 星」, 超越 React, 而他現在在 OpenAI ——寫道：

> 這是你每月一次的提醒：你不應該再親自提示 coding agent 了。
>
> 你應該設計會提示你 agent 的迴圈。

這則貼文截至 2026 年 7 月中已累積 **8.4M+ 次曝光**。它什麼都沒命名：Steinberger 沒有用「loop engineering」這個詞, 這幾個字在他的文字裡完全沒出現。命名來自其他人對他所催化的想法的回應。

同一天, **Addy Osmani**（Google）發表了給這個實踐命名的文章（《Loop Engineering》, addyosmani.com/blog/loop-engineering/, 6 月 7 日；6 月 22 日在 O'Reilly Radar 轉載）。他的定義是後續論述引用的那個版本：

> Loop engineering 是把你自己從那個提示 agent 的人的位置換掉。你改為設計一個代替你做這件事的系統。

同一個轉變也出現在前沿實驗室內部。**Boris Cherny**, Anthropic Claude Code 的創建者兼負責人, 在 2026 年中一集 podcast 上用同樣方式框定自己的工作流。根據 Lenny's Podcast 訪談中被引用最多的轉錄版本：

> 我已經不再親自提示 Claude 了。我有迴圈在跑, 由它們提示 Claude 並想出該做什麼。我的工作是寫迴圈。

這句引言需要一個但書, 而這正是本章存在的目的所在的那種但書。它是一句*口述*台詞, 在不同媒體上被轉錄得不一致（有些引用 Acquired podcast 而非 Lenny's）, 也沒有可靠的逐字文本或完整轉錄可查。其實質內容——Cherny 不再親自提示, 而是寫會提示 Claude 並決定下一步動作的迴圈——在多個二手來源中得到印證；但確切用字並不固定。

合起來看, 6 月 7 日那一週產出了一個催化劑（Steinberger）、一個名稱與定義（Osmani）、一個內部人的迴響（Cherny）。它沒有產出的是共識。這個詞在幾週內就在從業者論述中結晶, 但接受度分裂：一部分讀者稱它是真正的轉變, 另一部分稱它為時過早——是排程的改名, 或「配了 cron job 的 harness」。沒有任何同行評審著作使用這個詞。本指南把 loop engineering 當作一個正在浮現、有爭議的框架來處理（見第 1 章第四世代小節）, 這也是為什麼以下每個承重的說法都繫著一個主要來源, 而空白處會被明講而不是被填上。

---

## 13.2 在 harness 之上一層樓

支持者做出的最乾淨的定義動作, 是把迴圈直接放在第 4 章的 harness 之上。Osmani 直接說明了這層關係：

> Loop engineering 坐落在 harness 之上的一層樓。

他對迴圈*是什麼*的心智模型, 把 harness 保留為建構區塊：迴圈是那個「跑在計時器上、會生出小幫手、會餵養自己」的 harness。他明確表示這是延伸早期的工作, 而不是取代它——他「先前寫過這個的表親, agent harness engineering, 那是在打造一個單一 agent 跑在其中的環境」。

中國開發者 **程序員魚皮**（liyupi）給出這層關係中結構性最強的版本。在他 6 月 16 日的教程（codefather.cn）中, 他把 prompt 技巧、context 管理、harness 搭建、迴圈安排成**層層包含**的關係：

> 這四者是層層包含的關係。提示詞技巧、上下文管理、Harness 搭建，這些能力在 Loop 裡面全都要用上。

（這四者是巢狀的；prompt 技巧、context 管理、harness 搭建全都是在迴圈*裡面*被用到。）這和第 1 章套用在 prompt → context → harness 上的巢狀分層邏輯完全一樣, 只是往外多加了一個框。歸屬要講精確：魚皮是在為中國開發者受眾重新包裝、結構化既有詞彙, 而不是創造它們——「harness engineering」與「loop engineering」都可追溯到 Claude Code 與 Cherny 的論述。

他的馬匹隱喻, 把 harness／迴圈的界線畫得比任何人都清楚：

> 如果把 AI 比作一匹馬，Harness 就是你給馬裝上的韁繩、馬鞍和圍欄，然後你騎在馬上手動駕馭它。

（如果把 AI 比作一匹馬, harness 就是你給牠裝上的韁繩、馬鞍、圍欄——然後你騎在牠身上手動駕馭牠。）

> 而 Loop 呢，是你設定好一條巡邏路線後，不用上馬，讓馬自己按路線一圈一圈地跑。

（Loop 則是你設定好一條巡邏路線之後, *不用上馬*——馬自己按路線一圈一圈地跑。）

這個隱喻編碼了讓 loop engineering 不會塌縮成「agent 版 cron」的那個單一區別：**迴圈不是排程器。** 排程器按時觸發。迴圈按時觸發*, 然後讀取當前狀態來決定這一輪要做什麼*。那個 runtime 決策者——會先檢查 CI 狀態、開著的 issue、或上一輪跑剩的東西, 才選擇行動的那部分——正是一則 cron 條目所沒有的。迴圈是排程器加上一個每輪都重新決策的讀狀態 agent。（交叉參照：第 1 章,「關鍵洞察：共存, 而非取代」。）

---

## 13.3 迴圈由什麼構成

Osmani 的文章提供了最具體的清單。他那節的標題是 **「五個零件, 然後是附註」**——這個數字很重要, 因為很容易被灌水。是*五個零件加上外部狀態*, 不是六個地位相等的建構區塊：

- **自動化（Automations）**——啟動迴圈的觸發器（排程、事件）。
- **Worktree**——隔離的工作副本, 讓並行的 agent 不會互撞。
- **技能（Skills）**——第 5 章那種可重用能力包。
- **連接器（Connectors, MCP）**——第 7 章的工具與資料觸及範圍。
- **子 agent（Sub-agents）**——一次執行會生出的小幫手。

那個「附註」是**外部狀態／記憶**——一個 markdown 檔或一個 Linear 板, 在各輪執行之間持久保存進度。它不是第六個地位相等的區塊；它是那五個零件寫入與讀取的基底。

他的實例是一個晨間分診迴圈, 之所以有用正是因為每個零件都對得上那五個之一。一個**自動化**每天早上觸發。一個分診**技能**讀取 CI 失敗、開著的 issue、最近的 commit。隔離的 **worktree** 分別容納一個起草修復的**子 agent** 和一個審查它的第二個子 agent。**連接器**開 PR、更新工單。未解決的項目浮現到一個分診收件匣, 一個**狀態檔**持久保存進度, 讓隔天早上的執行接續下去而不是重新開始。狀態檔是承重的部分：沒有它, 迴圈就沒有昨天的記憶, 每次執行都得從零開始。

---

## 13.4 Generator 對 Evaluator

一個會自我提示的迴圈, 繼承了一個難題：*誰來檢查這份工作？* 如果產出變更的 agent 同時也給它打分, 迴圈就會朝自我恭維最佳化。被引用最多的主要論述, 時間上早於命名那一週, 這件事本身就很說明問題——實踐跑在了標籤前面。**Prithvi Rajasekaran** 的《Harness design for long-running application development》（anthropic.com/engineering/harness-design-long-running-apps, 2026 年 3 月 24 日）直接記錄了這個失效模式：被要求評估自己的輸出時, agent「傾向於自信地稱讚自己的工作」, 而且「在給自己的工作打分時可靠地偏向正面」。

他的解法借用了對抗訓練的結構：

> 受生成對抗網路（GAN）啟發, 我設計了一個含 generator agent 與 evaluator agent 的多 agent 結構。

這種不對稱就是整個洞察所在, 也是這個拆分值得多養一個 agent 的原因：

> 事實證明, 把一個獨立的 evaluator 調到懷疑論式的態度, 遠比讓 generator 學會批判自己的工作容易處理得多。

關鍵在於, evaluator 驗證的是*行為*, 不是 diff。在 Rajasekaran 的設計裡, 它「用 Playwright MCP 像使用者一樣點過整個跑著的應用程式, 測試 UI 功能、API 端點、資料庫狀態」, 而且它「會自己導覽頁面, 截圖並仔細研究實作, 才對每一項標準打分並寫出詳細評語」。讀程式碼不算驗證；跑起來才算。

這個 generator-evaluator split 現在能在已出貨的迴圈控制原語中看到, 而它們之間重要的區別在於*迴圈怎麼知道該停了*：

- **`/loop`**（Claude Code v2.1.71）在一個重複間隔上重跑一個 prompt 或斜線指令——changelog 的行是「新增 `/loop` 指令, 在重複間隔上跑一個 prompt 或斜線指令（例如 `/loop 5m check the deploy`）」。重複任務在建立後七天過期；任務會最後觸發一次, 然後自己刪除。
- **`/goal`**（Claude Code v2.1.139+）*跑到某個條件成立為止*：「一個小型快速模型會檢查條件是否成立」（預設用 Haiku）, 一個獨立的 evaluator 在「每個回合之後」檢查這個條件, 「所以完成與否是由一個全新的模型決定, 而不是做這份工作的那個」。在底層, `/goal` 是「一個包在 session 範圍、基於 prompt 的 Stop hook 外面的包裝」。
- **Cloud Routines** 跑在「Anthropic 託管的雲端基礎設施上, 所以你筆電關著它們也繼續動」；最小間隔是一小時, 每次執行都從一個全新的 clone 開始。
- **Codex 排程自動化** 支援每日與每週排程, 或透過 RFC 5545 重複規則（RRULE）設定的客製節奏。

`/loop` 對比 `/goal` 的對照, 就是 generator-evaluator split 浮現為產品設計的樣子。`/loop` 是*按間隔重跑*——不管狀態, 時間到就再觸發一次。`/goal` 是*由條件判定終止*——由第二個獨立模型決定工作何時完成。一個負責重複；另一個負責裁決。一個認真的迴圈通常兩者都需要：一個觸發它跑的東西, 一個知道何時該停的 evaluator。

---

## 13.5 生產案例：Stripe 的 Minions（2026 年 3 月）

目前公開揭露、跑在生產環境裡規模最大的迴圈, 是 Stripe 的**「minions」**。Stripe 工程師 **Steve Kaliski** 在 2026 年 3 月的*「How I AI」* podcast（由 Claire Vo 主持）上描述了這套系統；Stripe 自家的開發者部落格用兩篇《Minions》文章記錄了內部細節。（單集播出日在二手來源之間有爭議, 所以這裡只寫月份。）

頭條數字是無人看管產出的量。Kaliski 說 Stripe「每週落地大約 1,300 個 PR, 除了審查以外沒有任何人類協助」。Stripe 的部落格用更保守的方式陳述同一個數字：「Stripe 每週合併的 PR 中有超過一千個完全是 minion 產出」, 雖然它們「有人類審查」, 但「不含任何人類寫的程式碼」。

一個 minion 是從 Slack 觸發的——透過加上特定的表情符號反應, 或是 tag Slack app。用 Stripe 的話說：「透過 tag 我們的 Slack app, 工程師可以直接從討論某個變更的 thread 裡啟動一個 minion」。

對本指南而言, 承重的細節是 *Stripe 把決定性／機率性的邊界畫在哪裡*。Context 組裝發生在模型跑**之前**, 而且是決定性的：「我們在一個 minion 執行甚至開始之前, 就對看起來相關的連結決定性地跑相關的 MCP 工具, 好把 context 填得更飽滿。」只有到這之後, 機率性的部分才開始。核心 agent 迴圈是 Block 開源的 **Goose** 的一個 fork——「核心 agent 迴圈跑在 Block 的 coding agent goose 的一個 fork 上……我們很早就把它 fork 了」。執行被沙盒在 Stripe 的 **devbox** 裡；根據 Stripe 的開發者部落格（不是 podcast）,「一個 Stripe devbox 就是一個 AWS EC2 執行個體」, 被當作「牲口, 不是寵物」——標準化、可拋棄, 而不是量身訂做、長壽命。

這個框架的重點是：可靠性不是來自更聰明的模型。它來自*邊界的擺放位置*——在機率性生成之前先做決定性的 context 填充——也來自人類從寫的路徑移到審查的路徑。每個 minion PR 仍然由工程師審查。迴圈把寫的部分規模化了；它沒有移除人類, 只是把他們搬了位置。

---

## 13.6 堆疊迴圈

**LangChain** 的《The Art of Loop Engineering》（Sydney Runkle, 2026 年 6 月 16 日）是給這一層賦予內部結構最清楚的一次嘗試。它從最基本的情況出發：

> 核心 agent 演算法很簡單：給 LLM context, 讓它在一個迴圈裡呼叫工具, 直到完成為止。

從那裡開始它堆疊出四個階梯。該頁面自己的標題混用「Loop」跟「Level」兩種標籤, 這裡按原文重現——**「Loop 1: The Agent」、「Level 2: Verification loop」、「Level 3: Event driven loop」、「Level 4: Hill climbing loop」**。演進如下：

1. **Loop 1: The Agent**——最基本的工具呼叫迴圈, context 進去, 呼叫工具直到完成。
2. **Level 2: Verification loop**——對 agent 輸出的獨立檢查, 是 §13.4 的 generator-evaluator split 被套用成一個階梯。
3. **Level 3: Event driven loop**——迴圈由現實世界的事件觸發, 不只是間隔或人類的推動。
4. **Level 4: Hill climbing loop**——一個自我改善迴圈, 系統在連續執行中變得更好。

有一個精確度的補充要講, 因為二手報導把它講得過頭了：該頁面把第四個階梯框為*跨執行的自我改善*, 而不是一個會重寫自己 harness 的系統。這個更強的說法不在原始來源裡。Runkle 還借用了「**loopcraft**」這個詞——但把它歸功於 Swyx, 引用他那篇談「loopcraft：堆疊迴圈的藝術」的文章。這個造詞是 Swyx 的, 被 LangChain 引用, 不是 LangChain 自己的。

---

## 13.7 外層迴圈：人類保留的東西

如果 §13.1–13.6 描述的是 agent 跑的迴圈, Osmani 的後續文章描述的是人類被告知要保留的迴圈。《Own the Outer Loop》（addyo.substack.com/p/own-the-outer-loop）於 2026 年 7 月 8 日在 X 上宣布（Substack 版本掛的是 7 月 9 日的署名日期）。它的拆分是：agent 現在跑**內層執行迴圈**——調查、實作、測試／驗證、回報——而工程師握住**外層迴圈**。他的論點寫得很直白：

> 工程師擁有外層迴圈。

外層迴圈是那個不被委派出去的判斷, 用他的原話結構成三根支柱——**Quality（質量）**、**Verdict（裁決）**、**Answerability（可問責性）**。Quality 是在 agent 行動之前跑的那些檢查所形成的反壓。**Verdict** 是「工作進入我們的下游系統之前, 我們所做的最終決定」。**Answerability** 是「如果有人問起, 我能解釋為什麼的那種保證」。（他用的詞是單數的 *Verdict*, 「quality bar」不是他的原話——這根支柱就只是單純的 *Quality*。）把這些留給人類的理由是：

> Agent 可以把它寫出來。但在它到達使用者之前, 必須有人能解釋它為什麼該存在、為什麼它安全到足以成為生產環境的一部分, 以及當它出錯時他們會怎麼做。

他點名了過度委派外層迴圈的三種失效模式：**cognitive debt（認知債）**（「你解決問題的理解與記憶被侵蝕」）、**cognitive surrender（認知投降）**（「盲目接受 AI 給你的東西」）, 以及 **orchestration tax（編排稅）**（拉起比你的判斷實際能覆蓋更多的 agent 所帶來的拖累）。這些就是按下「go」卻沒有繼續當工程師所要付出的代價。

回扣到 6 月 7 日那篇文章的貫穿線, 是它結尾的指示, 讀起來正是對這件事的警告：

> 把迴圈建出來。但要用一個打算繼續當工程師的人的方式去建, 而不是只當那個按下 go 的人。

還有這句話, 削弱了任何「迴圈能自我證成」的假設：

> 兩個人可以建出一模一樣的迴圈, 卻得到完全相反的結果。

迴圈的好壞, 取決於圍繞它的外層迴圈有多好。這就是整個框架誠實的核心。

---

## 13.8 採用訊號

三個標記顯示這個框架正在擴散到它的創始者之外。每一個都只講可驗證的部分, 隨之流傳的誇大說法則被排除在外。

**廠商。** Anthropic 的官方開發者帳號 **@ClaudeDevs** 於 2026 年 7 月 6 日發布了 X 文章《Getting started with loops》（截至 7 月中大約 **6.0M 次曝光與 38K+ 收藏**）。這份材料直接教 agentic 迴圈——「你送出的每一個 prompt, 都啟動了一個由你指揮每個回合的手動迴圈。Claude 收集 context、採取行動、檢查自己的工作、需要時重複, 然後回應」——並走過以回合為基礎、以目標為基礎（`/goal`）、以時間為基礎（`/loop`、`/schedule`）的迴圈。有個編輯上的細微差別值得保留：這篇 X 文章自己的標題講的是*「loops」*, 不是*「loop engineering」*。「loop engineering」這個標籤出現在 Claude 部落格正典鏡像版本的框定裡（claude.com/blog/getting-started-with-loops）, 而不是在產品詞彙本身裡。廠商教迴圈, 是比廠商採用這個詞更弱的訊號——而且只有那個較弱的訊號被證實了。

**中國。** 魚皮 6 月 16 日的保姆級（「保姆等級」）教程, 是進入中國開發者論述的入口。它的標題——「提示詞工程已死，Loop Engineering 稱王！保姆級教程 + 項目實戰」——以「已死」開頭, 而這個噱頭是連內文自己都收回的誇大：這份教程自己的層層包含論點（§13.2）講的是 prompt 技巧被*用在*迴圈裡面, 不是被它殺死。作為一個粗略的觸及率替代指標, 他的 GitHub 帳號顯示 **23.9k 追蹤者**。（有更大的總追蹤數字流傳, 但無法對照主要來源驗證, 所以被省略。）

**記憶與評測。** 迴圈最依賴的那個子問題——在各次執行之間存活下來的跨 session 狀態——現在有了獨立的基準測試。Snorkel 的 **Continual Learning Bench**（arXiv 2606.05661；Snorkel AI / UC Berkeley SkyRL / UW-Madison）把結果拆解成 agent、記憶系統、任務三個因子。在這個基準上, 用 **Fable 作記憶骨幹的 agent 系統表現超越了建立在 Opus 或 Sonnet 上的系統**（Snorkel 的 Benchtalks 訪談；這是個定性發現——arXiv 論文的模型名單是 Opus 4.7 / Sonnet 4.6 / Gemini 3.1 Pro / Gemini 3 Flash / GPT-5.4, 沒有給 Fable 附上數字分數）。發布時, 同級最佳系統達到大約 **25% 的正規化增益**, in-context learning 領先排行榜。訊號不在那個數字；而在於*迴圈背後用什麼記憶*現在成了一個被測量的軸線。

得名五週後, loop engineering 有了一個定義、一個對 harness 的明確關係、一個大型生產案例、一份框架廠商的教材、一份中國主流教程, 以及一份廠商自己的迴圈材料。它沒有的, 是學術文獻、定型的接受度, 或是一個共識——它究竟是真正的第四世代, 還是配了排程器和狀態檔的 harness engineering。本指南把它當作正在浮現、尚未定型的東西來追蹤——而 Osmani 自己的警語, 兩個人能建出同一個迴圈卻得到相反的結果, 是最公道的一句總結。

---

## 來源

- Steinberger, Peter（@steipete）。催化「迴圈, 不是 prompt」框定的貼文（2026 年 6 月 7 日）：[https://x.com/steipete/status/2063697162748260627](https://x.com/steipete/status/2063697162748260627)——截至 2026 年 7 月中 8.4M+ 次曝光；貼文本身沒有用「loop engineering」這個詞。
- Osmani, Addy.「Loop Engineering」（2026 年 6 月 7 日）：[https://addyosmani.com/blog/loop-engineering/](https://addyosmani.com/blog/loop-engineering/)；6 月 22 日轉載於 O'Reilly Radar：[https://www.oreilly.com/radar/loop-engineering/](https://www.oreilly.com/radar/loop-engineering/)——命名文章；定義、「在 harness 之上一層樓」、五個零件、晨間分診實例。
- Osmani, Addy.「Own the Outer Loop」（7 月 8 日於 X 上宣布；Substack 署名日期 7 月 9 日）：[https://addyo.substack.com/p/own-the-outer-loop](https://addyo.substack.com/p/own-the-outer-loop)——內層對外層迴圈；Quality／Verdict／Answerability；cognitive debt、cognitive surrender、orchestration tax。
- Cherny, Boris.「Head of Claude Code: what happens next」訪談, Lenny's Podcast / Lenny's Newsletter（2026 年中）：[https://www.lennysnewsletter.com/p/head-of-claude-code-what-happens](https://www.lennysnewsletter.com/p/head-of-claude-code-what-happens)——「我已經不再親自提示 Claude 了……我的工作是寫迴圈」那句話；一句在不同媒體轉錄不一致的口述引言, 在此附上這個但書引用。
- Rajasekaran, Prithvi.「Harness design for long-running application development」, Anthropic Engineering（2026 年 3 月 24 日）：[https://www.anthropic.com/engineering/harness-design-long-running-apps](https://www.anthropic.com/engineering/harness-design-long-running-apps)——generator/evaluator（受 GAN 啟發）拆分；懷疑論式的獨立 evaluator；Playwright-MCP 行為驗證。
- Runkle, Sydney.「The Art of Loop Engineering」, LangChain 部落格（2026 年 6 月 16 日）：[https://www.langchain.com/blog/the-art-of-loop-engineering](https://www.langchain.com/blog/the-art-of-loop-engineering)——四個堆疊階梯（「Loop 1: The Agent」／「Level 2/3/4」）；「loopcraft」歸功於 Swyx。
- Kaliski, Steve. Stripe「minions」, 於 How I AI（主持人 Claire Vo, 2026 年 3 月）；Stripe 開發者部落格, Minions（Part 1 與 2）：[https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents](https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents)——每週約 1,300 個 minion PR（人類審查, 無人類寫的程式碼）；決定性 MCP 預先填充；Goose fork；devbox = EC2,「牲口, 不是寵物」（開發者部落格）。
- 程序員魚皮（liyupi）。「提示詞工程已死，Loop Engineering 稱王！保姆級教程 + 項目實戰」, codefather.cn（2026 年 6 月 16 日）：[https://www.codefather.cn/post/2066793761979092994](https://www.codefather.cn/post/2066793761979092994)——層層包含巢狀；馬與騎士隱喻；GitHub @liyupi 23.9k 追蹤者。
- Anthropic（@ClaudeDevs）。X 文章「Getting started with loops」（2026 年 7 月 6 日）：[https://x.com/ClaudeDevs/status/2074208949205881033](https://x.com/ClaudeDevs/status/2074208949205881033)；正典鏡像：[https://claude.com/blog/getting-started-with-loops](https://claude.com/blog/getting-started-with-loops)——約 6.0M 次曝光／38K+ 收藏（7 月中）；教的是「loops」,「loop engineering」標籤是部落格鏡像版本的框定。
- Claude Code 產品文件：`/loop` 與排程任務 [https://code.claude.com/docs/en/scheduled-tasks](https://code.claude.com/docs/en/scheduled-tasks)（v2.1.71；重複任務 7 天過期）；`/goal` [https://code.claude.com/docs/en/goal](https://code.claude.com/docs/en/goal)（v2.1.139+；全新模型條件檢查；prompt 式 Stop hook 包裝）；Cloud Routines [https://code.claude.com/docs/en/routines](https://code.claude.com/docs/en/routines)（Anthropic 託管基礎設施；最小一小時；每次執行全新 clone）。
- Codex 排程自動化（ChatGPT/Codex 文件）：[https://learn.chatgpt.com/docs/automations](https://learn.chatgpt.com/docs/automations)——每日／每週排程外加客製 RFC 5545 RRULE 節奏。
- Snorkel AI / UC Berkeley SkyRL / UW-Madison.「Continual Learning Bench」, arXiv 2606.05661（2026 年 6 月）：[https://arxiv.org/abs/2606.05661](https://arxiv.org/abs/2606.05661)——把 agent／記憶系統／任務拆解成因子；來自 Snorkel Benchtalks 訪談的定性 Fable 骨幹發現；發布時同級最佳約 25% 正規化增益, in-context learning 領先。

---

*上一章: [第 12 章 —— 本地模型與知識工程](12-local-models.md)*

*下一章: [第 14 章 —— Graph Engineering](14-graph-engineering.md)*
