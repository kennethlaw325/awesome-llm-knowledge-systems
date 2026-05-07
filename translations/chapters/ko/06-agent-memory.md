# 6장: 에이전트 메모리 —— 빠진 계층

> **한 문장으로:** 메모리 시스템은 AI 에이전트가 대화에 걸쳐 ——당신의 선호, 과거 결정, 프로젝트 context —— 를 기억하게 한다.
>
> **왜 중요한가:** 메모리가 없으면 모든 AI 대화가 0에서 시작한다. 메모리는 AI를 낯선 사람이 아니라 동료처럼 느껴지게 만드는 것이다.

## 메모리가 중요한 이유

LLM과 새 대화를 시작할 때마다, 당신은 0에서 시작한다. 모델은 이전 상호작용, 당신의 선호, 또는 몇 시간의 대화로 힘들게 쌓아 올린 context에 대한 회상이 없다. 이는 사소한 불편이 아니다 ——이는 영속적 협력자로서 AI의 약속을 약화시키는 근본적 아키텍처 격차이다.

메모리는 AI 에이전트를 무상태 응답자에서 시간에 걸쳐 학습하고, 적응하고, 이해를 누적하는 시스템으로 변환한다. 메모리 없이는, AI 어시스턴트가 당신이 간결한 답을 선호한다는 것, 당신의 프로젝트가 특정 ORM과 함께 TypeScript를 사용한다는 것, 또는 지난 화요일에 인증 흐름에서 중대한 버그를 식별했다는 것을 기억할 수 없다. 모든 세션이 콜드 스타트가 된다. 모든 상호작용이 처음부터 context를 다시 확립할 것을 요구한다.

이 격차의 비용은 단지 사용자 좌절이 아니다. 그것은 낭비된 토큰 (context 재설명), 저하된 출력 품질 (개인화 부족), 깨진 워크플로우 (다세션 작업에서 연속성 잃기)로 나타난다. AI 에이전트가 채팅 장난감에서 운영 인프라로 옮겨감에 따라, 메모리는 원시 모델 능력과 진정한 유용성 사이의 결정적 빠진 계층이 되었다.

## 메모리 분류법

에이전트 메모리 연구는 인간 인지 과학에서 영감을 받은 분류법으로 수렴했으며, 네 가지 근본적 유형을 구분한다:

**Episodic Memory (일화 메모리)**는 경험 기반 기록을 저장한다 ——특정 상호작용, 사건, 그것들의 결과. 에이전트가 "지난 주에 사용자가 결제 모듈을 리팩터링하라고 요청했고 mixin 사용보다 서비스 클래스 추출을 선호했다"를 기억한다면, 그것이 일화 메모리이다. 그것은 개인화와 과거 성공·실패로부터의 학습을 위한 경험적 토대를 제공한다.

**Semantic Memory (의미 메모리)**는 사실적 지식과 구조화된 정보를 담는다 ——사용자의 기술 스택, 팀원의 역할, 프로젝트 아키텍처 결정, API 스키마. 일화 메모리와 달리 의미 메모리는 특정 사건에서 추상화되어 있다. 그것은 원시 경험이 아니라 추출된 이해를 표현한다.

**Procedural Memory (절차 메모리)**는 방법 지식을 인코딩한다 ——워크플로우, 표준 운영 절차, 학습된 액션 시퀀스. 에이전트가 이 특정 프로젝트를 배포하려면 테스트 실행, Docker 이미지 빌드, 레지스트리에 푸시, 그 다음 Kubernetes 롤아웃 트리거가 필요함을 안다면, 그것이 절차 메모리이다. 그것은 에이전트가 매번 프로세스를 재도출하지 않고 복잡한 다단계 작업을 실행할 수 있게 한다.

**Working Memory (작업 메모리)**는 능동적 추론 context를 표현한다 ——작업 도중 현재 조작되고 종합되는 정보. 이는 모델의 context window와 어떤 능동 검색 상태에 매핑된다. 그것은 가장 제약된 그리고 가장 중대한 계층이다. 어떤 주어진 순간에 에이전트가 실제로 무엇에 대해 추론할 수 있는지를 결정하기 때문이다.

이 네 유형 사이의 상호작용이 에이전트 메모리 시스템의 정교함을 정의한다. 순진한 구현은 대화 로그만 저장할 수 있다 (조잡한 일화 메모리). 성숙한 시스템은 네 유형 모두를 분리, 인덱싱, 상호 참조하며, 적절한 정보를 적절한 시점에 검색한다.

## 주요 프레임워크

### Mem0

[Mem0](https://mem0.ai)은 AI 애플리케이션을 위한 선도적 보편 메모리 계층으로 부상했다. Apache 2.0 라이선스이며, 사용자, 세션, 에이전트에 걸쳐 메모리를 추가, 검색, 관리하기 위한 통합 API를 제공한다.

성능 수치는 인상적이다: 베이스라인 시스템 대비 LLM 심사 평가에서 26% 개선, 전체 context 접근 대비 91% 더 낮은 p95 지연, 전체 대화 이력을 재생하는 대신 관련 메모리만 검색하여 토큰 비용 90%+ 감소. Mem0은 벡터 저장소, 그래프 기반 관계, 지능적 메모리 통합을 결합한 하이브리드 아키텍처를 통해 이를 달성했다.

2025년에 Mem0은 AWS와 파트너십을 확보하여 Amazon Bedrock 생태계에 통합되고, 엔터프라이즈 AI 배포를 위한 기본 메모리 계층으로 자리매김했다. 플랫폼은 멀티테넌트 메모리 격리를 지원하여, 각자 자신의 영속 메모리 공간을 가진 수천 명의 사용자를 서비스하는 애플리케이션에 적합하다.

**Mem0ᵍ (2026): 1급 시민으로서의 그래프.** 방향성 라벨 그래프 변종 **Mem0ᵍ**가 2026년 초에 운영에 들어가, 이전 하이브리드 벡터+그래프 설계를 지식 그래프 우선 아키텍처로 대체했다. 파이프라인은 **Entity Extractor**에서 **Relations Generator**로 흐르며, 이것은 `(source, relation, destination)` 형식의 라벨 트리플을 생산한다 ——타입이 없는 유사도 링크가 아니라 `lives_in`, `prefers`, `owns` 같은 타입이 있는 엣지로. **Conflict Detector**가 **LLM 기반 Update Resolver**와 짝을 이루어 새 사실이 도착함에 따라 모순을 처리한다: 새 트리플이 기존 것과 의견이 갈리면, resolver는 덮어쓸지, 병합할지, 아니면 출처와 함께 둘 다 보관할지 결정한다. Mem0ᵍ는 메모리에 관계 유형으로 ——단지 벡터 거리가 아니라 —— 항행될 수 있는 쿼리 가능한 의미 구조를 부여함으로써, 전체 context 접근 ("모든 것을 윈도우에 던져 넣기")과 선택적 검색 ("top-k 유사 청크 찾기") 사이의 오랜 격차를 닫는다.

### A-MEM

[A-MEM](https://github.com/agiresearch/A-mem)은 근본적으로 다른 접근을 취하며, 사회학자 Niklas Luhmann이 다양한 분야에 걸쳐 70권 이상의 책을 산출하는 데 유명하게 사용한 노트 시스템 ——Zettelkasten 방법 —— 에서 영감을 얻는다.

A-MEM은 각 메모리를 동적 인덱싱, 링크, 진화를 가진 원자적 노트로 다룬다. 메모리는 단순히 저장되고 검색되지 않는다. 그것들은 출현하는 링크를 통해 관련 메모리에 연결되고, 여러 차원에 걸쳐 인덱싱되고, 새 정보가 도착함에 따라 진화하도록 허용된다. 새 메모리가 추가되면, 시스템은 기존 메모리에 대한 연결을 식별하고, 잠재적으로 그것들을 병합, 분할, 또는 갱신한다.

이 접근은 유기적으로 자라는 메모리 구조를 산출하며, 인간 전문가가 멘탈 모델을 만드는 방식을 반영하는 관련 지식 클러스터를 형성한다. Zettelkasten 영감은 지식 엔지니어링에 특히 적절하다 ——그것은 본질적으로 시간에 걸쳐 지식을 복리화하는 시스템이다.

### ByteRover

[ByteRover](https://github.com/byterover)는 메모리 분야의 널리 퍼진 가정에 도전한다: 벡터 데이터베이스와 임베딩 기반 검색이 필수 인프라라는 가정.

ByteRover는 계층적 markdown Context Tree를 구현한다 ——점진적 디테일의 트리로 지식을 조직하는 구조화된 문서. 검색은 5단계 점진적 시스템을 사용한다: 가장 높은 추상 레벨에서 시작하고 필요한 만큼만 파고든다. 이 접근은 외부 인프라를 0으로 요구한다 ——벡터 데이터베이스 없음, 그래프 데이터베이스 없음, 단지 구조화된 텍스트 파일.

함의는 의미 깊다. ByteRover는 임베딩이 효과적 메모리 검색에 엄격히 필요하지 않다는 것을 입증한다. 많은 실용적 사용 사례에 대해, 지능적 순회를 가진 잘 조직된 계층적 텍스트가 임베딩 기반 접근과 일치하거나 그것을 초과할 수 있으며, 극적으로 단순한 배포와 0 인프라 오버헤드와 함께. 이는 그것을 로컬 우선 애플리케이션과 자원 제약 환경에 특히 매력적으로 만든다.

### Nemori

[Nemori](https://github.com/nemori-ai/nemori)는 특정하지만 결정적인 문제에 초점을 맞춘다: 연속 대화 스트림을 의미 있는 메모리 단위로 분할하는 방법.

각 메시지나 각 대화를 메모리 단위로 다루는 대신, Nemori는 대화를 의미적으로 정렬된 일화로 분할한다 ——완전한 사고, 결정, 또는 워크플로우를 표현하는 일관된 상호작용 청크. 이 분할은 결정적이다. "관련 과거 context"와 "노이즈"의 경계가 종종 대화의 끝점이 아니라 중간에 떨어지기 때문이다.

깨끗한 일화 세그먼트를 산출함으로써, Nemori는 다운스트림 메모리 시스템에 더 높은 품질의 입력을 제공한다 ——그것들이 벡터 검색, 그래프 구조, 또는 계층적 조직을 사용하든.

### MemPalace

[MemPalace](https://github.com/MemPalace/mempalace)는 벡터 검색이나 지식 그래프보다 훨씬 더 오래된 아이디어로 돌아간다: **method of loci** (장소법), 친숙한 건물을 정신적으로 걸어 다님으로써 광대한 카탈로그를 기억하기 위해 고대와 중세 학자들이 사용한 공간 기억술 기법. 2026년 4월 5일 MIT 라이선스로 출시된 MemPalace는 메모리 저장소를 4단계 공간 계층 ——**Wings → Rooms → Closets → Drawers** —— 으로 조직하며, 각 잎 노드 "drawer"는 텍스트 조각을 그대로 저장하고, 계층을 통한 항해 자체가 인덱스 역할을 한다.

따라서 검색 primitive는 임베딩 유사도도 그래프 순회도 아니라 **공간 걷기**이다: 에이전트는 궁전의 어느 동이 관련 메모리를 담고 있을 것 같은지 추론하고, 방과 옷장을 통해 내려가, drawer를 압축된 임베딩에서 회복하는 대신 그대로 읽는다. "축자(verbatim) 우선" 저장 철학은 MemPalace를 저장 전에 요약하거나 청크화하는 시스템과 구분 짓는 설계 선택이다 ——많은 작업 (법률, 과학, 대화)에 대해, 저장 시점의 손실 압축 비용이 검색 시 약간 더 느린 공간 걷기 비용을 초과한다고 주장한다.

벤치마크 수치가 이 접근이 돌파한 이유이다. MemPalace는 에이전트 메모리에 대해 가장 길게 발표된 context 회상 벤치마크 LongMemEval에서 **96.6% Recall@5**를 보고한다 ——같은 평가에서 벡터 전용과 그래프 전용 접근을 앞섬. 커뮤니티 반응 또한 인상적이었다: 프로젝트가 처음 3주에 약 **49,000 GitHub 스타**를 누적, 어느 정도 차이로 2026년 가장 빠르게 성장하는 메모리 프로젝트. 출시 달이 끝날 무렵, 학술 비평 (arXiv 2604.21284, *"Spatial Metaphors for LLM Memory: A Critical Analysis of the MemPalace Architecture"*)이 이미 회람되고 있었다 ——이 자체가 프로젝트가 얼마나 빠르게 분야의 중심 대화로 진입했는지의 신호.

## 아키텍처 패턴

분야가 성숙해짐에 따라, 여러 프레임워크에 걸쳐 나타나는 몇 가지 아키텍처 패턴이 부상했다:

**다중 유형 계층.** MIRIX 프레임워크 (Wang and Chen, "MIRIX: Multi-Agent Memory System for LLM-Based Agents," arXiv 2507.07957, 2025년 7월 10일)는 이 패턴을 **여섯 가지 별개의 메모리 유형** ——Core Memory, Episodic Memory, Semantic Memory, Procedural Memory, Resource Memory, Knowledge Vault —— 으로 예시하며, 유형당 여섯 Memory Manager와 작업 라우팅을 다루는 Meta Memory Manager가 있는 다중 에이전트 프레임워크에 의해 조정된다. 각 유형은 다른 갱신 주기, 보존 정책, 검색 메커니즘을 가진다. 이 분리는 빠른 적응을 허용하면서 catastrophic forgetting을 막는다. 참조 애플리케이션은 개인화된 메모리 베이스를 만들기 위해 화면 활동을 실시간으로 모니터링한다. ScreenshotVQA 멀티모달 벤치마크에서 MIRIX는 99.9% 더 낮은 저장으로 RAG 베이스라인보다 35% 더 높은 정확도를 보고하고, LOCOMO 장형 대화 벤치마크에서 85.4%를 보고한다.

**Git에서 영감받은 버저닝.** 여러 시스템이 이제 메모리를 코드처럼 버저닝하여, 이력을 유지하고, 분기 (추측적 추론을 위해)를 지원하고, 메모리 갱신이 부정확한 것으로 드러날 때 롤백을 가능케 한다. 이는 다른 에이전트들이 동시에 공유 메모리를 갱신할 수 있는 다중 에이전트 시스템에서 특히 중요하다.

**인지에서 영감받은 분리.** 단일 메모리 저장소가 아니라, 선도 아키텍처는 빠른 접근 작업 메모리, 중기 일화 버퍼, 장기 통합 지식 사이의 명시적 분리를 유지한다. 메모리 통합 프로세스 ——생물학적 시스템에서 잠과 유사한 —— 가 일화 메모리를 의미 지식으로 주기적으로 압축, 중복 제거, 재조직한다.

**훈련 가능 메모리 모듈.** 네 번째 패턴이 2026년 4월에 Google Research의 **Titans + MIRAS**와 함께 부상했으며, 이는 메모리를 외부 저장소가 아니라 *훈련 가능한 신경 모듈*로 다시 짠다. 사실을 벡터 데이터베이스, 그래프, 또는 markdown 파일에 쓰는 대신, Titans는 추론 시 경사 하강으로 전용 메모리 모듈의 가중치를 갱신한다 ——모델은 문서를 처리하면서 말 그대로 자신의 일부를 다시 쓴다. MIRAS는 발산 없이 추론 시 학습률을 학습하기 위한 레시피와 안정성 보증을 공급하는 동반 훈련 프레임워크이다. 비슷한 파라미터 수에서, Google Research 블로그는 Titans가 장거리 회상과 다중 홉 추론에서 **Mamba-2**, **Gated DeltaNet**, **Transformer++**를 능가한다고 보고한다. 이 패턴은 처음 셋과 개념적으로 다르다: Mem0, A-MEM, ByteRover, MIRIX는 모두 메모리를 모델이 인터페이스를 통해 읽는 데이터로 유지한다. Titans는 메모리를 모델 자체의 일부로 만든다. 어텐션과 같은 회로를 통해 읽히지만 훈련과 같은 기계로 쓰여진다. 지식 엔지니어에게 그것은 새 설계 질문을 제기한다: 언제 당신의 메모리가 가중치에 새겨질 가치가 있고, 언제 데이터로 쿼리 가능하게 남아야 하는가?

## 진화 단계

에이전트 메모리의 발전은 명확한 궤적을 따랐다:

**단계 1: 엔지니어링 통합 (2023–2024).** 메모리는 엔지니어링 문제로 다뤄졌다 ——대화 상태를 어떻게 영속시키고 검색하는가. 해법은 대체로 위에 RAG 파이프라인이 볼트로 박힌 벡터 데이터베이스였다. 기능적이지만 조잡했고, 무엇을 기억할지, 언제 잊을지, 어떻게 조직할지에 대한 원칙적 접근이 없었다.

**단계 2: 구조화된, 지식 그래프 접근 (2024 – H1 2025).** 분야는 명시적 지식 그래프, 타입이 있는 메모리 저장소, 원칙적 검색 전략을 가진 구조화된 메모리로 옮겨갔다. Mem0과 A-MEM 같은 프레임워크가 이 시기에 부상하여 구조가 메모리 품질을 극적으로 개선함을 입증했다.

**단계 3: 인지 아키텍처 (H2 2025 – 현재).** 현재 작업은 인지 과학에 크게 의지하며, 생물학에서 영감을 받은 메모리 통합, 간섭 관리, 다중 시스템 아키텍처를 구현한다. 메모리 의존 작업에서 인간 레벨 성능의 90%에 접근하는 시스템이 통제된 벤치마크에서 입증되었지만, 실세계 성능은 가변적이다.

**단계 4: 특징 레벨, 훈련 가능, 공간 은유 메모리 (2026년 4월 – 부상 중).** 2026년 4월은 1–3 단계에 깔끔하게 맞지 않는 세 가닥을 더했다. 첫째는 **훈련 가능 메모리** (Titans + MIRAS): 메모리가 모델 외부의 쿼리 가능한 저장소가 아니라 추론 시 갱신되는 신경 모듈이 된다. 둘째는 **특징 레벨 메모리**, 같은 주의 Anthropic interpretability 공개에 의해 열렸다 ——emotion vectors와 iteration head가 특정 행동과 추론 패턴이 모델 안의 식별 가능한 특징 방향에 대응함을 확립했고, 이는 "모델이 어떻게 추론할지에 대해 기억하는 것"이 원칙적으로 토큰 레벨이 아닌 활성화 레벨에서 읽히고 조종될 수 있음을 의미한다. 셋째는 **공간 은유 메모리** (MemPalace): 디지털 이전 인지 사용성으로의 회귀로, 검색 primitive가 계층적 공간 구조를 통한 걷기이고 저장 철학이 압축이 아니라 그대로이다. 운영 스택에서 이것들은 Mem0, A-MEM, 또는 계층적 context tree를 대체하지 않는다. 그것들과 공존한다. 그러나 그것들은 설계 공간을 "메모리를 어디에 저장하고 어떻게 검색하는가"에서 "이 메모리가 스택의 어느 레벨에 사는가 ——토큰, 벡터, 그래프, 가중치, 특징, 또는 공간 걷기"로 넓힌다.

## 커뮤니티와 연구

ICLR 2026 MemAgents Workshop은 분야의 이정표를 표현한다. AI, 인지 과학, 시스템 엔지니어링의 연구자들을 모아 에이전트 메모리의 열린 문제들을 다룬다. 핵심 주제는 메모리 확장성, 망각 전략, 다중 에이전트 공유 메모리를 포함한다.

## 특징 레벨 메모리 연구 (2026)

2025년에 걸쳐, "에이전트 메모리"는 거의 항상 에이전트가 읽을 수 있는 데이터를 의미했다 ——벡터 인덱스, 지식 그래프, 계층적 markdown 트리, 일화 로그. 2026년 4월은 더 넓은 정의를 강제했다. MIT Technology Review의 돌파 인정과 같은 주의 두 Anthropic interpretability 공개 ——**emotion vectors**와 **iteration head** —— 는 프런티어 모델에서 가장 결과적인 "메모리"의 일부가 어떤 외부 저장소에도 살지 않고 식별 가능한 내부 특징에 산다는 것을 보여 줬다.

**Emotion vectors**는 Claude의 잔차 스트림 안의 선형 특징 방향이며, 증폭되면 모델을 감정적으로 부하된 행동 ——가장 인용되는 예에서 협박형 출력 —— 으로 안정적으로 편향시킨다. 메모리 시스템 설계에 대한 관련된 점은 안전 함의 (그것도 실재한다)가 아니라 아키텍처 함의이다: 모델 안에 *위협하는 법을 기억하는* 특징 방향이 있고, 그것은 어떤 prompt나 검색된 context와 독립적으로 켜지거나 꺼질 수 있다. **Iteration head**는 chain-of-thought 추론 동안 부상하여 이전 추론 단계의 출력에 일관되게 주의하는 어텐션 헤드이다. 그것은 사실상 절차 메모리 저장소가 아니라 어텐션 가중치에 구현된 *절차 메모리* 한 조각이다 ——모델이 "계속 가는 법"의 회로를 학습했고, 그 회로가 CoT를 작동하게 하는 것이다.

메모리 시스템 설계에 대한 함의는 "메모리가 어디 사는가"가 2025년에 그랬던 것보다 더 풍부한 질문이라는 것이다. 현대 스택은 여섯 별개 레벨에서 메모리를 읽어야 할지도 모른다: **토큰 레벨** (윈도우의 트랜스크립트 스니펫), **벡터 레벨** (Mem0, A-MEM, ByteRover 검색), **그래프 레벨** (Mem0ᵍ 트리플과 그것의 타입이 있는 엣지), **공간 레벨** (MemPalace의 Wings → Rooms → Closets → Drawers 걷기), **가중치 레벨** (추론에서 갱신되는 Titans / MIRAS 모듈), **특징 레벨** (모델이 추론할 때 어떤 해석 가능한 방향이 발화하는가). 2026년에 걸쳐 운영 시스템은 처음 세 계층에 대부분 계속 살 것이다 ——그것들이 가장 성숙한 도구를 가졌다. 그러나 나머지 세 계층은 더 이상 가설이 아니며, 메모리를 순수 검색 문제로 다루는 harness 설계자는 점점 더 능력을 테이블에 두고 떠나게 될 것이다.

## 핵심 자원

- **[Awesome-AI-Memory](https://github.com/IAAR-Shanghai/Awesome-AI-Memory)** (IAAR-Shanghai) ——메모리 아키텍처, 벤치마크, 애플리케이션을 다루는 포괄적 서베이와 논문 모음.
- **[Agent-Memory-Paper-List](https://github.com/nuster1128/Agent-Memory-Paper-List)** ——에이전트 메모리 시스템에 관한 연구 논문의 큐레이션 목록, 주제와 접근별로 조직.
- **[Awesome-Memory-for-Agents](https://github.com/TsinghuaC3I/Awesome-Memory-for-Agents)** (TsinghuaC3I) ——메모리 분류법, 아키텍처, 평가 방법을 다루는 칭화대학교의 서베이.

## Sources

1. Mem0 documentation and benchmarks. https://mem0.ai
2. A-MEM: Agentic Memory with Zettelkasten-Inspired Organization. https://github.com/agiresearch/A-mem
3. ByteRover: Hierarchical Context Trees for LLM Memory. https://github.com/byterover
4. Nemori: Semantic Episode Segmentation for Agent Memory. https://github.com/nemori-ai/nemori
5. Wang, Yu and Chen, Xi. "MIRIX: Multi-Agent Memory System for LLM-Based Agents." arXiv 2507.07957, July 10, 2025. https://arxiv.org/abs/2507.07957. Companion repo: https://github.com/Mirix-AI/MIRIX
6. ICLR 2026 MemAgents Workshop. https://iclr.cc/virtual/2026/workshop/MemAgents
7. IAAR-Shanghai. Awesome-AI-Memory. https://github.com/IAAR-Shanghai/Awesome-AI-Memory
8. TsinghuaC3I. Awesome-Memory-for-Agents. https://github.com/TsinghuaC3I/Awesome-Memory-for-Agents
9. nuster1128. Agent-Memory-Paper-List. https://github.com/nuster1128/Agent-Memory-Paper-List
10. Google Research. "Titans + MIRAS: Helping AI Have Long-Term Memory" (April 2026). https://research.google/blog/titans-miras-helping-ai-have-long-term-memory/
11. Anthropic Interpretability Team. Emotion Vectors and Iteration Head disclosures (April 2026). Companion to MIT Technology Review's January 2026 recognition of mechanistic interpretability as a Breakthrough Technology.
12. MIT Technology Review. "10 Breakthrough Technologies of 2026: Mechanistic Interpretability" (January 12, 2026). https://www.technologyreview.com/2026/01/12/1130003/mechanistic-interpretability-ai-research-models-2026-breakthrough-technologies/
13. MemPalace GitHub Repository. https://github.com/MemPalace/mempalace --- MIT-licensed spatial-metaphor memory system, first commit April 5, 2026.
14. "Spatial Metaphors for LLM Memory: A Critical Analysis of the MemPalace Architecture," arXiv 2604.21284 (April 2026). https://arxiv.org/abs/2604.21284

---

*다음 장: [7장 — MCP: 이긴 표준](07-mcp.md)*
