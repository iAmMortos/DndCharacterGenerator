import test_context
from model.data_loader import DataLoader
import webbrowser
import os
import io
from html.html_generator import HtmlGenerator


def main():
  dl = DataLoader('Complete')
  monster = dl.get_monster('Juiblex')
  hg = HtmlGenerator()
  html = hg.gen_stat_block(monster)
  page_html = hg.gen_html_page(monster.name, 'templates/css/statblock.css', html)

  with io.open('views/html/index.html', 'w', encoding='utf-8') as f:
    f.write(page_html)

  abspath = os.path.abspath('views/html/index.html')
  abspath = abspath.replace('\\', '/')
  url = 'file:///{}'.format(abspath)
  webbrowser.open_new_tab(url)


if __name__ == '__main__':
  main()
