/* Shows, hides and dismisses the bar rendered by
   layouts/partials/site_footer.html.

   The markup lives in the template so Hugo owns the copyright string and the
   contact address. This file only decides when the bar is on screen. */
(function () {
  var KEY = 'hxi-support-dismissed';

  function dismissed() {
    try { return sessionStorage.getItem(KEY) === '1'; } catch (e) { return false; }
  }

  document.addEventListener('DOMContentLoaded', function () {
    var bar = document.getElementById('hxi-sticky-support');
    if (!bar || dismissed()) return;

    bar.hidden = false;

    bar.querySelector('.hxi-sticky-close').addEventListener('click', function () {
      bar.classList.remove('is-visible');
      try { sessionStorage.setItem(KEY, '1'); } catch (e) { /* private mode */ }
    });

    function onScroll() {
      if (dismissed()) return;
      bar.classList.toggle('is-visible', window.scrollY > window.innerHeight * 0.6);
    }

    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  });
})();
