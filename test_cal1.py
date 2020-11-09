import unittest
import Calcul1

class testCalc(unittest.TestCase):

    def test_multiply(self):
        result = Calcul1.multiply(2,3)
        self.assertEqual(result, 6) 
    
    def test_divide(self):
        result = Calcul1.divide(6,3)
        self.assertEqual(result, 2) 


if __name__ == "--main--":
    unittest.main()