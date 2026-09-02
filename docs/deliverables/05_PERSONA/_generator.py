#!/usr/bin/env python3
# Cloud Alpacas — Persona Profile generator
# Source of truth: cloudalpacas-org-inventory/docs/00_STORY.md
import os, html

OUT = os.path.join(os.path.dirname(__file__), "persona_svg")
os.makedirs(OUT, exist_ok=True)
W, H = 1920, 1080

NAVY="#16294F"; NAVY2="#2E4E93"
ORANGE="#EC6A22"; ORANGE_DK="#B24B12"
TEAL="#0E7A82"; TEAL_DK="#0A5C62"
PINK="#C0477F"; PINK_DK="#98305F"
INK="#1E2532"; SLATE="#5A6472"; MUTE="#939BA8"
BORDER="#D9DFE8"; PANEL="#F5F7FA"; CANVAS="#FFFFFF"
FONT="'Helvetica Neue',Arial,'Apple SD Gothic Neo','Malgun Gothic',sans-serif"

def esc(s): return html.escape(str(s), quote=True)
def tint(hexc, a):  # overlay hex on white at alpha a
    r=int(hexc[1:3],16); g=int(hexc[3:5],16); b=int(hexc[5:7],16)
    r=int(r*a+255*(1-a)); g=int(g*a+255*(1-a)); b=int(b*a+255*(1-a))
    return f"#{r:02x}{g:02x}{b:02x}"

def tw(s,fs,wt=400):
    w=0.0
    for ch in s:
        w += fs*(0.55 if ord(ch)<0x1100 else 1.0)
    return w*(1.05 if wt>=600 else 1.0)

def wrap(s,maxw,fs,wt=400):
    out=[];cur=""
    for wd in s.split(" "):
        t=wd if not cur else cur+" "+wd
        if tw(t,fs,wt)<=maxw or not cur: cur=t
        else: out.append(cur);cur=wd
    if cur:out.append(cur)
    return out

class SVG:
    def __init__(s):s.b=[]
    def add(s,x):s.b.append(x)
    def t(s,x,y,txt,fs=18,fill=INK,wt=400,anchor="start",ls="0",op=1):
        s.add(f'<text x="{x:.1f}" y="{y:.1f}" font-size="{fs}" fill="{fill}" font-weight="{wt}" '
              f'text-anchor="{anchor}" letter-spacing="{ls}" opacity="{op}">{esc(txt)}</text>')
    def r(s,x,y,w,h,rx=0,fill="none",stroke="none",sw=1,dash=None,op=1):
        d=f' stroke-dasharray="{dash}"' if dash else ""
        s.add(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" fill="{fill}" '
              f'stroke="{stroke}" stroke-width="{sw}"{d} opacity="{op}"/>')
    def line(s,x1,y1,x2,y2,stroke=NAVY,sw=2,dash=None):
        d=f' stroke-dasharray="{dash}"' if dash else ""
        s.add(f'<path d="M {x1:.1f} {y1:.1f} L {x2:.1f} {y2:.1f}" stroke="{stroke}" stroke-width="{sw}" fill="none" stroke-linecap="round"{d}/>')
    def path(s,d,fill="none",stroke="none",sw=2,marker=None):
        m=f' marker-end="url(#{marker})"' if marker else ""
        s.add(f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"{m}/>')
    def bullets(s,x,y,items,color,maxw,fs=14,gap=7,lh=19):
        cy=y
        for it in items:
            lines=wrap(it,maxw-20,fs)
            s.add(f'<circle cx="{x+3}" cy="{cy-5}" r="3" fill="{color}"/>')
            for i,ln in enumerate(lines):
                s.t(x+16,cy+i*lh,ln,fs=fs,fill=INK if i==0 else SLATE,wt=400)
            cy += len(lines)*lh + gap
        return cy
    def out(s,defs=""):
        return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
                f'font-family="{FONT}"><defs>{defs}</defs>'+"".join(s.b)+"</svg>")

MARK=(f'<marker id="ah" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7.5" markerHeight="7.5" '
      f'orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="{NAVY}"/></marker>'
      f'<marker id="ao" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7.5" markerHeight="7.5" '
      f'orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="{ORANGE}"/></marker>'
      f'<marker id="ag" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" '
      f'orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="{MUTE}"/></marker>')

# role glyphs (simple)
def glyph(kind,cx,cy,c):
    if kind=="b2c":   # target
        return (f'<circle cx="{cx}" cy="{cy}" r="26" fill="none" stroke="{c}" stroke-width="5"/>'
                f'<circle cx="{cx}" cy="{cy}" r="13" fill="none" stroke="{c}" stroke-width="5"/>'
                f'<circle cx="{cx}" cy="{cy}" r="3.5" fill="{c}"/>')
    if kind=="b2b":   # briefcase
        return (f'<rect x="{cx-26}" y="{cy-14}" width="52" height="34" rx="5" fill="none" stroke="{c}" stroke-width="5"/>'
                f'<path d="M {cx-12} {cy-14} v-8 a4 4 0 0 1 4 -4 h16 a4 4 0 0 1 4 4 v8" fill="none" stroke="{c}" stroke-width="5"/>'
                f'<line x1="{cx-26}" y1="{cy+3}" x2="{cx+26}" y2="{cy+3}" stroke="{c}" stroke-width="5"/>')
    if kind=="sponsor":  # storefront / tag
        return (f'<path d="M {cx-26} {cy-6} l 6 -18 h 40 l 6 18 z" fill="none" stroke="{c}" stroke-width="5" stroke-linejoin="round"/>'
                f'<rect x="{cx-22}" y="{cy-6}" width="44" height="30" rx="3" fill="none" stroke="{c}" stroke-width="5"/>'
                f'<line x1="{cx}" y1="{cy-6}" x2="{cx}" y2="{cy+24}" stroke="{c}" stroke-width="5"/>')
    if kind=="fan":   # person + heart
        return (f'<circle cx="{cx}" cy="{cy-14}" r="11" fill="none" stroke="{c}" stroke-width="5"/>'
                f'<path d="M {cx-20} {cy+22} a20 20 0 0 1 40 0" fill="none" stroke="{c}" stroke-width="5"/>')
    return ""

def render_persona(p, fname):
    s=SVG()
    c=p["color"]; cd=p["color_dk"]
    s.r(0,0,W,H,fill=CANVAS)
    # header
    s.t(56,46,"☁  CLOUD ALPACAS",fs=14,fill=NAVY,wt=800,ls="2")
    s.t(56,78,p["kicker"],fs=14.5,fill=cd,wt=700,ls="1.4")
    dom=p["domain"]; bw=tw(dom,15,700)+44
    s.r(W-56-bw,34,bw,40,rx=20,fill=tint(c,0.12),stroke=c,sw=1.6)
    s.t(W-56-bw/2,60,dom,fs=15,fill=cd,wt=700,anchor="middle")

    TOP,BOT=104,1014

    # ---------------- LEFT PANEL ----------------
    LX,LW=56,592
    ty,th=TOP,360
    s.r(LX,ty,LW,th,rx=22,fill=tint(c,0.09),stroke=c,sw=1.6)
    s.add(f'<circle cx="{LX+LW/2}" cy="{ty+140}" r="92" fill="{CANVAS}" stroke="{c}" stroke-width="2.6"/>')
    s.t(LX+LW/2,ty+176,p["initial"],fs=100,fill=c,wt=800,anchor="middle")
    s.add(glyph(p["glyph"],LX+LW/2,ty+272,cd))
    s.t(LX+LW/2,ty+330,p["role_en"],fs=14.5,fill=cd,wt=700,anchor="middle",ls="1.6")

    ny=ty+th+62
    s.t(LX,ny,p["name"],fs=44,fill=NAVY,wt=800)
    roleL=wrap(p["role"],LW,16.5,500)
    for i,ln in enumerate(roleL):
        s.t(LX,ny+34+i*23,ln,fs=16.5,fill=SLATE,wt=500)
    qy=ny+34+len(roleL)*23+40
    tagL=wrap(p["tagline"],LW-26,19,600)
    s.add(f'<rect x="{LX}" y="{qy-26}" width="5" height="{16+len(tagL)*27}" rx="2.5" fill="{c}"/>')
    for i,ln in enumerate(tagL):
        s.t(LX+22,qy+i*27,ln,fs=19,fill=cd,wt=600)
    sy=qy+len(tagL)*27+46
    s.t(LX,sy,p["left_title"],fs=13.5,fill=NAVY,wt=800,ls="1.3")
    s.bullets(LX,sy+32,p["left_items"],c,LW,fs=14.5,gap=11,lh=20)

    s.line(LX+LW+34,TOP,LX+LW+34,BOT+2,stroke=BORDER,sw=1.4)

    # ---------------- RIGHT PANEL ----------------
    RX=LX+LW+72; RW=W-56-RX
    def cardH(items,fs=15,lh=21,gap=11):
        h=58
        for it in items: h+=len(wrap(it,RW-52,fs))*lh+gap
        return h+8
    def card(x,y,w,h,title,items,accent=c):
        s.r(x,y,w,h,rx=16,fill=CANVAS,stroke=BORDER,sw=1.5)
        s.add(f'<rect x="{x}" y="{y}" width="6" height="{h}" rx="3" fill="{accent}"/>')
        s.t(x+26,y+36,title,fs=16.5,fill=NAVY,wt=800,ls="0.5")
        s.bullets(x+24,y+70,items,accent,w-46,fs=15,gap=11,lh=21)

    bh=150                      # question banner
    cards=[("issues_title","issues"),("pain_title","pain"),("goals_title","goals")]
    hs=[cardH(p[k[1]]) for k in cards]
    g=24
    total=sum(hs)+2*g
    region=(BOT-bh-28) - TOP
    y=TOP + max(0,(region-total)/2)
    for (tk,ik),h in zip(cards,hs):
        card(RX,y,RW,h,p[tk],p[ik]); y+=h+g
    by=BOT-bh
    s.r(RX,by,RW,bh,rx=16,fill=c)
    s.t(RX+28,by+36,"핵심 질문  ·  KEY QUESTION",fs=13,fill="#FFFFFF",wt=800,ls="1.5",op=0.8)
    qL=wrap(p["question"],RW-56,26,700)
    for i,ln in enumerate(qL):
        s.t(RX+28,by+74+i*32,ln,fs=26,fill="#FFFFFF",wt=800)
    s.t(RX+28,by+74+len(qL)*32+16,p["chain"],fs=15,fill="#FFFFFF",wt=600,op=0.92)

    s.t(56,H-22,p["foot"],fs=12,fill=MUTE,wt=500)
    open(os.path.join(OUT,fname),"w").write(s.out(MARK))
    print("wrote",fname)

# ===========================================================================
KIM_MANAGER=dict(
 color=NAVY,color_dk=NAVY2,initial="김",glyph="b2c",
 kicker="PERSONA PROFILE · 01 / 04",domain="B2C · Fan Relationship",
 name="김매니저",role_en="B2C FRM MANAGER",
 role="Cloud Alpacas FRM Manager · Salesforce Customer 360 사용자(User)",
 tagline="“팬 데이터를 근거로, 지금 이 팬에게 가장 적절한 다음 행동을 실행한다.”",
 left_title="업무 방식 · WORK STYLE",
 left_items=[
  "Customer 360으로 팬이 여정(SNS→가입→첫직관→굿즈→재방문→멤버십)의 어디쯤 있는지 확인",
  "Current Segment · Engagement Level · Fan Value 3개 축으로 팬을 이해",
  "상태에 맞는 Next Best Action 실행 — Welcome / First Ticket / First Visit / Membership Campaign",
  "KPI로 성과 관리 — 활성화율 · 첫 관람 전환율 · 재방문율 · 멤버십 가입률 · Fan LTV",
 ],
 issues_title="핵심 이슈 · KEY ISSUES",
 issues=[
  "팬 정보가 티켓·굿즈·멤버십·앱·문의로 흩어져 “팬은 안 보이고 데이터만 보인다”",
  "이루키가 무엇을 좋아하는지 연결해서 볼 수 없다 — 360° Fan View 부재",
  "누가 Ticket Only Fan · Membership Candidate · VIP 후보인지 자동으로 알 수 없다",
 ],
 pain_title="Pain Point · 현재 상태",
 pain=[
  "모든 팬에게 같은 이벤트 · 같은 쿠폰 · 같은 메시지를 보낸다",
  "VIP 가능성이 높은 팬도 엑셀을 정리한 후에야 발견한다 — 타이밍을 놓친다",
  "신규 팬이 1,000명 생겨도 누구에게 무엇을 제안할지 우선순위를 알 수 없다",
 ],
 goals_title="목표 · 우선순위 · GOALS",
 goals=[
  "신규 팬을 이해하고 개인화된 액션으로 충성 팬으로 성장시킨다",
  "첫 관람 · 재방문 · 첫 굿즈 · 멤버십 · 시즌권 전환율을 높인다",
  "장기적으로 Fan Lifetime Value를 극대화한다 (구단 Phase 1 Business Goal)",
 ],
 question="어떤 팬에게 지금 무엇을 제안해야 하는가?",
 chain="Fan Insight → Fan 이해 → Recommendation → 개인화 → Action",
 foot="근거: 00_STORY.md §1 Business Goal · §2 Pain Point 1–5 · §3 FRM Team/KPI · §4·§5 Persona/Journey · §6 Segment · §7 Next Best Action",
)

LEE_MANAGER=dict(
 color=ORANGE,color_dk=ORANGE_DK,initial="이",glyph="b2b",
 kicker="PERSONA PROFILE · 02 / 04",domain="B2B · Sponsorship Sales",
 name="이매니저",role_en="B2B SPONSORSHIP SALES MANAGER",
 role="Cloud Alpacas Sponsorship Sales Manager  ·  이름 가칭(TBD)",
 tagline="“팬을 이해하고, 기업을 찾아, 계약으로 연결한다.”",
 left_title="업무 방식 · WORK STYLE",
 left_items=[
  "Fan 360 데이터에서 팬덤의 광고 가치 가설을 세운다 (예: 여성 팬 유입↑ · 뷰티/라이프스타일/F&B 관심↑)",
  "기업 DB(약 100개) + Agentforce Top 10 추천 + Recommendation Reason 검토",
  "실제 Outbound 대상만 Lead 등록 → Lead Qualification · Lead Score 평가",
  "Opportunity → Sponsorship Package/Quote → Negotiation → Closed Won",
  "Pipeline / Revenue Dashboard로 목표 매출 대비 부족분 관리",
 ],
 issues_title="핵심 이슈 · KEY ISSUES",
 issues=[
  "“유명한 회사”가 아니라 우리 팬덤에 실제 광고 가치가 높은 기업을 찾아야 한다",
  "Agentforce Fan Fit Score ≠ Lead Score — Fit이 높다고 계약 가능성이 높은 건 아니다",
  "Pipeline이 목표 매출 대비 얼마나 부족한지, 스폰서가 몇 개 더 필요한지 알아야 한다",
 ],
 pain_title="Pain Point · 현재 상태",
 pain=[
  "팬은 늘고 있는데 구단은 여전히 적자 — 티켓·멤버십·굿즈 매출만으로는 부족하다",
  "팬이 어떤 브랜드·콘텐츠에 반응하는지 데이터 없이 감·인맥에 의존해 영업한다",
  "후보 기업과 팬층의 광고 Fit을 검증할 근거가 없다",
  "과거 “야구 팬 = 40~50대 남성” 가정으로 진행한 장기 캠페인이 성과를 내지 못했다",
 ],
 goals_title="목표 · 우선순위 · GOALS",
 goals=[
  "Fan 360 데이터를 근거로 팬덤에 광고 가치가 높은 기업을 발굴한다",
  "Lead → Opportunity → Contract Pipeline으로 연결해 Sponsorship Revenue를 만든다",
  "목표 매출 대비 Pipeline 부족분을 추가 Outbound Lead 발굴로 메운다",
 ],
 question="어떤 기업을 먼저 접촉하고, 어떻게 계약으로 이끌 것인가?",
 chain="기업 발굴 → Fit 분석 → 영업 → 제안 → 계약 → 관계 확대",
 foot="근거: 00_STORY.md §1[P2] · §2[P2] Pain Point 1–7 · §4[P2] 이 매니저 · §8 Phase 2 Story · §9 B2B Next Best Action",
)

KIM_HANA=dict(
 color=TEAL,color_dk=TEAL_DK,initial="하",glyph="sponsor",
 kicker="PERSONA PROFILE · 03 / 04",domain="Sponsor · Brand",
 name="김하나",role_en="SPONSOR — d'ALBA (예시 시나리오)",
 role="d'Alba(달바) · 뷰티/스킨케어 브랜드 — 스폰서십 검토 담당  (이름·직책은 예시)",
 tagline="“Cloud Alpacas 팬덤이 우리 브랜드에 만드는 사업적 가치를 판단한다.”",
 left_title="브랜드 상황 · CONTEXT",
 left_items=[
  "d'Alba는 뷰티/스킨케어 브랜드 — Cloud Alpacas Top 10 추천 중 Fan Fit이 높은 대표 사례",
  "Cloud Alpacas 팬덤은 최근 여성 팬 유입이 크게 늘고, 뷰티·라이프스타일·F&B 관심이 높다",
  "구단이 제안하는 것: 구장·전광판·펜스 광고, 공식 SNS 노출, Brand Day, 프로모션, Collaboration Goods",
  "일방적으로 “판매되는 광고주”가 아니라, 팬덤 가치를 스스로 판단하려는 입장",
 ],
 issues_title="핵심 이슈 · KEY ISSUES",
 issues=[
  "이 브랜드의 타겟 고객층이 Cloud Alpacas 팬덤과 정말 겹치는가?",
  "계약이 성사돼도 실제 광고 효과가 기대에 못 미칠 위험은 없는가?",
  "구단이 감이 아니라 팬 데이터(Recommendation Reason)를 근거로 제안하는가?",
 ],
 pain_title="우려 · 현재 상태",
 pain=[
  "팬 Audience와 브랜드 타겟의 적합도(Brand Fit)를 확인할 근거가 필요하다",
  "어떤 Sponsorship Package가 우리 브랜드 노출 목표에 맞는지 판단해야 한다",
  "과거 잘못된 타깃 가정으로 성과를 못 낸 스폰서 사례를 경계한다",
 ],
 goals_title="목표 · Business Outcome",
 goals=[
  "팬 Audience와 브랜드 타겟의 적합도(Brand Fit)를 데이터로 확인한다",
  "스폰서십 투자 대비 브랜드 가치와 사업 성과(Business Outcome)를 확보한다",
  "구단과 장기적으로 유효한 파트너 관계로 발전할 수 있는지 가늠한다",
 ],
 question="Cloud Alpacas의 팬덤이 우리 브랜드에 어떤 가치를 주는가?",
 chain="Fan Audience → Brand Fit → Sponsorship Value → Business Outcome",
 foot="근거: 00_STORY.md §8.2·§8.3 (d'Alba·팬덤 관심사·Sponsorship Package) · §2[P2] Pain Point 4·7   |   이름 “김하나”와 직책은 문서에 없는 예시",
)

IRUKI=dict(
 color=PINK,color_dk=PINK_DK,initial="루",glyph="fan",
 kicker="PERSONA PROFILE · 04 / 04",domain="Fan · B2C Customer",
 name="이루키",role_en="FAN — B2C CUSTOMER",
 role="27세 · 직장인 · Cloud Alpacas 신규 팬  (20대 여성 대표 팬)",
 tagline="“내 활동과 취향에 맞는 경험과 제안을 받고 싶다.”",
 left_title="팬 특성 · FAN CHARACTERISTICS",
 left_items=[
  "야구를 거의 본 적이 없다",
  "SNS에서 우연히 문선수의 영상을 보고 Cloud Alpacas에 관심을 갖게 됐다",
  "친구와 함께 첫 직관을 경험했다",
  "응원 문화와 경기장 분위기에 빠져 점점 클라우드 팬이 되어간다",
 ],
 issues_title="Fan Journey · 기대",
 issues=[
  "여정: SNS → 회원가입 → 첫 티켓 → 첫 직관 → 첫 굿즈 → 재방문 → 멤버십 → 충성팬",
  "구단이 나를 팬으로 이해하는가 — 문선수를 좋아하고 직관을 다녀온 걸 아는가?",
  "내 상태(New Fan / Active Fan)에 맞는 다음 경험을 안내받고 있는가?",
 ],
 pain_title="Pain Point · 현재 상태",
 pain=[
  "모든 팬에게 똑같은 이벤트·쿠폰·메시지가 온다 — 내게 맞는 제안이 아니다",
  "첫 직관 후 무엇을 하면 좋을지(굿즈·재방문·멤버십) 안내가 없다",
  "관심이 식기 쉬운 시점에 적절한 계기를 받지 못하면 그냥 멀어진다",
 ],
 goals_title="이루키가 원하는 것 · GOALS",
 goals=[
  "내 취향(문선수·응원문화)에 맞는 개인화된 경험",
  "적절한 시점의 다음 단계 제안 — 첫 굿즈, 재방문, 멤버십",
  "Cloud Alpacas와 오래 함께하는 충성 팬으로 성장",
 ],
 question="나에게 적합한 경험과 제안을 받고 있는가?",
 chain="Fan Activity → Fan Profile → Personalized Experience → Loyalty",
 foot="근거: 00_STORY.md §4 이루키 · §5 Customer Journey · §6 Current Segment · §7 Next Best Action · §2 Pain Point 2·3   |   이루키의 데이터가 쌓일수록 이매니저의 근거도 쌓인다(§4·§8.3)",
)

for p,fn in [(KIM_MANAGER,"01_KIM_MANAGER.svg"),(LEE_MANAGER,"02_LEE_MANAGER.svg"),
             (KIM_HANA,"03_KIM_HANA.svg"),(IRUKI,"04_IRUKI.svg")]:
    render_persona(p,fn)

# ===========================================================================
# 05 — PERSONA MAP
# ===========================================================================
def render_map(fname):
    s=SVG()
    s.r(0,0,W,H,fill=CANVAS)
    s.t(56,46,"☁  CLOUD ALPACAS",fs=14,fill=NAVY,wt=800,ls="2")
    s.t(56,80,"PERSONA MAP · 05 / 05",fs=14.5,fill=ORANGE_DK,wt=700,ls="1.4")
    s.t(56,118,"네 페르소나가 하나의 매출 엔진으로 연결된다",fs=27,fill=NAVY,wt=700)

    def pcard(x,y,w,h,c,cd,initial,name,role,sub):
        s.r(x,y,w,h,rx=16,fill=tint(c,0.08),stroke=c,sw=1.8)
        s.add(f'<circle cx="{x+40}" cy="{y+42}" r="24" fill="{CANVAS}" stroke="{c}" stroke-width="2"/>')
        s.t(x+40,y+51,initial,fs=24,fill=c,wt=800,anchor="middle")
        s.t(x+78,y+34,name,fs=21,fill=NAVY,wt=800)
        s.t(x+78,y+56,role,fs=13.5,fill=cd,wt=700)
        for i,ln in enumerate(wrap(sub,w-40,13,400)):
            s.t(x+20,y+88+i*17,ln,fs=13,fill=SLATE)
        return (x,y,w,h)

    CW,CH=430,150
    iru = pcard(150,170,CW,CH,PINK,PINK_DK,"루","이루키","FAN",
                "SNS로 유입된 신규 팬. 관람·구매·관심 활동이 데이터로 쌓인다.")
    hana= pcard(W-150-CW,170,CW,CH,TEAL,TEAL_DK,"하","김하나","SPONSOR · d'Alba",
                "뷰티 브랜드. 팬덤이 브랜드에 주는 사업적 가치를 판단한다.")
    kim = pcard(150,470,CW,CH,NAVY,NAVY2,"김","김매니저","B2C · FRM",
                "Fan 360으로 팬을 이해하고 개인화 Next Best Action을 실행한다.")
    lee = pcard(W-150-CW,470,CW,CH,ORANGE,ORANGE_DK,"이","이매니저","B2B · Sponsorship Sales",
                "Fan 데이터로 광고 가치 높은 기업을 발굴해 계약으로 연결한다.")

    def elabel(x,y,txt,c):
        w=tw(txt,13.5,700)+16
        s.r(x-w/2,y-13,w,22,rx=6,fill=CANVAS,stroke=c,sw=1.2)
        s.t(x,y+3,txt,fs=13.5,fill=c,wt=700,anchor="middle")

    # iru -> kim (down)
    s.path(f"M {150+CW/2} {170+CH} L {150+CW/2} {470}",stroke=PINK,sw=2.6,marker="ao" if False else None)
    s.add(f'<path d="M {150+CW/2} {170+CH} L {150+CW/2} {470}" stroke="{PINK}" stroke-width="2.6" fill="none" marker-end="url(#ag)"/>')
    elabel(150+CW/2,320,"팬 데이터 · 팬덤 가치",PINK_DK)
    # iru -> lee (diagonal, dashed) : Fan Fit 근거
    s.add(f'<path d="M {150+CW} {170+CH-30} L {W-150-CW} {470+20}" stroke="{PINK}" stroke-width="2.4" '
          f'fill="none" stroke-dasharray="7 5" marker-end="url(#ag)"/>')
    elabel((150+CW+(W-150-CW))/2,372,"Fan 360 데이터 → 팬덤의 광고 가치 · Fan Fit 근거 (Agentforce Matching)",PINK_DK)
    # hana -> lee (down)
    s.add(f'<path d="M {W-150-CW/2} {170+CH} L {W-150-CW/2} {470}" stroke="{TEAL}" stroke-width="2.6" fill="none" marker-end="url(#ag)"/>')
    elabel(W-150-CW/2,320,"브랜드 가치 · 광고주 니즈",TEAL_DK)

    # kim -> outcome L
    oy=690; oh=96
    s.r(150,oy,CW,oh,rx=14,fill=NAVY,op=1)
    s.t(150+CW/2,oy+38,"팬 로열티 · 팬 기반 수익화",fs=17,fill="#FFFFFF",wt=700,anchor="middle")
    s.t(150+CW/2,oy+64,"티켓 · 굿즈 · 멤버십 · 시즌권 전환",fs=13,fill="#FFFFFF",wt=500,anchor="middle",op=0.85)
    s.add(f'<path d="M {150+CW/2} {470+CH} L {150+CW/2} {oy}" stroke="{NAVY}" stroke-width="2.6" fill="none" marker-end="url(#ah)"/>')
    elabel(150+CW/2,470+CH+38,"개인화 Recommendation · Campaign",NAVY2)

    # lee -> outcome R
    s.r(W-150-CW,oy,CW,oh,rx=14,fill=ORANGE)
    s.t(W-150-CW/2,oy+38,"Sponsorship · Contract Revenue",fs=17,fill="#FFFFFF",wt=700,anchor="middle")
    s.t(W-150-CW/2,oy+64,"Lead → Opportunity → Proposal → Negotiation → Closed Won",fs=12.5,fill="#FFFFFF",wt=500,anchor="middle",op=0.9)
    s.add(f'<path d="M {W-150-CW/2} {470+CH} L {W-150-CW/2} {oy}" stroke="{ORANGE}" stroke-width="2.6" fill="none" marker-end="url(#ao)"/>')
    elabel(W-150-CW/2,470+CH+38,"Sponsorship Package · Quote",ORANGE_DK)

    # converge to engine
    ey=880; ew=1000; ex=(W-ew)/2; eh=120
    s.r(ex,ey,ew,eh,rx=18,fill=tint(ORANGE,0.10),stroke=ORANGE,sw=2)
    s.t(W/2,ey+34,"FAN VALUE  +  SPONSOR VALUE",fs=15,fill=ORANGE_DK,wt=800,anchor="middle",ls="1.5")
    s.t(W/2,ey+72,"Cloud Alpacas의 지속 가능한 매출 엔진",fs=25,fill=NAVY,wt=800,anchor="middle")
    s.t(W/2,ey+100,"팬을 키우는 힘(Phase 1)과 팬덤을 수익으로 바꾸는 힘(Phase 2)이 같은 Fan 360 데이터 위에서 맞물린다",
        fs=13,fill=SLATE,wt=500,anchor="middle")
    s.add(f'<path d="M {150+CW/2} {oy+oh} L {150+CW/2} {ey+eh/2} L {ex} {ey+eh/2}" stroke="{NAVY}" stroke-width="2.6" fill="none" marker-end="url(#ah)"/>')
    s.add(f'<path d="M {W-150-CW/2} {oy+oh} L {W-150-CW/2} {ey+eh/2} L {ex+ew} {ey+eh/2}" stroke="{ORANGE}" stroke-width="2.6" fill="none" marker-end="url(#ao)"/>')

    s.t(56,H-24,"근거: 00_STORY.md §1·§3·§4·§5·§8.3 — 이루키(Fan) 데이터가 김매니저의 육성과 이매니저의 Fan Fit 판단 양쪽을 뒷받침한다",
        fs=12,fill=MUTE,wt=500)
    open(os.path.join(OUT,fname),"w").write(s.out(MARK))
    print("wrote",fname)

render_map("05_PERSONA_MAP.svg")
