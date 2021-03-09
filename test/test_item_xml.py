import test_context
import re

from model.data_loader import DataLoader

dl = DataLoader('data/xml/CoreOnly.xml')

# prints memory usage in mb
import os, psutil
print(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2)
