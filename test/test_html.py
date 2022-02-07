import test_context
from model.data_loader import DataLoader
from utils.regexes import is_attack, get_attack
from xml.etree import ElementTree as ET
import webbrowser
import os
import io
import re
import random
from html.html_generator import HtmlGenerator


def main():
  dl = DataLoader('Complete')
  monster = dl.get_monster('Tromokratis')
  hg = HtmlGenerator()
  html = hg.gen_stat_block(monster)

  with io.open('views/html/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

  abspath = os.path.abspath('views/html/index.html')
  abspath = abspath.replace('\\', '/')
  url = 'file:///{}'.format(abspath)
  webbrowser.open_new_tab(url)


if __name__ == '__main__':
  main()
