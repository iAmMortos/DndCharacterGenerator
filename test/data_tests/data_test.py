
import unittest
import test_context
from model.data_loader import DataLoader
from test.data_tests.data_loader_singleton import DataLoaderSingleton

class DataTest(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    super().setUpClass()
    cls.data_loader = DataLoaderSingleton.instance()
