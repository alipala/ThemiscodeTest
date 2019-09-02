from Tests.test_home import TestHome
from Tests.test_login import TestLogin
import unittest

loader = unittest.TestLoader()
suite =unittest.TestSuite()

# suite.addTests(loader.loadTestsFromModule(TestLogin))
suite.addTests(loader.loadTestsFromModule(TestHome))

runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)
