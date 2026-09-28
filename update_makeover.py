import re

with open('index.html', 'r') as f:
    html = f.read()

card_old = '<div class="ba-card"><div class="ba-pair"><div class="ba-half before"><span class="lbl">Before</span><svg viewBox="0 0 24 24" fill="none"><path d="M12 3v18M8 7h8M9 11h6" stroke="#008C95" stroke-width="1.4" stroke-linecap="round"/></svg></div><div class="ba-half after"><span class="lbl">After</span><svg viewBox="0 0 24 24" fill="none"><path d="M12 3v18M8 7h8M9 11h6" stroke="#008C95" stroke-width="1.4" stroke-linecap="round"/></svg></div></div><div class="cap"><b>Missing tooth, replaced</b>Single dental implant</div></div>'

card_new = '<div class="ba-card"><div class="ba-pair"><div class="ba-half before"><span class="lbl">Before</span><img src="/assets/img/makeover-before.jpg" alt="Before makeover" style="width:100%; height:100%; object-fit:cover;"></div><div class="ba-half after"><span class="lbl">After</span><img src="/assets/img/makeover-before.jpg" alt="After makeover" style="width:100%; height:100%; object-fit:cover; opacity: 0.5;"></div></div><div class="cap"><b>Full Smile Makeover</b>Veneers &amp; Teeth Whitening</div></div>'

html = html.replace(card_old, card_new)

with open('index.html', 'w') as f:
    f.write(html)
