
from data_test import DataTest


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
