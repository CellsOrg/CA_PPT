# 04. 프로세스 흐름도 — 최종 제출용 다이어그램

`04_PROCESS_FLOW.md` 를 기반으로 만든 **PPT/문서 삽입용 프로세스 다이어그램** 6종.

- 형식: SVG(벡터, 무손실 확대) + PNG(3840×2160, 16:9)
- 재생성: `python3 _generator.py` (표준 라이브러리만 사용, 네트워크 불필요)
- 내용 출처: `../04_PROCESS_FLOW.md` — MD에 없는 기능은 추가하지 않음

## 파일 목록

| 파일 | 프로세스 | 관점 |
|---|---|---|
| `P1_Fan_Data_Process_AsIs.svg` / `.png` | P1 Fan 가입 → 데이터 축적 → Segment/Engagement | As-Is |
| `P1_Fan_Data_Process_ToBe.svg` / `.png` | P1 | To-Be |
| `P2_Recommendation_Process_AsIs.svg` / `.png` | P2 Fan 분석 → Recommendation → Campaign/Action | As-Is |
| `P2_Recommendation_Process_ToBe.svg` / `.png` | P2 (핵심) | To-Be |
| `P3_Sponsorship_Process_AsIs.svg` / `.png` | P3 Sponsor 후보 → Fit → Lead → Opportunity → Sponsorship | As-Is |
| `P3_Sponsorship_Process_ToBe.svg` / `.png` | P3 (핵심) | To-Be |

PNG은 `png/` 폴더.

## 공통 시각 언어 (Cloud Alpacas)

| 요소 | 의미 |
|---|---|
| **네이비 카드 + 실선 화살표** | 사람이 하는 일반 업무 흐름 |
| **연한 파랑 카드 (OBJECT)** | 실제 Salesforce 레코드 — 제안·혜택·알림·딜이 전부 레코드로 남음 |
| **주황 테두리 카드 (FLOW / APEX) + 주황 화살표** | Flow·Apex 자동 실행 구간 = "여기서 자동화가 일어난다" |
| **주황 배경 카드 (AGENTFORCE / PROMPT)** | Agent·Prompt가 판단·생성하는 구간 = "여기서 AI가 개입한다" |
| **네이비 테두리 + '사람 판단·실행' 태그** | 사람이 검토·승인·판단하는 구간 (Human-in-the-loop) |
| **주황 마름모** | 자동 분기 판정 (세그먼트 조건 / VIP 후보 / Lead Score 임계) |
| **회색 점선** | 알림 · handoff (Fan Timeline, Slack, 캠페인 편성 등) |
| **빨강 카드 (As-Is)** | 분산·수기·감(感)으로 생기는 문제 지점 |
| **상단 페이즈 리본** | 프로세스 단계. 주황 강조 = 자동화/AI가 가치를 만드는 단계 |

메타데이터 이름(Flow/Apex/Prompt/LWC)은 카드 안 작은 보조 텍스트로만 표기해 메인 흐름과 계층 분리.

---

## 각 다이어그램의 의도 · 시각화 대상 · 확인 필요 항목

### P1 — Fan 데이터 프로세스

**As-Is 의도**: "데이터가 채널마다 흩어지고 등급이 수기·주관적"이라는 문제를 한눈에.
- 시각화: MD P1 As-Is 문단 — 티켓/입장/굿즈/SNS가 별도 시스템, 담당자가 엑셀로 취합, 감으로 등급 부여, "몇 번(횟수) vs 언제(시점)" 미분리.

**To-Be 의도**: 이벤트 → Flow 자동 집계 → 등급·세그먼트 산출의 자동 파이프라인.
- 시각화: MD P1 To-Be Mermaid + 자동화 매핑 표 전체.
- 실제 Metadata 연결:
  - `Start Upsert Flow` (Fan App → Account upsert, `External_ID__c`)
  - `Order Paid` → `Order + OrderItem`
  - `Admission Created` → `Attendance_Record__c` MD Roll-Up (`Total_Admissions__c`, `First/Last_Admission_Date__c` — 횟수/시점 분리 포인트)
  - `Fan Activity Pattern Admission Update`, `Count_Goods_And_Season` → `Fan_Activity_Pattern__c`
  - `Fan Value Calc` / `Start Fan Engagement Calc` → `Account.Current_Segment__c / Fan_Value_Tier__c / Engagement_Score__c`
  - `Fan_Segment_History__c` (세그먼트 이동 이력)
- 사람 확인 필요:
  - Fan App ↔ Salesforce 연동 방식(REST 추정, `04_PROCESS_FLOW.md` §5) — 다이어그램은 "이벤트 → Salesforce 전달"로 단순화.
  - 세그먼트 조건 분기(`세그먼트 조건 충족?`)의 실제 entry criteria는 Flow Builder 확인 필요.

### P2 — Recommendation 프로세스 (핵심)

**As-Is 의도**: "누구에게 뭘 줄지 감에 의존 + 약속한 혜택에 실체 없음(신뢰 문제)".
- 시각화: MD P2 As-Is 문단.

**To-Be 의도**: 데이터 → **AI 추천** → **매니저 검토·승인(사람 판단)** → **개인화 실행** → **알림·이력** 이 한 줄로 이어지고, 제안·혜택·알림이 모두 레코드로 추적됨.
- 페이즈 리본이 곧 핵심 메시지: `Fan Data → VIP 후보 감지 → 추천·메시지 생성(AI) → 매니저 검토·승인 → 개인화 실행 → 알림·이력`.
- 시각화: MD P2 To-Be Mermaid + 자동화 매핑 표.
- 실제 Metadata 연결:
  - `VIP Candidate Detection Flow -CA` → `Recommendations__c (Status=Pending)`
  - `VIP_Recommendation_Agent` + `GetPendingVipRecommendationsAction` (추천 액션 판단)
  - `Generate AI Recommendation Message` Flow + Prompt `Fan_Personalized_Message` (개인화 메시지 생성)
  - `recommendationReviewPanel` / `recommendationSegmentDashboard` LWC (매니저 검토 화면)
  - `ApproveRecommendationAction` / `SendRecommendationEmailAction` Apex (승인·발송)
  - `Benefits__c` (Status/Used_Date — 실제 혜택 레코드), `Fan_Campaign` Flow 군 + `Fan_Campaign_Msg_Request__e`
  - `Notification_Log__c` (Fan Timeline)
- 사람 확인 필요:
  - `VIP_Recommendation_Agent` 활성 버전(v1–v2 중) — 다이어그램은 버전 미표기.
  - Platform Event `Fan_Campaign_Msg_Request__e` 구독 Flow 경로는 캠페인 편성 handoff로만 축약.

### P3 — Sponsorship 프로세스 (핵심)

**As-Is 의도**: "엑셀 후보 수집 + 팬덤 적합도와 계약 가능성 미분리 + 미팅 메모 분산".
- 시각화: MD P3 As-Is 문단.

**To-Be 의도**: `External Data(DART) → 매칭·Lead Score → Opportunity → Agent 제안·협상(AI) → Sponsorship → PRM 포털` 로 외부 데이터부터 파트너 포털까지 연결. 사람(파트너 담당자)은 후보 선정·미팅·협상 판단에만 개입.
- 시각화: MD P3 To-Be Mermaid + 자동화 매핑 표.
- 실제 Metadata 연결:
  - `DartService` / `DartMatchService` / `DartEnrichmentQueueable`, RemoteSite `opendart_fss`, `DART_Setting__c` → `DART_Corp_Mapping__c`
  - `DART 승인 보강` Flow → `Account(Business).DART_* / Match_Confidence__c`
  - Lead Score 18필드(`Final_Lead_Score__c`, `Segment_Match__c` …) + `LeadConvertPartnerContact` trigger
  - Prompt `CA_Lead_AI_Summary` → `Lead.AI_Lead_Summary__c`
  - `DART Lead 전환 AI매칭` Flow → `Opportunity`
  - `Opportunity_Agent` (deal/proposal/negotiation/stage_guidance) + `SponsorshipProposalSaver` / `NegotiationTermsUpdater`
  - `CA Generate Meeting Interaction Intelligence` Flow + Prompt `CA_Offline_Meeting_*` → `Interaction_Intelligence__c` → `Interaction_Signal__c`
  - `Campaign_Deliverable__c` + `Campaign Deliverable Blocked Slack Alert` (이행 지연 → Slack)
  - `Rollup Sponsorship To Account` → `Account.Total_Sponsorship_Value__c` 등
  - `prm*` LWC 13종 + Prompt `CA_PRM360_Sales_Briefing` + `Sales_Briefing__c` (PRM 포털)
- 사람 확인 필요:
  - `Opportunity_Agent` 활성 버전(v1–v23 중 1개, 미확정) — 다이어그램은 버전 미표기.
  - Slack 채널 ID(`04_DEMO.md` 기재값) 미검증.
  - `고득점 리드 연락` / `협상 후속 연락` / `계약서 생성` Flow는 "고득점 리드 연락" handoff 하나로 축약 — 실제 3개 Flow.
  - Lead Score 임계값, DART 매칭 신뢰도 임계값은 Flow/필드 설정 확인 필요.

---

## 공통 주의

- Flow 트리거 조건·분기는 **프로세스 관점으로 단순화**했습니다. 정확한 entry criteria는 Flow Builder에서 확인하세요 (`04_PROCESS_FLOW.md` §5).
- `doesRequireRecordChangedToMeetCriteria=true` Flow는 과거 데이터 소급 적용 안 됨 — "예상 수치 vs 실제 수치" 대조 필요 (프로젝트 CLAUDE.md §11).
- 다이어그램 텍스트를 수정하려면 `_generator.py` 의 해당 `Node(...)` / `Edge(...)` 만 고치고 재실행하세요. 좌표·라우팅은 자동 계산됩니다.
