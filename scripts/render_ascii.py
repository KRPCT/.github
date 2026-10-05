"""Render KRPCT's ASCII identity. Standard library only; no network access."""

from html import escape
from math import hypot
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets" / "readme"
TRIBAR_FACES = [
    [(9, 19), (15, 19), (28, 6), (47, 25), (50, 22), (28, 0)],
    [(0, 22), (3, 25), (47, 25), (28, 6), (25, 9), (38, 22)],
    [(22, 0), (0, 22), (38, 22), (35, 19), (9, 19), (28, 0)],
]


def inside(x, y, polygon):
    odd = False
    for a, b in zip(polygon, polygon[1:] + polygon[:1]):
        if (a[1] > y) != (b[1] > y):
            cross = (b[0] - a[0]) * (y - a[1]) / (b[1] - a[1]) + a[0]
            if x < cross:
                odd = not odd
    return odd


def penrose():
    # The three six-sided faces form the cyclic depth order of the tribar.
    faces = zip([0.98, 0.63, 0.25], ["@MW", "%#M", "+#="], TRIBAR_FACES)
    grid = [[" "] * 151 for _ in range(76)]
    tones = [[0] * 151 for _ in range(76)]
    for base, marks, polygon in faces:
        for row in range(76):
            for col in range(151):
                x, y = (col + 0.5) / 3, (row + 0.5) / 3
                if not inside(x, y, polygon):
                    continue
                edge = edge_distance(x, y, polygon)
                # Narrow bevels, a darker seam, and three dominant face tones.
                # All visible material remains made of ASCII glyphs.
                if edge < 0.18:
                    value, mark = 1.0, "@"
                elif edge < 0.63:
                    value, mark = min(1.0, base + 0.24 * (1 - edge / 0.63)), "M"
                elif edge < 0.9:
                    value, mark = base * 0.76, marks[(col + row) % len(marks)]
                else:
                    value = min(1.0, base + 0.04 * (1 - y / 25))
                    mark = marks[(col + row) % len(marks)]
                grid[row][col] = mark
                tones[row][col] = round(value * 15)
    return ["".join(row).rstrip() for row in grid], tones


def edge_distance(x, y, polygon):
    # Measure in projected physical units, compensating for the glyph aspect.
    nearest = float("inf")
    for (ax, ay), (bx, by) in zip(polygon, polygon[1:] + polygon[:1]):
        ay, by = ay * 1.75, by * 1.75
        dx, dy = bx - ax, by - ay
        t = max(0, min(1, ((x - ax) * dx + (y * 1.75 - ay) * dy) / (dx * dx + dy * dy)))
        nearest = min(nearest, hypot(x - ax - t * dx, y * 1.75 - ay - t * dy))
    return nearest


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
    triangle, tones = penrose()
    (ASSETS / "penrose.txt").write_text("\n".join(triangle).rstrip() + "\n", encoding="ascii", newline="\n")
    (ASSETS / "wordmark.txt").write_text("\n".join(line.rstrip() for line in WORDMARK) + "\n", encoding="ascii", newline="\n")
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="860" viewBox="0 0 1200 860" role="img" aria-labelledby="title desc">
  <title id="title">KRPCT — Build what comes next. Keep it yours.</title>
  <desc id="desc">A black, signal-red and cold-white constructivist composition. A large dense ASCII Penrose tribar has three distinct illuminated faces, narrow bevel highlights and a hard character shadow. Build what comes next. Keep it yours.</desc>
  <rect width="1200" height="860" fill="#070709"/>
  <path d="M 0,460 1200,110 1200,600 0,950 Z" fill="#ff263b"/>
  <g fill="#fafbff" font-family="Arial, Helvetica, sans-serif" font-weight="900">
    <text x="42" y="217" font-size="174" letter-spacing="-12">KRPCT</text>
  </g>
  <g font-family="'Courier New', Courier, monospace" fill="#fafbff" font-size="21" font-weight="700">
    <text x="52" y="43">INDEPENDENT SOFTWARE</text>
    <text x="1148" y="43" text-anchor="end">THINK / MAKE / CHANGE</text>
  </g>
  <path d="M 52,266 H 318" stroke="#fafbff" stroke-width="4"/>
  <g fill="#fafbff" font-family="Arial, Helvetica, sans-serif" font-weight="900" font-size="80" letter-spacing="-4">
    <text x="46" y="380">BUILD</text>
    <text x="46" y="463">WHAT</text>
    <text x="46" y="546">COMES</text>
    <text x="46" y="629">NEXT.</text>
  </g>
  <g id="penrose-ascii" transform="translate(135 -105) scale(0.87) rotate(-7 770 580)" font-family="'Courier New', Courier, monospace" font-weight="700">
    <g opacity="0.52">
'''
    svg += rows(triangle, 398, 302, 8.4, 9.5, "#070709", 4.8) + "\n    </g>\n"
    # Neutral silhouette prevents the red poster plane bleeding through the
    # characters. Facet light, texture, and bevels are rendered by the glyphs.
    for polygon in TRIBAR_FACES:
        points = " ".join(f"{375 + x * 14.4:g},{270 + y * 25.2:g}" for x, y in polygon)
        svg += f'    <polygon points="{points}" fill="#070709"/>\n'
    svg += '    <g stroke-width="0.26" paint-order="stroke fill">\n'
    for tone in range(16):
        layer = ["".join(c if tones[y][x] == tone else " " for x, c in enumerate(line)) for y, line in enumerate(triangle)]
        channel = round(tone / 15 * 245 + 10)
        color = f"#{channel:02x}{channel:02x}{channel:02x}"
        svg += f'      <g stroke="{color}">\n' + rows(layer, 375, 278, 8.4, 9.5, color, 4.8) + "\n      </g>\n"
    svg += '''    </g>
  </g>
  <g fill="#fafbff" font-family="Arial, Helvetica, sans-serif" font-weight="900">
    <text x="52" y="708" font-size="35" letter-spacing="-1">KEEP IT YOURS.</text>
  </g>
  <path d="M 52,787 H 1148" stroke="#fafbff" stroke-width="2"/>
  <g fill="#fafbff" font-family="'Courier New', Courier, monospace" font-size="21" font-weight="700">
    <text x="52" y="832">KRPCT / INC.</text>
    <text x="1148" y="832" text-anchor="end">TOOLS FOR A FUTURE YOU OWN.</text>
  </g>
</svg>
'''
    (ASSETS / "hero.svg").write_text(svg, encoding="utf-8", newline="\n")
    work = '''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="470" viewBox="0 0 1200 470" role="img" aria-labelledby="title desc">
  <title id="title">From thought to form — InkStream and Pillowtome</title>
  <desc id="desc">An ASCII pen and a three-dimensional book with a hatched cover and stacked page edges. Black and cold-white panels are separated by a sharp red diagonal. InkStream for writing. Pillowtome for reading.</desc>
  <rect width="1200" height="470" fill="#fafbff"/>
  <path d="M 0,0 H 734 L 580,470 H 0 Z" fill="#070709"/>
  <path d="M 690,0 H 734 L 580,470 H 536 Z" fill="#ff263b"/>
  <g font-family="'Courier New', Courier, monospace" font-size="22" font-weight="700">
    <text x="52" y="48" fill="#fafbff">01 / WRITE</text>
    <text x="819" y="48" fill="#070709">02 / READ</text>
  </g>
  <g font-family="'Courier New', Courier, monospace" xml:space="preserve" font-weight="700">
'''
    pen = ["          /\\", "         /##/", "        /##/", "       /##/", "      /##/", "     /##/", "    /__ /", "   /.. /", "  /___/", "  /", " ."]
    book = ["       ___________________", "      /#################/ /|", "     /#################/ / |", "    /#################/ /  |", "   /#################/ /   |", "  /_________________/ /    |", " |___________________/    /", " |===================|   /", " |===================|  /", " |===================| /", " |___________________|/"]
    work += rows(pen, 244, 90, 20, 25, "#fafbff", 13.8) + "\n"
    work += rows(book, 747, 98, 20, 22, "#070709", 12.6) + "\n"
    work += '''  </g>
  <g font-family="Arial, Helvetica, sans-serif" font-weight="900" letter-spacing="-2">
    <text x="48" y="402" font-size="65" fill="#fafbff">InkStream</text>
    <text x="734" y="402" font-size="65" fill="#070709">Pillowtome</text>
  </g>
  <g font-family="'Courier New', Courier, monospace" font-size="20" font-weight="700">
    <text x="52" y="438" fill="#fafbff">THOUGHT, INTO WORDS.</text>
    <text x="739" y="438" fill="#070709">WORDS, INTO THOUGHT.</text>
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
