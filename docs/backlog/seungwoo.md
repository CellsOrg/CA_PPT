# Cloud Alpacas 개인 개발 업무 정리 - 승우

## B2B 개발

### 1. 스폰서십 캠페인 관리 Agent

[Feature]
캠페인 실행 과정의 지연 항목을 찾아 대책을 제안하고, 승인된 대책을 Salesforce에 기록하며, 계약 갱신에 필요한 성과까지 요약하는 `Sponsorship_Campaign_Agent`를 구축했다. Campaign 레코드 화면에서 바로 Agent를 사용할 수 있도록 채팅 위젯도 함께 구현했다.

[Business Purpose]
담당자가 수백 건의 캠페인 과업을 일일이 열어보지 않아도 실행 병목을 발견하고, 대응 Task 생성부터 갱신 자료 준비까지 한 화면에서 처리하기 위해 필요하다.

[Salesforce]
Agent: `Sponsorship_Campaign_Agent`
Apex: `CampaignBottleneckFinder`, `CampaignMitigationRecorder`, `RenewalSummaryRefresher`, `CampaignAgentChatController`
LWC: `campaignAgentChat`, `campaignAgentChatModal`
Permission Set: `CA_Campaign_Agent_Access`
FlexiPage: `Campaign_Record_Page3`
Named Credential: `CA_Agent_API_PerUser`

[How it works]
사용자가 Campaign 레코드에서 질문하면 Agent Router가 병목 조회 또는 갱신 요약으로 요청을 분류한다. 병목 조회 시 지연된 Deliverable을 찾아 대책을 제안하고, 사용자가 승인하면 Notes를 갱신하고 Task를 생성한다. 갱신 요청이면 최신 Campaign 성과를 재계산해 요약한다.

[Problem & Solution]
Agent Router가 이전 대화를 이어받지 못하고 실제 Action을 실행하지 않은 채 “적용하겠다”고만 응답하는 문제가 있었다. Router가 직접 답하지 않고 반드시 적절한 Subagent로 이동하도록 지침을 강화해 해결했다.

위젯에서는 Per-User OAuth 인증이 완료되지 않아 Named Credential 오류가 발생했다. Setup UI 대신 Connect REST API로 인증 URL을 발급해 사용자 인증을 완료했다.

[QA]
수정 필요. Agent의 조회·추천·대책 적용·갱신 요약은 Live Preview와 실데이터로 정상 검증했고 Agent도 Active 상태다. 다만 위젯 UI는 권장 시나리오 5개 중 1개만 검증됐으며, `CA_Campaign_Agent_Access`의 Named Credential Principal 권한 추가와 Apex 단위 테스트 작성이 필요하다.

---

### 2. 캠페인 실행 과업 추적 및 Slack 지연 알림

[Feature]
계약 후 실행해야 할 개별 업무를 관리하는 `Campaign_Deliverable__c`를 새로 만들고, 과업 차단 또는 납기 연기를 감지해 Slack으로 실시간 알림을 보내는 자동화를 구현했다.

[Business Purpose]
표준 Campaign만으로는 계약서 서명, 광고물 제작, 설치, 성과 보고서 제출과 같은 개별 실행 항목을 관리할 수 없다. 담당자가 지연된 과업을 놓치지 않고 즉시 대응할 수 있도록 하기 위해 필요하다.

[Salesforce]
Object: `Campaign_Deliverable__c`
Fields: `Campaign__c`, `Status__c`, `Weight__c`, `Due_Date__c`, `Completed_Date__c`, `Evidence_URL__c`, `Notes__c`, `Blocked_Reason__c`, `Pending_Slack_Message__c`
Flow: `Campaign_Deliverable_Detect_Due_Date_Push`, `Campaign_Deliverable_Blocked_Slack_Alert`
Integration: Salesforce Slack Action, `#campaign-alerts`

[How it works]
Campaign 아래에 실행 과업을 생성하고 각 과업의 상태, 마감일, 가중치와 증빙을 관리한다. 상태가 Blocked로 바뀌거나 마감일이 연기되면 Before-Save Flow가 정확한 시점의 메시지를 조립하고, After-Save 비동기 Flow가 해당 메시지를 Slack으로 발송한다.

[Problem & Solution]
비동기 Flow가 실행 시점의 최신 레코드를 다시 읽으면서, 연속 수정이 발생하면 과거 지연 사유 대신 빈 값이나 변경된 값이 발송되는 문제가 있었다. Before-Save Flow에서 메시지를 미리 완성해 별도 필드에 저장하고, 비동기 Flow는 저장된 메시지만 발송하도록 구조를 분리했다.

Custom Field가 Metadata API 배포 후 SOQL과 Describe API에서 조회되지 않는 문제도 발생했다. Setup UI에서 필드를 수동 재생성해 즉시 반영되도록 우회했다.

[QA]
현재 정상. 실제 데이터로 Blocked 전환, 납기 연기, 지연 사유 6종, 메모가 없는 경우까지 총 7개 시나리오의 Slack 발송을 확인했다. 현재 사용하지 않는 `Due_Date_Pushed__c` 필드는 추후 정리가 필요하다.

---

### 3. 갱신 캠페인 성과 자동 요약

[Feature]
기존 Collaboration Campaign의 팬 반응과 Deliverable 이행률을 자동 집계해 Renewal Campaign에 갱신용 성과 요약을 생성하는 기능을 구현했다.

[Business Purpose]
계약 갱신이나 업셀 제안 시 담당자가 스폰서 성과를 매번 수동으로 계산하지 않고, 스폰서 등급에 맞는 근거를 즉시 제시할 수 있도록 하기 위해 필요하다.

[Salesforce]
Flow: `Renewal_Campaign_Performance_Summary`
Fields: `Campaign.Performance_Summary__c`, `Total_Deliverable_Weight__c`, `Completed_Deliverable_Weight__c`
Reference Field: `Opportunity.Partner_Tier__c`
Apex: `RenewalSummaryRefresher`

[How it works]
Renewal Campaign이 저장되면 같은 Parent Campaign 아래의 Collaboration Campaign을 조회한다. 팬 도달·반응 수와 Deliverable 이행률을 집계하고, Partner Tier에 따라 적합한 성과지표를 조합해 `Performance_Summary__c`에 저장한다. Agent에서 조회할 때는 Renewal Campaign을 Touch Update해 최신 계산을 강제로 실행한다.

[Problem & Solution]
Flow 안에 `null__NotFound`라는 깨진 필드 참조가 남아 실행 오류가 발생했다. 실제 Record Type ID 조건으로 교체했다.

갱신 캠페인 자체에는 Deliverable이 없기 때문에 이행률이 항상 0으로 반환되는 문제도 있었다. 잘못된 개별 수치 출력을 제거하고, 형제 Collaboration Campaign에서 정확하게 계산된 `Performance_Summary__c`를 반환하도록 변경했다.

[QA]
수정 필요. Agent를 통해 조회하면 최신 성과가 정상 반환되며, 실제 d’Alba 데이터의 이행률도 정확히 계산됐다. 다만 Collaboration Campaign의 Deliverable만 변경한 경우 Renewal Campaign 자체는 자동 재계산되지 않으므로, Agent를 거치지 않는 직접 조회 경로의 정식 Flow 보완이 필요하다.

---

### 4. Proposal·Quote 추천 Subagent

[Feature]
Opportunity의 제안 단계에서 적합한 스폰서십 상품을 추천하고, 사용자 확인 후 Quote와 Quote Line Item을 생성하는 `Sponsorship_Proposal_Assistant`를 설계·구현했다.

[Business Purpose]
영업 담당자가 고객 조건에 맞는 상품을 빠르게 조합하고, 추천에서 견적 생성까지의 반복 업무를 줄이기 위해 필요하다.

[Salesforce]
Agent: `Sponsorship_Proposal_Assistant`
Apex: `OpportunityProposalContext`, `SponsorshipPackageLookup`, `SponsorshipProposalSaver`
Objects: `Opportunity`, `Product2`, `PricebookEntry`, `Quote`, `QuoteLineItem`
Permission Set: `CA_Opportunity_Agent_Access`

[How it works]
Opportunity 정보를 조회한 뒤 활성화된 Sponsorship Package와 가격을 불러온다. Agent가 실제 조회 결과를 바탕으로 상품을 추천하고 제안 초안을 보여준다. 사용자가 저장을 명시적으로 승인하면 Quote와 Quote Line Item을 생성하고 Opportunity의 Benefit 관련 필드를 갱신한다.

[Problem & Solution]
Record ID를 일반 String으로 선언했을 때 로컬 검증은 통과했지만 Live Preview에서만 오류가 발생했다. 타입을 `lightning__recordIdType`으로 변경해 해결했다.

또한 승우가 만든 Apex 3개와 Permission Set이 Git Main에 병합되기 전에 다른 담당자가 같은 이름의 컴포넌트를 별도로 구현했다. 현재 Main과 Org에는 다른 담당자의 버전이 반영돼 있어 두 버전 중 무엇을 채택할지 정리가 필요하다.

[QA]
수정 필요. 승우 버전은 실제 Opportunity를 이용한 조회·추천·확인·Quote 저장까지 Live Preview에서 통과했다. 그러나 Agent는 Publish되지 않았고 메인 Opportunity Agent에도 통합되지 않았다. 현재 운영 중인 동명 Apex는 다른 담당자의 구현이므로 버전 비교와 소유권 정리가 선행돼야 한다.

---

### 5. 스폰서십 상품 및 표준 견적 체계

[Feature]
구장 광고, Brand Day, 유니폼 패치, 명명권 등을 판매 가능한 상품으로 관리하는 Sponsorship Package 21종과 Salesforce 표준 Quote 체계를 구축했다.

[Business Purpose]
스폰서십을 단순 협업 아이디어가 아니라 실제 가격과 계약 조건을 가진 영업 상품으로 관리하고, Opportunity에서 공식 견적서까지 연결하기 위해 필요하다.

[Salesforce]
Objects: `Product2`, `Pricebook2`, `PricebookEntry`, `OpportunityLineItem`, `Quote`, `QuoteLineItem`
Record Type: `Product2.Sponsorship_Package`
Fields: `PricebookEntry.Max_Discounted_Price__c`, `Max_Discount_Percent__c`
Layout: `Sponsorship Package Layout`
Quote Template: `Cloud Alpacas Sponsorship Quote`
Feature: Product Revenue Schedule, Quote Sync

[How it works]
담당자가 Opportunity에 Sponsorship Package를 추가하면 Standard Price Book의 가격이 적용된다. Opportunity Product를 기준으로 Quote와 Quote Line Item을 생성하고, Quote Sync 후 PDF 견적서를 출력한다. 기간제 광고 상품은 Revenue Schedule을 통해 월별로 매출을 분할할 수 있다.

[Problem & Solution]
초기 상품 가격에서 명명권보다 유니폼 패치가 비싼 등 상품 간 가격 순위가 비현실적이었다. KBO·MLB 벤치마크를 기준으로 세 차례 가격을 조정해 최종 가격 체계를 확정했다.

Quote Sync 이후 Opportunity Line Item을 수정하면 값이 원복되는 문제는 오류가 아니라 Quote Line Item이 기준 데이터가 되는 표준 동작이었다. Sync 중에는 Quote Line Item에서만 수정하도록 사용 원칙을 정리했다.

[QA]
현재 정상. d’Alba 상품을 이용한 Product → Opportunity Product → Quote → Sync → PDF 생성 E2E 테스트를 통과했다. 다만 21개 전체 상품을 대상으로 한 개별 가격·견적 회귀 테스트는 추가로 권장된다.

---

### 6. Campaign 예상 매출 자동 동기화

[Feature]
Campaign에 연결된 Opportunity 금액의 합계를 `Campaign.ExpectedRevenue`에 자동 반영하는 Flow 3종을 구현했다.

[Business Purpose]
Opportunity 금액이 변경되거나 삭제됐는데 Campaign의 예상 매출은 그대로 남는 데이터 불일치를 방지하기 위해 필요하다.

[Salesforce]
Objects: `Opportunity`, `Campaign`
Fields: `Opportunity.Amount`, `Opportunity.CampaignId`, `Campaign.ExpectedRevenue`
Flows: `Recalculate_Campaign_Expected_Revenue`, `Campaign_Expected_Revenue_Sync`, `Campaign_Expected_Revenue_Sync_On_Delete`

[How it works]
Campaign과 연결된 Opportunity가 생성·수정·삭제되면 Subflow가 해당 Campaign의 모든 Opportunity Amount를 다시 합산해 Expected Revenue를 갱신한다.

[Problem & Solution]
Record-Triggered Flow 하나에서 생성·수정과 삭제를 모두 처리할 수 없었다. 생성·수정용 Flow와 삭제용 Flow를 분리하고, 실제 계산 로직은 공통 Subflow로 만들어 중복을 제거했다.

[QA]
수정 필요. Opportunity 생성과 삭제에 따른 예상 매출 증감은 실데이터로 정상 확인했다. 다만 Opportunity의 Campaign 연결이 A에서 B로 변경될 경우 이전 Campaign A의 금액을 다시 계산하지 않는 예외 케이스가 남아 있다.

---

### 7. 스폰서십 Campaign 생애주기 및 화면 구조

[Feature]
스폰서십을 발굴, 실행, 갱신 단계로 구분하는 Campaign Record Type·Hierarchy·Path·List View를 만들고, Collaboration과 Renewal 화면을 목적에 맞게 분리했다.

[Business Purpose]
계약 전 영업 활동과 계약 후 실행 관리, 계약 만료 전 갱신 활동은 필요한 정보가 다르다. 이를 하나의 Campaign 화면으로 관리하면서도 단계별로 필요한 정보만 보여주기 위해 필요하다.

[Salesforce]
Object: `Campaign`
Record Types: `Sponsorship_Prospecting`, `Sponsorship_Collaboration`, `Sponsorship_Renewal`
Path: Prospecting, Collaboration, Renewal Path
List View: 단계별 4종
Hierarchy: `Parent Campaign`
Layouts: `Sponsorship Collaboration Execution Layout`, `Sponsorship Renewal Layout`

[How it works]
Campaign 생성 시 목적에 맞는 Record Type을 선택한다. Prospecting은 스폰서 발굴, Collaboration은 계약 실행, Renewal은 갱신 제안을 관리한다. Parent Campaign을 통해 동일 스폰서의 여러 연도·단계 Campaign을 하나의 계층으로 연결한다.

[Problem & Solution]
세 Record Type이 같은 Layout을 공유해 Renewal 화면에도 실행 가중치가 보이고 Collaboration 화면에는 빈 성과 요약이 노출됐다. Collaboration과 Renewal 전용 Layout을 새로 만들고 필드와 Related List 순서를 각각 재구성했다.

Page Layout Assignment 화면에는 같은 이름의 System Administrator Profile이 두 개 표시됐다. 실제 사용자의 Profile ID를 API로 먼저 확인한 후 정확한 Profile에만 Layout을 배정했다.

[QA]
현재 정상. Collaboration과 Renewal 실제 레코드에서 섹션 순서, 필드 노출, Related List 배치를 확인했다. Prospecting은 기존 Layout을 유지한다.

---

### 8. 스폰서십 Pipeline·Revenue 대시보드

[Feature]
Campaign과 Opportunity 데이터를 기반으로 스폰서십 Pipeline, 예상 매출, 확정 매출, 순이익을 확인하는 Report 5종과 Dashboard 7개 위젯을 구성했다.

[Business Purpose]
관리자가 개별 Opportunity를 열지 않아도 목표 대비 확정 매출과 잠재 매출, 부족 금액을 한 화면에서 확인하고 우선 조치를 판단하기 위해 필요하다.

[Salesforce]
Objects: `Opportunity`, `Campaign`, `Quote`, `Campaign_Deliverable__c`
Fields: `Opportunity.Amount`, `Campaign.ExpectedRevenue`, 비용 관련 표준 필드
Reports: 5종
Dashboard: 7개 위젯
Formula: Net Profit Custom Summary Formula

[How it works]
Opportunity가 `CampaignId`를 통해 Campaign에 연결되고, Expected Revenue 동기화 Flow가 최신 금액을 반영한다. Report가 단계·기간·Campaign별 Pipeline과 Revenue를 집계하고 Dashboard가 핵심 KPI와 진행 상태를 시각화한다.

[Problem & Solution]
Dashboard 위젯을 API로 추가하면 `JSON_PARSER_ERROR`가 발생했다. Lightning UI에서 위젯을 직접 추가하는 방식으로 해결했다.

그룹이 없는 Summary Report가 내부적으로 Tabular Report로 되돌아가 Metric 위젯에 데이터가 표시되지 않았다. 최소 한 개의 그룹을 추가해 Summary 형식을 유지했다.

[QA]
수정 필요. Report와 Dashboard 구성은 완료됐지만, Conversion Rate Custom Summary Formula의 최종 완료 여부가 통합본에서 확인되지 않는다. 발표 전 전체 위젯의 최신 데이터와 필터 동작을 한 번 더 검증해야 한다.

## B2C

### 1. Fan 360 통합 고객 프로필

[Feature]
팬의 기본정보, 구매, 경기 관람, 캠페인 반응, 선호 선수와 활동 패턴을 한 명의 고객 프로필 중심으로 연결하는 Fan 360 데이터 구조를 구축했다.

[Business Purpose]
티켓 구매, 굿즈 구매, 경기 방문, 콘텐츠 반응이 서로 분리되면 팬별 행동을 이해하거나 개인화 마케팅을 수행하기 어렵다. 각 팬의 전체 여정을 하나의 CRM에서 파악하기 위해 필요하다.

[Salesforce]
Objects: `Account`의 Person Account, `Contact`, `Order`, `OrderItem`, `Admission__c`, `Attendance_Record__c`, `Engagement_Signal__c`, `Fan_Activity_Pattern__c`, `Fan_Segment_History__c`, `Recommendation__c`, `Player__c`, `Game__c`
Fields: 총 구매액, 멤버십 상태·종료일, 선호 선수, Engagement Level 등
LWC/Apex/Agent: 통합본에서 승우 담당 구현으로 확인되는 별도 컴포넌트 없음

[How it works]
Fan App과 Campaign에서 발생한 구매·방문·반응 데이터가 팬의 Person Account에 연결된다. 누적된 데이터는 팬 활동 패턴, 세그먼트 이력, 추천 정보로 확장돼 개인화 Flow와 캠페인의 입력값으로 사용된다.

[Problem & Solution]
Person Account를 활성화한 뒤 Record Type이 Profile에 배정되지 않으면 팬 레코드를 생성하거나 관련 필드를 사용할 수 없는 문제가 있었다. Person Account Record Type과 Profile 권한을 확인해 해결했다.

Org 기본 데이터 삭제 과정에서 테스트용 팬 데이터가 사라지는 문제도 있었다. Recycle Bin에서 복구하거나 대표 Person Account를 다시 생성해 테스트 기반을 마련하는 방식으로 대응했다.

[QA]
수정 필요. 데이터 모델은 구축됐지만, 현재 통합본만으로 전체 Person Account·활동 데이터의 최신 레코드 수와 모든 관계의 정합성을 확인하기 어렵다. 대표 팬 기준 E2E 재검증이 필요하다.

---

### 2. 팬 행동 기반 자동 Engagement Flow

[Feature]
팬의 가입, 첫 티켓 구매, 첫 경기 방문, 첫 굿즈 구매, 선호 선수 등록, VIP 후보 진입을 감지해 후속 안내와 추천을 실행하는 6종 Flow를 구축했다.

[Business Purpose]
모든 팬에게 동일한 메시지를 보내는 방식에서 벗어나, 팬의 실제 행동과 여정 단계에 맞는 안내와 혜택을 자동으로 제공하기 위해 필요하다.

[Salesforce]
Flows: Welcome, First Ticket, First Visit Guide, First Merchandise, Favorite Player, VIP Candidate Detection
Objects: Person Account, `Order`, `OrderItem`, `Admission__c` 또는 `Attendance_Record__c`, `Player__c`, `Recommendation__c`
Fields: 구매 유형, 첫 행동 여부, 선호 선수, 누적 구매액, VIP 기준 필드
LWC/Apex/Agent: 해당 6개 자동화의 핵심 구현에는 별도 구성 없음

[How it works]
팬의 레코드 또는 관련 구매·방문 데이터가 생성되면 각 Flow가 최초 행동 여부와 조건을 확인한다. 조건을 처음 충족한 팬에게만 안내 또는 Recommendation을 생성하고, 동일 이벤트가 반복 실행되지 않도록 상태를 기록한다.

[Problem & Solution]
Flow를 Debug할 대표 테스트 데이터가 부족해 분기 조건을 검증하기 어려웠다. Person Account와 구매·방문 레코드를 시나리오별로 준비해 하나씩 검증하는 방식으로 전환했다.

Order Type과 커스텀 주문 구분 필드가 중복되고, Person Account의 Contact ID가 화면에서 바로 보이지 않는 문제도 있었다. 실제 API 필드를 기준으로 Flow 조건을 통일하고 `PersonContactId` 관계를 사용하도록 정리했다.

[QA]
수정 필요. 6개 Flow의 구축과 활성화는 완료됐지만, 통합본에는 각 Flow의 최종 실데이터 E2E 결과가 모두 남아 있지 않다. 시나리오별 중복 실행 방지와 잘못된 대상에게 발송되지 않는지 회귀 테스트가 필요하다.

---

### 3. Fan App 구매·체크인 실시간 연동

[Feature]
외부 Fan App에서 발생한 상품 구매와 경기 체크인 데이터를 Salesforce의 팬, 주문, 경기, 입장 데이터로 연결하는 API 연동 구조를 마련했다.

[Business Purpose]
팬의 디지털 행동과 오프라인 경기장 경험을 CRM에 실시간으로 축적해 Fan 360 분석과 개인화 자동화에 활용하기 위해 필요하다.

[Salesforce]
Objects: Person Account, `Product2`, `PricebookEntry`, `Order`, `OrderItem`, `Game__c`, `Admission__c` 또는 `Attendance_Record__c`
Security: Connected App, API Scope, Refresh Token, Integration User, `Fan_App_API_Access` Permission Set
Integration: Salesforce REST API
Flow/LWC/Apex/Agent: 외부 Fan App 호출 중심이며 통합본에서 별도 내부 구현은 확인되지 않음

[How it works]
Fan App이 Integration User로 Salesforce API에 인증한다. 상품 구매 시 Product와 PricebookEntry를 기준으로 Order와 OrderItem을 생성하고, 경기 체크인 시 Game과 팬을 연결한 입장 레코드를 생성한다. 생성된 데이터는 Fan 360과 행동 기반 Flow에서 활용된다.

[Problem & Solution]
Fan App에는 상품 15개와 경기 5개가 있었지만 Salesforce에서는 일부만 일치해 주문과 체크인 생성이 실패할 수 있었다. 누락된 Product2 10개와 Game 1개를 정의하고, 판매 상품에는 Standard Price Book의 KRW PricebookEntry가 반드시 필요하다는 데이터 계약을 정리했다.

Security Token 수신과 인증 방식도 불안정했다. 개인 계정에 의존하지 않고 전용 Integration User, Connected App, Permission Set, OAuth 기반으로 권한을 분리하도록 구성했다.

[QA]
수정 필요. Integration User와 Permission Set의 존재는 확인되지만, 통합본에는 누락 상품·경기 데이터의 최종 생성 여부와 구매·체크인 전체 E2E 결과가 확정적으로 기록돼 있지 않다.

---

### 4. 팬 캠페인 반응·전환 추적

[Feature]
캠페인 대상 팬이 메시지를 받고, 반응하고, 행사에 참여하고, 구매 또는 전환에 도달하는 과정을 Campaign Member와 Engagement Signal로 관리하는 구조를 구축했다.

[Business Purpose]
캠페인을 단순 발송 건수로 평가하지 않고, 어떤 팬이 실제 반응·참여·구매로 이어졌는지 측정하기 위해 필요하다.

[Salesforce]
Objects: `Campaign`, `CampaignMember`, `Engagement_Signal__c`, `Admission__c`, `Order`, `OrderItem`
Fields: Campaign Member Status, `Is_Converted__c`, 반응 유형, 채널, 발생 시각, 연결 Campaign
Statuses: Targeted → Reached → Engaged → Attended → Converted
Flow/LWC/Apex/Agent: 통합본에서 B2C 전용 추가 컴포넌트는 확인되지 않음

[How it works]
팬이 Campaign Member로 등록되면 Targeted 상태에서 시작한다. 메시지 도달, 클릭·QR 스캔, 경기 참여, 구매 데이터가 발생할 때 상태와 Engagement Signal이 누적되고 최종 전환까지 추적한다.

[Problem & Solution]
Campaign Member Status에 기본값인 Sent와 Responded만 존재해 실제 팬 여정을 세분화할 수 없었다. 캠페인 목적에 맞는 5단계 상태를 정의해 전환 퍼널을 표현하도록 개선했다.

`CampaignMember.Is_Converted__c`가 배포 직후 조회되지 않는 스키마 전파 문제가 있었지만, 별도 재생성 없이 시간이 지난 뒤 정상 조회되는 것을 확인했다.

[QA]
수정 필요. `Is_Converted__c` 조회 문제는 해소됐지만, B2C Campaign 전체에 5단계 Status가 일관되게 적용됐는지와 실제 Engagement Signal이 상태 변경으로 연결되는지는 추가 확인이 필요하다.
