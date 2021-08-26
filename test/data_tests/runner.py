
import unittest

import monster

def main():
	loader = unittest.TestLoader()
	suite = unittest.TestSuite()

	suite.addTest(loader.loadTestsFromModule(monster))

	runner = unittest.TextTestRunner(verbosity=3)
	result = runner.run(suite)

if __name__ == '__main__':
	main()