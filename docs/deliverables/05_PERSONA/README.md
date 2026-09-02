# 05. 페르소나 프로파일링 — 최종 제출용

`../../00_STORY.md` 를 근거로 만든 **PPT/문서 삽입용 Persona Profile 이미지** 5종.

- 형식: SVG(벡터) + PNG(3840×2160, 16:9)
- 재생성: `python3 _generator.py`
- 원칙: 성격·업무·Pain·목표·행동은 `00_STORY.md`에 근거가 있는 내용만 사용. 문서에 없는 개인정보는 만들지 않음(김하나 이름·직책은 "예시"로 명시).

## 파일

| 파일 | Persona | Domain | Accent |
|---|---|---|---|
| `01_KIM_MANAGER` | 김매니저 | B2C · Fan Relationship | Navy |
| `02_LEE_MANAGER` | 이매니저 | B2B · Sponsorship Sales | Orange |
| `03_KIM_HANA` | 김하나 (d'Alba, 예시) | Sponsor · Brand | Teal |
| `04_IRUKI` | 이루키 | Fan · B2C Customer | Pink |
| `05_PERSONA_MAP` | 4인 관계도 | — | Navy+Orange |

레이아웃: 왼쪽 = 아바타(모노그램)·이름·역할·태그라인·업무방식/팬특성 / 오른쪽 = 핵심 이슈 · Pain Point/현재 상태 · 목표 · **핵심 질문 배너**. Persona별 색으로 한눈에 구분.

---

## 1. 각 Persona에서 00_STORY.md의 어떤 내용을 썼는가

### 01 김매니저 — B2C FRM Manager
- **§4** "Salesforce Customer 360을 사용하는 User", Mission(팬 데이터 분석→Next Best Action→충성 팬)
- **§1** Business Goal(신규 팬 이해→개인화 액션→충성 팬→시즌권→Fan LTV)
- **§2 Pain Point 1–5**: 정보 분산 / 360 Fan View 부재 / 세분화 불가 / 타이밍 놓침 / 우선순위 없음 → "데이터는 많지만 Action이 없다"
- **§3** KPI(활성화율·첫 관람 전환율·재방문율·첫 굿즈·멤버십·시즌권·Fan LTV)
- **§5** Customer Journey, **§6** Current Segment 3축, **§7** Next Best Action 표(Welcome/First Ticket/First Visit/First Merchandise/Favorite Player/Membership)

### 02 이매니저 — B2B Sponsorship Sales Manager
- **§4 [P2]** "이 매니저(가칭)" — Mission(Fan 360 근거로 광고 가치 높은 기업 발굴→Lead→Opp→Contract→Sponsorship Revenue), 5개 주요 고민, **이름 가칭·프로필 TBD**
- **§1 [P2]** Phase 2 Business Goal
- **§2 [P2] Pain Point 1–7**: 팬↑인데 적자 / 어떤 기업이 광고비 낼지 모름 / 팬 관심사 모른채 영업 / Fit 검증 방법 없음 / Fit≠계약가능성 / Pipeline·Revenue 관리 불가 / 과거 "40~50대 남성" 가정 실패
- **§8.3** 여정(Fan 360 분석→광고 가치 발견→기업 DB 100개→Agentforce Top 10+Reason→Outbound Lead→Lead Score→Account/Contact→Opportunity→Package/Quote→Negotiation→Closed Won→Dashboard)
- **§8.3 표** Agentforce Fit Score vs Lead Score 구분, **§9** B2B Next Best Action

### 03 김하나 — Sponsor / d'Alba (예시 시나리오)
- **§8.3** d'Alba(달바) = 뷰티/스킨케어 브랜드, Top 10 추천 중 Fan Fit 높은 대표 사례
- **§8.3-1** 팬덤 특성(여성 팬 유입↑, 뷰티·라이프스타일·F&B 관심↑)
- **§8.3-6** Sponsorship Package(구장·전광판·펜스 광고, 공식 SNS 노출, Brand Day, 프로모션, Collaboration Goods)
- **§8.2** "유명한 회사에 제안서 보내기 vs 광고 가치 검증", Recommendation Reason
- **§2 [P2] Pain Point 4·7** 관점을 스폰서 쪽에서 재구성(Fit 검증 근거 필요 / 잘못된 타깃 가정 경계)
- **이름 "김하나"와 직책은 문서에 없음** → "예시 시나리오"로 명시. d'Alba 담당자라는 역할과 판단 관점만 사용.

### 04 이루키 — Fan / B2C Customer
- **§4** "27세, 직장인, 신규 팬" — 야구 거의 안 봄 / SNS에서 문선수 영상 / 친구와 첫 직관 / 응원 문화에 빠져 팬이 되어감
- **§5** Customer Journey(SNS→가입→첫 티켓→첫 직관→첫 굿즈→재방문→멤버십→충성팬)
- **§6** Current Segment(New Fan / Active Fan …)
- **§2 Pain Point 2·3** 를 팬 입장에서 재구성(나를 이해하는가 / 모두에게 같은 이벤트·쿠폰·메시지)
- **§7** Next Best Action(굿즈·재방문·멤버십 안내) → "적절한 시점의 다음 단계 제안"
- **§4·§8.3** "이루키의 데이터가 쌓일수록 이매니저의 근거도 쌓인다" — 팬↔B2B 연결고리
- 사용자 지정 "20대 여성 대표 팬" + 문서의 "27세 직장인"을 병기.

### 05 Persona Map
- **§1·§3** 두 Phase의 목표, **§4·§5** 페르소나, **§8.3** Fan 360 데이터가 B2B 매칭의 근거가 되는 논리
- 좌축(Fan Value): 이루키 → 팬 데이터·팬덤 가치 → 김매니저 → 팬 로열티·팬 기반 수익화
- 우축(Sponsor Value): 김하나 → 브랜드 가치·광고주 니즈 → 이매니저 → Sponsorship·Contract Revenue
- 교차(핵심): 이루키의 Fan 360 데이터 → 팬덤의 광고 가치·Fan Fit 근거 → 이매니저(Agentforce Matching)
- 수렴: Fan Value + Sponsor Value → **Cloud Alpacas의 지속 가능한 매출 엔진**

---

## 2. Persona별 핵심 Pain Point / Goal

| Persona | 핵심 Pain Point | 핵심 Goal | 핵심 질문 |
|---|---|---|---|
| 김매니저 | 데이터는 많은데 Action이 없다 — 흩어진 정보, 자동 세분화 불가, 타이밍·우선순위를 놓침 | 신규 팬을 개인화 액션으로 충성 팬으로 성장, Fan LTV 극대화 | 어떤 팬에게 지금 무엇을 제안해야 하는가? |
| 이매니저 | 팬은 느는데 적자, 광고 가치 높은 기업을 가릴 근거 없음, Fit≠계약 가능성, Pipeline 가시성 없음 | Fan 데이터 근거로 기업 발굴 → Pipeline → Sponsorship Revenue | 어떤 기업을 먼저 접촉하고 어떻게 계약으로 이끌 것인가? |
| 김하나 | 팬덤과 브랜드 타겟의 적합도를 확인할 근거가 없음, 잘못된 타깃 가정 리스크 | Brand Fit 확인, 스폰서십 투자 대비 Business Outcome 확보 | Cloud Alpacas 팬덤이 우리 브랜드에 어떤 가치를 주는가? |
| 이루키 | 모든 팬에게 똑같은 이벤트·쿠폰·메시지, 다음 단계 안내 없음 | 취향에 맞는 개인화 경험, 적절한 시점의 제안, 충성 팬으로 성장 | 나에게 적합한 경험과 제안을 받고 있는가? |

---

## 3. 디자인에서 의도한 차이

- **Persona별 시그니처 색**: 김매니저 Navy(B2C 운영), 이매니저 Orange(B2B 영업), 김하나 Teal(외부 스폰서 — 구단 내부와 구분), 이루키 Pink(고객/팬). 발표 화면에서 색만으로 누구인지 즉시 구분.
- **B2C vs B2B**: 김매니저는 "팬 이해→추천→개인화→Action", 이매니저는 "발굴→Fit→영업→제안→계약". 하단 핵심 흐름 문구로 대비.
- **내부자 vs 외부자**: 김매니저·이매니저는 "구단이 겪는 문제"(Pain Point), 김하나는 "스폰서가 갖는 우려"(우려·현재 상태), 이루키는 "팬이 느끼는 불편". 카드 제목을 관점에 맞게 다르게 표기.
- **김하나 = 예시임을 3곳에 표시**(아바타 라벨·역할·푸터) — 없는 개인정보를 사실처럼 보이지 않게.
- **Persona Map**은 4장의 요약이 아니라 "두 수익 축이 같은 Fan 360 데이터 위에서 맞물린다"는 비즈니스 구조를 전달하는 것이 목적. 교차 화살표(이루키→이매니저)가 이 스킬의 핵심 메시지.
- 공통: 16:9, 밝은 배경, 카드·둥근 모서리·큰 타이포, gradient 없음, 아바타는 사진 대신 모노그램(가상 인물의 얼굴을 만들지 않음).

---

## 4. 추가 확인이 필요한 정보

- **이매니저 이름·세부 프로필**: `00_STORY.md §4`에서 "가칭 · TBD". 확정 시 `_generator.py`의 `LEE_MANAGER["name"]`, `role` 수정.
- **김하나 이름·직책**: 문서에 근거 없음 — 현재 "예시"로 표기. d'Alba 실제 담당자 페르소나를 확정하려면 별도 인터뷰/설정 필요.
- **이루키 성별**: `00_STORY.md §4`는 "27세, 직장인"만 명시(성별 없음). 사용자 요청 "20대 여성 대표 팬"과 `§8.3`의 "여성 팬 유입 급증" 맥락으로 여성으로 표기 — 확정 필요.
- **이루키 관심사**: 문서 근거는 "문선수(favorite player)·직관·응원문화". 뷰티/라이프스타일/F&B는 팬덤 **집단** 특성(§8.3)이지 이루키 개인 설정이 아니므로 개인 프로필에는 넣지 않음.
- **KPI 수치·목표값**: `00_STORY.md`는 KPI 항목만 나열. 실제 목표치는 `03_SYSTEM.md`/`P2_DUMMY_DATA_MASTER.md`에서 TBD.
- **d'Alba Sponsorship 시나리오 상세**(Quote 금액, Package 구성): `04_DEMO.md` / `03_SYSTEM.md §7` TBD.
