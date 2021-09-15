
from data_test import DataTest
from utils.regexes import get_sources


class TestFeats(DataTest):

  def test_feat_duplicates(self):
    names = []
    dupes = []
    for f in self.data_loader.feats:
      if f.name not in names:
        names += [f.name]
      else:
        dupes += [f.name]
    self.assertTrue(len(dupes) == 0, msg=f'{len(dupes)} feat names were duplicated: [{dupes}]')

  def test_feat_sources(self):
    missing = []
    for f in self.data_loader.feats:
      found = get_sources(f.text)
      if not found:
        missing += [f.name]
    self.assertTrue(len(missing) == 0, msg=f'{len(missing)} feats are missing source annotations: [{missing}]')
