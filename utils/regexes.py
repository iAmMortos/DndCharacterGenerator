
import re
from model.source import Source


def get_sources(s):
  if type(s) is not str:
    return []
  m = re.search(r'Source: ?(.*)$', s, re.MULTILINE)
  srcs = []
  if m:
    for g in m.groups():
      gs = [gr.strip() for gr in g.split(',')]
      srcs += [Source(gr) for gr in gs]
  return srcs

def get_src_abbr_str(srcs):
  return ', '.join([s.abbr for s in srcs])
  
def is_attack(s):
  m = re.match(r'^(Melee|Ranged)', s)
  return m is not None
  
def get_attack(s):
  m = re.match(r'^((?:Melee(?: or Ranged)?|Ranged) (?:Weapon|Spell|Magic(?:al)?)? ?Attack): ?(.*?)\.\s(?:Hit: ?)?([\s\S]*)', s)
  if m:
    gs = m.groups()
    atk = []
    atk += [gs[0].strip()]
    atk += [gs[1].strip()]
    atk += [gs[2].strip()]
    # if re.match(r'[0-9]', gs[2]):
    #   atk += [(gs[2] + gs[3]).strip()]
    # else:
    #   atk += [gs[3].strip()]
    return atk
  return None
