import unittest
from Calc2 import add, subtract

class test2(unittest.TestCase):
    def test_add(self):
        result = add(10, 5)
        self.assertEqual(result, 15)

    def test_subtract(self):
        result = subtract(10, 5)
        self.assertEqual(result, 5)

unittest.main()