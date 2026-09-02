# Cloud Alpacas AI CRM 프로젝트 최종 발표·데모 시나리오


## 13. 구현 결과 및 데모의 전체 이야기

### 한 줄 시나리오

> 관객의 팬 참여에서 시작된 데이터가 김매니저의 Fan Insight를 거쳐 d’Alba Lead로 이어지고, 김하나와의 Zoom 미팅과 Opportunity Agent를 통해 계약·재계약으로 전환된다.

### 데모 구성 원칙

각 Scene은 다음 순서로 설명한다.

> **문제 → 기능 → 사용 장면 → 자동화·데이터 변화 → 개선 효과**

단순히 화면을 차례로 보여주지 않는다.

---

## 14. Demo Scene 1 - 팬 참여로 이야기를 시작하다

### 문제

팬의 행동이 여러 채널에 분산돼 마케팅과 영업의 근거로 활용되지 않는다.

### 기능

관객 QR 이벤트와 Fan Interaction

### 사용자와 업무 상황

관객이 Cloud Alpacas 팬의 입장에서 문태양 선수 퀴즈에 참여한다.

### 사용 장면

- QR 접속
- 닉네임과 정답 제출
- 마지막 당첨자 추첨 안내

### 데이터 변화

Salesforce Campaign 연동이 실제로 검증된 경우에만 Campaign Member 또는 응답 데이터 생성을 설명한다.

### 개선 효과

팬 참여를 일회성 이벤트가 아니라 이후 개인화와 분석에 활용할 수 있는 데이터로 바라보게 된다.

### 방식

PPT + 관객 참여

---

## 15. Demo Scene 2 - 김매니저가 개인화된 팬 Action을 실행하다

### 문제

모든 팬에게 동일한 메시지를 보내고, 어떤 팬에게 지금 행동해야 하는지 판단하기 어렵다.

### 기능

- Recommendation Hub
- Segment
- Fan 360
- AI 개인화 메시지
- Fan Insight

### 사용자와 업무 상황

김매니저는 우선 대응할 팬을 확인하고, 대표 팬 이루키에게 적합한 메시지를 발송한다.

### 데모 영상 ①

권장 길이: 80~90초

### 영상 순서

1. Recommendation Hub 진입
2. 우선 대응 Segment 확인
3. 대표 팬 이루키 선택
4. Fan 360에서 방문·구매·선호 선수 확인
5. AI 개인화 메시지 생성
6. 김매니저 확인
7. 메시지 발송 결과 확인
8. Fan Insight에서 20·30대 여성 팬층 확인

### 자동화·데이터 변화

- 대상 팬이 Segment 조건에 따라 조회된다.
- 팬 데이터에 맞는 메시지가 생성된다.
- 발송 또는 실행 결과를 확인한다.
- 집계된 팬 행동에서 뷰티 관심 신호를 확인한다.

### 개선 효과

AS-IS의 일괄 마케팅이 팬 상태와 행동에 따른 개인화 Action으로 전환된다.

### 발표 멘트

> “AI는 팬을 분류하고 끝나지 않습니다. 왜 지금 이 팬에게 행동해야 하는지 보여주고, 개인화 메시지를 작성해 실제 업무까지 연결합니다.”

> “김매니저는 개별 팬 관리에서 한 단계 더 나아가, 최근 20·30대 여성 팬층의 성장과 뷰티 관심을 발견했습니다.”

### 담당자 표기

`Fan Insight & Recommendation - Sara`

---

## 16. Demo Scene 3 - Fan Insight가 B2B 업무로 전달되다

### 문제

B2C팀이 팬 인사이트를 발견해도 B2B 영업 담당자에게 적시에 전달되지 않는다.

### 기능

Salesforce와 Slack의 업무 연결

### 사용자와 업무 상황

김매니저가 발견한 20·30대 여성 팬 및 뷰티 관심 인사이트를 이매니저에게 전달한다.

### 라이브 ①

권장 시간: 40~50초

### 라이브 순서

1. Fan Insight 화면을 미리 열어둔다.
2. Insight 전달 작업을 실행한다.
3. Slack 채널로 전환한다.
4. 신규 메시지 도착을 확인한다.
5. 핵심 내용과 연결 링크를 보여준다.

### Slack 메시지 예시

> **신규 Fan Insight가 도착했습니다.**  
> 최근 20·30대 여성 팬층에서 높은 구매·참여 신호와 뷰티 카테고리 관심이 확인됐습니다. 관련 스폰서 후보를 검토해주세요.

### 자동화·데이터 변화

- B2C Insight가 Slack 메시지로 전달된다.
- B2B 담당자가 바로 후속 업무를 시작할 수 있다.

### 개선 효과

B2C와 B2B가 별도 부서로 움직이던 구조가 하나의 Revenue Process로 연결된다.

### 발표 멘트

> “B2C에서 발견한 인사이트는 보고서로 끝나지 않습니다. 이매니저의 Slack으로 전달되어 실제 B2B 영업을 시작합니다.”

### 실패 대응

10초 안에 메시지가 도착하지 않으면 동일 시나리오의 백업 영상을 재생한다.

### 담당자 표기

`B2C-B2B Connection with Slack - Sara · Seungwoo`

---

## 17. Demo Scene 4 - 이매니저가 d’Alba를 우선 영업 대상으로 선정하다

### 문제

어떤 기업을 먼저 접촉할지 담당자의 경험과 감에 의존한다.

### 기능

- PRM Dashboard
- AI 개인화 일정
- Tableau
- Fan Fit·Segment Match
- Lead Score
- Lead Convert
- Account AI Enrichment

### 사용자와 업무 상황

이매니저는 오늘의 업무와 Lead 우선순위를 확인하고 d’Alba를 우선 영업 대상으로 선정한다.

### 데모 영상 ②

권장 길이: 90~100초

### 영상 순서

1. PRM Dashboard 진입
2. 개인화된 오늘의 일정 확인
3. Tableau에서 팬층 특성 확인
4. Lead 목록에서 d’Alba 선택
5. Lead Score와 근거 확인
6. Lead Convert
7. Account·Contact 생성
8. AI가 Account의 빈 필드 보완
9. Opportunity 생성

### 반드시 구분할 개념

| 항목 | 의미 |
|---|---|
| Fan Fit·Segment Match | 팬덤과 기업 타깃이 얼마나 잘 맞는가 |
| Lead Score | 실제 접촉·담당자 권한·반응·예산을 고려했을 때 계약 가능성이 얼마나 높은가 |

### 자동화·데이터 변화

- Lead가 Account·Contact로 전환된다.
- 기업의 빈 정보가 보완된다.
- Sponsorship Opportunity가 생성된다.

### 개선 효과

감에 의존하던 스폰서 선정이 팬 데이터와 실제 영업 정보에 기반한 우선순위 업무로 전환된다.

### 발표 멘트

> “d’Alba는 먼저 Cloud Alpacas 팬덤과 높은 적합도를 보여 후보가 됐습니다. 이후 실제 접촉 정보를 반영한 Lead Score에서도 높은 우선순위를 보였습니다.”

### 담당자 표기

`PRM Dashboard & Lead Scoring - Hyejun`

`Account Intelligence - Aaron`

---

## 18. Demo Scene 5 - Stage Guidance가 다음 행동을 제안하다

### 문제

Opportunity 단계별로 무엇을 확인하고 어떤 행동을 해야 하는지 담당자가 수작업으로 판단한다.

### 기능

- Opportunity Record Page
- Stage Progress
- Activity Timeline
- Stage Guidance

### 사용자와 업무 상황

d’Alba Opportunity가 생성됐다. 이매니저는 현재 Stage에서 부족한 정보와 다음 행동을 확인한다.

### 데모 영상 ③

권장 길이: 45~50초

### 영상 순서

1. d’Alba Opportunity 진입
2. 현재 Stage 확인
3. Stage Guidance 확인
4. 확인된 정보와 부족한 정보 표시
5. 다음 추천 행동 확인
6. Activity Timeline으로 전환

### 자동화·데이터 변화

이 Scene은 읽기 전용이다. AI 가이드를 확인하되 Opportunity 데이터를 변경하지 않는다.

### 개선 효과

Stage마다 달라지는 업무 판단을 일관되게 지원하고, 누락 가능성을 낮춘다.

### 발표 멘트

> “Stage Guidance는 현재 Opportunity의 실제 정보를 바탕으로 지금 단계에서 부족한 정보와 다음 전략을 선제적으로 보여줍니다.”

### 담당자 표기

`Stage Guidance & Opportunity Workspace - Eunyeong`

---

## 19. Demo Scene 6 - Zoom 대화가 자동으로 영업 데이터가 되다

### 문제

미팅이 끝난 뒤 영업 담당자가 내용을 직접 정리해야 하고, 고객의 요구와 위험 신호가 누락될 수 있다.

### 기능

- Zoom 연동
- Activity 자동 기록
- Activity Summary
- Interaction Intelligence
- 고객 Signal 분석

### 역할

| 역할 | 담당 |
|---|---|
| 발표·이매니저 | 도은영 |
| d’Alba 김하나 | 관중석 팀원 1명 |
| 화면 조작 | 도은영 |
| 실패 시 영상 재생 | 도은영 |

김하나 역할 팀원은 발표자가 아니라 Demo Actor다.

### 라이브 ②

권장 시간: 약 3분

### Zoom 대화

약 45~50초로 고정한다.

**이매니저**

> “지난번 전달드린 Cloud Alpacas 팬 분석 자료는 어떻게 보셨나요?”

**김하나**

> “20·30대 여성 팬이 빠르게 늘고 있다는 점은 저희 뷰티 타깃과 잘 맞았습니다. SNS 노출과 Brand Day 구성에는 관심이 있습니다.”

**이매니저**

> “이번 시즌에는 전광판과 SNS 콘텐츠, Brand Day를 함께 구성할 수 있습니다.”

**김하나**

> “다만 올해 예산은 제한적입니다. 실제 노출과 팬 반응을 확인할 수 있어야 하고, 첫해 성과가 좋으면 다년 계약도 검토할 수 있습니다.”

**이매니저**

> “그럼 세부 구성과 측정 지표를 정리해서 다음 주에 제안드리겠습니다.”

### 자동화·데이터 변화

| 고객 발언 | 생성·분석될 정보 |
|---|---|
| 팬층과 뷰티 타깃이 잘 맞음 | 긍정 Signal |
| SNS와 Brand Day 관심 | 상품 요구사항 |
| 올해 예산 제한 | 위험 Signal |
| 팬 반응 측정 요구 | 의사결정 조건 |
| 성과가 좋으면 다년 계약 | 장기 Opportunity |
| 다음 주 제안 검토 | Next Step |

### 결과 확인

- Zoom Meeting과 Opportunity 연결
- Activity 생성
- 미팅 Summary
- 고객 요구사항
- 긍정·위험 Signal
- 다음 행동

### 개선 효과

미팅 후 수기 기록을 줄이고, 고객의 실제 발언을 다음 영업 행동의 근거로 활용한다.

### 발표 멘트

> “고객이 말한 요구사항과 위험 신호가 Activity에 연결되고, 다음 행동의 근거가 됩니다.”

### 처리 대기

1. Zoom 종료
2. ‘대화가 어떻게 데이터가 되는가’ 슬라이드를 약 20초 설명
3. Salesforce Activity 화면으로 이동
4. 결과 확인

리허설을 통해 실제 생성 시간을 측정한다.

### 실패 대응

결과가 예상 시간 안에 나타나지 않으면 백업 영상을 재생한다.

### 담당자 표기

`Zoom Integration & Activity Intelligence - Eunyeong`

---

## 20. Demo Scene 7 - Opportunity Agent가 후속 업무를 수행하다

### 문제

영업 담당자가 여러 화면을 확인하며 현재 상태와 다음 행동을 직접 판단해야 한다.

### 기능

- Opportunity 대화형 Agent
- Opportunity Context
- Activity·Signal 조회
- Conversation History
- Activity Assistant
- 참석자 검색
- 사용자 확인 후 Event·Task 생성

### 사용자와 업무 상황

이매니저는 방금 진행된 Zoom 미팅 내용과 d’Alba Opportunity의 다음 행동을 Agent에게 질문한다.

### 라이브 ③

권장 시간: 약 2분 40초

### 프롬프트 1

> “방금 김하나 담당자와 진행한 미팅의 요구사항과 고객 시그널을 요약해줘.”

#### 기대 결과

- SNS·Brand Day 관심
- 초기 예산 제한
- 성과 측정 요구
- 다년 계약 가능성
- 다음 주 제안 준비

### 프롬프트 2

> “현재 d’Alba Opportunity에서 다음 Stage로 넘어가기 전에 확인해야 할 내용을 알려줘.”

#### 기대 결과

- 현재 Stage
- 확인된 사실
- 부족한 정보
- 다음 추천 행동

### 프롬프트 3

> “김하나 담당자와 다음 주 패키지 검토 미팅을 등록해줘.”

#### 기대 결과

1. 김하나 Contact 식별
2. 일정과 Activity 내용 제시
3. 사용자 확인 요청
4. 승인 후 Event 또는 Task 생성
5. Activity Timeline 반영

### 자동화·데이터 변화

- Agent가 현재 Opportunity Context를 사용한다.
- Contact를 식별한다.
- 저장 전 사용자 확인을 받는다.
- 승인 후 Activity를 생성한다.

### 개선 효과

정보 조회, 판단, 후속 Activity 등록이 하나의 대화 흐름으로 연결된다.

### 발표 멘트

> “Agent는 조회와 추천은 바로 수행하지만, 고객 일정이나 계약 조건을 변경하는 작업은 담당자의 확인 없이는 실행하지 않습니다.”

> “이 Agent는 단순한 챗봇이 아니라 현재 Opportunity의 업무를 실제로 수행하는 영업 Assistant입니다.”

### 실패 대응

10초 이상 응답이 없거나 예상 밖 답변이 생성되면 동일 프롬프트의 백업 영상을 재생한다.

### 담당자 표기

`Opportunity Agent & Activity Assistant - Eunyeong`

---

## 21. Demo Scene 8 - 제안과 협상을 거쳐 Closed Won으로 전환하다

### 문제

상품, Quote, 고객 예산, 할인 조건과 활동 정보가 분산돼 협상 판단이 어렵다.

### 기능

- Proposal Assistant
- Sponsorship Product
- Standard Quote
- Negotiation Context
- Negotiation Assistant
- 사용자 확인
- Closed Won

### 사용자와 업무 상황

이매니저는 김하나의 요구사항을 바탕으로 패키지와 Quote를 구성하고 협상을 진행한다.

### 데모 영상 ④

권장 길이: 80~90초

### 영상 순서

1. 고객 요구사항 확인
2. 스폰서십 패키지 추천
3. Product·Quote 연결
4. 고객 예산과 Quote 차이 확인
5. Negotiation Agent의 협상안 제시
6. 사용자 승인
7. 조건 저장
8. Closed Won 전환

### 자동화·데이터 변화

- Opportunity Product가 연결된다.
- Quote가 생성된다.
- 협상 조건이 사용자 승인 후 반영된다.
- Opportunity가 Closed Won으로 전환된다.

### 개선 효과

제안과 협상이 실제 고객 요구와 데이터에 근거하고, 중요 변경은 담당자의 통제 아래 실행된다.

### 발표 멘트

> “AI가 임의로 조건을 바꾸는 것이 아닙니다. 기존 Quote, 고객 예산, 할인 기준과 고객 Signal을 근거로 안을 제시하고, 최종 결정은 영업 담당자가 내립니다.”

### 담당자 표기

`Product & Quote - Seungwoo`

`Negotiation Assistant - Aaron`

`Opportunity Agent Integration - Eunyeong`

### 가격 검증

동일한 `SPN-LED-BRANDDAY` 상품이 자료에 따라 3억 원과 5.5억 원으로 다르게 기록돼 있다.

발표 전 다음 값을 하나로 통일한다.

- Product2
- Pricebook
- Opportunity Product
- Quote
- PPT
- 발표 대사

통일 전에는 구체적인 금액을 말하지 않는다.

---

## 22. Demo Scene 9 - 1년 뒤, 첫 계약을 다년 파트너십으로 확장하다

### 문제

단년 계약 이후 재계약과 업셀 시점을 담당자가 다시 수작업으로 찾아야 한다.

### 기능

- Partnership Plan
- Campaign 구성 추천
- Campaign Dashboard
- Slack 진행률
- 재계약·업셀 Opportunity

### 시간 전환

화면에 크게 표시한다.

> **1년 뒤**

### 사용자와 업무 상황

이매니저는 d’Alba의 계약 만료 시점과 업셀 가능성을 확인한다.

Cloud Alpacas는 지난 시즌 스폰서사를 초청해 Thank You Day 캠페인을 진행한다.

- 지난 시즌 관계와 성과 공유
- 다음 시즌 신규 상품 소개
- 기업별 업셀 패키지 추천
- 상위 티어·다년 계약 제안
- 참여 기업 대상 추가 혜택
- Campaign 진행률과 반응 추적

### 데모 영상 ⑤

권장 길이: 60~70초

### 영상 순서

1. Partnership Plan에서 d’Alba 확인
2. 갱신·업셀 가능성 확인
3. 상위 티어·다년 계약 추천
4. Thank You Day Campaign 확인
5. 캠페인 진행률 확인
6. Slack 진행 상황 확인

### 자동화·데이터 변화

구현이 확인된 범위에서만 다음을 보여준다.

- 갱신 대상 표시
- 업셀 패키지 추천
- Campaign 생성·상태 변화
- Slack 진행 알림

### 개선 효과

첫 계약을 단발성 매출로 끝내지 않고 재계약과 상위 티어 영업으로 연결한다.

### 발표 멘트

> “첫 계약은 매출엔진의 끝이 아니라 시작입니다. 계약과 활동 데이터가 축적될수록 다음 재계약과 업셀도 다시 감이 아니라 데이터에서 출발합니다.”

### 담당자 표기

`Partnership Plan - Aaron`

`Campaign & Slack Progress - Seungwoo`

### 검증 조건

현재 GitHub `main`에서는 장기 재계약이 과거 문서상 Future Scope로 남아 있고 Partnership Plan의 구현 근거도 명확하지 않다.

| 현재 상태 | 발표 방식 |
|---|---|
| Org에서 정상 동작 | 구현 결과로 영상 시연 |
| 일부만 구현 | 구현된 부분만 시연 |
| 화면만 존재 | TO-BE 확장으로 구분 |
| 확인되지 않음 | 발표에서 제외 |

지난 시즌 성과도 실제 지표 또는 ‘발표용 시뮬레이션 데이터’로 명시한다.

---

## 23. 성과 및 마무리

운영진 가이드라인에 따라 핵심 성과를 2~3개로 압축한다.

### 성과 1. 팬 데이터가 개인화된 Action으로 이어졌다

**AS-IS:** 분산된 데이터와 일괄 마케팅

**TO-BE:** Fan 360 → Segment → Recommendation → 개인화 메시지

**가치:** 팬을 분석하는 데 그치지 않고 실제 고객 Action까지 연결한다.

### 성과 2. 팬 인사이트가 실제 스폰서 영업 Pipeline으로 이어졌다

**AS-IS:** 스폰서 후보를 감과 인맥으로 선정

**TO-BE:** Fan Insight → Slack → Lead Score → Account·Opportunity → Quote·Closed Won

**가치:** 팬덤의 특성이 실제 B2B 매출기회의 근거가 된다.

### 성과 3. 고객 대화가 다음 영업 행동으로 자동 연결됐다

**AS-IS:** 미팅 후 수기 기록과 담당자별 판단

**TO-BE:** Zoom → Activity Summary·Signal → Stage Guidance → Opportunity Agent → 후속 Activity

**가치:** 중요한 고객 Signal의 누락을 줄이고, 영업 실행의 속도와 일관성을 높인다.

---

## 24. 정량·정성 KPI 제시 방식

현재 측정되지 않은 효과를 실제 성과처럼 말하지 않는다.

### 발표에서 바로 말할 수 있는 정성 효과

- 분산 정보의 통합
- B2C와 B2B 부서 연결
- 수기 미팅 정리 감소
- 다음 행동 판단 지원
- 쓰기 작업의 사용자 통제
- Pipeline 가시성 향상
- 재계약·업셀 기회 체계화

### 향후 측정할 KPI

- 개인화 메시지 반응률
- 멤버십·굿즈 전환율
- Lead→Opportunity 전환율
- Opportunity Stage 체류 기간
- 미팅 후 Activity 작성 시간
- 스폰서십 수주율
- 재계약률
- 상위 티어 업셀 금액

실제 비교 데이터가 준비된 KPI만 숫자로 제시한다.

---

## 25. 최종 클로징

### 전체 흐름 회수

```text
관객의 팬 행동
→ Fan 데이터
→ 개인화 Recommendation
→ Fan Insight
→ d’Alba Lead
→ Zoom Meeting
→ Activity Intelligence
→ Opportunity Agent
→ Quote·Negotiation
→ Closed Won
→ Campaign·Upsell
```

### 발표 멘트

> “처음 여러분이 남긴 작은 팬 행동은 개인화된 팬 경험으로 이어졌습니다. 팬들의 데이터는 d’Alba라는 스폰서 기회를 만들었고, AI Agent는 그 기회를 계약과 다음 업셀까지 연결했습니다.”

> **“경기 성적은 통제할 수 없지만, 팬 데이터를 매출로 바꾸는 시스템은 설계할 수 있습니다.”**

### 관객 이벤트 마무리

1. 문태양 선수 퀴즈 정답 공개
2. 정답자 중 3명 추첨
3. 상품은 발표 종료 후 전달
4. Q&A로 전환
