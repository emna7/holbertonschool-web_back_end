#!/usr/bin/env python3
"""
execute multiple coroutines at the same time
"""
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """return the delay values
    Parameters
    ----------
    n: int
        number of times that wait_random
    max_delay: int
    Returns
    -------
    List[float]
    """
    my_list = []
    for i in range(n):
        my_list.append(await task_wait_random(max_delay))

    return my_list
