
import unittest
import test_context
from model.data_loader import DataLoader

class DataTest(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    super().setUpClass()
    cls.data_loader = DataLoader('data/xml/Complete.xml')
