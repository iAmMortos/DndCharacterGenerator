import ui

with open('test_html.html') as f:
  html = f.read()
v = ui.WebView()
v.load_html(html)
v.present()
