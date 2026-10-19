#!/usr/bin/env python3
"""alt_audit.py — mechanical alt-text checks for a CSV or a saved HTML page.

Usage:
    python3 alt_audit.py images.csv                    # CSV with columns: image, alt
    python3 alt_audit.py page.html                     # a saved HTML page
    python3 alt_audit.py page.html --brand "Acme"      # also flag the brand name
    python3 alt_audit.py images.csv --banned "tumbler,flask"   # words the store never uses

Checks: missing alt, file-name-as-alt, "image of"/"photo of", brand name,
banned terms, length (< 20 or > 125 characters), keyword repetition,
and duplicates within the batch. Read-only; Python 3.8+, standard library only.
Judgement (is it specific? does it match the picture?) is left to the skill.
"""
import argparse
import csv
import os
import re
import sys
from collections import Counter
from html.parser import HTMLParser

FILLER = re.compile(r"^\s*(an?\s+)?(image|photo|picture|graphic)\s+of\b", re.I)
FILENAME_LIKE = re.compile(r"^[\w\-]+\.(jpe?g|png|webp|gif|avif|svg)$|^(img|dsc|dcim)[_\-]?\d+", re.I)


class ImgCollector(HTMLParser):
    def __init__(self):
        super().__init__()
        self.rows = []

    def handle_starttag(self, tag, attrs):
        if tag != "img":
            return
        a = dict(attrs)
        src = a.get("src") or a.get("data-src") or "(no src)"
        alt = a.get("alt")  # None = attribute missing; "" = explicitly empty
        self.rows.append((src, alt))


def load(path):
    if path.lower().endswith((".html", ".htm")):
        p = ImgCollector()
        with open(path, encoding="utf-8", errors="replace") as fh:
            p.feed(fh.read())
        return p.rows
    with open(path, encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh)
        cols = {c.lower().strip(): c for c in (reader.fieldnames or [])}
        img_col = cols.get("image") or cols.get("src") or cols.get("file")
        alt_col = cols.get("alt") or cols.get("alt text") or cols.get("alt_text")
        if not img_col or not alt_col:
            sys.exit("CSV needs columns named 'image' and 'alt'.")
        return [(r[img_col], r[alt_col]) for r in reader]


def check(rows, brand, banned):
    alts = [(a or "").strip().lower() for _, a in rows]
    counts = Counter(a for a in alts if a)
    results = []
    for (src, alt), low in zip(rows, alts):
        issues = []
        if alt is None:
            issues.append("CRITICAL missing alt attribute")
        elif not alt.strip():
            issues.append("empty alt (fine only if purely decorative)")
        else:
            text = alt.strip()
            if FILENAME_LIKE.search(text) or text.lower() == os.path.basename(src).lower():
                issues.append("CRITICAL file name used as alt")
            if FILLER.search(text):
                issues.append('starts with "image/photo of"')
            if brand and re.search(r"\b" + re.escape(brand) + r"\b", text, re.I):
                issues.append(f'CRITICAL brand name "{brand}" (ok only on logo/packaging images)')
            for term in banned:
                if re.search(r"\b" + re.escape(term) + r"\b", text, re.I):
                    issues.append(f'banned term "{term}"')
            n = len(text)
            if n < 20:
                issues.append(f"too short ({n} chars)")
            elif n > 125:
                issues.append(f"too long ({n} chars)")
            stop = {"the", "and", "for", "with", "you", "your", "its"}
            words = [w for w in re.findall(r"[a-z]+", low) if len(w) > 2 and w not in stop]
            rep = [w for w, c in Counter(words).items() if c >= 3]
            if rep:
                issues.append("repeated words: " + ", ".join(rep))
            if counts[low] > 1:
                issues.append(f"duplicate of {counts[low] - 1} other image(s)")
        results.append((src, alt, issues))
    return results


def main():
    ap = argparse.ArgumentParser(description="Mechanical alt-text audit for a CSV or saved HTML page.")
    ap.add_argument("path")
    ap.add_argument("--brand", help="brand name to flag")
    ap.add_argument("--banned", default="", help="comma-separated terms the store never uses")
    args = ap.parse_args()

    rows = load(args.path)
    banned = [t.strip() for t in args.banned.split(",") if t.strip()]
    results = check(rows, args.brand, banned)
    flagged = [r for r in results if r[2]]

    print(f"# Alt text scan · {os.path.basename(args.path)} · {len(results)} images, {len(flagged)} flagged\n")
    for i, (src, alt, issues) in enumerate(results, 1):
        if not issues:
            continue
        shown = "(missing)" if alt is None else (alt if alt else '""')
        print(f"{i:>3}. {src}\n     alt: {shown}")
        for issue in issues:
            print(f"     - {issue}")
    if not flagged:
        print("No mechanical issues found. Still check that each alt matches its image.")


if __name__ == "__main__":
    main()
