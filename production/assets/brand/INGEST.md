# Logo ingest — one-step fix for defect D9 (OPEN)

**Situation:** the three logo files were attached in chat on 2 Oct 2026 (Profile Photo-CloudERP.jpeg ·
Facebook Banner Logo.jpeg · LinkedIn Banner.png), and the identity is documented from the visible renders
in `02-brand-system.md`. However, the chat attachment pipeline did **not** place the files in this
workspace (same behaviour as the interview-prep PDF, which arrived via paste instead).

**What I cannot do:** composite the *exact* logo into videos/end cards until the binary files reach the repo.
Per the standing rule I will not AI-redraw the mark — the interim text lockup stays until ingest.

**One-step fix (client, ~1 minute) — recommended:** use the **Logo upload portal** live preview
(this workspace runs a small upload server on port 8901; the "Logo upload portal" preview button
opens it). Select the three logo files; they auto-rename and land in `assets/brand/inbox/`.
Then say **"logo ingested"**.

**Alternative route:** upload via GitHub web UI —
1. Open the repo `Desabollo/CERP-Interview-Videos` on GitHub → branch `arena/01a0fd91-cerp-interview-videos`.
2. Add the three files to `production/assets/brand/` (web UI: "Add file → Upload files"), named exactly:

| Your file | Save as |
|---|---|
| Profile Photo-CloudERP.jpeg | `production/assets/brand/logo_stacked.jpeg` |
| Facebook Banner Logo.jpeg | `production/assets/brand/logo_horizontal.jpeg` |
| LinkedIn Banner.png | `production/assets/brand/banner_linkedin.png` |

3. Tell me "logo ingested" — I will: verify proportions/colours, sample exact hex values from the pixels
   (replacing the **[approx]** tokens), build transparent PNG cutouts for edit compositing, regenerate
   the E06 previz end card with the real mark, and close D9.

If the repo route is awkward, any publicly reachable URL to the files works too.
