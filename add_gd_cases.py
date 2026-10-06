import re

with open('general-dentistry/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

cases_section = """
<section class="block cases-band" id="results">
  <div class="wrap">
    <div class="sec-top reveal">
      <div><span class="eyebrow">Real results</span><h2>Before and after, our own patients</h2></div>
      <p>A few recent cases from the clinic.</p>
    </div>
    <div class="case-grid reveal">
      <figure class="case-card"><img src="/assets/img/cases/cleaning-1.jpg" alt="Teeth cleaning before and after" loading="lazy"><figcaption class="case-cap">Professional teeth cleaning and scaling.</figcaption></figure>
    </div>
    <p class="case-note reveal">Real patients treated at Roots Dental Care. Shared with consent.</p>
  </div>
</section>
"""

html = html.replace('<section class="block clinic-band">', cases_section + '\n<section class="block clinic-band">')

with open('general-dentistry/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
