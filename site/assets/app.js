// ===== Theme toggle =====
(function () {
  var root = document.documentElement;
  var KEY = 'knjige-theme';
  function apply(t) {
    if (t === 'dark' || t === 'light') root.setAttribute('data-theme', t);
    else root.removeAttribute('data-theme');
  }
  var saved = null;
  try { saved = localStorage.getItem(KEY); } catch (e) {}
  if (saved) apply(saved);

  window.toggleTheme = function () {
    var cur = root.getAttribute('data-theme');
    if (!cur) {
      var prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
      cur = prefersDark ? 'dark' : 'light';
    }
    var next = cur === 'dark' ? 'light' : 'dark';
    apply(next);
    try { localStorage.setItem(KEY, next); } catch (e) {}
  };
})();

// ===== Sidebar (mobile) + collapsible book groups =====
document.addEventListener('DOMContentLoaded', function () {
  var sidebar = document.getElementById('sidebar');
  var backdrop = document.getElementById('backdrop');
  var menuBtn = document.getElementById('menuBtn');

  function closeSidebar() {
    if (!sidebar) return;
    sidebar.classList.remove('open');
    if (backdrop) backdrop.classList.remove('show');
    document.body.classList.remove('no-scroll');
  }
  function openSidebar() {
    if (!sidebar) return;
    sidebar.classList.add('open');
    if (backdrop) backdrop.classList.add('show');
    document.body.classList.add('no-scroll');
  }
  if (menuBtn) menuBtn.addEventListener('click', function () {
    sidebar.classList.contains('open') ? closeSidebar() : openSidebar();
  });
  if (backdrop) backdrop.addEventListener('click', closeSidebar);

  // Collapse / expand book groups
  document.querySelectorAll('.nav-book').forEach(function (btn) {
    btn.addEventListener('click', function () {
      btn.closest('.nav-group').classList.toggle('collapsed');
    });
  });

  // Scroll active chapter into view inside sidebar
  var active = document.querySelector('.chapters a.active');
  if (active && sidebar) {
    var r = active.getBoundingClientRect();
    if (r.top < 120 || r.top > window.innerHeight - 120) {
      active.scrollIntoView({ block: 'center' });
    }
  }

  // ===== Wrap tables for horizontal scroll =====
  document.querySelectorAll('.article table').forEach(function (t) {
    if (t.parentElement && t.parentElement.classList.contains('table-scroll')) return;
    var w = document.createElement('div');
    w.className = 'table-scroll';
    t.parentNode.insertBefore(w, t);
    w.appendChild(t);
  });

  // ===== TOC scroll-spy =====
  var tocLinks = Array.prototype.slice.call(document.querySelectorAll('.toc a'));
  if (tocLinks.length) {
    var map = {};
    var targets = [];
    tocLinks.forEach(function (a) {
      var id = decodeURIComponent((a.getAttribute('href') || '').replace(/^#/, ''));
      var el = document.getElementById(id);
      if (el) { map[id] = a; targets.push(el); }
    });
    var obs = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) {
          tocLinks.forEach(function (l) { l.classList.remove('active'); });
          var a = map[e.target.id];
          if (a) a.classList.add('active');
        }
      });
    }, { rootMargin: '-70px 0px -70% 0px', threshold: 0 });
    targets.forEach(function (t) { obs.observe(t); });
  }
});
