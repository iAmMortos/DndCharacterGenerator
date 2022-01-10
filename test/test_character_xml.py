
import test_context
from xml.etree import ElementTree as ET


def main():
  tree = ET.parse('data/xml/characters/Melodias.xml')
  root = tree.getroot()
  for child in root:
    if child.tag == "imageData":
      for c in child:
        if c.tag == 'encoded':
          s = c.text
          print(s)



if __name__ == '__main__':
  main()
