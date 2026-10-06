with open('assets/js/main.js', 'r', encoding='utf-8') as f:
    js = f.read()

counter_code = """
  // Counter animation
  function wireCounters() {
    var counters = document.querySelectorAll(".counter");
    if (!("IntersectionObserver" in window) || !counters.length) return;
    
    var observer = new IntersectionObserver(function(entries) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting) {
          var el = entry.target;
          var target = parseInt(el.getAttribute("data-target"), 10);
          var duration = 2000; // 2 seconds
          var stepTime = Math.max(duration / target, 20); // ms per frame
          if (stepTime > 20) {
            // For small numbers like 4
            var current = 0;
            var timer = setInterval(function() {
              current++;
              el.textContent = current;
              if (current >= target) {
                el.textContent = target.toLocaleString();
                clearInterval(timer);
              }
            }, stepTime);
          } else {
            // For large numbers
            var steps = duration / 20;
            var increment = target / steps;
            var current = 0;
            var timer = setInterval(function() {
              current += increment;
              if (current >= target) {
                el.textContent = target.toLocaleString();
                clearInterval(timer);
              } else {
                el.textContent = Math.ceil(current).toLocaleString();
              }
            }, 20);
          }
          observer.unobserve(el);
        }
      });
    }, { threshold: 0.1 });
    
    counters.forEach(function(c) { observer.observe(c); });
  }
"""

# Inject wireCounters() call inside DOMContentLoaded
js = js.replace('wireReveal();', 'wireReveal();\n    wireCounters();')
# Inject function definition at the end
js += counter_code

with open('assets/js/main.js', 'w', encoding='utf-8') as f:
    f.write(js)
