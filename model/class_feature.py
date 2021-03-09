
from model.xml_entity import XmlEntity


class ClassFeature(XmlEntity):
  def __init__(self, xml_node):
    super().__init__(xml_node)

    self.name = self._get('name')
    self.text = self._get('text')
    attr = self._attrib
    self.optional = 'optional' in attr and attr['optional'] == 'YES'

  def __repr__(self):
    return 'Name: {0.name}\nText: {0.text}\nOptional: {0.optional}'.format(self)
