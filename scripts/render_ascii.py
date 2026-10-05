"""Render KRPCT's ASCII identity. Standard library only; no network access."""

from html import escape
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets" / "readme"


def inside(x, y, polygon):
    odd = False
    for a, b in zip(polygon, polygon[1:] + polygon[:1]):
        if (a[1] > y) != (b[1] > y):
            cross = (b[0] - a[0]) * (y - a[1]) / (b[1] - a[1]) + a[0]
            if x < cross:
                odd = not odd
    return odd


def penrose():
    # Three continuous, bent faces. The depth order cycles at the corners.
    faces = [
        (".", [(9, 19), (15, 19), (28, 6), (47, 25), (50, 22), (28, 0)]),
        (":", [(0, 22), (3, 25), (47, 25), (28, 6), (25, 9), (38, 22)]),
        ("#", [(22, 0), (0, 22), (38, 22), (35, 19), (9, 19), (28, 0)]),
    ]
    grid = [[" "] * 51 for _ in range(26)]
    for mark, polygon in faces:
        for y in range(26):
            for x in range(51):
                if inside(x + 0.1, y + 0.1, polygon):
                    grid[y][x] = mark
    for _, polygon in faces:
        for (x1, y1), (x2, y2) in zip(polygon, polygon[1:] + polygon[:1]):
            steps = max(abs(x2 - x1), abs(y2 - y1))
            mark = "_" if y1 == y2 else ("/" if (x2 - x1) * (y2 - y1) < 0 else "\\")
            for i in range(steps + 1):
                x = round(x1 + (x2 - x1) * i / steps)
                y = round(y1 + (y2 - y1) * i / steps)
                grid[y][x] = mark
    return ["".join(row).rstrip() for row in grid]


WORDMARK = [
    "K   K  RRRR   PPPP    CCCC  TTTTT",
    "K  K   R   R  P   P  C       T  ",
    "K K    R   R  P   P  C       T  ",
    "KK     RRRR   PPPP   C       T  ",
    "K K    R R    P      C       T  ",
    "K  K   R  R   P      C       T  ",
    "K   K  R   R  P       CCCC   T  ",
]


def rows(lines, x, y, step, size, color, cell):
    result = []
    for i, line in enumerate(lines):
        occupied = [(column, mark) for column, mark in enumerate(line) if mark != " "]
        if occupied:
            positions = " ".join(f"{x + column * cell:g}" for column, _ in occupied)
            letters = "".join(mark for _, mark in occupied)
            result.append(
                f'    <text x="{positions}" y="{y + i * step}" font-size="{size}" '
                f'fill="{color}">{escape(letters)}</text>'
            )
    return "\n".join(result)


def main():
    ASSETS.mkdir(parents=True, exist_ok=True)
    triangle = penrose()
    (ASSETS / "penrose.txt").write_text("\n".join(triangle) + "\n", encoding="ascii", newline="\n")
    (ASSETS / "wordmark.txt").write_text("\n".join(line.rstrip() for line in WORDMARK) + "\n", encoding="ascii", newline="\n")
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="1000" viewBox="0 0 1200 1000" role="img" aria-labelledby="title desc">
  <title id="title">KRPCT — Build what comes next. Keep it yours.</title>
  <desc id="desc">A constructivist poster in vermilion, paper white, and ink black. A monumental ASCII Penrose triangle stands on a diagonal red plane beside the words Build what comes next. The letter-built KRPCT wordmark appears at the foot.</desc>
  <rect width="1200" height="1000" fill="#f2ecdf"/>
  <path d="M 355,360 1200,128 1200,1000 490,1000 Z" fill="#e43b2c"/>
  <g fill="#181917" font-family="Arial, Helvetica, sans-serif" font-weight="900">
    <text x="44" y="217" font-size="224" letter-spacing="-16">KRPCT</text>
  </g>
  <g font-family="'Courier New', Courier, monospace" fill="#181917" font-size="22" font-weight="700">
    <text x="56" y="47">INDEPENDENT SOFTWARE</text>
    <text x="1139" y="47" text-anchor="end">THINK / MAKE / CHANGE</text>
  </g>
  <path d="M 57,261 H 358" stroke="#181917" stroke-width="5"/>
  <path d="M 57,315 H 180 L 157,292 M 180,315 157,338" fill="none" stroke="#e43b2c" stroke-width="12"/>
  <g fill="#181917" font-family="Arial, Helvetica, sans-serif" font-weight="900" font-size="86" letter-spacing="-4">
    <text x="51" y="455">BUILD</text>
    <text x="51" y="543">WHAT</text>
    <text x="51" y="631">COMES</text>
    <text x="51" y="719">NEXT.</text>
  </g>
  <g id="penrose-ascii" transform="translate(0 -42) rotate(-10 818 574)" font-family="'Courier New', Courier, monospace" font-weight="700" xml:space="preserve">
'''
    # The geometry consists only of ASCII glyphs. Three ink treatments expose
    # the impossible depth cycle without filling the triangle with vector paths.
    for symbols, color in [("#", "#181917"), (".", "#f2ecdf"), (":", "#181917"), ("/\\_", "#f2ecdf")]:
        layer = ["".join(c if c in symbols else " " for c in line) for line in triangle]
        svg += rows(layer, 510, 310, 21, 22, color, 12) + "\n"
    svg += '''  </g>
  <g fill="#181917" font-family="Arial, Helvetica, sans-serif" font-weight="900">
    <text x="56" y="825" font-size="43" letter-spacing="-1.5">KEEP IT YOURS.</text>
  </g>
  <path d="M 56,869 H 1144" stroke="#181917" stroke-width="2"/>
  <g font-family="'Courier New', Courier, monospace" xml:space="preserve" font-weight="700">
'''
    svg += rows(WORDMARK, 57, 905, 10, 10, "#181917", 6.7) + "\n"
    svg += '''  </g>
  <g fill="#181917" font-family="'Courier New', Courier, monospace" font-size="22" font-weight="700">
    <text x="450" y="920">TOOLS FOR A FUTURE</text>
    <text x="450" y="951">YOU OWN.</text>
    <text x="1139" y="951" text-anchor="end">KRPCT / INC.</text>
  </g>
</svg>
'''
    (ASSETS / "hero.svg").write_text(svg, encoding="utf-8", newline="\n")
    work = '''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="470" viewBox="0 0 1200 470" role="img" aria-labelledby="title desc">
  <title id="title">From thought to form — InkStream and Pillowtome</title>
  <desc id="desc">ASCII drawings of a pen and an open book on diagonal black and paper-white fields. InkStream for writing. Pillowtome for reading.</desc>
  <rect width="1200" height="470" fill="#f2ecdf"/>
  <path d="M 0,0 H 734 L 580,470 H 0 Z" fill="#181917"/>
  <path d="M 694,0 H 734 L 580,470 H 540 Z" fill="#e43b2c"/>
  <g font-family="'Courier New', Courier, monospace" font-size="22" font-weight="700">
    <text x="52" y="48" fill="#f2ecdf">01 / WRITE</text>
    <text x="819" y="48" fill="#181917">02 / READ</text>
  </g>
  <g font-family="'Courier New', Courier, monospace" xml:space="preserve" font-weight="700">
'''
    pen = ["          /\\", "         /##/", "        /##/", "       /##/", "      /##/", "     /##/", "    /__ /", "   /.. /", "  /___/", "  /", " ."]
    book = ["      __..--. .--..__", " .--''      |      ''--.", "|  .----.   |   .----.  |", "|  |    |   |   |    |  |", "|  '----'   |   '----'  |", "|  ------   |   ------  |", "|  ------   |   ------  |", "|  ------   |   ------  |", "|__         |         __|", "   ''--..__ | __..--''", "           '-' "]
    work += rows(pen, 244, 90, 20, 23, "#f2ecdf", 13.8) + "\n"
    work += rows(book, 758, 103, 19, 21, "#181917", 12.6) + "\n"
    work += '''  </g>
  <g font-family="Arial, Helvetica, sans-serif" font-weight="900" letter-spacing="-2">
    <text x="48" y="402" font-size="65" fill="#f2ecdf">InkStream</text>
    <text x="734" y="402" font-size="65" fill="#181917">Pillowtome</text>
  </g>
  <g font-family="'Courier New', Courier, monospace" font-size="20" font-weight="700">
    <text x="52" y="438" fill="#f2ecdf">THOUGHT, INTO WORDS.</text>
    <text x="739" y="438" fill="#181917">WORDS, INTO THOUGHT.</text>
  </g>
</svg>
'''
    (ASSETS / "work.svg").write_text(work, encoding="utf-8", newline="\n")
    (ASSETS / "work.txt").write_text("WRITE / INKSTREAM\n\n" + "\n".join(line.rstrip() for line in pen) + "\n\nREAD / PILLOWTOME\n\n" + "\n".join(line.rstrip() for line in book) + "\n", encoding="ascii", newline="\n")
    profile = (ROOT / "profile" / "README.md").read_text(encoding="utf-8")
    (ROOT / "README.md").write_text(profile.replace("../assets/readme/", "./assets/readme/"), encoding="utf-8", newline="\n")
    print("Rendered ASCII sources, hero.svg, and repository README.md")


if __name__ == "__main__":
    main()
