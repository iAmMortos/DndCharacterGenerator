
from data_test import DataTest
from utils.regexes import get_sources


class TestItems(DataTest):

  def test_item_duplicates(self):
    names = []
    dupes = []
    for i in self.data_loader.items:
      if i.name in names:
        dupes += [i.name]
      else:
        names += [i.name]
    self.assertTrue(len(dupes) == 0, msg=f'The following item names were duplicated: [{dupes}]')

  def test_item_sources(self):
    missing = []
    for i in self.data_loader.items:
      found = get_sources(i.text)
      if not found:
        missing += [i.name]
    self.assertTrue(len(missing) == 0, msg=f'The following items are missing source annotations: [{missing}]')
