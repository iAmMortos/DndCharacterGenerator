
import re
from model.source import Source


def find_sources(s):
  if type(s) is not str:
    return None
  m = re.search(r'Source: ?(.*)$', s, re.MULTILINE)
  srcs = []
  if m:
    for g in m.groups():
      gs = [gr.strip() for gr in g.split(',')]
      srcs += [Source(gr) for gr in gs]
  return srcs
