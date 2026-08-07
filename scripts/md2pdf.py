import html, re, sys
src, fontpx = sys.argv[1], sys.argv[2]
md = open(src).read()
def esc(s):
    s=html.escape(s)
    s=re.sub(r'\[([^\]]+)\]\(([^)]+)\)', lambda m:'<a href="%s">%s</a>'%(m.group(2), m.group(1)), s)
    s=re.sub(r'\*\*(.+?)\*\*',r'<strong>\1</strong>',s)
    s=re.sub(r'(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)',r'<em>\1</em>',s)
    s=re.sub(r'`(.+?)`',r'<code>\1</code>',s)
    return s
lines=md.split("\n"); out=[]; i=0; inlist=False
def closelist():
    global inlist
    if inlist: out.append("</ul>"); inlist=False
while i < len(lines):
    ln=lines[i]; st=ln.strip()
    if st.startswith("|") and i+1<len(lines) and re.match(r'^\s*\|?[\s:|-]+\|?\s*$', lines[i+1]):
        closelist()
        header=[c.strip() for c in st.strip("|").split("|")]
        out.append('<table><thead><tr>'+''.join('<th>%s</th>'%esc(c) for c in header)+'</tr></thead><tbody>')
        i+=2
        while i<len(lines) and lines[i].strip().startswith("|"):
            cells=[c.strip() for c in lines[i].strip().strip("|").split("|")]
            out.append('<tr>'+''.join('<td>%s</td>'%esc(c) for c in cells)+'</tr>')
            i+=1
        out.append('</tbody></table>'); continue
    if st.startswith("- "):
        if not inlist: out.append("<ul>"); inlist=True
        out.append("<li>"+esc(st[2:])+"</li>"); i+=1; continue
    closelist()
    if st=="---": out.append("<hr>")
    elif st.startswith("# "): out.append("<h1>"+esc(st[2:])+"</h1>")
    elif st.startswith("## "): out.append("<h2>"+esc(st[3:])+"</h2>")
    elif st=="": pass
    else: out.append("<p>"+esc(st)+"</p>")
    i+=1
closelist()
doc="""<!DOCTYPE html><html><head><meta charset="utf-8"><style>
body{{font-family:-apple-system,Helvetica,Arial,sans-serif;font-size:{f}px;line-height:1.4;color:#1a1a1a;margin:34px;}}
h1{{font-size:17px;color:#d1410c;margin-bottom:2px;}} h2{{font-size:12.5px;margin-top:14px;border-bottom:1px solid #ddd;padding-bottom:2px;}}
strong{{color:#000;}} em{{color:#555;}} code{{background:#f4f4f4;padding:0 2px;border-radius:2px;font-size:{c}px;}}
ul{{margin:3px 0 6px 0;padding-left:16px;}} li{{margin:2px 0;}} p{{margin:4px 0;}} hr{{border:none;border-top:1px solid #ccc;margin:10px 0;}}
a{{color:#1473e6;text-decoration:none;}}
table{{border-collapse:collapse;width:100%;margin:5px 0 10px;font-size:{c}px;}}
th{{background:#f4f4f4;text-align:left;padding:4px 7px;border:1px solid #ddd;font-size:{c}px;}}
td{{padding:4px 7px;border:1px solid #e2e2e2;vertical-align:top;}}
td:first-child{{white-space:nowrap;font-weight:600;}}
</style></head><body>{b}</body></html>""".format(f=fontpx, c=int(fontpx)-1, b="\n".join(out))
open(src.rsplit(".",1)[0]+".html","w").write(doc)
print("html:", src.rsplit(".",1)[0]+".html")
