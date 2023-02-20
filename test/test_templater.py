import test_context

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
print(tmpltr.make(monster))
