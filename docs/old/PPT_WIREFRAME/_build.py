#!/usr/bin/env python3
# Generates 25 wireframe/storyboard HTML slides for the Cloud Alpacas final presentation.
# Mid-fidelity layout wireframes (hierarchy + message + placeholders), NOT final visual design.
# Demo pages 06-17 follow "Demo순서.png" + 04_DEMO.md as Source of Truth.
import html, pathlib

OUT = pathlib.Path(__file__).parent
def esc(s): return html.escape(str(s), quote=False)

# ---------- format map (Demo순서 이미지 "표현 방식") ----------
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

def BIGS(items):
    d = ""
    for it in items:
        if len(it) == 3: w, s, up = it
        else: w, s = it; up = ""
        up_html = f'<div class="up">{esc(up)}</div>' if up else ""
        d += f'<div><div class="bw">{esc(w)}</div>{up_html}<div class="bs">{esc(s)}</div></div>'
    return f'<div class="bigs">{d}</div>'

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
                f'<span class="livebadge"><span class="fdot"></span>LIVE · 발표 현장 실행</span>'
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
  <div class="wfoot">Cloud Alpacas · Final Presentation Storyboard</div>
  <div class="wn">{esc(num)} / 21</div>
</div></body></html>'''
    (OUT / fname).write_text(doc, encoding="utf-8")

# ============================================================ SLIDES
S = []
def slide(*a): S.append(a)

C1=("c1","CHAPTER I · OVERVIEW")
C2=("c2","CHAPTER II · DEMO SCENARIO — B2C")
C2B=("c2b","CHAPTER II · DEMO SCENARIO — B2B")
C3=("c3","CHAPTER III · WHAT WE LEARNED")
C4=("c4","CHAPTER IV · CONCLUSION")

# ---- 01 COVER
slide("01_cover.png", *C1, "01 · Cover", "01", [
  '<div class="fill center" style="gap:34px">',
  PH("LOGO / WORDMARK","CLOUD ALPACAS","심플한 로고 타이포. 배경 장식 최소",variant="logo",grow=0),
  H1("외부 환경에 흔들리지 않는 지속 가능한 매출 엔진", big=True),
  KM("Salesforce Customer 360 · Fan 360 → Fan Insight → Partner Matching → Sponsorship Sales"),
  SM("Cellsforce · Fan Relationship Management Team   |   Final Presentation"),
  ANN("디자인 노트","표지는 타이포 중심. 한 문장(타이틀) + 한 줄(서브) + 팀/날짜만. 이미지/차트 없음."),
  '</div>',
])

# ---- 02 BUSINESS CHALLENGE
slide("02_business_challenge.png", *C1, "02 · Business Challenge", "02", [
  H1("팬은 늘어나는데, 왜 구단의 매출은 함께 성장하지 않을까?"),
  KM("팬 성장이 곧 구단의 지속 가능성으로 이어지지 않는다."),
  ROW([
    (1, PH("CHART — 팬 수","Fan Base ↑ (우상향)","더미/실측 범위 내. 없는 수치 만들지 말 것",variant="chart")),
    (1, PH("CHART — 구단 매출","Revenue ↔ / ↓ (정체·적자)","티켓·멤버십·굿즈만으로는 간극",variant="chart")),
  ]),
  PIV("p"),
  ANN("발표자 포인트","한 개의 큰 질문으로 시작한다. 두 그래프의 '엇갈림'이 핵심 — 숫자보다 방향."),
])

# ---- 03 PAIN POINTS  (교체)
slide("03_pain_points.png", *C1, "03 · Pain Point (AS-IS)", "03", [
  H1("Salesforce 도입 전, Cloud Alpacas의 3가지 문제"),
  CARDS([
    ("01","팬 데이터가 흩어져 있다","팬의 전체 여정을 하나로 볼 수 없다",
     "티켓 · 굿즈 · 멤버십 · 참여 데이터가 서로 다른 시스템에 존재 → 팬을 통합적으로 이해하기 어렵다."),
    ("02","데이터는 많지만 ACTION이 없다","팬을 이해해도 다음 행동으로 이어지지 않는다",
     "세분화 · 분석은 가능하지만, 누구에게 무엇을 해야 할지 결정하고 실행하는 과정이 분절되어 있다."),
    ("03","팬덤의 가치를 기업의 기회로 연결할 수 없다","어떤 기업이 우리 팬덤과 맞는지 판단할 근거가 없다",
     "팬의 연령 · 성별 · Engagement · 구매 특성을 알아도, 적합한 파트너를 발굴하고 Fit을 검증해 영업 기회로 전환하는 체계가 없다."),
  ]),
  ANN("디자인 노트","각 카드 hierarchy = 큰 번호 / 짧은 Headline / 한 줄 Sub-headline / 2~3줄 설명. 긴 문단처럼 보이지 않게."),
])

# ---- 04 OUR APPROACH  (자동화된 연결 구조 강조)
slide("04_our_approach.png", *C1, "04 · Our Approach", "04", [
  H1("데이터가 Insight에서 멈추지 않고 Action으로 연결된다"),
  SM('"Data does not stop at Insight. It moves to Action."'),
  '<div class="ph diagram" style="flex:1;align-items:stretch;justify-content:center;gap:16px;padding:30px 44px">',
  '<span class="tag" style="align-self:center">DIAGRAM — Automation Flow (슬라이드의 핵심 비주얼)</span>',
  FLOW([("Fan Activity","","b2c"),("Fan 360","","b2c"),("Fan Insight","","b2c"),
        ("Recommendation / AI","","b2c"),("Manager Action","","b2c"),
        ("B2B Partner Matching","","b2b"),("Sponsorship Sales","","b2b")], tight=True),
  '<div class="conn">각 단계 사이를 <b>Salesforce · Flow · Agentforce · Slack · Data</b> 가 자동으로 연결 (사람이 수작업으로 잇지 않는다)</div>',
  '<div style="border-top:2px dashed var(--dash);margin:2px 0"></div>',
  FLOW([("DATA","","hero"),("INSIGHT","","hero"),("ACTION","","hero"),("REVENUE","","hero")], tight=True),
  '</div>',
  PIV("i"),
  ANN("디자인 노트","중앙에 하나의 큰 Automation Flow. 상단=업무 흐름, 하단=DATA→INSIGHT→ACTION→REVENUE. 단계 사이 커넥터에 Flow/AI/Slack 아이콘. 텍스트 최소."),
])

# ---- 05 PROJECT SCOPE / TEAM
slide("05_project_scope.png", *C1, "05 · Project Scope / Team", "05", [
  H1("B2C에서 시작해 B2B로 이어지는 하나의 프로젝트"),
  ROW([
    (3, PH("DIAGRAM — Scope","B2C (Fan Relationship · Fan Experience)  →  Fan Insight  →  B2B (Partner Matching · Sponsorship Sales)",
           "가운데 Fan Insight가 B2C의 마지막이자 B2B로 넘어가는 연결점",variant="diagram")),
    (2, [
      SM("Feature Owner (02_TEAM_GUIDE)"),
      CHIPS([("Sara · Fan 360 / Insight","b2c"),("혜준 · Lead","b2b"),("아론 · Account·Contact","b2b"),
             ("은영 · Opportunity","b2b"),("승우 · Product·Quote·Campaign","b2b")]),
      ANN("디자인 노트","팀은 작게. '누가 무엇을' 1줄. B2C=파랑 / B2B=초록 색 구분 시작."),
    ]),
  ]),
])

# ======================= CHAPTER II — DEMO (06-17, 12 pages) =======================

# ---- 06 DEMO MAP  (Business Opportunity → Partner Matching)
slide("06_demo_map.png", *C2, "06 · Demo Map", "06", [
  H1("From Fan Action to Sponsorship Revenue"),
  KM("앞으로 보게 될 Demo의 전체 지도 — 10초 안에 이해되도록."),
  DFLOW("DIAGRAM — Demo Map (가로 대형, Fan Insight에서 파랑→초록 전환)", [
    ("Fan","QR 참여","b2c"),("Fan 360","팬 상태","b2c"),("Fan Insight","기회 발견 · Bridge","b2c"),
    ("Partner Matching","어떤 기업이 맞는가","b2b"),("Lead","영업 대상","b2b"),("Opportunity","딜","b2b"),
    ("AI Sales","가속","b2b"),("Closed Won","매출","b2b"),
  ], "B2C(파랑) 3단계 → Fan Insight(연결점) → B2B(초록) 5단계.", tight=True),
  ANN("발표자 포인트","Demo 목차 역할. Business Opportunity라는 표현은 쓰지 않는다 — Partner Matching. Fan Insight가 B2C의 마지막이자 B2B의 출발점."),
])

# ---- 07 LIVE EVENT — Game Day / Fan Activity
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
  FLOW([("관객 QR 참여","",""),("Quiz Entry","FanQuiz Site",""),("Fan Activity","Campaign / Member",""),
        ("Salesforce","저장",""),("Fan 360","연결","")], tight=True),
  '</div>',
  ANN("발표자 — 말할 것","“지금 여러분은 Cloud Alpacas 경기장의 관객입니다. 전광판에 이벤트가 떴습니다. QR을 찍고 참여해주세요.” — 기능 소개가 아니라 ‘지금 실제로 팬 참여가 발생 중’ 이라는 느낌."),
  ANN("화면 — 보여줄 것","FanQuiz Experience Site (liveFanQuizEntry LWC). 하단 띠 = 참여가 이벤트로 끝나지 않고 CRM 데이터가 된다는 개념도. 04_DEMO Scene 1 = ‘PPT + 관객 참여’."),
], "LIVE")

# ---- 08 · S1 · FAN
slide("08_s1_fan.png", *C2, "08 · S1 · FAN — B2C Fan Management", "08", DEMO(
  question="우리 팬은 누구인가?",
  fmt_key="PPT", zone="b2c",
  show_cap="Fan 360 → Segment → Recommendation Hub 핵심 화면",
  show_hint="실제 Fan 360 화면 캡처가 슬라이드의 55~70%. 04_DEMO Scene 2 앞부분.",
  features=["Fan 360","Segment","Recommendation Hub"],
  ai_role="팬 이해 지원", bvalue="Fan Understanding", piv="i",
  say="팬 데이터가 분산돼 개별 팬을 입체적으로 이해하기 어려웠다 → Fan 360으로 한 화면에서 팬을 본다.",
  screen="Fan Profile / Fan 360 Dashboard (LWC). Segment · Engagement Score · Fan Value Tier · Purchase · Attendance · Timeline.",
  persona=("김매니저","FRM Manager"),
), "PPT")

# ---- 09 · S2 · ACTIVATE
slide("09_s2_activate.png", *C2, "09 · S2 · ACTIVATE — B2C Marketing", "09", DEMO(
  question="각 팬에게 어떻게 다르게 행동할까?",
  fmt_key="DEMO VIDEO", zone="b2c", dur="01:30",
  show_cap="Target Fan 확인 → AI 개인화 메시지 생성 → Review → 발송",
  show_hint="영상 재생 영역이 화면의 중심. 04_DEMO 데모 영상 ① (80~90초).",
  features=["AI Personalized Message"],
  ai_role="Personalize", bvalue="Personalized Fan Engagement", piv="a",
  say="팬별 특성을 반영한 메시지를 담당자가 일일이 쓰기 어려웠다. AI가 생성하고 담당자가 검토·승인 후 발송한다.",
  screen="recommendationReviewPanel + Prompt Fan_Personalized_Message. 생성 결과는 Recommendations__c 레코드로 저장 (Human-in-the-loop).",
  persona=("김매니저","FRM Manager"),
), "DEMO VIDEO")

# ---- 10 · Fan Insight — B2C → B2B Bridge  (Transition, 시각적으로 강하게)
slide("10_fan_insight_bridge.png", *C2, "10 · Fan Insight — B2C → B2B Bridge ⭐", "10", [
  H1("B2C에서 쌓인 팬 데이터가, 여기서 기업의 기회가 된다"),
  KM("Fan Insight는 B2B가 아니라 B2C의 마지막 단계 — 두 세계를 잇는 Bridge."),
  SPLIT("B2C (여기까지)", ["Fan Experience","Fan 360","Recommendation / Personalization"],
        "B2B (여기부터)", ["Partner Matching","Sponsorship Sales"],
        "FAN INSIGHT"),
  ANN("전환 디자인 (가장 중요)","Demo 전체의 turning point. 이 페이지에서 색·커넥터가 파랑(B2C) → 초록(B2B)으로 전환되고, 발표 톤도 여기서 바뀐다. 다른 Demo 페이지보다 시각적으로 강하게."),
  ANN("화면 — 보여줄 것","개념 다이어그램 (FAN DATA ↓ FAN INSIGHT ↓ PARTNER OPPORTUNITY). 별도 스크린샷 없이 전환을 선언하는 페이지. Fan Insight = Report/Dashboard 기반."),
], "TRANSITION")

# ---- 11 · S3 · CONNECT
slide("11_s3_connect.png", *C2B, "11 · S3 · CONNECT — B2C → B2B Sponsorship", "11", DEMO(
  question="팬 데이터를 어떻게 B2B 영업 기회로 연결할까?",
  fmt_key="LIVE", zone="b2b",
  show_cap="Monthly Fan Insight Letter 확인 → 이매니저가 Slack Agent에게 분석 요청 → 적합한 Sponsorship 방향 탐색",
  show_hint="현장 시연. 20·30대 여성 팬 증가 등을 근거로 방향을 좁힌다. 04_DEMO Scene 3.",
  features=["Monthly Fan Insight Letter","Slack Agent"],
  ai_role="Analyze & Discover", bvalue="B2C Data → B2B Sales Opportunity", piv="i",
  say="B2C에서 축적된 팬 데이터를 B2B 담당자가 Sponsorship 관점에서 직접 다시 해석해야 했다. 이제 월간 Fan Insight Letter와 Slack Agent가 방향을 제시한다.",
  screen="Fan Insight Letter (Report/Dashboard 기반) + Flow → Slack. 김매니저 → 이매니저 handoff.",
  persona=("김매니저 → 이매니저","FRM → Sponsorship Sales"),
), "LIVE")

# ---- 12 · S4 · Partner Matching  (이미지에 S4 열 미표시 → 재구성, FORMAT TBD)
slide("12_s4_partner_matching.png", *C2B, "12 · S4 · Partner Matching", "12", DEMO(
  question="이 팬덤과 가장 잘 맞는 기업은 누구인가? — 왜 이 기업인가?",
  fmt_key="TBD", zone="b2b",
  show_cap="팬층 특성(연령·성별·Engagement·구매) ↔ 기업 후보 매칭 → Fit 근거 (Recommendation Reason) → d'Alba",
  show_hint="기업 데이터 = OpenDART API 조회. 00_STORY §8 (기업 DB → Matching → Top 후보 + Reason) / 04_DEMO Scene 4 '반드시 구분할 개념'. ※ Demo순서 이미지에 S4 열이 보이지 않음 (S3→S5) — 포함 여부·표현 방식 팀 확정 필요.",
  features=["Fan Fit","Segment Match","Recommendation Reason"],
  ai_role="Match & Explain", bvalue="데이터 기반 파트너 발굴", piv="i",
  say="“d'Alba는 먼저 Cloud Alpacas 팬덤과 높은 적합도를 보여 후보가 됐습니다.” — AI는 정답이 아니라 '왜 이 기업인가'를 설명한다.",
  screen="Fan Fit / Segment Match (팬덤 적합도) ≠ Lead Score (실제 계약 가능성) — 다음(S5)에서 이어짐.",
  persona=("이매니저","Sponsorship Sales Manager"),
), "TBD")

# ---- 13 · S5 · PIPELINE
slide("13_s5_pipeline.png", *C2B, "13 · S5 · PIPELINE — Dashboard → Lead → Account → OPP", "13", DEMO(
  question="Sponsor 후보를 어떻게 실제 Deal로 발전시킬까?",
  fmt_key="MIX", zone="b2b",
  show_cap="Tableau Next Dashboard → Lead / Lead Score → Account → AI로 부족한 Account 필드 자동 보완 → d'Alba OPP 진입",
  show_hint="PPT 위에 약 5초 임베드 영상. 04_DEMO Scene 4.",
  features=["Tableau Next","Lead Score","Account AI Enrichment"],
  ai_role="Analyze / Score / Enrich", bvalue="Sales Prioritization / Productivity / Data Quality", piv="a",
  say="유망 Sponsor 판단부터 Account 정보 보완까지 수작업이 많았다. 우선순위는 Lead Score로, 빈 정보는 AI가 DART로 채운다.",
  screen="PRM/Tableau Next Dashboard · Lead_Score__c…Final_Lead_Score__c · Prompt CA_Lead_AI_Summary · LeadConvertPartnerContact.",
  persona=("이매니저 / d'Alba","Sponsorship Sales"),
), "MIX")

# ---- 14 · S6 · UNDERSTAND
slide("14_s6_understand.png", *C2B, "14 · S6 · UNDERSTAND — OPP · Needs Analysis", "14", DEMO(
  question="고객은 무엇을 말했는가?",
  fmt_key="DEMO VIDEO", zone="b2b", dur="03:00",
  show_cap="고객 Meeting / Activity → 기록 → AI 분석 → Summary / Signal",
  show_hint="영상 재생 영역이 화면의 중심. 04_DEMO Scene 6 (Zoom 연동).",
  features=["Activity Intelligence"],
  ai_role="Understand", bvalue="Activity 자산화", piv="i",
  say="고객과의 미팅·대화가 단순 기록으로 남아 담당자가 다시 읽고 해석해야 했다. 이제 대화가 요약·Signal로 정리된다.",
  screen="Zoom → Activity 자동 기록 → Prompt CA_Offline_Meeting_* → Interaction_Intelligence__c → Interaction_Signal__c (긍정/위험).",
  persona=("이매니저 / 김하나","Sales / d'Alba 담당자"),
), "DEMO VIDEO")

# ---- 15 · S7 · REASON
slide("15_s7_reason.png", *C2B, "15 · S7 · REASON — OPP · Proposal", "15", DEMO(
  question="그래서 무엇을 제안할까?",
  fmt_key="LIVE", zone="b2b",
  show_cap="과거 유사 사례 + 현재 d'Alba OPP + 팬 데이터 + 고객 Activity → Agent 분석 → 제안 방향 / Package / Product + 근거",
  show_hint="현장 시연. 04_DEMO Scene 7 (Opportunity Agent).",
  features=["Opportunity Agent"],
  ai_role="Reason", bvalue="Context 기반 Sales Decision Support", piv="a",
  say="담당자가 과거 사례·현재 Deal·팬 데이터·고객 Activity를 직접 찾아 종합해야 했다. Agent가 컨텍스트를 모아 제안 방향을 근거와 함께 제시한다.",
  screen="Opportunity Agent (deal / proposal / negotiation / stage_guidance). 조회·추천은 즉시, 쓰기는 담당자 승인 후.",
  persona=("이매니저 / d'Alba","Sponsorship Sales"),
), "LIVE")

# ---- 16 · S8 · ACT
slide("16_s8_act.png", *C2B, "16 · S8 · ACT — OPP · Negotiation", "16", DEMO(
  question="고객의 변화에 어떻게 대응할까?",
  fmt_key="PPT", zone="b2b",
  show_cap="새로운 고객 Activity / 상황 → AI가 선제적으로 분석 → Negotiation 대응 / 수정안 + 판단 근거",
  show_hint="04_DEMO Scene 8. 협상 성사 시 Closed Won으로 전환.",
  features=["Proactive AI","Negotiation Assistant"],
  ai_role="Act Proactively", bvalue="Proactive Selling", piv="a",
  say="고객 반응 변화마다 담당자가 다시 상황을 분석하고 대응해야 했다. AI가 변화를 먼저 감지해 수정안을 근거와 함께 제시한다. 최종 결정·승인은 담당자.",
  screen="Negotiation Assistant · Standard Quote · Negotiation Context. 협상안은 담당자 승인 후 반영. ⚠️ 금액은 발표 전 통일 (04_DEMO 가격 검증).",
  persona=("이매니저 / 김하나","Sales / d'Alba 담당자"),
), "PPT")

# ---- 17 · S9 · EXPAND
slide("17_s9_expand.png", *C2B, "17 · S9 · EXPAND — Post-Sale · 1년 후", "17", DEMO(
  question="1년 후, d'Alba와의 관계를 어떻게 다음 매출로 연결할까?",
  fmt_key="TBD", zone="b2b",
  show_cap="“1년 후” → d'Alba 단년 계약 종료 임박 → Partnership Plan 확인 → d'Alba Upsell Sales 고려",
  show_hint="Demo순서 이미지: 표현 방식 미정 · AI 역할 미정 · 기능 '논의 필요'. 재계약/장기 Partnership 자동화는 문서상 Future Scope — 구현 확인된 부분만 시연 (04_DEMO Scene 9 검증 조건).",
  features=["Partnership Plan (논의 필요)","Upsell (논의 필요)"],
  ai_role="미정", bvalue="Renewal / Upsell을 통한 Revenue Expansion 방향", piv="v",
  say="단년 계약 종료 후 기존 Sponsor를 Renewal/Upsell로 연결할지 담당자가 다시 판단해야 한다. “첫 계약은 매출엔진의 끝이 아니라 시작” — 단, 여기부터는 방향 제시.",
  screen="현재 GitHub main 기준 구현 근거가 명확한 부분만. 지난 시즌 성과는 '발표용 시뮬레이션 데이터'로 명시.",
  persona=("이매니저 / d'Alba","Sponsorship Sales"),
), "TBD")

# ======================= CHAPTER III — WHAT WE LEARNED (18-19) =======================
#  DEMO(01-17) → 18 WHAT WE LEARNED → 19 FROM LEARNING TO BUILDING → 20 → 21 → PPT OFF → Org LIVE

# ---- 18 · WHAT WE LEARNED  (설계 판단 4개 + 중앙 큰 메시지)
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
          ("04","AI WITH HUMAN CONTROL","Agentforce는 추천·분석, Salesforce가 실행, 사람이 결정."),
        ])
    + '</div>',
  '<div class="fill center" style="gap:18px;justify-content:center">'
    '<div class="h1" style="text-align:center;font-size:50px;line-height:1.24;font-weight:800">'
      'We came here to learn Salesforce.<br>We leave knowing how to build with it.</div>'
    + '<div class="sm" style="text-align:center;letter-spacing:.06em">Fan Data → Customer 360 → Action → Revenue</div>'
    + '</div>',
  ANN("디자인 노트","상단 = 얇은 principle card 4개(영문 Headline + 1줄). 중앙 = 큰 타이포 메시지가 주인공. 하단 = 아주 얇은 flow 1줄 (복잡해지면 생략). 긴 설명·구현 수치·Object 목록·KPI·문단 금지 — 발표자가 말한다."),
])

# ---- 19 · FROM LEARNING TO BUILDING  (브리지 슬라이드 — 거의 빈 화면 + 초대형 타이포)
slide("19_from_learning_to_building.png", *C3, "19 · From Learning to Building", "19", [
  '<div class="fill center" style="gap:52px">',
  '<div class="sm" style="letter-spacing:.26em;text-transform:uppercase">From Learning to Building</div>',
  '<div class="h1" style="text-align:center;font-size:76px;line-height:1.32;font-weight:800">'
    "We didn't start with<br>Salesforce features.<br><br>"
    'We started with<br>the business.</div>',
  '</div>',
  ANN("디자인 노트","DEMO와 결론 사이의 브리지 슬라이드 — 정보 전달용이 아니라 '호흡'을 만드는 페이지. 거의 빈 화면 + 초대형 타이포 + 넉넉한 여백. 상단 작은 label + 중앙 두 문장이 전부. 다이어그램·카드·아이콘·Architecture·Object 목록·기술 스택·KPI·발표자 멘트 절대 금지. 타이포의 크기와 줄바꿈으로 메시지의 힘을 만든다."),
])

# ======================= CHAPTER IV — CONCLUSION (20-21) =======================

# ---- 20 · WHAT WE BUILT / BUSINESS VALUE  (기존 구조 유지 — FAN / INSIGHT / REVENUE)
slide("20_what_we_built.png", *C4, "20 · What We Built / Business Value", "20", [
  H1("What We Built"),
  KM("FAN → INSIGHT → REVENUE — 하나의 흐름."),
  '<div class="row grow" style="align-items:center">'
    + WVCARD("FAN","팬을 이해하다",["Fan 360","Personalization"],"Fan Lifetime Value ↑")
    + '<span class="arw" style="align-self:center">&rsaquo;</span>'
    + WVCARD("INSIGHT","기회를 발견하다",["Fan Insight","Partner Matching"],"Personalized Fan Experience ↑")
    + '<span class="arw" style="align-self:center">&rsaquo;</span>'
    + WVCARD("REVENUE","매출로 연결하다",["Sponsorship Sales","Opportunity"],"Sponsorship Revenue ↑")
    + '</div>',
  ANN("디자인 노트","FAN → INSIGHT → REVENUE 를 하나의 흐름으로. 미측정 KPI·추측성 ROI 절대 금지. 필요 시 05_ARCHITECTURE 실측 수치만."),
])

# ---- 21 · FUTURE / CLOSING  (PPT의 마지막 장. 이후 Org LIVE로 전환)
slide("21_future_closing.png", *C4, "21 · Future / Closing", "21", [
  H1("현재에서 미래로"),
  '<div class="ph diagram" style="flex:none;align-items:stretch;gap:16px;padding:22px 46px">'
    '<div><div class="sm" style="margin-bottom:8px;color:#3F4A5A">NOW · 현재 구현</div>'
      + FLOW([("Fan Data","","b2c"),("Insight","","b2c"),("Partner Matching","","b2b"),("Sponsorship","","b2b")], tight=True) + '</div>'
    + '<div style="border-top:2px dashed var(--dash)"></div>'
    + '<div><div class="sm" style="margin-bottom:8px">FUTURE SCOPE · 미구현 (점선 · 흐리게)</div>'
      + FLOW([("Real-time Data","","future"),("AI Decision","","future"),("Autonomous Action","","future"),("Continuous Revenue Growth","","future")], tight=True) + '</div>'
    + '</div>',
  '<div class="fill center" style="gap:18px">'
    '<div class="h1 big" style="text-align:center">팬을 이해하고, 팬덤의 가치를 발견하고,<br>그 가치를 매출로 연결합니다.</div>'
    + PH("WORDMARK","CLOUD ALPACAS","Sustainable Revenue Engine",variant="logo",grow=0)
    + '</div>',
  ANN('발표자 포인트', 'PPT의 마지막 장. 21장 이후 바로 PPT를 끄고 Salesforce Org LIVE로 전환 -> 퀴즈 당첨자 발표(실제 Org 화면) -> Q&A. Winner / Quiz Result / Q&A / Thank You 슬라이드는 만들지 않는다. FUTURE는 현재 구현처럼 보이지 않게 - 점선/흐리게/secondary hierarchy.'),
])

# ============================================================ render
for f in list(OUT.glob("[0-9][0-9]_*.html")) + list(OUT.glob("[0-9][0-9]_*.png")):
    f.unlink()
for args in S:
    fname, ccls, clabel, role, num, blocks, *rest = args
    fmt = rest[0] if rest else None
    page(fname.replace(".png", ".html"), ccls, clabel, role, num, blocks, fmt)
print(f"generated {len(S)} html slides in {OUT}")
