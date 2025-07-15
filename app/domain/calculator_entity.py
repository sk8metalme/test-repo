from app.domain.value_object.operand import Operand
from app.domain.value_object.operator import Operator

class CalculatorEntity:
    def calculate(self, left: Operand, right: Operand, operator: Operator) -> float:
        if operator.symbol == '+':
            return float(left) + float(right)
        elif operator.symbol == '-':
            return float(left) - float(right)
        elif operator.symbol == '*':
            return float(left) * float(right)
        elif operator.symbol == '/':
            if float(right) == 0:
                raise ZeroDivisionError("0で割ることはできません")
            return float(left) / float(right)
        else:
            raise ValueError(f"未対応の演算子です: {operator.symbol}")
