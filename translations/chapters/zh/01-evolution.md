# 第 1 章：三個世代

> **一句話總結：** AI 工程已經從寫好 prompt 演進到圍繞 AI 模型設計整個作業系統。
>
> **為什麼重要：** 理解這個領域的走向, 幫助你挑選合適的工具, 避免過時的方法。

**從 prompt engineering 到 context engineering 再到 harness engineering——以及為什麼這些邊界其實沒有你想的那麼重要。**

---

## 世代 1：Prompt Engineering（2022-2024）

2022 年 11 月 ChatGPT 上線時, 人和大型語言模型之間唯一的介面就是一個文字框。由此誕生的學科叫做 prompt engineering: 精心設計輸入文字以獲得更好輸出的藝術與科學。

核心技術快速演進:

**Few-shot prompting**（Brown 等, 2020）證明在 prompt 內放入幾個例子就能顯著提升任務表現, 而完全不需要 fine-tuning。要讓模型分類情感, 你不再訓練模型, 而是給它三個例子, 然後問它第四個該怎麼分。

**Chain-of-thought（CoT）prompting**（Wei 等, 2022）顯示, 加一句「Let's think step by step」或在例子裡加上推理過程, 能解鎖標準 prompting 看不到的多步推理能力。這可以說是首個跡象——**結構怎麼寫**和**問什麼內容**一樣重要。

**Prompt 範本** 成為標準抽象。LangChain、LlamaIndex 以及十幾個框架都提供了範本系統, 把變數注入精心設計的 prompt 結構。當時的心智模型很清楚: prompt 是程式, 模型是 runtime。

這個時代的其他技術包括:

- **ReAct**（Yao 等, 2022）: 在單一 prompt 結構內交錯推理與行動, 讓模型在一個 prompt 裡規劃並執行工具呼叫。
- **Tree of Thought**（Yao 等, 2023）: 探索多條推理路徑, 選擇最佳的一條。
- **Self-consistency**（Wang 等, 2022）: 採樣多條推理鏈, 取多數票決。

這個時代的侷限在於它的預設: LLM 互動的品質主要由 prompt 品質決定。當上下文視窗只有 4K-8K token、唯一輸入只有使用者文字時, 這是對的; 當模型可以吃下 100K+ token 並呼叫外部工具之後, 這就不再成立。

### 這個時代做對了什麼

Prompt engineering 確立了一件事: **結構很重要**。好 prompt 和爛 prompt 的差別不是 vibes, 而是資訊架構。這個洞察延續到了之後的一切。

### 這個時代漏掉了什麼

它把上下文視窗當成靜態產物。你寫好一個 prompt, 提交, 拿到回應。上下文視窗本身可以**在 runtime 由多個來源動態建構**——這是下一代的洞察。

---

## 世代 2：Context Engineering（2025）

2025 年中, Andrej Karpathy 發了一段後來被瘋狂轉傳的話:

> 「我一直在想這件事, 大多數人真正需要做好的不是『prompt engineering』, 而是『context engineering』——在上下文視窗裡塞入下一步所需正好資訊的藝術與科學。」

這次重構很重要, 因為它把焦點從**指令**（prompt）轉移到**整個資訊包**（上下文視窗）。一次現代 LLM 呼叫的上下文視窗遠不止使用者 prompt:

- 定義行為與限制的系統指令
- RAG 流程檢索到的文件
- 工具定義和 schema
- 對話歷史（選擇性壓縮過）
- 動態選擇的 few-shot 例子
- 關於當前任務的結構化 metadata

Prompt 只是其中一塊組件。Context engineering 是把這些全部協同安排。

### 六大技術

[Towards AI 的分析](https://towardsai.net/) 指出 context engineering 的六大核心技術:

1. **Retrieval-Augmented Generation（RAG）**: 在查詢時拉取相關文件
2. **工具與 API 整合**: 用結構化 schema 給模型外部能力
3. **記憶管理**: 在對話回合與 session 間維持相關資訊
4. **動態 prompt 建構**: 由範本、檢索內容和 runtime 狀態組裝 prompt
5. **上下文視窗最佳化**: 管理在有限 token 預算內放什麼、不放什麼
6. **指令層級**: 系統、開發者、使用者指令之間的優先序

### 來自 Manus 的教訓

[Manus](https://manus.im/) 是 2025 年話題度最高的 AI agent 平台之一, 分享了大規模 context engineering 的關鍵教訓:

**KV-cache 洞察**: Manus 把上下文視窗工程化, 維持高 KV-cache 命中率——確保之前 attention 計算出來的 key-value 對可以跨回合重用。這大幅降低 latency 和成本。原則是: 安排 context 讓**前綴穩定**, 僅**後綴**在呼叫之間變。

**100:1 比率**: Manus 報告每 1 個輸出 token 大約消耗 100 個 context token。這翻轉了輸出 token 主導成本的常見假設。真正的工程挑戰不是產生文字, 而是**選擇什麼 context 給模型**。

**Context 是產品**: Manus 把上下文視窗建構當作核心產品功能, 不是實作細節。他們 agent 的品質直接對應 context 組裝管線的品質。

### 分類的轉變

Context engineering 把 LLM 應用開發從「寫好 prompt」重構為「建構好的資訊管線」。模型變成對收到的任何 context 進行推理的引擎。工程挑戰往上游移動——到檢索、過濾、排序、壓縮與組裝。

但即使這個框架也有上限。它說明了**進入模型的是什麼**, 但沒說明**模型周圍的系統如何運作**。這需要再一次轉變。

---

## 世代 3：Harness Engineering（2026）

2025 年末到 2026 年初, 兩份有影響力的內容把下一次演進正式化:

**Birgitta Böckeler**（ThoughtWorks）於 2026 年 4 月在 Martin Fowler 的 *Exploring Generative AI* 備忘錄系列中發表分析, 主張 LLM 應用最有影響力的工程工作不是模型訓練或 prompt 設計, 而是**harness**——圍繞模型的工具、路由、記憶、規劃、錯誤恢復系統, 把模型呼叫編排成可靠的工作流程。

**OpenAI 的 Codex 團隊** 已經發表過關於 agentic coding 的 harness 設計案例資料（公開材料見 openai.com/index/introducing-codex）。在 2025-2026 年 OpenAI 的演講與文章中流傳的「三位工程師 / 約 100 萬行 / 約 1,500 個 PR」數字是社群廣為引用的, 但底層觀察是: Codex 的品質主要不是由模型決定, 而是 harness——決定**何時**呼叫模型、**提供什麼 context**、**讓哪些工具可用**、**如何**驗證與從錯誤恢復的系統。

### Phil Schmid 的類比

[Phil Schmid](https://www.philschmid.de/context-engineering) 提出了讓這個概念結晶化的類比:

- **模型是 CPU**——原始計算能力
- **上下文視窗是 RAM**——當前操作的工作記憶體
- **Harness 是作業系統**——排程、資源管理、I/O、錯誤處理、使用者介面

這個類比說明了為什麼 harness engineering 重要: 沒人會出貨一個沒有 OS 的 CPU。模型必要但不充分。Harness 決定模型實際能完成什麼。

### Meta-Harness 論文與 6 倍差距

2026 年初的研究論文量化了從業者已經懷疑的事: 一個裸模型與一個有良好 harness 的模型之間的差距, 在複雜任務上大約是**6 倍**。同樣權重、同樣訓練資料的同一個模型, 因為 harness 品質不同, 結果可以差到六倍。

這意味著對大多數實際應用來說, harness engineering 比模型改進有更大槓桿。一個好 harness 配上好模型, 跑贏一個一般 harness 配頂尖模型。

### IMPACT 框架

2020 年代中期的從業者討論中, **IMPACT 助記詞** 浮現為評估 harness 品質的清單:

- **I**nstructions——系統指令的清晰度與完整度
- **M**emory——跨 session 的持續與檢索
- **P**lanning——任務分解與排序
- **A**ctions——工具可用性與可靠性
- **C**ontext——相關資訊的動態組裝
- **T**esting——評估與品質保證迴路

IMPACT 把 context engineering 定位為更廣 harness engineering 學科裡的**一個組件**（「C」）。這種嵌套是關鍵的結構洞察: context engineering 在 harness engineering **之內**, 不是被它取代。

### Meta 收購 Manus（約 20 億美元）

2026 年初, Meta 以約 20 億美元收購 Manus。這場收購被廣泛解讀為 Meta **買的是 harness, 不是模型**。Meta 已經有 Llama, 它沒有的是**生產級、可在 context 組裝、工具編排、agent runtime 管理上驗證的系統**。

收購驗證了那個論點: LLM 生態系統裡最有價值的工程, 越來越多在編排層, 而非模型層。

---

## 關鍵洞察：共存而非取代

這三個世代不是清晰的歷史階段, 不是後一個取代前一個。它們是**嵌套層**, 在每個生產系統內共存:

```
+--------------------------------------------------+
|              HARNESS ENGINEERING                  |
|  +--------------------------------------------+  |
|  |          CONTEXT ENGINEERING                |  |
|  |  +--------------------------------------+  |  |
|  |  |       PROMPT ENGINEERING             |  |  |
|  |  |                                      |  |  |
|  |  |  系統 prompt、CoT、few-shot、         |  |  |
|  |  |  指令格式化                          |  |  |
|  |  +--------------------------------------+  |  |
|  |                                            |  |
|  |  RAG 管線、記憶、工具 schema、              |  |
|  |  上下文視窗最佳化                          |  |
|  +--------------------------------------------+  |
|                                                  |
|  技能路由、規劃迴路、錯誤恢復、                    |
|  漸進式揭露、多 agent 協調                        |
+--------------------------------------------------+
```

一個 harness 工程師仍然寫 prompt, 仍然做 context engineering。但他還要建構**系統**——決定何時用哪個 prompt、為每種情境組裝哪些 context、出錯時如何恢復。

演進不是拋棄早期技術, 而是認識到它們必要但不充分——並在它們之上建構那些把原始 LLM 能力轉化為可靠、生產級應用程式的層。

一篇來自上海交通大學等機構的 19 作者綜述 **「Externalization in LLM Agents: A Unified Review of Memory, Skills, Protocols and Harness Engineering」**（arXiv 2604.08224, 2026 年 4 月 9 日）獨立到達本章使用的相同三層組織: 在他們的框架中, 這個領域的演進從 *weights* 到 *context* 到 *harness*, 而他們把記憶、技能、協定、harness engineering 視為四個由 harness 作為整合層統合的外部化組件。這個收斂對從學術文獻來的讀者值得標註: 這不是只有從業者用的框架, 也不是這本指南獨有——它是 2026 年 4 月底學術綜述也獨立選擇的組織軸心。

---

## 來源

- Brown, T. 等（2020）. "Language Models are Few-Shot Learners." [arXiv:2005.14165](https://arxiv.org/abs/2005.14165)
- Wei, J. 等（2022）. "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models." [arXiv:2201.11903](https://arxiv.org/abs/2201.11903)
- Yao, S. 等（2022）. "ReAct: Synergizing Reasoning and Acting in Language Models." [arXiv:2210.03629](https://arxiv.org/abs/2210.03629)
- Yao, S. 等（2023）. "Tree of Thoughts: Deliberate Problem Solving with Large Language Models." [arXiv:2305.10601](https://arxiv.org/abs/2305.10601)
- Wang, X. 等（2022）. "Self-Consistency Improves Chain of Thought Reasoning in Language Models." [arXiv:2203.11171](https://arxiv.org/abs/2203.11171)
- Karpathy, A.（2025 年中）. 關於 context engineering 的公開發言; 在 X 與 AI engineering 社群廣為流傳, 奠定了這個領域採用的工作定義。
- Manus.（2025）. "Context Engineering Lessons from Building Manus." [manus.im/blog](https://manus.im/blog) ——KV-cache 命中率作為運營指標、append-only context、工具 logit-bias masking、滾動 todo-list 重寫。
- Böckeler, Birgitta.（2026 年 4 月 2 日）. "Harness engineering for coding agent users." martinfowler.com（*Exploring Generative AI* 系列）。[https://martinfowler.com/articles/harness-engineering.html](https://martinfowler.com/articles/harness-engineering.html) ——Guides vs. Sensors、Computational vs. Inferential 分類。
- OpenAI. Codex 公開材料: [https://openai.com/index/introducing-codex](https://openai.com/index/introducing-codex)。Codex 的 harness 設計框架錨點; 廣為引用的「三位工程師 / 約 100 萬行 / 約 1,500 個 PR」數字在 2025-2026 年 OpenAI 演講與文章中流傳, 在此引用為社群引用而非來自單一 canonical 帖。
- Schmid, Philipp. "The New Skill in AI is Not Prompting, It's Context Engineering" 與續篇。[https://www.philschmid.de/context-engineering](https://www.philschmid.de/context-engineering); [https://www.philschmid.de/context-engineering-part-2](https://www.philschmid.de/context-engineering-part-2) ——模型 = CPU、Context = RAM、Harness = OS 類比。
- IMPACT 助記詞。Intent / Memory / Planning / Authority / Control flow / Tools——一個六維 harness 設計清單, 在 2020 年代中期從業者討論中浮現。在本章作為教學框架使用; 不歸屬任何特定原始來源。
- Meta/Manus 收購報導.（2026）. 多個來源。
- Zhou, C. 等（2026 年 4 月）. "Externalization in LLM Agents: A Unified Review of Memory, Skills, Protocols and Harness Engineering." [arXiv:2604.08224](https://arxiv.org/abs/2604.08224) ——上海交通大學等機構 19 作者綜述, 獨立使用 Weights → Context → Harness 三層歷史框架。在本章「共存而非取代」一節作為從業者論點與學術文獻收斂的證據被引用。

---

*下一章: [第 2 章 —— RAG、長上下文與知識圖譜](../../../chapters/02-knowledge-layer.md)（英文）*
