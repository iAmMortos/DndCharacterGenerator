
from model.xml_entity import XmlEntity

class ImageData(XmlEntity):
  def __init__(self, xml_node):
    super().__init__(xml_node)
    
    self.uid = self._get('uid')
    self.encoded = self._get_as_bool('encoded', False)
