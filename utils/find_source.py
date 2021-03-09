
import re


def find_source(s):
  m = re.search(r'^Source: ?(.*)$', s, re.MULTILINE)
  return None if not m else m.group()
