# 9장: 중국 AI 지식 엔지니어링 풍경

> **한 문장으로:** 중국은 자체 오픈소스 플랫폼, 모델, 커뮤니티를 가진 평행 AI 생태계를 만들었다 ——종종 서양과 다른 방향으로 혁신한다.
>
> **왜 중요한가:** 세계 AI 연구자의 절반이 중국에 있다. 이 생태계를 무시하는 것은 혁신의 절반을 놓치는 것을 의미한다.

![Chinese vs Western AI Knowledge Engineering](../../../diagrams/china-comparison.png)

LLM 지식 엔지니어링에 관한 글로벌 대화는 중국 생태계를 살펴보지 않고는 불완전하다. 2025년 12월까지 규제 당국에 신고된 748개의 AI 서비스와 함께, 중국은 대규모 언어 모델로 지식 시스템을 만드는 평행 ——그리고 어떤 영역에서는 분기하는 —— 접근을 발전시켰다. 본 장은 중국 개발자와 기업들이 지식 엔지니어링에 어떻게 접근하는지를 형성하는 핵심 플랫폼, 모델, 문화적 차이를 매핑한다.

## A. 오픈소스 RAG와 에이전트 플랫폼

중국의 오픈소스 AI 생태계는 GitHub 인기에서 서양 대응물에 필적하거나 능가하는 여러 플랫폼을 산출했다. 이 프로젝트들을 구분 짓는 것은 시각 워크플로우, 엔터프라이즈 배포 준비성, 깊은 문서 이해에 대한 강조이다 ——중국 엔터프라이즈 고객의 실용적 수요를 반영한다.

### Dify (136K+ GitHub 스타)

[Dify](https://github.com/langgenius/dify)는 글로벌하게 가장 많이 별 받은 에이전트형 AI 플랫폼이다. Apache 2.0 라이선스로, RAG 파이프라인, 에이전트 워크플로우, 다단계 추론 사슬을 만들기 위한 시각 캔버스를 제공한다. 버전 1.0 이래 Dify는 Model Context Protocol (MCP)를 지원하여 외부 도구 서버와의 매끄러운 통합을 허용한다. 그것의 강점은 워크플로우를 시각적으로 설계하는 노코드 사용자와 프로그램적 통제가 필요한 개발자 사이의 격차를 메우는 데 있다. 엔터프라이즈 사용자는 전체 스택을 셀프 호스팅할 수 있는데, 이는 데이터 주권 요구사항이 종종 클라우드 전용 해법을 막는 중국 시장에서 중요하다.

### RAGFlow (62-75K+ GitHub 스타)

[RAGFlow](https://github.com/infiniflow/ragflow)는 깊은 문서 이해를 통해 자신을 차별화한다. 문서를 평면 텍스트로 다루는 대신, RAGFlow는 스캔된 PDF, 스프레드시트, 슬라이드 덱을 포함하여 20개 이상의 파일 형식에 걸쳐 레이아웃 인식 파싱, OCR, 테이블 추출을 적용한다. 그것의 "agentic RAG" 접근은 시스템이 쿼리 유형에 따라 어떤 검색 전략을 적용할지 자율적으로 결정할 수 있음을 의미한다. 레거시 문서 아카이브 ——중국 국유 기업과 제조 회사에서 흔한 시나리오 —— 를 다루는 기업에게, 이 능력은 "있으면 좋은" 것이 아니라 요구사항이다.

### FastGPT (27K+ GitHub 스타)

[FastGPT](https://github.com/labring/FastGPT)는 자원 효율성에 초점을 두고 엔터프라이즈 지식 베이스 Q&A를 겨냥한다. 그것의 QA 쌍 추출 파이프라인은 자동으로 문서를 질문-답 쌍으로 변환하며, 그 다음 검색과 fine-tuning 모두에 사용될 수 있다. 플랫폼은 RAM 2GB 정도로 적은 머신에서 실행되도록 설계되어, 전용 GPU 인프라를 감당할 수 없는 중소 기업에 접근 가능하게 한다. 이 검약은 중국 생태계의 더 넓은 패턴을 반영한다: 제약 아래에서의 최적화.

### MaxKB (18K+ GitHub 스타)

[MaxKB](https://github.com/1Panel-dev/MaxKB)는 원클릭 배포를 가진 엔터프라이즈 에이전트 플랫폼으로 자신을 자리매김한다. 도구 통합을 위한 MCP를 지원하고 흔한 엔터프라이즈 시나리오 ——고객 서비스, 내부 지식 검색, 문서 요약 —— 를 위한 사전 만들어진 템플릿을 제공한다. 그것의 매력은 "AI 어시스턴트를 원한다"에서 "그것이 실행되고 있다"까지의 시간을 몇 주에서 몇 시간으로 줄이는 데 있다.

### Coze Studio (15K+ GitHub 스타, ByteDance)

[Coze Studio](https://github.com/coze-dev/coze-studio)는 ByteDance의 오픈소스 시각 에이전트 개발 플랫폼이다. 원래 폐쇄 제품이었던 ByteDance가 2025년 7월에 오픈소스화했고, 3일 안에 10,000개의 GitHub 스타를 누적했다 ——억눌린 수요와 ByteDance의 배포 력 모두에 대한 증거. Coze Studio는 내장 메모리, 도구 사용, 다중 턴 대화 관리와 함께 에이전트를 만드는 드래그 앤 드롭 인터페이스를 제공한다. ByteDance의 Doubao 모델 패밀리와의 통합은 중국어 작업에서 그것에 네이티브 이점을 준다.

### DB-GPT (17K+ GitHub 스타)

[DB-GPT](https://github.com/eosphoros-ai/DB-GPT)는 AI 네이티브 데이터 상호작용을 전문으로 한다. 그것의 핵심 능력은 자연어 SQL 변환이며, 비기술 사용자가 데이터베이스를 대화적으로 쿼리할 수 있게 한다. 그것은 시각화 생성과 다중 에이전트 데이터 분석 파이프라인으로 이를 확장한다. 큰 구조화된 데이터셋 위에 앉아 있는 기업 ——금융, 물류, 제조의 대부분의 중국 회사를 기술 —— 에게 DB-GPT는 AI 강화 분석에 접근 가능한 진입점을 제공한다.

## B. 지식 관리를 위한 중국 LLM

중국의 기반 모델 풍경은 빠르게 성숙했으며, 여러 모델이 이제 특정 벤치마크에서 서양 대응물과 경쟁적이거나 우월하다.

### Qwen3 (Alibaba Cloud)

Qwen3는 Alibaba의 플래그십 모델 패밀리이다. 가장 큰 변종은 Apache 2.0으로 공개된 2,350억 파라미터 Mixture of Experts (MoE) 모델이다. 코딩 전문 변종 Qwen3-Coder-480B는 256K부터 1M 토큰까지의 context window를 지원한다. Apache 2.0 라이선스는 전략적으로 의미 있다: 그것은 무제한 상업적 사용을 가능케 하며, 이는 독점 API 비용을 감당할 수 없는 중국 스타트업 전반에 채택을 추진했다. Qwen의 다국어 능력은 중국어, 일본어, 한국어 ——서양 모델이 역사적으로 부진한 언어 —— 에서 특히 강하다.

### DeepSeek R1

DeepSeek R1은 MIT 라이선스로 공개되면서 수학과 과학 추론 벤치마크에서 OpenAI의 o1과 일치했다. 모델은 보고된 바로는 600만 달러 미만으로 훈련되었으며, 이는 비교 가능한 서양 모델의 일부이다. 이 비용 효율성은 산업 전반에 충격파를 보냈다: 중국에서 오픈소스 모델의 엔터프라이즈 채택은 그것의 출시 후 몇 달 안에 23%에서 67%로 뛰었다. DeepSeek R1은 프런티어 레벨 추론이 프런티어 레벨 예산을 요구하지 않음을 입증하여, 지식 엔지니어링의 경제학을 근본적으로 옮겼다.

2026년 4월에, DeepSeek은 자사의 아키텍처 기여를 **manifold-constrained hyper-connections (mHC)**, Transformer++ 스타일 모델에서 사용되는 잔차 연결의 일반화로 확장했다. 표준 잔차 스트림이 계층 전반에 정보의 단일 채널을 앞으로 운반하는 곳에서, mHC는 학습된 저차원 매니폴드에 놓이도록 각각 제약된 **여러 내부 스트림**을 운반한다. 구성은 단순 다중 스트림 잔차가 스케일에서 겪는 차원 붕괴 없이 후기 계층이 초기 표현에 더 풍부한 접근을 갖도록 설계되었다. DeepSeek의 블로그는 비슷한 파라미터 수에서 장기간 추론 벤치마크에서의 이득을 보고하며, 정보가 많은 중간 계층에 걸쳐 운반되어야 하는 작업에서 가장 큰 개선을 보고한다. 2026년 4월 기준 결과는 **독립 복제 대기 중으로 표시되어야 한다** ——그것은 단일 연구실 모델에 대한 단일 연구실 공개이며, 이 분야는 제3자 재현에서 살아남지 못한 아키텍처 주장으로 데인 적이 있다. 결과가 유지된다면, mHC는 MoE, MLA, DeepSeek의 이전 다중 토큰 예측 작업과 함께, 주류 사용으로 넘어오기 전에 중국 오픈웨이트 생태계에서 발원한 세 번째 또는 네 번째 아키텍처 primitive로 합류한다.

### DeepSeek V4 (2026년 4월)

DeepSeek의 **V4 프리뷰** (2026년 4월 24일)는 R1 서사를 동시에 세 축으로 확장한다: 경제학, 능력, 그리고 **추론 기반**. 릴리스는 MIT 라이선스로 Hugging Face에 두 개의 오픈웨이트 Mixture-of-Experts 모델 ——**V4-Pro 1.6조 파라미터 / 49B 활성**, **V4-Flash 284B / 13B 활성** —— 을 등급이 아니라 기본으로 1M 토큰 context window와 함께 출하한다. API 가격은 2026년의 어떤 프런티어급 모델보다 가장 공격적이다: **출력 백만 토큰당 V4-Flash $0.28**, V4-Pro $3.48, 하드웨어 최적화 단독이 아니라 아키텍처 변화에 의해 추진된 V3 대비 **토큰당 추론 FLOP 73% 감소**를 반영. 코딩 벤치마크에서 ——R1이 처음 신뢰성을 확립한 영역 —— V4-Pro가 리더보드 상위를 차지한다. **LiveCodeBench 93.5%** (Gemini 3.1 Pro 91.7%와 Claude Opus 4.6 88.8%를 앞섬)와 **Codeforces 레이팅 3206** (GPT-5.4 3168을 추월)을 가지고.

그러나 본 장에 가장 중요한 구조적 디테일은 가격이나 벤치마크가 아니라 **추론 기반**이다. V4 훈련은 NVIDIA A100과 H20 하드웨어를 포함하는 하이브리드 클러스터를 사용했다 ——프런티어 *훈련*이 NVIDIA 스택 밖에서 완전히 일어날 수 있는지의 질문은 어렵게 남아 있다. 그러나 모델은 Huawei의 Ascend 950PR에 **데이-제로로 적응**되었으며, DeepSeek과 Huawei가 공동으로 운영에서 모델을 서비스하는 Ascend NPU와 NVIDIA GPU 사이의 추론 패리티 ——그리고 이 아키텍처에서 NVIDIA의 H20 대비 약 **2.8배 컴퓨트 처리량** —— 를 보고한다. 이는 주권 실리콘 명제의 더 미묘한 형태이다: "우리는 NVIDIA 없이 훈련했다"가 아니라 **"우리는 NVIDIA 없이 서비스한다."** 미국 수출 통제에 직면한 중국 엔터프라이즈 고객에게, V4는 프런티어급 오픈웨이트 모델이 처음으로 신뢰할 만한 국내 실리콘 서빙 경로와 함께 첫날부터 출하된 사례이다 ——이는, 본 장이 기술해 온 배포 중심의 중국 생태계에 대해, 훈련 옵션성보다 부담을 떠받치는 제약에 더 가깝다. R1의 2025년 1월 변곡점과 함께 읽으면, V4는 1년에 걸친 이야기 호를 닫는다: 중국 오픈웨이트 생태계는 이제 프런티어 코딩 모델을 **그리고** 그것을 서비스할 기반을 같은 날에 출시할 수 있다.

### Kimi K2.5 (Moonshot AI)

Kimi K2.5는 "Agent Swarm"을 도입했다 ——단일 쿼리가 약 1,500개의 도구 호출을 통해 협조하는 최대 100개의 서브 에이전트를 생성할 수 있는 능력. 이는 연구 데모가 아니다. 시스템이 수십 개의 동시 에이전트에 걸쳐 웹 검색, 문서 분석, 종합을 병렬화하는 복잡한 연구 작업에 사용되는 운영 기능이다. 이전에 Kimi는 200만 한자 context window (약 2025년 3월)에 도달하여, 중국어 텍스트에 특별히 최적화된 가장 긴 context 모델이 되었다.

### ERNIE 5.0 (Baidu)

ERNIE 5.0은 네이티브 풀 모달리티 지원 ——단일 모델에서 텍스트, 이미지, 오디오, 비디오 이해와 생성 —— 을 가진 Baidu의 2.4조 파라미터 모델이다. 2026년 1월에 출시된 그것은 지식 시스템의 미래가 텍스트 모델 위에 사후에 볼트로 박힌 멀티모달이 아니라 처음부터 멀티모달이라는 Baidu의 베팅을 표현한다.

### GLM-4.5/5 (Zhipu AI)

7,440억 파라미터 MoE GLM-5에서 정점에 이르는 Zhipu AI의 GLM 시리즈는 에이전트 harness를 위해 목적 설계되었다. 모델 아키텍처는 신뢰할 수 있는 에이전트를 만드는 데 필요한 스캐폴딩 코드를 줄이는 네이티브 도구 사용 토큰과 구조화된 출력 보증을 포함한다. 이 "에이전트 네이티브" 설계 철학은 GLM을 운영 파이프라인에 통합할 때 더 적은 prompt engineering과 더 적은 재시도를 의미한다.

## C. 서양 생태계와의 핵심 차이

중국 지식 엔지니어링 풍경을 이해하는 것은 도구와 모델을 카탈로그하는 것 이상을 요구한다. 생태계는 첫날부터 아키텍처 결정을 형성하는 근본적으로 다른 제약과 인센티브 아래에서 운영된다.

### 도구 선호: 시각 우선 vs. 코드 우선

가장 인기 있는 중국 플랫폼들 ——Dify, Coze Studio, FastGPT —— 은 시각 우선이다. 사용자는 캔버스에 노드를 드래그함으로써 지식 파이프라인을 만든다. 대조적으로, 서양 생태계의 지배적 프레임워크 (LangChain, LlamaIndex, Haystack)는 코드 우선이며, 시각 도구는 부차적 추가이다. 이 분기는 다른 사용자 인구를 반영한다: 중국의 AI 채택은 Python을 쓰지 않을 수 있는 엔터프라이즈 IT 부서와 "시민 개발자"에 의해 크게 추진되며, 서양 초기 채택자들은 코드에 편안한 소프트웨어 엔지니어인 경향이 있다.

### 배포: 온프레미스 vs. API 우선

중국에서는 온프레미스 배포가 지배한다. 이는 두 강화하는 요인에 의해 추진된다: 데이터 주권을 위한 규제 요구사항 (특히 금융, 의료, 정부)과 대규모 클라우드 GPU 접근을 더 비싸게 만드는 미국 칩 수출 통제로부터의 실용적 제약. 결과는 중국 플랫폼이 양자화, 증류, 효율성에 크게 투자한다는 것이다 ——무제한 클라우드 컴퓨트를 가정하는 대신 모델이 가용 하드웨어에서 잘 실행되게 만든다. 대조적으로 서양 플랫폼은 모델이 제공자의 인프라에서 실행되는 API 우선 아키텍처를 기본으로 한다.

### 규제 아키텍처

2025년 12월까지, 748개의 AI 서비스가 Generative AI Management Measures 아래 중국 규제 당국에 신고되었다. 컴플라이언스는 선택 사항이거나 열망적이지 않다 ——그것은 설계 단계부터 기술 아키텍처를 형성한다. 콘텐츠 필터링, 감사 로깅, 사용자 정체성 검증이 출시 전에 볼트로 박히지 않고 핵심 기능으로 플랫폼에 빌트인된다. 이 규제 압력은 역설적으로 더 표준화된 아키텍처를 만들었다: 모두가 같은 컴플라이언스 요구사항을 구현해야 할 때, 컴플라이언스를 쉽게 만드는 플랫폼이 이긴다.

### 커뮤니티와 지식 공유

중국 개발자 커뮤니티는 근본적으로 다른 플랫폼에서 운영된다. WeChat 그룹 (Slack이나 Discord가 아니라)이 실시간 토론을 위한 1차 채널이다. Zhihu가 더 긴 기술 Q&A에 대해 Stack Overflow의 역할을 한다. CSDN (China Software Developer Network)은 튜토리얼과 블로그 포스트를 호스팅한다. GitHub는 코드를 위해 사용되지만, 토론은 다른 곳에서 일어난다. 이 파편화는 중국 도구에 대한 도움을 위해 GitHub Issues나 Discord를 검색하는 서양 개발자가 종종 희박한 영어 지원을 발견하는 반면, 중국어 커뮤니티는 활기차고 능동적임을 의미한다 ——단지 비중국어 화자에게 보이지 않을 뿐.

### 제약을 통한 혁신

미국 칩 수출 통제는 예상치 못한 혁신 동력을 만들었다. 단순히 컴퓨트를 스케일할 수 없는 중국 AI 연구실들은 알고리즘 효율성에 불균형하게 투자했다. DeepSeek R1의 600만 달러 미만 훈련 비용이 가장 가시적인 결과이지만, 패턴은 생태계 전반에 걸쳐 확장된다: 더 나은 추론 최적화를 가진 더 작은 모델, 더 공격적인 양자화 기법, FLOP당 능력을 최대화하도록 설계된 아키텍처. 더 많은 컴퓨트가 가용한 서양 생태계는 스케일을 통해 혁신하는 경향이 있다. 둘 다 프런티어 결과를 산출하지만, 다른 경로를 통해서이다.

### 전략적 책무로서의 오픈소스

중국 오픈웨이트 모델 릴리스는 이제 양에서 서양을 능가한다. 이는 이타심이 아니다 ——전략이다. 오픈소스화는 생태계 종속을 만들고 (개발자가 당신의 모델 위에 짓는다), 인재를 끌어들이고 (연구자들이 사람들이 사용하는 모델에서 일하기 원한다), 글로벌 개발자 커뮤니티에 외교적 호의를 만든다. Alibaba의 Qwen에 대한 Apache 2.0 라이선스, DeepSeek의 MIT 라이선스, ByteDance의 Coze Studio 오픈소스화 모두 이 패턴을 따른다. 결과는 세계 어디든 단독 개발자가 이제 모델에서 프레임워크에서 배포 도구까지 완전히 중국 오픈소스 인프라 위에 운영 지식 시스템을 만들 수 있다는 것이다.

## D. Bilibili 콘텐츠에 관한 노트

Bilibili (B站)는 큰 양의 AI 튜토리얼을 호스팅하지만, 실무자들은 많은 것이 영어 YouTube 콘텐츠의 재업로드나 번역임을 알아야 한다. Bilibili의 AI 콘텐츠의 원래 가치는 중국 특정 도구 튜토리얼에 있다: 단계별 Dify 배포 가이드, Qwen 통합 워크스루, 영어로 존재하지 않는 엔터프라이즈 배포 사례 연구. Bilibili에서 연구할 때, 항상 콘텐츠를 그것의 원래 출처로 추적하라. 튜토리얼이 중국어로 더빙된 영어 내레이션을 가진 LangChain을 시연한다면, 원본 YouTube 버전이 더 최신일 가능성이 높다.

## Sources

- Dify GitHub Repository: [https://github.com/langgenius/dify](https://github.com/langgenius/dify)
- RAGFlow GitHub Repository: [https://github.com/infiniflow/ragflow](https://github.com/infiniflow/ragflow)
- FastGPT GitHub Repository: [https://github.com/labring/FastGPT](https://github.com/labring/FastGPT)
- MaxKB GitHub Repository: [https://github.com/1Panel-dev/MaxKB](https://github.com/1Panel-dev/MaxKB)
- Coze Studio GitHub Repository: [https://github.com/coze-dev/coze-studio](https://github.com/coze-dev/coze-studio)
- DB-GPT GitHub Repository: [https://github.com/eosphoros-ai/DB-GPT](https://github.com/eosphoros-ai/DB-GPT)
- Qwen3 Technical Report and model cards, Alibaba Cloud (2025) --- canonical entry points: [https://huggingface.co/Qwen](https://huggingface.co/Qwen) and the Qwen team's Hugging Face write-ups. Apache 2.0 licensing detail confirmed via repository LICENSE files.
- DeepSeek R1 Paper: "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning" (January 2025). [https://github.com/deepseek-ai/DeepSeek-R1](https://github.com/deepseek-ai/DeepSeek-R1) hosts the model and links to the technical report PDF.
- Moonshot AI. Kimi K2.5 Agent Swarm coverage circulated in early 2026 across Moonshot's blog and tech press; the 100-sub-agent / ~1500 tool-call figures cited here are reported from secondary tech-press summaries. Primary access via [https://platform.moonshot.ai](https://platform.moonshot.ai).
- Baidu. ERNIE 5.0 launch (January 2026); 2.4T parameter / native full-modality claims circulated through Baidu official channels and Chinese tech press. No single primary URL is cited here; treat the modality and parameter figures as widely-reported but secondary.
- Zhipu AI. GLM-4/5 model cards on Hugging Face and the official ZhipuAI blog; "744B MoE GLM-5" + agent-native tool tokens are reported across model card and blog coverage. Primary entry point: [https://www.zhipuai.cn](https://www.zhipuai.cn).
- Cyberspace Administration of China, "Generative AI Service Filing" disclosures (December 2025) --- the 748-services figure is widely reproduced in Chinese tech press; the underlying registry is published in batches via the CAC official site.
- "Open Source AI in China" market commentary --- the 23%-to-67% Chinese enterprise open-source adoption shift after R1 is reported across multiple secondary outlets through 2025-2026; treat as widely-cited but no single primary survey is pinned here.
- DeepSeek. "DeepSeek mHC: Manifold-Constrained Hyper-Connections" (April 2026). [https://deepseek.ai/blog/deepseek-mhc-manifold-constrained-hyper-connections](https://deepseek.ai/blog/deepseek-mhc-manifold-constrained-hyper-connections) --- flagged as awaiting independent replication.
- DeepSeek. V4 model release on Hugging Face (April 24, 2026). MIT license; V4-Pro 1.6T (49B active) / V4-Flash 284B (13B active); 1M-token default context.
- Fortune. "DeepSeek unveils V4 model, with rock-bottom prices and close integration with Huawei's chips" (April 24, 2026). [https://fortune.com/2026/04/24/deepseek-v4-ai-model-price-performance-china-open-source/](https://fortune.com/2026/04/24/deepseek-v4-ai-model-price-performance-china-open-source/)
- South China Morning Post. "DeepSeek unveils next-gen AI model as Huawei vows 'full support' with new chips" (April 24, 2026). [https://www.scmp.com/tech/big-tech/article/3351239/deepseek-releases-next-gen-ai-model-world-leading-efficiency](https://www.scmp.com/tech/big-tech/article/3351239/deepseek-releases-next-gen-ai-model-world-leading-efficiency)
- Phemex News. "DeepSeek V4 Matches NVIDIA on Huawei Ascend, Dispels Rumors" (April 2026). [https://phemex.com/news/article/deepseek-v4-matches-nvidia-performance-on-huawei-ascend-dispels-delay-rumors-75616](https://phemex.com/news/article/deepseek-v4-matches-nvidia-performance-on-huawei-ascend-dispels-delay-rumors-75616) --- inference-parity claim, ~2.8x compute throughput vs NVIDIA H20 on Ascend 950PR.

---

*다음 장: [10장 — 실세계 지식 Harness 구축하기](10-case-study.md)*
