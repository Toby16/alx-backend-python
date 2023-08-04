#!/usr/bin/env python3
"""
Complex types - list of floats
"""


def sum_list(input_list: [float]) -> float:
    """
    function to return sum of all floats in a list
    """
    return sum(input_list)


if __name__ == "__main__":
    floats = [3.14, 1.11, 2.22]
    floats_sum = sum_list(floats)
    print(floats_sum == sum(floats))
    print(sum_list.__annotations__)
    print("sum_list(floats) returns {} which is a {}".format(floats_sum,
                                                             type(floats_sum)))
