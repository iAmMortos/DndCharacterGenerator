import test_context

from model.data_loader import DataLoader

dl = DataLoader('data/xml/CoreOnly.xml')

for mon in dl.monsters:
  print(mon.name)
  for act in mon.actions:
    print(act)
  print('\n\n')
