# 5장: Skill 시스템 —— 스킬, 스킬 그래프, Progressive Disclosure

> **한 문장으로:** 스킬은 AI에게 특정 작업을 어떻게 하는지 알려주는 재사용 가능한 지시 세트이며, 스킬 그래프는 그것들을 항행 가능한 지식 네트워크로 연결한다.
>
> **왜 중요한가:** 매번 같은 것을 AI에게 설명하는 대신, 스킬은 한 번 가르치고 그 지식을 영원히 재사용하게 한다.

스킬은 사전 패키지된 지시 세트 ——prompt, 도구 구성, 행동 규칙의 자기 완결적 묶음 —— 이며, 특정 능력이 필요할 때 에이전트의 context window에 주입된다. 그것은 모델을 무관한 지시로 익사시키지 않고, 에이전트 시스템이 한 줌의 내장 행동에서 수백 또는 수천 개의 전문화된 능력으로 스케일하는 메커니즘이다.

본 장은 스킬 시스템의 아키텍처, 그것이 만드는 조합 문제, 그리고 그것을 푸는 progressive disclosure 패턴을 다룬다.

---

## 5.1 Skill 개념

스킬은, 가장 단순한 형태로, 특정 작업을 위한 지시를 담은 markdown 파일 (또는 구조화된 텍스트 블록)이다. 사용자 요청이 스킬의 트리거 조건과 일치하면, 스킬의 내용이 context window에 로드된다. 일치가 일어나지 않으면, 스킬은 토큰 0을 기여한다.

이는 모든 능력을 다루려는 단일체적 시스템 prompt와는 근본적으로 다르다. 90개 도구와 50개 행동 모드를 기술하는 시스템 prompt는 사용자가 메시지를 입력하기도 전에 50,000 토큰 이상을 소비할 수 있다. 스킬 기반 시스템은 관련된 것만 로드하여, 기준 context를 가볍게 유지하고 윈도우 용량을 실제 작업을 위해 예약한다.

설계 패턴은 소프트웨어 엔지니어링에서 빌려왔다: 스킬은 에이전트에게 플러그인이 애플리케이션에게 그러한 것이다. 그것들은 비대해지지 않고 확장성을 제공한다.

## 5.2 Anthropic 스킬 생태계

Anthropic은 2025년 10월에 Claude Code를 위한 스킬을 출시했다. 처음에는 프로젝트 특정 기능으로 ——`.claude/` 디렉토리의 markdown 파일들이며, Claude가 관련될 때 호출할 수 있다. 형식은 의도적으로 단순했다: 설명, 트리거 조건, 지시를 가진 markdown 파일.

2025년 12월까지, Anthropic은 agentskills.io를 통해 스킬을 오픈 표준으로 발표하며, 어떤 에이전트 시스템도 채택할 수 있는 이식 가능한 형식을 정의했다. 사양은 다음을 다뤘다:

- 스킬 메타데이터 (이름, 설명, 버전, 저자)
- 트리거 정의 (키워드 매치, 의도 분류기, 정규식 패턴)
- 콘텐츠 구조 (지시, 예제, 도구 구성)
- 의존성 선언 (이 스킬이 기반하는 다른 스킬)

생태계 반응은 빨랐다. 2026년 초까지, 공식 저장소는 87,000개 이상의 GitHub 스타를 누적했고, 커뮤니티 기여 스킬은 700,000개를 넘었다. awesome-llm-skills, awesome-agent-skills (공식 플랫폼 팀의 1,000개 이상 스킬을 특집), awesome-claude-code 같은 컬렉션이 1차 발견 채널이 되었다.

이 성장은 스킬이 풀려고 설계된 바로 그 문제를 만들었다: 너무 많은 능력이 제한된 context 공간을 두고 경쟁하는 것.

## 5.3 스케일링 문제

OpenAI의 에이전트 문서는 실용적 가이드라인을 포함한다: **에이전트당 도구를 20개 미만으로 유지하고, 10개를 넘어서면 정확도 저하를 예상하라.** 여러 모델 패밀리에 걸친 경험적 테스트가 이 임계를 확인한다. 각 추가 도구 정의는 context에 토큰을 더하고 모델의 선택 공간에 결정 분기를 더한다. 90개 도구에서, 스키마 오버헤드만으로도 50,000 토큰을 넘을 수 있다 ——어떤 대화, 메모리, 검색된 문서가 윈도우에 들어오기 전에.

저하는 단지 토큰 수에 관한 것이 아니다. 그것은 결정 복잡도에 관한 것이다. 모델이 90개 도구 중에서 골라야 할 때, 확률 질량이 얇게 퍼진다. 모델은 더 많은 추론 용량을 도구 선택에 쓰고 작업 실행에는 덜 쓴다. 도구 매개변수 구성에서의 오류율이 증가한다. 모델이 그럴듯하지만 틀린 도구를 더 자주 선택하기 시작한다.

스킬은 같은 스케일링 압력에 직면한다. 500개의 사용 가능한 스킬을 가진 시스템은 500개의 설명을 모두 context에 로드할 수 없다. 500개 스킬의 트리거 설명만 로드하더라도 수천 토큰을 소비할 수 있고 모델의 실제 요청 처리 능력을 저하시킬 수 있다.

해결책은 progressive disclosure이다.

## 5.4 Progressive Disclosure 아키텍처

Progressive disclosure는 다단계 정보 아키텍처로, 각 레벨이 다음 라우팅 결정에 딱 충분한 디테일을 제공한다:

**레벨 0: 라우팅 인덱스.** 카테고리를 스킬 그룹에 매핑하는 컴팩트한 표. 전체 스킬 라이브러리에 대해 200–500 토큰을 소비할 수 있다. 이것이 휴면 상태에서 시스템 prompt에 자리한다.

**레벨 1: 카테고리 설명.** 라우팅 인덱스가 관련 카테고리를 식별할 때, 그 카테고리 안의 스킬에 대한 한 단락 설명을 로드한다. 각 설명은 스캐닝을 위해 최적화되어 있다 ——관련성을 결정하기에 충분하지만, 실행하기에는 충분하지 않다.

**레벨 2: 스킬 링크와 의존성.** 선택된 스킬에 대해, 그 의존성 그래프를 로드한다 ——어떤 다른 스킬이나 도구가 필요한지, 어떤 context를 기대하는지.

**레벨 3: 섹션과 요약.** 스킬의 구조적 개요를 로드한다 ——전체 지시 콘텐츠 없이 섹션 헤더, 핵심 결정 시점, 매개변수 목록.

**레벨 4: 전체 콘텐츠.** 완전한 스킬 지시를 context window에 로드한다. 이는 실제로 호출되는 한두 개의 스킬에 대해서만 일어난다.

Heinrich와 arscontexta 팀에 의해 형식화된 핵심 통찰은, **대부분의 결정이 단일 전체 파일을 읽기 전에 일어난다**는 것이다. 라우팅 인덱스가 스킬의 95%를 제거한다. 카테고리 설명이 나머지 대부분을 제거한다. 전체 콘텐츠 로딩이 규칙이 아니라 예외이다.

운영 시스템에 걸쳐 측정된, progressive disclosure는 모든 스킬 정의를 미리 로드하는 것에 비해 **85–95%**만큼 토큰 오버헤드를 줄인다. Anthropic 자신의 에이전트 스킬 구현이 이를 입증한다: 17개의 운영 스킬이 휴면 상태에서 약 1,700 토큰을 소비하고 (레벨 0 + 레벨 1), 호출 시에만 전체 콘텐츠로 확장된다.

## 5.5 Skill Graph

Heinrich의 Skill Graph 아키텍처 (arscontexta, 2025–2026)는 progressive disclosure를 네트워크 구조로 확장한다. 카테고리로 조직된 스킬의 평면 목록이 아니라, 스킬 그래프는 **wikilink로 연결된 상호 연결된 markdown 파일의 네트워크**이며, 각 노드는 다음을 가진다:

- 간결한 설명을 가진 YAML frontmatter 블록 (레벨 1에서의 스캐닝을 위해)
- 관련 스킬, 선행 스킬, 하위 스킬에 대한 wikilink
- 독립적으로 로드될 수 있는 구조화된 섹션

그래프 구조는 평면 스킬 목록이 지원할 수 없는 여러 능력을 가능케 한다:

**문맥적 항행.** 한 스킬이 호출될 때, 링크된 스킬들이 동시 로드의 후보가 된다. "deploy" 스킬은 "test," "rollback," "monitor" 스킬에 링크된다 ——같은 카테고리에 있어서가 아니라 운영적으로 인접하기 때문이다.

**의존성 해결.** 스킬은 선행 조건을 선언할 수 있다. 복잡한 스킬을 호출하면 그것이 의존하는 기초 스킬을 자동으로 끌어들인다. 패키지 의존성 해결과 비슷하다.

**부분 로딩.** 스킬이 명확한 섹션으로 구조화되어 있으므로, 시스템은 전체 문서를 로드하지 않고 특정 섹션 (예: 배포 스킬의 "오류 처리" 섹션만)을 로드할 수 있다.

그래프 토폴로지 자체가 지식 표현의 한 형태가 된다. 조밀하게 연결된 스킬 클러스터는 높은 내부 일관성을 가진 능력 영역을 가리킨다. 고립된 스킬은 시스템 커버리지의 격차나 통합 기회를 가리킬 수 있다.

## 5.6 SkillReducer 논문

2026년 3월에 발표된 한 연구는 여러 에이전트 플랫폼에 걸친 55,315개 스킬을 조사하여, 스킬 품질에 대한 순진한 가정에 도전하는 발견을 산출했다:

- **스킬의 26.4%가 라우팅 설명을 완전히 결여했다.** 그것들은 전체 지시 콘텐츠는 가졌지만 라우팅 시스템이 언제 호출할지 식별하는 데 도움이 되는 메타데이터가 없었다. 이 스킬들은 정확한 이름으로만 트리거될 수 있었다 ——어떤 지능적 라우팅 계층에도 보이지 않는다.

- **스킬 본문 콘텐츠의 60% 이상이 실행 불가능했다.** 그것은 모델이 실행할 수 있는 구체적 지시가 아니라 배경 context, 동기, 주의, 설명 텍스트로 구성되어 있었다. 이 콘텐츠는 작업 성능에 기여하지 않으면서 토큰을 소비했다.

- **압축된 스킬이 원본보다 출력 품질을 2.8% 개선했다.** 연구자들이 실행 불가능한 콘텐츠를 벗기고 지시 언어를 다지자, 모델 성능이 실제로 개선되었다. 적은 것이 더 많았다 ——context의 줄어든 노이즈가 모델로 하여금 실행 가능한 지시에 집중할 수 있게 했다.

스킬 저작에 대한 함의는 직접적이다:

1. **모든 스킬은 라우팅 설명이 필요하다.** 그것 없이는 스킬이 progressive disclosure 시스템에 사실상 보이지 않는다.
2. **지시 콘텐츠는 조밀하고 실행 가능해야 한다.** 배경 context는 context window에 주입되는 스킬 본문이 아니라 문서에 속한다.
3. **스킬 품질 측정은 토큰 효율을 포함해야 한다** ——단지 "그것이 작동하는가"가 아니라 "소비된 토큰당 작동하는가."

## 5.7 MCP를 위한 Meta-Tool 패턴

Model Context Protocol (MCP)은 에이전트가 제공자 전반에 걸쳐 도구를 발견하고 호출하는 표준화된 방법을 도입했다. 그러나 MCP의 원래 설계는 연결 시점에 모든 사용 가능한 도구 스키마를 로드하여, 스킬이 직면하는 같은 스케일링 문제를 만들었다.

Meta-tool 패턴은 두 구성 요소로 이를 푼다:

- **Discovery Tool:** 자연어 설명을 받아 전체 레지스트리에서 관련 도구 스키마를 반환하는 단일 도구. 이것이 기준에서 로드되는 유일한 도구이다.
- **Execution Tool:** 발견을 통해 스키마가 검색된 후 어떤 도구도 이름으로 호출할 수 있는 일반 도구 호출 래퍼.

시스템은 수백 개 대신 두 개의 도구 스키마를 로드한다. 모델이 능력이 필요하다고 결정하면, discovery tool을 호출하고, 관련 스키마를 받고, 그 다음 특정 도구를 호출한다. 이 패턴은 한 번의 추가 추론 라운드 트립을 거대한 context 절감과 거래한다.

이는 도구 관리에 적용된 progressive disclosure이다: 모델은 모든 연락처 파일의 내용이 아니라 전화번호부를 받는다.

## 5.8 저작 가이드라인

SkillReducer 발견과 운영 경험에서 도출하여, 스킬 저작 모범 사례 세트가 부상했다:

- **라우팅 설명을 앞에 두라.** YAML frontmatter 설명은 파일에서 가장 중요한 줄이다. 그것은 스킬이 호출될지 여부를 결정한다. 인간 독자가 아니라 분류기를 위해 그것을 작성하라.
- **실행 가능한 지시를 앞에 두라.** 스킬 본문의 첫 200 토큰은 핵심 행동 지시를 담아야 한다. 배경과 context는 뒤따라야 한다.
- **구조화된 섹션을 사용하라.** 헤더, 목록, 명확한 구분이 부분 로딩과 섹션 레벨 검색을 가능케 한다.
- **의존성을 명시적으로 선언하라.** 스킬이 다른 스킬이나 도구가 사용 가능하다고 가정한다면, 메타데이터에 그것을 명시하라.
- **트리거 예제를 포함하라.** 스킬을 활성화해야 하는 3–5개의 예제 사용자 메시지를 제공하라. 이들은 라우팅 계층을 위한 문서이자 테스트 케이스 역할을 한다.
- **토큰 비용을 측정하라.** 각 스킬의 토큰 수를 추적하고 예산을 설정하라. 스킬이 2,000 토큰을 넘으면, 분할되거나 압축될 수 있는지 고려하라.

## 5.9 산업 수렴: Google Agent Skills 사양 (2026년 4월)

2025년 대부분 동안, progressive disclosure는 주로 Anthropic 컨벤션이었다 ——2025년 10월의 Claude Code 스킬과 12월의 agentskills.io 오픈 표준을 통해 형식화되었다. **2026년 4월**, Google Developers Blog는 자체 **Agent Skills Spec**을 형식화하며, 같은 아키텍처를 채택하고 확장했다. 사양은 progressive disclosure의 세 가지 명시적 레벨을 기술한다:

- **레벨 1 —— 메타데이터 (스킬당 ~100 토큰).** 스킬의 이름, 한 줄 설명, 트리거 힌트, 버전을 담은 컴팩트한 기술자. 모든 사용 가능한 스킬에 대한 레벨 1 메타데이터가 에이전트의 기준 context에 자리한다. 10개 스킬이 로드되면, 이는 약 1,000 토큰의 일정한 오버헤드이다.
- **레벨 2 —— 지시 (<5K 토큰).** 스킬을 위한 전체 행동 지시이며, 레벨 1 매칭이 스킬을 관련 있다고 식별할 때 요청 시 로드된다. 레벨 2 콘텐츠는 스킬이 실제로 선택될 때까지 context에 들어가지 않는다.
- **레벨 3 —— 외부 자원.** 완전히 context window 밖에 사는 자산 ——참조 문서, 데이터셋, 도구 스키마, 코드 샘플 —— 이며, 실행 도중 스킬이 명시적으로 그것들을 요구할 때만 가져온다.

헤드라인 효율성 주장: 10개 스킬을 가진 에이전트의 경우, 기준 context 사용은 약 **10K 토큰** (전체 스킬 콘텐츠를 미리 로딩)에서 약 **1K 토큰** (레벨 1 메타데이터만)으로 떨어진다. 즉 **90% 감소**. 레벨 2 콘텐츠는 한 번에 한 스킬씩 로드되고, 레벨 3 자원은 실행 중 필요할 때만 로드된다.

두 디테일이 Google 사양을 숫자를 넘어 주목할 만하게 한다:

1. **그것은 보편 `agentskills.io` 사양을 사용한다.** 분기하는 대신, Google은 형식을 Anthropic이 2025년 12월에 발표한 오픈 표준에 정렬시켰다. 한 사양에 대해 저작된 스킬은 다른 플랫폼의 에이전트가 최소 적응으로 소비할 수 있다.
2. **그것은 progressive disclosure를 컨벤션에서 형식적 시스템 설계 패턴으로 끌어올린다.** 약 1년 동안, progressive disclosure는 "Anthropic이 스킬로 하는 일"로 기술되었다. Google의 채택과 형식화로, 그것은 명명된 아키텍처와 측정 가능한 목표를 가진 크로스벤더 산업 패턴이 된다 ——"MVC"나 "REST"가 특정 구현에서 범용 패턴으로 진화한 것에 비견할 만하다.

실용적 효과는 스킬 라이브러리가 제공자 전반에 걸쳐 이식 가능해지고, "기준 에이전트 context가 얼마나 많은 토큰을 소비하는가"가 벤더들이 경쟁하는 1급 지표가 된 것이다.

---

## Sources

- **Anthropic.** "Claude Code Skills." Documentation and open standard specification, October 2025 (launch), December 2025 (open standard via agentskills.io). 87K+ GitHub stars by early 2026.
- **OpenAI.** "Agent Design Best Practices." OpenAI documentation, 2025. Recommendation of fewer than 20 tools per agent, accuracy degradation past 10.
- **Heinrich (@arscontexta).** Skill Graphs concept and implementation. X posts (2026): [https://x.com/arscontexta/status/2023957499183829467](https://x.com/arscontexta/status/2023957499183829467) (Skill Graphs > SKILL.md). GitHub: [https://github.com/agenticnotetaking/arscontexta](https://github.com/agenticnotetaking/arscontexta) --- Claude Code plugin generating individualized markdown-graph knowledge systems with wikilinks and YAML frontmatter scanning. Secondary analysis: Linas Substack, "Skill Graphs: The Architecture That Solves the AI Agent Context Window Problem." [https://linas.substack.com/p/skill-graphs](https://linas.substack.com/p/skill-graphs)
- **SkillReducer Paper.** "Less Is More: Compressing Agent Skills for Improved Performance." March 2026. 55,315 skills analyzed, 26.4% lacking routing descriptions, 60%+ non-actionable content, 2.8% quality improvement from compression.
- **Model Context Protocol (MCP).** Anthropic specification, 2024-2025. Standardized tool discovery and invocation protocol.
- **awesome-llm-skills.** Community collection on GitHub. Curated skill libraries across platforms.
- **awesome-agent-skills.** GitHub collection, 1,000+ skills from official platform teams.
- **awesome-claude-code.** GitHub collection. Claude Code-specific skills and configurations.
- **OpenAI.** "Function Calling Best Practices." 2025. Empirical data on tool count vs. accuracy tradeoffs.
- **Griciūnas, Aurimas.** "State of Context Engineering in 2026." SwirlAI Newsletter, March 2026. [https://www.newsletter.swirlai.com/p/state-of-context-engineering-in-2026](https://www.newsletter.swirlai.com/p/state-of-context-engineering-in-2026) --- Progressive disclosure / compression / sliding window patterns; meta-tool pattern. See also "Breaking Down Context Engineering": [https://www.newsletter.swirlai.com/p/breaking-down-context-engineering](https://www.newsletter.swirlai.com/p/breaking-down-context-engineering)
