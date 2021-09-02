
from data_test import DataTest


class TestRaces(DataTest):

  def test_race_duplicates(self):
    names = []
    dupes = []
    for r in self.data_loader.races:
      if r.name not in names:
        names += [r.name]
      else:
        dupes += [r.name]
    self.assertTrue(len(dupes) == 0, msg=f'The following race names have duplicates: [{dupes}]')
