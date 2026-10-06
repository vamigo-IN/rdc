import os
import re

for root, dirs, files in os.walk('.'):
    for name in files:
        if name.endswith('.html'):
            filepath = os.path.join(root, name)
            with open(filepath, 'r', encoding='utf-8') as f:
                html = f.read()

            html = html.replace('<b>2,000+</b><span>Patients treated</span>', '<b><span class="counter" data-target="2000">0</span>+</b><span>Patients treated</span>')
            html = html.replace('<b>2,000+</b><br><span class="label">Patients treated</span>', '<b><span class="counter" data-target="2000">0</span>+</b><br><span class="label">Patients treated</span>')
            
            html = html.replace('<b>5000+</b><span>Implants placed</span>', '<b><span class="counter" data-target="5000">0</span>+</b><span>Implants placed</span>')
            
            html = html.replace('<b>15+</b><span>Years experience</span>', '<b><span class="counter" data-target="15">0</span>+</b><span>Years experience</span>')
            html = html.replace('<b>10,000+</b><span>Treatments done</span>', '<b><span class="counter" data-target="10000">0</span>+</b><span>Treatments done</span>')

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(html)

print("Updated all html files to use animated counters where possible.")
