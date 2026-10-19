# ecommerce-alt-text

English | [简体中文](README.zh-CN.md)

An AI skill plus a small Python script for writing and auditing image alt text and file names in an online store — so every image makes sense to screen-reader users, search engines and AI assistants.

Works with Claude (as a Skill) and any agent that can read a Markdown instruction file. The script runs on its own.

## What you get

**Generate mode** — give it images, a list or a product URL and get a paste-ready table: image type, SEO-friendly file name, alt text, character count. Templates cover 8 image types: hero, in-use, hardware detail, material close-up, size comparison, lifestyle, packaging/gift, and customer photos — plus blog illustrations and decorative images.

**Audit mode** — give it existing alt text (CSV, export, screenshot) and get every failing image flagged against six checks, with a rewrite for each and the three to fix first.

**`alt_audit.py`** — a standard-library Python script that scans a CSV or a saved HTML page for missing alt, file names used as alt, "image of…", brand names, banned terms, length problems, keyword stuffing and duplicates. See [sample output](examples/sample-output.md).

## The rules it follows

- **No brand name in alt text** (except when the logo is the subject of the image).
- **Consistent product terminology** — your words, never near-synonyms.
- **No copy-paste alt text** across variants.
- **No "image of" / "photo of".**
- **Numbers over adjectives.**
- **Roughly 80–125 characters**, most important words first.
- **Empty alt for purely decorative images.**
- **Never invents** specs or claims that aren't in the image or the brief.
- **File names:** lowercase, hyphenated, descriptive — `travel-mug-navy-lid-closeup-02.jpg`, never `IMG_4821.jpg`.

## Install

**Claude:** copy `skills/ecommerce-alt-text/` into `~/.claude/skills/` (or your project's `.claude/skills/`), then:

> Write alt text and file names for these 6 product photos.
> Audit the alt text in this CSV.

**Script only:**

```bash
python3 skills/ecommerce-alt-text/scripts/alt_audit.py images.csv --brand "YourBrand" --banned "word1,word2"
python3 skills/ecommerce-alt-text/scripts/alt_audit.py saved-product-page.html
```

The CSV needs two columns: `image` and `alt`.

## Files

```
skills/ecommerce-alt-text/
├── SKILL.md                  # Rules, templates by image type, generate and audit modes
└── scripts/
    └── alt_audit.py          # Mechanical alt-text scan for CSV or HTML
examples/
├── sample-images.csv         # Test data (fictional)
├── sample-page.html          # Test page (fictional)
└── sample-output.md          # What the script reports
```

## License

[MIT](LICENSE)
