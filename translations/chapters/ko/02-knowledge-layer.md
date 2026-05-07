# 2장: RAG, Long Context와 지식 그래프

> **한 문장으로:** AI에게 지식 접근을 부여하는 세 가지 주된 방법: 데이터베이스를 검색하기 (RAG), 긴 문서를 먹이기, 또는 사실을 그래프로 연결하기.
>
> **왜 중요한가:** 자기 데이터를 다루는 어떤 일에든 AI를 쓰고 있다면, 본 장은 당신의 상황에 어떤 접근이 가장 잘 맞는지 설명한다.

**지식 검색 계층 ——무엇이 작동하고, 무엇이 작동하지 않으며, 답이 거의 항상 "하이브리드"인 이유.**

---

## RAG는 죽지 않았다

여섯 달마다 누군가 "RAG는 죽었다, Long Context면 충분하다"를 발표한다. 여섯 달마다 기업들은 그들이 틀렸음을 입증한다.

**Gartner의 2025년 4분기 엔터프라이즈 설문조사**에서, RAG 파이프라인을 순수 context-stuffing (전체 문서 코퍼스를 큰 context window에 먹이기)로 대체하려 한 조직 중 71%가 12개월 안에 RAG를 다시 추가했다. 이유는 일관됐다: 비용, 지연, 스케일에서의 정확도 저하, 그리고 동적이거나 자주 갱신되는 지식 베이스를 다루지 못하는 한계.

RAG는 죽지 않았다. 진화하고 있다. 질문은 결코 "RAG냐 아니냐"가 아니었다 ——"어떤 종류의 RAG, 무엇과 결합하느냐"였다.

---

## 비용의 현실

RAG에 대한 경제적 논거는 여전히 압도적이다.

전형적인 RAG 파이프라인은 5–20개의 관련 청크 (대략 2,000–8,000 토큰)를 검색해 모델 호출에 먹인다. 같은 쿼리에 대해 context-stuffing 접근은 500K–1M 토큰의 출처 문서를 로드해야 할 수 있다.

**쿼리당 비용 비교 (대략, 2026년 중반 가격):**

| 접근 | 입력 토큰 | 대략적 비용 | 상대 비용 |
|------|---------|-----------|---------|
| RAG (타깃 검색) | ~5,000 | ~$0.00008 | 1x |
| Context-stuffing (전체 코퍼스) | ~500,000 | ~$0.10 | 1,250x |

이는 반올림 오차가 아니다. 엔터프라이즈 스케일 ——월 수백만 건의 쿼리 —— 에서는 월 추론 비용 $80과 $100,000의 차이가 프로젝트가 예산 검토를 통과하는지를 결정한다.

비용 격차는 모델 가격이 떨어지면서 좁아지지만, 검색은 항상 전체 지식 베이스를 모든 호출에 무차별 투입하는 것보다 저렴할 것이다. 정보 이론의 법칙이 이를 보장한다: 관련 정보를 선택하는 것이 모든 정보를 처리하는 것보다 저렴하다.

---

## Long Context: 작동할 때, 작동하지 않을 때

긴 context window (128K, 200K, 1M+ 토큰)는 특정 사용 사례에 진정으로 변혁적이다:

**Long context가 빛나는 곳:**
- **정적이고 경계가 분명한 문서 분석**: 단일 계약서, 코드베이스 파일, 또는 연구 논문 ——전체 관련 코퍼스가 윈도우에 들어가는 경우 —— 의 분석
- **상호 참조 작업**: 한 번에 로드된 고정된 문서 집합에 걸쳐 연결을 찾기
- **요약**: 크지만 유한한 입력을 구조화된 출력으로 응축

**Long context가 무너지는 곳:**

**"Lost in the middle" 저하.** [Liu et al. (2023)](https://arxiv.org/abs/2307.03172)의 연구는 LLM이 긴 context의 시작이나 끝에 놓인 정보에 비해 중간에 놓인 정보에서 현저히 더 나쁘게 수행한다는 것을 입증했다. 이후의 모델 개선이 이 효과를 줄였지만 제거하지는 못했다. 2026년 초 기준, 모델은 관련 정보가 500K+ 토큰의 context 안에 묻혀 있을 때 여전히 측정 가능한 정확도 저하를 보인다.

**동적 지식 베이스.** 지식 베이스가 매 시간 갱신된다면 (제품 재고, 지원 티켓, 뉴스 피드), 전체 코퍼스를 모든 context window에 다시 임베딩할 수 없다. RAG의 검색 단계는 갱신을 자연스럽게 처리한다 ——새 문서가 인덱싱되어 prompt 구조를 바꾸지 않고 즉시 검색 가능하다.

**멀티테넌트 격리.** Long context 접근은 접근 제어에서 어려움을 겪는다. 여러 사용자나 권한 레벨의 문서가 같은 코퍼스에 존재할 때, RAG 파이프라인은 검색 시점 필터링을 강제할 수 있다. Context-stuffing은 신중한 (그리고 오류가 발생하기 쉬운) 문서 분리를 요구한다.

**스케일에서의 지연.** 1M 토큰을 처리하는 것은 5K 토큰을 처리하는 것보다, 최적화된 추론으로도, 의미 있게 더 오래 걸린다. 1초 미만의 응답 시간이 중요한 사용자 대면 애플리케이션에서는 타깃 검색이 이긴다.

### 2026년 갱신: Titans + MIRAS가 Long-Context 트레이드오프를 다시 짠다

위의 모든 한계는 Transformer 스타일의 context window를 가정한다: 어텐션이 읽는 토큰의 평면 스팬, 위치에 무관한 동일한 토큰당 비용, 그리고 동일한 "lost in the middle" 실패 모드. **Titans + MIRAS**, Google Research의 2026년 4월 아키텍처 군은 그 가정을 깬다. Titans에서 메모리는 어텐션 윈도우가 아니다 ——추론 도중 경사 하강으로 자신의 가중치를 갱신하는 **훈련 가능한 신경 모듈**이다. 그래서 모델은 긴 이력을 토큰으로 앞으로 운반하는 것이 아니라 말 그대로 가중치 갱신으로 압축한다. MIRAS는 이 추론하면서 학습하는 과정을 안정적으로 유지하는 훈련 레시피를 제공한다. 비슷한 파라미터 수에서, Google은 Titans가 장거리 회상과 다중 홉 추론에서 Mamba-2, Gated DeltaNet, Transformer++을 능가한다고 보고한다. 이 중 어느 것도 원래의 long-context 한계를 반박하지 않는다 ——그것들은 GPT-4 Turbo, Gemini 1.5, Claude가 계속 사용하는 어텐션 윈도우 패러다임에 여전히 적용된다 —— 그러나 **"어텐션 예산은 희소하다"는 프레이밍이 이제 보편 제약이 아니라 한 아키텍처 군의 속성**임을 확립한다. 실무자에게 이는 long-context 트레이드오프가 더 이상 단일 곡선이 아님을 의미한다. 이제 적어도 두 개가 있다: 어텐션 윈도우 곡선 (lost-in-the-middle과 토큰당 비용이 지배하는 곳)과 훈련 가능한 메모리 곡선 (비용이 추론 시 가중치 갱신으로 옮겨가고 실패 모드가 안정성과 망각으로 옮겨가는 곳). RAG는 양쪽 모두에 강력한 기본값으로 남지만, RAG가 *이기는 이유*는 각 체제에서 다르다.

---

## GraphRAG: 평면 검색으로 충분하지 않을 때

표준 RAG는 문서를 독립적인 청크로 다룬다. 이는 사실 조회 ("반품 정책이 무엇인가?")에는 작동하지만, *관계 추론*을 요구하는 질문 ("우리의 지연된 배송과 품질 불만 모두에 연결된 공급업체는 누구인가?")에는 실패한다.

[Microsoft의 GraphRAG](https://github.com/microsoft/graphrag) (2024–2025)는 하이브리드 접근을 도입했다: 출처 문서로부터 지식 그래프를 구축한 다음, 쿼리에 답하기 위해 벡터 검색과 함께 그래프 순회를 사용한다.

### GraphRAG가 작동하는 방식

1. **인덱싱 단계**: 문서를 처리하여 엔티티 (사람, 조직, 개념)와 그들 사이의 관계를 추출한다. 이들은 전통적 벡터 임베딩과 함께 그래프 구조를 형성한다.
2. **커뮤니티 탐지**: 그래프는 조밀하게 연결된 엔티티들의 커뮤니티로 분할된다. 각 커뮤니티는 요약 설명을 받는다.
3. **쿼리 단계**: 주어진 쿼리에 대해, 관련 context를 검색하기 위해 벡터 유사도 *그리고* 그래프 순회 모두가 사용된다. 엔티티 관계는 평면 검색이 놓치는 다중 홉 추론 경로를 제공한다.

### GraphRAG가 중요한 경우

- **다중 홉 쿼리**: "2025년에 상장한 회사들과 인수된 회사들 사이의 공통 투자자는 누구인가?" ——관계 사슬을 순회해야 한다
- **엔티티 중심 추론**: 특정 엔티티와 다른 엔티티에 대한 그들의 연결에 관한 질문
- **전역 요약**: "우리 모든 고객 피드백에 걸친 주요 주제는 무엇인가?" ——커뮤니티 요약은 모든 문서를 처리하지 않고 이를 제공한다

### GraphRAG가 과한 경우

- 단순 사실 조회 (표준 RAG가 이를 잘 처리한다)
- Long context가 모든 것을 담을 수 있는 작은 코퍼스
- 엔티티 추출 품질이 낮은 사용 사례 (쓰레기 in, 쓰레기 out)

GraphRAG의 인덱싱 비용은 표준 RAG보다 현저히 높다. 관계 추론이 핵심 요구사항인 경우에만 그래프를 구축하라. 기본값으로는 아니다.

### 2026년 진화: Long Context를 위한 의미 백본으로서의 KG

2024년과 2025년 대부분 동안, GraphRAG는 **RAG의 대안** ——제한된 context window를 가진 모델을 위해 청크를 검색하는 다른 방법 —— 으로 프레이밍되었다. 2026년에 이르러 그 프레이밍은 변했다. 프런티어 모델이 context window를 수백만 토큰 범위로 밀어올리면서 (Gemini 1.5 1M, Kimi가 200만 한자를 넘어, 추가 확장이 진행 중), 질문은 더 이상 "어떻게 적은 수의 관련 청크를 검색하는가"가 아니라 "필요한 대부분을 이미 담을 만큼 충분히 큰 context를 어떻게 항행하는가"이다.

그 세계에서, 지식 그래프는 **검색 대체물**이기를 그치고 **long context를 위한 구조화된 인덱스 계층**이 된다. 그래프는 어떤 청크를 로드할지 결정하기 위해 거기 있는 것이 아니다 ——청크는 이미 윈도우 안에 있다. 그래프는 모델에게 윈도우 안에 무엇이 있는지의 의미 지도를 주기 위해 거기 있다: 어떤 엔티티가 존재하는지, 그들이 어떻게 관련되어 있는지, 어떤 섹션이 어떤 주제에 대응하는지, 모순이 어디 사는지, 어떤 다중 홉 경로가 질문을 관련 증거로 연결하는지. GraphRAG는 자신이 태어난 8K 토큰 윈도우의 우회책이 아니라, 에이전트가 100만 토큰 윈도우를 효율적으로 걸을 수 있게 하는 **의미 백본**으로 다시 부상한다. 2026년 4월의 훈련 가능 메모리 모듈 도래 (Titans + MIRAS)는 이 역할을 밀어내지 않는다 ——초기 증거는 지식 그래프와 훈련 가능 메모리가 운영 스택에서 **공존하고 함께 구성될 가능성이 높다**는 것이다. 그래프가 훈련 가능 모듈이 이미 가중치로 압축한 것 위에 타입이 있는 쿼리 가능한 구조를 제공한다.

---

## 2025-2026 RAG 기법 풍경

RAG 자체가 여러 전문화된 접근으로 분기되었다. 핵심 변종:

### Self-RAG (Asai et al., 2023)

[Self-RAG](https://arxiv.org/abs/2310.11511)는 모델을 *언제* 검색이 필요한지, *무엇을* 검색할지, 그리고 검색된 내용이 실제로 관련이 있는지를 결정하도록 훈련한다. 항상 검색하는 대신, 모델은 검색 과정을 게이트하는 특별한 "reflection 토큰"을 생성한다.

**핵심 이점**: 불필요한 검색 호출을 줄이고 무관한 검색 내용을 걸러내어, 효율성과 정확도 모두를 개선한다.

### Corrective RAG (CRAG)

[Corrective RAG](https://arxiv.org/abs/2401.15884) (Yan et al., 2024)는 검색 후 검증 단계를 추가한다. 가벼운 평가자가 검색된 문서가 쿼리와 관련이 있는지를 평가한다. 신뢰도가 낮으면 시스템이 폴백으로 웹 검색이나 대안 검색 전략을 트리거한다.

**핵심 이점**: 1차 지식 베이스가 답을 담고 있지 않을 때의 우아한 저하.

### Adaptive RAG

[Adaptive RAG](https://arxiv.org/abs/2403.14403) (Jeong et al., 2024)는 분류기를 사용해 복잡도에 따라 쿼리를 다른 검색 전략으로 라우팅한다. 단순 쿼리는 직접 검색을 받는다. 복잡한 쿼리는 chain-of-thought 추론과 함께 다단계 검색을 받는다. 모호한 쿼리는 결과 융합과 함께 여러 검색 패스를 받는다.

**핵심 이점**: 일률적 파이프라인을 사용하는 대신 검색 비용을 쿼리 복잡도에 맞춘다.

### Golden-Retriever RAG

Golden-Retriever RAG는 검색 전 LLM 자신을 사용해 쿼리를 다시 쓰는 것으로 검색 품질에 초점을 맞춘다. 모델은 "이상적 문서" 설명을 생성하고, 그것이 원시 사용자 입력 대신 검색 쿼리로 사용된다.

**핵심 이점**: 사용자가 질문하는 방식과 문서가 작성되는 방식 사이의 어휘 격차를 메운다.

---

## "Context Engine"으로서의 RAG

오픈소스 RAG 엔진 [RAGFlow](https://github.com/infiniflow/ragflow)는 2025년 말에 연말 리뷰를 발표하며, "Retrieval-Augmented Generation"이라는 용어가 더 이상 현대 RAG 시스템이 하는 일을 포착하지 못한다고 주장했다. 그들이 제안한 재프레임: RAG는 검색 기법에서 **Context Engine** ——이질적 출처로부터 모델의 context window로 관련 정보를 조립하는 범용 시스템 —— 으로 진화했다.

이 재프레임은 [1장](/chapters/01-evolution.md)에서 기술된 context engineering 진화와 정렬한다. RAG는 단지 "검색해서 채우기"가 아니다. 현대 RAG 시스템은:

- 쿼리 의도와 복잡도를 분류한다
- 적절한 검색 전략 (벡터, 키워드, 그래프, 하이브리드)으로 라우팅한다
- 결과를 재순위화하고 필터링한다
- 토큰 예산에 맞도록 검색된 내용을 압축한다
- 적절한 구조와 메타데이터로 결과를 포맷한다
- 인용과 검증을 위한 출처를 추적한다

이는 검색 단계가 아니라 context 어셈블리 파이프라인이다. RAG 시스템 *이* context engine이다.

---

## 하이브리드 아키텍처: 수렴

2025–2026의 증거는 하이브리드 접근을 분명히 가리킨다. 어떤 단일 기법도 모든 차원에서 이기지 못한다:

| 차원 | RAG | Long Context | 지식 그래프 |
|-----|-----|-------------|----------|
| 쿼리당 비용 | 낮음 | 높음 | 중간 |
| 동적 갱신 | 강함 | 약함 | 중간 |
| 관계 추론 | 약함 | 약함 | 강함 |
| 셋업 복잡도 | 중간 | 낮음 | 높음 |
| 정확도 (타깃) | 높음 | 중간 | 높음 |
| 정확도 (전역) | 중간 | 높음 | 높음 |

**운영에서 이기는 패턴:**

1. 엔티티 관계와 전역 이해를 위한 **지식 그래프**
2. 특정 쿼리에 대한 동적, 타깃 검색을 위한 **RAG**
3. 전체 문서가 중요한 경계가 분명한 분석 작업을 위한 **Long context**
4. 쿼리당 올바른 전략을 선택하는 **쿼리 라우터**

이는 이론이 아니다. 스케일의 운영 시스템 (엔터프라이즈 검색, 코딩 어시스턴트, 고객 지원 에이전트)은 셋 모두를 결합해 사용한다. 엔지니어링 과제는 하나를 고르는 것이 아니다 ——각 쿼리에 맞는 도구를 고르는 라우터를 만드는 것이다.

---

## 핵심 프로젝트와 자원

| 프로젝트 | 설명 | 링크 |
|--------|------|----|
| Microsoft GraphRAG | 지식 그래프 + RAG 하이브리드 | [github.com/microsoft/graphrag](https://github.com/microsoft/graphrag) |
| RAGFlow | 깊은 문서 이해를 갖춘 오픈소스 RAG 엔진 | [github.com/infiniflow/ragflow](https://github.com/infiniflow/ragflow) |
| NirDiamant/RAG_Techniques | RAG 구현의 포괄적 모음 | [github.com/NirDiamant/RAG_Techniques](https://github.com/NirDiamant/RAG_Techniques) |
| LangChain | 광범위한 RAG 도구를 갖춘 프레임워크 | [github.com/langchain-ai/langchain](https://github.com/langchain-ai/langchain) |
| LlamaIndex | LLM 애플리케이션을 위한 데이터 프레임워크 | [github.com/run-llama/llama_index](https://github.com/run-llama/llama_index) |
| Chroma | 오픈소스 임베딩 데이터베이스 | [github.com/chroma-core/chroma](https://github.com/chroma-core/chroma) |

---

## Sources

- Gartner. "Enterprise RAG Adoption" survey commentary, Q4 2025 --- the 71%-revert figure cited at the top of this chapter circulates across multiple industry analyses; primary access requires a Gartner subscription, so the figure is reported here as widely-cited industry stat rather than from a freely-reachable primary URL.
- Liu, N. F. et al. (2023). "Lost in the Middle: How Language Models Use Long Contexts." [arXiv:2307.03172](https://arxiv.org/abs/2307.03172)
- Microsoft. (2024). "GraphRAG: Unlocking LLM discovery on narrative private datasets." [microsoft.com/research](https://www.microsoft.com/en-us/research/blog/graphrag-unlocking-llm-discovery-on-narrative-private-datasets/)
- Asai, A. et al. (2023). "Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection." [arXiv:2310.11511](https://arxiv.org/abs/2310.11511)
- Yan, S. et al. (2024). "Corrective Retrieval Augmented Generation." [arXiv:2401.15884](https://arxiv.org/abs/2401.15884)
- Jeong, S. et al. (2024). "Adaptive-RAG: Learning to Adapt Retrieval-Augmented Large Language Models through Question Complexity." [arXiv:2403.14403](https://arxiv.org/abs/2403.14403)
- RAGFlow. (2025). "Year-End Review: From RAG to Context Engine." [github.com/infiniflow/ragflow](https://github.com/infiniflow/ragflow)
- NirDiamant. (2025). "RAG Techniques." [github.com/NirDiamant/RAG_Techniques](https://github.com/NirDiamant/RAG_Techniques)
- Google Research. (April 2026). "Titans + MIRAS: Helping AI Have Long-Term Memory." [research.google/blog/titans-miras-helping-ai-have-long-term-memory/](https://research.google/blog/titans-miras-helping-ai-have-long-term-memory/) --- trainable memory modules outperforming Mamba-2 / Gated DeltaNet / Transformer++ at comparable sizes.

---

*이전 장: [1장 — 세 세대](01-evolution.md)*

*다음 장: 3장 — Context Engineering 심화 (출시 예정)*
