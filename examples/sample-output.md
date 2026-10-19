# Sample scan output

Result of running the script on [`sample-images.csv`](sample-images.csv):

```bash
python3 skills/ecommerce-alt-text/scripts/alt_audit.py examples/sample-images.csv --brand Acme --banned tumbler,flask
```

```text
# Alt text scan · sample-images.csv · 8 images, 7 flagged

  2. IMG_4821.jpg
     alt: IMG_4821.jpg
     - CRITICAL file name used as alt
     - too short (12 chars)
  3. travel-mug-red-02.jpg
     alt: Image of a red mug
     - starts with "image/photo of"
     - too short (18 chars)
  4. travel-mug-black-03.jpg
     alt: Acme premium mug
     - CRITICAL brand name "Acme" (ok only on logo/packaging images)
     - too short (16 chars)
  5. travel-mug-green-04.jpg
     alt: travel mug
     - too short (10 chars)
     - duplicate of 1 other image(s)
  6. travel-mug-blue-05.jpg
     alt: travel mug
     - too short (10 chars)
     - duplicate of 1 other image(s)
  7. travel-mug-lid-06.jpg
     alt: mug travel mug coffee mug insulated mug tumbler mug for travel
     - banned term "tumbler"
     - repeated words: mug
  8. divider.png
     alt: ""
     - empty alt (fine only if purely decorative)
```

The script only catches mechanical problems. The skill then checks whether each alt actually describes its image and rewrites the flagged ones.
