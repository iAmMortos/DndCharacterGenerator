

from model.background import Background
from model.char_class import CharClass
from model.feat import Feat
from model.item import Item
from model.monster import Monster
from model.race import Race
from model.spell import Spell
from errors.no_such_entity_error import NoSuchEntityError
from util.data_file_loader import DataFileLoader as DFL


class DataLoader (object):
  def __init__(self, data_name):
    self.backgrounds = []
    self._bgs = {}
    self.classes = []
    self._cls = {}
    self.feats = []
    self._fts = {}
    self.items = []
    self._itms = {}
    self.monsters = []
    self._mnsts = {}
    self.races = []
    self._rcs = {}
    self.spells = []
    self._spls = {}

    root = DFL().load_compendium_xml(data_name)
    for c in list(root):
      t = c.tag
      if t == 'background':
        bg = Background(c)
        self.backgrounds += [bg]
        self._bgs[bg.name] = bg
      elif t == 'class':
        cls = CharClass(c)
        self.classes += [cls]
        self._cls[cls.name] = cls
      elif t == 'feat':
        ft = Feat(c)
        self.feats += [ft]
        self._fts[ft.name] = ft
      elif t == 'item':
        itm = Item(c)
        self.items += [itm]
        self._itms[itm.name] = itm
      elif t == 'monster':
        mnst = Monster(c)
        self.monsters += [mnst]
        self._mnsts[mnst.name] = mnst
      elif t == 'race':
        rc = Race(c)
        self.races += [rc]
        self._rcs[rc.name] = rc
      elif t == 'spell':
        spl = Spell(c)
        self.spells += [spl]
        self._spls[spl.name] = spl
        
  def get_background(self, name):
    if name in self._bgs:
      return self._bgs[name]
    else:
      raise NoSuchEntityError(name, 'Background')
    
  def get_class(self, name):
    if name in self._cls:
      return self._cls[name]
    else:
      raise NoSuchEntityError(name, 'Class')
    
  def get_feat(self, name):
    if name in self._fts:
      return self._fts[name]
    else:
      raise NoSuchEntityError(name, 'Feat')
    
  def get_item(self, name):
    if name in self._itms:
      return self._itms[name]
    else:
      raise NoSuchEntityError(name, 'Item')
    
  def get_monster(self, name):
    if name in self._mnsts:
      return self._mnsts[name]
    else:
      raise NoSuchEntityError(name, 'Monster')
    
  def get_race(self, name):
    if name in self._rcs:
      return self._rcs[name]
    else:
      raise NoSuchEntityError(name, 'Race')
    
  def get_spell(self, name):
    if name in self._spls:
      return self._spls[name]
    else:
      raise NoSuchEntityError(name, 'Spell')

  def print_stats(self):
    import sys
  
    print("Backgrounds: %s item(s)" % len(self.backgrounds))
    print("Classes: %s item(s)" % len(self.classes))
    print("Feats: %s item(s)" % len(self.feats))
    print("Items: %s item(s)" % len(self.items))
    print("Monsters: %s item(s)" % len(self.monsters))
    print("Races: %s item(s)" % len(self.races))
    print("Spells: %s item(s)" % len(self.spells))
    print(f"Memory Used: {sys.getsizeof(self)}")
