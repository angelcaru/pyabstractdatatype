#!/bin/env python3

from adt import adt

@adt
class Op:
    Add: (int, int)
    Subtract: (int, int)
    Multiply: (int, int)
    Divide: (int, int)
    Negate: (int)

    def calculate(self) -> int:
        match self:
            case Op.Add(a, b):
                return a + b
            case Op.Subtract(a, b):
                return a - b
            case Op.Multiply(a, b):
                return a * b
            case Op.Divide(a, b):
                return a // b
            case Op.Negate(x):
                return -x

def main():
    op1 = Op.Add(34, 35)
    op2 = Op.Subtract(100, 31)
    op3 = Op.Multiply(23, 3)
    op4 = Op.Divide(207, 3)
    op5 = Op.Negate(-69)

    ops = op1, op2, op3, op4, op5

    for op in ops:
        print(f"{op} = {op.calculate()}")
    
    print()
    
    assert Op.Add(1, 1) == Op.Add(1, 1)
    assert Op.Add(1, 1) != Op.Add(1, 2)
    assert Op.Divide(1, 1) != Op.Add(1, 1)
    assert Op.Add(1, 5) != Op.Negate(1)

    # Should raise error (Op is immutable)
    op1.arg0 = 1

    print(f"{op1} = {op1.calculate()}")

if __name__ == "__main__":
    main()