from xml.etree import ElementTree as ET
import test_context
from PyQt5.QtWidgets import QApplication, QLabel


def main():
  with open('data/xml/characters/Melodias.xml') as f:
    xmlstr = f.read()
  root = ET.fromstring(xmlstr)
  img_data = root.find('imageData').find('encoded').text
  with open('test_img.png', 'wb') as f:
    f.write(img_data.decode('base64'))

  app = QApplication([])
  label = QLabel('Hello World!')
  label.show()
  app.exec_()


if __name__ == '__main__':
  main()
