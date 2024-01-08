import test_context
# import console
# import clipboard

import os
import sys
import io

from model.data_loader import DataLoader
from templater.templater import Templater

tmpltr = Templater('markdown')

# console.clear()
dl = DataLoader('Complete')

os.chdir('E:\\Users\\Taylor\\Documents\\Obsidian\\oathbreaker-dm\\share\\Creatures\\MM')
existing_mons = os.listdir()
# spell = dl.get_spell('Detect Magic')
for monster in dl.monsters:
  if 'MM' in  [src.abbr for src in monster.sources] and f'{monster.name}.md' not in existing_mons:
    print(f'Writing {monster.name}.md...')
    mon_out = tmpltr.make(monster)
    with io.open(f'{monster.name}.md', 'w', encoding='utf-8') as f:
      f.write(mon_out)
# print('\n'.join(sorted([item.name for item in dl.items])))
# item = dl.get_item('Nine Lives Stealer Longsword')

