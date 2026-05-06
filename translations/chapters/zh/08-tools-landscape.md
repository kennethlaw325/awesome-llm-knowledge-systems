# 第 8 章：工具地景 —— AI 原生知識管理

> **一句話總結：** AI 驅動知識管理的工具地景從 AI 增強的筆記應用一路到完全 AI 原生的平臺。
>
> **為什麼重要：** 如果你做筆記、管理知識、組織資訊, AI 正在改變這個空間內每個工具的運作方式。

## 地景

人們用來組織、檢索、推理自己知識的工具正圍繞 AI 重建。本章調查 AI 驅動知識管理的主要平臺——不是產品評測, 而是本報告通篇討論的知識工程原則的實現。每個工具對人類與 AI 應如何在知識工作上協作下不同的架構賭注。

## Notion AI

Notion 佔協作知識管理市場約 25%, 讓它的 AI 策略對整個空間有重大影響。

**Notion 3.0**（2025 年 9 月）標誌根本轉變: Notion 把 AI 層從自動完成功能重建為自主 agent。不是建議續寫或回答關於你 workspace 的查詢, Notion 的 AI agent 現在能獨立導覽你的 workspace、建並修改頁面、更新資料庫、執行多步工作流。它理解你的 workspace 結構、跨頁面交叉參照資訊、維持關於你組織 pattern 的 context。

2026 年 1 月, Notion 引入多模型支援, 讓使用者把不同任務路由到不同模型: GPT-5.2 用於創意寫作、Claude Opus 4.6 用於分析任務、Gemini 3 用於多模態工作。這種模型路由做法反映成熟的理解: 沒有單一模型在每件事上都頂尖, 知識管理層應該是模型無關的。

Notion 的強項是它結合結構化資料（資料庫、關聯、rollup）與非結構化內容（頁面、block）。這種混合結構給 AI agent 豐富的後設資料可用——不只是文字搜尋, 還有型別化屬性、實體之間關聯、明確階層。

## Obsidian

Obsidian 佔整體知識管理市場約 8%, 但那個數字戲劇性低估它的影響力。在開發者、研究者、技術知識工作者——最積極實驗 AI 增強知識系統的人口——Obsidian 主導個人知識管理（PKM）利基。

截至 2026 年 2 月, Obsidian 有超過 150 萬活躍使用者（年增 22%）和 2,700+ 社群外掛生態系。它的架構選擇讓它獨特地適合 AI 整合:

**本地優先 markdown。** 每個筆記是你檔案系統上的一個純文字 markdown 檔。沒有專有資料庫、沒有云端依賴、沒有供應商鎖定。這意味任何能讀寫檔案的 AI 工具都能與 Obsidian vault 一起運作。無 API 金鑰、無 OAuth 流程、無 rate limit——只有檔案。

**雙向連結。** Obsidian 的 `[[wikilink]]` 語法隱含創造一個知識圖。每個連結是一個關係。結果的圖結構正是增強 AI 檢索與推理的那種結構化知識。

**外掛可擴充套件性。** 外掛生態系產生幾個突出的 AI 整合:

- **[Copilot for Obsidian](https://github.com/logancyang/obsidian-copilot)**（6,500+ GitHub stars）——用任何 LLM 與你的 vault 聊天。為基於 RAG 的檢索索引你的筆記, 支援多個 embedding 供應商, 跨 session 維持對話 context。

- **[Smart Connections](https://github.com/brianpetro/obsidian-smart-connections)**（4,700+ GitHub stars, $25/月 Pro 層）——AI 驅動的筆記發現, 你寫作時浮現語意相關筆記。用本地 embedding 跨你的 vault 建相似度索引, 不送資料到外部服務。

- **[Claudian](https://github.com/claudian-ai/claudian)**（5,800+ GitHub stars）——Claude 與 Obsidian 之間的深度整合, 讓 Claude 能讀、寫、推理 vault 內容, 配完整 context 覺知。

Obsidian 的本地優先架構讓它對隱私意識使用者、對知識庫本身敏感（研究筆記、專有分析、個人日記）的工作流是天然適合。取捨是協作功能落後雲端原生工具如 Notion。

## Mem

[Mem](https://mem.ai) 在地景中採取最激進立場: 知識管理應該需要零手動組織。沒有資料夾、沒有標籤、沒有手動分類。你寫筆記, Mem 的 AI 處理其他一切——把相關內容群集、在你需要時浮現相關資訊、維持連貫知識庫而不需使用者做任何組織勞動。

這個做法直接押注 AI 檢索已變得夠好可以取代人類策展。對覺得傳統 PKM 系統太苛刻的使用者, Mem 提供有說服力的替代。風險是沒有人類可讀組織, 使用者失去稽核、debug、理解自己知識庫的能力。

## 浮現平臺

幾個較新平臺正探索替代做法:

**[Heptabase](https://heptabase.com)** 用視覺畫布模型, 筆記作為卡片存在於無限空間表面。使用者視覺地排列、連結、群集筆記, 創造空間關係補足文字連結。這空間維度加一層文字系統不能複製的組織。

**[Capacities](https://capacities.io)** 引入基於物件的知識管理, 每片內容是有定義屬性與關聯的型別化物件（人、專案、會議、概念）。這種強型別做法比自由形式筆記產生更乾淨的結構化資料供 AI 消費。

**[Tana](https://tana.inc)** 實現 supertag——一個系統, 任何節點能用定義其結構、欄位、行為的型別標籤。Supertag 在 outliner 上面創造使用者定義的 schema 層, 啟用結構化資料捕捉而不犧牲自由形式筆記的靈活性。

## AI 輔助 vs. AI 原生差距

地景中浮現一個關鍵區分: 把 AI 功能栓在現有架構上的工具, 與從零圍繞 AI 設計的工具之間的差異。

**AI 輔助工具** 在現存知識庫上加「問 AI」按鈕、AI 生成總結、聊天介面等功能。底層資料模型、組織正規化、使用者體驗根本不變。大多數現有者——包括早期版 Notion AI——屬於這類。

**AI 原生工具** 把 AI 作為知識工作的一等參與者來設計核心架構。它們的資料模型為 AI 檢索最佳化。組織結構被設計為由 AI 而非人類維護。使用者體驗假設 AI 處理知識管理的繁瑣部分（分類、連結、浮現）, 人類聚焦在創造與決策。

這兩種做法的差距在擴大。AI 輔助工具永遠會被為只人類工作流設計的資料模型限制。AI 原生工具能為越來越定義知識工作的人類-AI 協作最佳化。

## 這些工具如何連到生態系

本章工具不與本報告描述的知識工程生態系分離——它們是它的消費者面實現。每個概念都直接對映:

**RAG** 是當你問 Copilot for Obsidian 一個問題, 它從你 vault 檢索相關筆記時發生的事。第 3 章的切塊策略、embedding 模型、檢索演算法在底下跑。

**第 6 章的記憶系統** 驅動 Notion AI 與 Mem 的個人化——學你的偏好、記你的專案、隨時間適應的能力。

**第 5 章的 context engineering** 決定這些工具產生回應時如何決定包含什麼資訊。視窗管理、優先化、壓縮技術讓 AI 功能感覺智慧而非通用。

**第 7 章的 MCP** 越來越是這些工具用來連到外部資料來源的協議, 讓你的知識庫能透過標準化介面從 GitHub、Slack、email、資料庫拉取。

這些工具是知識工程的抽象原則變成具體每日實務的地方。它們是個人為他們的個人與專業知識實現 RAG、記憶、context engineering 的 harness。

## AI 速度悖論

伴隨 *個人* 知識管理的工具地景, 平行故事在開發者工具中上演——2026 年 4 月它產生年內最受討論的資料點之一。Harness.io 與 Infosys 聯合發表 **「2026 DevOps 現狀」** 報告, 頭條發現變得叫做 **AI 速度悖論**:

> **69% 團隊報告部署瓶頸, 即使 AI 輔助編碼快了 45%。**

機制直接。AI 程式設計助手（Copilot、Cursor、Claude Code、Codex）讓程式碼生成戲劇性更快。更多 PR 開、更多 diff 到、更多候選實現堆在審查與部署階段。但生成下游的系統——程式碼審查、測試基礎設施、安全掃描、合規檢查、部署管線、事件回應——沒以同樣速度擴充套件。生成不再是約束。**評估與治理是新約束。**

報告給從業者私下叫了一打不同名字的 pattern 一個名字: **「Harness Fatigue」**。它描述團隊試圖為 AI 生成程式碼建自動化護欄, 速度跟生成本身一樣的掙扎。每個新模型釋出讓問題更糟, 讓產生需要審查的更多程式碼更容易。

這個框架從相反方向落到本報告從第 4 章起就在做的同一論點: 當行業整個 2025 年講「harness 是護城河」, 潛文是建好 harness 的工程團隊會拉開領先。2026 年, 速度悖論把同觀察轉成警告: 不擴充套件評估與治理層就擴充套件生成的團隊發現自己整體走得更慢, 不更快。瓶頸移了, 但總吞吐量未必改善。

對知識工程的實務收穫:「harness」不再只是為生產用包模型的東西。它也是必須與生成速度同步擴充套件的東西——否則部署吞吐量沉默地飽和, 而每個人都堅稱 AI 讓他們更快。

**而基底本身現在可移植。** 2026 年 4 月 27 日, Microsoft 與 OpenAI 公佈修訂過的合作協議, 結束 OpenAI 對 Azure 的雲端獨家（OpenAI 現在能透過 AWS、Google Cloud 或任何供應商服務 API 存取）, 不對稱封頂營收分成支付, 移除久爭議的 AGI 條款（會讓 OpenAI 單方宣告 AGI 已達成時退出財務義務）。對知識工程團隊這重要不是商業新聞而是基底變更: 最大封閉權重前沿模型不再鎖在一個雲端後面。「你跑哪個雲端」不再是限制「你能存取哪些模型」的選擇——至少對 GPT 家族, 在 DeepSeek 與開源權重生態系已享有的同樣條件下。結合 DeepSeek V4 的 day-one Ascend NPU 支援（第 11 章, 4 月 24 日）, 2026 下半年開始, 可移植基底是預設期望而非例外。

## 來源

1. Notion. "Introducing Notion 3.0."（2025 年 9 月）。https://www.notion.so/blog
2. Notion. "Multi-Model AI."（2026 年 1 月）。https://www.notion.so/blog
3. Obsidian 使用統計（2026 年 2 月）。https://obsidian.md
4. Copilot for Obsidian. https://github.com/logancyang/obsidian-copilot
5. Smart Connections. https://github.com/brianpetro/obsidian-smart-connections
6. Claudian. https://github.com/claudian-ai/claudian
7. Mem. https://mem.ai
8. Heptabase. https://heptabase.com
9. Capacities. https://capacities.io
10. Tana. https://tana.inc
11. Microsoft. "The next phase of the Microsoft-OpenAI partnership."（2026 年 4 月 27 日）。[https://blogs.microsoft.com/blog/2026/04/27/the-next-phase-of-the-microsoft-openai-partnership/](https://blogs.microsoft.com/blog/2026/04/27/the-next-phase-of-the-microsoft-openai-partnership/)
12. OpenAI. "The next phase of the Microsoft partnership."（2026 年 4 月 27 日）。[https://openai.com/index/next-phase-of-microsoft-partnership/](https://openai.com/index/next-phase-of-microsoft-partnership/)

---

*上一章: [第 7 章 —— MCP：勝出的標準](07-mcp.md)*

*下一章: [第 9 章 —— 中國 AI 生態系](09-china-ecosystem.md)*
