#!/usr/bin/env python3
# PPT_v2 — Cloud Alpacas 최종 발표 와이어프레임 (18장, from scratch).
# Mid-fidelity 레이아웃 시안 (위계 + 메시지 + 플레이스홀더), 최종 비주얼 아님.
# CH I WHY (01-05) · CH II DEMO SCENARIO 06-17 LOCKED · CH III SO WHAT (18).
# Demo 06-17 = docs/deliverables/PPT_WIREFRAME/00_WIREFRAME_GUIDE.md CHAPTER II + Demo순서.png + 04_DEMO.md 를 SoT로.
import html, pathlib

OUT = pathlib.Path(__file__).parent
def esc(s): return html.escape(str(s), quote=False)

# ---------- format map (Demo순서 "표현 방식") ----------
FMT = {
  "PPT":        ("ppt",   "PPT"),
  "DEMO VIDEO": ("video", "DEMO VIDEO"),
  "LIVE":       ("live",  "LIVE"),
  "MIX":        ("mix",   "PPT + 5s VIDEO"),
  "TBD":        ("tbd",   "FORMAT TBD"),
  "TRANSITION": ("trans", "TRANSITION"),
}
def fmt_badge(key):
    if not key: return ""
    cls, label = FMT[key][0], FMT[key][1]
    dot = '<span class="fdot"></span>' if cls in ("live", "video") else ""
    return f'<span class="fmt {cls}">{dot}{esc(label)}</span>'

# ---------- block renderers ----------
def H1(t, big=False):
    return f'<div class="blk"><span class="t">H1</span><div class="h1{" big" if big else ""}">{esc(t)}</div></div>'
def KM(t):
    return f'<div class="blk"><span class="t">KEY MSG</span><div class="km">{esc(t)}</div></div>'
def SM(t): return f'<div class="sm">{esc(t)}</div>'

def PH(tag, cap, hint="", variant="", grow=1):
    v = (" " + variant) if variant else ""
    hint_html = f'<div class="hint">{esc(hint)}</div>' if hint else ""
    flex = "none" if grow == 0 else str(grow)
    return (f'<div class="ph{v}" style="flex:{flex}"><span class="tag">{esc(tag)}</span>'
            f'<div class="cap">{esc(cap)}</div>{hint_html}</div>')

def FLOW(nodes, tight=False):
    parts = []
    for i, nd in enumerate(nodes):
        if len(nd) == 3:
            label, sub, cls = nd
            sub_html = f'<span class="n2">{esc(sub)}</span>' if sub else ""
        else:
            label, cls = nd; sub_html = ""
        parts.append(f'<div class="node {cls}">{esc(label)}{sub_html}</div>')
        if i < len(nodes) - 1:
            parts.append('<span class="arw">&rsaquo;</span>')
    return f'<div class="flowrow{" tight" if tight else ""}">{"".join(parts)}</div>'

def CARDS(items):
    cs = []
    for it in items:
        n, h = it[0], it[1]
        if len(it) >= 4:   # (n, headline, sub-headline, desc)
            sub, desc = it[2], it[3]
            sub_html = f'<div class="csub">{esc(sub)}</div>' if sub else ""
            cs.append(f'<div class="cardp big"><div class="cn">{esc(n)}</div>'
                      f'<div class="ch">{esc(h)}</div>{sub_html}'
                      f'<div class="cs">{esc(desc)}</div></div>')
        else:              # (n, headline, desc, [box])
            s = it[2]; box = it[3] if len(it) > 3 else "ICON / VISUAL"
            cs.append(f'<div class="cardp"><div class="cn">{esc(n)}</div>'
                      f'<div class="ch">{esc(h)}</div><div class="cbox">{esc(box)}</div>'
                      f'<div class="cs">{esc(s)}</div></div>')
    return f'<div class="cards">{"".join(cs)}</div>'

def DFLOW(tag, nodes, hint="", tight=False):
    hint_html = f'<div class="hint">{esc(hint)}</div>' if hint else ""
    return (f'<div class="ph diagram" style="flex:1"><span class="tag">{esc(tag)}</span>'
            f'{FLOW(nodes, tight)}{hint_html}</div>')

def ANN(k, t): return f'<div class="ann"><span class="k">{esc(k)}</span>{esc(t)}</div>'

def PIV(active):
    steps = [("p","Problem"),("i","Insight"),("a","Action"),("v","Business Value")]
    d = "".join(f'<div class="{"on" if key==active else ""}">'
                f'<div class="pk">{key.upper() if key!="v" else "VALUE"}</div>'
                f'<div class="pv">{lab}</div></div>' for key,lab in steps)
    return f'<div class="piv">{d}</div>'

def PERSONA(name, role):
    return (f'<div class="persona"><span class="av">FACE</span>'
            f'<b>{esc(name)}</b><span>{esc(role)}</span></div>')

def CHIPS(items):
    return '<div class="chips">' + "".join(
        f'<span class="chip2 {c}">{esc(l)}</span>' for l,c in items) + '</div>'

def WVCARD(word, tagline, impl, value):
    chips = "".join(f'<span class="chip2">{esc(x)}</span>' for x in impl)
    return (f'<div class="cardp wv"><div>'
            f'<div class="wvw">{esc(word)}</div>'
            f'<div class="wvt">{esc(tagline)}</div></div>'
            f'<div class="chips" style="justify-content:center">{chips}</div>'
            f'<div class="wvv">{esc(value)}</div></div>')

def SPLIT(lt, litems, rt, ritems, mid):
    li = "".join(f'<div class="chip2 b2c">{esc(x)}</div>' for x in litems)
    ri = "".join(f'<div class="chip2 b2b">{esc(x)}</div>' for x in ritems)
    return (f'<div class="split"><div class="half l"><div class="htitle">{esc(lt)}</div>'
            f'<div class="chips">{li}</div></div>'
            f'<div class="half r"><div class="htitle">{esc(rt)}</div>'
            f'<div class="chips">{ri}</div></div><div class="mid">{esc(mid)}</div></div>')

def ROW(cells, grow=True):
    inner = ""
    for c in cells:
        w, content = c if isinstance(c, tuple) else (1, c)
        if isinstance(content, list):
            content = f'<div class="col" style="flex:{w}">' + "".join(content) + "</div>"
        elif 'class="ph' in content:
            content = content.replace('style="flex:1"', f'style="flex:{w}"', 1)
        else:
            content = f'<div class="col" style="flex:{w}">{content}</div>'
        inner += content
    return f'<div class="row{" grow" if grow else ""}">{inner}</div>'

# ---------- demo page builder (06-17) ----------
def DEMO(question, fmt_key, zone, show_cap, show_hint, features,
         ai_role, bvalue, piv, say, screen, persona=None, dur="01:30"):
    cls = FMT[fmt_key][0]
    if cls == "video":
        main = (f'<div class="ph video" style="flex:7"><div class="play"></div>'
                f'<span class="tag">DEMO VIDEO — 재생 영역 (화면의 중심)</span>'
                f'<div class="cap">{esc(show_cap)}</div><div class="hint">{esc(show_hint)}</div>'
                f'<div class="scrub">&#9654;  00:00 &nbsp;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;  {esc(dur)}</div></div>')
    elif cls == "live":
        main = (f'<div class="ph live" style="flex:7">'
                f'<span class="livebadge"><span class="fdot"></span>LIVE · 발표 현장 실행 (백업 영상 준비)</span>'
                f'<span class="tag">실제 화면 (Salesforce / Slack) — 현장 시연</span>'
                f'<div class="cap">{esc(show_cap)}</div><div class="hint">{esc(show_hint)}</div></div>')
    elif cls == "mix":
        main = (f'<div class="ph img" style="flex:7"><span class="tag">PPT WIREFRAME &nbsp;+&nbsp; 약 5초 임베드 영상</span>'
                f'<div class="cap">{esc(show_cap)}</div><div class="hint">{esc(show_hint)}</div>'
                f'<div class="inset">&#9654; 5s embedded video</div></div>')
    elif cls == "tbd":
        main = (f'<div class="ph tbdbox" style="flex:7"><span class="tag">[ FORMAT TBD — 표현 방식 미정 ]</span>'
                f'<div class="cap">{esc(show_cap)}</div>'
                f'<div class="hint">{esc(show_hint)}<br>PPT / DEMO VIDEO / LIVE 중 미선택 — 팀 확정 필요</div></div>')
    else:
        main = (f'<div class="ph img" style="flex:7"><span class="tag">PPT — Screenshot / Wireframe</span>'
                f'<div class="cap">{esc(show_cap)}</div><div class="hint">{esc(show_hint)}</div></div>')
    info = (CHIPS([(f, zone) for f in features])
            + f'<div class="meta"><b>AI 역할</b>{esc(ai_role)}</div>'
            + f'<div class="meta"><b>Value</b>{esc(bvalue)}</div>'
            + PIV(piv)
            + ANN("발표자 — 말할 것", say)
            + ANN("화면 — 보여줄 것", screen))
    blocks = []
    if persona: blocks.append(PERSONA(*persona))
    blocks.append(H1(question))
    blocks.append(f'<div class="row grow">{main}<div class="col" style="flex:3">{info}</div></div>')
    return blocks

# ---------- page shell ----------
def page(fname, chapter_cls, chapter_label, role, num, blocks, fmt=None):
    body = "\n".join(blocks)
    doc = f'''<!doctype html><html lang="ko"><head><meta charset="utf-8">
<link rel="stylesheet" href="wf.css"></head>
<body><div class="slide {chapter_cls}">
  <div class="wtop"><div class="lft"><span class="ch">{esc(chapter_label)}</span>
    <span class="role">{esc(role)}</span></div>
    <div class="rgt">{fmt_badge(fmt)}<span class="wf-note">WIREFRAME · 레이아웃 시안 (최종 비주얼 아님)</span></div></div>
  <div class="body">
{body}
  </div>
  <div class="wfoot">Cloud Alpacas · Final Presentation · PPT_v2 Storyboard</div>
  <div class="wn">{esc(num)} / 19</div>
</div></body></html>'''
    (OUT / fname).write_text(doc, encoding="utf-8")

# ============================================================ SLIDES
S = []
def slide(*a): S.append(a)

C1 =("c1", "CHAPTER I · WHY")
C2 =("c2", "CHAPTER II · DEMO SCENARIO — B2C")
C2B=("c2b","CHAPTER II · DEMO SCENARIO — B2B")
C3 =("c4", "CHAPTER III · SO WHAT")

# ======================= CHAPTER I — WHY (01-05) =======================

# ---- 01 COVER
slide("01_cover.png", *C1, "01 · Cover", "01", [
  '<div class="fill center" style="gap:34px">',
  PH("LOGO / WORDMARK", "CLOUD ALPACAS", "심플한 로고 타이포. 배경 장식 최소. 마스코트 없음.", variant="logo", grow=0),
  H1("FROM FAN DATA TO REVENUE.", big=True),
  SM("Cellsforce · Cloud Alpacas Fan Relationship Management Team   |   Final Presentation"),
  ANN("디자인 노트", "표지는 타이포 중심. 대형 타이틀 1문장 + 팀 1줄. 이미지·차트·마스코트·부제 설명문 없음."),
  '</div>',
])

# ---- 02 BUSINESS QUESTION  (WE NOTICED)
slide("02_business_question.png", *C1, "02 · Business Question", "02", [
  H1('"한국에서 가장 인기 있는 스포츠 중 하나인 야구. 그런데 왜 구단은 적자인가?"'),
  KM("팬이 는다고 구단의 지속 가능성이 따라오지 않는다."),
  ROW([
    (1, PH("CHART — 팬 수", "Fan Base ↑ (우상향)", "방향만. 실측/가짜 수치 금지.", variant="chart")),
    (1, PH("CHART — 구단 매출", "Revenue ↔ / ↓ (정체·적자)", "티켓·멤버십·굿즈만으로는 간극.", variant="chart")),
  ]),
  PIV("p"),
  ANN("발표자 포인트", "한 개의 큰 질문으로 시작한다. 두 흐름의 '엇갈림'이 핵심 — 숫자보다 방향. 시장 통계·재무 수치 금지."),
])

# ---- 03 WHAT WE SAW  (WE NOTICED)
slide("03_what_we_saw.png", *C1, "03 · What We Saw", "03", [
  H1("Salesforce 도입 전, Cloud Alpacas의 3가지 문제"),
  CARDS([
    ("01", "DATA IS FRAGMENTED", "팬 데이터가 흩어져 있다 — 팬은 안 보이고 데이터만 보인다",
     "티켓 · 굿즈 · 멤버십 · 앱 · 문의가 서로 다른 시스템에 존재한다."),
    ("02", "DATA DOESN'T BECOME ACTION", "데이터는 많지만 액션이 없다 — 이해해도 다음 행동으로 안 이어진다",
     "세분화 · 타이밍 · 우선순위가 없어 결국 모든 팬에게 같은 이벤트 · 쿠폰 · 메시지를 보낸다."),
    ("03", "FAN VALUE DOESN'T REACH B2B", "팬덤의 가치가 기업의 기회로 닿지 않는다 — 어떤 기업이 우리 팬덤과 맞는지 판단할 근거가 없다",
     "팬의 연령 · 성별 · Engagement · 구매 특성을 알아도, 파트너 발굴 · Fit 검증 · 영업 전환 체계가 없다."),
  ]),
  ANN("디자인 노트", "카드 위계 = 큰 영문 라벨 / 짧은 국문 Headline·Sub / 1줄 설명. 4개째 pain·기능 언급·해법 미리보기 금지. 좌측 아이콘 그룹(퍼즐·확성기·끊긴 다리) 선택."),
])

# ---- 04 OUR APPROACH  (WE DECIDED)
slide("04_our_approach.png", *C1, "04 · Our Approach", "04", [
  H1("데이터가 Insight에서 멈추지 않고 Action으로, 다시 Revenue로 연결된다"),
  SM("팬에서 출발한다. 고객을 이해한다. 인사이트를 액션에 연결한다. 그 액션을 매출로 확장한다."),
  '<div class="ph diagram" style="flex:1;align-items:stretch;justify-content:center;gap:16px;padding:30px 44px">',
  '<span class="tag" style="align-self:center">DIAGRAM — 하나로 연결된 Customer 360 여정 (슬라이드의 핵심 비주얼)</span>',
  FLOW([("Fan Activity","","b2c"),("Fan 360","","b2c"),("Fan Insight","","b2c"),
        ("Partner Matching","","b2b"),("Sponsorship Sales","","b2b")], tight=True),
  '<div class="conn">단계 사이를 <b>Salesforce · Flow · Agentforce · Slack</b> 이 자동으로 연결 (사람이 수작업으로 잇지 않는다)</div>',
  '<div style="border-top:2px dashed var(--dash);margin:2px 0"></div>',
  FLOW([("DATA","","hero"),("INSIGHT","","hero"),("ACTION","","hero"),("REVENUE","","hero")], tight=True),
  '</div>',
  PIV("i"),
  ANN("디자인 노트", "중앙에 하나의 큰 여정. 상단=업무 흐름(B2C 파랑→B2B 초록), 하단=DATA→INSIGHT→ACTION→REVENUE. Object 목록·빌드 수치·5레이어 아키텍처 금지."),
])

# ---- 05 HOW WE BUILT IT  (WE DECIDED)
slide("05_how_we_built_it.png", *C1, "05 · How We Built It", "05", [
  H1("우리는 기능부터 시작하지 않았다"),
  KM("Object를 먼저 만들거나 Flow부터 짜지 않았다. Business 문제에서 시작해, 필요한 만큼만 Salesforce로 구현했다."),
  '<div class="ph diagram" style="flex:1;align-items:center;justify-content:center;gap:20px;padding:34px 50px">'
    '<span class="tag">DIAGRAM — 만든 순서 = 방법론 (슬라이드의 핵심 비주얼)</span>'
    + FLOW([("Business Problem","",""),("Customer / Data Model","",""),("Salesforce Standard","",""),
            ("Flow / Apex / LWC","",""),("Agentforce","",""),("Business Action","","hero")], tight=True)
    + '<div class="conn">Business → Problem → Persona → Story → Domain → Workflow → Salesforce → Demo &nbsp;·&nbsp; 30+ 설계 결정을 ADR(05_DECISIONS)로 기록</div>'
    + '</div>',
  '<div class="col" style="flex:none;gap:10px">'
    + SM("Cellsforce · Feature Owner — PM 1명 + Owner 4명, 각자 자기 구간을 Requirement부터 QA까지 (02_TEAM_GUIDE §10~§12)")
    + CHIPS([("Sara · Fan 360 / Insight","b2c"),("혜준 · Lead","b2b"),("아론 · Account·Contact","b2b"),
             ("은영 · Opportunity","b2b"),("승우 · Product·Quote·Campaign","b2b")])
    + '</div>',
  PIV("i"),
  ANN("디자인 노트", "중앙 세로(또는 계단형) 흐름 + 하단 얇은 팀 스트립 1줄. 풀 프로필 슬라이드·개인 사진·자동차 비유·빌드 수치 자랑 금지. B2C=파랑 / B2B=초록 색 구분이 여기서 시작됨을 암시."),
])

# ======================= CHAPTER II — DEMO (06-17, 12장 LOCKED) =======================

# ---- 06 DEMO MAP
slide("06_demo_map.png", *C2, "06 · Demo Map", "06", [
  H1("From Fan Action to Sponsorship Revenue"),
  KM("앞으로 보게 될 Demo의 전체 지도 — 10초 안에 이해되도록."),
  DFLOW("DIAGRAM — Demo Map (가로 대형, Fan Insight에서 파랑→초록 전환)", [
    ("Fan","QR 참여","b2c"),("Fan 360","팬 상태","b2c"),("Fan Insight","기회 발견 · Bridge","b2c"),
    ("Partner Matching","어떤 기업이 맞는가","b2b"),("Lead","영업 대상","b2b"),("Opportunity","딜","b2b"),
    ("AI Sales","가속","b2b"),("Closed Won","매출","b2b"),
  ], "B2C(파랑) 3단계 → Fan Insight(연결점) → B2B(초록) 5단계.", tight=True),
  ANN("발표자 포인트", "Demo 목차 역할. 'Business Opportunity'라는 표현은 쓰지 않는다 — Partner Matching. Fan Insight가 B2C의 마지막이자 B2B의 출발점. 8단계 초과 금지."),
])

# ---- 07 LIVE EVENT — Game Day
slide("07_live_event.png", *C2, "07 · Live Event — Game Day (Fan Activity)", "07", [
  '<div class="ph dark" style="flex:1;gap:14px">',
  '<span class="tag">LIVE SCOREBOARD MOCK — 실제 전광판 화면처럼</span>',
  '<div class="cap" style="font-size:26px">CLOUD ALPACAS &nbsp;·&nbsp; GAME DAY LIVE</div>',
  '<div class="cap" style="font-size:19px;color:#cdd3da">&#9918; 7회말 경기 진행 중</div>',
  '<div class="cap" style="font-size:22px;color:#FFD9B4">🎁 FAN EVENT OPEN — "문태양 선수 퀴즈에 참여하세요"</div>',
  '<div class="ph qr" style="flex:none;width:150px;height:150px;background:#fff;color:#8a94a3;font-weight:800;font-size:12px;display:flex;align-items:center;justify-content:center;border-style:solid">[ QR CODE ]</div>',
  '<div class="hint">설명문 금지. 전광판 그래픽 + 실물 QR. 발표자가 관객에게 직접 참여 유도.</div>',
  '</div>',
  '<div class="row" style="flex:0 0 auto;justify-content:center">',
  FLOW([("관객 QR 참여","",""),("Quiz Entry","FanQuiz Site",""),("Fan Activity","",""),
        ("Salesforce","저장",""),("Fan 360","연결","")], tight=True),
  '</div>',
  ANN("발표자 — 말할 것", "“지금 여러분은 Cloud Alpacas 경기장의 관객입니다. 전광판에 이벤트가 떴습니다. QR을 찍고 참여해주세요.” — 기능 소개가 아니라 ‘지금 실제로 팬 데이터가 만들어지는 중’ 이라는 느낌."),
  ANN("화면 — 보여줄 것 / 주의", "FanQuiz Experience Site (liveFanQuizEntry LWC). 하단 띠 = 참여가 CRM 데이터가 된다는 개념도. Campaign 연동은 검증된 경우에만 Campaign Member 생성 설명. 당첨자 추첨은 마무리(18)에서."),
], "LIVE")

# ---- 08 · S1 · FAN
slide("08_s1_fan.png", *C2, "08 · S1 · FAN — B2C Fan Management", "08", DEMO(
  question="우리 팬은 누구인가?",
  fmt_key="PPT", zone="b2c",
  show_cap="Fan 360 → Segment → Recommendation Hub 핵심 화면",
  show_hint="실제 Fan 360 화면 캡처가 슬라이드의 55~70%. 04_DEMO Scene 2 앞부분.",
  features=["Fan 360","Segment","Recommendation Hub"],
  ai_role="팬 이해 지원", bvalue="Fan Understanding", piv="i",
  say="팬 데이터가 분산돼 개별 팬을 입체적으로 이해하기 어려웠다. Person Account를 Fan 360의 중심에 놓고, 팬을 3개 축(생애주기·Engagement·Fan Value)으로 본다. 한 화면에서 팬이 보인다.",
  screen="Fan Profile / Fan 360 Dashboard (LWC). Segment · Engagement Score · Fan Value Tier · 구매 · 관람 · Timeline.",
  persona=("김매니저","FRM Manager"),
), "PPT")

# ---- 09 · S2 · ACTIVATE
slide("09_s2_activate.png", *C2, "09 · S2 · ACTIVATE — B2C Marketing", "09", DEMO(
  question="각 팬에게 어떻게 다르게 행동할까?",
  fmt_key="DEMO VIDEO", zone="b2c", dur="01:30",
  show_cap="Recommendation Hub → 우선 대응 Segment → 이루키 → Fan 360 확인 → AI 개인화 메시지 생성 → 검토 → 발송 → Fan Insight",
  show_hint="영상 재생 영역이 화면의 중심. 04_DEMO 데모 영상 ① (80~90초). 영상 끝에서 20·30대 여성 팬층 확인.",
  features=["AI Personalized Message"],
  ai_role="Personalize", bvalue="Personalized Fan Engagement", piv="a",
  say="팬별 특성을 반영한 메시지를 담당자가 일일이 쓰기 어려웠다. AI가 초안을 만들고 담당자가 검토·승인 후 발송한다. 생성 결과는 Recommendations__c 레코드로 남는다 — Human-in-the-loop.",
  screen="recommendationReviewPanel + Prompt Fan_Personalized_Message. 미측정 반응률·전환율 금지.",
  persona=("김매니저","FRM Manager"),
), "DEMO VIDEO")

# ---- 10 · Fan Insight — B2C → B2B Bridge
slide("10_fan_insight_bridge.png", *C2, "10 · Fan Insight — B2C → B2B Bridge ⭐", "10", [
  H1("B2C에서 쌓인 팬 데이터가, 여기서 기업의 기회가 된다"),
  KM("Fan Insight는 B2B가 아니라 B2C의 마지막 단계 — 두 세계를 잇는 Bridge."),
  SPLIT("B2C (여기까지)", ["Fan Experience","Fan 360","Recommendation / Personalization"],
        "B2B (여기부터)", ["Partner Matching","Sponsorship Sales"],
        "FAN INSIGHT"),
  ANN("전환 디자인 (가장 중요)", "Demo 전체의 turning point. 이 슬라이드에서 색·커넥터가 파랑(B2C) → 초록(B2B)으로 전환되고, 발표 톤도 여기서 바뀐다. 다른 Demo 슬라이드보다 시각적으로 강하게."),
  ANN("화면 — 보여줄 것", "개념 다이어그램 (FAN DATA ↓ FAN INSIGHT ↓ PARTNER OPPORTUNITY). 스크린샷 없이 전환을 선언하는 슬라이드. Fan Insight = Report/Dashboard 기반. B2B 상세·기능 목록 금지."),
], "TRANSITION")

# ---- 11 · S3 · CONNECT
slide("11_s3_connect.png", *C2B, "11 · S3 · CONNECT — B2C → B2B Sponsorship", "11", DEMO(
  question="팬 데이터를 어떻게 B2B 영업 기회로 연결할까?",
  fmt_key="LIVE", zone="b2b",
  show_cap="Monthly Fan Insight Letter 확인 → 이매니저가 Slack Agent에게 분석 요청 → 20·30대 여성 팬 증가 등을 근거로 Sponsorship 방향 탐색",
  show_hint="현장 시연. 04_DEMO Scene 3. 10초 내 미도착 시 동일 시나리오 백업 영상.",
  features=["Monthly Fan Insight Letter","Slack Agent"],
  ai_role="Analyze & Discover", bvalue="B2C Data → B2B Sales Opportunity", piv="i",
  say="B2C에서 발견한 인사이트가 보고서로 끝났다. 이제 이매니저의 Slack으로 전달되어 실제 B2B 영업을 시작한다 — B2C팀·B2B팀이 하나의 Revenue Process로 연결된다.",
  screen="Fan Insight Letter (Report/Dashboard 기반) + Flow → Slack. 김매니저 → 이매니저 handoff. Slack 채널 ID 화면 노출 금지.",
  persona=("김매니저 → 이매니저","FRM → Sponsorship Sales"),
), "LIVE")

# ---- 12 · S4 · Partner Matching
slide("12_s4_partner_matching.png", *C2B, "12 · S4 · Partner Matching", "12", DEMO(
  question="이 팬덤과 가장 잘 맞는 기업은 누구인가? — 왜 이 기업인가?",
  fmt_key="TBD", zone="b2b",
  show_cap="팬층 특성(연령·성별·Engagement·구매) ↔ 기업 후보 매칭 → Fit 근거(Recommendation Reason) → d'Alba",
  show_hint="기업 데이터 = OpenDART API 조회 (기업 DB는 Salesforce Object 아님, D-020). Agentforce Matching → Top 후보 + Reason. 00_STORY §8 / 04_DEMO Scene 4. ※ Demo순서 이미지에 S4 열 없음(S3→S5) — 포함 여부·표현 방식 팀 확정 필요.",
  features=["Fan Fit","Segment Match","Recommendation Reason"],
  ai_role="Match & Explain", bvalue="데이터 기반 파트너 발굴", piv="i",
  say="“d'Alba는 먼저 Cloud Alpacas 팬덤과 높은 적합도를 보여 후보가 됐습니다.” — AI는 정답이 아니라 ‘왜 이 기업인가’를 설명한다. 그리고 Fit이 높다고 곧바로 계약 가능성이 높은 건 아니다.",
  screen="Fan Fit / Segment Match (팬덤-기업 적합도, Agentforce 산출) ≠ Lead Score (실제 계약 가능성, 영업 활동 기반) — 다음(S5)에서 이어짐. 100개 기업 DB를 Object로 표현 금지.",
  persona=("이매니저","Sponsorship Sales Manager"),
), "TBD")

# ---- 13 · S5 · PIPELINE
slide("13_s5_pipeline.png", *C2B, "13 · S5 · PIPELINE — Dashboard → Lead → Account → OPP", "13", DEMO(
  question="Sponsor 후보를 어떻게 실제 Deal로 발전시킬까?",
  fmt_key="MIX", zone="b2b",
  show_cap="Tableau Next Dashboard → Lead / Lead Score → Lead Convert → Account·Contact → AI로 부족한 Account 필드 자동 보완 → d'Alba OPP 진입",
  show_hint="PPT 위에 약 5초 임베드 영상. 04_DEMO Scene 4. Tableau 수치는 검증 완료 전까지 노출하지 않는다.",
  features=["Tableau Next","Lead Score","Account AI Enrichment"],
  ai_role="Analyze / Score / Enrich", bvalue="Sales Prioritization / Productivity / Data Quality", piv="a",
  say="유망 Sponsor 판단부터 Account 정보 보완까지 수작업이 많았다. 우선순위는 Lead Score로, 빈 정보는 AI가 공시 데이터(DART Open API)로 채운다. ‘분석은 Tableau, 실행은 Salesforce’로 역할을 나눴다.",
  screen="PRM/Tableau Next Dashboard · Lead_Score__c…Final_Lead_Score__c · Prompt CA_Lead_AI_Summary · LeadConvertPartnerContact. Fit=계약가능성으로 표현 금지.",
  persona=("이매니저 / d'Alba","Sponsorship Sales"),
), "MIX")

# ---- 14 · S6 · UNDERSTAND
slide("14_s6_understand.png", *C2B, "14 · S6 · UNDERSTAND — OPP · Needs Analysis", "14", DEMO(
  question="고객은 무엇을 말했는가?",
  fmt_key="DEMO VIDEO", zone="b2b", dur="03:00",
  show_cap="고객 Meeting / Activity → 기록 → AI 분석 → Summary / Signal (긍정·위험)",
  show_hint="영상 재생 영역이 화면의 중심. 04_DEMO Scene 6 (Zoom 연동, 대화 45~50초 고정). 백업 영상 필수.",
  features=["Activity Intelligence"],
  ai_role="Understand", bvalue="Activity 자산화", piv="i",
  say="미팅이 끝나면 담당자가 내용을 직접 정리해야 했고, 요구·위험 신호가 누락될 수 있었다. 이제 고객이 말한 요구사항과 위험 신호가 Activity에 연결되고, 다음 행동의 근거가 된다.",
  screen="Zoom → Activity 자동 기록 → Prompt CA_Offline_Meeting_* → Interaction_Intelligence__c → Interaction_Signal__c. 대화 전체 스크립트를 슬라이드에 넣지 않는다.",
  persona=("이매니저 / 김하나","Sales / d'Alba 담당자(예시)"),
), "DEMO VIDEO")

# ---- 15 · S7 · REASON
slide("15_s7_reason.png", *C2B, "15 · S7 · REASON — OPP · Proposal", "15", DEMO(
  question="그래서 무엇을 제안할까?",
  fmt_key="LIVE", zone="b2b",
  show_cap="과거 유사 사례 + 현재 d'Alba OPP + 팬 데이터 + 고객 Activity → Opportunity Agent 분석 → 제안 방향 / Package / Product + 근거",
  show_hint="현장 시연. 04_DEMO Scene 7 (Opportunity Agent). 백업 영상 준비.",
  features=["Opportunity Agent"],
  ai_role="Reason", bvalue="Context 기반 Sales Decision Support", piv="a",
  say="담당자가 과거 사례·현재 Deal·팬 데이터·고객 Activity를 직접 찾아 종합해야 했다. Agent가 컨텍스트를 모아 제안 방향을 근거와 함께 제시한다. 조회·추천은 즉시, 고객 일정·계약 조건 변경은 담당자 확인 후.",
  screen="Opportunity Agent (deal / proposal / negotiation / stage_guidance). Agent가 임의로 쓰기 작업을 수행하는 것처럼 표현 금지.",
  persona=("이매니저 / d'Alba","Sponsorship Sales"),
), "LIVE")

# ---- 16 · S8 · ACT
slide("16_s8_act.png", *C2B, "16 · S8 · ACT — OPP · Negotiation", "16", DEMO(
  question="고객의 변화에 어떻게 대응할까?",
  fmt_key="PPT", zone="b2b",
  show_cap="새 고객 Activity / 상황 → AI 선제 분석 → Negotiation 대응 / 수정안 + 판단 근거 → Closed Won",
  show_hint="04_DEMO Scene 8. 협상 성사 시 Closed Won으로 전환.",
  features=["Proactive AI","Negotiation Assistant"],
  ai_role="Act Proactively", bvalue="Proactive Selling", piv="a",
  say="고객 반응이 바뀔 때마다 담당자가 다시 상황을 분석해야 했다. AI가 변화를 먼저 감지해 수정안을 근거와 함께 제시한다. AI가 임의로 조건을 바꾸는 게 아니다 — 기존 Quote·고객 예산·할인 기준·고객 Signal을 근거로 안을 내고, 최종 결정은 담당자.",
  screen="Negotiation Assistant · Standard Quote · Negotiation Context. 협상안은 담당자 승인 후 반영. ⚠️ 금액은 발표 전 통일 (SPN-LED-BRANDDAY 3억/5.5억 상충, 04_DEMO 가격 검증).",
  persona=("이매니저 / 김하나","Sales / d'Alba 담당자(예시)"),
), "PPT")

# ---- 17 · S9 · EXPAND
slide("17_s9_expand.png", *C2B, "17 · S9 · EXPAND — Post-Sale · 1년 후", "17", DEMO(
  question="1년 후, d'Alba와의 관계를 어떻게 다음 매출로 연결할까?",
  fmt_key="TBD", zone="b2b",
  show_cap="화면에 크게 “1년 후” → d'Alba 단년 계약 종료 임박 → Partnership Plan 확인 → d'Alba Upsell Sales 고려",
  show_hint="Demo순서 이미지: 표현 방식·AI 역할·기능 모두 미정. ✅ 구현 확인(실선): Campaign Renewal RecordType · 갱신 캠페인 성과 요약 Flow · Thank You Day Campaign. 🔵 Future Scope(점선·흐리게·라벨): 장기 재계약 자동 판단 · Autonomous Upsell · 계약 후 성과 분석. 지난 시즌 성과는 ‘발표용 시뮬레이션 데이터’로 명시. 04_DEMO Scene 9 검증 조건.",
  features=["Partnership Plan (논의 필요)","Upsell (논의 필요)"],
  ai_role="미정", bvalue="Renewal / Upsell을 통한 Revenue Expansion 방향", piv="v",
  say="첫 계약은 매출엔진의 끝이 아니라 시작이다. 계약·활동 데이터가 쌓일수록 다음 재계약·업셀도 감이 아니라 데이터에서 출발한다 — 다만 여기부터는 구현한 부분과 앞으로의 방향을 구분해서 말한다.",
  screen="현재 GitHub main 기준 구현 근거가 명확한 부분만 시연. 장기 재계약 자동화를 구현된 것처럼 표현 금지.",
  persona=("이매니저 / d'Alba","Sponsorship Sales"),
), "TBD")

# ======================= CHAPTER III — SO WHAT (18-19) =======================
#  DEMO(06-17) -> 18 WHAT WE LEARNED -> 19 FROM LEARNING TO BUILDING -> (PPT OFF) -> Org LIVE -> Quiz Winner -> Q&A

# ---- 18 · WHAT WE LEARNED  (설계 판단 4개 + 중앙 Closing 메시지)
slide("18_what_we_learned.png", *C3, "18 · What We Learned", "18", [
  H1("What We Learned"),
  '<div class="cards" style="flex:none">'
    + ''.join(
        f'<div class="cardp" style="padding:20px 22px;gap:8px"><div class="cn" style="font-size:26px">{n}</div>'
        f'<div class="ch" style="font-size:19px">{h}</div><div class="cs">{d}</div></div>'
        for n, h, d in [
          ("01","STANDARD FIRST","업무 프로세스가 이미 존재하는 곳엔 Salesforce 표준을 쓴다."),
          ("02","AUTOMATE WHAT REPEATS","반복되는 비즈니스 로직은 Flow로 자동화한다."),
          ("03","CUSTOMIZE WHERE IT MATTERS","차별화된 경험·로직에만 Apex / LWC를 쓴다."),
          ("04","AI WITH HUMAN CONTROL","Agentforce는 추천·분석, Salesforce가 실행, 사람이 결정한다."),
        ])
    + '</div>',
  '<div class="fill center" style="gap:20px;justify-content:center">'
    '<div class="h1" style="text-align:center;font-size:50px;line-height:1.22;font-weight:800">'
      'We came here to learn Salesforce.<br>We leave knowing how to build with it.</div>'
    + '<div class="sm" style="text-align:center;letter-spacing:.06em">Fan Data → Customer 360 → Action → Revenue &nbsp;·&nbsp; CELLSFORCE × CLOUD ALPACAS</div>'
    + '</div>',
  ANN("디자인 노트", "핵심 = '무엇을 만들었나'가 아니라 '어떤 설계 판단을 배웠나'. 상단 얇은 principle card 4개(영문 Headline + 1줄) + 중앙 큰 Closing 메시지. 구현 수치·Object 목록·KPI·ROI·문단 금지 — 발표자가 말한다."),
])

# ---- 19 · FROM LEARNING TO BUILDING  (typography bridge — 거의 빈 화면. PPT의 마지막 장)
slide("19_from_learning_to_building.png", *C3, "19 · From Learning to Building", "19", [
  '<div class="fill center" style="gap:52px">',
  '<div class="sm" style="letter-spacing:.26em;text-transform:uppercase">From Learning to Building</div>',
  '<div class="h1" style="text-align:center;font-size:76px;line-height:1.32;font-weight:800">'
    "We didn't start with<br>Salesforce features.<br><br>"
    'We started with<br>the business.</div>',
  '</div>',
  ANN("디자인 노트", "DEMO 이후 발표의 '호흡'을 만드는 typography bridge — 정보 전달용 아님. editorial typography poster처럼 과감하게 비운다. 상단 작은 label + 중앙 두 문장이 전부. Business→Domain→Entity diagram / Architecture diagram / Object 목록 / 기술 스택 / KPI / 팀 소개 / 긴 설명 / Winner·Quiz·Q&A 내용 절대 금지. 이 슬라이드가 PPT의 마지막 장 — 이후 PPT를 끄고 Salesforce Org LIVE로 전환 → 퀴즈 당첨자 발표(실제 Org 화면) → Q&A. Winner/Quiz Result/Thank You/Q&A 슬라이드는 만들지 않는다."),
])

# ============================================================ render
for f in list(OUT.glob("[0-9][0-9]_*.html")) + list(OUT.glob("[0-9][0-9]_*.png")):
    f.unlink()
for args in S:
    fname, ccls, clabel, role, num, blocks, *rest = args
    fmt = rest[0] if rest else None
    page(fname.replace(".png", ".html"), ccls, clabel, role, num, blocks, fmt)
print(f"generated {len(S)} html slides in {OUT}")
