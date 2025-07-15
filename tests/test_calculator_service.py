import unittest
from app.application.calculator_service import CalculatorService

class TestCalculatorService(unittest.TestCase):
    def setUp(self):
        self.service = CalculatorService()

    def test_execute_add(self):
        self.assertEqual(self.service.execute('1', '2', '+'), 3.0)

    def test_execute_subtract(self):
        self.assertEqual(self.service.execute('5', '3', '-'), 2.0)

    def test_execute_multiply(self):
        self.assertEqual(self.service.execute('2', '4', '*'), 8.0)

    def test_execute_divide(self):
        self.assertEqual(self.service.execute('8', '2', '/'), 4.0)

    def test_execute_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.service.execute('1', '0', '/')

    def test_invalid_operand(self):
        with self.assertRaises(ValueError):
            self.service.execute('a', '2', '+')

    def test_invalid_operator(self):
        with self.assertRaises(ValueError):
            self.service.execute('1', '2', '%')

if __name__ == '__main__':
    unittest.main() 