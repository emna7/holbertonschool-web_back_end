#!/usr/bin/env python3
"""
Duck typing
"""


from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Augment element
    """
    if lst:
        return lst[0]
    else:
        return None
