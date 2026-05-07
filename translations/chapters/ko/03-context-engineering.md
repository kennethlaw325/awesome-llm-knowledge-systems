# 3장: Context Engineering —— 윈도우를 채우는 기예

> **한 문장으로:** Context engineering은 AI에게 적절한 시점에 정확히 적절한 정보를 주는 기예이다 ——너무 많지도, 너무 적지도 않게.
>
> **왜 중요한가:** 더 좋은 context는 더 좋은 AI 답을 의미한다. 어떤 사람들은 AI에서 놀라운 결과를 얻는데 다른 사람들은 일반적인 응답만 얻는 이유가 이것이다.

> "Context engineering은 다음 단계에 필요한 정확히 적절한 정보로 context window를 채우는 섬세한 기예이자 과학이다."
> ——Andrej Karpathy, 2025년 6월

Prompt engineering이 좋은 질문을 작성하는 것이라면, context engineering은 그것을 둘러싼 브리핑 패킷 전체를 만드는 것이다. 한쪽에서 다른 쪽으로의 전환은 실무자들이 LLM 시스템을 어떻게 생각하는가에 대한 근본적 변화를 표시한다: 설계의 단위는 더 이상 단일 지시가 아니라 *정보 환경*이다.

본 장은 그 풍경 ——이론적 프레임워크부터 운영 검증된 패턴까지 —— 을 매핑하고, 이 분야를 정의하는 1차 출처들로 안내한다.

---

## 3.1 Prompt에서 Context로

"context engineering"이라는 용어는 2025년 중반에 Karpathy가 그것과 prompt engineering 사이에 날카로운 선을 그으면서 주류 사용에 진입했다. Prompt는 정적 문자열이다. Context는 모델이 필요로 하는 모든 것 ——지시, 메모리, 검색된 문서, 도구 정의, 대화 이력, 그리고 즉시 작업 —— 의 동적으로 조립된 패키지로, 프로그래밍 방식으로 구성되고 모든 턴에 갱신된다.

이 구분이 중요한 이유는, 현대 에이전트가 같은 context를 두 번 보내는 일이 드물기 때문이다. 각 추론 호출은 라우팅 로직, 검색 파이프라인, 압축 휴리스틱, 도구 가용성 검사의 산물이며, 이것들이 함께 무엇이 윈도우를 채우고 무엇이 빠지는지를 결정한다.

## 3.2 6계층 Context 모델

Anthropic의 [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents)와 인접 실무자 글에 기술된 패턴을 바탕으로, context window는 가장 영구적인 것에서 가장 일시적인 것 순으로 6개의 개념적 계층으로 유용하게 분해될 수 있다. 여기의 라벨은 본 가이드의 교육적 종합이며, Anthropic 자신이 발표하는 분류법이 아니다:

| 계층 | 내용 | 전형적 영속성 |
|------|------|------------|
| **System Rules** | 안전 제약, 페르소나 정의, 행동 가드레일 | 배포당 정적 |
| **Memory** | 사용자 선호, 이전 세션 요약, 학습된 사실 | 세션 횡단 |
| **Retrieved Documents** | RAG 결과, 검색 스니펫, 파일 내용 | 턴당 |
| **Tool Schemas** | 함수 정의, API 사양, 능력 선언 | 세션당 또는 턴당 마스킹 |
| **Conversation History** | 이전 메시지, 어시스턴트 응답, 도구 호출 결과 | 슬라이딩 윈도우 |
| **Current Task** | 즉시 사용자 요청 + 작업 특정 주입 | 턴당 |

핵심 통찰은 각 계층이 다른 갱신 주기, 다른 압축 전략, 다른 실패 모드를 가진다는 것이다. Retrieved Documents 계층을 과채우는 것은 Current Task 신호를 익사시킨다. Memory를 덜 채우는 것은 모델이 이미 가져야 할 context를 다시 도출하도록 강제한다. 좋은 context engineering은 6개 계층 모두에 걸친 동시적 균형에 관한 것이다.

## 3.3 Manus의 교훈: 북극성으로서의 KV-Cache

2025년 7월, Yichao "Peak" Ji (Manus CTO)는 단일 운영 지표 ——**KV-cache 적중률** —— 을 중심으로 context engineering을 다시 짠 운영 교훈 모음을 발표했다.

Manus는 자신들의 에이전트 시스템에서 입력과 출력 토큰의 일관된 100:1 비율을 관찰했다. 그 비율에서 입력 비용이 모든 것을 지배한다. KV-cache 적중 ——이전에 계산된 키-값 쌍이 다시 계산되지 않고 재사용되는 곳 —— 가 지연과 비용 모두에 대한 1차 레버가 된다.

이 통찰에서 세 기법이 부상했다:

1. **추가 전용 context 구조.** 이전 부분의 context를 다시 쓰지 마라. 중간에서의 삽입이나 편집은 캐시된 접두사를 무효화하여 전체 재계산을 강제한다. context를 문서가 아니라 로그로 설계하라.

2. **스키마 제거가 아닌 logit bias를 통한 도구 마스킹.** 도구가 일시적으로 사용 불가할 때, Manus는 context에서 도구 정의를 제거하지 않고 logit 레벨 마스킹을 통해 그 선택을 억제했다. 정의를 제거하면 토큰 시퀀스가 바뀌어 캐시가 깨진다. 마스킹은 접두사를 보존하면서 선택을 막는다.

3. **롤링 todo-list 재작성.** 긴 대화 초반의 목표를 모델이 회상하기를 의지하기보다, Manus는 주기적으로 재작성된 todo list를 context의 끝 가까이에 추가했다. 이는 어텐션의 최근성 편향을 활용한다 ——가장 최근 토큰의 목표가 수천 토큰 앞에 묻힌 동일한 목표보다 더 강한 어텐션 가중치를 받는다.

이는 prompt 레벨이 아니라 인프라 레벨 결정이다. 그것은 "context engineering"이 시스템 사고를 요구하는 이유를 보여 준다.

## 3.4 다섯 개의 지배적 패턴

Aurimas Griciūnas는 운영 시스템 전반에 관찰된 다섯 개의 반복 패턴으로 신흥 실무를 종합했다 (정전판: "State of Context Engineering in 2026," SwirlAI Newsletter, March 22, 2026, [https://www.newsletter.swirlai.com/p/state-of-context-engineering-in-2026](https://www.newsletter.swirlai.com/p/state-of-context-engineering-in-2026); "Breaking Down Context Engineering"도 참조):

**Progressive Disclosure.** 모든 것을 미리 로드하지 마라. 가벼운 인덱스를 먼저 제시하고, 모델 (또는 라우팅 로직)이 관련성을 결정할 때만 섹션을 확장하라. 이는 context 윈도우의 lazy loading 등가물이다. Anthropic 자체의 에이전트 스킬 시스템이 이 패턴을 사용한다 ——17개 스킬이 휴면 상태에서 약 1,700 토큰을 소비하고, 호출 시에만 확장된다.

**Context Compression.** 주입 전에 정보를 요약하거나, 절단하거나, 추출하라. 슬라이딩 윈도우 너머의 대화 이력은 요약으로 압축된다. 검색된 문서는 관련 구절로 발췌된다. 목표는 토큰 수를 줄이면서 의미 밀도를 보존하는 것이다.

**Context Routing.** 모든 쿼리가 같은 context를 필요로 하지는 않는다. 라우팅 계층이 들어오는 요청을 살펴보고 어떤 메모리 뱅크, 도구 세트, 문서 컬렉션을 포함할지 선택한다. 이는 데이터베이스 쿼리 플래너의 context-window 등가물이다.

**Retrieval Evolution.** 정적 RAG (한 번 검색하고, 주입하고, 생성)는 모델이 생성 도중 추가 정보를 요청할 수 있는 반복 검색에 길을 내준다. Context는 한 번에 조립되지 않고 생성 과정을 통해 진화한다.

**Tool and Capability Management.** 도구 라이브러리가 커짐에 따라, 모든 스키마를 로드하는 것은 금지적이 된다. 시스템은 도구 계층을 가볍게 유지하기 위해 메타-도구 패턴 (요청 시 관련 도구 스키마를 반환하는 발견 도구) 또는 스킬 그래프 아키텍처를 사용한다.

## 3.5 학술 풍경

2025년 중반은 context engineering을 형식적 연구 영역으로 다룬 첫 포괄적 학술 서베이를 가져왔다: **"A Survey of Context Engineering for Large Language Models"** (Mei et al., arXiv 2507.13334, 2025년 7월 17–21일). 1,400편이 넘는 연구 논문의 체계적 분석을 통해 이 분야의 기술 로드맵을 확립했다. 서베이는 설계 공간을 두 축을 따라 조직한다: **기초 구성 요소** (context 검색·생성, context 처리, context 관리)와 **시스템 구현** (RAG, 메모리 시스템, 도구 통합 추론, 다중 에이전트 시스템). 그것의 부담을 떠받치는 발견은 근본적 능력 비대칭이다: 현재 모델은 복잡한 context 이해에 놀랍도록 능숙하지만, 동등하게 정교한 장문 출력 생성에는 두드러진 한계를 보인다. 실무자에게 이 서베이는 이 분야가 가진 교과서에 가장 가까운 것이다 ——그것은 경험적으로 발견된 것을 형식화했다. context engineering은 단일 기법이 아니라 여러 독립 차원을 가진 설계 공간이라는 것을.

## 3.6 Agentic Context Engineering (ACE)

ACE 논문, **"Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models"** (Zhang et al., arXiv 2510.04618, 2025년 10월 6일; 동반 저장소 [github.com/ace-agent/ace](https://github.com/ace-agent/ace))는 개념적 전환을 도입했다: context를 정적 어셈블리가 아니라 **진화하는 playbook**으로 다루는 것. ACE 시스템에서 context는 에이전트 자신이 유지하는 살아 있는 문서다 ——관찰을 더하고, 계획을 갱신하고, 무관한 이력을 가지치고, 작업 진행에 따라 자신의 지시를 재구조화한다. 보고된 헤드라인 이득: 에이전트 벤치마크에서 +10.6%, 금융 작업에서 +8.6%, 적응 지연과 롤아웃 비용 감소와 함께. AppWorld 리더보드에서 ACE는 더 작은 오픈소스 모델을 사용하면서도 전체 평균에서 최상위 운영 레벨 에이전트와 일치하고 더 어려운 test-challenge 분할에서는 그것을 능가한다. ACE는 또한 자신이 대비해 엔지니어링된 실패 모드를 명명한다: **brevity bias** (간결한 요약을 위해 도메인 통찰을 잃는다)와 **context collapse** (반복 재작성이 시간에 걸쳐 디테일을 침식한다).

이는 context engineering을 순수 인프라 관심사 (각 호출 전 harness가 무엇을 조립하는가)에서 협업적 관심사 (harness가 *그리고* 모델이 능동적으로 다시 형성하는 것 무엇을 준비하는가)로 옮긴다. "시스템이 제공하는 context"와 "모델이 만드는 context" 사이의 경계가 유동적이 된다.

ACE 시스템은 일반적으로 context 안에 구조화된 스크래치패드를 유지한다 ——모델이 작업 노트, 중간 결과, 수정된 계획을 쓰는 지정된 영역. Harness는 자신의 정책에 따라 주변 계층을 관리하면서 이 영역을 턴에 걸쳐 보존한다.

## 3.7 실무적 함의

이 풍경에서 몇 가지 원칙이 부상한다:

- **출력만이 아니라 입력 토큰을 측정하라.** 운영 스케일에서, 100:1 입력/출력 비율은 context 어셈블리 비용이 지배함을 의미한다. 캐시 적중과 최소 중복을 위해 최적화하라.
- **Context를 계층 시스템으로 설계하라.** 각 계층은 자신의 갱신 정책, 압축 전략, 실패 모드를 가진다. 그것들을 독립적으로 다루어라.
- **기본으로 progressive disclosure를 사용하라.** 가볍게 시작하라. 요청 시 확장하라. 무관한 정보를 포함하는 비용은 단지 토큰이 아니다 ——저하된 어텐션과 증가된 환각 위험이다.
- **Prompt만이 아니라 context 구성을 테스트하라.** 다른 context의 같은 prompt는 다른 결과를 낳는다. 당신의 테스트 스위트는 단지 최종 지시가 아니라 context를 변화시켜야 한다.
- **모델 개선을 예상하라.** 모델이 long-context 추론에 더 능해질수록, 어떤 압축과 라우팅 전략은 불필요한 오버헤드가 된다. 계층이 단순화되거나 제거될 수 있도록 명확한 추상 경계로 만들어라.

---

## Sources

- **Karpathy, Andrej.** Public remarks on "context engineering" (mid-2025). Widely-shared framing across X and the AI engineering community that coined the working definition adopted across the field.
- **Anthropic.** "Building Effective Agents." Anthropic engineering blog, December 19, 2024. [https://www.anthropic.com/engineering/building-effective-agents](https://www.anthropic.com/engineering/building-effective-agents) --- describes orchestrator-worker patterns and evaluator-optimizer workflows; this guide labels the six conceptual layers in §3.2 pedagogically.
- **Ji, Yichao "Peak"** (Manus). "Context Engineering Lessons from Building Manus." Blog post, July 2025. [manus.im/blog](https://manus.im/blog) --- KV-cache hit rate as the operational metric, append-only context structure, tool masking via logit bias, rolling todo-list rewrites.
- **Griciūnas, Aurimas.** "State of Context Engineering in 2026." SwirlAI Newsletter, March 22, 2026. [https://www.newsletter.swirlai.com/p/state-of-context-engineering-in-2026](https://www.newsletter.swirlai.com/p/state-of-context-engineering-in-2026). See also "Breaking Down Context Engineering": [https://www.newsletter.swirlai.com/p/breaking-down-context-engineering](https://www.newsletter.swirlai.com/p/breaking-down-context-engineering)
- **Mei, Lingrui et al.** "A Survey of Context Engineering for Large Language Models." arXiv 2507.13334, July 17-21, 2025. [https://arxiv.org/abs/2507.13334](https://arxiv.org/abs/2507.13334) --- 1,400+ paper review establishing context engineering as a formal research area.
- **Zhang, Qizheng et al.** "Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models." arXiv 2510.04618, October 6, 2025. [https://arxiv.org/abs/2510.04618](https://arxiv.org/abs/2510.04618). Companion repo: [github.com/ace-agent/ace](https://github.com/ace-agent/ace). Frames contexts as evolving playbooks; names brevity bias and context collapse.
- **Schmid, Philipp.** "The New Skill in AI is Not Prompting, It's Context Engineering" and follow-up. [https://www.philschmid.de/context-engineering](https://www.philschmid.de/context-engineering); [https://www.philschmid.de/context-engineering-part-2](https://www.philschmid.de/context-engineering-part-2)
- **LangChain blog.** Context-engineering coverage at [blog.langchain.com](https://blog.langchain.com) --- the Agent Engineer framing as a practitioner pattern (no single canonical post; cited as discourse anchor).
- **Willison, Simon.** Ongoing AI engineering coverage at [simonwillison.net](https://simonwillison.net) --- accessible practitioner introductions that connect the ecosystem.
