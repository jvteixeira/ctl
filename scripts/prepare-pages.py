"""Prepare the reviewed prototype for GitHub Pages, retaining noindex."""
from pathlib import Path
import hashlib
import base64
import re
import shutil

root = Path(__file__).resolve().parent.parent
source = root / 'dist'
out = root / 'docs'
out.mkdir(exist_ok=True)
old_url = 'https://clube-tenis-loule-prototipo.zippy-shore-7205.chatgpt.site'
site_url = 'https://jvteixeira.github.io/ctl'
for path in source.rglob('*'):
    if not path.is_file() or path.name in ('_headers', '.DS_Store'):
        continue
    target = out / path.relative_to(source)
    target.parent.mkdir(parents=True, exist_ok=True)
    if path.suffix in ('.html', '.xml', '.txt'):
        text = path.read_text().replace(old_url, site_url)
        if path.suffix == '.html':
            text = text.replace('href="/"', 'href="./"')
            text = re.sub(r'(href|src)="/(?!/)', r'\1="./', text)
            text = text.replace('A plataforma que aloja este protótipo privado pode tratar dados técnicos e usar mecanismos próprios de autenticação.', 'Este protótipo é público e está alojado no GitHub Pages. O alojamento pode tratar dados técnicos de acesso.')
            text = text.replace('A plataforma pode tratar IP, registos técnicos e autenticação. O seu inventário e retenção precisam de validação separada.', 'O GitHub Pages pode tratar IP e registos técnicos. O site não exige autenticação. Consultar a política de privacidade do GitHub; a retenção e os termos aplicáveis precisam de validação separada.')
            if path.name == 'privacidade.html':
                text = text.replace('<h2>3. Email', '<p>Alojamento: <a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement" target="_blank" rel="noopener noreferrer">Política de privacidade do GitHub</a>.</p><h2>3. Email')
            scripts = re.findall(r'<script type="application/ld\+json">(.*?)</script>', text, re.S)
            hashes = ' '.join("'sha256-" + base64.b64encode(hashlib.sha256(s.encode()).digest()).decode() + "'" for s in scripts)
            policy = f"default-src 'self'; script-src 'self' {hashes}; style-src 'self'; img-src 'self'; font-src 'self'; connect-src 'none'; frame-src 'none'; object-src 'none'; base-uri 'self'; form-action 'none'"
            text = text.replace('<head>', '<head><meta http-equiv="Content-Security-Policy" content="' + policy + '"><meta name="referrer" content="strict-origin-when-cross-origin">', 1)
        target.write_text(text)
    else:
        shutil.copy2(path, target)
(out / '.nojekyll').touch()
print(f'GitHub Pages prepared in {out} for {site_url}/')
