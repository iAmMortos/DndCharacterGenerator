
import re


class ArmorClass (object):
  def __init__(self, s):
    m = re.search(r'^([0-9]+)(?: \((.*)\))?', s)
    gs = m.groups()
    self.value = int(gs[0])
    self.sources = []
    self.description = s
    if gs[1] is not None:
      self.sources = [e.strip() for e in gs[1].split(',')]

  def __repr__(self):
    return self.description
