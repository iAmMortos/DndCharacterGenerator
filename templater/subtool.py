
import io
import re
import enum


class SubFormat (enum.Enum):
  markdown = "Markdown"
  html = "HTML"


class SubTemplates (enum.Enum):
  proficiencies = 'Proficiencies'
  spell = 'Spell'
  statblock = 'Statblock'


class Subtool (object):
  def __init__(self):
    self.pattern = re.compile(r'{(.*?)}')
  
  def sub(self, text, obj):
    out = ''
    while True:
      m = re.search(self.pattern, text)
      if m is not None:
        key = m.group(1)
        v = self._get_value(obj, key)
        s = m.span()
        out += text[:s[0]]
        out += v
        text = text[s[1]:]
      else:
        out += text
        break
    return out

  def _get_value(self, obj, attr):
    attrs = []
    if type(attr) is list:
      attrs = attr
    elif type(attr) is str:
      attrs = attr.split('.')
      
    nxt = attrs[0]
    if nxt not in vars(obj):
      raise Exception(f'No such key [{nxt}] in object [{obj}]')
      
    if len(attrs) == 1:
      return str(vars(obj)[nxt])
    else:
      o = vars(obj)[nxt]
      return self._get_value(o, attrs[1:])
