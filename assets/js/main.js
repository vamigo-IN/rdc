/* ==========================================================================
   Roots Dental Care — booking form + interactions
   Leads go to WhatsApp (opens chat, prefilled) AND to email (Web3Forms).
   Edit the CONFIG block below — nothing else needs changing.
   ========================================================================== */
(function () {
  "use strict";

  var CONFIG = {
    // WhatsApp number that receives leads, with country code, digits only.
    // 91 = India. Example: 7990376179  ->  "917990376179"
    whatsappNumber: "917990376179",

    // Email backup via Web3Forms (free, works on static hosting).
    // 1) Sign up at https://web3forms.com  2) paste your Access Key below.
    // Leave blank to skip email — WhatsApp will still work.
    web3formsKey: "",

    // Where the email lead should be labelled as coming from.
    emailSubject: "New website booking — Roots Dental Care",

    // ---- Analytics & Google Ads (for lead-gen campaigns) ----
    // Paste your IDs and tracking turns on automatically. Leave blank = off
    // (no scripts load, no broken requests).
    ga4Id: "",              // e.g. "G-XXXXXXXXXX"  (Google Analytics 4)
    googleAdsId: "",        // e.g. "AW-XXXXXXXXXX" (Google Ads tag)
    metaPixelId: "",        // e.g. "1234567890"    (optional, Meta/Facebook)
    // The conversion action to fire when someone submits the form / taps
    // WhatsApp / calls. From Google Ads: "AW-XXXXXXXXXX/AbCdEf_gHi".
    googleAdsConversion: ""
  };

  // Inject GA4 / Google Ads / Meta only when an ID is set.
  function loadAnalytics() {
    if (CONFIG.ga4Id || CONFIG.googleAdsId) {
      var id = CONFIG.ga4Id || CONFIG.googleAdsId;
      var s = document.createElement("script");
      s.async = true;
      s.src = "https://www.googletagmanager.com/gtag/js?id=" + id;
      document.head.appendChild(s);
      window.dataLayer = window.dataLayer || [];
      window.gtag = function () { window.dataLayer.push(arguments); };
      window.gtag("js", new Date());
      if (CONFIG.ga4Id) window.gtag("config", CONFIG.ga4Id);
      if (CONFIG.googleAdsId) window.gtag("config", CONFIG.googleAdsId);
    }
    if (CONFIG.metaPixelId) {
      /* eslint-disable */
      !function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?
      n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;
      n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;
      t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window,
      document,'script','https://connect.facebook.net/en_US/fbevents.js');
      window.fbq('init', CONFIG.metaPixelId); window.fbq('track', 'PageView');
      /* eslint-enable */
    }
  }

  function $(sel, ctx) { return (ctx || document).querySelector(sel); }

  // Fire analytics events if GA4 / Meta Pixel are present (added later).
  function track(name) {
    try { if (window.gtag) window.gtag("event", name); } catch (e) {}
    try { if (window.fbq) window.fbq("trackCustom", name); } catch (e) {}
    // Count a Google Ads conversion for real lead actions.
    var isLead = (name === "lead_submit" || name === "whatsapp_click" || name === "call_click");
    try {
      if (isLead && window.gtag && CONFIG.googleAdsConversion) {
        window.gtag("event", "conversion", { send_to: CONFIG.googleAdsConversion });
      }
    } catch (e) {}
    try { if (isLead && window.fbq) window.fbq("track", "Lead"); } catch (e) {}
  }

  function buildMessage(data) {
    return (
      "Hi Roots Dental Care, I'd like to book a visit.\n\n" +
      "Name: " + data.name + "\n" +
      "Phone: " + data.phone + "\n" +
      "For: " + data.treatment + "\n" +
      "Preferred time: " + data.time
    );
  }

  function sendEmail(data) {
    if (!CONFIG.web3formsKey) return; // email skipped until key is set
    try {
      fetch("https://api.web3forms.com/submit", {
        method: "POST",
        headers: { "Content-Type": "application/json", Accept: "application/json" },
        body: JSON.stringify({
          access_key: CONFIG.web3formsKey,
          subject: CONFIG.emailSubject,
          from_name: "Roots Dental Care Website",
          name: data.name,
          phone: data.phone,
          treatment: data.treatment,
          preferred_time: data.time
        })
      });
    } catch (e) { /* non-blocking */ }
  }

  // Works for BOTH the popup form and the inline fallback form (fields by name).
  function handleSubmit(e) {
    e.preventDefault();
    var form = e.currentTarget;
    var name = form.querySelector('[name="name"]');
    var phone = form.querySelector('[name="phone"]');

    var digits = (phone.value || "").replace(/\D/g, "");
    var ok = true;
    if (!name.value.trim()) { name.classList.add("invalid"); ok = false; } else { name.classList.remove("invalid"); }
    if (digits.length < 10) { phone.classList.add("invalid"); ok = false; } else { phone.classList.remove("invalid"); }
    if (!ok) { (name.value.trim() ? phone : name).focus(); return; }

    var tEl = form.querySelector('[name="treatment"]'), timeEl = form.querySelector('[name="time"]');
    var data = {
      name: name.value.trim(),
      phone: digits,
      treatment: (tEl && tEl.value) || "General enquiry",
      time: (timeEl && timeEl.value) || "Any time"
    };

    sendEmail(data);
    track("lead_submit");

    var okBox = form.parentNode.querySelector(".form-ok");
    if (okBox) okBox.style.display = "block";

    var url = "https://wa.me/" + CONFIG.whatsappNumber + "?text=" + encodeURIComponent(buildMessage(data));
    window.open(url, "_blank");
  }

  // Track taps on any WhatsApp / call button too.
  function wireCtaTracking() {
    document.querySelectorAll('a[href^="https://wa.me/"], a[data-wa]').forEach(function (a) {
      a.addEventListener("click", function () { track("whatsapp_click"); });
    });
    document.querySelectorAll('a[href^="tel:"]').forEach(function (a) {
      a.addEventListener("click", function () { track("call_click"); });
    });
  }

  function wireMenu() {
    var btn = $("#menu-btn"), links = $("#nav-links");
    if (!btn || !links) return;
    btn.addEventListener("click", function () { links.classList.toggle("open"); });
    links.querySelectorAll("a").forEach(function (a) {
      a.addEventListener("click", function () { links.classList.remove("open"); });
    });
  }

  function wireReveal() {
    var els = document.querySelectorAll(".reveal");
    if (!("IntersectionObserver" in window) || !els.length) {
      els.forEach(function (el) { el.classList.add("in"); });
      return;
    }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); }
      });
    }, { threshold: 0.12 });
    els.forEach(function (el) { io.observe(el); });
  }

  function buildWhatsappLinks() {
    // Point every "Book on WhatsApp" link (without a form) straight to chat.
    var base = "https://wa.me/" + CONFIG.whatsappNumber +
      "?text=" + encodeURIComponent("Hi Roots Dental Care, I'd like to book a visit.");
    document.querySelectorAll("a[data-wa]").forEach(function (a) { a.setAttribute("href", base); });
  }

  // Booking bottom sheet: opens on any [data-open-book] click and once on scroll.
  function wireSheet() {
    var sheet = $("#booking"), backdrop = $("#sheet-backdrop"), closeBtn = $("#sheet-close");
    if (!sheet || !backdrop) return;
    sheet.removeAttribute("hidden");
    backdrop.removeAttribute("hidden");
    var touched = false, autoDone = false;

    function open() {
      touched = true;
      backdrop.classList.add("open");
      sheet.classList.add("open");
      document.body.classList.add("sheet-lock");
      track("book_open");
      setTimeout(function () { var n = $("#f-name"); if (n) n.focus({ preventScroll: true }); }, 320);
    }
    function close() {
      backdrop.classList.remove("open");
      sheet.classList.remove("open");
      document.body.classList.remove("sheet-lock");
    }

    document.querySelectorAll("[data-open-book]").forEach(function (a) {
      a.addEventListener("click", function (e) {
        e.preventDefault();
        var opened = false;
        try { open(); opened = sheet.classList.contains("open"); } catch (_) { opened = false; }
        // Fallback: if the popup can't open, scroll to the inline form instead.
        if (!opened) scrollToInlineForm();
      });
    });
    if (closeBtn) closeBtn.addEventListener("click", close);
    backdrop.addEventListener("click", close);
    document.addEventListener("keydown", function (e) { if (e.key === "Escape") close(); });

    // Slide up once, on its own, after the visitor scrolls past the hero.
    window.addEventListener("scroll", function () {
      if (autoDone || touched) return;
      if (window.scrollY > window.innerHeight * 0.9) { autoDone = true; open(); }
    }, { passive: true });
  }

  // Scroll the visitor to the always-present inline booking form.
  function scrollToInlineForm() {
    var inline = document.getElementById("book-inline");
    if (!inline) return;
    inline.scrollIntoView({ behavior: "smooth", block: "start" });
    var n = inline.querySelector('[name="name"]');
    if (n) setTimeout(function () { try { n.focus({ preventScroll: true }); } catch (_) {} }, 500);
  }

  document.addEventListener("DOMContentLoaded", function () {
    loadAnalytics();
    document.querySelectorAll(".booking-form").forEach(function (f) {
      f.addEventListener("submit", handleSubmit);
    });
    buildWhatsappLinks();
    wireCtaTracking();
    wireMenu();
    wireReveal();
    wireSheet();
    var y = $("#year"); if (y) y.textContent = new Date().getFullYear();
  });
})();
