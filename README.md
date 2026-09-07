# Roots Dental Care — Website

A fast, single-page site for Roots Dental Care (Althan, Surat). Plain static
HTML/CSS/JS — no build step, so Hostinger's Git tool serves it directly from
`public_html`. Bookings open WhatsApp with the patient's details pre-filled and
(optionally) email a copy to the clinic.

---

## 1. What's in here

```
index.html            The whole page
assets/css/styles.css Styling
assets/js/main.js      Booking form → WhatsApp + email, menu, analytics hooks
assets/img/            favicon.svg, og.png (social share image)
.htaccess              HTTPS redirect, gzip, caching, security headers
robots.txt, sitemap.xml
site.webmanifest
```

---

## 2. Before you go live — 4 things to set

All quick edits. Numbers already point to **79903 76179**.

1. **WhatsApp / email destination** — `assets/js/main.js`, top `CONFIG` block:
   - `whatsappNumber` — the number that should receive bookings (with `91`).
   - `web3formsKey` — paste your free key from https://web3forms.com to also get
     each lead by email. Leave blank and only WhatsApp is used.
2. **The offer** — search `index.html` for `free consultation + digital X-ray`
   and set your real, time-bound offer (hero pill + final section + og image text).
3. **Reviews** — the 3 testimonials in the "Patient stories" section are marked
   with a `REPLACE` comment. Swap in real Google reviews once available.
4. **Domain** — replace `https://www.rootsdentalcare.in/` throughout `index.html`,
   `sitemap.xml` and `robots.txt` with the live domain.

Doctor photos: drop images into `assets/img/` and replace the initials block in
each `.doc .ph` in `index.html`.

---

## 3. Deploy to Hostinger with Git

### One-time setup

**A. Put this repo on GitHub (or GitLab/Bitbucket)**

```bash
# from inside this folder
git remote add origin https://github.com/<you>/roots-dental-care.git
git branch -M main
git push -u origin main
```

**B. Connect it in Hostinger hPanel**

1. hPanel → **Websites** → your site → **Advanced → GIT**.
2. **Create a new repository**:
   - **Repository**: your repo URL (e.g. `https://github.com/<you>/roots-dental-care.git`)
   - **Branch**: `main`
   - **Directory**: leave **empty** to deploy into `public_html` (the site root).
3. Click **Create**. Hostinger clones the repo into `public_html`. The site is live.

> Private repo? Add Hostinger's deploy SSH key to the repo, or use a public repo.

### Auto-deploy on every push (recommended)

In the same GIT page, copy the **Webhook URL** and add it to your repo:
GitHub → repo **Settings → Webhooks → Add webhook** → paste URL →
Content type `application/json` → **Just the push event** → Add.

Now every `git push` updates the live site automatically.

### Updating the site later

```bash
git add -A
git commit -m "Update offer wording"
git push
```

The webhook redeploys within seconds. (No webhook? hPanel GIT page → **Deploy**.)

---

## 4. Analytics (when ready)

The form already fires `lead_submit`, `whatsapp_click` and `call_click`. To
capture them, paste your **GA4** and/or **Meta Pixel** snippet into `<head>` of
`index.html` — the events wire up automatically, giving your Meta/Google
campaigns real conversions to optimise on.

---

## 5. Local preview

Open `index.html` in a browser, or:

```bash
python3 -m http.server 8000   # then visit http://localhost:8000
```
