
from model.xml_entity import XmlEntity


class ImageRef(XmlEntity):
  def __init__(self, xml_node):
    super().__init__(xml_node)

    self.uid = self._get('uid')
