
from model.xml_entity import XmlEntity


class ContainerItem(XmlEntity):
  def __init__(self, xml_node):
    super().__init__(xml_node)

    self.name = self._get('name')
    self.text = self._get('text')
    self.quantity = self._get('quantity')
    self.weight = self._get('weight')
