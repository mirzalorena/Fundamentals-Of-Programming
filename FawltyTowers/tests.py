'''
Created on Feb 2, 2019

@author: Lorena
'''
import unittest
from controller import *
from repo import *


class Test(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)
    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testName(self):
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()