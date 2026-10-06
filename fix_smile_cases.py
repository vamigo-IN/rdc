import re

with open('smile-design/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

cases = ""
for i in range(1, 7):
    cases += f'<figure class="case-card"><img src="/assets/img/cases/smile-{i}.jpg" alt="Smile design before and after {i}" loading="lazy"><figcaption class="case-cap">Smile design transformation {i}.</figcaption></figure>'
for i in range(1, 4):
    cases += f'<figure class="case-card"><img src="/assets/img/cases/aligners-{i}.jpg" alt="Clear aligners before and after {i}" loading="lazy"><figcaption class="case-cap">Clear aligners transformation {i}.</figcaption></figure>'

cases += f'<figure class="case-card"><img src="/assets/img/cases/whitening-1.jpg" alt="Teeth whitening before and after" loading="lazy"><figcaption class="case-cap">Teeth whitening transformation.</figcaption></figure>'

html = re.sub(r'<div class="case-grid reveal">.*?</div>', f'<div class="case-grid reveal">{cases}</div>', html, flags=re.DOTALL)

with open('smile-design/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
