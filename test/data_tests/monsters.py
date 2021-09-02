
from data_test import DataTest
from utils.regexes import get_sources, is_attack, get_attack


class TestMonsters(DataTest):

  def test_monster_duplicates(self):
    names = []
    dupes = []
    for m in self.data_loader.monsters:
      if m.name not in names:
        names += [m.name]
      else:
        dupes += [m.name]
    self.assertTrue(len(dupes) == 0, msg=f'The following monster names are duplicated: [{dupes}]')


  def test_monster_sources(self):
    for m in self.data_loader.monsters:
      self.assertTrue(len(get_sources(m.description)) > 0, msg=f'Monster [{m.name}]: no source found in description.')

  def test_all_actions_have_text(self):
    for m in self.data_loader.monsters:
      for a in m.actions:
        self.assertTrue(a.text is not None, msg=f'Monster actions found without any text: Monster [{m.name}: {m.sources}], action: [{a}].')
      
  def test_attacks_have_text(self):
    for m in self.data_loader.monsters:
      for a in m.actions:
        if a.attack:
          self.assertTrue(a.text is not None and a.text.strip() != '', msg=f'Monster [{m.name}], Attack [{a.name}] missing text')
          
  def test_attack_text_format(self):
    import re
    for m in self.data_loader.monsters:
      for a in m.actions:
        if a.attack and is_attack(a.text):
          self.assertTrue(get_attack(a.text) is not None, msg=f'\nMonster: [{m.name}]\nAttack: [{a.name}, {a.attack}]\nText is improperly formatted:\n[{a.text}]')
