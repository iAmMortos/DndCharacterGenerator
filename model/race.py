
from model.ability_type import AbilityType
from model.ability_bonuses import AbilityBonuses
from model.creature_size import CreatureSize
from model.action import Action
from model.attribute import Attribute
from model.xml_entity import XmlEntity


class Race (XmlEntity):
  def __init__(self, xml_node):
    super().__init__(xml_node)

    self.name = self._get('name')
    self.abilities = self._get_as_obj('ability', AbilityBonuses)
    self.size = self._get_as_obj('size', CreatureSize.of_value)
    self.speed = self._get_as_obj('speed', int)
    self.spellAbility = self._get_as_obj('spellAbility', AbilityType.of_value)
    self.proficiencies = self._get_as_list('proficiency')
    self.traits = self._get_as_obj_list('trait', Action)
    self.modifiers = self._get_as_obj_list('modifier', Attribute)

  def __repr__(self):
    return 'Name: {0.name}\nAbility Bonuses: {0.abilities}\nSize: {0.size}\n' \
           'Speed: {0.speed}\nSpell Ability: {0.spellAbility}\nProficiencies: {0.proficiencies}\n' \
           'Traits: {0.traits}\nModifiers: {0.modifiers}'.format(self)
