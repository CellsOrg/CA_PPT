# backlog-sara.md — Cloud Alpacas에서 Sara가 실제로 한 일

> 이 문서는 "Sara가 만든 코드 목록"이 아니다. Cloud Alpacas(Cellsforce) 프로젝트에서
> Sara가 **어떤 문제를 발견했고, 어떤 제품적·기술적 판단을 했으며, 어떤 팀원과
> 연결해서 최종 결과물을 만들었는가**를 Evidence 교차검증으로 복원한 것이다.
>
> **역할**: Phase 1 — PM / Solution Architect / Product Designer.
> Phase 2 — 위 역할 유지 + **Fan 360 고도화 / B2C↔B2B 연결 지점(Fan Insight·Fan
> Grouping) Feature Owner** + Baby PM(전체 Story·Scope·공용 Data 기준·Integration/QA
> 흐름 연결).

---

## 0. 조사에 사용한 Evidence

| # | Source | 확인 내용 |
|---|---|---|
| 1 | Salesforce Org `CloudAlpacasProd` (`trailsignup-2abe91721f6a94.my.salesforce.com`) | ApexClass / LWC / Flow / CustomObject / GenAiPlannerDefinition의 `CreatedBy` / `LastModifiedBy` (읽기 전용 Tooling API 조회) |
| 2 | GitHub `CellsOrg/cloud-alpacas-agent` (= 로컬 `CA-FRM/cloud-alpacas-agent`) | Sara 단독 11 커밋 — Phase 2 endgame의 LWC/Apex/Flow/Agent 작업 |
| 3 | GitHub `CellsOrg/CloudAlpacas` (팀 repo) | Sara 30 커밋(문서·Dummy Data·Decision·Org 스냅샷) + 팀원 PR(은영/승우/아론) |
| 4 | `CloudAlpacas/docs/*` (00~05, decision_sheet/, data/) | 전 문서 `git log` 저자 = `sara bang` 단독 |
| 5 | `CA-FRM/cloud-alpacas-agent/docs/*` | AGENT_SPEC / EVENT_SPEC / VIP Agent Spec / HANDOFF / 05_DECISIONS 재구성본 |
| 6 | `CloudAlpacas/docs/data/PILOT_COHORT_ANALYSIS.md` | Sara의 60명 Pilot Cohort 생성·검증·Backfill 실행 기록 |

### 팀원 ↔ Org User 매핑 (Evidence 2·3·1 교차)

| 이름 | Git author | Org User | Phase 2 담당 |
|---|---|---|---|
| Sara | `sara bang` | Sara Bang | Fan 360 고도화 + B2B 연결 + Baby PM |
| 승우 | `RafaelJeong` / `Rafael Jeong` | Rafael Espada | Product / Quote / Campaign |
| 은영 | `Dohgrae` | Eunyeong Doh | Opportunity |
| 아론 | `TrailblazerAaron` | Aaron Choi | Account / Contact |
| 혜준 | (커밋 적음) | Hyejune Jo | Collab360 / Lead |
| — | — | Chanyeon Kim | Service Cloud / SDO 데모 템플릿(발표 제외 범위) |

### Contribution Type 범례

`A` 직접 개발 · `B` Sara 설계 → 팀원 구현 · `C` 팀원 기능을 Sara가 수정 ·
`D` 팀원 기능을 Sara가 Integration · `E` Sara QA / Troubleshooting ·
`F` Architecture / UX / Product Design · `G` PM / Scope / Requirement ·
`H` 공동 작업 · `I` Ownership 확인 필요

---

# 1. Project / Product Strategy

## 1.1 프로젝트 세계관·Business Goal·Persona 정의 (00_STORY.md)

- **Role**: PM / Product Designer
- **Contribution Type**: G(PM/Requirement) · F(Product Design) · Documentation
- **Business Purpose**: Salesforce 기능 학습이 아니라 "실제 기업 프로젝트처럼" Customer
  360을 설계하려면, 팀 전체가 "왜 만드는가"에서 출발해야 한다(CLAUDE.md §3 Business
  First). 그 출발점을 한 문서로 고정하는 것이 필요했다.
- **What Sara Did**:
  - 한화 이글스를 모델링한 가상 구단 **Cloud Alpacas**, FRM Team **Cellsforce**라는
    세계관 확정(Decision 001).
  - Business Goal 정의: "신규 팬을 이해하고, 개인화된 액션으로 충성 팬으로 성장시키고,
    장기적으로 Fan Lifetime Value를 높인다."
  - Pain Point 5가지(팬 정보 분산 / 팬 이해 불가 / 세분화 불가 / 타이밍 놓침 / Action
    부재) 정의.
  - Persona 확정: FRM Manager **김매니저**(User) / 신규 팬 **이루키**(Customer)
    (Decision 005).
  - Customer Journey(SNS → 가입 → 첫 티켓 → 첫 직관 → 첫 굿즈 → 재방문 → 멤버십 →
    충성팬)와 상태별 Next Best Action 표 정의.
- **Evidence**: `CloudAlpacas/docs/00_STORY.md` (git log 저자 `sara bang` 7커밋), 커밋
  `52b6a62 docs: add Cloud Alpacas project documentation`
- **Current State**: Git Main ✅ · 문서로 유지 중
- **Status**: COMPLETE

## 1.2 Business First 문서 체계·Source of Truth 원칙 수립

- **Role**: PM
- **Contribution Type**: G(PM) · Documentation
- **Business Purpose**: Baby Team이 같은 내용을 여러 문서에 중복 작성하면 충돌이
  생긴다. 문서마다 역할을 명확히 나누고 우선순위를 정해야 했다.
- **What Sara Did**: `00_STORY`(왜) / `01_PROJECT`(Domain·Workflow·Backlog) /
  `02_TEAM_GUIDE`(팀 운영·역할) / `03_SYSTEM`(Object·ERD·Flow) / `04_DEMO`(시나리오) /
  `05_DECISIONS`(ADR) 6문서 체계와 "충돌 시 05_DECISIONS 우선" 규칙 확정. "문서는 왜,
  GitHub Projects는 오늘 무엇을" 분리 원칙 수립.
- **Evidence**: `docs/CLAUDE.md §7`, `docs/members/README.md`
- **Status**: COMPLETE

## 1.3 팀 역할 정의 + 온보딩 문서 체계 (02_TEAM_GUIDE.md, members/)

- **Role**: PM
- **Contribution Type**: G(PM) · Documentation · H(팀 논의)
- **What Sara Did**:
  - Phase 1: 자동차 비유(무엇을 만들지 = Sara / 프레임·엔진 = 승우 / 내부·QA = 혜준 /
    기능 = 은영 / 운전 경험 = 아론)로 5역할 정의, "만드는 순서 = Business First" 흐름
    다이어그램.
  - Phase 2: **Baby PM + Feature Owner** 운영 모델 설계 — Sara가 전체 Story·Scope·
    공용 Data·Integration/QA를 연결하고, 나머지 4명이 B2B Pipeline 구간을 각자 하나의
    작은 프로젝트로 Requirement~QA까지 책임(§10~§17).
  - `members/00_SARA` ~ `04_AARON` 온보딩 문서 5개 + README 템플릿([P1] Weekly Guide,
    [P2] Current Role) 작성·유지.
- **Evidence**: `CloudAlpacas/docs/02_TEAM_GUIDE.md`, `docs/members/*` (전부 `sara bang`
  저자), 커밋 `c0062b7 은영 문서 수정`, `13eae01 workshop 문서 추가`
- **Status**: COMPLETE

## 1.4 Phase 2 B2B 확장 방향 수립 + 멘토 피드백 반영 (2회 대전환)

- **Role**: PM / Solution Architect
- **Contribution Type**: G(PM/Scope) · F(Architecture) · Documentation
- **Business Purpose**: "팬은 느는데 왜 구단은 적자인가" — Phase 1 Fan 360 데이터를
  구단의 새 수익원(스폰서십 영업)으로 연결하는 것이 Phase 2의 존재 이유.
- **What Sara Did**:
  1. **2026-08-16** — Phase 2 B2B 확장 전체 문서 체계 개편(커밋 `5bc32c2`). Fan
     Insight → 기업 Matching → Outbound Lead → Opportunity → Contract 흐름을
     00_STORY §8~§9, 01_PROJECT §2.7, 03_SYSTEM §7에 신규 서술.
  2. **2026-08-18 멘토링 반영**(커밋 `829feb8`, Decision 019) — 중심축을
     "Collaboration"에서 **"Sponsorship Sales / Pipeline"**으로, 대표 시나리오를
     Sanrio/Hello Kitty → **d'Alba(달바)**로 전환. Fan 목표 규모 약 1,000명 →
     **최소 5,000명**으로 상향. Performance 관련 기능을 Future Scope로 이동.
     `Agentforce Fit/Recommendation Score ≠ Lead Score` 개념 분리를 문서 전체에 반영.
  3. **2026-08-19**(커밋 `524b8a0`, Decision 020) — 기업 DB(약 100개)는 Salesforce
     Object가 아니라 **DART Open API를 Primary Data Source**로 하는 External Input,
     Top 10 Recommendation도 Object 아님, "담당자가 선택한 기업만 Lead" 흐름 확정.
  4. **2026-08-28 발표 범위 재편**(Decision 031, HANDOFF 문서) — 멘토 피드백으로
     P0 Recommendation Agent + P1 발표 참여 Event만 핵심으로, Case/FAQ/Data
     Cloud/Tableau/Campaign 신규기능/Fan App 대규모 리팩토링 전부 발표 제외. 핵심
     메시지를 "① AI가 Fan Action을 추천·실행 / ② 실제 관객 참여 데이터가 CRM으로
     유입" 2개로 압축.
- **Evidence**: `CloudAlpacas/docs/05_DECISIONS.md` Decision 017~020,
  `CloudAlpacas/docs/00_STORY.md §8`, `docs/HANDOFF_SESSION_SUMMARY.md`
- **Current State**: Git Main ✅ · 문서 반영 완료
- **Status**: COMPLETE

## 1.5 Phase 2 Technical Decision 회의 준비·진행 (A~K 11개 항목)

- **Role**: PM / Solution Architect
- **Contribution Type**: G(PM) · F(Architecture) · H(팀 회의)
- **Business Purpose**: Wireframe에 등장하는 Partner Candidate / AI Matching / Quote /
  Lead Score 등이 실제 Salesforce에서 무엇으로 구현될지 팀이 함께 확정해야 했다.
- **What Sara Did**: `P2_TECHNICAL_DECISION_SHEET.md`를 Working Document로 작성 —
  A~K 11개 결정 항목마다 Option A/B 비교표, 장단점, "화요일 결정 질문", Owner, Follow-up
  Doc을 사전 정리. Standard First 원칙(Decision 003) 기준. 회의 후 결과를
  `05_DECISIONS.md` Decision 017·018로 공식 기록하고 01_PROJECT / 03_SYSTEM /
  02_TEAM_GUIDE / members로 반영(반영 순서 규칙까지 정의).
  - 확정: A Lead 흡수 / B Agentforce Matching / C Standard Quote / D Campaign Record
    Type / E `Lead_Score__c` 신규 / F Expected Benefit 3필드 / G Target Segment
    Picklist / H Segment Match=Agentforce / I Recommendation Reason=Agentforce
    자동생성 / **J Fan Insight = Standard Report+Report Type+Dashboard(Sara Owner)**
  - K Account 집계 필드만 On Hold(TBD).
- **Evidence**: `CloudAlpacas/docs/decision_sheet/P2_TECHNICAL_DECISION_SHEET.md`
  (`sara bang` 4커밋), `05_DECISIONS.md` Decision 017·018
- **Status**: COMPLETE (K만 PARTIAL/On Hold)

---

# 2. Salesforce Architecture

## 2.1 Domain Model — Workflow 기준 Entity 추출·정리 (01_PROJECT.md)

- **Role**: Solution Architect
- **Contribution Type**: F(Architecture) · Documentation
- **Business Purpose**: Story("이 세계에 어떤 명사가 있는가")만으로는 실제 업무에 필요한
  Object를 놓친다. 6개 팀(마케팅/티켓/멤버십/굿즈/고객지원/스폰서십) Workflow를 기준으로
  재검증이 필요했다.
- **What Sara Did**:
  - Domain을 3개 → **5개**(Fan / Operations / Marketing / Service / Partnership)로
    재정의.
  - 6개 Workflow를 단계별로 훑어 명사 추출 → 신규 Entity(Fan Segment, Marketing
    Consent, Benefit, Benefit Redemption, Ticket Policy, Eligibility Rule, Ticket
    Transfer, Gate, Admission, Membership Card, Renewal, Shipment, Return,
    Recommendation, Sponsorship Package, Proposal) 도출 및 추가 근거 표.
  - 병합 판단: Promotion + Collaboration Campaign → `Campaign` 통합 / Licensor →
    `Partner` 흡수 / License Contract → `Sponsor Contract` 흡수.
  - "Entity로 만들지 않고 Field로 남길 후보"(Seat Grade, Channel, Product Category,
    Refund/Cancellation 등) 판단 기준 정의.
  - Entity 간 관계 다이어그램(Operations 축 / Fan 축 / Partnership 축) 작성.
- **Evidence**: `CloudAlpacas/docs/01_PROJECT.md` (867줄, `sara bang` 8커밋)
- **Status**: COMPLETE

## 2.2 Salesforce Object Mapping — Standard-first 판단 (01_PROJECT §6, 05_DECISIONS)

- **Role**: Solution Architect
- **Contribution Type**: F(Architecture) · G(Scope) · H(팀 결정)
- **What Sara Did**: Business Entity → Salesforce Object 매핑 전체 표 작성 + 선택지
  비교. Baby Team이 "왜 그렇게 정하는지" 이해하도록 각 항목에 Option A/B 비교(초보자
  예시 포함).
  - Fan = **Person Account** (Contact vs Person Account 비교, B2C 패턴 근거)
  - Ticket/Membership/Goods/Benefit = Product2 vs Custom Object 비교
  - Ticket Purchase/Goods Purchase/Membership Enrollment = **Standard Order**
    (Order vs Opportunity 비교)
  - Refund/Cancellation = Order 필드(`Payment_Status__c`/`Refund_Date__c`/
    `Refund_Reason__c`)로 확정(Decision 013)
  - Season = Custom Object, `Game__c`의 Master-Detail 부모(Decision 011)
  - Attendance_Record__c = Master / Admission__c = Master-Detail 자식(Decision 012)
  - Inquiry = Standard Case
- **핵심 3축 원칙 확립 (Decision 002)**: **Life Cycle**(`Current_Segment__c`) /
  **Engagement Level**(`Engagement_Level__c`) / **Fan Value**(`Fan_Value_Tier__c`) —
  세 축은 서로 독립, 혼용 금지. `Fan_Value_Tier__c`는 전적으로 행동 기반 자동 계산,
  매니저 수동 개입 없음(Decision 003 데이터 무결성 원칙). `Engagement_Level__c`는
  Admission/Order 직접 쿼리로 산출, `Fan_Activity_Pattern__c`(시즌 집계 전용)와
  혼용하지 않음(Decision 004).
- **Boundary**:
  - **Sara**: Object 선택 방향·근거·3축 설계·검토
  - **승우(Rafael Espada)**: 실제 Custom Object 생성 — Org 확인 결과 `Season__c`,
    `Game__c`, `Admission__c`, `Attendance_Record__c`, `Engagement_Signal__c`,
    `Fan_Activity_Pattern__c`, `Fan_Segment_History__c`, `Recommendations__c`,
    `Benefits__c`, `Notification_Log__c` 전부 `CreatedBy = Rafael Espada`
- **Evidence**: `CloudAlpacas/docs/01_PROJECT.md §6`, `05_DECISIONS.md` Decision
  002~013 / Org Tooling `SELECT CreatedBy.Name FROM CustomObject`
- **Status**: COMPLETE

## 2.3 Phase 2 B2B Architecture Draft (03_SYSTEM §7)

- **Role**: Solution Architect
- **Contribution Type**: F(Architecture) · Documentation
- **Business Purpose**: Phase 2 Wireframe(Collab360 / Opportunity Detail 등)이 실제
  Salesforce로 어떻게 매핑될지 확정하기 전, 팀 리뷰용 Draft가 필요했다.
- **What Sara Did**: 03_SYSTEM §7을 "✅ CONFIRMED / ⭐️ DRAFT — Team Review Required"로
  구조화. §7.1에 Standard First로 이미 확정된 것(Lead / Account·Contact / Opportunity /
  Product2 / Campaign 재사용) 정리, §7.2 A~K에 각 Draft 항목의 Option 비교와 화요일
  결정 질문. 멘토링 후 Sponsorship Sales 중심 재서술 및 "Fan Fit Score ≠ Lead Score"
  구분 반영. **B2C Fan Activity → Fan 360 Insight → B2B Sponsorship Sales Decision**
  이라는 확장 논리를 Architecture 레벨에서 명문화.
- **Evidence**: `CloudAlpacas/docs/03_SYSTEM.md §7` (1293줄, `sara bang` 10커밋)
- **Status**: COMPLETE (구현 세부는 각 Feature Owner에게 위임)

## 2.4 Org 검수 리포트 + Org 메타데이터 스냅샷

- **Role**: Solution Architect / PM
- **Contribution Type**: E(QA) · F(Architecture) · Documentation
- **What Sara Did**: 2026-08-17 실제 Org 상태를 읽기 전용으로 조회해 문서(SoT)와 Org의
  차이를 정리한 "org 검수 리포트" 작성(커밋 `dfd0a23`), Org 메타데이터 스냅샷 2회 커밋
  (`c2ae624`, `ebc4295`). `P2_B2B_ORG_BASELINE.md` / `P2_DATA_CONTRACT.md` 작성 —
  Phase 2 시작 시점의 Org baseline과 Record 단위 Owner/Related Record 계약 정의.
- **Evidence**: `CloudAlpacas/docs/decision_sheet/P2_B2B_ORG_BASELINE.md`,
  `P2_DATA_CONTRACT.md`, 커밋 `dfd0a23`, `c2ae624`, `ebc4295`
- **Status**: COMPLETE

## 2.5 Recommendation 실행 아키텍처 재설계 — Campaign 경유 → Recommendation 단위

- **Role**: Solution Architect
- **Contribution Type**: E(Troubleshooting) · F(Architecture) · G(Decision)
- **Business Purpose**: Pilot 검증 중 `Favorite Player Campaign` / `First Merchandise
  Campaign`의 Campaign 화면 "대상 인원 0명"의 원인을 규명해야 했다.
- **What Sara Did**: Org의 실제 활성 Flow 정의를 Tooling API로 직접 확인 →
  `Favorite_Player_Campaign_Flow_V1` / `First_Merchandise_Campaign_Flow_V1` 둘 다
  `Recommendations__c`(+Benefits__c)만 생성하고 **CampaignMember 생성 로직 자체가
  없음**을 발견(조건 미충족이 아니라 기능 부재). 대시보드 "0명"은 실제 데이터를 정확히
  반영한 것으로 판정(버그 아님). **결정(2026-08-25)**: 이 두 항목은 Marketing
  Campaign이 아니라 **개별 Recommendation Action으로 운영**, CampaignMember 자동 생성
  로직은 구현하지 않음. 향후 UX 방향(Recommendation → Prompt Template 개인화 메시지 →
  김매니저 검토/수정 → 실행 → `Status__c = Executed`)까지 설계.
- **Evidence**: `CloudAlpacas/docs/data/PILOT_COHORT_ANALYSIS.md §6.4`
- **Status**: COMPLETE (결정), 향후 UX는 별도 범위

---

# 3. Fan 360

## 3.1 Fan 360 Landing 대시보드 — LWC 직접 개발 (`fan360Landing`)

- **Role**: Feature Owner / Developer / Product Designer
- **Contribution Type**: A(직접 개발) · F(UX/UI)
- **Business Purpose**: 김매니저가 팬 데이터를 하나의 화면에서 보고 다음 액션을
  판단하는 진입점.
- **What Sara Did**: `fan360Landing` LWC(html/js/css)를 **본인이 생성·소유**. 다수
  커밋에 걸쳐 UI/UX 전면 개선 — 대시보드 스타일링 강화(`0d1572b`), 전면 개선
  (`fb6291c`), Fans 화면 리디자인(`cc94fbc`), 추천/리포트 UX 개선(`a6fa180`).
  전용 컨트롤러 `Fan360LandingController.cls`(생성·소유)로 데이터 연동. 공용 스타일
  `staticresources/cloudAlpacas.css` 및 재사용 SVG `icon` LWC 신설.
- **Salesforce**:
  - LWC: `fan360Landing` (CreatedBy/LastModifiedBy = Sara Bang)
  - Apex: `Fan360LandingController` (CreatedBy = Sara Bang)
  - Static Resource: `cloudAlpacas` · FlexiPage `Fan_360_Landing` · Tab
    `Fan_360_Landing`
- **How It Works**: 김매니저가 Fan 360 Landing 탭 진입 → `Fan360LandingController`가
  세그먼트/Engagement/Fan Value/신규가입 등 집계를 조회 → LWC가 카드·차트로 렌더.
- **Problem & Solution**: `@wire` Apex는 반드시 `cacheable=true`여야 호출됨(안 그러면
  무한 로딩) — 조회 메서드를 cacheable로 고정. 여러 화면의 상태/색상 매핑이 중복
  정의되기 쉬워 `fanListTable.js`의 `SEGMENT_CSS`를 공통 참조.
- **Evidence**: Org Tooling(LWC + ApexClass `CreatedBy`), 커밋 `0d1572b` `fb6291c`
  `cc94fbc` `a6fa180`
- **Current State**: Git Main ✅ · Org ✅
- **Status**: COMPLETE

## 3.2 Fan List 커스텀 화면 — Apex + LWC 5종 직접 개발

- **Role**: Feature Owner / Developer
- **Contribution Type**: A(직접 개발) · F(UX) · E(QA)
- **Business Purpose**: 8,000명 이상 규모에서 김매니저가 팬을 검색·필터·정렬하고
  상세를 빠르게 확인해야 한다.
- **What Sara Did**:
  - **`FanListController.cls`**(생성·소유) — `getFanKpiCounts` / `getFanList`
    (segmentFilter · membershipFilter · pendingRecommendation · fanValueFilter ·
    joinedWithinDays) / `getFanDrawerDetail` 3개 메서드.
  - **LWC 5개**(전부 생성·소유): `fanList`(부모) · `fanListKpiCards` ·
    `fanListSearchFilter` · `fanListTable` · `fanDetailDrawer`.
  - `RecommendationActionLabels.cls`(생성·소유) — 액션 영→한 라벨 공통 클래스,
    `FanListController`와 공유.
- **Problem & Solution**:
  - 최근 방문일 정렬: Account에 롤업 필드가 없고 SOQL OFFSET 2,000 제한 + 실시간 정렬
    부담 → **정렬 미지원으로 결정**(Decision 027).
  - 신규 팬(7일) KPI: `CreatedDate` 대신 `Fan_Join_Date__c` 기준 별도 파라미터로 구현.
  - 세그먼트 계열 KPI(활성/이탈위험)는 다른 필터와 조합 허용, 신규팬 KPI는 조합 시
    자동 해제(Decision 028).
  - Fan RecordType 필터를 전 쿼리에 필수 적용 — Phase 2 이후 Account에 팬/스폰서 혼재.
- **Salesforce**: Apex `FanListController`, `RecommendationActionLabels` / LWC
  `fanList` · `fanListKpiCards` · `fanListSearchFilter` · `fanListTable` ·
  `fanDetailDrawer` (전부 CreatedBy = Sara Bang)
- **Evidence**: Org Tooling, `docs/HANDOFF_SESSION_SUMMARY.md`, `05_DECISIONS.md`
  Decision 027·028
- **Current State**: Git Main ✅ · Org ✅ · QA 정상
- **Status**: COMPLETE

## 3.3 팀원 Fan 360 컴포넌트 Integration·리디자인

- **Role**: Feature Owner / Integration / Product Designer
- **Contribution Type**: C(팀원 기능 수정) · D(Integration) · F(UI)
- **Business Purpose**: Phase 1에서 은영이 만든 Fan 360 부품들을 하나의 일관된
  Customer 360 화면으로 통합·정리해야 했다.
- **What Sara Did**: 은영(Eunyeong Doh)이 최초 생성한 다음 LWC를 Sara가 대폭 수정·
  리디자인(Org `LastModifiedBy = Sara Bang`, 최초 `CreatedBy = Eunyeong Doh`):
  `reportDashboard`, `campaignBoard`, `fanTimeline`, `gameDetail`, `fan360Summary`,
  `fanSummary`, `fanRecommendedActions`. Phase 1 컨트롤러 `CampaignController.cls`도
  은영 생성 → Sara 수정.
- **Boundary**:
  - **은영**: Phase 1 Fan 360 컨트롤러(`Fan360Controller`, `GameDetailController`,
    `ReportController`, `FanDetailController`, `CampaignController`) + 세그먼트 LWC
    (`recommendationDashboard`, `segmentOpportunities`, `segmentFanList`) 최초 구현
    (PR #42~#49)
  - **Sara**: 위 컴포넌트들의 UX 재설계·통합·스타일 통일·발표용 정리
- **Evidence**: Org Tooling(LWC `CreatedBy` vs `LastModifiedBy`), 커밋 `18908f4`
  `a6fa180`, `CloudAlpacas` PR #42·#45·#46·#47·#49
- **Status**: COMPLETE

## 3.4 Recommendation Segment Dashboard (`recommendationSegmentDashboard`)

- **Role**: Feature Owner / Developer
- **Contribution Type**: A(직접 개발) · F(UX)
- **What Sara Did**: `recommendationSegmentDashboard` LWC와 `RecommendationSegmentController.cls`
  본인 생성·소유(2026-08-25). 추천 세그먼트 대시보드 기능 강화(커밋 `62af3fa`) —
  세그먼트별 추천 대상·상태 집계 화면. `RecommendationSegmentControllerTest.cls` 포함.
  FlexiPage `Recommendation_Dashboard` / Tab `Recommendation_Dashboard`.
- **Evidence**: Org Tooling(`CreatedBy = Sara Bang`, 2026-08-25/30), 커밋 `62af3fa`
  `a6fa180`
- **Current State**: Git Main ✅ · Org ✅
- **Status**: COMPLETE

---

# 4. Fan Data

## 4.1 공용 Dummy Data 제작 규칙 (DEMO_DATA_STANDARD.md)

- **Role**: PM / Solution Architect
- **Contribution Type**: G(PM) · F(Data Model) · Documentation
- **Business Purpose**: 팀원 5명이 각자 만든 Fan/Order/Product/Partner 데이터가 이름·
  구조가 달라 끊기면 End-to-End Demo가 하나의 Story로 이어지지 않는다.
- **What Sara Did**: Data Contract 문서 작성 — 공용 Naming Rule(Fan=한글 성명,
  Player=한글 성명, Product2=`카테고리-상세`, Campaign=영문 Title Case 등), Shared
  Scenario ID(`SCN-B2B-001`) 관례, Fan Data 분포 기준, **Cross-Object Consistency**
  체크리스트(`Fan_Activity_Pattern__c.Total_Spend__c` = 실제 Order 합계,
  `Current_Segment__c` = `Fan_Segment_History__c` 최신 행 등), Demo Data Owner 표,
  `Draft → QA → Data Freeze → Demo` 프로세스.
- **Evidence**: `CloudAlpacas/docs/data/DEMO_DATA_STANDARD.md` (`sara bang` 3커밋)
- **Status**: COMPLETE

## 4.2 P2 Dummy Data Master — 실제 레코드 값 설계 (30명 + d'Alba 시나리오)

- **Role**: Feature Owner / Product Designer
- **Contribution Type**: A(직접 설계) · F(Data) · G
- **Business Purpose**: Fan Insight 화면의 숫자(여성 팬 비중 변화, 굿즈 전환율, SNS
  반응률)가 Report에서 실제로 재현되려면, 그 숫자를 만드는 레코드 배정이 먼저 있어야
  한다.
- **What Sara Did**:
  - Fan 30명 설계 — Current Segment 6종×5명, Engagement Level 6종×5명, Fan Value
    (VIP 4 / 우수 9 / 일반 17), Gender 15:15, 그중 **10~30대 여성 11명을 SCN-B2B-001
    대표 팬층**으로 지정.
  - Fan Insight 계산 기준(Cross-Object Consistency) — 대표 팬층의 가입일/굿즈 Order/
    `Engagement_Signal__c` 건수를 역산해 "여성 비중 18%→37%", "굿즈 전환 27.3%",
    "SNS 반응 정확히 2배"가 Report에서 나오도록 배정.
  - **d'Alba Sponsorship 시나리오(SCN-B2B-001)** 전체 Master Data — Agentforce
    Recommendation(Top 10 중 하나, Fit 92) → Lead(김하나, `Lead_Score__c` 78) →
    Account/Contact → Opportunity(Advertising Sponsorship, 5,000만원) → Product2
    (Sponsorship Package) → Campaign(Collaboration RT) → Quote까지 각 레코드 필드값.
  - "구 dummy data 아카이빙"(커밋 `7f1dc23`) — 구버전을 `archive/`로 이동.
- **Evidence**: `CloudAlpacas/docs/data/P2_DUMMY_DATA_MASTER.md` (`sara bang` 3커밋),
  커밋 `56103ca dummy sample수정`, `7f1dc23`
- **Status**: COMPLETE

## 4.3 60명 Pilot Cohort — 생성 전 분석 + 실제 Org 생성 + Backfill

- **Role**: Feature Owner / Developer / QA
- **Contribution Type**: A(직접 실행) · E(QA/Troubleshooting) · F
- **Business Purpose**: Fan/Order/Admission/Engagement/Segment 로직과 자동화(Flow)가
  의도대로 맞물리는지, 60명 규모 Fan Journey 데이터 전체를 새로 생성해 검증.
- **What Sara Did** (`feature/pilot-cohort-data` 브랜치):
  - **생성 전 분석**(`PILOT_COHORT_ANALYSIS.md`) — 읽기 전용 SOQL로 Object별 현재 Org
    상태 조사, 재사용 vs 신규 생성 구분(Season/Game/Product2/PricebookEntry/
    Contact(Player)/Campaign은 재사용, Account/Order/Admission/Engagement/Activity
    Pattern은 신규), Mismatch 5건 정리(Account Fan RecordType 로컬 파일 부재 →
    SOQL로 Id 조회, `Fan_Activity_Pattern__c.Season__c` optional이지만 항상 채움,
    Season Total_Games 288 vs 실제 Game 251건, Standard Price Book 이미 활성), 생성
    의존 순서 정의.
  - **실행 결과**: Account 60 / Order 103 / OrderItem 103 / Admission__c 75 /
    Engagement_Signal__c 20 / Fan_Segment_History__c 9 — 실패 0건. 기존
    `PILOT-VIP-TEST-01~05`는 조회만, 미변경 확인.
  - **자동화 검증**: `Order_Paid` Flow(→`Fan_Engagement_Calc`/`Fan_Value_Calc`
    서브플로우)가 코호트별로 정확히 동작함을 확인. 코호트 3의 "티켓 2건" 6명이 예상
    "활동 팬"과 달리 "충성 팬"으로 계산된 것을 발견 — 티켓 구매마다 Admission을 함께
    만들어 `loyaltyScore`가 2플래그를 얻었기 때문(버그 아님, 코호트 스펙의 "예상
    결과"가 현실적 연쇄를 반영 못했던 것을 Pilot이 검증).
  - **VIP → Recommendation → Slack 체인 검증**: 코호트 1(3명) VIP 전환 즉시
    `Recommendations__c`(`Recommended_Action__c = 'VIP Benefit'`) 3건 정확 생성 확인.
  - **Backfill**: `PersonGender`(Male/Female 30:30), `PersonBirthdate`(19~65세),
    `PersonMobilePhone`(고유 010번호), `Acquisition_Channel__c`(SNS 45/검색 25/지인
    20/오프라인 10), Opt-In 4종(코호트 관여도 비례), `Consent_Updated_Date__c` —
    `External_ID__c LIKE 'PILOT-COHORT%'`로만 대상 한정, 미리보기 → 사용자 확인 →
    `--execute`, 60/60 성공.
  - **정정 발견**: `Gender__c`는 Org에 없는 필드(`PersonGender` 사용), 03_SYSTEM §2.1의
    `Gender__c` 기재는 미존재로 확정.
- **Evidence**: `CloudAlpacas/docs/data/PILOT_COHORT_ANALYSIS.md` (521줄),
  브랜치 `feature/pilot-cohort-data`, 커밋 `d030a7d Sara local Salesforce work before
  main sync`
- **Current State**: Org ✅ (60명 + 검증 완료) · Git — 분석 문서는 브랜치
- **Status**: COMPLETE

## 4.4 5,000명 Target Demo Scale + 분포 QA 기준

- **Role**: PM / QA
- **Contribution Type**: G(Scope) · E(QA 기준) · Documentation
- **What Sara Did**: 멘토 피드백(소규모 데이터로는 Segment/Matching/Scoring 분포를
  설득력 있게 못 보여줌)을 반영해 최종 목표를 최소 5,000명으로 상향. 읽기 전용
  조회로 Org에 `RecordType.DeveloperName='Fan'` Account **5,024건 존재**를 헤드카운트
  기준으로 확인. 단 그 5,024건이 분포 기준(Current Segment 각 5%+, Fan Value VIP
  10~15%, Engagement 각 5%+, Gender, 연령대, 대표 팬층 비중)과 필수 Field를 만족하는지는
  **별도 QA 대상 / 미검증**으로 명확히 구분해 기록.
- **Evidence**: `CloudAlpacas/docs/data/DEMO_DATA_STANDARD.md §6.4`, `docs/members/00_SARA.md`
- **Status**: PARTIAL (헤드카운트 ✅ / Field·Distribution QA 미완)

---

# 5. Fan Insight

## 5.1 Fan Insight 화면 방식 결정 (Decision 018-J, Owner: Sara)

- **Role**: Feature Owner
- **Contribution Type**: G(Decision) · F(Architecture) · H
- **Business Purpose**: Fan Insight를 Wireframe처럼 커스텀 화면(LWC)으로 만들지,
  표준 Report로 흐름만 증명할지 결정 필요.
- **What Sara Did**: Standard First 원칙 + Decision 003·009와의 정합성 근거로
  **Standard Report + Report Type + Dashboard**로 확정(별도 Custom Object/LWC 없음).
  "Report로 검증 후 필요 시 LWC" 단계적 접근. 이 결정의 Owner로서 03_SYSTEM §7 J,
  05_DECISIONS Decision 018-J에 반영.
- **Evidence**: `05_DECISIONS.md` Decision 018-J, `P2_TECHNICAL_DECISION_SHEET.md`
  행 J
- **Status**: COMPLETE (결정) / 실제 Report·Dashboard 구성은 PARTIAL

## 5.2 Fan Insight → 팬덤 광고 가치 발견 논리 설계

- **Role**: Solution Architect / Product Designer
- **Contribution Type**: F(Architecture/Product) · G · Documentation
- **Business Purpose**: "팬 데이터가 있으니 광고주를 찾는다"가 아니라 "팬 데이터가
  팬덤의 관심사(뷰티/라이프스타일/F&B)를 보여주고, 그 관심사가 기업 매칭의 근거가
  된다"는 논리적 연결이 Phase 2 Story의 핵심.
- **What Sara Did**: 00_STORY §8.3 / 01_PROJECT §2.7에 Fan 360 Analytics(Engagement /
  Fan Value / Attendance / Engagement Signal) → 팬층 변화 발견 → 광고 가치 가설 →
  기업 DB Matching의 단계 다이어그램과 서술 작성. Fan Insight는 새 저장 Entity가
  아니라 기존 Fan Analytics Entity를 활용하는 **분석 과정**임을 명시(Lead만 신규
  Entity). "여성 팬 유입 증가하나 구매력·재방문율은 낮다 → 단순 팬 수 증가로는 구단
  가치가 안 커진다"는 신호를 데이터로 표현.
- **Evidence**: `CloudAlpacas/docs/00_STORY.md §8.2~8.3`, `01_PROJECT.md §2.7`
- **Status**: COMPLETE (설계·문서) — Agentforce Matching 실제 구현은 혜준 담당

## 5.3 Fan Insight Slack Alert Flow (`Fan_Insight_Slack_Alert`)

- **Role**: Feature Owner / Developer
- **Contribution Type**: A(직접 개발)
- **What Sara Did**: `Fan_Insight_Slack_Alert` Flow 본인 생성·소유(2026-08-31,
  커밋 `a04f81b`). Fan Insight 관련 신호를 Slack으로 알림. `Test_Slack_Notification`
  Flow도 본인 생성.
- **Salesforce**: Flow `Fan_Insight_Slack_Alert` (CreatedBy = Sara Bang)
- **Evidence**: Org Tooling(FlowDefinition `CreatedBy`), 커밋 `a04f81b`
- **Status**: COMPLETE

## 5.4 Target Segment Picklist (Decision 018-G, 공동 Owner: Sara·혜준)

- **Role**: Feature Owner
- **Contribution Type**: G(Decision) · H(공동)
- **What Sara Did**: Target Segment를 자유 입력이 아닌 **Picklist**(사전 정의 목록)로
  하기로 확정 — 값 통일·집계 용이 근거. 실제 값 목록은 TBD로 남김(임의 확정 금지 원칙).
- **Evidence**: `05_DECISIONS.md` Decision 018-G, `docs/members/00_SARA.md §TBD`
- **Status**: PARTIAL (방식 확정 / 값 목록 TBD)

---

# 6. Recommendation / Personalization

## 6.1 Recommendation Review Sidebar — Apex + LWC 직접 개발

- **Role**: Feature Owner / Developer
- **Contribution Type**: A(직접 개발) · F(UX) · E(QA)
- **Business Purpose**: 김매니저가 AI가 생성한 추천 메시지를 화면에서 검수·승인·발송
  (버튼 클릭)하는 흐름 — "AI가 CRM 업무를 실제로 수행한다"의 화면 버전.
- **What Sara Did**:
  - **`RecommendationReviewController.cls`**(생성·소유) — `saveDraftMessage`(승인 후
    수정 시 자동 `Pending` 회귀) / `approveRecommendation` / `sendRecommendationEmail`
    (Approved만 발송 가능, `EmailMessage` 이력 생성, `Sent` 전환).
  - **`recommendationReviewPanel` LWC**(생성·소유) — 상태별 UI(Pending / Approved /
    Sent / Executed / Dismissed), Preview 토글, **"AI 제안 받기"** 버튼(신규
    Autolaunched Flow `Generate_AI_Recommendation_Message`를 Apex에서 동기 호출).
  - `Recommendations__c.Status__c`에 `Approved` / `Sent` 값 추가, `Sent_Date__c`
    필드 — Org `LastModifiedBy = Sara Bang`(최초 `CreatedBy = Rafael Espada`).
  - Sidebar 배치 방식(Lightning App Builder 표준 확장 지점 = Record Page 오른쪽 영역)
    확정(Decision 021).
  - 이메일: Apex `Messaging.SingleEmailMessage` 방식(Decision 022), 고정 HTML 템플릿
    (Apex 문자열 상수)에 순수 텍스트만 삽입(Decision 026), 발신자 = Organization-Wide
    Email Address(Decision 025).
- **Problem & Solution**:
  - `Personalized_Message__c` 저장 버그: Prompt Builder 응답 객체 전체가 문자열로
    저장됨 → `promptResponse=` 접두어 파싱 + HTML 태그 제거 로직 추가, 기존 오염
    레코드 3건 일괄 정제.
  - `AuraHandledException`은 생성자 메시지가 LWC로 전달 안 됨 → `.setMessage(e.getMessage())`
    명시 호출(코드에서 확인됨).
- **Salesforce**: Apex `RecommendationReviewController` / LWC
  `recommendationReviewPanel` / Object `Recommendations__c`(Status·Sent_Date 수정) /
  Flow `Generate_AI_Recommendation_Message`
- **Evidence**: Org Tooling, `CA-FRM/.../classes/RecommendationReviewController.cls`,
  `HANDOFF_SESSION_SUMMARY.md`, `05_DECISIONS.md` Decision 020~026
- **Current State**: Git Main ✅ · Org ✅ · 발송까지 검증됨
- **Status**: COMPLETE

## 6.2 개인화 메시지 생성 Flow + Prompt Template Integration

- **Role**: Feature Owner / Developer / Integration
- **Contribution Type**: A(직접 개발) · D(Integration)
- **What Sara Did**: 본인 생성·소유 Flow —
  - `Fan_Campaign_Personalized_Msg_Flow` — Prompt Builder 호출 + 메시지 정제(HTML
    제거).
  - `Generate_AI_Recommendation_Message` — Autolaunched, Sidebar "AI 제안 받기" 버튼용
    동기 호출(입력 recId → 출력 정제 텍스트, 레코드 미수정).
  - `TEST_Fan_Personalized_Message` — 테스트 Flow.
  - `Fan_Campaign_Msg_Request__e` — Platform Event(캠페인 메시지 요청 트리거), 본인
    생성·소유(Org `CreatedBy = Sara Bang`).
  - `GenAiPromptTemplate` `Fan_Personalized_Message` 연동(force-app에 포함).
- **Salesforce**: Flow ×3 + Platform Event `Fan_Campaign_Msg_Request__e` + Prompt
  Template `Fan_Personalized_Message`
- **Evidence**: Org Tooling(FlowDefinition + CustomObject `CreatedBy = Sara Bang`),
  `CA-FRM/.../flows/`, `genAiPromptTemplates/Fan_Personalized_Message`
- **Status**: COMPLETE

## 6.3 VIP 후보 감지 Flow — 로직 설계 검토 + 수정

- **Role**: Solution Architect / Feature Owner
- **Contribution Type**: C(팀원 Flow 수정) · B(로직 설계 검토) · E(QA)
- **What Sara Did**: `VIP_Candidate_Detection_Flow_V1`(최초 `CreatedBy = Rafael
  Espada`)를 Sara가 수정(Org `LastModifiedBy = Sara Bang`). VIP 전환 감지 → 
  `Recommendations__c` + `Benefits__c`(Coupon 30일) + Slack `#vip-알림` 알림 체인.
  Pilot Cohort로 이 체인이 정상 동작함을 검증(§4.3). `Fan_Value_Tier__c` 완전 자동
  산출 원칙(수동 승인 개입 없음, Decision 003) 유지.
- **Boundary**: **승우** = Flow 최초 구축 / **Sara** = 트리거 조건·로직 설계 검토,
  수정, E2E 검증
- **Evidence**: Org Tooling(FlowDefinition `CreatedBy` vs `LastModifiedBy`),
  `PILOT_COHORT_ANALYSIS.md §6.3`, `03_SYSTEM.md §4`
- **Status**: COMPLETE

## 6.4 Engagement / Value 계산 + Order/Admission 트리거 Flow 체인

- **Role**: Feature Owner / Developer
- **Contribution Type**: A(직접 개발) — 단, Phase 1 3축 설계는 팀 공동(H)
- **What Sara Did**: 현재 Org 기준 본인 생성·소유 Flow —
  `Fan_Engagement_Calc`(5단계), `Fan_Value_Calc`(3단계), `Order_Paid`(트리거 →
  Calc 체인), `Admission_Created`(트리거), `Fan_Activity_Pattern_Admission_Update`,
  `Upsert_Activity_Pattern_From_Order`, `Count_Goods_And_Season`,
  `Order_Membership_Status_Sync`, `Fan_Engagement_Daily_Recalc`(야간 보정).
  D-032(2026-08-28 Vibe 할당량 소진, Sara의 Claude Code가 Apex/Flow/LWC 전체 담당)
  이후 이 계산 체인의 구현·유지를 Sara가 소유.
- **Salesforce**: Flow ×9 (Org `CreatedBy = Sara Bang`)
- **Note**: 3축(Life Cycle / Engagement / Fan Value) **개념 설계**는 Phase 1 팀
  공동 결정(Decision 002~004, Sara 주도). Flow **구현 소유**는 현재 Org 기준 Sara.
- **Evidence**: Org Tooling(FlowDefinition `CreatedBy = Sara Bang`),
  `CA-FRM/.../flows/`
- **Current State**: Git Main ✅ · Org ✅
- **Status**: COMPLETE

---

# 7. B2C → B2B Integration

## 7.1 B2C↔B2B 연결 지점 End-to-End 설계 (Feature Owner)

- **Role**: Feature Owner / Solution Architect
- **Contribution Type**: F(Architecture) · G(Requirement) · Documentation
- **Business Purpose**: Phase 1 Fan 360 데이터가 Phase 2 B2B Sponsorship Sales
  의사결정에 실제로 쓰이고, 그 결과가 다른 담당자의 Feature(혜준의 Lead 발굴)로
  끊기지 않고 이어지게 만드는 것.
- **What Sara Did**:
  - Shared Scenario 흐름 정의(`02_TEAM_GUIDE.md §13`): Fan Insight → DART Open API →
    약 100개 기업 조회 → Agentforce Matching → Top 10 Recommendation → 담당자 선택 →
    Outbound Lead → Lead Qualification → Account/Contact → Opportunity → Sponsorship
    Package/Quote → Campaign(Collaboration RT) → Pipeline/Revenue Dashboard.
  - `SCN-B2B-001`의 **출발점(Fan Insight)**을 책임지고, 그 결과가 혜준의 Partner
    Candidate Discovery 입력이 되는 인수인계 지점 정의.
  - Partner Candidate → Lead 흡수(별도 Object 없음), `Agentforce Fit Score ≠
    Lead Score` 개념 분리를 문서 전반에 반영.
  - Data Contract에서 각 담당자의 Dummy Data가 앞뒤로 연결되는 최소 정보(Naming
    Rule, Related Record, Owner, Dependency, QA) 규칙화.
- **Boundary**:
  - **Sara**: Fan Insight 출발점, 전체 연결 흐름 설계, Integration/QA 조율
  - **혜준**: Agentforce Matching / Lead / `Lead_Score__c`
  - **아론**: Account/Contact (Lead Convert 후) — `DART_Lead_Convert_Match`,
    `DART_Account_Approved_Enrich`, `Rollup_Sponsorship_To_Account` Flow
  - **은영**: Opportunity + Opportunity Agent(v1~v23)
  - **승우**: Product2 Sponsorship Package / Quote / Campaign RT / Sponsorship
    Campaign Agent
- **Evidence**: `02_TEAM_GUIDE.md §10~§17`, `docs/members/00_SARA.md`,
  `00_STORY.md §8`, Org Tooling(팀원 Flow/Agent `CreatedBy`)
- **Status**: COMPLETE (설계·조율) / B2B 구현은 각 Feature Owner

## 7.2 DART Open API를 기업 DB Primary Data Source로 확정 (Decision 020)

- **Role**: Solution Architect / PM
- **Contribution Type**: G(Decision) · F(Architecture) · Documentation
- **What Sara Did**: 커밋 `524b8a0` — 기업 DB(약 100개)를 Salesforce Object로 만들지
  않고 **DART Open API**를 Primary Data Source로 확정. CSV는 개발/테스트용 Optional.
  Top 10 Recommendation도 Object 아님. "담당자가 선택한 기업만 Standard Lead" 흐름을
  01_PROJECT §2.7, 03_SYSTEM §7 B, 05_DECISIONS Decision 020에 반영. 남은 TBD는
  DART Open API의 실제 연동 기술 방식(커넥터/Apex 콜아웃/External Object)뿐임을 명시,
  임의로 새 Object/Field 만들지 않음.
- **Evidence**: `05_DECISIONS.md` Decision 020, 커밋 `524b8a0`
- **Status**: COMPLETE (결정) / 연동 기술 방식 TBD

---

# 8. UX / UI

## 8.1 Phase 1 핵심 4화면 UX 설계

- **Role**: Product Designer
- **Contribution Type**: F(UX 설계) · B(구현은 혜준/은영)
- **What Sara Did**: Fan 360 Dashboard / Fan Profile / Fan Timeline / Recommendation
  Panel의 UX 초안 설계. Information Architecture, User Journey, 화면 흐름 정의.
  (Phase 1에서 구현·QA는 혜준, 데이터 연동은 승우 — `02_TEAM_GUIDE.md §2`)
- **Evidence**: `docs/members/00_SARA.md §Owned Screens`, `02_TEAM_GUIDE.md §2`
- **Status**: COMPLETE

## 8.2 Cloud Alpacas 디자인 시스템 — 브랜드 컬러·공용 CSS·아이콘

- **Role**: Product Designer / Developer
- **Contribution Type**: A(직접 개발) · F(Visual)
- **What Sara Did**: 브랜드 컬러 `#FC4E00` 기준 공용 스타일시트
  `staticresources/cloudAlpacas.css` 신설·확장. 재사용 SVG 아이콘 라이브러리
  `icon` LWC(본인 생성·소유) — 여러 화면에서 인라인 SVG 아이콘 공유. 대시보드·Fans·
  추천·리포트 화면 전면 리디자인 커밋 5회(`0d1572b`~`18908f4`).
- **Salesforce**: Static Resource `cloudAlpacas` / LWC `icon` (CreatedBy = Sara Bang)
- **Evidence**: Org Tooling, 커밋 `0d1572b` `fb6291c` `cc94fbc` `a6fa180` `18908f4`
- **Status**: COMPLETE

## 8.3 발표 참여 Event UX 설계 (EVENT_SPEC.md)

- **Role**: Feature Owner / Product Designer
- **Contribution Type**: F(UX) · G(Requirement) · Documentation
- **What Sara Did**: EVENT_SPEC.md 작성 — 응모 화면(Experience Cloud, 청중 휴대폰용,
  4지선다 + 이름, 브랜드 컬러, 이모지 없이 심플)과 발표 Reveal 화면(큰 스크린용, 대기
  상태 → Reveal 애니메이션 → WINNER 표시, "New Fan Created" 연출은 시각 효과만)의
  와이어프레임·상태·연출 정의. 확정 설계 결정 표(객관식 채점 / 비로그인 LWR / 실제
  Fan 생성 안 함 = `Quiz_Entry__c`에만 저장 / 폴링 없음 / 정답자 중 최대 3명 랜덤 /
  Plan A·B 병행).
- **Evidence**: `CA-FRM/cloud-alpacas-agent/docs/EVENT_SPEC.md` (커밋 `62af3fa`)
- **Status**: COMPLETE

---

# 9. Agentforce / AI

## 9.1 VIP Recommendation Agent — 설계 + Agent Script + Invocable Apex 직접 개발

- **Role**: Feature Owner / Developer / Solution Architect
- **Contribution Type**: A(직접 개발) · F(Architecture) · E(Troubleshooting)
- **Business Purpose (P0)**: 발표 핵심 — "AI가 그럴싸한 대답만 하는 게 아니라, 버튼을
  눌러야 일어나던 일(추천 승인·이메일 발송)이 대화 한 줄로 실제로 일어난다"를 증명.
- **What Sara Did**:
  - **AGENT_SPEC.md**(Business Why / Scope / 시나리오 / Topic·Instructions·Actions) +
    **VIP_Recommendation_Agent-AgentSpec.md**(Agent Script 빌드 설계) 작성.
  - **`VIP_Recommendation_Agent.agent`**(Agent Script, aiAuthoringBundle) 작성·배포 —
    단일 실행 블록(`start_agent vip_recommendations`), Router/subagent 없음, 정중한
    존댓말, 상태 값 hallucination 금지, 범위 밖 요청 정중 거절.
  - **Invocable Apex Action 3개**(전부 본인 생성·소유):
    - `GetPendingVipRecommendationsAction` — Pending VIP Benefit 추천 다건 조회(JSON)
    - `ApproveRecommendationAction` — 기존 `RecommendationReviewController.approveRecommendation`
      얇은 래퍼
    - `SendRecommendationEmailAction` — 기존 `sendRecommendationEmail` 얇은 래퍼,
      기존 Approved 가드 유지
  - Agent 배포·publish·activate, 김매니저에게 접근 권한(`VIP_Recommendation_Agent_Access`
    + `CopilotSalesforceUser`) 부여, 라이브 프리뷰로 조회→승인→발송 E2E + 실제 이메일
    발송까지 검증.
- **Problem & Solution**:
  - **Service Agent → Employee Agent 전환(Decision 033)**: 최초 Service Agent
    (`VIP_Reccommendatio`)는 실행 계정(Einstein Agent User)이 라이선스상 "Send Email"
    권한·`EmailMessage` Create 권한을 가질 수 없어 이메일 발송이 구조적으로 불가능.
    이 실패가 컨트롤러의 `AuraHandledException`이 비-Aura 컨텍스트에서 catch 불가한
    `System.LimitException`으로 나타나 원인 추적에 시간이 걸림. **Employee Agent
    (`AgentforceEmployeeAgent`)로 재구축** — 로그인 사용자(김매니저) 권한으로 Action
    실행하므로 Sidebar에서 되던 승인·발송이 그대로 동작.
  - **Invocable 파라미터(Decision 034)**: `List<Id>` bare 파라미터 대신
    `@InvocableVariable` Request 래퍼 클래스. Apex `Id` 타입은 Agent Script에서
    `object` + `complex_data_type_name: "lightning__recordIdType"`로 매핑.
  - **다건 반환(Decision 036)**: 조회 Action은 JSON 문자열로 반환하고 Agent가 파싱
    (Invocable 1:1 계약 안에서 다건 전달), `filter_from_agent` 하지 않음.
- **Salesforce**:
  - Agent: `VIP_Recommendation_Agent` (v1·v2, Org `GenAiPlannerDefinition
    CreatedBy = Sara Bang`), aiAuthoringBundle
  - Apex: `GetPendingVipRecommendationsAction`, `ApproveRecommendationAction`,
    `SendRecommendationEmailAction` (전부 CreatedBy = Sara Bang)
  - Permission Set: `VIP_Recommendation_Agent_Access`
  - App: `Cloud_Alpacas_FRM`
- **Evidence**: Org Tooling(GenAiPlannerDefinition + ApexClass `CreatedBy = Sara
  Bang`), `docs/AGENT_SPEC.md`, `docs/VIP_Recommendation_Agent-AgentSpec.md`,
  `05_DECISIONS.md` Decision 033~037, 커밋 `caf172f`
- **Current State**: Git Main ✅ · Org ✅ (publish + activate) · E2E + 실제 이메일 검증
- **Status**: COMPLETE (남은 이슈: 실제 발표 계정 권한 확인, 한국어 `ko` 설정 복구)

## 9.2 Agent 아키텍처 표준 채택 (Decision 035)

- **Role**: Solution Architect
- **Contribution Type**: F(Architecture) · G(Decision)
- **What Sara Did**: "도메인이 하나면 Router + 복수 서브에이전트보다 **단일 실행 블록
  (`start_agent`)**으로 설계"를 표준으로 채택 — 상태 리셋·참조 깨짐 리스크 감소.
  "승인된 것만 발송" 안전장치는 Agent 변수/머신 게이트가 아니라 **Apex 하드 가드**로
  강제(Rule 7 최소 상태 준수).
- **Evidence**: `05_DECISIONS.md` Decision 035, `VIP_Recommendation_Agent-AgentSpec.md §5·§8`
- **Status**: COMPLETE

## 9.3 Agentforce Matching 범위 예외 승인 (Decision 017)

- **Role**: PM
- **Contribution Type**: G(Scope) · H(팀 회의)
- **What Sara Did**: CLAUDE.md §5가 Agentforce를 Future Scope로 못박아뒀으나, AI
  Matching / Segment Match / Recommendation Reason에 한해 **Phase 2 범위 좁은 예외로
  승인**하고 CLAUDE.md §5도 함께 갱신(Business Decision). 실제 Agentforce Matching
  구현은 혜준 담당으로 명확히 분리.
- **Evidence**: `05_DECISIONS.md` Decision 017, `CLAUDE.md §5`
- **Status**: COMPLETE

---

# 10. Demo / QA

## 10.1 Demo 시나리오 전면 재작성 (04_DEMO.md)

- **Role**: PM / Product Designer
- **Contribution Type**: G(Demo planning) · F · Documentation
- **What Sara Did**: 발표 범위 재편(D-031)에 맞춰 04_DEMO.md 재작성 — 기존 전체 여정
  시나리오(Case, 다중 Campaign)를 의도적으로 제외하고 **Scene 1(Recommendation Agent,
  P0)** + **Scene 2(발표 참여 Event, P1)** 2장면 중심으로 축소. 각 Scene의 흐름,
  사전 준비 체크리스트, 실패 시 대체 경로(수동 Sidebar 발송), "다루지 않는 것"과 질문
  대응 멘트, 남은 QA 범위(P2~P4).
- **Evidence**: `CA-FRM/cloud-alpacas-agent/docs/04_DEMO.md`
- **Status**: COMPLETE

## 10.2 Live Fan Quiz — Apex + LWC 2종 + Flow + Object 직접 개발 (P1)

- **Role**: Feature Owner / Developer
- **Contribution Type**: A(직접 개발) · F(UX)
- **Business Purpose**: "실제 사람의 참여가 그대로 Salesforce 데이터가 되고, 그
  데이터가 다시 화면에 살아 움직인다"를 발표장에서 실시간으로 보여주기.
- **What Sara Did** (전부 본인 생성·소유):
  - `Quiz_Entry__c` Custom Object + 필드(`Entrant_Name__c`, `Selected_Answer__c`,
    `Is_Correct__c`, `Is_Winner__c`, `Submitted_At__c`) — Setup UI 직접 생성
    (팀 원칙: Tooling/Metadata API 필드 미반영 회피).
  - `QuizEntrySubmitController.cls` — Guest User가 인증 없이 응모 insert.
  - `LiveFanQuizRevealController.cls` — 정답자 중 최대 3명 랜덤 추첨, `Is_Winner__c`
    업데이트.
  - `liveFanQuizEntry` LWC — Experience Cloud 응모 페이지.
  - `liveFanQuizReveal` LWC — 발표용 대기 화면 + Reveal 애니메이션 + 응모 집계.
  - `Quiz_Entry_Set_Is_Correct` Flow — 정답 판정.
  - FlexiPage `Live_Fan_Quiz_Reveal` + Tab, Experience Cloud 사이트 설정, `FanQuiz
    Profile` / `Marketing Landing Pages Profile`.
  - 응모 집계 및 전체 화면 UI 리뉴얼(커밋 `a04f81b`), 응모·추첨·Reveal 화면 최초 추가
    (커밋 `962dde7`).
- **Salesforce**: Object `Quiz_Entry__c` / Apex `QuizEntrySubmitController` ·
  `LiveFanQuizRevealController` / LWC `liveFanQuizEntry` · `liveFanQuizReveal` /
  Flow `Quiz_Entry_Set_Is_Correct` (전부 CreatedBy = Sara Bang)
- **Evidence**: Org Tooling, `CA-FRM/.../classes/`, `docs/EVENT_SPEC.md`,
  커밋 `962dde7` `a04f81b`
- **Current State**: Git Main ✅ · Org ✅
- **Status**: COMPLETE

## 10.3 이메일 발송 인프라 검증 (Decision 025)

- **Role**: QA / Solution Architect
- **Contribution Type**: E(Troubleshooting) · G(Decision)
- **What Sara Did**: Gmail 수신 실패 원인 규명 — 개인 웹메일 도메인(gmail.com)은
  SPF/DKIM 인증이 구조적으로 불가능(도메인 소유자만 설정 가능), Trial org에서 우회
  불가. Naver 메일 정상 수신 확인 → **데모는 Naver 계정으로 진행** 결정. 백로그 기록:
  "실제 회사 도메인 확보 시 Authorized Email Domain 설정으로 완전 해결 가능".
- **Evidence**: `HANDOFF_SESSION_SUMMARY.md`, `05_DECISIONS.md` Decision 025
- **Status**: COMPLETE

## 10.4 Campaign Hub 조사 (설계 완료, 구현 보류)

- **Role**: Solution Architect / QA
- **Contribution Type**: E(Troubleshooting) · F(설계) · G(Scope)
- **What Sara Did**: Campaign 대상 인원 0명/2명 원인 규명 —
  - First Merchandise: `Attendance_Record__c` Flow의
    `doesRequireRecordChangedToMeetCriteria=true`가 이미 조건 충족된 과거 데이터
    (2,972건)에 소급 미적용.
  - Favorite Player: `Product2.Related_Player__c`가 전체 상품 중 2개에만 설정.
  - `First_Ticket_Campaign_Flow_V1`이 "10% 쿠폰 도착" 알림은 보내지만 실제
    `Benefits__c` 미발급(알림-실체 불일치 버그).
  - `Benefits__c` 신규 필드 5개 설계·생성(`Badge_Label__c`, `Discount_Rate__c`,
    `Min_Purchase_Amount__c`, `Benefit_Type__c`에 `Badge` 값, `Contact.Name_EN__c`,
    `Product2.Is_Player_Goods__c`) — Setup UI 직접 생성. **필드만 생성, Flow 연결
    로직은 발표 우선순위 재편으로 Future Scope 보류**(Decision 030).
- **Evidence**: `HANDOFF_SESSION_SUMMARY.md`, `05_DECISIONS.md` Decision 029·030
- **Status**: PARTIAL (원인 규명·필드 생성 ✅ / 로직 연결 보류)

## 10.5 팀 개발 결과 검수 (은영 세그먼트/Apex PR, 승우 Campaign Flow)

- **Role**: PM / Feature Owner
- **Contribution Type**: E(검수) · D(Integration) · H
- **What Sara Did**: 은영의 PR #42~#49(segment 1~4 real-time count, Apex 5클래스,
  fanlist/detail view)를 받아 Fan 360 화면으로 통합·리디자인(§3.3). 승우의 Phase 1
  Campaign Flow 6종(`Welcome_Campaign_Flow`, `First_Ticket_Campaign_Flow_V1`,
  `First_Visit_Guide_Flow`, `First_Merchandise_Campaign_Flow_V1`,
  `Favorite_Player_Campaign_Flow_V1`) 수정·검증(Org `LastModifiedBy = Sara Bang`).
  Integration/QA 흐름 조율(`02_TEAM_GUIDE.md §15`: Feature QA → Integration QA →
  End-to-End Demo QA).
- **Evidence**: Org Tooling(FlowDefinition `LastModifiedBy`), `CloudAlpacas` PR
  히스토리, `02_TEAM_GUIDE.md §15`
- **Status**: COMPLETE

---

# 11. Documentation / Deliverables

## 11.1 프로젝트 Source of Truth 문서 6종 + 부속 문서

- **Role**: PM / Solution Architect / Product Designer
- **Contribution Type**: Documentation (전부 Sara 단독 저자) · Cross-check
- **What Sara Did**: `git log`상 저자가 `sara bang` 단독인 문서:

| 문서 | 줄수 | Sara 커밋 수 |
|---|---|---|
| `00_STORY.md` | 269 | 7 |
| `01_PROJECT.md` | 866 | 8 |
| `02_TEAM_GUIDE.md` | 423 | — |
| `03_SYSTEM.md` | 1293 | 10 |
| `04_DEMO.md` | 351 | 7 |
| `05_DECISIONS.md` | 1339 | 9 |
| `decision_sheet/P2_TECHNICAL_DECISION_SHEET.md` | 110 | 4 |
| `data/DEMO_DATA_STANDARD.md` | 173 | 3 |
| `data/P2_DUMMY_DATA_MASTER.md` | 297 | 3 |
| `data/PILOT_COHORT_ANALYSIS.md` | 521 | — |
| `decision_sheet/P2_B2B_ORG_BASELINE.md` / `P2_DATA_CONTRACT.md` | 244 / 161 | — |
| `members/00~04 + README` | — | — |

- 추가(CA-FRM repo): `CLAUDE.md`(13KB), `AGENT_SPEC.md`, `EVENT_SPEC.md`,
  `VIP_Recommendation_Agent-AgentSpec.md`, `HANDOFF_SESSION_SUMMARY.md`,
  05_DECISIONS 재구성본.
- **Cross-check**: CLAUDE.md §7 Source of Truth 원칙 유지, 문서 간 충돌 확인, 반영
  순서 규칙(Decision Sheet → 05_DECISIONS → 03_SYSTEM → 02_TEAM_GUIDE/members →
  04_DEMO → data/) 정의.
- **Evidence**: `git log --pretty=%an -- <file>` (CloudAlpacas repo)
- **Status**: COMPLETE

## 11.2 제출 산출물 설계 (ERD / Requirements / Process Flow / Architecture)

- **Role**: Solution Architect / PM
- **Contribution Type**: F · Documentation · H(팀 검토)
- **What Sara Did**: ERD·System Architecture·Process Flow·Data Flow 다이어그램
  (03_SYSTEM), Domain Model·Requirements(01_PROJECT), MVP Implementation Matrix,
  Custom Metadata/Permissions 방향, Project Proposal 서사(00_STORY). Excel Object
  Map / Member Sheet(구글시트 `🦙 CloudAlpacas - 메타데이터 기록 [B2B 확장]`)를 회의
  Source of Truth로 운영. workshop 문서 추가(커밋 `13eae01`), org 시안 업로드(커밋
  `2612540`).
- **Evidence**: `CloudAlpacas/docs/03_SYSTEM.md`, `01_PROJECT.md`,
  `P2_TECHNICAL_DECISION_SHEET.md §0`, 커밋 `13eae01` `2612540`
- **Status**: COMPLETE

---

# 12. Troubleshooting

> 아래는 Sara가 원인을 규명하고 재발 방지 체크리스트로 정리한 항목이다
> (`CLAUDE.md §11`, `HANDOFF_SESSION_SUMMARY.md`).

| # | 문제 | Sara의 규명·해결 | Evidence |
|---|---|---|---|
| T1 | 새 커스텀 필드가 스키마에 반영 안 됨 | Tooling API / Metadata API 배포 모두 이 org에서 필드 미반영 확인 → **Setup UI 직접 생성이 유일하게 안전** | CLAUDE.md §11, HANDOFF |
| T2 | LWC에 항상 "알 수 없는 오류"만 표시 | `AuraHandledException`은 생성자 메시지가 전달 안 됨 → `.setMessage(e.getMessage())` 명시 호출(코드 반영 확인) | `RecommendationReviewController.cls` |
| T3 | `@wire` Apex 무한 로딩/즉시 에러 | `@AuraEnabled(cacheable=true)` 필수, 데이터 변경 메서드만 `cacheable=false` + imperative | CLAUDE.md §11 |
| T4 | `INVALID_OR_NULL_FOR_RESTRICTED_PICKLIST` | Restricted Picklist는 로컬 메타에 값 추가해도 org 배포 전엔 사용 불가 → 배포 후 재조회 확인 | CLAUDE.md §11 |
| T5 | Gmail 이메일 미수신 | 개인 웹메일은 SPF/DKIM 인증 구조적 불가 → Naver로 데모 | Decision 025 |
| T6 | Prompt Builder 응답이 필드에 통째로 문자열 저장 | `promptResponse=` 접두어 파싱 + HTML 태그 제거, 오염 레코드 3건 정제 | HANDOFF |
| T7 | 트리거 Flow가 과거 데이터에 소급 미적용 | `doesRequireRecordChangedToMeetCriteria=true`는 소급 안 됨 → "예상 vs 실제 수치" 정기 대조 | Decision 029 |
| T8 | Campaign "대상 인원 0명" | Flow에 CampaignMember 생성 로직 자체가 없음(기능 부재), 대시보드는 정확 → Recommendation 단위 운영으로 결정 | PILOT_COHORT_ANALYSIS §6.4 |
| T9 | Agent 이메일 발송 크래시 (`System.LimitException`) | Service Agent 실행 계정 라이선스 한계 → Employee Agent로 재구축 | Decision 033 |
| T10 | Agent Script가 bare `List<Id>` 바인딩 미인식 | `@InvocableVariable` Request 래퍼 + `lightning__recordIdType` 매핑 | Decision 034 |
| T11 | 코호트 3 "티켓 2건"이 예상과 다른 세그먼트로 계산 | 티켓 구매마다 Admission 동반 → `loyaltyScore` 2플래그 → "충성 팬" 먼저 매칭(버그 아님, 스펙의 예상 결과가 부정확했음) | PILOT_COHORT_ANALYSIS §6.2 |
| T12 | `Gender__c` 필드 부재 | Org에 없음, `PersonGender` 표준 필드 사용 → 03_SYSTEM 정정 | PILOT_COHORT_ANALYSIS §6.5 |

- **Contribution Type**: E(Troubleshooting) 전반
- **Status**: COMPLETE (T7·T8은 결정으로 종결, 로직 연결은 Future Scope)

---

# 13. Major Decisions (Sara가 주도/기록한 ADR)

| Decision | 내용 | Sara 역할 |
|---|---|---|
| D-001 | 세계관 = Cloud Alpacas, 팀명 Cellsforce | 주도 |
| D-002~004 | 3축 원칙(Life Cycle / Engagement / Fan Value), 자동 산출, 축 혼용 금지 | 주도 |
| D-005 | Demo 페르소나(김매니저 / 이루키) | 주도 |
| D-009~013 | Segment History, Engagement 계산식, Season, Attendance Master-Detail, Order 환불 필드 | 주도·기록 |
| D-017 | Agentforce Matching 범위 예외 승인 | PM 승인 |
| D-018 A~K | Partner Candidate→Lead / Quote / Campaign RT / Lead Score / Expected Benefit / Target Segment / Segment Match / Recommendation Reason / **Fan Insight 화면(Owner)** / Account 집계 | 회의 준비·진행·기록 |
| D-019 | Sponsorship Sales 중심 전환, 대표 시나리오 d'Alba, Fan 5,000명, Performance Future Scope | 주도 |
| D-020 | 기업 DB = DART Open API Primary, Object 아님 | 주도 |
| D-021~028 | Recommendation Sidebar 배치 / 이메일 Apex 방식 / 재승인 회귀 / 읽기전용 상태 / OWA 발신 / 고정 HTML 템플릿 / 방문일 정렬 미지원 / KPI 조합 규칙 | 주도(직접 개발과 병행) |
| D-029~032 | Campaign 대상자 급감 원인 / Benefits 필드 신설·보류 / 발표 범위 재편 / 도구 역할 임시 전환 | 주도·기록 |
| D-033~037 | VIP Agent = Employee Agent / Invocable 래퍼 패턴 / 단일 실행 블록 표준 / JSON 다건 반환 / P0 완료 | 주도(직접 개발) |

- **Evidence**: `CloudAlpacas/docs/05_DECISIONS.md`(1339줄) + `CA-FRM` 재구성본
- **Status**: COMPLETE

---

# Sara's Contribution Summary

### Product

Sara는 Cloud Alpacas의 **"왜 이 제품이 존재하는가"를 정의하고 끝까지 지킨 사람**이다.
Business Goal · Pain Point · Persona · Customer Journey를 정의했고(00_STORY),
Phase 2에서 "팬은 느는데 왜 적자인가"라는 문제를 Fan 360 데이터 → 팬덤 광고 가치 →
Sponsorship Sales Pipeline이라는 제품 서사로 연결했다. 멘토 피드백을 받아 프로젝트
방향을 두 번(Collaboration→Sponsorship, 전체여정→2장면) 크게 틀었고, 그때마다 6개
문서를 정합성 있게 갱신했다. Fan Insight / Fan Grouping / Recommendation / Live Fan
Quiz의 Feature Owner로서 요구사항부터 화면·QA까지 책임졌다.

### Architecture

5개 Domain Model, Workflow 기준 Entity 추출, Business Entity → Salesforce Object
매핑(Person Account / Standard Order / Standard Lead·Quote 등 Standard-first 판단),
3축 데이터 모델(Life Cycle / Engagement / Fan Value)을 설계했다. Phase 2 B2B
Architecture Draft(03_SYSTEM §7)와 A~K 11개 Technical Decision을 준비·진행했으며,
"B2C Fan Activity → Fan 360 Insight → B2B Sponsorship Decision" 확장 구조와
"Agentforce Fit Score ≠ Lead Score" 개념 분리를 명문화했다. Agent 아키텍처
표준(단일 실행 블록, Apex 하드 가드)도 정립했다.

### Design

Phase 1 핵심 4화면 UX 초안, Cloud Alpacas 디자인 시스템(브랜드 컬러 `#FC4E00`, 공용
CSS, `icon` SVG 라이브러리), Fan 360 Landing / Fan List / Recommendation Segment
Dashboard / 발표 참여 Event의 화면 UX를 설계·구현했다. 팀원(은영)이 만든 Fan 360
부품 7종을 하나의 일관된 Customer 360 화면으로 리디자인·통합했다.

### Development

**직접 생성·소유한 Salesforce 컴포넌트**(Org `CreatedBy = Sara Bang` 확인):

- **Apex 10+**: `FanListController`, `Fan360LandingController`,
  `RecommendationReviewController`, `RecommendationActionLabels`,
  `RecommendationSegmentController`, `GetPendingVipRecommendationsAction`,
  `ApproveRecommendationAction`, `SendRecommendationEmailAction`,
  `LiveFanQuizRevealController`, `QuizEntrySubmitController` (+ Test 클래스)
- **LWC 11**: `fan360Landing`, `fanList`, `fanListKpiCards`, `fanListSearchFilter`,
  `fanListTable`, `fanDetailDrawer`, `recommendationReviewPanel`,
  `recommendationSegmentDashboard`, `liveFanQuizEntry`, `liveFanQuizReveal`, `icon`
- **Flow 14**: `Fan_Engagement_Calc`, `Fan_Value_Calc`, `Order_Paid`,
  `Admission_Created`, `Fan_Activity_Pattern_Admission_Update`,
  `Upsert_Activity_Pattern_From_Order`, `Count_Goods_And_Season`,
  `Order_Membership_Status_Sync`, `Fan_Engagement_Daily_Recalc`,
  `Fan_Campaign_Personalized_Msg_Flow`, `Generate_AI_Recommendation_Message`,
  `TEST_Fan_Personalized_Message`, `Quiz_Entry_Set_Is_Correct`,
  `Fan_Insight_Slack_Alert`, `Test_Slack_Notification`
- **Object**: `Quiz_Entry__c`, `Fan_Campaign_Msg_Request__e` (Platform Event)
- **Agent**: `VIP_Recommendation_Agent` (Employee Agent, Agent Script + 3 Invocable
  Action) + Permission Set `VIP_Recommendation_Agent_Access`, App `Cloud_Alpacas_FRM`
- **Prompt Template**: `Fan_Personalized_Message` 연동

### Integration

팀원이 만든 것을 수정·통합한 것: LWC 7종(`reportDashboard`, `campaignBoard`,
`fanTimeline`, `gameDetail`, `fan360Summary`, `fanSummary`, `fanRecommendedActions`
— 최초 `CreatedBy = Eunyeong Doh`), Apex `CampaignController`(은영 생성),
Flow 6종(`VIP_Candidate_Detection_Flow_V1` 및 Phase 1 Campaign Flow 5종 — 최초
`CreatedBy = Rafael Espada`), `Recommendations__c` Object(승우 생성, Sara가
Status/Sent_Date 확장). B2C↔B2B 전체 연결 흐름(Fan Insight → … → Pipeline
Dashboard)을 설계하고 혜준/아론/은영/승우의 Feature가 끊기지 않게 조율.

### QA

60명 Pilot Cohort를 실제 Org에 생성하고 자동화(Engagement/Value Calc, VIP →
Recommendation → Slack)를 검증, `Order_Paid` Flow의 세그먼트 계산 특성(코호트 3
"충성 팬" 매칭)을 규명. Campaign 대상 인원 0명의 원인(CampaignMember 생성 로직 부재)을
Tooling API로 규명. 이메일 인프라(SPF/DKIM) 한계 규명. `Gender__c` 필드 부재 정정.
Agent 이메일 발송 크래시(Service Agent 라이선스) 규명·해결. 재발 방지 체크리스트
12항목을 CLAUDE.md §11에 정리.

### PM

프로젝트 방향(Phase 1 B2C MVP → Phase 2 B2B Sponsorship), Scope(5,000명 목표,
발표 2장면 압축), Demo 시나리오, 제출 산출물(ERD/Requirements/Architecture), 팀 운영
모델(Baby PM + Feature Owner), 문서 Source of Truth 체계, 30+ Decision을 조정·기록.
멘토 피드백을 세 차례(2026-08-18, 08-19, 08-28) 프로젝트에 반영.

---

# Sara's Top 10 Contributions

1. **Business Goal·Persona·Story 정의(00_STORY)** → 팀 전체가 "왜 만드는가"에서
   출발하는 Business First 프로젝트의 기준점이 됨 → 6개 문서 체계와 모든 Decision의
   근거.
2. **5 Domain Model + Object Mapping + 3축 데이터 모델 설계** → Baby Team이
   Standard-first로 Object를 선택하는 판단 근거 확보 → 승우가 Custom Object 10종을
   근거 있게 구축.
3. **Phase 2 B2B 방향 전환(Decision 019·020)** → "팬은 느는데 왜 적자인가"를
   Sponsorship Sales Pipeline으로 연결, 대표 시나리오 d'Alba 확정 → Phase 2 전체
   Story·Data·Architecture가 하나의 축으로 정렬.
4. **VIP Recommendation Employee Agent 직접 개발(P0)** → Service Agent 라이선스
   한계를 규명하고 Employee Agent로 재구축, Agent Script + Invocable Apex 3개 → 발표
   핵심 "AI가 CRM 업무를 실제 수행" E2E + 실제 이메일 발송까지 검증 완료.
5. **Recommendation Review Sidebar(Apex + LWC) 직접 개발** → 김매니저가 AI 메시지를
   검수·승인·발송하는 화면, Prompt 응답 파싱 버그 해결 → Agent가 재사용하는 핵심 자산.
6. **Fan List 커스텀 화면(Apex + LWC 5종) 직접 개발** → 8,000명+ 규모에서 검색·필터·
   KPI·Drawer, OFFSET 2000 제약을 정렬 미지원 결정으로 우회 → Fan 360의 실사용 진입점.
7. **60명 Pilot Cohort 생성·검증·Backfill** → Fan Journey 데이터 전체를 새로 만들어
   자동화 Flow가 의도대로 맞물리는지 검증, 세그먼트 계산 특성·Campaign 0명 원인·
   `Gender__c` 부재를 발견 → Demo 데이터 QA의 기반.
8. **공용 Dummy Data 규칙 + P2 Master Data 설계** → Naming Rule·Cross-Object
   Consistency·`SCN-B2B-001`로 팀원 5명의 데이터가 하나의 End-to-End Story로 연결됨.
9. **Fan 360 컴포넌트 통합·리디자인(팀원 7 LWC + 디자인 시스템)** → 은영이 만든
   부품들을 브랜드 일관성 있는 하나의 Customer 360 화면으로 완성 → 발표 가능한 상태.
10. **A~K Technical Decision 회의 준비·진행 + Demo 재편** → Wireframe 개념을 실제
    Salesforce 구현(Lead/Quote/Campaign RT/Agentforce)으로 확정, 발표 범위를 2장면으로
    압축 → 팀 4명이 각자 B2B Pipeline 구간을 구현할 수 있는 명확한 기준.

---

# Current State

| Feature | Sara Role | Contribution | Git Main | Org | QA | Status |
|---|---|---|---|---|---|---|
| Project Story / Business Goal / Persona | PM / Product | G·F | ✅ | — | — | COMPLETE |
| 5 Domain Model / Object Mapping / 3축 | Solution Architect | F·G | ✅ | ✅(승우 구축) | ✅ | COMPLETE |
| Phase 2 B2B Architecture Draft (§7) | Solution Architect | F | ✅ | 부분 | — | COMPLETE(설계) |
| Fan 360 Landing 대시보드 (`fan360Landing`) | Feature Owner / Dev | A·F | ✅ | ✅ | ✅ | COMPLETE |
| Fan List 커스텀 화면 (Apex + LWC 5) | Feature Owner / Dev | A·F·E | ✅ | ✅ | 정상 | COMPLETE |
| Recommendation Segment Dashboard | Feature Owner / Dev | A·F | ✅ | ✅ | 정상 | COMPLETE |
| 팀원 Fan 360 LWC 7종 통합·리디자인 | Integration / Design | C·D·F | ✅ | ✅ | 정상 | COMPLETE |
| Engagement/Value Calc + Order/Admission Flow 체인 | Feature Owner / Dev | A (개념 H) | ✅ | ✅ | Pilot 검증 | COMPLETE |
| Recommendation Review Sidebar (Apex + LWC) | Feature Owner / Dev | A·F·E | ✅ | ✅ | 발송 검증 | COMPLETE |
| 개인화 메시지 Flow + Prompt Template | Feature Owner / Dev | A·D | ✅ | ✅ | 정상 | COMPLETE |
| VIP Candidate 감지 Flow | Solution Architect | C·B·E | ✅ | ✅ | Pilot 검증 | COMPLETE |
| Fan Insight 화면 방식 결정 (Report/Dashboard) | Feature Owner | G·F | ✅ | — | — | COMPLETE(결정)/Report 구성 PARTIAL |
| Fan Insight → 광고 가치 발견 논리 | Solution Architect / Product | F·G | ✅ | — | — | COMPLETE(설계) |
| Fan Insight Slack Alert Flow | Feature Owner / Dev | A | ✅ | ✅ | — | COMPLETE |
| Target Segment Picklist (D-018-G) | Feature Owner | G·H | ✅ | — | — | PARTIAL(값 목록 TBD) |
| B2C↔B2B 연결 흐름 설계·조율 | Feature Owner / SA | F·G·D | ✅ | — | — | COMPLETE(설계·조율) |
| DART Open API Primary Source 확정 (D-020) | Solution Architect / PM | G·F | ✅ | — | — | COMPLETE / 연동방식 TBD |
| 공용 Dummy Data 규칙 (DEMO_DATA_STANDARD) | PM / SA | G·F | ✅ | — | — | COMPLETE |
| P2 Dummy Data Master (30명 + d'Alba) | Feature Owner / Product | A·F | ✅ | 부분 | — | COMPLETE(설계) |
| 60명 Pilot Cohort 생성·검증·Backfill | Feature Owner / Dev / QA | A·E | 브랜치 | ✅ | ✅ | COMPLETE |
| 5,000명 Target Scale + 분포 QA 기준 | PM / QA | G·E | ✅ | 헤드카운트 ✅ | 분포 미검증 | PARTIAL |
| Phase 1 4화면 UX 설계 | Product Designer | F·B | ✅ | ✅(혜준/은영 구현) | — | COMPLETE |
| 디자인 시스템 (브랜드 컬러·CSS·`icon`) | Product Designer / Dev | A·F | ✅ | ✅ | — | COMPLETE |
| 발표 참여 Event UX (EVENT_SPEC) | Feature Owner / Product | F·G | ✅ | — | — | COMPLETE |
| VIP Recommendation Agent (Agent Script + Invocable Apex 3) | Feature Owner / Dev / SA | A·F·E | ✅ | ✅ publish | E2E + 이메일 검증 | COMPLETE (계정 권한·`ko` 잔여) |
| Agent 아키텍처 표준 (D-035) | Solution Architect | F·G | ✅ | — | — | COMPLETE |
| Agentforce 범위 예외 승인 (D-017) | PM | G·H | ✅ | — | — | COMPLETE |
| Demo 시나리오 재작성 (04_DEMO) | PM / Product | G·F | ✅ | — | — | COMPLETE |
| Live Fan Quiz (Object + Apex 2 + LWC 2 + Flow) | Feature Owner / Dev | A·F | ✅ | ✅ | 정상 | COMPLETE |
| 이메일 발송 인프라 검증 (D-025) | QA / SA | E·G | ✅ | ✅ | Naver 검증 | COMPLETE |
| Campaign Hub 조사 + Benefits 필드 (D-029·030) | Solution Architect / QA | E·F·G | ✅ | 필드만 ✅ | — | PARTIAL(로직 보류) |
| 팀 개발 결과 검수·Integration (은영/승우 PR) | PM / Feature Owner | E·D·H | ✅ | ✅ | — | COMPLETE |
| Source of Truth 문서 6종 + 부속 | PM / SA / Product | Documentation | ✅ | — | — | COMPLETE |
| Org 검수 리포트 + 메타 스냅샷 | Solution Architect / PM | E·F | ✅ | 읽기전용 | — | COMPLETE |
| A~K Technical Decision 회의 준비·진행 | PM / SA | G·F·H | ✅ | — | — | COMPLETE (K는 On Hold) |
| 30+ Major Decisions 조정·기록 (05_DECISIONS) | PM | G·Documentation | ✅ | — | — | COMPLETE |
| Troubleshooting 체크리스트 12항목 (CLAUDE.md §11) | QA / SA | E | ✅ | — | — | COMPLETE |

---

# Ownership 확인 필요 (Evidence 부족 / 경계 불명확)

| 항목 | 확인 필요 이유 |
|---|---|
| `Fan_Engagement_Calc` / `Fan_Value_Calc` / `Order_Paid` / `Admission_Created` 등 계산 체인 | 현재 Org `CreatedBy = Sara Bang`이지만, Phase 1 03_SYSTEM은 승우가 Flow를 구축했다고 서술. 3축 **개념 설계**는 팀 공동(Decision 002~004, Sara 주도). D-032(2026-08-28) 이후 Org 재구축 과정에서 Sara가 재생성했을 가능성 — 개념 설계(팀)와 현재 구현 소유(Sara)를 분리 기록함 |
| Phase 1 4화면(Fan 360 Dashboard / Profile / Timeline / Recommendation Panel) 최초 구현 | 02_TEAM_GUIDE는 혜준(Lightning Page/QA)·은영(LWC) 구현으로 기재. 현재 Org의 `fan360Landing` 등은 Sara 소유 — Phase 1 원본과 Phase 2 재구축본의 관계 미확인 |
| `03_SYSTEM.md` §4 Flow 목록의 Phase 1 원저자 | CA-FRM 재구성본은 "세션 기록 기반 초안"이라 명시. CloudAlpacas repo의 Flow 메타데이터가 git에 미포함 — Org `CreatedBy`만으로 판단 |
| 5,024건 기존 Fan Account | 과거 테스트용으로 생성·삭제됐다가 다시 존재하는 데이터. 누가 생성했는지, P2_DUMMY_DATA_MASTER 30명과 같은 레코드인지 미확인 |
| Chanyeon Kim의 Org 작업(c360_*, SDO_Service_*) | 팀원 매핑 불명확. Service Cloud 영역이라 Sara 범위 밖 — 발표 제외 범위(D-031)와 일치 |
| `FanDetailController` / `GameDetailController` / `ReportController` (+ Test) | force-app에 존재하나 Org `CreatedBy` 이 조사에서 미확인 — 은영의 Phase 1 Apex(PR #42)일 가능성 높음 |

---

> **문서 생성**: 2026-09-01. Evidence = Salesforce Org `CloudAlpacasProd`(읽기 전용
> Tooling API), GitHub `CellsOrg/cloud-alpacas-agent` + `CellsOrg/CloudAlpacas`
> git history, 프로젝트 MD 문서 전체. 추측한 항목은 "Ownership 확인 필요"에 분리.
