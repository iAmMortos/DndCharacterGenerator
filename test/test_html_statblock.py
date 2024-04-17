
from ui import WebView
import console
import test_context
from model.data_loader import DataLoader
from templater.templater import Templater
from utils import objc_utils


def main():
  # test_single_statblock()
  test_multi_statblock()

def test_multi_statblock():
  class BlockPageObj (object):
    pass
  dl = DataLoader("Complete")
  tmpltr = Templater("html")

  bpobj = BlockPageObj()
  bpobj.title="Monster Statblocks"
  with open('templater/templates/html/css/statblock.css') as f:
    bpobj.statblock_style = f.read()
  with open('templater/templates/html/css/statblock_page.css') as f:
    bpobj.page_style = f.read()
  bpobj.monsters = []
  bpobj.monsters.append(dl.get_monster("Goblin"))
  bpobj.monsters.append(dl.get_monster("Bugbear"))
  bpobj.monsters.append(dl.get_monster("Goblin Boss"))
  html = tmpltr.make(bpobj, "statblock_page")
  
  objc_utils.print_html(html)

  #  wv = WebView()
  #  wv.load_html(html)
  #  wv.present()
  
  
def test_single_statblock():
  dl = DataLoader("Complete")
  mon = dl.get_monster("Goblin")
  tmpltr = Templater("html")
  html = tmpltr.make(mon)
  
  wv = WebView()
  wv.load_html(html)
  wv.present()

if __name__ == '__main__':
  main()

