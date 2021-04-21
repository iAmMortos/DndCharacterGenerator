
from model.ability_type import AbilityType


class AbilityBonuses (object):
  def __init__(self, s):
    self.bonuses = {}
    parts = [p.strip() for p in s.split(',')]
    for part in parts:
      score, val = part.split(' ')
      score = AbilityType.of_value(score)
      val = int(val)
      self.bonuses[score] = val

  def __repr__(self):
    sparts = []
    for t in AbilityType.ordered_list():
      if t in self.bonuses:
        v = self.bonuses[t]
        sparts.append('{} {}{}'.format(t.str_short, '+' if v >= 0 else '', v))
    return ', '.join(sparts)
