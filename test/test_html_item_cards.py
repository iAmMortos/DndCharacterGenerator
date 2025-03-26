import base64
# from ui import WebView
import random
import webbrowser
import os
import io

import test_context
from model.data_loader import DataLoader
from templater.templater import Templater

from utils import objc_utils


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
  @page {
            size: 8.5in 11in;
            margin: 0.5in;
        }
        
        body {
            font-family: Arial, sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            margin: 0;
            padding: 0;
        }

        .print-button {
            margin: 10px;
            padding: 10px 15px;
            font-size: 16px;
            cursor: pointer;
        }

        .card-container {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 0.5in;
            width: 7.5in;
            margin: 0 auto;
        }

        .card {
            width: 2.5in;
            height: 3.5in;
            border: 1px solid black;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            font-size: 14px;
            background: white;
        }
        
        @media print {
            .print-button { display: none; }
            body { justify-content: flex-start; }
        }
  '''
  sheet.js = '''
  '''

  html = tmpltr.make(sheet, 'item_cards')
  # bjc_utils.print_html(html)
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

