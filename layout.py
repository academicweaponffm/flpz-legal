"""Shared public navigation and footer. Existing routes remain stable."""
import re

BASE = '/flpz-legal'
ROUTES = {'de': {'home': '', 'support': 'hilfe/', 'privacy': 'datenschutz/', 'terms': 'nutzungsbedingungen/'},
          'en': {'home': '', 'support': 'support/', 'privacy': 'privacy/', 'terms': 'terms/'}}

def apply_shell(html, lang, kind, route):
    other = 'en' if lang == 'de' else 'de'
    words = ('Funktionen', 'Hilfe', 'Datenschutz', 'Nutzungsbedingungen', 'Hauptnavigation', 'Rechtliches', 'English') if lang == 'de' else ('Features', 'Support', 'Privacy', 'Terms of use', 'Main navigation', 'Legal', 'Deutsch')
    def url(key, language=lang): return f"{BASE}/{language}/{ROUTES[language][key]}"
    header = f'<header><a class="brand" href="{url("home")}" aria-label="FLPZ">FLPZ<span class="brand-dot">.</span></a><nav aria-label="{words[4]}"><a href="{url("home")}#features">{words[0]}</a><a href="{url("support")}">{words[1]}</a><a href="{url(route, other)}" lang="{other}" hreflang="{other}">{words[6]}</a></nav></header>'
    footer = f'<footer><a class="brand" href="{url("home")}">FLPZ<span class="brand-dot">.</span></a><nav aria-label="{words[5]}"><a href="{url("privacy")}">{words[2]}</a><a href="{url("terms")}">{words[3]}</a><a href="{url("support")}">{words[1]}</a></nav><p>© 2026 Kiro Laban · <a href="mailto:flpz.support@gmail.com">flpz.support@gmail.com</a></p></footer>'
    html = re.sub(r'<header>.*?</header>', lambda _: header, html, flags=re.S)
    html = re.sub(r'<footer>.*?</footer>', lambda _: footer, html, flags=re.S)
    html = re.sub(r'<body(?: class="[^"]*")?>', f'<body class="{kind}">', html, count=1)
    return html
