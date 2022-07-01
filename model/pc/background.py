
from model.pc.feat import Feat
from model.xml_entity import XmlEntity


class Background(XmlEntity):
  def __init__(self, xml_node):
    super().__init__(xml_node)

    self.name = self._get('name')
    self.align = self._get('align')
    self.personality = self._get('personality')
    self.ideals = self._get('ideals')
    self.bonds = self._get('bonds')
    self.flaws = self._get('flaws')
    self.feats = self._get_as_obj_list('feat', Feat)
    self.proficiencies = self._get('proficiency')
