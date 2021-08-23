import test_context

from model.data_loader import DataLoader
import io

dl = DataLoader('data/xml/Complete.xml')
dl.print_stats()

with io.open('just_attacks.txt', 'w', encoding='utf-8') as f:
  from utils.find_source import find_sources
  for m in dl.monsters:
    # f.write(f'# {m.name} {find_sources(m.description)}\n')
    for a in m.actions:
      if a.attack:
        if 'Melee' in a.text or 'Ranged' in a.text:
          n = a.name
          t = a.text.replace('\n', '\\n')
          # f.write(f'\t{a}\n\t{t}\n')
          f.write(f'{t}\n')
