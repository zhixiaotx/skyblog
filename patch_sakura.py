import re, os, glob

ROOT = os.path.dirname(os.path.abspath(__file__))
LAYOUT = os.path.join(ROOT, "themes", "sakura", "layout")

# 1) ejs: 把字面量根路径 href="/x" / src="/x" 包成 url_for('/x')
attr_re = re.compile(r'''(?P<attr>href|src)=(?P<q>["'])(?P<val>/[^"']*?)(?P=q)''')

def patch_ejs(path):
    with open(path, encoding="utf-8") as f:
        s = f.read()
    orig = s

    def repl(m):
        val = m.group("val")
        if val.startswith("//"):          # 协议相对，保持原样
            return m.group(0)
        q = m.group("q")
        return f'{m.group("attr")}={q}<%- url_for(\'{val}\') %>{q}'

    s = attr_re.sub(repl, s)
    # favicon / avatar 输出包成 url_for
    s = s.replace('href="<%- theme.favicon %>"', 'href="<%- url_for(theme.favicon) %>"')
    s = re.sub(
        r'src="<%- \(theme\.cdn \|\| \'\'\) \+ theme\.avatar ?%>"',
        'src="<%- url_for((theme.cdn || \'\') + theme.avatar) %>"',
        s,
    )
    if s != orig:
        with open(path, "w", encoding="utf-8") as f:
            f.write(s)
        return True
    return False

count = 0
for p in glob.glob(os.path.join(LAYOUT, "**", "*.ejs"), recursive=True):
    if patch_ejs(p):
        count += 1
print(f"[ejs] patched {count} files")

# 2) CSS: url(/images/...) -> url(../images/...)  (兼容 /skyblog/ 子目录)
css_count = 0
for p in glob.glob(os.path.join(ROOT, "themes", "sakura", "source", "css", "**", "*"), recursive=True):
    if not os.path.isfile(p):
        continue
    if not p.endswith((".css", ".styl")):
        continue
    with open(p, encoding="utf-8") as f:
        s = f.read()
    if "url(/images/" in s:
        s2 = s.replace("url(/images/", "url(../images/")
        with open(p, "w", encoding="utf-8") as f:
            f.write(s2)
        css_count += 1
        print(f"[css] patched {os.path.relpath(p, ROOT)}")
print(f"[css] patched {css_count} files")
