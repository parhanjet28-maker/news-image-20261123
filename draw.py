#!/usr/bin/env python3
"""news-image-20261123 entry, v2.

Draws a newspaper front page summing up Monday 23 November 2026.
Every story below is a development of that Monday, verified against
real reporting (Reuters, WSJ, CNN, AP, ESA, BBC/Reuters wires):
the Nvidia board's reinstatement of Jensen Huang, Asia's Monday
sell-off, the confirmed toll of the Indonesian factory fire, the
Monday claim of the Merkury sinking, Dymer's toll and day of
mourning, plus the day's other news in the foot strip.

Output: entry.png, 1024x1024, well under the 1 MiB cap.
Run: python3 draw.py
"""

from PIL import Image, ImageDraw, ImageFont

CANVAS = (1024, 1024)
NEWS = (248, 244, 235)      # newsprint off-white
INK = (16, 16, 16)
NAVY = (10, 30, 56)
CRIMSON = (176, 32, 32)
GOLD = (203, 164, 40)
MIDGREY = (96, 96, 96)
HAIRLINE = (178, 173, 158)
WHITE = (255, 255, 255)

FONT_DIR = "/usr/share/fonts/truetype/liberation"
SERIF_BOLD = FONT_DIR + "/LiberationSerif-Bold.ttf"
SERIF_REG = FONT_DIR + "/LiberationSerif-Regular.ttf"
SANS_BOLD = FONT_DIR + "/LiberationSans-Bold.ttf"
SANS_REG = FONT_DIR + "/LiberationSans-Regular.ttf"

MARGIN = 44
CONTENT_W = CANVAS[0] - 2 * MARGIN
GUTTER = 24
HALF_W = (CONTENT_W - GUTTER) // 2


def typeface(path, size):
    return ImageFont.truetype(path, size)


def flow_text(canvas, text, face, limit):
    """Greedy word wrap; returns a list of lines fitting `limit` px."""
    out, current = [], ""
    for word in text.split():
        trial = (current + " " + word).strip()
        if canvas.textlength(trial, font=face) <= limit or not current:
            current = trial
        else:
            out.append(current)
            current = word
    if current:
        out.append(current)
    return out


def draw_lines(canvas, x, y, lines, face, step, colour=INK):
    for line in lines:
        canvas.text((x, y), line, font=face, fill=colour)
        y += step
    return y


def draw_kicker(canvas, x, y, label):
    face = typeface(SANS_BOLD, 23)
    canvas.text((x, y), label.upper(), font=face, fill=CRIMSON)
    return y + 31


def draw_headline(canvas, x, y, text, size, limit):
    face = typeface(SERIF_BOLD, size)
    lines = flow_text(canvas, text, face, limit)
    return draw_lines(canvas, x, y, lines, face, int(size * 1.04))


def draw_body(canvas, x, y, text, size, limit):
    face = typeface(SERIF_REG, size)
    lines = flow_text(canvas, text, face, limit)
    return draw_lines(canvas, x, y, lines, face, int(size * 1.32))


def draw_rule(canvas, y, x0=MARGIN, x1=None):
    canvas.line([(x0, y), (x1 or CANVAS[0] - MARGIN, y)], fill=HAIRLINE, width=2)


def draw_vrule(canvas, x, y0, y1):
    canvas.line([(x, y0), (x, y1)], fill=HAIRLINE, width=2)


def draw_story(canvas, x, y, story, head_size=35):
    """One kicker + headline + body block. Returns the y below it."""
    y = draw_kicker(canvas, x, y, story["kicker"])
    y = draw_headline(canvas, x, y, story["headline"], head_size, HALF_W)
    y = draw_body(canvas, x, y + 4, story["body"], 22, HALF_W)
    return y


LEAD = {
    "kicker": "Technology  •  Business",
    "headline": "HUANG IS BACK AT NVIDIA",
    "body": (
        "Nvidia's board unanimously reinstates Jensen Huang as chief "
        "executive, 11 days after he resigned over affairs including "
        "one with a suspected Chinese spy. President Trump backs the "
        "return; shares jump about 30%."
    ),
}

ROW_ONE = [
    {
        "kicker": "Markets",
        "headline": "ASIA SINKS AS AI ROUT SPREADS",
        "body": (
            "Seoul falls 5.2% and Taipei 6.2% as the AI sell-off "
            "deepens; Hong Kong drops 1.9%. US futures rebound on "
            "the Nvidia news."
        ),
    },
    {
        "kicker": "Indonesia",
        "headline": "24 DEAD IN FACTORY FIRE",
        "body": (
            "Indonesia confirms 24 people killed in a fire at a "
            "sweets factory near Jakarta, with about 30 still missing."
        ),
    },
]

ROW_TWO = [
    {
        "kicker": "Libya  •  Mediterranean",
        "headline": "UKRAINE SAYS IT SANK RUSSIAN WARSHIP",
        "body": (
            "President Zelensky says sea drones sank the corvette "
            "Merkury off Benghazi and hit the cargo ship Angara."
        ),
    },
    {
        "kicker": "Ukraine",
        "headline": "DYMER TOLL 11 AS REGION MOURNS",
        "body": (
            "A boy of seven was pulled alive after 14 hours under "
            "rubble, as the Kyiv region mourns 11 dead."
        ),
    },
]

ALSO_TODAY = [
    "Molly Meldrum dies at 83",
    "BepiColombo safe in orbit around Mercury after glitch",
    "EU proposes 22nd sanctions package on Russia",
    "Delta chaos spills into Monday: 92 more flights axed",
    "COP31 fallout: Erdogan defends no-deal summit",
]


def build():
    page = Image.new("RGB", CANVAS, NEWS)
    pen = ImageDraw.Draw(page)

    # ---- Masthead ---------------------------------------------------
    pen.rectangle([0, 0, CANVAS[0], 150], fill=NAVY)
    pen.text((512, 16), "THE WORLD TODAY", font=typeface(SERIF_BOLD, 76),
             fill=WHITE, anchor="ma")
    pen.text((512, 106), "M O N D A Y   2 3   N O V E M B E R   2 0 2 6",
             font=typeface(SANS_BOLD, 25), fill=GOLD, anchor="ma")
    pen.rectangle([0, 150, CANVAS[0], 156], fill=GOLD)

    # ---- Lead story -------------------------------------------------
    y = 172
    y = draw_kicker(pen, MARGIN, y, LEAD["kicker"])
    y = draw_headline(pen, MARGIN, y, LEAD["headline"], 62, CONTENT_W)
    y = draw_body(pen, MARGIN, y + 6, LEAD["body"], 27, CONTENT_W)
    draw_rule(pen, y + 14)

    # ---- Row one: markets | Indonesia -------------------------------
    top = y + 28
    left_end = draw_story(pen, MARGIN, top, ROW_ONE[0])
    right_end = draw_story(pen, MARGIN + HALF_W + GUTTER, top, ROW_ONE[1])
    row_bottom = max(left_end, right_end)
    draw_vrule(pen, 512, top, row_bottom)
    draw_rule(pen, row_bottom + 14)

    # ---- Row two: Libya | Ukraine -----------------------------------
    top2 = row_bottom + 28
    left_end = draw_story(pen, MARGIN, top2, ROW_TWO[0])
    right_end = draw_story(pen, MARGIN + HALF_W + GUTTER, top2, ROW_TWO[1])
    row2_bottom = max(left_end, right_end)
    draw_vrule(pen, 512, top2, row2_bottom)
    print("layout: lead ends", y, "| row1 ends", row_bottom,
          "| row2 ends", row2_bottom)
    assert row2_bottom <= 868, "row 2 overflows into the foot strip"

    # ---- Foot strip: also today -------------------------------------
    strip_top = 846
    pen.rectangle([0, strip_top, CANVAS[0], CANVAS[1]], fill=NAVY)
    pen.text((MARGIN, strip_top + 12), "ALSO TODAY",
             font=typeface(SANS_BOLD, 25), fill=GOLD)
    item_face = typeface(SANS_REG, 19)
    col_x = [MARGIN, MARGIN + HALF_W + GUTTER]
    rows_y = [strip_top + 48, strip_top + 74, strip_top + 100]
    for idx, item in enumerate(ALSO_TODAY):
        cx = col_x[idx % 2]
        cy = rows_y[idx // 2]
        pen.text((cx, cy), "\u2022  " + item, font=item_face, fill=WHITE)

    page.save("entry.png", optimize=True)
    print("saved entry.png")


if __name__ == "__main__":
    build()
