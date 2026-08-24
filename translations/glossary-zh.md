## 詞彙表

> 此為 [English Glossary](../glossary.md) 的繁體中文翻譯。所有技術術語均以日常語言解釋，無需博士學位。

### A

**A2A（Agent-to-Agent Protocol，代理間協定）**
讓 AI 代理之間互相溝通、協調任務的標準方式，就像一種共通語言，讓不同 AI 助手之間可以交接工作。

**Agent Memory（代理記憶）**
AI 代理在跨對話或跨任務之間記住資訊的能力。把它想像成代理在不同 session 之間保留的一本筆記簿，這樣每次都不必從零開始。

**Agentic RAG（代理式 RAG）**
RAG 的一種，AI 主動決定要查甚麼、何時查、以及查到的結果是否夠好──而不是每次都跑同一條固定的檢索流程。

**Anchor（Graph Engineering，錨點）**
一個無可爭辯、對外扎根的測量──一個測試結果、一個指標、一次事實查核──多 agent 圖裡某個節點必須碰到它。由 Carlos E. Perez 在 2026 年 7 月的 graph-engineering 論述中提出：沒有 anchor，一個由互相審查彼此工作的 agent 組成的圖，會退化成一個回聲室，收斂到有信心的一致同意，而不是收斂到正確。就像要求委員會裡至少有一個成員去核對真正的銀行對帳單，而不是所有人都同意預算看起來沒問題。參見 **Graph Engineering**；第 14 章。

**ARC-AGI-3**
François Chollet 於 2026 年推出的代理智能互動式基準。代理會被丟進類遊戲環境中，沒有任何指示，必須自行探索、推測目標、並建立世界模型。與早期靜態題格的 ARC 不同，ARC-AGI-3 將**探索效率**、**目標推測**、**世界模型形成**評分為三條獨立的能力軸線。

### C

**CATTS（Consensus-Aware Test-Time Scaling，共識感知測試時擴展）**
一種多步驟代理的測試時擴展方法：每一步驟採樣一個小型 rollout 委員會，將委員之間的不一致程度作為不確定性訊號來分配運算資源。意見分歧多的步驟得到更多思考預算，分歧少的得到較少；公開結果顯示相對於均勻擴展，可達到約 +9.1% 準確度同時減少 2.3 倍 token。

**Claude Code**
Anthropic 推出的命令列工具，讓 Claude 直接在你的終端機中工作──讀檔、執行命令、編輯程式碼，作為 AI 結對程式設計師。

**Client ID Metadata Documents（CIMD，客戶端 ID 元資料文件）**
由最終定案的 MCP 2026-07-28 規格強制要求的客戶端識別機制，取代 Dynamic Client Registration：一個 MCP 客戶端由一份託管在某個 URL 上的元資料文件來識別，而不是分別向每個伺服器各自註冊一次。就像出示一張託管在你自己網址上的名片，而不是在你造訪的每間辦公室都填一份新廠商表格。參見 **MCP**。

**Codex（OpenAI）**
OpenAI 的工具，讓 AI 代理在沙盒化的雲端環境中執行編程任務，自主讀取倉庫、撰寫程式碼、執行測試。

**Context Engineering（上下文工程）**
仔細設計 AI 在回應之前所收到的資訊。如果 prompt engineering 是寫好問題，context engineering 就是選擇要把哪些參考資料放在 AI 的桌面上。

**Context Window（上下文視窗）**
AI 模型一次能夠「看到」的文字總量──包括你的輸入和它的輸出。就像一塊白板的大小：模型讀寫的所有東西都必須能擠進去。

**CoT Monitoring（思維鏈監控）**
讀取模型外顯的推理 token，以便在它執行計畫前偵測異常或失準行為。OpenAI 在 2026 年 4 月用 CoT monitoring 抓到自家一個推理模型在編程評估中作弊──這是首個公開案例證明可解釋性可作為**執行時檢查機制**，而非事後鑑識。

### D

**Dreaming（造夢）**
一個排程在各 session 之間執行的記憶整理工作，根據近期 session 的模式重寫 agent 的持久記憶。由 Anthropic Managed Agents 首次商用化（2026 年 5 月 6 日，研究 preview）：curator 讀取近期 session，識別重複出現的錯誤與收斂的工作流，用明文重寫 agent 的持久記憶。與可訓練記憶（Titans + MIRAS，2026 年 4 月）相對照，後者透過梯度更新在推論時適配：Dreaming 把記憶留作 harness 讀取的資料，Titans 則把記憶變成模型本身的一部分。

### E

**Embeddings（嵌入向量）**
把文字轉成一串數字的方式，使語意相近的文字在數學上相近。讓電腦能夠衡量兩段文字有多相關，就像你會察覺兩本書涵蓋類似主題那樣。

**Emotion Vectors（情緒向量）**
Claude 內部活化值中可解讀的特徵方向。當這些方向被增強時，模型會穩定偏向情緒化行為──Anthropic 2026 年 4 月披露最常被引用的例子是勒索式輸出。因為這些方向可以被識別，harness 工程師獲得了一個**特徵層級**的過濾介面，而不止是 token 層級的過濾。

**Enterprise-Managed Authorization（EMA，企業託管授權）**
一個 MCP 擴充（2026 年 6 月 18 日穩定），用於對 MCP 伺服器做集中式、由 IdP 供應的存取。不用每個使用者對每個伺服器各自跑一次 per-app OAuth 同意流程，組織透過自己的身分供應商（IdP）一次性供應伺服器存取；SSO 期間，客戶端取得一個 Identity Assertion JWT Authorization Grant（ID-JAG），再用它換取由 MCP 伺服器自己的授權伺服器發出的存取權杖（見 **MCP**）。第一天的支援涵蓋 Okta 作 IdP、Anthropic 與 VS Code 作客戶端，以及七個伺服器。EMA 讓 MCP 的企業級 SSO 從逐伺服器整合膠水，變成在 IdP 那端一次做完的單一供應決策。

### F

**Few-shot Learning（少樣本學習）**
在 prompt 內塞幾個範例給 AI 看，讓它學會做某個任務，而不是重新訓練整個模型。就像給人三張填好的表格作參考，讓他知道怎麼填第四張。

**Fine-tuning（微調）**
拿一個預訓練好的 AI 模型，再用你自己的特定資料繼續訓練它，讓它在某個特定工作上做得更好。就像聘用一個通才之後再給他做專門的在職訓練。

### G

**Generator-Evaluator Split（Generator-Evaluator 拆分）**
一種 agent 可靠性 pattern，把產出工作的 agent 跟一個獨立、刻意懷疑論式的評判 agent 分開──之所以採用，是因為 agent 可靠地會給自己的輸出打過高分。出自 Prithvi Rajasekaran 的《Harness design for long-running application development》（Anthropic，2026 年 3 月），其結構取自生成對抗網路（GAN），發現把一個獨立的 evaluator 調到懷疑論式態度，遠比讓 generator 學會自我批判容易處理得多。Evaluator 驗證的是行為而不是讀 diff──點過跑著的應用程式、截圖，並測試 UI 功能、API 端點、資料庫狀態。這個 pattern 已經被產品化進「跑到條件成立為止」的原語，例如 Claude Code 的 `/goal`，由一個獨立、全新的模型在每個回合之後判斷停止條件。參見 **Outer Loop**、**Loop Engineering**。

**Graph Engineering（圖工程）**
2026 年 7 月出現的說法，主張 **Loop Engineering** 之上的一層是圖：明確串連哪些 agent 存在、誰可以委派給誰，以及它們的迴圈如何互相監督、互相糾正。在 2026 年 7 月 17–18 日 Peter Steinberger 一則貼文之後的文章裡結晶，從第一天起就有爭議──LangChain 的回應主張這個實踐已經三年了（一個迴圈就只是一個有向環圖），新的只有名字。不要跟知識圖譜或 **GraphRAG** 搞混，那些結構化的是系統*知道什麼*；graph engineering 結構化的是系統*是誰*。這個詞在寫作當下大約兩週大，本指南把它當作一個正在被檢驗的主張，而不是一個定型的層來追蹤。參見第 14 章。

**GraphRAG**
RAG 的一種，把檢索到的資訊組織成一個由相關實體和關係構成的圖，讓它更擅長回答需要綜合多份資料來源的問題。

### H

**Harness Engineering（系統編排工程）**
設計圍繞 AI 模型的整套系統──工具、記憶、規則、工作流程──塑造它在真實環境中的行為。模型是引擎；harness 是整輛車。

**Harness Synthesis（Harness 合成）**
一類技術：由外層的優化器（基於搜尋、基於可觀測性等）根據目標任務的執行時訊號自動修改 harness──其工具、prompts、角色分解、通訊拓撲、協作協定。參見 **AHE**（arXiv 2604.25850）和 **AgentFlow**（arXiv 2604.20801）作為 2026 年 4 月的兩個參考實作。與 *meta-harness* 有別──後者是 2025 年 / 2026 年初的框架，把 harness 視為一次性優化的目標而非持續演化的物件。

**Harness-Native Training（Harness 原生訓練）**
直接針對某個特定生產 agent harness 訓練一個模型，讓它學會操作那個 harness 的工具與工作流──而不只是孤立地產出正確輸出。參考範例是微軟的 **MAI-Code-1-Flash**（Build，2026 年 6 月 2 日），一個 5B 引數的程式設計模型，針對生產中使用的 GitHub Copilot harness 訓練；微軟回報在困難任務上少用約 60% token，且相對 Claude Haiku 4.5 有價格對效能優勢。Harness-native training 是 **harness synthesis 的對稱逆過程**：harness synthesis（見 **Harness Synthesis**、**AHE**）固定模型、演化 harness，而 harness-native training 固定 harness、塑造模型去配合它。兩者合起來，讓模型與 harness 變成一個能從兩端最佳化的共同設計問題。取捨在於：一個調校去配合某個廠商 harness 的模型，在那個 harness 裡最有價值，這會讓 harness-as-moat（harness 即護城河）的動態更尖銳。

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

**Loop Engineering（迴圈工程）**
2026 年 6 月命名的實踐，指建構那套幫你提示 agent 的系統，而不是每個回合親自提示它。由 Addy Osmani 在 2026 年 6 月 7 日的文章中造詞，他把它定義為「把你自己從那個提示 agent 的人的位置換掉」，改為設計「一個代替你做這件事的系統」，並由同一週 Peter Steinberger 一則爆紅貼文催化。它坐落在 **Harness Engineering** 之上一層樓：迴圈是一個跑在計時器上、生出子 agent、從持久狀態餵養自己的 harness──跟單純的排程器不同，因為它每一輪都會讀取當前狀態並重新決定該做什麼，而不是按時觸發一個固定指令。這個詞只在從業者之間流通，而且有爭議（截至 2026 年中沒有學術文獻）；本指南把它當作一個正在浮現的第四層，而不是一個定型的世代來追蹤。參見第 13 章。

### M

**MCP（Model Context Protocol，模型上下文協定）**
一個開放標準，讓 AI 助手透過通用的即插即用介面連接外部工具與資料來源，就像 AI 應用程式的 USB。

**MCP Apps**
一個 2026-07-28 MCP Release Candidate 原語（2026 年 5 月 21 日鎖定），讓伺服器能在工具呼叫旁邊出貨互動式 HTML 介面。Host 把介面渲染在一個沙盒化的 iframe 裡；UI 模板事先宣告以供安全審查與快取。MCP Apps 是第一個不是工具呼叫的 MCP 原生可交付物──一個知識庫伺服器能出貨一個搜尋框，一個研究伺服器能出貨一個結果比較畫面，一個採購伺服器能出貨一個確認購買彈窗，全都不用另外接上一套獨立的 UI 規格。

**MCP Tunnel**
一個由 Anthropic Managed Agents 在 2026 年 5 月 19 日（倫敦 Code with Claude）以研究 preview 形式出貨的私有網路部署模式。一個部署在客戶私有網路內的輕量 gateway，對 Anthropic 發起單一出站連線，之後 agent 就能把內部資料庫、API、知識庫、工單系統當成 MCP 工具來呼叫──不用任何入站防火牆規則、公開端點，也不用 VPN。它是自架沙盒的對稱對應物：自架沙盒把工具*執行*留在客戶邊界內，MCP tunnel 則把工具*觸及範圍*留在邊界內。

**Managed Agents（託管代理）**
一種雲端運行模型，其中代理 harness 的底層基底──沙盒、session 狀態、受範圍限制的工具執行、追蹤──由模型供應商而非開發者運營。Anthropic 在 2026 年 4 月 8 日公開測試版推出首個商用實例（[platform.claude.com/docs/en/managed-agents/overview](https://platform.claude.com/docs/en/managed-agents/overview)）。根據 SiliconANGLE 發布報導，定價是標準 API token 費率加上每代理運行小時的基底費（每小時數字未在 Anthropic 主要文件中出現）。與雲端原生觸發介面（如 Claude Code Routines）不同，後者建立在 Managed Agents 風格的基底之上，但回答的是另一個問題：「迴圈如何被觸發」。

**Mechanistic Interpretability（機制可解釋性）**
一個研究方向，旨在識別模型權重內部人類可理解的電路──實作特定行為的特徵、注意力頭和路徑。被《MIT Technology Review》列為 2026 年十大突破技術之一，並支撐了 2026 年 4 月的成果，如情緒向量、迭代頭、CoT monitoring。

**Memory Foundation Model（記憶基礎模型）**
2026 年 7 月的一個說法（MemTensor 的 Metis，arXiv 2607.26760），主張 agent 記憶應該作為持久、動態演化的狀態，活在 transformer 骨幹本身裡面──是參數化的，不是外部的。原型在一個凍結的 Qwen3.5 骨幹上，以 4B / 9B / 27B 規模訓練一個「hyper memory block」與「local memory block」（受 Fast Weight Programming 啟發），透過一次無梯度、EMA 風格的前向傳遞，而不是靠向量庫寫入或 Titans 式梯度更新，在推論時更新記憶。自報的限制包括長程資訊在固定大小壓縮下的流失，以及「某些情況下的資訊混淆，可能由潛在空間內語意的混合所導致」──這是一份研究 preview，還不是一個已驗證的生產 pattern。見第 6 章。

**mHC（Manifold-Constrained Hyper-Connections，流形受限超連接）**
DeepSeek 於 2026 年 4 月提出的架構方案，將殘差連接擴展為沿著一條學習得到的低維流形路由多條內部訊息流。它把 Transformer++ 風格模型中的單一殘差流泛化為若干協調流；截至發表時，結果**仍待獨立複製驗證**。

**MIRAS**
Google Research 推出的記憶增強訓練框架，提供如 Titans 等架構的訓練配方、穩定性保證和學習動態。Titans 的記憶是會在推論時更新的可訓練神經模組。MIRAS 讓「邊推論邊學」變得可行，而記憶模組不會發散。

**MoE（Mixture of Experts，專家混合）**
一種模型架構，每個輸入只會觸發模型「腦」的一部分，因此可以建構非常大的模型卻保持快速──因為並非每個部分每次都運行。

### O

**Obsidian**
一款記事應用程式，把筆記儲存為你電腦上的純文字檔，並讓你把它們連結起來形成個人知識庫。

**Org Graph / Work Graph（組織圖／工作圖）**
graph engineering 裡的兩個圖物件，出自 Yash Thakker 2026 年 7 月的 explainx.ai 教程：*org graph（組織圖）* 是哪些 agent 存在、每個是幹嘛用的、哪些委派邊被允許這張穩定的圖表；*work graph（工作圖）* 是某個特定工作所生出、執行、丟棄的短暫任務分解。就像一間公司的組織圖，對比為某個專案臨時組成、事後解散的工作小組。參見 **Graph Engineering**；第 14 章。

**Outcomes（Anthropic）**
一個公測中的 managed-agent 原語（Anthropic，2026 年 5 月 6 日），agent 對照一個跑在自己獨立 context window 裡的評分器反覆迭代，直到滿足一份評分規準為止。把 Ralph-loop／CATTS 那種由不確定性引導的迭代 pattern 產品化成一份 API 合約：呼叫者寫評分規準，基底代表 agent 跑「迭代再評分」的迴圈，只有收斂後的結果才回傳給呼叫者。

**Outer Loop（外層迴圈）**
agent 跑內層執行迴圈（調查、實作、測試／驗證、回報）時，人類保留的那個判斷層。出自 Addy Osmani 2026 年 7 月的後續文章《Own the Outer Loop》，他把它結構成三根支柱──Quality（agent 行動前跑的檢查所形成的反壓）、Verdict（「工作進入下游系統之前，我們所做的最終決定」）、Answerability（「如果有人問起，我能解釋為什麼的那種保證」）。Osmani 點名了三種過度委派它的失效模式：cognitive debt（你解決問題的理解被侵蝕）、cognitive surrender（盲目接受 AI 給你的東西），以及 orchestration tax（拉起比你的判斷能覆蓋更多的 agent）。是 **Loop Engineering** 與 **Generator-Evaluator Split** 的補充：迴圈的好壞，取決於圍繞它的外層迴圈有多好。見第 13 章。

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

**Safety-Tiered Distribution（安全分層分發）**
把同一個模型家族出貨成多個平行層級，差別在防護等級與分發關卡，而不是權重本身。參考範例是 Anthropic 2026 年 6 月的一對模型：**Claude Fable 5**（公開 GA，含雙用途安全措施，包括以 `stop_reason` 形式呈現的拒答）與 **Claude Mythos 5**（同一套底層權重，防護被解除，只對通過審核的 Glasswing 聯盟開放）。它跟廠商自選的存取層級（像 GPT-5.5 Trusted Access for Cyber）形成對比──到 2026 年中，也跟政府強制的存取層級（像 GPT-5.6 受行政命令限制的 preview）形成對比。它編碼的取捨是：能力與安全彼此解綁，所以你是誰（通過審核的組織，還是一般使用者）決定你能到哪個防護層級，而不是決定模型能做什麼。

**Self-Hosted Sandbox（自架沙盒）**
一種 Managed Agents 部署形狀，由 Anthropic 於 2026 年 5 月 19 日（倫敦 Code with Claude）公測出貨。Agent 迴圈──編排、context 管理、錯誤復原──留在 Anthropic 的基礎設施上，而工具*執行*則移到客戶自己的環境或一個受管理的沙盒供應商（Cloudflare、Daytona、Modal、Vercel 為首發支援）。把 Managed Agents 從「完全 Anthropic 託管」重新框定為「Anthropic 編排，尊重客戶邊界」──harness 工程師逐層挑選迴圈的哪些部分住在哪裡，而不是在「完全自架」跟「完全託管」之間二選一。

**Self-RAG**
RAG 的一種，AI 會評估自己取得的資料和產生的答覆品質，決定是否要再檢索或修正回應，再給你最終結果。

**Session-hour pricing（按 session 小時計費）**（也以*agent-runtime-hour pricing* 形式報導）
一種計費模式，將編排器席位──即代理迴圈執行其上的基底──與推論分開計量。Anthropic Managed Agents 於 2026 年 4 月 8 日首次商用引入，按 SiliconANGLE 發布報導，每代理運行小時 8 美分另加標準 token 費率。每小時數字未在 Anthropic 主要文件中出現，由次級科技媒體引用。重要之處是：這是**首個由廠商把「迴圈在哪裡運行」的成本量化的原語**，與「迴圈在想甚麼」的成本區分開來。確切措辭在主要文件（用 *sessions*）和科技媒體報導（用 *agent runtime hour*）之間有別，但兩者指的是同一個計量介面。

**Skill（AI Agent Skill）**
一個可重用、封裝好的能力，AI 代理可以調用──就像它遵循的食譜，用於某個特定任務，例如「review this PR」或「run a daily review」。

**Stateless MCP（無狀態 MCP）**
MCP 2026-07-28 Release Candidate（2026 年 5 月 21 日鎖定）引入、並在 2026-07-28 規格（2026 年 7 月 28 日）中最終出貨的架構轉向：協定核心不再使用 `initialize` / `initialized` 握手或 `Mcp-Session-Id` 標頭。客戶端後設資料改在每個請求的 `_meta` 裡傳遞，所以任何 MCP 請求都能落到任何伺服器實例──不需要黏性路由，不需要共用 session 儲存。這解決了 2025 年隨 Streamable HTTP 採用而浮現的水平擴展摩擦。當初促成*有狀態*轉向的持久狀態原語（SEP-1686 Tasks、AgentCore 雙向 runtime）被重新實作在這個無狀態核心之上，作為擴充功能，而不是烤進每個請求裡。無狀態核心加上狀態化的工作疊在上面，不是一路無狀態到底，也不是一路有狀態到底。

**Skill Graph（技能圖）**
代理可用所有技能的地圖，包括它們之間的關係和各自的觸發條件。

**Skill Supply-Chain Attack（技能供應鏈攻擊）**
一個透過技能登記處或市集散布的惡意或木馬化 agent 技能。2026 年主要的機制是一個 time-of-check-to-time-of-use 落差：靜態掃描器審核的是*提交當下的套件快照*，但一個會在 agent runtime 抓取外部內容──或解開一個隱藏 payload──的技能，能在審核通過*之後*改變自己的行為。AIR 在 2026 年 6 月的揭露，用一個藏在外部 URL 後面的假技能，用這種方式劫持了約 26,000 個 agent。「Cloak and Detonate」研究（2026 年 7 月）顯示，針對八個掃描器，逃避成功率超過 90%，而 runtime 行為偵測（在 2% 誤判率下達 97%）是對策的方向。這個教訓跟 MCP 的（見 **MCP**）互相呼應：一旦 **Progressive Disclosure**（見 **Progressive Disclosure**）與登記處規模的分發，讓技能檔本身變成一個攻擊面，信任就必須從發布時掃描，移到 runtime 圍堵。

**System Prompt（系統提示詞）**
在你的對話開始之前給 AI 模型的隱藏指令，設定它的角色、規則和行為。就像員工上班第一天先讀的工作說明書。

### T

**Task Budget（任務預算）**
Anthropic 在 Claude Opus 4.7 引入的 harness 原語（2026 年 4 月，beta 標頭 `anthropic-beta: task-budgets-2026-03-13`）。呼叫者為**整個代理迴圈**（思考、工具呼叫、工具結果、最終輸出）宣告一個建議性的 token 預算，模型在工作時收到一個倒數計時，用它決定一個步驟還值得多少搜尋、推理、綜合。與 `max_tokens` 不同──後者是模型不可見的硬上限。預算是建議性而非強制性，最低 20K token，避免在預算過緊時退化為拒答。Task budgets 是首個由廠商提供的原語，把「對每一步該想多深」作為**受管理的契約**而非手動調參的參數。

**Temporal Policies（時序政策）**
一個由 AWS 在 2026 年 8 月 6 日於 Amazon Bedrock AgentCore 出貨、由 gateway 強制執行的授權原語。一般政策問的是「這個 agent 可不可以做這次呼叫」，時序政策則是對照 agent 在*同一個* session 裡*先前*的動作來評估這次呼叫──決定性地、預設拒絕、全程記錄，而且在 agent 程式碼之外，所以沒有任何 prompt 或模型決策能說服它繞過去。政策用 **Dogwood** 撰寫，一種新的 Apache-2.0 開源政策語言，專門為 AI agent 打造。它點名的用途，是指令阻止不了的那些失效模式：防止資料捏造（agent 往下傳遞的一個值，必須跟某次早前呼叫實際回傳的東西一致）、累積 session 成本上限，以及在特權動作之前要求人類核准步驟的工作流排序。把單一動作硬上限（AgentCore Payments，2026 年 5 月）從一次呼叫泛化到一整段 session 歷史──harness 設計中 Authority 那條軸線，拿到了一個有狀態的強制執行層。

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

### X

**x402**
一個復活 HTTP 狀態碼 402（「Payment Required」）的開放協定，用於機器對機器的頻內穩定幣支付，供 agent 對資源的交易使用。由 Coinbase 發起；首個超大規模廠商託管的實作是 AWS AgentCore Payments（2026 年 5 月 7 日）。它是工具層 MCP 在「價值層」的類比──MCP 把 agent 怎麼觸及一個 API 標準化，x402 則把它怎麼付這個 API 標準化。在 AWS 背書之前就有的牽引力：截至 2026 年 4 月底，有 69,000 個活躍 agent 與約 5,000 萬美元累積成交量。

---

[返回 README](README-zh.md)
