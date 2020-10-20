#!/usr/bin/env python3
"""
tasks
"""
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """create task
    Parameters
    ----------
    max_delay: int
        integer max time of delay
    Returns
    -------
    asyncio.Task
        new task
    """
    return asyncio.create_task(wait_random(max_delay))
