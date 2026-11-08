"""Regenerate product pages and the shared shell on all public routes."""
from pathlib import Path
import runpy
from layout import apply_shell, ROUTES
ROOT = Path(__file__).resolve().parent
runpy.run_path(str(ROOT/'build_home.py'), run_name='__main__')
for lang, routes in ROUTES.items():
    for route, suffix in routes.items():
        if route == 'home': continue
        path = ROOT/lang/suffix/'index.html'
        path.write_text(apply_shell(path.read_text(encoding='utf-8'), lang, 'document', route), encoding='utf-8')
print('Built nine public pages with shared navigation and footer.')
