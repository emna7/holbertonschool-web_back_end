#!/us/bin/env python3
"""
complex types
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    return tuple
    """
    element: float = v * v
    tuple = (k, element)
    return tuple
