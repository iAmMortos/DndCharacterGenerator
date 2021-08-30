
import test_context
from model.data_loader import DataLoader
from utils.regexes import get_sources


dl = DataLoader('data/xml/CoreOnly.xml')

classes = sorted(dl.classes, key=lambda cls: cls.name)

for c in classes:
  name = c.name
  hit = c.hit_die
  nskills = c.num_skills
  profs = c.proficiencies
  print(f'{name}')
  

races = sorted(dl.races, key=lambda race: race.name)

# for r in races:
#   print(f'{r.name}\n  {", ".join([sa.abbr for sa in r.sources])}')

print(f'Num Classes: {len(dl.classes)}')
print(f'Num Races: {len(dl.races)}')

