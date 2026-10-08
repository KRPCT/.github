"""Export the public profile for GitHub's member view; no network or Git writes."""

import argparse
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PUBLIC_IMAGES = "https://raw.githubusercontent.com/KRPCT/.github/main/assets/readme/"
PUBLIC_SOURCES = "https://github.com/KRPCT/.github/blob/main/assets/readme/"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True, help="Destination profile/README.md")
    args = parser.parse_args()
    source = ROOT / "profile" / "README.md"
    target = args.output.resolve()
    if target == source.resolve():
        parser.error("The export destination must differ from the public profile.")
    public = source.read_text(encoding="utf-8")
    member = public.replace('src="../assets/readme/', f'src="{PUBLIC_IMAGES}')
    member = member.replace("](../assets/readme/", f"]({PUBLIC_SOURCES}")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(member, encoding="utf-8", newline="\n")
    print(f"Exported the complete member profile to {target}")


if __name__ == "__main__":
    main()
