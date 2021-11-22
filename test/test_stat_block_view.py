import test_context
from model.data_loader import DataLoader
from views.stat_block import StatBlockView
import random

dl = DataLoader('CoreOnly')
m = random.choice(dl.monsters)

v = StatBlockView.load_view(m)
v.present(style='fullscreen')
