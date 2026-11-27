#!/usr/bin/env python3
"""Draw the 27 November 2026 world-news image for make.fun.

Concept: an airport split-flap departure board. No masthead, no
cards, no grid, no feed, no frames, no poster title treatment:
one black board, amber flap letters, each story a departure row
with a three-letter destination code and a status word. The hero
is the top flap panel, set apart by a red BREAKING flap.

Pillow only, no network, no randomness, no timestamps: two runs
are byte-identical. Writes entry.png (1024x1024, < 1 MiB).
"""

from PIL import Image, ImageDraw, ImageFont

W = H = 1024
BG = (12, 12, 10)        # board black
PANEL = (22, 22, 19)     # flap panel
PANEL2 = (30, 29, 24)    # lighter flap
INK = (240, 236, 222)    # warm white
MUTED = (170, 164, 148)  # grey
AMBER = (245, 183, 49)   # split-flap amber
RED = (226, 62, 40)      # breaking red
GREEN = (96, 190, 110)   # on-time green
RULE = (58, 56, 48)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def font(name, size):
    return ImageFont.truetype(f"{FONT_DIR}/{name}", size)


F_BOARD = font("DejaVuSansMono-Bold.ttf", 30)
F_DATE = font("DejaVuSansMono-Bold.ttf", 22)
F_TAG = font("DejaVuSansMono-Bold.ttf", 24)
F_HERO_CODE = font("DejaVuSansMono-Bold.ttf", 92)
F_HERO = font("DejaVuSans-Bold.ttf", 58)
F_HERO_SUB = font("DejaVuSans.ttf", 27)
F_CODE = font("DejaVuSansMono-Bold.ttf", 40)
F_ROW = font("DejaVuSans-Bold.ttf", 28)
F_DETAIL = font("DejaVuSans.ttf", 23)
F_STATUS = font("DejaVuSansMono-Bold.ttf", 20)
F_FOOT = font("DejaVuSansMono-Bold.ttf", 21)


def wrap(draw, text, fnt, width):
    lines, cur = [], ""
    for word in text.split():
        trial = f"{cur} {word}".strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def flap(d, box, fill):
    """A split-flap tile: rounded-ish panel with a centre split line."""
    d.rectangle(box, fill=fill, outline=RULE)
    x0, y0, x1, y1 = box
    mid = (y0 + y1) // 2
    d.line([(x0, mid), (x1, mid)], fill=(0, 0, 0), width=2)


def main():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    mx = 48

    # ---- board header ------------------------------------------------------
    d.text((mx, 30), "WORLD DEPARTURES", font=F_BOARD, fill=AMBER)
    date = "FRI 27 NOV 2026"
    dw = d.textlength(date, font=F_DATE)
    d.text((W - mx - dw, 36), date, font=F_DATE, fill=MUTED)
    d.line([(mx, 82), (W - mx, 82)], fill=AMBER, width=3)

    # ---- hero flap panel ---------------------------------------------------
    hy0, hy1 = 104, 412
    d.rectangle([mx, hy0, W - mx, hy1], fill=PANEL, outline=RULE)
    d.line([(mx, (hy0 + hy1) // 2), (W - mx, (hy0 + hy1) // 2)],
           fill=(0, 0, 0), width=2)
    # BREAKING flap, top left; destination code, top right
    tag = " BREAKING "
    tw = d.textlength(tag, font=F_TAG)
    d.rectangle([mx + 24, hy0 + 20, mx + 24 + tw, hy0 + 20 + 38],
                fill=RED)
    d.text((mx + 24, hy0 + 24), tag, font=F_TAG, fill=(255, 255, 255))
    code = "KWI"
    cw = d.textlength(code, font=F_HERO_CODE)
    d.text((W - mx - 24 - cw, hy0 + 14), code, font=F_HERO_CODE,
           fill=AMBER)
    # headline, two lines
    d.text((mx + 24, hy0 + 106), "DRONE STRIKE KILLS", font=F_HERO,
           fill=INK)
    d.text((mx + 24, hy0 + 168), "2 ITALIANS", font=F_HERO, fill=INK)
    # sub, bottom of the panel
    sub = "Iran denies responsibility for the attack on Kuwait, officials say"
    lines = wrap(d, sub, F_HERO_SUB, W - 2 * mx - 48)
    sy = hy1 - 24 - len(lines) * 32
    for i, line in enumerate(lines):
        d.text((mx + 24, sy + i * 32), line, font=F_HERO_SUB, fill=MUTED)

    # ---- departure rows ----------------------------------------------------
    rows = [
        ("GAZ", "Israel kills 10 in Gaza", "Hamas weighs its response", RED, "ALERT"),
        ("USA", "Thanksgiving storm grounds flights", "Macy's parade postponed; 500k without power", AMBER, "DELAYED"),
        ("MLI", "300+ Russians killed backing Mali junta", "Moscow's support for the junta under fire", AMBER, "BREAKING"),
        ("FRA", "France faces presidential vote debacle", "Mainstream parties have no clear candidate", MUTED, "WATCH"),
        ("IBZ", "Diesel tanker capsizes off Ibiza", "One dead; 7,000 tonnes aboard", AMBER, "ALERT"),
        ("GBR", "UK net migration lowest since 1997", "Falls to lowest level outside the pandemic", GREEN, "ON TIME"),
    ]
    y = 424
    rh = 82
    for code, title, detail, colour, status in rows:
        d.rectangle([mx, y, W - mx, y + rh - 10], fill=PANEL2,
                    outline=RULE)
        d.line([(mx, y + (rh - 10) // 2), (W - mx, y + (rh - 10) // 2)],
               fill=(0, 0, 0), width=1)
        d.text((mx + 18, y + 14), code, font=F_CODE, fill=colour)
        d.text((mx + 158, y + 8), title, font=F_ROW, fill=INK)
        d.text((mx + 158, y + 42), detail, font=F_DETAIL, fill=MUTED)
        sw = d.textlength(status, font=F_STATUS)
        d.text((W - mx - 16 - sw, y + 24), status, font=F_STATUS,
               fill=colour)
        y += rh

    # ---- footer ticker -----------------------------------------------------
    fy = 936
    d.line([(mx, fy), (W - mx, fy)], fill=AMBER, width=2)
    foot = "CHESS: GUKESH-SINDAROV DRAW GAME 3  •  TRUMP SEEKS PROBE INTO 'FAKE' GDP"
    for i, line in enumerate(wrap(d, foot, F_FOOT, W - 2 * mx)):
        d.text((mx, fy + 16 + i * 28), line, font=F_FOOT, fill=AMBER)

    img.save("entry.png", optimize=True)


if __name__ == "__main__":
    main()
