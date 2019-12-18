import unittest
from checkoverlaplines import checkTwoLinesOverlap as cl

class TestClassCheckOverLapLines(unittest.TestCase):
    def test_linesOverlapp(self):
        firstline = (1,5)
        secondline = (2,6)
        self.assertTrue(cl.linesOverlapp(firstline, secondline))
        print(" \n In test_linesOverlapp()")