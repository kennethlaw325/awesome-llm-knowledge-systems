# 13장: Loop Engineering —— 에이전트에게 prompt하는 시스템을 설계하기

> **한 문장으로:** Loop engineering이란 에이전트에게 prompt하는 시스템을 직접 만드는 실천이다 —— 매 턴을 손으로 운전하는 것을 멈추고, 스스로 실행하고, 점검하고, 자신을 먹여 살리는 루프를 설계하기 시작하는 것.
>
> **왜 중요한가:** 이는 본 가이드의 진화 서사에서 가장 새롭고 가장 정착되지 않은 계층이며, 자율 에이전트 작업이 앞으로 1년 동안 실제로 어떻게 스케줄되고, 검증되고, 리뷰되는지를 형성할 가능성이 가장 큰 계층이다.

이것은 본 가이드에서 가장 수명이 짧은 아이디어다. (그 타이틀은 6주만 유지되었다: 2026년 7월 말, 같은 playbook이 루프 위의 다음 계층 —— graph engineering ——을 주장했고, 이는 [14장](14-graph-engineering.md)에서 다룬다.) "loop engineering"이라는 용어는 이 글을 쓰는 시점에 약 5주 되었다: 2026년 6월 초에 명명되어, 며칠 안에 실무자 블로그, 팟캐스트, X를 통해 퍼졌으며, 아직 그 뒤에 학술 문헌이 없다. 이어지는 내용은 의도적으로 조심스럽게 다뤄진다. 주장이 세 가지 다른 방식으로 받아 적힌 팟캐스트 인용에 기대거나, 아무것도 명명하지 않은 바이럴 포스트에 기댈 때는, 본 장이 그렇다고 밝힌다. 목표는 떠오르는 프레임을 정확히 기술하는 것이지, 정착된 세대로 인증하는 것이 아니다.

이 프레임은 서술할 가치가 있다. 실무자 담론에서 실제로 일을 하고 있기 때문이다: 4장의 harness engineering이 암시했지만 분리해내지는 못한 전환 —— *에이전트에게 prompt하기*에서 *에이전트에게 prompt하는 시스템을 설계하기*로의 이동 —— 에 이름을 준다. 그것이 자기만의 계층을 가질 자격이 있는지, 아니면 그냥 스케줄러가 붙은 harness engineering일 뿐인지가 바로 본 장이 열어 둔 질문이다.

본 장은 이 용어가 어디서 왔는지, 그 지지자들이 이를 harness와 어떻게 관계 짓는지, 루프가 무엇으로 이루어지는지, 루프를 정직하게 유지하는 generator-evaluator 분할, 하나의 대규모 프로덕션 사례, 스택된-루프 프레이밍, 인간이 지키라고 요구받는 판단, 그리고 채택의 초기 신호를 다룬다 —— 논쟁적인 부분들은 곳곳에서 명시적으로 표시된다.

---

## 13.1 이름을 얻은 주 (2026년 6월)

촉매는 단일 포스트였다. 2026년 6월 7일, **OpenClaw**의 창시자인 **Peter Steinberger** (@steipete) —— Y Combinator는 이를 "5개월도 채 안 되어 주말 프로젝트에서 GitHub에서 별을 가장 많이 받은 소프트웨어 저장소로" 성장해, React를 앞질러 346k개 이상의 별을 받았다고 묘사했다 —— 이며 현재는 OpenAI에 있는 그는 다음과 같이 썼다:

> 코딩 에이전트에게 더 이상 prompt하면 안 된다는 매달의 리마인더입니다.
>
> 여러분은 에이전트에게 prompt하는 루프를 설계해야 합니다.

이 포스트는 **2026년 7월 중순 기준 8.4M+ 노출**을 끌어냈다. 이는 아무것도 명명하지 않았다: Steinberger는 "loop engineering"이라는 문구를 사용하지 않았고, 그 단어들은 그의 텍스트 어디에도 나타나지 않는다. 명명은 그가 촉발한 발상에 응답한 다른 사람들에게서 왔다.

같은 날, **Addy Osmani** (Google)가 이 실천에 이름을 준 에세이를 발표했다 (*Loop Engineering*, addyosmani.com/blog/loop-engineering/, 6월 7일; O'Reilly Radar에 신디케이트, 6월 22일). 그의 정의는 나머지 담론이 인용하는 바로 그것이다:

> Loop engineering은 당신 자신을 에이전트에게 prompt하는 사람의 자리에서 교체하는 것이다. 당신은 그것을 대신하는 시스템을 설계한다.

같은 전환이 프런티어 연구실 내부에서도 나타난다. Anthropic의 Claude Code 창시자이자 책임자인 **Boris Cherny**는 2026년 중반 팟캐스트에서 자신의 워크플로우를 같은 방식으로 프레이밍했다. 가장 많이 인용되는 Lenny's Podcast 인터뷰 받아쓰기에 따르면:

> 저는 더 이상 Claude에게 prompt하지 않습니다. 저는 Claude에게 prompt하고 무엇을 할지 알아내는 루프들을 실행하고 있습니다. 제 일은 루프를 짜는 것입니다.

이 인용은 유보 조건이 필요하며, 그것이 바로 본 장이 존재하는 이유가 되는 종류의 유보 조건이다. 이는 *구어체* 발언이며, 여러 매체에서 일관되지 않게 받아 적혔고 (일부는 Lenny's가 아니라 Acquired 팟캐스트를 인용한다), 정본이 되는 verbatim 텍스트나 전체 트랜스크립트는 이용 가능하지 않다. 그 실체 —— Cherny는 더 이상 손으로 prompt하지 않고, Claude에게 prompt하고 다음 행동을 결정하는 루프를 짠다는 것 —— 은 여러 2차 출처에 걸쳐 확증되지만, 정확한 단어는 고정되어 있지 않다.

종합하면, 6월 7일 주는 촉매 (Steinberger), 이름과 정의 (Osmani), 그리고 내부자의 메아리 (Cherny)를 만들었다. 그것이 만들지 못한 것은 합의다. 이 용어는 몇 주 안에 실무자 담론에서 결정화되었지만, 수용은 이를 진정한 전환이라고 부르는 독자와 시기상조라고 —— 스케줄링의 리브랜딩, 즉 "cron이 붙은 harness"라고 —— 부르는 독자로 갈린다. 어떤 동료 심사 논문도 이 용어를 쓰지 않는다. 본 가이드는 loop engineering을 떠오르고 논쟁적인 프레임으로 다루며 (1장의 네 번째 세대 절 참조), 그 때문에 아래의 하중을 견디는 모든 주장은 1차 출처에 묶여 있고, 빈틈은 채워지기보다 명명된다.

---

## 13.2 Harness 바로 한 층 위

그 지지자들이 만드는 가장 깔끔한 정의적 움직임은 루프를 4장의 harness 바로 위에 놓는 것이다. Osmani는 그 관계를 노골적으로 말한다:

> Loop engineering은 harness 바로 한 층 위에 있다.

루프가 *무엇인지*에 대한 그의 심상 모델은 harness를 구성 요소로 유지한다: 루프란 "타이머로 돌고, 작은 helper들을 낳고, 스스로를 먹여 살리는" harness다. 그는 이것이 앞선 작업을 대체하는 것이 아니라 확장하는 것이라고 명시한다 —— 그는 "이것의 사촌, 즉 하나의 에이전트가 그 안에서 실행되는 환경을 만드는 agent harness engineering에 대해 전에 썼다"고 말한다.

중국 개발자 **程序员鱼皮** (liyupi)는 이 관계의 가장 구조적인 버전을 제시한다. 6월 16일 그의 가이드 (codefather.cn)에서, 그는 prompt 기법, context 관리, harness 구축, 루프를 **層層包含** —— 층층이 포함되는 관계 ——로 배치한다:

> 这四者是层层包含的关系。提示词技巧、上下文管理、Harness 搭建，这些能力在 Loop 里面全都要用上。

(이 넷은 층층이 포함되는 관계다; prompt 기법, context 관리, harness 구축은 모두 Loop *안에서* 사용되어야 한다.) 이는 1장이 prompt → context → harness에 적용하는 것과 같은 중첩-계층 논리이며, 바깥쪽으로 상자 하나가 확장된 것이다. 귀속에 관해 정확할 필요가 있다: 鱼皮는 중국 개발자 독자를 위해 기존 용어를 재포장하고 구조화하는 것이지, 용어를 만들어낸 것이 아니다 —— "harness engineering"과 "loop engineering"은 Claude Code와 Cherny의 담론으로 거슬러 올라간다.

그의 말 비유는 그 누구보다도 harness/loop의 경계선을 날카롭게 그린다:

> 如果把 AI 比作一匹马，Harness 就是你给马装上的缰绳、马鞍和围栏，然后你骑在马上手动驾驭它。

(AI를 말에 비유한다면, harness는 당신이 말에게 채운 고삐, 안장, 울타리다 —— 그런 다음 당신은 말에 올라타 손수 조종한다.)

> 而 Loop 呢，是你设定好一条巡逻路线后，不用上马，让马自己按路线一圈一圈地跑。

(Loop이란 당신이 순찰 경로를 정한 다음, *올라타지 않고*, 말이 스스로 그 경로를 한 바퀴 한 바퀴 달리게 두는 것이다.)

그 비유는 loop engineering을 "에이전트를 위한 cron"으로 무너지지 않게 지키는 단 하나의 구분을 인코딩한다: **루프는 스케줄러가 아니다.** 스케줄러는 시각에 맞춰 발화한다. 루프는 시각에 맞춰 발화*하고 나서* 이번 회차에 무엇을 할지 결정하기 위해 현재 상태를 읽는다. CI 상태, 열린 이슈, 지난 실행의 남은 것을 살핀 다음 행동을 선택하는 부분 —— 런타임 결정자 ——은 정확히 cron 항목이 갖지 못한 것이다. 루프는 스케줄러에 매 통과마다 다시 결정하는 상태-읽기 에이전트를 더한 것이다. (교차 참조: 1장, "핵심 통찰: 대체가 아니라 공존.")

---

## 13.3 루프는 무엇으로 이루어지는가

Osmani의 에세이는 가장 구체적인 목록을 제공한다. 그의 절은 **"다섯 조각, 그리고 노트"**라는 제목을 갖는다 —— 그리고 그 개수가 중요한 것은, 부풀리기 쉽기 때문이다. *다섯 조각과 외부 상태*이지, 여섯 개의 동등한 building block이 아니다:

- **오토메이션** —— 루프를 발화시키는 트리거 (스케줄, 이벤트).
- **워크트리** —— 병렬 에이전트가 충돌하지 않도록 하는 격리된 작업 사본.
- **스킬** —— 5장의 재사용 가능한 능력 묶음.
- **커넥터 (MCP)** —— 7장의 도구와 데이터 접근 범위.
- **서브에이전트** —— 하나의 실행이 낳는 작은 helper들.

"그리고 노트"는 **외부 상태 / 메모리**다 —— 실행 사이에 진행 상황을 지속시키는 markdown 파일이나 Linear 보드. 이것은 여섯 번째 동등한 block이 아니다; 이는 다섯 조각이 쓰고 읽는 기반이다.

그의 실제 사례는 아침 트리아지 루프이며, 다섯 조각 하나하나가 매핑되기 때문에 유용하다. **오토메이션**이 매일 아침 발화한다. 트리아지 **스킬**이 CI 실패, 열린 이슈, 최근 커밋을 읽는다. 격리된 **워크트리**가 수정을 작성하는 **서브에이전트** 하나와 그것을 리뷰하는 두 번째 서브에이전트를 호스팅한다. **커넥터**가 PR을 열고 티켓을 업데이트한다. 해결되지 않은 항목은 트리아지 인박스에 표면화되고, **상태 파일**이 진행 상황을 지속시켜 다음 날 아침 실행이 처음부터 다시 시작하는 대신 이어지게 한다. 상태 파일이 하중을 견디는 부분이다: 그것 없이는, 루프가 어제를 기억하지 못하고 매 실행이 차갑게 시작된다.

---

## 13.4 Generator 대 Evaluator

스스로에게 prompt하는 루프는 어려운 문제를 물려받는다: *누가 작업을 점검하는가?* 변경을 만드는 에이전트가 그것을 채점까지 한다면, 루프는 자기 축하를 향해 최적화된다. 가장 많이 인용되는 1차 다룸은 명명된 주보다 앞서며, 그 자체가 시사적이다 —— 실천이 라벨보다 앞서 달렸다는 것. **Prithvi Rajasekaran**의 *"Harness design for long-running application development"* (anthropic.com/engineering/harness-design-long-running-apps, 2026년 3월 24일)는 그 실패 모드를 직접 문서화한다: 자신의 산출물을 평가하도록 요청받으면 에이전트는 "자신의 작업을 확신에 차서 칭찬하는 것으로 반응하는 경향이 있다"고, 그리고 "자신의 작업을 채점할 때 신뢰성 있게 긍정으로 치우친다"고 한다.

그의 해결책은 적대적 훈련에서 구조를 빌린다:

> Generative Adversarial Networks (GAN)에서 영감을 받아, 저는 generator와 evaluator 에이전트를 가진 다중-에이전트 구조를 설계했습니다.

비대칭이 그 통찰의 전부이며, 그것이 여분의 에이전트를 들일 가치가 있는 이유다:

> 독립적인 evaluator를 회의적이 되도록 튜닝하는 것이, generator가 자신의 작업에 비판적이게 만드는 것보다 훨씬 다루기 쉽다는 것이 밝혀졌습니다.

결정적으로, evaluator는 diff가 아니라 *행동*을 검증한다. Rajasekaran의 설계에서 evaluator는 "실행 중인 애플리케이션을 사용자처럼 클릭해 다니기 위해 Playwright MCP를 사용해, UI 기능, API 엔드포인트, 데이터베이스 상태를 테스트했다", 그리고 "각 기준을 점수화하고 상세한 비평을 쓰기 전에 스스로 페이지를 탐색하고, 스크린샷을 찍고, 구현을 신중히 연구했다." 코드를 읽는 것은 검증이 아니다; 그것을 실행하는 것이 검증이다.

이 generator-evaluator 분할은 이제 출시된 루프-제어 primitive들에서 눈에 보이며, 그 사이에서 중요한 구분은 *루프가 언제 멈춰야 하는지를 어떻게 아는가*이다:

- **`/loop`** (Claude Code v2.1.71)는 prompt나 슬래시 명령을 반복 간격으로 재실행한다 —— 체인지로그 줄은 "prompt나 슬래시 명령을 반복 간격으로 실행하는 `/loop` 명령 추가 (예: `/loop 5m check the deploy`)"이다. 반복 작업은 생성 7일 후 만료된다; 그 작업은 마지막으로 한 번 더 발화한 다음 스스로를 삭제한다.
- **`/goal`** (Claude Code v2.1.139+)은 *조건이 성립할 때까지* 실행된다: "작은 빠른 모델이 조건이 성립하는지 확인한다" (기본값은 Haiku), 이는 "매 턴 뒤에" 조건을 확인하는 별도의 evaluator이며, 그래서 완료는 작업을 하는 모델이 아니라 신선한 모델에 의해 결정된다. 물밑에서, `/goal`은 "세션-스코프의 prompt 기반 Stop hook에 대한 wrapper"다.
- **Cloud Routines**는 "Anthropic이 관리하는 클라우드 인프라에서" 실행되며, "당신의 노트북이 닫혀 있을 때도 계속 작동한다"; 최소 간격은 1시간이며, 각 실행은 신선한 클론에서 시작한다.
- **Codex scheduled automations**는 매일 및 매주 스케줄을 지원하거나, RFC 5545 반복 규칙 (RRULE)을 통해 설정된 커스텀 주기를 지원한다.

`/loop` 대 `/goal`의 대비는 generator-evaluator 분할이 제품 설계로 표면화된 것이다. `/loop`는 *간격 재실행*이다 —— 상태와 무관하게 시계 위에서 다시 발화한다. `/goal`은 *조건-판단 종료*다 —— 두 번째의 독립적인 모델이 작업이 끝났는지를 결정한다. 하나는 반복하고, 다른 하나는 판결한다. 진지한 루프는 보통 둘 다 필요하다: 실행할 트리거와, 언제 멈출지를 아는 evaluator.

---

## 13.5 프로덕션 사례: Stripe의 Minions (2026년 3월)

프로덕션에서 실행되는 가장 큰 공개된 루프는 Stripe의 **"minions"**다. Stripe 엔지니어인 **Steve Kaliski**는 2026년 3월 (Claire Vo가 진행하는) *"How I AI"* 팟캐스트에서 이 시스템을 설명했다; Stripe 자체 개발자 블로그는 2부작 *Minions* 글에서 내부를 문서화한다. (에피소드 날짜는 2차 출처들 사이에서 엇갈리므로, 여기서는 월만 명시한다.)

핵심 숫자는 무인 산출물의 볼륨이다. Kaliski는 Stripe가 "리뷰 외에는 인간의 도움이 없는 PR을 매주 약 1,300개 착륙시키고 있다"고 말한다. Stripe의 블로그는 같은 수치를 더 보수적으로 진술한다: "Stripe에서 매주 병합되는 천 개 이상의 pull request가 완전히 minion이 생산한 것"이며, 이들은 "인간이 리뷰"하지만 "인간이 작성한 코드를 담고 있지 않다."

minion은 Slack에서 트리거된다 —— 특정 이모지 반응을 추가하거나 Slack 앱을 태그함으로써. Stripe의 말로: "Slack 앱을 태그함으로써, 엔지니어는 변경 사항을 논의하는 스레드에서 직접 minion을 시작할 수 있다."

본 가이드에 대해, 하중을 견디는 디테일은 *Stripe가 결정론적/확률론적 경계를 어디에 긋는가*이다. Context 조립은 모델이 실행되기 **전에** 일어나며, 그것은 결정론적이다: "우리는 minion 실행이 시작되기 전에도, context를 더 잘 hydrate하기 위해 그럴듯해 보이는 링크들에 대해 관련 MCP 도구를 결정론적으로 실행한다." 그다음에야 확률론적 부분이 시작된다. 핵심 에이전트 루프는 Block의 오픈소스 **Goose**의 fork다 —— "핵심 에이전트 루프는 Block의 코딩 에이전트 goose의 fork에서 실행된다 ... 우리는 이를 초기에 fork했다." 실행은 Stripe **devbox**에서 샌드박스화된다; Stripe 개발자 블로그에 따르면 (팟캐스트가 아니라), "Stripe devbox는 AWS EC2 인스턴스"이며, "pet이 아니라 cattle"로 다뤄진다 —— 맞춤화되고 장수하는 것이 아니라 표준화되고 처분 가능한 것으로.

이 프레임워크의 핵심: 신뢰성은 더 똑똑한 모델에서 오지 않는다. 그것은 *경계 배치*에서 온다 —— 확률론적 생성 이전의 결정론적 context hydration —— 그리고 인간이 쓰기 경로에서 나와 리뷰 경로로 옮겨간 것에서 온다. 모든 minion PR은 여전히 엔지니어가 리뷰한다. 루프는 작성을 스케일했다; 인간을 제거하지 않았고, 재배치했다.

---

## 13.6 루프 쌓기

**LangChain**의 *"The Art of Loop Engineering"* (Sydney Runkle, 2026년 6월 16일)은 이 계층에 내부 구조를 부여하려는 가장 명료한 시도다. 그것은 기본 사례에서 시작한다:

> 핵심 에이전트 알고리즘은 단순하다: LLM에게 context를 주고 끝날 때까지 루프 안에서 도구를 호출하게 하라.

거기서부터 네 단이 쌓인다. 페이지 자체의 제목은 "Loop"과 "Level" 라벨을 섞어 쓰며, 여기서는 쓰인 그대로 재현한다 —— **"Loop 1: The Agent," "Level 2: Verification loop," "Level 3: Event driven loop," "Level 4: Hill climbing loop."** 그 진행:

1. **Loop 1: The Agent** —— 기본 도구-호출 루프, context가 들어오고 끝날 때까지 도구가 호출된다.
2. **Level 2: Verification loop** —— 에이전트의 산출물에 대한 독립적인 점검, §13.4의 generator-evaluator 분할이 하나의 단으로 적용된 것.
3. **Level 3: Event driven loop** —— 루프가 간격이나 인간의 push뿐 아니라 실세계 이벤트에 대해 발화한다.
4. **Level 4: Hill climbing loop** —— 자기 개선 루프, 시스템이 연속된 실행에 걸쳐 나아지는 것.

정확성 노트 하나: 2차 보도는 이를 과장한다. 그 페이지는 네 번째 단을 *실행에 걸친 자기 개선*으로 프레이밍하지, 자기 harness를 다시 쓰는 시스템으로 프레이밍하지 않는다. 더 강한 주장은 원문에 없다. Runkle은 또한 **"loopcraft"**라는 용어를 빌리지만 —— "루프를 쌓는 기예"에 관한 Swyx의 글을 인용하며 Swyx에게 귀속시킨다. 그 조어는 Swyx의 것이며, LangChain이 인용한 것이지 LangChain 자신의 것이 아니다.

---

## 13.7 아우터 루프: 인간이 지키는 것

§13.1–13.6이 에이전트가 실행하는 루프를 기술한다면, Osmani의 후속작은 인간이 지키라고 지시받는 루프를 기술한다. *"Own the Outer Loop"* (addyo.substack.com/p/own-the-outer-loop)는 2026년 7월 8일 X에서 발표되었다 (Substack 사본은 7월 9일 byline을 달고 있다). 그 분할: 에이전트는 이제 **이너 루프** —— 조사, 구현, 테스트/검증, 보고 ——를 실행하고, 엔지니어는 **아우터 루프**를 쥔다. 그의 테제 문장은 단도직입적이다:

> 엔지니어는 아우터 루프를 소유한다.

아우터 루프는 위임되지 않는 판단이며, 그의 정확한 표현으로 세 기둥으로 구조화된다 —— **Quality**, **Verdict**, **Answerability**. Quality는 에이전트가 행동하기 전에 실행되는 점검들의 back-pressure다. **Verdict**는 "작업이 우리의 의존 시스템에 들어가기 전에 우리가 내리는 최종 결정"이다. **Answerability**는 "누군가 묻는다면, 나는 왜인지 설명할 수 있다는 보장"이다. (그의 용어는 단수형 *Verdict*이며, "quality bar"는 그의 표현이 아니다 —— 그 기둥은 그냥 *Quality*다.) 이것들을 인간에게 남겨두는 이유:

> 에이전트는 그것을 작성할 수 있다. 하지만 그것이 사용자에게 도달하기 전에, 누군가는 왜 그것이 존재해야 하는지, 왜 그것이 프로덕션의 일부가 될 만큼 충분히 안전한지, 그리고 그것이 틀렸을 때 무엇을 할 것인지 설명해야 한다.

그는 아우터 루프를 과잉 위임하는 세 가지 실패 모드를 명명한다: **cognitive debt** ("문제를 어떻게 푸는지에 대한 당신의 이해와 기억의 침식"), **cognitive surrender** ("AI가 주는 것을 맹목적으로 받아들이는 것"), 그리고 **orchestration tax** (당신의 판단이 실제로 감당할 수 있는 것보다 더 많은 에이전트를 띄우는 것의 부담). 이것들은 "go"를 누르면서도 엔지니어로 남지 않는 것의 비용이다.

6월 7일 에세이로 돌아가는 관통선은 그것의 마무리 지시이며, 정확히 그 위험에 대한 경고로 읽힌다:

> 루프를 지어라. 하지만 go를 누르는 사람으로서가 아니라, 계속 엔지니어로 남으려는 사람으로서 지어라.

그리고 루프가 스스로를 정당화한다는 어떤 가정도 무너뜨리는 문장:

> 두 사람이 똑같은 루프를 지어도 완전히 상반된 결과를 얻을 수 있다.

루프는 그 주위의 아우터 루프만큼만 좋다. 그것이 이 프레임 전체의 정직한 중심이다.

---

## 13.8 채택 신호

세 가지 표지가 이 프레임이 그 발원자를 넘어 퍼지고 있음을 보여준다. 각각은 검증 가능한 것에 한정되며, 그것들과 함께 돌던 과장된 주장들은 제외한다.

**벤더.** Anthropic의 공식 개발자 계정 **@ClaudeDevs**는 X Article *"Getting started with loops"*를 2026년 7월 6일 발표했다 (7월 중순 기준 약 **6.0M 노출과 38K+ 북마크**). 그 자료는 에이전틱 루프를 직접 가르친다 —— "당신이 보내는 모든 prompt는 당신이 매 턴을 지시하는 수동 루프를 시작한다. Claude는 context를 모으고, 행동을 취하고, 자신의 작업을 확인하고, 필요하면 반복하고, 응답한다" —— 그리고 턴-기반, 목표-기반 (`/goal`), 시간-기반 (`/loop`, `/schedule`) 루프를 훑는다. 남겨둘 만한 편집상의 뉘앙스가 있다: X article 자체의 제목은 *"loops,"*이지 *"loop engineering"*이 아니다. "loop engineering" 라벨은 정본 Claude 블로그 미러의 프레이밍 (claude.com/blog/getting-started-with-loops)에 나타나지, 제품 어휘 자체에는 나타나지 않는다. 벤더가 루프를 가르치는 것은 벤더가 그 용어를 채택하는 것보다 약한 신호다 —— 그리고 더 약한 쪽만 검증되었다.

**중국.** 鱼皮의 6월 16일 保姆级 ("보모 수준") 가이드는 중국 개발자 담론으로 들어가는 진입점이다. 그 제목 —— 「提示词工程已死，Loop Engineering 称王！保姆级教程 + 项目实战」 ("Prompt engineering은 죽었다, Loop Engineering이 왕이다! 보모 수준 튜토리얼 + 프로젝트 실전") ——은 已死 ("죽었다")로 시작하며, 그 훅은 본문 자체가 되돌리는 과장이다: 그 가이드 자체의 層層包含 논증 (§13.2)은 prompt 기법이 루프에 의해 죽는 것이 아니라 루프 *안에서 사용*된다는 것이다. 대략적인 도달 대리 지표로, 그의 GitHub 계정은 **23.9k명의 팔로워**를 보여준다. (더 큰 총 팔로잉 수치가 돌지만 1차 출처에 대해 검증되지 않아 여기서는 생략한다.)

**메모리와 평가.** 루프가 가장 의존하는 하위 문제 —— 실행 사이에서 살아남는 세션 간 상태 —— 는 이제 별도로 벤치마크된다. Snorkel의 **Continual Learning Bench** (arXiv 2606.05661; Snorkel AI / UC Berkeley SkyRL / UW-Madison)는 결과를 에이전트, 메모리 시스템, 작업으로 인수분해한다. 그 위에서, **Fable을 메모리 백본으로 사용한 에이전트 시스템이 Opus나 Sonnet 위에 지어진 것들을 능가**했다 (Snorkel의 Benchtalks 인터뷰; 정성적 발견 —— arXiv 논문의 모델 명부는 Opus 4.7 / Sonnet 4.6 / Gemini 3.1 Pro / Gemini 3 Flash / GPT-5.4이며, Fable에는 어떤 숫자 점수도 붙어 있지 않다). 출시 시점에, 최고 수준 시스템은 약 **25% 정규화 이득**에 도달했으며, in-context learning이 리더보드를 이끌었다. 신호는 그 숫자가 아니다; *어떤 메모리가 루프를 뒷받침하는가*가 이제 측정된 축이라는 것이다.

이름을 얻은 지 5주 만에, loop engineering은 정의, harness에 대한 명시된 관계, 하나의 대규모 프로덕션 사례, 프레임워크 벤더의 커리큘럼, 중국 주류 가이드, 그리고 벤더 자체의 루프 자료를 갖게 되었다. 그것이 갖지 못한 것은 학술 문헌, 정착된 수용, 또는 이것이 harness engineering에 스케줄러와 상태 파일을 붙인 것이 아니라 진정한 네 번째 세대라는 합의다. 본 가이드는 이를 정착된 것이 아니라 떠오르는 것으로 추적한다 —— 그리고 두 사람이 같은 루프를 지어도 상반된 결과를 얻을 수 있다는 Osmani 자신의 경계가, 이 프레임 전체가 왜 그런지에 대한 가장 공정한 요약이다.

---

## Sources

- Steinberger, Peter (@steipete). "loops, not prompts" 프레이밍을 촉발한 포스트 (2026년 6월 7일): [https://x.com/steipete/status/2063697162748260627](https://x.com/steipete/status/2063697162748260627) —— 2026년 7월 중순 기준 8.4M+ 노출; 포스트 자체는 "loop engineering"이라는 문구를 쓰지 않는다.
- Osmani, Addy. "Loop Engineering" (2026년 6월 7일): [https://addyosmani.com/blog/loop-engineering/](https://addyosmani.com/blog/loop-engineering/); O'Reilly Radar에 신디케이트 (2026년 6월 22일): [https://www.oreilly.com/radar/loop-engineering/](https://www.oreilly.com/radar/loop-engineering/) —— 명명 에세이; 정의, "harness 바로 한 층 위," 다섯 조각, 아침-트리아지 실제 사례.
- Osmani, Addy. "Own the Outer Loop" (2026년 7월 8일 X에서 발표; Substack byline 7월 9일): [https://addyo.substack.com/p/own-the-outer-loop](https://addyo.substack.com/p/own-the-outer-loop) —— 이너 루프 대 아우터 루프; Quality / Verdict / Answerability; cognitive debt, cognitive surrender, orchestration tax.
- Cherny, Boris. "Head of Claude Code: what happens next" 인터뷰, Lenny's Podcast / Lenny's Newsletter (2026년 중반): [https://www.lennysnewsletter.com/p/head-of-claude-code-what-happens](https://www.lennysnewsletter.com/p/head-of-claude-code-what-happens) —— "나는 더 이상 Claude에게 prompt하지 않는다 ... 내 일은 루프를 짜는 것이다" 문장; 매체마다 일관되지 않게 받아 적힌 구어체 인용이며, 그 유보와 함께 여기 인용된다.
- Rajasekaran, Prithvi. "Harness design for long-running application development," Anthropic Engineering (2026년 3월 24일): [https://www.anthropic.com/engineering/harness-design-long-running-apps](https://www.anthropic.com/engineering/harness-design-long-running-apps) —— generator/evaluator (GAN에서 영감) 분할; 회의적인 독립 evaluator; Playwright-MCP 행동 검증.
- Runkle, Sydney. "The Art of Loop Engineering," LangChain blog (2026년 6월 16일): [https://www.langchain.com/blog/the-art-of-loop-engineering](https://www.langchain.com/blog/the-art-of-loop-engineering) —— 네 개의 쌓인 단 ("Loop 1: The Agent" / "Level 2/3/4"); "loopcraft"는 Swyx에게 귀속.
- Kaliski, Steve. Stripe "minions," *How I AI* with Claire Vo (2026년 3월); Stripe developer blog, *Minions* (Parts 1 & 2): [https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents](https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents) —— 주당 ~1,300개 minion PR (인간이 리뷰, 인간이 작성한 코드 없음); 결정론적 MCP 사전-hydration; Goose fork; devbox = EC2, "pet이 아니라 cattle" (dev blog).
- 程序员鱼皮 (liyupi). 「提示词工程已死，Loop Engineering 称王！保姆级教程 + 项目实战」, codefather.cn (2026년 6월 16일): [https://www.codefather.cn/post/2066793761979092994](https://www.codefather.cn/post/2066793761979092994) —— 層層包含 중첩; 말/기수 비유; GitHub @liyupi 23.9k 팔로워.
- Anthropic (@ClaudeDevs). X Article "Getting started with loops" (2026년 7월 6일): [https://x.com/ClaudeDevs/status/2074208949205881033](https://x.com/ClaudeDevs/status/2074208949205881033); 정본 미러: [https://claude.com/blog/getting-started-with-loops](https://claude.com/blog/getting-started-with-loops) —— (7월 중순 기준) ~6.0M 노출 / 38K+ 북마크; "loops"를 가르치지만, "loop engineering" 라벨은 블로그 미러의 프레이밍이다.
- Claude Code 제품 문서: `/loop`와 예약 작업 [https://code.claude.com/docs/en/scheduled-tasks](https://code.claude.com/docs/en/scheduled-tasks) (v2.1.71; 7일 반복-작업 만료); `/goal` [https://code.claude.com/docs/en/goal](https://code.claude.com/docs/en/goal) (v2.1.139+; 신선한-모델 조건 확인; prompt 기반 Stop hook wrapper); Cloud Routines [https://code.claude.com/docs/en/routines](https://code.claude.com/docs/en/routines) (Anthropic이 관리하는 인프라; 1시간 최소; 실행마다 신선한 클론).
- Codex scheduled automations (ChatGPT/Codex docs): [https://learn.chatgpt.com/docs/automations](https://learn.chatgpt.com/docs/automations) —— 매일/매주 스케줄에 더해 커스텀 RFC 5545 RRULE 주기.
- Snorkel AI / UC Berkeley SkyRL / UW-Madison. "Continual Learning Bench," arXiv 2606.05661 (2026년 6월): [https://arxiv.org/abs/2606.05661](https://arxiv.org/abs/2606.05661) —— 에이전트 / 메모리 시스템 / 작업으로 인수분해; Snorkel의 Benchtalks 인터뷰에서 나온 정성적 Fable-백본 발견; 출시 시점 최고 수준 ~25% 정규화 이득, in-context learning이 선두.

---

*이전 장: [12장 — 지식 엔지니어링을 위한 로컬 모델](12-local-models.md)*

*다음 장: [14장 — Graph Engineering](14-graph-engineering.md)*
