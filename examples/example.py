from adt import ADT

@ADT
class Operation:
    Add = (int, int)
    Subtract = (int, int)
    Multiply = (int, int)
    Divide = (int, int)
    Negate = (int)

    def calculate(self) -> int:
        Add, Subtract, Multiply, Divide, Negate = Operation.variants
        match self:
            case Add(a, b):
                return a + b
            case Subtract(a, b):
                return a - b
            case Multiply(a, b):
                return a * b
            case Divide(a, b):
                return a // b
            case Negate(x):
                return -x

def main():
    Add, Subtract, Multiply, Divide, Negate = Operation.variants

    op1 = Add(34, 35)
    op2 = Subtract(100, 31)
    op3 = Multiply(23, 3)
    op4 = Divide(207, 3)
    op5 = Negate(-69)

    ops = op1, op2, op3, op4, op5

    for op in ops:
        print(op.calculate())

if __name__ == "__main__":
    pass