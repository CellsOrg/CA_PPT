# Cloud Alpacas — ORG Metadata Inventory (검증본)

> **Purpose:** 현재 Salesforce Org에 **실제로 존재하는** Cloud Alpacas 관련 Metadata의 실사 기록.
> **Source:** 2026-08-31, `cloud-alpacas` org (`00Dbm00000tkYqDEAU`, Enterprise, Production, API 62–67) 직접 조회.
> **Method:** Tooling API(`CustomObject`/`CustomField`/`Flow`/`ApexClass`/`ApexTrigger`/`LightningComponentBundle`/`GenAiPlannerDefinition`) + `sf sobject describe` + `sf project retrieve`.
> **분류 기준:** `CreatedBy` / `LastModifiedBy` ∈ 팀원, `NamespacePrefix = null`, 데모 접두사(`SDO_`/`xDO_`/`CGC_`/`DBM_` 등) 제외.
> **원칙:** 문서에 있다고 Org에 있다고 가정하지 않는다. Org에 있다고 현재 Phase 범위라고 가정하지 않는다. 담당자는 `CreatedBy` 기준이며 문서상 역할과 다를 수 있다.
>
> **Rev.2 정정 (2026-08-31, deliverables 재검증):** 아래 "Custom Object 18개" 중 `DART_Setting__c` 는 **Hierarchy Custom Setting** (Object 아님) → 팀 Custom Object **17개** + Custom Setting 1개. `DART_Corp_Mapping__c` 는 field 4개(`Corp_Code__c`/`Corp_Name__c`/`Corp_Name_Eng__c`/`Stock_Code__c`) 보유. 최신 정리는 `deliverables/01_ERD.md`, `deliverables/03_CUSTOM_METADATA.md` 참조.

---

## 0. Org 전체 규모 (컨텍스트)

| 항목 | 수치 | 비고 |
|---|---|---|
| 설치된 관리형 패키지 | 55 | FSL, Salesforce Maps, Pardot, Marketing Cloud, Sales Planning, Slack, Quip, `ssot` 등 |
| CustomObject (전체) | 1,522 | 대부분 패키지 소유 |
| CustomObject (무네임스페이스) | 149 | 이 중 **팀 제작 18개**, 나머지 131개는 SDO/QBrix 데모 스캐폴딩 |
| CustomField (전체) | 35,193 | — |
| ApexClass (전체) | 2,623 | 팀 제작 **100개** |
| ApexTrigger (전체) | 214 | 팀 제작 **1개** |
| Flow (Active 버전) | 308 | 팀 제작 Active **40개** |
| LWC (전체) | 491 | 팀 제작 **46개** |
| Agentforce Planner (GenAiPlannerDefinition) | 38 | 팀 제작 에이전트 **5종** (버전 누적 34개) |

> 이 org는 Salesforce 데모/SDO 조립형 org다. "실제 구현"은 팀원(Sara / Eunyeong / Hyejune / Aaron / Rafael Espada) 이 2026-08-11 ~ 08-31 사이에 만든 위 소계에 해당한다.
> **팀원 User 매핑:** Sara Bang(`sara6ang`), Eunyeong Doh(`dohrphin`), Hyejune Jo(`hyejunejo`), Aaron Choi(`counselor_aaron`), **Rafael Espada(`wjdtmddn5390` = Seungwoo)**, Seongbin An(08-24 추가, metadata 제작 이력 없음).

---

## 1. Custom Object (팀 제작, 18개)

| # | API Name | Label | Created | LastModified | 관계 요약 |
|---|---|---|---|---|---|
| 1 | `Season__c` | Season | Rafael 08-12 | Rafael 08-12 | (부모) → `Game__c`(MD), `Fan_Activity_Pattern__c`(L) |
| 2 | `Game__c` | Game | Rafael 08-11 | Hyejune 08-13 | → `Season__c`(MD 자식) · (참조됨) `Admission__c`, `Order` |
| 3 | `Admission__c` | Admission | Rafael 08-12 | Rafael 08-12 | → `Attendance_Record__c`(MD), `Fan__c`→Account(L), `Game__c`(L), `Order_Item__c`→OrderItem(L) |
| 4 | `Attendance_Record__c` | Attendance Record | Rafael 08-11 | Rafael 08-12 | (부모) → `Admission__c`(MD) · `Fan__c`→Account(L) · Roll-Up(Total/First/Last Admission) |
| 5 | `Engagement_Signal__c` | Engagement Signal | Rafael 08-11 | Rafael 08-13 | `Fan__c`→Account(L), `Player__c`→Contact(L) |
| 6 | `Fan_Activity_Pattern__c` | Fan Activity Pattern | Rafael 08-12 | Rafael 08-13 | `Fan__c`→Account(L), `Season__c`(L) |
| 7 | `Fan_Segment_History__c` | Fan Segment History | Rafael 08-12 | Rafael 08-13 | `Fan__c`→Account(L) |
| 8 | `Recommendations__c` | **Fan Recommendation** | Rafael 08-12 | **Sara 08-25** | `Fan__c`→Account(L), `Campaign__c`→Campaign(L) · (참조됨) `Benefits__c` |
| 9 | `Benefits__c` | Benefits | Rafael 08-12 | Rafael 08-13 | `Fan__c`→Account(L), `Recommendations__c`(L) |
| 10 | `Notification_Log__c` | Notification Log | Rafael 08-12 | Rafael 08-13 | `Fan__c`→Account(L), `Campaign__c`→Campaign(L) |
| 11 | `Quiz_Entry__c` | Quiz Entry | Sara 08-29 | Sara 08-29 | 관계 field 없음 (Experience Site 응모) |
| 12 | `Campaign_Deliverable__c` | Campaign Deliverable | Rafael 08-20 | Rafael 08-24 | `Campaign__c`→Campaign(MD) |
| 13 | `Interaction_Intelligence__c` | Interaction Intelligence | Eunyeong 08-26 | Eunyeong 08-26 | `Opportunity__c`→Opportunity(L) · (부모) → `Interaction_Signal__c`(MD) |
| 14 | `Interaction_Signal__c` | Interaction Signal | Eunyeong 08-26 | Eunyeong 08-26 | `Interaction_Intelligence__c`(MD 자식) |
| 15 | `Sales_Briefing__c` | Sales Briefing | Hyejune 08-27 | Hyejune 08-27 | `User__c`→User(L) |
| 16 | `PRM_Revenue_Target__c` | PRM Revenue Target | Hyejune 08-20 | Hyejune 08-20 | 관계 field 없음 (`Target_Amount__c` 1개) |
| 17 | `DART_Corp_Mapping__c` | DART 기업 매핑 | Aaron 08-28 | Aaron 08-28 | 커스텀 field 0개 (표준 field만) — Account와 논리적 매핑 |
| 18 | `DART_Setting__c` | DART 설정 | Aaron 08-28 | Aaron 08-28 | `Api_Key__c` 1개 (DART OpenAPI 키 저장) |

### 1.1 Custom Object 핵심 Field (describe 기준)

| Object | 핵심 커스텀 Field (관계 제외) |
|---|---|
| `Season__c` | `Start_Date__c`, `End_Date__c`, `Total_Games__c`, `Played_Games__c` |
| `Game__c` | `Game_Date__c`, `Opponent__c`, `Result__c`, `Status__c`, `Home_Away__c`, `External_ID__c` |
| `Admission__c` | `Admission_Time__c`, `Gate__c`, `External_ID__c` |
| `Attendance_Record__c` | `Total_Admissions__c`, `First_Admission_Date__c`, `Last_Admission_Date__c`, `External_ID__c` |
| `Engagement_Signal__c` | `Signal_Type__c`, `Source__c`, `Signal_Date__c`, `External_ID__c` |
| `Fan_Activity_Pattern__c` | `Games_Attended__c`, `Attendance_Rate__c`, `Goods_Purchases__c`, `Total_Spend__c`, `Analyzed_Date__c` |
| `Fan_Segment_History__c` | `Segment__c`, `Changed_Date__c`, `Reason__c`, `External_ID__c` |
| `Recommendations__c` | `Recommended_Action__c`, `Status__c`, `Reason__c`, `Personalized_Message__c`, `Sent_Date__c`, `External_ID__c` |
| `Benefits__c` | `Benefit_Type__c`, `Status__c`, `Issued_Date__c`, `Used_Date__c`, `Expiration_Date__c`, `Discount_Rate__c`, `Min_Purchase_Amount__c`, `Badge_Label__c` |
| `Notification_Log__c` | `Channel__c`, `Content__c`, `Sent_Date__c`, `External_ID__c` |
| `Quiz_Entry__c` | `Entrant_Name__c`, `Selected_Answer__c`, `Is_Correct__c`, `Is_Winner__c` |
| `Campaign_Deliverable__c` | `Status__c`, `Weight__c`, `Due_Date__c`, `Completed_Date__c`, `Evidence_URL__c`, `Blocked_Reason__c`, `Due_Date_Pushed__c`, `Pending_Slack_Message__c` |
| `Interaction_Intelligence__c` | `Summary__c`, `Key_Decision__c`, `Concerns_Objections__c`, `Customer_Reaction__c`, `Follow_Up__c`, `Source_Type__c`, `Source_Record_Id__c` |
| `Interaction_Signal__c` | `Signal_Category__c`, `Signal_Type__c`, `Direction__c`, `Confidence__c`, `Evidence__c` |
| `Sales_Briefing__c` | `Briefing_Date__c`, `Briefing_Key__c`, `Briefing_Text__c` |
| `DART_Corp_Mapping__c` | (커스텀 field 없음 — Name/표준 field로 운용) |

---

## 2. Standard Object — 팀이 추가한 Custom Field

> `_del__c`, `_tc__*`, `ZZ_Diag*`, `CA_Diag*` 는 폐기/테스트 잔재로 **제외 표기**.

### 2.1 Account — 37개 (Rafael 11, Aaron 20, Sara 6)
- **Fan(B2C) — Rafael:** `Acquisition_Channel__c`, `Current_Segment__c`, `Engagement_Level__c`, `Engagement_Score__c`, `Fan_Value_Tier__c`, `Favorite_Player__c`(→Contact L), `Email_Opt_In__c`, `SMS_Opt_In__c`, `Kakao_Opt_In__c`, `Push_Opt_In__c`, `Consent_Updated_Date__c`, `Segment_Updated_Date__c`
- **Fan(B2C) — Sara:** `Age_Group_c__c`(Formula), `Report_Gender__c`(Formula), `Fan_Join_Date__c`, `Registration_Date__c`, `Membership_Status__c`
- **B2B/스폰서·DART — Aaron:** `Business_Reg_No__c`, `Corp_Name_Eng__c`, `Stock_Code__c`, `Proposed_Corp_Name__c`, `Proposed_Stock_Code__c`, `Market_Type__c`, `Operating_Profit__c`, `Total_Assets__c`, `DART_Match_Status__c`, `DART_Enriched_At__c`, `Match_Confidence__c`, `Match_Rationale__c`, `Sponsor_Tier__c`, `SDO_Partner_Tier__c`, `Total_Sponsorship_Value__c`, `Sponsorship_Opportunity_Count__c`, `Latest_Open_Opportunity_Amount__c`, `Latest_Open_Opportunity_Stage__c`, `Latest_Open_Opportunity_Next_Step__c`
- **Hyejune:** `Lead_Qualification_Score__c`

### 2.2 Contact — 5개
- **Rafael:** `Position__c`, `Uniform_Number__c` (Player)
- **Sara:** `Name_EN__c`
- **Aaron:** `SDO_PRM_Region__c`, `SDO_PRM_Service_Delivery__c`

### 2.3 Lead — 18개 (전부 Hyejune)
`Lead_Score__c`, `Final_Lead_Score__c`, `Score_Industry__c`, `Score_Interest__c`, `Score_LeadSource__c`, `Score_Region__c`, `Score_Sponsorship__c`, `Risk_Penalty__c`, `Segment_Match__c`, `Target_Segment__c`, `Regional_Connection__c`, `Competitor_Sponsor__c`, `Controversial_Industry__c`, `Sponsorship_History__c`, `Company_Phone__c`, `Department__c`, `Recommendation_Reason__c`, `AI_Lead_Summary__c`

### 2.4 Opportunity — 41개 (Eunyeong 대부분, Rafael 소수)
- **활성 — Eunyeong:** `Last_Contact_Date__c`, `Last_Contact_Type__c`, `Days_Since_Last_Contact__c`, `Next_Activity_Subject__c`, `Next_Activity_Date__c`, `Open_Tasks_Count__c`, `Overdue_Tasks_Count__c`, `Expected_Benefit_Short_Term__c` / `_Mid_Term__c` / `_Long_Term__c`, `Brand_Fan_Fit__c`, `Client_Budget__c`, `Client_Budget_Status__c`, `Customer_KPI__c`, `Customer_Needs__c`, `Key_Requirements__c`, `Target_Segment__c`, `Target_Start_Season__c`, `Target_Start_Season_Display__c`, `Sponsorship_Interest_Level__c`, `Expected_Timing__c`, `Decision_Maker_Accessible__c`, `Deal_Note__c`, `Contract_Start_Date__c`, `Contract_End_Date__c`, `Primary_Contact_Email__c`, `Primary_Contact_Phone__c`
- **Rafael:** `Partner_Tier__c`
- **제외(폐기/테스트):** `Contact_Role_del__c`, `Contract_Term_del__c`, `Decision_Maker_Name_del__c`, `Expected_Close_Window_del__c`, `Interest_Direction_del__c`, `Partner_Tier_del__c`, `Partnership_Type_del__c`, `Long/Mid/Short_Term_Benefit_del__c`, `_tc__00Nbm*__c` ×3

### 2.5 Order — 9개 (전부 Rafael, 08-12)
`Game__c`(→Game__c L), `Order_Type__c`, `Payment_Status__c`, `Purchase_Channel__c`, `Membership_Status__c`, `Coverage_Start_Date__c`, `Coverage_End_Date__c`, `Refund_Date__c`, `Refund_Reason__c`

### 2.6 OrderItem — 5개 (전부 Rafael, 08-12)
`Current_Owner__c`(→Account L, 양도), `Seat_Number__c`, `Row__c`, `Section__c`, `Transfer_Status__c`

### 2.7 Product2 — 3개 실사용
`Category__c`(Rafael), `Tier__c`(Rafael), `Related_Player__c`(→Contact L, Rafael), `Is_Player_Goods__c`(Sara) — `ZZ_Diag_Test__c`(Sara) 제외

### 2.8 Campaign — 4개 실사용
`Total_Deliverable_Weight__c`(Roll-Up), `Completed_Deliverable_Weight__c`(Roll-Up), `Performance_Summary__c`, — Rafael 08-27. `*_del__c` 4개 제외

### 2.9 Case — 1개
`Related_Order__c`(→Order L, Rafael 08-12)

### 2.10 CampaignMember — 1개
`Is_Converted__c`(Rafael) — `_del*` 2개 제외

### 2.11 PricebookEntry — 1개 실사용
`Max_Discount_Percent__c` / `Max_Discounted_Price__c`(Rafael 08-27) — `_del__c` 3개 제외

### 2.12 Activity(Task/Event) — 6개 실사용 (Eunyeong 08-26)
`Meeting_Type__c`, `Key_Discussion__c`, `Key_Decision__c`, `Concerns_Objections__c`, `Customer_Reaction__c`, `Follow_up__c` — `CA_Diag*_del__c` 3개 제외. *→ Flow `CA Generate Meeting Interaction Intelligence`가 Activity → `Interaction_Intelligence__c` 변환.*

### 2.13 AccountPlan — 14개 (Aaron, 2026-08-31 · 신규)
`Sponsorship_Tier__c`, `Annual_Sponsorship_Value__c`, `Renewal_Date__c`, `Champion_Contact__c`, `Primary_Contact__c`, `Key_Decision_Makers__c`, `Company_Overview__c`, `Our_Positioning__c`, `Potential_Needs__c`, `Exposure_Channels__c`, `Relationship_Strategy__c`, `Resource_Allocation__c`, `Pipeline_Notes__c`, `Action_Plan__c`
> **주의:** 문서에 언급 없음. 당일 생성. 표준 `AccountPlan` Object(Sales 기능) 사용 여부·활성화 상태 팀 확인 필요.

### 2.14 Benefit (표준 Object) — 3개 (Sara 08-28)
`Badge_Label__c`, `Discount_Rate__c`, `Min_Purchase_Amount__c`
> **⚠️ 중복:** 커스텀 `Benefits__c`에도 동일 이름 필드가 존재. 어느 쪽이 실사용인지 확인 필요 (§RECONCILIATION G-2).

---

## 3. Implementation Inventory — Flow (Active 40개)

| 담당 | Flow Label | Type | Trigger | 대상 |
|---|---|---|---|---|
| Sara | Admission Created | AutoLaunched | RecordAfterSave | `Admission__c` |
| Sara | Fan Value Calc | AutoLaunched | — | Account |
| Sara | Start Fan Engagement Calc | AutoLaunched | — | Account |
| Sara | Count_Goods_And_Season | AutoLaunched | — | — |
| Sara | Fan Activity Pattern Admission Update | AutoLaunched | — | `Fan_Activity_Pattern__c` |
| Sara | Order Paid | AutoLaunched | RecordAfterSave? | Order |
| Sara | Order Membership Status Sync | AutoLaunched | — | Order |
| Sara | Start Upsert Flow | AutoLaunched | — | 데이터 적재 |
| Sara | Welcome Campaign Flow -CA | AutoLaunched | — | Campaign |
| Sara | First Visit Guide Flow -CA | AutoLaunched | — | Campaign |
| Sara | First Ticket Campaign Flow -CA | AutoLaunched | — | Campaign |
| Sara | First Merchandise Campaign Flow -CA | AutoLaunched | — | Campaign |
| Sara | Favorite Player Campaign Flow -CA | AutoLaunched | — | Campaign |
| Sara | VIP Candidate Detection Flow -CA | AutoLaunched | — | `Recommendations__c` |
| Sara | Fan Campaign Personalized Msg Flow | AutoLaunched | — | Platform Event `Fan_Campaign_Msg_Request__e` |
| Sara | Generate AI Recommendation Message | AutoLaunched | — | Prompt 연동 |
| Sara | Quiz Entry 정답 자동 판정 | AutoLaunched | — | `Quiz_Entry__c` |
| Sara | EAM Email | Flow (Screen) | — | (08-14, 초기) |
| Eunyeong | CA Update Opportunity Last Contact From Call / Email / Meeting | AutoLaunched | RecordAfterSave | Task/Event |
| Eunyeong | CA Update Opportunity Next Activity | AutoLaunched | RecordAfterSave | Task |
| Eunyeong | CA Update Opportunity Next Activity On Delete | AutoLaunched | RecordBeforeDelete | Task |
| Eunyeong | CA Create Opportunity Activity | AutoLaunched | — | Opportunity |
| Eunyeong | CA Generate Meeting Interaction Intelligence | AutoLaunched | RecordAfterSave | Event → `Interaction_Intelligence__c` |
| Eunyeong | CA Generate Stage Guidance | AutoLaunched | — | Opportunity |
| Rafael | Campaign 예상 매출 계산 / 동기화 / 동기화(Opportunity 삭제 시) | AutoLaunched | — | Campaign / Opportunity |
| Rafael | 갱신 캠페인 성과 요약 자동 생성 | AutoLaunched | — | Campaign (RT=Sponsorship_Renewal) |
| Rafael | Campaign Deliverable Blocked Slack Alert | AutoLaunched | RecordAfterSave | `Campaign_Deliverable__c` |
| Rafael | Campaign Deliverable Detect Due Date Push | AutoLaunched | RecordBeforeSave | `Campaign_Deliverable__c` |
| Aaron | DART Lead 전환 AI매칭 | AutoLaunched | — | Lead |
| Aaron | DART 승인 보강 | AutoLaunched | — | Account |
| Aaron | Rollup Sponsorship To Account / On Delete | AutoLaunched | — | Opportunity → Account |
| Aaron | Sync Account Latest Open Opportunity | AutoLaunched | — | Opportunity → Account |
| Hyejune | 계약서 생성 Flow | AutoLaunched | — | Opportunity |
| Hyejune | 고득점 리드 연락 Flow | AutoLaunched | — | Lead |
| Hyejune | 협상 후속 연락 Flow | AutoLaunched | — | Opportunity |

> 전체 Active Flow 308개 중 268개는 데모/패키지 소유(비팀). 위 40개만 CA 구현.

---

## 4. Implementation Inventory — Apex (100 클래스, 1 트리거)

### 4.1 도메인별 Apex Class (Test 클래스 포함)

| 도메인 | 담당 | 주요 클래스 |
|---|---|---|
| Fan 360 / Fan List | Sara, Eunyeong | `Fan360Controller`, `Fan360LandingController`, `FanDetailController`, `FanListController`, `GameDetailController`, `ReportController`, `CampaignController` |
| Fan Segmentation | Eunyeong | `SegmentDecliningVisits`, `SegmentMembershipCompleted`, `SegmentNoGoodsLoyal`, `SegmentNoVisitAfterSignup`, `SegmentFanListItem` |
| Recommendation / VIP | Sara | `RecommendationSegmentController`, `RecommendationReviewController`, `RecommendationActionLabels`, `ApproveRecommendationAction`, `SendRecommendationEmailAction`, `GetPendingVipRecommendationsAction` |
| Quiz / Experience Site | Sara | `QuizEntrySubmitController`, `LiveFanQuizRevealController`, `LightningSelfRegisterController`, `LightningLoginFormController`, `LightningForgotPasswordController` |
| Interaction Intelligence (Opp Agent) | Eunyeong | `ActivityIntelligenceController`, `ActivityIntelligenceAgentAction`, `InteractionIntelligenceParser`, `ConversationHistoryAgentAction` |
| Opportunity Agent / Stage Guidance | Eunyeong | `OpportunityAgentChatController`, `OpportunityStageGuidance`, `StageGuidanceController`, `DealContext`, `FindSimilarClosedDeals`, `FindActivityAttendee` |
| Negotiation | Aaron(생성)→Eunyeong(수정) | `NegotiationContext`, `NegotiationContextController`, `NegotiationTermsUpdater`, `NegotiationOpportunityLookup` |
| Sponsorship Proposal | Rafael(생성)→Eunyeong(수정) | `OpportunityProposalContext`, `SponsorshipPackageLookup`, `SponsorshipProposalSaver`, `FindSponsorshipPackage` |
| Campaign Agent (스폰서십) | Rafael | `CampaignAgentChatController`, `CampaignBottleneckFinder`, `CampaignMitigationRecorder`, `RenewalSummaryRefresher` |
| DART 연동 (Lead AI 매칭) | Aaron | `DartService`, `DartMatchService`, `DartEnrichmentInvocable`, `DartEnrichmentQueueable`, `DartMatchInvocable`, `DartMatchQueueable`, `DartHttpMock` |
| PRM / Lead AI (파트너 포털) | Hyejune | `PRM360Controller`, `PRM360SummaryController`, `PRM360SalesBriefingScheduler`, `LeadAiSummaryController`, `CheckWeather`, `WeatherService`, `CurrentDate` |
| Partnership Inquiry (Experience) | Eunyeong | `PartnershipInquiryController` |
| 공용 | Hyejune | `TestDataFactory` |

### 4.2 Apex Trigger (1개)

| Trigger | Object | Status | 담당 |
|---|---|---|---|
| `LeadConvertPartnerContact` | Lead | Active | Aaron |

> **관찰:** 자동화는 거의 전부 **Flow 중심**(40개). Trigger는 Lead 전환 보조 1개뿐. 나머지 Apex는 LWC Controller / Agent Action / Invocable.

---

## 5. Implementation Inventory — LWC (46개)

| 화면 그룹 | 담당 | 컴포넌트 |
|---|---|---|
| Fan 360 Landing / List | Sara | `fan360Landing`, `fanList`, `fanListTable`, `fanListKpiCards`, `fanListSearchFilter`, `fanDetailDrawer`, `icon` |
| Fan 360 Summary / Timeline | Eunyeong→Sara | `fan360Summary`, `fanSummary`, `fanTimeline`, `fanRecommendedActions`, `gameDetail` |
| Recommendation / Segment | Sara, Eunyeong | `recommendationReviewPanel`, `recommendationSegmentDashboard`, `recommendationDashboard`, `segmentFanList`, `segmentOpportunities` |
| Campaign | Eunyeong→Sara, Rafael | `campaignBoard`, `campaignAgentChat`, `campaignAgentChatModal` |
| Quiz (Experience Site) | Sara | `liveFanQuizEntry`, `liveFanQuizReveal` |
| Report | Eunyeong→Sara | `reportDashboard` |
| Opportunity Agent / Activity | Eunyeong | `opportunityAgentChat`, `opportunityAgentChatModal`, `opportunityStageGuidance`, `stageGuidance`, `stageProgress`, `activityIntelligence`, `activityOverview`, `activityTimeline`, `negotiationContextSummary` |
| Partnership Inquiry | Eunyeong | `partnershipInquiry` |
| PRM 파트너 포털 | Hyejune | `prm360RevenueSummary`, `prmClosingSoonOpportunities`, `prmHighPotentialLeads`, `prmKeyOpportunities`, `prmMyTasks`, `prmOpenSponsorshipPipeline`, `prmQuickLinks`, `prmSalesBriefing`, `prmSeasonClosedWonRevenue`, `prmSeasonTargetAttainment`, `prmTodaysEvents`, `prmYoyRevenue`, `leadAiSummaryCard` |

---

## 6. Implementation Inventory — Agentforce (5종, GenAiPlannerDefinition)

| Agent (MasterLabel) | 담당 | 버전 수 | 관련 Plugin(Topic) | 관련 Apex |
|---|---|---|---|---|
| **VIP Recommendation Agent** | Sara | v1–v2 | `vip_recommendations_*` | `GetPendingVipRecommendationsAction`, `ApproveRecommendationAction`, `SendRecommendationEmailAction` |
| **Opportunity Agent** | Eunyeong | **v1–v23** | `agent_router`, `activity_management`, `deal`, `proposal`, `negotiation`, `stage_guidance`, `escalation`, `off_topic`, `ambiguous_question` (버전마다 재생성) | `OpportunityAgentChatController`, `DealContext`, `OpportunityStageGuidance`, `ActivityIntelligenceAgentAction`, `ConversationHistoryAgentAction`, `FindSimilarClosedDeals` … |
| **Negotiation Assistant** | Aaron | v1–v2 | `negotiation_*`, `proposal_quote_*` | `NegotiationContext`, `NegotiationTermsUpdater`, `NegotiationOpportunityLookup` |
| **Sponsorship Proposal Assistant** | Aaron | v1 | `proposal_*` | `OpportunityProposalContext`, `SponsorshipPackageLookup`, `SponsorshipProposalSaver` |
| **스폰서십 캠페인 에이전트 (Sponsorship Campaign Agent)** | Rafael | v1 | `bottleneck_monitor_*`, `renewal_report_*`, `agent_router_*` | `CampaignAgentChatController`, `CampaignBottleneckFinder`, `RenewalSummaryRefresher` |

> **비팀(데모/OOTB) Planner:** `EmployeeCopilotPlanner`, `SearchAgent`, `DataQnAAgent`, `SDO_Service_Agentforce_Service_Agent/Assistant`, `SDO_Agentforce_Employee_Agent`, `Campaign_Agent_v1`, `AnalyticsAgentAutoSDM`, `AnalyticsAgentConcierge` — 생성자 `Chanyeon Kim` / `Automated Process`.
> **Prompt Template:** `CA_PRM360_Sales_Briefing`, `CA_Lead_AI_Summary`, `CA Stage Guidance Recommendation`, Fan Personalized Message 등 — GenAiPromptTemplate 상세는 다음 retrieve 대상.
> **주의:** `BotDefinition` 조회는 이 org에서 실패 → 에이전트는 구형 `Bot`이 아니라 신형 `GenAiPlanner` 모델. Opportunity Agent v1–v23은 반복 재배포 흔적으로, **활성 버전 1개만 유효**(GenAiPlannerBundle 확인 필요).

---

## 7. Verification / Gap (다음 단계)

| # | 확인할 것 | 방법 |
|---|---|---|
| 1 | `Recommendation__c`(단수) phantom row 정리 | Setup > Object Manager에서 Draft 여부 확인, 삭제 |
| 2 | `User__c` phantom row 정리 | 동일 |
| 3 | `Benefit`(표준) vs `Benefits__c`(커스텀) 중복 필드 | 레코드 수 조회, 실사용 확인 |
| 4 | Opportunity Agent 활성 버전 | `GenAiPlannerBundle` / `BotVersion` 조회 |
| 5 | `PRM_Revenue_Target__c` 관계 미구현 | Season/User FK 필요 여부 팀 결정 |
| 6 | `AccountPlan` 표준 Object 활성화 상태 | Setup > Account Plan, Sales 기능 확인 |
| 7 | `_del__c` / `_tc__*` / `ZZ_Diag*` / `CA_Diag*` 폐기 필드 | 배포 전 정리 대상 목록화 |
| 8 | GenAiPromptTemplate 전체 | `sf project retrieve -m GenAiPromptTemplate` |
| 9 | Experience Site (FanQuiz, Partnership) 구성 | `sf project retrieve -m ExperienceBundle` |
| 10 | Person Account 여부 / Fan RecordType 분포 | `SELECT RecordType.Name, COUNT(Id) FROM Account GROUP BY` |

### Source of Truth Priority
```
현재 Salesforce Org Metadata
        ↓
ORG_METADATA_INVENTORY.md  (이 문서 · 검증본)
        ↓
ERD_OBJECT_LIST.md
        ↓
DOC_RECONCILIATION.md  (기존 문서와의 차이)
        ↓
03_SYSTEM.md / 01_PROJECT.md / 05_DECISIONS.md 정합성 검수
```
