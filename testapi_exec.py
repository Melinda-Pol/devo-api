import unittest,os, HtmlTestRunner
from test_api import TestAPI
if __name__ == '__main__':
    curr_dir = os.getcwd()
    path = os.path.join(curr_dir,'output')
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=path))