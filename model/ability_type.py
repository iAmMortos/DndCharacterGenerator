
from enum import Enum


class AbilityType (Enum):
  str = "Strength"
  dex = "Dexterity"
  con = "Constitution"
  int = "Intelligence"
  wis = "Wisdom"
  cha = "Charisma"

  def __str__(self):
    return self.value

  @staticmethod
  def of_value(val):
    if type(val) is str:
      s = val.lower()[:3]
      try:
        return AbilityType.__getitem__(s)
      except Exception as ex:
        raise ValueError("No enum value available for string [%s]" % s)
