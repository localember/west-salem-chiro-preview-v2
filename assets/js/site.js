(function () {
  var sticky = document.querySelector(".sticky");
  if (sticky) {
    var toggle = function () {
      sticky.classList.toggle("is-on", window.scrollY > 420);
    };
    toggle();
    window.addEventListener("scroll", toggle, { passive: true });
  }

  document.querySelectorAll(".util__btn").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var item = btn.closest(".util__item");
      var open = item.classList.contains("is-open");
      document.querySelectorAll(".util__item.is-open").forEach(function (el) {
        el.classList.remove("is-open");
        var b = el.querySelector(".util__btn");
        if (b) b.setAttribute("aria-expanded", "false");
      });
      if (!open) {
        item.classList.add("is-open");
        btn.setAttribute("aria-expanded", "true");
      }
    });
  });
  document.addEventListener("click", function (e) {
    if (!e.target.closest(".util__item")) {
      document.querySelectorAll(".util__item.is-open").forEach(function (el) {
        el.classList.remove("is-open");
        var b = el.querySelector(".util__btn");
        if (b) b.setAttribute("aria-expanded", "false");
      });
    }
  });

  var toggleBtn = document.querySelector(".menu-toggle");
  var nav = document.querySelector(".nav");
  if (toggleBtn && nav) {
    toggleBtn.addEventListener("click", function () {
      var open = nav.classList.toggle("is-open");
      toggleBtn.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }

  document.querySelectorAll(".nav > li > button.nav__top").forEach(function (btn) {
    btn.addEventListener("click", function (e) {
      if (window.matchMedia("(max-width: 720px)").matches) {
        e.preventDefault();
        var li = btn.parentElement;
        var open = li.classList.contains("is-open");
        document.querySelectorAll(".nav > li.is-open").forEach(function (other) {
          if (other !== li) {
            other.classList.remove("is-open");
            var ob = other.querySelector("button.nav__top");
            if (ob) ob.setAttribute("aria-expanded", "false");
          }
        });
        li.classList.toggle("is-open", !open);
        btn.setAttribute("aria-expanded", !open ? "true" : "false");
      }
    });
  });

  var slides = Array.prototype.slice.call(document.querySelectorAll(".stories__slide"));
  var dots = Array.prototype.slice.call(document.querySelectorAll(".dots button"));
  if (slides.length && dots.length) {
    var show = function (i) {
      slides.forEach(function (s, n) { s.hidden = n !== i; });
      dots.forEach(function (d, n) {
        d.classList.toggle("is-on", n === i);
        d.setAttribute("aria-selected", n === i ? "true" : "false");
      });
    };
    dots.forEach(function (d, i) {
      d.addEventListener("click", function () { show(i); });
    });
    show(0);
  }

  var form = document.getElementById("request-form");
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var note = document.getElementById("form-preview-note");
      if (note) {
        note.hidden = false;
        note.focus();
      }
    });
  }
})();
