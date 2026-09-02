# 02. 권한 설정 현황표 — Cloud Alpacas

## Scope
- 권한 표기: `C`reate / `R`ead / `U`pdate(Edit) / `D`elete, `VA` = View All, `MA` = Modify All.

---

## 1. Permission Set — 업무용 (핵심)

| Permission Set | Label | 대상 Object (CRUD) | Field 수 | Apex / Flow | Tab | 용도 / 사용 대상 |
|---|---|---|---|---|---|---|
| **`FRM_Manager_Access`** | FRM Manager Access | Account `CRU+VA`, Campaign `CRU+VA`, Case `CRU`, Recommendations__c `RU+VA`, Contact/Order/Benefits__c/Attendance_Record__c/Engagement_Signal__c/Fan_Activity_Pattern__c/Fan_Segment_History__c/Notification_Log__c `R+VA`, Admission__c/Game__c/Season__c/Product2 `R` | 42 | Apex 7 (`Fan360Controller`, `FanListController`, `FanDetailController`, `Fan360LandingController`, `GameDetailController`, `CampaignController`, `ReportController`) | — | **FRM Manager(김매니저) 핵심 Permission Set.** Fan 360 전체 읽기 + Account/Campaign/Case 편집. `CreatedBy` Hyejune, `LastModifiedBy` Sara |
| **`Fan_App_API_Access`** | Fan App API Access | Account `CRU`, Order `CRU`, Admission__c `CR`, Engagement_Signal__c `CR`, Attendance_Record__c/Campaign/Contact/Game__c/Pricebook2/Product2/Season__c `R` | 45 | — | — | **외부 Fan App 연동용** (Integration User). License = `SalesforceAPIIntegrationPsl`. `External_ID__c` 기반 upsert. `CreatedBy` Rafael Espada |
| **`VIP_Recommendation_Agent_Access`** | VIP Recommendation Agent Access | Recommendations__c `RU`, Account/Contact `R` | 155 | Apex 8 (`GetPendingVipRecommendationsAction`, `ApproveRecommendationAction`, `SendRecommendationEmailAction`, `RecommendationSegmentController`, `RecommendationReviewController`, `RecommendationActionLabels`, +Test, `recommendationController`) | Recommendations__c, Account | VIP Recommendation Agent(Sara) 및 검토 화면 접근. Account 필드 155개 노출(광범위 — 검토 필요) |
| **`Campaign_Hub_New_Fields_Access`** | Campaign Hub New Fields Access | (object 없음, field only) | 5 (`Benefits__c.Badge_Label__c`/`Discount_Rate__c`/`Min_Purchase_Amount__c`, `Contact.Name_EN__c`, `Product2.Is_Player_Goods__c`) | — | — | 신규 필드 FLS 보강용 (add-on). `CreatedBy` Sara |
| **`Own_Organization_Access`** | Own Organization Access | (내용 없음) | 0 | — | — | `Own_Organization` RecordType(구단 자체 Account)용 — **현재 빈 Permission Set (Verification Required)** |

### B2B / 영업

| Permission Set | Label | 대상 Object (CRUD) | Field 수 | Apex / Flow | 용도 |
|---|---|---|---|---|---|
| **`CA_Opportunity_Agent_Access`** | CA Opportunity Agent Access | Opportunity `RU`, Quote `CRU`, Account/Contact/Lead/Interaction_Intelligence__c/Interaction_Signal__c/Pricebook2/Product2 `R` | 51 | Apex 16 (`OpportunityAgentChatController`, `DealContext`, `OpportunityStageGuidance`, `NegotiationContext(+Controller)`, `NegotiationTermsUpdater`, `NegotiationOpportunityLookup`, `SponsorshipPackageLookup`, `SponsorshipProposalSaver`, `OpportunityProposalContext`, `FindSimilarClosedDeals`, `FindActivityAttendee`, `FindSponsorshipPackage`, `ActivityIntelligence*`, `ConversationHistoryAgentAction`) | Opportunity Agent(Eunyeong) 전체 툴 접근 |
| **`CA_Opportunity_Qualification_Access`** | CA Opportunity Qualification Access | Interaction_Intelligence__c `CRU`, Interaction_Signal__c `CRU` | 47 (Opportunity 필드 다수 + Event 미팅 필드) | — | Opportunity Qualification 화면 (미팅 인텔리전스 입력·조회) |
| **`CA_Campaign_Agent_Access`** | CA Campaign Agent Access | Campaign `RU`, Campaign_Deliverable__c `RU` | 6 | Apex 3 (`CampaignBottleneckFinder`, `CampaignMitigationRecorder`, `RenewalSummaryRefresher`) | 스폰서십 캠페인 에이전트(Rafael) |
| **`PRM_Manager_Access`** | PRM Manager Access | Account/Contact/Quote `CRUD`, Opportunity `CRUD`, Lead `CRU+VA` | 9 | Apex 1 (`LeadAiSummaryController`), Tab `standard-Lead` | **파트너/영업 Manager 핵심 Permission Set.** License = `Salesforce`. `CreatedBy` Hyejune |
| **`PRM360_Home_Access`** | PRM360 Home Access | Sales_Briefing__c `R` | 2 (`Lead.Final_Lead_Score__c`, `Lead.Risk_Penalty__c`) | Apex 1 (`PRM360Controller`) | PRM 파트너 포털 홈 위젯 |
| **`Partner_Contacts_Access`** | Partner Contacts Access | Contact `CRU+VA` | 0 | — | 파트너 담당자 Contact 관리 |
| **`Partnership_Team_Access`** | Partnership Team Access | **AccountPlan** `CRU` | 14 (AccountPlan 전 필드) | — | 스폰서십 Account Plan 관리 (표준 AccountPlan Object — 활성 여부 `Verification Required`) |
| **`Sponsorship_Rollup_Access`** | Sponsorship Rollup Access | (object 없음) | 3 (`Account.Sponsor_Tier__c`/`Sponsorship_Opportunity_Count__c`/`Total_Sponsorship_Value__c`) | — | 스폰서십 롤업 필드 FLS |

### DART 연동

| Permission Set | Label | 대상 Object (CRUD) | Field 수 | Apex / Flow | 용도 |
|---|---|---|---|---|---|
| **`DART_Sponsorship_Features`** | DART & Sponsorship Features (Lee) | DART_Corp_Mapping__c `CRUD+VA+MA` | 21 (Account DART/스폰서 필드 전체) | Apex 12 (`DartService`, `DartMatchService`, `DartEnrichment*`, `DartMatch*`, `DartHttpMock`, +Test, `NegotiationContext` 계열) · **Flow 5** (`DART_Account_Approved_Enrich`, `DART_Lead_Convert_Match`, `Rollup_Sponsorship_To_Account`, `Rollup_Sponsorship_On_Delete`, `Sync_Account_Latest_Open_Opportunity`) | **DART 기능 통합 Permission Set** (데모 유저 "Lee"용). `CreatedBy` Aaron, 08-31 |
| **`DART_Enrichment_Admin`** | DART Enrichment Admin | DART_Corp_Mapping__c `CRUD+VA+MA` | 15 (Account DART 필드) | — | DART enrichment 관리자 |
| **`DART_Map_Eng`** | DART Map Eng | (object 없음) | 1 (`DART_Corp_Mapping__c.Corp_Name_Eng__c`) | — | 영문 기업명 필드 FLS add-on |

### 통합 / 세션

| Permission Set | Label | Type | 용도 |
|---|---|---|---|
| `sfdc_slack` | Slack Integration User | Session | Slack 연동 세션 권한. `CreatedBy` Sara |
| `Unmetered_Vibes` | Unmetered Vibes | Regular | Agentforce Vibe 사용량 관련. `CreatedBy` Sara |
| `PSforAgentforce` | PSforAgentforce | Regular | (내용 없음) `Verification Required` |

---

## 2. Persona별 Permission Set 할당


| Persona | Profile | Permission Set | 권한 영역 |
|---|---|---|---|
| Manager Kim (FRM) | Standard User | `FRM_Manager_Access` | FRM(팬/고객 관계) 관리 |
| Manager Kim (FRM) | Standard User | `VIP_Recommendation_Agent_Access` | VIP 추천 기능 |
| Manager Lee (B2B/PRM) | Standard User | `CA_Opportunity_Agent_Access` | Opportunity/영업 Agent 기능 |
| Manager Lee (B2B/PRM) | Standard User | `DART_Sponsorship_Features` | Sponsorship·DART 기능 |
| Manager Lee (B2B/PRM) | Standard User | `FRM_Manager_Access` | FRM(팬/고객 관계) 관리 |
| Manager Lee (B2B/PRM) | Standard User | `Partnership_Team_Access` | Partnership 업무 |
| Manager Lee (B2B/PRM) | Standard User | `PRM_Manager_Access` | PRM 영업/거래 관리 |
| Manager Lee (B2B/PRM) | Standard User | `PRM360_Home_Access` | PRM 360 홈/브리핑 |
| Manager Lee (B2B/PRM) | Standard User | `Sponsorship_Rollup_Access` | Sponsorship 롤업 지표 조회 |
| Team(팀원 전체) | Administrator | — | 개발/관리 전권 |

---

## 3. Permission Set — Agentforce 자동 생성 (껍데기)

| Permission Set | 연결 Agent | CreatedBy |
|---|---|---|
| `NextGen_1bYbm000000OVlpEAG_Permissions` | Sponsorship Proposal Assistant | Aaron |
| `VIP_Recommendation_Agent1953041785_Permissions` | VIP Recommendation Agent | Sara |
| `VIP_Reccommendatio1429748782_Permissions` | VIP Recommendation Agent (오타 버전) | Sara |
| `VIP_Reccommendatio617401267_Permissions` | VIP Recommendation Agent (오타 버전) | Sara |


---

## 4. Profile (팀 생성)

| Profile | Type | CreatedBy | 용도 |
|---|---|---|---|
| `FanQuiz Profile` | Guest | Sara (08-29) | **FanQuiz Experience Site Guest User** — 팬 퀴즈 응모(`Quiz_Entry__c`) |
| `Cloud Alpacas Partnership Profile` | Guest | Eunyeong (08-30) | **Partnership Experience Site Guest User** — 스폰서십 문의(`PartnershipInquiryController`) |
| `System Administrator` (clone) | Standard | Eunyeong (08-24) | 관리자 프로파일 커스터마이징 (상세 `Verification Required`) |
| `Standard User` | Standard | (Salesforce 기본) | Persona(Manager Kim/Lee)의 기본 Profile — Account/Contact/Lead/Opportunity/Order/Quote 등 `CRUD` 기본 제공 |


---

## 5. 레코드 접근 (OWD / Sharing Rule)

| Object | OWD | Sharing Rule | 공유 대상 | Access |
|---|---|---|---|---|
| Opportunity | Private | `Partnership Team Visibility` | Partnership Team | Edit |

**Sharing Rule 상세**

| Rule | Shared From | Shared To | Access | 설정 |
|---|---|---|---|---|
| Partnership Team Visibility | Partnership Team 소유 Opportunity | Partnership Team | Edit | Partnership Team 구성원 간 Opportunity 공동 관리 |

---

## 6. Role Hierarchy

| 대상 | Role | 적용 여부 | 설정 |
|---|---|---|---|
| Persona | 미할당 | 미사용 | Manager Kim / Manager Lee |
| Team | 미할당 | 미사용 | 프로젝트 팀원 계정 |

---

## 7. Permission Set Group

| | 내용 |
|---|---|
| **Org Actual** | `PermissionSetGroup` 조회 결과 팀 생성 PSG **확인 안 됨** (쿼리 실행됨, 팀 `CreatedBy` 0건) |
| **결론** | Cloud Alpacas 는 Permission Set Group 미사용 — 개별 Permission Set 을 사용자에게 직접 할당 |

---

## 8. Custom Tab (팀 생성, 19)

| Tab | CreatedBy | 연결 |
|---|---|---|
| `Fan_360_Landing`, `Fans`, `FAN_360_v1` | Sara / Hyejune | Fan 360 메인 |
| `Fan_Insights` | Eunyeong | 세그먼트/인사이트 |
| `Game_List` | Hyejune | Game 목록 |
| `Recommendation_Dashboard` | Sara | 추천 대시보드 |
| `Campaigns_Dashboard` | Sara | 캠페인 대시보드 |
| `Recommendations__c` (Object Tab) | Sara | `Recommendations__c` 레코드 |
| `PRM_360`, `PRM_360_Home` | Hyejune | PRM 파트너 포털 |
| `Quiz_Reveal`, `Live_Fan_Quiz_Reveal` | Sara | 라이브 퀴즈 |
| (이름 미표기 7개) | Sara/Hyejune | Web/VF Tab 추정 — `Verification Required` |

---

## 9. Field 권한 (상세)

### Field-Level Security

> 상세 Field-Level Security는 `🦙 권한 설정 현황표` Excel을 기준으로 관리하며,
> MD에는 주요 Permission Set별 접근 범위를 요약한다.

| Permission Set | 주요 대상 Object | 접근 범위 | 주요 목적 |
|---|---|---|---|
| `FRM_Manager_Access` | Account, Contact, Game__c, Order, Product2, Fan 관련 Custom Objects | Read / 일부 Edit | B2C Fan 360 및 Fan 관리 |
| `PRM_Manager_Access` | Lead, Opportunity | Read / Edit | B2B Partnership 관리 |
| `PRM360_Home_Access` | Lead | Read | PRM360 Home 조회 |
| `CA_Opportunity_Agent_Access` | Opportunity, Event, Task, Interaction Intelligence 등 | Read / 일부 Edit | Opportunity Agent 업무 수행 |
| `Sponsorship_Rollup_Access` | Account | Read | Sponsorship 집계 정보 조회 |
| `DART_Sponsorship_Features` | Account, DART_Corp_Mapping__c | Read / Edit | DART 기업정보 및 기업 매칭 |
| `VIP_Recommendation_Agent_Access` | Account, Recommendations__c | Read / 일부 Edit | VIP Fan 추천 및 개인화 |
| `Standard User` | Account, Campaign, Case, Contact, Lead, Opportunity, Order | Read | Salesforce 기본 사용자 접근 


### 주요 Field 권한

| 영역 | Object | 주요 Field | 권한 |
|---|---|---|---|
| Fan 360 | Account | `Current_Segment__c`, `Engagement_Level__c`, `Engagement_Score__c`, `Fan_Value_Tier__c` | Read |
| Fan 360 | Account | `Favorite_Player__c`, `Acquisition_Channel__c`, `Email_Opt_In__c` | Read / Edit |
| Fan Activity | `Fan_Activity_Pattern__c` | `Attendance_Rate__c`, `Games_Attended__c`, `Goods_Purchases__c`, `Total_Spend__c` | Read |
| Recommendation | `Recommendations__c` | `Personalized_Message__c`, `Reason__c` | Read / Edit |
| B2B Lead | Lead | `Lead_Score__c`, `Segment_Match__c`, `Target_Segment__c` | Read / Edit |
| B2B Opportunity | Opportunity | `Target_Segment__c`, `Partner_Tier__c`, `Expected_Benefit_*` | Read / Edit |
| Opportunity Agent | Opportunity | `Customer_Needs__c`, `Customer_KPI__c`, `Key_Requirements__c` | Read / Edit |
| Interaction | `Interaction_Intelligence__c` | `Summary__c`, `Key_Decision__c`, `Customer_Reaction__c` | Read |
| DART | Account | `Corp_Name_Eng__c`, `Stock_Code__c`, `Match_Confidence__c`, `Match_Rationale__c` | Read / Edit |

---

## 10. Known Limitations / Verification Required

| 항목 | 상태 |
|---|---|
| Persona↔Permission Set 할당(§2)이 Sara의 Org 인벤토리와 교차검증 안 됨 | `PermissionSetAssignment` 쿼리로 재확인 |
| Guest Profile 상세 권한 (`FanQuiz Profile`, `Cloud Alpacas Partnership Profile`) | Object/Field/Apex/Flow 권한 미조회 — 별도 retrieve 필요 |
| `System Administrator` clone 변경 내용 | 미조회 |
| `Own_Organization_Access`, `PSforAgentforce`, `Partner_Contacts_Access` | 실질 내용이 거의 없음 — 의도된 것인지 미완인지 팀 확인 |
| `VIP_Recommendation_Agent_Access` 의 Account 155필드 노출 | 최소 권한 원칙 대비 광범위 — 검토 권장 |
| `recommendationController` (VIP PS 참조 Apex) | `CreatedBy = Chanyeon Kim` (SDO 클래스) — 팀 코드 아님, 참조 경위 확인 필요 |
| Opportunity 외 Object(Account, Case, Recommendations__c 등)의 OWD | 미확인 — Setup > Sharing Settings 직접 확인 필요 |
| Field 권한 상세 (read vs edit 구분) | PS 11개는 혜준님 xlsx 참조, 나머지 8개는 XML 원본 참조 필요 |
| App(CustomApplication) 접근 | PS XML 에 `<applicationVisibilities>` 없음 — App 은 Profile 또는 별도 설정. `Verification Required` |
