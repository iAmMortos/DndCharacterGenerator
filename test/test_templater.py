import test_context
import console
import clipboard

import os
import sys

from model.data_loader import DataLoader
from templater.templater import Templater, OutputFormats

dl = DataLoader('Complete')
# spell = dl.get_spell('Detect Magic')
monster = dl.get_monster('Oni')
tmpltr = Templater(OutputFormats.md)

# print(tmpltr.make(spell))
# print('\n\n\n##########\n\n\n')
console.clear()
t = tmpltr.make(monster)
print(t)
clipboard.set(t)
print('\n\nValue copied to clipboard.')


#success = 0
#fail = 0
#total = len(dl.monsters)
#failures = []

#for i,m in enumerate(dl.monsters):
#  try:
#    tmpltr.make(m)
#    success += 1
#  except Exception as ex:
#    fail += 1
#    if type(ex) not in failures:
#      failures += [type(ex)]
#  print(f'Success: {success}/{i+1} ({success/(i+1)*100}%) of total {total}')
#print(f'Failed Monsters: {failures}')

