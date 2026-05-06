# 第 4 章：Harness Engineering —— モデルの周りに OS を構築する

> **一文で：** Harness とは AI モデルの周りのすべて ——それを実際に役立つものにする規則、ツール、安全チェック、ワークフロー —— である。
>
> **なぜ重要か：** AI モデルは強力なエンジンのようなもの。シャーシ、ハンドル、ブレーキがなければ役に立たない。Harness は生の AI をプロダクトへと変えるものだ。

> 「Harness のすべてのコンポーネントは、モデルが自力でできないことについての仮定を符号化している。そしてそれらの仮定はストレステストする価値がある。」
> ——Anthropic, "Building Effective Agents", 2025

> 「模型從來都沒有長手。」
> ——Cab、ツール使用がモデル問題ではなく harness 問題である理由について

エージェントはモデルではない。エージェントは **モデル + harness** ——生の推論を信頼性のある振る舞いへと変える、prompt、ツール、記憶、制御フロー、評価論理、編成コードの周辺システム —— である。モデルはエンジンで、harness は車両だ。本章は実践者がその車両をどう設計し、評価し、進化させるかを検討する。

**直感への補足。** 多くの初心者にこれを具体化させるメタファは、Cab の観察「モデルは文字通り手が生えたわけではない」だ。コーディングエージェントがファイルを編集するとき、ファイルを編集したのはモデルではない ——モデルがテキストとして返したツール呼び出しでトリガーされた harness だ。我々が「AI」のものと考えるすべての能力は、実はモデルを取り巻く harness の能力である。Harness を剥がせば、テキストしか生み出せないモデルが残る。モデルを剥がせば、ルートする対象を持たない harness が残る。Harness エンジニアリングはその線がどこに位置するか、両半分がどう協力するかを決める規律である。

---

## 4.1 Harness を定義する

Harness はモデル重み以外のすべてだ。それには以下が含まれる：

- システム prompt と指示テンプレート
- ツール定義と実行サンドボックス
- 記憶システム（短期、長期、エピソード）
- プランニングと分解論理
- 制御フロー（ループ、条件、再試行ポリシー）
- 評価と自己訂正機構
- 安全ガードレールと出力検証
- Context 組み立てパイプライン（第 3 章）

ユーザーメッセージ付きの素のモデル API 呼び出しは些細な harness だ。プランニング、多段ツール使用、自己評価、永続記憶を持つ本番エージェントは複雑なものだ。Harness エンジニアリングの規律は、このスペクトルに沿って原則的判断を下すことについてである。

## 4.2 Böckeler の分類体系

Birgitta Böckeler（ThoughtWorks、2026 年 4 月）は Martin Fowler の *Exploring Generative AI* シリーズに寄稿し、harness コンポーネントのための 2 軸分類体系 ——いまや標準的参照となった —— を提案した：

**軸 1：方向**
- **Guides（フィードフォワード）：** モデルが行動する*前*に振る舞いを形作るコンポーネント。システム prompt、few-shot 例、ツールスキーマ、プランニングテンプレート。これらはレールを敷く。
- **Sensors（フィードバック）：** モデルが行動した*後*に振る舞いを評価し結果をフィードバックするコンポーネント。出力 validator、テストランナー、人間レビュー、自己評価 prompt。これらは進路を訂正する。

**軸 2：機構**
- **計算的制御：** 決定的コード ——regex validator、型チェッカ、スキーマ強制、権限チェック。これらは決して幻覚しない硬い制約だ。
- **推論的制御：** 判断、ルーティング、洗練に使われる別の LLM 呼び出し。Evaluator モデル、分類器、要約器。これらは精密性を柔軟性と引き換えにする柔らかい制約だ。

この分類体系は設計空間を露わにする。大半の本番 harness は 4 つの象限すべてを使う：

|  | Feedforward (Guides) | Feedback (Sensors) |
|--|---------------------|--------------------|
| **計算的** | ツール入力のスキーマ検証、権限許可リスト | 出力フォーマットチェック、テストスイート実行 |
| **推論的** | プランニング prompt、few-shot ルーティング | 自己評価、LLM-as-judge、批評チェーン |

洞察は、計算的制御は安価で信頼性があるがより柔軟性に欠け、推論的制御は曖昧さを扱うが独自の失敗モードをもたらす、というものだ。よい harness 設計は可能な限り計算的制御を使い、真に曖昧な判断のために推論的制御を保留する。

## 4.3 OpenAI Codex：Harness を通じたスケール

実践者コミュニティで広く引用される印象的なデータポイントが、OpenAI による Codex の社内利用を記述する：**3 人のエンジニア + Codex エージェントシステムが、約 1,500 のプルリクエストにまたがって約 100 万行のコードを生み出した**。生産性倍率は主としてモデル品質ではなく ——harness 設計についてだった。（具体的な数字は 2025–2026 年の OpenAI トークと投稿で流通した；Codex の harness の公的素材は [openai.com/index/introducing-codex](https://openai.com/index/introducing-codex) を参照。）

Codex の harness は以下を含んでいた：
- 自動 PR 分解（大きなタスクをレビュー可能な単位に分割）
- 各タスクのためのサンドボックス化された実行環境
- 自動テスト生成と検証
- PR 境界での人間レビュー統合
- リポジトリ構造と規約に関する永続的 context

教訓：十分な harness 成熟度では、モデルは独立したツールではなくより大きな本番システムの中の構成要素となる。Harness が編成、品質管理、統合 ——どんなに prompt エンジニアリングをしても対処できない関心事 —— を扱う。

## 4.4 IMPACT フレームワーク

2020 年代中頃の実践者言説の中で、**IMPACT 記憶法** ——Intent、Memory、Planning、Authority、Control flow、Tools —— が harness 設計次元を体系的に考える方法として浮上した：

- **Intent：** システムはユーザーが実際に何を望むかをどう理解するか？ 意図分類、明確化対話、目標分解を含む。
- **Memory：** システムはターンとセッションを越えて何を記憶するか？ 会話バッファ、ベクトルストア、構造化ナレッジベース、ユーザー設定システムを含む。
- **Planning：** システムは複雑なタスクをどうステップへと分解するか？ Chain-of-thought prompting、明示的計画生成、行動空間上の木探索を含む。
- **Authority：** システムは何をすることを許されているか？ 権限システム、人間ループ内ゲート、能力境界を含む。
- **Control Flow：** 実行はどう進むか？ 順次チェーン、並列ファンアウト、条件分岐、終了条件付きループ、再試行ポリシーを含む。
- **Tools：** システムはどんな外部能力にアクセスできるか？ 関数定義、API 統合、コード実行環境、ブラウザアクセスを含む。

IMPACT は設計チェックリストとして有用だ。Harness を構築またはレビューするとき、各次元を歩くとギャップが表面化する。Tools は強いが Authority が弱いシステムにはセキュリティ問題がある。Planning は強いが Memory がないシステムは失敗から学べない。フレームワークはこれらの不均衡を可視化する。

## 4.5 Meta-Harness 論文：Harness 設計を自動化する

Stanford、MIT、KRAFTON の共同論文（2026 年 3 月）が **メタ harness** ——harness 構成を自動的に最適化するシステム —— のコンセプトを導入した。

彼らの鍵となる発見：同じベンチマークで、同じ基盤モデルで、異なる harness 構成が **6 倍の性能ギャップ** を生み出した。与えられたタスクに対する最良の harness 構成はめったに自明でなく、しばしば直感に反した。手動 harness チューニングは膨大な性能をテーブルに残していた。

メタ harness アプローチは harness パラメータ（再試行回数、プランニング深度、ツール選択戦略、記憶 window サイズ、評価厳格度）を探索空間として扱い、自動最適化を使って高性能構成を見つけた。システムは harness を異なるタスクタイプ、異なるモデル、異なるコスト制約に適応させられる。

この結果には深遠な含意がある：**Harness エンジニアリングは既知のベストプラクティスを持つ解決済みの設計問題ではなく ——大きく十分に理解されていない探索空間を持つ最適化問題である**。Harness 設計を一度きりのアーキテクチャ判断として扱うチームは、フロンティアより遥か下で運用している可能性が高い。

Meta-Harness 論文はいま、急速に動く系列の中の 1 データポイントだ。2026 年 4 月、**AHE 論文**（"Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses"、arXiv 2604.25850、復旦 / 北京 / 上海期智智峰）は問題を探索から*観測可能性*へと再フレーミングした：harness 構成を探索空間として扱いオプティマイザを走らせる代わりに、AHE は 3 つの観測可能性の柱 ——コンポーネント（明示的で可逆な行動空間）、経験（凝縮された軌跡証拠）、判断（実行前の反証可能な編集予測） —— を計装し、harness が自身のランタイムシグナルを読むことで自己進化することを許す。10 回の AHE イテレーションの後、Codex-CLI スタイルのベースラインは Terminal-Bench 2 で 69.7% pass@1 から始めて 77.0% に到達、人間設計のベースライン（71.9%）を超え、harness が最適化されていないモデル族に転送したときに **+5.1 から +10.1 pp のクロスファミリーゲイン** を示す。クロスファミリー転送が構造的なニュースだ：進化した harness は単一モデルのクセに過適合しているのではなく、下の基盤が入れ替わっても引き継がれる。Meta-Harness の発見（「harness エンジニアリングは大きな探索空間を持つ最適化問題」）と AHE の発見（「……探索は一発最適化ではなく継続的観測可能性ループとして走りうる」）が併せて、手動チューニングを急速に置き去りにしているエンジニアリング実践を記述する。

### リサーチから本番へ：Advisor Tool（2026 年 4 月）

Meta-harness の発見はリサーチ結果だった。1 か月後、Anthropic が初のプロダクト化されたメタ harness パターンを出荷した：**Advisor Tool**（ベータ、`advisor-tool-2026-03-01`）。このパターンは、より速い executor モデルと、より能力のある advisor モデルをペアにする。Executor が作業の大半を扱う；判断点に当たったとき、`advisor()` を呼び出して戦略計画や進路訂正（典型的に 400–700 テキストトークン、思考込みで 1,400–1,800）を、現在の API リクエストを離れずに受け取る。

Anthropic が推奨するデフォルト設定は示唆的だ：

| Executor | Advisor | 想定用途 |
|----------|---------|--------------|
| Haiku 4.5 | Opus 4.6 | Haiku 単独からの知能ステップアップ |
| Sonnet 4.6 | Opus 4.6 | Sonnet コストで Opus 単独品質 |
| Opus 4.6 | Opus 4.6 | 最難タスクでの品質洗練 |

これは 6 倍メタ harness ギャップを価格戦略へと翻訳したものだ。すべてのトークンに Opus レートを払う代わりに、実行に Sonnet レートを払い、実際に出力を形作る 1–2 回の advisor 呼び出しに Opus レートを払う。Anthropic が示唆する prompting パターンは、harness のタイミングをルールへと符号化するので引用に値する：

> 「実質的な作業の前に advisor を呼べ ——書く前に、解釈にコミットする前に、仮定を組み立てる前に。[…] 数ステップを超えるタスクでは、アプローチにコミットする前に少なくとも一度、完了を宣言する前にもう一度、advisor を呼べ。」

ドキュメントのいくつかの詳細が実践者にとって重要だ：

- **サーバーサイド・サブ推論。** Advisor は同じ `/v1/messages` リクエストの内側で動く。Executor は `server_tool_use` ブロックを発し、Anthropic は完全なトランスクリプトで別個の推論パスを走らせ、結果は `advisor_tool_result` として返ってくる。あなたのコードからの追加ラウンドトリップはなし。
- **キャッシュは ~3 回の呼び出しで損益分岐。** Advisor ツールで `caching` を有効化すると、advisor のトランスクリプトを 5 分または 1 時間のキャッシュへ書き込む。最初の呼び出しは追加コストがかかる；元が取れ始めるのは 3 回目あたり。短いタスクではキャッシュをオフのままにすべき。
- **簡潔さ prompt が出力を 35–45% 削減する。** 単一指示 ——「advisor は 100 語以下で応答し、説明ではなく番号付きステップを使うべき」 —— が、呼び出し頻度を変えずに advisor の最大コストドライバを測定可能に減らす。
- **明示的な reconcile プロトコル。** Advisor のアドバイスが executor が既に集めた経験的証拠と矛盾するとき、Anthropic のシステム prompt は executor に、黙って切り替えるのではなく「私は X を見つけた、あなたは Y を提案する、どの制約が決め手か」と枠組んだ追加の advisor 呼び出しを 1 回行うよう告げる。これは複数役割が不一致するときに常に出てくる「プランナーかデータか、どちらを信じるか」問題への、本番グレードの回答だ。

Advisor Tool は直近の有用性を超えて重要だ。これはメタ harness 思考がリサーチ好奇心から商業 primitive へと移ったシグナルである。「同じモデル、異なる harness、6 倍のギャップ」という発見は、もはや活用するためにリサーチチームを必要とするものではない ——Anthropic がツール呼び出しとして露出する。他のラボが独自の advisor / executor ペアリングで追随することを期待せよ。そして harness エンジニアリング求人記述がマルチモデル協調を中核スキルとして列挙し始めることを期待せよ。

## 4.6 Anthropic の 3 エージェントアーキテクチャ

繰り返される 3 役割パターン、しばしば実践者コミュニティが **Planner / Generator / Evaluator** と要約するもの、が 2025 年を通じてマルチエージェント harness の共通フレーミングとなった。このフレーミングは、Anthropic 自身が一次文書で採用するラベルではなく、Anthropic の [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents)（orchestrator-worker、evaluator-optimizer）が記述するパターンの教育的合成として読むのが最良だ。2026 年 3 月 31 日の Claude Code ソースリーク（本セクション後段でカバー）はこの区別を確認した：本番では、Anthropic の実際の harness は文字通りの 3 役割分解ではなく、層化された self-healing memory を中心に組織されている。役割は依然として有用な分類体系を記述するので、本セクションは関心の分離について議論するためにそれらを使う：

- **Planner：** タスクをサブタスクへ分解し、全体計画を維持し、いつ修正するかを決める。
- **Generator：** 個別サブタスクを実行 ——コードを書く、テキストを起草する、ツールを呼び出す。
- **Evaluator：** Generator の出力をタスク要件に照らして評価し、構造化フィードバックを提供する。

この関心の分離は、本章が **context 不安** と **自己評価バイアス** とラベル付けする 2 つの失敗モードに対処するために広く使われる（ラベルは本ガイドが使うフレーミング；根底にある観察は Anthropic の公開エージェント研究にインスパイアされたパターンに現れる）：

**Context 不安。** 単一エージェントがプランニング、実行、評価を扱うと、ヘッジしがちになる。出力を限定的にし、不要な但し書きを加え、タスク実行ではなくメタコメントにトークンを使う。役割を分けることで、各エージェントが他者の認知負荷を背負わずに集中できる。

**自己評価バイアス。** モデルは自分自身の出力を評価するのが体系的に下手だ。よく文書化された寛容バイアスを示す ——独立な judge より自分の作業を高く評価する。3 エージェントアーキテクチャは、生成された出力に投資のない別個の evaluator（潜在的に異なるモデルや異なる prompt のインスタンス）を使うことでこれを軽減する。

実践者コミュニティが強調してきた、Anthropic の evaluator-optimizer ガイダンスで観察されるパターンと整合する微妙さ：**Evaluator のキャリブレーション自体が harness エンジニアリング問題である**。厳しすぎる evaluator は無限改訂ループを引き起こす。寛容すぎるものは低品質作業を通す。Evaluator の閾値と基準は、generator の指示と同じくらい慎重にチューニングが必要だ。

### Claude Code リーク：経験的覗き見（2026 年 3 月 31 日）

2025 年の大半を通じて、3 エージェントアーキテクチャは Anthropic の公開リサーチを通じて知られ、振る舞いから推論されていた。**2026 年 3 月 31 日**、それが変わった。Anthropic は npm パッケージ **`@anthropic-ai/claude-code` v2.1.88** に 59.8MB の source map を誤って公開、**1,906 ファイルにまたがる約 513,000 行の難読化されていない TypeScript** を露出させた。Anthropic はこの事案を「人為的なパッケージングミスであってセキュリティ侵害ではない」と性格付けたが、実践者がフロンティアラボの本番 harness を直接読めるのは初めてだった。

リークから、コミュニティがアーキテクチャをどう記述するかを再形成するいくつかの発見：

- **文字通り「Planner / Generator / Evaluator」ではない。** Claude Code を 4.6 の 3 役割フレーミングへとマップした初期のコミュニティ記事は、リサーチの誤読だったことが判明した。実際のアーキテクチャは **3 層「Self-Healing Memory」** システムとして組織されている。層はスクラッチパッド/作業状態、圧縮された中期状態、永続的プロジェクト記憶に対応する ——層の間に明示的な修復・調停論理を伴う。
- **`MEMORY.md` は store ではなくインデックスである。** 一枚岩の記憶ファイルではなく、`MEMORY.md` はより詳細なノートへの **軽量なポインタインデックス** として働く。これはトランスクリプトよりファイルシステムディレクトリに近く、context を膨張させずに記憶層がスケールできる理由である。
- **`KAIROS` は自律デーモンモード。** `KAIROS` というフィーチャーフラグがソース全体で **150 回以上** 参照される。これは自律デーモンモード ——大半のユーザーが知る対話的 REPL を遥かに超えた、無人で長時間動く実行ループ —— をゲートする。
- **44 の隠しフィーチャーフラグ。** `KAIROS` を超えて、ソースには未リリース機能のための 44 のフィーチャーフラグが含まれており、公的に出荷されるものは harness が実際に内部でサポートするものの保守的な部分集合であることを示唆する。

実用的な帰結：Planner / Generator / Evaluator 分割は依然として有用な概念的分類体系（そして Anthropic のリサーチ論文はいまだそれらの用語でシステムを記述する）だが、本番ではアーキテクチャは役割分解だけではなく、**記憶と修復** を中心に層化される。2026 年の harness エンジニアリングはますます、記憶層とその間の遷移を設計することを意味する。

リーク 2 週間後、同じアーキテクチャは別の一歩を踏み出した ——今度は外側へ、ユーザーマシンから離れる方向へ。**Claude Code Routines**（2026 年 4 月 14 日）で、Anthropic はオーケストレーターシート自体をラップトップから自身のクラウドへと移し、スケジュール、API、GitHub イベントトリガーを第一級の harness primitive として露出した。リークと並べて読むと、これは明確なアーキテクチャ的修辞である：オーケストレーターはもはやユーザーが付き添う REPL としてモデル化されない、Anthropic の基盤に住むデーモンとしてモデル化される。3 層 self-healing memory はトリガー横断で保たれる；ループが進捗するためにユーザーのプロセスが生きている必要は、もう harness にはない。Routines を採用するかしないかにかかわらず、フレーミングはいま空気中にある：オーケストレーターシートはプロダクトサーフェスであり、「ループがどこで動くか」はデフォルトではなく設計判断だ。

## 4.7 堀としての Harness

2026 年初頭、Meta は Manus を約 20 億ドルで買収した。Manus は独自モデルを持っていなかった。その全価値は harness にあった ——コモディティモデル API を信頼性のあるエージェントプロダクトへと変える、編成論理、context engineering パイプライン、ツール統合層、運用インフラ。

この買収は、業界が発見していたことを結晶化した：**Harness が堀である**。モデルはますますコモディティ化されている。差別化要因はそれをどう包むか ——どんなツールを提供するか、context をどう管理するか、失敗をどう扱うか、多段ワークフローをどう編成するか、品質をどう評価するか —— である。

実践者にとっての含意は、harness エンジニアリングがモデル開発の「本当の仕事」へと向かう道のりに通すための配管ではないということだ。それ*が*、大半の本番 AI チームにとっての本当の仕事だ。2026 年 4 月までに、「harness エンジニアリング」は形式的規律として業界辞書に入り、Claude Code リークが本番 harness が実際に何を含むかの初の経験的覗き見を提供した。

## 4.8 Harness 保守：ストレステストの命法

Anthropic の最も実行可能な洞察は最も単純なものかもしれない：すべての harness コンポーネントはモデル制約についての仮定を符号化しており、**それらの仮定は期限切れになる**。

Harness が GPT-4 級の能力の周りに構築されたとき、それは以下を含んでいたかもしれない：
- 明示的な chain-of-thought prompting（モデルがそれを必要としたから）
- 攻撃的な出力パース（モデルがフォーマットに一貫性がなかったから）
- 多段検証（一発精度が不十分だったから）
- 詳細な few-shot 例（zero-shot 性能が貧弱だったから）

改善された推論、指示追従、出力一貫性を持つ新しいモデルが到来するにつれ、これらのコンポーネントは **もはや荷重を支える必要がないかもしれない荷重を支える壁** となる。品質に貢献せずレイテンシ、コスト、複雑度を加える。

規律は周期的ストレステストだ：harness コンポーネントを体系的に無効化して、どれがまだ必要かを判断する。プランニングステップを除去しても性能が劣化しないなら、除去せよ。モデルが few-shot 例なしでフォーマットを信頼性高く従うなら、それらを落とせ。自己評価がコストを加えるが品質を加えないなら、消せ。

これは直感に反する。エンジニアは本能的に安全機構を加え、それらを除去することに抵抗する。だが harness エンジニアリングでは、不要なコンポーネントは無料ではない ——context window 領域を消費し、レイテンシを加え、コストを増やし、保守負担を作る。現在のモデルの能力にマッチする無駄のない harness は、より弱いモデル向けに過剰設計されたものを上回る。

実用的推奨：新しいモデルをオンボードするとき、既存の harness を動かすところから始め、タスク性能を計測しながら系統的にコンポーネントを剥がせ。残るのがあなたの真の harness だ。除去したものは前の能力時代からの技術的負債だった。

成熟した harness は最終的にストレステスト問題を逆転させる：「どのコンポーネントを除去できるか」と問う代わりに、「どのコンポーネントにより多くの計算を費やすべきか、いつか」と問う。2026 年 4 月の **CATTS** preprint（Consensus-Aware Test-Time Scaling、arXiv 2602.12276）はその問いに使える答えを与える。CATTS はエージェントステップごとにロールアウトの小さな委員会をサンプリングし、それらの間の不一致をステップごとの不確実性スコアとして使う；そのスコアは次に、テスト時計算を非一様に割り当てるために使われる ——委員会が不一致するところにはより多くのロールアウト、収束するところにはより少なく。WebArena-Lite と GoBrowse で、技法は均一スケーリングより **2.3 倍少ないトークン**でタスク精度 **+9.1%** を報告している。成熟した harness にとって、CATTS は Advisor Tool の隣に収まる：advisor パターンが*何について*考えるかを決めるのに対し、CATTS は各ステップを*どれだけ深く*考えるかを決める。両方が、ランタイムに計算される計測された不確実性シグナルで仮定（「常に 3 回再試行する」、「常に難問題に Opus を使う」）を置き換える。

2026 年 4 月の AHE 結果（4.5 節）は構造的に同じ点を作る：ストレステストは一度きりのレビュー活動ではなく、継続的な観測可能性ループだ。手動ストレステストは実践者が今日走らせられる規律として依然として価値があり、AHE はそれが自動化可能でもあることを示す。

## 4.9 クラウドネイティブ harness primitive

2025 年と 2026 年第 1 四半期を通じて、harness は圧倒的に自分で構築し動かすものだった。最も洗練されたパターン ——3 エージェントアーキテクチャ、Advisor Tool、KAIROS スタイルの自律ループ —— ですら、あなたのコードがオーケストレーターシートを保つことを依然として前提としていた。あなたが cron ジョブを書き、デーモンを動かし、ラップトップを起こし続け、失敗モードを所有した。基盤は汎用計算（Mac mini、VPS、Kubernetes pod）で、harness 層はプロセススーパーバイザから上があなたの責任だった。

**2026 年 4 月 14 日**、Anthropic の **Claude Code Routines** リサーチプレビューが、それを変える最初の具体的な一歩を踏み出した。Routine は、ユーザーマシンではなく Anthropic のクラウドで動く Claude Code ワークフローで、3 つのトリガーのいずれかで発火する：**スケジュール**（cron 等価）、**API 呼び出し**（別サービスからのプログラム的呼び出し）、**GitHub イベント**（push、PR、issue、コメント）。トリガーは harness エンジニアが過去 18 か月にわたって書いてきたファイルベース・スケジューリングパターンの意図的な一般化である：同じ「平日 09:00 HKT に毎日走る」セマンティクスを、`cron + tmux + claude` シェル呪文ではなく管理 primitive として表現する。クォータは下層の Claude Code サブスクリプションと階層化されている ——**Pro 5/日、Max 15/日、Team/Enterprise 25/日** —— これは基盤を「シートあたり 1 日数回の意味あるループ」で価格付けし、「時間あたりの生計算」ではない。

クラウド側実行の詳細は聞こえる以上に重要だ。セルフホストのファイルベース・スケジューラはユーザーが所有するハードウェアでオーケストレーターシートを保つ；Mac が閉じている、スリープ、バッテリー切れなら、ループは動かない。Routine はユーザーのマシン状態にかかわらず完了する。これは失敗モードのまるごと一クラス（ラップトップの蓋、ネットワーク切断、OS 更新、偶発的電源サイクル）と対応する補償機構のクラス（Wake-on-LAN トリック、Mac Mini「常時オン」サーバー、冗長ランナー）を溶かし去る。真にイベント駆動のワークフロー ——「PR が開いたら X をする」 —— にとって、管理 primitive はセルフホストポーラーより素直に良い適合だ。

トレードオフは新しい天井である。管理 primitive はワークロードの物理ではなく、トリガーとクォータで価格付けする。あなたのループがスケジュール / API / GitHub イベント形に収まり、1 日あたりクォータが十分で、Anthropic の基盤があなたのコードとデータが住む適切な場所であると仮定する。harness ワークロードの非自明な集合にとって、これらの仮定のどれも綺麗に成り立たない。**ブラウザ自動化**された認証セッションは、ユーザーの cookie、プロファイル、信頼状態を既に持つマシンで動かすことから依然として恩恵を受ける。**高頻度オーケストレーション** ——サブ分単位ポーリング、リアルタイム市場やセンサーデータ、1 日 25 回の呼び出しでは侮辱になる何か —— はトリガーではなく秒単位で課金されるランタイムを必要とする。**非 GitHub イベントソース**（Discord メッセージ、内部 webhook、カスタム MCP サーバー、デバイス上ファイルシステムイベント）にはまだ Routines に第一級トリガーがない；表面化させるにはブリッジを自分で書く必要があり、それはブリッジを動かすためにあなたをセルフホストマシンに戻す。そしてローカルファイル、ローカルモデル推論、ローカルネットワークアクセスに依存するものは構造的にオフクラウドのままだ。

2026 年の harness エンジニアにとっての正直なフレーミング：Routines のようなクラウドネイティブ primitive は、harness ワークロードの **GitHub イベントトリガー、スケジュール、API 呼び出し** 象限にとっての正しい答えで、次の 12 か月でその象限の運用コストを劇的に圧縮する可能性が高い。セルフホスト harness は消え去ってはいない ——実際にコストを払うに値するところに狭められている。発展させるべき規律は、本章が向けて構築してきた同じ規律だ：各コンポーネントがどんな仮定を符号化しているかを知り、その下の基盤が変わったときに気づくこと。

**Routines vs. Managed Agents。** Anthropic が 2026 年 4 月に実際に何を出荷したかを正確にしておく価値がある、というのも 2 つの部分はときに混同されるからだ。**Claude Managed Agents**（パブリックベータ、2026 年 4 月 8 日）は*基盤*である：session（アペンドオンリーのイベントログ）、harness（Claude を呼び出してそのツール呼び出しをルーティングするループ）、sandbox（実行環境）の 3 つの仮想化された構成要素として露出するホスト型ランタイムで、トレーシングと Agent / Environment / Session / Events API サーフェスがその上に重なる。SiliconANGLE のローンチカバレッジは、基盤を標準トークンレート + **エージェント実行時間あたり 8 セント**で価格付けされていると報じている；この数字は二次テックプレスからのもので、一次 Anthropic ドキュメントからではない。二次引用バーであっても、価格構造は重要だ：これはオーケストレーターシート自体を、推論とは別に課金する初のフロンティアベンダー primitive である。**Claude Code Routines**（リサーチプレビュー、2026 年 4 月 14 日）は、その基盤（または互換代替）の上で動く*トリガーサーフェス*である：スケジュール、API 呼び出し、GitHub イベント、Pro / Max / Team-Enterprise 階層で 5 / 15 / 25 回/日のクォータ付き。両者は異なる質問に答える。Managed Agents は「エージェントループは物理的にどこで動くか、その状態はターン間でどう永続的に維持されるか？」に答える。Routines は「そもそもループが始まる原因は何か？」に答える。Routines を採用するが Managed Agents は採用しないセルフホスト harness は、自身の状態と実行環境の所有を保つ；Managed Agents を採用するが独自トリガー層を構築するものは、作業がいつ始まるかの所有を保つ。実践では、2026 年中盤の大半のクラウドネイティブ harness 設計は両方を採用するだろう ——だが unbundling がアーキテクチャ的論点である。Anthropic はもはや「harness」を一つのものとして売っていない；その構成 primitive を売っている。

Unbundling は 2026 年 4 月後半を通じて、構造的に重要な 2 つの動きで継続した。第一に、**4 月 23 日**、Anthropic は **Memory for Managed Agents** をパブリックベータに加えた：ファイルシステムマウント型、監査ログ付きのストアで、エージェントに永続的セッション横断状態を、同時アクセスセマンティクス、スコープ付きエンタープライズ権限、Claude Console でのロールバック / 編集サーフェス付きで与える。基盤はいまや 3 つ目の primitive ——*永続的記憶* —— を session と sandbox と並べて出荷する；3 月 31 日 Claude Code ソースリークが明らかにした本番アーキテクチャ（3 層 self-healing memory）が、いまや他チームがレンタルできるベンダー管理 primitive として露出している。第二に、**4 月 28 日**、AWS と OpenAI は限定プレビューで **OpenAI による Amazon Bedrock Managed Agents** を出荷し、「OpenAI のエージェント harness」を別個のプロダクトサーフェスとして名指して売る初めての時となった。両者を併せて読むと、2 つの出来事は Managed Agents パターンを「Anthropic の 4 月 8 日の賭け」から **クロスベンダー基盤の形** へとシフトする ——3 社のフロンティアベンダーのうち 2 社がいまやオーケストレーターシートを管理 primitive として、エージェント別アイデンティティ、アクションログ、永続的状態を組み込みで出荷する。2026 年中盤にオーケストレーターシートでビルド対バイを比較する harness エンジニアにとって、選択肢集合はもはや単一ベンダーではなく、基盤はもはや薄いランタイムではない：それは記憶を含む。

## 4.10 マネージド推論への転回（2026 年 4 月）

2025 年を通じて、呼び出し側とモデルの間の harness 契約は概ねつまみパネルだった：`temperature`、`top_p`、`top_k`、`max_tokens`、`budget_tokens`、システム prompt。実践者はそれらのつまみをケースバイケースで、ときに同じ agentic ループ内のステップごとに回した。2026 年 4 月 16 日の **Claude Opus 4.7** リリースはそのパターンを破った。単一のリリース内で、3 つの変更が同じ方向を引いた：

1. **`temperature`、`top_p`、`top_k` は廃止予定。** デフォルト以外の値は 400 エラーを返す。サンプリングレベルの制御はもはや呼び出し側の手にない。
2. **Adaptive thinking が唯一の thinking-on モードになる。** 手動 `budget_tokens`（拡張思考）は除去される；`effort`（`low`、`high`、`xhigh`、`max`）が置き換える。
3. **Task budgets が第一級 primitive になる。** 新しいベータヘッダ（`anthropic-beta: task-budgets-2026-03-13`）は、呼び出し側に*agentic ループ全体* ——思考、ツール呼び出し、ツール結果、最終出力 —— の助言的トークンバジェットを宣言させる。モデルは作業しながら走るカウントダウンを見る。

最初の 2 つの変更は引き算的だ：つまみを除去した。3 つ目は足し算的だ：以前どのフロンティア API にもなかった primitive。合わせて契約変更を記述する。「あなたがサンプラーを調整しモデルが応答を生む」の代わりに、契約はいまや「あなたが計算予算を宣言し、モデルがそれに対して自己割り当てし、タスクがまだ値する探索、推論、合成の量をステップごとに決める」となる。Harness はパラメータ盤ではなく予算会話となる。

「強制ではなく助言的」の詳細が重要だ。Task budgets は硬いキャップではない（`max_tokens` が依然としてその役割を果たし、呼び出し側向けのみのままだ）。代わりに、モデルは予算を告げられそれを優先順位付けに使う。実践では、きつすぎる予算は劣化したものではなく拒否風出力を生む ——モデルは資金不足と判断する結果を出荷するより、辞退することを好む。20K トークンの最低値が、まさに非自明なタスクに対するこの失敗モードを防ぐために強制される。

Harness 設計者にとって、含意は具体的だ：Opus 4.6 で動いていたどんな harness も 4.7 のために再ベースラインが必要だ、prompt レベルだけでなくタイムアウト、再試行、圧縮、ツール呼び出し予算レベルでも。Anthropic 自身の移行ドキュメントはこれを直接言う ——*prompt だけでなく、harness を再ベースラインせよ*。Advisor Tool（4.5 節）と task budgets（このセクション）は、長期視野のどんな harness にも新しい 2 軸最適化を記述する：Advisor は*何について*考えるかを決める；task budgets は各ステップを*どれだけ深く*考えるかを決める。両方が、ランタイムに計算される計測されたシグナルで、つまみいじりを置き換える。

これがより広いパターンだ：**マネージド推論への転回**。フロンティアベンダーはますます推論自体を、パラメータサーフェスではなくプロダクトサーフェスとして扱う。Harness 層は「あなたが推論呼び出しを設定する」から「あなたが作業を記述し推論層が適応する」へと移っている。他のラボが Anthropic の特定の判断（サンプリングつまみの廃止、助言的予算）を追うか方向だけを追うかは未解決の問いだ。方向自体は決着したように見える。

---

## Sources

- **Böckeler, Birgitta.** "Harness engineering for coding agent users." martinfowler.com (Exploring Generative AI series), April 2, 2026. [https://martinfowler.com/articles/harness-engineering.html](https://martinfowler.com/articles/harness-engineering.html) — Guides vs. Sensors、Computational vs. Inferential 分類体系。
- **OpenAI.** Codex 公式素材：[https://openai.com/index/introducing-codex](https://openai.com/index/introducing-codex)。OpenAI Codex の harness 設計フレーミングのアンカー；広く引用される「3 人のエンジニア / ~100 万行 / ~1,500 件の PR」の数字は 2025–2026 年の OpenAI トークと投稿で流通したもので、単一の典拠投稿からではなくコミュニティ引用としてここに記載する。
- **IMPACT 記憶法。** Intent / Memory / Planning / Authority / Control flow / Tools — 2020 年代中頃の実践者言説で浮上した 6 次元の harness 設計チェックリスト。本章では教育的フレーミングとして用い、特定の一次出典には帰属させない。
- **Stanford / MIT / KRAFTON.** "Meta-Harness: Automated Optimization of LLM Agent Harnesses." arXiv preprint, March 2026. 6 倍性能ギャップ発見、自動 harness チューニング。
- **Lin et al.** "Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses." arXiv 2604.25850, April 28, 2026. [https://arxiv.org/abs/2604.25850](https://arxiv.org/abs/2604.25850) — 復旦 / 北京 / 上海期智智峰。Meta-harness 探索問題の観測可能性柱による再フレーミング；Terminal-Bench 2 で 69.7% → 77.0%、クロスファミリー転送付き。
- **Anthropic.** "Claude Managed Agents overview." API documentation, April 8, 2026. [https://platform.claude.com/docs/en/managed-agents/overview](https://platform.claude.com/docs/en/managed-agents/overview)
- **Anthropic Engineering.** "Scaling Managed Agents: Decoupling the brain from the body." April 8, 2026. [https://www.anthropic.com/engineering/managed-agents](https://www.anthropic.com/engineering/managed-agents) — 3 つの仮想化された構成要素（session、harness、sandbox）；価格詳細（標準トークンレート + エージェント実行時間あたり 8 セント、SiliconANGLE ローンチカバレッジによる）は一次 Anthropic ドキュメントにはなく、二次テックプレスから引用する。
- **Anthropic.** "Memory for Claude Managed Agents" (April 23, 2026). [https://claude.com/blog/claude-managed-agents-memory](https://claude.com/blog/claude-managed-agents-memory) — ファイルシステムマウント型記憶、セッション横断学習、監査ログ、スコープ付きエンタープライズ権限；3 月 31 日 Claude Code ソースリークの 3 層 self-healing memory 発見でループを閉じる。
- **AWS and OpenAI.** "Bedrock Managed Agents powered by OpenAI" (April 28, 2026, limited preview). AWS announcement: [https://aws.amazon.com/about-aws/whats-new/2026/04/bedrock-openai-models-codex-managed-agents/](https://aws.amazon.com/about-aws/whats-new/2026/04/bedrock-openai-models-codex-managed-agents/). About Amazon: [https://www.aboutamazon.com/news/aws/bedrock-openai-models](https://www.aboutamazon.com/news/aws/bedrock-openai-models). OpenAI announcement: [https://openai.com/index/openai-on-aws/](https://openai.com/index/openai-on-aws/) — 「OpenAI のエージェント harness」がプロダクトサーフェスとして名指し売られる初めての時；Managed Agents パターンへのクロスベンダー収束。
- **Anthropic.** "Building Effective Agents." Anthropic engineering blog, December 19, 2024. [https://www.anthropic.com/engineering/building-effective-agents](https://www.anthropic.com/engineering/building-effective-agents) — orchestrator-worker パターンと evaluator-optimizer ワークフローを記述する；本ガイドは関連する失敗モードに「context 不安」と「自己評価バイアス」のラベルを教育的に付与する。実践者コミュニティが Planner / Generator / Evaluator 三項として要約するものはこれらのパターン上に構築されたフレーミングであり、Anthropic 自身は一次文書でその正確な三項を使っていない。実際の Claude Code アーキテクチャは、2026 年 3 月 31 日のソースリーク（4.6 節）が明らかにしたように、役割分解ではなく層化された self-healing memory を中心に組織されている。
- **Meta / Manus 買収。** 各種報道、2026 年初頭。Harness を堀とするテーゼを妥当化した約 20 億ドル買収。
- **Karpathy, Andrej.** "From Vibe Coding to Agentic Engineering" — Sequoia AI Ascent 2026 でのファイアサイドチャット（録画 ~2026 年 4 月後半、一次 YouTube 動画 [https://www.youtube.com/watch?v=96jN2OCOfLs](https://www.youtube.com/watch?v=96jN2OCOfLs)；著者要約 [https://karpathy.bearblog.dev/sequoia-ascent-2026/](https://karpathy.bearblog.dev/sequoia-ascent-2026/)）。Vibe coding を*床上げ*モード（誰もが構築できる）として、agentic engineering を*天井上げ*規律（仕様、計画監督、diff 検査、eval ループ、権限スコーピング、worktree 分離）として枠付ける。Karpathy 自身がコーディング比率を ~80% 手書きから ~80% 委任へと反転させたと報告する 2025 年 12 月の転換点を錨とする。2025 年初期の "Software 3.0" / "Software Is Changing (Again)" トーク（AI Engineer World's Fair、YC AI Startup School）が、新種のプログラム可能コンポーネントとしてのモデルというより広いフレームを確立した。
- **LangChain.** "Agent Architecture Patterns." LangChain documentation, 2025. 制御フローとツール編成のための実用パターン。
- **Harrison Chase.** "Agent Engineer" フレーミング、2025 — LangChain ブログと X 投稿。この語句は harness 焦点エンジニアリングの役割定義フレーミングとして実践者語彙に入った；単一の典拠投稿ではなく 2025 年代言説のパターンとしてここに引用する。
- **"CATTS: Consensus-Aware Test-Time Scaling for Agents."** arXiv 2602.12276 (April 2026 release cycle). 投票由来の不確実性をテスト時計算割り当て器として；WebArena-Lite と GoBrowse で均一スケーリング比 +9.1% / 2.3 倍少ないトークン。[https://arxiv.org/abs/2602.12276](https://arxiv.org/abs/2602.12276)
- **Anthropic.** "Introducing Routines in Claude Code." Anthropic blog, April 14, 2026. [https://claude.com/blog/introducing-routines-in-claude-code](https://claude.com/blog/introducing-routines-in-claude-code)
- **Anthropic.** "Claude Code Routines documentation." [https://code.claude.com/docs/en/routines](https://code.claude.com/docs/en/routines) — トリガー（スケジュール / API / GitHub イベント）、クォータ（Pro 5/日、Max 15/日、Team/Enterprise 25/日）、クラウド側実行セマンティクス。
- **Anthropic.** "Introducing Claude Opus 4.7" (April 16, 2026). [https://www.anthropic.com/news/claude-opus-4-7](https://www.anthropic.com/news/claude-opus-4-7)
- **Anthropic.** "What's new in Claude Opus 4.7" (API documentation). [https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-7](https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-7) — task budgets（`anthropic-beta: task-budgets-2026-03-13`、助言的、20K 最低）、adaptive のみの thinking、`temperature` / `top_p` / `top_k` の除去。
- **Caylent.** "Claude Opus 4.7 Deep Dive: Capabilities, Migration, and the New Economics of Long-Running Agents" (April 2026). [https://caylent.com/blog/claude-opus-4-7-deep-dive-capabilities-migration-and-the-new-economics-of-long-running-agents](https://caylent.com/blog/claude-opus-4-7-deep-dive-capabilities-migration-and-the-new-economics-of-long-running-agents) — "re-baseline the harness, not just the prompt"。
- **Archon GitHub Repository.** [https://github.com/coleam00/Archon](https://github.com/coleam00/Archon) — TypeScript / Bun harness ビルダー、Claude Code と OpenAI Codex CLI をラップする YAML DAG ワークフロー；v2.1 は 2026 年 4 月に出荷。
- **OpenHarness GitHub Repository.** [https://github.com/HKUDS/OpenHarness](https://github.com/HKUDS/OpenHarness) — 香港科技大学データラボからの Python 参照実装；初コミット 2026 年 4 月 1 日。

### 初心者向けのさらに読むこと

- **Cab.** "A Layer-by-Layer Walk Through Harness Engineering." 繁体中文エッセイ、2026。単一の `POST /v1/messages` 呼び出しから始めて、prompt engineering、関数呼び出し、エージェントループ、最終的に完全な harness 複雑度へと積み上げる。注目すべきは "模型從來都沒有長手" メタファ ——ツール使用をモデル能力ではなく harness 問題として再フレーミングする —— と、Claude Code の harness が裏で実際に何をしているかを明示的に歩くこと。本章の理論優先のフレーミング（Böckeler 分類体系、IMPACT、Meta-Harness）を読む前の優しいオンランプとして推奨。
- **Anthropic.** ["Building Effective Agents"](https://www.anthropic.com/research/building-effective-agents) — リサーチ背景でない読者にとっての典拠的短形式入門。上の Cab エッセイとよく組む：Cab は積み上げを与え、Anthropic は具体的パターンを与える。
