#!/usr/bin/env python3
"""Build a static multi-page site from the markdown books in docs/.

Markdown -> HTML conversion uses pandoc (GFM). The script generates one HTML
page per chapter, a landing page, a sidebar nav, a per-page table of contents,
and prev/next pagers. Output goes to ./site (ready for GitHub Pages).
"""
import html
import re
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).parent.resolve()
DOCS = ROOT / "docs"
OUT = ROOT / "site"

SITE_TITLE = "Biblije"
SITE_TAGLINE = "Praktični priručnici za pravljenje, marketing i podučavanje digitalnih proizvoda uz Claude Code."

# Book configuration: id, title, short label, accent, description, source folder
BOOKS = [
    {
        "id": "claude-code",
        "title": "Claude Code Biblija",
        "subtitle": "Od ideje do digitalnog proizvoda",
        "accent": "#4f46e5",
        "desc": "Kompletan kurs u 14 modula: kako od ideje, bez programerskog znanja, izgraditi, "
                "proveriti i lansirati pravi web proizvod uz Claude Code.",
        "src": "biblija-parts",
    },
    {
        "id": "marketing",
        "title": "Marketing Biblija",
        "subtitle": "Od prvog korisnika do autonomnog marketinškog OS-a",
        "accent": "#0d9488",
        "desc": "Operativni priručnik za SaaS marketing: metrike, pozicioniranje, growth petlje, "
                "lansiranja i autonomni marketinški sistem koji radi sam.",
        "src": "marketing-parts",
    },
    {
        "id": "edukator",
        "title": "Top 5% Edukator",
        "subtitle": "Coaching priručnik",
        "accent": "#db2777",
        "desc": "Trening za trenera: kako od kurikuluma napraviti program koji transformiše polaznike, "
                "zadržava ih do kraja i pretvara njihove rezultate u tvoj brend.",
        "src": "edukator-parts",
    },
]

HEAD_RE = re.compile(r'<h([1-6]) id="([^"]*)"[^>]*>(.*?)</h\1>', re.S)
TAG_RE = re.compile(r"<[^>]+>")


def strip_tags(s: str) -> str:
    return html.unescape(TAG_RE.sub("", s)).strip()


def pandoc(md_path: Path) -> str:
    """Convert a markdown file to an HTML fragment."""
    result = subprocess.run(
        ["pandoc", "--from", "gfm", "--to", "html5", "--no-highlight", "--wrap=none",
         str(md_path)],
        capture_output=True, text=True, check=True,
    )
    return result.stdout


def derive_title(raw: str) -> str:
    """Clean a heading into a sidebar-friendly label."""
    t = raw.strip()
    # Drop leading 'Modul N:', 'Poglavlje N:', 'Dodatak A:' etc. for short label
    return t


def short_label(title: str) -> str:
    m = re.match(r"^(Modul|Poglavlje)\s+(\d+)\s*[:—-]\s*(.+)$", title)
    if m:
        return f"{m.group(2)}. {m.group(3).split('—')[0].split(' - ')[0].strip()}"
    return title


def load_book(book: dict) -> dict:
    src = DOCS / book["src"]
    files = sorted(src.glob("*.md"))
    chapters = []
    for i, f in enumerate(files):
        body = pandoc(f)
        heads = HEAD_RE.findall(body)
        full_title = strip_tags(heads[0][2]) if heads else f.stem
        slug = f"{book['id']}-{f.stem}"
        # TOC: headings after the first, levels firstLevel+1 .. firstLevel+2
        toc = []
        if heads:
            first_level = int(heads[0][0])
            for lvl, hid, htext in heads[1:]:
                lvl = int(lvl)
                rel = lvl - first_level  # 1 or 2 typically
                if rel in (1, 2) and hid:
                    toc.append({"level": rel, "id": hid, "text": strip_tags(htext)})
        chapters.append({
            "file": f,
            "slug": slug,
            "out": f"{slug}.html",
            "title": full_title,
            "label": short_label(full_title) if i > 0 else "Uvod",
            "body": body,
            "toc": toc,
        })
    book["chapters"] = chapters
    return book


def render_sidebar(active_slug: str) -> str:
    out = ['<nav class="sidebar" id="sidebar">']
    out.append('<a href="index.html" class="home-link">← Početna</a>')
    for book in BOOKS:
        collapsed = not any(c["slug"] == active_slug for c in book["chapters"])
        cls = "nav-group collapsed" if collapsed else "nav-group"
        out.append(f'<div class="{cls}">')
        out.append(
            f'<button class="nav-book"><span class="bk-dot" style="background:{book["accent"]}"></span>'
            f'{html.escape(book["title"])}<span class="chev">▼</span></button>'
        )
        out.append('<ul class="chapters">')
        for c in book["chapters"]:
            a = "active" if c["slug"] == active_slug else ""
            out.append(f'<li><a class="{a}" href="{c["out"]}">{html.escape(c["label"])}</a></li>')
        out.append("</ul></div>")
    out.append("</nav>")
    return "\n".join(out)


def render_toc(chapter: dict) -> str:
    if not chapter["toc"]:
        return '<aside class="toc"></aside>'
    out = ['<aside class="toc"><div class="toc-inner">',
           '<div class="toc-title">Na ovoj strani</div><ul>']
    for item in chapter["toc"]:
        out.append(
            f'<li class="lvl-{item["level"]+1}">'
            f'<a href="#{html.escape(item["id"], quote=True)}">{html.escape(item["text"])}</a></li>'
        )
    out.append("</ul></div></aside>")
    return "\n".join(out)


def render_pager(book: dict, idx: int) -> str:
    chapters = book["chapters"]
    prev_c = chapters[idx - 1] if idx > 0 else None
    next_c = chapters[idx + 1] if idx < len(chapters) - 1 else None
    out = ['<nav class="pager">']
    if prev_c:
        out.append(
            f'<a class="prev" href="{prev_c["out"]}"><span class="lbl">← Prethodno</span>'
            f'<span class="ttl">{html.escape(prev_c["label"])}</span></a>'
        )
    else:
        out.append("<span></span>")
    if next_c:
        out.append(
            f'<a class="next" href="{next_c["out"]}"><span class="lbl">Sledeće →</span>'
            f'<span class="ttl">{html.escape(next_c["label"])}</span></a>'
        )
    else:
        out.append("<span></span>")
    out.append("</nav>")
    return "\n".join(out)


def page_shell(title: str, accent: str, sidebar: str, main_html: str, desc: str = "") -> str:
    meta_desc = html.escape(desc or SITE_TAGLINE, quote=True)
    return f"""<!DOCTYPE html>
<html lang="sr" style="--accent:{accent}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>{html.escape(title)} — {SITE_TITLE}</title>
<meta name="description" content="{meta_desc}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{meta_desc}">
<meta property="og:type" content="article">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'><rect width='32' height='32' rx='7' fill='{accent.replace('#','%23')}'/></svg>">
<link rel="stylesheet" href="assets/style.css">
<script>
(function(){{try{{var t=localStorage.getItem('knjige-theme');if(t)document.documentElement.setAttribute('data-theme',t);}}catch(e){{}}}})();
</script>
</head>
<body>
<header class="topbar">
<button class="icon-btn menu-btn" id="menuBtn" aria-label="Meni">☰</button>
<a class="brand" href="index.html"><span class="dot"></span>{SITE_TITLE}</a>
<span class="spacer"></span>
<button class="icon-btn" onclick="toggleTheme()" aria-label="Promeni temu" title="Svetla / tamna tema">◐</button>
</header>
<div class="backdrop" id="backdrop"></div>
<div class="layout">
{sidebar}
<div class="content">
{main_html}
</div>
</div>
<script src="assets/app.js"></script>
</body>
</html>
"""


def build_home() -> str:
    cards = []
    for i, book in enumerate(BOOKS, 1):
        n = len(book["chapters"]) - 1  # exclude intro from "chapters" count phrasing
        first = book["chapters"][0]["out"]
        cards.append(f"""<a class="card" href="{first}" style="--card-accent:{book['accent']}">
<span class="card-bar"></span>
<span class="card-num">KNJIGA {i:02d}</span>
<h2>{html.escape(book['title'])}</h2>
<p>{html.escape(book['desc'])}</p>
<span class="card-meta"><span>{len(book['chapters'])} poglavlja</span><span class="card-cta">Čitaj →</span></span>
</a>""")
    cards_html = "\n".join(cards)
    body = f"""<main class="home">
<section class="hero">
<span class="eyebrow">Edukativni priručnici</span>
<h1>{SITE_TITLE}</h1>
<p>{html.escape(SITE_TAGLINE)}</p>
</section>
<section class="cards">
{cards_html}
</section>
<p class="home-foot">Napravljeno od markdown izvora · pretvoreno u sajt automatski.</p>
</main>"""
    return f"""<!DOCTYPE html>
<html lang="sr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>{SITE_TITLE} — priručnici za digitalne proizvode</title>
<meta name="description" content="{html.escape(SITE_TAGLINE, quote=True)}">
<meta property="og:title" content="{SITE_TITLE}">
<meta property="og:description" content="{html.escape(SITE_TAGLINE, quote=True)}">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'><rect width='32' height='32' rx='7' fill='%234f46e5'/></svg>">
<link rel="stylesheet" href="assets/style.css">
<script>(function(){{try{{var t=localStorage.getItem('knjige-theme');if(t)document.documentElement.setAttribute('data-theme',t);}}catch(e){{}}}})();</script>
</head>
<body>
<header class="topbar">
<a class="brand" href="index.html"><span class="dot"></span>{SITE_TITLE}</a>
<span class="spacer"></span>
<button class="icon-btn" onclick="toggleTheme()" aria-label="Promeni temu" title="Svetla / tamna tema">◐</button>
</header>
{body}
<script src="assets/app.js"></script>
</body>
</html>
"""


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    shutil.copytree(ROOT / "assets", OUT / "assets")

    for book in BOOKS:
        load_book(book)

    # Chapter pages
    total = 0
    for book in BOOKS:
        for idx, c in enumerate(book["chapters"]):
            sidebar = render_sidebar(c["slug"])
            crumbs = (f'<div class="crumbs"><a href="index.html">Početna</a>'
                      f'<span class="sep">/</span>'
                      f'<span>{html.escape(book["title"])}</span></div>')
            article = (f'<div class="article-wrap"><article class="article">'
                       f'{crumbs}{c["body"]}{render_pager(book, idx)}</article></div>')
            main_html = article + render_toc(c)
            page = page_shell(c["title"], book["accent"], sidebar, main_html,
                              desc=f"{book['title']} — {c['title']}")
            (OUT / c["out"]).write_text(page, encoding="utf-8")
            total += 1

    (OUT / "index.html").write_text(build_home(), encoding="utf-8")
    (OUT / ".nojekyll").write_text("", encoding="utf-8")
    # Block all search-engine indexing
    (OUT / "robots.txt").write_text("User-agent: *\nDisallow: /\n", encoding="utf-8")
    print(f"Built {total} chapter pages + home -> {OUT}")
    for book in BOOKS:
        print(f"  - {book['title']}: {len(book['chapters'])} pages")


if __name__ == "__main__":
    main()
