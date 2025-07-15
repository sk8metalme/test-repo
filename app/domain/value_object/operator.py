class Operator:
    SUPPORTED_OPERATORS = {'+', '-', '*', '/'}

    def __init__(self, symbol: str):
        if symbol not in self.SUPPORTED_OPERATORS:
            raise ValueError(f"未対応の演算子です: {symbol}")
        self.symbol = symbol

    def __eq__(self, other):
        if not isinstance(other, Operator):
            return False
        return self.symbol == other.symbol

    def __str__(self):
        return self.symbol
