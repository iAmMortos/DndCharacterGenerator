
import test_context
from utils.find_table import find_tables, get_tables_for_bg
from utils.find_source import find_source
from model.data_loader import DataLoader
from model.die_table import DieTable


dl = DataLoader('data/xml/CoreOnly.xml')

background = 'Folk Hero'

for bg in dl.backgrounds:
  if bg.name == background:
    tbls = get_tables_for_bg(bg)
    print("Found %s tables for %s" % (len(tbls), background))
    d_tables = []
    for tbl in tbls:
      dt = DieTable(tbl)
      d_tables += [dt]
      print(dt, end='\n\n\n')
    break
