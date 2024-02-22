import base64
from ui import WebView
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
  
  sheet.items = random.sample(dl.items, 9)
  # sheet.items = [dl.get_item('Korolnor Scepter')]
  for item in sheet.items:
    if item.text and type(item.text) is str:
      item.text = item.text.replace('\n', '</p>\n<p>')
      item.text = item.text.replace('\xa0', '&nbsp;')
      item.text = item.text.replace('•', '&#x2022;')
    setattr(item, "item_img_b64", str(item_img)[2:-1])
  # print(dl.get_item('Iron Flask'))
  
  sheet.css = '''html, body
{
  padding: 0;
  margin: 0;
}

.guide
{
  background-color: red;
  position: absolute;
}

.hguide
{
  width: 100%;
  height: 1px;
  left: 0;
}

.vguide
{
  width: 1px;
  height: 100%;
  top: 0;
}

.hguide0{ top: 2.2727%; }
.hguide1{ top: 34.0909%; }
.hguide2{ top: 65.9091%; }
.hguide3{ top: 97.7273%; }
.vguide0{ left: 5.8824%; }
.vguide1{ left: 35.2941%; }
.vguide2{ left: 64.7059%; }
.vguide3{ left: 94.1176%; }

.page
{
  position: relative;
  /* width: 2250px;
  height: 3150px;
  padding: 75px 150px; */
  float: left;
  margin: 10px;
  width: 600px;
  height: 840px;
  padding: 20px 40px;
  border: 1px solid black;
}

.card
{
  position: relative;
  float: left;
  width: 33.33333%;
  height: 33.33333%;
  /* background-color: red; */
  border: 1px #ccc solid;
  margin: 0px;
  padding: 6px;
  box-sizing: border-box;
  overflow: hidden;
}

.card-back
{
  float: right;
  background-image: url("data:image/png;base64,''' + str(back_img)[2:-1] + '''");
  background-size: 100% 100%;
}

.card h1
{
  font-size: 8pt;
  color: #600;
  font-weight: bold;
  margin: 0;
}

.card h6
{
  font-size: 6pt;
  color: #999;
  font-style: italic;
  margin: 0;
}

.card p
{
  font-size: 6pt;
  color: black;
  margin: 0px;
  text-indent: 8px;
}

.card .bg_img
{
  opacity: .3;
  width: 100%;
  z-index: -900;
  position: absolute;
  bottom: 0;
}
'''
  sheet.js = '''function printDiv(divId)
{
	var printContents = document.getElementById(divId).innerHTML;
  var originalContents = document.body.innerHTML;
  
  document.body.innerHTML = printContents;
  window.print();
  document.body.innerHTML = originalContents;
}'''

  html = tmpltr.make(sheet, 'item_cards')
  with io.open('test/cards.html', 'w', encoding="utf-8") as f:
    f.write(html)
  url = 'file:/' + os.path.realpath('test/cards.html')
  url = url.replace(' ', '%20')
  # print(url)
  webbrowser.open(url)
  # show_html(html)
  # print(html)
  

def show_html(html):
  wv = WebView()
  wv.load_html(html)
  wv.present()
  
  
if __name__ == '__main__':
  main()

