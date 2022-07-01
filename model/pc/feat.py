
from model.xml_entity import XmlEntity

class Feat(XmlEntity):
  def __init__(self, xml_node):
    super().__init__(xml_node)
    
    self.name = self._get('name')
    self.text = self._get('text')
    self.expanded = self._get_as_boolean('expanded', True)
