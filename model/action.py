from model.xml_entity import XmlEntity
from model.attack import Attack


class Action(XmlEntity):
  def __init__(self, xml_node):
    super().__init__(xml_node)
    self.name = self._get('name')
    self.text = self._get('text')
    self.attack = self._get_as_obj('attack', Attack)
    if type(self.text) is list:
      self.text = '\n'.join(self.text)

  def __repr__(self):
    return 'Name: {0.name}\nAttack: {0.attack}\nText: {0.text}'.format(self)
