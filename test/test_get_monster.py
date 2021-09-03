
import test_context
from model.data_loader import DataLoader


name = 'Undead Spirit'

dl = DataLoader('data/xml/Complete.xml')
for m in dl.monsters:
  if m.name == name:
    print('\n\n'.join([str(a) for a in m.actions]))

