
import xml.etree.ElementTree as ET


class DataLoader (object):
  def __init__(self, file):
    tree = ET.parse(file)
    root = tree.getroot()
    self.data = {}
    for c in root.getchildren():
      t = c.tag
      if t not in self.data:
        self.data[t] = [c]
      else:
        self.data[t] += [c]
        
  def print_stats(self):
    for k in self.data:
      print('%s: %s item(s)' % (k, len(self.data[k])))
