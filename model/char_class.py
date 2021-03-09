
from model.roll import Roll
from model.ability_type import AbilityType
from model.auto_level import AutoLevel
from model.xml_entity import XmlEntity
from model.attribute import Attribute
from model.rest_type import RestType


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
    self.modifiers = self._get_as_obj('modifier', Attribute)

  def __repr__(self):
    return 'Name: {0.name}\nHit Dice: {0.hit_die}\nProficiencies: {0.proficiencies}\nNum Skills: {0.num_skills}\n' \
           'Armor: {0.armor}\nWeapons: {0.weapons}\nTools: {0.tools}\nWealth: {0.wealth}\n' \
           'Spell Ability: {0.spell_ability}\nSlots Reset: {0.slots_reset}\nAuto Level Configs: {1}\n' \
           'Modifiers: {0.modifiers}'.format(self, len(self.auto_levels))
