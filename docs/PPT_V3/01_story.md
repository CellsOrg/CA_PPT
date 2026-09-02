# PPT_V3 · 01_STORY — Cloud Alpacas 최종 발표 서사

상태: 최종 동기화본 · 29장 기준 (00 Cover · 01–25 본편 · 06A Fan Event · 26 Ending · 27 Gift Notice)

## 한 문장 메시지

Cloud Alpacas는 Salesforce를 통해 Fan Data를 개인화된 관계로, Fan Insight를 Sponsorship Opportunity로, Sales Activity를 다음 Action을 위한 Intelligence로 전환한다.

## 0. 시작 — Cover (슬라이드 00)

발표의 첫 화면이자 전체의 시작점이다. 타이포 중심의 표지로, 대형 타이틀 한 문장 "From Fan Data to Revenue."와 팀·발표 정보 한 줄만 둔다. 새로운 메시지를 만들지 않고 기존 Cover 디자인을 그대로 활용한다.

## 1. 프로젝트 개요 — 왜 이 주제인가 (슬라이드 01–02)

프로야구의 팬덤은 성장하지만, 팬 증가가 자동으로 지속 가능한 수익으로 이어지지는 않는다. Cloud Alpacas는 이 문제를 검토하기 위한 가상의 프로야구 구단 시나리오다. 구단은 개인 팬을 상대하는 B2C Fan Business와 기업을 상대하는 B2B Sponsorship Business를 함께 운영하며, 팬의 규모·특성·행동이 기업 제휴의 근거가 되는 구조를 가진다.

- B2C: 티켓·멤버십·굿즈 등 팬 관계와 매출을 관리
- B2B: Sponsor 발굴, 제안, 계약, Partnership 관리를 수행
- 연결점: Fan Value가 Sponsorship Value의 근거가 됨
- 목표: 외부 환경에 흔들리지 않는 지속 가능한 매출 엔진 구축과 흑자 전환

## 2. 설계 기준 — 팀·절차·문제 정의 (슬라이드 03–05)

- 03: 기능 단위가 아니라 고객 여정의 구간을 끝까지 책임진 팀 구성
- 04: 비즈니스 문제에서 시작해 검증 가능한 Demo까지 이어지는 수행 절차
- 05: 세 개의 단절을, 세 개의 연결된 Revenue Flow로 바꾼다

| AS-IS Pain Point | TO-BE Salesforce Value |
|---|---|
| 늘어난 팬, 어려워진 개인화 | Fan Data → Personalized Engagement |
| Fan Insight와 Sponsorship의 단절 | Fan Insight → Sponsorship Opportunity |
| 쌓이지만 활용되지 못하는 영업 경험 | Sales Activity → Intelligence → Action |

## 3. 구현·데모의 흐름 (슬라이드 06–23, 06A 포함)

### 3-0. Fan Event — Game Day (슬라이드 06A)

06과 07 사이에 삽입한 현장 이벤트 슬라이드다. "CLOUD ALPACAS · GAME DAY LIVE" — 팬이 경기장에서 실제로 이벤트에 참여하는 장면을 전광판 화면처럼 보여준다. 슬라이드에는 실물 QR(`src/quiz-qr.jpg`)을 발표 현장에서 스캔 가능한 크기로 크게 넣고, "SCAN TO JOIN · QR을 찍고 참여해주세요" 문구를 함께 둔다. QR의 destination은 변경하지 않는다.

이 슬라이드의 역할은 광고·이벤트 안내가 아니라 Demo narrative의 시작을 보여주는 것이다:

Fan participation → Fan Activity → Salesforce → Fan 360

즉 "지금 이 자리에서 실제로 Fan Data가 만들어지는 순간"이 첫 번째 데이터 생성 지점이며, 이후 06–23의 Fan 360과 개인화가 이 데이터 위에서 이어진다. 당첨자 추첨·안내는 27에서 마무리한다.

### 3-1. Scene 흐름 (슬라이드 06–23)

각 Scene은 개요 1장 + Demo Flow 1장의 쌍으로 구성한다.

1. Fan Data를 통합해 Fan 360과 개인화 기반을 만든다 (S1)
2. AI 제안과 사람의 검토를 연결한다 (S2)
3. Fan Insight를 Sponsor 탐색과 후보 평가의 근거로 쓴다 (S3–S4)
4. Lead에서 Opportunity로 이어지는 B2B 영업 흐름을 관리한다 (S5)
5. Online Meeting과 Activity를 영업 Intelligence로 축적한다 (S6)
6. Deal Context를 바탕으로 Stage별 다음 행동을 추천한다 (S7)
7. Quote와 고객 신호를 바탕으로 협상 전략을 정리한다 (S8)
8. 계약 이후에도 Partnership을 장기 관계로 관리한다 (S9)

## 4. 성과·마무리 (슬라이드 24)

발표에서는 핵심 구현 성과 2~3개, 가능한 범위의 정성·정량 근거, 실무 적용 가능성 및 확장 방향을 제시한다. 마지막 메시지는 "데이터가 쌓이는 CRM"이 아니라 "다음 행동을 연결하는 CRM"이다.

## 5. 자체 평가 (슬라이드 25)

프로젝트 완성도, 잘한 점과 아쉬운 점, 개선·보완점, 개인 성과와 소감을 팀원이 최종 작성해 반영하는 자리다.

## 6. Ending (슬라이드 26)

전체 발표의 마지막 메시지 슬라이드다. Closing tone은 자축이 아니라 quiet confidence + reflection + what we learned이다.

- 온슬라이드 문구(현재 반영): "We didn't start with Salesforce features. We started with the business."
- 같은 뜻의 대체 문구: "We came here to learn Salesforce. We leave knowing how to build with it."
- 기존 ending 디자인·문구가 이미 존재하므로 그것을 우선 유지한다.

Ending 안에는 퀴즈 당첨자·굿즈 배송 안내를 넣지 않는다. Ending은 "우리의 이야기"를 끝내고, 다음 슬라이드 27이 "관객에게 전달할 실제 안내"다.

## 7. Quiz Winner / Gift Delivery Notice (슬라이드 27)

발표 후반의 실제 안내 슬라이드다. Fan Event Quiz 당첨자에게 준비한 굿즈가 발표 당일까지 도착하지 못할 가능성이 있어, 현장에서 "당첨되신 분들께 준비한 굿즈는 발표일 이후 직접 전달드리겠습니다"라고 안내한다.

- 메인 비주얼: `src/sad.png` (큰 이미지 + 짧은 안내 문구, 과도한 UI/card 구성 없음)
- 톤: 미안함 + 따뜻함 + 감사 + 귀여운 Cloud Alpacas tone. 장황한 사과문은 피한다.
- 온슬라이드 문구(한국어 발표 기준):
  - "TO OUR QUIZ WINNERS"
  - "준비한 선물이 발표일까지 도착하지 못했어요. 🥲"
  - "행사 후 직접 만나서 전달드릴게요. 조금만 기다려 주세요!"
- 이 슬라이드는 Q&A 슬라이드가 아니다. 별도 Winner 명단 슬라이드도 만들지 않는다 — 27 하나로 끝낸다.

## 8. Ending 이후 실제 발표 진행

```
SLIDE 26 Ending
  ↓
SLIDE 27 Quiz Winner / Gift Notice
  ↓
PPT 종료
  ↓
필요하면 Salesforce Org LIVE로 전환
  ↓
Q&A
```

## 표현 원칙

- 이 산출물은 최종 발표용 와이어보드다. 데모 화면·영상 영역은 실제 검증된 캡처로 교체해 사용한다.
- 06A의 QR과 27의 sad.png는 placeholder가 아니라 실제 asset(`src/quiz-qr.jpg`, `src/sad.png`)을 사용한다.
- 가상 구단 설정과 발표 메시지를 실제 운영 성과나 외부 통계로 표현하지 않는다.
- 미검증 상태, 수치, E2E 결과는 사실처럼 단정하지 않는다.
- 기존 Demo sequence(순서·주인공·핵심 질문·핵심 기능·format·business narrative)는 임의로 재설계하지 않는다. 이번 동기화의 목적은 ADD / RESTORE / SYNCHRONIZE다.
