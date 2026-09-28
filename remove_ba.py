import re

with open('index.html', 'r') as f:
    html = f.read()

# Remove the ba-section we added
pattern = re.compile(r'<!-- ===== BEFORE & AFTER ===== -->.*?<!-- ===== STATS BAND ===== -->', re.DOTALL)
html = pattern.sub('<!-- ===== STATS BAND ===== -->', html)

with open('index.html', 'w') as f:
    f.write(html)
