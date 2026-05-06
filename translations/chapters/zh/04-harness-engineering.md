# 第 4 章：Harness Engineering —— 圍繞模型構建作業系統

> **一句話總結：** Harness 是 AI 模型周圍的一切——讓它真正可用的規則、工具、安全檢查、工作流程。
>
> **為什麼重要：** AI 模型像一具強大引擎。沒有底盤、方向盤、煞車, 它就沒用。Harness 是把原始 AI 變成產品的東西。

> 「Harness 中每一個元件都編碼了一個關於模型自己做不到什麼的假設, 而這些假設值得做壓力測試。」
> —— Anthropic, "Building Effective Agents", 2025

> 「模型從來都沒有長手。」
> —— Cab, 論為什麼工具使用是 harness 問題而非模型問題

Agent 不是模型。Agent 是 **模型加 harness**——圍繞的 prompt、工具、記憶、控制流、評估邏輯、編排程式碼系統, 把原始推論變成可靠行為。模型是引擎; harness 是車輛。本章檢視從業者如何設計、評估、演化那輛車。

**關於直覺的註記。** 把這件事變具體的隱喻, 對許多初學者來說是 Cab 的觀察:「模型從來沒有真的長出手。」當一個程式設計 agent 編輯檔案, 編輯檔案的不是模型——是 harness, 由模型作為文字返回的工具呼叫所觸發。我們歸給「AI」的每個能力, 實際上是圍繞模型的 harness 的能力。把 harness 拿走, 你得到一個只能產文字的模型。把模型拿走, 你得到一個沒有東西可路由的 harness。Harness engineering 是決定那條線在哪、兩半如何合作的學科。

---

## 4.1 定義 Harness

Harness 是除模型權重以外的一切。它包括:

- 系統 prompt 與指令模板
- 工具定義與執行沙盒
- 記憶系統（短期、長期、情節）
- 規劃與分解邏輯
- 控制流（迴圈、條件、重試政策）
- 評估與自我修正機制
- 安全護欄與輸出驗證
- Context 組裝管線（第 3 章）

一個赤裸的模型 API 呼叫配使用者訊息是個瑣碎 harness。一個有規劃、多步工具使用、自我評估、持續記憶的生產 agent 是複雜的。Harness engineering 的學科是在這個光譜上做有原則的決策。

## 4.2 Böckeler 分類

Birgitta Böckeler（ThoughtWorks, 2026 年 4 月）在 Martin Fowler 的 *Exploring Generative AI* 系列中, 提出了一個二軸 harness 元件分類, 已成為標準參考:

**軸 1：方向**
- **Guides（前饋）：** 在模型行動*之前*塑造行為的元件。系統 prompt、few-shot 例子、工具 schema、規劃模板。它們設定軌道。
- **Sensors（回饋）：** 在模型行動*之後*評估行為並把結果回饋的元件。輸出驗證器、測試執行器、人工審查、自我評估 prompt。它們修正路線。

**軸 2：機制**
- **計算控制：** 確定性程式碼——regex 驗證器、型別檢查器、schema 強制、許可權檢查。這些是從不幻覺的硬約束。
- **推論控制：** 用來評判、路由、精煉的另一次 LLM 呼叫。評估模型、分類器、總結器。這些是軟約束, 用精度換取靈活性。

這個分類揭示一個設計空間。大多數生產 harness 都用四個象限:

|  | 前饋（Guides） | 回饋（Sensors） |
|--|---------------|----------------|
| **計算** | 工具輸入的 schema 驗證、許可權白名單 | 輸出格式檢查、測試套件執行 |
| **推論** | 規劃 prompt、few-shot 路由 | 自我評估、LLM-as-judge、批評鏈 |

洞察是: 計算控制更便宜、更可靠但較不靈活, 而推論控制處理模糊但引入自己的失效模式。好的 harness 設計儘可能用計算控制, 把推論控制保留給真正模糊的決策。

## 4.3 OpenAI Codex：透過 Harness 規模化

社群廣為引用的一個資料點描述 OpenAI 內部使用 Codex 的情況: **三位工程師加上 Codex agent 系統產出約 100 萬行程式碼、約 1,500 個 PR**。生產力倍數主要不是關於模型質量——是關於 harness 設計。（具體數字在 2025-2026 年 OpenAI 演講與文章中流傳; 關於 Codex harness 的公開材料, 見 [openai.com/index/introducing-codex](https://openai.com/index/introducing-codex)。）

Codex harness 包括:
- 自動化 PR 分解（把大任務拆成可審查單元）
- 每個任務的沙盒執行環境
- 自動化測試生成與驗證
- PR 邊界的人工審查整合
- 關於 repo 結構與慣例的持續 context

教訓: 在足夠的 harness 成熟度下, 模型變成更大生產系統中的一個元件, 而非獨立工具。Harness 處理編排、質量控制、整合——這些是 prompt engineering 怎麼調都解決不了的關切。

## 4.4 IMPACT 框架

在 2020 年代中期從業者討論中, **IMPACT 助記詞**——Intent、Memory、Planning、Authority、Control flow、Tools——浮現為系統化思考 harness 設計維度的方式:

- **Intent（意圖）：** 系統如何理解使用者實際想要什麼？包括意圖分類、澄清對話、目標分解。
- **Memory（記憶）：** 系統跨回合與 session 記得什麼？包括對話緩衝、向量庫、結構化知識庫、使用者偏好系統。
- **Planning（規劃）：** 系統如何把複雜任務分解成步驟？包括思維鏈 prompting、明確計畫生成、動作空間的樹搜尋。
- **Authority（許可權）：** 系統被允許做什麼？包括許可權系統、人在迴路 gate、能力邊界。
- **Control Flow（控制流）：** 執行如何進行？包括順序鏈、並行扇出、條件分支、含退出條件的迴圈、重試政策。
- **Tools（工具）：** 系統能存取什麼外部能力？包括函式定義、API 整合、程式碼執行環境、瀏覽器存取。

IMPACT 作為設計清單有用。建構或審查 harness 時, 走過每個維度能浮現差距。一個工具強但許可權弱的系統有安全問題。一個規劃強但無記憶的系統不能從錯誤學習。這個框架讓這些不平衡可見。

## 4.5 Meta-Harness 論文：自動化 harness 設計

Stanford、MIT、KRAFTON 聯合論文（2026 年 3 月）引入 **meta-harness** 概念——一個自動最佳化 harness 配置的系統。

他們的關鍵發現: 在同一基準、同一基礎模型上, 不同 harness 配置產出 **6 倍效能差距**。給定任務的最佳 harness 配置很少明顯, 常常違反直覺。手動 harness 調整正在桌上留下大量效能。

Meta-harness 做法把 harness 引數（重試次數、規劃深度、工具選擇策略、記憶視窗大小、評估嚴格度）視為搜尋空間, 用自動最佳化找出高效能配置。系統能把 harness 適配到不同任務型別、不同模型、不同成本約束。

這個結果有深刻含義: **harness engineering 不是已知最佳實務的已解決設計問題——它是有大且不太理解搜尋空間的最佳化問題**。把 harness 設計視為一次性架構決策的團隊, 很可能在遠低於前沿的狀態執行。

Meta-Harness 論文現在是快速移動一線上的一個資料點。2026 年 4 月, **AHE 論文**（「Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses」, arXiv 2604.25850, 復旦/北大/上海齊跡智鋒）把這個問題從搜尋重構為*可觀測性*: 不是把 harness 配置當搜尋空間然後跑最佳化器, AHE 裝備三個可觀測性支柱——元件（明確、可還原的動作空間）、經驗（濃縮的軌跡證據）、決策（執行前做的可證偽編輯預測）——讓 harness 透過讀自己的 runtime 訊號自我演化。經過 10 次 AHE 迭代, Codex-CLI 風格的基線在 Terminal-Bench 2 上 69.7% pass@1 達到 77.0%, 超越人類設計基線（71.9%）, 在轉移到沒被最佳化過的模型家族時顯示 **+5.1 到 +10.1 個百分點的跨家族增益**。跨家族轉移是結構性新聞: 演化的 harness 不只是過擬合到一個模型的怪癖, 它在底下基底換代時仍能延續。Meta-Harness 發現（「harness engineering 是有大搜尋空間的最佳化問題」）與 AHE 發現（「……而搜尋能跑成連續可觀測性迴路, 不是單次最佳化」）一起描述一個快速遠離手動調整的工程實務。

### 從研究到生產：Advisor Tool（2026 年 4 月）

Meta-harness 發現是研究結果。一個月後, Anthropic 出貨首個產品化的 meta-harness pattern: **Advisor Tool**（beta, `advisor-tool-2026-03-01`）。該 pattern 把更快的 executor 模型與更有能力的 advisor 模型配對。Executor 處理大部分工作; 當它撞到決策點, 它呼叫 `advisor()` 並收到一個策略計畫或路線修正（典型 400-700 文字 token, 含思考 1,400-1,800）, 而不離開當前 API 請求。

Anthropic 推薦的預設配置很說明:

| Executor | Advisor | 目標用途 |
|----------|---------|----------|
| Haiku 4.5 | Opus 4.6 | 從只用 Haiku 提升智慧 |
| Sonnet 4.6 | Opus 4.6 | 用 Sonnet 成本達到 Opus 單獨的質量 |
| Opus 4.6 | Opus 4.6 | 最難任務的質量精煉 |

這是 6 倍 meta-harness 差距被翻譯成定價策略。不是為每個 token 付 Opus 價格, 你為執行付 Sonnet 價格、為真正塑造輸出的 1-2 次 advisor 呼叫付 Opus 價格。Anthropic 建議的 prompting pattern 值得引用, 因為它把 harness 時機編纂成規則:

> 「在實質工作*之前*呼叫 advisor——在寫之前、在承諾解讀之前、在基於假設建構之前。[...] 在長於幾步的任務上, 至少在承諾做法之前呼叫一次 advisor, 並在宣告完成之前呼叫一次。」

文件中幾個細節對從業者重要:

- **服務端子推論。** Advisor 在同一個 `/v1/messages` 請求內執行。Executor 發出 `server_tool_use` 塊, Anthropic 用完整 transcript 跑獨立推論 pass, 結果作為 `advisor_tool_result` 回來。你的程式碼不需額外 round trip。
- **快取約 3 次呼叫打平。** 在 advisor 工具上啟用 `caching` 把 advisor 的 transcript 寫入 5 分鐘或 1 小時快取。第一次呼叫花費額外; 收益從約第三次呼叫開始。短任務應關 caching。
- **簡潔 prompt 減少輸出 35-45%。** 單一指令——「Advisor 應在 100 字內回應, 用列舉步驟而非解釋」——可衡量地減少 advisor 的最大成本驅動, 而不改變呼叫頻率。
- **明確協調協議。** 當 advisor 建議與 executor 已經收集的實證證據衝突, Anthropic 的系統 prompt 告訴 executor 再做一次 advisor 呼叫, 框為「我發現 X, 你建議 Y, 哪個約束破解平局？」, 而非沉默切換。這是對「該信任規劃者還是資料」問題的生產級答覆——這個問題在多個角色不同意時都會出現。

Advisor Tool 在直接效用之外重要。它是 meta-harness 思維已從研究好奇心移到商業 primitive 的訊號。「同模型、不同 harness、6 倍差距」發現不再需要研究團隊來利用——Anthropic 把它暴露為工具呼叫。預期其他實驗室跟進推出他們自己的 advisor/executor 配對, 預期 harness engineering 職位描述開始把多模型協調列為核心技能。

## 4.6 Anthropic 的三 Agent 架構

一個反覆出現的三角色 pattern, 常被從業者社群總結為 **Planner / Generator / Evaluator**, 整個 2025 年成為多 agent harness 的常見框架。這個框架最好讀為對 Anthropic 的 [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents) 中描述的 pattern（orchestrator-worker、evaluator-optimizer）的教學綜合, 而非 Anthropic 自己在主要寫作中採用的標籤。2026 年 3 月 31 日 Claude Code 原始碼外洩（本節稍後涵蓋）確認了這個區別: 在生產中, Anthropic 實際 harness 是圍繞分層自愈記憶組織, 而非字面的三角色分解。這些角色仍描述一個有用分類, 所以本節用它們討論關切分離:

- **Planner：** 把任務分解成子任務, 維持整體計畫, 決定何時修訂。
- **Generator：** 執行個別子任務——寫程式碼、起草文字、呼叫工具。
- **Evaluator：** 對照任務要求評估 Generator 輸出, 提供結構化回饋。

這種關切分離被廣泛用於處理本章標記為 **context anxiety** 與 **self-evaluation bias** 的兩個失效模式（這些標籤是本指南用的框架; 底層觀察出現在受 Anthropic 已發表 agent 研究啟發的 pattern 中）:

**Context Anxiety（上下文焦慮）。** 當單一 agent 處理規劃、執行、評估, 它傾向規避。它給輸出加資格、加不必要的注意事項、把 token 花在元評論而非任務執行上。分離角色讓每個 agent 專注, 不必扛其他角色的認知負載。

**Self-Evaluation Bias（自我評估偏差）。** 模型系統性地不擅長評估自己的輸出。它們表現出有據可查的寬容偏差——給自己的工作打的分比獨立評判者會打的高。三 agent 架構透過用獨立的評估器（可能是不同模型或不同 prompt 的例項）來緩解, 評估器對生成輸出沒有投資。

從業者社群強調的一個微妙之處, 與 Anthropic 的 evaluator-optimizer 指引中觀察到的 pattern 一致: **評估器校準本身是個 harness engineering 問題**。過嚴的評估器導致無限修訂迴圈。過寬的讓低質量工作透過。評估器的閾值與標準需要和 generator 的指令一樣仔細調整。

### Claude Code 外洩：實證觀察（2026 年 3 月 31 日）

整個 2025 年大部分時間, 三 agent 架構是透過 Anthropic 已發表研究知道的、從行為推論的。2026 年 **3 月 31 日**, 這變了。Anthropic 不慎在 npm 包 **`@anthropic-ai/claude-code` v2.1.88** 內釋出一份 59.8MB source map, 暴露約 **513,000 行未混淆 TypeScript 跨 1,906 檔**。Anthropic 把事件描述為「人為打包錯誤, 不是安全外洩」, 但從業者首次能直接讀到一個前沿實驗室的生產 harness。

外洩中重塑社群對架構描述的幾個發現:

- **它字面上不是「Planner / Generator / Evaluator」。** 早期社群文章把 Claude Code 對映到 4.6 三角色框架, 結果是對研究的誤讀。實際架構組織為**三層「自愈記憶」**系統。這些層對應到 scratchpad / 工作狀態、壓縮中期狀態、持久專案記憶——層之間有明確的修復與協調邏輯。
- **`MEMORY.md` 是索引, 不是倉庫。** 不是單一記憶檔, `MEMORY.md` 擔任**輕量級指標索引**, 指向更詳細筆記。這更接近檔案系統目錄而非 transcript, 這是讓記憶層在不膨脹 context 下擴充套件的原因。
- **`KAIROS` 是自主 daemon 模式。** 名為 `KAIROS` 的 feature flag 在原始碼中被引用 **超過 150 次**。它把守一個自主 daemon 模式——一個無人看管、長時間執行的迴圈, 遠超大多數使用者知道的互動 REPL。
- **44 個隱藏 feature flag。** 除了 `KAIROS`, 原始碼含 44 個未釋出功能的 feature flag, 顯示公開發布的是 harness 內部支援的保守子集。

實務結論: Planner / Generator / Evaluator 拆分仍是有用的概念分類（Anthropic 研究論文仍以這些術語描述系統）, 但生產中架構是圍繞**記憶與修復**分層, 而非僅圍繞角色分解。2026 年的 harness engineering 越來越意味著設計記憶層與層之間的轉換。

外洩兩週後, 同一架構再走一步——這次向外, 離開使用者機器。透過 **Claude Code Routines**（2026 年 4 月 14 日）, Anthropic 把編排器席位本身從筆電移到自己的雲端, 把排程、API、GitHub 事件觸發器暴露為一等 harness primitive。讀在外洩旁邊, 這是一個清楚的架構修辭: 編排器不再被建模為使用者照顧的 REPL, 而是住在 Anthropic 基底上的 daemon。三層自愈記憶跨觸發器持續; harness 不再需要使用者的程式活著才能讓迴圈進展。無論你採納 Routines 與否, 這個框架現在在空氣裡: 編排器席位是產品表面, 「迴圈在哪執行」是設計決策而非預設。

## 4.7 Harness 即護城河

2026 年初, Meta 以約 20 億美元收購 Manus。Manus 沒有專有模型。它的全部價值在 harness——把商品級模型 API 變成可靠 agent 產品的編排邏輯、context engineering 管線、工具整合層、運營基礎設施。

這場收購把行業一直在發現的事結晶化: **harness 是護城河**。模型越來越商品化。差異化在於你怎麼包它——你提供什麼工具、你怎麼管 context、你怎麼處理失敗、你怎麼編排多步工作流、你怎麼評估質量。

對從業者的含義是: harness engineering 不是通往模型開發「真正工作」途中要應付的管線工事。對大多數生產 AI 團隊它*就是*真正工作。到 2026 年 4 月,「harness engineering」作為正式學科已進入行業詞彙, Claude Code 外洩提供了對生產 harness 實際包含什麼的首次實證觀察。

## 4.8 Harness 維護：壓力測試的命令

Anthropic 最可行動的洞察可能是最簡單的: 每個 harness 元件編碼一個關於模型侷限的假設, 而**這些假設會過期**。

當一個 harness 圍繞 GPT-4 級能力建構, 它可能包括:
- 明確思維鏈 prompting（因為模型需要它）
- 激進的輸出解析（因為模型在格式上不一致）
- 多步驗證（因為單 pass 準確度不足）
- 詳細 few-shot 例子（因為零樣本表現差）

隨著新模型帶來改善的推理、指令遵循、輸出一致性, 這些元件變成**可能不再需要承重的承重牆**。它們加 latency、成本、複雜度而不貢獻質量。

學科是週期性壓力測試: 系統性地停用 harness 元件, 決定哪些仍必要。如果移除規劃步驟不退化效能, 移除它。如果模型現在不需 few-shot 例子也能可靠遵循格式, 丟掉它們。如果自我評估加成本但不加質量, 消除它。

這違反直覺。工程師天然加安全機制並抗拒移除它們。但在 harness engineering, 不必要元件不是免費的——它們消耗 context window 空間、加 latency、增加成本、創造維護負擔。一個匹配當前模型能力的精簡 harness, 跑贏一個為更弱模型過度工程的。

實務建議: 當上線新模型, 先跑你現有的 harness, 然後系統性剝離元件同時衡量任務效能。剩下的就是你真正的 harness。你移除的是先前能力時代的技術債。

成熟 harness 最終把壓力測試問題反轉: 不是問「我能移除哪些元件」, 而是「我應該在哪些元件上多花運算, 何時多花」。2026 年 4 月 **CATTS** 預印本（Consensus-Aware Test-Time Scaling, arXiv 2602.12276）給那個問題一個可用答案。CATTS 每個 agent 步驟取樣小型 rollout 委員會, 用它們之間的分歧作為每步不確定性分數; 該分數被用來不均勻分配測試時運算——委員會分歧時更多 rollout, 收斂時更少。在 WebArena-Lite 與 GoBrowse 上, 該技術報告在 **2.3 倍少 token** 下 **+9.1%** 任務準確度。對成熟 harness, CATTS 與 Advisor Tool 並排: advisor pattern 決定*想什麼*, CATTS 決定*想多深*。兩者都用 runtime 計算的衡量不確定性訊號, 取代假設（「永遠重試三次」、「永遠在難問題上用 Opus」）。

2026 年 4 月 AHE 結果（第 4.5 節）在結構上做出同樣論點: 壓力測試不是一次性審查活動, 而是連續可觀測性迴路。手動壓力測試作為從業者今天能跑的學科仍有價值; AHE 顯示它也是可自動化的。

## 4.9 雲原生 Harness Primitive

整個 2025 與 2026 年第一季, harness 幾乎都是你自己建、自己跑的東西。即使最複雜的 pattern——三 agent 架構、Advisor Tool、KAIROS 風格自主迴圈——也都假設你的程式碼握有編排器席位。你寫 cron 工作、跑 daemon、保持筆電喚醒、擁有失效模式。基底是通用運算（Mac mini、VPS、Kubernetes pod）, harness 層從程式監督員往上是你的責任。

**2026 年 4 月 14 日**, Anthropic 的 **Claude Code Routines** 研究 preview 朝改變這件事跨出第一具體步。一個 Routine 是在 Anthropic 雲端而非使用者機器上執行的 Claude Code 工作流, 由三種觸發器之一觸發: **排程**（cron 等價）、**API 呼叫**（來自其他服務的程式化呼叫）、**GitHub 事件**（push、PR、issue、comment）。這些觸發器是 harness 工程師過去 18 個月寫的檔案式排程 pattern 的刻意泛化: 一樣的「每週日 09:00 HKT 跑」語意, 但被表達為託管 primitive 而非 `cron + tmux + claude` shell 咒語。配額與底層 Claude Code 訂閱分層——**Pro 5/天、Max 15/天、Team/Enterprise 25/天**——把基底定價為「每席每天少數有意義的迴圈」, 而非「按小時的原始運算」。

雲端執行細節比聽起來重要。自架檔案式排程器把編排器席位握在使用者擁有的硬體上; 如果 Mac 關、睡、沒電, 迴圈不跑。Routine 不論使用者機器狀態都完成。這溶解了一整類失效模式（筆電蓋、網路掉、OS 更新、意外重啟）和對應一類補償機制（wake-on-LAN 把戲、Mac Mini「永遠開」伺服器、冗餘執行器）。對真正事件驅動的工作流——「PR 開時, 做 X」——託管 primitive 直截了當比自架輪詢器更適合。

取捨是新的天花板。託管 primitive 按觸發器與配額定價, 不按工作負載的物理。它假設你的迴圈符合排程 / API / GitHub 事件形狀、每天配額夠、Anthropic 基底是你程式碼與資料該住的地方。對相當數量的 harness 工作負載, 那些假設都不乾淨成立。**瀏覽器自動化** 已認證 session 仍受益於執行在已經有使用者 cookie、profile、信任狀態的機器上。**高頻編排**——亞分鐘輪詢、即時市場或感測器資料、每天 25 次呼叫是侮辱的任何東西——需要按秒計費的 runtime, 不是按觸發器。**非 GitHub 事件來源**（Discord 訊息、內部 webhook、客制 MCP 伺服器、裝置上檔案系統事件）在 Routines 中沒有一等觸發器; 暴露它們需要自己寫 bridge, 這把你放回自架機器跑 bridge。任何依賴本機檔案、本機模型推論、本機網路存取的, 在結構上都仍在雲外。

對 2026 年 harness 工程師的誠實框架: 像 Routines 這樣的雲原生 primitive 是 harness 工作負載裡 **GitHub 事件觸發、排程、API 呼叫** 那一象限的對答, 它們很可能在接下來 12 個月戲劇性壓縮那個象限的運營成本。自架 harness 不會消失——它正被收窄到它實際付清自己的地方。要發展的學科是本章一直在建構的同一學科: 知道每個元件編碼什麼假設, 注意到下面基底何時改變。

**Routines 與 Managed Agents。** 值得精確說明 Anthropic 在 2026 年 4 月實際出貨什麼, 因為這兩塊有時被混淆。**Claude Managed Agents**（公測, 2026 年 4 月 8 日）是*基底*: 一個把 session（一切發生過事情的 append-only 事件 log）、harness（呼叫 Claude 與路由工具呼叫的迴圈）、sandbox（Claude 可執行程式碼的環境）暴露為三個虛擬化元件的託管 runtime, 配 tracing 與 Agent / Environment / Session / Events API 表面疊加在上。SiliconANGLE 的釋出報道指出基底定價是標準 token 費率加上**每 agent runtime 小時 8 美分**; 該數字來自次級科技媒體, 不是 Anthropic 主要文件。即便在次級引用 bar, 定價結構重要: 這是首個把編排器席位本身與推論分開計費的前沿供應商 primitive。**Claude Code Routines**（研究 preview, 2026 年 4 月 14 日）是*觸發表面*, 跑在該基底（或相容替代）之上: 排程、API 呼叫、GitHub 事件, 配 Pro / Max / Team-Enterprise 層級每天 5 / 15 / 25 次呼叫配額。兩者回答不同問題。Managed Agents 答「agent 迴圈物理上在哪執行, 它的狀態如何在回合之間持久維持？」Routines 答「什麼讓迴圈開始？」一個採納 Routines 但不採納 Managed Agents 的自架 harness, 仍擁有它的狀態與執行環境; 一個採納 Managed Agents 但建自己觸發層的, 仍擁有工作何時開始。實務上, 2026 年中大多數雲原生 harness 設計都會兩者都採——但解綁是架構重點。Anthropic 不再把「harness」當一件事賣; 它在賣它的組成 primitive。

解綁在 2026 年 4 月底兩個結構性重要的動作中繼續。第一, **4 月 23 日**, Anthropic 把 **Memory for Managed Agents** 加到公測: 一個檔案系統掛載、稽核日誌的儲存, 給 agent 耐久跨 session 狀態, 配併發存取語意、範圍企業許可權、Claude Console 的 rollback / redaction 表面。基底現在出貨第三個 primitive——*耐久記憶*——與 sessions 和 sandboxes 並列; 3 月 31 日 Claude Code 原始碼外洩揭示的生產架構（三層自愈記憶）現在是其他團隊能租用的供應商管理 primitive。第二, **4 月 28 日**, AWS 與 OpenAI 出貨 **Amazon Bedrock Managed Agents powered by OpenAI** 在 limited preview, 首次命名並販售「OpenAI agent harness」作為獨立產品表面。讀在一起, 這兩件事把 Managed Agents pattern 從「Anthropic 4 月 8 日的賭注」轉移到 **跨供應商基底形狀**——三個前沿供應商中兩個現在把編排器席位作為託管 primitive 出貨, 配每 agent 身分、動作日誌、內建耐久狀態。對 2026 年中在編排器席位上比較 build vs. buy 的 harness 工程師, 選項集不再單一供應商, 基底不再是薄 runtime: 它含記憶。

## 4.10 託管推論轉變（2026 年 4 月）

整個 2025 年, 呼叫者與模型之間的 harness 合約大致是個旋鈕面板: `temperature`、`top_p`、`top_k`、`max_tokens`、`budget_tokens`、系統 prompt。從業者按案轉旋鈕, 有時在同一 agentic 迴圈內每步都轉。2026 年 4 月 16 日 **Claude Opus 4.7** 的釋出打破那個 pattern。在單一發布中, 三項變更朝同一方向拉:

1. **`temperature`、`top_p`、`top_k` 被棄用。** 任何非預設值返回 400 錯誤。取樣級控制不再在呼叫者手上。
2. **自適應思考是唯一的思考開模式。** 手動 `budget_tokens`（extended thinking）被移除; `effort`（`low`、`high`、`xhigh`、`max`）取代它。
3. **Task budgets 變成一等 primitive。** 一個新 beta 標頭（`anthropic-beta: task-budgets-2026-03-13`）讓呼叫者為*整個 agentic 迴圈*——思考、工具呼叫、工具結果、最終輸出——宣告建議性 token 預算。模型在工作時看到倒數。

前兩項變更是減法: 旋鈕被移除。第三項是加法: 一個先前在任何前沿 API 都不存在的 primitive。一起它們描述合約變更。不是「你調取樣器, 模型產生回應」, 合約現在是「你宣告運算預算, 模型對它自我分配, 一步一步決定任務還值多少搜尋、推理、綜合」。Harness 變成預算對話而非引數面板。

「建議而非強制」細節重要。Task budgets 不是硬上限（`max_tokens` 仍擔任那個角色, 仍只面向呼叫者）。相反, 模型被告知它的預算並用它來排序優先。實務上, 設太緊的預算產生拒答式輸出而非退化的——模型偏好拒絕而非出貨它判定為資金不足的結果。最低 20K token 被強制, 正是為防止重大任務的那個失效模式。

對 harness 設計者, 含義具體: 任何在 Opus 4.6 跑的 harness 需要為 4.7 重新基線, 不只在 prompt 層級, 也在 timeout、retry、壓縮、工具呼叫預算層級。Anthropic 自家遷移文件直接說: *重新基線 harness, 不只是 prompt*。Advisor Tool（第 4.5 節）與 task budgets（本節）描述任何長時間 harness 的新兩軸最佳化: Advisor 決定*想什麼*; task budgets 決定*每一步想多深*。兩者都用 runtime 計算的衡量訊號取代旋鈕調整。

這是更廣 pattern: **託管推論轉變**。前沿供應商越來越把推論本身視為產品表面而非參數列面。Harness 層正從「你配置推論呼叫」移到「你描述工作, 推論層適配」。其他實驗室是否跟隨 Anthropic 的具體決策（取樣旋鈕棄用、建議性預算）還是隻跟方向, 是開放問題。方向本身看起來已成定局。

---

## 來源

- **Böckeler, Birgitta.** "Harness engineering for coding agent users." martinfowler.com（Exploring Generative AI 系列）, 2026 年 4 月 2 日。[https://martinfowler.com/articles/harness-engineering.html](https://martinfowler.com/articles/harness-engineering.html) ——Guides vs. Sensors、Computational vs. Inferential 分類。
- **OpenAI.** Codex 公開材料: [https://openai.com/index/introducing-codex](https://openai.com/index/introducing-codex)。OpenAI Codex 的 harness 設計框架錨點; 廣為引用的「三位工程師 / 約 100 萬行 / 約 1,500 個 PR」數字在 2025-2026 年 OpenAI 演講與文章中流傳, 在此引用為社群引用而非來自單一標準帖。
- **IMPACT 助記詞。** Intent / Memory / Planning / Authority / Control flow / Tools——一個六維 harness 設計清單, 在 2020 年代中期從業者討論中浮現。在本章作為教學框架使用; 不歸屬任何特定原始來源。
- **Stanford / MIT / KRAFTON.** "Meta-Harness: Automated Optimization of LLM Agent Harnesses." arXiv 預印本, 2026 年 3 月。6 倍效能差距發現, 自動化 harness 調整。
- **Lin et al.** "Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses." arXiv 2604.25850, 2026 年 4 月 28 日。[https://arxiv.org/abs/2604.25850](https://arxiv.org/abs/2604.25850) ——復旦/北大/上海齊跡智鋒。Meta-harness 搜尋問題的可觀測性支柱重構; 在 Terminal-Bench 2 上 69.7% → 77.0%, 配跨家族轉移。
- **Anthropic.** "Claude Managed Agents overview." API 文件, 2026 年 4 月 8 日。[https://platform.claude.com/docs/en/managed-agents/overview](https://platform.claude.com/docs/en/managed-agents/overview)
- **Anthropic Engineering.** "Scaling Managed Agents: Decoupling the brain from the body." 2026 年 4 月 8 日。[https://www.anthropic.com/engineering/managed-agents](https://www.anthropic.com/engineering/managed-agents) ——三個虛擬化元件（session、harness、sandbox）; 定價細節（標準 token 費率加上每 agent runtime 小時 8 美分, 按 SiliconANGLE 釋出報道）不在 Anthropic 主要文件中, 由次級科技媒體引用。
- **Anthropic.** "Memory for Claude Managed Agents"（2026 年 4 月 23 日）。[https://claude.com/blog/claude-managed-agents-memory](https://claude.com/blog/claude-managed-agents-memory) ——檔案系統掛載記憶、跨 session 學習、稽核日誌、範圍企業許可權; 與 3 月 31 日 Claude Code 原始碼外洩關於三層自愈記憶的發現關閉迴路。
- **AWS 與 OpenAI.** "Bedrock Managed Agents powered by OpenAI"（2026 年 4 月 28 日, limited preview）。AWS 公告: [https://aws.amazon.com/about-aws/whats-new/2026/04/bedrock-openai-models-codex-managed-agents/](https://aws.amazon.com/about-aws/whats-new/2026/04/bedrock-openai-models-codex-managed-agents/)。About Amazon: [https://www.aboutamazon.com/news/aws/bedrock-openai-models](https://www.aboutamazon.com/news/aws/bedrock-openai-models)。OpenAI 公告: [https://openai.com/index/openai-on-aws/](https://openai.com/index/openai-on-aws/) ——首次「OpenAI agent harness」被命名並作為獨立產品表面販售; Managed Agents pattern 上的跨供應商收斂。
- **Anthropic.** "Building Effective Agents." Anthropic 工程部落格, 2024 年 12 月 19 日。[https://www.anthropic.com/engineering/building-effective-agents](https://www.anthropic.com/engineering/building-effective-agents) ——描述 orchestrator-worker pattern 與 evaluator-optimizer workflow; 本指南把相關失效模式標為「context anxiety」與「self-evaluation bias」作教學使用。從業者社群把它總結為 Planner / Generator / Evaluator triple 的框架, 是建立在這些 pattern 上; Anthropic 自己在主要寫作中沒用那個明確 triple。實際 Claude Code 架構, 由 2026 年 3 月 31 日原始碼外洩揭示（第 4.6 節）, 是圍繞分層自愈記憶組織而非角色分解。
- **Meta / Manus 收購。** 多份報道, 2026 年初。約 20 億美元收購驗證 harness 即護城河論點。
- **Karpathy, Andrej.** "From Vibe Coding to Agentic Engineering" —— Sequoia AI Ascent 2026 fireside chat（約 2026 年 4 月底錄製, 主要 YouTube 影片 [https://www.youtube.com/watch?v=96jN2OCOfLs](https://www.youtube.com/watch?v=96jN2OCOfLs); 作者總結在 [https://karpathy.bearblog.dev/sequoia-ascent-2026/](https://karpathy.bearblog.dev/sequoia-ascent-2026/)）。把 vibe coding 框為*提升地板*模式（人人能建）, agentic engineering 為*抬升天花板*學科（規格、計畫督導、diff 檢查、eval 迴路、許可權範圍、worktree 隔離）。錨定 2025 年 12 月一個拐點, Karpathy 在那時把自己的程式設計比例從約 80% 手寫翻轉到約 80% 委派。早期 2025「Software 3.0」/「Software Is Changing (Again)」演講在 AI Engineer World's Fair 與 YC AI Startup School, 建立模型作為新一類可程式化元件的更廣框架。
- **LangChain.** "Agent Architecture Patterns." LangChain 文件, 2025。控制流與工具編排的實務 pattern。
- **Harrison Chase.** "Agent Engineer" 框架, 2025——LangChain 部落格與 X 貼。這個詞以 harness 為中心工程的角色定義框架進入從業者詞彙; 在此作為 2025 年代討論中的 pattern 引用, 而非單一標準帖。
- **"CATTS: Consensus-Aware Test-Time Scaling for Agents."** arXiv 2602.12276（2026 年 4 月釋出週期）。投票推導不確定性作為測試時運算分配器; 在 WebArena-Lite 與 GoBrowse 上 +9.1% / 比均勻擴充套件少 2.3 倍 token。[https://arxiv.org/abs/2602.12276](https://arxiv.org/abs/2602.12276)
- **Anthropic.** "Introducing Routines in Claude Code." Anthropic 部落格, 2026 年 4 月 14 日。[https://claude.com/blog/introducing-routines-in-claude-code](https://claude.com/blog/introducing-routines-in-claude-code)
- **Anthropic.** "Claude Code Routines documentation." [https://code.claude.com/docs/en/routines](https://code.claude.com/docs/en/routines) ——觸發器（排程 / API / GitHub 事件）、配額（Pro 5/天、Max 15/天、Team/Enterprise 25/天）、雲端執行語意。
- **Anthropic.** "Introducing Claude Opus 4.7"（2026 年 4 月 16 日）。[https://www.anthropic.com/news/claude-opus-4-7](https://www.anthropic.com/news/claude-opus-4-7)
- **Anthropic.** "What's new in Claude Opus 4.7"（API 文件）。[https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-7](https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-7) ——task budgets（`anthropic-beta: task-budgets-2026-03-13`, 建議性, 最低 20K）、自適應專用思考、移除 `temperature` / `top_p` / `top_k`。
- **Caylent.** "Claude Opus 4.7 Deep Dive: Capabilities, Migration, and the New Economics of Long-Running Agents"（2026 年 4 月）。[https://caylent.com/blog/claude-opus-4-7-deep-dive-capabilities-migration-and-the-new-economics-of-long-running-agents](https://caylent.com/blog/claude-opus-4-7-deep-dive-capabilities-migration-and-the-new-economics-of-long-running-agents) ——「重新基線 harness, 不只是 prompt」。
- **Archon GitHub Repository.** [https://github.com/coleam00/Archon](https://github.com/coleam00/Archon) ——TypeScript / Bun harness 構建器, YAML DAG 工作流包 Claude Code 與 OpenAI Codex CLI; v2.1 在 2026 年 4 月釋出。
- **OpenHarness GitHub Repository.** [https://github.com/HKUDS/OpenHarness](https://github.com/HKUDS/OpenHarness) ——香港科技大學資料實驗室的 Python 參考實現; 首次 commit 2026 年 4 月 1 日。

### 給入門者的延伸閱讀

- **Cab.** 「A Layer-by-Layer Walk Through Harness Engineering.」繁體中文文章, 2026。從單一 `POST /v1/messages` 呼叫一路建到 prompt engineering、function calling、agent loop, 最後到完整 harness 複雜度。值得注意的是「模型從來都沒有長手」的隱喻, 把工具使用重構為 harness 問題而非模型能力, 還有它對 Claude Code 的 harness 實際在背後做什麼的明確走讀。推薦作為讀本章理論優先框架（Böckeler 分類、IMPACT、Meta-Harness）之前的溫和入門。
- **Anthropic.** ["Building Effective Agents"](https://www.anthropic.com/research/building-effective-agents) ——給來自非研究背景讀者的標準短篇介紹。與上面的 Cab 文章配對得好: Cab 給建構, Anthropic 給具體 pattern。

---

*上一章: [第 3 章 —— Context Engineering](03-context-engineering.md)*

*下一章: [第 5 章 —— Skill Systems 與 Skill Graphs](05-skill-systems.md)*
