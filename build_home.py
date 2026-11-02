"""Generate the static public product pages; no app data or runtime dependencies."""
from html import escape as h
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BASE = '/flpz-legal'
COPY = {
    'de': {
        'title': 'Deine Flips. Dein Überblick.', 'lead': 'Vom ersten Einkauf bis zum tatsächlichen Gewinn. FLPZ hält Bestand, Kosten und Verkäufe zusammen – auf deinem iPhone.',
        'tag': 'Für Menschen, die weiterverkaufen.', 'features': 'Was FLPZ für dich macht', 'featuresLink': 'Funktionen',
        'intro': 'Weniger verstreute Notizen. Ein klarer Blick auf deine laufenden Flips.',
        'cards': [('01', 'Wissen, was übrig bleibt', 'Erfasse Einkauf, Zusatzkosten und Verkauf. Sieh deinen tatsächlichen Gewinn und das Geld, das noch im Bestand steckt.'), ('02', 'Den Verkauf zu Ende bringen', 'Belege, Zahlungsstatus, Versand und Erstattungen gehören zum Artikel. Offene Aufgaben und eigene Erinnerungen helfen dir beim Nachhalten.'), ('03', 'Deinen Bestand verstehen', 'Suche nach Artikeln, Lagerorten oder Artikelnummern. Vergleiche deine erfassten Verkäufe und halte EUR und USD getrennt.')],
        'proTitle': 'Pro begleitet deinen wachsenden Bestand.', 'proLead': 'Vor dem Kauf rechnen. Liegen gebliebenen Bestand erkennen. Wiederkehrende Arbeit zusammen erledigen.',
        'pro': [('Kauf-Check', 'Prüfe den geschätzten Gewinn nach Kosten und Gebühren. Sieh, welchen Einkaufspreis dein Gewinnziel erlaubt – mit deinen eigenen Preisannahmen.'), ('Bestandsradar', 'Finde ältere aktive Artikel und sieh, wie viel Kapital darin steckt. Die Altersgrenze legst du fest.'), ('Persönliche Erkenntnisse', 'Erkenne Kategorien und Plattformen mit dem höchsten Durchschnittsgewinn, kurze Haltedauern und deine größte Kostenart. Aus deinen tatsächlichen Verkäufen; Gruppenvergleiche ab drei Verkäufen.'), ('Weniger wiederholte Eingaben', 'Bearbeite mehrere Artikel gemeinsam, teile Paketkäufe centgenau auf und übernimm wiederkehrende Beträge aus Kostenvorlagen.'), ('Inserate im Blick', 'Sammle Links, Angebotspreise und Status je Marktplatz. Nach einem Verkauf erkennst du weitere Inserate, die du manuell entfernen musst.'), ('Deine Übersicht griffbereit', 'Optionale Home-Bildschirm-Widgets und ein wöchentlicher Bestandscheck. Dazu lokale KI-Inseratsentwürfe auf unterstützten Geräten sowie passende Farben und Icons.')],
        'freeTitle': 'Mit fünf aktiven Flips kostenlos starten.', 'free': 'Verkaufshistorie, Belege, Zahlungs- und Versandstatus, Erstattungen, eigene Erinnerungen, Ziele, Basisstatistiken, Backups, CSV und optionaler iCloud-Sync bleiben in Free. Pro erweitert den aktiven Bestand ohne Limit. Gespeicherte Daten bleiben nach Pro zugänglich.',
        'privacyTitle': 'Dein Bestand bleibt bei dir.', 'privacy': 'Kein zusätzliches App-Konto. Lokal arbeiten und bei Bedarf mit deinem persönlichen iCloud synchronisieren. Keine Werbung und keine Tracking-SDKs. Erinnerungen und Widgets aktivierst du selbst.',
        'limits': 'FLPZ veröffentlicht keine Inserate und greift nicht auf Marktplatzkonten zu. KI benötigt ein kompatibles Gerät und ein verfügbares Apple-Intelligence-Modell; Fotoanalyse zusätzlich iOS 27. Generierte Texte vor dem Teilen prüfen.',
        'betaTitle': 'Die nächste Beta ist in Vorbereitung.', 'beta': 'Diese Seite zeigt den vorgesehenen Funktionsumfang der kommenden Beta. Der öffentliche TestFlight-Zugang wird nach Freigabe hier ergänzt. Voraussetzung: iPhone mit iOS 26 oder neuer.',
        'contact': 'Fragen zu FLPZ?', 'contactLink': 'Support kontaktieren', 'privacyLink': 'Datenschutz', 'termsLink': 'Nutzungsbedingungen', 'supportLink': 'Hilfe', 'other': 'English', 'otherPath': '/en/', 'skip': 'Zum Inhalt', 'nav': 'Hauptnavigation', 'preview': 'Beispielwerte', 'profit': 'Gewinn diesen Monat', 'capital': 'Gebundenes Kapital', 'active': 'Aktive Flips', 'money': '+142,00 €', 'bound': '310,00 €',
    },
    'en': {
        'title': 'Your flips. In focus.', 'lead': 'From the first purchase to actual profit. FLPZ keeps inventory, costs and sales together on your iPhone.',
        'tag': 'For people who resell.', 'features': 'What FLPZ helps you do', 'featuresLink': 'Features', 'intro': 'Fewer scattered notes. A clear view of your ongoing flips.',
        'cards': [('01', 'Know what you actually earn', 'Record purchases, extra costs and sales. See actual profit separately from the money still tied up in inventory.'), ('02', 'Finish the sale', 'Keep receipts, payment, shipping and refunds with each item. Open tasks and personal reminders help you follow through.'), ('03', 'Understand your inventory', 'Search items, storage locations and SKUs. Compare recorded sales while keeping EUR and USD separate.')],
        'proTitle': 'Pro grows with your inventory.', 'proLead': 'Check the numbers before buying. Spot older stock. Handle repeated work together.',
        'pro': [('Purchase check', 'Estimate profit after costs and fees. See the highest purchase price that meets your profit target, using your own sale-price assumptions.'), ('Inventory radar', 'Find older active items and see how much capital is tied up in them. Choose your own age threshold.'), ('Personal insights', 'Find the categories and platforms with the highest average profit, short holding times and your largest cost type. Based on actual sales; group comparisons need three sales.'), ('Fewer repeated entries', 'Edit several items together, split purchased bundles with cent-exact cost allocation and reuse cost presets.'), ('Keep listings organized', 'Keep marketplace links, asking prices and status with each item. After selling, see which other listings you still need to remove manually.'), ('Your overview within reach', 'Optional Home Screen widgets and a weekly stock review. Plus local AI listing drafts on supported devices and matching app colors and icons.')],
        'freeTitle': 'Start free with five active flips.', 'free': 'Sold history, receipts, payment and shipping tracking, refunds, personal reminders, goals, basic statistics, backups, CSV and optional iCloud sync stay in Free. Pro removes the active-inventory limit. Your saved data remains accessible when Pro ends.',
        'privacyTitle': 'Your inventory stays yours.', 'privacy': 'No extra app account. Work locally and enable personal iCloud sync when you want it. No ads or tracking SDKs. Reminders and widget sharing are opt-in.',
        'limits': 'FLPZ does not publish listings or access marketplace accounts. AI needs a compatible device and an available Apple Intelligence model; photo analysis also requires iOS 27. Review generated text before sharing.',
        'betaTitle': 'The next beta is taking shape.', 'beta': 'This page describes the planned feature set of the upcoming beta. A public TestFlight invitation will be added here after approval. Requires an iPhone with iOS 26 or later.',
        'contact': 'Questions about FLPZ?', 'contactLink': 'Contact support', 'privacyLink': 'Privacy', 'termsLink': 'Terms of use', 'supportLink': 'Support', 'other': 'Deutsch', 'otherPath': '/de/', 'skip': 'Skip to content', 'nav': 'Main navigation', 'preview': 'Example values', 'profit': 'Profit this month', 'capital': 'Tied-up capital', 'active': 'Active flips', 'money': '+€142.00', 'bound': '€310.00',
    },
}


def page(lang, c):
    privacy, terms, support = ('datenschutz', 'nutzungsbedingungen', 'hilfe') if lang == 'de' else ('privacy', 'terms', 'support')
    cards = ''.join(f'<article class="feature"><span class="number">{n}</span><h3>{h(title)}</h3><p>{h(body)}</p></article>' for n, title, body in c['cards'])
    pro = ''.join(f'<article class="pro-feature"><h3>{h(title)}</h3><p>{h(body)}</p></article>' for title, body in c['pro'])
    return f'''<!doctype html>
<html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="description" content="{h(c['lead'])}"><meta name="referrer" content="no-referrer"><title>FLPZ · {h(c['title'])}</title><link rel="stylesheet" href="{BASE}/assets/style.css"><link rel="stylesheet" href="{BASE}/assets/product.css"><link rel="alternate" hreflang="de" href="https://academicweaponffm.github.io{BASE}/de/"><link rel="alternate" hreflang="en" href="https://academicweaponffm.github.io{BASE}/en/"></head>
<body class="product"><a class="skip" href="#content">{c['skip']}</a>
<header><a class="brand" href="{BASE}/{lang}/">FLPZ<span class="brand-dot">.</span></a><nav aria-label="{c['nav']}"><a href="#features">{c['featuresLink']}</a><a href="#pro">Pro</a><a href="{BASE}/{lang}/{support}/">{c['supportLink']}</a><a href="{BASE}{c['otherPath']}" lang="{'en' if lang == 'de' else 'de'}">{c['other']}</a></nav></header>
<main id="content"><section class="hero"><div><p class="eyebrow">{c['tag']}</p><h1>{c['title']}</h1><p class="lead">{c['lead']}</p><a class="button" href="#features">{c['featuresLink']} <span aria-hidden="true">↗</span></a><p class="meta">iPhone · Deutsch / English</p></div>
<aside class="overview" aria-label="{c['preview']}"><div class="overview-top"><strong>FLPZ</strong><span class="pill">{c['preview']}</span></div><p>{c['profit']}</p><p class="profit">{c['money']}</p><div class="overview-row"><span>{c['capital']}</span><strong>{c['bound']}</strong></div><div class="overview-row"><span>{c['active']}</span><strong>4 / 5</strong></div><div class="bars" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i><i></i></div></aside></section>
<section id="features"><p class="eyebrow">FLPZ</p><h2>{c['features']}</h2><p class="section-lead">{c['intro']}</p><div class="features">{cards}</div></section>
<section id="pro" class="pro-section"><p class="eyebrow">FLPZ Pro</p><h2>{c['proTitle']}</h2><p class="section-lead">{c['proLead']}</p><div class="pro-grid">{pro}</div></section>
<section class="free-section"><h2>{c['freeTitle']}</h2><p>{c['free']}</p></section>
<section class="privacy-section"><h2>{c['privacyTitle']}</h2><p>{c['privacy']}</p><a href="{BASE}/{lang}/{privacy}/">{c['privacyLink']} ↗</a><p class="meta">{c['limits']}</p></section>
<section class="beta-section" id="beta"><p class="eyebrow">TestFlight</p><h2>{c['betaTitle']}</h2><p>{c['beta']}</p><p><strong>{c['contact']}</strong> <a href="mailto:flpz.support@gmail.com">{c['contactLink']}</a></p></section></main>
<footer><strong>FLPZ</strong><nav aria-label="{'Rechtliches' if lang == 'de' else 'Legal'}"><a href="{BASE}/{lang}/{privacy}/">{c['privacyLink']}</a><a href="{BASE}/{lang}/{terms}/">{c['termsLink']}</a><a href="{BASE}/{lang}/{support}/">{c['supportLink']}</a></nav><p>© 2026 Kiro Laban · <a href="mailto:flpz.support@gmail.com">flpz.support@gmail.com</a></p></footer></body></html>'''


if __name__ == '__main__':
    for language, copy in COPY.items():
        destination = ROOT/language/'index.html'
        destination.parent.mkdir(exist_ok=True)
        destination.write_text(page(language, copy)+'\n', encoding='utf-8')
    (ROOT/'index.html').write_text(page('en', COPY['en'])+'\n', encoding='utf-8')
