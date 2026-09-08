# Save every booking to a Google Sheet (Apps Script)

Every form submission on the site (hero form, inline form, popup) is sent to
your Google Sheet as a row, with the treatment, phone, which page it came from,
and which form. It still opens WhatsApp and (if set) emails a copy — the sheet
is an extra, permanent record.

## One-time setup (about 3 minutes)

1. Create a Google Sheet (or open the one you want to use).
2. In the Sheet: **Extensions → Apps Script**. Delete anything there and paste
   the code below. Save.
3. **Deploy → New deployment → gear icon → Web app.**
   - **Description:** Roots leads
   - **Execute as:** Me
   - **Who has access:** Anyone
   - Click **Deploy**, authorise when asked, and **copy the Web app URL**
     (it ends in `/exec`).
4. Open `assets/js/main.js`, find the `CONFIG` block near the top, and paste the
   URL into `appsScriptUrl`:

   ```js
   appsScriptUrl: "https://script.google.com/macros/s/AKfyc.../exec"
   ```

5. Deploy the site. Submit a test booking — a new row should appear in the sheet
   within a second or two.

> Whenever you change the Apps Script code later, you must **Deploy → Manage
> deployments → edit → New version** (or the old code keeps running). Pasting the
> URL once is enough; the URL stays the same across new versions.

## The Apps Script code

```javascript
function doPost(e) {
  try {
    var ss = SpreadsheetApp.getActiveSpreadsheet();
    var sheet = ss.getSheetByName('Leads') || ss.insertSheet('Leads');
    if (sheet.getLastRow() === 0) {
      sheet.appendRow(['Timestamp', 'Name', 'Phone', 'Treatment',
                       'Preferred time', 'Form', 'Page', 'URL']);
    }
    var d = JSON.parse(e.postData.contents);
    sheet.appendRow([
      new Date(),
      d.name || '',
      d.phone || '',
      d.treatment || '',
      d.time || '',
      d.source || '',
      d.page || '',
      d.url || ''
    ]);
    return ContentService
      .createTextOutput(JSON.stringify({ ok: true }))
      .setMimeType(ContentService.MimeType.JSON);
  } catch (err) {
    return ContentService
      .createTextOutput(JSON.stringify({ ok: false, error: String(err) }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}
```

## Notes
- The site posts with `Content-Type: text/plain` and `mode: no-cors`. This is the
  reliable way for a static site to write to Apps Script without CORS errors. The
  browser can't read the response, but the row is still written — that's expected.
- Columns saved: **Timestamp, Name, Phone, Treatment, Preferred time, Form
  (Hero/Inline/Popup), Page, URL.** The Form and Page columns tell you which
  landing page and which form converted — useful for judging your Google Ads.
- Leave `appsScriptUrl` blank to turn sheet logging off; nothing breaks.
