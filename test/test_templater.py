import test_context
# import console

import os
import sys

# import console
# console.clear()

from model.data_loader import DataLoader
from templater.templater import Templater, OutputFormats

dl = DataLoader('Complete')
# spell = dl.get_spell('Detect Magic')
monster = dl.get_monster('Knight')
tmpltr = Templater(OutputFormats.md)

# print(tmpltr.make(spell))
# print('\n\n\n##########\n\n\n')
# console.clear()
print(tmpltr.make(monster))
