
import re
from model.source import Source


def get_sources(s):
  if type(s) is not str:
    return None
  m = re.search(r'Source: ?(.*)$', s, re.MULTILINE)
  srcs = []
  if m:
    for g in m.groups():
      gs = [gr.strip() for gr in g.split(',')]
      srcs += [Source(gr) for gr in gs]
  return srcs
  
def is_attack(s):
  m = re.match(r'^(Melee|Ranged)', s)
  return m is not None
  
def get_attack(s):
  m = re.match(r'^(Melee( or Ranged)?|Ranged) ?(Weapon|Spell|Magical)? Attack', s)
  if m:
    return m.groups()
  return None
