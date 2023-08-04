#!/usr/bin/env python3
"""
Duck typing - first element of a sequence
"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Retrieves the first element of a sequence if it exists.
    """
    if lst:
        return lst[0]
    else:
        return None


if __name__ == "__main__":
    print(safe_first_element.__annotations__)
