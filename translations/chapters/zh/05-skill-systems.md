# 第 5 章：Skill Systems —— 技能、技能圖與漸進式揭露

> **一句話總結：** Skill 是可重用的指令集, 告訴 AI 如何做特定任務; skill graph 把它們連成可導航的知識網路。
>
> **為什麼重要：** 不用每次都跟 AI 解釋同一件事, skill 讓你教一次就永遠複用那份知識。

Skill 是預先打包的指令集——內含 prompt、工具配置、行為規則的自足束——在需要某種特定能力時被注入 agent 的 context window。它們是 agent 系統從少數內建行為擴充套件到數百上千專門能力, 同時不讓模型淹沒在不相關指令中的機制。

本章涵蓋技能系統的架構、它們造成的組合問題, 以及解決它的漸進式揭露 pattern。

---

## 5.1 技能概念

最簡單的技能是含特定任務指令的 markdown 檔（或結構化文字塊）。當使用者請求匹配技能的觸發條件, 技能內容被載入到 context window。無匹配時, 該技能貢獻零 token。

這與一個想涵蓋每種能力的整體系統 prompt 根本不同。一個描述 90 個工具與 50 種行為模式的系統 prompt 在使用者開始打字之前就可能消耗 50,000 token 以上。基於技能的系統只載入相關的, 讓基線 context 精簡, 把視窗容量保留給實際任務。

設計 pattern 借自軟體工程: skill 之於 agent 就像 plugin 之於應用。它們提供可擴充套件性而不臃腫。

## 5.2 Anthropic 技能生態系

Anthropic 在 2025 年 10 月為 Claude Code 推出技能, 最初是個專案專用功能——`.claude/` 目錄下的 markdown 檔, Claude 在相關時能呼叫。格式刻意簡單: 一個含描述、觸發條件、指令的 markdown 檔。

到 2025 年 12 月, Anthropic 透過 agentskills.io 把技能作為開放標準釋出, 定義任何 agent 系統都能採納的可移植格式。規格涵蓋:

- 技能後設資料（名稱、描述、版本、作者）
- 觸發定義（關鍵字匹配、意圖分類器、regex pattern）
- 內容結構（指令、例子、工具配置）
- 依賴宣告（這個技能建立在其他哪些技能之上）

生態系反應迅速。到 2026 年初, 官方倉庫累積超過 87,000 GitHub stars, 社群貢獻的技能超過 700,000。awesome-llm-skills、awesome-agent-skills（含來自官方平臺團隊的 1,000+ 技能）、awesome-claude-code 等收整合為主要發現頻道。

這種成長創造了技能本來要解決的問題: 太多能力爭搶有限 context 空間。

## 5.3 擴充套件問題

OpenAI 的 agent 文件含一個實務指引: **保持 agent 在 20 個工具以下, 預期超過 10 個會準確度退化**。跨多個模型家族的實證測試確認這個閾值。每個額外工具定義都加 token 到 context, 加決策分支到模型選擇空間。在 90 個工具時, schema 開銷本身就可能超過 50,000 token——在任何對話、記憶、檢索檔案進入視窗之前。

退化不只是 token 數。是關於決策複雜度。當模型必須在 90 個工具間選, 機率質量分薄。模型把更多推理容量花在工具選擇上, 較少在任務執行上。工具引數構造的錯誤率上升。模型開始更頻繁選「合理但錯」的工具。

技能面對同樣的擴充套件壓力。一個有 500 個可用技能的系統不能把全部 500 個描述都載入到 context。即使只載入 500 個技能的觸發描述, 也可能消耗數千 token, 退化模型處理實際請求的能力。

解法是漸進式揭露。

## 5.4 漸進式揭露架構

漸進式揭露是個多層資訊架構, 每一層為下一個路由決策提供剛好夠的細節:

**第 0 層: 路由索引。** 一個把類別對映到技能群組的精簡表。整個技能庫可能總共消耗 200-500 token。這是靜態時坐在系統 prompt 裡的東西。

**第 1 層: 類別描述。** 當路由索引識別相關類別, 載入該類別中技能的一段描述。每個描述為掃讀最佳化——足以判斷相關性, 不足以執行。

**第 2 層: 技能連結與依賴。** 對選中的技能, 載入它的依賴圖——它需要哪些其他技能或工具、它預期什麼 context。

**第 3 層: 段落與摘要。** 載入技能的結構大綱——段落標題、關鍵決策點、引數清單——不含完整指令內容。

**第 4 層: 完整內容。** 把完整技能指令載入到 context window。這隻對實際被呼叫的一兩個技能發生。

由 Heinrich 與 arscontexta 團隊正式化的關鍵洞察是: **大多數決策在讀到任一完整檔案之前就發生**。路由索引消除 95% 技能。類別描述消除大多數剩餘。完整內容載入是例外, 不是規則。

跨生產系統衡量, 漸進式揭露相對於前置載入所有技能定義, 把 token 開銷減少 **85-95%**。Anthropic 自家 agent skills 實現示範這一點: 17 個生產技能在靜態時消耗約 1,700 token（第 0 層 + 第 1 層）, 僅在呼叫時展開到完整內容。

## 5.5 技能圖

Heinrich 的 Skill Graph 架構（arscontexta, 2025-2026）把漸進式揭露延伸到網路結構。不是按類別組織的扁平技能清單, 技能圖是 **由 wikilink 連結的互聯 markdown 檔網路**, 每個節點帶:

- 含簡潔描述的 YAML frontmatter 區塊（用於第 1 層掃讀）
- 指向相關技能、前置技能、子技能的 wikilink
- 能獨立載入的結構化段落

圖結構啟用扁平技能清單不能支援的幾個能力:

**情境式導航。** 當一個技能被呼叫, 它連結的技能成為共載候選。一個「deploy」技能連結到「test」、「rollback」、「monitor」技能——不是因為它們在同一類別, 而是因為它們在運營上相鄰。

**依賴解析。** 技能能宣告前置條件。呼叫複雜技能自動拉入它依賴的基礎技能, 類似套件依賴解析。

**部分載入。** 因為技能用清晰段落結構化, 系統能載入特定段落（例如部署技能的「錯誤處理」段落）而不載入完整檔案。

圖拓撲本身變成一種知識表示。密集連線的技能群指出有高內部一致性的能力領域。孤立技能可能指出系統涵蓋的差距或整合機會。

## 5.6 SkillReducer 論文

2026 年 3 月發表的研究檢視跨多個 agent 平臺的 55,315 個技能, 產生挑戰對技能質量天真假設的發現:

- **26.4% 技能完全缺路由描述**。它們有完整指令內容但無後設資料幫路由系統識別何時呼叫。這些技能只能透過精確名字觸發——對任何智慧路由層都不可見。

- **超過 60% 技能 body 內容是非可行動的**。它包含背景 context、動機、注意事項、解釋性文字, 而非模型能執行的具體指令。這些內容消耗 token 而不貢獻任務效能。

- **壓縮過的技能比原版改善輸出質量 2.8%**。當研究者剝離非可行動內容並緊縮指令語言, 模型效能實際改善。少即是多——context 中減少的噪音讓模型聚焦於可行動指令。

技能撰寫的含義直接:

1. **每個技能都需要路由描述**。沒有它, 技能對漸進式揭露系統等於不可見。
2. **指令內容應密集且可行動**。背景 context 屬於文件, 不是被注入 context window 的技能 body。
3. **技能質量衡量應包含 token 效率**——不只「它有效嗎」而是「每消耗 token 它有效嗎」。

## 5.7 MCP 的 Meta-Tool Pattern

Model Context Protocol（MCP）引入跨供應商 agent 發現並呼叫工具的標準方式。但 MCP 原本設計在連線時載入所有可用工具 schema, 創造與技能面對的同樣擴充套件問題。

Meta-tool pattern 用兩個元件解決:

- **發現工具:** 一個接受自然語言描述、從完整登錄檔返回相關工具 schema 的單一工具。這是基線時唯一載入的工具。
- **執行工具:** 一個通用工具呼叫包裝器, 一旦工具的 schema 透過發現取得, 就能按名呼叫任何工具。

系統載入兩個工具 schema 而非數百。當模型判定需要某能力, 它呼叫發現工具, 收到相關 schema, 然後呼叫具體工具。該 pattern 用一次額外推論 round-trip 換取大量 context 節省。

這是漸進式揭露應用到工具管理: 模型拿到電話簿, 不是每個聯絡人檔案的內容。

## 5.8 撰寫指引

從 SkillReducer 發現與生產經驗, 一組技能撰寫最佳實務浮現:

- **以路由描述領頭。** YAML frontmatter 描述是檔案中最重要一行。它決定技能是否會被呼叫。為分類器寫, 不是為人類讀者寫。
- **前置可行動指令。** 技能 body 頭 200 token 應含核心行為指令。背景與 context 在後。
- **用結構化段落。** 標題、清單、清楚分隔啟用部分載入與段落級檢索。
- **明確宣告依賴。** 如果技能假設另一技能或工具可用, 在後設資料中陳述。
- **包含觸發例子。** 提供 3-5 個該啟用技能的使用者訊息例子。這些既是文件也是路由層的測試案例。
- **衡量 token 成本。** 追蹤每個技能的 token 數並設預算。如果技能超過 2,000 token, 考慮它能否被拆或壓縮。

## 5.9 行業收斂：Google Agent Skills 規格（2026 年 4 月）

整個 2025 年大部分時間, 漸進式揭露主要是 Anthropic 慣例——透過 2025 年 10 月 Claude Code 技能與 12 月 agentskills.io 開放標準正式化。在 **2026 年 4 月**, Google Developers Blog 把它自己的 **Agent Skills 規格** 正式化, 採納並延伸同一架構。規格描述漸進式揭露的三個明確層級:

- **第 1 層 —— 後設資料（每技能約 100 token）。** 含技能名稱、單行描述、觸發提示、版本的精簡描述符。每個可用技能的第 1 層後設資料坐在 agent 的基線 context 中。載入 10 個技能, 這是約 1,000 token 的恆定開銷。
- **第 2 層 —— 指令（< 5K token）。** 一個技能的完整行為指令, 在第 1 層匹配識別該技能為相關時按需載入。第 2 層內容在技能實際被選中前永不進入 context。
- **第 3 層 —— 外部資源。** 完全住在 context window 外的資產——參考檔案、資料集、工具 schema、程式碼範例——只在技能在執行時明確需要才取。

頭條效率主張: 對一個有 10 個技能的 agent, 基線 context 用量從約 **10K token**（前置載入完整技能內容）降到約 **1K token**（僅第 1 層後設資料）, **90% 減少**。第 2 層內容一次載入一個技能, 第 3 層資源只在執行中需要時載入。

兩個細節讓 Google 規格在數字之外顯著:

1. **它用通用的 `agentskills.io` 規格**。不是分叉, Google 把它的格式與 Anthropic 在 2025 年 12 月釋出的開放標準對齊。對一個規格寫的技能, 能由另一個平臺的 agent 以最少調整消費。
2. **它把漸進式揭露從慣例提升到正式系統設計 pattern**。約一年時間, 漸進式揭露被描述為「Anthropic 跟技能做的事」。隨 Google 的採納與正式化, 它變成有命名架構與可衡量目標的跨供應商行業 pattern——可比作「MVC」或「REST」如何從特定實現演化為通用 pattern。

實務效果是技能庫正變得跨供應商可移植, 「你的基線 agent context 消耗多少 token」已變成供應商競爭的一等指標。

---

## 來源

- **Anthropic.** "Claude Code Skills." 文件與開放標準規格, 2025 年 10 月（推出）, 2025 年 12 月（透過 agentskills.io 的開放標準）。2026 年初 87K+ GitHub stars。
- **OpenAI.** "Agent Design Best Practices." OpenAI 文件, 2025。建議每 agent 少於 20 個工具, 超過 10 個會準確度退化。
- **Heinrich (@arscontexta).** Skill Graphs 概念與實現。X 貼（2026）: [https://x.com/arscontexta/status/2023957499183829467](https://x.com/arscontexta/status/2023957499183829467)（Skill Graphs > SKILL.md）。GitHub: [https://github.com/agenticnotetaking/arscontexta](https://github.com/agenticnotetaking/arscontexta) ——Claude Code 外掛, 生成含 wikilink 與 YAML frontmatter 掃描的個人化 markdown-graph 知識系統。次級分析: Linas Substack, "Skill Graphs: The Architecture That Solves the AI Agent Context Window Problem." [https://linas.substack.com/p/skill-graphs](https://linas.substack.com/p/skill-graphs)
- **SkillReducer Paper.** "Less Is More: Compressing Agent Skills for Improved Performance." 2026 年 3 月。分析 55,315 個技能, 26.4% 缺路由描述, 60%+ 非可行動內容, 壓縮後 2.8% 質量改善。
- **Model Context Protocol（MCP）.** Anthropic 規格, 2024-2025。標準化工具發現與呼叫協議。
- **awesome-llm-skills.** GitHub 上的社群收集。跨平臺編纂的技能庫。
- **awesome-agent-skills.** GitHub 收集, 來自官方平臺團隊的 1,000+ 技能。
- **awesome-claude-code.** GitHub 收集。Claude Code 專屬技能與配置。
- **OpenAI.** "Function Calling Best Practices." 2025。工具數量與準確度取捨的實證資料。
- **Griciūnas, Aurimas.** "State of Context Engineering in 2026." SwirlAI Newsletter, 2026 年 3 月。[https://www.newsletter.swirlai.com/p/state-of-context-engineering-in-2026](https://www.newsletter.swirlai.com/p/state-of-context-engineering-in-2026) ——漸進式揭露 / 壓縮 / 滑動視窗 pattern; meta-tool pattern。也見 "Breaking Down Context Engineering": [https://www.newsletter.swirlai.com/p/breaking-down-context-engineering](https://www.newsletter.swirlai.com/p/breaking-down-context-engineering)

---

*上一章: [第 4 章 —— Harness Engineering](04-harness-engineering.md)*

*下一章: [第 6 章 —— Agent Memory](06-agent-memory.md)*
