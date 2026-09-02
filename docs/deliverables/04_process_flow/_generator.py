#!/usr/bin/env python3
# Cloud Alpacas — 프로세스 흐름도 SVG generator  (v2)
# Source of truth: cloudalpacas-org-inventory/docs/deliverables/04_PROCESS_FLOW.md
import os, html

OUT = os.path.join(os.path.dirname(__file__), "svg")
os.makedirs(OUT, exist_ok=True)
W, H = 1920, 1080

# ---- Cloud Alpacas palette ----
NAVY="#16294F"; NAVY2="#2E4E93"
ORANGE="#EC6A22"; ORANGE_DK="#B24B12"; ORANGE_BG="#FCE9D8"
BLUE="#0B62B0"; BLUE_BG="#E7F1FB"
GREEN="#1E8A5B"; GREEN_BG="#E3F3EC"
INK="#1E2532"; SLATE="#59626F"; MUTE="#8A93A2"
BORDER="#D3DAE4"; LANE_A="#F7F9FC"; LANE_B="#EFF3F8"
PAIN="#BC3B22"; PAIN_BG="#FAE9E3"
PLUM="#6A4A9C"; PLUM_BG="#EFEAF6"
NOTE_BG="#FFF7E4"; NOTE_BD="#E6C980"
FONT="'Helvetica Neue',Arial,'Apple SD Gothic Neo','Malgun Gothic',sans-serif"

def esc(s): return html.escape(str(s), quote=True)

def tw(s, fs, wt=400):
    w=0.0
    for ch in s:
        o=ord(ch)
        if o<0x1100: w+=fs*0.545
        else: w+=fs*1.0
    return w*(1.04 if wt>=600 else 1.0)

def wrap(s, maxw, fs, wt=400):
    out=[]; cur=""
    for wd in s.split(" "):
        t=wd if not cur else cur+" "+wd
        if tw(t,fs,wt)<=maxw or not cur:
            cur=t
        else:
            out.append(cur); cur=wd
    if cur: out.append(cur)
    return out

class SVG:
    def __init__(s): s.b=[]
    def add(s,x): s.b.append(x)
    def text(s,x,y,t,fs=18,fill=INK,wt=400,anchor="start",ls="0",op=1):
        s.add(f'<text x="{x:.1f}" y="{y:.1f}" font-size="{fs}" fill="{fill}" '
              f'font-weight="{wt}" text-anchor="{anchor}" letter-spacing="{ls}" opacity="{op}">{esc(t)}</text>')
    def rect(s,x,y,w,h,rx=0,fill="none",stroke="none",sw=1,dash=None,op=1):
        d=f' stroke-dasharray="{dash}"' if dash else ""
        s.add(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" '
              f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d} opacity="{op}"/>')
    def line(s,x1,y1,x2,y2,stroke=NAVY,sw=2,dash=None):
        d=f' stroke-dasharray="{dash}"' if dash else ""
        s.add(f'<path d="M {x1:.1f} {y1:.1f} L {x2:.1f} {y2:.1f}" fill="none" stroke="{stroke}" '
              f'stroke-width="{sw}" stroke-linecap="round"{d}/>')
    def path(s,d,stroke=NAVY,sw=2,dash=None,marker="ah"):
        da=f' stroke-dasharray="{dash}"' if dash else ""
        m=f' marker-end="url(#{marker})"' if marker else ""
        s.add(f'<path d="{d}" fill="none" stroke="{stroke}" stroke-width="{sw}" '
              f'stroke-linecap="round" stroke-linejoin="round"{da}{m}/>')
    def out(s):
        return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
                f'font-family="{FONT}"><defs>'
                f'<marker id="ah" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" '
                f'orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="{NAVY}"/></marker>'
                f'<marker id="aho" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" '
                f'orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="{ORANGE}"/></marker>'
                f'<marker id="ahg" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" '
                f'orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="{MUTE}"/></marker>'
                f'</defs>'+"".join(s.b)+"</svg>")

FLOW_X0, FLOW_X1 = 244, 1884
LBL_X = 40
LANE_Y0_R, LANE_Y0_N = 176, 132
LANE_Y1 = 986

KIND = {
 "start": dict(fill=NAVY,stroke=NAVY,title="#FFFFFF",pill=1),
 "end":   dict(fill=GREEN,stroke=GREEN,title="#FFFFFF",pill=1),
 "step":  dict(fill="#FFFFFF",stroke=NAVY2,title=NAVY),
 "human": dict(fill="#FFFFFF",stroke=NAVY2,title=NAVY,tag="사람 판단·실행",tagc=NAVY2,sw=1.9),
 "object":dict(fill=BLUE_BG,stroke=BLUE,title=NAVY,tag="OBJECT",tagc=BLUE),
 "flow":  dict(fill="#FFFFFF",stroke=ORANGE,title=NAVY,tag="FLOW",tagc=ORANGE_DK,bar=ORANGE),
 "apex":  dict(fill="#FFFFFF",stroke=ORANGE,title=NAVY,tag="APEX",tagc=ORANGE_DK,bar=ORANGE),
 "event": dict(fill="#FFFFFF",stroke=ORANGE,title=NAVY,tag="PLATFORM EVENT",tagc=ORANGE_DK,bar=ORANGE),
 "agent": dict(fill=ORANGE_BG,stroke=ORANGE,title=ORANGE_DK,tag="AGENTFORCE",tagc=ORANGE_DK,sw=2.3),
 "prompt":dict(fill=ORANGE_BG,stroke=ORANGE,title=ORANGE_DK,tag="PROMPT",tagc=ORANGE_DK,dash="5 4"),
 "ext":   dict(fill="#FFFFFF",stroke=MUTE,title=SLATE,tag="EXTERNAL",tagc=MUTE,dash="5 4"),
 "slack": dict(fill=PLUM_BG,stroke=PLUM,title=PLUM,tag="SLACK",tagc=PLUM),
 "pain":  dict(fill=PAIN_BG,stroke=PAIN,title=PAIN,tag=None),
 "note":  dict(fill=NOTE_BG,stroke=NOTE_BD,title="#7A5712",dash="4 4"),
 "decision": dict(fill="#FFF9F2",stroke=ORANGE,title=NAVY),
}

def L(label, w=1, **kw): d=dict(label=label,w=w); d.update(kw); return d

class Node:
    def __init__(s,nid,lane,col,title,kind="step",chips=None,row=0,wspan=1,h=None):
        s.id=nid;s.lane=lane;s.col=col;s.title=title;s.kind=kind
        s.chips=chips or [];s.row=row;s.wspan=wspan;s.hfix=h

class Edge:
    def __init__(s,a,b,kind="solid",label=None,ports=None,chan=0):
        s.a=a;s.b=b;s.kind=kind;s.label=label;s.ports=ports;s.chan=chan

def render(spec, fname):
    s=SVG()
    mode=spec["mode"]; lanes=spec["lanes"]; cols=spec["cols"]
    ncol=len(cols); nlane=len(lanes)
    ribbon=spec.get("ribbon", "phases" in spec)
    lane_y0 = LANE_Y0_R if ribbon else LANE_Y0_N
    flow_w=FLOW_X1-FLOW_X0; colW=flow_w/ncol
    lane_h_total=min(LANE_Y1-lane_y0, nlane*(384 if nlane<=2 else 340))
    Y1=lane_y0+lane_h_total
    wsum=sum(l["w"] for l in lanes)
    lane_y=[lane_y0]
    for l in lanes: lane_y.append(lane_y[-1]+lane_h_total*l["w"]/wsum)

    s.rect(0,0,W,H,fill="#FFFFFF")

    # wordmark + title
    s.text(48,44,"☁  CLOUD ALPACAS",fs=14,fill=NAVY,wt=800,ls="2")
    s.text(48,74,spec["kicker"],fs=14.5,fill=ORANGE_DK,wt=700,ls="1.2")
    s.text(48,110,spec["headline"],fs=27,fill=NAVY,wt=700)
    mb=("As-Is · 현재 프로세스" if mode=="AS-IS" else "To-Be · Salesforce 적용")
    mc,mg=((PAIN,PAIN_BG) if mode=="AS-IS" else (GREEN,GREEN_BG))
    bw=tw(mb,16,700)+40
    s.rect(W-48-bw,40,bw,38,rx=19,fill=mg,stroke=mc,sw=1.5)
    s.text(W-48-bw/2,64,mb,fs=16,fill=mc,wt=700,anchor="middle")

    # ribbon (aligned to columns)
    if ribbon:
        ph=spec["phases"]; ry,rh=124,40
        for i,(lbl,hot) in enumerate(ph):
            x=FLOW_X0+i*colW
            s.rect(x+4,ry,colW-8,rh,rx=8,
                   fill=(ORANGE_BG if hot else "#ECF0F6"),
                   stroke=(ORANGE if hot else BORDER),sw=1.2)
            s.text(x+colW/2,ry+rh/2+5,lbl,fs=15,
                   fill=(ORANGE_DK if hot else SLATE),wt=700,anchor="middle")
            if i<ncol-1:
                s.add(f'<path d="M {x+colW-5} {ry+rh/2-6} L {x+colW+5} {ry+rh/2} L {x+colW-5} {ry+rh/2+6}" fill="{MUTE}"/>')

    # lane bands + left labels
    for li,ln in enumerate(lanes):
        y0,y1=lane_y[li],lane_y[li+1]; mid=(y0+y1)/2
        s.rect(FLOW_X0,y0,flow_w,y1-y0,fill=(LANE_A if li%2==0 else LANE_B))
        s.rect(LBL_X,y0+7,FLOW_X0-LBL_X-12,y1-y0-14,rx=10,
               fill=ln.get("bg","#FFFFFF"),stroke=ln.get("bd",BORDER),sw=1.5)
        ic=ln.get("accent",NAVY2)
        s.add(f'<circle cx="{LBL_X+24}" cy="{mid-14}" r="12" fill="{ic}"/>')
        s.text(LBL_X+24,mid-9,ln.get("glyph","•"),fs=12.5,fill="#FFFFFF",wt=800,anchor="middle")
        ll=wrap(ln["label"],FLOW_X0-LBL_X-32,15.5,700)
        for k,seg in enumerate(ll):
            s.text(LBL_X+16,mid+14+k*19,seg,fs=15,fill=NAVY,wt=700)
        if ln.get("note"):
            s.text(LBL_X+16,mid+14+len(ll)*19+4,ln["note"],fs=12,fill=SLATE)
    for y in lane_y:
        s.line(FLOW_X0,y,FLOW_X1,y,stroke=BORDER,sw=1)
    s.rect(FLOW_X0,lane_y0,flow_w,Y1-lane_y0,fill="none",stroke=BORDER,sw=1.4,rx=4)
    for c in range(1,ncol):
        x=FLOW_X0+c*colW
        s.add(f'<path d="M {x} {lane_y0} L {x} {Y1}" stroke="{BORDER}" stroke-width="1" stroke-dasharray="2 7"/>')

    # layout nodes
    nodes={n.id:n for n in spec["nodes"]}
    rows={}
    for n in spec["nodes"]:
        rows[n.lane]=max(rows.get(n.lane,1),n.row+1)
    for n in spec["nodes"]:
        k=KIND[n.kind]
        n.w=colW*n.wspan-30
        n.x=FLOW_X0+n.col*colW+15
        fs_t=16
        n._tl=[]
        for _p in n.title.split("\n"): n._tl+=wrap(_p,n.w-28,fs_t,700)
        n._cl=[]
        for c in n.chips: n._cl+=wrap(c,n.w-26,11.5,500)
        tag=k.get("tag")
        hh=12+(16 if tag else 0)+len(n._tl)*20+(len(n._cl)*15+6 if n._cl else 0)+12
        n.h=n.hfix or max(56,hh)
        if n.kind=="decision": n.h=108
        rL=rows[n.lane]; y0,y1=lane_y[n.lane],lane_y[n.lane+1]
        rowH=(y1-y0)/rL
        n.y=y0+n.row*rowH+(rowH-n.h)/2
        n.y=max(y0+6,min(n.y,y1-n.h-6))
        n.cx=n.x+n.w/2; n.cy=n.y+n.h/2
        n._tag=tag; n._fs=fs_t

    def anc(n,p):
        return {"r":(n.x+n.w,n.cy),"l":(n.x,n.cy),"t":(n.cx,n.y),"b":(n.cx,n.y+n.h)}[p]

    # edges
    for e in spec["edges"]:
        a,b=nodes[e.a],nodes[e.b]
        col={"solid":NAVY,"auto":ORANGE,"dash":MUTE}[e.kind]
        mk={"solid":"ah","auto":"aho","dash":"ahg"}[e.kind]
        dash="6 5" if e.kind=="dash" else None
        sw=2.5 if e.kind=="auto" else 2.0
        if e.ports: pa,pb=e.ports
        elif b.col>a.col: pa,pb="r","l"
        elif b.col<a.col:
            if b.lane>a.lane: pa,pb="b","t"
            elif b.lane<a.lane: pa,pb="t","b"
            else: pa,pb="b","b"
        elif b.row>a.row: pa,pb="b","t"
        elif b.row<a.row: pa,pb="t","b"
        else: pa,pb="r","l"
        ax,ay=anc(a,pa); bx,by=anc(b,pb)
        H_=("r","l"); V_=("t","b")
        if pa in H_ and pb in H_:
            mx=(ax+bx)/2 if ((pa=="r" and bx>ax) or (pa=="l" and bx<ax)) else ax+(30 if pa=="r" else -30)
            d=f"M {ax} {ay} L {bx} {by}" if abs(ay-by)<3 else f"M {ax} {ay} L {mx} {ay} L {mx} {by} L {bx} {by}"
        elif pa in V_ and pb in V_:
            if pa=="b" and pb=="b":
                cy=Y1+14+e.chan*15
                d=f"M {ax} {ay} L {ax} {cy} L {bx} {cy} L {bx} {by}"
            elif pa=="t" and pb=="t":
                cy=lane_y0+12+e.chan*14
                d=f"M {ax} {ay} L {ax} {cy} L {bx} {cy} L {bx} {by}"
            else:
                my=(ay+by)/2
                d=f"M {ax} {ay} L {bx} {by}" if abs(ax-bx)<3 else f"M {ax} {ay} L {ax} {my} L {bx} {my} L {bx} {by}"
        elif pa in H_ and pb in V_:
            d=f"M {ax} {ay} L {bx} {ay} L {bx} {by}"
        else:  # V -> H
            d=f"M {ax} {ay} L {ax} {by} L {bx} {by}"
        s.path(d,stroke=col,sw=sw,dash=dash,marker=mk)
        if e.label:
            if pa=="r": lx,ly,an=ax+10,ay-8,"start"
            elif pa=="l": lx,ly,an=ax-10,ay-8,"end"
            elif pa=="b": lx,ly,an=ax+9,(ay+by)/2,"start"
            else: lx,ly,an=ax+9,(ay+by)/2,"start"
            wd=tw(e.label,12,700)
            rx0=lx-5 if an=="start" else lx-wd-5
            s.rect(rx0,ly-13,wd+10,18,rx=4,fill="#FFFFFF",op=0.9)
            s.text(lx,ly,e.label,fs=12,fill=(ORANGE_DK if e.kind=="auto" else SLATE),wt=700,anchor=an)

    # nodes
    for n in spec["nodes"]:
        k=KIND[n.kind]
        if n.kind=="decision":
            hw=min(n.w/2,108); hh=52
            cx,cy=n.cx,n.cy
            s.add(f'<path d="M {cx} {cy-hh} L {cx+hw} {cy} L {cx} {cy+hh} L {cx-hw} {cy} z" '
                  f'fill="#FFF7EE" stroke="{ORANGE}" stroke-width="2"/>')
            dl=wrap(n.title.replace("\n"," "),hw*1.75,14,700)
            for i,seg in enumerate(dl):
                s.text(cx,cy-(len(dl)-1)*9+i*17+5,seg,fs=14,fill=NAVY,wt=700,anchor="middle")
            continue
        pill=k.get("pill"); rx=n.h/2 if pill else 12
        s.rect(n.x,n.y,n.w,n.h,rx=rx,fill=k["fill"],stroke=k["stroke"],sw=k.get("sw",1.7),dash=k.get("dash"))
        if k.get("bar"):
            s.add(f'<path d="M {n.x+3} {n.y+9} L {n.x+3} {n.y+n.h-9}" stroke="{k["bar"]}" stroke-width="5" stroke-linecap="round"/>')
        ty=n.y+22
        if n._tag:
            s.text(n.x+16,ty,k["tag"],fs=10.5,fill=k.get("tagc",SLATE),wt=800,ls="0.7"); ty+=18
        for seg in n._tl:
            s.text(n.cx if pill else n.x+16,ty,seg,fs=n._fs,fill=k["title"],wt=700,
                   anchor=("middle" if pill else "start")); ty+=20
        if n._cl:
            ty+=4
            for seg in n._cl:
                s.text(n.x+16,ty,("· "+seg),fs=12,wt=500,
                       fill=(ORANGE_DK if n.kind in("flow","apex","event","agent","prompt") else SLATE))
                ty+=15

    # legend — horizontal bar
    ly=Y1+34
    s.text(48,ly+4,"범례",fs=12.5,fill=NAVY,wt=800,ls="1")
    x=96
    for t,label in spec["legend"]:
        if t=="obj": s.rect(x,ly-11,24,15,rx=3,fill=BLUE_BG,stroke=BLUE,sw=1.5)
        elif t=="flow": s.rect(x,ly-11,24,15,rx=3,fill="#FFFFFF",stroke=ORANGE,sw=1.7)
        elif t=="agent": s.rect(x,ly-11,24,15,rx=3,fill=ORANGE_BG,stroke=ORANGE,sw=1.7)
        elif t=="human": s.rect(x,ly-11,24,15,rx=3,fill="#FFFFFF",stroke=NAVY2,sw=1.8)
        elif t=="pain": s.rect(x,ly-11,24,15,rx=3,fill=PAIN_BG,stroke=PAIN,sw=1.5)
        elif t=="ext": s.rect(x,ly-11,24,15,rx=3,fill="#FFFFFF",stroke=MUTE,sw=1.4,dash="4 3")
        elif t=="slack": s.rect(x,ly-11,24,15,rx=3,fill=PLUM_BG,stroke=PLUM,sw=1.5)
        elif t=="e_solid": s.line(x,ly-4,x+24,ly-4,stroke=NAVY,sw=2.4)
        elif t=="e_auto": s.line(x,ly-4,x+24,ly-4,stroke=ORANGE,sw=2.8)
        elif t=="e_dash": s.line(x,ly-4,x+24,ly-4,stroke=MUTE,sw=2,dash="5 4")
        x+=32
        s.text(x,ly,label,fs=12.5,fill=INK,wt=500)
        x+=tw(label,12.5,500)+26

    s.text(48,max(H-26,Y1+70),spec.get("foot",""),fs=12,fill=MUTE,wt=500)

    open(os.path.join(OUT,fname),"w").write(s.out())
    print("wrote",fname)

# ===========================================================================
# P1 — Fan 가입 → 데이터 축적 → Segment / Engagement
# ===========================================================================
P1_ASIS=dict(mode="AS-IS",
 kicker="P1 · FAN 가입 → 데이터 축적 → SEGMENT / ENGAGEMENT",
 headline="팬 데이터가 채널마다 흩어지고, 팬 등급은 수기·주관적으로 매겨진다",
 phases=[("① 팬 활동",False),("② 분산된 채널",False),("③ 수기 취합",False),("④ 주관적 등급",False)],
 lanes=[L("이루키 (Fan)",w=1,glyph="F",accent=NAVY2),
        L("운영 채널 (분산)",w=1,glyph="!",accent=MUTE,note="채널 간 연결 없음"),
        L("FRM 담당자",w=1,glyph="M",accent=NAVY2)],
 cols=["a","b","c","d"],
 nodes=[
  Node("f1",0,0,"티켓 예매 / 굿즈 구매","step"),
  Node("f2",0,1,"경기장 입장","step"),
  Node("f3",0,2,"SNS 반응 · 관심 표현","step"),
  Node("c1",1,0,"예매 시스템","pain"),
  Node("c2",1,1,"게이트 · 입장 기록","pain"),
  Node("c3",1,2,"굿즈 POS / SNS","pain"),
  Node("m1",2,1,"엑셀로 수기 취합","pain",chips=["채널별로 따로 내려받아 붙여넣기"]),
  Node("m2",2,2,"감으로 팬 등급 부여","pain",chips=["기준이 담당자마다 다름"]),
  Node("m3",2,3,"‘몇 번 왔는지’와 ‘언제 왔는지’를 구분해서 볼 수 없음","note"),
 ],
 edges=[
  Edge("f1","f2"),Edge("f2","f3"),
  Edge("f1","c1","dash"),Edge("f2","c2","dash"),Edge("f3","c3","dash"),
  Edge("c1","m1","dash"),Edge("c2","m1","dash"),Edge("c3","m1","dash"),
  Edge("m1","m2"),Edge("m2","m3"),
 ],
 legend=[("pain","분산·수작업으로 생기는 문제 지점"),("e_solid","업무 흐름"),
         ("e_dash","채널 → 담당자 수동 취합")],
 foot="As-Is · 문제: 데이터 분산 · 수기 등급 · 횟수와 시점 미분리    |    출처 04_PROCESS_FLOW.md — P1 As-Is",
)

P1_TOBE=dict(mode="TO-BE",
 kicker="P1 · FAN 가입 → 데이터 축적 → SEGMENT / ENGAGEMENT",
 headline="입장·구매·관심 이벤트를 Flow가 자동 집계해 팬 등급·세그먼트를 산출한다",
 phases=[("데이터 유입",False),("트랜잭션 기록",False),("활동 패턴 분석",False),
         ("등급·점수 산출",True),("세그먼트 확정",True)],
 lanes=[L("이루키 (Fan)",w=0.9,glyph="F",accent=NAVY2),
        L("Fan App",w=0.9,glyph="A",accent=MUTE,note="Demo 데이터 채널"),
        L("Salesforce · Flow / Apex",w=2.6,glyph="S",accent=ORANGE,bg=ORANGE_BG,bd=ORANGE,note="자동화 영역")],
 cols=["c0","c1","c2","c3","c4"],
 nodes=[
  Node("a1",0,0,"티켓 예매 / 굿즈 구매","step"),
  Node("a2",0,1,"경기장 입장","step"),
  Node("a3",0,2,"SNS 관심 · 반응","step"),
  Node("b1",1,0,"구매·입장·관심 이벤트 발생","step",chips=["External_ID__c 로 Salesforce 전달"]),
  Node("c1",2,0,"Account (Fan · Person Account)","object",chips=["Flow: Start Upsert Flow"]),
  Node("c2",2,1,"Order + OrderItem","object",chips=["Flow: Order Paid"]),
  Node("c3",2,1,"Admission__c","object",row=1,chips=["Flow: Admission Created"]),
  Node("c5",2,2,"Engagement_Signal__c","object",chips=["SNS 관심 신호 적재"]),
  Node("c4",2,2,"Attendance_Record__c","object",row=1,
       chips=["Roll-Up · Total_Admissions__c","First / Last_Admission_Date__c"]),
  Node("c6",2,3,"Fan_Activity_Pattern__c","object",
       chips=["Flow: Fan Activity Pattern Admission Update"]),
  Node("c9",2,3,"Account 등급·점수 갱신","flow",row=1,
       chips=["Current_Segment__c · Fan_Value_Tier__c · Engagement_Score__c",
              "Flow: Fan Value Calc / Start Fan Engagement Calc"]),
  Node("c7",2,4,"세그먼트\n조건 충족?","decision"),
  Node("c8",2,4,"Fan_Segment_History__c","object",row=1,chips=["세그먼트 이동 이력 기록"]),
 ],
 edges=[
  Edge("a1","a2"),Edge("a2","a3"),
  Edge("a2","b1","dash",label="이벤트"),Edge("a3","b1","dash"),
  Edge("b1","c1","auto",label="upsert",ports=("b","t")),
  Edge("b1","c2","auto",ports=("b","t")),
  Edge("c2","c3","solid",ports=("b","t"),label="입장 처리"),
  Edge("b1","c5","auto",label="관심 신호"),
  Edge("c3","c4","auto",ports=("r","l")),
  Edge("c3","c6","auto",ports=("r","l")),
  Edge("c4","c6","auto",ports=("r","t")),
  Edge("c5","c6","auto",ports=("r","l")),
  Edge("c6","c9","auto",ports=("b","t"),label="Fan Value Calc"),
  Edge("c9","c7","solid",ports=("r","l")),
  Edge("c7","c8","solid",ports=("b","t"),label="Yes"),
  Edge("c8","c9","dash",ports=("l","r")),
 ],
 legend=[("obj","Salesforce Object (레코드)"),("flow","Flow / Apex 자동화"),
         ("e_auto","자동 실행 (Flow·Apex)"),("e_solid","업무 흐름"),("e_dash","이벤트 · handoff")],
 foot="To-Be · 개선: 수기 등급 → 데이터 기반 Flow 자동 산출 · 횟수(Total_Admissions__c)와 시점(First/Last_Admission_Date__c) 분리    |    04_PROCESS_FLOW.md — P1 To-Be",
)

# ===========================================================================
# P2 — Fan 분석 → Recommendation → Campaign / Action   (핵심)
# ===========================================================================
P2_ASIS=dict(mode="AS-IS",
 kicker="P2 · FAN 분석 → RECOMMENDATION → CAMPAIGN / ACTION",
 headline="누구에게 무엇을 제안할지 담당자 감(感)에 의존하고, 약속한 혜택에 실체가 없다",
 phases=[("① 팬 목록 검토",False),("② 감으로 선정",False),("③ 구두 약속",False),("④ 추적 불가",False)],
 lanes=[L("김매니저 (FRM Manager)",w=1,glyph="M",accent=NAVY2),
        L("팬 / 결과",w=1,glyph="F",accent=MUTE)],
 cols=["a","b","c","d"],
 nodes=[
  Node("m1",0,0,"팬 목록을 눈으로 훑어봄","pain"),
  Node("m2",0,1,"감으로 VIP 후보 선정","pain",chips=["세그먼트·활동 데이터 근거 없음"]),
  Node("m3",0,2,"구두 / 메시지로 혜택 약속","pain"),
  Node("m4",0,3,"어떤 제안을 했는지 기록이 남지 않음","note"),
  Node("f1",1,2,"혜택 레코드가 생성되지 않음","pain",chips=["‘말은 했는데 실체 없음’"]),
  Node("f2",1,3,"팬: 약속한 혜택이 오지 않음 → 신뢰 저하","pain"),
 ],
 edges=[
  Edge("m1","m2"),Edge("m2","m3"),Edge("m3","m4"),
  Edge("m3","f1","dash",ports=("b","t")),Edge("f1","f2"),
 ],
 legend=[("pain","감·구두 처리로 생기는 문제 지점"),("e_solid","업무 흐름"),("e_dash","실체 없는 handoff")],
 foot="As-Is · 문제: 감에 의존한 제안 · 제안↔혜택 미연결 · 이력 추적 불가    |    04_PROCESS_FLOW.md — P2 As-Is",
)

P2_TOBE=dict(mode="TO-BE",
 kicker="P2 · FAN 분석 → RECOMMENDATION → CAMPAIGN / ACTION   ★ 핵심 흐름",
 headline="데이터 → AI 추천 → 매니저 검토·승인 → 개인화 실행 → 알림 이력까지 한 줄로 추적된다",
 phases=[("Fan Data",False),("VIP 후보 감지",True),("추천·메시지 생성 (AI)",True),
         ("매니저 검토·승인",False),("개인화 실행",True),("알림 · 이력",False)],
 lanes=[L("System · Flow / Event",w=1.3,glyph="S",accent=ORANGE,bg=ORANGE_BG,bd=ORANGE),
        L("VIP Recommendation Agent",w=1.35,glyph="AI",accent=ORANGE,bg=ORANGE_BG,bd=ORANGE,note="+ Prompt Template"),
        L("김매니저 (FRM Manager)",w=1.3,glyph="M",accent=NAVY2,note="Human-in-the-loop")],
 cols=["c0","c1","c2","c3","c4","c5"],
 nodes=[
  Node("d1",0,0,"Fan_Segment_History__c\nFan_Activity_Pattern__c","object"),
  Node("d2",0,1,"VIP 후보\n조건?","decision"),
  Node("d3",0,2,"Recommendations__c","object",chips=["Status = Pending","Flow: VIP Candidate Detection -CA"]),
  Node("d9",0,4,"Campaign (Fan_Campaign) + CampaignMember","object",
       chips=["Welcome / First Ticket … Flow -CA"]),
  Node("d8",0,4,"Benefits__c","object",row=1,chips=["Status / Used_Date — 실제 혜택 레코드"]),
  Node("d7",0,5,"Notification_Log__c","object",chips=["Fan Timeline — 발송·혜택·캠페인 이력"]),
  Node("e1",1,2,"추천 액션 판단","agent",wspan=1.5,
       chips=["Agent: VIP_Recommendation_Agent","Action: GetPendingVipRecommendations"]),
  Node("e2",1,2,"개인화 메시지 생성","prompt",wspan=1.5,row=1,
       chips=["Prompt: Fan_Personalized_Message","Flow: Generate AI Recommendation Message"]),
  Node("f1",2,3,"Recommendation 검토 화면","human",
       chips=["LWC: recommendationReviewPanel · recommendationSegmentDashboard"]),
  Node("f2",2,3,"승인?","decision",row=1),
  Node("f3",2,4,"승인 / 반려","apex",chips=["Apex: ApproveRecommendationAction","→ Recommendations__c 상태 갱신"]),
  Node("f4",2,4,"이메일 발송 실행","apex",row=1,chips=["Apex: SendRecommendationEmailAction"]),
 ],
 edges=[
  Edge("d1","d2","auto",label="감지 Flow"),
  Edge("d2","d3","solid",label="Yes"),
  Edge("d3","e1","solid",ports=("b","t")),
  Edge("e1","e2","solid",ports=("b","t")),
  Edge("e2","d3","auto",ports=("t","b"),label="메시지 저장"),
  Edge("d3","f1","solid",ports=("r","l"),label="검토 (LWC)"),
  Edge("f1","f2","solid",ports=("b","t")),
  Edge("f2","f3","solid",ports=("r","l"),label="Yes"),
  Edge("f3","f4","solid",ports=("b","t")),
  Edge("f3","d8","auto",ports=("t","b"),label="혜택 발급"),
  Edge("f4","d7","auto",ports=("r","l"),label="발송 로그"),
  Edge("d3","d9","dash",ports=("r","l"),label="캠페인 편성"),
  Edge("d9","d7","solid",ports=("r","l")),
  Edge("d8","d7","dash",ports=("r","l"),label="혜택 알림"),
  Edge("d7","f1","dash",ports=("b","t"),chan=0,label="Fan Timeline"),
 ],
 legend=[("obj","Object — 제안·혜택·알림 모두 레코드로 추적"),
         ("agent","Agentforce / Prompt — AI 판단·생성"),
         ("human","매니저가 검토·승인 (사람 판단)"),
         ("e_auto","자동 실행"),("e_dash","알림 · 캠페인 handoff")],
 foot="핵심 흐름:  Fan Data → VIP Candidate Detection → Recommendation → VIP Recommendation Agent → Manager Review → Approval → Personalized Message → Email / Campaign → Notification Log",
)

# ===========================================================================
# P3 — Sponsor 후보(B2B) → Fit → Lead → Opportunity → Sponsorship   (핵심)
# ===========================================================================
P3_ASIS=dict(mode="AS-IS",
 kicker="P3 · SPONSOR 후보(B2B) → FIT → LEAD → OPPORTUNITY → SPONSORSHIP",
 headline="스폰서 후보를 엑셀로 모으고, 팬덤 적합도와 계약 가능성을 구분하지 않는다",
 phases=[("① 후보 발굴",False),("② 엑셀 수집",False),("③ 미팅 진행",False),("④ 개인 메모",False)],
 lanes=[L("파트너 담당자",w=1,glyph="P",accent=NAVY2),
        L("자료 / 결과",w=1,glyph="!",accent=MUTE)],
 cols=["a","b","c","d"],
 nodes=[
  Node("p1",0,0,"뉴스·지인 통해 후보 기업 발굴","pain"),
  Node("p2",0,1,"엑셀에 수기 입력","pain",chips=["적합도와 계약 가능성이 섞임"]),
  Node("p3",0,2,"미팅 진행","step"),
  Node("p4",0,3,"개인 노트에 메모","pain"),
  Node("r1",1,1,"후보 우선순위가 주관적","pain"),
  Node("r2",1,3,"미팅 내용이 흩어져 공유되지 않음","pain"),
  Node("r3",1,3,"파이프라인 가시성 없음","note",row=1),
 ],
 edges=[
  Edge("p1","p2"),Edge("p2","p3"),Edge("p3","p4"),
  Edge("p2","r1","dash",ports=("b","t")),
  Edge("p4","r2","dash",ports=("b","t")),Edge("r2","r3","solid",ports=("b","t")),
 ],
 legend=[("pain","엑셀·개인 메모로 생기는 문제 지점"),("e_solid","업무 흐름"),("e_dash","비공식 handoff")],
 foot="As-Is · 문제: 엑셀 후보 수집 · Fit과 계약 가능성 미분리 · 미팅 메모 분산    |    04_PROCESS_FLOW.md — P3 As-Is",
)

P3_TOBE=dict(mode="TO-BE",
 kicker="P3 · SPONSOR 후보(B2B) → FIT → LEAD → OPPORTUNITY → SPONSORSHIP   ★ 핵심 흐름",
 headline="DART 자동 조회 → Lead Score → Opportunity Agent 코칭 → Sponsorship → PRM 포털까지 연결된다",
 phases=[("External Data · DART",True),("매칭 · Lead Score",True),("Opportunity",False),
         ("Agent 제안·협상 (AI)",True),("Sponsorship",False),("PRM 포털",False)],
 lanes=[L("외부 (OpenDART)",w=0.7,glyph="W",accent=MUTE,note="opendart.fss.or.kr"),
        L("Salesforce · Flow / Apex",w=1.7,glyph="S",accent=ORANGE,bg=ORANGE_BG,bd=ORANGE),
        L("Agentforce + Prompt",w=1.35,glyph="AI",accent=ORANGE,bg=ORANGE_BG,bd=ORANGE),
        L("파트너 담당자",w=1.2,glyph="P",accent=NAVY2,note="사람 판단"),
        L("Slack",w=0.55,glyph="#",accent=PLUM)],
 cols=["c0","c1","c2","c3","c4","c5"],
 nodes=[
  Node("g1",0,0,"OpenDART API","ext",chips=["RemoteSite: opendart_fss"]),
  Node("h1",1,0,"DART_Corp_Mapping__c","object",
       chips=["Apex: DartService / DartMatchService"]),
  Node("h2",1,1,"Account (Business) 보강","flow",
       chips=["DART_* · Match_Confidence__c","Flow: DART 승인 보강"]),
  Node("h3",1,1,"Lead + Lead Score (18필드)","object",row=1,
       chips=["Final_Lead_Score__c · Segment_Match__c","Trigger: LeadConvertPartnerContact"]),
  Node("h4",1,2,"Lead Score 임계 초과?","decision"),
  Node("h5",1,2,"Opportunity (스폰서십 Deal)","object",row=1,
       chips=["Flow: DART Lead 전환 AI매칭"]),
  Node("h6",1,3,"Interaction_Intelligence__c","object",
       chips=["→ Interaction_Signal__c","Flow: CA Generate Meeting Interaction Intelligence"]),
  Node("h7",1,4,"Campaign (Sponsorship_*) + Campaign_Deliverable__c","object"),
  Node("h8",1,5,"Account 롤업","flow",
       chips=["Total_Sponsorship_Value__c 등","Flow: Rollup Sponsorship To Account"]),
  Node("i1",2,1,"Lead 요약","prompt",chips=["Prompt: CA_Lead_AI_Summary","→ Lead.AI_Lead_Summary__c"]),
  Node("i2",2,3,"Opportunity Agent","agent",
       chips=["deal · proposal · negotiation · stage_guidance","Apex: SponsorshipProposalSaver"]),
  Node("i3",2,3,"미팅 인텔리전스","prompt",row=1,chips=["Prompt: CA_Offline_Meeting_*"]),
  Node("i5",2,4,"스폰서십 캠페인 에이전트","agent",chips=["bottleneck · renewal 탐지"]),
  Node("j1",3,1,"후보 검토 / 영업 대상 선정","human"),
  Node("j2",3,3,"미팅 진행 → 활동 기록","human",chips=["Task / Event 저장"]),
  Node("j3",3,3,"제안 / 협상","human",row=1),
  Node("j4",3,5,"PRM 포털에서 파이프라인 확인","human",
       chips=["prm* LWC 13종","Prompt: CA_PRM360_Sales_Briefing"]),
  Node("k1",4,4,"이행 지연 알림","slack",chips=["Deliverable Blocked Slack Alert"]),
 ],
 edges=[
  Edge("g1","h1","auto",label="DartService"),
  Edge("g1","h2","auto",ports=("b","l"),chan=1),
  Edge("h1","i1","solid",ports=("b","l")),
  Edge("h2","h3","solid",ports=("b","t")),
  Edge("h2","j1","solid",ports=("b","t")),
  Edge("i1","h3","solid",ports=("b","t")),
  Edge("j1","h3","solid",label="선정 시만"),
  Edge("h3","h4","auto",label="전환"),
  Edge("h4","h5","solid",ports=("b","t"),label="Yes"),
  Edge("h3","j1","dash",ports=("b","t"),chan=1,label="고득점 리드 연락"),
  Edge("h5","i2","solid",ports=("b","t")),
  Edge("j2","h6","solid",ports=("l","l"),label="Task/Event"),
  Edge("h6","i3","auto",ports=("b","t")),
  Edge("i3","h6","solid",ports=("t","b"),chan=2),
  Edge("j3","i2","solid",ports=("t","b")),
  Edge("i2","h5","auto",ports=("t","b"),chan=0,label="제안·협상 저장"),
  Edge("h5","h7","solid",ports=("r","l"),label="Won"),
  Edge("h7","i5","solid",ports=("b","t")),
  Edge("h7","k1","dash",ports=("b","t"),label="Blocked"),
  Edge("k1","j1","dash",ports=("b","b"),chan=0),
  Edge("h7","h8","solid",ports=("r","l")),
  Edge("h8","j4","solid",ports=("b","t"),label="Sales Briefing"),
 ],
 legend=[("obj","Object (레코드)"),("flow","Flow / Apex"),
         ("agent","Agentforce / Prompt — AI"),("human","파트너 담당자 판단·실행"),
         ("ext","외부 시스템 (OpenDART)"),("slack","Slack 알림"),
         ("e_auto","자동 실행"),("e_dash","알림 · handoff")],
 foot="핵심 흐름:  External Data → DART → Fit / Lead → Opportunity → Agent → Proposal / Negotiation → Sponsorship → PRM",
)

for spec,fn in [
 (P1_ASIS,"P1_Fan_Data_Process_AsIs.svg"),
 (P1_TOBE,"P1_Fan_Data_Process_ToBe.svg"),
 (P2_ASIS,"P2_Recommendation_Process_AsIs.svg"),
 (P2_TOBE,"P2_Recommendation_Process_ToBe.svg"),
 (P3_ASIS,"P3_Sponsorship_Process_AsIs.svg"),
 (P3_TOBE,"P3_Sponsorship_Process_ToBe.svg"),
]:
    render(spec,fn)
