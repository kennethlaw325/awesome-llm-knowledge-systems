# 第 9 章：中国 AI ナレッジエンジニアリングランドスケープ

> **一文で：** 中国は独自のオープンソースプラットフォーム、モデル、コミュニティを持つ並行 AI エコシステムを構築した ——しばしば西側とは異なる方向に革新する。
>
> **なぜ重要か：** 世界の AI リサーチャーの半分は中国にいる。このエコシステムを無視することは革新の半分を見逃すことを意味する。

![Chinese vs Western AI Knowledge Engineering](../../../diagrams/china-comparison.png)

LLM ナレッジエンジニアリングについてのグローバルな会話は、中国エコシステムを検討せずには不完全だ。2025 年 12 月までに 748 を超える AI サービスが規制当局に届け出されており、中国は大規模言語モデルでナレッジシステムを構築する並行的な ——いくつかの領域では発散的な —— アプローチを発展させた。本章は中国の開発者と企業がナレッジエンジニアリングにどうアプローチするかを形作る、鍵となるプラットフォーム、モデル、文化的差異を地図化する。

## A. オープンソース RAG とエージェントプラットフォーム

中国のオープンソース AI エコシステムは、GitHub 人気で西側相当物に匹敵するか超えるいくつかのプラットフォームを生み出した。これらのプロジェクトを区別するのは、ビジュアルワークフロー、エンタープライズデプロイメント準備、深い文書理解への強調 ——中国エンタープライズ顧客の実用的需要を反映する —— である。

### Dify（13 万 6 千以上の GitHub スター）

[Dify](https://github.com/langgenius/dify) はグローバルに最も多くスターを集めるエージェント AI プラットフォームだ。Apache 2.0 ライセンス、RAG パイプライン、エージェントワークフロー、多段推論チェーンを構築するためのビジュアルキャンバスを提供する。バージョン 1.0 以来、Dify は Model Context Protocol (MCP) をサポートし、外部ツールサーバーとのシームレスな統合を可能にする。その強みは、視覚的にワークフローを設計するノーコードユーザーと、プログラム的制御を必要とする開発者の間のギャップを埋めることにある。エンタープライズユーザーは全スタックをセルフホストできる、これは中国市場で臨界的だ、というのもデータ主権要件がしばしばクラウドのみの解を排除するからだ。

### RAGFlow（6 万 2 千～ 7 万 5 千以上の GitHub スター）

[RAGFlow](https://github.com/infiniflow/ragflow) は深い文書理解で差別化する。文書をフラットなテキストとして扱う代わりに、RAGFlow はスキャン PDF、スプレッドシート、スライドデックを含む 20+ ファイル形式にレイアウト認識パース、OCR、表抽出を適用する。「Agentic RAG」アプローチは、システムがクエリタイプに基づいてどの検索戦略を適用するかを自律的に決められることを意味する。レガシー文書アーカイブを扱うエンタープライズ ——中国の国有企業と製造業でよくあるシナリオ —— にとって、この能力はあったらいいねではなく要件だ。

### FastGPT（2 万 7 千以上の GitHub スター）

[FastGPT](https://github.com/labring/FastGPT) はリソース効率に焦点を当てたエンタープライズナレッジベース Q&A をターゲットとする。QA-pair 抽出パイプラインは文書を自動的に質問・回答ペアに変換し、検索とファインチューニングの両方に使える。プラットフォームは 2GB ほどの RAM のマシンで動くよう設計され、専用 GPU インフラを買えない中小企業にアクセスしやすくする。この倹約は中国エコシステムのより広いパターンを反映する：制約下での最適化。

### MaxKB（1 万 8 千以上の GitHub スター）

[MaxKB](https://github.com/1Panel-dev/MaxKB) は、ワンクリックデプロイメントのエンタープライズエージェントプラットフォームとして自身を位置付ける。ツール統合のための MCP をサポートし、一般的なエンタープライズシナリオ（カスタマーサービス、内部知識検索、文書要約）のための事前構築テンプレートを提供する。その魅力は、「AI アシスタントが欲しい」から「動いている」までの時間を週から時間に減らすことにある。

### Coze Studio（1 万 5 千以上の GitHub スター、ByteDance）

[Coze Studio](https://github.com/coze-dev/coze-studio) は ByteDance のオープンソース・ビジュアルエージェント開発プラットフォームだ。元はクローズドプロダクトだったが、ByteDance が 2025 年 7 月にオープンソース化し、3 日以内に GitHub スター 1 万を集めた ——抑圧された需要と ByteDance の流通力の両方の証だ。Coze Studio は組み込みの記憶、ツール使用、多ターン会話管理を伴うエージェント構築のためのドラッグアンドドロップインターフェースを提供する。ByteDance の Doubao モデル族との統合は、中国語タスクでネイティブな優位性を与える。

### DB-GPT（1 万 7 千以上の GitHub スター）

[DB-GPT](https://github.com/eosphoros-ai/DB-GPT) は AI ネイティブデータ相互作用に特化する。中核能力は自然言語から SQL への変換で、非技術ユーザーがデータベースを会話的にクエリできるようにする。視覚化生成とマルチエージェントデータ分析パイプラインでこれを拡張する。大規模構造化データセットの上に座るエンタープライズ ——金融、物流、製造の大半の中国企業を記述する —— にとって、DB-GPT は AI 強化分析へのアクセス可能なエントリポイントを提供する。

## B. ナレッジ管理向け中国 LLM

中国の基盤モデルランドスケープは急速に成熟し、いくつかのモデルが今や西側相当物と特定ベンチマークで競合する、または優れる。

### Qwen3（Alibaba Cloud）

Qwen3 は Alibaba のフラッグシップモデル族だ。最大の亜種は Apache 2.0 で公開された 2,350 億パラメータの Mixture of Experts（MoE）モデル。Qwen3-Coder-480B、コーディング専門亜種は 256K から 1M トークンの context window をサポートする。Apache 2.0 ライセンスは戦略的に重要だ：無制限の商用利用を可能にし、独自 API コストを買えない中国スタートアップ全体での採用を駆動した。Qwen の多言語能力は中国語、日本語、韓国語で特に強い ——西側モデルが歴史的に劣る言語。

### DeepSeek R1

DeepSeek R1 は数学・科学推論ベンチマークで OpenAI の o1 に並びながら MIT ライセンスで公開された。モデルは 600 万ドル未満で訓練されたと報じられ、比較可能な西側モデルのほんの一部だ。このコスト効率は業界に衝撃を送った：中国でのオープンソースモデルのエンタープライズ採用は公開後数か月で 23% から 67% へ跳ね上がった。DeepSeek R1 はフロンティアレベルの推論にフロンティアレベルの予算が必要ないことを実証し、ナレッジエンジニアリングの経済学を根本的にシフトさせた。

2026 年 4 月、DeepSeek は **manifold-constrained hyper-connections (mHC)** で、Transformer++ 風モデルで使われる残差接続の一般化、アーキテクチャ的貢献を拡張した。標準的な residual stream が層横断で単一の情報チャネルを前進させるのに対し、mHC は **複数の内部ストリーム** を運び、それぞれが学習された低次元多様体に存在するよう制約される。構造は、単純なマルチストリーム残差がスケールで被る次元崩壊なしに、後の層が初期表現により豊かにアクセスすることを可能にするよう設計される。DeepSeek のブログは同程度のパラメータ数で長期視野推論ベンチマークでの利得を報告し、最大の改善は情報が多くの介在層を越えて運ばれる必要のあるタスクで起こる。2026 年 4 月時点で結果は **独立な再現を待つものとしてフラグされるべき** だ ——単一ラボのモデルの単一ラボ開示であり、この分野は第三者再現を生き残らなかったアーキテクチャ的主張で焼かれてきた。結果が成立すれば、mHC は MoE、MLA、DeepSeek の早期のマルチトークン予測作業に並ぶ、メインストリーム使用に渡る前に中国オープンウェイトエコシステムから生まれた 3 つ目か 4 つ目のアーキテクチャ的 primitive となる。

### DeepSeek V4（2026 年 4 月）

DeepSeek の **V4 プレビュー**（2026 年 4 月 24 日）は R1 物語を 3 軸で同時に拡張する：経済学、能力、**推論基盤**。リリースは MIT ライセンスで Hugging Face に 2 つのオープンウェイト Mixture-of-Experts モデルを出荷する ——**V4-Pro が 1.6 兆パラメータ / 49B アクティブ**、**V4-Flash が 284B / 13B アクティブ** —— デフォルトとして 100 万トークン context window 付きで、層としてではなく。API 価格は 2026 年のフロンティアクラスモデルで最も攻撃的だ：**V4-Flash が出力百万トークンあたり $0.28**、V4-Pro が $3.48、ハードウェア最適化単独ではなくアーキテクチャ的変更で駆動された V3 比 **トークンあたり推論 FLOPs 73% 削減** を反映する。コーディングベンチマーク ——R1 が最初に信頼性を確立した領域 —— で、V4-Pro はリーダーボード首位を取り、**LiveCodeBench 93.5%**（Gemini 3.1 Pro の 91.7% と Claude Opus 4.6 の 88.8% を抜く）と **Codeforces レーティング 3206**（GPT-5.4 の 3168 を上回る）。

ただしこの章にとって最も重要な構造的詳細は価格でもベンチマークでもなく、**推論基盤** だ。V4 の訓練には NVIDIA A100 と H20 ハードウェアを含むハイブリッドクラスタが用いられた ——フロンティア*訓練*が NVIDIA スタックの完全に外側で起こりうるかという質問は依然として困難だ。だがモデルは **Huawei の Ascend 950PR にデイゼロで適合**された。DeepSeek と Huawei が共同で、本番でモデルをサーブする Ascend NPU と NVIDIA GPU の間で推論パリティ ——そしてこのアーキテクチャでは NVIDIA H20 比でおよそ **2.8 倍の計算スループット** —— を報告している。これは sovereign-silicon テーゼのより微妙な形だ：「NVIDIA なしで訓練した」ではなく **「NVIDIA なしでサーブする」**。米国輸出規制に直面する中国エンタープライズ顧客にとって、V4 はフロンティアクラスのオープンウェイトモデルが信頼できる国内シリコン サービングパス付きで初日に出荷された初めてだ ——本章が記述してきたデプロイメント重い中国エコシステムにとって、これは訓練の選択性より荷重を支える制約に近い。R1 の 2025 年 1 月転換点と並べて読むと、V4 は 1 年がかりの物語の弧を閉じる：中国オープンウェイトエコシステムは、フロンティアコーディングモデル**と**それをサーブする基盤を、同じ日にリリースできるようになった。

### Kimi K2.5（Moonshot AI）

Kimi K2.5 は「Agent Swarm」を導入した ——単一クエリが最大 100 のサブエージェントを派生させ、約 1,500 のツール呼び出しを通して協調できる能力。これはリサーチデモではない；複数同時エージェントにまたがってウェブ検索、文書分析、合成を並列化する複雑なリサーチタスクで使われる本番機能だ。それ以前、Kimi は 200 万中国語文字の context window を達成していた（約 2025 年 3 月）、中国語テキストに特化して最適化された最長 context モデルとなった。

### ERNIE 5.0（百度）

ERNIE 5.0 は百度の 2.4 兆パラメータのモデルで、ネイティブの完全モダリティサポート ——テキスト、画像、音声、動画の理解と生成を単一モデルで —— を持つ。2026 年 1 月にローンチされ、ナレッジシステムの未来は最初からマルチモーダルであり、テキストモデルにボルト付けされた事後のマルチモーダルではないという百度の賭けを表す。

### GLM-4.5/5（Zhipu AI）

Zhipu AI の GLM シリーズは、7,440 億パラメータの MoE GLM-5 で頂点を迎え、エージェント harness 向けに目的設計されている。モデルアーキテクチャはネイティブのツール使用トークンと構造化出力保証を含み、信頼性のあるエージェント構築に必要な足場コードを減らす。この「エージェントネイティブ」設計哲学は、GLM を本番パイプラインに統合するときに必要な prompt エンジニアリングと再試行が少ないことを意味する。

## C. 西側エコシステムからの主要な差異

中国ナレッジエンジニアリングランドスケープを理解することは、ツールとモデルをカタログするだけ以上を必要とする。エコシステムは、最初からアーキテクチャ判断を形作る根本的に異なる制約とインセンティブの下で動く。

### ツール選好：ビジュアルファースト vs. コードファースト

最も人気のある中国プラットフォーム ——Dify、Coze Studio、FastGPT —— はビジュアルファーストだ。ユーザーはキャンバス上でノードをドラッグして知識パイプラインを構築する。対照的に、西側エコシステムの支配的フレームワーク（LangChain、LlamaIndex、Haystack）はコードファーストで、ビジュアルツールは二次的アドオンだ。この発散は異なるユーザー層を反映する：中国の AI 採用はエンタープライズ IT 部門と Python を書かないかもしれない「市民開発者」によって重く駆動される、一方で西側の早期採用者はコードに馴染んだソフトウェアエンジニアである傾向がある。

### デプロイメント：オンプレミス vs. API ファースト

オンプレミスデプロイメントは中国で支配的だ。これは 2 つの強化し合う要因によって駆動される：データ主権の規制要件（特に金融、医療、政府で）と、大規模クラウド GPU アクセスをより高価にする米国チップ輸出規制からの実用的制約。結果として中国プラットフォームは量子化、蒸留、効率に重く投資する ——無制限のクラウド計算を仮定するのではなく、利用可能なハードウェアでモデルがよく動くようにする。一方、西側プラットフォームはデフォルトで API ファーストアーキテクチャを採り、モデルが提供者のインフラで動く。

### 規制アーキテクチャ

2025 年 12 月までに、748 の AI サービスが Generative AI Management Measures の下で中国規制当局に届け出された。コンプライアンスはオプションでも願望でもない ——設計段階から技術アーキテクチャを形作る。コンテンツフィルタリング、監査ログ、ユーザーアイデンティティ検証は、ローンチ前にボルト付けされるのではなく、コア機能としてプラットフォームに組み込まれる。この規制圧力は、逆説的に、より標準化されたアーキテクチャを作った：誰もが同じコンプライアンス要件を実装しなければならないとき、コンプライアンスを簡単にするプラットフォームが勝つ。

### コミュニティと知識共有

中国の開発者コミュニティは根本的に異なるプラットフォーム上で動く。WeChat グループ（Slack や Discord ではない）はリアルタイム議論の主要チャネルだ。Zhihu はより長い技術 Q&A の Stack Overflow の役割を果たす。CSDN（China Software Developer Network）はチュートリアルとブログ投稿をホストする。GitHub はコードに使われるが、議論は他の場所で起こる。この断片化は、中国ツールのヘルプを求めて GitHub Issues や Discord を検索する西側の開発者が、しばしばまばらな英語サポートを見つけることを意味する、一方で中国語コミュニティは活気に満ちて活発である ——非中国語話者には見えないだけ。

### 制約を通じた革新

米国チップ輸出規制は予期しない革新ダイナミクスを作った。中国 AI ラボは単純に計算をスケールできず、アルゴリズム効率に不釣り合いに投資した。DeepSeek R1 の 600 万ドル未満の訓練コストは最も目立つ結果だが、パターンはエコシステム全体に及ぶ：より良い推論最適化を持つより小さなモデル、より攻撃的な量子化技法、FLOP あたり能力を最大化するよう設計されたアーキテクチャ。西側エコシステムは、利用可能な計算がより多く、スケールを通して革新する傾向がある。両アプローチがフロンティア結果を生むが、異なるパスを通じて。

### 戦略的命法としてのオープンソース

中国のオープンウェイトモデルリリースは、いまや西側を量で上回る。これは利他主義ではない ——戦略だ。オープンソース化はエコシステムロックインを構築する（開発者があなたのモデルの上に構築する）、人材を引き付ける（リサーチャーは人々が使うモデルで作業したい）、グローバルな開発者コミュニティで外交的好意を作る。Alibaba の Qwen の Apache 2.0 ライセンス、DeepSeek の MIT ライセンス、ByteDance の Coze Studio のオープンソース化はすべてこのパターンに従う。結果として、世界のどこの単独開発者も、モデルからフレームワークからデプロイメントツーリングまで、完全に中国オープンソースインフラ上で本番ナレッジシステムを構築できるようになった。

## D. Bilibili コンテンツについての注

Bilibili（B 站）は大量の AI チュートリアルをホストするが、実践者は多くが英語 YouTube コンテンツの再アップロードや翻訳であることを認識すべきだ。Bilibili の AI コンテンツの元の価値は、中国固有のツールチュートリアルにある：ステップバイステップの Dify デプロイメントガイド、Qwen 統合ウォークスルー、英語に存在しないエンタープライズデプロイメントケーススタディ。Bilibili でリサーチするときは、常にコンテンツを元のソースまで遡れ。チュートリアルが英語ナレーションの中国語吹き替えで LangChain を実演しているなら、元の YouTube 版がより最新である可能性が高い。

## Sources

- Dify GitHub Repository: [https://github.com/langgenius/dify](https://github.com/langgenius/dify)
- RAGFlow GitHub Repository: [https://github.com/infiniflow/ragflow](https://github.com/infiniflow/ragflow)
- FastGPT GitHub Repository: [https://github.com/labring/FastGPT](https://github.com/labring/FastGPT)
- MaxKB GitHub Repository: [https://github.com/1Panel-dev/MaxKB](https://github.com/1Panel-dev/MaxKB)
- Coze Studio GitHub Repository: [https://github.com/coze-dev/coze-studio](https://github.com/coze-dev/coze-studio)
- DB-GPT GitHub Repository: [https://github.com/eosphoros-ai/DB-GPT](https://github.com/eosphoros-ai/DB-GPT)
- Qwen3 Technical Report and model cards, Alibaba Cloud (2025) — 典拠的エントリポイント：[https://huggingface.co/Qwen](https://huggingface.co/Qwen) と Qwen チームの Hugging Face 記事。Apache 2.0 ライセンスの詳細はリポジトリ LICENSE ファイルで確認。
- DeepSeek R1 Paper: "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning" (January 2025). [https://github.com/deepseek-ai/DeepSeek-R1](https://github.com/deepseek-ai/DeepSeek-R1) はモデルをホストし、技術レポート PDF にリンクする。
- Moonshot AI. Kimi K2.5 Agent Swarm カバレッジは Moonshot のブログとテックプレス全体で 2026 年初頭に流通した；ここで引用される 100 サブエージェント / 約 1500 ツール呼び出し数値は二次テックプレス要約から報じられる。一次アクセスは [https://platform.moonshot.ai](https://platform.moonshot.ai) 経由。
- Baidu. ERNIE 5.0 ローンチ（2026 年 1 月）；2.4T パラメータ / ネイティブ完全モダリティ主張は百度公式チャネルと中国テックプレスを通して流通した。ここでは単一の一次 URL は引用しない；モダリティとパラメータ数値は広く報告されているが二次として扱う。
- Zhipu AI. Hugging Face の GLM-4/5 モデルカードと公式 ZhipuAI ブログ；「744B MoE GLM-5」+ エージェントネイティブツールトークンはモデルカードとブログカバレッジ全体で報告される。一次エントリポイント：[https://www.zhipuai.cn](https://www.zhipuai.cn)。
- Cyberspace Administration of China, "Generative AI Service Filing" 開示（2025 年 12 月） — 748 サービス数値は中国テックプレスで広く再生産される；下層レジストリは CAC 公式サイト経由でバッチで公開される。
- "Open Source AI in China" 市場コメント — R1 後の中国エンタープライズオープンソース採用 23% から 67% へのシフトは 2025–2026 年を通じて複数の二次媒体で報告される；広く引用されるが単一の一次調査はピン留めされていないものとして扱う。
- DeepSeek. "DeepSeek mHC: Manifold-Constrained Hyper-Connections" (April 2026). [https://deepseek.ai/blog/deepseek-mhc-manifold-constrained-hyper-connections](https://deepseek.ai/blog/deepseek-mhc-manifold-constrained-hyper-connections) — 独立な再現を待つものとしてフラグ。
- DeepSeek. V4 model release on Hugging Face (April 24, 2026). MIT license; V4-Pro 1.6T (49B active) / V4-Flash 284B (13B active); 1M トークンデフォルト context。
- Fortune. "DeepSeek unveils V4 model, with rock-bottom prices and close integration with Huawei's chips" (April 24, 2026). [https://fortune.com/2026/04/24/deepseek-v4-ai-model-price-performance-china-open-source/](https://fortune.com/2026/04/24/deepseek-v4-ai-model-price-performance-china-open-source/)
- South China Morning Post. "DeepSeek unveils next-gen AI model as Huawei vows 'full support' with new chips" (April 24, 2026). [https://www.scmp.com/tech/big-tech/article/3351239/deepseek-releases-next-gen-ai-model-world-leading-efficiency](https://www.scmp.com/tech/big-tech/article/3351239/deepseek-releases-next-gen-ai-model-world-leading-efficiency)
- Phemex News. "DeepSeek V4 Matches NVIDIA on Huawei Ascend, Dispels Rumors" (April 2026). [https://phemex.com/news/article/deepseek-v4-matches-nvidia-performance-on-huawei-ascend-dispels-delay-rumors-75616](https://phemex.com/news/article/deepseek-v4-matches-nvidia-performance-on-huawei-ascend-dispels-delay-rumors-75616) — 推論パリティ主張、Ascend 950PR で NVIDIA H20 比 ~2.8 倍計算スループット。

---

*次の章: [第 10 章 — 実世界のナレッジ Harness を作る](10-case-study.md)*
