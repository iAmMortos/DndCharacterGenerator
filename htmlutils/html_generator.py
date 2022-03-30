
from htmlutils.stat_block_gen import gen_stat_block
import io
import os


class HtmlGenerator(object):
  def __init__(self):
    pass

  def gen_stat_block(self, monster):
    return gen_stat_block(monster)

  def gen_spell_block(self, spell):
    pass

  def gen_html_page(self, title, styleref, content_html):
    with open('views/html/templates/boilerplate.html') as f:
      html = f.read()
    html = html.replace('{title}', title)
    html = html.replace('{stylesheet-path}', styleref)
    # with io.open(os.path.abspath(styleref), encoding='utf-8') as f:
    #   css = f.read()
    #   html = html.replace('{stylesheet-body}', css)
    html = html.replace('{body}', content_html)
    return html


