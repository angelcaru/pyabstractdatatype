# PyAbstractDataType
A simple library that adds [ADTs](https://en.wikipedia.org/wiki/Abstract_data_type) to Python.

[Source Code](https://github.com/angelcaru/pyabstractdatatype/blob/main/src/adt/__init__.py)

## Documentation
Basic usage:
```python
from adt import adt

@adt
class MyADT:
    Variant1: (int, int)
    Variant2: (int)
    Variant3: (str, str, list[float])
```

Supports `match` statement!
```python
obj1 = MyADT.Variant1(2, 2)
obj2 = MyADT.Variant3("hi", "foo", [2.3, 5.6, 3.1415])

objs = obj1, obj2

for obj in objs:
    match obj1:
        case MyADT.Variant1(a, b):
            print(f"Found you! {a}, {b}")
        case MyADT.Variant2(x):
            print(":(")
        case _:
            raise ValueError("wtf")
```

Output:
```python
Found you! 2, 2
Traceback (most recent call last):
...
ValueError: wtf
```

## Examples
See [example.py](https://github.com/angelcaru/pyabstractdatatype/blob/main/example.py).
