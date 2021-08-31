
import unittest
from model.data_loader import DataLoader


class TestClasses(unittest.TestCase):

  @classmethod
  def setUpClass(cls) -> None:
    super().setUpClass()
    cls.data_loader = DataLoader('data/xml/Complete.xml')
