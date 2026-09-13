# Lead capture — saves to Google Sheet AND emails you (Apps Script)

Every booking on the site is sent to your Apps Script, which does BOTH:
1. appends a row to your Google Sheet, and
2. emails the lead to you.

One endpoint, both outcomes — no SMTP, no Web3Forms needed.

---

## IMPORTANT: why you saw no leads

Apps Script runs the **deployed** version, not the code you see in the editor,
and it only accepts anonymous POSTs from the website when access is **"Anyone."**
99% of "no leads" cases are one of these:

- The Web-app deployment access is **"Only myself"** (must be **Anyone**).
- The code was edited but **not re-deployed as a new version**.
- The site was never deployed with the `/exec` URL in place.

The steps below fix all three, and there's a one-click test at the end.

---

## 1) Paste this code

In your Sheet → **Extensions → Apps Script** → delete everything → paste:

```javascript
// === Roots Dental Care — lead capture: Sheet + Email ===
var TO_EMAIL = "aditya@growven.ai";   // <-- WHERE LEAD EMAILS GO. Change to the
                                       //     clinic inbox. Comma-separate for many:
                                       //     "clinic@x.com, aditya@growven.ai"

function doPost(e) {
  try {
    var d = JSON.parse(e.postData.contents);

    // 1) Save to the Sheet
    var ss = SpreadsheetApp.getActiveSpreadsheet();
    var sheet = ss.getSheetByName('Leads') || ss.insertSheet('Leads');
    if (sheet.getLastRow() === 0) {
      sheet.appendRow(['Timestamp','Name','Phone','Treatment',
                       'Preferred time','Form','Page','URL']);
    }
    sheet.appendRow([new Date(), d.name||'', d.phone||'', d.treatment||'',
                     d.time||'', d.source||'', d.page||'', d.url||'']);

    // 2) Email you
    if (TO_EMAIL) {
      var subject = 'New booking: ' + (d.name||'Website lead') +
                    (d.treatment ? ' — ' + d.treatment : '');
      var body =
        'New enquiry from the website:\n\n' +
        'Name: '            + (d.name||'')      + '\n' +
        'Phone / WhatsApp: '+ (d.phone||'')     + '\n' +
        'Treatment: '       + (d.treatment||'') + '\n' +
        'Preferred time: '  + (d.time||'')      + '\n' +
        'Form: '            + (d.source||'')    + '\n' +
        'Page: '            + (d.page||'')      + '\n' +
        'URL: '             + (d.url||'')        + '\n\n' +
        'Call or WhatsApp them now while they are warm.';
      MailApp.sendEmail(TO_EMAIL, subject, body);
    }

    return ContentService.createTextOutput(JSON.stringify({ok:true}))
                         .setMimeType(ContentService.MimeType.JSON);
  } catch (err) {
    return ContentService.createTextOutput(JSON.stringify({ok:false, error:String(err)}))
                         .setMimeType(ContentService.MimeType.JSON);
  }
}

// Open the /exec URL in a browser to check the deployment is live + public.
function doGet(e) {
  return ContentService.createTextOutput('Roots lead endpoint is live')
                       .setMimeType(ContentService.MimeType.TEXT);
}
```

Set `TO_EMAIL` at the top. **Save** (disk icon).

## 2) Deploy correctly (this is the step people get wrong)

- If you have NO deployment yet: **Deploy → New deployment → gear → Web app.**
- If you already deployed once: **Deploy → Manage deployments → pencil (Edit)
  the existing one** — do NOT create a brand-new one, or the URL changes and the
  site would need updating.

In the dialog set:
- **Execute as:** Me
- **Who has access:** **Anyone**   ← must be this, not "Only myself"
- **Version:** **New version**      ← every code change needs a new version
- **Deploy** → **Authorize access** → allow Sheets + Send email.

Copy the **Web app URL** (ends in `/exec`). It should match the one already in the
site (`assets/js/main.js` → `appsScriptUrl`). If it's different, send it to me.

## 3) Test in 30 seconds

- **Open the `/exec` URL in a browser.** You should see: **"Roots lead endpoint is live"**.
  - If you instead see a Google sign-in / "you need permission" page → access is
    still "Only myself". Redeploy with **Anyone**.
  - If you see a 404 → the deployment doesn't exist; deploy it.
- Then submit a real test on the live site. Within ~2 seconds: a new **row** in the
  Sheet **and** an **email** to `TO_EMAIL`.
- Still nothing? Open the site, press **F12 → Console**, submit again, and look for
  `[RDC] sending lead to Google Sheet…`. If that line appears, the site is sending
  and the problem is on the Apps Script side (re-check access + new version).

## Notes
- Consumer Gmail sends up to ~100 emails/day via MailApp; Google Workspace ~1500.
  Plenty for a clinic.
- The site posts with `text/plain` + `no-cors` (required for a static site to reach
  Apps Script without CORS errors). The browser can't read the reply, but the row is
  written and the email sent — that's expected.
