#!/usr/bin/env python3
# Cloud Alpacas — System Architecture diagram  (v2)
# Source of truth: cloudalpacas-org-inventory/docs/deliverables/05_ARCHITECTURE.md
import os, html
OUT=os.path.join(os.path.dirname(__file__),"arch_svg"); os.makedirs(OUT,exist_ok=True)
W,H=1920,1080

NAVY="#07111F"; NAVY2="#22314A"
ORANGE="#FC4E00"; ORANGE_DK="#C23A00"; ORANGE_BG="#FDE9DE"
BG="#F6F3F1"; CARD="#FFFFFF"
SF="#0B79C4"; SF_BG="#E9F3FB"
BLUE="#2E6FB0"; BLUE_BG="#E7F0F9"
GREY="#59626F"; GREY_BG="#EDEFF2"
INK="#1B2430"; SLATE="#5A6472"; MUTE="#8B95A2"; BORDER="#D6DCE4"
FONT="'Pretendard','Helvetica Neue',Arial,'Apple SD Gothic Neo','Malgun Gothic',sans-serif"

def esc(s): return html.escape(str(s),quote=True)
def tw(s,fs,wt=400):
    return sum(fs*(0.55 if ord(c)<0x1100 else 1.0) for c in s)*(1.04 if wt>=600 else 1.0)
def wrap(s,mw,fs,wt=400):
    o=[];c=""
    for wd in s.split(" "):
        t=wd if not c else c+" "+wd
        if tw(t,fs,wt)<=mw or not c: c=t
        else: o.append(c);c=wd
    if c:o.append(c)
    return o

class S:
    def __init__(s):s.b=[]
    def add(s,x):s.b.append(x)
    def t(s,x,y,txt,fs=16,fill=INK,wt=400,anchor="start",ls="0",op=1):
        s.add(f'<text x="{x:.1f}" y="{y:.1f}" font-size="{fs}" fill="{fill}" font-weight="{wt}" '
              f'text-anchor="{anchor}" letter-spacing="{ls}" opacity="{op}">{esc(txt)}</text>')
    def r(s,x,y,w,h,rx=0,fill="none",stroke="none",sw=1,dash=None,op=1):
        d=f' stroke-dasharray="{dash}"' if dash else ""
        s.add(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" fill="{fill}" '
              f'stroke="{stroke}" stroke-width="{sw}"{d} opacity="{op}"/>')
    def path(s,d,stroke=NAVY,sw=2,dash=None,marker="ah",fill="none"):
        da=f' stroke-dasharray="{dash}"' if dash else ""
        m=f' marker-end="url(#{marker})"' if marker else ""
        s.add(f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"{da}{m}/>')
    def chip(s,x,y,txt,c=SLATE,fs=11.5):
        w=tw(txt,fs,700)+14
        s.r(x-w/2,y-11,w,19,rx=5,fill="#FFFFFF",stroke=BORDER,sw=1)
        s.t(x,y+3,txt,fs=fs,fill=c,wt=700,anchor="middle")
    def out(s):
        return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" font-family="{FONT}">'
                f'<defs>'
                f'<marker id="ah" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7.5" markerHeight="7.5" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="{NAVY}"/></marker>'
                f'<marker id="ao" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7.5" markerHeight="7.5" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="{ORANGE}"/></marker>'
                f'<marker id="as" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="{SF}"/></marker>'
                f'</defs>'+"".join(s.b)+"</svg>")

def cloud(x,y,sc,c):
    return (f'<path transform="translate({x},{y}) scale({sc})" fill="{c}" d="M20 8a7 7 0 0 0-13-2 6 6 0 0 0-6 6 6 6 0 0 0 6 6h13a5 5 0 0 0 0-10z"/>')

s=S()
s.r(0,0,W,H,fill=BG)
s.add(cloud(56,30,1.5,ORANGE))
s.t(96,52,"Cloud Alpacas — System Architecture",fs=27,fill=NAVY,wt=800)
s.t(96,78,"cloud-alpacas Org · Enterprise · Production   |   2026-08-31 실제 구현 기준   ·   근거: 05_ARCHITECTURE.md",fs=13,fill=SLATE,wt=500)

# value-flow ribbon
ry,rh=96,40; rx0,rx1=56,W-56
steps=["데이터 통합","팬·기업 이해","AI · Automation 실행","고객 경험 · 비즈니스 성과"]
seg=(rx1-rx0)/len(steps)
for i,st in enumerate(steps):
    x=rx0+i*seg; hot=i>=2
    s.r(x+3,ry,seg-6,rh,rx=9,fill=(ORANGE_BG if hot else "#ECEFF3"),stroke=(ORANGE if hot else BORDER),sw=1.2)
    s.t(x+seg/2,ry+rh/2+5,st,fs=15,fill=(ORANGE_DK if hot else NAVY2),wt=700,anchor="middle")
    if i<len(steps)-1:
        s.add(f'<path d="M {x+seg-3} {ry+rh/2-6} L {x+seg+7} {ry+rh/2} L {x+seg-3} {ry+rh/2+6}" fill="{MUTE}"/>')

# ---- geometry ----
TOP,BOT=170,980
EX,EW=56,336
PX,PW=522,904
BX,BW=1502,362

# ================= CENTER : SALESFORCE PLATFORM =================
s.r(PX,TOP,PW,BOT-TOP,rx=20,fill=SF_BG,stroke=SF,sw=2.6)
s.add(cloud(PX+24,TOP+16,1.5,SF))
s.t(PX+64,TOP+38,"SALESFORCE PLATFORM",fs=20,fill=NAVY,wt=800,ls="0.5")
s.t(PX+PW-22,TOP+38,"cloud-alpacas Org · 팀 제작 구현",fs=12,fill=SF,wt=700,anchor="end")

layers=[
 ("Experience Layer","누가 · 어디서 접근",BLUE_BG,BLUE,
  ["Lightning Experience (FRM Manager · 파트너 담당자)  ·  PRM 파트너 포털 (prm* LWC 13)",
   "FanQuiz Site · Partnership Inquiry Site (Guest Profile 2)  ·  Fan App ingest"]),
 ("Data / CRM Layer","무엇을 저장하는가",BLUE_BG,BLUE,
  ["Standard Objects — Account · Contact · Lead · Opportunity · Order/OrderItem · Product2 · Campaign · Case",
   "17 Custom Objects (Season·Admission·Engagement·Recommendations·Interaction Intelligence·PRM …)  ·  DART_Setting__c  ·  RecordType 12"]),
 ("Automation Layer","언제 자동으로 반응하는가  ·  Flow 우선 / Trigger 최소",ORANGE_BG,ORANGE,
  ["40 Active Flows — Record-triggered · AutoLaunched · Platform-Event-triggered",
   "Platform Event  Fan_Campaign_Msg_Request__e"]),
 ("Application / Code Layer","복잡한 로직 · 화면 부품",GREY_BG,GREY,
  ["100 Apex Classes — LWC Controller · Agent Action · Invocable · Queueable",
   "1 Apex Trigger  LeadConvertPartnerContact    ·    46 LWC"]),
 ("AI Layer — Agentforce","판단 · 생성을 돕는다  ·  Human-in-the-loop",ORANGE_BG,ORANGE,
  ["5 Agentforce Agents — VIP Recommendation · Opportunity · Negotiation · Sponsorship Proposal · Sponsorship Campaign",
   "6 Prompt Templates    ·    출력은 항상 레코드로 저장 (Recommendations__c · Interaction_Intelligence__c · Sales_Briefing__c)"]),
]
lx=PX+22; lw=PW-44
reg_y0=TOP+58; reg_y1=BOT-46
bh=112
gap=(reg_y1-reg_y0-bh*len(layers))/(len(layers)-1)
band=[]
for i,(name,sub,bg,bd,items) in enumerate(layers):
    y=reg_y0+i*(bh+gap)
    band.append((y,y+bh))
    s.r(lx,y,lw,bh,rx=11,fill=bg,stroke=bd,sw=1.6)
    s.add(f'<rect x="{lx}" y="{y}" width="6" height="{bh}" rx="3" fill="{bd}"/>')
    s.t(lx+20,y+28,f"{i+1}. {name}",fs=15.5,fill=NAVY,wt=800)
    s.t(lx+24+tw(f'{i+1}. {name}',15.5,800),y+28,"  "+sub,fs=11,fill=SLATE,wt=500)
    for j,it in enumerate(items):
        s.t(lx+20,y+52+j*18,it,fs=11,fill=INK,wt=400)

# down-flow chevrons (L1→L5), centered
cx=PX+PW/2
for i in range(len(layers)-1):
    yy=(band[i][1]+band[i+1][0])/2
    s.add(f'<path d="M {cx-7} {yy-4} L {cx} {yy+4} L {cx+7} {yy-4}" stroke="{NAVY2}" stroke-width="2.4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')

# AI -> Data writeback (inside right gutter)
ai_cy=(band[4][0]+band[4][1])/2
da_cy=(band[1][0]+band[1][1])/2
gx=lx+lw-10
s.path(f"M {gx} {ai_cy} L {gx+14} {ai_cy} L {gx+14} {da_cy} L {gx} {da_cy}",stroke=ORANGE,sw=2.2,marker="ao")
midw=(band[1][1]+band[2][0])/2
s.chip(gx-70,(band[2][1]+band[3][0])/2,"AI 출력 → 레코드 저장",ORANGE_DK)

# substrate
sy=BOT-40
s.r(lx,sy,lw,30,rx=8,fill="#FFFFFF",stroke=BORDER,sw=1,dash="4 4")
s.t(lx+14,sy+20,"기반(substrate): 55 관리형 패키지 + SDO/QBrix 데모 (FSL · Maps · Pardot · Marketing Cloud · Sales Planning) — 대부분 미사용",
    fs=11,fill=MUTE,wt=500)

# ================= LEFT : EXTERNAL SYSTEMS =================
s.t(EX,TOP-12,"EXTERNAL SYSTEMS",fs=14,fill=NAVY,wt=800,ls="1")
exts=[
 ("Fan App", "Demo 데이터 채널 — 티켓·입장·굿즈·관심 이벤트 전달 (업무 UI 아님)",
  "→ REST upsert · External_ID__c · API user", "in"),
 ("OpenDART API","opendart.fss.or.kr · 금융감독원 전자공시 (RemoteSite opendart_fss)",
  "→ REST GET · Apex HTTP callout", "in"),
 ("Slack Workspace","이행 지연 등 Flow 알림 (sfdc_slack PS · 채널 ID 미검증)",
  "← Flow → Slack action", "out"),
 ("Agent API","api.salesforce.com (사용처 상세 미확인)",
  "⇄ Named Credential CA_Agent_API · SecuredEndpoint", "bi"),
]
eh,eg=150,24
ecy=[]
for i,(nm,desc,method,dr) in enumerate(exts):
    y=TOP+6+i*(eh+eg); ecy.append(y+eh/2)
    s.r(EX,y,EW,eh,rx=14,fill=CARD,stroke=NAVY2,sw=1.7)
    s.add(f'<circle cx="{EX+24}" cy="{y+27}" r="11" fill="{NAVY}"/>')
    s.t(EX+44,y+32,nm,fs=15.5,fill=NAVY,wt=800)
    yy=y+58
    for ln in wrap(desc,EW-32,11.5): s.t(EX+18,yy,ln,fs=11.5,fill=SLATE,wt=400); yy+=16
    mc={"in":NAVY2,"out":ORANGE_DK,"bi":SF}[dr]
    for ln in wrap(method,EW-32,11.5,700): s.t(EX+18,yy+8,ln,fs=11.5,fill=mc,wt=700); yy+=15

def bcy(i): return (band[i][0]+band[i][1])/2
def conn(x1,y1,x2,y2,c,mk,short,mxf=0.5):
    mx=x1+(x2-x1)*mxf
    if abs(y1-y2)<6:
        s.path(f"M {x1} {y1} L {x2} {y2}",stroke=c,sw=2.3,marker=mk)
        s.chip((x1+x2)/2,y1-13,short,c)
    else:
        s.path(f"M {x1} {y1} L {mx} {y1} L {mx} {y2} L {x2} {y2}",stroke=c,sw=2.3,marker=mk)
        s.chip((x1+mx)/2,y1-13,short,c)

conn(EX+EW, ecy[0], PX, bcy(1), NAVY2, "ah", "REST upsert", 0.42)
conn(EX+EW, ecy[1], PX, bcy(3), NAVY2, "ah", "Apex callout", 0.80)
conn(PX, bcy(2), EX+EW, ecy[2], ORANGE, "ao", "Flow → Slack")
mx=EX+EW+(PX-EX-EW)*0.5
s.path(f"M {PX} {bcy(4)} L {mx} {bcy(4)} L {mx} {ecy[3]} L {EX+EW} {ecy[3]}",stroke=SF,sw=2.3,marker="as")
s.chip((EX+EW+mx)/2, ecy[3]-13, "Named Cred", SF)

# ================= RIGHT : BUSINESS OUTCOME =================
s.t(BX+BW,TOP-12,"BUSINESS OUTCOME",fs=14,fill=NAVY,wt=800,ls="1",anchor="end")
outs=[
 ("Fan 360","신규 팬 이해 → 개인화 액션 → 충성 팬 육성 → Fan LTV ↑",
  "Data 11 Custom Obj · Automation 17 Flow · AI VIP Agent · Experience"),
 ("B2B Sponsorship","팬덤 광고가치 발견 → DART 기업 매칭 → Lead → Opportunity → 스폰서십 계약·이행",
  "Data 6 Custom Obj · Automation 15 Flow · AI 3 Agent · Integration (DART/Slack)"),
 ("PRM","파트너 담당자 영업 생산성 — 브리핑 · 파이프라인 · 목표",
  "Experience (PRM 포털) · AI (Sales Briefing Prompt) · Data (Sales_Briefing__c)"),
]
oh,og=210,28
for i,(nm,goal,sup) in enumerate(outs):
    y=TOP+6+i*(oh+og)
    s.r(BX,y,BW,oh,rx=14,fill=NAVY)
    s.add(f'<rect x="{BX}" y="{y}" width="6" height="{oh}" rx="3" fill="{ORANGE}"/>')
    s.t(BX+22,y+36,nm,fs=18,fill="#FFFFFF",wt=800)
    yy=y+64
    for ln in wrap(goal,BW-42,13,600): s.t(BX+22,yy,ln,fs=13,fill="#FFFFFF",wt=600); yy+=20
    yy+=8
    for ln in wrap(sup,BW-42,11.5): s.t(BX+22,yy,ln,fs=11.5,fill="#A9B4C3",wt=400); yy+=16
    s.path(f"M {PX+PW} {y+oh/2} L {BX} {y+oh/2}",stroke=ORANGE,sw=2.3,marker="ao")

# ================= LEGEND + OUT OF SCOPE =================
gy=1000
s.t(56,gy+4,"범례",fs=12.5,fill=NAVY,wt=800,ls="1")
x=98
for t,label in [("d","데이터 / API 흐름"),("o","Flow → 외부 (Slack)"),("s","Named Credential"),
                ("v","Salesforce 내부 Layer 흐름 (L1→L5)"),("w","AI 출력 → 레코드 저장")]:
    col={"d":NAVY2,"o":ORANGE,"s":SF,"v":NAVY2,"w":ORANGE}[t]
    mk={"d":"ah","o":"ao","s":"as","v":"ah","w":"ao"}[t]
    s.path(f"M {x} {gy-4} L {x+24} {gy-4}",stroke=col,sw=2.4,marker=mk)
    x+=30; s.t(x,gy,label,fs=12,fill=INK,wt=500); x+=tw(label,12,500)+26

s.t(56,gy+32,"Out of Scope",fs=12.5,fill=ORANGE_DK,wt=800)
s.t(158,gy+32,"Marketing Cloud · Pardot · Data Cloud (패키지만 설치 · 팀 미구현)    ·    결제 PG 없음 (Order.Payment_Status__c 필드로만 표현)",
    fs=12,fill=SLATE,wt=500)
s.t(W-56,gy+32,"세부 Object 관계 → 01_ERD.md   ·   프로세스 흐름 → 04_PROCESS_FLOW.md",fs=11.5,fill=MUTE,wt=500,anchor="end")

open(os.path.join(OUT,"CLOUD_ALPACAS_ARCHITECTURE.svg"),"w").write(s.out())
print("wrote CLOUD_ALPACAS_ARCHITECTURE.svg")
