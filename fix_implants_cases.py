import re

with open('dental-implants/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

cases = ""
for i in range(1, 6):
    cases += f'<figure class="case-card"><img src="/assets/img/cases/implants-{i}.jpg" alt="Dental implants treatment {i}" loading="lazy"><figcaption class="case-cap">Dental implants treatment {i}.</figcaption></figure>'

html = re.sub(r'<div class="case-grid reveal">.*?</div>', f'<div class="case-grid reveal">{cases}</div>', html, flags=re.DOTALL)

with open('dental-implants/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
