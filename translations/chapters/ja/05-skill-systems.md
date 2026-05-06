# 第 5 章：Skill Systems —— Skills、Skill Graphs、Progressive Disclosure

> **一文で：** Skills は AI に特定のタスクをどう行うかを伝える再利用可能な指示集合で、skill graph はそれらを航行可能な知識ネットワークへと繋ぐ。
>
> **なぜ重要か：** 同じことを毎回 AI に説明する代わりに、skills は一度教えてその知識を永遠に再利用させる。

Skills は事前パッケージされた指示集合 ——prompt、ツール設定、振る舞い規則の自己完結したバンドル —— で、特定の能力が必要なときにエージェントの context window に注入される。これは、エージェントシステムが少数の組み込み振る舞いから、関連しない指示でモデルを溺れさせずに数百あるいは数千の専門化された能力へとスケールする機構である。

本章は skill システムのアーキテクチャ、それが作り出す組合せ問題、そしてそれを解く progressive disclosure パターンを扱う。

---

## 5.1 Skill のコンセプト

最も単純な形での skill は、特定のタスクのための指示を含む markdown ファイル（または構造化テキストブロック）だ。ユーザー要求が skill のトリガー条件にマッチするとき、その内容が context window へとロードされる。マッチがないとき、skill はゼロトークンを寄与する。

これは、すべての能力をカバーしようとする一枚岩のシステム prompt とは根本的に異なる。90 のツールと 50 の振る舞いモードを記述するシステム prompt は、ユーザーがメッセージを打つ前に 50,000 以上のトークンを消費するかもしれない。Skill ベースのシステムは関連するものだけをロードし、ベースライン context を軽く保ち、実際のタスクのために window 容量を保留する。

設計パターンはソフトウェアエンジニアリングから借りられている：Skills はエージェントに対して、プラグインがアプリケーションに対するのと同じである。膨張なしの拡張性を提供する。

## 5.2 Anthropic Skills エコシステム

Anthropic は 2025 年 10 月に Claude Code 向けに skills をローンチした、当初はプロジェクト固有機能として ——Claude が関連時に呼び出せる `.claude/` ディレクトリの markdown ファイル。フォーマットは意図的に単純だった：説明、トリガー条件、指示を持つ markdown ファイル。

2025 年 12 月までに、Anthropic は agentskills.io を通じてオープン標準として skills を公開し、どのエージェントシステムでも採用できるポータブルな形式を定義した。仕様は以下をカバーした：

- Skill メタデータ（名前、説明、バージョン、著者）
- トリガー定義（キーワードマッチ、意図分類器、regex パターン）
- 内容構造（指示、例、ツール設定）
- 依存宣言（この skill が依拠する他の skills）

エコシステムの応答は急速だった。2026 年初頭までに、公式リポジトリは 87,000 を超える GitHub スターを集め、コミュニティ寄稿の skills は 700,000 を超えた。awesome-llm-skills、awesome-agent-skills（公式プラットフォームチームからの 1,000 以上の skills を特集）、awesome-claude-code のようなコレクションが主要な発見チャネルとなった。

この成長は、skills が解決するために設計されたまさにその問題を作り出した：限られた context 領域を競う能力が多すぎる。

## 5.3 スケーリング問題

OpenAI のエージェントドキュメントは実用的なガイドラインを含む：**エージェントを 20 ツール未満に保ち、10 を超えると精度劣化を予期せよ**。複数モデル族にまたがる経験的テストはこの閾値を確認する。各追加ツール定義は context にトークンを加え、モデルの選択空間に判断分岐を加える。90 ツールでは、スキーマオーバーヘッドだけで 50,000 トークンを超えることがある ——会話、記憶、取得文書が window に入る前に。

劣化はトークン数だけのものではない。判断複雑度のものでもある。モデルが 90 ツールから選ばなければならないとき、確率質量が薄く広がる。モデルはツール選択により多くの推論能力を費やし、タスク実行により少なく費やす。ツールパラメータ構築のエラー率が増える。モデルは、それらしいが間違ったツールをより頻繁に選び始める。

Skills は同じスケーリング圧力に直面する。500 の利用可能 skills を持つシステムは、500 の説明をすべて context にロードできない。500 skills のトリガー説明だけをロードしても、数千トークンを消費し実際の要求を処理するモデルの能力を劣化させかねない。

解は progressive disclosure である。

## 5.4 Progressive Disclosure アーキテクチャ

Progressive disclosure は、各レベルが次のルーティング判断にちょうどよい詳細を提供する多層情報アーキテクチャである：

**Level 0：ルーティングインデックス。** カテゴリを skill グループへとマップするコンパクトなテーブル。skill ライブラリ全体で総じて 200–500 トークンを消費するかもしれない。これは安静時にシステム prompt に置かれるものだ。

**Level 1：カテゴリ説明。** ルーティングインデックスが関連カテゴリを特定したら、そのカテゴリの skills の一段落の説明をロードする。各説明は走査用に最適化されている ——関連性を判断するに足り、実行するに足りない。

**Level 2：Skill リンクと依存。** 選択された skill について、その依存グラフをロードする ——どの他の skills やツールを必要とするか、どんな context を期待するか。

**Level 3：セクションと要約。** Skill の構造的アウトラインをロードする ——セクションヘッダ、鍵となる判断点、パラメータリスト —— 完全な指示内容なしで。

**Level 4：完全な内容。** 完全な skill 指示を context window へとロードする。これは実際に呼び出される 1 つか 2 つの skills でのみ起こる。

鍵となる洞察は、Heinrich と arscontexta チームが形式化したように、**大半の判断は単一の完全ファイルを読む前に起こる**ということだ。ルーティングインデックスは 95% の skills を除外する。カテゴリ説明は残りの大半を除外する。完全内容ロードは規則ではなく例外である。

本番システムにまたがって計測すると、progressive disclosure は、すべての skill 定義を最初にロードするのと比べて、トークンオーバーヘッドを **85–95%** 削減する。Anthropic 自身のエージェント skills 実装はこれを実証する：17 本番 skills が安静時に約 1,700 トークン（Level 0 + Level 1）を消費し、呼び出し時のみ完全内容に展開する。

## 5.5 Skill Graphs

Heinrich の Skill Graph アーキテクチャ（arscontexta、2025–2026）は progressive disclosure をネットワーク構造へと拡張する。カテゴリで組織されたフラットな skill リストではなく、skill graph は **wikilink で繋がれた相互接続された markdown ファイルのネットワーク** で、各ノードが以下を持つ：

- 簡潔な説明を持つ YAML フロントマターブロック（Level 1 走査用）
- 関連 skills、前提 skills、サブ skills への wikilink
- 独立にロード可能な構造化セクション

グラフ構造は、フラットな skill リストがサポートできないいくつかの能力を可能にする：

**文脈的航行。** 1 つの skill が呼び出されると、リンクされた skills が共ロードの候補となる。「deploy」skill は「test」、「rollback」、「monitor」 skills にリンクする ——同じカテゴリにあるからではなく、運用上隣接しているから。

**依存解決。** Skills は前提を宣言できる。複雑な skill を呼び出すと、それが依拠する基盤 skills が自動的に引き込まれる、パッケージ依存解決と同様に。

**部分ロード。** Skills は明確なセクションで構造化されているので、システムは特定セクション（例：デプロイ skill の「エラーハンドリング」セクションのみ）を、完全文書をロードせずにロードできる。

グラフトポロジ自体が知識表現の一形式となる。密に接続された skill クラスタは、内部的整合性が高い能力領域を示す。孤立した skills は、システムのカバレッジのギャップや統合の機会を示すかもしれない。

## 5.6 SkillReducer 論文

2026 年 3 月に公開された研究は、複数のエージェントプラットフォームにまたがる 55,315 の skills を検査し、skill 品質に関する素朴な仮定に挑戦する発見を生み出した：

- **26.4% の skills がルーティング説明を完全に欠いていた。** 完全な指示内容は持つが、ルーティングシステムがいつ呼び出すかを特定するメタデータがない。これらの skills は完全名でしかトリガーできなかった ——どのインテリジェントなルーティング層にも見えない。

- **Skill 本体の 60% 超が実行不能だった。** 背景 context、動機、但し書き、説明テキストで構成され、モデルが実行できる具体的指示ではなかった。この内容はタスク性能に貢献せずトークンを消費した。

- **圧縮された skills は元のものより出力品質を 2.8% 改善した。** 研究者が実行不能内容を剥ぎ取り指示言語をきつくしたとき、モデル性能が実際に改善した。Less is more —— context 内のノイズ削減が、モデルが実行可能指示に集中することを可能にした。

Skill 著作への含意は直接的だ：

1. **すべての skill にはルーティング説明が必要。** なしでは、skill は progressive disclosure システムから事実上見えない。
2. **指示内容は密で実行可能であるべき。** 背景 context は context window に注入される skill 本体ではなく、ドキュメントに属する。
3. **Skill 品質計測はトークン効率を含むべき** ——「動くか」だけでなく「消費トークンあたり動くか」も。

## 5.7 MCP 用の Meta-Tool パターン

Model Context Protocol（MCP）は、エージェントが提供者横断でツールを発見し呼び出す標準化された方法を導入した。だが MCP のオリジナル設計は接続時にすべての利用可能ツールスキーマをロードし、skills が直面するのと同じスケーリング問題を作った。

Meta-tool パターンはこれを 2 つの構成要素で解く：

- **Discovery Tool：** 自然言語記述を受け取り、完全なレジストリから関連ツールスキーマを返す単一のツール。これがベースラインでロードされる唯一のツールだ。
- **Execution Tool：** 発見でスキーマが取得された後、名前で任意のツールを呼び出せる汎用ツール呼び出しラッパー。

システムは数百ではなく 2 つのツールスキーマをロードする。モデルが能力が必要だと判断すると、discovery tool を呼び、関連スキーマを受け取り、特定のツールを呼び出す。このパターンは、1 つの追加推論ラウンドトリップを大規模な context 節約と引き換えにする。

これはツール管理に適用された progressive disclosure である：モデルは電話帳を得て、すべての連絡先のファイルの内容ではない。

## 5.8 著作ガイドライン

SkillReducer の発見と本番経験から、skill 著作のベストプラクティスの集合が浮上した：

- **ルーティング説明から始めよ。** YAML フロントマターの説明はファイル中で最も重要な行だ。Skill が呼び出されるかどうかを決める。人間の読者ではなく分類器のために書け。
- **実行可能指示を前置せよ。** Skill 本体の最初の 200 トークンは中核的振る舞い指示を含むべき。背景と context は後に続く。
- **構造化されたセクションを使え。** ヘッダ、リスト、明確な区切りが部分ロードとセクションレベル取得を可能にする。
- **依存を明示的に宣言せよ。** Skill が他の skill やツールが利用可能であると仮定するなら、メタデータでそれを述べよ。
- **トリガー例を含めよ。** Skill を活性化すべき 3–5 のユーザーメッセージ例を提供せよ。これらはルーティング層のドキュメントとテストケース両方として機能する。
- **トークンコストを計測せよ。** 各 skill のトークン数を追跡し予算を設定せよ。Skill が 2,000 トークンを超えるなら、分割や圧縮が可能か検討せよ。

## 5.9 業界の収束：Google Agent Skills 仕様（2026 年 4 月）

2025 年の大半を通して、progressive disclosure は主に Anthropic の慣習だった ——2025 年 10 月の Claude Code skills と 2025 年 12 月の agentskills.io オープン標準を通じて形式化された。**2026 年 4 月**、Google Developers Blog は同じアーキテクチャを採用し拡張する自身の **Agent Skills Spec** を形式化した。仕様は progressive disclosure の 3 つの明示的レベルを記述する：

- **Level 1 —— メタデータ（skill あたり ~100 トークン）。** Skill の名前、一行説明、トリガーヒント、バージョンを含むコンパクトな記述子。各利用可能 skill の Level 1 メタデータがエージェントのベースライン context に置かれる。10 skills がロードされていれば、定数オーバーヘッドはおよそ 1,000 トークンだ。
- **Level 2 —— 指示（< 5K トークン）。** Skill の完全な振る舞い指示、Level 1 マッチが skill を関連と特定したときオンデマンドでロード。Level 2 の内容は skill が実際に選択されるまで context に入らない。
- **Level 3 —— 外部リソース。** Context window の完全に外側に住むアセット ——参照文書、データセット、ツールスキーマ、コードサンプル —— skill が実行中に明示的に必要とするときのみ取得される。

見出しの効率主張：10 skills を持つエージェントの場合、ベースライン context 使用が約 **10K トークン**（skill 完全内容を最初にロード）から約 **1K トークン**（Level 1 メタデータのみ）へと下がる、**90% 削減**。Level 2 内容は一度に 1 skill ロードし、Level 3 リソースは実行中に必要なときのみロードする。

Google 仕様を数字を超えて注目に値するものにする 2 つの詳細：

1. **普遍的な `agentskills.io` 仕様を使う。** フォークする代わりに、Google は Anthropic が 2025 年 12 月に公開したオープン標準と形式を整列させた。1 つの仕様に対して書かれた skill は、最小の適応で他のプラットフォームのエージェントが消費できる。
2. **Progressive disclosure を慣習から正式なシステム設計パターンへと格上げする。** およそ 1 年間、progressive disclosure は「Anthropic が skills でやること」と記述されていた。Google の採用と形式化により、それは命名されたアーキテクチャと計測可能な目標を持つクロスベンダー業界パターンとなる ——「MVC」や「REST」が特定実装から汎用パターンへと進化したのに比類する。

実用効果は、skill ライブラリが提供者横断でポータブルになりつつあること、そして「ベースラインエージェント context は何トークン消費するか」がベンダーが競う第一級の指標となったことだ。

---

## Sources

- **Anthropic.** "Claude Code Skills." Documentation and open standard specification, October 2025 (launch), December 2025 (open standard via agentskills.io). 87K+ GitHub stars by early 2026.
- **OpenAI.** "Agent Design Best Practices." OpenAI documentation, 2025. エージェントあたり 20 ツール未満の推奨、10 を超えると精度劣化。
- **Heinrich (@arscontexta).** Skill Graphs concept and implementation. X posts (2026): [https://x.com/arscontexta/status/2023957499183829467](https://x.com/arscontexta/status/2023957499183829467) (Skill Graphs > SKILL.md)。GitHub: [https://github.com/agenticnotetaking/arscontexta](https://github.com/agenticnotetaking/arscontexta) — wikilink と YAML フロントマター走査を伴う、個別化された markdown グラフ知識システムを生成する Claude Code プラグイン。二次分析：Linas Substack, "Skill Graphs: The Architecture That Solves the AI Agent Context Window Problem." [https://linas.substack.com/p/skill-graphs](https://linas.substack.com/p/skill-graphs)
- **SkillReducer Paper.** "Less Is More: Compressing Agent Skills for Improved Performance." March 2026. 55,315 skills 分析、26.4% がルーティング説明を欠如、60%+ が実行不能内容、圧縮で 2.8% の品質改善。
- **Model Context Protocol (MCP).** Anthropic specification, 2024-2025. 標準化されたツール発見・呼び出しプロトコル。
- **awesome-llm-skills.** GitHub のコミュニティコレクション。プラットフォーム横断の精選 skill ライブラリ。
- **awesome-agent-skills.** GitHub コレクション、公式プラットフォームチームからの 1,000+ skills。
- **awesome-claude-code.** GitHub コレクション。Claude Code 固有の skills と設定。
- **OpenAI.** "Function Calling Best Practices." 2025. ツール数対精度トレードオフの経験データ。
- **Griciūnas, Aurimas.** "State of Context Engineering in 2026." SwirlAI Newsletter, March 2026. [https://www.newsletter.swirlai.com/p/state-of-context-engineering-in-2026](https://www.newsletter.swirlai.com/p/state-of-context-engineering-in-2026) — Progressive disclosure / 圧縮 / スライディング window パターン；meta-tool パターン。"Breaking Down Context Engineering" も参照：[https://www.newsletter.swirlai.com/p/breaking-down-context-engineering](https://www.newsletter.swirlai.com/p/breaking-down-context-engineering)
