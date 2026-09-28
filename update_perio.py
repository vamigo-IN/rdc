import re

with open('index.html', 'r') as f:
    html = f.read()

card_old = '<div class="ba-card"><div class="ba-pair"><div class="ba-half before"><span class="lbl">Before</span><svg viewBox="0 0 24 24" fill="none"><path d="M5 8h14M5 12h14M5 16h14" stroke="#008C95" stroke-width="1.4" stroke-linecap="round"/></svg></div><div class="ba-half after"><span class="lbl">After</span><svg viewBox="0 0 24 24" fill="none"><path d="M5 8h14M5 12h14M5 16h14" stroke="#008C95" stroke-width="1.4" stroke-linecap="round"/></svg></div></div><div class="cap"><b>Straighter in months</b>Clear aligners</div></div>'

card_new = '<div class="ba-card"><div class="ba-pair"><div class="ba-half before"><span class="lbl">Before</span><img src="/assets/img/perio-before.jpg" alt="Before treatment" style="width:100%; height:100%; object-fit:cover;"></div><div class="ba-half after"><span class="lbl">After</span><img src="/assets/img/perio-after.jpg" alt="After treatment" style="width:100%; height:100%; object-fit:cover;"></div></div><div class="cap"><b>Advanced Periodontics</b>Gum Surgery &amp; Rehabilitation</div></div>'

html = html.replace(card_old, card_new)

with open('index.html', 'w') as f:
    f.write(html)
