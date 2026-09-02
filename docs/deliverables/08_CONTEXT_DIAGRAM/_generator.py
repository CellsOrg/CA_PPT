#!/usr/bin/env python3
# Cloud Alpacas — Context Diagram  (System Context, hub-and-spoke)
# Source of truth: cloudalpacas-org-inventory/docs/deliverables/08_CONTEXT_DIAGRAM.md
# 원칙: Salesforce 내부(Object/Flow/Apex/LWC/Agentforce/Layer)는 그리지 않는다 — 하나의 Black Box.
#       08_CONTEXT_DIAGRAM.md 에 정의된 외부 주체·관계만 사용한다.
# stdlib only. PNG 는 별도로 SVG 에서 1920x1080 export.
import os, html

HERE = os.path.dirname(os.path.abspath(__file__))
W, H = 1920, 1080

NAVY      = "#07111F"
NAVY_SOFT = "#1F3047"
ORANGE    = "#FC4E00"
ORANGE_DK = "#B23800"
ORANGE_LN = "#EFD2C2"
BG        = "#F6F3F1"
CARD      = "#FFFFFF"
EXT_BG    = "#EEF1F5"
EXT_LN    = "#C6CED9"
INK       = "#1C2430"
SLATE     = "#586173"
MUTE      = "#8A94A2"
LOOP      = "#B7C0CC"
FONT = "'Pretendard','Apple SD Gothic Neo','Helvetica Neue',Arial,'Malgun Gothic',sans-serif"

B = []
def add(x): B.append(x)
def esc(s): return html.escape(str(s), quote=True)

def tw(s, fs, wt=400):
    return sum(fs * (0.56 if ord(c) < 0x1100 else 1.0) for c in s) * (1.03 if wt >= 600 else 1.0)

def wrap(s, mw, fs, wt=400):
    out, cur = [], ""
    for wd in s.split(" "):
        t = wd if not cur else cur + " " + wd
        if tw(t, fs, wt) <= mw or not cur:
            cur = t
        else:
            out.append(cur); cur = wd
    if cur:
        out.append(cur)
    return out

def text(x, y, s, fs=14, fill=INK, wt=400, anchor="start", ls="0", op=1, rot=None):
    tr = f' transform="rotate({rot} {x:.1f} {y:.1f})"' if rot is not None else ""
    add(f'<text x="{x:.1f}" y="{y:.1f}" font-size="{fs}" fill="{fill}" font-weight="{wt}" '
        f'text-anchor="{anchor}" letter-spacing="{ls}" opacity="{op}"{tr}>{esc(s)}</text>')

def rect(x, y, w, h, rx=0, fill="none", stroke="none", sw=1, dash=None, op=1):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    add(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" fill="{fill}" '
        f'stroke="{stroke}" stroke-width="{sw}"{d} opacity="{op}"/>')

def arrow(d, col=NAVY_SOFT, sw=2.0, two=False, dash=None):
    key = {NAVY_SOFT: "n", ORANGE: "o", LOOP: "l"}.get(col, "n")
    st = f' marker-start="url(#a{key}s)"' if two else ""
    da = f' stroke-dasharray="{dash}"' if dash else ""
    add(f'<path d="{d}" fill="none" stroke="{col}" stroke-width="{sw}" stroke-linecap="round" '
        f'stroke-linejoin="round"{da}{st} marker-end="url(#a{key}e)"/>')

def chip(cx, cy, s, fill=SLATE, fs=11):
    w = tw(s, fs, 700) + 16
    rect(cx - w / 2, cy - 10, w, 20, rx=6, fill="#FFFFFF", stroke=EXT_LN, sw=1)
    text(cx, cy + 3.5, s, fs=fs, fill=fill, wt=700, anchor="middle")

def icon_actor(cx, cy, col):
    add(f'<circle cx="{cx}" cy="{cy-4.5}" r="4.1" fill="{col}"/>')
    add(f'<path d="M {cx-7} {cy+8} C {cx-7} {cy-1.5} {cx+7} {cy-1.5} {cx+7} {cy+8} Z" fill="{col}"/>')

def icon_system(cx, cy, col):
    add(f'<rect x="{cx-7.5}" y="{cy-6.5}" width="15" height="13" rx="2.4" fill="none" stroke="{col}" stroke-width="1.8"/>')
    add(f'<line x1="{cx-7.5}" y1="{cy-1.6}" x2="{cx+7.5}" y2="{cy-1.6}" stroke="{col}" stroke-width="1.3"/>')

def icon_data(cx, cy, col):
    add(f'<ellipse cx="{cx}" cy="{cy-5}" rx="7" ry="2.5" fill="none" stroke="{col}" stroke-width="1.7"/>')
    add(f'<path d="M {cx-7} {cy-5} L {cx-7} {cy+5}" stroke="{col}" stroke-width="1.7"/>')
    add(f'<path d="M {cx+7} {cy-5} L {cx+7} {cy+5}" stroke="{col}" stroke-width="1.7"/>')
    add(f'<ellipse cx="{cx}" cy="{cy+5}" rx="7" ry="2.5" fill="none" stroke="{col}" stroke-width="1.7"/>')

_ICON = {"actor": icon_actor, "system": icon_system, "data": icon_data}

def node(x, y, w, h, name, desc, rel, kind):
    is_actor = kind == "actor"
    if is_actor:
        rect(x, y, w, h, rx=14, fill=CARD, stroke=ORANGE_LN, sw=1.7)
        add(f'<rect x="{x:.1f}" y="{y:.1f}" width="5" height="{h}" rx="2.5" fill="{ORANGE}"/>')
        icol = ORANGE_DK
    else:
        rect(x, y, w, h, rx=14, fill=EXT_BG, stroke=EXT_LN, sw=1.5)
        icol = SLATE
    bx, by = x + 27, y + 27
    add(f'<circle cx="{bx}" cy="{by}" r="15" fill="#FFFFFF" stroke="{EXT_LN}" stroke-width="1"/>')
    _ICON[kind](bx, by, icol)
    text(x + 52, y + 26, name, fs=15, fill=NAVY, wt=800)
    yy = y + 49
    for ln in wrap(desc, w - 30, 11):
        text(x + 16, yy, ln, fs=11, fill=SLATE)
        yy += 15
    text(x + 16, yy + 9, rel, fs=10.5, fill=(ORANGE_DK if is_actor else NAVY_SOFT), wt=700)

# ---------------------------------------------------------------- canvas
add(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" font-family="{FONT}">')
add('<defs>')
for key, col in (("n", NAVY_SOFT), ("o", ORANGE), ("l", LOOP)):
    add(f'<marker id="a{key}e" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="7" markerHeight="7" '
        f'orient="auto"><path d="M0 0L10 5L0 10z" fill="{col}"/></marker>')
    add(f'<marker id="a{key}s" viewBox="0 0 10 10" refX="1.5" refY="5" markerWidth="7" markerHeight="7" '
        f'orient="auto"><path d="M10 0L0 5L10 10z" fill="{col}"/></marker>')
add('</defs>')
rect(0, 0, W, H, fill=BG)

# ---------------------------------------------------------------- title
text(64, 58, "CLOUD ALPACAS", fs=13.5, fill=ORANGE, wt=800, ls="3.5")
text(64, 96, "CONTEXT DIAGRAM", fs=33, fill=NAVY, wt=800, ls="0.5")
text(66, 119, "Who surrounds the system?", fs=14.5, fill=SLATE, wt=500)

text(1856, 54, "SYSTEM CONTEXT", fs=12, fill=SLATE, wt=800, ls="2", anchor="end")
text(1856, 76, "Salesforce = one black box", fs=12, fill=SLATE, wt=600, anchor="end")
text(1856, 96, "내부 구조 → 05_ARCHITECTURE.md", fs=11, fill=MUTE, wt=500, anchor="end")
text(1856, 118, "→ 유입    ← 유출    ⇄ 양방향", fs=11, fill=MUTE, wt=600, anchor="end")

# ---------------------------------------------------------------- central black box
cxb, cyb = 960, 492
bw, bh = 540, 240
bx, by = cxb - bw / 2, cyb - bh / 2          # 690, 372 .. 1230, 612
rect(bx - 6, by - 6, bw + 12, bh + 12, rx=22, fill="none", stroke=ORANGE, sw=3)
rect(bx, by, bw, bh, rx=18, fill=NAVY)
add(f'<rect x="{bx}" y="{by}" width="7" height="{bh}" rx="3.5" fill="{ORANGE}"/>')
text(cxb, by + 60, "CLOUD ALPACAS", fs=30, fill="#FFFFFF", wt=800, anchor="middle", ls="1")
text(cxb, by + 88, "Salesforce CRM · Customer 360", fs=14.5, fill="#AEB9C7", wt=600, anchor="middle")
add(f'<line x1="{bx+80}" y1="{by+108}" x2="{bx+bw-80}" y2="{by+108}" stroke="#2C3C50" stroke-width="1"/>')
text(cxb, by + 140, "Fan 360   ·   Fan Insight", fs=15, fill="#FFFFFF", wt=600, anchor="middle")
text(cxb, by + 166, "B2B Sponsorship Sales   ·   PRM", fs=15, fill="#FFFFFF", wt=600, anchor="middle")
text(cxb, by + 204, "ONE BLACK BOX — 내부 구조는 05_ARCHITECTURE.md", fs=10.5, fill="#F0A883", wt=600, anchor="middle", ls="0.4")

# ---------------------------------------------------------------- external nodes
CW, CH = 300, 100        # top / bottom cards
SW, SH = 320, 100        # side cards

# top (customer side)
node(690 - CW/2, 128, CW, CH, "Fan / Customer",
     "팬 · 이루키 — 구매 · 입장 · 퀴즈 · 관심 신호", "→ Fan Activity · Purchase · Participation", "actor")
node(1230 - CW/2, 128, CW, CH, "Fan App",
     "Demo 데이터 채널 · 업무 UI 아님", "→ Fan Data (event ingest)", "system")

# left (business users)
node(175 - SW/2, 300, SW, SH, "FRM Manager",
     "김매니저 — B2C 팬 운영 · Human-in-the-loop", "⇄ Fan 360 · Recommendation · Insight", "actor")
node(175 - SW/2, 560, SW, SH, "Sponsorship Sales Manager",
     "이매니저 · 파트너 담당자 — B2B 스폰서십 영업", "⇄ PRM · Lead · Opportunity · Activity", "actor")

# right (business & data)
node(1745 - SW/2, 300, SW, SH, "OpenDART",
     "금융감독원 전자공시 · opendart.fss.or.kr", "⇄ Company · Financial · Disclosure", "data")
node(1745 - SW/2, 560, SW, SH, "Slack",
     "담당자 업무 알림 · B2C→B2B 핸드오프", "← Fan Insight · Alerts", "system")

# bottom (communication)
node(690 - CW/2, 792, CW, CH, "Email / Messaging",
     "Email · SMS · Push · KakaoTalk", "← Personalized Message · Benefit", "system")
node(1230 - CW/2, 792, CW, CH, "Prospective Sponsor",
     "Partnership Inquiry Site 로 문의 접수", "→ Partnership Inquiry", "actor")

# ---------------------------------------------------------------- connectors
# 1 Fan -> CA (in)
arrow("M 690 228 L 690 300 L 800 300 L 800 372", col=NAVY_SOFT)
chip(745, 288, "Fan Activity")
# 2 Fan App -> CA (in)
arrow("M 1230 228 L 1230 300 L 1160 300 L 1160 372", col=NAVY_SOFT)
chip(1195, 288, "Fan Data")
# 3 FRM Manager <-> CA
arrow("M 335 353 L 512 353 L 512 430 L 690 430", col=NAVY_SOFT, two=True)
chip(438, 341, "Fan 360 · Recommendation")
# 4 Sales Manager <-> CA
arrow("M 335 613 L 512 613 L 512 555 L 690 555", col=NAVY_SOFT, two=True)
chip(430, 601, "PRM · Pipeline")
# 5 OpenDART <-> CA
arrow("M 1585 353 L 1408 353 L 1408 430 L 1230 430", col=NAVY_SOFT, two=True)
chip(1486, 341, "Company Data")
# 6 CA -> Slack (out)
arrow("M 1230 555 L 1408 555 L 1408 613 L 1585 613", col=ORANGE)
chip(1345, 543, "Insight · Alerts", fill=ORANGE_DK)
# 7 CA -> Email / Messaging (out)
arrow("M 800 612 L 800 700 L 690 700 L 690 792", col=ORANGE)
chip(745, 700, "Personalized Message", fill=ORANGE_DK)
# 8 Prospective Sponsor -> CA (in)
arrow("M 1230 792 L 1230 700 L 1160 700 L 1160 612", col=NAVY_SOFT)
chip(1195, 700, "Partnership Inquiry")

# ---------------------------------------------------------------- business context strip (secondary)
sy, sh = 946, 34
text(64, sy - 8, "BUSINESS CONTEXT", fs=10.5, fill=MUTE, wt=800, ls="2")
strip = ["FAN ACTIVITY", "CUSTOMER 360", "FAN INSIGHT", "PARTNER OPPORTUNITY", "SPONSORSHIP REVENUE"]
sx0, sx1, gap = 64, 1856, 24
pw = (sx1 - sx0 - gap * (len(strip) - 1)) / len(strip)
for i, lab in enumerate(strip):
    px = sx0 + i * (pw + gap)
    rect(px, sy, pw, sh, rx=8, fill="#EBEEF2")
    text(px + pw / 2, sy + sh / 2 + 4, lab, fs=12, fill=SLATE, wt=700, anchor="middle")
    if i < len(strip) - 1:
        mx = px + pw + gap / 2
        add(f'<path d="M {mx-3.5} {sy+sh/2-5} L {mx+3.5} {sy+sh/2} L {mx-3.5} {sy+sh/2+5} z" fill="{MUTE}"/>')

# ---------------------------------------------------------------- footer
add(f'<line x1="64" y1="1000" x2="1856" y2="1000" stroke="{EXT_LN}" stroke-width="1"/>')
text(64, 1020, "근거: docs/deliverables/08_CONTEXT_DIAGRAM.md   ·   실제 구현/문서에서 확인되는 관계만 표현", fs=11, fill=MUTE, wt=500)
text(1856, 1020, "CELLSFORCE × CLOUD ALPACAS    ·    System Context · 2026", fs=11, fill=SLATE, wt=700, anchor="end")

add("</svg>")

out_svg = os.path.join(HERE, "context_diagram.svg")
with open(out_svg, "w", encoding="utf-8") as f:
    f.write("".join(B))
print("wrote", out_svg)
