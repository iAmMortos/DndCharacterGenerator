
import test_context
from utils.find_table import find_tables, get_tables_for_bg
from utils.find_source import find_source
from model.data_loader import DataLoader
from model.die_table import DieTable


# for each background in the loader, get
# the tables, roll them, and print results
dl = DataLoader('data/xml/CoreOnly.xml')

for bg in dl.backgrounds:
  tbls = get_tables_for_bg(bg)
  print("Found %s tables for %s" % (len(tbls), bg.name))
  d_tables = []
  for tbl in tbls:
    dt = DieTable(tbl)
    d_tables += [dt]
    print('{0.name}: {0.die} - {1}'.format(dt, dt.roll()))
  print('\n\n')
