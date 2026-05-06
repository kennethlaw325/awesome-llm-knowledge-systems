# 第 12 章：本地模型與知識工程

> **一句話總結：** 本地模型讓你在自己的硬體上跑整套知識 harness——私密、免費, 而且越來越能與雲端 API 競爭。
>
> **為什麼重要：** 如果你的知識庫含敏感資料, 或你想在自己的筆記上微調模型, 本地推論是唯一讓一切留在你掌握下的路徑。

前幾章描述的知識工程堆疊基本假設雲端 API 存取——把你的 context window 送給 Anthropic、OpenAI 或 Google, 拿回回應。這對大多數使用者運作良好。但有越來越多的從業者, 雲端推論對他們要麼不切實際, 要麼不可取: 處理敏感企業資料的、所在司法管轄區有嚴格資料駐地要求的、以及想透過在自己編纂知識上微調模型來完全閉環的。

本章涵蓋本地模型與知識工程的交集。它不涵蓋 GPU 採購指南、基準比較、或量化技術——那些主題有其他資源專門處理。相反, 它聚焦於把模型帶進你自己基礎設施時真正重要的架構決策。

---

## 為什麼本地對知識工程重要

三股力量推動本地模型在知識系統中的採用:

**隱私作為架構, 不只政策。** 當你對內部公司檔案跑 RAG, 每次查詢都送檔案 chunk 給雲端供應商。資料處理協議有幫助, 但不消除攻擊面。本地推論下, 資料從不離開機器。對法律事務所、醫療組織、政府機構, 這不是偏好——是要求。

**規模化成本。** 一個跑持續背景程式——vault 檢查、自動筆記編纂、定期重新索引——的知識系統每天產生數千次 API 呼叫。在雲端定價下, 這快速累積。一個跑在消費級硬體的本地模型, 在初始設定後, 每查詢零邊際成本。對永遠開著的知識維護（來自 Karpathy 架構的 Lint 操作）, 本地推論徹底改變經濟學。

**微調終局。** 這或許是最有說服力的理由。一旦你的知識庫達到足夠質量——透過數月 Ingest 操作累積數百份結構良好、互相連結的筆記——它變成原始合成資料集。你能在這個資料集上微調一個小本地模型, 產出一個內在「知道」你領域的模型, 不需在 runtime 檢索。知識在權重裡, 不在 context window。

---

## 架構：本地模型適合哪裡

不是知識 harness 的每個元件都同等受益於本地推論。這裡是本地模型提供最大價值的地方:

### Embedding 模型（高價值）

Embedding 是任何 RAG 管線的基礎。每次你加筆記到 vault, 它需要被轉成向量做相似度搜尋。這是高量、低複雜度的操作——本地推論的完美物件。

熱門選擇:
- **nomic-embed-text**（137M 引數）: 強健的通用 embedding, 在 CPU 上跑
- **mxbai-embed-large**（335M）: 更高質量, 在普通硬體上仍可管理
- **bge-m3**（568M）: 多語言, 對混合語言內容的 vault 極佳

這些模型夠小, 能在任何現代筆電跑而不需 GPU。本地與雲端 embedding（OpenAI 的 text-embedding-3、Cohere 的 embed）之間的質量差距已顯著縮窄——對大多數知識管理用例, 本地 embedding 夠用。

透過 Ollama 在本地跑:
```
ollama pull nomic-embed-text
```

### 查詢與推理（中等價值）

用本地模型回答關於你 vault 的問題——Query 操作——是取捨變得更微妙的地方。雲端模型（Claude Opus、GPT-4o）在複雜推理、多步綜合、微妙指令遵循上仍有意義地更好。但對直接的檢索式 Q&A（「我上個月寫過關於 X 的什麼？」）, 7-14B 引數範圍的本地模型表現良好。

實務選項:
- **Qwen3-14B**: 強健多語言效能, Apache 2.0 授權
- **Llama 3.3-8B**: 快速推論, 擅長遵循結構化指令
- **DeepSeek-R1-Distill-7B**: 從完整 R1 蒸餾的推理能力, MIT 授權
- **Gemma 3-12B**: Google 的高效架構, 擅長結構化輸出

最有效的 pattern 是 **分層做法**: 用本地模型處理日常查詢與 vault 維護, 升級到雲端 API 處理複雜綜合與創意任務。這呼應漸進式揭露的 harness engineering 原則如何應用到模型選擇——為每個任務用最低能幹模型。

### 知識編纂（高價值）

Ingest 操作——讀原始來源並把它們編纂成結構化 wiki 頁面——出乎意料地適合本地模型。這個任務定義良好: 讀文章、提取關鍵點、生成含 wikilink 的結構化筆記。一個 14B 模型配良好指令遵循能可靠處理這個, 特別在系統 prompt 精確指定輸出格式時。

這是經濟論點最強的地方。如果你的 Web Clipper 每天捕捉 5-10 篇文章, 每次編纂花 2-3 分鐘推論, 在本地跑這件事意味著你的知識庫以零邊際成本持續成長。

### Vault 維護（高價值）

Lint 操作——掃描矛盾、陳舊、孤立筆記——是個批次過程, 極受益於本地推論。你能每小時、每天、或在背景持續跑它而不用擔心 API 成本。一個本地模型掃描你的 vault, 標記問題, 產出健康報告——全部不需任何資料離開你的機器。

---

## 微調終局

Andrej Karpathy 概述了一個許多從業者現在在追求的願景: 一旦你的 LLM 維護 wiki 達到足夠質量, 用它微調一個個人小型語言模型（SLM）。

工作流程:

1. **編纂** 你的知識庫, 透過數月 Ingest 操作。Wiki 成長到數百份結構良好、互相連結的筆記。
2. **提取** wiki 的訓練對: 每份筆記變成一個（問題, 答覆）對, 或一個（context, 續寫）對。
3. **微調** 一個小模型（1-3B 引數）在這個資料集上, 用 LoRA 或 QLoRA。
4. **部署** 微調後的模型在本地。它現在從權重回答關於你領域的問題, 不需檢索。

這不會完全取代 RAG——微調後的模型對最近資訊與具體細節仍受益於檢索。但它戲劇性減少檢索負擔。模型「知道」你領域的基礎概念、關係、pattern。RAG 只需補充新或高度特定的資訊。

這個管線的工具已成熟:
- **Unsloth** 用於高效微調（快 2 倍, 記憶少 60%）
- **Axolotl** 用於託管訓練配置
- **MLX**（Apple Silicon）或 **llama.cpp** 用於微調後模型的本地推論

---

## 整合 Pattern

### Pattern 1: Ollama 作為通用後端

Ollama 提供一個用相容 OpenAI API 跑本地模型的統一介面。這意味著任何與 OpenAI API 一起運作的工具能透過改 base URL 指向本地模型:

```
base_url: http://localhost:11434/v1
model: qwen3:14b
```

這與 LangChain、LlamaIndex、Dify、大多數 RAG 框架一起運作。對 Obsidian 使用者, Smart Connections 等外掛能配置成用本地 Ollama 模型而非雲端 API。

### Pattern 2: 混合雲端-本地

對大多數使用者最實用的架構:
- **本地**: Embedding、vault 維護、日常查詢、知識編纂
- **雲端**: 複雜推理、創意綜合、多步 agent 工作流

這給你高量操作的隱私與成本優勢, 同時保留對真正需要的任務存取前沿模型能力。

### Pattern 3: MCP 配本地模型

Model Context Protocol 透過 Ollama 的相容 OpenAI 端點與本地模型一起運作。這意味著你能建 MCP 伺服器, 連到本地知識來源——你的 vault、你的資料庫、你的檔案系統——並把它們服務給本地跑的模型。整套知識 harness 跑在你的機器上。

---

## 本章不涵蓋什麼

本章刻意省略:
- **硬體建議**: GPU 選擇、VRAM 要求、雲端 GPU 租賃在 r/LocalLLaMA 的 wiki 與 Ollama 文件等資源中廣泛涵蓋。
- **模型基準**: 排名每月變。最新排名見 [Open LLM Leaderboard](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard)。
- **量化細節**: GGUF 格式、INT4 vs INT8、質量/速度取捨在 llama.cpp 與 Ollama 社群中有良好文件。
- **訓練基礎設施**: 多 GPU 設定、分散式訓練、雲端訓練平臺都在知識工程範圍之外。

這裡的焦點是架構問題: 本地模型在你的知識 harness 中適合哪裡, 它們如何改變什麼是可能的？

---

## 關鍵要點

1. **本地 embedding 是不用想的選擇。** 質量差距已關閉, 成本是零, 隱私好處是絕對的。如果你跑 RAG, 在本地跑 embedding。

2. **分層推論是務實選擇。** 本地處理日常操作, 雲端處理複雜推理。不要強迫 7B 模型做前沿模型做得更好的事。

3. **編纂用例被低估。** 在本地跑 Ingest 意味著你的知識庫能以零成本持續成長。這改變知識維護的經濟學。

4. **微調是終局, 不是起點。** 先建 wiki。編纂數百份質量筆記。然後微調。訓練資料的質量——你的 wiki——決定結果模型的質量。

5. **隱私是架構決策。** 如果你的知識含敏感資訊, 本地推論不是可選的。從一開始就為它設計。

---

## 來源

- Ollama: [https://ollama.ai](https://ollama.ai)
- llama.cpp: [https://github.com/ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)
- Unsloth: [https://github.com/unslothai/unsloth](https://github.com/unslothai/unsloth)
- Karpathy, Andrej. "LLM Wiki" pattern——本章引用的 raw → wiki → schema 分層架構與 Ingest / Compile / Lint / Query 操作所定義的 Gist。[https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
- Open LLM Leaderboard: [https://huggingface.co/spaces/open-llm-leaderboard](https://huggingface.co/spaces/open-llm-leaderboard)
- Nomic Embed: [https://huggingface.co/nomic-ai/nomic-embed-text-v1.5](https://huggingface.co/nomic-ai/nomic-embed-text-v1.5)
- r/LocalLLaMA: [https://reddit.com/r/LocalLLaMA](https://reddit.com/r/LocalLLaMA)

---

*上一章: [第 11 章 —— LLM 知識工程的關鍵時刻](11-timeline.md)*
