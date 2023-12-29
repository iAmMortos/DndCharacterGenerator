
import io
import re
import enum

from templater.template_token import TemplateToken
from templater.subtemplates import SubTemplates


class SubFormat (enum.Enum):
  markdown = "Markdown"
  html = "HTML"


class Subtool (object):
  def __init__(self):
    self.pattern = re.compile(r'{(.*?)}')
  
  def sub(self, text, obj):
    out = []
    objs = []
    repeating = False
    if type(obj) is list:
      objs = obj
    else:
      objs = [obj]

    for o in objs:
      tmptext = text[:]
      while True:
        m = re.search(self.pattern, tmptext)
        if m is not None:
          key = m.group(1)
          token = TemplateToken(key)
          s = m.span()
          self._sub_append(out, tmptext[:s[0]])
          if not token.template:  # if it's not a nested template, resolve and append the string value now
            v = self._get_value(o, token.obj)
            if v:
              self._sub_append(out, f'{token.prefix}{str(v)}{token.suffix}')
            elif not v and token.optline:
              # If there's a newline at the end of the previous section, remove it
              if len(out) > 0 and type(out[-1]) is str and out[-1][-1] == '\n':
                out[-1] = out[-1][:-1]
              # If a newline wasn't found before, try to remove one after
              elif tmptext[s[1]] == '\n':
                tmptext = tmptext[:s[1]] + tmptext[s[1]+1:]
          else:  # if it is a nested template leave the token with appropriate information for a later parsing pass
            if token.obj == 'this':
              token.obj = o
            else:
              token.obj = self._get_value(o, token.obj)
            self._sub_append(out, token)
            # just deposit token object in out list and return to templater
          tmptext = tmptext[s[1]:]
        else:
          self._sub_append(out, tmptext)
          break

    # if the output list no longer contains tokens (and is just a single string),
    #   return just the string. Otherwise return the list of output objects
    if len(out) == 1 and type(out[0]) is str:
      return out[0]
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
      return vars(obj)[nxt]
    else:
      o = vars(obj)[nxt]
      return self._get_value(o, attrs[1:])

  def _sub_append(self, group, obj):
    if len(group) == 0:
      group.append(obj)
    else:
      if type(obj) is str and type(group[-1]) is str:
        group[-1] += obj
      else:
        group.append(obj)