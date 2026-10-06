import re

with open('kids-dentistry/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

cases = ""
for i in range(1, 6):
    cases += f'<figure class="case-card"><img src="/assets/img/cases/kids-{i}.jpg" alt="Child dental treatment before and after {i}" loading="lazy"><figcaption class="case-cap">Child dental treatment before and after {i}.</figcaption></figure>'

html = re.sub(r'<div class="case-grid reveal">.*?</div>', f'<div class="case-grid reveal">{cases}</div>', html, flags=re.DOTALL)

with open('kids-dentistry/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
