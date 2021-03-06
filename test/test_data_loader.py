import test_context

from model.data_loader import DataLoader

dl = DataLoader('data/CoreOnly.xml')
for c in dl.data['class']:
  print(c.getchildren())
