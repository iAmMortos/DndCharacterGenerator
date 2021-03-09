
from model.xml_entity import XmlEntity
from model.action import Action
from model.attribute import Attribute


class Background (XmlEntity):
  def __init__(self, xml_node):
    super().__init__(xml_node)

    self.name = self._get('name')
    self.proficiencies = self._get_as_list('proficiency')
    self.traits = self._get_as_obj_list('trait', Action)
    self.modifiers = self._get_as_obj_list('modifier', Attribute)

  def __repr__(self):
    return 'Name: {0.name}\nProficiencies: {0.proficiencies}\nTraits: {0.traits}\nModifiers: {0.modifiers}'.format(self)
