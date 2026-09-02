# PPT_v2 · 01_STORY — Cloud Alpacas 최종 발표 내러티브

> **이 문서의 역할:** 최종 발표 PPT를 "왜 이 순서로, 이 톤으로 말하는가" 관점에서 정의한다.
> 슬라이드 목록은 `02_slide_inventory.md`, 슬라이드별 상세 스펙(문구·비주얼·발표자 멘트)은 `03_wireframe.md`.
>
> **소스:** `docs/00_STORY.md` · `docs/01_PROJECT.md` · `docs/02_TEAM_GUIDE.md` · `docs/03_SYSTEM.md` ·
> `docs/04_DEMO.md` · `docs/backlog/06_backlog.md` · `docs/new/ORG_METADATA_INVENTORY.md` ·
> `docs/deliverables/05_ARCHITECTURE.md` · `docs/deliverables/PPT_WIREFRAME/00_WIREFRAME_GUIDE.md`
> (CHAPTER II — DEMO SCENARIO) · `docs/deliverables/05_PERSONA/README.md`.
>
> **원칙:** 구현되지 않은 것을 구현된 것처럼 말하지 않는다. TBD / Future Scope는 그렇게 표기한다.
> 측정되지 않은 KPI·전환율·ROI 숫자는 쓰지 않는다. 유일하게 숫자로 말해도 되는 것은 빌드 수치다(§7).

---

## 1. 청중과 우리가 남기고 싶은 인상

**청중:** Salesforce 본사 / Salesforce 파트너.

**남기고 싶지 않은 인상**
- "우리가 제일 잘한다."
- "우리 정말 열심히 했다."
- "기능 많이 만들었다."

**남기고 싶은 인상**
> "이 사람들은 약 4개월밖에 없었는데, 이미 **Salesforce-native / solution-engineering 방식으로 사고**한다."

**발표 태도**
- 문제와 해법에 대해서는 **자신 있게.**
- 사고 과정에 대해서는 **투명하게.**
- 배운 것에 대해서는 **겸손하게.**

**한 문장 인격:** `WE THOUGHT. WE BUILT. WE LEARNED.`

청중이 발표를 마치고 이렇게 생각하면 성공이다:
> "저 팀은 Salesforce 기능을 배운 게 아니라, **Salesforce로 비즈니스 문제를 푸는 법**을 배웠다."

---

## 2. 핵심 논지 (Core Thesis)

**표지 한 줄:** `FROM FAN DATA TO REVENUE.`

**마무리 한 줄:**
> We came here to learn Salesforce.
> We leave knowing how to build with it.

**관통 서사:**
> 한국에서 야구는 가장 인기 있는 스포츠 중 하나다.
> 그런데도 구단은 재정적으로 어려울 수 있다.
>
> 그래서 우리는 물었다:
> **"팬이 스포츠 구단의 가장 큰 자산이라면, 왜 구단은 팬 데이터를 지속 가능한 사업 가치로 바꾸지 못하는가?"**
>
> 우리의 가설:
> **Fan Data → Customer 360 → Insight → Action → Revenue**
>
> 우리는 팬에서 출발했다.
> 팬을 이해했다.
> 팬 데이터를 인사이트로 바꿨다.
> 그 인사이트를 B2B 스폰서십 세일즈에 연결했다.
> 그리고 그 여정 전체를 Salesforce로 이었다.

---

## 3. 발표 태도 — "잘한 신입 Solution Engineer"의 톤

우리는 이렇게 말하지 않는다: *"우리는 전문가입니다."*
우리는 이렇게 말하지 않는다: *"우리는 열심히 한 학생입니다."*

우리는 이렇게 말한다:
> "우리는 이런 문제를 만났습니다.
> 우리는 이렇게 생각했습니다.
> 우리는 이런 이유로 이 Salesforce 기능을 선택했습니다.
> 우리는 그것을 만들었습니다.
> 그리고 우리는 이것을 배웠습니다."

**아키텍처를 설명할 때 — 판단을 드러낸다:**

| 이렇게 말하지 않는다 | 이렇게 말한다 |
|---|---|
| "Flow를 썼습니다." | "무엇이 자동으로 일어나야 하는지 물었고, 반복되는 비즈니스 로직에는 Flow를 선택했습니다." |
| "Lead를 썼습니다." | "새 Custom Object가 필요한지 고민했지만, 이 업무 프로세스가 이미 Salesforce 표준 Lead 생애주기와 맞는다는 걸 알았습니다." |
| "Agentforce를 썼습니다." | "분석과 추천은 AI가 돕게 하고, 실행과 비즈니스 의사결정의 책임은 Salesforce와 사람이 갖게 하고 싶었습니다." |

---

## 4. 내러티브 아크

```
CHAPTER I — WHY               CHAPTER II — DEMO SCENARIO           CHAPTER III — SO WHAT
(01–05, 매우 압축)              (06–17, 순서·주인공·질문 LOCKED)        (18–19)

의문 ──────▶ 관찰 ──────▶ 판단 ──────▶ 증명 ──────▶ 성찰(18) ──────▶ 브리지(19) ──────▶ (PPT OFF → Org LIVE)
왜 적자?     흩어진 데이터  연결 구조     Demo 12장    설계 판단 4개    "We started with     퀴즈 당첨자 발표
                                                    + Closing 메시지  the business."       → Q&A
```

**후반부 발표 흐름:** DEMO → 18 WHAT WE LEARNED → 19 FROM LEARNING TO BUILDING → **PPT 종료
→ Salesforce Org LIVE → 퀴즈 당첨자 발표(실제 Org 화면) → Q&A.**
Winner / Quiz Result / Thank You / Q&A 슬라이드는 만들지 않는다.

**모든 콘텐츠 슬라이드는 다음 셋 중 하나에 답한다:**

| | 예시 |
|---|---|
| **WE NOTICED** | "팬 데이터는 존재했지만, 흩어져 있었다." |
| **WE DECIDED** | "Fan 360 View의 중심에 Person Account를 놓았다." |
| **WE LEARNED** | "Customer 360은 인사이트가 액션을 촉발할 수 있을 때에야 가치가 생긴다." |

**하지 않는 것:** "우리 기능은 이렇습니다" 라고만 말하는 슬라이드.

---

## 5. AS-IS — 문제

### 5.1 비즈니스 상황

Cloud Alpacas는 한화 이글스를 모델링한 가상의 프로야구 구단이다. 신규 팬 — 특히 20·30대 여성 팬 —
이 빠르게 늘고 있지만, 이 팬층의 구매력·재방문율은 오히려 낮다. 티켓·멤버십·굿즈 매출만으로는
감당이 어려워 구단 재정은 운영상 적자다. 과거에는 "야구 팬 = 40·50대 남성"이라는, 데이터로
검증하지 않은 가정에 따라 장기 스폰서 캠페인을 진행했으나 기대만큼의 성과를 내지 못한 경험이 있다.

> **발표에서 가짜 통계를 쓰지 않는다.** 핵심은 시장 통계를 증명하는 것이 아니라 **비즈니스 질문**이다:
> 팬은 느는데, 왜 구단 매출은 함께 성장하지 않는가?

### 5.2 팬 데이터가 있어도 풀리지 않던 3가지 (Pain Point 압축)

`00_STORY.md §2` / `08_PROJECT_BRIEF.md 01` 을 3개로 압축한다.

1. **DATA IS FRAGMENTED — 팬 데이터가 흩어져 있다.**
   티켓·굿즈·멤버십·앱·문의 데이터가 서로 다른 시스템에 존재한다. "팬은 안 보이고 데이터만 보인다."

2. **DATA DOESN'T BECOME ACTION — 데이터는 많지만 액션이 없다.**
   세분화·분석은 가능하지만, 누구에게 지금 무엇을 할지 결정하고 실행하는 과정이 분절되어 있다.
   결국 모든 팬에게 같은 이벤트·쿠폰·메시지를 보낸다.

3. **FAN VALUE DOESN'T REACH B2B — 팬덤의 가치가 기업의 기회로 연결되지 않는다.**
   팬의 연령·성별·Engagement·구매 특성을 알아도, 적합한 파트너를 발굴하고 Fit을 검증해
   영업 기회로 전환하는 체계가 없다.

---

## 6. TO-BE — 우리의 접근

### 6.1 하나의 흐름

> **DATA → INSIGHT → ACTION → REVENUE**

B2C와 B2B는 별개 프로젝트가 아니라 하나로 연결된 Customer 360이다:

> **Fan Experience → Fan 360 → Fan Insight → Sponsorship Sales**

작은 보조 문장:
> "팬에서 출발한다. 고객을 이해한다. 인사이트를 액션에 연결한다. 그 액션을 매출로 확장한다."

### 6.2 우리가 만든 방식 (기능부터 시작하지 않았다)

```
BUSINESS PROBLEM
      ↓
CUSTOMER / DATA MODEL      (Person Account 중심, 3축 Fan 분류)
      ↓
SALESFORCE STANDARD        (Account · Contact · Lead · Opportunity · Campaign · Quote)
      ↓
FLOW / APEX / LWC          (반복 자동화 · 차별화 로직 · 전용 화면)
      ↓
AGENTFORCE                 (분석·추천 — 실행·결정은 사람)
      ↓
BUSINESS ACTION
```

이 순서 자체가 우리 팀의 실행 방법론이다: **Business → Problem → Persona → Story → Domain → Workflow → Salesforce → Demo**
(`CLAUDE.md §3`). 30개 이상의 의사결정을 ADR(`05_DECISIONS.md`)로 기록했고, PM 1명 + Feature Owner 4명
구조로 각자 자기 구간을 Requirement부터 QA까지 책임졌다(`02_TEAM_GUIDE.md §10~§12`).

---

## 7. 우리가 실제로 만든 것 vs Future Scope (발표 가드레일)

> **원칙:** `04_DEMO.md`에 구현으로 확인된 것만 시나리오에 넣는다. TBD / Future Scope는
> 그렇게 명시한다(`00_WIREFRAME_GUIDE.md` Source of Truth / 금지사항).

### 7.1 ✅ 측정 가능한 빌드 수치 (숫자로 말해도 되는 유일한 것)

`05_ARCHITECTURE.md` 기준, 팀 제작분:

| 자산 | 수 |
|---|---|
| Custom Object | 17 (+ Custom Setting 1, Platform Event 1) |
| Active Flow | 40 |
| Apex Class | 100 |
| Apex Trigger | 1 (`LeadConvertPartnerContact`) |
| LWC | 46 |
| Agentforce Agent | 5 |
| Prompt Template | 6 |
| RecordType | 12 |
| Permission Set (업무용) | 17 |

### 7.2 ✅ 실제 구현된 기능 (Demo에서 보여줄 수 있음)

| 영역 | 구현 | 근거 |
|---|---|---|
| Fan 360 | Landing / List / Timeline, 3축 데이터 모델(Life Cycle / Engagement / Fan Value), Recommendation Hub | `06_backlog.md §3` "완료" |
| 개인화 메시지 | Prompt `Fan_Personalized_Message` + Platform Event + Flow, `Recommendations__c` 저장 | 완료 |
| VIP Recommendation Agent | 조회 → 승인 → 발송 E2E + 실제 이메일 발송 검증 | 완료 |
| 발표 참여 이벤트 | Live Fan Quiz (Experience Site, `Quiz_Entry__c`, 정답 자동판정) | 완료 |
| DART OpenDART API | Apex 콜아웃, Lead 전환 → 공시 자동보강 프로덕션 E2E | 완료 |
| Lead Scoring | `Final_Lead_Score__c` 100점 체계 + Risk Penalty | 검증 진행 |
| PRM 360 Dashboard | LWC 13종 + Report 11종 + Sales Briefing(Prompt) | 검증 진행 |
| Opportunity Agent | Router + Activity/Deal/Proposal/Negotiation 서브에이전트, 확인 단계 | 보완 필요 (활성 버전 재확인) |
| Stage Guidance | `stageGuidance` LWC + Prompt (읽기 전용) | 보완 필요 |
| Interaction Intelligence | Zoom/Meet 대화 → Activity → `Interaction_Intelligence__c` → `Interaction_Signal__c` | 보완 필요 (E2E) |
| Negotiation / Proposal Assistant | 서브에이전트 + Apex | 보완 필요 |
| Sponsorship Package / Quote | Product2 21종 + Standard Quote + Template + PDF (d'Alba E2E) | 완료 |
| Campaign 생애주기 | RecordType 3종 + Deliverable 추적 + Slack 지연 알림 + Sponsorship Campaign Agent | 완료 (Agent 위젯 보완) |

### 7.3 ⚠️ 부분 구현 — "구현된 부분만" 원칙 적용

| 항목 | 상태 | 발표 방식 |
|---|---|---|
| Tableau Next 임베딩 (S5) | 집계 기준·수치 일치 확인 중 | `PPT + 약 5초 임베드 영상` |
| Zoom/Google Meet 연동 (S6) | E2E 재확인 필요 | `DEMO VIDEO` (백업 영상 준비) |
| Partnership Plan / 재계약·Upsell (S9) | 표준 `AccountPlan` Object가 08-31에 생성됐으나 문서에 없고 팀 검증 필요. Campaign Renewal RecordType + 갱신 성과 요약 Flow는 존재 | **FORMAT TBD** — 구현 확인된 부분만, Future Scope는 점선·라벨로 분리 |
| S4 · Partner Matching | `Demo순서.png`에 S4 열이 없음 (S3→S5). Partner Matching을 별도 페이지로 둘지 팀 확정 필요 | **FORMAT TBD** |

### 7.4 🔵 Future Scope (완성된 것처럼 표현 금지 — Slide 17(S9)에서만 점선·흐리게·라벨)

- 계약 이후 실제 광고 효과·팬 반응 성과 분석
- 성과가 낮은 Sponsorship 재검토 / 관계 종료 (판단 기준 TBD)
- 첫 계약 이후 장기 재계약 / Partnership 전환 자동 판단
- Marketing Cloud / Data Cloud 활용, Tableau Next 고도화
- 실시간 외부 데이터 연동, Autonomous Action
- Fan App 대규모 리팩토링 (발표 후, 시간 남으면)

### 7.5 ⚠️ 발표 전 통일 필요

`SPN-LED-BRANDDAY` 상품 금액이 자료마다 **3억 원 / 5.5억 원**으로 다르게 기록돼 있다
(`04_DEMO.md §21 가격 검증`). Product2 · Pricebook · Opportunity Product · Quote · PPT · 발표 대사를
**하나로 통일하기 전까지는 구체적인 금액을 말하지 않는다.**

---

## 8. 페르소나

`docs/deliverables/05_PERSONA/README.md` 기준. 근거 없는 개인정보는 만들지 않는다.

| Persona | 역할 | 발표에서의 위치 |
|---|---|---|
| **김매니저** | Cloud Alpacas FRM Manager (Salesforce User) | S1·S2·S3 앞부분 — B2C 팬 이해·개인화 |
| **이매니저** | Cloud Alpacas Sponsorship Sales Manager (이름 가칭 · 프로필 TBD) | S3 뒷부분~S9 — B2B 발굴·영업·계약 |
| **이루키** | 27세 직장인, 신규 팬 (Customer) | S1·S2의 대표 팬. 관객 참여(S7 Live Event)의 상징 |
| **김하나** | d'Alba 담당자 (**문서에 이름·직책 근거 없음 → "예시"로 표기**) | S6·S8 미팅·협상 상대 |

> Persona별 색: 김매니저 Navy · 이매니저 Orange · 김하나 Teal · 이루키 Pink. 발표 화면에서 색으로 구분.

---

## 9. Architecture Judgment — Slide 18용 4가지 설계 판단

Slide 18에서 "무엇을 만들었나"가 아니라 **"어떻게 판단했나"**를 4개로 압축한다.

| 원칙 | 한 줄 |
|---|---|
| **STANDARD FIRST** | 업무 프로세스가 이미 존재하는 곳에는 Salesforce 표준을 쓴다. (Person Account · Lead · Opportunity · Quote · Contract) |
| **AUTOMATE WHAT REPEATS** | 반복되는 비즈니스 로직은 Flow로 자동화한다. (Trigger는 1개뿐) |
| **CUSTOMIZE WHERE IT MATTERS** | 차별화된 경험·로직에만 Apex / LWC를 쓴다. (Fan Analytics, 전용 화면) |
| **AI WITH HUMAN CONTROL** | Agentforce는 추천·분석하고, Salesforce가 실행하고, 사람이 결정한다. (Human-in-the-loop, 쓰기 작업은 승인 후) |

이 4개는 별도의 무거운 슬라이드가 아니라, Slide 18의 얇은 principle card 밴드로 넣는다.
슬라이드에는 Headline + 1줄만 — 괄호 안의 부연(Person Account 목록 등)은 발표자가 말한다.

---

## 10. 표지·마무리 확정 문구

**표지 (Slide 01)**
- 큰 타이틀: `FROM FAN DATA TO REVENUE.`
- 하단: `Cellsforce · Cloud Alpacas Fan Relationship Management Team`

**Slide 18 — What We Learned (Closing message)**
- 상단: principle card 4개 (§9)
- 큰 문장:
  > We came here to learn Salesforce.
  > We leave knowing how to build with it.
- 그 아래 한 줄, 아주 흐리게: `Fan Data → Customer 360 → Action → Revenue · CELLSFORCE × CLOUD ALPACAS`
- 긴 문단 없음. 감정 톤: 조용한 자신감, 자축 아님.

**Slide 19 — From Learning to Building (PPT의 마지막 장)**
- 상단 작은 label: `FROM LEARNING TO BUILDING`
- 중앙 초대형 두 문장 (이게 전부):
  > We didn't start with Salesforce features.
  > We started with the business.
- editorial typography poster처럼 과감하게 비운다. 다이어그램·카드·아이콘·Object 목록·KPI·팀 소개 없음.
- **이후 PPT 종료 → Salesforce Org LIVE 전환 → 퀴즈 당첨자 발표(실제 Org 화면) → Q&A.**
  Winner / Quiz Result / Thank You / Q&A 슬라이드는 만들지 않는다.

---

## 11. 비주얼 디렉션 (요약 — 상세는 `03_wireframe.md`)

느낌: **Salesforce executive briefing + 모던 product storytelling + Cloud Alpacas 브랜드.**
아닌 것: 학생 프로젝트 / 컨설팅 템플릿 / 기능 카탈로그 / 마스코트 남발.

- 16:9 · 텍스트 최소 · 슬라이드당 지배 메시지 1개 · 큰 타이포 · 강한 시각 위계
- 문단보다 다이어그램, 설명보다 스크린샷, 문장보다 키워드, 넉넉한 여백
- Navy / off-white / orange (Cloud Alpacas) 팔레트. 마스코트는 내러티브 가치가 있을 때만.
- 불필요한 그라데이션·장식 금지
- **B2C → B2B 전환점 = Slide 10.** 여기서 색(파랑→초록)·커넥터·발표 톤이 바뀐다.
- 설치 디자인 스킬: `minimalist-ui` + `high-end-visual-design` 우선, `industrial-brutalist-ui`는 선택적으로.

---

## 12. Demo 프레젠테이션 규칙

PPT는 Demo를 **준비**시킨다. PPT는 Demo와 **경쟁하지 않는다.**

각 Demo 슬라이드:
- **HEADLINE:** 하나의 비즈니스 질문
- **VISUAL:** 하나의 화면 / 하나의 다이어그램 / 하나의 결과
- **KEYWORDS:** 최대 3~5개

발표자가 말로 설명하는 것: 왜 이 문제가 중요한가 / 어떤 Salesforce 기능을 골랐나 / 왜 그 선택이 타당했나.
슬라이드 자체에 전체 설명을 담지 않는다.

---

## 부록. 소스 매핑

| 이 문서 섹션 | 원본 근거 |
|---|---|
| §1 청중·인상 | 사용자 브리프 §1 |
| §2 핵심 논지 | 사용자 브리프 §2 · `00_STORY.md §1·§8` |
| §3 발표 태도 | 사용자 브리프 §3 |
| §4 내러티브 아크 | 사용자 브리프 §7·§11 · `00_WIREFRAME_GUIDE.md` |
| §5 AS-IS | `00_STORY.md §2` · `07_PROPOSAL.md 2` · `08_PROJECT_BRIEF.md 01` |
| §6 TO-BE | `00_STORY.md §8` · `01_PROJECT.md §2.7·§8` · `08_PROJECT_BRIEF.md 02·03` |
| §7 구현 vs Future Scope | `ORG_METADATA_INVENTORY.md` · `06_backlog.md §3` · `05_ARCHITECTURE.md` · `04_DEMO.md` |
| §8 페르소나 | `05_PERSONA/README.md` · `00_STORY.md §4` |
| §9 Architecture Judgment | 사용자 브리프 §8 · `05_DECISIONS.md` D-003·008·017 · `03_SYSTEM.md §7` |
| §10 표지·마무리 | 사용자 브리프 §2·§9 |
| §11 비주얼 | 사용자 브리프 §10 · `00_WIREFRAME_GUIDE.md §1` |
| §12 Demo 규칙 | 사용자 브리프 §12 · `04_DEMO.md §10` |
