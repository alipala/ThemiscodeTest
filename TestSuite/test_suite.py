import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from Tests.test_home import TestHome
from Tests.test_login import TestLogin
from Tests.test_home_welcome import TestHomeWelcome
from Tests.test_lawsuit import TestLawsuit
from Tests.test_case_details import TestCaseDetails
import unittest


loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTest(loader.loadTestsFromModule(TestCaseDetails))
suite.addTest(loader.loadTestsFromModule(TestLawsuit))
suite.addTest(loader.loadTestsFromModule(TestHomeWelcome))
suite.addTests(loader.loadTestsFromModule(TestHome))
suite.addTests(loader.loadTestsFromModule(TestLogin))


runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)
