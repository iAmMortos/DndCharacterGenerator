import test_context
import re

from model.data_loader import DataLoader

dl = DataLoader('data/xml/CoreOnly.xml')

for mon in dl.monsters:
  for atype in [mon.traits, mon.actions, mon.reactions, mon.legendaries]:
    for act in atype:
      if act.attack is not None:
        print(act.attack)
