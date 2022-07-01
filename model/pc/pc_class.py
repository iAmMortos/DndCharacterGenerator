
from model.pc.autolevel import AutoLevel
from model.pc.class_feat import ClassFeat
from model.pc.spell import Spell
from model.xml_entity import XmlEntity


class Class(XmlEntity):
  def __init__(self, xml_node):
    super().__init__(xml_node)

    self.id = self._get('id')
    self.name = self._get('name')
    self.level = self._get('level')
    self.hd = self._get('hd')
    self.hdCurrent = self._get('hdCurrent')
    self.wealth = self._get('wealth')
    self.proficiencies = self._get('proficiency')
    self.numClassSkills = self._get('numClassSkills')
    self.armor = self._get('armor')
    self.weapons = self._get('weapons')
    self.tools = self._get('tools')
    self.slots = self._get('slots')
    self.slotsCurrent = self._get('slotsCurrent')
    self.feats = self._get_as_obj_list('feat', ClassFeat)
    self.autolevels = self._get_as_obj_list('autolevel', AutoLevel)
    self.spells = self._get_as_obj_list('spell', Spell)
