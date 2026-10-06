import re

with open('general-dentistry/index.html', 'r') as f:
    html = f.read()

# Fix Hero H1
html = html.replace('General Dentistry in<br><span class="accent">Althan, Surat<svg', 'General Dentistry<br><span class="accent">That Puts You First<svg')

# Fix Hero Sub
html = html.replace('Check-ups, cleaning, fillings and sensitivity care, done gently, priced up front, most finished in a single visit.', 'Comfortable, transparent and modern dental care in Althan & Vesu, Surat.')

# Fix Sub-heading
html = html.replace('General dentistry at a multi-specialty clinic', 'General dentistry in Althan, Surat')

# Replace blurry clinic image
html = html.replace('src="/assets/img/clinic-1.jpg"', 'src="/assets/img/clinic-2.jpg"')

with open('general-dentistry/index.html', 'w') as f:
    f.write(html)

print("Updated general-dentistry/index.html")
