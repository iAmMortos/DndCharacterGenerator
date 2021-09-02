
from data_test import DataTest


class TestFeats(DataTest):

  def test_feat_duplicates(self):
    names = []
    dupes = []
    for f in self.data_loader.feats:
      if f.name not in names:
        names += [f.name]
      else:
        dupes += [f.name]
    self.assertTrue(len(dupes) == 0, msg=f'The following feat names were duplicated: [{dupes}]')
