#!/usr/bin/env python3
"""
mixed list
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    summing floats and integers
    """
    sum: float = 0
    for i in mxd_lst:
        sum = sum + i
    return sum
