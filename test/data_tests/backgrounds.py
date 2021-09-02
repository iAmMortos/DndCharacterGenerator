
from data_test import DataTest
from utils.regexes import get_sources


class TestBackgrounds(DataTest):

  def test_background_duplicates(self):
    names = []
    dupes = []
    for b in self.data_loader.backgrounds:
      if b.name in names:
        dupes += [b.name]
      else:
        names += [b.name]
      self.assertTrue(len(dupes) == 0, msg=f'The following background names are duplicated: [{dupes}]')

  def test_backgrounds_have_source(self):
    for b in self.data_loader.backgrounds:
      found = False
      for t in b.traits:
        if t.name == 'Description':
          if get_sources(t.text):
            found = True
            break
      self.assertTrue(found, msg=f'Background [{b.name}] has no source in description.')
