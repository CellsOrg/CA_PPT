# PPT_V3 · 03_WIREFRAME — 슬라이드별 구성

상태: 최종 동기화본 · 16:9 · 총 29장 (00 Cover · 01–25 본편 · 06A · 26 · 27)

## 공통 규칙

- 배경은 딥 네이비/페이퍼 그레이, 핵심 전환은 오렌지와 라이트 블루로 표시한다.
- 제목은 한 슬라이드에 하나의 판단 또는 메시지를 전달한다.
- 본문은 발표자가 설명할 수 있도록 짧은 문장·카드·흐름도로 구성한다.
- 데모 화면 영역은 실제 검증된 캡처·영상으로 교체하되, 와이어보드의 정보 구조는 유지한다.
- 06A의 QR과 27의 sad 이미지는 placeholder가 아니라 실제 asset을 사용한다.

## 00 · Cover

- 한 줄 메시지: From Fan Data to Revenue.
- 온슬라이드 문구:
  - (로고/워드마크) CLOUD ALPACAS
  - H1: "FROM FAN DATA TO REVENUE."
  - 하단: "Cellsforce · Cloud Alpacas Fan Relationship Management Team | Final Presentation"
- 비주얼 구성: 타이포 중심. 대형 타이틀 1문장 + 팀 1줄. 배경 장식 최소, 마스코트·부제 설명문 없음.
- 미디어/asset: 없음 (기존 Cover 디자인 그대로).
- 발표자 멘트: "Cloud Alpacas Fan Relationship Management 팀입니다. 오늘 발표는 '팬 데이터가 어떻게 수익으로 이어지는가'에 대한 이야기입니다."
- 다음 전환: 01 프로젝트 선정 배경.
- 넣지 않는 것: 목차, 아젠다, 부제 설명문, 이미지·차트.

## 01–05 · 프로젝트 개요와 설계 기준

### 01. 프로젝트 선정 배경

- 헤드라인: "팬의 성장은 왜 구단의 지속 가능한 수익으로 이어지지 않는가"
- 좌측: 성장하는 팬덤과 수익성 문제
- 우측: B2C ↔ B2B 연결 구조
- 하단: Salesforce CRM으로 Fan Value를 지속 가능한 수익 기회로 전환한다는 결론

### 02. Cloud Alpacas 소개

- 헤드라인: "Cloud Alpacas는 팬과 기업을 동시에 상대하는 가상 프로야구 구단이다"
- 중앙: B2C Fan Business ↔ Fan Value ↔ B2B Sponsorship Business 흐름
- 하단: 티켓·멤버십·굿즈 / Sponsor 발굴·제안·계약·Partnership 운영을 병렬로 제시
- 우측: Salesforce 도입 목표 — 지속 가능한 매출 엔진과 흑자 전환

### 03. 팀 구성과 역할

- 고객 여정 구간별 오너십을 카드로 표시
- 역할의 범위와 협업 접점을 함께 제시

### 04. 수행 절차 및 방법

- 문제 정의 → 설계 → 구현 → 검증 → 데모 흐름
- 각 단계의 산출물을 간결한 타임라인으로 표시

### 05. AS-IS → TO-BE 핵심 변화

- 좌측 AS-IS 3개 카드: B2C 개인화 난이도 / Fan Insight와 Sponsorship 단절 / 활용되지 못하는 영업 경험
- 중앙: 변환 화살표
- 우측 TO-BE 3개 카드: Fan Data → Personalized Engagement / Fan Insight → Sponsorship Opportunity / Sales Activity → Intelligence → Action
- AS-IS와 대응 TO-BE에 같은 계열 색을 사용해 "문제에서 변화로" 이동을 보이게 함

## 06 · Scene S1 개요 — Fan 360

- 헤드라인: "팬 데이터를 한 화면에서 입체적으로 이해한다" / 부제 "우리 팬은 누구인가?"
- 좌: Fan 360 실제 화면 캡처 자리
- 우: BUSINESS VALUE = Fan Understanding / DEMO POINT = 무엇을 증명할 것인가

## 06A · Fan Event — Game Day

- 한 줄 메시지: 지금 이 자리에서 실제로 Fan Data가 만들어지는 첫 순간.
- 온슬라이드 문구:
  - "LIVE SCOREBOARD MOCK — 실제 전광판 화면처럼"
  - "CLOUD ALPACAS · GAME DAY LIVE" / "⚾ 7회말 경기 진행 중"
  - "🎁 FAN EVENT OPEN — \"문태양 선수 퀴즈에 참여하세요\""
  - QR 아래: "SCAN TO JOIN · QR을 찍고 참여해주세요"
  - flow: 관객 QR 참여 › Quiz Entry (FanQuiz Site) › Fan Activity › Salesforce (저장) › Fan 360 (연결)
- 비주얼 구성: 전체 딥 네이비 전광판 목업. 중앙에 큰 실물 QR. 하단에 참여→CRM 데이터 개념 flow 띠. 설명문 최소.
- 미디어/asset: **`src/quiz-qr.jpg`** (필수). 발표 현장에서 스캔 가능한 크기·대비로 크게 배치. destination URL·내용 변경 금지.
- 발표자 멘트: "지금 여러분은 Cloud Alpacas 경기장의 관객입니다. 전광판에 이벤트가 떴습니다. QR을 찍고 참여해주세요." — 기능 소개가 아니라 '지금 실제로 팬 데이터가 만들어지는 중'이라는 느낌.
- 화면 — 보여줄 것/주의: FanQuiz Experience Site (liveFanQuizEntry LWC). 하단 띠 = 참여가 CRM 데이터가 된다는 개념도. Campaign 연동은 검증된 경우에만 Campaign Member 생성 설명. 당첨자 추첨·안내는 27에서.
- 다음 전환: 07 S1 Demo Flow (방금 만들어진 데이터가 Fan 360으로).
- 넣지 않는 것: 이벤트 경품 상세, 당첨자 명단, 광고 카피, 굿즈 배송 안내(27에서).

## 07–23 · 구현 결과 및 데모

각 Scene은 **개요 1장 + Demo Flow 1장**의 쌍으로 구성한다. 개요는 업무 가치와 데이터 흐름, Demo Flow는 실제 조작 순서와 화면 캡처·영상 자리로 사용한다.

| Scene | 개요 슬라이드 | Demo Flow 슬라이드 | 전달할 연결 |
|---|---:|---:|---|
| S1 | 06 | 07 | Fan Data → Fan 360 |
| S2 | 08 | 09 | AI 제안 → 사람 검토 |
| S3 | 10 | 11 | Fan Insight → Sponsor 탐색 |
| S4 | 12 | 13 | Sponsor 후보 → 가치 기반 평가 |
| S5 | 14 | 15 | Lead → Opportunity |
| S6 | 16 | 17 | Online Meeting → Sales Intelligence |
| S7 | 18 | 19 | Deal Context → Stage Guidance |
| S8 | 20 | 21 | Quote·고객 신호 → Negotiation Strategy |
| S9 | 22 | 23 | 계약 이후 → Long-term Partnership |

## 24–25 · 성과와 회고

### 24. 성과 및 마무리

- 핵심 구현 성과 2~3개
- Pain Point 해결을 설명하는 정성 또는 가능한 범위의 정량 지표
- 실무 적용 가능성과 다음 확장 방향
- 마지막 한 문장: "데이터가 쌓이는 CRM에서, 다음 행동을 연결하는 CRM으로"

### 25. 자체 평가

- 프로젝트 완성도(5점 만점)
- 잘한 점과 아쉬운 점
- 개선·보완점
- 개인 성과와 소감
- 실제 발표 시에는 팀원별 최종 문구를 넣고 필요하면 숨김 처리

## 26 · Ending — From Learning to Building

- 한 줄 메시지: 우리는 기능이 아니라 비즈니스에서 시작했다.
- 온슬라이드 문구:
  - 상단 label: "FROM LEARNING TO BUILDING"
  - 중앙: "We didn't start with Salesforce features. We started with the business."
  - (동의 대체안) "We came here to learn Salesforce. We leave knowing how to build with it."
- 비주얼 구성: editorial 타이포 포스터. 상단 작은 label + 중앙 두 문장이 전부. 과감하게 비운다.
- 미디어/asset: 없음.
- 발표자 멘트: 짧게. "우리가 배운 건 Salesforce 사용법이 아니라, 비즈니스에서 출발해 그걸로 만드는 방법이었습니다."
- 다음 전환: 27 Quiz Winner / Gift Notice.
- 넣지 않는 것: Business→Domain→Entity diagram, Architecture diagram, Object 목록, 기술 스택, KPI, 팀 소개, 긴 설명, Winner·Quiz·Q&A 내용, 굿즈 배송 안내.

## 27 · Quiz Winner / Gift Delivery Notice

- 한 줄 메시지: 준비한 선물이 발표일까지 못 왔어요 — 행사 후 직접 전달드릴게요.
- 온슬라이드 문구:
  - "TO OUR QUIZ WINNERS"
  - "준비한 선물이 발표일까지 도착하지 못했어요. 🥲"
  - "행사 후 직접 만나서 전달드릴게요. 조금만 기다려 주세요!"
  - (sad.png 내 문구) "경품은 추후 따로 만나서 전달드릴 예정입니다! / 조금만 기다려 주세요! 감사합니다!"
- 비주얼 구성: 큰 sad alpaca 이미지 중앙 + 상단 작은 label + 하단 한 줄 안내. card/UI 구성 없음.
- 미디어/asset: **`src/sad.png`** (필수). 메인 비주얼로 크게. "굿즈가 제때 도착하지 못한 상황"을 표현.
- 발표자 멘트: "퀴즈에 참여해주신 당첨자분들께 드릴 굿즈가 오늘까지 도착하지 못했어요. 행사 끝나고 직접 전해드릴게요. 참여해주셔서 감사합니다."
- 다음 전환: PPT 종료 → 필요 시 Salesforce Org LIVE → Q&A.
- 넣지 않는 것: 장황한 사과문, 당첨자 명단, Q&A 슬라이드, architecture/data 구성, 배송 추적 표.

## Ending 이후 실제 발표 진행

```
26 Ending → 27 Quiz Winner / Gift Notice → PPT 종료 → (필요 시) Salesforce Org LIVE → Q&A
```

별도 Winner / Quiz Result / Thank You / Q&A 슬라이드는 만들지 않는다.

## 산출물 대응

- `slides/slide-00.png` ~ `slides/slide-27.png` + `slides/slide-06A.png`: 슬라이드별 PNG (총 29장, 1920×1080)
- `slides/_original_backup/`: 06A 원본(placeholder QR) 백업
- `src/quiz-qr.jpg`: 06A 실물 QR
- `src/sad.png`: 27 메인 비주얼
- `src/slide-06A.source.html`, `src/slide-27.source.html`, `src/wf.css`: 06A·27 PNG 재생성용 소스
- `Cloud_Alpacas_Final_Wireframe.html`: 브라우저용 29장 갤러리 (실물 QR·sad.png 렌더링 포함)
