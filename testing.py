import unittest
from cw22 import *



class Test_calculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculate()

    def test_add(self):
        self.assertEqual(self.calc.add(2,3),5)
        self.assertEqual(self.calc.add(2,3.5),5.5)
        self.assertEqual(self.calc.add(2,'4'),6)
        self.assertEqual(self.calc.add(x=1,y=2),3)
        self.assertEqual(self.calc.add('a',2),2)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10,4),6)

    def test_mult(self):
        self.assertEqual(self.calc.mult(4,5),20)

    def test_divide(self):
        self.assertEqual(self.calc.div(10, 2), 5)
        with self.assertRaises(ZeroDivisionError):
            self.calc.div(5, 0)

    def test_exponent(self):
        self.assertEqual(self.calc.exp(2, 3), 8)
        self.assertEqual(self.calc.exp(5, 0), 1)

if __name__ == "__main__":
    unittest.main()