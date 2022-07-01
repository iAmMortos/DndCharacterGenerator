
from model.pc.mod import Mod
from model.xml_entity import XmlEntity


class ClassFeat(XmlEntity):
  def __init__(self, xml_node):
    super().__init__(xml_node)

    self.name = self._get('name')
    self.text = self._get('text')
    self.expanded = self._get_as_bool('expanded', True)
    self.mod = self._get_as_obj_list('mod', Mod)
    self.optional = self._get_as_bool('optional', True)
