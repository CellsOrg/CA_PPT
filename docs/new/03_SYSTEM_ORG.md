# 03_SYSTEM_ORG — Cloud Alpacas 실제 Org 구현 시스템

> **Source of Truth: Salesforce Org Metadata — 2026-08-31**
> Org: `cloud-alpacas` (`00Dbm00000tkYqDEAU`, Enterprise Edition, Production, API 62–67).
> 조회 방법: Tooling API SELECT + `sf sobject describe` + `sf project retrieve` (모두 read-only, 변경 없음).
>
> 이 문서는 **"현재 Org에 실제로 구현되어 있는 Cloud Alpacas 시스템"** 만 설명한다.
> 기존 `CloudAlpacas/docs/*` 는 비교·참고용이며 이 문서의 근거가 아니다. 차이는 `ORG_VS_DOCUMENT_GAP.md` 에 별도 기록한다.
> 표기: **Org Actual** = Org에서 직접 확인. `CreatedBy` = 최초 생성자(사람), 역할 ≠ 생성자.
> 팀원 매핑: Sara Bang · Eunyeong Doh · Hyejune Jo · Aaron Choi · **Rafael Espada = Seungwoo(승우)** · Seongbin An(제작 이력 없음).
>
> **Rev.2 정정 (2026-08-31, deliverables 작업 중 재검증):**
> ① `DART_Setting__c` 는 Custom **Object 가 아니라 Hierarchy Custom Setting** 이다 (`DartService` 가 `getOrgDefaults()` 사용, `<customSettingsType>Hierarchy</customSettingsType>` 확인). → 팀 Custom Object 는 **18개 → 17개**, Custom Setting **1개** 추가.
> ② `DART_Corp_Mapping__c` 는 커스텀 field **4개** 보유: `Corp_Code__c`, `Corp_Name__c`, `Corp_Name_Eng__c`, `Stock_Code__c` (초판의 "field 0개"는 오조회).
> ③ DART 연동 = Apex HTTP callout → `https://opendart.fss.or.kr` (RemoteSiteSetting `opendart_fss`, 활성), 인증키는 `DART_Setting__c.Api_Key__c`.
> ④ NamedCredential `CA_Agent_API` (→ `https://api.salesforce.com`, ExternalCredential `CA_Agent_API_Cred`) = Agentforce/Agent API 호출용.

---

## 1. System Overview

Cloud Alpacas Org는 Salesforce 데모(SDO/QBrix) org 위에 팀이 2026-08-11 ~ 08-31 사이 구축한 **B2C Fan 360 + B2B Sponsorship** 통합 CRM이다.

| 구분 | Org Actual |
|---|---|
| 관리형 패키지 | 55개 (FSL, Salesforce Maps, Pardot, Marketing Cloud, Sales Planning, Slack, Quip 등) |
| CustomObject (무네임스페이스) | 149개 중 **팀 제작 17개 (+ Custom Setting `DART_Setting__c`)** (나머지 132개 = SDO/QBrix 데모 스캐폴딩) |
| 팀 제작 자산 | Custom Object **17** · Custom Setting 1 · 팀 Custom Field ~230(유효분) · Active Flow 40 · Apex Class 100 · Apex Trigger 1 · LWC 46 · Agentforce Planner 5종 · Prompt Template 6 · RecordType 12 |
| Person Account | 활성화됨 (`Fan` RecordType 사용) |
| 아키텍처 성격 | **Flow 중심 자동화** + LWC 커스텀 UI + Agentforce(Opportunity/Recommendation 계열) + 외부 연동(DART OpenAPI, Slack) |

시스템은 3개 영역으로 나뉜다.

1. **B2C Fan 360** — 팬(Person Account) 데이터를 통합해 세그먼트·활동패턴·추천·혜택·알림을 운영.
2. **B2B Sales / Sponsorship** — 기업 데이터(DART) → Lead → Opportunity → Campaign(스폰서십) 파이프라인.
3. **Supporting / AI / Intelligence** — Agentforce 에이전트 5종, Prompt Template 6종, Interaction Intelligence, Sales Briefing 등 판단 보조 계층.

---

## 2. Domain / Object Map

### 2.1 B2C Fan 360

| Layer | Object | 종류 |
|---|---|---|
| 주체 | `Account` (RT `Fan`, Person Account) · `Contact` (RT `Player`) | Standard |
| 시즌·경기 | `Season__c` · `Game__c` | Custom |
| 입장·관람 | `Admission__c` · `Attendance_Record__c` | Custom |
| 거래 | `Order` · `OrderItem` · `Product2`(RT `Ticket`/`Season_Pass`/`Membership`/`Goods`) · `Pricebook2` · `PricebookEntry` | Standard |
| 관심·분석 | `Engagement_Signal__c` · `Fan_Activity_Pattern__c` · `Fan_Segment_History__c` | Custom |
| 실행 | `Recommendations__c` · `Benefits__c` · `Notification_Log__c` | Custom |
| 마케팅 | `Campaign`(RT `Fan_Campaign`) · `CampaignMember` | Standard |
| 서비스 | `Case`(RT `Fan_Case`) | Standard |
| 이벤트(P1) | `Quiz_Entry__c` | Custom |

### 2.2 B2B Sales / Sponsorship

| Layer | Object | 종류 |
|---|---|---|
| 기업 데이터 | `DART_Corp_Mapping__c` (Custom Object) · `DART_Setting__c` (Custom **Setting**) | Custom |
| 발굴 | `Lead` (RT `SDO_Lead_Default`, `Lead_Partner_Application`) | Standard |
| 기업/담당자 | `Account` (RT `Business_Account`) · `Contact` (RT `Partner_Contact`) | Standard |
| 딜 | `Opportunity` (RT `SimpleOpportunity`, `ChannelPartner`) · `OpportunityLineItem` · `Product2`(RT `Sponsorship_Package`) | Standard |
| 스폰서십 캠페인 | `Campaign` (RT `Sponsorship_Collaboration`/`Sponsorship_Prospecting`/`Sponsorship_Renewal`) · `Campaign_Deliverable__c` | Standard + Custom |
| 계정 계획 | `AccountPlan` (표준, Aaron 08-31 신규) | Standard |
| PRM 파트너 포털 | `Sales_Briefing__c` · `PRM_Revenue_Target__c` | Custom |

### 2.3 Supporting / AI / Intelligence

| 항목 | Object / Metadata | 종류 |
|---|---|---|
| 미팅 인텔리전스 | `Interaction_Intelligence__c` · `Interaction_Signal__c` | Custom |
| 이벤트 트리거 | `Fan_Campaign_Msg_Request__e` | Platform Event |
| Agentforce | GenAiPlannerDefinition 5종 (§7) | Metadata |
| Prompt Builder | GenAiPromptTemplate 6종 (§7) | Metadata |

---

## 3. Object별 역할 (Custom Object 17)

> 관계 표기: **MD** = Master-Detail(cascade delete). **L!** = 필수 Lookup(restrict delete, MD 유사). **L** = 선택 Lookup.
> Name 필드: 별도 표기 없으면 **AutoNumber**.

### B2C Fan 360

| # | Object / API | 주요 Field | 관계 | 실제 사용 목적 |
|---|---|---|---|---|
| 1 | Season / `Season__c` (Name=Text) | `Start_Date__c`, `End_Date__c`, `Total_Games__c`, `Played_Games__c` | (부모) `Game__c` MD, `Fan_Activity_Pattern__c` L | 시즌 단위 경기·활동 집계 기준 |
| 2 | Game / `Game__c` | `Game_Date__c`, `Opponent__c`, `Result__c`, `Status__c`, `Home_Away__c`, `External_ID__c`(uniq) | `Season__c` **MD** · (부모) `Admission__c` | 경기 마스터. 티켓 주문·입장의 기준 |
| 3 | Admission / `Admission__c` | `Admission_Time__c`(req), `Gate__c`, `External_ID__c`(uniq) | `Attendance_Record__c` **MD** · `Fan__c`→Account **L!** · `Game__c`→Game **L!** · `Order_Item__c`→OrderItem **L!** | 개별 입장 1건(“언제/어느 게이트로 들어왔나”) |
| 4 | Attendance Record / `Attendance_Record__c` | `Total_Admissions__c`, `First_Admission_Date__c`, `Last_Admission_Date__c`, `External_ID__c`(uniq) | `Fan__c`→Account **L!** · (부모) `Admission__c` MD | 팬별 누적 관람 집계(운영상 팬당 1건, 스키마상 강제 아님). Admission을 MD 롤업 |
| 5 | Engagement Signal / `Engagement_Signal__c` | `Signal_Type__c`, `Source__c`, `Signal_Date__c`, `External_ID__c`(uniq) | `Fan__c`→Account **L!** · `Player__c`→Contact **L** | 구매 이전 관심 신호(SNS 반응 등) |
| 6 | Fan Activity Pattern / `Fan_Activity_Pattern__c` | `Games_Attended__c`, `Attendance_Rate__c`, `Goods_Purchases__c`, `Total_Spend__c`, `Analyzed_Date__c` | `Fan__c`→Account **L!** · `Season__c`→Season **L** | 시즌별 활동 패턴 분석 결과 |
| 7 | Fan Segment History / `Fan_Segment_History__c` | `Segment__c`(req), `Changed_Date__c`, `Reason__c`, `External_ID__c`(uniq) | `Fan__c`→Account **L!** | 세그먼트 변경 이력(시점 기록) |
| 8 | **Fan Recommendation** / `Recommendations__c` | `Recommended_Action__c`(req), `Status__c`(req), `Reason__c`, `Personalized_Message__c`, `Sent_Date__c`, `External_ID__c`(uniq) | `Fan__c`→Account **L!** · `Campaign__c`→Campaign **L** · (부모) `Benefits__c` | Next Best Action 추천 결과. VIP Recommendation Agent 산출물 |
| 9 | Benefits / `Benefits__c` | `Benefit_Type__c`(req), `Status__c`(req), `Issued_Date__c`, `Used_Date__c`, `Expiration_Date__c`, `Discount_Rate__c`, `Min_Purchase_Amount__c`, `Badge_Label__c`, `External_ID__c`(uniq) | `Fan__c`→Account **L!** · `Recommendations__c`→Recommendation **L** | 팬에게 발급된 쿠폰·할인·혜택. 사용 여부는 `Status__c`/`Used_Date__c` |
| 10 | Notification Log / `Notification_Log__c` | `Channel__c`, `Content__c`, `Sent_Date__c`, `External_ID__c`(uniq) | `Fan__c`→Account **L!** · `Campaign__c`→Campaign **L** | 팬에게 보낸 개인화 안내 이력 (Fan Timeline 원천) |
| 11 | Quiz Entry / `Quiz_Entry__c` (Name=Text) | `Entrant_Name__c`, `Selected_Answer__c`, `Is_Correct__c`, `Is_Winner__c` | 관계 없음 | 발표 참여 이벤트 응모 저장(Experience Site) |

### B2B Sales / Sponsorship

| # | Object / API | 주요 Field | 관계 | 실제 사용 목적 |
|---|---|---|---|---|
| 12 | Campaign Deliverable / `Campaign_Deliverable__c` | `Status__c`(req), `Weight__c`(req), `Due_Date__c`, `Completed_Date__c`, `Evidence_URL__c`, `Blocked_Reason__c`, `Due_Date_Pushed__c`, `Pending_Slack_Message__c` | `Campaign__c`→Campaign **MD** | 스폰서십 캠페인 이행 항목. 가중치로 진행률 롤업, 지연 시 Slack 알림 |
| 13 | Interaction Intelligence / `Interaction_Intelligence__c` | `Summary__c`, `Key_Decision__c`, `Concerns_Objections__c`, `Customer_Reaction__c`, `Follow_Up__c`, `Source_Type__c`(req), `Source_Record_Id__c`(uniq req) | `Opportunity__c`→Opportunity **L** · (부모) `Interaction_Signal__c` | 미팅/통화 내용을 AI가 구조화한 결과. `Source_Record_Id__c`로 원본 Task/Event 참조(다형) |
| 14 | Interaction Signal / `Interaction_Signal__c` | `Signal_Category__c`(req), `Signal_Type__c`(req), `Direction__c`(req), `Confidence__c`(req), `Evidence__c` | `Interaction_Intelligence__c` **MD** | 인텔리전스에서 추출한 개별 신호(관심/우려/결정 등) |
| 15 | Sales Briefing / `Sales_Briefing__c` | `Briefing_Date__c`(req), `Briefing_Key__c`(uniq), `Briefing_Text__c` | `User__c`→User **L** | 파트너 담당자별 일일 세일즈 브리핑(스케줄러가 생성) |
| 16 | PRM Revenue Target / `PRM_Revenue_Target__c` (Name=Text) | `Target_Amount__c` | 관계 없음 | 파트너 매출 목표. **관계 미구현 — Season/User 연결 검토 필요** |
| 17 | DART 기업 매핑 / `DART_Corp_Mapping__c` (Name=Text) | `Corp_Code__c`, `Corp_Name__c`, `Corp_Name_Eng__c`, `Stock_Code__c` (Rev.2 정정) | 명시적 FK 없음 | DART OpenAPI 기업코드 ↔ 종목코드/기업명 매핑 테이블. Flow가 `Account.DART_*` 필드로 매칭 |

> ~~18. `DART_Setting__c`~~ → **Custom Setting 으로 재분류 (Rev.2).** `03_CUSTOM_METADATA.md` 참조. 팀 Custom Object = **17개**.

### Object 아님 (혼동 주의)

| 이름 | 실제 정체 | 비고 |
|---|---|---|
| `Fan_Campaign_Msg_Request__e` | **Platform Event** (Sara 08-26) | Fan Campaign 개인화 메시지 생성 트리거. Flow `Fan Campaign Personalized Msg Flow`가 구독 |
| `Recommendation__c` (단수) | **존재하지 않음** | Tooling `CustomObject` phantom row(Rafael 08-12). `EntityDefinition`·`describe` 실패. 실사용은 `Recommendations__c` |
| `User__c` | **존재하지 않음** | phantom row(Rafael 08-11). Staff는 표준 `User` |
| `Recommendation` (표준) | Einstein/NBA 표준 Object | 팀 미사용 |

---

## 4. Standard Object Customization

> `_del__c` / `_tc__*` / `ZZ_Diag*` / `CA_Diag*` (폐기·진단 잔재 ~25개) 제외.

| Object | CA 필드 수 | 주요 필드 | RecordType (팀) |
|---|---|---|---|
| **Account** | 37 | **Fan:** `Current_Segment__c`, `Engagement_Level__c`, `Engagement_Score__c`, `Fan_Value_Tier__c`, `Favorite_Player__c`(→Contact L), `Acquisition_Channel__c`, `Email/SMS/Kakao/Push_Opt_In__c`, `Consent_Updated_Date__c`, `Segment_Updated_Date__c`, `Age_Group_c__c`(Formula), `Report_Gender__c`(Formula), `Fan_Join_Date__c`, `Membership_Status__c` <br> **B2B/DART:** `Business_Reg_No__c`, `Corp_Name_Eng__c`, `Stock_Code__c`, `Market_Type__c`, `Operating_Profit__c`, `Total_Assets__c`, `DART_Match_Status__c`, `DART_Enriched_At__c`, `Match_Confidence__c`, `Match_Rationale__c`, `Sponsor_Tier__c`, `Total_Sponsorship_Value__c`, `Sponsorship_Opportunity_Count__c`, `Latest_Open_Opportunity_{Amount/Stage/Next_Step}__c` | `Fan`(Rafael), `Own_Organization`(Sara) |
| **Contact** | 5 | `Position__c`, `Uniform_Number__c` (Player), `Name_EN__c`, `SDO_PRM_Region__c`, `SDO_PRM_Service_Delivery__c` | `Player`(Rafael) |
| **Lead** | 18 (전부 Hyejune) | `Lead_Score__c`, `Final_Lead_Score__c`, `Score_{Industry/Interest/LeadSource/Region/Sponsorship}__c`, `Risk_Penalty__c`, `Segment_Match__c`, `Target_Segment__c`, `Regional_Connection__c`, `Competitor_Sponsor__c`, `Controversial_Industry__c`, `Sponsorship_History__c`, `Company_Phone__c`, `Department__c`, `Recommendation_Reason__c`, `AI_Lead_Summary__c` | — |
| **Opportunity** | 41 (Eunyeong 중심) | `Last_Contact_{Date/Type}__c`, `Days_Since_Last_Contact__c`, `Next_Activity_{Subject/Date}__c`, `Open/Overdue_Tasks_Count__c`, `Expected_Benefit_{Short/Mid/Long}_Term__c`, `Brand_Fan_Fit__c`, `Client_Budget__c`, `Client_Budget_Status__c`, `Customer_KPI__c`, `Customer_Needs__c`, `Key_Requirements__c`, `Target_Segment__c`, `Target_Start_Season__c`, `Sponsorship_Interest_Level__c`, `Expected_Timing__c`, `Decision_Maker_Accessible__c`, `Contract_{Start/End}_Date__c`, `Primary_Contact_{Email/Phone}__c`, `Partner_Tier__c`(Rafael) | `SimpleOpportunity`, `ChannelPartner` (둘 다 SDO 생성) |
| **Campaign** | 3 실사용 | `Total_Deliverable_Weight__c`(Roll-Up), `Completed_Deliverable_Weight__c`(Roll-Up), `Performance_Summary__c` | `Fan_Campaign`(Sara), `Sponsorship_Collaboration`/`_Prospecting`/`_Renewal`(Rafael) |
| **CampaignMember** | 1 | `Is_Converted__c` | — |
| **Product2** | 4 실사용 | `Category__c`, `Tier__c`, `Related_Player__c`(→Contact L), `Is_Player_Goods__c` | `Ticket`/`Season_Pass`/`Membership`/`Goods`/`Sponsorship_Package` (전부 Rafael) |
| **Order** | 9 (전부 Rafael) | `Game__c`(→Game__c L), `Order_Type__c`, `Payment_Status__c`, `Purchase_Channel__c`, `Membership_Status__c`, `Coverage_{Start/End}_Date__c`, `Refund_{Date/Reason}__c` | `SDO_Order_Consumer`/`SDO_Order_Business` (SDO) |
| **OrderItem** | 5 (전부 Rafael) | `Current_Owner__c`(→Account L, 티켓 양도), `Seat_Number__c`, `Row__c`, `Section__c`, `Transfer_Status__c` | — |
| **Case** | 1 | `Related_Order__c`(→Order L) | `Fan_Case`(Sara) |
| **PricebookEntry** | 1 실사용 | `Max_Discount_Percent__c`, `Max_Discounted_Price__c` | — |
| **Activity** (Task/Event) | 6 (Eunyeong) | `Meeting_Type__c`, `Key_Discussion__c`, `Key_Decision__c`, `Concerns_Objections__c`, `Customer_Reaction__c`, `Follow_up__c` | — |
| **AccountPlan** (표준) | 14 (Aaron, 08-31) | `Sponsorship_Tier__c`, `Annual_Sponsorship_Value__c`, `Renewal_Date__c`, `Champion_Contact__c`, `Primary_Contact__c`, `Key_Decision_Makers__c`, `Company_Overview__c`, `Our_Positioning__c`, `Potential_Needs__c`, `Exposure_Channels__c`, `Relationship_Strategy__c`, `Resource_Allocation__c`, `Pipeline_Notes__c`, `Action_Plan__c` | — (표준 기능 활성 상태 확인 필요) |
| **Benefit** (표준) | 3 (Sara, 08-28) | `Badge_Label__c`, `Discount_Rate__c`, `Min_Purchase_Amount__c` | — **⚠️ 커스텀 `Benefits__c`와 중복 필드** |

---

## 5. 주요 Relationship

### 5.1 B2C Fan 360

| From (Child) | Field | To (Parent) | Type | Cardinality |
|---|---|---|---|---|
| `Game__c` | `Season__c` | `Season__c` | Master-Detail | N:1 |
| `Admission__c` | `Attendance_Record__c` | `Attendance_Record__c` | Master-Detail | N:1 |
| `Admission__c` | `Fan__c` | `Account` (Fan) | Lookup (req, restrict) | N:1 |
| `Admission__c` | `Game__c` | `Game__c` | Lookup (req, restrict) | N:1 |
| `Admission__c` | `Order_Item__c` | `OrderItem` | Lookup (req, restrict) | N:1 |
| `Attendance_Record__c` | `Fan__c` | `Account` (Fan) | Lookup (req, restrict) | N:1 (운영상 1:1) |
| `Engagement_Signal__c` | `Fan__c` | `Account` (Fan) | Lookup (req, restrict) | N:1 |
| `Engagement_Signal__c` | `Player__c` | `Contact` (Player) | Lookup | N:1 |
| `Fan_Activity_Pattern__c` | `Fan__c` | `Account` (Fan) | Lookup (req, restrict) | N:1 |
| `Fan_Activity_Pattern__c` | `Season__c` | `Season__c` | Lookup | N:1 |
| `Fan_Segment_History__c` | `Fan__c` | `Account` (Fan) | Lookup (req, restrict) | N:1 |
| `Recommendations__c` | `Fan__c` | `Account` (Fan) | Lookup (req, restrict) | N:1 |
| `Recommendations__c` | `Campaign__c` | `Campaign` | Lookup | N:1 |
| `Benefits__c` | `Fan__c` | `Account` (Fan) | Lookup (req, restrict) | N:1 |
| `Benefits__c` | `Recommendations__c` | `Recommendations__c` | Lookup | N:1 |
| `Notification_Log__c` | `Fan__c` | `Account` (Fan) | Lookup (req, restrict) | N:1 |
| `Notification_Log__c` | `Campaign__c` | `Campaign` | Lookup | N:1 |
| `Account` (Fan) | `Favorite_Player__c` | `Contact` (Player) | Lookup | N:1 |
| `Order` | `AccountId` | `Account` (Fan) | Lookup (표준) | N:1 |
| `Order` | `Game__c` | `Game__c` | Lookup | N:1 |
| `OrderItem` | `OrderId` | `Order` | Master-Detail (표준) | N:1 |
| `OrderItem` | `Current_Owner__c` | `Account` (Fan) | Lookup | N:1 |
| `OrderItem` | `PricebookEntryId` → `Product2Id` | `Product2` | Lookup (표준) | N:1 |
| `Case` | `Related_Order__c` | `Order` | Lookup | N:1 |
| `CampaignMember` | `CampaignId` / `ContactId`/`LeadId` | `Campaign` / `Account`·`Contact`·`Lead` | 표준 정션 | N:1 |

### 5.2 B2B Sales / Sponsorship

| From (Child) | Field | To (Parent) | Type | Cardinality |
|---|---|---|---|---|
| `Opportunity` | `AccountId` | `Account` (Business) | Lookup (표준) | N:1 |
| `OpportunityLineItem` | `OpportunityId` | `Opportunity` | Master-Detail (표준) | N:1 |
| `OpportunityLineItem` | `Product2Id` | `Product2` (Sponsorship Package) | Lookup (표준) | N:1 |
| `Interaction_Intelligence__c` | `Opportunity__c` | `Opportunity` | Lookup | N:1 |
| `Interaction_Signal__c` | `Interaction_Intelligence__c` | `Interaction_Intelligence__c` | Master-Detail | N:1 |
| `Campaign_Deliverable__c` | `Campaign__c` | `Campaign` (Sponsorship) | Master-Detail | N:1 |
| `Sales_Briefing__c` | `User__c` | `User` | Lookup | N:1 |
| `Lead` | (convert) | `Account` / `Contact` / `Opportunity` | 표준 Lead 전환 | 1:1 |
| `DART_Corp_Mapping__c` | (FK 없음) | `Account` (논리적) | — | — |

---

## 6. Automation

### 6.1 Flow (Active, 팀 제작 40)

| 담당(Created) | Flow | Type / Trigger | 시스템 역할 |
|---|---|---|---|
| Sara | Admission Created | AutoLaunched · RecordAfterSave `Admission__c` | 입장 발생 시 Attendance Record·Activity Pattern 갱신 트리거 |
| Sara | Fan Value Calc / Start Fan Engagement Calc | AutoLaunched (Account) | Fan Value Tier / Engagement Score 재계산 |
| Sara | Count_Goods_And_Season | AutoLaunched | 굿즈·시즌 관련 카운트 집계 |
| Sara | Fan Activity Pattern Admission Update | AutoLaunched (`Fan_Activity_Pattern__c`) | 입장 기반 활동패턴 필드 업데이트 |
| Sara | Order Paid / Order Membership Status Sync | AutoLaunched (Order) | 결제 완료 처리, 멤버십 상태 동기화 |
| Sara | Start Upsert Flow | AutoLaunched | 외부(Fan App) 데이터 upsert 진입점 (`External_ID__c` 키) |
| Sara | Welcome / First Visit Guide / First Ticket / First Merchandise / Favorite Player Campaign Flow -CA | AutoLaunched (Campaign) | Fan 여정 단계별 캠페인 자동 편성 |
| Sara | VIP Candidate Detection Flow -CA | AutoLaunched (`Recommendations__c`) | VIP 후보 감지 → 추천 레코드 생성 |
| Sara | Fan Campaign Personalized Msg Flow | AutoLaunched · Platform Event `Fan_Campaign_Msg_Request__e` | 개인화 메시지 생성 요청 처리 |
| Sara | Generate AI Recommendation Message | AutoLaunched | Prompt Template `Fan_Personalized_Message` 호출 → `Personalized_Message__c` |
| Sara | Quiz Entry 정답 자동 판정 | AutoLaunched (`Quiz_Entry__c`) | 응모 정답/당첨 판정 |
| Eunyeong | CA Update Opportunity Last Contact From Call/Email/Meeting | AutoLaunched · RecordAfterSave (Task/Event) | 활동 저장 시 Opportunity 최근 접촉 필드 갱신 |
| Eunyeong | CA Update Opportunity Next Activity (+ On Delete) | AutoLaunched · RecordAfterSave/BeforeDelete (Task) | 다음 활동 요약 필드 유지 |
| Eunyeong | CA Create Opportunity Activity | AutoLaunched (Opportunity) | Opportunity에서 활동 생성 |
| Eunyeong | CA Generate Meeting Interaction Intelligence | AutoLaunched · RecordAfterSave (Event) | 미팅 → `Interaction_Intelligence__c` 생성 (Prompt 호출) |
| Eunyeong | CA Generate Stage Guidance | AutoLaunched (Opportunity) | 단계별 가이던스 생성 (Prompt `CA_Stage_Guidance_Recommendation`) |
| Rafael | Campaign 예상 매출 계산 / 동기화 / 동기화(Opp 삭제 시) | AutoLaunched (Campaign/Opportunity) | 스폰서십 캠페인 예상 매출 롤업 |
| Rafael | 갱신 캠페인 성과 요약 자동 생성 | AutoLaunched (Campaign RT `Sponsorship_Renewal`) | Prompt로 성과 요약 텍스트 생성 |
| Rafael | Campaign Deliverable Blocked Slack Alert | AutoLaunched · RecordAfterSave (`Campaign_Deliverable__c`) | Blocked 상태 → Slack 알림 |
| Rafael | Campaign Deliverable Detect Due Date Push | AutoLaunched · RecordBeforeSave | 마감 임박 감지 플래그 |
| Aaron | DART Lead 전환 AI매칭 | AutoLaunched (Lead) | Lead 전환 시 DART 기업 데이터 매칭 |
| Aaron | DART 승인 보강 | AutoLaunched (Account) | 승인 시 기업 정보 enrichment |
| Aaron | Rollup Sponsorship To Account (+ On Delete) | AutoLaunched (Opportunity→Account) | 스폰서십 총액·건수 롤업 |
| Aaron | Sync Account Latest Open Opportunity | AutoLaunched (Opportunity→Account) | Account에 최신 Open Opp 요약 |
| Hyejune | 계약서 생성 Flow | AutoLaunched (Opportunity) | 계약서 문서 생성 |
| Hyejune | 고득점 리드 연락 Flow | AutoLaunched (Lead) | Lead Score 임계 초과 시 후속 |
| Hyejune | 협상 후속 연락 Flow | AutoLaunched (Opportunity) | 협상 단계 후속 |

> 전체 Active Flow 308개 중 268개는 데모/패키지 소유. 위 40개만 CA 구현.
> 자동화는 대부분 **AutoLaunched (record-triggered)** — 별도 Trigger 프레임워크 없음.

### 6.2 Apex (Class 100, Trigger 1)

| 도메인 | 대표 클래스 | 시스템 역할 |
|---|---|---|
| Fan 360 UI Controller | `Fan360Controller`, `Fan360LandingController`, `FanDetailController`, `FanListController`, `GameDetailController`, `ReportController` | LWC(`@AuraEnabled cacheable`) 데이터 제공 |
| Fan Segmentation | `SegmentDecliningVisits`, `SegmentMembershipCompleted`, `SegmentNoGoodsLoyal`, `SegmentNoVisitAfterSignup`, `SegmentFanListItem` | 세그먼트별 팬 목록 계산 |
| Recommendation / VIP | `RecommendationSegmentController`, `RecommendationReviewController`, `ApproveRecommendationAction`, `SendRecommendationEmailAction`, `GetPendingVipRecommendationsAction`, `RecommendationActionLabels` | 추천 생성·검토·승인·발송. 뒤 3개는 Agent Invocable |
| Interaction Intelligence | `ActivityIntelligenceController`, `ActivityIntelligenceAgentAction`, `InteractionIntelligenceParser`, `ConversationHistoryAgentAction` | 미팅 파싱, Agent Action |
| Opportunity Agent / Stage Guidance | `OpportunityAgentChatController`, `OpportunityStageGuidance`, `StageGuidanceController`, `DealContext`, `FindSimilarClosedDeals`, `FindActivityAttendee` | Opportunity Agent 컨텍스트·툴 |
| Negotiation | `NegotiationContext(+Controller)`, `NegotiationTermsUpdater`, `NegotiationOpportunityLookup` | 협상 컨텍스트/조건 갱신 |
| Sponsorship Proposal | `OpportunityProposalContext`, `SponsorshipPackageLookup`, `SponsorshipProposalSaver`, `FindSponsorshipPackage` | 제안서 생성 |
| Campaign Agent | `CampaignAgentChatController`, `CampaignBottleneckFinder`, `CampaignMitigationRecorder`, `RenewalSummaryRefresher` | 스폰서십 캠페인 병목/갱신 |
| DART 연동 | `DartService`, `DartMatchService`, `DartEnrichmentInvocable`, `DartEnrichmentQueueable`, `DartMatchInvocable`, `DartMatchQueueable`, `DartHttpMock` | DART OpenAPI 호출·매칭·비동기 enrichment |
| PRM 포털 | `PRM360Controller`, `PRM360SummaryController`, `PRM360SalesBriefingScheduler`, `LeadAiSummaryController`, `CheckWeather`, `WeatherService`, `CurrentDate` | 파트너 포털 위젯, 스케줄 브리핑 |
| Quiz / Experience Site | `QuizEntrySubmitController`, `LiveFanQuizRevealController`, `LightningSelfRegisterController`, `LightningLoginFormController`, `LightningForgotPasswordController` | 응모 제출, 사이트 로그인 |
| Partnership Inquiry | `PartnershipInquiryController` | 스폰서십 문의 폼 |
| 공용 | `TestDataFactory` | 테스트 |

**Apex Trigger (1):** `LeadConvertPartnerContact` — Lead(Active, Aaron). Lead 전환 시 Partner Contact 보정.

---

## 7. Agentforce / AI

### 7.1 Agentforce Agent (GenAiPlannerDefinition, 팀 5종)

| Agent | Created | 버전 | 연결 Topic(Plugin) | 연결 Apex Action |
|---|---|---|---|---|
| **VIP Recommendation Agent** | Sara | v1–v2 | `vip_recommendations` | `GetPendingVipRecommendationsAction`, `ApproveRecommendationAction`, `SendRecommendationEmailAction` |
| **Opportunity Agent** | Eunyeong | v1–**v23** | `agent_router`, `activity_management`, `deal`, `proposal`, `negotiation`, `stage_guidance`, `escalation`, `off_topic`, `ambiguous_question` | `OpportunityAgentChatController`, `DealContext`, `OpportunityStageGuidance`, `ActivityIntelligenceAgentAction`, `ConversationHistoryAgentAction`, `FindSimilarClosedDeals`, `FindActivityAttendee` |
| **Negotiation Assistant** | Aaron | v1–v2 | `negotiation`, `proposal_quote` | `NegotiationContext`, `NegotiationTermsUpdater`, `NegotiationOpportunityLookup` |
| **Sponsorship Proposal Assistant** | Aaron | v1 | `proposal` | `OpportunityProposalContext`, `SponsorshipPackageLookup`, `SponsorshipProposalSaver` |
| **스폰서십 캠페인 에이전트** | Rafael | v1 | `bottleneck_monitor`, `renewal_report`, `agent_router` | `CampaignAgentChatController`, `CampaignBottleneckFinder`, `RenewalSummaryRefresher` |

> **버전 누적 주의:** `Opportunity_Agent_v1`~`v23` 등은 반복 재배포 흔적. **활성 버전은 각 1개**로 추정 — `GenAiPlannerBundle`/활성 상태 재확인 필요(§10).
> 비팀 Planner(데모/OOTB): `EmployeeCopilotPlanner`, `SearchAgent`, `DataQnAAgent`, `SDO_Service_Agentforce_*`, `Campaign_Agent_v1`, `AnalyticsAgent*` (생성자 Chanyeon Kim / Automated Process).

### 7.2 Prompt Template (GenAiPromptTemplate, 팀 6종)

| Template | Created | 용도 |
|---|---|---|
| `Fan_Personalized_Message` | Sara | 팬 개인화 메시지 생성 (→ `Recommendations__c.Personalized_Message__c`) |
| `CA_Offline_Meeting_Interaction_Intelligence` | Eunyeong | 미팅 노트 → 구조화 인텔리전스 |
| `CA_Offline_Meeting_Intelligence_UI` | Eunyeong | 미팅 인텔리전스 UI 표시용 |
| `CA_Stage_Guidance_Recommendation` | Eunyeong | Opportunity 단계별 가이던스 |
| `CA_PRM360_Sales_Briefing` | Hyejune | 파트너 담당자 일일 브리핑 (→ `Sales_Briefing__c.Briefing_Text__c`) |
| `CA_Lead_AI_Summary` | Hyejune | Lead 요약 (→ `Lead.AI_Lead_Summary__c`) |

> `CA_Diag_*` 4종(Eunyeong) = 진단/테스트용, 시스템 아님. `SDO_Sales_*` = 데모.

---

## 8. Frontend / LWC (팀 46)

| 화면 그룹 | 컴포넌트 |
|---|---|
| **Fan 360 Landing / List** | `fan360Landing`, `fanList`, `fanListTable`, `fanListKpiCards`, `fanListSearchFilter`, `fanDetailDrawer`, `icon` |
| **Fan 360 Detail / Timeline** | `fan360Summary`, `fanSummary`, `fanTimeline`, `fanRecommendedActions`, `gameDetail` |
| **Recommendation / Segment** | `recommendationReviewPanel`, `recommendationSegmentDashboard`, `recommendationDashboard`, `segmentFanList`, `segmentOpportunities` |
| **Campaign** | `campaignBoard`, `campaignAgentChat`, `campaignAgentChatModal` |
| **Report** | `reportDashboard` |
| **Quiz (Experience Site)** | `liveFanQuizEntry`, `liveFanQuizReveal` |
| **Opportunity Agent / Activity** | `opportunityAgentChat(+Modal)`, `opportunityStageGuidance`, `stageGuidance`, `stageProgress`, `activityIntelligence`, `activityOverview`, `activityTimeline`, `negotiationContextSummary` |
| **Partnership Inquiry** | `partnershipInquiry` |
| **PRM 파트너 포털** | `prm360RevenueSummary`, `prmClosingSoonOpportunities`, `prmHighPotentialLeads`, `prmKeyOpportunities`, `prmMyTasks`, `prmOpenSponsorshipPipeline`, `prmQuickLinks`, `prmSalesBriefing`, `prmSeasonClosedWonRevenue`, `prmSeasonTargetAttainment`, `prmTodaysEvents`, `prmYoyRevenue`, `leadAiSummaryCard` |

---

## 9. 주요 Business Flow

### 9.1 Fan → Engagement → Recommendation (B2C)

```
[외부 Fan App / 데이터] --External_ID__c--> Start Upsert Flow
      │
      ├─ Order (결제) ──> "Order Paid" ──> OrderItem, Admission__c
      │        └─> "Order Membership Status Sync" ──> Account.Membership_Status__c
      │
      ├─ Admission__c 생성 ──> "Admission Created"
      │        ├─> Attendance_Record__c 롤업 (Total/First/Last Admission)
      │        └─> "Fan Activity Pattern Admission Update" ──> Fan_Activity_Pattern__c
      │
      ├─ Engagement_Signal__c (SNS 관심 신호)
      │
      ▼
"Fan Value Calc" / "Start Fan Engagement Calc"
      ──> Account.Fan_Value_Tier__c / Engagement_Score__c / Engagement_Level__c
      ──> Fan_Segment_History__c (세그먼트 변경 시 이력)
      │
      ▼
"VIP Candidate Detection Flow" / VIP Recommendation Agent
      ──> Recommendations__c (Recommended_Action, Status=Pending)
      │
      ├─ "Generate AI Recommendation Message" (Prompt: Fan_Personalized_Message)
      │        ──> Recommendations__c.Personalized_Message__c
      │
      ├─ ApproveRecommendationAction ──> Status=Approved
      ├─ SendRecommendationEmailAction ──> Notification_Log__c
      └─ Benefits__c 발급 (Recommendations__c 연결, Status/Used_Date로 사용 추적)
      │
      ▼
Campaign(Fan_Campaign) + CampaignMember ──> Notification_Log__c (Fan Timeline)
```

### 9.2 Company Data → Agentforce → Lead → Opportunity → Sponsorship → Pipeline (B2B)

```
DART OpenAPI (DartService, DartMatchService)
      │  DART_Setting__c.Api_Key__c
      ▼
DART_Corp_Mapping__c + Account(Business).DART_* / Match_Confidence__c / Match_Rationale__c
      │  "DART 승인 보강" / DartEnrichmentQueueable
      ▼
Lead (RT SDO_Lead_Default) ── Hyejune Lead Scoring
      │  Score_* → Final_Lead_Score__c, Segment_Match__c, AI_Lead_Summary__c (Prompt: CA_Lead_AI_Summary)
      │  "DART Lead 전환 AI매칭" / "고득점 리드 연락 Flow"
      ▼
Lead 전환 (LeadConvertPartnerContact trigger)
      ──> Account(Business) + Contact(Partner_Contact) + Opportunity
      │
      ▼
Opportunity (RT SimpleOpportunity/ChannelPartner) — 41 custom fields
      │
      ├─ Task/Event 저장 ──> "CA Update Opportunity Last Contact / Next Activity"
      │        └─> "CA Generate Meeting Interaction Intelligence"
      │                 ──> Interaction_Intelligence__c ──(MD)──> Interaction_Signal__c
      │
      ├─ Opportunity Agent (v-latest): deal / proposal / negotiation / stage_guidance
      │        ├─ "CA Generate Stage Guidance" (Prompt: CA_Stage_Guidance_Recommendation)
      │        ├─ Negotiation Assistant ──> NegotiationTermsUpdater
      │        └─ Sponsorship Proposal Assistant ──> SponsorshipProposalSaver
      │
      ├─ OpportunityLineItem ──> Product2 (RT Sponsorship_Package)
      ├─ "계약서 생성 Flow"
      │
      ▼
Campaign (RT Sponsorship_Collaboration / _Prospecting / _Renewal)
      ├─ Campaign_Deliverable__c (가중치 이행 관리)
      │        ├─ "Campaign Deliverable Blocked Slack Alert" ──> Slack
      │        └─ Roll-Up ──> Campaign.Total/Completed_Deliverable_Weight__c
      ├─ "Campaign 예상 매출 계산/동기화" ──> 예상 매출
      ├─ "갱신 캠페인 성과 요약 자동 생성" ──> Campaign.Performance_Summary__c
      └─ 스폰서십 캠페인 에이전트 ──> CampaignBottleneckFinder / RenewalSummaryRefresher
      │
      ▼
Account Rollup: "Rollup Sponsorship To Account" / "Sync Account Latest Open Opportunity"
      ──> Account.Total_Sponsorship_Value__c / Sponsorship_Opportunity_Count__c / Latest_Open_Opportunity_*
      │
      ▼
PRM 파트너 포털 (Experience) — prm* LWC 13종 + Sales_Briefing__c (Prompt: CA_PRM360_Sales_Briefing) + PRM_Revenue_Target__c
```

---

## 10. Org 구현 현황 / 주의사항

| # | 항목 | 상태 |
|---|---|---|
| 1 | `Recommendation__c` (단수) / `User__c` | **phantom** — Tooling row만, 실 Object 아님. 정리 검토 |
| 2 | 표준 `Benefit` vs 커스텀 `Benefits__c` | 동일 이름 필드 3개 양쪽 존재. 실사용 1개로 통일 필요 |
| 3 | 폐기 필드 `_del__c` (~20) / 진단 필드 `_tc__*`,`ZZ_Diag*`,`CA_Diag*` | 배포·문서화 전 정리 대상 |
| 4 | Agent 버전 누적 (Opportunity Agent v1–v23 등) | 활성 버전 1개 확인 필요 (`GenAiPlannerBundle`) |
| 5 | `PRM_Revenue_Target__c` | 관계 field 0개 — Season/User 연결 미구현 |
| 6 | `AccountPlan` (표준, 08-31 Aaron 14필드) | 표준 Account Plan 기능 활성 여부·Layout 확인 필요 |
| 7 | `DART_Corp_Mapping__c` | Account와 물리적 FK 없음 — Flow 로직 의존. `05_DECISIONS D-020`("기업 DB는 Object 아님")과 상충 |
| 8 | `Attendance_Record__c.Fan__c` | UNIQUE 아님 — "팬당 1건"은 Flow 운영 규칙일 뿐 스키마 강제 아님 |
| 9 | PermissionSet / Profile | 이번 실사 미포함. `FRM_Manager_Access`, `Fan_App_API_Access` 등 후속 조회 필요 |
| 10 | Experience Site (FanQuiz, Partnership, PRM Portal) | Guest User·Apex·LWC 확인. `ExperienceBundle`/`Network` 메타데이터 후속 retrieve 필요 |
| 11 | `Opportunity` RecordType | 팀 생성 없음 — SDO `SimpleOpportunity`/`ChannelPartner` 재사용 중 |
| 12 | Order / OrderItem 자동화 | Rafael 필드 다수. Trigger 없음, Flow(`Order Paid` 등)로 처리 |

### Source of Truth 우선순위
```
Salesforce Org Metadata (2026-08-31)
        ↓
03_SYSTEM_ORG.md   ← 이 문서
        ↓
ERD_OBJECT_LIST.md
        ↓
ORG_VS_DOCUMENT_GAP.md  (기존 문서와의 차이 — 병합하지 않음)
```
