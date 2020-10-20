#!/usr/bin/env python3
"""
Measure the runtime
"""
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measures the total execution time for wait()
    Parameters
    ----------
    n: int
        number of times
    max_delay: int
        waiting time
    Returns
    -------
    float
        the total execution time
    """
    s = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.perf_counter() - s
    return total_time / n
