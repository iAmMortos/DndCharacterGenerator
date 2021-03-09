import test_context
import re

from model.data_loader import DataLoader
from utils.find_source import find_source

dl = DataLoader('data/xml/CoreOnly.xml')

# print('\n'.join(sorted([race.name for race in dl.races])))

sources = []
for race in dl.races:
  s = '\n'.join([t.text for t in race.traits])
  # print(s)
  src = find_source(s)
  if src is not None:
    sources += [src]
  else:
    print("Race: {0.name} - No source detected".format(race))
for monster in dl.monsters:
  s = monster.description
  src = find_source(s)
  if src is not None:
    sources += [src]
  else:
    print("Monster: {0.name} - No source detected".format(monster))
for spell in dl.spells:
  s = spell.text
  if type(s) is list:
    s = '\n'.join(s)
  src = find_source(s)
  if src is not None:
    sources += [src]
  else:
    print("Spell: {0.name} - No source detected".format(spell))
for feat in dl.feats:
  s = feat.text
  if type(s) is list:
    s = '\n'.join(s)
  src = find_source(s)
  if src is not None:
    sources += [src]
  else:
    print("Feat: {0.name} - No source detected".format(feat))
for item in dl.items:
  s = item.text
  if type(s) is list:
    s = '\n'.join(s)
  src = find_source(s)
  if src is not None:
    sources += [src]
  else:
    print("Item: {0.name} - No source detected".format(item))
for cls in dl.classes:
  for al in cls.auto_levels:
    s = '\n'.join(['\n'.join(f.text) for f in al.features])
    src = find_source(s)
    if src is not None:
      sources += [src]
    else:
      pass
      # print('Class: {0.name}, Auto-Level: {1.level} - No source detected\nAuto-Level Features: {1.features}'.format(cls, al))
for bg in dl.backgrounds:
  s = '\n'.join(['\n'.join([t.text for t in bg.traits]) for bg in dl.backgrounds])
  src = find_source(s)
  if src is not None:
    sources += [src]
  else:
    print('Background: {0.name} - No source detected'.format(bg))



print(len(sources))
dl.print_stats()
# prints memory usage in mb
# import os, psutil
# print(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2)
