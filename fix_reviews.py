# -*- coding: utf-8 -*-
import re

with open('general-dentistry/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

revs = """<div class="rev"><div class="stars" aria-label="5 out of 5">★★★★★</div><p>Went in for a cleaning and a nervous first visit. Quick, gentle, and they showed me the cost before starting.</p><div class="who"><b>Priya M.</b> · Vesu</div></div><div class="rev"><div class="stars" aria-label="5 out of 5">★★★★★</div><p>Honest advice. They told me a filling could wait rather than pushing treatment.</p><div class="who"><b>Rahul P.</b> · Adajan</div></div><div class="rev"><div class="stars" aria-label="5 out of 5">★★★★★</div><p>The best dental experience I've had. Clean clinic, very professional staff, and they explained every step.</p><div class="who"><b>Aarav S.</b> · Piplod</div></div><div class="rev"><div class="stars" aria-label="5 out of 5">★★★★★</div><p>I usually dread visiting the dentist, but the team made my scaling completely painless.</p><div class="who"><b>Neha K.</b> · Althan</div></div><div class="rev"><div class="stars" aria-label="5 out of 5">★★★★★</div><p>Transparent pricing and no hidden costs. They took the time to answer all my questions.</p><div class="who"><b>Vikram R.</b> · Vesu</div></div><div class="rev"><div class="stars" aria-label="5 out of 5">★★★★★</div><p>Very gentle and patient, especially since I have very sensitive teeth. Highly recommend them!</p><div class="who"><b>Rohan J.</b> · Majura Gate</div></div>"""

# Be very careful with regex
html = re.sub(r'<div class="rev-grid reveal">.*?</div>\n  </div>', f'<div class="rev-grid reveal">{revs}</div>\n  </div>', html, flags=re.DOTALL)

with open('general-dentistry/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated general dentistry reviews")
