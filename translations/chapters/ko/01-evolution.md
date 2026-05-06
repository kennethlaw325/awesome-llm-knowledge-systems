# 1장: 세 세대

> **한 문장으로:** AI 엔지니어링은 좋은 prompt를 작성하는 것에서, AI 모델 주변에 운영 체제 전체를 설계하는 것으로 진화했다.
>
> **왜 중요한가:** 이 분야가 어디로 향하는지 이해하면 적합한 도구를 선택하고 시대에 뒤떨어진 접근을 피할 수 있다.

**Prompt engineering에서 context engineering으로, 그리고 harness engineering으로 —— 그리고 이 셋의 경계가 생각만큼 중요하지 않은 이유.**

---

## 제 1세대: Prompt Engineering (2022–2024)

2022년 11월 ChatGPT가 출시되었을 때, 인간과 대규모 언어 모델 사이의 인터페이스는 통째로 텍스트 박스 하나였다. 거기서 출현한 분야가 prompt engineering이다 ——더 나은 출력을 얻기 위해 입력 텍스트를 다듬는 기예이자 과학.

핵심 기법들이 빠르게 발전했다:

**Few-shot prompting**(Brown 외, 2020)은 prompt에 예시를 포함시키는 것만으로도 fine-tuning 없이 작업 성능이 극적으로 개선될 수 있음을 보였다. 감정 분류를 위해 모델을 훈련하는 대신, 예시 세 개를 보여주고 네 번째를 분류하게 한 것이다.

**Chain-of-thought (CoT) prompting**(Wei 외, 2022)은 "Let's think step by step"을 덧붙이거나 예시에 추론 흔적을 포함시키는 것만으로 표준 prompting에서는 보이지 않던 다단계 추론 능력이 나타남을 보였다. 이는 아마도, *문맥을 어떻게 구조화하는가*가 *무엇을 묻는가*만큼 중요하다는 첫 번째 단서였다.

**Prompt template**이 표준적인 추상화가 되었다. LangChain, LlamaIndex, 그리고 수십 개의 프레임워크가 정교하게 설계된 prompt 구조에 변수를 주입할 수 있는 템플릿 시스템을 제공했다. 멘탈 모델은 명확했다: prompt가 프로그램이고 모델이 런타임이다.

이 시대의 다른 기법들에는 다음이 포함된다:

- **ReAct**(Yao 외, 2022): 추론 단계와 행동 단계를 번갈아, 단일 prompt 구조 안에서 모델이 계획과 도구 호출을 실행하게 한다.
- **Tree of Thought**(Yao 외, 2023): 여러 추론 경로를 탐색하고 최선의 것을 선택한다.
- **Self-consistency**(Wang 외, 2022): 여러 추론 사슬을 샘플링하고 다수결을 취한다.

이 시대의 한계는 그 전제에 있었다: LLM 상호작용의 품질은 주로 prompt의 품질에 의해 결정된다는 전제. 이는 context window가 4K–8K 토큰이고 입력이 사용자 텍스트뿐이던 시절에는 옳았다. 모델이 10만+ 토큰을 받아들이고 외부 도구를 호출할 수 있게 되자 이 전제는 더 이상 유효하지 않게 되었다.

### 이 시대가 옳게 본 것

Prompt engineering은 *구조가 중요하다*는 것을 확립했다. 좋은 prompt와 나쁜 prompt의 차이는 감각이 아니라 ——정보 아키텍처다. 그 통찰은 그 다음 모든 것으로 이어졌다.

### 이 시대가 놓친 것

Context window를 정적인 산출물로 취급했다. Prompt를 작성하고, 제출하고, 응답을 받는다. Context window 자체가 실행 시점에 여러 소스로부터 *동적으로 구성될 수 있다*는 발상 ——그것이 다음 세대의 통찰이었다.

---

## 제 2세대: Context Engineering (2025)

2025년 중반, Andrej Karpathy가 prompt engineering과 context engineering 사이에 날카로운 선을 그으며, AI 엔지니어링 커뮤니티에서 가장 많이 공유된 관찰 중 하나를 게시했다:

> "이것에 대해 생각해 봤는데, 대부분의 사람들이 실제로 잘해야 하는 것의 올바른 용어는 'prompt engineering'이 아니라 'context engineering'이라고 본다. 다음 단계에 필요한 정보를 적절히 context window에 채우는 기예이자 과학이다."

이 리프레이밍이 중요했던 이유는, 주의를 *지시*(prompt)에서 *정보 패키지 전체*(context window)로 옮겼기 때문이다. 현대 LLM 호출의 context window에는 사용자 prompt보다 훨씬 더 많은 것이 들어 있다:

- 동작과 제약을 정의하는 시스템 지시
- RAG 파이프라인에서 검색된 문서
- 도구 정의와 스키마
- 대화 이력(선택적으로 압축됨)
- 동적으로 선택된 few-shot 예시
- 현재 작업에 관한 구조화된 메타데이터

Prompt는 한 구성 요소일 뿐이다. Context engineering은 이 모두를 편성하는 것이다.

### 여섯 가지 기법

[Towards AI의 분석](https://towardsai.net/)은 이 분야를 정의하는 여섯 가지 핵심 기법을 식별했다:

1. **Retrieval-Augmented Generation (RAG)**: 질의 시점에 관련 문서를 가져온다
2. **Tool 및 API 통합**: 구조화된 스키마로 모델에 외부 능력 접근을 부여한다
3. **Memory management**: 대화 턴과 세션 횡단으로 관련 정보를 유지한다
4. **동적 prompt 구축**: 템플릿, 검색된 콘텐츠, 실행 시점 상태로부터 prompt를 조립한다
5. **Context window 최적화**: 한정된 토큰 예산에 무엇을 넣고 무엇을 빼는지 관리한다
6. **지시 계층**: 시스템, 개발자, 사용자 지시를 명확한 우선순위로 계층화한다

### Manus의 교훈

[Manus](https://manus.im/) ——2025년 가장 많이 언급된 AI 에이전트 플랫폼 중 하나 —— 는 스케일에서의 context engineering에 대한 중요한 교훈을 공유했다:

**KV-cache 통찰**: Manus는 KV-cache 적중률을 높게 유지하도록 context window를 설계했다 ——어텐션 메커니즘에서 이전에 계산된 key-value 쌍이 턴 횡단으로 재사용되도록. 이는 지연과 비용을 극적으로 낮추었다. 원칙: 호출 사이에 *접두부는 안정적*으로 유지하고 *접미부만 변하도록* context를 구조화하라.

**100:1 비율**: Manus는 모델 출력 1 토큰당 약 100 토큰의 context가 소비된다고 보고했다. 이는 출력 토큰이 주요 비용 요인이라는 일반적 가정을 뒤집었다. 진정한 엔지니어링 과제는 텍스트를 생성하는 것이 아니라 ——*어떤 context를 투입할지 선택하는 것* —— 이었다.

**제품으로서의 context**: Manus는 context window 구축을 구현 세부 사항이 아니라 핵심 제품 기능으로 취급했다. 에이전트의 품질은 context 조립 파이프라인의 품질에 직접 비례했다.

### 분류 체계의 전환

Context engineering은 LLM 애플리케이션 개발을 "좋은 prompt 작성"에서 "좋은 정보 파이프라인 구축"으로 리프레이밍했다. 모델은 받은 context 위에서 동작하는 추론 엔진이 되었다. 엔지니어링 과제는 상류로 옮겨갔다 ——검색, 필터링, 랭킹, 압축, 조립으로.

그러나 이 프레이밍에도 천장이 있었다. *모델에 들어가는 것*은 기술했지만 *모델 주변 시스템이 어떻게 동작하는가*는 기술하지 못했다. 그것에는 또 다른 전환이 필요했다.

---

## 제 3세대: Harness Engineering (2026)

2025년 후반부터 2026년 초까지, 영향력 있는 두 작품이 다음 진화를 형식화했다:

**Birgitta Böckeler**(ThoughtWorks)는 2026년 4월 Martin Fowler의 *Exploring Generative AI* 메모 시리즈에 기고한 분석에서, LLM 애플리케이션에서 가장 영향력 있는 엔지니어링 작업이 모델 훈련이나 prompt 다듬기가 아니라 *harness* —— 모델 호출을 신뢰성 있는 워크플로로 편성하는 도구, 라우팅, 메모리, 계획, 오류 복구의 주변 시스템 —— 에서 일어나고 있다고 논했다.

**OpenAI의 Codex 팀**은 에이전트적 코딩의 harness 측면에 대한 사례 연구 자료를 공개해 왔다 (공식 자료는 openai.com/index/introducing-codex 참조). 널리 인용되는 "엔지니어 3명 / 약 100만 줄 / 약 1,500개 PR" 수치는 2025–2026년 OpenAI 강연과 게시물을 통해 유통되었다; 근저의 관찰은 Codex의 품질이 주로 모델이 아니라 harness ——모델을 *언제* 호출할지, *어떤 context*를 제공할지, *어떤 도구*를 사용 가능하게 할지, 오류를 어떻게 검증하고 회복할지 결정하는 시스템 —— 에 의해 결정되었다는 것이다.

### Phil Schmid의 비유

[Phil Schmid](https://www.philschmid.de/) (Hugging Face)는 이 개념을 결정화한 비유를 제시했다:

- **모델은 CPU** —— 원시 계산 능력
- **Context window는 RAM** —— 현재 작업을 위한 작업 메모리
- **Harness는 운영 체제** —— 스케줄링, 자원 관리, I/O, 오류 처리, 사용자 인터페이스

이 비유는 왜 harness engineering이 중요한지 명확히 한다: 누구도 OS 없이 CPU만 출하하지 않는다. 모델은 필요하지만 충분하지 않다. 모델이 실제로 무엇을 해낼 수 있는지 결정하는 것은 harness다.

### Meta-Harness 논문과 6배 격차

2026년 초에 발표된 연구는 실무자들이 막연히 느끼던 것을 정량화했다: 베어 모델과 잘 harness된 모델 사이의 격차는 **복잡한 작업에서 약 6배** 였다. 같은 가중치, 같은 훈련 데이터의 같은 모델이, harness의 품질에 따라 6배의 차이로 다른 결과를 생산했다.

이는 대부분의 실용 애플리케이션에서 harness engineering이 모델 개선보다 더 큰 레버리지를 제공한다는 것을 의미했다. 좋은 모델 위에 나은 harness는, 평범한 harness의 위대한 모델을 능가했다.

### IMPACT 프레임워크

2020년대 중반 실무자 담론에서, harness 품질을 평가하는 체크리스트로 IMPACT 기억법이 떠올랐다:

- **I**nstructions —— 시스템 지시의 명료함과 완전성
- **M**emory —— 세션 횡단의 지속과 검색
- **P**lanning —— 작업 분해와 시퀀싱
- **A**ctions —— 도구 가용성과 신뢰성
- **C**ontext —— 관련 정보의 동적 조립
- **T**esting —— 평가와 품질 보증 루프

IMPACT는 context engineering을 더 넓은 harness engineering 분야 안의 한 구성 요소("C")로 위치시킨다. 이 중첩이 핵심 구조적 통찰이다: context engineering은 harness engineering으로 *대체되는* 것이 아니라 그 *안에 있다*.

### Meta가 Manus를 인수 (~20억 달러)

2026년 초, Meta는 Manus를 약 20억 달러에 인수했다. 인수는 Meta가 *모델이 아니라 harness를 사들였다*고 널리 해석되었다. Meta는 이미 Llama를 가지고 있었다. 가지지 못했던 것은 context 조립, 도구 편성, 에이전트 런타임 관리의 본격 검증된 시스템이었다.

이 인수는 다음 테제를 검증했다: LLM 생태계에서 가장 가치 있는 엔지니어링은 점점 모델 계층이 아니라 편성 계층에 있다.

---

## 핵심 통찰: 대체가 아니라 공존

이 세 세대는 한 세대가 다음 세대로 대체되는 깔끔한 역사적 시기가 아니다. 본격 시스템 안에서 공존하는 *중첩된 계층*이다:

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

Harness 엔지니어는 여전히 prompt를 쓴다. 여전히 context engineering을 한다. 그러나 더해서 어떤 prompt를 언제 쓸지, 상황마다 어떤 context를 조립할지, 문제가 생기면 어떻게 회복할지 결정하는 *시스템*을 구축한다.

진화는 이전 기법을 버리는 것이 아니다. 그것들이 필요하지만 충분하지 않다는 것을 인식하고 ——그 위에 계층을 쌓아 원시 LLM 능력을 신뢰성 있는, 본격 등급의 애플리케이션으로 만드는 것이다.

상하이 교통대학 등의 19인 저자 서베이 **"Externalization in LLM Agents: A Unified Review of Memory, Skills, Protocols and Harness Engineering"** (arXiv 2604.08224, 2026년 4월 9일)은 이 장이 사용하는 것과 같은 3계층 조직에 독립적으로 도달한다: 그들의 프레이밍에서 이 분야의 진전은 *weights*에서 *context*로, *harness*로 진행되며, memory, skills, protocols, harness engineering을 harness를 통합 계층으로 하는 4개의 외재화된 구성 요소로 다룬다. 이 수렴은 학술 문헌에서 본 가이드로 오는 독자에게 명시할 가치가 있다: 이는 실무자만의 프레이밍이 아니며 본 가이드 고유의 것도 아니다 ——2026년 4월 후반의 학술 서베이도 같은 조직 축을 선택했다.

---

## Sources

- Brown, T. et al. (2020). "Language Models are Few-Shot Learners." [arXiv:2005.14165](https://arxiv.org/abs/2005.14165)
- Wei, J. et al. (2022). "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models." [arXiv:2201.11903](https://arxiv.org/abs/2201.11903)
- Yao, S. et al. (2022). "ReAct: Synergizing Reasoning and Acting in Language Models." [arXiv:2210.03629](https://arxiv.org/abs/2210.03629)
- Yao, S. et al. (2023). "Tree of Thoughts: Deliberate Problem Solving with Large Language Models." [arXiv:2305.10601](https://arxiv.org/abs/2305.10601)
- Wang, X. et al. (2022). "Self-Consistency Improves Chain of Thought Reasoning in Language Models." [arXiv:2203.11171](https://arxiv.org/abs/2203.11171)
- Karpathy, A. (mid-2025). "context engineering"을 본 분야의 올바른 용어로 명명한 공개 발언; X와 AI 엔지니어링 커뮤니티 전반에서 널리 공유된 프레이밍.
- Manus. (2025). "Context Engineering Lessons from Building Manus." [manus.im/blog](https://manus.im/blog) — 운영 지표로서 KV-cache 적중률, append-only context, logit bias로 도구 마스킹, 롤링 todo-list 재작성.
- Böckeler, Birgitta. (April 2, 2026). "Harness engineering for coding agent users." martinfowler.com (*Exploring Generative AI* series). [https://martinfowler.com/articles/harness-engineering.html](https://martinfowler.com/articles/harness-engineering.html) — Guides vs. Sensors, Computational vs. Inferential 분류.
- OpenAI. Codex 공식 자료: [https://openai.com/index/introducing-codex](https://openai.com/index/introducing-codex). Codex의 harness 설계 프레이밍을 위한 앵커; 널리 인용되는 "엔지니어 3명 / 약 100만 줄 / 약 1,500개 PR" 수치는 2025–2026년 OpenAI 강연과 게시물에서 유통되었으며, 단일 정전 게시물이 아닌 커뮤니티 인용으로 여기 보고한다.
- Schmid, Philipp. "The New Skill in AI is Not Prompting, It's Context Engineering" 및 후속편. [https://www.philschmid.de/context-engineering](https://www.philschmid.de/context-engineering); [https://www.philschmid.de/context-engineering-part-2](https://www.philschmid.de/context-engineering-part-2) — Model = CPU, Context = RAM, Harness = OS 비유.
- IMPACT 기억법. Intent / Memory / Planning / Authority / Control flow / Tools — 2020년대 중반 실무자 담론에서 떠오른 6차원 harness 설계 체크리스트. 본 장에서는 교육적 프레이밍으로 사용; 특정 1차 출처에 귀속시키지 않음.
- Meta/Manus 인수 보도. (2026). 다양한 출처.
- Zhou, C. et al. (April 2026). "Externalization in LLM Agents: A Unified Review of Memory, Skills, Protocols and Harness Engineering." [arXiv:2604.08224](https://arxiv.org/abs/2604.08224) — 상하이 교통대학 등의 19인 저자 서베이가 Weights → Context → Harness 3계층 역사적 프레이밍을 독립적으로 사용. 본 장의 "대체가 아니라 공존" 절에서 실무자 테제가 학술 문헌과 수렴한 증거로 인용.

---

*다음 장: [2장 — RAG, 롱 컨텍스트, 지식 그래프](02-knowledge-layer.md)*
