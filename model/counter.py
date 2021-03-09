
from model.xml_entity import XmlEntity
from model.rest_type import RestType


class Counter (XmlEntity):
  def __init__(self, xml_node):
    super().__init__(xml_node)

    self.name = self._get('name')
    self.value = self._get_as_obj('value', int)
    self.reset = self._get_as_obj('reset', RestType.of_value)

  def __repr__(self):
    return 'Name: {0.name}\nStarting Value: {0.value}\nResets On: {0.reset}'.format(self)
