(function () {
  var active = false;
  var originalHTML = null;

  function toggleSeats() {
    var panel = document.getElementById('info-panel');
    if (!panel) return;

    if (!active) {
      originalHTML = panel.innerHTML;
      panel.innerHTML =
        '<div style="display:flex;gap:6px;height:100%;">' +
          '<iframe src="http://127.0.0.1:5999/conv_a?format=html" ' +
            'style="flex:1;border:1px solid #ddd;border-radius:3px;"></iframe>' +
          '<iframe src="http://127.0.0.1:5999/conv_b?format=html" ' +
            'style="flex:1;border:1px solid #ddd;border-radius:3px;"></iframe>' +
        '</div>';
      active = true;
    } else {
      if (originalHTML !== null) {
        panel.innerHTML = originalHTML;
      }
      active = false;
    }
  }

  window.addEventListener('DOMContentLoaded', function () {
    var btn = document.getElementById('seatsTestBtn');
    if (btn) btn.addEventListener('click', toggleSeats);
  });
})();
