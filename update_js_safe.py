with open('assets/js/main.js', 'r') as f:
    js = f.read()

old_sendToSheet = """  function sendToSheet(data) {
    if (!CONFIG.appsScriptUrl) return Promise.resolve(); // logging off until URL set
    try { console.info("[RDC] sending lead to Google Sheet…", data.source); } catch (e) {}
    var req = fetch(CONFIG.appsScriptUrl, {
      method: "POST",
      mode: "no-cors",
      headers: { "Content-Type": "text/plain;charset=utf-8" },
      body: JSON.stringify({
        name: data.name,
        phone: data.phone,
        treatment: data.treatment,
        time: data.time,
        page: (document.title || ""),
        url: location.href,
        source: data.source || ""
      })
    }).catch(function () { /* network error — don't block the lead */ });
    var timeout = new Promise(function (res) { setTimeout(res, 8000); });
    return Promise.race([req, timeout]);
  }"""

new_sendToSheet = """  function sendToSheet(data) {
    if (!CONFIG.appsScriptUrl) return Promise.resolve({});
    try { console.info("[RDC] sending lead to Google Sheet…", data.source); } catch (e) {}
    var req = fetch(CONFIG.appsScriptUrl, {
      method: "POST",
      headers: { "Content-Type": "text/plain;charset=utf-8" },
      body: JSON.stringify({
        name: data.name,
        phone: data.phone,
        treatment: data.treatment,
        time: data.time,
        page: (document.title || ""),
        url: location.href,
        source: data.source || ""
      })
    }).then(function(res) { return res.json(); }).catch(function() { return {}; });
    var timeout = new Promise(function (_, reject) { setTimeout(function() { reject("timeout"); }, 8000); });
    return Promise.race([req, timeout]);
  }"""

old_handleSubmit = """    function proceed() {
      sendEmail(data);
      track("lead_submit");
      var okBox = form.parentNode.querySelector(".form-ok");
      if (okBox) okBox.style.display = "block";
      if (btn) { btn.disabled = false; btn.innerHTML = btnHtml; }
      try { form.reset(); } catch (_) {}
    }

    // Save the lead to the sheet (+ email), then show the confirmation.
    // No WhatsApp redirect. Resolves either way (success, network error, or the
    // 8s timeout) so the visitor always sees the confirmation.
    sendToSheet(data).then(proceed, proceed);"""

new_handleSubmit = """    sendToSheet(data).then(function(resData) {
      sendEmail(data);
      track("lead_submit");
      if (btn) { btn.innerHTML = "Sent!"; }
      var okBox = form.parentNode.querySelector(".form-ok");
      if (okBox) { okBox.style.display = "block"; okBox.textContent = "Thank you. We have your details and will call or email you shortly."; }
      try { form.reset(); } catch (_) {}
    }).catch(function(err) {
      // Fallback
      sendEmail(data);
      track("lead_submit");
      if (btn) { btn.disabled = false; btn.innerHTML = btnHtml; }
      var okBox = form.parentNode.querySelector(".form-ok");
      if (okBox) { okBox.style.display = "block"; okBox.textContent = "Thank you. We have your details and will call or email you shortly."; }
      try { form.reset(); } catch (_) {}
    });"""

js = js.replace(old_sendToSheet, new_sendToSheet)
js = js.replace(old_handleSubmit, new_handleSubmit)

with open('assets/js/main.js', 'w') as f:
    f.write(js)
