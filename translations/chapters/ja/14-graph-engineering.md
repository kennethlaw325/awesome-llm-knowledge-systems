# 第 14 章：Graph Engineering —— エージェントの組織を配線する

> **一文で：** Graph engineering とは、loop engineering の上のもう一つの層は graph である——どのエージェントが存在し、誰が誰に委任してよく、それぞれのループが互いをどう監督し訂正し合うかを明示的に配線すること——という 2026 年 7 月の主張である。
>
> **なぜ重要か：** この主張が生き残るなら、それはマルチエージェントシステムが場当たり的なループの寄せ集めであることをやめ、設計された組織になる層に名前を与えることになる；生き残らないなら、それはこうした世代のラベルがどう作られ——そして解体されるかについての、最も明快な生きたケーススタディとなる。

いまや本書の中で最も短命なアイデアはこれであり、その称号は第 13 章から引き継いだ。「graph engineering」という用語は、執筆時点でおよそ 2 週間前のものだ：2026 年 7 月 17〜18 日の後の数日間で結晶化し、完全に実践者のブログとベンダーのエッセイの中に生きており、その背後に学術文献はない。これはまた、本ガイドが扱う中で最も係争的な用語でもある。それに対する最も声高な反応——文字通りグラフにちなんで名付けられたフレームワークを持つベンダーである LangChain から——は、この実践は 3 年前からあり、新しいのはラベルだけだ、というものだ。

以下は意図的にヘッジされている。懐疑派には提唱派と同じだけの紙幅を割き、ソース間で食い違う閲覧数は食い違うものとして報告し、本章は判定ではなく明示的な生存ゲートで締めくくる。

本章は、触媒となった投稿とそれが引き起こしたエッセイの波、この新しいフレームが実際に主張していること、それへの反論、この名前が必要にしているナレッジグラフとの区別、もしこれが層であるならどこに位置するか、中国エコシステムの反響、そして実践者がいま気にすべきかどうかを扱う。

---

## 14.1 それを始めたツイート（2026年7月17〜18日）

このプレイブックは見覚えがある、なぜなら本ガイドはまさにそれが実行されるのを見たばかりだからだ。6 月 7 日の投稿が loop engineering を触媒してから（第 13.1 節）6 週間後、**Peter Steinberger**——OpenClaw の作者、現在は OpenAI に在籍——が再び投稿した。[Carlos E. Perez](https://medium.com/intuitionmachine/from-loop-engineering-to-graph-engineering-d3ebeb08511c) と [Yash Thakker](https://explainx.ai/blog/graph-engineering-ai-agents-multi-agent-organizations-2026) が逐語的に引用したところによれば、その投稿はこう書かれていた：

> 私たちはまだループの話をしているのか、それともすでにグラフへとシフトしたのか？

何よりもまず 2 つのソース上の注記が必要だ、なぜならそれを行うことこそが本章の存在理由だからだ。第一に、この投稿自体は本ガイドのために直接取得されたものではなく、独立に取得された二次ソースはそれを同一の形で伝えていない。この正確な英語の文言を引用しているのは Perez と Thakker だけだ。[LangChain](https://www.langchain.com/blog/3-years-of-graph-engineering-with-langgraph) と Perez は文章を引用せずに投稿にリンクしている；[36kr](https://eu.36kr.com/en/p/3904771418867330) と Tony Bai はそれを中国語訳で表現しており、36kr の英語版はそれを「Are we still talking about loops, or have we moved on to graphs?」と逆翻訳している；そして [Eigent](https://www.eigent.ai/blog/graph-engineering-ai-agents) はそれを言い換えている。この 2 つの逐語的な引用こそが、上記の文言をそもそも印刷する根拠だ。

第二に、それを取り巻く数字は一致しない。この投稿に日付を付けているすべてのソースは 7 月 18 日としている；本章の見出しで使っている範囲の 7 月 17 日側の端は、米国時間での可能性であって、ソース間の記録された不一致ではない。閲覧数は本当に食い違っている——ただしそれらは同一時点の対立する測定というより、異なる瞬間に取られたスナップショットだ：Thakker は数時間で 575K 閲覧と報告し、36kr は 2 日以内で 2.6M（同記事によれば、6 週間前のループ時代の投稿の 8.4M 閲覧と対比して）、Tony Bai は 2 日間でおよそ 800K としている。ここではどの数字も単独で事実として述べない。

6 月の投稿と同様、Steinberger は何も名付けなかった。「graph engineering」というフレーズは彼の文章のどこにも現れない。この複合語は、prompt、context、harness、loop engineering を意識的にパターンとして踏襲する応答エッセイの中で数日のうちに結晶化した——そしてその波は速かった：

- **7 月 18 日** —— [Yash Thakker の explainx.ai ガイド](https://explainx.ai/blog/graph-engineering-ai-agents-multi-agent-organizations-2026)（7 月 26 日まで更新）が、このツイートを触媒として名指し、org graph／work graph の分割を提示する。
- **7 月 19 日** —— **Carlos E. Perez**（Intuition Machine）が、最初の実質的な理論的拡張を公開する。
- **7 月 20 日** —— エンタープライズベンダー **TrueFoundry** が、ガバナンスチェックリスト付きの[本番指向のガイド](https://www.truefoundry.com/blog/graph-engineering-enterprise-guide)を出荷する。
- **7 月 21 日** —— **eigent.ai** がそのベンダーエッセイを公開する；中国の **Tony Bai** と **36kr** がともに同日にこの言説を取り上げる（14.6）。
- **7 月 22 日** —— Sydney Runkle と Harrison Chase による **LangChain** の公式回答が、触媒から 4 日後に着地する（14.3）。

触媒、エッセイの波、ベンダーによる対抗フレーム、そして中国エコシステムの反響——すべてが 1 週間のうちに：loop engineering の命名シーケンスが、より高速で再生されたのだ。

---

## 14.2 Graph Engineering は何を主張しているか

これらのエッセイを削ぎ落とすと、3 つの主張が繰り返し現れる。

**エージェントの振る舞いではなく、エージェントの組織。** Thakker のフレーミングは、この進行の中で最も引用しやすいバージョンだ：

> ループはエージェントの振る舞いをプログラム可能にした。グラフはエージェントの組織をプログラム可能にする。

彼のガイドは、グラフを 2 つの明確に異なるオブジェクトに分割する：

- **org graph** —— どのエージェントが存在し、それぞれが何のためにあり、どの委任のエッジが許可されているかについての安定したチャート；
- **work graph** —— 特定のジョブが生み出し、実行し、破棄する、儚いタスク分解。

その主張は、この両方がいまや、第 4 章が harness を、第 13 章が loop を扱うのと同じように、設計され、バージョン管理され、レビューされるべきエンジニアリング成果物だというものだ。

**互いを監督し合うループを、アンカーがつなぎ止める。** [Perez のエッセイ](https://medium.com/intuitionmachine/from-loop-engineering-to-graph-engineering-d3ebeb08511c)——最初の理論的拡張、7 月 19 日——は、グラフを互いを監督し制約し合うループのネットワークとして記述する。彼の独自の追加が **anchor（アンカー）** だ：グラフのいずれかのノードが必ず触れなければならない、議論の余地のない、外部に接地された測定（テスト結果、メトリクス、グラウンドトゥルースのチェック）。アンカーがなければ、互いをレビューし合うエージェントのグラフは、正しさではなく自信に満ちた合意へと収束するエコーチェンバーへと退化する、と彼は論じる——これは、第 13.4 節が単一のループについて文書化した自己採点の失敗の、マルチエージェント版である。

**統治されたトポロジー。** ベンダーのエッセイ——[TrueFoundry](https://www.truefoundry.com/blog/graph-engineering-enterprise-guide)（7 月 20 日）と [Eigent](https://www.eigent.ai/blog/graph-engineering-ai-agents)（7 月 21 日、Steinberger の投稿と Perez のネットワーク・オブ・ループの拡張の両方をクレジットしている）——は同じ運用上の読み方に収束する：graph engineering とは、エージェントのトポロジーのガバナンスと可観測性である。この読み方において、それが所有する問いは：

- エージェント間のどの遷移が許可され、どれが構造的に不可能か；
- 障害が組織全体にカスケードする前に、どこで隔離されるか；
- work graph の暴走したブランチがどう検知され、切断されるか；
- エージェント組織の監査とは、そもそもどのようなものか。

TrueFoundry はこれらのためのエンタープライズチェックリストを出荷している；そのチェックリストが存在するために新しい規律の名前を必要としたかどうかは、まさに次のセクションが取り上げる問いである。

**ベンダーは名前ではなく構造を出荷する。** 2026 年 8 月 7 日（Claude Code v2.1.224、8 月 23 日までに v2.1.241 へと反復）、Anthropic は session を横断するエージェントのメッセージングを出荷した：`ListAgents` は名前のついた session ——サブエージェント、agent-team のチームメイト、他のローカル session、クラウド session、他のマシン上の Remote Control session——を発見し、`SendMessage` はそれらの間で名前によってプレーンテキストを配送する。これは session ごとの受信ガバナンス（accept／hold／refuse）、permission-mode に基づくデフォルト、そしてサイズ／バースト／ループのスロットリングによってゲートされている。スコープは意図的に狭い：会話履歴やファイルは session を横断せず、session を横断した権限承認もなく、この機能は Bedrock、AWS 上の Claude Platform、Google Cloud Agent Platform、Microsoft Foundry では利用できない。上で定義したばかりの org graph——名前のついたエージェントの安定した名簿に許可された委任のエッジを加えたもの——に照らして読むと、これはその出荷済みインスタンスのように見える：名前がつけられ、アドレス指定可能な session に、それらの間の統治されたメッセージのエッジを加えたものだ。そうではないのは、語彙の採用だ：Anthropic 自身のドキュメントと changelog は、この機能を記述するのに「graph engineering」というフレーズをどこにも使っていない。このギャップ——大手 harness ベンダーが、本章が追跡しているパターンを運用化しながら、そのために作られたラベルについては沈黙を保っている——は、この用語ではなく、このプリミティブについての証拠であり、両者は同じ主張ではない。

---

## 14.3 反論

懐疑派には、儀礼的な一段落ではなく、ここで対等な重みを与える価値がある、なぜなら 4 日以内に、この言説はそれを行う最も強い立場にある当事者から、自分自身への最も強い反論を生み出したからだ。

**LangChain：これは 3 年前からある。** [*3 Years of Graph Engineering with LangGraph*](https://www.langchain.com/blog/3-years-of-graph-engineering-with-langgraph)（Sydney Runkle と Harrison Chase、2026 年 7 月 22 日）は、同時に 2 つのことを行っている。それはこの用語を正当化する——この投稿は明示的に、graph engineering を「prompt engineering、context engineering、harness engineering、そして loop engineering」の後に位置づけており、これはまさに本ガイドが追跡している世代の背骨を、もう 1 段拡張したものだ。そして同じ息で、この用語の勢いを削ぐ：

> エージェント的システムをグラフとして表現することは新しくない、私たちは 3 年間それをやってきた。

彼らの還元はクリーンだ：**ループとは単に有向で巡回するグラフに過ぎない。** LangGraph は 2023 年以来、エージェントをグラフのトポロジー——ノード、エッジ、条件付き遷移、サイクル——としてモデル化してきた。この読み方では、2026 年 7 月に語彙以外何もシフトしていない：この実践はラベルより 3 年先行しており、ラベルが加えるのは能力ではなく名前だ。

これが証拠基盤に対して何をするか、注意しておく価値がある。graph engineering が持つ最も強い採用シグナル——大手フレームワークベンダーが 4 日以内に反応したこと——は、同時にその最も強い懐疑的ソースでもある。同じ文書が両方であり、正直な記述はそれを両方として運ばなければならない。

**Tony Bai：今日のフレームは、明日の廃棄の山。** 中国の開発者インフラ系ライターによる[7 月 21 日の投稿](https://tonybai.com/2026/07/21/from-loop-engineering-to-graph-engineering/)は、loops-supervising-loops と anchor というフレーミングを共感的に説明した後、こう転じる：loop engineering がホットだったのはわずか 2 か月に過ぎず、そこでシリコンバレーが次の用語を生み出した、そして「graph」自体も明日には廃棄されたバズワードになっているかもしれない、と。ループのフレームの早期からの、慎重な解説者から出てくるものだからこそ——彼の懐疑は反射的なアンチ・ハイプではない——その警告はより重く響く。

**証拠の不在が語ること。** 2 週間が経った時点で、この用語を使ったカンファレンストーク、コース、求人票は 1 つもない；本ガイドのためにそれらを探したが見つからなかった。これは 2 週間に満たない用語と整合的であり、そして長続きしない用語とも整合的である。正直な言明は、証拠がまだこの 2 つを区別できないということだ。

---

## 14.4 ナレッジグラフではない

この名前は、本ガイドが構造的に解消する義務を負う衝突を運んでくる、なぜなら第 2 章は本ガイドが始まって以来グラフを扱ってきたからだ。「knowledge graph engineering」は確立された、10 年以上前からの規律である——semantic web、オントロジー、トリプルストア——そして GraphRAG（第 2 章）は、システムが自分の知っていることを検索し推論できるように、エンティティと関係のグラフを構築する。2026 年 7 月の意味での graph engineering は、この言葉以外、これと何も共有しない。TrueFoundry の区別が入手可能な中で最も明快であり、境界線として引用する価値がある：

> ナレッジグラフはシステムが何を知っているかを構造化する；2026 年の意味での graph engineering は、システムが誰であるか——そのメンバー、権限、メッセージの経路——を構造化する。

並べてみると、この 2 つのグラフはデータ構造以外に共通点がない：

| | ナレッジグラフ／GraphRAG（第 2 章） | Graph engineering（本章） |
|---|---|---|
| ノード | エンティティ | エージェント |
| エッジ | ラベル付きの関係 | 許可された委任 |
| 構築される時点 | インデックス作成時 | アーキテクチャ設計時 |
| 使われる時点 | 検索時 | 実行時（走査され、変更される） |
| 答える問い | システムは何を知っているか？ | システムとは誰か？ |

第 2 章の GraphRAG セクションから本章にたどり着いた読者は、この共有された単語を、共有された系譜としてではなく、語彙上の偶然として扱うべきだ。（第 2 章は逆方向のポインタを持っている。）

---

## 14.5 どこに位置するか——第五世代か、第四世代のリファクタか？

もしこのフレームが生き残るなら、本ガイドの進化の物語の中でどこに位置づけられるのか？ 本ガイドの背骨は、prompt（第 1 章）から context（第 1〜3 章）、harness（第 4 章）、loop（第 13 章）へと走っている。提唱者たちの答えは：もう 1 階層、というものだ。LangChain 自身のリスト——prompt、context、harness、loop の後に graph engineering を置く——は、その新規性に異議を唱えつつも、それを第五段として位置づけている。

この期間で最も有用な構造的扱いは、同時に最も新しいものでもある。[MarkTechPost の 7 月 29 日の記事](https://www.marktechpost.com/2026/07/29/prompt-engineering-vs-loop-engineering-vs-graph-engineering-what-changes-at-each-layer/)は、これらの層は継承者ではなく、積み重なった制御の単位だと論じる：

- **harness**（第 4 章）は 1 つのエージェントを取り巻く環境である；
- **loop**（第 13 章）は 1 つのエージェントの振る舞いのサイクルである；
- **graph** は、安定した組織のグラフと儚い work graph を通じて、複数のエージェントを協調させる。

その通底線——「グラフはループから作られ、ループは prompt から作られる」——は、第 1 章の共存テーゼをもう 1 つの箱で拡張したものであり、本ガイドがすでに以前の層をどう扱っているかと最も整合的な読み方である。

しかし、勢いを削ぐ読み方も同じ事実に適合する。もしループが単に有向巡回グラフに過ぎない（LangChain）なら、ループのグラフはより大きなループシステムに過ぎず、「graph engineering」は 1 つではなく N 個のエージェントに適用された harness-plus-loop engineering である——第五層ではなく、第四層のリファクタだ。第 13 章は、loop engineering が本物の層なのか、それとも「スケジューラを取り付けた harness engineering」なのかを未解決のまま残した；graph engineering はその未解決の問いを受け継ぎ、自分自身の問いを付け加える。本ガイドはそれを解決しない。このフレームは 2 週間前のものだ；それを解決することは、記述することではなく、認定することになってしまう。

---

## 14.6 中国エコシステムの反響

あるフレームがその発祥のバブルを脱したことを示すより強いシグナルの 1 つは、中国の開発者エコシステムがそれをどれだけ速く取り上げるかであり、ここでの反響は 3 日以内に、すでに定まった訳語——**图工程**——を伴ってやってきた。

検証されたアンカーは 2 つある。[Tony Bai の 7 月 21 日の投稿](https://tonybai.com/2026/07/21/from-loop-engineering-to-graph-engineering/)——タイトル：「Loop Engineering才火两个月，硅谷已经卷出"Graph Engineering"了」——は実質的な解説記事であり、中国のインフラ系読者向けに Perez の loops-supervising-loops と anchor を扱い、14.3 節のバズワード警告を付している。そして [36kr の英語版の報道](https://eu.36kr.com/en/p/3904771418867330)（同じく 7 月 21 日）は、この言説をニュースとして扱う：14.1 節の閲覧数比較を報じ、Geoffrey Huntley、Boris Cherny、Addy Osmani、Luis Catacora をこの言説の参加者として名指す。（これらの帰属は 36kr のみに依拠しており、ここでもそのようなものとしてのみ引用する。）

この 2 つを超えると、反響はタイトルのみへと薄まっていく。中国語での検索は、CSDN 智能体开发者社区 の 2 本の記事——1 つは控えめに「从Loop Engineering到Graph Engineering」と題され、もう 1 つは「Loop工程已死，Graph工程永生」（「Loop engineering は死んだ、graph engineering は永遠に生きる」——第 13.8 節がループの波について文書化したのと同じ 已死 のフック）というハイプのテンプレートを全開にしたもの——、そして繁体字中国語の解説記事を浮上させた。この 3 本のいずれも本ガイドのために独立に取得されたものではない；検索結果のタイトルとして、中国語コンテンツパイプラインがこの用語に関与している証拠として引用しているに過ぎず、それ以上のものではない。

このパターンは第 13 章から見覚えがある：loop-engineering の解説記事を産業化したパイプラインが、いま 图工程 を処理している——触媒から触媒までの遅れはおよそ 6 週間だが、触媒から反響までは数日に過ぎない。

---

## 14.7 いま気にすべきか？

2026 年 7 月下旬にこれを読んでいる実践者は、2 つの別々の答えを必要とする、なぜならラベルと問題は切り離せるからだ。

**問題は、ラベルとは関係なく本物だ。** もしあなたが 1 つの harness の中で、1 つのループを使って 1 つのエージェントを走らせているなら、本章の何もあなたの仕事を変えない；第 4 章と第 13 章がいまも実務上の層だ。もしあなたがすでに複数のエージェントを配線してつなげているなら、これらのエッセイが名指す懸念——どの委任のエッジが許可されているか、障害がカスケードする前にどこで隔離されるか、何が観測され監査されるか、システムが自己合意へと漂流しないようにどのノードが anchor に触れるか——は、「graph engineering」がその名前として生き残ろうと生き残るまいと、あなたが抱えているエンジニアリング上の問いである。TrueFoundry のチェックリストと Perez の anchor は、どんな語彙のもとであっても、いま使えるものだ。LangChain の反論は、この一点に関しては合意でもある：彼らは 3 年間これらのグラフをエンジニアリングしてきており、それはこれらの問題が少なくとも 3 年前からあることを意味する。

**このラベルは、あなたが張る必要のない賭けだ。** 本ガイドが第 13 章を追加したのは、loop engineering が 5 週間前のものだったときだ；graph engineering は 2 週間で 1 章を得ており、それは厳密により強い初期の証拠（より速いエッセイの波、同じ週のフレームワークベンダーの反応、より速い中国語の反響）と、厳密により弱い成熟度（Stripe の minions に匹敵する本番ケーススタディなし、ベンダーのカリキュラムなし、ベンチマークなし）の上に成り立っている。だから本章は主張ではなくゲートで締めくくる。**生存テストは、この用語が 2026 年 9 月にもまだ流通しているかどうかだ。** 具体的には、以下を注視せよ：

- フレームワークやベンダーのドキュメントが、単なるブログのフレーミングとしてではなく、プロダクトの語彙としてこの用語を採用すること；
- カンファレンストーク、コース、求人票がそれを使うこと（執筆時点：見つからず）；
- Stripe の minions が loop engineering に与えたのと同じ重みを持つ、名前のついた本番ケーススタディ；
- 1 つの投稿への返答として書かれたものではない、第二のエッセイの波。

それらが到来すれば、本章は第 13 章がそうしたように成長する。到来しなければ、本章は 2 週間の命名イベントの記録として立ち、勢いを削ぐ読み方が勝つ。

本ガイドは graph engineering を、定まった層としてではなく、検証中の主張として追跡する——そして、今日のフレームは明日の廃棄されたバズワードになるかもしれないという Tony Bai の警告こそが、この賭け金の最も公正な一文要約である。

---

## Sources

- Steinberger, Peter. X の投稿、「Are we still talking loops or did we shift to graphs yet?」（2026 年 7 月 18 日、それに日付を付けている以下のすべてのソースによれば）—— 本ガイドのために直接取得されたものではなく、以下のソースを通じてのみ引用：Perez と Thakker（explainx）が逐語的に引用、LangChain と Perez は引用せずリンク、36kr と Tony Bai は中国語訳で表現、Eigent は言い換え。報告されている閲覧数はソース間で食い違う。
- Runkle, Sydney と Harrison Chase（LangChain）. "3 Years of Graph Engineering with LangGraph"（2026 年 7 月 22 日）：[https://www.langchain.com/blog/3-years-of-graph-engineering-with-langgraph](https://www.langchain.com/blog/3-years-of-graph-engineering-with-langgraph) —— graph engineering を prompt／context／harness／loop の後に位置づける；「ループは単に有向巡回グラフに過ぎない」；3 年前からの実践だという反論。
- Perez, Carlos E.（Intuition Machine）. "From Loop Engineering to Graph Engineering?"（2026 年 7 月 19 日）：[https://medium.com/intuitionmachine/from-loop-engineering-to-graph-engineering-d3ebeb08511c](https://medium.com/intuitionmachine/from-loop-engineering-to-graph-engineering-d3ebeb08511c) —— 最初の理論的拡張；loops supervising loops；エコーチェンバーに対する議論の余地のない測定としての anchor。
- Thakker, Yash（explainx.ai）. "Graph Engineering: After Loops, This Is How You Wire Multi-Agent Orgs (2026)"（2026 年 7 月 18 日、7 月 26 日更新）：[https://explainx.ai/blog/graph-engineering-ai-agents-multi-agent-organizations-2026](https://explainx.ai/blog/graph-engineering-ai-agents-multi-agent-organizations-2026) —— org graph 対 work graph；「ループはエージェントの振る舞いをプログラム可能にした。グラフはエージェントの組織をプログラム可能にする」。
- TrueFoundry. "Graph Engineering for Multi-Agent Systems: Architecture, Governance, and Observability"（2026 年 7 月 20 日）：[https://www.truefoundry.com/blog/graph-engineering-enterprise-guide](https://www.truefoundry.com/blog/graph-engineering-enterprise-guide) —— エンタープライズチェックリスト；ナレッジグラフとの区別の引用（「システムが何を知っているか」対「システムが誰であるか」）。
- Eigent. "Graph Engineering for AI Agents"（2026 年 7 月 21 日）：[https://www.eigent.ai/blog/graph-engineering-ai-agents](https://www.eigent.ai/blog/graph-engineering-ai-agents) —— Steinberger の投稿と Perez の拡張をクレジット；互いを訂正し合うループの統治されたトポロジー。
- 36kr（英語版）. "Father of Lobster's One Tweet: Is the Loop Era Over?"（2026 年 7 月 21 日）：[https://eu.36kr.com/en/p/3904771418867330](https://eu.36kr.com/en/p/3904771418867330) —— このツイートを 2.6M 閲覧、ループ時代の投稿を 8.4M 閲覧として報告；言説の追加の参加者を名指す；この用語を新興のものとして扱う。
- Bai, Tony. 「Loop Engineering才火两个月，硅谷已经卷出"Graph Engineering"了」（2026 年 7 月 21 日）：[https://tonybai.com/2026/07/21/from-loop-engineering-to-graph-engineering/](https://tonybai.com/2026/07/21/from-loop-engineering-to-graph-engineering/) —— 中国エコシステム向けの 图工程 解説記事；「graph」自体も廃棄されたバズワードになるかもしれないと警告。
- MarkTechPost. "Prompt Engineering vs Loop Engineering vs Graph Engineering: What Changes at Each Layer"（2026 年 7 月 29 日）：[https://www.marktechpost.com/2026/07/29/prompt-engineering-vs-loop-engineering-vs-graph-engineering-what-changes-at-each-layer/](https://www.marktechpost.com/2026/07/29/prompt-engineering-vs-loop-engineering-vs-graph-engineering-what-changes-at-each-layer/) —— 積み重なった制御の単位としての読み方；org graph ＋ work graph；「グラフはループから作られ、ループは prompt から作られる」。
- Claude Code（Anthropic）. Session を横断するメッセージングのドキュメントと changelog（2026 年 8 月 7 日、v2.1.224；2026 年 8 月 23 日までに v2.1.241 へと反復）：[https://code.claude.com/docs/en/cross-session-messaging](https://code.claude.com/docs/en/cross-session-messaging) ；[https://code.claude.com/docs/en/changelog](https://code.claude.com/docs/en/changelog) —— ListAgents／SendMessage が、名前のついたエージェントの発見と、session を横断する統治されたメッセージのエッジを出荷する；「graph engineering」というフレーズはどちらのページにもどこにも現れない。

---

*前の章: [第 13 章 — Loop Engineering：エージェントにプロンプトを送るシステムを設計する](13-loop-engineering.md)*
