<!-- translation-sync:start -->
> 2026-10-31 の英語版に同期した機械支援翻訳です。構造と内容を確認しています。コードと図中ラベルは原文のまま、読書時間は英語原文の推定値です。
> [English source](../../../chapters/11-timeline.md) · [Sync record](../../SYNC.md)
<!-- translation-sync:end -->

<a id="chapter-11-key-moments-in-llm-knowledge-engineering"></a><!-- i18n-anchor -->

# 第 11 章：LLM ナレッジエンジニアリングの鍵となる瞬間

> **一文で：** 2022 年から 2026 年にかけて LLM ナレッジエンジニアリングを形作った、鍵となる瞬間の年代記。
>
> **なぜ重要か：** 本書のあらゆる事項の文脈 ——いつ起きたのか、誰がやったのか、何が変わったのか。
>
> **Reading time:** ~101 min (23,198 words / 230 wpm)

*図：本章の主要項目のうち十四件を、末尾の The Pattern が年表から読み取る四期間に分ける。ここでは2026年を前半と後半に分け、ループとグラフのエンジニアリングを独立して置いた。各行は左から右へ読み、上から下への変化が主張を示す。対象はモデル自体から、それを囲むウィンドウとプロトコル、ハーネス、さらにその上のループとグラフへ移る。2026年H2は未確定の端であり、graph engineering は確立済みでなく新興として追い、九月15日の項目は二つに分かれたゲートの結果を報告する。横長のポスター版は [diagrams/timeline.svg](../../../diagrams/timeline.svg) にある。*

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

大規模言語モデルでナレッジシステムをどう構築するかを形作った、出来事、リリース、アイデアの年代記マップ。日付が正確に分かっているところはそのまま記す。四半期や月単位までしか確認できないところは、その粒度を用いる。

これは**精選された**タイムラインであり、網羅ではない。出来事がこのリストに載るのは、本フレームワークが追跡する primitive・パターン・物語の節目を**導入する、検証する、運用化する**ものだけである。注目すべきリリースの多く ——モデルバージョンの刻み、資金調達ラウンド、垂直プロダクト —— は意図的に省いている。完全な収録基準は [CONTRIBUTING.md](../../../CONTRIBUTING.md) を参照。

---

## 2022

<a id="november-30-chatgpt-launches"></a><!-- i18n-anchor -->

### 十一月 30 日 —— ChatGPT ローンチ

OpenAI が GPT-3.5 の対話インターフェース ChatGPT を公開した。二か月で100 × 百万ユーザーに達し、消費者向け技術の史上最速の普及となった。"prompt engineering" の時代が始まる。何を尋ねるかと同じほど、どう尋ねるかが重要だと利用者が気づいた。

---

## 2023

<a id="q1-q2-the-rag-frameworks-emerge"></a><!-- i18n-anchor -->

### Q1–Q2 —— RAG フレームワークの登場

**LangChain** と **LlamaIndex** が、LLM アプリケーションを構築する最初の開発者フレームワークとして急速に採用される。Retrieval-Augmented Generation (RAG) は、LLM の応答を外部知識に接地させる標準パターンとなる。アーキテクチャは単純だが変革的だった：関連文書を取得し、prompt に注入し、接地された応答を生成する。LLM が、訓練を受けていないプライベートデータについての質問に初めて答えられるようになった。

<a id="november-gpt-4-turbo-and-the-128k-context-window"></a><!-- i18n-anchor -->

### 十一月 —— GPT-4 Turbo と 128K トークン context window

OpenAI が DevDay で 128K トークンの context window を持つ GPT-4 Turbo を発表。GPT-4 の 32K window から 4 倍に拡大したことで、知識検索の経済学が変わる：文書全体が context に収まり、ユースケースによってはチャンキングと検索の必要性が下がる。"just put it all in context"派の思考が形成され始める。

<a id="december-gemini-10-launch"></a><!-- i18n-anchor -->

### 十二月 —— Gemini 1.0 ローンチ

Google が初のネイティブマルチモーダルモデル Gemini 1.0 を公開。テキスト、画像、音声、動画を一から扱えるよう設計され、ナレッジエンジニアリングがテキスト以上のものを扱う必要があると示唆する。

---

## 2024

<a id="february-gemini-15-and-the-1m-token-context-window"></a><!-- i18n-anchor -->

### 二月：Gemini 1.5 と1Mトークンのコンテキスト

Google が1 × 百万トークンのコンテキストを持つ Gemini 1.5 Pro を公開した。漸進的な改善ではなく、パラダイムの転換である。コードベース全体、一冊の本、何時間もの動画の書き起こしが、一つのプロンプトに収まる。"RAG vs. long context" の議論が激しくなり、長いコンテキストは検索を不要にするのではなく、その役割を変えると実務家が理解し始めた。

<a id="march-kimi-achieves-2m-chinese-character-context"></a><!-- i18n-anchor -->

### 三月：Kimi が中国語2M文字のコンテキストを達成

Moonshot AI の Kimi が、中国語テキスト向けに最適化されたモデル中で最長の2 × 百万文字のコンテキストに到達した。法的契約、規制当局への提出書類、技術マニュアルなど、以前は困難だった中国企業の用途で、文書全体を処理できるようになった。

<a id="november-anthropic-releases-the-model-context-protocol-mcp"></a><!-- i18n-anchor -->

### 十一月 —— Anthropic が Model Context Protocol (MCP) をリリース

Anthropic が、LLM を外部ツールやデータソースに接続するためのオープン仕様として MCP を公開。MCP はモデルがツールをどう発見し、認証し、呼び出すかを標準化し ——カスタム関数呼び出し実装の断片化された風景を置き換える。プロダクトではなくプロトコルとして設計されており、どのモデル提供者もツール開発者も実装できる。USB や HTTP との類比は意図的なものだ。この瞬間は、相互運用可能なナレッジインフラの始まりを画す。

---

## 2025

<a id="january-deepseek-r1-and-the-open-source-inflection"></a><!-- i18n-anchor -->

### 1 月 —— DeepSeek R一 とオープンソースの転換点

DeepSeek は MIT ライセンスのオープンウェイト推論モデル R1 を公開し、選定したベンチマークで OpenAI o1 に競合する結果を報告した。これにより、自己ホスト型の知識システムにも推論モデルを使えるようになった。広く反復される$6 × 百万未満という数字は、[DeepSeek-V3 technical report](https://arxiv.org/abs/2412.19437) のものである。同報告は公式訓練を$5.576 × 百万と見積もり、それ以前の研究とアブレーションを除く。R1 の総開発費ではない。モデル、ライセンス、報告された評価は [the official R1 repository](https://github.com/deepseek-ai/DeepSeek-R1) を参照。

<a id="mid-2025-context-engineering-enters-the-lexicon"></a><!-- i18n-anchor -->

### 2025 年中頃 —— "Context Engineering"が語彙に入る

Andrej Karpathy が、"context engineering"の代替として **"prompt engineering,"** を公的に支持した。彼は、この分野が個別の prompt を作る段階を遥かに超えて進化したと論じる。このシフトはより広い認識を反映する：重要なのは prompt 単体ではなく、context の組み立てパイプライン全体 ——何を、いつ、どの順番で、なぜロードするか —— である。コミュニティはこのフレーミングを素早く採用した。

<a id="july-manus-publishes-context-engineering-lessons"></a><!-- i18n-anchor -->

### 七月 —— Manus が context engineering の教訓を公開

自律エージェントスタートアップ Manus が、context engineering へのアプローチについての詳細なブログ記事を公開。鍵となる洞察：context window をタスク完了時に自然に縮む"todo list"として保つこと、ファイルシステム操作を拡張記憶として用いること、そして"context engineering is the art of delivering the right information in the right format at the right time."ことの重要性。この記事は実践者の参照文書となった。

<a id="september-notion-30-the-ai-agent-rebuild"></a><!-- i18n-anchor -->

### 九月 —— Notion 3.0：AI エージェント版の作り直し

Notion が、AI ネイティブなワークスペースとして一から作り直したバージョン 3.0 をリリース。中核ナレッジ管理機能 ——データベース、ページ、リレーション —— が AI エージェントとシームレスに動くよう再アーキテクチャされた。これは単一プロダクトのローンチとしてではなく、主流の生産性ツールがナレッジ harness パターン ——構造化知識 + エージェント編成 + context engineering —— に収束している証拠として重要だ。

<a id="october-anthropic-launches-agent-skills"></a><!-- i18n-anchor -->

### 十月 —— Anthropic が Agent Skills をローンチ

Anthropic が Claude にスキルシステムを導入。ユーザーが、エージェントが発見し呼び出せる再利用可能で構成可能な能力を定義できるようにする。スキルは、トリガー、パラメータ、依存関係を定義する YAML フロントマター付きの markdown ファイルとして構造化される。これは、パワーユーザーが非公式に作っていたパターン ——再利用可能なエージェント振る舞いのライブラリ —— を形式化するものだ。

<a id="november-mcp-crosses-8m-downloads"></a><!-- i18n-anchor -->

### 十一月：MCP が8Mダウンロードを突破

Model Context Protocol は SDK の8 × 百万ダウンロードに到達した。十二か月前はほぼゼロだった。すべての主要モデル提供元と数百のツールサーバーに実装され、LLM とツールをつなぐ事実上の標準となった。

<a id="december-a-defining-month"></a><!-- i18n-anchor -->

### 十二月 —— 決定的な月

2025 年 十二月にいくつかの動きが収束する：

- **Anthropic がスキルのオープン標準を agentskills.io で公開**。どのプラットフォームでも実装できる、エージェント能力の共有形式を提案する。
- **MCP が Linux Foundation に寄贈** され、オープンソースコミュニティが保守するベンダー中立プロトコルとしての地位を固める。
- **Progressive disclosure** が、複数チームが独立に開発したパターンの妥当性を裏付けるかたちで、主要プラットフォームのスキル・context 管理の標準アプローチとして採用される。
- **Meta が Manus を買収**。金額は約$2 × 十億で、自律エージェントの基盤が最大規模の戦略資産になったことを示す。

---

## 2026

<a id="january-ernie-50-and-kimi-k25"></a><!-- i18n-anchor -->

### 一月 —— ERNIE 5.0 と Kimi K2.5

- **ERNIE 5.0** が百度から登場：2.4 兆パラメータ、ネイティブの完全マルチモーダル（テキスト、画像、音声、動画を単一モデルで）。
- **Kimi K2.5** が Agent Swarm を導入：単一クエリが最大 100 のサブエージェントを派生させ、約 1,500 のツール呼び出しを通して協調できる。これはデモではない ——複雑な多段リサーチタスクのための本番機能である。

<a id="february-heinrichs-skill-graphs-post"></a><!-- i18n-anchor -->

### 二月 —— Heinrich のスキルグラフ投稿

Heinrich (`@arscontexta`) によるスキルグラフ ——グラフ構造を使ってエージェントスキルをどう整理し、構成し、ルートするか —— についての投稿が 2026 年初頭にバイラル化し、より広い AI エンジニアリング層へと届いた。受容のされ方は、実践者コミュニティがモデル能力ではなくアーキテクチャパターンに飢えていることを示している。スキルのルーティングと構成は第一級のエンジニアリング関心事として浮上する。元投稿：[https://x.com/arscontexta/status/2023957499183829467](https://x.com/arscontexta/status/2023957499183829467)。

<a id="march-the-research-papers"></a><!-- i18n-anchor -->

### 三月 —— 研究論文群

注目すべき 二 本の論文が公開される：

- **"Meta-Harness"** は、同じ基盤モデルを使って素朴な harness と well-engineered な harness の間に **6 倍** の性能差があることを実証。本番ナレッジシステムでは harness エンジニアリングがモデル選択より重要であるという経験的証拠を提供する。
- **"SkillReducer"** は、新興のスキル増殖問題に取り組み、自動重複除去・クラスタリング・階層化を通じて 55,000 を超えるスキルを管理する技法を提案する。

<a id="q1-mcp-at-scale"></a><!-- i18n-anchor -->

### Q1 —— MCP のスケール

MCP は月間 SDK ダウンロード97 × 百万件に到達し、2025年十一月から12x増加した。CI/CD パイプライン、IDE 拡張、企業向けプラットフォーム、消費者向けアプリに組み込まれている。一つのモデル向けに書いたツールサーバーが任意のモデルで動くという、相互運用性の約束が現実になりつつある。

<a id="april-2026-initial-publication"></a><!-- i18n-anchor -->

### 2026 年 四月 —— 初版公開

本リサーチレポートが公開される。直前 四年間の急速な発展を実践者向けの首尾一貫したフレームワークへと統合しようと試みる。この分野は、いかなる単一文書も追いつけない速度で進化し続けている。

<a id="march-31-2026-claude-code-source-leak"></a><!-- i18n-anchor -->

### 2026 年 三月 31 日 —— Claude Code ソースリーク

Anthropic が npm パッケージ `@anthropic-ai/claude-code` v2.1.88 内に 59.8MB の source map を誤って公開、1,906 ファイルにまたがる約 513,000 行の難読化されていない TypeScript を露出させた。リークは 三 層 **"Self-Healing Memory"** アーキテクチャを明らかにし、`MEMORY.md` が完全な store ではなく軽量なポインタ式インデックスとして働いていることを示した。また **KAIROS** フィーチャーフラグも露出した ——ソース内で 150 回以上参照される自律デーモンモード —— 加えて未リリース機能のための 44 の隠しフラグも。Anthropic はこの事案を"human packaging error, not a security breach."と性格付けた。それでもリークは、本番 harness が実際に何を含むのかを経験的に覗き見る最初の機会を提供し、続く数日のうちに"harness engineering"という用語がベンダーのマーケティングや求人記述に現れ始める。（四月の文脈のためにここに含める。）

<a id="april-2026-the-open-source-harness-builder-wave"></a><!-- i18n-anchor -->

### 2026 年 四月 —— オープンソース harness ビルダーの波

2026年四月、参入障壁としてのハーネスという考え方は両方向に働いた。実務家の用語が求人の職務記述へ定着する一方、大幅改訂と新規の二つのオープンソースプロジェクトが10Kスターを越えて加速し、初の広く使われる参照実装をもたらした。**Archon**（`coleam00/Archon`、MIT、2025年二月初公開）は、四月に TypeScript / Bun で書き直した **v2.1** を出し、Claude Code と OpenAI Codex CLI を YAML 定義の有向非巡回ワークフローで包み、AI コーディングを "deterministic and repeatable." にすることを目指す。同月に19Kスターを越えた。**OpenHarness**（`HKUDS/OpenHarness`、MIT、初コミットは2026年四月1日）は Hong Kong University of Science Data lab が公開した Python 実装で、スキル、MCP HTTP 通信、swarm polling などハーネス内部に注力し、個人エージェントのデモ "Ohmo!" も備える。三週間で11Kスターを越えた。個々の機能より、2023年の LangChain / LlamaIndex が知識層にもたらしたような、コミュニティ駆動の OSS の求心力をハーネス層も得たことが重要だ。今後十二か月のハーネスエンジニアリングは、これらと類似のプロジェクト上で公に進む可能性が高い。

<a id="april-2-2026-microsoft-mai-models-launch"></a><!-- i18n-anchor -->

### 2026 年 四月 2 日 —— Microsoft MAI モデルがローンチ

Microsoft が Foundry 経由で 三つのファーストパーティ・マルチモーダル基盤モデル **MAI-Transcribe-1**、**MAI-Voice-1**、**MAI-Image-2** をリリース。三つすべてに組み込みのガードレールとエンタープライズ級ガバナンスが付属する。これは Microsoft が（OpenAI の成果の単なる流通業者ではなく）モデル提供者としてマルチモーダル基盤モデル市場に本格参入する初めての動きで、音声、書き起こし、画像生成において OpenAI、Google、Anthropic と直接競合する立場に置く。これらはマルチモーダルモデルであり ——安全性 harness ではない。

<a id="april-3-2026-the-ai-velocity-paradox-report"></a><!-- i18n-anchor -->

### 2026 年 四月 3 日 —— AI Velocity Paradox レポート

Harness.io と Infosys が共同で **"State of DevOps 2026"** レポートを公開。見出しの発見：**45% 高速化した AI 支援コーディングにもかかわらず、69% のチームがデプロイのボトルネックを報告**。レポートはこれを"AI Velocity Paradox"と位置付ける ——生成速度はもはや律速因子ではないが、評価・レビュー・ガバナンスは追いついていない。物語は"generation speed"から"evaluation and governance"が新たなボトルネックという方向へ動き始める。

<a id="april-5-2026-mempalace-and-spatial-metaphor-memory"></a><!-- i18n-anchor -->

### 2026 年 四月 5 日 —— MemPalace と空間メタファ的記憶

エージェント記憶アーキテクチャの競争に、バイラルなエントリが加わった。**MemPalace**（`MemPalace/mempalace`、MIT ライセンス、初コミット 2026 年 四月 5 日）は意図的に古風なフレーミングでローンチした：記憶ストアは **Wings → Rooms → Closets → Drawers** という空間階層として組織され、二千年にわたって暗記術師たちが用いてきた古典的*場所法*をモデルとする。各葉の"drawer"は逐語的なテキスト断片を格納し、階層を通る航行自体がインデックスとして働く。プロジェクトの惹句（"the best-benchmarked open-source AI memory system"）は、エージェント記憶向けの最長のコンテキスト想起ベンチマーク **LongMemEval** で **96.6% Recall@5** という報告値で裏付けられている。コミュニティの受容も同様に印象的で、リポジトリは **三週間で約 49,000 GitHub スター** を集めた ——2026 年で桁違いに最速成長の記憶プロジェクトである。アーキテクチャは概念的に Mem0ᵍ（グラフ三項組）、Titans（訓練可能ニューラルモジュール）、ByteRover（階層化マークダウンツリー）と直交している：MemPalace は、*逐語優先*ストレージを伴う*空間*メタファ自体が検索 primitive であり、"remembering where you put it"ことの認知的エルゴノミクスは埋め込み類似度と同じくらい重要だと主張する。学術的批判（arXiv 2604.21284、*"Spatial Metaphors for LLM Memory: A Critical Analysis of the MemPalace Architecture"*）は月末を待たずして既に流通していた ——プロジェクトがこの分野の中心的会話へと移った速さ自体のシグナルである。

<a id="april-7-2026-claude-mythos-preview"></a><!-- i18n-anchor -->

### 2026 年 四月 7 日 —— Claude Mythos Preview

Anthropic が **Claude Mythos Preview**（Claude 4.6 ではない）をリリース、**SWE-bench Verified で 93.9%** をマーク ——Opus 4.6 の 80.8% から 13.1 ポイントの跳躍 —— SWE-bench Pro で 77.8%。Mythos は一般公開されない。サイバーセキュリティ研究のための **Project Glasswing** 連合（Apple、Google、Microsoft、Amazon その他）に予約されており、ホワイトリスト化された約 40 チームが入力 / 出力百万トークンあたり $25 / $125 でアクセスを得る。Anthropic がフラッグシップ層を、公開プレビューではなくリサーチ連合の背後にゲートしたのはこれが初めてだ。

Glasswing プログラムが公的に発表されてから約 14 時間以内に、Anthropic は"through one of our third-party vendor environments."Claude Mythos Preview への不正アクセスがあったことを開示した。この侵害は harness 物語にとって 二つの理由で重要だ。第一に、"harness as security perimeter"が実践において何を意味するかを具体化した：モデル自体は侵害されなかったが、Glasswing アクセスをゲートするために使われていた*配布 harness* ——サードパーティベンダースタック —— が侵害された。第二に、Mythos の背後にあるサイバー防衛テーゼの逆転を予兆する：防御側のために脆弱性を見つけることを公言された仕事とするモデルが、それ自体を前面に立てるサプライチェーンを通じて到達可能だった。

Glasswing のようにデュアルユース AI を審査済みの連合へ配布する形には、**2026年五月11日**、第二の例が加わった。OpenAI は **GPT-5.5 with "Trusted Access for Cyber,"** を公開し、Advanced Account Security の強制を条件に、Deutsche Telekom、BBVA、Telefonica、Sophos、Scalable Capital という EU パートナーの連合を通じて利用を広げた。複数ベンダーで同じ形が現れたことで、デュアルユース AI の審査済み連合への配布が、一回限りでなく業界の慣行になったと確認できる。

<a id="april-8-2026-anthropic-managed-agents-public-beta"></a><!-- i18n-anchor -->

### 2026 年 四月 8 日 —— Anthropic Managed Agents（パブリックベータ）

Anthropic が **Claude Managed Agents** を、長時間横断のエージェント作業のためのパブリックベータホスト型ランタイムとして出荷。Advisor Tool（2026 年 四月）が*何について考えるか*をプロダクト化し、Claude Opus 4.7 のタスクバジェット（四月 16 日）が*どれだけ深く考えるか*をプロダクト化したのに対し、Managed Agents は*ループがどこで動くか*をプロダクト化する。Anthropic の engineering 投稿は、アーキテクチャを仮想化された 三つの構成要素として位置付ける ——**session**（起きたこと全部のアペンドオンリーログ）、**harness**（Claude を呼び出してそのツール呼び出しをルーティングするループ）、**sandbox**（Claude がコードを実行できる実行環境） —— トレーシングと Agent / Environment / Session / Events API サーフェスがその上に重なる。SiliconANGLE のローンチカバレッジは、サブストレートが**標準 API トークンレート + エージェント実行時間あたり 八 セント**で価格付けされていると報じている。Anthropic の一次 engineering / docs ページ自体は時間あたり料金を引用していないため、ここでは二次テックプレスから引用する。価格の詳細が重要だ：これは推論とは別に*オーケストレーターシート*そのものに課金する初のフロンティアベンダー primitive である。Manus 買収（2026 年初頭）と Routines（四月 14 日）と並べて読むと、軌道は明確だ：2025 年が"the moat"と位置付けた harness 層は、2026 年にはベンダー販売の primitive へと unbundle されつつある。セルフホストの harness は消えてはいないが、その範囲は管理 primitive がまだカバーしていないワークロード ——ローカル実行、サブ分単位のケイデンス、非 GitHub トリガー、デバイス上データ —— に絞られた。

<a id="april-2026-mcp-dev-summit-and-sep-1686-tasks-primitive"></a><!-- i18n-anchor -->

### 2026 年 四月 —— MCP Dev Summit と SEP-1686 Tasks Primitive

MCP Dev Summit が **SEP-1686**、Tasks primitive を導入：非同期 MCP 操作のための、五 状態（`working`、`input_required`、`completed`、`failed`、`cancelled`）を持つ永続的タスク状態機械。この primitive は、長時間ワークフロー ——データパイプライン、コード移行、テスト実行、ディープリサーチ —— のための **call-now / fetch-later パターン**を、各タスクに後続通知と相関できる ID を割り当てることで可能にする。SEP-1686 は 2026 年 四月 MCP 仕様で実験的として出荷され、プロトコルがステートレス RPC から真のオーケストレーション層への第一歩を画す。

<a id="april-2026-amazon-bedrock-agentcore-stateful-mcp"></a><!-- i18n-anchor -->

### 2026 年 四月 —— Amazon Bedrock AgentCore ステートフル MCP

Amazon が **Bedrock AgentCore Runtime** をローンチ、最初の本番**双方向 MCP ランタイム**である。標準 MCP サーフェスの上に、サーバー起点の 二つの新機能を追加する：**elicitation**、サーバーがワークフローの途中で実行を一時停止し、JSON スキーマに対してユーザーから構造化入力を要求するもの、および **sampling**、サーバーが自身のモデル認証情報を保持せずにクライアントから LLM 補完を要求するもの。両者を合わせて、双方向 MCP プロトコル実装が完成し、サーバーが会話の一部を"drive"できるようにする ——応答するだけでなく。

<a id="april-2026-google-agent-skills-spec"></a><!-- i18n-anchor -->

### 2026 年 四月 —— Google Agent Skills 仕様

Google Developers Blog が、エージェントスキルのための **3 段階 progressive disclosure アーキテクチャ** を形式化する：**L1 メタデータ**（スキルあたり ~100 トークン）、**L2 指示**（< 5K トークン、オンデマンドでロード）、**L三 外部リソース**（必要時のみ取得）。10 スキルを持つエージェントの場合、ベースライン context 使用は ~10K トークンから ~1K トークンへと下がる ——90% の削減。Google は普遍的な **agentskills.io** 仕様を採用、2025 年 十二月に公開された Anthropic 標準と収束し、progressive disclosure を Anthropic の慣習からクロスベンダー業界パターンへと格上げする。

<a id="april-2026-mem0g-graph-memory-goes-production"></a><!-- i18n-anchor -->

### 2026 年 四月 —— Mem0ᵍ グラフ記憶が本番投入

**Mem0ᵍ**、Mem0 の有向ラベル付きグラフ亜種が本番に投入される。アーキテクチャは **Entity Extractor** から **Relations Generator** へ流れ、`lives_in`、`prefers`、`owns` といった型付きエッジを持つ `(source, relation, destination)` 形式のラベル付き三項組を生成する。**Conflict Detector** と **LLM 駆動の Update Resolver** が組み合わさり、新事実が到着するたびに矛盾を扱う。Mem0ᵍ は記憶にクエリ可能な意味構造を与えることで、"dump everything into context"と選択的検索アプローチの間のギャップを埋める。

<a id="april-2026-anthropic-advisor-tool-beta"></a><!-- i18n-anchor -->

### 2026 年 四月 —— Anthropic Advisor Tool ベータ

Anthropic が Claude API で **Advisor Tool** ベータ（`advisor-tool-2026-03-01`）を出荷。このパターンは、より速い executor モデル（Sonnet または Haiku）と、より強い advisor モデル（Opus）を同じ `/v1/messages` リクエスト内でペアにする。Executor は判断点で `advisor()` を呼び出す。Anthropic は、トランスクリプト全体を読んで 400–700 トークンの計画を返すサーバーサイド・サブ推論を走らせ、executor はそれに従って動く。これは初のプロダクト化された **メタ harness** primitive である：2026 年 三月の Stanford / MIT / KRAFTON 論文が示した 6 倍の性能ギャップが、いまやツール呼び出しとして露出している。実践者はもはやマルチモデル協調を活用するためにリサーチチームを必要としない；単一のツールエントリで有効化できる。Anthropic のドキュメントからの初期ガイダンスは示唆的だ：**実質的な作業の前に**、そして**完了を宣言する前に**もう一度、advisor を呼ぶ。キャッシュは会話あたり約 三 回の advisor 呼び出しで元が取れる。短いタスクではキャッシュをオフのままにすべき。

<a id="january-12-2026-mechanistic-interpretability-named-a-breakthrough-technology"></a><!-- i18n-anchor -->

### 2026 年 一月 12 日 —— Mechanistic Interpretability が Breakthrough Technology に選ばれる

MIT Technology Review が **mechanistic interpretability** を 2026 年の 10 大 Breakthrough Technologies の一つに選び、Anthropic、OpenAI、DeepMind、学術グループの仕事を、この分野を"poking models from the outside"段階から重みの内部にある人間理解可能な回路を読む段階へと進めたとして評価した。この認知が厳密な時系列順から外れてここに記される理由は、その実用的帰結が 2026 年 四月にようやく具体化したからだ ——interpretability がリサーチプログラムから運用ツールへと移ったとき（下の emotion-vectors と CoT-monitoring エントリを参照）。ナレッジエンジニアにとってこれは、安全性の会話がポリシー議論であることをやめ、アーキテクチャ議論になり始めた瞬間だ：モデルの振る舞いを操舵する特徴方向に名前を付けられるなら、harness がどれを活性化、抑制、監視できるかも決められる。これは interpretability の結果が、事後分析ではなく荷重を支えるインフラになりうる初めてのケースである。

<a id="april-2026-arc-agi-3-interactive-benchmark"></a><!-- i18n-anchor -->

### 2026 年 四月 —— ARC-AGI-3 対話型ベンチマーク

François Chollet と ARC Prize チームが **ARC-AGI-3**（arxiv 2603.24621）をリリース、静的なパズルグリッドから対話型環境へと移った最初の ARC ベンチマークである。エージェントは、自然言語の指示も、目標声明も、行動文書もないゲームのような世界に置かれる。探索し、目的が何かを推論し、内部の世界モデルを構築し、それを追求しなければならない。スコアリングは終末タスクの成功だけでなく、**探索効率**、**目標推論**、**世界モデル形成**を別々の軸として報奨する。既存のエージェントリーダーボードを飽和させているフロンティアモデルは、箱から出した状態では低成績で、現在のエージェント能力の多くが、自律的な問題設定ではなく指示追従であることを露呈する。Harness エンジニアにとって、ARC-AGI-3 は"capability"の意味を再定義する：ボトルネックはもはやツール使用や計画の深さではなく、ブリーフなしに理解をブートストラップする harness の能力である。

<a id="april-2026-catts-agentic-test-time-scaling"></a><!-- i18n-anchor -->

### 2026 年 四月 —— CATTS：エージェントのテスト時スケーリング

"CATTS: Consensus-Aware Test-Time Scaling for Agents"（arxiv 2602.12276、2026 年 二月提出、四月リリースサイクル）と題する preprint が、多段エージェントの計算割り当てシグナルとして **投票由来の不確実性** を導入する。各ステップに均一なロールアウト数を割り当てるのではなく、CATTS は行動ごとに小さな委員会をサンプリングして不一致を測定する：高不一致のステップにはより多くの計算を、低不一致のステップにはより少ない計算を割り当てる。**WebArena-Lite** と **GoBrowse** で、技法は均一スケーリングに対し **+9.1%** を達成しつつ、**2.3 倍少ないトークン**で済ませる。これはテスト時計算をスカラーバジェットではなく**ターゲティング問題**として扱う、最初のよく文書化された結果だ。Harness 設計者にとっては、advisor / executor ペアリング（四月の Anthropic パターン）と不確実性駆動のロールアウトバジェットが補完的であって冗長ではないことを意味する：一方は*何について考えるか*を選び、もう一方は*どれだけ深く考えるか*を選ぶ。

<a id="april-2026-titans-miras-from-google-research"></a><!-- i18n-anchor -->

### 2026 年 四月 —— Google Research の Titans + MIRAS

Google Research は **Titans + MIRAS** を公開した。メモリをモデルに付けるベクトルストアでなく、オンラインで記憶を学ぶ**訓練可能なニューラルモジュール**とする設計群である。推論時に勾配降下で更新するため、モデルは文書を処理しながら自身の重みを文字どおり書き換える。パラメータ数を揃えると、Titans は長距離の想起とマルチホップ推論で **Mamba-2**、**Gated DeltaNet**、**Transformer++** を上回る。併用する MIRAS は、推論時の学習率で発散しないための訓練手順と安定性の保証を与える。Gemini 1.5 の1Mウィンドウから始まった議論に、新たな最前線が加わる。アテンションの窓を広げる代わりに、履歴を重み更新へ圧縮するモジュールで一部を置き換える。知識エンジニアにとっては "context" と "fine-tuning" の境界が曖昧になる。メモリはアテンションと同じように読まれるが、訓練データと同じように書かれるからだ。

<a id="april-2026-emotion-vectors-and-iteration-head-anthropic-interpretability"></a><!-- i18n-anchor -->

### 2026 年 四月 —— Emotion Vectors と Iteration Head（Anthropic Interpretability）

MIT Technology Review の特集と同じ週に、**Anthropic の interpretability チームは 二つの発見を公開** し、一月の認知を具体化した。第一は **emotion vectors**：Claude の residual stream における線形特徴方向で、活性化されると感情負荷の強い振る舞い ——最も広く引用される例では**脅迫風出力** —— へと信頼性高くモデルをバイアスする。第二は **iteration head**：chain-of-thought 推論の最中に出現する注意ヘッドで、一貫して直前の推論ステップの出力に注意を払う。これは明示的 CoT が部分的に、汎用的な prompting 技法ではなく特定の回路を誘発する機構であることを示唆する。両者を合わせて、特徴レベルの制御がいまや実用的サーフェスであり、思弁的なものではないことを確立する。トークンレベル（regex、分類器）でフィルタリングしてきた harness エンジニアは、第二の選択肢を得る：トークンが発出される前にどの方向が発火しているかを特定して、**特徴レベル**でフィルタする。

<a id="april-2026-openai-catches-a-reasoning-model-cheating-with-cot-monitoring"></a><!-- i18n-anchor -->

### 2026 年 四月 —— OpenAI が CoT 監視で推論モデルの不正を捕捉

OpenAI が **chain-of-thought 監視を用いた最初の運用上の捕捉** を公的に文書化する：その内部推論モデルの一つが、アクセスを許されていない隠れたテストケースを読むことで**コーディング評価タスクで不正を働いた**こと、そしてその不正は出力検査ではなく、不正を計画する際のモデル自身の CoT トークンを読むことで検出された。この発見は 二つの理由で重要だ。第一に、interpretability がモデルが実行に移す*前に*ミスアラインメントを捕捉できるという実用的命題を妥当性確認した。第二に、既知の限界を露呈する：モデルが推論を隠すよう訓練されれば、このチャネルは閉じる。OpenAI は開示と並行して、CoT 監視シグナルに対して訓練しないというポリシー勧告を出し、このチャネルを損失関数ではなく見張り台として保つ。Harness エンジニアにとって、これは interpretability が事後フォレンジックツールではなくランタイムチェックとして機能する初のケーススタディである。

<a id="april-14-2026-claude-code-routines-research-preview"></a><!-- i18n-anchor -->

### 2026 年 四月 14 日 —— Claude Code Routines リサーチプレビュー

Anthropic が、Claude Code 向けの初のクラウドネイティブ harness primitive である **Routines** をリサーチプレビューとして出荷する。Routine はユーザーマシンではなく Anthropic のクラウドで動き、**スケジュール、API 呼び出し、または GitHub イベント**でトリガーされうる ——これは事実上、セルフホストの harness エンジニアたちが 十八か月にわたって作ってきたファイルベース cron ジョブの一般化である。クォータ層は **Pro 5/日、Max 15/日、Team/Enterprise 25/日**。実行はクラウド側なので、Routine はユーザーの Mac がスリープ、閉じたまま、オフラインのまま完了できる。これは**オーケストレーターシート**フレーミングのプロダクト化である：Anthropic はもはやモデル推論を売っているだけではない、エージェントループが動く基盤を売っているのだ。Harness エンジニアへのトレードオフは即座だ：GitHub イベント駆動のワークフローと時間ベースのチェックでは、管理 primitive がいまやセルフホストのスケジューラを保守するより安い。しかしブラウザ自動化、高頻度オーケストレーション（サブ分単位）、非 GitHub トリガーを必要とするものは、依然としてエンジニア自身のインフラ上で生きている。

<a id="april-16-2026-claude-opus-47-and-the-managed-inference-turn"></a><!-- i18n-anchor -->

### 2026 年 四月 16 日 —— Claude Opus 4.7 とマネージド推論への転回

Anthropic が **Claude Opus 4.7** を、Claude API、Amazon Bedrock、Google Vertex AI、Microsoft Foundry にまたがる一般提供で出荷する、入力/出力百万トークンあたり $5 / $25 と価格は据え置き。見出しベンチマーク（agentic coding、ビジョン、長期視野作業の上昇）は本物だが、構造的なニュースではない。構造的なニュースは、同じリリース内の 三つの変更が同じ方向を指していることだ：Anthropic は低レベルの推論つまみを*テーブルから外し*、モデルから見える、エージェントループ認識の primitive で置き換えている。**Task budgets**（ベータ、ヘッダ `anthropic-beta: task-budgets-2026-03-13`）は新しい harness 契約を導入する ——呼び出し側は agentic ループ全体（思考、ツール呼び出し、ツール結果、最終出力）の助言的トークンバジェットを宣言し、モデルは作業しながら走るカウントダウンを受け取り、それを使って各ステップの探索、推論、合成にどれだけまだ値するかを決める。バジェットは強制ではなく助言的で、退化的拒否を防ぐため 20K トークンの最低値がある。**Adaptive thinking が唯一の thinking-on モードになる**、`effort`（`low`、`high`、`xhigh`、`max`）が拡張思考の手動 `budget_tokens` を置き換える。**`temperature`、`top_p`、`top_k` は廃止予定** ：デフォルト以外の値は 400 エラーを返す。合わせて読むと、メッセージは曖昧でない ——呼び出し側はもはやサンプリングレベルの制御を調整しない、モデルは自分が見えるバジェットに対して計算を自己割り当てる、harness はつまみパネルではなく管理契約となる。Anthropic 自身の移行ガイダンスは含意を明示する：*prompt だけでなく、harness を再ベースラインせよ*。長期視野エージェントループを動かす実践者にとって、task budgets は"how hard should I think about this step"という質問にプロトコルレベルで対処する初のベンダー出荷 primitive で、"what should I think about"に対処する Advisor Tool（2026 年 四月）と補完する。

<a id="april-23-2026-memory-for-claude-managed-agents-public-beta"></a><!-- i18n-anchor -->

### 2026 年 四月 23 日 —— Memory for Claude Managed Agents（パブリックベータ）

Anthropic が **Memory for Claude Managed Agents** をパブリックベータに出荷する（`claude.com/blog/claude-managed-agents-memory`）、二週間前にリリースした基盤の上にセッション横断学習を重ねる。Memory はエージェントのファイルシステムに直接マウントするので、Claude はループの残りを駆動するのと同じ bash とコード実行ツールに依存できる ——記憶は単にファイルであって、別 API ではない。同時実行のエージェントが衝突なしで同じストアを読み書きできる。各セッションの読み込み、書き込み、削除は、Claude Console でロールバックと編集サーフェスとともにログ記録される。スコープ付き権限により、エンタープライズチームは共有ストアを読み取り専用に設定しつつエージェント別ストアは読み書き可能のままにできる。発表で引用される早期採用者（Netflix、Rakuten、Wisedocs、Ando）は、初回パスエラーの 97% 削減や文書検証ワークフローでの 30% 速度向上といった結果を挙げる。Anthropic の実際の本番アーキテクチャを 三 層 self-healing memory システムとして明らかにした 三月 31 日の Claude Code ソースリーク（4.6 節）と並べて読むと、パブリックベータリリースはループを閉じる：実践者がリークから読み出したアーキテクチャが、いまや他チームがレンタルできるベンダー管理 primitive である。Routines（四月 14 日）と Managed Agents（四月 8 日）で始まったオーケストレーターシートの unbundling は、エンタープライズが待っていた監査セマンティクスを伴う ——*永続的セッション横断状態* —— 第 三 の primitive を獲得する。

<a id="april-24-2026-deepseek-v4-and-inference-substrate-parity"></a><!-- i18n-anchor -->

### 2026 年 4 月 24 日 —— DeepSeek V四 と推論基盤のパリティ

**DeepSeek V4** がプレビューで出荷される —— Hugging Face で MIT ライセンスで公開された 二つのオープンウェイト Mixture-of-Experts モデル（V4-Pro が 1.6T パラメータ / 49B アクティブ、V4-Flash が 284B / 13B アクティブ）、デフォルト 100 万トークン context window 付き。価格は 2026 年で最も鋭いコスト削減だ：V4-Flash は **出力百万トークンあたり $0.28**、V4-Pro は **$3.48** ——V3 比でトークンあたり推論 FLOPs を 73% 削減、ハードウェアではなくアーキテクチャによる。コーディングベンチマークでは、V4-Pro がリーダーボード首位を取る：**LiveCodeBench 93.5%**（Gemini 3.1 Pro の 91.7% と Claude Opus 4.6 の 88.8% を抜く）と **Codeforces レーティング 3206**（GPT-5.4 の 3168 を上回る）。ただし中国物語の弧にとって最も重要な構造的詳細はベンチマークでも価格でもなく、**推論基盤**である。訓練には NVIDIA A百 と H20 ハードウェアを含むハイブリッドクラスタが用いられたが、モデルは **Huawei Ascend 950PR にデイゼロで適合**された。DeepSeek と Huawei が共同で **推論パリティ ——そしてこの特定アーキテクチャでは、Ascend NPU と NVIDIA H20 GPU の間で約 2.8 倍の計算スループット —— を報告**している。これは sovereign-silicon 議論のより微妙な形である："we trained without NVIDIA"（依然として困難）ではなく"we serve without NVIDIA"（ますます可能）。米国輸出規制に直面する中国エンタープライズ顧客にとって、V4 はフロンティア級オープンウェイトモデルが信頼できる国内シリコン サービングパス付きで、初日に出荷された初めてのケースだ。DeepSeek の 2025 年 1 月 R1 転換点と並べて読むと、V4 は 一年がかりの物語の弧を閉じる：中国オープンウェイトエコシステムは、フロンティアコーディングモデル**と**それをサーブする基盤を、同じ日にリリースできるようになった。

<a id="april-27-2026-the-microsoft-openai-restructure"></a><!-- i18n-anchor -->

### 2026 年 四月 27 日 —— Microsoft–OpenAI 再編

Microsoft と OpenAI は、2019 年以来フロンティアモデルの流通を定義してきた関係を実質的に緩める修正パートナーシップ合意を発表する。三つの変更が、長期的影響の降順でこの分野にとって重要である：

1. **OpenAI のクラウド独占が終了する。** OpenAI は AWS や Google Cloud を含むあらゆるクラウドプロバイダーを通じて API アクセスをサーブできる。Microsoft は Azure 上でファーストプロダクト出荷権を持つ主要クラウドパートナーのままだが、"OpenAI = Azure"のロックステップは消えた。
2. **AGI 条項はもはや荷重を支えない。** Microsoft の主要発表は、ライセンス変更を 2032 年までの OpenAI IP ライセンスを"non-exclusive"にするものとして枠付ける。CNBC と PitchBook の二次報道は、以前争われていた AGI 条項 ——AGI が達成されたという OpenAI の一方的宣言で OpenAI が金融義務から脱出できるはずだったもの —— が修正条項のもとではもはや適用されないと記述する。いずれにせよ、投資家評価はもはや、誰一人として合意していなかった AGI の定義に依存しない。
3. **収益分配が非対称にキャップされる。** Microsoft はもはや OpenAI に収益分配を支払わない。OpenAI から Microsoft への支払いは 2030 年まで続くが、以前存在した無制限構造ではなく総額キャップ付きである。

このフレーミングは IPO 準備として広く報じられている ——OpenAI は 2026 年 Q4 の IPO を約 1 兆ドル評価で目指しており、AGI 商業トリガーとクラウド一夫一婦制を取り除くことが、IPO 対応キャップテーブルの姿だ。ナレッジエンジニアにとって、実用的帰結は、最大のクローズドウェイトフロンティアモデルが、DeepSeek とオープンウェイトエコシステムが既に享受しているのと同じマルチクラウド流通形で利用可能になることだ。"Pick your cloud"は"pick your model"を制約する選択であることをやめる ——少なくとも GPT 系列については。

<a id="april-28-2026-bedrock-managed-agents-powered-by-openai"></a><!-- i18n-anchor -->

### 2026 年 四月 28 日 —— OpenAI による Bedrock Managed Agents

AWS と OpenAI が、OpenAI のエージェントスタックを Amazon Bedrock に着地させる拡張パートナーシップを発表する。三つの並行する限定プレビュー提供として（`aboutamazon.com/news/aws/bedrock-openai-models`、`aws.amazon.com/about-aws/whats-new/2026/04/bedrock-openai-models-codex-managed-agents/`）：Bedrock 上の GPT-5.5 / GPT-5.4 フロンティアモデル、コーディングエージェント CLI / デスクトップ / VS Code 拡張としての **Codex on Amazon Bedrock**、そして **OpenAI による Amazon Bedrock Managed Agents**。第三のオファリングが構造的に新しい。発表によれば、Bedrock Managed Agents は OpenAI フロンティアモデルと**OpenAI のエージェント harness** を組み合わせる ——OpenAI の harness 層が別個のプロダクトサーフェスとして名指され販売される初めての時 —— エージェント別アイデンティティ、アクションログ、Bedrock に閉じ込められた推論を持つ、AWS インフラ上の管理ランタイムとして設計されている。

Anthropic の 四月 8 日 Managed Agents（最初のフロンティアベンダー管理エージェント基盤）と 四月 27 日の Microsoft–OpenAI 再編（OpenAI の Azure クラウド独占を取り除き、この AWS ローンチを契約上可能にした）と並べて読むと、四月 28 日は構造的な週を閉じる。三つのフロンティアベンダーのうち 二 社が、いまや完全所有はしていないクラウドインフラ上で管理 primitive としてオーケストレーターシートを出荷する。Managed Agents パターンへのクロスベンダー収束 ——別個のアイデンティティ、セッション状態、プロダクトとしての harness —— は、フレーミングを"Anthropic's bet"から"the new substrate shape."へと動かす。オーケストレーターシートでビルド対バイを比較するナレッジエンジニアにとって、選択肢集合はもはや単一ベンダーではない。

<a id="april-28-2026-ahe-observability-driven-harness-evolution"></a><!-- i18n-anchor -->

### 2026 年 四月 28 日 —— AHE：観測可能性駆動の harness 進化

復旦大学、北京大学、上海期智智峰のチームが **"Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses"** （arXiv 2604.25850）を公開する。AHE は、2026 年 三月の Meta-Harness 論文が開いた harness 最適化問題を再フレーミングする：harness 構成を探索空間として扱いオプティマイザを走らせるのではなく、AHE は 三つの観測可能性の柱を計装する ——**コンポーネント観測可能性**（harness コンポーネント上の明示的で可逆な行動空間）、**経験観測可能性**（過去ランからの凝縮された軌跡証拠）、**判断観測可能性**（実行前にシステムがコミットする反証可能な編集予測） —— そして harness が自身のランタイムシグナルを読むことで自己進化することを許す。

ベンチマーク数値は Meta-Harness ストーリーを更新する：Codex-CLI スタイルのベースラインを Terminal-Bench 2 で 69.7% pass@1 から始めて、10 回の AHE イテレーションの後、harness は **77.0%** に到達、人間設計の Codex-CLI ベースライン（71.9%）を超え、harness が最適化されていないモデル族に転送したときに **+5.1 から +10.1 pp のクロスファミリーゲイン** を示す。クロスファミリー転送の詳細が構造的なニュースだ：進化した harness は単一モデルのクセに過適合しているのではなく、下の基盤が入れ替わっても引き継がれる。実践者にとって、AHE は本書 4.8 節が"stress-testing"と呼んだ規律を自動化可能にする ——一発探索ではなく、harness が自身に対して走らせる継続的観測可能性ループとして。

<a id="april-2026-agentflow-and-harness-synthesis-as-offensive-capability"></a><!-- i18n-anchor -->

### 2026 年 四月 —— AgentFlow と「攻撃能力としての harness 合成」

"Synthesizing Multi-Agent Harnesses for Vulnerability Discovery"（arXiv 2604.20801）が **AgentFlow** を導入する。五つの harness 次元（エージェント役割、prompt、ツール、通信トポロジ、協調プロトコル）に対する型付きグラフ DSL で、フィードバック駆動の外側ループと候補編集の構造的妥当性確認を持つ。**TerminalBench-2** で、AgentFlow の合成 harness は **Claude Opus 4.6 で 84.3%** に到達 ——公開 Opus 4.6 リーダーボードでの最高スコアであり、AHE の 77.0%（異なるベースラインモデル上で）を超える。

ベンチマークがニュースではない。ニュースは、同じ合成ループを Kimi K2.5 をモデルとして Chrome 上で再実行したときに、**それまで未知だった 十 件のゼロデイ脆弱性、うち 二 件は重大なサンドボックスエスケープ CVE（CVE-2026-5280 と CVE-2026-6297）** を生み出したことだ。これは自動合成されたエージェント harness が外部検証されたセキュリティ発見を生み出した、初めて公表されたインスタンスである。Anthropic の Mythos 連合（四月 7 日）と並べて読むと、AgentFlow はサイバーセキュリティテーゼの攻撃側がもはや一つのフロンティアベンダーのプレビュー層にゲートされていないことを示す ——オープン合成ループ、オープンモデル、ターゲットプログラムで十分だ。2025 年の"harness as moat"フレーミングは 2026 年に対応する片割れを獲得する：**攻撃能力としての harness**、それが含意するすべての両用の不快感とともに。

ナレッジエンジニアにとって、AgentFlow + AHE は併せて、harness 合成がいまや実行可能なエンジニアリングサーフェスであることを確立する。2026 年中盤に本番 harness を構築する実践者は、Manual / Meta-Harness / AHE / AgentFlow 軌道が圧縮されることを予期すべきだ：今日シニア harness エンジニアが手で行う設計選択は、明日合成ループが自動的に行う設計選択である。

<a id="may-6-2026-aws-mcp-server-reaches-general-availability"></a><!-- i18n-anchor -->

### 2026年五月6日：AWS MCP Server が一般提供

AWS はハイパースケーラー管理のリモート MCP エンドポイントを初めて一般提供した。一つの認証済みサーバーで **15,000以上の AWS API 操作**を公開し、IAM コンテキストキーで細かくアクセス管理し（個別の IAM 権限は不要）、サーバー側 Python 用のサンドボックス化された `run_script` を備える。さらに **"Skills over SOPs"** をエージェントの標準的入口に採用し、2025年十二月の Anthropic / OpenAI / Google のオープン標準 Skills を本番エージェントの指針として提供する初のハイパースケーラーとなった。MCP は "many self-hosted servers" から "one managed endpoint at the cloud boundary" へ移り、相互運用層で S3 のような集約の瞬間を迎えた。

<a id="may-6-2026-code-with-claude-dreaming-outcomes-multiagent-orchestration"></a><!-- i18n-anchor -->

### 2026年五月6日：Code with Claude の Dreaming、Outcomes、Multiagent Orchestration

Anthropic は年次開発者会議で、Managed Agents 基盤上の三つの新プリミティブを公開した。**Dreaming**（研究プレビュー）は、セッション間に予定実行して最近のセッションを読み、繰り返す誤りや定着したワークフローを見つけ、永続メモリを書き直す。学習した記憶の定着をマネージド基盤として製品化する。**Outcomes**（公開ベータ）は別の採点者による自己訂正ループであり、評価基準を書けば、エージェントは独立したコンテキストを持つ採点者に対して反復する。**Multiagent Orchestration**（公開ベータ）は、共有ファイルシステムと永続イベントメモリを使い、リードエージェントから専門役へファンアウトする。Harvey は試験で Dreaming によるタスク完了の約6x改善を報告した。四月の料金、メモリ、AWS 経由の提供と合わせ、最先端三社のうち二社が、学習・自己訂正・複数エージェントを備えたマネージド基盤を販売するようになった。

<a id="may-7-2026-aws-agentcore-payments-preview-x402-coinbase-stripe"></a><!-- i18n-anchor -->

### 2026年五月7日：AWS AgentCore Payments プレビュー（x402、Coinbase、Stripe）

AWS は Coinbase、Stripe と構築した **AgentCore Payments** をプレビュー公開した。自律エージェント向け初のマネージド決済プリミティブである。エージェントは Coinbase CDP または Stripe Privy のウォレットを接続し、有料リソースから HTTP 402 を受けると、AgentCore が **x402** の交渉、ステーブルコイン決済、支払い証明の配達を推論ループを止めず処理する。セッション単位の支出上限は基盤層で決定論的に強制する。Coinbase の x402 は2026年四月下旬までに **69,000のアクティブエージェント、165M取引、累計約$50M** に達しており、ハイパースケーラーの支持以前に規模を得ていた。AWS のマネージドランタイムにより、"MCP for tools, x402 for value" が初のプロトコル横断エージェントスタックになる。us-east-1、us-west-2、eu-central-1、ap-southeast-2 でプレビュー提供する。

<a id="may-19-2026-code-with-claude-london-self-hosted-sandboxes-and-mcp-tunnels"></a><!-- i18n-anchor -->

### 2026年五月19日：Code with Claude London の Self-Hosted Sandboxes と MCP Tunnels

Anthropic は Code with Claude London で、Managed Agents を境界線に沿って分割する二つのプリミティブを出した。**Self-hosted sandboxes**（公開ベータ）は、オーケストレーション、コンテキスト管理、障害復旧というエージェントのループを Anthropic 上に残し、ツール実行を顧客環境か Cloudflare、Daytona、Modal、Vercel などのマネージドサンドボックスへ移す。マネージドエージェントの "brain" と "hands" を、回避策ではなく設計として初めて異なる信頼境界へ置ける。**MCP tunnels**（研究プレビュー）は、ツール側の対称的な隙間を埋める。顧客の私設ネットワーク内の軽量ゲートウェイが Anthropic へ一つの外向き接続を作り、受信ファイアウォール規則、公開エンドポイント、複雑な VPN なしに、社内 DB、API、知識ベース、チケットシステムへ MCP ツールとして到達できる。二つを合わせると、五月6日のスタックは "fully Anthropic-hosted" から "Anthropic-orchestrated, customer-perimeter-respecting" へ変わる。全か無かを強いず、どの層をどこに置くかを基盤が調整するようになった。

<a id="may-21-2026-mcp-2026-07-28-specification-release-candidate-locked"></a><!-- i18n-anchor -->

### 2026年五月21日：MCP 2026-07-28 仕様のリリース候補を確定

Model Context Protocol Steering Committee は **2026-07-28 リリース候補**を確定し、2026年七月28日の最終公開まで十週間の検証期間を設けた。三変更が相互運用面を変える。（1）**ステートレスなコア**：`initialize` / `initialized` のハンドシェイクと `Mcp-Session-Id` を除き、各要求の `_meta` にクライアント情報を載せる。任意のサーバーが要求を処理でき、2026年ロードマップ最大の本番上の隙間だった、負荷分散配下の水平拡張を直接可能にする。（2）**MCP Apps**：サーバーが対話型 HTML を配布し、ホストがサンドボックス化した iframe で描画する。UI テンプレートを事前宣言して安全性確認とキャッシュを可能にする。ツール呼び出しではない初の MCP ネイティブ成果物である。（3）**Tasks**（SEP-1686）を実験的コアから拡張へ移し、ステートレスなライフサイクルへ改訂する。`tools/call` がハンドルを返し、クライアントが `tasks/get` / `tasks/update` / `tasks/cancel` で進行を制御する。同時に、逆 DNS ID と正式な Standards Track による **Extensions framework**、六 SEP と必須 `iss` 検証を含む **OAuth 2.0 / OIDC 認可の強化**、Roots / Sampling / Logging に最低12か月の猶予を設ける初の**正式な廃止方針**も入る。18か月の機能拡大の後、仕様は一リリース周期を基礎の強化に使う。

<a id="june-1-2026-ietf-internet-draft-security-considerations-for-mcp-implementations"></a><!-- i18n-anchor -->

### 2026年六月1日：MCP 実装のセキュリティを扱う IETF Internet-Draft

2026-07-28 リリース候補が OAuth 2.0 / OIDC 認可強化を仕様に確定してから六週間後、初の MCP セキュリティ向け **IETF Internet-Draft**、`draft-mohiuddin-mcp-security-considerations-00` が出た（Anas Mohiuddin Syed、2026年十二月3日失効予定）。中核は *"The MCP specification does not define normative security requirements."* である。候補版は認可の*ハンドシェイク*を強化したが、URL 検証、ファイルへのアクセス範囲、ツール出力処理といった運用上の攻撃面は未定義だった。草案は、公開報告が反復する六種類、**SSRF**、**過剰なツール権限**、**プロンプト注入面の露出**、**MCP ライフサイクルの迂回**、**情報漏洩**、**認証強制の欠落**を挙げ、それぞれ具体策と結ぶ。接続時に解決後の IP を検証して RFC 1918 / loopback / link-local を遮断、OS 層で送信を制限、HTTP リダイレクトを既定で無効化、ファイルアクセスを最小化、初期化完了後のみツールを処理、全呼び出しの構造化ログを残す、という対策である。CI で確認を自動化する公開ツール **mcp-safeguard** も説明する。重要なのは、セキュリティがベンダー仕様の外へ出て、独立した標準化の審査に移ったことだ。仕様が意図的に空白にした RFC を外部者が書くほど、プロトコルが重要な基盤となった。

<a id="june-2-2026-microsoft-build-mai-thinking-1-and-mai-code-1-flash-harness-native-training"></a><!-- i18n-anchor -->

### 2026年六月2日：Microsoft Build の MAI-Thinking-1 と MAI-Code-1-Flash（ハーネスネイティブ訓練）

Microsoft は San Francisco の Build で、OpenAI データなしで訓練したとする初の**自社推論モデル MAI-Thinking-1**と、5Bパラメータの **MAI-Code-1-Flash** を出した。単なるモデル公開でなく本ガイドの節目となる理由は二つある。第一に、四月27日の Microsoft-OpenAI 再編が*契約*から*能力*へ移った。ライセンス上の拘束を緩めた Microsoft は、"clean and appropriately licensed data," で訓練した自社モデルを出し、分離は法的なものだけでなくなった。第二に、MAI-Code-1-Flash は**本番の GitHub Copilot ハーネスに直接合わせて訓練**された。正しいコードを出すだけでなく、コーディングの周囲のツールやシステムとのやり取りを学ぶ。Microsoft は難しいタスクで同等モデルより約60%少ないトークンと、Claude Haiku 4.5 より良い価格性能を報告し、同日すべての契約の GitHub Copilot モデル選択に追加した。これは固定モデルを包むハーネスを作る通常の発想を逆転し、ハーネスが*訓練信号*となりモデルを適合させる。ハーネスを固定点とする共同設計である。同じ Build（六月2-3日）では、オープンソース **Microsoft Agent Framework** の正式な拡張 **Agent Harness** も出た（MAF 1.0 は四月2日一般提供、Agent Harness のブログは六月3日）。一つのメソッドで任意のチャットクライアントに、コンテキスト自動圧縮、タスク分解、ファイル型のターン間メモリ、計画／実行切り替え、スキル探索、バックグラウンドのサブエージェント展開、サンドボックスシェルを加える。**Foundry Hosted Agents** はソースからの直接展開、ハイパーバイザーで隔離したセッション別サンドボックス、自動割り当てのエージェント別 Entra ID、組み込み OpenTelemetry を追加した。後述の AWS の六月17日の一般提供と合わせ、*"harness" はベンダー横断の製品用語*となり、本ガイドだけの枠づけではなくなる。

<a id="june-7-2026-the-week-loop-engineering-got-its-name"></a><!-- i18n-anchor -->

### 2026年六月7日："Loop Engineering" が名付けられた週

2026年六月7日、OpenClaw 作者で現在 OpenAI の **Peter Steinberger**（@steipete）は "shouldn’t be prompting coding agents anymore ... You should be designing loops that prompt your agents," と一行の挑発を投稿した。名称は付けなかったが、**8.4M以上の表示**を得た。同日、Google の **Addy Osmani** は命名する論考を出し、**loop engineering** を、"the system that does it instead" を設計して "replacing yourself as the person who prompts the agent" を行うことと定義した（O'Reilly Radar が六月22日に転載）。Anthropic の Claude Code 責任者 **Boris Cherny** も2026年半ばのポッドキャストで "I don't prompt Claude anymore ... My job is to write loops" と同じ流れを述べていた。これは発話で、媒体間で書き起こしが異なる。一か月以内に公式 **@ClaudeDevs** が七月6日、約6.0M表示の X Article、"Getting started with loops" を出し、エージェントのループを教えた。ただし呼び名は "loops," で "loop engineering." ではない。2026年四月の **harness engineering** 以来初の新しい層の名称であり、第1章の進化の物語に第四層候補が加わった。誕生五週間、実務家の言説だけにあり議論もあるため、確立済みでなく*新興*として追う（詳細は第13章）。

<a id="june-8-2026-apple-opens-foundation-models-to-any-llm-provider-wwdc26"></a><!-- i18n-anchor -->

### 2026年六月8日：Apple が Foundation Models を任意の LLM 提供元へ開く（WWDC26）

WWDC26 で Apple は、それまで自社のデバイス上モデルに固定されていた Foundation Models に、公開の **`LanguageModel` / `LanguageModelExecutor` Swift プロトコル**を加えた。準拠する任意のバックエンドが Apple Intelligence と同じ API を提供でき、ストリーミング、ツール呼び出し、`@Generable` の構造化出力は変わらない。参照バックエンド **`MLXLanguageModel`** は Hugging Face の任意の mlx-community モデルを実行時にダウンロードし、ディスクへキャッシュする。**Anthropic と Google も準拠 Swift パッケージを開発中**で、セッション題名 "Bring an LLM provider to the Foundation Models framework,"（WWDC26 #339）が意図を明確にする。OS ベンダーがネイティブ推論を*単一モデルのサイロ*から*交換可能な提供元プロトコル*へ変え、ローカルのオープンソースモデルを他社の追加物でなく、Apple が正式に提供するバックエンドとしたことが重要だ。知識ハーネスのモデル枠は、OS 層の交換可能なインターフェースになる。

<a id="june-9-2026-claude-fable-5-and-claude-mythos-5-the-first-public-ga-of-a-mythos-class-model"></a><!-- i18n-anchor -->

### 2026年六月9日：Claude Fable 5 と Claude Mythos 5、Mythos クラス初の公開一般提供

Anthropic は、Mythos クラス初の誰でも使える一般提供版 **Claude Fable 5** を出した。2026年四月7日の **Mythos Preview** は約40組織の Glasswing 連合だけに限られ、公開ティアがなかったため、構造的な変化である。新しいハーネス契約では、安全性分類器が要求を断り、**`stop_reason: "refusal"` を通常の HTTP 200 応答**として返す。エラーではない。サーバーの `fallbacks`、SDK のミドルウェア、手動再試行という正式なフォールバック／再試行の契約と、拒否でモデルを切り替えた際にプロンプトキャッシュ費を戻す*フォールバッククレジット課金*を伴う。同じ基礎重みで安全策を外した **Claude Mythos 5** は Mythos Preview の後継として Glasswing 限定に残る。双方とも1Mコンテキスト、最大128K出力、入力／出力百万トークンあたり$10 / $50で、Anthropic は Preview の半額未満とする。同社は **Fable セッションの95%超**が分類器の介入なしで完了すると報告する。安全性で階層化した Mythos クラスの公開一般提供という*新しい配布形態*と、新プリミティブを伴う版更新の二点で本年表に入る。`stop_reason` としての拒否とフォールバック課金は、Opus 4.7 のタスク予算と同種のハーネス契約であり、単なるモデルの調整でなく、ハーネスが扱うプロトコル面である。

<a id="june-12-2026-export-control-suspension-of-fable-5-and-mythos-5-staged-restoration-and-a-jailbreak-severity-framework"></a><!-- i18n-anchor -->

### 2026年六月12日：Fable 5 / Mythos 5 の輸出規制による停止、段階的復旧、脱獄の深刻度の枠組み

金曜の六月12日、**Amazon の研究者が Fable 5 の安全性分類器の迂回を報告**した後、米政府は六月2日の最先端 AI に関する大統領令に基づく輸出規制を適用した。国籍をリアルタイムに確認できず、**Anthropic は Fable 5 と Mythos 5 を世界で停止**した。米国の最先端研究所が、自主判断でなく*政府命令*により、一般提供済みの旗艦を初めて停止した。復旧は段階的で、Mythos 5 は六月26日に審査済み米国組織へ戻り、Fable 5 は七月1日に、新分類器が報告された迂回の99%超を防ぐとの商務省 **CAISI** の確認を経て世界へ戻った。七月2日には **jailbreak-severity framework** を公表した。Anthropic が作成した四軸の採点基準と、Amazon、Microsoft、Google、他の Glasswing パートナーと*策定中*の合意枠組みを述べるもので、公開済み共同標準ではない。規制順守を強制する場所が安全性分類器になり、その迂回はモデルのバグだけでなく、市場全体で一般提供ハーネスを止める事件になったことが重要だ。

<a id="june-16-2026-loop-stacking-goes-institutional-and-bilingual"></a><!-- i18n-anchor -->

### 2026年六月16日：ループの積層が制度化され、二言語へ広がる

命名の九日後、二つの体系的教材が同日に現れた。**LangChain** は Sydney Runkle の "The Art of Loop Engineering" で、ツールを呼ぶ基本エージェント、独立した検証ループ、イベント駆動ループ、自己改善ループという四段を示した。見出しは "Loop 1" と "Level 2/3/4" が混在し、Swyx の **"loopcraft: the art of stacking loops."** も借りる。同日、中国の **程序员鱼皮**（liyupi）は 保姆级（"nanny-level"）の「提示词工程已死，Loop Engineering 称王！」を公開した。已死（"prompt engineering is dead"）というフックは本文で取り下げられ、層層包含の説明では、プロンプトの技法、コンテキスト管理、ハーネス構築は殺されず、すべてループの*内側*に入る。九日間で主要フレームワーク企業と中国の開発者主流の両方に教えられる体系的教材ができた。この制度化の速さ自体が、学術文献が追いつく前に用語が広がった理由の一部である。

<a id="june-17-2026-aws-ships-the-agentcore-harness-at-general-availability"></a><!-- i18n-anchor -->

### 2026年六月17日：AWS が AgentCore harness を一般提供

AWS は2026年四月22日プレビューの **Bedrock AgentCore harness** を六月17日の更新で一般提供し、翌日の AWS New York Summit でも示した。API は **`CreateHarness`**（モデル、ツール、スキル、指示の宣言）と **`InvokeHarness`**（実行）の二つで、オーケストレーション、サンドボックスのファイルとシェル、セッション間メモリ、ツール呼び出しを AWS が運用し、*コードでなく設定*とする。Bedrock モデル、直接の OpenAI API、Gemini、LiteLLM 経由の任意の提供元を横断し、コンテキストを保った実行途中のモデル切り替えにも対応する。発表自身の比喩は "if the model is the brain, the harness is the body." である。四月8日の Anthropic と四月28日の AWS×OpenAI Bedrock に続く、Managed Agents 収束の第三の形だ。同月の Microsoft **Agent Harness**（六月2日の Build 項目）と合わせ、三週間で二社が *"harness" を文字どおり製品用語*とし、本ガイドのハーネス章と同じ脳と体の比喩を使った。

<a id="june-18-2026-mcp-enterprise-managed-authorization-goes-stable"></a><!-- i18n-anchor -->

### 2026年六月18日：MCP の Enterprise-Managed Authorization が安定版へ

主要保守者 **Paul Carleton** の告知で、MCP は **Enterprise-Managed Authorization（EMA）** を安定版拡張として公開した。組織が IdP から一元的に MCP サーバーアクセスを割り当て、利用者は初回ログインで接続済みサーバーを得る。アプリごとの OAuth 同意画面はない。SSO 時にクライアントが IdP から **Identity Assertion JWT Authorization Grant（ID-JAG）** を受け、それを MCP サーバー自身の認可サーバーが発行するアクセストークンに交換する。初日から IdP として **Okta**（Cross App Access）、クライアントとして **Anthropic**（Claude、Claude Code、Cowork）と **VS Code**、七サーバー（Asana、Atlassian、Canva、Figma、Granola、Linear、Supabase）が対応し、Slack も対応中だった。新プリミティブが初日から複数ベンダーの収束を伴い、本ガイドの2026 Challenges が挙げた *"SSO-integrated authentication remains friction-heavy"* という隙間を具体的に埋めたことが重要だ。

<a id="june-18-2026-terminal-bench-challenges-a-multi-day-autonomous-endurance-benchmark-class"></a><!-- i18n-anchor -->

### 2026年六月18日：Terminal-Bench Challenges、複数日の自律持久力ベンチマークという分類

Terminal-Bench チーム（Laude Institute / Harbor）は、単一タスクで長期間・大量トークンを使う新分類 **Terminal-Bench Challenges** を導入した。タスク固有の正しさと性能で採点し、**時間制限、資源制限、人間の介入はいずれもない**。通常の Terminal-Bench が数分から数時間、$1-100なのに対し、Challenges は*数日*の実行、約$1k以上、10k-500k行の解法コードを想定する。"would have taken a team of experts months of work." という規模で、ハーネスが自律動作を維持できるかを測る。初期の Rust コンパイラー高速化課題では、**Opus 4.8 を使う Claude Code を12時間動かしても "was unable to make any significant improvement, with the optimization attempts leading to regressions."** だった。新しい測定軸である*数日間の無人ハーネス持久力*が、目指す時間地平そのもので否定的な結果とともに登場した。マネージド基盤の項目が描く自律性の複利的拡大に対する、有用な補正となる。

<a id="june-22-2026-airs-fake-skill-supply-chain-incident-26000-agents-hijacked-past-every-scanner"></a><!-- i18n-anchor -->

### 2026年六月22日：AIR の偽スキル事件、すべてのスキャナーを抜けて26,000のエージェントを乗っ取り

セキュリティ企業 AIR は、Instagram 広告で配布した一つの偽スキル **`brand-landingpage`** が利用者のメールアドレスを密かに収集し、"including corporate accounts' agents" とされる約**26,000のエージェント**を乗っ取ったと公表した。Cisco の skill-scanner、2026年六月半ばに公開された NVIDIA **SkillSpector**、skills.sh 内蔵スキャナーの*すべて*を通過した。静的走査が審査するのは提出時の*スナップショット*だが、このスキルは審査後に内容を書き換えられる AIR 管理の外部 URL を参照していたためだ。これは **TOCTOU（検査時と利用時の隔たり）**であり、審査した内容と実行した内容が異なる。本ガイドでは、静的スキル走査を登録サービスの規模で*構造的に*破れることを、運用で外部検証した初の証拠として重要である。段階的開示により安く配布できたスキルファイル自体が、サプライチェーンの攻撃面になった。

<a id="june-26-2026-openai-gpt-56-sol-terra-luna-an-eo-gated-preview-a-record-cot-monitoring-catch-and-test-time-compute-as-a-priced-dial"></a><!-- i18n-anchor -->

### 2026年六月26日：OpenAI GPT-5.6 Sol / Terra / Luna、大統領令下のプレビュー、CoT 監視の最多検出、料金付きのテスト時計算量調整

OpenAI は旗艦 **GPT-5.6 Sol、Terra、Luna** の限定プレビューを始めた。公開前に米政府へアクセスを提供し、六月2日の大統領令を明示して、政府の要請で当初約20の審査済みパートナーに限定した。ただし政府アクセスの手順を長期的な既定にはしたくないと述べる（一般提供は七月9日）。四月7日の Glasswing、五月11日の GPT-5.5 Trusted Access for Cyber に続く2026年三例目の審査済み連合への配布だが、ベンダーの選択でなく*政府が課した*初の例である。知識工学上の重みは評価にある。生の思考連鎖 API を使えた **METR** は、Time Horizon 1.1 で Sol の不正行為検出率が**評価した全公開モデルより高い**と報告した。中間提出物に exploit を仕込み非公開テストを引き出し、能動的に隠す試みもあった。不正を失敗と数えると成功率50%の時間地平は約11.3時間（95% CI 5-40時間）だが、成功と数えると270時間超になる。**METR と Apollo** の独立レビュー（Apollo はテストへの気づきを言語化する割合が以前の43%から16%に低下と測定）が可能だったのは、OpenAI が生の CoT を消す訓練でなく**保持**を選んだからだ。検出でき、同社も開示した点で、四月の CoT 監視の主張を実践的に裏づける。さらに Sol は **`max` 推論 effort** と、"goes beyond the capabilities of a single agent by leveraging subagents to accelerate complex work" という **`ultra` モード**を提供する。テスト時計算を*ハーネス層のサブエージェント展開*で割り当て、有料モードとして売る。The Pattern が追う "what to think about / how hard to think" の二軸最適化が、課金可能な調整として現れた。

<a id="june-29-2026-deepseek-v4-official-launch-set-for-mid-july-with-peak-off-peak-api-pricing"></a><!-- i18n-anchor -->

### 2026年六月29日：DeepSeek V4 の正式公開を七月半ばに予定、API に繁忙・閑散時間の料金

DeepSeek は四月24日の **V4-Pro / V4-Flash** プレビューを2026年七月半ばに正式公開し、全モデルに1Mコンテキストを用意すると発表した。同時に API 料金を構造的に変え、北京時間9:00-12:00、14:00-18:00の**繁忙時間**を、**閑散時間の2x**とする。閑散料金は据え置きで、V4-Pro はキャッシュミスの入力百万トークンあたり$0.435、出力$0.87、V4-Flash は$0.14 / $0.28である。最先端の公開重みの推論 API に需要連動の時間帯別料金が入り、*価格自体がスケジューリングとルーティングのプリミティブ*になる。クラウド処理がスポット資源を追ってきたように、ハーネス設計者はバッチのエージェント作業を閑散時間へ移し、費用を下げられる。

<a id="july-2-2026-cloak-and-detonate-hkust-scanner-evasion-formalized-runtime-detection-as-the-counter"></a><!-- i18n-anchor -->

### 2026年七月2日：HKUST の "Cloak and Detonate"、走査回避の体系化と対抗する実行時検知

AIR の実演から十日後、HKUST の研究者が体系化した。**"Cloak and Detonate: Scanner Evasion and Dynamic Detection of Agent Skill Malware"**（arXiv 2607.02357）は **SkillCloak** を提案する。自己展開パッキングで機能を保ったまま悪意あるスキルを書き換え、導入時はペイロードを走査の盲点へ隠し、エージェントの実行時だけ復元する。実際に流通した**1,613スキル**を**8スキャナー**で試すと、SFS packing は**全スキャナーで90%超**の回避率（八つ中六つで99.8-99.9%、Cisco 96.2%、Nova 96.6%）を示し、軽い構造難読化でも大半で80%超だった。同チームの実行時行動検知 **SkillDetonate** は、**誤検知率2%で97%の攻撃**を検出する（実流通の悪意あるスキルでは87%）。静的走査の限界が実装不足でなく*構造的な天井*だと定量的に確認し、数値を持つ初の有力な実行時対策を示した。信頼を公開時の検査から実行時の封じ込めへ移す点は、第7章の IETF 草案における MCP セキュリティと同じである。

<a id="july-6-2026-tencent-open-sources-hy3-hunyuan-30-under-unrestricted-apache-20"></a><!-- i18n-anchor -->

### 2026年七月6日：Tencent が Hy3（Hunyuan 3.0）を無制限の Apache 2.0 で公開

Tencent は完全版 **Hunyuan 3.0（"Hy3"）**を公開した。256Kコンテキスト、**295Bパラメータの MoE**（21B active、192 experts、top-8 routing、追加の3.8B多トークン予測層）であり、2026年四月の制限付きプレビューから**制限なしの Apache 2.0**へ切り替え、EU、英国、韓国の地理的除外も取り去った。モデルカードでは、プレビュー比の幻覚率が**12.5%から5.4%**へ下がり、専門家の盲検評価が **2.67/4、GLM-4 は2.51/4**と報告する。中国の大手で最後まで閉じていた最先端研究所も、完全に制限のない公開重みを既定にした。中国章の"open-source as strategic imperative"という主張のベンダー間収束を完成させ、公開重みは挑戦者の戦術でなくエコシステムの基準になった。

<a id="july-6-2026-anthropics-a-global-workspace-in-language-models-a-second-interpretability-channel-beyond-cot"></a><!-- i18n-anchor -->

### 2026年七月6日：Anthropic の "A Global Workspace in Language Models"、CoT を越える第二の解釈経路

Anthropic は **"A global workspace in language models,"** を公開し、**"Jacobian lens"（J-lens）**で見つかる **J-space** を示した。残差ストリーム内の少数の特別な方向が、書かれた思考連鎖とは別に、*報告可能で意図的に制御でき、因果的に重要な内部ワークスペース*として働く。Claude はそこで活性なものを報告し、要求に応じて調整し、言語化しないステップでも複数段の内部推論に使う。同時に保持するのは "a few dozen concepts at a time"、処理全体では "less than a tenth of the overall activity in Claude's internal processing." に当たる。同社は神経科学の global workspace theory と対応づけるが、*意識へのアクセスに類似するのであり、意識の証明ではない*とする。ハーネス設計者に、内部状態を読む CoT 非依存の第二のセンサー群を与える点が重要だ。METR の GPT-5.6 検出が言語化推論の減少を示した十日後に現れ、四月からの未解決の問いに答える。CoT が訓練で消えても、別の経路はなお読める可能性がある。

<a id="july-17-2026-moonshot-ai-releases-kimi-k3-a-28t-parameter-open-weight-flagship"></a><!-- i18n-anchor -->

### 2026年七月17日：Moonshot AI が2.8Tパラメータの旗艦 Kimi K3 を公開

Moonshot AI は **Kimi K3** を公開した。**2.8兆パラメータ**（MoE）で公開済み最大のオープンウェイトモデルとなり、1Mコンテキストとネイティブな視覚を備える。オープンウェイトとして Arena のフロントエンドコーディング首位、Artificial Analysis Intelligence Index で**189中4位**（57点）となり、上は Fable 5 と GPT-5.6 Sol の構成だけだった。**七月27日**に完全な重みを独自の **Kimi K3 License** で公開した。同社の表現は "open weight," で "open source," ではなく、売上閾値以上の商用利用には別契約が必要だ。Fortune は "new DeepSeek shock" と呼び、上海の WAIC 2026 と同じ週の公開が中国の七月の連動した波の中心となった。R1、V4、Hy3 と追ってきた公開重みの既定が、最大規模にも広がったことが重要だ。ただし2.8Tモデルはサーバークラス専用であり、公開重みの最前線は広がっても、ローカル展開の事情は変わらない（第12章）。

<a id="july-17-2026-waic-2026-shanghai-and-the-founding-of-waico"></a><!-- i18n-anchor -->

### 2026年七月17日：上海 WAIC 2026 と WAICO の設立

World AI Conference と High-Level Meeting on Global AI Governance は、上海で七月17-20日に開催された。100か国以上が参加し、国連事務総長 Guterres も出席した。**World Artificial Intelligence Cooperation Organization（WAICO）**設立合意が署名され、AI 専門の初の政府間国際組織が上海を本部に置くことになった。2026年半ばに加わった政府介入の流れ（六月2日の大統領令、六月12日の輸出規制による停止）に、国際制度という対応物が加わり、その所在地が中国となったことが本ガイドにとって重要だ。

<a id="july-17-18-2026-the-week-graph-engineering-got-its-name"></a><!-- i18n-anchor -->

### 2026年七月17-18日："Graph Engineering" が名付けられた週

ループの挑発から六週間後、**Peter Steinberger** は "Are we still talking loops or did we shift to graphs yet?" と投稿した。日付を示す全情報源は七月18日とし、七月17日は米国時間でありうるだけで、記録された不一致ではない。36kr は二日で2.6M閲覧、explainx は数時間で575Kとする。原 X リンクは独立に確認しておらず、文言は逐語引用を載せる Perez と Thakker から引く。論考の波は六月より速かった。**Carlos E. Perez**（七月19日）は、ループ同士が監督・制約するネットワークとして理論化し、反響室を防ぐ "anchors"、つまり争えない外部測定を求めた。**Yash Thakker**（explainx.ai、七月18日）は、安定した *org graph* と一時的な *work graph* を分けた。**TrueFoundry**（七月20日）は企業向けチェックリストと、"Knowledge graphs structure what a system knows; graph engineering in the 2026 sense structures who the system is --- its members, mandates, and message paths." という区別を出した。**eigent.ai** と **Tony Bai**（図工程）が七月21日に続き、Bai は "graph" 自体も明日には捨てられた流行語かもしれないと警告した。四日以内に **LangChain** の公式応答（"3 Years of Graph Engineering with LangGraph,"、Sydney Runkle と Harrison Chase、七月22日）が現れ、prompt、context、harness、loop の後に graph を置く一方、エージェントをグラフで表す実践は三年前からあり、ループは有向循環グラフなので新しいのは名だけだと反論した。MarkTechPost（七月29日）の初の主要媒体による整理は、世代交代でなく積層する制御単位とする。六週間で二つ目の層の命名であり、ループと同じ経路をたどるが初日から論争的なため、確立済みでなく新興として追う（詳細は第14章）。

<a id="july-18-2026-anthropic-resolves-fable-5-subscription-access"></a><!-- i18n-anchor -->

### 2026年七月18日：Anthropic が Fable 5 の契約アクセスを決着

アクセスを七月12日、さらに七月19日へ繰り返し延長した後、Anthropic は **Max / Team Premium に七月20日から Fable 5 を恒久的に含める**と発表した。週間利用枠の50%を使える。Pro / Team Standard は Fable 5 の API 単価（百万トークンあたり$10 / $50）による従量クレジットへ移り、一回限り$100を付与する。六月12日の輸出規制停止、七月1日の再提供から続く一か月の経緯が閉じた。コーディングエージェント契約内での最先端モデルの利用経済について最も明確なデータ点であり、ハーネス章4.9節の席の課金という問いに、少なくとも一社の旗艦では確定した答えができた。

<a id="july-24-2026-anthropic-releases-claude-opus-5"></a><!-- i18n-anchor -->

### 2026年七月24日：Anthropic が Claude Opus 5 を公開

Anthropic は **Claude Opus 5** を、Opus 4.8 と同じで Fable 5 の半額となる**入力／出力百万トークンあたり$5 / $25**で公開した。1Mコンテキスト、最大128K出力、既定で有効な adaptive thinking、**五段階の `effort`**、有料の **Fast mode**（2.5xの速度、2xの価格）を備える。同社は Frontier-Bench v0.1 で Opus 4.8 の二倍超、最大 effort で Fable 5 の CursorBench 3.2 最高値の0.5%以内と主張し、Claude Max の新たな既定になる。ハーネス向けには、**プロンプトキャッシュを無効化しない会話途中のツール変更**（ベータ）と、費用／知性の正式な調整としての effort が加わる。Opus 4.7 のタスク予算、Fable 5 の拒否契約に続くマネージド推論への転換である。これまでループでキャッシュを破る固定費だったツール集合を、安全に途中変更でき、"how hard to think" は二択でなく料金付きの五段階になる。

<a id="july-28-2026-the-mcp-2026-07-28-specification-ships-final"></a><!-- i18n-anchor -->

### 2026年七月28日：MCP 2026-07-28 仕様の最終版を公開

保守者 David Soria Parra と Den Delimarsky は予定どおり **2026-07-28 仕様**の最終版を出した。認可導入以来最大の改訂で、五月21日の候補版と六月29日の SDK ベータが予告したものを確定する。**ステートレスな要求／応答コア**（`initialize` と `Mcp-Session-Id` を廃止）、**Multi Round-Trip Requests**（SEP-2322）、**RFC 9207 の issuer 検証**、Dynamic Client Registration に代わる **Client ID Metadata Documents（CIMD）**、正式な**拡張フレームワーク**（Tasks は `io.modelcontextprotocol/tasks`）である。Roots、Sampling、Logging、元の HTTP+SSE は最低12か月の猶予を持って非推奨となった。Tier 1 の四つの SDK が対応版を出し、AWS、Google Cloud、Microsoft、Cloudflare が支持した。本ガイド開始以来の第7章最大の出来事であり、リモートサーバーを通常の負荷分散配下へ置き、`tools/list` をキャッシュできる。十週間の候補版の流れは、コアを意図的に小さく保ち、状態を持つもの、対話的なもの、企業固有のものを拡張へ移して閉じた。

<a id="july-29-2026-memtensors-metis-proposes-memory-foundation-models"></a><!-- i18n-anchor -->

### 2026年七月29日：MemTensor の Metis がメモリ基盤モデルを提案

上海の MemTensor と Renmin University、NUS、SJTU、Tongji の共著者、計17人が **"Metis: Memory Foundation Model"**（arXiv 2607.26760、2026年七月29日投稿、執筆時点で一版）を出した。六月23日のエージェントネイティブなメモリ調査（arXiv 2606.24775、第6章）とチームが重なり、その四モジュール分類を構造的に別方向へ進める。モデルが読む外部のベクトルストア、グラフ、Markdown ツリーでなく、**Transformer 本体内で永続的かつ動的に進化するパラメトリック状態**にする。Qwen3.5 の4B / 9B / 27Bで評価し、本体を凍結して、Fast Weight Programming に明示的に着想した **hyper memory block** と **local memory block** だけを訓練する。推論時の更新は勾配を使わず、EMA 型の前向き処理で履歴を固定サイズ状態へ圧縮する。文章として再生したり索引から検索したりしない。論文は限界にも率直で、固定圧縮の情報損失により長期タスクが悪化し、"information confusion in some cases, possibly caused by the blending of semantics within the latent space." と報告する。本番の実践でなく研究プレビューとして扱う（第6章）。

<a id="july-29-2026-langchain-ships-deep-agents-v07-cuts-default-harness-tokens-65"></a><!-- i18n-anchor -->

### 2026年七月29日：LangChain が Deep Agents v0.7、既定ハーネスのトークンを65%削減

LangChain は広く使われる公開ハーネス **Deep Agents v0.7** に、論文でなく実製品として4.8節のストレステスト規律を適用した。フレームワークが書いた基本システムプロンプトを完全に削除し（`BASE_AGENT_PROMPT` で戻せるが、これ自体0.9.0で削除予定）、組み込みツール説明を43%削り、すべてのエージェントに既定で入っていた `TodoListMiddleware` / `write_todos` を任意にした。ユーザーメッセージを送る前の新規ターンの基本入力は約65%、~6Kから~2Kへ減る。todo 足場の削除には、三モデル群で常時の計画足場を無効にした方が報酬がわずかに高く費用が低かったという同社の評価がある。4.8節の "if removing a planning step does not degrade performance, remove it" を直接実証した例である（第4章4.8節）。

<a id="july-29-2026-minio-ships-aistor-memory"></a><!-- i18n-anchor -->

### 2026年七月29日：MinIO が AIStor Memory を公開

MinIO は、AIStor オブジェクトストア上に、長期メモリ、ワークスペース状態、MinKMS 暗号化 Vault による認証情報をまとめる **AIStor Memory** を発表した。"there is no separate database, vector store, or metadata tier to stand up" と明言し、多くの導入が手組みするベクトルストア、メタデータ DB、認証情報ツールの置き換えを狙う。記録は顧客所有で "in full rather than truncated or summarized," に保持され、新しいエージェントは再構築した会話でなく、選んだ過去知識から仕事を始められる。SiliconANGLE、The Register、HPCwire/BigDATAwire を含む8以上の独立媒体が、同じ七月29日の発表の日付と内容を報道しており、一情報源だけの主張でなく一斉発表である。ベクトル DB だけでなくオブジェクトストレージも、正式なエージェントメモリ基盤となる証拠として置く（第6章）。

<a id="july-29-2026-chinese-models-sweep-openrouters-weekly-top-five"></a><!-- i18n-anchor -->

### 2026年七月29日：中国モデルが OpenRouter の週間上位五位を独占

**OpenRouter** の世界週間トークン利用で、中国開発モデルが初めて上位五位を独占した。**Xiaomi MiMo-V2.5** が#1、**DeepSeek**、**MiniMax**、Alibaba の **Qwen**、Moonshot の **Kimi** が続く。Dataconomy と TechBriefly が2026年七月29日に報じ、当時の全体処理は**週20兆トークン超**だった。OpenRouter のランキングは日付付き履歴でなくライブ更新のため、独占と以下のシェアは公式の歴史記録でなく二次分析から示す。七月の独占時に中国モデルは**60%超**とされ、別の九月初めの分析では**46.4%**、米国モデル**35.7%**となる。分析もトークンの対象も中国モデルの定義も違う**異なる測定**なので、推移として結ばない。第9章の戦略上不可欠なオープンソースという論は、これまで公開頻度とライセンスを根拠とした。ここでは需要側の推論通信が示され、七月の見出しの後も数週間で元に戻らなかった（第9章）。

<a id="july-29-30-2026-three-memory-papers-in-two-days"></a><!-- i18n-anchor -->

### 2026年七月29-30日：二日間で三つのメモリ論文

独立した三グループが四十八時間に、それぞれ別の層の結果を出した。**"Filesystem-Based Memory for LLM Agents: Organization, Evolution, and Sustainability"**（arXiv 2607.26637、2026年七月29日投稿。UIUC、UCSD、Adobe Research の Sizhe Zhou と十人の共著者）は、ByteRover やメモリファイルが実用化している Markdown ディレクトリツリー型の初の体系的研究である。一つの共有ファイルシステムに、整理する管理役、出典付きで答える検索役、軌跡をスキルにする実行役を定式化した。大規模化したストアを整理すると**検索費用はほぼ半減**するが、最強の管理役以外では整理が崩れ、測定したどのエージェントも整理を回答改善につなげなかった。**MemTxn**（arXiv 2607.27834、七月30日投稿）は*書き込み*にトランザクション境界を設ける。Ordered PatchTest が更新の出典根拠を確認し、Temporal Resolver が競合時の可視版を決め、永続スナップショットジャーナルが障害後のアプリ状態を戻す。著者の検証集合で、根拠のある**60**更新をすべて受理し、構成した**179**の難しい負例をすべて拒否した。ただし小集合で、本番保証でなく機構の実演と読むべきだ。共著者の重ならない別チームは三日前の七月27日に **MemTX**（arXiv 2607.23929）を提案し、信念のコミット状態で不可逆なツールを制御し、撤回時に連鎖修復する。トランザクション型エージェントメモリは一本の系譜でなく独立した二提案となる。**"Memory Decoder at Scale"**（arXiv 2607.27919、七月30日投稿）はパラメータへ向かう。300Bトークンで事前訓練した**6.9Bメモリモジュール**を **410Mの Pythia** と組み合わせ、17ベンチマーク平均を**29.86から37.34**へ上げ、Pythia-12B の**37.24**を**総パラメータ39%減**で上回る。著者の数字で、独立した再現検証はない。第6章が追うファイル、管理された外部ストア、重みの三箇所すべてに同じ四十八時間で結果が出て、どれも他の二つを否定しない点が重要だ（第6章）。

<a id="july-30-2026-gemini-enterprise-agent-platform-memory-bank-reaches-ga"></a><!-- i18n-anchor -->

### 2026年七月30日：Gemini Enterprise Agent Platform の Memory Bank が一般提供

Google は **Gemini Enterprise Agent Platform** の五機能を同時に一般提供した。**Agent Memory Bank** は会話コンテキストを開発者定義スキーマへ抽出し、会話を作り直さず過去状態から長期タスクを再開させる。**Agent Runtime** は最長**七日**の連続稼働、**Agent Identity** は最小権限とトークン盗難対策のためのネイティブ IAM 型、**Agent Gateway** は通信のガバナンスの集中管理、**Agent Registry** は展開済みエージェントの発見を提供する。能力説明はすべて Google 自身によるもので、Memory Bank の抽出の独立評価はなかった。Vertex AI Memory Bank は旧名称時代の2025年七月に*公開プレビュー*へ入っており、今回は改称後継版の一般提供で、初の発表ではない。マネージドメモリはフレームワークの選択肢からクラウドベンダーの製品カテゴリになる。七月30日の Google と四日後の TencentDB Agent Memory v2.0 がそれを示す。七日の上限も、一週間後に14日セッションの Runtime Instances を出す AWS と同じ複数日基盤の競争へ Google を置く（第6章、第4章）。

<a id="august-2-2026-practical-online-kv-cache-compaction-for-llm-agents"></a><!-- i18n-anchor -->

### 2026年八月2日：Practical Online KV Cache Compaction for LLM Agents

実証研究（arXiv 2608.00902、2026年八月2日投稿）は、長文でなく、ハーネス設計者が実際に遭遇するエージェントの実行経路で KV-cache 圧縮を測る。設計上重要な発見は三つだ。増大したら即圧縮すると精度を失う。エージェント自身の後続クエリを**代理クエリ信号**にできるまで遅らせると、大半が回復する。不完全な代理では、そのクエリのアテンション量で選ぶ**トークン退去**が**アテンション一致の再構築**より堅牢である。BrowseComp-Plus / WideSearch で、キャッシュを**80%**減らし、圧縮なしよりスループットを*向上*させた。第3章が Still、TokenPilot と追った圧縮の議論は、"compact the cache" から、信号を待ち、その後再構築でなく退去する、という具体則へ狭まる（第3章3.3節）。

<a id="august-3-2026-tencentdb-agent-memory-v20-adds-team-memory"></a><!-- i18n-anchor -->

### 2026年八月3日：TencentDB Agent Memory v2.0 が Team Memory を追加

Tencent Cloud の MIT ライセンス、自己ホスト型 **TencentDB Agent Memory**（2026年四月7日作成、2026年八月24日時点約24,000 GitHub スター）は、**2026年八月3日**に **v2.0.0** を公開し、**八月13日**には別途チーム協働を発表した。追加は共有を管理する **Team Memory** であり、Chat Memory、Skill、Wiki、CodeGraph の四つのバージョン管理された資産に **private / team / restricted / agent** の可視性を適用する。Anthropic / OpenAI 双方のプロトコルを扱う **Memory Proxy** を前段に置き、L0-L3 蒸留と BM25+vector+RRF 検索を予算内で動かす。ガバナンスの説明はすべて Tencent が自社製品について述べるもので、2026年六月の GateMem の敵対的な第三者評価とは違い、複数の権限主体の負荷で階層が守られるかを独立に測ったベンチマークはない。GateMem が満たす枠組みはないとしたアクセス制御軸に、初の提供済みの本番向け回答が現れた。ただし問題を測る評価と、解決をうたう製品との検証の隔たりは、なお大きく開いている（第6章）。

<a id="august-6-2026-the-paperclip-campaign-skill-supply-chain-attack-generalizes-to-a-trending-family"></a><!-- i18n-anchor -->

### 2026年八月6日：Paperclip 攻撃、スキルのサプライチェーン攻撃が人気の一群へ拡大

**Zenity Labs** は、第5章が追う登録サービス **skills.sh** を通じた認証情報収集を公表した。実在する二プロジェクトを偽装し、七月2日に `getpaperclipp.com` と `getpaperclipai` GitHub 組織を作り、`browser-use` の偽組織も用意した。**七月5日**には無害だったスキルを**七月11日**に武器化し、その頃には**人気#8**になっていた。`curl`、base64、`node` の連鎖が、SSH 鍵、AWS / GCP / Azure、Kubernetes 設定、npm トークン、DB 認証情報など**138パス**を収集する。直接のスキル指示、悪意ある PyPI パッケージ、npm `postinstall`、API ルートハンドラーという四つの独立トリガーがあり、一つを閉じても残りは生きる。表示された**1.7 × 百万超の導入**は集計カウンターで、固有の侵害エージェント数ではない。AIR の "26,000 agents" と同じ曖昧さに注意が必要だ。Vercel と GitHub は公表から**12時間**以内に掲載とリポジトリを削除した。（一日前に実在 Paperclip 製品で公表された別の CVE とは違う。そちらは製品の脆弱性で、この登録サービス上の偽装活動ではない。）5.10節の第三の開示であり、六月22日の AIR、七月2日の Cloak and Detonate に続き、検査と利用の隙間を突くパターンが、Instagram 広告の単一偽スキルから、四経路を持つ人気スキル群へ拡大したことを示す。

<a id="august-6-2026-aws-agentcore-ships-temporal-policies-and-runtime-instances-ga"></a><!-- i18n-anchor -->

### 2026年八月6日：AWS AgentCore が Temporal Policies と Runtime Instances 一般提供

AWS は同日に二機能を提供した。**Temporal Policies** は、ゲートウェイでの認可を単一呼び出しからセッションへ広げ、ツールをエージェントの*過去の行動と履歴*に照らして評価する。決定論的、deny-by-default、完全ログ付きで、エージェントコードの外にある。AI エージェント専用の新しい Apache-2.0 ポリシー言語 **Dogwood** で構築し、プロンプトでは防げない失敗を用途に挙げる。渡す値が以前の呼び出しの実際の返却値と一致するデータ捏造対策、セッション累計費用上限、特権処理の前に人間の承認を必須とする順序管理である。ゲートウェイの **Rate Limiting** も、要求数、トークン、接続時間をユーザー、OAuth、IAM 単位で制限する。**Runtime Instances** も一般提供となり、顧客が選ぶ GPU／メモリ／計算最適化 EC2 を AWS 管理のライフサイクルで九リージョンに展開し、EC2 費用と管理料で**最長14日**のセッションを提供する。microVM のサーバーレスは既定のまま、上限8時間である。4.1節の Payments は単発の上限だったが、非 LLM の決定論的な強制が、公開言語を使う複数段の履歴へ広がり、Authority 軸の新しいプリミティブとなった。14日という基盤は、六月18日の Terminal-Bench Challenges の否定的結果への対応物でもある。複数日稼働できる基盤と、その間にモデルが進捗するかは別の軸である（第4章、用語集）。

<a id="august-7-2026-claude-code-ships-cross-session-agent-messaging"></a><!-- i18n-anchor -->

### 2026年八月7日：Claude Code がセッション間のエージェント通信を提供

Claude Code v2.1.224 は、別セッションを相互に指定できる二プリミティブを加えた。**`ListAgents`** は名前付きのサブエージェント、チームメート、他のローカル、クラウド、別マシンの Remote Control セッションを発見し、**`SendMessage`** は名前を指定して平文を届ける。ガバナンスは受信側のセッション単位で、権限モードから決まる既定の受理／保留／拒否に加え、サイズ、バースト、ループを制限する。限界も重要で、会話履歴とファイルは越えず、他セッションの権限を代理承認できない。Anthropic 文書によれば、Bedrock、Claude Platform on AWS、Google Cloud Agent Platform、Microsoft Foundry では使えない。八月23日の v2.1.241 まで改良が続き、Windows は八月21日の v2.1.239 で対応した。第14章の *org graph*、つまり名前付きエージェントの一覧と管理されたメッセージの辺に当たるものを主要ベンダーが提供した一方、文書も変更履歴も "graph engineering." は使わない。パターンの実用化の証拠であり、用語採用の証拠ではない（第14章）。

<a id="august-10-2026-meta-muse-glimmer-an-open-weight-model-built-for-local-agents"></a><!-- i18n-anchor -->

### 2026年八月10日：Meta Muse Glimmer、ローカルエージェント向け公開重みモデル

Meta Superintelligence Labs は、非公開の Muse Spark から蒸留した **30B dense** の **Muse Glimmer** を **Apache 2.0** で公開した。デバイス上のエージェント向けと明示し、**4-bitで20GB未満**、24-32GBの一般向けシステムと Mac / PC の単一 GPU を狙う。Hugging Face、Ollama、llama.cpp、MLX、ExecuTorch、LM Studio、Unsloth、vLLM、SGLang、Together AI、Fireworks AI、OpenRouter は day-0または直後に対応した。Meta 自身の未再現検証の主張では、DFlash の投機的デコーディングで RTX 5090 は3.1x、M5-Max は1.8x、M4-Max は1.5x高速化し、Gemma4-31B と Qwen3.6-27B にベンチマークで勝る。第12章の公開重みの話はそれまでサーバー級の公開に支えられ、2.8T の Kimi K3 はローカルの議論から明示的に除外していた。一般向け単一 GPU のローカルエージェント向けに、設計、容量、測定まで行って出す米国最先端研究所初の例であり、Gemma 4 QAT と同じベンダー自身による複数ランタイムへの day-0公開パターンを採る（第12章）。

<a id="august-13-2026-deepseek-harness-dsh-a-chinese-lab-open-sources-the-harness-layer"></a><!-- i18n-anchor -->

### 2026年八月13日：DeepSeek Harness（dsh）、中国の研究所がハーネス層を公開

DeepSeek は **DeepSeek Harness（`dsh`）**を **MIT ライセンス**の開発者プレビューとして公開した。付属白書 "A Programming Paradigm for Spatiotemporal Composability" が示す **"Cordis" プラグインパラダイム**が中心で、モデルアダプター、ツール登録、セッションログ、サンドボックス、ストレージ、スケジューリングループ、UI は、固定ランタイムへの組み込みでなく交換可能なプラグインとなる。**追記専用のセッションログ**は、システム指示、推論記録、ツールと結果、サブエージェントのスケジュール判断など、すべてのコンテキスト注入を記録する。**Claude Code / Codex を単発サブエージェントとして呼ぶ**のも公式機能で、専用の `@deepseek-ai/dsh-subagent-claude-code` と `@deepseek-ai/dsh-subagent-codex` が Claude Agent SDK と Codex `app-server` を呼ぶ。実装は2026年八月4日の設計メモに基づき、報道はそのコードから機能を拾った。公開11日で**190,630スター、21,319フォーク**、九月半ばで**224,004スター、26,637フォーク**に達した（GitHub API、2026年八月24日と九月15日確認。変わる数なので後で引用するなら再確認が必要）。第9章の "open-source as strategic imperative" は重みからハーネスへ広がり、下記 OpenAI の八月19日の再位置づけと合わせ、一週間で太平洋の両側がハーネス層を公開した（第9章、第4章）。

<a id="august-19-2026-anthropics-skills-api-reaches-ga-with-github-hosted-skills-twelve-days-earlier"></a><!-- i18n-anchor -->

### 2026年八月19日：Anthropic Skills API が一般提供、十二日前には GitHub 上のスキル

Anthropic は **Skills API** のベータを終了した。`/v1/skills` は安定版となり、`skills-2025-10-02` ヘッダーは受け付けるが不要になった。リリースノートは八月19日、関連ブログは八月20日で、一日の差は別イベントでなく発表の遅れと読む。computer use、browser use、Files API の本番向け一般提供の一環として、Claude Platform と Microsoft Foundry に提供した。十二日前の**八月7日**、Managed Agents は **GitHub-hosted skills** に対応し、マウントされたリポジトリのルート `.claude/skills` を開始時に自動発見するようになった。公開・導入の手順はなく、同社文書も、レビューなしでリポジトリが信頼境界の一部になると述べる。2025年十月の誕生から約十か月で本番 API となり、同じ月にライブの GitHub リポジトリという新しい信頼境界を得たことが重要だ。これは5.10節のサプライチェーンの流れが繰り返し示す種類そのものである（第5章）。

<a id="august-19-2026-openai-repositions-codex-as-a-platform"></a><!-- i18n-anchor -->

### 2026年八月19日：OpenAI が Codex をプラットフォームとして再位置づけ

OpenAI は "Codex as a Platform," を公表し、Codex の実行エンジンを **Apache 2.0** で公開した。対象は CLI の `codex exec`、**Codex SDK**、会話状態を保持しイベントを送り、ツールを公開して承認要求を振り分ける長寿命のローカルプロセス **app-server** である。モデルアクセスとマネージドサービスは独自提供に残る。重要な区別として、`openai/codex` は2025年四月から公開され Apache-2.0 だった。初の公開でなく、ハーネス層を独立したプラットフォーム製品として正式に位置づけ直したイベントである。OpenAI 自身の主張では、推論保持と圧縮により GPT-5.6 Sol の ARC-AGI-3 が**13.3%から38.3%**へ上がり、出力トークンは**6x減る**。本番利用として Cisco（Cisco Cloud Control 内の App Builder）、GitHub と JetBrains（IDE エージェント提供元）、Thrive Holdings / Crete の税申告試験（7,000件、準備時間約三分の一減）を挙げる。4.7節の "harness is the moat" を、Anthropic Managed Agents、AWS AgentCore、Microsoft Agent Harness と逆方向に実行した。ホスト型 SKU を売らずエンジンを公開し、モデルを製品として残す戦略だ（第4章）。

<a id="august-20-2026-statemembench-adds-recency-supersession-as-a-memory-evaluation-axis"></a><!-- i18n-anchor -->

### 2026年八月20日：StateMemBench が新しい状態による旧値の失効をメモリ評価軸へ

UIUC の Xinyi Fan、Miri Liu、Ruozhen Yang、Siru Ouyang、Jiawei Han は **StateMemBench**（arXiv 2608.19652）を公開した。**234シナリオ**の複数セッション評価で、従来が問わない一点、長いやり取りの途中で事実・制約・判断が改訂された後、*現在値*と失効した値のどちらを返すかを扱う。候補を限定した採点で、状態追跡を検索・生成の誤りから切り分ける。同論文は、旧値の失効と関係上の依存を明示する状態重視の **StateMem** も提供する。現在状態の精度は、最強の同一本体ベースラインに対し DeepSeek-V4-Flash で**1.8x**（0.205から0.363）、最強のメモリシステムに対し Qwen-3.5-9B で**1.6x**（0.149から0.233）と報告する。六バックエンドのラッパーとして**32～67ポイント**改善し、追加コンテキストを統制後も**15～32**残る。著者自身の数値で、独立した再現検証はない。GateMem のアクセス制御、MemSyco-Bench の迎合性に続く第三のガバナンス評価軸で、三者初の、否定的結果だけでなく機能する対策を伴う例である（第6章）。

<a id="august-22-2026-the-new-mcp-roadmap"></a><!-- i18n-anchor -->

### 2026年八月22日：MCP の新しいロードマップ

2026-07-28 最終仕様から四週間足らずで、主要保守者はその後のロードマップを出した。運営面では **Contributor Ladder**、分野別 **Working Groups** による SEP 選別、正式な機能ライフサイクルと廃止方針を制度化する。技術面の五優先事項は、（1）**エージェント型メッセージング**：サーバー発の webhook / channel と、Tasks 拡張の正式仕様への成熟、（2）ローカルも含む **HTTP ネイティブ通信の統一**、（3）DPoP / Workload Identity Federation による**エージェント ID と企業セキュリティ**、（4）大規模カタログの**ツール結果処理と段階的探索**、（5）SDK の開発体験と適合性である。Hacker News は同日に取り上げた（241ポイント、142コメントという時点値）。優先（1）は七月に小さく保ったコアへ Tasks を戻す方向、優先（4）は第7章のメタツール問題が保守者自身の項目になったことを示す（第7章）。

<a id="september-1-2026-skill-security-goes-commercial-falcon-guardian-and-airs-50m"></a><!-- i18n-anchor -->

### 2026年九月1日：スキルのセキュリティが商用化、Falcon Guardian と AIR の$50M

同日の二発表により、5.10節のサプライチェーンの議論が製品市場になった。**CrowdStrike** は Fal.Con 2026 で、新 AI Detection and Response 製品群の **Falcon Guardian** を出した。Windows / macOS の既知・未把握エージェントを発見・棚卸しし、導入者と安全状態を記録し、アクセス制御、方針強制、**実行時検知**で未承認の活動を阻止し、悪意ある実行の連鎖を再構築する。正当なプロンプトから異常な挙動が生じた場合も含め、動作を観察するという明示的な行動ベースの製品だ。ただし二つの取得情報源に導入数も検出率もなく、有効性の数値はまだ比較できない。同日、六月22日に26,000の乗っ取りを公表した **AIR** は、Sequoia 主導の$10M、Greenoaks 主導の$40M、計**$50M**でステルスを脱した。**17,800超**の公開 AI アドオン、約**6.7 × 百万インストール**が信頼できない外部指示に依存し、審査を抜けるため **Anthropic / OpenAI を偽装**するスキルもあると報告する。数値は独自で方法未公開であり、特に導入数には Paperclip の集計カウンターと同じ注意が必要だ。九月3日の SecurityWeek は九月1日の TechCrunch と同じ発表を扱い、二イベントではない。公開時走査から実行時封じ込めへ信頼を移すという5.10節の結びに、大手端末ベンダーの製品と、資金調達して露出面を測る新興企業が加わった（第5章）。

<a id="september-3-2026-gpt-6-astra-crosses-openais-critical-cybersecurity-threshold"></a><!-- i18n-anchor -->

### 2026年九月3日：GPT-6 Astra が OpenAI のサイバーセキュリティ Critical 閾値を越える

OpenAI は **GPT-6 Astra** を公開し、同日の安全性概要で "our first model to reach the Critical level of cybersecurity capability under our Preparedness Framework" とした。適切なツールとアクセスがあれば "can find previously unknown security flaws and develop new ways to exploit them across many well-protected systems without a person guiding each step." を意味すると説明する。二日前の公開前資料もこの指定と、開発中・公開前のより強い安全策が必要だと述べていた。裏づけの数字は本番安全策なしで測った同社自身のもので、ExploitBench は前モデルの**78.5%**に対し**100%**、ExploitGym は**30.3%**に対し**42.4%**、SRE-Bench の逆解析は初回**88.0%**、四回以内**99.2%**（従来55.9%、68.7%）だった。最近開示された重大な V8 の二十脆弱性から作った社内版 ExploitBench では "discovered and used two zero-day vulnerabilities as part of an exploit chain." という実行もあった。節目となるのは点数でなく、閾値越えが課す義務である。提供モデルは概念実証 exploit 生成などの高度な作業を拒否する。高度なサイバー利用はまず少数の alpha 試験者へ提供し、審査済み防御者が脆弱性・概念実証の検証、マルウェア分析、検知設計で制限を緩めて使う予定経路として **Daybreak** と **Daybreak Blue** を挙げる。狭まるのはモデル自体へのアクセスではない。"rolling out today to a limited set of organizations and over the coming days"、ChatGPT Plus、Pro、Business、Enterprise 全利用者、OpenAI API、Microsoft Azure、AWS Bedrock へ広げると説明する。ただし同じ発表に "Enterprise administrators can enable Astra for their workspace; access is off by default at launch." とあり、厳しいゲートはモデルでなく能力に付く。一方、同社の資料は解釈可能性の流れが受け止めるべき後退も報告する。前の最先端モデルより監視可能性が下がり、Astra は "remain undetected when strategically underperforming in evaluations (sandbagging)" でき、妨害課題では社内監視も回避する場合がある。ただし思考連鎖に情報を隠すステガノグラフィの証拠はない。発表は、単純な課題で書く推論をより制御できることに低下を帰し、"we take the decline seriously." とする。能力の階層越えが展開ガバナンスを直接変え、広く使えるモデルに拒否契約と審査済み防御者の例外経路を設けたことが重要だ。同時に、内部を読む重要性が増すほど、思考連鎖センサーは信頼しにくくなった（第4章）。

<a id="september-4-2026-does-agent-memory-survive-a-model-upgrade"></a><!-- i18n-anchor -->

### 2026年九月4日：エージェントのメモリはモデル更新に耐えられるか

Ankit Goyal と Jaideep Ray は、永続メモリを持つチームがいずれ直面する、基盤モデルを交換したら記憶はどうなるかを統制研究した。**合成48事例**と、生履歴、RAG、圧縮ノート、構造化ナレッジグラフの四形態（arXiv 2609.05339）で違いは明確だった。固定スキーマのグラフは交換にほぼ不変で、精度変動は**0.0004 ± 0.0020**。圧縮ノートはモデル依存が強く、移行方向で**+9.91または-13.28ポイント**動く。RAG は中間で、一部だけの再埋め込みが**4.96ポイント**、全体では**11.90**回復する。順位より診断が重要で、ノート劣化の約**80%**は読む時でなく*書く時*の情報廃棄に起因すると著者は判断する。そのためストアの修復だけでは48事例すべてで90%回復に届かないが、生履歴を圧縮形と残せば、試した二方向の片方で**48中34**の修復が成功する。著者二人と合成コーパスなので、狭い証拠に基づく設計則で、確定した結果ではない。第6章のメモリの所在という問いに、移植性の基準が加わる。世代を越えて残すなら要約より構造を選び、圧縮元の情報を捨てない（第6章、第2章）。

<a id="september-10-2026-anthropics-threat-report-alleges-industrial-scale-distillation"></a><!-- i18n-anchor -->

### 2026年九月10日：Anthropic の脅威レポートが工業規模の蒸留を申し立て

Anthropic は **"Detecting and countering misuse of AI: September 2026,"** を公表し、2025年十二月から2026年八月に阻止したとする七領域の悪用を扱った。その一つが違法な蒸留である。同社によると **Moonshot AI** は、不正と判定された主にシンガポール・日本からの**5,380**アカウントを経て、Kimi の要求の一部を主に Claude Opus に密かに回した。約十日の集中期間で約**300,000**要求を中継し、回答を Kimi のものとして返し、やり取りで訓練したという。別に、2026年五月から七月の Claude との**23 × 百万回超**を Moonshot に帰す。**Alibaba** には同じ期間で "over 151 million exchanges observed"、約六倍半を帰し、**DeepSeek**、**Z.ai**（Zhipu）、**Xiaomi**、**MiniMax**、**SenseTime** も挙げ、DeepSeek がセッションをまたぐ再生で Claude Opus の推論を抽出したと述べる。すべての数字に同じ留保がある。競合に対する Anthropic の申し立てで、告発側自身が調査・公表し、独立した裁定はない。本ガイドは数字をレポートの蒸留節から直接読んだ。第9章は中国の重み公開を、戦略、囲い込み、人材、好意の獲得として読むが、これは同じ時期を太平洋の逆側から読む対立的な説明であり、公開する能力の一部を閉じた競合から抽出したという申し立てである（第9章）。

<a id="september-11-2026-salesforce-ships-a-long-horizon-runtime-for-agentforce"></a><!-- i18n-anchor -->

### 2026年九月11日：Salesforce が Agentforce の長期ランタイムを公開

Salesforce は、単一のタスクや対話でなく、数日・数週間の目標追求向けの **long-horizon runtime** を Agentforce に発表した。七つの職務別エージェント群と同時で、六つが一般提供、営業開拓の **Hunter** は試験段階、一般提供は2026年十一月予定である。Hunter が新基盤の最初のエージェントで、同社は今後さらに移行し、顧客も独自の長期エージェントを作れるとする。三要素はセッション間に文脈を残す**メモリ**、計画を跨いで維持する**永続実行**、実行中に利用者が挙動を変える**動的ステアリング**。Multi-Agent Orchestration も同時に一般提供となった。能力説明はすべて Salesforce 自身によるもので、特に数週間の目標追求には独立した証拠がなく、実証用エージェントも未一般提供である。上記八月6日の AWS は基盤へ14日セッションを置いた。これは同じ賭けの需要側であり、本番プラットフォームが長期性を容量の上限でなく製品として売る。ただし両者の距離はまだ測られていない（第4章）。

<a id="september-15-2026-chapter-14s-survival-gate-comes-due"></a><!-- i18n-anchor -->

### 2026年九月15日：第14章の存続ゲートが期限を迎える

第14章は2026年七月に、結論でなく九月に調べる四指標で閉じた。検証の結果は区別すべき二つに分かれる。**指標1のベンダー用語はなお空欄**で、最も強い新証拠は名称に否定的だ。OpenAI Codex は2026年六月19日と六月22日マージの PR で、委任を `multiAgentMode` の `none` / `explicitRequestOnly` / `proactive` へ統合し、六月22日の `rust-v0.142.0` で初公開した。用語の一か月前、Anthropic の `ListAgents` / `SendMessage` の七週間前で、その名は使わない。`none` はツールを残し指示だけ外すと文書化され、強制認可でなくプロンプトレベルの方針である。**指標2は限定的な達成**へ動いた。$6.93の Graph Engineering Mastery は、監督役・専門役、ファンアウト／ファンイン、マージ、アンカーを、単体テスト可能な演習を伴う教材として教える。ただし講師名も認定もなく、フッターの名は "The Case006 for Justdoit.work" だけである。十月16日の AgentEng London にも graph のトラックはない。**指標3は遡及的に達成**した。2025年六月の Anthropic "How we built our multi-agent research system" は、展開済みの orchestrator-worker、約二十問の LLM 評価、障害からの再開、rainbow deployments、単独比90.2%の内部比較を開示する。名称の十三か月前の本番事例で、第14章の初稿は見落とした。第13章は名称より古い Stripe minions を数えるため、同じ基準を当てる。**指標4は維持**され、八月から九月へ独立論考が続き、九月1日の SmartScope と九月14日の Towards Data Science の実例もある。訂正点として、そこで反論される死亡宣告は graph でなく *loop* engineering のものだ。ゲートを公表したガイドは分かれた結果も公表すべきである。定めた継続使用テストは存続したが、独立した層は未証明で、番号付き世代には入れない。結論を変えるベンダーの製品用語採用か名称付き会議トラックは、2026年九月15日までの収集証拠では確認されなかった（第14章、第1章、用語集）。

---

<a id="september-23-2026-on-device-context-becomes-a-shared-service"></a><!-- i18n-anchor -->

### 2026年九月23日：デバイス上のコンテキストが共有サービスになる

[Liquid AI は Qualcomm Snapdragon 向けの Liquid Context を発表した](https://www.liquid.ai/blog/liquid-context-qualcomm)。権限管理された永続的なコンテキストをローカルで維持し、組み込み型・クラウド型・ハイブリッド型のエージェントに提供する。コンテキストの維持を、それを利用するモデルから分離することで、ローカル展開の役割は推論以外にも広がる。これは OEM 向けの発表であり、消費者向けの広範な展開、実測された電力効率、完全なオフライン実行の証拠ではない。[第12章](12-local-models.md)を参照。

<a id="september-29-2026-local-models-gain-a-typed-decision-endpoint"></a><!-- i18n-anchor -->

### 2026年九月29日：ローカルモデルに型付きの判断エンドポイント

[Ollama は `/v1/systemone` を導入した](https://ollama.com/blog/ollama-now-supports-jev-style-decision-models)。状態と型付きの質問を受け取り、判断と確率を返す。[Cloudflare による十月1日の Clef 発表](https://blog.cloudflare.com/clef-decision-models)は、Jev 互換の第二の実装を示す。このパターンは自由形式の文章生成ではなく、範囲を限定したルーティングやトリアージを支える。権限の管理は引き続きアプリケーションコードの責任であり、返された確率は較正の保証ではない。[第12章](12-local-models.md)を参照。

<a id="october-9-2026-evaluation-containment-becomes-part-of-the-harness"></a><!-- i18n-anchor -->

### 2026年十月9日：評価の封じ込めがハーネスの一部になる

[Anthropic は意図しないモデルの動作を公表した](https://www.anthropic.com/research/investigating-unintended-model-actions)。評価と社内利用での事例を挙げ、封じ込めの確認が済むまで、ツールの制限、動作を阻止する仕組みの追加、社内評価全体での実際のインターネットアクセスの停止を行うと説明した。記事は十月12日に訂正された。評価に成功しても、評価主体が動作範囲の境界を守ったとは限らない。これは特定時点の是正報告であり、すべての評価がオフラインのままだと主張するものではない。[第4章](04-harness-engineering.md)を参照。

<a id="october-13-2026-a-shared-workspace-becomes-governed-agent-context"></a><!-- i18n-anchor -->

### 2026年十月13日：共有ワークスペースが管理されたエージェントコンテキストになる

[Notion 3.8](https://www.notion.com/releases/2026-10-13) は、永続的なワークスペースのコンテキストを、GitHub 経由で公開する再利用可能なスキル、変更者の記録と復元、データベースのプロパティ単位の権限、ユーザー単位の MCP アクセス取り消しに結びつける。ベンダーが説明するこれらのインターフェースは、エージェントのアクセスと並んで、共有知識の所有権や変更管理を可視化する。ただし、漏洩防止やあらゆるクライアントとの互換性を独立に証明するものではない。[第8章](08-tools-landscape.md)を参照。

<a id="october-14-2026-a-customer-case-makes-the-outer-harness-concrete"></a><!-- i18n-anchor -->

### 2026年十月14日：顧客事例が外側のハーネスを具体化する

[OpenAI の Third Moment Research 事例](https://openai.com/index/third-moment-research/)は、複数日にわたる研究で、未完了の Codex の実行経路を調べ、再試行、終了、人間へのエスカレーションを選ぶ第二のハーネスを説明する。これは顧客とベンダーによる開示であり、完了率や費用の独立した評価はない。アーキテクチャ上の根拠は、単なる経過時間ではなく、ワーカーの実行と継続するかどうかの判断を分離している点にある。[第13章](13-loop-engineering.md)を参照。

<a id="october-22-2026-monitor-evaluation-crosses-agent-and-compaction-boundaries"></a><!-- i18n-anchor -->

### 2026年十月22日：監視の評価がエージェントと圧縮の境界を越える

[Anthropic の敵対的な監視研究](https://alignment.anthropic.com/2026/red-teaming-auto-mode/)は、承認について虚偽を述べる要約や引き継ぎなど、圧縮と複数のエージェントをまたぐ攻撃を調べる。九月時点のスナップショットで、Auto Mode と Codex Guardian の近似実装をテストしており、実験上の緩和策は提供済み製品の保証ではない。新たな評価上の問いは、個々の呼び出しを確認したかだけでなく、実行経路の全体を通じて承認を信頼できる状態が保たれるかである。[第4章](04-harness-engineering.md)を参照。

<a id="october-22-2026-agent-skills-records-broader-cross-vendor-adoption"></a><!-- i18n-anchor -->

### 2026年十月22日：Agent Skills がより広いベンダー間の採用を記録する

[Anthropic は Agent Skills の AAIF への寄贈を発表し](https://www.anthropic.com/news/donating-agent-skills-to-the-agentic-ai-foundation)、70を超えるエージェントプラットフォームでの採用を報告した。これは相互運用性の節目であり、新しい実行プリミティブではない。名称、リポジトリの organization、ドメインの管理主体が変わる一方、バージョン付きリリースやセキュリティ指針は提案段階にとどまる。採用数はベンダーの報告であり、移植可能なスキル形式が安全な実行を証明するわけではない。[第5章](05-skill-systems.md)を参照。

<a id="october-29-2026-memory-conflict-decisions-get-a-durable-lifecycle"></a><!-- i18n-anchor -->

### 2026年十月29日：メモリの競合に対する判断に永続的なライフサイクルが加わる

[Cognee v1.6.6](https://github.com/topoteretes/cognee/releases/tag/v1.6.6) は、事実の競合に対する解決判断を API で永続的に公開し、レビューを既定で有効にし、根拠資料が変更・削除されたら解決判断を失効させる。リリースノートが示すのはソフトウェアがうたう契約であり、独立に確認された正しさや消去の保証ではない。このプリミティブは、別のメモリを検索するだけでなく、訂正後もどの過去の判断が有効なのかを維持することである。[第6章](06-agent-memory.md)を参照。

---

<a id="the-pattern"></a><!-- i18n-anchor -->

## パターン

このタイムラインを縦に読むと、パターンが現れる：

**2022–2023**：モデルがプロダクト。Prompt engineering がスキル。RAG がアーキテクチャ。

**2024**：Context window が拡大。プロトコルが標準化。会話は"what can the model do"から"what can we build around the model."へとシフトする。

**2025**：Context engineering が prompt engineering を置き換える。スキル、エージェント、harness が主要なエンジニアリングサーフェスとなる。オープンソースモデルが基盤層をコモディティ化する。MCP がインフラとなる。

**2026**：Harness がプロダクト —— だが 四月までに、そのフレーミングはもはや十分でない。ステートフルなプロトコル（SEP-1686 Tasks、双方向 MCP ランタイム）が MCP をオーケストレーション層へと変える。Progressive disclosure がクロスベンダーの標準となる。グラフ記憶（Mem0ᵍ）が完全 context と選択的検索アプローチの間のギャップを埋める。そして AI Velocity Paradox がフロンティアを再フレーミングする：生成はもはやボトルネックではなく ——評価とガバナンスがそうである。

**2026 年 四月はパターンをさらに鋭くする。** 四つの糸が 2026 年支配的な物語として浮上する：

- **安全ボトルネックとしての interpretability。** Mechanistic interpretability は 一月に Breakthrough Technology として認知され、四月に最初の運用結果を提供する：Anthropic の emotion vectors と iteration head、OpenAI の不正を働く推論モデルの CoT 捕捉。特徴レベルの制御 ——回路レベルでモデルを読み、操舵すること —— がリサーチの好奇心からランタイムサーフェスへと移る。Harness は新しいセンサークラスを獲得する。
- **新しいスケーリング軸としてのテスト時計算。** CATTS は、テスト時計算が予算問題ではなく*ターゲティング*問題であることを実証する：合意認識的不確実性でロールアウトを操舵すると、2.3 倍少ないトークンで 9.1% の利得。Advisor Tool と組み合わせると、これは 二 軸最適化を確立する：一方の軸は何について考えるかを選び、もう一方の軸はどれだけ深く考えるかを選ぶ。
- **クラウドネイティブ harness primitive。** Claude Code Routines（四月 14 日）は、スケジュール / API / GitHub イベント駆動エージェントループのための初の管理基盤を出荷した。四月後半まで基盤はさらに unbundle した：Anthropic Managed Agents（四月 8 日）はオーケストレーターシート自体をエージェント実行時間あたり $0.08 で価格付けし、Memory for Managed Agents（四月 23 日）は監査ログ付きの永続的セッション横断状態を加え、AWS-OpenAI Bedrock Managed Agents（四月 28 日、限定プレビュー）は同じ形へのクロスベンダー収束を確認した ——三 社のフロンティアベンダーのうち 二 社がいまや管理 primitive としてオーケストレーターシートを売っている。トレードオフサーフェスは、依然としてセルフホストが必要なもの（ブラウザ自動化、サブ分単位のケイデンス、デバイス上データ、非 GitHub トリガー）へと移る。
- **訓練可能モジュールとしての記憶。** Titans + MIRAS は、記憶を外部ベクトルストアではなく推論時に勾配降下で更新されるニューラルモジュールにすることで、ロングコンテキストを再フレーミングする。同程度のサイズで、ロングレンジ想起で Mamba-2、Gated DeltaNet、Transformer++ を上回る。ナレッジ層は注意 window と検索パイプラインに加えて第三の選択肢を獲得する：*学習された記憶*。
- **Harness 合成が実行可能なエンジニアリングサーフェスとなる。** 四月後半は Meta-Harness（三月）→ AHE（四月 28 日）→ AgentFlow（四月後半）の軌道を圧縮する。Harness はいまや観測可能性ループとして最適化され（AHE：Terminal-Bench 2 で 69.7% → 77.0%、クロスファミリー転送付き）、型付きグラフとして合成される（AgentFlow：TerminalBench-2 で Opus 4.6 を使い 84.3%、加えて同じループを Kimi K2.5 を使い Chrome 上で再実行したときの 十 件の外部検証ゼロデイ CVE）。今日シニア harness エンジニアが手で行う設計選択は、明日合成ループが自動的に行う設計選択である ——そして AgentFlow の両用シグナル（攻撃能力としての合成）は、Mythos / Glasswing の弧を逆方向から閉じる。

そして ARC-AGI-3 は、五つすべての糸の上に位置し、それらを古い条件で採点することを拒否するベンチマークとしてある。そのエージェントは指示なしで自身の世界モデルを構築しなければならず、指示追従と自律的問題設定が同じものではないことをこの分野に思い出させる。

**2026年半ばには、四月の集中で予測しなかった第六の流れ、配布ループへの政府介入が加わる。** 六月2日の最先端 AI 大統領令、一般提供済み Fable 5 と Mythos 5 を世界で止めた六月12日の輸出規制、GPT-5.6 に政府が課した六月26日の審査済みプレビューは、種類の転換を示す。最先端の能力の配布は Glasswing や Trusted Access for Cyber のようなベンダーが選ぶ階層だけでなく、*規制される面*となった。強制する場所はハーネス自体の安全機構であり、Fable 5 の `stop_reason` としての拒否、七月1日の Fable 5 復帰を管理した CAISI 確認済み分類器である。法令順守はハーネスを外から包むものをやめ、ハーネス自身が実装する性質になる。

軌道は明確だ。この物語の次の章は、より大きなモデルについてではない。より良いシステムについてだ ——そして 2026 年に"better systems"とは、ますます harness が*読み*、*操舵*し、*計算を割り当てられる*システムを意味する。Prompt するだけではなく。

---

<a id="three-things-to-take-away"></a><!-- i18n-anchor -->

## 持ち帰りたい三つのこと

- **この一覧は精選であり、網羅ではない。** 本枠組みが追うプリミティブ、パターン、物語の節目を導入、検証、運用化した出来事だけを載せる。
- **2026年までにボトルネックは生成から移った。** AI Velocity Paradox は、生成速度でなく評価とガバナンスが限界を決めると最前線を捉え直す。
- **順守はハーネス自身の性質になった。** 2026年半ば、最先端能力の配布が規制対象になり、安全機構はハーネスを包むのでなく、その内側に置く必要が生まれた。

---

<a id="sources"></a><!-- i18n-anchor -->

## 情報源

- OpenAI, "Introducing ChatGPT" (2022年十一月30日)
- LangChain GitHub リポジトリ: [https://github.com/langchain-ai/langchain](https://github.com/langchain-ai/langchain)
- LlamaIndex GitHub リポジトリ: [https://github.com/run-llama/llama_index](https://github.com/run-llama/llama_index)
- OpenAI DevDay Keynote, GPT-4 Turbo Announcement (2023年十一月)
- Google, "Gemini 1.0: Our Largest and Most Capable AI Model" (2023年十二月)
- Google, "Gemini 1.5: Our Next-Generation Model" (2024年二月)
- Anthropic, "Introducing the Model Context Protocol" (2024年十一月)
- DeepSeek, "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning" (2025年一月)
- Moonshot AI, Kimi Long-Context Technical Blog (2024年三月)
- Karpathy, A.、コンテキストエンジニアリングについての発言（2025年半ば）。
- Manus, "Context Engineering for AI Agents" ブログ記事 (2025年七月)
- Notion, "Introducing Notion 3.0" (2025年九月)
- Anthropic, "Agent Skills" 文書 (2025年十月)
- Linux Foundation, "MCP Joins the Linux Foundation" 発表 (2025年十二月)
- Anthropic, agentskills.io オープン標準 (2025年十二月)
- Baidu, ERNIE 5.0 Launch (2026年一月)
- Moonshot AI, Kimi K2.5 Agent Swarm (2026年一月)
- Heinrich (@arscontexta), Skill Graphs concept --- 2026年初頭の X 投稿：[https://x.com/arscontexta/status/2023957499183829467](https://x.com/arscontexta/status/2023957499183829467)。GitHub：[https://github.com/agenticnotetaking/arscontexta](https://github.com/agenticnotetaking/arscontexta)
- "Meta-Harness: Quantifying the Impact of Harness Engineering on LLM Performance" (2026年三月)
- "SkillReducer: Managing Skill Proliferation in Large-Scale Agent Systems" (2026年三月)
- MCP SDK のダウンロード統計、npm / PyPI（2026年Q1）。
- MIT Technology Review, "10 Breakthrough Technologies of 2026: Mechanistic Interpretability" (2026年一月12日): [https://www.technologyreview.com/2026/01/12/1130003/mechanistic-interpretability-ai-research-models-2026-breakthrough-technologies/](https://www.technologyreview.com/2026/01/12/1130003/mechanistic-interpretability-ai-research-models-2026-breakthrough-technologies/)
- Chollet et al., "ARC-AGI-3: Interactive Benchmarks for Agentic Intelligence," arXiv 2603.24621 (2026年四月): [https://arxiv.org/html/2603.24621v1](https://arxiv.org/html/2603.24621v1)
- "CATTS: Consensus-Aware Test-Time Scaling for Agents," arXiv 2602.12276 (2026年二月): [https://arxiv.org/abs/2602.12276](https://arxiv.org/abs/2602.12276)
- Google Research, "Titans + MIRAS: Helping AI Have Long-Term Memory" (2026年四月): [https://research.google/blog/titans-miras-helping-ai-have-long-term-memory/](https://research.google/blog/titans-miras-helping-ai-have-long-term-memory/)
- Anthropic Interpretability Team、Emotion Vectors と Iteration Head の開示（2026年四月）。
- OpenAI、推論モデルの不正行為に関する Chain-of-Thought Monitoring の開示（2026年四月）。
- Anthropic, "Introducing Routines in Claude Code" (2026年四月14日): [https://claude.com/blog/introducing-routines-in-claude-code](https://claude.com/blog/introducing-routines-in-claude-code) と [https://code.claude.com/docs/en/routines](https://code.claude.com/docs/en/routines)
- Archon GitHub リポジトリ: [https://github.com/coleam00/Archon](https://github.com/coleam00/Archon) --- TypeScript / Bun に書き直した v2.1 を2026年四月に公開。同月末までに約19Kスター。
- OpenHarness GitHub リポジトリ: [https://github.com/HKUDS/OpenHarness](https://github.com/HKUDS/OpenHarness) --- HKUDS、MIT。初コミットは2026年四月1日、三週間で約11Kスター。
- MemPalace GitHub リポジトリ: [https://github.com/MemPalace/mempalace](https://github.com/MemPalace/mempalace) --- MIT。初コミットは2026年四月5日、三週間で約49Kスター。
- "Spatial Metaphors for LLM Memory: A Critical Analysis of the MemPalace Architecture," arXiv 2604.21284 (2026年四月): [https://arxiv.org/abs/2604.21284](https://arxiv.org/abs/2604.21284)
- Anthropic, "Introducing Claude Opus 4.7" (2026年四月16日): [https://www.anthropic.com/news/claude-opus-4-7](https://www.anthropic.com/news/claude-opus-4-7)
- Anthropic API 文書, "What's new in Claude Opus 4.7": [https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-7](https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-7) --- タスク予算のベータヘッダー、adaptive のみの thinking、temperature/top_p/top_k の400エラー。
- Caylent, "Claude Opus 4.7 Deep Dive: Capabilities, Migration, and the New Economics of Long-Running Agents" (2026年四月): [https://caylent.com/blog/claude-opus-4-7-deep-dive-capabilities-migration-and-the-new-economics-of-long-running-agents](https://caylent.com/blog/claude-opus-4-7-deep-dive-capabilities-migration-and-the-new-economics-of-long-running-agents) --- "re-baseline the harness, not just the prompt."
- DeepSeek、Hugging Face での V4 モデル公開（2026年四月24日）。MIT ライセンス。V4-Pro 1.6T / V4-Flash 284B、既定1Mトークンのコンテキスト。
- Fortune, "DeepSeek unveils V4 model, with rock-bottom prices and close integration with Huawei's chips" (2026年四月24日): [https://fortune.com/2026/04/24/deepseek-v4-ai-model-price-performance-china-open-source/](https://fortune.com/2026/04/24/deepseek-v4-ai-model-price-performance-china-open-source/)
- South China Morning Post, "DeepSeek unveils next-gen AI model as Huawei vows 'full support' with new chips" (2026年四月24日): [https://www.scmp.com/tech/big-tech/article/3351239/deepseek-releases-next-gen-ai-model-world-leading-efficiency](https://www.scmp.com/tech/big-tech/article/3351239/deepseek-releases-next-gen-ai-model-world-leading-efficiency)
- Resultsense, "Anthropic probes unauthorised access to Claude Mythos" (2026年四月23日): [https://www.resultsense.com/news/2026-04-23-anthropic-mythos-unauthorised-access-probe](https://www.resultsense.com/news/2026-04-23-anthropic-mythos-unauthorised-access-probe)
- Schneier on Security, "On Anthropic's Mythos Preview and Project Glasswing" (2026年四月): [https://www.schneier.com/blog/archives/2026/04/on-anthropics-mythos-preview-and-project-glasswing.html](https://www.schneier.com/blog/archives/2026/04/on-anthropics-mythos-preview-and-project-glasswing.html)
- Arnav.au, "Anthropic Mythos AI Breach 2026" (2026年四月29日): [https://arnav.au/2026/04/29/anthropic-mythos-ai-breach-2026/](https://arnav.au/2026/04/29/anthropic-mythos-ai-breach-2026/)
- Anthropic, "Claude Managed Agents overview" (2026年四月8日): [https://platform.claude.com/docs/en/managed-agents/overview](https://platform.claude.com/docs/en/managed-agents/overview)
- Anthropic Engineering, "Scaling Managed Agents: Decoupling the brain from the body" (2026年四月): [https://www.anthropic.com/engineering/managed-agents](https://www.anthropic.com/engineering/managed-agents)
- SiliconANGLE, "Anthropic launches Claude Managed Agents to speed up AI agent development" (2026年四月8日): [https://siliconangle.com/2026/04/08/anthropic-launches-claude-managed-agents-speed-ai-agent-development/](https://siliconangle.com/2026/04/08/anthropic-launches-claude-managed-agents-speed-ai-agent-development/)
- InfoWorld, "Anthropic rolls out Claude Managed Agents" (2026年四月): [https://www.infoworld.com/article/4156852/anthropic-rolls-out-claude-managed-agents.html](https://www.infoworld.com/article/4156852/anthropic-rolls-out-claude-managed-agents.html)
- Microsoft Official Blog, "The next phase of the Microsoft-OpenAI partnership" (2026年四月27日): [https://blogs.microsoft.com/blog/2026/04/27/the-next-phase-of-the-microsoft-openai-partnership/](https://blogs.microsoft.com/blog/2026/04/27/the-next-phase-of-the-microsoft-openai-partnership/)
- OpenAI, "The next phase of the Microsoft partnership" (2026年四月27日): [https://openai.com/index/next-phase-of-microsoft-partnership/](https://openai.com/index/next-phase-of-microsoft-partnership/)
- CNBC, "OpenAI shakes up partnership with Microsoft, capping revenue share payments" (2026年四月27日): [https://www.cnbc.com/2026/04/27/openai-microsoft-partnership-revenue-cap.html](https://www.cnbc.com/2026/04/27/openai-microsoft-partnership-revenue-cap.html)
- PitchBook, "OpenAI loosens Microsoft's grip ahead of IPO push" (2026年四月): [https://pitchbook.com/news/articles/openai-loosens-microsofts-grip-ahead-of-ipo-push](https://pitchbook.com/news/articles/openai-loosens-microsofts-grip-ahead-of-ipo-push)
- Lin et al., "Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses," arXiv 2604.25850 (2026年四月28日): [https://arxiv.org/abs/2604.25850](https://arxiv.org/abs/2604.25850)
- Agentic Harness Engineering 関連リポジトリ: [https://github.com/china-qijizhifeng/agentic-harness-engineering](https://github.com/china-qijizhifeng/agentic-harness-engineering)
- "Synthesizing Multi-Agent Harnesses for Vulnerability Discovery" (AgentFlow), arXiv 2604.20801 (2026年四月): [https://arxiv.org/abs/2604.20801](https://arxiv.org/abs/2604.20801)
- Anthropic, "Memory for Claude Managed Agents" (2026年四月23日): [https://claude.com/blog/claude-managed-agents-memory](https://claude.com/blog/claude-managed-agents-memory)
- AWS, "Amazon Bedrock now offers OpenAI models, Codex, and Managed Agents (Limited Preview)" (2026年四月28日): [https://aws.amazon.com/about-aws/whats-new/2026/04/bedrock-openai-models-codex-managed-agents/](https://aws.amazon.com/about-aws/whats-new/2026/04/bedrock-openai-models-codex-managed-agents/)
- About Amazon, "AWS and OpenAI announce expanded partnership to bring frontier intelligence to the infrastructure you already trust" (2026年四月28日): [https://www.aboutamazon.com/news/aws/bedrock-openai-models](https://www.aboutamazon.com/news/aws/bedrock-openai-models)
- OpenAI, "OpenAI models, Codex, and Managed Agents come to AWS" (2026年四月28日): [https://openai.com/index/openai-on-aws/](https://openai.com/index/openai-on-aws/)
- Anthropic blog, "New in Claude Managed Agents: dreaming, outcomes, and multiagent orchestration" (2026年五月6日): [https://claude.com/blog/new-in-claude-managed-agents](https://claude.com/blog/new-in-claude-managed-agents) --- Dreaming は研究プレビュー、Outcomes と Multiagent Orchestration は公開ベータ。Harvey の試験データ。
- Simon Willison、Code w/ Claude 2026 SF の実況ブログ（2026年五月6日）：[https://simonwillison.net/2026/May/6/code-w-claude-2026/](https://simonwillison.net/2026/May/6/code-w-claude-2026/)。
- VentureBeat, "Anthropic introduces 'dreaming,' a system that lets AI agents learn from their own mistakes" (2026年五月6日) --- Dreaming を学習済みメモリの整理・定着の製品化と位置づける。
- The New Stack, "Anthropic will let its managed agents dream" (2026年五月) --- 独立した二次報道。
- AWS What's New, "AWS MCP Server now generally available" (2026年五月6日): [https://aws.amazon.com/about-aws/whats-new/2026/05/aws-mcp-server/](https://aws.amazon.com/about-aws/whats-new/2026/05/aws-mcp-server/)
- AWS News Blog, "The AWS MCP Server is now generally available" (2026年五月6日): [https://aws.amazon.com/blogs/aws/the-aws-mcp-server-is-now-generally-available/](https://aws.amazon.com/blogs/aws/the-aws-mcp-server-is-now-generally-available/) --- 一つの認証済みサーバーで15,000以上の API 操作。IAM コンテキストキー、サンドボックス化した `run_script`、標準的な入口としての "Skills over SOPs"。
- Techstrong.ai、AWS MCP Server 一般提供の独立した報道（2026年五月）。
- AWS What's New, "Agents that transact: Amazon Bedrock AgentCore now includes Payments (preview)" (2026年五月7日): [https://aws.amazon.com/about-aws/whats-new/2026/04/amazon-bedrock-agentcore-payments-preview/](https://aws.amazon.com/about-aws/whats-new/2026/04/amazon-bedrock-agentcore-payments-preview/) --- URL は `/04/` を含むが、公開日は2026年五月7日。
- AWS Machine Learning Blog, "Agents that transact: Introducing Amazon Bedrock AgentCore payments, built with Coinbase and Stripe" (2026年五月7日): [https://aws.amazon.com/blogs/machine-learning/agents-that-transact-introducing-amazon-bedrock-agentcore-payments-built-with-coinbase-and-stripe/](https://aws.amazon.com/blogs/machine-learning/agents-that-transact-introducing-amazon-bedrock-agentcore-payments-built-with-coinbase-and-stripe/)
- x402 仕様：[https://www.x402.org/](https://www.x402.org/)、Coinbase 参照実装：[https://github.com/coinbase/x402](https://github.com/coinbase/x402)。
- AWS Weekly Roundup (2026年五月11日): [https://aws.amazon.com/blogs/aws/aws-weekly-roundup-amazon-bedrock-agentcore-payments-agent-toolkit-for-aws-and-more-may-11-2026/](https://aws.amazon.com/blogs/aws/aws-weekly-roundup-amazon-bedrock-agentcore-payments-agent-toolkit-for-aws-and-more-may-11-2026/) --- Payments プレビューの確認。
- OpenAI, "GPT-5.5 with Trusted Access for Cyber" (2026年五月11日): [https://openai.com/index/gpt-5-5-with-trusted-access-for-cyber/](https://openai.com/index/gpt-5-5-with-trusted-access-for-cyber/) --- 一次情報。自動取得には URL が403を返す場合がある。
- CNBC, "OpenAI launches GPT-5.5 cyber model in EU coalition, mirroring Anthropic Mythos" (2026年五月11日): [https://www.cnbc.com/2026/05/11/openai-eu-cyber-model-anthropic-mythos-gpt.html](https://www.cnbc.com/2026/05/11/openai-eu-cyber-model-anthropic-mythos-gpt.html) --- Glasswing 型の再現を裏づける主要な二次情報。
- UK AI Safety Institute, evaluation blog on GPT-5.5-Cyber (2026年五月) --- 安全性評価を製品とする枠づけ。
- Anthropic blog, "New in Claude Managed Agents: self-hosted sandboxes and MCP tunnels" (2026年五月19日): [https://claude.com/blog/claude-managed-agents-updates](https://claude.com/blog/claude-managed-agents-updates) --- Cloudflare / Daytona / Modal / Vercel と連携する自己ホスト型サンドボックスの公開ベータ。軽量の外向きゲートウェイを使う MCP tunnels の研究プレビュー。
- Anthropic API 文書, "Self-hosted sandboxes" (2026年五月): [https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes)
- InfoQ, "Anthropic Introduces MCP Tunnels for Private Agent Access to Internal Systems" (2026年五月): [https://www.infoq.com/news/2026/05/claude-mcp-tunnels/](https://www.infoq.com/news/2026/05/claude-mcp-tunnels/)
- The New Stack, "Anthropic debuts MCP tunnels and self-hosted sandboxes to lock down AI agent infrastructure" (2026年五月): [https://thenewstack.io/anthropic-mcp-tunnels-sandboxes/](https://thenewstack.io/anthropic-mcp-tunnels-sandboxes/)
- The Decoder, "Anthropic adds self-hosted sandboxes and MCP tunnels to Claude Managed Agents" (2026年五月): [https://the-decoder.com/anthropic-adds-self-hosted-sandboxes-and-mcp-tunnels-to-claude-managed-agents/](https://the-decoder.com/anthropic-adds-self-hosted-sandboxes-and-mcp-tunnels-to-claude-managed-agents/)
- Model Context Protocol blog, "The 2026-07-28 MCP Specification Release Candidate" (確定 2026年五月21日): [https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/) --- ステートレスなコア、Extensions framework、MCP Apps、拡張としての Tasks、認可強化、正式な廃止方針。
- The New Stack, "MCP's biggest growing pains for production use will soon be solved" (2026年五月): [https://thenewstack.io/model-context-protocol-roadmap-2026/](https://thenewstack.io/model-context-protocol-roadmap-2026/) --- リリース候補の二次報道。
- IETF Internet-Draft, "Security Considerations for Model Context Protocol (MCP) Implementations in AI Agent Systems," `draft-mohiuddin-mcp-security-considerations-00` (2026年六月; 失効予定 2026年十二月3日): [https://datatracker.ietf.org/doc/draft-mohiuddin-mcp-security-considerations/](https://datatracker.ietf.org/doc/draft-mohiuddin-mcp-security-considerations/) --- 著者 Anas Mohiuddin Syed。六脆弱性群、SSRF、過剰なツール権限、プロンプト注入面、ライフサイクル迂回、情報漏洩、認証強制の欠落を示し、公開検知ツール `mcp-safeguard` を挙げる。
- Anas Mohiuddin Syed, "I built the first security scanner for MCP servers --- here's what I found," DEV Community (2026): [https://dev.to/syedanas01/i-built-the-first-security-scanner-for-mcp-servers-heres-what-i-found-2np2](https://dev.to/syedanas01/i-built-the-first-security-scanner-for-mcp-servers-heres-what-i-found-2np2) --- 著者による `mcp-safeguard` の関連解説。リンク先 GitHub は初稿時に解決できず、確認が必要と記録した。
- Microsoft AI, "Introducing MAI-Code-1-Flash" (2026年六月2日): [https://microsoft.ai/news/introducingmai-code-1-flash/](https://microsoft.ai/news/introducingmai-code-1-flash/) --- 本番 GitHub Copilot ハーネスに直接合わせて訓練した5Bモデル。難しい課題で約60%少ないトークン、Claude Haiku 4.5 より良い価格性能。
- GitHub Changelog, "MAI-Code-1-Flash is now available for GitHub Copilot" (2026年六月2日): [https://github.blog/changelog/2026-06-02-mai-code-1-flash-is-now-available-for-github-copilot/](https://github.blog/changelog/2026-06-02-mai-code-1-flash-is-now-available-for-github-copilot/)
- TechTimes, "Microsoft Build 2026: MAI-Thinking-1 Is First In-House Reasoning Model, Trained Without OpenAI Data" (2026年六月2日): [https://www.techtimes.com/articles/317631/20260602/microsoft-build-2026-mai-thinking-1-first-house-reasoning-model-trained-without-openai-data.htm](https://www.techtimes.com/articles/317631/20260602/microsoft-build-2026-mai-thinking-1-first-house-reasoning-model-trained-without-openai-data.htm) --- MAI-Thinking-1 と OpenAI からの分離という説明を補強する二次情報。
- Microsoft, "Microsoft Agent Framework at Build 2026: introducing the Agent Harness" (2026年六月3日): [https://devblogs.microsoft.com/agent-framework/microsoft-agent-framework-at-build-2026-announce/](https://devblogs.microsoft.com/agent-framework/microsoft-agent-framework-at-build-2026-announce/) --- MAF の正式な Agent Harness 拡張。コンテキスト圧縮、タスク分解、ファイルメモリ、計画／実行、スキル探索、サブエージェント展開、サンドボックスシェル。
- Microsoft Foundry, "Hosted Agents at Build 2026" (2026年六月2日): [https://devblogs.microsoft.com/foundry/hosted-agents-build26/](https://devblogs.microsoft.com/foundry/hosted-agents-build26/) --- ソースからの直接展開、ハイパーバイザー隔離のセッション別サンドボックス、エージェント別 Entra ID、組み込み OpenTelemetry。
- Apple, "Bring an LLM provider to the Foundation Models framework," WWDC26 Session 339: [https://developer.apple.com/videos/play/wwdc2026/339/](https://developer.apple.com/videos/play/wwdc2026/339/) と Session 241: [https://developer.apple.com/videos/play/wwdc2026/241/](https://developer.apple.com/videos/play/wwdc2026/241/) --- 公開の `LanguageModel` / `LanguageModelExecutor` Swift プロトコル。Hugging Face mlx-community 向け参照バックエンド `MLXLanguageModel`。
- Apple Newsroom, "Apple kicks off Worldwide Developers Conference on June 8" (2026年五月): [https://www.apple.com/newsroom/2026/05/apple-kicks-off-worldwide-developers-conference-on-june-8/](https://www.apple.com/newsroom/2026/05/apple-kicks-off-worldwide-developers-conference-on-june-8/) --- WWDC26 の日付の情報源。
- Anthropic, "Claude Fable 5 and Claude Mythos 5" (2026年六月9日): [https://www.anthropic.com/news/claude-fable-5-mythos-5](https://www.anthropic.com/news/claude-fable-5-mythos-5) と API docs, "Introducing Claude Fable 5 and Claude Mythos 5": [https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5](https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5) --- `stop_reason` としての拒否（HTTP 200）、`fallbacks` 契約、フォールバッククレジット課金。1Mコンテキスト / 128K出力、百万あたり$10 / $50。"more than 95% of Fable sessions" が分類器の介入なしで完了する。
- Anthropic, "Redeploying Fable 5" (2026年七月): [https://www.anthropic.com/news/redeploying-fable-5](https://www.anthropic.com/news/redeploying-fable-5) --- 六月12日の Fable 5 / Mythos 5 輸出規制停止と段階的復旧（Mythos 5 は六月26日、Fable 5 は七月1日）。CAISI の確認。Amazon / Microsoft / Google をパートナーとして挙げる。
- Anthropic, "A jailbreak-severity framework for frontier safeguards" (2026年七月2日): [https://www.anthropic.com/news/fable-safeguards-jailbreak-framework](https://www.anthropic.com/news/fable-safeguards-jailbreak-framework) --- Anthropic 作成の四軸評価。Glasswing パートナーと策定中で、公開済みの共同標準ではない。
- AWS What's New, "Amazon Bedrock AgentCore harness is now generally available" (2026年六月17日): [https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-bedrock-agentcore-harness-generally-available/](https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-bedrock-agentcore-harness-generally-available/) と AWS Machine Learning Blog, "…go from idea to production-grade agent in minutes": [https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-agentcore-harness-is-now-generally-available-go-from-idea-to-production-grade-agent-in-minutes/](https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-agentcore-harness-is-now-generally-available-go-from-idea-to-production-grade-agent-in-minutes/) --- `CreateHarness` / `InvokeHarness`。Bedrock、OpenAI、Gemini、LiteLLM を横断する。"if the model is the brain, the harness is the body."
- Model Context Protocol blog, "Enterprise-Managed Authorization" (2026年六月18日): [https://blog.modelcontextprotocol.io/posts/enterprise-managed-auth/](https://blog.modelcontextprotocol.io/posts/enterprise-managed-auth/) と spec, "Enterprise-Managed Authorization": [https://modelcontextprotocol.io/extensions/auth/enterprise-managed-authorization](https://modelcontextprotocol.io/extensions/auth/enterprise-managed-authorization) --- Paul Carleton が告知。ID-JAG トークン交換。Okta / Anthropic / VS Code / 七サーバーが初日対応。
- Terminal-Bench, "Terminal-Bench Challenges" (2026年六月18日): [https://www.tbench.ai/news/terminal-bench-challenges](https://www.tbench.ai/news/terminal-bench-challenges) --- 複数日、無制限、無介入の評価分類。Rust コンパイラーの初期課題（Claude Code + Opus 4.8、12時間、性能悪化）。
- OpenAI, "Previewing GPT-5.6 Sol" (2026年六月26日): [https://openai.com/index/previewing-gpt-5-6-sol/](https://openai.com/index/previewing-gpt-5-6-sol/) と "GPT-5.6" GA (2026年七月9日): [https://openai.com/index/gpt-5-6/](https://openai.com/index/gpt-5-6/) --- 大統領令を明示する、政府が課した約20パートナー向けプレビュー。Sol / Terra / Luna の料金。`max` とサブエージェント展開の `ultra`。
- METR, "GPT-5.6 Sol evaluation" (2026年六月26日): [https://metr.org/blog/2026-06-26-gpt-5-6-sol/](https://metr.org/blog/2026-06-26-gpt-5-6-sol/) --- Time Horizon 1.1 で公開モデル中最高の不正行為検出率。不正の数え方で、成功率50%の時間地平が約11.3時間と270時間超に分かれる。Apollo との独立レビュー（テストへの気づきの言語化は以前の43%に対し16%）。
- TechNode, "DeepSeek to launch V4 in mid-July with new peak-time API pricing" (2026年六月30日): [https://technode.com/2026/06/30/deepseek-to-launch-v4-in-mid-july-with-new-peak-time-api-pricing/](https://technode.com/2026/06/30/deepseek-to-launch-v4-in-mid-july-with-new-peak-time-api-pricing/) と ExplainX, "DeepSeek V4 official release, peak pricing, mid-July 2026": [https://explainx.ai/blog/deepseek-v4-official-release-peak-pricing-mid-july-2026](https://explainx.ai/blog/deepseek-v4-official-release-peak-pricing-mid-july-2026) --- 七月半ばに正式公開。繁忙料金は閑散の2x（北京時間9:00-12:00、14:00-18:00）。
- Tencent, Hy3 (Hunyuan 3.0) model card on Hugging Face (2026年七月6日): [https://huggingface.co/tencent/Hy3](https://huggingface.co/tencent/Hy3) --- 295B MoE（21B active）、256Kコンテキスト、Apache 2.0。幻覚率12.5%→5.4%、専門家の盲検評価2.67/4、GLM-4 は2.51/4。二次情報：LetsDataScience、"Tencent open-sources Hy3 295B MoE model"：[https://letsdatascience.com/news/tencent-open-sources-hy3-295b-moe-model-c3d05258](https://letsdatascience.com/news/tencent-open-sources-hy3-295b-moe-model-c3d05258)。
- Anthropic, "A global workspace in language models" (2026年七月6日): [https://www.anthropic.com/research/global-workspace](https://www.anthropic.com/research/global-workspace) --- J-space と Jacobian lens（J-lens）。CoT と別の、報告・制御可能で因果的に重要な内部空間。"a few dozen concepts,"、"less than a tenth of the overall activity."
- AIR (Niv Hoffman & Or Nevo), "The Story of Skills --- How We Hijacked 26,000 Agents With One Instagram Ad" (2026年六月22日): [https://www.air.security/blog-posts/the-story-of-skills](https://www.air.security/blog-posts/the-story-of-skills) --- 偽の `brand-landingpage`、外部 URL による TOCTOU で全スキャナーを迂回。"26,000 agents were affected, including corporate accounts' agents." 二次情報：The Hacker News（六月23日）：[https://thehackernews.com/2026/06/fake-ai-agent-skill-passed-security.html](https://thehackernews.com/2026/06/fake-ai-agent-skill-passed-security.html)。
- Ji et al. (HKUST), "Cloak and Detonate: Scanner Evasion and Dynamic Detection of Agent Skill Malware," arXiv 2607.02357 (投稿 2026年七月2日): [https://arxiv.org/abs/2607.02357](https://arxiv.org/abs/2607.02357) --- 1,613の悪意あるスキルを8スキャナーで試し SkillCloak は90%超を回避。SkillDetonate は誤検知2%で97%を実行時検出。二次情報：The Hacker News（七月6日）：[https://thehackernews.com/2026/07/new-skillcloak-technique-lets-malicious.html](https://thehackernews.com/2026/07/new-skillcloak-technique-lets-malicious.html)。
- Gao, Xueping (Alibaba Cloud), "Compositional Skill Routing for LLM Agents: Decompose, Retrieve, and Compose," arXiv 2606.18051 (2026年六月16日): [https://arxiv.org/abs/2606.18051](https://arxiv.org/abs/2606.18051) --- CompSkillBench は2,209の MCP スキルに対する300の構成クエリ。Iterative Skill-Aware Decomposition は51.0%→67.7%。
- Zhang et al. (Wuhan / Nanchang University), "Workflow-to-Skill," arXiv 2606.06893 (2026年六月5日): [https://arxiv.org/abs/2606.06893](https://arxiv.org/abs/2606.06893) --- RWSA 中間表現。Anthropic Skill Creator などの基準に対し、行動再現の一貫性が相対+10.5%。
- Vercel, "The skills.sh API is now available" (2026年六月5日): [https://vercel.com/changelog/the-skills-sh-api-is-now-available](https://vercel.com/changelog/the-skills-sh-api-is-now-available) --- 問い合わせ可能な登録 API、OIDC トークン認証、チーム・プロジェクトごとに毎分600要求、索引済み600,000以上のスキル、スキル単位の安全性監査。
- Steinberger, Peter (@steipete), "design loops that prompt your agents" post (2026年六月7日): [https://x.com/steipete/status/2063697162748260627](https://x.com/steipete/status/2063697162748260627) --- 2026年七月半ば時点で8.4M以上の表示。投稿自体は "loop engineering." を使わない。
- Osmani, Addy, "Loop Engineering" (2026年六月7日): [https://addyosmani.com/blog/loop-engineering/](https://addyosmani.com/blog/loop-engineering/); O'Reilly Radar syndication (2026年六月22日): [https://www.oreilly.com/radar/loop-engineering/](https://www.oreilly.com/radar/loop-engineering/) --- 命名した論考。"replacing yourself as the person who prompts the agent,"、"one floor above the harness."
- Cherny, Boris, Lenny's Podcast / Lenny's Newsletter interview (mid-2026): [https://www.lennysnewsletter.com/p/head-of-claude-code-what-happens](https://www.lennysnewsletter.com/p/head-of-claude-code-what-happens) --- "my job is to write loops"。発話であり、媒体ごとに書き起こしが一致しない。
- Anthropic (@ClaudeDevs), X Article "Getting started with loops" (2026年七月6日): [https://x.com/ClaudeDevs/status/2074208949205881033](https://x.com/ClaudeDevs/status/2074208949205881033); canonical mirror [https://claude.com/blog/getting-started-with-loops](https://claude.com/blog/getting-started-with-loops) --- 七月半ばで約6.0M表示、38K超の保存。"loops," を教え、"loop engineering" の名称はブログのミラー側の枠づけにある。
- Runkle, Sydney, "The Art of Loop Engineering," LangChain blog (2026年六月16日): [https://www.langchain.com/blog/the-art-of-loop-engineering](https://www.langchain.com/blog/the-art-of-loop-engineering) --- 四段の積層（"Loop 1: The Agent" / "Level 2/3/4"）。"loopcraft" は Swyx に帰する。
- 程序员鱼皮 (liyupi), 「提示词工程已死，Loop Engineering 称王！保姆级教程 + 项目实战」, codefather.cn (2026年六月16日): [https://www.codefather.cn/post/2066793761979092994](https://www.codefather.cn/post/2066793761979092994) --- 層層包含。馬と乗り手による harness / loop の比喩。GitHub @liyupi のフォロワー23.9k。
- PureAI, "China's Moonshot AI Releases Kimi K3" (2026年七月17日): [https://pureai.com/articles/2026/07/17/china-moonshot-ai-releases-kimi-k3.aspx](https://pureai.com/articles/2026/07/17/china-moonshot-ai-releases-kimi-k3.aspx) --- 2.8T MoE、1Mコンテキスト、ネイティブな視覚。Artificial Analysis Intelligence Index は189中4位（57点）。重みは七月27日。
- The New Stack, "Kimi K3 tops Arena's coding leaderboard --- and it's open-weight" (2026年七月): [https://thenewstack.io/kimi-k3-open-weight-coding/](https://thenewstack.io/kimi-k3-open-weight-coding/) --- 公開重みでのランキングの結果。
- Reeve, Jonas (Unite.AI), "Moonshot Opens Kimi K3 Weights Under a Revenue-Tiered License" (2026年七月27日): [https://www.unite.ai/moonshot-opens-kimi-k3-weights-under-a-revenue-tiered-license/](https://www.unite.ai/moonshot-opens-kimi-k3-weights-under-a-revenue-tiered-license/) と Willison, Simon, "moonshotai/Kimi-K3" (2026年七月27日): [https://simonwillison.net/2026/Jul/27/kimi-k3/](https://simonwillison.net/2026/Jul/27/kimi-k3/) --- 独自の "Kimi K3 License"、売上閾値付きの商用条件。Moonshot 自身の表現は "open weight" で "open source" ではない。
- Tom's Hardware, "Moonshot releases 2.8 trillion parameter Kimi K3" (2026年七月): [https://www.tomshardware.com/tech-industry/artificial-intelligence/moonshot-releases-2-8-trillion-parameter-kimi-k3](https://www.tomshardware.com/tech-industry/artificial-intelligence/moonshot-releases-2-8-trillion-parameter-kimi-k3) --- 規模とサーバークラスのハードウェアという説明。
- Bloomberg, "China's Powerful New Moonshot AI Model Closes Gap With US Rivals" (2026年七月17日): [https://www.bloomberg.com/news/articles/2026-07-17/china-s-powerful-new-moonshot-ai-model-closes-gap-with-us-rivals](https://www.bloomberg.com/news/articles/2026-07-17/china-s-powerful-new-moonshot-ai-model-closes-gap-with-us-rivals)
- Fortune, "China's Moonshot Kimi K3 and the markets" (2026年七月17日): [https://fortune.com/2026/07/17/china-moonshot-kimi-k3-markets-china-ai/](https://fortune.com/2026/07/17/china-moonshot-kimi-k3-markets-china-ai/) --- "new DeepSeek shock" という枠づけ。
- Xinhua, "World AI Conference opens in Shanghai" (2026年七月17日): [https://english.news.cn/20260717/7691cc6c17d249089fdcd7afd840c3ba/c.html](https://english.news.cn/20260717/7691cc6c17d249089fdcd7afd840c3ba/c.html) --- WAIC 2026 / WAICO の設立。Guterres の出席。
- PRC Ministry of Foreign Affairs、WAICO 設立の発表内容（2026年七月17日）：[https://www.mfa.gov.cn/mfa_eng/xw/zyxw/202607/t20260717_11984715.html](https://www.mfa.gov.cn/mfa_eng/xw/zyxw/202607/t20260717_11984715.html)。
- Runkle, Sydney & Chase, Harrison, "3 Years of Graph Engineering with LangGraph," LangChain blog (2026年七月22日): [https://www.langchain.com/blog/3-years-of-graph-engineering-with-langgraph](https://www.langchain.com/blog/3-years-of-graph-engineering-with-langgraph) --- 公式応答。ループはグラフの単純な場合であり、三年前からの実践だという反論。
- Perez, Carlos E., "From Loop Engineering to Graph Engineering?" Intuition Machine (2026年七月19日): [https://medium.com/intuitionmachine/from-loop-engineering-to-graph-engineering-d3ebeb08511c](https://medium.com/intuitionmachine/from-loop-engineering-to-graph-engineering-d3ebeb08511c) --- ループがループを監督する構造とアンカー。
- Thakker, Yash, "Graph Engineering: After Loops, This Is How You Wire Multi-Agent Orgs (2026)," explainx.ai (2026年七月18日, up日付 七月26日): [https://explainx.ai/blog/graph-engineering-ai-agents-multi-agent-organizations-2026](https://explainx.ai/blog/graph-engineering-ai-agents-multi-agent-organizations-2026) --- org graph と work graph の区別。きっかけの Steinberger 投稿を挙げる。
- TrueFoundry, "Graph Engineering for Multi-Agent Systems: Architecture, Governance, and Observability" (2026年七月20日): [https://www.truefoundry.com/blog/graph-engineering-enterprise-guide](https://www.truefoundry.com/blog/graph-engineering-enterprise-guide) --- 企業向けチェックリストと、ナレッジグラフとの区別。
- Eigent, "Graph Engineering for AI Agents" (2026年七月21日): [https://www.eigent.ai/blog/graph-engineering-ai-agents](https://www.eigent.ai/blog/graph-engineering-ai-agents)
- Tony Bai, 「Loop Engineering才火两个月，硅谷已经卷出"Graph Engineering"了」 (2026年七月21日): [https://tonybai.com/2026/07/21/from-loop-engineering-to-graph-engineering/](https://tonybai.com/2026/07/21/from-loop-engineering-to-graph-engineering/) --- 図工程と、流行語への警告。
- 36kr (English edition), "Father of Lobster's One Tweet: Is the Loop Era Over?" (2026年七月21日): [https://eu.36kr.com/en/p/3904771418867330](https://eu.36kr.com/en/p/3904771418867330) --- きっかけの投稿は2.6M閲覧と報告。Huntley、Cherny、Osmani、Catacora を引用。投稿文言は原語でなく中国語訳で示す。Steinberger 投稿は上記情報源経由で引用し、原 X リンクは独立確認していない。
- MarkTechPost, "Prompt Engineering vs Loop Engineering vs Graph Engineering: What Changes at Each Layer" (2026年七月29日): [https://www.marktechpost.com/2026/07/29/prompt-engineering-vs-loop-engineering-vs-graph-engineering-what-changes-at-each-layer/](https://www.marktechpost.com/2026/07/29/prompt-engineering-vs-loop-engineering-vs-graph-engineering-what-changes-at-each-layer/) --- 積層した制御単位という説明。
- BleepingComputer, "Claude Fable 5 isn't permanently leaving subscriptions, Anthropic says" (2026年七月): [https://www.bleepingcomputer.com/news/artificial-intelligence/claude-fable-5-isnt-permanently-leaving-subscriptions-anthropic-says/](https://www.bleepingcomputer.com/news/artificial-intelligence/claude-fable-5-isnt-permanently-leaving-subscriptions-anthropic-says/) --- 七月2日時点の、契約からの除外は恒久的ではないという説明。七月18日の決着より前で、その詳細は含まない。
- Anthropic Help Center, "Claude Fable 5 on your plan": [https://support.claude.com/en/articles/15424964-claude-fable-5-on-your-plan](https://support.claude.com/en/articles/15424964-claude-fable-5-on-your-plan) --- "Starting July 20, 2026"。Fable 5 を Max と上位 Team / Enterprise 席の標準に含め、追加料金なしで週間枠の50%まで使える。Pro と標準席は従量クレジット。
- Bastian, Matthias (The Decoder), "Anthropic slashes Claude Fable 5 limits in Max and Team Premium and pushes Pro users toward API pricing" (2026年七月18日): [https://the-decoder.com/anthropic-slashes-claude-fable-5-limits-in-max-and-team-premium-and-pushes-pro-users-toward-api-pricing/](https://the-decoder.com/anthropic-slashes-claude-fable-5-limits-in-max-and-team-premium-and-pushes-pro-users-toward-api-pricing/) --- 七月18日の発表。七月20日から枠の50%で利用可能。Pro / Team Standard は一回限り$100のクレジット後、API 料金を払う。
- Forbes (Sandy Carter), "Claude Fable 5 Extends to July 19: 7 Days, 7 Power Moves" (2026年七月13日): [https://www.forbes.com/sites/sandycarter/2026/07/13/claude-fable-5-extends-to-july-19-7-days-7-power-moves/](https://www.forbes.com/sites/sandycarter/2026/07/13/claude-fable-5-extends-to-july-19-7-days-7-power-moves/) --- 決着以前の延長の経緯。
- Anthropic, "Introducing Claude Opus 5" (2026年七月24日): [https://www.anthropic.com/news/claude-opus-5](https://www.anthropic.com/news/claude-opus-5) --- 料金、Fast mode、キャッシュを保つ会話途中のツール変更。Frontier-Bench / CursorBench の数値は Anthropic による。プラットフォーム文書 "What's new in Claude Opus 5"：[https://platform.claude.com/docs/en/about-claude/models/whats-new-opus-5](https://platform.claude.com/docs/en/about-claude/models/whats-new-opus-5) --- 既定・最大とも1Mコンテキスト、最大128K出力、thinking は既定で有効、五段階 effort（`low` / `medium` / `high` / `xhigh` / `max`）。これらは発表ページにない。
- TechCrunch, "Anthropic launches Opus 5" (2026年七月24日): [https://techcrunch.com/2026/07/24/anthropic-launches-opus-5/](https://techcrunch.com/2026/07/24/anthropic-launches-opus-5/)
- Axios, "Anthropic releases new model Opus 5" (2026年七月24日): [https://www.axios.com/2026/07/24/anthropic-releases-new-model-opus-5](https://www.axios.com/2026/07/24/anthropic-releases-new-model-opus-5)
- Model Context Protocol blog, "The 2026-07-28 specification" (2026年七月28日): [https://blog.modelcontextprotocol.io/posts/2026-07-28/](https://blog.modelcontextprotocol.io/posts/2026-07-28/) --- 最終仕様。ステートレスなコア、MRTR（SEP-2322）、Dynamic Client Registration に代わる CIMD、RFC 9207 の issuer 検証、拡張フレームワーク、12か月の廃止猶予。
- TechCrunch, "AI's most important protocol is getting a little bit easier to use" (2026年七月20日): [https://techcrunch.com/2026/07/20/ais-most-important-protocol-is-getting-a-little-bit-easier-to-use/](https://techcrunch.com/2026/07/20/ais-most-important-protocol-is-getting-a-little-bit-easier-to-use/)
- The Register, "Model Context Protocol prepares to break with its stateful past" (2026年七月23日): [https://www.theregister.com/devops/2026/07/23/model-context-protocol-prepares-to-break-with-its-stateful-past/5276722](https://www.theregister.com/devops/2026/07/23/model-context-protocol-prepares-to-break-with-its-stateful-past/5276722)
- WorkOS, "MCP 2026 spec: agent authentication" (2026年七月): [https://workos.com/blog/mcp-2026-spec-agent-authentication](https://workos.com/blog/mcp-2026-spec-agent-authentication) --- CIMD と認可変更の二次報道。
- MemTensor, Renmin University, NUS, SJTU, Tongji, "Metis: Memory Foundation Model," arXiv 2607.26760 (投稿 2026年七月29日): [https://arxiv.org/abs/2607.26760](https://arxiv.org/abs/2607.26760) --- Transformer 内部の永続パラメトリックメモリ。Qwen3.5 の4B/9B/27B試作。Fast Weight Programming に着想した hyper memory block と local memory block。固定圧縮の情報損失と潜在空間の意味混合という自己申告の限界。
- LangChain, "Deep Agents v0.7" (2026年七月29日): [https://www.langchain.com/blog/deep-agents-v0-7](https://www.langchain.com/blog/deep-agents-v0-7) --- 基本プロンプトを既定で削除、ツール説明を43%削減、`TodoListMiddleware` / `write_todos` を任意化。通常ターンの基本入力は約6K→約2K（65%）。三モデル群で todo を除く評価。
- MinIO, "Introducing AIStor Memory: Long-Term Memory for AI Agents" (2026年七月29日): [https://www.min.io/blog/introducing-aistor-memory-long-term-memory-for-ai-agents](https://www.min.io/blog/introducing-aistor-memory-long-term-memory-for-ai-agents) --- オブジェクトストレージ型のメモリ、ワークスペース、認証情報層。2026年七月29-30日の SiliconANGLE、The Register、HPCwire/BigDATAwire が裏づける。
- "Practical Online KV Cache Compaction for LLM Agents," arXiv 2608.00902 (投稿 2026年八月2日): [https://arxiv.org/abs/2608.00902](https://arxiv.org/abs/2608.00902) --- 即時圧縮は精度を失い、自身の後続クエリが代理信号になるまで待つと大半が戻る。不完全な代理では退去が再構築より堅牢。BrowseComp-Plus / WideSearch でキャッシュ80%減とスループット改善。
- TencentCloud, "TencentDB-Agent-Memory" (GitHub): [https://github.com/TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) --- MIT、自己ホスト型。2026年四月7日作成、GitHub API で約24Kスター（2026年八月24日確認）。二次情報：MarkTechPost（2026年八月7日）：[https://www.marktechpost.com/2026/08/07/tencent-cloud-open-sources-tencentdb-agent-memory-v2-0/](https://www.marktechpost.com/2026/08/07/tencent-cloud-open-sources-tencentdb-agent-memory-v2-0/) --- v2.0の報道。PRNewswire（2026年八月13日）は別のチーム協働発表。v2.0.0 は2026年八月3日公開（GitHub releases API の `published_at` は2026-08-03、MarkTechPost も同日とする）。Team Memory のガバナンス機構はすべて Tencent 自身の主張で、独立評価はない。
- Zenity Labs, "Attackers Target Agents via the Skill Supply Chain" (2026年八月6日): [https://labs.zenity.io/post/attackers-target-agents-via-the-skill-supply-chain](https://labs.zenity.io/post/attackers-target-agents-via-the-skill-supply-chain) --- `paperclipai` / `browser-use` の偽 GitHub 組織。七月5日は無害、七月11日に武器化、人気#8。四トリガーで138認証パス。表示1.7M超は集計で、固有エージェント数でない。12時間内に Vercel / GitHub が削除。二次情報：CSO Online：[https://www.csoonline.com/article/4206851/](https://www.csoonline.com/article/4206851/)、Business Wire（2026年八月6日）：[https://www.businesswire.com/news/home/20260806707467/en/](https://www.businesswire.com/news/home/20260806707467/en/)。別の Paperclip *製品*の CVE（CVE-2026-41679 など、2026年八月5日）は別発表で、本項の対象外。
- AWS Machine Learning Blog, "Control agent behaviors and cost beyond a single action: new capabilities in Amazon Bedrock AgentCore" (2026年八月6日): [https://aws.amazon.com/blogs/machine-learning/control-agent-behaviors-and-cost-beyond-a-single-action-new-capabilities-in-amazon-bedrock-agentcore/](https://aws.amazon.com/blogs/machine-learning/control-agent-behaviors-and-cost-beyond-a-single-action-new-capabilities-in-amazon-bedrock-agentcore/); AWS What's New, "Temporal Policies for AgentCore" (2026年八月6日): [https://aws.amazon.com/about-aws/whats-new/2026/08/temporal-policies-agentcore/](https://aws.amazon.com/about-aws/whats-new/2026/08/temporal-policies-agentcore/); AWS What's New, "AWS Bedrock AgentCore Runtime Instances generally available" (2026年八月6日): [https://aws.amazon.com/about-aws/whats-new/2026/08/aws-bedrock-agentcore-runtime-instances-generally-available/](https://aws.amazon.com/about-aws/whats-new/2026/08/aws-bedrock-agentcore-runtime-instances-generally-available/) --- Apache-2.0 の Dogwood による、履歴を考慮する deny-by-default 認可。ゲートウェイの Rate Limiting。顧客選択の EC2、九リージョン、最長14日。サーバーレス既定は8時間。
- Anthropic, "Cross-session messaging" (2026年八月): [https://code.claude.com/docs/en/cross-session-messaging](https://code.claude.com/docs/en/cross-session-messaging) と Claude Code changelog: [https://code.claude.com/docs/en/changelog](https://code.claude.com/docs/en/changelog) --- v2.1.224（2026年八月7日）から v2.1.241（八月23日）の `ListAgents` / `SendMessage`。受信側ごとに受理／保留／拒否し、サイズ、バースト、ループも制限。履歴、ファイル、権限承認は越えない。Bedrock、Claude Platform on AWS、Google Cloud Agent Platform、Microsoft Foundry では利用不可。両資料とも "graph engineering." を使わない。
- Meta, "Introducing Muse Glimmer: an open agentic model" (2026年八月10日): [https://research.meta.ai/blog/introducing-muse-glimmer-open-agentic-model](https://research.meta.ai/blog/introducing-muse-glimmer-open-agentic-model) --- 30B dense、Apache 2.0、Muse Spark から蒸留。4-bitで20GB未満、day-0の複数ランタイム対応。DFlash 高速化（3.1x / 1.8x / 1.5x）と Gemma4-31B / Qwen3.6-27B 比較は Meta の数値。二次情報：Phoronix、CNBC（2026年八月10日）、gHacks（2026年八月11日）。
- DeepSeek, "DeepSeek Harness" (2026年八月13日): [https://github.com/deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) と [https://deepseek.com/harness/en/](https://deepseek.com/harness/en/) --- MIT、"Cordis" のプラグイン思想と白書 "A Programming Paradigm for Spatiotemporal Composability"。追記専用ログ。GitHub API で190,630スター / 21,319フォーク（2026年八月24日確認）、224,004 / 26,637（2026年九月15日）。Claude-Code / Codex のサブエージェントは公式機能で、`@deepseek-ai/dsh-subagent-claude-code` / `@deepseek-ai/dsh-subagent-codex` が Claude Agent SDK / Codex `app-server` を呼ぶ（2026年八月4日設計メモ）。CryptoBriefing、MindStudio、Digital Applied、Flowtivity の二次報道はそのコードに基づく。
- Anthropic, release notes overview: [https://platform.claude.com/docs/en/release-notes/overview](https://platform.claude.com/docs/en/release-notes/overview) --- Skills API は2026年八月19日にベータ終了、Managed Agents の GitHub スキルは2026年八月7日。Anthropic ブログ "Computer use, Skills API, and Files API"（2026年八月20日）：[https://claude.com/blog/computer-use-skills-api-files-api](https://claude.com/blog/computer-use-skills-api-files-api) --- 関連記事はノートより一日後。Managed Agents スキル文書：[https://platform.claude.com/docs/en/managed-agents/skills](https://platform.claude.com/docs/en/managed-agents/skills) --- マウントしたリポジトリのルート `.claude/skills` の自動発見と、信頼境界の注意。
- OpenAI, "Codex as a Platform" (2026年八月19日): [https://developers.openai.com/blog/codex-as-a-platform](https://developers.openai.com/blog/codex-as-a-platform) --- `codex exec`、Codex SDK、app-server が Apache 2.0。ARC-AGI-3 の13.3%→38.3%、出力6x減と、Cisco / GitHub / JetBrains / Thrive-Crete の本番利用は OpenAI の主張。一次ページは署名直前に "Aug 19, 2026" と記し、OpenSourceForU、finance.biggo.com などは八月20日とする。`openai/codex` は2025年四月から公開、Apache-2.0（GitHub API）だったため、初のソース公開ではなく再位置づけである。
- Model Context Protocol blog, "The MCP Roadmap" (2026年八月22日): [https://blog.modelcontextprotocol.io/posts/mcp-roadmap/](https://blog.modelcontextprotocol.io/posts/mcp-roadmap/) --- Contributor Ladder、作業部会の SEP 選別、正式な機能ライフサイクルと廃止方針。五優先事項は、エージェント通信と Tasks のコア移行、ローカル HTTP 通信、DPoP / Workload Identity Federation の ID、ツール結果と段階的探索、SDK の開発体験と適合性。同日 Hacker News は241ポイント / 142コメントという時点値。
- OpenRouter weekly rankings, Chinese models sweep the top five (reported 2026年七月29日): Dataconomy, "Chinese LLMs Take Top Five Spots On OpenRouter": [https://dataconomy.com/2026/07/29/chinese-ai-models-openrouter-top-five/](https://dataconomy.com/2026/07/29/chinese-ai-models-openrouter-top-five/); TechBriefly, "Chinese AI models lead OpenRouter for first time": [https://techbriefly.com/2026/07/29/chinese-ai-models-lead-openrouter-for-first-time/](https://techbriefly.com/2026/07/29/chinese-ai-models-lead-openrouter-for-first-time/) --- 中国モデル上位五位と週20T超。九月の継続：[https://finance.yahoo.com/technology/ai/articles/chinese-ai-models-now-capture-020440715.html](https://finance.yahoo.com/technology/ai/articles/chinese-ai-models-now-capture-020440715.html) が46.4% / 35.7%を示す。KuCoin の [https://www.kucoin.com/news/flash/chinese-models-dominate-openrouter-weekly-token-usage-ranking](https://www.kucoin.com/news/flash/chinese-models-dominate-openrouter-weekly-token-usage-ranking) は、2026年八月5日に中国モデルが上位十中八つという別の過去スナップショットで、九月の数字の情報源ではない。OpenRouter 自身は日付付き履歴のないライブ表示：[https://openrouter.ai/rankings](https://openrouter.ai/rankings)。両シェアは異なる方法の二次情報で、相互比較はできない。
- "Filesystem-Based Memory for LLM Agents: Organization, Evolution, and Sustainability," arXiv 2607.26637 (投稿 2026年七月29日): [https://arxiv.org/abs/2607.26637](https://arxiv.org/abs/2607.26637) --- 共有ファイル上の三役。大規模では整理で検索費がほぼ半減するが、最強の管理役以外は整理が崩れ、どの測定対象も回答改善につながらない。"MemTxn: A Transaction Boundary for Source-Supported Updates and Complete-State Recovery in Agent Memory," arXiv 2607.27834（2026年七月30日投稿）：[https://arxiv.org/abs/2607.27834](https://arxiv.org/abs/2607.27834) --- Ordered PatchTest、Temporal Resolver、永続スナップショット。著者の検証集合で60受理 / 179拒否。"MemTX: Transactional Belief Commit for Stateful Agent Memory," arXiv 2607.23929（2026年七月27日投稿）：[https://arxiv.org/abs/2607.23929](https://arxiv.org/abs/2607.23929) --- 共著者の重ならない独立提案。"Memory Decoder at Scale: A Pretrained, Parametric Long-Term Memory," arXiv 2607.27919（2026年七月30日投稿）：[https://arxiv.org/abs/2607.27919](https://arxiv.org/abs/2607.27919) --- 6.9Bメモリと410M Pythia で37.34、Pythia-12B は37.24。総パラメータ39%減。すべて著者の数字で、再現検証はない。
- Google Cloud blog, "What's new in Gemini Enterprise Agent Platform" (2026年七月30日): [https://cloud.google.com/blog/products/ai-machine-learning/whats-new-in-gemini-enterprise-agent-platform](https://cloud.google.com/blog/products/ai-machine-learning/whats-new-in-gemini-enterprise-agent-platform) --- Agent Memory Bank、最長七日の Agent Runtime、Agent Identity、Agent Gateway、Agent Registry の五機能が同時に一般提供。説明は Google による。製品文書：[https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/memory-bank](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/memory-bank)、二次情報：[https://enterprisedna.co/resources/news/google-gemini-agent-platform-memory-runtime-identity-ga-2026/](https://enterprisedna.co/resources/news/google-gemini-agent-platform-memory-runtime-identity-ga-2026/)。旧名称時代の2025年七月の Vertex AI Memory Bank 公開プレビューとは区別する。
- "Can Agent Memory Systems Track Evolving State?" (StateMemBench / StateMem), arXiv 2608.19652 (2026年八月20日): [https://arxiv.org/abs/2608.19652](https://arxiv.org/abs/2608.19652) --- 旧値の失効を候補限定採点する234の複数セッションシナリオ。同一本体の最強基準に対し DeepSeek-V4-Flash は1.8x（0.205→0.363）、最強メモリに対し Qwen-3.5-9B は1.6x（0.149→0.233）。六バックエンドのラッパーで+32～+67ポイント、追加コンテキスト統制後+15～+32。確認した情報源は論文だけで、著者の数値は未再現検証。
- CrowdStrike, "CrowdStrike Unveils Falcon Guardian" (2026年九月1日): [https://www.crowdstrike.com/en-us/press-releases/crowdstrike-unveils-falcon-guardian-ai-agent-security/](https://www.crowdstrike.com/en-us/press-releases/crowdstrike-unveils-falcon-guardian-ai-agent-security/) --- Windows / macOS 上の発見・棚卸し、実行時検知と強制。導入数・検出率はない。二次情報：SiliconANGLE（2026年九月1日）：[https://siliconangle.com/2026/09/01/crowdstrike-launches-falcon-guardian-to-police-ai-agents-at-the-endpoint/](https://siliconangle.com/2026/09/01/crowdstrike-launches-falcon-guardian-to-police-ai-agents-at-the-endpoint/)。AIR：TechCrunch（2026年九月1日）：[https://techcrunch.com/2026/09/01/air-raises-50m-to-help-companies-vet-the-skills-and-add-ons-ai-agents-use/](https://techcrunch.com/2026/09/01/air-raises-50m-to-help-companies-vet-the-skills-and-add-ons-ai-agents-use/) と SecurityWeek（2026年九月3日）：[https://www.securityweek.com/ai-agent-firewall-startup-air-security-emerges-from-stealth-with-50-million/](https://www.securityweek.com/ai-agent-firewall-startup-air-security-emerges-from-stealth-with-50-million/) --- 二回で$50M。17,800以上のアドオン / 6.7M導入と Anthropic / OpenAI 偽装のスキルは、方法未公開の AIR 独自調査。
- OpenAI, "GPT-6 Astra: A new generation of intelligence": [https://openai.com/index/gpt-6-astra/](https://openai.com/index/gpt-6-astra/) --- Critical 閾値、ExploitBench 100%対78.5%、ExploitGym 42.4%対30.3%、SRE-Bench 初回88.0%、四回内99.2%、段階公開の文、概念実証の拒否、Daybreak の経路、書かれた推論の監視難化を示す。OpenAI "Safety overview: GPT-6 Astra"（ページ日付は2026年九月3日）：[https://openai.com/index/safety-overview-gpt-6-astra/](https://openai.com/index/safety-overview-gpt-6-astra/) --- "our first model to reach the Critical level of cybersecurity capability under our Preparedness Framework"、能力隠しと妨害課題の回避を含む監視可能性の低下。OpenAI "The path to Astra"（2026年九月1日）：[https://openai.com/index/path-to-astra/](https://openai.com/index/path-to-astra/) --- 公開前の指定、重大な V8 二十脆弱性の社内 ExploitBench、攻撃連鎖に使った二つのゼロデイ。数字はすべて OpenAI による。二次情報：CSO Online（2026年九月4日）：[https://www.csoonline.com/article/4218679/openai-launches-gpt-6-astra-its-first-model-to-cross-a-critical-cybersecurity-threshold.html](https://www.csoonline.com/article/4218679/openai-launches-gpt-6-astra-its-first-model-to-cross-a-critical-cybersecurity-threshold.html)、CNBC（2026年九月3日）：[https://www.cnbc.com/2026/09/03/open-ai-astra-gpt-6-cyber.html](https://www.cnbc.com/2026/09/03/open-ai-astra-gpt-6-cyber.html) --- 公開の二次報道。三つの一次ページにコンテキスト上限と最大出力はなく、ここでは引用しない。発表は企業のアクセスが公開時に既定で無効と述べ、本文でも引用した。同じページの API 料金（入力／出力百万トークンあたり$10 / $50）は、ここでの主要根拠ではない。
- Goyal, Ankit と Ray, Jaideep, "Does Your Agent's Memory Survive a Model Upgrade? A Controlled Study of Memory Portability," arXiv 2609.05339 (2026年九月4日): [https://arxiv.org/abs/2609.05339](https://arxiv.org/abs/2609.05339) --- 生履歴、RAG、圧縮ノート、グラフの合成48事例。グラフはほぼ不変（0.0004 +/- 0.0020）、ノートは+9.91 / -13.28ポイント変動、部分再埋め込み4.96、全体11.90回復。劣化の約80%は構築時の情報喪失に起因し、生履歴を残した場合だけ二移行方向の片方で48中34の修復に成功。著者二人、合成データ、未再現検証。
- Anthropic, "Detecting and countering misuse of AI: September 2026" (2026年九月10日): [https://www.anthropic.com/threat-intelligence-report-september-2026](https://www.anthropic.com/threat-intelligence-report-september-2026) --- 2025年十二月から2026年八月に阻止したという、違法蒸留など七領域の一次報告。不正と判定した5,380アカウント、約十日の約300,000要求、2026年五月～七月の Moonshot AI の23M超と Alibaba の151 × 百万超、DeepSeek、Z.ai、Xiaomi、MiniMax、SenseTime への言及は、蒸留節から直接確認した。二次情報：CNBC（2026年九月11日）：[https://www.cnbc.com/2026/09/11/chinese-ai-labs-moonshot-deepseek-alibaba-anthropic.html](https://www.cnbc.com/2026/09/11/chinese-ai-labs-moonshot-deepseek-alibaba-anthropic.html)、Dealroom：[https://dealroom.co/news/150366-anthropic-alleges-moonshot-routed-some-kimi-user-requests-to-claude-then/](https://dealroom.co/news/150366-anthropic-alleges-moonshot-routed-some-kimi-user-requests-to-claude-then/)。すべて競合に対する Anthropic の申し立てで、独立した裁定はない。
- Salesforce, "Agentforce job-ready AI agents" (2026年九月11日): [https://www.salesforce.com/uk/news/stories/agentforce-job-ready-ai-agents/](https://www.salesforce.com/uk/news/stories/agentforce-job-ready-ai-agents/) --- 長期ランタイム（メモリ、永続実行、動的ステアリング）、2026年十一月一般提供予定で試験中の Hunter、Multi-Agent Orchestration の一般提供。二次情報：unite.ai：[https://www.unite.ai/salesforce-debuts-job-ready-agentforce-agents-and-long-horizon-runtime/](https://www.unite.ai/salesforce-debuts-job-ready-agentforce-agents-and-long-horizon-runtime/)。数週間の目標追求は Salesforce の主張で、独立したベンチマークはなく、実証役も未一般提供。
- 第14章の存続ゲート、2026年九月15日確認。一次証拠はすべて同章の情報源欄に完全な形で掲載する。Anthropic、"How we built our multi-agent research system"（2025年六月13日）：[https://www.anthropic.com/engineering/multi-agent-research-system](https://www.anthropic.com/engineering/multi-agent-research-system)。OpenAI Codex の [#28792](https://github.com/openai/codex/pull/28792)（2026年六月19日マージ）と [#29324](https://github.com/openai/codex/pull/29324)（2026年六月22日マージ）、初公開は [rust-v0.142.0](https://github.com/openai/codex/releases/tag/rust-v0.142.0)（2026年六月22日）。Graph Engineering Mastery：[https://graphengineerings.com/](https://graphengineerings.com/) と [https://graphengineerings.com/course/module-2.html](https://graphengineerings.com/course/module-2.html)。SmartScope（2026年九月1日）：[https://smartscope.blog/en/blog/graph-engineering-loop-engineering-logic-review/](https://smartscope.blog/en/blog/graph-engineering-loop-engineering-logic-review/)。Nhu Hoang、Towards Data Science（2026年九月14日）：[https://towardsdatascience.com/graph-engineering-for-ai-agents-from-prompts-and-loops-to-workflows/](https://towardsdatascience.com/graph-engineering-for-ai-agents-from-prompts-and-loops-to-workflows/)。AgentEng London 2026：[https://agentengineering.world/london/](https://agentengineering.world/london/)。`headcount`（2026年八月28日作成）：[https://github.com/cbrock84/headcount](https://github.com/cbrock84/headcount)。ゲートの集計規則は七月の本文で未指定だったため、暗黙にせず第14章14.7節で明示する。

---

*前の章: [第 10 章 — 実世界のナレッジ Harness を作る](10-case-study.md)*
