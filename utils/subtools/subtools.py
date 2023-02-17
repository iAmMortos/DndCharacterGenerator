
import io
import re


class Subtools (object):
  def __init__(self):
    self.pattern = re.compile(f'\{(.*?)\}')
  
  def subfile(self, path, obj):
    text = ''
    out = ''
    with io.open(path, encoding="utf-8") as f:
      text = f.read()
    while True:
      m = re.search(self.pattern, text)
      if m is not None:
        key = m.group(0)
        s = m.span()
        out += text[:s[0]]
        print(key)
        text = text[s[1]:]
      else:
        out += text
    return out
        
