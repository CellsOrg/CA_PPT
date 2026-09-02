# ☁️ Cloud Alpacas

## 1. 우리가 누구고, 무엇을 만드는가

우리 팀 이름은 **Cellsforce**입니다.

우리는 **한화 이글스를 모델링한 가상의 구단 'Cloud Alpacas'**의 **Fan Relationship Management(FRM) Team**이 되어 Salesforce Customer 360을 설계합니다. 즉, 한화 이글스는 우리가 참고한 실제 모델(reference)이고, 우리가 실제로 만들고 다루는 대상은 가상의 구단 **Cloud Alpacas**입니다.

이번 프로젝트는 Salesforce 기능을 공부하는 프로젝트가 아닙니다. 실제 기업 프로젝트처럼 **Cloud Alpacas의 팬 데이터를 하나로 연결하고**, 팬을 이해하며, 적절한 시점에 가장 적합한 경험을 제공할 수 있는 **Customer 360 플랫폼**을 만드는 것이 목표입니다.

우리는 티켓 예매 시스템이나 쇼핑몰을 만드는 것이 아니라, **팬을 이해하고 성장시키는 Salesforce Customer 360**을 설계합니다.

Demo에서는 Cloud Alpacas의 FRM Manager인 **김매니저**가 Salesforce를 사용하여 신규 팬 **이루키**를 충성 팬으로 성장시키는 과정을 보여줍니다.

---

## 2. 프로젝트 목표

한화 이글스를 모델링한 Cloud Alpacas를 하나의 B2C 스포츠 기업으로 바라보고, Salesforce Customer 360을 기반으로 다음까지 실제 프로젝트처럼 수행합니다.

- Business 분석
- Customer Journey 설계
- Domain Modeling
- Data Modeling
- Salesforce Org 설계
- Demo Story
- Dummy Data

우리의 Business Goal은 다음과 같습니다.

> **신규 팬을 이해하고, 적절한 시점에 개인화된 액션을 통해 충성 팬으로 성장시키고, 장기적으로 Fan Lifetime Value를 높인다.**

모든 설계와 구현은 이 목표를 달성하기 위한 수단입니다.

---

## 3. 프로젝트 철학 (Business First)

우리는 Salesforce 기능부터 생각하지 않습니다. 항상 아래 순서를 지킵니다.

**Business → Problem → Persona → Story → Domain → Workflow → Salesforce → Demo**

Salesforce는 문제를 해결하기 위한 도구입니다. Object를 먼저 만들거나 Flow부터 구현하지 않습니다.

항상 **"왜 이것이 필요한가?"**를 먼저 설명하고, 그다음 **"Salesforce에서는 어떻게 구현하는가?"**를 설명합니다.

---

## 4. 프로젝트 세계관 (Cloud Alpacas)

**Cloud Alpacas**는 한화 이글스를 모델링한 가상의 프로야구 구단이고, **Cellsforce**는 그 구단의 **Fan Relationship Management(FRM) Team**이 되어 이 프로젝트를 수행합니다.

FRM Team의 역할은 팬 데이터를 분석하는 것이 목적이 아니라, 팬을 이해하고, 팬의 현재 상태를 파악하며, 가장 적절한 Next Best Action을 실행하여 팬이 Cloud Alpacas와 더 오래 함께하도록 돕는 것입니다.

이번 프로젝트의 주인공은 두 사람입니다.

- **김매니저** : Cloud Alpacas의 FRM Manager. Salesforce Customer 360을 사용하는 사용자(User)
- **이루키** : SNS를 통해 처음 Cloud Alpacas를 알게 된 신규 팬(Customer)

Customer 360은 이루키의 행동을 하나의 화면에서 연결하여 보여주고, 김매니저는 그 정보를 바탕으로 적절한 Action을 실행합니다.

---

## 5. 현재 프로젝트 범위 (MVP)

이번 프로젝트는 MVP(Minimum Viable Product)를 목표로 합니다. 다음 범위까지만 구현합니다.

- Salesforce Customer 360
- Fan 360 Dashboard
- Fan Profile
- Fan Timeline
- Fan Segmentation
- Recommendation (Next Best Action)
- Salesforce Flow
- Slack Notification
- Demo용 Fan App (데이터 생성 목적)

이번 프로젝트에서 **Fan App은 주인공이 아닙니다.** Fan App은 티켓 구매, 체크인, 굿즈 구매 등의 이벤트를 생성하여 Salesforce에 데이터를 전달하는 **Demo용 채널**입니다.

프로젝트의 핵심은 **Salesforce Customer 360**이며, Demo 역시 Customer 360을 중심으로 진행합니다.

Marketing Cloud, Data Cloud, Agentforce, 실제 결제 및 외부 API 연동은 이번 MVP 범위에 포함하지 않으며 Future Scope로 관리합니다.

> **업데이트 (2026-08-28)**: 발표 임박에 따라 범위를 한 번 더 좁혔습니다. 자세한 내용은 9번 섹션 참고.

새로운 아이디어가 나오더라도 MVP 범위를 벗어나면 바로 구현하지 않고 Future Scope로 기록합니다.

---

## 6. Claude 사용 원칙 ⭐⭐⭐⭐⭐

우리 팀은 모두 Salesforce 프로젝트가 처음인 **Baby Team**입니다. Claude는 항상 아래 원칙을 지킵니다.

**설명 방식**
- 어려운 용어를 먼저 사용하지 않습니다.
- Salesforce 기능보다 Business를 먼저 설명합니다.
- 새로운 개념은 반드시 예시와 비유를 함께 설명합니다.
- 하나의 개념만 설명하고 다음 단계로 넘어갑니다.
- 항상 "왜 이것을 하는가?"부터 설명합니다.
- 모르는 것을 부끄럽게 만들지 않습니다. 애매한 내용은 추측하지 말고 질문합니다.

**답변 관점**
Claude는 단순히 답을 알려주는 AI가 아니라, 항상 아래 네 가지 관점에서 함께 고민합니다.

- Salesforce Enterprise Architect
- Business Analyst
- CRM Consultant
- Product Manager

답을 바로 제시하기보다, 왜 그렇게 설계하는지 → 다른 선택지는 무엇인지 → 이번 프로젝트에서는 어떤 선택이 가장 적절한지 순서로 설명하고 추천합니다. 모든 설명은 친절하고 다정하게 합니다.

---

## 7. 문서와 프로젝트 관리 원칙 (Source of Truth)

Cloud Alpacas 프로젝트는 문서를 최소화하되, **각 문서의 역할은 명확하게 분리**합니다. 같은 내용을 여러 문서에 중복 작성하지 않습니다. 문서 간 내용이 충돌할 경우 아래 문서를 기준으로 판단합니다.

| 문서 | 역할 |
|------|------|
| `00_STORY.md` | 프로젝트가 왜 존재하는지, Business Goal, Pain Point, Persona, Story |
| `01_PROJECT.md` | Domain Model, Workflow, Backlog, 프로젝트의 전체 설계 |
| `02_TEAM_GUIDE.md` | 팀 운영 방식, GitHub Projects, Git/Slack Convention, 역할 정의 |
| `03_SYSTEM.md` | Salesforce Object, Data Model, Architecture, ERD, Flow |
| `04_DEMO.md` | Demo Story, Sample Data, Screen, 발표 시나리오 |
| `05_DECISIONS.md` | 프로젝트 전체에 영향을 주는 의사결정(ADR) 기록 |
| `HANDOFF_SESSION_SUMMARY.md` | 세션 간 인수인계용 요약 (신규, 9번 참고) |
| `AGENT_SPEC.md` | Recommendation Agent 설계 문서 (신규, P0) |

예를 들어 Business 변경은 `00_STORY.md`, Workflow 변경은 `01_PROJECT.md`, Object 변경은 `03_SYSTEM.md`, 프로젝트 정책 변경은 `05_DECISIONS.md`를 수정합니다.

**지켜야 할 원칙**

- 프로젝트 전체에 영향을 주는 변경(Object 구조, Workflow, Persona, MVP 범위 등)은 반드시 `05_DECISIONS.md`에 Decision으로 기록합니다.
- 문서는 "왜 만드는가"를 설명하고, GitHub Projects는 "오늘 무엇을 하는가"를 관리합니다. Task, Sprint, Bug, Progress는 문서가 아니라 GitHub Projects에서 관리합니다.
- 기존 문서를 함부로 수정하지 않습니다. 크게 변경해야 하는 경우 먼저 관련 문서와 충돌 여부를 확인하고, 애매한 경우 추측하지 말고 질문합니다.
- AI가 다른 제안을 하더라도 공식 문서(Source of Truth)가 우선입니다.

---

## 8. 프로젝트 구조

```text
CloudAlpacas/

├── CLAUDE.md
│
├── docs/
│   ├── 00_STORY.md
│   ├── 01_PROJECT.md
│   ├── 02_TEAM_GUIDE.md
│   ├── 03_SYSTEM.md
│   ├── 04_DEMO.md
│   ├── 05_DECISIONS.md
│   ├── HANDOFF_SESSION_SUMMARY.md
│   ├── AGENT_SPEC.md
│   │
│   ├── members/
│   │   ├── README.md
│   │   ├── 00_SARA.md
│   │   ├── 01_SEUNGWOO.md
│   │   ├── 02_EUNYEONG.md
│   │   ├── 03_HYEJUNE.md
│   │   └── 04_AARON.md
│   │
│   └── data/
│       ├── SAMPLE_DATA.md
│       └── DEMO_DATASETS.md
│
├── force-app/
│
└── README.md
```

**폴더 역할**

- **docs/** : 프로젝트의 설계 문서(Source of Truth)
- **docs/members/** : 팀원 개인 온보딩 문서
- **docs/data/** : Demo 및 Dummy Data
- **force-app/** : Salesforce Org Metadata
- **README.md** : 프로젝트 소개

---

## 9. 현재 진행 상황 (2026-08-28 기준)

발표가 임박하여 범위를 재편했습니다. 자세한 배경은 `docs/HANDOFF_SESSION_SUMMARY.md`와 `docs/05_DECISIONS.md`(D-031)를 참고하세요. 요약:

| 우선순위 | 내용 |
|---|---|
| **P0 ⭐** | Recommendation Agent — VIP Offer 1개 시나리오 E2E 성공 |
| **P1 ⭐** | 발표 참여 Event — 응모/추첨/당첨자 이메일 |
| P2 | Campaign 최소 QA (신규 기능 추가 없음) |
| P3 | UX Polish (발표에서 실제 보여줄 화면만) |
| P4 | Fan App (발표 후, 시간 남으면) |

**이번 발표에서 완전히 제외**: Case/FAQ/Knowledge, Experience Cloud 고객센터, Data Cloud, Tableau Next, Fan App 대규모 리팩토링, Campaign 신규 기능(Badge/쿠폰)

새 작업을 시작하기 전에 `docs/HANDOFF_SESSION_SUMMARY.md`를 먼저 읽고, 오늘까지의 맥락을 파악한 뒤 진행하세요.

---

## 10. 역할 분담 (임시 변경 중)

원래 원칙: **Vibe(Agentforce) = Flow/Apex 전용, Claude Code = LWC/Python/스크립팅 전용**

> **임시 변경 (2026-08-28~)**: Agentforce Vibe의 월간 할당량이 소진되어(~22일 뒤 리셋 예정), **이 프로젝트 폴더의 Claude Code가 Apex/Flow/LWC 전체를 담당**합니다. Vibe 할당량이 복구되면 원래 역할 분담으로 되돌립니다. 이 문서를 다시 열어 이 섹션이 지워졌는지 확인하세요 — 지워졌다면 역할 분담이 원상복구된 것입니다.

Flow를 Claude Code가 텍스트(XML)로 직접 다룰 때는, **Vibe처럼 시각적으로 검증할 수 없으므로 수정 후 반드시 Flow Builder 화면에서 눈으로 열어서 확인**하세요.

---

## 11. Salesforce 작업 시 필수 체크리스트 (실제로 겪은 함정들)

아래는 전부 이 프로젝트에서 실제로 겪고 확인한 문제입니다. 추측이 아니라 재발 방지용 체크리스트입니다.

- **새 커스텀 필드는 Setup UI에서 직접 생성할 것.** Tooling API, Metadata API 배포 모두 이 org에서 필드가 실제 스키마에 반영되지 않는 경우가 반복 확인됐습니다 (Draft 상태로만 남거나, FLS 없이 생성되거나, 아예 무시됨).
- **`AuraHandledException`은 생성자에 메시지를 넣어도 LWC로 전달되지 않습니다.** 반드시 `.setMessage(e.getMessage())`를 명시적으로 호출할 것. 안 하면 화면엔 항상 "알 수 없는 오류"만 뜹니다.
- **`@wire`로 호출하는 Apex 메서드는 반드시 `@AuraEnabled(cacheable=true)`.** `false`면 호출 자체가 안 되고 무한 로딩 또는 즉시 에러가 납니다. 데이터를 변경하는 메서드(저장/승인/발송 등)만 `cacheable=false` + imperative 호출로.
- **Restricted Picklist는 로컬 필드 메타에 값을 추가해도, 실제 org에 배포되지 않으면 사용 시 `INVALID_OR_NULL_FOR_RESTRICTED_PICKLIST` 에러가 납니다.** 항상 배포 후 재조회로 확인.
- **개인 웹메일 도메인(gmail.com 등)은 Salesforce에서 SPF/DKIM 인증이 구조적으로 불가능합니다.** 도메인 소유자만 설정 가능한 영역이라 Setup에서 아무리 시도해도 우회 불가. Trial org에서 실제 이메일 발송 테스트는 인증 요구가 덜 까다로운 서비스(Naver 등)로 진행.
- **Prompt Builder/Prompt Template 응답을 Flow에서 필드에 저장할 때, 전체 응답 객체가 문자열로 그대로 저장되는 함정이 있습니다.** `promptResponse=` 접두어 파싱 + HTML 태그 제거 로직 필수.
- **`doesRequireRecordChangedToMeetCriteria=true`인 트리거 Flow는 과거 데이터에 소급 적용되지 않습니다.** 마이그레이션된 데이터나 Flow 비활성 시점에 이미 조건을 만족한 레코드는 영구히 누락됩니다. 주기적으로 "예상 수치 vs 실제 수치" 대조 확인.
- **여러 화면에 걸친 상태/색상 매핑(뱃지 등)은 중복 정의되기 쉽습니다.** 가능하면 공통 클래스/상수로 단일화하고, 여의치 않으면 최소한 코드 주석으로 "이 두 곳은 동기화 필요"라고 명시.
- **알림/메시지가 언급하는 혜택은 반드시 실제 레코드(Benefits__c 등)로 뒷받침되는지 정기적으로 감사(audit)할 것.** "말은 했는데 실체가 없는" 버그는 신뢰 문제로 직결됩니다.
- **RecordType 필터를 Account 관련 모든 쿼리에 필수 적용할 것.** Phase 2(B2B) 진행 이후 Account 오브젝트에 팬(Fan)과 스폰서(B2B) 데이터가 함께 존재합니다.