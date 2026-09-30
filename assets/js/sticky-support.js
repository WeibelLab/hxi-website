/* Shows and hides the bar rendered by layouts/partials/site_footer.html.

   The markup lives in the template so Hugo owns the copyright string and the
   contact address. This file only decides when the bar is on screen: it stays
   hidden over the hero and slides up once the reader is past the first screen.
   There is no dismiss, so the giving link stays reachable for the whole visit. */
(function () {
  document.addEventListener('DOMContentLoaded', function () {
    var bar = document.getElementById('hxi-sticky-support');
    if (!bar) return;

    bar.hidden = false;

    function onScroll() {
      bar.classList.toggle('is-visible', window.scrollY > window.innerHeight * 0.6);
    }

    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  });
})();
