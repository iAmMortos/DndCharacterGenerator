
from enum import Enum


class CreatureSize (Enum):
  T = 'tiny'
  S = 'small'
  M = 'medium'
  L = 'large'
  H = 'huge'
  G = 'gargantuan'

  def __str__(self):
    return self.value

  @staticmethod
  def of_value(s):
    try:
      return CreatureSize.__getitem__(s)
    except Exception as ex:
      raise ValueError("No enum value available for string [%s]" % s)
