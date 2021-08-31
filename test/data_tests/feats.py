
import unittest
from model.data_loader import DataLoader


class TestFeats(unittest.TestCase):

  @classmethod
  def setUpClass(cls) -> None:
    super().setUpClass()
    cls.data_loader = DataLoader('data/xml/Complete.xml')
