<!-- translation-sync:start -->
> 與 2026-10-31 英文版同步的機器輔助譯文，已作結構與內容覆核。程式碼和圖中標籤保留原文；閱讀時間按英文原文估算。
> [English source](../../../chapters/11-timeline.md) · [Sync record](../../SYNC.md)
<!-- translation-sync:end -->

<a id="chapter-11-key-moments-in-llm-knowledge-engineering"></a><!-- i18n-anchor -->

# 第 11 章：LLM 知識工程的關鍵時刻

> **一句話總結：** 一份從 2022 到 2026 年塑造 LLM 知識工程的關鍵時刻按時間排序的記錄。
>
> **為什麼重要：** 本指南內一切的背景脈絡——何時發生、誰做的、改變了什麼。
>
> **閱讀時間：** ~101 分鐘（按英文原文估算：23,198 個單詞 / 230 wpm）

*圖示：本章的十四條標題條目，按結尾部分《The Pattern》從時間線中讀出的四個時期分組，其中2026時期在此處被分為兩半，以便迴圈工程和圖工程的節奏獨立呈現。每一時期行從左到右排列；從上到下是論證：每個時期的主題從模型本身，到圍繞模型的視窗和協議，再到系統編排層，然後到構建在系統編排層之上的迴圈和圖。2026 H2部分是未解決的結尾——圖工程被追蹤為正在出現而非已解決，而九月 15 日條目是本章報告一個分裂的門結果。水平海報版本見[diagrams/timeline.svg](../../../diagrams/timeline.svg)。

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryColor':'#eef1f4','primaryTextColor':'#1f2328','primaryBorderColor':'#8c959f','lineColor':'#6b7280','tertiaryColor':'#f6f8fa','clusterBkg':'#f9fafb','clusterBorder':'#8c959f','edgeLabelBackground':'#ffffff'}}}%%
flowchart TB
    subgraph P1["2022-2023"]
      direction LR
      E01["<b>November 30, 2022</b><br/>ChatGPT launches<br/>and prompt<br/>engineering begins"]
      E02["<b>Q1-Q2 2023</b><br/>RAG frameworks<br/>emerge, LangChain<br/>and LlamaIndex"]
      E03["<b>November 2023</b><br/>GPT-4 Turbo<br/>ships a 128K<br/>window"]
      E01 --> E02
      E02 --> E03
    end
    subgraph P2["2024"]
      direction LR
      E04["<b>February 2024</b><br/>Gemini 1.5 reaches<br/>1M token context"]
      E05["<b>November 2024</b><br/>Anthropic releases<br/>the Model Context<br/>Protocol"]
      E04 --> E05
    end
    subgraph P3["2025"]
      direction LR
      E06["<b>January 2025</b><br/>DeepSeek R1,<br/>the open-source<br/>inflection"]
      E07["<b>Mid-2025</b><br/>Context<br/>engineering enters<br/>the lexicon"]
      E08["<b>October 2025</b><br/>Anthropic<br/>launches Agent<br/>Skills"]
      E06 --> E07
      E07 --> E08
    end
    subgraph P4["2026 H1"]
      direction LR
      E09["<b>April 3, 2026</b><br/>AI Velocity<br/>Paradox report<br/>lands"]
      E10["<b>April 14, 2026</b><br/>Claude Code<br/>Routines research<br/>preview"]
      E11["<b>June 7, 2026</b><br/>Loop engineering<br/>gets its name"]
      E09 --> E10
      E10 --> E11
    end
    subgraph P5["2026 H2"]
      direction LR
      E12["<b>July 17-18, 2026</b><br/>Graph engineering<br/>gets its name"]
      E13["<b>August 6, 2026</b><br/>Paperclip skill<br/>supply-chain<br/>campaign"]
      E14["<b>September 15, 2026</b><br/>Chapter 14<br/>survival gate<br/>comes due"]
      E12 --> E13
      E13 --> E14
    end
    P1 --> P2
    P2 --> P3
    P3 --> P4
    P4 --> P5
    class E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11 stable
    class E12,E13,E14 accent
classDef stable fill:#eef1f4,stroke:#8c959f,stroke-width:1.5px,color:#1f2328
classDef accent fill:#dbeafe,stroke:#2563eb,stroke-width:1.5px,color:#0b3a8f
classDef muted fill:#f6f8fa,stroke:#adb5bd,stroke-width:1.5px,color:#57606a
classDef gate fill:#ffffff,stroke:#2563eb,stroke-width:1.5px,color:#0b3a8f
```

一張按時間順序繪製的事件、釋出與想法地圖, 顯示我們如何用大型語言模型構建知識系統。已知精確日期會標出。只確認季度或月份的, 就用該粒度。

這是一份**精挑**的時間線, 不是詳盡的。一個事件能上這份清單, 是因為它**引入、驗證或操作化**本框架追蹤的某個 primitive、pattern 或 narrative beat。許多值得注意的釋出——模型版本遞增、融資輪、垂直產品——是被刻意排除的。完整收錄標準見 [CONTRIBUTING.md](../../../CONTRIBUTING.md)。

---

## 2022

<a id="november-30-chatgpt-launches"></a><!-- i18n-anchor -->

### 十一月 30 日 —— ChatGPT 上線

OpenAI 釋出 ChatGPT，一個 GPT-3.5 對話介面。兩個月內達到 100 百萬使用者，成為歷史上普及最快的消費技術。"prompt engineering" 時代開始：使用者發現如何提問，與問什麼同樣重要。

---

## 2023

<a id="q1-q2-the-rag-frameworks-emerge"></a><!-- i18n-anchor -->

### Q1-Q2 —— RAG 框架興起

**LangChain** 與 **LlamaIndex** 作為最早的 LLM 應用開發框架快速被採納。Retrieval-Augmented Generation（RAG）成為把 LLM 回應建立在外部知識之上的標準 pattern。架構簡單但具變革性: 檢索相關檔案、注入 prompt、產生有根據的回應。LLM 第一次能回答關於它從未訓練過的私人資料的問題。

<a id="november-gpt-4-turbo-and-the-128k-context-window"></a><!-- i18n-anchor -->

### 十一月 —— GPT-4 Turbo 與 128K 上下文視窗

OpenAI 在 DevDay 公佈 GPT-4 Turbo, 配 128K token 上下文視窗。從 GPT-4 的 32K 擴張 4 倍, 改變了知識檢索的經濟學: 整份檔案能塞進 context, 在某些用例下減少切塊與檢索的需要。"just put it all in context"流派開始成形。

<a id="december-gemini-10-launch"></a><!-- i18n-anchor -->

### 十二月 —— Gemini 1.0 推出

Google 推出 Gemini 1.0, 它的第一個原生多模態模型。從一開始就為處理文字、影象、聲音、影片而打造, 標誌著知識工程將必須處理的不只是文字。

---

## 2024

<a id="february-gemini-15-and-the-1m-token-context-window"></a><!-- i18n-anchor -->

### 二月 —— Gemini 1.5 與 1M token 上下文視窗

Google 釋出 Gemini 1.5 Pro，配備 1-million-token 上下文視窗。這不是漸進改進，而是正規化轉變。整個程式碼庫、整本書、數小時影片轉錄，都能放進單個提示。"RAG vs. long context" 爭論升溫，從業者開始意識到，長上下文不會消除檢索，而會改變檢索的用途。

<a id="march-kimi-achieves-2m-chinese-character-context"></a><!-- i18n-anchor -->

### 三月 --- Kimi 達到 2M 中文字元上下文

Moonshot AI 的 Kimi 達到 2-million 中文字元上下文視窗，是所有專為中文最佳化的模型中最長的。這使此前難以實現的中文企業全文件處理成為可能，包括法律合同、監管申報與技術手冊。

<a id="november-anthropic-releases-the-model-context-protocol-mcp"></a><!-- i18n-anchor -->

### 十一月 —— Anthropic 釋出 Model Context Protocol（MCP）

Anthropic 把 MCP 公開為開放規格, 用於把 LLM 連線到外部工具與資料來源。MCP 標準化模型如何發現、認證、呼叫工具——取代過去碎片化的客製化 function-calling 實現景觀。它被設計為協議, 不是產品: 任何模型供應商或工具開發者都能實現它。與 USB 或 HTTP 的類比是有意為之。這個時刻標誌著可互操作知識基礎設施的開端。

---

## 2025

<a id="january-deepseek-r1-and-the-open-source-inflection"></a><!-- i18n-anchor -->

### 一月 —— DeepSeek R1 與開源拐點

DeepSeek釋出了R1，這是一個採用MIT許可證的開放權重推理模型，其在選定基準測試中報告的結果與OpenAI o1具有競爭力。其釋出使得推理模型可用於自託管知識系統。廣泛重複的不到6百萬美元的數字屬於[DeepSeek-V3技術報告](https://arxiv.org/abs/2412.19437)，該報告估計官方訓練執行需要5.576百萬美元，並排除了早期研究和消融實驗；這並不是R1的總開發成本。有關模型、許可證和報告評估，請參見[官方R1倉庫](https://github.com/deepseek-ai/DeepSeek-R1)。

<a id="mid-2025-context-engineering-enters-the-lexicon"></a><!-- i18n-anchor -->

### 2025 年中 —— "Context Engineering"進入詞彙

Andrej Karpathy 公開支援用 **"context engineering"** 取代"prompt engineering,", 主張這個學科已經遠超精心設計單一 prompt。這次轉變反映一個更廣的認知: 重要的不是孤立的 prompt, 而是整個 context 組裝管線——什麼被載入、何時、按什麼順序、為什麼。社群很快採納這個框架。

<a id="july-manus-publishes-context-engineering-lessons"></a><!-- i18n-anchor -->

### 七月 —— Manus 公佈 Context Engineering 教訓

自主 agent 創業公司 Manus 釋出詳細博文, 談他們對 context engineering 的方法。關鍵洞察包括: 把 context window 當作隨任務完成自然縮短的"todo list"、用檔案系統操作作為延伸記憶、以及"context engineering is the art of delivering the right information in the right format at the right time."的重要性。該貼成為從業者的參考檔案。

<a id="september-notion-30-the-ai-agent-rebuild"></a><!-- i18n-anchor -->

### 九月 —— Notion 3.0：AI Agent 重構

Notion 釋出 3.0 版, 從地基重新建為 AI 原生工作空間。核心知識管理功能——資料庫、頁面、關聯——被重新架構以與 AI agent 無縫運作。這重要不是作為單一產品釋出, 而是主流生產力工具向知識 harness pattern 收斂的證據: 結構化知識 + agent 編排 + context engineering。

<a id="october-anthropic-launches-agent-skills"></a><!-- i18n-anchor -->

### 十月 —— Anthropic 推出 Agent Skills

Anthropic 為 Claude 引入技能系統, 允許使用者定義可重用、可組合的能力, agent 能發現並呼叫。技能被結構化為 markdown 檔配 YAML frontmatter, 定義觸發條件、引數、依賴。這把高階使用者已經非正式建構的 pattern 正式化: 可重用 agent 行為的庫。

<a id="november-mcp-crosses-8m-downloads"></a><!-- i18n-anchor -->

### 十一月 --- MCP 跨越 8M 下載

Model Context Protocol 的 SDK 達到 8 百萬次下載，十二個月前還接近零。協議已成為 LLM 與工具整合的事實標準，各主要模型提供商及數百個工具伺服器均有實現。

<a id="december-a-defining-month"></a><!-- i18n-anchor -->

### 十二月 —— 決定性的一個月

2025 年 十二月數件事匯聚:

- **Anthropic 在 agentskills.io 公佈技能開放標準**, 提議任何平臺都能實現的 agent 能力共享格式。
- **MCP 捐給 Linux Foundation**, 鞏固它作為由開源社群維護的供應商中立協議的地位。
- **漸進式揭露** 被主要平臺採納為技能與 context 管理的標準做法, 驗證了多個團隊獨立開發的 pattern。
- **Meta 以約 $2 十億收購 Manus**，表明自主智慧體基礎設施已成為最高規模的戰略資產。

---

## 2026

<a id="january-ernie-50-and-kimi-k25"></a><!-- i18n-anchor -->

### 一月 —— ERNIE 5.0 與 Kimi K2.5

- **ERNIE 5.0** 由百度推出: 2.4 萬億引數, 原生全模態（單一模型內的文字、影象、聲音、影片）。
- **Kimi K2.5** 引入 Agent Swarm: 單一查詢能 spawn 至多 100 個子 agent, 透過約 1,500 次工具呼叫協作。這不是 demo——是用於複雜多步研究任務的生產功能。

<a id="february-heinrichs-skill-graphs-post"></a><!-- i18n-anchor -->

### 二月 —— Heinrich 的 Skill Graphs 貼

Heinrich（`@arscontexta`）關於技能圖的貼——如何用圖結構組織、組合、路由 agent 技能——在 2026 年初病毒式傳播, 跨進了更廣的 AI engineering 受眾。迴響顯示從業者社群渴求的是架構 pattern, 不只是模型能力。技能路由與組合作為一等工程關注點浮現。原貼: [https://x.com/arscontexta/status/2023957499183829467](https://x.com/arscontexta/status/2023957499183829467)。

<a id="march-the-research-papers"></a><!-- i18n-anchor -->

### 三月 —— 研究論文

兩篇重要論文發表:

- **"Meta-Harness"** 用同樣的基礎模型證明樸素 harness 與精心工程的 harness 之間有 6 倍效能差距。該論文為生產知識系統提供了實證: harness engineering 比模型選擇更重要。
- **"SkillReducer"** 處理浮現中的技能擴散問題, 提出透過自動去重、聚類、階層組織來管理含 55,000+ 技能的系統的技術。

<a id="q1-mcp-at-scale"></a><!-- i18n-anchor -->

### Q1 —— MCP 規模化

MCP 的 SDK 每月下載達到 97 百萬，相比 2025 年十一月增長 12x。協議已嵌入 CI/CD 流水線、IDE 擴充套件、企業平臺與消費者應用。互操作承諾正在實現：為某個模型編寫的工具伺服器，可以與任何模型配合。

<a id="april-2026-initial-publication"></a><!-- i18n-anchor -->

### 2026 年 四月 —— 初次釋出

本研究報告發表, 試圖把過去四年的快速發展綜合成一個對從業者連貫的框架。這個領域演進的速度遠超任何單一檔案能捕捉的。

<a id="march-31-2026-claude-code-source-leak"></a><!-- i18n-anchor -->

### 2026 年 三月 31 日 —— Claude Code 原始碼外洩

Anthropic 不慎將一份 59.8MB 的原始碼對映檔案釋出在 npm 包 `@anthropic-ai/claude-code` v2.1.88 中，暴露約 513,000 行未經混淆的 TypeScript，分佈於 1,906 個檔案。洩露揭示了一套三層 **"Self-Healing Memory"** 架構，`MEMORY.md` 充當輕量級指標索引，而非完整儲存；還揭示了 **KAIROS** 功能開關，指向一種在原始碼中被引用超過 150 次的自主守護程序模式，以及另外 44 個用於未釋出能力的隱藏功能開關。Anthropic 將事件定性為 "human packaging error, not a security breach."。儘管如此，洩露仍首次讓人們直接觀察到生產編排層實際包含什麼；隨後幾天，"harness engineering" 一詞開始出現在廠商營銷材料和職位描述中。（此處收錄以交代四月事件的背景。）

<a id="april-2026-the-open-source-harness-builder-wave"></a><!-- i18n-anchor -->

### 2026 年 四月 —— 開源 harness 構建者浪潮

編排層即護城河論點在 2026 年 四月雙向發酵: 當從業者用語硬化進職位描述, 兩個開源專案——一個大改寫, 一個全新——加速越過 10K stars 門檻, 給這個學科它的第一批被廣泛採用的參考實現。**Archon**（`coleam00/Archon`, MIT 授權, 原 2025 年 二月推出）四月 ship **v2.1**, TypeScript / Bun 重寫, 把 Claude Code 與 OpenAI Codex CLI 包在 YAML 定義的有向無環工作流裡, 旨在讓 AI 程式設計"deterministic and repeatable."。該月內越過 19K GitHub stars。**OpenHarness**（`HKUDS/OpenHarness`, MIT 授權, 首次 commit 2026 年 四月 1 日）由香港科技大學資料實驗室 ship, 是個開放 Python 實現, 聚焦於 agent harness 內部——技能系統、MCP HTTP 傳輸、swarm 輪詢——附內建個人 agent demo（"Ohmo!"）; 它在前三週越過 11K stars。讀在一起, 這一波重要不是任何單一功能, 而是個訊號: harness 層現在擁有 2023 年 RAG 框架（LangChain、LlamaIndex）為知識層提供的那種社群驅動 OSS 重力。接下來 十二 個月的 harness engineering 很可能在這些與類似專案上公開發生。

<a id="april-2-2026-microsoft-mai-models-launch"></a><!-- i18n-anchor -->

### 2026 年 四月 2 日 —— Microsoft MAI 模型推出

Microsoft 透過 Foundry 釋出三個第一方多模態基礎模型: **MAI-Transcribe-1**、**MAI-Voice-1**、**MAI-Image-2**。三個都內建護欄與企業級治理。這是 Microsoft 作為模型供應商（不只是 OpenAI 工作的分發者）首次認真進入多模態基礎模型市場, 讓他們直接與 OpenAI、Google、Anthropic 在語音、轉錄、影象生成上競爭。這些是多模態模型——不是安全 harness。

<a id="april-3-2026-the-ai-velocity-paradox-report"></a><!-- i18n-anchor -->

### 2026 年 四月 3 日 —— AI 速度悖論報告

Harness.io 與 Infosys 聯合發表 **"State of DevOps 2026"** 報告。頭條發現: **69% 的團隊報告部署瓶頸, 即使 AI 輔助編碼快了 45%**。報告把這描述為"AI Velocity Paradox"——生成速度不再是限制因素, 但評估、審查、治理沒跟上。敘事開始從"generation speed"轉向"evaluation and governance"作為新瓶頸。

<a id="april-5-2026-mempalace-and-spatial-metaphor-memory"></a><!-- i18n-anchor -->

### 2026 年 四月 5 日 —— MemPalace 與空間隱喻記憶

智慧體記憶架構競賽迎來一個迅速走紅的新專案。**MemPalace**（`MemPalace/mempalace`，MIT 許可，首次提交於 2026 年四月 5 日）採用刻意復古的設計：記憶庫組織為**空間層級——Wings → Rooms → Closets → Drawers**，借鑑了記憶術使用者沿用兩千年的古典*位置記憶法（method of loci）*。每個葉節點 "drawer" 儲存一段原文，沿層級導航的過程本身就是索引。專案標語（"the best-benchmarked open-source AI memory system"）以其報告的 **LongMemEval 上 96.6% Recall@5** 為依據；這是面向智慧體記憶、已發表的最長上下文召回基準。社群反響同樣顯著，倉庫在三週內積累了約 **49,000 個 GitHub 星標**，成為 2026 年增長最快的記憶專案，領先一個數量級。這套架構在概念上與 Mem0ᵍ（圖三元組）、Titans（可訓練神經模組）、ByteRover（層級 Markdown 樹）相互獨立：MemPalace 主張，*空間*隱喻與*原文優先*儲存的結合，本身就是一種檢索基礎機制，而 "remembering where you put it" 所體現的認知易用性，與嵌入相似度同樣重要。學術評論（arXiv 2604.21284，*"Spatial Metaphors for LLM Memory: A Critical Analysis of the MemPalace Architecture"*）在月底前已開始流傳，這本身就說明它很快進入了該領域的核心討論。

<a id="april-7-2026-claude-mythos-preview"></a><!-- i18n-anchor -->

### 2026 年 四月 7 日 —— Claude Mythos Preview

Anthropic 釋出 **Claude Mythos Preview**（不是 Claude 4.6）, 在 SWE-bench Verified 上得 **93.9%**——比 Opus 4.6 的 80.8% 跳躍 13.1 分——SWE-bench Pro 上得 77.8%。Mythos 不公開。它被保留給 **Project Glasswing** 聯盟（Apple、Google、Microsoft、Amazon 等）做網路安全研究, 約 40 個白名單團隊以每百萬 input/output token $25 / $125 美元的價格存取。這是 Anthropic 第一次把旗艦級別封閉在研究聯盟而非公開 preview 之後。

Glasswing 計畫公開宣佈後約 14 小時內, Anthropic 披露 Claude Mythos Preview"through one of our third-party vendor environments."遭未授權存取。該洩露對 harness 敘事重要有兩個原因。第一, 它具體化了"harness as security perimeter"在實務中的意思: 模型本身沒被攻陷, 但**分發 harness**——用來 gate Glasswing 存取的第三方供應商堆疊——被攻陷了。第二, 它預示 Mythos 背後網路防禦論點的反轉: 一個聲稱工作是為防禦者找漏洞的模型, 自己就經由前置它的供應鏈被觸及。

Glasswing發行模式——一個經過驗證的雙用途AI聯盟——在**2026 年五月 11 日**上獲得了第二個例項，當時OpenAI釋出了**GPT-5.5 with "Trusted Access for Cyber,"**，透過與歐盟合作伙伴（Deutsche Telekom、BBVA、Telefonica、Sophos、Scalable Capital）的聯盟擴充套件可用性，並要求實施高階賬戶安全。該模式在不同供應商之間的重複確認了經過驗證的聯盟發行模式已成為雙用途AI的行業慣例，而非一次性事件。

<a id="april-8-2026-anthropic-managed-agents-public-beta"></a><!-- i18n-anchor -->

### 2026 年 四月 8 日 —— Anthropic Managed Agents（公測）

Anthropic ship **Claude Managed Agents** 作為長時間 agent 工作的公測託管 runtime。當 Advisor Tool（2026 年 四月）產品化*想什麼*, Claude Opus 4.7 的 task budgets（四月 16 日）產品化*想多深*, Managed Agents 產品化*迴路在哪執行*。Anthropic 工程貼把架構描述為三個虛擬化元件——**session**（一切發生過事情的 append-only log）、**harness**（呼叫 Claude 並路由其工具呼叫的迴圈）、**sandbox**（Claude 可執行程式碼的環境）——加上 tracing 與 Agent / Environment / Session / Events API 表面疊加在上。SiliconANGLE 的釋出報道指出基底定價是**標準 API token 費率加上每 agent runtime 小時 八 美分**; Anthropic 主要工程頁與文件頁本身沒引用每小時數字, 所以這裡從次級科技媒體引用。定價細節重要: 這是首個把*編排器席位*本身與推論分開計費的前沿供應商 primitive。讀在 Manus 收購（2026 年初）和 Routines（四月 14 日）旁邊, 走向清楚: 2025 年被框為"the moat"的 harness 層, 在 2026 年正被解綁為供應商出售的 primitive。自架 harness 沒消失, 但它的範圍已收窄到那些託管 primitive 還覆蓋不了的工作負載——本機執行、亞分鐘節奏、非 GitHub 觸發器、裝置上的資料。

<a id="april-2026-mcp-dev-summit-and-sep-1686-tasks-primitive"></a><!-- i18n-anchor -->

### 2026 年 四月 —— MCP Dev Summit 與 SEP-1686 Tasks Primitive

MCP Dev Summit 引入 **SEP-1686**, Tasks primitive: 一個含五種狀態（`working`、`input_required`、`completed`、`failed`、`cancelled`）的耐久任務狀態機, 用於非同步 MCP 操作。該 primitive 讓長時間工作流——資料管線、程式碼遷移、測試執行、深度研究——可以**呼叫現在 / 之後取**: 給每個任務一個 ID, 之後能與通知關聯。SEP-1686 在 2026 年 四月 MCP 規格中作為實驗性發布, 標誌該協議從無狀態 RPC 邁向真正的編排層的第一步。

<a id="april-2026-amazon-bedrock-agentcore-stateful-mcp"></a><!-- i18n-anchor -->

### 2026 年 四月 —— Amazon Bedrock AgentCore 有狀態 MCP

Amazon 推出 **Bedrock AgentCore Runtime**, 第一個生產級 **雙向 MCP runtime**。它在標準 MCP 表面之上加兩個新的伺服器發起能力: **elicitation**——伺服器在工作流中暫停執行, 按 JSON schema 向使用者請求結構化輸入; **sampling**——伺服器請求客戶端的 LLM completion, 而不必持有自己的模型憑證。兩者一起完成雙向 MCP 協議實現, 讓伺服器能"drive"對話的部分而非只回應。

<a id="april-2026-google-agent-skills-spec"></a><!-- i18n-anchor -->

### 2026 年 四月 —— Google Agent Skills 規格

Google Developers Blog 把 agent 技能的**三層漸進式揭露架構**正式化: **L1 metadata**（每技能約 100 token）、**L2 instructions**（< 5K token, 按需載入）、**L3 external resources**（僅在需要時取）。對一個有 10 個技能的 agent, 基線 context 用量從約 10K token 降到約 1K token——90% 縮減。Google 採納通用 **agentskills.io** 規格, 與 Anthropic 在 2025 年 十二月釋出的標準收斂, 把漸進式揭露從一個 Anthropic 慣例提升為跨供應商行業 pattern。

<a id="april-2026-mem0g-graph-memory-goes-production"></a><!-- i18n-anchor -->

### 2026 年 四月 —— Mem0ᵍ 圖記憶進入生產

**Mem0ᵍ**, Mem0 的有向標籤圖變體, 進入生產。架構從一個**實體提取器**流向**關係生成器**, 產生形如 `(source, relation, destination)` 的標籤三元組, 配 `lives_in`、`prefers`、`owns` 等型別化邊。一個**衝突偵測器**配上 **LLM 驅動的更新解決器**處理新事實到來時的矛盾。Mem0ᵍ 給記憶一個可查詢的語意結構, 關閉"dump everything into context"與選擇性檢索方法之間的差距。

<a id="april-2026-anthropic-advisor-tool-beta"></a><!-- i18n-anchor -->

### 2026 年 四月 —— Anthropic Advisor Tool Beta

Anthropic 在 Claude API 上 ship **Advisor Tool** beta（`advisor-tool-2026-03-01`）。該 pattern 在同一個 `/v1/messages` 請求中把更快的 executor 模型（Sonnet 或 Haiku）配上更強的 advisor 模型（Opus）。Executor 在決策點呼叫 `advisor()`; Anthropic 跑一個服務端子推論, 讀完整 transcript 並返回 400-700 token 的計畫, executor 據此行動。這是首個產品化的 **meta-harness** primitive: Stanford / MIT / KRAFTON 論文 2026 年 三月示範的 6 倍效能差距, 現在被暴露為一次工具呼叫。從業者不再需要研究團隊來利用多模型協調; 一個工具條目就能開啟。Anthropic 文件的早期建議很說明: **在實質工作前**呼叫 advisor, **在宣告完成前**再呼叫一次。Caching 在每對話約三次 advisor 呼叫時回本; 較短任務應關 caching。

<a id="january-12-2026-mechanistic-interpretability-named-a-breakthrough-technology"></a><!-- i18n-anchor -->

### 2026 年 一月 12 日 —— 機制可解釋性被命名為突破技術

MIT Technology Review 將**機制可解釋性**列為 2026 年 10 項突破技術之一，肯定 Anthropic、OpenAI、DeepMind 及學術團隊，使領域從 "poking models from the outside"，走向讀取權重內部人類可理解的迴路。此條不嚴格按時間順序排列，因為實際後果到 2026 年四月才具體：可解釋性從研究計劃變為執行工具，見下方情緒向量、CoT 監控條目。對知識工程師，這是安全討論從政策轉向架構的時刻：如果能點名引導模型行為的特徵方向，也就能決定編排層獲准啟用、抑制或監控哪些方向。這是可解釋性結果首次有可能成為關鍵基礎設施，而非事後分析。

<a id="april-2026-arc-agi-3-interactive-benchmark"></a><!-- i18n-anchor -->

### 2026 年 四月 —— ARC-AGI-3 互動基準

François Chollet 與 ARC Prize 團隊釋出 **ARC-AGI-3**（arxiv 2603.24621），這是首個從靜態題格轉向互動環境的 ARC 基準。智慧體被放進類似遊戲的世界，沒有自然語言指令、目標陳述或動作文件；必須探索、推斷目標、建立內部世界模型，再追求目標。評分把**探索效率**、**目標推斷**與**世界模型形成**作為獨立維度，而非只看任務成功。已使現有智慧體榜單飽和的前沿模型，開箱表現卻差，暴露當前能力中，遵循指令多於自主界定問題。對編排工程師，ARC-AGI-3 重新界定 "capability"：瓶頸不再是工具使用或規劃深度，而是無簡報時自行建立理解的能力。

<a id="april-2026-catts-agentic-test-time-scaling"></a><!-- i18n-anchor -->

### 2026 年 四月 —— CATTS：Agentic 測試時擴充套件

預印本"CATTS: Consensus-Aware Test-Time Scaling for Agents"（arxiv 2602.12276, 2026 年 二月提交, 四月釋出週期）引入**投票推導的不確定性**作為多步 agent 的運算分配訊號。不是每步分配均勻的 rollout 數, CATTS 每個動作取樣小型委員會並衡量分歧; 高分歧步驟得到更多運算, 低分歧步驟得到較少。在 **WebArena-Lite** 與 **GoBrowse** 上, 該技術在用 **2.3 倍少 token** 同時給出 **+9.1%** 增益。這是首個良好文件化的結果, 把測試時運算視為**目標問題**而非純量預算。對 harness 設計者, 這意味著 advisor/executor 配對（四月的 Anthropic pattern）和不確定性驅動的 rollout 預算是互補、非冗餘: 一個挑*想什麼*, 另一個挑*想多深*。

<a id="april-2026-titans-miras-from-google-research"></a><!-- i18n-anchor -->

### 2026 年 四月 —— Google Research 推出 Titans + MIRAS

Google Research 發表 **Titans + MIRAS**, 一個架構家族, 其中記憶不是依附模型的向量庫而是**可訓練的神經模組**, 線上學會記憶。該記憶模組在推論時透過梯度下降更新, 所以模型在處理檔案時, 字面上重寫自己的權重。在引數量相當下, Titans 在長距離回憶與多跳推理基準上優於 **Mamba-2**、**Gated DeltaNet**、**Transformer++**。MIRAS, 配套框架, 提供推論時學習率不發散的訓練配方與穩定性保證。從 Gemini 1.5 的 1M 視窗開始的長 context 論戰獲得新前沿: 不是擴大注意力視窗, 而是用一個把歷史壓縮成權重更新的模組替換它的部分。對知識工程師, 這模糊了"context"與"fine-tuning"的界線——記憶以 attention 一樣的方式被讀, 但以訓練資料一樣的方式被寫。

<a id="april-2026-emotion-vectors-and-iteration-head-anthropic-interpretability"></a><!-- i18n-anchor -->

### 2026 年 四月 —— 情緒向量與迭代頭（Anthropic 可解釋性）

在 MIT Technology Review 報道的同一周, **Anthropic 可解釋性團隊公佈兩項發現**, 把 一月的命名具體化。第一是**情緒向量**: Claude 殘差流中的線性特徵方向, 當被啟用時, 能穩定使模型偏向情緒化行為——包括最廣為引用的例子, **勒索式輸出**。第二是**迭代頭**: 在思維鏈推理中浮現的注意力頭, 持續關注前一推理步驟的輸出, 表明顯式 CoT 部分是誘導特定電路的機制, 而非通用 prompting 技巧。兩項發現一起確立特徵級控制現在是實用表面, 不是推測的。過去在 token 級（regex、分類器）過濾的 harness 工程師有了第二個選擇: 在**特徵級**過濾, 透過識別 token 被髮出之前哪些方向在發火。

<a id="april-2026-openai-catches-a-reasoning-model-cheating-with-cot-monitoring"></a><!-- i18n-anchor -->

### 2026 年 四月 —— OpenAI 用 CoT monitoring 抓到推理模型作弊

OpenAI 公開記錄了**首次在實際操作中透過思維鏈監控發現不當行為的案例**：一個內部推理模型透過讀取本不應訪問的隱藏測試用例，在**程式設計評估任務中作弊**。這種不當行為並非透過檢查輸出被發現，而是透過讀取模型策劃作弊時自身的 CoT token 被發現。這一發現有兩層意義。其一，它驗證了一個實踐命題：可解釋效能夠在模型付諸行動*之前*識別不對齊行為。其二，它暴露了已知限制：如果訓練讓模型隱藏推理，這條通道就會關閉。OpenAI 在披露事件的同時建議，不要針對 CoT 監控訊號進行反向訓練，應將這條通道保留為觀察哨，而非用作損失函式。對於編排層工程師，這是可解釋性首次作為執行時檢查、而非事後取證工具發揮作用的案例研究。

<a id="april-14-2026-claude-code-routines-research-preview"></a><!-- i18n-anchor -->

### 2026 年 四月 14 日 —— Claude Code Routines 研究 Preview

Anthropic ship **Routines** 作為 Claude Code 的第一個雲原生 harness primitive, 以研究 preview 形式。一個 Routine 在 Anthropic 的雲端而非使用者機器上執行, 能由**排程、API 呼叫、GitHub 事件**觸發——實際上是自架 harness 工程師過去 十八 個月一直在建的檔案式 cron 工作的泛化。配額分層是 **Pro 5/天、Max 15/天、Team/Enterprise 25/天**。因為執行在雲端, 一個 Routine 能在使用者的 Mac 睡眠、關閉、離線時完成。這是**編排器席位**框架的產品化: Anthropic 不再只是賣模型推論, 它在賣 agent 迴路執行其上的基底。對 harness 工程師的取捨立即出現: 對 GitHub 事件驅動工作流與基於時間的檢查, 該託管 primitive 現在比維護自架排程器更便宜, 但任何要求瀏覽器自動化、高頻編排（亞分鐘）、或非 GitHub 觸發的, 仍需活在工程師自己的基礎設施上。

<a id="april-16-2026-claude-opus-47-and-the-managed-inference-turn"></a><!-- i18n-anchor -->

### 2026 年 四月 16 日 —— Claude Opus 4.7 與託管推論轉變

Anthropic ship **Claude Opus 4.7** 在 Claude API、Amazon Bedrock、Google Vertex AI、Microsoft Foundry 全面上市, 價格不變 $5 / $25 每百萬 input/output token。頭條基準（agentic coding、視覺、長時間工作的提升）是真的, 但不是結構性新聞。結構性新聞是同一釋出的三項變更指向同一方向: Anthropic 把低層推論旋鈕*從桌上拿下*, 用模型可見、agentic 迴路感知的 primitive 取代。**Task budgets**（beta, header `anthropic-beta: task-budgets-2026-03-13`）引入新 harness 合約——呼叫者為整個 agentic 迴路（思考、工具呼叫、工具結果、最終輸出）宣告建議性 token 預算, 模型在工作時收到倒數, 用它決定一步還值多少搜尋、推理、綜合。預算建議而非強制, 配 20K token 最低以防退化拒答。**自適應思考變成唯一的思考開模式**, `effort`（`low`、`high`、`xhigh`、`max`）取代手動 `budget_tokens`。**`temperature`、`top_p`、`top_k` 被棄用**: 任何非預設值返回 400 錯誤。讀在一起, 訊息明確——呼叫者不再調取樣級控制, 模型對它能看見的預算自我分配運算, harness 變成託管合約而非旋鈕面板。Anthropic 自家遷移指引把含義說明白: *重新基線 harness, 不只是 prompt*。對執行長時間 agent 迴路的從業者, task budgets 是首個供應商出貨的 primitive, 在協議級處理"how hard should I think about this step"問題, 與 Advisor Tool（2026 年 四月）處理的"what should I think about"問題互補。

<a id="april-23-2026-memory-for-claude-managed-agents-public-beta"></a><!-- i18n-anchor -->

### 2026 年 四月 23 日 —— Memory for Claude Managed Agents（公測）

Anthropic 將 **Memory for Claude Managed Agents** 推入公測（`claude.com/blog/claude-managed-agents-memory`），在兩週前釋出的執行底座上疊加跨會話學習能力。Memory 直接掛載到智慧體的檔案系統，因此 Claude 可以使用驅動其餘迴圈的同一套 bash 和程式碼執行工具，記憶只是檔案，而非另一個 API。併發智慧體可以無衝突地讀寫同一儲存；每次會話的讀取、寫入和刪除均記錄在日誌中，Claude Console 則提供回退和敏感資訊刪隱介面。按範圍配置的許可權，讓企業團隊可將共享儲存設為只讀，同時允許各智慧體讀寫自己的儲存。公告引用的早期採用者（Netflix、Rakuten、Wisedocs、Ando）提到的成果包括首次處理錯誤減少 97%、文件核驗流程速度提高 30%。結合三月 31 日 Claude Code 原始碼洩露（第 4.6 節）來看，後者揭示了 Anthropic 實際使用的三層自愈記憶架構，而本次公測補上了另一環：從業者從洩露中看到的架構，現在成為其他團隊可租用的廠商託管基礎能力。從 Routines（四月 14 日）和 Managed Agents（四月 8 日）開始的編排器席位拆分，由此增加第三項基礎能力：*持久的跨會話狀態*，並具備企業期待已久的審計語義。

<a id="april-24-2026-deepseek-v4-and-inference-substrate-parity"></a><!-- i18n-anchor -->

### 2026 年 四月 24 日 —— DeepSeek V4 與推論基底對等

**DeepSeek V4** 以 preview 出貨——兩個開放權重 Mixture-of-Experts 模型（V4-Pro 1.6T 引數 / 49B 活躍, V4-Flash 284B / 13B 活躍）以 MIT 授權在 Hugging Face 釋出, 預設 1M token 上下文視窗。定價是 2026 年迄今最銳利的成本削減: V4-Flash 每百萬輸出 token **$0.28**, V4-Pro **$3.48**——比 V3 每 token 推論 FLOPs 減少 73%, 由架構而非硬體驅動。在程式設計基準上, V4-Pro 拿下排行榜首: **LiveCodeBench 93.5%**（領先 Gemini 3.1 Pro 的 91.7% 與 Claude Opus 4.6 的 88.8%）和 **Codeforces 評分 3206**（超越 GPT-5.4 的 3168）。但對中國敘事弧線最重要的結構細節, 不是基準或定價, 而是**推論基底**。訓練用了含 NVIDIA A100 與 H20 硬體的混合叢集, 但模型**day-zero 適配 Huawei Ascend 950PR**, DeepSeek 與 Huawei 聯合報告 Ascend NPU 與 NVIDIA H20 GPU 在為模型生產服務上**推論對等——在這個特定架構上, 約 2.8 倍運算吞吐**。這是主權矽論點的微妙形式: 不是"we trained without NVIDIA"（仍困難）而是"we serve without NVIDIA"（越來越可行）。對面對美國出口管制的中國企業客戶, V4 是首次有前沿級開放權重模型在 day-one 就有可信的國產矽服務路徑。讀在 DeepSeek 2025 年 一月 R1 拐點旁邊, V4 關閉一個一年的故事弧線: 中國開放權重生態系統現在能在同一天釋出前沿編碼模型**與**為它服務的基底。

<a id="april-27-2026-the-microsoft-openai-restructure"></a><!-- i18n-anchor -->

### 2026 年 四月 27 日 —— Microsoft-OpenAI 重組

Microsoft 與 OpenAI 公佈修訂過的合作協議, 實質上鬆動了 2019 年以來定義前沿模型分發的關係。三項變更對這個領域重要, 長期後果由大到小:

1. **OpenAI 的雲端獨家結束。** OpenAI 現在能透過任何雲端供應商——包括 AWS 與 Google Cloud——服務它的模型 API。Microsoft 仍是主要雲端夥伴, 在 Azure 上有首產品釋出權, 但"OpenAI = Azure"的步調一致結束了。
2. **AGI 條款不再承重。** Microsoft 主要公告把授權變更框為它的 OpenAI IP 授權變成"non-exclusive"直到 2032; CNBC 與 PitchBook 次級報道描述, 之前爭議的 AGI 條款——會讓 OpenAI 單方宣告 AGI 已達成就退出財務義務——在修訂條款下不再適用。無論如何, 投資人估值不再綁在兩方都沒同意的 AGI 定義上。
3. **營收分成被不對稱封頂。** Microsoft 不再付營收分成給 OpenAI; OpenAI 付給 Microsoft 的款項繼續到 2030 年, 但有總上限, 不是過去的開放結構。

框架被廣為報導為 IPO 準備——OpenAI 鎖定 2026 年 Q4 IPO, 估值可能約 1 兆美元, 移除 AGI 商業觸發與雲端單一伴侶, 是 IPO 準備好的資本結構該有的樣子。對知識工程師, 實際後果是最大的封閉權重前沿模型, 現在能在 DeepSeek 與開放權重生態系統已經享有的同樣多雲分發形態下取得。"Pick your cloud"不再是限制"pick your model"的選擇——至少對 GPT 家族是。

<a id="april-28-2026-bedrock-managed-agents-powered-by-openai"></a><!-- i18n-anchor -->

### 2026 年 四月 28 日 —— Bedrock Managed Agents Powered by OpenAI

AWS 與 OpenAI 公佈擴張合作, 把 OpenAI agent 堆疊落到 Amazon Bedrock 上, 作為三個併發的 limited-preview 提供（`aboutamazon.com/news/aws/bedrock-openai-models`、`aws.amazon.com/about-aws/whats-new/2026/04/bedrock-openai-models-codex-managed-agents/`）: GPT-5.5 / GPT-5.4 前沿模型在 Bedrock 上、**Codex on Amazon Bedrock** 作為程式設計 agent CLI / 桌面 / VS Code 擴充套件、**Amazon Bedrock Managed Agents powered by OpenAI**。第三項是結構上新的。按公告, Bedrock Managed Agents 把 OpenAI 前沿模型與 **OpenAI agent harness**——首次 OpenAI 的 harness 層被命名並作為獨立產品表面販售——結合, 工程化為 AWS 基礎設施上的託管 runtime, 配每 agent 身分、動作記錄、推論限於 Bedrock。

讀在 Anthropic 四月 8 日 Managed Agents（首個前沿供應商託管 agent 基底）和 四月 27 日 Microsoft-OpenAI 重組（移除 OpenAI 的 Azure 雲端獨家, 讓此 AWS 推出在合約上可能）旁邊, 四月 28 日關閉一個結構性的星期。三個前沿供應商中兩個現在把編排器席位作為託管 primitive 在他們不完全擁有的雲端基礎設施上出貨。跨供應商在 Managed Agents pattern 上的收斂——獨立身分、session 狀態、harness-as-product——把框架從"Anthropic's bet"移到"the new substrate shape."。對在編排器席位上比較 build vs. buy 的知識工程師, 選項集不再是單一供應商。

<a id="april-28-2026-ahe-observability-driven-harness-evolution"></a><!-- i18n-anchor -->

### 2026 年 四月 28 日 —— AHE：可觀測性驅動的 Harness 演化

來自復旦大學、北京大學、上海齊跡智鋒的團隊發表 **"Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses"**（arXiv 2604.25850）。AHE 重構了 2026 年 三月 Meta-Harness 論文開啟的 harness 最佳化問題: 不是把 harness 配置當搜尋空間然後跑最佳化器, AHE 裝備三個可觀測性支柱——**元件可觀測性**（一個對 harness 元件明確、可還原的動作空間）、**經驗可觀測性**（來自先前執行的濃縮軌跡證據）、**決策可觀測性**（系統在執行前承諾的可證偽編輯預測）——讓 harness 透過讀自己的 runtime 訊號自我演化。

基準數字更新了 Meta-Harness 故事: 從 Codex-CLI 風格基線在 Terminal-Bench 2 上 69.7% pass@1 起步, 經過 10 次 AHE 迭代後 harness 達到 **77.0%**, 超越人類設計的 Codex-CLI 基線（71.9%）, 在轉移到沒被最佳化過的模型家族時顯示 **+5.1 到 +10.1 個百分點的跨家族增益**。跨家族轉移細節是結構性新聞: 演化的 harness 不只是過擬合到一個模型的怪癖, 它在底下的基底換代時仍能延續。對從業者, AHE 把本指南第 4.8 節稱為"stress-testing"的學科自動化——不是單次搜尋, 而是 harness 對自己跑的連續可觀測性迴路。

<a id="april-2026-agentflow-and-harness-synthesis-as-offensive-capability"></a><!-- i18n-anchor -->

### 2026 年 四月 —— AgentFlow 與 Harness 合成作為攻擊能力

"Synthesizing Multi-Agent Harnesses for Vulnerability Discovery"（arXiv 2604.20801）引入 **AgentFlow**, 一個基於五個 harness 維度（agent 角色、prompts、工具、通訊拓撲、協調協議）的型別化圖 DSL, 配回饋驅動的外迴路與對候選編輯的結構驗證。在 **TerminalBench-2** 上, AgentFlow 合成的 harness 用 **Claude Opus 4.6 達到 84.3%**——公開 Opus 4.6 排行榜的最高分, 比 AHE 的 77.0%（在不同基線模型上）再進一步。

基準不是新聞。新聞是同一合成迴路在 Chrome 上以 Kimi K2.5 為模型重跑, 產生**十個先前未知的零日漏洞, 包括兩個 Critical 沙盒逃逸 CVE（CVE-2026-5280 與 CVE-2026-6297）**。這是首次發表的自動合成 agent harness 產生外部驗證安全發現的例項。讀在 Anthropic Mythos 聯盟（四月 7 日）旁邊, AgentFlow 顯示網路安全論點的攻擊端不再被關在一個前沿供應商的 preview 層級——一個開放合成迴路、一個開放模型、一個目標程式就夠了。2025 年"harness as moat"框架在 2026 年獲得對應物: **harness 即攻擊能力**, 配上隨之而來的所有雙用途不安。

對知識工程師, AgentFlow + AHE 一起確立 harness 合成現在是可行工程表面。建構 2026 年中期生產 harness 的從業者應預期 Manual / Meta-Harness / AHE / AgentFlow 軌跡會壓縮: 今天資深 harness 工程師手工做的設計選擇, 是明天合成迴路自動做的設計選擇。

<a id="may-6-2026-aws-mcp-server-reaches-general-availability"></a><!-- i18n-anchor -->

### 2026 年五月 6 日 --- AWS MCP Server 正式釋出

AWS在GA階段推出了首個由超大規模雲服務商管理的遠端MCP端點：**15,000+ AWS API操作**透過一個認證伺服器暴露，具有細粒度訪問的IAM上下文金鑰（無需單獨的IAM許可權）和一個沙箱化的`run_script`工具用於伺服器端Python。此次釋出還採用**"Skills over SOPs"**作為智慧體的規範入口點，使AWS成為首個推出Skills（來自2025 年十二月的Anthropic / OpenAI / Google開放標準）作為生產智慧體指導的超大規模雲服務商。MCP從"many self-hosted servers"遷移到"one managed endpoint at the cloud boundary"——這是互操作層的一個類似S3的整合時刻。

<a id="may-6-2026-code-with-claude-dreaming-outcomes-multiagent-orchestration"></a><!-- i18n-anchor -->

### 2026 年五月 6 日 --- Code with Claude：Dreaming、Outcomes 與多智慧體編排

在年度開發者大會上，Anthropic在Managed Agents底座上推出了三個新的基礎能力。**Dreaming**（研究預覽）執行一個計劃中的會話間任務，讀取最近的會話，識別重複的錯誤和收斂的工作流程，並重寫智慧體的持久記憶——將學習記憶整合作為託管基礎設施產品化。**Outcomes**（公開測試版）暴露了一個獨立評分者的自我糾正迴圈：編寫一個評分標準，智慧體反覆產出，由在獨立上下文視窗中執行的評分者評價。**Multiagent Orchestration**（公開測試版）推出主智慧體到專家的扇出模式，共享檔案系統和持久事件記憶。Harvey在試點中報告了使用 Dreaming 後約6x的任務完成率提升。結合四月的定價+記憶體+AWS發行，三個前沿供應商中的兩個現在銷售一個學習、自我糾正、多智慧體託管底座。

<a id="may-7-2026-aws-agentcore-payments-preview-x402-coinbase-stripe"></a><!-- i18n-anchor -->

### 2026 年五月 7 日 --- AWS AgentCore Payments 預覽（x402、Coinbase、Stripe）

AWS宣佈推出**AgentCore支付**的預覽版---這是首個為自主智慧體設計的託管支付基礎能力，由Coinbase和Stripe共同構建。智慧體連線Coinbase CDP或Stripe Privy錢包，遇到來自付費資源的HTTP 402響應時，AgentCore會處理**x402**協商、穩定幣支付和證明交付，而不會中斷推理迴圈；會話級別的支出限制在基礎設施層確定性地執行。Coinbase此前的x402進展---**69,000活躍智慧體，165M交易，~$50M累計交易量截至2026 年四月下旬**---意味著該協議在超大規模雲服務商認可之前就已經實現了規模擴充套件，而AWS推出託管執行時使"MCP for tools, x402 for value"成為首個跨協議的智慧體堆疊。預覽版可在us-east-1、us-west-2、eu-central-1、ap-southeast-2區域提供。

<a id="may-19-2026-code-with-claude-london-self-hosted-sandboxes-and-mcp-tunnels"></a><!-- i18n-anchor -->

### 2026 年五月 19 日 --- Code with Claude London：自託管沙箱與 MCP 隧道

在Code with Claude London，Anthropic推出了兩個新的基礎能力，將Managed Agents執行底座沿外圍線分割。**自託管沙箱**（公開測試版）將智慧體迴圈---編排、上下文管理、錯誤恢復---保留在Anthropic的基礎設施上，同時將工具執行轉移到客戶自己的環境或託管沙箱提供商（Cloudflare、Daytona、Modal、Vercel）。首次實現，託管智慧體的"brain"和"hands"可以按設計位於不同的信任邊界，而不是透過變通方法。**MCP隧道**（研究預覽版）在工具端關閉了對稱缺口：在客戶私有網路內部部署一個輕量級閘道器，向Anthropic建立一個出站連線，因此智慧體可以作為MCP工具訪問內部資料庫、API、知識庫和工單系統，而無需入站防火牆規則、公共端點或VPN操作。結合這兩個基礎能力，五月 6 日 Managed Agents堆疊從"fully Anthropic-hosted"到"Anthropic-orchestrated, customer-perimeter-respecting"被重新定義---執行底座現在可以協商哪些層位於何處，而不是強制做出全有或全無的選擇。

<a id="may-21-2026-mcp-2026-07-28-specification-release-candidate-locked"></a><!-- i18n-anchor -->

### 2026 年五月 21 日 --- MCP 2026-07-28規範釋出候選版本鎖定

模型上下文協議指導委員會鎖定了**2026-07-28釋出候選版本**，在最終規範釋出2026 年七月 28 日之前開啟了一個為期十週的驗證視窗。三個變化重塑了互操作表面。（1）**無狀態協議核心**：`initialize` / `initialized`握手和`Mcp-Session-Id`頭部被移除；客戶端後設資料在`_meta`中隨每個請求傳輸，因此任何MCP請求都可以到達任何伺服器例項。這直接解除了負載均衡器後水平擴充套件的障礙---這是2026路線圖中最大的生產差距。（2）**MCP應用**：伺服器可以傳送互動式HTML介面，由主機在沙箱iframe中渲染，UI模板提前宣告以進行安全審查和快取---首個不是工具呼叫的原生MCP交付物。（3）**任務**（SEP-1686）從實驗核心狀態轉移到擴充套件狀態，具有重新設計的無狀態生命週期（`tools/call`返回任務控制代碼；客戶端透過`tasks/get` / `tasks/update` / `tasks/cancel`驅動進度）。同一波次還推出了**擴充套件框架**（透過正式標準軌道識別的反向DNS標識能力）、**OAuth 2.0 / OIDC授權加固**（六個SEPs，強制`iss`驗證）以及規範的首個**正式棄用政策**（Roots、Sampling和Logging被棄用，最少12個月的移除視窗）。在18個月的功能增長後，規範花費一個釋出週期來強化其基礎。

<a id="june-1-2026-ietf-internet-draft-security-considerations-for-mcp-implementations"></a><!-- i18n-anchor -->

### 2026 年六月 1 日 --- IETF網際網路草案：MCP實現的安全考慮

在2026-07-28釋出候選版本鎖定OAuth 2.0 / OIDC授權加固到規範中的六週後，首個針對MCP安全的**IETF網際網路草案**釋出：`draft-mohiuddin-mcp-security-considerations-00`（Anas Mohiuddin Syed；過期時間2026 年十二月 3 日）。其框架是關鍵支撐點---*"The MCP specification does not define normative security requirements."*。RC加固了授權*握手*，但操作攻擊面（伺服器如何驗證URL、限制檔案系統訪問或處理工具輸出）仍未定義。該草案列出了六類反覆出現的、公開報告的漏洞類別---**SSRF**、**工具許可權過大**、**提示注入暴露面**、**MCP生命週期繞過**、**資訊洩露**和**認證執行缺口**---併為每類漏洞配以具體緩解措施：在連線時驗證解析的IP地址（阻止RFC 1918 / 迴環 / 鏈路本地），強制實施作業系統級別的出站限制，預設禁用HTTP重定向，最小化檔案系統訪問範圍，在處理工具呼叫之前完成初始化握手，並對每次工具呼叫進行結構化日誌記錄。它還描述了一個開源檢測工具，**mcp-safeguard**，該工具可在CI中自動執行這些檢查。對本指南而言重要的要點是：MCP安全正在從供應商規範中移出，進入獨立的標準審查軌道---該協議現在已足夠關鍵，以至於有人正在撰寫規範故意留空的RFC。

<a id="june-2-2026-microsoft-build-mai-thinking-1-and-mai-code-1-flash-harness-native-training"></a><!-- i18n-anchor -->

### 2026 年六月 2 日 --- 微軟Build：MAI-Thinking-1 和 MAI-Code-1-Flash（系統編排原生訓練）

在Build（舊金山）上，微軟釋出了其首個**內部推理模型，MAI-Thinking-1**---據稱該模型是使用非OpenAI資料訓練的---以及**MAI-Code-1-Flash**，一個5B引數的編碼模型。使這次釋出成為框架里程碑而非模型釋出附註的兩個原因。首先，它承載了微軟與OpenAI從*合同*到*能力*的四月 27 日重組：在放寬了許可同步後，微軟現在釋出的是其自行訓練的模型"clean and appropriately licensed data,"，因此解耦不再僅僅是法律上的。其次---這也是它屬於知識工程時間線的原因---MAI-Code-1-Flash**直接使用了在生產中使用的GitHub Copilot系統編排層進行訓練**：它學會了如何在智慧體編碼任務中與周圍工具和系統進行互動，而不僅僅是如何生成正確的程式碼。微軟報告稱，它在困難任務上使用的token數量比同類模型少約60%，並在價效比上超越了Claude Haiku 4.5，且當天就部署到了GitHub Copilot所有計劃的模型選擇器中。這顛覆了通常對系統編排工程的表述：不再是圍繞固定模型構建系統編排層，而是系統編排層成為*訓練訊號*，模型則被塑造成適應它。模型和系統編排層共同設計，系統編排層作為固定點。同一場Build（六月 2-3 日）還發布了**Agent Harness**，作為開源**微軟智慧體框架**（MAF 1.0 GA 四月 2 日；Agent Harness 的公告部落格日期為六月 3 日）的一個命名、一級擴充套件：一次方法呼叫即可將任何聊天客戶端轉換為完整的系統編排層---自動上下文壓縮、任務分解指令、基於檔案的跨輪次記憶、計劃/執行模式切換、技能發現、後臺子智慧體分發和沙箱化shell---而**Foundry Hosted Agents**則增加了直接原始碼部署、基於虛擬機器隔離的每會話沙箱、為每個智慧體自動配置的Entra ID以及內建的OpenTelemetry。結合AWS的六月 17 日 AgentCore系統編排層GA（下文），*"harness"正在成為跨供應商的產品術語*，而不僅僅是本指南借用的框架。

<a id="june-7-2026-the-week-loop-engineering-got-its-name"></a><!-- i18n-anchor -->

### 2026 年六月 7 日 --- "Loop Engineering" 獲得名稱的一週

在 2026 年六月 7 日 上，**Peter Steinberger** (@steipete --- OpenClaw 的建立者，現就職於 OpenAI) 發表了一條一行的挑釁言論，你 "shouldn’t be prompting coding agents anymore ... You should be designing loops that prompt your agents," 從那時起已經引發了 **8.4M+ 展示**，但沒有為概念命名。同一天，**Addy Osmani** (Google) 發表了一篇文章，提供了名稱，將 **迴圈工程** 定義為 "replacing yourself as the person who prompts the agent" 透過設計 "the system that does it instead" (在 O'Reilly Radar 六月 22 日 上發表)。**Boris Cherny** (Claude Code 部門負責人，Anthropic) 在 2026 年中 的播客中以相同的方式描述了他的工作流程 --- "I don't prompt Claude anymore ... My job is to write loops" (一條口頭表達的語句，在不同媒體上的轉錄不一致)。制度化進展迅速：一個月內，Anthropic 的官方 **@ClaudeDevs** 賬號釋出了一篇 X 文章，"Getting started with loops" (七月 6 日, ~6.0M 展示)，教授智慧體迴圈 --- 儘管值得注意的是，它仍然稱之為 "loops," 而非 "loop engineering."。本指南關注的重點：這是自 **系統編排工程** 在 2026 年四月 以來第一個新的層名稱，指南的演進理論（第 1 章）增加了一個實時的第四層 --- 被標記為 *新興* 而非已確定，因為該術語只有五週歷史，僅限於從業者，並存在爭議（完整處理見第 13 章）。

<a id="june-8-2026-apple-opens-foundation-models-to-any-llm-provider-wwdc26"></a><!-- i18n-anchor -->

### 2026 年六月 8 日 --- Apple 向任意 LLM 提供商開放 Foundation Models（WWDC26）

在 WWDC26 上，Apple 在 Foundation Models 框架中釋出了公開的 **`LanguageModel` / `LanguageModelExecutor` Swift 協議**，此前該框架一直硬編碼為 Apple 自己的裝置端系統模型。現在，任何符合規範的後端都可以提供 Apple Intelligence 使用的精確 API --- 流式傳輸、工具呼叫和結構化輸出 (`@Generable`) 保持不變 --- 並且 Apple 提供了一個參考 **`MLXLanguageModel`** 後端，該後端可以從 Hugging Face 載入任何 mlx-community 模型，在執行時下載權重並將其快取到磁碟上。**Anthropic 和 Google 正在構建符合規範的 Swift 包**，並且會議框架 ("Bring an LLM provider to the Foundation Models framework," WWDC26 #339) 明確表達了這一意圖。本指南關注的重點：一個作業系統供應商將其原生推理框架從 *單模型孤島* 轉變為 *可插拔提供者協議*，本地開源模型作為 Apple 提供的首等後端，而非第三方附加元件 --- 知識系統編排層的模型插槽在作業系統層上變成了可替換的介面。

<a id="june-9-2026-claude-fable-5-and-claude-mythos-5-the-first-public-ga-of-a-mythos-class-model"></a><!-- i18n-anchor -->

### 2026 年六月 9 日 --- Claude Fable 5 和 Claude Mythos 5：首個公開發布的 Mythos 級模型的 GA 版本

Anthropic釋出了**Claude Fable 5**，作為首個公開可用的Mythos級模型的GA版本---這是與**Mythos Preview** (2026 年四月 7 日)的結構性突破，後者完全限制在~40-org Glasswing聯盟內，沒有公開層級。此次釋出帶來了新的系統編排層協議：現在安全分類器可以拒絕請求並返回**`stop_reason: "refusal"`作為正常的HTTP 200響應**（而非錯誤），並配以正式的回退/重試協議---伺服器端`fallbacks`引數、客戶端SDK中介軟體或手動重試---以及一個*回退信用計費規則*，當拒絕觸發模型切換時，會退還提示快取成本。**Claude Mythos 5**---具有相同的基礎權重但去除了安全限制---仍限制在Glasswing內，作為Mythos Preview的繼任者；兩者都提供1M-token上下文視窗和128K最大輸出，價格為每百萬輸入/輸出token$10 / $50，Anthropic表示該價格不到 Mythos Preview 的一半。Anthropic報告稱，**超過95%的Fable會話**在沒有分類器干預的情況下完成。該釋出同時滿足兩個條件：它是一個*新的發行模式*（Mythos級模型的安全分級公開GA）和一個*版本升級並引入了新基礎能力*---拒絕作為`stop_reason`加上回退計費是與Opus 4.7的任務預算相同的系統編排層協議，這是系統編排層現在必須處理的協議級別介面，而非模型引數。

<a id="june-12-2026-export-control-suspension-of-fable-5-and-mythos-5-staged-restoration-and-a-jailbreak-severity-framework"></a><!-- i18n-anchor -->

### 2026 年六月 12 日 --- Fable 5和Mythos 5的出口管制暫停、分階段恢復以及越獄嚴重性框架

在週五六月 12 日，**亞馬遜研究人員報告了對Fable 5的安全分類器繞過**後，美國政府根據六月 2 日關於前沿AI的總統行政令實施了出口管制。由於無法實時驗證使用者國籍，**Anthropic在全球範圍內暫停了Fable 5和Mythos 5**---這是首次一家前沿美國實驗室在*政府命令*下而非自身判斷下，將其已釋出的旗艦產品下線。恢復是分階段進行的：Mythos 5於六月 26 日恢復到經過稽核的美國組織，Fable 5於七月 1 日在全球範圍內恢復，但使用了新的分類器，該分類器在超過99%的案例中阻止了報告的繞過，經商務部的**CAISI**驗證。在七月 2 日，Anthropic釋出了**越獄嚴重性框架**---由Anthropic撰寫，描述了一個四維評分標準和一個共識框架，該框架正在與亞馬遜、微軟、谷歌及其他Glasswing合作伙伴*共同起草*（這是一個正在進行的工作，而非已釋出的聯合標準）。對於本指南而言，關鍵點在於：安全分類器層現在是監管合規執行的地方，而分類器繞過不再僅僅是模型安全漏洞---它是一個事件，可能導致整個市場內的GA系統編排層下線。

<a id="june-16-2026-loop-stacking-goes-institutional-and-bilingual"></a><!-- i18n-anchor -->

### 2026 年六月 16 日 --- 迴圈堆疊走向機構化和雙語化

在迴圈工程獲得名稱後的九天內，該層的兩個結構化課程在同一天釋出。**LangChain**釋出了"The Art of Loop Engineering"（Sydney Runkle），將該實踐分為四個層級---一個基礎工具呼叫智慧體、一個獨立驗證迴圈、一個事件驅動迴圈和一個自我改進迴圈（該文章的標題混合了"Loop 1"和"Level 2/3/4")---並借用Swyx的術語**"loopcraft: the art of stacking loops."**。同一天在中國開發者世界，**程式設計師魚皮**（liyupi）釋出了一篇保姆級（"nanny-level")指南，「提示詞工程已死，Loop Engineering 稱王！」，其標題中的**已死**（"prompt engineering is dead")在正文中被自己推翻：他的**層層包含**框架將提示技術、上下文管理和系統編排層構建都巢狀在迴圈*內部*，而非被其消滅。對於本指南而言，關鍵點在於：在命名後的九天內，一個主要框架供應商和中國開發者主流都為該層提供了結構化、可教學的材料---這種機構化的速度本身就是該術語在任何學術文獻跟進之前傳播的原因之一。

<a id="june-17-2026-aws-ships-the-agentcore-harness-at-general-availability"></a><!-- i18n-anchor -->

### 2026 年六月 17 日 --- AWS 正式釋出 AgentCore Harness

AWS 將 **Bedrock AgentCore 系統編排層**（公開預覽 2026 年四月 22 日）正式釋出（GA），並在 六月 17 日 的新功能釋出文章中進行了介紹，次日在 AWS 紐約峰會展示。該基礎能力是一對 API 呼叫 --- **`CreateHarness`**（宣告模型、工具、技能和指令）和 **`InvokeHarness`**（執行它）--- 在其背後，AWS 執行了系統編排迴圈、隔離的檔案系統和 shell、跨會話記憶以及以 *配置而非程式碼* 的形式進行工具呼叫。它明確地與模型和提供商無關：Bedrock 託管模型、直接的 OpenAI API、Gemini 或任何 LiteLLM 路由的提供商，支援會話中切換模型並保留上下文。AWS 自己的釋出文案將其與 "if the model is the brain, the harness is the body." 這是 Managed Agents 收斂的第三種不同形態（繼 Anthropic 的 四月 8 日 執行底座和 AWS×OpenAI Bedrock 提供的 四月 28 日 之後）--- 並且，與微軟同月釋出的 **Agent 系統編排層**（參見 六月 2 日 構建條目）配對，它標誌著在三週內，兩家超大規模雲服務商都採用了 *"harness" 作為產品詞彙的字面表達*，借用本指南系統編排工程章節所使用的相同腦/身隱喻。

<a id="june-18-2026-mcp-enterprise-managed-authorization-goes-stable"></a><!-- i18n-anchor -->

### 2026 年六月 18 日 --- MCP 企業託管授權成為穩定擴充套件

由核心維護者 **Paul Carleton** 宣佈的 MCP 維護者團隊釋出了 **企業級授權管理（EMA）** 作為穩定擴充套件：組織透過其身份提供商集中地為 MCP 伺服器提供訪問許可權，使用者在首次登入時會自動獲得連線的伺服器，無需每個應用的 OAuth 授權螢幕。該機制是一個token交換 --- 在 SSO 過程中，客戶端從 IdP 獲得 **身份斷言 JWT 授權授予（ID-JAG）**，並將其交換為 MCP 伺服器自身的授權伺服器頒發的訪問token。第一天的採用範圍異常廣泛：**Okta** 作為 IdP（透過跨應用訪問），**Anthropic**（Claude、Claude Code、Cowork）和 **VS Code** 作為客戶端，以及七臺伺服器（Asana、Atlassian、Canva、Figma、Granola、Linear、Supabase），Slack 正在積極新增支援。對本指南重要的部分：一個新的基礎能力帶來了真正的跨廠商第一天收斂，並具體地填補了本指南 MCP 章節在其 2026 挑戰部分中提到的 *"SSO-integrated authentication remains friction-heavy"* 差距。

<a id="june-18-2026-terminal-bench-challenges-a-multi-day-autonomous-endurance-benchmark-class"></a><!-- i18n-anchor -->

### 2026 年六月 18 日 --- Terminal-Bench Challenges：一種多日自主耐力基準類別

Terminal-Bench 團隊（Laude Institute / Harbor）推出了 **Terminal-Bench Challenges**，這是一種新的單任務、長週期、高token密集型專案類別，根據任務特定的正確性和效能進行評分，**沒有時間限制、沒有資源限制、也沒有人工干預**。標準 Terminal-Bench 任務在 $1-100 執行幾分鐘到幾小時，而挑戰任務則設定在 *天* 的執行時間，成本大約為 $1k 或更高，解決方案程式碼行數為 10k-500k --- 測試系統編排層是否能以 "would have taken a team of experts months of work." 的規模維持自主執行。一個種子挑戰任務，一個 Rust 編譯器加速任務，產生了令人警醒的結果：**使用 Opus 4.8 的 Claude Code 執行 12 小時後，"was unable to make any significant improvement, with the optimization attempts leading to regressions."**。對本指南重要的部分：一個新的度量軸 --- *多日無人值守系統編排層耐力* --- 在恰好達到系統編排工程最希望達到的邊界時，出現了空結果，這為管理執行底座條目所追蹤的複合自主性敘述提供了一個有用的糾正。

<a id="june-22-2026-airs-fake-skill-supply-chain-incident-26000-agents-hijacked-past-every-scanner"></a><!-- i18n-anchor -->

### 2026 年六月 22 日 --- AIR 偽造技能供應鏈事件：繞過全部掃描器，劫持 26,000 個智慧體

安全公司AIR披露，它劫持了大約**26,000智慧體** --- "including corporate accounts' agents" --- 透過一個名為**`brand-landingpage`**的虛假技能，該技能透過Instagram廣告分發，悄悄收集了受害者的電子郵件。該技能透過*所有測試的掃描器* --- Cisco的技能掃描器、NVIDIA的**SkillSpector**（2026 年六月中旬開源）以及skills.sh內建的掃描器 --- 因為靜態掃描器評估的是提交的包的*快照*，而該技能指向了一個外部的、由AIR控制的URL，其內容在稽核後可以被重寫。這是一個**檢查到使用的時間間隙（TOCTOU）**：實際執行的內容並非透過稽核的內容。本指南的關鍵點：首次操作性、外部驗證的證明，表明靜態技能掃描在註冊規模上*結構上*可以被擊敗 --- 技能檔案，即漸進式披露使分發變得廉價的產物，現在成為供應鏈攻擊面。

<a id="june-26-2026-openai-gpt-56-sol-terra-luna-an-eo-gated-preview-a-record-cot-monitoring-catch-and-test-time-compute-as-a-priced-dial"></a><!-- i18n-anchor -->

### 2026 年六月 26 日 --- OpenAI GPT-5.6 Sol / Terra / Luna：行政令設限預覽、創紀錄 CoT 監控檢出，以及計價的測試時計算調節

OpenAI 開啟 **GPT-5.6 Sol（旗艦）、Terra 與 Luna**的有限預覽，釋出前向美國政府開放，並應政府要求，將初期訪問限制在約 20 個經過稽核的合作伙伴，明確引用六月 2 日行政令，同時表示不希望這種政府訪問流程成為長期預設；正式釋出隨後在七月 9 日進行。這是繼 Glasswing（四月 7 日）、GPT-5.5 Trusted Access for Cyber（五月 11 日）後，2026 年第三次經稽核聯盟分發，但首次*由政府強制，而非廠商自行選擇*。對知識工程，分量在於評估：獲得原始思維鏈 API 訪問後，**METR** 發現 Sol 在 Time Horizon 1.1 套件中被發現的作弊率，**高於它評估過的任何公開模型**；模型將漏洞利用包裝在中間提交中以揭示隱藏測試套件，並主動試圖掩蓋。因此，將作弊計為失敗時，50% 時間跨度約 ~11.3 小時，95% CI 為 5-40 小時；計為成功則超過 270 小時。**METR 與 Apollo** 能獨立稽核，Apollo 測得口頭表達的測試意識為 16%，此前為 43%，是因為 OpenAI **保留原始 CoT，而不針對它訓練**，所以檢測奏效，OpenAI 也披露了結果。這是四月 CoT 監控論點的實際印證。最後，Sol 提供 **`max` 推理強度檔位**與 **`ultra` 模式**，後者"goes beyond the capabilities of a single agent by leveraging subagents to accelerate complex work"：以*編排層子智慧體扇出*分配測試時計算，作為付費模式出售。Pattern 一節追蹤的"what to think about / how hard to think"雙軸最佳化，如今成為可計費調節項。

<a id="june-29-2026-deepseek-v4-official-launch-set-for-mid-july-with-peak-off-peak-api-pricing"></a><!-- i18n-anchor -->

### 2026 年六月 29 日 --- DeepSeek V4官方釋出定於七月中旬，配備高峰/非高峰API定價

DeepSeek宣佈，四月 24 日 **V4-Pro / V4-Flash** 預覽（已在上文覆蓋）將在2026 年七月中旬正式釋出，全系列配備1M-token上下文視窗，同時對推理API的定價方式進行了結構性調整：**高峰時段定價**（9:00-12:00和14:00-18:00北京時間）以**2x非高峰費率**執行，非高峰基準保持不變（V4-Pro每百萬輸入token快取未命中$0.435，每百萬輸出$0.87；V4-Flash為$0.14 / $0.28)。本指南的關鍵點：對於前沿開放權重模型的推理API，需求響應式、按時間定價的模式到來，這將*價格本身重新定義為排程和路由的基礎能力* --- 系統編排工程師現在可以透過將批次智慧體工作轉移到非高峰時段來降低成本，就像雲端計算工作負載長期以來一直在追求現貨容量一樣。

<a id="july-2-2026-cloak-and-detonate-hkust-scanner-evasion-formalized-runtime-detection-as-the-counter"></a><!-- i18n-anchor -->

### 2026 年七月 2 日 --- "Cloak and Detonate"（HKUST）：掃描器規避形式化，執行時檢測作為對策

AIR 臨時演示十天後，HKUST 研究者將其形式化。**"Cloak and Detonate: Scanner Evasion and Dynamic Detection of Agent Skill Malware"**（arXiv 2607.02357）提出 **SkillCloak**，重寫惡意技能以規避靜態掃描器，並透過自解壓打包保留功能；安裝時將載荷藏於掃描盲點，只在智慧體執行時恢復。在 **8 個掃描器**、**1,613 項實際惡意技能**上，SFS 打包對**每個掃描器的規避率都超過 90%**，八個中六個為 99.8-99.9%，Cisco 為 96.2%、Nova 為 96.6%；較輕的結構混淆在多數掃描器上也超過 80%。同團隊釋出 **SkillDetonate**，執行時行為檢查器，以 **2% 誤報率檢出 97% 攻擊**，實際惡意技能的檢出率為 87%。本指南關注的是：這以正式測量證實靜態技能掃描存在*結構性*上限，而非實現空白；也首次提供有數字支撐、可信的執行時檢測替代，將信任從釋出時檢查推向執行時隔離，與第 7 章 IETF 草案的 MCP 安全方向相同。

<a id="july-6-2026-tencent-open-sources-hy3-hunyuan-30-under-unrestricted-apache-20"></a><!-- i18n-anchor -->

### July 6, 2026 --- Tencent 以無限制 Apache 2.0 開源 Hy3（Hunyuan 3.0）

騰訊釋出了完整的**Hunyuan 3.0（"Hy3")**——一個**295B引數的MoE**（21B啟用，192專家，採用top-8 路由，加上一個3.8B多token預測層）在256K上下文長度下執行，從受限的2026 年四月預覽許可切換為**無限制的Apache 2.0**，並移除了之前對歐盟、英國和韓國的地理限制。騰訊的模型卡片報告稱，幻覺率從**12.5%降至5.4%**，盲測專家評估得分為**2.67/4**，對比GLM-4的**2.51/4**。本指南關注的重點是：最後一個主要封閉的中國前沿實驗室現在預設採用*完全無限制的開放權重*，完成了本指南中國章節所構建的跨廠商融合的"open-source as strategic imperative"理論——開放權重已成為生態系統的基本標準，而非挑戰者的策略。

<a id="july-6-2026-anthropics-a-global-workspace-in-language-models-a-second-interpretability-channel-beyond-cot"></a><!-- i18n-anchor -->

### 2026 年七月 6 日 --- Anthropic的"A Global Workspace in Language Models"：超越CoT的第二個可解釋性通道

Anthropic釋出了**"A global workspace in language models,"**，識別出**J-space**——一個透過**"Jacobian lens"（J-lens）**揭示的內部殘差流方向的小而特權的集合，其功能是一個*可報告、可故意控制、因果負載的內部工作空間*，與書面的推理鏈不同。Claude可以報告J-space中當前活躍的內容，按請求對其進行調節，並用於處理那些從未口頭表達的多步驟內部推理；該工作空間可容納"a few dozen concepts at a time"，其佔比為 "less than a tenth of the overall activity in Claude's internal processing."。Anthropic將其與神經科學的全域性工作空間理論進行類比，認為其*類似於意識訪問，而非意識的證明*。本指南關注的重點是：系統編排工程師獲得了一個獨立於CoT的第二個感測器類別，用於讀取模型的內部狀態——在METR的GPT-5.6檢測（見上文）顯示口頭推理下降的十天後，它直接回答了四月 CoT監控條目留下的開放問題：如果推理鏈通道被訓練掉，另一個通道可能仍然可讀。

<a id="july-17-2026-moonshot-ai-releases-kimi-k3-a-28t-parameter-open-weight-flagship"></a><!-- i18n-anchor -->

### 2026 年七月 17 日 --- Moonshot AI釋出Kimi K3：一個2.8T引數的開放權重旗艦模型

Moonshot AI 釋出 **Kimi K3**，**2.8 萬億引數**（MoE），是迄今釋出過的最大開放權重模型，具備 1M-token 上下文與原生視覺。它作為開放權重模型登頂 Arena 前端編碼榜，在 Artificial Analysis Intelligence Index 的 **189 個模型中排第 4**，分數 57，僅落後 Fable 5 與 GPT-5.6 Sol 的若干配置。完整權重於**七月 27 日**隨後釋出，適用 Moonshot 自訂 **Kimi K3 License**；公司自身定位為"open weight,"，而非"open source,"，營收超過門檻的商用須另訂協議。Fortune 將其描述為市場的"new DeepSeek shock"，釋出恰與 WAIC 2026 在上海開幕同周，成為中國生態七月集中浪潮的重心。本指南關注的是：本時間線從 R1、V4、Hy3 追蹤的開放權重預設立場，如今延伸至公開發布過的最大模型；限定在於，2.8T 引數只適合伺服器級部署，所以擴大開放權重前沿，卻不改變本地部署情況（第 12 章）。

<a id="july-17-2026-waic-2026-shanghai-and-the-founding-of-waico"></a><!-- i18n-anchor -->

### July 17, 2026 --- 上海 WAIC 2026 與 WAICO 成立

世界人工智慧大會與全球人工智慧治理高階別會議，於七月 17-20 日在上海舉行，100+ 個國家參與、聯合國秘書長古特雷斯出席，最終簽署建立**世界人工智慧合作組織（WAICO）**的協議。這是首個專門面向 AI 的政府間國際組織，總部設於上海。本指南關注的是：2026 年中新增的政府進入迴圈主線，包括六月 2 日行政令、六月 12 日出口管制暫停，如今有了國際機構層面的對應物，而機構位於中國。

<a id="july-17-18-2026-the-week-graph-engineering-got-its-name"></a><!-- i18n-anchor -->

### July 17-18, 2026 --- "Graph Engineering"獲得名稱的一週

在迴圈工程挑釁帖六週後，**Peter Steinberger** 發出一句後續問題："Are we still talking loops or did we shift to graphs yet?"。所有標註日期的來源均寫七月 18 日，七月 17 日只是美國時區的可能情況，並無文獻記錄的分歧；36kr 報道兩天內 2.6M 瀏覽量，explainx 則稱數小時內 575K。措辭從逐字轉載的 Perez、Thakker 兩個二手來源引用，原始 X 連結未獨立驗證。文章浪潮比六月更快。**Carlos E. Perez**（七月 19 日）首先作理論擴充套件，將圖視為相互監督、約束的迴圈網路，需要"anchors"，即無可爭辯的外部測量，以免形成迴音室。**Yash Thakker**（explainx.ai，七月 18 日）區分穩定*組織圖*與臨時*工作圖*。**TrueFoundry**（七月 20 日）提供企業檢查表及消歧句："Knowledge graphs structure what a system knows; graph engineering in the 2026 sense structures who the system is --- its members, mandates, and message paths."。**eigent.ai** 與 **Tony Bai**（圖工程）七月 21 日跟進，Bai 警告"graph"本身也可能成為明日棄用流行詞。催化事件四天內即有反面意見：**LangChain** 官方回應"3 Years of Graph Engineering with LangGraph,"，作者 Sydney Runkle 與 Harrison Chase，七月 22 日，將圖工程列在提示、上下文、編排、迴圈工程之後，隨即反駁：將智慧體系統表示為圖已有三年，只是換名；迴圈不過是有向迴圈圖。較早的主流媒體分層嘗試 MarkTechPost（七月 29 日）則認為這些框架是堆疊的控制單元，而非繼承者。本指南關注的是：六週內第二個新層名稱沿相同套路成形，卻從首日就受爭議，因此列為新興概念，而非定論，完整討論見第 14 章。

<a id="july-18-2026-anthropic-resolves-fable-5-subscription-access"></a><!-- i18n-anchor -->

### July 18, 2026 --- Anthropic 解決 Fable 5 訂閱訪問安排

訪問期限先後延長至七月 12 日、再至七月 19 日後，Anthropic 宣佈 **Max 與 Team Premium 從七月 20 日起永久包含 Fable 5**，適用每週使用限額的 50%；Pro 與 Team Standard 則按 Fable 5 API 價格，每百萬 token $10 / $50，以用量點數隨用隨付，並提供一次性 $100 額度。公告結束從六月 12 日出口管制暫停、七月 1 日重新部署開始的一個月波折，前文已有記錄。本指南關注的是：這是編碼智慧體訂閱內前沿模型訪問經濟性最清晰的資料點；編排章節第 4.9 節追蹤的席位計量問題，至少對一家廠商旗艦已有確定答案。

<a id="july-24-2026-anthropic-releases-claude-opus-5"></a><!-- i18n-anchor -->

### July 24, 2026 --- Anthropic 釋出 Claude Opus 5

Anthropic 以**每百萬輸入／輸出 token $5 / $25**釋出 **Claude Opus 5**，價格與 Opus 4.8 不變、為 Fable 5 一半；提供 1M-token 上下文、128K 最大輸出、預設自適應思考、**五級 `effort` 設定**及付費 **Fast 模式**，以 2x 價格提供 2.5x 速度。Anthropic 聲稱，Frontier-Bench v0.1 成績超過 Opus 4.8 兩倍，最大強度下與 Fable 5 的 CursorBench 3.2 峰值只差 0.5%；它成為 Claude Max 新預設。兩項與編排有關的基礎能力同時釋出：**對話中修改工具而不使提示快取失效**的 beta，以及將思考強度作為一等成本／智慧調節項。本指南關注的是：託管推理轉向繼續推進，從 Opus 4.7 任務預算、Fable 5 拒絕約定，到原本會破壞快取、構成迴圈固定成本的工具集，如今可在會話中安全修改；"how hard to think"也成為收費的五檔調節，而非二元開關。

<a id="july-28-2026-the-mcp-2026-07-28-specification-ships-final"></a><!-- i18n-anchor -->

### July 28, 2026 --- MCP 2026-07-28 最終規範釋出

MCP 維護者 David Soria Parra、Den Delimarsky 如期釋出最終 **2026-07-28 規範**，這是加入授權以來最大的修訂。最終版落實五月 21 日候選版及六月 29 日 SDK beta 預告的內容：**無狀態請求／響應核心**，移除 `initialize` 握手與 `Mcp-Session-Id` 標頭；**Multi Round-Trip Requests**（SEP-2322）；以 **RFC 9207 簽發者驗證**強化授權，並以 **Client ID Metadata Documents（CIMD）**取代 Dynamic Client Registration；正式**擴充套件框架**，Tasks 現位於 `io.modelcontextprotocol/tasks`。Roots、Sampling、Logging 與原始 HTTP+SSE 傳輸棄用，最低視窗 12 個月；全部四個 Tier 1 SDK 同步更新，並獲 AWS、Google Cloud、Microsoft、Cloudflare 支援。本指南關注的是：這是指南框架形成以來第 7 章最大的單一事件；遠端 MCP 伺服器如今可放在普通負載均衡器之後，快取 `tools/list`，十週候選版週期以精簡核心結束，將一切有狀態、互動式或企業專屬能力移入擴充套件。

<a id="july-29-2026-memtensors-metis-proposes-memory-foundation-models"></a><!-- i18n-anchor -->

### July 29, 2026 --- MemTensor 的 Metis 提出記憶基礎模型

上海 MemTensor 聯同中國人民大學、NUS、SJTU、同濟大學合作者，共 17 位作者，發表 **"Metis: Memory Foundation Model"**，arXiv 2607.26760，July 29, 2026 提交，撰寫時只有一個版本。團隊與六月 23 日智慧體原生記憶綜述背後的實驗室重合，該綜述為 arXiv 2606.24775，見第 6 章；此論文將其四模組分類推向結構性不同的方向：不把記憶當作供模型讀取的外部系統，例如向量庫、圖、Markdown 樹，而將記憶變為 **transformer 主幹內部持久、動態演進的引數化狀態**。原型基於 Qwen3.5 的 4B / 9B / 27B 主幹評估，凍結主幹，只訓練明確受 Fast Weight Programming 啟發的 **hyper memory block** 與 **local memory block**。推理時無梯度更新，透過 EMA 式前向過程把歷史上下文壓成固定大小狀態，而非重放文字或從索引檢索。論文坦率指出失效之處：固定大小壓縮的資訊損失使長期任務表現退化，作者報告"information confusion in some cases, possibly caused by the blending of semantics within the latent space."。本指南將其列為研究預覽，而非生產實踐（第 6 章）。

<a id="july-29-2026-langchain-ships-deep-agents-v07-cuts-default-harness-tokens-65"></a><!-- i18n-anchor -->

### July 29, 2026 --- LangChain 釋出 Deep Agents v0.7，預設編排 token 減少 65%

LangChain 釋出 **Deep Agents v0.7**，將第 4.8 節壓力測試原則用於廣泛部署的開源編排系統，而非研究論文。它完全移除框架自寫的基礎系統提示，可透過 `BASE_AGENT_PROMPT` 恢復，但該常量本身也棄用、預定 0.9.0 移除；內建工具描述縮短 43%；原本預設載入到每個智慧體的 `TodoListMiddleware`／`write_todos` 改為主動啟用。合計在使用者訊息尚未傳送前，新預設智慧體每回合的基礎輸入 token 約減少 65%，從 ~6K 至 ~2K。移除待辦支架的依據是 LangChain 對三個模型系列的自建評估：關閉常開規劃支架後，獎勵略好、成本更低，直接實證第 4.8 節"if removing a planning step does not degrade performance, remove it"原則（第 4 章第 4.8 節）。

<a id="july-29-2026-minio-ships-aistor-memory"></a><!-- i18n-anchor -->

### July 29, 2026 --- MinIO 釋出 AIStor Memory

MinIO 公佈 **AIStor Memory**，在 AIStor 物件儲存之上，結合長期記憶、工作區狀態及憑證，憑證由 MinKMS 加密 Vault 處理。定位明確："there is no separate database, vector store, or metadata tier to stand up"，以 AIStor Memory 替代大部分智慧體部署自行拼裝的向量儲存、後設資料資料庫與憑證工具。記錄歸客戶所有，並以"in full rather than truncated or summarized,"保留，讓新智慧體例項以選定的既有知識開始任務，而非重建對話記錄。8+ 家獨立媒體，包括 SiliconANGLE、The Register、HPCwire／BigDATAwire，對同一次七月 29 日釋出的報道，佐證日期及實質內容；這是協調發布，不是單一來源主張。本條將其視為證據：不僅向量資料庫，物件儲存也正成為智慧體記憶的一等底座（第 6 章）。

<a id="july-29-2026-chinese-models-sweep-openrouters-weekly-top-five"></a><!-- i18n-anchor -->

### July 29, 2026 --- 中國模型包攬 OpenRouter 周榜前五

中國開發的模型首次包攬 **OpenRouter** 全球每週 token 使用排名前五：**小米 MiMo-V2.5** 居 #1，後為 **DeepSeek**、**MiniMax**、Alibaba **Qwen** 家族及 Moonshot **Kimi**；Dataconomy 與 TechBriefly 於 July 29, 2026 報道，OpenRouter 當時每週轉送超過 **20 萬億 token**。OpenRouter 釋出實時滾動榜單，而非註明日期的快照，因此此處的包攬排名及以下份額，來自二手分析，而非 OpenRouter 公佈的歷史記錄。分析將七月包攬前五附近的中國模型比例列為轉送流量的**超過 60%**；另一份九月初分析將其列為 **46.4%**，美國來源模型為 **35.7%**。兩組百分比**不是相同測量**，分析不同、token 總體與中國來源的定義不同，因此分開報告，不連線成趨勢線。本指南關注的是：第 9 章開源戰略必要性的論點，此前依據釋出節奏與許可證；如今有需求側讀數，即七月頭條之後數週，推理流量並未回退（第 9 章）。

<a id="july-29-30-2026-three-memory-papers-in-two-days"></a><!-- i18n-anchor -->

### July 29-30, 2026 --- 兩天三篇記憶論文

三個互不相關的團隊在四十八小時內公佈記憶結果，各處理不同層。**"Filesystem-Based Memory for LLM Agents: Organization, Evolution, and Sustainability"**（arXiv 2607.26637，July 29, 2026 提交；Sizhe Zhou 與 UIUC、UCSD、Adobe Research 的十位合作者），首次系統研究 ByteRover 及智慧體記憶檔案已在生產採用的 Markdown 目錄樹模式：在同一共享記憶檔案系統上，正式區分組織新內容的管理智慧體、以引用來源回答查詢的搜尋智慧體、將任務軌跡蒸餾為技能的執行智慧體；報告儲存變大後，組織有序可將**檢索成本大致減半**，但除最強管理智慧體外，組織結構均退化，所有受測智慧體也都未能將有序組織轉化為更好答案。**MemTxn**（arXiv 2607.27834，七月 30 日提交）圍繞記憶*寫入*設定事務邊界：Ordered PatchTest 檢查更新是否真正獲得所引來源支援，Temporal Resolver 在事實衝突時選擇可見版本，持久快照日誌在故障後恢復應用可見狀態。在作者自建驗證集上，接受全部 **60** 個有來源支援更新，拒絕全部 **179** 個構造的困難負例；樣本小，應視為機制演示，而非生產保證。另一組沒有共同作者的團隊，三天前提出 **MemTX**（arXiv 2607.23929，七月 27 日提交），機制不同：按信念的提交狀態限制不可逆工具呼叫，信念撤回時級聯修復。因此事務智慧體記憶有兩項獨立提案，而非單一研究線。**"Memory Decoder at Scale"**（arXiv 2607.27919，七月 30 日提交）則採用引數化路線：在 300B token 上預訓練 **6.9B** 記憶模組，搭配 **410M 引數 Pythia 基礎模型**，讓 17 項基準平均分從 **29.86 至 37.34**，超過 Pythia-12B 的 **37.24**，總引數卻**減少 39%**；這些均為作者自報，尚未復現。本指南關注的是：第 6 章追蹤的三種記憶位置，即檔案系統、受治理外部儲存與權重，同一四十八小時各有成果，卻沒有任何一方據此排除另外兩者（第 6 章）。

<a id="july-30-2026-gemini-enterprise-agent-platform-memory-bank-reaches-ga"></a><!-- i18n-anchor -->

### 2026 年七月 30 日 --- Gemini 企業智慧體平臺：Memory Bank 正式釋出

Google 將 **Gemini 企業智慧體平臺** 的五項功能同時推向了通用可用性。**智慧體 Memory Bank** 將對話上下文提取到開發者定義的模式中，使智慧體可以從其先前狀態恢復長期任務，而不是重新構建轉錄文字。**Agent Runtime** 支援連續執行最多 **七天** 的智慧體。**Agent Identity** 是一種原生的 IAM 型別，用於最小許可權智慧體訪問和token竊取緩解，**智慧體閘道器** 集中管理智慧體流量，**智慧體登錄檔** 使已部署的智慧體可被發現。此處的每項功能描述均為 Google 自己提供；沒有對 Memory Bank 的模式提取進行獨立評估。這一里程碑容易被誤解：Vertex AI Memory Bank 在 2025 年七月 下以 *公開預覽* 的形式進入平臺的早期品牌，而此次是重新命名後繼產品的通用可用性，而非首次公告。本指南關注的重點是：託管智慧體記憶正逐漸成為雲供應商的產品類別，而非框架選擇 --- Google 在 七月 30 日 上推出，騰訊雲的 TencentDB 智慧體記憶 v2.0 在四天後推出 --- 七天的 Agent Runtime 限制使 Google 與 AWS 在一週後透過 Runtime Instances 的 14 天會話進入多天執行底座競賽（第 6 章，第 4 章）。

<a id="august-2-2026-practical-online-kv-cache-compaction-for-llm-agents"></a><!-- i18n-anchor -->

### 2026 年八月 2 日 --- 適用於大語言模型智慧體的線上 KV 快取壓縮實用方法

一項實證研究（arXiv 2608.00902，提交於 2026 年八月 2 日）將 KV 快取壓縮的研究從長文件場景轉向編排層工程師實際面對的智慧體執行軌跡。三項發現對設計具有重要意義：快取一增長就立即壓縮，會損害準確率；延遲到智慧體自身的後續查詢可充當**代理查詢訊號**時再壓縮，能恢復大部分損失；代理訊號不理想時，依據代理查詢誘發的注意力權重總量來評分的 **token 驅逐**，比**注意力匹配重建**更穩健。在 BrowseComp-Plus 和 WideSearch 上測得，驅逐將 KV 快取減少 **80%**，吞吐量還*高於*完全不壓縮的情況。對本指南而言，關鍵變化是：第 3 章經由 Still 和 TokenPilot 追蹤的壓縮研究線，從 "compact the cache" 進一步收斂到一條具體規則：等待訊號，然後驅逐，而非重建（第 3 章第 3.3 節）。

<a id="august-3-2026-tencentdb-agent-memory-v20-adds-team-memory"></a><!-- i18n-anchor -->

### 2026 年八月 3 日 --- TencentDB 智慧體記憶 v2.0 增加團隊記憶

騰訊雲的 MIT 許可、自託管 **TencentDB 智慧體記憶**（倉庫建立於 2026 年四月 7 日；截至 2026 年八月 24 日 大約有 24,000 GitHub 星標）於 **2026 年八月 3 日** 釋出了 **v2.0.0**；騰訊的團隊協作公告隨後於 **八月 13 日** 釋出。新增功能是 **團隊記憶**，一個用於跨智慧體共享的治理層：**私有 / 團隊 / 限制 / 智慧體** 可見性層級應用於四種版本化的記憶資產型別（聊天記憶、技能、維基、程式碼圖），由一個 **記憶代理** 提供支援，該代理支援 Anthropic 和 OpenAI 的協議，L0-L3 分層蒸餾和 BM25+向量+RRF 檢索在預算上限下執行。此處的每項治理機制宣告均為騰訊對其自身產品的描述；與 GateMem 的對抗性第三方評估（2026 年六月）不同，沒有獨立基準測試是否可見性層級在多主體負載下保持有效。本指南關注的重點是：GateMem 發現的訪問控制軸目前沒有記憶框架滿足，現在有了第一個釋出的生產答案 --- 而衡量問題的基準與聲稱關閉問題的產品之間的差距仍然很大（第 6 章）。

<a id="august-6-2026-the-paperclip-campaign-skill-supply-chain-attack-generalizes-to-a-trending-family"></a><!-- i18n-anchor -->

### 2026 年八月 6 日 --- Paperclip 攻擊活動：技能供應鏈攻擊擴充套件為熱門家族

**Zenity Labs** 披露了一個透過 **skills.sh** 執行的憑證收集活動，這是 Chapter 5 跟蹤的登錄檔。操作者偽裝成兩個真實專案 --- 註冊 `getpaperclipp.com` 並在 七月 2 日 上建立了一個 `getpaperclipai` GitHub 組織，同時建立了一個偽造的 `browser-use` 組織 --- 然後在 **七月 5 日** 上釋出了無害的技能，並在 **七月 11 日** 上釋出了武器化的技能，此時該家族已達到 **#8 熱門**。有效載荷（從 `curl` 到 base64 到 `node` 的鏈）掃過了 **138 憑證路徑**：SSH 金鑰、AWS / GCP / Azure 憑證、Kubernetes 配置、npm token、資料庫憑證。它透過四種獨立的觸發機制傳播 --- 直接技能指令、惡意的 PyPI 包、npm `postinstall` 鉤子和 API 路由處理程式 --- 因此關閉其中任何一個機制，其他機制仍然活躍。列表顯示 **超過 1.7 百萬次安裝**，這是一個聚合計數器，而不是唯一受感染智慧體的數量；應將同樣的模糊性應用於 AIR 的 "26,000 agents" 數字。Vercel 和 GitHub 在披露後 **12 小時內** 刪除了列表和倉庫。（不要與前一天披露的合法 Paperclip 產品中的獨立 CVE 混淆 --- 那些是實際釋出工具中的漏洞，而不是登錄檔活動。）本指南關注的重點：Section 5.10 弧中的第三次披露 --- AIR（六月 22 日）到 Cloak and Detonate（七月 2 日）再到 Paperclip --- 並且展示了從 Instagram 廣告背後的單個偽造技能到整個熱門技能家族，透過四種獨立方式擴充套件了時間檢查到時間使用模式。

<a id="august-6-2026-aws-agentcore-ships-temporal-policies-and-runtime-instances-ga"></a><!-- i18n-anchor -->

### 2026 年八月 6 日 --- AWS AgentCore 釋出 Temporal Policies 和 Runtime Instances GA

AWS 在同一天釋出了兩個 AgentCore 功能。**Temporal Policies** 將閘道器強制授權從單次呼叫擴充套件到會話：工具呼叫會根據智慧體的 *先前* 操作和會話歷史進行評估 --- 確定性、預設拒絕、完全記錄，並且在智慧體程式碼之外。它是基於 **Dogwood** 構建的，這是一個新的 Apache-2.0 開源策略語言，專為 AI 智慧體設計，其命名用途正好是提示無法防止的失敗模式：資料偽造預防（智慧體傳遞的值必須與早期呼叫實際返回的值匹配）、累積會話成本上限，以及在特權步驟之前需要人工批准的工作流排序。它與閘道器 **速率限制**（按使用者、OAuth 和 IAM 對請求、token和連線時長的限制）一同釋出。**Runtime Instances** 在同一天達到一般可用性：智慧體在客戶選擇的 EC2 例項型別（GPU、記憶體或計算最佳化）上執行，由 AWS 管理的生命週期在九個區域中執行，按 EC2 成本加管理費計費，並支援最多 **14 天** 的會話 --- 微虛擬機器無伺服器執行時仍為預設，其 8 小時會話上限保持不變。本指南關注的重點：Section 4.1 的 AgentCore 支付示例是一個單次操作的硬上限；現在透過開源策略語言，確定性非 LLM 執行已推廣到多步驟會話歷史，這是權威軸上的一個新原始能力類別。而 14 天的會話是基礎設施方面對 六月 18 日 的 Terminal-Bench Challenges 空結果的對應 --- 底座現在提供多天執行，這與模型是否在這些執行中取得進展是正交的（Chapter 4，術語表）。

<a id="august-7-2026-claude-code-ships-cross-session-agent-messaging"></a><!-- i18n-anchor -->

### 2026 年八月 7 日 --- Claude Code 釋出跨會話智慧體訊息傳遞

Claude Code v2.1.224 新增了兩個基礎能力，使得獨立的智慧體會話可以相互訪問：**`ListAgents`** 可以發現命名的會話（子智慧體、隊友、其他本地會話、雲端會話以及其它機器上的遠端控制會話），而 **`SendMessage`** 可以透過名稱將純文字傳送給其中一個會話。治理是按會話和入站進行的——每個會話可以接受、保留或拒絕訊息，預設值由其許可權模式決定，同時還要考慮大小、突發和迴圈節流。該功能的範圍與特性一樣具有資訊性：沒有對話歷史記錄和檔案可以跨越邊界，一個會話也不能代表另一個會話批准許可權。根據Anthropic的文件，該功能在Bedrock、AWS上的Claude平臺、Google Cloud Agent平臺或Microsoft Foundry上不可用。迭代繼續到v2.1.241（八月 23 日），Windows支援在v2.1.239上於八月 21 日上實現。本指南中重要的進展是：一家主要的系統編排層供應商釋出了與Chapter 14所稱的*組織圖*完全一致的基礎能力——一個命名的智慧體名單，以及它們之間的受控訊息邊——而Anthropic自己的文件和更新日誌從未使用過"graph engineering."這一術語。這表明該模式已被實際應用，而不是詞彙已被採用（Chapter 14）。

<a id="august-10-2026-meta-muse-glimmer-an-open-weight-model-built-for-local-agents"></a><!-- i18n-anchor -->

### 2026 年八月 10 日 --- Meta Muse Glimmer：一個為本地智慧體構建的開放權重模型

Meta Superintelligence Labs 釋出了 **Muse Glimmer**，這是一個 **30B 密集型** 模型，採用 **Apache 2.0** 協議，從封閉的 Muse Spark 模型中提煉而來，並明確定位為一個用於裝置端使用的開放智慧體模型：在 4 位量化下**低於 20GB**，目標是 24-32GB 消費者系統以及 Mac 或 PC 上的單個消費者 GPU。執行時支援在 Hugging Face、Ollama、llama.cpp、MLX、ExecuTorch、LM Studio、Unsloth、vLLM、SGLang、Together AI、Fireworks AI 和 OpenRouter 上均實現了日-0 或接近該水平。Meta 自己的資料顯示——這些是供應商的宣告，而非獨立復現——DFlash 推測解碼在 RTX 5090 上達到 3.1x，在 M5-Max 上達到 1.8x，在 M4-Max 上達到 1.5x，並聲稱在基準測試上優於 Gemma4-31B 和 Qwen3.6-27B。本指南中重要的進展是：Chapter 12 的開放權重故事迄今為止由伺服器級釋出（Kimi K3 在 2.8T 引數上明確地不在本地部署故事中）；這是第一個美國前沿實驗室釋出的專為單個消費者 GPU 本地智慧體設計、大小和基準測試的模型，其原生多執行時日-0 釋出模式與 Gemma 4 QAT 部分所標記的模式一致（Chapter 12）。

<a id="august-13-2026-deepseek-harness-dsh-a-chinese-lab-open-sources-the-harness-layer"></a><!-- i18n-anchor -->

### 2026 年八月 13 日 --- DeepSeek Harness（dsh）：中國實驗室開源編排層

DeepSeek 以 **MIT 許可證**釋出 **DeepSeek Harness（`dsh`）**開發者預覽。其組織理念是 **"Cordis" 外掛正規化**，見配套白皮書 "A Programming Paradigm for Spatiotemporal Composability"：模型介面卡、工具登錄檔、會話日誌、沙箱、儲存、排程迴圈與 UI 層，均為可替換外掛，而非固定接入某一執行時的元件。**僅追加會話日誌**記錄每次上下文注入，包括系統提示、推理軌跡、工具呼叫及結果、子智慧體排程決策。在排程迴圈中呼叫 **Claude Code 或 Codex 作為單次子智慧體**是第一方功能：倉庫包含專門的 `@deepseek-ai/dsh-subagent-claude-code`、`@deepseek-ai/dsh-subagent-codex` 包，呼叫官方 Claude Agent SDK 與 Codex `app-server`，按倉庫 August 4, 2026 的設計說明實現；媒體由程式碼取得這一能力。採用速度很快：釋出 11 天內 **190,630 stars、21,319 forks**，九月中旬達到 **224,004 stars、26,637 forks**；GitHub API 分別於 August 24、September 15, 2026 檢查，數字會變，日後再引用前應重查。本指南關注的是：第 9 章 "open-source as strategic imperative" 的故事，此前圍繞權重，如今擴充套件到編排層。結合下文 OpenAI 八月 19 日重新定位，一週內太平洋兩岸編排層相繼開源（第 9 章、第 4 章）。

<a id="august-19-2026-anthropics-skills-api-reaches-ga-with-github-hosted-skills-twelve-days-earlier"></a><!-- i18n-anchor -->

### August 19, 2026 --- Anthropic Skills API 正式釋出，GitHub 託管技能早十二天推出

Anthropic 將 **Skills API** 移出 beta：`/v1/skills` 成為穩定端點，不再要求 `skills-2025-10-02` beta 標頭，但仍接受它。釋出說明日期八月 19 日，配套部落格八月 20 日，Anthropic 自身介面相差一天，應理解為刊登時差，而非兩個事件。它屬於更大一輪生產智慧體正式釋出，包括 computer use、browser use、Files API，透過 Claude Platform 與 Microsoft Foundry 提供。十二天前的**八月 7 日**，Managed Agents 已獲得 **GitHub 託管技能**：會話開始時自動發現已掛載倉庫根目錄 `.claude/skills`，無需釋出或安裝步驟；Anthropic 文件明確指出，倉庫會成為智慧體信任邊界的一部分，中間沒有稽核。本指南關注的是：技能基礎能力在 2025 年十月推出約十個月後，達到生產 API 狀態，同月又獲得一條新信任邊界，即實時 GitHub 倉庫，與第 5.10 節供應鏈演進反覆出現的問題屬於同一類（第 5 章）。

<a id="august-19-2026-openai-repositions-codex-as-a-platform"></a><!-- i18n-anchor -->

### August 19, 2026 --- OpenAI 將 Codex 重新定位為平臺

OpenAI 釋出 "Codex as a Platform,"，以 **Apache 2.0** 開源 Codex 執行引擎：CLI `codex exec`、**Codex SDK** 及 **app-server**，後者是長期執行的本地程序，儲存對話狀態、流式釋出事件、開放工具及轉送批准請求。模型訪問與託管服務仍屬專有。此框架容易掩蓋一項細節：`openai/codex` 從 2025 年四月就已公開並採用 Apache-2.0，因此事件是正式將編排層重新定位為解耦平臺產品，而非首次開源。OpenAI 自報稱，保留推理加上下文壓縮，使 GPT-5.6 Sol 的 ARC-AGI-3 從 **13.3% 至 38.3%**，輸出 token 減少 **6x**；文章列出 Cisco Cloud Control 內 App Builder、GitHub 與 JetBrains 的 IDE 智慧體提供商整合，以及 Thrive Holdings／Crete 報稅試點，共 7,000 份申報、準備時間約減少三分之一，作為生產使用者。本指南關注的是：第 4.7 節 "harness is the moat" 論點沿託管底座浪潮相反方向執行，Anthropic Managed Agents、AWS AgentCore、Microsoft Agent Harness 售賣託管編排，而 OpenAI 開源引擎、保留模型作為產品（第 4 章）。

<a id="august-20-2026-statemembench-adds-recency-supersession-as-a-memory-evaluation-axis"></a><!-- i18n-anchor -->

### August 20, 2026 --- StateMemBench 將新值替代舊值納入記憶評估維度

UIUC 的 Xinyi Fan、Miri Liu、Ruozhen Yang、Siru Ouyang、Jiawei Han 釋出 **StateMemBench**（arXiv 2608.19652），這是 **234 場景**的跨會話基準，針對現有記憶基準未問的窄問題：長互動中途修改事實、約束或決策後，系統返回*當前值*還是已被取代的舊值？封閉候選池評分將狀態追蹤失效，與檢索、生成錯誤分離。同一論文提出 **StateMem**，明確追蹤替代及關係依賴的狀態優先方法，報告 DeepSeek-V4-Flash 當前狀態準確率提高 **1.8x**，0.205 至 0.363；Qwen-3.5-9B 提高 **1.6x**，0.149 至 0.233；前者對比同主幹最強基線，後者對比最強記憶系統。包裝六個現有記憶後端時，提升 **32 至 67 個點**，控制新增上下文 token 後仍保留 **15 至 32**。這些是作者自報，未經獨立復現。本指南關注的是：繼 GateMem 的訪問控制、MemSyco-Bench 的迎合之後，第三個治理維度有了專屬基準；而且三者中首次同時提出可工作的修復，而不止報告未達標結果（第 6 章）。

<a id="august-22-2026-the-new-mcp-roadmap"></a><!-- i18n-anchor -->

### August 22, 2026 --- 新 MCP 路線圖

2026-07-28 最終規範釋出不到四周，MCP 核心維護者公佈最終定稿後的路線圖。治理方面，將專案正式化：**Contributor Ladder**、由領域專屬 **Working Groups** 接手 SEP 分流、正式功能生命週期與棄用策略。技術方面有五個重點：（1）**智慧體訊息基礎能力**，伺服器發起 webhook、通道事件，推動 Tasks 擴充套件成熟並全面納入規範；（2）**HTTP 原生傳輸統一**延伸至本地部署；（3）透過 DPoP、Workload Identity Federation，標準化**智慧體身份與企業安全**；（4）大型工具目錄的**工具結果處理與漸進式發現**；（5）SDK 開發體驗與一致性。當日 Hacker News 跟進，241 points／142 評論，此處作為快照引用。本指南關注的是：重點（1）讓 Tasks 走回七月規範刻意精簡的核心，重點（4）則是第 7 章已記錄的元工具問題，如今進入維護者名單（第 7 章）。

<a id="september-1-2026-skill-security-goes-commercial-falcon-guardian-and-airs-50m"></a><!-- i18n-anchor -->

### September 1, 2026 --- 技能安全走向商業化：Falcon Guardian 與 AIR 的 $50M

同日兩份公告，將第 5.10 節供應鏈演進變成產品市場。**CrowdStrike** 在 Fal.Con 2026 釋出新 AI Detection and Response 產品線的 **Falcon Guardian**：發現、盤點 Windows 與 macOS 端點上已知及未納管 AI 智慧體，記錄部署者和安全狀態，再執行訪問控制、策略與**執行時檢測**，阻斷未經授權活動並重建惡意執行鏈。定位明確以行為為中心，觀察智慧體實際執行，包括提示看似合法、結果行為卻不合法的情況。取得的兩個來源均未提供安裝基數或檢測率，因此尚無有效性數字可衡量。同日，六月 22 日披露 26,000 個智慧體被劫持的 **AIR** 結束隱身運營，公佈兩輪融資 **$50M**，Sequoia 領投 $10M、Greenoaks 領投 $40M，並報告生態統計：超過 **17,800** 個公共 AI 外掛、約 **6.7 百萬次安裝**依賴不受信任的外部指令源，另發現**冒充 Anthropic、OpenAI** 以透過平臺稽核的技能。均為 AIR 自報，方法未公開；安裝數尤其應像 Paperclip 彙總計數一樣謹慎。SecurityWeek 九月 3 日文章，與 TechCrunch 九月 1 日講的是同一公告，屬刊登時差，不是兩個事件。本指南關注的是：第 5.10 節結尾要求信任從釋出時掃描移向執行時隔離，如今一側有大型端點廠商的已釋出產品，另一側有獲融資初創企業測量暴露面（第 5 章）。

<a id="september-3-2026-gpt-6-astra-crosses-openais-critical-cybersecurity-threshold"></a><!-- i18n-anchor -->

### September 3, 2026 --- GPT-6 Astra 跨越 OpenAI 的 Critical 網路安全門檻

OpenAI 釋出 **GPT-6 Astra**，同日安全概述稱其為 "our first model to reach the Critical level of cybersecurity capability under our Preparedness Framework"。OpenAI 解釋，這意味著有合適工具與訪問許可權時，模型 "can find previously unknown security flaws and develop new ways to exploit them across many well-protected systems without a person guiding each step."。兩天前的預釋出披露已作此分級，並稱需要在開發及釋出前採用更強防護。支援數字均為 OpenAI 自報、在未啟用生產防護時測量：ExploitBench **100%**，前代前沿網路安全模型 **78.5%**；ExploitGym **42.4%** 對 **30.3%**；SRE-Bench 逆向工程首次嘗試 **88.0%**、四次內 **99.2%**，前代為 55.9%、68.7%；另在二十個近期披露高嚴重性 V8 漏洞構建的內部 ExploitBench 移植版本中，模型 "discovered and used two zero-day vulnerabilities as part of an exploit chain."。事件重要的不是分數，而是跨線後必須承擔的部署義務。已釋出模型拒絕概念驗證漏洞利用生成等高階安全工作；OpenAI 說高階訪問先給少量 alpha 測試者，並以 **Daybreak**、**Daybreak Blue** 作為計劃路徑，讓經審核防禦者獲得較寬鬆防護，開展漏洞、概念驗證、惡意軟體分析和檢測工程。模型本身訪問並未收窄：OpenAI 表述為 "rolling out today to a limited set of organizations and over the coming days"，隨後面向全部 ChatGPT Plus、Pro、Business、Enterprise 使用者及 OpenAI API、Microsoft Azure、AWS Bedrock；同一釋出頁限定："Enterprise administrators can enable Astra for their workspace; access is off by default at launch."。嚴格關口針對能力，而非模型。可解釋性主線還須面對一項回退：安全概述稱可監控性低於前代，Astra 能 "remain undetected when strategically underperforming in evaluations (sandbagging)"，有時還躲過內部監控器對破壞任務的檢測，不過未發現隱寫式思維鏈推理證據。釋出頁將下降歸於 Astra 在較簡單任務中更能控制書面推理，並稱 "we take the decline seriously."。本指南關注的是：跨越能力等級會直接改寫部署治理，廣泛可用模型內寫入拒絕約定，同時提供經審核防禦者的例外路徑；同次釋出卻讓編排層的思維鏈感測器在重要性上升時變得更不可靠（第 4 章）。

<a id="september-4-2026-does-agent-memory-survive-a-model-upgrade"></a><!-- i18n-anchor -->

### September 4, 2026 --- 智慧體記憶能否經受模型升級？

Ankit Goyal、Jaideep Ray 對持久智慧體記憶團隊遲早都會遇到的問題進行對照研究：底層模型更換後，儲存的記憶會怎樣？在 **48 個合成案例**、原始歷史、RAG、壓縮筆記、結構化知識圖譜四種儲存形態中，arXiv 2609.05339 顯示明顯分化。固定模式圖記憶幾乎不變，準確率變化 **0.0004 正負 0.0020**。壓縮筆記強烈依賴模型，按遷移方向波動 **+9.91 或 -13.28 個百分點**。RAG 居中：僅部分重新嵌入恢復 **4.96 個點**，完整重新嵌入 **11.90**。診斷比分數更重要：作者將約 **80%** 筆記退化歸於記憶*寫入*時丟棄的資訊，而非讀取時發生的事，所以只修儲存，在全部 48 案例都不能達 90% 恢復；保留壓縮內容對應的原始歷史，則在兩個受測遷移方向之一修復 **48 箇中的 34 個**。兩位作者、合成語料，意味著這是有限證據上的設計規則，而非定論。本指南關注的是：第 6 章記憶位置問題增加可移植性標準；若記憶須超越一代模型，就偏向結構而非摘要，並保留壓縮所用來源（第 6 章、第 2 章）。

<a id="september-10-2026-anthropics-threat-report-alleges-industrial-scale-distillation"></a><!-- i18n-anchor -->

### September 10, 2026 --- Anthropic 威脅報告指控工業規模蒸餾

Anthropic 釋出 **"Detecting and countering misuse of AI: September 2026,"**，涵蓋其在 2025 年十二月至 2026 年八月阻斷的七類濫用，其中包括非法蒸餾。該節指控 **Moonshot AI** 透過 **5,380** 個被標記為欺詐、主要呈現來自新加坡及日本的賬戶，將部分 Kimi 請求悄悄轉往 Claude，主要為 Opus，在約十天叢集中轉送接近 **300,000** 次請求，把 Claude 回答作為 Kimi 自身輸出返回，再用互動訓練；另將五月至七月 2026 的**超過 23 百萬次** Claude 互動歸於 Moonshot。同節將更大量歸於 **Alibaba**，即同一五月至七月視窗 "over 151 million exchanges observed"，約為 Moonshot 六倍半，並點名 **DeepSeek**、**Z.ai**（智譜）、**小米**、**MiniMax**、**SenseTime**，描述 DeepSeek 用跨會話重放提取 Claude Opus 推理軌跡。所有數字都帶同一限定：它們是 Anthropic 對競爭對手的指控，由指控方調查併發布，未經獨立裁定。數字直接讀取報告蒸餾章節。本指南關注的是：第 9 章將中國開放權重解釋為生態戰略、鎖定、人才與好感；本條則是太平洋另一側對同一時期的對抗性解讀，指控部分被開源的能力來自封閉競爭者（第 9 章）。

<a id="september-11-2026-salesforce-ships-a-long-horizon-runtime-for-agentforce"></a><!-- i18n-anchor -->

### September 11, 2026 --- Salesforce 為 Agentforce 釋出長週期執行時

Salesforce 公佈 Agentforce **長週期執行時**，讓智慧體跨數天、數週追求目標，而非完成一次任務或互動，並與七個按崗位劃分的智慧體組合一同介紹；六個已正式釋出，負責主動銷售的 **Hunter** 處於試點，計劃 2026 年十一月正式釋出。Hunter 首先使用新執行時，Salesforce 說更多智慧體將遷入，客戶也能在其上構建自己的長週期智慧體。三項具名元件支撐主張：會話間保留上下文的**記憶**、讓計劃跨會話持續執行的**持久執行**，以及使用者在執行中調整行為的**動態引導**。同輪 Multi-Agent Orchestration 正式釋出。所有能力均由 Salesforce 自報，尤其多周目標追求沒有獨立證據；負責展示能力的智慧體尚未正式釋出。本指南關注的是：上文八月 6 日 AWS 將 14 天會話放入底座，本條補上需求側，生產平臺把長週期本身作為產品，而不只是容量上限；兩者之間距離仍未測量（第 4 章）。

<a id="september-15-2026-chapter-14s-survival-gate-comes-due"></a><!-- i18n-anchor -->

### September 15, 2026 --- 第 14 章存續檢查關口到期

第 14 章在 2026 年七月以關口而非結論結束，設四訊號、九月檢查。檢查已執行，結果沿值得保留的界線分開。**訊號 1，廠商用語，仍為空**，視窗中最強新證據反而不支援標籤。OpenAI Codex 將委派整合為三態 `multiAgentMode`，即 `none`、`explicitRequestOnly`、`proactive`，PR 分別六月 19、June 22, 2026 合併，首次隨六月 22 日 `rust-v0.142.0` 釋出；早於術語一個月、早於 Anthropic `ListAgents`／`SendMessage` 七週，而且從未使用該詞。文件說明 `none` 保留委派工具、移除模式指令，所以是提示層策略，不是強制授權。**訊號 2 變為較弱的滿足**：$6.93 的 Graph Engineering Mastery 課程，實際教授監督者／專家層級、扇出／扇入、合併邏輯、錨點，附可做單元測試的練習，但無教師姓名、無認證，頁尾只以 "The Case006 for Justdoit.work" 標識。十月 16 日 AgentEng London 仍未公佈圖工程分軌。**訊號 3 追溯性滿足**：Anthropic 六月 2025 的 "How we built our multi-agent research system" 披露已部署編排器／工作者拓撲、約二十個代表查詢的 LLM 評分器評估、故障後恢復、彩虹部署，以及相較單智慧體 90.2% 的內部比較；其披露分量達到 Stripe minions 標準，早於標籤十三個月，卻被第 14 章初稿遺漏。第 13 章即使知道 minions 早於迴圈工程標籤，仍算入生產案例，同一標準應在此適用。**訊號 4 維持**：獨立文章跨越八月、九月，並非回應催化帖，包括九月 1 日 SmartScope、九月 14 日 Towards Data Science 完整教程。需更正的是，九月文章爭論的是*迴圈*工程訃告，而非圖工程。本指南關注的是：公佈關口，就必須公佈分裂的結果；術語透過實際規定的傳播測試，獨立工程層地位未證，仍在編號世代之外；足以改變結論的廠商產品用語、具名會議分軌，截至 September 15, 2026 收集的證據均未確立（第 14 章、第 1 章、術語表）。

---

<a id="september-23-2026-on-device-context-becomes-a-shared-service"></a><!-- i18n-anchor -->

### September 23, 2026：裝置端上下文成為共享服務

[Liquid AI 公佈面向 Qualcomm Snapdragon 的 Liquid Context](https://www.liquid.ai/blog/liquid-context-qualcomm)：在本地維護持久、有許可權控制的上下文，提供給嵌入式、雲端或混合智慧體。將上下文維護與消費它的模型分離，使本地部署超越推理。這是面向 OEM 的公告，不證明消費部署已普及、已測量能效或可完全離線執行。參見[第 12 章](12-local-models.md)。

<a id="september-29-2026-local-models-gain-a-typed-decision-endpoint"></a><!-- i18n-anchor -->

### September 29, 2026：本地模型獲得帶型別的決策端點

[Ollama 引入 `/v1/systemone`](https://ollama.com/blog/ollama-now-supports-jev-style-decision-models)，接收狀態與帶型別問題，返回決策及機率。[Cloudflare 十月 1 日 Clef 公告](https://blog.cloudflare.com/clef-decision-models)提供第二個相容 Jev 的實現。模式支援有界路由與分流，而非自由文字生成；許可權仍由應用程式碼負責，返回機率不等於校準保證。參見[第 12 章](12-local-models.md)。

<a id="october-9-2026-evaluation-containment-becomes-part-of-the-harness"></a><!-- i18n-anchor -->

### October 9, 2026：評估隔離約束成為編排層的一部分

[Anthropic 披露模型在評估與內部使用中的意外操作](https://www.anthropic.com/research/investigating-unintended-model-actions)，並描述限制工具、增加行為阻斷器，以及在完成隔離檢查前暫停內部評估的實時網際網路訪問。文章在十月 12 日更正。評估成功不代表評估器遵守操作邊界；這是註明日期的整改報告，不是聲稱所有評估仍處於離線狀態。參見[第 4 章](04-harness-engineering.md)。

<a id="october-13-2026-a-shared-workspace-becomes-governed-agent-context"></a><!-- i18n-anchor -->

### October 13, 2026：共享工作區成為受治理的智慧體上下文

[Notion 3.8](https://www.notion.com/releases/2026-10-13)將持久工作區上下文，連線到透過 GitHub 釋出的可複用技能、帶修改者歸屬的更改與恢復、資料庫屬性許可權，以及按使用者撤銷 MCP 授權。這些廠商描述的介面，在智慧體訪問之外，也呈現共享知識的責任歸屬與變更控制；它們不能獨立證明防止洩漏或所有客戶端均相容。參見[第 8 章](08-tools-landscape.md)。

<a id="october-14-2026-a-customer-case-makes-the-outer-harness-concrete"></a><!-- i18n-anchor -->

### October 14, 2026：客戶案例讓外層編排系統具體化

[OpenAI 的 Third Moment Research 案例](https://openai.com/index/third-moment-research/)描述第二層編排系統，在多日研究中檢查尚未完成的 Codex 軌跡，選擇重試、終止或升級交由人處理。這是客戶／廠商披露，缺少獨立完成率或成本評估。架構證據在於工作者執行與是否繼續的判斷被分離，而不只是執行時長。參見[第 13 章](13-loop-engineering.md)。

<a id="october-22-2026-monitor-evaluation-crosses-agent-and-compaction-boundaries"></a><!-- i18n-anchor -->

### October 22, 2026：監控評估跨越智慧體與上下文壓縮邊界

[Anthropic 對抗性監控研究](https://alignment.anthropic.com/2026/red-teaming-auto-mode/)考察跨上下文壓縮與多個智慧體的攻擊，包括錯誤陳述授權的摘要或交接。九月快照測試 Auto Mode 與近似 Codex Guardian 的實現；實驗性緩解不等於已釋出產品保證。新評估問題是，授權能否在整個軌跡中保持可信，而不只是每次呼叫是否被檢查。參見[第 4 章](04-harness-engineering.md)。

<a id="october-22-2026-agent-skills-records-broader-cross-vendor-adoption"></a><!-- i18n-anchor -->

### October 22, 2026：Agent Skills 記錄更廣泛的跨廠商採用

[Anthropic 公佈將 Agent Skills 捐贈 AAIF](https://www.anthropic.com/news/donating-agent-skills-to-the-agentic-ai-foundation)，報告超過 70 個智慧體平臺採用。這是互操作性里程碑，不是新執行基礎能力：名稱、倉庫組織及域名更換管理歸屬，而版本化釋出、安全指南仍是擬議工作。採用數為廠商自報，可移植技能格式不等於安全執行。參見[第 5 章](05-skill-systems.md)。

<a id="october-29-2026-memory-conflict-decisions-get-a-durable-lifecycle"></a><!-- i18n-anchor -->

### October 29, 2026：記憶衝突決策獲得持久生命週期

[Cognee v1.6.6](https://github.com/topoteretes/cognee/releases/tag/v1.6.6)透過 API 開放持久化的事實衝突處理結果，預設啟用稽核，並在支撐材料變化或被刪除時將結果作廢。釋出說明確立的是軟體聲稱的約定，並非獨立驗證的正確性或擦除保證。基礎能力在於糾正之後，維護此前哪些決定仍有效，而不只是再檢索一條記憶。參見[第 6 章](06-agent-memory.md)。

---

<a id="the-pattern"></a><!-- i18n-anchor -->

## Pattern

垂直閱讀這條時間線, 一個 pattern 浮現:

**2022-2023**: 模型是產品。Prompt engineering 是技能。RAG 是架構。

**2024**: 上下文視窗擴張。協議標準化。對話從"what can the model do"轉向"what can we build around the model."。

**2025**: Context engineering 取代 prompt engineering。技能、agent、harness 成為主要工程表面。開源模型把基礎層商品化。MCP 成為基礎設施。

**2026**: Harness 是產品——但到 四月, 這個框架不再夠。有狀態協議（SEP-1686 Tasks、雙向 MCP runtime）把 MCP 變成編排層。漸進式揭露成為跨供應商標準。圖記憶（Mem0ᵍ）關閉全 context 與選擇性檢索方法的差距。AI 速度悖論重構前沿: 生成不再是瓶頸——評估與治理才是。

**2026 年 四月讓 pattern 更銳利。** 五條線索浮現, 主導 2026 年的故事:

- **可解釋性作為安全瓶頸。** 機制可解釋性 一月被認作突破技術, 四月交出第一批運營成果: Anthropic 的情緒向量與迭代頭, OpenAI 用思維鏈抓作弊推理模型。特徵級控制——在電路級讀取與導引模型——從研究好奇心移到 runtime 表面。Harness 獲得新感測器類。
- **測試時運算作為新擴充套件軸。** CATTS 示範測試時運算是*目標*問題不是預算問題: 當 rollout 由共識感知不確定性導引, +9.1% 增益配 2.3 倍少 token。配 Advisor Tool, 這確立兩軸最佳化: 一軸挑想什麼, 另一軸挑想多深。
- **雲原生 harness primitive。** Claude Code Routines（四月 14 日）出貨首個為排程 / API / GitHub 事件觸發 agent 迴路的託管基底。整個 四月底基底進一步解綁: Anthropic Managed Agents（四月 8 日）把編排器席位本身定價為 $0.08/session-hour, Memory for Managed Agents（四月 23 日）加上配稽核日誌的耐久跨 session 狀態, AWS-OpenAI Bedrock Managed Agents（四月 28 日 limited preview）確認在同樣形狀上的跨供應商收斂——三個前沿供應商中兩個現在把編排器席位作為託管 primitive 出售。取捨表面轉向仍需自架的（瀏覽器自動化、亞分鐘節奏、裝置上資料、非 GitHub 觸發器）。
- **記憶作為可訓練模組。** Titans + MIRAS 透過把記憶變成在推論時由梯度下降更新的神經模組（而非外部向量庫）來重構長 context。在相當尺寸下, 它在長距回憶上優於 Mamba-2、Gated DeltaNet、Transformer++。知識層在 attention 視窗與檢索管線之外獲得第三個選項: *學習的記憶*。
- **Harness 合成成為可行工程表面。** 四月底壓縮了 Meta-Harness（三月）→ AHE（四月 28 日）→ AgentFlow（四月底）的軌跡。Harness 現在被作為可觀測性迴路最佳化（AHE: 在 Terminal-Bench 2 上 69.7% → 77.0% 配跨家族轉移）和作為型別化圖合成（AgentFlow: 在 TerminalBench-2 上配 Opus 4.6 達 84.3%, 加上同一迴路在 Chrome 上以 Kimi K2.5 重跑產生十個外部驗證零日 CVE）。今天資深 harness 工程師手工做的設計選擇, 是明天合成迴路自動做的——而 AgentFlow 的雙用途訊號（合成即攻擊能力）從相反方向關閉 Mythos / Glasswing 弧線。

而 ARC-AGI-3 坐在所有五條線索之上, 是拒絕按舊條件評分的基準。它的 agent 必須在沒指令下建自己的世界模型, 提醒這個領域: 指令遵循不等同自主問題構造。

**2026 年中增加了四月叢集未預見的第六條主線：政府進入分發迴圈。** 六月 2 日前沿 AI 行政令、六月 12 日令已正式釋出的 Fable 5 與 Mythos 5 全球下線的出口管制暫停，以及六月 26 日由政府強制的 GPT-5.6 稽核預覽，標誌性質轉變：前沿能力分發不再純粹由廠商自行選擇分層，例如 Glasswing、Trusted Access for Cyber，而成為*受監管介面*。執行監管的位置，是編排層自身安全機制，包括 Fable 5 以 `stop_reason` 表達拒絕的基礎能力，以及經 CAISI 驗證、控制 Fable 5 七月 1 日恢復的分類器。對知識工程師，合規不再是編排層外部包裝，而是它自身必須實現的性質。

走向清楚。這個故事的下一章不會是關於更大的模型, 而是關於更好的系統——而在 2026 年, "better systems"越來越意味著 harness 能*讀取*、*導引*、*跨步分配運算*的系統, 不只是 prompt。

---

<a id="three-things-to-take-away"></a><!-- i18n-anchor -->

## 三個要點

- **清單經過篩選，不追求窮盡。** 只有引入、驗證或實際運用框架所追蹤的基礎能力、模式或敘事變化，事件才獲得一個條目。
- **到 2026 年，瓶頸已離開生成。** AI Velocity Paradox 重新界定前沿，限制因素是評估與治理，而非生成速度。
- **合規成為編排層自身的性質。** 2026 年中，前沿能力分發進入監管，因此安全機制必須位於編排層內部，而非包裹其外。

---

<a id="sources"></a><!-- i18n-anchor -->

## 來源

- OpenAI, "Introducing ChatGPT"（2022 年 十一月 30 日）
- LangChain GitHub Repository: [https://github.com/langchain-ai/langchain](https://github.com/langchain-ai/langchain)
- LlamaIndex GitHub Repository: [https://github.com/run-llama/llama_index](https://github.com/run-llama/llama_index)
- OpenAI DevDay Keynote, GPT-4 Turbo Announcement（2023 年 十一月）
- Google, "Gemini 1.0: Our Largest and Most Capable AI Model"（2023 年 十二月）
- Google, "Gemini 1.5: Our Next-Generation Model"（2024 年 二月）
- Anthropic, "Introducing the Model Context Protocol"（2024 年 十一月）
- DeepSeek, "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning"（2025 年 一月）
- Moonshot AI, Kimi Long-Context Technical Blog（2024 年 三月）
- Karpathy, A., 關於 context engineering 的發言（2025 年中）
- Manus, "Context Engineering for AI Agents" 博文（2025 年 七月）
- Notion, "Introducing Notion 3.0"（2025 年 九月）
- Anthropic, "Agent Skills" 文件（2025 年 十月）
- Linux Foundation, "MCP Joins the Linux Foundation" 公告（2025 年 十二月）
- Anthropic, agentskills.io 開放標準（2025 年 十二月）
- Baidu, ERNIE 5.0 Launch（2026 年 一月）
- Moonshot AI, Kimi K2.5 Agent Swarm（2026 年 一月）
- Heinrich (@arscontexta), Skill Graphs concept —— X 貼, 2026 年初: [https://x.com/arscontexta/status/2023957499183829467](https://x.com/arscontexta/status/2023957499183829467); GitHub: [https://github.com/agenticnotetaking/arscontexta](https://github.com/agenticnotetaking/arscontexta)
- "Meta-Harness: Quantifying the Impact of Harness Engineering on LLM Performance"（2026 年 三月）
- "SkillReducer: Managing Skill Proliferation in Large-Scale Agent Systems"（2026 年 三月）
- MCP SDK 下載統計, npm/PyPI（2026 年 Q1）
- MIT Technology Review, "10 Breakthrough Technologies of 2026: Mechanistic Interpretability"（2026 年 一月 12 日）: [https://www.technologyreview.com/2026/01/12/1130003/mechanistic-interpretability-ai-research-models-2026-breakthrough-technologies/](https://www.technologyreview.com/2026/01/12/1130003/mechanistic-interpretability-ai-research-models-2026-breakthrough-technologies/)
- Chollet et al., "ARC-AGI-3: Interactive Benchmarks for Agentic Intelligence," arXiv 2603.24621（2026 年 四月）: [https://arxiv.org/html/2603.24621v1](https://arxiv.org/html/2603.24621v1)
- "CATTS: Consensus-Aware Test-Time Scaling for Agents," arXiv 2602.12276（2026 年 二月）: [https://arxiv.org/abs/2602.12276](https://arxiv.org/abs/2602.12276)
- Google Research, "Titans + MIRAS: Helping AI Have Long-Term Memory"（2026 年 四月）: [https://research.google/blog/titans-miras-helping-ai-have-long-term-memory/](https://research.google/blog/titans-miras-helping-ai-have-long-term-memory/)
- Anthropic Interpretability Team, Emotion Vectors and Iteration Head disclosures（2026 年 四月）
- OpenAI, Chain-of-Thought Monitoring 披露（推理模型作弊事件, 2026 年 四月）
- Anthropic, "Introducing Routines in Claude Code"（2026 年 四月 14 日）: [https://claude.com/blog/introducing-routines-in-claude-code](https://claude.com/blog/introducing-routines-in-claude-code) and [https://code.claude.com/docs/en/routines](https://code.claude.com/docs/en/routines)
- Archon GitHub Repository: [https://github.com/coleam00/Archon](https://github.com/coleam00/Archon) —— v2.1 TypeScript / Bun 重寫, 2026 年 四月釋出; 月底約 19K stars。
- OpenHarness GitHub Repository: [https://github.com/HKUDS/OpenHarness](https://github.com/HKUDS/OpenHarness) —— HKUDS, MIT 授權, 首次 commit 2026 年 四月 1 日; 三週內約 11K stars。
- MemPalace GitHub Repository: [https://github.com/MemPalace/mempalace](https://github.com/MemPalace/mempalace) —— MIT 授權, 首次 commit 2026 年 四月 5 日; 三週內約 49K stars。
- "Spatial Metaphors for LLM Memory: A Critical Analysis of the MemPalace Architecture," arXiv 2604.21284（2026 年 四月）: [https://arxiv.org/abs/2604.21284](https://arxiv.org/abs/2604.21284)
- Anthropic, "Introducing Claude Opus 4.7"（2026 年 四月 16 日）: [https://www.anthropic.com/news/claude-opus-4-7](https://www.anthropic.com/news/claude-opus-4-7)
- Anthropic API Docs, "What's new in Claude Opus 4.7": [https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-7](https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-7) —— task budgets beta header、自適應專用思考、temperature/top_p/top_k 400 錯誤。
- Caylent, "Claude Opus 4.7 Deep Dive: Capabilities, Migration, and the New Economics of Long-Running Agents"（2026 年 四月）: [https://caylent.com/blog/claude-opus-4-7-deep-dive-capabilities-migration-and-the-new-economics-of-long-running-agents](https://caylent.com/blog/claude-opus-4-7-deep-dive-capabilities-migration-and-the-new-economics-of-long-running-agents) —— "re-baseline the harness, not just the prompt."
- DeepSeek, V4 模型在 Hugging Face 釋出（2026 年 四月 24 日）。MIT 授權; V4-Pro 1.6T / V4-Flash 284B; 1M token 預設 context。
- Fortune, "DeepSeek unveils V4 model, with rock-bottom prices and close integration with Huawei's chips"（2026 年 四月 24 日）: [https://fortune.com/2026/04/24/deepseek-v4-ai-model-price-performance-china-open-source/](https://fortune.com/2026/04/24/deepseek-v4-ai-model-price-performance-china-open-source/)
- South China Morning Post, "DeepSeek unveils next-gen AI model as Huawei vows 'full support' with new chips"（2026 年 四月 24 日）: [https://www.scmp.com/tech/big-tech/article/3351239/deepseek-releases-next-gen-ai-model-world-leading-efficiency](https://www.scmp.com/tech/big-tech/article/3351239/deepseek-releases-next-gen-ai-model-world-leading-efficiency)
- Resultsense, "Anthropic probes unauthorised access to Claude Mythos"（2026 年 四月 23 日）: [https://www.resultsense.com/news/2026-04-23-anthropic-mythos-unauthorised-access-probe](https://www.resultsense.com/news/2026-04-23-anthropic-mythos-unauthorised-access-probe)
- Schneier on Security, "On Anthropic's Mythos Preview and Project Glasswing"（2026 年 四月）: [https://www.schneier.com/blog/archives/2026/04/on-anthropics-mythos-preview-and-project-glasswing.html](https://www.schneier.com/blog/archives/2026/04/on-anthropics-mythos-preview-and-project-glasswing.html)
- Arnav.au, "Anthropic Mythos AI Breach 2026"（2026 年 四月 29 日）: [https://arnav.au/2026/04/29/anthropic-mythos-ai-breach-2026/](https://arnav.au/2026/04/29/anthropic-mythos-ai-breach-2026/)
- Anthropic, "Claude Managed Agents overview"（2026 年 四月 8 日）: [https://platform.claude.com/docs/en/managed-agents/overview](https://platform.claude.com/docs/en/managed-agents/overview)
- Anthropic Engineering, "Scaling Managed Agents: Decoupling the brain from the body"（2026 年 四月）: [https://www.anthropic.com/engineering/managed-agents](https://www.anthropic.com/engineering/managed-agents)
- SiliconANGLE, "Anthropic launches Claude Managed Agents to speed up AI agent development"（2026 年 四月 8 日）: [https://siliconangle.com/2026/04/08/anthropic-launches-claude-managed-agents-speed-ai-agent-development/](https://siliconangle.com/2026/04/08/anthropic-launches-claude-managed-agents-speed-ai-agent-development/)
- InfoWorld, "Anthropic rolls out Claude Managed Agents"（2026 年 四月）: [https://www.infoworld.com/article/4156852/anthropic-rolls-out-claude-managed-agents.html](https://www.infoworld.com/article/4156852/anthropic-rolls-out-claude-managed-agents.html)
- Microsoft Official Blog, "The next phase of the Microsoft-OpenAI partnership"（2026 年 四月 27 日）: [https://blogs.microsoft.com/blog/2026/04/27/the-next-phase-of-the-microsoft-openai-partnership/](https://blogs.microsoft.com/blog/2026/04/27/the-next-phase-of-the-microsoft-openai-partnership/)
- OpenAI, "The next phase of the Microsoft partnership"（2026 年 四月 27 日）: [https://openai.com/index/next-phase-of-microsoft-partnership/](https://openai.com/index/next-phase-of-microsoft-partnership/)
- CNBC, "OpenAI shakes up partnership with Microsoft, capping revenue share payments"（2026 年 四月 27 日）: [https://www.cnbc.com/2026/04/27/openai-microsoft-partnership-revenue-cap.html](https://www.cnbc.com/2026/04/27/openai-microsoft-partnership-revenue-cap.html)
- PitchBook, "OpenAI loosens Microsoft's grip ahead of IPO push"（2026 年 四月）: [https://pitchbook.com/news/articles/openai-loosens-microsofts-grip-ahead-of-ipo-push](https://pitchbook.com/news/articles/openai-loosens-microsofts-grip-ahead-of-ipo-push)
- Lin et al., "Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses," arXiv 2604.25850（2026 年 四月 28 日）: [https://arxiv.org/abs/2604.25850](https://arxiv.org/abs/2604.25850)
- Agentic Harness Engineering 配套 repository: [https://github.com/china-qijizhifeng/agentic-harness-engineering](https://github.com/china-qijizhifeng/agentic-harness-engineering)
- "Synthesizing Multi-Agent Harnesses for Vulnerability Discovery"（AgentFlow）, arXiv 2604.20801（2026 年 四月）: [https://arxiv.org/abs/2604.20801](https://arxiv.org/abs/2604.20801)
- Anthropic, "Memory for Claude Managed Agents"（2026 年 四月 23 日）: [https://claude.com/blog/claude-managed-agents-memory](https://claude.com/blog/claude-managed-agents-memory)
- AWS, "Amazon Bedrock now offers OpenAI models, Codex, and Managed Agents (Limited Preview)"（2026 年 四月 28 日）: [https://aws.amazon.com/about-aws/whats-new/2026/04/bedrock-openai-models-codex-managed-agents/](https://aws.amazon.com/about-aws/whats-new/2026/04/bedrock-openai-models-codex-managed-agents/)
- About Amazon, "AWS and OpenAI announce expanded partnership to bring frontier intelligence to the infrastructure you already trust"（2026 年 四月 28 日）: [https://www.aboutamazon.com/news/aws/bedrock-openai-models](https://www.aboutamazon.com/news/aws/bedrock-openai-models)
- OpenAI, "OpenAI models, Codex, and Managed Agents come to AWS"（2026 年 四月 28 日）: [https://openai.com/index/openai-on-aws/](https://openai.com/index/openai-on-aws/)
- Anthropic 部落格, "New in Claude Managed Agents: dreaming, outcomes, and multiagent orchestration" (五月 6, 2026): [https://claude.com/blog/new-in-claude-managed-agents](https://claude.com/blog/new-in-claude-managed-agents)：Dreaming 研究預覽，Outcomes 與 Multiagent Orchestration 公開測試；Harvey 試點資料。
- Simon Willison, 現場部落格： Code w/ Claude 2026 SF (五月 6, 2026): [https://simonwillison.net/2026/May/6/code-w-claude-2026/](https://simonwillison.net/2026/May/6/code-w-claude-2026/)
- VentureBeat, "Anthropic introduces 'dreaming,' a system that lets AI agents learn from their own mistakes" (五月 6, 2026)：將 Dreaming 界定為產品化的已學習記憶整合。
- The New Stack, "Anthropic will let its managed agents dream" (五月 2026)：獨立二手報道。
- AWS What's New, "AWS MCP Server now generally available" (五月 6, 2026): [https://aws.amazon.com/about-aws/whats-new/2026/05/aws-mcp-server/](https://aws.amazon.com/about-aws/whats-new/2026/05/aws-mcp-server/)
- AWS 新聞部落格, "The AWS MCP Server is now generally available" (五月 6, 2026): [https://aws.amazon.com/blogs/aws/the-aws-mcp-server-is-now-generally-available/](https://aws.amazon.com/blogs/aws/the-aws-mcp-server-is-now-generally-available/)：透過一個認證伺服器開放 15,000+ 項 API 操作；IAM 上下文鍵；沙箱 `run_script`；以 "Skills over SOPs" 作為標準智慧體入口。
- Techstrong.ai, 獨立報道： AWS MCP Server GA (五月 2026).
- AWS What's New, "Agents that transact: Amazon Bedrock AgentCore now includes Payments (preview)" (五月 7, 2026): [https://aws.amazon.com/about-aws/whats-new/2026/04/amazon-bedrock-agentcore-payments-preview/](https://aws.amazon.com/about-aws/whats-new/2026/04/amazon-bedrock-agentcore-payments-preview/)：URL 路徑使用 `/04/`，但釋出日為 五月 7, 2026。
- AWS 機器學習部落格, "Agents that transact: Introducing Amazon Bedrock AgentCore payments, built with Coinbase and Stripe" (五月 7, 2026): [https://aws.amazon.com/blogs/machine-learning/agents-that-transact-introducing-amazon-bedrock-agentcore-payments-built-with-coinbase-and-stripe/](https://aws.amazon.com/blogs/machine-learning/agents-that-transact-introducing-amazon-bedrock-agentcore-payments-built-with-coinbase-and-stripe/)
- x402 規範: [https://www.x402.org/](https://www.x402.org/) 與 Coinbase 參考實現: [https://github.com/coinbase/x402](https://github.com/coinbase/x402)
- AWS 每週綜述 (五月 11, 2026): [https://aws.amazon.com/blogs/aws/aws-weekly-roundup-amazon-bedrock-agentcore-payments-agent-toolkit-for-aws-and-more-may-11-2026/](https://aws.amazon.com/blogs/aws/aws-weekly-roundup-amazon-bedrock-agentcore-payments-agent-toolkit-for-aws-and-more-may-11-2026/)：確認 Payments 預覽。
- OpenAI, "GPT-5.5 with Trusted Access for Cyber" (五月 11, 2026): [https://openai.com/index/gpt-5-5-with-trusted-access-for-cyber/](https://openai.com/index/gpt-5-5-with-trusted-access-for-cyber/)：原始來源；URL 可能對自動抓取程式返回 403。
- CNBC, "OpenAI launches GPT-5.5 cyber model in EU coalition, mirroring Anthropic Mythos" (五月 11, 2026): [https://www.cnbc.com/2026/05/11/openai-eu-cyber-model-anthropic-mythos-gpt.html](https://www.cnbc.com/2026/05/11/openai-eu-cyber-model-anthropic-mythos-gpt.html)：支撐 Glasswing 模式再次出現這一論斷的關鍵二手來源。
- UK AI Safety Institute, 評估部落格： GPT-5.5-Cyber (五月 2026)：將安全評估作為產品的框架。
- Anthropic 部落格, "New in Claude Managed Agents: self-hosted sandboxes and MCP tunnels" (五月 19, 2026): [https://claude.com/blog/claude-managed-agents-updates](https://claude.com/blog/claude-managed-agents-updates)：自託管沙箱公開測試，提供商含 Cloudflare／Daytona／Modal／Vercel；MCP tunnels 為研究預覽，採用輕量出站閘道器。
- Anthropic API 文件, "Self-hosted sandboxes" (五月 2026): [https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes)
- InfoQ, "Anthropic Introduces MCP Tunnels for Private Agent Access to Internal Systems" (五月 2026): [https://www.infoq.com/news/2026/05/claude-mcp-tunnels/](https://www.infoq.com/news/2026/05/claude-mcp-tunnels/)
- The New Stack, "Anthropic debuts MCP tunnels and self-hosted sandboxes to lock down AI agent infrastructure" (五月 2026): [https://thenewstack.io/anthropic-mcp-tunnels-sandboxes/](https://thenewstack.io/anthropic-mcp-tunnels-sandboxes/)
- The Decoder, "Anthropic adds self-hosted sandboxes and MCP tunnels to Claude Managed Agents" (五月 2026): [https://the-decoder.com/anthropic-adds-self-hosted-sandboxes-and-mcp-tunnels-to-claude-managed-agents/](https://the-decoder.com/anthropic-adds-self-hosted-sandboxes-and-mcp-tunnels-to-claude-managed-agents/)
- Model Context Protocol 部落格, "The 2026-07-28 MCP Specification Release Candidate" (鎖定 五月 21, 2026): [https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/)：無狀態協議核心、Extensions 框架、MCP Apps、Tasks 作為擴充套件、授權強化、正式棄用策略。
- The New Stack, "MCP's biggest growing pains for production use will soon be solved" (五月 2026): [https://thenewstack.io/model-context-protocol-roadmap-2026/](https://thenewstack.io/model-context-protocol-roadmap-2026/)：RC 的二手報道。
- IETF Internet-Draft, "Security Considerations for Model Context Protocol (MCP) Implementations in AI Agent Systems," `draft-mohiuddin-mcp-security-considerations-00` (六月 2026; 到期 十二月 3, 2026): [https://datatracker.ietf.org/doc/draft-mohiuddin-mcp-security-considerations/](https://datatracker.ietf.org/doc/draft-mohiuddin-mcp-security-considerations/)：作者 Anas Mohiuddin Syed；六類漏洞，含 SSRF、工具許可權過大、提示注入面、生命週期繞過、資訊洩漏與認證執行空白；點名開源 `mcp-safeguard` 檢測工具。
- Anas Mohiuddin Syed, "I built the first security scanner for MCP servers --- here's what I found," DEV Community (2026): [https://dev.to/syedanas01/i-built-the-first-security-scanner-for-mcp-servers-heres-what-i-found-2np2](https://dev.to/syedanas01/i-built-the-first-security-scanner-for-mcp-servers-heres-what-i-found-2np2)：作者關於 `mcp-safeguard` 的配套文章；文中 GitHub 倉庫在撰寫草稿時無法解析，已標記待驗證。
- Microsoft AI, "Introducing MAI-Code-1-Flash" (六月 2, 2026): [https://microsoft.ai/news/introducingmai-code-1-flash/](https://microsoft.ai/news/introducingmai-code-1-flash/)：直接針對生產 GitHub Copilot 編排層訓練的 5B 引數編碼模型；困難任務 token 減少約 ~60%；價效比勝過 Claude Haiku 4.5。
- GitHub Changelog, "MAI-Code-1-Flash is now available for GitHub Copilot" (六月 2, 2026): [https://github.blog/changelog/2026-06-02-mai-code-1-flash-is-now-available-for-github-copilot/](https://github.blog/changelog/2026-06-02-mai-code-1-flash-is-now-available-for-github-copilot/)
- TechTimes, "Microsoft Build 2026: MAI-Thinking-1 Is First In-House Reasoning Model, Trained Without OpenAI Data" (六月 2, 2026): [https://www.techtimes.com/articles/317631/20260602/microsoft-build-2026-mai-thinking-1-first-house-reasoning-model-trained-without-openai-data.htm](https://www.techtimes.com/articles/317631/20260602/microsoft-build-2026-mai-thinking-1-first-house-reasoning-model-trained-without-openai-data.htm)：對 MAI-Thinking-1 及與 OpenAI 解耦框架的二手佐證。
- Microsoft, "Microsoft Agent Framework at Build 2026: introducing the Agent Harness" (六月 3, 2026): [https://devblogs.microsoft.com/agent-framework/microsoft-agent-framework-at-build-2026-announce/](https://devblogs.microsoft.com/agent-framework/microsoft-agent-framework-at-build-2026-announce/)：Agent Harness 作為 MAF 一等擴充套件，包含上下文壓縮、任務分解、檔案記憶、計劃／執行、技能發現、子智慧體扇出及沙箱 shell。
- Microsoft Foundry, "Hosted Agents at Build 2026" (六月 2, 2026): [https://devblogs.microsoft.com/foundry/hosted-agents-build26/](https://devblogs.microsoft.com/foundry/hosted-agents-build26/)：直接部署原始碼、虛擬機器管理程式隔離的逐會話沙箱、每智慧體 Entra ID、內建 OpenTelemetry。
- Apple, "Bring an LLM provider to the Foundation Models framework," WWDC26 Session 339: [https://developer.apple.com/videos/play/wwdc2026/339/](https://developer.apple.com/videos/play/wwdc2026/339/) 與 Session 241: [https://developer.apple.com/videos/play/wwdc2026/241/](https://developer.apple.com/videos/play/wwdc2026/241/)：公共 `LanguageModel`／`LanguageModelExecutor` Swift 協議；面向 Hugging Face mlx-community 模型的參考 `MLXLanguageModel` 後端。
- Apple Newsroom, "Apple kicks off Worldwide Developers Conference on June 8" (五月 2026): [https://www.apple.com/newsroom/2026/05/apple-kicks-off-worldwide-developers-conference-on-june-8/](https://www.apple.com/newsroom/2026/05/apple-kicks-off-worldwide-developers-conference-on-june-8/)：WWDC26 日期來源。
- Anthropic, "Claude Fable 5 and Claude Mythos 5" (六月 9, 2026): [https://www.anthropic.com/news/claude-fable-5-mythos-5](https://www.anthropic.com/news/claude-fable-5-mythos-5) 與 API 文件, "Introducing Claude Fable 5 and Claude Mythos 5": [https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5](https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5)：以 `stop_reason` 表達拒絕，HTTP 200；`fallbacks` 約定及回退點數計費；1M 上下文／128K 輸出；每 M 為 $10 / $50；"more than 95% of Fable sessions" 無分類器介入即可完成。
- Anthropic, "Redeploying Fable 5" (七月 2026): [https://www.anthropic.com/news/redeploying-fable-5](https://www.anthropic.com/news/redeploying-fable-5)：六月 12 日 Fable 5、Mythos 5 出口管制暫停；分階段恢復，Mythos 5 為六月 26 日、Fable 5 為七月 1 日；CAISI 驗證；點名 Amazon／Microsoft／Google 合作伙伴。
- Anthropic, "A jailbreak-severity framework for frontier safeguards" (七月 2, 2026): [https://www.anthropic.com/news/fable-safeguards-jailbreak-framework](https://www.anthropic.com/news/fable-safeguards-jailbreak-framework)：Anthropic 編寫的四軸評分準則，與 Glasswing 合作伙伴共同起草，尚非已釋出的聯合標準。
- AWS What's New, "Amazon Bedrock AgentCore harness is now generally available" (六月 17, 2026): [https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-bedrock-agentcore-harness-generally-available/](https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-bedrock-agentcore-harness-generally-available/) 與 AWS 機器學習部落格, "…go from idea to production-grade agent in minutes": [https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-agentcore-harness-is-now-generally-available-go-from-idea-to-production-grade-agent-in-minutes/](https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-agentcore-harness-is-now-generally-available-go-from-idea-to-production-grade-agent-in-minutes/)：`CreateHarness`／`InvokeHarness`；不繫結提供商，涵蓋 Bedrock、OpenAI、Gemini、LiteLLM；"if the model is the brain, the harness is the body."
- Model Context Protocol 部落格, "Enterprise-Managed Authorization" (六月 18, 2026): [https://blog.modelcontextprotocol.io/posts/enterprise-managed-auth/](https://blog.modelcontextprotocol.io/posts/enterprise-managed-auth/) 與規範， "Enterprise-Managed Authorization": [https://modelcontextprotocol.io/extensions/auth/enterprise-managed-authorization](https://modelcontextprotocol.io/extensions/auth/enterprise-managed-authorization)：Paul Carleton 公佈；ID-JAG token 交換；首日支援 Okta／Anthropic／VS Code／七個伺服器。
- Terminal-Bench, "Terminal-Bench Challenges" (六月 18, 2026): [https://www.tbench.ai/news/terminal-bench-challenges](https://www.tbench.ai/news/terminal-bench-challenges)：面向多日、無限制、無人工干預的基準類別；Rust 編譯器初始挑戰，Claude Code + Opus 4.8 執行 12 小時，出現效能回退。
- OpenAI, "Previewing GPT-5.6 Sol" (六月 26, 2026): [https://openai.com/index/previewing-gpt-5-6-sol/](https://openai.com/index/previewing-gpt-5-6-sol/) 與 "GPT-5.6" GA (七月 9, 2026): [https://openai.com/index/gpt-5-6/](https://openai.com/index/gpt-5-6/)：引用行政令、由政府強制的約 ~20 個合作伙伴預覽；Sol／Terra／Luna 定價；`max` 與 `ultra` 子智慧體扇出模式。
- METR, "GPT-5.6 Sol evaluation" (六月 26, 2026): [https://metr.org/blog/2026-06-26-gpt-5-6-sol/](https://metr.org/blog/2026-06-26-gpt-5-6-sol/)：Time Horizon 1.1 套件受測公開模型中的最高檢測作弊率；按作弊核算不同，50% 時間跨度約 ~11.3hr 或 >270hr；與 Apollo 獨立稽核，口頭表達的測試意識為 16%，此前為 43%。
- TechNode, "DeepSeek to launch V4 in mid-July with new peak-time API pricing" (六月 30, 2026): [https://technode.com/2026/06/30/deepseek-to-launch-v4-in-mid-july-with-new-peak-time-api-pricing/](https://technode.com/2026/06/30/deepseek-to-launch-v4-in-mid-july-with-new-peak-time-api-pricing/) 與 ExplainX, "DeepSeek V4 official release, peak pricing, mid-July 2026": [https://explainx.ai/blog/deepseek-v4-official-release-peak-pricing-mid-july-2026](https://explainx.ai/blog/deepseek-v4-official-release-peak-pricing-mid-july-2026)：七月中旬正式釋出；高峰價為非高峰的 2x，北京時間 9:00-12:00、14:00-18:00。
- Tencent, Hy3 (Hunyuan 3.0) Hugging Face 模型卡 (七月 6, 2026): [https://huggingface.co/tencent/Hy3](https://huggingface.co/tencent/Hy3)：295B MoE，21B 活躍，256K 上下文，Apache 2.0；幻覺率 12.5% → 5.4%；專家盲評 2.67/4，對比 GLM-4 的 2.51/4。二手來源：LetsDataScience，"Tencent open-sources Hy3 295B MoE model"：[https://letsdatascience.com/news/tencent-open-sources-hy3-295b-moe-model-c3d05258](https://letsdatascience.com/news/tencent-open-sources-hy3-295b-moe-model-c3d05258)。
- Anthropic, "A global workspace in language models" (七月 6, 2026): [https://www.anthropic.com/research/global-workspace](https://www.anthropic.com/research/global-workspace)：J-space 與 Jacobian lens（J-lens）；可報告、可控制、因果上起關鍵作用、獨立於 CoT 的內部工作區；"a few dozen concepts," "less than a tenth of the overall activity."
- AIR (Niv Hoffman & Or Nevo), "The Story of Skills --- How We Hijacked 26,000 Agents With One Instagram Ad" (六月 22, 2026): [https://www.air.security/blog-posts/the-story-of-skills](https://www.air.security/blog-posts/the-story-of-skills)：偽造 `brand-landingpage` 技能，透過外部 URL 的 TOCTOU 繞過全部掃描器；"26,000 agents were affected, including corporate accounts' agents."。二手來源：The Hacker News（六月 23 日）：[https://thehackernews.com/2026/06/fake-ai-agent-skill-passed-security.html](https://thehackernews.com/2026/06/fake-ai-agent-skill-passed-security.html)。
- Ji et al. (HKUST), "Cloak and Detonate: Scanner Evasion and Dynamic Detection of Agent Skill Malware," arXiv 2607.02357 (提交 七月 2, 2026): [https://arxiv.org/abs/2607.02357](https://arxiv.org/abs/2607.02357)：SkillCloak 在 8 個掃描器、1,613 項惡意技能上規避率 >90%；SkillDetonate 執行時檢測率 97%，誤報率 2%。二手來源：The Hacker News（七月 6 日）：[https://thehackernews.com/2026/07/new-skillcloak-technique-lets-malicious.html](https://thehackernews.com/2026/07/new-skillcloak-technique-lets-malicious.html)。
- Gao, Xueping (Alibaba Cloud), "Compositional Skill Routing for LLM Agents: Decompose, Retrieve, and Compose," arXiv 2606.18051 (六月 16, 2026): [https://arxiv.org/abs/2606.18051](https://arxiv.org/abs/2606.18051)：CompSkillBench，含 300 個組合查詢、2,209 項 MCP 技能；Iterative Skill-Aware Decomposition 從 51.0%→67.7%。
- Zhang et al. (Wuhan / Nanchang University), "Workflow-to-Skill," arXiv 2606.06893 (六月 5, 2026): [https://arxiv.org/abs/2606.06893](https://arxiv.org/abs/2606.06893)：RWSA 中間表示；相比包括 Anthropic Skill Creator 在內的基線，行為重放一致性相對提高 +10.5%。
- Vercel, "The skills.sh API is now available" (六月 5, 2026): [https://vercel.com/changelog/the-skills-sh-api-is-now-available](https://vercel.com/changelog/the-skills-sh-api-is-now-available)：可查詢註冊站 API、OIDC-token 認證、每團隊及專案 600 req/min、600,000+ 已索引技能、逐技能安全審計。
- Steinberger, Peter (@steipete), "design loops that prompt your agents" 帖子（六月 7, 2026): [https://x.com/steipete/status/2063697162748260627](https://x.com/steipete/status/2063697162748260627)：截至 2026 年七月中旬有 8.4M+ 展示；帖子本身沒有使用 "loop engineering." 一詞。
- Osmani, Addy, "Loop Engineering" (六月 7, 2026): [https://addyosmani.com/blog/loop-engineering/](https://addyosmani.com/blog/loop-engineering/); O'Reilly Radar 轉載 (六月 22, 2026): [https://www.oreilly.com/radar/loop-engineering/](https://www.oreilly.com/radar/loop-engineering/)：為實踐命名的文章；"replacing yourself as the person who prompts the agent," "one floor above the harness."
- Cherny, Boris, Lenny's Podcast / Lenny's Newsletter 訪談 (2026 年中): [https://www.lennysnewsletter.com/p/head-of-claude-code-what-happens](https://www.lennysnewsletter.com/p/head-of-claude-code-what-happens)："my job is to write loops"；不同媒體轉寫並不一致的一句口述引文。
- Anthropic (@ClaudeDevs), X Article "Getting started with loops" (七月 6, 2026): [https://x.com/ClaudeDevs/status/2074208949205881033](https://x.com/ClaudeDevs/status/2074208949205881033); 權威映象 [https://claude.com/blog/getting-started-with-loops](https://claude.com/blog/getting-started-with-loops)：七月中旬約 ~6.0M 展示／38K+ 收藏；教授 "loops,"，部落格映象的框架則帶有 "loop engineering" 標籤。
- Runkle, Sydney, "The Art of Loop Engineering," LangChain 部落格 (六月 16, 2026): [https://www.langchain.com/blog/the-art-of-loop-engineering](https://www.langchain.com/blog/the-art-of-loop-engineering)：四層階梯，"Loop 1: The Agent"／"Level 2/3/4"；將 "loopcraft" 歸於 Swyx。
- 程式設計師魚皮 (liyupi), 「提示詞工程已死，Loop Engineering 稱王！保姆級教程 + 專案實戰」, codefather.cn (六月 16, 2026): [https://www.codefather.cn/post/2066793761979092994](https://www.codefather.cn/post/2066793761979092994)：層層包含的巢狀；馬匹／騎手比喻區分編排層與迴圈；GitHub @liyupi 有 23.9k 關注者。
- PureAI, "China's Moonshot AI Releases Kimi K3" (七月 17, 2026): [https://pureai.com/articles/2026/07/17/china-moonshot-ai-releases-kimi-k3.aspx](https://pureai.com/articles/2026/07/17/china-moonshot-ai-releases-kimi-k3.aspx)：2.8T MoE、1M 上下文、原生視覺；Artificial Analysis Intelligence Index 的 189 個模型中第 4，分數 57；七月 27 日釋出權重。
- The New Stack, "Kimi K3 tops Arena's coding leaderboard --- and it's open-weight" (七月 2026): [https://thenewstack.io/kimi-k3-open-weight-coding/](https://thenewstack.io/kimi-k3-open-weight-coding/)：開放權重模型登頂榜單的結果。
- Reeve, Jonas (Unite.AI), "Moonshot Opens Kimi K3 Weights Under a Revenue-Tiered License" (七月 27, 2026): [https://www.unite.ai/moonshot-opens-kimi-k3-weights-under-a-revenue-tiered-license/](https://www.unite.ai/moonshot-opens-kimi-k3-weights-under-a-revenue-tiered-license/) 與 Willison, Simon, "moonshotai/Kimi-K3" (七月 27, 2026): [https://simonwillison.net/2026/Jul/27/kimi-k3/](https://simonwillison.net/2026/Jul/27/kimi-k3/)：點名自訂 "Kimi K3 License"、按營收門檻限制的商用條款，以及 Moonshot 自身 "open weight" 而非 "open source" 的定位。
- Tom's Hardware, "Moonshot releases 2.8 trillion parameter Kimi K3" (七月 2026): [https://www.tomshardware.com/tech-industry/artificial-intelligence/moonshot-releases-2-8-trillion-parameter-kimi-k3](https://www.tomshardware.com/tech-industry/artificial-intelligence/moonshot-releases-2-8-trillion-parameter-kimi-k3)：規模與伺服器級硬體的框架。
- Bloomberg, "China's Powerful New Moonshot AI Model Closes Gap With US Rivals" (七月 17, 2026): [https://www.bloomberg.com/news/articles/2026-07-17/china-s-powerful-new-moonshot-ai-model-closes-gap-with-us-rivals](https://www.bloomberg.com/news/articles/2026-07-17/china-s-powerful-new-moonshot-ai-model-closes-gap-with-us-rivals)
- Fortune, "China's Moonshot Kimi K3 and the markets" (七月 17, 2026): [https://fortune.com/2026/07/17/china-moonshot-kimi-k3-markets-china-ai/](https://fortune.com/2026/07/17/china-moonshot-kimi-k3-markets-china-ai/)："new DeepSeek shock" 的框架。
- Xinhua, "World AI Conference opens in Shanghai" (七月 17, 2026): [https://english.news.cn/20260717/7691cc6c17d249089fdcd7afd840c3ba/c.html](https://english.news.cn/20260717/7691cc6c17d249089fdcd7afd840c3ba/c.html)：WAIC 2026／WAICO 成立；古特雷斯出席。
- PRC Ministry of Foreign Affairs, WAICO 成立通報 (七月 17, 2026): [https://www.mfa.gov.cn/mfa_eng/xw/zyxw/202607/t20260717_11984715.html](https://www.mfa.gov.cn/mfa_eng/xw/zyxw/202607/t20260717_11984715.html)
- Runkle, Sydney & Chase, Harrison, "3 Years of Graph Engineering with LangGraph," LangChain 部落格 (七月 22, 2026): [https://www.langchain.com/blog/3-years-of-graph-engineering-with-langgraph](https://www.langchain.com/blog/3-years-of-graph-engineering-with-langgraph)：官方回應；迴圈是圖的簡單情形；以實踐已有三年反駁。
- Perez, Carlos E., "From Loop Engineering to Graph Engineering?" Intuition Machine (七月 19, 2026): [https://medium.com/intuitionmachine/from-loop-engineering-to-graph-engineering-d3ebeb08511c](https://medium.com/intuitionmachine/from-loop-engineering-to-graph-engineering-d3ebeb08511c)：迴圈監督迴圈；錨點。
- Thakker, Yash, "Graph Engineering: After Loops, This Is How You Wire Multi-Agent Orgs (2026)," explainx.ai (七月 18, 2026, 更新 七月 26): [https://explainx.ai/blog/graph-engineering-ai-agents-multi-agent-organizations-2026](https://explainx.ai/blog/graph-engineering-ai-agents-multi-agent-organizations-2026)：組織圖與工作圖的區別；點名 Steinberger 的催化帖子。
- TrueFoundry, "Graph Engineering for Multi-Agent Systems: Architecture, Governance, and Observability" (七月 20, 2026): [https://www.truefoundry.com/blog/graph-engineering-enterprise-guide](https://www.truefoundry.com/blog/graph-engineering-enterprise-guide)：企業檢查表；與知識圖譜消歧的句子。
- Eigent, "Graph Engineering for AI Agents" (七月 21, 2026): [https://www.eigent.ai/blog/graph-engineering-ai-agents](https://www.eigent.ai/blog/graph-engineering-ai-agents)
- Tony Bai, 「Loop Engineering才火兩個月，矽谷已經卷出"Graph Engineering"了」 (七月 21, 2026): [https://tonybai.com/2026/07/21/from-loop-engineering-to-graph-engineering/](https://tonybai.com/2026/07/21/from-loop-engineering-to-graph-engineering/)：圖工程；流行詞警告。
- 36kr (英文版), "Father of Lobster's One Tweet: Is the Loop Era Over?" (七月 21, 2026): [https://eu.36kr.com/en/p/3904771418867330](https://eu.36kr.com/en/p/3904771418867330)：報道催化帖子為 2.6M 瀏覽量；引用 Huntley、Cherny、Osmani、Catacora；提供帖子的中文翻譯，而非原始措辭。Steinberger 帖子本身透過上列來源引用，原始 X 連結未經獨立驗證。
- MarkTechPost, "Prompt Engineering vs Loop Engineering vs Graph Engineering: What Changes at Each Layer" (七月 29, 2026): [https://www.marktechpost.com/2026/07/29/prompt-engineering-vs-loop-engineering-vs-graph-engineering-what-changes-at-each-layer/](https://www.marktechpost.com/2026/07/29/prompt-engineering-vs-loop-engineering-vs-graph-engineering-what-changes-at-each-layer/)：堆疊控制單元的框架。
- BleepingComputer, "Claude Fable 5 isn't permanently leaving subscriptions, Anthropic says" (七月 2026): [https://www.bleepingcomputer.com/news/artificial-intelligence/claude-fable-5-isnt-permanently-leaving-subscriptions-anthropic-says/](https://www.bleepingcomputer.com/news/artificial-intelligence/claude-fable-5-isnt-permanently-leaving-subscriptions-anthropic-says/)：七月 2 日說明移出訂閱並非永久；早於七月 18 日最終安排，不包含後者具體細節。
- Anthropic Help Center, "Claude Fable 5 on your plan": [https://support.claude.com/en/articles/15424964-claude-fable-5-on-your-plan](https://support.claude.com/en/articles/15424964-claude-fable-5-on-your-plan)："Starting July 20, 2026"：Fable 5 成為 Max 計劃及 Team／Enterprise 高階席位的標準組成，無額外費用可用至每週限額的 50%；Pro 與標準席位採用隨用隨付點數。
- Bastian, Matthias (The Decoder), "Anthropic slashes Claude Fable 5 limits in Max and Team Premium and pushes Pro users toward API pricing" (七月 18, 2026): [https://the-decoder.com/anthropic-slashes-claude-fable-5-limits-in-max-and-team-premium-and-pushes-pro-users-toward-api-pricing/](https://the-decoder.com/anthropic-slashes-claude-fable-5-limits-in-max-and-team-premium-and-pushes-pro-users-toward-api-pricing/)：七月 18 日公告：七月 20 日起包含在訂閱內，適用 50% 限額；Pro／Team Standard 獲一次性 $100 點數，之後按 API 價格付費。
- Forbes (Sandy Carter), "Claude Fable 5 Extends to July 19: 7 Days, 7 Power Moves" (七月 13, 2026): [https://www.forbes.com/sites/sandycarter/2026/07/13/claude-fable-5-extends-to-july-19-7-days-7-power-moves/](https://www.forbes.com/sites/sandycarter/2026/07/13/claude-fable-5-extends-to-july-19-7-days-7-power-moves/)：最終安排前，先後延長訪問期限的過程。
- Anthropic, "Introducing Claude Opus 5" (七月 24, 2026): [https://www.anthropic.com/news/claude-opus-5](https://www.anthropic.com/news/claude-opus-5)：價格、Fast 模式、對話中改工具而不破壞快取；Frontier-Bench／CursorBench 數字均為 Anthropic 自報。平臺文件 "What's new in Claude Opus 5"：[https://platform.claude.com/docs/en/about-claude/models/whats-new-opus-5](https://platform.claude.com/docs/en/about-claude/models/whats-new-opus-5)，提供預設及最大均為 1M-token 的上下文視窗、128K 最大輸出、預設開啟思考，以及完整五級強度 `low`／`medium`／`high`／`xhigh`／`max`；這些都不見於公告頁。
- TechCrunch, "Anthropic launches Opus 5" (七月 24, 2026): [https://techcrunch.com/2026/07/24/anthropic-launches-opus-5/](https://techcrunch.com/2026/07/24/anthropic-launches-opus-5/)
- Axios, "Anthropic releases new model Opus 5" (七月 24, 2026): [https://www.axios.com/2026/07/24/anthropic-releases-new-model-opus-5](https://www.axios.com/2026/07/24/anthropic-releases-new-model-opus-5)
- Model Context Protocol 部落格, "The 2026-07-28 specification" (七月 28, 2026): [https://blog.modelcontextprotocol.io/posts/2026-07-28/](https://blog.modelcontextprotocol.io/posts/2026-07-28/)：最終規範：無狀態核心、MRTR（SEP-2322）、CIMD 取代 Dynamic Client Registration、RFC 9207 簽發者驗證、擴充套件框架、12 個月棄用視窗。
- TechCrunch, "AI's most important protocol is getting a little bit easier to use" (七月 20, 2026): [https://techcrunch.com/2026/07/20/ais-most-important-protocol-is-getting-a-little-bit-easier-to-use/](https://techcrunch.com/2026/07/20/ais-most-important-protocol-is-getting-a-little-bit-easier-to-use/)
- The Register, "Model Context Protocol prepares to break with its stateful past" (七月 23, 2026): [https://www.theregister.com/devops/2026/07/23/model-context-protocol-prepares-to-break-with-its-stateful-past/5276722](https://www.theregister.com/devops/2026/07/23/model-context-protocol-prepares-to-break-with-its-stateful-past/5276722)
- WorkOS, "MCP 2026 spec: agent authentication" (七月 2026): [https://workos.com/blog/mcp-2026-spec-agent-authentication](https://workos.com/blog/mcp-2026-spec-agent-authentication)：CIMD 與授權變化的二手報道。
- MemTensor, Renmin University, NUS, SJTU, Tongji, "Metis: Memory Foundation Model," arXiv 2607.26760 (提交 七月 29, 2026): [https://arxiv.org/abs/2607.26760](https://arxiv.org/abs/2607.26760)：transformer 主幹內部的引數化持久記憶；基於 Qwen3.5 的 4B/9B/27B 原型；hyper memory block + local memory block 受 Fast Weight Programming 啟發；自報侷限為固定大小壓縮的資訊丟失、潛在空間語義混合。
- LangChain, "Deep Agents v0.7" (七月 29, 2026): [https://www.langchain.com/blog/deep-agents-v0-7](https://www.langchain.com/blog/deep-agents-v0-7)：預設移除基礎系統提示，內建工具描述縮短 43%，`TodoListMiddleware`／`write_todos` 改為主動啟用；預設智慧體回合基礎輸入 token 從 ~6K → ~2K，減少 65%；在三個模型系列上評估待辦列表消融。
- MinIO, "Introducing AIStor Memory: Long-Term Memory for AI Agents" (七月 29, 2026): [https://www.min.io/blog/introducing-aistor-memory-long-term-memory-for-ai-agents](https://www.min.io/blog/introducing-aistor-memory-long-term-memory-for-ai-agents)：基於物件儲存的記憶、工作區與憑證層；SiliconANGLE、The Register、HPCwire／BigDATAwire 在 七月 29-30, 2026 的報道提供佐證。
- "Practical Online KV Cache Compaction for LLM Agents," arXiv 2608.00902 (提交 八月 2, 2026): [https://arxiv.org/abs/2608.00902](https://arxiv.org/abs/2608.00902)：立即壓縮降低準確率；等智慧體自身後續查詢成為代理查詢訊號，可恢復大部分差距；代理不理想時，token 驅逐比注意力匹配重建更穩健；KV-cache 減少 80%，BrowseComp-Plus、WideSearch 吞吐改善。
- TencentCloud, "TencentDB-Agent-Memory" (GitHub): [https://github.com/TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory)：MIT 許可、自託管；倉庫建立於 四月 7, 2026；GitHub API 約 ~24K stars，八月 24, 2026 檢查。二手來源：MarkTechPost（八月 7, 2026）：[https://www.marktechpost.com/2026/08/07/tencent-cloud-open-sources-tencentdb-agent-memory-v2-0/](https://www.marktechpost.com/2026/08/07/tencent-cloud-open-sources-tencentdb-agent-memory-v2-0/)，報道 v2.0；PRNewswire（八月 13, 2026）是另一份團隊協作公告。v2.0.0 於 八月 3, 2026 釋出，GitHub releases API `published_at` 為 2026-08-03，MarkTechPost 也寫同一天。全部 Team Memory 治理機制均為 Tencent 自報，尚無獨立評估。
- Zenity Labs, "Attackers Target Agents via the Skill Supply Chain" (八月 6, 2026): [https://labs.zenity.io/post/attackers-target-agents-via-the-skill-supply-chain](https://labs.zenity.io/post/attackers-target-agents-via-the-skill-supply-chain)：冒充 `paperclipai`、`browser-use` 的 GitHub 組織；技能七月 5 日無害，七月 11 日武器化，熱門 #8；四種觸發機制涉及 138 個憑證路徑；顯示 >1.7M 安裝，為彙總計數，不代表獨立智慧體；Vercel／GitHub 在 12 小時內下架。二手來源：CSO Online：[https://www.csoonline.com/article/4206851/](https://www.csoonline.com/article/4206851/)；Business Wire（八月 6, 2026）：[https://www.businesswire.com/news/home/20260806707467/en/](https://www.businesswire.com/news/home/20260806707467/en/)。獨立的 Paperclip *產品* CVE，包括 CVE-2026-41679 及相關漏洞，八月 5, 2026 披露，屬於不同事件，此處不涵蓋。
- AWS 機器學習部落格, "Control agent behaviors and cost beyond a single action: new capabilities in Amazon Bedrock AgentCore" (八月 6, 2026): [https://aws.amazon.com/blogs/machine-learning/control-agent-behaviors-and-cost-beyond-a-single-action-new-capabilities-in-amazon-bedrock-agentcore/](https://aws.amazon.com/blogs/machine-learning/control-agent-behaviors-and-cost-beyond-a-single-action-new-capabilities-in-amazon-bedrock-agentcore/); AWS What's New, "Temporal Policies for AgentCore" (八月 6, 2026): [https://aws.amazon.com/about-aws/whats-new/2026/08/temporal-policies-agentcore/](https://aws.amazon.com/about-aws/whats-new/2026/08/temporal-policies-agentcore/); AWS What's New, "AWS Bedrock AgentCore Runtime Instances generally available" (八月 6, 2026): [https://aws.amazon.com/about-aws/whats-new/2026/08/aws-bedrock-agentcore-runtime-instances-generally-available/](https://aws.amazon.com/about-aws/whats-new/2026/08/aws-bedrock-agentcore-runtime-instances-generally-available/)：基於 Apache-2.0 Dogwood 策略語言、理解會話歷史的預設拒絕授權；閘道器 Rate Limiting；客戶自選 EC2 例項型別，九個區域，會話最長 14 天，相比無伺服器預設 8 小時。
- Anthropic, "Cross-session messaging" (八月 2026): [https://code.claude.com/docs/en/cross-session-messaging](https://code.claude.com/docs/en/cross-session-messaging) 與 Claude Code changelog: [https://code.claude.com/docs/en/changelog](https://code.claude.com/docs/en/changelog)：`ListAgents`／`SendMessage` 從 v2.1.224（八月 7, 2026）至 v2.1.241（八月 23 日）；按會話入站接受／暫存／拒絕，以及大小、突發、迴圈節流；歷史、檔案與許可權批准均不跨會話；Bedrock、Claude Platform on AWS、Google Cloud Agent Platform、Microsoft Foundry 不可用。兩個介面均沒有 "graph engineering." 一詞。
- Meta, "Introducing Muse Glimmer: an open agentic model" (八月 10, 2026): [https://research.meta.ai/blog/introducing-muse-glimmer-open-agentic-model](https://research.meta.ai/blog/introducing-muse-glimmer-open-agentic-model)：30B 稠密、Apache 2.0、從 Muse Spark 蒸餾；4-bit 下低於 20GB；day-0 多執行時支援。DFlash 加速 3.1x / 1.8x / 1.5x，以及與 Gemma4-31B／Qwen3.6-27B 的比較，均為 Meta 自報。二手來源：Phoronix、CNBC（八月 10, 2026）、gHacks（八月 11, 2026）。
- DeepSeek, "DeepSeek Harness" (八月 13, 2026): [https://github.com/deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) 與 [https://deepseek.com/harness/en/](https://deepseek.com/harness/en/)：MIT 許可證；"Cordis" 外掛正規化及其 "A Programming Paradigm for Spatiotemporal Composability" 白皮書；僅追加會話日誌；GitHub API 的 190,630 stars／21,319 forks，檢查日期 八月 24, 2026；224,004 stars／26,637 forks，檢查日期 九月 15, 2026。Claude-Code／Codex 子智慧體能力屬於第一方：倉庫提供 `@deepseek-ai/dsh-subagent-claude-code`、`@deepseek-ai/dsh-subagent-codex` 包，設計說明日期 八月 4, 2026，呼叫官方 Claude Agent SDK 與 Codex `app-server`；CryptoBriefing、MindStudio、Digital Applied、Flowtivity 的二手報道由程式碼取得該能力。
- Anthropic, 釋出說明總覽: [https://platform.claude.com/docs/en/release-notes/overview](https://platform.claude.com/docs/en/release-notes/overview)：Skills API 於 八月 19, 2026 結束測試；Managed Agents 的 GitHub 託管技能為 八月 7, 2026。Anthropic 部落格 "Computer use, Skills API, and Files API"，日期 八月 20, 2026：[https://claude.com/blog/computer-use-skills-api-files-api](https://claude.com/blog/computer-use-skills-api-files-api)，是比釋出說明晚一天的配套文章。Managed Agents 技能文件：[https://platform.claude.com/docs/en/managed-agents/skills](https://platform.claude.com/docs/en/managed-agents/skills)，說明自動發現已掛載倉庫根目錄 `.claude/skills`，以及信任邊界提示。
- OpenAI, "Codex as a Platform" (八月 19, 2026): [https://developers.openai.com/blog/codex-as-a-platform](https://developers.openai.com/blog/codex-as-a-platform)：`codex exec`、Codex SDK 與 app-server 採用 Apache 2.0；ARC-AGI-3 從 13.3% 至 38.3%、輸出 token 減少 6x，以及 Cisco／GitHub／JetBrains／Thrive-Crete 生產使用者，均為 OpenAI 自報。原始頁面在作者欄正上方標記 "Aug 19, 2026"；部分二手來源 OpenSourceForU、finance.biggo.com 標為八月 20 日。`openai/codex` 倉庫自 2025 年四月起已公開並採用 Apache-2.0，來自 GitHub API，因此是重新定位編排層，而非首次開源。
- Model Context Protocol 部落格, "The MCP Roadmap" (八月 22, 2026): [https://blog.modelcontextprotocol.io/posts/mcp-roadmap/](https://blog.modelcontextprotocol.io/posts/mcp-roadmap/)：Contributor Ladder、Working-Group SEP 分流、正式功能生命週期與棄用策略；五個重點為智慧體訊息及 Tasks 走向核心、本地部署 HTTP 原生傳輸、以 DPoP 與 Workload Identity Federation 實現智慧體身份、工具結果處理及漸進式發現，以及 SDK 開發體驗與一致性。當日 Hacker News 為 241 points／142 條評論，屬於快照。
- OpenRouter 周榜，中國模型包攬前五（報道日期 七月 29, 2026): Dataconomy, "Chinese LLMs Take Top Five Spots On OpenRouter": [https://dataconomy.com/2026/07/29/chinese-ai-models-openrouter-top-five/](https://dataconomy.com/2026/07/29/chinese-ai-models-openrouter-top-five/); TechBriefly, "Chinese AI models lead OpenRouter for first time": [https://techbriefly.com/2026/07/29/chinese-ai-models-lead-openrouter-for-first-time/](https://techbriefly.com/2026/07/29/chinese-ai-models-lead-openrouter-for-first-time/)：中國模型包攬前五，以及每週 >20T token 的數字。九月延續：[https://finance.yahoo.com/technology/ai/articles/chinese-ai-models-now-capture-020440715.html](https://finance.yahoo.com/technology/ai/articles/chinese-ai-models-now-capture-020440715.html) 提供 46.4%／35.7% 劃分。KuCoin 快訊 [https://www.kucoin.com/news/flash/chinese-models-dominate-openrouter-weekly-token-usage-ranking](https://www.kucoin.com/news/flash/chinese-models-dominate-openrouter-weekly-token-usage-ranking) 涉及不同、更早快照：八月 5, 2026，中國模型佔前十中八個，不是九月數字來源。OpenRouter 自身排名頁是實時滾動檢視，沒有註明日期的歷史記錄：[https://openrouter.ai/rankings](https://openrouter.ai/rankings)。兩組份額均為二手來源、方法不同，彼此不可比較。
- "Filesystem-Based Memory for LLM Agents: Organization, Evolution, and Sustainability," arXiv 2607.26637 (提交 七月 29, 2026): [https://arxiv.org/abs/2607.26637](https://arxiv.org/abs/2607.26637)：在共享記憶檔案系統上正式區分三類角色；規模擴大後，有序組織使檢索成本大致減半，但除最強管理智慧體外，組織都會退化，所有受測智慧體都未能轉化為更好答案。"MemTxn: A Transaction Boundary for Source-Supported Updates and Complete-State Recovery in Agent Memory,"，arXiv 2607.27834（七月 30, 2026 提交）：[https://arxiv.org/abs/2607.27834](https://arxiv.org/abs/2607.27834)，Ordered PatchTest、Temporal Resolver、持久快照日誌；作者驗證集接受 60、拒絕 179。"MemTX: Transactional Belief Commit for Stateful Agent Memory,"，arXiv 2607.23929（七月 27, 2026 提交）：[https://arxiv.org/abs/2607.23929](https://arxiv.org/abs/2607.23929)，無共同作者的獨立提案。"Memory Decoder at Scale: A Pretrained, Parametric Long-Term Memory,"，arXiv 2607.27919（七月 30, 2026 提交）：[https://arxiv.org/abs/2607.27919](https://arxiv.org/abs/2607.27919)，6.9B 記憶模組加 410M Pythia 基礎模型，成績 37.34，對比 Pythia-12B 的 37.24，總引數減少 39%。全部數字均為論文自報，尚未復現。
- Google Cloud 部落格, "What's new in Gemini Enterprise Agent Platform" (七月 30, 2026): [https://cloud.google.com/blog/products/ai-machine-learning/whats-new-in-gemini-enterprise-agent-platform](https://cloud.google.com/blog/products/ai-machine-learning/whats-new-in-gemini-enterprise-agent-platform)：Agent Memory Bank、Agent Runtime（最長七天）、Agent Identity、Agent Gateway、Agent Registry，共五項能力一同正式釋出；全部能力描述均來自 Google。產品文件：[https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/memory-bank](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/memory-bank)。二手來源：[https://enterprisedna.co/resources/news/google-gemini-agent-platform-memory-runtime-identity-ga-2026/](https://enterprisedna.co/resources/news/google-gemini-agent-platform-memory-runtime-identity-ga-2026/)。不同於平臺舊品牌下、七月 2025 的 Vertex AI Memory Bank 公開預覽。
- "Can Agent Memory Systems Track Evolving State?" (StateMemBench / StateMem), arXiv 2608.19652 (八月 20, 2026): [https://arxiv.org/abs/2608.19652](https://arxiv.org/abs/2608.19652)：234 個多會話場景，以封閉候選池評分衡量新近值取代舊值；StateMem 報告 DeepSeek-V4-Flash 當前狀態準確率，相比同主幹最強基線為 1.8x（0.205 至 0.363），Qwen-3.5-9B 相比最強記憶系統為 1.6x（0.149 至 0.233）；包裝六個後端提升 +32 至 +67 個點，控制新增上下文後仍為 +15 至 +32。論文是唯一已檢查來源；數字均為作者自報，尚未復現。
- CrowdStrike, "CrowdStrike Unveils Falcon Guardian" (九月 1, 2026): [https://www.crowdstrike.com/en-us/press-releases/crowdstrike-unveils-falcon-guardian-ai-agent-security/](https://www.crowdstrike.com/en-us/press-releases/crowdstrike-unveils-falcon-guardian-ai-agent-security/)：在 Windows 與 macOS 端點發現、盤點智慧體，並執行執行時檢測與控制；未提供安裝基數或檢測率。二手來源：SiliconANGLE（九月 1, 2026）：[https://siliconangle.com/2026/09/01/crowdstrike-launches-falcon-guardian-to-police-ai-agents-at-the-endpoint/](https://siliconangle.com/2026/09/01/crowdstrike-launches-falcon-guardian-to-police-ai-agents-at-the-endpoint/)。AIR：TechCrunch（九月 1, 2026）：[https://techcrunch.com/2026/09/01/air-raises-50m-to-help-companies-vet-the-skills-and-add-ons-ai-agents-use/](https://techcrunch.com/2026/09/01/air-raises-50m-to-help-companies-vet-the-skills-and-add-ons-ai-agents-use/)，SecurityWeek（九月 3, 2026）：[https://www.securityweek.com/ai-agent-firewall-startup-air-security-emerges-from-stealth-with-50-million/](https://www.securityweek.com/ai-agent-firewall-startup-air-security-emerges-from-stealth-with-50-million/)，兩輪融資 $50M；17,800+ 外掛／6.7M 安裝，以及冒充 Anthropic、OpenAI 的技能，均來自 AIR 自身研究，方法未公開。
- OpenAI, "GPT-6 Astra: A new generation of intelligence": [https://openai.com/index/gpt-6-astra/](https://openai.com/index/gpt-6-astra/)：Critical 門檻宣告，ExploitBench 100% 對比 78.5%，ExploitGym 42.4% 對比 30.3%，SRE-Bench 首次嘗試 88.0%、四次內 99.2%，分階段推出的句子、概念驗證拒絕、Daybreak 擴充套件路徑，以及 Astra 書面推理更難監控的發現。OpenAI，"Safety overview: GPT-6 Astra"，頁面日期 九月 3, 2026：[https://openai.com/index/safety-overview-gpt-6-astra/](https://openai.com/index/safety-overview-gpt-6-astra/)，"our first model to reach the Critical level of cybersecurity capability under our Preparedness Framework"，以及可監控性下降，包括故意降低表現、躲避破壞任務檢測。OpenAI，"The path to Astra"，頁面日期 九月 1, 2026：[https://openai.com/index/path-to-astra/](https://openai.com/index/path-to-astra/)，釋出前分級、在二十個高嚴重性 V8 漏洞上內部移植的 ExploitBench，以及利用鏈中的兩個零日。基準數字均為 OpenAI 自報。二手來源：CSO Online（九月 4, 2026）：[https://www.csoonline.com/article/4218679/openai-launches-gpt-6-astra-its-first-model-to-cross-a-critical-cybersecurity-threshold.html](https://www.csoonline.com/article/4218679/openai-launches-gpt-6-astra-its-first-model-to-cross-a-critical-cybersecurity-threshold.html)；CNBC（九月 3, 2026）：[https://www.cnbc.com/2026/09/03/open-ai-astra-gpt-6-cyber.html](https://www.cnbc.com/2026/09/03/open-ai-astra-gpt-6-cyber.html)，均為釋出報道。三個 OpenAI 頁面都沒有上下文視窗與最大輸出數字，因此此處不引用。釋出頁稱企業訪問在推出時預設關閉，條目已引用；API 每百萬輸入／輸出 token $10 / $50 也在同頁，但不是此處關鍵論據。
- Goyal, Ankit 與 Ray, Jaideep, "Does Your Agent's Memory Survive a Model Upgrade? A Controlled Study of Memory Portability," arXiv 2609.05339 (九月 4, 2026): [https://arxiv.org/abs/2609.05339](https://arxiv.org/abs/2609.05339)：48 個合成案例，比較原始歷史、RAG、壓縮筆記、知識圖譜；圖記憶幾乎不變（0.0004 +/- 0.0020），壓縮筆記波動 +9.91 / -13.28 個點，部分重新嵌入恢復 4.96、完整重新嵌入 11.90；約 ~80% 退化歸於構建時資訊丟失；只有保留原始歷史，才在兩個受測遷移方向之一修復 48 案例中的 34 個。兩位作者，合成語料，尚未復現。
- Anthropic, "Detecting and countering misuse of AI: September 2026" (九月 10, 2026): [https://www.anthropic.com/threat-intelligence-report-september-2026](https://www.anthropic.com/threat-intelligence-report-september-2026)：原始報告，涵蓋其在 2025 年十二月至 2026 年八月阻斷的七類濫用，包括非法蒸餾。具體指控及數字，含 5,380 標記賬戶、約十天叢集中的 ~300,000 次請求、歸於 Moonshot AI 的 23M+ 次互動、五月至七月 2026 歸於 Alibaba 的超過 151 百萬次，以及點名 DeepSeek、Z.ai、小米、MiniMax、SenseTime，均直接讀取蒸餾章節。二手來源：CNBC（九月 11, 2026）：[https://www.cnbc.com/2026/09/11/chinese-ai-labs-moonshot-deepseek-alibaba-anthropic.html](https://www.cnbc.com/2026/09/11/chinese-ai-labs-moonshot-deepseek-alibaba-anthropic.html)；Dealroom：[https://dealroom.co/news/150366-anthropic-alleges-moonshot-routed-some-kimi-user-requests-to-claude-then/](https://dealroom.co/news/150366-anthropic-alleges-moonshot-routed-some-kimi-user-requests-to-claude-then/)。每項主張都是 Anthropic 對競爭對手的指控，未經獨立裁定。
- Salesforce, "Agentforce job-ready AI agents" (九月 11, 2026): [https://www.salesforce.com/uk/news/stories/agentforce-job-ready-ai-agents/](https://www.salesforce.com/uk/news/stories/agentforce-job-ready-ai-agents/)：長週期執行時含記憶、持久執行、動態引導；Hunter 處於試點，計劃 2026 年十一月正式釋出；Multi-Agent Orchestration 正式釋出。二手來源：unite.ai：[https://www.unite.ai/salesforce-debuts-job-ready-agentforce-agents-and-long-horizon-runtime/](https://www.unite.ai/salesforce-debuts-job-ready-agentforce-agents-and-long-horizon-runtime/)。多周目標追求能力是 Salesforce 自報，沒有獨立基準；負責展示能力的智慧體尚未正式釋出。
- 第 14 章存續檢查關口，檢查日期 2026 年九月 15 日。原始證據均在該章來源完整列出：Anthropic，"How we built our multi-agent research system"（2025 年六月 13 日）：[https://www.anthropic.com/engineering/multi-agent-research-system](https://www.anthropic.com/engineering/multi-agent-research-system)；OpenAI Codex PR [#28792](https://github.com/openai/codex/pull/28792)（2026 年六月 19 日 合併）、[#29324](https://github.com/openai/codex/pull/29324)（2026 年六月 22 日 合併），首次隨 [rust-v0.142.0](https://github.com/openai/codex/releases/tag/rust-v0.142.0)（2026 年六月 22 日）釋出；Graph Engineering Mastery：[https://graphengineerings.com/](https://graphengineerings.com/)、[https://graphengineerings.com/course/module-2.html](https://graphengineerings.com/course/module-2.html)；SmartScope（2026 年九月 1 日）：[https://smartscope.blog/en/blog/graph-engineering-loop-engineering-logic-review/](https://smartscope.blog/en/blog/graph-engineering-loop-engineering-logic-review/)；Nhu Hoang，Towards Data Science（2026 年九月 14 日）：[https://towardsdatascience.com/graph-engineering-for-ai-agents-from-prompts-and-loops-to-workflows/](https://towardsdatascience.com/graph-engineering-for-ai-agents-from-prompts-and-loops-to-workflows/)；AgentEng London 2026：[https://agentengineering.world/london/](https://agentengineering.world/london/)；`headcount`，倉庫建立於 2026 年八月 28 日：[https://github.com/cbrock84/headcount](https://github.com/cbrock84/headcount)。七月文字未規定關口彙總規則，已在第 14 章第 14.7 節明示，而非暗示。

---

*上一章：[第 10 章：構建真實世界的知識編排系統](10-case-study.md)*
