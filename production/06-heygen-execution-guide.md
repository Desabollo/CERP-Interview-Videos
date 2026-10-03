# 06 — HeyGen Execution Guide (Series A · BOARDROOM-READY)

**Decision:** HeyGen is the video-generation tool for Category A interview episodes.
**Selected by client:** 3 Oct 2026 ("use heygen"). Supersedes "tool-agnostic prompts, adapt on selection" (05 §4.1).
**Scope:** All GFC-series episodes (Wave 1, Wave 2, and future waves). Pilot = **GFC-E06** (only episode with recorded voice assets + previz).
**Facts current as of 3 Oct 2026** — verify HeyGen plan limits/engine availability at execution; do not hard-code pricing in client materials.

---

## 1. How our production model maps to HeyGen

We do **dialogue-by-beats**: each storyboard row = one speaking beat = **one HeyGen scene** (one avatar, one line/paragraph). The editor cuts between alternating "singles" exactly as in the E06 previz animatic. This matches how the packages were designed (shots ≤ 8–10 s, sentence-boundary splits) and keeps every visual control we already have.

| Our package field | HeyGen equivalent |
|---|---|
| Character prompts + cast plates | **Photo avatars** built once from `assets/cast/*.jpg`; locked looks (wardrobe already inside the plate) |
| Scene prompts / set references | Avatar look background (baked into plate) + optional uploaded set image `assets/set/SET-lagos-boardroom_ref.jpg` as scene background |
| Motion prompts | `motion_prompt` (Avatar V engines) / gesture direction at scene level — one short instruction per scene (§5) |
| Voice prompts | **Audio mode** (uploaded MP3, lip-synced) where recorded assets exist (E06) · **Script mode** (HeyGen TTS voice) elsewhere, keeping our spell-outs & letter-spacing (§4) |
| Error-negatives | No negative-prompt field in HeyGen → becomes the "never direct" list (§5) + G3 QC checklist (§9) |
| Shot list (SH-ids) | Scene IDs in this guide (`S1…Sn` per episode) |
| Editing/export package | **Unchanged** — HeyGen MP4s are the "shots"; captions, chips, lower thirds, end card remain edit-time overlays |

**What HeyGen does NOT do natively (plan accordingly):**
- **True two-shots / OTS angles.** Wide cold-opens and over-the-shoulder beats become: alternating singles + hook/topic chips in edit + (optional) freeze-frame reaction inserts taken from already-rendered frames. Signed-off substitution; storyboards remain visual intent, *scene plans are the executing contract*.
- **Free camera moves (push-ins).** Achieve in edit (2–3% scale ramp over the clip) — same result as our previz.
- **On-screen text.** Never ask the avatar/scene to render text; all chips/captions/cards are overlays in edit.

## 2. One-time HeyGen workspace setup (≈30 min, at app.heygen.com)

### 2.1 Photo avatars (record the returned IDs in §10)
1. **Avatars → Create photo avatar → upload front-facing image:**
   - `production/assets/cast/INT-01_adaeze-nwosu_ref.jpg` → name **`CEABS-INT-01`** ("Mrs. Adaeze Nwosu", recurring interviewer)
   - `production/assets/cast/CAND-GFC-01_olumide-adeyemi_ref.jpg` → name **`CEABS-CAND-GFC-01`** ("Mr. Olumide Adeyemi", GFC candidate)
   - `production/assets/cast/INT-02_chijioke-eze_ref.jpg` → name **`CEABS-INT-02`** (reserved — panel format, Wave 3+)
2. **Consent/rights step:** our plates are original AI-generated fictional people — we hold the rights; if HeyGen's flow requires a video consent for photo avatars on your plan, fall back per §11-B.
3. Create **one look per avatar** (the plate IS the look: wardrobe + Lagos-boardroom background). Never generate additional looks per episode — wardrobe continuity rule (03-cast sheet).
4. Test-render 3 s on each avatar with any audio; verify: face matches plate, blazer/suit unchanged, no jewelry drift. Save the **avatar_id** for each.

### 2.2 Brand kit (Studio → Brand)
- Colours (tokens `[approx]` until pixel-verified at logo ingest — D10): primary **CE-BLUE `#1B86C9`**, secondary **CE-NAVY `#172A5B`**, accent **CE-CYAN `#2FB9E8`**. Replace at ingest.
- Font: closest available to Montserrat/Inter (used across the programme).
- Caption preset: **white semibold, subtle navy highlight pill, positioned bottom-third but above y=1140px equivalent** (below captions our lower thirds live 1140–1260 — see 01 §graphics language). Do NOT rely on HeyGen's default caption placement.
- Upload set image `assets/set/SET-lagos-boardroom_ref.jpg` as a **custom background asset** (optional; plates already contain the room).

### 2.3 Voice assets (E06 — audio mode)
Upload to your audio library (each becomes an `audio_asset_id`):
`assets/audio/E06/`: **E06-V01** (int01 question, 3.7 s) · **E06-V02a** (framework, 4.0 s) · **E06-V02b** (assess, 8.8 s) · **E06-V03** (memo, 7.8 s) · **E06-V04a** (close-matrix, 11.7 s) · **E06-V04b** (policy, 5.2 s) · **E06-V05** (institutionalise, 13.3 s) · **E06-V06** (success, 9.3 s).
These are our recorded `voice-03`/`voice-04` performances with exact letter-spelled acronyms — **audio mode preserves voice continuity and pronunciation exactly**.

### 2.4 HeyGen voice for script mode (E01–E05, E07–E09, E20 — until recorded)
1. Audition HeyGen voice library for an **African/Nigerian English-accented voice** matching: INT-01 = warm feminine, measured (≈145 wpm); CAND-GFC-01 = baritone, unhurried (≈140 wpm).
2. If no Nigerian-accented English voice exists at execution time (see D3/D11), pick the closest neutral-international voice; set **speed 0.95**, and if the engine exposes ElevenLabs-style knobs: **stability 0.7, similarity 0.7, style 0.3**.
3. Script text goes in **exactly as written in episode §B** — letter-spellings (`E R P`, `K P Is`), spell-outs (`IFRS` as "eye-eff-ar-ess" is *already applied* where needed) and spelled numerals are part of the copy. Do not "clean up" the script text.
4. Record chosen `voice_id`s in §10. Premium option later: clone consented VO talent to replace `voice-03/04` permanently.

## 3. Mapping rules for every episode

1. **1 storyboard row = 1 scene** (speaker beats). Split any beat at sentence boundaries if > ~12–15 s (heygen renders longer lines less reliably and QC gets harder).
2. **Speaker → avatar:** INT-01 lines → `CEABS-INT-01`; candidate lines → `CEABS-CAND-GFC-01`; (INT-02 follow-ups → `CEABS-INT-02`, panel waves only).
3. **Framing:** plate crops give MS/MCU. For edit variety, render the *same* beat a second time with avatar scaled ~110–115% on canvas (creates the MCU for emphasis beats) — cheaper than re-writing motion prompts.
4. **Captions:** enable SRT sidecar on every render (`caption.file_format: srt`); we restyle and reposition in edit. Turn **off** HeyGen burned captions for masters.
5. **Overlays (edit-time, never in HeyGen):** hook chip (first 2 s), topic chip, speaker lower thirds, phase/list chips, *illustrative* tags on quantified claims, takeaway card, end card, "AI-generated interview simulation" disclosure.
6. **End card (all episodes):** append PNG in edit (3.0–3.5 s) — the E06 previz end card is the template; swaps to the real lockup at logo ingest (D9). Do not build end cards inside HeyGen.
7. **Hook A/B:** hook text variants (E03, E06) are chip overlays at export (`_hookB` master) — **no re-rendering**.

## 4. Motion-prompt dictionary (use these, one per scene)

Derived from 03-cast-sheet "Shared performance direction". Keep ≤ 14 words, present tense, exactly one behaviour cluster:

| Code | Prompt text | Used for |
|---|---|---|
| MO-ASK | "leans in slightly while asking, warm confident authority, small nod on final word" | INT-01 questions |
| MO-FRAME | "brief composed pause, then states the headline on raised fingers, calm steady eye contact" | framework openers |
| MO-LIST | "enumerates points on fingers at a measured pace, still upper body, board-room calm" | enumerations |
| MO-EMPH | "quiet emphasis on the named phrase, slight forward settle, minimal hand movement" | key-insight beats |
| MO-MEASURE | "weights the key word deliberately, small affirming nod, unhurried" | metrics/results beats |
| MO-LAND | "settles into the final clause, calm certainty, holds eye contact to the end" | closers |
| MO-CALM | "composed breath, neutral warm expression, no hand movement" | pause/reaction-adjacent beats |
| MO-REACT | "attentive listening nod, slight smile, hands still" | INT-02 panel reactions (Wave 3+) |

**Never direct (our negatives as motion constraints):** walking, standing, turning away, large arm gestures, pointing at camera, exaggerated smiling, looking into lens mid-dialogue, holding props other than the folio/pen, scene-to-scene wardrobe or lighting changes.

For engines without motion prompts (photo-avatar default), behaviour comes from the audio + idle engine — QC at G3 against the same list.

## 5. HeyGen UI pipeline (per episode)

1. Create project → **9:16 (1080×1920)**.
2. For each scene in the episode plan: add scene → pick avatar (`CEABS-*`) → set background (avatar look or set-plate asset) → **Audio:** attach the beat's MP3 **or** paste the beat's script text + selected voice → motion prompt from dictionary → captions on (SRT sidecar).
3. Preview the scene's start frame (avatar fidelity vs plate: face/wardrobe/background).
4. Render scenes (batch). Download each MP4 + SRT.
5. Name exactly: `<EP>_HeyGen_S<n>_<avatar>_<v1>.mp4` → hand to edit per episode §F.
6. Log render date/IDs in the episode's §H manifest; mark G3 QC (§9) then send assembled rough cut for review.

## 6. API v3 template (identical scenes, scriptable)

```bash
# Prereq: HEYGEN_API_KEY (workspace settings → API). One call per scene.
curl -X POST https://api.heygen.com/v3/videos \
  -H "x-api-key: $HEYGEN_API_KEY" -H "Content-Type: application/json" -d '{
  "type": "avatar",
  "avatar_id": "<CEABS-CAND-GFC-01 avatar_id>",
  "title": "GFC-E06_S2_framework",
  "aspect_ratio": "9:16",
  "audio_asset_id": "<E06-V02a audio_asset_id>",
  "caption": { "file_format": "srt" },
  "background": { "asset_id": "<SET-lagos-boardroom asset_id (optional)>" },
  "motion_prompt": "brief composed pause, then states the headline on raised fingers, calm steady eye contact",
  "output_format": "mp4"
}'
# Poll the returned video id until completed; download MP4 + subtitle_url SRT.
```
Script mode: replace `audio_asset_id` with `"script": "<beat text>", "voice_id": "<voice_id>"` (+ `voice_settings`).
Keep the key out of Git (local `.env`, gitignored). If you prefer to drive renders from here, add the key to the sandbox environment and I'll batch all scenes.

## 7. Pilot — GFC-E06 HeyGen scene plan (LOCKED ← §B script + recorded audio previz-verified)

| Scene | Avatar | Audio asset (mode) | Exact beat (source §B) | Motion | Dur |
|---|---|---|---|---|---|
| S1 | CEABS-INT-01 | E06-V01 (3.7 s) | "What would your first ninety days as Group Financial Controller look like?" | MO-ASK | 3.7 |
| S2 | CEABS-CAND-GFC-01 | E06-V02a (4.0 s) | "I run it in three phases — assess, design, institutionalise." | MO-FRAME | 4.0 |
| S3 | CEABS-CAND-GFC-01 | E06-V02b (8.8 s) | "Days one to thirty: map the entities, people, chart of accounts and systems; time the current close end-to-end; inventory reconciliations and controls." | MO-LIST | 8.8 |
| S4 | CEABS-CAND-GFC-01 | E06-V03 (7.8 s) | "Then I publish a findings memo with quick wins — high-risk reconciliations, cut-off fixes, ERP functionality we already own." | MO-EMPH | 7.8 |
| S5 | CEABS-CAND-GFC-01 | E06-V04a (11.7 s) | "Days thirty-one to sixty: a redesigned close calendar with hour-level ownership; a consolidation pack and eliminations matrix; a controls matrix for segregation of duties and delegation limits;" | MO-LIST | 11.7 |
| S6 | CEABS-CAND-GFC-01 | E06-V04b (5.2 s) | "and policy papers for the highest-risk areas — revenue, leases, credit losses." | MO-CALM | 5.2 |
| S7 | CEABS-CAND-GFC-01 | E06-V05 (13.3 s) | "Days sixty-one to ninety: run one full close under the new framework and measure it — close days, reconciliation completion, late adjustments. Publish the KPIs and deliver the first board-standard reporting pack." | MO-MEASURE | 13.3 |
| S8 | CEABS-CAND-GFC-01 | E06-V06 (9.3 s) | "Success looks like: a faster close, key reconciliations one hundred per cent current, and a leadership team that trusts the numbers without a caveat." | MO-LAND | 9.3 |
| (cards) | — | — | Takeaway card 3.5 s + end card 3.5 s — **edit-time overlays**, not HeyGen scenes | — | 7.0 |

* V02→V02a/b split at the silence after "institutionalise." (3.9 s mark); V04→V04a/b at the silence after "delegation limits;" (11.6 s) — files pre-cut in `assets/audio/E06/`. Unsplit masters retained for continuity.
* If S7's 13.3 s fails a plan limit: split after "late adjustments." using the same recipe: `ffmpeg -i E06-V05.mp3 -af silencedetect=noise=-35dB:d=0.3 -f null -` → cut at silence.
* **Camera variety in edit:** S3 and S5 use the ~112% scale variant (MCU); add 2–3% scale ramp on S8 (the "slow push" from the storyboard).
* **Reaction inserts (optional):** 1.0–1.5 s freeze-frame of INT-01 from an S1 frame, inserted between S4/S5 — replaces silent renders.
* Hook chip covers 0–2 s of S1; E06 meets the ≤2 s hook rule (question IS the hook). Hook-B variant = different chip, same renders.
* **Expected final master: ≈ 70.8 s** (audio beats 63.8 + cards 7.0) — inside the 45–75 s window.

## 8. Other episodes (Wave 1–2) — quick-map table

Same rules; script-mode voice per §2.4 until recorded. Beat counts from each §C:

| Episode | Scenes (beats) | Split guidance | Notes |
|---|---|---|---|
| GFC-E01 | 6–7 | CAND answers split at semicolon boundaries | — |
| GFC-E02 | 6–7 | "Five layers" enumeration = one scene (MO-LIST) | takeaway chip: layer names |
| GFC-E03 | 5–6 | hook A/B edit-time only | shortest dialogue |
| GFC-E04 | 7 | IFRS 15 five areas split 3+2 | like E06 S5/S6 |
| GFC-E05 | 6–7 | three pillars = one scene each where >10 s | — |
| GFC-E07 | 5–6 | SoD/DoA enumeration one scene | internal-controls insight link in description (approved) |
| GFC-E08 | 6 | adoption beats = MO-EMPH | services/erp-implementation link in description (approved) |
| GFC-E09 | 6–7 | multicurrency list split at ";" | — |
| GFC-E20 | 5 | closer MO-LAND, hold 0.4 s | series finale of Wave 1 |

## 9. QC at G3 (HeyGen render review — updates 05 §1 G3)

Per rendered scene before assembly:
- [ ] Face/wardrobe **identical** to approved plate (`03` identity controls) — any drift → re-render, never fix in edit
- [ ] Lip-sync lands on letter-spelled acronyms (E R P, K P Is) and key numbers; no mouth-freeze on silence beats
- [ ] Hands/fingers anatomically clean during MO-LIST/MO-FRAME (re-render on morphing)
- [ ] No "never direct" behaviours (§4 list) present
- [ ] Background = approved boardroom; no invented people, logos, or text in frame
- [ ] SRT matches §B verbatim (HeyGen hears *your* audio — mismatches flag audio upload errors)
- [ ] Single-scene resolution/rate: 1080×1920 @ 30 (or scaled on delivery if plan renders capped — record actual in manifest)

## 10. IDs on file (fill in at setup — keep this table current)

| Item | Value |
|---|---|
| HeyGen workspace/project folder | _to fill_ |
| CEABS-INT-01 avatar_id | _to fill_ |
| CEABS-CAND-GFC-01 avatar_id | _to fill_ |
| CEABS-INT-02 avatar_id (reserved) | _to fill_ |
| INT-01 voice (script mode) voice_id | _to fill_ (fallback until `voice-03` recorded/clone) |
| CAND-GFC-01 voice voice_id | _to fill_ (fallback until `voice-04` recorded/clone) |
| E06 audio_asset_ids (V01, V02a, V02b, V03, V04a, V04b, V05, V06) | _to fill_ |
| Brand kit / caption preset name | _to fill_ |
| Plan/render limits observed | _to fill_ |

## 11. Gotchas & fallbacks

- **A. Free-plan watermark/low-res:** masters must be watermark-free 1080p — requires a paid plan tier; draft passes may use anything, masters may not.
- **B. Photo-avatar consent flow blocks upload:** fall back to closest visual stock avatars (Black African professional matches to 03 descriptors) **only after noting the substitution in 05-review**; our continuity anchor stays the cast plates + voices.
- **C. Engine eligibility:** motion prompts apply to Avatar V-capable avatars; photo avatars may render on Avatar IV with idle motion — QC at G3 either way.
- **D. Mispronunciation (script mode):** consult the 03 pronunciation key — spell it out in the script text (e.g. "naira" stays "naira"; "IFRS fifteen" if the voice mangles the numeral). Log at G3.
- **E. Scene length ceilings:** vary by plan; recipe for splitting audio is in §7 note. Prefer audio-mode splits at natural silences over mid-word cuts in edit.
- **F. Render budget:** pilot = E06's 8 scenes only; get sign-off at G3/G4 before batching the other ~55 scenes of Waves 1–2.

## 12. Next actions

1. **Client (in HeyGen):** execute §2 setup; fill §10; render pilot E06 scenes (§7); upload scene MP4s + SRTs (portal route works for these too, or repo upload per INGEST-style steps).
2. **This workspace (on receipt):** G3 review → assemble rough cut (captions/chips/end card per §F) → G4 pre-publish package.
3. **Logo ingest (D9):** unchanged — portal (8901) or repo upload; end card then rebuilds with true lockup and pixel-sampled hex.
