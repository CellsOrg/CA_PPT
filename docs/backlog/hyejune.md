# Cloud Alpacas 개인 개발 업무 정리 - 혜준

## B2B 개발

### 1. PRM 360 Dashboard 기획 및 화면 구성

**[Feature]**
Sales Manager가 Sponsorship Sales의 주요 현황과 당일 업무를 한 화면에서 확인할 수 있도록 PRM 360 Dashboard를 기획하고 구성.

**[Business Purpose]**
기존 Salesforce 화면과 Report를 각각 확인해야 하는 불편을 줄이고, Sales Manager가 현재 매출 상황 → 주요 Deal → 고전환 Lead → 오늘 할 일을 한 화면에서 빠르게 파악할 수 있도록 하기 위함.

**[Salesforce]**

* **App:** `Cloud Alpacas PRM`
* **Lightning Page:** `PRM_360`, `PRM_360_Home`
* **Dashboard:** `PRM_360_Overview`
* **LWC:**

  * `prmSeasonTargetAttainment`
  * `prmSeasonClosedWonRevenue`
  * `prmYoyRevenue`
  * `prmOpenSponsorshipPipeline`
  * `prmKeyOpportunities`
  * `prmClosingSoonOpportunities`
  * `prmHighPotentialLeads`
  * `prmTodaysEvents`
  * `prmMyTasks`
  * `prmQuickLinks`
  * `prmSalesBriefing`

**[How it works]**
PRM 360 Home에서 매출 KPI, Pipeline, Opportunity, Lead, Task, Event, AI Briefing을 하나의 업무 화면으로 제공.

각 영역은 LWC와 Report/Apex를 조합하여 구현하고, Lead와 Opportunity 등 실제 Salesforce Record로 이동할 수 있도록 구성.

**[Problem & Solution]**

* 정보가 많아질수록 Dashboard가 복잡해지는 문제를 고려하여 Sales Manager의 실제 판단과 업무 실행에 필요한 영역 중심으로 구성.
* 단순히 차트 수를 늘리는 대신 KPI와 List 중심으로 구성.
* 특히 전환 가능성이 높은 Lead는 단순 비율이 아니라 실제 Lead 목록으로 제공하여 후속 영업으로 연결되도록 설계.
* Salesforce는 실제 업무 실행, Tableau는 분석 역할을 담당하도록 역할을 구분.

**[QA]**
각 KPI 및 List의 원천 데이터와 화면 값이 일치하는지 확인하고, Record 클릭 및 사용자 권한에 따른 데이터 접근을 확인.

### 2. PRM 360 Sales KPI 및 영업 현황 구현

**[Feature]**
PRM 360에서 시즌 목표 달성률, Closed Won Revenue, Pipeline, YoY Revenue 등 Sales Manager가 가장 먼저 확인해야 할 영업 KPI를 구현.

**[Business Purpose]**
Sales Manager가 현재 시즌의 매출 달성 정도와 향후 영업 상황을 빠르게 판단할 수 있도록 하기 위함.

**[Salesforce]**

* **Object:** `Opportunity`, `OpportunityHistory`
* **Custom Object/Setting:** `PRM_Revenue_Target__c`
* **LWC:** `prmSeasonTargetAttainment`, `prmSeasonClosedWonRevenue`, `prmOpenSponsorshipPipeline`, `prmYoyRevenue`
* **Apex:** `PRM360Controller`, `PRM360SummaryController`
* **Report:**

  * `Season_Target_Attainment`
  * `Open_Sponsorship_Pipeline`
  * `Sponsorship_Pipeline_by_Stage_PRM`
  * `Season_Closed_Won_2026`
  * `Season_Closed_Won_Summary_PRM`
  * `Sponsorship_Revenue_YoY_PRM`

**[How it works]**
Opportunity의 Stage, Amount, Close Date 등의 데이터를 기반으로 Pipeline과 Closed Won을 집계하고, `PRM_Revenue_Target__c`의 목표값과 비교하여 현재 시즌 매출 현황을 표시.

**[Problem & Solution]**

* 단순 Report 표시로 해결하기 어려운 동적 KPI는 Apex에서 계산.
* 목표 대비 실적, Gap, Pipeline 등을 한 화면에서 연결하여 현재 상황과 향후 부족분을 함께 판단할 수 있도록 구성.
* 전년 대비 매출도 현재 시즌 기준으로 동적으로 비교할 수 있도록 구성.

**[QA]**
Opportunity 원천 데이터 → Apex/Report → LWC 표시값의 일치 여부 확인.

### 3. PRM 360 영업 업무 및 우선순위 관리

**[Feature]**
Sales Manager가 PRM 360 Home에서 오늘의 일정과 Task, 주요 Opportunity, Closing Soon Opportunity, High Potential Lead를 바로 확인할 수 있도록 업무 영역을 구현.

**[Business Purpose]**
Dashboard에서 현황만 확인하는 것이 아니라, 무엇을 먼저 처리해야 하는지까지 한 화면에서 판단할 수 있도록 하기 위함.

**[Salesforce]**

* **Object:** `Lead`, `Opportunity`, `Task`, `Event`, `User`
* **LWC:**

  * `prmTodaysEvents`
  * `prmMyTasks`
  * `prmKeyOpportunities`
  * `prmClosingSoonOpportunities`
  * `prmHighPotentialLeads`
  * `prmQuickLinks`
* **Apex:** `PRM360Controller`
* **Report:**

  * `Todays_Events_PRM`
  * `ActionsByPriority`
  * `Key_Opportunities_PRM`
  * `Closing_Soon_Opportunities`
  * `High_Potential_Leads`

**[How it works]**
사용자의 Task/Event를 조회하고, 영업상 중요도가 높은 Opportunity와 Closing Soon Opportunity를 보여줌.

Lead 영역에서는 `Final_Lead_Score__c`를 활용하여 전환 가능성이 높은 Lead를 우선적으로 노출하고, 각 Record를 클릭하여 상세 화면으로 이동할 수 있도록 구성.

**[Problem & Solution]**

* KPI만 보여주는 Dashboard는 실제 업무 실행으로 이어지기 어렵다는 점을 고려하여 업무 List를 함께 구성.
* High Potential Lead를 숫자나 차트가 아닌 실제 Lead 목록으로 구현하여 영업 담당자가 바로 후속 조치를 할 수 있도록 설계.

**[QA]**
Task/Event/Opportunity/Lead 데이터가 현재 사용자 기준으로 정상 조회되는지 확인하고, 각 Record 클릭 시 올바른 상세 화면으로 이동하는지 확인.

### 4. PRM 360 Sales Briefing

**[Feature]**
PRM 360 Home에서 현재 영업 상황을 AI가 자연어로 요약하여 제공하는 Sales Briefing 기능을 구현.

**[Business Purpose]**
Sales Manager가 여러 KPI와 영업 데이터를 직접 확인하고 조합하지 않아도, 오늘 확인해야 할 주요 영업 상황을 빠르게 파악할 수 있도록 하기 위함.

**[Salesforce]**

* **Object:** `Sales_Briefing__c`, `Opportunity`, `Lead`, `Task`, `Event`, `User`
* **LWC:** `prmSalesBriefing`
* **Apex:** `PRM360Controller`, `PRM360SalesBriefingScheduler`
* **Prompt:** `CA_PRM360_Sales_Briefing`
* **Agent:** 별도 Agentforce Agent 없음

**[How it works]**
Sales Briefing 요청 → Apex에서 영업 관련 데이터 조회 → Prompt Template에 Context 전달 → AI Briefing 생성 → `Sales_Briefing__c`에 저장 → LWC에서 표시.

AI 호출 실패 시 규칙 기반 Fallback을 사용하도록 구성.

**[Problem & Solution]**

* AI 호출 자체가 실패하더라도 Dashboard 기능이 중단되지 않도록 Fallback 구조를 적용.
* Agent가 Salesforce 데이터를 직접 조작하는 방식이 아니라 조회된 데이터를 기반으로 Briefing을 생성하는 역할로 제한.
* 매번 실시간 AI 호출만 하는 것이 아니라 Briefing 데이터를 저장하여 활용할 수 있도록 구성.

**[QA]**
Prompt 호출 → Briefing 생성 → `Sales_Briefing__c` 저장 → LWC 표시까지 전체 흐름을 확인.

### 5. Lead Scoring 설계 및 구현

**[Feature]**
B2B Sponsorship Sales에 적합한 Lead의 영업 우선순위를 판단하기 위해 기존 SDO Scoring 구조를 분석하고 새로운 Lead Scoring 체계를 설계 및 구현.

**[Business Purpose]**
모든 Lead를 동일하게 관리하는 것이 아니라 우리 구단과의 적합성 + 관심도 + 계약 준비도 + Risk를 종합하여 우선적으로 접근해야 할 Lead를 판단하기 위함.

**[Salesforce]**

* **Object:** `Lead`
* **신규 Field:**

  * `Regional_Connection__c`
  * `Sponsorship_History__c`
  * `Competitor_Sponsor__c`
  * `Controversial_Industry__c`
  * `Score_Industry__c`
  * `Score_Region__c`
  * `Score_Sponsorship__c`
  * `Score_Interest__c`
  * `Score_LeadSource__c`
  * `Risk_Penalty__c`
  * `Final_Lead_Score__c`
* **기존 SDO Scoring Field 활용:**

  * `Score1__c`
  * `Score2__c`
  * `Score3__c`
  * `Score4__c`
  * `SDO_Sales_Lead_Total__c`
  * `SDO_Sales_Lead_Quality__c`
  * `SDO_Sales_Has_Budget__c`
  * `SDO_Sales_Know_Decision_Maker__c`
  * `SDO_Sales_Project_Defined__c`
  * `SDO_Sales_Decision_Timeframe__c`
  * `pi__score__c`
* **수정 Field:** `Score2__c`, `SDO_Sales_Lead_Total__c`, `SDO_Sales_Lead_Quality__c`

**[How it works]**
기본 Scoring:

* Industry Fit: 25
* Regional Connection: 10
* Sponsorship History: 10
* Interest: 12
* Lead Source: 8
* Budget: 5
* Decision Maker: 5
* Project Defined: 5
* Decision Timeframe: 20

→ **Total 100점**

이후 `Risk_Penalty__c`를 적용하여 `Final_Lead_Score__c`를 최종 점수로 사용.

기존 SDO Scoring Field를 그대로 버리고 새로 만드는 방식이 아니라, 기존 구조 중 활용 가능한 항목은 재사용하고 B2B Sponsorship Sales에 필요한 평가 기준을 추가하는 방식으로 설계.

**[Problem & Solution]**

* 기존 SDO Demo의 Scoring 구조가 존재하여 전체를 새로 만들 경우 기존 데이터 구조와 분리되는 문제가 있어 기존 Field를 재사용.
* 단순 Lead Engagement만으로 판단하지 않고 Sponsorship Sales에 중요한 업종·지역·스폰서십 경험 및 계약 준비도를 추가.
* 경쟁 구단 후원이나 논란 업종 등 영업상 Risk를 별도로 반영.
* Formula의 컴파일 크기 문제를 확인하여 Scoring Formula를 분리 및 최적화.

**[QA]**
대표 Lead 데이터를 기준으로 각 항목별 예상 점수와 Salesforce 계산 결과를 비교하고, 고득점/저득점/Risk 적용 케이스를 각각 검증.

### 6. Lead AI Summary 및 후속 업무 자동화

**[Feature]**
Lead Record에서 Lead Score를 AI가 자연어로 요약하고, 고득점 Lead에 대해서는 후속 연락 Task가 자동 생성되도록 Lead 업무 지원 기능을 구현.

**[Business Purpose]**
영업 담당자가 Lead의 여러 Field와 Score를 직접 해석하지 않아도 Lead의 상태를 빠르게 파악하고, 우선순위가 높은 Lead에 대한 후속 영업을 놓치지 않도록 하기 위함.

**[Salesforce]**

* **Object:** `Lead`, `Task`
* **LWC:** `leadAiSummaryCard`
* **Apex:** `LeadAiSummaryController`
* **Flow:** `HighScore_Lead_Contact_Flow`
* **Prompt:** `CA_Lead_AI_Summary`
* **Lightning Page:** `Lead_Record_Page`
* **Field:** `AI_Lead_Summary__c`, `Final_Lead_Score__c` 및 Scoring 관련 Field

**[How it works]**
Lead Record Page 접속 → Lead Score 및 관련 Field 조회 → `CA_Lead_AI_Summary` Prompt Template 호출 → AI Summary 생성 → Lead 화면에 표시.

별도로 `HighScore_Lead_Contact_Flow`는 고득점 Lead를 대상으로 담당자에게 후속 연락 Task를 자동 생성하도록 구성.

**[Problem & Solution]**

* AI가 Lead Score를 다시 계산하는 것이 아니라 Salesforce의 `Final_Lead_Score__c`를 기준으로 설명하도록 역할을 분리.
* 높은 우선순위의 Lead가 실제 영업 업무로 연결될 수 있도록 자동 Task 생성 Flow를 구성.

**[QA]**

* Lead Score와 AI Summary 내용의 일치 여부
* Lead별 AI Summary 데이터 혼선 여부
* Prompt 호출 및 오류 처리
* 고득점 Lead의 Task 자동 생성 여부
* 현재 Flow가 구필드 `Lead_Score__c`를 기준으로 동작하고 있어 새 `Final_Lead_Score__c` 체계와 기준이 일치하는지 확인 필요
* Task Priority 설정과 실제 업무 의도와의 일치 여부 확인 필요

### 7. PRM 360 분석 연계

**[Feature]**
PRM 360에서 Salesforce 기반 영업 현황과 Tableau Next 기반 분석을 함께 활용할 수 있도록 분석 영역과 데이터 활용 구조를 구성.

**[Business Purpose]**
Salesforce에서는 실제 영업 업무와 Record 관리를 담당하고, Tableau에서는 데이터를 분석하여 Sales Manager의 판단을 지원하도록 역할을 구분하기 위함.

**[Salesforce / Tableau]**

* PRM 360 Home
* `PRM_360_Overview` Salesforce Dashboard
* Tableau Next
* Salesforce C360 Semantic Model
* Opportunity / Sponsorship Sales 데이터
* Dashboard Embedding

**[How it works]**
Salesforce PRM 360에서 KPI와 영업 업무 정보를 확인하고, Tableau Next를 활용한 분석 영역에서 Sponsorship Sales 데이터를 추가로 분석할 수 있도록 구성.

Salesforce의 원천 데이터와 Tableau의 집계 기준을 비교하여 화면 간 데이터 차이를 확인하고 원인을 추적.

**[Problem & Solution]**

* Salesforce와 Tableau에서 동일한 정보를 중복해서 제공하기보다 Salesforce는 업무 실행, Tableau는 분석에 집중하도록 역할을 구분.
* Dashboard를 단순히 시각적으로 화려하게 만드는 것이 아니라 Sales Manager의 실제 판단에 필요한 분석 정보를 제공하는 방향으로 구성.
* Salesforce와 Tableau의 수치가 일치하지 않는 경우 원천 데이터와 집계 기준을 비교하여 데이터 불일치 원인을 확인.

**[QA]**
Salesforce 원천 데이터와 Tableau 표시값의 집계 기준 및 수치 일치 여부, Dashboard 권한 및 분석 영역의 Embedding 상태를 확인.
