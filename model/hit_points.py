
import re


class HitPoints (object):
  def __init__(self, s):
    m = re.search(r'^([0-9]+)(?: \(([0-9]+)d([0-9]+)(?:([+-])([0-9]+))?\))?', s)
    self.hp, self._ndice, self._nsides, self._op, self._const = m.groups()
    self.hp = int(self.hp)
    if self._ndice is not None:
      self._ndice = int(self._ndice)
      self._nsides = int(self._nsides)
    if self._const is not None:
      self._const = int(self._const)
    self._text = s

  @property
  def formula(self):
    if self._ndice is not None:
      if self._op is not None:
        return '{0._ndice}d{0._nsides} {0._op} {0._const}'.format(self)
      else:
        return '{0._ndice}d{0._nsides}'.format(self)
    return None

  def __repr__(self):
    if self.formula is not None:
      return '{0.hp} ({0.formula})'.format(self)
    else:
      return '{0.hp}'.format(self)
