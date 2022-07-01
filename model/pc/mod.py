
from model.xml_entity import XmlEntity


class Mod(XmlEntity):
  def __init__(self, xml_node):
    super().__init__(xml_node)

    self.category = self._get('category')
    self.type = self._get('type')
    self.value = self._get('value')
