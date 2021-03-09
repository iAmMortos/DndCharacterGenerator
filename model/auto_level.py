
from model.class_feature import ClassFeature
from model.counter import Counter
from model.xml_entity import XmlEntity


class AutoLevel (XmlEntity):
  def __init__(self, xml_node):
    super().__init__(xml_node)

    attribs = self._attrib
    self.level = int(attribs['level'])
    self.score_improvement = 'scoreImprovement' in attribs and attribs['scoreImprovement'] == 'YES'

    self.slots = self._get_as_list('slots', fn=int)
    slots_attrib = self._get_attrib('slots')
    self.slots_optional = slots_attrib is not None and 'optional' in slots_attrib and slots_attrib['optional'] == 'YES'

    self.features = self._get_as_obj_list('feature', ClassFeature)
    self.counters = self._get_as_obj_list('counter', Counter)

  def __repr__(self):
    return 'Level: {0.level}\nScore Improvement: {0.score_improvement}\nSlots: {0.slots}\n' \
           'Slots are optional: {0.slots_optional}\nFeatures: {0.features}\nCounters: {0.counters}'.format(self)
