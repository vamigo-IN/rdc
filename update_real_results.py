import re

with open('index.html', 'r') as f:
    html = f.read()

card_old = '<div class="ba-card"><div class="ba-pair"><div class="ba-half before"><span class="lbl">Before</span><svg viewBox="0 0 24 24" fill="none"><path d="M12 3c-4 0-6.5 2-6.5 6 0 3 1 5.5 2 9 .5 2 2.5 2.5 3 0 .5-2.5.5-4.5 1.5-4.5s1 2 1.5 4.5c.5 2.5 2.5 2 3 0 1-3.5 2-6 2-9 0-4-2.5-6-6.5-6Z" stroke="#008C95" stroke-width="1.4"/></svg></div><div class="ba-half after"><span class="lbl">After</span><svg viewBox="0 0 24 24" fill="none"><path d="M12 3c-4 0-6.5 2-6.5 6 0 3 1 5.5 2 9 .5 2 2.5 2.5 3 0 .5-2.5.5-4.5 1.5-4.5s1 2 1.5 4.5c.5 2.5 2.5 2 3 0 1-3.5 2-6 2-9 0-4-2.5-6-6.5-6Z" stroke="#008C95" stroke-width="1.4"/></svg></div></div><div class="cap"><b>Full smile makeover</b>Veneers &amp; teeth whitening</div></div>'

card_new = '<div class="ba-card"><div class="ba-pair"><div class="ba-half before"><span class="lbl">Before</span><img src="/assets/img/smile-before.jpg" alt="Before restoration" style="width:100%; height:100%; object-fit:cover;"></div><div class="ba-half after"><span class="lbl">After</span><img src="/assets/img/smile-after.jpg" alt="After restoration" style="width:100%; height:100%; object-fit:cover;"></div></div><div class="cap"><b>Complete Smile Restoration</b>Dental Crowns &amp; Tooth Restoration</div></div>'

html = html.replace(card_old, card_new)

with open('index.html', 'w') as f:
    f.write(html)
