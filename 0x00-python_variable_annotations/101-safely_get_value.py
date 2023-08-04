#!/usr/bin/env python3
"""
More involved type annotations
"""
from typing import Mapping, Any, TypeVar, Union


T = TypeVar('T')
Res = Union[Any, T]
Def = Union[T, None]

def safely_get_value(dct: Mapping[Any, T], key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Retrieves a value from a dict using a given key.
    """
    if key in dct:
        return dct[key]
    else:
        return default



if __name__ == "__main__":
    annotations = safely_get_value.__annotations__

    print("Here's what the mappings should look like")
    for k, v in annotations.items():
        print(("{}: {}".format(k, v)))
