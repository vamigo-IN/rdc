with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

modal_html = """
<div id="navratri-modal" class="modal-backdrop">
  <div class="modal-content">
    <button class="modal-close" onclick="document.getElementById('navratri-modal').style.display='none'">✕</button>
    <h3>Navratri Special Offer!</h3>
    <p>Get <strong>25% off</strong> on all treatment services this festive season.</p>
    <a href="#book-inline" class="btn btn-red" onclick="document.getElementById('navratri-modal').style.display='none'" data-open-book>Claim Offer</a>
  </div>
</div>
<script>
  document.addEventListener("DOMContentLoaded", function() {
    if (!sessionStorage.getItem('navratri_seen')) {
      document.getElementById('navratri-modal').style.display = 'flex';
      sessionStorage.setItem('navratri_seen', 'true');
    } else {
      document.getElementById('navratri-modal').style.display = 'none';
    }
  });
</script>
</body>"""

html = html.replace('</body>', modal_html)
html = html.replace('2000+', '20000+')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Modal added to index.html")
