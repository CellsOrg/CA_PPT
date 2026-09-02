# ORG_VS_DOCUMENT_GAP — Cloud Alpacas

> **Source of Truth: Salesforce Org Metadata — 2026-08-31**
> `ORG → 03_SYSTEM_ORG.md → ERD_OBJECT_LIST.md` 흐름과, 기존 문서(`CloudAlpacas/docs/00_STORY.md`, `01_PROJECT.md`, `03_SYSTEM.md`, `05_DECISIONS.md`, `docs/members/*.md`, `workshop/05_OBJECT_MAP.md`) 사이의 **차이만** 기록한다.
>
> **원칙:** 두 상태를 **병합하지 않는다.** 각 항목을 `Org Actual` / `Document Design` / `Gap` 3개로 분리해 적는다.
> **이번 작업 범위 아님:** 기존 문서는 수정하지 않는다. 이 문서는 사용자 검토용 차이 목록이다.
>
> ⚠️ 참고: `cloudalpacas-org-inventory/docs/` 에 복사된 기존 문서는 **2026-08-19 스냅샷**이다 (`05_DECISIONS.md` 는 D-020 까지). 프로젝트 `CLAUDE.md` 는 08-28 기준(D-031, P0/P1 언급) — 문서 세트 자체가 서로 시점이 다르다.
>
> **Rev.2 정정 (2026-08-31):** 아래 A-1 의 "Custom Object 18개" 는 `DART_Setting__c` (Hierarchy Custom Setting) 를 포함한 수치. 실제 팀 Custom Object 는 **17개** + Custom Setting 1개. 최신 산출물: `deliverables/01_ERD.md`~`05_ARCHITECTURE.md`.

---

## A. Custom Object

### A-1. Object 개수

| | 내용 |
|---|---|
| **Org Actual** | 팀 제작 Custom Object **18개** (`Season__c`, `Game__c`, `Admission__c`, `Attendance_Record__c`, `Engagement_Signal__c`, `Fan_Activity_Pattern__c`, `Fan_Segment_History__c`, `Recommendations__c`, `Benefits__c`, `Notification_Log__c`, `Quiz_Entry__c`, `Campaign_Deliverable__c`, `Interaction_Intelligence__c`, `Interaction_Signal__c`, `Sales_Briefing__c`, `PRM_Revenue_Target__c`, `DART_Corp_Mapping__c`, `DART_Setting__c`) + Platform Event `Fan_Campaign_Msg_Request__e` |
| **Document Design** | `03_SYSTEM.md §1.2` = **10개** (`Season__c`, `Game__c`, `Admission__c`, `Benefit__c`, `Notification_Log__c`, `Attendance_Record__c`, `Engagement_Signal__c`, `Fan_Activity_Pattern__c`, `Fan_Segment_History__c`, `Recommendation__c`). `workshop/05_OBJECT_MAP.md` 동일. B2B Object는 `03_SYSTEM.md §7` DRAFT. |
| **Gap** | Org에 **+8**: `Quiz_Entry__c`(D-031 P1), `Campaign_Deliverable__c`(§7 DRAFT→구현), `Interaction_Intelligence__c`·`Interaction_Signal__c`(문서 없음), `Sales_Briefing__c`(문서 없음), `PRM_Revenue_Target__c`(문서 없음), `DART_Corp_Mapping__c`(D-020과 상충), `DART_Setting__c`(문서 없음). Platform Event는 문서에 개념 없음. |

### A-2. `Recommendation__c` (단수)

| | 내용 |
|---|---|
| **Org Actual** | `Recommendations__c` (복수, Label "Fan Recommendation", Deployed). 단수 `Recommendation__c` 는 Tooling `CustomObject` phantom row(Rafael 08-12)만 존재, `EntityDefinition`·`describe` 실패 → **실 Object 아님**. |
| **Document Design** | `03_SYSTEM.md §1.2/§2.15/§3`, `workshop/05_OBJECT_MAP.md`, `01_PROJECT.md §5` 전부 `Recommendation__c` (단수). Decision 004·009·010 도 단수. |
| **Gap** | **API Name 불일치.** 문서 전체의 `Recommendation__c` → 실제 `Recommendations__c` 로 교체 필요. 단수 phantom row는 삭제 검토. |

### A-3. `Benefit__c` (단수)

| | 내용 |
|---|---|
| **Org Actual** | `Benefits__c` (복수, Deployed). 추가로 **표준 `Benefit` Object에도** `Badge_Label__c`/`Discount_Rate__c`/`Min_Purchase_Amount__c` 3필드가 Sara에 의해 08-28 생성됨 (커스텀 `Benefits__c` 와 동일 이름). |
| **Document Design** | `03_SYSTEM.md §2.8` `Benefit__c` (단수). Decision 006 은 "Benefit Object 최소화" — Redemption 분리 안 함. |
| **Gap** | **API Name 불일치** + **중복 위험**: `Benefit`(표준) vs `Benefits__c`(커스텀). 실사용 하나로 통일 필요. |

### A-4. 만들지 않기로 한 Object

| | 내용 |
|---|---|
| **Org Actual** | `Benefit_Redemption`, `Collaboration__c`, `Ballpark/Section/Seat/Gate`, `Shipment`, `Return` — **없음** (필드로 대체: `Benefits__c.Status__c`/`Used_Date__c`, Campaign RT `Sponsorship_Collaboration`, `OrderItem.Seat_Number__c`/`Row__c`/`Section__c`, `Admission__c.Gate__c`). |
| **Document Design** | `03_SYSTEM.md §1.3` / Decision 005·006 = 전부 Future Scope (안 만듦). |
| **Gap** | **일치.** 문서 결정대로 구현됨. |

---

## B. Standard Object Custom Field

| Object | Org Actual (CA 필드) | Document Design | Gap |
|---|---|---|---|
| **Account** | 37개 — Fan 12(Rafael/Sara) + B2B·DART 20(Aaron) + 기타 5 | `03_SYSTEM.md §2.1` Fan 필드 목록 (대체로 일치). B2B는 `§7 K` 일부 DRAFT | Fan 필드는 **일치**. **DART/스폰서 집계 20개(Aaron)는 문서에 없음** |
| **Contact** | 5개 — `Position__c`, `Uniform_Number__c`, `Name_EN__c`, `SDO_PRM_*` 2 | `03_SYSTEM.md §2.2` `Position__c`, `Uniform_Number__c`, `Notes__c` | 대체로 일치. `Notes__c`는 표준/SDO, `Name_EN__c` 문서 없음 |
| **Lead** | 18개 (전부 Hyejune) — Score 5종, Final/Risk/Segment Match, `AI_Lead_Summary__c` 등 | `03_SYSTEM.md §7 E` Lead Score 만. `P2_B2B_ORG_BASELINE`(08-17) "CA 필드 0개" | **문서 대비 대량 신규** — 스코어링 체계 전체 미기재 |
| **Opportunity** | 41개 (Eunyeong 중심) — Last Contact, Next Activity, Expected Benefit 3, Client Budget, Customer KPI/Needs, Target Season 등 | `03_SYSTEM.md §7 F~K` 일부 DRAFT (Expected Benefit, Target Segment, Segment Match). `P2_B2B_ORG_BASELINE` "CA 필드 확인 안 됨" | **DRAFT → 전면 구현.** 활동 추적 필드군(Last/Next Activity, Task Count)은 문서에 아예 없음 |
| **Order / OrderItem** | Order 9 + OrderItem 5 (전부 Rafael) | `03_SYSTEM.md §2.4` + Decision 013 (Payment/Refund/Coverage 필드) | **일치** — Decision 013 대로 |
| **Campaign** | Roll-Up 2 + `Performance_Summary__c` (Rafael) + RT 7종 | `03_SYSTEM.md §7 D` Campaign vs Collaboration DRAFT | Roll-Up·성과요약 문서 없음. RT는 문서보다 앞섬 |
| **Product2** | `Category__c`, `Tier__c`, `Related_Player__c`, `Is_Player_Goods__c` + RT 5종 | `03_SYSTEM.md §2.3` + Decision 003 (Product2 RT) | 대체로 일치. `Sponsorship_Package` RT 추가 |
| **Case** | `Related_Order__c` + RT `Fan_Case` | `03_SYSTEM.md §2.9/§3.3` `Related_Order__c` | **일치** |
| **Activity** (Task/Event) | 6개 (Eunyeong) — `Meeting_Type__c`, `Key_Decision__c` 등 | `03_SYSTEM.md §4.6` "미정의 Trigger" | 문서가 "미정"이라 한 자동화가 이미 구현됨 |
| **AccountPlan** (표준) | 14개 (Aaron, 08-31) | 문서에 **전혀 없음** | **완전 신규.** 표준 Account Plan 기능 사용 — 팀 검토 필요 |

---

## C. Relationship / ERD

| 관계 | Org Actual | Document Design (`03_SYSTEM.md §3.4`) | Gap |
|---|---|---|---|
| `Game__c` → `Season__c` | Master-Detail | Master-Detail (Decision 011) | 일치 |
| `Admission__c` → `Attendance_Record__c` | Master-Detail | Master-Detail (Decision 012) | 일치 |
| `Admission__c` → Account(Fan) | 필수 Lookup (restrict) | `Person Account ||--o{ Admission__c` | 일치 (타입은 Lookup) |
| `Admission__c` → `Game__c` | 필수 Lookup | `Game__c ||--o{ Admission__c` | 일치 |
| `Admission__c` → `OrderItem` (`Order_Item__c`) | 필수 Lookup | `OrderItem ||--o{ Admission__c` | 일치 |
| `Attendance_Record__c` → Account | Lookup (**UNIQUE 아님**) | `Person Account ||--o| Attendance_Record__c` (1:1) | **부분 불일치** — 스키마는 1:N, "팬당 1건"은 Flow 규칙만 |
| `Order` → `Game__c` | Lookup | `Game__c ||--o{ Order` | 일치 |
| `Recommendations__c` → Account | 필수 Lookup | `Person Account ||--o{ Recommendation__c` | 일치 (이름만 복수) |
| `Recommendations__c` → `Campaign` | Lookup **존재** | 문서 §3.4 관계 **없음** | **Gap — 문서에 관계 1줄 누락** |
| `Benefits__c` → `Recommendations__c` | Lookup | `Recommendation__c ||--o{ Benefit__c` | 일치 (이름만 복수) |
| `Benefits__c` → Account | 필수 Lookup | `Person Account ||--o{ Benefit__c` | 일치 |
| `Notification_Log__c` → Account / Campaign | Lookup 2 | `Person Account`, `Campaign ||--o{ Notification_Log__c` | 일치 |
| `Engagement_Signal__c` → Contact(`Player__c`) | Lookup | `Contact ||--o{ Engagement_Signal__c` | 일치 |
| `Fan_Activity_Pattern__c` → `Season__c` | Lookup | `Season__c ||--o{ Fan_Activity_Pattern__c` (Decision 011) | 일치 |
| `Case` → `Order` (`Related_Order__c`) | Lookup | `Order ||--o{ Case` | 일치 |
| **B2B 전체** (`Interaction_Intelligence__c`↔`Interaction_Signal__c`, `Campaign_Deliverable__c`→Campaign MD, `Sales_Briefing__c`→User, `Opportunity`→`Interaction_Intelligence__c`) | 구현됨 | `03_SYSTEM.md §3` 정식 ERD에 **없음** (§7 일부 DRAFT) | **Gap — B2B 데이터 모델 전체가 문서 정식 ERD 밖** |

> **결론:** B2C ERD는 문서(`03_SYSTEM.md §3.4`)와 **거의 일치** — 이름(단수→복수)과 `Recommendations__c→Campaign` 1줄만 보정하면 됨. B2B ERD는 Org만 존재.

---

## D. Automation (Flow / Apex / Trigger)

| | 내용 |
|---|---|
| **Org Actual** | Active Flow 40 (record-triggered 중심), Apex Class 100(대부분 LWC Controller·Agent Action), Apex Trigger **1개**(`LeadConvertPartnerContact`). |
| **Document Design** | `03_SYSTEM.md §4` — Flow 중심 자동화 방향 명시. Decision 008: "Flow 우선, Apex는 복잡 로직만". `§4.6` 미정의 Trigger 목록. `04_DEMO` 등에서 Slack 알림 언급. |
| **Gap** | **방향성 일치** (Flow-first, Trigger 최소). `§4.6` "구현 전 확정 필요"라던 자동화(Fan Activity Pattern 재계산 등)는 이미 구현. 개별 Flow 40개의 정확한 이름·트리거는 문서에 없음 → `03_SYSTEM_ORG.md §6.1` 이 최초 정리. |

---

## E. Agentforce / AI

| | 내용 |
|---|---|
| **Org Actual** | 팀 커스텀 Agent **5종** (VIP Recommendation / Opportunity(v1–v23) / Negotiation / Sponsorship Proposal / 스폰서십 캠페인) + Prompt Template **6종** + Agent Action Apex 30+. |
| **Document Design** | `00_STORY.md §5`: "Agentforce ... 이번 MVP 범위에 포함하지 않으며 Future Scope". `members/02_EUNYEONG.md`: "Agentforce가 이번 MVP 범위 밖". **Decision 017**: Agentforce AI **Matching** 만 Phase 2 예외 편입. `CLAUDE.md`(08-28): **D-031 P0 = Recommendation Agent**. |
| **Gap** | 문서(08-19)와 **큰 불일치**. 08-28 CLAUDE.md 시점에 Recommendation Agent가 P0로 재편입됐고, Org에는 그 이상(Opportunity/Negotiation/Proposal/Campaign 에이전트)이 구현됨. `00_STORY.md §5` 텍스트가 현실과 다름. |

---

## F. 담당자 / 역할 (⚠️ Org `CreatedBy` 우선)

| 영역 | Org Actual (`CreatedBy`) | Document Design | Gap |
|---|---|---|---|
| Custom Object 18개 중 15개 · Order/OrderItem/Product2/Case 필드 | **Rafael Espada (= Seungwoo/승우)** | `members/01_SEUNGWOO.md`: 승우 = "설계된 Object를 Org로 만드는 Builder" | **일치** (Rafael Espada = 승우 persona 확인) |
| Fan Account 필드·`Fan` RecordType·초기 12필드 | **Rafael Espada** | `members/04_AARON.md`: 아론 = "Account/Contact End-to-End" | **부분 불일치** — Fan Account 골격은 Rafael, Aaron은 B2B/DART 필드 |
| **DART 연동 / AI 기업 매칭** (`DartService`, `DART_*` Object, `Account.DART_*`, Flow `DART Lead 전환 AI매칭`) | **Aaron Choi** | `members/03_HYEJUNE.md`: 혜준 = "기업 DB·Agentforce Matching". Decision 017 도 혜준 맥락 | **불일치 — 실제 구현자는 Aaron** |
| Lead Scoring · PRM 포털 · Sales Briefing | **Hyejune Jo** | `members/03_HYEJUNE.md`: 혜준 = Collab360 + Lead | **일치** (Lead 쪽) |
| Negotiation / Sponsorship Proposal Agent | **Aaron Choi**(생성) → Eunyeong(Apex 수정) | 문서에 담당 명시 없음 | 신규 — Aaron 오너 |
| Opportunity 필드·Flow·Agent(v23)·Interaction Intelligence | **Eunyeong Doh** | `members/02_EUNYEONG.md`: 은영 = Opportunity, Developer Lead | **일치** |
| VIP Recommendation Agent · Quiz · Fan Segmentation UI | **Sara Bang** | `members/00_SARA.md`: 사라 = Fan Insight/Segmentation | **일치** |
| Campaign Deliverable · 스폰서십 Campaign Agent · 예상매출 Flow | **Rafael Espada** | `members/01_SEUNGWOO.md`: 승우 = Product+Quote+Campaign | **일치** |

> **핵심 Gap:** 문서의 "혜준 = DART/AI Matching" 기술이 Org와 배치. 실제 DART 스택 구현자는 **Aaron**. ERD·인벤토리에서는 Org `CreatedBy` 를 담당자로 사용한다 (단, "만든 사람" ≠ "현재 유지보수/오너"일 수 있음 — 팀 확인 필요).

---

## G. Decisions 대조

| Decision | Document Design | Org Actual | Gap |
|---|---|---|---|
| **D-003** Standard First, Custom When Needed | Person Account, Product2+Order, 최소 Custom | Person Account ✓, Product2 RT 5종 ✓, Custom Object 18(문서 10 예상) | 원칙 유지, 규모는 예상보다 큼 (B2B 확장분) |
| **D-005** Sponsorship Domain 제외 (Phase 1) | MVP 범위 밖 | Phase 2로 전면 구현 (Lead·Opp·Campaign·Agent) | D-015~019 로 편입됨 — 정합 (시점 차이) |
| **D-006** Benefit/Notification Object 최소화 | Redemption 분리 안 함 | `Benefits__c.Status__c`/`Used_Date__c` 로 처리 ✓ | **일치** |
| **D-011** Season MD + Roll-Up | `Season__c ||--(MD)--|| Game__c` | Org 확인 ✓ | **일치** |
| **D-012** Admission↔Attendance Record MD + Roll-Up | Master-Detail + Roll-Up Summary | Org: `Admission__c.Attendance_Record__c` MD ✓, `Total/First/Last_Admission__c` 롤업 ✓ | **일치** |
| **D-013** Order Payment/Refund/Coverage 필드 | Payment_Status, Refund_Date/Reason, Coverage_Start/End | Org 전부 확인 ✓ | **일치** |
| **D-014** Fan Profile 원천 데이터 Account 비복제, Related List 참조 | 집계값을 Account에 중복 저장하지 않음 | Org: `Fan_Activity_Pattern__c` 에 `Total_Spend__c`/`Games_Attended__c` 집계 저장. Account 에도 `Engagement_Score__c` 등 집계 존재 | **부분 불일치** — 집계 필드가 여러 Object에 분산 저장됨 |
| **D-017** Agentforce AI Matching 만 Phase 2 편입 | Matching 예외 편입, 나머지 Agentforce는 Future | Org: 5종 에이전트 (Matching 외 Opportunity/Negotiation/Proposal/Campaign) | **불일치 — 범위 초과** |
| **D-020** 기업 DB는 Object 아님 (DART OpenAPI + Top 10 Recommendation) | `DART_Corp_Mapping__c` 같은 Object 만들지 않음 | Org: `DART_Corp_Mapping__c` + `DART_Setting__c` **존재** | **불일치 — 결정과 반대로 Object 생성** (보조 매핑 용도로 보이나 결정 재확인 필요) |

---

## H. 요약 — 문서 갱신 시 검토 항목 (사용자 결정 필요)

1. `03_SYSTEM.md §1.2` — Custom Object 10 → 18, `Recommendation__c`→`Recommendations__c`, `Benefit__c`→`Benefits__c`
2. `03_SYSTEM.md §3.4` — `Recommendations__c → Campaign` 관계 추가, `Attendance_Record__c` 1:1 표기 재검토(스키마 1:N)
3. `03_SYSTEM.md §3/§7` — B2B 데이터 모델(Interaction Intelligence/Signal, Campaign Deliverable, Sales Briefing) 정식 ERD 편입, §7 DRAFT 항목 상태 갱신
4. `00_STORY.md §5` — "Agentforce Future Scope" 문구가 현실(5종 구현)과 불일치
5. `members/03_HYEJUNE.md` / `members/04_AARON.md` — DART/AI Matching 담당자 정정
6. `05_DECISIONS.md D-020` — `DART_Corp_Mapping__c` 존재와의 상충 해소 (또는 새 Decision 기록)
7. `05_DECISIONS.md D-017` — Agentforce 실제 구현 범위로 갱신
8. `05_DECISIONS.md D-014` — 집계 필드 비복제 원칙 vs 실제 분산 저장 재확인
9. 신규 문서화 필요: `AccountPlan` 표준 Object 채택, `Quiz_Entry__c`/Experience Site, `PRM_Revenue_Target__c` 관계 설계
10. Org 클린업 선행: phantom(`Recommendation__c`,`User__c`), `_del__c`/`_tc__*` 잔재, `Benefit` vs `Benefits__c` 중복, Agent 버전 정리
