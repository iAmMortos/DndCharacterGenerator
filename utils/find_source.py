
import re


def find_source(s):
  m = re.search(r'Source: ?(.*)(?:, ?(.*)){0,}\n', s)
  return None if not m else m.groups()
