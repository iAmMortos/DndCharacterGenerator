
from model.attribute import Attribute
from model.xml_entity import XmlEntity


class Feat (XmlEntity):
  def __init__(self, xml_node):
    super().__init__(xml_node)
    self.name = self._get('name')
    self.prerequisite = self._get('prerequisite')
    self.special = self._get('special')
    self.text = self._get('text')
    self.modifier = self._get_as_obj('modifier', Attribute)

  def __repr__(self):
    return 'Name: {0.name}\nPrerequisite: {0.prerequisite}\nSpecial: {0.special}\nModifier: {0.modifier}\n' \
           'Text: {0.text}'.format(self)
