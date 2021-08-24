
import unittest

import monster

loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTest(loader.loadTestsFromModule(monster))

runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)
