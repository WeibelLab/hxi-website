/**
 * Two-axis project filtering for the research page.
 *
 * The Wowchemy portfolio widget supports one filter toolbar, and each click
 * replaces the whole Isotope filter, so a second toolbar cannot narrow the
 * first. This script adds combination filtering:
 *
 *   - Selections from each axis are intersected into one compound selector
 *     (e.g. ".js-id-HealthCare.js-id-XR").
 *   - The compound filter is applied to EVERY portfolio Isotope instance on the
 *     page, so it spans both the current and the earlier projects sections.
 *
 * The widget renders these toolbars under .hxi-filter-axes, deliberately not
 * .project-filters, so the theme's own single-group handler does not bind to
 * them and fight this one. The existing Isotope instances are reached through
 * Isotope.data(), since the theme keeps them in a closure.
 */
(function () {
  function init() {
    var toolbar = document.querySelector('.hxi-filter-axes');
    if (!toolbar || typeof Isotope === 'undefined') return;

    var axes = Array.prototype.slice.call(toolbar.querySelectorAll('.hxi-filter-axis'));
    if (!axes.length) return;

    var containers = Array.prototype.slice.call(
      document.querySelectorAll('.projects-container')
    );
    if (!containers.length) return;

    function selectorFor() {
      var parts = axes
        .map(function (axis) {
          var active = axis.querySelector('a.active');
          var f = active ? active.getAttribute('data-filter') : '*';
          return f === '*' ? null : f;
        })
        .filter(Boolean);
      return parts.length ? parts.join('') : '*';
    }

    function noteFor(container) {
      var note = container.parentNode.querySelector('.hxi-empty-note');
      if (!note) {
        note = document.createElement('p');
        note.className = 'hxi-empty-note';
        note.textContent = 'No projects match this combination.';
        container.parentNode.insertBefore(note, container.nextSibling);
      }
      return note;
    }

    function apply() {
      var selector = selectorFor();

      containers.forEach(function (c) {
        var iso = Isotope.data(c);
        if (iso) iso.arrange({filter: selector});
      });

      // An empty section must never be hidden outright: the filter toolbars sit
      // inside the first section, so hiding it would take the controls away and
      // leave no way back to a non-empty combination. Instead the heading stays
      // and the grid is replaced by a short note.
      containers.forEach(function (c) {
        var matches = Array.prototype.slice
          .call(c.querySelectorAll('.isotope-item'))
          .filter(function (el) {
            return selector === '*' || el.matches(selector);
          });
        noteFor(c).style.display = matches.length ? 'none' : '';
      });
    }

    axes.forEach(function (axis) {
      axis.querySelectorAll('a').forEach(function (button) {
        button.addEventListener('click', function (e) {
          e.preventDefault();
          axis.querySelectorAll('a').forEach(function (sibling) {
            sibling.classList.remove('active');
          });
          button.classList.add('active');
          apply();
        });
      });
    });

    // Isotope is created after its images load, so wait for it to exist.
    var tries = 0;
    (function waitForIsotope() {
      if (containers.every(function (c) { return Isotope.data(c); })) return;
      if (++tries > 100) return;
      setTimeout(waitForIsotope, 100);
    })();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
