#!/usr/bin/env python3
"""Draw the news-image-20261123 entry: a one-page newspaper front page
summing up world news of Monday 23 November 2026. Output: entry.png,
1024x1024, well under the 1 MiB cap. Run: python3 draw.py"""

from PIL import Image, ImageDraw, ImageFont
import textwrap

W, H = 1024, 1024
PAPER = (247, 243, 234)   # off-white newsprint
INK = (18, 18, 18)
NAVY = (11, 31, 58)
RED = (178, 34, 34)
GOLD = (201, 162, 39)
GREY = (90, 90, 90)
RULE = (180, 175, 160)

SERIF_B = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
SANS_B = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def para(draw, x, y, text, fnt, max_w, leading, fill=INK):
    for line in wrap(draw, text, fnt, max_w):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def kicker(draw, x, y, text, color=RED):
    f = font(SANS_B, 24)
    draw.text((x, y), text, font=f, fill=color)
    return y + 32


def headline(draw, x, y, text, size, max_w, fill=INK):
    f = font(SERIF_B, size)
    for line in wrap(draw, text, f, max_w):
        draw.text((x, y), line, font=f, fill=fill)
        y += int(size * 1.02)
    return y


img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

# ---- Masthead -------------------------------------------------------
d.rectangle([0, 0, W, 148], fill=NAVY)
d.text((512, 18), "THE WORLD TODAY", font=font(SERIF_B, 78),
       fill=(255, 255, 255), anchor="ma")
d.text((512, 108), "M O N D A Y   2 3   N O V E M B E R   2 0 2 6",
       font=font(SANS_B, 26), fill=GOLD, anchor="ma")
d.rectangle([0, 148, W, 154], fill=GOLD)

# ---- Lead story: COP31 ----------------------------------------------
y = 178
y = kicker(d, 40, y, "CLIMATE  •  ANTALYA, TURKEY")
y = headline(d, 40, y, "COP31 COLLAPSES", 72, 944)
y = para(d, 40, y + 6,
         "The climate summit ends with no deal after the longest talks in "
         "UN history. The EU and about 130 nations reject a draft text "
         "that omits fossil fuels.",
         font(SERIF, 29), 944, 36)
d.line([40, y + 18, 984, y + 18], fill=RULE, width=2)

# ---- Row 1: markets | Ukraine ---------------------------------------
y1 = y + 38
col_w = 452
y = kicker(d, 40, y1, "MARKETS")
y = headline(d, 40, y, "AI SELL-OFF SINKS STOCKS", 38, col_w)
para(d, 40, y + 4,
     "Nikkei falls 5.06% and the S&P 500 drops 3.7% as AI fears spread "
     "across Asia. Gold climbs as investors seek safety.",
     font(SERIF, 25), col_w, 30)

y = kicker(d, 532, y1, "UKRAINE")
y = headline(d, 532, y, "BOY, 7, PULLED ALIVE FROM RUBBLE", 38, col_w)
para(d, 532, y + 4,
     "A Russian strike on Dymer, north of Kyiv, kills at least 10. "
     "Rescuers free a seven-year-old boy from the rubble.",
     font(SERIF, 25), col_w, 30)

d.line([512, y1, 512, y1 + 210], fill=RULE, width=2)
d.line([40, y1 + 230, 984, y1 + 230], fill=RULE, width=2)

# ---- Row 2: warship | cartel boss -----------------------------------
y2 = y1 + 250
y = kicker(d, 40, y2, "LIBYA  •  MEDITERRANEAN")
y = headline(d, 40, y, "RUSSIAN WARSHIP SUNK", 38, col_w)
para(d, 40, y + 4,
     "A Ukrainian naval drone severely damages the Russian corvette "
     "Merkury off Benghazi.",
     font(SERIF, 25), col_w, 30)

y = kicker(d, 532, y2, "MEXICO")
y = headline(d, 532, y, "\u2018EL CHAPO ISIDRO\u2019 CAPTURED", 38, col_w)
para(d, 532, y + 4,
     "FBI most-wanted cartel leader Fausto Isidro Meza Flores is arrested "
     "in Sinaloa.",
     font(SERIF, 25), col_w, 30)

d.line([512, y2, 512, y2 + 200], fill=RULE, width=2)

# ---- Bottom strip: also today ---------------------------------------
by = 884
d.rectangle([0, by, W, H], fill=NAVY)
d.text((40, by + 16), "ALSO TODAY", font=font(SANS_B, 26), fill=GOLD)
items = [
    "Penny ends \u2014 Trump signs Common Cents Act",
    "Delta outage delays 1,600+ flights",
    "Lebanon ceasefire: villagers return home",
    "Molly Meldrum dies at 83",
]
yy = by + 52
for i, item in enumerate(items):
    col_x = 40 if i % 2 == 0 else 532
    if i == 2:
        yy = by + 92
    d.text((col_x, yy), "\u2022  " + item, font=font(SANS, 20),
           fill=(255, 255, 255))

img.save("entry.png", optimize=True)
print("saved entry.png")
