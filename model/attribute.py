
from enum import Enum


class AttributeCategory (Enum):
  bonus = "bonus"
  ability_score = "ability score"
  ability_modifier = "ability modifier"
  saving_throw = "saving throw"
  skill = "skill"


class Attribute(object):
  def __init__(self, s):
    self.s = s

  def __repr__(self):
    return s

