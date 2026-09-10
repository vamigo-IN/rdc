#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate the 5 Google-Ads service landing pages for Roots Dental Care.
Each page reuses /assets/css/styles.css + /assets/js/main.js, has its own
message-matched hero + booking form, service-specific proof, a specialist
highlight, an objection-handling FAQ, and per-page schema (LocalBusiness +
Service + FAQPage + BreadcrumbList). Re-run any time content changes."""

import os

SITE = "https://rootsdentalcaresurat.com"
PHONE_TEL = "+917990376179"
PHONE_DISPLAY = "79903 76179"
OFFER = "This month: free consultation + digital X-ray"

ROOT = os.path.dirname(os.path.abspath(__file__))

TREATMENTS = [
    "Choose a treatment", "Toothache or emergency", "Check-up & cleaning",
    "Root canal", "Dental implant / missing tooth", "Braces / clear aligners",
    "Smile design / whitening", "My child's teeth", "Not sure, need advice",
]

def esc(s):
    return s.replace("&", "&amp;")

def sel(preselect, idp):
    opts = ""
    for t in TREATMENTS:
        s = " selected" if t == preselect else ""
        opts += f"<option{s}>{esc(t)}</option>"
    return opts

SWOOSH = ('<svg class="swoosh" viewBox="0 0 300 18" preserveAspectRatio="none" aria-hidden="true">'
          '<path d="M3 13C60 5 150 3 297 8" fill="none" stroke="currentColor" stroke-width="5" stroke-linecap="round"/></svg>')

WA_ARROW = ('<svg width="16" height="16" viewBox="0 0 24 24" fill="none"><path d="M5 12h14M13 6l6 6-6 6" '
            'stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>')

# --- shared chrome ---------------------------------------------------------

def header():
    return f'''<header>
  <div class="wrap nav">
    <a class="brand" href="/" aria-label="Roots Dental Care home">
      <img class="brand-logo" src="/assets/img/logo.png" alt="Roots Dental Care" width="46" height="46">
      <span class="name">Roots Dental Care<small>WHERE WE CARE</small></span>
    </a>
    <nav class="nav-links" id="nav-links">
      <a href="/">Home</a>
      <div class="nav-dd">
        <a href="/#services" class="nav-dd-t">Services</a>
        <div class="nav-dd-menu">
          <a href="/general-dentistry/">General Dentistry</a>
          <a href="/root-canal/">Root Canal</a>
          <a href="/dental-implants/">Dental Implants</a>
          <a href="/smile-design/">Smile Design &amp; Cosmetic</a>
          <a href="/kids-dentistry/">Kids' Dentistry</a>
        </div>
      </div>
      <a href="/#doctors">Doctors</a>
      <a href="#faq">FAQ</a>
      <a href="#location">Location</a>
      <a href="tel:{PHONE_TEL}" class="menu-only">Call {PHONE_DISPLAY}</a>
      <a href="#book-inline" class="menu-only book" data-open-book>Book appointment</a>
    </nav>
    <div class="nav-cta">
      <a class="nav-phone" href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>
      <a href="#book-inline" class="btn btn-red" data-open-book>Book Now</a>
      <button class="menu-btn" id="menu-btn" aria-label="Open menu">
        <svg viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg>
      </button>
    </div>
  </div>
</header>
<span id="top"></span>'''

def hero(d):
    return f'''<section class="hero-page">
  <div class="wrap hero-content">
    <div class="hero-left">
      <span class="offer-tag"><span class="dotpulse"></span>{OFFER}</span>
      <h1>{d["h1_main"]}<br><span class="accent">{d["h1_accent"]}{SWOOSH}</span></h1>
      <p class="hero-sub">{d["hero_sub"]}</p>
      <div class="hero-cta">
        <a href="tel:{PHONE_TEL}" class="btn btn-glass">Call {PHONE_DISPLAY}</a>
        <a href="#book-inline" class="btn btn-red" data-open-book>Book appointment</a>
      </div>
    </div>
    <div class="hero-form" id="book-hero">
      <span class="badge-offer"><span class="dotpulse"></span>Free consultation this month</span>
      <h3>Book your {d["short"]} visit</h3>
      <p class="sub">Tell us what's bothering you, we reply on WhatsApp in minutes.</p>
      <form class="booking-form" novalidate>
        <div class="field two">
          <div><label for="fh-name">Your name</label><input id="fh-name" name="name" type="text" placeholder="Full name" autocomplete="name"></div>
          <div><label for="fh-phone">Phone / WhatsApp</label><input id="fh-phone" name="phone" type="tel" placeholder="10-digit number" autocomplete="tel"></div>
        </div>
        <div class="field"><label for="fh-treatment">What do you need?</label>
          <select id="fh-treatment" name="treatment">{sel(d["treatment"], "fh")}</select>
        </div>
        <button type="submit" class="btn btn-red">Book appointment {WA_ARROW}</button>
      </form>
      <div class="form-ok">Thank you. We have your details and will call or message you shortly. Prefer to talk now? Call <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY.replace(" ","&nbsp;")}</a>.</div>
      <p class="form-note">No pressure, no upselling. We only suggest what your teeth actually need.</p>
    </div>
  </div>
</section>'''

def statsband(d):
    cells = "".join(f'<div class="stat"><b>{b}</b><span>{s}</span></div>' for b, s in d["stats"])
    return f'<section class="stats"><div class="wrap stats-grid">{cells}</div></section>'

def included(d):
    items = ""
    for t, txt in d["included"]:
        items += f'<div class="ci"><span class="plus">+</span><div><b>{esc(t)}.</b> <span>{esc(txt)}</span></div></div>'
    return f'''<section class="block" id="treatment">
  <div class="wrap">
    <div class="sec-top reveal">
      <div><span class="eyebrow">{esc(d["eyebrow"])}</span><h2>{esc(d["incl_head"])}</h2></div>
      <p>{esc(d["incl_intro"])}</p>
    </div>
    <div class="incl-grid reveal">{items}</div>
  </div>
</section>'''

def why(d):
    cards = ""
    for i, (t, txt) in enumerate(d["why"], 1):
        cards += f'<div class="usp"><span class="n">{i:02d}</span><h3>{esc(t)}</h3><p>{esc(txt)}</p></div>'
    return f'''<section class="block why" id="why">
  <div class="wrap">
    <div class="sec-top reveal">
      <div><span class="eyebrow">Why Roots</span><h2>{esc(d["why_head"])}</h2></div>
      <p>{esc(d["why_intro"])}</p>
    </div>
    <div class="usp-grid usp-grid-4 reveal">{cards}</div>
  </div>
</section>'''

def specialist(d):
    s = d["specialist"]
    portrait = " clinic-photo-portrait" if "/doctors/" in s["img"] else ""
    return f'''<section class="block clinic-band">
  <div class="wrap clinic-grid">
    <div class="clinic-photo{portrait} reveal"><img src="{s["img"]}" alt="{esc(s["alt"])}" loading="lazy"></div>
    <div class="clinic-copy reveal">
      <span class="eyebrow">{esc(s["eyebrow"])}</span>
      <h2>{esc(s["name"])}</h2>
      <p class="spec-role">{esc(s["role"])}</p>
      <p>{esc(s["bio"])}</p>
      <div class="quick"><a href="#book-inline" class="btn btn-teal" data-open-book>{esc(s["cta"])}</a>
      <a href="tel:{PHONE_TEL}" class="btn btn-ghost">Call {PHONE_DISPLAY}</a></div>
    </div>
  </div>
</section>'''

def faqsection(d):
    rows = ""
    for q, a in d["faqs"]:
        rows += f'<details class="faq-item"><summary>{esc(q)}</summary><div class="a">{esc(a)}</div></details>'
    return f'''<section class="block faq" id="faq">
  <div class="wrap">
    <div class="sec-top sec-top-center reveal">
      <div><span class="eyebrow">Questions</span><h2>{esc(d["faq_head"])}</h2></div>
      <p>The things patients ask us most, before they book.</p>
    </div>
    <div class="faq-list reveal">{rows}</div>
  </div>
</section>'''

CROSS = [
    ("general-dentistry", "General Dentistry"),
    ("root-canal", "Root Canal"),
    ("dental-implants", "Dental Implants"),
    ("smile-design", "Smile Design"),
    ("kids-dentistry", "Kids' Dentistry"),
]

def crosslinks(slug):
    links = ""
    for s, label in CROSS:
        if s == slug:
            continue
        links += f'<a class="btn btn-ghost" href="/{s}/">{esc(label)}</a>'
    return f'''<section class="block crosslinks">
  <div class="wrap">
    <div class="sec-top sec-top-center reveal">
      <div><span class="eyebrow">More treatments</span><h2>Everything else your family may need</h2></div>
    </div>
    <div class="cross-row reveal">{links}<a class="btn btn-teal" href="/#services">See all treatments</a></div>
  </div>
</section>'''

def location():
    return f'''<section class="block" id="location">
  <div class="wrap">
    <div class="sec-top reveal">
      <div><span class="eyebrow">Find us</span><h2>In Althan, open six days a week</h2></div>
      <p>4th floor, Atlanta Shopping Center, with evening hours, so you don't have to take a day off work.</p>
    </div>
    <div class="loc-grid">
      <div class="map-embed reveal">
        <iframe title="Roots Dental Care location map" loading="lazy" referrerpolicy="no-referrer-when-downgrade"
          src="https://www.google.com/maps?q=Roots%20Dental%20Care%20Atlanta%20Shopping%20Center%20Althan%20Surat%20395017&output=embed"></iframe>
      </div>
      <div class="reveal">
        <p class="addr"><span class="lbl">Address</span>T312, Roots Dental Care<br>4th Floor, Atlanta Shopping Center<br>Althan, Surat 395017</p>
        <table class="hours">
          <tr><td>Monday to Saturday</td><td>10 am to 8 pm</td></tr>
          <tr><td>Sunday</td><td>10 am to 1:30 pm</td></tr>
        </table>
        <div class="contact-btns">
          <a href="tel:{PHONE_TEL}" class="btn btn-teal">Call {PHONE_DISPLAY}</a>
          <a href="https://maps.app.goo.gl/DxogEZhVLLLkT5VC6" target="_blank" rel="noopener" class="btn btn-ghost">Get directions</a>
        </div>
      </div>
    </div>
  </div>
</section>'''

def bookinline(d):
    return f'''<section class="block book-section" id="book-inline">
  <div class="wrap book-wrap">
    <div class="book-copy reveal">
      <span class="eyebrow">Ready when you are</span>
      <h2>{esc(d["book_head"])}</h2>
      <p>Send your details and we'll confirm your slot on WhatsApp in minutes. Free consultation, digital X-ray and an honest opinion, whether or not you go ahead.</p>
      <div class="quick">
        <a href="tel:{PHONE_TEL}" class="btn btn-teal">Call {PHONE_DISPLAY}</a>
        <a class="btn btn-ghost" data-wa href="#" target="_blank" rel="noopener">WhatsApp us</a>
      </div>
    </div>
    <div class="book-form-card reveal">
      <h3>Book your visit</h3>
      <p class="sub">We reply on WhatsApp within minutes during clinic hours.</p>
      <form class="booking-form" novalidate>
        <div class="field two">
          <div><label for="fi-name">Your name</label><input id="fi-name" name="name" type="text" placeholder="Full name" autocomplete="name"></div>
          <div><label for="fi-phone">Phone / WhatsApp</label><input id="fi-phone" name="phone" type="tel" placeholder="10-digit number" autocomplete="tel"></div>
        </div>
        <div class="field"><label for="fi-treatment">What do you need?</label>
          <select id="fi-treatment" name="treatment">{sel(d["treatment"], "fi")}</select>
        </div>
        <div class="field"><label for="fi-time">Preferred time</label>
          <select id="fi-time" name="time"><option>Any time works</option><option>Morning (10am to 1pm)</option><option>Afternoon (1pm to 5pm)</option><option>Evening (5pm to 8pm)</option></select>
        </div>
        <button type="submit" class="btn btn-red">Book appointment {WA_ARROW}</button>
      </form>
      <div class="form-ok">Thank you. We have your details and will call or message you shortly. Prefer to talk now? Call <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY.replace(" ","&nbsp;")}</a>.</div>
      <p class="form-note">No pressure, no upselling. We only suggest what your teeth actually need.</p>
    </div>
  </div>
</section>'''

def footer():
    return f'''<footer class="f">
  <div class="wrap f-grid">
    <div class="f-brand">
      <img class="brand-logo f-logo" src="/assets/img/logo.png" alt="Roots Dental Care" width="60" height="60">
      <div class="name">Roots Dental Care</div>
      <p>Where we care. Multi-specialty dental care for the whole family, in Althan, Surat.</p>
    </div>
    <div>
      <h4>Treatments</h4>
      <a href="/dental-implants/">Implants</a><a href="/root-canal/">Root canals</a><a href="/general-dentistry/">General dentistry</a><a href="/smile-design/">Smile design</a><a href="/kids-dentistry/">Kids' dentistry</a>
    </div>
    <div>
      <h4>Clinic</h4>
      <a href="/#doctors">Our doctors</a><a href="/#why">Why Roots</a><a href="#location">Location &amp; hours</a><a href="#book-inline" data-open-book>Book a visit</a><a href="/privacy.html">Privacy Policy</a>
    </div>
    <div>
      <h4>Contact</h4>
      <p>T312, 4th Floor,<br>Atlanta Shopping Center,<br>Althan, Surat 395017</p>
      <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a><a href="tel:+917984575670">79845 75670</a>
    </div>
  </div>
  <div class="wrap f-bot">
    <span>© <span id="year">2026</span> Roots Dental Care. All rights reserved.</span>
    <span class="powered">Powered by <a href="https://growclinic.io" target="_blank" rel="noopener">GrowClinic.io</a></span>
  </div>
</footer>'''

FAB_SHEET = f'''<aside class="side-actions" aria-label="Quick contact">
  <a class="fab fab-maps" href="https://maps.app.goo.gl/DxogEZhVLLLkT5VC6" target="_blank" rel="noopener" aria-label="Get directions on Google Maps">
    <svg viewBox="0 0 24 24" fill="none"><path d="M12 21s7-6.2 7-11a7 7 0 1 0-14 0c0 4.8 7 11 7 11Z" stroke="#fff" stroke-width="1.8"/><circle cx="12" cy="10" r="2.5" fill="#fff"/></svg>
  </a>
  <a class="fab fab-wa" data-wa href="#" target="_blank" rel="noopener" aria-label="Chat on WhatsApp">
    <svg viewBox="0 0 24 24" fill="#fff"><path d="M12 2a10 10 0 0 0-8.5 15.2L2 22l4.9-1.4A10 10 0 1 0 12 2Zm0 18a8 8 0 0 1-4.1-1.1l-.3-.2-2.9.8.8-2.8-.2-.3A8 8 0 1 1 12 20Zm4.4-6c-.2-.1-1.4-.7-1.6-.8-.2-.1-.4-.1-.5.1l-.7.9c-.1.2-.3.2-.5.1a6.5 6.5 0 0 1-3.2-2.8c-.1-.2 0-.4.1-.5l.4-.5c.1-.2.1-.3 0-.5l-.7-1.7c-.2-.4-.4-.4-.5-.4h-.5c-.2 0-.5.1-.7.3-.7.7-.9 1.6-.6 2.6.4 1.4 1.3 2.7 2.6 3.7 1.6 1.3 3 1.6 3.7 1.5.5-.1 1.3-.6 1.5-1.1.2-.5.2-.9.1-1-.1-.1-.2-.1-.4-.2Z"/></svg>
  </a>
  <a class="fab fab-call" href="tel:{PHONE_TEL}" aria-label="Call the clinic">
    <svg viewBox="0 0 24 24" fill="none"><path d="M6.5 3h3l1.5 4-2 1.5a11 11 0 0 0 4.5 4.5l1.5-2 4 1.5v3a2 2 0 0 1-2.2 2A16 16 0 0 1 4.5 5.2 2 2 0 0 1 6.5 3Z" fill="#fff"/></svg>
  </a>
</aside>'''

def sheet(d):
    return f'''<div class="sheet-backdrop" id="sheet-backdrop" hidden></div>
<div class="sheet" id="booking" role="dialog" aria-modal="true" aria-labelledby="sheet-title" hidden>
  <div class="sheet-panel">
    <button class="sheet-close" id="sheet-close" aria-label="Close">&times;</button>
    <div class="sheet-grip"></div>
    <span class="offer-tag sheet-offer"><span class="dotpulse"></span>Free consultation + digital X-ray this month</span>
    <h3 id="sheet-title">Book your visit</h3>
    <p class="sub">Tell us what's bothering you, we'll reply on WhatsApp within minutes.</p>
    <form id="booking-form" class="booking-form" novalidate>
      <div class="field two">
        <div><label for="f-name">Your name</label><input id="f-name" name="name" type="text" placeholder="Full name" autocomplete="name"></div>
        <div><label for="f-phone">Phone / WhatsApp</label><input id="f-phone" name="phone" type="tel" placeholder="10-digit number" autocomplete="tel"></div>
      </div>
      <div class="field"><label for="f-treatment">What do you need?</label>
        <select id="f-treatment" name="treatment">{sel(d["treatment"], "f")}</select>
      </div>
      <div class="field"><label for="f-time">Preferred time</label>
        <select id="f-time" name="time"><option>Any time works</option><option>Morning (10am-1pm)</option><option>Afternoon (1pm-5pm)</option><option>Evening (5pm-8pm)</option></select>
      </div>
      <button type="submit" class="btn btn-red">Book appointment {WA_ARROW}</button>
    </form>
    <div class="form-ok" id="form-ok">Thank you. We have your details and will call or message you shortly. Prefer to talk now? Call <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY.replace(" ","&nbsp;")}</a>.</div>
    <p class="form-note">No pressure, no upselling, we only suggest what your teeth actually need.</p>
  </div>
</div>'''

def schema(d):
    url = f"{SITE}/{d['slug']}/"
    faq_entities = ",".join(
        '{"@type":"Question","name":%s,"acceptedAnswer":{"@type":"Answer","text":%s}}' %
        (jstr(q), jstr(a)) for q, a in d["faqs"])
    return f'''<script type="application/ld+json">
{{
  "@context":"https://schema.org","@type":"Dentist","name":"Roots Dental Care",
  "url":"{url}","image":"{SITE}/assets/img/og.png","telephone":"{PHONE_TEL}","priceRange":"$$",
  "address":{{"@type":"PostalAddress","streetAddress":"T312, 4th Floor, Atlanta Shopping Center, Althan","addressLocality":"Surat","addressRegion":"Gujarat","postalCode":"395017","addressCountry":"IN"}},
  "areaServed":["Althan","Vesu","Adajan","Piplod","Surat"],
  "openingHoursSpecification":[
    {{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],"opens":"10:00","closes":"20:00"}},
    {{"@type":"OpeningHoursSpecification","dayOfWeek":"Sunday","opens":"10:00","closes":"13:30"}}
  ]
}}
</script>
<script type="application/ld+json">
{{
  "@context":"https://schema.org","@type":"MedicalProcedure","name":{jstr(d["service_name"])},
  "howPerformed":{jstr(d["service_desc"])},
  "procedureType":"https://schema.org/TherapeuticProcedure",
  "provider":{{"@type":"Dentist","name":"Roots Dental Care","url":"{url}","telephone":"{PHONE_TEL}",
    "address":{{"@type":"PostalAddress","addressLocality":"Surat","addressRegion":"Gujarat","postalCode":"395017","addressCountry":"IN"}}}}
}}
</script>
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{faq_entities}]}}
</script>
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
  {{"@type":"ListItem","position":1,"name":"Home","item":"{SITE}/"}},
  {{"@type":"ListItem","position":2,"name":"Treatments","item":"{SITE}/#services"}},
  {{"@type":"ListItem","position":3,"name":{jstr(d["service_name"])},"item":"{url}"}}
]}}
</script>'''

def jstr(s):
    import json
    return json.dumps(s, ensure_ascii=False)

def head(d):
    url = f"{SITE}/{d['slug']}/"
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(d["title"])}</title>
<meta name="description" content="{esc(d["meta"])}">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#006D75">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Roots Dental Care">
<meta property="og:title" content="{esc(d["title"])}">
<meta property="og:description" content="{esc(d["og"])}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/assets/img/og.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(d["title"])}">
<meta name="twitter:description" content="{esc(d["og"])}">
<meta name="twitter:image" content="{SITE}/assets/img/og.png">
<link rel="icon" type="image/png" href="/assets/img/favicon-64.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Schibsted+Grotesk:wght@500;600;700;800&family=Hanken+Grotesk:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap">
<link rel="stylesheet" href="/assets/css/styles.css">
{schema(d)}
</head>
<body>'''

def page(d):
    return "\n".join([
        head(d), header(), hero(d), statsband(d), included(d), why(d),
        specialist(d), crosslinks(d["slug"]), faqsection(d), location(),
        bookinline(d), footer(), FAB_SHEET, sheet(d),
        '<script src="/assets/js/main.js" defer></script>',
        "</body>\n</html>",
    ])

# --- per-service content ---------------------------------------------------

SERVICES = [
{
  "slug":"general-dentistry","short":"check-up","treatment":"Check-up & cleaning",
  "title":"General Dentistry in Althan, Surat | Roots Dental Care",
  "meta":"Gentle general dentistry in Althan, Surat, check-ups, scaling and polishing, tooth-coloured fillings and sensitivity care, most in a single visit. Free consultation and digital X-ray this month. Book appointment.",
  "og":"Check-ups, cleaning, fillings and sensitivity care, done gently and priced up front, in Althan, Surat.",
  "h1_main":"General Dentistry in","h1_accent":"Althan, Surat",
  "hero_sub":"Check-ups, cleaning, fillings and sensitivity care, done gently, priced up front, most finished in a single visit.",
  "eyebrow":"General & preventive dentistry",
  "stats":[("Same day","Most check-ups & fillings"),("Digital","X-rays on site"),("No-cost","EMI available"),("2000+","Families treated")],
  "incl_head":"Everything your routine dental care needs",
  "incl_intro":"The everyday treatments that keep small problems small, under one roof, by the doctor who trained for it.",
  "included":[
    ("Check-ups & oral exams","A thorough look with digital X-rays, so nothing is missed and you know exactly where you stand."),
    ("Scaling & polishing","Professional cleaning that lifts tartar and stains without harming enamel. The idea that scaling weakens teeth is a myth."),
    ("Tooth-coloured fillings","Cavities repaired with fillings matched to your tooth, so the repair is invisible and the tooth stays strong."),
    ("Sensitivity & early gum care","Sharp pain on cold or sweet, or gums that bleed when you brush, treated early before they turn into bigger, costlier problems."),
  ],
  "why_head":"Routine care that won't feel like the dentist you remember",
  "why_intro":"Why families in Althan, Vesu and Adajan make Roots their regular clinic.",
  "why":[
    ("Small problems caught early","Regular check-ups mean a filling instead of a root canal, and a cleaning instead of gum surgery."),
    ("Genuinely painless","Digital X-rays and a gentle hand. Most patients say routine care here is nothing like they remember."),
    ("One honest opinion","We tell you what your teeth actually need, and what can wait. No upselling."),
    ("Fits your week","Open six days with evening hours, and most routine work is done in a single visit."),
  ],
  "specialist":{
    "img":"/assets/img/clinic-1.jpg","alt":"Inside the Roots Dental Care clinic in Althan, Surat",
    "eyebrow":"Seen by the right specialist","name":"A routine visit, backed by four specialists",
    "role":"General dentistry at a multi-specialty clinic",
    "bio":"General dentistry here isn't handed to whoever is free. A routine visit is your entry to a four-specialist clinic, so the moment something needs an endodontist, a periodontist or an oral surgeon, they are already in the building. No referrals across the city, no starting over.",
    "cta":"Book a check-up"},
  "faq_head":"General dentistry in Surat, answered",
  "faqs":[
    ("How much does a dental check-up and cleaning cost in Surat?","We keep routine care affordable and tell you the full cost before we start. Your first consultation and digital X-ray are free this month, so you get a clear opinion at no risk."),
    ("Does scaling loosen or damage teeth?","No. This is one of the most common myths. Scaling removes hardened tartar that irritates the gums; it does not harm enamel. Teeth can feel slightly different afterwards simply because the buildup wedged between them is gone."),
    ("Do fillings hurt?","For most small cavities, no. We use digital imaging to be precise and gentle, and numb the area properly when needed. Most fillings are done comfortably in a single visit."),
    ("How often should I visit the dentist?","For most people, once every six months for a check-up and cleaning. If you are prone to cavities or gum problems, we may suggest coming a little more often."),
    ("Do you offer same-day treatment?","Yes. Most check-ups, cleanings and simple fillings are completed the same day. Message us on WhatsApp and we will find you a slot."),
    ("Where is Roots Dental Care located?","T312, 4th Floor, Atlanta Shopping Center, Althan, Surat 395017, serving Althan, Vesu, Adajan and Piplod."),
  ],
  "book_head":"Book your check-up, this month it's free",
  "service_name":"General Dentistry",
  "service_desc":"Routine dental examinations with digital X-rays, professional scaling and polishing, tooth-coloured fillings, and sensitivity and early gum care, most completed in a single visit.",
},
{
  "slug":"root-canal","short":"root canal","treatment":"Root canal",
  "title":"Painless Root Canal in Althan, Surat | Roots Dental Care",
  "meta":"Microscope-guided root canal treatment in Althan, Surat, often in a single sitting and far more comfortable than its reputation. Save your natural tooth. Free consultation and digital X-ray. Book appointment.",
  "og":"Microscope-guided root canal in Althan, Surat, often a single sitting, and far gentler than its reputation.",
  "h1_main":"Painless Root Canal in","h1_accent":"Althan, Surat",
  "hero_sub":"Microscope-guided, often finished in a single sitting, and far gentler than the reputation would have you believe.",
  "eyebrow":"Microscopic endodontics",
  "stats":[("Single","sitting, most cases"),("Microscope","guided precision"),("Save","the natural tooth"),("No-cost","EMI available")],
  "incl_head":"A root canal done properly, and comfortably",
  "incl_intro":"Done under magnification by an endodontist, so the tooth is cleaned thoroughly the first time, and lasts.",
  "included":[
    ("Microscope-guided treatment","Every canal found and cleaned under high magnification, the detail a naked eye misses, and the reason our root canals hold up."),
    ("Often a single sitting","Many teeth are treated and sealed in one visit, so you are not making trip after trip across the city."),
    ("Genuinely comfortable","Proper anaesthesia and a gentle technique. Most patients tell us it felt no worse than a filling."),
    ("Redo of failed root canals","A previous root canal that still hurts or flares up can usually be re-treated and saved, rather than pulled."),
    ("Crown to protect it","A treated tooth becomes brittle. We fit a crown so it takes normal biting force again and lasts for years."),
  ],
  "why_head":"Why a specialist root canal is worth it",
  "why_intro":"The difference between a tooth that is saved for years and one that fails in months.",
  "why":[
    ("Treated by an endodontist","Not a general dentist working it out, a specialist who does root canals every day and takes the difficult ones others refer out."),
    ("The tooth is saved","Where possible we keep your natural tooth, which is always better than removing and replacing it."),
    ("Priced up front, EMI available","You see the full cost before we begin, and no-cost EMI covers the treatment and the crown."),
    ("Fast relief","In pain now? Message us on WhatsApp, many emergencies are seen and settled the same day."),
  ],
  "specialist":{
    "img":"/assets/img/doctors/dr-nikil.jpg","alt":"Dr. Nikhilkumar Gudla, Microscopic Root Canal Specialist at Roots Dental Care",
    "eyebrow":"Your specialist","name":"Dr. Nikhilkumar Gudla","role":"Microscopic Root Canal Specialist",
    "bio":"Fellowship in advanced microscopic endodontics and various courses, certified by RCS Edinburgh. He is the specialist you want when a root canal is difficult, a canal is hard to find, or a previous treatment has failed, the cases that decide whether a tooth is saved or lost.",
    "cta":"Book with Dr. Nikhil"},
  "faq_head":"Root canals in Surat, answered",
  "faqs":[
    ("Is a root canal painful?","Not the way people fear. The pain patients associate with root canals is usually the infection beforehand. Under proper anaesthesia and a microscope, the treatment itself is comfortable, most say it felt like a routine filling, and the relief is immediate."),
    ("How many sittings does it take?","Many root canals are completed in a single sitting. More complex or badly infected teeth may need two. We will tell you which after the X-ray."),
    ("How much does a root canal cost in Surat?","It depends on the tooth and whether a crown is needed, and we share the full cost before starting, with no hidden charges. no-cost EMI is available, and your consultation and X-ray are free this month."),
    ("Should I just get the tooth pulled instead?","Saving your natural tooth is almost always better. An extraction leaves a gap that then needs an implant or bridge, usually more time and more cost than saving the tooth now."),
    ("Do I really need a crown afterwards?","For back teeth, in most cases yes. A root-canal-treated tooth becomes brittle; a crown protects it from cracking so it lasts for years."),
    ("My old root canal still hurts, can it be fixed?","Often, yes. A failed root canal can usually be re-treated under the microscope and saved, rather than removed."),
  ],
  "book_head":"Stop the pain, save the tooth",
  "service_name":"Root Canal Treatment",
  "service_desc":"Microscope-guided endodontic treatment that removes infection from inside the tooth, cleans and seals the canals, often in a single sitting, followed by a protective crown.",
},
{
  "slug":"dental-implants","short":"implant","treatment":"Dental implant / missing tooth",
  "title":"Dental Implants in Althan, Surat | Roots Dental Care",
  "meta":"Dental implants in Althan, Surat by an implantologist with 5000+ implants placed. Single tooth to full-mouth fixed teeth, bone grafting in-house, no-cost EMI. Free consultation and digital X-ray. Book appointment.",
  "og":"Dental implants in Althan, Surat, single tooth to full-mouth fixed teeth, 5000+ placed, no-cost EMI.",
  "h1_main":"Dental Implants in","h1_accent":"Althan, Surat",
  "hero_sub":"Replace missing teeth for good, single tooth to full-mouth fixed teeth, with 5,000+ implants placed and no-cost EMI.",
  "eyebrow":"Implantology",
  "stats":[("5000+","Implants placed"),("Full-mouth","fixed-teeth options"),("In-house","bone grafting"),("No-cost","EMI available")],
  "incl_head":"From a single gap to a full set of fixed teeth",
  "incl_intro":"Implants that look, feel and bite like your own, placed by a specialist and planned on 3D imaging.",
  "included":[
    ("Single & multiple implants","One missing tooth or several, replaced without grinding down the healthy teeth on either side."),
    ("Full-mouth fixed teeth","A full arch of fixed teeth on as few as four implants (All-on-4 / All-on-6), for those tired of loose, removable dentures."),
    ("Bone grafting & sinus lift in-house","Not enough bone? We rebuild it here, so ‘you are not a candidate’ rarely turns out to be true."),
    ("Guided, precise placement","Planned on 3D scans and placed accurately, which is what makes an implant last."),
    ("Priced up front, no-cost EMI","The full cost before we start, and EMI that makes even full-mouth work manageable."),
  ],
  "why_head":"Why patients choose Roots for implants",
  "why_intro":"Complex cases and severe bone loss are routine here, not a first attempt.",
  "why":[
    ("5,000+ implants placed","Experience you cannot fake. The difficult cases and severe bone loss are everyday work here."),
    ("Implantologist-led","Placed by a periodontist and implant specialist, Munich-certified, not handed to a general dentist."),
    ("Everything under one roof","Grafting, placement and the final teeth all here, so you are not sent between clinics."),
    ("Built to last","Quality implant systems and precise placement, so your investment holds up for the long run."),
  ],
  "specialist":{
    "img":"/assets/img/doctors/dr-dhawal.jpg","alt":"Dr. Dhawal Shah, Periodontist and Implantologist at Roots Dental Care",
    "eyebrow":"Your specialist","name":"Dr. Dhawal Shah","role":"Periodontist & Implantologist · MDS",
    "bio":"Implant Foundation (Munich) certified, with over 5,000 implants placed. He rebuilds smiles even where the bone has been severely lost, the full-mouth and ‘no other clinic would attempt it’ cases.",
    "cta":"Book with Dr. Dhawal"},
  "faq_head":"Dental implants in Surat, answered",
  "faqs":[
    ("How much does a dental implant cost in Surat?","It depends on how many teeth, the implant system and whether bone grafting is needed. We give you the full plan and cost before starting, with no hidden charges, and no-cost EMI to spread it. The consultation and X-ray are free this month."),
    ("Does getting an implant hurt?","Placing an implant is usually more comfortable than an extraction. It is done under local anaesthesia, and most patients are back to normal the next day with simple aftercare."),
    ("How long does the whole process take?","The implant is placed in a single appointment, then integrates with the bone over a few weeks to a few months before the final tooth goes on. Some cases allow immediate fixed teeth, we will tell you at the consultation."),
    ("I've been told I don't have enough bone. Can I still get implants?","Very often, yes. We do bone grafting and sinus lifts in-house to rebuild the site, so patients turned away elsewhere can usually still be treated."),
    ("Implant, bridge or denture, which is better?","An implant is the only option that replaces the root, does not damage neighbouring teeth, and does not come loose like a denture. For most people it is the longest-lasting choice, which is why we usually recommend it."),
    ("How long do dental implants last?","With good care and regular check-ups, a well-placed implant can last many years, often decades. Precise placement and quality components are what make the difference."),
  ],
  "book_head":"Replace missing teeth, for good",
  "service_name":"Dental Implants",
  "service_desc":"Titanium implants that replace missing teeth from a single gap to a full arch, planned on 3D imaging and placed by an implantologist, with bone grafting and sinus lifts performed in-house where needed.",
},
{
  "slug":"smile-design","short":"smile","treatment":"Smile design / whitening",
  "title":"Smile Design & Veneers in Althan, Surat | Roots Dental Care",
  "meta":"Smile makeovers in Althan, Surat, veneers, teeth whitening and digital smile design. See your new smile on screen before we begin. Natural, colour-matched results. Free consultation. Book appointment.",
  "og":"Veneers, whitening and digital smile design in Althan, Surat, see your new smile before we begin.",
  "h1_main":"Smile Design in","h1_accent":"Althan, Surat",
  "hero_sub":"Veneers, whitening and digital smile design, see your new smile on screen before we touch a single tooth.",
  "eyebrow":"Cosmetic dentistry",
  "stats":[("Digital","smile preview"),("Natural","colour-matched"),("No-cost","EMI available"),("2000+","Smiles cared for")],
  "incl_head":"A smile designed around your face, not a template",
  "incl_intro":"Planned digitally so you see the result first, then created with veneers, whitening and fine cosmetic work.",
  "included":[
    ("Digital smile design","We design your new smile on screen and show you the preview, you approve the look before any treatment begins."),
    ("Veneers & laminates","Chips, gaps, stains and worn edges corrected with veneers colour-matched so closely no one can tell."),
    ("Professional whitening","Safe, in-clinic whitening that lifts years of coffee, tea and staining in a single session."),
    ("Gap & shape correction","Close gaps, reshape uneven teeth and fix a gummy smile, small changes that change the whole face."),
  ],
  "why_head":"Why a smile makeover here looks natural",
  "why_intro":"The goal is a smile that looks like yours on a good day, not a row of identical blocks.",
  "why":[
    ("You see it before you commit","The digital preview means no surprises, you sign off on the smile before we start."),
    ("Natural, not obvious","Shape and shade matched to your face and your existing teeth, so the result reads as real."),
    ("Specialist clinic behind it","If a tooth needs a root canal or an implant first, the specialists are already here, the cosmetics sit on a healthy foundation."),
    ("Priced up front, EMI available","You get the full plan and cost before starting, with no-cost EMI to spread a full makeover."),
  ],
  "specialist":{
    "img":"/assets/img/clinic-1.jpg","alt":"Smile design and cosmetic dentistry at Roots Dental Care, Althan, Surat",
    "eyebrow":"How we work","name":"Designed digitally, done by specialists",
    "role":"Digital smile design at a multi-specialty clinic",
    "bio":"A great smile has to be built on healthy teeth. Because Roots is a full multi-specialty clinic, your smile design is planned around what your teeth actually need, whitening and veneers where that is enough, and the right specialist on hand when a tooth needs treating first. You see the plan, and the preview, before anything begins.",
    "cta":"Book a smile consult"},
  "faq_head":"Smile design in Surat, answered",
  "faqs":[
    ("How much do veneers and teeth whitening cost in Surat?","It depends on how many teeth and the type of veneer or whitening. You will get the full plan and cost before starting, with no-cost EMI available, and the consultation is free this month."),
    ("Will veneers look natural?","That is the whole point of designing digitally. We match shape and shade to your face and existing teeth, and you approve the preview first, the aim is natural, not obvious."),
    ("Do veneers ruin the teeth underneath?","Modern veneers are conservative and remove very little tooth structure, some need almost none. We only prepare what is necessary, and always explain exactly what is involved."),
    ("How long does a smile makeover take?","Whitening can be done in a single session. Veneers typically take two to three visits over a couple of weeks. A full makeover is planned so you know the timeline up front."),
    ("Is teeth whitening safe, and how long does it last?","Professional in-clinic whitening is safe when done by a dentist. Results last many months, and longer with simple care, avoiding heavy staining and the occasional touch-up keep it bright."),
    ("Can I see the result before I decide?","Yes. We show you a digital preview of your new smile before any treatment, so you decide with the outcome in front of you."),
  ],
  "book_head":"See your new smile before you begin",
  "service_name":"Smile Design & Cosmetic Dentistry",
  "service_desc":"Cosmetic dentistry including digital smile design previews, porcelain and composite veneers, professional in-clinic whitening, and gap, shape and gummy-smile correction, colour-matched for a natural result.",
},
{
  "slug":"kids-dentistry","short":"child's","treatment":"My child's teeth",
  "title":"Kids' Dentistry in Althan, Surat | Roots Dental Care",
  "meta":"Child-friendly pediatric dentistry in Althan, Surat. Gentle check-ups, cavity fillings, fluoride and sealants, and calm care for anxious children, led by an MDS pediatric dentist. Free consultation. Book appointment.",
  "og":"Gentle pediatric dentistry in Althan, Surat, led by an MDS pediatric dentist. Calm care for anxious kids.",
  "h1_main":"Kids' Dentistry in","h1_accent":"Althan, Surat",
  "hero_sub":"Gentle, unhurried care that keeps children calm, from the first visit to fillings, fluoride and sealants.",
  "eyebrow":"Pediatric dentistry",
  "stats":[("MDS","pediatric dentist"),("Calm","first-visit friendly"),("Painless","child technique"),("Six days","evening hours")],
  "incl_head":"Dental visits your child won't dread",
  "incl_intro":"Led by a pediatric specialist who makes the chair feel safe, so good habits start early and stay.",
  "included":[
    ("Gentle check-ups & cleaning","A calm, unhurried first visit that teaches your child the dentist is nothing to fear."),
    ("Cavity fillings","Child-friendly, comfortable fillings. Treating baby teeth matters, because they hold the space for the adult ones."),
    ("Fluoride & sealants","Simple preventive treatments that protect the grooves where cavities usually start."),
    ("Anxious & first-time kids","Patient handling for nervous children, with no drama, often the difference between a lifelong fear and none."),
    ("Habit guidance","Help with thumb-sucking, bottle habits and brushing that saves bigger trouble later."),
  ],
  "why_head":"Why parents trust their kids to Roots",
  "why_intro":"Children are not small adults, and they are not treated like them here.",
  "why":[
    ("A specialist, not a general dentist","An MDS pediatric dentist is trained specifically in how children feel, behave and heal."),
    ("Calm, patient, no drama","The pace is set by your child. The first visit is about trust, not treatment."),
    ("Prevention first","Sealants, fluoride and honest advice, so we are preventing cavities rather than filling them."),
    ("Easy for parents","Open six days with evening hours, and honest guidance on what your child actually needs."),
  ],
  "specialist":{
    "img":"/assets/img/doctors/dr-neha.jpg","alt":"Dr. Neha Saradhara, Pediatric Dentist at Roots Dental Care",
    "eyebrow":"Your specialist","name":"Dr. Neha Saradhara","role":"Pediatric Dentist · MDS",
    "bio":"She makes the dentist feel safe for children, patient, gentle and never rushed, while quietly building the habits that keep their teeth healthy for life. Nervous and first-time children are her speciality.",
    "cta":"Book with Dr. Neha"},
  "faq_head":"Kids' dentistry in Surat, answered",
  "faqs":[
    ("At what age should my child first see a dentist?","Ideally by their first birthday, or when the first teeth appear. Early visits are short and friendly, they catch problems while they are tiny, and they build a child who is not scared of the dentist."),
    ("My child is terrified of the dentist. How do you handle that?","Gently and without rushing. The first visit is often just about getting comfortable, meeting the chair, a count of the teeth. Most anxious children settle once they realise it does not hurt."),
    ("Baby teeth fall out anyway, are they worth treating?","Yes. Baby teeth hold the space for adult teeth and are needed for eating and speech. An untreated cavity can be painful and can affect the adult tooth forming underneath."),
    ("How much does a child's filling or check-up cost?","We keep children's treatment affordable and tell you the cost up front. The first consultation is free this month."),
    ("Do you use sedation for children?","Most children do beautifully with a calm, patient approach and need nothing more. Where a very nervous child or a bigger treatment calls for it, we will discuss safe options with you first."),
    ("Are sealants and fluoride really worth it?","For most children, yes. They are quick, painless and protect exactly the spots where cavities usually begin, cheaper and easier than treating a cavity later."),
  ],
  "book_head":"A dentist your child won't be scared of",
  "service_name":"Pediatric Dentistry",
  "service_desc":"Child-focused dental care including gentle check-ups and cleaning, cavity fillings, fluoride application and sealants, habit counselling, and calm handling of anxious and first-time children, led by an MDS pediatric dentist.",
},
]

def main():
    for d in SERVICES:
        folder = os.path.join(ROOT, d["slug"])
        os.makedirs(folder, exist_ok=True)
        with open(os.path.join(folder, "index.html"), "w", encoding="utf-8") as f:
            f.write(page(d))
        print("wrote", d["slug"] + "/index.html")

if __name__ == "__main__":
    main()
