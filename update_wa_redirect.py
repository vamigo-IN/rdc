import re

with open('assets/js/main.js', 'r') as f:
    js = f.read()

# Fix handleSubmit
match_handleSubmit = re.search(r'function handleSubmit\(e\) \{.*?\}\);\n  \}', js, flags=re.DOTALL)
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
    });
  }"""
    js = js.replace(match_handleSubmit.group(0), new_handleSubmit)

with open('assets/js/main.js', 'w') as f:
    f.write(js)
