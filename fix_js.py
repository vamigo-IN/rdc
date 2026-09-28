import re

with open('assets/js/main.js', 'r') as f:
    js = f.read()

# Fix sendToSheet
match_sendToSheet = re.search(r'function sendToSheet\(data\) \{.*?\return Promise\.race\(\[req, timeout\]\);\n  \}', js, flags=re.DOTALL)
if match_sendToSheet:
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
    }).then(function(res) { return res.json(); });
    
    var timeout = new Promise(function (_, reject) { setTimeout(function() { reject("timeout"); }, 8000); });
    return Promise.race([req, timeout]);
  }"""
    js = js.replace(match_sendToSheet.group(0), new_sendToSheet)

# Fix handleSubmit
match_handleSubmit = re.search(r'function handleSubmit\(e\) \{.*?\sendToSheet\(data\)\.then\(proceed, proceed\);\n  \}', js, flags=re.DOTALL)
if match_handleSubmit:
    new_handleSubmit = """  function handleSubmit(e) {
    e.preventDefault();
    var form = e.currentTarget;
    var name = form.querySelector('[name="name"]');
    var phone = form.querySelector('[name="phone"]');

    var digits = (phone.value || "").replace(/\\D/g, "");
    var ok = true;
    if (!name.value.trim()) { name.classList.add("invalid"); ok = false; } else { name.classList.remove("invalid"); }
    if (digits.length < 10) { phone.classList.add("invalid"); ok = false; } else { phone.classList.remove("invalid"); }
    if (!ok) { (name.value.trim() ? phone : name).focus(); return; }

    var tEl = form.querySelector('[name="treatment"]'), timeEl = form.querySelector('[name="time"]');
    var src = form.closest("#booking") ? "Popup" :
              form.closest("#book-hero") ? "Hero form" :
              form.closest("#book-inline") ? "Inline form" : "Form";
    var data = {
      name: name.value.trim(),
      phone: digits,
      treatment: (tEl && tEl.value) || "General enquiry",
      time: (timeEl && timeEl.value) || "Any time",
      source: src
    };

    var btn = form.querySelector('button[type="submit"]');
    var btnHtml = btn ? btn.innerHTML : "";
    if (btn) { btn.disabled = true; btn.textContent = "Sending…"; }

    sendToSheet(data).then(function(resData) {
      sendEmail(data);
      track("lead_submit");
      if (btn) { btn.innerHTML = "Sent!"; }
      var ref = resData && resData.leadId ? "\\n\\n(Ref: " + resData.leadId + ")" : "";
      var url = "https://wa.me/" + CONFIG.whatsappNumber + "?text=" + encodeURIComponent(buildMessage(data) + ref);
      window.open(url, "_blank");
      var okBox = form.parentNode.querySelector(".form-ok");
      if (okBox) { okBox.style.display = "block"; okBox.textContent = "Redirecting to WhatsApp..."; }
      try { form.reset(); } catch (_) {}
    }).catch(function(err) {
      // Fallback
      sendEmail(data);
      track("lead_submit");
      if (btn) { btn.disabled = false; btn.innerHTML = btnHtml; }
      var url = "https://wa.me/" + CONFIG.whatsappNumber + "?text=" + encodeURIComponent(buildMessage(data));
      window.open(url, "_blank");
      var okBox = form.parentNode.querySelector(".form-ok");
      if (okBox) { okBox.style.display = "block"; okBox.textContent = "Redirecting to WhatsApp..."; }
      try { form.reset(); } catch (_) {}
    });
  }"""
    js = js.replace(match_handleSubmit.group(0), new_handleSubmit)

with open('assets/js/main.js', 'w') as f:
    f.write(js)
