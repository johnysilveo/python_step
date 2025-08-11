import unittest
from aveargecalc import *




class Test_Average_Calc(unittest.TestCase):

    def test_avg(self):
        self.assertEqual(calculate_average([1, 2, 3, 4, 5]), 3.0)

    def test_none(self):
        self.assertIsNone(calculate_average([]))

    def test_one_number(self):
        self.assertEqual(calculate_average([2]),2.0)

    def test_float(self):
        self.assertIs(float())


if __name__ == "__main__":
    unittest.main()