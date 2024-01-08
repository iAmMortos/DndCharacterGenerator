import test_context
import console
# import clipboard

import os
import sys

from model.data_loader import DataLoader
from templater.templater import Templater

console.clear()
dl = DataLoader('Complete')
# spell = dl.get_spell('Detect Magic')
# monster = dl.get_monster('Arasta')
# print('\n'.join(sorted([item.name for item in dl.items])))
item = dl.get_item('Nine Lives Stealer Longsword')
print(item)
#tmpltr = Templater('markdown')
#print(tmpltr.make(item))

