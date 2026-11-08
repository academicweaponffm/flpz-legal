"""Check public routes, language counterparts and release claims without network access."""
from html.parser import HTMLParser
from pathlib import Path
import re
import unittest
from urllib.parse import urlsplit, unquote
from build_home import COPY, page

ROOT=Path(__file__).resolve().parent

class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(); self.tags=[]; self.links=[]; self.ids=set(); self.lang=None
        self.feed(text)
    def handle_starttag(self, tag, pairs):
        attrs=dict(pairs); self.tags.append(tag)
        if tag=='html': self.lang=attrs.get('lang')
        if attrs.get('id'): self.ids.add(attrs['id'])
        if tag in ('a','link') and attrs.get('href'): self.links.append(attrs['href'])

class SiteTests(unittest.TestCase):
    def test_nine_bilingual_pages_have_shared_shell_and_no_paid_offers(self):
        files=list(ROOT.rglob('*.html'))
        self.assertEqual(len(files),9)
        for file in files:
            text=file.read_text(encoding='utf-8'); parsed=Page(text)
            with self.subTest(page=str(file.relative_to(ROOT))):
                for tag in ['header','footer','h1','main']:self.assertEqual(parsed.tags.count(tag),1)
                self.assertIn(parsed.lang,['de','en'])
                self.assertIn('aria-label="FLPZ"',text)
                self.assertIn('/flpz-legal/assets/style.css',text)
                self.assertIn('mailto:flpz.support@gmail.com',text)
                self.assertNotRegex(text,r'\bPro\b|\bFree plan\b|4 / 5|fünf aktive|five active')
                self.assertNotRegex(text,r'[\u00c2\u00c3][\u0080-\u00bf]|\ufffd')
                self.assertNotIn('<script',text)
    def test_every_local_link_and_anchor_resolves(self):
        for file in ROOT.rglob('*.html'):
            for href in Page(file.read_text(encoding='utf-8')).links:
                url=urlsplit(href)
                if url.scheme or url.netloc:continue
                if url.path.startswith('/flpz-legal/'):
                    target=ROOT/unquote(url.path[len('/flpz-legal/'):])
                elif not url.path: target=file
                else: target=file.parent/unquote(url.path)
                if target.is_dir():target=target/'index.html'
                self.assertTrue(target.is_file(),f'{file}: {href}')
                if url.fragment:self.assertIn(url.fragment,Page(target.read_text(encoding='utf-8')).ids)
    def test_generated_product_pages_match_sources(self):
        for lang in ('de','en'):
            self.assertEqual((ROOT/lang/'index.html').read_text(encoding='utf-8'),page(lang,COPY[lang])+'\n')
        self.assertEqual((ROOT/'index.html').read_text(encoding='utf-8'),page('en',COPY['en'])+'\n')
    def test_legal_dates_and_device_qualifications(self):
        for lang,privacy,terms in [('de','datenschutz','nutzungsbedingungen'),('en','privacy','terms')]:
            for route in [privacy,terms]:
                text=(ROOT/lang/route/'index.html').read_text(encoding='utf-8')
                self.assertIn('8. November 2026' if lang=='de' else '8 November 2026',text)
                self.assertIn('Apple',text)
                self.assertIn('EULA',text) if route==terms else self.assertIn('StoreKit',text)
        for lang in ('de','en'):
            self.assertIn('iOS 27',(ROOT/lang/'index.html').read_text(encoding='utf-8'))

if __name__=='__main__':unittest.main()
