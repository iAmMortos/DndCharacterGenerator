
import test_context
from utils.find_table import find_tables, get_tables_for_bg
from utils.find_source import find_source
from model.data_loader import DataLoader
from model.die_table import DieTable


import console
console.clear()
dl = DataLoader('data/xml/CoreOnly.xml')

# with open('data/background_traits.csv', 'w') as f:
ss = []
for bg in dl.backgrounds:
  s = '\n'.join([t.text for t in bg.traits])
  ss += [find_source(s)]
  tbls = get_tables_for_bg(bg)
  for tbl in tbls:
    dt = DieTable(tbl)
    #print('{0.name}: {0.die} - {1}'.format(dt, dt.roll()))
  #print('\n\n')
print(ss)
