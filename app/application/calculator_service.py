from app.domain.value_object.operand import Operand
from app.domain.value_object.operator import Operator
from app.domain.calculator_entity import CalculatorEntity

class CalculatorService:
    def __init__(self):
        self.calculator = CalculatorEntity()

    def execute(self, left: str, right: str, operator: str) -> float:
        left_operand = Operand(left)
        right_operand = Operand(right)
        op = Operator(operator)
        return self.calculator.calculate(left_operand, right_operand, op)
