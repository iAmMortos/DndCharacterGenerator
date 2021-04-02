
import re


def find_tables(s):
  matches = re.findall(r'^d[0-9]+ \| .*\n(?:^[0-9]+(?:-[0-9]+)? \| .*\n?){1,}', s, re.MULTILINE)
  return matches


def get_tables_for_bg(bg):
  s = '\n'.join([trait.text for trait in bg.traits])
  ts = find_tables(s)
  if len(ts) == 0:
    return []
  else:
    return ts
