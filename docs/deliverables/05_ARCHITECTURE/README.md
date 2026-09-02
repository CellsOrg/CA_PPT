# 05. 시스템 아키텍처 — 최종 제출용 다이어그램

`../05_ARCHITECTURE.md` 를 근거로 만든 **PPT 삽입용 System Architecture Diagram**.

- `CLOUD_ALPACAS_ARCHITECTURE.svg` — Master (벡터)
- `CLOUD_ALPACAS_ARCHITECTURE.png` — 3840×2160, 16:9 PPT 삽입용
- `_generator.py` — 재생성 (`python3 _generator.py`, 표준 라이브러리)
- 원칙: `05_ARCHITECTURE.md` 에 없는 시스템·연동은 추가하지 않음

## 레이아웃

```
값 흐름 리본: 데이터 통합 → 팬·기업 이해 → AI·Automation 실행 → 고객 경험·비즈니스 성과

EXTERNAL SYSTEMS      SALESFORCE PLATFORM (중앙·최대·SF 블루 프레임)     BUSINESS OUTCOME
 Fan App        ──▶   1. Experience Layer                          ──▶  Fan 360
 OpenDART API   ──▶   2. Data / CRM Layer   ◀── (AI 출력→레코드)      ──▶  B2B Sponsorship
 Slack          ◀──   3. Automation Layer                          ──▶  PRM
 Agent API      ⇄     4. Application / Code Layer
                      5. AI Layer — Agentforce
                      substrate: 55 관리형 패키지 (미사용)
```

내부 5개 Layer는 위→아래 chevron으로 L1→L5 흐름을, 오른쪽 되돌림 화살표로 "AI 출력은 항상 레코드로 저장"을 표현.

---

## 05_ARCHITECTURE.md 에서 시각화한 내용

| 다이어그램 요소 | 근거 (05_ARCHITECTURE.md) |
|---|---|
| 값 흐름 리본 (4단계) | Purpose + §7 User/Business Layer + Known Limitations 취지 |
| **Salesforce Platform 5 Layer** | §1 Layer 개요도 (L1–L5) + §2 Layer별 책임 표 |
| 1. Experience Layer | §2-1 — Lightning Experience, PRM 포털(prm* LWC 13), FanQuiz Site, Partnership Inquiry Site, Fan App ingest, Guest Profile 2 |
| 2. Data / CRM Layer | §2-2 + 수치표 — Standard Objects 8종, 17 Custom Objects, DART_Setting__c, RecordType 12 |
| 3. Automation Layer | §2-3 + 수치표 — 40 Active Flows (Record-triggered·AutoLaunched·Platform-Event), Platform Event `Fan_Campaign_Msg_Request__e`, "Flow 우선/Trigger 최소" (Decision 008) |
| 4. Application / Code Layer | §2-4 + 수치표 — 100 Apex Classes(Controller·Agent Action·Invocable·Queueable), 1 Trigger `LeadConvertPartnerContact`, 46 LWC |
| 5. AI Layer — Agentforce | §2-5 + 수치표 — 5 Agentforce Agents(VIP Recommendation·Opportunity·Negotiation·Sponsorship Proposal·Sponsorship Campaign), 6 Prompt Templates, "출력은 항상 레코드로 저장 → Human-in-the-loop" |
| L1→L5 chevron 흐름 | §1 mermaid `L1→L2→L3→L4→L5` |
| AI → Data 되돌림 화살표 | §1 mermaid `L5 → L2` + §2-5 "Agent/Prompt 출력은 레코드로 저장" |
| substrate 주석 | §3 mermaid `SUBSTRATE` — 55 관리형 패키지 + SDO/QBrix (FSL·Maps·Pardot·Marketing Cloud·Sales Planning) |
| **External — Fan App** | §2-1, §6 — Demo 데이터 채널, `Fan_App_API_Access` PS |
| **External — OpenDART API** | §6 — `opendart.fss.or.kr`, RemoteSite `opendart_fss`, `DART_Setting__c.Api_Key__c` |
| **External — Slack** | §6 — `Campaign Deliverable Blocked Slack Alert`, `sfdc_slack` PS (채널 ID 미검증) |
| **External — Agent API** | §6 — Named Credential `CA_Agent_API` (SecuredEndpoint, api.salesforce.com, 사용처 미확정) |
| 연동 방식 라벨 | §6 표 — "REST upsert (External_ID__c)·API user" / "REST GET·Apex HTTP callout" / "Flow → Slack action" / "Named Credential" |
| 연결 방향 | §3 mermaid — FanApp→Fan360(in), DART→B2B(in), B2B→Slack(out), AgentAPI(⇄) |
| **BUSINESS OUTCOME 3 도메인** | §7 표 — Fan 360 / B2B Sponsorship / PRM 의 목표 + 지원 Layer 구성 |
| Out of Scope | §6 하단 + §4 — Marketing Cloud·Pardot·Data Cloud (패키지만), 결제 PG 없음 (`Order.Payment_Status__c`) |

---

## 최종 검수 (요청 13항)

| # | 항목 | 결과 |
|---|---|---|
| 1 | 문서에 없는 시스템 추가 안 함 | ✅ External 4종·5 Layer·substrate 전부 §1/§2/§3/§6 근거 |
| 2 | 핵심 시스템 누락 없음 | ✅ 7개 Layer 중 아키텍처 관점 L1–L5 + Integration + Business 반영 |
| 3 | Salesforce Platform 중앙·강조 | ✅ 화면 중앙·최대 폭·SF 블루 프레임 |
| 4 | External ↔ Salesforce 경계 명확 | ✅ 좌측 별도 카드군 + 경계선 + 방향 화살표 |
| 5 | 데이터/호출 방향 이해 가능 | ✅ in/out/⇄ 구분, chevron, 되돌림 화살표 |
| 6 | Integration 방식이 문서와 일치 | ✅ §6 표의 방식(REST upsert·Apex callout·Flow Slack·Named Credential) 그대로 |
| 7 | ERD처럼 Object-level 복잡화 안 됨 | ✅ 개별 Object 나열 대신 그룹+수치(17/40/100/46/5/6) |
| 8 | 16:9에서 글자 읽힘 | ✅ 1920×1080 / PNG 3840×2160, 본문 최소 11px |
| 9 | Navy/Orange 아이덴티티 | ✅ Navy #07111F·Orange #FC4E00 중심, 플랫폼 프레임만 SF 블루 |
| 10 | 10초 내 전체 구조 이해 | ✅ 좌(외부)→중앙(Salesforce 5 Layer)→우(비즈니스 성과) 3단 구조 |

## 사람이 확인해야 하는 부분 (문서 §4 Known Limitations 반영)

- Fan App 실제 연동 프로토콜/호스트 — 미확인 (다이어그램 "REST upsert" 는 추정)
- `CA_Agent_API` Named Credential 실제 호출 코드 — 사용처 미확정
- Slack 채널·앱 구성 — Flow 내 채널 ID 미검증
- Opportunity Agent 활성 버전 (v1–v23 중 1개) — 다이어그램에 버전 미표기
- Experience Site 상세 (Network/DigitalExperienceBundle) — 미 retrieve, Guest Profile 존재만 확인
- Business Layer의 Flow/Object 개수(11/17, 6/15 등)는 §7 표 기재값 — 재집계 시 갱신 필요
