
import io
from utils.data_file_loader import DataFileLoader as DFL


class Source(object):
  def __init__(self, s):
    pp = s.split('p.')
    self.src = None
    self.abbr = None
    self.p = None
    if len(pp) > 1:
      self.src = pp[0].strip()
      self.p = pp[1].strip()
    else:
      self.src = pp[0]
    self.abbr = self.lookup(self.src)


  def lookup(self, s):
    for line in DFL().load_csv('sources'):
      if line[1] == s or line[2] == s:
        return line[0]
    return None

  def get_abbr(self):
    return f'{self.abbr}{"" if self.p is None else f" (p. {self.p})"}'


  def __repr__(self):
    return f'{self.src}{"" if self.p is None else f" (p. {self.p})"}'
