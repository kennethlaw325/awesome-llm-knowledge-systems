# 第 1 章：3 つの世代

> **一文で：** AI エンジニアリングは、よい prompt を書くことから、AI モデルの周囲に OS 全体を設計することへと進化した。
>
> **なぜ重要か：** この分野がどこに向かっているかを理解すれば、適切なツールを選び、時代遅れのアプローチを避けられる。

**Prompt engineering から context engineering、そして harness engineering へ —— そして三者の境界は思っているほど重要ではない理由。**

---

## 第 1 世代：Prompt Engineering（2022–2024）

2022 年 11 月に ChatGPT が公開されたとき、人間と大規模言語モデルとのインターフェースは丸ごとテキストボックス 1 つだった。そこから生まれた分野が prompt engineering ——よりよい出力を得るために入力テキストを設計する技芸であり科学である。

中核となる手法は急速に発展した：

**Few-shot prompting**（Brown 他, 2020）は、prompt に例を含めるだけで、ファインチューニングなしでもタスク性能が劇的に改善されることを示した。感情分類のためにモデルを訓練するのではなく、例を 3 つ示して 4 つ目を分類させるのである。

**Chain-of-thought (CoT) prompting**（Wei 他, 2022）は、「Let's think step by step」と付け加えるか、例に推論過程を含めるだけで、標準的な prompting では現れなかった多段推論能力が引き出されることを示した。これはおそらく、「文脈をどう構造化するか」が「何を尋ねるか」と同じくらい重要であるという、最初の手がかりだった。

**Prompt templates** は標準的な抽象化となった。LangChain、LlamaIndex、その他多数のフレームワークが、慎重に設計された prompt 構造に変数を注入できるテンプレートシステムを提供した。メンタルモデルは明確だった：prompt がプログラム、モデルがランタイム。

この時代のその他の手法には以下が含まれる：

- **ReAct**（Yao 他, 2022）：推論ステップと行動ステップを交互に行い、モデルが単一の prompt 構造の中で計画とツール呼び出しを実行できるようにする。
- **Tree of Thought**（Yao 他, 2023）：複数の推論経路を探索し、最良のものを選ぶ。
- **Self-consistency**（Wang 他, 2022）：複数の推論連鎖をサンプリングし、多数決を取る。

この時代の限界は、その前提にあった：LLM とのやり取りの質は、主として prompt の質によって決まる、という前提である。これは context window が 4K–8K トークンで、入力がユーザーテキストのみだった時代には正しかった。モデルが 10 万トークン以上を取り込み、外部ツールを呼び出せるようになると、この前提は通用しなくなった。

### この時代が捉えていたこと

Prompt engineering は、*構造が重要である*ことを確立した。よい prompt と悪い prompt の差は感覚ではなく ——それは情報アーキテクチャである。この洞察は、その後のすべてに引き継がれた。

### この時代が見落としていたこと

Context window を静的な成果物として扱っていた。prompt を作り、送信し、応答を得る。Context window 自体が、実行時に複数のソースから *動的に構築されうる* という発想 ——それが次世代の洞察だった。

---

## 第 2 世代：Context Engineering（2025）

2025 年中頃、Andrej Karpathy が AI エンジニアリングコミュニティで最も拡散された観察の一つを投稿した：

> 「私はこれについて考えてきたが、ほとんどの人が実際に上達すべきものに対する正しい用語は『prompt engineering』ではなく『context engineering』だと思う。次のステップに必要な情報をちょうどよく context window に詰める技芸であり科学である。」

このリフレーミングが重要なのは、注目を「指示」（prompt）から「情報パッケージ全体」（context window）へと移したからだ。現代の LLM 呼び出しの context window には、ユーザー prompt よりずっと多くのものが入っている：

- 振る舞いと制約を定義するシステム指示
- RAG パイプラインから取得した文書
- ツール定義とスキーマ
- 会話履歴（選択的に圧縮されたもの）
- 動的に選ばれた few-shot 例
- 現在のタスクに関する構造化メタデータ

Prompt は 1 構成要素にすぎない。Context engineering とはこれら全部を編成することだ。

### 6 つの手法

[Towards AI の分析](https://towardsai.net/) は、この分野を定義する 6 つの中核的手法を特定した：

1. **Retrieval-Augmented Generation (RAG)**：問い合わせ時に関連文書を引いてくる
2. **Tool と API の統合**：構造化スキーマでモデルに外部能力へのアクセスを与える
3. **Memory management**：会話のターンとセッションを越えて関連情報を保持する
4. **動的 prompt 構築**：テンプレート、取得コンテンツ、実行時状態から prompt を組み立てる
5. **Context window の最適化**：限られたトークン予算に何を入れ何を残すかを管理する
6. **指示階層**：システム、開発者、ユーザーの指示を明確な優先順位で階層化する

### Manus からの教訓

[Manus](https://manus.im/) ——2025 年に最も語られた AI エージェントプラットフォームの一つ —— は、スケールにおける context engineering について重要な教訓を共有した：

**KV-cache の洞察**：Manus は、KV-cache のヒット率を高く保つよう context window を設計した ——アテンション機構で計算済みの key-value ペアをターンを越えて再利用できるようにしたのである。これによりレイテンシとコストが劇的に下がった。原則：呼び出し間で*プレフィックスは安定*させ、*サフィックスのみが変わる*ように context を構造化せよ。

**100:1 の比率**：Manus は、モデル出力 1 トークンに対して context が約 100 トークン消費されると報告した。これは出力トークンが主要なコスト要因だという一般的な前提を逆転させた。本当のエンジニアリング課題は、テキスト生成ではなく ——*どの context を投入するかを選ぶこと*だった。

**プロダクトとしての context**：Manus は context window の構築を、実装上の細部ではなく中核となるプロダクト機能として扱った。エージェントの品質は、context 組み立てパイプラインの品質に直接比例した。

### 分類体系のシフト

Context engineering は LLM アプリケーション開発を「よい prompt を書く」から「よい情報パイプラインを作る」へとリフレーミングした。モデルは受け取った context 上で動作する推論エンジンとなった。エンジニアリング課題は上流に移った ——検索、フィルタリング、ランキング、圧縮、組み立てへ。

しかし、このフレーミングにも天井があった。それは*モデルに何が入るか*を記述したが、*モデルの周りのシステムがどう動作するか*は記述しなかった。それにはもう一段のシフトが必要だった。

---

## 第 3 世代：Harness Engineering（2026）

2025 年後半から 2026 年初頭にかけて、影響力のある 2 つの作品が次の進化を形式化した：

**Birgitta Böckeler**（ThoughtWorks）は、Martin Fowler の *Exploring Generative AI* メモシリーズに 2026 年 4 月に寄稿した分析の中で、LLM アプリケーションにおける最も影響力の大きいエンジニアリング作業は、モデル訓練でも prompt 設計でもなく、*harness* —— モデル呼び出しを信頼性のあるワークフローへと編成する、ツール、ルーティング、メモリ、プランニング、エラーリカバリの周辺システム ——で起きていると論じた。

**OpenAI の Codex チーム**は、エージェント的コーディングの harness 側についてのケーススタディ素材を公開している（公式素材は openai.com/index/introducing-codex を参照）。広く引用される「3 人のエンジニア / 約 100 万行 / 約 1,500 件の PR」という数字は 2025–2026 年の OpenAI トークと投稿で流通したもので、根底にある観察は、Codex の品質は主としてモデルではなく harness ——*いつ*モデルを呼ぶか、*どんな context* を提供するか、*どのツール*を使えるようにするか、エラーをどう検証し回復するかを決めるシステム ——によって決まったということだ。

### Phil Schmid のアナロジー

[Phil Schmid](https://www.philschmid.de/)（Hugging Face）は、この概念を結晶化させたアナロジーを示した：

- **モデルは CPU** —— 生の計算能力
- **Context window は RAM** —— 現在の操作のための作業メモリ
- **Harness は OS** —— スケジューリング、リソース管理、I/O、エラーハンドリング、ユーザーインターフェース

このアナロジーは、なぜ harness engineering が重要かを明らかにする：CPU だけを OS なしで出荷する者はいない。モデルは必要だが十分ではない。モデルが実際に何を達成できるかを決めるのは harness である。

### Meta-Harness 論文と 6 倍のギャップ

2026 年初頭に公表された研究は、現場の実践者が薄々感じていたことを定量化した：素のモデルとうまく harness されたモデルとのギャップは、**複雑なタスクで約 6 倍**だった。同じ重み、同じ訓練データの同じモデルが、harness の質によって 6 倍の差で異なる結果を生み出した。

これは、ほとんどの実用アプリケーションにとって harness engineering がモデル改善より大きいレバレッジを提供することを意味した。よいモデルに優れた harness をかぶせる方が、平凡な harness の偉大なモデルを上回った。

### IMPACT フレームワーク

2020 年代中頃の実践者の言説の中で、harness の品質を評価するチェックリストとして IMPACT という記憶法が浮上した：

- **I**nstructions —— システム指示の明確さと完全性
- **M**emory —— セッション横断の永続化と取得
- **P**lanning —— タスク分解とシーケンシング
- **A**ctions —— ツールの可用性と信頼性
- **C**ontext —— 関連情報の動的組み立て
- **T**esting —— 評価と品質保証ループ

IMPACT は context engineering を、より広い harness engineering 分野の中の 1 構成要素（「C」）として位置付ける。この入れ子構造こそが鍵となる構造的洞察である：context engineering は harness engineering に*置き換えられる*のではなく、その*中にある*。

### Meta が Manus を買収（約 20 億ドル）

2026 年初頭、Meta は Manus を約 20 億ドルで買収した。この買収は広く、Meta が*モデルではなく harness を買った*と解釈された。Meta はすでに Llama を持っていた。持っていなかったのは、context 組み立て、ツール編成、エージェントランタイム管理の本番証明済みシステムだった。

この買収は次のテーゼを裏付けた：LLM エコシステムで最も価値のあるエンジニアリングは、ますますモデル層ではなく編成層に移っている。

---

## 鍵となる洞察：置き換えではなく共存

これら 3 世代は、ある世代が次の世代に取って代わる、すっきりとした歴史的時期ではない。これらは本番システムの中で共存する*入れ子の層*である：

```
+--------------------------------------------------+
|              HARNESS ENGINEERING                  |
|  +--------------------------------------------+  |
|  |          CONTEXT ENGINEERING                |  |
|  |  +--------------------------------------+  |  |
|  |  |       PROMPT ENGINEERING             |  |  |
|  |  |                                      |  |  |
|  |  |  System prompts, CoT, few-shot,      |  |  |
|  |  |  instruction formatting              |  |  |
|  |  +--------------------------------------+  |  |
|  |                                            |  |
|  |  RAG pipelines, memory, tool schemas,      |  |
|  |  context window optimization               |  |
|  +--------------------------------------------+  |
|                                                  |
|  Skill routing, planning loops, error recovery,  |
|  progressive disclosure, multi-agent coord       |
+--------------------------------------------------+
```

Harness エンジニアは依然として prompt を書く。依然として context engineering を行う。しかし加えて、いつどの prompt を使うか、状況ごとにどんな context を組み立てるか、問題が起きたらどう回復するかを決める*システム*を構築する。

進化は、それまでの手法を捨てることではない。それらが必要だが不十分であることを認め —— その上に層を重ねて、生の LLM 能力を信頼性のある本番グレードのアプリケーションへと変えることである。

上海交通大学らの 19 著者によるサーベイ **"Externalization in LLM Agents: A Unified Review of Memory, Skills, Protocols and Harness Engineering"**（arXiv 2604.08224、2026 年 4 月 9 日）は、本章が用いるのと同じ三層構成に独立して到達している：彼らのフレーミングでは、この分野の進展は *weights* から *context* へ、そして *harness* へと進み、memory・skills・protocols・harness engineering の 4 つを、harness を統合層とする外在化された構成要素として扱う。学術文献から本書に来る読者には、この収束を明示的に指摘しておく価値がある：これは実践者だけのフレーミングではないし、本ガイド独自のものでもない —— 2026 年 4 月後半の学術サーベイも同じ構成軸を選んだ。

---

## Sources

- Brown, T. et al. (2020). "Language Models are Few-Shot Learners." [arXiv:2005.14165](https://arxiv.org/abs/2005.14165)
- Wei, J. et al. (2022). "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models." [arXiv:2201.11903](https://arxiv.org/abs/2201.11903)
- Yao, S. et al. (2022). "ReAct: Synergizing Reasoning and Acting in Language Models." [arXiv:2210.03629](https://arxiv.org/abs/2210.03629)
- Yao, S. et al. (2023). "Tree of Thoughts: Deliberate Problem Solving with Large Language Models." [arXiv:2305.10601](https://arxiv.org/abs/2305.10601)
- Wang, X. et al. (2022). "Self-Consistency Improves Chain of Thought Reasoning in Language Models." [arXiv:2203.11171](https://arxiv.org/abs/2203.11171)
- Karpathy, A. (mid-2025). "context engineering" を本分野の正しい用語として提唱した公の発言。X および AI エンジニアリングコミュニティで広く共有されたフレーミング。
- Manus. (2025). "Context Engineering Lessons from Building Manus." [manus.im/blog](https://manus.im/blog) —— 運用指標としての KV-cache ヒット率、append-only な context、logit bias によるツールマスキング、ローリングな todo-list 書き換え。
- Böckeler, Birgitta. (April 2, 2026). "Harness engineering for coding agent users." martinfowler.com（*Exploring Generative AI* シリーズ）。[https://martinfowler.com/articles/harness-engineering.html](https://martinfowler.com/articles/harness-engineering.html) —— Guides vs. Sensors、Computational vs. Inferential の分類体系。
- OpenAI. Codex 公式素材：[https://openai.com/index/introducing-codex](https://openai.com/index/introducing-codex)。Codex の harness 設計フレーミングのアンカー。広く引用される「3 人のエンジニア / 約 100 万行 / 約 1,500 件の PR」の数字は 2025–2026 年の OpenAI トークと投稿で流通したもので、単一の典拠投稿からではなくコミュニティ引用としてここに記載する。
- Schmid, Philipp. "The New Skill in AI is Not Prompting, It's Context Engineering" および続編。[https://www.philschmid.de/context-engineering](https://www.philschmid.de/context-engineering)；[https://www.philschmid.de/context-engineering-part-2](https://www.philschmid.de/context-engineering-part-2) —— Model = CPU、Context = RAM、Harness = OS のアナロジー。
- IMPACT 記憶法。Intent / Memory / Planning / Authority / Control flow / Tools —— 2020 年代中頃の実践者言説で浮上した 6 次元の harness 設計チェックリスト。本章では教育的フレーミングとして用い、特定の一次出典には帰属させない。
- Meta/Manus 買収報道。(2026). 各種ソース。
- Zhou, C. et al. (April 2026). "Externalization in LLM Agents: A Unified Review of Memory, Skills, Protocols and Harness Engineering." [arXiv:2604.08224](https://arxiv.org/abs/2604.08224) —— 上海交通大学らによる 19 著者のサーベイ。Weights → Context → Harness という三層歴史的フレーミングを独立して用いる。本章「置き換えではなく共存」節で、実践者のテーゼが学術文献と収束した証拠として引用。

---

*次の章: [第 2 章 —— RAG、ロングコンテキストとナレッジグラフ](02-knowledge-layer.md)*
