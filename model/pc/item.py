
from model.pc.mod import Mod
from model.xml_entity import XmlEntity


class Item(XmlEntity):
  def __init__(self, xml_node):
    super().__init__(xml_node)

    self.name = self._get('name')
    self.detail = self._get('detail')
    self.text = self._get('text')
    self.type = self._get('type')
    self.slot = self._get('slot')
    self.quantity = self._get('quantity')
    self.value = self._get('value')
    self.weight = self._get('weight')
    self.ac = self._get('ac')
    self.damage1H = self._get('damage1H')
    self.damageType = self._get('damageType')
    self.weaponProperty = self._get('weaponProperty')
    self.weaponRange = self._get('weaponRange')
    self.weaponLongRange = self._get('weaponLongRange')
    self.mods = self._get_as_obj_list('mod', Mod)
