
from model.pc.container_item import ContainerItem
from model.xml_entity import XmlEntity


class Container(XmlEntity):
  def __init__(self, xml_node):
    super().__init__(xml_node)

    self.label = self._get('label')
    self.name = self._get('name')
    self.value = self._get('value')
    self.weight = self._get('weight')
    self.carried = self._get('carried')
    self.items = self._get_as_obj_list('item', ContainerItem)
