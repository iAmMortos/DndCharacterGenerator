from model.xml_entity import XmlEntity

class Character(XmlEntity):
  def __init__(self, xml_node):
    super().__init__(xml_node)
    
    self.version = self._get('version')
    self.uid = self._get('uid')
    self.name = self._get('name')
