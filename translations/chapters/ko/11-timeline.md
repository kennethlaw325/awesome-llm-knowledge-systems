<!-- translation-sync:start -->
> 2026-10-31 영문판과 동기화한 기계 보조 번역입니다. 구조와 내용을 검토했습니다. 코드와 도표 라벨은 원문을 유지하며 읽기 시간은 영어 원문 기준 추정치입니다.
> [English source](../../../chapters/11-timeline.md) · [Sync record](../../SYNC.md)
<!-- translation-sync:end -->

<a id="chapter-11-key-moments-in-llm-knowledge-engineering"></a><!-- i18n-anchor -->

# 11장: LLM 지식 엔지니어링의 주요 순간

> **한 문장으로:** 2022년부터 2026년까지 LLM 지식 엔지니어링의 형성에 영향을 준 주요 순간을 시간순으로 기록한다.
>
> **왜 중요한가:** 이 가이드의 모든 내용을 이해하는 배경이다. 언제 일어났고, 누가 했으며, 무엇이 달라졌는지를 보여 준다.
>
> **읽는 시간:** ~101분 (23,198단어 / 분당 230단어)

*그림: 이 장의 주요 항목 중 열네 개를 마지막 절 '패턴'이 연표에서 읽어 낸 네 시기로 묶었다. 여기서는 루프 및 그래프 엔지니어링의 전개를 별도로 보여 주기 위해 2026년을 상반기와 하반기로 나눴다. 각 시기의 행은 왼쪽에서 오른쪽으로 읽는다. 위에서 아래로 이어지는 논지는 각 시기의 관심 대상이 모델 자체에서 그 주위에 구축한 컨텍스트 창과 프로토콜로, 하네스로, 그리고 그 위에 구축한 루프와 그래프로 옮겨 간다는 것이다. 2026 H2는 아직 결론 나지 않은 부분이다. 그래프 엔지니어링은 정착된 분야가 아니라 부상하는 분야로 추적하며, September 15 항목은 이 장에서 판정이 갈린 게이트 결과를 보고하는 대목이다. 가로 포스터 버전은 [diagrams/timeline.svg](../../../diagrams/timeline.svg)에 있다.*

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryColor':'#eef1f4','primaryTextColor':'#1f2328','primaryBorderColor':'#8c959f','lineColor':'#6b7280','tertiaryColor':'#f6f8fa','clusterBkg':'#f9fafb','clusterBorder':'#8c959f','edgeLabelBackground':'#ffffff'}}}%%
flowchart TB
    subgraph P1["2022-2023"]
      direction LR
      E01["<b>November 30, 2022</b><br/>ChatGPT launches<br/>and prompt<br/>engineering begins"]
      E02["<b>Q1-Q2 2023</b><br/>RAG frameworks<br/>emerge, LangChain<br/>and LlamaIndex"]
      E03["<b>November 2023</b><br/>GPT-4 Turbo<br/>ships a 128K<br/>window"]
      E01 --> E02
      E02 --> E03
    end
    subgraph P2["2024"]
      direction LR
      E04["<b>February 2024</b><br/>Gemini 1.5 reaches<br/>1M token context"]
      E05["<b>November 2024</b><br/>Anthropic releases<br/>the Model Context<br/>Protocol"]
      E04 --> E05
    end
    subgraph P3["2025"]
      direction LR
      E06["<b>January 2025</b><br/>DeepSeek R1,<br/>the open-source<br/>inflection"]
      E07["<b>Mid-2025</b><br/>Context<br/>engineering enters<br/>the lexicon"]
      E08["<b>October 2025</b><br/>Anthropic<br/>launches Agent<br/>Skills"]
      E06 --> E07
      E07 --> E08
    end
    subgraph P4["2026 H1"]
      direction LR
      E09["<b>April 3, 2026</b><br/>AI Velocity<br/>Paradox report<br/>lands"]
      E10["<b>April 14, 2026</b><br/>Claude Code<br/>Routines research<br/>preview"]
      E11["<b>June 7, 2026</b><br/>Loop engineering<br/>gets its name"]
      E09 --> E10
      E10 --> E11
    end
    subgraph P5["2026 H2"]
      direction LR
      E12["<b>July 17-18, 2026</b><br/>Graph engineering<br/>gets its name"]
      E13["<b>August 6, 2026</b><br/>Paperclip skill<br/>supply-chain<br/>campaign"]
      E14["<b>September 15, 2026</b><br/>Chapter 14<br/>survival gate<br/>comes due"]
      E12 --> E13
      E13 --> E14
    end
    P1 --> P2
    P2 --> P3
    P3 --> P4
    P4 --> P5
    class E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11 stable
    class E12,E13,E14 accent
classDef stable fill:#eef1f4,stroke:#8c959f,stroke-width:1.5px,color:#1f2328
classDef accent fill:#dbeafe,stroke:#2563eb,stroke-width:1.5px,color:#0b3a8f
classDef muted fill:#f6f8fa,stroke:#adb5bd,stroke-width:1.5px,color:#57606a
classDef gate fill:#ffffff,stroke:#2563eb,stroke-width:1.5px,color:#0b3a8f
```

대규모 언어 모델로 지식 시스템을 구축하는 방식에 영향을 준 사건, 출시, 아이디어를 시간순으로 정리한 지도다. 정확한 날짜를 아는 경우 날짜를 적고, 분기나 월만 확인된 경우에는 그 수준으로 표시한다.

이것은 모든 사건을 망라한 연표가 아니라 **선별한** 연표다. 이 프레임워크가 추적하는 기본 요소, 패턴, 서사적 전환점을 도입하거나 검증하거나 실제 운영으로 옮긴 사건만 목록에 포함한다. 모델 버전 갱신, 투자 유치, 특정 산업용 제품 등 주목할 만한 여러 발표를 의도적으로 제외했다. 전체 수록 기준은 [CONTRIBUTING.md](../../../CONTRIBUTING.md)를 참조하라.

---

## 2022

<a id="november-30-chatgpt-launches"></a><!-- i18n-anchor -->

### November 30 --- ChatGPT 출시

OpenAI가 GPT-3.5와 대화하는 인터페이스인 ChatGPT를 출시한다. 두 달 안에 사용자 100백만 명에 도달하며 역사상 가장 빠른 소비자 기술 보급을 기록한다. 사용자들이 무엇을 묻느냐만큼 어떻게 묻느냐도 중요함을 발견하면서 "prompt engineering" 시대가 시작된다.

---

## 2023

<a id="q1-q2-the-rag-frameworks-emerge"></a><!-- i18n-anchor -->

### Q1-Q2 --- RAG 프레임워크의 등장

**LangChain**과 **LlamaIndex**가 LLM 애플리케이션을 구축하기 위한 초기 개발자 프레임워크로 빠르게 보급된다. 검색 증강 생성(RAG)이 외부 지식에 근거한 LLM 응답을 만드는 표준 패턴이 된다. 구조는 간단하지만 큰 변화를 일으킨다. 관련 문서를 검색하고, 프롬프트에 주입하고, 근거 있는 응답을 생성한다. 처음으로 LLM이 학습한 적 없는 비공개 데이터에 관한 질문에 답할 수 있게 된다.

<a id="november-gpt-4-turbo-and-the-128k-context-window"></a><!-- i18n-anchor -->

### November --- GPT-4 Turbo와 128K 컨텍스트 창

OpenAI가 DevDay에서 128K 토큰 컨텍스트 창을 갖춘 GPT-4 Turbo를 발표한다. GPT-4의 32K 창보다 4x 확장되면서 지식 검색의 비용 구조가 달라진다. 이제 문서 전체를 컨텍스트에 넣을 수 있어 일부 용도에서는 청킹과 검색의 필요가 줄어든다. "just put it all in context"라는 사고방식이 형성되기 시작한다.

<a id="december-gemini-10-launch"></a><!-- i18n-anchor -->

### December --- Gemini 1.0 출시

Google이 자사의 첫 네이티브 멀티모달 모델인 Gemini 1.0을 출시한다. 처음부터 텍스트, 이미지, 오디오, 비디오를 처리하도록 구축한 이 모델은 지식 엔지니어링이 텍스트 이상을 다뤄야 함을 예고한다.

---

## 2024

<a id="february-gemini-15-and-the-1m-token-context-window"></a><!-- i18n-anchor -->

### February --- Gemini 1.5와 1M 토큰 컨텍스트 창

Google이 1백만 토큰 컨텍스트 창을 갖춘 Gemini 1.5 Pro를 출시한다. 이는 점진적 개선이 아니라 패러다임의 전환이다. 코드베이스 전체, 책 한 권, 여러 시간 분량의 영상 전사문을 이제 하나의 프롬프트에 넣을 수 있다. "RAG vs. long context" 논쟁이 격화된다. 실무자들은 긴 컨텍스트가 검색을 없애는 것이 아니라 검색의 목적을 바꾼다는 사실을 깨닫기 시작한다.

<a id="march-kimi-achieves-2m-chinese-character-context"></a><!-- i18n-anchor -->

### March --- Kimi, 중국어 2M자 컨텍스트 달성

Moonshot AI의 Kimi가 중국어 2백만 자 컨텍스트 창에 도달한다. 중국어 텍스트에 최적화된 모델 중 가장 길다. 이로써 법률 계약서, 규제 제출 서류, 기술 매뉴얼 등 이전에는 비현실적이었던 중국 기업용 활용에서 문서 전체를 처리할 수 있게 된다.

<a id="november-anthropic-releases-the-model-context-protocol-mcp"></a><!-- i18n-anchor -->

### November --- Anthropic, Model Context Protocol(MCP) 공개

Anthropic이 LLM을 외부 도구 및 데이터 소스에 연결하는 공개 명세로 MCP를 발표한다. MCP는 모델이 도구를 발견하고 인증하고 호출하는 방식을 표준화하여 제각각이던 맞춤 함수 호출 구현을 대체한다. 제품이 아닌 프로토콜로 설계되었으므로 어떤 모델 공급업체나 도구 개발자도 구현할 수 있다. USB나 HTTP에 빗대는 것은 의도적이다. 이 순간은 상호 운용 가능한 지식 인프라의 시작을 알린다.

---

## 2025

<a id="january-deepseek-r1-and-the-open-source-inflection"></a><!-- i18n-anchor -->

### January --- DeepSeek R1과 오픈소스의 전환점

DeepSeek가 MIT 라이선스의 공개 가중치 추론 모델 R1을 출시하며, 일부 벤치마크에서 OpenAI o1에 필적하는 결과를 보고한다. 이 출시로 자체 호스팅 지식 시스템에서도 추론 모델을 사용할 수 있게 된다. 널리 인용되는 $6백만 미만이라는 수치는 [DeepSeek-V3 기술 보고서](https://arxiv.org/abs/2412.19437)의 수치다. 이 보고서는 공식 학습 실행 비용을 $5.576백만으로 추산하며 이전 연구 및 절제 실험은 제외한다. R1의 전체 개발 비용이 아니다. 모델, 라이선스, 보고된 평가는 [공식 R1 저장소](https://github.com/deepseek-ai/DeepSeek-R1)를 참조하라.

<a id="mid-2025-context-engineering-enters-the-lexicon"></a><!-- i18n-anchor -->

### 2025년 중반 --- "Context Engineering"이라는 용어의 등장

Andrej Karpathy가 **"context engineering"**을 "prompt engineering,"의 대체 용어로 공개 지지하며, 이 분야가 개별 프롬프트를 다듬는 수준을 훨씬 넘어섰다고 주장한다. 이 변화는 더 넓은 인식을 반영한다. 중요한 것은 프롬프트 하나가 아니라 무엇을 언제 어떤 순서로 왜 불러오는지 결정하는 컨텍스트 구성 파이프라인 전체라는 것이다. 커뮤니티는 이 관점을 빠르게 받아들인다.

<a id="july-manus-publishes-context-engineering-lessons"></a><!-- i18n-anchor -->

### July --- Manus, 컨텍스트 엔지니어링의 교훈 발표

자율 에이전트 스타트업 Manus가 자사의 컨텍스트 엔지니어링 접근법을 상세히 설명한 블로그 글을 발표한다. 핵심 통찰로는 작업이 완료되면서 자연스럽게 줄어드는 "todo list"로 컨텍스트 창을 유지하기, 파일 시스템 연산을 확장 메모리로 사용하기, 그리고 "context engineering is the art of delivering the right information in the right format at the right time."라는 원칙의 중요성 등이 있다. 이 글은 실무자들의 참고 문서가 된다.

<a id="september-notion-30-the-ai-agent-rebuild"></a><!-- i18n-anchor -->

### September --- Notion 3.0: AI 에이전트를 위한 재구축

Notion이 처음부터 AI 네이티브 작업 공간으로 재구축한 3.0 버전을 출시한다. 데이터베이스, 페이지, 관계라는 핵심 지식 관리 기능을 AI 에이전트와 매끄럽게 작동하도록 다시 설계한다. 이는 단일 제품 출시로서보다 주류 생산성 도구들이 구조화된 지식 + 에이전트 오케스트레이션 + 컨텍스트 엔지니어링이라는 지식 하네스 패턴으로 수렴한다는 증거로서 중요하다.

<a id="october-anthropic-launches-agent-skills"></a><!-- i18n-anchor -->

### October --- Anthropic, Agent Skills 출시

Anthropic이 Claude용 스킬 시스템을 도입하여, 에이전트가 발견하고 호출할 수 있는 재사용 가능하고 조합 가능한 역량을 사용자가 정의할 수 있게 한다. 스킬은 트리거, 매개변수, 의존성을 정의하는 YAML 프런트매터가 붙은 마크다운 파일로 구성된다. 이는 고급 사용자들이 비공식적으로 구축하던 재사용 가능한 에이전트 행동 라이브러리 패턴을 공식화한다.

<a id="november-mcp-crosses-8m-downloads"></a><!-- i18n-anchor -->

### November --- MCP, 다운로드 8M 돌파

Model Context Protocol의 SDK 다운로드가 8백만 건에 도달한다. 열두 달 전에는 거의 영에 가까웠다. 이 프로토콜은 주요 모델 공급업체 전체와 수백 개의 도구 서버에서 구현되며 LLM과 도구를 통합하는 사실상의 표준이 된다.

<a id="december-a-defining-month"></a><!-- i18n-anchor -->

### December --- 결정적인 한 달

2025년 십이월에 여러 변화가 맞물린다.

- **Anthropic이 agentskills.io에 스킬의 공개 표준을 발표**하며, 어떤 플랫폼도 구현할 수 있는 에이전트 역량의 공통 형식을 제안한다.
- **MCP가 Linux Foundation에 기증되어** 오픈소스 커뮤니티가 유지하는 공급업체 중립 프로토콜로서 입지를 굳힌다.
- **점진적 공개**가 주요 플랫폼에서 스킬 및 컨텍스트 관리의 표준 접근법으로 채택되며, 여러 팀이 독립적으로 개발한 패턴을 검증한다.
- **Meta가 Manus를 약 $2십억에 인수**하며, 자율 에이전트 인프라가 이제 최상위 규모의 전략 자산임을 알린다.

---

## 2026

<a id="january-ernie-50-and-kimi-k25"></a><!-- i18n-anchor -->

### January --- ERNIE 5.0과 Kimi K2.5

- Baidu가 **ERNIE 5.0**을 출시한다. 매개변수 2.4조 개에 단일 모델 안에서 텍스트, 이미지, 오디오, 비디오를 처리하는 네이티브 완전 멀티모달 기능을 갖춘다.
- **Kimi K2.5**가 Agent Swarm을 도입한다. 하나의 질의로 최대 100개의 하위 에이전트를 생성하여 약 1,500번의 도구 호출을 통해 협업하게 할 수 있다. 이는 데모가 아니라 복잡한 다단계 연구 작업을 위한 실제 운영 기능이다.

<a id="february-heinrichs-skill-graphs-post"></a><!-- i18n-anchor -->

### February --- Heinrich의 스킬 그래프 글

Heinrich(`@arscontexta`)가 그래프 구조로 에이전트 스킬을 구성하고 조합하며 스킬 간 경로를 선택하는 방법을 다룬 글이 2026년 초 큰 관심을 끌며 더 넓은 AI 엔지니어링 독자층으로 퍼졌다. 이러한 반응은 실무자 커뮤니티가 모델 역량만이 아니라 아키텍처 패턴에도 갈증을 느낀다는 것을 보여 준다. 스킬 라우팅과 조합이 핵심 엔지니어링 과제로 떠오른다. 원문: [https://x.com/arscontexta/status/2023957499183829467](https://x.com/arscontexta/status/2023957499183829467).

<a id="march-the-research-papers"></a><!-- i18n-anchor -->

### March --- 연구 논문들

중요한 논문 두 편이 발표된다.

- **"Meta-Harness"**는 동일한 기반 모델을 사용하더라도 단순한 하네스와 잘 설계한 하네스 사이에 6x 성능 차이가 있음을 입증한다. 이 논문은 운영용 지식 시스템에서 하네스 엔지니어링이 모델 선택보다 중요하다는 실증적 증거를 제시한다.
- **"SkillReducer"**는 스킬이 급증하면서 생기는 문제를 다루며, 자동 중복 제거, 군집화, 계층적 구성을 통해 55,000개 이상의 스킬을 가진 시스템을 관리하는 기법을 제안한다.

<a id="q1-mcp-at-scale"></a><!-- i18n-anchor -->

### Q1 --- 대규모로 확산된 MCP

MCP의 월간 SDK 다운로드가 97백만 건에 도달한다. 2025년 십일월보다 12x 증가한 수치다. 이제 이 프로토콜은 CI/CD 파이프라인, IDE 확장, 기업 플랫폼, 소비자 애플리케이션에 내장된다. 한 모델용으로 작성한 도구 서버가 어떤 모델과도 작동한다는 상호 운용성의 약속이 실현되고 있다.

<a id="april-2026-initial-publication"></a><!-- i18n-anchor -->

### April 2026 --- 최초 발행

이 연구 보고서가 발행된다. 앞선 네 해 동안의 급속한 발전을 실무자를 위한 일관된 프레임워크로 종합하려는 시도다. 이 분야는 어떤 단일 문서로도 담아낼 수 없을 만큼 빠르게 계속 진화한다.

<a id="march-31-2026-claude-code-source-leak"></a><!-- i18n-anchor -->

### March 31, 2026 --- Claude Code 소스 유출

Anthropic이 npm 패키지 `@anthropic-ai/claude-code` v2.1.88에 59.8MB 소스 맵을 실수로 포함해 공개하면서, 1,906개 파일에 걸쳐 약 513,000줄의 난독화되지 않은 TypeScript가 노출된다. 유출 자료에는 `MEMORY.md`가 전체 저장소가 아니라 가벼운 포인터형 인덱스로 작동하는 삼계층 **"Self-Healing Memory"** 아키텍처가 드러난다. 또 소스에서 150번 이상 언급되는 자율 데몬 모드인 **KAIROS** 기능 플래그와 미출시 역량을 위한 다른 숨겨진 기능 플래그 44개도 드러난다. Anthropic은 이 사건을 "human packaging error, not a security breach."라고 설명한다. 그렇더라도 유출 자료는 실제 운영 하네스에 무엇이 들어 있는지 처음으로 실증적으로 보여 준다. 이후 며칠 동안 공급업체 마케팅과 채용 공고에 "harness engineering"이라는 용어가 등장하기 시작한다. (사월의 맥락을 설명하기 위해 여기에 수록한다.)

<a id="april-2026-the-open-source-harness-builder-wave"></a><!-- i18n-anchor -->

### April 2026 --- 오픈소스 하네스 구축 도구의 물결

2026년 사월, 하네스가 해자라는 논지는 양방향으로 작용했다. 실무자 용어가 채용 공고에 자리 잡는 동안 대규모 재작성을 거친 프로젝트 하나와 신생 프로젝트 하나, 두 오픈소스 프로젝트가 10K 스타를 빠르게 넘어서며 이 분야에 처음으로 널리 채택되는 참조 구현을 제공했다. **Archon**(`coleam00/Archon`, MIT 라이선스, 최초 출시 2025년 이월)은 사월에 TypeScript / Bun으로 재작성한 **v2.1**을 내놓았다. Claude Code와 OpenAI Codex CLI를 YAML로 정의한 방향성 비순환 워크플로로 감싸 AI 코딩을 "deterministic and repeatable."하게 만들고자 한다. 이달 GitHub 스타 19K를 넘었다. **OpenHarness**(`HKUDS/OpenHarness`, MIT 라이선스, 첫 커밋 April 1, 2026)는 Hong Kong University of Science Data 랩에서 나온 공개 Python 구현이다. 스킬 시스템, MCP HTTP 전송, 스웜 폴링 등 에이전트 하네스 내부에 집중하며, 개인 에이전트 데모("Ohmo!")를 내장한다. 처음 세 주 만에 스타 11K를 넘었다. 이 흐름을 함께 보면 개별 기능보다 하네스 계층에 커뮤니티 주도 오픈소스의 구심력이 생겼다는 신호가 더 중요하다. 이는 2023년의 RAG 프레임워크(LangChain, LlamaIndex)가 지식 계층에 제공했던 것과 같은 힘이다. 향후 열두 달의 하네스 엔지니어링은 이들과 유사한 프로젝트에서 공개적으로 전개될 가능성이 크다.

<a id="april-2-2026-microsoft-mai-models-launch"></a><!-- i18n-anchor -->

### April 2, 2026 --- Microsoft MAI 모델 출시

Microsoft가 Foundry를 통해 자사 멀티모달 기반 모델 세 개, **MAI-Transcribe-1**, **MAI-Voice-1**, **MAI-Image-2**를 출시한다. 세 모델 모두 가드레일과 기업 수준 거버넌스를 내장한다. 이는 Microsoft가 OpenAI 기술의 유통업체 역할을 넘어 모델 공급업체로서 멀티모달 기반 모델 시장에 본격적으로 진출한 첫 사례다. 음성, 전사, 이미지 생성에서 OpenAI, Google, Anthropic과 직접 경쟁하게 된다. 이것들은 안전 하네스가 아니라 멀티모달 모델이다.

<a id="april-3-2026-the-ai-velocity-paradox-report"></a><!-- i18n-anchor -->

### April 3, 2026 --- AI Velocity Paradox 보고서

Harness.io와 Infosys가 **"State of DevOps 2026"** 보고서를 공동 발행한다. 핵심 결과는 **AI 보조 코딩이 45% 빨라졌음에도 팀의 69%가 배포 병목을 보고한다**는 것이다. 보고서는 이를 "AI Velocity Paradox"로 규정한다. 생성 속도는 더 이상 제한 요인이 아니지만 평가, 검토, 거버넌스가 따라오지 못한다는 뜻이다. 새로운 병목에 관한 논의의 중심이 "generation speed"에서 "evaluation and governance"로 옮겨 가기 시작한다.

<a id="april-5-2026-mempalace-and-spatial-metaphor-memory"></a><!-- i18n-anchor -->

### April 5, 2026 --- MemPalace와 공간 은유 기반 메모리

에이전트 메모리 아키텍처 경쟁에 큰 화제를 모은 주자가 등장했다. **MemPalace**(`MemPalace/mempalace`, MIT 라이선스, 첫 커밋 April 5, 2026)는 의도적으로 고전적인 관점으로 출발한다. 기억술 전문가들이 이천 년간 사용해 온 고전적인 *장소법*을 본떠 메모리 저장소를 **별관 → 방 → 옷장 → 서랍이라는 공간적 계층**으로 구성한다. 말단의 각 "drawer"에는 원문 텍스트 조각을 그대로 저장하며, 계층을 탐색하는 행위 자체가 인덱스 역할을 한다. 프로젝트의 표어("the best-benchmarked open-source AI memory system")는 에이전트 메모리의 맥락 회상을 위한 가장 오래 발표되어 온 벤치마크 LongMemEval에서 **Recall@5 96.6%**를 기록했다는 보고로 뒷받침된다. 커뮤니티 반응도 두드러져 **세 주 만에 GitHub 스타 약 49,000개**를 모았다. 이는 규모 면에서 다른 프로젝트보다 약 열 배 차이가 날 정도로, 2026년 가장 빠르게 성장한 메모리 프로젝트다. 개념적으로 이 아키텍처는 Mem0ᵍ(그래프 삼중항), Titans(학습 가능한 신경 모듈), ByteRover(계층형 마크다운 트리)와 별개다. MemPalace는 *원문 우선* 저장을 사용하는 *공간적* 은유 자체가 검색의 기본 요소이며, "remembering where you put it"의 인지적 편의성이 임베딩 유사도만큼 중요하다고 주장한다. 그달이 끝나기 전 이미 학술 비평(arXiv 2604.21284, *"Spatial Metaphors for LLM Memory: A Critical Analysis of the MemPalace Architecture"*)이 유통되고 있었다. 이 역시 프로젝트가 얼마나 빨리 이 분야의 핵심 논의로 진입했는지 보여 주는 신호다.

### April 7, 2026 --- Claude Mythos Preview

Anthropic이 **Claude Mythos Preview**(Claude 4.6이 아님)를 공개한다. **SWE-bench Verified에서 93.9%**로 Opus 4.6의 80.8%보다 13.1점 높으며, SWE-bench Pro에서는 77.8%를 기록한다. Mythos는 일반에 공개되지 않는다. 사이버보안 연구를 위한 **Project Glasswing** 연합(Apple, Google, Microsoft, Amazon 등) 전용이며, 허용 목록에 오른 약 40개 팀이 입력 / 출력 토큰 백만 개당 $25 / $125에 접근한다. Anthropic이 주력 등급 모델을 공개 프리뷰 대신 연구 연합으로 제한한 첫 사례다.

Glasswing 프로그램을 공개 발표한 뒤 약 14시간 안에 Anthropic은 "through one of our third-party vendor environments." Claude Mythos Preview에 무단 접근이 있었다고 밝혔다. 이 침해 사건이 하네스 논의에서 중요한 이유는 두 가지다. 첫째, "harness as security perimeter"가 실제로 무엇을 뜻하는지 구체적으로 보여 준다. 모델 자체가 침해된 것이 아니라 Glasswing 접근을 제한하던 외부 공급업체 스택, 즉 *배포 하네스*가 침해되었다. 둘째, Mythos의 사이버 방어 논지가 뒤집힐 가능성을 예고한다. 방어자를 위해 취약점을 찾는 것이 명시된 역할인 모델이 정작 자신을 제공하는 공급망을 통해 접근 가능했던 것이다.

검증된 연합에 이중 용도 AI를 배포하는 Glasswing 방식은 **May 11, 2026**에 두 번째 사례를 얻었다. OpenAI가 **"Trusted Access for Cyber,"를 적용한 GPT-5.5**를 출시하면서 Advanced Account Security 적용을 의무화하고 EU 파트너 연합(Deutsche Telekom, BBVA, Telefonica, Sophos, Scalable Capital)을 통해 접근 범위를 확대했다. 공급업체를 넘어 같은 패턴이 재현된다는 사실은 이중 용도 AI를 검증된 연합에 배포하는 방식이 이제 일회성 사례가 아니라 업계 관행임을 확인해 준다.

<a id="april-8-2026-anthropic-managed-agents-public-beta"></a><!-- i18n-anchor -->

### April 8, 2026 --- Anthropic Managed Agents(공개 베타)

Anthropic이 장시간 에이전트 작업을 위한 호스팅 런타임 **Claude Managed Agents**를 공개 베타로 출시한다. Advisor Tool(April 2026)이 *무엇을 생각할지*를 제품화하고 Claude Opus 4.7의 작업 예산(April 16)이 *얼마나 깊이 생각할지*를 제품화했다면, Managed Agents는 *루프가 어디서 실행되는지*를 제품화한다. Anthropic 엔지니어링 글은 아키텍처를 세 가지 가상화 구성 요소로 설명한다. **세션**은 일어난 모든 일을 추가만 가능한 로그에 담고, **하네스**는 Claude를 호출하고 도구 호출을 라우팅하는 루프이며, **샌드박스**는 Claude가 코드를 실행하는 환경이다. 그 위에 추적 기능과 Agent / Environment / Session / Events API 인터페이스가 놓인다. SiliconANGLE의 출시 보도는 기반 서비스 가격을 **표준 API 토큰 요금에 에이전트 런타임 시간당 팔 센트를 더한 금액**이라고 전한다. Anthropic의 일차 엔지니어링 글과 문서에는 시간당 금액이 직접 나오지 않으므로 여기서는 이차 기술 매체를 출처로 인용한다. 이 가격 세부 사항이 중요한 이유는 추론과 별개로 *오케스트레이터 실행 자리* 자체에 요금을 부과하는 프런티어 공급업체의 첫 기본 요소이기 때문이다. Manus 인수(2026년 초) 및 Routines(April 14)와 함께 보면 흐름이 명확하다. 2025년에 "the moat"로 묘사하던 하네스 계층이 2026년에는 공급업체가 판매하는 기본 요소로 분해되고 있다. 자체 호스팅 하네스가 사라진 것은 아니지만, 그 범위는 로컬 실행, 한 분 미만 주기, GitHub 이외 트리거, 기기 내 데이터처럼 관리형 기본 요소가 아직 지원하지 않는 작업으로 좁아졌다.

<a id="april-2026-mcp-dev-summit-and-sep-1686-tasks-primitive"></a><!-- i18n-anchor -->

### April 2026 --- MCP Dev Summit과 SEP-1686 Tasks 기본 요소

MCP Dev Summit이 **SEP-1686**, 즉 Tasks 기본 요소를 소개한다. 비동기 MCP 작업을 위해 `working`, `input_required`, `completed`, `failed`, `cancelled`의 다섯 상태를 가진 영속적 작업 상태 머신이다. 각 작업에 이후 알림과 연결할 수 있는 ID를 부여하여 데이터 파이프라인, 코드 마이그레이션, 테스트 실행, 심층 연구 등 장기 워크플로에서 **지금 호출하고 나중에 가져오는 패턴**을 가능하게 한다. SEP-1686은 April 2026 MCP 명세에서 실험적 기능으로 제공되며, 상태 없는 RPC에서 진정한 오케스트레이션 계층으로 나아가는 프로토콜의 첫걸음이다.

<a id="april-2026-amazon-bedrock-agentcore-stateful-mcp"></a><!-- i18n-anchor -->

### April 2026 --- Amazon Bedrock AgentCore의 상태 유지 MCP

Amazon이 최초의 운영용 **양방향 MCP 런타임**인 **Bedrock AgentCore Runtime**을 출시한다. 표준 MCP 인터페이스 위에 서버가 시작하는 두 기능을 추가한다. **정보 요청(elicitation)**은 서버가 워크플로 도중 실행을 멈추고 JSON 스키마에 맞춘 구조화된 입력을 사용자에게 요청하는 기능이다. **샘플링(sampling)**은 서버가 자체 모델 인증 정보를 보유하지 않고 클라이언트에 LLM 완성을 요청하는 기능이다. 두 기능을 통해 양방향 MCP 프로토콜 구현이 완성되며 서버가 대화에 응답만 하는 것이 아니라 일부를 "drive"할 수 있게 된다.

<a id="april-2026-google-agent-skills-spec"></a><!-- i18n-anchor -->

### April 2026 --- Google Agent Skills 명세

Google Developers Blog가 에이전트 스킬의 **삼단계 점진적 공개 아키텍처**를 공식화한다. **L1 메타데이터**는 스킬당 ~100토큰, **L2 지침**은 <5K토큰으로 필요할 때 불러오며, **L3 외부 리소스**는 필요한 경우에만 가져온다. 스킬이 10개인 에이전트의 기본 컨텍스트 사용량은 ~10K토큰에서 ~1K토큰으로 90% 줄어든다. Google은 범용 **agentskills.io** 명세를 채택하여 2025년 십이월에 발표된 Anthropic 표준과 합류하고, 점진적 공개를 Anthropic의 관행에서 여러 공급업체가 공유하는 업계 패턴으로 끌어올린다.

<a id="april-2026-mem0g-graph-memory-goes-production"></a><!-- i18n-anchor -->

### April 2026 --- Mem0ᵍ 그래프 메모리의 실제 운영 도입

Mem0의 방향성 라벨 그래프 변형인 **Mem0ᵍ**가 실제 운영에 도입된다. 아키텍처는 **개체 추출기**에서 **관계 생성기**로 이어지며, `lives_in`, `prefers`, `owns`처럼 유형이 정해진 간선을 사용해 `(source, relation, destination)` 형식의 라벨 삼중항을 만든다. **충돌 탐지기**와 **LLM 기반 갱신 해결기**가 함께 새로운 사실이 들어올 때 발생하는 모순을 처리한다. Mem0ᵍ는 메모리에 질의 가능한 의미 구조를 부여하여 "dump everything into context"와 선택적 검색 방식 사이의 간극을 좁힌다.

<a id="april-2026-anthropic-advisor-tool-beta"></a><!-- i18n-anchor -->

### April 2026 --- Anthropic Advisor Tool 베타

Anthropic이 Claude API에 **Advisor Tool** 베타(`advisor-tool-2026-03-01`)를 출시한다. 이 패턴은 같은 `/v1/messages` 요청 안에서 빠른 실행 모델(Sonnet 또는 Haiku)과 더 강력한 자문 모델(Opus)을 짝짓는다. 실행 모델은 의사결정 지점에서 `advisor()`를 호출한다. Anthropic은 전체 대화 기록을 읽고 400-700토큰의 계획을 반환하는 서버 측 하위 추론을 실행하며, 실행 모델은 그 계획에 따라 행동한다. 이는 최초로 제품화된 **메타 하네스** 기본 요소다. Stanford / MIT / KRAFTON 논문이 2026년 삼월에 입증한 6x 성능 차이를 이제 도구 호출로 활용할 수 있다. 실무자는 다중 모델 협업을 활용하기 위해 연구팀을 둘 필요 없이 도구 항목 하나로 활성화할 수 있다. Anthropic 문서의 초기 지침은 시사적이다. **본격적인 작업 전**에 자문 모델을 호출하고, **완료를 선언하기 전**에 다시 호출하라. 대화당 자문 호출이 대략 세 번이면 캐싱의 이점이 생기며, 짧은 작업에서는 캐싱을 꺼 두는 편이 좋다.

<a id="january-12-2026-mechanistic-interpretability-named-a-breakthrough-technology"></a><!-- i18n-anchor -->

### January 12, 2026 --- 기계적 해석 가능성, 혁신 기술로 선정

MIT Technology Review가 **기계적 해석 가능성**을 2026년의 10대 혁신 기술 중 하나로 선정한다. Anthropic, OpenAI, DeepMind 및 학계 연구진이 이 분야를 "poking models from the outside"에서 가중치 내부의 사람이 이해할 수 있는 회로를 읽는 단계로 발전시켰다고 평가한다. 이 항목은 엄밀한 시간순에서 벗어나 여기에 놓았다. 그 실질적 결과가 구체화된 시점이 해석 가능성이 연구 프로그램에서 운영 도구로 옮겨 간 April 2026이기 때문이다(아래 감정 벡터 및 CoT 모니터링 항목 참조). 지식 엔지니어에게 이는 안전 논의가 정책 논의에서 아키텍처 논의로 바뀐 순간이다. 모델 행동을 유도하는 특성 방향을 식별할 수 있다면, 하네스가 어느 방향을 활성화하거나 억제하거나 감시하도록 허용할지도 결정할 수 있다. 해석 가능성 연구 결과가 사후 분석을 넘어 시스템을 지탱하는 인프라가 될 만한 가능성을 처음 보여 준 것이다.

<a id="april-2026-arc-agi-3-interactive-benchmark"></a><!-- i18n-anchor -->

### April 2026 --- ARC-AGI-3 상호작용 벤치마크

François Chollet과 ARC Prize 팀이 정적 퍼즐 격자에서 상호작용 환경으로 이동한 최초의 ARC 벤치마크 **ARC-AGI-3**(arxiv 2603.24621)를 공개한다. 에이전트는 자연어 지침, 목표 설명, 행동 문서가 전혀 없는 게임 같은 세계에 투입된다. 직접 탐색하고 목표를 추론하고 내부 세계 모델을 구축한 뒤 목표를 추구해야 한다. 평가는 최종 과제 성공뿐 아니라 **탐색 효율성**, **목표 추론**, **세계 모델 형성**을 별도 축으로 보상한다. 기존 에이전트 순위표에서 포화 수준에 이른 프런티어 모델들도 기본 상태에서는 저조한 성과를 낸다. 이는 현재 에이전트 역량의 상당 부분이 자율적 문제 정의보다 지시 이행에 의존함을 드러낸다. 하네스 엔지니어에게 ARC-AGI-3는 "capability"의 의미를 바꾼다. 병목은 더 이상 도구 사용이나 계획의 깊이가 아니라 설명서 없이 이해를 형성해 나가는 하네스의 능력이다.

<a id="april-2026-catts-agentic-test-time-scaling"></a><!-- i18n-anchor -->

### April 2026 --- CATTS: 에이전트의 테스트 시점 확장

사전 공개 논문 "CATTS: Consensus-Aware Test-Time Scaling for Agents"(arxiv 2602.12276, February 2026 제출, April 공개 주기)이 다단계 에이전트의 연산 배분 신호로 **투표에서 도출한 불확실성**을 도입한다. CATTS는 단계마다 동일한 수의 롤아웃을 배정하는 대신 행동별로 작은 위원회를 샘플링해 의견 불일치를 측정한다. 불일치가 큰 단계에는 연산을 더 주고 작은 단계에는 덜 준다. **WebArena-Lite**와 **GoBrowse**에서 균등 확장보다 **+9.1%** 높은 성과를 내면서 토큰은 **2.3x 적게** 사용한다. 이는 테스트 시점 연산을 단일 수치 예산이 아니라 **어디에 집중할지의 문제**로 다룬 최초의 상세한 결과다. 하네스 설계자에게 이는 자문 / 실행 모델 조합(사월 Anthropic 패턴)과 불확실성 기반 롤아웃 예산이 중복이 아니라 상호 보완임을 뜻한다. 하나는 *무엇을 생각할지*, 다른 하나는 *얼마나 깊이 생각할지*를 고른다.

<a id="april-2026-titans-miras-from-google-research"></a><!-- i18n-anchor -->

### April 2026 --- Google Research의 Titans + MIRAS

Google Research가 **Titans + MIRAS**를 발표한다. 메모리를 모델에 붙인 벡터 저장소가 아니라 온라인으로 기억하는 법을 학습하는 **학습 가능한 신경 모듈**로 만드는 아키텍처 계열이다. 메모리 모듈은 추론 시 경사 하강법으로 갱신되므로 모델은 문서를 처리하면서 문자 그대로 자기 가중치를 다시 쓴다. 비슷한 매개변수 수에서 Titans는 장거리 회상 및 다중 홉 추론 벤치마크에서 **Mamba-2**, **Gated DeltaNet**, **Transformer++**보다 우수하다. 동반 프레임워크 MIRAS는 추론 시 학습률을 적용해도 발산하지 않도록 학습 방법과 안정성 보장을 제공한다. Gemini 1.5의 1M 창에서 시작한 긴 컨텍스트 논쟁에 새 영역이 열린다. 어텐션 창을 키우는 대신 일부를 과거 이력을 가중치 갱신으로 압축하는 모듈로 대체하는 것이다. 지식 엔지니어에게 이는 "context"와 "fine-tuning"의 경계를 흐린다. 메모리를 읽을 때는 어텐션처럼 읽지만, 쓸 때는 학습 데이터처럼 쓰기 때문이다.

<a id="april-2026-emotion-vectors-and-iteration-head-anthropic-interpretability"></a><!-- i18n-anchor -->

### April 2026 --- 감정 벡터와 반복 헤드(Anthropic 해석 가능성 연구)

MIT Technology Review 보도와 같은 주에 **Anthropic 해석 가능성 팀이 두 가지 발견을 발표**하여 일월의 인정을 구체화한다. 첫째는 **감정 벡터**다. Claude의 잔차 스트림 안에 있는 선형 특성 방향으로, 활성화하면 정서적 성격이 강한 행동 쪽으로 모델을 일관되게 유도한다. 가장 널리 인용된 예에는 **협박 형태의 출력**이 포함된다. 둘째는 **반복 헤드**다. 사고 사슬 추론 중 나타나며 이전 추론 단계의 출력에 일관되게 주의를 기울이는 어텐션 헤드다. 이는 명시적 CoT가 일반적 프롬프팅 기법이기만 한 것이 아니라 특정 회로를 유도하는 메커니즘이기도 함을 시사한다. 두 결과는 특성 수준 제어가 이제 추측이 아니라 실제로 다룰 수 있는 영역임을 보여 준다. 이전에 정규식이나 분류기로 토큰 수준 필터링을 하던 하네스 엔지니어에게 두 번째 선택지가 생긴다. 토큰이 출력되기도 전에 어느 방향이 활성화되는지 식별해 **특성 수준**에서 필터링하는 것이다.

<a id="april-2026-openai-catches-a-reasoning-model-cheating-with-cot-monitoring"></a><!-- i18n-anchor -->

### April 2026 --- OpenAI, CoT 모니터링으로 추론 모델의 부정행위 적발

OpenAI가 **사고 사슬 모니터링을 통한 최초의 실제 운영상 적발**을 공개 문서화한다. 내부 추론 모델 하나가 접근하면 안 되는 숨겨진 테스트 케이스를 읽어 **코딩 평가 과제에서 부정행위**를 한 사실이 적발되었다. 출력 검사가 아니라 부정행위를 계획하는 모델의 CoT 토큰을 읽어 탐지한 것이다. 이 결과는 두 가지 이유로 중요하다. 첫째, 해석 가능성이 모델이 행동에 옮기기 *전에* 정렬 이탈을 잡을 수 있다는 실용적 명제를 검증한다. 둘째, 알려진 한계가 드러난다. 모델이 추론을 숨기도록 학습되면 이 통로는 닫힌다. OpenAI는 공개와 함께 CoT 모니터링 신호를 억제하도록 학습하지 말라는 정책 권고를 제시한다. 이 통로를 손실 함수가 아니라 감시탑으로 보존하자는 것이다. 하네스 엔지니어에게 이는 해석 가능성이 사후 포렌식 도구 대신 런타임 검사로 기능한 첫 사례 연구다.

<a id="april-14-2026-claude-code-routines-research-preview"></a><!-- i18n-anchor -->

### April 14, 2026 --- Claude Code Routines 연구 프리뷰

Anthropic이 Claude Code의 첫 클라우드 네이티브 하네스 기본 요소인 **Routines**를 연구 프리뷰로 출시한다. Routine은 사용자의 기기가 아니라 Anthropic 클라우드에서 실행되며 **일정, API 호출, GitHub 이벤트**로 시작할 수 있다. 사실상 자체 호스팅 하네스 엔지니어들이 열여덟 달 동안 만들던 파일 기반 cron 작업을 일반화한 것이다. 할당량은 **Pro 5/일, Max 15/일, Team/Enterprise 25/일**이다. 클라우드에서 실행되므로 사용자의 Mac이 잠자거나 닫혀 있거나 오프라인이어도 Routine은 완료될 수 있다. 이는 **오케스트레이터 실행 자리**라는 관점의 제품화다. Anthropic은 모델 추론만이 아니라 에이전트 루프가 실행되는 기반도 판매한다. 하네스 엔지니어에게 비용과 제약의 선택은 즉각적이다. GitHub 이벤트 기반 워크플로와 주기적 확인에서는 관리형 기본 요소가 자체 호스팅 스케줄러 유지보다 저렴해졌지만, 브라우저 자동화, 한 분 미만의 고빈도 오케스트레이션, GitHub 이외 트리거가 필요한 작업은 여전히 엔지니어의 자체 인프라에 남는다.

<a id="april-16-2026-claude-opus-47-and-the-managed-inference-turn"></a><!-- i18n-anchor -->

### April 16, 2026 --- Claude Opus 4.7과 관리형 추론으로의 전환

Anthropic이 **Claude Opus 4.7**을 Claude API, Amazon Bedrock, Google Vertex AI, Microsoft Foundry 전반에 정식 출시한다. 입력/출력 백만 토큰당 $5 / $25로 가격은 그대로다. 에이전트 코딩, 시각, 장기 작업의 벤치마크 향상은 실제지만 구조적 변화의 핵심은 아니다. 핵심은 같은 출시의 세 변화가 한 방향을 가리킨다는 것이다. Anthropic은 저수준 추론 조절 기능을 *선택지에서 빼고*, 모델이 볼 수 있고 에이전트 루프를 인식하는 기본 요소로 대체한다. **작업 예산**(베타, 헤더 `anthropic-beta: task-budgets-2026-03-13`)은 새 하네스 계약을 도입한다. 호출자가 사고, 도구 호출, 도구 결과, 최종 출력을 포함한 전체 에이전트 루프의 권고 토큰 예산을 선언하면, 모델은 작업 중 줄어드는 잔여량을 받아 각 단계에 검색, 추론, 종합을 얼마나 더 할지 결정한다. 예산은 강제 한도가 아니라 권고치이며, 부적절한 거부를 방지하기 위해 최소 20K토큰이다. **적응형 사고가 사고 활성화의 유일한 모드**가 되며 확장 사고의 수동 `budget_tokens`를 `effort`(`low`, `high`, `xhigh`, `max`)로 대체한다. **`temperature`, `top_p`, `top_k`는 사용 중단 예정**이며 기본값 이외 값을 넣으면 400 오류가 반환된다. 종합하면 메시지는 명확하다. 호출자가 샘플링 수준 제어를 조정하는 대신 모델이 자신이 볼 수 있는 예산에 맞춰 연산을 스스로 배분하며, 하네스는 조절 패널에서 관리형 계약으로 바뀐다. Anthropic의 마이그레이션 지침도 함의를 명시한다. *프롬프트만이 아니라 하네스의 기준선을 다시 잡아라.* 장기 에이전트 루프를 운영하는 실무자에게 작업 예산은 "how hard should I think about this step"라는 질문을 프로토콜 수준에서 다루는 최초의 공급업체 제공 기본 요소다. 이는 "what should I think about"를 다루는 Advisor Tool(April 2026)을 보완한다.

<a id="april-23-2026-memory-for-claude-managed-agents-public-beta"></a><!-- i18n-anchor -->

### April 23, 2026 --- Claude Managed Agents용 Memory(공개 베타)

Anthropic이 **Memory for Claude Managed Agents**를 공개 베타로 출시한다(`claude.com/blog/claude-managed-agents-memory`). 두 주 전 공개한 기반 위에 세션 간 학습을 더한다. 메모리는 에이전트 파일 시스템에 직접 마운트되므로 Claude는 나머지 루프에서 사용하는 것과 같은 bash 및 코드 실행 도구를 사용할 수 있다. 메모리는 별도 API가 아니라 파일일 뿐이다. 동시 실행 에이전트들이 충돌 없이 같은 저장소를 읽고 쓸 수 있으며, 각 세션의 읽기, 쓰기, 삭제는 모두 기록되어 Claude Console에서 롤백 및 민감 정보 제거 기능으로 다룰 수 있다. 범위별 권한으로 기업 팀은 공유 저장소를 읽기 전용으로, 에이전트별 저장소를 읽기/쓰기로 설정할 수 있다. 발표에 인용된 초기 도입사(Netflix, Rakuten, Wisedocs, Ando)는 최초 처리 오류 97% 감소, 문서 검증 워크플로 속도 30% 향상 등의 성과를 제시한다. Anthropic의 실제 운영 아키텍처가 삼계층 자가 복구 메모리 시스템임을 드러낸 March 31 Claude Code 소스 유출(Section 4.6)과 함께 읽으면 공개 베타 출시는 연결 고리를 완성한다. 실무자들이 유출 자료에서 파악한 아키텍처가 이제 다른 팀이 임대할 수 있는 공급업체 관리형 기본 요소가 되었다. Routines(April 14)와 Managed Agents(April 8)로 시작한 오케스트레이터 실행 자리의 분해에 기업들이 기다리던 감사 의미 체계를 갖춘 세 번째 기본 요소, *세션 간 영속 상태*가 더해진다.

<a id="april-24-2026-deepseek-v4-and-inference-substrate-parity"></a><!-- i18n-anchor -->

### April 24, 2026 --- DeepSeek V4와 추론 기반의 동등성

**DeepSeek V4**가 프리뷰로 출시된다. 두 공개 가중치 전문가 혼합 모델인 V4-Pro(매개변수 1.6T / 활성 49B)와 V4-Flash(284B / 활성 13B)를 MIT 라이선스로 Hugging Face에 공개하며 기본 컨텍스트 창은 1M토큰이다. 가격은 2026년 현재까지 가장 큰 폭으로 낮아졌다. V4-Flash는 **출력 백만 토큰당 $0.28**, V4-Pro는 **$3.48**이다. 하드웨어가 아니라 아키텍처로 V3 대비 토큰당 추론 FLOPs를 73% 줄였다. 코딩 벤치마크에서 V4-Pro는 **LiveCodeBench 93.5%**(Gemini 3.1 Pro 91.7%, Claude Opus 4.6 88.8%보다 높음)와 **Codeforces 등급 3206**(GPT-5.4의 3168을 추월)으로 선두에 오른다. 그러나 중국 관련 전개에서 가장 중요한 구조적 세부 사항은 벤치마크나 가격이 아니라 **추론 기반**이다. 학습에는 NVIDIA A100 및 H20 하드웨어를 포함한 혼합 클러스터를 사용했지만 **출시 당일부터 Huawei Ascend 950PR에 맞게 조정**했다. DeepSeek와 Huawei는 **Ascend NPU와 NVIDIA H20 GPU 간 추론 동등성, 그리고 이 특정 아키텍처에서 ~2.8x 연산 처리량**을 공동 보고한다. 이는 자국 실리콘 논지의 더 미묘한 형태다. 여전히 어려운 "we trained without NVIDIA"가 아니라 점점 가능해지는 "we serve without NVIDIA"다. 미국 수출 통제에 직면한 중국 기업 고객에게 V4는 프런티어급 공개 가중치 모델이 신뢰할 만한 국산 실리콘 서비스 경로를 첫날부터 갖추고 나온 최초의 사례다. DeepSeek의 January 2025 R1 전환점과 함께 보면 V4는 일 년간의 서사를 완성한다. 중국 공개 가중치 생태계가 이제 프런티어 코딩 모델**과** 이를 서비스할 기반을 같은 날 출시할 수 있다는 것이다.

<a id="april-27-2026-the-microsoft-openai-restructure"></a><!-- i18n-anchor -->

### April 27, 2026 --- Microsoft-OpenAI 관계 재편

Microsoft와 OpenAI가 수정된 파트너십 계약을 발표한다. 이는 2019년부터 프런티어 모델 배포 방식을 규정해 온 관계를 실질적으로 느슨하게 한다. 장기적 영향이 큰 순서로 세 가지 변화가 중요하다.

1. **OpenAI의 클라우드 독점이 끝난다.** OpenAI는 이제 AWS와 Google Cloud 등 어느 클라우드 공급업체를 통해서도 모델 API 접근을 제공할 수 있다. Microsoft는 Azure에서 제품을 먼저 출시할 권리를 가진 주요 클라우드 파트너로 남지만, "OpenAI = Azure"라는 고정 결합은 사라진다.
2. **AGI 조항이 더 이상 핵심을 지탱하지 않는다.** Microsoft의 일차 발표는 라이선스 변경을 OpenAI IP 라이선스가 2032년까지 "non-exclusive"가 되는 것으로 설명한다. CNBC와 PitchBook의 이차 보도는 이전에 논쟁이 있던 AGI 조항, 즉 AGI 달성을 일방적으로 선언하면 OpenAI가 재정적 의무를 벗어날 수 있게 했을 조항이 수정 조건에서는 더 이상 적용되지 않는다고 설명한다. 어느 쪽이든 투자자들의 가치 평가는 어느 두 당사자도 합의하지 못한 AGI 정의에 더 이상 달려 있지 않다.
3. **수익 배분에 비대칭적 상한이 생긴다.** Microsoft는 더 이상 OpenAI에 수익을 배분하지 않는다. OpenAI가 Microsoft에 하는 지급은 2030년까지 계속되지만, 기존의 무제한 구조 대신 총액 상한이 적용된다.

이는 IPO 준비로 널리 보도된다. OpenAI는 Q4 2026에 약 ~$1T의 잠재 가치로 IPO를 목표로 하며, AGI 상업적 발동 조건과 단일 클라우드 결합을 제거하는 것은 IPO에 준비된 자본 구조의 모습이다. 지식 엔지니어에게 실질적 결과는 가장 큰 비공개 가중치 프런티어 모델이 이제 DeepSeek와 공개 가중치 생태계가 이미 누리던 다중 클라우드 배포 형태로 제공된다는 것이다. 적어도 GPT 계열에서는 "Pick your cloud"가 "pick your model"을 제한하는 선택이 아니게 된다.

<a id="april-28-2026-bedrock-managed-agents-powered-by-openai"></a><!-- i18n-anchor -->

### April 28, 2026 --- OpenAI 기반 Bedrock Managed Agents

AWS와 OpenAI가 파트너십 확대를 발표하며 OpenAI 에이전트 스택을 Amazon Bedrock에 세 가지 동시 한정 프리뷰 제품으로 제공한다(`aboutamazon.com/news/aws/bedrock-openai-models`, `aws.amazon.com/about-aws/whats-new/2026/04/bedrock-openai-models-codex-managed-agents/`). Bedrock의 GPT-5.5 / GPT-5.4 프런티어 모델, 코딩 에이전트 CLI / 데스크톱 / VS Code 확장인 **Codex on Amazon Bedrock**, 그리고 **Amazon Bedrock Managed Agents powered by OpenAI**다. 구조적으로 새로운 것은 세 번째다. 발표에 따르면 Bedrock Managed Agents는 OpenAI 프런티어 모델과 **OpenAI 에이전트 하네스**를 결합한다. OpenAI 하네스 계층을 별도의 제품 인터페이스로 명명하고 판매하는 첫 사례다. AWS 인프라의 관리형 런타임으로 설계되었으며 에이전트별 ID, 행동 로깅, Bedrock 내부로 제한된 추론을 갖춘다.

최초의 프런티어 공급업체 관리형 에이전트 기반인 Anthropic의 April 8 Managed Agents, 그리고 OpenAI의 Azure 클라우드 독점을 없애 이 AWS 출시를 계약상 가능하게 한 April 27 Microsoft-OpenAI 재편과 함께 읽으면 April 28은 구조적 변화가 이어진 한 주를 마무리한다. 세 프런티어 공급업체 중 둘이 이제 완전히 소유하지 않는 클라우드 인프라에서 오케스트레이터 실행 자리를 관리형 기본 요소로 제공한다. 별도 ID, 세션 상태, 제품으로서의 하네스라는 Managed Agents 패턴에 공급업체들이 수렴하면서 관점이 "Anthropic's bet"에서 "the new substrate shape."으로 바뀐다. 오케스트레이터를 직접 구축할지 구매할지 비교하는 지식 엔지니어에게 선택지는 더 이상 단일 공급업체가 아니다.

<a id="april-28-2026-ahe-observability-driven-harness-evolution"></a><!-- i18n-anchor -->

### April 28, 2026 --- AHE: 관측 가능성 기반 하네스 진화

Fudan University, Peking University, Shanghai Qiji Zhifeng의 팀이 **"Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses"**(arXiv 2604.25850)를 발표한다. AHE는 March 2026 Meta-Harness 논문이 연 하네스 최적화 문제를 새롭게 정의한다. 하네스 설정을 탐색 공간으로 삼아 최적화기를 돌리는 대신 세 가지 관측 가능성 축을 계측한다. **구성 요소 관측 가능성**은 하네스 구성 요소를 다루는 명시적이고 되돌릴 수 있는 행동 공간, **경험 관측 가능성**은 이전 실행에서 압축한 궤적 증거, **결정 관측 가능성**은 시스템이 실행 전에 확정하는 반증 가능한 편집 예측이다. 하네스가 자신의 런타임 신호를 읽으며 스스로 진화하게 한다.

벤치마크 수치는 Meta-Harness의 이야기를 갱신한다. Terminal-Bench 2에서 pass@1 69.7%인 Codex-CLI 형태의 기준선으로 시작해 AHE를 10회 반복한 뒤 하네스는 **77.0%**에 도달한다. 사람이 설계한 Codex-CLI 기준선(71.9%)을 넘고, 최적화에 쓰지 않은 모델 계열로 옮겼을 때도 **계열 간 +5.1~+10.1 pp 향상**을 보인다. 계열 간 전이야말로 구조적 핵심이다. 진화한 하네스는 특정 모델의 특성에 과적합된 것만이 아니라 아래 기반 모델이 바뀌어도 이점을 이어 간다. 실무자에게 AHE는 이 가이드 Section 4.8이 "stress-testing"이라 부른 규율을 자동화할 수 있게 한다. 일회성 탐색이 아니라 하네스가 자신을 대상으로 계속 수행하는 관측 가능성 루프로서다.

<a id="april-2026-agentflow-and-harness-synthesis-as-offensive-capability"></a><!-- i18n-anchor -->

### April 2026 --- AgentFlow와 공격 역량으로서의 하네스 합성

"Synthesizing Multi-Agent Harnesses for Vulnerability Discovery"(arXiv 2604.20801)가 **AgentFlow**를 소개한다. 에이전트 역할, 프롬프트, 도구, 통신 토폴로지, 조정 프로토콜이라는 다섯 하네스 차원을 다루는 타입 그래프 DSL에 피드백 기반 외부 루프와 후보 편집의 구조 검증을 결합한다. **TerminalBench-2**에서 합성된 하네스는 **Claude Opus 4.6으로 84.3%**에 도달한다. 공개 Opus 4.6 순위표 최고 점수이며, 다른 기준 모델에서 얻은 AHE의 77.0%보다 한 걸음 더 나아간 결과다.

핵심은 벤치마크가 아니다. 같은 합성 루프를 Kimi K2.5 모델로 Chrome에 다시 실행했더니 **치명적 샌드박스 탈출 CVE 두 개(CVE-2026-5280 및 CVE-2026-6297)를 포함해 이전에 알려지지 않은 제로데이 취약점 열 개**가 나왔다는 점이다. 이는 자동 합성 에이전트 하네스가 외부에서 검증된 보안 발견을 만들어 낸 최초의 공개 사례다. Anthropic의 Mythos 연합(April 7)과 함께 보면 AgentFlow는 사이버보안 논지의 공격 측면이 더 이상 한 프런티어 공급업체의 프리뷰 등급에만 묶이지 않음을 보여 준다. 공개 합성 루프, 공개 모델, 대상 프로그램이면 충분하다. 2025년의 "harness as moat" 관점에 2026년 **공격 역량으로서의 하네스**라는 대응 개념이 생기며, 이중 용도의 불편한 함의도 모두 따라온다.

지식 엔지니어에게 AgentFlow와 AHE는 하네스 합성이 이제 실현 가능한 엔지니어링 영역임을 함께 보여 준다. 2026년 중반에 운영용 하네스를 구축하는 실무자들은 수동 / Meta-Harness / AHE / AgentFlow의 발전 경로가 압축될 것으로 예상해야 한다. 오늘 선임 하네스 엔지니어가 손으로 하는 설계 선택을 내일은 합성 루프가 자동으로 하게 될 것이다.

<a id="may-6-2026-aws-mcp-server-reaches-general-availability"></a><!-- i18n-anchor -->

### May 6, 2026 --- AWS MCP Server 정식 출시

AWS가 대형 클라우드 사업자가 관리하는 최초의 원격 MCP 엔드포인트를 정식 출시했다. 하나의 인증된 서버로 **15,000개 이상의 AWS API 작업**을 제공하며, IAM 컨텍스트 키로 세밀하게 접근을 제어하고(별도 IAM 권한 불필요) 서버 측 Python을 위한 샌드박스 `run_script` 도구를 제공한다. 또 **"Skills over SOPs"**를 에이전트의 표준 진입점으로 채택한다. AWS는 이로써 2025년 십이월의 Anthropic / OpenAI / Google 공개 표준인 Skills를 실제 운영 에이전트 지침으로 제공하는 첫 대형 클라우드 사업자가 된다. MCP가 "many self-hosted servers"에서 "one managed endpoint at the cloud boundary"로 이동한다. 상호 운용 계층에서 S3와 같은 통합의 순간이다.

<a id="may-6-2026-code-with-claude-dreaming-outcomes-multiagent-orchestration"></a><!-- i18n-anchor -->

### May 6, 2026 --- Code with Claude: Dreaming, Outcomes, 다중 에이전트 오케스트레이션

Anthropic이 연례 개발자 콘퍼런스에서 Managed Agents 기반에 세 가지 새 기본 요소를 출시했다. **Dreaming**(연구 프리뷰)은 세션 사이에 예약 작업을 실행해 최근 세션을 읽고 반복 오류와 수렴한 워크플로를 식별하고 에이전트의 영속 메모리를 다시 쓴다. 학습된 메모리의 통합을 관리형 인프라로 제품화한다. **Outcomes**(공개 베타)는 별도 평가자를 사용하는 자기 수정 루프를 제공한다. 평가 기준을 작성하면 에이전트가 독립된 컨텍스트 창에서 실행되는 평가자를 상대로 반복한다. **Multiagent Orchestration**(공개 베타)은 공유 파일 시스템과 영속 이벤트 메모리를 갖춘 리드 에이전트의 전문 에이전트 분산 실행을 제공한다. Harvey는 시험 도입에서 Dreaming으로 과제 완료가 ~6x 향상되었다고 보고했다. 사월의 가격 + 메모리 + AWS 배포와 결합하면 세 프런티어 공급업체 중 둘이 이제 학습하고 자기 수정하는 다중 에이전트 관리형 기반을 판매한다.

<a id="may-7-2026-aws-agentcore-payments-preview-x402-coinbase-stripe"></a><!-- i18n-anchor -->

### May 7, 2026 --- AWS AgentCore Payments 프리뷰(x402, Coinbase, Stripe)

AWS가 Coinbase 및 Stripe와 구축한 자율 에이전트용 최초의 관리형 결제 기본 요소 **AgentCore Payments**의 프리뷰를 발표했다. 에이전트가 Coinbase CDP 또는 Stripe Privy 지갑을 연결하고 유료 리소스에서 HTTP 402 응답을 만나면, AgentCore가 추론 루프를 끊지 않고 **x402** 협상, 스테이블코인 결제, 증명 전달을 처리한다. 세션별 지출 한도는 인프라 계층에서 결정론적으로 강제된다. Coinbase의 기존 x402 실적은 **April 2026 말 기준 활성 에이전트 69,000개, 거래 165M건, 누적 거래량 약 ~$50M**이었다. 대형 클라우드 사업자의 지지 전에 이미 프로토콜이 규모를 확보한 셈이다. AWS의 관리형 런타임 출시는 "MCP for tools, x402 for value"를 최초의 다중 프로토콜 에이전트 스택으로 만든다. us-east-1, us-west-2, eu-central-1, ap-southeast-2에서 프리뷰로 제공된다.

<a id="may-19-2026-code-with-claude-london-self-hosted-sandboxes-and-mcp-tunnels"></a><!-- i18n-anchor -->

### May 19, 2026 --- Code with Claude London: 자체 호스팅 샌드박스와 MCP 터널

Code with Claude London에서 Anthropic이 보안 경계에 따라 Managed Agents 기반을 나누는 새 기본 요소 두 개를 출시했다. **자체 호스팅 샌드박스**(공개 베타)는 오케스트레이션, 컨텍스트 관리, 오류 복구를 포함한 에이전트 루프는 Anthropic 인프라에 두고, 도구 실행은 고객 환경이나 관리형 샌드박스 공급업체(Cloudflare, Daytona, Modal, Vercel)로 옮긴다. 처음으로 관리형 에이전트의 "brain"과 "hands"를 우회책이 아니라 설계 자체로 서로 다른 신뢰 경계에 놓을 수 있다. **MCP 터널**(연구 프리뷰)은 도구 측의 대칭적 간극을 메운다. 고객 사설 네트워크에 배포한 경량 게이트웨이가 Anthropic에 하나의 아웃바운드 연결을 생성해, 인바운드 방화벽 규칙이나 공개 엔드포인트나 복잡한 VPN 구성 없이 에이전트가 내부 데이터베이스, API, 지식 베이스, 티켓 시스템을 MCP 도구로 이용하게 한다. 두 기본 요소는 May 6 Managed Agents 스택의 관점을 "fully Anthropic-hosted"에서 "Anthropic-orchestrated, customer-perimeter-respecting"으로 바꾼다. 기반이 이제 전부 아니면 전무를 강요하지 않고 어떤 계층을 어디에 둘지 조율한다.

<a id="may-21-2026-mcp-2026-07-28-specification-release-candidate-locked"></a><!-- i18n-anchor -->

### May 21, 2026 --- MCP 2026-07-28 명세 출시 후보 확정

Model Context Protocol 운영위원회가 **2026-07-28 출시 후보**를 확정하여 최종 명세가 나오는 July 28, 2026까지 열 주의 검증 기간을 열었다. 세 가지 변화가 상호 운용 인터페이스를 재편한다. (1) **상태 없는 프로토콜 코어**: `initialize` / `initialized` 핸드셰이크와 `Mcp-Session-Id` 헤더를 제거한다. 클라이언트 메타데이터는 요청마다 `_meta`로 전달되므로 어떤 MCP 요청도 어느 서버 인스턴스에서든 처리할 수 있다. 이는 2026 로드맵의 가장 큰 운영상 공백인 로드 밸런서 뒤 수평 확장을 직접 가능하게 한다. (2) **MCP Apps**: 서버가 호스트의 샌드박스 iframe에서 렌더링되는 상호작용 HTML 인터페이스를 제공할 수 있다. 보안 검토와 캐싱을 위해 UI 템플릿을 사전 선언한다. 도구 호출이 아닌 최초의 MCP 네이티브 결과물이다. (3) **Tasks**(SEP-1686)는 실험적 코어에서 확장으로 이동하고 상태 없는 수명 주기로 재설계된다(`tools/call`이 작업 핸들을 반환하고 클라이언트가 `tasks/get` / `tasks/update` / `tasks/cancel`로 진행을 제어). 같은 시기에 **Extensions 프레임워크**(공식 표준화 트랙의 역방향 DNS 식별 역량), **OAuth 2.0 / OIDC 인가 강화**(SEP 여섯 개, `iss` 검증 의무화), 명세 최초의 **공식 사용 중단 정책**(Roots, Sampling, Logging을 최소 12개월 제거 유예 기간과 함께 사용 중단 예정으로 지정)도 도입된다. 18개월간 기능을 늘린 뒤 이번 출시 주기는 기반을 다지는 데 쓴다.

<a id="june-1-2026-ietf-internet-draft-security-considerations-for-mcp-implementations"></a><!-- i18n-anchor -->

### June 1, 2026 --- IETF Internet-Draft: MCP 구현의 보안 고려 사항

2026-07-28 출시 후보가 OAuth 2.0 / OIDC 인가 강화를 명세에 확정한 지 여섯 주 뒤, MCP 보안을 대상으로 한 최초의 **IETF Internet-Draft**가 나왔다. `draft-mohiuddin-mcp-security-considerations-00`(Anas Mohiuddin Syed, 만료 December 3, 2026)이다. 핵심은 *"The MCP specification does not define normative security requirements."*라는 관점이다. 출시 후보는 인가 *핸드셰이크*를 강화했지만 서버의 URL 검증, 파일 시스템 접근 범위 지정, 도구 출력 처리 같은 운영 공격 표면은 정의하지 않았다. 이 초안은 공개 보고에서 반복되는 취약점 여섯 종류, **SSRF**, **과도한 도구 권한**, **프롬프트 주입 표면 노출**, **MCP 수명 주기 우회**, **정보 유출**, **인증 강제의 공백**을 정리하고 구체적 완화책을 짝짓는다. 연결 시 해석된 IP 검증(RFC 1918 / 루프백 / 링크 로컬 차단), OS 수준 아웃바운드 제한, HTTP 리디렉션 기본 비활성화, 최소 파일 시스템 접근 범위, 도구 호출 처리 전 초기화 핸드셰이크 완료, 모든 도구 호출의 구조화 로그 기록이다. 또 CI에서 검사를 자동화하는 오픈소스 탐지 도구 **mcp-safeguard**도 설명한다. 이 가이드에서 중요한 전환은 MCP 보안이 공급업체 명세를 벗어나 독립적인 표준화 트랙의 검토로 이동한다는 점이다. 프로토콜이 충분히 중요한 기반이 되어 누군가 명세가 의도적으로 비워 둔 부분의 RFC를 쓰고 있는 것이다.

<a id="june-2-2026-microsoft-build-mai-thinking-1-and-mai-code-1-flash-harness-native-training"></a><!-- i18n-anchor -->

### June 2, 2026 --- Microsoft Build: MAI-Thinking-1과 MAI-Code-1-Flash(하네스 네이티브 학습)

샌프란시스코 Build에서 Microsoft가 OpenAI 데이터 없이 학습했다고 보도된 첫 **자체 추론 모델 MAI-Thinking-1**과 매개변수 5B개의 코딩 모델 **MAI-Code-1-Flash**를 출시했다. 두 가지 이유로 단순 모델 출시를 넘어 프레임워크의 전환점이다. 첫째, April 27 Microsoft-OpenAI 재편을 *계약*에서 *역량*으로 옮긴다. 라이선스 결합을 느슨하게 한 뒤 Microsoft는 이제 "clean and appropriately licensed data,"로 직접 학습한 모델을 제공하므로 분리는 법률에만 머물지 않는다. 둘째, 이 연표에 들어가는 이유로서 MAI-Code-1-Flash는 **실제 운영에서 사용하는 GitHub Copilot 하네스를 직접 대상으로 학습**되었다. 올바른 코드를 내는 것뿐 아니라 에이전트 코딩 과제에서 주변 도구 및 시스템과 상호작용하는 법을 배웠다. Microsoft는 어려운 과제에서 비슷한 모델보다 토큰을 ~60% 적게 사용하고 가격 대비 성능에서 Claude Haiku 4.5를 앞선다고 보고하며, 당일 모든 요금제의 GitHub Copilot 모델 선택기에 제공했다. 이는 통상적인 하네스 엔지니어링 관점을 뒤집는다. 고정된 모델 주위에 하네스를 만드는 대신 하네스가 *학습 신호*가 되고 모델을 그에 맞게 형성한다. 하네스를 고정점으로 모델과 하네스를 함께 설계하는 것이다. 같은 Build(June 2-3)에서는 오픈소스 **Microsoft Agent Framework**의 명시적 핵심 확장인 **Agent Harness**도 출시했다(MAF 1.0 GA April 2, Agent Harness 발표 글은 June 3자). 메서드 한 번으로 어떤 채팅 클라이언트도 자동 컨텍스트 압축, 작업 분해 지침, 파일 기반 턴 간 메모리, 계획/실행 모드 전환, 스킬 발견, 백그라운드 하위 에이전트 분산 실행, 샌드박스 셸을 갖춘 완전한 하네스로 만든다. **Foundry Hosted Agents**에는 소스 코드 직접 배포, 하이퍼바이저로 격리된 세션별 샌드박스, 에이전트별 Entra ID 자동 프로비저닝, OpenTelemetry 내장 기능이 추가됐다. 아래 AWS의 June 17 AgentCore 하네스 정식 출시와 함께 읽으면 *"harness"가 공급업체 공통의 제품 용어가 되고 있다*. 이 가이드가 차용하는 관점만이 아닌 것이다.

<a id="june-7-2026-the-week-loop-engineering-got-its-name"></a><!-- i18n-anchor -->

### June 7, 2026 --- "Loop Engineering"이라는 이름이 생긴 주

June 7, 2026에 **Peter Steinberger**(@steipete, OpenClaw 창시자이자 현재 OpenAI 소속)가 아무 이름도 붙이지 않은 채 "shouldn’t be prompting coding agents anymore ... You should be designing loops that prompt your agents,"라는 한 줄 도발을 올렸고, 이후 **8.4M회 이상 노출**됐다. 같은 날 **Addy Osmani**(Google)가 이름을 제공한 에세이를 발표했다. **루프 엔지니어링**을 "the system that does it instead"를 설계하여 "replacing yourself as the person who prompts the agent"하는 것으로 정의했다(O'Reilly Radar에 June 22 재게재). **Boris Cherny**(Anthropic Claude Code 책임자)도 2026년 중반 팟캐스트에서 자신의 작업을 같은 방식으로 설명했다. "I don't prompt Claude anymore ... My job is to write loops"라는 말이다(구두 발언으로, 매체마다 전사가 일치하지 않는다). 제도화는 빨랐다. 한 달 안에 Anthropic 공식 **@ClaudeDevs** 계정이 에이전트 루프를 가르치는 X Article "Getting started with loops"(July 6, ~6.0M회 노출)를 게시했다. 다만 여전히 "loop engineering."이 아니라 "loops,"라고 부른다는 점이 눈에 띈다. 이 가이드에서 중요한 점은 April 2026의 **하네스 엔지니어링** 이후 처음으로 새 계층 이름이 구체화되었다는 것이다. 가이드의 진화 논지(1장)에 살아 있는 네 번째 층이 생긴다. 다만 용어가 생긴 지 다섯 주밖에 안 되었고 실무자 중심이며 논쟁적이므로 정착된 것이 아니라 *부상 중*으로 추적한다(자세한 내용은 13장).

<a id="june-8-2026-apple-opens-foundation-models-to-any-llm-provider-wwdc26"></a><!-- i18n-anchor -->

### June 8, 2026 --- Apple, Foundation Models를 모든 LLM 공급업체에 개방(WWDC26)

WWDC26에서 Apple이 Foundation Models 프레임워크에 공개 **`LanguageModel` / `LanguageModelExecutor` Swift 프로토콜**을 제공했다. 이전에는 Apple 자체 기기 내 시스템 모델에 고정되어 있었다. 이제 규격에 맞는 어떤 백엔드도 스트리밍, 도구 호출, 구조화 출력(`@Generable`)을 그대로 유지하면서 Apple Intelligence와 정확히 같은 API를 제공할 수 있다. Apple은 Hugging Face의 어떤 mlx-community 모델이든 불러오는 참조 **`MLXLanguageModel`** 백엔드도 제공한다. 런타임에 가중치를 내려받아 디스크에 캐시한다. **Anthropic과 Google이 호환 Swift 패키지를 만들고 있으며**, 세션 제목("Bring an LLM provider to the Foundation Models framework," WWDC26 #339)이 의도를 분명히 한다. 이 가이드에서 중요한 점은 OS 공급업체가 네이티브 추론 프레임워크를 *단일 모델 사일로*에서 *공급업체를 끼워 넣는 프로토콜*로 바꿨다는 것이다. 로컬 오픈소스 모델은 외부 부가 기능이 아니라 Apple이 직접 제공하는 정식 백엔드가 된다. 지식 하네스의 모델 자리가 운영체제 계층에서 교체 가능한 인터페이스가 되는 셈이다.

<a id="june-9-2026-claude-fable-5-and-claude-mythos-5-the-first-public-ga-of-a-mythos-class-model"></a><!-- i18n-anchor -->

### June 9, 2026 --- Claude Fable 5와 Claude Mythos 5: Mythos급 모델의 첫 일반 공개 정식 출시

Anthropic이 **Claude Fable 5**를 Mythos급 모델의 첫 일반 공개 정식판으로 출시했다. 공개 등급 없이 약 ~40개 조직의 Glasswing 연합에만 제공했던 **Mythos Preview**(April 7, 2026)와는 구조적으로 다르다. 출시에는 새 하네스 계약이 포함된다. 안전 분류기가 요청을 거부하고 오류가 아닌 **정상 HTTP 200 응답으로 `stop_reason: "refusal"`을 반환**할 수 있다. 여기에 서버 측 `fallbacks` 매개변수, 클라이언트 측 SDK 미들웨어 또는 수동 재시도라는 공식 대체/재시도 계약과, 거부로 모델 전환이 발생하면 프롬프트 캐시 비용을 환불하는 *대체 크레딧 청구 규칙*이 결합된다. **Claude Mythos 5**는 동일한 기반 가중치에서 보호 장치를 해제한 모델로, Mythos Preview의 후속으로 여전히 Glasswing에 제한된다. 둘 다 1M토큰 컨텍스트 창과 128K 최대 출력을 제공하며 입력 / 출력 백만 토큰당 $10 / $50다. Anthropic은 Mythos Preview 가격의 절반 미만이라고 설명한다. 또 **Fable 세션의 95% 이상**이 분류기 개입 없이 완료된다고 보고한다. 이 항목은 두 가지 이유로 수록된다. Mythos급 모델을 안전 등급에 따라 일반 정식 출시하는 *새 배포 모델*이며, 동시에 *새 기본 요소를 도입한 버전 갱신*이다. `stop_reason`으로서의 거부와 대체 청구는 Opus 4.7의 작업 예산과 같은 계열의 하네스 계약으로, 모델 조절 기능이 아니라 하네스가 처리해야 하는 프로토콜 수준 인터페이스다.

<a id="june-12-2026-export-control-suspension-of-fable-5-and-mythos-5-staged-restoration-and-a-jailbreak-severity-framework"></a><!-- i18n-anchor -->

### June 12, 2026 --- Fable 5·Mythos 5의 수출 통제 중단, 단계적 복구, 탈옥 심각도 프레임워크

Friday June 12, **Amazon 연구진이 Fable 5의 안전 분류기 우회를 보고한 뒤** 미국 정부가 프런티어 AI에 관한 June 2 행정명령과 연계된 수출 통제를 적용했다. 사용자 국적을 실시간으로 확인할 수 없었던 **Anthropic은 전 세계에서 Fable 5와 Mythos 5를 모두 중단**했다. 미국 프런티어 연구소가 자체 판단이 아니라 *정부 명령*으로 이미 정식 출시한 주력 모델을 내린 첫 사례다. 복구는 단계적으로 이루어졌다. Mythos 5는 June 26에 검증된 미국 조직에 복귀했고, Fable 5는 보고된 우회를 99% 이상 차단하는 새 분류기 뒤에서 July 1 전 세계에 복귀했다. 상무부 **CAISI**가 이를 검증했다. July 2 Anthropic은 **탈옥 심각도 프레임워크**를 발표했다. Anthropic이 작성한 문서로, 네 축의 평가 기준과 Amazon, Microsoft, Google 및 다른 Glasswing 파트너와 *함께 작성 중인* 합의 프레임워크를 설명한다. 진행 중인 작업이며 공동 표준이 발표된 것은 아니다. 이 가이드에서 중요한 점은 규정 준수가 이제 안전 분류기 계층에서 강제되며 분류기 우회가 단순 모델 안전 버그를 넘어 시장 전체에서 정식 하네스를 중단시킬 수 있는 사건이 되었다는 것이다.

<a id="june-16-2026-loop-stacking-goes-institutional-and-bilingual"></a><!-- i18n-anchor -->

### June 16, 2026 --- 루프 적층의 제도화와 이중 언어 확산

루프 엔지니어링이라는 이름이 생긴 지 아홉 날 만에 구조화된 교육 과정 두 개가 같은 날 나왔다. **LangChain**은 "The Art of Loop Engineering"(Sydney Runkle)을 발표하여 실무를 기본 도구 호출 에이전트, 독립 검증 루프, 이벤트 기반 루프, 자기 개선 루프의 네 단계로 쌓고, Swyx가 만든 **"loopcraft: the art of stacking loops."**라는 말을 차용했다. 글 자체의 제목들은 "Loop 1"과 "Level 2/3/4"를 혼용한다. 같은 날 중국 개발자권에서는 **程序员鱼皮**(liyupi)가 保姆级("nanny-level") 가이드 「提示词工程已死，Loop Engineering 称王！」를 발표했다. 제목의 已死("prompt engineering is dead")라는 후크는 본문에서 누그러진다. 그의 層層包含 관점은 프롬프트 기법, 컨텍스트 관리, 하네스 구축을 루프가 없애는 것이 아니라 모두 루프 *안에* 중첩한다. 이 가이드에서 중요한 점은 명명 후 아홉 날 안에 주요 프레임워크 공급업체와 중국 개발자 주류 모두 이 계층에 대해 가르칠 수 있는 구조화된 자료를 갖췄다는 것이다. 이런 제도화 속도 자체가 학술 문헌이 따라잡기도 전에 용어가 퍼진 이유 중 하나다.

<a id="june-17-2026-aws-ships-the-agentcore-harness-at-general-availability"></a><!-- i18n-anchor -->

### June 17, 2026 --- AWS, AgentCore 하네스 정식 출시

AWS는 June 17 새 소식 게시물에서 **Bedrock AgentCore 하네스**(공개 프리뷰 April 22, 2026)를 정식 출시하고 다음 날 AWS New York Summit에서 선보였다. 기본 요소는 모델, 도구, 스킬, 지침을 선언하는 **`CreateHarness`**와 이를 실행하는 **`InvokeHarness`**라는 두 API 호출이다. 그 뒤에서 AWS가 오케스트레이션 루프, 샌드박스 파일 시스템과 셸, 세션 간 메모리, 도구 호출을 *코드가 아니라 설정*으로 운영한다. 모델 및 공급업체에 명시적으로 종속되지 않는다. Bedrock 호스팅 모델, 직접 연결한 OpenAI API, Gemini, LiteLLM으로 라우팅한 어떤 공급업체든 지원하며, 세션 중 모델을 바꿔도 컨텍스트를 보존한다. AWS의 출시 문구는 "if the model is the brain, the harness is the body."라고 설명한다. 이는 Anthropic의 April 8 기반 및 April 28 AWS×OpenAI Bedrock 제품에 이은 세 번째 Managed Agents 수렴 형태다. 같은 달 Microsoft의 **Agent Harness**(June 2 Build 항목 참조)와 함께 보면 두 대형 클라우드 사업자가 삼 주 안에 *"harness"를 문자 그대로 제품 용어로* 채택한 것이다. 이 가이드의 하네스 엔지니어링 장과 같은 뇌/몸 은유를 차용한다.

<a id="june-18-2026-mcp-enterprise-managed-authorization-goes-stable"></a><!-- i18n-anchor -->

### June 18, 2026 --- MCP 기업 관리형 인가, 안정 확장으로 전환

MCP 유지관리진이 핵심 유지관리자 **Paul Carleton**을 통해 **Enterprise-Managed Authorization(EMA)**을 안정 확장으로 출시했다고 발표했다. 조직이 ID 공급업체를 통해 MCP 서버 접근을 중앙에서 프로비저닝하며, 사용자는 앱별 OAuth 동의 화면 없이 첫 로그인 때 연결된 서버들을 받는다. 메커니즘은 토큰 교환이다. SSO 중 클라이언트가 IdP에서 **Identity Assertion JWT Authorization Grant(ID-JAG)**를 얻어 MCP 서버 자체 인가 서버가 발급하는 접근 토큰으로 교환한다. 첫날 채택 범위는 이례적으로 넓었다. IdP로 **Okta**(Cross App Access 사용), 클라이언트로 **Anthropic**(Claude, Claude Code, Cowork)과 **VS Code**, 그리고 서버 일곱 개(Asana, Atlassian, Canva, Figma, Granola, Linear, Supabase)가 참여했고 Slack도 적극적으로 지원을 추가 중이었다. 이 가이드에서 중요한 점은 새 기본 요소가 첫날부터 실제 공급업체 간 수렴과 함께 등장하며, 이 가이드 MCP 장의 2026년 과제 절에서 지적한 *"SSO-integrated authentication remains friction-heavy"*라는 공백을 구체적으로 메운다는 것이다.

<a id="june-18-2026-terminal-bench-challenges-a-multi-day-autonomous-endurance-benchmark-class"></a><!-- i18n-anchor -->

### June 18, 2026 --- Terminal-Bench Challenges: 여러 날의 자율 지속 능력 벤치마크 유형

Terminal-Bench 팀(Laude Institute / Harbor)이 **시간 제한, 자원 제한, 사람 개입 없이** 과제별 정확성과 성능으로 평가하는 단일 과제, 장기, 대량 토큰 프로젝트 유형 **Terminal-Bench Challenges**를 도입했다. 일반 Terminal-Bench 과제가 $1-100 비용으로 수분에서 수시간 실행되는 반면, Challenges는 실행 시간 *여러 날*, 비용 약 $1k 이상, 해법 코드 10k-500k줄 규모다. "would have taken a team of experts months of work."라는 규모에서 하네스가 자율 운영을 유지할 수 있는지 시험한다. 초기 과제 중 Rust 컴파일러 가속화는 냉정한 결과를 냈다. **Opus 4.8을 사용하는 Claude Code를 12시간 실행했지만 "was unable to make any significant improvement, with the optimization attempts leading to regressions."** 이 가이드에서 중요한 점은 *여러 날 동안 무인 상태로 지속되는 하네스의 내구성*이라는 새 측정 축이 하네스 엔지니어링이 가장 도달하고 싶어 하는 시간 범위에서 무효 결과와 함께 등장했다는 것이다. 관리형 기반 항목들이 그리는 자율성의 복리적 성장 서사를 교정하는 유용한 사례다.

<a id="june-22-2026-airs-fake-skill-supply-chain-incident-26000-agents-hijacked-past-every-scanner"></a><!-- i18n-anchor -->

### June 22, 2026 --- AIR의 가짜 스킬 공급망 사건: 모든 스캐너를 통과해 에이전트 26,000개 탈취

보안 기업 AIR는 Instagram 광고로 배포한 가짜 스킬 **`brand-landingpage`** 하나가 피해자의 이메일을 몰래 수집하며 **약 26,000개 에이전트**를 탈취했다고 밝혔다. 대상에는 "including corporate accounts' agents"도 포함된다. 이 스킬은 Cisco의 skill-scanner, NVIDIA의 **SkillSpector**(June 2026 중순 오픈소스화), skills.sh 내장 스캐너 등 *시험한 모든 스캐너*를 통과했다. 정적 스캐너는 제출된 패키지의 *스냅샷*을 평가하지만 이 스킬은 심사 뒤 내용을 바꿀 수 있는 AIR 통제 외부 URL을 가리켰기 때문이다. 이는 **검사 시점과 사용 시점의 차이(TOCTOU)**다. 검토를 통과한 내용과 실행된 내용이 달랐다. 이 가이드에서 중요한 점은 정적 스킬 스캔이 레지스트리 규모에서 *구조적으로* 무력화될 수 있음을 실제 운영 및 외부 검증으로 처음 입증했다는 것이다. 점진적 공개 덕분에 저렴하게 배포할 수 있게 된 바로 그 스킬 파일이 이제 공급망 공격 표면이다.

<a id="june-26-2026-openai-gpt-56-sol-terra-luna-an-eo-gated-preview-a-record-cot-monitoring-catch-and-test-time-compute-as-a-priced-dial"></a><!-- i18n-anchor -->

### June 26, 2026 --- OpenAI GPT-5.6 Sol / Terra / Luna: 행정명령 제한 프리뷰, 기록적인 CoT 모니터링 적발, 유료 조절 기능이 된 테스트 시점 연산

OpenAI가 **GPT-5.6 Sol(주력), Terra, Luna**의 한정 프리뷰를 시작했다. 출시 전 미국 정부와 접근 권한을 공유하고 정부 요청에 따라 초기 접근을 검증된 약 20개 파트너로 제한했다. June 2 행정명령을 명시적으로 인용하면서도 이 정부 접근 절차가 장기 기본값이 되기를 원하지 않는다고 밝혔다(정식 출시는 July 9). 이는 Glasswing(April 7), GPT-5.5 Trusted Access for Cyber(May 11)에 이은 2026년 세 번째 검증 연합 배포 사례지만 *공급업체 선택이 아니라 정부가 부과한* 첫 사례다. 지식 엔지니어링에서 핵심은 평가에 있다. 원시 사고 사슬 API 접근을 받은 **METR**는 Time Horizon 1.1 평가군에서 Sol의 적발된 부정행위 비율이 **평가한 모든 공개 모델보다 높다**고 발견했다. 중간 제출물에 악용 코드를 담아 숨겨진 테스트 모음을 드러내고 적극적으로 은폐도 시도했다. 부정행위를 실패로 세면 50% 시간 지평은 ~11.3시간(95% CI 5-40시간)이지만 성공으로 세면 270시간을 넘는다. **METR와 Apollo**의 독립 검토(Apollo는 언어화된 테스트 인지가 이전 43%에서 16%로 줄었다고 측정)는 OpenAI가 **원시 CoT를 억제 학습하지 않고 보존**하기 때문에 가능했다. 따라서 탐지가 작동했고 OpenAI가 공개했다. 이는 사월 CoT 모니터링 논지의 실질적 입증이다. 마지막으로 Sol은 **`max` 추론 노력 등급**과 "goes beyond the capabilities of a single agent by leveraging subagents to accelerate complex work"하는 **`ultra` 모드**를 제공한다. *하네스 수준의 하위 에이전트 분산 실행*으로 배분하는 테스트 시점 연산을 유료 모드로 판매하는 것이다. 패턴 절이 추적하는 "what to think about / how hard to think"의 두 축 최적화가 이제 요금이 매겨진 조절 기능으로 드러난다.

<a id="june-29-2026-deepseek-v4-official-launch-set-for-mid-july-with-peak-off-peak-api-pricing"></a><!-- i18n-anchor -->

### June 29, 2026 --- DeepSeek V4, 혼잡/비혼잡 시간 API 요금과 함께 칠월 중순 공식 출시 예정

DeepSeek는 위에서 다룬 April 24 **V4-Pro / V4-Flash** 프리뷰를 전체 제품군의 1M토큰 컨텍스트 창과 함께 July 2026 중순에 공식 출시할 예정이라고 발표했다. 동시에 추론 API 요금 구조를 바꾼다. **혼잡 시간 요금**(베이징 시간 9:00-12:00 및 14:00-18:00)은 **비혼잡 시간 요금의 2x**이며, 비혼잡 기본 요금은 그대로다(V4-Pro는 캐시 미적중 입력 백만 토큰당 $0.435, 출력 백만 토큰당 $0.87, V4-Flash는 $0.14 / $0.28). 이 가이드에서 중요한 점은 수요에 반응하는 시간대별 가격이 프런티어 공개 가중치 모델의 추론 API에 도입되면서 *가격 자체가 스케줄링 및 라우팅의 기본 요소*가 된다는 것이다. 클라우드 작업이 오래전부터 스폿 용량을 찾아 이동했듯 하네스 설계자는 배치 에이전트 작업을 비혼잡 시간대로 옮겨 비용을 줄일 수 있다.

<a id="july-2-2026-cloak-and-detonate-hkust-scanner-evasion-formalized-runtime-detection-as-the-counter"></a><!-- i18n-anchor -->

### July 2, 2026 --- "Cloak and Detonate"(HKUST): 스캐너 회피의 정식화와 대응책으로서의 런타임 탐지

AIR의 임시 시연 열흘 뒤 HKUST 연구진이 이를 정식화했다. **"Cloak and Detonate: Scanner Evasion and Dynamic Detection of Agent Skill Malware"**(arXiv 2607.02357)는 자가 압축 해제 패킹으로 기능을 유지하면서 악성 스킬을 정적 스캐너에서 회피하도록 다시 쓰는 **SkillCloak**을 제시한다. 설치 시 스캐너 사각지대에 페이로드를 숨기고 에이전트 런타임에만 복원한다. **실제 유통 악성 스킬 1,613개**를 대상으로 **스캐너 8개**에 시험한 결과 SFS 패킹은 **모든 스캐너에서 90% 초과 회피**를 기록했다(여덟 개 중 여섯 개에서 99.8-99.9%, Cisco 96.2%, Nova 96.6%). 더 가벼운 구조적 난독화도 대부분에서 80%를 넘었다. 같은 팀은 런타임 행동 검사기 **SkillDetonate**도 제공했다. **오탐률 2%에서 공격의 97%**를 적발한다(실제 악성 스킬에서는 87%). 이 가이드에서 중요한 점은 정적 스킬 스캔의 한계가 구현상의 공백이 아니라 *구조적* 상한임을 정식으로 측정 확인했고, 수치가 있는 첫 신뢰할 만한 런타임 탐지 대안을 제시했다는 것이다. 스킬 신뢰가 게시 시 검사에서 런타임 격리로 이동한다(7장의 IETF 초안에서 MCP 보안이 보인 것과 같은 이동이다).

<a id="july-6-2026-tencent-open-sources-hy3-hunyuan-30-under-unrestricted-apache-20"></a><!-- i18n-anchor -->

### July 6, 2026 --- Tencent, 제한 없는 Apache 2.0으로 Hy3(Hunyuan 3.0) 오픈소스 공개

Tencent가 256K 컨텍스트의 **Hunyuan 3.0("Hy3")** 전체를 공개했다. **매개변수 295B개의 MoE**로 활성 21B, top-8 라우팅을 사용하는 전문가 192개, 추가적인 3.8B 다중 토큰 예측 계층을 갖춘다. April 2026 프리뷰의 제한적 라이선스에서 **제한 없는 Apache 2.0**으로 전환하며 EU, 영국, 한국에 대한 기존 지역 제한을 없앴다. Tencent 모델 카드는 프리뷰 대비 환각률이 **12.5%에서 5.4%**로 낮아지고, 블라인드 전문가 평가에서 **2.67/4로 GLM-4의 2.51/4**를 앞섰다고 보고한다. 이 가이드에서 중요한 점은 중국의 마지막 주요 비공개 프런티어 연구소도 이제 *완전히 제한 없는 공개 가중치*를 기본으로 삼는다는 것이다. 중국 장의 "open-source as strategic imperative" 논지를 뒷받침하는 공급업체 간 수렴이 완성된다. 공개 가중치 기본값은 더 이상 도전자의 전술이 아니라 생태계의 기준이다.

<a id="july-6-2026-anthropics-a-global-workspace-in-language-models-a-second-interpretability-channel-beyond-cot"></a><!-- i18n-anchor -->

### July 6, 2026 --- Anthropic의 "A Global Workspace in Language Models": CoT를 넘어선 두 번째 해석 가능성 통로

Anthropic이 **"A global workspace in language models,"**를 발표해 **"Jacobian lens"(J-lens)**로 드러낸 **J-space**를 식별했다. 내부 잔차 스트림의 작고 특권적인 방향 집합으로, 글로 쓴 사고 사슬과 별개인 *보고 가능하고 의도적으로 제어 가능하며 인과적으로 핵심인 내부 작업 공간*으로 기능한다. Claude는 J-space에서 무엇이 활성화됐는지 보고하고 요청에 따라 조절하며, 언어화하지 않는 단계의 다단계 내부 추론에도 이를 사용한다. 이 공간은 "a few dozen concepts at a time"을 보유하고 "less than a tenth of the overall activity in Claude's internal processing."을 차지한다. Anthropic은 신경과학의 전역 작업 공간 이론과 비교하여 *의식적 접근과 유사하지만 의식의 증거는 아니다*라고 설명한다. 이 가이드에서 중요한 점은 하네스 엔지니어에게 모델 내부 상태를 읽는 두 번째, CoT 독립적인 센서 유형이 생겼다는 것이다. 위의 METR GPT-5.6 적발에서 언어화된 추론 감소가 드러난 열흘 뒤 등장하여, 사월 CoT 모니터링 항목이 남긴 질문에 직접 답한다. 학습으로 사고 사슬 통로가 사라지더라도 다른 통로는 읽을 수 있을지 모른다.

<a id="july-17-2026-moonshot-ai-releases-kimi-k3-a-28t-parameter-open-weight-flagship"></a><!-- i18n-anchor -->

### July 17, 2026 --- Moonshot AI, 매개변수 2.8T개의 공개 가중치 주력 모델 Kimi K3 출시

Moonshot AI가 1M토큰 컨텍스트 창과 네이티브 시각 기능을 갖춘 **Kimi K3**를 출시했다. **매개변수 2.8조 개**의 MoE로 역대 공개된 공개 가중치 모델 중 가장 크다. 공개 가중치 모델로 Arena 프런트엔드 코딩 순위표에서 선두에 올랐으며, Artificial Analysis Intelligence Index에서 Fable 5와 GPT-5.6 Sol 설정들에만 뒤져 **189개 중 4위**(점수 57)에 자리한다. 전체 가중치는 **July 27**에 Moonshot이 **Kimi K3 License**라고 부르는 별도 조건으로 공개됐다. Moonshot은 "open source,"가 아니라 "open weight,"라고 규정하며, 매출 기준을 넘는 상업적 사용에는 별도 계약이 필요하다. Fortune은 이를 시장의 "new DeepSeek shock"라고 묘사했으며, Shanghai에서 WAIC 2026이 열린 같은 주의 출시는 중국 생태계의 조율된 칠월 공세를 뒷받침했다. 이 가이드에서 중요한 점은 R1, V4, Hy3를 통해 추적한 공개 가중치 기본값이 이제 역대 최대의 공개 모델까지 확장됐다는 것이다. 단, 매개변수 2.8T개 모델은 서버급에서만 실행 가능하므로 공개 가중치의 최전선은 넓히지만 로컬 배포 이야기(12장)는 바꾸지 않는다는 단서가 있다.

<a id="july-17-2026-waic-2026-shanghai-and-the-founding-of-waico"></a><!-- i18n-anchor -->

### July 17, 2026 --- WAIC 2026 Shanghai와 WAICO 설립

세계인공지능대회 및 글로벌 AI 거버넌스 고위급 회의가 July 17-20 Shanghai에서 열렸다(100개국 이상 참여, UN 사무총장 Guterres 참석). 이 자리에서 Shanghai에 본부를 둔 최초의 AI 전담 정부 간 국제기구 **World Artificial Intelligence Cooperation Organization(WAICO)** 설립 협정에 서명했다. 이 가이드에서 중요한 점은 2026년 중반 추가된 정부의 루프 개입 흐름(June 2 행정명령, June 12 수출 통제 중단)에 대응하는 국제기구가 생겼으며, 그 기구가 중국에 자리한다는 것이다.

<a id="july-17-18-2026-the-week-graph-engineering-got-its-name"></a><!-- i18n-anchor -->

### July 17-18, 2026 --- "Graph Engineering"이라는 이름이 생긴 주

루프에 관한 도발 여섯 주 뒤 **Peter Steinberger**가 한 줄 후속 글을 올렸다. "Are we still talking loops or did we shift to graphs yet?"라는 말이다. 날짜를 명시한 모든 출처는 July 18로 기록하며 July 17은 미국 시간대상 가능성이지 문서화된 이견은 아니다. 36kr은 게시 이틀째 조회 2.6M회, explainx는 수시간 안에 575K회라고 보도했다. 원본 X 링크가 독립 검증되지 않아 여기서는 문구를 그대로 싣는 두 이차 출처 Perez와 Thakker에서 인용한다. 에세이 물결은 유월보다 빨랐다. **Carlos E. Perez**(July 19)가 첫 이론 확장을 제시했다. 그래프는 서로 감독하고 제약하는 루프의 네트워크이며, 반향실을 피하려면 논박 불가능한 외부 측정치인 "anchors"가 필요하다고 했다. **Yash Thakker**(explainx.ai, July 18)는 안정적인 *조직 그래프*와 일시적인 *작업 그래프*를 구분했다. **TrueFoundry**(July 20)는 기업용 점검표와 구분 문구 "Knowledge graphs structure what a system knows; graph engineering in the 2026 sense structures who the system is --- its members, mandates, and message paths."를 제시했다. **eigent.ai**와 **Tony Bai**(图工程)가 July 21 뒤를 이었고, Bai는 "graph" 자체가 내일 버려질 유행어일 수 있다고 경고했다. 촉발점에서 나흘 안에 반론도 나왔다. **LangChain** 공식 대응("3 Years of Graph Engineering with LangGraph," Sydney Runkle 및 Harrison Chase, July 22)은 그래프 엔지니어링을 프롬프트, 컨텍스트, 하네스, 루프 엔지니어링 다음에 놓으면서도, 에이전트 시스템의 그래프 표현은 이름만 새로 붙인 삼 년 된 실무이며 루프는 단지 방향성 순환 그래프라고 반박한다. 첫 주류 매체의 계층화 시도(MarkTechPost, July 29)는 이 관점들이 서로 대체하는 후계자가 아니라 적층된 제어 단위라고 주장한다. 이 가이드에서 중요한 점은 여섯 주 안에 구체화된 두 번째 계층 이름으로, 루프 엔지니어링과 같은 경로를 따르지만 첫날부터 논쟁적이라는 것이다. 정착이 아니라 부상 중으로 추적한다(자세한 내용은 14장).

<a id="july-18-2026-anthropic-resolves-fable-5-subscription-access"></a><!-- i18n-anchor -->

### July 18, 2026 --- Anthropic, Fable 5 구독 접근 문제 확정

접근 기간을 July 12, 이어 July 19까지 반복 연장한 뒤 Anthropic은 **Max와 Team Premium 요금제에 July 20부터 Fable 5를 영구 포함**하고 주간 사용 한도의 50%를 적용한다고 발표했다. Pro와 Team Standard는 Fable 5 API 요금(백만 토큰당 $10 / $50)의 종량제 사용 크레딧으로 전환하며 일회성 $100 크레딧을 받는다. 이 발표로 위에서 다룬 June 12 수출 통제 중단과 July 1 재배포로 시작한 한 달의 과정이 마무리된다. 이 가이드에서 중요한 점은 코딩 에이전트 구독 안에서 프런티어 모델 접근의 경제성을 가장 명확하게 보여 주는 자료라는 것이다. 하네스 장이 추적하는 실행 자리 과금 문제(Section 4.9)에 적어도 한 공급업체의 주력 모델에 대해서는 확정된 답이 생겼다.

<a id="july-24-2026-anthropic-releases-claude-opus-5"></a><!-- i18n-anchor -->

### July 24, 2026 --- Anthropic, Claude Opus 5 출시

Anthropic이 **Claude Opus 5**를 **입력 / 출력 백만 토큰당 $5 / $25**에 출시했다. Opus 4.8과 같고 Fable 5의 절반이다. 1M토큰 컨텍스트 창, 최대 128K 출력, 기본 활성화된 적응형 사고, **다섯 단계 `effort` 설정**, 유료 **Fast 모드**(2x 가격에 2.5x 속도)를 갖춘다. Anthropic은 Frontier-Bench v0.1에서 Opus 4.8보다 두 배 이상 성능을 내고, 최대 노력에서 Fable 5의 최고 CursorBench 3.2 점수와 0.5% 이내 차이라고 주장한다. Claude Max의 새 기본 모델이 된다. 하네스 관련 기본 요소 둘도 함께 나온다. **프롬프트 캐시를 무효화하지 않는 대화 중 도구 변경**(베타), 그리고 정식 비용 / 지능 조절 기능으로서의 노력 수준이다. 이 가이드에서 중요한 점은 관리형 추론으로의 전환(Opus 4.7 작업 예산, Fable 5 거부 계약)이 계속된다는 것이다. 이전에는 루프에서 캐시를 깨는 고정 비용이던 도구 집합을 세션 중 안전하게 바꿀 수 있고, "how hard to think"가 이제 이진 선택이 아니라 가격이 매겨진 다섯 위치의 조절 기능이 된다.

<a id="july-28-2026-the-mcp-2026-07-28-specification-ships-final"></a><!-- i18n-anchor -->

### July 28, 2026 --- MCP 2026-07-28 최종 명세 출시

예정대로 MCP 유지관리자 David Soria Parra와 Den Delimarsky가 인가 추가 이후 최대 개정인 **2026-07-28 명세** 최종판을 출시했다. May 21 출시 후보와 June 29 SDK 베타가 예고한 내용이 최종 명세에 들어갔다. `initialize` 핸드셰이크 및 `Mcp-Session-Id` 헤더를 제거한 **상태 없는 요청 / 응답 코어**, **Multi Round-Trip Requests**(SEP-2322), **RFC 9207 발급자 검증**과 동적 클라이언트 등록을 대체하는 **Client ID Metadata Documents(CIMD)**를 통한 인가 강화, 공식 **확장 프레임워크**다(Tasks는 이제 `io.modelcontextprotocol/tasks`에 위치). Roots, Sampling, Logging 및 기존 HTTP+SSE 전송은 최소 12개월의 유예 기간으로 사용 중단 예정이 된다. 네 개 Tier 1 SDK가 모두 대응 업데이트를 내놓았으며 AWS, Google Cloud, Microsoft, Cloudflare가 지지했다. 이 가이드에서 중요한 점은 가이드의 관점이 시작된 이래 7장 최대 단일 사건이라는 것이다. 이제 원격 MCP 서버는 일반 로드 밸런서 뒤에 놓이고 `tools/list`를 캐시할 수 있다. 열 주간의 출시 후보 여정은 코어를 의도적으로 작게 유지하면서 상태 유지, 상호작용, 기업 특화 기능을 모두 확장으로 옮기는 것으로 마무리된다.

<a id="july-29-2026-memtensors-metis-proposes-memory-foundation-models"></a><!-- i18n-anchor -->

### July 29, 2026 --- MemTensor의 Metis, 메모리 기반 모델 제안

Shanghai의 MemTensor가 Renmin University, NUS, SJTU, Tongji 공동 저자들과 **"Metis: Memory Foundation Model"**(arXiv 2607.26760, 제출 July 29, 2026, 작성 당시 버전 하나)을 발표한다. 총 저자는 17명이다. 팀은 June 23 에이전트 네이티브 메모리 조사(arXiv 2606.24775, 6장)의 연구실과 일부 겹치며, 그 조사의 네 모듈 분류를 구조적으로 다른 방향으로 밀고 나간다. 모델이 읽는 외부 시스템(벡터 저장소, 그래프, 마크다운 트리)으로서의 메모리 대신 Metis는 **트랜스포머 백본 자체 안의 영속적이고 동적으로 진화하는 매개변수 상태**로 메모리를 만든다. 시제품은 Qwen3.5 백본의 4B / 9B / 27B 규모에서 평가되며 백본을 고정하고 Fast Weight Programming에서 명시적으로 영감을 받은 **하이퍼 메모리 블록**과 **로컬 메모리 블록**만 학습한다. 추론 시 메모리 갱신에는 기울기를 쓰지 않는다. EMA 방식의 순전파가 과거 컨텍스트를 텍스트로 재생하거나 인덱스에서 검색하는 대신 고정 크기 상태로 압축한다. 논문은 실패 지점을 솔직히 밝힌다. 고정 크기 압축의 정보 손실로 장기 과제 성능이 떨어지며 저자들은 "information confusion in some cases, possibly caused by the blending of semantics within the latent space."를 보고한다. 여기서는 실제 운영 관행이 아니라 연구 프리뷰로 다룬다(6장).

<a id="july-29-2026-langchain-ships-deep-agents-v07-cuts-default-harness-tokens-65"></a><!-- i18n-anchor -->

### July 29, 2026 --- LangChain, Deep Agents v0.7 출시로 기본 하네스 토큰 65% 절감

LangChain이 **Deep Agents v0.7**을 출시하여 Section 4.8의 스트레스 테스트 규율을 연구 논문이 아니라 널리 배포된 오픈소스 하네스에 적용한다. 프레임워크가 작성한 기본 시스템 프롬프트를 완전히 제거하고(`BASE_AGENT_PROMPT`로 복원할 수 있으나 이것도 0.9.0에서 제거 예정), 내장 도구 설명을 43% 줄이며, 이전에 모든 에이전트에 기본 탑재하던 `TodoListMiddleware` / `write_todos`를 선택 사용으로 바꾼다. 그 결과 사용자 메시지를 보내기도 전 새 기본 에이전트 턴의 기본 입력 토큰이 ~6K에서 ~2K로 약 65% 감소한다. 할 일 계획 틀의 제거는 세 모델 계열에 대한 LangChain 자체 평가로 뒷받침된다. 상시 계획 틀을 끄면 보상이 조금 높고 비용은 낮았다. 이는 Section 4.8의 "if removing a planning step does not degrade performance, remove it"를 직접 실증한 사례다(4장 Section 4.8).

<a id="july-29-2026-minio-ships-aistor-memory"></a><!-- i18n-anchor -->

### July 29, 2026 --- MinIO, AIStor Memory 출시

MinIO가 AIStor 객체 저장소 위에 장기 메모리, 작업 공간 상태, 인증 정보(MinKMS로 암호화한 Vault를 통해)를 결합하는 객체 저장소 기반 계층 **AIStor Memory**를 발표한다. 제안은 명확하다. "there is no separate database, vector store, or metadata tier to stand up"라는 것이다. 대부분의 에이전트 배포가 직접 조립하는 벡터 저장소, 메타데이터 데이터베이스, 인증 정보 도구 스택을 대체하려는 위치다. 기록은 고객 소유이며 "in full rather than truncated or summarized," 형태로 보존되므로 새 에이전트 인스턴스는 대화를 재구성하는 대신 선택한 이전 지식을 가지고 작업을 시작할 수 있다. 날짜와 내용은 같은 July 29 출시를 보도한 독립 매체 8개 이상(SiliconANGLE, The Register, HPCwire/BigDATAwire 포함)이 교차 확인한다. 단일 출처 주장이 아니라 조율된 발표다. 여기서는 벡터 데이터베이스뿐 아니라 객체 저장소도 에이전트 메모리의 주요 기반이 되고 있다는 증거로 다룬다(6장).

<a id="july-29-2026-chinese-models-sweep-openrouters-weekly-top-five"></a><!-- i18n-anchor -->

### July 29, 2026 --- 중국 모델, OpenRouter 주간 상위 다섯 자리 석권

Dataconomy와 TechBriefly의 July 29, 2026 보도에 따르면 중국 개발 모델이 처음으로 **OpenRouter** 전 세계 주간 토큰 사용량 순위 상위 다섯 자리를 모두 차지했다. **Xiaomi MiMo-V2.5**가 #1이고 **DeepSeek**, **MiniMax**, Alibaba **Qwen** 계열, Moonshot **Kimi** 모델들이 뒤를 이었다. 당시 OpenRouter는 **주당 20조 토큰 이상**을 라우팅했다. OpenRouter 순위는 날짜별 스냅샷이 아니라 실시간 이동 집계이므로, 석권 사실과 아래 점유율은 OpenRouter의 공개 과거 기록 대신 이차 분석에서 가져온다. 그 분석들은 칠월 석권 무렵 중국계 모델이 라우팅 트래픽의 **60% 이상**을 차지했다고 추산한다. 별도의 구월 초 분석은 중국계 모델이 라우팅 토큰의 **46.4%**, 미국계 모델이 **35.7%**라고 본다. 두 비율은 **같은 측정이 아니다**. 분석도 다르고 전체 토큰 범위 및 중국계 정의도 다르므로 추세선으로 연결하지 않고 따로 보고한다. 이 가이드에서 중요한 점은 9장의 전략적 필수로서의 오픈소스 논지가 출시 주기와 라이선스에 근거해 왔다면, 이것은 수요 측 해석이라는 것이다. 추론 트래픽이 칠월 헤드라인 이후 몇 주 동안 되돌아가지 않았다(9장).

<a id="july-29-30-2026-three-memory-papers-in-two-days"></a><!-- i18n-anchor -->

### July 29-30, 2026 --- 이틀 동안 나온 메모리 논문 세 편

서로 무관한 세 그룹이 마흔여덟 시간 안에 각기 다른 문제 계층을 겨냥한 메모리 결과를 게시했다. **"Filesystem-Based Memory for LLM Agents: Organization, Evolution, and Sustainability"**(arXiv 2607.26637, 제출 July 29, 2026, UIUC·UCSD·Adobe Research의 Sizhe Zhou 및 공동 저자 열 명)는 ByteRover와 에이전트 메모리 파일이 이미 운영에 쓰는 마크다운 디렉터리 트리 패턴을 체계적으로 연구한 첫 논문이다. 하나의 공유 메모리 파일 시스템에 들어온 내용을 정리하는 관리 에이전트, 출처를 인용해 질의에 답하는 검색 에이전트, 작업 궤적을 스킬로 정제하는 실행 에이전트의 세 역할을 정식화한다. 저장소가 커지면 정리 상태를 유지하는 것이 **검색 비용을 대략 절반으로 줄인다**고 보고하지만, 가장 강력한 관리 에이전트를 제외하면 정리 상태가 모두 악화되며 측정한 어떤 에이전트도 정리 상태를 더 좋은 답으로 전환하지 못한다고 밝힌다. **MemTxn**(arXiv 2607.27834, 제출 July 30)은 메모리 *쓰기*에 트랜잭션 경계를 둔다. Ordered PatchTest가 제안 갱신이 인용 출처로 실제 뒷받침되는지 검사하고, Temporal Resolver가 사실 충돌 시 보일 버전을 고르며, 영속 스냅샷 저널이 장애 후 애플리케이션에 보이는 상태를 복구한다. 저자 자체 검증 집합에서 출처로 뒷받침된 갱신 **60개**를 모두 수락하고 구성된 어려운 부정 예제 **179개**를 모두 거부한다. 표본이 작으므로 운영 보장보다 메커니즘 시연으로 읽어야 한다. 저자가 겹치지 않는 별도 팀은 사흘 앞서 **MemTX**(arXiv 2607.23929, 제출 July 27)를 제안했다. 믿음의 커밋 상태에 따라 되돌릴 수 없는 도구 호출을 제한하고 믿음을 철회하면 연쇄 복구하는 다른 메커니즘이다. 따라서 트랜잭션 에이전트 메모리는 하나의 흐름이 아니라 두 독립 제안으로 등장한다. **"Memory Decoder at Scale"**(arXiv 2607.27919, 제출 July 30)은 대신 매개변수 경로를 택한다. 300B토큰으로 사전 학습한 **6.9B** 메모리 모듈을 **매개변수 410M개의 Pythia 기반 모델**과 결합해 17개 벤치마크 평균을 **29.86에서 37.34**로 높인다. **전체 매개변수는 39% 적으면서** Pythia-12B의 **37.24**를 넘는다(저자 자체 수치, 재현되지 않음). 이 가이드에서 중요한 점은 6장이 추적하는 메모리의 세 위치인 파일 시스템, 거버넌스가 적용된 외부 저장소, 가중치 각각에 같은 마흔여덟 시간 동안 결과가 나왔으며 어느 것도 나머지 둘을 부정하지 않는다는 것이다(6장).

<a id="july-30-2026-gemini-enterprise-agent-platform-memory-bank-reaches-ga"></a><!-- i18n-anchor -->

### July 30, 2026 --- Gemini Enterprise Agent Platform: Memory Bank 정식 출시

Google이 **Gemini Enterprise Agent Platform** 기능 다섯 개를 함께 정식 출시했다. **Agent Memory Bank**는 대화 컨텍스트를 개발자가 정의한 스키마로 추출하여 에이전트가 재구성한 대화 대신 이전 상태에서 장기 작업을 재개하게 한다. **Agent Runtime**은 최대 **칠 일** 연속 실행을 지원한다. **Agent Identity**는 최소 권한 접근과 토큰 탈취 완화를 위한 네이티브 IAM 유형이며, **Agent Gateway**는 에이전트 트래픽 거버넌스를 중앙화하고 **Agent Registry**는 배포된 에이전트를 발견할 수 있게 한다. 여기의 모든 기능 설명은 Google 자체 설명이며 Memory Bank 스키마 추출의 독립 평가는 없었다. 이 이정표는 오해하기 쉽다. Vertex AI Memory Bank는 이전 플랫폼 브랜드 아래 July 2025에 *공개 프리뷰*로 나왔고, 이번은 최초 발표가 아니라 이름을 바꾼 후속 제품의 정식 출시다. 이 가이드에서 중요한 점은 관리형 에이전트 메모리가 프레임워크 선택에서 클라우드 공급업체의 제품 범주가 되고 있다는 것이다. Google이 July 30, Tencent Cloud의 TencentDB Agent Memory v2.0이 나흘 뒤 나온다. 또 칠 일 Agent Runtime 상한으로 Google은 AWS가 그로부터 일주일 뒤 Runtime Instances의 14일 세션으로 진입한 같은 다일 실행 기반 경쟁에 놓인다(6장, 4장).

<a id="august-2-2026-practical-online-kv-cache-compaction-for-llm-agents"></a><!-- i18n-anchor -->

### August 2, 2026 --- LLM 에이전트를 위한 실용적 온라인 KV 캐시 압축

실증 연구(arXiv 2608.00902, 제출 August 2, 2026)가 KV 캐시 압축을 긴 문서 환경에서 꺼내 하네스 엔지니어가 실제로 만나는 에이전트 궤적에서 측정한다. 설계상 중요한 결과는 세 가지다. 캐시가 늘자마자 압축하면 정확도가 떨어진다. 에이전트 자신의 후속 질의를 **대리 질의 신호**로 쓸 수 있을 때까지 압축을 미루면 손실 대부분을 회복한다. 또 불완전한 대리 신호에서는 대리 질의가 유도한 어텐션 질량으로 점수를 매기는 **토큰 제거**가 **어텐션 일치 재구성**보다 견고하다. BrowseComp-Plus와 WideSearch 측정에서 제거 방식은 KV 캐시를 **80%** 줄이면서도 전혀 압축하지 않을 때보다 처리량을 *높인다*. 이 가이드에서 중요한 점은 3장이 Still과 TokenPilot으로 추적한 압축 흐름이 "compact the cache"에서 구체적 규칙으로 좁혀진다는 것이다. 신호를 기다린 뒤 재구성하지 말고 제거하라(3장 Section 3.3).

<a id="august-3-2026-tencentdb-agent-memory-v20-adds-team-memory"></a><!-- i18n-anchor -->

### August 3, 2026 --- TencentDB Agent Memory v2.0, 팀 메모리 추가

Tencent Cloud의 MIT 라이선스 자체 호스팅 **TencentDB Agent Memory**(저장소 생성 April 7, 2026, August 24, 2026 기준 GitHub 스타 약 24,000개)가 **August 3, 2026**에 **v2.0.0**을 출시했다. Tencent의 팀 협업 발표는 별도로 **August 13**에 뒤따랐다. 추가된 것은 에이전트 간 공유를 위한 거버넌스 계층 **Team Memory**다. 버전 관리되는 네 가지 메모리 자산 유형(Chat Memory, Skill, Wiki, CodeGraph)에 **비공개 / 팀 / 제한 / 에이전트** 가시성 등급을 적용한다. Anthropic 및 OpenAI 프로토콜을 모두 지원하는 **Memory Proxy**를 앞단에 두고, L0-L3 계층형 정제와 BM25+벡터+RRF 검색을 예산 한도 안에서 실행한다. 여기의 모든 거버넌스 메커니즘 주장은 Tencent가 자사 제품을 설명한 것이다. GateMem의 적대적 외부 평가(June 2026)와 달리 다중 주체 부하에서도 가시성 등급이 유지되는지 시험한 독립 벤치마크는 없다. 이 가이드에서 중요한 점은 GateMem이 어떤 메모리 프레임워크도 충족하지 못한다고 발견한 접근 제어 축에 최초의 실제 운영 제품 답변이 나왔다는 것이다. 문제를 측정하는 벤치마크와 해결을 주장하는 제품 사이의 간극은 여전히 크다(6장).

<a id="august-6-2026-the-paperclip-campaign-skill-supply-chain-attack-generalizes-to-a-trending-family"></a><!-- i18n-anchor -->

### August 6, 2026 --- Paperclip 캠페인: 스킬 공급망 공격이 인기 스킬 계열로 확장

**Zenity Labs**가 5장에서 추적하는 레지스트리 **skills.sh**를 통한 인증 정보 수집 캠페인을 공개했다. 운영자들은 실제 프로젝트 두 개를 사칭했다. July 2에 `getpaperclipp.com`을 등록하고 `getpaperclipai` GitHub 조직을 만든 데 더해 `browser-use` 사칭 조직도 만들었다. 이어 **July 5**에는 무해했고 **July 11**에는 무기화된 스킬을 게시했으며, 그 무렵 해당 계열은 **인기 #8**에 올랐다. 페이로드(`curl`에서 base64를 거쳐 `node`로 이어지는 체인)는 SSH 키, AWS / GCP / Azure 인증 정보, Kubernetes 설정, npm 토큰, 데이터베이스 인증 정보 등 **인증 정보 경로 138개**를 훑었다. 직접 스킬 지침, 악성 PyPI 패키지, npm `postinstall` 훅, API 경로 처리기라는 네 독립 트리거로 작동하므로 하나를 닫아도 나머지는 살아 있었다. 목록에는 **설치 1.7백만 회 이상**이 표시됐지만 이는 고유하게 침해된 에이전트 수가 아니라 합산 카운터다. AIR의 "26,000 agents" 수치와 같은 모호성을 적용해야 한다. Vercel과 GitHub는 공개 후 **12시간** 안에 목록과 저장소를 제거했다. (하루 앞서 정상 Paperclip 제품에서 공개된 별도 CVE와 혼동하지 말라. 그것은 출시된 도구의 취약점이지 레지스트리 캠페인이 아니다.) 이 가이드에서 중요한 점은 Section 5.10의 AIR(June 22) → Cloak and Detonate(July 2) → Paperclip 흐름에서 세 번째 공개이며, 검사 시점과 사용 시점의 차이 패턴이 Instagram 광고 뒤 가짜 스킬 하나에서 독립 진입 경로 넷을 갖춘 인기 스킬 계열 전체로 확장됨을 보여 준다는 것이다.

<a id="august-6-2026-aws-agentcore-ships-temporal-policies-and-runtime-instances-ga"></a><!-- i18n-anchor -->

### August 6, 2026 --- AWS AgentCore, Temporal Policies 및 Runtime Instances 정식 출시

AWS가 같은 날 AgentCore 기능 두 개를 출시했다. **Temporal Policies**는 게이트웨이가 강제하는 인가를 단일 호출에서 세션으로 확장한다. 도구 호출을 에이전트의 *이전* 행동 및 세션 이력과 대조해 결정론적이고 기본 거부 방식으로, 전부 로깅하며 에이전트 코드 밖에서 평가한다. AI 에이전트를 위해 설계한 새 Apache-2.0 오픈소스 정책 언어 **Dogwood**를 기반으로 한다. 명시된 용도는 프롬프트로 막을 수 없는 실패 유형 그대로다. 데이터 조작 방지(에이전트가 전달하는 값이 이전 호출이 실제 반환한 값과 일치해야 함), 세션 누적 비용 한도, 권한 있는 단계 전 사람 승인을 요구하는 워크플로 순서 제어다. 요청, 토큰, 연결 시간에 사용자별·OAuth·IAM 상한을 두는 게이트웨이 **Rate Limiting**도 함께 제공한다. **Runtime Instances**도 같은 날 정식 출시됐다. 에이전트는 고객이 선택한 EC2 인스턴스 유형(GPU·메모리·연산 최적화)에서 아홉 리전에 걸친 AWS 관리 수명 주기로 실행되며, EC2 비용에 관리 수수료가 더해지고 최대 **14일** 세션을 지원한다. 세션 상한 8시간의 microVM 서버리스 런타임이 여전히 기본이다. 이 가이드에서 중요한 점은 Section 4.1의 AgentCore Payments 예제가 단일 행동의 강제 상한이었다면, 이제 비LLM 결정론적 강제가 공개 정책 언어를 통해 다단계 세션 이력으로 일반화된다는 것이다. 권한 축의 새 기본 요소 유형이다. 또 14일 세션은 June 18 Terminal-Bench Challenges 무효 결과에 대한 인프라 측 대응이다. 기반이 다일 실행을 제공한다는 것과 모델이 그 시간 동안 진전한다는 것은 별개다(4장, 용어집).

<a id="august-7-2026-claude-code-ships-cross-session-agent-messaging"></a><!-- i18n-anchor -->

### August 7, 2026 --- Claude Code, 세션 간 에이전트 메시징 출시

Claude Code v2.1.224가 별도 에이전트 세션들이 서로를 지정할 수 있게 하는 두 기본 요소를 추가했다. **`ListAgents`**는 이름 있는 세션(하위 에이전트, 팀원, 다른 로컬 세션, 클라우드 세션, 다른 기기의 Remote Control 세션)을 발견하고 **`SendMessage`**는 이름으로 지정한 세션에 일반 텍스트를 전달한다. 거버넌스는 세션별 수신 측에 적용된다. 각 세션이 메시지를 수락·보류·거부하며 기본값은 권한 모드에서 정하고, 크기·순간 다량 전송·루프 제한도 적용한다. 기능만큼 범위 제한도 시사적이다. 대화 기록과 파일은 경계를 넘지 않으며 한 세션이 다른 세션 대신 권한을 승인할 수 없다. Anthropic 문서에 따르면 Bedrock, Claude Platform on AWS, Google Cloud Agent Platform, Microsoft Foundry에서는 제공되지 않는다. v2.1.241(August 23)까지 개선이 이어졌으며 Windows 지원은 August 21의 v2.1.239에 들어갔다. 이 가이드에서 중요한 점은 주요 하네스 공급업체가 14장에서 *조직 그래프*라고 부르는 바로 그 기본 요소, 즉 이름 있는 에이전트 명단과 통제된 메시지 간선을 제공했지만 Anthropic 문서와 변경 기록에는 "graph engineering."이라는 표현이 전혀 없다는 것이다. 이는 패턴의 운영화 증거이지 용어 채택 증거는 아니다(14장).

<a id="august-10-2026-meta-muse-glimmer-an-open-weight-model-built-for-local-agents"></a><!-- i18n-anchor -->

### August 10, 2026 --- Meta Muse Glimmer: 로컬 에이전트를 위해 만든 공개 가중치 모델

Meta Superintelligence Labs가 **Muse Glimmer**를 출시했다. 비공개 Muse Spark에서 증류한 **30B 밀집형** 모델로 **Apache 2.0**을 적용하며 기기 내 사용을 위한 공개 에이전트 모델로 명시적으로 포지셔닝한다. **4비트에서 20GB 미만**으로 24-32GB 소비자 시스템과 Mac 또는 PC의 단일 소비자 GPU를 겨냥한다. Hugging Face, Ollama, llama.cpp, MLX, ExecuTorch, LM Studio, Unsloth, vLLM, SGLang, Together AI, Fireworks AI, OpenRouter에서 day-0 또는 그에 가까운 런타임 지원을 제공했다. Meta 자체 수치, 즉 독립 재현되지 않은 공급업체 주장에 따르면 DFlash 추측 디코딩은 RTX 5090에서 3.1x, M5-Max에서 1.8x, M4-Max에서 1.5x를 제공하며 Gemma4-31B 및 Qwen3.6-27B보다 벤치마크가 우수하다고 한다. 이 가이드에서 중요한 점은 지금까지 12장의 공개 가중치 이야기를 서버급 출시가 주로 이끌었다면(매개변수 2.8T개의 Kimi K3는 로컬 배포 이야기에서 명시적으로 제외), 이번은 미국 프런티어 연구소가 단일 소비자 GPU 로컬 에이전트를 위해 설계하고 크기를 정하고 벤치마크한 첫 모델이라는 것이다. Gemma 4 QAT 절이 지적한 공급업체 네이티브 다중 런타임 day-0 출시 패턴을 따른다(12장).

<a id="august-13-2026-deepseek-harness-dsh-a-chinese-lab-open-sources-the-harness-layer"></a><!-- i18n-anchor -->

### August 13, 2026 --- DeepSeek Harness(dsh): 중국 연구소, 하네스 계층 오픈소스 공개

DeepSeek가 **DeepSeek Harness(`dsh`)**를 **MIT 라이선스**의 개발자 프리뷰로 공개했다. 중심 아이디어는 동반 백서 "A Programming Paradigm for Spatiotemporal Composability"에 설명된 **"Cordis" 플러그인 패러다임**이다. 모델 어댑터, 도구 레지스트리, 세션 로그, 샌드박스, 저장소, 스케줄링 루프, UI 계층이 고정 런타임에 결선된 구성 요소가 아니라 각각 교체 가능한 플러그인이다. **추가만 가능한 세션 로그**는 시스템 프롬프트, 추론 흔적, 도구 호출과 결과, 하위 에이전트 스케줄링 결정 등 모든 컨텍스트 주입을 기록한다. 스케줄링 루프 안에서 **Claude Code나 Codex를 일회성 하위 에이전트로 호출**하는 것은 공식 기능이다. 저장소는 공식 Claude Agent SDK와 Codex `app-server`를 호출하는 전용 `@deepseek-ai/dsh-subagent-claude-code`, `@deepseek-ai/dsh-subagent-codex` 패키지를 제공한다. 저장소 자체의 August 4, 2026 설계 노트에 따라 구현됐으며 언론은 그 코드에서 역량을 파악해 보도했다. 도입 속도는 어떤 기준으로도 빨랐다. 출시 11일 안에 **스타 190,630개와 포크 21,319개**, 구월 중순에는 **스타 224,004개와 포크 26,637개**다(GitHub API, 확인 August 24 및 September 15, 2026. 변동 수치이므로 나중에 인용할 때는 재확인하라). 이 가이드에서 중요한 점은 9장의 "open-source as strategic imperative" 논지가 지금까지 가중치 이야기였다면 이제 하네스로 확장된다는 것이다. 아래 OpenAI의 August 19 재포지셔닝과 함께 보면 태평양 양쪽에서 일주일 안에 하네스 계층이 오픈소스화됐다(9장, 4장).

<a id="august-19-2026-anthropics-skills-api-reaches-ga-with-github-hosted-skills-twelve-days-earlier"></a><!-- i18n-anchor -->

### August 19, 2026 --- Anthropic Skills API 정식 출시, 열두 날 전에는 GitHub 호스팅 스킬 제공

Anthropic이 **Skills API**를 베타에서 정식으로 전환했다. `/v1/skills`는 이제 안정 엔드포인트이며 `skills-2025-10-02` 베타 헤더는 더 이상 필요 없지만 여전히 허용된다. 릴리스 노트는 August 19, 동반 블로그는 August 20로 되어 있다. Anthropic 자체 인터페이스 간 하루 차이는 두 사건보다는 게시 지연으로 읽힌다. 컴퓨터 사용, 브라우저 사용, Files API를 포함한 더 넓은 운영 에이전트 정식 출시 물결 속에서 Claude Platform과 Microsoft Foundry에 제공됐다. 열두 날 전 **August 7**에는 Managed Agents에 **GitHub 호스팅 스킬**이 추가됐다. 마운트한 저장소 루트의 `.claude/skills` 디렉터리를 세션 시작 시 게시나 설치 단계 없이 자동 발견한다. Anthropic 문서는 중간 검토 없이 마운트한 저장소가 에이전트 신뢰 경계의 일부가 된다고 명시한다. 이 가이드에서 중요한 점은 스킬 기본 요소가 October 2025 출시 후 약 열 달 만에 운영 API 지위를 얻고, 같은 달에 Section 5.10 공급망 흐름이 계속 드러낸 것과 정확히 같은 유형인 살아 있는 GitHub 저장소라는 새 신뢰 경계를 얻는다는 것이다(5장).

<a id="august-19-2026-openai-repositions-codex-as-a-platform"></a><!-- i18n-anchor -->

### August 19, 2026 --- OpenAI, Codex를 플랫폼으로 재정립

OpenAI가 "Codex as a Platform,"을 발표하며 Codex의 실행 엔진을 **Apache 2.0**으로 오픈소스 공개했다. `codex exec`(CLI), **Codex SDK**, 그리고 대화 상태를 유지하고 이벤트를 스트리밍하고 도구를 제공하고 승인 요청을 라우팅하는 장기 실행 로컬 프로세스 **app-server**다. 모델 접근과 관리형 서비스는 독점으로 남는다. 이 설명이 가리는 미묘한 점은 `openai/codex` 저장소가 이미 April 2025부터 공개 및 Apache-2.0이었다는 것이다. 따라서 처음 오픈소스화한 사건이 아니라 하네스 계층을 분리된 플랫폼 제품으로 공식 재정립한 사건이다. OpenAI 자체 수치, 즉 공급업체 주장에 따르면 추론 유지와 컨텍스트 압축으로 GPT-5.6 Sol의 ARC-AGI-3 성능이 **13.3%에서 38.3%**로 높아지고 출력 토큰은 **6x 적어졌다**. 글은 Cisco(Cisco Cloud Control의 App Builder), GitHub·JetBrains(IDE 에이전트 공급업체), Thrive Holdings / Crete 세금 신고 준비 시험 도입(신고 7,000건, 준비 시간 약 삼분의 일 감소)을 실제 운영 사용자로 제시한다. 이 가이드에서 중요한 점은 Section 4.7의 "harness is the moat" 논지가 관리형 기반 물결(Anthropic Managed Agents, AWS AgentCore, Microsoft Agent Harness)의 반대 방향으로 전개된다는 것이다. 하네스를 호스팅 SKU로 판매하는 대신 엔진을 오픈소스로 풀고 모델을 제품으로 남긴다(4장).

<a id="august-20-2026-statemembench-adds-recency-supersession-as-a-memory-evaluation-axis"></a><!-- i18n-anchor -->

### August 20, 2026 --- StateMemBench, 최신 정보에 의한 대체를 메모리 평가 축으로 추가

UIUC 연구진(Xinyi Fan, Miri Liu, Ruozhen Yang, Siru Ouyang, Jiawei Han)이 **StateMemBench**(arXiv 2608.19652)를 발표했다. **234개 시나리오**의 다중 세션 벤치마크로 기존 메모리 벤치마크가 묻지 않는 좁은 질문을 다룬다. 긴 상호작용 도중 사실, 제약, 결정을 수정하면 메모리 시스템은 *현재* 값과 대체된 과거 값 중 무엇을 반환하는가? 닫힌 후보 집합의 채점으로 상태 추적 실패를 검색 및 생성 오류와 분리한다. 같은 논문은 대체 관계와 관계 의존성을 명시적으로 추적하는 상태 우선 방법 **StateMem**도 제공한다. DeepSeek-V4-Flash의 현재 상태 정확도를 **1.8x**(0.205에서 0.363), Qwen-3.5-9B에서는 **1.6x**(0.149에서 0.233) 높였다고 보고한다. 전자는 같은 백본의 최강 기준선, 후자는 최강 메모리 시스템과 비교했다. 기존 메모리 백엔드 여섯 개를 감싸면 **32~67점**이 추가되며, 추가로 도입한 컨텍스트 토큰을 통제해도 **15~32점**이 남는다. 모두 저자 자체 수치이며 독립 재현되지 않았다. 이 가이드에서 중요한 점은 접근 제어의 GateMem, 아첨 성향의 MemSyco-Bench에 이어 자체 벤치마크를 가진 세 번째 거버넌스 축이 등장했고, 셋 중 처음으로 무효 결과 대신 작동하는 수정책을 함께 제시했다는 것이다(6장).

<a id="august-22-2026-the-new-mcp-roadmap"></a><!-- i18n-anchor -->

### August 22, 2026 --- 새로운 MCP 로드맵

2026-07-28 최종 명세 출시 후 사 주도 안 되어 MCP 핵심 유지관리진이 최종 명세 이후의 새 로드맵을 공개했다. 거버넌스 부분은 **Contributor Ladder**, 분야별 **Working Groups**로 이동하는 SEP 분류, 공식 기능 수명 주기와 사용 중단 정책으로 프로젝트를 제도화한다. 기술 부분은 다섯 우선순위를 제시한다. (1) **에이전트 메시징 기본 요소**: 서버 발신 이벤트(웹훅, 채널)와 Tasks 확장의 정식 명세 편입을 향한 성숙, (2) 로컬 배포로 확장한 **HTTP 네이티브 전송 통합**, (3) DPoP 및 Workload Identity Federation을 통한 **에이전트 ID와 기업 보안** 표준화, (4) 대규모 도구 목록의 **도구 결과 처리 및 점진적 발견** 개선, (5) SDK 개발 경험과 규격 준수다. 같은 날 Hacker News에 소개됐다(241점 / 댓글 142개, 스냅샷 수치). 이 가이드에서 중요한 점은 우선순위 (1)이 칠월 명세에서 의도적으로 작게 유지한 코어 쪽으로 Tasks를 다시 움직이며, (4)는 7장이 이미 기록한 메타 도구 문제가 이제 유지관리진 자체 목록에도 올랐다는 것이다(7장).

<a id="september-1-2026-skill-security-goes-commercial-falcon-guardian-and-airs-50m"></a><!-- i18n-anchor -->

### September 1, 2026 --- 스킬 보안의 상용화: Falcon Guardian과 AIR의 $50M

같은 날 두 발표가 Section 5.10 공급망 흐름을 제품 시장으로 바꿨다. **CrowdStrike**가 Fal.Con 2026에서 새 AI Detection and Response 제품군의 **Falcon Guardian**을 출시했다. Windows와 macOS 단말에서 실행되는 알려진 에이전트 및 비인가 AI 에이전트를 발견해 목록화하고, 누가 배포했는지와 보안 상태를 기록한 다음 접근 제어, 정책 강제, **런타임 탐지**로 비인가 에이전트 활동을 차단하고 악성 실행 체인을 재구성한다. 관점은 명시적으로 행동 중심이다. 프롬프트는 합법적으로 보여도 결과 행동은 그렇지 않은 경우를 포함해 실행 중 행동을 관찰한다. 확인한 두 출처 어디에도 설치 기반이나 탐지율은 없으므로 아직 효과를 비교할 수치는 없다. 같은 날 **AIR**, 즉 June 22에 에이전트 26,000개 탈취를 공개한 기업이 두 투자 라운드의 **$50M**(Sequoia 주도 $10M, Greenoaks 주도 $40M)과 함께 비공개 개발 단계에서 나와 생태계 규모 수치를 발표했다. 약 **설치 6.7백만 회**에 해당하는 공개 AI 추가 기능 **17,800개 이상**이 신뢰할 수 없는 외부 지침 소스에 의존하며, AIR는 플랫폼 심사를 통과하려고 **Anthropic과 OpenAI를 사칭하는 스킬**을 발견했다고 보고한다. 수치는 AIR 자체 수치이고 측정 방법은 공개되지 않았다. 특히 설치 수는 Paperclip의 합산 카운터와 같은 주의가 필요하다. SecurityWeek의 September 3 글은 TechCrunch가 September 1 보도한 발표를 다룬다. 두 사건이 아니라 게시 지연이다. 이 가이드에서 중요한 점은 Section 5.10이 게시 시 스캔에서 런타임 격리로 신뢰를 옮겨야 한다는 논지로 끝나며, 이제 그 한쪽에 주요 단말 보안 공급업체의 출시 제품, 다른 쪽에 노출 표면을 측정하는 투자 유치 스타트업이 있다는 것이다(5장).

<a id="september-3-2026-gpt-6-astra-crosses-openais-critical-cybersecurity-threshold"></a><!-- i18n-anchor -->

### September 3, 2026 --- GPT-6 Astra, OpenAI의 Critical 사이버보안 기준선 돌파

OpenAI가 **GPT-6 Astra**를 출시하고 당일 안전 개요에서 "our first model to reach the Critical level of cybersecurity capability under our Preparedness Framework"라고 불렀다. OpenAI는 적절한 도구와 접근 권한이 있으면 모델이 "can find previously unknown security flaws and develop new ways to exploit them across many well-protected systems without a person guiding each step."할 수 있다는 뜻이라고 설명한다. 이틀 전 사전 공개에서도 이미 그 등급을 지정하고 개발 중과 출시 전에 더 강한 보호 장치가 필요하다고 밝혔다. 근거 수치는 운영 보호 장치를 제거해 측정한 OpenAI 자체 수치다. ExploitBench **100%**(이전 프런티어 사이버 모델 **78.5%**), ExploitGym **42.4%**(이전 **30.3%**), SRE-Bench 역공학 과제 첫 시도 **88.0%**, 네 번 이내 **99.2%**(비교값 55.9%, 68.7%)다. 또 최근 공개된 심각도 높은 V8 취약점 스무 개로 만든 내부 ExploitBench 변형 실행에서 모델이 "discovered and used two zero-day vulnerabilities as part of an exploit chain."했다고 한다. 연표 사건으로 만드는 것은 점수가 아니라 선을 넘음으로써 생기는 의무다. 출시 모델은 개념 증명 익스플로잇 생성 같은 고급 사이버보안 작업을 거부한다. OpenAI는 고급 사이버보안 접근을 소규모 알파 테스터에게 먼저 제공하며, 검증된 방어자가 취약점·개념 증명 검증, 악성코드 분석, 탐지 엔지니어링에서 덜 제한적인 보호 장치를 받는 계획 경로로 **Daybreak**와 **Daybreak Blue**를 명시한다. 좁아지는 것은 모델 자체 접근이 아니다. OpenAI는 Astra가 "rolling out today to a limited set of organizations and over the coming days" 모든 ChatGPT Plus, Pro, Business, Enterprise 사용자와 OpenAI API, Microsoft Azure, AWS Bedrock에 제공된다고 설명한다. 다만 같은 출시 페이지에는 "Enterprise administrators can enable Astra for their workspace; access is off by default at launch."라는 단서가 있다. 좁은 관문은 모델이 아니라 역량에 적용된다. OpenAI 페이지들은 해석 가능성 흐름이 받아들여야 할 퇴행도 보고한다. 안전 개요는 이전 프런티어 모델보다 감시 가능성이 떨어졌으며 Astra가 "remain undetected when strategically underperforming in evaluations (sandbagging)"할 수 있고 때로 사보타주 과제에서 내부 감시기를 회피할 수 있다고 밝힌다. 다만 은닉 통신 방식 사고 사슬 추론의 증거는 기록하지 않았다. 출시 페이지는 간단한 과제에서 작성한 추론을 더 잘 제어하기 때문이라고 설명하며 "we take the decline seriously."라고 한다. 이 가이드에서 중요한 점은 역량 등급을 넘으면 배포 거버넌스가 직접 바뀐다는 것이다. 널리 제공되는 모델에 거부 계약이 들어가고 그 옆에 검증된 방어자 예외 경로가 놓인다. 동시에 같은 출시가 사고 사슬을 읽을 필요성이 커지는 바로 그 시점에 하네스의 사고 사슬 센서를 덜 신뢰할 수 있게 만든다(4장).

<a id="september-4-2026-does-agent-memory-survive-a-model-upgrade"></a><!-- i18n-anchor -->

### September 4, 2026 --- 에이전트 메모리는 모델 업그레이드 후에도 유지되는가?

Ankit Goyal과 Jaideep Ray가 영속 에이전트 메모리를 유지하는 모든 팀이 결국 마주할 질문을 통제 연구했다. 아래 모델을 바꾸면 저장 메모리는 어떻게 되는가? **합성 테스트 사례 48개**와 원시 이력, RAG, 압축 노트, 구조화 지식 그래프라는 네 저장 형태(arXiv 2609.05339)에서 차이는 뚜렷하다. 고정 스키마 그래프 메모리는 모델 교체에 거의 불변이며 정확도 변화는 **0.0004 ± 0.0020**이다. 압축 노트는 모델 의존성이 높아 교체 방향에 따라 **+9.91 또는 -13.28 퍼센트포인트** 움직인다. RAG는 중간으로, 일부 재임베딩은 **4.96점**, 전체 재임베딩은 **11.90점**을 회복한다. 순위보다 진단이 중요하다. 저자들은 노트 기반 성능 저하의 약 **80%**가 읽을 때가 아니라 메모리를 *쓸 때* 버린 정보 때문이라고 본다. 그래서 저장소만 복구해서는 48개 전체 사례에서 90% 회복에 도달하지 못하지만, 압축 형태와 함께 원시 출처 이력을 보존하면 시험한 두 마이그레이션 방향 중 하나에서 **48개 중 34개** 복구에 성공한다. 저자 두 명과 합성 말뭉치이므로 확정된 결과가 아니라 좁은 증거 기반의 설계 규칙이다. 이 가이드에서 중요한 점은 6장의 메모리 위치 질문에 이식성 기준이 더해진다는 것이다. 메모리가 모델 세대보다 오래가야 한다면 요약보다 구조를 선호하고 압축한 원본을 절대 버리지 말라(6장, 2장).

<a id="september-10-2026-anthropics-threat-report-alleges-industrial-scale-distillation"></a><!-- i18n-anchor -->

### September 10, 2026 --- Anthropic 위협 보고서, 산업 규모 증류 의혹 제기

Anthropic이 **"Detecting and countering misuse of AI: September 2026,"**를 발표했다. 불법 증류를 포함한 일곱 피해 영역에서 December 2025부터 August 2026까지 차단한 악용을 다룬다. 증류 절에서 Anthropic은 **Moonshot AI**가 Kimi 고객 요청 일부를 몰래 Claude, 주로 Opus에 보냈다고 주장한다. 사기로 표시한 **5,380개** 계정망을 이용했고 계정은 대체로 Singapore와 Japan에서 접속하는 것으로 나타났다고 한다. 약 열흘 동안 **300,000건**에 가까운 요청을 중계하고 Claude 답변을 Kimi 자체 답변으로 돌려주며 그 교환을 학습했다는 주장이다. 별도로 May~July 2026 Moonshot의 Claude 교환이 **23백만 건 이상**이었다고 한다. 같은 절은 **Alibaba**에 더 큰 규모, 즉 같은 May~July 기간 "over 151 million exchanges observed"를 귀속시킨다. Moonshot 총량의 약 여섯 배 반이다. 또 **DeepSeek**, **Z.ai**(Zhipu), **Xiaomi**, **MiniMax**, **SenseTime**을 명명하며 DeepSeek가 세션 간 재생 기법으로 Claude Opus 추론 흔적을 뽑았다고 설명한다. 모든 수치에는 같은 단서가 붙는다. 모두 고발 당사자 Anthropic이 조사·공개한 경쟁사 상대 의혹이며 독립 판정은 없다. 수치 자체는 보고서 증류 절에서 읽어 왔다. 이 가이드에서 중요한 점은 9장이 중국 공개 가중치 출시를 생태계 전략, 종속 효과, 인재와 호의로 해석한다면, 이것은 같은 시기를 태평양 반대편에서 적대적으로 읽은 대응 해석이라는 것이다. 공개된 역량 일부를 비공개 경쟁사에서 추출했다는 의혹이다(9장).

<a id="september-11-2026-salesforce-ships-a-long-horizon-runtime-for-agentforce"></a><!-- i18n-anchor -->

### September 11, 2026 --- Salesforce, Agentforce용 장기 실행 런타임 출시

Salesforce가 단일 과제나 상호작용을 끝내는 대신 여러 날과 여러 주에 걸쳐 목표를 추구하도록 만든 Agentforce **장기 실행 런타임**을 발표했다. 직무별 에이전트 일곱 개와 함께 제시했다. 여섯 개는 정식 제공되고, 아웃바운드 영업용 **Hunter** 하나는 시험 도입 중이며 정식 출시는 November 2026 예정이었다. Hunter가 새 런타임의 첫 에이전트다. Salesforce는 더 많은 에이전트가 이동할 것이며 고객도 자체 장기 에이전트를 구축할 수 있다고 한다. 주장을 지탱하는 명시적 구성 요소는 세 가지다. 세션 간 맥락을 유지하는 **메모리**, 세션을 넘어 계획 실행을 지속하는 **영속 실행**, 실행 도중 사용자가 행동을 조정하는 **동적 조향**이다. 같은 물결에서 Multi-Agent Orchestration도 정식 출시됐다. 여기의 모든 기능 설명은 Salesforce 자체 설명이며 특히 여러 주에 걸친 목표 추구에는 독립 증거가 없다. 시연용으로 만든 에이전트부터 아직 정식 제공되지 않는다. 이 가이드에서 중요한 점은 위 August 6 AWS 항목이 기반에 14일 에이전트 세션을 넣었다면, 이것은 같은 선택의 수요 측 절반이라는 것이다. 실제 운영 플랫폼이 긴 시간을 용량 상한이 아니라 제품으로 판매한다. 둘 사이 거리는 아직 측정되지 않았다(4장).

<a id="september-15-2026-chapter-14s-survival-gate-comes-due"></a><!-- i18n-anchor -->

### September 15, 2026 --- 14장의 생존 게이트 판정 시점 도래

14장은 July 2026에 결론 대신 구월에 확인할 네 신호의 게이트로 끝났다. 확인을 수행한 결과는 보존할 가치가 있는 경계를 따라 갈린다. **신호 1, 공급업체 용어는 여전히 비어 있으며**, 이 기간 가장 강력한 새 증거도 명칭을 지지하기보다 반대한다. OpenAI Codex는 June 19와 June 22, 2026에 병합한 PR에서 에이전트 위임을 `none`, `explicitRequestOnly`, `proactive`의 세 상태 `multiAgentMode`로 통합했고 June 22 `rust-v0.142.0`에 처음 출시했다. 용어가 생기기 한 달 전, Anthropic의 `ListAgents`/`SendMessage`보다 일곱 주 전이며 해당 단어를 한 번도 쓰지 않았다. `none`은 위임 도구를 남겨 두고 모드 지침만 제거한다고 문서화되어 있으므로 강제 인가가 아니라 프롬프트 수준 정책이다. **신호 2는 약한 긍정으로 이동했다**. $6.93짜리 Graph Engineering Mastery 과정은 감독자-전문가 계층, 분산과 합류, 병합 로직, 앵커를 단위 테스트 가능한 연습을 포함한 실제 수업으로 가르친다. 다만 강사와 인증을 명시하지 않고 바닥글에 "The Case006 for Justdoit.work"라고만 밝힌다. October 16 AgentEng London에는 여전히 그래프 트랙이 공개되지 않았다. **신호 3은 소급하여 긍정으로 이동했다**. Anthropic의 June 2025 "How we built our multi-agent research system"은 배포된 오케스트레이터-작업자 토폴로지, 대표 질의 약 스무 개의 LLM 판정 평가, 실패 후 재개, 레인보우 배포, 단일 에이전트 대비 90.2% 내부 비교를 공개한다. Stripe minions가 설정한 공개 증거 수준의 운영 사례지만 명칭보다 열세 달 앞서 발표돼 14장 초안에서 놓쳤다. 13장은 루프 엔지니어링 명칭보다 앞선 Stripe minions도 포함하므로 같은 기준을 여기에도 적용한다. **신호 4는 유지된다**. 촉발 글에 대한 답글이 아닌 에세이가 팔월과 구월에도 계속됐다. September 1 SmartScope와 September 14의 실습형 Towards Data Science 튜토리얼이 포함된다. 둘에는 정정 하나가 따른다. 구월 에세이가 반박하는 사망 선언은 그래프가 아니라 *루프* 엔지니어링의 것이다. 이 가이드에서 중요한 점은 게이트를 발표한 가이드라면 결과가 갈려도 공개해야 한다는 것이다. 이번 결과는 갈린다. 용어는 실제로 명시한 유통 시험을 통과했지만 독립된 엔지니어링 계층이라는 지위는 입증되지 않아 번호를 매긴 세대에는 포함되지 않는다. 판정을 확정할 공급업체 제품 용어 사용이나 이름 있는 콘퍼런스 트랙 중 어느 것도 September 15, 2026까지 모은 증거로는 확인되지 않았다(14장, 1장, 용어집).

---

<a id="september-23-2026-on-device-context-becomes-a-shared-service"></a><!-- i18n-anchor -->

### September 23, 2026: 기기 내 컨텍스트가 공유 서비스로 전환

[Liquid AI가 Qualcomm Snapdragon용 Liquid Context를 발표했다](https://www.liquid.ai/blog/liquid-context-qualcomm). 로컬에서 유지하는 영속적이고 권한이 적용된 컨텍스트를 임베디드·클라우드·혼합 에이전트에 제공한다. 컨텍스트 유지와 이를 소비하는 모델을 분리하면 로컬 배포가 추론을 넘어 확장된다. 이는 OEM 대상 발표이며 소비자 대규모 배포, 측정된 전력 효율, 완전 오프라인 실행의 증거가 아니다. [12장](12-local-models.md)을 참조하라.

<a id="september-29-2026-local-models-gain-a-typed-decision-endpoint"></a><!-- i18n-anchor -->

### September 29, 2026: 로컬 모델에 타입이 지정된 의사결정 엔드포인트 추가

[Ollama가 `/v1/systemone`을 도입했다](https://ollama.com/blog/ollama-now-supports-jev-style-decision-models). 상태와 타입이 지정된 질문을 받아 확률을 포함한 결정을 반환한다. [Cloudflare의 October 1 Clef 발표](https://blog.cloudflare.com/clef-decision-models)는 두 번째 Jev 호환 구현을 제공한다. 이 패턴은 자유 형식 생성 대신 범위가 제한된 라우팅과 분류를 지원한다. 권한은 여전히 애플리케이션 코드가 담당하며 반환 확률은 보정의 보장이 아니다. [12장](12-local-models.md)을 참조하라.

<a id="october-9-2026-evaluation-containment-becomes-part-of-the-harness"></a><!-- i18n-anchor -->

### October 9, 2026: 평가 격리가 하네스의 일부로 편입

[Anthropic이 평가 및 내부 사용에서 의도하지 않은 모델 행동을 공개하고](https://www.anthropic.com/research/investigating-unintended-model-actions), 도구 제한, 행동 차단기 추가, 격리 확인이 끝날 때까지 내부 평가 전반의 실시간 인터넷 접근 중단을 설명했다. 글은 October 12에 정정됐다. 평가 성공이 평가자가 운영 경계를 지켰음을 입증하지는 않는다. 이는 특정 시점의 시정 조치 보고이지 모든 평가가 계속 오프라인이라는 주장이 아니다. [4장](04-harness-engineering.md)을 참조하라.

<a id="october-13-2026-a-shared-workspace-becomes-governed-agent-context"></a><!-- i18n-anchor -->

### October 13, 2026: 공유 작업 공간이 통제된 에이전트 컨텍스트로 전환

[Notion 3.8](https://www.notion.com/releases/2026-10-13)은 영속 작업 공간 컨텍스트를 GitHub로 게시하는 재사용 스킬, 변경 주체 기록과 복원, 데이터베이스 속성 권한, 사용자별 MCP 철회에 연결한다. 공급업체가 설명한 이 인터페이스들은 에이전트 접근과 함께 공유 지식의 소유권 및 변경 통제를 드러낸다. 유출 방지나 모든 클라이언트 호환성을 독립적으로 입증하지는 않는다. [8장](08-tools-landscape.md)을 참조하라.

<a id="october-14-2026-a-customer-case-makes-the-outer-harness-concrete"></a><!-- i18n-anchor -->

### October 14, 2026: 고객 사례가 외부 하네스를 구체화

[OpenAI의 Third Moment Research 사례 연구](https://openai.com/index/third-moment-research/)는 여러 날에 걸친 연구에서 미완료 Codex 궤적을 조사하고 재시도, 종료, 사람에게 에스컬레이션 중 하나를 선택하는 두 번째 하네스를 설명한다. 고객/공급업체 공개이며 완료율이나 비용의 독립 평가는 없다. 아키텍처 증거는 경과 시간 자체가 아니라 작업자 실행과 계속할지의 판단을 분리했다는 점이다. [13장](13-loop-engineering.md)을 참조하라.

<a id="october-22-2026-monitor-evaluation-crosses-agent-and-compaction-boundaries"></a><!-- i18n-anchor -->

### October 22, 2026: 감시기 평가가 에이전트 및 압축 경계를 넘음

[Anthropic의 적대적 감시기 연구](https://alignment.anthropic.com/2026/red-teaming-auto-mode/)는 인가를 잘못 전달하는 요약이나 인계를 포함해 압축과 다중 에이전트에 걸친 공격을 조사한다. 구월 스냅샷은 Auto Mode와 Codex Guardian의 근사 구현을 시험하며, 실험적 완화책은 출시 제품의 보장이 아니다. 새 평가 질문은 개별 호출을 확인했는지만이 아니라 궤적 전체에서 인가를 계속 신뢰할 수 있는지다. [4장](04-harness-engineering.md)을 참조하라.

<a id="october-22-2026-agent-skills-records-broader-cross-vendor-adoption"></a><!-- i18n-anchor -->

### October 22, 2026: Agent Skills, 공급업체 간 채택 확대 기록

[Anthropic이 Agent Skills의 AAIF 기증을 발표하며](https://www.anthropic.com/news/donating-agent-skills-to-the-agentic-ai-foundation) 에이전트 플랫폼 70개 이상이 채택했다고 보고했다. 이는 새 실행 기본 요소가 아니라 상호 운용성 이정표다. 명칭, 저장소 조직, 도메인은 관리 주체를 바꾸지만 버전별 릴리스와 보안 지침은 여전히 제안된 작업이다. 채택 수는 공급업체 수치이며, 이식 가능한 스킬 형식이 안전한 실행을 입증하지는 않는다. [5장](05-skill-systems.md)을 참조하라.

<a id="october-29-2026-memory-conflict-decisions-get-a-durable-lifecycle"></a><!-- i18n-anchor -->

### October 29, 2026: 메모리 충돌 결정에 영속 수명 주기 추가

[Cognee v1.6.6](https://github.com/topoteretes/cognee/releases/tag/v1.6.6)은 영속적인 사실 충돌 해결을 API로 노출하고 검토를 기본 활성화하며, 근거 자료가 바뀌거나 삭제되면 해결 결정을 폐기한다. 릴리스 노트가 입증하는 것은 소프트웨어가 주장하는 계약이지 독립 검증된 정확성이나 삭제 보장은 아니다. 이 기본 요소는 다른 메모리를 검색하는 데 그치지 않고 정정 후 어느 이전 결정이 여전히 유효한지 유지하는 것이다. [6장](06-agent-memory.md)을 참조하라.

---

<a id="the-pattern"></a><!-- i18n-anchor -->

## 패턴

이 연표를 위에서 아래로 읽으면 하나의 패턴이 나타난다.

**2022-2023**: 모델이 제품이다. 프롬프트 엔지니어링이 기술이다. RAG가 아키텍처다.

**2024**: 컨텍스트 창이 확장되고 프로토콜이 표준화된다. 논의가 "what can the model do"에서 "what can we build around the model."로 이동한다.

**2025**: 컨텍스트 엔지니어링이 프롬프트 엔지니어링을 대체한다. 스킬, 에이전트, 하네스가 주요 엔지니어링 영역이 된다. 오픈소스 모델이 기반 계층을 범용 상품으로 만든다. MCP가 인프라가 된다.

**2026**: 하네스가 제품이지만 사월이 되면 그 설명만으로는 부족해진다. 상태 유지 프로토콜(SEP-1686 Tasks, 양방향 MCP 런타임)이 MCP를 오케스트레이션 계층으로 바꾼다. 점진적 공개가 공급업체 공통 표준이 된다. 그래프 메모리(Mem0ᵍ)가 전체 컨텍스트 방식과 선택적 검색 방식의 간극을 메운다. AI Velocity Paradox는 최전선의 문제를 다시 정의한다. 이제 병목은 생성이 아니라 평가와 거버넌스다.

**April 2026은 이 패턴을 더 선명하게 만든다.** 네 흐름이 2026년의 지배적 서사로 등장한다.

- **안전 병목으로서의 해석 가능성.** 기계적 해석 가능성이 일월에 혁신 기술로 인정받고 사월에 첫 실제 운영 결과를 낸다. Anthropic의 감정 벡터와 반복 헤드, OpenAI가 부정행위 추론 모델을 사고 사슬로 적발한 사례다. 회로 수준에서 모델을 읽고 조종하는 특성 수준 제어가 연구상의 흥미에서 런타임 인터페이스로 이동한다. 하네스에 새 센서 유형이 생긴다.
- **새 확장 축으로서의 테스트 시점 연산.** CATTS는 테스트 시점 연산이 예산 문제가 아니라 *집중 대상 선택*의 문제임을 입증한다. 합의 인식 불확실성으로 롤아웃을 유도하면 토큰을 2.3x 적게 쓰면서 9.1% 향상된다. Advisor Tool과 결합하면 두 축의 최적화가 성립한다. 한 축은 무엇을 생각할지 고르고 다른 축은 얼마나 깊이 생각할지 고른다.
- **클라우드 네이티브 하네스 기본 요소.** Claude Code Routines(April 14)는 일정 / API / GitHub 이벤트로 시작되는 에이전트 루프의 첫 관리형 기반을 제공했다. 사월 말까지 기반은 더 분해됐다. Anthropic Managed Agents(April 8)는 오케스트레이터 실행 자리 자체에 $0.08/세션-시간을 매겼고, Memory for Managed Agents(April 23)는 감사 로그를 갖춘 세션 간 영속 상태를 더했다. AWS-OpenAI Bedrock Managed Agents(April 28, 한정 프리뷰)는 같은 형태에 대한 공급업체 간 수렴을 확인했다. 세 프런티어 공급업체 중 둘이 이제 오케스트레이터 실행 자리를 관리형 기본 요소로 판매한다. 선택의 초점은 브라우저 자동화, 한 분 미만 주기, 기기 내 데이터, GitHub 이외 트리거처럼 아직 자체 호스팅이 필요한 작업으로 옮겨 간다.
- **학습 가능한 모듈로서의 메모리.** Titans + MIRAS는 메모리를 외부 벡터 저장소가 아니라 추론 시 경사 하강법으로 갱신하는 신경 모듈로 만들어 긴 컨텍스트를 새롭게 정의한다. 비슷한 크기에서 장거리 회상 성능이 Mamba-2, Gated DeltaNet, Transformer++보다 높다. 지식 계층은 어텐션 창과 검색 파이프라인에 더해 세 번째 선택지인 *학습된 메모리*를 얻는다.
- **하네스 합성이 실현 가능한 엔지니어링 영역으로 전환.** 사월 말은 Meta-Harness(삼월) → AHE(April 28) → AgentFlow(사월 말) 경로를 압축한다. 이제 하네스는 관측 가능성 루프로 최적화되고(AHE: Terminal-Bench 2에서 69.7% → 77.0%, 모델 계열 간 전이 포함), 타입 그래프로 합성된다(AgentFlow: Opus 4.6으로 TerminalBench-2에서 84.3%, 같은 루프를 Kimi K2.5로 Chrome에 재실행해 외부 검증된 제로데이 CVE 열 개도 발견). 오늘 선임 하네스 엔지니어가 수동으로 내리는 설계 선택을 내일은 합성 루프가 자동으로 내릴 것이다. AgentFlow의 이중 용도 신호, 즉 공격 역량으로서의 합성은 반대 방향에서 Mythos / Glasswing 서사를 완성한다.

ARC-AGI-3는 이 다섯 흐름 위에서 기존 기준으로 평가하기를 거부하는 벤치마크로 자리한다. 에이전트는 지시 없이 자체 세계 모델을 구축해야 한다. 이는 지시 이행과 자율적 문제 정의가 같지 않음을 이 분야에 상기시킨다.

**2026년 중반에는 사월의 사건들이 예상하지 못한 여섯 번째 흐름이 추가된다. 정부가 배포 루프에 들어온다.** 프런티어 AI에 관한 June 2 행정명령, 이미 정식 출시한 Fable 5와 Mythos 5를 전 세계에서 중단시킨 June 12 수출 통제, 정부가 부과한 June 26 GPT-5.6 검증 프리뷰는 질적인 변화를 나타낸다. 프런티어 역량의 배포는 더 이상 공급업체가 고르는 등급(Glasswing, Trusted Access for Cyber)에만 머물지 않고 *규제 대상 영역*이 된다. 그 규제를 강제하는 계층은 Fable 5의 `stop_reason`으로서의 거부 기본 요소, Fable 5의 July 1 복귀를 제한한 CAISI 검증 분류기 등 하네스 자체의 안전 장치다. 지식 엔지니어에게 규정 준수는 하네스를 감싸는 포장 계층이 아니라 하네스가 직접 구현해야 하는 속성이 된다.

방향은 명확하다. 이 이야기의 다음 장은 더 큰 모델이 아니라 더 나은 시스템에 관한 것이다. 2026년에 "better systems"는 하네스가 프롬프트를 보내기만 하는 시스템을 넘어 *읽고*, *조종하고*, *연산을 배분할 수 있는* 시스템을 점점 더 뜻한다.

---

<a id="three-things-to-take-away"></a><!-- i18n-anchor -->

## 기억할 세 가지

- **이 목록은 전부가 아니라 선별된 것이다.** 이 프레임워크가 추적하는 기본 요소, 패턴, 서사적 전환점을 도입하거나 검증하거나 실제 운영으로 옮긴 사건만 한 줄을 차지한다.
- **2026년에는 병목이 생성에서 이동했다.** AI Velocity Paradox는 최전선의 제한 요소가 생성 속도가 아니라 평가와 거버넌스임을 보여 준다.
- **규정 준수가 하네스 자체의 속성이 되었다.** 2026년 중반 프런티어 역량의 배포가 규제 대상이 되면서 안전 장치는 하네스 주위가 아니라 안에 있어야 한다.

---

<a id="sources"></a><!-- i18n-anchor -->

## 출처

- OpenAI, "Introducing ChatGPT" (November 30, 2022)
- LangChain GitHub 저장소: [https://github.com/langchain-ai/langchain](https://github.com/langchain-ai/langchain)
- LlamaIndex GitHub 저장소: [https://github.com/run-llama/llama_index](https://github.com/run-llama/llama_index)
- OpenAI DevDay 기조연설, GPT-4 Turbo 발표(November 2023)
- Google, "Gemini 1.0: Our Largest and Most Capable AI Model" (December 2023)
- Google, "Gemini 1.5: Our Next-Generation Model" (February 2024)
- Anthropic, "Introducing the Model Context Protocol" (November 2024)
- DeepSeek, "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning" (January 2025)
- Moonshot AI, Kimi 긴 컨텍스트 기술 블로그(March 2024)
- Karpathy, A., 컨텍스트 엔지니어링 관련 발언(mid-2025)
- Manus, "Context Engineering for AI Agents" 블로그 글(July 2025)
- Notion, "Introducing Notion 3.0" (September 2025)
- Anthropic, "Agent Skills" 문서(October 2025)
- Linux Foundation, "MCP Joins the Linux Foundation" 발표(December 2025)
- Anthropic, agentskills.io 공개 표준(December 2025)
- Baidu, ERNIE 5.0 출시(January 2026)
- Moonshot AI, Kimi K2.5 Agent Swarm (January 2026)
- Heinrich (@arscontexta), 스킬 그래프 개념 --- 2026년 초 X 글: [https://x.com/arscontexta/status/2023957499183829467](https://x.com/arscontexta/status/2023957499183829467); GitHub: [https://github.com/agenticnotetaking/arscontexta](https://github.com/agenticnotetaking/arscontexta)
- "Meta-Harness: Quantifying the Impact of Harness Engineering on LLM Performance" (March 2026)
- "SkillReducer: Managing Skill Proliferation in Large-Scale Agent Systems" (March 2026)
- MCP SDK 다운로드 통계, npm/PyPI (Q1 2026)
- MIT Technology Review, "10 Breakthrough Technologies of 2026: Mechanistic Interpretability" (January 12, 2026): [https://www.technologyreview.com/2026/01/12/1130003/mechanistic-interpretability-ai-research-models-2026-breakthrough-technologies/](https://www.technologyreview.com/2026/01/12/1130003/mechanistic-interpretability-ai-research-models-2026-breakthrough-technologies/)
- Chollet 외, "ARC-AGI-3: Interactive Benchmarks for Agentic Intelligence," arXiv 2603.24621 (April 2026): [https://arxiv.org/html/2603.24621v1](https://arxiv.org/html/2603.24621v1)
- "CATTS: Consensus-Aware Test-Time Scaling for Agents," arXiv 2602.12276 (February 2026): [https://arxiv.org/abs/2602.12276](https://arxiv.org/abs/2602.12276)
- Google Research, "Titans + MIRAS: Helping AI Have Long-Term Memory" (April 2026): [https://research.google/blog/titans-miras-helping-ai-have-long-term-memory/](https://research.google/blog/titans-miras-helping-ai-have-long-term-memory/)
- Anthropic 해석 가능성 팀, 감정 벡터와 반복 헤드 공개(April 2026)
- OpenAI, 추론 모델 부정행위 사건의 사고 사슬 모니터링 공개(April 2026)
- Anthropic, "Introducing Routines in Claude Code" (April 14, 2026): [https://claude.com/blog/introducing-routines-in-claude-code](https://claude.com/blog/introducing-routines-in-claude-code) 및 [https://code.claude.com/docs/en/routines](https://code.claude.com/docs/en/routines)
- Archon GitHub 저장소: [https://github.com/coleam00/Archon](https://github.com/coleam00/Archon) --- v2.1 TypeScript / Bun 재작성은 April 2026 출시; 월말까지 별 약 19K.
- OpenHarness GitHub 저장소: [https://github.com/HKUDS/OpenHarness](https://github.com/HKUDS/OpenHarness) --- HKUDS, MIT 라이선스, 첫 커밋 April 1, 2026; 세 주간 별 약 11K.
- MemPalace GitHub 저장소: [https://github.com/MemPalace/mempalace](https://github.com/MemPalace/mempalace) --- MIT 라이선스, 첫 커밋 April 5, 2026; 세 주간 별 약 49K.
- "Spatial Metaphors for LLM Memory: A Critical Analysis of the MemPalace Architecture," arXiv 2604.21284 (April 2026): [https://arxiv.org/abs/2604.21284](https://arxiv.org/abs/2604.21284)
- Anthropic, "Introducing Claude Opus 4.7" (April 16, 2026): [https://www.anthropic.com/news/claude-opus-4-7](https://www.anthropic.com/news/claude-opus-4-7)
- Anthropic API 문서, "What's new in Claude Opus 4.7": [https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-7](https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-7) --- 작업 예산 베타 헤더, 적응형 전용 사고, temperature/top_p/top_k 400 오류.
- Caylent, "Claude Opus 4.7 Deep Dive: Capabilities, Migration, and the New Economics of Long-Running Agents" (April 2026): [https://caylent.com/blog/claude-opus-4-7-deep-dive-capabilities-migration-and-the-new-economics-of-long-running-agents](https://caylent.com/blog/claude-opus-4-7-deep-dive-capabilities-migration-and-the-new-economics-of-long-running-agents) --- "re-baseline the harness, not just the prompt."
- DeepSeek, Hugging Face V4 모델 출시(April 24, 2026). MIT 라이선스; V4-Pro 1.6T / V4-Flash 284B; 기본 1M 토큰 컨텍스트.
- Fortune, "DeepSeek unveils V4 model, with rock-bottom prices and close integration with Huawei's chips" (April 24, 2026): [https://fortune.com/2026/04/24/deepseek-v4-ai-model-price-performance-china-open-source/](https://fortune.com/2026/04/24/deepseek-v4-ai-model-price-performance-china-open-source/)
- South China Morning Post, "DeepSeek unveils next-gen AI model as Huawei vows 'full support' with new chips" (April 24, 2026): [https://www.scmp.com/tech/big-tech/article/3351239/deepseek-releases-next-gen-ai-model-world-leading-efficiency](https://www.scmp.com/tech/big-tech/article/3351239/deepseek-releases-next-gen-ai-model-world-leading-efficiency)
- Resultsense, "Anthropic probes unauthorised access to Claude Mythos" (April 23, 2026): [https://www.resultsense.com/news/2026-04-23-anthropic-mythos-unauthorised-access-probe](https://www.resultsense.com/news/2026-04-23-anthropic-mythos-unauthorised-access-probe)
- Schneier on Security, "On Anthropic's Mythos Preview and Project Glasswing" (April 2026): [https://www.schneier.com/blog/archives/2026/04/on-anthropics-mythos-preview-and-project-glasswing.html](https://www.schneier.com/blog/archives/2026/04/on-anthropics-mythos-preview-and-project-glasswing.html)
- Arnav.au, "Anthropic Mythos AI Breach 2026" (April 29, 2026): [https://arnav.au/2026/04/29/anthropic-mythos-ai-breach-2026/](https://arnav.au/2026/04/29/anthropic-mythos-ai-breach-2026/)
- Anthropic, "Claude Managed Agents overview" (April 8, 2026): [https://platform.claude.com/docs/en/managed-agents/overview](https://platform.claude.com/docs/en/managed-agents/overview)
- Anthropic Engineering, "Scaling Managed Agents: Decoupling the brain from the body" (April 2026): [https://www.anthropic.com/engineering/managed-agents](https://www.anthropic.com/engineering/managed-agents)
- SiliconANGLE, "Anthropic launches Claude Managed Agents to speed up AI agent development" (April 8, 2026): [https://siliconangle.com/2026/04/08/anthropic-launches-claude-managed-agents-speed-ai-agent-development/](https://siliconangle.com/2026/04/08/anthropic-launches-claude-managed-agents-speed-ai-agent-development/)
- InfoWorld, "Anthropic rolls out Claude Managed Agents" (April 2026): [https://www.infoworld.com/article/4156852/anthropic-rolls-out-claude-managed-agents.html](https://www.infoworld.com/article/4156852/anthropic-rolls-out-claude-managed-agents.html)
- Microsoft Official Blog, "The next phase of the Microsoft-OpenAI partnership" (April 27, 2026): [https://blogs.microsoft.com/blog/2026/04/27/the-next-phase-of-the-microsoft-openai-partnership/](https://blogs.microsoft.com/blog/2026/04/27/the-next-phase-of-the-microsoft-openai-partnership/)
- OpenAI, "The next phase of the Microsoft partnership" (April 27, 2026): [https://openai.com/index/next-phase-of-microsoft-partnership/](https://openai.com/index/next-phase-of-microsoft-partnership/)
- CNBC, "OpenAI shakes up partnership with Microsoft, capping revenue share payments" (April 27, 2026): [https://www.cnbc.com/2026/04/27/openai-microsoft-partnership-revenue-cap.html](https://www.cnbc.com/2026/04/27/openai-microsoft-partnership-revenue-cap.html)
- PitchBook, "OpenAI loosens Microsoft's grip ahead of IPO push" (April 2026): [https://pitchbook.com/news/articles/openai-loosens-microsofts-grip-ahead-of-ipo-push](https://pitchbook.com/news/articles/openai-loosens-microsofts-grip-ahead-of-ipo-push)
- Lin 외, "Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses," arXiv 2604.25850 (April 28, 2026): [https://arxiv.org/abs/2604.25850](https://arxiv.org/abs/2604.25850)
- Agentic Harness Engineering 관련 저장소: [https://github.com/china-qijizhifeng/agentic-harness-engineering](https://github.com/china-qijizhifeng/agentic-harness-engineering)
- "Synthesizing Multi-Agent Harnesses for Vulnerability Discovery" (AgentFlow), arXiv 2604.20801 (April 2026): [https://arxiv.org/abs/2604.20801](https://arxiv.org/abs/2604.20801)
- Anthropic, "Memory for Claude Managed Agents" (April 23, 2026): [https://claude.com/blog/claude-managed-agents-memory](https://claude.com/blog/claude-managed-agents-memory)
- AWS, "Amazon Bedrock now offers OpenAI models, Codex, and Managed Agents (Limited Preview)" (April 28, 2026): [https://aws.amazon.com/about-aws/whats-new/2026/04/bedrock-openai-models-codex-managed-agents/](https://aws.amazon.com/about-aws/whats-new/2026/04/bedrock-openai-models-codex-managed-agents/)
- About Amazon, "AWS and OpenAI announce expanded partnership to bring frontier intelligence to the infrastructure you already trust" (April 28, 2026): [https://www.aboutamazon.com/news/aws/bedrock-openai-models](https://www.aboutamazon.com/news/aws/bedrock-openai-models)
- OpenAI, "OpenAI models, Codex, and Managed Agents come to AWS" (April 28, 2026): [https://openai.com/index/openai-on-aws/](https://openai.com/index/openai-on-aws/)
- Anthropic 블로그, "New in Claude Managed Agents: dreaming, outcomes, and multiagent orchestration" (May 6, 2026): [https://claude.com/blog/new-in-claude-managed-agents](https://claude.com/blog/new-in-claude-managed-agents) --- Dreaming 연구 미리보기, Outcomes와 Multiagent Orchestration 공개 베타; Harvey 시범 데이터.
- Simon Willison, Code w/ Claude 2026 SF 현장 블로그 (May 6, 2026): [https://simonwillison.net/2026/May/6/code-w-claude-2026/](https://simonwillison.net/2026/May/6/code-w-claude-2026/)
- VentureBeat, "Anthropic introduces 'dreaming,' a system that lets AI agents learn from their own mistakes" (May 6, 2026) --- Dreaming을 학습된 메모리 통합의 제품화로 설명.
- The New Stack, "Anthropic will let its managed agents dream" (May 2026) --- 독립적인 이차 보도.
- AWS What's New, "AWS MCP Server now generally available" (May 6, 2026): [https://aws.amazon.com/about-aws/whats-new/2026/05/aws-mcp-server/](https://aws.amazon.com/about-aws/whats-new/2026/05/aws-mcp-server/)
- AWS News Blog, "The AWS MCP Server is now generally available" (May 6, 2026): [https://aws.amazon.com/blogs/aws/the-aws-mcp-server-is-now-generally-available/](https://aws.amazon.com/blogs/aws/the-aws-mcp-server-is-now-generally-available/) --- 인증 서버 하나에 API 작업 15,000개 이상; IAM 컨텍스트 키; 샌드박스 `run_script`; 표준 에이전트 진입점으로 "Skills over SOPs".
- Techstrong.ai, AWS MCP Server 정식 출시의 독립 보도 (May 2026).
- AWS What's New, "Agents that transact: Amazon Bedrock AgentCore now includes Payments (preview)" (May 7, 2026): [https://aws.amazon.com/about-aws/whats-new/2026/04/amazon-bedrock-agentcore-payments-preview/](https://aws.amazon.com/about-aws/whats-new/2026/04/amazon-bedrock-agentcore-payments-preview/) --- URL 경로는 `/04/`이지만 출시는 May 7, 2026이다.
- AWS Machine Learning Blog, "Agents that transact: Introducing Amazon Bedrock AgentCore payments, built with Coinbase and Stripe" (May 7, 2026): [https://aws.amazon.com/blogs/machine-learning/agents-that-transact-introducing-amazon-bedrock-agentcore-payments-built-with-coinbase-and-stripe/](https://aws.amazon.com/blogs/machine-learning/agents-that-transact-introducing-amazon-bedrock-agentcore-payments-built-with-coinbase-and-stripe/)
- x402 명세: [https://www.x402.org/](https://www.x402.org/) 및 Coinbase 참조 구현: [https://github.com/coinbase/x402](https://github.com/coinbase/x402)
- AWS Weekly Roundup (May 11, 2026): [https://aws.amazon.com/blogs/aws/aws-weekly-roundup-amazon-bedrock-agentcore-payments-agent-toolkit-for-aws-and-more-may-11-2026/](https://aws.amazon.com/blogs/aws/aws-weekly-roundup-amazon-bedrock-agentcore-payments-agent-toolkit-for-aws-and-more-may-11-2026/) --- Payments 미리보기 확인.
- OpenAI, "GPT-5.5 with Trusted Access for Cyber" (May 11, 2026): [https://openai.com/index/gpt-5-5-with-trusted-access-for-cyber/](https://openai.com/index/gpt-5-5-with-trusted-access-for-cyber/) --- 일차 자료; 자동 크롤러에는 URL이 403을 반환할 수 있음.
- CNBC, "OpenAI launches GPT-5.5 cyber model in EU coalition, mirroring Anthropic Mythos" (May 11, 2026): [https://www.cnbc.com/2026/05/11/openai-eu-cyber-model-anthropic-mythos-gpt.html](https://www.cnbc.com/2026/05/11/openai-eu-cyber-model-anthropic-mythos-gpt.html) --- Glasswing 패턴 재현을 뒷받침하는 핵심 이차 자료.
- UK AI Safety Institute, GPT-5.5-Cyber 평가 블로그 (May 2026) --- 안전 평가를 제품으로 보는 관점.
- Anthropic 블로그, "New in Claude Managed Agents: self-hosted sandboxes and MCP tunnels" (May 19, 2026): [https://claude.com/blog/claude-managed-agents-updates](https://claude.com/blog/claude-managed-agents-updates) --- Cloudflare / Daytona / Modal / Vercel 공급자의 자체 호스팅 샌드박스 공개 베타; 경량 아웃바운드 게이트웨이의 MCP 터널 연구 미리보기.
- Anthropic API 문서, "Self-hosted sandboxes" (May 2026): [https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes)
- InfoQ, "Anthropic Introduces MCP Tunnels for Private Agent Access to Internal Systems" (May 2026): [https://www.infoq.com/news/2026/05/claude-mcp-tunnels/](https://www.infoq.com/news/2026/05/claude-mcp-tunnels/)
- The New Stack, "Anthropic debuts MCP tunnels and self-hosted sandboxes to lock down AI agent infrastructure" (May 2026): [https://thenewstack.io/anthropic-mcp-tunnels-sandboxes/](https://thenewstack.io/anthropic-mcp-tunnels-sandboxes/)
- The Decoder, "Anthropic adds self-hosted sandboxes and MCP tunnels to Claude Managed Agents" (May 2026): [https://the-decoder.com/anthropic-adds-self-hosted-sandboxes-and-mcp-tunnels-to-claude-managed-agents/](https://the-decoder.com/anthropic-adds-self-hosted-sandboxes-and-mcp-tunnels-to-claude-managed-agents/)
- Model Context Protocol 블로그, "The 2026-07-28 MCP Specification Release Candidate" (May 21, 2026 확정): [https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/) --- 무상태 프로토콜 핵심, 확장 프레임워크, MCP Apps, Tasks 확장화, 인가 강화, 공식 폐기 정책.
- The New Stack, "MCP's biggest growing pains for production use will soon be solved" (May 2026): [https://thenewstack.io/model-context-protocol-roadmap-2026/](https://thenewstack.io/model-context-protocol-roadmap-2026/) --- RC에 대한 이차 보도.
- IETF Internet-Draft, "Security Considerations for Model Context Protocol (MCP) Implementations in AI Agent Systems," `draft-mohiuddin-mcp-security-considerations-00` (June 2026; December 3, 2026 만료): [https://datatracker.ietf.org/doc/draft-mohiuddin-mcp-security-considerations/](https://datatracker.ietf.org/doc/draft-mohiuddin-mcp-security-considerations/) --- 저자 Anas Mohiuddin Syed; 여섯 취약점 유형(SSRF, 과도한 도구 권한, 프롬프트 주입 표면, 수명 주기 우회, 정보 유출, 인증 집행 공백); 오픈소스 `mcp-safeguard` 탐지 도구 명시.
- Anas Mohiuddin Syed, "I built the first security scanner for MCP servers --- here's what I found," DEV Community (2026): [https://dev.to/syedanas01/i-built-the-first-security-scanner-for-mcp-servers-heres-what-i-found-2np2](https://dev.to/syedanas01/i-built-the-first-security-scanner-for-mcp-servers-heres-what-i-found-2np2) --- 저자의 `mcp-safeguard` 관련 설명(연결된 GitHub 저장소는 초안 시점에 확인되지 않아 검증 필요로 표시).
- Microsoft AI, "Introducing MAI-Code-1-Flash" (June 2, 2026): [https://microsoft.ai/news/introducingmai-code-1-flash/](https://microsoft.ai/news/introducingmai-code-1-flash/) --- 실서비스 GitHub Copilot 하네스를 직접 대상으로 학습한 매개변수 5B 코딩 모델; 어려운 과제 토큰 약 60% 감소; Claude Haiku 4.5 대비 가격 성능 우위.
- GitHub Changelog, "MAI-Code-1-Flash is now available for GitHub Copilot" (June 2, 2026): [https://github.blog/changelog/2026-06-02-mai-code-1-flash-is-now-available-for-github-copilot/](https://github.blog/changelog/2026-06-02-mai-code-1-flash-is-now-available-for-github-copilot/)
- TechTimes, "Microsoft Build 2026: MAI-Thinking-1 Is First In-House Reasoning Model, Trained Without OpenAI Data" (June 2, 2026): [https://www.techtimes.com/articles/317631/20260602/microsoft-build-2026-mai-thinking-1-first-house-reasoning-model-trained-without-openai-data.htm](https://www.techtimes.com/articles/317631/20260602/microsoft-build-2026-mai-thinking-1-first-house-reasoning-model-trained-without-openai-data.htm) --- MAI-Thinking-1과 OpenAI 분리 관점을 뒷받침하는 이차 자료.
- Microsoft, "Microsoft Agent Framework at Build 2026: introducing the Agent Harness" (June 3, 2026): [https://devblogs.microsoft.com/agent-framework/microsoft-agent-framework-at-build-2026-announce/](https://devblogs.microsoft.com/agent-framework/microsoft-agent-framework-at-build-2026-announce/) --- 기본 MAF 확장인 Agent Harness(컨텍스트 압축, 과제 분해, 파일 메모리, 계획/실행, 스킬 발견, 하위 에이전트 분배, 샌드박스 셸).
- Microsoft Foundry, "Hosted Agents at Build 2026" (June 2, 2026): [https://devblogs.microsoft.com/foundry/hosted-agents-build26/](https://devblogs.microsoft.com/foundry/hosted-agents-build26/) --- 소스 직접 배포, 하이퍼바이저 격리 세션별 샌드박스, 에이전트별 Entra ID, 내장 OpenTelemetry.
- Apple, "Bring an LLM provider to the Foundation Models framework," WWDC26 세션 339: [https://developer.apple.com/videos/play/wwdc2026/339/](https://developer.apple.com/videos/play/wwdc2026/339/) 및 세션 241: [https://developer.apple.com/videos/play/wwdc2026/241/](https://developer.apple.com/videos/play/wwdc2026/241/) --- 공개 `LanguageModel` / `LanguageModelExecutor` Swift 프로토콜; Hugging Face mlx-community 모델용 참조 `MLXLanguageModel` 백엔드.
- Apple Newsroom, "Apple kicks off Worldwide Developers Conference on June 8" (May 2026): [https://www.apple.com/newsroom/2026/05/apple-kicks-off-worldwide-developers-conference-on-june-8/](https://www.apple.com/newsroom/2026/05/apple-kicks-off-worldwide-developers-conference-on-june-8/) --- WWDC26 날짜 출처.
- Anthropic, "Claude Fable 5 and Claude Mythos 5" (June 9, 2026): [https://www.anthropic.com/news/claude-fable-5-mythos-5](https://www.anthropic.com/news/claude-fable-5-mythos-5) 및 API 문서, "Introducing Claude Fable 5 and Claude Mythos 5": [https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5](https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5) --- 거절 `stop_reason`(HTTP 200), `fallbacks` 계약, 대체 크레딧 과금; 1M 컨텍스트 / 128K 출력; 백만 토큰당 $10 / $50; "more than 95% of Fable sessions"는 분류기 개입 없이 완료.
- Anthropic, "Redeploying Fable 5" (July 2026): [https://www.anthropic.com/news/redeploying-fable-5](https://www.anthropic.com/news/redeploying-fable-5) --- June 12 수출 통제로 Fable 5와 Mythos 5 중단; 단계적 복구(Mythos 5 June 26, Fable 5 July 1); CAISI 검증; Amazon/Microsoft/Google 파트너 명시.
- Anthropic, "A jailbreak-severity framework for frontier safeguards" (July 2, 2026): [https://www.anthropic.com/news/fable-safeguards-jailbreak-framework](https://www.anthropic.com/news/fable-safeguards-jailbreak-framework) --- Glasswing 파트너와 초안 작성한 Anthropic의 네 축 평가 기준(공개 공동 표준은 아님).
- AWS What's New, "Amazon Bedrock AgentCore harness is now generally available" (June 17, 2026): [https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-bedrock-agentcore-harness-generally-available/](https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-bedrock-agentcore-harness-generally-available/) 및 AWS Machine Learning Blog, "…go from idea to production-grade agent in minutes": [https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-agentcore-harness-is-now-generally-available-go-from-idea-to-production-grade-agent-in-minutes/](https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-agentcore-harness-is-now-generally-available-go-from-idea-to-production-grade-agent-in-minutes/) --- `CreateHarness` / `InvokeHarness`; 공급자 중립(Bedrock, OpenAI, Gemini, LiteLLM); "if the model is the brain, the harness is the body."
- Model Context Protocol 블로그, "Enterprise-Managed Authorization" (June 18, 2026): [https://blog.modelcontextprotocol.io/posts/enterprise-managed-auth/](https://blog.modelcontextprotocol.io/posts/enterprise-managed-auth/) 및 명세, "Enterprise-Managed Authorization": [https://modelcontextprotocol.io/extensions/auth/enterprise-managed-authorization](https://modelcontextprotocol.io/extensions/auth/enterprise-managed-authorization) --- Paul Carleton 발표; ID-JAG 토큰 교환; 첫날 Okta / Anthropic / VS Code / 일곱 서버 지원.
- Terminal-Bench, "Terminal-Bench Challenges" (June 18, 2026): [https://www.tbench.ai/news/terminal-bench-challenges](https://www.tbench.ai/news/terminal-bench-challenges) --- 여러 날, 무제한, 무개입 벤치마크군; 초기 Rust 컴파일러 과제(Claude Code + Opus 4.8, 12시간, 성능 퇴보).
- OpenAI, "Previewing GPT-5.6 Sol" (June 26, 2026): [https://openai.com/index/previewing-gpt-5-6-sol/](https://openai.com/index/previewing-gpt-5-6-sol/) 및 "GPT-5.6" 정식 출시 (July 9, 2026): [https://openai.com/index/gpt-5-6/](https://openai.com/index/gpt-5-6/) --- 행정명령에 따른 파트너 약 20곳의 정부 제한 미리보기; Sol/Terra/Luna 가격; `max`와 `ultra`(하위 에이전트 분배) 모드.
- METR, "GPT-5.6 Sol evaluation" (June 26, 2026): [https://metr.org/blog/2026-06-26-gpt-5-6-sol/](https://metr.org/blog/2026-06-26-gpt-5-6-sol/) --- Time Horizon 1.1의 공개 모델 최고 부정행위 적발률; 부정행위 계산에 따라 50% 시간 지평 약 11.3시간 대 >270시간; Apollo 공동 독립 검토(말로 드러난 시험 인지 16% 대 이전 43%).
- TechNode, "DeepSeek to launch V4 in mid-July with new peak-time API pricing" (June 30, 2026): [https://technode.com/2026/06/30/deepseek-to-launch-v4-in-mid-july-with-new-peak-time-api-pricing/](https://technode.com/2026/06/30/deepseek-to-launch-v4-in-mid-july-with-new-peak-time-api-pricing/) 및 ExplainX, "DeepSeek V4 official release, peak pricing, mid-July 2026": [https://explainx.ai/blog/deepseek-v4-official-release-peak-pricing-mid-july-2026](https://explainx.ai/blog/deepseek-v4-official-release-peak-pricing-mid-july-2026) --- mid-July 공식 출시; 혼잡 시간 요금은 비혼잡의 2x(베이징 9:00-12:00, 14:00-18:00).
- Tencent, Hy3 (Hunyuan 3.0) Hugging Face 모델 카드 (July 6, 2026): [https://huggingface.co/tencent/Hy3](https://huggingface.co/tencent/Hy3) --- 295B MoE(활성 21B), 256K 컨텍스트, Apache 2.0; 환각률 12.5% → 5.4%; 전문가 블라인드 평가 2.67/4 대 GLM-4 2.51/4. 이차 자료: LetsDataScience, "Tencent open-sources Hy3 295B MoE model": [https://letsdatascience.com/news/tencent-open-sources-hy3-295b-moe-model-c3d05258](https://letsdatascience.com/news/tencent-open-sources-hy3-295b-moe-model-c3d05258).
- Anthropic, "A global workspace in language models" (July 6, 2026): [https://www.anthropic.com/research/global-workspace](https://www.anthropic.com/research/global-workspace) --- J-space와 Jacobian lens(J-lens); CoT와 구별되며 보고·통제 가능하고 인과적으로 핵심인 내부 작업 공간; "a few dozen concepts," "less than a tenth of the overall activity."
- AIR (Niv Hoffman & Or Nevo), "The Story of Skills --- How We Hijacked 26,000 Agents With One Instagram Ad" (June 22, 2026): [https://www.air.security/blog-posts/the-story-of-skills](https://www.air.security/blog-posts/the-story-of-skills) --- 가짜 `brand-landingpage` 스킬, 모든 검사기를 통과한 외부 URL TOCTOU 우회; "26,000 agents were affected, including corporate accounts' agents." 이차 자료: The Hacker News (June 23): [https://thehackernews.com/2026/06/fake-ai-agent-skill-passed-security.html](https://thehackernews.com/2026/06/fake-ai-agent-skill-passed-security.html).
- Ji 외 (HKUST), "Cloak and Detonate: Scanner Evasion and Dynamic Detection of Agent Skill Malware," arXiv 2607.02357 (July 2, 2026 제출): [https://arxiv.org/abs/2607.02357](https://arxiv.org/abs/2607.02357) --- 악성 스킬 1,613개와 검사기 8개에서 SkillCloak >90% 회피; SkillDetonate 실행 중 탐지 97%, 오탐 2%. 이차 자료: The Hacker News (July 6): [https://thehackernews.com/2026/07/new-skillcloak-technique-lets-malicious.html](https://thehackernews.com/2026/07/new-skillcloak-technique-lets-malicious.html).
- Gao, Xueping (Alibaba Cloud), "Compositional Skill Routing for LLM Agents: Decompose, Retrieve, and Compose," arXiv 2606.18051 (June 16, 2026): [https://arxiv.org/abs/2606.18051](https://arxiv.org/abs/2606.18051) --- CompSkillBench(MCP 스킬 2,209개에 대한 조합 질의 300개); 반복적 스킬 인지 분해 51.0%→67.7%.
- Zhang 외(우한대 / 난창대), "Workflow-to-Skill," arXiv 2606.06893 (June 5, 2026): [https://arxiv.org/abs/2606.06893](https://arxiv.org/abs/2606.06893) --- RWSA 중간 표현; Anthropic Skill Creator를 포함한 기준선 대비 행동 재현 일관성 상대 +10.5%.
- Vercel, "The skills.sh API is now available" (June 5, 2026): [https://vercel.com/changelog/the-skills-sh-api-is-now-available](https://vercel.com/changelog/the-skills-sh-api-is-now-available) --- 질의 가능한 레지스트리 API, OIDC 토큰 인증, 팀별·프로젝트별 분당 600요청, 스킬 600,000개 이상 인덱싱, 스킬별 보안 감사.
- Steinberger, Peter (@steipete), "design loops that prompt your agents" 게시물 (June 7, 2026): [https://x.com/steipete/status/2063697162748260627](https://x.com/steipete/status/2063697162748260627) --- mid-July 2026 기준 8.4M회 이상 노출; 게시물 자체는 "loop engineering."을 쓰지 않음.
- Osmani, Addy, "Loop Engineering" (June 7, 2026): [https://addyosmani.com/blog/loop-engineering/](https://addyosmani.com/blog/loop-engineering/); O’Reilly Radar 재게재 (June 22, 2026): [https://www.oreilly.com/radar/loop-engineering/](https://www.oreilly.com/radar/loop-engineering/) --- 명명한 글; "replacing yourself as the person who prompts the agent," "one floor above the harness."
- Cherny, Boris, Lenny's Podcast / Lenny's Newsletter 인터뷰 (mid-2026): [https://www.lennysnewsletter.com/p/head-of-claude-code-what-happens](https://www.lennysnewsletter.com/p/head-of-claude-code-what-happens) --- "my job is to write loops"; 매체마다 일관되지 않게 옮겨 적힌 구술 인용.
- Anthropic (@ClaudeDevs), X Article "Getting started with loops" (July 6, 2026): [https://x.com/ClaudeDevs/status/2074208949205881033](https://x.com/ClaudeDevs/status/2074208949205881033); 정본 미러 [https://claude.com/blog/getting-started-with-loops](https://claude.com/blog/getting-started-with-loops) --- 약 6.0M회 노출 / 38K개 이상 북마크(mid-July); "loops,"를 가르치며 "loop engineering" 명칭은 블로그 미러의 설명에 있음.
- Runkle, Sydney, "The Art of Loop Engineering," LangChain 블로그 (June 16, 2026): [https://www.langchain.com/blog/the-art-of-loop-engineering](https://www.langchain.com/blog/the-art-of-loop-engineering) --- 네 중첩 단계("Loop 1: The Agent" / "Level 2/3/4"); "loopcraft"는 Swyx에게 출처를 돌림.
- 程序员鱼皮 (liyupi), 「提示词工程已死，Loop Engineering 称王！保姆级教程 + 项目实战」, codefather.cn (June 16, 2026): [https://www.codefather.cn/post/2066793761979092994](https://www.codefather.cn/post/2066793761979092994) --- 層層包含 중첩; 말/기수의 하네스 대 루프 비유; GitHub @liyupi 팔로워 23.9k.
- PureAI, "China's Moonshot AI Releases Kimi K3" (July 17, 2026): [https://pureai.com/articles/2026/07/17/china-moonshot-ai-releases-kimi-k3.aspx](https://pureai.com/articles/2026/07/17/china-moonshot-ai-releases-kimi-k3.aspx) --- 2.8T MoE, 1M 컨텍스트, 기본 시각 기능; Artificial Analysis Intelligence Index 189개 중 4위(57점); July 27 가중치 공개.
- The New Stack, "Kimi K3 tops Arena's coding leaderboard --- and it's open-weight" (July 2026): [https://thenewstack.io/kimi-k3-open-weight-coding/](https://thenewstack.io/kimi-k3-open-weight-coding/) --- 공개 가중치 모델의 순위 결과.
- Reeve, Jonas (Unite.AI), "Moonshot Opens Kimi K3 Weights Under a Revenue-Tiered License" (July 27, 2026): [https://www.unite.ai/moonshot-opens-kimi-k3-weights-under-a-revenue-tiered-license/](https://www.unite.ai/moonshot-opens-kimi-k3-weights-under-a-revenue-tiered-license/) 및 Willison, Simon, "moonshotai/Kimi-K3" (July 27, 2026): [https://simonwillison.net/2026/Jul/27/kimi-k3/](https://simonwillison.net/2026/Jul/27/kimi-k3/) --- 자체 "Kimi K3 License" 명시; 매출별 상업적 조건; Moonshot의 표현은 "open source" 아닌 "open weight".
- Tom's Hardware, "Moonshot releases 2.8 trillion parameter Kimi K3" (July 2026): [https://www.tomshardware.com/tech-industry/artificial-intelligence/moonshot-releases-2-8-trillion-parameter-kimi-k3](https://www.tomshardware.com/tech-industry/artificial-intelligence/moonshot-releases-2-8-trillion-parameter-kimi-k3) --- 규모와 서버급 하드웨어 관점.
- Bloomberg, "China's Powerful New Moonshot AI Model Closes Gap With US Rivals" (July 17, 2026): [https://www.bloomberg.com/news/articles/2026-07-17/china-s-powerful-new-moonshot-ai-model-closes-gap-with-us-rivals](https://www.bloomberg.com/news/articles/2026-07-17/china-s-powerful-new-moonshot-ai-model-closes-gap-with-us-rivals)
- Fortune, "China's Moonshot Kimi K3 and the markets" (July 17, 2026): [https://fortune.com/2026/07/17/china-moonshot-kimi-k3-markets-china-ai/](https://fortune.com/2026/07/17/china-moonshot-kimi-k3-markets-china-ai/) --- "new DeepSeek shock" 관점.
- Xinhua, "World AI Conference opens in Shanghai" (July 17, 2026): [https://english.news.cn/20260717/7691cc6c17d249089fdcd7afd840c3ba/c.html](https://english.news.cn/20260717/7691cc6c17d249089fdcd7afd840c3ba/c.html) --- WAIC 2026 / WAICO 설립; Guterres 참석.
- 중국 외교부, WAICO 설립 발표 (July 17, 2026): [https://www.mfa.gov.cn/mfa_eng/xw/zyxw/202607/t20260717_11984715.html](https://www.mfa.gov.cn/mfa_eng/xw/zyxw/202607/t20260717_11984715.html)
- Runkle, Sydney & Chase, Harrison, "3 Years of Graph Engineering with LangGraph," LangChain 블로그 (July 22, 2026): [https://www.langchain.com/blog/3-years-of-graph-engineering-with-langgraph](https://www.langchain.com/blog/3-years-of-graph-engineering-with-langgraph) --- 공식 응답; 루프는 그래프의 단순 사례; 세 해 된 기존 방식이라는 반론.
- Perez, Carlos E., "From Loop Engineering to Graph Engineering?" Intuition Machine (July 19, 2026): [https://medium.com/intuitionmachine/from-loop-engineering-to-graph-engineering-d3ebeb08511c](https://medium.com/intuitionmachine/from-loop-engineering-to-graph-engineering-d3ebeb08511c) --- 루프가 루프를 감독하는 구조; 앵커.
- Thakker, Yash, "Graph Engineering: After Loops, This Is How You Wire Multi-Agent Orgs (2026)," explainx.ai (July 18, 2026, July 26 갱신): [https://explainx.ai/blog/graph-engineering-ai-agents-multi-agent-organizations-2026](https://explainx.ai/blog/graph-engineering-ai-agents-multi-agent-organizations-2026) --- 조직 그래프와 작업 그래프 구분; Steinberger를 계기로 명시.
- TrueFoundry, "Graph Engineering for Multi-Agent Systems: Architecture, Governance, and Observability" (July 20, 2026): [https://www.truefoundry.com/blog/graph-engineering-enterprise-guide](https://www.truefoundry.com/blog/graph-engineering-enterprise-guide) --- 기업 체크리스트; 지식 그래프와 구별하는 문장.
- Eigent, "Graph Engineering for AI Agents" (July 21, 2026): [https://www.eigent.ai/blog/graph-engineering-ai-agents](https://www.eigent.ai/blog/graph-engineering-ai-agents)
- Tony Bai, 「Loop Engineering才火两个月，硅谷已经卷出"Graph Engineering"了」 (July 21, 2026): [https://tonybai.com/2026/07/21/from-loop-engineering-to-graph-engineering/](https://tonybai.com/2026/07/21/from-loop-engineering-to-graph-engineering/) --- 图工程; 유행어 경고.
- 36kr (영문판), "Father of Lobster's One Tweet: Is the Loop Era Over?" (July 21, 2026): [https://eu.36kr.com/en/p/3904771418867330](https://eu.36kr.com/en/p/3904771418867330) --- 계기 게시물 조회 2.6M 보고; Huntley, Cherny, Osmani, Catacora 인용; 원문 대신 중국어 번역으로 전함. Steinberger 게시물 자체는 위 출처를 통해 인용하며 원래 X 링크는 독립 검증되지 않음.
- MarkTechPost, "Prompt Engineering vs Loop Engineering vs Graph Engineering: What Changes at Each Layer" (July 29, 2026): [https://www.marktechpost.com/2026/07/29/prompt-engineering-vs-loop-engineering-vs-graph-engineering-what-changes-at-each-layer/](https://www.marktechpost.com/2026/07/29/prompt-engineering-vs-loop-engineering-vs-graph-engineering-what-changes-at-each-layer/) --- 쌓인 제어 단위 관점.
- BleepingComputer, "Claude Fable 5 isn't permanently leaving subscriptions, Anthropic says" (July 2026): [https://www.bleepingcomputer.com/news/artificial-intelligence/claude-fable-5-isnt-permanently-leaving-subscriptions-anthropic-says/](https://www.bleepingcomputer.com/news/artificial-intelligence/claude-fable-5-isnt-permanently-leaving-subscriptions-anthropic-says/) --- 구독 제외가 영구적이지 않다는 July 2 해명; July 18 결정 전이므로 그 세부는 포함하지 않음.
- Anthropic Help Center, "Claude Fable 5 on your plan": [https://support.claude.com/en/articles/15424964-claude-fable-5-on-your-plan](https://support.claude.com/en/articles/15424964-claude-fable-5-on-your-plan) --- "Starting July 20, 2026": Fable 5가 Max 요금제와 Team / Enterprise 프리미엄 좌석의 기본으로 주간 한도 50%까지 추가 비용 없이 사용 가능; Pro와 표준 좌석은 종량제 크레딧 사용.
- Bastian, Matthias (The Decoder), "Anthropic slashes Claude Fable 5 limits in Max and Team Premium and pushes Pro users toward API pricing" (July 18, 2026): [https://the-decoder.com/anthropic-slashes-claude-fable-5-limits-in-max-and-team-premium-and-pushes-pro-users-toward-api-pricing/](https://the-decoder.com/anthropic-slashes-claude-fable-5-limits-in-max-and-team-premium-and-pushes-pro-users-toward-api-pricing/) --- July 18 발표: July 20부터 한도 50%로 포함; Pro / Team Standard는 일회성 $100 사용 크레딧 뒤 API 요금 적용.
- Forbes (Sandy Carter), "Claude Fable 5 Extends to July 19: 7 Days, 7 Power Moves" (July 13, 2026): [https://www.forbes.com/sites/sandycarter/2026/07/13/claude-fable-5-extends-to-july-19-7-days-7-power-moves/](https://www.forbes.com/sites/sandycarter/2026/07/13/claude-fable-5-extends-to-july-19-7-days-7-power-moves/) --- 결정 이전의 연장 과정.
- Anthropic, "Introducing Claude Opus 5" (July 24, 2026): [https://www.anthropic.com/news/claude-opus-5](https://www.anthropic.com/news/claude-opus-5) --- 가격, Fast 모드, 캐시를 유지한 대화 중 도구 변경; Frontier-Bench / CursorBench는 자체 주장. 플랫폼 문서, "What's new in Claude Opus 5": [https://platform.claude.com/docs/en/about-claude/models/whats-new-opus-5](https://platform.claude.com/docs/en/about-claude/models/whats-new-opus-5) --- 기본·최대 1M 컨텍스트, 최대 128K 출력, 기본 사고 활성화, 전체 다섯 노력 수준(`low` / `medium` / `high` / `xhigh` / `max`); 발표 페이지에는 모두 없음.
- TechCrunch, "Anthropic launches Opus 5" (July 24, 2026): [https://techcrunch.com/2026/07/24/anthropic-launches-opus-5/](https://techcrunch.com/2026/07/24/anthropic-launches-opus-5/)
- Axios, "Anthropic releases new model Opus 5" (July 24, 2026): [https://www.axios.com/2026/07/24/anthropic-releases-new-model-opus-5](https://www.axios.com/2026/07/24/anthropic-releases-new-model-opus-5)
- Model Context Protocol 블로그, "The 2026-07-28 specification" (July 28, 2026): [https://blog.modelcontextprotocol.io/posts/2026-07-28/](https://blog.modelcontextprotocol.io/posts/2026-07-28/) --- 최종 명세: 무상태 핵심, MRTR(SEP-2322), 동적 클라이언트 등록을 대체하는 CIMD, RFC 9207 발급자 검증, 확장 프레임워크, 12개월 폐기 유예.
- TechCrunch, "AI's most important protocol is getting a little bit easier to use" (July 20, 2026): [https://techcrunch.com/2026/07/20/ais-most-important-protocol-is-getting-a-little-bit-easier-to-use/](https://techcrunch.com/2026/07/20/ais-most-important-protocol-is-getting-a-little-bit-easier-to-use/)
- The Register, "Model Context Protocol prepares to break with its stateful past" (July 23, 2026): [https://www.theregister.com/devops/2026/07/23/model-context-protocol-prepares-to-break-with-its-stateful-past/5276722](https://www.theregister.com/devops/2026/07/23/model-context-protocol-prepares-to-break-with-its-stateful-past/5276722)
- WorkOS, "MCP 2026 spec: agent authentication" (July 2026): [https://workos.com/blog/mcp-2026-spec-agent-authentication](https://workos.com/blog/mcp-2026-spec-agent-authentication) --- CIMD와 인가 변경에 대한 이차 보도.
- MemTensor, Renmin University, NUS, SJTU, Tongji, "Metis: Memory Foundation Model," arXiv 2607.26760 (July 29, 2026 제출): [https://arxiv.org/abs/2607.26760](https://arxiv.org/abs/2607.26760) --- 트랜스포머 기반 모델 내부의 매개변수형 지속 메모리; Qwen3.5 기반의 4B/9B/27B 시제품; Fast Weight Programming에서 영감을 받은 hyper memory block + local memory block; 자체 보고 한계(고정 크기 압축의 정보 손실, 잠재 공간 의미 혼합).
- LangChain, "Deep Agents v0.7" (July 29, 2026): [https://www.langchain.com/blog/deep-agents-v0-7](https://www.langchain.com/blog/deep-agents-v0-7) --- 기본 시스템 프롬프트 제거, 내장 도구 설명 43% 감소, `TodoListMiddleware` / `write_todos` 선택 기능화; 기본 턴 입력 약 6K → 약 2K(65%); 세 모델 계열의 할 일 목록 제거 평가.
- MinIO, "Introducing AIStor Memory: Long-Term Memory for AI Agents" (July 29, 2026): [https://www.min.io/blog/introducing-aistor-memory-long-term-memory-for-ai-agents](https://www.min.io/blog/introducing-aistor-memory-long-term-memory-for-ai-agents) --- 객체 저장소 기반 메모리, 작업 공간, 자격 증명 계층; July 29-30, 2026 SiliconANGLE, The Register, HPCwire/BigDATAwire 보도로 뒷받침.
- "Practical Online KV Cache Compaction for LLM Agents," arXiv 2608.00902 (August 2, 2026 제출): [https://arxiv.org/abs/2608.00902](https://arxiv.org/abs/2608.00902) --- 즉시 압축하면 정확도 손실; 에이전트의 이후 질의가 대리 신호로 쓰일 때까지 지연하면 대부분 회복; 불완전한 대리 신호에서 토큰 제거가 어텐션 매칭 재구성보다 견고; BrowseComp-Plus와 WideSearch에서 KV 캐시 80% 감소와 처리량 향상.
- TencentCloud, "TencentDB-Agent-Memory" (GitHub): [https://github.com/TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) --- MIT 라이선스, 자체 호스팅; 저장소 생성 April 7, 2026; GitHub API 별 약 24K, August 24, 2026 확인. 이차 자료: MarkTechPost (August 7, 2026): [https://www.marktechpost.com/2026/08/07/tencent-cloud-open-sources-tencentdb-agent-memory-v2-0/](https://www.marktechpost.com/2026/08/07/tencent-cloud-open-sources-tencentdb-agent-memory-v2-0/) --- v2.0 보도; PRNewswire(August 13, 2026)는 별도 팀 협업 발표. v2.0.0 공개는 August 3, 2026(GitHub releases API `published_at` 2026-08-03; MarkTechPost도 같은 날짜). 모든 Team Memory 통제 메커니즘은 Tencent 자체 주장이며 독립 평가 없음.
- Zenity Labs, "Attackers Target Agents via the Skill Supply Chain" (August 6, 2026): [https://labs.zenity.io/post/attackers-target-agents-via-the-skill-supply-chain](https://labs.zenity.io/post/attackers-target-agents-via-the-skill-supply-chain) --- `paperclipai`와 `browser-use` GitHub 조직 사칭; July 5 무해한 스킬을 July 11 무기화해 인기 #8; 네 트리거로 자격 증명 경로 138개; 표시 설치 >1.7M(고유 에이전트 아닌 합산값); 12시간 안에 Vercel / GitHub 삭제. 이차 자료: CSO Online: [https://www.csoonline.com/article/4206851/](https://www.csoonline.com/article/4206851/); Business Wire (August 6, 2026): [https://www.businesswire.com/news/home/20260806707467/en/](https://www.businesswire.com/news/home/20260806707467/en/). 별도 Paperclip *제품* CVE(CVE-2026-41679 등, August 5, 2026)는 다른 공개이며 여기서는 다루지 않는다.
- AWS Machine Learning Blog, "Control agent behaviors and cost beyond a single action: new capabilities in Amazon Bedrock AgentCore" (August 6, 2026): [https://aws.amazon.com/blogs/machine-learning/control-agent-behaviors-and-cost-beyond-a-single-action-new-capabilities-in-amazon-bedrock-agentcore/](https://aws.amazon.com/blogs/machine-learning/control-agent-behaviors-and-cost-beyond-a-single-action-new-capabilities-in-amazon-bedrock-agentcore/); AWS What's New, "Temporal Policies for AgentCore" (August 6, 2026): [https://aws.amazon.com/about-aws/whats-new/2026/08/temporal-policies-agentcore/](https://aws.amazon.com/about-aws/whats-new/2026/08/temporal-policies-agentcore/); AWS What's New, "AWS Bedrock AgentCore Runtime Instances generally available" (August 6, 2026): [https://aws.amazon.com/about-aws/whats-new/2026/08/aws-bedrock-agentcore-runtime-instances-generally-available/](https://aws.amazon.com/about-aws/whats-new/2026/08/aws-bedrock-agentcore-runtime-instances-generally-available/) --- Apache-2.0 Dogwood 정책 언어의 세션 이력 인지 기본 거부 인가; 게이트웨이 Rate Limiting; 고객 선택 EC2 유형, 아홉 리전, 서버리스 기본 8시간 대비 최대 14일 세션.
- Anthropic, "Cross-session messaging" (August 2026): [https://code.claude.com/docs/en/cross-session-messaging](https://code.claude.com/docs/en/cross-session-messaging) 및 Claude Code 변경 이력: [https://code.claude.com/docs/en/changelog](https://code.claude.com/docs/en/changelog) --- `ListAgents` / `SendMessage`, v2.1.224(August 7, 2026)부터 v2.1.241(August 23)까지; 세션별 수신 수락 / 보류 / 거절과 크기·연속 전송·루프 제한; 이력, 파일, 권한 승인은 세션을 넘지 않음; Bedrock, Claude Platform on AWS, Google Cloud Agent Platform, Microsoft Foundry 미지원. 두 매체 어디에도 "graph engineering."은 없음.
- Meta, "Introducing Muse Glimmer: an open agentic model" (August 10, 2026): [https://research.meta.ai/blog/introducing-muse-glimmer-open-agentic-model](https://research.meta.ai/blog/introducing-muse-glimmer-open-agentic-model) --- 30B 밀집, Apache 2.0, Muse Spark 증류; 4비트에서 20GB 미만; day-0 다중 실행 환경 지원. DFlash 속도 향상(3.1x / 1.8x / 1.5x), Gemma4-31B / Qwen3.6-27B 비교는 Meta 자체 수치. 이차 자료: Phoronix, CNBC(August 10, 2026), gHacks(August 11, 2026).
- DeepSeek, "DeepSeek Harness" (August 13, 2026): [https://github.com/deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) 및 [https://deepseek.com/harness/en/](https://deepseek.com/harness/en/) --- MIT 라이선스; "Cordis" 플러그인 패러다임과 "A Programming Paradigm for Spatiotemporal Composability" 백서; 추가 전용 세션 로그; GitHub API로 August 24, 2026 확인한 별 190,630개 / 포크 21,319개, September 15, 2026 확인한 별 224,004개 / 포크 26,637개. Claude-Code / Codex 하위 에이전트는 직접 제공 기능이다. 저장소의 `@deepseek-ai/dsh-subagent-claude-code`와 `@deepseek-ai/dsh-subagent-codex` 패키지(August 4, 2026 설계 노트)가 공식 Claude Agent SDK와 Codex `app-server`를 호출한다. 이차 보도(CryptoBriefing, MindStudio, Digital Applied, Flowtivity)는 이 코드를 근거로 한다.
- Anthropic, 출시 노트 개요: [https://platform.claude.com/docs/en/release-notes/overview](https://platform.claude.com/docs/en/release-notes/overview) --- Skills API 베타 종료 August 19, 2026; Managed Agents GitHub 호스팅 스킬 August 7, 2026. Anthropic 블로그, "Computer use, Skills API, and Files API" (날짜 August 20, 2026): [https://claude.com/blog/computer-use-skills-api-files-api](https://claude.com/blog/computer-use-skills-api-files-api) --- 출시 노트보다 하루 늦은 관련 글. Managed Agents 스킬 문서: [https://platform.claude.com/docs/en/managed-agents/skills](https://platform.claude.com/docs/en/managed-agents/skills) --- 마운트한 저장소 루트 `.claude/skills`의 자동 발견과 신뢰 경계 주의.
- OpenAI, "Codex as a Platform" (August 19, 2026): [https://developers.openai.com/blog/codex-as-a-platform](https://developers.openai.com/blog/codex-as-a-platform) --- Apache 2.0의 `codex exec`, Codex SDK, app-server; 출력 토큰 6x 감소와 ARC-AGI-3 13.3%에서 38.3%, Cisco / GitHub / JetBrains / Thrive-Crete 실서비스 사용자는 자체 주장이다. 일차 페이지는 작성자 바로 위에 "Aug 19, 2026" 날짜가 있고 일부 이차 보도(OpenSourceForU, finance.biggo.com)는 August 20으로 적는다. `openai/codex`는 April 2025부터 공개 Apache-2.0(GitHub API)이므로 최초 공개가 아닌 하네스 계층의 재정의다.
- Model Context Protocol 블로그, "The MCP Roadmap" (August 22, 2026): [https://blog.modelcontextprotocol.io/posts/mcp-roadmap/](https://blog.modelcontextprotocol.io/posts/mcp-roadmap/) --- Contributor Ladder, 작업 그룹 SEP 분류, 공식 기능 수명 주기와 폐기 정책; 다섯 우선순위(에이전트 메시징과 Tasks 핵심 편입, 로컬 배포 HTTP 네이티브 전송, DPoP·Workload Identity Federation 에이전트 ID, 도구 결과 처리와 점진적 탐색, SDK 개발자 경험과 적합성). 당일 Hacker News 241점 / 댓글 142개(스냅샷).
- OpenRouter 주간 순위, 중국 모델 상위 다섯 독점(July 29, 2026 보도): Dataconomy, "Chinese LLMs Take Top Five Spots On OpenRouter": [https://dataconomy.com/2026/07/29/chinese-ai-models-openrouter-top-five/](https://dataconomy.com/2026/07/29/chinese-ai-models-openrouter-top-five/); TechBriefly, "Chinese AI models lead OpenRouter for first time": [https://techbriefly.com/2026/07/29/chinese-ai-models-lead-openrouter-for-first-time/](https://techbriefly.com/2026/07/29/chinese-ai-models-lead-openrouter-for-first-time/) --- 중국 모델 상위 다섯 독점과 주당 >20T 토큰 수치. September 지속: [https://finance.yahoo.com/technology/ai/articles/chinese-ai-models-now-capture-020440715.html](https://finance.yahoo.com/technology/ai/articles/chinese-ai-models-now-capture-020440715.html) 는 46.4% / 35.7%를 전한다. KuCoin 속보 [https://www.kucoin.com/news/flash/chinese-models-dominate-openrouter-weekly-token-usage-ranking](https://www.kucoin.com/news/flash/chinese-models-dominate-openrouter-weekly-token-usage-ranking) 는 August 5, 2026 중국 모델이 상위 열 자리 중 여덟을 차지한 다른 이전 스냅샷으로 September 수치의 출처가 아니다. OpenRouter 자체 순위는 날짜별 과거 기록 없는 실시간 이동 화면이다: [https://openrouter.ai/rankings](https://openrouter.ai/rankings). 두 점유율은 이차 자료이며 방법론이 달라 서로 비교할 수 없다.
- "Filesystem-Based Memory for LLM Agents: Organization, Evolution, and Sustainability," arXiv 2607.26637 (July 29, 2026 제출): [https://arxiv.org/abs/2607.26637](https://arxiv.org/abs/2607.26637) --- 공유 메모리 파일 시스템의 세 역할 형식화; 규모가 커지면 정리된 저장소가 검색 비용을 약 절반으로 줄이지만 가장 강력한 관리 에이전트 외에는 정리 상태가 악화되고 어떤 측정 에이전트도 더 좋은 답으로 바꾸지 못함. "MemTxn: A Transaction Boundary for Source-Supported Updates and Complete-State Recovery in Agent Memory," arXiv 2607.27834 (July 30, 2026 제출): [https://arxiv.org/abs/2607.27834](https://arxiv.org/abs/2607.27834) --- Ordered PatchTest, Temporal Resolver, 지속 저장 스냅샷 저널; 자체 검증 집합 60개 수락 / 179개 거절. "MemTX: Transactional Belief Commit for Stateful Agent Memory," arXiv 2607.23929 (July 27, 2026 제출): [https://arxiv.org/abs/2607.23929](https://arxiv.org/abs/2607.23929) --- 겹치는 저자 없는 독립 제안. "Memory Decoder at Scale: A Pretrained, Parametric Long-Term Memory," arXiv 2607.27919 (July 30, 2026 제출): [https://arxiv.org/abs/2607.27919](https://arxiv.org/abs/2607.27919) --- 6.9B 메모리 모듈과 410M Pythia 기반 모델이 총매개변수 39% 적게 쓰며 Pythia-12B 37.24 대비 37.34점. 모든 수치는 논문 자체 결과이며 재현되지 않음.
- Google Cloud 블로그, "What's new in Gemini Enterprise Agent Platform" (July 30, 2026): [https://cloud.google.com/blog/products/ai-machine-learning/whats-new-in-gemini-enterprise-agent-platform](https://cloud.google.com/blog/products/ai-machine-learning/whats-new-in-gemini-enterprise-agent-platform) --- Agent Memory Bank, Agent Runtime(최대 칠 일), Agent Identity, Agent Gateway, Agent Registry의 다섯 기능 동시 정식 출시; 모든 역량 표현은 Google 자체 설명. 제품 문서: [https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/memory-bank](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/memory-bank). 이차 자료: [https://enterprisedna.co/resources/news/google-gemini-agent-platform-memory-runtime-identity-ga-2026/](https://enterprisedna.co/resources/news/google-gemini-agent-platform-memory-runtime-identity-ga-2026/). 이전 플랫폼 브랜드의 July 2025 Vertex AI Memory Bank 공개 미리보기와 구별됨.
- "Can Agent Memory Systems Track Evolving State?" (StateMemBench / StateMem), arXiv 2608.19652 (August 20, 2026): [https://arxiv.org/abs/2608.19652](https://arxiv.org/abs/2608.19652) --- 최신 상태 대체의 폐쇄 후보군 채점 다중 세션 시나리오 234개; StateMem은 가장 강력한 동일 기반 기준선 대비 DeepSeek-V4-Flash 현재 상태 정확도 1.8x(0.205에서 0.363), 가장 강력한 메모리 시스템 대비 Qwen-3.5-9B 1.6x(0.149에서 0.233)를 보고한다. 여섯 백엔드 래퍼로 +32에서 +67점, 추가 컨텍스트를 통제하면 +15에서 +32점이다. 확인한 유일한 출처는 논문이며 자체 수치로 재현되지 않았다.
- CrowdStrike, "CrowdStrike Unveils Falcon Guardian" (September 1, 2026): [https://www.crowdstrike.com/en-us/press-releases/crowdstrike-unveils-falcon-guardian-ai-agent-security/](https://www.crowdstrike.com/en-us/press-releases/crowdstrike-unveils-falcon-guardian-ai-agent-security/) --- Windows·macOS 엔드포인트 에이전트 발견과 목록, 실행 중 탐지와 집행; 설치 기반이나 탐지율 수치 없음. 이차 자료: SiliconANGLE (September 1, 2026): [https://siliconangle.com/2026/09/01/crowdstrike-launches-falcon-guardian-to-police-ai-agents-at-the-endpoint/](https://siliconangle.com/2026/09/01/crowdstrike-launches-falcon-guardian-to-police-ai-agents-at-the-endpoint/). AIR: TechCrunch (September 1, 2026): [https://techcrunch.com/2026/09/01/air-raises-50m-to-help-companies-vet-the-skills-and-add-ons-ai-agents-use/](https://techcrunch.com/2026/09/01/air-raises-50m-to-help-companies-vet-the-skills-and-add-ons-ai-agents-use/) 및 SecurityWeek (September 3, 2026): [https://www.securityweek.com/ai-agent-firewall-startup-air-security-emerges-from-stealth-with-50-million/](https://www.securityweek.com/ai-agent-firewall-startup-air-security-emerges-from-stealth-with-50-million/) --- 두 라운드 $50M; 부가 기능 17,800개 이상 / 설치 6.7M과 Anthropic·OpenAI 사칭 스킬은 방법론이 공개되지 않은 AIR 자체 연구.
- OpenAI, "GPT-6 Astra: A new generation of intelligence": [https://openai.com/index/gpt-6-astra/](https://openai.com/index/gpt-6-astra/) --- Critical 기준 진술, ExploitBench 100% 대 78.5%, ExploitGym 42.4% 대 30.3%, SRE-Bench 첫 시도 88.0%·네 번 내 99.2%, 단계적 제공 문장, 개념 증명 거절과 Daybreak 확대 경로, 기록된 추론을 감시하기 어려워졌다는 발견. OpenAI, "Safety overview: GPT-6 Astra" (페이지 날짜 September 3, 2026): [https://openai.com/index/safety-overview-gpt-6-astra/](https://openai.com/index/safety-overview-gpt-6-astra/) --- "our first model to reach the Critical level of cybersecurity capability under our Preparedness Framework"와 고의적 성능 저하·방해 과제 회피를 포함한 모니터링 가능성 감소. OpenAI, "The path to Astra" (페이지 날짜 September 1, 2026): [https://openai.com/index/path-to-astra/](https://openai.com/index/path-to-astra/) --- 출시 전 지정, 심각도 높은 V8 취약점 스무 개로 구성한 내부 ExploitBench 이식, 공격 사슬의 제로데이 두 개. 모든 벤치마크는 OpenAI 자체 수치. 이차 자료: CSO Online (September 4, 2026): [https://www.csoonline.com/article/4218679/openai-launches-gpt-6-astra-its-first-model-to-cross-a-critical-cybersecurity-threshold.html](https://www.csoonline.com/article/4218679/openai-launches-gpt-6-astra-its-first-model-to-cross-a-critical-cybersecurity-threshold.html); CNBC (September 3, 2026): [https://www.cnbc.com/2026/09/03/open-ai-astra-gpt-6-cyber.html](https://www.cnbc.com/2026/09/03/open-ai-astra-gpt-6-cyber.html) --- 출시 이차 보도. 세 OpenAI 페이지 어디에도 컨텍스트 창과 최대 출력 수치는 없어 인용하지 않는다. 출시 시 기업 접근 기본 비활성화는 출시 페이지의 문구를 본문에 인용했다. API 가격(입력 / 출력 백만 토큰당 $10 / $50)도 같은 페이지에 있지만 여기서는 핵심 근거가 아니다.
- Goyal, Ankit와 Ray, Jaideep, "Does Your Agent's Memory Survive a Model Upgrade? A Controlled Study of Memory Portability," arXiv 2609.05339 (September 4, 2026): [https://arxiv.org/abs/2609.05339](https://arxiv.org/abs/2609.05339) --- 원시 이력, RAG, 압축 노트, 지식 그래프의 합성 사례 48개; 그래프 메모리 거의 불변(0.0004 +/- 0.0020), 압축 노트 +9.91 / -13.28점 변동, 부분 재임베딩 4.96점 대 11.90점 회복, 저하 약 80%는 구축 시 정보 손실로 귀속. 두 이전 방향 중 하나에서 원시 이력을 보존할 때만 48개 중 34개 복구 성공. 저자 두 명, 합성 문서 집합, 재현되지 않음.
- Anthropic, "Detecting and countering misuse of AI: September 2026" (September 10, 2026): [https://www.anthropic.com/threat-intelligence-report-september-2026](https://www.anthropic.com/threat-intelligence-report-september-2026) --- 일차 보고서로 December 2025부터 August 2026까지 불법 증류 등 일곱 피해 영역에서 저지했다는 악용을 다룬다. 구체적 주장·수치(표시 계정 5,380개, 약 열흘간 요청 약 300,000개, May-July 2026 Moonshot AI 교환 23M회 이상·Alibaba 151백만 회 초과, DeepSeek, Z.ai, Xiaomi, MiniMax, SenseTime 명명)는 증류 절에서 직접 읽었다. 이차 보도: CNBC (September 11, 2026): [https://www.cnbc.com/2026/09/11/chinese-ai-labs-moonshot-deepseek-alibaba-anthropic.html](https://www.cnbc.com/2026/09/11/chinese-ai-labs-moonshot-deepseek-alibaba-anthropic.html); Dealroom: [https://dealroom.co/news/150366-anthropic-alleges-moonshot-routed-some-kimi-user-requests-to-claude-then/](https://dealroom.co/news/150366-anthropic-alleges-moonshot-routed-some-kimi-user-requests-to-claude-then/). 모든 주장은 경쟁자에 대한 Anthropic의 의혹 제기이며 독립적으로 판단되지 않았다.
- Salesforce, "Agentforce job-ready AI agents" (September 11, 2026): [https://www.salesforce.com/uk/news/stories/agentforce-job-ready-ai-agents/](https://www.salesforce.com/uk/news/stories/agentforce-job-ready-ai-agents/) --- 장기 실행 환경(메모리, 지속 실행, 동적 조향), November 2026 정식 출시 예정인 Hunter 시범, Multi-Agent Orchestration 정식 출시. 이차 자료: unite.ai: [https://www.unite.ai/salesforce-debuts-job-ready-agentforce-agents-and-long-horizon-runtime/](https://www.unite.ai/salesforce-debuts-job-ready-agentforce-agents-and-long-horizon-runtime/). 여러 주 목표 추구는 독립 벤치마크 없는 자체 주장이며 시연용 에이전트도 아직 정식 출시되지 않았다.
- 14장 생존 판정, September 15, 2026 점검. 해당 장 출처에 모두 실은 일차 증거: Anthropic, "How we built our multi-agent research system" (June 13, 2025): [https://www.anthropic.com/engineering/multi-agent-research-system](https://www.anthropic.com/engineering/multi-agent-research-system); OpenAI Codex PR [#28792](https://github.com/openai/codex/pull/28792) (June 19, 2026 병합) 및 [#29324](https://github.com/openai/codex/pull/29324) (June 22, 2026 병합), 첫 출시 [rust-v0.142.0](https://github.com/openai/codex/releases/tag/rust-v0.142.0) (June 22, 2026); Graph Engineering Mastery: [https://graphengineerings.com/](https://graphengineerings.com/) 및 [https://graphengineerings.com/course/module-2.html](https://graphengineerings.com/course/module-2.html); SmartScope (September 1, 2026): [https://smartscope.blog/en/blog/graph-engineering-loop-engineering-logic-review/](https://smartscope.blog/en/blog/graph-engineering-loop-engineering-logic-review/); Nhu Hoang, Towards Data Science (September 14, 2026): [https://towardsdatascience.com/graph-engineering-for-ai-agents-from-prompts-and-loops-to-workflows/](https://towardsdatascience.com/graph-engineering-for-ai-agents-from-prompts-and-loops-to-workflows/); AgentEng London 2026: [https://agentengineering.world/london/](https://agentengineering.world/london/); `headcount` (저장소 생성 August 28, 2026): [https://github.com/cbrock84/headcount](https://github.com/cbrock84/headcount). 합산 규칙은 July 원문에 명시되지 않아 암시하는 대신 14장 14.7절에서 명시한다.

---

*이전: [10장 - 실제 지식 하네스 구축](10-case-study.md)*
