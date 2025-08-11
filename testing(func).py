import unittest
from cw22 import *

class My_test(unittest.TestCase):

    def test_args(self):
        self.assertEqual(add(2,2),4)

    def test_kwargs(self):
        self.assertEqual(add(c = 1, a = 2),3)

    def test_mixed(self):
        self.assertEqual(add(10,a=11),21)

    def test_diff(self):
        y = 10
        x = 0
        self.assertEqual(add(0,-5,y,a=x),5)

    def test_wrong(self):
        self.assertEqual(add('5','abc',10),15)


if __name__ == "__main__":
    unittest.main()


