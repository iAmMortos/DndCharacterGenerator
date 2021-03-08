
import re


class CreatureType (object):
  def __init__(self, s):
    m = re.search(r'^([^( ]*)(?: \((.*)\))?', s)
    self.type = m.groups()[0]
    self.subtype = m.groups()[1]

  def __repr__(self):
    return '{}{}{}'.format(self.type, ' ' if self.subtype is not None else '', ('(%s)' % self.subtype) if self.subtype is not None else '')
