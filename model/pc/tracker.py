
from model.xml_entity import XmlEntity


class Tracker(XmlEntity):
  def __init__(self, xml_node):
    super().__init__(xml_node)

    self.label = self._get('label')
    self.resetType = self._get('resetType')
    self.value = self._get('value')
    self.formula = self._get('formula')
