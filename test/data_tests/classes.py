
from utils.regexes import get_sources
from data_test import DataTest


class TestClasses(DataTest):
  
  def test_classes_have_source(self):
    for cl in self.data_loader.classes:
      found = None
      for al in cl.auto_levels:
        if al.level == 1:
          for f in al.features:
            s = f.name if type(f.name) is str else "".join(f.name)
            if s.startswith('Starting'):
              found = get_sources(''.join(f.text))
              break
      self.assertTrue(found, msg=f'No source found for class [{cl.name}]')

  def test_class_duplicates(self):
    names = []
    dupes = []
    for cl in self.data_loader.classes:
      if cl.name not in names:
        names += [cl.name]
      else:
        dupes += [cl.name]
    self.assertTrue(len(dupes) == 0, msg=f'The following class names were duplicated: {dupes}.')
