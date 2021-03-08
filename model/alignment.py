
import re


class Alignment (object):
  def __init__(self, s):
    self.morality = None
    self.order = None
    self.description = None

    m = re.search(r'^(?:(Lawful|Neutral|Chaotic) (Good|Neutral|Evil)|(Unaligned|Neutral)|(.*))', s)
    gs = m.groups()
    if gs[0] is not None:
      self.order = gs[0]
      self.morality = gs[1]
      self.description = '{} {}'.format(self.order, self.morality)
    elif gs[2] == 'Neutral':
      self.order = 'Neutral'
      self.morality = 'Neutral'
      self.description = 'Neutral'
    elif gs[2] is not None:
      self.description = gs[2]
    elif gs[3] is not None:
      self.description = gs[3]

  def __repr__(self):
    return self.description
