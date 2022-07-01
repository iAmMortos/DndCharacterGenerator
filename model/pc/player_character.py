
from model.xml_entity import XmlEntity
from model.pc.character import Character
from model.pc.image_data import ImageData

class PlayerCharacter (XmlEntity):
  def __init__(self, xml_node):
    super().__init__(xml_node)
    
    self.character = self._get_as_obj('character', Character)
    self.imageData = self._get_as_obj('imageData', ImageData)
