---
name: ecommerce-alt-text
description: Writes and audits image alt text and SEO-friendly image file names for online stores — product hero shots, detail and material close-ups, in-scale and comparison images, lifestyle, packaging, customer photos, blog illustrations and collection images. Two modes — generate paste-ready alt text plus file names, or audit existing alt text line by line with rewrites. Use when the user says "write alt text", "audit my alt tags", "image SEO", "how should I name my image files", "my images have no alt", "screen reader", or "rank in image search".
---

# E-commerce alt text

One job: **make every image on the store make sense to the readers who can't see it.**

| Reader | What they need | Why it matters |
|---|---|---|
| **Screen-reader users** | What the image actually shows | Accessibility (WCAG) and basic decency; also legal exposure in some markets |
| **Google Images and web search** | A clear relevance signal tying the image to the page topic | Image-search traffic and page relevance |
| **AI assistants** (ChatGPT, Perplexity, Gemini, Claude) | Alt text is part of the page's meaning when they read it | Accurate descriptions when your product is cited |

Before starting, ask for (or infer) the store's **terminology** — the exact words the brand uses for its products, and the words it never uses. If the user has a glossary, follow it.

---

## Ground rules (break one = rewrite)

### 1. Don't put the store's brand name in alt text

Alt text has a tiny budget; every word should describe the image or carry a real search term. The brand name does neither:
- People searching the brand name are already on the site.
- A screen-reader user learns nothing from it.
- Brand name on every image is a textbook "stuffing" pattern.

**Only exception:** the brand name or logo is *visibly printed* and is the subject of the image (packaging front, logo wall). Then you're describing text in the image.

```
❌ Acme 20 oz insulated travel mug navy
✅ Navy 20 oz insulated travel mug with flip-top leakproof lid, front view
✅ Exception: Kraft gift box with the ACME logo stamped on the lid
```

### 2. Lock the terminology

Use the store's own product words consistently, and never their near-synonyms. Example for a mug store:

| Always | Never |
|---|---|
| travel mug | tumbler / flask / cup (unless that's what it is) |
| leakproof | leak-resistant / spill-free |
| 20 oz | 20oz / twenty ounce / 600 ml (unless localizing) |

Mixed terms dilute relevance and confuse screen-reader users.

### 3. Never copy alt text across products

Two variants shot from the same angle still get **different** alt text — at least the variant name plus one variant-specific detail. Dozens of images sharing one template sentence is an easy low-quality signal.

### 4. Never write "image of", "photo of", "picture of"

Screen readers already announce "image". Repeating it wastes the budget.

### 5. Use numbers when they exist

"Holds 20 oz", "fits 16-inch laptops", "6 color options". Numbers are specific and are real search terms. "High capacity" is neither.

### 6. Never invent

Describe what is in the image and what the user told you about the product. Don't add specs, certifications or claims you can't see or weren't given.

---

## Length and structure

**Aim for roughly 80–125 characters.** Many screen-reader users experience very long alt text as a burden, and some tools truncate it; past ~125 characters, move detail into the page copy or a caption.

**Structure: subject → key attribute → context/state**

```
[Product type/variant] + [size or capacity] + [material/color/state] + [context, if any]
```

Front-load the first ~60 characters with the product and its distinguishing detail.

```
✅ Navy 20 oz travel mug in a car cup holder, lid closed, steam on the window
   (75 characters — variant, size, product, context)

❌ A high quality premium mug for all your coffee needs on the go
   (adjectives only, nothing specific, no search value)
```

---

## Templates by image type

| # | Image type | What the alt should carry | Template |
|---|---|---|---|
| 1 | **Hero / main image** | Product + variant + key spec. Highest weight. | `[Variant] [size] [product] with [distinctive detail], [view]` |
| 2 | **In use / inside view** | Capacity, fit, compatibility — the core differentiator | `Open [product] showing [what's inside / how it's used]` |
| 3 | **Hardware / detail** | Exact part name + material | `[Part] on a [variant] [product], [material/finish]` |
| 4 | **Material / texture close-up** | Concrete words for feel and craft | `Close-up of [color] [material] with [texture/finish]` |
| 5 | **Size / comparison** | Numbers + the comparison object | `[Product] next to a [familiar object] showing [dimension]` |
| 6 | **Lifestyle / scene** | Who, where, doing what | `[Person] using a [variant] [product] at [place]` |
| 7 | **Packaging / gift** | What gift buyers care about | `[Packaging] for a [variant] [product], [gift-ready detail]` |
| 8 | **Customer photo (UGC)** | Authentic, not written like a studio shot | `Customer photo of a [variant] [product] [in real use]` |

**Blog illustrations:** match the alt to **that section's subheading**, not the article's overall topic. In an article on "how to keep coffee hot longer", an illustration might be `Thermometer reading 140°F in a travel mug after six hours`, not `coffee guide`.

**Decorative images** (dividers, background textures, purely ornamental icons) get **empty alt** (`alt=""`) so screen readers skip them. Test: if you deleted the image, would the page lose information? If not, it's decorative.

---

## Image file names (always delivered with the alt)

Search engines read both. Rule:

```
[product]-[variant]-[detail]-[NN].jpg

✅ travel-mug-navy-lid-closeup-02.jpg
✅ travel-mug-gift-box-front-01.jpg
❌ IMG_4821.jpg / DSC00193.jpg / final-v3-USE-THIS.jpg
❌ acme-travel-mug.jpg   (brand-name rule applies to file names too)
```

- All lowercase, hyphen-separated, no underscores or spaces.
- No keyword stuffing: `travel-mug-best-premium-insulated-coffee-mug-cheap.jpg` ❌

---

## Mode A — Generate

**Input:** the images themselves, a list, a product URL, or a short description.

1. Establish (infer if not given — don't stall on questions): the product and variant, the key numbers, where the image sits in the gallery and which of the 8 types it is.
2. Write each alt from its template.
3. **Compare the batch against itself** — no two alts nearly identical.
4. Check ground rules 1–6.
5. Output:

```markdown
| # | Image | Type | File name | Alt text | Chars |
|---|---|---|---|---|---|
| 1 | Main | Hero | travel-mug-navy-front-01.jpg | Navy 20 oz insulated travel mug with flip-top leakproof lid, front view | 72 |
```

End with a one-line batch check: N images, longest X characters, no brand name, no repeated template, terminology consistent.

---

## Mode B — Audit

**Input:** existing alt text (screenshot, CSV, a store export, or pasted). For a quick mechanical pass on a CSV or saved HTML page, run `scripts/alt_audit.py` first.

Six checks per image:

| # | Check | Severity | Fails when |
|---|---|---|---|
| 1 | Alt present | Critical | Missing, empty on a meaningful image, or just the file name |
| 2 | Brand-name rule | Critical | Brand name used on a non-logo image |
| 3 | Terminology | High | Uses a word the store never uses |
| 4 | Specificity | High | Only adjectives; no numbers, parts or context |
| 5 | Length | Medium | Over ~125 or under ~20 characters |
| 6 | Duplicates in batch | Medium | Several images share one sentence |

**Output:**

```markdown
## Alt text audit — N images, M need changes

**Verdict:** <one line>

| # | Current alt | Problems | Rewrite |
|---|---|---|---|
| 3 | Acme premium mug | Rule 1 brand name · check 4 nothing specific | Matte black 12 oz travel mug with bamboo lid, side view |

### Fix these 3 first
1. <which, and why it's most urgent>
```

List only the images that need changes; summarize the rest in one line ("The other 12 pass").

---

## Common mistakes

| Wrong | Problem | Better |
|---|---|---|
| `Acme Travel Mug` | Brand name, no information | `Navy 20 oz travel mug with leakproof lid, front view` |
| `Best premium high quality mug` | Adjectives only | `Double-wall stainless steel travel mug with bamboo lid` |
| `mug` | Too short | `Sage green 12 oz travel mug on a desk next to a laptop` |
| `mug travel mug coffee mug insulated mug` | Keyword stuffing | `Insulated travel mug with flip-top lid in a car cup holder` |
| `Image of a red mug` | "Image of" | `Red 16 oz travel mug with handle, lid open` |
| Every image: `travel mug` | Batch duplicates | Rewrite each from its type template |
