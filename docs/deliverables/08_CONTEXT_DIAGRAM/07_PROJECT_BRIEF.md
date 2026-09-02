# 08_PROJECT_BRIEF — Cloud Alpacas 프로젝트 기획서 (PPT용 4장)

> 이 문서는 **기술 설계서가 아니라 프로젝트 기획서**다. Object/Field/Flow 목록이 아니라
> "왜 시작했는가 → 무엇을 해결하는가 → 무엇을 만들었는가 → 어떤 비즈니스 가치가 생기는가"를 다룬다.
> 각 페이지는 `[페이지 제목 / 핵심 메시지 / 본문 / 시각화 제안]` 구조이며, PPT 1장에 대응한다.
> 근거 문서: `00_STORY.md`(Business Goal·Pain Point), `04_DEMO.md`(구현된 Scene 1~9), `07_PROPOSAL.md`.

---

## 한 줄 요약 (표지 문구)

> **"경기 성적은 통제할 수 없지만, 팬 데이터를 매출로 바꾸는 시스템은 설계할 수 있다."**
> Cloud Alpacas는 흩어진 팬 데이터를 하나로 모아 팬을 성장시키고, 그 팬덤의 가치를 스폰서십 매출로 잇는 **지속 가능한 매출 엔진**을 만든다.

---

## 01. 프로젝트 개요

### 핵심 메시지
1. **팬은 늘어도 구단은 적자다.** 팬 성장이 곧 구단의 지속 가능성으로 이어지지 않는다.
2. **팬 데이터는 많지만 흩어져 있다.** "팬은 안 보이고 데이터만 보인다" — 이해도, 타이밍도, 액션도 없다.
3. **그래서 팬 경험과 구단 매출을 하나의 데이터 흐름으로 연결한다.** 팬을 이해 → 개인화 액션 → 팬덤의 가치를 스폰서 매출로.

### 본문

**프로젝트 배경**
우리 팀 Cellsforce는 한화 이글스를 모델링한 가상 구단 **Cloud Alpacas**의 Fan Relationship Management(FRM) Team이 되어, 팬 데이터를 하나로 연결하는 Salesforce Customer 360을 실제 기업 프로젝트처럼 설계·구현한다.

**Cloud Alpacas의 비즈니스 상황**
- 신규 팬 — 특히 20·30대 여성 팬 — 이 빠르게 늘고 있으나, 이 팬층의 구매력·재방문율은 오히려 낮다.
- 티켓·멤버십·굿즈 매출만으로는 감당이 어려워 구단 재정은 운영상 적자다.
- 과거 "야구 팬 = 40·50대 남성"이라는, 데이터로 검증하지 않은 가정에 따라 장기 스폰서 캠페인을 진행했으나 기대만큼의 성과를 내지 못한 경험이 있다.

**핵심 Pain Point**
1. 팬 정보가 티켓·굿즈·멤버십·앱·문의로 흩어져 **팬을 한눈에 볼 수 없다.**
2. 세분화도 타이밍도 없어 **모든 팬에게 같은 이벤트·쿠폰·메시지**를 보낸다. 데이터는 많지만 Action이 없다.
3. 팬은 느는데 **팬덤의 가치를 구단 매출로 연결할 방법이 없다.** 어떤 기업이 우리 팬덤에 광고비를 낼지 판단할 근거가 없다.

**Business Goal**
- **Phase 1 (B2C):** 신규 팬을 이해하고, 적절한 시점에 개인화된 액션으로 충성 팬으로 성장시켜 **Fan Lifetime Value**를 높인다.
- **Phase 2 (B2B):** Phase 1이 쌓은 Fan 360 데이터로 **팬덤의 광고 가치**를 발견하고, 이를 실제 스폰서십 Sales Pipeline과 매출로 연결한다. (Phase 1 목표를 대체하지 않고 그 위에 더한다.)

**핵심 Value Proposition**
팬 경험과 구단 매출을 **하나의 데이터 흐름(Fan 360 → Fan Insight → Sponsorship Sales)**으로 연결하는 지속 가능한 매출 엔진.

### 시각화 제안
- 상단: **엇갈리는 두 화살표** — "팬 수 ↑" vs "구단 재정 ▼ (적자)". 숫자 대신 방향으로 긴장 표현.
- 중앙: Pain Point 3개를 아이콘으로 — 흩어진 퍼즐 조각 / 확성기(일괄 발송) / 끊긴 다리(팬↔매출).
- 하단: 가는 파이프라인 띠 `Fan 360 → Fan Insight → Sponsorship Sales` (다음 페이지 예고).

---

## 02. 프로젝트 목표 / To-Be

### 핵심 메시지
1. **하나의 흐름이다.** B2C와 B2B는 별개 프로젝트가 아니라 `Fan 360 → Fan Insight → Sponsorship Sales`로 이어진다.
2. **감(感)에서 데이터로.** 팬 관리도, 스폰서 발굴도 경험·인맥이 아니라 팬 데이터에서 출발한다.
3. **분석에서 Action·Revenue로.** 팬을 분류하고 끝내지 않고 실제 행동과 매출까지 연결한다.

### 본문 — FROM → TO

| FROM (AS-IS) | TO (TO-BE) |
|---|---|
| 흩어진 팬 데이터 | **Fan 360** — 한 화면에서 팬을 본다 |
| 감각·경험 중심 팬 관리 | **데이터 기반 Fan Insight** |
| 모두에게 같은 메시지 (일괄 마케팅) | **팬 상태별 개인화 Recommendation / Next Best Action** |
| 팬 데이터와 영업 데이터의 단절 | **Fan Insight 기반 Sponsorship Sales** |
| 감·인맥으로 스폰서 후보 선정 | **팬덤 광고 가치 기반 기업 발굴 + Pipeline** |
| 미팅 후 수기 정리, 판단 누락 | **대화가 자동으로 영업 데이터가 됨** |

관통 원리: **B2C Fan Activity → Fan 360 Insight → B2B Sponsorship Decision.**

### 시각화 제안
- 좌(회색 = AS-IS) / 우(브랜드 컬러 = TO-BE) **2단 대비 표**, 행마다 가운데 화살표.
- 표 아래에 굵은 관통선 하나: `B2C Fan Activity ──▶ Fan 360 Insight ──▶ B2B Sponsorship Decision`.
- 핵심 6줄만, 표 테두리는 최소화.

---

## 03. 핵심 솔루션 / 구현 범위

### 핵심 메시지
1. **4개 비즈니스 영역**으로 묶어 구현했다 — 기능 나열이 아니라 "무엇을 해결하려 무엇을 만들었나".
2. **Standard First** — Salesforce 표준 기능을 먼저 쓰고, 안 될 때만 Custom 개발.
3. 네 영역 모두 **하나의 팬 데이터(One Fan Data)** 위에서 연결된다.

### 본문 — 영역별 "무엇을 해결하기 위해 무엇을 구현했는가"

- **B2C Fan Relationship**
  팬이 흩어진 데이터로만 존재하는 문제를 해결하기 위해, **Fan 360**(프로필·타임라인·선호 선수·구매·방문)과 **Current Segment(Life Cycle)**로 팬의 현재 상태를 정의하고, **Recommendation Hub**에서 "지금 이 팬에게 왜 행동해야 하는지"와 개인화 메시지까지 연결했다.

- **Fan Experience**
  팬 참여가 일회성 이벤트로 소모되는 문제를 해결하기 위해, **QR 기반 참여 이벤트**(선수 퀴즈·응모·추첨)로 팬 행동을 이후 분석과 개인화에 쓸 수 있는 데이터로 전환했다.

- **AI / Agentforce / Automation**
  판단과 정리를 사람이 수작업으로 하는 문제를 해결하기 위해, **개인화 메시지 생성**, **팬–기업 Matching**(Fan Fit·Segment Match·Recommendation Reason), **Stage Guidance**, **Zoom 대화의 자동 Activity·고객 Signal 기록**, **Opportunity Agent**(조회·추천은 즉시 수행, 일정·계약 변경 등 쓰기 작업은 담당자 확인 후)를 구현했다. **Flow + Slack 알림**으로 "팬 상태 변화 → 담당자 액션", "B2C Insight → B2B 영업 착수"를 부서 간에 연결했다.

- **B2B Sponsorship Sales**
  팬덤 가치를 매출로 연결할 Pipeline이 없는 문제를 해결하기 위해, **Fan Insight → 기업 데이터 매칭 → Top 후보 추천 → (담당자가 선택한 기업만) Lead → Lead Score(실제 계약 가능성) → Account/Contact/Opportunity → Sponsorship Package·Quote·Negotiation → Closed Won → Pipeline/Revenue Dashboard**의 흐름을 구축했다.

### 구현 방식 (필요한 만큼만)
- **Standard Salesforce:** Person Account(Fan), Campaign, Lead, Account/Contact, Opportunity, Standard Quote, Contract — B2B Sales는 대부분 표준 세일즈 기능 위에 구축.
- **Custom Development:** 표준으로 안 되는 Fan Analytics와 전용 화면(Fan 360 Dashboard, Recommendation Hub, PRM Dashboard)만 최소한으로.
- **Automation:** Flow + Slack 알림으로 상태 변화와 부서 간 인계를 자동화.
- **Agentforce:** 개인화 메시지, 기업 Matching, Stage Guidance, Opportunity Agent — 분류에서 끝내지 않고 **근거와 다음 행동**을 제시.

### 시각화 제안
- **2×2 사분면** (4개 영역), 중앙에 "One Fan Data" 코어 원.
- 각 영역 박스에 태그 칩: `Standard` / `Custom` / `Automation` / `AI`.
- 하단에 작은 배지: **"Standard First — 표준 우선, 필요할 때만 개발"**.

---

## 04. 대표 시나리오 / 기대효과

### 핵심 메시지
1. **관객이 남긴 팬 행동 하나**가 스폰서 계약까지 이어지는 단일 흐름.
2. **팬을 이해하고(김매니저) → 기업을 찾아(이매니저) → 계약으로 연결한다.**
3. **첫 계약은 끝이 아니라 매출 엔진의 시작**이다 (재계약·업셀).

### 본문 — 대표 흐름 (`04_DEMO.md` Scene 1~9 기준, 구현된 기능만)

1. **팬 참여** — 관객이 QR로 문태양 선수 퀴즈에 참여한다. 팬 행동이 데이터가 된다. *(Scene 1)*
2. **김매니저의 개인화 액션** — Recommendation Hub에서 우선 대응 팬(이루키) 확인 → Fan 360으로 방문·구매·선호 선수 파악 → AI 개인화 메시지 발송. *(Scene 2)*
3. **팬덤 기회 발견** — Fan Insight에서 20·30대 여성 팬층의 성장과 **뷰티 관심 신호**를 확인한다. *(Scene 2)*
4. **B2C → B2B 전달** — 이 Insight가 **Slack으로 이매니저에게 전달**되어 스폰서 검토가 시작된다. *(Scene 3)*
5. **이매니저의 기업 발굴** — PRM Dashboard에서 Lead 우선순위 확인 → **d'Alba**를 Fan Fit + Lead Score 근거로 우선 영업 대상 선정 → Lead Convert → Account/Contact → Opportunity. *(Scene 4)*
6. **영업 실행** — Stage Guidance가 단계별 다음 행동 제안 *(Scene 5)* → Zoom 미팅 대화가 자동으로 Activity·고객 Signal로 기록 *(Scene 6)* → Opportunity Agent가 요약·다음 행동·일정 등록 수행(쓰기는 담당자 확인 후) *(Scene 7)*.
7. **제안·협상·계약** — Sponsorship Package·Standard Quote 구성 → Negotiation Assistant 협상안 → 담당자 승인 후 **Closed Won**. *(Scene 8)*
8. **(확장) 1년 뒤** — Partnership Plan에서 재계약·업셀 기회 확인, Thank You Day Campaign. *(Scene 9 — 구현이 확인된 범위 내에서만 시연)*

> **B2C ↔ B2B 연결점(3~4단계)**이 이 시나리오의 핵심이다. "팬 데이터가 있으니 광고주를 찾는다"가 아니라, "팬 데이터가 팬덤의 관심사(뷰티)를 보여주고, 그 관심사가 기업 매칭의 근거가 된다".

### 기대효과

1. **Fan Lifetime Value 향상** — 흩어진 데이터가 한 팬의 프로필·타임라인으로 연결되고, 분석에서 끝나지 않고 실제 개인화 Action까지 이어진다.
2. **팬 로열티 및 개인화 경험 강화** — 모두에게 같은 메시지 대신 팬 상태에 맞는 Next Best Action을 적시에 실행한다.
3. **팬덤 기반 Sponsorship Revenue 확대** — 팬덤의 특성이 B2B 매출 기회의 근거가 되고, Pipeline이 가시화되며, 첫 계약이 재계약·업셀로 이어진다.

> 보조 정성 효과(발표에서 바로 말할 수 있는 것): 분산 정보 통합 · B2C↔B2B 부서 연결 · 미팅 수기 정리 감소 · 쓰기 작업의 담당자 통제 · Pipeline 가시성.
> 추측성 ROI·매출 증가율은 넣지 않는다. 실제 비교 데이터가 준비된 KPI만 숫자로 제시한다.

### 시각화 제안
- **가로 8단계 타임라인** — 위쪽 절반 B2C(파랑), 아래쪽 절반 B2B(초록), 3~4단계에서 색 전환 지점에 Slack 아이콘.
- 단계별 아이콘: QR / 팬 카드 / 돋보기+막대그래프 / Slack / 회사 빌딩 / 영상통화 / 로봇 / 악수(계약) / 순환 화살표(재계약).
- 하단에 기대효과 3개 카드(아이콘 + 한 줄).

---

## 부록. 자체 검수 — 발표 평가 기준 매핑

| 평가 기준 | 어느 페이지에서 드러나는가 |
|---|---|
| **문제 정의** | 01 핵심 Pain Point (팬↔매출 단절), 02 FROM(AS-IS) |
| **솔루션 설계** | 02 TO-BE, 03 4개 비즈니스 영역 + One Fan Data |
| **기술 구현** | 03 구현 방식(Standard/Custom/Automation/Agentforce), 04 Scene별 기능 |
| **가치 전달** | 01 Value Proposition, 04 기대효과 3개 + 표지 한 줄 |

**연결성 체크:** B2C와 B2B가 별개로 보이지 않도록 모든 페이지에서 `Fan 360 → Fan Insight → Sponsorship Sales` 관통선을 반복 노출한다(01 하단 예고 → 02 관통선 → 03 코어 → 04 타임라인 색 전환).

**표현 원칙 준수:** `04_DEMO.md`에 구현으로 확인된 Scene만 시나리오에 포함했고, Scene 9(재계약·Partnership Plan)는 "확장 / 구현 확인 범위 내 시연"으로 명시했다.
