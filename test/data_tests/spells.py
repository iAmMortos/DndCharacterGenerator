
from data_test import DataTest
from utils.regexes import get_sources


class TestSpells(DataTest):

  def test_spell_duplicates(self):
    names = []
    dupes = []
    for s in self.data_loader.spells:
      if s.name not in names:
        names += [s.name]
      else:
        dupes += [s.name]
    self.assertTrue(len(dupes) == 0, msg=f'{len(dupes)} Spells have duplicate names: [{dupes}]')

  def test_spell_sources(self):
    missing = []
    for s in self.data_loader.spells:
      found = get_sources(s.text)
      if not found:
        missing += [s.name]
    self.assertTrue(len(missing) == 0, msg=f'{len(missing)} Spells are missing source annotations: [{missing}]')
