# 4장: Harness Engineering —— 모델 주변에 OS를 짓기

> **한 문장으로:** Harness는 AI 모델을 둘러싼 모든 것이다 ——그것을 실제로 유용하게 만드는 규칙, 도구, 안전 검사, 워크플로우.
>
> **왜 중요한가:** AI 모델은 강력한 엔진과 같다. 섀시, 핸들, 브레이크가 없으면 쓸모가 없다. Harness는 원시 AI를 제품으로 바꾸는 것이다.

> "Harness의 모든 구성 요소는 모델이 스스로 할 수 없는 것에 대한 가정을 인코딩하며, 그 가정들은 스트레스 테스트할 가치가 있다."
> ——Anthropic, "Building Effective Agents," 2025

> "模型從來都沒有長手。"
> ——Cab, 도구 사용이 모델 문제가 아니라 harness 문제인 이유에 대해

에이전트는 모델이 아니다. 에이전트는 **모델 + harness**이다 ——원시 추론을 신뢰할 수 있는 행동으로 바꾸는, 둘러싼 prompt, 도구, 메모리, 제어 흐름, 평가 로직, 편성 코드의 시스템. 모델은 엔진이고, harness는 차량이다. 본 장은 실무자들이 그 차량을 어떻게 설계하고, 평가하고, 진화시키는지를 살펴본다.

**직관에 관한 노트.** 많은 초심자에게 이를 구체화하는 비유는 "모델은 결코 손을 자라게 하지 않았다"는 Cab의 관찰이다. 코딩 에이전트가 파일을 편집할 때, 그 파일을 편집한 것은 모델이 아니다 ——그것은 모델이 텍스트로 반환한 도구 호출에 의해 트리거된 harness이다. 우리가 "AI"에 귀속시키는 모든 능력은 사실 모델을 둘러싼 harness의 능력이다. Harness를 벗기면 텍스트만 생성할 수 있는 모델이 남는다. 모델을 벗기면 라우팅할 것이 없는 harness가 남는다. Harness engineering은 그 선이 어디에 있는지, 그리고 두 절반이 어떻게 협력하는지를 결정하는 분야이다.

---

## 4.1 Harness 정의

Harness는 모델 가중치가 아닌 모든 것이다. 그것은 다음을 포함한다:

- 시스템 prompt와 지시 템플릿
- 도구 정의와 실행 샌드박스
- 메모리 시스템 (단기, 장기, 일화)
- 계획과 분해 로직
- 제어 흐름 (루프, 조건, 재시도 정책)
- 평가와 자기 교정 메커니즘
- 안전 가드레일과 출력 검증
- Context 어셈블리 파이프라인 (3장)

사용자 메시지를 가진 베어 모델 API 호출은 사소한 harness이다. 계획, 다단계 도구 사용, 자기 평가, 영속 메모리를 가진 운영 에이전트는 복잡한 것이다. Harness engineering 분야는 이 스펙트럼에 걸쳐 원칙 있는 결정을 내리는 것에 관한 것이다.

## 4.2 Böckeler 분류법

Birgitta Böckeler (ThoughtWorks, 2026년 4월)는 Martin Fowler의 *Exploring Generative AI* 시리즈에 기고하며, 표준 참조가 된 harness 구성 요소에 대한 두 축 분류법을 제안했다:

**축 1: 방향**
- **Guides (피드포워드):** 모델이 행동하기 *전에* 행동을 형성하는 구성 요소. 시스템 prompt, few-shot 예제, 도구 스키마, 계획 템플릿. 이들은 레일을 깐다.
- **Sensors (피드백):** 모델이 행동한 *후에* 행동을 평가하고 결과를 다시 먹이는 구성 요소. 출력 검증기, 테스트 러너, 사람 리뷰, 자기 평가 prompt. 이들은 경로를 교정한다.

**축 2: 메커니즘**
- **계산적 통제:** 결정적 코드 ——정규식 검증기, 타입 검사기, 스키마 강제, 권한 검사. 이들은 결코 환각하지 않는 단단한 제약이다.
- **추론적 통제:** 판단, 라우팅, 또는 정제에 사용되는 또 다른 LLM 호출. 평가자 모델, 분류기, 요약기. 이들은 정밀도를 유연성과 거래하는 부드러운 제약이다.

분류법은 설계 공간을 드러낸다. 대부분의 운영 harness는 네 사분면 모두를 사용한다:

|  | 피드포워드 (Guides) | 피드백 (Sensors) |
|--|---------------------|--------------------|
| **계산적** | 도구 입력에 대한 스키마 검증, 권한 허용 목록 | 출력 형식 검사, 테스트 스위트 실행 |
| **추론적** | 계획 prompt, few-shot 라우팅 | 자기 평가, LLM-as-judge, 비평 사슬 |

통찰은 계산적 통제가 더 저렴하고 더 신뢰할 수 있지만 덜 유연하며, 추론적 통제는 모호성을 다루지만 자체적인 실패 모드를 도입한다는 것이다. 좋은 harness 설계는 가능한 곳마다 계산적 통제를 사용하고 진정으로 모호한 결정에 대해서만 추론적 통제를 예약한다.

## 4.3 OpenAI Codex: Harness를 통한 스케일

실무자 커뮤니티에서 널리 인용되는 인상적인 데이터 포인트는 OpenAI의 Codex 내부 사용을 기술한다: **세 명의 엔지니어와 Codex 에이전트 시스템이 약 1,500개의 풀 리퀘스트에 걸쳐 약 100만 줄의 코드를 생산했다.** 생산성 배수는 주로 모델 품질에 관한 것이 아니었다 ——그것은 harness 설계에 관한 것이었다. (구체적 수치는 2025–2026 OpenAI 강연과 포스트를 통해 회람되었다. Codex의 harness에 대한 공개 자료는 [openai.com/index/introducing-codex](https://openai.com/index/introducing-codex)를 참조.)

Codex harness는 다음을 포함했다:
- 자동 PR 분해 (큰 작업을 리뷰 가능한 단위로 쪼개기)
- 각 작업을 위한 샌드박스 실행 환경
- 자동 테스트 생성과 검증
- PR 경계에서의 사람 리뷰 통합
- 저장소 구조와 컨벤션에 관한 영속 context

교훈: 충분한 harness 성숙도에서 모델은 독립 도구가 아니라 더 큰 운영 시스템 안의 한 구성 요소가 된다. Harness는 편성, 품질 관리, 통합을 다룬다 ——어떤 양의 prompt engineering도 다룰 수 없는 관심사들.

## 4.4 IMPACT 프레임워크

2020년대 중반 실무자 담론에서 **IMPACT 기억법** ——Intent, Memory, Planning, Authority, Control flow, Tools —— 이 harness 설계 차원에 대해 생각하는 체계적인 방식으로 부상했다:

- **Intent:** 시스템은 사용자가 실제로 원하는 것을 어떻게 이해하는가? 의도 분류, 명확화 대화, 목표 분해를 포함한다.
- **Memory:** 시스템은 턴과 세션에 걸쳐 무엇을 기억하는가? 대화 버퍼, 벡터 저장소, 구조화된 지식 베이스, 사용자 선호 시스템을 포함한다.
- **Planning:** 시스템은 복잡한 작업을 어떻게 단계로 쪼개는가? Chain-of-thought prompting, 명시적 계획 생성, 액션 공간에 대한 트리 검색을 포함한다.
- **Authority:** 시스템은 무엇을 하도록 허용되는가? 권한 시스템, human-in-the-loop 게이트, 능력 경계를 포함한다.
- **Control Flow:** 실행은 어떻게 진행되는가? 순차 사슬, 병렬 팬아웃, 조건 분기, 종료 조건이 있는 루프, 재시도 정책을 포함한다.
- **Tools:** 시스템은 어떤 외부 능력에 접근할 수 있는가? 함수 정의, API 통합, 코드 실행 환경, 브라우저 접근을 포함한다.

IMPACT는 설계 체크리스트로서 유용하다. Harness를 구축하거나 검토할 때, 각 차원을 걸어 보면 격차가 드러난다. 강한 Tools를 가지지만 약한 Authority를 가진 시스템은 보안 문제가 있다. 강한 Planning을 가지지만 Memory가 없는 시스템은 자신의 실수에서 배울 수 없다. 프레임워크는 이 불균형을 가시화한다.

## 4.5 Meta-Harness 논문: Harness 설계 자동화

Stanford, MIT, KRAFTON의 공동 논문 (2026년 3월)이 **meta-harness** 개념을 도입했다 ——harness 구성을 자동으로 최적화하는 시스템.

그들의 핵심 발견: 같은 벤치마크에서, 같은 기반 모델로, 다른 harness 구성이 **6배의 성능 격차**를 산출했다. 주어진 작업에 대한 최선의 harness 구성은 거의 자명하지 않았고 종종 직관에 반했다. 수동 harness 튜닝은 엄청난 성능을 테이블에 두고 있었다.

Meta-harness 접근은 harness 매개변수 (재시도 횟수, 계획 깊이, 도구 선택 전략, 메모리 윈도우 크기, 평가 엄격성)를 검색 공간으로 다루고 자동 최적화를 사용해 고성능 구성을 찾았다. 시스템은 다른 작업 유형, 다른 모델, 다른 비용 제약에 harness를 적응시킬 수 있었다.

이 결과는 심오한 함의를 가진다: **harness engineering은 알려진 모범 사례를 가진 해결된 설계 문제가 아니다 ——크고 잘 이해되지 않은 검색 공간을 가진 최적화 문제이다.** Harness 설계를 일회성 아키텍처 결정으로 다루는 팀은 프런티어보다 훨씬 아래에서 운영하고 있을 가능성이 높다.

Meta-Harness 논문은 이제 빠르게 움직이는 라인의 한 데이터 포인트이다. 2026년 4월, **AHE 논문** ("Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses," arXiv 2604.25850, Fudan / Peking / Shanghai Qiji Zhifeng)은 문제를 검색에서 *관측가능성*으로 다시 짰다: harness 구성을 검색 공간으로 다루고 그 위에서 옵티마이저를 실행하는 대신, AHE는 세 가지 관측가능성 기둥 ——구성 요소 (명시적이고 되돌릴 수 있는 액션 공간), 경험 (응축된 궤적 증거), 결정 (실행 전에 만들어지는 위변조 가능한 편집 예측) —— 을 계측하고, harness가 자체 런타임 신호를 읽음으로써 스스로 진화하게 한다. 10번의 AHE 반복 후, Terminal-Bench 2 pass@1 69.7%의 Codex-CLI 스타일 베이스라인이 77.0%에 도달, 인간 설계 베이스라인 (71.9%)을 능가하며, harness가 최적화되지 않은 모델 패밀리로 이전되었을 때 **+5.1 ~ +10.1 pp 크로스 패밀리 이득**을 보인다. 크로스 패밀리 이전은 구조적 뉴스다: 진화한 harness는 한 모델의 특이점에 과적합되어 있지 않으며, 그 아래의 기반이 교체되어도 앞으로 운반된다. Meta-Harness 발견 ("harness engineering은 큰 검색 공간을 가진 최적화 문제이다")과 AHE 발견 ("…그리고 검색은 일회성 최적화가 아니라 지속적인 관측가능성 루프로 실행될 수 있다")이 함께, 빠르게 수동 튜닝을 뒤로하고 있는 엔지니어링 실무를 기술한다.

### 연구에서 운영으로: Advisor Tool (2026년 4월)

Meta-harness 발견은 연구 결과였다. 한 달 후, Anthropic은 첫 제품화된 meta-harness 패턴을 출하했다: **Advisor Tool** (베타, `advisor-tool-2026-03-01`). 이 패턴은 더 빠른 실행 모델을 더 능력 있는 자문 모델과 짝짓는다. 실행 모델이 작업의 대부분을 다룬다. 결정 시점에 도달하면 `advisor()`를 호출하고 현재 API 요청을 떠나지 않은 채 전략적 계획이나 경로 교정 (전형적으로 텍스트 토큰 400–700, 사고 포함 1,400–1,800)을 받는다.

Anthropic이 권장하는 기본 구성은 시사적이다:

| 실행 모델 | 자문 모델 | 의도된 사용 |
|----------|---------|--------------|
| Haiku 4.5 | Opus 4.6 | Haiku 단독에서 지능 단계 상승 |
| Sonnet 4.6 | Opus 4.6 | Sonnet 비용으로 Opus 단독 품질 매칭 |
| Opus 4.6 | Opus 4.6 | 가장 어려운 작업에서의 품질 정제 |

이는 가격 전략으로 번역된 6배 meta-harness 격차이다. 모든 토큰에 Opus 요금을 지불하는 대신, 실행에는 Sonnet 요금을, 출력을 실제로 형성하는 1–2번의 자문 호출에는 Opus 요금을 지불한다. Anthropic이 제안한 prompting 패턴은 harness 타이밍을 규칙으로 코드화하기에 인용할 가치가 있다:

> "본격 작업 전 ——쓰기 전, 해석을 확정하기 전, 가정 위에 짓기 전 —— 에 자문을 호출하라. […] 몇 단계보다 긴 작업에서는 접근을 확정하기 전에 적어도 한 번, 완료를 선언하기 전에 한 번 자문을 호출하라."

문서의 몇 가지 디테일은 실무자에게 중요하다:

- **서버 측 서브-추론.** 자문은 같은 `/v1/messages` 요청 안에서 실행된다. 실행 모델이 `server_tool_use` 블록을 방출하면, Anthropic이 전체 트랜스크립트로 별도의 추론 패스를 실행하고, 결과가 `advisor_tool_result`로 돌아온다. 당신의 코드에서 추가 라운드 트립이 없다.
- **약 3 호출에서의 캐시 손익분기.** 자문 도구에서 `caching`을 활성화하면 자문의 트랜스크립트가 5분 또는 1시간 캐시에 쓰여진다. 첫 호출은 추가 비용이 든다. 이득은 약 세 번째 호출에서 시작된다. 짧은 작업은 캐싱을 끄는 편이 낫다.
- **간결성 prompt가 출력을 35–45% 줄인다.** 단일 지시 ——"자문은 100단어 미만으로 응답하고 설명이 아니라 열거된 단계를 사용해야 한다" —— 가 호출 빈도를 바꾸지 않고 자문의 가장 큰 비용 동인을 측정 가능하게 줄인다.
- **명시적 화해 프로토콜.** 자문 조언이 실행 모델이 이미 모은 경험적 증거와 상충할 때, Anthropic의 시스템 prompt는 실행 모델에게 조용히 전환하기보다 "X를 발견했고, 당신은 Y를 제안하는데, 어떤 제약이 동점을 깨는가?"로 프레이밍된 자문 호출을 한 번 더 하라고 말한다. 이는 여러 역할이 의견이 갈릴 때마다 나타나는 "계획자를 믿어야 하는가 데이터를 믿어야 하는가" 질문에 대한 운영 등급의 답이다.

Advisor Tool은 즉각적 유용성을 넘어 중요하다. 이는 meta-harness 사고가 연구 호기심에서 상업적 primitive로 옮겨갔다는 신호이다. "같은 모델, 다른 harness, 6배 격차" 발견은 더 이상 활용하기 위해 연구팀이 필요한 것이 아니다 ——Anthropic이 이를 도구 호출로 노출한다. 다른 연구실들이 자신의 자문/실행 짝짓기로 따를 것을 기대하라. 그리고 harness engineering 채용 공고가 핵심 기술로 다중 모델 협조를 나열하기 시작할 것을 기대하라.

## 4.6 Anthropic의 3-에이전트 아키텍처

자주 반복되는 세 역할 패턴은, 실무자 커뮤니티에 의해 종종 **Planner / Generator / Evaluator**로 요약되며, 2025년에 걸쳐 다중 에이전트 harness에 대한 흔한 프레이밍이 되었다. 이 프레이밍은 Anthropic 자신이 1차 글에서 채택한 라벨이라기보다, Anthropic의 [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents) (orchestrator-worker, evaluator-optimizer)에 기술된 패턴의 교육적 종합으로 가장 잘 읽힌다. 2026년 3월 31일 Claude Code 소스 유출 (본 섹션 후반에서 다룸)은 그 구분을 확인했다: 운영에서 Anthropic의 실제 harness는 문자 그대로의 세 역할 분해가 아니라 계층화된 자기 치유 메모리를 중심으로 조직된다. 그래도 이 역할들은 유용한 분류법을 기술하므로, 본 섹션은 관심사 분리를 논의하는 데 그것들을 사용한다:

- **Planner:** 작업을 하위 작업으로 분해하고, 전체 계획을 유지하고, 언제 수정할지 결정한다.
- **Generator:** 개별 하위 작업을 실행한다 ——코드 작성, 텍스트 초안, 도구 호출.
- **Evaluator:** 작업 요구사항에 대한 Generator 출력을 평가하고 구조화된 피드백을 제공한다.

이 관심사 분리는, 본 장이 **context anxiety**와 **self-evaluation bias**라고 라벨링하는 두 실패 모드를 다루기 위해 널리 사용된다 (라벨은 본 가이드가 사용하는 프레이밍이다. 기저 관찰은 Anthropic의 발표된 에이전트 연구에서 영감을 받은 패턴에 나타난다):

**Context Anxiety.** 단일 에이전트가 계획, 실행, 평가를 모두 다룰 때, 그것은 헷지하는 경향이 있다. 출력에 단서를 달고, 불필요한 주의를 더하고, 작업 실행보다 메타 코멘터리에 토큰을 쓴다. 역할을 분리하면 각 에이전트가 다른 것들의 인지 부하를 짊어지지 않고 집중할 수 있다.

**Self-Evaluation Bias.** 모델은 자신의 출력을 평가하는 데 체계적으로 약하다. 그들은 잘 문서화된 관대함 편향을 보인다 ——독립 심사자가 평가했을 것보다 자기 작업을 더 높게 평가한다. 3-에이전트 아키텍처는 생성된 출력에 투자가 없는 별도의 평가자 (잠재적으로 다른 모델이나 다르게 prompt된 인스턴스)를 사용해 이를 완화한다.

Anthropic의 evaluator-optimizer 가이드에서 관찰된 패턴과 일관되게, 실무자 커뮤니티가 강조해 온 미묘함: **평가자 보정 자체가 harness engineering 문제이다.** 지나치게 엄격한 평가자는 무한 수정 루프를 일으킨다. 지나치게 관대한 평가자는 저품질 작업을 통과시킨다. 평가자의 임계와 기준은 생성자의 지시만큼 신중하게 튜닝되어야 한다.

### Claude Code 유출: 경험적 일별 (2026년 3월 31일)

2025년 대부분 동안 3-에이전트 아키텍처는 Anthropic의 발표된 연구를 통해 알려졌고 행동에서 추론되었다. **2026년 3월 31일**, 그것이 변했다. Anthropic이 npm 패키지 **`@anthropic-ai/claude-code` v2.1.88** 안에 59.8MB 소스 맵을 실수로 발행하여, **1,906개 파일에 걸쳐 약 513,000줄의 난독화되지 않은 TypeScript**를 노출했다. Anthropic은 이 사건을 "보안 침해가 아니라 인간의 패키징 오류"로 규정했지만, 실무자들은 처음으로 프런티어 연구실의 운영 harness를 직접 읽을 수 있었다.

커뮤니티가 아키텍처를 기술하는 방식을 다시 짠 유출의 몇 가지 발견:

- **그것은 문자 그대로 "Planner / Generator / Evaluator"가 아니다.** Claude Code를 4.6 세 역할 프레이밍에 매핑했던 이전 커뮤니티 글들은 연구의 오독으로 드러났다. 실제 아키텍처는 **3계층 "Self-Healing Memory"** 시스템으로 조직되어 있다. 계층은 스크래치패드 / 작업 상태, 압축된 중기 상태, 영속 프로젝트 메모리에 대응하며 ——계층 간 명시적 수리 및 화해 로직을 갖추고 있다.
- **`MEMORY.md`는 인덱스이지 저장소가 아니다.** 단일체적 메모리 파일이 아니라, `MEMORY.md`는 더 상세한 노트들로 향하는 **가벼운 포인터 인덱스** 역할을 한다. 이는 트랜스크립트보다 파일시스템 디렉토리에 가까우며, 메모리 계층이 context를 부풀리지 않고 스케일할 수 있게 하는 것이다.
- **`KAIROS`는 자율 데몬 모드이다.** `KAIROS`라는 피처 플래그가 소스 전반에 **150회 이상** 참조된다. 그것은 자율 데몬 모드 ——대부분의 사용자가 아는 인터랙티브 REPL을 훨씬 넘어가는, 무인의 장기 실행 실행 루프 —— 를 게이트한다.
- **44개의 숨겨진 피처 플래그.** `KAIROS` 외에, 소스는 미공개 능력을 위한 44개의 피처 플래그를 담고 있어, 공개로 출하되는 것이 harness가 내부적으로 실제로 지원하는 것의 보수적 부분 집합임을 시사한다.

실무적 결론: Planner / Generator / Evaluator 분할은 유용한 개념적 분류법으로 남아 있지만 (그리고 Anthropic의 연구 논문은 여전히 그러한 용어로 시스템을 기술한다), 운영에서 아키텍처는 역할 분해만이 아니라 **메모리와 수리**를 중심으로 계층화되어 있다. 2026년 harness engineering은 점점 더 메모리 계층과 그 사이의 전이를 설계하는 것을 의미한다.

유출 두 주 후, 같은 아키텍처는 또 다른 단계를 밟았다 ——이번에는 사용자의 머신에서 멀어지는, 바깥쪽으로. **Claude Code Routines** (2026년 4월 14일)와 함께, Anthropic은 오케스트레이터 시트 자체를 노트북에서 떼어 자체 클라우드 위로 옮겼고, 스케줄, API, GitHub 이벤트 트리거를 1급 harness primitive로 노출했다. 유출과 함께 읽으면, 이는 명확한 아키텍처 수사이다: 오케스트레이터는 더 이상 사용자가 돌보는 REPL로 모델링되지 않고, Anthropic의 기반 위에 사는 데몬으로 모델링된다. 3계층 자기 치유 메모리가 트리거에 걸쳐 영속한다. Harness는 더 이상 루프가 진전을 만들기 위해 사용자의 프로세스가 살아 있을 필요가 없다. Routines를 채택하든 안 하든, 프레이밍은 이제 공중에 있다: 오케스트레이터 시트는 제품 표면이며, "루프가 어디서 실행되는가"는 기본값이 아니라 설계 결정이다.

## 4.7 해자로서의 Harness

2026년 초, Meta가 약 20억 달러에 Manus를 인수했다. Manus는 독점 모델을 가지고 있지 않았다. 그 전체 가치는 harness ——편성 로직, context engineering 파이프라인, 도구 통합 계층, 그리고 일용품 모델 API를 신뢰할 수 있는 에이전트 제품으로 바꾼 운영 인프라 —— 에 있었다.

이 인수는 산업이 발견하고 있던 것을 결정화시켰다: **harness가 해자이다.** 모델은 점점 더 일용품화된다. 차별화는 그것을 어떻게 감싸느냐이다 ——어떤 도구를 제공하는가, 어떻게 context를 관리하는가, 어떻게 실패를 다루는가, 어떻게 다단계 워크플로우를 편성하는가, 어떻게 품질을 평가하는가.

실무자에 대한 함의는 harness engineering이 모델 개발의 "진짜 일"로 가는 길에 거쳐야 하는 배관이 아니라는 것이다. 그것 *이* 대부분의 운영 AI 팀에 진짜 일이다. 2026년 4월까지, "harness engineering"은 형식적 분야로 산업 어휘에 진입했고, Claude Code 유출은 운영 harness가 실제로 무엇을 담고 있는지에 대한 첫 경험적 일별을 제공했다.

## 4.8 Harness 유지: 스트레스 테스트 책무

Anthropic의 가장 실행 가능한 통찰은 가장 단순할지도 모른다: 모든 harness 구성 요소는 모델 한계에 대한 가정을 인코딩하며, **그 가정들은 만료된다.**

GPT-4 레벨 능력을 중심으로 harness가 만들어졌을 때, 그것은 다음을 포함했을 수 있다:
- 명시적 chain-of-thought prompting (모델이 그것을 필요로 했기 때문에)
- 공격적 출력 파싱 (모델이 형식에 일관적이지 않았기 때문에)
- 다단계 검증 (단일 패스 정확도가 불충분했기 때문에)
- 상세한 few-shot 예제 (zero-shot 성능이 좋지 않았기 때문에)

개선된 추론, 지시 따르기, 출력 일관성을 가진 더 새 모델이 도착함에 따라, 이 구성 요소들은 **더 이상 부담을 짊어질 필요가 없을지도 모르는 부담을 떠받치는 벽**이 된다. 그것들은 품질에 기여하지 않으면서 지연, 비용, 복잡도를 더한다.

분야는 주기적 스트레스 테스트이다: 어떤 것이 여전히 필요한지를 결정하기 위해 harness 구성 요소를 체계적으로 비활성화하기. 계획 단계를 제거하는 것이 성능을 저하시키지 않는다면, 그것을 제거하라. 모델이 이제 few-shot 예제 없이 형식을 신뢰할 수 있게 따른다면, 그것을 떨어뜨려라. 자기 평가가 비용을 더하지만 품질을 더하지 않는다면, 그것을 제거하라.

이는 직관에 반한다. 엔지니어들은 자연스럽게 안전 메커니즘을 추가하고 그것을 제거하는 것에 저항한다. 그러나 harness engineering에서 불필요한 구성 요소는 무료가 아니다 ——그것들은 context window 공간을 소비하고, 지연을 더하고, 비용을 증가시키고, 유지 부담을 만든다. 현재 모델의 능력과 일치하는 가벼운 harness가 더 약한 모델을 위해 과도하게 엔지니어링된 것보다 더 잘 수행한다.

실무적 권장: 새 모델을 온보딩할 때, 기존 harness를 실행하는 것으로 시작하고, 그 다음 작업 성능을 측정하면서 체계적으로 구성 요소를 벗겨라. 남은 것이 당신의 진짜 harness이다. 제거된 것은 이전 능력 시대의 기술 부채였다.

성숙한 harness는 결국 스트레스 테스트 질문을 뒤집는다: "어떤 구성 요소를 제거할 수 있는가" 대신, "어떤 구성 요소에 더 많은 컴퓨트를 써야 하는가, 그리고 언제"를 묻는다. 2026년 4월 **CATTS** 프리프린트 (Consensus-Aware Test-Time Scaling, arXiv 2602.12276)가 그 질문에 사용 가능한 답을 준다. CATTS는 에이전트 단계당 작은 롤아웃 위원회를 표집하고 그들 사이의 불일치를 단계당 불확실성 점수로 사용한다. 그 점수는 그 다음 비균일하게 테스트 시 컴퓨트를 할당하는 데 사용된다 ——위원회가 의견이 갈리는 곳에는 더 많은 롤아웃, 그것이 수렴하는 곳에는 더 적은 롤아웃. WebArena-Lite와 GoBrowse에서 이 기법은 균일 스케일링보다 **2.3배 더 적은 토큰**으로 작업 정확도 **+9.1%**를 보고한다. 성숙한 harness에 대해, CATTS는 Advisor Tool 옆에 끼어든다: 자문 패턴은 *무엇*에 대해 생각할지를 결정하고, CATTS는 각 단계에 대해 *얼마나 깊게* 생각할지를 결정한다. 둘 다 가정 ("항상 세 번 재시도," "어려운 문제에는 항상 Opus를 사용")을 런타임에 계산되는 측정된 불확실성 신호로 대체한다.

2026년 4월의 AHE 결과 (섹션 4.5)는 같은 점을 구조적으로 만든다: 스트레스 테스트는 일회성 검토 활동이 아니라 지속적인 관측가능성 루프이다. 수동 스트레스 테스트는 실무자들이 오늘 실행할 수 있는 분야로 가치 있게 남아 있다. AHE는 그것이 자동화 가능하기도 함을 보여 준다.

## 4.9 클라우드 네이티브 Harness Primitive

2025년과 2026년 1분기에 걸쳐, harness는 압도적으로 당신이 직접 만들고 실행하는 것이었다. 가장 정교한 패턴들조차 ——3-에이전트 아키텍처, Advisor Tool, KAIROS 스타일 자율 루프 —— 여전히 당신의 코드가 오케스트레이터 시트를 차지한다고 가정했다. 당신이 cron job을 작성하고, 당신이 데몬을 실행하고, 당신이 노트북을 깨워 두고, 당신이 실패 모드를 소유했다. 기반은 일반 컴퓨트 (Mac mini, VPS, Kubernetes 파드)였고, harness 계층은 프로세스 슈퍼바이저 위로 당신의 책임이었다.

**2026년 4월 14일**, Anthropic의 **Claude Code Routines** research preview가 그것을 바꾸기 위한 첫 구체적 단계를 밟았다. Routine은 사용자의 머신이 아니라 Anthropic의 클라우드에서 실행되는 Claude Code 워크플로우이며, 세 트리거 중 하나에 의해 발사된다: **스케줄** (cron 등가물), **API 호출** (다른 서비스로부터의 프로그램적 호출), **GitHub 이벤트** (push, PR, issue, comment). 트리거는 harness 엔지니어들이 지난 18개월 동안 작성해 온 파일 기반 스케줄링 패턴의 의도적 일반화이다: 같은 `매주 평일 09:00 HKT에 실행` 의미론, 그러나 `cron + tmux + claude` 셸 주문이 아니라 관리되는 primitive로 표현된다. 쿼터는 기저 Claude Code 구독과 등급화된다 ——**Pro 5/일, Max 15/일, Team/Enterprise 25/일** —— 이는 기반을 "시간당 원시 컴퓨트"가 아니라 "시트당 하루 의미 있는 루프 한 줌"으로 가격 매긴다.

클라우드 측 실행 디테일은 들리는 것보다 더 중요하다. 셀프 호스팅 파일 기반 스케줄러는 사용자가 소유한 하드웨어에서 오케스트레이터 시트를 차지한다. Mac이 닫혀 있거나, 잠자거나, 배터리가 떨어지면 루프는 실행되지 않는다. Routine은 사용자의 머신 상태와 무관하게 완료된다. 이는 전체 실패 모드 부류 (노트북 뚜껑, 네트워크 끊김, OS 갱신, 우발적 전원 사이클)와 대응하는 보상 메커니즘 부류 (wake-on-LAN 트릭, "항상 켜진" Mac Mini 서버, 중복 러너)를 해소시킨다. 진정으로 이벤트 주도인 워크플로우 ——"PR이 열릴 때 X를 하라" —— 에 대해, 관리되는 primitive는 셀프 호스팅 폴러보다 솔직히 더 잘 맞는다.

트레이드오프는 새 천장이다. 관리되는 primitive는 작업 부하의 물리학이 아니라 트리거와 쿼터로 자신을 가격 매긴다. 그것은 당신의 루프가 스케줄 / API / GitHub-이벤트 모양에 맞고, 일일 쿼터가 충분하며, Anthropic의 기반이 당신의 코드와 데이터가 살기에 적절한 곳이라고 가정한다. 사소하지 않은 harness 작업 부하 집합에 대해, 이 가정 중 어느 것도 깔끔하게 성립하지 않는다. 인증된 세션의 **브라우저 자동화**는 사용자의 쿠키, 프로필, 신뢰 상태를 이미 가진 머신에서 실행되는 것이 여전히 이득이다. **고빈도 편성** ——분 미만 폴링, 실시간 시장 또는 센서 데이터, 하루 25 호출이 모욕적인 무엇이든 —— 은 트리거가 아니라 초로 청구되는 런타임이 필요하다. **비-GitHub 이벤트 소스** (Discord 메시지, 내부 웹훅, 커스텀 MCP 서버, 디바이스 위 파일시스템 이벤트)는 Routines에서 아직 1급 트리거가 없다. 그것들을 표면화하는 것은 다리를 직접 작성해야 하며, 그것은 어쨌든 다리를 실행하기 위해 셀프 호스팅 머신으로 다시 돌아가게 한다. 그리고 로컬 파일, 로컬 모델 추론, 또는 로컬 네트워크 접근에 의존하는 무엇이든 구조적으로 클라우드 밖에 남아 있다.

2026년 harness 엔지니어들에 대한 정직한 프레이밍: Routines와 같은 클라우드 네이티브 primitive는 harness 작업 부하의 **GitHub 이벤트 트리거된, 스케줄된, API 호출된** 사분면에 맞는 답이며, 그 사분면의 운영 비용을 이후 12개월 동안 극적으로 압축할 가능성이 높다. 셀프 호스팅 harness는 사라지지 않고 있다 ——그것은 실제로 자신의 비용을 지불하는 곳으로 좁혀지고 있다. 개발할 분야는 본 장이 향해 짓고 있던 것과 같은 분야이다: 각 구성 요소가 어떤 가정을 인코딩하는지를 알고, 그 아래의 기반이 변할 때 알아채는 것.

**Routines vs. Managed Agents.** Anthropic이 2026년 4월에 실제로 출하한 것에 대해 정확한 것이 가치 있다. 두 조각이 때때로 혼동되기 때문이다. **Claude Managed Agents** (퍼블릭 베타, 2026년 4월 8일)는 *기반*이다: 세션 (추가 전용 이벤트 로그), harness (Claude를 호출하고 도구 호출을 라우팅하는 루프), 샌드박스 (실행 환경)를 세 가지 가상화된 구성 요소로 노출하는 호스팅 런타임이며, 그 위에 트레이싱과 Agent / Environment / Session / Events API 표면이 얹혀 있다. SiliconANGLE의 출시 보도는 기반을 표준 토큰 요금에 더해 **에이전트 런타임 시간당 8센트**로 가격 매긴다고 보고한다. 이 수치는 Anthropic의 1차 문서가 아니라 2차 기술 언론에서 온 것이다. 2차 인용 바에서조차 가격 구조가 중요하다: 이는 추론과 별개로 오케스트레이터 시트 자체에 미터링하는 첫 프런티어 벤더 primitive이다. **Claude Code Routines** (research preview, 2026년 4월 14일)는 그 기반 (또는 호환 대안) 위에서 실행되는 *트리거링 표면*이다: 스케줄, API 호출, GitHub 이벤트, Pro / Max / Team-Enterprise 등급에 대해 일일 5 / 15 / 25 호출 쿼터. 둘은 다른 질문에 답한다. Managed Agents는 "에이전트 루프가 물리적으로 어디서 실행되며, 그 상태가 턴 사이에 어떻게 내구성 있게 유지되는가?"에 답한다. Routines는 "무엇이 루프를 처음에 시작시키는가?"에 답한다. Routines를 채택하지만 Managed Agents를 채택하지 않는 셀프 호스팅 harness는 자신의 상태와 실행 환경을 계속 소유한다. Managed Agents를 채택하지만 자신의 트리거링 계층을 만드는 것은 작업이 언제 시작하는지를 계속 소유한다. 실무에서, 2026년 중반의 대부분의 클라우드 네이티브 harness 설계는 둘 다 채택할 것이다 ——그러나 언번들링이 아키텍처적 핵심이다. Anthropic은 더 이상 "harness"를 한 가지로 팔지 않는다. 그 구성 primitive들을 팔고 있다.

언번들링은 2026년 4월 후반에 두 가지 구조적으로 의미 있는 움직임으로 계속됐다. 첫째, **4월 23일**에, Anthropic이 **Memory for Managed Agents**를 퍼블릭 베타에 더했다: 에이전트에게 내구성 있는 세션 횡단 상태를 주는 파일시스템에 마운트되고 감사 로그된 저장소. 동시 접근 의미론, 범위가 정해진 엔터프라이즈 권한, Claude Console에서의 롤백 / 삭제 표면을 갖췄다. 기반은 이제 세션과 샌드박스 옆에 세 번째 primitive ——*내구성 메모리* —— 와 함께 출하된다. 3월 31일 Claude Code 소스 유출이 드러낸 운영 아키텍처 (3계층 자기 치유 메모리)가 이제 다른 팀이 빌릴 수 있는 벤더 관리 primitive로 노출된다. 둘째, **4월 28일**에, AWS와 OpenAI가 **Amazon Bedrock Managed Agents powered by OpenAI**를 한정 프리뷰로 출하하며, "OpenAI 에이전트 harness"를 처음으로 별개 제품 표면으로 명명하고 판매했다. 함께 읽으면, 두 사건이 Managed Agents 패턴을 "Anthropic의 4월 8일 베팅"에서 **크로스벤더 기반 형태**로 옮긴다 ——3 프런티어 벤더 중 둘이 이제 에이전트별 정체성, 액션 로깅, 내구성 상태가 내장된 관리 primitive로 오케스트레이터 시트를 출하한다. 2026년 중반에 오케스트레이터 시트에 대해 빌드 대 구매를 비교하는 harness 엔지니어들에게, 옵션 집합은 더 이상 단일 벤더가 아니고 기반은 더 이상 가는 런타임이 아니다: 메모리를 포함한다.

## 4.10 관리되는 추론 전환 (2026년 4월)

2025년에 걸쳐, 호출자와 모델 사이의 harness 계약은 대체로 노브 패널이었다: `temperature`, `top_p`, `top_k`, `max_tokens`, `budget_tokens`, 시스템 prompt. 실무자들은 그 노브들을 사례별로, 때로는 같은 에이전트 루프 안에서 단계별로 돌렸다. 2026년 4월 16일 **Claude Opus 4.7** 릴리스가 그 패턴을 깼다. 단일 릴리스에서, 세 변경이 같은 방향으로 당겼다:

1. **`temperature`, `top_p`, `top_k`가 폐기되었다.** 비기본값은 400 에러를 반환한다. 표집 레벨 통제는 더 이상 호출자의 손에 있지 않다.
2. **적응적 사고가 유일한 사고-온 모드이다.** 수동 `budget_tokens` (extended thinking)가 제거되었다. `effort` (`low`, `high`, `xhigh`, `max`)가 그것을 대체한다.
3. **Task budgets가 1급 primitive가 된다.** 새 베타 헤더 (`anthropic-beta: task-budgets-2026-03-13`)가 호출자에게 *전체 에이전트 루프* ——사고, 도구 호출, 도구 결과, 최종 출력 —— 에 대한 권고 토큰 예산을 선언하게 한다. 모델은 작업하면서 실행 중인 카운트다운을 본다.

처음 두 변경은 빼는 것이다: 노브 제거. 세 번째는 더하는 것이다: 어떤 프런티어 API에도 이전에 존재하지 않던 primitive. 함께 그것들은 계약 변경을 기술한다. "당신이 표집기를 튜닝하고 모델이 응답을 생산한다" 대신, 계약은 이제 "당신이 컴퓨트 예산을 선언하고 모델이 그에 대해 자체 할당하며, 작업이 여전히 얼마만큼의 검색, 추론, 종합을 받을 가치가 있는지 단계별로 결정한다"이다. Harness는 매개변수 보드가 아니라 예산 대화가 된다.

"강제가 아니라 권고" 디테일이 중요하다. Task budgets는 단단한 상한이 아니다 (`max_tokens`가 여전히 그 역할을 하고 호출자를 향한 것으로 남는다). 대신, 모델이 자신의 예산을 들으면 그것을 우선순위화하는 데 사용한다. 실무에서, 너무 빡빡하게 설정된 예산은 저하된 출력이 아니라 거부 스타일 출력을 산출한다 ——모델은 자신이 자금이 부족하다고 판단하는 결과를 출하하기보다 거절하기를 선호한다. 비사소한 작업에 대한 그 실패 모드를 정확히 막기 위해 20K 토큰 최소가 강제된다.

Harness 설계자에게 함의는 구체적이다: Opus 4.6에서 실행된 어떤 harness도 4.7을 위해 재기준화가 필요하다. prompt 레벨만이 아니라 타임아웃, 재시도, 압축, 도구 호출 예산 레벨에서. Anthropic 자신의 마이그레이션 문서가 이를 직접 말한다 ——*prompt만이 아니라 harness를 재기준화하라*. Advisor Tool (섹션 4.5)과 task budgets (본 섹션)는 어떤 장기간 harness에 대해서도 새로운 두 축 최적화를 기술한다: Advisor는 *무엇*에 대해 생각할지를 결정한다. Task budgets는 각 단계에 대해 *얼마나 깊게* 생각할지를 결정한다. 둘 다 노브 돌리기를 런타임에 계산되는 측정된 신호로 대체한다.

이것이 더 넓은 패턴이다: **관리되는 추론 전환.** 프런티어 벤더들은 점점 더 추론 자체를 매개변수 표면이 아니라 제품 표면으로 다루고 있다. Harness 계층은 "당신이 추론 호출을 구성한다"에서 "당신이 작업을 기술하고 추론 계층이 적응한다"로 이동하고 있다. 다른 연구실들이 Anthropic의 구체적 결정 (표집 노브 폐기, 권고 예산)을 따를지 아니면 방향만을 따를지가 열린 질문이다. 방향 자체는 정해진 것 같다.

---

## Sources

- **Böckeler, Birgitta.** "Harness engineering for coding agent users." martinfowler.com (Exploring Generative AI series), April 2, 2026. [https://martinfowler.com/articles/harness-engineering.html](https://martinfowler.com/articles/harness-engineering.html) --- Guides vs. Sensors, Computational vs. Inferential taxonomy.
- **OpenAI.** Codex public-facing material: [https://openai.com/index/introducing-codex](https://openai.com/index/introducing-codex). Anchor for the harness-design framing of OpenAI Codex; the widely-cited "three engineers / ~1M lines / ~1,500 PRs" figures circulated through 2025-2026 OpenAI talks and posts and are reported here as community-cited rather than from a single canonical post.
- **IMPACT mnemonic.** Intent / Memory / Planning / Authority / Control flow / Tools --- a six-dimension harness design checklist that emerged in mid-2020s practitioner discourse. Used in this chapter as a pedagogical framing; not attributed to a specific primary source.
- **Stanford / MIT / KRAFTON.** "Meta-Harness: Automated Optimization of LLM Agent Harnesses." arXiv preprint, March 2026. 6x performance gap finding, automated harness tuning.
- **Lin et al.** "Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses." arXiv 2604.25850, April 28, 2026. [https://arxiv.org/abs/2604.25850](https://arxiv.org/abs/2604.25850) --- Fudan / Peking / Shanghai Qiji Zhifeng. Observability-pillar reframing of the meta-harness search problem; 69.7% → 77.0% on Terminal-Bench 2 with cross-family transfer.
- **Anthropic.** "Claude Managed Agents overview." API documentation, April 8, 2026. [https://platform.claude.com/docs/en/managed-agents/overview](https://platform.claude.com/docs/en/managed-agents/overview)
- **Anthropic Engineering.** "Scaling Managed Agents: Decoupling the brain from the body." April 8, 2026. [https://www.anthropic.com/engineering/managed-agents](https://www.anthropic.com/engineering/managed-agents) --- three virtualized components (session, harness, sandbox); pricing details (standard token rates plus eight cents per agent runtime hour, per SiliconANGLE launch coverage) are not in primary Anthropic documentation and are cited from secondary tech-press.
- **Anthropic.** "Memory for Claude Managed Agents" (April 23, 2026). [https://claude.com/blog/claude-managed-agents-memory](https://claude.com/blog/claude-managed-agents-memory) --- filesystem-mounted memory, cross-session learning, audit logs, scoped enterprise permissions; closes the loop with the March 31 Claude Code source-leak finding on three-layer self-healing memory.
- **AWS and OpenAI.** "Bedrock Managed Agents powered by OpenAI" (April 28, 2026, limited preview). AWS announcement: [https://aws.amazon.com/about-aws/whats-new/2026/04/bedrock-openai-models-codex-managed-agents/](https://aws.amazon.com/about-aws/whats-new/2026/04/bedrock-openai-models-codex-managed-agents/). About Amazon: [https://www.aboutamazon.com/news/aws/bedrock-openai-models](https://www.aboutamazon.com/news/aws/bedrock-openai-models). OpenAI announcement: [https://openai.com/index/openai-on-aws/](https://openai.com/index/openai-on-aws/) --- first time "the OpenAI agent harness" is named and sold as a product surface; cross-vendor convergence on the Managed Agents pattern.
- **Anthropic.** "Building Effective Agents." Anthropic engineering blog, December 19, 2024. [https://www.anthropic.com/engineering/building-effective-agents](https://www.anthropic.com/engineering/building-effective-agents) --- describes orchestrator-worker patterns and evaluator-optimizer workflows; this guide labels the relevant failure modes "context anxiety" and "self-evaluation bias" pedagogically. The practitioner-community summary as a Planner / Generator / Evaluator triple is a framing built on these patterns; Anthropic itself does not use that exact triple in primary writing. The actual Claude Code architecture, as revealed by the March 31, 2026 source leak (Section 4.6), is organized around layered self-healing memory rather than role decomposition.
- **Meta / Manus Acquisition.** Various reporting, early 2026. ~$2B acquisition validating harness-as-moat thesis.
- **Karpathy, Andrej.** "From Vibe Coding to Agentic Engineering" --- fireside chat at Sequoia AI Ascent 2026 (recorded ~late April 2026, primary YouTube video [https://www.youtube.com/watch?v=96jN2OCOfLs](https://www.youtube.com/watch?v=96jN2OCOfLs); author summary at [https://karpathy.bearblog.dev/sequoia-ascent-2026/](https://karpathy.bearblog.dev/sequoia-ascent-2026/)). Frames vibe coding as the *floor-raising* mode (everyone can build) and agentic engineering as the *ceiling-raising* discipline (specs, plan supervision, diff inspection, eval loops, permission scoping, worktree isolation). Anchors a December 2025 inflection point at which Karpathy reports inverting his own coding ratio from ~80% hand-written to ~80% delegated. Earlier 2025 "Software 3.0" / "Software Is Changing (Again)" talks at AI Engineer World's Fair and YC AI Startup School established the broader frame of models as a new kind of programmable component.
- **LangChain.** "Agent Architecture Patterns." LangChain documentation, 2025. Practical patterns for control flow and tool orchestration.
- **Harrison Chase.** "Agent Engineer" framing, 2025 --- LangChain blog and X posts. The phrase entered practitioner vocabulary as a role-definition framing for harness-focused engineering; cited here as a pattern in 2025-era discourse rather than a single canonical post.
- **"CATTS: Consensus-Aware Test-Time Scaling for Agents."** arXiv 2602.12276 (April 2026 release cycle). Vote-derived uncertainty as a test-time compute allocator; +9.1% / 2.3x fewer tokens vs. uniform scaling on WebArena-Lite and GoBrowse. [https://arxiv.org/abs/2602.12276](https://arxiv.org/abs/2602.12276)
- **Anthropic.** "Introducing Routines in Claude Code." Anthropic blog, April 14, 2026. [https://claude.com/blog/introducing-routines-in-claude-code](https://claude.com/blog/introducing-routines-in-claude-code)
- **Anthropic.** "Claude Code Routines documentation." [https://code.claude.com/docs/en/routines](https://code.claude.com/docs/en/routines) --- triggers (schedule / API / GitHub event), quotas (Pro 5/day, Max 15/day, Team/Enterprise 25/day), cloud-side execution semantics.
- **Anthropic.** "Introducing Claude Opus 4.7" (April 16, 2026). [https://www.anthropic.com/news/claude-opus-4-7](https://www.anthropic.com/news/claude-opus-4-7)
- **Anthropic.** "What's new in Claude Opus 4.7" (API documentation). [https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-7](https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-7) --- task budgets (`anthropic-beta: task-budgets-2026-03-13`, advisory, 20K minimum), adaptive-only thinking, removal of `temperature` / `top_p` / `top_k`.
- **Caylent.** "Claude Opus 4.7 Deep Dive: Capabilities, Migration, and the New Economics of Long-Running Agents" (April 2026). [https://caylent.com/blog/claude-opus-4-7-deep-dive-capabilities-migration-and-the-new-economics-of-long-running-agents](https://caylent.com/blog/claude-opus-4-7-deep-dive-capabilities-migration-and-the-new-economics-of-long-running-agents) --- "re-baseline the harness, not just the prompt."
- **Archon GitHub Repository.** [https://github.com/coleam00/Archon](https://github.com/coleam00/Archon) --- TypeScript / Bun harness builder, YAML DAG workflows wrapping Claude Code and OpenAI Codex CLI; v2.1 shipped April 2026.
- **OpenHarness GitHub Repository.** [https://github.com/HKUDS/OpenHarness](https://github.com/HKUDS/OpenHarness) --- Python reference implementation from Hong Kong University Data lab; first commit April 1, 2026.

### 초심자를 위한 더 읽을거리

- **Cab.** "A Layer-by-Layer Walk Through Harness Engineering." 번체중문 에세이, 2026. 단일 `POST /v1/messages` 호출에서 시작하여 prompt engineering, 함수 호출, 에이전트 루프, 그리고 마지막으로 완전한 harness 복잡도까지 쌓아 올린다. 주목할 만한 것은 "模型從來都沒有長手" 비유 ——도구 사용을 모델 능력이 아니라 harness 문제로 다시 짠다 —— 와, Claude Code의 harness가 실제로 무대 뒤에서 무엇을 하는지를 명시적으로 걸어 본다는 점. 본 장의 이론 우선 프레이밍 (Böckeler 분류법, IMPACT, Meta-Harness)을 읽기 전 부드러운 진입로로 추천된다.
- **Anthropic.** ["Building Effective Agents"](https://www.anthropic.com/research/building-effective-agents) ——연구 배경이 아닌 독자에게 정전판 단형식 입문. 위의 Cab 에세이와 잘 짝을 이룬다: Cab이 쌓아 올림을 주고, Anthropic이 구체적 패턴을 준다.
