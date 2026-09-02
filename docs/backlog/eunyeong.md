# Cloud Alpacas 개인 개발 업무 정리 - 도은영

## B2B 개발

### 1. Opportunity Agent 통합 및 오케스트레이션

**[Feature] 무엇을 만들었는가?**  
사용자 요청을 분석하여 Activity, Deal, Proposal, Negotiation 등 적절한 전문 Assistant로 연결하는 Opportunity Agent 구조

**[Business Purpose] 왜 필요한가?**  
영업 담당자가 하나의 Agent에서 활동 관리, Deal 분석, 제안 및 협상 업무를 자연어로 처리하도록 지원하기 위해 필요함.

**[Salesforce] Object / Field / Flow / LWC / Apex / Agent**  
Opportunity Agent / Agent Router / Activity Assistant / Deal Assistant / Proposal Assistant / Negotiation Assistant / Ambiguous Question / Escalation / Off Topic / Agent 상태 변수 및 확인 단계

**[How it works] 간단한 동작 흐름**  
사용자 질문 입력 → Router가 의도 및 Opportunity 식별 → 전문 Assistant 호출 → 조회 결과 제공 → 쓰기 작업은 사용자 확인 후 실행

**[Problem & Solution] 개발하면서 해결한 문제**

- 여러 Assistant 간 요청이 섞이는 문제를 Router와 역할별 범위 분리로 해결
- 잘못된 Opportunity가 수정되는 위험을 줄이기 위해 Opportunity 식별값과 작업별 확인 상태를 유지하도록 구성

**[QA]**  
통합 구조와 소스는 확인됨. 과거 정상 버전 기록은 있으나 현재 활성 Agent 버전과 실제 대화 실행은 Org에서 재확인 필요.

---

### 2. Opportunity Stage Guidance

**[Feature] 무엇을 만들었는가?**  
현재 Opportunity Stage와 실제 Deal 정보를 바탕으로 다음 영업 행동을 제안하는 읽기 전용 AI 가이드 카드

**[Business Purpose] 왜 필요한가?**  
영업 담당자가 단계별 필수 확인사항을 놓치지 않고 일관된 영업 프로세스를 수행하도록 지원하기 위해 필요함.

**[Salesforce] Object / Field / Flow / LWC / Apex / Agent**  
Opportunity / Quote·Product·Activity 관련 Deal Context / `stageGuidance` LWC / `StageGuidanceController` Apex / `CA_Stage_Guidance_Recommendation` Prompt Template / Einstein

**[How it works] 간단한 동작 흐름**  
Opportunity 데이터 조회 → Controller가 근거 데이터 요약 → Prompt Template 호출 → 현재 Stage에 해당하는 추천 생성 → 카드 형태로 표시

**[Problem & Solution] 개발하면서 해결한 문제**

- AI가 다른 Stage의 행동을 섞는 문제를 Stage별 입력·출력 구조로 분리
- 근거가 없는 내용을 사실처럼 생성하지 않도록 읽기 전용 구조와 `확인 필요` 원칙 적용

**[QA]**  
컴포넌트·Apex 테스트와 Stage 분리 검증은 통과. 일부 AI 응답에서 근거 없는 요구사항이나 완료 상태가 생성된 이력이 있어 최신 Prompt의 환각 방지 검증은 수정 및 재검증 필요.

---

### 3. Activity Assistant 및 Interaction Intelligence

**[Feature] 무엇을 만들었는가?**  
Task·Event 조회·생성·수정, 참석자 검색, 활동 이력 및 기존 Interaction Intelligence를 조회하는 Assistant 기능

**[Business Purpose] 왜 필요한가?**  
영업 활동 기록 누락을 줄이고, 미팅·통화에서 축적된 정보를 다음 영업 행동에 활용하기 위해 필요함.

**[Salesforce] Object / Field / Flow / LWC / Apex / Agent**  
Task / Event / Contact / Lead / `Interaction_Intelligence__c` / `Interaction_Signal__c` / `FindActivityAttendee` / `CA_Create_Opportunity_Activity` / `ActivityIntelligenceController` / Activity Assistant

**[How it works] 간단한 동작 흐름**  
사용자 활동 요청 → Opportunity 및 참석자 확인 → 기존 활동·Intelligence 조회 → 생성·수정 내용 제시 → 사용자 확인 후 저장

**[Problem & Solution] 개발하면서 해결한 문제**

- 이름만 입력된 참석자를 실제 Salesforce Record와 연결하도록 참석자 검색 기능 구성
- Agent가 활동 관리 범위를 넘어 임의로 Deal 분석을 수행하지 않도록 역할과 작업 범위 분리

**[QA]**  
기존 테스트와 과거 E2E 기록 기준 정상. 현재 활성 Agent에서 조회·생성·수정 전 과정은 재확인 필요.

---

### 4. Proposal·Negotiation Assistant 통합

**[Feature] 무엇을 만들었는가?**  
기존 Proposal 및 Negotiation 기능을 Opportunity Agent 흐름과 Opportunity 화면에 연결하고, 저장 전에 확인받는 통합 UX

**[Business Purpose] 왜 필요한가?**  
제안과 협상 과정에서 잘못된 조건이나 할인 정보가 저장되는 위험을 줄이고 업무 흐름을 연결하기 위해 필요함.

**[Salesforce] Object / Field / Flow / LWC / Apex / Agent**  
Opportunity / Quote / Proposal 관련 Apex·Flow / `negotiationContextSummary` / Proposal Assistant / Negotiation Assistant / `proposal_confirmed`·`terms_confirmed` 상태

**[How it works] 간단한 동작 흐름**  
현재 Deal과 기존 Quote 조회 → 제안 또는 협상 조건 제시 → 사용자가 내용 확인 → 명시적 승인 후 저장

**[Problem & Solution] 개발하면서 해결한 문제**

- 여러 Assistant의 결과가 하나의 Opportunity 흐름에서 이어지도록 Context 통합
- 할인·예산·조건이 즉시 수정되지 않도록 명시적 확인 단계 적용

**[QA]**  
통합 구조와 관련 소스는 확인됨. 현재 Agent에서 Proposal·Negotiation 쓰기 전 과정은 재검증 필요. 최초 Assistant 개발 담당자는 별도 팀원이므로 본인 업무는 통합·화면·오케스트레이션 범위로 표기하는 것이 정확함.

---

### 5. Similar Historical Closed Won Deal 조회

**[Feature] 무엇을 만들었는가?**  
현재 Opportunity와 유사한 과거 Closed Won Deal을 찾아 비교하는 기능

**[Business Purpose] 왜 필요한가?**  
과거 성공 사례를 바탕으로 현재 Deal의 전략, 제품 구성 및 다음 행동을 판단하도록 지원하기 위해 필요함.

**[Salesforce] Object / Field / Flow / LWC / Apex / Agent**  
Opportunity / Opportunity Product / `FindSimilarClosedDeals` / Deal Assistant / 유사도 점수 계산 로직

**[How it works] 간단한 동작 흐름**  
현재 Opportunity 정보 조회 → 과거 Closed Won Deal 검색 → 조건별 유사도 계산 → 점수가 높은 Deal과 비교 정보 반환

**[Problem & Solution] 개발하면서 해결한 문제**

- 단순 최신순 조회가 아니라 비교 가능한 속성을 사용하여 유사도를 계산
- AI의 임의 판단에 의존하지 않도록 결정 가능한 점수 계산 로직 적용

**[QA]**  
기존 단위 테스트 기준 정상. 현재 Org 데이터에서 검색 결과의 적절성은 확인 필요.

---

### 6. Opportunity Agent 내장 채팅

**[Feature] 무엇을 만들었는가?**  
Opportunity Record Page에서 Agent와 대화하고 이전 대화 내용을 확인할 수 있는 채팅 UI

**[Business Purpose] 왜 필요한가?**  
영업 담당자가 Opportunity 화면을 벗어나지 않고 Deal 관련 질문과 작업을 수행하도록 지원하기 위해 필요함.

**[Salesforce] Object / Field / Flow / LWC / Apex / Agent**  
`opportunityAgentChat` LWC / `OpportunityAgentChatController` Apex / `CA_Agent_API_PerUser` / Opportunity Agent

**[How it works] 간단한 동작 흐름**  
Opportunity에서 채팅 열기 → 현재 Opportunity Context 전달 → Agent 응답 표시 → 대화 이력 유지 및 조회

**[Problem & Solution] 개발하면서 해결한 문제**

- Agent Context가 다른 Deal과 섞이지 않도록 현재 Opportunity ID 전달
- 사용자별 인증이 필요한 문제를 Per-User 인증 구조로 분리

**[QA]**  
기존 Jest와 Apex 테스트 기준 정상. 현재 사용자 권한, OAuth 및 실제 Agent 호출은 재확인 필요.

---

### 7. Opportunity 업무 화면 및 단계별 UI

**[Feature] 무엇을 만들었는가?**  
영업기회 진행 단계, 활동 이력, 협상 정보, 단계별 가이드와 Agent 진입점을 한 화면에서 확인할 수 있는 Opportunity 업무 화면

**[Business Purpose] 왜 필요한가?**  
영업 담당자가 여러 화면을 이동하지 않고 현재 Deal 상태와 다음 행동을 빠르게 판단하도록 지원하기 위해 필요함.

**[Salesforce] Object / Field / Flow / LWC / Apex / Agent**  
Opportunity / `CA_Opportunity` FlexiPage / `stageProgress` / `activityTimeline` / `negotiationContextSummary` / `stageGuidance` / `opportunityAgentChat`

**[How it works] 간단한 동작 흐름**  
Opportunity 접속 → 현재 Stage와 핵심 정보 조회 → 활동·협상·가이드 확인 → 필요한 경우 Agent 실행

**[Problem & Solution] 개발하면서 해결한 문제**

- 단계별로 필요한 정보가 다른 문제를 Dynamic Forms와 독립 컴포넌트 배치로 해결
- 기존 Stage Progress를 훼손하지 않고 추가 업무 카드를 독립적으로 구성

**[QA]**  
컴포넌트와 페이지 메타데이터 기준 정상. 현재 Org 페이지 할당 및 사용자별 표시 상태는 재확인 필요.

---

### 8. Zoom·Google Meet 연동

**[Feature] 무엇을 만들었는가?**  
Zoom과 Google Meet 미팅 데이터를 Salesforce 영업 활동 및 Conversation Intelligence에 활용할 수 있도록 연결

**[Business Purpose] 왜 필요한가?**  
온라인 미팅 기록과 대화 정보를 Opportunity 후속 활동, 코칭 및 Agent Context에 활용하기 위해 필요함.

**[Salesforce] Object / Field / Flow / LWC / Apex / Agent**  
VideoCall / Conversation 또는 Interaction Intelligence 관련 데이터 / 사용자 권한 세트 / Opportunity 활동 및 Activity Assistant 연계

**[How it works] 간단한 동작 흐름**  
Zoom·Google Meet 미팅 진행 → 미팅 데이터 Salesforce 연동 → 대화·활동 정보 생성 → Opportunity 및 Agent에서 조회

**[Problem & Solution] 개발하면서 해결한 문제**

- 여러 미팅 플랫폼의 연결과 사용자 권한 설정 완료
- 미팅 데이터를 단순 외부 기록이 아닌 영업 활동 Context로 활용할 수 있도록 연계 범위 구성

**[QA]**  
Zoom·Google Meet 연결 완료는 사용자 확인 기준 정상. 실제 녹화·대화 데이터 생성 및 Opportunity 자동 매칭 전 과정은 별도 E2E 확인 필요.

---

### 9. Partnership Inquiry Experience Cloud

**[Feature] 무엇을 만들었는가?**  
외부 파트너가 제휴 문의와 첨부파일을 제출할 수 있는 Experience Cloud 페이지

**[Business Purpose] 왜 필요한가?**  
잠재 파트너의 문의를 Salesforce Lead로 자동 수집하고 영업 후속 조치로 연결하기 위해 필요함.

**[Salesforce] Object / Field / Flow / LWC / Apex / Agent**  
Lead / ContentVersion / 첨부파일 Token Field / `partnershipInquiry` LWC / `PartnershipInquiryController` Apex / Experience Cloud 사이트 `/CApartnership`

**[How it works] 간단한 동작 흐름**  
외부 사용자가 문의 작성 → 첨부파일 업로드 → Lead와 파일 정보 저장 → 내부 담당자가 Salesforce에서 확인

**[Problem & Solution] 개발하면서 해결한 문제**

- 비로그인 사용자의 파일 제출을 처리하기 위해 토큰 기반 연결 구조 적용
- 문의 내용과 첨부파일이 분리되지 않도록 Salesforce Record와 연결

**[QA]**  
사이트 Live 상태는 기록되어 있음. 비로그인 사용자의 실제 제출부터 Lead·파일 생성까지는 현재 환경에서 재확인 필요.

---

# B2C 개발

### 10. Recommendation Segment 및 Fan 360

**[Feature] 무엇을 만들었는가?**  
팬 행동에 따른 4개 추천 세그먼트와 세그먼트별 팬 목록, Fan 360 상세 조회 기능

- 멤버십 전환 대상
- 가입 후 미방문 팬
- 최근 방문 감소 팬
- 충성도가 높지만 굿즈 구매가 없는 팬

**[Business Purpose] 왜 필요한가?**  
모든 팬에게 동일한 마케팅을 하는 대신, 행동 특성에 따라 전환 가능성이 높은 고객군을 빠르게 찾기 위해 필요함.

**[Salesforce] Object / Field / Flow / LWC / Apex / Agent**  
Person Account / `Admission__c` / `Engagement_Signal__c` / `segmentFanList` LWC / `Fan360Controller` / `FanDetailController` / `SegmentFanListItem`

**[How it works] 간단한 동작 흐름**  
팬의 가입·방문·구매·앱 활동 데이터 분석 → 세그먼트 조건 적용 → 대상 팬 목록 표시 → 팬 선택 → Fan 360 상세 화면 조회

**[Problem & Solution] 개발하면서 해결한 문제**

- 추상적인 추천 기준을 실제 Salesforce 데이터로 판별 가능한 조건으로 구체화
- 세그먼트 목록과 Fan 360 상세 화면을 연결하여 마케터가 근거 데이터를 바로 확인하도록 구성

**[QA]**  
관련 소스와 PR 병합은 정상. 현재 Org의 실제 세그먼트 인원수와 최신 데이터 반영 여부는 확인 필요.

---

### 11. B2C Fan App 및 Salesforce 연동

**[Feature] 무엇을 만들었는가?**  
팬 회원가입, 개인정보 동의, 선호 선수 선택, 티켓·멤버십·시즌권·굿즈 조회, 체크인, My 페이지를 포함한 B2C Fan App과 Salesforce 연동 기능

**[Business Purpose] 왜 필요한가?**  
팬의 가입·관심사·구매·방문 행동 데이터를 Salesforce에 통합하여 개인화 마케팅과 팬 분석에 활용하기 위해 필요함.

**[Salesforce] Object / Field / Flow / LWC / Apex / Agent**  
Person Account / `Favorite_Player__c` / `Admission__c` / `Engagement_Signal__c` / OAuth Client Credentials / `signup`, `favorite-player`, `checkin`, `engagement`, `auth` API

**[How it works] 간단한 동작 흐름**  
팬이 앱에서 가입하거나 행동 수행 → Fan App API 호출 → OAuth 인증 → Salesforce 고객·선호 선수·방문·행동 데이터 조회 또는 저장

**[Problem & Solution] 개발하면서 해결한 문제**

- 외부 웹 앱에서 Salesforce 데이터를 안전하게 처리하기 위해 OAuth 기반 서버 연동 구조 적용
- 화면의 팬 행동을 Salesforce 데이터 모델과 연결하여 추천·캠페인에서 재사용할 수 있도록 구성

**[QA]**  
소스와 병합 이력 기준 정상. 운영 API 쓰기, Phone 필드 권한, 일부 경기 ID 매핑은 현재 환경에서 재확인 필요.

---

### 12. 캠페인 실시간 성과 대시보드

**[Feature] 무엇을 만들었는가?**  
캠페인의 발송·반응 현황을 확인할 수 있는 실시간 지표 화면

**[Business Purpose] 왜 필요한가?**  
마케팅 담당자가 캠페인의 도달 및 반응 결과를 빠르게 파악하고 후속 조치를 결정하도록 지원하기 위해 필요함.

**[Salesforce] Object / Field / Flow / LWC / Apex / Agent**  
Campaign / CampaignMember / `CampaignMember.Responded` / `Notification_Log__c` / `campaignBoard` LWC / `CampaignController` Apex

**[How it works] 간단한 동작 흐름**  
캠페인 및 알림 로그 조회 → 발송·응답 지표 집계 → 캠페인 보드에 표시 → 담당자가 성과 확인

**[Problem & Solution] 개발하면서 해결한 문제**

- 여러 Object에 분산된 캠페인 결과를 하나의 화면에서 확인할 수 있도록 집계
- 단순 캠페인 목록이 아닌 실제 반응 데이터를 중심으로 화면 구성

**[QA]**  
소스와 PR 병합 기준 정상. 현재 Org 데이터로 실시간 집계 결과를 다시 확인할 필요가 있음.

---

### 13. Fan App 구매·체크인 사용자 경험

**[Feature] 무엇을 만들었는가?**  
상품 장바구니, 결제 화면, 티켓·시즌권·멤버십 이용, 경기장 체크인 기능

**[Business Purpose] 왜 필요한가?**  
팬이 상품 구매와 경기 관람 행동을 하나의 앱에서 수행하고, 해당 행동을 후속 추천과 캠페인의 근거로 활용하기 위해 필요함.

**[Salesforce] Object / Field / Flow / LWC / Apex / Agent**  
`Admission__c` / `Engagement_Signal__c` / Fan App SPA / 장바구니 및 결제 상태 관리 / Check-in API

**[How it works] 간단한 동작 흐름**  
상품·티켓 선택 → 장바구니와 결제 화면 진행 → 구매 상태 반영 → 경기 방문 시 체크인 → Salesforce 행동 데이터와 연결

**[Problem & Solution] 개발하면서 해결한 문제**

- 여러 상품 유형의 화면 상태를 일관된 구매 흐름으로 통합
- 체크인 결과를 단순 화면 이벤트가 아니라 팬 행동 데이터로 활용할 수 있도록 연동

**[QA]**  
화면 흐름은 기존 테스트 기준 정상. 실제 Salesforce `Order`·`OrderItem` 저장은 구현 범위에 포함되지 않아 추가 개발 필요.