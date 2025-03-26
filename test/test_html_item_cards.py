import base64
# from ui import WebView
import random
import webbrowser
import os
import io

import test_context
from model.data_loader import DataLoader
from templater.templater import Templater


class ItemSheet (object):
  pass


def main():
  dl = DataLoader('Complete')
  tmpltr = Templater('html')
  
  sheet = ItemSheet()
  with open("test/card_back.png", "rb") as image_file:
    back_img = base64.b64encode(image_file.read())
  with open('test/rod.JPEG', 'rb') as image_file:
    item_img = base64.b64encode(image_file.read())
#  print(item_img)
#  return
  
  sheet.items = random.sample(dl.items, 7)
  # sheet.items = [dl.get_item('Korolnor Scepter')]
  for item in sheet.items:
    if item.text and type(item.text) is str:
      item.text = item.text.replace('\n', '</p>\n<p>')
      item.text = item.text.replace('\xa0', '&nbsp;')
      item.text = item.text.replace('•', '&#x2022;')
    setattr(item, "item_img_b64", str(item_img)[2:-1])
  sheet.card_back_data = str(back_img)[2:-1]
  # print(dl.get_item('Iron Flask'))
  
  sheet.css = '''
  '''
  sheet.js = '''
  '''

  html = tmpltr.make(sheet, 'item_cards')
  with io.open('test/cards.html', 'w', encoding="utf-8") as f:
    f.write(html)
  url = 'file:/' + os.path.realpath('test/cards.html')
  url = url.replace(' ', '%20')
  # print(url)
  webbrowser.open(url)
  # show_html(html)
  # print(html)
  

# def show_html(html):
#   wv = WebView()
#   wv.load_html(html)
#   wv.present()
  
  
if __name__ == '__main__':
  main()

