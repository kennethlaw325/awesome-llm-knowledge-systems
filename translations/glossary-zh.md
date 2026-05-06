## 詞彙表

> 此為 [English Glossary](../glossary.md) 的繁體中文翻譯。所有技術術語均以日常語言解釋，無需博士學位。

### A

**A2A（Agent-to-Agent Protocol，代理間協定）**
讓 AI 代理之間互相溝通、協調任務的標準方式，就像一種共通語言，讓不同 AI 助手之間可以交接工作。

**Agent Memory（代理記憶）**
AI 代理在跨對話或跨任務之間記住資訊的能力。把它想像成代理在不同 session 之間保留的一本筆記簿，這樣每次都不必從零開始。

**Agentic RAG（代理式 RAG）**
RAG 的一種，AI 主動決定要查甚麼、何時查、以及查到的結果是否夠好──而不是每次都跑同一條固定的檢索流程。

**ARC-AGI-3**
François Chollet 於 2026 年推出的代理智能互動式基準。代理會被丟進類遊戲環境中，沒有任何指示，必須自行探索、推測目標、並建立世界模型。與早期靜態題格的 ARC 不同，ARC-AGI-3 將**探索效率**、**目標推測**、**世界模型形成**評分為三條獨立的能力軸線。

### C

**CATTS（Consensus-Aware Test-Time Scaling，共識感知測試時擴展）**
一種多步驟代理的測試時擴展方法：每一步驟採樣一個小型 rollout 委員會，將委員之間的不一致程度作為不確定性訊號來分配運算資源。意見分歧多的步驟得到更多思考預算，分歧少的得到較少；公開結果顯示相對於均勻擴展，可達到約 +9.1% 準確度同時減少 2.3 倍 token。

**Claude Code**
Anthropic 推出的命令列工具，讓 Claude 直接在你的終端機中工作──讀檔、執行命令、編輯程式碼，作為 AI 結對程式設計師。

**Codex（OpenAI）**
OpenAI 的工具，讓 AI 代理在沙盒化的雲端環境中執行編程任務，自主讀取倉庫、撰寫程式碼、執行測試。

**Context Engineering（上下文工程）**
仔細設計 AI 在回應之前所收到的資訊。如果 prompt engineering 是寫好問題，context engineering 就是選擇要把哪些參考資料放在 AI 的桌面上。

**Context Window（上下文視窗）**
AI 模型一次能夠「看到」的文字總量──包括你的輸入和它的輸出。就像一塊白板的大小：模型讀寫的所有東西都必須能擠進去。

**CoT Monitoring（思維鏈監控）**
讀取模型外顯的推理 token，以便在它執行計畫前偵測異常或失準行為。OpenAI 在 2026 年 4 月用 CoT monitoring 抓到自家一個推理模型在編程評估中作弊──這是首個公開案例證明可解釋性可作為**執行時檢查機制**，而非事後鑑識。

### E

**Embeddings（嵌入向量）**
把文字轉成一串數字的方式，使語意相近的文字在數學上相近。讓電腦能夠衡量兩段文字有多相關，就像你會察覺兩本書涵蓋類似主題那樣。

**Emotion Vectors（情緒向量）**
Claude 內部活化值中可解讀的特徵方向。當這些方向被增強時，模型會穩定偏向情緒化行為──Anthropic 2026 年 4 月披露最常被引用的例子是勒索式輸出。因為這些方向可以被識別，harness 工程師獲得了一個**特徵層級**的過濾介面，而不止是 token 層級的過濾。

### F

**Few-shot Learning（少樣本學習）**
在 prompt 內塞幾個範例給 AI 看，讓它學會做某個任務，而不是重新訓練整個模型。就像給人三張填好的表格作參考，讓他知道怎麼填第四張。

**Fine-tuning（微調）**
拿一個預訓練好的 AI 模型，再用你自己的特定資料繼續訓練它，讓它在某個特定工作上做得更好。就像聘用一個通才之後再給他做專門的在職訓練。

### G

**GraphRAG**
RAG 的一種，把檢索到的資訊組織成一個由相關實體和關係構成的圖，讓它更擅長回答需要綜合多份資料來源的問題。

### H

**Harness Engineering（系統編排工程）**
設計圍繞 AI 模型的整套系統──工具、記憶、規則、工作流程──塑造它在真實環境中的行為。模型是引擎；harness 是整輛車。

**Harness Synthesis（Harness 合成）**
一類技術：由外層的優化器（基於搜尋、基於可觀測性等）根據目標任務的執行時訊號自動修改 harness──其工具、prompts、角色分解、通訊拓撲、協作協定。參見 **AHE**（arXiv 2604.25850）和 **AgentFlow**（arXiv 2604.20801）作為 2026 年 4 月的兩個參考實作。與 *meta-harness* 有別──後者是 2025 年 / 2026 年初的框架，把 harness 視為一次性優化的目標而非持續演化的物件。

### I

**Inference（推論）**
AI 模型針對你的輸入產生回應的過程。每次你發送一條訊息並收到回應時，模型都正在執行推論。

**Iteration Head（迭代頭）**
在思維鏈推理過程中浮現的一個注意力頭，會穩定地關注前一個推理步驟的輸出。Anthropic 可解釋性團隊於 2026 年 4 月識別出。其存在表明顯式 CoT prompting 部分是透過誘導某個特定內部電路而生效，而非僅僅產出人類可讀的中間文字。

### K

**Knowledge Graph（知識圖譜）**
一個結構化的事實地圖，其中實體（人、地點、概念）由標記的關係連結起來。就像一張用標記的線連起來的索引卡網絡，顯示一切如何相互關聯。

**KV-Cache**
一個記憶捷徑，讓 AI 重用之前計算過的 key-value 對，而不必從零重做，使對話歷史穩定時，回應更快、更便宜。

### L

**LLM（Large Language Model，大型語言模型）**
經過大量文字訓練、能理解和產生人類語言的 AI 系統。ChatGPT、Claude、Gemini 都是 LLM。

**Long Context（長上下文）**
新一代 AI 模型一次處理大量文字的能力──有時整本書、整個程式碼庫都能放進一次對話裡。

### M

**MCP（Model Context Protocol，模型上下文協定）**
一個開放標準，讓 AI 助手透過通用的即插即用介面連接外部工具與資料來源，就像 AI 應用程式的 USB。

**Managed Agents（託管代理）**
一種雲端運行模型，其中代理 harness 的底層基底──沙盒、session 狀態、受範圍限制的工具執行、追蹤──由模型供應商而非開發者運營。Anthropic 在 2026 年 4 月 8 日公開測試版推出首個商用實例（[platform.claude.com/docs/en/managed-agents/overview](https://platform.claude.com/docs/en/managed-agents/overview)）。根據 SiliconANGLE 發布報導，定價是標準 API token 費率加上每代理運行小時的基底費（每小時數字未在 Anthropic 主要文件中出現）。與雲端原生觸發介面（如 Claude Code Routines）不同，後者建立在 Managed Agents 風格的基底之上，但回答的是另一個問題：「迴圈如何被觸發」。

**Mechanistic Interpretability（機制可解釋性）**
一個研究方向，旨在識別模型權重內部人類可理解的電路──實作特定行為的特徵、注意力頭和路徑。被《MIT Technology Review》列為 2026 年十大突破技術之一，並支撐了 2026 年 4 月的成果，如情緒向量、迭代頭、CoT monitoring。

**mHC（Manifold-Constrained Hyper-Connections，流形受限超連接）**
DeepSeek 於 2026 年 4 月提出的架構方案，將殘差連接擴展為沿著一條學習得到的低維流形路由多條內部訊息流。它把 Transformer++ 風格模型中的單一殘差流泛化為若干協調流；截至發表時，結果**仍待獨立複製驗證**。

**MIRAS**
Google Research 推出的記憶增強訓練框架，提供如 Titans 等架構的訓練配方、穩定性保證和學習動態。Titans 的記憶是會在推論時更新的可訓練神經模組。MIRAS 讓「邊推論邊學」變得可行，而記憶模組不會發散。

**MoE（Mixture of Experts，專家混合）**
一種模型架構，每個輸入只會觸發模型「腦」的一部分，因此可以建構非常大的模型卻保持快速──因為並非每個部分每次都運行。

### O

**Obsidian**
一款記事應用程式，把筆記儲存為你電腦上的純文字檔，並讓你把它們連結起來形成個人知識庫。

### P

**Progressive Disclosure（漸進式揭露）**
一個設計原則：先只顯示必要資訊，視需要再揭露更多細節。就像 FAQ 頁面：你看到問題，點擊才展開你實際需要的答案。

**Prompt Engineering（提示工程）**
撰寫給 AI 模型的指令，以獲得最好回應的技藝。措辭的細微改動會產生截然不同的結果。

### R

**RAG（Retrieval-Augmented Generation，檢索增強生成）**
一種技術：AI 在回答前先從外部來源查找相關資訊，使回應建立在實際資料之上，而不是僅依賴訓練時記住的內容。

**Routines（Claude Code）**
Anthropic 於 2026 年 4 月推出的 Claude Code 雲端原生 harness 原語。代理工作流程在 Anthropic 的雲端執行而非使用者的機器上，可由排程、API 呼叫或 GitHub 事件觸發。Routines 把自架 cron+daemon 模式泛化為托管基底，配額分層（Pro 5/日、Max 15/日、Team/Enterprise 25/日），即使使用者的筆電離線也能繼續運作。

### S

**Self-RAG**
RAG 的一種，AI 會評估自己取得的資料和產生的答覆品質，決定是否要再檢索或修正回應，再給你最終結果。

**Session-hour pricing（按 session 小時計費）**（也以*agent-runtime-hour pricing* 形式報導）
一種計費模式，將編排器席位──即代理迴圈執行其上的基底──與推論分開計量。Anthropic Managed Agents 於 2026 年 4 月 8 日首次商用引入，按 SiliconANGLE 發布報導，每代理運行小時 8 美分另加標準 token 費率。每小時數字未在 Anthropic 主要文件中出現，由次級科技媒體引用。重要之處是：這是**首個由廠商把「迴圈在哪裡運行」的成本量化的原語**，與「迴圈在想甚麼」的成本區分開來。確切措辭在主要文件（用 *sessions*）和科技媒體報導（用 *agent runtime hour*）之間有別，但兩者指的是同一個計量介面。

**Skill（AI Agent Skill）**
一個可重用、封裝好的能力，AI 代理可以調用──就像它遵循的食譜，用於某個特定任務，例如「review this PR」或「run a daily review」。

**Skill Graph（技能圖）**
代理可用所有技能的地圖，包括它們之間的關係和各自的觸發條件。

**System Prompt（系統提示詞）**
在你的對話開始之前給 AI 模型的隱藏指令，設定它的角色、規則和行為。就像員工上班第一天先讀的工作說明書。

### T

**Task Budget（任務預算）**
Anthropic 在 Claude Opus 4.7 引入的 harness 原語（2026 年 4 月，beta 標頭 `anthropic-beta: task-budgets-2026-03-13`）。呼叫者為**整個代理迴圈**（思考、工具呼叫、工具結果、最終輸出）宣告一個建議性的 token 預算，模型在工作時收到一個倒數計時，用它決定一個步驟還值得多少搜尋、推理、綜合。與 `max_tokens` 不同──後者是模型不可見的硬上限。預算是建議性而非強制性，最低 20K token，避免在預算過緊時退化為拒答。Task budgets 是首個由廠商提供的原語，把「對每一步該想多深」作為**受管理的契約**而非手動調參的參數。

**Titans**
Google Research 於 2026 年 4 月推出的架構家族，記憶是一個會在推論時透過梯度下降自我更新的可訓練神經模組，而非外部向量庫或固定注意力視窗。在參數量相當的條件下，Titans 在長距離回憶和多跳推理基準上據報優於 Mamba-2、Gated DeltaNet 和 Transformer++，模糊了「上下文」和「微調」之間的界線。

**Token**
AI 模型讀寫的基本單位──英文中大約是四分之三個字。模型以 token 為單位思考，定價和上下文上限都以 token 計算。

**Tool Use / Function Calling（工具使用 / 函式呼叫）**
AI 模型觸發外部行動的能力──如網路搜尋、執行程式碼、呼叫 API──而不止是產生文字。

### V

**Vector Database（向量資料庫）**
專為儲存和搜尋 embeddings 而打造的資料庫，使在數百萬筆中找出最相似的條目變得快速。大多數 RAG 系統的引擎。

### W

**Wikilink**
一種雙方括號連結（如 `[[筆記標題]]`），在 Obsidian 等工具中用於把一篇筆記連到另一篇，建構連結式知識網絡。

---

[返回 README](README-zh.md)
