import re

with open('assets/js/main.js', 'r') as f:
    js = f.read()

ba_js = """
  // Before & After Slider Logic
  function wireBeforeAfterSlider() {
    var slider = document.getElementById("ba-slider");
    if (!slider) return;
    var handle = document.getElementById("ba-handle");
    var beforeImg = document.getElementById("ba-before");
    var isDown = false;

    function updateSlider(e) {
      if (!isDown) return;
      var rect = slider.getBoundingClientRect();
      var x = (e.touches ? e.touches[0].clientX : e.clientX) - rect.left;
      var percent = Math.max(0, Math.min(100, (x / rect.width) * 100));
      handle.style.left = percent + "%";
      beforeImg.style.clipPath = "inset(0 " + (100 - percent) + "% 0 0)";
    }

    slider.addEventListener("mousedown", function(e) { isDown = true; updateSlider(e); });
    window.addEventListener("mouseup", function() { isDown = false; });
    window.addEventListener("mousemove", updateSlider);
    
    // Touch support
    slider.addEventListener("touchstart", function(e) { isDown = true; updateSlider(e); }, {passive: true});
    window.addEventListener("touchend", function() { isDown = false; });
    window.addEventListener("touchmove", function(e) { 
      if (!isDown) return;
      // prevent vertical scroll only when sliding horizontally
      var rect = slider.getBoundingClientRect();
      var x = e.touches[0].clientX - rect.left;
      if (x > 0 && x < rect.width) e.preventDefault(); 
      updateSlider(e); 
    }, {passive: false});
  }

  document.addEventListener("DOMContentLoaded", function () {"""

js = js.replace('  document.addEventListener("DOMContentLoaded", function () {', ba_js)
js = js.replace('wireSheet();', 'wireSheet();\n    wireBeforeAfterSlider();')

with open('assets/js/main.js', 'w') as f:
    f.write(js)
