
from data_test import DataTest
from utils.regexes import get_sources


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

  def test_race_sources(self):
    missing = []
    for r in self.data_loader.races:
      for t in r.traits:
        if t.name == 'Description':
          found = get_sources(t.text)
      if not found:
        missing += [r.name]
    self.assertTrue(len(missing) == 0, msg=f'The following races are missing source annotations: [{missing}]')
