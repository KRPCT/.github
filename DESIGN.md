# KRPCT profile

`profile/README.md` is the organization homepage. `README.md` presents the same page at the repository root, with adjusted local asset paths.

The organization page opens directly with the full-width 1200 × 860 poster. Its name and principal slogans are part of the composition, with no Markdown heading or explanatory paragraph preceding it. Navigation and project descriptions follow the poster.

## Direction

- Audience: people exploring KRPCT's software and potential contributors.
- Promise: tools for thinking and creating, with user control as a design direction.
- Evidence: KRPCT's public InkStream and Pillowtome repository descriptions, checked on 2026-10-05. Product descriptions are repository claims, not independent validation.
- First action: open a project or its issue tracker.
- Visual language: monumental constructivist typography, an oblique signal-red plane, a dense 151-column ASCII tribar with three face values, beveled edges and a hard character shadow, plus an ASCII wordmark, pen, three-dimensional book, and cube.
- Palette: `#070709` black, `#fafbff` cold white, `#ff263b` signal red. Neutral gray steps are confined to the ASCII surface lighting. No cream, beige, glow, or blur.
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

This standard-library command writes three ASCII source files, two poster SVGs, and the root README. The visible Penrose surface lighting, its hard character shadow, pen, book, and separate wordmark are rendered in ASCII glyphs. A neutral silhouette behind the triangle prevents the colored background showing through its surfaces. The tribar uses projected edge distances for bevels, three dominant face tones, and 16 neutral light levels. Flat SVG planes and large display typography provide the constructivist composition. The command makes no network requests. The published SVGs have no scripts, external fonts, linked images, or animation.

Keep previews and check outputs outside Git. Verify the GitHub-rendered Markdown, actual organization asset URLs, and wide/narrow layouts before publishing changes.

## License

The MIT license here applies to this repository's original profile copy, ASCII art, and generation script. Linked projects retain their respective license terms.
