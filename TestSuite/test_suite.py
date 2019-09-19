import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from Tests.test_1_login import TestLogin
from Tests.test_2_home import TestHome
from Tests.test_3_home_welcome import TestHomeWelcome
from Tests.test_4_lawsuit import TestLawsuit
from Tests.test_5_case_details import TestCaseDetails
import unittest


loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTest(loader.loadTestsFromModule(TestLogin))
suite.addTest(loader.loadTestsFromModule(TestHome))
suite.addTest(loader.loadTestsFromModule(TestHomeWelcome))
suite.addTest(loader.loadTestsFromModule(TestLawsuit))
suite.addTest(loader.loadTestsFromModule(TestCaseDetails))

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=3)
    result = runner.run(suite)
