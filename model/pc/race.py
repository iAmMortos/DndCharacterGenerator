
from model.pc.mod import Mod
from model.pc.feat import Feat
from model.xml_entity import XmlEntity


class Race(XmlEntity):
  def __init__(self, xml_node):
    super().__init__(xml_node)

    self.name = self._get('name')
    self.size = self._get('size')
    self.speed = self._get('speed')
    self.height = self._get('height')
    self.weight = self._get('weight')
    self.feats = self._get_as_obj_list('feat', Feat)
    self.mods = self._get_as_obj_list('mod', Mod)
