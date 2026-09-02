# Cloud Alpacas 개인 개발 업무 정리 - 아론

## B2B 개발 (PRM · 파트너십/스폰서십)

### 1. 파트너십 데이터 모델·레코드타입 정비

**[Feature] 무엇을 만들었는가?**
채널판매 PRM 기본값을 스포츠 구단의 스폰서·제휴 맥락으로 바꾼 데이터 모델 기반 — 관계 유형/파트너십 상태 필드 재정의, 레코드타입 라벨·화면 정비, Opportunity 계약 단계 추가

**[Business Purpose] 왜 필요한가?**
한 Org에서 FRM(팬)과 PRM(제휴사)이 섞이는 걸 막고, 제휴 담당자가 업무 언어 그대로 화면을 보게 하기 위해 필요함.

**[Salesforce] Object / Field / Flow / LWC / Apex / Agent**
Account·Contact RecordType(→ "파트너십") / `SDO_Partner_Type__c`(관계 유형)·`SDO_Partnership_Status__c`(파트너십 상태) 제한 픽리스트 개편 / OpportunityStage `Contracting` 추가 / FlexiPage 탭 재편 / Salesforce DX 소스 관리

**[How it works] 간단한 동작 흐름**
API 이름은 유지하고 라벨·값세트만 정비 → Flow·리포트·기존 레코드 영향 없이 화면 언어만 파트너십 맥락으로 전환

**[Problem & Solution] 개발하면서 해결한 문제**
- 레코드타입을 늘리는 대신 관계 유형 값으로 제휴사 종류를 구분해, 레이아웃·페이지·프로필 할당이 한 벌씩 붙는 비용을 회피
- 라벨만 바꾸고 API명을 유지해 마이그레이션 없이 정비

**[QA]**
배포·화면 반영 정상. 단 `SDO_` 접두사 중복 필드(파트너십 상태 등)의 주 필드 확정은 팀 확정 필요.

---

### 2. 파트너십 계정 · 스폰서 계정 리스트뷰

**[Feature] 무엇을 만들었는가?**
목적이 다른 두 리스트뷰 — 기본 "파트너십 계정"과 시나리오용 "스폰서 계정", 각각 담당자가 판단할 정보로 컬럼을 다르게 구성

**[Business Purpose] 왜 필요한가?**
"이 계정이 무엇인지 식별"이 아니라 "지금 뭘 먼저 챙길지"를 목록에서 바로 판단하게 하기 위해 필요함.

**[Salesforce] Object / Field / Flow / LWC / Apex / Agent**
Account List View `PartnershipAccounts`·`Sponsor Accounts` / RecordType 필터 / 컬럼: (파트너십) 최근 영업기회 단계·금액·최근 활동 경과일 / (스폰서) `Sponsor_Tier__c`·`Sponsorship_Opportunity_Count__c`

**[How it works] 간단한 동작 흐름**
파트너십 계정은 최근 영업 기회·활동 중심 컬럼, 스폰서 계정은 스폰서 등급·건수 중심 컬럼으로 분리해 표시

**[Problem & Solution] 개발하면서 해결한 문제**
- 리스트뷰 컬럼이 필드 API명이 아니라 전용 토큰(`ACCOUNT.PHONE1` 등)을 써서, 동작하는 뷰를 retrieve해 포맷을 맞춤
- 최근 영업 기회 정보는 크로스오브젝트라 직접 못 넣어 계정 요약필드로 우회(→ 작업 6)

**[QA]**
두 리스트뷰 컬럼 의도대로 표시 정상.

---

### 3. 파트너십 계정 레코드 화면 (레코드페이지 + 연도별 추이 그래프)

**[Feature] 무엇을 만들었는가?**
파트너십 계정을 열면 연도별 스폰서십 추이 그래프와 함께 계약·관계 정보가 이어지는 레코드 화면. 실무 관련 리스트(Order·Asset·Account Planning)까지 배치

**[Business Purpose] 왜 필요한가?**
계정 하나에서 "몇 년째 파트너인지, 추이가 어떤지, 현재 무엇을 보유했는지"를 한눈에 보기 위해 필요함.

**[Salesforce] Object / Field / Flow / LWC / Apex / Agent**
FlexiPage `SDO_Sales_Account_Partner_Account` / 레코드페이지 레코드타입 Activation / 연도별 스폰서십 금액 Report 차트 / 관련 리스트 Contacts·Opportunities·Order·Asset·Account Planning(ADVGRID) / *LWC는 팀 공통 UI 합의 후 착수 예정*

**[How it works] 간단한 동작 흐름**
계정 열기 → 연도별 추이 그래프 표시 → 기본 Contacts·Opportunities 확인. Order·Asset·Account Planning은 실무 완성도용으로 데이터만 채우고 데모에서는 미노출

**[Problem & Solution] 개발하면서 해결한 문제**
- 탭이 통째로 비어 보이던 원인이 데이터가 아니라 **레코드페이지가 레코드타입에 미활성**인 것이라, 페이지를 Activation해 해결
- 새 관련 리스트가 공란이던 원인은 `relatedListComponentOverride`가 NONE이라 ADVGRID로 재배포

**[QA]**
그래프·탭 표시 정상. Order·Asset·Account Planning은 더미 데이터만 채우면 됨(데모 미노출).

---

### 4. 파트너 연락처 리스트뷰 (연락 중심)

**[Feature] 무엇을 만들었는가?**
계정 목록과 달리 담당자에게 바로 연락할 수 있도록 모바일·이메일을 앞세운 연락처 리스트뷰

**[Business Purpose] 왜 필요한가?**
연락처 화면의 목적은 "식별"이 아니라 "연락"이므로 연락 수단이 먼저 보여야 함.

**[Salesforce] Object / Field / Flow / LWC / Apex / Agent**
Contact List View `Partner Contacts` / RecordType 필터(Partner) / 컬럼: 이름·Account·직함·전화·모바일·이메일·담당자

**[How it works] 간단한 동작 흐름**
RecordType으로 파트너 담당자만 걸러 표시하고, 모바일·이메일 컬럼을 우선 배치

**[Problem & Solution] 개발하면서 해결한 문제**
- 스코프를 넓히자 팬까지 전체가 노출돼, RecordType 필터로 파트너 담당자만 한정

**[QA]**
연락 중심 컬럼 표시 정상.

---

### 5. 스폰서 등급·건수·금액 자동 산정 (Flow)

**[Feature] 무엇을 만들었는가?**
계정의 스폰서십 기회를 집계해 스폰서 등급·건수·총 금액을 자동으로 채우는 Flow

**[Business Purpose] 왜 필요한가?**
담당자가 손으로 등급을 매기지 않아도 금액 기준으로 일관되게 스폰서를 분류하기 위해 필요함.

**[Salesforce] Object / Field / Flow / LWC / Apex / Agent**
Record-Triggered Flow(Opportunity 생성·수정·삭제) / `Sponsor_Tier__c`(Diamond·Platinum·Gold·None)·`Sponsorship_Opportunity_Count__c`(Number)·`Total_Sponsorship_Value__c`

**[How it works] 간단한 동작 흐름**
Opportunity 변경 → 해당 Account의 스폰서십 총액 합산 → 임계값(15억/5억)으로 등급·건수·금액 세팅

**[Problem & Solution] 개발하면서 해결한 문제**
- 표준 Roll-Up Summary는 Master-Detail에서만 되고 Account–Opportunity는 Lookup이라 불가 → **Flow로 집계**(건수 필드는 롤업이 아니라 Flow가 채우는 Number 필드)

**[QA]**
금액 변경 시 등급 실시간 재산정 확인(예: 6억↑ → Platinum). 정상.

---

### 6. 계정 요약필드 동기화 (Flow)

**[Feature] 무엇을 만들었는가?**
계정의 최신 Open Opportunity 단계·금액·다음 단계를 계정 필드로 내려 담는 Flow

**[Business Purpose] 왜 필요한가?**
리스트뷰·계정 화면에서 자식 오브젝트인 영업 기회 정보를 바로 보여주기 위해 필요함.

**[Salesforce] Object / Field / Flow / LWC / Apex / Agent**
Record-Triggered Flow(Opportunity) / Account `Latest_Open_Opportunity_Stage__c`·`Latest_Open_Opportunity_Amount__c`·`Latest_Open_Opportunity_Next_Step__c`

**[How it works] 간단한 동작 흐름**
Opportunity 생성/수정 → 해당 계정의 "가장 최근 수정된 Open 기회" 기준으로 요약 3필드 갱신

**[Problem & Solution] 개발하면서 해결한 문제**
- 계정 리스트뷰에 기회 컬럼을 넣으면 `Could not resolve list view column`(1:다 제약) → 요약필드+Flow로 우회, 기존 26계정 백필

**[QA]**
정상. 단 Opportunity delete 이벤트는 미처리(필요 시 추가).

---

### 7. Lead 전환 시 DART 공시 자동보강

**[Feature] 무엇을 만들었는가?**
리드가 전환되어 생긴 파트너십 계정에, 매출·영업이익·자산총계 등 기업 규모정보를 DART 공시에서 자동으로 채우는 AI 매칭 + 승인 + 보강 파이프라인

**[Business Purpose] 왜 필요한가?**
스폰서 체결을 판단할 규모정보를 담당자가 매번 공시 사이트에서 찾아 넣던 반복 작업을 없애기 위해 필요함.

**[Salesforce] Object / Field / Flow / LWC / Apex / Agent**
Lead·Account / `DART_Corp_Mapping__c`(상장사 3,988건)·`DART_Setting__c` / `DartService`·`DartMatchService`·Queueable·Invocable Apex / Flow `DART_Lead_Convert_Match`·`DART_Account_Approved_Enrich` / Einstein Models API(`sfdc_ai__DefaultGPT4Omni`) / RemoteSiteSetting·PermissionSet

**[How it works] 간단한 동작 흐름**
리드 전환 → 파트너십 Account 생성 → AI가 회사명으로 종목코드 추론해 "검토대기" 제안 → 담당자가 리스트뷰에서 확인·승인 → Flow가 DART API 콜아웃으로 빈 규모정보 필드만 채우고 "보강완료" 처리

**[Problem & Solution] 개발하면서 해결한 문제**
- LLM은 6자리 종목코드, 공시 API는 8자리 corp_code 요구 → 매핑 테이블로 변환, 동시에 실재 검증으로 환각 방지(삼성전자·카카오 등 안정 매칭)
- 프로덕션은 Protected 커스텀세팅 불가 → Public으로, 새 필드는 FLS 없으면 API에서 안 보여 PermissionSet으로 선부여

**[QA]**
프로덕션 E2E 검증 완료(정상). 단 인증키가 Public 커스텀세팅이라 Named Credential 이전은 후속 검토 필요.

---

### 8. Negotiation 서브에이전트

**[Feature] 무엇을 만들었는가?**
Opportunity Agent의 협상 파트로, Proposal 이후 고객사 담당자와 오간 활동을 반영해 Pricebook 등급별 할인율에 맞춘 협상안을 만들어주는 서브에이전트

**[Business Purpose] 왜 필요한가?**
담당자가 감으로 정하던 할인·협상 조건을, 실제 대화 이력과 등급 기준 위에서 일관되게 잡기 위해 필요함.

**[Salesforce] Object / Field / Flow / LWC / Apex / Agent**
Opportunity Agent / Negotiation 서브에이전트 / Pricebook·PricebookEntry(등급별 할인율) / Activity(협상 근거)

**[How it works] 간단한 동작 흐름**
기회가 Proposal을 지나면 → 담당자와 오간 활동 이력을 근거로 읽고 → Pricebook 등급 할인율에 맞춰 협상안 초안 생성

**[Problem & Solution] 개발하면서 해결한 문제**
- 근거 없는 할인이 나오지 않도록, Proposal 이후 활동 이력을 그라운딩으로 넣고 할인율을 Pricebook 등급 기준에 묶음

**[QA]**
협상안 생성 동작 확인. 통합·오케스트레이션은 Opportunity Agent 담당(도은영)과 연계되며, 현재 활성 Agent 버전에서의 쓰기 전 과정은 재확인 권장.

---

### 9. 소유권 이관 · Opportunity 공유

**[Feature] 무엇을 만들었는가?**
PRM 데이터의 소유자를 매니저로 이관하고, 팀이 스폰서십 기회를 볼 수 있도록 공유 구조 구성

**[Business Purpose] 왜 필요한가?**
데모·운영의 주체가 구단 매니저이고, Private 기회를 팀이 함께 봐야 하기 때문에 필요함.

**[Salesforce] Object / Field / Flow / LWC / Apex / Agent**
Account·Contact·Opportunity Owner 이관(300건, → Manager Lee) / Public Group `Partnership_Team` / Opportunity Sharing Rule / AccountPlan 오브젝트 권한(Permission Set)

**[How it works] 간단한 동작 흐름**
소유권 300건 이관 → OWD=Private + Role 없는 계정을 위해 Public Group + Sharing Rule로 Read/Write 공유

**[Problem & Solution] 개발하면서 해결한 문제**
- 소유자를 옮겨도 Role이 없어 못 보던 기회를, Public Group + Sharing Rule로 접근 부여
- Account Planning 탭이 비던 원인이 오브젝트 권한 부재라 Permission Set으로 부여

**[QA]**
이관·공유 후 매니저 조회/편집 권한 확인. 정상.

---

### 10. 파트너십 샘플 데이터 구축

**[Feature] 무엇을 만들었는가?**
파이프라인·화면이 실제 규모에서 동작하도록 파트너 더미와 스폰서십 계약 이력 5년치, 관련 리스트 데이터를 구축

**[Business Purpose] 왜 필요한가?**
"매년 갱신되는 장기 파트너십"과 갱신율·N년차 파트너를 데이터로 보여주기 위해 필요함.

**[Salesforce] Object / Field / Flow / LWC / Apex / Agent**
Account·Contact·Opportunity 각 100 / 계약 이력 2020~2024(Opp ~253·LineItem ~299) / Order ~220·OrderItem ~298·Asset ~99·Contract 78·AccountPlan 50

**[How it works] 간단한 동작 흐름**
앵커 스폰서는 매 시즌 갱신, 2차 스폰서는 중도 합류로 시계열 구성 → Closed Won마다 라인아이템·Order·Asset을 붙여 상품·정산·보유 권리로 연결

**[Problem & Solution] 개발하면서 해결한 문제**
- 이 Org의 Order에 `OpportunityId`가 없어, Description에 `SPN-AUTO|<oppId>` 마커로 추적(단 long-text라 SOQL 필터 불가)

**[QA]**
데이터 적재·분포 확인 정상. 데이터는 **DART OpenDART API 연동분 외 전부 더미**.
