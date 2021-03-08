import test_context
import re

from model.data_loader import DataLoader

dl = DataLoader('data/xml/CoreOnly.xml')

for mon in dl.monsters:
  for atype in [mon.traits, mon.actions, mon.reactions, mon.legendaries]:
    for act in atype:
      if type(act.text) is list:
        t = ''
        for at in act.text:
          if at is not None:
            t += at
      elif act.text is not None:
        t = act.text
      if t:
        m = re.search(r'[0-9]+d[0-9]+', t)
        if m and act.attack is None:
          print('{}: {}'.format(mon.name, act.name))
