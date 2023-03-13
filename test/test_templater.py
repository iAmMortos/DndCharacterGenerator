import test_context
# import console
# import clipboard

import os
import sys

# import console
# console.clear()

from model.data_loader import DataLoader
from templater.templater import Templater, OutputFormats

dl = DataLoader('Complete')
# spell = dl.get_spell('Detect Magic')
monster = dl.get_monster('Arasta')
tmpltr = Templater(OutputFormats.md)

# print(tmpltr.make(spell))
# print('\n\n\n##########\n\n\n')
# console.clear()
t = tmpltr.make(monster)
print(t)
# clipboard.set(t)
# print('\n\nValue copied to clipboard.')
