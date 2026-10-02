# 05 — Quality Review, Defect List & Dependencies

## 1. Review gates

| Gate | Applies to | Rule |
|---|---|---|
| G1 Script review | Every episode before any media generation | Technical/numerical accuracy; faithful condense of source; no sanitised names re-introduced; timing fits 45–75 s |
| G2 Previz review | Episodes with animatic | Pacing, caption load, CTA flow verified on actual audio |
| G3 Video review | Only when real generated video exists | Never mark video quality "passed" without observing the footage |
| G4 Pre-publish | Final master | Mobile preview on-device; YouTube UI safe zones; disclosure ticked |

## 2. Wave-1 review results (this run)

| Episode | G1 script | G2 previz | G3 video | G4 pre-publish |
|---|---|---|---|---|
| GFC-E01 | ✅ passed | n/a | ⬜ open — no footage yet | ⬜ open |
| GFC-E02 | ✅ passed | n/a | ⬜ open | ⬜ open |
| GFC-E03 | ✅ passed | n/a | ⬜ open | ⬜ open |
| GFC-E06 | ✅ passed | ✅ passed — real audio timings: Q 3.7s / answers 63.8s + cards; caption load verified on frames; **v2 rebuilt in brand identity** with interim lockup (D9) | ⬜ open | ⬜ open |
| GFC-E20 | ✅ passed | n/a | ⬜ open | ⬜ open |
| GFC-E04 | ✅ passed (contingency trim marked, ~73 s) | n/a | ⬜ open | ⬜ open |
| GFC-E05 | ✅ passed (two contingency trims, ~73–76 s; hook A/B) | n/a | ⬜ open | ⬜ open |
| GFC-E07 | ✅ passed (~73 s; CloudERP controls-guide link verified live) | n/a | ⬜ open | ⬜ open |
| GFC-E08 | ✅ passed (~70 s; deliberately vendor-free script; ERP service link verified) | n/a | ⬜ open | ⬜ open |
| GFC-E09 | ✅ passed (~71 s; IAS 21 + exchangeability amendment accurate) | n/a | ⬜ open | ⬜ open |

**Script-review scope covered (per programme §12):** technical accuracy of IFRS references (IFRS 10 control criteria incl. de facto considerations; IFRS 3/IAS 36 measurement layer; IAS 21 closing-rate vs average-rate translation and the cumulative translation reserve; close-process mechanics); arithmetic plausibility of retained illustrative figures; sanitisation check (zero prep-pack organisation names in any script, prompt, title or description — verified by grep across `production/`); fictional-character disclosure present in every description; single CTA per episode; durations calculated from real word counts at ~145 wpm + card holds.

## 3. Defect & correction list

| # | Defect | Severity | Correction | Status |
|---|---|---|---|---|
| D1 | ~~No client logo files~~ Superseded by D9 | — | Brand renders received in chat 2 Oct; identity decoded in brand system v2 | Closed → see D9 |
| D2 | Interview prep arrived as pasted text (PDF announced at `/home/user/uploads/` never materialised in sandbox) | Low | None — content received in full; pasted copy is the source of truth for Wave 1 | Closed |
| D3 | Sandbox TTS has no `en-NG` accent model | Medium | Fallback executed: `en` voices `voice-03/04/05` client-selected; Nigerian-English cadence set via voice direction (cast sheet note). Re-audition at final production if Nigerian-accent synthesis becomes available | **Closed — fallback documented** |
| D4 | Previz animatic uses system fallback fonts (Inter/Sora unavailable in sandbox) | Low (previz only) | Final edit uses brand fonts; previz is labelled accordingly | Closed (documented) |
| D5 | E06 runs at the duration cap: previz measured 74.7 s (video) / 75.0 s (audio) — dialogue ends 67.5 s, end card ≈3.7 s | Low | Acceptable for Wave 1; contingency trims pre-marked in script if final footage runs long | Monitoring |
| D6 | E20-SH07 ("Thank you…") is a 1-s micro-line; some video tools mishandle | Low | Fallback documented: cut straight to takeaway card | Documented |
| D7 | First INT-02 plate contained blurred background people (breaks visual-error controls) | Low | Regenerated plate with empty-room constraint; old file overwritten | **Closed** |
| D8 | First previz render: zoompan mis-feed froze on hook card; caption/strap overlap; end-card text overflow and watermark crop | Medium | All fixed in builder (`build_previz.py` patches 1–3); re-verified on QC frames + duration check (74.7 s) | **Closed** |
| D9 | Logo master files unreachable: chat attachments never materialise in this sandbox; site logo is inline SVG (fetcher returns text only); direct download TLS-blocked; not indexed on public web | High (brand) | Exact-file ingest steps in `assets/brand/INGEST.md` (2-min repo upload, fixed filenames) — then pixel-sample hex, cut transparent PNGs, rebuild end cards, close | **Open — client action** |
| D10 | Hex tokens in brand system v2 are visually estimated from renders | Low | Replace with pixel-sampled values at ingest (D9) | Monitoring |

## 4. Unresolved dependencies

1. **Video generation tool** for SH-series shots (client choice: HeyGen / Veo 3 / Runway / Synthesia-class). Prompts are tool-agnostic; adapt syntax at execution.
2. **YouTube channel owner** must enable "Altered content" disclosure per episode at upload (requirement current as of Oct 2026 — verify at upload time).
3. **Client sign-off** on: placeholder brand swap (D1), fictional-candidate treatment of the real prep pack (00 §2.4), and CTA copy (approved route strings).
4. **Music licensing** if underscore is added post-Wave-1 (library/licensed only).

## 5. Publishing compliance checklist (per episode, at upload)

- [ ] Title matches content; no guaranteed-outcome claims
- [ ] First line of description = AI-simulation disclosure
- [ ] "Altered content" setting ticked (realistic synthetic people/voices)
- [ ] Illustrative-figures note present where numbers are cited
- [ ] One CTA; routes stated in words and URL
- [ ] Publisher identified as CloudERP Accounting & Business Solutions
- [ ] No vendor partnership/certification implied; IFRS Foundation attribution where IFRS content is discussed (education/commentary)

## 6. Measurement plan (no invented analytics — framework only)

Track per episode: 3-second hold, average % viewed, completion, saves, shares, relevant comments (questions about the topic), channel page visits, and **qualified enquiries** (consultation bookings/WhatsApp messages referencing the series). Review after each wave; feed learnings into hook A/B choices (E03, E06) and Wave-2 selection. No performance targets are stated as facts; nothing in this programme guarantees reach or sales.
