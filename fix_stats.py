import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the stats block
new_stats = """  <div class="wrap stats-grid">
    <div class="stat"><b><span class="counter" data-target="2000">0</span>+</b><span>Families Treated</span></div>
    <div class="stat"><b><span class="counter" data-target="10000">0</span>+</b><span>Treatments Completed</span></div>
    <div class="stat"><b><span class="counter" data-target="5000">0</span>+</b><span>Implants</span></div>
    <div class="stat"><b><span class="counter" data-target="4">0</span></b><span>Expert Specialists</span></div>
  </div>"""

html = re.sub(r'<div class="wrap stats-grid">.*?</div>\n  </div>', new_stats, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
