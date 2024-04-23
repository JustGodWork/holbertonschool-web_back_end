#!/usr/bin/env python3
"""
    Tasks and concurrent coroutines
"""


from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
        Asynchronous function that waits for a
        random delay between 0 and max_delay
    """
    delays = []
    for _ in range(n):
        delays.append(await task_wait_random(max_delay))
    return sorted(delays)
