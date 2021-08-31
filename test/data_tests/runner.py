
import unittest
import test_context
from model.data_loader import DataLoader

from test.data_tests import backgrounds
from test.data_tests import classes
from test.data_tests import feats
from test.data_tests import items
from test.data_tests import monsters
from test.data_tests import races
from test.data_tests import spells


def main():
	suite = unittest.TestSuite()
	loader = unittest.TestLoader()
	dl = DataLoader('data/xml/Complete.xml')

	suite.addTest(loader.loadTestsFromModule(backgrounds))
	suite.addTest(loader.loadTestsFromModule(classes))
	suite.addTest(loader.loadTestsFromModule(feats))
	suite.addTest(loader.loadTestsFromModule(items))
	suite.addTest(loader.loadTestsFromModule(monsters))
	suite.addTest(loader.loadTestsFromModule(races))
	suite.addTest(loader.loadTestsFromModule(spells))

	runner = unittest.TextTestRunner(verbosity=3)
	result = runner.run(suite)

if __name__ == '__main__':
	main()
