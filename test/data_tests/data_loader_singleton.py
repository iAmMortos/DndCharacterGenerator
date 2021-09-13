
import test_context
from utils.singleton import Singleton
from model.data_loader import DataLoader


@Singleton
class DataLoaderSingleton(object):
  def __init__(self):
    self.dl = DataLoader('data/xml/Complete.xml')