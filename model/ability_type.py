
from enum import Enum


class AbilityType (Enum):
  str = "Strength"
  dex = "Dexterity"
  con = "Constitution"
  int = "Intelligence"
  wis = "Wisdom"
  cha = "Charisma"

  def __str__(self):
    return self.str_short
    
  def __repr__(self):
    return str(self)
    
  @property
  def str_short(self):
    return self.value[:3].upper()
   
  @property 
  def str_long(self):
    return self.value
    
  @staticmethod
  def ordered_list():
    return (AbilityType.str, AbilityType.dex, AbilityType.con, AbilityType.int, AbilityType.wis, AbilityType.cha)

  @staticmethod
  def of_value(val):
    if type(val) is str:
      s = val.lower()[:3]
      try:
        return AbilityType.__getitem__(s)
      except Exception as ex:
        raise ValueError("No enum value available for string [%s]" % s)
