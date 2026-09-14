/**
 * Randomize the order of the homepage slider images on each page load.
 *
 * The Wowchemy slider widget renders a Bootstrap carousel with a fixed slide
 * order taken from content/home/slider.md. Shuffling at build time would only
 * reorder once per deploy, so this runs in the browser instead and gives each
 * visitor a different order.
 *
 * It reorders the .carousel-item elements, moves the "active" class to the new
 * first slide, and rebuilds the indicator list to match. Runs before the
 * carousel is cycled, so Bootstrap picks up the new order on its own.
 */
(function () {
  function shuffleSlider() {
    var slider = document.getElementById('slider');
    if (!slider) return;

    var inner = slider.querySelector('.carousel-inner');
    if (!inner) return;

    var slides = Array.prototype.slice.call(inner.querySelectorAll('.carousel-item'));
    if (slides.length < 2) return;

    // Fisher-Yates
    for (var i = slides.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1));
      var tmp = slides[i];
      slides[i] = slides[j];
      slides[j] = tmp;
    }

    slides.forEach(function (slide, index) {
      slide.classList.toggle('active', index === 0);
      inner.appendChild(slide);
    });

    var indicators = slider.querySelector('.carousel-indicators');
    if (indicators) {
      var dots = Array.prototype.slice.call(indicators.querySelectorAll('li'));
      dots.forEach(function (dot, index) {
        dot.setAttribute('data-slide-to', String(index));
        dot.classList.toggle('active', index === 0);
      });
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', shuffleSlider);
  } else {
    shuffleSlider();
  }
})();
