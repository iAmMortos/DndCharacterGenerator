
from utils.regexes import get_sources
from data_test import DataTest


class TestClasses(DataTest):

  def test_class_duplicates(self):
    names = []
    dupes = []
    for cl in self.data_loader.classes:
      if cl.name not in names:
        names += [cl.name]
      else:
        dupes += [cl.name]
    self.assertTrue(len(dupes) == 0, msg=f'The following class names were duplicated: {dupes}.')

  def test_class_sources(self):
    missing = []
    for cl in self.data_loader.classes:
      found = None
      for al in cl.auto_levels:
        if al.level == 1:
          for f in al.features:
            s = f.name if type(f.name) is str else "".join(f.name)
            if s.startswith('Starting'):
              found = get_sources(''.join(f.text))
              break
      if not found:
        missing += [cl.name]
    self.assertTrue(len(missing) == 0, msg=f'The following classes are missing source annotations: [{missing}]')
