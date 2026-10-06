import os
import re

for root, dirs, files in os.walk('.'):
    for name in files:
        if name.endswith('.html'):
            filepath = os.path.join(root, name)
            with open(filepath, 'r', encoding='utf-8') as f:
                html = f.read()

            # Fix alt text: "before and after 1" -> "before and after"
            html = re.sub(r' before and after \d', ' before and after', html)
            html = re.sub(r' transformation \d\.', ' transformation.', html)
            html = re.sub(r' treatment \d\.', ' treatment.', html)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(html)

print("Removed numbers from captions.")
