# PPT_v2 — Cloud Alpacas 최종 발표 와이어프레임 (새로 작성)

소스 문서에서 **처음부터 다시** 만든 최종 발표 storyboard.
`docs/deliverables/PPT_DRAFT` / `PPT_REDESIGN` / `PPT_WIREFRAME` 의 구조를 재사용하지 않았다
(단, 렌더링 도구 `wf.css` + Python 헬퍼는 mid-fidelity 와이어프레임 kit으로 그대로 사용).

## 파일

| 파일 | 역할 |
|---|---|
| `01_story.md` | 내러티브 — 청중·인상, 핵심 논지, AS-IS/TO-BE, 구현 vs Future Scope 가드레일, 표지·마무리 문구 |
| `02_slide_inventory.md` | 19장 목록 + 한 줄 메시지 + 표현 방식 + 공식 아젠다 매핑 + 품질 체크리스트 |
| `03_wireframe.md` | 슬라이드별 상세 스펙 (제목·온-슬라이드 문구·비주얼 구성·미디어 영역·발표자 멘트·전환·금지사항) |
| `_build.py` | 19개 HTML 생성 — **온-슬라이드 문구의 Source of Truth** |
| `wf.css` | 와이어프레임 스타일 kit (16:9 · 1920×1080 · Pretendard · Slate/Blue/Green/Navy) |
| `_shoot.sh` | HTML → 1920×1080 PNG (headless Chrome) |
| `NN_*.png` (19) | mid-fidelity 와이어프레임 — 최종 비주얼 디자인 아님 |
| `wireframe.pdf` | 19장 PNG 합본 |

## 구조 (19장)

```
CH I · WHY (01–05)        01 Cover · 02 Business Question · 03 What We Saw · 04 Our Approach · 05 How We Built It
CH II · DEMO (06–17)      06 Demo Map · 07 Live Event · 08 S1 FAN · 09 S2 ACTIVATE · 10 Fan Insight Bridge
   ↑ 순서·주인공·질문       11 S3 CONNECT · 12 S4 Partner Matching · 13 S5 PIPELINE · 14 S6 UNDERSTAND
   ·표현 방식 LOCKED        15 S7 REASON · 16 S8 ACT · 17 S9 EXPAND
CH III · SO WHAT (18–19)  18 What We Learned · 19 From Learning to Building
                          → (PPT 종료) → Salesforce Org LIVE → 퀴즈 당첨자 발표 → Q&A
```

> 19장 이후 당첨자 발표는 **실제 Salesforce Org 화면**에서 진행한다.
> Winner / Quiz Result / Thank You / Q&A 슬라이드는 만들지 않는다.

## 재생성

```bash
cd docs/PPT_v2
./_shoot.sh        # _build.py → HTML → PNG 19장
```

문구 수정 = `_build.py`, 레이아웃/스타일 = `wf.css`.
Demo 06–17의 순서·주인공·핵심 질문·표현 방식은 변경하지 않는다.

## 팀 확정 대기 (02_slide_inventory.md §5)

1. S4(12) 포함 여부 + 표현 방식 — `Demo순서.png`에 S4 열 없음
2. S9(17) 표현 방식·AI 역할·기능 — 전부 미정
3. 스폰서십 금액 일원화 — `SPN-LED-BRANDDAY` 3억/5.5억 상충
4. 이매니저 이름·프로필 — 가칭/TBD
5. Tableau Next 수치 검증 — 완료 전 수치 노출 금지
6. `AccountPlan` 표준 Object — 08-31 생성, 문서화·시연 범위 팀 확인
