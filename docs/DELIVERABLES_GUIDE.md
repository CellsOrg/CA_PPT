# CloudAlpacas 9/2 산출물 작성 가이드 (Claude Code 참고용)

> 이 문서는 `cloudalpacas-org-inventory` 프로젝트에서 산출물을 작성할 때
> **형식과 기준을 통일**하기 위한 가이드입니다.
> Salesforce가 제시한 공식 산출물 포맷을 Cloud Alpacas 프로젝트에 맞게 재정리한 것입니다.

---

## 0. 작업 원칙 (반드시 지킬 것)

1. **Source of Truth는 실제 Org 상태**입니다. 기존 `03_SYSTEM.md`, `CloudAlpacas_P2_Object_Field_Design.xlsx`,
   Google Drive 문서는 참고만 하고, 실제 존재 여부/구조 판단의 기준으로 쓰지 않습니다.
   (이유: 개발 진행 중 반영이 안 된 부분이 많음 — 문서가 아니라 Org가 최신 상태)
2. Salesforce **표준 기능 자체는 제외**하고, Cloud Alpacas 프로젝트에서 **추가/커스터마이징한 것만** 정리합니다.
3. 이번 작업은 **조회(retrieve) + 문서화만** 수행합니다. Org에 대한 배포/수정/삭제는 절대 하지 않습니다.
4. 없는 것을 억지로 만들지 않습니다. (예: Custom Metadata Type이 없으면 "해당 없음"으로 명시)
5. 모든 산출물은 `docs/deliverables/` 폴더 하위에 markdown으로 먼저 작성 → 이후 Sara가 PPT/Word로 옮깁니다.
   (Claude Code는 pptx/docx 변환까지 할 필요 없음. markdown 초안만 완성도 있게 작성)

---

## 1. 작업 순서 (우선순위)

Org 조회만으로 완성 가능한 것 먼저, 사람(팀원) 응답이 필요한 것은 병렬로 별도 진행합니다.

| 순서 | 산출물 | 의존성 | 목표 시간 |
|---|---|---|---|
| 1 | ERD | Org metadata inventory | 30분~1시간 |
| 2 | 권한 설정 현황표 | Org metadata inventory | 1시간 |
| 3 | Custom Metadata 정보 | Org metadata inventory | 30분 |
| 4 | 아키텍처 다이어그램 | ERD 완료 후 | - |
| 5 | 프로세스 흐름도 | 04_DEMO.md 시나리오 | - |
| 6 | 요구사항 정의서 | **팀원 Slack 응답 취합 (병렬 진행, 별도 트랙)** | - |
| 7 | 프로젝트 기획서 | 1~6 전체 요약 | 마지막 |

> ⚠️ 6번(요구사항 정의서)은 팀원 응답을 기다려야 하므로, Sara가 다른 항목을 작업하는 동안
> 별도로 응답을 취합하는 트랙으로 진행합니다. 이 문서의 작업 순서에 넣지 않고 병행합니다.

---

## 2. 산출물별 상세 스펙

### ① ERD (Object ERD)

**목적**: 업무를 구현하는 Salesforce Object(Standard + Custom)와 관계를 시각화하여 데이터 중복·누락을 방지하고 설계 기준을 합의하기 위함.

**작성 규칙**:
- 각 Object의 **Label + API Name**을 함께 표기, Standard/Custom 구분 (Custom은 별도 색상/표시)
- 핵심 필드만 일부 표시: Record Id, 상태 필드, 관계 필드(Lookup/Master-Detail), 필수값
- 관계는 **1:1 / 1:N / N:M**을 구분하고, Junction Object 여부, Lookup vs Master-Detail 구분
- 관계선 양 끝에 Cardinality 표시, 부모-자식 방향 명확히

**작성 가이드**:
- 프로세스 흐름 순서대로 핵심 Object를 왼쪽 → 오른쪽 배치 (예: Lead → Account → Opportunity → Quote)
- Object가 많으면 **전체 ERD (Master) + Scene별 상세 ERD**로 분리
  - Cloud Alpacas 기준 Scene 예시: Fan 가입/육성, Fan 세그먼트/추천, B2B 스폰서십(Lead→Opportunity→Quote), Campaign
- Mermaid ERD로 작성 → PNG/PDF export

**산출 파일**: `docs/deliverables/01_ERD.md` (Mermaid 코드 포함)

---

### ② 권한 설정 현황표

**목적**: 현재 Org의 Permission Set / Profile 구조를 한눈에 파악.

**작성 항목**: Permission Set/Profile 이름 / 대상 Object / 부여 권한(CRUD) / 용도 / 사용 대상(User)

**작성 가이드**:
- `FRM_Manager_Access`, `Fan_App_API_Access`, `FanQuiz Profile` (Guest User) 등 실제 존재하는 것만 기준
- Object별로 표를 나누기보다, Permission Set/Profile 단위로 한 행씩 정리하고 관련 Object를 함께 표기

**산출 파일**: `docs/deliverables/02_PERMISSIONS.md`

---

### ③ Custom Metadata 정보

**목적**: 실제 사용 중인 Custom Metadata Type / Custom Setting 존재 여부 확인 및 문서화.

**작성 항목**: 이름 / Type(Custom Metadata Type or Custom Setting) / 용도 / 사용 위치(Flow/Apex/LWC 이름)

**작성 가이드**:
- Recommendation, Campaign 로직에서 실제 참조되는 것만 기록
- 존재하지 않으면 "해당 없음 — 이번 프로젝트는 Custom Metadata 미사용"으로 명시하고 끝낼 것 (억지로 만들지 않기)

**산출 파일**: `docs/deliverables/03_CUSTOM_METADATA.md`

---

### ④ 프로세스 흐름도 (Process Diagram)

**목적**: 현재 업무 흐름과 참여 주체(페르소나)별 역할을 시각화하여 As-Is 문제점과 Salesforce 기반 To-Be 개선 지점을 명확히 함.

**작성 규칙**:
- 페르소나별 **Swimlane** 구분 (예: 이루키(Fan), 김매니저(FRM Manager), System/Flow)
- 항목: 시작/종료 노드, 참여 주체(행) × 주요 업무 단계(열), 의사결정 조건, 업무 인계(handoff) 지점
- 흐름 방향과 도형/연결선 의미를 전체 다이어그램에서 일관되게 사용

**대상 프로세스 3개** (04_DEMO.md 시나리오 기반):
1. Fan 가입 → 데이터 축적 → Segment/Engagement 산출
2. Fan 분석 → Recommendation → Campaign/Action 실행
3. Sponsor 후보(B2B) → Fit 분석 → 영업 프로세스 (Lead → Opportunity)

**작성 가이드**:
- Flow XML을 그대로 옮기지 말고, **업무 프로세스 관점**으로 단순화
- To-Be에는 As-Is 대비 Salesforce로 자동화/통합된 지점을 명확히 표시 (예: "수기 취합 → Flow 자동 생성")

**산출 파일**: `docs/deliverables/04_PROCESS_FLOW.md` (다이어그램은 Mermaid flowchart 또는 설명 + 별도 이미지)

---

### ⑤ 시스템 아키텍처 다이어그램

**목적**: Cloud Alpacas가 사용하는 Salesforce 앱 영역과 외부 시스템 연동 구조를 한눈에 파악.

**작성 규칙**:
- Salesforce 핵심 영역을 중앙에 배치, 시스템 경계를 명확히 표시
- 외부 연동은 연동 방식을 간단히 표기 (API / 미들웨어 / 이벤트 기반 / 배치 등)
- 필요 시 Salesforce 내부는 Object 레벨까지 상세 표현 가능

**Cloud Alpacas 구조 (실제 구현 기준으로 채워야 함)**:
```
Fan App (Demo용 데이터 생성 채널)
      ↓ (연동 방식: 실제 확인 필요 — REST API? Flow? 직접 입력?)
Salesforce Platform
  ├─ Person Account / Contact (Fan)
  ├─ Order / Admission (구매/입장 데이터)
  ├─ Campaign / Quiz_Entry__c
  ├─ Recommendation Segment Dashboard
  ├─ Agentforce (VIP_Recommendation_Agent — Employee Agent)
  └─ Experience Cloud (FanQuiz LWR Site)
      ↓
Slack (VIP Alert 연동, channel C0BSDEZHUBV)
```
> 위 구조는 memory 기준 초안입니다. Claude Code가 실제 Org 조회 결과로 검증/수정할 것.

**작성 가이드**: 구현하지 않았지만 시나리오상 접점이 있는 외부 앱은 "Out of Scope"로 표기 가능.

**산출 파일**: `docs/deliverables/05_ARCHITECTURE.md`

---

### ⑥ 요구사항 정의서 (Backlog)

**목적**: 구현 범위/우선순위/담당/완료 조건을 명확히 하여 팀이 같은 기준으로 개발·검수.

**구조**: `Business Area → Process Line → Epic → User Story → Task`

**필수 항목**: Business Area / Process Line / User Story / Task / 상태(Done/진행중/예정) / 우선순위(Must/Should/Could 등 팀 기준 통일) / 담당자 / 목표 Sprint / 완료 조건

**작성 가이드**:
- 팀원에게 요청한 템플릿([Feature]/[Business Purpose]/[Salesforce]/[How it works]/[Problem & Solution]/[QA]) 응답을
  위 Backlog 구조에 매핑해서 통합
- 이미 구현된 기능은 상태를 `Done`으로 표시
- **새 요구사항을 만들지 않음** — 팀원이 준 내용만 재구조화
- QA용 테스트 데이터/절차/기대 결과가 있으면 Task에 함께 기록

**산출 파일**: `docs/deliverables/06_REQUIREMENTS.md` (팀원 응답 취합 후 별도 작업)

---

### ⑦ 프로젝트 기획서

**목적**: 프로젝트 배경, Pain Point, 목표, 범위, 기대효과를 제출용으로 요약.

**작성 가이드**: `00_STORY.md` + `01_PROJECT.md` 내용을 그대로 재구성 (새로 쓰지 않기)

**산출 파일**: `docs/deliverables/07_PROPOSAL.md`

---

## 3. Claude Code 작업 시 체크리스트

- [ ] Org 연결 상태 확인 후에만 retrieve 진행
- [ ] Custom Object/Field/Flow/LWC/Apex/Agent 목록을 `ORG_METADATA_INVENTORY.md`로 먼저 정리
- [ ] 위 인벤토리를 기준으로 ①→②→③→⑤ 순서로 문서 작성 (④, ⑥은 별도 트랙)
- [ ] 각 문서 작성 후, 기존 memory/문서와 다른 부분이 있으면 "차이점" 섹션에 별도로 기록 (판단은 Sara가 나중에)
- [ ] 기존 Cloud Alpacas 프로젝트 Org에는 어떠한 배포/수정도 하지 않음
