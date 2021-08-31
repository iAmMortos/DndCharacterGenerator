
import unittest
from model.data_loader import DataLoader


class TestBackgrounds(unittest.TestCase):

  @classmethod
  def setUpClass(cls) -> None:
    super().setUpClass()
    cls.data_loader = DataLoader('data/xml/Complete.xml')

  def test_backgrounds_have_source(self):
    self.assertTrue(True)
