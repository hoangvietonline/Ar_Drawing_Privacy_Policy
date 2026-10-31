#!/usr/bin/env python3
"""Copy complete legal pages into the Android app, with embedded CSS."""
from pathlib import Path
import argparse

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--project-root", type=Path, help="Android project root; defaults to this repository's parent")
args = parser.parse_args()
source = Path(__file__).resolve().parent
project = (args.project_root or source.parent).resolve()
if not (project / "app/src/main/AndroidManifest.xml").is_file():
    parser.error("Android project not found; pass --project-root PATH")
destination = project / "app/src/main/assets/legal"
destination.mkdir(parents=True, exist_ok=True)
css = (source / "styles.css").read_text(encoding="utf-8")
for page, asset in (("index.html", "en-privacy.html"), ("terms.html", "en-terms.html")):
    html = (source / page).read_text(encoding="utf-8")
    html = html.replace('<link rel="stylesheet" href="styles.css">', '<style>' + css + '</style>')
    html = html.replace('href="index.html"', 'href="en-privacy.html"').replace('href="terms.html"', 'href="en-terms.html"')
    (destination / asset).write_text(html, encoding="utf-8")
    print("Updated", destination / asset)
