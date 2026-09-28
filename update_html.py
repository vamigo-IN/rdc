import re

with open('index.html', 'r') as f:
    html = f.read()

# 1. Update Header Button (line ~121)
html = re.sub(r'<a href="#book-inline" class="btn btn-red" data-open-book>Book Appointment</a>', 
              r'<a href="#book-inline" class="btn btn-primary" data-open-book>BOOK APPOINTMENT</a>', html)
              
# Make phone number clickable in header
html = html.replace('<div class="nav-phone"><svg width="18" height="18"', '<a href="tel:+917990376179" class="nav-phone"><svg width="18" height="18"')
html = html.replace('76179</div>', '76179</a>')

# 2. Update Hero Section
hero_old = r'''<span class="offer-tag"><span class="dotpulse green-dot"></span>This month: <strong>Free</strong> Consultation \+ Digital X-Ray</span>
    <h1>Professional Dental Care<br><span class="accent">for You & Your Family</span></h1>
    <div class="hero-cta">
      <a href="#book-inline" class="btn btn-teal" data-open-book>Book Appointment</a>
      <a href="tel:\+917990376179" class="btn btn-glass">Call the clinic</a>
    </div>
    <div class="hero-trust-strip">'''
hero_new = r'''<span class="eyebrow" style="color:#A4F4F3; font-size:0.85rem; letter-spacing:0.1em; margin-bottom:12px; display:inline-block;">Professional Dental Care in Althan, Surat</span>
    <h1 style="margin-top:0;">Healthy, confident smiles <br><span class="accent">for you & your family</span></h1>
    <p style="font-size:1.1rem; max-width:600px; margin-bottom:24px; opacity:0.9;">9 dental specialties. Experienced specialists. Patient-focused care based on what your teeth actually need.</p>
    <div class="hero-cta">
      <a href="#book-inline" class="btn btn-primary" data-open-book>BOOK APPOINTMENT</a>
      <a data-wa href="#" class="btn btn-wa" target="_blank" rel="noopener"><svg viewBox="0 0 24 24"><path d="M12 2a10 10 0 0 0-8.5 15.2L2 22l4.9-1.4A10 10 0 1 0 12 2Zm0 18a8 8 0 0 1-4.1-1.1l-.3-.2-2.9.8.8-2.8-.2-.3A8 8 0 1 1 12 20Zm4.4-6c-.2-.1-1.4-.7-1.6-.8-.2-.1-.4-.1-.5.1l-.7.9c-.1.2-.3.2-.5.1a6.5 6.5 0 0 1-3.2-2.8c-.1-.2 0-.4.1-.5l.4-.5c.1-.2.1-.3 0-.5l-.7-1.7c-.2-.4-.4-.4-.5-.4h-.5c-.2 0-.5.1-.7.3-.7.7-.9 1.6-.6 2.6.4 1.4 1.3 2.7 2.6 3.7 1.6 1.3 3 1.6 3.7 1.5.5-.1 1.3-.6 1.5-1.1.2-.5.2-.9.1-1-.1-.1-.2-.1-.4-.2Z"/></svg>WHATSAPP US</a>
    </div>
    <div class="hero-trust-strip">'''
html = re.sub(hero_old, hero_new, html)

# Fix trust strip layout slightly if needed (already fine)
html = html.replace('<span>Google 5-Star Rated</span><span class="sep">|</span><span>Althan, Surat</span><span class="sep">|</span><span>Open 7 days a week</span>', '<span>Google 5-Star Rated</span><span class="sep">|</span><span>Experienced specialists</span><span class="sep">|</span><span>Althan, Surat</span><span class="sep">|</span><span>Open 7 days a week</span>')

# 3. Services Section
html = html.replace('<h2>Comprehensive Care</h2>\n        <p>From routine check-ups to advanced full-mouth rehabilitation, everything is done under one roof by specialists.</p>', '<h2>Here is what we can help you with.</h2>\n        <p>From routine check-ups to advanced full-mouth rehabilitation, everything is done under one roof by specialists.</p>')

# Update service cards to have "Learn More ->" (I'll just add it to the first few high intent ones)
services_to_update = ['Root Canal', 'Dental Implants', 'Smile Designing & Cosmetic', 'Wisdom Teeth & Surgery', 'Braces & Clear Aligners']
for svc in services_to_update:
    html = re.sub(rf'(<h3>{svc}</h3>\s*<p>.*?)</p>', r'\1 <br><br><span style="color:var(--teal); font-weight:600; font-size:0.9rem;">Learn More &rarr;</span></p>', html)

# 4. Why Roots
html = html.replace('<p>Five reasons you won\'t feel like you\'re at the dentist you remember.</p>', '<p>Five reasons you won\'t feel like you\'re at the dentist you remember.</p>\n        <br>\n        <a data-wa href="#" class="btn btn-secondary">TALK TO A DENTIST</a>')

# 5. Doctors Section
doc_names = ['Dr. Nikhil Shah', 'Dr. Dhawal Shah', 'Dr. Dhyey Shah', 'Dr. Neha Shah']
for doc in doc_names:
    html = re.sub(rf'(<h3>{doc}</h3>\s*<p class="role">.*?</p>\s*<p class="desc">.*?)</p>', rf'\1</p>\n          <a href="#book-inline" class="btn btn-primary" style="margin-top:16px; width:100%;" data-open-book>BOOK WITH {doc.upper()}</a>', html)

# 6. Honest Care Band
html = html.replace('<p>We take pride in our conservative approach. We explain exactly what your teeth need, what they don\'t, and we show you the full cost before we begin.</p>', '<p>We take pride in our conservative approach. We explain exactly what your teeth need, what they don\'t, and we show you the full cost before we begin.</p>\n      <br>\n      <a data-wa href="#" class="btn btn-secondary" style="background:#fff; color:var(--ink);">TALK TO A DENTIST</a>')

# 7. Reviews Section
html = html.replace('<p>What our patients in Surat say about their treatment.</p>', '<p>What our patients in Surat say about their treatment.</p>\n        <br>\n        <div style="display:flex; gap:12px; flex-wrap:wrap;">\n          <a href="https://maps.app.goo.gl/DxogEZhVLLLkT5VC6" target="_blank" rel="noopener" class="btn btn-secondary">READ GOOGLE REVIEWS</a>\n          <a href="#book-inline" class="btn btn-primary" data-open-book>BOOK APPOINTMENT</a>\n        </div>')

# 8. FAQ Section
html = html.replace('<h2>Questions? We have answers.</h2>', '<h2>Questions? We have answers.</h2>\n        <p>Still have questions? Talk to our dental team and find the right next step.</p>\n        <br>\n        <div style="display:flex; gap:12px; flex-wrap:wrap; margin-bottom:32px;">\n          <a data-wa href="#" class="btn btn-wa"><svg viewBox="0 0 24 24"><path d="M12 2a10 10 0 0 0-8.5 15.2L2 22l4.9-1.4A10 10 0 1 0 12 2Zm0 18a8 8 0 0 1-4.1-1.1l-.3-.2-2.9.8.8-2.8-.2-.3A8 8 0 1 1 12 20Zm4.4-6c-.2-.1-1.4-.7-1.6-.8-.2-.1-.4-.1-.5.1l-.7.9c-.1.2-.3.2-.5.1a6.5 6.5 0 0 1-3.2-2.8c-.1-.2 0-.4.1-.5l.4-.5c.1-.2.1-.3 0-.5l-.7-1.7c-.2-.4-.4-.4-.5-.4h-.5c-.2 0-.5.1-.7.3-.7.7-.9 1.6-.6 2.6.4 1.4 1.3 2.7 2.6 3.7 1.6 1.3 3 1.6 3.7 1.5.5-.1 1.3-.6 1.5-1.1.2-.5.2-.9.1-1-.1-.1-.2-.1-.4-.2Z"/></svg>WHATSAPP US</a>\n          <a href="#book-inline" class="btn btn-primary" data-open-book>BOOK APPOINTMENT</a>\n        </div>')

# 9. Location Section
html = html.replace('<h2>We are easy to find.</h2>\n        <p>Located in the heart of Althan, with ample parking and elevator access.</p>', '<h2>Visit Roots Dental Care in Althan, Surat</h2>\n        <p>Easy to find. Open 7 days a week.</p>')
html = html.replace('<a href="tel:+917990376179" class="btn btn-teal">Call 79903 76179</a>', '<a href="tel:+917990376179" class="btn btn-secondary">CALL CLINIC</a>')
html = html.replace('<a href="https://maps.app.goo.gl/DxogEZhVLLLkT5VC6" target="_blank" rel="noopener" class="btn btn-ghost">Get directions</a>', '<a href="https://maps.app.goo.gl/DxogEZhVLLLkT5VC6" target="_blank" rel="noopener" class="btn btn-primary">GET DIRECTIONS</a>')

# 10. Final Booking Section
html = html.replace('<h2>Ready for a healthy smile?</h2>\n        <p>Book your visit today. No waiting, no surprises, just premium dental care.</p>', '<h2>Book Your Dental Visit</h2>\n        <p>Tell us what you need help with and our team will help you take the next step.</p>')
html = html.replace('<button type="submit" class="btn btn-red">Book Appointment</button>', '<button type="submit" class="btn btn-primary">BOOK MY APPOINTMENT</button>')
html = html.replace('<a href="tel:+917990376179" class="btn btn-teal" style="margin-top:12px; width:100%;">Call 79903 76179</a>', '<a href="tel:+917990376179" class="btn btn-secondary" style="margin-top:12px; width:100%;">CALL CLINIC</a>')


# 11. Mobile CTA Bar & Floating Actions
# Simplify floating actions (remove maps)
html = html.replace('''<a class="fab fab-maps" href="https://maps.app.goo.gl/DxogEZhVLLLkT5VC6" target="_blank" rel="noopener" aria-label="Get directions on Google Maps">
    <svg viewBox="0 0 24 24" fill="none"><path d="M12 21s7-6.2 7-11a7 7 0 1 0-14 0c0 4.8 7 11 7 11Z" stroke="#fff" stroke-width="1.8"/><circle cx="12" cy="10" r="2.5" fill="#fff"/></svg>
  </a>\n  ''', '')

# Insert Mobile CTA Bar right before </body>
mobile_bar = '''
<!-- ===== MOBILE CTA BAR ===== -->
<div class="mobile-cta-bar">
  <a href="tel:+917990376179" class="m-call">
    <svg viewBox="0 0 24 24" fill="none"><path d="M6.5 3h3l1.5 4-2 1.5a11 11 0 0 0 4.5 4.5l1.5-2 4 1.5v3a2 2 0 0 1-2.2 2A16 16 0 0 1 4.5 5.2 2 2 0 0 1 6.5 3Z" fill="currentColor"/></svg>
    CALL
  </a>
  <a data-wa href="#" class="m-wa" target="_blank" rel="noopener">
    <svg viewBox="0 0 24 24"><path d="M12 2a10 10 0 0 0-8.5 15.2L2 22l4.9-1.4A10 10 0 1 0 12 2Zm0 18a8 8 0 0 1-4.1-1.1l-.3-.2-2.9.8.8-2.8-.2-.3A8 8 0 1 1 12 20Zm4.4-6c-.2-.1-1.4-.7-1.6-.8-.2-.1-.4-.1-.5.1l-.7.9c-.1.2-.3.2-.5.1a6.5 6.5 0 0 1-3.2-2.8c-.1-.2 0-.4.1-.5l.4-.5c.1-.2.1-.3 0-.5l-.7-1.7c-.2-.4-.4-.4-.5-.4h-.5c-.2 0-.5.1-.7.3-.7.7-.9 1.6-.6 2.6.4 1.4 1.3 2.7 2.6 3.7 1.6 1.3 3 1.6 3.7 1.5.5-.1 1.3-.6 1.5-1.1.2-.5.2-.9.1-1-.1-.1-.2-.1-.4-.2Z"/></svg>
    WHATSAPP
  </a>
  <a href="#book-inline" class="m-book" data-open-book>
    BOOK APPOINTMENT
  </a>
</div>
'''
html = html.replace('</body>', mobile_bar + '\n</body>')

with open('index.html', 'w') as f:
    f.write(html)
