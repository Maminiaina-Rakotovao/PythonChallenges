import unittest
import calculator

class Testaddition(unittest.TestCase):

    # Test for addition
    def test_add(self):
        self.assertEqual(calculator.add(10,5), 15)
        self.assertEqual(calculator.add(-1,1), 0)
        self.assertEqual(calculator.add(-2,-3), -5)
    
    # Test for Multiplication
    def test_mult(self):
        self.assertEqual(calculator.mult(10, 5), 50)
        self.assertEqual(calculator.mult(-1, 1), -1)
        self.assertEqual(calculator.mult(11, 0), 0)

    # Test for subtraction
    def test_sub(self):
        self.assertEqual(calculator.sub(10, 5), 5)
        self.assertEqual(calculator.sub(-1, 1), -2)
        self.assertEqual(calculator.sub(11, 0), 11)

    # Test for division
    def test_div(self):
        self.assertEqual(calculator.div(10, 5), 2)
        self.assertEqual(calculator.div(-1, 1), -1)
        self.assertEqual(calculator.div(0, 1), 0)

        # Test in case the number is divided by 0
        with self.assertRaises(ValueError):
            calculator.div(10, 0)

if __name__ == '__main__':
    unittest.main()
