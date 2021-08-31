import test_context

from model.data_loader import DataLoader

dl = DataLoader('data/xml/Complete.xml')
# dl.print_stats()

from utils.regexes import is_attack
import re

for mn in dl.monsters:
  m = dl.monsters[mn]
  for a in m.actions:
    if is_attack(a.text) and len(re.findall(r'Hit:', a.text)) > 1:
      print(f'{m.name}')
      print(f'  {a.name}: {a.text}')