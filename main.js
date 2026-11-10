(function () {
  var root = document.documentElement;

  /* ---------- theme ---------- */
  function store(key, val) {
    try { if (val === undefined) return localStorage.getItem(key); localStorage.setItem(key, val); } catch (e) { return null; }
  }
  var mq = window.matchMedia ? window.matchMedia("(prefers-color-scheme: light)") : null;
  function activeTheme() {
    var t = root.getAttribute("data-theme");
    if (t === "light" || t === "dark") return t;
    return mq && mq.matches ? "light" : "dark";
  }
  function paint() {
    var t = activeTheme();
    root.setAttribute("data-active-theme", t);
    document.querySelectorAll(".theme-toggle").forEach(function (b) {
      b.setAttribute("aria-label", t === "dark" ? "Switch to light theme" : "Switch to dark theme");
      b.setAttribute("title", t === "dark" ? "Light theme" : "Dark theme");
    });
  }
  paint();
  if (mq && mq.addEventListener) mq.addEventListener("change", paint);
  document.querySelectorAll(".theme-toggle").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var next = activeTheme() === "dark" ? "light" : "dark";
      root.setAttribute("data-theme", next);
      store("zevoro-theme", next);
      paint();
    });
  });

  /* ---------- mobile nav ---------- */
  var header = document.querySelector(".site-header");
  var menuBtn = document.querySelector(".menu-btn");
  if (menuBtn && header) {
    menuBtn.addEventListener("click", function () {
      var open = header.classList.toggle("nav-open");
      menuBtn.setAttribute("aria-expanded", open ? "true" : "false");
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && header.classList.contains("nav-open")) {
        header.classList.remove("nav-open");
        menuBtn.setAttribute("aria-expanded", "false");
        menuBtn.focus();
      }
    });
  }

  /* ---------- year ---------- */
  document.querySelectorAll("[data-year]").forEach(function (el) { el.textContent = new Date().getFullYear(); });

  /* ---------- game filters ---------- */
  var filters = document.querySelectorAll(".filter");
  if (filters.length) {
    var cards = document.querySelectorAll("[data-genre]");
    var empty = document.querySelector(".empty-note");
    filters.forEach(function (f) {
      f.addEventListener("click", function () {
        var g = f.getAttribute("data-filter");
        filters.forEach(function (x) { x.setAttribute("aria-pressed", x === f ? "true" : "false"); });
        var shown = 0;
        cards.forEach(function (c) {
          var match = g === "all" || c.getAttribute("data-genre").split(" ").indexOf(g) > -1;
          c.hidden = !match;
          if (match) shown++;
        });
        if (empty) empty.hidden = shown !== 0;
      });
    });
  }

  /* ---------- copy buttons ---------- */
  document.querySelectorAll("[data-copy]").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var text = btn.getAttribute("data-copy");
      function done() { var o = btn.textContent; btn.textContent = "Copied"; setTimeout(function () { btn.textContent = o; }, 1600); }
      function fallback() {
        var target = document.getElementById(btn.getAttribute("aria-controls"));
        if (!target) return;
        var r = document.createRange(); r.selectNodeContents(target);
        var s = window.getSelection(); s.removeAllRanges(); s.addRange(r);
      }
      try {
        navigator.clipboard.writeText(text).then(done, fallback);
      } catch (e) { fallback(); }
    });
  });

  /* ---------- contact form ---------- */
  var form = document.getElementById("contact-form");
  if (form) {
    var success = document.getElementById("form-success");
    function setErr(name, msg) {
      var field = form.querySelector('[data-field="' + name + '"]');
      if (!field) return;
      field.classList.toggle("invalid", !!msg);
      var e = field.querySelector(".err");
      if (e) e.textContent = msg || "";
    }
    form.addEventListener("submit", function (ev) {
      ev.preventDefault();
      var data = new FormData(form);
      var ok = true;
      var name = (data.get("name") || "").toString().trim();
      var email = (data.get("email") || "").toString().trim();
      var msg = (data.get("message") || "").toString().trim();
      setErr("name", name ? "" : "Add your name so we know who to reply to.");
      setErr("email", /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email) ? "" : "Enter an email like you@company.com.");
      setErr("message", msg.length >= 10 ? "" : "Tell us a little about the project (at least 10 characters).");
      if (!name || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email) || msg.length < 10) ok = false;
      if (!ok) { var first = form.querySelector(".invalid input, .invalid textarea"); if (first) first.focus(); return; }
      // TODO: connect to a form backend (Formspree, Netlify Forms, or your own API).
      form.hidden = true;
      if (success) {
        success.querySelector("[data-name]").textContent = name.split(" ")[0];
        success.hidden = false;
        success.focus();
      }
    });
    var again = document.getElementById("form-again");
    if (again) again.addEventListener("click", function () { form.reset(); form.hidden = false; success.hidden = true; });
  }
})();
