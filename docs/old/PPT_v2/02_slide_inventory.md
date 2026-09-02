# PPT_v2 · 02_SLIDE_INVENTORY — 19장

> `01_story.md`의 내러티브를 19개 슬라이드로 나눈 목록. 슬라이드별 상세(문구·비주얼·발표자 멘트·전환·금지)는 `03_wireframe.md`.
>
> **총 19장 = CH I 5장 (01–05) + CH II 12장 (06–17, LOCKED) + CH III 2장 (18–19).**
> `06–17`의 **순서 · 주인공 · 핵심 질문 · 핵심 기능 · 표현 방식**은 변경 금지
> (`docs/deliverables/PPT_WIREFRAME/00_WIREFRAME_GUIDE.md` CHAPTER II + `Demo순서.png` + `04_DEMO.md` = Source of Truth).
>
> **19장 이후 = PPT 종료 → Salesforce Org LIVE → 퀴즈 당첨자 발표(실제 Org 화면) → Q&A.**
> Winner / Quiz Result / Thank You / Q&A 슬라이드는 만들지 않는다.

---

## 1. 전체 구조

| Chapter | 슬라이드 | 액센트 | 역할 |
|---|---|---|---|
| **I · WHY** | 01–05 | Slate | 우리가 왜 이 문제·이 이야기를 택했는가 (매우 압축) |
| **II · DEMO SCENARIO** ⭐ | 06–17 | Blue(B2C) → Green(B2B) | 하나의 비즈니스 스토리. 기능 목록 아님. Demo가 본체 |
| **III · SO WHAT** | 18–19 | Navy | 18 무엇을 배웠나(설계 판단 4가지 + Closing 메시지) → 19 우리는 어떻게 사고했나 (typography bridge) |

```
01 Cover · 02 Business Question · 03 What We Saw · 04 Our Approach · 05 How We Built It
06 Demo Map · 07 Live Event · 08 S1 FAN · 09 S2 ACTIVATE · 10 Fan Insight Bridge · 11 S3 CONNECT
12 S4 Partner Matching · 13 S5 PIPELINE · 14 S6 UNDERSTAND · 15 S7 REASON · 16 S8 ACT · 17 S9 EXPAND
18 What We Learned · 19 From Learning to Building
→ (PPT 종료) → Salesforce Org LIVE → 퀴즈 당첨자 발표 → Q&A
```

### 관통 스토리 (모든 슬라이드가 이 흐름의 한 지점)

```
Fan → Fan Activity → Fan 360 → Personalized Action → Fan Insight (Bridge)
→ Partner Matching → Sponsorship Sales → Opportunity → AI Sales → Closed Won → Expansion
```

### 감정 아크

```
의문 → 관찰 → 판단 → (증명: Demo) → 성찰 → 조용한 자신감 → (PPT OFF → Org LIVE)
02     03      04·05    06–17         18       19
```

### 표현 방식 배지 (Demo 슬라이드 상단)

| 배지 | 의미 | Wireframe 처리 |
|---|---|---|
| **PPT** | 일반 슬라이드 (스크린샷 중심) | 스크린샷 영역이 화면의 55~70% |
| **DEMO VIDEO** | 사전 녹화 영상 | 다크 재생 영역 + ▶ + 스크러버가 화면 중심 |
| **LIVE** | 발표 현장 실행 (Salesforce/Slack) | 붉은 톤 프레임 + `● LIVE` 배지 + 백업 영상 명시 |
| **PPT + 5s VIDEO** | 슬라이드 + 짧은 임베드 영상 | PPT + `▶ 5s embedded video` 인셋 |
| **FORMAT TBD** | 표현 방식 미정 (팀 확정 필요) | 노란 `[ FORMAT TBD ]` 박스. 임의 선택 금지 |
| **TRANSITION** | 전환 전용 (Demo 콘텐츠 아님) | 중립 배지 |

---

## 2. 슬라이드 인벤토리

### CHAPTER I — WHY

| # | 제목 | 한 줄 메시지 | 관점 | 표현 | PIV | 절대 넣지 않는 것 |
|---|---|---|---|---|---|---|
| 01 | Cover | **FROM FAN DATA TO REVENUE.** | — | — | — | 이미지·차트·마스코트·부제 설명문 |
| 02 | Business Question | "한국에서 가장 인기 있는 스포츠 중 하나인 야구. 그런데 왜 구단은 적자인가?" | NOTICED | — | Problem | 가짜 시장 통계, 구체 매출 수치 |
| 03 | What We Saw | 데이터가 흩어짐 · 데이터가 액션이 안 됨 · 팬 가치가 B2B에 닿지 않음 | NOTICED | — | Problem | 4개 이상의 pain, 기능 언급, 해법 |
| 04 | Our Approach | **DATA → INSIGHT → ACTION → REVENUE** — 하나로 연결된 Customer 360 | DECIDED | — | Insight | 상세 아키텍처, Object 목록, 수치 |
| 05 | How We Built It | "우리는 기능부터 시작하지 않았다" | DECIDED | — | Insight | 풀 팀 프로필 슬라이드, 빌드 수치 나열, Flow 개수 자랑 |

### CHAPTER II — DEMO SCENARIO (06–17, LOCKED)

| # | 제목 | 핵심 질문 (Headline) | 핵심 기능 | 관점 | 표현 | PIV | 절대 넣지 않는 것 |
|---|---|---|---|---|---|---|---|
| 06 | Demo Map | (질문 없음 — Demo 전체 지도, 10초 이해) | — | — | — | — | 8단계 초과, "Business Opportunity"라는 표현(→ Partner Matching) |
| 07 | Live Event — Game Day | "지금 경기장에서 실제로 팬 참여가 발생 중" | QR 참여 이벤트 (FanQuiz Site) | NOTICED | **LIVE** | Problem | 기능 설명문, Campaign 연동을 검증 전 단정 |
| 08 | S1 · FAN | "우리 팬은 누구인가?" | Fan 360 · Segment · Recommendation Hub | INSIGHT | **PPT** | Insight | 필드 목록 나열, 3축 정의 강의 |
| 09 | S2 · ACTIVATE | "각 팬에게 어떻게 다르게 행동할까?" | AI Personalized Message | ACTION | **DEMO VIDEO** | Action | 미측정 반응률·전환율 |
| 10 | Fan Insight — B2C→B2B Bridge ⭐ | "B2C에서 쌓인 팬 데이터가, 여기서 기업의 기회가 된다" | — (전환 페이지) | INSIGHT | **TRANSITION** | Insight | 스크린샷, B2B 상세, 기능 목록 |
| 11 | S3 · CONNECT | "팬 데이터를 어떻게 B2B 영업 기회로 연결할까?" | Monthly Fan Insight Letter · Slack Agent | INSIGHT | **LIVE** | Insight | Slack 채널 ID 노출, 실패 시 대응 미준비 |
| 12 | S4 · Partner Matching | "이 팬덤과 가장 잘 맞는 기업은? 왜 이 기업인가?" | Fan Fit · Segment Match · Recommendation Reason | INSIGHT | **FORMAT TBD** | Insight | Fit Score와 Lead Score 혼용, 기업 DB를 Salesforce Object로 표현 |
| 13 | S5 · PIPELINE | "Sponsor 후보를 어떻게 실제 Deal로 발전시킬까?" | Tableau Next · Lead Score · Account AI Enrichment | ACTION | **PPT + 5s VIDEO** | Action | Tableau 수치를 검증된 것처럼, Fit=계약가능성 |
| 14 | S6 · UNDERSTAND | "고객은 무엇을 말했는가?" | Activity Intelligence | INSIGHT | **DEMO VIDEO** | Insight | 실시간 성공 보장 (백업 영상 필수) |
| 15 | S7 · REASON | "그래서 무엇을 제안할까?" | Opportunity Agent | ACTION | **LIVE** | Action | Agent가 임의로 쓰기 작업 수행하는 것처럼 표현 |
| 16 | S8 · ACT | "고객의 변화에 어떻게 대응할까?" | Proactive AI · Negotiation Assistant | ACTION | **PPT** | Action | 통일 전 스폰서십 금액, AI가 조건을 단독 결정하는 것처럼 |
| 17 | S9 · EXPAND | "1년 후, d'Alba와의 관계를 어떻게 다음 매출로?" | Partnership Plan · Upsell (논의 필요) | BUSINESS VALUE | **FORMAT TBD** | Business Value | 장기 재계약 자동화를 구현된 것처럼, 지난 시즌 성과를 실측처럼 |

### CHAPTER III — SO WHAT (18–19)

| # | 제목 | 한 줄 메시지 | 관점 | 표현 | 절대 넣지 않는 것 |
|---|---|---|---|---|---|
| 18 | What We Learned | 설계 판단 4가지 + **"We came here to learn Salesforce. We leave knowing how to build with it."** | LEARNED | — | 미측정 KPI·ROI, 구현 수치·Object 목록, Future를 현재처럼, 긴 문단 |
| 19 | From Learning to Building | **"We didn't start with Salesforce features. / We started with the business."** (typography bridge — PPT의 마지막 장) | LEARNED | — | Business→Domain→Entity / Architecture diagram, Object 목록, 기술 스택, KPI, 팀 소개, 긴 설명, Winner·Quiz·Q&A 내용, 별도 당첨자 슬라이드 |

---

## 3. 공식 평가 아젠다 매핑

> 평가 프레임워크지, "한 항목 = 한 슬라이드"가 아니다. 지능적으로 압축한다.

| 공식 아젠다 | 어느 슬라이드에서 드러나는가 |
|---|---|
| 1. Project Overview | 01 Cover · 04 Our Approach |
| 2. Team & Roles | 05 하단 팀 스트립 (풀 프로필 슬라이드 없음) |
| 3. Execution Process / Method | 05 How We Built It (Business First 순서 = 방법론) |
| 4. AS-IS Problems & Requirements | 02 Business Question · 03 What We Saw |
| 5. TO-BE Design | 04 Our Approach · (Demo 전반에서 구체화) |
| 6. Implementation Results & Demo | 06–17 (본체) |
| 7. Results & Conclusion | 18 What We Learned · 19 From Learning to Building |
| 8. Self Evaluation | **발표에 포함하지 않음** |

---

## 4. 품질 체크리스트 (사용자 브리프 §14)

- [ ] 표지가 `FROM FAN DATA TO REVENUE.` 라고 말한다 → 01
- [ ] 마무리(18)가 `We came here to learn Salesforce. / We leave knowing how to build with it.` 라고 말한다 → 18
- [ ] 19가 `We didn't start with Salesforce features. / We started with the business.` 두 문장만으로 최소화되어 있다 → 19
- [ ] 당첨자 발표용 슬라이드(Winner/Quiz Result/Thank You/Q&A)가 없다 → §1
- [ ] 공식 평가 아젠다가 커버되지만, 기계적으로 한 슬라이드씩 만들지 않았다 → §3
- [ ] Demo 슬라이드 06–17이 정확히 순서대로 남아 있다 → §2
- [ ] B2C → Fan Insight → B2B 전환이 명확하다 → 10 (색·톤 전환)
- [ ] 야구 구단의 재정 문제가 초반에 나온다 → 02
- [ ] 청중이 왜 이 스토리를 택했는지 이해한다 → 02·03·04
- [ ] 청중이 무엇을 만들었는지가 아니라 어떻게 사고했는지를 본다 → 04·05·18·19, Demo 발표자 멘트
- [ ] Salesforce 아키텍처 판단이 보이되 과부하되지 않는다 → 18 (4개 카드)
- [ ] 본문 텍스트가 매우 적다 → 03_wireframe.md 문구 규칙
- [ ] 기능 카탈로그가 아니다 → 모든 콘텐츠 슬라이드가 NOTICED/DECIDED/LEARNED에 답
- [ ] 근거 없는 주장이 없다 → 01_story.md §7 가드레일
- [ ] Future Scope가 구현 기능과 명확히 구분된다 → 17 (S9), 01_story.md §7.4
- [ ] "solution judgment를 갖춘, 준비된 Salesforce 신입"으로 느껴진다 (숙제 검사 아님)

---

## 5. 아직 팀 확정이 필요한 항목

1. **S4 (12번)** — `Demo순서.png`에 S4 열이 없음. Partner Matching을 별도 페이지로 둘지 + 표현 방식 확정.
2. **S9 (17번)** — 표현 방식 · AI 역할 · 기능 모두 "미정". 재계약·Upsell 자동화 구현 근거 확정 후 내용 채움.
3. **스폰서십 금액** — S8(16번) 등. `SPN-LED-BRANDDAY` 3억/5.5억 상충 → Product2/Quote/PPT/대사 일원화.
4. **이매니저 이름·프로필** — `00_STORY.md §4`에서 가칭·TBD.
5. **Tableau Next 수치** — 집계 기준·화면 값 일치 검증 완료 후에만 S5에서 수치 노출.
6. **AccountPlan 표준 Object** — 08-31 생성, 문서에 없음. Partnership Plan(S9)에서 어디까지 시연할지 팀 확인.
