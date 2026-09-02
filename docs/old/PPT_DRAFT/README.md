# Cloud Alpacas — 최종 발표 PPT Draft

`Wireframe`이 아니라 **실제로 열어서 수정할 수 있는 PowerPoint 초안**이다.
PPT 담당자는 이 파일을 열어 텍스트·색·도형을 직접 다듬고, placeholder 자리에 실제 자산(스크린샷·영상·로고·QR)을 넣으면 된다.

---

## 파일

| 파일 | 설명 |
|---|---|
| **`Cloud_Alpacas_Final_Presentation_Draft.pptx`** | 21장. 16:9 (13.333 × 7.5 in ≈ 1920×1080). 모든 요소가 **네이티브 도형/텍스트/선** — 슬라이드를 통째로 PNG로 넣지 않았다. 각 슬라이드에 **발표자 노트** 포함 |
| `preview/01.png … 21.png` | 렌더 미리보기 (LibreOffice로 pptx → PDF → PNG). 최종 렌더는 PowerPoint에서 확인 |
| `build_pptx.py` | 이 pptx를 생성한 스크립트. 문구/레이아웃을 코드로 다시 만들고 싶을 때 |
| `render_preview.py` | pptx → preview PNG 재생성 |
| `assets/` | 실제 자산(로고·마스코트·스크린샷)을 넣는 곳 — `assets/README.txt` 참고 |

**재생성:** `python3 build_pptx.py && python3 render_preview.py`
(python-pptx / pymupdf / LibreOffice 필요. 미리보기에 Pretendard가 필요하면 `~/Library/Fonts`의 Pretendard OTF를 LibreOffice 폰트 폴더에 복사)

---

## 이 초안이 하는 일 / 하지 않는 일

**한다**
- 21장 전체 구조·순서·핵심 메시지·표현 방식(PPT/DEMO VIDEO/LIVE/FORMAT TBD)을 확정된 wireframe 그대로 옮김
- 편집 가능한 도형으로 레이아웃·타이포·브랜드 컬러를 잡아둠
- 스크린샷/영상/LIVE 화면/QR/로고가 들어갈 자리를 **명시적 placeholder**로 표시
- 발표자가 말할 내용을 **슬라이드 노트**로 분리 (슬라이드 위 텍스트는 최소화)

**하지 않는다 (담당자 몫)**
- 실제 Salesforce 스크린샷·데모 영상 삽입 → `[ SCREENSHOT ]` / `DEMO VIDEO 재생 영역` placeholder 교체
- Cloud Alpacas 로고·알파카 마스코트 삽입 → `[ ALPACA MASCOT + LOGO ]` placeholder 교체 (현재 자산 없음)
- 실제 QR 코드 → `QR PLACEHOLDER` 교체 (destination 확정 후)
- 차트에 수치 채우기 → `DATA PLACEHOLDER`. **임의 성장률·ROI·매출 증가율·KPI를 만들지 않음**
- Sponsorship 금액 → 발표 전 Product2/Quote/PPT/대사 하나로 통일 (04_DEMO 가격 검증)

---

## 21장 구조 (wireframe와 동일)

| # | 슬라이드 | 유형 | 표현 방식 |
|---|---|---|---|
| 01 | Cover | Hero (Navy full-bleed) | — |
| 02 | Business Challenge | Editorial + 2 chart placeholder | — |
| 03 | Pain Point | 카드 3개 (번호 / Headline / subline) | — |
| 04 | Our Approach | Automation Flow + DATA→INSIGHT→ACTION→REVENUE | — |
| 05 | Project Scope / Team | B2C → Fan Insight → B2B + Feature Owner 1줄 | — |
| 06 | Demo Map | 8-node 지도 (파랑 B2C → 초록 B2B, **Partner Matching**) | — |
| 07 | Live Event — Game Day | Hero (Navy) + 전광판 + QR placeholder | **LIVE** |
| 08 | S1 · FAN — "우리 팬은 누구인가?" | 스크린샷 placeholder + rail | **PPT** |
| 09 | S2 · ACTIVATE — "각 팬에게 어떻게 다르게?" | 영상 재생 영역 | **DEMO VIDEO** |
| 10 | Fan Insight — B2C→B2B Bridge | Split (B2C 파랑 / B2B 초록) + FAN INSIGHT pivot | **TRANSITION** |
| 11 | S3 · CONNECT — "팬 데이터를 B2B 기회로?" | LIVE 화면 placeholder | **LIVE** |
| 12 | S4 · Partner Matching — "왜 이 기업인가?" | FORMAT TBD 박스 | **FORMAT TBD** |
| 13 | S5 · PIPELINE — "후보를 Deal로?" | 스크린샷 + 5s 영상 | **PPT + 5s VIDEO** |
| 14 | S6 · UNDERSTAND — "고객은 무엇을 말했나?" | 영상 재생 영역 | **DEMO VIDEO** |
| 15 | S7 · REASON — "그래서 무엇을 제안할까?" | LIVE 화면 placeholder | **LIVE** |
| 16 | S8 · ACT — "고객의 변화에 어떻게?" | 스크린샷 placeholder | **PPT** |
| 17 | S9 · EXPAND — "1년 후, 다음 매출로?" | FORMAT TBD 박스 | **FORMAT TBD** (AI 역할·기능 미정) |
| 18 | Why This Architecture? | 설계 원칙 3개 카드 + 얇은 흐름 | — |
| 19 | How It Works | Working Flow + navy statement bar | — |
| 20 | What We Built → Business Value | FAN / INSIGHT / REVENUE 카드 3개 (구현요소 + Value ↑) | — |
| 21 | Future → Closing | NOW / FUTURE(점선·흐리게) + 대형 Closing 문장 (발표 마지막) | — |

> **당첨자 발표 슬라이드 없음.** 21 Closing 이후 발표자가 "오늘 참여해주신 분들 중…" 하며 LIVE 당첨자 발표 → Q&A로 전환한다.

---

## 브랜드 / 디자인 시스템

- **Navy `#0B2A47` / Deep Navy `#07203A`** (배경·제목) · **Orange `#E77C25`** (포인트·kicker·강조) · **Warm off-white `#FAF6F0`** (본문 배경)
- 보조: B2C `#2F6FB0` (파랑) · B2B `#1E7F58` (초록) · Chapter III `#0E6E77` (teal)
- 폰트 **Pretendard** (라틴·한글·CS 모두 지정). 담당자 PC에 Pretendard 설치 권장
- 얇은 hairline · 라운드 카드 · 넓은 여백 · 큰 타이포 · 카드 남발 안 함 · 장식/그라디언트 최소
- Hero(01·07·21)만 full-bleed Navy, 나머지는 off-white editorial
- **알파카 마스코트는 표지·이벤트·클로징에만** placeholder로 표시 (B2B/Best Practices 페이지엔 없음)
- 레퍼런스의 특정 회사/문구/레이아웃을 복제하지 않고 디자인 언어(editorial·corporate·큰 숫자·짧은 메시지)만 사용

---

## 자체 QA

| # | 항목 | 결과 |
|---|---|---|
| 1 | 21장인가 | ✅ 21 |
| 2 | 01–17 Demo 순서가 정확한가 | ✅ 06 Map · 07 Live · 08 S1 · 09 S2 · 10 Bridge · 11 S3 · 12 S4 · 13 S5 · 14 S6 · 15 S7 · 16 S8 · 17 S9 |
| 3 | PPT / VIDEO / LIVE / TBD 표현 방식이 정확한가 | ✅ 상단 배지 + 레이아웃(영상=재생영역 / LIVE=현장화면 / TBD=명시) |
| 4 | Pain Point가 정확히 3개인가 | ✅ 03: 흩어짐 / ACTION 없음 / 기업 기회로 연결 못 함 |
| 5 | Fan Insight가 B2C→B2B의 Bridge인가 | ✅ 10: B2C 마지막 단계, split + FAN INSIGHT pivot, 색 전환 |
| 6 | Business Opportunity가 아니라 Partner Matching인가 | ✅ 06·10·12·21 모두 Partner Matching |
| 7 | 18–19가 WHY / HOW로 압축되었는가 | ✅ 18 설계 원칙 3개 / 19 Working Flow |
| 8 | 20이 FAN → INSIGHT → REVENUE를 보여주는가 | ✅ 카드 3개 + Business Value ↑ 연결 |
| 9 | 21이 Future + Closing으로 끝나는가 | ✅ NOW/FUTURE + Closing 문장 (마지막 슬라이드) |
| 10 | 당첨자 발표용 별도 슬라이드가 없는가 | ✅ 없음 (노트로 안내) |
| 11 | 텍스트가 발표자가 말할 수 있는 수준으로 적은가 | ✅ 슬라이드당 Headline 1 + Supporting 1 + 요소 3~5, 나머지는 노트 |
| 12 | Navy + Orange + Alpaca identity가 느껴지는가 | ✅ 컬러 시스템 + 마스코트 placeholder(표지/이벤트/클로징) |
| 13 | 레퍼런스를 복제하지 않았는가 | ✅ 디자인 언어만 사용, 고유 문구/구조 |
| 14 | 모든 주요 object가 PowerPoint에서 수정 가능한가 | ✅ 슬라이드당 18–40개 네이티브 도형/텍스트/선, 이미지 삽입 0 |

### Story Flow 검수
문제(02·03) → 해결(04·05) → 실제 Demo로 증명(06–17) → 왜 이렇게 설계했나(18·19) → 무엇을 만들었고 어떤 가치가(20) → 미래 + Closing(21).  **→ 자연스럽게 이어짐.**

---

## 팀 확정 필요 (wireframe와 동일)

1. **S4 (12번)** — `Demo순서.png`에 S4 열이 없음. Partner Matching을 별도 페이지로 둘지 + 표현 방식(PPT/VIDEO/LIVE) 확정
2. **S9 (17번)** — 표현 방식·AI 역할·기능 모두 "미정". 재계약·Upsell 자동화 구현 근거 확정 후 채움
3. **금액** — S8(16번) 등 Sponsorship 금액 일원화
4. **자산** — Cloud Alpacas 로고·알파카 마스코트·실제 Salesforce 스크린샷·데모 영상·QR
