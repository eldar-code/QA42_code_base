def add(a: float, b: float) -> float:
    return a + b


def sub(a: float, b: float) -> float:
    return a - b


def mul(a: float, b: float) -> float:
    return a * b


def div(a: float, b: float) -> float:
    return a / b


def get_avg(*values: float):
    """get values and return the average """
    total = 0
    for val in values:
        total += val
    return total / len(values)


class Calculator:
    def __init__(self):
        self.result = 0.0

    def add(self, val):
        self.result += val

    def sub(self, val):
        self.result += val

    def mul(self, val):
        self.result += val

    def div(self, val):
        self.result += val

    def clear(self):
        self.result = 0.0
