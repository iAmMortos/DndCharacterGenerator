
import unittest



class TestMonsterSources(unittest.TestCase):

  def setUp(self) -> None:
    import os
    import test_context
    raise Exception(os.getcwd())
    from model.data_loader import DataLoader
    from utils.find_source import find_sources

    self.data_loader = DataLoader('data/xml/Complete.xml')
    return super().setUp()

  def test_monster_sources(self):
    for m in self.data_loader.monsters:
      unittest.TestCase.assertTrue(len(find_sources(m.description)) > 0)

  def tearDown(self) -> None:
    return super().tearDown()
