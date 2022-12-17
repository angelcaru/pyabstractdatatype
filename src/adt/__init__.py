"""Abstract Data Types for Python
TODO: write the damn thing
"""
from typing import get_type_hints, Tuple, List

__all__ = ["adt"]

def _make_arg_getter(n: int, arg_type: type) -> property:    
    @property
    def arg_getter(self) -> arg_type:
        return self._Variant__vargs[n]
    
    return arg_getter

def adt(cls):
    """Decorator responsible for creating ADT's
    """

    variants: List[type] = []
    for name, user_args in get_type_hints(cls).items():
        if isinstance(user_args, type):
            user_args = (user_args,) # Turn `(int)` into `(int,)`
        
        class Variant(cls):
            __match_args__ = tuple(f"arg{n}" for n in range(len(user_args)))
            __args = user_args
            __vargs: Tuple[user_args]

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
            
            @property
            def args(self):
                return self.__vargs

        for n, arg_type in enumerate(user_args):
            property_name = f"arg{n}"

            setattr(Variant, property_name, _make_arg_getter(n, arg_type))

        Variant.__name__ = name
        setattr(cls, name, Variant)
        variants.append(Variant)
    
    cls.variants = variants

    return cls
