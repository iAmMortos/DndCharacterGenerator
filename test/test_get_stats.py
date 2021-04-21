
import test_context
from model.data_loader import DataLoader


dl = DataLoader('data/xml/Complete.xml')

for c in dl.classes:
  name = c.name
  hit = c.hit_die
  nskills = c.num_skills
  profs = c.proficiencies
  
  #print(f'{name}')
  

for r in dl.races:
  print(f'{r.name}:\n  {r.abilities}')

