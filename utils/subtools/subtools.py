
import io
import re
import enum


class UnsupportedFormatException (Exception):
  def __init__(self, fstr, typ):
    super().__init__(f'Unsupported format [{fstr}] for type [{typ}].')


class SubFormat (enum.Enum):
  markdown = "Markdown"
  html = "HTML"


class Subtools (object):
  def __init__(self):
    self.pattern = re.compile(r'\{(.*?)\}')
  
  def subfile(self, path, obj):
    text = ''
    out = ''
    with io.open(path, encoding="utf-8") as f:
      text = f.read()
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

  def subspell(self, spell, output=SubFormat.markdown):
    if output == SubFormat.markdown:
      return self.subfile('views/markdown/templates/spell.md', spell)
    raise UnsupportedFormatException(output, "spell")
    

  def substatblock(self, creature, output=SubFormat.markdown):
    if output == SubFormat.markdown:
      return self.subfile('views/markdown/templates/statblock.md', creature)
    raise UnsupportedformatException(output, "statblock")
    
  def _get_value(self, obj, attr):
    attrs = []
    if type(attr) is list:
      attrs = attr
    elif type(attr) is str:
      attrs = attr.split('.')
      
    next = attrs[0]
    if next not in vars(obj):
      raise Exception(f'No such key [{next}] in object [{obj}]')
      
    if len(attrs) == 1:
      return str(vars(obj)[next])
    else:
      o = vars(obj)[next]
      return self._get_value(o, attrs[1:])

# so we can access in console afterwards
monster = None

if __name__ == "__main__":
  import os
  import sys
  import console
  console.clear()
  
  sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
  os.chdir('../..')
  from model.data_loader import DataLoader

  dl = DataLoader('Complete')
  monster = dl.get_monster('Arasta')
  
  s = Subtools()
  print(s.substatblock(monster, SubFormat.markdown))
  
  
"""
_data
_node
name
size
type
alignment
sta_txt
armor_class
hit_points
speed
ability_scores
saves
skill
vulnerable
resist
immune
conditionImmune
senses
passive
senses_str
languages
challenge_rating
summary
description
traits
actions
reactions
legendaries
mythics
lairs
environment
sources
"""
