# Google Ads lead-gen — setup for the Roots Dental Care landing page

The landing page is built to capture and track leads. Here's what's already
wired, and the few things you set before launching ads.

## Already done
- Booking popup → opens WhatsApp with the patient's details **and** emails a copy.
- Floating WhatsApp / Call / Directions buttons.
- Conversion **events** fire on: form submit (`lead_submit`), WhatsApp tap
  (`whatsapp_click`), call tap (`call_click`).
- A **Privacy Policy** page at `/privacy.html`, linked in the footer
  (Google Ads requires this for lead-form ads).

## Turn on tracking — edit ONE file
Open `assets/js/main.js`, top `CONFIG` block, and paste your IDs:

```js
ga4Id: "G-XXXXXXXXXX",              // Google Analytics 4
googleAdsId: "AW-XXXXXXXXXX",       // Google Ads tag
googleAdsConversion: "AW-XXXXXXXXXX/AbCdEf_gHi",  // the conversion action
metaPixelId: "",                    // optional (Meta/Facebook)
```

Leave a field blank and it stays off — no scripts load, nothing breaks.
When set, the scripts load automatically and a **Google Ads conversion fires
on every lead action**.

## Get the conversion ID (Google Ads)
1. Google Ads → **Goals → Conversions → New conversion action → Website**.
2. Create one called **"Lead — Booking"**, category **Submit lead form**.
3. Choose **"Use Google tag"**. It gives you a tag ID `AW-XXXXXXXXXX` and a
   **conversion label**. Combine them: `AW-XXXXXXXXXX/AbCdEf_gHi` → paste into
   `googleAdsConversion`.
4. (Optional) Make separate actions for WhatsApp and Call if you want them
   counted separately — tell me and I'll split them in the code.

## GA4
Create a GA4 property, paste the `G-XXXXXXXXXX` into `ga4Id`, then in GA4 mark
`lead_submit` as a **Key event** so it flows into Google Ads as a conversion.

## Pre-launch checklist
- [ ] IDs pasted in `CONFIG`; deployed live.
- [ ] Test a booking on your phone → lead reaches WhatsApp/email.
- [ ] Verify the conversion fires with **Google Tag Assistant** (Chrome).
- [ ] Final URL domain matches the live domain and has the Privacy Policy link.
- [ ] Real offer set in the hero (currently "Free consultation + digital X-ray").
- [ ] Real Google reviews swapped in (placeholders now).
- [ ] In Google Ads, add **Call** and **Lead form** assets, and location = Surat.

## Tip
Point campaigns at high-intent keywords (e.g. "dental implants Althan",
"root canal Surat", "braces near me") — the `Dentist` schema and local keywords
are already in place to support Quality Score.
