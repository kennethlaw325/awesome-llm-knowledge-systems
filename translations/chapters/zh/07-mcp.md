# 第 7 章：MCP —— 勝出的標準

> **一句話總結：** MCP 是一個通用標準, 讓 AI 透過單一協議連線到任何外部工具或資料來源。
>
> **為什麼重要：** 把 MCP 想成 AI 的 USB——之前每個工具都需要自己的客制連線。現在有一個插頭到處通用。

## 什麼是 MCP？

Model Context Protocol（MCP）是 Anthropic 創造的開放協議, 標準化 AI 模型如何連線到外部工具、資料來源、服務。MCP 之前, 每個 AI 整合都是客制——客制函式定義、專有工具格式、手寫認證、脆弱粘合程式碼。MCP 用通用介面取代這碎片: 任何模型都能用單一協議發現、認證、呼叫任何工具。

把 MCP 想成 AI 的 USB。USB 之前, 每個外設需要自己的聯結器、驅動、協議。USB 沒讓外設更強大——它讓它們可互操作。MCP 對 AI 工具生態系做同樣的事。一個 MCP 伺服器實現能服務 Claude、GPT、Gemini, 或任何講該協議的模型。一個 MCP 客戶端能連到數千伺服器而不需客制整合程式碼。

## 時間線：從推出到 Linux Foundation

**2024 年 11 月。** Anthropic 把 MCP 作為開源規格釋出, 配 Python 與 TypeScript 的參考實現。初次釋出含一些參考伺服器（filesystem、GitHub、Slack）與建客制伺服器的 SDK 支援。反響審慎樂觀——AI 社群之前看過被提議的可互操作性標準。

**2025 年 4 月。** 推出後六個月, MCP 跨過累積 800 萬 SDK 下載, 社群已建超過 5,800 個伺服器。生態系成長比任何人預期都快。關鍵的是, 競爭 AI 實驗室開始採納該協議, 而非創造替代。

**2025 年底。** MCP 被捐給 Agentic AI Foundation, Linux Foundation 旗下的新實體, 由 Anthropic、Block、OpenAI 聯合治理。這個動作中和「Anthropic 控制標準」的關切, 把 MCP 確立為真正行業標準而非供應商專屬協議。

**2026（現在）。** MCP SDK 跨所有套件 registry 下載每月超過 9,700 萬。生態系含 75+ 個由 foundation 維護的官方聯結器, 加上數千個社群建的伺服器。該協議已成為 AI 應用的預設整合層, 像 REST 之於 web API。

## 為什麼它勝出

幾個因素解釋 MCP 的快速主導:

**第一天就開放標準。** MCP 在寬鬆授權下發布, 含完整規格而非只 SDK。這意味競爭者能實現它而不依賴 Anthropic 的程式碼或善意。

**簡單架構。** 協議有三個核心概念: 客戶端（AI 模型一側）、伺服器（工具/資料一側）、傳輸層（它們如何溝通）。伺服器用 JSON Schema 描述暴露工具。客戶端發現並呼叫。傳輸層處理溝通層（stdio、HTTP+SSE、WebSocket）。這個簡單讓採納瑣碎——一位勝任開發者能在一小時內建好 MCP 伺服器。

**供應商中立治理。** 捐給 Linux Foundation, 配 OpenAI 作為聯合治理成員, 消除了最後可信反對。當你的主要競爭者聯合治理標準, 標準是真正中立的。

**網路效應。** 每個新 MCP 伺服器讓協議對每個客戶端更有價值, 反之亦然。一旦生態系跨過有用伺服器的臨界質量, 不支援 MCP 的成本變得高於採納它的成本。

## 關鍵採用者

MCP 採納的廣度說明它的主導:

- **OpenAI** 把 MCP 支援整合進 ChatGPT 平臺與 Agents SDK, 讓 GPT 模型能用任何 MCP 伺服器。
- **Google DeepMind** 給 Gemini 加了 MCP 客戶端支援, 引用生態系相容性為主要動機。
- **Microsoft** 走最遠, 在 Windows 的 OS 層級建 MCP 支援, 跨 Azure AI 服務、Copilot、GitHub Copilot 整合。
- **Amazon / AWS** 在 2026 年 4 月出貨 **Bedrock AgentCore Runtime**, 第一個生產級雙向 MCP runtime, 在標準協議上加 elicitation 與 sampling（見下方「有狀態 MCP 轉變」）。
- **GitHub** 把 Copilot extensions 系統重建在 MCP 上, 取代它們的專有工具格式。
- **Figma、Slack、Block、Notion** 全部出貨官方 MCP 伺服器, 讓它們的平臺成為任何 AI 工作流中的一等公民。
- **Hugging Face** 在它的模型 hub 旁邊託管社群 MCP 伺服器的 registry。
- **LangChain** 與其他編排框架提供原生 MCP 客戶端支援, 讓它成為預設工具整合方法。

**MCP 作為合成維度。** 一個微妙的 2026 年發展: MCP 工具選擇開始作為自動 harness 合成系統中的*變數*之一出現, 而非固定基底。AgentFlow 論文（arXiv 2604.20801, 2026 年 4 月）把 agent 角色、prompt、*工具*、通訊拓撲、協調協議視為它合成迴路搜尋的型別化圖 DSL 的五個維度。對 MCP 覺知的 harness 設計者這是雙面刃。MCP 的標準化讓工具維度真正可搜尋——合成迴路能用一個 MCP 伺服器換另一個而不重寫整合層。但同樣的標準化讓 MCP 伺服器本身變成選擇候選: 問題不再是「我裝哪些伺服器」而是「在可觀測性壓力下我的 harness *演化成用* 哪些伺服器」。

## 與知識工程的連結

MCP 本身不是知識工程技術——它是讓知識工程可擴充套件的基礎設施層。本報告討論的每個做法——RAG 管線、知識圖、記憶系統、context engineering pattern——都需要把外部知識餵給模型。MCP 標準化這個喂法。

考慮一個實務例子: 一個增強了知識的 AI agent 需要存取公司 wiki、查詢資料庫、搜尋向量儲存、讀檔案系統。沒有 MCP, 每個整合都需要客制程式碼、客制認證、客制錯誤處理。有 MCP, 每個都是一個 MCP 伺服器, agent 透過統一介面連到它們全部。

這是 MCP 對知識工程生態系核心的原因。它不取代 RAG 或記憶——它提供讓它們跨模型與平臺可組合、可移植、可互操作的管線工事。

## Meta-Tool Pattern

MCP 採納浮現的最重要架構 pattern 之一是 Meta-Tool Pattern, 也叫工具的漸進式揭露。

問題: 當 MCP 生態系成長, 一個 agent 可能有數十或數百工具的存取權。把它們的 schema 全載入到 context window 是浪費的——大多數工具對任何給定任務無關。載入 29 個工具 schema, 你在模型永不會用的工具描述上燒數千 token, 你增加模型選錯工具的機會。

解法: 不是前置載入所有工具 schema, 載入兩個 meta-tool: **發現工具**讓 agent 按描述搜尋相關工具, **執行工具**透過參照呼叫已發現工具。Agent 先發現當下任務有什麼工具可用, 然後只載入它需要的 schema。

該 pattern 在工具密集環境減少 context window 消耗 80-90%, 透過減少決策空間改善工具選擇準確度。它已成為任何含 10-15 個以上可用工具部署的最佳實務。

## 2026 挑戰

儘管成功, MCP 面對顯著的開放挑戰:

**稽核軌跡。** 在企業環境, 每次工具呼叫需要日誌、歸屬、合規追蹤。當前 MCP 規格不規定稽核軌跡格式, 導致不一致實現。

**SSO 整合認證。** MCP 的認證故事自推出以來顯著改善, 但跨完整客戶端-伺服器-傳輸鏈整合企業 SSO 系統（SAML、OIDC）仍摩擦重。最近批准的 MCP OAuth 2.1 流程處理這一些, 但採納還在 rollout。

**Gateway 行為。** 當組織規模化部署 MCP, 它們需要 gateway 層做 rate limiting、存取控制、請求路由、監控。生態系缺少標準 MCP gateway 規格, 導致專有解法。

**配置可移植性。** MCP 伺服器配置（連哪些伺服器、用什麼憑證、按什麼順序）沒有標準化。在機器、團隊、組織間移動 MCP 設定需要手動重新配置。

**工具描述質量。** MCP 的有效性完全依賴工具描述質量。描述差的工具導致錯誤呼叫。沒有工具描述質量的標準、沒有 linting、沒有認證。

**Schema 版本控制。** 當 MCP 伺服器更新它的工具 schema, 現存客戶端可能壞。該協議缺內建版本控制與相容性協商機制。

**工具重疊。** 數千社群伺服器中, 多個伺服器常提供重疊功能。該協議沒去重或偏好表達機制。

## 2026：有狀態 MCP 轉變

整個頭 18 個月, MCP 根本上是個 **無狀態 RPC 協議**: 客戶端呼叫伺服器, 伺服器返回結果, 對話繼續。這模型對簡單工具呼叫（讀檔案、查詢 API、貼訊息）運作良好, 但對任何長期或互動東西掙扎。2026 年 4 月, 兩個發展開始把 MCP 推向真正編排層。

**SEP-1686：Tasks Primitive。** 在 2026 年 4 月 MCP Dev Summit 引入, **SEP-1686** 給協議加了一個耐久任務狀態機。每個長期工具呼叫變成一個有持續 ID 的 **task**, 狀態有五種: `working`、`input_required`、`completed`、`failed`、`cancelled`。客戶端能開始任務、斷線、之後重連查狀態或取結果——一個 **call-now / fetch-later** pattern。Task ID 與伺服器送出的通知關聯, 客戶端能訂閱進度事件而不必維持開放連線。該 primitive 直接瞄準 MCP 之前強迫客制 workaround 的工作流:

- 花數分鐘到數小時完成的**資料管線**
- 跨大 repo 的**程式碼遷移**
- 完整 CI 套件的**測試執行**
- 衍生子 agent 與等外部 API 的**深度研究**
- 一個 agent 非同步把工作交給另一個的**多 agent 系統**

SEP-1686 在 2026 年 4 月 MCP 規格中作為實驗性出貨。它是從無狀態 RPC 邁向耐久、可恢復編排的第一個認真步驟。

**Amazon Bedrock AgentCore：第一個雙向 runtime。** 也在 2026 年 4 月, AWS 出貨 **Bedrock AgentCore Runtime**, 第一個實現 **雙向** 溝通的生產 MCP runtime。標準 MCP 是客戶端發起: 客戶端呼叫工具, 伺服器回應。AgentCore 加上兩個伺服器發起的能力:

- **Elicitation。** 執行中, 伺服器能暫停並按 JSON schema 向使用者請求結構化輸入。這把先前需要客制 UI 層的多步工作流變成協議級互動。一個遷移工具能停下來問「我應該針對哪個分支？」配型別化回應。
- **Sampling。** 伺服器能從客戶端請求 LLM 生成完成, 而不必持有自己的模型憑證。伺服器提供 prompt 與取樣引數; 客戶端跑自己的模型並返回完成。這讓工具伺服器做 LLM 驅動的工作（總結、分類、提取）, 同時使用者的模型、配額、計費留在客戶端。

一起, elicitation 與 sampling 完成 MCP 的雙向協議表面。伺服器現在能 **驅動** 部分對話, 不只對呼叫回應。

**含義。** 2025 年 MCP 的框架是「無狀態工具的統一插頭」。2026 年框架更廣: MCP 正變成 **有狀態、互動、雙向 agent 編排** 的協議層。工具伺服器不再被動——它們能持有耐久狀態、暫停等使用者輸入、向客戶端請求 LLM 工作。對知識工程, 這意味長期檢索管線、分階段資料豐富、人在迴路工作流終於有原生協議跑在上面。

## 市場情境

行業分析師把 2025 年 AI 工具整合市場（MCP 是其中主導協議）預測在 18 億美元, 當企業採納加速時預期顯著成長。這個數字包含 MCP 基礎設施、伺服器開發、gateway 服務、相關工具。

## 關鍵資源

- **[modelcontextprotocol.io](https://modelcontextprotocol.io)** ——官方規格、SDK、文件。
- **Anthropic MCP 課程** ——可在 [Skilljar](https://anthropic.skilljar.com) 與 [DeepLearning.AI](https://www.deeplearning.ai/short-courses/) 取得, 涵蓋協議基礎與伺服器開發。
- **The New Stack** ——MCP 架構、採納、挑戰的持續技術報道。關於 meta-tool pattern 與企業部署 pattern 的著名文章。
- **MCP SDK 下載統計** ——npm（`@modelcontextprotocol/sdk`, [https://www.npmjs.com/package/@modelcontextprotocol/sdk](https://www.npmjs.com/package/@modelcontextprotocol/sdk)）與 PyPI（`mcp`, [https://pypi.org/project/mcp/](https://pypi.org/project/mcp/)）作為第一方採納指標。

## 來源

1. Anthropic. "Introducing the Model Context Protocol."（2024 年 11 月）。https://www.anthropic.com/news/model-context-protocol
2. Model Context Protocol Specification. https://modelcontextprotocol.io
3. Linux Foundation. "Agentic AI Foundation Established."（2025）。https://www.linuxfoundation.org/press/agentic-ai-foundation
4. MCP SDK 下載統計, npm: [https://www.npmjs.com/package/@modelcontextprotocol/sdk](https://www.npmjs.com/package/@modelcontextprotocol/sdk) 與 PyPI: [https://pypi.org/project/mcp/](https://pypi.org/project/mcp/)（2026 Q1 累積約 9,700 萬下載, 在次級報道中廣為引用）。
5. The New Stack. "The Meta-Tool Pattern: Progressive Disclosure for AI Tools."（2025）。
6. Anthropic. MCP Course. Skilljar. https://anthropic.skilljar.com
7. DeepLearning.AI. "Building MCP Servers." https://www.deeplearning.ai/short-courses/
8. Microsoft. "MCP Support in Windows and Azure."（2025）。https://devblogs.microsoft.com
9. OpenAI. "Agents SDK: MCP Integration."（2025）。https://openai.com/index/new-tools-for-building-agents
10. AgentFlow / "Synthesizing Multi-Agent Harnesses for Vulnerability Discovery." arXiv 2604.20801（2026 年 4 月）。[https://arxiv.org/abs/2604.20801](https://arxiv.org/abs/2604.20801)

---

*上一章: [第 6 章 —— Agent Memory：缺失的層](06-agent-memory.md) | 下一章: [第 8 章 —— 工具地景：AI 原生知識管理](08-tools-landscape.md)*
