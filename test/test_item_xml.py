import test_context
import re

from model.data_loader import DataLoader
from utils.find_source import find_source

dl = DataLoader('data/xml/CoreOnly.xml')

# print('\n'.join(sorted([race.name for race in dl.races])))

for race in dl.races:
  print('Race: {0.name}'.format(race))
  s = '\n'.join([t.text for t in race.traits])
  # print(s)
  print(find_source(s))

# prints memory usage in mb
# import os, psutil
# print(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2)
