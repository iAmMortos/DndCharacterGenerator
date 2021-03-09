
from model.xml_entity import XmlEntity


class AutoLevel (XmlEntity):
  def __init__(self, xml_node):
    super().__init__(xml_node)

    self.slots = self._get_as_list('slots', fn=int)
    
