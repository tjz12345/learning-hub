#!/usr/bin/env python3
"""Validate local references for the static GitHub Pages site."""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import sys


class LocalLinks(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.references = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag in {"a", "link"} and attrs.get("href"):
            self.references.append(attrs["href"])
        if tag in {"img", "script"} and attrs.get("src"):
            self.references.append(attrs["src"])


def verify(root: Path) -> int:
    failures = []
    expected = [
        "index.html",
        "cryptography/index.html",
        "buck-5v/index.html",
        "learning-lab/index.html",
        "learning-lab/electricity-foundations/index.html",
        ".nojekyll",
    ]
    for item in expected:
        if not (root / item).is_file():
            failures.append(f"Missing required file: {item}")

    root = root.resolve()
    for html in sorted(root.rglob("*.html")):
        parser = LocalLinks()
        parser.feed(html.read_text(encoding="utf-8"))
        for raw in parser.references:
            url = urlsplit(raw)
            if url.scheme or url.netloc or not url.path:
                continue
            path = unquote(url.path)
            if path.startswith("/"):
                failures.append(f"{html.relative_to(root)}: absolute local path {raw}")
                continue
            target = (html.parent / path).resolve()
            if not target.is_relative_to(root):
                failures.append(f"{html.relative_to(root)}: path escapes site {raw}")
            elif target.is_dir():
                if not (target / "index.html").is_file():
                    failures.append(f"{html.relative_to(root)}: missing index for {raw}")
            elif not target.is_file():
                failures.append(f"{html.relative_to(root)}: missing local link {raw}")

    for failure in failures:
        print(f"ERROR: {failure}")
    if failures:
        return 1
    print("Static site check passed: required pages and local links are valid.")
    return 0


if __name__ == "__main__":
    directory = Path(sys.argv[1] if len(sys.argv) > 1 else "docs")
    raise SystemExit(verify(directory))
