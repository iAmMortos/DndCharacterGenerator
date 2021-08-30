
import unittest
import test_context
import os
from model.data_loader import DataLoader
from utils.regexes import get_sources, is_attack, get_attack


class TestMonsterSources(unittest.TestCase):

  def setUp(self) -> None:
    self.data_loader = DataLoader('data/xml/Complete.xml')
    return super().setUp()

  def test_monster_sources(self):
    for m in self.data_loader.monsters:
      self.assertTrue(len(get_sources(m.description)) > 0, msg=f'Monster [{m.name}]: no source found in description.')
      
  def test_attacks_have_text(self):
    for m in self.data_loader.monsters:
      for a in m.actions:
        if a.attack:
          self.assertTrue(a.text, msg=f'Monster [{m.name}], Attack [{a.name}] missing text')
          
  def test_attack_text_format(self):
    import re
    for m in self.data_loader.monsters:
      for a in m.actions:
        if a.attack and is_attack(a.text):
          self.assertTrue(get_attack(a.text) is not None, msg=f'Monster [{m.name}], Attack [{a.name}, {a.attack}] text is improperly formatted [{a.text}]')

  def tearDown(self) -> None:
    return super().tearDown()
