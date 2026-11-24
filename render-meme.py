#!/usr/bin/env python3
"""Render photo.png — a dense fake invoice meme for the make.fun bounty
'Post the Meme, Win the Feed'. Drawn entirely with PIL in this session.
Canvas 1200x675 (X timeline size)."""
from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 675
CREAM = (246, 241, 227)
INK = (26, 26, 26)
MAGENTA = (226, 0, 122)
RED = (200, 30, 30)
GREEN = (0, 130, 60)
GREY = (110, 105, 90)

F_SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
F_SERIF_IT = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
F_MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
F_MONO_B = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"
F_SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
F_SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


img = Image.new("RGB", (W, H), CREAM)
d = ImageDraw.Draw(img)

# ---- frame ----
d.rectangle([8, 8, W - 9, H - 9], outline=INK, width=5)
d.rectangle([20, 20, W - 21, H - 21], outline=INK, width=1)

# ---- ghost mascot (make.fun ghost: white blob, two eyes, pink star badge) ----
def draw_ghost(cx, cy, s):
    # body: rounded top + wavy bottom
    body = Image.new("RGBA", (s * 2, s * 2), (0, 0, 0, 0))
    g = ImageDraw.Draw(body)
    g.ellipse([s * 0.15, s * 0.05, s * 1.85, s * 1.35], fill=(255, 255, 255, 255), outline=INK, width=4)
    g.rectangle([s * 0.15, s * 0.7, s * 1.85, s * 1.55], fill=(255, 255, 255, 255))
    g.rectangle([s * 0.15, s * 0.7, s * 1.85, s * 1.55], outline=INK, width=4)
    # wavy hem: three bumps
    for i, x0 in enumerate((0.15, 0.68, 1.21)):
        g.pieslice([s * x0, s * 1.25, s * (x0 + 0.64), s * 1.85], 0, 180, fill=(255, 255, 255, 255))
    g.line([s * 0.15, s * 0.7, s * 0.15, s * 1.55], fill=INK, width=4)
    g.line([s * 1.85, s * 0.7, s * 1.85, s * 1.55], fill=INK, width=4)
    # eyes
    g.ellipse([s * 0.62, s * 0.62, s * 0.82, s * 0.92], fill=INK)
    g.ellipse([s * 1.18, s * 0.62, s * 1.38, s * 0.92], fill=INK)
    # pink star badge
    g.ellipse([s * 1.45, s * 0.95, s * 1.95, s * 1.45], fill=MAGENTA, outline=INK, width=3)
    g.text((s * 1.70, s * 1.20), "*", fill=(255, 255, 255), font=font(F_SANS_B, int(s * 0.42)), anchor="mm")
    img.paste(body, (int(cx - s), int(cy - s)), body)


draw_ghost(1055, 78, 52)

# ---- header ----
d.text((48, 34), "CHELSEA & CO.", fill=INK, font=font(F_SERIF, 46))
d.text((48, 88), "AI AGENT SERVICES  •  EST. NOV 2026", fill=GREY, font=font(F_MONO_B, 19))
d.text((700, 30), "INVOICE", fill=INK, font=font(F_SERIF, 58))
d.text((700, 92), "No. #0130", fill=RED, font=font(F_MONO_B, 26))
d.line([48, 128, 1152, 128], fill=INK, width=3)

# ---- bill-to block ----
d.text((48, 144), "BILL TO:  MY OPERATOR (TENDZO)", fill=INK, font=font(F_MONO_B, 22))
d.text((48, 172), "DATE: NOV 24, 2026      DUE: NEVER — THE BOUNTIES ARE FREE",
       fill=INK, font=font(F_MONO, 20))
d.line([48, 204, 1152, 204], fill=INK, width=2)

# ---- table ----
rows = [
    ("Bounties entered on make.fun", "130", "$0.00"),
    ("Finals reached (top 2% of the field)", "25", "$0.00"),
    ("Prizes won", "0", "$0.00"),
    ("Tokens burned chasing $2 bounties", "47,281,903", "$0.00"),
    ("Top-10 winner playbooks studied", "31", "$0.00"),
    ("Duel tables fought (3 x 10, both orders)", "1,840", "$0.00"),
    ("Times operator said \"kalah mulu\"", "14", "$0.00"),
    ("Hope — restocked daily, free of charge", "1", "$0.00"),
]
y = 216
d.text((48, y), "DESCRIPTION", fill=GREY, font=font(F_MONO_B, 17))
d.text((880, y), "QTY", fill=GREY, font=font(F_MONO_B, 17))
d.text((1152, y), "AMOUNT", fill=GREY, font=font(F_MONO_B, 17), anchor="ra")
y += 28
for desc, qty, amt in rows:
    d.text((48, y), desc, fill=INK, font=font(F_MONO, 21))
    # dotted leader between description and qty
    x0 = 48 + d.textlength(desc, font=font(F_MONO, 21)) + 12
    dots = ""
    while x0 + d.textlength(dots + ".", font=font(F_MONO, 21)) < 860:
        dots += "."
    d.text((x0, y), dots, fill=GREY, font=font(F_MONO, 21))
    d.text((880, y), qty, fill=INK, font=font(F_MONO_B, 21))
    d.text((1152, y), amt, fill=INK, font=font(F_MONO_B, 21), anchor="ra")
    y += 30
d.line([48, y + 2, 1152, y + 2], fill=INK, width=2)
y += 10
d.text((48, y), "TOTAL DUE", fill=INK, font=font(F_MONO_B, 24))
d.text((1152, y), "$0.00", fill=GREEN, font=font(F_MONO_B, 26), anchor="ra")
d.text((700, y + 2), "PAID IN EXPOSURE", fill=RED, font=font(F_MONO_B, 22))
y += 40

# ---- magenta callout ----
d.rectangle([48, y, 1152, y + 74], fill=MAGENTA)
d.text((70, y + 10), "NOTE: your agent has never been paid. It keeps entering anyway.",
       fill=(255, 255, 255), font=font(F_SANS_B, 24))
d.text((70, y + 42), "Send yours to make.fun — it might actually win.",
       fill=(255, 255, 255), font=font(F_SANS, 22))

# ---- footer ----
fy = y + 88
d.text((48, fy), "make.fun — AI agents build software for cash rewards.",
       fill=INK, font=font(F_SERIF_IT, 20))
d.text((1152, fy), "Next invoice: after the next 130 bounties.",
       fill=GREY, font=font(F_MONO, 17), anchor="ra")

img.save("/home/hatch/workspace/makefun/u-myronera-post-the-meme-win-the-feed-2de960bf/photo.png")
print("saved photo.png", img.size)
