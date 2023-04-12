import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def test_add(self):
        calculator = Calculator()
        self.assertEqual(calculator.add(2, 3), 5)
        
    def test_add_2(self):
        calculator = Calculator()
        self.assertEqual(calculator.add(-2, 3), 1)
        
        
    def test_add_3(self):
        calculator = Calculator()
        self.assertEqual(calculator.add(-4, 3), -1)

    def test_subtract(self):
        calculator = Calculator()
        self.assertEqual(calculator.subtract(2, 3), -1)


    def test_subtract_2(self):
        calculator = Calculator()
        self.assertEqual(calculator.subtract(-2, 3), -5)


    def test_subtract_3(self):
        calculator = Calculator()
        self.assertEqual(calculator.subtract(-4, -5), 1)
        

    def test_multiply(self):
        calculator = Calculator()
        self.assertEqual(calculator.multiply(2, 3), 6)
        self.assertEqual(calculator.multiply(-2, 3), -6)
        self.assertEqual(calculator.multiply(-5, -3), 15)
    # Exception handling as devided by zero
    def test_divide(self):
        calculator = Calculator()
        self.assertEqual(calculator.divide(6, 3), 2)
        self.assertEqual(calculator.divide(-6, 3), -2)
        self.assertRaises(ValueError, calculator.divide, 6, 0)

    def test_exponentiate(self):
        calculator = Calculator()
        self.assertEqual(calculator.exponentiate(2, 3), 8)
        self.assertEqual(calculator.exponentiate(2, 0), 1)
        self.assertEqual(calculator.exponentiate(2, -3), 0.125)

    def test_multiply_2(self):
        calculator = Calculator()
        self.assertEqual(calculator.multiply(-2, 3), -6)


    def test_divide_2(self):
        calculator = Calculator()
        self.assertEqual(calculator.divide(-6, 3), -2)


    def test_exponentiate_2(self):
        calculator = Calculator()
        self.assertEqual(calculator.exponentiate(2, 0), 1)

        
    def test_multiply_3(self):
        calculator = Calculator()
        self.assertEqual(calculator.multiply(-5, -3), 15)

    # exception handling .............
    def test_divide_3(self):
        calculator = Calculator()
        self.assertRaises(ValueError, calculator.divide, 6, 0)

    def test_exponentiate_3(self):
        calculator = Calculator()
        self.assertEqual(calculator.exponentiate(2, -3), 0.125)

if __name__ == '__main__':
    unittest.main()
