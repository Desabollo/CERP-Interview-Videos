# 02 — Brand Visual System v2 (CloudERP · Series A)

> **Status: brand identity RECEIVED (visuals), master files PENDING.**
> The client supplied three official logo renders (profile/stacked, Facebook banner lockup, LinkedIn banner
> lockup) on 2 Oct 2026. The identity below is decoded from those renders. Hex values marked **[approx]** are
> visually sampled and must be confirmed against the client brand guidelines when the master files land.
> **Defect D9 (open):** the upload pipeline did not deliver the files into this workspace — see
> `assets/brand/INGEST.md` for the one-step fix. Until then, on-screen composites use the clearly-marked
> interim text lockup (no AI-redrawn mark, per the standing logo rule).

## 1. The official identity (from supplied renders)

| Variant (supplied) | Description | Use |
|---|---|---|
| **Stacked / profile** ("Profile Photo-CloudERP.jpeg") | Gradient "C" ribbon mark (cyan → mid blue → deep navy) above lowercase **clouderp** wordmark + letterspaced **ACCOUNTING** | Avatars, square placements, plaque |
| **Horizontal lockup** ("Facebook Banner Logo.jpeg") | "C" mark left of **clouderp / ACCOUNTING** wordmark | End cards, banners, lower-third end tags |
| **LinkedIn banner** ("LinkedIn Banner.png") | Horizontal lockup + divider + tagline "**Financial clarity. Connected systems. Confident growth.**", service line "ERP Implementation \| Accounting \| Business Advisory", URL www.clouderpaccounting.com | Reference for end-card copy hierarchy |

**Verified brand strings (use exactly):** wordmark lowercase `clouderp` · descriptor `ACCOUNTING` (letterspaced) · tagline `Financial clarity. Connected systems. Confident growth.` · services `ERP Implementation | Accounting | Business Advisory` · URL `www.clouderpaccounting.com`.

**Logo handling (standing rule):** composite the exact file asset in editing; never ask an image/video model to redraw or approximate the mark; maintain proportions, clear space (≥ glyph "C" height on all sides), min width 240 px on 1080×1920; no recolours, no shadows. In-scene plaque: logo composited in edit only.

## 2. Colour palette v2 (from supplied identity)

| Token | Hex | Conf. | Use |
|---|---|---|---|
| `CE-NAVY` (primary) | `#172A5B` **[approx]** | visually sampled from wordmark | Cards, straps, scrim bands, plaque, text on light |
| `CE-NAVY-DEEP` | `#12224D` **[approx]** | mark's dark tips | Gradient/depth only |
| `CE-BLUE` (secondary) | `#1B86C9` **[approx]** | mark's mid band | Chips, accents, secondary text-on-light |
| `CE-CYAN` (highlight) | `#2FB9E8` **[approx]** | mark's light end | Takeaway labels, URL text, accent bars, illustrative chip outline |
| `CE-INK` | `#1F2933` | (system neutral) | Body text on light cards |
| `CE-OFFWHITE` | `#F7F9FA` | (system neutral) | Card bg, reversed text |
| `CE-WARMGREY` | `#8A94A6` | (system neutral, cool-shifted) | Secondary text on cards |

**Deprecated from placeholder v1:** `CE-TEAL #0E7C7B` and `CE-GOLD #C9A227` are no longer brand tokens. Existing locked wardrobe accents (teal blouse, gold tie on approved cast plates) remain acceptable as complementary colours — new plates/graphics use cyan/blue family.

Contrast: white on `CE-NAVY` ≈ 12:1 (AAA). Captions: white on 70–80% navy band (≥8:1). Colour never carries meaning alone (labels on every chip).

## 3. Typography

Unchanged from v1 (free, edit-friendly, close to identity's geometric voice): **Sora** SemiBold/Bold for display & cards; **Inter** Medium/SemiBold for captions/straps/chips; tabular lining figures for numerals. Wordmark reproductions of `clouderp / ACCOUNTING` (interim lockup only): Sora Bold lowercase + Inter letterspaced caps — clearly tagged *interim*, replaced by the master asset on ingest.

## 4. Safe zones — unchanged: content-safe x 60–900, y 180–1500 @1080×1920; straps y 1140–1260; captions y ~1340–1520; hook chip (60, 200).

## 5. Template inventory v2 (rebuild once, reuse per episode)

1. `TPL-hook-chip` — cyan-tinted navy chip + Sora hook text (0–2 s).
2. `TPL-topic-chip` — `CE-BLUE` pill, white text: `ROLE · EPISODE`.
3. `TPL-lowerthird` — 70% navy band: name (SemiBold) + fictional title + tiny horizontal logo lockup right side (master asset when ingested).
4. `TPL-captions` — Inter SemiBold on navy band; timings from final audio.
5. `TPL-takeaway` — navy full-frame, `CE-CYAN` "KEY TAKEAWAY" label, Sora lesson line, small stacked lockup bottom-left.
6. `TPL-endcard` — white frame; horizontal lockup (master asset) centred upper-middle; CTA lines navy; URL in `CE-BLUE`; disclosure microcopy grey. Mirrors the LinkedIn banner hierarchy.
7. `TPL-illustrative-chip` — `CE-CYAN`-outline `ILLUSTRATIVE FIGURES` chip, bottom-left y ≈ 1320.

## 6. Wardrobe & prop accents — set plaque, mug and folio stay navy-family (matches identity). New cast plates should bias `CE-CYAN`/`CE-BLUE` accents over teal/gold.

## 7. End-card copy lock (one CTA per video)
> Line 1 (Sora SemiBold, navy): episode-relevant bridge, e.g. *"First 90 days need a plan you can defend?"*
> Line 2 (Inter Medium): *Book a consultation at **clouderpaccounting.com/book-consultation** — or WhatsApp **+234 708 037 1266**.*
> Microcopy (grey): *AI-generated interview simulation for educational purposes. All characters are fictional; figures are illustrative examples.*

Series→brand mapping: **Series A (BOARDROOM-READY) = CloudERP** · Series B (tutorials) excluded this run.
