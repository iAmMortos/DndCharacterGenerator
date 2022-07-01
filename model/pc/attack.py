
from model.xml_entity import XmlEntity


class Attack(XmlEntity):
  def __init__(self, xml_node):
    super().__init__(xml_node)

    self.name = self._get('name')
    self.type = self._get('type')
    self.attackBonus = self._get('attackBonus')
    self.damage = self._get('damage')
    self.damageType = self._get('damageType')

  def __repr__(self):
    return f'{self.name}: {self.type} Weapon Attack, {self.attackBonus} to hit. Hit {self.damage} {self.type} damage.'
