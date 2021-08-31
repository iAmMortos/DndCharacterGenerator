
import xml.etree.ElementTree as ET

from model.background import Background
from model.char_class import CharClass
from model.feat import Feat
from model.item import Item
from model.monster import Monster
from model.race import Race
from model.spell import Spell


class DataLoader (object):
  def __init__(self, file):
    self.backgrounds = []
    self.classes = []
    self.feats = []
    self.items = []
    self.monsters = {}
    self.races = []
    self.spells = []

    tree = ET.parse(file)
    root = tree.getroot()
    for c in list(root):
      t = c.tag
      if t == 'background':
        self.backgrounds += [Background(c)]
      elif t == 'class':
        self.classes += [CharClass(c)]
      elif t == 'feat':
        self.feats += [Feat(c)]
      elif t == 'item':
        self.items += [Item(c)]
      elif t == 'monster':
        m = Monster(c)
        self.monsters[m.name] = m
      elif t == 'race':
        self.races += [Race(c)]
      elif t == 'spell':
        self.spells += [Spell(c)]

  def print_stats(self):
    print("Backgrounds: %s item(s)" % len(self.backgrounds))
    print("Classes: %s item(s)" % len(self.classes))
    print("Feats: %s item(s)" % len(self.feats))
    print("Items: %s item(s)" % len(self.items))
    print("Monsters: %s item(s)" % len(self.monsters))
    print("Races: %s item(s)" % len(self.races))
    print("Spells: %s item(s)" % len(self.spells))
