# 第 3 章：Context Engineering —— window を埋める技芸

> **一文で：** Context engineering とは、AI に適切な情報を適切な時に与える技芸である ——多すぎず少なすぎず。
>
> **なぜ重要か：** より良い context はより良い AI 回答を意味する。これが、AI から驚くべき結果を得る人と平凡な応答しか得られない人の差を生む理由だ。

> 「Context engineering とは、次のステップに必要な情報をちょうどよく context window に詰める繊細な技芸であり科学である。」
> ——Andrej Karpathy、2025 年 6 月

Prompt engineering がよい質問を書くことなら、context engineering はそれを取り巻くブリーフィングパケット全体を構築することだ。前者から後者へのシフトは、実践者が LLM システムをどう考えるかの根本的変化を画す：設計の単位はもはや単一指示ではなく、*情報環境* である。

本章はこのランドスケープを地図化する ——理論フレームワークから本番で検証されたパターンまで —— そして本分野を定義する一次出典を指し示す。

---

## 3.1 Prompt から Context へ

「context engineering」という用語は 2025 年中頃、Karpathy がそれと prompt engineering の間に鋭い線を引いたときにメインストリーム使用に入った。Prompt は静的な文字列だ。Context はモデルが必要とするすべて ——指示、記憶、取得文書、ツール定義、会話履歴、直近のタスク —— を動的に組み立てたパッケージで、プログラム的に構成され各ターンで更新される。

この区別が重要なのは、現代のエージェントが同じ context を 2 度送ることはほぼないからだ。各推論呼び出しは、何が window を埋め何が外されるかを決めるルーティング論理、検索パイプライン、圧縮ヒューリスティクス、ツール可用性チェックの産物である。

## 3.2 6 層の Context モデル

Anthropic の [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents) や周辺の実践者文書が記述するパターンに基づいて、context window を概念的に 6 層に分解できる。最も永続的なものから最も儚いものへと並べる。ここでのラベルは Anthropic 自身が公開する分類体系ではなく、本ガイドの教育的合成である：

| 層 | 内容 | 典型的な永続性 |
|-------|----------|-------------------|
| **System Rules** | 安全制約、ペルソナ定義、振る舞いガードレール | デプロイメントごとに静的 |
| **Memory** | ユーザー設定、過去のセッション要約、学習された事実 | セッション横断 |
| **Retrieved Documents** | RAG 結果、検索スニペット、ファイル内容 | ターンごと |
| **Tool Schemas** | 関数定義、API 仕様、能力宣言 | セッションごと、またはターンごとマスク |
| **Conversation History** | 過去のメッセージ、アシスタント応答、ツール呼び出し結果 | スライディング window |
| **Current Task** | 直近のユーザー要求 + タスク固有注入 | ターンごと |

鍵となる洞察は、各層が異なる更新頻度、異なる圧縮戦略、異なる失敗モードを持つことだ。Retrieved Documents 層を詰めすぎると Current Task のシグナルを溺れさせる。Memory が薄すぎると、本来既に持つべき context をモデルに再導出させる。よい context engineering とは、6 つすべての層にまたがってバランスを取ることである。

## 3.3 Manus からの教訓：北極星としての KV-Cache

2025 年 7 月、Yichao "Peak" Ji（Manus CTO）が一連の本番教訓を公開し、context engineering を単一の運用指標 ——**KV-cache ヒット率** —— の周りで再フレーミングした。

Manus はエージェントシステムで入力と出力トークンの間に 100:1 の比率を一貫して観察した。その比率では、入力コストがすべてを支配する。KV-cache ヒット ——以前計算された key-value ペアが再計算されずに再利用されるところ —— がレイテンシとコスト両方の主要レバーとなる。

この洞察から 3 つの技法が浮上した：

1. **Append-only な context 構造。** Context の前部分を決して書き換えない。中央への挿入や編集はキャッシュされた接頭辞を無効化し、完全再計算を強いる。Context をログとして設計せよ、文書としてではない。

2. **スキーマ削除ではなく logit bias によるツールマスキング。** ツールが一時的に利用不能なとき、Manus は context からツール定義を削除する代わりに logit レベルのマスキングで選択を抑制した。定義の削除はトークンシーケンスを変え、キャッシュを破壊する。マスキングは選択を防ぎつつ接頭辞を保つ。

3. **ローリング todo-list 書き換え。** 長い会話の早い段階の目標をモデルに想起させることに頼る代わりに、Manus は context の末尾近くに書き換えた todo list を周期的に追加した。これは注意の最近性バイアスを利用する ——最も最近のトークンの目標は、数千トークン早く埋もれた同一の目標より強い注意重みを受ける。

これらは prompt レベルではなく、インフラレベルの判断だ。なぜ「context engineering」がシステム思考を要するかを示す。

## 3.4 5 つの支配的パターン

Aurimas Griciūnas は、本番システムにまたがって観察される 5 つの繰り返しパターンへと、新興の実践を統合した（典拠：「State of Context Engineering in 2026」、SwirlAI Newsletter、2026 年 3 月 22 日、[https://www.newsletter.swirlai.com/p/state-of-context-engineering-in-2026](https://www.newsletter.swirlai.com/p/state-of-context-engineering-in-2026)；「Breaking Down Context Engineering」も参照）：

**Progressive Disclosure。** すべてを最初にロードしない。軽量なインデックスを最初に提示する；モデル（またはルーティング論理）が関連と判断したセクションだけを展開する。Context window 版の遅延ロードである。Anthropic 自身のエージェントスキルシステムがこのパターンを使う ——17 スキルが安静時に約 1,700 トークンを消費し、呼び出し時のみ展開する。

**Context Compression。** 注入前に情報を要約、切り詰め、蒸留する。スライディング window を超えた会話履歴は要約に圧縮される。取得文書は関連箇所に抜粋される。目標は、トークン数を減らしつつ意味密度を保つことだ。

**Context Routing。** すべてのクエリが同じ context を必要とするわけではない。ルーティング層が入ってくる要求を検査し、含めるべき記憶バンク、ツール集合、文書コレクションを選ぶ。Context window 版のデータベースクエリプランナである。

**Retrieval Evolution。** 静的 RAG（一度取得、注入、生成）は、モデルが生成中に追加情報を要求できる反復検索に道を譲る。Context は一度組み立てられるのではなく、生成プロセスを通じて進化する。

**Tool and Capability Management。** ツールライブラリが拡大するにつれ、すべてのスキーマをロードすることは禁止的になる。システムは meta-tool パターン（オンデマンドで関連ツールスキーマを返す発見ツール）やスキルグラフアーキテクチャを使ってツール層を軽く保つ。

## 3.5 学術ランドスケープ

2025 年中頃、context engineering を形式的研究領域として扱った最初の包括的学術サーベイが登場した：**「A Survey of Context Engineering for Large Language Models」**（Mei 他、arXiv 2507.13334、2025 年 7 月 17–21 日）。1,400 を超える研究論文の体系的分析を通じて、本分野の技術ロードマップを確立した。サーベイは設計空間を 2 軸で組織する：**基盤コンポーネント**（context 検索と生成、context 処理、context 管理）と**システム実装**（RAG、記憶システム、ツール統合推論、マルチエージェントシステム）。荷重を支える発見は、能力の根本的非対称性である：現在のモデルは複雑な context の理解には著しく堪能だが、同等に洗練されたロングフォーム出力の生成には顕著な制約を示す。実践者にとって、このサーベイは本分野が持つ教科書に最も近いものだ ——経験的に発見されてきたものを形式化した：context engineering は単一技法ではなく、複数の独立次元を持つ設計空間である。

## 3.6 Agentic Context Engineering (ACE)

ACE 論文 **「Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models」**（Zhang 他、arXiv 2510.04618、2025 年 10 月 6 日；コンパニオンリポジトリ [github.com/ace-agent/ace](https://github.com/ace-agent/ace)）は、概念シフトを導入した：context を静的な組み立てではなく **進化する playbook** として扱う。ACE システムでは、context はエージェント自身が保守する生きた文書である ——観察を加え、計画を更新し、関連しない履歴を刈り取り、タスク進捗に基づいて自身の指示を再構成する。報告された見出しゲイン：エージェントベンチマークで +10.6%、金融タスクで +8.6%、適応レイテンシとロールアウトコストの削減付き；AppWorld リーダーボードで、ACE はより小さなオープンソースモデルを使いながら、全体平均で本番レベルの首位エージェントに並び、より難しい test-challenge スプリットでは超える。ACE はまた、対抗するために設計された失敗モードに名前を付ける：**簡潔さバイアス**（簡潔な要約のためにドメイン洞察を落とす）と **context 崩壊**（反復書き換えが時間とともに詳細を浸食する）。

これは context engineering を純粋なインフラ関心事（各呼び出し前に harness が組み立てるもの）から協調的なものへ（harness が準備するもの*かつ*モデルが能動的に作り変えるもの）へと移す。「システムが提供する context」と「モデルが作る context」の境界は流動的になる。

ACE システムは典型的に context 内に構造化スクラッチパッドを保つ ——モデルが作業ノート、中間結果、改訂計画を書く、指定された領域。Harness はターン横断でこの領域を保ちつつ、自身のポリシーに従って周辺の層を管理する。

## 3.7 実践への含意

このランドスケープからいくつかの原則が浮上する：

- **出力だけでなく入力トークンも計測する。** 本番スケールでは、100:1 の入力/出力比率は context 組み立てコストが支配することを意味する。キャッシュヒットと最小冗長性のために最適化せよ。
- **Context を層化されたシステムとして設計せよ。** 各層は独自の更新ポリシー、圧縮戦略、失敗モードを持つ。独立に扱え。
- **デフォルトで progressive disclosure を使え。** 軽く始めよ。オンデマンドで展開せよ。関連しない情報を含めるコストはトークンだけではない ——劣化した注意と幻覚リスクの増加でもある。
- **Prompt だけでなく context 構成をテストせよ。** 異なる context 内の同じ prompt は異なる結果を生む。テストスイートは最終指示だけでなく context を変えるべきだ。
- **モデル改善を予期せよ。** モデルが長 context 推論で良くなるにつれ、いくつかの圧縮・ルーティング戦略は不要なオーバーヘッドになる。層を単純化または除去できるよう、明確な抽象境界で構築せよ。

---

## Sources

- **Karpathy, Andrej.** Public remarks on "context engineering" (mid-2025). 本分野を横断して採用された作業定義を作った、X と AI エンジニアリングコミュニティで広く共有されたフレーミング。
- **Anthropic.** "Building Effective Agents." Anthropic engineering blog, December 19, 2024. [https://www.anthropic.com/engineering/building-effective-agents](https://www.anthropic.com/engineering/building-effective-agents) — orchestrator-worker パターンと evaluator-optimizer ワークフローを記述する；本ガイドは §3.2 で 6 層概念ラベルを教育的に付与する。
- **Ji, Yichao "Peak"** (Manus). "Context Engineering Lessons from Building Manus." Blog post, July 2025. [manus.im/blog](https://manus.im/blog) — 運用指標としての KV-cache ヒット率、append-only context 構造、logit bias によるツールマスキング、ローリング todo-list 書き換え。
- **Griciūnas, Aurimas.** "State of Context Engineering in 2026." SwirlAI Newsletter, March 22, 2026. [https://www.newsletter.swirlai.com/p/state-of-context-engineering-in-2026](https://www.newsletter.swirlai.com/p/state-of-context-engineering-in-2026)。"Breaking Down Context Engineering" も参照：[https://www.newsletter.swirlai.com/p/breaking-down-context-engineering](https://www.newsletter.swirlai.com/p/breaking-down-context-engineering)
- **Mei, Lingrui et al.** "A Survey of Context Engineering for Large Language Models." arXiv 2507.13334, July 17-21, 2025. [https://arxiv.org/abs/2507.13334](https://arxiv.org/abs/2507.13334) — context engineering を形式的研究領域として確立した 1,400+ 論文レビュー。
- **Zhang, Qizheng et al.** "Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models." arXiv 2510.04618, October 6, 2025. [https://arxiv.org/abs/2510.04618](https://arxiv.org/abs/2510.04618)。コンパニオンリポジトリ：[github.com/ace-agent/ace](https://github.com/ace-agent/ace)。Context を進化する playbook として枠付け、簡潔さバイアスと context 崩壊に名前を付ける。
- **Schmid, Philipp.** "The New Skill in AI is Not Prompting, It's Context Engineering" および続編。[https://www.philschmid.de/context-engineering](https://www.philschmid.de/context-engineering)；[https://www.philschmid.de/context-engineering-part-2](https://www.philschmid.de/context-engineering-part-2)
- **LangChain blog.** Context-engineering coverage at [blog.langchain.com](https://blog.langchain.com) — 実践者パターンとしての Agent Engineer フレーミング（単一の典拠投稿はなし；言説アンカーとして引用）。
- **Willison, Simon.** Ongoing AI engineering coverage at [simonwillison.net](https://simonwillison.net) — エコシステムを繋ぐ手の届く実践者向け入門。
