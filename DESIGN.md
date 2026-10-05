# KRPCT profile

`profile/README.md` is the organization homepage. `README.md` presents the same page at the repository root, with adjusted local asset paths.

## Direction

- Audience: people exploring KRPCT's software and potential contributors.
- Promise: tools for thinking and creating, with user control as a design direction.
- Evidence: KRPCT's public InkStream and Pillowtome repository descriptions, checked on 2026-10-05. Product descriptions are repository claims, not independent validation.
- First action: open a project or its issue tracker.
- Visual language: constructivist typography, oblique planes, unequal fields, hard geometry, a monumental ASCII impossible triangle, a letter-built wordmark, and ASCII pen/book/cube drawings.
- Palette: `#f2ecdf` paper, `#181917` ink, `#e43b2c` vermilion. Flat ink only; no gradients, cards, glow, or shadows.
- Type: heavy Arial / Helvetica for poster text; Courier New / Courier / monospace for the artwork. Explicit character widths keep the artwork aligned.

## Reference boundary

Copy and editorial direction refer only to [Manifold's GitHub identity](https://github.com/manifold-inc), [homepage](https://www.manifold.inc/), and [mission](https://www.manifold.inc/mission). The wording is adapted to KRPCT. No claims about Manifold's compute network, encryption, investors, adoption, or infrastructure are transferred to KRPCT. No other repository supplies layout or slogan inspiration.

The Penrose construction follows the standard three-face geometric illusion. The [public-domain geometric reference](https://commons.wikimedia.org/wiki/File:Penrose-dreieck.svg) is mathematical reference material; the character grid, wordmark, layout, and supporting ASCII drawings are created for this profile. No third-party image is embedded.

Only already-public KRPCT projects appear on the public page. No private repository metadata belongs in this repository.

## Editing

Edit `profile/README.md` for prose. Edit `scripts/render_ascii.py` for the triangle, letterforms, or hero composition, then run:

```sh
python scripts/render_ascii.py
```

This standard-library command writes three ASCII source files, two poster SVGs, and the root README. The Penrose triangle, pen, book, and small wordmark consist entirely of text glyphs. Flat SVG planes and large display typography provide the constructivist composition. The command makes no network requests. The published SVGs have no scripts, external fonts, linked images, or animation.

Keep previews and check outputs outside Git. Verify the GitHub-rendered Markdown, actual organization asset URLs, and wide/narrow layouts before publishing changes.

## License

The MIT license here applies to this repository's original profile copy, ASCII art, and generation script. Linked projects retain their respective license terms.
