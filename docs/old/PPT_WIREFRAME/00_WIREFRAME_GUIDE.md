# Cloud Alpacas — 최종 발표 PPT Wireframe / Storyboard Guide

> 이 폴더의 PNG **21장**은 **레이아웃 시안(Mid-fidelity Wireframe)**이다. 최종 비주얼 디자인이 아니다.
> 디자인 담당자는 각 PNG의 구조(제목·핵심 메시지·이미지/영상/Live 영역·다이어그램·QR·페르소나 위치)를 기준으로 최종 Visual Design을 만든다.
> Demo(06–17)의 **순서·주인공·핵심 질문·핵심 기능·표현 방식**은 첨부 이미지 `Demo순서.png` + `04_DEMO.md` 를 Source of Truth로 한다.

- 규격: 16:9 · 1920×1080 PNG · 한글 폰트 Pretendard
- 재생성: `./_shoot.sh` (headless Chrome로 `_build.py` → HTML → PNG). 문구 = `_build.py`, 스타일 = `wf.css`.

---

## 0. 이번 개정에서 바뀐 것 (Change Log)

### 3차 개정 — 후반부(18–21) 재구성: DEMO 직후 바로 Closing되는 느낌 제거

DEMO(01–17)가 끝나자마자 결론처럼 끝나던 흐름을, 발표 후반부에 "무엇을 배웠고 / 어떻게 Salesforce를
바라보게 되었는가"를 한 번 더 보여준 뒤 자연스럽게 **LIVE Org 시연**으로 넘어가도록 바꿨다.

| 슬라이드 | 이전 (2차) | 현재 (3차) |
|---|---|---|
| **CH III** | GLOBAL BEST PRACTICES | **WHAT WE LEARNED** |
| **18** | Why This Architecture? (설계 원칙 3개) | **WHAT WE LEARNED** — 설계 판단 4개(STANDARD FIRST / AUTOMATE WHAT REPEATS / CUSTOMIZE WHERE IT MATTERS / AI WITH HUMAN CONTROL) + 중앙 큰 메시지 "We came here to learn Salesforce. We leave knowing how to build with it." |
| **19** | How It Works (Automation Working Flow) | **FROM LEARNING TO BUILDING** — 브리지 슬라이드. 거의 빈 화면 + 초대형 타이포. "We didn't start with Salesforce features. / We started with the business." 그게 전부. 다이어그램·카드·아이콘 금지 |
| **20** | What We Built → Business Value | **WHAT WE BUILT / BUSINESS VALUE** — FAN / INSIGHT / REVENUE 구조 유지 |
| **21** | Future → Closing | **FUTURE / CLOSING** — NOW/FUTURE + Closing 유지. PPT의 마지막 장 |
| 파일명 | `18_why_this_architecture` · `19_how_it_works` | `18_what_we_learned` · `19_from_learning_to_building` |

**발표 흐름:** DEMO → 18 WHAT WE LEARNED → 19 FROM LEARNING TO BUILDING → 20 WHAT WE BUILT / BUSINESS VALUE
→ 21 FUTURE / CLOSING → **PPT 종료 → Salesforce Org LIVE 전환 → 퀴즈 당첨자 발표(실제 Org 화면) → Q&A.**

**당첨자 발표는 PPT가 아니라 실제 Salesforce Org 화면에서 진행한다.** 따라서 당첨자 발표용 슬라이드,
QR 슬라이드, Winner / Quiz Result / Q&A / Thank You 슬라이드는 절대 추가하지 않는다. 페이지 수는 **21장 유지**.

감정선: `WHAT WE LEARNED → HOW WE THINK → WHAT WE BUILT → WHERE WE GO NEXT`.

### 2차 개정 — 25장 → **21장** 압축 (발표 흐름을 더 짧고 강하게)

| 변경 | 이전 | 현재 |
|---|---|---|
| **CH I · OVERVIEW** | 01–05 | 01–05 (유지) |
| **CH II · DEMO** | 06–17 | 06–17 (유지 — 순서·주인공·핵심 질문·표현 방식 그대로) |
| **CH III · BEST PRACTICES** | 18 Standard First / 19 Customer 360 / 20 AI+Human / 21 Automation (4장) | **18 Why This Architecture?** (설계 원칙 3개로 통합) / **19 How It Works** (Automation 중심 재구성) (2장) |
| **CH IV · CONCLUSION** | 22 What We Built / 23 Business Value / 24 Future Vision / 25 Closing (4장) | **20 What We Built → Business Value** (22+23 통합) / **21 Future → Closing** (24+25 통합, 발표 마지막) (2장) |
| 페이지 표기 | `NN / 25` | `NN / 21` |
| 당첨자 발표 | (PPT에 언급) | **PPT 페이지 없음** — 21 Closing 이후 발표자가 "오늘 참여해주신 분들 중…" 하며 LIVE 당첨자 발표 → Q&A |

> 18~25의 세부(Standard First 2패널·실측 수치·AI/Human 다이어그램·BIGS 카드 등)는 **삭제가 아니라 압축**했다. 핵심 메시지는 보존, 세부 기술 설명은 발표자 몫으로 이관.

### 1차 개정 (Demo순서.png 반영) — 아래는 유지됨

| 항목 | 내용 |
|---|---|
| **#03 Pain Point** | 3개 카드를 새 내용으로 전면 교체. hierarchy = 큰 번호 / 짧은 Headline / 한 줄 Sub-headline / 2~3줄 설명 |
| **#04 Our Approach** | Process Flow → **자동화된 연결 구조**. 중앙 대형 Automation Flow + `DATA → INSIGHT → ACTION → REVENUE` + 단계 사이 `Salesforce·Flow·Agentforce·Slack·Data` 커넥터. 핵심 문구 "데이터가 Insight에서 멈추지 않고 Action으로 연결된다 / Data does not stop at Insight. It moves to Action." |
| **#06 Demo Map** | `Business Opportunity` → **`Partner Matching`** (표현 통일). Fan → Fan 360 → Fan Insight → Partner Matching → Lead → Opportunity → AI Sales → Closed Won |
| **#10 Fan Insight** | B2B 안이 아니라 **B2C의 마지막 단계 / B2C→B2B Bridge**로 이동. 전용 Transition 페이지(시각적으로 가장 강하게). B2C ── FAN INSIGHT ── B2B |
| **Demo 06–17** | 12페이지를 `Demo순서.png` 기준으로 재구성. 각 페이지에 **표현 방식 배지**(PPT / DEMO VIDEO / LIVE / FORMAT TBD / TRANSITION)를 상단에 표기. 표현 방식에 따라 레이아웃이 달라짐(영상 페이지=재생 영역 중심, LIVE=현장 실행 화면, 미정=`[FORMAT TBD]`) |
| **파일명** | Demo 페이지를 `NN_sX_name.png`로 재명명 (아래 매핑표) |

### 파일명 매핑 (이전 → 현재)

| 이전 | 현재 | 비고 |
|---|---|---|
| 06_demo_map | 06_demo_map | 내용 수정 |
| 07_live_event | 07_live_event | Game Day / Fan Activity로 정리 |
| 08_fan_360 | **08_s1_fan** | S1 · FAN |
| 09_fan_insight | **09_s2_activate** | S2 · ACTIVATE |
| 10_recommendation | **10_fan_insight_bridge** | Fan Insight = B2C→B2B Bridge |
| 11_slack_transition | **11_s3_connect** | S3 · CONNECT |
| 12_business_opportunity | **12_s4_partner_matching** | S4 · Partner Matching (이미지에 S4 열 미표시 → 재구성, FORMAT TBD) |
| 13_ai_matching | **13_s5_pipeline** | S5 · PIPELINE |
| 14_lead_conversion | **14_s6_understand** | S6 · UNDERSTAND |
| 15_opportunity | **15_s7_reason** | S7 · REASON |
| 16_ai_sales | **16_s8_act** | S8 · ACT |
| 17_closed_won | **17_s9_expand** | S9 · EXPAND |

> ⚠️ `Demo순서.png`는 컬럼이 `S1 · S2 · S3 · S5 · S6 · S7 · S8 · S9` 로, **S4 열이 보이지 않는다(S3→S5)**. 사용자 지시(Partner Matching = 별도 단계)와 `00_STORY §8` / `04_DEMO Scene 4`를 근거로 **S4 = Partner Matching** 으로 재구성했고, 표현 방식은 잠정 **FORMAT TBD**로 표시했다. 이미지에 S4 상세가 있으면 12번 페이지를 그에 맞춰 교체한다.

---

## 1. 발표 전체 구조 (총 21장)

| Chapter | 슬라이드 | 액센트 | 역할 |
|---|---|---|---|
| **I. OVERVIEW** | 01–05 | Slate | 프로젝트 개요 · 팀 · AS-IS / Pain Point |
| **II. DEMO SCENARIO** ⭐ | 06–17 (12장) | Blue(B2C) → Green(B2B) | 하나의 Business Story. 기능 목록이 아님 |
| **III. WHAT WE LEARNED** | 18–19 (2장) | Teal | 무엇을 배웠는가 → 우리는 어떻게 사고했는가 (브리지) |
| **IV. CONCLUSION** | 20–21 (2장) | Navy | 무엇을 만들었고 어떤 가치가 생겼는가 → 미래 + Closing |

```
01 Cover · 02 Business Challenge · 03 Pain Point · 04 Our Approach · 05 Project Scope/Team
06 Demo Map · 07 Live Event · 08 S1 FAN · 09 S2 ACTIVATE · 10 Fan Insight Bridge · 11 S3 CONNECT
12 S4 Partner Matching · 13 S5 PIPELINE · 14 S6 UNDERSTAND · 15 S7 REASON · 16 S8 ACT · 17 S9 EXPAND
18 What We Learned · 19 From Learning to Building
20 What We Built / Business Value · 21 Future / Closing
→ (PPT 종료) → Salesforce Org LIVE → 퀴즈 당첨자 발표 → Q&A
```

### 관통 Story (모든 슬라이드가 이 흐름의 한 지점)

```
Fan → Fan Activity → Fan 360 → Personalized Action → Fan Insight(Bridge)
→ Partner Matching → Sponsorship Sales → Opportunity → AI Sales → Closed Won → Expansion
```

### 원칙

- 슬라이드 골격 = **Problem → Insight → Action → Business Value** (콘텐츠 슬라이드 하단 PIV 레일이 현재 단계 표시)
- Demo 페이지 = **하나의 큰 질문 → 화면 → 결과**. 설명은 발표자가 말하고, PPT는 보여준다.
- 텍스트: Headline 1 · Supporting 1 · 핵심 요소 3~5개. 긴 문단·표 남발·문서 복붙 금지.
- **B2C → B2B 전환점 = Slide 10 (Fan Insight Bridge)**. 여기서 색·커넥터·발표 톤이 파랑→초록으로 전환.

### 표현 방식 배지 (Demo 페이지 상단)

| 배지 | Wireframe 처리 |
|---|---|
| **PPT** | 일반 PPT 슬라이드 Wireframe (Screenshot 영역 중심) |
| **DEMO VIDEO** | 다크 영상 재생 영역 + ▶ + 스크러버가 화면의 중심 |
| **LIVE** | 붉은 톤 "실제 화면 · 현장 실행" 프레임 + `● LIVE` 배지 |
| **PPT + 5s VIDEO** | PPT Wireframe + `▶ 5s embedded video` 인셋 |
| **FORMAT TBD** | 노란 `[ FORMAT TBD — 표현 방식 미정 ]` 박스. PPT/Video/Live 임의 선택 금지 |
| **TRANSITION** | 전환 전용 페이지 (Demo 콘텐츠 아님). 배지는 중립 |

### Source of Truth / 금지사항

- **문서·이미지에 없는 기능을 만들지 않는다.** Future Scope를 현재 구현처럼 표현하지 않는다(21번에서만, 점선·흐리게·라벨).
- 미측정 KPI(반응률·전환율) 숫자 금지. 실측 가능한 것은 빌드 수치뿐(17 Custom Objects · 40 Active Flows · 1 Trigger · 46 LWC · 5 Agentforce Agents · 6 Prompt Templates — `05_ARCHITECTURE.md`).
- Sponsorship 금액은 발표 전 Product2/Quote/PPT/대사 하나로 통일. 통일 전 금액 언급 금지.
- 페르소나: FRM Manager = **김매니저**, 신규 팬 = **이루키**, Sponsorship Sales Manager = **이매니저**, d'Alba 담당자 = **김하나**.

---

## 2. 슬라이드별 정의

### CHAPTER I — OVERVIEW

| # | Slide | 목적 | 핵심 메시지 | 실제 보여줄 것 | 표현 방식 |
|---|---|---|---|---|---|
| 01 | Cover | 표지 | "외부 환경에 흔들리지 않는 지속 가능한 매출 엔진" | 로고/워드마크만. 이미지·차트 없음 | — |
| 02 | Business Challenge | 큰 질문으로 문제의식 (PIV: Problem) | "팬은 늘어나는데, 왜 구단의 매출은 함께 성장하지 않을까?" | 팬 수 ↑ / 구단 매출 ↔·↓ 두 그래프의 엇갈림 | — |
| 03 | Pain Point (AS-IS) | 도입 전 문제 3가지 | ① 팬 데이터가 흩어져 있다 ② 데이터는 많지만 ACTION이 없다 ③ 팬덤의 가치를 기업의 기회로 연결할 수 없다 | 카드 3개. 번호 / Headline / Sub-headline / 2~3줄 설명 | — |
| 04 | Our Approach | 자동화된 연결 구조 (PIV: Insight) | "데이터가 Insight에서 멈추지 않고 Action으로 연결된다" / "Data does not stop at Insight. It moves to Action." | 중앙 대형 Automation Flow (Fan Activity → … → Sponsorship Sales) + `DATA→INSIGHT→ACTION→REVENUE` + 단계 사이 Salesforce·Flow·Agentforce·Slack·Data 커넥터 | — |
| 05 | Project Scope / Team | B2C→Insight→B2B가 하나의 프로젝트 | "B2C에서 시작해 B2B로 이어지는 하나의 프로젝트" | Scope 다이어그램(가운데 Fan Insight가 연결점) + Feature Owner 1줄 | — |

### CHAPTER II — DEMO SCENARIO (06–17)

| # | Slide | 목적 / 핵심 질문 | 핵심 기능 (Demo순서) | 실제 보여줄 것 | 표현 방식 |
|---|---|---|---|---|---|
| 06 | Demo Map | Demo 전체 지도 (10초 이해) | — | Fan → Fan 360 → Fan Insight(Bridge) → **Partner Matching** → Lead → Opportunity → AI Sales → Closed Won | — |
| 07 | Live Event — Game Day | "지금 경기장에서 실제로 팬 참여가 발생 중" | QR 참여 이벤트 (FanQuiz Site) | 전광판 목업(CLOUD ALPACAS · GAME DAY LIVE · ⚾ 7회말 · 🎁 FAN EVENT OPEN · [QR CODE]) + 관객QR→Quiz Entry→Fan Activity→Salesforce→Fan 360 | **LIVE** (관객 참여 / `04_DEMO` Scene 1은 "PPT + 관객 참여") |
| 08 | S1 · FAN — "우리 팬은 누구인가?" | 김매니저 · B2C Fan Management (PIV: Insight) | Fan 360 · Segment · Recommendation Hub | Fan 360 → Segment → Recommendation Hub 핵심 화면 캡처 (`04_DEMO` Scene 2 앞부분) | **PPT** |
| 09 | S2 · ACTIVATE — "각 팬에게 어떻게 다르게 행동할까?" | 김매니저 · B2C Marketing (PIV: Action) | AI Personalized Message | Target Fan 확인 → AI 개인화 메시지 생성 → Review → 발송 (`04_DEMO` 데모 영상 ① 80~90초) | **DEMO VIDEO** |
| 10 | **Fan Insight — B2C → B2B Bridge ⭐** | B2C의 마지막 단계 / 두 세계의 연결점 (PIV: Insight) | — (전환 페이지) | B2C(Fan Experience·Fan 360·Recommendation) ── **FAN INSIGHT** ── B2B(Partner Matching·Sponsorship Sales). 색·톤이 여기서 전환 | **TRANSITION** |
| 11 | S3 · CONNECT — "팬 데이터를 어떻게 B2B 영업 기회로 연결할까?" | 김매니저 → 이매니저 · B2C→B2B Sponsorship (PIV: Insight) | Monthly Fan Insight Letter · Slack Agent | Fan Insight Letter 확인 → 이매니저가 Slack Agent에게 분석 요청 → 20·30대 여성 팬 증가 등을 근거로 Sponsorship 방향 탐색 (`04_DEMO` Scene 3) | **LIVE** |
| 12 | S4 · Partner Matching — "이 팬덤과 가장 잘 맞는 기업은? 왜 이 기업인가?" | 이매니저 (PIV: Insight) | Fan Fit · Segment Match · Recommendation Reason | 팬층 특성 ↔ 기업 후보 매칭 → Fit 근거 → d'Alba. 기업 데이터 = OpenDART API (`00_STORY §8` / `04_DEMO` Scene 4) | **FORMAT TBD** (이미지에 S4 열 미표시) |
| 13 | S5 · PIPELINE — "Sponsor 후보를 어떻게 실제 Deal로 발전시킬까?" | 이매니저 / d'Alba · Dashboard→Lead→Account→OPP (PIV: Action) | Tableau Next · Lead Score · Account AI Enrichment | Tableau Next Dashboard → Lead / Lead Score → Account → AI 필드 자동 보완 → d'Alba OPP 진입 (`04_DEMO` Scene 4) | **PPT + 약 5초 임베드 영상** |
| 14 | S6 · UNDERSTAND — "고객은 무엇을 말했는가?" | 이매니저 / 김하나 · OPP · Needs Analysis (PIV: Insight) | Activity Intelligence | 고객 Meeting/Activity → 기록 → AI 분석 → Summary / Signal (`04_DEMO` Scene 6) | **DEMO VIDEO** |
| 15 | S7 · REASON — "그래서 무엇을 제안할까?" | 이매니저 / d'Alba · OPP · Proposal (PIV: Action) | Opportunity Agent | 과거 유사 사례 + 현재 OPP + 팬 데이터 + 고객 Activity → Agent 분석 → 제안 방향 / Package / Product + 근거 (`04_DEMO` Scene 7) | **LIVE** |
| 16 | S8 · ACT — "고객의 변화에 어떻게 대응할까?" | 이매니저 / 김하나 · OPP · Negotiation (PIV: Action) | Proactive AI · Negotiation Assistant | 새 고객 Activity/상황 → AI 선제 분석 → Negotiation 대응/수정안 + 근거 (`04_DEMO` Scene 8, Closed Won으로 전환) | **PPT** |
| 17 | S9 · EXPAND — "1년 후, d'Alba와의 관계를 어떻게 다음 매출로?" | 이매니저 / d'Alba · Post-Sale · 1년 후 (PIV: Business Value) | Partnership Plan · Upsell (논의 필요) | "1년 후" → 단년 계약 종료 임박 → Partnership Plan 확인 → Upsell Sales 고려. 재계약/장기 Partnership은 Future Scope — 구현 확인된 부분만 (`04_DEMO` Scene 9 검증 조건) | **미정 (FORMAT TBD)** — AI 역할·기능 모두 미정 |

### CHAPTER III — WHAT WE LEARNED (18–19)

| # | Slide | 목적 | 핵심 메시지 | 실제 보여줄 것 (핵심 Visual) | 표현 방식 |
|---|---|---|---|---|---|
| 18 | **What We Learned** | "Salesforce를 썼다"가 아니라 **Salesforce를 통해 어떤 설계 판단을 배웠는가** | **We came here to learn Salesforce. We leave knowing how to build with it.** | 상단: 얇은 principle card 4개 — ① STANDARD FIRST ② AUTOMATE WHAT REPEATS ③ CUSTOMIZE WHERE IT MATTERS ④ AI WITH HUMAN CONTROL (각 Headline + 1줄). 중앙: 큰 타이포 메시지. 하단: 아주 얇은 flow `Fan Data → Customer 360 → Action → Revenue` (복잡해지면 생략). 긴 설명·구현 수치·Object 목록·KPI·문단 금지 | — |
| 19 | **From Learning to Building** | DEMO → 결론 사이의 **호흡을 만드는 브리지 슬라이드** (정보 전달용 아님) | **We didn't start with Salesforce features. / We started with the business.** | 거의 빈 화면 + 초대형 타이포. 상단 작은 label `FROM LEARNING TO BUILDING` + 중앙 두 문장이 전부. **Business→Domain→Entity diagram / 4개 카드 / Architecture diagram / Object 목록 / 기술 스택 / KPI / 긴 설명 / 발표자 멘트 절대 금지.** 타이포의 크기·줄바꿈으로 메시지의 힘을 만든다 | — |

### CHAPTER IV — CONCLUSION (20–21)

| # | Slide | 목적 | 핵심 메시지 | 실제 보여줄 것 (핵심 Visual) | 표현 방식 |
|---|---|---|---|---|---|
| 20 | **What We Built / Business Value** | 만든 것 + 가치를 하나의 흐름으로 (구조 유지) | **FAN → INSIGHT → REVENUE** | 대형 카드 3개. 각 카드 = 키워드 / 1줄 / 구현요소(FAN: Fan 360·Personalization / INSIGHT: Fan Insight·Partner Matching / REVENUE: Sponsorship Sales·Opportunity) / Business Value(Fan Lifetime Value ↑ · Personalized Fan Experience ↑ · Sponsorship Revenue ↑). 미측정 KPI·ROI, 가상 성과 수치 금지 | — |
| 21 | **Future / Closing** (PPT의 마지막 장) | 현재→미래 + Closing (구조 유지) | "팬을 이해하고, 팬덤의 가치를 발견하고, 그 가치를 매출로 연결합니다." + CLOUD ALPACAS · Sustainable Revenue Engine | 상단: NOW(Fan Data→Insight→Partner Matching→Sponsorship) / FUTURE SCOPE(Real-time Data→AI Decision→Autonomous Action→Continuous Revenue Growth, **점선·lighter·secondary hierarchy** — 현재 구현처럼 보이면 안 됨). 하단: 대형 Closing 문장 + 워드마크. **21장 이후 바로 PPT 종료 → Salesforce Org LIVE → 퀴즈 당첨자 발표(실제 Org 화면) → Q&A.** Winner/Quiz Result/Q&A/Thank You 슬라이드 만들지 않음 | — |

---

## 3. 최종 검수 — 3차 개정 (21장)

- [x] 총 **21장** (01–05 · 06–17 · 18–19 · 20–21), 페이지 표기 `NN / 21`
- [x] **01–17 무변경** — Demo 06–17의 순서·주인공·핵심 질문·핵심 기능·표현 방식(PPT/DEMO VIDEO/LIVE/FORMAT TBD/TRANSITION) 그대로. Demo를 설명용 텍스트 슬라이드로 바꾸지 않음
- [x] **18 What We Learned** — 설계 판단 4개(STANDARD FIRST / AUTOMATE WHAT REPEATS / CUSTOMIZE WHERE IT MATTERS / AI WITH HUMAN CONTROL) 얇은 카드 + 중앙 큰 메시지 "We came here to learn Salesforce. We leave knowing how to build with it." + 하단 얇은 flow. 구현 수치·Object 목록·KPI·문단 없음
- [x] **19 From Learning to Building** — 브리지 슬라이드. 거의 빈 화면 + 초대형 타이포. "We didn't start with Salesforce features. / We started with the business." 상단 작은 label + 중앙 두 문장이 전부. 다이어그램·카드·아이콘·Architecture·Object 목록·KPI·발표자 멘트 없음
- [x] **20 What We Built / Business Value** — FAN→INSIGHT→REVENUE 카드 3개(키워드/구현요소/Business Value). 미측정 KPI·ROI·가상 성과 수치 없음
- [x] **21 Future / Closing** — PPT의 마지막 장. NOW/FUTURE 분리(FUTURE 점선·lighter·secondary) + 대형 Closing 문장 + 워드마크. **21장 이후 PPT 종료 → Salesforce Org LIVE → 퀴즈 당첨자 발표 → Q&A.** Winner/Quiz Result/Q&A/Thank You 슬라이드 없음
- [x] 후반부는 **내용을 더 넣는 게 아니라 과감히 덜어내는** 방향. 각 슬라이드 = 발표자가 말할 핵심 하나
- [x] 디자인 시스템 유지 (16:9 / 1920×1080 / Pretendard / Chapter·PageNumber / Slate·Blue·Green·Teal·Navy / Mid-fidelity). 18–21은 "귀여운 알파카 발표자료"보다 "고급 Final Presentation" 느낌 우선. Cloud Alpacas 브랜드 컬러(#FC4E00 / #07111F / #F6F3F1 / #D9D9D9) 유지

### Story Flow 자체 검수

> 문제(02·03) → 해결 방법(04·05) → 실제 Demo로 증명(06–17) → **무엇을 배웠는가(18) → 우리는 어떻게 사고했는가(19, 브리지) → 무엇을 만들었고 어떤 가치가 생겼는지(20) → 미래 + Closing(21) → PPT OFF → Org LIVE → Winner → Q&A**

감정선: **WHAT WE LEARNED → HOW WE THINK → WHAT WE BUILT → WHERE WE GO NEXT**

**→ YES.** 01 표지 → 02 큰 질문 → 03 Pain 3개 → 04 자동화 해법 → 05 B2C·B2B 하나의 프로젝트 → 06 Demo 지도 → 07 Live로 팬 참여 발생 → 08–09 팬 이해·개인화 → 10 Fan Insight에서 B2C→B2B 전환 → 11–12 팬 데이터로 기업 발굴·매칭 → 13–17 Lead→OPP→협상→확장 → **18 무엇을 배웠나(설계 판단 4개) → 19 우리는 어떻게 사고했나("기능이 아니라 비즈니스에서 시작") → 20 FAN·INSIGHT·REVENUE 성과+가치 → 21 미래 + "팬을 이해하고, 팬덤의 가치를 발견하고, 매출로 연결합니다." → PPT 종료 후 Org LIVE 시연**

### 아직 팀 확정이 필요한 항목 (1차와 동일)

1. **S4 (12번)** — `Demo순서.png`에 S4 열 미표시. Partner Matching을 별도 페이지로 둘지 + 표현 방식 확정.
2. **S9 (17번)** — 표현 방식·AI 역할·기능 모두 "미정". 재계약·Upsell 자동화 구현 근거 확정 후 내용 채움.
3. **금액** — S8(16번) 등 Sponsorship 금액 일원화.
