import test_context

from model.data_loader import DataLoader

dl = DataLoader('data/xml/CoreOnly.xml')
for item in dl.items:
  pass