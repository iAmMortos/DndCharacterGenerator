
from data_test import DataTest


class TestSpells(DataTest):

  def test_spell_duplicates(self):
    names = []
    dupes = []
    for s in self.data_loader.spells:
      if s.name not in names:
        names += [s.name]
      else:
        dupes += [s.name]
    self.assertTrue(len(dupes) == 0, msg=f'The following Spells have duplicate names: [{dupes}]')
