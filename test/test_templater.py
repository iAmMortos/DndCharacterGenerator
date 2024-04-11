import test_context
# import console
# import clipboard

import os
import sys
import io

from model.data_loader import DataLoader
from templater.templater import Templater

# console.clear()
dl = DataLoader('Complete')


def test_template_spells():
  tmpltr = Templater('markdown')
  # os.chdir('E:\\Users\\Taylor\\Documents\\Obsidian\\oathbreaker-dm\\share\\Spells')
  print(os.getcwd())
  for spell in dl.spells:
    if 'PHB' in [src.abbr for src in spell.sources]:
      pass


def write_mm_monsters():
  tmpltr = Templater('markdown')
  os.chdir('E:\\Users\\Taylor\\Documents\\Obsidian\\oathbreaker-dm\\share\\Creatures\\MM')
  existing_mons = os.listdir()
  # spell = dl.get_spell('Detect Magic')
  for monster in dl.monsters:
    if 'MM' in  [src.abbr for src in monster.sources] and f'{monster.name}.md' not in existing_mons:
      print(f'Writing {monster.name}.md...')
      mon_out = tmpltr.make(monster)
      with io.open(f'{monster.name}.md', 'w', encoding='utf-8') as f:
        f.write(mon_out)
        
        
def test_template_monster():
  tmpltr = Templater('markdown')
  gob = dl.get_monster('Goblin')
  gob_md = tmpltr.make(gob)
  print(gob_md)


if __name__ == '__main__':
  test_template_monster()

