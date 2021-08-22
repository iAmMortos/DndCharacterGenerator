
import math


class AbilityScore (object):
  def __init__(self, s):
    self._score = int(s)

  def __repr__(self):
    return '%s (%s%s)' % (self._score, '+' if self.bonus >= 0 else '', self.bonus)

  @property
  def score(self):
    return self._score

  @property
  def bonus(self):
    return math.floor((self._score - 10) / 2)
