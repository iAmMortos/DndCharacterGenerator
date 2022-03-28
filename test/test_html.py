import test_context
from model.data_loader import DataLoader
# import webbrowser
import os
import io
import ui
from htmlutils.html_generator import HtmlGenerator
import urllib.parse
import random


def main():
  dl = DataLoader('Complete')
  # monster = random.choice(dl.monsters)
  monster = dl.get_monster('Arasta')
  hg = HtmlGenerator()
  htmlstr = hg.gen_stat_block(monster)
  page_html = hg.gen_html_page(monster.name, 'templates/css/statblock.css', htmlstr)

  with io.open('views/html/index.html', 'w', encoding='utf-8') as f:
    f.write(page_html)

  abspath = os.path.abspath('views/html/index.html')
  abspath = abspath.replace('\\', '/')
  url = 'file://{}'.format(urllib.parse.quote(abspath))
  w = ui.WebView()
  w.load_url(url)
  # w.load_html(page_html)
  w.present(style='fullscreen', hide_title_bar=True)


if __name__ == '__main__':
  main()
