
from model.xml_entity import XmlEntity


class Spell(XmlEntity):
  def __init__(self, xml_node):
    super().__init__(xml_node)

    self.name = self._get('name')
    self.school = self._get('school')
    self.ritual = self._get_as_bool('ritual')
    self.level = self._get('level')
    self.time = self._get('time')
    self.range = self._get('range')
    self.v = self._get_as_bool('v')
    self.s = self._get_as_bool('s')
    self.m = self._get_as_bool('m')
    self.materials = self._get('materials')
    self.duration = self._get('duration')
    self.text = self._get('text')
    self.sclass = self._get('sclass')
    self.roll = self._get('roll')
