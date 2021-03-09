
from enum import Enum

from model.roll import Roll
from model.ability_type import AbilityType
from model.auto_level import AutoLevel
from model.xml_entity import XmlEntity


class RestType (Enum):
  S = "short rest"
  L = "long rest"

  def __str__(self):
    return self.value

  @staticmethod
  def of_value(val):
    try:
      return RestType.__getitem__(val)
    except Exception as ex:
      raise ValueError("No enum value available for string [%s]" % val)


class CharClass (XmlEntity):
  def __init__(self, xml_node):
    super().__init__(xml_node)

    self.name = self._get('name')
    self.hit_die = self._get_as_obj('hd', int)
    self.proficiencies = self._get_as_list('proficiency')
    self.num_skills = self._get_as_obj('numSkills', int)
    self.armor = self._get('armor')
    self.weapons = self._get('weapons')
    self.tools = self._get('tools')
    self.wealth = self._get_as_obj('wealth', Roll)
    self.spell_ability = self._get_as_obj('spellAbility', AbilityType.of_value)
    self.slots_reset = self._get_as_obj('slotReset', RestType.of_value)
    self.auto_levels = self._get_as_obj_list('autolevel', AutoLevel)

  def __repr__(self):
    return ''.format(self)