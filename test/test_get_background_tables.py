
import test_context
from utils.find_table import find_tables, get_tables_for_bg
from utils.regexes import get_sources
from utils.data_file_loader import DataFileLoader as DFL
from model.data_loader import DataLoader
from model.die_table import DieTable
import io


# import console
# console.clear()
dfl = DFL()
dl = DataLoader('CoreOnly')
sources = {}

lines = dfl.load_csv('sources')
for line in lines:
  sources[line[0]] = line[1]

lines = []
for bg in dl.backgrounds:
  ss = get_sources('\n'.join([t.text for t in bg.traits]))[8:]
  srcs = []
  for s in [s.strip() for s in ss.split(',')]:
    srcs += [s.split(' p. ')[0]]
  keys = []
  for src in srcs:
    for k,v in sources.items():
      if v == src:
        keys += [k]
  tbls = get_tables_for_bg(bg)
  for tbl in tbls:
    dt = DieTable(tbl)
    d = dt.die
    n = dt.name
    for v in dt.values:
      lines += ['{}\t{}\t{}\t{}\t{}'.format(bg.name, n, d, '|'.join(v), '/'.join(keys))]

with io.open('data/background_traits.csv', mode='w', encoding='utf-8') as f:
  f.write('\n'.join(lines))

    #print('{0.name}: {0.die} - {1}'.format(dt, dt.roll()))
  #print('\n\n')
