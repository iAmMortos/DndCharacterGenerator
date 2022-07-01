
from model.pc.feat import Feat
from model.xml_entity import XmlEntity


class AutoLevel(XmlEntity):
  def __init__(self, xml_node):
    super().__init__(xml_node)

    self.level = self._get('level')
    self.scoreImprovement = self._get('scoreImprovement')
    self.slots = self._get('slots')
    self.feats = self._get_as_obj_list('feat', Feat)
    self.spellAbility = self._get('spellAbility')

