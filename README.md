# FLPZ public website

Static English/German product pages, support, privacy and terms for FLPZ.

- Product: https://academicweaponffm.github.io/flpz-legal/
- Deutsch: https://academicweaponffm.github.io/flpz-legal/de/
- English: https://academicweaponffm.github.io/flpz-legal/en/

The homepage explains the feature set being tested before launch, all included features and local
privacy choices. A download link is added only after confirmed app availability.

Edit product copy in `build_home.py` and run `python build_site.py` to regenerate
all nine pages with shared navigation and footer. Existing legal/support paths remain stable.
GitHub Pages serves the static files; no server, external fonts, analytics or JS.

This public repository contains no app source, credentials, internal release
status, private identifiers or user records. Illustrative metrics are labeled.

Copy follows [COPY_STYLE.md](COPY_STYLE.md), using the Humanizer editing skill.

Run `python -m unittest test_site -v` to check routes, generation, bilingual copy
and free access claims.
