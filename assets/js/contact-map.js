/**
 * Multi-pin contact map.
 *
 * Wowchemy's contact widget renders exactly one marker: wowchemy.js reads the
 * hidden #map-lat / #map-lng inputs and does `L.marker([lat, lng]).addTo(map)`.
 * The lab occupies two buildings, so the widget override emits #hxi-map with a
 * JSON list of locations and this script draws them.
 *
 * The container is deliberately named #hxi-map: the theme only initialises its
 * own map when it finds #map, so using a different id keeps the two apart
 * rather than fighting over the same element.
 *
 * Locations come from site.Params.map.locations:
 *   - name, lat, lng, and an optional description
 */
(function () {
  function init() {
    var el = document.getElementById('hxi-map');
    if (!el || typeof L === 'undefined') return;

    var locations;
    try {
      locations = JSON.parse(el.getAttribute('data-locations') || '[]');
    } catch (e) {
      return;
    }
    if (!locations.length) return;

    // Leaflet resolves its default marker images against L.Icon.Default.imagePath,
    // which it derives from its own <script src>. That detection does not fire
    // here, so the icons resolve against the page URL and 404. Derive the path
    // from the Leaflet script tag the theme loads.
    if (!L.Icon.Default.imagePath) {
      var lscript = document.querySelector('script[src*="leaflet"]');
      if (lscript) {
        L.Icon.Default.imagePath = lscript.src.replace(/[^/]*$/, '') + 'images/';
      }
    }

    var zoom = parseInt(el.getAttribute('data-zoom'), 10) || 15;
    var map = L.map('hxi-map', {scrollWheelZoom: false});

    // OpenStreetMap standard tiles. CARTO's key-free raster endpoint now
    // returns tiles watermarked "API KEY REQUIRED", and OSM renders campus
    // building footprints, malls and walkways at this zoom. No key required;
    // attribution is required by the OSM tile usage policy.
    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
      maxZoom: 19,
      attribution:
        '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
    }).addTo(map);

    var points = [];
    locations.forEach(function (loc) {
      var lat = parseFloat(loc.lat);
      var lng = parseFloat(loc.lng);
      if (isNaN(lat) || isNaN(lng)) return;

      var parts = [];
      if (loc.name) parts.push('<strong>' + loc.name + '</strong>');
      if (loc.description) parts.push(loc.description);
      var directions =
        'https://www.google.com/maps/dir/?api=1&destination=' + lat + ',' + lng;
      parts.push('<a href="' + directions + '" target="_blank" rel="noopener">Directions</a>');

      L.marker([lat, lng]).addTo(map).bindPopup(parts.join('<br>'));
      points.push([lat, lng]);
    });

    if (points.length > 1) {
      // Frame both buildings rather than centring on one of them.
      map.fitBounds(L.latLngBounds(points), {padding: [45, 45], maxZoom: zoom});
    } else if (points.length === 1) {
      map.setView(points[0], zoom);
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
