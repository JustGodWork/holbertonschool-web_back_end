#!/usr/bin/env python3
"""
    Concurrent coroutines
"""


from typing import List
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
        Wait for a random delay between 0 and max_delay
    """
    delays = []
    tasks = []

    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)

    for task in tasks:
        delay = await task
        delays.append(delay)

    return sorted(delays)
