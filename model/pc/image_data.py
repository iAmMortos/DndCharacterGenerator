
from model.xml_entity import XmlEntity
from utils import image_utils


class ImageData(XmlEntity):
  def __init__(self, xml_node):
    super().__init__(xml_node)
    
    self.uid = self._get('uid')
    self.encoded = str.encode(self._get('encoded'))

  def as_img(self):
    return image_utils.bytestr_to_img(self.encoded)
