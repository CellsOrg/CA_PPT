# 06_BACKLOG — Cloud Alpacas Team Development Backlog

## 1. 전체 개발 범위

프로젝트 전체에서 팀이 구현한 영역을 7개 카테고리로 정리한다.

| # | 카테고리 | 내용 | 주요 담당(원본 기준) |
|---|---|---|---|
| A | **Project Strategy / Documentation** | Business Goal·Persona·Story, Domain Model, Salesforce Architecture, 의사결정(ADR), Source of Truth 문서, 제출 산출물 설계 | 사라 |
| B | **B2C Fan Relationship** | Fan 360 통합 프로필, 3축 데이터 모델, 팬 행동 기반 Engagement Flow, 추천 세그먼트, 캠페인 반응·전환 추적 | 승우 · 은영 · 사라 |
| C | **Fan Experience / Event** | Fan App(가입·구매·체크인) ↔ Salesforce 연동, 발표 참여 이벤트(Live Fan Quiz) | 은영 · 사라 |
| D | **Recommendation / Agentforce** | Recommendation 검수·발송, VIP Recommendation Agent, 개인화 메시지, Opportunity Agent(+서브에이전트), Sponsorship Campaign Agent, Lead AI Summary, Stage Guidance, Sales Briefing | 사라 · 은영 · 승우 · 혜준 · 아론 |
| E | **B2B Sponsorship Sales** | 파트너십 데이터 모델, Lead Scoring, DART 공시 자동보강, Sponsorship Package·Quote, Campaign 생애주기, Pipeline·Revenue 대시보드, 스폰서 등급 산정 | 아론 · 혜준 · 승우 · 은영 |
| F | **Automation / Integration** | Record-Triggered Flow 자동화, Slack 지연 알림, Fan App REST API, Zoom·Google Meet, Experience Cloud, DART OpenDART API, Campaign 예상 매출 동기화 | 승우 · 아론 · 사라 · 은영 |
| G | **Dashboard / UX** | Fan 360 Landing·Fan List, PRM 360 Dashboard, Pipeline·Revenue 대시보드, 캠페인 실시간 성과, Opportunity 업무 화면, 디자인 시스템 | 사라 · 혜준 · 은영 · 승우 |
| H | **Data / Org Configuration** | 공용 Dummy Data 규칙, Pilot Cohort, 파트너십 샘플 데이터, RecordType·Permission·Sharing 정비, Org 검수 | 사라 · 아론 · 승우 |

> B2B(스폰서십 세일즈)와 B2C(팬 관계)를 두 축으로, 그 위에 Agentforce·자동화·
> 대시보드·데이터/Org 구성이 공통 기반으로 얹히는 구조다.

---

## 2. 팀원별 담당 및 구현 내용

### 사라

| 구분 | 내용 |
|---|---|
| **기획/설계** | 프로젝트 세계관·Business Goal·Pain Point·Persona(김매니저/이루키)·Customer Journey 정의(`00_STORY`), Business First 문서 체계·Source of Truth 원칙, 팀 역할 정의(자동차 비유·Baby PM+Feature Owner), Phase 2 B2B 방향 전환(Sponsorship Sales Pipeline, 대표 시나리오 d'Alba), 발표 범위 재편(P0 Recommendation Agent + P1 참여 Event), A~K Technical Decision 회의 준비·진행, 30+ 의사결정 기록(`05_DECISIONS`) |
| **Salesforce Architecture** | 5 Domain Model(Fan/Operations/Marketing/Service/Partnership), Workflow 기준 Entity 추출, Business Entity → Salesforce Object 매핑(Standard-first 판단), 3축 데이터 모델(**Life Cycle `Current_Segment__c` / Engagement `Engagement_Level__c` / Fan Value `Fan_Value_Tier__c`**), Phase 2 B2B Architecture Draft(`03_SYSTEM §7`), Org 검수 리포트·메타 스냅샷 |
| **Object / Field** | `Quiz_Entry__c`, `Fan_Campaign_Msg_Request__e`(Platform Event) 생성 / `Recommendations__c`에 `Status__c` 값(Approved·Sent)·`Sent_Date__c` 추가 |
| **Flow / Automation** | `Fan_Engagement_Calc`, `Fan_Value_Calc`, `Order_Paid`, `Admission_Created`, `Fan_Activity_Pattern_Admission_Update`, `Upsert_Activity_Pattern_From_Order`, `Count_Goods_And_Season`, `Order_Membership_Status_Sync`, `Fan_Engagement_Daily_Recalc`, `Fan_Campaign_Personalized_Msg_Flow`, `Generate_AI_Recommendation_Message`, `Quiz_Entry_Set_Is_Correct`, `Fan_Insight_Slack_Alert`, `Test_Slack_Notification` 생성 / `VIP_Candidate_Detection_Flow_V1` 및 Phase 1 Campaign Flow(Welcome·First Ticket·First Visit Guide·First Merchandise·Favorite Player) 수정·검증 |
| **Apex** | `FanListController`, `Fan360LandingController`, `RecommendationReviewController`, `RecommendationActionLabels`, `RecommendationSegmentController`, `GetPendingVipRecommendationsAction`, `ApproveRecommendationAction`, `SendRecommendationEmailAction`, `LiveFanQuizRevealController`, `QuizEntrySubmitController`(+Test 클래스) / `CampaignController` 수정 |
| **LWC** | `fan360Landing`, `fanList`·`fanListKpiCards`·`fanListSearchFilter`·`fanListTable`·`fanDetailDrawer`, `recommendationReviewPanel`, `recommendationSegmentDashboard`, `liveFanQuizEntry`, `liveFanQuizReveal`, `icon` 생성 / `reportDashboard`·`campaignBoard`·`fanTimeline`·`gameDetail`·`fan360Summary`·`fanSummary`·`fanRecommendedActions` 통합·리디자인 |
| **Agentforce** | **VIP Recommendation Agent**(`VIP_Recommendation_Agent`, Employee Agent) — Agent Script + Invocable Apex 3종 + Permission Set `VIP_Recommendation_Agent_Access` + App `Cloud_Alpacas_FRM`. 조회→승인→발송 E2E + 실제 이메일 발송 검증. Agent 아키텍처 표준(단일 실행 블록, Apex 하드 가드), Agentforce 범위 예외 승인(Decision 017) |
| **Data** | 공용 Dummy Data 규칙(`DEMO_DATA_STANDARD` — Naming Rule, Cross-Object Consistency, `SCN-B2B-001`), P2 Dummy Data Master(Fan 30명 + d'Alba 시나리오), 60명 Pilot Cohort 생성·자동화 검증·Backfill(`PersonGender`/`PersonBirthdate`/`Acquisition_Channel__c` 등), 5,000명 Target Scale 기준 |
| **UX/UI** | Phase 1 핵심 4화면 UX 초안(Fan 360 Dashboard/Profile/Timeline/Recommendation Panel), 디자인 시스템(브랜드 컬러 `#FC4E00`, 공용 `cloudAlpacas.css`, `icon` SVG), 발표 참여 Event UX(`EVENT_SPEC`) |
| **QA / Demo** | Demo 시나리오 재작성(`04_DEMO` — Scene 1 Recommendation Agent / Scene 2 Live Fan Quiz), 이메일 발송 인프라 검증(SPF/DKIM 한계 규명 → Naver 데모), Campaign Hub 조사(대상 0명 원인 규명 + `Benefits__c` 필드 5종), 팀원 개발 결과(은영 PR·승우 Campaign Flow) 검수·Integration, Troubleshooting 체크리스트 12항목 |
| **Documentation** | `00_STORY`·`01_PROJECT`·`02_TEAM_GUIDE`·`03_SYSTEM`·`04_DEMO`·`05_DECISIONS`, `P2_TECHNICAL_DECISION_SHEET`, `DEMO_DATA_STANDARD`·`P2_DUMMY_DATA_MASTER`·`PILOT_COHORT_ANALYSIS`, `members/00~04`+README, `AGENT_SPEC`·`EVENT_SPEC`·`VIP_Recommendation_Agent-AgentSpec`·`HANDOFF_SESSION_SUMMARY` |
| **관련 산출물** | `docs/00~05`, `docs/decision_sheet/`, `docs/data/`, `docs/members/`, `docs/AGENT_SPEC.md`, `docs/EVENT_SPEC.md`, `docs/backlog/sara.md` |

### 승우

| 구분 | 내용 |
|---|---|
| **기획/설계** | 스폰서십을 "판매 가능한 영업 상품"으로 관리하는 상품·견적 체계 설계, 스폰서십 Campaign 생애주기(발굴/실행/갱신) 구조 설계, KBO·MLB 벤치마크 기준 상품 가격 체계 확정 |
| **Salesforce Configuration** | Campaign Record Type·Path·List View·Hierarchy(Parent Campaign), Layout(`Sponsorship Collaboration Execution Layout`, `Sponsorship Renewal Layout`), Page Layout Assignment, Quote Template `Cloud Alpacas Sponsorship Quote`, Product Revenue Schedule / Quote Sync, Permission Set `CA_Campaign_Agent_Access`, Named Credential `CA_Agent_API_PerUser`, FlexiPage `Campaign_Record_Page3` |
| **Object / Field** | `Campaign_Deliverable__c` 신규(`Status__c`·`Weight__c`·`Due_Date__c`·`Completed_Date__c`·`Evidence_URL__c`·`Notes__c`·`Blocked_Reason__c`·`Pending_Slack_Message__c`), `Product2.Sponsorship_Package` Record Type + 상품 21종, `PricebookEntry.Max_Discounted_Price__c`·`Max_Discount_Percent__c`, `Campaign.Performance_Summary__c`·`Total_Deliverable_Weight__c`·`Completed_Deliverable_Weight__c`·`ExpectedRevenue`, `Opportunity.Partner_Tier__c` |
| **Flow / Automation** | `Campaign_Deliverable_Detect_Due_Date_Push`(Before-Save 메시지 조립), `Campaign_Deliverable_Blocked_Slack_Alert`(비동기 Slack 발송), `Renewal_Campaign_Performance_Summary`, `Recalculate_Campaign_Expected_Revenue`·`Campaign_Expected_Revenue_Sync`·`Campaign_Expected_Revenue_Sync_On_Delete` |
| **Apex** | `CampaignBottleneckFinder`, `CampaignMitigationRecorder`, `RenewalSummaryRefresher`, `CampaignAgentChatController`, `OpportunityProposalContext`, `SponsorshipPackageLookup`, `SponsorshipProposalSaver` |
| **LWC** | `campaignAgentChat`, `campaignAgentChatModal` |
| **Agentforce** | `Sponsorship_Campaign_Agent`(실행 병목 조회 → 대책 제안 → Notes 갱신·Task 생성 → 갱신 성과 요약, Router + Subagent), `Sponsorship_Proposal_Assistant`(Opportunity 조회 → 상품 추천 → 확인 후 Quote·QuoteLineItem 생성) |
| **Integration** | Salesforce Slack Action `#campaign-alerts`, Connect REST API로 Per-User OAuth 인증 URL 발급, Fan App REST API 연동(Connected App·API Scope·Refresh Token·Integration User·`Fan_App_API_Access`) |
| **Data / Org** | Fan App 누락 상품(Product2 10종)·경기(Game 1건) 정의, Standard Price Book KRW PricebookEntry 데이터 계약, Person Account Record Type / Profile 권한 정비, 테스트 팬 데이터 복구 |
| **Dashboard** | 스폰서십 Pipeline·Revenue Report 5종 + Dashboard 7위젯 + Net Profit Custom Summary Formula |
| **QA** | Deliverable Blocked/납기연기/지연사유 6종 Slack 발송(7시나리오), d'Alba Product→Opportunity Product→Quote→Sync→PDF E2E |
| **관련 산출물** | `docs/backlog/seungwoo.md`, Sponsorship Package 상품 카탈로그, Sponsorship Quote Template, Pipeline·Revenue Dashboard |

### 은영

| 구분 | 내용 |
|---|---|
| **기획/설계** | Opportunity Agent 오케스트레이션 구조 설계(Router + 역할별 Assistant 분리), 단계별 Opportunity 업무 화면 설계, 추천 세그먼트 4종을 실제 데이터 판별 조건으로 구체화 |
| **Salesforce Configuration** | `CA_Opportunity` FlexiPage(Dynamic Forms + 독립 컴포넌트 배치), Experience Cloud 사이트 `/CApartnership`, OAuth(Per-User `CA_Agent_API_PerUser`, Client Credentials), Zoom·Google Meet 사용자 권한 세트 |
| **Object / Field** | `Interaction_Intelligence__c`, `Interaction_Signal__c`, Interaction Intelligence 관련 필드(summary·customer reaction·key decision·concerns·follow-up·signals), 첨부파일 Token Field |
| **Flow / Automation** | `CA_Create_Opportunity_Activity`, Zoom·Google Meet ↔ Salesforce 영업 활동/Conversation Intelligence 연동 |
| **Apex** | `StageGuidanceController`, `ActivityIntelligenceController`, `FindActivityAttendee`, `FindSimilarClosedDeals`(유사도 점수 계산), `OpportunityAgentChatController`, `PartnershipInquiryController` |
| **LWC** | `stageGuidance`, `opportunityAgentChat`, `stageProgress`, `activityTimeline`, `negotiationContextSummary`, `segmentFanList`, `campaignBoard`, `partnershipInquiry` |
| **Agentforce** | **Opportunity Agent**(Agent Router + Activity/Deal/Proposal/Negotiation Assistant + Ambiguous/Escalation/Off Topic, 상태 변수·확인 단계), Opportunity Stage Guidance(`CA_Stage_Guidance_Recommendation` Prompt Template, 읽기 전용), Activity Assistant + Interaction Intelligence, Proposal·Negotiation Assistant를 Opportunity Agent 흐름에 **통합·오케스트레이션**(최초 Assistant 개발자는 별도 팀원), Similar Historical Closed Won Deal 조회, Opportunity Record Page 내장 채팅 |
| **Data** | Recommendation 세그먼트 대상(멤버십 전환 대상 / 가입 후 미방문 / 최근 방문 감소 / 충성도 높지만 굿즈 미구매) 판별 조건 |
| **UX/UI** | Opportunity 업무 화면(진행 단계·활동 이력·협상 정보·단계별 가이드·Agent 진입점 통합), 캠페인 실시간 성과 대시보드, Fan App 화면 흐름(장바구니·결제·체크인) |
| **Integration** | B2C Fan App ↔ Salesforce(`signup`·`favorite-player`·`checkin`·`engagement`·`auth` API, OAuth Client Credentials), 외부 파트너 문의 → Lead 자동 수집(Experience Cloud) |
| **QA** | 컴포넌트·Apex·Jest 테스트, Stage 분리 검증, 과거 E2E 기록(현재 활성 Agent 버전·실제 대화 실행은 재확인 필요로 표기) |
| **관련 산출물** | `docs/backlog/eunyeong.md`, Opportunity Agent, `CA_Opportunity` 업무 화면, B2C Fan App |

### 혜준

| 구분 | 내용 |
|---|---|
| **기획/설계** | PRM 360 Dashboard 기획(매출 상황 → 주요 Deal → 고전환 Lead → 오늘 할 일 흐름), Lead Scoring 체계 설계(적합성 + 관심도 + 계약 준비도 + Risk), "Salesforce는 업무 실행 / Tableau는 분석" 역할 구분 |
| **Salesforce Configuration** | App `Cloud Alpacas PRM`, Lightning Page `PRM_360`·`PRM_360_Home`·`Lead_Record_Page`, Dashboard `PRM_360_Overview` |
| **Object / Field** | `PRM_Revenue_Target__c`(Custom Object/Setting), `Sales_Briefing__c`, Lead 신규 필드 11종(`Regional_Connection__c`·`Sponsorship_History__c`·`Competitor_Sponsor__c`·`Controversial_Industry__c`·`Score_Industry__c`·`Score_Region__c`·`Score_Sponsorship__c`·`Score_Interest__c`·`Score_LeadSource__c`·`Risk_Penalty__c`·`Final_Lead_Score__c`), `AI_Lead_Summary__c`, 기존 SDO Scoring 필드 재사용·수정(`Score2__c`·`SDO_Sales_Lead_Total__c`·`SDO_Sales_Lead_Quality__c`) |
| **Flow / Automation** | `HighScore_Lead_Contact_Flow`(고득점 Lead 후속 연락 Task 자동 생성) |
| **Apex** | `PRM360Controller`, `PRM360SummaryController`, `PRM360SalesBriefingScheduler`, `LeadAiSummaryController` |
| **LWC** | `prmSeasonTargetAttainment`, `prmSeasonClosedWonRevenue`, `prmYoyRevenue`, `prmOpenSponsorshipPipeline`, `prmKeyOpportunities`, `prmClosingSoonOpportunities`, `prmHighPotentialLeads`, `prmTodaysEvents`, `prmMyTasks`, `prmQuickLinks`, `prmSalesBriefing`, `leadAiSummaryCard` |
| **Agentforce / AI** | PRM 360 Sales Briefing(`CA_PRM360_Sales_Briefing` Prompt Template, 규칙 기반 Fallback, `Sales_Briefing__c` 저장 — 별도 Agent 없음), Lead AI Summary(`CA_Lead_AI_Summary` Prompt Template, `Final_Lead_Score__c` 기준 설명) |
| **Report** | `Season_Target_Attainment`, `Open_Sponsorship_Pipeline`, `Sponsorship_Pipeline_by_Stage_PRM`, `Season_Closed_Won_2026`, `Season_Closed_Won_Summary_PRM`, `Sponsorship_Revenue_YoY_PRM`, `Todays_Events_PRM`, `ActionsByPriority`, `Key_Opportunities_PRM`, `Closing_Soon_Opportunities`, `High_Potential_Leads` |
| **Lead Scoring 로직** | 항목 배점(Industry Fit 25 / Decision Timeframe 20 / Interest 12 / Regional 10 / Sponsorship History 10 / Lead Source 8 / Budget·Decision Maker·Project Defined 각 5 = 100점) + `Risk_Penalty__c` → `Final_Lead_Score__c`, Formula 컴파일 크기 최적화 |
| **UX/UI** | PRM 360 Home(KPI + List + AI Briefing 통합), 고전환 Lead를 차트가 아닌 실제 Lead 목록으로 제공 |
| **분석 연계** | Tableau Next, Salesforce C360 Semantic Model, Dashboard Embedding, Salesforce↔Tableau 집계 기준 비교 |
| **QA** | KPI 원천 데이터 ↔ 화면 값 일치, Record 클릭·권한별 데이터 접근, 대표 Lead 고득점/저득점/Risk 케이스 검증, Prompt 호출·Fallback 흐름 |
| **관련 산출물** | `docs/backlog/hyejune.md`, PRM 360 Dashboard, Lead Scoring 체계, Sales Briefing |

### 아론

| 구분 | 내용 |
|---|---|
| **기획/설계** | 채널판매 PRM 기본값을 스포츠 구단 스폰서·제휴 맥락으로 전환하는 데이터 모델 정비, "식별이 아니라 다음 행동 판단"을 위한 리스트뷰 설계, 장기 파트너십(연 갱신·N년차) 시계열 데이터 설계 |
| **Salesforce Configuration** | Account·Contact RecordType 라벨 → "파트너십", `SDO_Partner_Type__c`·`SDO_Partnership_Status__c` 제한 픽리스트 개편, OpportunityStage `Contracting` 추가, FlexiPage 탭 재편, FlexiPage `SDO_Sales_Account_Partner_Account` + 레코드페이지 Record Type Activation, `relatedListComponentOverride` ADVGRID 재배포, Page Layout Assignment |
| **List View** | Account `PartnershipAccounts`·`Sponsor Accounts`(RecordType 필터, 목적별 컬럼 분리), Contact `Partner Contacts`(모바일·이메일 우선) |
| **Object / Field** | `DART_Corp_Mapping__c`(상장사 3,988건), `DART_Setting__c`(Custom Setting), `Sponsor_Tier__c`(Diamond/Platinum/Gold/None), `Sponsorship_Opportunity_Count__c`, `Total_Sponsorship_Value__c`, Account `Latest_Open_Opportunity_Stage__c`·`Latest_Open_Opportunity_Amount__c`·`Latest_Open_Opportunity_Next_Step__c` |
| **Flow / Automation** | 스폰서 등급·건수·금액 자동 산정(Record-Triggered, 임계값 15억/5억), 계정 요약필드 동기화(최신 Open Opportunity 3필드, 기존 26계정 백필), `DART_Lead_Convert_Match`·`DART_Account_Approved_Enrich` |
| **Apex** | `DartService`, `DartMatchService`, Queueable / Invocable Apex(DART 매칭·보강) |
| **Agentforce** | Negotiation 서브에이전트(Opportunity Agent 협상 파트 — Proposal 이후 활동 이력 그라운딩 + Pricebook 등급별 할인율 기준 협상안 초안, 통합·오케스트레이션은 은영과 연계) |
| **Integration** | DART OpenDART 공시 API 콜아웃(RemoteSiteSetting), Einstein Models API(`sfdc_ai__DefaultGPT4Omni`)로 회사명 → 종목코드 추론 + 실재 검증(환각 방지) |
| **Security / 권한** | Owner 이관 300건(→ Manager Lee), Public Group `Partnership_Team` + Opportunity Sharing Rule(OWD Private 대응), AccountPlan 오브젝트 Permission Set, DART 신규 필드 FLS Permission Set 선부여 |
| **Data / Org** | 파트너십 샘플 데이터 — Account·Contact·Opportunity 각 100, 계약 이력 2020~2024(Opp ~253·LineItem ~299), Order ~220·OrderItem ~298·Asset ~99·Contract 78·AccountPlan 50 (DART 연동분 외 전부 더미), `SPN-AUTO|<oppId>` 마커 추적 |
| **UX/UI** | 파트너십 계정 레코드 화면(연도별 스폰서십 추이 Report 차트 + 계약·관계 정보 + 관련 리스트) |
| **QA** | 배포·화면 반영, 리스트뷰 컬럼 의도대로 표시, 금액 변경 시 등급 실시간 재산정, DART Lead 전환 → 공시 보강 프로덕션 E2E 완료 |
| **관련 산출물** | `docs/backlog/aaron.md`, 파트너십 데이터 모델, DART 공시 자동보강 파이프라인, 파트너십 샘플 데이터셋 |

---

## 3. 주요 기능별 담당 현황

### B2C Fan Relationship / Fan Experience

| Feature / Business Area | 담당자 | 구현 내용 | 상태 |
|---|---|---|---|
| Fan 360 통합 고객 프로필 (데이터 모델) | 승우 | Person Account 중심으로 Order·Admission·Engagement·Activity Pattern·Segment History·Recommendation 연결 | 보완 필요 (대표 팬 E2E 재검증) |
| Fan 360 Landing 대시보드 | 사라 | `fan360Landing` LWC + `Fan360LandingController`, 세그먼트/Engagement/Fan Value 집계 | 완료 |
| Fan List 커스텀 화면 | 사라 | `FanListController` + LWC 5종(KPI·검색/필터/정렬·페이지네이션·Drawer) | 완료 |
| 3축 데이터 모델 (Life Cycle / Engagement / Fan Value) | 사라 | 축 정의·독립 원칙, Engagement/Value 계산 Flow 체인(`Fan_Engagement_Calc`·`Fan_Value_Calc`·`Order_Paid`·`Admission_Created` 등) | 완료 (Pilot 검증) |
| 팬 행동 기반 자동 Engagement Flow 6종 | 승우(구축) · 사라(수정·검증) | Welcome / First Ticket / First Visit Guide / First Merchandise / Favorite Player / VIP Candidate Detection | 보완 필요 (시나리오별 회귀 테스트) |
| 추천 세그먼트 + Fan 360 상세 조회 | 은영 | 4개 세그먼트 판별, `segmentFanList` LWC + `Fan360Controller`·`FanDetailController` | 보완 필요 (현재 Org 인원수·최신 데이터 확인) |
| Recommendation Segment Dashboard | 사라 | `recommendationSegmentDashboard` LWC + `RecommendationSegmentController` | 완료 |
| 팀원 Fan 360 LWC 통합·리디자인 | 사라 | `reportDashboard`·`campaignBoard`·`fanTimeline`·`gameDetail`·`fan360Summary`·`fanSummary`·`fanRecommendedActions` | 완료 |
| 팬 캠페인 반응·전환 추적 (5단계 Status) | 승우 | CampaignMember Status(Targeted→Reached→Engaged→Attended→Converted) + `Is_Converted__c` + Engagement Signal | 보완 필요 (5단계 일관 적용·연동 확인) |
| 캠페인 실시간 성과 대시보드 | 은영 | `campaignBoard` LWC + `CampaignController` + `Notification_Log__c` | 보완 필요 (현재 Org 데이터 재확인) |
| Fan App ↔ Salesforce 연동 (API) | 승우 · 은영 | Connected App·Integration User·`Fan_App_API_Access` / OAuth Client Credentials + signup·checkin·engagement·auth API | 보완 필요 (운영 API 쓰기·E2E) |
| Fan App 구매·체크인 UX (화면) | 은영 | Fan App SPA, 장바구니·결제·체크인 흐름 | 보완 필요 (`Order`/`OrderItem` 저장 추가 개발) |
| 발표 참여 이벤트 (Live Fan Quiz) | 사라 | `Quiz_Entry__c` + `QuizEntrySubmitController`·`LiveFanQuizRevealController` + `liveFanQuizEntry`·`liveFanQuizReveal` + `Quiz_Entry_Set_Is_Correct` | 완료 |

### Recommendation / Agentforce

| Feature / Business Area | 담당자 | 구현 내용 | 상태 |
|---|---|---|---|
| Recommendation 검수·승인·발송 Sidebar | 사라 | `RecommendationReviewController` + `recommendationReviewPanel` LWC, `Messaging.SingleEmailMessage` 발송, `EmailMessage` 이력 | 완료 (발송 검증) |
| 개인화 메시지 생성 (Prompt 연동) | 사라 | `Fan_Campaign_Personalized_Msg_Flow`·`Generate_AI_Recommendation_Message` + `Fan_Campaign_Msg_Request__e` + `Fan_Personalized_Message` Prompt Template | 완료 |
| VIP Recommendation Agent | 사라 | `VIP_Recommendation_Agent`(Employee Agent) + Invocable Apex 3종(`GetPendingVipRecommendationsAction`·`ApproveRecommendationAction`·`SendRecommendationEmailAction`) + PS `VIP_Recommendation_Agent_Access` | 완료 (E2E + 실제 이메일 검증, 계정 권한·`ko` 잔여) |
| Opportunity Agent (통합·오케스트레이션) | 은영 | Router + Activity/Deal/Proposal/Negotiation Assistant + Escalation/Off Topic, 확인 단계 | 보완 필요 (현재 활성 Agent 버전·실행 재확인) |
| Opportunity Stage Guidance | 은영 | `stageGuidance` LWC + `StageGuidanceController` + `CA_Stage_Guidance_Recommendation` Prompt | 보완 필요 (환각 방지 재검증) |
| Activity Assistant + Interaction Intelligence | 은영 | Task/Event 조회·생성·수정, 참석자 검색, `Interaction_Intelligence__c`·`Interaction_Signal__c` | 보완 필요 (현재 Agent 전 과정 재확인) |
| Similar Closed Won Deal 조회 | 은영 | `FindSimilarClosedDeals`, 유사도 점수 계산 | 보완 필요 (현재 Org 결과 적절성 확인) |
| Opportunity Agent 내장 채팅 | 은영 | `opportunityAgentChat` LWC + `OpportunityAgentChatController` + `CA_Agent_API_PerUser` | 보완 필요 (권한·OAuth·Agent 호출 재확인) |
| Sponsorship Campaign Agent | 승우 | `Sponsorship_Campaign_Agent` + Apex 4종 + `campaignAgentChat`·`campaignAgentChatModal` | 보완 필요 (위젯 시나리오·PS·단위 테스트) |
| Proposal·Quote 추천 Subagent | 승우 · (은영 통합) | `Sponsorship_Proposal_Assistant` + `OpportunityProposalContext`·`SponsorshipPackageLookup`·`SponsorshipProposalSaver` | 보완 필요 (Publish 안 됨, 동명 컴포넌트 소유권 정리 필요) |
| Negotiation 서브에이전트 | 아론 · (은영 통합) | Proposal 이후 활동 이력 그라운딩 + Pricebook 등급별 할인율 협상안 | 보완 필요 (현재 활성 Agent 쓰기 재확인) |
| Lead AI Summary + 후속 Task 자동화 | 혜준 | `leadAiSummaryCard` + `LeadAiSummaryController` + `CA_Lead_AI_Summary` Prompt + `HighScore_Lead_Contact_Flow` | 보완 필요 (구필드 `Lead_Score__c` ↔ `Final_Lead_Score__c` 기준 일치 확인) |
| PRM 360 Sales Briefing | 혜준 | `prmSalesBriefing` + `PRM360SalesBriefingScheduler` + `CA_PRM360_Sales_Briefing` Prompt + 규칙 기반 Fallback | 미표기 (전체 흐름 확인 진행) |

### B2B Sponsorship Sales

| Feature / Business Area | 담당자 | 구현 내용 | 상태 |
|---|---|---|---|
| 파트너십 데이터 모델·RecordType 정비 | 아론 | Account/Contact RecordType → "파트너십", `SDO_Partner_Type__c`·`SDO_Partnership_Status__c`, OpportunityStage `Contracting` | 미표기 (배포·화면 반영 정상, `SDO_` 중복 필드 확정 필요) |
| 파트너십/스폰서 계정·연락처 리스트뷰 | 아론 | `PartnershipAccounts`·`Sponsor Accounts`·`Partner Contacts` List View | 완료 |
| 파트너십 계정 레코드 화면 + 추이 그래프 | 아론 | FlexiPage `SDO_Sales_Account_Partner_Account` + 연도별 Report 차트 + 관련 리스트 | 완료 (Order·Asset·Account Planning 더미 데이터만 필요) |
| 스폰서 등급·건수·금액 자동 산정 Flow | 아론 | Record-Triggered Flow, `Sponsor_Tier__c`·`Sponsorship_Opportunity_Count__c`·`Total_Sponsorship_Value__c` | 완료 |
| 계정 요약필드 동기화 Flow | 아론 | Account `Latest_Open_Opportunity_*` 3필드, 26계정 백필 | 완료 (Opportunity delete 미처리) |
| Lead 전환 시 DART 공시 자동보강 | 아론 | `DART_Corp_Mapping__c`(3,988건)·`DART_Setting__c` + `DartService`·`DartMatchService` + `DART_Lead_Convert_Match`·`DART_Account_Approved_Enrich` + Einstein Models API | 완료 (프로덕션 E2E, 인증키 Named Credential 이전 후속 검토) |
| Lead Scoring 설계·구현 | 혜준 | Lead 신규 필드 11종 + 기존 SDO Scoring 재사용, 100점 체계 + `Risk_Penalty__c` → `Final_Lead_Score__c` | 미표기 (대표 Lead 케이스 검증 진행) |
| PRM 360 Dashboard / Sales KPI / 업무 화면 | 혜준 | App `Cloud Alpacas PRM`, LWC 11종, Apex `PRM360Controller`·`PRM360SummaryController`, Report 11종, `PRM_Revenue_Target__c` | 미표기 (원천 데이터 ↔ 화면 값 일치 검증 진행) |
| PRM 360 분석 연계 (Tableau) | 혜준 | Tableau Next + C360 Semantic Model + Dashboard Embedding | 미표기 (집계 기준·수치 일치 확인 진행) |
| 스폰서십 상품 + 표준 견적 체계 | 승우 | `Product2.Sponsorship_Package` 21종 + Quote/QuoteLineItem + Quote Template + Revenue Schedule / Quote Sync | 완료 (d'Alba E2E, 21종 전체 회귀 테스트 권장) |
| 스폰서십 Campaign 생애주기·화면 구조 | 승우 | Campaign Record Type 3종(Prospecting/Collaboration/Renewal) + Path + List View 4종 + Hierarchy + 전용 Layout | 완료 (Prospecting 기존 Layout 유지) |
| Campaign 실행 과업 추적 + Slack 지연 알림 | 승우 | `Campaign_Deliverable__c` + Before/After-Save Flow 2종 + Slack `#campaign-alerts` | 완료 (7시나리오 검증, `Due_Date_Pushed__c` 정리 필요) |
| 갱신 캠페인 성과 자동 요약 | 승우 | `Renewal_Campaign_Performance_Summary` + `Campaign.Performance_Summary__c` + `RenewalSummaryRefresher` | 보완 필요 (Agent 미경유 직접 조회 경로 Flow 보완) |
| Campaign 예상 매출 자동 동기화 | 승우 | Flow 3종(생성·수정 / 삭제 / 공통 Subflow) → `Campaign.ExpectedRevenue` | 보완 필요 (Campaign 연결 A→B 변경 시 이전 Campaign 재계산 예외) |
| 스폰서십 Pipeline·Revenue 대시보드 | 승우 | Report 5종 + Dashboard 7위젯 + Net Profit Custom Summary Formula | 보완 필요 (Conversion Rate Formula 완료 여부·발표 전 재검증) |
| 소유권 이관·Opportunity 공유 | 아론 | Owner 이관 300건 + Public Group `Partnership_Team` + Sharing Rule + AccountPlan PS | 완료 |
| Partnership Inquiry Experience Cloud | 은영 | Lead + ContentVersion + `partnershipInquiry` LWC + `PartnershipInquiryController` + 사이트 `/CApartnership` | 보완 필요 (비로그인 제출 → Lead·파일 생성 재확인) |
| Zoom·Google Meet 연동 | 은영 | VideoCall / Conversation·Interaction Intelligence + 사용자 권한 세트 | 보완 필요 (녹화·대화 데이터 생성·Opportunity 자동 매칭 E2E) |

### Project / Data / Org

| Feature / Business Area | 담당자 | 구현 내용 | 상태 |
|---|---|---|---|
| 프로젝트 기획·Architecture·의사결정 | 사라 | `00~05` 문서, 5 Domain Model, Object Mapping, Phase 2 B2B Architecture, A~K Technical Decision, 30+ ADR | 완료 |
| 공용 Dummy Data 규칙 (Data Contract) | 사라 | Naming Rule, Cross-Object Consistency, `SCN-B2B-001`, Demo Data Owner, Data Freeze | 완료 |
| P2 Dummy Data Master (30명 + d'Alba) | 사라 | Fan 30명(6종×5), Fan Insight 계산 기준, d'Alba Sponsorship 시나리오 레코드 | 완료 (설계) |
| 60명 Pilot Cohort | 사라 | Account 60·Order 103·OrderItem 103·Admission 75·Engagement 20 생성 + 자동화 검증 + 인구통계/채널/동의 Backfill | 완료 |
| 5,000명 Target Demo Scale | 사라 | 헤드카운트 5,024건 확인 + 분포/Field QA 기준 정의 | 보완 필요 (분포·Field QA 미검증) |
| Fan Insight 화면 방식 (Report/Dashboard) | 사라 | Decision 018-J, Standard Report + Report Type + Dashboard | 완료 (결정) / Report 구성 진행 |
| Fan Insight → 팬덤 광고 가치 논리 | 사라 | Fan 360 Analytics → 팬층 변화 → 광고 가치 가설 → 기업 Matching 흐름 | 완료 (설계·문서) |
| 파트너십 샘플 데이터 구축 | 아론 | Account/Contact/Opportunity 각 100 + 5년 계약 이력 + Order·Asset·Contract·AccountPlan | 완료 |
| 디자인 시스템 (브랜드 컬러·CSS·아이콘) | 사라 | `#FC4E00`, 공용 `cloudAlpacas.css`, `icon` SVG LWC | 완료 |
| 이메일 발송 인프라 검증 | 사라 | SPF/DKIM 구조적 한계 규명 → Naver 데모 (Decision 025) | 완료 |
| Campaign Hub 조사 + Benefits 필드 | 사라 | 대상 0명 원인 규명(CampaignMember 생성 로직 부재) + `Benefits__c` 필드 5종 | 보완 필요 (Flow 로직 연결 Future Scope) |
| Demo 시나리오 (`04_DEMO`) | 사라 | Scene 1 Recommendation Agent / Scene 2 Live Fan Quiz 2장면 | 완료 |

---

## 4. 최종 산출물과 연결

| 최종 산출물 | 연결되는 팀 작업 (backlog 기준) |
|---|---|
| **프로젝트 기획서** | 사라 — `00_STORY`(Business Goal·Pain Point·Persona·Customer Journey), `CLAUDE.md`(프로젝트 철학·MVP 범위), Phase 2 B2B 방향 전환·발표 범위 재편 |
| **요구사항 정의서** | 사라 — `01_PROJECT`(Domain·Workflow·Entity), `03_SYSTEM`(MVP Implementation Matrix), `AGENT_SPEC`·`EVENT_SPEC` / Feature Owner별 `[Feature]`·`[Business Purpose]` 기록(승우·은영·혜준·아론 backlog) |
| **ERD** | 사라 — `03_SYSTEM §3`(Object 관계·ERD), 3축 데이터 모델 / 승우 — Fan 360 데이터 구조(Person Account 중심 12 Object), `Campaign_Deliverable__c` / 아론 — 파트너십 데이터 모델(RecordType·`SDO_Partner_Type__c`·`DART_Corp_Mapping__c`) / 혜준 — Lead Scoring 필드 구조, `PRM_Revenue_Target__c`·`Sales_Briefing__c` / 은영 — `Interaction_Intelligence__c`·`Interaction_Signal__c` |
| **프로세스 흐름도** | 사라 — `03_SYSTEM` Process/Data Flow, B2C→B2B 연결 흐름(Fan Insight → DART → Agentforce Matching → Lead → Opportunity → Contract) / 승우 — Campaign 생애주기(Prospecting→Collaboration→Renewal), Deliverable Blocked→Slack / 은영 — Opportunity Agent Router→Assistant 흐름 / 아론 — Lead 전환→DART 매칭→승인→보강 파이프라인 |
| **권한 설정 현황표** | 사라 — `VIP_Recommendation_Agent_Access`, `FRM_Manager_Access` / 승우 — `CA_Campaign_Agent_Access`, `CA_Opportunity_Agent_Access`, `Fan_App_API_Access`, Named Credential `CA_Agent_API_PerUser` / 은영 — `CA_Agent_API_PerUser`(Per-User OAuth), Client Credentials, Zoom·Meet 권한 세트 / 아론 — Owner 이관 300건, Public Group `Partnership_Team` + Opportunity Sharing Rule, AccountPlan PS, DART 필드 FLS PS / 혜준 — PRM 360 Record 접근·권한별 데이터 확인 |
| **커스텀 메타데이터 / Object·Field 정보** | 사라 — `Quiz_Entry__c`, `Fan_Campaign_Msg_Request__e`, `Recommendations__c`(Status·Sent_Date) / 승우 — `Campaign_Deliverable__c`(+필드 9), `Product2.Sponsorship_Package` RT, `PricebookEntry` 할인 필드 / 아론 — `DART_Corp_Mapping__c`, `DART_Setting__c`, `Sponsor_Tier__c` 외 등급/요약 필드 / 혜준 — `PRM_Revenue_Target__c`, `Sales_Briefing__c`, Lead 신규 필드 11종, `AI_Lead_Summary__c` / 은영 — `Interaction_Intelligence__c`, `Interaction_Signal__c` |
| **아키텍처 다이어그램** | 사라 — `03_SYSTEM §7` Phase 2 B2B Architecture Draft, System Architecture, Agent 아키텍처 표준(단일 실행 블록 + Apex 하드 가드) / 은영 — Opportunity Agent 오케스트레이션(Router + 역할별 Assistant) / 승우 — Sponsorship Campaign Agent Router + Subagent 구조 |
| **데모 / 발표 자료** | 사라 — `04_DEMO`(Scene 1 Recommendation Agent VIP Offer E2E / Scene 2 Live Fan Quiz 실시간 응모·추첨·Reveal), `HANDOFF_SESSION_SUMMARY` / 승우 — d'Alba Product→Quote→PDF E2E / 아론 — 파트너십 샘플 데이터 5년치(갱신율·N년차 파트너 시연) / 혜준 — PRM 360 Dashboard 데모 화면 / 은영 — Opportunity 업무 화면·Agent 채팅 데모 |

---

## 5. 프로젝트 전체 흐름

팀 전체 작업은 아래 순서로 하나의 프로젝트로 연결된다.

```
기획 (사라)
  Business Goal · Persona · Domain Model · Salesforce Architecture · 의사결정(ADR)
        │
        ▼
Data / Org (사라 · 아론 · 승우)
  공용 Dummy Data 규칙 · Pilot Cohort · 파트너십 샘플 데이터 ·
  RecordType/Permission/Sharing 정비 · Fan 360 데이터 모델
        │
        ▼
B2C Fan Relationship (승우 · 은영 · 사라)
  팬 행동 기반 Engagement Flow · 3축 계산 Flow · 추천 세그먼트 ·
  캠페인 반응·전환 추적 · Fan App 연동
        │
        ▼
Fan Insight (사라)
  Fan 360 데이터 → 팬층 변화 → 팬덤 광고 가치 → 기업 Matching 근거
        │
        ▼
Recommendation / Agentforce / Automation (사라 · 은영 · 승우 · 혜준 · 아론)
  Recommendation 검수·발송 + VIP Recommendation Agent ·
  Opportunity Agent(+Proposal·Negotiation 서브에이전트) ·
  Sponsorship Campaign Agent · Lead AI Summary · Stage Guidance · Sales Briefing ·
  Slack 지연 알림 · Campaign 예상 매출 동기화
        │
        ▼
B2B Sponsorship Sales (아론 · 혜준 · 승우 · 은영)
  파트너십 데이터 모델 · Lead Scoring · DART 공시 자동보강 ·
  Sponsorship Package·Quote · Campaign 생애주기 · Opportunity 파이프라인
        │
        ▼
UX / Demo (사라 · 혜준 · 은영 · 승우)
  Fan 360 Landing·Fan List · PRM 360 Dashboard · Pipeline·Revenue 대시보드 ·
  Opportunity 업무 화면 · 디자인 시스템 · Live Fan Quiz · Demo 시나리오
        │
        ▼
QA (전원 Feature QA / 사라 Integration·E2E 검수)
        │
        ▼
Final Deliverables (사라 문서 · 전원 backlog 기록)
  기획서 · 요구사항 정의서 · ERD · 프로세스 흐름도 ·
  권한 현황표 · 커스텀 Object/Field 정보 · 아키텍처 다이어그램 · 데모 자료
```

---

## 자체 검수 (팀원 파일 ↔ 06_backlog 대조)

| 팀원 파일 | 반영 여부 | 확인 |
|---|---|---|
| `sara.md` (13 카테고리) | ✅ | §2 사라 표에 기획/Architecture/Object/Flow/Apex/LWC/Agentforce/Data/UX/QA/Documentation 전 항목 반영. §3 B2C·Agentforce·Project/Data/Org 표, §4 8개 산출물 전부 연결 |
| `seungwoo.md` (B2B 8건 + B2C 4건) | ✅ | B2B: Sponsorship Campaign Agent / Campaign Deliverable+Slack / 갱신 성과 요약 / Proposal·Quote Subagent / Sponsorship Package·Quote / Campaign 예상 매출 동기화 / Campaign 생애주기·화면 / Pipeline·Revenue 대시보드 — 8건 모두 §2·§3 반영. B2C: Fan 360 데이터 모델 / Engagement Flow 6종 / Fan App API / 캠페인 전환 추적 — 4건 모두 반영 |
| `eunyeong.md` (B2B 9건 + B2C 4건) | ✅ | B2B: Opportunity Agent / Stage Guidance / Activity Assistant+Interaction Intelligence / Proposal·Negotiation 통합 / Similar Closed Won / 내장 채팅 / Opportunity 업무 화면 / Zoom·Meet / Partnership Inquiry — 9건 모두 반영. B2C: 추천 세그먼트+Fan 360 / Fan App 연동 / 캠페인 실시간 성과 / Fan App 구매·체크인 UX — 4건 모두 반영 |
| `hyejune.md` (B2B 7건) | ✅ | PRM 360 Dashboard 기획·화면 / Sales KPI / 영업 업무·우선순위 / Sales Briefing / Lead Scoring / Lead AI Summary+Task 자동화 / PRM 360 분석 연계(Tableau) — 7건 모두 §2·§3 반영. LWC 12종·Apex 4종·Report 11종·Lead 신규 필드 11종 명시. (B2C 항목은 원본에 없음 — 추가하지 않음) |
| `aaron.md` (B2B 10건) | ✅ | 파트너십 데이터 모델·RecordType / 계정·스폰서 리스트뷰 / 계정 레코드 화면+추이 그래프 / 파트너 연락처 리스트뷰 / 스폰서 등급 자동 산정 Flow / 계정 요약필드 동기화 Flow / DART 공시 자동보강 / Negotiation 서브에이전트 / 소유권 이관·공유 / 파트너십 샘플 데이터 — 10건 모두 반영 |

**누락 팀원**: 없음 (사라·승우·은영·혜준·아론 5명 전원 §2 개별 표 + §3 기능 표 + §4 산출물 연결).

**누락 주요 작업 점검**:
- Agentforce 관련 5개 Agent(VIP Recommendation / Opportunity / Sponsorship Campaign / Proposal Assistant / Negotiation 서브에이전트) 및 AI 기능 2종(Lead AI Summary / Sales Briefing) — 모두 §1-D, §3, §4 반영.
- DART OpenDART API 연동(아론), Fan App REST API(승우·은영), Slack 알림(승우·사라), Zoom·Google Meet(은영), Experience Cloud 2종(`/CApartnership` 은영 · Live Fan Quiz 사이트 사라) — 모두 §1-F, §3 반영.
- 데이터 구축 3종(사라 Pilot Cohort / 아론 파트너십 샘플 / 사라 P2 Dummy Data Master) — §1-H, §3, §4 반영.
- 팀원 간 중복·경계가 명시된 항목(Proposal·Negotiation Assistant = 최초 개발자와 통합 담당자 분리 / Fan 행동 Engagement Flow = 승우 구축·사라 수정 / 동명 Proposal Apex 소유권 정리 필요)은 원본 표현 그대로 담당자를 병기.

