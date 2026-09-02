# 03. Custom Metadata 정보 — Cloud Alpacas

## Scope
- Custom Metadata Type (`__mdt`)
- Custom Setting (List / Hierarchy)
- 각 항목의 용도·필드·사용처(Flow/Apex/LWC)·의존성

---

## 1. Custom Metadata Type (`__mdt`)

| | 내용 |
|---|---|
| **Org Actual** | Org 전체에 `__mdt` 타입 **15개** 존재: `AI_Agent_Label__mdt`, `B2BFeaturedProductsCfg__mdt`, `B2B_SPC_Delivery_Method__mdt`, `B2B_SPC_Tax_Rates__mdt`, `FSL__O2_Settings__mdt`, `Pardot_Template__mdt`, `QLabs__mdt`, `Slack__mdt`, `asj__VideoComponentSetting__mdt`, `bmpyrckt__Timeline_Configuration__mdt`, `vbtapp__TrialforceSetupScript__mdt`, `xDO_Base_QBrix_Register__mdt`, `xDO_Service_TrackedLoginApplication__mdt`, `xDO_Tool_TrackingEventJob__mdt`, `xdo__Demo_Boost_MQ__mdt` |
| **팀 생성 여부** | **0개.** 전부 SDO/QBrix 데모 스캐폴딩 또는 관리형 패키지 소유 (`CreatedBy` 팀원 IN 절 = 0건). `Slack__mdt`·`QLabs__mdt`·`xDO_*`·`B2B_*` = 데모 구성, `FSL__*`·`asj__*`·`bmpyrckt__*`·`vbtapp__*` = 패키지 네임스페이스 |
| **결론** | **No Cloud Alpacas-specific Custom Metadata Type verified.** 이번 프로젝트는 Custom Metadata Type 미사용. |

> Recommendation / Campaign 로직에서 참조되는 `__mdt` 도 없음 — Recommendation Action 라벨은 Apex 클래스 `RecommendationActionLabels` (하드코딩/상수)로 처리.

---

## 2. Custom Setting

| | 내용 |
|---|---|
| **Org Actual** | Cloud Alpacas 팀 생성 Custom Setting **1개: `DART_Setting__c`** |
| 데모 Custom Setting | `ers_datatableConfig__c` (`CreatedBy = Chanyeon Kim`, 패키지 `datatable` v4.3.7) — 팀 아님 |

### 2.1 `DART_Setting__c` — Hierarchy Custom Setting

| 항목 | 값 |
|---|---|
| API Name | `DART_Setting__c` |
| Label | DART 설정 |
| Type | **Hierarchy** (`<customSettingsType>Hierarchy</customSettingsType>`) |
| Visibility | Public |
| Description (Org) | "OpenDART API 설정 (인증키 등)" |
| CreatedBy | Aaron Choi (2026-08-28) |
| 필드 | `Api_Key__c` (Text) — OpenDART API 인증키 (`crtfc_key`) |
| 사용처 (Apex) | **`DartService`** — `DART_Setting__c.getOrgDefaults()` 로 org 기본값 조회 → `apiKey()` 로 사용. 호출: `https://opendart.fss.or.kr/api/company.json?crtfc_key=...`, `fnlttSinglAcnt.json?crtfc_key=...` |
| 사용처 (Flow) | 간접 — `DART Lead 전환 AI매칭`, `DART 승인 보강` 이 `DartEnrichmentInvocable` / `DartMatchInvocable` 통해 `DartService` 호출 |
| 의존성 | RemoteSiteSetting `opendart_fss` (`https://opendart.fss.or.kr`, 활성) 필요 |
| 주의 | 인증키가 Custom Setting 평문 저장 — 배포/공유 시 값 노출 주의. Named Credential 로 이전 검토 권장 (`Verification Required`) |

> **주의:** 초판 `03_SYSTEM_ORG.md` 는 `DART_Setting__c` 를 Custom Object 로 잘못 분류했다. `getOrgDefaults()` 사용과 `object-meta.xml` 의 `customSettingsType` 로 **Hierarchy Custom Setting** 확정. Rev.2 정정 반영됨.

---

## 3. 참고 — Custom Setting 이 아닌 유사 구성

이번 프로젝트에서 "설정값 저장"에 쓰인 다른 패턴:

| 대상 | 실제 구현 방식 | 비고 |
|---|---|---|
| Recommendation Action 라벨/색상 | Apex `RecommendationActionLabels` (상수) | Custom Metadata 아님 |
| Agent API endpoint/auth | **NamedCredential `CA_Agent_API`** + ExternalCredential `CA_Agent_API_Cred` (`https://api.salesforce.com`) | Custom Setting 아님 |
| DART 기업 코드 ↔ 종목 매핑 | **Custom Object `DART_Corp_Mapping__c`** (레코드 데이터, `Corp_Code__c`/`Corp_Name__c`/`Corp_Name_Eng__c`/`Stock_Code__c`) | Custom Metadata 아님 — 런타임 데이터 |
| PRM 매출 목표 | **Custom Object `PRM_Revenue_Target__c`** (`Target_Amount__c`) | Custom Metadata 아님 |

---

## 4. Known Limitations / Verification Required

| 항목 | 상태 |
|---|---|
| `DART_Setting__c` 실제 레코드 값 (Org Default) | 조회 안 함 (인증키 노출 방지) — 존재 여부만 확인 |
| List-type Custom Setting | 팀 생성분 없음으로 확인 |
| `DART_Setting__c` → Named Credential 이전 권장 여부 | 팀 결정 필요 |
| Protected vs Public Custom Metadata | 해당 없음 (Custom Metadata Type 미사용) |
