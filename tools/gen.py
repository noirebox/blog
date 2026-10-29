#!/usr/bin/env python3
"""Génère depuis INDEX.md, pour chaque article :
  - /fr/<slug>.html et /en/<slug>.html · page complète : title réel, meta description,
    canonical, hreflang, Open Graph, Twitter card et JSON-LD Article injectés ;
  - /posts/<slug>.html · redirection vers la version française ;
  - sitemap.xml (alternates + lastmod) et rss.xml.
Lancé localement ou par l'action GitHub à chaque push."""
import datetime, email.utils, json, pathlib, html as _h

root = pathlib.Path(__file__).resolve().parent.parent
BASE = 'https://blog.noirebox.eu'
SITE = 'NoireBox blog'

def parse_fm(path):
    txt = path.read_text(); fm = {}
    if txt.startswith('---'):
        block = txt[3:txt.index('---', 3)]
        for line in block.splitlines():
            if ':' in line:
                k, v = line.split(':', 1)
                fm[k.strip()] = v.strip().strip('"')
    return fm

slugs = [l.strip()[2:] for l in (root / 'INDEX.md').read_text().splitlines()
         if l.strip().startswith('- ')]
tpl = (root / 'article.html').read_text()

posts = []
for slug in slugs:
    frp = root / f'posts/{slug}.fr.md'
    if not frp.exists():
        continue
    enp = root / f'posts/{slug}.en.md'
    posts.append({'slug': slug, 'fr': parse_fm(frp),
                  'en': parse_fm(enp) if enp.exists() else None})
posts.sort(key=lambda p: p['fr'].get('date', ''), reverse=True)

def head(lang, slug, fr, en):
    has_en = en is not None
    src = fr if lang == 'fr' else (en or fr)
    title = src.get('titre') or (en.get('titre') if en else slug)
    desc = src.get('resume') or (en.get('resume') if en else '')
    image = src.get('image') or ''
    url = f'{BASE}/{lang}/{slug}'
    alt = ''
    if has_en:
        o = f'{BASE}/' + ('en' if lang == 'fr' else 'fr') + f'/{slug}'
        alt = (f'<link rel="alternate" hreflang="fr" href="{o}">\n'
               f'<link rel="alternate" hreflang="en" href="{BASE}/en/{slug}">\n'
               f'<link rel="alternate" hreflang="x-default" href="{BASE}/fr/{slug}">\n')
    jsonld = {"@context": "https://schema.org", "@type": "BlogPosting",
              "headline": title, "description": desc, "url": url,
              "mainEntityOfPage": url, "datePublished": fr.get('date', ''),
              "inLanguage": lang,
              "author": {"@type": "Person", "name": "Sam Labbe", "url": "https://slabb.dev"},
              "publisher": {"@type": "Person", "name": "Sam Labbe"}}
    if image: jsonld["image"] = [image]
    head = (f'<title>{_h.escape(title)} · {SITE}</title>\n'
            f'<meta name="description" content="{_h.escape(desc)}">\n'
            f'<link rel="canonical" href="{url}">\n{alt}'
            f'<meta property="og:type" content="article">\n'
            f'<meta property="og:site_name" content="{SITE}">\n'
            f'<meta property="og:title" content="{_h.escape(title)}">\n'
            f'<meta property="og:description" content="{_h.escape(desc)}">\n'
            f'<meta property="og:url" content="{url}">\n'
            f'<meta property="article:published_time" content="{fr.get("date", "")}">\n'
            + (f'<meta property="og:image" content="{image}">\n' if image else '') +
            f'<meta name="twitter:card" content="{"summary_large_image" if image else "summary"}">\n'
            f'<meta name="twitter:title" content="{_h.escape(title)}">\n'
            f'<meta name="twitter:description" content="{_h.escape(desc)}">\n'
            + (f'<meta name="twitter:image" content="{image}">\n' if image else '') +
            f'<script type="application/ld+json">{json.dumps(jsonld, ensure_ascii=False)}</script>\n'
            f'<script>window.POST_SLUG="{slug}";window.POST_LANG="{lang}";'
            f'window.POST_HAS_EN="{"true" if has_en else "false"}";</script>\n</head>')
    return head

count = 0
urls = []
for p in posts:
    slug = p['slug']; fr = p['fr']; en = p['en']
    has_en = en is not None
    for lang in (['fr', 'en'] if has_en else ['fr']):
        page = tpl.replace('<title>Article · NoireBox blog</title>',
                           head(lang, slug, fr, en))
        d = root / lang
        d.mkdir(exist_ok=True)
        (d / f'{slug}.html').write_text(page)
        count += 1
        urls.append((f'{BASE}/{lang}/{slug}', fr.get('date', ''), has_en, slug))
    redir = (f'<!DOCTYPE html><meta charset="utf-8">'
             f'<meta http-equiv="refresh" content="0; url={BASE}/fr/{slug}">'
             f'<script>location.replace("{BASE}/fr/{slug}")</script>')
    (root / f'posts/{slug}.html').write_text(redir)

sm = ('<?xml version="1.0" encoding="UTF-8"?>\n'
      '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
      'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n')
for url, date, has_en, slug in urls:
    alt = ''
    if has_en:
        o = url.replace(f'/{slug}', f'/en/{slug}') if '/fr/' in url else url.replace(f'/{slug}', f'/fr/{slug}')
        alt = (f'<xhtml:link rel="alternate" hreflang="fr" href="{BASE}/fr/{slug}"/>'
               f'<xhtml:link rel="alternate" hreflang="en" href="{BASE}/en/{slug}"/>')
    lastmod = f'<lastmod>{date}</lastmod>' if date else ''
    sm += f'  <url><loc>{url}</loc>{alt}{lastmod}</url>\n'
sm += '</urlset>\n'
(root / 'sitemap.xml').write_text(sm)

rss = '<?xml version="1.0" encoding="UTF-8"?>\n<rss version="2.0"><channel>\n'
rss += f'<title>{SITE} · Sam Labbe</title>\n<link>https://blog.slabb.dev</link>\n'
rss += '<description>Agents IA, sécurité &amp; preuve · EN first, FR as translations land</description>\n<language>fr</language>\n'
for p in posts:
    fm = p['fr']
    rss += (f'<item><title>{_h.escape(fm.get("titre", p["slug"]))}</title>'
            f'<link>{BASE}/fr/{p["slug"]}</link><guid>{BASE}/fr/{p["slug"]}</guid>'
            f'<description>{_h.escape(fm.get("resume", ""))}</description>')
    dt = fm.get('date', '')
    rss += (f'<pubDate>{email.utils.format_datetime(datetime.datetime.fromisoformat(dt))}</pubDate>' if dt else '')
    rss += '</item>\n'
rss += '</channel></rss>\n'
(root / 'rss.xml').write_text(rss)
print(f'gen.py : {count} pages slug ({len(posts)} articles) · sitemap {len(urls)} URLs · rss {len(posts)} items')
