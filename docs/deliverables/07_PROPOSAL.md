# 07_PROPOSAL — Cloud Alpacas 프로젝트 기획서

---

## 1. 프로젝트 배경

우리 팀 **Cellsforce**는 가상의 프로야구 구단 **Cloud Alpacas**의 **Fan Relationship Management(FRM) Team**이 되어, Salesforce Customer 360을 설계·구현한다 (`00_STORY.md` §3).

이 프로젝트는 Salesforce 기능을 학습하기 위한 것이 아니라, **실제 기업 프로젝트처럼 Cloud Alpacas의 팬 데이터를 하나로 연결하고, 팬을 이해하며, 적절한 시점에 가장 적합한 경험을 제공하는 Customer 360 플랫폼**을 만드는 것이 목표다.

프로젝트는 두 단계로 나뉜다.

| 단계 | 초점 | 한 줄 요약 |
|---|---|---|
| **Phase 1** | B2C — Fan 360 | 신규 팬을 이해하고 충성 팬으로 성장시켜 Fan Lifetime Value를 높인다 |
| **Phase 2** | B2B — Sponsorship Sales | Phase 1이 쌓은 Fan 360 데이터로 팬덤의 광고 가치를 발견하고, 이를 실제 스폰서십 Sales Pipeline과 매출로 연결한다 |

Phase 2는 Phase 1의 목표를 대체하지 않고 그 위에 새로운 목표를 더한다. Cloud Alpacas는 팬이 늘고 있음에도 구단 재정 운영상 적자 상황이며, **팬을 키우는 것만으로는 구단의 지속 가능성 문제가 풀리지 않는다**는 인식이 Phase 2의 출발점이다.

---

## 2. Pain Point — Salesforce 도입 전 Cloud Alpacas의 문제

### 2.1 Phase 1 (B2C — Fan 360)

1. **팬 정보를 한눈에 볼 수 없다.** 티켓·굿즈·멤버십·앱·문의 데이터가 서로 다른 시스템에 흩어져 있어, "팬은 보이지 않고 데이터만 보인다."
2. **팬을 이해하지 못한다.** 이루키가 특정 선수를 좋아하는지, 직관을 자주 오는지, 굿즈를 샀는지를 연결해서 볼 수 없다 — 360° Fan View가 없다.
3. **팬을 세분화하지 못한다.** 누가 Ticket Only Fan인지, 멤버십 후보인지, VIP 후보인지 자동으로 알 수 없어, 결국 모든 팬에게 같은 이벤트·쿠폰·메시지를 보낸다.
4. **적절한 타이밍을 놓친다.** VIP가 될 가능성이 높은 팬도 엑셀을 정리한 뒤에야 발견한다 — "한 달 전에 알았으면…"
5. **무엇을 해야 할지 우선순위를 알 수 없다.** 신규 팬이 대량으로 유입돼도 누구에게 굿즈를, 멤버십을, 시즌권을 권해야 하는지 판단할 수 없다 — 데이터는 많지만 Action이 없다.

### 2.2 Phase 2 (B2B — Sponsorship Sales)

1. **팬은 늘고 있는데 왜 적자인가?** 티켓·멤버십·굿즈 매출만으로는 구단 재정 적자를 해결하지 못한다.
2. **어떤 기업이 우리 팬덤에 광고비를 지불할 가능성이 높은지 알 수 없다.** "유명한 회사"에 무작정 제안서를 보내는 것과, 실제로 광고 가치가 있는 기업을 찾는 것은 다르다.
3. **우리 팬이 실제로 무엇에 관심 있는지 모른 채 영업하게 된다.** 팬이 어떤 상품·브랜드·선수·콘텐츠에 반응하는지 정리된 데이터 없이 감·인맥에 의존한다.
4. **후보 기업과 팬층의 광고 Fit을 검증할 방법이 없다.** "이 브랜드의 타겟 고객층이 우리 팬덤과 정말 겹치는가?"를 확인할 근거가 없다.
5. **추천된 기업 중 실제로 영업을 시작할 가치가 있는 곳을 가려낼 방법이 없다.** Fit이 높다고 곧바로 계약 가능성이 높은 것은 아니다.
6. **Pipeline과 실제 계약(Revenue)으로 이어지는 흐름을 관리할 방법이 없다.** 각 단계가 어디서 막히는지, 목표 매출 대비 얼마나 부족한지 한눈에 볼 수 없다.
7. **과거 잘못된 타깃 가정으로 진행한 장기 스폰서 캠페인이 기대만큼 성과를 내지 못한 경험이 있다.** "야구 팬은 40~50대 남성"이라는, 데이터로 검증하지 않은 가정에 따라 진행했기 때문이다. 이 경험이 이번에 Fan 360 데이터를 근거로 삼는 방식을 택하게 된 배경이다.

---

## 3. 프로젝트 목표

### 3.1 Phase 1 Business Goal

> **신규 팬을 이해하고, 적절한 시점에 개인화된 액션을 통해 충성 팬으로 성장시키고, 장기적으로 시즌권 구매까지 이어지는 Fan Lifetime Value를 높인다.**

Demo에서는 FRM Manager인 **김매니저**가 신규 팬 **이루키**를 충성 팬으로 성장시키는 과정을 보여준다.

### 3.2 Phase 2 Business Goal

> **Phase 1에서 쌓은 Fan 360 데이터를 활용해 팬덤의 광고 가치를 발견하고, Cloud Alpacas에 광고비/스폰서십 비용을 지불할 가능성이 높은 기업을 발굴해, 이를 실제 Sales Pipeline(Lead → Opportunity → Contract)으로 연결함으로써 구단의 Sponsorship Revenue를 늘린다.**

핵심은 "Collaboration을 잘할 기업을 찾는 것"이 아니라 **"광고비/스폰서십 비용을 지불할 가능성이 높은 기업을 발굴하는 것"**이다.

### 3.3 FRM Team의 Mission

> "우리는 고객이 아니라 팬을 관리한다."

팬 데이터를 기반으로 팬의 현재 상태를 이해하고, 가장 적절한 다음 행동(Next Best Action)을 실행하여 Fan Lifetime Value를 높인다. Phase 2에서는 이 이해를 구단의 B2B Sponsorship Sales 의사결정에도 활용한다.

---

## 4. Persona

| Persona | 역할 | 설명 |
|---|---|---|
| **김매니저** | Cloud Alpacas FRM Manager (Salesforce User) | 팬 데이터를 분석해 팬을 이해하고, 가장 적절한 Next Best Action을 실행해 신규 팬을 충성 팬으로 성장시킨다. |
| **이루키** | 27세 직장인, 신규 팬 (Customer) | 야구를 거의 본 적 없다가 SNS에서 우연히 한 선수의 영상을 보고 Cloud Alpacas에 관심을 갖는다. 친구와 첫 직관을 경험하고, 응원 문화와 경기장 분위기에 빠져 점점 팬이 되어간다. |
| **이 매니저** (가칭) | Cloud Alpacas Sponsorship Sales Manager | 팬덤의 광고 가치를 근거로 새로운 광고주·스폰서를 발굴하고 실제 계약(Revenue)으로 연결하는 책임을 맡는다. (세부 프로필 TBD) |

---

## 5. 프로젝트 범위

> 범위는 `00_STORY.md` / `01_PROJECT.md` 에서 정의한 내용을 기준으로 한다. 현재 Org에 구현된 기능을 보고 범위를 다시 정의하지 않는다.

### 5.1 Phase 1 — B2C Fan 360 (MVP)

- **Customer 360** — 이루키의 행동(티켓·입장·굿즈·관심·문의)을 한 화면에서 연결
- **Fan Profile / Fan Timeline** — 팬이 누구이고 어떤 여정의 어디에 있는지
- **Fan Segmentation** — 팬의 현재 상태(Life Cycle) 정의
- **Recommendation (Next Best Action)** — 시스템이 생성한 개인화 추천
- **Campaign / 알림** — 세분화 → 수신 동의 확인 → 발송
- **Demo용 Fan App** — 티켓 구매·체크인·굿즈 구매 등 이벤트를 생성해 Salesforce에 데이터를 전달하는 **Demo용 채널** (프로젝트의 주인공은 아님)

> Domain은 5개로 구분한다: **Fan / Operations / Marketing / Service / Partnership** (`01_PROJECT.md` §1). Domain은 명사가 어떤 업무 관심사에서 나왔는지를 보여주는 라벨이며, 서로 겹치지 않는 상자가 아니다 (예: `Campaign`은 Marketing에서도 Partnership에서도 쓰인다).

### 5.2 Phase 2 — B2B Sponsorship Sales (확장)

- **Fan Insight** — Fan 360 데이터로 팬덤의 광고 가치 분석 (별도 저장소가 아니라 Phase 1 Fan Analytics 데이터를 활용하는 분석 과정)
- **기업 Matching** — 기업 데이터(약 100개)와 팬층 특성을 매칭해 Top 후보 추천 + Recommendation Reason
- **Outbound Lead** — 추천 후보 중 담당자가 실제 영업 대상으로 **선택한 기업만** Lead로 등록
- **Lead Qualification / Lead Score** — 실제 계약 가능성 판단
- **Account / Contact → Opportunity → Sponsorship Package / Quote / Negotiation → Contract**
- **Pipeline / Revenue Dashboard** — 목표 매출 대비 부족 금액, Stage별 현황 등 전체 현황 집계

### 5.3 이번 범위에서 다루지 않는 것 (Future Scope)

`00_STORY.md` §8.4 기준:

- 계약 이후 실제 광고 효과·팬 반응 성과 분석
- 성과가 낮은 Sponsorship의 재검토 / 관계 종료 (판단 기준 TBD)
- 첫 계약 이후 장기 재계약 / Partnership 전환
- Collaboration을 실행 수단으로 쓸 경우의 성공 기준 / KPI

> `01_PROJECT.md` §3.4 에서 검토했으나 Entity(별도 Object)로 만들지 않고 속성(필드)으로 남기기로 한 후보: Seat Grade, Channel, Product Category, Membership Card, Refund/Cancellation 등.

---

## 6. 주요 기능 / 서비스 구성

### 6.1 Phase 1 — 이루키의 Customer Journey

```
SNS → 회원가입 → 첫 티켓 구매 → 첫 직관 → 첫 굿즈 구매 → 재방문 → 멤버십 가입 → 충성팬
```

김매니저는 Customer 360으로 이루키가 이 여정의 어디에 있는지 확인하고, 가장 적절한 시점에 개인화된 Action을 실행한다.

**팬의 현재 상태(Current Segment — Life Cycle)**

| Segment | 정의 | 주요 Action |
|---|---|---|
| New Fan (미활성) | 가입만 하고 아직 행동 없음 | 첫 티켓 구매 유도 |
| Active Fan | 최근 90일 활동 | 개인화 추천 |
| At-Risk Fan | 활동 감소 | 이탈 방지 |
| Dormant Fan | 181~365일 활동 없음 | 복귀 캠페인 |
| Churned Fan | 365일 이상 활동 없음 | 저빈도 재활성화 |
| Unreachable Fan | 수신 불가 | 동의/연락처 관리 |

**FRM Team의 Next Best Action (Phase 1)**

| 이루키의 상태 | FRM Team Action |
|---|---|
| 회원가입만 함 | Welcome Campaign |
| 티켓 구매 안 함 | First Ticket Campaign |
| 첫 직관 완료 | First Visit Guide |
| Ticket Only Fan | First Merchandise Campaign |
| 굿즈 구매 완료 | Favorite Player Campaign |
| 재방문 시작 | Membership Campaign |
| 충성 팬 | Season Ticket Recommendation *(향후)* |
| At-Risk Fan | Win-back Campaign *(향후)* |

### 6.2 Phase 2 — B2B Sponsorship Sales Journey

```
Fan 360 Data 분석 → 팬덤의 광고 가치 발견 → 기업 데이터(약 100개) → Matching / Top 10 추천
→ Outbound Lead → Lead Qualification / Lead Score → Account/Contact → Opportunity
→ Sponsorship Package / Quote → Negotiation → Closed Won → Contract / Sponsorship Revenue
→ Pipeline / Revenue Dashboard
```

1. **Fan 360 분석 → 팬덤의 광고 가치 발견.** 예: 특정 팬층이 뷰티·라이프스타일·F&B 콘텐츠에 높은 관심을 보인다 → "어떤 산업의 기업이 광고 가치가 있을지"의 근거.
2. **기업 데이터 → Matching → Top 추천.** 기업 데이터(약 100개)와 Fan Insight를 매칭해 Top 후보와 **Recommendation Reason**을 제시. 대표 예시: **d'Alba(달바)** — 뷰티/스킨케어 브랜드.
3. **Outbound Lead 선정.** 추천 후보는 아직 Lead가 아니다. 담당자가 실제 영업 대상으로 선택한 기업만 Lead가 된다.
4. **Lead Qualification / Lead Score.** 담당자의 의사결정 권한, 접촉 이력, 예산 등 **실제 영업 활동**을 근거로 계약 가능성을 평가.
5. **Account/Contact 전환 → Opportunity 생성** (예: "d'Alba × Cloud Alpacas — Advertising Sponsorship").
6. **Sponsorship Package / Quote 제안 → Negotiation.** 구장 광고, 전광판/펜스 광고, 공식 SNS 노출, Brand Day, 프로모션 등 "무엇을 얼마에 파는가".
7. **Closed Won → Contract / Sponsorship Revenue → Pipeline / Revenue Dashboard.**

> **중요한 개념 구분 — Fit/Recommendation Score ≠ Lead Score**
>
> | | Fit / Recommendation Score | Lead Score |
> |---|---|---|
> | 질문 | 우리 팬덤과 이 기업이 잘 맞는가? | 이 Lead가 실제로 계약까지 이어질 가능성이 높은가? |
> | 근거 | Fan 360 데이터, Target Segment, Segment Match | 담당자 권한, 직무/역할, 접촉 이력, 반응, 예산 등 |
> | 산출 시점·주체 | Matching 단계에서 자동 산출 | 담당자의 실제 영업 활동 결과 |
>
> Fit이 높아도, 실제 담당자와 접촉하고 예산·의사결정권을 확인해야 진짜 Lead Score가 만들어진다.

---

## 7. 기대효과

> `00_STORY.md` / `01_PROJECT.md` 에 정의된 것만 재구성한다. 추측성 ROI·매출 증가율·사용자 증가율은 넣지 않는다.

### 7.1 Phase 1 — FRM Team KPI

- 신규 팬 활성화율
- 첫 경기 관람 전환율
- 재방문율
- 첫 굿즈 구매율
- 멤버십 가입률
- 시즌권 구매 전환율
- Fan Lifetime Value

### 7.2 Phase 1 — 정성적 기대효과

- **팬이 보인다.** 흩어진 데이터가 한 팬의 프로필·타임라인으로 연결된다 (Pain Point 1·2 해소).
- **팬을 구분해서 대한다.** 모든 팬에게 같은 메시지를 보내는 대신, 팬의 상태에 맞는 Action을 실행한다 (Pain Point 3 해소).
- **타이밍을 잡는다.** VIP 후보·이탈 위험 팬을 엑셀 정리 없이 적시에 발견한다 (Pain Point 4 해소).
- **데이터가 Action으로 이어진다.** "누구에게 무엇을 제안할지"의 우선순위가 시스템에서 나온다 (Pain Point 5 해소).

### 7.3 Phase 2 — 기대효과

- **감이 아니라 데이터에서 출발하는 B2B 영업.** 팬덤의 관심사(뷰티/라이프스타일/F&B 등)가 기업 매칭의 근거가 된다 (Pain Point 2·3·4 해소).
- **Fit과 계약 가능성을 구분한다.** 추천 후보를 그대로 영업하지 않고, 실제 계약 가능성을 별도로 평가한다 (Pain Point 5 해소).
- **Pipeline이 보인다.** 후보 발굴부터 계약까지 각 단계와 목표 매출 대비 부족분을 한눈에 확인한다 (Pain Point 6 해소).
- **새로운 수익원.** 팬 성장과 구단 재정 사이의 간극을 Sponsorship Revenue로 메우기 시작한다 (Pain Point 1 해소).
- **과거 실패를 반복하지 않는다.** 검증되지 않은 타깃 가정 대신 실제 Fan 360 데이터로 광고 가치를 판단한다 (Pain Point 7 해소).

---

## 8. 프로젝트 방향 / 핵심 가치

### 8.1 Business First — 사고의 흐름 (`01_PROJECT.md` §0·§7)

```
Business (실제 업무) → Domain (업무를 묶는 관점) → Entity (업무에 등장하는 명사) → Salesforce (그 명사를 어떤 Object로 만들 것인가)
```

기능부터 생각하지 않는다. Object를 먼저 만들거나 자동화부터 구현하지 않고, 항상 "왜 이것이 필요한가?"를 먼저 설명한 뒤 "Salesforce에서는 어떻게 구현하는가?"를 설명한다.

- **Workflow는 Story가 놓친 명사를 드러내고, 과하게 나눈 명사를 정리해준다.**
- **Entity를 만드는 것과 Salesforce Object로 구현하는 것은 다른 결정이다.** "업무에 명사로 등장한다"가 자동으로 "Custom Object가 필요하다"를 뜻하지 않는다 — "이 정보가 자기만의 생애주기·이력을 갖는가", "이 정보를 근거로 자동화를 실행할 것인가"로 나눠서 판단한다.

### 8.2 Phase 2 핵심 메시지

> **"팬을 이해하고, 기업을 찾아, 계약으로 연결하다."**

B2B는 별도의 독립 CRM이 아니라, 기존 Fan 360을 Sponsorship Sales에 활용하는 확장이다:

> **B2C Fan Activity → Fan 360 Insight → B2B Sponsorship Sales Decision**

---

## 부록. 이 문서가 재구성한 원본 매핑

| 07_PROPOSAL 섹션 | 원본 근거 |
|---|---|
| 1. 프로젝트 배경 | `00_STORY.md` §1·§3, `01_PROJECT.md` 서두 |
| 2. Pain Point | `00_STORY.md` §2 (P1 5개), §2 [P2] (P2 7개) |
| 3. 프로젝트 목표 | `00_STORY.md` §1, §1 [P2], §3 (FRM Team Mission·KPI) |
| 4. Persona | `00_STORY.md` §4 |
| 5. 프로젝트 범위 | `00_STORY.md` §5(P1 MVP 성격), §8.4(Future Scope) / `01_PROJECT.md` §1(5 Domain), §2.7, §3.4, §8 |
| 6. 주요 기능 / 서비스 구성 | `00_STORY.md` §5·§6·§7 (P1 Journey·Segment·NBA), §8·§9 (P2 Journey) / `01_PROJECT.md` §2.7·§8.1 |
| 7. 기대효과 | `00_STORY.md` §3 (KPI), §2·§2[P2] (Pain Point 해소 대응) |
| 8. 프로젝트 방향 / 핵심 가치 | `01_PROJECT.md` §0·§7·§8 (Business→Domain→Entity→Salesforce 사고 흐름) / `00_STORY.md` §8 (Phase 2 핵심 메시지) |
