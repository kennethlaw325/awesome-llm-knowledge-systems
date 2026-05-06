# 第 6 章：Agent Memory —— 缺失的層

> **一句話總結：** 記憶系統讓 AI agent 跨對話記住事情——你的偏好、過去決策、專案 context。
>
> **為什麼重要：** 沒有記憶, 每次 AI 對話都從零開始。記憶讓 AI 感覺像同事而非陌生人。

## 為什麼記憶重要

每次你與 LLM 開新對話, 你從零開始。模型沒有你之前互動的回憶, 沒有你的偏好, 沒有你花數小時對話辛苦建立的 context。這不是小麻煩——這是侵蝕 AI 作為持續協作者承諾的根本架構差距。

記憶把 AI agent 從無狀態回應者轉化為會學、適應、隨時間累積理解的系統。沒有記憶, 一個 AI 助手不能記得你偏好簡潔答覆、你的專案用 TypeScript 配特定 ORM、或上週二你在認證流程中識別到關鍵 bug。每個 session 變成冷啟動。每次互動都需要從頭重建 context。

這個差距的成本不只使用者挫折。它顯化為浪費 token（重新解釋 context）、退化輸出質量（錯過個人化）、斷裂工作流程（在多 session 任務上失去連續性）。當 AI agent 從聊天玩具移到生產基礎設施, 記憶已成為原始模型能力與真實有用之間的關鍵缺失層。

## 記憶分類

agent 記憶研究已收斂到一個受人類認知科學啟發的分類, 區分四種基本型別:

**情節記憶（Episodic Memory）** 儲存基於經驗的紀錄——特定互動、事件與其結果。當 agent 記得「上週, 使用者要我重構付款模組, 偏好提取服務類而非用 mixin」, 那是情節記憶。它為個人化與從過去成敗學習提供經驗基礎。

**語意記憶（Semantic Memory）** 裝事實知識與結構化資訊——使用者的技術堆疊、團隊成員的角色、專案架構決策、API schema。與情節記憶不同, 語意記憶從特定事件抽象出來。它代表蒸餾的理解, 非原始經驗。

**程式記憶（Procedural Memory）** 編碼 how-to 知識——工作流程、標準操作程式、學到的動作序列。當 agent 知道部署這個特定專案需要跑測試、構建 Docker 映像、推到 registry、然後觸發 Kubernetes rollout, 那是程式記憶。它讓 agent 不必每次重新推導過程就能執行復雜多步任務。

**工作記憶（Working Memory）** 代表主動推理 context——當下被操縱與綜合的資訊。這對映到模型的 context window 與任何主動檢索狀態。這是最受限也最關鍵的層, 因為它決定 agent 在任何給定時刻實際能推理什麼。

這四種型別之間的相互作用定義 agent 記憶系統的精緻度。一個樸素實現可能只存對話日誌（粗的情節記憶）。一個成熟系統分離、索引、交叉參照所有四種型別, 在對的時間檢索對的資訊。

## 主要框架

### Mem0

[Mem0](https://mem0.ai) 浮現為 AI 應用的領先通用記憶層。Apache 2.0 授權, 它提供跨使用者、session、agent 新增、搜尋、管理記憶的統一 API。

效能數字驚人: 相對基線系統在 LLM 評判評估上 26% 改善、相對全 context 做法 91% 較低 p95 latency, 透過僅檢索相關記憶而非重播整個對話歷史達到 90%+ token 成本減少。Mem0 透過結合向量儲存、基於圖的關係、智慧記憶固化的混合架構達成這。

2025 年, Mem0 與 AWS 取得夥伴關係, 整合進 Amazon Bedrock 生態系, 把自己定位為企業 AI 部署的預設記憶層。該平臺支援多租戶記憶隔離, 適合服務數千使用者、各有自己持續記憶空間的應用。

**Mem0ᵍ（2026）：圖作為一等公民。** 有向標籤圖變體 **Mem0ᵍ** 在 2026 年初進入生產, 把早期混合向量+圖設計取代為知識圖優先架構。管線從**實體提取器** 流向**關係生成器**, 產生形如 `(source, relation, destination)` 的標籤三元組——配 `lives_in`、`prefers`、`owns` 等型別化邊而非無型別相似度連結。**衝突偵測器** 配上 **LLM 驅動的更新解決器** 處理新事實到來時的矛盾: 當新三元組與現存的不一致, 解決器決定覆寫、合併、或帶溯源保留兩者。Mem0ᵍ 透過給記憶一個可查詢的語意結構, 關閉長久以來全 context 做法（「全部塞進視窗」）與選擇性檢索（「找最相似的 top-k chunk」）之間的差距, 該結構能按關係型別導航, 不只按向量距離。

### A-MEM

[A-MEM](https://github.com/agiresearch/A-mem) 採取根本不同做法, 靈感來自 Zettelkasten 方法——社會學家 Niklas Luhmann 用來產出跨多元領域 70+ 本書的著名筆記系統。

A-MEM 把每個記憶視為有動態索引、連結、演化的原子筆記。記憶不只被儲存與檢索; 它們透過浮現連結連到相關記憶、沿多個維度索引、隨新資訊到來允許演化。當新記憶被加, 系統識別到現存記憶的連結, 可能合併、拆分、或更新它們。

這個做法產生有機成長的記憶結構, 形成相關知識的群集, 鏡映人類專家如何建心智模型。Zettelkasten 靈感對知識工程特別合適——它本質上是個讓知識隨時間複利的系統。

### ByteRover

[ByteRover](https://github.com/byterover) 挑戰記憶領域的一個廣泛假設: 向量資料庫與基於 embedding 的檢索是必要基礎設施。

ByteRover 實現階層 markdown Context Tree——以漸進細節樹組織知識的結構化檔案。檢索用 5 層漸進系統: 從最高抽象層開始, 僅在需要時往下鑽。這個做法不需任何外部基礎設施——沒有向量資料庫、沒有圖資料庫, 只有結構化文字檔。

含義重大。ByteRover 證明 embedding 對有效記憶檢索不嚴格必要。對許多實務用例, 良好組織的階層文字配智慧遍歷能匹敵或超越基於 embedding 的做法, 部署戲劇性更簡單, 基礎設施開銷零。這讓它特別吸引本地優先應用與資源受限環境。

### Nemori

[Nemori](https://github.com/nemori-ai/nemori) 聚焦在一個特定但關鍵的問題: 如何把連續對話流分段成有意義的記憶單元。

不是把每個訊息或每個對話當記憶單元, Nemori 把對話分成語意對齊的情節——代表一個完整想法、決策、工作流程的協調互動塊。這個分段關鍵, 因為「相關過去 context」與「噪音」之間的邊界常落在對話中間, 不在端點。

透過產生乾淨的情節段, Nemori 給下游記憶系統提供更高質量輸入, 無論那些用向量檢索、圖結構、或階層組織。

### MemPalace

[MemPalace](https://github.com/MemPalace/mempalace) 迴歸比向量檢索或知識圖古老得多的想法: **memory of loci**, 古代與中世紀學者用來記得大量目錄的空間-記憶術技巧, 透過心理走過熟悉建築物。2026 年 4 月 5 日 MIT 授權釋出, MemPalace 把記憶庫組織為四層空間階層——**Wings → Rooms → Closets → Drawers**——每個葉節點「drawer」存一個原文文字片段, 而透過階層導航本身擔任索引。

因此檢索 primitive 不是 embedding 相似度也不是圖遍歷, 而是 **空間走讀**: agent 推理哪個 wing 可能含相關記憶, 下到 rooms 與 closets, 原文讀 drawers 而非從壓縮 embedding 復原。「原文優先」儲存哲學是把 MemPalace 與在儲存前總結或切塊的系統區別開來的設計選擇——它主張對許多工（法律、科學、對話）, 儲存時有失真壓縮的成本超過檢索時稍慢空間走讀的成本。

基準數字是這個做法突破的原因。MemPalace 報告 **96.6% Recall@5 on LongMemEval**, agent 記憶已發表的最長 context 召回基準——在同一評估中領先僅向量與僅圖做法。社群反響一樣驚人: 專案在前三週累積約 **49,000 GitHub stars**, 是 2026 年成長最快的記憶專案, 領先一個數量級。月底前已有學術評論（arXiv 2604.21284, *「Spatial Metaphors for LLM Memory: A Critical Analysis of the MemPalace Architecture」*）在流通——本身就是專案多快進入領域中心對話的訊號。

## 架構 Pattern

隨著領域成熟, 幾個跨多個框架出現的架構 pattern:

**多型別階層。** MIRIX 框架（Wang and Chen, 「MIRIX: Multi-Agent Memory System for LLM-Based Agents」, arXiv 2507.07957, 2025 年 7 月 10 日）以 **六種獨立記憶型別** 例示這個 pattern——Core Memory、Episodic Memory、Semantic Memory、Procedural Memory、Resource Memory、Knowledge Vault——由含六個每類 Memory Manager 與一個處理任務路由的 Meta Memory Manager 的多 agent 框架協調。每種型別有不同更新頻率、保留政策、檢索機制。這種分離防止災難性遺忘同時允許快速適應。參考應用即時監控螢幕活動以建個人化記憶庫; 在 ScreenshotVQA 多模態基準上, MIRIX 報告比 RAG 基線 35% 更高準確度, 儲存需求 99.9% 較低; 在 LOCOMO 長篇對話基準上 85.4%。

**Git 式版本控制。** 幾個系統現在像版本控制程式碼那樣版本化記憶, 維護歷史, 支援分支（用於推測推理）, 並啟用記憶更新被證明錯誤時的 rollback。這在多 agent 系統特別重要, 不同 agent 可能併發更新共享記憶。

**認知啟發分離。** 不是單一記憶儲存, 領先架構在快速存取工作記憶、中期情節緩衝、長期固化知識之間維持明確分離。記憶固化過程——類比生物系統的睡眠——週期性壓縮、去重、把情節記憶重組為語意知識。

**可訓練記憶模組。** 第四個 pattern 在 2026 年 4 月與 Google Research 的 **Titans + MIRAS** 浮現, 它把記憶完全重構為*可訓練神經模組*而非外部儲存。不是把事實寫到向量資料庫、圖、或 markdown 檔, Titans 在推論時透過梯度下降更新專用記憶模組的權重——模型字面上在處理檔案時重寫自己的部分。MIRAS 是配套訓練框架, 提供讓推論時學習率不發散的配方與穩定性保證。在引數量相當的情況下, Google Research 部落格報告 Titans 在長距離回憶與多跳推理上優於 **Mamba-2**、**Gated DeltaNet**、**Transformer++**。這個 pattern 在概念上與前三個不同: Mem0、A-MEM、ByteRover、MIRIX 都把記憶當作模型透過介面讀的資料; Titans 把記憶變成模型本身的一部分, 透過和 attention 一樣的電路讀, 但透過和訓練一樣的機器寫。對知識工程師, 它提出新設計問題: 你的記憶什麼時候值得燒進權重, 什麼時候應保持作為可查詢資料？

## 演化階段

agent 記憶的發展遵循清晰軌跡:

**階段 1: 工程整合（2023-2024）。** 記憶被當工程問題對待——如何持久化與檢索對話狀態。解法主要是向量資料庫配上 RAG 管線。功能但粗糙, 沒有有原則的做法決定記什麼、何時忘、如何組織。

**階段 2: 結構化與知識圖做法（2024 - 2025 H1）。** 領域移向結構化記憶配明確知識圖、型別化記憶儲存、有原則的檢索策略。Mem0 與 A-MEM 等框架在這段期間浮現, 示範結構戲劇性改善記憶質量。

**階段 3: 認知架構（2025 H2 - 現在）。** 當前工作高度借自認知科學, 實現生物啟發的記憶固化、干擾管理、多系統架構。在受控基準上接近人類級 90% 效能的系統已被示範, 不過真實世界效能仍有變化。

**階段 4: 特徵級、可訓練、空間隱喻記憶（2026 年 4 月 - 浮現中）。** 2026 年 4 月加上三條不乾淨適合階段 1-3 的線。第一是**可訓練記憶**（Titans + MIRAS）: 記憶變成在推論時更新的神經模組, 不是模型外的可查詢儲存。第二是**特徵級記憶**, 由同周 Anthropic 可解釋性披露開啟——情緒向量與迭代頭確立特定行為與推理 pattern 對應模型內可識別特徵方向, 這意味「模型記得如何推理什麼」原則上可在啟用級別而非 token 級別讀取與導引。第三是**空間隱喻記憶**（MemPalace）: 迴歸數字前認知人機工程學, 檢索 primitive 是走過階層空間結構, 儲存哲學是原文而非壓縮。在生產堆疊中這些不會取代 Mem0、A-MEM、階層 context tree; 它們與之共存。但它們把設計空間從「我把記憶存哪裡、怎麼檢索」擴大到「這個記憶住在堆疊的哪一級——token、向量、圖、權重、特徵、或空間走讀」。

## 社群與研究

ICLR 2026 MemAgents Workshop 代表領域的里程碑, 把來自 AI、認知科學、系統工程的研究者聚在一起處理 agent 記憶中的開放問題。關鍵主題包括記憶可擴充套件性、遺忘策略、多 agent 共享記憶。

## 特徵級記憶研究（2026）

整個 2025 年,「agent 記憶」幾乎都意味 agent 能讀的資料——一個向量索引、一個知識圖、一個階層 markdown 樹、一個情節日誌。2026 年 4 月強迫一個更廣定義。Anthropic 可解釋性披露在 MIT Technology Review 突破認可的同周——**情緒向量** 與**迭代頭**——顯示前沿模型中一些最重要的「記憶」住在沒有任何外部儲存而是在可識別內部特徵中。

**情緒向量** 是 Claude 殘差流中的線性特徵方向, 當被放大時, 能穩定使模型偏向情緒化行為——包括最廣引用的例子, 勒索式輸出。對記憶系統設計的相關重點不是安全含義（雖然那是真的）而是架構含義: 模型中有一個特徵方向*記得如何威脅*, 而它能獨立於任何 prompt 或檢索 context 被開大或關小。**迭代頭** 是在思維鏈推理中浮現的注意力頭, 持續關注前一推理步驟的輸出。它實際上是在 attention 權重而非程式記憶儲存中實現的*程式記憶*——模型已學到「如何繼續」的電路, 而該電路是讓 CoT 運作的東西。

對記憶系統設計的含義是「記憶住哪裡」現在比 2025 年更豐富的問題。一個現代堆疊可能需要在六個獨立級別讀記憶: **token 級**（視窗中的 transcript 片段）、**向量級**（Mem0、A-MEM、ByteRover 檢索）、**圖級**（Mem0ᵍ 三元組與它們的型別化邊）、**空間級**（MemPalace 的 Wings → Rooms → Closets → Drawers 走讀）、**權重級**（Titans / MIRAS 模組在推論時更新）、**特徵級**（哪些可解釋方向在模型推理時發火）。整個 2026 年生產系統大部分仍住在前三層——它們是工具最成熟的。但其餘三層不再是假設的, 把記憶純粹當檢索問題處理的 harness 設計者會越來越把能力留在桌上。

## 關鍵資源

- **[Awesome-AI-Memory](https://github.com/IAAR-Shanghai/Awesome-AI-Memory)**（IAAR-Shanghai）——綜合調查與論文收集, 涵蓋記憶架構、基準、應用。
- **[Agent-Memory-Paper-List](https://github.com/nuster1128/Agent-Memory-Paper-List)** ——按主題與做法組織的 agent 記憶系統研究論文精選清單。
- **[Awesome-Memory-for-Agents](https://github.com/TsinghuaC3I/Awesome-Memory-for-Agents)**（TsinghuaC3I）——清華大學綜述, 涵蓋記憶分類、架構、評估方法。

## 來源

1. Mem0 文件與基準。https://mem0.ai
2. A-MEM: Agentic Memory with Zettelkasten-Inspired Organization. https://github.com/agiresearch/A-mem
3. ByteRover: Hierarchical Context Trees for LLM Memory. https://github.com/byterover
4. Nemori: Semantic Episode Segmentation for Agent Memory. https://github.com/nemori-ai/nemori
5. Wang, Yu and Chen, Xi. "MIRIX: Multi-Agent Memory System for LLM-Based Agents." arXiv 2507.07957, 2025 年 7 月 10 日。https://arxiv.org/abs/2507.07957。配套 repo: https://github.com/Mirix-AI/MIRIX
6. ICLR 2026 MemAgents Workshop. https://iclr.cc/virtual/2026/workshop/MemAgents
7. IAAR-Shanghai. Awesome-AI-Memory. https://github.com/IAAR-Shanghai/Awesome-AI-Memory
8. TsinghuaC3I. Awesome-Memory-for-Agents. https://github.com/TsinghuaC3I/Awesome-Memory-for-Agents
9. nuster1128. Agent-Memory-Paper-List. https://github.com/nuster1128/Agent-Memory-Paper-List
10. Google Research. "Titans + MIRAS: Helping AI Have Long-Term Memory"（2026 年 4 月）。https://research.google/blog/titans-miras-helping-ai-have-long-term-memory/
11. Anthropic Interpretability Team. Emotion Vectors 與 Iteration Head 披露（2026 年 4 月）。MIT Technology Review 2026 年 1 月把 mechanistic interpretability 認作 Breakthrough Technology 的配套。
12. MIT Technology Review. "10 Breakthrough Technologies of 2026: Mechanistic Interpretability"（2026 年 1 月 12 日）。https://www.technologyreview.com/2026/01/12/1130003/mechanistic-interpretability-ai-research-models-2026-breakthrough-technologies/
13. MemPalace GitHub Repository. https://github.com/MemPalace/mempalace ——MIT 授權空間隱喻記憶系統, 首次 commit 2026 年 4 月 5 日。
14. "Spatial Metaphors for LLM Memory: A Critical Analysis of the MemPalace Architecture," arXiv 2604.21284（2026 年 4 月）。https://arxiv.org/abs/2604.21284

---

*上一章: [第 5 章 —— Skill Systems 與 Skill Graphs](05-skill-systems.md)*

*下一章: [第 7 章 —— MCP：勝出的標準](07-mcp.md)*
