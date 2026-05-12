import os, re, datetime

files = sorted([
    f for f in os.listdir(".")
    if f.endswith(".html") and f != "index.html"
])

def get_title(filename):
    try:
        with open(filename, encoding="utf-8") as fh:
            content = fh.read(2000)
        m = re.search(r"<title>(.*?)</title>", content, re.IGNORECASE)
        if m:
            return m.group(1).strip()
    except:
        pass
    return filename

items = ""
for f in files:
    title = get_title(f)
    items += f'<li><a href="{f}">{title}</a></li>\n'

now = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>微策展 · 索引</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;1,300&family=EB+Garamond:wght@400;500&display=swap" rel="stylesheet">
<style>
*, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{
  background: #0b1509;
  color: #f3ead3;
  font-family: 'EB Garamond', serif;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 4rem 2rem;
}}
h1 {{
  font-family: 'Cormorant Garamond', serif;
  font-size: clamp(3rem, 10vw, 6rem);
  font-weight: 300;
  font-style: italic;
  letter-spacing: -0.02em;
  margin-bottom: 0.4rem;
  color: #f3ead3;
}}
.sub {{
  font-size: 0.72rem;
  letter-spacing: 0.28em;
  text-transform: uppercase;
  color: #b08a34;
  margin-bottom: 3rem;
}}
hr {{
  width: 60px;
  border: none;
  border-top: 0.5px solid #b08a34;
  margin: 0 auto 3rem;
  opacity: 0.5;
}}
ol {{
  list-style: none;
  width: 100%;
  max-width: 560px;
  counter-reset: items;
}}
ol li {{
  counter-increment: items;
  border-bottom: 0.5px solid rgba(176,138,52,0.15);
  padding: 0.9rem 0;
  display: flex;
  align-items: baseline;
  gap: 1.2rem;
}}
ol li::before {{
  content: counter(items, decimal-leading-zero);
  font-size: 0.68rem;
  letter-spacing: 0.1em;
  color: rgba(176,138,52,0.45);
  min-width: 2ch;
}}
ol li a {{
  font-family: 'EB Garamond', serif;
  font-size: 1.05rem;
  color: #e2c87a;
  text-decoration: none;
  transition: color 0.2s;
}}
ol li a:hover {{ color: #f3ead3; }}
.updated {{
  margin-top: 3rem;
  font-size: 0.68rem;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: rgba(176,138,52,0.3);
}}
</style>
</head>
<body>
<h1>微策展</h1>
<p class="sub">Micro-Curation Archive</p>
<hr>
<ol>
{items}</ol>
<p class="updated">Updated {now}</p>
</body>
</html>"""

with open("index.html", "w", encoding="utf-8") as fh:
    fh.write(html)

print(f"Generated index.html with {len(files)} entries.")
