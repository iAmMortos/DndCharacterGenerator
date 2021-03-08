
from model.roll import Roll


class Attack(object):
  def __init__(self, s):
    ps = s.split('|')
    self.label = ps[0]
    self.bonus = int(ps[1]) if ps[1] != '' else 0
    self.roll = Roll(ps[2])

  def __repr__(self):
    return '{0.label} ({1}{0.bonus} to hit) Roll: {0.roll}'.format(self, '+' if self.bonus >= 0 else '')
