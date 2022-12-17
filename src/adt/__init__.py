"""Abstract Data Types for Python

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
"""
from typing import get_type_hints, Tuple, List

__all__ = ["adt"]

def _make_arg_getter(n: int, arg_type: type) -> property:    
    def arg_getter(self) -> arg_type:
        return self._Variant__vargs[n]
    
    return property(arg_getter)

_variant_id = 0

def adt(cls):
    """Decorator responsible for creating ADT's
    """
    global _variant_id

    variants: List[type] = []
    for name, user_args in get_type_hints(cls).items():
        if isinstance(user_args, type):
            user_args = (user_args,) # Turn `(int)` into `(int,)`
        
        class Variant(cls):
            __match_args__ = tuple(f"arg{n}" for n in range(len(user_args)))
            __args = user_args
            __vargs: Tuple[user_args]
            __variant_id: int = _variant_id

            def __init__(self, *vargs):
                args = type(self).__args
                if len(vargs) != len(args):
                    message = f"{type(self).__name__}() takes {len(args)} argument{'s' if len(args) != 1 else ''} but {len(vargs)} were given"
                    raise TypeError(message)

                self.__vargs = vargs

                cls.__init__(self)
            
            def __repr__(self) -> str:
                inside_parens = ", ".join(map(str, self.__vargs))
                return f"{type(self).__name__}({inside_parens})"

            def __hash__(self) -> int:
                return hash(self.__vargs + (self.__variant_id,))
            
            def __eq__(self, other) -> bool:
                if isinstance(other, cls):
                    return hash(self) == hash(other)
                return self is other
            
            def __ne__(self, other) -> bool:
                return not (self == other)

            @property
            def args(self):
                return self.__vargs

        for n, arg_type in enumerate(user_args):
            property_name = f"arg{n}"

            setattr(Variant, property_name, _make_arg_getter(n, arg_type))

        Variant.__name__ = name
        setattr(cls, name, Variant)
        variants.append(Variant)

        _variant_id += 1
    
    cls.variants = variants

    return cls
