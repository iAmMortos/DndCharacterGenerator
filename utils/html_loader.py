
html_path = 'views/html/'

def load_html_boilerplate(body):
  with open(html_path + 'boilerplate.html') as f:
    html = f.read()
  html = html.format(body)
  return html 
