import unittest
from app.domain.calculator_entity import CalculatorEntity
from app.domain.value_object.operand import Operand
from app.domain.value_object.operator import Operator

class TestCalculatorEntity(unittest.TestCase):
    def setUp(self):
        self.calc = CalculatorEntity()

    def test_add(self):
        self.assertEqual(self.calc.calculate(Operand(1), Operand(2), Operator('+')), 3.0)

    def test_subtract(self):
        self.assertEqual(self.calc.calculate(Operand(5), Operand(3), Operator('-')), 2.0)

    def test_multiply(self):
        self.assertEqual(self.calc.calculate(Operand(2), Operand(4), Operator('*')), 8.0)

    def test_divide(self):
        self.assertEqual(self.calc.calculate(Operand(8), Operand(2), Operator('/')), 4.0)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.calculate(Operand(1), Operand(0), Operator('/'))

    def test_invalid_operator(self):
        class DummyOperator:
            symbol = '^'
        with self.assertRaises(ValueError):
            self.calc.calculate(Operand(1), Operand(2), DummyOperator())

if __name__ == '__main__':
    unittest.main() 