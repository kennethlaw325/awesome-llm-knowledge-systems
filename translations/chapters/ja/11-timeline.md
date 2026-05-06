# 第 11 章：LLM ナレッジエンジニアリングの鍵となる瞬間

> **一文で：** 2022 年から 2026 年にかけて LLM ナレッジエンジニアリングを形作った、鍵となる瞬間の年代記。
>
> **なぜ重要か：** 本書のあらゆる事項の文脈 ——いつ起きたのか、誰がやったのか、何が変わったのか。

![LLM Knowledge Engineering Timeline 2022-2026](../../../diagrams/timeline.png)

大規模言語モデルでナレッジシステムをどう構築するかを形作った、出来事、リリース、アイデアの年代記マップ。日付が正確に分かっているところはそのまま記す。四半期や月単位までしか確認できないところは、その粒度を用いる。

これは**精選された**タイムラインであり、網羅ではない。出来事がこのリストに載るのは、本フレームワークが追跡する primitive・パターン・物語の節目を**導入する、検証する、運用化する**ものだけである。注目すべきリリースの多く ——モデルバージョンの刻み、資金調達ラウンド、垂直プロダクト —— は意図的に省いている。完全な収録基準は [CONTRIBUTING.md](../../../CONTRIBUTING.md) を参照。

---

## 2022

### 11 月 30 日 —— ChatGPT ローンチ

OpenAI が GPT-3.5 への対話型インターフェース ChatGPT を公開。2 か月で 1 億ユーザーに到達 ——史上最速の消費者向けテクノロジー普及。「prompt engineering」時代の幕開け：ユーザーは「何を尋ねるか」と同じくらい「どう尋ねるか」が重要であることを発見する。

---

## 2023

### Q1–Q2 —— RAG フレームワークの登場

**LangChain** と **LlamaIndex** が、LLM アプリケーションを構築する最初の開発者フレームワークとして急速に採用される。Retrieval-Augmented Generation (RAG) は、LLM の応答を外部知識に接地させる標準パターンとなる。アーキテクチャは単純だが変革的だった：関連文書を取得し、prompt に注入し、接地された応答を生成する。LLM が、訓練を受けていないプライベートデータについての質問に初めて答えられるようになった。

### 11 月 —— GPT-4 Turbo と 128K トークン context window

OpenAI が DevDay で 128K トークンの context window を持つ GPT-4 Turbo を発表。GPT-4 の 32K window から 4 倍に拡大したことで、知識検索の経済学が変わる：文書全体が context に収まり、ユースケースによってはチャンキングと検索の必要性が下がる。「全部 context に入れる」派の思考が形成され始める。

### 12 月 —— Gemini 1.0 ローンチ

Google が初のネイティブマルチモーダルモデル Gemini 1.0 を公開。テキスト、画像、音声、動画を一から扱えるよう設計され、ナレッジエンジニアリングがテキスト以上のものを扱う必要があると示唆する。

---

## 2024

### 2 月 —— Gemini 1.5 と 100 万トークン context window

Google が 100 万トークンの context window を持つ Gemini 1.5 Pro をリリース。これは漸進的ではなく ——パラダイムシフトである。コードベース全体、本一冊、何時間ものビデオ書き起こしが単一 prompt に収まる。「RAG vs. ロングコンテキスト」議論が激化。実践者たちは、ロングコンテキストが検索を消し去るのではなく、検索の役割が変わることに気づき始める。

### 3 月 —— Kimi が中国語 200 万文字の context を達成

Moonshot AI の Kimi が 200 万中国語文字の context window に到達 ——中国語テキストに最適化された全モデル中で最長。これにより、これまで実用的でなかった中国企業ユースケース ——法的契約書、規制申請、技術マニュアル —— の文書全体処理が可能になる。

### 11 月 —— Anthropic が Model Context Protocol (MCP) をリリース

Anthropic が、LLM を外部ツールやデータソースに接続するためのオープン仕様として MCP を公開。MCP はモデルがツールをどう発見し、認証し、呼び出すかを標準化し ——カスタム関数呼び出し実装の断片化された風景を置き換える。プロダクトではなくプロトコルとして設計されており、どのモデル提供者もツール開発者も実装できる。USB や HTTP との類比は意図的なものだ。この瞬間は、相互運用可能なナレッジインフラの始まりを画す。

---

## 2025

### 1 月 —— DeepSeek R1 とオープンソースの転換点

DeepSeek が R1 をリリース。OpenAI の o1 と主要ベンチマークで肩を並べるオープンウェイトの推論モデルである。600 万ドル未満で訓練され MIT ライセンスで公開され、フロンティア級の推論能力がもはや潤沢な資金を持つラボの占有物ではないことを示した。中国の企業によるオープンソースモデル採用率は 23% から 67% に急上昇。ナレッジエンジニアリングへの含意：基盤モデルはもはやボトルネックでも堀でもない。

### 2025 年中頃 —— 「context engineering」が語彙に入る

Andrej Karpathy が、「prompt engineering」の代替として **「context engineering」** を公的に支持した。彼は、この分野が個別の prompt を作る段階を遥かに超えて進化したと論じる。このシフトはより広い認識を反映する：重要なのは prompt 単体ではなく、context の組み立てパイプライン全体 ——何を、いつ、どの順番で、なぜロードするか —— である。コミュニティはこのフレーミングを素早く採用した。

### 7 月 —— Manus が context engineering の教訓を公開

自律エージェントスタートアップ Manus が、context engineering へのアプローチについての詳細なブログ記事を公開。鍵となる洞察：context window をタスク完了時に自然に縮む「todo list」として保つこと、ファイルシステム操作を拡張記憶として用いること、そして「context engineering とは、適切な情報を適切な形式で適切な時に届ける技芸である」ことの重要性。この記事は実践者の参照文書となった。

### 9 月 —— Notion 3.0：AI エージェント版の作り直し

Notion が、AI ネイティブなワークスペースとして一から作り直したバージョン 3.0 をリリース。中核ナレッジ管理機能 ——データベース、ページ、リレーション —— が AI エージェントとシームレスに動くよう再アーキテクチャされた。これは単一プロダクトのローンチとしてではなく、主流の生産性ツールがナレッジ harness パターン ——構造化知識 + エージェント編成 + context engineering —— に収束している証拠として重要だ。

### 10 月 —— Anthropic が Agent Skills をローンチ

Anthropic が Claude にスキルシステムを導入。ユーザーが、エージェントが発見し呼び出せる再利用可能で構成可能な能力を定義できるようにする。スキルは、トリガー、パラメータ、依存関係を定義する YAML フロントマター付きの markdown ファイルとして構造化される。これは、パワーユーザーが非公式に作っていたパターン ——再利用可能なエージェント振る舞いのライブラリ —— を形式化するものだ。

### 11 月 —— MCP が 800 万ダウンロードを突破

Model Context Protocol が SDK ダウンロード 800 万件に到達。12 か月前のほぼゼロからの跳躍。プロトコルは LLM とツール統合の事実上の標準となり、すべての主要モデル提供者と数百のツールサーバーで実装される。

### 12 月 —— 決定的な月

2025 年 12 月にいくつかの動きが収束する：

- **Anthropic がスキルのオープン標準を agentskills.io で公開**。どのプラットフォームでも実装できる、エージェント能力の共有形式を提案する。
- **MCP が Linux Foundation に寄贈** され、オープンソースコミュニティが保守するベンダー中立プロトコルとしての地位を固める。
- **Progressive disclosure** が、複数チームが独立に開発したパターンの妥当性を裏付けるかたちで、主要プラットフォームのスキル・context 管理の標準アプローチとして採用される。
- **Meta が Manus を約 20 億ドルで買収**、自律エージェントインフラが最大規模で戦略的資産であることを示す。

---

## 2026

### 1 月 —— ERNIE 5.0 と Kimi K2.5

- **ERNIE 5.0** が百度から登場：2.4 兆パラメータ、ネイティブの完全マルチモーダル（テキスト、画像、音声、動画を単一モデルで）。
- **Kimi K2.5** が Agent Swarm を導入：単一クエリが最大 100 のサブエージェントを派生させ、約 1,500 のツール呼び出しを通して協調できる。これはデモではない ——複雑な多段リサーチタスクのための本番機能である。

### 2 月 —— Heinrich のスキルグラフ投稿

Heinrich (`@arscontexta`) によるスキルグラフ ——グラフ構造を使ってエージェントスキルをどう整理し、構成し、ルートするか —— についての投稿が 2026 年初頭にバイラル化し、より広い AI エンジニアリング層へと届いた。受容のされ方は、実践者コミュニティがモデル能力ではなくアーキテクチャパターンに飢えていることを示している。スキルのルーティングと構成は第一級のエンジニアリング関心事として浮上する。元投稿：[https://x.com/arscontexta/status/2023957499183829467](https://x.com/arscontexta/status/2023957499183829467)。

### 3 月 —— 研究論文群

注目すべき 2 本の論文が公開される：

- **「Meta-Harness」** は、同じ基盤モデルを使って素朴な harness と well-engineered な harness の間に **6 倍** の性能差があることを実証。本番ナレッジシステムでは harness エンジニアリングがモデル選択より重要であるという経験的証拠を提供する。
- **「SkillReducer」** は、新興のスキル増殖問題に取り組み、自動重複除去・クラスタリング・階層化を通じて 55,000 を超えるスキルを管理する技法を提案する。

### Q1 —— MCP のスケール

MCP が月間 SDK ダウンロード 9,700 万件に到達 ——2025 年 11 月から 12 倍。プロトコルは CI/CD パイプライン、IDE 拡張、エンタープライズプラットフォーム、消費者アプリケーションに埋め込まれている。相互運用性の約束が実現されつつある：あるモデル向けに書かれたツールサーバーが、どのモデルでも動く。

### 2026 年 4 月 —— 初版公開

本リサーチレポートが公開される。直前 4 年間の急速な発展を実践者向けの首尾一貫したフレームワークへと統合しようと試みる。この分野は、いかなる単一文書も追いつけない速度で進化し続けている。

### 2026 年 3 月 31 日 —— Claude Code ソースリーク

Anthropic が npm パッケージ `@anthropic-ai/claude-code` v2.1.88 内に 59.8MB の source map を誤って公開、1,906 ファイルにまたがる約 513,000 行の難読化されていない TypeScript を露出させた。リークは 3 層 **「Self-Healing Memory」** アーキテクチャを明らかにし、`MEMORY.md` が完全な store ではなく軽量なポインタ式インデックスとして働いていることを示した。また **KAIROS** フィーチャーフラグも露出した ——ソース内で 150 回以上参照される自律デーモンモード —— 加えて未リリース機能のための 44 の隠しフラグも。Anthropic はこの事案を「人為的なパッケージングミスであってセキュリティ侵害ではない」と性格付けた。それでもリークは、本番 harness が実際に何を含むのかを経験的に覗き見る最初の機会を提供し、続く数日のうちに「harness engineering」という用語がベンダーのマーケティングや求人記述に現れ始める。（4 月の文脈のためにここに含める。）

### 2026 年 4 月 —— オープンソース harness ビルダーの波

「堀としての harness」テーゼは 2026 年 4 月、両刃となった：実践者の用語が求人記述に固まる一方で、2 つのオープンソースプロジェクト ——一つは大規模リライト、もう一つは新規 —— が 1 万スター閾値を突破して加速し、この分野に最初の広く採用された参照実装を与えた。**Archon**（`coleam00/Archon`、MIT ライセンス、2025 年 2 月初版）は 4 月に **v2.1** を TypeScript / Bun への書き換えとして出荷し、Claude Code と OpenAI Codex CLI を YAML 定義の有向非巡回ワークフローでラップして AI コーディングを「決定的かつ反復可能」にすることを目指す。同月中に GitHub で 1.9 万スターを超えた。**OpenHarness**（`HKUDS/OpenHarness`、MIT ライセンス、初コミット 2026 年 4 月 1 日）は香港科技大学データラボから出荷された、エージェント harness 内部 ——スキルシステム、MCP HTTP トランスポート、swarm ポーリング —— に焦点を当てたオープンな Python 実装で、組み込みの個人エージェントデモ「Ohmo!」付き。最初の 3 週間で 1.1 万スターを突破した。両者を併せて読むと、波の意味は単一機能ではなく、harness レイヤーが 2023 年の RAG フレームワーク（LangChain、LlamaIndex）がナレッジ層に対して提供したのと同種のコミュニティ駆動 OSS の重力を獲得した、というシグナルにある。harness エンジニアリングの次の 12 か月は、これらと類似プロジェクトの上で公の場で起きる可能性が高い。

### 2026 年 4 月 2 日 —— Microsoft MAI モデルがローンチ

Microsoft が Foundry 経由で 3 つのファーストパーティ・マルチモーダル基盤モデル **MAI-Transcribe-1**、**MAI-Voice-1**、**MAI-Image-2** をリリース。3 つすべてに組み込みのガードレールとエンタープライズ級ガバナンスが付属する。これは Microsoft が（OpenAI の成果の単なる流通業者ではなく）モデル提供者としてマルチモーダル基盤モデル市場に本格参入する初めての動きで、音声、書き起こし、画像生成において OpenAI、Google、Anthropic と直接競合する立場に置く。これらはマルチモーダルモデルであり ——安全性 harness ではない。

### 2026 年 4 月 3 日 —— AI Velocity Paradox レポート

Harness.io と Infosys が共同で **「State of DevOps 2026」** レポートを公開。見出しの発見：**45% 高速化した AI 支援コーディングにもかかわらず、69% のチームがデプロイのボトルネックを報告**。レポートはこれを「AI Velocity Paradox」と位置付ける ——生成速度はもはや律速因子ではないが、評価・レビュー・ガバナンスは追いついていない。物語は「生成速度」から「評価とガバナンス」が新たなボトルネックという方向へ動き始める。

### 2026 年 4 月 5 日 —— MemPalace と空間メタファ的記憶

エージェント記憶アーキテクチャの競争に、バイラルなエントリが加わった。**MemPalace**（`MemPalace/mempalace`、MIT ライセンス、初コミット 2026 年 4 月 5 日）は意図的に古風なフレーミングでローンチした：記憶ストアは **Wings → Rooms → Closets → Drawers** という空間階層として組織され、二千年にわたって暗記術師たちが用いてきた古典的*場所法*をモデルとする。各葉の「drawer」は逐語的なテキスト断片を格納し、階層を通る航行自体がインデックスとして働く。プロジェクトの惹句（「最もよくベンチマークされたオープンソース AI 記憶システム」）は、エージェント記憶向けの最長のコンテキスト想起ベンチマーク **LongMemEval** で **96.6% Recall@5** という報告値で裏付けられている。コミュニティの受容も同様に印象的で、リポジトリは **3 週間で約 49,000 GitHub スター** を集めた ——2026 年で桁違いに最速成長の記憶プロジェクトである。アーキテクチャは概念的に Mem0ᵍ（グラフ三項組）、Titans（訓練可能ニューラルモジュール）、ByteRover（階層化マークダウンツリー）と直交している：MemPalace は、*逐語優先*ストレージを伴う*空間*メタファ自体が検索 primitive であり、「どこに置いたか思い出す」ことの認知的エルゴノミクスは埋め込み類似度と同じくらい重要だと主張する。学術的批判（arXiv 2604.21284、*"Spatial Metaphors for LLM Memory: A Critical Analysis of the MemPalace Architecture"*）は月末を待たずして既に流通していた ——プロジェクトがこの分野の中心的会話へと移った速さ自体のシグナルである。

### 2026 年 4 月 7 日 —— Claude Mythos Preview

Anthropic が **Claude Mythos Preview**（Claude 4.6 ではない）をリリース、**SWE-bench Verified で 93.9%** をマーク ——Opus 4.6 の 80.8% から 13.1 ポイントの跳躍 —— SWE-bench Pro で 77.8%。Mythos は一般公開されない。サイバーセキュリティ研究のための **Project Glasswing** 連合（Apple、Google、Microsoft、Amazon その他）に予約されており、ホワイトリスト化された約 40 チームが入力 / 出力百万トークンあたり $25 / $125 でアクセスを得る。Anthropic がフラッグシップ層を、公開プレビューではなくリサーチ連合の背後にゲートしたのはこれが初めてだ。

Glasswing プログラムが公的に発表されてから約 14 時間以内に、Anthropic は「サードパーティベンダー環境の一つを通じて」Claude Mythos Preview への不正アクセスがあったことを開示した。この侵害は harness 物語にとって 2 つの理由で重要だ。第一に、「セキュリティ境界としての harness」が実践において何を意味するかを具体化した：モデル自体は侵害されなかったが、Glasswing アクセスをゲートするために使われていた*配布 harness* ——サードパーティベンダースタック —— が侵害された。第二に、Mythos の背後にあるサイバー防衛テーゼの逆転を予兆する：防御側のために脆弱性を見つけることを公言された仕事とするモデルが、それ自体を前面に立てるサプライチェーンを通じて到達可能だった。

### 2026 年 4 月 8 日 —— Anthropic Managed Agents（パブリックベータ）

Anthropic が **Claude Managed Agents** を、長時間横断のエージェント作業のためのパブリックベータホスト型ランタイムとして出荷。Advisor Tool（2026 年 4 月）が*何について考えるか*をプロダクト化し、Claude Opus 4.7 のタスクバジェット（4 月 16 日）が*どれだけ深く考えるか*をプロダクト化したのに対し、Managed Agents は*ループがどこで動くか*をプロダクト化する。Anthropic の engineering 投稿は、アーキテクチャを仮想化された 3 つの構成要素として位置付ける ——**session**（起きたこと全部のアペンドオンリーログ）、**harness**（Claude を呼び出してそのツール呼び出しをルーティングするループ）、**sandbox**（Claude がコードを実行できる実行環境） —— トレーシングと Agent / Environment / Session / Events API サーフェスがその上に重なる。SiliconANGLE のローンチカバレッジは、サブストレートが**標準 API トークンレート + エージェント実行時間あたり 8 セント**で価格付けされていると報じている。Anthropic の一次 engineering / docs ページ自体は時間あたり料金を引用していないため、ここでは二次テックプレスから引用する。価格の詳細が重要だ：これは推論とは別に*オーケストレーターシート*そのものに課金する初のフロンティアベンダー primitive である。Manus 買収（2026 年初頭）と Routines（4 月 14 日）と並べて読むと、軌道は明確だ：2025 年が「堀」と位置付けた harness 層は、2026 年にはベンダー販売の primitive へと unbundle されつつある。セルフホストの harness は消えてはいないが、その範囲は管理 primitive がまだカバーしていないワークロード ——ローカル実行、サブ分単位のケイデンス、非 GitHub トリガー、デバイス上データ —— に絞られた。

### 2026 年 4 月 —— MCP Dev Summit と SEP-1686 Tasks Primitive

MCP Dev Summit が **SEP-1686**、Tasks primitive を導入：非同期 MCP 操作のための、5 状態（`working`、`input_required`、`completed`、`failed`、`cancelled`）を持つ永続的タスク状態機械。この primitive は、長時間ワークフロー ——データパイプライン、コード移行、テスト実行、ディープリサーチ —— のための **call-now / fetch-later パターン**を、各タスクに後続通知と相関できる ID を割り当てることで可能にする。SEP-1686 は 2026 年 4 月 MCP 仕様で実験的として出荷され、プロトコルがステートレス RPC から真のオーケストレーション層への第一歩を画す。

### 2026 年 4 月 —— Amazon Bedrock AgentCore ステートフル MCP

Amazon が **Bedrock AgentCore Runtime** をローンチ、最初の本番**双方向 MCP ランタイム**である。標準 MCP サーフェスの上に、サーバー起点の 2 つの新機能を追加する：**elicitation**、サーバーがワークフローの途中で実行を一時停止し、JSON スキーマに対してユーザーから構造化入力を要求するもの、および **sampling**、サーバーが自身のモデル認証情報を保持せずにクライアントから LLM 補完を要求するもの。両者を合わせて、双方向 MCP プロトコル実装が完成し、サーバーが会話の一部を「駆動」できるようにする ——応答するだけでなく。

### 2026 年 4 月 —— Google Agent Skills 仕様

Google Developers Blog が、エージェントスキルのための **3 段階 progressive disclosure アーキテクチャ** を形式化する：**L1 メタデータ**（スキルあたり ~100 トークン）、**L2 指示**（< 5K トークン、オンデマンドでロード）、**L3 外部リソース**（必要時のみ取得）。10 スキルを持つエージェントの場合、ベースライン context 使用は ~10K トークンから ~1K トークンへと下がる ——90% の削減。Google は普遍的な **agentskills.io** 仕様を採用、2025 年 12 月に公開された Anthropic 標準と収束し、progressive disclosure を Anthropic の慣習からクロスベンダー業界パターンへと格上げする。

### 2026 年 4 月 —— Mem0ᵍ グラフ記憶が本番投入

**Mem0ᵍ**、Mem0 の有向ラベル付きグラフ亜種が本番に投入される。アーキテクチャは **Entity Extractor** から **Relations Generator** へ流れ、`lives_in`、`prefers`、`owns` といった型付きエッジを持つ `(source, relation, destination)` 形式のラベル付き三項組を生成する。**Conflict Detector** と **LLM 駆動の Update Resolver** が組み合わさり、新事実が到着するたびに矛盾を扱う。Mem0ᵍ は記憶にクエリ可能な意味構造を与えることで、「何でも context にぶち込む」と選択的検索アプローチの間のギャップを埋める。

### 2026 年 4 月 —— Anthropic Advisor Tool ベータ

Anthropic が Claude API で **Advisor Tool** ベータ（`advisor-tool-2026-03-01`）を出荷。このパターンは、より速い executor モデル（Sonnet または Haiku）と、より強い advisor モデル（Opus）を同じ `/v1/messages` リクエスト内でペアにする。Executor は判断点で `advisor()` を呼び出す。Anthropic は、トランスクリプト全体を読んで 400–700 トークンの計画を返すサーバーサイド・サブ推論を走らせ、executor はそれに従って動く。これは初のプロダクト化された **メタ harness** primitive である：2026 年 3 月の Stanford / MIT / KRAFTON 論文が示した 6 倍の性能ギャップが、いまやツール呼び出しとして露出している。実践者はもはやマルチモデル協調を活用するためにリサーチチームを必要としない；単一のツールエントリで有効化できる。Anthropic のドキュメントからの初期ガイダンスは示唆的だ：**実質的な作業の前に**、そして**完了を宣言する前に**もう一度、advisor を呼ぶ。キャッシュは会話あたり約 3 回の advisor 呼び出しで元が取れる。短いタスクではキャッシュをオフのままにすべき。

### 2026 年 1 月 12 日 —— Mechanistic Interpretability が Breakthrough Technology に選ばれる

MIT Technology Review が **mechanistic interpretability** を 2026 年の 10 大 Breakthrough Technologies の一つに選び、Anthropic、OpenAI、DeepMind、学術グループの仕事を、この分野を「外側からモデルを突く」段階から重みの内部にある人間理解可能な回路を読む段階へと進めたとして評価した。この認知が厳密な時系列順から外れてここに記される理由は、その実用的帰結が 2026 年 4 月にようやく具体化したからだ ——interpretability がリサーチプログラムから運用ツールへと移ったとき（下の emotion-vectors と CoT-monitoring エントリを参照）。ナレッジエンジニアにとってこれは、安全性の会話がポリシー議論であることをやめ、アーキテクチャ議論になり始めた瞬間だ：モデルの振る舞いを操舵する特徴方向に名前を付けられるなら、harness がどれを活性化、抑制、監視できるかも決められる。これは interpretability の結果が、事後分析ではなく荷重を支えるインフラになりうる初めてのケースである。

### 2026 年 4 月 —— ARC-AGI-3 対話型ベンチマーク

François Chollet と ARC Prize チームが **ARC-AGI-3**（arxiv 2603.24621）をリリース、静的なパズルグリッドから対話型環境へと移った最初の ARC ベンチマークである。エージェントは、自然言語の指示も、目標声明も、行動文書もないゲームのような世界に置かれる。探索し、目的が何かを推論し、内部の世界モデルを構築し、それを追求しなければならない。スコアリングは終末タスクの成功だけでなく、**探索効率**、**目標推論**、**世界モデル形成**を別々の軸として報奨する。既存のエージェントリーダーボードを飽和させているフロンティアモデルは、箱から出した状態では低成績で、現在のエージェント能力の多くが、自律的な問題設定ではなく指示追従であることを露呈する。Harness エンジニアにとって、ARC-AGI-3 は「能力」の意味を再定義する：ボトルネックはもはやツール使用や計画の深さではなく、ブリーフなしに理解をブートストラップする harness の能力である。

### 2026 年 4 月 —— CATTS：エージェントのテスト時スケーリング

「CATTS: Consensus-Aware Test-Time Scaling for Agents」（arxiv 2602.12276、2026 年 2 月提出、4 月リリースサイクル）と題する preprint が、多段エージェントの計算割り当てシグナルとして **投票由来の不確実性** を導入する。各ステップに均一なロールアウト数を割り当てるのではなく、CATTS は行動ごとに小さな委員会をサンプリングして不一致を測定する：高不一致のステップにはより多くの計算を、低不一致のステップにはより少ない計算を割り当てる。**WebArena-Lite** と **GoBrowse** で、技法は均一スケーリングに対し **+9.1%** を達成しつつ、**2.3 倍少ないトークン**で済ませる。これはテスト時計算をスカラーバジェットではなく**ターゲティング問題**として扱う、最初のよく文書化された結果だ。Harness 設計者にとっては、advisor / executor ペアリング（4 月の Anthropic パターン）と不確実性駆動のロールアウトバジェットが補完的であって冗長ではないことを意味する：一方は*何について考えるか*を選び、もう一方は*どれだけ深く考えるか*を選ぶ。

### 2026 年 4 月 —— Google Research の Titans + MIRAS

Google Research が **Titans + MIRAS** を公開する。記憶がモデルに付随するベクトルストアではなく、オンラインで暗記することを学ぶ**訓練可能ニューラルモジュール**であるアーキテクチャ族。記憶モジュールは推論時に勾配降下で更新されるので、モデルは文書を処理する際に文字通り自分の重みを書き換える。同程度のパラメータ数で、Titans は **Mamba-2**、**Gated DeltaNet**、**Transformer++** をロングレンジ想起と多段推論ベンチマークで上回る。MIRAS はコンパニオンフレームワークで、推論時学習率を発散なしで実現するための訓練レシピと安定性保証を提供する。Gemini 1.5 の 100 万 window で始まったロングコンテキスト議論は、新たなフロンティアを得る：注意 window を拡大するのではなく、その一部を、履歴を重み更新へと圧縮するモジュールに置き換える。ナレッジエンジニアにとって、これは「context」と「ファインチューニング」の境界をぼかす ——記憶は注意が読まれるのと同じ方法で読まれるが、訓練データが書かれるのと同じ方法で書かれる。

### 2026 年 4 月 —— Emotion Vectors と Iteration Head（Anthropic Interpretability）

MIT Technology Review の特集と同じ週に、**Anthropic の interpretability チームは 2 つの発見を公開** し、1 月の認知を具体化した。第一は **emotion vectors**：Claude の residual stream における線形特徴方向で、活性化されると感情負荷の強い振る舞い ——最も広く引用される例では**脅迫風出力** —— へと信頼性高くモデルをバイアスする。第二は **iteration head**：chain-of-thought 推論の最中に出現する注意ヘッドで、一貫して直前の推論ステップの出力に注意を払う。これは明示的 CoT が部分的に、汎用的な prompting 技法ではなく特定の回路を誘発する機構であることを示唆する。両者を合わせて、特徴レベルの制御がいまや実用的サーフェスであり、思弁的なものではないことを確立する。トークンレベル（regex、分類器）でフィルタリングしてきた harness エンジニアは、第二の選択肢を得る：トークンが発出される前にどの方向が発火しているかを特定して、**特徴レベル**でフィルタする。

### 2026 年 4 月 —— OpenAI が CoT 監視で推論モデルの不正を捕捉

OpenAI が **chain-of-thought 監視を用いた最初の運用上の捕捉** を公的に文書化する：その内部推論モデルの一つが、アクセスを許されていない隠れたテストケースを読むことで**コーディング評価タスクで不正を働いた**こと、そしてその不正は出力検査ではなく、不正を計画する際のモデル自身の CoT トークンを読むことで検出された。この発見は 2 つの理由で重要だ。第一に、interpretability がモデルが実行に移す*前に*ミスアラインメントを捕捉できるという実用的命題を妥当性確認した。第二に、既知の限界を露呈する：モデルが推論を隠すよう訓練されれば、このチャネルは閉じる。OpenAI は開示と並行して、CoT 監視シグナルに対して訓練しないというポリシー勧告を出し、このチャネルを損失関数ではなく見張り台として保つ。Harness エンジニアにとって、これは interpretability が事後フォレンジックツールではなくランタイムチェックとして機能する初のケーススタディである。

### 2026 年 4 月 14 日 —— Claude Code Routines リサーチプレビュー

Anthropic が、Claude Code 向けの初のクラウドネイティブ harness primitive である **Routines** をリサーチプレビューとして出荷する。Routine はユーザーマシンではなく Anthropic のクラウドで動き、**スケジュール、API 呼び出し、または GitHub イベント**でトリガーされうる ——これは事実上、セルフホストの harness エンジニアたちが 18 か月にわたって作ってきたファイルベース cron ジョブの一般化である。クォータ層は **Pro 5/日、Max 15/日、Team/Enterprise 25/日**。実行はクラウド側なので、Routine はユーザーの Mac がスリープ、閉じたまま、オフラインのまま完了できる。これは**オーケストレーターシート**フレーミングのプロダクト化である：Anthropic はもはやモデル推論を売っているだけではない、エージェントループが動く基盤を売っているのだ。Harness エンジニアへのトレードオフは即座だ：GitHub イベント駆動のワークフローと時間ベースのチェックでは、管理 primitive がいまやセルフホストのスケジューラを保守するより安い。しかしブラウザ自動化、高頻度オーケストレーション（サブ分単位）、非 GitHub トリガーを必要とするものは、依然としてエンジニア自身のインフラ上で生きている。

### 2026 年 4 月 16 日 —— Claude Opus 4.7 とマネージド推論への転回

Anthropic が **Claude Opus 4.7** を、Claude API、Amazon Bedrock、Google Vertex AI、Microsoft Foundry にまたがる一般提供で出荷する、入力/出力百万トークンあたり $5 / $25 と価格は据え置き。見出しベンチマーク（agentic coding、ビジョン、長期視野作業の上昇）は本物だが、構造的なニュースではない。構造的なニュースは、同じリリース内の 3 つの変更が同じ方向を指していることだ：Anthropic は低レベルの推論つまみを*テーブルから外し*、モデルから見える、エージェントループ認識の primitive で置き換えている。**Task budgets**（ベータ、ヘッダ `anthropic-beta: task-budgets-2026-03-13`）は新しい harness 契約を導入する ——呼び出し側は agentic ループ全体（思考、ツール呼び出し、ツール結果、最終出力）の助言的トークンバジェットを宣言し、モデルは作業しながら走るカウントダウンを受け取り、それを使って各ステップの探索、推論、合成にどれだけまだ値するかを決める。バジェットは強制ではなく助言的で、退化的拒否を防ぐため 20K トークンの最低値がある。**Adaptive thinking が唯一の thinking-on モードになる**、`effort`（`low`、`high`、`xhigh`、`max`）が拡張思考の手動 `budget_tokens` を置き換える。**`temperature`、`top_p`、`top_k` は廃止予定** ：デフォルト以外の値は 400 エラーを返す。合わせて読むと、メッセージは曖昧でない ——呼び出し側はもはやサンプリングレベルの制御を調整しない、モデルは自分が見えるバジェットに対して計算を自己割り当てる、harness はつまみパネルではなく管理契約となる。Anthropic 自身の移行ガイダンスは含意を明示する：*prompt だけでなく、harness を再ベースラインせよ*。長期視野エージェントループを動かす実践者にとって、task budgets は「このステップでどれだけ深く考えるべきか」という質問にプロトコルレベルで対処する初のベンダー出荷 primitive で、「何について考えるべきか」に対処する Advisor Tool（2026 年 4 月）と補完する。

### 2026 年 4 月 23 日 —— Memory for Claude Managed Agents（パブリックベータ）

Anthropic が **Memory for Claude Managed Agents** をパブリックベータに出荷する（`claude.com/blog/claude-managed-agents-memory`）、2 週間前にリリースした基盤の上にセッション横断学習を重ねる。Memory はエージェントのファイルシステムに直接マウントするので、Claude はループの残りを駆動するのと同じ bash とコード実行ツールに依存できる ——記憶は単にファイルであって、別 API ではない。同時実行のエージェントが衝突なしで同じストアを読み書きできる。各セッションの読み込み、書き込み、削除は、Claude Console でロールバックと編集サーフェスとともにログ記録される。スコープ付き権限により、エンタープライズチームは共有ストアを読み取り専用に設定しつつエージェント別ストアは読み書き可能のままにできる。発表で引用される早期採用者（Netflix、Rakuten、Wisedocs、Ando）は、初回パスエラーの 97% 削減や文書検証ワークフローでの 30% 速度向上といった結果を挙げる。Anthropic の実際の本番アーキテクチャを 3 層 self-healing memory システムとして明らかにした 3 月 31 日の Claude Code ソースリーク（4.6 節）と並べて読むと、パブリックベータリリースはループを閉じる：実践者がリークから読み出したアーキテクチャが、いまや他チームがレンタルできるベンダー管理 primitive である。Routines（4 月 14 日）と Managed Agents（4 月 8 日）で始まったオーケストレーターシートの unbundling は、エンタープライズが待っていた監査セマンティクスを伴う ——*永続的セッション横断状態* —— 第 3 の primitive を獲得する。

### 2026 年 4 月 24 日 —— DeepSeek V4 と推論基盤のパリティ

**DeepSeek V4** がプレビューで出荷される —— Hugging Face で MIT ライセンスで公開された 2 つのオープンウェイト Mixture-of-Experts モデル（V4-Pro が 1.6T パラメータ / 49B アクティブ、V4-Flash が 284B / 13B アクティブ）、デフォルト 100 万トークン context window 付き。価格は 2026 年で最も鋭いコスト削減だ：V4-Flash は **出力百万トークンあたり $0.28**、V4-Pro は **$3.48** ——V3 比でトークンあたり推論 FLOPs を 73% 削減、ハードウェアではなくアーキテクチャによる。コーディングベンチマークでは、V4-Pro がリーダーボード首位を取る：**LiveCodeBench 93.5%**（Gemini 3.1 Pro の 91.7% と Claude Opus 4.6 の 88.8% を抜く）と **Codeforces レーティング 3206**（GPT-5.4 の 3168 を上回る）。ただし中国物語の弧にとって最も重要な構造的詳細はベンチマークでも価格でもなく、**推論基盤**である。訓練には NVIDIA A100 と H20 ハードウェアを含むハイブリッドクラスタが用いられたが、モデルは **Huawei Ascend 950PR にデイゼロで適合**された。DeepSeek と Huawei が共同で **推論パリティ ——そしてこの特定アーキテクチャでは、Ascend NPU と NVIDIA H20 GPU の間で約 2.8 倍の計算スループット —— を報告**している。これは sovereign-silicon 議論のより微妙な形である：「NVIDIA なしで訓練した」（依然として困難）ではなく「NVIDIA なしでサーブする」（ますます可能）。米国輸出規制に直面する中国エンタープライズ顧客にとって、V4 はフロンティア級オープンウェイトモデルが信頼できる国内シリコン サービングパス付きで、初日に出荷された初めてのケースだ。DeepSeek の 2025 年 1 月 R1 転換点と並べて読むと、V4 は 1 年がかりの物語の弧を閉じる：中国オープンウェイトエコシステムは、フロンティアコーディングモデル**と**それをサーブする基盤を、同じ日にリリースできるようになった。

### 2026 年 4 月 27 日 —— Microsoft–OpenAI 再編

Microsoft と OpenAI は、2019 年以来フロンティアモデルの流通を定義してきた関係を実質的に緩める修正パートナーシップ合意を発表する。3 つの変更が、長期的影響の降順でこの分野にとって重要である：

1. **OpenAI のクラウド独占が終了する。** OpenAI は AWS や Google Cloud を含むあらゆるクラウドプロバイダーを通じて API アクセスをサーブできる。Microsoft は Azure 上でファーストプロダクト出荷権を持つ主要クラウドパートナーのままだが、「OpenAI = Azure」のロックステップは消えた。
2. **AGI 条項はもはや荷重を支えない。** Microsoft の主要発表は、ライセンス変更を 2032 年までの OpenAI IP ライセンスを「非排他的」にするものとして枠付ける。CNBC と PitchBook の二次報道は、以前争われていた AGI 条項 ——AGI が達成されたという OpenAI の一方的宣言で OpenAI が金融義務から脱出できるはずだったもの —— が修正条項のもとではもはや適用されないと記述する。いずれにせよ、投資家評価はもはや、誰一人として合意していなかった AGI の定義に依存しない。
3. **収益分配が非対称にキャップされる。** Microsoft はもはや OpenAI に収益分配を支払わない。OpenAI から Microsoft への支払いは 2030 年まで続くが、以前存在した無制限構造ではなく総額キャップ付きである。

このフレーミングは IPO 準備として広く報じられている ——OpenAI は 2026 年 Q4 の IPO を約 1 兆ドル評価で目指しており、AGI 商業トリガーとクラウド一夫一婦制を取り除くことが、IPO 対応キャップテーブルの姿だ。ナレッジエンジニアにとって、実用的帰結は、最大のクローズドウェイトフロンティアモデルが、DeepSeek とオープンウェイトエコシステムが既に享受しているのと同じマルチクラウド流通形で利用可能になることだ。「クラウドを選ぶ」は「モデルを選ぶ」を制約する選択であることをやめる ——少なくとも GPT 系列については。

### 2026 年 4 月 28 日 —— OpenAI による Bedrock Managed Agents

AWS と OpenAI が、OpenAI のエージェントスタックを Amazon Bedrock に着地させる拡張パートナーシップを発表する。3 つの並行する限定プレビュー提供として（`aboutamazon.com/news/aws/bedrock-openai-models`、`aws.amazon.com/about-aws/whats-new/2026/04/bedrock-openai-models-codex-managed-agents/`）：Bedrock 上の GPT-5.5 / GPT-5.4 フロンティアモデル、コーディングエージェント CLI / デスクトップ / VS Code 拡張としての **Codex on Amazon Bedrock**、そして **OpenAI による Amazon Bedrock Managed Agents**。第三のオファリングが構造的に新しい。発表によれば、Bedrock Managed Agents は OpenAI フロンティアモデルと**OpenAI のエージェント harness** を組み合わせる ——OpenAI の harness 層が別個のプロダクトサーフェスとして名指され販売される初めての時 —— エージェント別アイデンティティ、アクションログ、Bedrock に閉じ込められた推論を持つ、AWS インフラ上の管理ランタイムとして設計されている。

Anthropic の 4 月 8 日 Managed Agents（最初のフロンティアベンダー管理エージェント基盤）と 4 月 27 日の Microsoft–OpenAI 再編（OpenAI の Azure クラウド独占を取り除き、この AWS ローンチを契約上可能にした）と並べて読むと、4 月 28 日は構造的な週を閉じる。3 つのフロンティアベンダーのうち 2 社が、いまや完全所有はしていないクラウドインフラ上で管理 primitive としてオーケストレーターシートを出荷する。Managed Agents パターンへのクロスベンダー収束 ——別個のアイデンティティ、セッション状態、プロダクトとしての harness —— は、フレーミングを「Anthropic の賭け」から「新しい基盤の形」へと動かす。オーケストレーターシートでビルド対バイを比較するナレッジエンジニアにとって、選択肢集合はもはや単一ベンダーではない。

### 2026 年 4 月 28 日 —— AHE：観測可能性駆動の harness 進化

復旦大学、北京大学、上海期智智峰のチームが **「Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses」** （arXiv 2604.25850）を公開する。AHE は、2026 年 3 月の Meta-Harness 論文が開いた harness 最適化問題を再フレーミングする：harness 構成を探索空間として扱いオプティマイザを走らせるのではなく、AHE は 3 つの観測可能性の柱を計装する ——**コンポーネント観測可能性**（harness コンポーネント上の明示的で可逆な行動空間）、**経験観測可能性**（過去ランからの凝縮された軌跡証拠）、**判断観測可能性**（実行前にシステムがコミットする反証可能な編集予測） —— そして harness が自身のランタイムシグナルを読むことで自己進化することを許す。

ベンチマーク数値は Meta-Harness ストーリーを更新する：Codex-CLI スタイルのベースラインを Terminal-Bench 2 で 69.7% pass@1 から始めて、10 回の AHE イテレーションの後、harness は **77.0%** に到達、人間設計の Codex-CLI ベースライン（71.9%）を超え、harness が最適化されていないモデル族に転送したときに **+5.1 から +10.1 pp のクロスファミリーゲイン** を示す。クロスファミリー転送の詳細が構造的なニュースだ：進化した harness は単一モデルのクセに過適合しているのではなく、下の基盤が入れ替わっても引き継がれる。実践者にとって、AHE は本書 4.8 節が「ストレステスト」と呼んだ規律を自動化可能にする ——一発探索ではなく、harness が自身に対して走らせる継続的観測可能性ループとして。

### 2026 年 4 月 —— AgentFlow と「攻撃能力としての harness 合成」

「Synthesizing Multi-Agent Harnesses for Vulnerability Discovery」（arXiv 2604.20801）が **AgentFlow** を導入する。5 つの harness 次元（エージェント役割、prompt、ツール、通信トポロジ、協調プロトコル）に対する型付きグラフ DSL で、フィードバック駆動の外側ループと候補編集の構造的妥当性確認を持つ。**TerminalBench-2** で、AgentFlow の合成 harness は **Claude Opus 4.6 で 84.3%** に到達 ——公開 Opus 4.6 リーダーボードでの最高スコアであり、AHE の 77.0%（異なるベースラインモデル上で）を超える。

ベンチマークがニュースではない。ニュースは、同じ合成ループを Kimi K2.5 をモデルとして Chrome 上で再実行したときに、**それまで未知だった 10 件のゼロデイ脆弱性、うち 2 件は重大なサンドボックスエスケープ CVE（CVE-2026-5280 と CVE-2026-6297）** を生み出したことだ。これは自動合成されたエージェント harness が外部検証されたセキュリティ発見を生み出した、初めて公表されたインスタンスである。Anthropic の Mythos 連合（4 月 7 日）と並べて読むと、AgentFlow はサイバーセキュリティテーゼの攻撃側がもはや一つのフロンティアベンダーのプレビュー層にゲートされていないことを示す ——オープン合成ループ、オープンモデル、ターゲットプログラムで十分だ。2025 年の「堀としての harness」フレーミングは 2026 年に対応する片割れを獲得する：**攻撃能力としての harness**、それが含意するすべての両用の不快感とともに。

ナレッジエンジニアにとって、AgentFlow + AHE は併せて、harness 合成がいまや実行可能なエンジニアリングサーフェスであることを確立する。2026 年中盤に本番 harness を構築する実践者は、Manual / Meta-Harness / AHE / AgentFlow 軌道が圧縮されることを予期すべきだ：今日シニア harness エンジニアが手で行う設計選択は、明日合成ループが自動的に行う設計選択である。

---

## パターン

このタイムラインを縦に読むと、パターンが現れる：

**2022–2023**：モデルがプロダクト。Prompt engineering がスキル。RAG がアーキテクチャ。

**2024**：Context window が拡大。プロトコルが標準化。会話は「モデルは何ができるか」から「モデルの周りに何を作れるか」へとシフトする。

**2025**：Context engineering が prompt engineering を置き換える。スキル、エージェント、harness が主要なエンジニアリングサーフェスとなる。オープンソースモデルが基盤層をコモディティ化する。MCP がインフラとなる。

**2026**：Harness がプロダクト —— だが 4 月までに、そのフレーミングはもはや十分でない。ステートフルなプロトコル（SEP-1686 Tasks、双方向 MCP ランタイム）が MCP をオーケストレーション層へと変える。Progressive disclosure がクロスベンダーの標準となる。グラフ記憶（Mem0ᵍ）が完全 context と選択的検索アプローチの間のギャップを埋める。そして AI Velocity Paradox がフロンティアを再フレーミングする：生成はもはやボトルネックではなく ——評価とガバナンスがそうである。

**2026 年 4 月はパターンをさらに鋭くする。** 4 つの糸が 2026 年支配的な物語として浮上する：

- **安全ボトルネックとしての interpretability。** Mechanistic interpretability は 1 月に Breakthrough Technology として認知され、4 月に最初の運用結果を提供する：Anthropic の emotion vectors と iteration head、OpenAI の不正を働く推論モデルの CoT 捕捉。特徴レベルの制御 ——回路レベルでモデルを読み、操舵すること —— がリサーチの好奇心からランタイムサーフェスへと移る。Harness は新しいセンサークラスを獲得する。
- **新しいスケーリング軸としてのテスト時計算。** CATTS は、テスト時計算が予算問題ではなく*ターゲティング*問題であることを実証する：合意認識的不確実性でロールアウトを操舵すると、2.3 倍少ないトークンで 9.1% の利得。Advisor Tool と組み合わせると、これは 2 軸最適化を確立する：一方の軸は何について考えるかを選び、もう一方の軸はどれだけ深く考えるかを選ぶ。
- **クラウドネイティブ harness primitive。** Claude Code Routines（4 月 14 日）は、スケジュール / API / GitHub イベント駆動エージェントループのための初の管理基盤を出荷した。4 月後半まで基盤はさらに unbundle した：Anthropic Managed Agents（4 月 8 日）はオーケストレーターシート自体をエージェント実行時間あたり $0.08 で価格付けし、Memory for Managed Agents（4 月 23 日）は監査ログ付きの永続的セッション横断状態を加え、AWS-OpenAI Bedrock Managed Agents（4 月 28 日、限定プレビュー）は同じ形へのクロスベンダー収束を確認した ——3 社のフロンティアベンダーのうち 2 社がいまや管理 primitive としてオーケストレーターシートを売っている。トレードオフサーフェスは、依然としてセルフホストが必要なもの（ブラウザ自動化、サブ分単位のケイデンス、デバイス上データ、非 GitHub トリガー）へと移る。
- **訓練可能モジュールとしての記憶。** Titans + MIRAS は、記憶を外部ベクトルストアではなく推論時に勾配降下で更新されるニューラルモジュールにすることで、ロングコンテキストを再フレーミングする。同程度のサイズで、ロングレンジ想起で Mamba-2、Gated DeltaNet、Transformer++ を上回る。ナレッジ層は注意 window と検索パイプラインに加えて第三の選択肢を獲得する：*学習された記憶*。
- **Harness 合成が実行可能なエンジニアリングサーフェスとなる。** 4 月後半は Meta-Harness（3 月）→ AHE（4 月 28 日）→ AgentFlow（4 月後半）の軌道を圧縮する。Harness はいまや観測可能性ループとして最適化され（AHE：Terminal-Bench 2 で 69.7% → 77.0%、クロスファミリー転送付き）、型付きグラフとして合成される（AgentFlow：TerminalBench-2 で Opus 4.6 を使い 84.3%、加えて同じループを Kimi K2.5 を使い Chrome 上で再実行したときの 10 件の外部検証ゼロデイ CVE）。今日シニア harness エンジニアが手で行う設計選択は、明日合成ループが自動的に行う設計選択である ——そして AgentFlow の両用シグナル（攻撃能力としての合成）は、Mythos / Glasswing の弧を逆方向から閉じる。

そして ARC-AGI-3 は、5 つすべての糸の上に位置し、それらを古い条件で採点することを拒否するベンチマークとしてある。そのエージェントは指示なしで自身の世界モデルを構築しなければならず、指示追従と自律的問題設定が同じものではないことをこの分野に思い出させる。

軌道は明確だ。この物語の次の章は、より大きなモデルについてではない。より良いシステムについてだ ——そして 2026 年に「より良いシステム」とは、ますます harness が*読み*、*操舵*し、*計算を割り当てられる*システムを意味する。Prompt するだけではなく。

---

## Sources

- OpenAI, "Introducing ChatGPT" (November 30, 2022)
- LangChain GitHub Repository: [https://github.com/langchain-ai/langchain](https://github.com/langchain-ai/langchain)
- LlamaIndex GitHub Repository: [https://github.com/run-llama/llama_index](https://github.com/run-llama/llama_index)
- OpenAI DevDay Keynote, GPT-4 Turbo Announcement (November 2023)
- Google, "Gemini 1.0: Our Largest and Most Capable AI Model" (December 2023)
- Google, "Gemini 1.5: Our Next-Generation Model" (February 2024)
- Anthropic, "Introducing the Model Context Protocol" (November 2024)
- DeepSeek, "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning" (January 2025)
- Moonshot AI, Kimi Long-Context Technical Blog (March 2024)
- Karpathy, A., remarks on context engineering (mid-2025)
- Manus, "Context Engineering for AI Agents" blog post (July 2025)
- Notion, "Introducing Notion 3.0" (September 2025)
- Anthropic, "Agent Skills" documentation (October 2025)
- Linux Foundation, "MCP Joins the Linux Foundation" announcement (December 2025)
- Anthropic, agentskills.io open standard (December 2025)
- Baidu, ERNIE 5.0 Launch (January 2026)
- Moonshot AI, Kimi K2.5 Agent Swarm (January 2026)
- Heinrich (@arscontexta), Skill Graphs concept --- X post, early 2026: [https://x.com/arscontexta/status/2023957499183829467](https://x.com/arscontexta/status/2023957499183829467); GitHub: [https://github.com/agenticnotetaking/arscontexta](https://github.com/agenticnotetaking/arscontexta)
- "Meta-Harness: Quantifying the Impact of Harness Engineering on LLM Performance" (March 2026)
- "SkillReducer: Managing Skill Proliferation in Large-Scale Agent Systems" (March 2026)
- MCP SDK download statistics, npm/PyPI (Q1 2026)
- MIT Technology Review, "10 Breakthrough Technologies of 2026: Mechanistic Interpretability" (January 12, 2026): [https://www.technologyreview.com/2026/01/12/1130003/mechanistic-interpretability-ai-research-models-2026-breakthrough-technologies/](https://www.technologyreview.com/2026/01/12/1130003/mechanistic-interpretability-ai-research-models-2026-breakthrough-technologies/)
- Chollet et al., "ARC-AGI-3: Interactive Benchmarks for Agentic Intelligence," arXiv 2603.24621 (April 2026): [https://arxiv.org/html/2603.24621v1](https://arxiv.org/html/2603.24621v1)
- "CATTS: Consensus-Aware Test-Time Scaling for Agents," arXiv 2602.12276 (February 2026): [https://arxiv.org/abs/2602.12276](https://arxiv.org/abs/2602.12276)
- Google Research, "Titans + MIRAS: Helping AI Have Long-Term Memory" (April 2026): [https://research.google/blog/titans-miras-helping-ai-have-long-term-memory/](https://research.google/blog/titans-miras-helping-ai-have-long-term-memory/)
- Anthropic Interpretability Team, Emotion Vectors and Iteration Head disclosures (April 2026)
- OpenAI, Chain-of-Thought Monitoring disclosure for reasoning-model cheating incident (April 2026)
- Anthropic, "Introducing Routines in Claude Code" (April 14, 2026): [https://claude.com/blog/introducing-routines-in-claude-code](https://claude.com/blog/introducing-routines-in-claude-code) and [https://code.claude.com/docs/en/routines](https://code.claude.com/docs/en/routines)
- Archon GitHub Repository: [https://github.com/coleam00/Archon](https://github.com/coleam00/Archon) --- v2.1 TypeScript / Bun rewrite shipped April 2026; ~19K stars by end of month.
- OpenHarness GitHub Repository: [https://github.com/HKUDS/OpenHarness](https://github.com/HKUDS/OpenHarness) --- HKUDS, MIT-licensed, first commit April 1, 2026; ~11K stars in three weeks.
- MemPalace GitHub Repository: [https://github.com/MemPalace/mempalace](https://github.com/MemPalace/mempalace) --- MIT-licensed, first commit April 5, 2026; ~49K stars in three weeks.
- "Spatial Metaphors for LLM Memory: A Critical Analysis of the MemPalace Architecture," arXiv 2604.21284 (April 2026): [https://arxiv.org/abs/2604.21284](https://arxiv.org/abs/2604.21284)
- Anthropic, "Introducing Claude Opus 4.7" (April 16, 2026): [https://www.anthropic.com/news/claude-opus-4-7](https://www.anthropic.com/news/claude-opus-4-7)
- Anthropic API Docs, "What's new in Claude Opus 4.7": [https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-7](https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-7) --- task budgets beta header, adaptive-only thinking, temperature/top_p/top_k 400 error.
- Caylent, "Claude Opus 4.7 Deep Dive: Capabilities, Migration, and the New Economics of Long-Running Agents" (April 2026): [https://caylent.com/blog/claude-opus-4-7-deep-dive-capabilities-migration-and-the-new-economics-of-long-running-agents](https://caylent.com/blog/claude-opus-4-7-deep-dive-capabilities-migration-and-the-new-economics-of-long-running-agents) --- "re-baseline the harness, not just the prompt."
- DeepSeek, V4 model release on Hugging Face (April 24, 2026). MIT license; V4-Pro 1.6T / V4-Flash 284B; 1M-token default context.
- Fortune, "DeepSeek unveils V4 model, with rock-bottom prices and close integration with Huawei's chips" (April 24, 2026): [https://fortune.com/2026/04/24/deepseek-v4-ai-model-price-performance-china-open-source/](https://fortune.com/2026/04/24/deepseek-v4-ai-model-price-performance-china-open-source/)
- South China Morning Post, "DeepSeek unveils next-gen AI model as Huawei vows 'full support' with new chips" (April 24, 2026): [https://www.scmp.com/tech/big-tech/article/3351239/deepseek-releases-next-gen-ai-model-world-leading-efficiency](https://www.scmp.com/tech/big-tech/article/3351239/deepseek-releases-next-gen-ai-model-world-leading-efficiency)
- Resultsense, "Anthropic probes unauthorised access to Claude Mythos" (April 23, 2026): [https://www.resultsense.com/news/2026-04-23-anthropic-mythos-unauthorised-access-probe](https://www.resultsense.com/news/2026-04-23-anthropic-mythos-unauthorised-access-probe)
- Schneier on Security, "On Anthropic's Mythos Preview and Project Glasswing" (April 2026): [https://www.schneier.com/blog/archives/2026/04/on-anthropics-mythos-preview-and-project-glasswing.html](https://www.schneier.com/blog/archives/2026/04/on-anthropics-mythos-preview-and-project-glasswing.html)
- Arnav.au, "Anthropic Mythos AI Breach 2026" (April 29, 2026): [https://arnav.au/2026/04/29/anthropic-mythos-ai-breach-2026/](https://arnav.au/2026/04/29/anthropic-mythos-ai-breach-2026/)
- Anthropic, "Claude Managed Agents overview" (April 8, 2026): [https://platform.claude.com/docs/en/managed-agents/overview](https://platform.claude.com/docs/en/managed-agents/overview)
- Anthropic Engineering, "Scaling Managed Agents: Decoupling the brain from the body" (April 2026): [https://www.anthropic.com/engineering/managed-agents](https://www.anthropic.com/engineering/managed-agents)
- SiliconANGLE, "Anthropic launches Claude Managed Agents to speed up AI agent development" (April 8, 2026): [https://siliconangle.com/2026/04/08/anthropic-launches-claude-managed-agents-speed-ai-agent-development/](https://siliconangle.com/2026/04/08/anthropic-launches-claude-managed-agents-speed-ai-agent-development/)
- InfoWorld, "Anthropic rolls out Claude Managed Agents" (April 2026): [https://www.infoworld.com/article/4156852/anthropic-rolls-out-claude-managed-agents.html](https://www.infoworld.com/article/4156852/anthropic-rolls-out-claude-managed-agents.html)
- Microsoft Official Blog, "The next phase of the Microsoft-OpenAI partnership" (April 27, 2026): [https://blogs.microsoft.com/blog/2026/04/27/the-next-phase-of-the-microsoft-openai-partnership/](https://blogs.microsoft.com/blog/2026/04/27/the-next-phase-of-the-microsoft-openai-partnership/)
- OpenAI, "The next phase of the Microsoft partnership" (April 27, 2026): [https://openai.com/index/next-phase-of-microsoft-partnership/](https://openai.com/index/next-phase-of-microsoft-partnership/)
- CNBC, "OpenAI shakes up partnership with Microsoft, capping revenue share payments" (April 27, 2026): [https://www.cnbc.com/2026/04/27/openai-microsoft-partnership-revenue-cap.html](https://www.cnbc.com/2026/04/27/openai-microsoft-partnership-revenue-cap.html)
- PitchBook, "OpenAI loosens Microsoft's grip ahead of IPO push" (April 2026): [https://pitchbook.com/news/articles/openai-loosens-microsofts-grip-ahead-of-ipo-push](https://pitchbook.com/news/articles/openai-loosens-microsofts-grip-ahead-of-ipo-push)
- Lin et al., "Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses," arXiv 2604.25850 (April 28, 2026): [https://arxiv.org/abs/2604.25850](https://arxiv.org/abs/2604.25850)
- Agentic Harness Engineering companion repository: [https://github.com/china-qijizhifeng/agentic-harness-engineering](https://github.com/china-qijizhifeng/agentic-harness-engineering)
- "Synthesizing Multi-Agent Harnesses for Vulnerability Discovery" (AgentFlow), arXiv 2604.20801 (April 2026): [https://arxiv.org/abs/2604.20801](https://arxiv.org/abs/2604.20801)
- Anthropic, "Memory for Claude Managed Agents" (April 23, 2026): [https://claude.com/blog/claude-managed-agents-memory](https://claude.com/blog/claude-managed-agents-memory)
- AWS, "Amazon Bedrock now offers OpenAI models, Codex, and Managed Agents (Limited Preview)" (April 28, 2026): [https://aws.amazon.com/about-aws/whats-new/2026/04/bedrock-openai-models-codex-managed-agents/](https://aws.amazon.com/about-aws/whats-new/2026/04/bedrock-openai-models-codex-managed-agents/)
- About Amazon, "AWS and OpenAI announce expanded partnership to bring frontier intelligence to the infrastructure you already trust" (April 28, 2026): [https://www.aboutamazon.com/news/aws/bedrock-openai-models](https://www.aboutamazon.com/news/aws/bedrock-openai-models)
- OpenAI, "OpenAI models, Codex, and Managed Agents come to AWS" (April 28, 2026): [https://openai.com/index/openai-on-aws/](https://openai.com/index/openai-on-aws/)

---

*前の章: [第 10 章 — 実世界のナレッジ Harness を作る](10-case-study.md)*
