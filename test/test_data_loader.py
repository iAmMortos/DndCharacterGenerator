import test_context

from model.data_loader import DataLoader

dl = DataLoader('data/xml/CoreOnly.xml')
dl.print_stats()

from utils.find_source import find_sources
for m in dl.monsters:
  if m.actions:
    print(m.actions)
