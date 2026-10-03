#!/usr/bin/env python3
"""One-off logo ingest portal for CloudERP production workspace.
Serves a branded upload page; POSTed images land in production/assets/brand/inbox/.
Stdlib only. Stop this server after ingest."""
import http.server, cgi, os, re, html

ROOT = "/home/user/CERP-Interview-Videos/production/assets/brand"
INBOX = os.path.join(ROOT, "inbox")
os.makedirs(INBOX, exist_ok=True)
ALLOWED = {".jpg", ".jpeg", ".png", ".svg", ".webp"}
MAX = 25 * 1024 * 1024

MAP = [
    ("profile", "logo_stacked"), ("stacked", "logo_stacked"),
    ("facebook", "logo_horizontal"), ("horizontal", "logo_horizontal"),
    ("linkedin", "banner_linkedin"), ("banner", "banner_linkedin"),
]
def dest_name(orig):
    base = os.path.basename(orig) or "file"
    safe = re.sub(r"[^A-Za-z0-9._-]", "_", base)
    stem, ext = os.path.splitext(safe)
    mapped = stem
    for key, name in MAP:
        if key in stem.lower():
            mapped = name; break
    return mapped + ext.lower()

PAGE = """<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>CloudERP logo ingest</title><style>
body{margin:0;font-family:Segoe UI,Arial,sans-serif;background:#172A5B;color:#F7F9FA;display:flex;justify-content:center;padding:40px 16px}
.card{background:#fff;color:#1F2933;max-width:560px;width:100%;border-radius:16px;padding:32px;box-shadow:0 12px 40px rgba(0,0,0,.35)}
h1{font-size:26px;color:#172A5B;margin:0}.sub{color:#5b6572;font-size:14px;margin:6px 0 20px}
ol{font-size:14px;line-height:1.7;color:#37424f;padding-left:20px}
input[type=file]{display:block;margin:18px 0;padding:14px;border:2px dashed #1B86C9;border-radius:10px;width:100%%;box-sizing:border-box;background:#F2F8FC}
button{background:#1B86C9;color:#fff;border:0;border-radius:10px;padding:14px 28px;font-size:16px;font-weight:600;cursor:pointer;width:100%%}
button:hover{background:#172A5B}.done{background:#e9f7ef;border:1px solid #2fae6e;color:#176b3f;border-radius:10px;padding:12px;margin-top:16px;font-size:14px;word-break:break-all}
.note{margin-top:18px;font-size:12px;color:#8A94A6}.brand{font-weight:700;color:#172A5B;font-size:30px}.brand small{display:block;letter-spacing:6px;font-size:12px;color:#1B86C9;font-weight:400}
.list{font-size:13px;color:#37424f}.list b{color:#176b3f}
</style></head><body><div class="card">
<div class="brand">clouderp<small>ACCOUNTING</small></div>
<h1>Logo ingest portal</h1>
<p class="sub">Defect D9 — get the master logo files into the production workspace.</p>
<ol>
<li>Select the three logo files from your device (profile/stacked, Facebook banner, LinkedIn banner).</li>
<li>They are auto-renamed to <b>logo_stacked.jpeg</b>, <b>logo_horizontal.jpeg</b>, <b>banner_linkedin.png</b>.</li>
<li>After upload, tell the production agent: <i>&ldquo;logo ingested&rdquo;</i> — colours get pixel-sampled, end cards rebuilt with the real mark.</li>
</ol>
<form method="POST" action="/upload" enctype="multipart/form-data">
<input type="file" name="files" multiple accept=".jpg,.jpeg,.png,.svg,.webp">
<button type="submit">Upload logo files</button>
</form>
LIST_BLOCK
<p class="note">Files go to production/assets/brand/inbox/ in the CERP-Interview-Videos repo. Images only · 25&nbsp;MB max each.</p>
</div></body></html>"""

class H(http.server.BaseHTTPRequestHandler):
    def _page(self, extra=""):
        files = sorted(os.listdir(INBOX))
        lst = ("<div class='list'><b>Received:</b> " + ", ".join(html.escape(f) for f in files) + "</div>") if files else ""
        body = PAGE.replace("LIST_BLOCK", extra + lst)
        data = body.encode()
        self.send_response(200); self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(data))); self.end_headers(); self.wfile.write(data)
    def do_GET(self): self._page()
    def do_POST(self):
        if self.path != "/upload":
            self.send_error(404); return
        length = int(self.headers.get("Content-Length", 0))
        if length > MAX * 6:
            self._page("<div class='done' style='background:#fdecea;border-color:#c0392b;color:#922'>Upload too large.</div>"); return
        form = cgi.FieldStorage(fp=self.rfile, headers=self.headers, environ={"REQUEST_METHOD": "POST"})
        saved, rejected = [], []
        fields = form["files"] if "files" in form else []
        if not isinstance(fields, list): fields = [fields]
        for f in fields:
            if not getattr(f, "filename", None): continue
            ext = os.path.splitext(f.filename)[1].lower()
            if ext not in ALLOWED: rejected.append(f.filename); continue
            name = dest_name(f.filename)
            with open(os.path.join(INBOX, name), "wb") as out:
                out.write(f.file.read())
            saved.append(name)
        msg = ""
        if saved: msg += "<div class='done'>Saved: " + ", ".join(html.escape(x) for x in saved) + " — now tell the agent <b>logo ingested</b>.</div>"
        if rejected: msg += "<div class='done' style='background:#fdecea;border-color:#c0392b;color:#922'>Rejected (not an image): " + ", ".join(html.escape(x) for x in rejected) + "</div>"
        self._page(msg)
    def log_message(self, *a): pass

if __name__ == "__main__":
    srv = http.server.ThreadingHTTPServer(("0.0.0.0", 8901), H)
    print("ingest portal on :8901", flush=True)
    srv.serve_forever()
