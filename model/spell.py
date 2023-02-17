
from enum import Enum
from model.range import Range
from model.roll import Roll
from model.xml_entity import XmlEntity
from utils.ordinals import get_ord_str
import re


# TODO: Flesh out class
class Duration(object):
  def __init__(self, s):
    self.s = s

  def __repr__(self):
    return self.s


class Components(object):
  def __init__(self, s):
    m = re.search(r'^(V?)(?:, )?(S?)(?:, )?(M \(.*\))?', s)
    gs = m.groups()

    self.verbal = gs[0] == 'V'
    self.somatic = gs[1] == 'S'
    self.material = gs[2][3:-1] if gs[2] is not None else None

  def __repr__(self):
    s = ''
    if self.verbal:
      s = 'V'
    if self.somatic:
      if s:
        s += ', '
      s += 'S'
    if self.material:
      if s:
        s += ', '
      s += f'M ({self.material})'
    return s


class CastTime(object):
  def __init__(self, s):
    ps = s.split(' ')
    self.value = int(ps[0])
    self.units = ' '.join(ps[1:])

  def __repr__(self):
    return '%s %s' % (self.value, self.units)


class MagicSchools(Enum):
  A = 'Abjuration'
  C = 'Conjuration'
  D = 'Divination'
  EN = 'Enchantment'
  EV = 'Evocation'
  I = 'Illusion'
  N = 'Necromancy'
  T = 'Transmutation'

  def __str__(self):
    return self.value

  @staticmethod
  def of_value(s):
    try:
      return MagicSchools.__getitem__(s)
    except Exception as ex:
      raise ValueError("No enum value available for string [%s]" % s)


class Spell (XmlEntity):
  def __init__(self, xml_node):
    super().__init__(xml_node)
    self.name = self._get('name', '')
    self.level = self._get_as_obj('level', int, -1)
    self.school = self._get_as_obj('school', MagicSchools.of_value, None)
    self.ritual = self._get_as_bool('ritual', False)
    self.slr_txt = self._build_school_level_ritual_text()
    self.time = self._get_as_obj('time', CastTime, None)
    self.range = self._get_as_obj('range', Range, None)
    self.components = self._get_as_obj('components', Components, None)
    self.duration = self._get_as_obj('duration', Duration, None)
    self.text = self._get('text', '')
    self.roll = self._get_as_obj('roll', Roll, None)
    self.classes = self._get_as_list('classes')

  def _build_school_level_ritual_text(self):
    s = ''
    if self.level == 0:
      s = f'{self.school} cantrip'
    else:
      s = f'{get_ord_str(self.level)}-level {str(self.school).lower()}'

    if self.ritual:
      s += ' (ritual)'

    return s

  def get_book_str(self):
    s = f'{self.name}\n' \
        f'{self.slr_txt}\n' \
        f'Casting Time: {self.time}\n' \
        f'Range: {self.range}\n' \
        f'Component: {str(self.components)}\n' \
        f'Duration: {self.duration}\n' \
        f'{self.text}'
    return s

  def __repr__(self):
    return f'Spell: {self.name}'
    # return 'Spell Name: {0.name}\nLevel: {0.level}\nSchool: {0.school}\nRitual: {0.ritual}\nTime: {0.time}\n' \
    #        'Range: {0.range}\nComponents: {0.components}\nDuration: {0.duration}\nRoll: {0.roll}\n' \
    #        'Classes: {0.classes}\nText: {0.text}'.format(self)
