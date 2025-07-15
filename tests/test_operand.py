import unittest
from app.domain.value_object.operand import Operand

class TestOperand(unittest.TestCase):
    def test_valid_operand(self):
        self.assertEqual(float(Operand('3')), 3.0)
        self.assertEqual(float(Operand(2.5)), 2.5)
        self.assertEqual(float(Operand('-1.2')), -1.2)

    def test_invalid_operand(self):
        with self.assertRaises(ValueError):
            Operand('abc')
        with self.assertRaises(ValueError):
            Operand(None)

    def test_str(self):
        self.assertEqual(str(Operand('5')), '5.0')

if __name__ == '__main__':
    unittest.main() 