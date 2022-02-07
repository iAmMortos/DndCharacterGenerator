from model.xml_entity import XmlEntity
from model.attack import Attack


class Action(XmlEntity):
  def __init__(self, xml_node):
    super().__init__(xml_node)
    self.name = self._get('name')
    self.text = self._get('text', default_value='')
    self.attack = self._get_as_obj('attack', Attack)
    if type(self.text) is list:
      self.text = '\n'.join(self.text)

  def __repr__(self):
    parts = []
    if self.name:
      parts += [f'Name: {self.name}']
    if self.attack:
      parts += [f'Attack: {self.attack}']
    if self.text:
      parts += [f'Text: {self.text}']
    return '\t'.join(parts)
