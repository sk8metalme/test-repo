import unittest
from app.domain.value_object.operator import Operator

class TestOperator(unittest.TestCase):
    def test_valid_operators(self):
        for op in ['+', '-', '*', '/']:
            operator = Operator(op)
            self.assertEqual(str(operator), op)

    def test_invalid_operator(self):
        with self.assertRaises(ValueError):
            Operator('%')

    def test_equality(self):
        self.assertEqual(Operator('+'), Operator('+'))
        self.assertNotEqual(Operator('+'), Operator('-'))

    def test_not_equal_to_other_type(self):
        self.assertNotEqual(Operator('+'), '+')

if __name__ == '__main__':
    unittest.main() 