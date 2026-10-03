#!/usr/bin/env python3
"""Build GFC-E06 previsualization animatic (1080x1920, 30fps).
Stills + PIL-rendered overlay PNGs + synthetic voice MP3s -> MP4 via imageio-ffmpeg static binary.
All text is rendered with PIL (no libfreetype in the static ffmpeg build).
Output: GFC-E06_previz_v1.mp4 + GFC-E06_captions.srt  (PREVISUALIZATION — NOT FINAL VIDEO)
"""
import os, subprocess, textwrap, json
from mutagen.mp3 import MP3
from PIL import Image, ImageDraw, ImageFont
import imageio_ffmpeg, matplotlib

ROOT = os.path.dirname(os.path.abspath(__file__))
A = os.path.join(ROOT, "..", "assets")
PNG = os.path.join(ROOT, "_png")
os.makedirs(PNG, exist_ok=True)
FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()
FONTDIR = os.path.join(os.path.dirname(matplotlib.__file__), "mpl-data", "fonts", "ttf")
FB = os.path.join(FONTDIR, "DejaVuSans-Bold.ttf")
FR = os.path.join(FONTDIR, "DejaVuSans.ttf")

NAVY = (23, 42, 91); TEAL = (27, 134, 201); GOLD = (47, 185, 232)  # brand v2: CE-NAVY/CE-BLUE/CE-CYAN
OFFW = (247, 249, 250); CHAR = (31, 41, 51); WGREY = (185, 180, 172)
W, H = 1080, 1920

def fnt(path, size): return ImageFont.truetype(path, size)
def wrap(draw, text, font, maxw):
    words = text.split(); lines, cur = [], ""
    for w_ in words:
        t = (cur + " " + w_).strip()
        if draw.textlength(t, font=font) <= maxw: cur = t
        else:
            if cur: lines.append(cur)
            cur = w_
    if cur: lines.append(cur)
    return lines

def text_block(draw, xy, text, font, fill, maxw, lh=1.28, anchor_center=False, cx=None):
    lines = wrap(draw, text, font, maxw); x, y = xy
    asc, desc = font.getmetrics(); step = int((asc + desc) * lh)
    for ln in lines:
        if anchor_center:
            draw.text((cx, y), ln, font=font, fill=fill, anchor="ma")
        else:
            draw.text((x, y), ln, font=font, fill=fill)
        y += step
    return y

def watermark(draw):
    f = fnt(FB, 24)
    tw = draw.textlength("PREVISUALIZATION", font=f)
    x0 = W - 60 - tw - 48
    draw.rounded_rectangle([x0, 42, W - 60, 88], 14, fill=(23, 42, 91, 165))
    draw.text((x0 + 24, 65), "PREVISUALIZATION", font=f, fill=(247, 249, 250, 235), anchor="lm")

def chip(draw, xy, text, font, bg, fg, pad=22):
    x, y = xy
    tw = draw.textlength(text, font=font); asc, desc = font.getmetrics(); th = asc + desc
    draw.rounded_rectangle([x, y, x + tw + 2*pad, y + th + int(1.2*pad)], radius=int((th + 2*pad)/2), fill=bg)
    draw.text((x + pad, y + int(0.42*pad)), text, font=font, fill=fg)
    return x + tw + 2*pad

# ---------------- caption chunks (display text, proper casing; timings proportional) ----------
CLIPS = [
    ("E06-V01_int01_question.mp3", ["What would your first ninety days as Group Financial Controller look like?"]),
    ("E06-V02_cand_assess.mp3", ["I run it in three phases \u2014 assess, design, institutionalise.",
                                  "Days one to thirty: map the entities, people, chart of accounts and systems;",
                                  "time the current close end-to-end; inventory reconciliations and controls."]),
    ("E06-V03_cand_memo.mp3", ["Then I publish a findings memo with quick wins \u2014",
                                "high-risk reconciliations, cut-off fixes, ERP functionality we already own."]),
    ("E06-V04_cand_design.mp3", ["Days thirty-one to sixty: a redesigned close calendar with hour-level ownership;",
                                  "a consolidation pack and eliminations matrix; a controls matrix for segregation of duties and delegation limits;",
                                  "and policy papers for the highest-risk areas \u2014 revenue, leases, credit losses."]),
    ("E06-V05_cand_institutionalise.mp3", ["Days sixty-one to ninety: run one full close under the new framework and measure it \u2014",
                                            "close days, reconciliation completion, late adjustments.",
                                            "Publish the KPIs and deliver the first board-standard reporting pack."]),
    ("E06-V06_cand_success.mp3", ["Success looks like: a faster close, key reconciliations one hundred per cent current,",
                                   "and a leadership team that trusts the numbers without a caveat."]),
]
PRE, GAP = 2.0, 0.35
TAKE_D, END_D = 3.5, 4.0

durs = [MP3(os.path.join(A, "audio", "E06", c[0])).info.length for c in CLIPS]
segs, t = [], PRE
seg_times = [(0.0, PRE)]
for i, d in enumerate(durs):
    segs.append((t, t + d)); t += d + GAP
t -= GAP
take_start, end_start = t, t + TAKE_D
TOTAL = t + TAKE_D + END_D

# ---------------- render overlay PNGs ----------
def new_overlay():
    return Image.new("RGBA", (W, H), (0, 0, 0, 0))

def strap(draw, name, role):
    draw.rounded_rectangle([0, 1140, 760, 1140+120], 0, fill=(23, 42, 91, 205))
    draw.text((54, 1155), name, font=fnt(FB, 42), fill=OFFW)
    draw.text((54, 1219), role, font=fnt(FR, 30), fill=WGREY)

def topic(draw, txt="GROUP FINANCIAL CONTROLLER \u00b7 E06"):
    chip(draw, (54, 180), txt, fnt(FB, 30), (27, 134, 201, 220), OFFW)

# topic + interviewer strap
im = new_overlay(); d = ImageDraw.Draw(im); topic(d); strap(d, "Adaeze Nwosu", "Group CFO \u00b7 interviewer (fictional)"); watermark(d)
im.save(f"{PNG}/ov_q.png")
# candidate strap + phase chips
def cand_overlay(fn, phasetxt=None):
    im = new_overlay(); d = ImageDraw.Draw(im); topic(d); strap(d, "Olumide Adeyemi", "Candidate \u00b7 Group Financial Controller (fictional)")
    if phasetxt: chip(d, (54, 250), phasetxt, fnt(FB, 34), (23, 42, 91, 210), OFFW)
    watermark(d); im.save(fn)
cand_overlay(f"{PNG}/ov_p1.png", "PHASE 1/3 \u00b7 ASSESS \u2014 DAYS 1\u201330")
cand_overlay(f"{PNG}/ov_p2.png", "PHASE 2/3 \u00b7 DESIGN \u2014 DAYS 31\u201360")
cand_overlay(f"{PNG}/ov_p3.png", "PHASE 3/3 \u00b7 INSTITUTIONALISE \u2014 DAYS 61\u201390")
cand_overlay(f"{PNG}/ov_pf.png", None)

# caption PNGs
cap_png = []
ci = 0
for (clipfile, chunks), (s, e) in zip(CLIPS, segs):
    total_chars = sum(len(c) for c in chunks)
    tcur = s
    for c in chunks:
        cd = max(1.2, (e - s) * len(c) / max(1, total_chars))
        cd = min(cd, e - tcur + 0.001)
        im = new_overlay(); d = ImageDraw.Draw(im); watermark(d)
        font = fnt(FB, 44)
        lines = wrap(d, c, font, W - 2*70)
        asc, desc = font.getmetrics(); lh = int((asc + desc) * 1.3); bh = lh*len(lines) + 44
        y0 = H - 400 - bh
        d.rounded_rectangle([46, y0, W-46, y0 + bh], 18, fill=(23, 42, 91, 175))
        yy = y0 + 22
        for ln in lines:
            d.text((W/2, yy), ln, font=font, fill=OFFW, anchor="ma"); yy += lh
        fn = f"{PNG}/cap_{ci:02d}.png"; im.save(fn)
        cap_png.append((fn, tcur + 0.10, min(e, tcur + cd) - 0.06))
        tcur += cd; ci += 1

# full-frame cards
def hook_card():
    im = Image.new("RGB", (W, H), NAVY); d = ImageDraw.Draw(im)
    chip(d, (60, 200), "BOARDROOM-READY \u00b7 CLOUDERP", fnt(FB, 34), (27, 134, 201, 255), OFFW)
    y = text_block(d, (60, 640), "Day one.", fnt(FB, 110), OFFW, W-120)
    y = text_block(d, (60, y+10), "Ninety days.", fnt(FB, 110), OFFW, W-120)
    y = text_block(d, (60, y+10), "What changes?", fnt(FB, 110), GOLD, W-120)
    d.rectangle([60, 600, 210, 612], fill=TEAL)
    d.text((60, H-330), "The first-90-days question, answered by a fictional", font=fnt(FR, 38), fill=WGREY)
    d.text((60, H-280), "Group Financial Controller candidate.", font=fnt(FR, 38), fill=WGREY)
    d.text((60, H-160), "AI-generated interview simulation \u00b7 educational purposes", font=fnt(FR, 28), fill=(120, 135, 150))
    watermark(d); im.save(f"{PNG}/card_hook.png")
def takeaway_card():
    im = Image.new("RGB", (W, H), NAVY); d = ImageDraw.Draw(im)
    d.rectangle([60, 620, 210, 632], fill=TEAL)
    d.text((60, 660), "KEY TAKEAWAY", font=fnt(FB, 44), fill=(47, 185, 232))
    text_block(d, (60, 740), "Ninety days, three phases: assess the engine, redesign it, prove it with one measured close.", fnt(FB, 64), OFFW, W-120)
    d.text((60, H-140), "CLOUDERP \u00b7 Accounting & Business Solutions", font=fnt(FB, 30), fill=WGREY)
    watermark(d); im.save(f"{PNG}/card_takeaway.png")
def end_card():
    # brand v2: mirrors supplied LinkedIn banner hierarchy; INTERIM text lockup (no redrawn mark) until D9 ingest
    im = Image.new("RGB", (W, H), (255, 255, 255)); d = ImageDraw.Draw(im)
    d.text((W/2, 470), "clouderp", font=fnt(FB, 132), fill=NAVY, anchor="ma")
    d.text((W/2, 600), "A C C O U N T I N G", font=fnt(FR, 40), fill=NAVY, anchor="ma")
    d.rectangle([W/2-330, 680, W/2+330, 684], fill=(27, 134, 201))
    d.text((W/2, 720), "Financial clarity. Connected systems.", font=fnt(FB, 40), fill=NAVY, anchor="ma")
    d.text((W/2, 772), "Confident growth.", font=fnt(FB, 40), fill=NAVY, anchor="ma")
    d.text((W/2, 845), "ERP Implementation  |  Accounting  |  Business Advisory", font=fnt(FR, 30), fill=(90, 100, 115), anchor="ma")
    y = text_block(d, (0, 980), "First 90 days need a plan you can defend?", fnt(FB, 46), CHAR, W-160, anchor_center=True, cx=W/2)
    d.text((W/2, y + 25), "Book a consultation:", font=fnt(FR, 40), fill=CHAR, anchor="ma")
    d.text((W/2, y + 85), "clouderpaccounting.com/book-consultation", font=fnt(FB, 38), fill=(27, 134, 201), anchor="ma")
    d.text((W/2, y + 160), "or WhatsApp +234 708 037 1266", font=fnt(FB, 40), fill=CHAR, anchor="ma")
    d.text((W/2, H-260), "AI-generated interview simulation for educational purposes.", font=fnt(FR, 26), fill=(120, 125, 130), anchor="ma")
    d.text((W/2, H-215), "All characters are fictional; examples are illustrative.", font=fnt(FR, 26), fill=(120, 125, 130), anchor="ma")
    d.text((W/2, H-150), "INTERIM BRAND LOCKUP — final logo art pending (assets/brand/INGEST.md)", font=fnt(FR, 22), fill=(150, 155, 165), anchor="ma")
    watermark(d); im.save(f"{PNG}/card_end.png")
hook_card(); takeaway_card(); end_card()

# ---------------- SRT ----------
def st(t_):
    h_ = int(t_//3600); m_ = int((t_%3600)//60); s_ = t_%60
    return f"{h_:02d}:{m_:02d}:{int(s_):02d},{int((s_%1)*1000):03d}"
srt = []; k = 1
for (clipfile, chunks), (s, e) in zip(CLIPS, segs):
    total_chars = sum(len(c) for c in chunks); tcur = s
    for c in chunks:
        cd = max(1.2, (e - s) * len(c) / max(1, total_chars)); cd = min(cd, e - tcur + 0.001)
        srt.append(f"{k}\n{st(tcur+0.10)} --> {st(min(e, tcur+cd)-0.06)}\n{c}\n"); k += 1; tcur += cd
with open(os.path.join(ROOT, "GFC-E06_captions.srt"), "w") as f: f.write("\n".join(srt))

# ---------------- audio assembly ----------
adin = []
for i, (cf, _) in enumerate(CLIPS):
    adin += ["-i", os.path.join(A, "audio", "E06", cf)]
fc, chains = [], []
for i in range(len(CLIPS)):
    chains.append(f"[{i}:a]aresample=44100,aformat=channel_layouts=stereo[c{i}]")
labels = []
labels.append("[s0]"); chains.insert(0, "anullsrc=r=44100:cl=stereo:d=%.3f[s0]" % PRE)
for i in range(len(CLIPS)):
    labels.append(f"[c{i}]")
    if i < len(CLIPS)-1:
        g = f"g{i}"; chains.append(f"anullsrc=r=44100:cl=stereo:d={GAP}[{g}]"); labels.append(f"[{g}]")
chains.append("anullsrc=r=44100:cl=stereo:d=%.3f[st]" % (TAKE_D + END_D)); labels.append("[st]")
fc.append(";".join(chains) + f";{''.join(labels)}concat=n={len(labels)}:v=0:a=1[af]")
wavout = os.path.join(ROOT, "_dialogue.wav")
subprocess.run([FFMPEG, "-y", "-hide_banner", "-loglevel", "error"] + adin + ["-filter_complex", fc[0], "-map", "[af]", wavout], check=True)

# ---------------- video assembly ----------
INT01 = os.path.join(A, "cast", "INT-01_adaeze-nwosu_ref.jpg")
CAND = os.path.join(A, "cast", "CAND-GFC-01_olumide-adeyemi_ref.jpg")
def zseg(idx, dur, zoom=True):
    N = max(2, int(round(dur*30)))
    if zoom:
        z = f"1.0667*(1+0.05*on/{N})"
        return (f"[{idx}:v]scale=1152:2048:force_original_aspect_ratio=increase,"
                f"zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={N}:s=1080x1920:fps=30[vs{idx}]")
    return (f"[{idx}:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,"
            f"zoompan=z=1.0:x=0:y=0:d={N}:s=1080x1920:fps=30[vs{idx}]")

vin = ["-i", f"{PNG}/card_hook.png",
       "-i", INT01, "-i", CAND, "-i", CAND, "-i", CAND, "-i", CAND, "-i", CAND,
       "-i", f"{PNG}/card_takeaway.png",
       "-i", f"{PNG}/card_end.png",
       "-i", wavout]
ov_files = [(f"{PNG}/ov_q.png", segs[0][0], segs[0][1]),
            (f"{PNG}/ov_p1.png", segs[1][0], segs[2][1]),
            (f"{PNG}/ov_p2.png", segs[3][0], segs[3][1]),
            (f"{PNG}/ov_p3.png", segs[4][0], segs[4][1]),
            (f"{PNG}/ov_pf.png", segs[5][0], segs[5][1])] + cap_png
base_i = 10
for fn, _, _ in ov_files:
    vin += ["-i", fn]

fchains = []
fchains.append(zseg(0, PRE, zoom=False))
fchains.append(zseg(1, segs[0][1]-segs[0][0]))
for i, mot in zip(range(2, 7), [True, False, True, True, True]):
    fchains.append(zseg(i, segs[i-1][1]-segs[i-1][0], zoom=mot))
fchains.append(zseg(7, TAKE_D, zoom=False))
fchains.append(zseg(8, END_D, zoom=False))
fchains.append("[vs0][vs1][vs2][vs3][vs4][vs5][vs6][vs7][vs8]concat=n=9:v=1:a=0[vcat]")
cur = "vcat"
for j, (fn, s, e) in enumerate(ov_files):
    out = f"w{j}"
    fchains.append(f"[{cur}][{base_i+j}:v]overlay=0:0:eof_action=repeat:enable='between(t,{s:.3f},{e:.3f})'[{out}]")
    cur = out
fgraph = ";".join(fchains)

outmp4 = os.path.join(ROOT, "GFC-E06_previz_v2_brand.mp4")
cmd = [FFMPEG, "-y", "-hide_banner", "-loglevel", "error"] + vin + ["-filter_complex", fgraph,
      "-map", f"[{cur}]", "-map", "9:a", "-r", "30", "-c:v", "libx264", "-preset", "medium",
      "-crf", "21", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "128k", "-t", f"{TOTAL:.3f}", outmp4]
print("segments:", json.dumps({"pre": seg_times[0], "clips": segs, "takeaway": [take_start, take_start+TAKE_D], "end": [end_start, end_start+END_D], "total": TOTAL}, indent=1))
subprocess.run(cmd, check=True)
print("OK:", outmp4, os.path.getsize(outmp4), "bytes; total %.2fs" % TOTAL)
# QC frames
for tq, name in [(1.0, "qc_hook"), (segs[0][0]+1.0, "qc_question"), (segs[3][0]+1.5, "qc_design"), (take_start+1.0, "qc_takeaway"), (end_start+1.0, "qc_end")]:
    subprocess.run([FFMPEG, "-y", "-hide_banner", "-loglevel", "error", "-ss", f"{tq:.2f}", "-i", outmp4, "-frames:v", "1", os.path.join(ROOT, f"_qc_{name}.png")], check=True)
print("QC frames written")
