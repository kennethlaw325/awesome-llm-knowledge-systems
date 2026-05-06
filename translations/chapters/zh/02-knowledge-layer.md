# 第 2 章：RAG、長上下文與知識圖譜

> **一句話總結：** 給 AI 取得知識有三種主要方法: 搜資料庫（RAG）、喂長檔案、或在圖裡連結事實。
>
> **為什麼重要：** 如果你用 AI 處理任何關於自己資料的事情, 這章解釋哪種做法最適合你的情境。

**知識檢索層——什麼有效、什麼無效, 為什麼答案几乎永遠是「混合」。**

---

## RAG 沒死

每六個月就有人發表「RAG 死了, 長上下文就夠了」。每六個月企業證明他們錯了。

**Gartner 2025 Q4 企業調查** 發現, 71% 試著用純 context-stuffing（把整個檔案庫喂進大上下文視窗）取代 RAG 管線的組織, 在 12 個月內把 RAG 加回去。理由都一樣: 成本、延遲、規模化時的準確度退化、以及無法處理動態或頻繁更新的知識庫。

RAG 沒死, 它在演化。問題從來不是「RAG 還是不 RAG」——而是「哪種 RAG, 配合什麼其他東西」。

---

## 成本現實

RAG 的經濟論點仍然壓倒性。

一個典型 RAG 管線檢索 5-20 個相關 chunk（約 2,000-8,000 token）, 把它們喂入模型呼叫。同樣查詢的 context-stuffing 做法可能需要載入 500K-1M token 的來原始檔。

**每查詢成本對比（約略, 2026 年中價格）:**

| 做法 | 輸入 token | 約略成本 | 相對成本 |
|------|-----------|---------|---------|
| RAG（針對性檢索） | ~5,000 | ~$0.00008 | 1x |
| Context-stuffing（全庫） | ~500,000 | ~$0.10 | 1,250x |

這不是四捨五入的誤差。在企業規模——每月數百萬查詢——每月推論成本 $80 與 $100,000 的差異決定專案是否能撐過預算審查。

隨模型價格下降, 差距會縮, 但檢索永遠比把整個知識庫硬塞進每次呼叫便宜。資訊理論的定律保證: 選擇相關資訊比處理全部資訊便宜。

---

## 長上下文：何時有效, 何時無效

長上下文視窗（128K、200K、1M+ token）對特定用例是真正變革性的:

**長上下文擅長的地方:**
- **靜態、有邊界的檔案分析**: 分析單一合同、codebase 檔、研究論文, 整個相關語料能放進視窗
- **交叉參照任務**: 在一組固定、一次載入的檔案中找連結
- **總結**: 把大量但有限的輸入濃縮成結構化輸出

**長上下文崩潰的地方:**

**「迷失在中間」退化。** [Liu et al.（2023）](https://arxiv.org/abs/2307.03172) 的研究顯示, LLM 對放在長 context 中間的資訊表現, 顯著差於放在頭或尾的。後續模型改進減少但沒消除這個效應。截至 2026 年初, 當相關資訊埋在 500K+ token 的 context 中時, 模型仍顯示可衡量的準確度退化。

**動態知識庫。** 如果你的知識庫每小時更新（產品庫存、客服工單、新聞流）, 你不能在每次 context window 都重新 embed 整個語料。RAG 的檢索步驟天然處理更新——新檔案被索引並立即可檢索, 不需改 prompt 結構。

**多租戶隔離。** 長上下文在許可權控制上掙扎。當來自多個使用者或許可權級別的檔案存在同一語料中, RAG 管線能在檢索時強制過濾。Context-stuffing 需要小心（且容易出錯）的檔案分隔。

**規模延遲。** 處理 100 萬 token 比處理 5K token 顯著慢, 即便是最佳化後的推論。對面向使用者、需要亞秒級回應時間的應用, 針對性檢索勝出。

### 2026 更新：Titans + MIRAS 重構長上下文取捨

上面所有限制都假設 Transformer 風格的上下文視窗: 一段被 attention 讀取的扁平 token, 每 token 成本不分位置都一樣, 同樣的「迷失在中間」失效模式。**Titans + MIRAS**, Google Research 2026 年 4 月的架構家族, 打破這個假設。在 Titans 中, 記憶不是 attention 視窗——它是**可訓練神經模組**, 在推論期間用梯度下降更新自己的權重, 所以模型字面上把長曆史壓縮成權重更新, 而非作為 token 向前攜帶。MIRAS 提供讓這種邊推論邊學過程穩定的訓練配方。在引數量相當下, Google 報告 Titans 在長距回憶與多跳推理上優於 Mamba-2、Gated DeltaNet、Transformer++。這並不反駁原本的長上下文限制——那些對 GPT-4 Turbo、Gemini 1.5、Claude 仍在用的 attention 視窗正規化仍成立——但它確立**「attention 預算稀缺」框架現在是單一架構家族的屬性, 不是普遍約束**。對從業者, 這意味著長上下文取捨不再是單一曲線。現在至少有兩條: attention 視窗曲線（迷失在中間和每 token 成本主導）與可訓練記憶曲線（成本轉向推論時權重更新, 失效模式轉向穩定性與遺忘）。RAG 在兩者中都仍是強預設, 但 RAG 勝出的*理由*在每個範疇裡不同。

---

## GraphRAG：當扁平檢索不夠

標準 RAG 把檔案當獨立的 chunk。這對事實查詢有效（「退貨政策是什麼？」）, 但對要求*關係推理*的問題失敗（「哪些供應商同時跟我們的延遲出貨和質量投訴相連？」）。

[Microsoft GraphRAG](https://github.com/microsoft/graphrag)（2024-2025）引入混合做法: 從來原始檔構建知識圖, 然後用圖遍歷配合向量檢索回答查詢。

### GraphRAG 怎麼運作

1. **索引階段**: 檔案被處理以提取實體（人、組織、概念）和它們之間的關係。這些與傳統向量 embedding 一起形成圖結構。
2. **社群偵測**: 圖被分割成密集連線實體的社群。每個社群得到一個總結描述。
3. **查詢階段**: 給定查詢, 向量相似度*與*圖遍歷都被用來檢索相關 context。實體關係提供扁平檢索錯過的多跳推理路徑。

### GraphRAG 何時重要

- **多跳查詢**: 「2025 年 IPO 公司與被收購公司之間的共同投資人是誰？」——需要遍歷關係鏈
- **以實體為中心的推理**: 關於特定實體與它們對其他實體之連結的問題
- **全域性總結**: 「我們所有客戶回饋的主題是什麼？」——社群總結提供這, 而不需處理每份檔案

### GraphRAG 何時過度

- 簡單事實查詢（標準 RAG 處理得很好）
- 長上下文能容納一切的小語料
- 實體提取質量低的用例（垃圾進, 垃圾出）

GraphRAG 的索引成本顯著高於標準 RAG。只在關係推理是核心需求時建圖, 不要作為預設。

### 2026 演化：KG 作為長上下文的語意骨幹

整個 2024 與 2025 年大部分時間, GraphRAG 被框為 **RAG 的替代**——一種為有限上下文視窗的模型檢索 chunk 的不同方法。到 2026 年, 這個框架轉變了。當前沿模型把上下文視窗推到數百萬 token 範圍（Gemini 1.5 1M、Kimi 超過 200 萬中文字、還在擴張）, 問題不再是「我們怎麼檢索少量相關 chunk」而是「我們怎麼導覽一個已經夠大、能容納大部分所需的 context」。

在那個世界, 知識圖不再是**檢索替代品**, 變成 **長上下文的結構化索引層**。圖不是用來決定載入哪些 chunk——chunk 已經在視窗裡。圖是用來給模型一張視窗內容的語意地圖: 哪些實體在場、它們如何相關、哪些段落對應哪些主題、矛盾住在哪、哪些多跳路徑連結問題與相關證據。GraphRAG 重新浮現為 **語意骨幹**, 讓 agent 高效走過百萬 token 視窗, 而非作為它出生的 8K token 視窗的解決方案。2026 年 4 月可訓練記憶模組（Titans + MIRAS）的到來不會取代這個角色——早期證據顯示知識圖與可訓練記憶會**共存且很可能在生產堆疊中組合**, 由圖在可訓練模組已經壓縮排權重的內容上提供型別化、可查詢的結構。

---

## 2025-2026 RAG 技術地景

RAG 本身已分支出多個專門做法。關鍵變體:

### Self-RAG（Asai et al., 2023）

[Self-RAG](https://arxiv.org/abs/2310.11511) 訓練模型決定 *何時* 需要檢索、*檢索什麼*、檢索內容是否真的相關。不是總是檢索, 模型生成特殊的「reflection token」來 gate 檢索過程。

**關鍵好處**: 減少不必要的檢索呼叫, 過濾掉不相關的檢索內容, 同時改善效率與準確度。

### Corrective RAG（CRAG）

[Corrective RAG](https://arxiv.org/abs/2401.15884)（Yan et al., 2024）在檢索後加一個驗證步驟。一個輕量評估器評估檢索檔案是否與查詢相關。如果信心低, 系統觸發網頁搜尋或替代檢索策略作為後備。

**關鍵好處**: 主要知識庫不含答案時優雅退化。

### Adaptive RAG

[Adaptive RAG](https://arxiv.org/abs/2403.14403)（Jeong et al., 2024）用分類器根據複雜度把查詢路由到不同檢索策略。簡單查詢直接檢索。複雜查詢多步檢索配思維鏈推理。模糊查詢多次檢索 pass 配結果融合。

**關鍵好處**: 把檢索成本與查詢複雜度匹配, 而非用一刀切管線。

### Golden-Retriever RAG

Golden-Retriever RAG 聚焦於檢索質量, 讓 LLM 自己改寫查詢再檢索。模型生成一個「理想檔案」描述, 然後用作檢索查詢而非原始使用者輸入。

**關鍵好處**: 橋接使用者提問方式與檔案寫作方式之間的詞彙差距。

---

## RAG 作為「Context Engine」

[RAGFlow](https://github.com/infiniflow/ragflow), 開源 RAG 引擎, 2025 年底發表年度回顧, 主張「Retrieval-Augmented Generation」一詞不再捕捉現代 RAG 系統在做的事。他們提議的重構: RAG 已從檢索技術演化為 **Context Engine**——一個通用系統, 用於把異質來源的相關資訊組裝到模型 context window。

這個重構與 [第 1 章](01-evolution.md) 描述的 context engineering 演化對齊。RAG 不只是「檢索並塞」。一個現代 RAG 系統:

- 分類查詢意圖與複雜度
- 路由到合適的檢索策略（向量、關鍵字、圖、混合）
- 重排與過濾結果
- 壓縮檢索內容以符合 token 預算
- 用合適結構與 metadata 格式化結果
- 追蹤溯源以便引用與驗證

這是一個 context 組裝管線, 不是檢索步驟。RAG 系統*就是* context engine。

---

## 混合架構：收斂

2025-2026 的證據清楚指向混合做法。沒有單一技術在所有維度都勝出:

| 維度 | RAG | 長上下文 | 知識圖 |
|------|-----|---------|--------|
| 每查詢成本 | 低 | 高 | 中 |
| 動態更新 | 強 | 弱 | 中 |
| 關係推理 | 弱 | 弱 | 強 |
| 設定複雜度 | 中 | 低 | 高 |
| 準確度（針對性） | 高 | 中 | 高 |
| 準確度（全域性） | 中 | 高 | 高 |

**生產中勝出的 pattern:**

1. **知識圖** 處理實體關係與全域性理解
2. **RAG** 處理特定查詢的動態、針對性檢索
3. **長上下文** 處理整份檔案重要的有界分析任務
4. **查詢路由器** 為每個查詢挑對的策略

這不是理論。規模化生產系統（企業搜尋、程式設計助手、客服 agent）三者並用。工程挑戰不是選一個——是建那個為每個查詢挑對工具的路由器。

---

## 關鍵專案與資源

| 專案 | 描述 | 連結 |
|------|------|------|
| Microsoft GraphRAG | 知識圖 + RAG 混合 | [github.com/microsoft/graphrag](https://github.com/microsoft/graphrag) |
| RAGFlow | 配深度檔案理解的開源 RAG 引擎 | [github.com/infiniflow/ragflow](https://github.com/infiniflow/ragflow) |
| NirDiamant/RAG_Techniques | 綜合 RAG 實現集合 | [github.com/NirDiamant/RAG_Techniques](https://github.com/NirDiamant/RAG_Techniques) |
| LangChain | 含廣泛 RAG 工具的框架 | [github.com/langchain-ai/langchain](https://github.com/langchain-ai/langchain) |
| LlamaIndex | LLM 應用的資料框架 | [github.com/run-llama/llama_index](https://github.com/run-llama/llama_index) |
| Chroma | 開源 embedding 資料庫 | [github.com/chroma-core/chroma](https://github.com/chroma-core/chroma) |

---

## 來源

- Gartner. "Enterprise RAG Adoption" 調查評論, 2025 Q4 ——本章頂引用的 71% 反轉數字在多份行業分析中流通; 主要存取需 Gartner 訂閱, 所以這個數字在此被作為廣為引用的行業資料包告, 而非來自可自由抵達的主要 URL。
- Liu, N. F. 等（2023）. "Lost in the Middle: How Language Models Use Long Contexts." [arXiv:2307.03172](https://arxiv.org/abs/2307.03172)
- Microsoft.（2024）. "GraphRAG: Unlocking LLM discovery on narrative private datasets." [microsoft.com/research](https://www.microsoft.com/en-us/research/blog/graphrag-unlocking-llm-discovery-on-narrative-private-datasets/)
- Asai, A. 等（2023）. "Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection." [arXiv:2310.11511](https://arxiv.org/abs/2310.11511)
- Yan, S. 等（2024）. "Corrective Retrieval Augmented Generation." [arXiv:2401.15884](https://arxiv.org/abs/2401.15884)
- Jeong, S. 等（2024）. "Adaptive-RAG: Learning to Adapt Retrieval-Augmented Large Language Models through Question Complexity." [arXiv:2403.14403](https://arxiv.org/abs/2403.14403)
- RAGFlow.（2025）. "Year-End Review: From RAG to Context Engine." [github.com/infiniflow/ragflow](https://github.com/infiniflow/ragflow)
- NirDiamant.（2025）. "RAG Techniques." [github.com/NirDiamant/RAG_Techniques](https://github.com/NirDiamant/RAG_Techniques)
- Google Research.（2026 年 4 月）. "Titans + MIRAS: Helping AI Have Long-Term Memory." [research.google/blog/titans-miras-helping-ai-have-long-term-memory/](https://research.google/blog/titans-miras-helping-ai-have-long-term-memory/) ——可訓練記憶模組在相當尺寸下優於 Mamba-2 / Gated DeltaNet / Transformer++。

---

*上一章: [第 1 章 —— 三個世代](01-evolution.md)*

*下一章: [第 3 章 —— Context Engineering](03-context-engineering.md)*
