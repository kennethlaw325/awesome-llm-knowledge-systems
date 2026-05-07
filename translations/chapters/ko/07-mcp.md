# 7장: MCP —— 이긴 표준

> **한 문장으로:** MCP는 AI가 단일 프로토콜을 통해 어떤 외부 도구나 데이터 출처에도 연결할 수 있게 하는 보편 표준이다.
>
> **왜 중요한가:** MCP를 AI를 위한 USB라고 생각하라 ——그것 이전에는 모든 도구가 자기만의 커스텀 연결을 필요로 했다. 이제 모든 곳에서 작동하는 한 플러그가 있다.

## MCP란 무엇인가?

Model Context Protocol (MCP)은 AI 모델이 외부 도구, 데이터 출처, 서비스에 연결하는 방식을 표준화하기 위해 Anthropic이 만든 오픈 프로토콜이다. MCP 이전에는 모든 AI 통합이 맞춤 작업이었다 ——커스텀 함수 정의, 독점 도구 형식, 직접 만든 인증, 깨지기 쉬운 글루 코드. MCP는 이 파편화를 보편 인터페이스로 대체했다: 어떤 모델도 사용해 어떤 도구도 발견하고, 인증하고, 호출할 수 있는 단일 프로토콜.

MCP를 AI를 위한 USB라고 생각하라. USB 이전에는 모든 주변 장치가 자기만의 커넥터, 드라이버, 프로토콜을 필요로 했다. USB는 주변 장치를 더 강력하게 만들지 않았다 ——그것들을 상호 운용 가능하게 만들었다. MCP는 AI 도구 생태계에 같은 일을 한다. 단일 MCP 서버 구현이 Claude, GPT, Gemini, 또는 프로토콜을 말하는 어떤 다른 모델에도 서비스할 수 있다. 단일 MCP 클라이언트가 커스텀 통합 코드 없이 수천 개의 서버에 연결할 수 있다.

## 타임라인: 출시에서 Linux Foundation까지

**2024년 11월.** Anthropic이 Python과 TypeScript용 참조 구현과 함께 MCP를 오픈소스 사양으로 공개한다. 초기 릴리스는 한 줌의 참조 서버 (파일시스템, GitHub, Slack)와 커스텀 서버를 만들기 위한 SDK 지원을 포함한다. 반응은 조심스럽게 낙관적이다 ——AI 커뮤니티는 이전에 상호 운용성 표준이 제안되는 것을 본 적이 있다.

**2025년 4월.** 출시 6개월 후, MCP는 8백만 누적 SDK 다운로드를 넘어서고 커뮤니티는 5,800개 이상의 서버를 만들었다. 생태계는 누구도 예상하지 못한 것보다 빠르게 자란다. 결정적으로, 경쟁 AI 연구실들이 대안을 만드는 대신 프로토콜을 채택하기 시작한다.

**2025년 후반.** MCP가 Linux Foundation 산하의 새 단체 Agentic AI Foundation에 기증된다. 창립 거버넌스에 Anthropic, Block, OpenAI가 참여한다. 이 움직임은 "Anthropic이 표준을 통제한다"는 우려를 중화시키고, MCP를 벤더 특정 프로토콜이 아니라 진정한 산업 표준으로 확립한다.

**2026년 (현재).** 모든 패키지 레지스트리에 걸쳐 MCP SDK 다운로드가 월 9,700만을 초과한다. 생태계는 재단이 유지하는 75개 이상의 공식 커넥터를 포함하며, 수천 개의 커뮤니티 빌드 서버가 더 있다. 이 프로토콜은 AI 애플리케이션의 기본 통합 계층이 되었다, REST가 웹 API의 기본이 되었던 것처럼.

## 그것이 이긴 이유

MCP의 빠른 지배를 설명하는 몇 가지 요인:

**처음부터 오픈 표준.** MCP는 단지 SDK가 아니라 전체 사양과 함께 관대한 라이선스로 공개되었다. 이는 경쟁자들이 Anthropic의 코드나 호의에 의존하지 않고 그것을 구현할 수 있음을 의미했다.

**단순한 아키텍처.** 프로토콜은 세 가지 핵심 개념을 가진다: 클라이언트 (AI 모델 측), 서버 (도구/데이터 측), 트랜스포트 (그것들이 어떻게 통신하는가). 서버는 JSON Schema 설명을 가진 도구를 노출한다. 클라이언트는 그것들을 발견하고 호출한다. 트랜스포트는 통신 계층 (stdio, SSE를 가진 HTTP, WebSocket)을 다룬다. 이 단순함이 채택을 사소하게 만들었다 ——유능한 개발자가 한 시간 안에 MCP 서버를 만들 수 있다.

**벤더 중립 거버넌스.** OpenAI를 공동 거버넌스 멤버로 한 Linux Foundation에의 기증은 마지막 신뢰할 만한 반대를 제거했다. 당신의 1차 경쟁자가 표준을 공동 거버넌스할 때, 그 표준은 진정으로 중립이다.

**네트워크 효과.** 모든 새 MCP 서버가 모든 클라이언트에 대해 프로토콜을 더 가치 있게 만들고, 그 반대도 마찬가지다. 생태계가 유용한 서버의 임계 질량을 넘자, MCP를 지원하지 않는 비용이 그것을 채택하는 비용보다 더 높아졌다.

## 핵심 채택자

MCP 채택의 폭은 그 지배의 이야기를 말한다:

- **OpenAI**가 ChatGPT 플랫폼과 Agents SDK에 MCP 지원을 통합하여, GPT 모델이 어떤 MCP 서버도 사용하게 했다.
- **Google DeepMind**가 Gemini에 MCP 클라이언트 지원을 추가했고, 1차 동기로 생태계 호환성을 인용했다.
- **Microsoft**가 가장 멀리 갔다. Windows에 OS 레벨에서 MCP 지원을 구축하고 Azure AI 서비스, Copilot, GitHub Copilot에 걸쳐 통합했다.
- **Amazon / AWS**가 2026년 4월에 첫 운영 양방향 MCP 런타임으로서 **Bedrock AgentCore Runtime**을 출하했고, 표준 프로토콜 위에 elicitation과 sampling을 더했다 (아래 "Stateful MCP 전환" 참조).
- **GitHub**가 자사의 Copilot 확장 시스템을 MCP 위에 다시 만들어, 그들의 독점 도구 형식을 대체했다.
- **Figma, Slack, Block, Notion** 모두 공식 MCP 서버를 출하하여, 자신의 플랫폼을 어떤 AI 워크플로우에서도 1급 시민으로 만들었다.
- **Hugging Face**가 자사의 모델 허브와 함께 커뮤니티 MCP 서버 레지스트리를 호스팅한다.
- **LangChain**과 다른 편성 프레임워크가 네이티브 MCP 클라이언트 지원을 제공하여, 그것을 기본 도구 통합 방법으로 만들었다.

**합성 차원으로서의 MCP.** 더 미묘한 2026년 발전: MCP 도구 선택이 고정 기반이 아니라 자동 harness 합성 시스템의 *변수*들 중 하나로 나타나기 시작하고 있다. AgentFlow 논문 (arXiv 2604.20801, 2026년 4월)은 에이전트 역할, prompt, *도구*, 통신 토폴로지, 협조 프로토콜을 자체 합성 루프가 검색하는 타입 그래프 DSL의 다섯 차원으로 다룬다. MCP 인식 harness 설계자에게 이는 양날이다. MCP의 표준화가 도구 차원을 진정으로 검색 가능하게 만든다 ——합성 루프가 통합 계층을 다시 쓰지 않고 한 MCP 서버를 다른 것으로 바꿀 수 있다. 그러나 같은 표준화가 MCP 서버 자체를 선택 후보로 만든다: 질문은 더 이상 "어떤 서버를 설치하는가"가 아니라 "내 harness가 관측가능성 압력 아래에서 *어떤 서버를 사용하도록 진화하는가*"이다.

## 지식 엔지니어링과의 연결

MCP는 그 자체로 지식 엔지니어링 기법이 아니다 ——그것은 지식 엔지니어링을 스케일 가능하게 만드는 인프라 계층이다. 본 보고서에서 논의된 모든 접근 ——RAG 파이프라인, 지식 그래프, 메모리 시스템, context engineering 패턴 —— 은 외부 지식을 모델에 먹이는 것을 요구한다. MCP는 그 먹이는 일이 일어나는 방식을 표준화한다.

실용적 예를 고려하라: 회사 위키에 접근하고, 데이터베이스를 쿼리하고, 벡터 저장소를 검색하고, 파일 시스템에서 읽어야 하는 지식 강화 AI 에이전트. MCP 없이는 이 통합 각각이 커스텀 코드, 커스텀 인증, 커스텀 오류 처리를 요구한다. MCP와 함께라면 각각이 MCP 서버이며, 에이전트는 통합된 인터페이스를 통해 그 모두에 연결된다.

이것이 MCP가 지식 엔지니어링 생태계에 중심인 이유이다. 그것은 RAG나 메모리를 대체하지 않는다 ——그것은 그것들이 모델과 플랫폼 전반에 걸쳐 구성 가능하고, 이식 가능하고, 상호 운용 가능하게 만드는 배관을 제공한다.

## Meta-Tool 패턴

MCP 채택에서 부상한 가장 중요한 아키텍처 패턴 중 하나는 Meta-Tool 패턴이며, 도구를 위한 progressive disclosure라고도 불린다.

문제: MCP 생태계가 자라면서, 에이전트가 수십 또는 수백 개의 도구에 접근할 수 있다. 그것들의 모든 스키마를 context window에 로드하는 것은 낭비이다 ——대부분의 도구가 어떤 주어진 작업에도 무관하다. 29개의 도구 스키마가 로드되면, 모델이 결코 사용하지 않을 도구 설명에 수천 토큰을 태우고, 모델이 잘못된 도구를 선택할 가능성을 증가시킨다.

해결책: 모든 도구 스키마를 미리 로드하는 대신, 두 개의 메타 도구를 로드하라: 에이전트가 설명으로 관련 도구를 검색할 수 있게 하는 **discovery tool**과, 발견된 도구를 참조로 호출하는 **execution tool**. 에이전트는 먼저 자신의 현재 작업에 어떤 도구가 사용 가능한지 발견하고, 그 다음 필요한 스키마만 로드한다.

이 패턴은 도구가 많은 환경에서 context window 소비를 80–90% 줄이고 결정 공간을 줄여 도구 선택 정확도를 개선한다. 그것은 10–15개 이상의 사용 가능한 도구를 가진 어떤 배포에 대해서도 모범 사례가 되었다.

## 2026년 과제

성공에도 불구하고, MCP는 의미 있는 열린 과제에 직면해 있다:

**감사 추적.** 엔터프라이즈 환경에서, 모든 도구 호출이 로깅, 귀속, 컴플라이언스 추적을 필요로 한다. 현재 MCP 사양은 감사 추적 형식을 처방하지 않아, 일관성 없는 구현으로 이어진다.

**SSO 통합 인증.** MCP의 인증 이야기는 출시 이래 의미 있게 개선되었지만, 전체 클라이언트-서버-트랜스포트 사슬에 걸쳐 엔터프라이즈 SSO 시스템 (SAML, OIDC)과 통합하는 것은 여전히 마찰이 많다. 최근 비준된 MCP를 위한 OAuth 2.1 흐름이 이 일부를 다루지만, 채택은 여전히 진행 중이다.

**게이트웨이 행동.** 조직들이 MCP를 스케일에서 배포함에 따라, 그들은 속도 제한, 접근 통제, 요청 라우팅, 모니터링을 위한 게이트웨이 계층을 필요로 한다. 생태계는 표준 MCP 게이트웨이 사양을 결여하여, 독점 해법으로 이어진다.

**구성 이식성.** MCP 서버 구성 (어떤 서버에 어떤 자격으로 어떤 순서로 연결할지)은 표준화되지 않았다. 머신, 팀, 또는 조직 사이에서 MCP 셋업을 옮기는 것은 수동 재구성을 요구한다.

**도구 설명 품질.** MCP의 효과는 전적으로 도구 설명의 품질에 의존한다. 잘못 설명된 도구는 부정확한 호출로 이어진다. 도구 설명 품질에 대한 표준이 없고, 린팅이 없고, 인증이 없다.

**스키마 버저닝.** MCP 서버가 자신의 도구 스키마를 갱신하면, 기존 클라이언트가 깨질 수 있다. 프로토콜은 내장 버저닝과 호환성 협상 메커니즘을 결여한다.

**도구 중복.** 수천 개의 커뮤니티 서버와 함께, 여러 서버가 종종 겹치는 기능을 제공한다. 프로토콜은 중복 제거나 선호 표현을 위한 메커니즘을 제공하지 않는다.

## 2026: Stateful MCP 전환

처음 18개월에 걸쳐, MCP는 근본적으로 **무상태 RPC 프로토콜**이었다: 클라이언트가 서버를 호출하고, 서버가 결과를 반환하고, 대화는 다음으로 넘어간다. 이 모델은 단순 도구 호출 (파일 읽기, API 쿼리, 메시지 게시)에는 잘 작동했지만, 어떤 장기간이거나 인터랙티브한 것에는 어려움을 겪었다. 2026년 4월에, 두 발전이 MCP를 진정한 오케스트레이션 계층으로 밀기 시작했다.

**SEP-1686: Tasks Primitive.** 2026년 4월 MCP Dev Summit에서 도입된 **SEP-1686**은 프로토콜에 내구성 있는 작업 상태 머신을 더한다. 각 장기간 도구 호출은 영속 ID와 다섯 상태 중 하나 ——`working`, `input_required`, `completed`, `failed`, `cancelled` —— 를 가진 **task**가 된다. 클라이언트는 task를 시작하고, 연결을 끊고, 나중에 상태를 확인하거나 결과를 가져오기 위해 다시 연결할 수 있다 ——**call-now / fetch-later** 패턴. Task ID는 서버가 보낸 알림과 상관되어 클라이언트가 열린 연결을 유지하지 않고 진행 이벤트에 구독할 수 있다. 이 primitive는 MCP가 이전에 맞춤 우회로 강제했던 워크플로우를 정확히 겨냥한다:

- 완료에 분이나 시간이 걸리는 **데이터 파이프라인**
- 큰 저장소에 걸친 **코드 마이그레이션**
- 전체 CI 스위트를 위한 **테스트 실행**
- 서브 에이전트를 생성하고 외부 API를 기다리는 **심화 연구**
- 한 에이전트가 다른 에이전트에게 작업을 비동기적으로 넘기는 **다중 에이전트 시스템**

SEP-1686은 2026년 4월 MCP 사양에서 실험적으로 출시된다. 이는 무상태 RPC에서 내구성 있는 재개 가능한 편성으로의 첫 진지한 단계이다.

**Amazon Bedrock AgentCore: 첫 양방향 런타임.** 또한 2026년 4월에, AWS가 **양방향** 통신을 구현한 첫 운영 MCP 런타임 **Bedrock AgentCore Runtime**을 출하한다. 표준 MCP는 클라이언트가 시작한다: 클라이언트가 도구를 호출하고, 서버가 응답한다. AgentCore는 두 가지 서버 시작 능력을 더한다:

- **Elicitation.** 실행 도중에, 서버가 일시 정지하고 JSON 스키마에 대해 사용자로부터 구조화된 입력을 요청할 수 있다. 이는 이전에 커스텀 UI 계층을 필요로 했던 다단계 워크플로우를 프로토콜 레벨 상호작용으로 바꾼다. 마이그레이션 도구가 멈추고 "어떤 브랜치를 대상으로 해야 하는가?"를 타입이 있는 응답과 함께 물을 수 있다.
- **Sampling.** 서버가 자체 모델 자격을 보유하지 않고 클라이언트로부터 LLM 생성 완성을 요청할 수 있다. 서버가 prompt와 표집 매개변수를 제공한다. 클라이언트가 자기 모델을 실행하고 완성을 반환한다. 이는 도구 서버가 LLM 기반 작업 (요약, 분류, 추출)을 할 수 있게 하면서, 사용자의 모델, 쿼터, 청구는 클라이언트 측에 남는다.

함께, elicitation과 sampling이 MCP의 양방향 프로토콜 표면을 완성한다. 서버는 이제 단지 호출에 응답하지 않고 대화의 일부를 **운전**할 수 있다.

**함의.** MCP의 2025년 프레이밍은 "무상태 도구를 위한 통합 플러그"였다. 2026년 프레이밍은 더 넓다: MCP는 **상태 있는, 인터랙티브한, 양방향 에이전트 편성**을 위한 프로토콜 계층이 되고 있다. 도구 서버는 더 이상 수동적이지 않다 ——그것들은 내구성 있는 상태를 유지하고, 사용자 입력을 위해 일시 정지하고, 클라이언트로부터 LLM 작업을 요청할 수 있다. 지식 엔지니어링에 이는 장기간 검색 파이프라인, 단계화된 데이터 강화, human-in-the-loop 워크플로우가 마침내 위에서 실행할 네이티브 프로토콜을 가짐을 의미한다.

## 시장 맥락

산업 분석가들은 ——MCP가 지배적 프로토콜인 —— AI 도구 통합 시장을 2025년에 18억 달러로 추정하며, 엔터프라이즈 채택이 가속함에 따라 의미 있는 성장이 예상된다. 이 수치는 MCP 인프라, 서버 개발, 게이트웨이 서비스, 관련 도구를 포함한다.

## 핵심 자원

- **[modelcontextprotocol.io](https://modelcontextprotocol.io)** ——공식 사양, SDK, 문서.
- **Anthropic MCP Courses** —— [Skilljar](https://anthropic.skilljar.com)와 [DeepLearning.AI](https://www.deeplearning.ai/short-courses/)에서 가용, 프로토콜 기초와 서버 개발을 다룬다.
- **The New Stack** —— MCP 아키텍처, 채택, 과제에 대한 지속적 기술 보도. Meta-tool 패턴과 엔터프라이즈 배포 패턴에 관한 주목할 만한 기사.
- **MCP SDK 다운로드 통계** —— npm (`@modelcontextprotocol/sdk`, [https://www.npmjs.com/package/@modelcontextprotocol/sdk](https://www.npmjs.com/package/@modelcontextprotocol/sdk))과 PyPI (`mcp`, [https://pypi.org/project/mcp/](https://pypi.org/project/mcp/))에서 1차 채택 지표.

## Sources

1. Anthropic. "Introducing the Model Context Protocol." November 2024. https://www.anthropic.com/news/model-context-protocol
2. Model Context Protocol Specification. https://modelcontextprotocol.io
3. Linux Foundation. "Agentic AI Foundation Established." 2025. https://www.linuxfoundation.org/press/agentic-ai-foundation
4. MCP SDK download statistics, npm: [https://www.npmjs.com/package/@modelcontextprotocol/sdk](https://www.npmjs.com/package/@modelcontextprotocol/sdk) and PyPI: [https://pypi.org/project/mcp/](https://pypi.org/project/mcp/) (Q1 2026 cumulative ~97M downloads, widely cited in secondary coverage).
5. The New Stack. "The Meta-Tool Pattern: Progressive Disclosure for AI Tools." 2025.
6. Anthropic. MCP Course. Skilljar. https://anthropic.skilljar.com
7. DeepLearning.AI. "Building MCP Servers." https://www.deeplearning.ai/short-courses/
8. Microsoft. "MCP Support in Windows and Azure." 2025. https://devblogs.microsoft.com
9. OpenAI. "Agents SDK: MCP Integration." 2025. https://openai.com/index/new-tools-for-building-agents
10. AgentFlow / "Synthesizing Multi-Agent Harnesses for Vulnerability Discovery." arXiv 2604.20801, April 2026. [https://arxiv.org/abs/2604.20801](https://arxiv.org/abs/2604.20801)

---

*이전 장: [6장 — 에이전트 메모리: 빠진 계층](06-agent-memory.md) | 다음 장: [8장 — 도구 풍경: AI 네이티브 지식 관리](08-tools-landscape.md)*
