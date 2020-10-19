#!/usr/bin/env python3
"""
complex types
"""


from typing import Callable
def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """multiply multiplier by float
    """
    return lambda a: a * multiplier
