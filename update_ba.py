import re

with open('index.html', 'r') as f:
    html = f.read()

ba_section = """
<!-- ===== BEFORE & AFTER ===== -->
<section class="ba-section">
  <div class="ba-wrap">
    <div class="ba-header reveal">
      <h2>Complete Smile Restoration</h2>
      <p>Dental Crowns & Tooth Restoration. See the difference modern dentistry can make.</p>
    </div>
    <div class="ba-slider reveal" id="ba-slider">
      <img class="ba-img-after" src="/assets/img/smile-after.jpg" alt="After Complete Smile Restoration">
      <img class="ba-img-before" id="ba-before" src="/assets/img/smile-before.jpg" alt="Before Complete Smile Restoration">
      <div class="ba-handle" id="ba-handle">
        <span class="ba-arrows"></span>
      </div>
      <div class="ba-label ba-label-before">BEFORE</div>
      <div class="ba-label ba-label-after">AFTER</div>
    </div>
  </div>
</section>

<!-- ===== STATS BAND ===== -->"""

html = html.replace('<!-- ===== STATS BAND ===== -->', ba_section)

with open('index.html', 'w') as f:
    f.write(html)
