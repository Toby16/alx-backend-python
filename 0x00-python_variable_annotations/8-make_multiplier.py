#!/usr/bin/env python3
"""
Complex types - functions
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Creates a multiplier function
    """
    def multiplier_function(x: float) -> float:
        return x * multiplier
    return multiplier_function


if __name__ == "__main__":
    make_multiplier = __import__('8-make_multiplier').make_multiplier
    print(make_multiplier.__annotations__)
    fun = make_multiplier(2.22)
    print("{}".format(fun(2.22)))
