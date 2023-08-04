#!/usr/bin/python3
"""
Duck typing - first element of a sequence
"""
from typing import Any, List, Union


def safe_first_element(lst: List[Any]) -> Union[Any, None]:
    """
    Retrieves the first element of a sequence if it exists.
    """
    if lst:
        return lst[0]
    else:
        return None


if __name__ == "__main__":
    print(safe_first_element.__annotations__)
