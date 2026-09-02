# PPT_v2 · 03_WIREFRAME — 슬라이드별 상세 스펙 (19장)

> Mid-fidelity 와이어프레임 스펙. **최종 비주얼 디자인이 아니다** — 디자인 담당자는 각 슬라이드의
> 구조(제목 · 지배 메시지 · 온-슬라이드 문구 · 비주얼 구성 · 미디어/다이어그램/LIVE 영역)를 기준으로
> 최종 Visual Design을 만든다.
>
> **재생성:** `python3 _build.py` → HTML → `./_shoot.sh` (headless Chrome) → `NN_*.png` 19장.
> 문구 = `_build.py`, 스타일 = `wf.css`.
>
> **규격:** 16:9 · 1920×1080 · 한글 폰트 Pretendard · 페이지 표기 `NN / 19`.
> **팔레트 (최종 비주얼 디자인 기준):** Navy `#07111F` · Orange `#FC4E00` · Off-white `#F6F3F1` · Gray `#D9D9D9`.
> 느낌: Salesforce executive briefing + modern product storytelling + Cloud Alpacas brand.
> NOT: 학생 프로젝트 발표 / 기능 카탈로그 / 컨설팅 템플릿 / 마스코트 남발 / 장식용 UI.
> (이 폴더의 PNG는 mid-fidelity 와이어프레임 kit이라 중립 팔레트를 쓴다 — 최종 색은 위 브랜드 팔레트.)
>
> **공통 규칙:** Headline 1 · Supporting 1 · 핵심 요소 3~5개. 긴 문단·표 남발·문서 복붙 금지.
> 각 콘텐츠 슬라이드는 `WE NOTICED` / `WE DECIDED` / `WE LEARNED` 중 하나에 답한다.

---

# CHAPTER I — WHY (01–05)

## 01 · Cover

- **한 줄 메시지:** `FROM FAN DATA TO REVENUE.`
- **온-슬라이드 문구 (전부):**
  - (대형) `FROM FAN DATA TO REVENUE.`
  - (하단 1줄) `Cellsforce · Cloud Alpacas Fan Relationship Management Team`
- **비주얼 구성:** 타이포 중심. 워드마크/로고 1개 + 대형 타이틀 1문장 + 팀 1줄. 배경 장식 최소.
  마스코트 없음. 차트 없음.
- **미디어 영역:** 없음.
- **발표자 멘트:** "저희는 Salesforce를 배우러 왔습니다. 오늘 보여드릴 것은 — 팬 데이터에서 매출까지입니다."
- **다음 슬라이드로 전환:** "그런데 시작은 질문 하나였습니다." → 02
- **넣지 않는 것:** 부제 설명 문단, 이미지, 차트, 마스코트, 날짜를 제외한 메타데이터.

## 02 · Business Question — `WE NOTICED`

- **한 줄 메시지:** 팬은 늘어나는데, 왜 구단의 매출은 함께 성장하지 않을까?
- **온-슬라이드 문구:**
  - (H1) `"한국에서 가장 인기 있는 스포츠 중 하나인 야구. 그런데 왜 구단은 적자인가?"`
  - (Key Msg) `팬이 는다고 구단의 지속 가능성이 따라오지 않는다.`
- **비주얼 구성:** 엇갈리는 두 흐름 — `팬 수 ↑ (우상향)` vs `구단 매출 ↔ / ↓ (정체·적자)`. 숫자 대신 방향.
- **미디어 영역:** 개념 그래프 2개 (플레이스홀더). **실측/가짜 수치 금지** — 곡선의 방향만.
- **발표자 멘트:** "야구는 인기 스포츠입니다. 그런데 팬이 느는 중에도 구단은 적자일 수 있습니다.
  저희는 여기서 멈춰서 물었습니다 — 팬이 구단의 가장 큰 자산이라면, 왜 그 데이터가 사업 가치가 되지 못하는가?"
- **다음 슬라이드로 전환:** "그 이유를 저희는 세 군데에서 봤습니다." → 03
- **넣지 않는 것:** 시장 규모 통계, KBO 관중 수치, 구단 재무제표 숫자.

## 03 · What We Saw — `WE NOTICED`

- **한 줄 메시지:** 도입 전 Cloud Alpacas의 3가지 문제.
- **온-슬라이드 문구 (카드 3개):**
  1. `DATA IS FRAGMENTED` — 팬 데이터가 흩어져 있다 / "팬은 안 보이고 데이터만 보인다"
     · 티켓·굿즈·멤버십·앱·문의가 서로 다른 시스템에.
  2. `DATA DOESN'T BECOME ACTION` — 데이터는 많지만 액션이 없다 / 이해해도 다음 행동으로 안 이어진다
     · 세분화·타이밍·우선순위가 없어 결국 모두에게 같은 메시지.
  3. `FAN VALUE DOESN'T REACH B2B` — 팬덤의 가치가 기업의 기회로 닿지 않는다 / 어떤 기업이 우리 팬덤과 맞는지 판단할 근거가 없다
     · 팬의 특성을 알아도 파트너 발굴·Fit 검증·영업 전환 체계가 없다.
- **비주얼 구성:** 카드 3개. hierarchy = 큰 영문 라벨 / 짧은 국문 Headline / 한 줄 Sub / 1줄 설명.
  좌측에 "흩어진 팬 접점 → 막다른 길" 개념 아이콘 그룹(선택).
- **미디어 영역:** 아이콘/다이어그램 (퍼즐 조각 흩어짐 · 확성기 · 끊긴 다리).
- **발표자 멘트:** "데이터가 흩어져 있고, 흩어진 데이터는 액션이 되지 못하고, 팬덤의 가치는 B2B까지 닿지 못했습니다."
- **다음 슬라이드로 전환:** "그래서 저희는 이 셋을 하나의 흐름으로 연결하기로 했습니다." → 04
- **넣지 않는 것:** 4개째 pain, Salesforce 기능 언급, 해결책 미리보기.

## 04 · Our Approach — `WE DECIDED`

- **한 줄 메시지:** 데이터가 Insight에서 멈추지 않고 Action으로, 다시 Revenue로 연결된다.
- **온-슬라이드 문구:**
  - (H1) `DATA → INSIGHT → ACTION → REVENUE`
  - (Supporting) `팬에서 출발한다. 고객을 이해한다. 인사이트를 액션에 연결한다. 그 액션을 매출로 확장한다.`
  - (커넥터 캡션) `Fan Experience → Fan 360 → Fan Insight → Sponsorship Sales`
- **비주얼 구성:** 중앙에 하나의 연결된 Customer 360 여정.
  상단 레일: `Fan Activity → Fan 360 → Fan Insight`(파랑) `→ Partner Matching → Sponsorship Sales`(초록).
  하단 레일: `DATA → INSIGHT → ACTION → REVENUE`.
  단계 사이 커넥터 = Salesforce / Flow / Agentforce / Slack.
- **미디어 영역:** 다이어그램 1개가 슬라이드의 핵심 비주얼. 상세 아키텍처 아님.
- **발표자 멘트:** "저희의 가설은 단순합니다. 팬 데이터를 Customer 360으로 모으고, 인사이트로 바꾸고,
  그 인사이트가 액션이 되고, 그 액션이 매출이 된다. B2C와 B2B는 별개 프로젝트가 아니라 하나의 흐름입니다."
- **다음 슬라이드로 전환:** "그리고 이걸 만들 때, 저희는 기능부터 시작하지 않았습니다." → 05
- **넣지 않는 것:** Object 목록, 빌드 수치, 5레이어 아키텍처 상세.

## 05 · How We Built It — `WE DECIDED`

- **한 줄 메시지:** 우리는 기능부터 시작하지 않았다.
- **온-슬라이드 문구:**
  - (H1) `우리는 기능부터 시작하지 않았다`
  - (세로 흐름) `Business Problem → Customer / Data Model → Salesforce Standard → Flow / Apex / LWC → Agentforce → Business Action`
  - (하단 팀 스트립) `Cellsforce` · Sara(Fan 360 / Insight) · 혜준(Lead) · 아론(Account·Contact) · 은영(Opportunity) · 승우(Product·Quote·Campaign)
- **비주얼 구성:** 중앙 세로(또는 계단형) 흐름 다이어그램. 하단에 얇은 팀 스트립 1줄(칩).
  B2C=파랑 / B2B=초록 색 구분이 여기서 시작됨을 암시.
- **미디어 영역:** 다이어그램. 풀 팀 프로필 카드 금지.
- **발표자 멘트:** "저희 방법은 Business → Problem → Persona → Story → Domain → Workflow → Salesforce → Demo 순서입니다.
  Object를 먼저 만들거나 Flow부터 짜지 않았습니다. 30개 넘는 설계 결정을 ADR로 기록했고, 5명이 각자
  자기 구간을 요구사항부터 QA까지 책임졌습니다."
- **다음 슬라이드로 전환:** "이제 이 사고가 실제로 어떻게 작동하는지, Demo로 보여드리겠습니다." → 06
- **넣지 않는 것:** 개인별 사진·이력, Flow 40개·Apex 100개 같은 수치 자랑, 자동차 비유.

---

# CHAPTER II — DEMO SCENARIO (06–17) · LOCKED

> 06–17의 순서 · 주인공 · 핵심 질문 · 핵심 기능 · 표현 방식은 변경 금지.
> 각 Demo 슬라이드 = **하나의 큰 질문 → 하나의 화면/결과 → 키워드 3~5개.** 설명은 발표자가 말한다.

## 06 · Demo Map

- **한 줄 메시지:** 앞으로 보게 될 Demo의 전체 지도 — 10초 안에 이해.
- **온-슬라이드 문구:**
  - (H1) `From Fan Action to Sponsorship Revenue`
  - (Map) `Fan → Fan 360 → Fan Insight → Partner Matching → Lead → Opportunity → AI Sales → Closed Won`
- **비주얼 구성:** 가로 대형 8노드 맵. `Fan Insight`에서 파랑(B2C, 앞 3개) → 초록(B2B, 뒤 5개) 전환.
- **미디어 영역:** 다이어그램만. 스크린샷 없음.
- **발표자 멘트:** "Demo는 관객의 팬 참여에서 시작해 스폰서 계약까지 갑니다. 가운데 Fan Insight가
  B2C의 마지막이자 B2B의 출발점입니다."
- **다음 슬라이드로 전환:** "먼저, 팬 참여가 지금 실제로 일어나고 있습니다." → 07
- **넣지 않는 것:** 8단계 초과, "Business Opportunity"라는 표현 (→ `Partner Matching`).

## 07 · Live Event — Game Day (Fan Activity) · **LIVE**

- **한 줄 메시지:** 지금 경기장에서 실제로 팬 참여가 발생 중.
- **온-슬라이드 문구:**
  - `CLOUD ALPACAS · GAME DAY LIVE`
  - `⚾ 7회말 경기 진행 중`
  - `🎁 FAN EVENT OPEN — "문태양 선수 퀴즈에 참여하세요"`
  - `[ QR CODE ]`
- **비주얼 구성:** 다크 전광판 목업 + 실물 QR. 하단 얇은 띠:
  `관객 QR 참여 → Quiz Entry (FanQuiz Site) → Fan Activity → Salesforce → Fan 360`.
- **미디어 영역:** LIVE — FanQuiz Experience Site (`liveFanQuizEntry` LWC). 발표자가 관객에게 직접 참여 유도.
- **발표자 멘트:** "지금 여러분은 Cloud Alpacas 경기장의 관객입니다. 전광판에 이벤트가 떴습니다.
  QR을 찍고 참여해 주세요. — 이건 기능 소개가 아니라, 지금 실제로 팬 데이터가 만들어지는 중이라는 뜻입니다."
- **데이터 변화:** Campaign 연동이 **검증된 경우에만** Campaign Member / 응답 데이터 생성을 설명한다.
- **다음 슬라이드로 전환:** "이 참여가 CRM에 들어오면, 김매니저는 팬을 이렇게 봅니다." → 08
- **넣지 않는 것:** 기능 설명 문단, Campaign 연동을 검증 전 단정, 당첨자 추첨을 여기서 진행(마무리에서).

## 08 · S1 · FAN — "우리 팬은 누구인가?" · **PPT**

- **주인공:** 김매니저 (FRM Manager) · **PIV:** Insight
- **핵심 기능:** Fan 360 · Segment · Recommendation Hub
- **온-슬라이드 문구:**
  - (H1) `우리 팬은 누구인가?`
  - (칩) `Fan 360` `Segment` `Recommendation Hub`
  - (AI 역할) `팬 이해 지원` · (Value) `Fan Understanding`
- **비주얼 구성:** 실제 Fan 360 화면 캡처가 슬라이드의 55~70%. 우측에 칩 + AI 역할 + Value + PIV 레일.
- **미디어 영역:** PPT — Fan Profile / Fan 360 Dashboard (LWC). Segment · Engagement Score · Fan Value Tier ·
  구매 · 관람 · Timeline. (`04_DEMO.md` Scene 2 앞부분)
- **발표자 멘트:** "팬 데이터가 분산돼 개별 팬을 입체적으로 이해하기 어려웠습니다. 저희는 Person Account를
  Fan 360의 중심에 놓고, 팬을 3개 축 — 생애주기 · Engagement · Fan Value — 로 봅니다. 한 화면에서 팬이 보입니다."
- **다음 슬라이드로 전환:** "팬이 보이면, 다음은 팬마다 다르게 행동하는 것입니다." → 09
- **넣지 않는 것:** 필드 목록 전체 나열, 3축 정의 강의, 미측정 수치.

## 09 · S2 · ACTIVATE — "각 팬에게 어떻게 다르게 행동할까?" · **DEMO VIDEO**

- **주인공:** 김매니저 · **PIV:** Action
- **핵심 기능:** AI Personalized Message
- **온-슬라이드 문구:**
  - (H1) `각 팬에게 어떻게 다르게 행동할까?`
  - (칩) `AI Personalized Message`
  - (AI 역할) `Personalize` · (Value) `Personalized Fan Engagement`
- **비주얼 구성:** 다크 영상 재생 영역이 화면의 중심 (▶ + 스크러버). 우측 정보 컬럼.
- **미디어 영역:** DEMO VIDEO 80~90초 — Recommendation Hub 진입 → 우선 대응 Segment 확인 → 대표 팬 이루키 →
  Fan 360에서 방문·구매·선호 선수 확인 → AI 개인화 메시지 생성 → 김매니저 확인 → 발송 →
  Fan Insight에서 20·30대 여성 팬층 확인. (`04_DEMO.md` Scene 2 데모 영상 ①)
- **발표자 멘트:** "팬별 특성을 반영한 메시지를 담당자가 일일이 쓰기 어려웠습니다. AI가 초안을 만들고,
  담당자가 검토·승인 후 발송합니다. 생성 결과는 `Recommendations__c` 레코드로 남습니다 — Human-in-the-loop입니다."
- **다음 슬라이드로 전환:** "그리고 영상 마지막에, 김매니저는 개별 팬을 넘어 팬층의 변화를 봤습니다." → 10
- **넣지 않는 것:** 미측정 반응률·전환율 수치, AI가 자동 발송하는 것처럼 표현.

## 10 · Fan Insight — B2C → B2B Bridge ⭐ · **TRANSITION**

- **한 줄 메시지:** B2C에서 쌓인 팬 데이터가, 여기서 기업의 기회가 된다.
- **온-슬라이드 문구:**
  - (H1) `B2C에서 쌓인 팬 데이터가, 여기서 기업의 기회가 된다`
  - (Key Msg) `Fan Insight는 B2B가 아니라 B2C의 마지막 단계 — 두 세계를 잇는 Bridge.`
  - (좌) `B2C (여기까지)` : Fan Experience · Fan 360 · Recommendation / Personalization
  - (중앙 대형) `FAN INSIGHT`
  - (우) `B2B (여기부터)` : Partner Matching · Sponsorship Sales
- **비주얼 구성:** 좌/우 2분할 + 중앙 대형 배지. 좌측 파랑, 우측 초록. **이 슬라이드에서 색·톤이 전환된다.**
  Demo 전체에서 시각적으로 가장 강하게.
- **미디어 영역:** 개념 다이어그램만 (`FAN DATA ↓ FAN INSIGHT ↓ PARTNER OPPORTUNITY`). 스크린샷 없음.
  Fan Insight = Report / Dashboard 기반이라는 점 명시.
- **발표자 멘트:** (톤 전환) "여기까지가 B2C입니다. 이 팬 인사이트가 — 20·30대 여성 팬의 성장, 뷰티 관심 —
  이제 B2B 영업의 출발점이 됩니다. 팬 데이터가 있으니 광고주를 찾는 게 아니라, 팬 데이터가 팬덤의
  관심사를 보여주고, 그 관심사가 기업 매칭의 근거가 됩니다."
- **다음 슬라이드로 전환:** "이 인사이트가 어떻게 B2B 담당자에게 전달되는지 보시죠." → 11
- **넣지 않는 것:** 스크린샷, B2B 상세 설명, 기능 목록.

## 11 · S3 · CONNECT — "팬 데이터를 어떻게 B2B 영업 기회로 연결할까?" · **LIVE**

- **주인공:** 김매니저 → 이매니저 · **PIV:** Insight
- **핵심 기능:** Monthly Fan Insight Letter · Slack Agent
- **온-슬라이드 문구:**
  - (H1) `팬 데이터를 어떻게 B2B 영업 기회로 연결할까?`
  - (칩) `Monthly Fan Insight Letter` `Slack Agent`
  - (AI 역할) `Analyze & Discover` · (Value) `B2C Data → B2B Sales Opportunity`
- **비주얼 구성:** 붉은 톤 LIVE 프레임 + `● LIVE` 배지. Salesforce Fan Insight Letter → Slack 채널 전환 화면.
- **미디어 영역:** LIVE — Fan Insight Letter 확인 → 이매니저가 Slack Agent에게 분석 요청 →
  20·30대 여성 팬 증가 등을 근거로 Sponsorship 방향 탐색. (`04_DEMO.md` Scene 3) **백업 영상 준비.**
- **발표자 멘트:** "B2C에서 발견한 인사이트는 보고서로 끝나지 않습니다. 이매니저의 Slack으로 전달되어
  실제 B2B 영업을 시작합니다. B2C팀과 B2B팀이 별도로 움직이던 구조가 하나의 Revenue Process로 연결됩니다."
- **실패 대응:** 10초 안에 메시지가 도착하지 않으면 동일 시나리오 백업 영상 재생.
- **다음 슬라이드로 전환:** "그럼 이 팬덤에 가장 잘 맞는 기업은 누구일까요?" → 12
- **넣지 않는 것:** Slack 채널 ID 화면 노출, 실패 대응 미준비.

## 12 · S4 · Partner Matching — "이 팬덤과 가장 잘 맞는 기업은? 왜 이 기업인가?" · **FORMAT TBD**

- **주인공:** 이매니저 · **PIV:** Insight
- **핵심 기능:** Fan Fit · Segment Match · Recommendation Reason
- **온-슬라이드 문구:**
  - (H1) `이 팬덤과 가장 잘 맞는 기업은 누구인가? — 왜 이 기업인가?`
  - (칩) `Fan Fit` `Segment Match` `Recommendation Reason`
  - (박스) `[ FORMAT TBD — 표현 방식 미정, 팀 확정 필요 ]`
- **비주얼 구성:** 노란 FORMAT TBD 박스. 팬층 특성 ↔ 기업 후보 매칭 → Fit 근거 → `d'Alba`.
- **미디어 영역:** FORMAT TBD. 기업 데이터 = **OpenDART API 조회** (기업 DB는 Salesforce Object가 아님,
  `05_DECISIONS.md` D-020). Agentforce Matching → Top 후보 + Recommendation Reason. (`00_STORY.md §8` / `04_DEMO.md` Scene 4)
  ※ `Demo순서.png`에 S4 열이 없음(S3→S5) — 포함 여부·표현 방식 팀 확정 필요.
- **발표자 멘트:** "d'Alba는 먼저 Cloud Alpacas 팬덤과 높은 적합도를 보여 후보가 됐습니다. AI는 정답을
  주는 게 아니라 — 왜 이 기업인지를 설명합니다. 그리고 이 Fit이 높다고 곧바로 계약 가능성이 높은 건 아닙니다."
- **반드시 구분:** `Fan Fit / Segment Match` (팬덤-기업 적합도, Agentforce 산출) ≠ `Lead Score` (실제 계약 가능성, 영업 활동 기반).
- **다음 슬라이드로 전환:** "그럼 이 후보를 어떻게 실제 Deal로 발전시킬까요?" → 13
- **넣지 않는 것:** Fit Score와 Lead Score 혼용, 100개 기업 DB를 Salesforce Object로 표현, 임의 표현 방식 선택.

## 13 · S5 · PIPELINE — "Sponsor 후보를 어떻게 실제 Deal로 발전시킬까?" · **PPT + 약 5초 임베드 영상**

- **주인공:** 이매니저 / d'Alba · **PIV:** Action
- **핵심 기능:** Tableau Next · Lead Score · Account AI Enrichment
- **온-슬라이드 문구:**
  - (H1) `Sponsor 후보를 어떻게 실제 Deal로 발전시킬까?`
  - (칩) `Tableau Next` `Lead Score` `Account AI Enrichment`
  - (AI 역할) `Analyze / Score / Enrich` · (Value) `Sales Prioritization / Productivity / Data Quality`
  - (흐름) `Tableau Next Dashboard → Lead / Lead Score → Account → AI 필드 자동 보완 → d'Alba Opportunity`
- **비주얼 구성:** PPT 와이어프레임 + 우하단 `▶ 5s embedded video` 인셋.
- **미디어 영역:** PPT + 약 5초 임베드 영상 — PRM / Tableau Next Dashboard → Lead 목록에서 d'Alba →
  Lead Score와 근거 → Lead Convert → Account·Contact 생성 → AI가 Account 빈 필드 보완(DART) → Opportunity 생성.
  (`04_DEMO.md` Scene 4) **Tableau 수치는 검증 완료 전까지 노출하지 않는다.**
- **발표자 멘트:** "유망 Sponsor 판단부터 Account 정보 보완까지 수작업이 많았습니다. 우선순위는 Lead Score로,
  빈 정보는 AI가 공시 데이터(DART Open API)로 채웁니다. '분석은 Tableau, 실행은 Salesforce'로 역할을 나눴습니다."
- **다음 슬라이드로 전환:** "Opportunity가 열렸으니, 이제 고객이 무엇을 원하는지 들어야 합니다." → 14
- **넣지 않는 것:** Tableau 수치를 검증된 것처럼, Fit = 계약 가능성.

## 14 · S6 · UNDERSTAND — "고객은 무엇을 말했는가?" · **DEMO VIDEO**

- **주인공:** 이매니저 / 김하나 · **PIV:** Insight
- **핵심 기능:** Activity Intelligence
- **온-슬라이드 문구:**
  - (H1) `고객은 무엇을 말했는가?`
  - (칩) `Activity Intelligence`
  - (AI 역할) `Understand` · (Value) `Activity 자산화`
  - (흐름) `고객 Meeting / Activity → 기록 → AI 분석 → Summary / Signal`
- **비주얼 구성:** 다크 영상 재생 영역이 화면의 중심.
- **미디어 영역:** DEMO VIDEO 약 3분 (Zoom 대화 45~50초 고정) — Zoom 미팅 → Activity 자동 기록 →
  Prompt `CA_Offline_Meeting_*` → `Interaction_Intelligence__c` → `Interaction_Signal__c` (긍정/위험 Signal).
  (`04_DEMO.md` Scene 6) **백업 영상 필수.**
- **발표자 멘트:** "미팅이 끝나면 담당자가 내용을 직접 정리해야 했고, 고객의 요구와 위험 신호가 누락될 수
  있었습니다. 이제 고객이 말한 요구사항과 위험 신호가 Activity에 연결되고, 다음 행동의 근거가 됩니다."
- **다음 슬라이드로 전환:** "고객의 말을 이해했으니, 그래서 무엇을 제안할지가 다음입니다." → 15
- **넣지 않는 것:** 실시간 성공 보장 (백업 영상 없이), 대화 전체 스크립트를 슬라이드에.

## 15 · S7 · REASON — "그래서 무엇을 제안할까?" · **LIVE**

- **주인공:** 이매니저 / d'Alba · **PIV:** Action
- **핵심 기능:** Opportunity Agent
- **온-슬라이드 문구:**
  - (H1) `그래서 무엇을 제안할까?`
  - (칩) `Opportunity Agent`
  - (AI 역할) `Reason` · (Value) `Context 기반 Sales Decision Support`
  - (입력) `과거 유사 사례 + 현재 d'Alba OPP + 팬 데이터 + 고객 Activity`
- **비주얼 구성:** 붉은 톤 LIVE 프레임. Opportunity Record Page 내장 Agent 채팅.
- **미디어 영역:** LIVE — Opportunity Agent에 프롬프트 → 미팅 요구사항·Signal 요약 → 다음 Stage 확인 사항 →
  (승인 후) 후속 미팅 Event/Task 생성. 조회·추천은 즉시, 쓰기는 담당자 확인 후. (`04_DEMO.md` Scene 7)
  **백업 영상 준비.**
- **발표자 멘트:** "담당자가 과거 사례·현재 Deal·팬 데이터·고객 Activity를 직접 찾아 종합해야 했습니다.
  Agent가 컨텍스트를 모아 제안 방향을 근거와 함께 제시합니다. 다만 — 조회와 추천은 바로 하지만,
  고객 일정이나 계약 조건을 바꾸는 작업은 담당자 확인 없이는 실행하지 않습니다."
- **다음 슬라이드로 전환:** "제안이 오가면, 고객의 상황도 바뀝니다. 거기에 어떻게 대응할까요?" → 16
- **넣지 않는 것:** Agent가 임의로 쓰기 작업을 수행하는 것처럼 표현.

## 16 · S8 · ACT — "고객의 변화에 어떻게 대응할까?" · **PPT**

- **주인공:** 이매니저 / 김하나 · **PIV:** Action
- **핵심 기능:** Proactive AI · Negotiation Assistant
- **온-슬라이드 문구:**
  - (H1) `고객의 변화에 어떻게 대응할까?`
  - (칩) `Proactive AI` `Negotiation Assistant`
  - (AI 역할) `Act Proactively` · (Value) `Proactive Selling`
  - (흐름) `새 고객 Activity / 상황 → AI 선제 분석 → Negotiation 대응 / 수정안 + 판단 근거 → Closed Won`
- **비주얼 구성:** PPT 스크린샷 중심. Negotiation Context / Quote 비교 화면.
- **미디어 영역:** PPT — 고객 요구사항 확인 → 스폰서십 패키지 추천 → Product·Quote 연결 →
  고객 예산과 Quote 차이 확인 → Negotiation Assistant 협상안 → 담당자 승인 → Closed Won 전환. (`04_DEMO.md` Scene 8)
- **발표자 멘트:** "고객 반응이 바뀔 때마다 담당자가 다시 상황을 분석해야 했습니다. AI가 변화를 먼저 감지해
  수정안을 근거와 함께 제시합니다. AI가 임의로 조건을 바꾸는 게 아닙니다 — 기존 Quote, 고객 예산,
  할인 기준, 고객 Signal을 근거로 안을 제시하고, 최종 결정은 담당자가 합니다."
- **다음 슬라이드로 전환:** "계약은 끝이 아닙니다. 1년 뒤를 봅니다." → 17
- **넣지 않는 것:** 통일 전 스폰서십 금액 (`SPN-LED-BRANDDAY` 3억/5.5억 상충), AI가 조건을 단독 결정하는 것처럼.

## 17 · S9 · EXPAND — "1년 후, d'Alba와의 관계를 어떻게 다음 매출로?" · **FORMAT TBD**

- **주인공:** 이매니저 / d'Alba · **PIV:** Business Value
- **핵심 기능:** Partnership Plan · Upsell (논의 필요)
- **온-슬라이드 문구:**
  - (H1) `1년 후, d'Alba와의 관계를 어떻게 다음 매출로 연결할까?`
  - (칩) `Partnership Plan (논의 필요)` `Upsell (논의 필요)`
  - (박스) `[ FORMAT TBD — 표현 방식 · AI 역할 · 기능 모두 미정 ]`
  - (시간 전환) 화면에 크게 `1년 후`
- **비주얼 구성:** `1년 후` 대형 시간 전환 + Partnership Plan / Thank You Day Campaign.
  **구현 확인된 부분(실선) vs Future Scope(점선·흐리게·라벨)를 슬라이드에서 명확히 분리.**
- **미디어 영역:** FORMAT TBD. 구현 확인 범위에서만:
  - ✅ 구현 확인: Campaign Renewal RecordType · 갱신 캠페인 성과 요약 Flow · Thank You Day Campaign 개념
  - 🔵 Future Scope (점선): 장기 재계약 자동 판단 · Autonomous Upsell · 계약 후 성과 분석
  지난 시즌 성과는 **'발표용 시뮬레이션 데이터'로 명시.** (`04_DEMO.md` Scene 9 검증 조건)
- **발표자 멘트:** "첫 계약은 매출 엔진의 끝이 아니라 시작입니다. 계약과 활동 데이터가 쌓일수록 다음
  재계약과 업셀도 다시 감이 아니라 데이터에서 출발합니다. — 다만 여기부터는 저희가 구현한 부분과
  앞으로의 방향을 구분해서 말씀드리겠습니다."
- **다음 슬라이드로 전환:** "이 전체를 만들면서, 저희가 무엇을 배웠는지 정리하겠습니다." → 18
- **넣지 않는 것:** 장기 재계약 자동화를 구현된 것처럼, 지난 시즌 성과를 실측처럼, 임의 표현 방식 선택.

---

# CHAPTER III — SO WHAT (18–19)

> 발표 흐름: DEMO → **18 WHAT WE LEARNED** → **19 FROM LEARNING TO BUILDING** → (PPT 종료)
> → Salesforce Org LIVE → 퀴즈 당첨자 발표(실제 Org 화면) → Q&A.
> **Winner / Quiz Result / Thank You / Q&A 슬라이드는 만들지 않는다.**

## 18 · What We Learned — `WE LEARNED`

- **한 줄 메시지:** "무엇을 만들었나"가 아니라 — Salesforce를 쓰면서 **어떤 설계 판단을 배웠나.**
- **온-슬라이드 문구:**
  - (상단 — 얇은 principle card 4개, 각 영문 Headline + 1줄)
    1. `STANDARD FIRST` — 업무 프로세스가 이미 존재하는 곳엔 Salesforce 표준을 쓴다.
    2. `AUTOMATE WHAT REPEATS` — 반복되는 비즈니스 로직은 Flow로 자동화한다.
    3. `CUSTOMIZE WHERE IT MATTERS` — 차별화된 경험·로직에만 Apex / LWC를 쓴다.
    4. `AI WITH HUMAN CONTROL` — Agentforce는 추천·분석, Salesforce가 실행, 사람이 결정.
  - (중앙 대형 문장 — Closing message)
    > We came here to learn Salesforce.
    > We leave knowing how to build with it.
  - (그 아래 한 줄, 아주 흐리게) `Fan Data → Customer 360 → Action → Revenue · CELLSFORCE × CLOUD ALPACAS`
- **비주얼 구성:** 상단 = 얇은 4-카드 밴드(설계 판단). 중앙 = 큰 Closing 타이포가 주인공. 하단 = 아주 얇은 identity 한 줄.
- **미디어 영역:** 없음 (타이포).
- **발표자 멘트:** "저희가 배운 건 네 가지입니다 — 표준을 먼저, 반복은 자동화, 차별화는 커스텀,
  AI는 사람의 통제 아래. Flow를 썼다가 아니라, 무엇이 자동으로 일어나야 하는지 물었고 반복 로직에 Flow를 택한 겁니다."
- **다음 슬라이드로 전환:** "그 판단의 출발점은 하나였습니다." → 19
- **넣지 않는 것:** 미측정 KPI·ROI, 구현 수치·Object 목록, Future를 현재처럼, 긴 문단, 자축 톤.

## 19 · From Learning to Building — `WE LEARNED` (typography bridge, PPT의 마지막 장)

- **한 줄 메시지:** 우리는 Salesforce 기능이 아니라 비즈니스에서 시작했다.
- **온-슬라이드 문구 (전부):**
  - (상단 작은 label) `FROM LEARNING TO BUILDING`
  - (중앙 초대형 두 문장)
    > We didn't start with Salesforce features.
    > We started with the business.
  - 그 외 아무것도 없다.
- **비주얼 구성:** editorial typography poster. 거의 빈 화면 + 초대형 타이포 + 넉넉한 여백.
  타이포의 크기·줄바꿈으로 메시지의 힘을 만든다. 장식보다 typography가 주인공.
- **미디어 영역:** 없음.
- **발표자 멘트:** (짧게) "저희는 Salesforce 기능에서 시작하지 않았습니다. 비즈니스에서 시작했습니다.
  — 이제 실제 Org를 보시겠습니다." → PPT 종료 → Salesforce Org LIVE.
- **다음 슬라이드로 전환:** (PPT 종료) PPT를 끄고 Salesforce Org LIVE로 전환 → 퀴즈 당첨자 발표(실제 Org 화면) → Q&A.
- **넣지 않는 것:** Business→Domain→Entity diagram, Architecture diagram, Object 목록, 기술 스택, KPI,
  팀 소개, 긴 설명, Winner / Quiz / Thank You / Q&A 내용, 별도 당첨자·Q&A 슬라이드.

---

## 부록 A. 파일 구조

```
docs/PPT_v2/
├── 01_story.md              내러티브 (왜 이 순서·이 톤)
├── 02_slide_inventory.md    19장 목록 + 아젠다 매핑 + 체크리스트
├── 03_wireframe.md          이 문서 — 슬라이드별 상세 스펙
├── _build.py                19개 HTML 생성 (문구의 Source of Truth)
├── wf.css                   와이어프레임 스타일 kit (mid-fidelity)
├── _shoot.sh                HTML → 1920×1080 PNG (headless Chrome)
└── NN_*.png                 19장 와이어프레임 (재생성물)
```

## 부록 B. 재생성

```bash
cd docs/PPT_v2
./_shoot.sh            # _build.py 실행 → HTML → PNG 19장
```

문구를 바꾸려면 `_build.py`를, 레이아웃/스타일을 바꾸려면 `wf.css`를 수정한다.
Demo 06–17의 순서·주인공·핵심 질문·표현 방식은 바꾸지 않는다.
