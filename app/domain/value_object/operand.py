class Operand:
    def __init__(self, value):
        try:
            self.value = float(value)
        except (ValueError, TypeError):
            raise ValueError(f"数値として解釈できません: {value}")

    def __float__(self):
        return self.value

    def __str__(self):
        return str(self.value)
