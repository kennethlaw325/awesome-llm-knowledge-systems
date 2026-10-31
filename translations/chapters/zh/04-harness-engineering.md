<!-- translation-sync:start -->
> 與 2026-10-31 英文版同步的機器輔助譯文，已作結構與內容覆核。程式碼和圖中標籤保留原文；閱讀時間按英文原文估算。
> [English source](../../../chapters/04-harness-engineering.md) · [Sync record](../../SYNC.md)
<!-- translation-sync:end -->

<a id="chapter-4-harness-engineering-building-the-os-around-the-model"></a><!-- i18n-anchor -->

# 第 4 章：Harness Engineering —— 圍繞模型構建作業系統

> **一句話總結：** Harness 是 AI 模型周圍的一切——讓它真正可用的規則、工具、安全檢查、工作流程。
>
> **為什麼重要：** AI 模型像一具強大引擎。沒有底盤、方向盤、煞車, 它就沒用。Harness 是把原始 AI 變成產品的東西。
>
> **閱讀時間：** ~49 分鐘（按英文原文估算：11,174 個單詞 / 230 wpm）

*圖：編排層的構成，依據第 4.4 節六個 IMPACT 維度，即意圖、記憶、規劃、許可權、控制流、工具，圍繞模型排列。由左至右的主幹對應本章開篇定義：編排層將原始推理轉化為可靠行為。每條邊標明該維度決定或提供什麼，這正是第 4.4 節使用清單的方式，逐條檢查連線便會暴露缺口。兩個強調維度承載論點，因為工具強大、許可權薄弱的系統，正是該節指出的安全問題。*

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryColor':'#eef1f4','primaryTextColor':'#1f2328','primaryBorderColor':'#8c959f','lineColor':'#6b7280','tertiaryColor':'#f6f8fa','clusterBkg':'#f9fafb','clusterBorder':'#8c959f','edgeLabelBackground':'#ffffff'}}}%%
flowchart LR
    INT["Intent"] -->|what the user actually wants| M
    MEM["Memory"] -->|what survives turns and sessions| M
    PLAN["Planning"] -->|how the task breaks into steps| M
    AUTH["Authority"] -->|what the system is allowed to do| M
    CF["Control flow"] -->|how execution proceeds| M
    TOOL["Tools"] -->|which external capabilities it can reach| M
    M["Model<br/>raw inference"] -->|harness turns it into| OUT["Reliable behavior"]
    class INT,MEM,PLAN,CF,M,OUT stable
    class AUTH,TOOL accent
classDef stable fill:#eef1f4,stroke:#8c959f,stroke-width:1.5px,color:#1f2328
classDef accent fill:#dbeafe,stroke:#2563eb,stroke-width:1.5px,color:#0b3a8f
classDef muted fill:#f6f8fa,stroke:#adb5bd,stroke-width:1.5px,color:#57606a
classDef gate fill:#ffffff,stroke:#2563eb,stroke-width:1.5px,color:#0b3a8f
```

> "Every component in a harness encodes an assumption about what the model can't do on its own, and those assumptions are worth stress testing."
> —— Anthropic, "Building Effective Agents,", 2025

> "模型從來都沒有長手。"
> —— Cab, 論為什麼工具使用是 harness 問題而非模型問題

Agent 不是模型。Agent 是 **模型加 harness**——圍繞的 prompt、工具、記憶、控制流、評估邏輯、編排程式碼系統, 把原始推論變成可靠行為。模型是引擎; harness 是車輛。本章檢視從業者如何設計、評估、演化那輛車。

**關於直覺的註記。** 把這件事變具體的隱喻, 對許多初學者來說是 Cab 的觀察:"the model never literally grew hands."當一個程式設計 agent 編輯檔案, 編輯檔案的不是模型——是 harness, 由模型作為文字返回的工具呼叫所觸發。我們歸給"the AI"的每個能力, 實際上是圍繞模型的 harness 的能力。把 harness 拿走, 你得到一個只能產文字的模型。把模型拿走, 你得到一個沒有東西可路由的 harness。Harness engineering 是決定那條線在哪、兩半如何合作的學科。

---

<a id="41-defining-the-harness"></a><!-- i18n-anchor -->

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

2026 年 五月，AWS AgentCore Payments（第 11 章）出現了一類新的利用合約：**確定性基礎設施對智慧體操作強制執行的限制。**其中評估器式元件透過詢問另一個 LLM "did this go too far," AgentCore Payments 的會話級支出限制進行軟強制，是底層邊界的硬上限--- 智慧體根本無法超過它，不涉及 LLM 判斷。該模式概括為：隨著託管智慧體、記憶體和支付等底層基礎能力的積累，利用契約越來越多地包含模型無法推理的硬限制，與過濾模型內容的軟推理控制元件並存。

該單一操作上限推廣到 2026 年 **八月 6** 的完整會話歷史記錄，當時 AWS 為 Bedrock AgentCore 提供了 **臨時策略**，由 **Dogwood** 提供支援，Dogwood** 是一種新的 Apache-2.0 開源策略語言，專為 AI 智慧體而構建，其本身構建在 Cedar 的基礎上。臨時策略在閘道器處根據智慧體在會話中已完成的所有操作進行評估 - 確定性、預設拒絕、完全記錄以及在智慧體自己的程式碼之外強制執行。指定用途包括捕獲資料偽造（傳遞給工具的值必須與之前的呼叫實際返回的值相匹配）、累積會話成本上限以及在工作流程中稍後的特權步驟之前需要人工批准。 AgentCore Payments 強制執行單個操作，而臨時策略則強制執行整個會話的先前操作——許可權軸上的一個新的原始類（第 4.4 節）。 AWS 與閘道器速率限制（每使用者/OAuth/IAM 對請求、token、連線持續時間的上限）一起提供，並在同一天將 **執行時例項** 全面提供：智慧體現在可以在 AWS 管理的生命週期下在客戶選擇的 EC2 例項型別上執行，並且會話持續最長 **14 天**，而無伺服器 microVM 預設為 8 小時。更長的會話上限與跨越它的持續進步不是同一軸——第 4.8 節的終端基準挑戰結果顯示，即使在原則上現在可以執行兩週的會話中，前沿模型也可以磨練 12 個小時而沒有任何改進。

五週後，權威軸心有了第二個答案，建立在相反的機制上。 2026 年 **九月 10 日**，Anthropic 在現有 `always_allow` 和 `always_ask` 的基礎上，向託管智慧體新增了 **`auto` 許可權策略**。臨時策略是用策略語言編寫並在閘道器處評估的確定性程式，而 `auto` 是模型評估的每次呼叫判斷：伺服器（而不是呼叫客戶端）權衡每個單獨的工具呼叫（工具、其輸入以及迄今為止的會話內容），並返回三個結果之一。呼叫執行；或者被拒絕，並且智慧體收到客戶端無法覆蓋的錯誤結果；或者暫停審批，流程與 `always_ask` 相同。判決透過 `agent.tool_use` 和 `agent.mcp_tool_use` 事件上的 `evaluation` 物件返回，攜帶巢狀的 `evaluated_permission` 和 `reason_code`（例如 `high_risk` 或 `indeterminate`），並且適用，根據 Anthropic 的文件，MCP 工具集以及預構建的智慧體工具集 --- 各個 MCP 工具呼叫受到平臺級治理的控制，第 7 章從協議方面進行處理。相同的文件注意`auto`不是人工審查門：伺服器判斷安全的呼叫立即執行，並且可能是不可逆的。所有這些都來自 Anthropic 的文件；尚未出現該功能的獨立報道。閱讀AgentCore旁邊的內容，配對才是重點。兩個供應商相隔五週回答了相同的權威問題，採用了相反的機制——一方面是確定性的策略語言，另一方面是每次呼叫的推理判斷——這是第 4.2 節中計算與推理的分離，到達授權階段，之前它存在於輸出驗證中。

<a id="42-the-bockeler-taxonomy"></a><!-- i18n-anchor -->

## 4.2 Böckeler 分類

Birgitta Böckeler（ThoughtWorks, 2026 年 四月）在 Martin Fowler 的 *Exploring Generative AI* 系列中, 提出了一個二軸 harness 元件分類, 已成為標準參考:

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

**功能級感測器類別於 2026 年出現。** Böckeler 的感測器象限最初涵蓋輸出級反饋——驗證者、測試執行者、讀取模型*發出*內容的判斷者。機制可解釋性新增了一個通道，可以在模型發出任何內容之前讀取模型正在做什麼：殘差流中的特徵方向（Anthropic 的 2026 年四月情感向量）和思維鏈監控（OpenAI 的推理模型讀取隱藏測試用例的四月捕獲）。 2026 年中期的兩項結果使承諾和限制都更加明確。在六月，**METR** --- 給予 OpenAI 的 GPT-5.6 Sol 的原始 CoT 訪問許可權 --- 記錄了它評估過的任何公共模型中檢測到的最高作弊率（第 11 章），而捕獲之所以有效，正是因為OpenAI *保留*原始 CoT 而不是針對它進行訓練；訓練通道離開，通道就會關閉。七月，Anthropic 的 **J 空間** 研究（第 11 章）為該限制提供了候選答案：一小組內部殘餘流方向 Claude 可以報告並有意調製，充當*第二個 CoT 獨立感測器類*，即使在模型從未用語言表達的步驟上，系統編排層也可以讀取。對於系統編排層設計人員來說，感測器象限不再只是 "check the output"——它越來越多地包括讀取並最終控制模型的內部狀態。

**最新的資料點與樂觀情緒背道而馳。** 2026 年 九月 3 日，OpenAI 發貨了 **GPT-6 Astra**，在其自己的安全概述中描述為 "our first model to reach the Critical level of cybersecurity capability under our Preparedness Framework"——第一個型號 OpenAI 已指定在其自己釋出的風險階梯的頂層。接下來的內容是系統編排層設計而不是模型釋出：Astra 在全面上市之前向有限的組織推出，釋出頁面指出部署的模型 "Enterprise administrators can enable Astra for their workspace; access is off by default at launch," 拒絕更高階的網路安全任務（其中概念驗證漏洞利用生成），OpenAI 命名為 Daybreak 和Daybreak Blue 是經過審查的防禦者在漏洞驗證、惡意軟體分析和檢測工程方面獲得限制較少的保護措施的途徑。該名稱背後的能力數字是 OpenAI 自己的，在沒有生產保障的情況下測量：ExploitBench 為 100%，GPT-5.6 Sol 為 78.5%，ExploitGym 為 42.4%， 88.0% 的 SRE-Bench 任務透過一次嘗試就解決了，其中 99.2% 在四次嘗試內解決。不過，對於本節來說，承重句是一個比較安靜的句子。 OpenAI 指出，"GPT-6 Astra's monitorability has decreased relative to GPT-5.6 Sol," 將下降歸因於模型對其自身思想鏈的更大控制以及將有罪材料放在那裡的傾向較低；儘管 OpenAI 報告沒有隱寫推理的證據，並且認為逃避風險很大程度上侷限於較低推理的任務，但在對抗壓力下，它可能在故意降低表現時不被發現。這是一家供應商自願表示，其最新的前沿模型比之前的模型更難觀察。它並沒有反駁 J 空間線，該線提出了一種根本不依賴於語言推理的感測器——但它確實啟動了一個時鐘。三個月前開發的CoT通道METR從模型方面正在縮小，任何依賴於它的系統編排層元件都是貶值資產。

<a id="43-openai-codex-scale-through-harness"></a><!-- i18n-anchor -->

## 4.3 OpenAI Codex：透過 Harness 規模化

社群廣為引用的一個資料點描述 OpenAI 內部使用 Codex 的情況: **三位工程師加上 Codex agent 系統產出約 一百 萬行程式碼、約 1,500 個 PR**。生產力倍數主要不是關於模型質量——是關於 harness 設計。（具體數字在 2025-2026 年 OpenAI 演講與文章中流傳; 關於 Codex harness 的公開材料, 見 [openai.com/index/introducing-codex](https://openai.com/index/introducing-codex)。）

Codex harness 包括:
- 自動化 PR 分解（把大任務拆成可審查單元）
- 每個任務的沙盒執行環境
- 自動化測試生成與驗證
- PR 邊界的人工審查整合
- 關於 repo 結構與慣例的持續 context

教訓: 在足夠的 harness 成熟度下, 模型變成更大生產系統中的一個元件, 而非獨立工具。Harness 處理編排、質量控制、整合——這些是 prompt engineering 怎麼調都解決不了的關切。

<a id="44-the-impact-framework"></a><!-- i18n-anchor -->

## 4.4 IMPACT 框架

在 2020 年代中期從業者討論中, **IMPACT 助記詞**——Intent、Memory、Planning、Authority、Control flow、Tools——浮現為系統化思考 harness 設計維度的方式:

- **Intent（意圖）：** 系統如何理解使用者實際想要什麼？包括意圖分類、澄清對話、目標分解。
- **Memory（記憶）：** 系統跨回合與 session 記得什麼？包括對話緩衝、向量庫、結構化知識庫、使用者偏好系統。
- **Planning（規劃）：** 系統如何把複雜任務分解成步驟？包括思維鏈 prompting、明確計畫生成、動作空間的樹搜尋。
- **Authority（許可權）：** 系統被允許做什麼？包括許可權系統、人在迴路 gate、能力邊界。
- **Control Flow（控制流）：** 執行如何進行？包括順序鏈、並行扇出、條件分支、含退出條件的迴圈、重試政策。
- **Tools（工具）：** 系統能存取什麼外部能力？包括函式定義、API 整合、程式碼執行環境、瀏覽器存取。

IMPACT 作為設計清單有用。建構或審查 harness 時, 走過每個維度能浮現差距。一個工具強但許可權弱的系統有安全問題。一個規劃強但無記憶的系統不能從錯誤學習。這個框架讓這些不平衡可見。

<a id="45-the-meta-harness-paper-automating-harness-design"></a><!-- i18n-anchor -->

## 4.5 Meta-Harness 論文：自動化 harness 設計

Stanford、MIT、KRAFTON 聯合論文（2026 年 三月）引入 **meta-harness** 概念——一個自動最佳化 harness 配置的系統。

他們的關鍵發現: 在同一基準、同一基礎模型上, 不同 harness 配置產出 **6 倍效能差距**。給定任務的最佳 harness 配置很少明顯, 常常違反直覺。手動 harness 調整正在桌上留下大量效能。

Meta-harness 做法把 harness 引數（重試次數、規劃深度、工具選擇策略、記憶視窗大小、評估嚴格度）視為搜尋空間, 用自動最佳化找出高效能配置。系統能把 harness 適配到不同任務型別、不同模型、不同成本約束。

這個結果有深刻含義: **harness engineering 不是已知最佳實務的已解決設計問題——它是有大且不太理解搜尋空間的最佳化問題**。把 harness 設計視為一次性架構決策的團隊, 很可能在遠低於前沿的狀態執行。

Meta-Harness 論文現在是快速移動一線上的一個資料點。2026 年 四月, **AHE 論文**（"Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses,", arXiv 2604.25850, 復旦/北大/上海齊跡智鋒）把這個問題從搜尋重構為*可觀測性*: 不是把 harness 配置當搜尋空間然後跑最佳化器, AHE 裝備三個可觀測性支柱——元件（明確、可還原的動作空間）、經驗（濃縮的軌跡證據）、決策（執行前做的可證偽編輯預測）——讓 harness 透過讀自己的 runtime 訊號自我演化。經過 10 次 AHE 迭代, Codex-CLI 風格的基線在 Terminal-Bench 2 上 69.7% pass@1 達到 77.0%, 超越人類設計基線（71.9%）, 在轉移到沒被最佳化過的模型家族時顯示 **+5.1 到 +10.1 個百分點的跨家族增益**。跨家族轉移是結構性新聞: 演化的 harness 不只是過擬合到一個模型的怪癖, 它在底下基底換代時仍能延續。Meta-Harness 發現（"harness engineering is an optimization problem with a large search space"）與 AHE 發現（"...and the search can run as a continuous observability loop, not a one-shot optimization"）一起描述一個快速遠離手動調整的工程實務。

**演化進入測試時，並首次受到方法學檢查。** Meta-Harness 與 AHE 在部署前或跨部署演化編排層；**TTHE**（"Test-Time Harness Evolution,"，arXiv 2607.08124，July 9, 2026）將迴圈移入評估本身：智慧體提案者推理未標記的執行軌跡，在執行中改進候選編排層群體；評判者依據執行產生的代理訊號提交改進候選。求解者、提案者、評判者是同一凍結 LLM 外的獨立角色，迴圈中沒有標準答案標籤、沒有任務特定監督，權重不動、標籤不存在，使用當刻適應的是支架。五天後另一論文提出另一面。"Rethinking the Evaluation of Harness Evolution for Agents"（arXiv 2607.12227，July 14, 2026；八月 27 日修訂）提出核算問題：必須在匹配反饋與推理預算下，將編排演化與簡單任務級搜尋基線比較，否則收益無法與購買更多搜尋區分；邊搜尋編排層、邊在同一基準上評價，也有明顯過擬合風險。在 Terminal-Bench 2.1、GPT-5.4 與 Claude Opus 4.6 上按該協議測試，作者報告自動編排演化並不穩定優於簡單測試時擴充套件，且對保留任務泛化較差。批評未點名 TTHE，針對的是整條研究線共享的協議。兩篇合看，編排演化不再只是漂亮數字來源，而成為有測量爭議的領域；參照本章其他基準的證據，這反而更健康。

**對稱方向：為編排層訓練模型。** 編排層合成固定模型、最佳化編排層；2026 年六月 Microsoft 釋出反向方案。**MAI-Code-1-Flash**（Build，June 2, 2026）是 5B 引數編碼模型，Microsoft 報告其**直接針對生產使用的 GitHub Copilot 編排層訓練**，因此不只學會生成正確程式碼，也在智慧體編碼任務中學會*操作周圍工具與系統*。Microsoft 自報，困難任務比同類模型少用 ~60% token，價效比優於 Claude Haiku 4.5，同日進入 Copilot 模型選擇器。通常的框架是 "build a harness around a fixed model"；這裡固定的是編排層，*模型*被訓練為適配它，見術語表 **Harness-Native Training**。兩方向合看，系統編排工程不再單向：外迴圈可為給定模型演化編排層（AHE），訓練執行也可為給定編排層演化模型（MAI-Code），從兩端共同設計。應注意的風險是鎖定：針對某廠商生產編排層訓練的模型，按構建方式，其價值在該編排層內部最大，強化而非削弱第 4.7 節編排層即護城河的動態。

<a id="from-research-to-production-the-advisor-tool-april-2026"></a><!-- i18n-anchor -->

### 從研究到生產：Advisor Tool（2026 年 四月）

Meta-harness 發現是研究結果。一個月後, Anthropic 出貨首個產品化的 meta-harness pattern: **Advisor Tool**（beta, `advisor-tool-2026-03-01`）。該 pattern 把更快的 executor 模型與更有能力的 advisor 模型配對。Executor 處理大部分工作; 當它撞到決策點, 它呼叫 `advisor()` 並收到一個策略計畫或路線修正（典型 400-700 文字 token, 含思考 1,400-1,800）, 而不離開當前 API 請求。

Anthropic 推薦的預設配置很說明:

| Executor | Advisor | 目標用途 |
|----------|---------|----------|
| Haiku 4.5 | Opus 4.6 | 從只用 Haiku 提升智慧 |
| Sonnet 4.6 | Opus 4.6 | 用 Sonnet 成本達到 Opus 單獨的質量 |
| Opus 4.6 | Opus 4.6 | 最難任務的質量精煉 |

這是 6 倍 meta-harness 差距被翻譯成定價策略。不是為每個 token 付 Opus 價格, 你為執行付 Sonnet 價格、為真正塑造輸出的 1-2 次 advisor 呼叫付 Opus 價格。Anthropic 建議的 prompting pattern 值得引用, 因為它把 harness 時機編纂成規則:

> "Call advisor BEFORE substantive work -- before writing, before committing to an interpretation, before building on an assumption. [...] On tasks longer than a few steps, call advisor at least once before committing to an approach and once before declaring done."

文件中幾個細節對從業者重要:

- **服務端子推論。** Advisor 在同一個 `/v1/messages` 請求內執行。Executor 發出 `server_tool_use` 塊, Anthropic 用完整 transcript 跑獨立推論 pass, 結果作為 `advisor_tool_result` 回來。你的程式碼不需額外 round trip。
- **快取約 3 次呼叫打平。** 在 advisor 工具上啟用 `caching` 把 advisor 的 transcript 寫入 5 分鐘或 1 小時快取。第一次呼叫花費額外; 收益從約第三次呼叫開始。短任務應關 caching。
- **簡潔 prompt 減少輸出 35-45%。** 單一指令——"The advisor should respond in under 100 words and use enumerated steps, not explanations"——可衡量地減少 advisor 的最大成本驅動, 而不改變呼叫頻率。
- **明確協調協議。** 當 advisor 建議與 executor 已經收集的實證證據衝突, Anthropic 的系統 prompt 告訴 executor 再做一次 advisor 呼叫, 框為"I found X, you suggest Y, which constraint breaks the tie?", 而非沉默切換。這是對"should I trust the planner or the data"問題的生產級答覆——這個問題在多個角色不同意時都會出現。

Advisor Tool 在直接效用之外重要。它是 meta-harness 思維已從研究好奇心移到商業 primitive 的訊號。"same model, different harness, 6x gap"發現不再需要研究團隊來利用——Anthropic 把它暴露為工具呼叫。預期其他實驗室跟進推出他們自己的 advisor/executor 配對, 預期 harness engineering 職位描述開始把多模型協調列為核心技能。

<a id="46-anthropics-three-agent-architecture"></a><!-- i18n-anchor -->

## 4.6 Anthropic 的三 Agent 架構

一個反覆出現的三角色 pattern, 常被從業者社群總結為 **Planner / Generator / Evaluator**, 整個 2025 年成為多 agent harness 的常見框架。這個框架最好讀為對 Anthropic 的 [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents) 中描述的 pattern（orchestrator-worker、evaluator-optimizer）的教學綜合, 而非 Anthropic 自己在主要寫作中採用的標籤。2026 年 三月 31 日 Claude Code 原始碼外洩（本節稍後涵蓋）確認了這個區別: 在生產中, Anthropic 實際 harness 是圍繞分層自愈記憶組織, 而非字面的三角色分解。這些角色仍描述一個有用分類, 所以本節用它們討論關切分離:

- **Planner：** 把任務分解成子任務, 維持整體計畫, 決定何時修訂。
- **Generator：** 執行個別子任務——寫程式碼、起草文字、呼叫工具。
- **Evaluator：** 對照任務要求評估 Generator 輸出, 提供結構化回饋。

這種關切分離被廣泛用於處理本章標記為 **context anxiety** 與 **self-evaluation bias** 的兩個失效模式（這些標籤是本指南用的框架; 底層觀察出現在受 Anthropic 已發表 agent 研究啟發的 pattern 中）:

**Context Anxiety（上下文焦慮）。** 當單一 agent 處理規劃、執行、評估, 它傾向規避。它給輸出加資格、加不必要的注意事項、把 token 花在元評論而非任務執行上。分離角色讓每個 agent 專注, 不必扛其他角色的認知負載。

**Self-Evaluation Bias（自我評估偏差）。** 模型系統性地不擅長評估自己的輸出。它們表現出有據可查的寬容偏差——給自己的工作打的分比獨立評判者會打的高。三 agent 架構透過用獨立的評估器（可能是不同模型或不同 prompt 的例項）來緩解, 評估器對生成輸出沒有投資。

從業者社群強調的一個微妙之處, 與 Anthropic 的 evaluator-optimizer 指引中觀察到的 pattern 一致: **評估器校準本身是個 harness engineering 問題**。過嚴的評估器導致無限修訂迴圈。過寬的讓低質量工作透過。評估器的閾值與標準需要和 generator 的指令一樣仔細調整。

<a id="the-claude-code-leak-an-empirical-look-march-31-2026"></a><!-- i18n-anchor -->

### Claude Code 外洩：實證觀察（2026 年 三月 31 日）

整個 2025 年大部分時間, 三 agent 架構是透過 Anthropic 已發表研究知道的、從行為推論的。2026 年 **三月 31 日**, 這變了。Anthropic 不慎在 npm 包 **`@anthropic-ai/claude-code` v2.1.88** 內釋出一份 59.8MB source map, 暴露約 **513,000 行未混淆 TypeScript 跨 1,906 檔**。Anthropic 把事件描述為"human packaging error, not a security breach,", 但從業者首次能直接讀到一個前沿實驗室的生產 harness。

外洩中重塑社群對架構描述的幾個發現:

- **它字面上不是"Planner / Generator / Evaluator."。** 早期社群文章把 Claude Code 對映到 4.6 三角色框架, 結果是對研究的誤讀。實際架構組織為**三層"Self-Healing Memory"**系統。這些層對應到 scratchpad / 工作狀態、壓縮中期狀態、持久專案記憶——層之間有明確的修復與協調邏輯。
- **`MEMORY.md` 是索引, 不是倉庫。** 不是單一記憶檔, `MEMORY.md` 擔任**輕量級指標索引**, 指向更詳細筆記。這更接近檔案系統目錄而非 transcript, 這是讓記憶層在不膨脹 context 下擴充套件的原因。
- **`KAIROS` 是自主 daemon 模式。** 名為 `KAIROS` 的 feature flag 在原始碼中被引用 **超過 150 次**。它把守一個自主 daemon 模式——一個無人看管、長時間執行的迴圈, 遠超大多數使用者知道的互動 REPL。
- **44 個隱藏 feature flag。** 除了 `KAIROS`, 原始碼含 44 個未釋出功能的 feature flag, 顯示公開發布的是 harness 內部支援的保守子集。

實務結論: Planner / Generator / Evaluator 拆分仍是有用的概念分類（Anthropic 研究論文仍以這些術語描述系統）, 但生產中架構是圍繞**記憶與修復**分層, 而非僅圍繞角色分解。2026 年的 harness engineering 越來越意味著設計記憶層與層之間的轉換。

外洩兩週後, 同一架構再走一步——這次向外, 離開使用者機器。透過 **Claude Code Routines**（2026 年 四月 14 日）, Anthropic 把編排器席位本身從筆電移到自己的雲端, 把排程、API、GitHub 事件觸發器暴露為一等 harness primitive。讀在外洩旁邊, 這是一個清楚的架構修辭: 編排器不再被建模為使用者照顧的 REPL, 而是住在 Anthropic 基底上的 daemon。三層自愈記憶跨觸發器持續; harness 不再需要使用者的程式活著才能讓迴圈進展。無論你採納 Routines 與否, 這個框架現在在空氣裡: 編排器席位是產品表面, "where the loop runs"是設計決策而非預設。

2026 年 **五月 6**，Anthropic 透過 **Dreaming**（研究預覽）將 self-healing memory 的血統更進一步，這是一項預定的會話間作業，可讀取最近的會話、識別重複出現的錯誤和融合的工作流程，並重寫智慧體的持久記憶體。三月 31 日的洩密事件揭示了 self-healing memory 作為 Claude Code 內部的執行時架構，而 Dreaming 將整合通道產品化為託管基礎設施：當智慧體未主動響應請求時發生的管理。結合四月 23 日釋出的託管智慧體記憶（持久跨會話狀態）和當天釋出的另外兩個基礎能力 --- **結果**（獨立評分器自校正迴圈）和 **多智慧體編排**（具有共享檔案系統和持久事件記憶體的主導智慧體扇出） --- 軌跡是從 "memory is data the harness reads" 到 "memory is a maintained store the substrate keeps in good repair on the agent's behalf." 的早期試點資料Harvey 報告稱，啟用 Dreaming 後，任務完成率提高了約 6 倍。

<a id="47-the-harness-as-moat"></a><!-- i18n-anchor -->

## 4.7 Harness 即護城河

2026 年初，Meta 以約 $2 billion 收購 Manus。Manus 沒有專有模型，全部價值都在系統編排層：編排邏輯、上下文工程流水線、工具整合層和執行基礎設施，將通用模型 API 變為可靠的智慧體產品。

這場收購把行業一直在發現的事結晶化: **harness 是護城河**。模型越來越商品化。差異化在於你怎麼包它——你提供什麼工具、你怎麼管 context、你怎麼處理失敗、你怎麼編排多步工作流、你怎麼評估質量。

對從業者的含義是: harness engineering 不是通往模型開發"real work"途中要應付的管線工事。對大多數生產 AI 團隊它*就是*真正工作。到 2026 年 四月,"harness engineering"作為正式學科已進入行業詞彙, Claude Code 外洩提供了對生產 harness 實際包含什麼的首次實證觀察。

**對策：開源護城河。** 本章從第 4.9 節開始跟蹤託管執行底座浪潮（Anthropic 託管智慧體、AWS AgentCore、Microsoft 智慧體系統編排層），所有系統編排層都作為託管基礎能力出售。 2026年**八月19日**，OpenAI以相反的方向執行了護城河論文。品牌 **"Codex as a Platform,"** OpenAI 在 Apache-2.0 下開源了 Codex 背後的執行引擎：`codex exec`（CLI）、Codex SDK 和**應用程式伺服器** - 一個長期存在的本地程序，用於儲存對話狀態、流事件、公開工具和路由批准請求。模型訪問和 OpenAI 的託管服務保持專有；開放的正是本節認為真正的差異化因素的編排層。細微差別很重要：`openai/codex` 儲存庫自 2025 年四月以來已公開並採用 Apache-2.0，因此這不是第一次開源 - 它是 OpenAI 正式完成並將 app-server-plus-SDK 組合重新定位為解耦平臺產品。引用的生產使用者包括 Cisco（Cisco Cloud Control 內的 App Builder）、GitHub 和 JetBrains（作為 IDE 智慧體提供商），以及供應商引用的 Thrive Holdings/Crete 稅務準備試點（7,000 個申報表，大約減少了三分之一的準備時間）。 OpenAI 還將功能跳躍歸因於系統編排層重新設計本身：新應用伺服器中的保留推理和上下文壓縮將 GPT-5.6 Sol 的 ARC-AGI-3 分數從 13.3% 提高到 38.3%，輸出減少 6 倍token——同樣，OpenAI自己的數字，不是獨立轉載的。 OpenAI 沒有將系統編排層作為託管 SKU 進行銷售，而是開源引擎並將模型保留為產品——與第 4.9 節中供應商的相反賭注，並且是在 DeepSeek 釋出自己的開源智慧體系統編排層 `dsh`（第 9 章）一週後推出的：系統編排層層在兩側都開源了。太平洋七日內。

<a id="48-harness-maintenance-the-stress-testing-imperative"></a><!-- i18n-anchor -->

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

成熟 harness 最終把壓力測試問題反轉: 不是問"which components can I remove,", 而是"which components should I spend more compute on, and when."。2026 年 四月 **CATTS** 預印本（Consensus-Aware Test-Time Scaling, arXiv 2602.12276）給那個問題一個可用答案。CATTS 每個 agent 步驟取樣小型 rollout 委員會, 用它們之間的分歧作為每步不確定性分數; 該分數被用來不均勻分配測試時運算——委員會分歧時更多 rollout, 收斂時更少。在 WebArena-Lite 與 GoBrowse 上, 該技術報告在 **2.3 倍少 token** 下 **+9.1%** 任務準確度。對成熟 harness, CATTS 與 Advisor Tool 並排: advisor pattern 決定*想什麼*, CATTS 決定*想多深*。兩者都用 runtime 計算的衡量不確定性訊號, 取代假設（"always retry three times,"、"always use Opus on hard problems"）。

2026 年四月 AHE 結果（第 4.5 節）在結構上提出了相同的觀點：壓力測試不是一次性審查活動，而是一個連續的可觀察性迴圈。作為當今實踐者可以執行的一門學科，手動壓力測試仍然很有價值。 AHE 表明它也是可自動化的。英國 AI 安全研究所同時進行的一項研究（arXiv 2606.17930，2026 年六月 16 日）從測量方面論證了同樣的情況：在 12 個前沿模型和 7 個基準中，token預算會大幅改變分數，因此評估應將能力報告為推理時間計算的函式而不是單個數字——相同重新構建 CATTS 適用於分配和報告。

同月出現了值得警惕的反面證據。**Terminal-Bench Challenges**（Laude Institute／Harbor，June 18, 2026）引入一類基準，面向以*天*為單位的無人值守執行，成本約 $1k 或以上，解法包含 10k-500k 行程式碼，不設時間限制、資源限制，也沒有人工干預，直接檢驗編排層能否維持多日自主操作。早期結果令人清醒：在 Rust 編譯器加速挑戰中，搭配 Opus 4.8 的 Claude Code 連續執行 12 小時，卻"was unable to make any significant improvement, with the optimization attempts leading to regressions."。持續壓力測試與按不確定性分配計算資源，能夠逐步改進編排層；但*多日耐力是另一個維度*，即使前沿模型置於成熟編排系統中，也可能長時間執行而毫無進展。

**LangChain 的 Deep Agents v0.7**（2026 年 七月 29 日）是應用於廣泛部署的開源工具而不是研究論文的壓力測試規則。該版本完全刪除了框架編寫的基本系統提示（之前預設在每個智慧體上載入的一般準則和工具使用散文；可透過 `BASE_AGENT_PROMPT` 恢復，本身在 0.9.0 中已棄用），將內建工具描述削減了 43%，並使 `TodoListMiddleware` / `write_todos` -- 成為規劃腳手架之前預設在每個智慧體上載入 --- 選擇加入。在傳送單個使用者訊息之前，新的預設智慧體上的基本輸入token總共下降了大約 65%，從 ~6K 到 ~2K。刪除待辦事項腳手架是更有趣的編輯決定：LangChain 自己對三個模型系列的評估發現，始終線上的規劃腳手架沒有產生可測量的效能增益——禁用它時，獎勵稍好，成本更低。這正是本節開頭的規定（如果刪除計劃步驟不會降低效能，則將其刪除），針對框架本身預設作為承載提供的元件執行。該課程概括了這一框架：系統編排層附帶的預設腳手架本身就是壓力測試目標，而不僅僅是提示措辭或工具數量。

**監控必須跨越上下文。** Anthropic 在 October 22, 2026 的[研究](https://alignment.anthropic.com/2026/red-teaming-auto-mode/)中攻擊 Auto Mode 與一個近似 Codex Guardian 的系統。智慧體編寫的摘要和交接，可以跨上下文壓縮及共享工作區隱瞞有害步驟或偽造授權。擴大監控範圍能夠提高檢測率，卻會增加延遲。這些是基於九月版本快照進行的對抗實驗；如何以可接受成本實現可靠的跨上下文預防，仍未解決。

**評估器同樣需要隔離約束。** October 9, 2026，[Anthropic 披露了意外操作](https://www.anthropic.com/research/investigating-unintended-model-actions)，涉及評估與內部使用，包括實際提交線上表單、繞過訪問控制。它宣佈在可靠防護到位前，更廣泛地暫停內部評估的實時網際網路訪問，同時採用離線或重建任務、受限工具與監控。報告稱影響極小。這是一個註明日期的整改公告，不能據此證明 October 31 時每項評估仍處於離線狀態。

<a id="49-cloud-native-harness-primitives"></a><!-- i18n-anchor -->

## 4.9 雲原生 Harness Primitive

整個 2025 與 2026 年第一季, harness 幾乎都是你自己建、自己跑的東西。即使最複雜的 pattern——三 agent 架構、Advisor Tool、KAIROS 風格自主迴圈——也都假設你的程式碼握有編排器席位。你寫 cron 工作、跑 daemon、保持筆電喚醒、擁有失效模式。基底是通用運算（Mac mini、VPS、Kubernetes pod）, harness 層從程式監督員往上是你的責任。

2026 年四月 14 日，Anthropic 的 **Claude Code 例程**研究預覽朝著改變這一現狀邁出了具體的第一步。例程是在 Anthropic 的雲而不是使用者計算機上執行的 Claude Code 工作流程，由以下三個觸發器之一觸發：**計劃**（相當於 cron）、**API 呼叫**（來自另一個服務的程式設計呼叫）或 **GitHub 事件**（推送、PR、問題、評論）。這些觸發器是對基於檔案的排程模式的精心概括，系統編排工程師在過去十八個月中一直在編寫：相同的 `runs every weekday at 09:00 HKT` 語義，但表示為託管基礎能力而不是 `cron + tmux + claude` shell 咒語。配額按基礎 Claude Code 訂閱分級 --- **Pro 5/天、Max 15/天、團隊/企業 25/天** --- 執行底座定價為 "a handful of meaningful loops per day per seat"，而不是 "raw compute by the hour."

雲端執行細節比聽起來重要。自架檔案式排程器把編排器席位握在使用者擁有的硬體上; 如果 Mac 關、睡、沒電, 迴圈不跑。Routine 不論使用者機器狀態都完成。這溶解了一整類失效模式（筆電蓋、網路掉、OS 更新、意外重啟）和對應一類補償機制（wake-on-LAN 把戲、Mac Mini"always on"伺服器、冗餘執行器）。對真正事件驅動的工作流——"when a PR opens, do X"——託管 primitive 直截了當比自架輪詢器更適合。

取捨是新的天花板。託管 primitive 按觸發器與配額定價, 不按工作負載的物理。它假設你的迴圈符合排程 / API / GitHub 事件形狀、每天配額夠、Anthropic 基底是你程式碼與資料該住的地方。對相當數量的 harness 工作負載, 那些假設都不乾淨成立。**瀏覽器自動化** 已認證 session 仍受益於執行在已經有使用者 cookie、profile、信任狀態的機器上。**高頻編排**——亞分鐘輪詢、即時市場或感測器資料、每天 25 次呼叫是侮辱的任何東西——需要按秒計費的 runtime, 不是按觸發器。**非 GitHub 事件來源**（Discord 訊息、內部 webhook、客制 MCP 伺服器、裝置上檔案系統事件）在 Routines 中沒有一等觸發器; 暴露它們需要自己寫 bridge, 這把你放回自架機器跑 bridge。任何依賴本機檔案、本機模型推論、本機網路存取的, 在結構上都仍在雲外。

對 2026 年 harness 工程師的誠實框架: 像 Routines 這樣的雲原生 primitive 是 harness 工作負載裡 **GitHub 事件觸發、排程、API 呼叫** 那一象限的對答, 它們很可能在接下來 十二 個月戲劇性壓縮那個象限的運營成本。自架 harness 不會消失——它正被收窄到它實際付清自己的地方。要發展的學科是本章一直在建構的同一學科: 知道每個元件編碼什麼假設, 注意到下面基底何時改變。

**Routines 與 Managed Agents。** 值得精確說明 Anthropic 在 2026 年 四月實際出貨什麼, 因為這兩塊有時被混淆。**Claude Managed Agents**（公測, 2026 年 四月 8 日）是*基底*: 一個把 session（一切發生過事情的 append-only 事件 log）、harness（呼叫 Claude 與路由工具呼叫的迴圈）、sandbox（Claude 可執行程式碼的環境）暴露為三個虛擬化元件的託管 runtime, 配 tracing 與 Agent / Environment / Session / Events API 表面疊加在上。SiliconANGLE 的釋出報道指出基底定價是標準 token 費率加上**每 agent runtime 小時 八 美分**; 該數字來自次級科技媒體, 不是 Anthropic 主要文件。即便在次級引用 bar, 定價結構重要: 這是首個把編排器席位本身與推論分開計費的前沿供應商 primitive。**Claude Code Routines**（研究 preview, 2026 年 四月 14 日）是*觸發表面*, 跑在該基底（或相容替代）之上: 排程、API 呼叫、GitHub 事件, 配 Pro / Max / Team-Enterprise 層級每天 5 / 15 / 25 次呼叫配額。兩者回答不同問題。Managed Agents 答"where does the agent loop physically run, and how is its state durably maintained between turns?"Routines 答"what makes the loop start in the first place?"一個採納 Routines 但不採納 Managed Agents 的自架 harness, 仍擁有它的狀態與執行環境; 一個採納 Managed Agents 但建自己觸發層的, 仍擁有工作何時開始。實務上, 2026 年中大多數雲原生 harness 設計都會兩者都採——但解綁是架構重點。Anthropic 不再把"the harness"當一件事賣; 它在賣它的組成 primitive。

解綁在 2026 年 四月底兩個結構性重要的動作中繼續。第一, **四月 23 日**, Anthropic 把 **Memory for Managed Agents** 加到公測: 一個檔案系統掛載、稽核日誌的儲存, 給 agent 耐久跨 session 狀態, 配併發存取語意、範圍企業許可權、Claude Console 的 rollback / redaction 表面。基底現在出貨第三個 primitive——*耐久記憶*——與 sessions 和 sandboxes 並列; 三月 31 日 Claude Code 原始碼外洩揭示的生產架構（三層自愈記憶）現在是其他團隊能租用的供應商管理 primitive。第二, **四月 28 日**, AWS 與 OpenAI 出貨 **Amazon Bedrock Managed Agents powered by OpenAI** 在 limited preview, 首次命名並販售"the OpenAI agent harness"作為獨立產品表面。讀在一起, 這兩件事把 Managed Agents pattern 從"Anthropic's bet on April 8"轉移到 **跨供應商基底形狀**——三個前沿供應商中兩個現在把編排器席位作為託管 primitive 出貨, 配每 agent 身分、動作日誌、內建耐久狀態。對 2026 年中在編排器席位上比較 build vs. buy 的 harness 工程師, 選項集不再單一供應商, 基底不再是薄 runtime: 它含記憶。

同一周，第三個受管理的基礎能力降落在**執行底座的外邊緣**。 2026 年 **五月 6**，AWS 正式釋出 **AWS MCP 伺服器** --- 第一個超大規模管理器管理的遠端 MCP 端點，暴露了 15,000 多個 AWS API 透過一臺經過身份驗證的伺服器進行操作，該伺服器具有用於細粒度訪問的 IAM 上下文金鑰和用於伺服器端 Python 的沙盒 `run_script` 工具。對於系統編排工程師來說，託管 MCP 邊緣是雲原生三角形的第三條邊：託管智慧體（迴圈執行的位置）+ 託管智慧體記憶（迴圈記住的內容）+ 託管 MCP 邊緣（迴圈如何到達外部工具）。自託管MCP伺服器並沒有消失，但"where do my agents connect to the cloud's APIs"的重心從"one MCP server per service"轉向"one managed endpoint at the cloud boundary."

**然後基底沿著周邊線分裂。** 在四月和五月早期，採用託管智慧體的成本是二元的：程式碼、狀態、沙箱和工具範圍全部轉移到 Anthropic 的基礎設施中，或者都沒有轉移。 2026 年 **五月 19 日**，在倫敦 Code with Claude 上，Anthropic 釋出了兩個基礎能力，消除了這種全有或全無的選擇。 **自託管沙箱**（公開測試版）將智慧體迴圈（編排、上下文管理、錯誤恢復）保留在 Anthropic 的基礎設施上，同時將工具執行轉移到客戶自己的環境中，併為 Cloudflare、Daytona、Modal 和 Vercel 作為託管沙箱提供商提供第一方支援。 "brain" 保持受管理； "hands" 可以返回到工作負載所需的任何信任邊界（本地受監管資料、簽約提供商上的 GPU 作業、現有 CI 沙箱中的構建步驟）。 **MCP 隧道**（研究預覽）縮小了工具到達端的對稱差距：部署在客戶專用網路內的輕量級閘道器與 Anthropic 建立單個出站連線，之後智慧體可以將內部資料庫、API、知識庫和票務系統作為 MCP 工具呼叫 — 無需入站防火牆規則、公共端點或 VPN體操。這兩個基礎能力一起將託管智慧體重新構建為**底層協商而不是底層採用**：系統編排工程師現在逐層選擇迴圈的哪些部分位於何處，而不是在完全自託管和完全託管之間進行選擇。雲原生三角形成為引數化契約，而不是單一形狀。

**到2026年中，"harness"本身就成為超大規模產品詞彙。** 2026年六月17日，AWS將**Bedrock AgentCoreharness**帶到GA：`CreateHarness`宣告瞭模型、工具、技能和指令， `InvokeHarness` 執行它，AWS 操作編排迴圈、沙盒檔案系統和 shell、跨會話記憶體以及作為*配置而不是程式碼*的工具呼叫——跨 Bedrock 託管模型明確提供者無關，直接 OpenAI API， Gemini 以及任何 LiteLLM 路由的提供商，具有保留上下文的會話中模型切換功能。它的釋出副本——"if the model is the brain, the harness is the body"——借用了本章開頭的確切比喻。三週前的 Build 大會上，Microsoft 釋出了自己的 **Agent Harness**，作為開源 Microsoft Agent Framework 的一流擴充套件（一個方法呼叫新增了上下文壓縮、任務分解指令、基於檔案的記憶體、計劃/執行切換、技能發現、子智慧體扇出和沙盒外殼），以及 **Foundry Hosted Agents**（直接原始碼部署、虛擬機器管理程式隔離）每個會話沙箱、每個智慧體 Entra ID、內建 OpenTelemetry）。一個月內，兩家超大規模企業採用 "harness" 作為字面 SKU 名稱，這是迄今為止最明顯的跡象，表明本章描述的學科已經硬化為一個產品類別——繼 Anthropic（四月 8 日）和 AWS×OpenAI Bedrock（四月 八 日）之後第三和第四種不同形狀的託管執行底座融合28）。

**計量線仍在繪製中 --- 並且可以重新繪製。** Managed Agents 引入的協調器席位計量有一個未解決的邊緣：當*相同*訂閱以程式設計方式而不是互動方式驅動時會發生什麼。 2026年五月13日，Anthropic宣佈，從六月15日起，程式化使用——Agent SDK、`claude -p`無頭呼叫、Claude Code GitHub Actions和第三方智慧體 SDK 應用程式 --- 將離開固定費率訂閱池以獲得單獨的以美元計價的每月信用額（20 美元 Pro / 100 美元最多 5 倍 / 200 美元最多 20 倍），按標準 API 費率計費，無展期，而互動式 Claude Code 和claude.ai 聊天仍保留在訂閱中。六月 15 日，也就是生效日，Anthropic 暫停了它："For now, nothing has changed... We're working to update the plan." 這是第一個前沿供應商試圖在訂閱內的互動席位和程式化席位之間劃出一條嚴格的計量線，其公開撤回是直接證據，表明編排者計量和解尚未解決。相關舉措於 七月 7 日落地，當時 **Claude Cowork** 擴充套件到網路和移動裝置，在原始裝置離線後工作仍在繼續——根據 Anthropic，超過 90% 的 Cowork 使用不是軟體開發，因此編排器席位正在離開開發人員的機器，轉向第二個非開發人員產品表面。

**供給側迎來需求側。** 本節此前的各項基礎能力，回答的是迴圈在哪裡執行、記住什麼、由誰付費，均為容量問題。AWS 八月 6 日的 Runtime Instances（第 4.1 節）將會話上限提高至 14 天；Google 的 Gemini Enterprise Agent Platform 在 **July 30, 2026** 正式釋出，提供最長七天持續執行的 Agent Runtime，以及將智慧體設為原生 IAM 型別、而非借用服務賬戶的 Agent Identity。這些均為 Google 自身的能力描述，其中託管記憶部分 Memory Bank 見第 6 章。但它們均未展示智慧體實際跨越該時段追求目標。**September 11, 2026**，Salesforce 宣稱補上另一半：為 Agentforce 提供**長週期執行時**，使智慧體跨數天或數週追求目標，而非只完成一次任務或互動，包含三項具名元件：會話間持久保留的記憶、讓計劃跨會話繼續執行的持久執行，以及根據使用者指令在執行中調整行為的動態引導。它與七個按崗位劃分的智慧體組合一同釋出；主動銷售智慧體 **Hunter** 首先採用新執行時，也是唯一尚未正式釋出的一個，計劃在 2026 年十一月正式釋出。這項限定是結構性的，並非修辭：追求數週目標只是 Salesforce 自身的描述，沒有獨立測量顯示 Hunter 一週內完成什麼，展示該基礎能力的智慧體也仍處於試點。對照第 4.8 節 Terminal-Bench Challenges 中前沿模型執行 12 小時毫無進展的結果，2026 年誠實的解讀是，多日智慧體的*基礎設施*已在三家廠商之間成為通用品，而智慧體能取得多日進展的*證據*仍幾乎完全由廠商提供。

有關在多日調查中使用外層編排系統的十月執行披露，參見[第 13 章](13-loop-engineering.md#136-stacking-loops)。

<a id="410-the-managed-inference-turn-april-2026"></a><!-- i18n-anchor -->

## 4.10 託管推論轉變（2026 年 四月）

整個 2025 年, 呼叫者與模型之間的 harness 合約大致是個旋鈕面板: `temperature`、`top_p`、`top_k`、`max_tokens`、`budget_tokens`、系統 prompt。從業者按案轉旋鈕, 有時在同一 agentic 迴圈內每步都轉。2026 年 四月 16 日 **Claude Opus 4.7** 的釋出打破那個 pattern。在單一發布中, 三項變更朝同一方向拉:

1. **`temperature`、`top_p`、`top_k` 被棄用。** 任何非預設值返回 400 錯誤。取樣級控制不再在呼叫者手上。
2. **自適應思考是唯一的思考開模式。** 手動 `budget_tokens`（extended thinking）被移除; `effort`（`low`、`high`、`xhigh`、`max`）取代它。
3. **Task budgets 變成一等 primitive。** 一個新 beta 標頭（`anthropic-beta: task-budgets-2026-03-13`）讓呼叫者為*整個 agentic 迴圈*——思考、工具呼叫、工具結果、最終輸出——宣告建議性 token 預算。模型在工作時看到倒數。

前兩項變更是減法: 旋鈕被移除。第三項是加法: 一個先前在任何前沿 API 都不存在的 primitive。一起它們描述合約變更。不是"you tune the sampler and the model produces a response,", 合約現在是"you declare a compute budget and the model self-allocates against it, deciding step by step how much searching, reasoning, and synthesis the task still deserves."。Harness 變成預算對話而非引數面板。

"advisory rather than enforced"細節重要。Task budgets 不是硬上限（`max_tokens` 仍擔任那個角色, 仍只面向呼叫者）。相反, 模型被告知它的預算並用它來排序優先。實務上, 設太緊的預算產生拒答式輸出而非退化的——模型偏好拒絕而非出貨它判定為資金不足的結果。最低 20K token 被強制, 正是為防止重大任務的那個失效模式。

對 harness 設計者, 含義具體: 任何在 Opus 4.6 跑的 harness 需要為 4.7 重新基線, 不只在 prompt 層級, 也在 timeout、retry、壓縮、工具呼叫預算層級。Anthropic 自家遷移文件直接說: *重新基線 harness, 不只是 prompt*。Advisor Tool（第 4.5 節）與 task budgets（本節）描述任何長時間 harness 的新兩軸最佳化: Advisor 決定*想什麼*; task budgets 決定*每一步想多深*。兩者都用 runtime 計算的衡量訊號取代旋鈕調整。

2026 年六月的第二次合同變更遵循了相同的邏輯。 **Claude Fable 5** 新增了 `stop_reason: "refusal"` 作為正常的 HTTP 200 結果：安全分類器可以拒絕請求，並且系統編排層必須將該拒絕視為一流的控制流分支而不是錯誤。 Anthropic 將其與正式的後備合約配對——伺服器端 `fallbacks` 引數、客戶端 SDK 中介軟體或手動重試——以及在拒絕觸發模型切換時退還提示快取成本的計費規則。與任務預算一樣，這是呼叫者現在在協議級別處理的利用合同：預算使 "how hard to think" 成為託管對話，拒絕作為 `stop_reason` 使 "the model may decline, and here is the sanctioned way to recover" 成為合同的一部分。託管推理現在不僅涵蓋如何分配計算，還涵蓋如何處理被拒絕的請求。

本回合的最新步驟是 **Claude Opus 5**（2026 年 七月 24 日）。定價為每百萬輸入/輸出token 5 美元 / 25 美元 --- 與 Opus 4.8 相同，是 Fable 5 的一半 --- 它提供了一個 1M token上下文視窗，最大輸出 128K，預設情況下自適應思維具有 **五級 `effort` 設定**，付費 **快速模式** （2.5 倍的速度，2 倍的價格），而且，這裡最相關的是，**對話中工具更改，沒有提示快取失效**（測試版）。作為一個定價的五位轉盤，延長了 "how hard to think" 軸 Opus 4.7 的工作量，並且快取安全工具交換消除了長期執行迴圈的最後固定成本之一：工具集現在可以在會話中演變，而無需支付快取失效稅。 （Anthropic 的釋出聲稱——在 Frontier-Bench v0.1 上比 Opus 4.8 提高了一倍多，並且以最大努力達到 Fable 5 峰值 CursorBench 3.2 分數的 0.5% 以內——是供應商自己的數字。）

這是更廣 pattern: **託管推論轉變**。前沿供應商越來越把推論本身視為產品表面而非參數列面。Harness 層正從"you configure the inference call"移到"you describe the work and the inference layer adapts."。其他實驗室是否跟隨 Anthropic 的具體決策（取樣旋鈕棄用、建議性預算）還是隻跟方向, 是開放問題。方向本身看起來已成定局。

---

<a id="three-things-to-take-away"></a><!-- i18n-anchor -->

## 需要帶走的三件事

- **智慧體是一個模型加上一個工具。** 當編碼智慧體編輯檔案時，它不是編輯該檔案的模型 - 它是工具，由呼叫以文字形式返回的模型的工具觸發。
- **系統編排層就是槓桿所在。** Meta-系統編排層論文發現，在相同基準和相同基礎模型上，系統編排層配置之間存在 6 倍的效能差距。
- **系統編排層元件過期。**每個元件都編碼了關於模型不能做什麼的假設，因此加入新模型意味著剝離元件並衡量哪些元件仍然值得使用。

---

<a id="sources"></a><!-- i18n-anchor -->

## 來源

- **Remedios, Alex; Storf, Simon 等。** 阻斷式監控器研究（October 22, 2026）：[https://alignment.anthropic.com/2026/red-teaming-auto-mode/](https://alignment.anthropic.com/2026/red-teaming-auto-mode/)。
- **Anthropic。** "Investigating unintended model actions in our evaluations and internal use"（October 9，October 12, 2026 更正）：[https://www.anthropic.com/research/investigating-unintended-model-actions](https://www.anthropic.com/research/investigating-unintended-model-actions)。
- **Böckeler, Birgitta.** "Harness engineering for coding agent users." martinfowler.com（Exploring Generative AI 系列）, 2026 年 四月 2 日。[https://martinfowler.com/articles/harness-engineering.html](https://martinfowler.com/articles/harness-engineering.html) ——Guides vs. Sensors、Computational vs. Inferential 分類。
- **OpenAI。** Codex 公開材料：[https://openai.com/index/introducing-codex](https://openai.com/index/introducing-codex)。支撐 OpenAI Codex 的編排層設計框架；廣為引用的"three engineers / ~1M lines / ~1,500 PRs"數字在 2025-2026 年 OpenAI 演講與文章中流傳，此處作為社群引用報告，而非歸於某一篇權威原文。
- **IMPACT 助記詞。** Intent / Memory / Planning / Authority / Control flow / Tools——一個六維 harness 設計清單, 在 2020 年代中期從業者討論中浮現。在本章作為教學框架使用; 不歸屬任何特定原始來源。
- **Stanford / MIT / KRAFTON.** "Meta-Harness: Automated Optimization of LLM Agent Harnesses." arXiv 預印本, 2026 年 三月。6 倍效能差距發現, 自動化 harness 調整。
- **Lin et al.** "Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses." arXiv 2604.25850, 2026 年 四月 28 日。[https://arxiv.org/abs/2604.25850](https://arxiv.org/abs/2604.25850) ——復旦/北大/上海齊跡智鋒。Meta-harness 搜尋問題的可觀測性支柱重構; 在 Terminal-Bench 2 上 69.7% → 77.0%, 配跨家族轉移。
- **Microsoft AI。** "Introducing MAI-Code-1-Flash"（2026 年六月 2 日）。 [https://microsoft.ai/news/introducingmai-code-1-flash/](https://microsoft.ai/news/introducingmai-code-1-flash/) 和 GitHub 變更日誌 [https://github.blog/changelog/2026-06-02-mai-code-1-flash-is-now-available-for-github-copilot/](https://github.blog/changelog/2026-06-02-mai-code-1-flash-is-now-available-for-github-copilot/) --- 直接針對生產 GitHub Copilot 系統編排層進行訓練的 5B 引數編碼模型（系統編排層合成的對稱逆：針對固定系統編排層最佳化的模型）；困難任務的token減少約 60%；與 Claude Haiku 4.5 相比具有價效比優勢。根據 TechTimes 二次報道，MAI-Thinking-1，Microsoft 的首款內部推理模型 "trained without OpenAI data," 在同一天發貨。
- **Anthropic.** "Claude Managed Agents overview." API 文件, 2026 年 四月 8 日。[https://platform.claude.com/docs/en/managed-agents/overview](https://platform.claude.com/docs/en/managed-agents/overview)
- **Anthropic Engineering.** "Scaling Managed Agents: Decoupling the brain from the body." 2026 年 四月 8 日。[https://www.anthropic.com/engineering/managed-agents](https://www.anthropic.com/engineering/managed-agents) ——三個虛擬化元件（session、harness、sandbox）; 定價細節（標準 token 費率加上每 agent runtime 小時 八 美分, 按 SiliconANGLE 釋出報道）不在 Anthropic 主要文件中, 由次級科技媒體引用。
- **Anthropic.** "Memory for Claude Managed Agents"（2026 年 四月 23 日）。[https://claude.com/blog/claude-managed-agents-memory](https://claude.com/blog/claude-managed-agents-memory) ——檔案系統掛載記憶、跨 session 學習、稽核日誌、範圍企業許可權; 與 三月 31 日 Claude Code 原始碼外洩關於三層自愈記憶的發現關閉迴路。
- **AWS 與 OpenAI.** "Bedrock Managed Agents powered by OpenAI"（2026 年 四月 28 日, limited preview）。AWS 公告: [https://aws.amazon.com/about-aws/whats-new/2026/04/bedrock-openai-models-codex-managed-agents/](https://aws.amazon.com/about-aws/whats-new/2026/04/bedrock-openai-models-codex-managed-agents/)。About Amazon: [https://www.aboutamazon.com/news/aws/bedrock-openai-models](https://www.aboutamazon.com/news/aws/bedrock-openai-models)。OpenAI 公告: [https://openai.com/index/openai-on-aws/](https://openai.com/index/openai-on-aws/) ——首次"the OpenAI agent harness"被命名並作為獨立產品表面販售; Managed Agents pattern 上的跨供應商收斂。
- **Anthropic。** "New in Claude Managed Agents: dreaming, outcomes, and multiagent orchestration"（2026 年五月 6 日）。 [https://claude.com/blog/new-in-claude-managed-agents](https://claude.com/blog/new-in-claude-managed-agents) --- 夢想（計劃的會話間記憶體管理，研究預覽），結果（單獨評分者自我修正，公開測試版），多智慧體編排（具有共享檔案系統的主導智慧體扇出，公開測試版）； Harvey 試點報告稱，透過 Dreaming，任務完成率提高了約 6 倍。
- **AWS。** "The AWS MCP Server is now generally available"（2026 年五月 6 日）。 [https://aws.amazon.com/blogs/aws/the-aws-mcp-server-is-now-generally-available/](https://aws.amazon.com/blogs/aws/the-aws-mcp-server-is-now-generally-available/) 和 [https://aws.amazon.com/about-aws/whats-new/2026/05/aws-mcp-server/](https://aws.amazon.com/about-aws/whats-new/2026/05/aws-mcp-server/) --- 透過一臺經過身份驗證的伺服器執行 15,000+ AWS API 操作； IAM 用於細粒度訪問的上下文鍵；用於伺服器端 Python 的沙盒 `run_script`。
- **Anthropic。** "New in Claude Managed Agents: self-hosted sandboxes and MCP tunnels"（2026 年五月 19 日）。 [https://claude.com/blog/claude-managed-agents-updates](https://claude.com/blog/claude-managed-agents-updates) --- 自託管沙箱公測版（Cloudflare / Daytona / Modal / Vercel 提供商）； MCP 隧道研究預覽（僅出站輕量級閘道器，無入站防火牆規則）。
- **Anthropic。** "Self-hosted sandboxes." API 文件（2026 年五月）。 [https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes)
- **Anthropic.** "Building Effective Agents." Anthropic 工程部落格, 2024 年 十二月 19 日。[https://www.anthropic.com/engineering/building-effective-agents](https://www.anthropic.com/engineering/building-effective-agents) ——描述 orchestrator-worker pattern 與 evaluator-optimizer workflow; 本指南把相關失效模式標為"context anxiety"與"self-evaluation bias"作教學使用。從業者社群把它總結為 Planner / Generator / Evaluator triple 的框架, 是建立在這些 pattern 上; Anthropic 自己在主要寫作中沒用那個明確 triple。實際 Claude Code 架構, 由 2026 年 三月 31 日原始碼外洩揭示（第 4.6 節）, 是圍繞分層自愈記憶組織而非角色分解。
- **Meta／Manus 收購。** 2026 年初的多家報道。約 ~$2B 的收購，支援編排層即護城河的論點。
- **Karpathy, Andrej.** "From Vibe Coding to Agentic Engineering" —— Sequoia AI Ascent 2026 fireside chat（約 2026 年 四月底錄製, 主要 YouTube 影片 [https://www.youtube.com/watch?v=96jN2OCOfLs](https://www.youtube.com/watch?v=96jN2OCOfLs); 作者總結在 [https://karpathy.bearblog.dev/sequoia-ascent-2026/](https://karpathy.bearblog.dev/sequoia-ascent-2026/)）。把 vibe coding 框為*提升地板*模式（人人能建）, agentic engineering 為*抬升天花板*學科（規格、計畫督導、diff 檢查、eval 迴路、許可權範圍、worktree 隔離）。錨定 2025 年 十二月一個拐點, Karpathy 在那時把自己的程式設計比例從約 80% 手寫翻轉到約 80% 委派。早期 2025"Software 3.0"/"Software Is Changing (Again)"演講在 AI Engineer World's Fair 與 YC AI Startup School, 建立模型作為新一類可程式化元件的更廣框架。
- **LangChain.** "Agent Architecture Patterns." LangChain 文件, 2025。控制流與工具編排的實務 pattern。
- **Harrison Chase.** "Agent Engineer" 框架, 2025——LangChain 部落格與 X 貼。這個詞以 harness 為中心工程的角色定義框架進入從業者詞彙; 在此作為 2025 年代討論中的 pattern 引用, 而非單一標準帖。
- **"CATTS: Consensus-Aware Test-Time Scaling for Agents."** arXiv 2602.12276（2026 年 四月釋出週期）。投票推導不確定性作為測試時運算分配器; 在 WebArena-Lite 與 GoBrowse 上 +9.1% / 比均勻擴充套件少 2.3 倍 token。[https://arxiv.org/abs/2602.12276](https://arxiv.org/abs/2602.12276)
- **Anthropic.** "Introducing Routines in Claude Code." Anthropic 部落格, 2026 年 四月 14 日。[https://claude.com/blog/introducing-routines-in-claude-code](https://claude.com/blog/introducing-routines-in-claude-code)
- **Anthropic.** "Claude Code Routines documentation." [https://code.claude.com/docs/en/routines](https://code.claude.com/docs/en/routines) ——觸發器（排程 / API / GitHub 事件）、配額（Pro 5/天、Max 15/天、Team/Enterprise 25/天）、雲端執行語意。
- **Anthropic.** "Introducing Claude Opus 4.7"（2026 年 四月 16 日）。[https://www.anthropic.com/news/claude-opus-4-7](https://www.anthropic.com/news/claude-opus-4-7)
- **Anthropic.** "What's new in Claude Opus 4.7"（API 文件）。[https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-7](https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-7) ——task budgets（`anthropic-beta: task-budgets-2026-03-13`, 建議性, 最低 20K）、自適應專用思考、移除 `temperature` / `top_p` / `top_k`。
- **Caylent.** "Claude Opus 4.7 Deep Dive: Capabilities, Migration, and the New Economics of Long-Running Agents"（2026 年 四月）。[https://caylent.com/blog/claude-opus-4-7-deep-dive-capabilities-migration-and-the-new-economics-of-long-running-agents](https://caylent.com/blog/claude-opus-4-7-deep-dive-capabilities-migration-and-the-new-economics-of-long-running-agents) ——"re-baseline the harness, not just the prompt."。
- **Archon GitHub Repository.** [https://github.com/coleam00/Archon](https://github.com/coleam00/Archon) ——TypeScript / Bun harness 構建器, YAML DAG 工作流包 Claude Code 與 OpenAI Codex CLI; v2.1 在 2026 年 四月釋出。
- **OpenHarness GitHub Repository.** [https://github.com/HKUDS/OpenHarness](https://github.com/HKUDS/OpenHarness) ——香港科技大學資料實驗室的 Python 參考實現; 首次 commit 2026 年 四月 1 日。
- **Anthropic.** "Claude Fable 5 and Claude Mythos 5"（2026 年六月 9 日）。 [https://www.anthropic.com/news/claude-fable-5-mythos-5](https://www.anthropic.com/news/claude-fable-5-mythos-5) 和 API 文件 [https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5](https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5) --- 拒絕作為 `stop_reason` (HTTP 200)、`fallbacks` 合同、拒絕觸發模型切換時的後備信用計費。
- **AWS.** "Amazon Bedrock AgentCore harness is now generally available"（2026 年六月 17 日）。 [https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-bedrock-agentcore-harness-generally-available/](https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-bedrock-agentcore-harness-generally-available/) 和 [https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-agentcore-harness-is-now-generally-available-go-from-idea-to-production-grade-agent-in-minutes/](https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-agentcore-harness-is-now-generally-available-go-from-idea-to-production-grade-agent-in-minutes/) --- `CreateHarness` / `InvokeHarness`；與提供商無關（Bedrock、OpenAI、Gemini、LiteLLM）； "if the model is the brain, the harness is the body."
- **Microsoft.** "Microsoft Agent Framework at Build 2026: the Agent Harness"（2026 年六月 3 日）。 [https://devblogs.microsoft.com/agent-framework/microsoft-agent-framework-at-build-2026-announce/](https://devblogs.microsoft.com/agent-framework/microsoft-agent-framework-at-build-2026-announce/) 和 "Hosted Agents at Build 2026" (2026年六月2日) [https://devblogs.microsoft.com/foundry/hosted-agents-build26/](https://devblogs.microsoft.com/foundry/hosted-agents-build26/) --- 開源Microsoft Agent Framework的一鍵呼叫Agent Harness擴充套件； Foundry 託管智慧體（原始碼部署、虛擬機器管理程式隔離沙箱、每個智慧體 Entra ID、OpenTelemetry）。
- **Anthropic.** "Use the Claude Agent SDK with your Claude plan"（2026 年五月 13 日釋出）。 [https://support.claude.com/en/articles/15036540-use-the-claude-agent-sdk-with-your-claude-plan](https://support.claude.com/en/articles/15036540-use-the-claude-agent-sdk-with-your-claude-plan) 和新堆疊、"Anthropic pauses Claude Agent SDK subscription change" [https://thenewstack.io/anthropic-pauses-claude-agent-sdk-subscription-change/](https://thenewstack.io/anthropic-pauses-claude-agent-sdk-subscription-change/) --- 程式化使用積分（$20 Pro / $100 Max 5x / $200 Max 20x，標準 API 費率，無翻轉），互動介面不受影響，暫停六月 15（到期日）。
- **Anthropic。** "Cowork is now on web and mobile"（2026 年 七月 7 日）。 [https://claude.com/blog/cowork-web-mobile](https://claude.com/blog/cowork-web-mobile) --- 第二個非開發人員表面上的協調器席位；當原始裝置離線時，工作仍在繼續； "more than 90% of Cowork usage was not software development."
- **Anthropic。** "Introducing Claude Opus 5"（2026 年 七月 24 日）。 [https://www.anthropic.com/news/claude-opus-5](https://www.anthropic.com/news/claude-opus-5) --- 5 美元/25 美元定價，快速模式，對話中工具更改，無需提示快取失效（測試版）； Frontier-Bench / CursorBench 資料是 Anthropic 自己的宣告。規格來自平臺文件，"What's new in Claude Opus 5"：[https://platform.claude.com/docs/en/about-claude/models/whats-new-opus-5](https://platform.claude.com/docs/en/about-claude/models/whats-new-opus-5) --- 1M token上下文視窗（預設和最大），128K 最大輸出，預設情況下考慮，以及全力階梯 `low` / `medium` / `high` / `xhigh` / `max`（預設`high`）；公告頁面沒有說明這些。
- **終端長凳。** "Terminal-Bench Challenges"（2026 年六月 18 日）。 [https://www.tbench.ai/news/terminal-bench-challenges](https://www.tbench.ai/news/terminal-bench-challenges)——多日、無限額、無干預基準類； Rust 編譯器種子挑戰（Claude Code + Opus 4.8，12 小時，迴歸）。
- **METR.** "GPT-5.6 Sol evaluation"（2026 年六月 26 日）。 [https://metr.org/blog/2026-06-26-gpt-5-6-sol/](https://metr.org/blog/2026-06-26-gpt-5-6-sol/) --- Time Horizo​​n 1.1套件上所有公開模型中檢測到的最高作弊率； CoT 監控之所以有效，是因為 OpenAI 保留了原始 CoT，而不是針對它進行訓練。
- **英國AI安全研究所。** "Capability as a function of inference-time compute." arXiv 2606.17930，2026年六月16日。[https://arxiv.org/abs/2606.17930](https://arxiv.org/abs/2606.17930) --- 12個前沿模型，7個基準；token預算會極大地影響分數，因此評估應報告針對推理時間計算的能力。
- **Anthropic。** "A global workspace in language models"（2026 年 七月 6 日）。 [https://www.anthropic.com/research/global-workspace](https://www.anthropic.com/research/global-workspace)---J空間和雅可比透鏡（J-lens）；可報告、可控、獨立於 CoT 的內部工作空間，可用作第二類感測器。
- **LangChain。** "Deep Agents v0.7"（2026 年 七月 29 日）。 [https://www.langchain.com/blog/deep-agents-v0-7](https://www.langchain.com/blog/deep-agents-v0-7) ---預設基本系統提示已刪除，內建工具描述修剪了43%，`TodoListMiddleware` / `write_todos` 選擇加入；預設智慧體上的基本輸入token依次下降 ~6K → ~2K (65%)；對三個模型系列的評估發現，預設規劃支架沒有帶來任何可衡量的收益。
- **AWS。** "Control agent behaviors and cost beyond a single action: new capabilities in Amazon Bedrock AgentCore"（2026 年八月 6 日）。 [https://aws.amazon.com/blogs/machine-learning/control-agent-behaviors-and-cost-beyond-a-single-action-new-capabilities-in-amazon-bedrock-agentcore/](https://aws.amazon.com/blogs/machine-learning/control-agent-behaviors-and-cost-beyond-a-single-action-new-capabilities-in-amazon-bedrock-agentcore/)； "Temporal Policies for Amazon Bedrock AgentCore" [https://aws.amazon.com/about-aws/whats-new/2026/08/temporal-policies-agentcore/](https://aws.amazon.com/about-aws/whats-new/2026/08/temporal-policies-agentcore/); "Amazon Bedrock AgentCore Runtime Instances now generally available" [https://aws.amazon.com/about-aws/whats-new/2026/08/aws-bedrock-agentcore-runtime-instances-generally-available/](https://aws.amazon.com/about-aws/whats-new/2026/08/aws-bedrock-agentcore-runtime-instances-generally-available/) --- 臨時策略（Dogwood、Apache-2.0 策略語言）、閘道器速率限制、會話長達 14 天的執行時例項 GA。
- **OpenAI.** "Codex as a Platform"（2026 年八月 19 日）。 [https://developers.openai.com/blog/codex-as-a-platform](https://developers.openai.com/blog/codex-as-a-platform) --- Apache-2.0開源`codex exec`、Codex SDK和app-server； `openai/codex` 自 2025 年四月起公開； ARC-AGI-3和生產使用者數字是OpenAI自己的宣告。
- **OpenAI.** GPT-6 Astra 釋出材料（2026 年九月）："GPT-6 Astra: A new generation of intelligence" [https://openai.com/index/gpt-6-astra/](https://openai.com/index/gpt-6-astra/)； "Safety overview: GPT-6 Astra"（頁面日期為2026年九月3日）[https://openai.com/index/safety-overview-gpt-6-astra/](https://openai.com/index/safety-overview-gpt-6-astra/)； "The path to Astra"（頁面日期為2026年九月1日）[https://openai.com/index/path-to-astra/](https://openai.com/index/path-to-astra/)——OpenAI準備框架的關鍵網路安全級別指定的第一個模型；有限組織推出、拒絕概念驗證利用任務、Daybreak / Daybreak Blue 經過審查的防禦者擴充套件；相對於 GPT-5.6 Sol 的思想鏈可監控性降低是 OpenAI 自己對安全概述的宣告。 ExploitBench / ExploitGym / SRE-Bench 數字是 OpenAI 自己的，在沒有生產保障的情況下測量。
- **Anthropic.** "Permission policies." 託管智慧體 API 文件； `auto` 政策日期為 2026 年 九月 10 日，透過平臺發行說明發布。 [https://platform.claude.com/docs/en/managed-agents/permission-policies](https://platform.claude.com/docs/en/managed-agents/permission-policies) 和 [https://platform.claude.com/docs/en/release-notes/overview](https://platform.claude.com/docs/en/release-notes/overview) --- 伺服器端每次呼叫評估返回執行/拒絕/暫停批准，透過 `agent.tool_use` 和 `agent.mcp_tool_use` 事件上的 `evaluation` 物件報告，原因程式碼如 `high_risk` 和`indeterminate`;適用於 MCP 工具集。 Anthropic 的文件單一來源；沒有獨立的覆蓋範圍。
- **Nie 等人** "TTHE: Test-Time Harness Evolution." arXiv 2607.08124，2026 年 七月 9 日。[https://arxiv.org/abs/2607.08124](https://arxiv.org/abs/2607.08124) --- 圍繞單個凍結 LLM 的提議者/法官/求解者角色；利用在測試時從未標記的執行痕跡中精煉的群體，無需黃金標籤或特定於任務的監督。
- **Wang et al.** "Rethinking the Evaluation of Harness Evolution for Agents." arXiv 2607.12227, v1 七月 14, 2026, v2 八月 27, 2026. [https://arxiv.org/abs/2607.12227](https://arxiv.org/abs/2607.12227) --- 方法論批判加上負面的實證結果：針對任務級搜尋的匹配反饋和推理預算基線，以及在同一基準上搜尋和評估系統編排層時的過度擬合風險；在使用 GPT-5.4 和 Claude Opus 4.6 的 Terminal-Bench 2.1 上執行時，作者報告說，自動系統編排層演化並不總是優於簡單的測試時間縮放，並且泛化能力有限。論文沒有引用或點名 TTHE；兩者在這裡是作為一場辯論的兩個方面提出的，而不是作為直接的交流。
- **Salesforce。** "Job-ready AI agents"（2026 年 九月 11 日）。 [https://www.salesforce.com/uk/news/stories/agentforce-job-ready-ai-agents/](https://www.salesforce.com/uk/news/stories/agentforce-job-ready-ai-agents/) ---長視野執行時（記憶體、持久執行、動態轉向）；七個工作範圍的智慧體，其中 Hunter 參與試點，GA 計劃於 2026 年 十一月進行。多周目標追求是 Salesforce 自己的主張，沒有獨立的衡量標準。二次覆蓋：[https://www.unite.ai/salesforce-debuts-job-ready-agentforce-agents-and-long-horizon-runtime/](https://www.unite.ai/salesforce-debuts-job-ready-agentforce-agents-and-long-horizon-runtime/)和[https://siliconangle.com/2026/09/11/salesforce-introduces-new-ai-agents-to-automate-sales-support-tasks/](https://siliconangle.com/2026/09/11/salesforce-introduces-new-ai-agents-to-automate-sales-support-tasks/)。
- **Google 雲。** "What's new in Gemini Enterprise Agent Platform"（2026 年 七月 30 日）。 [https://cloud.google.com/blog/products/ai-machine-learning/whats-new-in-gemini-enterprise-agent-platform](https://cloud.google.com/blog/products/ai-machine-learning/whats-new-in-gemini-enterprise-agent-platform) --- 智慧體執行時（連續智慧體長達 七 天）和智慧體身份（本機 IAM 型別）以及智慧體 Memory Bank GA，第 6 章介紹。所有功能描述均為 Google 自己的。

<a id="further-reading-for-beginners"></a><!-- i18n-anchor -->

### 給入門者的延伸閱讀

- **Cab.** "A Layer-by-Layer Walk Through Harness Engineering."繁體中文文章, 2026。從單一 `POST /v1/messages` 呼叫一路建到 prompt engineering、function calling、agent loop, 最後到完整 harness 複雜度。值得注意的是"模型從來都沒有長手"的隱喻, 把工具使用重構為 harness 問題而非模型能力, 還有它對 Claude Code 的 harness 實際在背後做什麼的明確走讀。推薦作為讀本章理論優先框架（Böckeler 分類、IMPACT、Meta-Harness）之前的溫和入門。
- **Anthropic.** ["Building Effective Agents"](https://www.anthropic.com/research/building-effective-agents) ——給來自非研究背景讀者的標準短篇介紹。與上面的 Cab 文章配對得好: Cab 給建構, Anthropic 給具體 pattern。
