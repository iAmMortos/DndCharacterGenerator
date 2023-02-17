
import io
import re
import enum


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
        if key not in vars(obj):
          raise Exception(f'No such key [{key}] in object for [{obj}]')
        v = str(vars(obj)[key])
        s = m.span()
        out += text[:s[0]]
        out += v
        text = text[s[1]:]
      else:
        out += text
        break
    return out

  def subspell(self, spell, output):
    return self.subfile('views/markdown/templates/spell.md', spell)

  def substatblock(self, monster, output):
    return self.subfile('views/markdown/templates/monster.md', monster)


if __name__ == "__main__":
  import os
  import sys
  sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
  os.chdir('../..')
  from model.data_loader import DataLoader

  dl = DataLoader('Complete')
  sp = dl.get_spell('Detect Magic')

  s = Subtools()
  print(s.subspell(sp))
  pass
